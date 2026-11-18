#!/usr/bin/env python3
"""Read a completed fixed-stencil probe; never construct a core or call a solver.

Full 24-row tables and finite arrays remain in scratch. This collector checks
their identities and scalar arithmetic, retaining only envelopes, the two new
trace trends, the existing delta-FD comparison, and original execution status.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[4]
BASE = WORK/'m3_work/q060-circle-trace-parameter-jac-v1'
PLAN_SHA = 'e294ae4ab301897895fcc9d37ed6121f260c8ce4c9035040adc9906878f75d1f'
RESULT_SHA = 'e6db3def04940e35e31f612d9355453b7f5531e3ae74996df54bad0b0588aac2'
ARRAY_SHA = '323985a44a0d97e4bd5a61d0b703be08c75f818b0a44331dec89c1bfbb2e6aad'
RESOURCE_SHA = 'ee6eede57278a13634f5f075cc3a44f8096ffa3f20d5aefc365a83cf25864420'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def payload_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def binary_sha(value):
    return hashlib.sha256(np.asarray(value,dtype='float64').tobytes()).hexdigest()


def collect():
    for name,expected in [('launch-plan.json',PLAN_SHA),('diagnostic.json',RESULT_SHA),
                          ('diagnostic-arrays.npz',ARRAY_SHA),('resource.json',RESOURCE_SHA)]:
        if sha(BASE/name)!=expected:
            raise ValueError('Frozen probe output changed: '+name)
    plan=json.loads((BASE/'launch-plan.json').read_text())
    check=dict(plan);identity=check.pop('identity_sha256')
    if payload_sha(check)!=identity:raise ValueError('Plan payload changed')
    result=json.loads((BASE/'diagnostic.json').read_text())
    resource=json.loads((BASE/'resource.json').read_text())
    for path,expected in plan['source_sha256'].items():
        if sha(path)!=expected:raise ValueError('Bound source/input changed: '+path)
    for item in plan['inputs'].values():
        if sha(item['path'])!=item['sha256']:raise ValueError('Bound reference changed')
    if (resource['status']!='observed_terminal' or resource['child_returncode']!=0 or
        result['completed'] is not True or result['exit_status_requested']!=0 or
        result['plan_identity_sha256']!=identity or 'failure' in result):
        raise ValueError('The complete original probe terminal is required')
    if result['counters']!={'BVP_attempts':0,'tail_attempts':0,'original_fun_evaluations':50,
        'original_fun_jac_evaluations':1,'original_initial_evaluations':50}:
        raise ValueError('Unexpected original probe calls')
    rows=result['rows'];expected_order=[(j,e) for j in range(8) for e in (-20,-21,-22)]
    if [(r['parameter'],r['physical_step_exponent']) for r in rows]!=expected_order:
        raise ValueError('The predeclared complete stencil order changed')
    if not all(r['original_domains_passed'] is True for r in rows):
        raise ValueError('An original domain gate did not pass')
    events=[json.loads(line) for line in (BASE/'diagnostic-events.jsonl').read_text().splitlines()]
    if [(r['parameter'],r['exponent']) for r in events if r['event']=='fixed_stencil_completed']!=expected_order:
        raise ValueError('Event order differs from completed records')
    if any(r['event']=='diagnostic_failed' for r in events):raise ValueError('Unexpected failure event')
    with np.load(BASE/'diagnostic-arrays.npz',allow_pickle=False) as a:
        for name in a.files:
            if not np.all(np.isfinite(a[name])):raise ValueError('Nonfinite saved array: '+name)
        if binary_sha(a['selected_y'])!=plan['safe_initial']['selected_y_binary64_sha256']:
            raise ValueError('The original fixed state changed')
        if binary_sha(a['parameters'])!=plan['safe_initial']['p_binary64_sha256']:
            raise ValueError('The original parameter vector changed')
        scales=np.r_[1.,plan['safe_initial']['parameter_scales']]
        if binary_sha(a['physical_units'])!=binary_sha(scales):raise ValueError('Physical units changed')
        actual=a['parameter_jac_original']/scales[None,:,None]
        if actual.shape!=(25,8,10) or binary_sha(actual)!=binary_sha(a['parameter_jac_physical']):
            raise ValueError('Original Jacobian physical-column conversion differs')
        max_encoded_difference=0.
        for r in rows:
            j=r['parameter'];exponent=r['physical_step_exponent'];key=f'p{j}_e{abs(exponent)}'
            for which,analytic in [('fun',a['parameter_jac_physical'][:,j,:]),
                                   ('initial',a['initial_jac_physical'][:,j])]:
                plus,minus=a[key+'_'+which+'_plus'],a[key+'_'+which+'_minus']
                for version,denominator in [('nominal',2*r['physical_step']),
                                             ('encoded',r['encoded_physical_denominator'])]:
                    finite=(plus-minus)/denominator
                    saved=a[key+'_'+which+'_fd_'+version]
                    if binary_sha(finite)!=binary_sha(saved):
                        raise ValueError('Saved finite difference arithmetic differs')
                    diff=float(np.max(np.abs(finite-analytic)))
                    if diff!=r[which+'_'+version]['maximum_absolute_difference']:
                        raise ValueError('Saved maximum derivative difference differs')
                max_encoded_difference=max(max_encoded_difference,float(np.max(np.abs(
                    a[key+'_'+which+'_fd_nominal']-a[key+'_'+which+'_fd_encoded']))))
    envelopes=[]
    for e in (-20,-21,-22):
        control=[r for r in rows if r['parameter']>0 and r['physical_step_exponent']==e]
        kept=[r for r in control if r['parameter']<=5]
        delta=next(r for r in rows if r['parameter']==0 and r['physical_step_exponent']==e)
        worst=max(control,key=lambda r:r['fun_nominal']['mixed_scale_difference'])
        envelopes.append(dict(physical_step_exponent=e,physical_step=2.**e,
            core_control_fun_maximum_absolute=max(r['fun_nominal']['maximum_absolute_difference'] for r in control),
            core_control_fun_maximum_mixed=worst['fun_nominal']['mixed_scale_difference'],
            largest_mixed_control=worst['name'],
            retained_B2_B6_fun_maximum_mixed=max(r['fun_nominal']['mixed_scale_difference'] for r in kept),
            core_control_inlet_maximum_absolute=max(r['initial_nominal']['maximum_absolute_difference'] for r in control),
            existing_delta_FD_difference_absolute=delta['fun_nominal']['maximum_absolute_difference'],
            existing_delta_FD_difference_mixed=delta['fun_nominal']['mixed_scale_difference'],
            existing_delta_inlet_difference_absolute=delta['initial_nominal']['maximum_absolute_difference']))
    traces={}
    for j,name in [(6,'T'),(7,'U')]:
        selected=[r for r in rows if r['parameter']==j]
        traces[name]=dict(parameter=j,
            fun_absolute_differences=[r['fun_nominal']['maximum_absolute_difference'] for r in selected],
            finest_mixed_difference=selected[-1]['fun_nominal']['mixed_scale_difference'],
            finest_inlet_absolute_difference=selected[-1]['initial_nominal']['maximum_absolute_difference'])
    return dict(scope=__doc__,collector=ref(__file__),execution_plan=ref(BASE/'launch-plan.json'),
        original_probe_source=ref(HERE/'probe_q060_trace_parameter_jacobian.py'),
        published_entry_record=ref(HERE/'q060_trace_parameter_jacobian_entry.json'),
        original_outputs={name:ref(BASE/name) for name in ('diagnostic.json','diagnostic-arrays.npz',
            'diagnostic-events.jsonl','resource.json','stdout.log')},
        source_identity_scope='All 75 source/input hashes and 10 named refs from the frozen plan were rechecked; see that plan and the published entry record, without a duplicate map here.',
        tool_observation=dict(session_id=87257,launch_chunk='6c7062',completion_chunk='5914e0',
            observed_observer_exit_code=0,scope='These are actual session-tool observations; child status is independently stored in resource.json.'),
        resource_terminal=resource,diagnostic_started_utc=events[0]['utc'],
        original_probe_completed=result['completed'],completed_scope='All 24 fixed stencils executed; no new derivative acceptance threshold is implied.',
        counters=result['counters'],counters_scope=result['counters_scope'],
        baseline=result['baseline'],restored_baseline=result['restored_baseline'],
        three_layer_envelopes=envelopes,new_trace_columns=traces,
        largest_nominal_vs_actual_encoded_difference=max_encoded_difference,
        full_stencil_table=dict(output=ref(BASE/'diagnostic.json'),field='rows',rows=24,
            canonical_payload_sha256=payload_sha(rows),scope='Full reproducible table stays in scratch.'),
        interpretation='Finite differences support the implemented seven physical core columns and inlet scale chain at this one safe initial state. T is nonmonotone at the smallest scales; its numerical-error source was not separately isolated. The delta column is the existing finite difference, not an independent analytic derivative. No BVP Jacobian condition, failed-final-state derivative, continuous certificate, or solver success follows.',
        no_new_BVP=True,no_new_tail=True,no_final_state_reevaluation=True,
        no_mean_height_reconstruction=True,no_complete_metric=True,
        collector_evaluated_original_equations=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():raise FileExistsError('Do not overwrite a frozen compact record')
    out=collect()
    with args.out.open('x') as stream:json.dump(out,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(output=ref(args.out),completed_stencils=24,original_child_returncode=0,
                          new_numerical_equation_evaluations=0)),flush=True)


if __name__=='__main__':main()
