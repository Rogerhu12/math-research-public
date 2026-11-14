#!/usr/bin/env python3
"""Direct C2 angle connector from a Hermite prefix to a physical tail cut.

All reported roots are for the linearized Frenet equation and a finite
linear tail DN. They are profile/initial-guess designs, not closed nonlinear
solutions. Bernstein angle control bounds make |a'|<1 explicit.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares,minimize
from scipy.special import comb
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_direct_scan',P/'root_profile_scan.py');scan=importlib.util.module_from_spec(sp);sp.loader.exec_module(scan)

class DirectConnector:
 def __init__(self,a0,v0,cut,length,angles,degree=32):
  self.a0=float(a0);self.v0=float(v0);self.cut=cut;self.L=float(length);self.angles=np.asarray(angles,float);self.n=int(degree)
  self.p0=math.asin(v0);self.p1=-math.atan2(1.,cut['backgroundSlope']);self.ps1=-cut['backgroundSecond']/(1+cut['backgroundSlope']**2)**1.5
  nodes=np.r_[0.,np.linspace(.15,.9,len(angles)),1.];vals=np.r_[self.p0,angles,self.p1]
  self.control=np.interp(np.arange(self.n+1)/self.n,nodes,vals);self.control[0]=self.control[1]=self.p0;self.control[-1]=self.p1;self.control[-2]=self.p1-self.L*self.ps1/self.n
  if max(abs(self.control))>=math.pi/2:raise ValueError('Bernstein angle hull leaves |a prime|<1')
  self.j=np.arange(self.n+1);self.binom=comb(self.n,self.j);self.j1=np.arange(self.n);self.binom1=comb(self.n-1,self.j1);self.dc=self.n*np.diff(self.control)
  self.g,self.gw=np.polynomial.legendre.leggauss(64)
 def angle(self,u):
  u=np.asarray(u);basis=self.binom*u[...,None]**self.j*(1-u[...,None])**(self.n-self.j)
  first=self.binom1*u[...,None]**self.j1*(1-u[...,None])**(self.n-1-self.j1)
  return basis@self.control,first@self.dc
 def scalar_angle(self,u):
  return float(np.dot(self.binom*u**self.j*(1-u)**(self.n-self.j),self.control))
 def profile(self,s):
  scalar=np.ndim(s)==0;u=np.asarray(s,float)/self.L;phi,pu=self.angle(u)
  phi_q,_=self.angle(u[...,None]*(self.g+1)/2)
  a=self.a0+self.L*u/2*(np.sin(phi_q)@self.gw)
  out=a,np.sin(phi),np.cos(phi)*pu/self.L
  return tuple(float(z)for z in out)if scalar else out
 def summary(self):
  u=np.linspace(0,1,1001);phi,pu=self.angle(u);a,v,acc=self.profile(self.L*u)
  return dict(length=self.L,angles=self.angles.tolist(),degree=self.n,bernstein_angle_control=self.control.tolist(),bernstein_abs_angle_bound=float(abs(self.control).max()),initial_jets=list(self.profile(0.)),terminal_jets=list(self.profile(self.L)),radius_min=float(a.min()),radius_max=float(a.max()),background_height=float(self.L*np.trapezoid(np.cos(phi),u)),background_kappa_sample=float(max(abs(pu/self.L).max(),(np.cos(phi)/a).max())),speed_abs_max=float(abs(v).max()))

class Search:
 def __init__(self,port,V=.35,S=.65,k0=.45,degree=32):
  self.V=V;self.S=S;self.k0=k0;self.delta=V*S/2+k0*S*S/12;self.a0=1+self.delta;self.degree=degree;self.terminal=[]
  for m in (2,4):
   cut,slope=scan.parse_port(port,m);r,w=cut['radius'],cut['backgroundSlope'];z=np.array([-w*(r*slope-m*m)/(m*m-1),1.]);self.terminal.append(z/np.linalg.norm(z))
  self.cut=cut;self.back=[]
  def prefix(s):
   u=s/S;b=k0*S;c=3*V-2*b;d=b-2*V
   return 1+S*(b*u*u/2+c*u**3/3+d*u**4/4),b*u+c*u*u+d*u**3
  for m in (2,4):
   sol=solve_ivp(lambda s,y:(scan.linear_matrix(*prefix(s),m)@y.reshape(2,2)).ravel(),(S,0.),np.eye(2).ravel(),method='DOP853',rtol=2e-12,atol=2e-14,max_step=S/60)
   if not sol.success:raise RuntimeError(sol.message)
   self.back.append(sol.y[:,-1].reshape(2,2))
  s=np.linspace(0,S,1001);self.prefix_height=float(np.trapezoid([math.sqrt(1-prefix(x)[1]**2)for x in s],s))
 def residual(self,x,details=False):
  conn=DirectConnector(self.a0,self.V,self.cut,x[0],x[1:],self.degree);state=np.r_[self.cut['radius'],self.terminal[0],self.terminal[1],0.];gains=np.ones(2)
  def rhs(u,y):
   phi=conn.scalar_angle(u);v=math.sin(phi);b=math.cos(phi);L=conn.L;a=y[0]
   if a<=.03:raise ValueError('Radius left positive search domain')
   f,g,F,G=y[1:5]
   return np.array([L*v,L/a*(-3*v*f-4*b*g),L/a*(3*v*v/b*f+4*v*g),L/a*(-15*v*F-16*b*G),L/a*(15*v*v/b*F+16*v*G),L*b])
  us=np.linspace(1.,0.,11)
  for right,left in zip(us[:-1],us[1:]):
   sol=solve_ivp(rhs,(right,left),state,method='DOP853',rtol=3e-9,atol=3e-11,max_step=.04)
   if not sol.success:raise RuntimeError(sol.message)
   state=sol.y[:,-1]
   for j in range(2):
    sl=slice(1+2*j,3+2*j);nn=np.linalg.norm(state[sl]);state[sl]/=nn;gains[j]*=nn
  core=[]
  for j in range(2):
   z=self.back[j]@state[1+2*j:3+2*j];z/=np.linalg.norm(z);core.append(z)
  res=np.array([state[0]-self.a0,core[0][1],core[1][1]])
  return (res,conn,core,gains,-state[-1])if details else res
 def summary(self,x):
  res,conn,core,gains,height=self.residual(x,True);row=conn.summary();row.update(x=list(map(float,x)),residual=res.tolist(),residual_max=float(abs(res).max()),core_lines=dict(m2=core[0].tolist(),m4=core[1].tolist()),transport_norm_gains=gains.tolist(),connector_height_backward=height,prefix_height=self.prefix_height,total_background_height=self.prefix_height+height)
  return row
 def run(self,seeds=6,out=None):
  lo=np.r_[max(.55,self.a0-self.cut['radius']+.015),np.full(6,-1.56)];hi=np.r_[1.45,np.full(6,.6)];rng=np.random.default_rng(20261110);rows=[];attempts=[];begin=time.time()
  report=dict(scope=__doc__,cut=self.cut,V=self.V,S=self.S,k0=self.k0,delta=self.delta,degree=self.degree,rows=rows,attempts=attempts)
  for index in range(seeds):
   L=rng.uniform(lo[0]+.03,min(hi[0]-.03,1.25));u=np.linspace(.15,.9,6);p0=math.asin(self.V);p1=-math.atan2(1.,self.cut['backgroundSlope']);ang=p0+(p1-p0)*(3*u*u-2*u**3)-rng.uniform(.1,.7)*np.sin(math.pi*u)+rng.normal(0,.1,6)
   x=np.clip(np.r_[L,ang],lo+1e-6,hi-1e-6)
   try:
    z=least_squares(self.residual,x,bounds=(lo,hi),xtol=5e-9,ftol=5e-9,gtol=5e-9,max_nfev=110)
    row=self.summary(z.x);attempts.append(dict(seed=index,residual_max=row['residual_max'],x=row['x'],height=row['total_background_height'],kappa=row['background_kappa_sample']))
    if row['residual_max']<2e-6 and not any(np.linalg.norm(np.asarray(r['x'])-z.x)<1e-4 for r in rows):rows.append(row);rows.sort(key=lambda r:r['total_background_height'])
    print(json.dumps(dict(event='seed',index=index,residual=row['residual_max'],height=row['total_background_height'],kappa=row['background_kappa_sample'])),flush=True)
   except Exception as e:attempts.append(dict(seed=index,error=repr(e)));print(json.dumps(dict(event='error',index=index,error=repr(e))),flush=True)
   report['seconds']=time.time()-begin
   if out:out.write_text(json.dumps(report,indent=2)+'\n')
  return report

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--V',type=float,default=.35);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--degree',type=int,default=32);p.add_argument('--seeds',type=int,default=6);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 report=Search(json.loads(args.port.read_text()),args.V,args.S,args.k0,args.degree).run(args.seeds,args.out);report.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),port_sha256=hashlib.sha256(args.port.read_bytes()).hexdigest());args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',seconds=report['seconds'],candidates=len(report['rows']),best=report['rows'][:1])))
if __name__=='__main__':main()
