"""Exact smooth isometric cone-annulus family from closed spherical curves.

The inverse arclength is defined by quadrature, and all material derivatives
below are analytic chain-rule formulas. This is a local flat-g example only;
no match to the prefix or to the infinite oscillatory tail is asserted.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

class ConePlateau:
 def __init__(self,w=.00358,amplitude=.0088):
  self.w=float(w);self.a=float(amplitude);self.R=math.hypot(1,w)
  if not(0<w<=.01 and 0<=self.a<=.01):raise ValueError('Proved parameter window is 0<w<=.01, 0<=a<=.01')
  self.b=math.atan(w)if self.a==0 else brentq(lambda b:self.length(b)-2*math.pi,self.a,.1,xtol=5e-15,rtol=4*np.finfo(float).eps)
 def speed(self,p,b=None):
  if b is None:b=self.b
  B=b+self.a*math.cos(2*p);Bp=-2*self.a*math.sin(2*p)
  return self.R*math.sqrt(math.cos(B)**2+Bp*Bp)
 def length(self,b):return quad(lambda p:self.speed(p,b),0,2*math.pi,epsabs=2e-13,epsrel=2e-13,limit=100)[0]
 def u_of_phi(self,p):return quad(lambda x:self.speed(x),0,float(p),epsabs=1e-13,epsrel=1e-13,limit=100)[0]
 def phi_of_u(self,u):
  u=float(u)%(2*math.pi)
  if u==0:return 0.
  return brentq(lambda p:self.u_of_phi(p)-u,0,2*math.pi,xtol=3e-14,rtol=4*np.finfo(float).eps)
 def spherical(self,phi):
  p=np.asarray(phi);B=self.b+self.a*np.cos(2*p);Bp=-2*self.a*np.sin(2*p);Bpp=-4*self.a*np.cos(2*p);c=np.cos(B);s=np.sin(B);er=np.stack([np.cos(p),np.sin(p),np.zeros_like(p)],-1);et=np.stack([-np.sin(p),np.cos(p),np.zeros_like(p)],-1);ez=np.zeros_like(er);ez[...,2]=1
  g=self.R*(c[...,None]*er+s[...,None]*ez)
  gp=self.R*((-s*Bp)[...,None]*er+c[...,None]*et+(c*Bp)[...,None]*ez)
  gpp=self.R*((-c*(1+Bp*Bp)-s*Bpp)[...,None]*er+(-2*s*Bp)[...,None]*et+(-s*Bp*Bp+c*Bpp)[...,None]*ez)
  speed=self.R*np.sqrt(c*c+Bp*Bp);speedp=self.R*(-c*s*Bp+Bp*Bpp)/np.sqrt(c*c+Bp*Bp)
  gu=gp/speed[...,None];guu=gpp/speed[...,None]**2-gp*speedp[...,None]/speed[...,None]**3
  return g,gu,guu
 def evaluate(self,r,u):
  rr,uu=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(u,dtype=float));phi=np.array([self.phi_of_u(v)for v in uu.ravel()]).reshape(uu.shape);g,gu,guu=self.spherical(phi)
  return dict(X=rr[...,None]*g,Xr=g,Xu=rr[...,None]*gu,Xrr=np.zeros_like(g),Xru=gu,Xuu=rr[...,None]*guu)
 def diagnostics(self,r=.25,N=1024,M=16):
  u=np.arange(N)*2*np.pi/N;v=self.evaluate(r,u);Xr,Xu=v['Xr'],v['Xu'];E=np.sum(Xr*Xr,axis=-1);F=np.sum(Xr*Xu,axis=-1);G=np.sum(Xu*Xu,axis=-1);normal=np.cross(Xr,Xu);normal/=np.linalg.norm(normal,axis=-1)[:,None];curv=np.sum(normal*v['Xuu'],axis=-1)/r**2
  hz=v['Xr'][:,2];hu=v['Xru'][:,2];huu=v['Xuu'][:,2]/r;P=hu/self.w;Pt=huu/self.w;K=hz/self.w-1;A=1+K+(1+self.w**2)*Pt;D=1-self.w**2*(2*K+K*K+(1+self.w**2)*P*P);S=1-self.w**2*P*P;U=2*K+K*K+(1+self.w**2)*P*P;B=U/(np.sqrt(D)*(1+np.sqrt(D)))+(1+K)*Pt/(S*np.sqrt(D));phi=np.c_[np.ones(N),np.sqrt(2)*np.cos(u[:,None]*(2*np.arange(1,M+1))[None,:])];Gram=phi.T@((A/D**1.5)[:,None]*phi)/N
  return dict(w=self.w,amplitude=self.a,b=self.b,R=self.R,radius=r,angles=N,length_residual=self.length(self.b)-2*math.pi,metric_error=max(float(np.max(abs(E-self.R**2))),float(np.max(abs(F))),float(np.max(abs(G-r*r)))),minimum_nz=float(np.min(normal[:,2])),minimum_D=float(np.min(D)),minimum_S=float(np.min(S)),minimum_A=float(np.min(A)),maximum_A=float(np.max(A)),angular_normal_curvature_min=float(np.min(curv)),angular_normal_curvature_max=float(np.max(curv)),maximum_principal_curvature=float(np.max(abs(curv))),mean_momentum_density=float(np.mean(B)),gram_mode_count=M,gram_eigen_min=float(np.linalg.eigvalsh(Gram)[0]),height_cos2=float(2*np.mean(v['X'][:,2]*np.cos(2*u))),height_mean=float(np.mean(v['X'][:,2])),scope=__doc__)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--w',type=float,default=.00358);p.add_argument('--amplitude',type=float,default=.0088);p.add_argument('--radius',type=float,default=.25);p.add_argument('--out',type=Path,required=True);a=p.parse_args();d=ConePlateau(a.w,a.amplitude).diagnostics(a.radius);a.out.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
