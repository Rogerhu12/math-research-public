#!/usr/bin/env python3
"""Read a closed failed run; no worker, numerical engine, or solver is imported."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

TOPIC=Path(__file__).resolve().parents[1]
REPO=TOPIC.parents[1]
P=TOPIC/'notes/2026-11-09-db6f-prefix-harmonic-s1-audited-target-01'
LAUNCH=TOPIC/'notes/2026-11-09-db6f-root-harmonic-s1-launch.json'
OBSERVED=TOPIC/'notes/2026-11-09-db6f-root-harmonic-s1-observed-execution.json'
IO={'initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile','trialStatePrefix'}
NAMES={'db6f-prefix-tail-continuation-client.py','db6f-prefix-tail-trial-worker.mjs',
 'db6f-prefix-tail-trial-core.mjs','db6f-prefix-tail-trial-split.mjs',
 '950f-tail-subdivision.mjs','950f-tail-warm-remesh.mjs',
 'closing_weighted_tail.mjs','closing_recalibrated_tail.mjs'}

def read(p):
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)

def canonical(v):
    return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False)

def same(a,b):
    return canonical(a)==canonical(b)

def path(p):
    p=Path(p)
    return p if p.is_absolute() else REPO/p

def identity(p):
    p=path(p).resolve(); b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def check(row):
    x=identity(row['path'])
    assert x['bytes']==row['bytes'] and x['sha256']==row['sha256']
    return x

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    assert not args.out.exists()
    launch,observed=read(LAUNCH),read(OBSERVED)
    assert identity(LAUNCH)['sha256']=='08e2ffc4aa3d73240962cc71315e3be3d941f3cde2c350d050106dd02b66c707'
    assert identity(OBSERVED)['sha256']=='88c823cbbc09b536da2bf3707445055de55c881e8c108274d5c3bde716e15c73'
    assert launch['source_binding_count']==98==len(launch['bound_files'])
    bound=[check(x) for x in launch['bound_files']]
    assert len({x['path'] for x in bound})==98
    outputs=[check(x) for x in observed['closed_output_files']]
    assert len(outputs)==6
    expected=[Path(str(P)+s) for s in ('-config.json','-reproduction.json','-run.log',
                                      '-summary.json','-trace.jsonl','_tail_0001.json.gz')]
    assert {x['path'] for x in outputs}=={str(p) for p in expected}
    assert same(launch['command'],observed['command'])
    assert observed['launch_path']==str(LAUNCH)
    assert observed['launch_sha256']==identity(LAUNCH)['sha256']
    assert observed['actual_child_exit_code']==2
    assert observed['child_exit_inferred_from_file_existence'] is False
    assert observed['root_outer_tool_exit_observed'] is True
    receipt=observed['root_tool_observation']
    assert receipt['session_id']==28395 and receipt['tool_result_chunk']=='75bf61'
    assert receipt['actual_tool_exit_code']==2 and receipt['observer'].endswith('/ root')
    assert receipt['observed_from']=='write_stdin final completion result'
    cfg,repro,summary,record=map(read,(expected[0],expected[1],expected[3],expected[5]))
    assert same(repro['command'],launch['command'])
    assert identity(path(repro['runner']['path']))==check(repro['runner'])
    assert repro['runner']['sha256']=='173d03b8c02107349275ad58509cd24d09963c6e26a09e17458507db1e20c7c5'
    for key in ('client','authority','input_binding','original_config','supplied_config',
                'target_prefix','initial_checkpoint','reference_layout','run_config'):
        check(repro[key])
    assert len(repro['authority_bindings'])==66
    for row in repro['authority_bindings']:
        check(row)
    old=read(path(repro['original_config']['path']))
    changed={k for k in set(cfg)|set(old)
             if k not in cfg or k not in old or not same(cfg[k],old[k])}
    assert changed==IO
    assert same({k:v for k,v in cfg.items() if k not in IO},
                {k:v for k,v in old.items() if k not in IO})
    assert cfg['maxIterations']==36 and cfg['solveTolerance']==2e-9
    assert 'projectionFloor' not in cfg and 'correctInitialBoundary' not in cfg
    target=read(path(repro['target_prefix']['path']))
    warm=read(path(repro['initial_checkpoint']['path']))
    goal=target['predicted_cut_height']
    assert warm['status']=='UNSOLVED_HARMONIC_WARM_ONLY'
    assert warm['actual_solver_runs']==0 and same(warm['checkpoint']['cutHeight'],goal)
    assert cfg['initialCheckpoint']==str(path(repro['initial_checkpoint']['path']))
    assert same(repro['request'],dict(height=goal,jacobian=True,audit=True))
    assert same(record['request'],repro['request']) and same(record['config'],cfg)
    assert set(record['source_sha256'])==NAMES
    assert same(record['source_sha256'],repro['source_sha256'])
    for name,digest in record['source_sha256'].items():
        assert identity(TOPIC/'scripts'/name)['sha256']==digest
    response=record['response']
    assert set(response)=={'failed','lastIteration','checkpoint'}
    assert response['failed']=='Error: momentum Newton line search failed'
    assert response['lastIteration'] is None and response['checkpoint'] is None
    assert identity(expected[5])['sha256']=='8205dcefb590623700d14dd111bbf0ef6f9cd6defb8e9802de2e12dbad090c8e'
    assert summary['status']=='SINGLE_TARGET_NOT_ACCEPTED_PREFIX_UNSOLVED'
    assert summary['actual_request_count']==1 and summary['actual_worker_exit_code']==0
    assert summary['intended_runner_exit_code']==2 and summary['validated_target_response'] is None
    assert summary['prefix_solved'] is False and summary['continuation02_completion_asserted'] is False
    assert summary['original_response_schema_modified'] is False
    assert summary['original_failed_text']==response['failed']
    assert summary['original_last_iteration'] is None
    assert summary['response_validation_error']['message']=='No complete original successful response schema'
    assert check(summary['actual_response'])==identity(expected[5])
    assert check(summary['config'])==identity(expected[0])
    assert check(summary['reproduction'])==identity(expected[1])
    log=read(expected[2])
    assert same(log,{k:summary[k] for k in log})
    trace=[json.loads(line) for line in expected[4].read_bytes().splitlines()]
    assert [x['event'] for x in trace]==['warm_initial_state','request','failure']
    assert trace[0]['source']==cfg['initialCheckpoint']
    assert trace[1]['call']==trace[2]['call']==1
    assert same(trace[1]['height'],goal) and trace[1]['jacobian'] is True and trace[1]['audit'] is True
    assert trace[2]['error']==response['failed']
    assert not Path(str(P)+'-iteration.json.gz').exists()
    assert not Path(str(P)+'-trials.jsonl').exists()
    assert not list(P.parent.glob(P.name+'-stage-input*'))
    for row in bound+outputs:
        check(row)
    result=dict(status='PASS-CLOSED-FAILED-SINGLE-TARGET-PROVENANCE-REVIEW',
        scope='Metadata and original error-path review only; no mathematical solver rerun.',
        producer=identity(__file__), launch=identity(LAUNCH), observed_execution=identity(OBSERVED),
        root_result_note=identity(TOPIC/'notes/2026-11-09-db6f-root-harmonic-s1-result.md'),
        bound_input_count=98, closed_output_count=6, bound_inputs=bound, closed_outputs=outputs,
        actual_root_tool_receipt=receipt, actual_child_exit_code=2,
        observed_worker_exit_code=0, elapsed_child_seconds=observed['elapsed_seconds'],
        runner_elapsed_seconds=summary['elapsed_seconds'], changed_config_keys=sorted(changed),
        true_request_goal_jacobian_audit=True, requested_audit_was_not_a_returned_audit=True,
        actual_response_keys=list(response), failed=response['failed'],
        actual_last_iteration=None, actual_checkpoint=None,
        trace_event_sequence=[x['event'] for x in trace], trace_iteration_count=0,
        no_new_shooting_checkpoint=True, specific_stage_or_RK_point_recorded=False,
        initial_norm_or_minA_recorded=False, mathematical_nonexistence_asserted=False,
        no_single_target_readiness=True, mathematical_solver_calls_by_reviewer=0,
        active_continuation_read_or_modified=False)
    args.out.write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ('status','bound_input_count','closed_output_count',
       'actual_child_exit_code','observed_worker_exit_code','trace_iteration_count',
       'mathematical_solver_calls_by_reviewer')}))

if __name__=='__main__':
    main()
