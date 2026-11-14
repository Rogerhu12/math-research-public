#!/usr/bin/env python3
"""Optimize the complete core gap in the actual current M32 geometry model.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All nineteen current fields, all five geometric row families and complete
row replay are retained. The first core coordinate is a bounded variable;
the amplitude constraint/objective is G=2 sum(c_m: m=2 mod4), using all32
actual core coordinates and all nine current response columns. Weighted
complete-core tail bounds remain design proxies, not inlet error bounds.
No accepted state, continuous geometric certificate or new BVP is produced.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import ast
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import types
import numpy as np

HERE=Path(__file__).resolve().parent
PINS={
    'root_geometry_anchor_current_reader.py':'b69abdc1f615a9d96b65fb187f2e87831bf975f5b2752303db4c10c37f9c3b84',
    'root_geometry_anchor_current_interfaces.py':'8da06d8c7909b55e56bef75e92dceec8e1dd3226b208a80896fa2ce7aaaa0b48',
    'root_geometry_minimax_initial_laws_controls.py':'ccdcc95d3e7dd2a1447714578e6976179f1b5c32d3495e13a074399872c31e57',
    'root_geometry_minimax_control_constraints.py':'7d5f91ca193ef9d6c02070b5c062f278ab29a01f070eb12b66c8c9dff701cc63',
    'root_fine_core_tail_proxy_eight_sync_trust.py':'9af5df6752ccf7865fc180c22d50e5ee1aaca40de1fd2e430041f61a4ac01c9e',
}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)
def binary(value):return F.from_float(float(value))
def rat(value):value=F(value);return dict(numerator=str(value.numerator),denominator=str(value.denominator))
def gap(core):return 2*sum((binary(c) for c in core[::2]),F(0))


def transformed_module(name,edits):
    source=original=(HERE/name).read_text()
    for before,after in edits:
        if source.count(before)!=1:raise ValueError('A unique frozen source edit changed: '+before)
        source=source.replace(before,after,1)
    ast.parse(source)
    reverse=source
    for before,after in reversed(edits):
        if reverse.count(after)!=1:raise ValueError('A source edit is not uniquely reversible')
        reverse=reverse.replace(after,before,1)
    if reverse!=original:raise ValueError('Unlisted frozen algorithm changes')
    module=types.ModuleType('current_gap_'+Path(name).stem)
    module.__file__=str(HERE/name)
    exec(compile(source,'<current-full-gap-'+name+'>','exec'),module.__dict__)
    provenance=dict(original_source=name,original_sha256=sha(HERE/name),
        transformed_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_original_source=True,edits=[dict(before=b,after=a) for b,a in edits])
    return module,provenance


def prepare_modules():
    for name,want in PINS.items():
        if sha(HERE/name)!=want:raise ValueError('A frozen complete-field source changed: '+name)
    kernel,kernel_provenance=transformed_module('root_geometry_minimax_control_constraints.py',[
        ("    bounds = [(q1_step, q1_step)]+[(-trust, trust)]*(controls-1)+[(0., None)]",
         "    bounds = [(-trust, trust)]*controls+[(0., None)]")])
    algorithm,algorithm_provenance=transformed_module('root_geometry_minimax_initial_laws_controls.py',[
        ("    ap.add_argument('--q1-factors',type=float,nargs='+',default=[.5,1.,2.])",
         "    ap.add_argument('--gap-increments',dest='q1_factors',type=float,nargs='+',required=True)"),
        ("                normalized_bounds=[(qstep,qstep)]+[(-args.trust_factor,args.trust_factor)]*(controls-1)",
         "                normalized_bounds=[CURRENT_Q1_NORMALIZED_RANGE]+[(-args.trust_factor,args.trust_factor)]*(controls-1)"),
        ("                result.update(fixed_q1_factor=qstep,size_factor=factor,size_cap=cap,",
         "                result.update(minimum_complete_gap_increment=qstep,size_factor=factor,size_cap=cap,"),
        ("print(json.dumps({key:result.get(key) for key in ('fixed_q1_factor','size_factor','success',",
         "print(json.dumps({key:result.get(key) for key in ('minimum_complete_gap_increment','size_factor','success',")])
    return kernel,algorithm,dict(kernel=kernel_provenance,driver=algorithm_provenance)


def main():
    p=argparse.ArgumentParser(add_help=False,description=__doc__)
    p.add_argument('--prepare-source-only',type=Path)
    p.add_argument('--plan',type=Path)
    p.add_argument('--out',type=Path)
    p.add_argument('--bridge-out',type=Path)
    p.add_argument('--goal',choices=('minimum-curvature','maximum-gap'),default='minimum-curvature')
    p.add_argument('--q1-increment-range',type=float,nargs=2,default=[0.,.032])
    p.add_argument('--curvature-size-cap',type=float)
    p.add_argument('--core-tail-factor',default='2')
    p.add_argument('--core-tail-frequencies',type=int,nargs='+',default=[16,24,32,40,48])
    a,rest=p.parse_known_args()
    kernel,algorithm,preparation=prepare_modules()
    if a.prepare_source_only:
        if a.prepare_source_only.exists():raise FileExistsError(a.prepare_source_only)
        a.prepare_source_only.parent.mkdir(parents=True,exist_ok=True)
        a.prepare_source_only.write_text(json.dumps(dict(schema='current-M32-complete-gap-tail-source-preparation-v1',
            author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
            pinned_sources=PINS,source_transformations=preparation,source_only=True,
            no_future_accepted_response_or_fields_created=True,
            unchanged_original_complete_row_generation_and_replay=True,
            mathematical_additions=['bounded free first core coordinate','full32-mode gap lower constraint',
                'optional full32-mode gap objective under explicit curvature-size cap',
                'same original positive core-tail auxiliary rows and final complete-tail replay'],
            no_new_ODE_Node_Jacobian_or_field=True),indent=2)+'\n')
        print(json.dumps(dict(prepared=str(a.prepare_source_only),sha256=sha(a.prepare_source_only),new_ODE_or_fields=0)),flush=True)
        return
    if not all((a.plan,a.out,a.bridge_out)) or a.out.exists() or a.bridge_out.exists():
        raise ValueError('Require a complete actual plan and fresh result/reader paths')
    if not np.isfinite(a.q1_increment_range).all() or a.q1_increment_range[0]>a.q1_increment_range[1]:
        raise ValueError('An explicit ordered finite physical q1 increment interval is required')
    if a.goal=='maximum-gap' and a.curvature_size_cap is None:
        raise ValueError('The maximum-gap objective needs an explicit curvature-times-size design cap')
    if a.curvature_size_cap is not None and (not math.isfinite(a.curvature_size_cap) or a.curvature_size_cap<=0):
        raise ValueError('Use a positive finite curvature-size design cap')
    factor=F(a.core_tail_factor)
    if not 1<=factor<=64:raise ValueError('Explicit positive baseline tail multiplier in [1,64] required')
    if a.core_tail_frequencies!=sorted(set(a.core_tail_frequencies)) or any(k<8 or k>64 or k%2 for k in a.core_tail_frequencies):
        raise ValueError('Distinct ordered nonempty actual even-frequency tails required')
    import root_geometry_anchor_current_reader as bridge
    from root_geometry_anchor_current_interfaces import CONTROL_NAMES,require_response
    from root_fine_core_tail_proxy_eight_sync_trust import make_tail_solver
    plan,bridge_record,checked_loader=bridge.verify(a.plan,a.bridge_out)
    rows={r['name']:r for r in plan['candidates']}
    baseline=read(rows['baseline']['report'])
    response=read(bridge_record['response_file']);require_response(response)
    directions=plan['directions']
    if tuple(r['name'] for r in directions)!=CONTROL_NAMES:raise ValueError('The current nine-control ordering changed')
    core=np.asarray(baseline['actual_core'],dtype=np.float64)
    accepted=read(baseline['actual_reference'])
    if (accepted['core']['frequencies']!=list(range(2,65,2)) or
            np.asarray(accepted['core']['coefficients'],dtype=np.float64).tobytes()!=core.tobytes()):
        raise ValueError('The full-gap functional requires these exact physical even modes')
    if core.shape!=(32,) or core.tobytes()!=np.asarray(response['baseline']['core'],dtype=np.float64).tobytes():
        raise ValueError('The complete accepted current core differs from the actual response')
    base_command=rows['baseline']['command']
    tail_path=Path(base_command[base_command.index('--actual-reference-tail')+1])
    tail=read(tail_path)
    current_tail_floor=float(tail['response']['audit']['formalCurvature'])
    if not tail['response']['converged'] or not math.isfinite(current_tail_floor) or current_tail_floor<=0:
        raise ValueError('Require the actual current accepted tail curvature sample')
    response_rows={r['direction']:r for r in response['prescribed_low_core_responses']}
    response_rows.update({r['external_field']:r for r in response['additional_core_held_directions']})
    physical_derivatives=np.column_stack([response_rows[r['name']]['core_derivative'] for r in directions])
    steps=np.asarray([r['step'] for r in directions])
    slopes=physical_derivatives*steps[None,:]
    exact_gap_gradient=[2*sum((binary(steps[j])*binary(physical_derivatives[i,j]) for i in range(0,32,2)),F(0)) for j in range(9)]
    numerical_gap_gradient=np.array([float(v) for v in exact_gap_gradient])
    gradient_scale=max(abs(numerical_gap_gradient))
    if not np.isfinite(slopes).all() or not math.isfinite(gradient_scale) or gradient_scale<=0:
        raise ValueError('Require the complete finite nonzero gap response')
    frequencies=2*np.arange(1,33)
    exact_tails={k:sum(((int(m)**2-1)*abs(binary(c)) for c,m in zip(core,frequencies) if m>=k),F(0)) for k in a.core_tail_frequencies}
    if any(v<=0 for v in exact_tails.values()):raise ValueError('Every declared baseline tail must be positive')
    budgets={k:float(factor*v) for k,v in exact_tails.items()}
    tail_solve=make_tail_solver(kernel,core,slopes,frequencies,budgets)
    def solve(base,changes,size_cap,minimum_gap_increment,*positional,**kwargs):
        if a.curvature_size_cap is not None and current_tail_floor>a.curvature_size_cap/size_cap:
            return dict(success=False,status=2,history=[],all_finite_rows_checked=False,
                message='The explicitly retained current tail sample already exceeds this conservative size-cap budget.',
                current_tail_floor=current_tail_floor,requested_curvature_cap=a.curvature_size_cap/size_cap,
                exact_physical_impossibility_claimed=False)
        original_lp=kernel.linprog;extra_calls=[]
        def gap_lp(objective,A_ub,b_ub,bounds,method,options):
            n=len(objective)
            if n<10 or len(bounds)!=n:raise ValueError('All current controls and original curvature variable must remain')
            gaprow=np.zeros(n);gaprow[:9]=-numerical_gap_gradient/gradient_scale
            matrix=np.vstack((A_ub,gaprow));rhs=np.r_[b_ub,-minimum_gap_increment/gradient_scale]
            box=list(bounds)
            box[9]=(max(box[9][0],current_tail_floor),box[9][1])
            if a.curvature_size_cap is not None:
                cap=a.curvature_size_cap/size_cap
                box[9]=(box[9][0],cap if box[9][1] is None else min(box[9][1],cap))
            objective=np.asarray(objective,dtype=np.float64).copy()
            if a.goal=='maximum-gap':objective[:]=0.;objective[:9]=-numerical_gap_gradient/gradient_scale
            fitted=original_lp(objective,A_ub=matrix,b_ub=rhs,bounds=box,method=method,options=options)
            item=dict(goal=a.goal,full_gap_row=True,minimum_gap_increment=minimum_gap_increment,
                current_accepted_tail_sample_floor=current_tail_floor,
                curvature_cap=(a.curvature_size_cap/size_cap if a.curvature_size_cap is not None else None),
                complete_augmented_rows=len(rhs),success=bool(fitted.success))
            if fitted.success:item['max_augmented_float_row_violation']=float(np.max(matrix@fitted.x-rhs))
            extra_calls.append(item);return fitted
        kernel.linprog=gap_lp
        try:result=tail_solve(base,changes,size_cap,minimum_gap_increment,*positional,**kwargs)
        finally:kernel.linprog=original_lp
        result['full_core_gap_design']=dict(goal=a.goal,minimum_complete_gap_increment=minimum_gap_increment,
            current_axis_gap_exact_binary=rat(gap(core)),all_32_modes_used=True,
            actual_full_gap_LP_calls=extra_calls,first_coordinate_is_bounded_variable=True,
            q1_increment_interval=a.q1_increment_range,curvature_times_size_cap=a.curvature_size_cap)
        if a.goal=='maximum-gap' and 'optimized_curvature_cap' in result:
            result['feasible_curvature_cap_from_gap_LP']=result.pop('optimized_curvature_cap')
        return result
    algorithm.CURRENT_Q1_NORMALIZED_RANGE=tuple(v/steps[0] for v in a.q1_increment_range)
    algorithm.load_field=checked_loader
    algorithm.solve_minimax=solve
    original_argv=sys.argv
    sys.argv=[original_argv[0],'--plan',str(a.plan),'--out',str(a.out),*rest]
    try:algorithm.main()
    finally:sys.argv=original_argv
    output=read(a.out)
    output['scope']=__doc__
    for row in output['predictions']:
        if not row.get('success'):continue
        predicted=core+np.asarray(row['predicted_complete_core_increment'])
        final_gap=gap(predicted);increment=final_gap-gap(core)
        requested=binary(row['minimum_complete_gap_increment'])
        tolerance=F(1,10**9)
        if increment+ tolerance<requested:
            raise ArithmeticError('The original complete predicted core fails its explicit gap design replay')
        tail_checks=[]
        for k in a.core_tail_frequencies:
            value=sum(((int(m)**2-1)*abs(binary(c)) for c,m in zip(predicted,frequencies) if m>=k),F(0))
            budget=factor*exact_tails[k]
            if value>budget*(1+F(1,50_000_000)):
                raise ArithmeticError('Original complete predicted core fails its weighted-tail design replay')
            tail_checks.append(dict(minimum_physical_frequency=k,exact_predicted_binary_tail=rat(value),exact_budget=rat(budget),display_ratio=float(value/budget)))
        if not binary(a.q1_increment_range[0])<=binary(row['physical_steps']['actual_q1'])<=binary(a.q1_increment_range[1]):
            raise ArithmeticError('The actual physical first coordinate escaped its declared interval')
        if row['finite_rows']!=bridge_record['full_finite_row_count'] or not row['all_finite_rows_checked']:
            raise ArithmeticError('Every original current geometric row must be replayed')
        profile=dict(baseline['warm_profile'])
        for key,value in row['predicted_profile_increment'].items():profile[key]=profile.get(key,0.)+value
        p0=baseline['warm_profile']
        sync_ok=all(math.isfinite(profile[k]) for k in ('vd','loop_speed','descending_sync_curvature')) and abs(profile['vd'])<1 and abs(profile['loop_speed'])<1 and profile['descending_sync_curvature']>0
        sync_length=(abs(math.asin(profile['loop_speed'])-math.asin(profile['vd']))/(.92*profile['descending_sync_curvature']) if sync_ok else None)
        baseline_sync=abs(math.asin(p0['loop_speed'])-math.asin(p0['vd']))/(.92*p0['descending_sync_curvature'])
        row['full_core_gap_design'].update(final_original_complete_core=predicted.tolist(),
            exact_binary_final_gap=rat(final_gap),exact_binary_final_gap_increment=rat(increment),
            final_gap_display=float(final_gap),final_gap_increment_display=float(increment),
            exact_binary_gap_replay_absolute_tolerance=rat(tolerance),
            final_original_complete_tail_replay=tail_checks,
            gap_over_actual_predicted_size=float(final_gap)/row['predicted_max_twice_norm'],
            predicted_sync_profile_domain=sync_ok,predicted_sync_length=sync_length,
            original_sync_length=baseline_sync,predicted_sync_length_ratio=(sync_length/baseline_sync if sync_ok else None),
            sync_formula_is_design_diagnostic_not_nonlinear_domain_certificate=True)
    output['actual_anchor_current_geometry_bridge']=dict(path=str(a.bridge_out),sha256=sha(a.bridge_out),
        source_sha256=PINS['root_geometry_anchor_current_reader.py'],all_identity_gates=True,
        gate_count=bridge_record['gate_count'],controls=list(CONTROL_NAMES),
        current_M32_fields_only=True,old_coarse_or_stale_derivative_fields_used=False)
    output['current_complete_core_gap_tail_adapter']=dict(source_sha256=sha(__file__),pinned_sources=PINS,
        source_transformations=preparation,goal=a.goal,complete_core_modes=32,
        physical_gap_derivative=[float(2*sum((binary(physical_derivatives[i,j]) for i in range(0,32,2)),F(0))) for j in range(9)],
        normalized_gap_gradient_exact_binary=[rat(v) for v in exact_gap_gradient],
        complete_normalized_core_slopes=slopes.tolist(),complete_physical_frequencies=frequencies.tolist(),
        baseline_exact_gap=rat(gap(core)),baseline_exact_weighted_tails={str(k):rat(v) for k,v in exact_tails.items()},
        tail_factor=str(factor),q1_physical_increment_interval=a.q1_increment_range,
        current_complete_response_sha256=sha(bridge_record['response_file']),
        current_tail_sample_floor=dict(path=str(tail_path),sha256=sha(tail_path),value=current_tail_floor,
            explicitly_retained_in_LP_curvature_variable=True,new_target_tail_bound=False),
        current_complete_field_bridge_sha256=sha(a.bridge_out),original_five_row_families_retained=True,
        gap_is_full_core_design_proxy_not_closed_surface_Hausdorff=True,
        tail_proxy_does_not_certify_inlet_or_new_BVP=True,
        exact_arithmetic_replays_saved_binary_predictions_only=True,
        new_ODE_Node_Jacobian_or_geometry_field=False)
    temporary=a.out.with_name(a.out.name+'.complete-gap.tmp')
    temporary.write_text(json.dumps(output,indent=2)+'\n');temporary.replace(a.out)
    print(json.dumps(dict(event='actual_current_full_gap_tail_model_finished',out=str(a.out),sha256=sha(a.out),
        predictions=len(output['predictions']),successful=sum(bool(row.get('success')) for row in output['predictions']))),flush=True)


if __name__=='__main__':main()
