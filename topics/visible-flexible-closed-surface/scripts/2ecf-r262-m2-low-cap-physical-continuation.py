#!/usr/bin/env python3
"""Genuine finite-amplitude, two-ended full Cartesian fields on a new resonant mixed-curvature meridian and the inherited R262 oscillating deep tail."""
import argparse,hashlib,importlib.util,json,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import BSpline
from scipy.optimize import brentq
HERE=Path(__file__).resolve().parent
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
base=load(HERE/'2ecf-r262-minkowski-physical-continuation.py','resonant_bulk_fit');O=base.O
def herm(x,L):
    polys=[[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5]]
    return np.stack([[np.polynomial.polynomial.polyval(x,np.polynomial.polynomial.polyder(p,j))*L**(i-j) for i,p in enumerate(polys)] for j in range(3)])
def support(R,eps,u):
    ph=u.copy()
    for _ in range(9):
        ph-=(R*ph-1.5*eps*np.sin(2*ph)-R*u)/(R-3*eps*np.cos(2*ph))
    if max(abs(R*ph-1.5*eps*np.sin(2*ph)-R*u))>2e-12:raise ValueError('central true material inverse')
    N=np.stack([np.cos(ph),np.sin(ph),0*u],axis=-1);T=np.stack([-np.sin(ph),np.cos(ph),0*u],axis=-1)
    return np.stack([(R+eps*np.cos(2*ph))[:,None]*N-(2*eps*np.sin(2*ph))[:,None]*T,R*T,-R**2/(R-3*eps*np.cos(2*ph))[:,None]*N])
class Source:
    def __init__(self,args):
        m=json.loads(args.meridian.read_bytes());self.ease=m.get('phaseEasing',0.);m=m['selected'][args.index];z=json.loads(args.buffer.read_bytes());B=z['choices'][0];seam=z['originalSeam']
        self.bp=np.array(B['levels']);self.bl=np.array(B['lengths']);self.rb=np.r_[z['innerRadius'],z['innerRadius']+np.cumsum(self.bl)]
        y=np.array([1/seam['r']**4,seam['w']*seam['r']**4*(seam['Hr']/seam['H']-4/seam['r']),0.,0.]);self.bsol=[]
        for i in range(len(self.bl)):
            def rhs(r,y):
                w,_=self.w(i,r);return [y[1]/(w*r**8),-12*w*r**6*y[0],w,np.hypot(1,w)]
            q=solve_ivp(rhs,self.rb[i:i+2],y,method='DOP853',rtol=3e-12,atol=[1e-11,1e-17,1e-14,1e-14],max_step=self.bl[i]/12,dense_output=True)
            assert q.success;self.bsol.append(q.sol);y=q.y[:,-1]
        r=self.rb[-1];self.Hout=y[0]*r**4;self.dzo=y[2];self.dso=y[3];w=self.bp[-1];D=4/r+y[1]/(r**8*w*y[0]);self.D=D;fcut=-w*(r*D-4)/3
        self.ph=np.array(m['phases']);self.ll=np.array(m['lengths']);self.co=np.array(m['coasts'])
        def merid(coast,save=False):
            self.co[1]=coast;breaks=[0.];self.segs=[]
            for j in range(4):
                self.segs.append((j,False));breaks.append(breaks[-1]+self.ll[j])
                if j<3:self.segs.append((j,True));breaks.append(breaks[-1]+self.co[j])
            self.breaks=np.array(breaks);self.S=breaks[-1];self.sol=[None]*len(self.segs);y=np.array([r,0,fcut,1.])
            for j in reversed(range(len(self.segs))):
                if breaks[j+1]-breaks[j]<1e-12:continue
                def fun(s,y):
                    phi,_=self.phase(j,s);v,b=np.sin(phi),np.cos(phi);R,Z,F,H=y;Fs=-(3*v*F+4*b*H)/R
                    return [v,b,Fs,-v/b*Fs]
                o=solve_ivp(fun,(breaks[j+1],breaks[j]),y,method='DOP853',rtol=2e-12,atol=3e-14,dense_output=save,max_step=(breaks[j+1]-breaks[j])/15);assert o.success
                if save:self.sol[j]=o.sol
                y=o.y[:,-1]
            return y
        left,right=max(0,m['coasts'][1]-.025),min(.63,m['coasts'][1]+.025)
        t=brentq(lambda c:merid(c)[3],left,right,xtol=3e-15)
        y0=merid(t,True);self.R=y0[0];self.shift=-y0[1];self.F0=y0[2];self.cutGain=1/self.F0
        with np.load(args.tail_table) as f:self.tail={k:f[k].copy() for k in f.files}
        d=self.tail;i=np.argmin(abs(d['r']-seam['r']));self.inner=i;self.innerH=d['linear'][1,i];self.sa=d['meridian'][i];self.za=d['height'][i]
        self.T=self.S+self.dso+max(d['meridian'])-self.sa
        self.tailScale=1/(self.F0*self.Hout*self.innerH)
    def phase(self,j,s):
        i,co=self.segs[j];x=(s-self.breaks[j])/max(1e-16,self.breaks[j+1]-self.breaks[j]);d=self.ph[i+1]-self.ph[i]
        if co:return self.ph[i+1]+0*x,0*x
        if self.ease:
            e=self.ease;h=np.where(x<e,x*x/(2*e*(1-e)),np.where(x>1-e,1-(1-x)**2/(2*e*(1-e)),(x-e/2)/(1-e)));hp=np.minimum(np.minimum(x/e,(1-x)/e),1)/(1-e)
            return self.ph[i]+d*h,d*hp/self.ll[i]
        return self.ph[i]+d*x*x*(3-2*x),6*d*x*(1-x)/self.ll[i]
    def w(self,j,r):
        t=(r-self.rb[j])/self.bl[j];a=np.log(self.bp[j+1]/self.bp[j]);w=self.bp[j]*np.exp(a*t**3*(10+t*(-15+6*t)));return w,w*a*30*t*t*(1-t)**2/self.bl[j]
    def prefix(self,ss):
        ret=np.empty((len(ss),13))
        for i in range(len(self.segs)):
            mask=(ss>=self.breaks[i])&(ss<self.breaks[i+1] if i+1<len(self.segs) else ss<=self.breaks[i+1]+1e-14)
            t=ss[mask]
            if not len(t):continue
            phi,k=self.phase(i,t);v,b=np.sin(phi),np.cos(phi);r,z,F,H=self.sol[i](t);z+=self.shift
            F,H=F/self.F0,H/self.F0;vs,bs=b*k,-v*k;Fs=-(3*v*F+4*b*H)/r;Hs=-v/b*Fs
            Fss=-(3*vs*F+4*v*Fs+4*bs*H+4*b*Hs)/r;Hss=-vs/b**3*Fs-v/b*Fss
            ret[mask]=np.column_stack([t,r,z,v,b,vs,bs,F,H,Fs,Hs,Fss,Hss])
        return ret
    def buffer(self,rs):
        ret=np.empty((len(rs),13))
        for i in range(len(self.bl)):
            mask=(rs>=self.rb[i])&(rs<self.rb[i+1] if i+1<len(self.bl) else rs<=self.rb[i+1]+1e-14);r=rs[mask]
            if not len(r):continue
            Q,p,z,s=self.bsol[i](r);w,wr=self.w(i,r);E=1+w*w;v=-1/np.sqrt(E);b=w/np.sqrt(E);vs=-w*wr/E**2;bs=-v*vs/b
            H=Q*r**4/(self.F0*self.Hout);J=p/(r**4*w*self.F0*self.Hout);F=-w*r*J/3
            Hr=4*H/r+J;Fs=-(3*v*F+4*b*H)/r;Hs=v*Hr
            Fss=-(3*vs*F+4*v*Fs+4*bs*H+4*b*Hs)/r;Hss=-v*v*wr/w*J+vs*Hr
            ret[mask]=np.column_stack([self.S+self.dso-s,r,self.shift+self.dzo-z,v,b,vs,bs,F,H,Fs,Hs,Fss,Hss])
        return ret
    def original(self,ids):
        d=self.tail;r=d['r'][ids];w=d['w'][ids];wr=d['wr'][ids];E=1+w*w
        v=-1/np.sqrt(E);b=w/np.sqrt(E);vs=-w*wr/E**2;bs=-wr/E**2
        F,H,Fs,Hs,Fss,Hss=d['linear'][:,ids]*self.tailScale
        return np.column_stack([self.S+self.dso+d['meridian'][ids]-self.sa,r,self.shift+self.dzo+d['height'][ids]-self.za,v,b,vs,bs,F,H,Fs,Hs,Fss,Hss])
    def grid(self,n,a,shift):
        def mesh(nodes,cnt):
            rows=[]
            for x,y in zip(nodes[:-1],nodes[1:]):
                m=max(3,round(cnt*(y-x)/(nodes[-1]-nodes[0])));t=np.r_[0.,(np.arange(m)+.5)/m,1.] if shift else np.linspace(0,1,m+1)
                rows.extend(x+(y-x)*t)
            return np.unique(np.clip(rows,nodes[0],nodes[-1]))
        knots=self.breaks
        if self.ease:
            extra=[self.breaks[i]+(self.breaks[i+1]-self.breaks[i])*q for i,(_,co) in enumerate(self.segs) if not co for q in (self.ease,1-self.ease)];knots=np.unique(np.r_[knots,extra])
        P=self.prefix(mesh(knots,n));B=self.buffer(mesh(self.rb,n//2))
        d=self.tail;use=np.where(d['r']<=self.rb[0]+1e-14)[0];r=d['r'][use]
        selected=[use[np.argmin(abs(r-t))] for t in mesh(np.array([r.min(),r.max()]),n//2)]
        for k in np.unique(d['labels'][use,0]):
            ix=use[d['labels'][use,0]==k];peak=abs(d['linear'][4,ix])+abs(d['linear'][5,ix]);selected.append(ix[np.argmax(peak)])
        Z=self.original(np.unique(selected));allrows=np.vstack([P,B,Z]);return allrows[np.argsort(allrows[:,0],kind='stable')],np.arange(a)*2*np.pi/a+(np.pi/a if shift else 0)
def jet(rows,u,eps,linear=True):
    s,r,z,v,b,vs,bs,f,h,fs,hs,fss,hss=rows.T
    er=np.stack([np.cos(u),np.sin(u),0*u],axis=-1);et=np.stack([-np.sin(u),np.cos(u),0*u],axis=-1);ez=np.stack([0*u,0*u,1+0*u],axis=-1)
    ang2=[];angz=[]
    for j in range(3):
        # complex horizontal modes e^(3iu)/4 +3e^(-iu)/4
        a=.25*(3j)**j*np.exp(3j*u)+.75*(-1j)**j*np.exp(-1j*u);ang2.append(np.stack([a.real,a.imag,0*u],axis=-1))
        angz.append(np.cos(2*u+j*np.pi/2)*2**j)
    au=[er,et,-er];out=[]
    for idx,((i,j),R,Z,F,H) in enumerate(zip(O,(r,v,r,vs,v,r),(z,b,z,bs,b,z),(f,fs,f,fss,fs,f),(h,hs,h,hss,hs,h))):
        out.append(R[:,None,None]*au[j]+(Z[:,None,None]*ez if j==0 else 0)+eps*(F[:,None,None]*ang2[j]+H[:,None,None]*angz[j][:,None]*ez))
    return np.stack(out,axis=1)
class Fit:
    def __init__(self,src,rows,u,eps,spans,modes):
        self.z=rows[:,0]/src.T;self.t=u;self.bb=rows[:,1,None]+np.zeros((1,len(u)))
        self.base=jet(rows,u,eps)
        g0=src.prefix(np.array([0.]));jj=jet(g0,u,eps)[0];sup=support(src.R,eps,u)
        # Central value, radial first and second derivatives are attached by exact Hermite lifting.
        # Angular derivatives for its non-value radial traces follow the same explicit harmonics.
        change=np.empty((3,3,len(u),3));base0=g0.copy()
        for i,(iv,iz,if0,ih) in enumerate(((1,2,7,8),(3,4,9,10),(5,6,11,12))):
            temp=g0.copy();temp[:,1]=g0[:,iv];temp[:,2]=g0[:,iz];temp[:,7]=g0[:,if0];temp[:,8]=g0[:,ih]
            v=jet(temp,u,eps)[0,[0,2,5]]
            target=np.zeros_like(v)
            if i==0:target=sup
            if i==1:target[0,:,2]=1.
            change[i]=target-v
        hh=herm(self.z,src.T)
        self.base+=np.stack([np.einsum('in,iud->nud',hh[i],change[:,j]) for i,j in O],axis=1)
        knot=np.r_[np.zeros(6),np.arange(1,spans)/spans,np.ones(6)]
        b=BSpline(knot,np.eye(len(knot)-6)[:,3:-3],5)
        self.B=[b(self.z,j)/src.T**j for j in range(3)];self.nb=self.B[0].shape[1];self.na=3*modes
        self.ang=np.zeros((3,len(u),self.na,3));a=0
        for d in range(3):
            for mm in (range(1,2*modes+1,2) if d<2 else range(0,2*modes,2)):
                c,s=np.cos(mm*u),np.sin(mm*u)
                for j,ds in enumerate(((s,mm*c,-mm**2*s) if d==1 else (c,-mm*s,-mm**2*c))):self.ang[j,:,a,d]=ds
                a+=1
    field=base.Grid.field
    metrics=base.Grid.metrics
    step=base.Grid.step
def main():
    p=argparse.ArgumentParser()
    for k in ('meridian','buffer','tail-table','out'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--index',type=int,default=0);p.add_argument('--epsilon',type=float,required=True);p.add_argument('--modes',type=int,default=4);p.add_argument('--spans',type=int,default=16);p.add_argument('--steps',type=int,default=8);p.add_argument('--parent',type=Path)
    a=p.parse_args();src=Source(a);make=lambda n,m,j:Fit(src,*src.grid(n,m,j),a.epsilon,a.spans,a.modes)
    g=make(152,72,False);x=np.zeros((g.nb,g.na));ref=None
    if a.parent:
        ref=json.loads(a.parent.read_bytes());x=(a.epsilon/ref['epsilon'])**2*np.array(ref['xyz'])
    hist=[g.metrics(x)];ats=[];print('start',src.R,src.T,src.cutGain,hist[0],flush=True)
    for i in range(a.steps):
        old=hist[-1];ok=False
        for reg in [1e-6,.00007,.004,.05]:
            dx=g.step(x,reg,min(4,1+i*.5))
            for st in [1,.5,.25,.125,.0625,.03125]:
                v=g.metrics(x+st*dx)
                if v['metric']<old['metric']*(1-1e-6) and v['curvature']<max(10.1,old['curvature']+.003):
                    x+=st*dx;hist.append(v);ats.append(dict(scale=st,reg=reg));ok=True;print('acc',i,v,flush=True);break
            if ok:break
        if not ok:break
    out=[]
    for n,m,sh in [(260,144,False),(243,181,True)]:
        gg=make(n,m,sh);out.append(dict(radial=len(gg.z),angular=m,actual=gg.metrics(x)));print('obs',out[-1],flush=True)
    inner=src.original(np.where(src.tail['r']<=src.rb[0]+1e-14)[0]);deep=[]
    for start in range(0,len(inner),48):
        gg=Fit(src,inner[start:start+48],np.pi/120+np.arange(120)*2*np.pi/120,a.epsilon,a.spans,a.modes);deep.append(gg.metrics(x))
    rep=dict(schema='true-nonlinear-R262-infinite-deep-and-new-buffer-and-physical-short-resonant-m2-full-cartesian-v1',scriptSHA256=base.sha(__file__),meridianSHA256=base.sha(a.meridian),bufferSHA256=base.sha(a.buffer),tableSHA256=base.sha(a.tail_table),index=a.index,epsilon=a.epsilon,
        centralRadius=src.R,centralHalfWidthDifference=2*a.epsilon,cutS=src.S,materialT=src.T,cutHeight=src.shift,cutHeightGain=src.cutGain,correctedCoasts=src.co.tolist(),newExactSupportRadiusLower=src.R-3*a.epsilon,spans=a.spans,modes=a.modes,xyz=x.tolist(),history=hist,steps=ats,trainingRadial=len(g.z),observers=out,
        deepObserver=dict(rawRadial=len(inner),angular=120,metric=max(z['metric'] for z in deep),curvature=max(z['curvature'] for z in deep)),fixedNewG=True,previousCompleteFieldSHA256=base.sha(a.parent) if a.parent else None)
    with a.out.open('x') as f:json.dump(rep,f,indent=2);f.write('\n')
    print('complete deep',rep['deepObserver'],flush=True)
if __name__=='__main__':main()
