#!/usr/bin/env python3
"""Generate the complete 1.03 preparation from one SHA-bound frozen source.
The exact edits shorten the explicit reference and cover every original
midpoint/RMS evaluator; all 482 equations and 325/157 row rules remain.
Generated source and reports stay outside the repository.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path
BASE='fe6bbefb8cc0411ab6018376b6fde6c957acbe4f57bb24c4a10ce7acecdc9104'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
 if sha(a.base_source)!=BASE:raise ValueError('The frozen complete preparation source changed')
 code=a.base_source.read_text()
 def change(old,new):
  nonlocal code
  if code.count(old)!=1:raise ValueError('Exact source edit must occur once: '+old[:80])
  code=code.replace(old,new)
 change('full M160 HoldProfile BVP to 1.04.','full M160 HoldProfile BVP to 1.03.')
 change('end=1.04;interface=', 'end=1.03;interface=')
 change('x[32],.997,1.017,1.037])','x[32],.997,1.017])')
 change('from scipy.linalg import eigvals,solve,svdvals','from scipy.linalg import eigvals,solve,svdvals\nimport scipy.integrate._bvp as backend')
 change("  if not bad_node:\n   for i,h in enumerate(np.diff(mesh)):\n    s=float((mesh[i]+mesh[i+1])/2);ym=(yy[i]+yy[i+1])/2-h*(ff[i+1]-ff[i])/8;val=values(ym,s);mid_min=np.minimum(mid_min,val)\n    if min(val)<=0:bad_cell.append(i)",
 """  groups=[]
  if not bad_node:
   hh=np.diff(mesh);middle=mesh[:-1]+.5*hh;offset=.5*hh*np.sqrt(3/7);spline=backend.create_spline(yy.T,ff.T,mesh,hh)
   for name,times in (('midpoint',middle),('RMS_left',middle-offset),('RMS_right',middle+offset)):
    group_bad=[];group_min=np.full(3,np.inf)
    for i,(s,ym)in enumerate(zip(times,spline(times).T)):
     val=values(ym,float(s));mid_min=np.minimum(mid_min,val);group_min=np.minimum(group_min,val)
     if min(val)<=0:group_bad.append(i);bad_cell.append(i)
    groups.append(dict(kind=name,QWH_lower=group_min.tolist(),invalid_cells=group_bad,invalid_count=len(group_bad)))
   bad_cell=sorted(set(bad_cell))""")
 change('invalid_collocation_cells=bad_cell,','invalid_solver_evaluation_cells=bad_cell,solver_point_groups=groups,')
 change('collocation_midpoint_QWH_lower=mid_min.tolist()','solver_evaluation_QWH_lower=mid_min.tolist()')
 change('All actual collocation midpoints are admissible on the audit grid','All actual midpoints and both RMS positions are admissible on the audit grid')
 change('Only tail cells with invalid actual collocation midpoints are bisected,','Only tail cells with invalid actual midpoint/RMS positions are bisected,')
 change('prepared=prepared and not bad,','prepared=prepared and not bad and not bad_cell and not bad_node,')
 change('preparation_gates_passed=prepared and not bad,','preparation_gates_passed=prepared and not bad and not bad_cell and not bad_node,')
 change('bisect only bad actual collocation tail cells','bisect the union of bad actual midpoint/RMS tail cells')
 a.generated_source.write_text(code)
 spec=importlib.util.spec_from_file_location('actual_short_full_BVP_preparation',a.generated_source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.main(a)
 report=json.loads(a.out.read_text());report.update(patch_generator_sha256=sha(__file__),base_prepare_sha256=BASE,generated_prepare_sha256=sha(a.generated_source),
  definition_change='New explicit 1.03 terminal reference and newly frozen complete Schur rows; original 1.04 failed state is not used. Full original midpoint/RMS checks precede any future solve.')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(final_report_sha256=sha(a.out),generated_source_sha256=sha(a.generated_source),generator_sha256=sha(__file__))),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('base-source','generated-source','topic','parent','interface','hold-source','warm','arrays','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
