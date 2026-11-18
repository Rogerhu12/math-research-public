#!/usr/bin/env python3
"""Collect the original lambda=.02 inner success and subsequent actual-tail failure.

Read saved states and original records only. Do not evaluate a core, residual,
Jacobian, mean integral, BVP or tail. Full raw arrays and event lists remain in
scratch; this record keeps their hashes and the exact recovery boundary.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[4]/'m3_work/q060-circle-trace-path-coupled-lam002-v1'
PLAN_SHA='99b888b421ecaea72dbbafffca9811121ed8d663c62049c3ce03e54edc6b52be'
TAIL_SHA='6f0cdfa7bdc27c330bd3320ba94417e1fb410430dfdcdd3bd685c2944d2411ac'
RETURN_SHA='bc2fee7117ba8d8d842ac3352290ce55e966813ebf8048494688ce6d46180cc0'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def rows(path):return [json.loads(line) for line in Path(path).read_text().splitlines()]
def bits(x):return np.asarray(x,dtype='float64').tobytes()
def payload_sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def collect():
    planfile=BASE/'launch-plan.json';assert sha(planfile)==PLAN_SHA
    plan=load(planfile);check=dict(plan);identity=check.pop('identity_sha256')
    assert payload_sha(check)==identity
    for path,digest in plan['source_sha256'].items():assert sha(path)==digest,path
    for item in plan['derived_source_files'].values():assert sha(item['path'])==item['sha256']
    for key in ('initial_plan','completed_initializer','completed_initializer_terminal','initial_arrays','profile','tail_config'):
        item=plan[key];assert sha(item['path'])==item['sha256']
    resource=load(BASE/'resource.json');terminal=load(BASE/'runner-terminal.json');summary=load(BASE/'seed-summary.json')
    assert resource['status']=='observed_terminal' and resource['child_returncode']==0
    assert terminal['original_main_returned'] is True and terminal['observed_worker_returncode']==0
    assert terminal['raw_inner_calls']==terminal['actual_tail_calls']==1
    assert summary['solver_success'] is False and summary['tail_calls']==1
    assert terminal['original_error']==summary['error']
    assert not (BASE/'seed.json.gz').exists()
    tailfile=BASE/'seed_tail_0001.json.gz';assert sha(tailfile)==TAIL_SHA
    assert sorted(p.name for p in BASE.glob('seed_tail_*.json.gz'))==[tailfile.name]
    tail=load(tailfile);cfg=load(plan['tail_config']['path']);response=tail['response']
    assert tail['config']==cfg and tail['source_sha256']==plan['native_tail_source_sha256']
    assert tail['request']['jacobian'] is True and tail['request']['audit'] is True
    assert isinstance(response['failed'],str) and not response.get('converged',False)
    assert response['lastIteration']['norm']==3.667862901158431e-9
    assert cfg['solveTolerance']==2e-9 and response['lastIteration']['norm']>=cfg['solveTolerance']
    cp=response['checkpoint'];states=np.asarray(cp['states'],float)
    assert states.ndim==2 and states.shape[1]==16 and np.all(np.isfinite(states))
    assert bits(cp['cutHeight'])==bits(tail['request']['height'])
    events=rows(BASE/'entry-events.jsonl');trace=rows(BASE/'domain-newton.jsonl')
    saved=[r for r in events if r['event']=='raw_inner_saved'];counts=Counter();manifest=[];meshes=[]
    for event in saved:
        file=Path(event['raw']['path']);side=Path(event['dn_anchor']['path'])
        assert ref(file)==event['raw'] and ref(side)==event['dn_anchor']
        raw=load(file);anchor=load(side);counts[raw['stage']]+=1
        assert anchor['raw']==ref(file)
        assert anchor['actual_tail_record']['sha256']==plan['starting_actual_anchor']['sha256']
        assert anchor['tail_native_calls']==0
        assert raw['core_kind']=='exact_m3_finite_circle_trace_path_partial_lift'
        assert raw['core_control_path']=='finite-cosine-trace-synchronous-lift-v1'
        assert raw['path_lambda']==.02 and raw['q_gauge']==.06
        assert raw['seed_support_amplitude']==.059818741459951905 and raw['lift_window']==[.5,.9]
        assert raw['path_base_profile']==plan['design']['physical_profile']
        x=np.asarray(raw['x']);y=np.asarray(raw['y']);p=np.asarray(raw['p'])
        assert y.shape==(25,len(x)) and p.shape==(8,) and np.all(np.diff(x)>0)
        assert np.all(np.isfinite(y)) and np.all(np.isfinite(p))
        controls=p[1:]*np.asarray(raw['parameter_scales'])
        for key in ('physical_controls','original_physical_controls'):
            if key in raw:assert bits(raw[key])==bits(controls)
        if raw['cubic_available']:
            cubic=raw['raw_cubic'];c=np.asarray(cubic['c'])
            assert c.shape==(4,len(x)-1,25) and cubic['axis']==1 and bits(cubic['x'])==bits(x)
            assert np.all(np.isfinite(c)) and bits(c[3])==bits(y[:,:-1].T)
            if raw.get('node_rhs') is not None:assert bits(c[2])==bits(np.asarray(raw['node_rhs'])[:,:-1].T)
        if raw['stage']=='ordinary_return':meshes.append(len(x))
        manifest.append(dict(raw=ref(file),anchor=ref(side),stage=raw['stage'],nodes=len(x)))
    lastfile=BASE/'inner-00-returned.json.gz';assert sha(lastfile)==RETURN_SHA
    last=load(lastfile)
    assert last['solver_success'] is True and last['status']==0 and last['niter']==5
    assert len(last['x'])==493 and max(last['rms_residuals'])==9.873637694422844e-7
    assert bits(last['candidate_cut_height'])==bits(tail['request']['height'])
    assert bits(last['candidate_cut_height'])!=bits(plan['starting_actual_anchor']['full_H'])
    endings=[r for r in trace if r['event']=='newton_end'];assert len(endings)==5
    stats=endings[-1]['stats']
    assert stats['accepted_steps']==7 and stats['rejected_domain_trials']==stats['rejected_merit_trials']==0
    assert stats['minimum_alpha']==1. and stats['no_step']==0
    assert counts==dict(before_original_solve_bvp=1,before_initial_evaluation=5,
        initial_domain_pass=5,accepted_assignment=7,ordinary_return=5,immediately_after_original_solve_bvp=1)
    assert not [r for r in events if r['event']=='extra_RMS_point_domain_rejection']
    loaded=next(r for r in events if r['event']=='stored_initializer_loaded')
    for key,value in plan['initial_hashes'].items():assert loaded[key]==value
    failure=next(r for r in events if r['event']=='original_main_exception')
    assert failure['error']==summary['error'] and 'solve_with_actual_tail' in failure['traceback']
    worker=rows(BASE/'tail-worker.jsonl')
    assert len([r for r in worker if r['event']=='request'])==1
    records={name:ref(BASE/name) for name in ('resource.json','runner-terminal.json','seed-summary.json',
        'entry-events.jsonl','domain-newton.jsonl','tail-worker.jsonl','stdout.log')}
    return dict(status='Original inner BVP accepted; subsequent changed-H actual tail failed its original line search; no coupled or metric acceptance',
        collector=ref(__file__),launch_plan=ref(planfile),entry_record=ref(HERE/'q060_trace_path_coupled_entry.json'),
        sources_rechecked=len(plan['source_sha256']),original_records=records,
        observed_execution=dict(tool_session=94553,launch_chunk='67ca61',completion_chunk='38def1',
            observer_exit_code=0,child_returncode=0,worker_returncode=0,
            started_utc=events[0]['time_utc'],terminal_utc=resource['observed_utc'],seconds=resource['seconds']),
        initial_hashes=plan['initial_hashes'],design=plan['design'],
        raw_returned=ref(lastfile),raw_returned_actual_anchor=ref(BASE/'inner-00-returned-dn-anchor.json'),
        original_solve_bvp_returned=True,inner_solver_success=True,inner_status=last['status'],
        inner_message=last['message'],nodes=len(last['x']),raw_cubic_shape=[4,492,25],
        maximum_original_RMS=max(last['rms_residuals']),mesh_nodes=meshes,newton_stats=stats,
        raw_snapshot_count=len(saved),snapshot_counts=dict(counts),snapshot_manifest_payload_sha256=payload_sha(manifest),
        snapshot_manifest_scope='Every listed raw/anchor hash and complete saved finite array checked; full event list remains in the bound entry-events.jsonl, without a duplicate Git table.',
        full_final_parameters=last['p'],parameter_scales=last['parameter_scales'],
        full_final_physical_controls=last['original_physical_controls'],
        new_H_sent_to_actual_tail=last['candidate_cut_height'],
        starting_actual_tail_anchor=plan['starting_actual_anchor'],
        failed_actual_tail=dict(record=ref(tailfile),request_jacobian=True,request_audit=True,
            original_gate=cfg['solveTolerance'],last_iteration=response['lastIteration'],
            failure=response['failed'],finite_state_shape=list(states.shape),
            source_scope='The full failed native checkpoint is preserved; it is not an accepted response or complete returned audit.'),
        original_main_error=summary['error'],original_failure_traceback=failure['traceback'],
        actual_tail_requests=1,new_actual_tail_acceptances=0,physical_checkpoint_saved=False,
        mean_height_reconstructed=False,full_metric_available=False,
        recovery_boundary='Resume after the preserved accepted inner0, with a genuinely accepted actual response at its exact new H; do not rerun the completed inner. Original outer/BC/mean/metric gates remain necessary.',
        collector_evaluated_equations=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=collect()
    with args.out.open('x') as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=ref(args.out),inner_success=True,coupled_success=False,
        raw_snapshots=result['raw_snapshot_count'],new_equation_evaluations=0)),flush=True)


if __name__=='__main__':main()
