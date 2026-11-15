#!/usr/bin/env python3
"""A new two-block154-column proposal domain in the unchanged 163-parameter family.

Complete original coarse/fine values, 163-column selected Jacobians and row IDs
remain authoritative. Only primary/SOC array assembly is restricted. Constant
outside hard rows and the constant height gate keep their original tolerance;
both outside soft branches become a complete-grid lower bound on rho.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
import numpy as np
import scipy
from scipy.optimize import linprog

from frame_collar_residual_audit import digest
from frame_entry_single_q import SingleQProblem
from frame_entry_tail_blocks import (EntryTail154Subspace, expected_layout,
    RationalRowGrid, FullGridValues, SelectedRows, ConstantCapGate,
    fixed_domain_summary, initial_restriction_decision, build_primary,
    build_correction, primary_physical_step, ACTUAL_FLAGS, array_digest)
from frame_metric_spectral_soc_scaling import (
    SOCScaledSpectralMetricObjective, configuration as previous_configuration,
    implementation_hashes as previous_hashes, compact_with_all_actual_gates,
    curvature_trial_diagnostics, scaling_definition as inherited_scaling_definition)
from frame_metric_spectral_strip_reserve import strip_floor_definition, strip_diagnostics
from frame_metric_spectral_curvature_reserve import floor_definition, floor_diagnostics
from frame_metric_spectral_physical_penalty import (penalty_definition as inherited_penalty_definition,
    evaluated_penalty as inherited_evaluated_penalty)
from frame_metric_spectral_adaptive import trial_quality, next_trust as shrink_next_trust
from frame_second_order_correction_scaling import scale_correction_lp
from frame_metric_budget_recovery import (require_public_research_environment,
    EvaluationBudgetReached, parabolic_candidate, curvature_arc_slack_bound)

POLICY = 'same-g-entry-tail154-restricted-spectral-step-v1'
POSITION_JETS = ('X', 'Xs', 'Xt', 'Xss', 'Xst', 'Xtt')


def implementation_hashes():
    from frame_metric_entry_body103 import implementation_hashes as prefix_hashes
    result = prefix_hashes()
    for name in ['frame_entry_tail_blocks.py', Path(__file__).name]:
        result[name] = hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return result


def configuration(base):
    cfg = previous_configuration(base)
    for key in list(cfg):
        if key.startswith('entry_body103_'):cfg.pop(key)
    cfg.update(entry_tail154_policy=POLICY,
        entry_tail154_initial_trust_exact='1/4000',
        entry_tail154_maximum_trust_exact='1/4000',
        entry_tail154_initial_success_streak=0,
        entry_tail154_tail_to_body_radius_ratio_exact='1/8',
        entry_tail154_effective_total_eta_drop_reference_exact='1/10000',
        entry_tail154_radius_is_new_subspace_choice_not_old_controller_continuation=True,
        entry_tail154_reference_drop_is_diagnostic_not_an_acceptance_threshold=True,
        full_geometry_Jacobian_still_has_163_columns=True)
    return cfg


def restriction_definition(cfg):
    if cfg.get('entry_tail154_policy') != POLICY:
        raise ValueError('explicit entry/tail154 algorithm configuration required')
    for key in ['entry_tail154_initial_trust_exact', 'entry_tail154_maximum_trust_exact']:
        if Q(cfg[key]) != Q(1, 4000):
            raise ValueError('the declared new subspace radius must not drift')
    if Q(cfg['entry_tail154_tail_to_body_radius_ratio_exact']) != Q(1,8):
        raise ValueError('declared tail/body ratio must not drift')
    if cfg['entry_tail154_initial_success_streak'] != 0:
        raise ValueError('new restricted proposal policy starts with zero success streak')
    return {'schema':POLICY+'-definition',
        'selected_columns':list(range(154)),
        'body_columns':list(range(54))+list(range(81,129))+[153],
        'tail_columns':list(range(54,81))+list(range(129,153)),
        'tail_to_body_radius_ratio_exact':'1/8',
        'physical_parameter_count':163, 'free_proposal_columns':154, 'fixed_columns':9,
        'new_initial_radius_exact':cfg['entry_tail154_initial_trust_exact'],
        'new_maximum_radius_exact':cfg['entry_tail154_maximum_trust_exact'],
        'new_initial_success_streak':0,
        'minimum_common_body_radius_exact':cfg['minimum_trust_box_fraction_exact'],
        'derived_minimum_tail_radius_exact':str(Q(cfg['minimum_trust_box_fraction_exact'])/8),
        'not_the_old_uniform_fullspace_minimum_for_every_coordinate':True,
        'variable_open_radial_interval_exact':['9/250','423/500'],
        'only_arrays_are_projected_full_J_and_row_IDs_are_preserved':True,
        'primary_step_mapping':'p_i=r D_i s_i z_i, s_B=1,s_T=1/8',
        'primary_infinity_epigraph':'h>=s_i abs(z_i), physical cost .001*r*h',
        'SOC_radius':'.5*max_i abs(p_i)/(D_i*s_i), v=w/D, abs(v_i)<=rc*s_i',
        'SOC_objective_remains_unweighted_physical_L1':'sum h_i, h_i>=abs(v_i)',
        'outside_hard_and_global_cap_keep_original_gate_tolerances':True,
        'complete_both_grid_outside_soft_branches_form_rho_lower_bound':True,
        'in_domain_zero_J_rows_are_kept':True,
        'primary_physical_norm_coefficient_exact':cfg['step_cost_physical_box_norm_coefficient_exact'],
        'actual_gates_Schur_eta_curvature_boxes_and_shared_budgets_unchanged':True,
        'quality_shrink_and_two_success_growth_conditions_unchanged_new_cap_explicit':True,
        'effective_total_drop_reference_exact':cfg['entry_tail154_effective_total_eta_drop_reference_exact'],
        'drop_reference_is_not_a_new_acceptance_gate':True,
        'no_Jacobian_cost_reduction_or_convergence_claim':True}


def scaling_definition(cfg):
    """Positive reparameterization of this new restricted SOC array LP only."""
    old=inherited_scaling_definition(cfg)
    for key in ['old_targets_including_strip_and_curvature_floors_unchanged',
            'old_primary_LP_and_every_controller_branch_unchanged',
            'no_increase_in_feasible_LP_set_or_actual_geometry_gate']:
        old.pop(key)
    old.update(schema=POLICY+'-SOC-positive-scaling-definition',
        equivalence_scope='the newly assembled two-block154 SOC array LP before versus after positive variable and affine-row scaling',
        old_variables='154 v=D^-1 w, abs(v_i)<=rc*s_i, 0<=h_i<=rc, h_i>=abs(v_i)',
        equivalence_is_only_inside_the_new_weighted_SOC_domain=True,
        new_SOC_radius_uses_weighted_primary_norm_explicitly=True,
        restricted_SOC_targets_unchanged_by_scaling_itself=True,
        restricted_SOC_primal_projection_and_optimal_set_equivalent_before_and_after_scaling=True,
        original_complete_geometry_gates_unchanged=True,
        proposal_subspace_and_radius_policy_changed_explicitly=True,
        invariant_outside_proposal_floors_and_constant_cap_row_omitted_explicitly=True,
        not_equivalence_to_the_old_full163_primary_or_SOC_feasible_set=True)
    return old



def penalty_definition(cfg):
    result=inherited_penalty_definition(cfg)
    result.pop('no_second_LP_or_changed_constraint_or_acceptance_threshold')
    result.pop('physical_model_and_all_SOC_rows_and_objective_unchanged')
    result.update(schema=POLICY+'-same-physical-penalty-definition',
        primary_objective='rho+.001*r*h; h>=s_i*abs(z_i), p_i=r*D_i*s_i*z_i',
        same_calibrated_physical_infinity_cost=True,
        proposal_domain_changes_are_defined_by_restriction_definition=True,
        actual_geometry_gates_and_no_second_cost_LP_unchanged=True,
        SOC_physical_L1_objective_unchanged_but_weighted_proposal_domain_is_new=True)
    return result


def evaluated_penalty(cfg,trust):
    result=inherited_evaluated_penalty(cfg,trust)
    result['definition']=penalty_definition(cfg)
    result['auxiliary_is_physical_norm_over_common_body_radius']=True
    return result

def layout_from_problem(problem):
    """Derive the descriptor from real source metadata, before expected-layout validation."""
    if not isinstance(problem, SingleQProblem):
        raise ValueError('the published SingleQProblem family is required')
    src = problem.source.space_definition()
    entry = problem.entry.identity
    original = problem.entry.original_source
    if (src.get('schema') != 'paired-entry-one-Q-column-tangent-space-v1'
            or src.get('radial_direction') != 'W5(x)*first retained original clamped quintic B3(t)'
            or entry.get('schema') != 'paired-entry-u4-v7-b6-definition-v1'
            or entry.get('free_weight_powers') != {'u':2,'v':5,'height':4}
            or src.get('all_old_columns_are_retained_with_their_original_coefficients') is not True
            or problem.metric_free != 0
            or original.angular_modes != 5 or original.phi_modes != 3
            or original.core_direction is not True):
        raise ValueError('proved entry/Q/angle metadata changed')
    basis = src['radial_basis_identity']
    if (basis.get('zero_extension_outside_active_interval') is not True
            or problem.Q.identity.get('schema') != 'exact-elliptic-normalized-Q-angular-direction-v1'
            or src['old_radial_field_knots'] != problem.radial_knots
            or src['old_radial_field_knots'] != basis['clamped_knots_exact']):
        raise ValueError('the Q support or original field knots are not the declared ones')
    left, length = Q(entry['entry_left_exact']), Q(entry['entry_length_exact'])
    if left != problem.entry.left_exact or length != problem.entry.length_exact:
        raise ValueError('entry object and exact identity disagree')
    layout = {'schema':'published-entry-single-Q-163-layout-v1',
        'nunknown':int(problem.nunknown),
        'slices':{name:[sl.start,sl.stop] for name,sl in problem.slices.items()},
        'flattening':'radial-major/angular-minor',
        'radial_free':int(original.radial_free),
        'u_angular_columns':int(original.angular_counts['u']),
        'v_angular_columns_before_Q':int(original.angular_counts['v']),
        'radial_degree':int(original.field_basis.full.k),
        'retained_original_basis_indices':list(range(3, original.field_basis.full.c.shape[0]-3)),
        'clamped_knots_exact':list(basis['clamped_knots_exact']),
        'entry_left_exact':str(left), 'entry_length_exact':str(length),
        'entry_cutoff':'1 on [0,ell/3]; 1-S9((3*x/ell-1)/2) to ell; 0 afterwards',
        'entry_weight':'1-chi+chi*(x/ell)^power',
        'entry_weight_powers':{k:entry['free_weight_powers'][k] for k in ['u','v']},
        'normalized_Q_parameter_index':int(problem.q_index),
        'Q_radial_basis_index':int(basis['selected_full_spline_index']),
        'Q_weight_power':5, 'length_exact':str(problem.seed.length_exact),
        'current_height_independent_of_current_u_v':bool(problem.identity(np.zeros(problem.nunknown)).get(
            'immutable_height_reference_is_the_old_model_not_recomputed_using_new_Q') is True)}
    # identity() serializes coefficients and metadata only; it does not evaluate geometry.
    EntryTail154Subspace(layout)
    return layout


def restricted_growth_definition(cfg):
    definition = restriction_definition(cfg)
    return {'schema':POLICY+'-next-model-scale',
        'initial_radius_exact':definition['new_initial_radius_exact'],
        'initial_success_streak':0, 'maximum_radius_exact':definition['new_maximum_radius_exact'],
        'consecutive_models':cfg['trust_growth_required_consecutive_models'],
        'complete_ratio_threshold_exact':cfg['trust_growth_minimum_complete_ratio_exact'],
        'norm_fraction_threshold_exact':cfg['trust_growth_minimum_actual_norm_fraction_exact'],
        'growth_factor_exact':cfg['trust_growth_factor_exact'],
        'old_actual_quality_and_curvature_failure_shrink_priority':True,
        'growth_requires_first_full_primary_acceptance_no_SOC_backtrack_new_rows':True,
        'at_most_one_update_per_model':True,
        'restored_entry_body103_controller_is_recorded_but_not_inherited':True}


def next_restricted_trust(model, current_trust, streak, cfg):
    restricted_growth_definition(cfg)
    if type(streak) is not int or not 0 <= streak < 2:
        raise ValueError('bounded consecutive-success streak required')
    before = float(model['trust_before_model'])
    after, old = shrink_next_trust(before, current_trust, model.get('scale_feedback_trials',[]), cfg)
    trials = model.get('trials',[]); first = trials[0] if len(trials)==1 else {}
    quality = first.get('scale_feedback',{}); ratio = quality.get('actual_to_predicted_ratio')
    norm = model.get('linear_program',{}).get('primary_step_cost_diagnostic',{}).get('actual_trust_normalized_step_norm')
    checks = {
        'first_only_full_primary_accepted':bool(len(trials)==1 and first.get('kind')=='primary-metric-short-step'
            and first.get('alpha_exact')=='1' and first.get('accepted_as_next_iterate') is True
            and model.get('result')=='accepted-two-grid-true-metric-descent'),
        'no_SOC_or_backtrack':bool(not model.get('corrections') and len(trials)==1),
        'complete_actual_two_grid_gates':bool(quality.get('full_two_grid_actual_available')
            and first.get('coarse_decision',{}).get('single_grid_admissible_recovery_point')
            and first.get('fine_decision',{}).get('single_grid_admissible_recovery_point')),
        'valid_high_complete_ratio':bool(quality.get('ratio_denominator_usable') and ratio is not None
            and np.isfinite(ratio) and ratio >= float(Q(cfg['trust_growth_minimum_complete_ratio_exact']))),
        'actual_step_uses_radius':bool(norm is not None and np.isfinite(norm)
            and norm >= float(Q(cfg['trust_growth_minimum_actual_norm_fraction_exact']))),
        'no_new_coarse_or_fine_rows':bool(trials and all(t.get('new_coarse_rows')==0
            and t.get('new_fine_rows')==0 for t in trials)),
        'old_shrink_not_requested_or_applied':bool(after==before and current_trust==before
            and not old['trigger_trial_indices'])}
    qualified=all(checks.values()); count=streak+1 if qualified else 0
    cap=float(Q(cfg['entry_tail154_maximum_trust_exact'])); next_radius=after; grew=False;at_cap=False
    if count==2:
        next_radius=min(after*float(Q(cfg['trust_growth_factor_exact'])),cap)
        if next_radius<after:raise ValueError('restricted trust already exceeds declared new cap')
        grew=next_radius>after;at_cap=not grew;count=0
    report=copy.deepcopy(old)
    report.update(next_trust=next_radius,trust_after_unchanged_shrink_rule=after,
        conservative_growth={'streak_before':streak,'streak_after':count,
            'qualifying_model':qualified,'checks':checks,'failed_conditions':[k for k,v in checks.items() if not v],
            'complete_ratio':ratio,'actual_step_norm_over_radius':norm,
            'new_coarse_rows':sum(int(t.get('new_coarse_rows',0)) for t in trials),
            'new_fine_rows':sum(int(t.get('new_fine_rows',0)) for t in trials),
            'grew_for_next_model':grew,'qualified_pair_at_cap':at_cap,
            'new_explicit_cap_evaluated':cap,'old_shrink_has_priority':True,
            'input_model_and_trials_not_modified':True})
    return next_radius,count,report


class EntryTail154Objective(SOCScaledSpectralMetricObjective):
    def __init__(self,*args,radial_nodes_exact,**kwargs):
        super().__init__(*args,**kwargs)
        self.subspace=EntryTail154Subspace(layout_from_problem(self.problem))
        self.row_grids=[RationalRowGrid('coarse',radial_nodes_exact,len(self.theta)),
                       RationalRowGrid('fine',radial_nodes_exact,len(self.fine_theta))]
        if any(not np.array_equal(np.array([float(t) for t in g.nodes]),self.radial) for g in self.row_grids):
            raise ValueError('rational support classification must bind actual value-grid coordinates')
        if np.any(self.gate.row[self.subspace.columns]!=0):
            raise ValueError('the common height gate must be independent of all selected u/v columns')
        self.restricted_reference=None;self.restricted_initial_diagnostic=None
        self.evaluation_definition.update(primary_physical_step_cost=penalty_definition(self.cfg),
            entry_tail154=restriction_definition(self.cfg),
            entry_tail154_layout=self.subspace.definition,
            original_row_grids=[g.definition for g in self.row_grids],
            adaptive_trust_policy=restricted_growth_definition(self.cfg),
            conservative_trust_growth=restricted_growth_definition(self.cfg),
            SOC_reversible_scaling=scaling_definition(self.cfg),
            entry_tail154_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def full_views(self,state):
        state=np.asarray(state,float)
        if (not np.array_equal(self.epigraph_cache['vector'][:-1],state)
                or not np.array_equal(self.geometry_cache['state'],state)
                or not np.array_equal(self.fine_cache['state'],state)):
            raise ValueError('both complete current-state caches required, without implicit value calls')
        values=[]
        for grid,rows,data in [(self.row_grids[0],self.epigraph_cache['rows'],self.geometry_cache),
                (self.row_grids[1],self.fine_cache['rows'],self.fine_cache['data'])]:
            values.append(FullGridValues(grid,rows,data['eta'],data['height']['b'],self.row_tolerances(),
                np.mean(data['Xs'],axis=1)))
        return values

    def constant_cap(self):
        c=self.epigraph_cache['record']['decision']['cap_and_box'];f=self.fine_cache['decision']['cap_and_box']
        for key in ['affine_height_margin','height_tolerance','height_reconstruction_consistency_tolerance']:
            if c[key]!=f[key]:raise ValueError('constant cap numerical gate differs between current grids')
        return ConstantCapGate(c['affine_height_margin'],
            min(c['reconstructed_height_margin'],f['reconstructed_height_margin']),c['height_tolerance'],
            max(c['reconstructed_minus_affine_height_absolute'],f['reconstructed_minus_affine_height_absolute']),
            c['height_reconstruction_consistency_tolerance'])

    def install_reference(self,state):
        views=self.full_views(state);self.restricted_initial_diagnostic=fixed_domain_summary(self.subspace,views)
        reference={'state':np.asarray(state,float).copy(),'grids':{}}
        for grid,data in [(self.row_grids[0],self.geometry_cache),(self.row_grids[1],self.fine_cache['data'])]:
            outside=np.array([not(self.subspace.left<t<self.subspace.right) for t in grid.nodes])
            reference['grids'][grid.label]={k:np.asarray(data[k])[outside].copy() for k in POSITION_JETS}
            reference['grids'][grid.label].update(
                metric={k:np.asarray(data['metric'][k])[outside].copy() for k in ['a','a_s','a_ss']},
                center=np.asarray(data['center']).copy(),
                height={k:np.asarray(data['height'][k]).copy() for k in ['b','b_s','b_ss']})
        self.restricted_reference=reference
        return self.restricted_initial_diagnostic

    def invariant_diagnostic(self,state,*,fine_present):
        if self.restricted_reference is None:raise ValueError('initial accepted reference required')
        state=np.asarray(state,float);fixed=self.subspace.fixed_columns
        same=state[fixed].tobytes()==self.restricted_reference['state'][fixed].tobytes()
        if not same:raise ArithmeticError('a proposal changed one of the fixed9 coefficients')
        result={'fixed9_coefficients_bitwise_unchanged':same,'no_additional_geometry_call':True,
            'whole_grid_gates_still_required':True,'grids':{}}
        specs=[(self.row_grids[0],self.geometry_cache)]
        if fine_present:specs.append((self.row_grids[1],self.fine_cache['data']))
        for grid,data in specs:
            outside=np.array([not(self.subspace.left<t<self.subspace.right) for t in grid.nodes])
            ref=self.restricted_reference['grids'][grid.label]
            result['grids'][grid.label]={'outside_six_jet_max_difference':{
                    k:float(np.max(abs(np.asarray(data[k])[outside]-ref[k]))) for k in POSITION_JETS},
                'outside_metric_jet_max_difference':{k:float(np.max(abs(np.asarray(data['metric'][k])[outside]-ref['metric'][k])))
                    for k in ['a','a_s','a_ss']},
                'full_common_center_max_difference':float(np.max(abs(np.asarray(data['center'])-ref['center']))),
                'full_fixed_height_jet_max_difference':{k:float(np.max(abs(np.asarray(data['height'][k])-ref['height'][k])))
                    for k in ['b','b_s','b_ss']}}
        return result

    def snapshot(self):
        result=super().snapshot()
        result.update(primary_physical_step_cost=penalty_definition(self.cfg),
            entry_tail154=restriction_definition(self.cfg),
            adaptive_trust_policy=restricted_growth_definition(self.cfg),
            conservative_trust_growth=restricted_growth_definition(self.cfg),
            SOC_reversible_scaling=scaling_definition(self.cfg),
            entry_tail154_initial_fixed_domain=copy.deepcopy(self.restricted_initial_diagnostic))
        return result


def selected_model(objective,state,base,J,groups,tols,trust,cfg):
    full=objective.full_views(state);count=len(objective.pool)
    selected=[SelectedRows(objective.subspace,full[0],objective.pool,J[:count]),
              SelectedRows(objective.subspace,full[1],objective.fine_pool,J[count:])]
    if (not np.array_equal(np.r_[selected[0].values,selected[1].values],base)
            or not np.array_equal(np.r_[selected[0].parts['groups'],selected[1].parts['groups']],groups)
            or not np.array_equal(np.r_[selected[0].tolerances,selected[1].tolerances],tols)):
        raise ValueError('full original selected row stack no longer binds current cache/IDs')
    return build_primary(objective.subspace,full,selected,state,objective.lower,objective.upper,
        objective.constant_cap(),trust_exact=str(Q.from_float(float(trust))),
        fraction_to_boundary_exact=cfg['linear_fraction_to_boundary_exact'],
        physical_norm_weight_exact=cfg['step_cost_physical_box_norm_coefficient_exact'],
        strip_floor_exact=cfg['strip_proposal_floor_exact'],
        curvature_floor_exact=cfg['curvature_proposal_floor_exact'])


def model_projection_record(model):
    info=model.information
    return {'subspace_definition_sha256':model.subspace.definition_sha256,
        'physical_parameters':163,'LP_free_physical_columns':154,'fixed_parameters':9,
        'active_original_row_count':len(info['active_original_rows']),
        'active_original_row_mapping_sha256':digest(info['active_original_rows']),
        'invariant_original_selected_row_count':len(info['invariant_original_rows']),
        'invariant_original_row_mapping_sha256':digest(info['invariant_original_rows']),
        'in_domain_zero_J_rows_kept':info['in_domain_zero_J_rows_kept'],
        'outside_selected_J_max_diagnostic_only':info['outside_selected_J_max_diagnostic_only'],
        'rho_out':info['rho_out'],'eta_out':info['fixed_domain']['eta_out'],
        'eta_out_location':info['fixed_domain']['eta_out_location'],
        'constant_cap':info['cap_invariant'],
        'full_original_base_J_rowIDs_preserved_for_defect_diagnostics':True,
        'full_geometric_Jacobians_still_163_columns_not_a_memory_reduction_claim':True}


def _proposal_floor_report(model,cfg,*,trial=None,linear=None):
    base=model.active_values;groups=model.active_groups
    if trial is None:
        actual=base;legacy=base-float(Q(cfg['linear_fraction_to_boundary_exact']))*(base+model.active_tolerances)
    else:
        actual=trial;legacy=float(Q(cfg['SOC_physical_margin_retention_exact']))*np.maximum(base,0.)
    before=legacy.copy();curved=np.isin(groups,[7,8,9,10])
    before[curved]=np.maximum(before[curved],float(Q(cfg['curvature_proposal_floor_exact'])))
    target=before.copy();strip=np.isin(groups,[4,5])
    target[strip]=np.maximum(target[strip],float(Q(cfg['strip_proposal_floor_exact'])))
    curve=floor_diagnostics(base,actual,legacy,target,groups,cfg,linear=linear)
    strip_report=strip_diagnostics(base,actual,before,target,groups,cfg,linear=linear)
    indices=[];offset=0
    for selection in model.selections:
        indices.extend((offset+np.flatnonzero(selection.parts['variable'])).tolist());offset+=len(selection.ids)
    table=curve.get('group8_selected_rows',{})
    if table:
        table['columns'][0]='active_projection_stack_index'
        table['columns']+=['original_full_selected_stack_index','original_grid','original_flat_row_id']
        for row in table['rows']:
            i=int(row[0]);tag=model.information['active_original_rows'][i]
            row += [indices[i],tag['grid'],tag['flat_row_id']]
    curve['indexing']='active projection stack with an explicit mapping back to unchanged original coarse/fine selected stacks'
    strip_report['selected_stack']=curve['indexing']
    return {'curvature_proposal_diagnostics':curve,'strip_proposal_diagnostics':strip_report}


def solve_primary(model,cfg):
    before=time.monotonic()
    r=linprog(model.c,A_ub=model.A,b_ub=model.b,bounds=list(zip(model.lower,model.upper)),method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    rho0=model.information['initial_selected_and_constant_metric_slack']
    report={'method':'HiGHS two-block154 spectral recovery; complete constant-domain treatment',
        'LP_invoked':True,'success':bool(r.success),'status':int(r.status),'message':str(r.message),
        'nit':int(r.nit),'elapsed_seconds':time.monotonic()-before,'rows':len(model.b),
        'variables':len(model.c),'matrix_bytes':model.A.nbytes,'trust_fraction':model.trust,
        'initial_metric_slack':rho0,'projection':model_projection_record(model),
        'hard_rows_count':int(np.sum(model.active_groups>=2)),
        'soft_metric_rows_count':int(np.sum(model.active_groups<2)),
        'curvature_cap_and_physical_rows_not_elastic':True}
    report.update(_proposal_floor_report(model,cfg))
    finite_primal=bool(r.x is not None and np.asarray(r.x).shape==model.c.shape and np.all(np.isfinite(r.x)))
    report['solver_returned_finite_primal']=finite_primal
    if not finite_primal:return None,report
    x=np.asarray(r.x,float);p=primary_physical_step(model,x);res=model.residual(x)
    actual_rho=max(model.information['rho_out'],0.,float(np.max(-(model.active_values+model.active_J@p[model.subspace.columns])[model.active_groups<2])))
    report.update(predicted_metric_slack=float(x[154]),
        predicted_slack_improvement=rho0-float(x[154]),
        predicted_slack_from_rows_and_outside=actual_rho,
        normalized_step_norm=float(x[-1]),maximum_linear_row_violation=res['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=res['maximum_original_linear_bound_violation'],
        maximum_absolute_physical_step=float(np.max(abs(p))),physical_step_l2=float(np.linalg.norm(p)))
    penalty=evaluated_penalty(cfg,model.trust);physical_norm=float(np.max(abs(p[model.subspace.columns])/model.width))
    penalty.update(returned_LP_norm_auxiliary=float(x[-1]),returned_primary_step_cost=float(model.c[-1]*x[-1]),
        returned_weighted_objective=res['objective_evaluated'],returned_predicted_metric_slack=float(x[154]),
        predicted_metric_slack_improvement=rho0-float(x[154]),
        actual_physical_box_normalized_step_norm=physical_norm,
        actual_trust_normalized_step_norm=float(np.max(abs(p[model.subspace.columns])/(model.width*model.block_weights)))/model.trust,
        actual_block_box_normalized_step_norm=float(np.max(abs(p[model.subspace.columns])/(model.width*model.block_weights))),
        body_utilization=float(np.max(abs(p[model.subspace.body_columns])/(model.width[model.subspace.body_columns]*model.trust))),
        tail_utilization=float(np.max(abs(p[model.subspace.tail_columns])/(model.width[model.subspace.tail_columns]*model.trust/8))),
        common_body_radius=model.trust,tail_radius=model.trust/8,
        physical_norm_cost_evaluated=float(Q(cfg['step_cost_physical_box_norm_coefficient_exact']))*physical_norm)
    report['primary_step_cost_diagnostic']=penalty
    report.update(_proposal_floor_report(model,cfg,linear=model.active_values+model.active_J@p[model.subspace.columns]))
    if not r.success or max(res['maximum_original_linear_row_violation'],res['maximum_original_linear_bound_violation'])>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='LP status or independent original-unit residual';return None,report
    return p,report


def solve_correction(primary,actual_full,p,cfg):
    model,info=build_correction(primary,actual_full,p,
        physical_margin_retention_exact=cfg['SOC_physical_margin_retention_exact'],
        predicted_descent_retention_exact=cfg['SOC_predicted_descent_retention_exact'],
        correction_relative_radius_exact=cfg['SOC_maximum_correction_relative_to_proposed_step_exact'],
        strip_floor_exact=cfg['strip_proposal_floor_exact'],curvature_floor_exact=cfg['curvature_proposal_floor_exact'],
        improvement_floor=cfg['linear_model_improvement_floor'])
    report={'initial_metric_slack':info['initial_metric_slack'],
        'primary_predicted_metric_slack':info['primary_predicted_metric_slack'],
        'primary_predicted_slack_improvement':info['primary_predicted_improvement'],
        'primary_box_normalized_step_infinity_norm':info['primary_box_normalized_norm'],
        'primary_block_normalized_step_infinity_norm':info['primary_block_normalized_norm'],
        'rho_out':info['rho_out'],'residual_source':'actual same y on both full grids',
        'Jacobian_source':'last accepted x; same original IDs; projected to154 only at LP assembly',
        'constant_cap_and_external_hard_not_restored_by_false_zero_J_rows':True}
    if model is None:
        report['proposal_rejected_before_LP']=info['status'];return None,report
    radius=model.radius;trial=model.active_trial_values
    report.update(metric_slack_budget=info['metric_slack_budget'],
        maximum_box_normalized_correction_infinity_norm=radius,
        body_correction_radius=radius,tail_correction_radius=radius/8,
        hard_margin_retention=float(Q(cfg['SOC_physical_margin_retention_exact'])),
        rows=len(model.b),variables=len(model.c),matrix_bytes=model.A.nbytes,
        metric_budget_applied_to_actual_trial_rows_plus_old_Jacobian_correction=True,
        selected_metric_actual_minus_primary_linear_minimum=float(np.min((trial-primary.active_values-primary.active_J@p[primary.subspace.columns])[primary.active_groups<2])))
    report.update(_proposal_floor_report(primary,cfg,trial=trial))
    started=time.monotonic()
    scaled=scale_correction_lp(model.A,model.b,model.lower,model.upper,radius)
    report['SOC_reversible_scaling']=scaled.definition()
    report['SOC_scaling_prepare_seconds']=time.monotonic()-started
    report['SOC_solver_tolerances_are_in_scaled_units_not_original_residual_units']=True
    started=time.monotonic()
    r=linprog(scaled.objective,A_ub=scaled.A,b_ub=scaled.b,bounds=list(zip(scaled.lower,scaled.upper)),method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    report.update(LP_invoked=True,success=bool(r.success),status=int(r.status),message=str(r.message),nit=int(r.nit),
        elapsed_seconds=time.monotonic()-started)
    report['SOC_solver_returned_finite_primal']=bool(r.x is not None and np.asarray(r.x).shape==scaled.objective.shape
        and np.all(np.isfinite(r.x)))
    report['SOC_original_unit_dual_diagnostics']=scaled.original_dual_diagnostics(r,
        np.r_[primary.active_groups,np.full(308,-2)])
    if not report['SOC_solver_returned_finite_primal']:return None,report
    x=scaled.to_original(r.x);w=primary.subspace.lift_step(primary.width*x[:154]);res=model.residual(x)
    report['SOC_original_and_scaled_residuals']=scaled.original_residuals(r.x)
    linear=primary.active_values+primary.active_J@p[primary.subspace.columns]
    hard=primary.active_groups>=2;soft=~hard;out=primary.information['rho_out'];Jw=primary.active_J@w[primary.subspace.columns]
    report.update(maximum_linear_row_violation=res['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=res['maximum_original_linear_bound_violation'],
        maximum_absolute_correction=float(np.max(abs(w))),correction_l2=float(np.linalg.norm(w)),
        correction_box_normalized_infinity_norm=float(np.max(abs(w[primary.subspace.columns])/primary.width)),
        correction_box_normalized_l1_norm=float(np.sum(abs(w[primary.subspace.columns])/primary.width)),
        correction_block_normalized_infinity_norm=float(np.max(abs(w[primary.subspace.columns])/(primary.width*primary.block_weights))),
        corrected_predicted_metric_slack=max(out,0.,float(np.max(-(linear+Jw)[soft]))),
        corrected_actual_trial_linear_metric_slack=max(out,0.,float(np.max(-(trial+Jw)[soft]))),
        basepoint_prediction_slack_is_only_for_parabolic_linear_bookkeeping=True,
        minimum_corrected_linear_hard_margin=float(np.min(trial[hard]+Jw[hard])) if np.any(hard) else None,
        corrected_affine_cap_margin=primary.information['cap_invariant']['affine_margin'])
    report.update(_proposal_floor_report(primary,cfg,trial=trial,linear=trial+Jw))
    if not r.success or max(res['maximum_original_linear_row_violation'],res['maximum_original_linear_bound_violation'])>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC LP status or original-unit residual';return None,report
    return w,report


def predicted_slack(primary,full_step):
    p=np.asarray(full_step,float)
    if np.any(p[primary.subspace.fixed_columns]!=0):raise ValueError('only the declared154 step is allowed')
    soft=primary.active_groups<2
    return max(primary.information['rho_out'],0.,float(np.max(-(primary.active_values+primary.active_J@p[primary.subspace.columns])[soft])))


def restricted_parabolic_candidate(subspace,current,p,w,alpha,reference_alpha):
    candidate,detail=parabolic_candidate(current,p,w,alpha,reference_alpha)
    # The established formula computes the moving entries; assignment preserves
    # all fixed bits, including negative zero, rather than adding zero to them.
    out=np.asarray(current,float).copy();out[subspace.columns]=candidate[subspace.columns]
    return out,detail


def run_restricted_recovery(objective,initial,*,known_metric_locations=(),restored_controller=None,artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,EntryTail154Objective):
        raise ValueError('the explicit adaptive spectral objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    restriction_definition(cfg)
    inherited_trust=float(Q(cfg['entry_tail154_initial_trust_exact']));growth_streak=0
    continuation={'restored_entry_body103_controller_not_inherited':copy.deepcopy(restored_controller),
        'new_restricted_initial_trust_exact':cfg['entry_tail154_initial_trust_exact'],
        'new_restricted_initial_success_streak':0,
        'initial_tail_radius_exact':'1/32000',
        'new_to_restored_radius_ratio_evaluated':None if not restored_controller else
            inherited_trust/float(restored_controller['trust_evaluated'])}
    objective.evaluation_definition['entry_tail154_controller_initialization']=continuation
    objective.evaluation_sha256=digest(objective.evaluation_definition)
    meta={'method':POLICY,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
        'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
        'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
        'nonlinear_minimize_invocation_count':0,'linear_program_invocation_count':0,
        'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'shared_max_LPs':cfg['max_linear_models'],'shared_max_values':cfg['max_physical_evaluations'],
        'shared_active_seconds':cfg['max_seconds'],'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'new_restricted_controller_initialization':continuation,
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    trust=inherited_trust
    def finish(status,error=None,budget=None):
        snap=objective.snapshot(); point=snap.get('selected_two_grid_physical_point')
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':meta,'checkpoint':snap,
            'new_metric_target_reached_on_both_grids':bool(point and point['new_metric_target_qualified_on_both_grids']),
            'adaptive_trust_policy':restricted_growth_definition(objective.cfg),
            'curvature_proposal_floor':floor_definition(objective.cfg),
            'primary_physical_step_cost':penalty_definition(objective.cfg),
            'conservative_trust_growth':restricted_growth_definition(objective.cfg),
            'strip_proposal_floor':strip_floor_definition(objective.cfg),
            'SOC_reversible_scaling':scaling_definition(objective.cfg),
            'entry_tail154':restriction_definition(objective.cfg),
            'initial_fixed_domain_and_height_diagnostic':copy.deepcopy(objective.restricted_initial_diagnostic),
            'last_pre_LP_decision':copy.deepcopy(meta.get('last_pre_LP_decision')),
            'last_restricted_trust':trust,
            'final_consecutive_growth_qualifying_models':growth_streak,
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    def update_model_scale(model,proposed):
        nonlocal growth_streak
        radius,growth_streak,feedback=next_restricted_trust(model,proposed,growth_streak,cfg)
        model['scale_feedback_update']=feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius
    try:
        initial=np.asarray(initial,float).copy()
        current=initial.copy(); vector=objective.vector(current)
        cd=objective.evaluate(vector)['decision']; fd=objective.fine_decision(current)
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        accepted=objective.accepted_point(current,cd,fd,{'kind':'temporary-restored103-two-grid-success-entry-tail154-start'})
        objective.install_reference(current)
        if not len(objective.pool):objective.initialize_pool(vector)
        objective.expand_pool(vector,'initial-soft-metric-envelope-and-hard-coarse-separation')
        objective.initialize_fine_pool(current,known_metric_locations=known_metric_locations)
        initial_summary=fixed_domain_summary(objective.subspace,objective.full_views(current))
        initial_flags={name:compact_with_all_actual_gates(d)['actual_gate_booleans']
            for name,d in [('coarse',cd),('fine',fd)]}
        preflight=initial_restriction_decision(initial_summary,initial_flags,
            new_target_qualified=bool(accepted['new_metric_target_qualified_on_both_grids']),
            minimum_drop_exact=cfg['minimum_accepted_eta_decrease_exact'],
            target_exact=cfg['fixed_metric_budget_exact'],actual_eta_tolerance=cfg['direct_eta_tolerance'])
        meta['initial_pre_LP_decision']=preflight;meta['last_pre_LP_decision']=preflight
        if evaluate_only:return finish('evaluation-only-restricted-initialization')
        if not preflight['may_call_LP']:return finish(preflight['status'])
        if accepted['new_metric_target_qualified_on_both_grids']:return finish('new-metric-target-already-qualified')
        objective.linear_rows(vector); objective.begin_optimization()
        trust=inherited_trust
        minimum_trust=float(Q(cfg['minimum_trust_box_fraction_exact']))
        drop=float(Q(cfg['minimum_accepted_eta_decrease_exact']))
        if trust<minimum_trust:return finish('new-restricted-controller-below-original-minimum-trust')
        while meta['linear_program_invocation_count']<cfg['max_linear_models']:
            objective._wall(); vector=objective.vector(current)
            # A rejected trial may own the latest caches. Restore the accepted
            # value caches first; an already cached accepted state costs no call.
            # A fixed outside maximum exits before constructing another J.
            objective.evaluate(vector);objective.fine_decision(current)
            current_summary=fixed_domain_summary(objective.subspace,objective.full_views(current))
            flags={name:compact_with_all_actual_gates(d)['actual_gate_booleans'] for name,d in
                [('coarse',objective.epigraph_cache['record']['decision']),('fine',objective.fine_cache['decision'])]}
            preflight=initial_restriction_decision(current_summary,flags,
                new_target_qualified=bool(accepted['new_metric_target_qualified_on_both_grids']),
                minimum_drop_exact=cfg['minimum_accepted_eta_decrease_exact'],
                target_exact=cfg['fixed_metric_budget_exact'],actual_eta_tolerance=cfg['direct_eta_tolerance'])
            meta['last_pre_LP_decision']=preflight
            if not preflight['may_call_LP']:return finish(preflight['status'])
            base,J,groups,tols=objective.linear_rows(vector)
            versions=(objective.pool_version,objective.fine_pool_version)
            remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
            primary=selected_model(objective,current,base,J,groups,tols,trust,local)
            p,lp=solve_primary(primary,local)
            meta['linear_program_invocation_count']+=1; meta['primary_LP_invocation_count']+=1
            model={'number':len(meta['models'])+1,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'coarse_pool_version':versions[0],'fine_pool_version':versions[1],
                'trust_before_model':trust,'scale_feedback_trials':[],
                'linear_program':lp,'trials':[],'corrections':[]}; meta['models'].append(model);objective._wall()
            if p is None:
                trust*=.5;model['result']='primary-LP-failed-trust-shrunk'
                trust=update_model_scale(model,trust)
                if trust<minimum_trust:return finish('minimum-trust-after-primary-failure')
                continue
            if lp['predicted_slack_improvement']<=cfg['linear_model_improvement_floor'] or np.max(abs(p))==0:
                model['result']='no-primary-metric-restoration';return finish('metric-restoration-linear-model-stalled')
            model['exact_binary64_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_eta=accepted['maximum_eta_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None
            def assess(candidate,kind,alpha,need_fine=False,curve=None,prediction=None,curvature_reference=None):
                nonlocal current,accepted,succeeded,relearned
                if candidate[objective.subspace.fixed_columns].tobytes()!=initial[objective.subspace.fixed_columns].tobytes():
                    raise ArithmeticError('candidate changed fixed9 bits before geometry')
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                if curve is not None:record['parabolic_curve']=copy.deepcopy(curve)
                model['trials'].append(record)
                rv=objective.evaluate(objective.vector(candidate)); c=rv['decision']
                record.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=rv['physical_geometry_evaluation'],coarse_decision=compact_with_all_actual_gates(c))
                possible=c['direct_max_eta']<old_eta and (
                    old_eta-c['direct_max_eta']>=drop or c['single_grid_new_target_qualified'])
                f=None
                if c.get('regularity_screen_pass',False) and (need_fine or (possible and c['single_grid_admissible_recovery_point'])):
                    f=objective.fine_decision(candidate)
                    record.update(fine_value_evaluation=objective.fine_evaluations,fine_decision=compact_with_all_actual_gates(f),
                        actual_fine_evaluated_even_if_coarse_ineligible=not c['single_grid_admissible_recovery_point'])
                    maximum=max(c['direct_max_eta'],f['direct_max_eta'])
                    qualified=c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified']
                    if (c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point']
                            and maximum<old_eta and (old_eta-maximum>=drop or qualified)):
                        accepted=objective.accepted_point(candidate,c,f,{'kind':kind,'model':model['number'],
                            'alpha_exact':alpha,'previous_two_grid_maximum_eta':old_eta})
                        current=candidate.copy();succeeded=True
                        record.update(accepted_as_next_iterate=True,accepted_index=accepted['accepted_index'])
                record['restricted_support_invariants']=objective.invariant_diagnostic(candidate,fine_present=f is not None)
                # Values and forms are already cached at this exact candidate.
                # Capture before any learned row changes the pool indexing.
                reference=(base,vector[:-1],'accepted-basepoint-plus-J-total-step') if curvature_reference is None else curvature_reference
                record['curvature_nonlinear_defect_diagnostic']=curvature_trial_diagnostics(
                    objective,candidate,reference[0],J,groups,reference[1],reference[2],fine_present=f is not None)
                added,detail=objective.expand_pool(objective.vector(candidate),'recovery-coarse-actual-hard-and-soft-envelope')
                record.update(coarse_omitted_rows=detail['omitted_violating_count'],
                    coarse_omitted_hard_rows=detail['omitted_hard_violating_count'],
                    new_coarse_rows=len(added['added_row_indices']) if added else 0)
                if detail.get('pool_capacity_would_be_exceeded'):
                    raise EvaluationBudgetReached('coarse row capacity; last accepted metric point retained')
                relearned=relearned or bool(added)
                if f is not None:
                    addf,detailf=objective.learn_fine_violations(candidate,'recovery-fine-hard-and-soft-envelope')
                    record.update(fine_omitted_rows=detailf['omitted_violating_count'],
                        fine_omitted_hard_rows=detailf['omitted_hard_violating_count'],
                        fine_violation_groups=detailf['group_counts'],
                        new_fine_rows=len(addf['added_row_indices']) if addf else 0)
                    if detailf.get('pool_capacity_would_be_exceeded'):
                        raise EvaluationBudgetReached('fine row capacity; last accepted metric point retained')
                    relearned=relearned or bool(addf)
                quality=trial_quality(old_eta,c,f,prediction,kind,cfg)
                record['scale_feedback']=quality;model['scale_feedback_trials'].append(quality)
                return c,f,record
            for bi in range(int(cfg['maximum_backtracks_per_model'])):
                alpha=str(Q(1,2**bi)); step=float(Q(alpha))*p
                may_soc=arc is None and not soc_used and meta['linear_program_invocation_count']<cfg['max_linear_models']
                if arc is None:y=objective.subspace.apply(current,step[objective.subspace.columns]);kind='primary-metric-short-step';curve=None
                else:
                    y,curve=restricted_parabolic_candidate(objective.subspace,current,p,arc['w'],alpha,arc['reference_alpha_exact'])
                    curve.update(correction_index=arc['correction_index'],
                        linear_metric_slack_upper_bound=max(primary.information['rho_out'],curvature_arc_slack_bound(
                            arc['initial'],arc['primary'],arc['corrected'],float(Q(curve['curve_fraction_exact'])))))
                    kind='metric-SOC-parabolic-backtrack'
                predicted=(predicted_slack(primary,step) if arc is None
                    else curve['linear_metric_slack_upper_bound'])
                prediction={'predicted_slack':predicted,
                    'model_kind':'basepoint-plus-J-step' if arc is None else 'parabolic-basepoint-linear-bound',
                    'pool_versions':list(versions),'full_fine_actual_required_for_eta_ratio':True}
                c,f,trial=assess(y,kind,alpha,may_soc,curve,prediction)
                if succeeded:model['result']='accepted-two-grid-true-metric-descent';break
                if relearned:model['result']='new-rows-return-to-last-accepted-before-SOC';break
                if may_soc and f is not None and c.get('regularity_screen_pass',False) and f.get('regularity_screen_pass',False):
                    soc_used=True
                    if versions!=(objective.pool_version,objective.fine_pool_version):
                        raise ArithmeticError('SOC old Jacobian cannot survive pool layout change')
                    trial_rows=np.r_[objective.constraint_fun(objective.vector(y)),
                        objective.fine_rows(y).reshape(-1)[objective.fine_pool]]
                    remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
                    local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
                    w,soc=solve_correction(primary,objective.full_views(y),step,local)
                    if soc.get('LP_invoked'):
                        meta['linear_program_invocation_count']+=1;meta['correction_LP_invocation_count']+=1
                    correction={'primary_trial_index':len(model['trials'])-1,
                        'primary_trial_physical_sha256':digest(objective.problem.identity(y)),
                        'coarse_residual_evaluation':trial['coarse_physical_evaluation'],
                        'fine_residual_evaluation':trial['fine_value_evaluation'],
                        'coarse_pool_version':versions[0],'fine_pool_version':versions[1],'linear_program':soc}
                    model['corrections'].append(correction);objective._wall()
                    if w is not None:
                        correction['exact_binary64_correction']=[str(Q.from_float(float(x))) for x in w]
                        arc={'w':w.copy(),'reference_alpha_exact':alpha,'correction_index':len(model['corrections'])-1,
                            'initial':soc['initial_metric_slack'],'primary':soc['primary_predicted_metric_slack'],
                            'corrected':soc['corrected_predicted_metric_slack']}
                        assess(objective.subspace.apply(y,w[objective.subspace.columns]),'metric-SOC-corrected-short-step',alpha,
                            prediction={'predicted_slack':soc['corrected_actual_trial_linear_metric_slack'],
                                'model_kind':'same-actual-y-rows-plus-J-correction',
                                'pool_versions':list(versions),'full_fine_actual_required_for_eta_ratio':True},
                            curvature_reference=(trial_rows,y.copy(),'same-primary-y-actual-rows-plus-old-J-correction'))
                        if succeeded:model['result']='accepted-full-SOC-two-grid-metric-descent';break
                        if relearned:model['result']='corrected-new-rows-return-to-last-accepted';break
            if succeeded and accepted['new_metric_target_qualified_on_both_grids']:
                return finish('fixed-new-metric-target-qualified-on-both-grids')
            original_minimum_reached=False
            if not succeeded and not relearned:
                trust*=.5;model['result']='all-proposals-rejected-last-accepted-retained'
                original_minimum_reached=trust<minimum_trust
            trust=update_model_scale(model,trust)
            if trust<minimum_trust:return finish('minimum-trust-after-SOC-and-backtracking' if original_minimum_reached
                else 'minimum-trust-after-actual-model-quality-feedback')
            if objective.checkpoint:objective.checkpoint(objective.snapshot())
        return finish('shared-primary-plus-SOC-LP-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-value-time-or-pool-budget-exit',budget=str(error))
    except Exception as error:
        return finish('entry-tail154-recovery-error',error={'type':type(error).__name__,'message':str(error)})




class _TwoBlockArrayObjective(EntryTail154Objective):
    """New tiny array interface, never an actual surface."""
    from frame_metric_entry_body103 import _RestrictedArrayObjective as _OldFixture
    _wall=_OldFixture._wall
    evaluate=_OldFixture.evaluate
    fine_decision=_OldFixture.fine_decision
    row_tolerances=_OldFixture.row_tolerances
    initialize_pool=_OldFixture.initialize_pool
    initialize_fine_pool=_OldFixture.initialize_fine_pool
    expand_pool=_OldFixture.expand_pool
    learn_fine_violations=_OldFixture.learn_fine_violations
    begin_optimization=_OldFixture.begin_optimization
    constraint_fun=_OldFixture.constraint_fun
    fine_rows=_OldFixture.fine_rows
    accepted_point=_OldFixture.accepted_point
    snapshot=_OldFixture.snapshot

    def __init__(self,cfg,*,curved=False,fail_after=None):
        self._OldFixture.__init__(self,cfg,curved=curved,fail_after=fail_after)
        self.subspace=EntryTail154Subspace(expected_layout())
        nodes=['0','9/250','9/100','99/500','33/50','153/200','309/400','423/500','9/10']
        self.row_grids=[RationalRowGrid('coarse',nodes,4),RationalRowGrid('fine',nodes,8)]
        self.radial=np.array([float(Q(v)) for v in nodes])
        self.pool=np.arange(self.row_grids[0].total_rows)
        self.fine_pool=np.arange(self.row_grids[1].total_rows)
        self.original_pool_rows=(len(self.pool),len(self.fine_pool))

    def _data(self,state,grid):
        data,rows,decision=self._OldFixture._data(self,state,grid)
        # Both entry/body and formerly frozen .7725 tail must improve.
        data['eta'][6]=.2667-state[54]
        rows[0,6]=float(Q(self.cfg['fixed_metric_budget_exact']))-data['eta'][6]
        rows[4:6,6]=.1
        data['X'][6,:,0]=state[54]
        data['e']=data['eta'].copy()
        decision['direct_max_eta']=float(np.max(data['eta']))
        decision['single_grid_new_target_qualified']=bool(decision['direct_max_eta']<=
            float(Q(self.cfg['fixed_metric_budget_exact']))+self.cfg['direct_eta_tolerance']
            and decision['independent_direct_curvature_pass'])
        return data,rows,decision

    def linear_rows(self,vector):
        values,J,groups,tols=self._OldFixture.linear_rows(self,vector)
        offset=0
        for grid in self.row_grids:
            J[offset+6*grid.nt:offset+7*grid.nt,54]=1.
            offset+=grid.total_rows
        self.last_full_J_shape=J.shape
        return values,J,groups,tols


def developer_check():
    """Only new block maps and controller/fixture interactions, not old suites."""
    from frame_entry_tail_blocks import developer_check as block_check
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(recovery_configuration(start_configuration(),target='13/50',curvature_cap='58'))
    cfg.update(max_linear_models=1,max_physical_evaluations=40,max_seconds=30.,linear_program_seconds=2.)
    state=np.zeros(163);state[154]=-0.;state[162]=.125
    obj=_TwoBlockArrayObjective(cfg)
    result=run_restricted_recovery(obj,state,artificial_inputs_only=True)
    point=result['checkpoint']['selected_two_grid_physical_point']
    final=np.asarray(point['physical_parameter_coefficients_binary64'])
    model=result['solver']['models'][0];cost=model['linear_program']['primary_step_cost_diagnostic']
    flags=model['trials'][0]
    # A single new fixture SOC uses the same y caches and both blocks' columns.
    curved=_TwoBlockArrayObjective(dict(cfg,max_linear_models=2),curved=True)
    soc=run_restricted_recovery(curved,state,artificial_inputs_only=True)
    corrections=[v for m in soc['solver']['models'] for v in m['corrections']]
    bad=_TwoBlockArrayObjective(cfg,fail_after=1)
    failed=run_restricted_recovery(bad,state,artificial_inputs_only=True)
    p=np.zeros(163);w=np.zeros(163);p[0]=.01;p[54]=.001;w[54]=-.0001
    arc,detail=restricted_parabolic_candidate(obj.subspace,state,p,w,'1/2','1')
    checks={
        'one_new_model_can_move_body_and_previously_fixed_tail':bool(final[0]>0 and final[54]>0
            and result['solver']['linear_program_invocation_count']==1 and len(result['checkpoint']['accepted_iterates'])==2),
        'nine_height_bits_preserved_on_primary_and_parabolic_paths':bool(
            final[154:].tobytes()==state[154:].tobytes() and arc[154:].tobytes()==state[154:].tobytes()),
        'tail_block_use_drives_growth_norm_not_physical_norm':bool(cost['actual_trust_normalized_step_norm']>=.999
            and cost['tail_utilization']>=.999 and cost['actual_physical_box_normalized_step_norm']<cost['actual_block_box_normalized_step_norm']),
        'same_original_complete_actual_gate_fields_required':bool(flags['accepted_as_next_iterate']
            and all(flags[k]['actual_gate_booleans'][v] for k in ['coarse_decision','fine_decision'] for v in ACTUAL_FLAGS)),
        'full_J_and_original_row_ID_layout_not_reduced_to154':obj.last_full_J_shape[1]==163,
        'SOC_new_block_projection_has308_original_aux_rows':bool(corrections and
            corrections[0]['linear_program']['variables']==308 and
            corrections[0]['linear_program']['SOC_solver_returned_finite_primal']),
        'new_value_failure_keeps_original_accepted_state':bool(failed['error'] and
            np.asarray(failed['checkpoint']['selected_two_grid_physical_point']['physical_parameter_coefficients_binary64']).tobytes()==state.tobytes()),
        'no_false_equivalence_to_old_fullspace_or_old103_domains':bool(scaling_definition(cfg)['not_equivalence_to_the_old_full163_primary_or_SOC_feasible_set']
            and scaling_definition(cfg)['new_SOC_radius_uses_weighted_primary_norm_explicitly']),
        'new_tail_minimum_is_explicit_not_old_uniform_minimum':restriction_definition(cfg)['derived_minimum_tail_radius_exact']=='1/819200'}
    arrays=block_check();checks['new_block_array_checks_passed']=arrays['passed']
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema':POLICY+'-targeted-development','passed':all(checks.values()),'checks':checks,
        'source_files_sha256':implementation_hashes(),'array_checks':arrays,
        'primary_result_status':result['status'],'SOC_result_status':soc['status'],
        'primary_block_cost':cost,'SOC_linear_program':corrections[0]['linear_program'] if corrections else None,
        'actual_research_geometry_or_old_development_suite_run':False}


def artificial_single_Q_cache_check():
    """Actual class APIs on a newly specified small artificial ellipse; no solve."""
    from frame_collar_bvp import EllipticCylinderPort,NegativeKRadialSeed,FrameCollarProblem
    from frame_collar_enriched import make_enriched
    from frame_collar_natural_body_audit import NaturalBodyProblem
    from frame_independent_height import IndependentHeightProblem
    from frame_entry_paired_repair import EntryRepairProblem
    from frame_entry_bounded_height import BoundedEntryHeightProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    core=EllipticCylinderPort('9/10','18/25','1/50',1)
    seed=NegativeKRadialSeed.from_core(core,'9/10','11/50')
    baseline=FrameCollarProblem(core,seed,radial_free=4,angular_modes=5,
        ellipse_envelope=(core.major,core.minor),height_limit=.45,radial_nodes=9,
        angular_nodes=8,radial_quadrature_order=2)
    old=make_enriched(baseline,9,3,9,8,2,strip_half_width='3/4')
    c0=.0002*np.sin(np.arange(old.nunknown)+.3)
    source=NaturalBodyProblem(old,c0,metric_free=2,heat_order=4,
        radial_nodes=9,angular_nodes=8,quadrature_order=2,strip_half_width='3/4')
    un=IndependentHeightProblem(source,9,height_angular_nodes=8)
    un,state=un.frozen_metric_copy(un.initial_state())
    paired=EntryRepairProblem(un,state,'81/1000',entry_mean_nodes=16,uniform_panels=4,primitive_order=2)
    bounded=BoundedEntryHeightProblem(paired,state,uniform_panels=4,primitive_order=2)
    p=SingleQProblem(bounded);state=p.lift_state(state)
    nodes=['0','9/250','9/100','117/1000','33/50','153/200','309/400','423/500','9/10']
    radial=np.array([float(Q(x)) for x in nodes]);theta=np.arange(8)*np.pi/4
    data=p.geometry(state,radial,theta,2)
    gate=HeightAffineGate.from_frozen_problem(p,state,data)
    cfg=configuration(recovery_configuration(start_configuration(),target='13/50',curvature_cap='58'))
    lower=np.full(163,-8.);upper=np.full(163,8.)
    lower[p.slices['height']]=-1.;upper[p.slices['height']]=1.
    objective=EntryTail154Objective(p,gate,radial,theta,2,lower,upper,
        cfg=cfg,radial_nodes_exact=nodes)
    objective.evaluate(objective.vector(state));objective.fine_decision(state)
    counts=(objective.geometry_evaluations,objective.fine_evaluations)
    views=objective.full_views(state);summary=objective.install_reference(state)
    objective.invariant_diagnostic(state,fine_present=True)
    unchanged=(counts==(objective.geometry_evaluations,objective.fine_evaluations))
    delta=np.zeros(154);delta[54]=1e-5;delta[129]=-1e-5
    moved=objective.subspace.apply(state,delta)
    objective.evaluate(objective.vector(moved));objective.fine_decision(moved)
    invariant=objective.invariant_diagnostic(moved,fine_present=True)
    moved_data=objective.geometry_cache
    tail_index=nodes.index('309/400')
    tail_changed=float(np.max(abs(moved_data['X'][tail_index]-data['X'][tail_index])))>0
    objective.evaluate(objective.vector(state));objective.fine_decision(state)
    saved=objective.fine_cache['state'].copy();objective.fine_cache['state'][0]+=1e-5
    try:objective.full_views(state);bad=False
    except ValueError:bad=True
    objective.fine_cache['state']=saved
    checks={'actual_SingleQ_layout_derived_from_real_metadata':layout_from_problem(p)==expected_layout(),
        'coarse_epigraph_vector_and_geometry_state_bound':bool(
            np.array_equal(objective.epigraph_cache['vector'][:-1],state)
            and np.array_equal(objective.geometry_cache['state'],state)),
        'fine_state_and_data_bound':bool(np.array_equal(objective.fine_cache['state'],state)),
        'height_b_and_Xs_read_from_actual_geometry':bool(all(v.b.shape==(len(radial),)
            and v.mean_Xs.shape==(len(radial),3) for v in views)),
        'full_views_and_invariant_diagnostics_make_no_value_calls':unchanged,
        'mismatched_real_fine_cache_rejected':bad,
        'outside_and_height_summary_finite':bool(np.isfinite(summary['full_true_eta'])),
        'new_tail_columns_change7725_but_keep_core_tail_sixjets_and_height':bool(tail_changed and all(
            max(g['outside_six_jet_max_difference'].values())==0
            and max(g['outside_metric_jet_max_difference'].values())==0
            and g['full_common_center_max_difference']==0
            and max(g['full_fixed_height_jet_max_difference'].values())==0 for g in invariant['grids'].values()))}
    return {'passed':all(checks.values()),'checks':checks,
        'artificial_core_exact':{'A':'9/10','B':'18/25','L':'9/10'},
        'artificial_anchor_amplitude_evaluated':0.0002,
        'artificial_anchor_formula':'0.0002*sin(arange(n)+0.3); no research report is read',
        'full_value_grid_sizes':[[len(radial),8],[len(radial),16]],
        'cached_complete_value_counts':list(counts),'optimization_invocations':0,
        'research_candidate_constructed_or_evaluated':False}
