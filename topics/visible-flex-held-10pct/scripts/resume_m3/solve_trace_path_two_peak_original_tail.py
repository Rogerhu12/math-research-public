#!/usr/bin/env python3
"""Submit the one complete-row-defined neighbor pair to the original worker.

Only node86/c8 toward +infinity and node86/c11 toward -infinity may differ
from the pinned original failed state. Both are one nextafter step. No search
or retry is implemented. All physical/config/source inputs and the original
2e-9/Jacobian/audit requirements remain unchanged; only IO paths differ.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
TRANSFER=HERE.parent/'resume_transfer'
sys.path.insert(0,str(TRANSFER))
from recovering_tail_client_v2 import (sha,payload_sha,read_gzip,write_new_json,
    exact_equal,check_original_reload_boundary,validate_parameter_io_mapping)

FAILURE_SHA='6f0cdfa7bdc27c330bd3320ba94417e1fb410430dfdcdd3bd685c2944d2411ac'
PROPOSER=HERE/'propose_trace_path_two_peak_neighbors.mjs'
PROPOSER_SHA='12b6e35756a6404a30f98e7c979a14f3bfe2f5e84e6be0c73191e975f4aeb31c'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','failure','candidate','candidate-summary','out-prefix','sparse-helper'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--node-heap',type=int,default=3072)
    args=parser.parse_args();topic=args.source_topic.resolve()
    failure=args.failure.resolve();candidate_file=args.candidate.resolve();prefix=args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True,exist_ok=True)
    summary_file=prefix.with_name(prefix.name+'-summary.json')
    entry_file=prefix.with_name(prefix.name+'-entry.json')
    config_file=prefix.with_name(prefix.name+'-config.json')
    trace_file=prefix.with_name(prefix.name+'-worker.jsonl')
    if any(p.exists() for p in (summary_file,entry_file,config_file,trace_file)):
        raise FileExistsError('Use a fresh single native output prefix')
    if sha(failure)!=FAILURE_SHA or sha(PROPOSER)!=PROPOSER_SHA:
        raise ValueError('Only the declared original failure and candidate generator are allowed')
    original,candidate=read_gzip(failure),read_gzip(candidate_file)
    if (original['response'].get('failed')!='Error: multiple-shooting line search failed at 3.667862901158431e-9' or
        original['response']['lastIteration']['norm']!=3.667862901158431e-9):
        raise ValueError('The pinned original failed response is required')
    check=json.loads(args.candidate_summary.read_text())
    if (candidate.get('solver_success') is not False or candidate.get('candidate_only') is not True or
        check['original_solver_invoked'] is not False or check['input']['sha256']!=FAILURE_SHA or
        check['candidate']['sha256']!=sha(candidate_file) or candidate['input_failure_sha256']!=FAILURE_SHA or
        check['changed_scalars']!=2 or not exact_equal(check['named_changes'],candidate['named_changes']) or
        not check['strict_full_replay_improvement'] or not candidate['strict_full_replay_improvement'] or
        not math.isfinite(check['full_candidate_replay']['norm']) or
        not check['full_candidate_replay']['norm']<check['before']['norm'] or
        check['source_sha256'].get(str(PROPOSER))!=PROPOSER_SHA):
        raise ValueError('A source-bound strictly improved candidate-only record is required')
    for key in ('request','config','source_sha256'):
        if not exact_equal(candidate[key],original[key]):raise ValueError('Candidate changed '+key)
    cp,old=candidate['checkpoint'],original['response']['checkpoint']
    for key in ('parameters','rawNode','cutHeight'):
        if not exact_equal(cp[key],old[key]):raise ValueError('Candidate changed original identity: '+key)
    changes=check['named_changes']
    if [(c['node'],c['component'],c['direction']) for c in changes]!=[(86,8,1),(86,11,-1)]:
        raise ValueError('The complete predeclared peak set/directions changed')
    for c in changes:
        destination=math.inf if c['direction']==1 else -math.inf
        if (not math.isfinite(c['before']) or not math.isfinite(c['after']) or
            not exact_equal(math.nextafter(c['before'],destination),c['after']) or
            not exact_equal(c['after']-c['before'],c['signed_step'])):
            raise ValueError('Each changed value must be precisely its declared directed neighbor')
    if len(cp['states'])!=len(old['states']):raise ValueError('Candidate grid changed')
    found=[]
    for i,(left,right) in enumerate(zip(old['states'],cp['states'])):
        if len(left)!=len(right):raise ValueError('Candidate state dimension changed')
        for j,(a,b) in enumerate(zip(left,right)):
            if not exact_equal(a,b):found.append((i,j,a,b))
    expected=[(c['node'],c['component'],c['before'],c['after']) for c in changes]
    if not exact_equal(found,expected):raise ValueError('Only the declared two free interior scalar changes are allowed')
    if not exact_equal(cp['rawStates'],[cp['states'][i] for i in cp['rawNode']]):
        raise ValueError('The original raw-node copy changed')
    sources=dict(check['source_sha256'])
    for name,digest in original['source_sha256'].items():sources[str(topic/'scripts'/name)]=digest
    sources[str(Path(__file__).resolve())]=sha(__file__)
    sources[str(TRANSFER/'recovering_tail_client_v2.py')]=sha(TRANSFER/'recovering_tail_client_v2.py')
    sparse=args.sparse_helper.resolve();sources[str(sparse)]=sha(sparse)
    for file,digest in sources.items():
        if sha(file)!=digest:raise ValueError('An execution source changed: '+file)
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER']=str(sparse)
    os.environ['VISIBLE_FLEX_SPARSE_PYTHON']=sys.executable
    cfg=copy.deepcopy(original['config'])
    if cfg.get('designInitialCheckpoint') or cfg.get('secantCheckpoint'):
        raise ValueError('Only the explicit same-state initializer is allowed')
    cfg['initialCheckpoint']=str(candidate_file);cfg['traceFile']=str(trace_file)
    changed=sorted(k for k in set(cfg)|set(original['config']) if cfg.get(k)!=original['config'].get(k))
    if set(changed)-{'initialCheckpoint','traceFile'}:raise ValueError('A physical or numerical option changed')
    if (cfg['solveTolerance']!=2e-9 or cfg.get('sharedEngines') or cfg['spacing']!=3 or
        cfg['modes']!=8 or cfg['shootingParts']!=16 or cfg['steps']!=16):
        raise ValueError('The exact original M8/parts16/RK16/native gate is required')
    write_new_json(config_file,cfg)
    entry=dict(scope=__doc__,command=[sys.executable,*sys.argv],failure=dict(path=str(failure),sha256=sha(failure)),
        candidate=dict(path=str(candidate_file),sha256=sha(candidate_file)),
        candidate_summary=dict(path=str(args.candidate_summary.resolve()),sha256=sha(args.candidate_summary)),
        source_sha256=sources,configuration=dict(path=str(config_file),sha256=sha(config_file)),
        configuration_changed_keys=changed,physical_request=old['cutHeight'],original_gate=cfg['solveTolerance'],
        original_unaccepted_replay=check['full_candidate_replay']['norm'],named_changes=changes,
        changed_scalars=2,requested_jacobian=True,requested_audit=True,node_heap_resource_only=args.node_heap)
    write_new_json(entry_file,entry)
    file=topic/'scripts/950f-tail-client-v3.py'
    spec=importlib.util.spec_from_file_location('trace_path_unchanged_native_client',file)
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    tail=None;began=time.monotonic()
    result=dict(scope=__doc__,entry=dict(path=str(entry_file),sha256=sha(entry_file)),solver_success=False,prefix_solver_invoked=False)
    print(json.dumps(dict(event='original_named_pair_native_started',entry=str(entry_file),sha256=sha(entry_file))),flush=True)
    try:
        tail=native.WeightedTailPort(config_file,topic/'repro/source-root',prefix.with_name(prefix.name+'_tail'),node_heap=args.node_heap)
        result['ready_parameter_metadata_transition']=validate_parameter_io_mapping(cp['parameters'],tail.ready['parameters'],original['config'],cfg)
        result['reload_arithmetic']=check_original_reload_boundary(candidate_file,old['cutHeight'],tail.cut['radius'])
        response=tail.solve(np.asarray(old['cutHeight'],float),jacobian=True,audit=True)
        J=np.asarray(response['heightJetJacobian'],float)
        if (response.get('converged') is not True or not math.isfinite(response['residual']) or
            not response['residual']<cfg['solveTolerance'] or J.size!=208 or not np.all(np.isfinite(J)) or
            response.get('audit') is None):
            raise ValueError('Original worker did not return the complete original-gate/Jacobian/audit result')
        result.update(solver_success=True,original_residual=response['residual'],finite_jacobian_entries=int(J.size),
            audit_returned=True,final_state_nodes=len(response['checkpoint']['states']),native_iterations=len(response['history']),
            original_worker_final_states_equal_candidate=exact_equal(response['checkpoint']['states'],cp['states']))
    except Exception as error:
        result['error']=repr(error)
    finally:
        if tail is not None:
            try:
                result['native_calls']=tail.calls
                file=tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
                if file.is_file():
                    saved=read_gzip(file)
                    if (not exact_equal(saved['request'],dict(height=old['cutHeight'],jacobian=True,audit=True)) or
                        not exact_equal(saved['config'],cfg)):
                        raise AssertionError('Original native request/config identity changed')
                    result['native_record']=dict(path=str(file),sha256=sha(file))
                    if saved['response'].get('lastIteration'):result['last_iteration']=saved['response']['lastIteration']
            finally:tail.close()
            result['worker_returncode']=tail.proc.poll()
        for file,digest in sources.items():
            if sha(file)!=digest:raise AssertionError('Executed source changed: '+file)
        result['seconds']=time.monotonic()-began;write_new_json(summary_file,result)
        print(json.dumps(dict(event='original_named_pair_native_terminal',**result)),flush=True)
    if not result['solver_success']:raise SystemExit(2)


if __name__=='__main__':main()
