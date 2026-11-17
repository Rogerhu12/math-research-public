#!/usr/bin/env python3
"""Actual m=3 finite-tail continuation through the original R114 client/worker.

No source equation, root guard or Newton criterion is changed. Signed input is
lambda times the complete supplied physical upper height vector; lambda<0
implements the upper reflection convention. Scaled vectors alone are not
coupled prefixes at scaled core amplitude. Checkpoints stay outside git.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,gzip,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
for k in ('source-topic','config','height-trace','out'):p.add_argument('--'+k,type=Path,required=True)
p.add_argument('--lambdas',default='-.00001,-.00002,-.00004,-.00008,-.00016,-.00032,-.00064,-.00128,-.00256,-.00512,-.01024,-.02048,-.04096,-.08192,-.16384,-.32768,-.65536,-1')
p.add_argument('--audit',action='store_true');p.add_argument('--stop-on-failure',action='store_true')
a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
cfg=json.loads(a.config.read_text());cfg['traceFile']=str((a.out/'worker-trace.jsonl').resolve())
if cfg['spacing']!=3:raise ValueError('This branch requires physical frequencies 3,6,...')
effective=a.out/'effective-config.json';effective.write_text(json.dumps(cfg,indent=2)+'\n')
client_path=a.source_topic/'scripts/950f-tail-client-v3.py'
spec=importlib.util.spec_from_file_location('original_m3_tail_client',client_path);client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
hdata=json.loads(a.height_trace.read_text());original=np.array(hdata['H'],float);M=cfg['modes'];h=np.zeros(M);h[:min(M,len(original))]=original[:M]
if hdata.get('modes',list(3*np.arange(1,len(original)+1)))[:len(original)]!=list(3*np.arange(1,len(original)+1)):raise ValueError('Trace frequencies are not m=3 multiples')
report=dict(scope=__doc__,config_sha256=sha(a.config),height_trace_sha256=sha(a.height_trace),client_sha256=sha(client_path),worker_sha256=sha(a.source_topic/'scripts/950f-tail-stage-port-v3.mjs'),base_mode=3,modes=M,omitted_height_l1=float(abs(original[M:]).sum()),runs=[])
port=None;started=time.monotonic()
try:
 port=client.WeightedTailPort(effective,a.source_topic/'repro/source-root',a.out/'response',node_heap=2304)
 report['cut']={k:port.cut[k]for k in ['radius','backgroundSlope','backgroundSecond','E','Ep']};report['source_sha256']=port.sources
 report['resolved_numerics']={k:port.ready['parameters'].get(k)for k in ['modes','spacing','depth','physicalDepth','quadrature','steps','projectionFloor']}
 print(json.dumps(dict(event='ready',cut=report['cut'],modes=M,depth=cfg['depth'],resolved_numerics=report['resolved_numerics'])),flush=True)
 for lam in map(float,a.lambdas.split(',')):
  before=time.monotonic();r=None;error=None
  try:r=port.solve(lam*h,jacobian=False,audit=a.audit)
  except Exception as e:error=repr(e)
  file=a.out/f'response_{port.calls:04d}.json.gz'
  if r is None and file.exists():r=json.loads(gzip.decompress(file.read_bytes()))['response']
  row=dict(lam=lam,converged=bool(r and r.get('converged')),seconds=time.monotonic()-before,error=error,response_file=file.name,response_sha256=sha(file)if file.exists()else None)
  if r:
   row.update({k:r.get(k)for k in ['residual','audit','failed','lastIteration']})
   hist=r.get('history')or[]
   if hist:row.update(final_minA=hist[-1].get('minA'),final_minD=hist[-1].get('minD'))
   if r.get('jets')and 'Hr'in hdata:row['linear_prefix_slope_mismatch_l1']=float(abs(np.array(r['jets']['slope'])-lam*np.array(hdata['Hr'])[:M]).sum())
  report['runs'].append(row);report['seconds']=time.monotonic()-started;(a.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(row),flush=True)
  if not row['converged']and a.stop_on_failure:break
finally:
 if port:port.close()
 report['seconds']=time.monotonic()-started;(a.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
