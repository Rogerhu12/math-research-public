#!/usr/bin/env python3
"""C2 direct angle-turn/plateau/brake connector and two-mode linear search.

Finite linear-tail matching is only a design screen. Neither the strong
nonlinear turn nor the complete closed phase family is certified here.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_plateau_direct',P/'alternative-direct-tail-connector.py');direct=importlib.util.module_from_spec(sp);sp.loader.exec_module(direct)

class AnglePlateauConnector:
 def __init__(self,a0,v0,cut,turn_curvature=4.,peak_gap=None):
  self.a0=float(a0);self.v0=float(v0);self.cut=cut;self.K=float(turn_curvature);self.p0=math.asin(v0);self.p1=-math.atan2(1.,cut['backgroundSlope']);self.ps1=-cut['backgroundSecond']/(1+cut['backgroundSlope']**2)**1.5
  self.gap=(math.pi/2+self.p1)/2 if peak_gap is None else float(peak_gap);self.peak=self.p1-self.gap
  if self.K<=0 or not 0<self.gap<math.pi/2+self.p1 or self.ps1<=0:raise ValueError('Invalid plateau parameters')
  self.T=1.5*(self.p0-self.peak)/self.K;self.B=2*self.gap/self.ps1;self.sigma=-1
  self.g,self.gw=np.polynomial.legendre.leggauss(64)
  u=(self.g+1)/2
  self.dr_turn=self.T/2*float(np.dot(np.sin(self.p0+(self.peak-self.p0)*(3*u*u-2*u**3)),self.gw))
  self.dr_brake=self.B/2*float(np.dot(np.sin(self.peak+self.gap*u*u),self.gw))
  self.C=(cut['radius']-a0-self.dr_turn-self.dr_brake)/math.sin(self.peak)
  if self.C<0:raise ValueError('Negative plateau length')
  self.L=self.T+self.C+self.B;self.knots=np.array([0.,self.T,self.T+self.C,self.L])
 def profile(self,s):
  scalar=np.ndim(s)==0;s=np.asarray(s,float);u=np.clip(s/self.T,0.,1.);ut=np.clip((s-self.T-self.C)/self.B,0.,1.)
  pp=self.p0+(self.peak-self.p0)*(3*u*u-2*u**3);vp=np.sin(pp);ap=np.cos(pp)*(self.peak-self.p0)*6*u*(1-u)/self.T
  q=u[...,None]*(self.g+1)/2;pt=self.p0+(self.peak-self.p0)*(3*q*q-2*q**3)
  aa=self.a0+self.T*u/2*(np.sin(pt)@self.gw)
  middle=(s>self.T)&(s<=self.T+self.C);last=s>self.T+self.C
  a=np.where(middle,self.a0+self.dr_turn+math.sin(self.peak)*(s-self.T),aa);v=np.where(middle,math.sin(self.peak),vp);acc=np.where(middle,0.,ap)
  p2=self.peak+self.gap*ut*ut;q=ut[...,None]*(self.g+1)/2
  a2=self.a0+self.dr_turn+self.C*math.sin(self.peak)+self.B*ut/2*(np.sin(self.peak+self.gap*q*q)@self.gw)
  a=np.where(last,a2,a);v=np.where(last,np.sin(p2),v);acc=np.where(last,np.cos(p2)*2*self.gap*ut/self.B,acc)
  return tuple(float(z)for z in(a,v,acc))if scalar else(a,v,acc)
 def summary(self):
  s=np.unique(np.r_[np.linspace(0,self.T,301),np.linspace(self.T,self.T+self.C,301),np.linspace(self.T+self.C,self.L,151)]);a,v,acc=self.profile(s);b=np.sqrt(1-v*v)
  return dict(turn_curvature=self.K,peak_gap=self.gap,angle_initial=self.p0,angle_peak=self.peak,angle_terminal=self.p1,turn_length=self.T,plateau_length=self.C,brake_length=self.B,length=self.L,initial_jets=list(self.profile(0.)),terminal_jets=list(self.profile(self.L)),maximum_radius=float(a.max()),minimum_radius=float(a.min()),background_height=float(np.trapezoid(b,s)),background_kappa_sample=float(np.max(np.maximum(abs(acc)/b,b/a))))

def constant_transfer(a0,a1,v,m):
 b=math.sqrt(1-v*v);mm=m*m;M=np.array([[-(mm-1),-mm*b/v],[(mm-1)*v/b,mm]])
 return np.eye(2)+(a1/a0-1)*M

class Search(direct.Search):
 def residual(self,x,details=False):
  conn=AnglePlateauConnector(self.a0,self.V,self.cut,x[0],x[1]);state=np.r_[self.cut['radius'],self.terminal[0],self.terminal[1]];gains=np.ones(2)
  def leg(state,length,phase):
   def rhs(u,y):
    pp=phase(u);v=math.sin(pp);b=math.cos(pp);a=y[0];f,g,F,G=y[1:]
    return length*np.array([v,(-3*v*f-4*b*g)/a,(3*v*v/b*f+4*v*g)/a,(-15*v*F-16*b*G)/a,(15*v*v/b*F+16*v*G)/a])
   sol=solve_ivp(rhs,(1.,0.),state,method='DOP853',rtol=3e-10,atol=3e-12,max_step=.045)
   if not sol.success:raise RuntimeError(sol.message)
   return sol.y[:,-1]
  state=leg(state,conn.B,lambda u:conn.peak+conn.gap*u*u)
  ab=conn.a0+conn.dr_turn;aa=state[0]
  for j,m in enumerate((2,4)):state[1+2*j:3+2*j]=constant_transfer(aa,ab,math.sin(conn.peak),m)@state[1+2*j:3+2*j]
  state[0]=ab
  for j in range(2):
   sl=slice(1+2*j,3+2*j);norm=np.linalg.norm(state[sl]);state[sl]/=norm;gains[j]*=norm
  state=leg(state,conn.T,lambda u:conn.p0+(conn.peak-conn.p0)*(3*u*u-2*u**3))
  core=[]
  for j in range(2):
   z=self.back[j]@state[1+2*j:3+2*j];norm=np.linalg.norm(z);gains[j]*=norm;core.append(z/norm)
  res=np.array([core[0][1],core[1][1]])
  H=[float(self.terminal[j][1]/(gains[j]*core[j][0]))for j in range(2)]
  return (res,conn,core,gains,H,float(state[0]-self.a0))if details else res
 def summary(self,x):
  res,conn,core,gains,H,radial_error=self.residual(x,True);row=conn.summary();row.update(x=list(map(float,x)),residual=res.tolist(),residual_max=float(abs(res).max()),linear_radial_integration_error=radial_error,core_lines=dict(m2=core[0].tolist(),m4=core[1].tolist()),full_core_amplification=gains.tolist(),unit_core_terminal_height=H,terminal_height_at_core_A038=[.38*H[0],-.38/(10*math.sqrt(2))*H[1]],prefix_height=self.prefix_height,total_background_height=self.prefix_height+row['background_height'])
  return row
 def run(self,seeds=12,out=None):
  gapmax=math.pi/2+(-math.atan2(1.,self.cut['backgroundSlope']));lo=np.array([2.6,.03*gapmax]);hi=np.array([14.,.94*gapmax]);rng=np.random.default_rng(20261110);rows=[];attempts=[];start=time.time();report=dict(scope=__doc__,cut=self.cut,V=self.V,S=self.S,k0=self.k0,rows=rows,attempts=attempts)
  for i in range(seeds):
   x=lo+(hi-lo)*rng.uniform(.02,.98,2)
   try:
    z=least_squares(self.residual,x,bounds=(lo,hi),xtol=3e-10,ftol=3e-10,gtol=3e-10,max_nfev=90);r=self.summary(z.x);attempts.append(dict(seed=i,x=r['x'],residual=r['residual'],height=r['total_background_height'],H=r['terminal_height_at_core_A038']))
    if r['residual_max']<2e-6 and not any(np.linalg.norm(np.array(rr['x'])-z.x)<1e-4 for rr in rows):rows.append(r);rows.sort(key=lambda rr:rr['total_background_height'])
    print(json.dumps(dict(event='seed',i=i,residual=r['residual_max'],height=r['total_background_height'],H=r['terminal_height_at_core_A038'])),flush=True)
   except Exception as e:attempts.append(dict(seed=i,error=repr(e)));print(json.dumps(dict(event='failure',i=i,error=repr(e))),flush=True)
   report['seconds']=time.time()-start
   if out:out.write_text(json.dumps(report,indent=2)+'\n')
  return report

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--V',type=float,default=.35);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--seeds',type=int,default=12);p.add_argument('--out',type=Path,required=True);args=p.parse_args();report=Search(json.loads(args.port.read_text()),args.V,args.S,args.k0).run(args.seeds,args.out);report.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),port_sha256=hashlib.sha256(args.port.read_bytes()).hexdigest());args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',seconds=report['seconds'],candidates=len(report['rows']),best=report['rows'][:2])))
if __name__=='__main__':main()
