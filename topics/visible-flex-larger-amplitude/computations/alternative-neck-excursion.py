#!/usr/bin/env python3
"""C2 neck excursion screened for linear resonance, attenuation, and height.

The design starts at a fixed Hermite prefix, descends to a small neck,
turns outward once, expands, then turns inward to the physical tail cut.
Every constant-angle/turn seam has continuous a,a',a''. The complete search
is linear; nonlinear domain, metric, reach and closed-family existence are
not certified by a root or a small terminal-height coefficient.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares,minimize
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_neck_plateau',P/'alternative-angle-plateau-connector.py');pl=importlib.util.module_from_spec(sp);sp.loader.exec_module(pl)
gx,gw=np.polynomial.legendre.leggauss(64);gu=(gx+1)/2

def phase(seg,u):
 if seg['kind']=='turn':return seg['p0']+(seg['p1']-seg['p0'])*(3*u*u-2*u**3)
 if seg['kind']=='brake':return seg['p0']+(seg['p1']-seg['p0'])*u*u
 return np.zeros_like(u)+seg['p0']

def turn(p0,p1,K):
 L=1.5*abs(p1-p0)/K;d=dict(kind='turn',p0=p0,p1=p1,length=L,K=K)
 d['dr']=L/2*float(np.dot(np.sin(phase(d,gu)),gw));d['dh']=L/2*float(np.dot(np.cos(phase(d,gu)),gw))
 u=np.linspace(0,1,201);uq=u[:,None]*gu[None,:];r=L*u/2*(np.sin(phase(d,uq))@gw)
 d['dr_min']=float(r.min());d['dr_max']=float(r.max());return d

class Program:
 def __init__(self,a0,v0,cut,x,loop_curvature=8.):
  rmin,down,up,extra,gapfraction,Kstart=map(float,x);self.x=list(map(float,x));self.cut=cut;self.a0=a0;self.v0=v0;self.Kloop=loop_curvature
  p0=math.asin(v0);pd=-math.asin(down);pu=math.asin(up);pt=-math.atan2(1.,cut['backgroundSlope']);ps=-cut['backgroundSecond']/(1+cut['backgroundSlope']**2)**1.5
  gap=gapfraction*(math.pi/2+pt);peak=pt-gap
  start=turn(p0,pd,Kstart);low=turn(pd,pu,loop_curvature);high=turn(pu,peak,loop_curvature)
  brake=dict(kind='brake',p0=peak,p1=pt,length=2*gap/ps,K=ps)
  brake['dr']=brake['length']/2*float(np.dot(np.sin(phase(brake,gu)),gw));brake['dh']=brake['length']/2*float(np.dot(np.cos(phase(brake,gu)),gw));brake['dr_min']=brake['dr'];brake['dr_max']=0.
  lower_start=rmin-low['dr_min'];before_brake=cut['radius']-brake['dr'];upper_start=before_brake-high['dr']+extra
  self.segments=[];a=a0;h=0.;s=0.
  def append(seg):
   nonlocal a,h,s
   seg=dict(seg);seg.update(a0=a,h0=h,s0=s,a1=a+seg['dr'],h1=h+seg['dh'],s1=s+seg['length']);a=seg['a1'];h=seg['h1'];s=seg['s1'];self.segments.append(seg)
  def coast(target,p):
   L=(target-a)/math.sin(p)
   if L< -1e-10:raise ValueError('Negative constant-angle leg')
   L=max(0.,L);append(dict(kind='coast',p0=p,p1=p,length=L,dr=target-a,dh=L*math.cos(p),dr_min=min(0.,target-a),dr_max=max(0.,target-a),K=0.))
  append(start);coast(lower_start,pd);append(low);coast(upper_start,pu);append(high);coast(before_brake,peak);append(brake)
  self.end=s;self.height=h;self.end_radius=a;self.minimum_radius=min(seg['a0']+seg['dr_min']for seg in self.segments);self.maximum_radius=max(seg['a0']+seg['dr_max']for seg in self.segments)
  if self.minimum_radius<=0:raise ValueError('Nonpositive program radius')
 def summary(self):
  kmax=0.;rmax=0.;pmin=1.
  for seg in self.segments:
   u=np.linspace(0,1,151);uQ=u[:,None]*gu[None,:];a=seg['a0']+seg['length']*u/2*(np.sin(phase(seg,uQ))@gw);pp=phase(seg,u)
   if seg['kind']=='turn':dp=(seg['p1']-seg['p0'])*6*u*(1-u)/seg['length']
   elif seg['kind']=='brake':dp=2*(seg['p1']-seg['p0'])*u/seg['length']
   else:dp=np.zeros_like(u)
   h=seg['h0']+seg['length']*u/2*(np.cos(phase(seg,uQ))@gw)
   kmax=max(kmax,float(np.max(np.maximum(abs(dp),np.cos(pp)/a))));rmax=max(rmax,float(np.sqrt(a*a+h*h).max()));pmin=min(pmin,float(np.cos(pp).min()))
  return dict(x=self.x,segments=self.segments,connector_length=self.end,connector_height=self.height,connector_minimum_radius=self.minimum_radius,connector_maximum_radius=self.maximum_radius,connector_background_kappa_sample=kmax,minimum_background_vertical_speed=pmin,terminal_radius=self.end_radius)

class Search(pl.direct.Search):
 def residual(self,x,details=False):
  program=Program(self.a0,self.V,self.cut,x);state=np.r_[self.cut['radius'],self.terminal[0],self.terminal[1]];gains=np.ones(2)
  for seg in reversed(program.segments):
   if seg['length']<1e-14:continue
   if seg['kind']=='coast':
    for j,m in enumerate((2,4)):state[1+2*j:3+2*j]=pl.constant_transfer(seg['a1'],seg['a0'],math.sin(seg['p0']),m)@state[1+2*j:3+2*j]
    state[0]=seg['a0']
   else:
    def rhs(u,y):
     pp=float(phase(seg,u));v=math.sin(pp);b=math.cos(pp);a=y[0];f,g,F,G=y[1:]
     return seg['length']*np.array([v,(-3*v*f-4*b*g)/a,(3*v*v/b*f+4*v*g)/a,(-15*v*F-16*b*G)/a,(15*v*v/b*F+16*v*G)/a])
    sol=solve_ivp(rhs,(1.,0.),state,method='DOP853',rtol=3e-9,atol=3e-11,max_step=.045)
    if not sol.success:raise RuntimeError(sol.message)
    state=sol.y[:,-1]
   for j in range(2):
    sl=slice(1+2*j,3+2*j);norm=np.linalg.norm(state[sl]);gains[j]*=norm;state[sl]/=norm
  core=[]
  for j in range(2):
   z=self.back[j]@state[1+2*j:3+2*j];norm=np.linalg.norm(z);gains[j]*=norm;core.append(z/norm)
  H=np.array([self.terminal[j][1]/(gains[j]*core[j][0])for j in range(2)])
  resonance=np.array([core[0][1],core[1][1]])
  return (resonance,program,core,gains,H)if details else np.r_[resonance,.05*math.log10(max(abs(.38*H[0]),1e-30)/2e-4)]
 def summary(self,x):
  res,program,core,gains,H=self.residual(x,True);r=program.summary();r.update(core_resonance=res.tolist(),resonance_max=float(abs(res).max()),full_core_amplification=gains.tolist(),unit_core_terminal_height=H.tolist(),terminal_height_at_core_A038=[.38*H[0],-.38/(10*math.sqrt(2))*H[1]],prefix_height=self.prefix_height,total_background_height=self.prefix_height+program.height)
  maxnorm=0.
  for seg in program.segments:
   u=np.linspace(0,1,151);uQ=u[:,None]*gu[None,:];a=seg['a0']+seg['length']*u/2*(np.sin(phase(seg,uQ))@gw);h=self.prefix_height+seg['h0']+seg['length']*u/2*(np.cos(phase(seg,uQ))@gw);maxnorm=max(maxnorm,float(np.sqrt(a*a+h*h).max()))
  r['connector_background_centered_D_sample']=2*maxnorm;return r
 def run(self,seeds,out):
  lo=np.array([.13,.65,.3,0.,.04,4.]);hi=np.array([.3,.995,.94,.3,.93,8.]);rng=np.random.default_rng(20261110);rows=[];attempts=[];begin=time.time();report=dict(scope=__doc__,V=self.V,S=self.S,k0=self.k0,cut=self.cut,rows=rows,attempts=attempts)
  for index in range(seeds):
   x=lo+(hi-lo)*rng.uniform(.04,.96,6)
   try:
    z=least_squares(self.residual,x,bounds=(lo,hi),xtol=5e-9,ftol=5e-9,gtol=5e-9,max_nfev=130);r=self.summary(z.x);attempts.append(dict(seed=index,x=r['x'],resonance=r['resonance_max'],height=r['total_background_height'],H=r['terminal_height_at_core_A038']))
    if r['resonance_max']<2e-5 and abs(r['terminal_height_at_core_A038'][0])<3e-4 and not any(np.linalg.norm(np.array(row['x'])-z.x)<1e-4 for row in rows):rows.append(r);rows.sort(key=lambda rr:rr['total_background_height'])
    print(json.dumps(dict(event='seed',index=index,resonance=r['resonance_max'],height=r['total_background_height'],H=r['terminal_height_at_core_A038'],D=r['connector_background_centered_D_sample'])),flush=True)
   except Exception as e:attempts.append(dict(seed=index,error=repr(e)));print(json.dumps(dict(event='error',index=index,error=repr(e))),flush=True)
   report['seconds']=time.time()-begin;out.write_text(json.dumps(report,indent=2)+'\n')
  return report

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--V',type=float,default=.25);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--seeds',type=int,default=8);p.add_argument('--out',type=Path,required=True);a=p.parse_args();report=Search(json.loads(a.port.read_text()),a.V,a.S,a.k0).run(a.seeds,a.out);report.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest());a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(event='complete',seconds=report['seconds'],candidates=len(report['rows']),best=report['rows'][:1])))
if __name__=='__main__':main()
