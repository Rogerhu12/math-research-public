#!/usr/bin/env python3
"""Collect the completed unique finite-path entry, with no equation evaluation.

The complete finite arrays remain in scratch. Lambda-zero equality is a
literal-source/full-polynomial identity plus seven sampled represented jets;
lambda=.02 completed its original finite initial diagnostics, not a BVP.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[4]/'m3_work/q060-circle-trace-path-entry-v1'
HASHES={
    'launch-plan.json':'945259b830d5d4a129cbe86068a6f72a2940f5cba2265224584cc8ac192a785f',
    'entry.json':'7e39adda827887d715188f0ef263136316e8dcaa7d286abe13c44c5ee1fa0444',
    'entry-arrays.npz':'1f882f0004ad58817b60245a363a9e773322b8bc8620179d36f9b6ce16a5e142',
    'resource.json':'106f3e6045ba8e4c1b5563d35ecc78e04f0d2a46f4b2448144aed027852f4c03'}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ref(path):return dict(path=str(Path(path).resolve()),sha256=sha(path))
def binary_sha(a):return hashlib.sha256(np.asarray(a,dtype='float64').tobytes()).hexdigest()
def payload_sha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def collect():
    for name,digest in HASHES.items():
        if sha(BASE/name)!=digest:raise ValueError('Frozen entry output changed: '+name)
    plan=json.loads((BASE/'launch-plan.json').read_text())
    result=json.loads((BASE/'entry.json').read_text())
    resource=json.loads((BASE/'resource.json').read_text())
    check=dict(plan);identity=check.pop('identity_sha256')
    if payload_sha(check)!=identity or result['plan_identity_sha256']!=identity:
        raise ValueError('Entry plan identity changed')
    for path,digest in plan['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('Bound source/input changed: '+path)
    for item in [*plan['inputs'].values(),*plan['derived_source_files'].values()]:
        if sha(item['path'])!=item['sha256']:raise ValueError('Bound entry reference changed')
    if (not result['complete'] or result['exit_status_requested']!=0 or 'failure' in result or
        resource['status']!='observed_terminal' or resource['child_returncode']!=0):
        raise ValueError('The actual complete entry terminal is required')
    if result['counters']!={'BVP_attempts':0,'native_tail_attempts':0}:
        raise ValueError('The planned entry attempted an unrequested solver')
    if not result['native_reference_constructed']:
        raise ValueError('The actual native-reference construction was not recorded')
    zero=result['lambda_zero_identity'];first=result['formed_first_entry']
    diag=result['original_entry_diagnostics']
    if (first['lambda_value']!=.02 or first['path_definition']['numerical_gauge']!=.06 or
        first['path_definition']['defining_support_amplitude']!=.059818741459951905 or
        not diag['original_domains_passed'] or not zero['core_class_literal_original']):
        raise ValueError('The declared first path model changed')
    with np.load(BASE/'entry-arrays.npz',allow_pickle=False) as a:
        for key in a.files:
            if not np.all(np.isfinite(a[key])):raise ValueError('Nonfinite saved array: '+key)
        for name in plan['lambda0_identity']['jets']:
            old,new=a['lambda0_original_'+name],a['lambda0_new_'+name]
            if old.shape!=(10,256,3) or binary_sha(old)!=binary_sha(new):
                raise ValueError('Lambda-zero represented identity differs: '+name)
            if zero['represented_jet_checks'][name]['maximum_absolute_difference']!=0:
                raise ValueError('The saved zero-difference summary changed')
        for key,field in [('initial_y','state_binary64_sha256'),
                          ('initial_p','parameter_binary64_sha256'),
                          ('initial_H','full_H_binary64_sha256')]:
            if binary_sha(a[key])!=first[field]:raise ValueError('Initial array identity differs')
        if a['initial_y'].shape!=(25,271) or a['initial_cubic'].shape!=(4,270,25):
            raise ValueError('Incomplete original finite initializer arrays')
        if binary_sha(a['initial_H'])!=binary_sha(a['original_H_anchor']):
            raise ValueError('Actual full-H encoding differs')
        physical=a['initial_p'][1:]*np.asarray(plan['original_parameter_scales'])
        if binary_sha(physical)!=binary_sha(plan['complete_original_controls']):
            raise ValueError('One of the original seven physical controls changed')
        for name,key in [('initial_rms','maximum_original_collocation_RMS'),
                         ('collocation_residual','maximum_collocation_residual'),
                         ('initial_BC_affine_only','maximum_original_BC_affine_only')]:
            if float(np.max(abs(a[name])))!=diag[key]:raise ValueError('Stored diagnostic maximum differs')
    events=[json.loads(line) for line in (BASE/'entry-events.jsonl').read_text().splitlines()]
    if [r['event'] for r in events]!=['entry_started','lambda_zero_identity_completed',
        'first_nonzero_entry_formed','entry_diagnostic_completed','entry_record_saved']:
        raise ValueError('Unexpected actual execution sequence')
    return dict(scope=__doc__,collector=ref(__file__),plan=ref(BASE/'launch-plan.json'),
        published_entry_record=ref(HERE/'q060_trace_path_entry_record.json'),
        source_identity_scope=dict(source_inputs_rechecked=len(plan['source_sha256']),
            named_inputs_rechecked=len(plan['inputs']),derived_excerpts_rechecked=len(plan['derived_source_files'])),
        outputs={name:ref(BASE/name) for name in ('entry.json','entry-arrays.npz','entry-events.jsonl','resource.json','stdout.log')},
        tool_observation=dict(session_id=5281,launch_chunk='c8d676',completion_chunk='b8aea6',
            observed_observer_exit_code=0,scope='Actual tool observations; independently recorded child status is in resource.json.'),
        started_utc=events[0]['utc'],resource_terminal=resource,
        entry_complete=True,complete_scope='The two declared model checks completed; no BVP or full-metric acceptance is asserted.',
        native_reference_constructed_in_this_run=True,counters=result['counters'],
        lambda_zero_identity=zero,first_entry=first,original_entry_diagnostics=diag,
        numerical_scope='All finite values retain their original binary64 evaluation. Core and frame numerical guards are not interval certificates.',
        no_BVP=True,no_actual_tail=True,no_mean_height_reconstruction=True,no_complete_metric=True,
        no_endpoint_lambda_one_evaluation=True,collector_evaluated_equations=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Do not overwrite a frozen compact record')
    result=collect()
    with args.out.open('x') as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=ref(args.out),complete=True,original_child_returncode=0,new_equation_evaluations=0)),flush=True)


if __name__=='__main__':main()
