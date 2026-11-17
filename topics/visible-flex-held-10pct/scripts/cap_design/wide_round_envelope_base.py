#!/usr/bin/env python3
"""Experimental C2 ellipse-to-circle cap metric design; no exactness claim."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline,PchipInterpolator
from scipy.integrate import cumulative_simpson
from scipy.optimize import least_squares
from scipy.spatial import cKDTree

class Model:
 def __init__(self,A=1,B=.7,rc=.25,height=.55,speed=.85,nc=18,m=6):
  self.A,self.B,self.rc,self.height,self.speed=A,B,rc,height,speed
  self.nc,self.m=nc,m
  self.odd=np.arange(1,2*m,2)
  self.even=np.arange(0,2*m,2)
  self.shape=(nc-6,3*m)
  self.size=np.prod(self.shape)
  interior=np.linspace(0,1,nc-4)[1:-1]
  knots=np.r_[np.zeros(6),interior,np.ones(6)]
  self.spline=BSpline(knots,np.eye(nc),5,extrapolate=False)
  p=np.linspace(0,2*np.pi,65537)
  v=np.sqrt(A*A*np.sin(p)**2+B*B*np.cos(p)**2)
  integral=cumulative_simpson(v,x=p,initial=0)
  self.a0=integral[-1]/(2*np.pi)
  self.inv=PchipInterpolator(integral/self.a0,p)
  self.intervals=np.unique(knots)
 def radial(self,s):
  return [self.spline.derivative(d)(s)[:,3:-3] for d in range(3)]
 def angles(self,u):
  odd,even=self.odd,self.even
  base=np.zeros((len(u),3*self.m,3));d1=base.copy();d2=base.copy()
  base[:,:self.m,0]=np.cos(u[:,None]*odd);d1[:,:self.m,0]=-odd*np.sin(u[:,None]*odd);d2[:,:self.m,0]=-odd**2*np.cos(u[:,None]*odd)
  base[:,self.m:2*self.m,1]=np.sin(u[:,None]*odd);d1[:,self.m:2*self.m,1]=odd*np.cos(u[:,None]*odd);d2[:,self.m:2*self.m,1]=-odd**2*np.sin(u[:,None]*odd)
  base[:,2*self.m:,2]=np.cos(u[:,None]*even);d1[:,2*self.m:,2]=-even*np.sin(u[:,None]*even);d2[:,2*self.m:,2]=-even**2*np.cos(u[:,None]*even)
  return base,d1,d2
 def curve(self,u):
  p=self.inv(np.mod(u,2*np.pi));a,b=self.A,self.B
  v=np.sqrt(a*a*np.sin(p)**2+b*b*np.cos(p)**2);pp=self.a0/v
  ppp=-self.a0**2*(a*a-b*b)*np.sin(p)*np.cos(p)/v**4
  c=np.stack((a*np.cos(p),b*np.sin(p),np.zeros_like(p)),axis=-1)
  cp=np.stack((-a*np.sin(p),b*np.cos(p),np.zeros_like(p)),axis=-1)
  cpp=np.stack((-a*np.cos(p),-b*np.sin(p),np.zeros_like(p)),axis=-1)
  return c,cp*pp[:,None],cpp*pp[:,None]**2+cp*ppp[:,None]
 def prepare(self,s,u):
  s,u=np.asarray(s),np.asarray(u)
  polynomials=[np.array([1,0,0,-10,15,-6]),np.array([0,0,0,10,-15,6]),np.array([0,1,0,-6,8,-3]),np.array([0,0,0,-4,7,-3])]
  hp=[[np.polynomial.polynomial.polyval(s,np.polynomial.polynomial.polyder(p,d)) for p in polynomials]for d in range(3)]
  c=self.curve(u);circle=np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1)
  cp=np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1)
  circles=[circle,cp,-circle]
  ez=np.array([0.,0.,1.]);end=self.rc*circle+self.height*ez
  geom=[]
  for ds,du in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
   h=hp[ds]
   endpoint=self.rc*circles[du]+(self.height*ez if du==0 else 0)
   row=h[0][:,None,None]*c[du]+h[1][:,None,None]*endpoint-h[3][:,None,None]*self.speed*circles[du]
   if du==0: row+=h[2][:,None,None]*self.speed*ez
   geom.append(row)
  return dict(s=s,u=u,geom=geom,r=self.radial(s),ang=self.angles(u))
 def geometry(self,q,g,second=False):
  q=q.reshape(self.shape)
  orders=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
  return [g['geom'][i]+np.einsum('sj,ucd,jc->sud',g['r'][a],g['ang'][b],q,optimize=True)for i,(a,b)in enumerate(orders[:6 if second else 3])]
 def residual_jac(self,q,g,need_jac=False):
  x,fs,fu=self.geometry(q,g)
  e=np.sum(fs*fs,axis=-1);f=np.sum(fs*fu,axis=-1);gg=np.sum(fu*fu,axis=-1)
  me=np.mean(e,axis=1,keepdims=True);mg=np.mean(gg,axis=1,keepdims=True)
  me=np.maximum(me,1e-15);mg=np.maximum(mg,1e-15)
  r=np.stack((e/me-1,np.sqrt(2)*f/np.sqrt(me*mg),gg/mg-1),axis=-1)
  floor=.02
  barriers=10*np.sqrt(len(g['u']))*np.stack((np.maximum(floor-me[:,0],0),np.maximum(floor-mg[:,0],0),np.maximum(me[:,0]-16,0),np.maximum(mg[:,0]-1.2,0)),axis=-1)
  rho2=np.sum(x*x,axis=-1)
  wp=x-np.array([0.,1.,0.]);wm=x-np.array([0.,-1.,0.])
  dp=np.sum(wp*wp,axis=-1);dm=np.sum(wm*wm,axis=-1)
  geo=10*np.stack((np.maximum(rho2-1.3**2,0),np.maximum(.30**2-dp,0),np.maximum(.30**2-dm,0),np.maximum(x[:,:,2]-.85,0),np.maximum(-x[:,:,2],0)),axis=-1)
  if not need_jac:return np.r_[r.ravel(),barriers.ravel(),geo.ravel()]
  Bs=g['r'][1][:,None,:,None,None]*g['ang'][0][None,:,None,:,:]
  Bu=g['r'][0][:,None,:,None,None]*g['ang'][1][None,:,None,:,:]
  de=2*np.sum(fs[:,:,None,None,:]*Bs,axis=-1)
  df=np.sum(fu[:,:,None,None,:]*Bs+fs[:,:,None,None,:]*Bu,axis=-1)
  dg=2*np.sum(fu[:,:,None,None,:]*Bu,axis=-1)
  dme=np.mean(de,axis=1,keepdims=True);dmg=np.mean(dg,axis=1,keepdims=True)
  ME=me[:,:,None,None];MG=mg[:,:,None,None]
  je=de/ME-e[:,:,None,None]*dme/ME**2
  jf=np.sqrt(2)*df/np.sqrt(ME*MG)-r[:,:,1,None,None]*.5*(dme/ME+dmg/MG)
  jg=dg/MG-gg[:,:,None,None]*dmg/MG**2
  j=np.stack((je,jf,jg),axis=2).reshape(-1,self.size)
  jb=10*np.sqrt(len(g['u']))*np.stack((-dme[:,0]*(me[:,0]<floor)[:,None,None],-dmg[:,0]*(mg[:,0]<floor)[:,None,None],dme[:,0]*(me[:,0]>16)[:,None,None],dmg[:,0]*(mg[:,0]>1.2)[:,None,None]),axis=1).reshape(-1,self.size)
  B0=g['r'][0][:,None,:,None,None]*g['ang'][0][None,:,None,:,:]
  jgeo=10*np.stack((2*np.sum(x[:,:,None,None,:]*B0,axis=-1)*(rho2>1.3**2)[:,:,None,None],-2*np.sum(wp[:,:,None,None,:]*B0,axis=-1)*(dp<.30**2)[:,:,None,None],-2*np.sum(wm[:,:,None,None,:]*B0,axis=-1)*(dm<.30**2)[:,:,None,None],B0[:,:,:,:,2]*(x[:,:,2]>.85)[:,:,None,None],-B0[:,:,:,:,2]*(x[:,:,2]<0)[:,:,None,None]),axis=2).reshape(-1,self.size)
  return np.r_[j,jb,jgeo]
 def audit(self,q,n=129,nu=128):
  g=self.prepare(np.linspace(0,1,n),np.arange(nu)*2*np.pi/nu)
  x,fs,fu,fss,fsu,fuu=self.geometry(q,g,True)
  e=np.sum(fs*fs,axis=-1);f=np.sum(fs*fu,axis=-1);gg=np.sum(fu*fu,axis=-1)
  me=e.mean(1,keepdims=True);mg=gg.mean(1,keepdims=True)
  de=e/me-1;df=f/np.sqrt(me*mg);dg=gg/mg-1
  err=np.maximum(np.abs((de+dg)/2+np.sqrt((de-dg)**2/4+df*df)),np.abs((de+dg)/2-np.sqrt((de-dg)**2/4+df*df)))
  cross=np.cross(fs,fu);area=np.linalg.norm(cross,axis=-1);normal=cross/area[:,:,None]
  l=np.sum(normal*fss,axis=-1);m=np.sum(normal*fsu,axis=-1);nn=np.sum(normal*fuu,axis=-1)
  det=e*gg-f*f;H=(gg*l+e*nn-2*f*m)/(2*det);K=(l*nn-m*m)/det
  kap=np.abs(H)+np.sqrt(np.maximum(H*H-K,0))
  return dict(grid=[n,nu],metric_max=float(err.max()),metric_rms=float(np.sqrt(np.mean(de*de+2*df*df+dg*dg))),max_curvature=float(kap.max()),min_area=float(area.min()),E_range=[float(me.min()),float(me.max())],G_range=[float(mg.min()),float(mg.max())],coordinate_min=x.min(axis=(0,1)).tolist(),coordinate_max=x.max(axis=(0,1)).tolist(),scope='finite samples only, designed g varies by candidate; no exactness/refinement/reach claim')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--B',type=float,default=.7);ap.add_argument('--height',type=float,default=.55);ap.add_argument('--speed',type=float,default=.85);ap.add_argument('--rc',type=float,default=.25);ap.add_argument('--nc',type=int,default=18);ap.add_argument('--m',type=int,default=6);ap.add_argument('--nfev',type=int,default=200);ap.add_argument('--seed',type=Path);ap.add_argument('--out',type=Path,required=True)
 a=ap.parse_args();model=Model(B=a.B,height=a.height,speed=a.speed,rc=a.rc,nc=a.nc,m=a.m)
 nodes,_=np.polynomial.legendre.leggauss(4);ss=np.concatenate([l+(r-l)*(nodes+1)/2 for l,r in zip(model.intervals[:-1],model.intervals[1:])]);nu=max(32,6*a.m)
 grid=model.prepare(ss,np.arange(nu)*2*np.pi/nu)
 q=np.zeros(model.size)
 if a.seed:
  data=json.loads(a.seed.read_text());q=np.array(data['q'])
 t=time.monotonic();count=0
 def fun(q):
  nonlocal count
  count+=1;r=model.residual_jac(q,grid)
  if count%10==1:print(json.dumps({'eval':count,'rms':float(np.sqrt(np.mean(r*r))),'max':float(np.max(np.abs(r))),'seconds':time.monotonic()-t}),flush=True)
  return r
 result=least_squares(fun,q,jac=lambda q:model.residual_jac(q,grid,True),method='lm',max_nfev=a.nfev,ftol=1e-11,gtol=1e-11,xtol=1e-11,x_scale='jac')
 out=dict(parameters={k:v for k,v in vars(a).items()if k not in ['out','seed']},q=result.x.tolist(),shape=model.shape,success=bool(result.success),message=result.message,nfev=result.nfev,cost=result.cost,audit=model.audit(result.x),seconds=time.monotonic()-t)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='q'}),flush=True)
if __name__=='__main__':main()
