"""Load a complete prefix with the correct flat/cosine physical metric.
Returned source mesh includes all flat polynomial and angular-chart knots.
The saved interpolant is evaluated at additional knots; the physical metric
and checkpoint coefficients are unchanged. This is not an existence proof.
"""
import importlib.util,json,math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
HERE=Path(__file__).resolve().parent

def module(name,file):
 spec=importlib.util.spec_from_file_location(name,file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def source(checkpoint,port_path,source_root):
 adaptive=module('db6f_geometry_adaptive',HERE/'950f-prefix-adaptive-chart-bvp-v2.py')
 patch=module('db6f_geometry_flat_patch',HERE/'db6f-prefix-flat-profile.py')
 patch.install(adaptive);adaptive.old.install_source(source_root)
 from curve_stable_prefix_bvp import load_checkpoint
 rec=load_checkpoint(checkpoint);port=json.loads(Path(port_path).read_text())
 _,BVP=adaptive.build_classes(rec['chart']);M=rec['config']['modes'];q=rec['gauge_amplitude']
 obj=BVP(rec['frozen_profile'],port,q,M,max(256,32*M),True,rec['warp_reference_q'])
 par=np.asarray(rec['parameters'],float).copy();par[0]=math.log(rec['actual_primary_amplitude']/q)
 flow=obj.flow(par[0]);obj.initial(par)
 oldmesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),oldmesh,extrapolate=True,axis=1)
 # Merge the knots themselves before removing nearby old mesh nodes.
 # Physics is unchanged: this chooses only interpolation/sample nodes.
 # Interval metric readers must still split at true profile/chart formulas.
 tolerance=2e-11
 groups=[np.asarray(flow.breaks),np.asarray(rec['chart']['knots'])*flow.end,
         np.array([.75*flow.end])]
 anchors=[];discarded=[]
 for group in groups:  # Physical profile breaks have priority.
  for b in np.sort(group):
   if b<0 or b>flow.end:continue
   if any(abs(float(b)-v)<=tolerance for v in anchors):discarded.append(float(b))
   else:anchors.append(float(b))
 knots=np.sort(np.asarray(anchors))
 remaining=[]
 for b in np.sort(oldmesh):
  if any(abs(float(b)-v)<=tolerance for v in anchors):continue
  if remaining and float(b)-remaining[-1]<=tolerance:continue
  remaining.append(float(b))
 mesh=np.sort(np.r_[remaining,knots])
 if float(np.min(np.diff(mesh)))<=tolerance:
  raise ValueError('Canonical source mesh retained a near-duplicate')
 detail=dict(merge_tolerance=tolerance,profile_break_priority=True,
             discarded_nearby_knots=discarded,minimum_span=float(np.min(np.diff(mesh))))
 sol=SimpleNamespace(x=mesh,y=pp(mesh),p=par,sol=pp,mesh_details=detail)
 return rec,obj,flow,sol
