#!/usr/bin/env python3
"""Collect the completed first circle-trace coupled attempt without evaluating it.

The original solve_bvp raised inside RMS estimation before returning. Only its
initial raw state and actual DN anchor exist. Do not reconstruct a final cubic
from two logged parameter scalars, or label an observer exit zero as acceptance.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

PLAN_SHA='8b9de60b551deccd8ceb4bb2f88ee6f406b3b24e6abc35158f54ebeae0c54da4'
ERROR="FloatingPointError('Adaptive Frenet domain failure: -1.717530786436109e-06')"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def rows(path):return [json.loads(line) for line in Path(path).read_text().splitlines()]
def binary_sha(value):return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()

def collect(directory):
    directory=Path(directory).resolve();planfile=directory/'launch-plan.json'
    if sha(planfile)!=PLAN_SHA:raise ValueError('This collector is bound to the one executed plan')
    plan=load(planfile)
    for path,digest in plan['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('Frozen source/input changed: '+path)
    for item in plan['derived_source_files'].values():
        if sha(item['path'])!=item['sha256']:raise ValueError('Frozen function changed')
    terminal=load(directory/'runner-terminal.json');summary=load(directory/'seed-summary.json')
    resource=load(directory/'resource.json');events=rows(directory/'entry-events.jsonl')
    newton=rows(directory/'domain-newton.jsonl');worker=rows(directory/'tail-worker.jsonl')
    assert terminal['original_main_returned'] is True and terminal['original_solver_success'] is False
    assert terminal['original_error']==summary['error']==ERROR
    assert terminal['raw_inner_calls']==1 and terminal['actual_tail_calls']==0
    assert terminal['observed_worker_returncode']==0
    assert resource['status']=='observed_terminal' and resource['child_returncode']==0
    assert not list(directory.glob('inner-*-returned.json.gz'))
    assert not list(directory.glob('seed_tail_*.json.gz')) and not (directory/'seed.json.gz').exists()
    assert len(worker)==1 and worker[0]['event']=='warm_initial_state'
    started=next(r for r in events if r['event']=='entry_started')
    rebuilt=next(r for r in events if r['event']=='initializer_rebuilt')
    primed=next(r for r in events if r['event']=='original_actual_cache_primed')
    failure=next(r for r in events if r['event']=='inner_raised_before_return')
    assert failure['error']==ERROR and failure['inner']==0
    assert 'estimate_rms_residuals' in failure['traceback'] and 'f2 = fun(x2, y2, p)' in failure['traceback']
    assert primed['native_calls']==0
    ended=[r for r in newton if r['event']=='newton_end']
    assert len(ended)==1 and ended[0]['singular'] is False
    final_newton=ended[0]
    assert final_newton['stats']['accepted_steps']==9
    entryfile=directory/'inner-00-entry.json.gz';entry=load(entryfile)
    anchorfile=directory/'inner-00-entry-dn-anchor.json';anchor=load(anchorfile)
    assert np.asarray(entry['y']).shape==(25,271) and np.asarray(entry['p']).shape==(8,)
    assert entry['stage']=='before_original_solve_bvp' and entry['cubic_available'] is False
    for key,value in [('state_binary64_sha256',entry['y']),('parameter_binary64_sha256',entry['p'])]:
        assert binary_sha(value)==plan['initial_hashes'][key]==rebuilt[key]
    assert binary_sha(anchor['height'])==plan['initial_hashes']['full_H_binary64_sha256']
    assert anchor['raw']==ref(entryfile) and anchor['tail_native_calls']==0
    assert anchor['actual_tail_record']['sha256']==plan['starting_actual_anchor']['sha256']
    originals={name:ref(directory/name) for name in ['runner-terminal.json','seed-summary.json',
        'resource.json','resource-live.json','stdout.log','entry-events.jsonl','domain-newton.jsonl','tail-worker.jsonl',
        'inner-00-entry.json.gz','inner-00-entry-dn-anchor.json']}
    return dict(status='Failed before original solve_bvp returned; no new coupled state or tail solve',
        collector=ref(__file__),launch_plan=ref(planfile),source_sha256=plan['source_sha256'],
        derived_source_files=plan['derived_source_files'],original_records=originals,
        observed_execution=dict(tool_session=12897,start_chunk='0d336f',completion_chunk='5e626c',
            observed_tool_exit=0,observer_child_returncode=resource['child_returncode'],
            worker_returncode=terminal['observed_worker_returncode'],
            started_utc=started['time_utc'],terminal_utc=resource['observed_utc'],
            observer_seconds=resource['seconds'],runner_seconds=terminal['seconds']),
        new_design=dict(q=plan['design']['new_q'],modes=8,control_columns=plan['design']['new_columns'],
            core_settings=plan['design']['new_core_settings'],initial_frozen_profile=plan['design']['physical_profile'],
            new_initial_p0=0.,fixed_metric=False,warp_reference_q=.06),
        reconstructed_initial_hashes=plan['initial_hashes'],initial_states_shape=[25,271],
        initial_physical_controls=rebuilt['physical_controls'],initial_parameter_scales=rebuilt['parameter_scales'],
        exact_original_same_H_actual_anchor=plan['starting_actual_anchor'],
        original_solve_bvp_invoked=True,original_solve_bvp_returned=False,
        original_newton_returned=True,original_newton_final_logged_scalars=final_newton,
        last_newton_scalar_scope='Only p0 and p1 were logged. They do not recover the remaining parameters, node values, cubic, or any final physical core.',
        failure=dict(error=ERROR,inner=0,time_utc=failure['time_utc'],
            stage='SciPy estimate_rms_residuals: original RHS at its second extra Lobatto point x2',
            negative_frenet_margin=-1.717530786436109e-6,
            traceback=failure['traceback'],
            classification='Original Frenet-domain rejection before RMS completion and before any BVP return; not max-nodes, post-prefix/seam audit, or a new tail failure.'),
        recovery=dict(entry_state=ref(entryfile),entry_actual_DN_anchor=ref(anchorfile),
            raw_returned_state_available=False,raw_returned_cubic_available=False,
            complete_last_parameters_available=False,final_metric_available=False,physical_checkpoint_available=False),
        new_actual_tail_requests=0,new_actual_tail_acceptances=0,
        solver_success=False,full_metric_computed=False,
        limits='An actual tool/observer exit zero records normal exception handling, not BVP acceptance. No failed inner was replayed, and no numerical state or final control vector was invented.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir',type=Path,required=True);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=collect(args.run_dir)
    with args.out.open('x') as stream:json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(args.out),solver_success=False,original_solve_bvp_returned=False,new_tail_calls=0)))

if __name__=='__main__':main()
