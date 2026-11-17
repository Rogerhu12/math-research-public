#!/usr/bin/env python3
"""Finite n4 three-mode resonance using actual C3 meridian shape controls.

Only the physical prefix changes. Tail DN, linear equations, and all boundary
frequencies remain literal. No nonlinear or circular-core solution is claimed.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'even_circle/double_resonance_linear'))
from physical_linear_design import PhysicalDesign,FlatLoop,geometry
class ShapeLoop(FlatLoop):
 def __init__(self,design,parameters):
  super().__init__(design,parameters)
  if self.cycles!=1:raise ValueError('One exact loop')
  self.controls=np.array(parameters['shape_controls'],float);self.intervals=np.array(parameters.get('shape_intervals',[[0.,.4],[.3,.7],[.6,1.]]),float)
  self.prefix_breaks=np.unique(np.r_[self.prefix_breaks,self.intervals.ravel()*self.prefix_end]);self.breaks=np.unique(np.r_[self.prefix_breaks,self.prefix_end+self.bridge.breakpoints])
 def prefix_profile(self,s):
  s=np.asarray(s);a,v,k=super().prefix_profile(s)
  for control,(l,h)in zip(self.controls,self.intervals):
   scale=(h-l)*self.prefix_end;u=(s-l*self.prefix_end)/scale;inside=(u>0)&(u<1);u=np.clip(u,0.,1.)
   b=256*u**4*(1-u)**4;d=256*(4*u**3-20*u**4+36*u**5-28*u**6+8*u**7);dd=256*(12*u**2-80*u**3+180*u**4-168*u**5+56*u**6)
   a=a+control*np.where(inside,b,0.);v=v+control*np.where(inside,d/scale,0.);k=k+control*np.where(inside,dd/scale**2,0.)
  return a,v,k
class ShapeDesign(PhysicalDesign):
 def profile(self,parameters):return ShapeLoop(self,parameters)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--max-nfev',type=int,default=100);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 d=ShapeDesign(a.source_root,a.port);common=dict(direction='outward',vu=.4,ramp=.45,ramp_eta=.05,cycles=1,prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2));record=dict(scope=__doc__,argv=sys.argv,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies=d.provenance,rows=[]);started=time.monotonic()
 for seed in ((.02840070836443855,.2644695137018561,0,0,0),(.032,.3,.001,-.001,.001),(.025,.22,-.001,.002,-.001)):
  trace=[]
  def residual(x):
   cfg=dict(common,delta=float(x[0]),vd=float(x[1]),shape_controls=list(map(float,x[2:])))
   try:rr=d.linear(cfg,3,rtol=2e-11)['core'][:,1]
   except (ValueError,FloatingPointError):rr=np.ones(3)*10
   trace.append(dict(parameters=list(map(float,x)),tau=rr.tolist()));return rr
  sol=least_squares(residual,seed,bounds=([.018,.14,-.006,-.006,-.006],[.06,.6,.006,.006,.006]),x_scale=[.03,.3,.001,.001,.001],diff_step=2e-5,ftol=1e-10,xtol=1e-10,gtol=1e-10,max_nfev=a.max_nfev)
  cfg=dict(common,delta=float(sol.x[0]),vd=float(sol.x[1]),shape_controls=list(map(float,sol.x[2:])));lin=d.linear(cfg,12,rtol=2e-12);g=geometry(d.profile(cfg),halfwidth=.147,cylinder_length=.54);g={k:g[k]for k in ('background_height','sample_ball_D_with_nominal_tail','background_curvature_sample','minimum_root','radius_max','length')};g['scope']='Modified physical background only; first positive-curvature boundary and characteristic consumption have not been recomputed.'
  entry=dict(seed=seed,profile=cfg,optimizer_success=bool(sol.success),optimizer_message=sol.message,nfev=sol.nfev,tau=lin['core'][:,1].tolist(),H_per_unit_core_support=lin['H_per_unit_core_support'].tolist(),linear_three_root=bool(np.max(np.abs(lin['core'][:3,1]))<1e-7),geometry=g,trace=trace)
  record['rows'].append(entry);record['seconds']=time.monotonic()-started;(a.out/'summary.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in entry.items()if k!='trace'}),flush=True)
if __name__=='__main__':main()
