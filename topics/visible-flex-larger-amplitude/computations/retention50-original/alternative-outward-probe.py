#!/usr/bin/env python3
"""Finite Fourier Frenet IVP probe for a strong planar m=2 support core.

The fixed angular coordinate is the initial normal angle phi. Its material
metric is ds^2 + a(s)^2 rho0(phi)^2 dphi^2. This preserves the initial core's
short Fourier representation without forcing a circle arclength chart.
Only an outward acceleration/constant-speed leg is integrated; no closed
surface, exact infinite-mode existence, or all-time certificate is claimed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

class Probe:
 def __init__(self,A=.38,M=12,N=256,v=.6,S=.7,amax=1.3,coast_at=None,coast_length=.1):
  self.A=A;self.M=M;self.N=N;self.v=v;self.S=S;self.amax=amax
  self.coast_at=coast_at;self.coast_length=coast_length
  self.n=3*M+2;self.phi=2*np.pi*np.arange(N)/N
  self.freq=2*np.arange(M+1);self.C=np.cos(self.freq[:,None]*self.phi);self.Sn=np.sin(self.freq[:,None]*self.phi)
  self.C1=-self.freq[:,None]*self.Sn;self.S1=self.freq[:,None]*self.C
  self.C2=-self.freq[:,None]**2*self.C;self.S2=-self.freq[:,None]**2*self.Sn
  self.rho0=1-3*A*np.cos(2*self.phi)+15*A/(10*np.sqrt(2))*np.cos(4*self.phi)
  self.s_end=S+(amax-1-.5*v*S)/v
  if self.s_end<S:raise ValueError('amax must exceed ramp endpoint')
  self.calls=0;self.min_margin=1.;self.last_s=0.
 def profile(self,s):
  if self.coast_at is not None and s>self.coast_at:
   s0=self.coast_at;L=self.coast_length;u0=s0/self.S
   a0=1+self.v*self.S*(u0**3-u0**4/2);v0=self.v*(3*u0*u0-2*u0**3);q0=6*self.v/self.S*u0*(1-u0)
   if s<s0+L:
    u=(s-s0)/L
    return a0+v0*L*u+q0*L*L*(u*u/2-u**3/3+u**4/12),v0+q0*L*(u-u*u+u**3/3),q0*(1-u)**2
   a1=a0+v0*L+q0*L*L/4;v1=v0+q0*L/3
   return a1+v1*(s-s0-L),v1,0.
  if s<self.S:
   u=s/self.S; a=1+self.v*self.S*(u**3-u**4/2);ap=self.v*(3*u*u-2*u**3);app=6*self.v/self.S*u*(1-u)
  else:a=1+.5*self.v*self.S+self.v*(s-self.S);ap=self.v;app=0.
  return a,ap,app
 def unpack(self,y):
  return y[:self.M+1],y[self.M+1:2*self.M+1],y[2*self.M+1:]
 def jet(self,y):
  r,t,z=self.unpack(y)
  R=r@self.C;T=t@self.Sn[1:];Z=z@self.C
  Rp=r@self.C1;Tp=t@self.S1[1:];Zp=z@self.C1
  Rpp=r@self.C2;Tpp=t@self.S2[1:];Zpp=z@self.C2
  F=np.stack([R,T,Z],axis=1)
  d=np.stack([Rp-T,Tp+R,Zp],axis=1)
  dd=np.stack([Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp],axis=1)
  return F,d,dd
 def project(self,V):
  r=(2/self.N)*(self.C@V[:,0]);r[0]*=.5
  t=(2/self.N)*(self.Sn[1:]@V[:,1])
  z=(2/self.N)*(self.C@V[:,2]);z[0]*=.5
  return np.r_[r,t,z]
 def frame(self,s,y,strict=True):
  F,d,dd=self.jet(y);lam=np.sqrt(np.sum(d*d,axis=1));T=d/lam[:,None]
  dt=np.sum(dd*T,axis=1);nv=dd-dt[:,None]*T;nn=np.sqrt(np.sum(nv*nv,axis=1));N=nv/nn[:,None]
  kap=nn/lam**2;B=np.cross(T,N);a,ap,app=self.profile(s);al=-ap/(a*kap);margin=1-al**2
  if strict and np.min(margin.real)<=0:raise FloatingPointError(f'domain at s={s:.12g}, margin={np.min(margin.real):.12g}')
  be=np.sqrt(margin);V=al[:,None]*N+be[:,None]*B
  return dict(F=F,d=d,dd=dd,lam=lam,T=T,dt=dt,nv=nv,nn=nn,N=N,kap=kap,B=B,a=a,ap=ap,app=app,al=al,be=be,margin=margin,V=V)
 def fun(self,s,y):
  self.calls+=1;self.last_s=s;fr=self.frame(s,y)
  self.min_margin=min(self.min_margin,float(np.min(fr['margin'].real)))
  return self.project(fr['V'])
 def stats(self,s,y):
  fr=self.frame(s,y);yp=self.project(fr['V']);V,dV,ddV=self.jet(yp)
  E=np.sum(V*V,axis=1);FF=np.sum(V*fr['d'],axis=1);G=fr['lam']**2
  metric=max(np.max(abs(E-1)),np.max(abs(FF)/(fr['a']*self.rho0)),np.max(abs(G/(fr['a']**2*self.rho0**2)-1)))
  # Exact derivative of this finite projected ODE via a complex-step state JVP.
  h=1e-25
  state_jvp=self.project(self.frame(s,y.astype(complex)+1j*h*yp,strict=False)['V']).imag/h
  da=-fr['app']/(fr['a']*fr['kap'])+fr['ap']**2/(fr['a']**2*fr['kap'])
  db=-fr['al']*da/fr['be']
  explicit=self.project(da[:,None]*fr['N']+db[:,None]*fr['B'])
  Acc=self.jet(state_jvp+explicit)[0]
  normal=np.cross(V,fr['d']);normal/=np.linalg.norm(normal,axis=1)[:,None]
  IIe=np.sum(Acc*normal,axis=1);IIf=np.sum(dV*normal,axis=1);IIg=np.sum(fr['dd']*normal,axis=1)
  det=E*G-FF**2;tr=(IIe*G+IIg*E-2*IIf*FF)/det;kdet=(IIe*IIg-IIf**2)/det
  dis=np.maximum(0,tr**2-4*kdet);K=float(np.max((np.abs(tr)+np.sqrt(dis))/2))
  rad=np.linalg.norm(fr['F'][:,:2],axis=1);z=fr['F'][:,2]
  return dict(s=float(s),a=fr['a'],ap=fr['ap'],margin=float(fr['margin'].min()),metric_sample=float(metric),kappa_curve_min=float(fr['kap'].min()),kappa_curve_max=float(fr['kap'].max()),surface_kappa_sample=K,max_radius=float(rad.max()),height_mean=float(z.mean()),height_min=float(z.min()),height_max=float(z.max()),tail_fourier_max=float(max(abs(y[self.M]),abs(y[2*self.M]),abs(y[-1]))))
 def run(self,rtol=1e-9,steps=80,maxstep=.0005,end_s=None):
  if end_s is not None:self.s_end=float(end_s)
  y=np.zeros(self.n);y[0]=1;y[1]=self.A;y[2]=-self.A/(10*np.sqrt(2));y[self.M+1]=-2*self.A;y[self.M+2]=4*self.A/(10*np.sqrt(2))
  # Integrate with bounded macroscopic segments so every successful state is retained.
  rows=[self.stats(0,y)];status='success';last=0.;begin=time.time()
  for right in np.linspace(0,self.s_end,steps+1)[1:]:
   try:
    sol=solve_ivp(self.fun,(last,right),y,method='DOP853',rtol=rtol,atol=rtol*.01,max_step=min(maxstep,(right-last)/2))
    if not sol.success:raise RuntimeError(sol.message)
    y=sol.y[:,-1];last=float(right);rows.append(self.stats(last,y))
   except Exception as e:status=repr(e);break
  return dict(scope=__doc__,config=dict(A=self.A,M=self.M,N=self.N,v=self.v,S=self.S,amax=self.amax,rtol=rtol,steps=steps,maxstep=maxstep,end_s=end_s,coast_at=self.coast_at,coast_length=self.coast_length),status=status,reached_s=last,target_s=self.s_end,calls=self.calls,seconds=time.time()-begin,rows=rows,final_coefficients=y.tolist())

def main():
 p=argparse.ArgumentParser();p.add_argument('--A',type=float,default=.38);p.add_argument('--M',type=int,default=12);p.add_argument('--N',type=int,default=256);p.add_argument('--v',type=float,default=.6);p.add_argument('--S',type=float,default=.7);p.add_argument('--amax',type=float,default=1.3);p.add_argument('--rtol',type=float,default=1e-9);p.add_argument('--steps',type=int,default=80);p.add_argument('--coast-at',type=float);p.add_argument('--coast-length',type=float,default=.1);p.add_argument('--end-s',type=float);p.add_argument('--maxstep',type=float,default=.0005);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 r=Probe(a.A,a.M,a.N,a.v,a.S,a.amax,a.coast_at,a.coast_length).run(a.rtol,a.steps,a.maxstep,a.end_s);a.out.write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:r[k] for k in ['config','status','reached_s','target_s','calls','seconds']}));print(json.dumps(r['rows'][-1]))
if __name__=='__main__':main()
