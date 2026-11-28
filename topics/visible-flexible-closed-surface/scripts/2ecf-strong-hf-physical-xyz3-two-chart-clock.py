#!/usr/bin/env python3
"""Two material coordinates on the actual three-step physical HF64 XYZ shape and frozen g."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import time
from fractions import Fraction as F
from pathlib import Path
for k in ('MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import linprog

ORD=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))


def load(p,name):
    z=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(z);z.loader.exec_module(m);return m


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class HarmonicSpline:
    def __init__(self,knots,coef,freq,parity):
        self.freq=np.asarray(freq)
        self.parity=np.asarray(parity)
        self.coef=np.asarray(coef)
        self.B=BSpline(knots,np.pad(self.coef,[(3,3)]+[(0,0)]*(self.coef.ndim-1)),5,extrapolate=False)
    def angular(self,u):
        a=u[...,None]*self.freq+self.parity
        return [np.cos(a),-self.freq*np.sin(a),-self.freq**2*np.cos(a)]
    def jets(self,s,u):
        w=self.angular(u);z=[self.B(s,k) for k in range(3)]
        return [np.einsum('nk,nk...->n...',w[j],z[i]) for i,j in ORD]


def chain(j,P,Q):
    X,Vs,Vu,Vss,Vsu,Vuu=j
    _,ps,pu,pss,psu,puu=P;_,qs,qu,qss,qsu,quu=Q
    v=lambda a:a[...,None]
    return [X,v(ps)*Vs+v(qs)*Vu,v(pu)*Vs+v(qu)*Vu,
        v(ps**2)*Vss+v(2*ps*qs)*Vsu+v(qs**2)*Vuu+v(pss)*Vs+v(qss)*Vu,
        v(ps*pu)*Vss+v(ps*qu+pu*qs)*Vsu+v(qs*qu)*Vuu+v(psu)*Vs+v(qsu)*Vu,
        v(pu**2)*Vss+v(2*pu*qu)*Vsu+v(qu**2)*Vuu+v(puu)*Vs+v(quu)*Vu]


class Physical:
    def __init__(self,a,clockmod):
        self.a=a;data=np.load(a.field)
        self.t=data['knots'];self.coeff=data['coefficients']
        self.alpha=BSpline(data['alphaKnots'],np.pad(data['alpha'],(3,3)),5,extrapolate=False)
        co=json.loads(a.clock.read_bytes());st=json.loads(a.state.read_bytes())
        if co['fieldSHA256']!=sha(a.field) or sha(a.state)!='bf6fcb21bd1ff8ee830c3e6e054667bface063c1d7486171355d003e20a4b0d5':
            raise ValueError('Use the actual physical own3 and original HF clock')
        B=st['modelDefinition']['basis'];self.gid=st['modelDefinition']['frozenTargetDefinitionSHA256']
        if not np.array_equal(B['physicalKnots'],data['Wknots']) or B['dimension']!=6615:raise ValueError('Physical 45-by-147 space mismatch')
        f=np.r_[0,np.repeat(np.arange(1,25),2)]
        self.xyz=[]
        self.xyzfreq=f
        for c in [data['physicalW'],np.asarray(st['z']).reshape(45,147)]:
            self.xyz.append(BSpline(data['Wknots'],np.pad(c.reshape(45,3,49).transpose(0,2,1),((3,3),(0,0),(0,0))),5,extrapolate=False))
        self.outer=HarmonicSpline(co['radialKnots'],np.array(co['coefficients']).reshape(-1,len(co['angularModes'])),co['angularModes'],0.) if 'angularModes' in co else HarmonicSpline(co['radialKnots'],np.array(co['coefficients']).reshape(-1,5),np.arange(5)*2,0.)
        raw=load(a.scripts/'6a65-geometry-nonfold-polar-connector.py','hf_twoclock_native')
        self.source=raw.NonfoldPolarConnector(a.scripts,a.ramp,a.coast)
        self.mat=clockmod.Field.__init__
        self.poly=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
            [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])
    def xyzvalues(self,i,s,u):
        n=np.arange(1,25);ang=n*u[:,None];cc=np.cos(ang);sn=np.sin(ang)
        w=np.empty((3,len(u),49));w[0,:,0]=1;w[1:,:,0]=0
        w[0,:,1::2]=cc;w[0,:,2::2]=sn;w[1,:,1::2]=-n*sn;w[1,:,2::2]=n*cc;w[2,:,1::2]=-n*n*cc;w[2,:,2::2]=-n*n*sn
        z=[self.xyz[i](s,k) for k in range(3)]
        return [np.einsum('nk,nkd->nd',w[j],z[k]) for k,j in ORD]
    def curve(self,index,w):
        if index in (0,len(self.t)-1):
            v=self.source.providers[int(index>0)](w)
            return np.stack([np.stack([v[z+'u'*o] for z in ('P','V','A')],axis=1) for o in range(3)],axis=1)
        m=np.arange(self.coeff.shape[2]);ph=np.exp(1j*w[:,None]*m)
        cc=self.coeff[index].transpose(1,0,2).reshape(len(m),9)
        return np.stack([(ph*(1j*m)**o)@cc for o in range(3)],axis=1).real.reshape(len(w),3,3,3)
    def hf(self,s,u):
        # For each ring precompute all actual endpoint functions once on its own angle vector.
        idx=np.clip(np.searchsorted(self.t,s,side='right')-1,0,len(self.t)-2)
        h=self.t[idx+1]-self.t[idx];t=(s-self.t[idx])/h
        ports=np.empty((len(s),2,3,3,3))
        for side in (0,1):
            ix=idx+side
            for j in np.unique(ix):
                sel=ix==j;ports[sel,side]=self.curve(j,u[sel])
        ports=ports.transpose(0,2,1,3,4).reshape(len(s),3,6,3)
        weights=[]
        for o in range(3):
            p=np.arange(o,6);v=np.stack([t**(j-o)*(math.factorial(j)//math.factorial(j-o)) for j in p],axis=-1)
            weights.append((v@self.poly[:,p].T)*h[:,None]**(np.arange(6)%3-o))
        xyz=self.xyzvalues(0,s,u)
        return [v+np.einsum('nl,nld->nd',weights[i],ports[:,j]) for (i,j),v in zip(ORD,xyz)]
    def parent(self,s,u):
        h=self.outer.jets(s,u);P=[s+h[0],1+h[1],*h[2:]]
        scalar=np.ones_like(s);zero=np.zeros_like(s);Q=[u,zero,scalar,zero,zero,zero]
        out=chain(self.hf(np.clip(P[0],self.t[0],self.t[-1]),u),P,Q)
        return [v+w for v,w in zip(out,self.xyzvalues(1,s,u))]


class Chart:
    def __init__(self,knots,modes):
        self.knots=knots;self.n=len(knots)-12;self.radfreq=2*np.arange(modes+1);self.angfreq=2*np.arange(1,modes+1)
        self.B=BSpline(knots,np.eye(len(knots)-6)[:,3:-3],5,extrapolate=False)
    def build(self,c):
        n=len(self.radfreq);return c[:self.n*n].reshape(self.n,n),c[self.n*n:].reshape(self.n,-1)
    def factors(self,s,u):
        B=[self.B(s,i) for i in range(3)]
        a=u[:,None]*self.radfreq;v=u[:,None]*self.angfreq
        h=[np.cos(a),-self.radfreq*np.sin(a),-self.radfreq**2*np.cos(a)]
        k=[np.sin(v),self.angfreq*np.cos(v),-self.angfreq**2*np.sin(v)]
        return B,h,k
    def jets(self,s,u,c):
        h,k=self.build(c);B,C,D=self.factors(s,u)
        return ([B[i]@h@C[j].T for i,j in ORD],[B[i]@k@D[j].T for i,j in ORD])
    def orientation(self,c):
        vals=[]
        for cc,fr in zip(self.build(c),(self.radfreq,self.angfreq)):
            v=[[F(x) for x in row] for row in np.pad(cc,((3,3),(0,0)))]
            knots=list(map(F,self.knots))
            ds=max(sum(5*abs(b-a)/(knots[i+6]-knots[i+1]) for a,b in zip(v[i],v[i+1])) for i in range(len(v)-1))
            du=max(sum(int(m)*abs(x) for m,x in zip(fr,row)) for row in v)
            vals.append([ds,du])
        return vals


def eig(e,f,g):
    tr=(e+g)/2;dif=(e-g)/2;d=np.hypot(dif,f);sg=np.where(tr>=0,1.,-1.)
    v=sg*dif/np.maximum(d,1e-30);w=sg*f/np.maximum(d,1e-30)
    return abs(tr)+d,sg,(1+v)/2,w,(1-v)/2


def fit(ch,ns,u,radius,J):
    B,C,D=ch.factors(ns,u);nr,nc,nd=ch.n,len(ch.radfreq),len(ch.angfreq);N=nr*(nc+nd)
    _,V,U,A,B2,C2=J.swapaxes(0,1);dot=lambda x,y:np.sum(x*y,axis=-1)
    E,F0,G=dot(V,V),dot(V,U),dot(U,U);r=radius[:,None]
    Es,Fs,Gs=2*dot(V,A),dot(U,A)+dot(V,B2),2*dot(U,B2)
    Eu,Fu,Gu=2*dot(V,B2),dot(U,B2)+dot(V,C2),2*dot(U,C2)
    def predicted(c):
        (h,hs,hu,*_),(k,ks,ku,*_)=ch.jets(ns,u,c)
        return (E-1+Es*h+Eu*k+2*E*hs+2*F0*ks,
               (F0+Fs*h+Fu*k+F0*hs+G*ks+E*hu+F0*ku)/r,
               G/r**2-1+(Gs*h+Gu*k+2*F0*hu+2*G*ku)/r**2)
    x=np.zeros(N);cuts=[];rhs=[];history=[]
    for des,offset,lim in ((nc,0,.32),(nd,nr*nc,.36)):
        eye=np.eye(nr*des).reshape(nr*des,nr,des);p=np.pad(eye,((0,0),(3,3),(0,0)))
        der=(5*np.diff(p,axis=1)/(ch.knots[6:-1]-ch.knots[1:-6])[None,:,None]).reshape(nr*des,-1).T
        mat=np.zeros((len(der),N+1));mat[:,offset:offset+nr*des]=der
        cuts.extend([mat,-mat]);rhs.extend([np.full(len(der),lim/des)]*2)
    for step in range(15):
        er,sg,v,w,y=eig(*predicted(x));sel=[]
        for ix in np.array_split(np.arange(len(ns)),56):
            a=er[ix].ravel();ind=np.argpartition(a,-5)[-5:];sel.extend((ix[j//len(u)],j%len(u)) for j in ind)
        hot=np.argpartition(er.ravel(),-300)[-300:];sel.extend(zip(*np.unravel_index(hot,er.shape)))
        ii,jj=np.unique(sel,axis=0).T;q=lambda a:a[ii,jj];ra=radius[ii];v,w,y,sg=map(q,(v,w,y,sg))
        def block(a,b,d,tr):
            return (a[:,None,None]*B[0][ii,:,None]*tr[0][jj,None,:]+b[:,None,None]*B[1][ii,:,None]*tr[0][jj,None,:]+d[:,None,None]*B[0][ii,:,None]*tr[1][jj,None,:]).reshape(len(ii),-1)
        rs=block(v*q(Es)+w*q(Fs)/ra+y*q(Gs)/ra**2,2*v*q(E)+w*q(F0)/ra,w*q(E)/ra+2*y*q(F0)/ra**2,C)
        us=block(v*q(Eu)+w*q(Fu)/ra+y*q(Gu)/ra**2,2*v*q(F0)+w*q(G)/ra,w*q(F0)/ra+2*y*q(G)/ra**2,D)
        base=v*(q(E)-1)+w*q(F0)/ra+y*(q(G)/ra**2-1)
        cuts.append(np.c_[sg[:,None]*rs,sg[:,None]*us,-np.ones(len(ii))]);rhs.append(-sg*base)
        sol=linprog(np.r_[np.zeros(N),1.],A_ub=np.vstack(cuts),b_ub=np.concatenate(rhs),bounds=[(-.006,.006)]*(nr*nc)+[(-.012,.012)]*(nr*nd)+[(0,2)],method='highs')
        if not sol.success:raise ValueError(sol.message)
        x=sol.x[:-1];peak=eig(*predicted(x))[0].max();history.append([float(sol.x[-1]),float(peak)])
        if peak<sol.x[-1]+.0002:break
    return x,history


def run(a):
    here=Path(__file__).parent;clock=load(here/'2ecf-strong-hf-material-radial-clock.py','twoclock_orig')
    helper=load(here/'2ecf-strong-port-hermite-fourier-background-physical-W.py','twoclock_metrics')
    field=Physical(a,clock);o=clock.Clock(field.t[0],field.t[-1]);ch=Chart(o.knots,a.modes)
    def direct(s,u,v):
        hh,kk=ch.jets(s,u,v);sgrid,ugrid=np.broadcast_arrays(s[:,None],u[None,:])
        hh[0]=sgrid+hh[0];kk[0]=ugrid+kk[0];hh[1]=1+hh[1];kk[2]=1+kk[2]
        vals=field.parent(np.clip(hh[0],field.t[0],field.t[-1]).ravel(),kk[0].ravel())
        shape=sgrid.shape
        return np.stack(chain([w.reshape(*shape,3) for w in vals],hh,kk),axis=1)
    zero=np.zeros(ch.n*(len(ch.angfreq)+len(ch.radfreq)))
    ns,u,a0,old,_=clock.data_g(a,'training');mask=(ns>=field.t[0])&(ns<=field.t[-1]);active=ns[mask];r=a0[mask]*np.exp(field.alpha(active))
    trial=np.concatenate([direct(active[j:j+12],u,zero) for j in range(0,len(active),12)])
    print('parent training',tuple((z.min(),z.max()) for z in helper.metrics(trial,r)),flush=True)
    c,hist=fit(ch,active,u,r,trial)
    del trial
    def observe(name,coef):
        ns,u,r,old,_=clock.data_g(a,name);r=r.copy()
        act=(ns>=field.t[0])&(ns<=field.t[-1]);r[act]*=np.exp(field.alpha(ns[act]))
        best=np.array([0.,0.,1e9,1e9]);peaks=[];idxs=[None]*4
        A=F(float(np.load(a.ramp)['centralA']))
        for j in range(0,len(ns),12):
            s=ns[j:j+12];m=act[j:j+12];v=np.asarray(old[j:j+12]).copy()
            if m.any():v[m]=direct(s[m],u,coef)
            E,K,G=helper.metrics(v,r[j:j+12]);p=v[:,0];dist=np.sqrt(p[:,:,0]**2+(np.abs(p[:,:,1])-float(A))**2+p[:,:,2]**2)
            for i,(t,sign) in enumerate(((E,1),(K,1),(G,-1),(dist,-1))):
                aij=np.unravel_index(np.argmax(sign*t),t.shape);vv=t[aij]
                if best[i]*sign<vv*sign:best[i]=vv;idxs[i]=[float(s[aij[0]]),float(u[aij[1]])]
        return dict(metric=best[0],curvature=best[1],minAreaRatio=best[2],minHeld=best[3],at=idxs,points=len(ns)*len(u))
    orient=ch.orientation(c)
    if any(sum(o)>=F(4,5) for o in orient):raise ArithmeticError('Two-chart map failed the strict global contraction budget')
    tries={};scales=[1.,.75,.5]
    for scale in scales:
        obs=observe('training',c*scale);tries[str(scale)]=obs
        print('nonlinear training',scale,obs,flush=True)
    choose=min(scales,key=lambda s:tries[str(s)]['metric']);actual=c*choose
    groups={'training':tries[str(choose)]}
    for key in ('observer','independent'):
        groups[key]=observe(key,actual);print(key,groups[key],flush=True)
    orient=ch.orientation(actual)
    out=dict(schema='clocked-HF64-physical-XYZ-own3-same-frozen-g-two-material-coordinate-step-v1',
        entrySHA256=sha(__file__),fieldSHA256=sha(a.field),stateSHA256=sha(a.state),radialParentClockSHA256=sha(a.clock),
        frozenMetricDefinitionSHA256=field.gid,knots=ch.knots.tolist(),radialFrequencies=ch.radfreq.tolist(),angularFrequencies=ch.angfreq.tolist(),
        exactCoefficientsHex=[float(v).hex() for v in actual],linearizedLPHistory=hist,actualScale=choose,
        trueGlobalDerivativeAbsRowBounds=[[str(x) for x in o] for o in orient],realNonlinearTrainingTrials=tries,
        completeObservations=groups,trainingParentPeak=float(tries[str(choose)]['metric']))
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for n in ('scripts','field','ramp','coast','prepared','independent','state','clock','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--modes',type=int,default=5);run(ap.parse_args())
