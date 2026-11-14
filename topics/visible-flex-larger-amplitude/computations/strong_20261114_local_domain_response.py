#!/usr/bin/env python3
"""Read actual-response effects on the descending segment's Frenet gap.

Every one of the 32 numerical/core modes and all 1280 production angles are
retained. This uses the same complete initial response fields, physical cubic
interpolation, profile reconstruction, and exact inlet repair as the existing
warm screen. It computes q_lat=a*kappa_lat and q_lat-|a'| algebraically, without
any square root of the Frenet margin. No height integration, LP, tail solve,
BVP Jacobian, mode filtering, or acceptance test is performed. Values and
central response slopes are diagnostic and design information only.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,io,json,math,sys,time
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline
import strong_20261114_compact_control_screen as shared


def write(path,value):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')

def main():
 parser=argparse.ArgumentParser(add_help=False)
 parser.add_argument('--domain-response',type=Path,required=True)
 parser.add_argument('--domain-plan',type=Path,required=True)
 parser.add_argument('--domain-out',type=Path,required=True)
 own,remaining=parser.parse_known_args()
 response=shared.read(own.domain_response);plan=shared.read(own.domain_plan)
 names=list(plan['physical_steps']);rows=shared.response_directions(response,names)
 import strong_actual_warm_screen as warm
 import strong_20261114_loop_actual_bvp as entry
 original,old_argv=warm.inspect_warm,sys.argv
 done=False
 def probe(obj,x,y,p,baseline_H,**unused):
  nonlocal done
  started=time.monotonic();cfg0=dict(obj.cfg);port0,bridge0=obj.port,obj.bridge;core0=obj.actual_coefficients(p)
  if core0.tolist()!=response['baseline']['core'] or cfg0!=response['baseline']['profile'] or obj.q!=response['baseline']['gauge']:
   raise ValueError('Local domain response baseline differs from the accepted response')
  reference_s=np.unique(np.r_[np.linspace(1.45,2.10,29),1.59451763,1.7841598,1.90875633,2.00883399])
  grid=obj.inverse_chart(reference_s,0.)
  def state(steps):
   cfg=dict(cfg0);yy=y.copy();pp=p.copy();core=core0.copy()
   for name,weight in steps.items():
    row=rows[name]['row'];direction=rows[name]['vector'];yy+=weight*direction[:y.size].reshape(y.shape,order='F');pp[:obj.M]+=weight*direction[y.size:]
    core+=weight*np.asarray(row['core_derivative'])
    for field,value in row['physical_profile_derivative'].items():
     if field in shared.PRIMARY:pp[obj.M+shared.PRIMARY.index(field)]+=weight*value
     else:cfg[field]=cfg.get(field,0.)+weight*value
   obj.cfg=cfg;obj.port,obj.bridge=shared.rebuild(cfg,port0,bridge0)
   obj._flow=obj._flow_key=obj._core_key=obj._initial=None;obj._augmented_initial_geometry_key=None
   pp[0]=math.log(core[0]/obj.q);pp[1]=(core[1]-obj.ref_coeff[1])/obj.pscale[0];pp[2]=core[2]/obj.pscale[1]
   obj.select(pp);flow=obj.flow();sn,_=obj.chart(x,0.)
   correction=obj.initial(pp)-yy[:,0];yy+=correction[:,None]*np.maximum(0.,1-sn/(flow.Tu/2))[None,:]**3
   return yy,pp
  def evaluate(yy,pp):
   obj.select(pp);flow=obj.flow();sn,_=obj.chart(x,0.);s,_=obj.chart(grid,0.)
   if flow.nt!=1280:raise ValueError('Retain the actual production angular grid')
   spline=CubicSpline(sn,yy,axis=1);Y=spline(s);geo=flow.geo(s,1280);radius,ap,app=flow.profile(s)
   d=flow.values(obj.q*Y,flow.B1)+geo['p1'];dd=flow.values(obj.q*Y,flow.B2)+geo['p2']
   lam=np.linalg.norm(d,axis=2);T=d/lam[:,:,None];nv=dd-(dd*T).sum(axis=2)[:,:,None]*T
   qlat=radius[:,None]*np.linalg.norm(nv,axis=2)/lam**2;gap=qlat-np.abs(ap)[:,None];margin=1-(ap[:,None]/qlat)**2
   if not all(np.isfinite(v).all() for v in (qlat,gap,margin)):raise ValueError('Nonfinite algebraic local-domain diagnostic')
   i,j=np.unravel_index(np.argmin(gap),gap.shape)
   return gap,dict(min_gap=float(gap[i,j]),min_margin=float(margin.min()),witness=dict(row=int(i),angle_index=int(j),physical_s=float(s[i]),reference_s=float(reference_s[i]),material_tau=float(grid[i]),psi=float(2*np.pi*j/1280),radius=float(radius[i]),ap=float(ap[i]),q_lat=float(qlat[i,j])),physical_s=s.tolist(),ap=ap.tolist(),q_lat_min_by_radius=qlat.min(axis=1).tolist(),gap_min_by_radius=gap.min(axis=1).tolist(),all_modes=obj.M,angular=1280,physical_profile=dict(flow.cfg))
  base,bs=evaluate(*state({}));shape=base.shape;derivatives=np.empty((*shape,len(names)));checks=[]
  for col,name in enumerate(names):
   width=shared.CONTROL[name][0];plus,ps=evaluate(*state({name:width}));minus,ms=evaluate(*state({name:-width}));derivatives[:,:,col]=(plus-minus)/(2*width)
   checks.append(dict(name=name,width=width,central_derivative_min=float(derivatives[:,:,col].min()),central_derivative_max=float(derivatives[:,:,col].max()),second_difference_max=float(abs(plus+minus-2*base).max()),plus=ps,minus=ms))
   print(json.dumps(dict(event='local_domain_direction',name=name,seconds=time.monotonic()-started)),flush=True)
  candidates=[]
  for factor in (1.,.5):
   weights=np.array([factor*plan['physical_steps'][name] for name in names]);steps=dict(zip(names,weights));values,summary=evaluate(*state(steps));predicted=base+derivatives@weights
   i,j=np.unravel_index(np.argmin(predicted),shape);wi,wj=summary['witness']['row'],summary['witness']['angle_index']
   summary.update(factor=factor,physical_steps=steps,linear_predicted_min_gap=float(predicted[i,j]),linear_gap_error_max=float(abs(values-predicted).max()),directional_contributions_at_actual_minimum={name:float(derivatives[wi,wj,k]*weights[k]) for k,name in enumerate(names)},baseline_at_actual_minimum=float(base[wi,wj]),algebraic_linear_gap_at_actual_minimum=float(predicted[wi,wj]),nonlinear_solution=False)
   candidates.append(summary)
  state({})
  array=own.domain_out.with_name(own.domain_out.stem+'-point-responses.npz')
  np.savez_compressed(array,reference_s=reference_s,material_tau=grid,baseline_gap=base,derivative_gap=derivatives,controls=np.asarray(names))
  if array.stat().st_size>1_000_000:
   target=array.with_suffix(array.suffix+'.gz');target.write_bytes(gzip.compress(array.read_bytes(),mtime=0));array.unlink();array=target
  out=dict(scope=__doc__,finished=True,source_sha256=shared.sha(__file__),response=dict(file=str(own.domain_response),sha256=shared.sha(own.domain_response)),plan=dict(file=str(own.domain_plan),sha256=shared.sha(own.domain_plan)),controls=names,baseline=bs,central_direction_checks=checks,candidates=candidates,point_response_array=dict(file=str(array),sha256=shared.sha(array),bytes=array.stat().st_size,shape=list(derivatives.shape)),original_all_modes_and_full_angular_preserved=True,original_equations_unchanged=True,new_nonlinear_solution=False,seconds=time.monotonic()-started)
  write(own.domain_out,out);done=True
  print(json.dumps(dict(event='local_domain_complete',out=str(own.domain_out),seconds=out['seconds'],baseline_min_gap=bs['min_gap'],candidate_min_gaps=[v['min_gap'] for v in candidates])),flush=True)
  return dict(finite_domain_passed=all(v['min_gap']>0 for v in candidates),local_domain_diagnostic=str(own.domain_out),nonlinear_solution=False)
 warm.inspect_warm=probe;sys.argv=[old_argv[0],*remaining]
 try:entry.main()
 finally:warm.inspect_warm,sys.argv=original,old_argv
 if not done:raise RuntimeError('Local-domain response diagnostic did not complete')

if __name__=='__main__':main()
