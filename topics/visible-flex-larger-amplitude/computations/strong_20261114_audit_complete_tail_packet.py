#!/usr/bin/env python3
"""Run the original complete tail audit at an already computed complete H.

The input packet supplies its complete H and same-discretization raw state as
a warm guess. Every original nonlinear residual, full Jacobian, positivity and
audit check executes. No prefix is accepted here. This produces an actually
audited current-H packet usable by the existing exact-H, idle-worker release
adapter; it never substitutes an old A audit for a different H.
"""
from __future__ import annotations
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,gzip,hashlib,json,time
from pathlib import Path

IO={'traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'}

def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def equations(p):return {k:v for k,v in p.items() if k not in IO}
def write(p,v):Path(p).write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')

def main():
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('packet','accepted-reference','source-topic','frozen-reference-ready','frozen-calibration-ledger','stage-cache-directory','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
 p.add_argument('--node-heap',type=int,default=768);p.add_argument('--node-young-semi-space',type=int,default=16)
 a=p.parse_args();packet=read(a.packet);reference=read(a.accepted_reference);cfg=dict(packet['config']);H=packet['request']['height'];M=cfg['modes'];prefix=a.out_prefix.resolve();prefix.parent.mkdir(exist_ok=True,parents=True);file=lambda s:prefix.with_name(prefix.name+s)
 if not packet['response']['converged'] or packet['response']['residual']>cfg['solveTolerance']:raise ValueError('Input is not a completed original full-H tail response')
 if equations(cfg)!=equations(reference['actual_tail']['config']):raise ValueError('Physical or numerical tail changed')
 if packet['response']['checkpoint']['cutHeight']!=H or len(H)!=M:raise ValueError('The complete current H is not bound to its raw state')
 for key,suffix in [('traceFile','-trace.jsonl'),('iterationCheckpointFile','-iteration.json.gz'),('trialDiagnosticFile','-trials.jsonl')]:cfg[key]=str(file(suffix))
 cfg['initialCheckpoint']=str(a.packet.resolve());cfgpath=file('-config.json');write(cfgpath,cfg)
 env={'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT':'8','VISIBLE_FLEX_FROZEN_LEDGER_READY':str(a.frozen_calibration_ledger.resolve()),'VISIBLE_FLEX_FROZEN_STORED_READY':str(a.frozen_reference_ready.resolve()),'VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND':'fourier-root','VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND':'tangent','VISIBLE_FLEX_EXACT_STAGE_CACHE':str(a.stage_cache_directory.resolve()),'VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX':str(file('-seed'))}
 os.environ.update(env)
 from strong_full_tangent_tail_client import WeightedTailPort
 from strong_full_tangent_resource_guard import resource_port_class
 Port=resource_port_class(WeightedTailPort,a.node_heap,a.node_young_semi_space)
 report=dict(scope=__doc__,status='running',input_packet=dict(file=str(a.packet),sha256=sha(a.packet)),source_sha256=sha(__file__),complete_H=H,original_H_preserved=True,actual_prefix_accepted=False,audit_requested=True,config_sha256=sha(cfgpath));start=time.monotonic();tail=None
 write(file('-summary.json'),report)
 try:
  tail=Port(cfgpath,a.source_topic/'repro/source-root',file('-response'),node_heap=a.node_heap)
  expected=reference['actual_tail']['ready']['storedMetricAdapter'];actual=tail.ready['storedMetricAdapter']
  for key in ('frozenWarpAlpha','profileFingerprintBefore','profileFingerprintAfter','fingerprintFields','fingerprintFractions'):
   if actual[key]!=expected[key]:raise ValueError('Original stored physical profile differs: '+key)
  if equations(actual['physicalParameters'])!=equations(expected['physicalParameters']):raise ValueError('Stored complete tail parameters differ')
  write(file('-ready.json'),tail.ready);print(json.dumps(dict(event='actual_current_H_tail_audit_ready',H=H)),flush=True)
  response=tail.solve(H,jacobian=True,audit=True)
  if not response.get('converged') or response.get('audit') is None or response['residual']>cfg['solveTolerance'] or response['checkpoint']['cutHeight']!=H or len(response['heightJetJacobian'])!=(3*M+2)*M:raise ValueError('Original full current-H audit conditions did not pass')
  report.update(status='complete',residual=response['residual'],audit=response['audit'],response_file=str(file('-response_0001.json.gz')),response_sha256=sha(file('-response_0001.json.gz')),ready_file=str(file('-ready.json')),ready_sha256=sha(file('-ready.json')))
  print(json.dumps(dict(event='actual_current_H_tail_audit_complete',residual=response['residual'])),flush=True)
 except BaseException as e:
  report.update(status='failed',error=repr(e));raise
 finally:
  if tail is not None:
   report['worker_returncode_before_close']=tail.proc.poll();tail.close();report['worker_returncode_after_close']=tail.proc.poll()
  report['seconds']=time.monotonic()-start;write(file('-summary.json'),report)
if __name__=='__main__':main()
