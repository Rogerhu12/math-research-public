#!/usr/bin/env python3
"""Three-mode physical design with a cylindrical hold at maximum radius.

The hold preserves both physical two-jets. All DN entries are those of the
unaltered actual tail. Only a finite linear design is computed here.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'even_circle/double_resonance_linear'))
from physical_linear_design import PhysicalDesign,FlatLoop,geometry

class CylinderLoop(FlatLoop):
 def __init__(self,design,parameters):
  super().__init__(design,parameters)
  if self.cycles!=1:raise ValueError('One exact physical loop only')
  self.hold=float(parameters['middle_cylinder'])
  if self.hold<0:raise ValueError('Positive cylinder length required')
  b=self.prefix_breaks
  self.prefix_breaks=np.unique(np.r_[b[b<=self.Tu],self.Tu+self.hold,b[b>self.Tu]+self.hold])
  self.prefix_end+=self.hold;self.end+=self.hold
  self.breaks=np.unique(np.r_[self.prefix_breaks,self.prefix_end+self.bridge.breakpoints])
 def prefix_profile(self,s):
  s=np.asarray(s);hold=(s>=self.Tu)&(s<=self.Tu+self.hold)
  shifted=np.where(s>self.Tu+self.hold,s-self.hold,s)
  a,v,k=super().prefix_profile(shifted)
  return np.where(hold,1+self.delta,a),np.where(hold,0.,v),np.where(hold,0.,k)
class CylinderDesign(PhysicalDesign):
 def profile(self,parameters):return CylinderLoop(self,parameters)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--vu',type=float,default=.4);p.add_argument('--max-nfev',type=int,default=70);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 d=CylinderDesign(a.source_root,a.port);common=dict(direction='outward',vu=a.vu,ramp=.45,ramp_eta=.05,cycles=1,prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2));record=dict(scope=__doc__,argv=sys.argv,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependencies=d.provenance,rows=[]);started=time.monotonic()
 for seed in ((.0284,.26447,.025),(.0284,.26447,.12),(.02,.18,.25),(.04,.5,.07)):
  trace=[]
  def residual(x):
   cfg=dict(common,delta=float(x[0]),vd=float(x[1]),middle_cylinder=float(x[2]));z=d.linear(cfg,3,rtol=2e-11);rr=z['core'][:,1];trace.append(dict(parameters=list(map(float,x)),tau=rr.tolist()));return rr
  sol=least_squares(residual,seed,bounds=([.003,.055,0.],[.15,.92,.5]),x_scale=[.03,.3,.1],diff_step=2e-5,ftol=1e-10,xtol=1e-10,gtol=1e-10,max_nfev=a.max_nfev)
  cfg=dict(common,delta=float(sol.x[0]),vd=float(sol.x[1]),middle_cylinder=float(sol.x[2]));lin=d.linear(cfg,12,rtol=2e-12);entry=dict(seed=seed,profile=cfg,optimizer_success=bool(sol.success),optimizer_message=sol.message,nfev=sol.nfev,tau=lin['core'][:,1].tolist(),H_per_unit_core_support=lin['H_per_unit_core_support'].tolist(),linear_three_root=bool(np.max(np.abs(lin['core'][:3,1]))<1e-7),geometry=geometry(d.profile(cfg),halfwidth=.147,cylinder_length=.54),trace=trace)
  record['rows'].append(entry);record['seconds']=time.monotonic()-started;(a.out/'summary.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in entry.items()if k!='trace'}),flush=True)
if __name__=='__main__':main()
