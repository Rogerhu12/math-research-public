#!/usr/bin/env python3
"""Read the completed single five-point-domain attempt; no solver evaluation.

All 28 completed raw snapshots and their actual DN references are checked.
The BVP returned max-nodes with a full cubic. The later physical audit failed
inside height_integral, leaving a failed pre-audit physical checkpoint.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np

PLAN_SHA='da2c3d945ac45fcb04dc456c7e00283fb1c8b9bdbe4d2fe5fb5d3c8687c2374b'
ERROR="FloatingPointError('Adaptive Frenet domain failure: -8.824213515445933e-08')"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def load(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw)
def rows(path):return [json.loads(line) for line in Path(path).read_text().splitlines()]
def bits(value):return np.asarray(value,dtype='float64').tobytes()
def binary_sha(value):return hashlib.sha256(bits(value)).hexdigest()

def collect(directory):
    directory=Path(directory).resolve();planfile=directory/'lobatto-launch-plan.json'
    assert sha(planfile)==PLAN_SHA
    plan=load(planfile)
    for path,digest in plan['source_sha256'].items():assert sha(path)==digest,path
    for item in [*plan['derived_source_files'].values(),plan['lobatto_guard']['recording_newton_source']]:
        assert sha(item['path'])==item['sha256']
    events=rows(directory/'entry-events.jsonl');trace=rows(directory/'domain-newton.jsonl')
    resource=load(directory/'resource.json');terminal=load(directory/'runner-terminal.json')
    summary=load(directory/'seed-summary.json');cpfile=directory/'seed.json.gz';cp=load(cpfile)
    assert resource['status']=='observed_terminal' and resource['child_returncode']==0
    assert terminal['original_main_returned'] is True and terminal['observed_worker_returncode']==0
    assert terminal['original_error']==summary['error']==ERROR
    assert terminal['raw_inner_calls']==1 and terminal['actual_tail_calls']==0
    assert cp['solver_success'] is False and cp['nodes']==2431
    assert 'summary' not in cp and 'tail_seam' not in cp
    assert not list(directory.glob('seed_tail_*.json.gz'))
    worker=rows(directory/'tail-worker.jsonl')
    assert len(worker)==1 and worker[0]['event']=='warm_initial_state'
    saved=[row for row in events if row['event']=='raw_inner_saved'];assert len(saved)==28
    stages=Counter();manifest=[];mesh_returns=[];last=None
    for event in saved:
        file=Path(event['raw']['path']);side=Path(event['dn_anchor']['path'])
        assert ref(file)==event['raw'] and ref(side)==event['dn_anchor']
        raw=load(file);anchor=load(side);stages[raw['stage']]+=1
        assert anchor['raw']==ref(file)
        assert anchor['actual_tail_record']['sha256']==plan['starting_actual_anchor']['sha256']
        assert anchor['height_binary64_sha256']==plan['initial_hashes']['full_H_binary64_sha256']
        assert anchor['tail_native_calls']==0
        x=np.asarray(raw['x'],float);y=np.asarray(raw['y'],float);p=np.asarray(raw['p'],float)
        assert y.shape==(25,len(x)) and p.shape==(8,) and np.all(np.diff(x)>0)
        assert np.all(np.isfinite(y)) and np.all(np.isfinite(p))
        controls=p[1:]*np.asarray(raw['parameter_scales'],float)
        for key in ('physical_controls','original_physical_controls'):
            if key in raw:assert bits(controls)==bits(raw[key])
        cubic_shape=None
        if raw['cubic_available']:
            cubic=raw['raw_cubic'];c=np.asarray(cubic['c'],float)
            assert c.shape==(4,len(x)-1,25) and cubic['axis']==1
            assert bits(cubic['x'])==bits(x) and np.all(np.isfinite(c))
            assert bits(c[3])==bits(y[:,:-1].T)
            if raw.get('node_rhs') is not None:
                ff=np.asarray(raw['node_rhs'],float);assert ff.shape==y.shape and np.all(np.isfinite(ff))
                assert bits(c[2])==bits(ff[:,:-1].T)
            cubic_shape=list(c.shape)
        item=dict(raw=ref(file),actual_anchor_sidecar=ref(side),stage=raw['stage'],nodes=len(x),
            inner=raw['inner'],prepared_system=raw.get('prepared_system'),
            newton_call=raw.get('newton_call'),newton_iteration=raw.get('newton_iteration'),
            y_binary64_sha256=binary_sha(y),p_binary64_sha256=binary_sha(p),
            cubic_shape=cubic_shape)
        manifest.append(item)
        if raw['stage']=='ordinary_return':mesh_returns.append(item)
        if raw['stage']=='immediately_after_original_solve_bvp':last=raw
    assert stages==dict(before_original_solve_bvp=1,before_initial_evaluation=3,
        initial_domain_pass=3,accepted_assignment=17,ordinary_return=3,immediately_after_original_solve_bvp=1)
    assert [row['nodes'] for row in mesh_returns]==[271,811,2431]
    assert last['solver_success'] is False and last['status']==1 and last['niter']==3
    assert last['message']=='The maximum number of mesh nodes is exceeded.'
    assert bits(last['p'])==bits(cp['parameters'])
    assert bits(last['original_physical_controls'])==bits(cp['physical_controls'])
    maximum_rms=max(last['rms_residuals']);assert maximum_rms==cp['max_rms_collocation_residual']
    assert maximum_rms==1.3860615692460996
    chunks=[]
    for item in cp['pp_coefficient_chunks']:
        file=directory/item['file'];assert sha(file)==item['sha256']
        coefficient=np.load(io.BytesIO(gzip.decompress(file.read_bytes())),allow_pickle=False)
        assert coefficient.shape==(6,2430,item['state_last_exclusive']-item['state_first'])
        assert np.all(np.isfinite(coefficient))
        chunks.append(dict(**ref(file),shape=list(coefficient.shape),state_first=item['state_first'],state_last_exclusive=item['state_last_exclusive']))
    failure=next(row for row in events if row['event']=='original_main_exception')
    assert failure['error']==ERROR and 'height_integral' in failure['traceback'] and 'adaptive.audit' in failure['traceback']
    extra=[row for row in events if row['event']=='extra_RMS_point_domain_rejection'];assert len(extra)==32
    ends=[row for row in trace if row['event']=='newton_end'];assert len(ends)==3
    stats=ends[-1]['stats'];assert stats['accepted_steps']==17 and stats['rejected_domain_trials']==238
    assert stats['rejected_merit_trials']==4 and stats['no_step']==2
    ordinary=[row for row in events if row['event']=='initializer_rebuilt'];assert len(ordinary)==1
    for key,value in plan['initial_hashes'].items():assert ordinary[0][key]==value
    records={name:ref(directory/name)for name in ['resource.json','resource-live.json','runner-terminal.json',
        'seed-summary.json','stdout.log','entry-events.jsonl','domain-newton.jsonl','tail-worker.jsonl']}
    return dict(status='Original BVP returned max-nodes; later physical prefix mean-height audit failed; no coupled acceptance',
        collector=ref(__file__),launch_plan=ref(planfile),source_sha256=plan['source_sha256'],
        lobatto_guard=plan['lobatto_guard'],original_records=records,
        observed_execution=dict(tool_session=82557,start_chunk='5cda97',completion_chunk='ae3122',
            observed_tool_exit=0,observer_child_returncode=0,worker_returncode=0,
            started_utc=next(row for row in events if row['event']=='entry_started')['time_utc'],
            terminal_utc=resource['observed_utc'],seconds=resource['seconds']),
        observation_incident='One read-only exec request reported exec-server transport disconnected. The existing session subsequently remained running and read access recovered; no run or source was restarted and no memory-failure claim is made.',
        initial_hashes=plan['initial_hashes'],starting_actual_tail_anchor=plan['starting_actual_anchor'],
        original_solve_bvp_returned=True,BVP_solver_success=False,status_code=last['status'],message=last['message'],
        nodes=2431,newton_meshes=[271,811,2431],original_scipy_iterations=3,
        maximum_original_RMS=maximum_rms,newton_stats=stats,extra_original_RMS_point_domain_rejections=32,
        snapshot_counts=dict(stages),all_raw_snapshots=manifest,
        raw_returned=ref(directory/'inner-00-returned.json.gz'),raw_returned_anchor=ref(directory/'inner-00-returned-dn-anchor.json'),
        raw_returned_cubic_shape=[4,2430,25],full_final_parameters=last['p'],
        original_parameter_scales=last['parameter_scales'],full_final_physical_controls=last['original_physical_controls'],
        candidate_H_not_sent_to_actual_tail=last['candidate_cut_height'],
        failed_physical_checkpoint=ref(cpfile),failed_physical_coefficient_chunks=chunks,
        failed_physical_core_kind=cp['core_kind'],failed_physical_profile=cp['frozen_profile'],
        failed_physical_meridian_length=cp['meridian_length'],
        later_failure=dict(error=ERROR,stage='After the failed physical C2 checkpoint was saved: adaptive.audit -> height_integral -> original frame',
            finite_sampling='Original six-point per-span mean-height integration at audit angular count 512',
            negative_frenet_margin=-8.824213515445933e-8,traceback=failure['traceback']),
        new_actual_tail_requests=0,new_actual_tail_acceptances=0,full_metric_available=False,
        limitations='The five-point check covers the original finite RMS locations, not all later physical/angle samples or a continuous domain. Raw Newton and returned states are recovery material, not accepted BVPs. Saved failed physical CP is not an anchor for production closure. No original inner has been replayed.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir',type=Path,required=True);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=collect(args.run_dir)
    with args.out.open('x')as stream:json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(args.out),BVP_solver_success=False,nodes=result['nodes'],RMS=result['maximum_original_RMS'],snapshots=len(result['all_raw_snapshots']))))

if __name__=='__main__':main()
