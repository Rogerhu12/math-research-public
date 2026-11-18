#!/usr/bin/env python3
"""Freeze completed prefix evidence of the running original native DN.

Only complete immutable batch records and copied log prefixes are bound.
This script does not evaluate a model or relabel an in-progress solve as
accepted. The separate final terminal must still pay original Jac/audit.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys


PLAN_SHA='7aadf15137197d201eb2e94a5344f201951675a1a159e554da12173cc09a3f1c'


def ref(p):
    p=Path(p).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def verify(item):
    if ref(item['path'])!=item:raise ValueError('Changed immutable binding: '+item['path'])
def load(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def number_hash(v):return hashlib.sha256(struct.pack('<'+'d'*len(v),*v)).hexdigest()
def snapshot(p,content):
    if p.exists():
        if p.read_bytes()!=content:raise ValueError('Snapshot already exists with other bytes')
    else:p.write_bytes(content)
    return ref(p)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args();w=a.workspace.resolve();b=w/'n4_work/native-dn-halfH-v1'
    plan=load(b/'plan.json')
    if ref(b/'plan.json')['sha256']!=PLAN_SHA:raise ValueError('Wrong original same-H plan')
    for item in plan['files'].values():verify(item)
    manifest=load(plan['files']['manifest']['path'])
    for item in [*manifest['owned_sources'],*manifest['native_files'].values(),*manifest['runtime_libraries']]:verify(item)
    old=load(plan['files']['input_checkpoint']['path']);cfg=load(plan['files']['config']['path'])
    changed=[key for key in sorted(set(cfg)|set(old['config'])) if cfg.get(key)!=old['config'].get(key)]
    if changed!=['initialCheckpoint','traceFile']:raise ValueError('Unexpected config edit')
    if plan['request']!={'height':old['response']['checkpoint']['cutHeight'],'jacobian':True,'audit':True}:
        raise ValueError('Original whole-H/Jac/audit request differs')
    if number_hash(plan['request']['height'])!=plan['height_sha256']:
        raise ValueError('Physical H byte identity differs')
    ready_path=b/'worker-ready.json';ready=load(ready_path)
    for key,value in old['response']['checkpoint']['parameters'].items():
        if key in ('initialCheckpoint','traceFile'):continue
        if ready['parameters'].get(key)!=value:raise ValueError('Original ready parameter differs: '+key)
    entry=load(plan['files']['entry_summary']['path'])
    first_path=b/'native-evaluates/0001-jac-record.json';first=load(first_path)
    original_batch=load(w/'n4_work/native-node-adapter-v1/actual-entry/0001-jac-record.json')
    for item in [first['input'],original_batch['input']]:verify(item)
    if Path(first['input']['path']).read_bytes()!=Path(original_batch['input']['path']).read_bytes():
        raise ValueError('Original warm/remesh/Dirichlet initialization changed a complete input')
    trace_path=Path(cfg['traceFile']);trace_lines=trace_path.read_bytes().splitlines(keepends=True)
    rows=[json.loads(line) for line in trace_lines]
    request=next(row for row in rows if row['event']=='request')
    if request['height']!=plan['request']['height'] or request['jacobian'] is not True or request['audit'] is not True:
        raise ValueError('The actual original worker request differs')
    # Bind the two completed fullJac iterations, without copying a growing log.
    points=[(i,row) for i,row in enumerate(rows) if row['event']=='iteration' and 'phase' not in row]
    if len(points)<2 or [row['iteration'] for _,row in points[:2]]!=[0,1]:
        raise ValueError('Original iterations0 and1 have not both completed')
    first_iter=points[0][1];next_iter=points[1][1]
    if first_iter['norm']!=entry['original_normalizedResidual']:
        raise ValueError('First original DN norm does not match complete entry')
    if not (next_iter['norm']<first_iter['norm'] and next_iter['norm']>=2e-9):
        raise ValueError('This entry records the observed strict decrease but not acceptance')
    trace_copy=snapshot(b/'entry-trace-prefix.jsonl',b''.join(trace_lines[:points[1][0]+1]))
    events_path=b/'native-evaluates/events.jsonl';event_lines=events_path.read_bytes().splitlines(keepends=True)
    events=[json.loads(line) for line in event_lines]
    terminal_rows=[(i,row) for i,row in enumerate(events) if row['event']=='batch_terminal' and row['call']<=8]
    if [row['call'] for _,row in terminal_rows]!=list(range(1,9)):
        raise ValueError('Expected exact original first eight completed evaluates')
    completed=[]
    for _,row in terminal_rows:
        verify(row['record']);rec=load(row['record']['path'])
        if rec['status']!='complete' or rec['returncode']!=0 or rec['signal'] is not None:
            raise ValueError('One original completed evaluate failed')
        if rec['withJac']!=(rec['call'] in (1,8)):
            raise ValueError('Original first accepted-step evaluation order differs')
        for key in ['input','output','stdout','stderr','static_metadata']:verify(rec[key])
        completed.append(dict(record=row['record'],input=rec['input'],output=rec['output'],
            call=rec['call'],withJac=rec['withJac'],returncode=rec['returncode'],
            process_wall_seconds=rec['process_wall_seconds']))
    event_copy=snapshot(b/'entry-native-events-prefix.jsonl',b''.join(event_lines[:terminal_rows[-1][0]+1]))
    accepted_state=load(b/'native-evaluates/0007-state-record.json')
    next_jac=load(b/'native-evaluates/0008-jac-record.json')
    left=bytearray(Path(accepted_state['input']['path']).read_bytes())
    right=bytearray(Path(next_jac['input']['path']).read_bytes())
    left[40:108]=right[40:108]
    if left!=right:raise ValueError('Accepted candidate and next Jacobian inputs differ beyond mode/token')
    live_bytes=(b/'resource-live.json').read_bytes();live=json.loads(live_bytes)
    live_copy=snapshot(b/'entry-resource-observation.json',live_bytes)
    if live['command']!=plan['command']:raise ValueError('Observer actual command differs')
    result=dict(scope=__doc__,source=ref(__file__),command=sys.argv,
        collected_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        files=plan['files'],plan=ref(b/'plan.json'),worker_ready=ref(ready_path),
        trace_prefix=trace_copy,native_events_prefix=event_copy,resource_observation=live_copy,
        actual_observer_command=plan['observer_command'],observer_session=35038,
        original_config_changed_keys=changed,same_H_sha256=plan['height_sha256'],
        same_original_complete_state_sha256=plan['full_original_state_sha256'],
        first_payload_byte_equal_to_successful_entry=True,first_payload=first['input'],
        original_entry_payload=original_batch['input'],
        original_ready_physical_and_numerical_parameters_equal=True,
        ready_parameter_identity_excludes_only_declared_runtime_paths=changed,
        prior_collector_only_path_check_failure=ref(b/'collector-entry-first-failure.json'),
        prior_collector_source=ref(b/'record_native_DN_entry_v0_failed.py'),
        observed_unique_request_count=1,jacobian_requested=True,audit_requested=True,
        numerical_options=plan['numerical_options'],projectionFloor=.05,
        completed_evaluate_prefix=completed,completed_fullJac=2,completed_scalar_trials=6,
        accepted_original_line_search_step=1/32,
        accepted_step_inference='Original source tries2^(-k), k=0..9. Calls2..7 are the six scalar candidates; call8 is the next fullJac. No other evaluation or manual state operation intervenes.',
        next_Jacobian_inputs_equal_accepted_scalar_inputs=True,
        initial_original_residual=first_iter['norm'],next_original_residual=next_iter['norm'],
        next_minA=next_iter['minA'],next_minD=next_iter['minD'],
        observed_original_iteration_number=1,original_residual_gate=2e-9,
        current_record_claims_final_acceptance=False,original_cutJets_audit_terminal_not_yet_claimed=True,
        continuation_scope='Same recorded .5H target only. No fullH, prefix match, exact arc or closed-family conclusion.',
        no_new_flow_by_collector=True,
        live_scope='The resource file is copied as an observation of the running command, not assigned a final-process identity. Later terminal is separate.')
    with a.out.open('x') as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(a.out),initial_residual=first_iter['norm'],next_residual=next_iter['norm'],
        accepted_original_step=1/32,read_only=True)),flush=True)


if __name__=='__main__':main()
