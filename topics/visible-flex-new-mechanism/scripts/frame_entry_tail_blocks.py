#!/usr/bin/env python3
"""Two-block arrays for all existing154 u/v columns, with9 heights fixed.

No geometry or research input is loaded. B uses radius r and T uses r/8;
physical infinity and L1 costs retain the original box-normalized units.
Only the artificial CLI may solve small array LPs.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import numpy as np
from frame_entry_body_subspace import (
    EntryBody103Subspace, expected_layout, RationalRowGrid, FullGridValues,
    SelectedRows, ConstantCapGate, ArrayLP, ACTUAL_FLAGS, GROUP_COUNT,
    digest, exact, finite, array_digest, _validate_center,
    fixed_domain_summary as old_fixed_domain_summary,
    initial_restriction_decision, constant_soft_budget_feasible)

SCHEMA='same-163-entry-tail154-two-block-array-model-v1'


class EntryTail154Subspace(EntryBody103Subspace):
    def __init__(self,layout):
        super().__init__(layout)
        self.body_columns=self.columns.copy()
        self.tail_columns=np.r_[np.arange(54,81),np.arange(129,153)].astype(np.int64)
        self.columns=np.arange(154,dtype=np.int64)
        self.fixed_columns=np.arange(154,163,dtype=np.int64)
        self.block_weights=np.ones(154);self.block_weights[self.tail_columns]=1/8
        for x in (self.body_columns,self.tail_columns,self.columns,self.fixed_columns,self.block_weights):
            x.flags.writeable=False
        self.right=Q(423,500)
        self.definition={'schema':SCHEMA,'layout':self.layout,
            'columns':self.columns.tolist(),'fixed_columns':self.fixed_columns.tolist(),
            'body_columns':self.body_columns.tolist(),'tail_columns':self.tail_columns.tolist(),
            'block_weight_exact':{'body':'1','tail':'1/8'},
            'variable_radial_open_interval_exact':[str(self.left),str(self.right)],
            'endpoints_are_constant_by_zero_two_jets':True,
            'fixed_height_and_fixed_radial_metric_required':True,
            'classification_uses_exact_radial_support_not_small_Jacobian':True,
            'existing163_family_not_a_new_basis_or_new_metric':True}
        self.definition_sha256=digest(self.definition)

    def lift_step(self,selected):
        full=np.zeros(163);full[self.columns]=finite(selected,(154,));return full

    def apply(self,state,selected):
        state=finite(state,(163,));out=state.copy()
        out[self.columns]=state[self.columns]+finite(selected,(154,))
        if out[self.fixed_columns].tobytes()!=state[self.fixed_columns].tobytes():
            raise ArithmeticError('fixed9 height coefficient bits changed')
        return out


def fixed_domain_summary(subspace,full_grids):
    out=old_fixed_domain_summary(subspace,full_grids)
    out['schema']=SCHEMA+'-fixed-domain'
    out['outside_scope']='t<=9/250 or t>=423/500, not the old103 tail-fixed region'
    return out


def build_primary(subspace, full_grids, selections, state, lower, upper, cap, *,
        trust_exact, fraction_to_boundary_exact='1/2', physical_norm_weight_exact='1/1000',
        strip_floor_exact='1/10000000', curvature_floor_exact='1/10000000'):
    state, lower, upper, cap_record = _validate_center(subspace, state, lower, upper, cap)
    summary = fixed_domain_summary(subspace, full_grids)
    if not summary['outside_hard_original_tolerance_pass']:
        raise ValueError('constant outside hard row fails original tolerance')
    if len(selections) != 2 or any(s.full is not f for s, f in zip(selections, full_grids)):
        raise ValueError('selected J rows must belong to these same complete coarse/fine values')
    r, gamma, weight = map(float, [exact(trust_exact), exact(fraction_to_boundary_exact), exact(physical_norm_weight_exact)])
    strip_floor, curve_floor = float(exact(strip_floor_exact)), float(exact(curvature_floor_exact))
    if not(r > 0 and 0 < gamma <= 1 and weight >= 0 and min(strip_floor, curve_floor) >= 0):
        raise ValueError('positive declared trust and valid original target constants required')
    values, jacobians, groups, tols, tags = [], [], [], [], []
    invariant_rows, outside_J_max = [], 0.
    for selection in selections:
        parts, grid = selection.parts, selection.full.grid
        if np.any(selection.values[parts['groups'] >= 2] < -selection.tolerances[parts['groups'] >= 2]):
            raise ValueError('selected accepted hard rows must satisfy original tolerances')
        variable = parts['variable']
        Jsub = selection.J[:, subspace.columns]
        if np.any(~variable):
            outside_J_max = max(outside_J_max, float(np.max(abs(Jsub[~variable]))))
        for i in np.flatnonzero(~variable):
            invariant_rows.append({**grid.coordinate(int(selection.ids[i])),
                'role': 'outside-soft-aggregated' if parts['groups'][i] < 2 else 'outside-hard-original-tolerance'})
        values.extend(selection.values[variable]); jacobians.extend(Jsub[variable])
        groups.extend(parts['groups'][variable]); tols.extend(selection.tolerances[variable])
        tags.extend(grid.coordinate(int(i)) for i in selection.ids[variable])
    values, groups, tols = np.array(values, float), np.array(groups, int), np.array(tols, float)
    J = np.array(jacobians, float).reshape(-1, 154)
    n, m = 154, len(values); soft, hard = groups < 2, groups >= 2
    width = upper[subspace.columns]-lower[subspace.columns]
    weights = subspace.block_weights
    scale = r*width*weights
    target = values-gamma*(values+tols)
    target[soft] = 0.
    target[np.isin(groups, [4, 5])] = np.maximum(target[np.isin(groups, [4, 5])], strip_floor)
    target[np.isin(groups, [7, 8, 9, 10])] = np.maximum(target[np.isin(groups, [7, 8, 9, 10])], curve_floor)
    A, b = np.zeros((m+2*n, n+2)), np.zeros(m+2*n)
    A[:m, :n] = -J*scale; b[:m] = values
    b[:m][hard] = values[hard]-target[hard]
    A[:m, n][soft] = -1.
    for j in range(n):
        A[m+j, j] = weights[j]; A[m+j, n+1] = -1.
        A[m+n+j, j] = -weights[j]; A[m+n+j, n+1] = -1.
    lo = np.maximum(-1., (lower[subspace.columns]-state[subspace.columns])/scale)
    hi = np.minimum(1., (upper[subspace.columns]-state[subspace.columns])/scale)
    c = np.r_[np.zeros(n), 1., weight*r]
    rho0 = max(summary['rho_out'], 0., float(np.max(-values[soft])) if np.any(soft) else 0.)
    center_signature = {'subspace': subspace.definition_sha256, 'state': array_digest(state),
        'lower': array_digest(lower), 'upper': array_digest(upper), 'cap': cap_record,
        'selected_tags': tags, 'values': array_digest(values), 'Jacobian154': array_digest(J),
        'tolerances': array_digest(tols), 'outside_soft_lower_bound': summary['rho_out'],
        'fraction_to_boundary_exact': str(exact(fraction_to_boundary_exact)),
        'physical_norm_weight_exact': str(exact(physical_norm_weight_exact)),
        'strip_floor_exact': str(exact(strip_floor_exact)), 'curvature_floor_exact': str(exact(curvature_floor_exact))}
    info = {'schema': SCHEMA+'-primary', 'subspace_definition_sha256': subspace.definition_sha256,
        'trust_exact': str(exact(trust_exact)), 'trust_evaluated': r,
        'body_radius_evaluated':r, 'tail_radius_evaluated':r/8,
        'block_step_definition':'p_i=r*D_i*s_i*z_i; s_B=1,s_T=1/8',
        'norm_epigraph_definition':'h>=s_i*abs(z_i); objective rho+physical_weight*r*h',
        'variables': '154 block-normalized selected steps, rho, physical-infinity auxiliary',
        'physical_norm_weight_exact': str(exact(physical_norm_weight_exact)),
        'auxiliary_objective_coefficient': weight*r, 'rho_out': summary['rho_out'],
        'initial_selected_and_constant_metric_slack': rho0,
        'cap_invariant': cap_record, 'fixed_domain': summary,
        'active_original_rows': tags, 'invariant_original_rows': invariant_rows,
        'in_domain_zero_J_rows_kept': int(np.sum(np.all(J == 0, axis=1))),
        'outside_selected_J_max_diagnostic_only': outside_J_max,
        'row_classification_did_not_use_J_values': True,
        'no_cap_LP_row_added': True, 'original_complete_pools_not_mutated': True,
        'radius_independent_model_sha256': digest(center_signature)}
    result = ArrayLP(A, b, c, np.r_[lo, summary['rho_out'], 0.], np.r_[hi, np.inf, 1.], information=info)
    result.subspace, result.full_grids, result.selections = subspace, full_grids, selections
    result.state, result.original_lower, result.original_upper = state, lower, upper
    result.active_values, result.active_J, result.active_groups, result.active_tolerances = values, J, groups, tols
    result.targets, result.width, result.step_scale, result.trust = target, width, scale, r
    result.block_weights=weights
    return result


def primary_physical_step(model, variables):
    x = finite(variables, model.c.shape)
    return model.subspace.lift_step(model.step_scale*x[:154])


def radius_mapped_witness(old_model, new_model, variables):
    if old_model.information['radius_independent_model_sha256'] != new_model.information['radius_independent_model_sha256']:
        raise ValueError('radius containment compares one center, row set, D and physical objective only')
    if new_model.trust < old_model.trust:
        raise ValueError('only enlargement is the declared feasible-set inclusion')
    x = finite(variables, old_model.c.shape).copy()
    ratio = old_model.trust/new_model.trust
    x[:154] *= ratio; x[-1] *= ratio
    return x


def build_correction(primary, trial_full_grids, full_primary_step, *,
        physical_margin_retention_exact='1/4', predicted_descent_retention_exact='1/2',
        correction_relative_radius_exact='1/2', strip_floor_exact='1/10000000',
        curvature_floor_exact='1/10000000', improvement_floor=1e-10):
    """Original-unit SOC arrays; a separate positive scaling helper may consume them."""
    p = finite(full_primary_step, (163,)); S = primary.subspace.columns
    if np.any(p[primary.subspace.fixed_columns] != 0):
        raise ValueError('SOC primary step must have only the declared154 u/v coordinates')
    if len(trial_full_grids) != 2 or any(a.grid.definition != b.grid.definition
            for a, b in zip(primary.full_grids, trial_full_grids)):
        raise ValueError('actual same-y rows on the same full grids required')
    if any(not np.array_equal(a.b, b.b) for a, b in zip(primary.full_grids, trial_full_grids)):
        raise ValueError('fixed common height changed in trial input')
    trial = []
    for original, actual in zip(primary.selections, trial_full_grids):
        ids = original.ids[original.parts['variable']]
        trial.extend(actual.rows.reshape(-1)[ids])
    trial = np.array(trial, float)
    base, J, groups = primary.active_values, primary.active_J, primary.active_groups
    soft, hard = groups < 2, groups >= 2
    outside = primary.information['rho_out']
    linear = base+J@p[S]
    rho0 = primary.information['initial_selected_and_constant_metric_slack']
    rho1 = max(outside, 0., float(np.max(-linear[soft])) if np.any(soft) else 0.)
    norm = float(np.max(abs(p[S])/(primary.width*primary.block_weights)))
    physical_norm=float(np.max(abs(p[S])/primary.width)); gain = rho0-rho1
    retention = float(exact(predicted_descent_retention_exact))
    gamma = float(exact(physical_margin_retention_exact)); relative = float(exact(correction_relative_radius_exact))
    if not(0 < retention <= 1 and 0 <= gamma <= 1 and relative > 0):
        raise ValueError('valid declared original SOC retention and radius required')
    info = {'schema': SCHEMA+'-SOC', 'source_primary_model_sha256': primary.information['radius_independent_model_sha256'],
        'initial_metric_slack': rho0, 'primary_predicted_metric_slack': rho1,
        'primary_predicted_improvement': gain, 'primary_box_normalized_norm': physical_norm,
        'primary_block_normalized_norm':norm,
        'correction_radius_based_on_block_norm_not_unweighted_physical_norm':True,
        'rho_out': outside, 'actual_y_rows_not_base_linear_rows': True,
        'full_original_rows_and_J_layout_unchanged_outside_this_array_projection': True}
    if norm == 0 or gain <= improvement_floor:
        return None, dict(info, status='no-primary-predicted-restoration-for-SOC')
    radius = relative*norm; budget = rho0-retention*gain
    info.update(metric_slack_budget=budget, maximum_box_normalized_correction=radius,
        body_correction_radius=radius,tail_correction_radius=radius/8)
    if not constant_soft_budget_feasible(outside, budget):
        return None, dict(info, status='SOC-budget-below-fixed-outside-soft-bound')
    target = gamma*np.maximum(base, 0.)
    for gs, floor in [([4, 5], float(exact(strip_floor_exact))), ([7, 8, 9, 10], float(exact(curvature_floor_exact)))]:
        if floor < 0:
            raise ValueError('proposal floor must be nonnegative')
        mask = np.isin(groups, gs); target[mask] = np.maximum(target[mask], floor)
    n, m = 154, len(base)
    A, b = np.zeros((m+2*n, 2*n)), np.zeros(m+2*n)
    A[:m, :n] = -J*primary.width; b[:m] = trial-target
    b[:m][soft] = trial[soft]+budget
    for j in range(n):
        A[m+j, j] = 1.; A[m+j, n+j] = -1.
        A[m+n+j, j] = -1.; A[m+n+j, n+j] = -1.
    y = primary.state+p
    lo = np.maximum(-radius*primary.block_weights, (primary.original_lower[S]-y[S])/primary.width)
    hi = np.minimum(radius*primary.block_weights, (primary.original_upper[S]-y[S])/primary.width)
    if np.any(lo > hi):
        return None, dict(info, status='SOC-original-box-and-relative-radius-empty')
    info.update(status='original-unit-two-block-SOC-arrays-ready',
        active_original_rows=primary.information['active_original_rows'],
        no_cap_or_external_hard_restoration_row_added=True,
        original_unit_objective='sum h_j, h_j>=abs(D_S^-1 w_S_j)',
        physical_v_box='abs(v_i)<=r_c*s_i; common auxiliary bound0<=h_i<=r_c',
        existing_positive_scaling_helper_remains_bijective_for_full_extended_array_LP=True,
        caller_must_keep_original_unit_residual_and_all_whole_grid_gates=True)
    model = ArrayLP(A, b, np.r_[np.zeros(n), np.ones(n)], np.r_[lo, np.zeros(n)],
                    np.r_[hi, np.full(n, radius)], information=info)
    model.subspace, model.width, model.radius = primary.subspace, primary.width, radius
    model.active_trial_values, model.targets = trial, target
    return model, info


def developer_check():
    """New two-block artificial arrays only; no surface or research input."""
    from frame_second_order_correction_scaling import scale_correction_lp
    S=EntryTail154Subspace(expected_layout())
    nodes=['0','9/250','9/100','33/50','309/400','423/500','9/10']
    arrays=[];selections=[]
    for label,nt in [('coarse',4),('fine',8)]:
        grid=RationalRowGrid(label,nodes,nt)
        rows=np.ones((11,grid.nr,nt));eta=np.full((grid.nr,nt),.2)
        rows[0,2]=-.0064;rows[0,4]=-.0065;rows[1,4]=-.005
        eta[2]=.2664;eta[4]=.2665
        rows[8,5]=2e-8  # constant endpoint, below the proposal floor only
        b=np.full(grid.nr,.7);means=np.zeros((grid.nr,3));means[:,2]=b
        values=FullGridValues(grid,rows,eta,b,np.full(11,1e-9),means)
        ids=np.array([2*nt,4*nt,grid.point_count+4*nt,
            8*grid.point_count+4*nt,8*grid.point_count+3*nt,8*grid.point_count+5*nt])
        J=np.zeros((len(ids),163));J[0,0]=.5;J[1:3,54]=1.;J[3,54]=-.1
        arrays.append(values);selections.append(SelectedRows(S,values,ids,J))
    state=np.zeros(163);state[154]=-0.;state[162]=.1
    lower=np.full(163,-1.);upper=np.full(163,1.)
    cap=ConstantCapGate(0.,-2.78e-17,1e-9,2.78e-17,1e-10)
    model=build_primary(S,arrays,selections,state,lower,upper,cap,trust_exact='1/4000')
    x=np.zeros(156);x[0]=.05;x[54]=1.;x[154]=.007;x[155]=.125
    p=primary_physical_step(model,x);candidate=S.apply(state,p[S.columns])
    norm=float(np.max(abs(p[S.columns])/model.width))
    larger=build_primary(S,arrays,selections,state,lower,upper,cap,trust_exact='1/2000')
    mapped=radius_mapped_witness(model,larger,x)
    checks={
        'partition_existing154_with103_body51_tail_and9_fixed':bool(
            len(S.body_columns)==103 and len(S.tail_columns)==51 and
            np.array_equal(np.sort(np.r_[S.body_columns,S.tail_columns]),S.columns)
            and len(S.fixed_columns)==9),
        'fixed_height_signed_zero_bits_preserved':candidate[S.fixed_columns].tobytes()==state[S.fixed_columns].tobytes(),
        'tail7725_is_now_variable_open_core_and_tail_remain_constant':
            arrays[0].grid.classify([4*4,1*4,5*4],S)['variable'].tolist()==[True,False,False],
        'block_primary_step_matches_declared_radii':bool(p[54]==model.trust*2/8 and p[0]==model.trust*2*.05),
        'physical_infinity_cost_not_unweighted_block_norm':bool(norm==model.trust*.125
            and model.c[-1]*x[-1]==.001*norm and x[-1]!=np.max(abs(x[:154]))),
        'constant_endpoint_floor_does_not_enter_LP':bool(any(t['t_exact']=='423/500'
            for t in model.information['invariant_original_rows']) and all(t['t_exact']!='423/500'
            for t in model.information['active_original_rows'])),
        'internal_zero_J_hard_rows_kept':bool(model.information['in_domain_zero_J_rows_kept']==2),
        'same_center_radius_mapping_preserves_step_cost_and_feasibility':bool(
            np.array_equal(primary_physical_step(model,x),primary_physical_step(larger,mapped))
            and model.residual(x)['objective_evaluated']==larger.residual(mapped)['objective_evaluated']
            and model.residual(x)['maximum_original_linear_row_violation']==0
            and larger.residual(mapped)['maximum_original_linear_row_violation']==0
            and larger.residual(mapped)['maximum_original_linear_bound_violation']==0)}
    p=S.lift_step(np.r_[.00001,np.zeros(53),.00002,np.zeros(99)])
    trials=[]
    for item in arrays:
        rows=item.rows.copy();rows[0,2]+=.5*p[0];rows[:2,4]+=p[54]-2e-6
        trials.append(FullGridValues(item.grid,rows,item.eta,item.b,item.tolerances,item.mean_Xs))
    correction,info=build_correction(model,trials,p)
    if correction is None:raise AssertionError('new artificial SOC arrays unexpectedly absent')
    rc=correction.radius
    scaled=scale_correction_lp(correction.A,correction.b,correction.lower,correction.upper,rc)
    z=np.zeros(308);z[54]=.0625;z[154+54]=.0625
    original=scaled.to_original(z);physical=correction.width*original[:154]
    soft=model.active_groups<2
    checks.update({
        'SOC_radius_uses_new_block_norm':bool(rc==.5*np.max(abs(p[:154])/(model.width*S.block_weights))
            and info['primary_box_normalized_norm']==np.max(abs(p[:154])/model.width)),
        'SOC_tail_and_body_bounds_keep_one_eighth_ratio':bool(np.allclose(correction.upper[:154],rc*S.block_weights,rtol=0,atol=0)
            and np.allclose(scaled.upper[:154],S.block_weights,rtol=0,atol=0)),
        'SOC_physical_L1_and_positive_scaling_objective_match':bool(np.isclose(
            correction.c@original,rc*(scaled.objective@z),rtol=0,atol=1e-20)
            and np.isclose(correction.c@original,np.sum(abs(physical)/correction.width),rtol=0,atol=1e-20)),
        'SOC_actual_y_soft_rows_and_cumulative_original_box':bool(np.array_equal(
            correction.b[:len(soft)][soft],correction.active_trial_values[soft]+info['metric_slack_budget'])
            and np.array_equal(correction.lower[:154],np.maximum(-rc*S.block_weights,(lower[:154]-state[:154]-p[:154])/model.width))
            and np.array_equal(correction.upper[:154],np.minimum(rc*S.block_weights,(upper[:154]-state[:154]-p[:154])/model.width))),
        'SOC_zero_primary_has_no_division_or_solver':build_correction(model,arrays,np.zeros(163))[0] is None,
        'original_unit_residual_remains_available':all(k in scaled.original_residuals(z)
            for k in ['maximum_original_linear_row_violation','maximum_original_linear_bound_violation'])})
    bad=expected_layout();bad['normalized_Q_parameter_index']=152
    try:EntryTail154Subspace(bad);checks['changed_layout_rejected']=False
    except ValueError:checks['changed_layout_rejected']=True
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema':SCHEMA+'-new-array-development','passed':all(checks.values()),'checks':checks,
        'artificial_arrays_only':True,'no_geometry_or_old_development_suite_run':True,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'primary_dimensions':list(model.A.shape),'SOC_dimensions':list(correction.A.shape),
        'body_radius':model.trust,'tail_radius':model.trust/8,'SOC_radius':rc}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path)
    args=parser.parse_args();report=developer_check()
    text=json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.out:args.out.write_text(text)
    print(text,end='')
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
