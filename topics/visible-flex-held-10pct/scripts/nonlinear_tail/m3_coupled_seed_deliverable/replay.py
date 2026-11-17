#!/usr/bin/env python3
"""Replay the recorded m3 finite-tail and coupled seed path in fresh scratch.

The historical fast55 run did not record its initial node budget. This replay
uses nodes=401,max_nodes=4000 there, while preserving all known numerical and
physical settings. It is a declared replay recipe, not a claim that this
entire command has already run. Records retain the historical output hashes.
"""
import argparse,gzip,json,os,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--through',choices=['reference','prefix','tail','coupled','fixed'],default='fixed');a=p.parse_args();here=Path(__file__).resolve().parent;w=a.work.resolve();w.mkdir(parents=True,exist_ok=False)
env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
def run(name,*args):subprocess.run([sys.executable,str(here/name),*map(str,args)],check=True,env=env)
def write(path,obj):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,indent=2)+'\n')
run('recover_m3_source.py','--repo',a.repo,'--dest',w/'recovery');source=w/'recovery/bundle/topics/visible-flexible-closed-surface';short=w/'recovery/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py';base=json.loads((here/'tail-config.json').read_text());write(w/'tail-config.json',base)
run('export_original_worker_port.py','--source-topic',source,'--config',w/'tail-config.json','--out',w/'port8.json')
for name,ang in [('fast55',384),('fast45',256)]:
 d=w/name;run('regenerate_m3_reference.py','--source-topic',source,'--short-bridge',short,'--profile',here/(name+'-reference-profile.json'),'--port',w/'port8.json','--out',d)
if a.through=='reference':raise SystemExit(0)
for name,ang in [('fast55',384),('fast45',256)]:
 d=w/name;run('linear_prefix_m3.py','--source-topic',source,'--short-bridge',short,'--profile',d/'profile.json','--chart',d/'chart.json','--linear-port',d/'port.json','--out-prefix',d/'q020-m8','--amplitude','.02','--warp-reference','.02','--modes','8','--angular',ang,'--audit-angular',('768'if name=='fast55'else '512'),'--nodes','401','--max-nodes','4000','--tol','1e-6','--bc-tol','1e-7','--physical-bc-tol','2e-9')
 run('extract_m3_height.py','--source-topic',source,'--checkpoint',d/'q020-m8.json.gz','--out',d/'H.json')
if a.through=='prefix':raise SystemExit(0)
run('m3_actual_tail_continue.py','--source-topic',source,'--config',w/'tail-config.json','--height-trace',w/'fast55/H.json','--out',w/'fast55-tail','--lambdas=-.001,-.003,-.01,-.03,-.1,-.3,-1','--audit','--stop-on-failure')
# The historical final -1 failed. Its previous response_0006 is the accepted warm.
accept=w/'fast55-tail/response_0006.json.gz'
if not json.loads(gzip.decompress(accept.read_bytes()))['response']['converged']:raise RuntimeError('Historical warm path did not reproduce an accepted -.3 point')
cfg={**base,'initialCheckpoint':str(accept)};write(w/'fast45-warm-config.json',cfg)
run('m3_actual_tail_continue.py','--source-topic',source,'--config',w/'fast45-warm-config.json','--height-trace',w/'fast45/H.json','--out',w/'fast45-tail','--lambdas=-.4,-.5,-.6,-.7,-.8,-.9,-1','--audit','--stop-on-failure')
if a.through=='tail':raise SystemExit(0)
accept=w/'fast45-tail/response_0007.json.gz'
if not json.loads(gzip.decompress(accept.read_bytes()))['response']['converged']:raise RuntimeError('Full fast45 height vector not accepted')
d=w/'coupled';cfg={**base,'initialCheckpoint':str(accept),'traceFile':str(d/'worker-trace.jsonl')};write(d/'config.json',cfg)
common=['--source-topic',source,'--short-bridge',short,'--chart',w/'fast45/chart.json','--linear-port',w/'fast45/port.json','--amplitude','.02','--warp-reference','.02','--modes','8','--angular','256','--audit-angular','512','--max-nodes','4000','--bc-tol','1e-7','--physical-bc-tol','2e-9','--node-heap','2304','--warmup-scales','1','--lagged-tail']
run('couple_m3_smallcut.py',*common,'--profile',w/'fast45/profile.json','--tail-config',d/'config.json','--out-prefix',d/'seed','--restart',w/'fast45/q020-m8.json.gz','--nodes','601','--tol','1e-6')
summary=json.loads((d/'seed-summary.json').read_text())
if not summary['solver_success']:raise RuntimeError('Actual coupled prefix was not accepted')
if a.through=='coupled':raise SystemExit(0)
f=w/'fixed-m8';cfg={**base,'initialCheckpoint':str(d/summary['tail_seam']['tail_record']),'traceFile':str(f/'worker-trace.jsonl')};write(f/'config.json',cfg);write(f/'profile.json',summary['frozen_profile'])
run('couple_m3_smallcut.py',*common,'--profile',f/'profile.json','--tail-config',f/'config.json','--out-prefix',f/'seed','--restart',d/'seed.json.gz','--nodes','701','--tol','3e-7','--fixed')
for folder in [d,f]:
 run('m3_prefix_tensor_diagnostic.py','--source-topic',source,'--short-bridge',short,'--checkpoint',folder/'seed.json.gz','--port',w/'fast45/port.json','--output',folder/'prefix-tensor-diagnostic.json','--angular','512')
print(json.dumps(dict(scope='Finite replay only; no infinite tail or closed-family certificate',work=str(w))))
