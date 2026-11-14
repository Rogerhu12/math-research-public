#!/usr/bin/env python3
"""Retain every current geometry row and bound complete predicted core tails.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Fresh frontload-trust design successor; only the frontload interval becomes [-.04,.04].
The sync interval [-.004,+.001] is retained; no nonlinear domain is certified by the box.
Fresh actual-eight adapter of parent source a4982368cd86d09fc542ec64d4e7dd43c292cd2b6861aeca20b3f1f058176cf6.
Adapted from geometry_audit original tail-proxy algorithm. All geometric rows
still refer to the actual coarse17 fields; only the tail design proxy is
centred at the accepted fine32 core. Coarse directions are padded with zero
increment in its four extra modes. No fine Jacobian or new solution is claimed.
Each explicit physical-frequency tail sum (m*m-1)*abs(c_m) has its own budget.
Positive auxiliary variables encode the absolute values in every actual LP.
This is a floating design proxy, not an inlet-error or nonlinear certificate.
The entry binds the completed q122 thirteen-plus-four fields and explicit
assembled eight-response identity. Original six combined-half vectors remain
unavailable; no direct combined-half gate or fine-Jacobian claim is added.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
from fractions import Fraction as F
import hashlib
import gzip
import json
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
PINS={
 'root_geometry_eight_actual_reader_bridge.py':'841e98e4156b3c42c72b3aeeb6da917676452f6f22e57bf149f4c26b718ff8c7',
 'root_geometry_minimax_initial_laws_controls.py':'ccdcc95d3e7dd2a1447714578e6976179f1b5c32d3495e13a074399872c31e57',
 'root_geometry_minimax_control_constraints.py':'7d5f91ca193ef9d6c02070b5c062f278ab29a01f070eb12b66c8c9dff701cc63',
}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def rat(q):q=F(q);return {'numerator':str(q.numerator),'denominator':str(q.denominator)}


def make_tail_solver(base_algorithm,core,slopes,frequencies,budgets):
    """Append exact algebraic absolute-value rows to each finite LP.

    The original solver, all five geometric row families, row generation,
    complete-field replay and control intervals remain intact. Only the
    call to linprog is augmented. The auxiliary solution is removed before
    the original code reads its unchanged control-plus-curvature vector.
    """
    core=np.asarray(core,dtype=np.float64)
    slopes=np.asarray(slopes,dtype=np.float64)
    frequencies=np.asarray(frequencies,dtype=np.int64)
    if (core.ndim!=1 or slopes.ndim!=2 or slopes.shape[0]!=len(core) or
        frequencies.shape!=core.shape or not np.isfinite(core).all() or
        not np.isfinite(slopes).all() or not np.all(frequencies>=2)):
        raise ValueError('A complete finite core and every current direction are required')
    cutoffs=sorted(budgets)
    if not cutoffs or any(not np.isfinite(budgets[k]) or budgets[k]<=0 for k in cutoffs):
        raise ValueError('Explicit positive tail budgets required')
    ix=np.flatnonzero(frequencies>=cutoffs[0])
    if not len(ix) or any(not np.any(frequencies>=k) for k in cutoffs):
        raise ValueError('Every declared physical-frequency tail must be nonempty')
    weights=(frequencies[ix].astype(np.float64)**2-1)
    scale=max(budgets.values())
    # z_m >= (m^2-1)|c_m|/scale, hence each tail is a positive sum.
    C=weights*core[ix]/scale
    A=weights[:,None]*slopes[ix,:]/scale
    original_solve=base_algorithm.solve_minimax

    def solve(*args,**kwargs):
        original_lp=base_algorithm.linprog
        lp_calls=[]
        def augmented_lp(objective,A_ub,b_ub,bounds,method,options):
            controls=slopes.shape[1];nold=controls+1;extra=len(ix)
            objective=np.asarray(objective,dtype=np.float64)
            if len(objective)!=nold or A_ub.shape[1]!=nold or len(bounds)!=nold:
                raise ValueError('The complete original control and curvature columns changed')
            old=np.column_stack((A_ub,np.zeros((len(A_ub),extra))))
            pos=np.column_stack((A,np.zeros(extra),-np.eye(extra)))
            neg=np.column_stack((-A,np.zeros(extra),-np.eye(extra)))
            tails=np.array([[float(m>=k) for m in frequencies[ix]] for k in cutoffs])
            tailrows=np.column_stack((np.zeros((len(cutoffs),nold)),tails))
            matrix=np.vstack((old,pos,neg,tailrows))
            rhs=np.r_[b_ub,-C,C,[budgets[k]/scale for k in cutoffs]]
            fitted=original_lp(np.r_[objective,np.zeros(extra)],A_ub=matrix,b_ub=rhs,
                bounds=[*bounds,*[(0.,None)]*extra],method=method,options=options)
            record=dict(original_geometry_rows=len(A_ub),absolute_value_rows=2*extra,
                tail_budget_rows=len(cutoffs),auxiliary_count=extra,success=bool(fitted.success))
            if fitted.success:
                extended=np.asarray(fitted.x).copy()
                record.update(max_complete_augmented_float_row_violation=float(np.max(matrix@extended-rhs)),
                    auxiliary_values=extended[nold:].tolist())
                fitted.x=extended[:nold]
            else:record.update(status=int(fitted.status),message=str(fitted.message))
            lp_calls.append(record)
            return fitted
        base_algorithm.linprog=augmented_lp
        try:result=original_solve(*args,**kwargs)
        finally:base_algorithm.linprog=original_lp
        tailcheck=[]
        if result.get('success'):
            x=np.asarray(result['normalized_steps']);predicted=core+slopes@x
            for k in cutoffs:
                chosen=frequencies>=k
                value=float(np.sum((frequencies[chosen]**2-1)*abs(predicted[chosen])))
                ratio=value/budgets[k]
                if not np.isfinite(ratio) or ratio>1+2e-8:
                    raise ArithmeticError('Complete predicted tail failed explicit floating replay')
                tailcheck.append(dict(minimum_physical_frequency=k,budget=budgets[k],
                    complete_predicted_tail=value,ratio=ratio,all_modes_in_tail_replayed=True))
            result['predicted_complete_core_for_tail_proxy']=predicted.tolist()
        result['core_tail_design_proxy']=dict(frequencies=frequencies.tolist(),
            weight='m*m-1 at actual physical frequency m',absolute_value_LP_auxiliaries=True,
            budgets={str(k):v for k,v in budgets.items()},normalization_scale=scale,
            actual_LP_calls=lp_calls,complete_tail_replay=tailcheck,
            all_original_geometric_rows_retained=True,
            floating_replay_relative_tolerance=2e-8,
            inlet_metric_or_nonlinear_remainder_certified=False)
        return result
    return solve


def main():
    p=argparse.ArgumentParser(add_help=False,description=__doc__)
    p.add_argument('--plan',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bridge-out',type=Path,required=True)
    p.add_argument('--core-tail-factor',type=str,required=True)
    for key in ('fine-accepted','fine-resource','fine-readback','fine-readback-resource'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--core-tail-frequencies',nargs='+',type=int,default=[16,24,32,40,48])
    a,rest=p.parse_known_args()
    if a.out.exists() or a.bridge_out.exists():raise FileExistsError('Fresh tail-proxy output paths required')
    required_ranges={'start_acceleration':(-.064,0.),'initial_speed_frontload':(-.04,.04),'vd':(-.004,.001)}
    observed_ranges={}
    for index,word in enumerate(rest):
        if word=='--control-range':
            name,lo,hi=rest[index+1:index+4]
            if name in observed_ranges:raise ValueError('Duplicate physical control range')
            observed_ranges[name]=(float(lo),float(hi))
    if observed_ranges!=required_ranges:
        raise ValueError('Require the explicit reviewed k0/frontload/vd physical increment box')
    factor=F(a.core_tail_factor)
    if factor<1 or factor>64:raise ValueError('Explicit baseline tail factor must be in [1,64]')
    if a.core_tail_frequencies!=sorted(set(a.core_tail_frequencies)) or any(k<8 or k%2 for k in a.core_tail_frequencies):
        raise ValueError('Distinct increasing actual even physical-frequency cutoffs required')
    for name,want in PINS.items():
        if sha(HERE/name)!=want:raise ValueError('Frozen actual minimax source changed: '+name)
    plan=read(a.plan);rows={z['name']:z for z in plan['candidates']};names=[z['name'] for z in plan['directions']]
    baseline=read(rows['baseline']['report']);coarse_core=np.asarray(baseline['actual_core'],dtype=np.float64)
    response_path=Path(plan['assembled_response_file']);response=read(response_path)
    if (sha(response_path)!='5c83df392bb2e9ed75b767e0ed90fc85bfb83ae545945acb4177d200891937c0'
        or names!=['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature','start_acceleration','initial_speed_frontload','vd']):
        raise ValueError('Require the actual assembled eight response and all eight exact control names')
    if (not baseline['finished'] or baseline['nonlinear_solution'] or len(coarse_core)!=plan['modes'] or
        not response['partial_recovery'] or response['modes']!=plan['modes']):
        raise ValueError('This entry requires the actual q122 partial-recovery eight-control baseline and directions')
    columns={r['direction']:r for r in response['prescribed_low_core_responses']}
    columns.update({r['external_field']:r for r in response['additional_core_held_directions']})
    coarse_slopes=np.column_stack([d['step']*np.asarray(columns[d['name']]['core_derivative']) for d in plan['directions']])
    fine,fr,zero,zr=map(read,(a.fine_accepted,a.fine_resource,a.fine_readback,a.fine_readback_resource))
    if (sha(a.fine_accepted)!='4c0e13b2ea4e2541e75891a3b4fafa93ffc2f8331cfdcdc7e4083ac3cbfef1ad'
        or sha(a.fine_readback)!='e1a67e518ae311e493bd87595a2a1cfc56860cdde3cd81904fa1cb651d83f676'
        or not fine['solver_success'] or fine['audit_pending'] or fine['modes']!=32
        or fr['exitcode']!=0 or fr.get('termination_signal') is not None
        or zr['exitcode']!=0 or zr.get('termination_signal') is not None
        or not zero['original_both_full_H_J_and_audits_verified']
        or zero['fine_original_owned_exitcode']!=0
        or not zero['original_material_chart_and_physical_metric_identical']
        or not zero['added_fine_channels_have_zero_increment_only']
        or zero['fine_control_derivative_claim']):
        raise ValueError('The actual accepted fine baseline and real two-baseline readback are required')
    core=np.asarray(fine['core']['coefficients'],dtype=np.float64)
    if (len(core)!=32 or fine['core']['frequencies']!=list(range(2,65,2))
        or not np.array_equal(core,np.asarray(zero['fine_baseline_complete_core'],dtype=np.float64))
        or not np.array_equal(coarse_core,np.asarray(zero['coarse_baseline_complete_core'],dtype=np.float64))
        or coarse_slopes.shape!=(28,8)):
        raise ValueError('Complete original core identities or actual eight directions changed')
    slopes=np.zeros((32,8),dtype=np.float64);slopes[:28]=coarse_slopes
    frequencies=2*np.arange(1,len(core)+1)
    exact={k:sum((F.from_float(abs(float(c)))*(int(m)**2-1)
                       for c,m in zip(core,frequencies) if m>=k),F(0)) for k in a.core_tail_frequencies}
    if any(v<=0 for v in exact.values()):raise ValueError('This baseline requires positive explicitly declared tails')
    budgets={k:float(factor*v) for k,v in exact.items()}
    import root_geometry_minimax_control_constraints as kernel
    import root_geometry_minimax_initial_laws_controls as algorithm
    import root_geometry_eight_actual_reader_bridge as bridge
    old=algorithm.solve_minimax
    algorithm.solve_minimax=make_tail_solver(kernel,core,slopes,frequencies,budgets)
    argv=sys.argv;sys.argv=[argv[0],'--plan',str(a.plan),'--out',str(a.out),'--bridge-out',str(a.bridge_out),*rest]
    try:bridge.main()
    finally:algorithm.solve_minimax=old;sys.argv=argv
    output=read(a.out)
    # Read the original complete-core prediction too, preserving its actual
    # floating addition order rather than silently changing either array.
    for row in output['predictions']:
        if not row.get('success'):continue
        increment=np.asarray(row['predicted_complete_core_increment'])
        if increment.shape!=(28,):raise ValueError('Original complete coarse increment changed')
        original_prediction=core+np.r_[increment,np.zeros(4)]
        row['fine_complete_core_tail_proxy_prediction']=original_prediction.tolist()
        row['coarse_geometry_prediction_kept_as_design_reference']=True
        alternate=np.asarray(row['predicted_complete_core_for_tail_proxy'])
        row['core_tail_design_proxy']['original_prediction_addition_order_max_difference']=float(np.max(abs(original_prediction-alternate)))
        final=[]
        for k in a.core_tail_frequencies:
            value=sum((F.from_float(abs(float(c)))*(int(m)**2-1)
                       for c,m in zip(original_prediction,frequencies) if m>=k),F(0))
            ratio=float(value/(factor*exact[k]))
            if value>factor*exact[k]*(1+F(1,50_000_000)):
                raise ArithmeticError('Original final predicted core violates the declared exact rational tail proxy and original tolerance')
            final.append(dict(minimum_physical_frequency=k,exact_binary_core_tail=rat(value),
                exact_baseline_factor_budget=rat(factor*exact[k]),display_ratio=ratio))
        row['core_tail_design_proxy']['final_original_prediction_exact_rational_replay']=final
    for row in output['predictions']:
        if not row.get('success'):continue
        for name,(lo,hi) in required_ranges.items():
            step=float(row['physical_steps'][name])
            if not F.from_float(lo)<=F.from_float(step)<=F.from_float(hi):
                raise ArithmeticError('Final physical control escaped its explicit binary-float interval: '+name)
        if row['finite_rows']!=14_453_760 or not row['all_finite_rows_checked']:
            raise ArithmeticError('The complete original five geometric families were not replayed')
        row['explicit_physical_box_exact_binary_replay']=True
    output['reviewed_extra_physical_control_ranges']=required_ranges
    output['full_core_tail_proxy_adapter']=dict(source_sha256=sha(__file__),original_sources=PINS,
        response_path=str(response_path),response_sha256=sha(response_path),baseline_report=rows['baseline']['report'],
        parent_fine_tail_adapter_sha256='a4982368cd86d09fc542ec64d4e7dd43c292cd2b6861aeca20b3f1f058176cf6',
        actual_seventeen_field_reader_sha256=PINS['root_geometry_eight_actual_reader_bridge.py'],
        actual_eight_parent_adapter_sha256='e383770d5e1828a837d323a45ba779f1afca3ce5997cf4c481f7d1fe84d0152d',
        vd_positive_increment_trust_restricted_to=.001,
        sync_length_restriction_is_design_only_not_a_problem_completion_standard=True,
        original_six_combined_half_vectors_remain_unavailable=True,
        new_two_measured_external_half_columns_do_not_replace_that_missing_direct_gate=True,
        accepted_fine_core_primary=str(a.fine_accepted),accepted_fine_core_sha256=sha(a.fine_accepted),
        actual_two_baseline_readback_sha256=sha(a.fine_readback),
        tail_proxy_core_centre_is_fine32=True,geometric_row_centre_remains_original_coarse28=True,
        actual_coarse28_direction_embedding_into_fine32='All28 original increments retained; four additional fine modes have zero increment, while their actual fine baseline values are preserved.',
        fine_control_Jacobian_or_fine_geometry_LP_claimed=False,
        baseline_report_sha256=sha(rows['baseline']['report']),complete_control_order=names,
        normalized_complete_core_slopes=slopes.tolist(),actual_physical_frequencies=frequencies.tolist(),
        explicit_baseline_multiplier=str(factor),baseline_exact_weighted_tails={str(k):rat(v) for k,v in exact.items()},
        exact_weighted_tail_budgets={str(k):rat(factor*v) for k,v in exact.items()},
        extra_positive_LP_variables_only=True,original_five_geometric_row_families_retained=True,
        design_proxy_only=True,inlet_projection_and_actual_new_BVP_still_required=True)
    tmp=a.out.with_name(a.out.name+'.tail-proxy.tmp');tmp.write_text(json.dumps(output,indent=2)+'\n');tmp.replace(a.out)
    print(json.dumps(dict(event='actual_complete_core_tail_proxy_minimax_finished',path=str(a.out),sha256=sha(a.out),
                         scenarios=len(output['predictions']),successful=sum(bool(r.get('success')) for r in output['predictions']))),flush=True)


if __name__=='__main__':main()
