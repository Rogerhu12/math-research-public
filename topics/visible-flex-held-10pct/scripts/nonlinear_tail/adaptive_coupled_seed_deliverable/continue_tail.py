"""Actual finite nonlinear Darboux-tail continuation of a fixed physical H trace.

This uses the original solver, guards and full nonlinear momentum equations.
Finite depth/modes and omitted H modes are explicit; no linear capacity bound
is used as a stopping rule. Generated response checkpoints stay outside git.
"""
import argparse,gzip,hashlib,importlib.util,json,os,time,types
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--height-trace',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--lambdas',default='.0001,.0003,.001,.003,.01,.02,.04,.06,.08,.10,.15,.2,.3,.5,.75,1');p.add_argument('--audit',action='store_true');p.add_argument('--stop-on-failure',action='store_true');p.add_argument('--worker',default='db6f-prefix-tail-trial-worker.mjs',choices=['db6f-prefix-tail-trial-worker.mjs','78718-prefix-tail-tangent-fourier-worker.mjs']);p.add_argument('--worker-path',type=Path);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
cfg=json.loads(a.config.read_text());cfg['traceFile']=str(a.out/'worker-trace.jsonl');cfg['trialDiagnosticFile']=str(a.out/'trial-diagnostics.jsonl');cfg['iterationCheckpointFile']=str(a.out/'iteration-recovery.json.gz');(a.out/'effective-config.json').write_text(json.dumps(cfg,indent=2)+'\n')
client_path=a.source_topic/'scripts/db6f-prefix-tail-trial-client.py';client_source=client_path.read_text();old_worker="worker=Path(__file__).with_name('db6f-prefix-tail-trial-worker.mjs')";worker_path=a.worker_path.resolve() if a.worker_path else a.source_topic/'scripts'/a.worker;new_worker="worker=Path("+repr(str(worker_path))+")";assert client_source.count(old_worker)==1;client_source=client_source.replace(old_worker,new_worker)
old_hash="worker.with_name(name).read_bytes()";new_hash="Path(__file__).with_name(name).read_bytes()";assert client_source.count(old_hash)==1;client_source=client_source.replace(old_hash,new_hash)
mod=types.ModuleType('actual_trial_client');mod.__file__=str(client_path);exec(compile(client_source,str(client_path),'exec'),mod.__dict__);os.environ['VISIBLE_FLEX_SOURCE_TOPIC']=str(a.source_topic)
hdata=json.loads(a.height_trace.read_text());M=cfg['modes'];original=np.array(hdata['H']);h=np.zeros(M);h[:min(M,len(original))]=original[:M]
report=dict(scope=__doc__,height_trace=str(a.height_trace),height_trace_sha256=hashlib.sha256(a.height_trace.read_bytes()).hexdigest(),source_checkpoint_sha256=hdata.get('checkpoint_sha256'),worker=str(worker_path),worker_sha256=hashlib.sha256(worker_path.read_bytes()).hexdigest(),client_worker_selection_transform=[old_worker,new_worker],client_hash_location_transform=[old_hash,new_hash],config=cfg,original_height_modes=len(original),tail_modes=M,omitted_height_l1=float(abs(original[M:]).sum()),runs=[])
start=time.monotonic();port=None
try:
 port=mod.WeightedTailPort(a.out/'effective-config.json',a.source_topic/'repro/source-root',a.out/'response',node_heap=2304);report['ready']={k:v for k,v in port.ready.items()if k!='parameters'};print(json.dumps(dict(event='ready',modes=M,depth=cfg['depth'],physical_protect=cfg['protectCell'],cut=port.cut,omitted_height_l1=report['omitted_height_l1'])),flush=True)
 for lam in [float(v)for v in a.lambdas.split(',')]:
  t=time.monotonic();result=None;error=None
  try:result=port.solve(lam*h,jacobian=False,audit=a.audit)
  except Exception as e:error=repr(e)
  record=a.out/f'response_{port.calls:04d}.json.gz'
  if result is None and record.exists():result=json.loads(gzip.decompress(record.read_bytes()))['response']
  row=dict(lam=lam,seconds=time.monotonic()-t,converged=bool(result and result.get('converged')),error=error,response_file=record.name,response_sha256=hashlib.sha256(record.read_bytes()).hexdigest()if record.exists()else None)
  if result:
   row.update({k:result.get(k)for k in ['residual','jets','history','audit','failed','lastIteration']});history=result.get('history')or[]
   if history:row['final_minA']=history[-1].get('minA');row['final_minD']=history[-1].get('minD')
   if result.get('jets'):
    target_slope=lam*np.array(hdata['Hr'])[:M];actual=np.array(result['jets']['slope']);row['linear_prefix_radial_slope_mismatch_l1']=float(abs(actual-target_slope).sum())
  report['runs'].append(row);report['seconds']=time.monotonic()-start;(a.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
  print(json.dumps({k:v for k,v in row.items()if k not in ['jets','history']}),flush=True)
  if not row['converged']and a.stop_on_failure:break
finally:
 if port:port.close()
 report['seconds']=time.monotonic()-start;(a.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
