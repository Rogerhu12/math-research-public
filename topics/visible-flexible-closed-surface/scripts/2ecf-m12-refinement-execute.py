#!/usr/bin/env python3
"""Reproducible original Q-free same-g refinement from an actual saved parent.

All numerical inputs are explicit. This runs exact transfer, real nonlinear
LM, R226, existing metric/geometry consumers and every ancestor observation.
It never generates or substitutes a parent field, target metric or query.
"""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('scripts','data','old-grid','old-field','old-result','old-correction-bounds','new-grid','query-report','query-cache','source-bounds','out-dir'):
  ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--solver-entry',type=Path,default=HERE/'2ecf-m12-h2-disk-normal-cached-lm.py')
 ap.add_argument('--lambda-step',type=float,default=1e-13);ap.add_argument('--steps',type=int,default=1)
 ap.add_argument('--block',type=int,default=24);ap.add_argument('--normal-assembly-block',type=int,default=8)
 ap.add_argument('--hessian-step-cap',type=float,default=.05)
 a=ap.parse_args();out=a.out_dir;out.mkdir(parents=True,exist_ok=True)
 recordpath=out/'execution.json';result=out/'result.json';field=Path(str(result)+'.field.npz')
 if recordpath.exists() or result.exists() or field.exists():raise FileExistsError('A fresh refinement output directory is required')
 old=json.loads(a.old_result.read_text());bounds=json.loads(a.old_correction_bounds.read_text())
 for k,p in [('field_sha256',a.old_field),('grid_sha256',a.old_grid)]:
  if old[k]!=sha(p) or bounds[k]!=sha(p):raise ValueError('Actual parent/result/R226 identity mismatch '+k)
 query=json.loads(a.query_report.read_text())
 if 'source_regularization' in query:raise ValueError('This driver only consumes the explicit original Q-free source')
 if query['endpoint_cache_sha256']!=sha(a.query_cache):raise ValueError('Actual complete query cache changed')
 s=a.scripts;common=['--scripts',str(s),'--data',str(a.data)]
 base=['--grid',str(a.new_grid),'--field',str(field),'--result',str(result)]
 transfer=out/'warm-transfer.json';initial=Path(str(transfer)+'.field.npz');correction=out/'correction-bounds.json'
 commands=[
  ('actual-exact-warm-transfer',['python3',str(s/'6a65-m12-exact-radial-angular-warm-transfer.py'),'--scripts',str(s),'--old-field',str(a.old_field),'--old-grid',str(a.old_grid),'--old-result',str(a.old_result),'--old-correction-bounds',str(a.old_correction_bounds),'--new-grid',str(a.new_grid),'--out',str(transfer)]),
  ('actual-original-g-H2-direct-LM',['python3','-u',str(a.solver_entry),*common,'--grid',str(a.new_grid),'--query-report',str(a.query_report),'--query-cache',str(a.query_cache),'--transfer-receipt',str(transfer),'--initial-field',str(initial),'--initial-result',str(a.old_result),'--out',str(result),'--lambda-step',str(a.lambda_step),'--steps',str(a.steps),'--hessian-step-cap',str(a.hessian_step_cap),'--block',str(a.block),'--normal-assembly-block',str(a.normal_assembly_block)]),
  ('actual-field-R226',['python3',str(s/'6a65-m12-entire-half-continuous-correction-bounds.py'),*common,*base,'--out',str(correction)]),
  ('actual-field-original-global-geometry-consumer',['python3',str(s/'6a65-m12-entire-half-actual-field-geometry-transfer.py'),'--source-bounds',str(a.source_bounds),'--correction-bounds',str(correction),*base,'--out',str(out/'geometry.json')]),
  ('actual-field-original-R236',['python3',str(s/'6a65-m12-local-bernstein-angular-metric-budget.py'),*common,*base,'--correction-bounds',str(correction),'--out',str(out/'metric-budget.json')]),
  ('actual-field-existing-two-window-microspan',['python3',str(HERE/'2ecf-m12-declared-basis-observer.py'),'--kind','microspan',*common,*base,'--query-report',str(a.query_report),'--query-cache',str(a.query_cache),'--out',str(out/'microspan-observer.json')]),
  ('actual-field-true-parent-and-child-ancestor-union',['python3',str(HERE/'2ecf-m12-quadrature-observer-union.py'),'--initial-field',str(initial),*common,*base,'--query-report',str(a.query_report),'--query-cache',str(a.query_cache),'--out',str(out/'ancestor-observer-union.json')])]
 record={'schema':'2ecf-M12-explicit-original-Q-free-refinement-execution-v1','driver_sha256':sha(__file__),
  'actual_driver_PID':os.getpid(),'input_sha256':{k:sha(getattr(a,k.replace('-','_'))) for k in ['data','old-grid','old-field','old-result','old-correction-bounds','new-grid','query-report','query-cache','source-bounds','solver-entry']},
  'parameters':{'lambda_step':a.lambda_step,'steps':a.steps,'hessian_step_cap':a.hessian_step_cap,'block':a.block,'normal_assembly_block':a.normal_assembly_block},
  'thread_environment':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},
  'actual_parent_has_returned_and_R226_matches':True,'initialization_is_zero':False,'commands':commands,'stages':[],'finished':False}
 def save():recordpath.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
 save();print(json.dumps({'actual_driver_PID':os.getpid(),'directory':str(out),'actual_parent_field_sha256':sha(a.old_field)}),flush=True)
 for name,cmd in commands:
  print(json.dumps({'stage':name,'status':'starting'}),flush=True);began=time.monotonic()
  child=subprocess.Popen(cmd);record['active_stage']={'name':name,'PID':child.pid};save();child.wait()
  record['stages'].append({'stage':name,'exit_code':child.returncode,'seconds':time.monotonic()-began});record['active_stage']=None;save()
  if child.returncode:raise SystemExit(child.returncode)
 record['finished']=True;record['output_sha256']={p.name:sha(p) for p in out.iterdir() if p.is_file() and p.name!='execution.json'};save()
 print(json.dumps({'finished':True,'directory':str(out),'output_sha256':record['output_sha256']}),flush=True)
if __name__=='__main__':main()
