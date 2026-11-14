#!/usr/bin/env python3
"""C2 radial metrics with a nonzero initial outward acceleration.

FastStartCycle is a one-cycle provider that can be installed on
PlanarSymmetryFlow, leaving the original terminal bridge intact.
FastOutwardLeg is a simpler nonnegative-acceleration IVP design family;
it reaches a constant-slope developable leg without an acceleration jump.
No nonlinear closed-surface existence is asserted by defining a profile.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json
from pathlib import Path
import numpy as np

class FastStartCycle:
 def __init__(self,cfg):
  if int(cfg.get('cycles',1))!=1:raise ValueError('fast_start currently defines exactly one C2 cycle')
  self.delta=float(cfg['delta']);self.k0=float(cfg.get('start_acceleration',1.5))
  self.Tu=float(cfg.get('up_time',self.delta/(float(cfg['vu'])*(1-float(cfg['ramp'])))))
  self.Td=float(cfg.get('down_time',15*self.delta/(8*float(cfg['vd']))))
  if min(self.delta,self.Tu,self.Td)<=0 or self.k0<0:raise ValueError('Invalid fast_start parameters')
  self.A=self.k0*self.Tu;self.B=30*self.delta/self.Tu-2.5*self.A
  if self.A+self.B<0:raise ValueError('The outward speed changes sign')
  self.end=self.Tu+self.Td
  roots=np.roots([4*self.B,3*(self.A-2*self.B),2*(self.B-2*self.A),self.A])
  critical=[float(z.real) for z in roots if abs(z.imag)<1e-10 and 0<z.real<1]
  self.knots=np.unique(np.r_[0.,self.Tu*np.asarray(critical),self.Tu,self.Tu+self.Td*.5,self.end])
  v=[float(self.profile(x)[1])for x in self.knots]
  self.maximum_speed=max(abs(x)for x in v)
  if self.maximum_speed>=1:raise ValueError(f'Profile leaves |a prime|<1: {self.maximum_speed}')
 def profile(self,s):
  scalar=np.ndim(s)==0;s=np.asarray(s,dtype=float);up=s<=self.Tu
  u=np.clip(s/self.Tu,0.,1.);A=self.A;B=self.B
  aa=1+self.Tu*(A*u*u/2+(B-2*A)*u**3/3+(A-2*B)*u**4/4+B*u**5/5)
  vv=u*(1-u)**2*(A+B*u)
  acc=(A+2*(B-2*A)*u+3*(A-2*B)*u*u+4*B*u**3)/self.Tu
  x=np.clip((s-self.Tu)/self.Td,0.,1.)
  a2=1+self.delta-self.delta*(10*x**3-15*x**4+6*x**5)
  v2=-30*self.delta/self.Td*x*x*(1-x)**2
  q2=-60*self.delta/self.Td**2*x*(1-x)*(1-2*x)
  result=tuple(np.where(up,z,w)for z,w in zip((aa,vv,acc),(a2,v2,q2)))
  return tuple(float(z)for z in result) if scalar else result

class FastOutwardLeg:
 def __init__(self,velocity=.5,length=2/3,power=1):
  self.velocity=float(velocity);self.length=float(length);self.power=int(power)
  if not 0<self.velocity<1 or self.length<=0 or self.power<1:raise ValueError('Invalid fast outward parameters')
  self.k0=self.velocity*(self.power+1)/self.length
  self.a_end=1+self.velocity*self.length*(self.power+1)/(self.power+2)
 def profile(self,s):
  scalar=np.ndim(s)==0;s=np.asarray(s,dtype=float);u=np.clip(s/self.length,0.,1.);p=self.power
  aa=1+self.velocity*self.length*(u-(1-(1-u)**(p+2))/(p+2))
  vv=self.velocity*(1-(1-u)**(p+1));acc=self.k0*(1-u)**p
  result=(np.where(s<=self.length,aa,self.a_end+self.velocity*(s-self.length)),np.where(s<=self.length,vv,self.velocity),np.where(s<=self.length,acc,0.))
  return tuple(float(z)for z in result) if scalar else result

def install(flow_class=None):
 """Call after loading the original source/flat provider, before building BVPs."""
 if flow_class is None:
  from fixed_metric_mode3_flow import PlanarSymmetryFlow
  flow_class=PlanarSymmetryFlow
 if getattr(flow_class,'alternative_fast_profile_installed',False):return
 original_init=flow_class.__init__;original_prefix=flow_class.prefix_profile
 def flow_init(self,cfg,*args,**kwargs):
  original_init(self,cfg,*args,**kwargs)
  if cfg.get('ramp_law')=='fast_start':
   law=FastStartCycle(cfg);self._alternative_fast_profile=law
   self.Tu=law.Tu;self.Td=law.Td;self.period=law.end;self.prefix_end=law.end;self.end=law.end+self.bridge.L
   self.breakpoints=law.knots.copy();self.breaks=np.unique(np.r_[self.breakpoints,self.end])
 def prefix_profile(self,s):
  if self.cfg.get('ramp_law')=='fast_start':return self._alternative_fast_profile.profile(s)
  return original_prefix(self,s)
 flow_class.__init__=flow_init;flow_class.prefix_profile=prefix_profile;flow_class.alternative_fast_profile_installed=True

def probe_class():
 path=Path(__file__).with_name('alternative-outward-probe.py');sp=importlib.util.spec_from_file_location('alternative_fast_probe_base',path);base=importlib.util.module_from_spec(sp);sp.loader.exec_module(base)
 class FastProbe(base.Probe):
  def __init__(self,A,M,N,v,S,power):
   self.fast_law=FastOutwardLeg(v,S,power)
   super().__init__(A,M,N,v,S,max(1.8,self.fast_law.a_end+.1))
   self.s_end=S
  def profile(self,s):return self.fast_law.profile(s)
 return FastProbe

def main():
 p=argparse.ArgumentParser();p.add_argument('--A',type=float,default=.38);p.add_argument('--M',type=int,default=48);p.add_argument('--N',type=int,default=768);p.add_argument('--v',type=float,default=.5);p.add_argument('--S',type=float,default=2/3);p.add_argument('--power',type=int,default=1);p.add_argument('--rtol',type=float,default=1e-10);p.add_argument('--maxstep',type=float,default=.0004);p.add_argument('--steps',type=int,default=40);p.add_argument('--end-s',type=float);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 q=probe_class()(a.A,a.M,a.N,a.v,a.S,a.power);r=q.run(a.rtol,a.steps,a.maxstep,a.end_s)
 r['config'].update(radial_law='fast_outward',power=a.power,initial_acceleration=q.fast_law.k0)
 r['fast_profile_source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(dict(status=r['status'],config=r['config'],seconds=r['seconds'],last=r['rows'][-1])))
if __name__=='__main__':main()
