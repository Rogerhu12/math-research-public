#!/usr/bin/env python3
"""Read recorded failed Newton blocks without changing or accepting a field.

Reconstruct the same current-anchor physical Flow and algebraically evaluate
its original latitude curvature and Frenet discriminant on the failed state.
Low-pass variants are diagnostic only; no BVP, Jacobian or tail is solved.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np

def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--computations',type=Path,required=True);p.add_argument('--source-topic',type=Path,required=True)
 p.add_argument('--accepted',type=Path,required=True);p.add_argument('--port',type=Path,required=True)
 p.add_argument('--block',type=Path,nargs='+',required=True);p.add_argument('--out',type=Path,required=True)
 a=p.parse_args();sys.path.insert(0,str(a.computations.resolve()))
 pull=load('strong_failed_block_pullback',a.computations/'geometric-checkpoint-core-pullback.py')
 original=pull.module
 def module(name,path):
  value=original(name,path)
  if Path(path).name=='alternative-neck-provider.py':
   import strong_initial_speed_pulse as pulse
   import strong_monotone_initial_speed_anchor as frontload
   pulse.install(value);frontload.install(value)
  return value
 pull.module=module
 saved,_=pull.load_saved(a.accepted,a.source_topic,a.port,angular=1280)
 provider=sys.modules['geometric_pullback_neck_provider'];port=json.loads(a.port.read_text())
 rows=[]
 for path in a.block:
  z=np.load(path,allow_pickle=False);meta=json.loads(z['metadata'].tobytes());ident=meta['identity'];cfg=ident['actually_constructed_Flow_cfg']
  f=type(saved.flow)(cfg,provider.tagged_port(port,cfg),saved.M,saved.q,ident['nt'],saved.mode,warp_q=0.)
  pull.charts.attach_to_adaptive_flow(f,ident['ref_coeff'],ident['ref_frequencies'],reference='core-blend',transition_start=saved.rec.get('chart_transition_start',0.),transition_end=saved.rec.get('chart_transition_end',1.))
  s=z['s'];Y=np.asarray(z['y'],np.longdouble);geo=f.geo(s,f.B1.shape[1]);radius,ap,app=f.profile(s)
  def evaluate(Y):
   d=f.values(f.q*Y,f.B1)+geo['p1'];dd=f.values(f.q*Y,f.B2)+geo['p2'];lam=np.sqrt(np.sum(d*d,axis=2));T=d/lam[:,:,None]
   normal_second=dd-np.sum(dd*T,axis=2)[:,:,None]*T
   kappa=np.sqrt(np.sum(normal_second*normal_second,axis=2))/lam**2
   qlat=radius[:,None]*kappa;margin=1-(ap[:,None]/qlat)**2
   i,j=np.unravel_index(np.argmin(margin),margin.shape)
   return dict(min_margin=float(margin[i,j]),physical_s=float(s[i]),psi=float(2*np.pi*j/margin.shape[1]),angular_index=int(j),radial_index=int(i),radius=float(radius[i]),ap=float(ap[i]),a_kappa_lat=float(qlat[i,j]),q_minus_abs_ap=float(qlat[i,j]-abs(ap[i])),minimum_a_kappa_lat=float(qlat.min()),minimum_q_minus_abs_ap=float((qlat-abs(ap[:,None])).min()),minimum_lambda=float(lam.min()))
  full=evaluate(Y);variants=[]
  for keep in (2,4,8,12,16,24):
   yy=Y.copy()
   for start in (1,1+f.M,1+2*f.M):yy[start+keep:start+f.M]=0
   v=evaluate(yy);v['kept_numerical_harmonics']=keep;v['physical_field_modified_for_diagnostic_only']=True;variants.append(v)
  expected=float(meta['exception_repr'].split('failure: ')[1].split("'")[0])
  row=dict(file=path.name,sha256=sha(path),physical_profile=cfg,original_reported_min_margin=expected,reconstructed=full,margin_reconstruction_absolute_difference=abs(full['min_margin']-expected),diagnostic_lowpass_variants=variants)
  if row['margin_reconstruction_absolute_difference']>2e-12:raise ValueError('Failed block does not reconstruct its original domain decision')
  rows.append(row)
 out=dict(scope=__doc__,source_sha256=sha(__file__),accepted_sha256=sha(a.accepted),records=rows,all_original_domain_decisions_reproduced=True,original_solver_or_field_modified=False,new_nonlinear_solution=False,lowpass_is_not_a_proposed_solution=True)
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(out=str(a.out),blocks=len(rows),max_reconstruction_difference=max(r['margin_reconstruction_absolute_difference'] for r in rows))),flush=True)

if __name__=='__main__':main()
