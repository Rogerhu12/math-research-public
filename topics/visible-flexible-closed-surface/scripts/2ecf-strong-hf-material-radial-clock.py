#!/usr/bin/env python3
"""Actual whole-suffix radial material reparametrization of a fixed strong source and frozen target."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import time
from pathlib import Path
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import linprog


def load(p,name):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m);return m


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


class Field:
    def __init__(self,args,u):
        h=load(Path(__file__).with_name('2ecf-strong-port-hermite-fourier-background-physical-W.py'),'hff')
        data=np.load(args.field);self.knots=data['knots'];self.u=u
        c=data['coefficients'];phase=h.phases(u,c.shape[2]-1)
        self.curves=np.einsum('kum,nrmc->nrkuc',phase,c,optimize=True).real
        self.curves[[0,-1]]=h.numerical_endpoint_pair(args.scripts,args.ramp,args.coast,u)
        z=data['physicalW'];self.ws=BSpline(data['Wknots'],np.pad(z,((3,3),(0,0))),5,extrapolate=False)
        self.trig=np.empty((3,len(u),49))
        self.trig[0,:,0]=1;self.trig[1:,:,0]=0
        for k in range(1,25):
            co,si=np.cos(k*u),np.sin(k*u)
            self.trig[:,:,2*k-1]=np.array([co,-k*si,-k*k*co])
            self.trig[:,:,2*k]=np.array([si,k*co,-k*k*si])
        self.af=BSpline(data['alphaKnots'],np.pad(data['alpha'],(3,3)),5,extrapolate=False)
        self.poly=np.array([[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
                       [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]])
        self.ui=np.arange(len(u))[None,:]

    def at(self,S):
        # S is an (s,u) physical array entirely inside the connector.
        k=np.clip(np.searchsorted(self.knots,S,side='right')-1,0,len(self.knots)-2)
        h=self.knots[k+1]-self.knots[k];t=(S-self.knots[k])/h
        uidx=np.broadcast_to(self.ui,k.shape)
        out=[]
        for ri,uj in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2)):
            p=np.arange(ri,6)
            powers=np.stack([t**(j-ri)*(math.factorial(j)//math.factorial(j-ri)) for j in p],axis=-1)
            weights=powers@self.poly[:,p].T
            cols=self.ws(S,ri).reshape(*S.shape,3,49)
            W=np.einsum('sudk,uk->sud',cols,self.trig[uj],optimize=False)
            val=W.copy()
            for b in range(6):
                val+=(weights[:,:,b]*h**(b%3-ri))[:,:,None]*self.curves[k+(b>=3),b%3,uj,uidx]
            out.append(val)
        return np.stack(out,axis=1)


class Clock:
    def __init__(self,b,S,nmode=4):
        self.freq=2*np.arange(nmode+1)
        offsets=[.003,.006,.01,.015,.023,.035,.05,.072,.10,.14,.19,.25,.32,.40,.49,.58,.66,.73,.77]
        self.knots=np.r_[np.repeat(b,6),b+np.array(offsets),np.repeat(S,6)]
        n=len(self.knots)-6;self.B=BSpline(self.knots,np.eye(n)[:,3:-3],5,extrapolate=False)
        self.n=n-6;self.nm=len(self.freq)
    def angular(self,u):
        v=u[:,None]*self.freq[None,:]
        return [np.cos(v),-self.freq[None,:]*np.sin(v),-self.freq[None,:]**2*np.cos(v)]
    def factor(self,s,u):
        return [self.B(s,j) for j in range(3)],self.angular(u)
    def jets(self,s,u,x):
        B,C=self.factor(s,u);coef=x.reshape(self.n,self.nm)
        return [B[i]@coef@C[j].T for i,j in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))]
    def derivative_enclosure(self,x):
        cc=np.pad(x.reshape(self.n,self.nm),((3,3),(0,0)))
        ds=5*np.diff(cc,axis=0)/(self.knots[6:-1]-self.knots[1:-6])[:,None]
        return np.max(np.abs(ds).sum(1))


def compose(f,clock,s,u,x):
    h,hs,hu,hss,hsu,huu=clock.jets(s,u,x)
    ts=1+hs;ss=s[:,None]+h
    # Both endpoints are identities by omitted controls. Floating point
    # clipping only selects the same exact limiting endpoint for observations.
    val=f.at(np.clip(ss,f.knots[0],f.knots[-1]))
    P,V,U,A,B,C=val.swapaxes(0,1)
    mul=lambda scalar,vector:scalar[:,:,None]*vector
    return np.stack((P,mul(ts,V),U+mul(hu,V),mul(ts*ts,A)+mul(hss,V),
           mul(ts,B+mul(hu,A))+mul(hsu,V),C+mul(2*hu,B)+mul(hu*hu,A)+mul(huu,V)),axis=1)


def data_g(args,key):
    prep=json.loads(args.prepared.read_bytes());ind=json.loads(args.independent.read_bytes())
    rec=ind if key=='independent' else prep['caches'][key]
    ns=np.asarray(rec.get('nodes',rec.get('physicalNodes')));u=np.asarray(rec['angles'])
    ar=np.load(rec['files']['radius'],mmap_mode='r')[:,0];jets=np.load(rec['files']['jets'],mmap_mode='r')
    return ns,u,ar,jets,rec


def learn(args,clk,field,ns,u,a,base):
    b,S=field.knots[[0,-1]];valid=(ns>=b)&(ns<=S);sr=ns[valid]
    radii=a[valid]*np.exp(field.af(sr))
    # The annular design is mirror-balanced but we retain all actual angles.
    cube=np.concatenate([field.at(np.broadcast_to(s[:,None],(len(s),len(u)))) for s in np.array_split(sr,20)])
    P,V,U,A,B,C=cube.swapaxes(0,1);dot=lambda v,w:np.sum(v*w,axis=-1)
    E,F,G=dot(V,V),dot(V,U),dot(U,U);r=radii[:,None]
    Es,Fs,Gs=2*dot(V,A),dot(A,U)+dot(V,B),2*dot(U,B)
    Bm,Cm=clk.factor(sr,u);zero=np.zeros(clk.n*clk.nm)
    mat=lambda Q,i,j,ir,iu:Q[:,None,None]*Bm[i][ir,:,None]*Cm[j][iu,None,:]
    def actual_linear(x):
        q,qs,qu,*_=clk.jets(sr,u,x)
        e=E-1+Es*q+2*E*qs
        f=(F+Fs*q+F*qs+E*qu)/r
        g=(G+Gs*q+2*F*qu)/r**2-1
        return e,f,g
    def extremal(e,f,g):
        tr=(e+g)/2;rad=np.hypot((e-g)/2,f);sgn=np.where(tr>=0,1.,-1.)
        err=np.abs(tr)+rad
        cs=sgn*(e-g)/np.maximum(2*rad,1e-30);sn=sgn*f/np.maximum(rad,1e-30)
        return err,sgn,(1+cs)/2,sn,(1-cs)/2
    cs=[];rhs=[];x=zero
    N=clk.n*clk.nm; reg=np.eye(N).reshape(N,clk.n,clk.nm)
    padded=np.pad(reg,((0,0),(3,3),(0,0)))
    der=(5*np.diff(padded,axis=1)/(clk.knots[6:-1]-clk.knots[1:-6])[None,:,None]).reshape(N,-1).T
    # Each harmonic derivative is bounded separately, guaranteeing a global oriented clock.
    cs.append(np.c_[der,np.zeros(len(der))]);rhs.append(np.full(len(der),.14/clk.nm))
    cs.append(np.c_[-der,np.zeros(len(der))]);rhs.append(np.full(len(der),.14/clk.nm))
    history=[]
    for step in range(12):
        e,f,g=actual_linear(x);err,sg,c2,sc2,s2=extremal(e,f,g)
        # Add worst cuts on distinct radial rows and throughout angle sectors.
        ids=[]
        for part in np.array_split(np.arange(len(sr)),64):
            flat=err[part].reshape(-1);jj=np.argpartition(flat,-6)[-6:]
            ids.extend((part[j//len(u)],j%len(u)) for j in jj)
        hot=np.argpartition(err.ravel(),-400)[-400:]
        ids.extend(zip(*np.unravel_index(hot,err.shape)))
        ij=np.unique(np.asarray(ids),axis=0);ir,iu=ij.T
        Z=lambda m:m[ir,iu]
        sign,p,q,t=Z(sg),Z(c2),Z(sc2),Z(s2);ra=radii[ir]
        a0=p*Z(Es)+q*Z(Fs)/ra+t*Z(Gs)/ra**2
        a1=p*2*Z(E)+q*Z(F)/ra; a2=q*Z(E)/ra+t*2*Z(F)/ra**2
        jac=(mat(a0,0,0,ir,iu)+mat(a1,1,0,ir,iu)+mat(a2,0,1,ir,iu)).reshape(len(ir),N)
        val=p*(Z(E)-1)+q*Z(F)/ra+t*(Z(G)/ra**2-1)
        cs.append(np.c_[sign[:,None]*jac,-np.ones(len(jac))]);rhs.append(-sign*val)
        sol=linprog(np.r_[np.zeros(N),1.],A_ub=np.vstack(cs),b_ub=np.concatenate(rhs),
                    bounds=[(-.003,.003)]*N+[(0,2)],method='highs')
        if not sol.success:raise ArithmeticError(sol.message)
        x=sol.x[:-1];new=extremal(*actual_linear(x))[0].max()
        history.append([float(sol.x[-1]),float(new)])
        if new<sol.x[-1]+.00015:break
    return x,history


def observe(args,clock,vector,helper):
    groups={};cost=0
    ref=np.load(args.field);b,S=ref['knots'][[0,-1]]
    for key in ('training','observer','independent'):
        ns,u,a,old,rec=data_g(args,key)
        fg=Field(args,u);active=(ns>=b)&(ns<=S)
        radius=a.copy();radius[active]*=np.exp(fg.af(ns[active]))
        stats=[];rms=0.;num=0;originalRms=0.
        for j in range(0,len(ns),16):
            ss=ns[j:j+16];mask=active[j:j+16];vv=np.asarray(old[j:j+16]).copy()
            if mask.any():vv[mask]=compose(fg,clock,ss[mask],u,vector)
            e,k,area=helper.metrics(vv,radius[j:j+16])
            rms+=float((e*e).sum());num+=e.size
            row=[]
            for q,g in ((e,1),(k,1),(area,-1)):
                ij=np.unravel_index(np.argmax(g*q),q.shape)
                row.append([float(q[ij]),float(ss[ij[0]]),float(u[ij[1]])])
            stats.append(row)
        groups[key]=dict(metric=max(q[0] for q in stats),curvature=max(q[1] for q in stats),
                         area=min(q[2] for q in stats),points=num,rms=float(np.sqrt(rms/num)))
        print(key,groups[key],flush=True)
    return groups


def main():
    ap=argparse.ArgumentParser()
    for k in ('scripts','field','ramp','coast','prepared','independent','output'):
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    h=load(Path(__file__).with_name('2ecf-strong-port-hermite-fourier-background-physical-W.py'),'hfm')
    ns,u,a,j,rec=data_g(args,'training');f=Field(args,u);c=Clock(*f.knots[[0,-1]])
    coeff,hist=learn(args,c,f,ns,u,a,j); print('linear trial',hist,'derivative',c.derivative_enclosure(coeff),flush=True)
    if c.derivative_enclosure(coeff)>.141:raise ArithmeticError('Orientation limit not achieved')
    data=observe(args,c,coeff,h)
    out=dict(schema='H65-HF64M80-same-g-true-radial-material-clock-v1',fieldSHA256=sha(args.field),
             sourceSHA256=sha(__file__),preparedSHA256=sha(args.prepared),independentSHA256=sha(args.independent),
             radialKnots=c.knots.tolist(),frequencies=c.freq.tolist(),coefficients=coeff.tolist(),
             linearizedCuttingPlane=hist,nominalAbsRadialClockDerivativeUpper=c.derivative_enclosure(coeff),
             support=[f.knots[0],f.knots[-1]],allOwnFullGridObservations=data,seconds=time.monotonic()-start)
    with args.output.open('x') as fp:json.dump(out,fp,indent=2);fp.write('\n')


if __name__=='__main__':main()
