#!/usr/bin/env python3
"""Frozen weighted-tail finite nonlinear continuation, with full saved states.

This is an actual finite Galerkin shooting calculation. It neither replaces
the infinite tail by an exact collar nor certifies reach of a closed surface.
"""
import argparse, gzip, hashlib, json, os, subprocess, time
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--config',type=Path,required=True)
p.add_argument('--source-root',type=Path,required=True)
p.add_argument('--out',type=Path,required=True)
p.add_argument('--amplitudes',type=float,nargs='+',default=[1e-7,3e-7,1e-6,3e-6,1e-5,3e-5,.0001,.0003,.0006,.001,.00135])
p.add_argument('--node-heap',type=int,default=768)
p.add_argument('--no-audit',action='store_true')
a=p.parse_args()
cfg=json.loads(a.config.read_text())
if a.out.exists(): raise FileExistsError(a.out)
env=dict(os.environ,VISIBLE_FLEX_SOURCE_ROOT=str(a.source_root),CLOSING_TAIL_CACHE=str(a.source_root/'topics/large-amplitude-twist-flex/scripts'),NODE_OPTIONS=f'--max-old-space-size={a.node_heap}')
worker=Path(__file__).with_name('950f-tail-stage-port.mjs')
source_files=[worker,Path(__file__),worker.with_name('closing_recalibrated_tail.mjs'),worker.with_name('closing_weighted_tail.mjs'),worker.with_name('950f-tail-stage-core.mjs'),worker.with_name('950f-tail-stage-split.mjs'),worker.with_name('950f-tail-subdivision.mjs')]
result=dict(scope=__doc__,config=cfg,sources={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in source_files},rows=[])
start=time.time()
def save():
 result['seconds']=time.time()-start
 a.out.write_text(json.dumps(result,indent=2)+'\n')
def brief(obj):
 print(json.dumps(obj,ensure_ascii=False),flush=True)
err=a.out.with_suffix('.stderr.log')
with err.open('x') as ef:
 proc=subprocess.Popen(['node',str(worker),str(a.config)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=ef,text=True,bufsize=1,env=env)
 try:
  line=proc.stdout.readline()
  if not line: raise RuntimeError(f'Initialization failed; see {err.name}')
  ready=json.loads(line); result['ready']=ready; save()
  brief(dict(event='ready',seconds=time.time()-start,linearSlope=ready.get('linearSlope'),modes=cfg['modes'],depth=cfg['depth']))
  for i,amp in enumerate(a.amplitudes,1):
   h=[-amp]+[0.]*(cfg['modes']-1)
   request=dict(height=h,jacobian=False,audit=not a.no_audit)
   before=time.time();proc.stdin.write(json.dumps(request)+'\n');proc.stdin.flush()
   line=proc.stdout.readline()
   if not line: raise RuntimeError(f'Worker ended; see {err.name}')
   response=json.loads(line)
   record=dict(request=request,response=response,config=cfg,source_hashes=result['sources'])
   file=a.out.with_name(a.out.stem+f'-state-{i:03d}.json.gz')
   raw=gzip.compress((json.dumps(record,separators=(',',':'))+'\n').encode(),mtime=0)
   if len(raw)>=5_000_000: raise RuntimeError('Repository file size limit exceeded')
   with file.open('xb') as f:f.write(raw)
   jets=response.get('jets',{})
   row=dict(amplitude=amp,seconds=time.time()-before,converged=response.get('converged',False),residual=response.get('residual'),error=response.get('failed'),audit=response.get('audit'),cut_slope=jets.get('slope'),cut_mean_slope_correction=jets.get('meanSlopeCorrection'),cut_fullD=jets.get('endpointFullD'),iterations=response.get('history'),last_iteration=response.get('lastIteration'),state_file=file.name)
   result['rows'].append(row);save();brief(row)
   if not row['converged']:break
 except Exception as e:
  result['error']=repr(e);save();brief(dict(error=repr(e)))
 finally:
  if proc.poll() is None:
   try:
    proc.stdin.write('{"stop":true}\n');proc.stdin.flush();proc.stdin.close();proc.wait(timeout=15)
   except Exception:proc.terminate()
