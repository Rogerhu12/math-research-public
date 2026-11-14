#!/usr/bin/env python3
"""Verify the actual next-worker tangent restore without a new nonlinear solve.

This opens the unchanged production full-tangent client against an explicitly
bound accepted checkpoint, verifies the new worker's original predictor-factory
restore and exact physical identity, then closes it before any request. It does
not calculate or accept new-H jets, a prefix, an audit, or a geometric result.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
for key in tuple(os.environ):
    if key in ('GH_TOKEN','GITHUB_TOKEN','GITHUB_PAT') or key.startswith('GIT_CONFIG_'):
        os.environ.pop(key,None)
import argparse,hashlib,json,time
from pathlib import Path
from root_actual_staged_tail import read_json,equation_config,sha
from strong_full_tangent_resource_guard import resource_port_class
import strong_full_tangent_tail_client as client


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('config','accepted-tail','snapshot','bootstrap-summary','source-topic','out-prefix','reference-adapter','calibration-ledger','stage-cache-directory'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args();start=time.monotonic();prefix=a.out_prefix
    prefix.parent.mkdir(parents=True,exist_ok=True)
    report=prefix.with_name(prefix.name+'-summary.json')
    if report.exists():raise FileExistsError(report)
    original=read_json(a.config);accepted=read_json(a.accepted_tail);saved=read_json(a.bootstrap_summary)
    if (saved.get('status')!='complete' or saved['accepted_tail']['sha256']!=sha(a.accepted_tail)
            or saved['snapshot']['manifestSha256']!=sha(a.snapshot)
            or not accepted['response']['converged'] or not accepted['response'].get('audit')
            or not accepted['request']['jacobian'] or not accepted['request']['audit']
            or equation_config(original)!=equation_config(accepted['config'])):
        raise ValueError('Original accepted checkpoint, bootstrap identity or equations differ')
    cfg=dict(original)
    for key,suffix in [('traceFile','-trace.jsonl'),('iterationCheckpointFile','-iteration.json.gz'),('trialDiagnosticFile','-trials.jsonl')]:
        cfg[key]=str(prefix.with_name(prefix.name+suffix).resolve())
    cfg['initialCheckpoint']=str(a.accepted_tail.resolve())
    cp=prefix.with_name(prefix.name+'-config.json');cp.open('x').write(json.dumps(cfg,indent=2)+'\n')
    updates={'VISIBLE_FLEX_SOURCE_TOPIC':str(a.source_topic.resolve()),
        'VISIBLE_FLEX_EXACT_STAGE_CACHE':str(a.stage_cache_directory.resolve()),
        'VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX':str(prefix.resolve())+'-exact-initial',
        'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT':'8',
        'VISIBLE_FLEX_FROZEN_LEDGER_READY':str(a.calibration_ledger.resolve()),
        'VISIBLE_FLEX_FROZEN_STORED_READY':str(a.reference_adapter.resolve()),
        'VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND':'fourier-root',
        'VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND':'tangent',
        'VISIBLE_FLEX_FULL_TANGENT_START_MANIFEST':str(a.snapshot.resolve())}
    before={key:os.environ.get(key) for key in updates};tail=None
    result=dict(scope=__doc__,status='running',source_sha256=sha(__file__),
        accepted_tail=dict(file=str(a.accepted_tail),sha256=sha(a.accepted_tail)),
        snapshot=dict(file=str(a.snapshot),sha256=sha(a.snapshot)),
        original_equations_unchanged=True,nonlinear_requests=0,new_H_accepted=False)
    try:
        os.environ.update(updates)
        Port=resource_port_class(client.WeightedTailPort,256,4)
        tail=Port(cp,a.source_topic/'repro/source-root',prefix.with_name(prefix.name+'-response'),node_heap=256)
        ready=tail.ready;restored=ready.get('fullFlowTangentRestored')
        if not restored or not restored.get('originalFactoryCalled') or not restored.get('initialGuessOnly'):
            raise ValueError('Independent worker did not restore the original full-state predictor')
        reference=read_json(a.reference_adapter);reference=reference.get('ready',reference)
        expected=reference.get('storedMetricAdapter',reference.get('stored_metric'))
        actual=ready['storedMetricAdapter']
        if expected is None or equation_config(expected['physicalParameters'])!=equation_config(actual['physicalParameters']):
            raise ValueError('Restored worker changed the original physical equations')
        for key in ('frozenWarpAlpha','profileFingerprintBefore','profileFingerprintAfter','fingerprintFields','fingerprintFractions'):
            if actual[key]!=expected[key]:raise ValueError('Restored original geometry differs: '+key)
        ready_path=prefix.with_name(prefix.name+'-ready.json');ready_path.open('x').write(json.dumps(ready,indent=2)+'\n')
        result.update(status='complete',independent_worker_started=True,original_factory_restored=True,
            original_geometry_exactly_matched=True,restored=restored,
            ready=dict(file=str(ready_path),sha256=sha(ready_path)))
    except Exception as e:
        result.update(status='failed',error=repr(e));raise
    finally:
        if tail is not None:
            tail.close();result['owned_worker_returncode_after_close']=tail.proc.poll()
        trace=prefix.with_name(prefix.name+'-trace.jsonl')
        if trace.exists():
            rows=[json.loads(line) for line in trace.read_text().splitlines() if line.strip()]
            result['trace_events']=[row['event'] for row in rows]
            if any(row['event'] in ('iteration','response','exact_stage_cache','exact_initial_stage_seed_saved') for row in rows):
                result['status']='failed';result['unexpected_request_trace']=True
        result['wall_seconds']=time.monotonic()-start
        report.open('x').write(json.dumps(result,indent=2,allow_nan=False)+'\n')
        for key,value in before.items():
            if value is None:os.environ.pop(key,None)
            else:os.environ[key]=value
        print(json.dumps(result),flush=True)
    if result['status']!='complete' or result.get('owned_worker_returncode_after_close')!=0:
        raise RuntimeError('Independent startup restore did not complete normally')


if __name__=='__main__':main()
