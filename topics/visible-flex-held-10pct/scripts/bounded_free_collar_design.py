#!/usr/bin/env python3
"""New collar metric design with a positive speed bound and true curvature penalty.

Finite design only. Bounds are optimization penalties, not certificates.
The input and exact C2 endpoint jets are those of short_collar_design.py.
"""
import argparse, hashlib, json, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from short_collar_design import Collar

class BoundedCollar(Collar):
    def __init__(self,*args,curvature_limit=10.,**kwargs):
        super().__init__(*args,free_E=True,**kwargs)
        self.limit=curvature_limit

    def residual(self,q,g,jac=False):
        base=super().residual(q,g,jac)
        x,fs,fu,fss,fsu,fuu=self.geometry(q,g,True)
        e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1)
        me=e.mean(1);lo=np.maximum(.5-me/self.length**2,0);hi=np.maximum(me/self.length**2-1.5,0)
        cross=np.cross(fs,fu);area=np.linalg.norm(cross,axis=-1);normal=cross/np.maximum(area,1e-20)[:,:,None]
        l=np.sum(normal*fss,-1);m=np.sum(normal*fsu,-1);n=np.sum(normal*fuu,-1)
        det=np.maximum(e*gg-f*f,1e-30);T=gg*l+e*n-2*f*m;P=l*n-m*m
        H=T/(2*det);K=P/det;Q=np.maximum(4*H*H-2*K,1e-30);root=np.sqrt(Q)
        res=.3*np.maximum(root/self.limit-1,0)
        if not jac:return np.r_[base,lo,hi,res.ravel()]
        Bs,Bu,Bss,Bsu,Buu=[g['radial'][a][:,None,:,None,None]*g['angle'][b][None,:,None,:,:] for a,b in ((1,0),(0,1),(2,0),(1,1),(0,2))]
        def lift(v):return v[:,:,None,None]
        de=2*np.sum(fs[:,:,None,None,:]*Bs,-1)
        df=np.sum(fu[:,:,None,None,:]*Bs+fs[:,:,None,None,:]*Bu,-1)
        dg=2*np.sum(fu[:,:,None,None,:]*Bu,-1)
        dme=de.mean(1)/self.length**2
        jlo=-dme*(lo>0)[:,None,None];jhi=dme*(hi>0)[:,None,None]
        dcross=np.cross(Bs,fu[:,:,None,None,:])+np.cross(fs[:,:,None,None,:],Bu)
        dnormal=(dcross-normal[:,:,None,None,:]*np.sum(normal[:,:,None,None,:]*dcross,-1)[:,:,:,:,None])/area[:,:,None,None,None]
        dl=np.sum(dnormal*fss[:,:,None,None,:]+normal[:,:,None,None,:]*Bss,-1)
        dm=np.sum(dnormal*fsu[:,:,None,None,:]+normal[:,:,None,None,:]*Bsu,-1)
        dn=np.sum(dnormal*fuu[:,:,None,None,:]+normal[:,:,None,None,:]*Buu,-1)
        ddet=lift(gg)*de+lift(e)*dg-2*lift(f)*df
        dT=lift(l)*dg+lift(gg)*dl+lift(n)*de+lift(e)*dn-2*lift(m)*df-2*lift(f)*dm
        dP=lift(n)*dl+lift(l)*dn-2*lift(m)*dm
        dQ=(4*lift(H)*dT-2*dP+lift(2*K-8*H*H)*ddet)/lift(det)
        jk=.3*dQ/(2*self.limit*lift(root))*(root>self.limit)[:,:,None,None]
        return np.r_[base,jlo.reshape(-1,self.size),jhi.reshape(-1,self.size),jk.reshape(-1,self.size)]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--trace',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--length',type=float,default=.55);p.add_argument('--rise',type=float,default=.25);p.add_argument('--radius',type=float,default=.15)
    p.add_argument('--nc',type=int,default=16);p.add_argument('--m',type=int,default=8);p.add_argument('--nfev',type=int,default=200)
    p.add_argument('--curvature-limit',type=float,default=10.);p.add_argument('--seed',type=Path)
    a=p.parse_args();obj=BoundedCollar(dict(np.load(a.trace)),length=a.length,rise=a.rise,radius=a.radius,nc=a.nc,m=a.m,curvature_limit=a.curvature_limit)
    x,_=np.polynomial.legendre.leggauss(7)
    s=np.concatenate([l+(r-l)*(1+x)/2 for l,r in zip(obj.intervals[:-1],obj.intervals[1:])]);nu=max(96,12*a.m)
    g=obj.prepare(s,np.arange(nu)*2*np.pi/nu);q=np.zeros(obj.size) if a.seed is None else np.array(json.loads(a.seed.read_text())['q'])
    start=time.monotonic();count=0
    def fun(q):
        nonlocal count
        count+=1;r=obj.residual(q,g)
        if count%10==1:print(json.dumps(dict(eval=count,rms=float(np.sqrt(np.mean(r*r))),maximum=float(abs(r).max()),seconds=time.monotonic()-start)),flush=True)
        return r
    res=least_squares(fun,q,jac=lambda q:obj.residual(q,g,True),method='lm',max_nfev=a.nfev,ftol=1e-11,xtol=1e-11,gtol=1e-11,x_scale='jac')
    d=dict(parameters={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},trace_sha256=hashlib.sha256(a.trace.read_bytes()).hexdigest(),q=res.x.tolist(),success=bool(res.success),message=res.message,nfev=res.nfev,cost=res.cost,seconds=time.monotonic()-start,audit=obj.audit(res.x,401,384))
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items()if k!='q'}),flush=True)
if __name__=='__main__':main()
