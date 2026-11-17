#!/usr/bin/env python3
"""Bounded cap design with actual shape-operator penalty."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from relaxed_cap_base import Model

class CurvedModel(Model):
 def __init__(self,*args,curvature_limit=12.,curvature_weight=.2,**kwargs):
  super().__init__(*args,**kwargs);self.limit=curvature_limit;self.weight=curvature_weight
 def residual_jac(self,q,g,need_jac=False):
  base=super().residual_jac(q,g,need_jac)
  if self.weight==0:return base
  x,fs,fu,fss,fsu,fuu=self.geometry(q,g,True)
  e=np.sum(fs*fs,-1);f=np.sum(fs*fu,-1);gg=np.sum(fu*fu,-1)
  cross=np.cross(fs,fu);area=np.linalg.norm(cross,axis=-1);normal=cross/np.maximum(area,1e-20)[:,:,None]
  l=np.sum(normal*fss,-1);m=np.sum(normal*fsu,-1);n=np.sum(normal*fuu,-1)
  det=np.maximum(e*gg-f*f,1e-30);T=gg*l+e*n-2*f*m;P=l*n-m*m
  H=T/(2*det);K=P/det;Q=np.maximum(4*H*H-2*K,1e-30);root=np.sqrt(Q)
  res=self.weight*np.maximum(root/self.limit-1,0)
  support=-np.sum(x*normal,axis=-1)
  sres=10*np.maximum(.09-support,0)
  if not need_jac:return np.r_[base,res.ravel(),sres.ravel()]
  B=[]
  for a,b in [(1,0),(0,1),(2,0),(1,1),(0,2)]:
   B.append(g['r'][a][:,None,:,None,None]*g['ang'][b][None,:,None,:,:])
  Bs,Bu,Bss,Bsu,Buu=B
  def lift(v):return v[:,:,None,None]
  de=2*np.sum(fs[:,:,None,None,:]*Bs,-1);df=np.sum(fu[:,:,None,None,:]*Bs+fs[:,:,None,None,:]*Bu,-1);dg=2*np.sum(fu[:,:,None,None,:]*Bu,-1)
  dcross=np.cross(Bs,fu[:,:,None,None,:])+np.cross(fs[:,:,None,None,:],Bu)
  dnormal=(dcross-normal[:,:,None,None,:]*np.sum(normal[:,:,None,None,:]*dcross,-1)[:,:,:,:,None])/area[:,:,None,None,None]
  dl=np.sum(dnormal*fss[:,:,None,None,:]+normal[:,:,None,None,:]*Bss,-1)
  dm=np.sum(dnormal*fsu[:,:,None,None,:]+normal[:,:,None,None,:]*Bsu,-1)
  dn=np.sum(dnormal*fuu[:,:,None,None,:]+normal[:,:,None,None,:]*Buu,-1)
  ddet=lift(gg)*de+lift(e)*dg-2*lift(f)*df
  dT=lift(l)*dg+lift(gg)*dl+lift(n)*de+lift(e)*dn-2*lift(m)*df-2*lift(f)*dm
  dP=lift(n)*dl+lift(l)*dn-2*lift(m)*dm
  dQ=(4*lift(H)*dT-2*dP+lift(2*K-8*H*H)*ddet)/lift(det)
  jac=self.weight*dQ/(2*self.limit*lift(root))*(root>self.limit)[:,:,None,None]
  B0=g['r'][0][:,None,:,None,None]*g['ang'][0][None,:,None,:,:]
  dsupport=-np.sum(B0*normal[:,:,None,None,:]+x[:,:,None,None,:]*dnormal,axis=-1)
  sjac=-10*dsupport*(support<.09)[:,:,None,None]
  return np.r_[base,jac.reshape(-1,self.size),sjac.reshape(-1,self.size)]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--B',type=float,default=.7);ap.add_argument('--height',type=float,default=.55);ap.add_argument('--speed',type=float,default=.85);ap.add_argument('--rc',type=float,default=.25);ap.add_argument('--nc',type=int,default=18);ap.add_argument('--m',type=int,default=6);ap.add_argument('--nfev',type=int,default=180);ap.add_argument('--curvature-limit',type=float,default=12);ap.add_argument('--curvature-weight',type=float,default=.2);ap.add_argument('--neck-seed',type=float,default=0);ap.add_argument('--seed',type=Path);ap.add_argument('--out',type=Path,required=True)
 ap.add_argument('--bend',type=float,default=.4)
 a=ap.parse_args();model=CurvedModel(bend=a.bend,B=a.B,height=a.height,speed=a.speed,rc=a.rc,nc=a.nc,m=a.m,curvature_limit=a.curvature_limit,curvature_weight=a.curvature_weight)
 nodes,_=np.polynomial.legendre.leggauss(5);ss=np.concatenate([l+(r-l)*(nodes+1)/2 for l,r in zip(model.intervals[:-1],model.intervals[1:])]);nu=max(48,8*a.m);grid=model.prepare(ss,np.arange(nu)*2*np.pi/nu)
 q=np.zeros(model.size)
 if a.seed:q=np.array(json.loads(a.seed.read_text())['q'])
 if a.neck_seed:
  radial=model.radial(ss)[0];bump=np.sin(np.pi*ss)**4;target=-a.neck_seed*bump
  co=np.linalg.lstsq(radial,target,rcond=None)[0];q=q.reshape(model.shape);q[:,0]+=co;q[:,model.m]+=co;q=q.ravel()
 t=time.monotonic();count=0
 def fun(q):
  nonlocal count
  count+=1;r=model.residual_jac(q,grid)
  if count%10==1:print(json.dumps({'eval':count,'rms':float(np.sqrt(np.mean(r*r))),'max':float(np.max(np.abs(r))),'seconds':time.monotonic()-t}),flush=True)
  return r
 result=least_squares(fun,q,jac=lambda q:model.residual_jac(q,grid,True),method='lm',max_nfev=a.nfev,ftol=1e-11,gtol=1e-11,xtol=1e-11,x_scale='jac')
 gg=model.prepare(np.linspace(0,1,257),np.arange(192)*2*np.pi/192)
 xx,xxs,xxu=model.geometry(result.x,gg);nn=-np.cross(xxs,xxu);nn/=np.linalg.norm(nn,axis=-1)[:,:,None]
 support_min=float(np.sum(xx*nn,-1).min())
 out=dict(actual_meridian_speed=model.speed,meridian_asymmetry=model.asym,support_min=support_min,parameters={k:v for k,v in vars(a).items()if k not in ['out','seed']},q=result.x.tolist(),shape=model.shape,success=bool(result.success),message=result.message,nfev=result.nfev,cost=result.cost,audit=model.audit(result.x,257,192),seconds=time.monotonic()-t)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='q'}),flush=True)
if __name__=='__main__':main()
