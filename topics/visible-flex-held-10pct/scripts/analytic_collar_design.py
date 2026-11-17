#!/usr/bin/env python3
"""A circular-reference collar whose meridian speed is exact, before correction.

The reference satisfies the old cut's rotating-background first/second jet.
Its two integral endpoint equations determine length and an angular control.
The actual noncircular prefix endpoint is then lifted with all its two-jets.
This is a finite design experiment, not an exact nonlinear closure theorem.
"""
import argparse, hashlib, json, time
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import root, least_squares
from short_collar_design import Collar


class AnalyticCollar(Collar):
    def __init__(self,trace,rise=.25,radius=.15,nc=18,m=8,bend=0.,degree=5):
        super().__init__(trace,rise=rise,radius=radius,nc=nc,m=m)
        self.r0=.6;self.beta0=np.arctan2(1.,-2.)
        self.beta_s0=-(28/15)/np.sin(self.beta0)
        self.bend=bend;self.degree=degree
        self.qnodes,self.qweights=np.polynomial.legendre.leggauss(160)
        q=(1+self.qnodes)/2;w=self.qweights/2
        def eq(v):
            L,c=v;beta,_=self.beta(q,L,c)
            return [L*np.dot(w,np.cos(beta))-(self.radius-self.r0),
                    L*np.dot(w,np.sin(beta))-self.rise]
        sol=root(eq,[np.hypot(self.r0-radius,rise)+.04,-.1],tol=1e-11)
        if np.max(abs(np.array(eq(sol.x))))>2e-12 or sol.x[0]<=0:
            raise ValueError('Reference endpoint integral equations failed')
        self.length,self.asym=sol.x
        self.reference_error=float(np.max(abs(np.array(eq(sol.x)))))
        knots=np.r_[np.zeros(degree+1),np.linspace(0,1,nc-degree+1)[1:-1],np.ones(degree+1)]
        self.spline=BSpline(knots,np.eye(nc),degree,extrapolate=False)
        self.intervals=np.unique(knots)

    def beta(self,s,L=None,c=None):
        if L is None:L=self.length
        if c is None:c=self.asym
        s=np.asarray(s);S=s**3*(10-15*s+6*s*s);Sp=30*s*s*(1-s)**2
        H=s-6*s**3+8*s**4-3*s**5;Hp=1-18*s*s+32*s**3-15*s**4
        b=self.beta0+(np.pi-self.beta0)*S+L*self.beta_s0*H+self.bend*np.sin(2*np.pi*S)+c*np.sin(np.pi*S)
        bp=(np.pi-self.beta0)*Sp+L*self.beta_s0*Hp+2*np.pi*self.bend*Sp*np.cos(2*np.pi*S)+np.pi*c*Sp*np.cos(np.pi*S)
        return b,bp

    def reference_radial(self,s):
        s=np.asarray(s);v=s[:,None]*(1+self.qnodes)/2;b,_=self.beta(v)
        r=self.r0+self.length*s/2*(np.cos(b)@self.qweights)
        z=self.z0+self.length*s/2*(np.sin(b)@self.qweights)
        b,bp=self.beta(s)
        return ([r,self.length*np.cos(b),-self.length*np.sin(b)*bp],
                [z,self.length*np.sin(b),self.length*np.cos(b)*bp])

    def prepare(self,s,u):
        s,u=np.asarray(s),np.asarray(u);g=super().prepare(s,u)
        rad,ax=self.reference_radial(s)
        start_r=[self.r0,self.length*np.cos(self.beta0),-self.length**2*np.sin(self.beta0)*self.beta_s0]
        start_z=[self.z0,self.length*np.sin(self.beta0),self.length**2*np.cos(self.beta0)*self.beta_s0]
        end_r=[self.radius,-self.length,0.];end_z=[self.z1,0.,0.]
        polys=[[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5],
               [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,.5,-1,.5]]
        Hr=[];Hz=[]
        for ds in range(3):
            h=[np.polynomial.polynomial.polyval(s,np.polynomial.polynomial.polyder(p,ds)) for p in polys]
            Hr.append(sum(h[j]*(start_r+end_r)[j] for j in range(6)))
            Hz.append(sum(h[j]*(start_z+end_z)[j] for j in range(6)))
        er=np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1)
        et=np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1)
        circle=(er,et,-er);ez=np.array([0.,0.,1.])
        for i,(ds,du) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
            g['base'][i]+=(rad[ds]-Hr[ds])[:,None,None]*circle[du]
            if du==0:g['base'][i]+=(ax[ds]-Hz[ds])[:,None,None]*ez
        return g


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--trace',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rise',type=float,default=.25);p.add_argument('--radius',type=float,default=.15)
    p.add_argument('--nc',type=int,default=18);p.add_argument('--m',type=int,default=8)
    p.add_argument('--degree',type=int,default=5);p.add_argument('--bend',type=float,default=0.)
    p.add_argument('--nfev',type=int,default=140);p.add_argument('--seed',type=Path)
    a=p.parse_args();obj=AnalyticCollar(dict(np.load(a.trace)),rise=a.rise,radius=a.radius,nc=a.nc,m=a.m,bend=a.bend,degree=a.degree)
    nodes,_=np.polynomial.legendre.leggauss(max(6,a.degree))
    s=np.concatenate([l+(r-l)*(1+nodes)/2 for l,r in zip(obj.intervals[:-1],obj.intervals[1:])])
    nu=max(64,8*a.m);g=obj.prepare(s,np.arange(nu)*2*np.pi/nu)
    q=np.zeros(obj.size) if a.seed is None else np.array(json.loads(a.seed.read_text())['q'])
    start=time.monotonic();count=0
    def fun(q):
        nonlocal count
        count+=1;r=obj.residual(q,g)
        if count%10==1:print(json.dumps(dict(eval=count,rms=float(np.sqrt(np.mean(r*r))),maximum=float(abs(r).max()),seconds=time.monotonic()-start)),flush=True)
        return r
    res=least_squares(fun,q,jac=lambda q:obj.residual(q,g,True),method='lm',max_nfev=a.nfev,ftol=1e-11,xtol=1e-11,gtol=1e-11,x_scale='jac')
    d=dict(parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()},
           trace_sha256=hashlib.sha256(a.trace.read_bytes()).hexdigest(),q=res.x.tolist(),
           length=float(obj.length),asym=float(obj.asym),reference_equation_error=obj.reference_error,
           success=bool(res.success),message=res.message,nfev=res.nfev,cost=res.cost,
           seconds=time.monotonic()-start,audit=obj.audit(res.x,241,256))
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps({k:v for k,v in d.items() if k!='q'}),flush=True)

if __name__=='__main__':main()
