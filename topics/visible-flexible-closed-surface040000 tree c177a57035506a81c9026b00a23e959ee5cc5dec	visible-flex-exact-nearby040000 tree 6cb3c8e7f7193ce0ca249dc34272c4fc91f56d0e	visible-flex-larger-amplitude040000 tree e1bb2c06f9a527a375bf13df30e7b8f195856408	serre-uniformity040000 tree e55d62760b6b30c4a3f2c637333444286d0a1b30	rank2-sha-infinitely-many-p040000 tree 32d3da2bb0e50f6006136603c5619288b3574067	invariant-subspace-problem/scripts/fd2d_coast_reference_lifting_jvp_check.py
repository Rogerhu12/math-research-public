#!/usr/bin/env python3
"""Small actual-grid check of new reference lifting parameter/spatial jets."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import copy,json,time,resource
from pathlib import Path
import numpy as np
from fd2d_gc_raw_bump_coast_reference import CoastReferenceRawBumpDAE,coast_window
from fd2d_gc_archive_arrays import identity,load_npz

def main():
 root=Path(__file__).resolve().parent.parent;notes=root/'notes';start=time.monotonic()
 candidate=notes/'2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json'
 field=notes/'2026-11-12-fd2d-raw-bump-gauss08-b0008-accepted-0002.npz'
 inlet=notes/'2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz'
 cache=notes/'2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz'
 out=notes/'2026-11-12-fd2d-coast-reference-lifting-jvp01.json'
 if out.exists():raise FileExistsError('Use a new version for any subsequent actual check')
 saved=load_npz(field);problem=CoastReferenceRawBumpDAE(candidate,modes=int(saved['modes']),max_step=.04,profile_count=int(saved['profile_count']),supports=saved['profile_supports'],base_kind=str(saved['base_kind']),blend=tuple(saved['blend']),reference_inlet=inlet,reference_cache=cache)
 if not np.array_equal(problem.x,saved['mesh']):raise ValueError('Actual saved unknown mesh differs')
 metadata=json.loads(str(load_npz(cache)['metadata']))
 points=np.array(sorted(float.fromhex(r['s_hex']) for r in metadata['entries']))
 ref=problem.coast_reference;w,ws=coast_window(points,ref.entry_s,ref.length,.12)
 ramps=np.flatnonzero((w>.01)&(w<.99));plateau=np.flatnonzero(w==1)
 selected=np.array(sorted(set([int(ramps[0]),int(ramps[-1]),int(plateau[len(plateau)//2])])));x=points[selected]
 small=copy.copy(problem);small.x=x;small.N=len(x);small.h=np.diff(x);small.size=small.N*small.q+small.parameter_count;small._operator_cache={}
 small.coords={k:np.asarray(v,float) for k,v in small.chart.coordinates(x).items()}
 p=np.array(saved['parameters'],copy=True);b=(p[problem.tail_parameter_slice]+.6)/2;delta=p[problem.profile_parameter_slice].copy()
 base=small.lifting(delta,b);rng=np.random.default_rng(1440001);cases=[]
 for group,count in [('tail',len(b)),('profile',len(delta))]:
  direction=rng.standard_normal(count);direction/=np.linalg.norm(direction);h=1e-6
  if group=='tail':plus=small.lifting(delta,b+h*direction);minus=small.lifting(delta,b-h*direction);keys=('parameters','x_parameters','xi_parameters')
  else:plus=small.lifting(delta+h*direction,b);minus=small.lifting(delta-h*direction,b);keys=('profile_parameters','profile_s_parameters','profile_xi_parameters')
  for value,key in zip(('values','x','xi'),keys):
   exact=np.einsum('wncp,p->wnc',base[key],direction);fd=(plus[value]-minus[value])/(2*h);err=fd-exact;norm=float(np.linalg.norm(exact));rel=float(np.linalg.norm(err)/max(norm,1e-300))
   cases.append(dict(parameter_block=group,jet=value,step=h,analytic_direction_norm=norm,absolute_maximum=float(np.max(abs(err))),relative_l2=rel))
 checks=dict(six_nonzero_directions=all(r['analytic_direction_norm']>1e-9 for r in cases),all_relative_errors_small=all(r['relative_l2']<2e-6 for r in cases),no_reference_cache_misses=ref.cache_statistics()['misses']==0)
 report=dict(schema='fd2d-reference-lifting-small-actual-grid-JVP-v1',source=identity(__file__),provider=identity(root/'scripts/fd2d_gc_raw_bump_coast_reference.py'),reference_source=identity(root/'scripts/fd2d_gc_frozen_coast_reference.py'),candidate=identity(candidate),field=identity(field),reference_cache=identity(cache),radial_points=x.tolist(),weights=w[selected].tolist(),weight_first=ws[selected].tolist(),tail_test_parameters=b.tolist(),profile_parameters=delta.tolist(),directions_seed=1440001,scope='Three actual cached physical points; tail moved into the interior for centered differences; no BVP/body/whole-domain certificate',cases=cases,checks=checks,passed=bool(all(checks.values())),cache_statistics=ref.cache_statistics(),seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(passed=report['passed'],points=report['radial_points'],weights=report['weights'],maximum_relative_error=max(r['relative_l2'] for r in cases),misses=report['cache_statistics']['misses'],seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'],report=str(out))),flush=True)
 return 0 if report['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
