#!/usr/bin/env python3
"""One original DN request from a single reverse selected-flow initializer.

Independently bind the complete actual over-gate set, source/flow-row records,
full-state difference and both boundaries. The candidate changes each named
coordinate to its current original full-Jac flow in decreasing stage order.
Its locality bound must strictly improve the original norm; it need not be
below the final gate to be an initial guess. Only the original complete DN,
finite Jacobian/audit and unchanged strict 2e-9 gate can accept a response.
No physical parameter change, boundary change, repeated pass or retry.
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
from recovering_tail_client_v2 import (sha,read_gzip,write_new_json,exact_equal,
    check_original_reload_boundary,validate_parameter_io_mapping)
PROPOSER=HERE/'propose_complete_row_reverse_flow.mjs'
PROPOSER_SHA='dc60aefb800c4064d795ae9d8b287f60e7f00606209aef1c4f8dae5df2b64db1'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','failure','complete-rows','candidate','candidate-summary','out-prefix','sparse-helper'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--node-heap',type=int,default=3072)
    args=parser.parse_args();topic=args.source_topic.resolve();prefix=args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True,exist_ok=True)
    files={key:prefix.with_name(prefix.name+'-'+key+suffix) for key,suffix in
           (('entry','.json'),('config','.json'),('worker','.jsonl'),('summary','.json'))}
    if any(file.exists() for file in files.values()):raise FileExistsError('Use a fresh one-shot native prefix')
    failure=args.failure.resolve();candidate_file=args.candidate.resolve()
    original,candidate=read_gzip(failure),read_gzip(candidate_file)
    rows=json.loads(args.complete_rows.read_text());check=json.loads(args.candidate_summary.read_text())
    if (not original['response'].get('failed') or rows['input']['sha256']!=sha(failure) or
        rows['original_solver_invoked'] is not False or rows['statesChanged'] is not False or
        check['input']['sha256']!=sha(failure) or check['complete_rows']['sha256']!=sha(args.complete_rows) or
        candidate['input_failure']['sha256']!=sha(failure) or candidate['complete_rows']['sha256']!=sha(args.complete_rows) or
        candidate.get('candidate_only') is not True or candidate.get('solver_success') is not False or
        check['candidate']['sha256']!=sha(candidate_file) or check['original_solver_invoked'] is not False or
        check['full_candidate_replay_invoked'] is not False or
        check['locality_bound_viable'] is not True or candidate['locality_bound_viable'] is not True or
        not math.isfinite(check['candidateNormUpperBound']) or
        check.get('method')!='one_reverse_selected_flow_pass_v1' or
        candidate.get('method')!=check['method'] or check.get('passes')!=1 or
        not check['candidateNormUpperBound']<rows['before']['norm'] or
        sha(PROPOSER)!=PROPOSER_SHA or check['source_sha256'][str(PROPOSER)]!=PROPOSER_SHA):
        raise ValueError('A source-bound complete-row candidate with its original finite locality bound is required')
    for key in ('request','config','source_sha256'):
        if not exact_equal(candidate[key],original[key]):raise ValueError('Candidate changed '+key)
    old,cp=original['response']['checkpoint'],candidate['checkpoint']
    for key in ('parameters','rawNode','cutHeight'):
        if not exact_equal(cp[key],old[key]):raise ValueError('Candidate changed '+key)
    changes=candidate['named_changes']
    if not exact_equal(changes,check['named_changes']) or len(changes)!=len(rows['completeOverGateComponents']):
        raise ValueError('The complete declared component set differs')
    expected=[]
    impacted=sorted({n for row in rows['completeOverGateComponents'] for n in (row['stage']-1,row['stage'])},reverse=True)
    after_rows=check['afterImpactedRows']
    if (check['descending_stage_order']!=impacted or [r['stage'] for r in after_rows]!=impacted or
            len({r['stage'] for r in after_rows})!=len(impacted)):
        raise ValueError('The complete decreasing affected/upstream order differs')
    K=2*original['config']['modes']
    for after in after_rows:
        node=after['stage']
        before=next(r for r in rows['fullAffectedAndUpstreamRows'] if r['stage']==node)
        same_input=exact_equal(cp['states'][node+1],old['states'][node+1])
        if (after['inputNode']!=node+1 or after['originalSavedFlowReused'] is not same_input or
                len(after['flow'])!=K or len(after['residual'])!=K or
                not all(math.isfinite(float(v)) for v in after['flow']+after['residual']) or
                not exact_equal(after['normalizationScale'],before['components'][0]['normalizationScale'])):
            raise ValueError('The current whole original flow row or input identity differs')
        if same_input and not exact_equal(after['flow'],[r['flow'] for r in before['components']]):
            raise ValueError('A reused saved original flow differs')
        differences=[float(v)-float(cp['states'][node][j]) for j,v in enumerate(after['flow'])]
        if any(float(a)!=b for a,b in zip(after['residual'],differences)):
            raise ValueError('A saved current-row residual does not use the final candidate state')
        norm=max(abs(v)/after['normalizationScale'] for v in differences)
        if not exact_equal(norm,after['norm']):
            raise ValueError('A current row norm differs from its original normalization')
    bound=max(rows['otherComponentMaximum'],rows['before']['boundary']['cut'],rows['before']['boundary']['deep'],*(r['norm'] for r in after_rows))
    if not exact_equal(bound,check['candidateNormUpperBound']):
        raise ValueError('The complete locality upper bound differs')
    for change,row in zip(changes,rows['completeOverGateComponents']):
        node,j=change['node'],change['component']
        after=next(r for r in after_rows if r['stage']==node)
        if (not 0<node<len(old['states'])-1 or not 0<=j<K or
            (node,j)!=(row['stage'],row['component']) or
            row['normalizedResidual']<original['config']['solveTolerance'] or
            not exact_equal(change['before'],old['states'][node][j]) or
            not exact_equal(change['before'],row['state']) or
            not exact_equal(change['originalFlow'],row['flow']) or
            not exact_equal(change['after'],after['flow'][j]) or
            not exact_equal(change['currentFlow'],after['flow'][j]) or
            float(change['remainingToCurrentFlow'])!=0. or
            change['currentFlowInputWasOriginal'] is not after['originalSavedFlowReused']):
            raise ValueError('Each declared internal change must equal its current original flow')
        if not exact_equal(change['before'],change['after']):
            expected.append((node,j,change['before'],change['after']))
    found=[(i,j,a,b) for i,(left,right) in enumerate(zip(old['states'],cp['states']))
           for j,(a,b) in enumerate(zip(left,right)) if not exact_equal(a,b)]
    if (len(cp['states'])!=len(old['states']) or any(len(a)!=len(b) for a,b in zip(cp['states'],old['states'])) or
            not exact_equal(found,expected) or not exact_equal(cp['rawStates'],[cp['states'][i] for i in cp['rawNode']])):
        raise ValueError('The complete state differs outside the declared free components')
    sources=dict(check['source_sha256'])
    sparse=args.sparse_helper.resolve()
    for file in (Path(__file__).resolve(),TRANSFER/'recovering_tail_client_v2.py',sparse):sources[str(file)]=sha(file)
    for file,digest in sources.items():
        if sha(file)!=digest:raise ValueError('Executed source changed: '+file)
    cfg=copy.deepcopy(original['config'])
    if cfg.get('designInitialCheckpoint') or cfg.get('secantCheckpoint'):raise ValueError('No other initializer is allowed')
    cfg['initialCheckpoint']=str(candidate_file);cfg['traceFile']=str(files['worker'])
    changed=sorted(k for k in cfg.keys()|original['config'].keys() if not exact_equal(cfg.get(k),original['config'].get(k)))
    if set(changed)!={'initialCheckpoint','traceFile'} or cfg['solveTolerance']!=2e-9:
        raise ValueError('Only IO paths may change; the original 2e-9 gate is retained')
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER']=str(sparse)
    os.environ['VISIBLE_FLEX_SPARSE_PYTHON']=sys.executable
    write_new_json(files['config'],cfg)
    entry=dict(scope=__doc__,command=[sys.executable,*sys.argv],
        failure=dict(path=str(failure),sha256=sha(failure)),complete_rows=dict(path=str(args.complete_rows.resolve()),sha256=sha(args.complete_rows)),
        candidate=dict(path=str(candidate_file),sha256=sha(candidate_file)),candidate_summary=dict(path=str(args.candidate_summary.resolve()),sha256=sha(args.candidate_summary)),
        configuration=dict(path=str(files['config']),sha256=sha(files['config'])),configuration_changed_keys=changed,
        source_sha256=sources,named_changes=changes,original_gate=cfg['solveTolerance'],
        candidate_locality_upper_bound=check['candidateNormUpperBound'],new_request=original['request'],
        original_full_residual_still_required=True,node_heap_resource_only=args.node_heap)
    write_new_json(files['entry'],entry)
    spec=importlib.util.spec_from_file_location('complete_row_original_native_client',topic/'scripts/950f-tail-client-v3.py')
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    tail=None;began=time.monotonic();result=dict(scope=__doc__,entry=dict(path=str(files['entry']),sha256=sha(files['entry'])),
        solver_success=False,prefix_solver_invoked=False)
    try:
        tail=native.WeightedTailPort(files['config'],topic/'repro/source-root',prefix.with_name(prefix.name+'_tail'),node_heap=args.node_heap)
        if tail.sources!=original['source_sha256']:raise ValueError('Original native execution source differs')
        result['ready_parameter_metadata_transition']=validate_parameter_io_mapping(cp['parameters'],tail.ready['parameters'],original['config'],cfg)
        result['reload_arithmetic']=check_original_reload_boundary(candidate_file,old['cutHeight'],tail.cut['radius'])
        response=tail.solve(np.asarray(old['cutHeight'],float),jacobian=True,audit=True)
        J=np.asarray(response['heightJetJacobian'],float)
        if (response.get('converged') is not True or not math.isfinite(response['residual']) or
            not response['residual']<cfg['solveTolerance'] or J.size!=208 or not np.all(np.isfinite(J)) or response.get('audit') is None):
            raise ValueError('The original full stopping test/Jacobian/audit did not pass')
        result.update(solver_success=True,original_residual=response['residual'],finite_jacobian_entries=int(J.size),
            audit_returned=True,last_iteration=response['history'][-1]['iteration'],
            final_states_equal_candidate=exact_equal(response['checkpoint']['states'],cp['states']))
    except Exception as error:result['error']=repr(error)
    finally:
        if tail is not None:
            try:
                result['native_calls']=tail.calls
                file=tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
                if file.is_file():
                    saved=read_gzip(file)
                    if not exact_equal(saved['request'],original['request']) or not exact_equal(saved['config'],cfg):
                        raise AssertionError('The actual native request/config identity changed')
                    result['native_record']=dict(path=str(file),sha256=sha(file))
                    if saved['response'].get('lastIteration'):result['failed_last_iteration']=saved['response']['lastIteration']
            finally:tail.close()
            result['worker_returncode']=tail.proc.poll()
        for file,digest in sources.items():
            if sha(file)!=digest:raise AssertionError('Executed source changed: '+file)
        result['seconds']=time.monotonic()-began;write_new_json(files['summary'],result)
        print(json.dumps(result),flush=True)
    if not result['solver_success']:raise SystemExit(2)


if __name__=='__main__':main()
