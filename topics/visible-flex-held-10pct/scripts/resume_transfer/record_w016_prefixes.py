#!/usr/bin/env python3
"""Collect the completed wCut=.16 design prefixes without regenerable arrays."""
import argparse,gzip,hashlib,json
from pathlib import Path
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def scalar(v):return {k:x for k,x in v.items()if not isinstance(x,(dict,list))}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--work',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--names',nargs='+',default=['q010-m16','q0125-m16']);a=p.parse_args()
 names=a.names;runs=[]
 dependencies=['run_large_radius_circle.py','large_radius_local_core.py','local_flatten_core.py','bimodal_chart_loader.py','even_mode_loader.py','plateau_core.py','complementary_moment_basis.py','moment_interval_bounds.py','dual_design_bvp.py','exact_core_lift.py','analytic_adaptive_core_jac.py','bimodal_material_restart.py','material_warm_restart.py']
 for name in names:
  path=a.work/(name+'.json');raw=json.loads(path.read_text());row=raw['rows'][-1]
  assert row['success'] and row['homotopy']==0
  result=scalar(row)
  for k in ['physical_profile','parameters','domain_newton','material_restart','parameter_jac_checks','boundary_jac_checks']:
   if k in row:result[k]=row[k]
  result['summary']=scalar(row['summary']);result['core']=scalar(row['core'])
  inputs={}
  for k in ['port','profile','restart','previous']:
   if raw['arguments'].get(k):
    f=Path(raw['arguments'][k]);inputs[k]=dict(path=str(f),sha256=sha(f))
  cp=a.work/(name+'-lam0.json.gz');check=json.loads(gzip.decompress(cp.read_bytes()))
  for c in check['pp_coefficient_chunks']:assert sha(a.work/c['file'])==c['sha256']
  sources={n:raw['source_sha256'][n]for n in dependencies}
  for n,h in sources.items():assert sha(a.work/'runtime'/n)==h,n
  runs.append(dict(run=name,arguments=raw['arguments'],result=result,input_sha256=inputs,
      executed_dependencies_sha256=sources,historical_source_transforms=raw['source_transforms'],
      raw_result_sha256=sha(path),checkpoint_sha256=sha(cp),coefficient_chunks=check['pp_coefficient_chunks'],
      log_sha256=sha(a.work/(name+'.log')),unabridged_runtime_manifest_sha256=sha(a.work/'runtime/snapshot-hashes.json')))
 out=dict(scope='Actual accepted finite prefixes for the new wCut=.16 physical design; lambda0 and linear port only. Different solved delta/vd mean different g; no closed-family or same-g claim.',runs=runs,
          reproducibility='Prepare resume_n4 sources; regenerate w016 port/profile with n4_thicker_cut_design.py; run run_large_radius_circle.py with the recorded arguments in order. Only source, parameters, scalar findings and hashes are stored.')
 a.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))
if __name__=='__main__':main()
