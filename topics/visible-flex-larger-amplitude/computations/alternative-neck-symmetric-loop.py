#!/usr/bin/env python3
"""A finite C2 symmetric high-slope radius loop and complete linear match.

The loop has two flat-top angular-speed reversals and two constant-slope
radial legs. Its exact linear transfer is evaluated, not replaced by the
instantaneous-turn seed matrix. Search also includes the preceding strong
Hermite prefix and the terminal C2 connector to the physical small cut.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('alternative_sym_flat_neck',P/'alternative-neck-flatturn.py');fl=importlib.util.module_from_spec(sp);sp.loader.exec_module(fl)
base=fl.base

class SymmetricProgram:
 def __init__(self,a0,v0,cut,x,loop_curvature=8.):
  r0,q,v,C,Kstart,gapfraction=map(float,x);self.x=list(map(float,x));self.cut=cut;self.a0=a0;self.v0=v0;self.Kloop=loop_curvature;self.loop_radius=r0;self.loop_ratio=q;self.loop_speed=v
  pp=math.asin(v);p0=math.asin(v0);pt=-math.atan2(1.,cut['backgroundSlope']);ps=-cut['backgroundSecond']/(1+cut['backgroundSlope']**2)**1.5;gap=gapfraction*(math.pi/2+pt);peak=pt-gap
  start=fl.turn(p0,-pp,Kstart);low=fl.turn(-pp,pp,loop_curvature);high=fl.turn(pp,-pp,loop_curvature);tailturn=fl.turn(-pp,peak,loop_curvature)
  brake=dict(kind='brake',p0=peak,p1=pt,length=2*gap/ps,K=ps)
  brake['dr']=brake['length']*float(fl.integral(brake,1.));brake['dh']=brake['length']*float(fl.integral(brake,1.,'cos'));brake['dr_min']=brake['dr'];brake['dr_max']=0.
  self.segments=[];a=a0;h=0.;s=0.
  def append(seg):
   nonlocal a,h,s
   seg=dict(seg);seg.update(a0=a,h0=h,s0=s,a1=a+seg['dr'],h1=h+seg['dh'],s1=s+seg['length']);a=seg['a1'];h=seg['h1'];s=seg['s1'];self.segments.append(seg)
  def coast(target,p):
   L=(target-a)/math.sin(p)
   if L< -2e-10:raise ValueError('Negative constant-angle leg')
   L=max(0.,L);append(dict(kind='coast',p0=p,p1=p,length=L,dr=target-a,dh=L*math.cos(p),dr_min=min(0.,target-a),dr_max=max(0.,target-a),K=0.))
  coast(a0+v0*C,p0);append(start);coast(r0,-pp)
  self.loop_first=len(self.segments);append(low);coast(q*r0,pp);append(high);coast(r0,-pp);self.loop_last=len(self.segments)
  append(tailturn);coast(cut['radius']-brake['dr'],peak);append(brake)
  self.end=s;self.height=h;self.end_radius=a;self.minimum_radius=min(seg['a0']+seg['dr_min']for seg in self.segments);self.maximum_radius=max(seg['a0']+seg['dr_max']for seg in self.segments)
  if self.minimum_radius<=0:raise ValueError('Nonpositive program radius')
 summary=fl.program_summary
 def loop_transfer(self,m):
  y=np.r_[self.loop_radius,np.eye(2).ravel()]
  for seg in self.segments[self.loop_first:self.loop_last]:
   if seg['kind']=='coast':
    T=base.pl.constant_transfer(seg['a0'],seg['a1'],math.sin(seg['p0']),m);y=np.r_[seg['a1'],(T@y[1:].reshape(2,2)).ravel()]
   else:
    def fun(u,y):
     phi=float(fl.phase(seg,u));v=math.sin(phi);b=math.cos(phi);mm=m*m;A=np.array([[-(mm-1)*v,-mm*b],[(mm-1)*v*v/b,mm*v]])/y[0]
     return seg['length']*np.r_[v,(A@y[1:].reshape(2,2)).ravel()]
    sol=solve_ivp(fun,(0.,1.),y,method='DOP853',rtol=1e-11,atol=1e-13,max_step=.015)
    if not sol.success:raise RuntimeError(sol.message)
    y=sol.y[:,-1]
  T=y[1:].reshape(2,2);eig=np.linalg.eigvals(T)
  return dict(matrix=T.tolist(),determinant=float(np.linalg.det(T)),trace=float(np.trace(T)),eigenvalue_real=eig.real.tolist(),eigenvalue_imag=eig.imag.tolist(),eigenvalue_abs=abs(eig).tolist(),minimum_radius=min(s['a0']+s['dr_min']for s in self.segments[self.loop_first:self.loop_last]),maximum_radius=max(s['a0']+s['dr_max']for s in self.segments[self.loop_first:self.loop_last]),height=sum(s['dh']for s in self.segments[self.loop_first:self.loop_last]))

base.Program=SymmetricProgram

class Search(fl.Search):
 def run(self,seeds,out):
  lo=np.array([.345,1.5,.95,0.,4.,.03]);hi=np.array([.5,2.8,.995,.32,8.,.32]);rng=np.random.default_rng(20261110);rows=[];attempts=[];begin=time.time();report=dict(scope=__doc__,V=self.V,S=self.S,k0=self.k0,cut=self.cut,turn_ramp=.08,rows=rows,attempts=attempts)
  seeds_x=[np.array([.35,2.2,.985,.1,4.5,.1])]+[lo+(hi-lo)*rng.uniform(.04,.96,6)for _ in range(max(0,seeds-1))]
  for index,x in enumerate(seeds_x):
   try:
    z=least_squares(self.residual,x,bounds=(lo,hi),xtol=5e-9,ftol=5e-9,gtol=5e-9,max_nfev=140);r=self.summary(z.x);attempts.append(dict(seed=index,x=r['x'],resonance=r['resonance_max'],residual=r['core_resonance'],height=r['total_background_height'],H=r['terminal_height_at_core_A038'],D=r['connector_background_centered_D_sample']))
    if r['resonance_max']<2e-5 and abs(r['terminal_height_at_core_A038'][0])<6e-4 and not any(np.linalg.norm(np.array(row['x'])-z.x)<1e-4 for row in rows):
     program=SymmetricProgram(self.a0,self.V,self.cut,z.x);r['loop_transfer']={str(m):program.loop_transfer(m)for m in (2,4)};rows.append(r);rows.sort(key=lambda rr:rr['total_background_height'])
    print(json.dumps(dict(event='seed',index=index,resonance=r['resonance_max'],height=r['total_background_height'],H=r['terminal_height_at_core_A038'],D=r['connector_background_centered_D_sample'])),flush=True)
   except Exception as e:attempts.append(dict(seed=index,error=repr(e)));print(json.dumps(dict(event='error',index=index,error=repr(e))),flush=True)
   report['seconds']=time.time()-begin;out.write_text(json.dumps(report,indent=2)+'\n')
  return report

def main():
 p=argparse.ArgumentParser();p.add_argument('--port',type=Path,required=True);p.add_argument('--V',type=float,default=.25);p.add_argument('--S',type=float,default=.65);p.add_argument('--k0',type=float,default=.45);p.add_argument('--seeds',type=int,default=6);p.add_argument('--seed-only',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args();search=Search(json.loads(a.port.read_text()),a.V,a.S,a.k0)
 if a.seed_only:
  x=[.35,2.2,.985,.1,4.5,.1];report=search.summary(x);program=SymmetricProgram(search.a0,search.V,search.cut,x);report['loop_transfer']={str(m):program.loop_transfer(m)for m in (2,4)};report['scope']=__doc__;print(json.dumps(report))
 else:report=search.run(a.seeds,a.out);print(json.dumps(dict(event='complete',seconds=report['seconds'],candidates=len(report['rows']),best=report['rows'][:1])))
 report.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),base_source_sha256=hashlib.sha256((P/'alternative-neck-flatturn.py').read_bytes()).hexdigest(),port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest());a.out.write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
