#!/usr/bin/env python3
"""One new proposal representation: 154 tangent coordinates plus five exact null heights.

The physical family, permanent anchor, fixed g and b0, all original complete-grid
gates and the shared12LP/40value/120s budget are retained. Only the proposal
space, its coupled physical boxes and the new height radius are changed here.
No change to the inherited new-soft-row-before-SOC return policy is made.
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

from frame_height_null_coordinates import digest
from frame_five_height_field import FiveHeightField
from frame_height_null_gate import FiveNullHeightGate
from frame_entry_tail_height_blocks import (
    EntryTailHeight159Subspace,SelectedMappedRows,RationalRowGrid,FullGridValues,
    ConstantCapGate,initial_restriction_decision,fixed_domain_summary,
    build_primary,build_correction,primary_independent_step,correction_independent_step,
    predicted_slack,scale_mapped_correction,N,P)
from frame_metric_entry_tail154 import (
    configuration as old154_configuration,implementation_hashes as old154_hashes,
    layout_from_problem,EntryTail154Objective,
    _proposal_floor_report as inherited_proposal_floor_report)
from frame_metric_spectral_soc_scaling import (
    SOCScaledSpectralMetricObjective,compact_with_all_actual_gates,curvature_trial_diagnostics)
from frame_metric_spectral_strip_reserve import strip_floor_definition
from frame_metric_spectral_curvature_reserve import floor_definition
from frame_metric_spectral_adaptive import trial_quality,next_trust as shrink_next_trust
from frame_metric_budget_recovery import (
    EvaluationBudgetReached,require_public_research_environment,parabolic_candidate,
    curvature_arc_slack_bound)

POLICY='same-g-entry-tail159-five-null-height-spectral-step-v1'
POSITION_JETS=('X','Xs','Xt','Xss','Xst','Xtt')


def implementation_hashes():
    out=old154_hashes()
    for name in ['frame_height_null_coordinates.py','frame_five_height_field.py',
            'frame_height_null_gate.py','frame_entry_tail_height_blocks.py',Path(__file__).name]:
        out[name]=hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
    return out


def configuration(base):
    cfg=old154_configuration(base)
    old={k:cfg.pop(k) for k in list(cfg) if k.startswith('entry_tail154_')}
    cfg.update(entry_tail159_policy=POLICY,
        entry_tail159_body_and_tail_controller_inherited_from_this_run154=True,
        entry_tail159_height_to_body_radius_ratio_exact='4',
        entry_tail159_tail_to_body_radius_ratio_exact='1/8',
        entry_tail159_maximum_body_radius_exact=old['entry_tail154_maximum_trust_exact'],
        entry_tail159_effective_total_eta_drop_reference_exact='1/10000',
        entry_tail159_reference_drop_is_diagnostic_not_an_acceptance_gate=True,
        complete_physical_family_parameter_count=163,independent_coordinate_count=159,
        original_geometry_163_J_still_computed_before_new159_columns_are_returned=True,
        source154_controller_configuration=old,
        no_new_soft_return_policy_change=True)
    return cfg


def restriction_definition(cfg):
    if cfg.get('entry_tail159_policy')!=POLICY:
        raise ValueError('explicit five-null-height proposal configuration required')
    if (Q(cfg['entry_tail159_height_to_body_radius_ratio_exact'])!=4
            or Q(cfg['entry_tail159_tail_to_body_radius_ratio_exact'])!=Q(1,8)
            or Q(cfg['entry_tail159_maximum_body_radius_exact'])!=Q(1,4000)):
        raise ValueError('declared inherited B/T cap or new H/B radius changed')
    return {'schema':POLICY+'-definition','physical_parameter_count':163,'independent_coordinate_count':159,
        'tangent_coordinates':list(range(154)),'height_null_coordinates':list(range(154,159)),
        'height_map':'three entry-to-c3 compensation columns and two c6/c7-to-c8 compensation columns',
        'physical_height_coefficients_are_exact_reference_plus_rational_H_times_binary64_tau':True,
        'new_height_to_body_radius_exact':'4','inherited_tail_to_body_radius_exact':'1/8',
        'inherited_maximum_body_radius_exact':cfg['entry_tail159_maximum_body_radius_exact'],
        'inherited_minimum_body_radius_exact':cfg['minimum_trust_box_fraction_exact'],
        'restoration_below_original_minimum_exits_without_hidden_reset':True,
        'all_nine_original_height_boxes_are_coupled_exact_affine_conditions':True,
        'primary_cost':'rho+.001*norm_infinity(Dphysical^-1 M p)',
        'SOC_cost':'norm1(Dphysical^-1 M w)',
        'SOC_common_body_radius':'.5*max(N_B,8*N_T,N_H/4) of the actual primary displacement',
        'cap_height_row_constant_by_exact_integral_null_original_tolerance_retained':True,
        'complete_coarse_fine_values_and_all_original_gates_unchanged':True,
        'interior_zero_Jacobian_rows_kept_exterior_soft_aggregated':True,
        'new_soft_row_before_SOC_return_behavior_unchanged':True,
        'effective_total_drop_reference_exact':cfg['entry_tail159_effective_total_eta_drop_reference_exact'],
        'reference_is_diagnostic_not_an_acceptance_threshold':True}


def penalty_definition(cfg):
    restriction_definition(cfg)
    return {'schema':POLICY+'-physical-cost',
        'coefficient_exact':cfg['step_cost_physical_box_norm_coefficient_exact'],
        'primary':'rho+coefficient*norm_inf(Dphysical^-1 M delta_q)',
        'SOC':'norm1(Dphysical^-1 M correction_q)',
        'five_height_tau_norm_never_substituted_for_nine_physical_coefficient_norm':True,
        'no_second_cost_LP_is_added':True}


def scaling_definition(cfg):
    restriction_definition(cfg)
    return {'schema':POLICY+'-mapped-SOC-scaling',
        'scope':'already assembled159 independent correction plus163 physical absolute auxiliaries',
        'positive_common_factor':'rH_c=4*rB_c multiplies all322 variables',
        'scalar_affine_rows_divided_by_positive_powers_of_two':True,
        'original_unit_LP_status_and_residual_gate_remain_authoritative':True,
        'new_scaled_solver_path_is_not_claimed_identical_to_old_float_solver':True,
        'not_equivalence_to_old154_SOC_or_old_full163_proposal_domains':True,
        'all_actual_geometry_gates_and_shared_time_budget_unchanged':True}


def growth_definition(cfg):
    restriction_definition(cfg)
    return {'schema':POLICY+'-inherited-B-controller',
        'initial_B_radius_and_success_streak':'actual completed/unfinished controller state from this run154 prefix',
        'H_radius_exact_multiplier':'4','T_radius_exact_multiplier':'1/8',
        'maximum_B_radius_exact':cfg['entry_tail159_maximum_body_radius_exact'],
        'minimum_B_radius_exact':cfg['minimum_trust_box_fraction_exact'],
        'consecutive_models':cfg['trust_growth_required_consecutive_models'],
        'complete_ratio_threshold_exact':cfg['trust_growth_minimum_complete_ratio_exact'],
        'norm_fraction_threshold_exact':cfg['trust_growth_minimum_actual_norm_fraction_exact'],
        'growth_factor_exact':cfg['trust_growth_factor_exact'],
        'old_actual_quality_and_curvature_failure_shrink_priority':True,
        'growth_requires_first_full_primary_no_SOC_no_backtrack_no_new_rows':True,
        'height_step_counts_through_the_weighted_physical_block_norm':True,
        'at_most_one_update_per_model':True}


def next_mapped_trust(model,current_trust,streak,cfg):
    growth_definition(cfg)
    if type(streak) is not int or not 0<=streak<2:raise ValueError('declared bounded success streak required')
    before=float(model['trust_before_model'])
    after,old=shrink_next_trust(before,current_trust,model.get('scale_feedback_trials',[]),cfg)
    trials=model.get('trials',[]);first=trials[0] if len(trials)==1 else {}
    quality=first.get('scale_feedback',{});ratio=quality.get('actual_to_predicted_ratio')
    norm=model.get('linear_program',{}).get('primary_step_cost_diagnostic',{}).get('actual_trust_normalized_step_norm')
    checks={
        'first_only_full_primary_accepted':bool(len(trials)==1 and first.get('kind')=='primary-metric-short-step'
            and first.get('alpha_exact')=='1' and first.get('accepted_as_next_iterate') is True
            and model.get('result')=='accepted-two-grid-true-metric-descent'),
        'no_SOC_or_backtrack':bool(not model.get('corrections') and len(trials)==1),
        'complete_actual_two_grid_gates':bool(quality.get('full_two_grid_actual_available')
            and first.get('coarse_decision',{}).get('single_grid_admissible_recovery_point')
            and first.get('fine_decision',{}).get('single_grid_admissible_recovery_point')),
        'valid_high_complete_ratio':bool(quality.get('ratio_denominator_usable') and ratio is not None
            and np.isfinite(ratio) and ratio>=float(Q(cfg['trust_growth_minimum_complete_ratio_exact']))),
        'actual_step_uses_radius':bool(norm is not None and np.isfinite(norm)
            and norm>=float(Q(cfg['trust_growth_minimum_actual_norm_fraction_exact']))),
        'no_new_coarse_or_fine_rows':bool(trials and all(t.get('new_coarse_rows')==0
            and t.get('new_fine_rows')==0 for t in trials)),
        'old_shrink_not_requested_or_applied':bool(after==before and current_trust==before
            and not old['trigger_trial_indices'])}
    qualified=all(checks.values());count=streak+1 if qualified else 0
    cap=float(Q(cfg['entry_tail159_maximum_body_radius_exact']));radius=after;grew=False;at_cap=False
    if count==2:
        radius=min(after*float(Q(cfg['trust_growth_factor_exact'])),cap)
        if radius<after:raise ValueError('inherited B radius exceeds its existing cap')
        grew=radius>after;at_cap=not grew;count=0
    report=copy.deepcopy(old)
    report.update(next_trust=radius,trust_after_unchanged_shrink_rule=after,
        inherited_radius_is_body_block=True,next_tail_radius=radius/8,next_height_radius=4*radius,
        conservative_growth={'streak_before':streak,'streak_after':count,'qualifying_model':qualified,
            'checks':checks,'failed_conditions':[k for k,v in checks.items() if not v],
            'complete_ratio':ratio,'actual_step_norm_over_radius':norm,
            'new_coarse_rows':sum(int(t.get('new_coarse_rows',0)) for t in trials),
            'new_fine_rows':sum(int(t.get('new_fine_rows',0)) for t in trials),
            'grew_for_next_model':grew,'qualified_pair_at_cap':at_cap,
            'inherited_cap_evaluated':cap,'old_shrink_has_priority':True,
            'input_model_and_trials_not_modified':True})
    return radius,count,report


class EntryTailHeight159Objective(SOCScaledSpectralMetricObjective):
    def __init__(self,problem,gate,radial,theta,order,lower,upper,*,radial_nodes_exact,cfg,checkpoint=None):
        if not isinstance(problem,FiveHeightField) or not isinstance(gate,FiveNullHeightGate):
            raise ValueError('explicit exact field and null-height physical gate are required')
        if not np.array_equal(lower,gate.coordinate_lower) or not np.array_equal(upper,gate.coordinate_upper):
            raise ValueError('declared necessary pivot envelope required for inherited numerical container')
        self.physical_lower=gate.original_lower;self.physical_upper=gate.original_upper
        super().__init__(problem,gate,radial,theta,order,lower,upper,cfg=cfg,checkpoint=checkpoint)
        self.subspace=EntryTailHeight159Subspace(
            layout_from_problem(problem.original_problem),problem.coordinates)
        self.row_grids=[RationalRowGrid('coarse',radial_nodes_exact,len(self.theta)),
            RationalRowGrid('fine',radial_nodes_exact,len(self.fine_theta))]
        if any(not np.array_equal(np.array([float(t) for t in g.nodes]),self.radial) for g in self.row_grids):
            raise ValueError('exact support classification must bind the actual complete grids')
        if np.any(gate.row!=0):raise ValueError('mathematical null gate must be constant')
        self.restricted_reference=None;self.restricted_initial_diagnostic=None
        self.evaluation_definition.update(schema=POLICY+'-evaluation',
            complete_original_physical_parameter_count=P,independent_coordinate_count=N,
            physical_parameter_count=P,solver_parameter_count=N,
            exact_coordinate_definition=problem.coordinate_definition,
            necessary_coordinate_outer_bounds_not_original_box_replacements=True,
            all_original_physical_boxes_and_cap_checked_by_mapped_gate=True,
            primary_physical_step_cost=penalty_definition(cfg),
            entry_tail_height159=restriction_definition(cfg),
            adaptive_trust_policy=growth_definition(cfg),conservative_trust_growth=growth_definition(cfg),
            SOC_reversible_scaling=scaling_definition(cfg),
            source_files_sha256=implementation_hashes())
        self.evaluation_definition['fine_selected_Jacobian_definition']['height_mean_and_height_primitive_evaluation_unchanged']=False
        self.evaluation_definition['fine_selected_Jacobian_definition']['height_evaluation']='original immutable b0 primitive plus the same exact null-polynomial increment in every query'
        self.evaluation_sha256=digest(self.evaluation_definition)

    full_views=EntryTail154Objective.full_views
    constant_cap=EntryTail154Objective.constant_cap

    def _coordinate_record(self,state):
        return self.problem.state_record(state)

    def _capture_coarse(self):
        cache=self.epigraph_cache
        if cache is None:return
        record=cache['record'];number=record['physical_geometry_evaluation']
        if number in self.saved_coarse_trials:return
        state=cache['vector'][:-1]
        self.saved_coarse_trials[number]={
            'coarse_physical_evaluation':number,'physical_state_sha256':digest(self.problem.identity(state)),
            'independent_coordinates_binary64':state.tolist(),
            'exact_binary64_independent_coordinates':[str(Q.from_float(float(x))) for x in state],
            'exact_original_physical_coefficients':[str(x) for x in self.problem.coordinates.physical_exact(state)],
            'coordinate_definition_sha256':self.problem.coordinate_definition_sha256,
            'fixed_hard_curvature_cap_exact':self.cfg['fixed_hard_curvature_cap_exact'],
            'new_metric_target_exact':self.cfg['fixed_metric_budget_exact'],
            'decision':copy.deepcopy(record['decision'])}

    def fine_decision(self,state):
        try:return super().fine_decision(state)
        finally:
            # The inherited implementation records independent numbers under an
            # old generic name. Correct the representation label even on failure.
            for item in self.saved_fine_trials:
                values=item.pop('exact_binary64_physical_coefficients',None)
                if values is not None:
                    item['exact_binary64_independent_coordinates']=values
                    q=np.array([float(Q(x)) for x in values])
                    item['exact_original_physical_coefficients']=[
                        str(x) for x in self.problem.coordinates.physical_exact(q)]
                    item['coordinate_definition_sha256']=self.problem.coordinate_definition_sha256

    def accepted_point(self,state,coarse,fine,reason):
        point=super().accepted_point(state,coarse,fine,reason)
        point['independent_coordinates_binary64']=point.pop('physical_parameter_coefficients_binary64')
        point['exact_binary64_independent_coordinates']=point.pop('exact_binary64_physical_coefficients')
        point['exact_original_physical_coefficients']=[
            str(x) for x in self.problem.coordinates.physical_exact(state)]
        point['coordinate_definition_sha256']=self.problem.coordinate_definition_sha256
        return point

    def install_reference(self,state):
        self.restricted_initial_diagnostic=fixed_domain_summary(self.subspace,self.full_views(state))
        reference={'state':np.asarray(state,float).copy(),'grids':{}}
        for grid,data in [(self.row_grids[0],self.geometry_cache),(self.row_grids[1],self.fine_cache['data'])]:
            outside=np.array([not(self.subspace.left<t<self.subspace.right) for t in grid.nodes])
            reference['grids'][grid.label]={k:np.asarray(data[k])[outside].copy() for k in POSITION_JETS}
            reference['grids'][grid.label].update(
                metric={k:np.asarray(data['metric'][k]).copy() for k in ['a','a_s','a_ss']},
                center=np.asarray(data['center'])[outside].copy(),
                height={k:np.asarray(data['height'][k])[outside].copy() for k in ['b','b_s','b_ss']})
        self.restricted_reference=reference
        return self.restricted_initial_diagnostic

    def invariant_diagnostic(self,state,*,fine_present):
        if self.restricted_reference is None:raise ValueError('accepted initial reference required')
        q=self.problem.coordinates.validate(state)
        exact=self.problem.coordinates.exact_heights(q);ref=self.problem.coordinates.reference_exact
        conserved=sum(self.problem.null_basis.integrals[j]*(exact[j]-ref[j]) for j in range(9))
        unchanged=all(exact[j]==ref[j] for j in [4,5])
        if conserved!=0 or not unchanged:raise ArithmeticError('exact null/fixed height slots failed')
        result={'exact_total_height_integral_change':str(conserved),'physical_height_c4_c5_unchanged':unchanged,
            'all_nine_exact_height_coefficients':[str(x) for x in exact],
            'no_additional_geometry_call':True,'whole_grid_gates_still_required':True,'grids':{}}
        specs=[(self.row_grids[0],self.geometry_cache)]
        if fine_present:specs.append((self.row_grids[1],self.fine_cache['data']))
        for grid,data in specs:
            outside=np.array([not(self.subspace.left<t<self.subspace.right) for t in grid.nodes])
            refg=self.restricted_reference['grids'][grid.label]
            result['grids'][grid.label]={
                'outside_six_jet_max_difference':{k:float(np.max(abs(np.asarray(data[k])[outside]-refg[k]))) for k in POSITION_JETS},
                'full_frozen_metric_jet_max_difference':{k:float(np.max(abs(np.asarray(data['metric'][k])-refg['metric'][k])))
                    for k in ['a','a_s','a_ss']},
                'outside_common_center_max_difference':float(np.max(abs(np.asarray(data['center'])[outside]-refg['center']))),
                'outside_height_jet_max_difference':{k:float(np.max(abs(np.asarray(data['height'][k])[outside]-refg['height'][k])))
                    for k in ['b','b_s','b_ss']}}
        return result

    def snapshot(self):
        result=super().snapshot()
        result['physical_box_lower']=self.physical_lower.tolist()
        result['physical_box_upper']=self.physical_upper.tolist()
        result['independent_coordinate_outer_envelope_lower']=self.lower.tolist()
        result['independent_coordinate_outer_envelope_upper']=self.upper.tolist()
        result.update(schema=POLICY+'-checkpoint',
            independent_coordinate_definition=self.problem.coordinate_definition,
            original_physical_coefficient_count=P,independent_coordinate_count=N,
            physical_height_mean_and_primitive_are_unchanged=False,
            immutable_b0_and_primitive_anchor_are_unchanged=True,
            current_height_uses_the_declared_exact_null_increment=True,
            primary_physical_step_cost=penalty_definition(self.cfg),
            adaptive_trust_policy=growth_definition(self.cfg),conservative_trust_growth=growth_definition(self.cfg),
            SOC_reversible_scaling=scaling_definition(self.cfg),
            entry_tail_height159=restriction_definition(self.cfg),
            initial_fixed_domain_and_current_height_diagnostic=copy.deepcopy(self.restricted_initial_diagnostic))
        return result


def selected_model(objective,state,base,J,groups,tols,trust,cfg):
    full=objective.full_views(state);count=len(objective.pool)
    selected=[SelectedMappedRows(objective.subspace,full[0],objective.pool,J[:count]),
        SelectedMappedRows(objective.subspace,full[1],objective.fine_pool,J[count:])]
    if (not np.array_equal(np.r_[selected[0].values,selected[1].values],base)
            or not np.array_equal(np.r_[selected[0].parts['groups'],selected[1].parts['groups']],groups)
            or not np.array_equal(np.r_[selected[0].tolerances,selected[1].tolerances],tols)):
        raise ValueError('actual original row stack or independent parameter Jacobian changed')
    return build_primary(objective.subspace,full,selected,state,objective.physical_lower,objective.physical_upper,
        objective.constant_cap(),trust_exact=str(Q.from_float(float(trust))),
        fraction_to_boundary_exact=cfg['linear_fraction_to_boundary_exact'],
        physical_norm_weight_exact=cfg['step_cost_physical_box_norm_coefficient_exact'],
        strip_floor_exact=cfg['strip_proposal_floor_exact'],
        curvature_floor_exact=cfg['curvature_proposal_floor_exact'])


def model_projection_record(model):
    info=model.information
    return {'subspace_definition_sha256':model.subspace.definition_sha256,
        'physical_parameters':P,'independent_coordinates':N,'null_height_coordinates':5,
        'coupled_physical_box_and_trust_rows':2*P,'physical_norm_rows':2*P,
        'active_original_row_count':len(info['active_original_rows']),
        'active_original_row_mapping_sha256':digest(info['active_original_rows']),
        'invariant_original_selected_row_count':len(info['invariant_original_rows']),
        'invariant_original_row_mapping_sha256':digest(info['invariant_original_rows']),
        'in_domain_zero_J_rows_kept':info['in_domain_zero_J_rows_kept'],
        'outside_selected_J_max_diagnostic_only':info['outside_selected_J_max_diagnostic_only'],
        'rho_out':info['rho_out'],'eta_out':info['fixed_domain']['eta_out'],
        'constant_cap':info['cap_invariant'],
        'original163_geometry_J_still_computed_then159_independent_columns_returned':True}


def solve_primary(model,cfg):
    started=time.monotonic()
    r=linprog(model.c,A_ub=model.A,b_ub=model.b,bounds=list(zip(model.lower,model.upper)),method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    rho0=model.information['initial_selected_and_constant_metric_slack']
    report={'method':'HiGHS159 independent coordinates with original163 coupled boxes and norms',
        'LP_invoked':True,'success':bool(r.success),'status':int(r.status),'message':str(r.message),
        'nit':int(r.nit),'elapsed_seconds':time.monotonic()-started,'rows':len(model.b),
        'variables':len(model.c),'matrix_bytes':model.A.nbytes,'trust_fraction':model.trust,
        'initial_metric_slack':rho0,'projection':model_projection_record(model),
        'hard_rows_count':int(np.sum(model.active_groups>=2)),'soft_metric_rows_count':int(np.sum(model.active_groups<2)),
        'curvature_cap_and_physical_rows_not_elastic':True}
    report.update(inherited_proposal_floor_report(model,cfg))
    finite_primal=bool(r.x is not None and np.asarray(r.x).shape==model.c.shape and np.all(np.isfinite(r.x)))
    report['solver_returned_finite_primal']=finite_primal
    if not finite_primal:return None,report
    x=np.asarray(r.x,float);p=primary_independent_step(model,x);res=model.residual(x)
    norms=model.subspace.step_norms(p,model.width);physical=model.subspace.M@p
    actual_rho=predicted_slack(model,p)
    report.update(predicted_metric_slack=float(x[N]),predicted_slack_improvement=rho0-float(x[N]),
        predicted_slack_from_rows_and_outside=actual_rho,normalized_step_norm=float(x[-1]),
        maximum_linear_row_violation=res['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=res['maximum_original_linear_bound_violation'],
        maximum_absolute_physical_step=float(np.max(abs(physical))),physical_step_l2=float(np.linalg.norm(physical)),
        maximum_absolute_independent_step=float(np.max(abs(p))))
    report['primary_step_cost_diagnostic']={
        'definition':penalty_definition(cfg),'returned_LP_norm_auxiliary':float(x[-1]),
        'returned_primary_step_cost':float(model.c[-1]*x[-1]),
        'returned_weighted_objective':res['objective_evaluated'],
        'returned_predicted_metric_slack':float(x[N]),'predicted_metric_slack_improvement':rho0-float(x[N]),
        'actual_physical_box_normalized_step_norm':norms['physical_infinity'],
        'actual_trust_normalized_step_norm':norms['common_body_radius_norm']/model.trust,
        'actual_block_box_normalized_step_norm':norms['common_body_radius_norm'],
        'body_utilization':norms['body_physical_normalized']/model.trust,
        'tail_utilization':norms['tail_physical_normalized']/(model.trust/8),
        'height_utilization':norms['height_physical_normalized']/(4*model.trust),
        'common_body_radius':model.trust,'tail_radius':model.trust/8,'height_radius':4*model.trust,
        'physical_norm_cost_evaluated':float(Q(cfg['step_cost_physical_box_norm_coefficient_exact']))*norms['physical_infinity'],
        'norm_of_independent_height_tau_not_substituted':True}
    report.update(inherited_proposal_floor_report(model,cfg,linear=model.active_values+model.active_J@p))
    if not r.success or max(res['maximum_original_linear_row_violation'],res['maximum_original_linear_bound_violation'])>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='LP status or original-unit residual';return None,report
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
        'primary_box_normalized_step_infinity_norm':info['primary_norms']['physical_infinity'],
        'primary_block_normalized_step_infinity_norm':info['primary_norms']['common_body_radius_norm'],
        'rho_out':info['rho_out'],'residual_source':'actual same y on both complete grids',
        'Jacobian_source':'last accepted x; original IDs and159 independent parameter columns',
        'constant_cap_and_external_hard_not_restored_by_false_zero_J_rows':True}
    if model is None:
        report['proposal_rejected_before_LP']=info['status'];return None,report
    trial=model.active_trial_values
    report.update(metric_slack_budget=info['metric_slack_budget'],
        maximum_box_normalized_correction_infinity_norm=model.radius,
        body_correction_radius=info['body_correction_radius'],tail_correction_radius=info['tail_correction_radius'],
        height_correction_radius=info['height_correction_radius'],
        rows=len(model.b),variables=len(model.c),matrix_bytes=model.A.nbytes,
        hard_margin_retention=float(Q(cfg['SOC_physical_margin_retention_exact'])),
        metric_budget_applied_to_actual_trial_rows_plus_old_Jacobian_correction=True,
        selected_metric_actual_minus_primary_linear_minimum=float(np.min(
            (trial-primary.active_values-primary.active_J@p)[primary.active_groups<2])))
    report.update(inherited_proposal_floor_report(primary,cfg,trial=trial))
    started=time.monotonic();scaled=scale_mapped_correction(model)
    report['SOC_reversible_scaling']=scaled.definition()
    report['SOC_scaling_prepare_seconds']=time.monotonic()-started
    report['SOC_solver_tolerances_are_in_scaled_units_not_original_residual_units']=True
    started=time.monotonic()
    r=linprog(scaled.objective,A_ub=scaled.A,b_ub=scaled.b,bounds=list(zip(scaled.lower,scaled.upper)),method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    report.update(LP_invoked=True,success=bool(r.success),status=int(r.status),message=str(r.message),
        nit=int(r.nit),elapsed_seconds=time.monotonic()-started)
    report['SOC_solver_returned_finite_primal']=bool(r.x is not None and np.asarray(r.x).shape==scaled.objective.shape
        and np.all(np.isfinite(r.x)))
    report['SOC_original_unit_dual_diagnostics']=scaled.original_dual_diagnostics(r,model.original_row_group_labels)
    if not report['SOC_solver_returned_finite_primal']:return None,report
    x=scaled.to_original(r.x);w=correction_independent_step(model,x);res=model.residual(x)
    report['SOC_original_and_scaled_residuals']=scaled.original_residuals(r.x)
    linear=primary.active_values+primary.active_J@p;Jw=primary.active_J@w
    hard=primary.active_groups>=2;soft=~hard;outside=primary.information['rho_out']
    norms=primary.subspace.step_norms(w,primary.width);physical=primary.subspace.M@w
    report.update(maximum_linear_row_violation=res['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=res['maximum_original_linear_bound_violation'],
        maximum_absolute_correction=float(np.max(abs(physical))),correction_l2=float(np.linalg.norm(physical)),
        correction_box_normalized_infinity_norm=norms['physical_infinity'],
        correction_box_normalized_l1_norm=norms['physical_L1'],
        correction_block_normalized_infinity_norm=norms['common_body_radius_norm'],
        corrected_predicted_metric_slack=max(outside,0.,float(np.max(-(linear+Jw)[soft]))),
        corrected_actual_trial_linear_metric_slack=max(outside,0.,float(np.max(-(trial+Jw)[soft]))),
        basepoint_prediction_slack_is_only_for_parabolic_linear_bookkeeping=True,
        minimum_corrected_linear_hard_margin=float(np.min(trial[hard]+Jw[hard])) if np.any(hard) else None,
        corrected_affine_cap_margin=primary.information['cap_invariant']['affine_margin'])
    report.update(inherited_proposal_floor_report(primary,cfg,trial=trial,linear=trial+Jw))
    if not r.success or max(res['maximum_original_linear_row_violation'],res['maximum_original_linear_bound_violation'])>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC status or original-unit residual';return None,report
    return w,report


def mapped_parabolic_candidate(subspace,current,p,w,alpha,reference_alpha):
    candidate,detail=parabolic_candidate(current,p,w,alpha,reference_alpha)
    return subspace.apply(current,candidate-np.asarray(current,float)),detail

def run_mapped_recovery(objective,initial,*,known_metric_locations=(),restored_controller=None,artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,EntryTailHeight159Objective):
        raise ValueError('the explicit adaptive spectral objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    restriction_definition(cfg)
    if not isinstance(restored_controller,dict):
        raise ValueError('actual154 controller state from this necessary restoration is required')
    inherited_trust=float(Q(restored_controller['trust_binary64_exact']))
    growth_streak=restored_controller['success_streak']
    if (inherited_trust!=restored_controller.get('trust_evaluated') or not np.isfinite(inherited_trust)
            or not 0<inherited_trust<=float(Q(cfg['entry_tail159_maximum_body_radius_exact']))
            or type(growth_streak) is not int or not 0<=growth_streak<2):
        raise ValueError('finite source-bound inherited B radius and complete success streak required')
    continuation={'restored_entry_tail154_controller_inherited':copy.deepcopy(restored_controller),
        'inherited_body_radius_exact_binary64':str(Q.from_float(inherited_trust)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(inherited_trust)/8),
        'new_height_radius_exact_binary64':str(4*Q.from_float(inherited_trust)),
        'inherited_success_streak':growth_streak,
        'height_to_body_radius_is_new_parameter_exact':'4',
        'no_reset_when_restoration_is_below_original_minimum':True}
    objective.evaluation_definition['entry_tail159_controller_initialization']=continuation
    objective.evaluation_sha256=digest(objective.evaluation_definition)
    meta={'method':POLICY,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
        'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
        'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
        'nonlinear_minimize_invocation_count':0,'linear_program_invocation_count':0,
        'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'shared_max_LPs':cfg['max_linear_models'],'shared_max_values':cfg['max_physical_evaluations'],
        'shared_active_seconds':cfg['max_seconds'],'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'inherited154_plus_new_height_controller':continuation,
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    trust=inherited_trust
    def finish(status,error=None,budget=None):
        snap=objective.snapshot(); point=snap.get('selected_two_grid_physical_point')
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':meta,'checkpoint':snap,
            'new_metric_target_reached_on_both_grids':bool(point and point['new_metric_target_qualified_on_both_grids']),
            'adaptive_trust_policy':growth_definition(objective.cfg),
            'curvature_proposal_floor':floor_definition(objective.cfg),
            'primary_physical_step_cost':penalty_definition(objective.cfg),
            'conservative_trust_growth':growth_definition(objective.cfg),
            'strip_proposal_floor':strip_floor_definition(objective.cfg),
            'SOC_reversible_scaling':scaling_definition(objective.cfg),
            'entry_tail_height159':restriction_definition(objective.cfg),
            'initial_fixed_domain_and_height_diagnostic':copy.deepcopy(objective.restricted_initial_diagnostic),
            'last_pre_LP_decision':copy.deepcopy(meta.get('last_pre_LP_decision')),
            'last_restricted_trust':trust,
            'final_consecutive_growth_qualifying_models':growth_streak,
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    def update_model_scale(model,proposed):
        nonlocal growth_streak
        radius,growth_streak,feedback=next_mapped_trust(model,proposed,growth_streak,cfg)
        model['scale_feedback_update']=feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius
    try:
        initial=np.asarray(initial,float).copy()
        current=initial.copy(); vector=objective.vector(current)
        cd=objective.evaluate(vector)['decision']; fd=objective.fine_decision(current)
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        accepted=objective.accepted_point(current,cd,fd,{'kind':'temporary-restored154-exact-zero-height-null-coordinate-start'})
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
        trust=inherited_trust
        minimum_trust=float(Q(cfg['minimum_trust_box_fraction_exact']))
        drop=float(Q(cfg['minimum_accepted_eta_decrease_exact']))
        if trust<minimum_trust:return finish('inherited154-controller-below-original-minimum-trust')
        objective.linear_rows(vector); objective.begin_optimization()
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
            model['exact_binary64_independent_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_eta=accepted['maximum_eta_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None
            def assess(candidate,kind,alpha,need_fine=False,curve=None,prediction=None,curvature_reference=None):
                nonlocal current,accepted,succeeded,relearned
                objective.problem.coordinates.validate(candidate)
                exact_height=objective.problem.coordinates.exact_heights(candidate)
                if any(exact_height[j]!=objective.problem.coordinates.reference_exact[j] for j in [4,5]):
                    raise ArithmeticError('candidate changed fixed physical height slots4 or5')
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'physical_state_sha256':digest(objective.problem.identity(candidate)),
                    'exact_binary64_independent_coordinates':[str(Q.from_float(float(x))) for x in candidate],
                    'exact_original_physical_coefficients':[str(x) for x in objective.problem.coordinates.physical_exact(candidate)],
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
                    y,curve=mapped_parabolic_candidate(objective.subspace,current,p,arc['w'],alpha,arc['reference_alpha_exact'])
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
                        correction['exact_binary64_independent_correction']=[str(Q.from_float(float(x))) for x in w]
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
        return finish('entry-tail-height159-recovery-error',error={'type':type(error).__name__,'message':str(error)})


class _MappedArrayObjective(EntryTailHeight159Objective):
    """New labelled159 arrays; deliberately not an immersion or research surface."""
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
    snapshot=_OldFixture.snapshot

    def __init__(self,cfg,*,fail_after=None):
        from types import SimpleNamespace
        from frame_entry_tail_height_blocks import artificial_arrays
        from frame_height_null_gate import coordinate_outer_bounds
        self._OldFixture.__init__(self,cfg,fail_after=fail_after)
        sub,full,selected,state,lo,hi,cap=artificial_arrays()
        self.subspace=sub;self.physical_lower=lo;self.physical_upper=hi
        self.lower,self.upper=coordinate_outer_bounds(sub.coordinates,lo,hi)
        self.n=N
        self.problem=SimpleNamespace(coordinates=sub.coordinates,null_basis=sub.coordinates.basis,
            identity=sub.coordinates.physical_identity,coordinate_definition_sha256=sub.coordinates.definition_sha256)
        self.gate=SimpleNamespace(kind='artificial-array',row=np.zeros(N),intercept=0.,target=0.)
        nodes=['0','9/250','9/100','117/1000','33/50','153/200','309/400','423/500','9/10']
        self.row_grids=[RationalRowGrid('coarse',nodes,4),RationalRowGrid('fine',nodes,8)]
        self.radial=np.array([float(Q(x)) for x in nodes])
        self.pool=np.arange(self.row_grids[0].total_rows)
        self.fine_pool=np.arange(self.row_grids[1].total_rows)
        self.original_pool_rows=(len(self.pool),len(self.fine_pool))

    def _data(self,state,grid):
        data,rows,d=self._OldFixture._data(self,state,grid)
        variable=np.array([self.subspace.left<t<self.subspace.right for t in grid.nodes])
        eta=np.full((grid.nr,grid.nt),.2)
        eta[2:5]=.2666-state[154]
        eta[6]=.2666-state[157]
        rows[:2]=.1;rows[0]=float(Q(self.cfg['fixed_metric_budget_exact']))-eta
        rows[4:6]=.1;rows[4,-1]=-1e-10
        C=self.problem.null_basis.values(self.radial);Cs=self.problem.null_basis.values(self.radial,1)
        Css=self.problem.null_basis.values(self.radial,2);Z=self.problem.null_basis.values(self.radial,integral=True)
        tau=np.asarray(state)[154:]
        data['center']=self.radial+Z@tau
        data['height']={'b':np.ones(grid.nr)+C@tau,'b_s':Cs@tau,'b_ss':Css@tau}
        data['X'][...,2]=(Z@tau)[:,None]
        data['Xs'][...,2]=data['height']['b'][:,None]
        data['Xss'][...,2]=data['height']['b_s'][:,None]
        data.update(eta=eta,e=eta.copy())
        exact=self.problem.coordinates.exact_box_decision(state,self.physical_lower,self.physical_upper)
        d['cap_and_box']['eligible_under_declared_numerical_gate_tolerances']=exact['exact_original_box_pass']
        d['direct_max_eta']=float(np.max(eta))
        d['single_grid_new_target_qualified']=bool(np.max(eta)<=float(Q(self.cfg['fixed_metric_budget_exact']))+self.cfg['direct_eta_tolerance'])
        d['single_grid_admissible_recovery_point']=bool(exact['exact_original_box_pass'])
        return data,rows,d

    def linear_rows(self,vector):
        self.evaluate(vector);self.fine_decision(vector[:-1])
        rows=[];matrices=[];groups=[]
        for grid,cache in [(self.row_grids[0],self.epigraph_cache),(self.row_grids[1],self.fine_cache)]:
            J=np.zeros((grid.total_rows,N))
            J[2*grid.nt:5*grid.nt,154]=1.;J[6*grid.nt:7*grid.nt,157]=1.
            rows.append(cache['rows'].reshape(-1));matrices.append(J)
            groups.extend(np.arange(grid.total_rows)//grid.point_count)
        result=np.concatenate(rows),np.vstack(matrices),np.array(groups),np.full(sum(len(x) for x in rows),1e-9)
        self.last_full_J_shape=result[1].shape
        return result

    def accepted_point(self,state,c,f,reason):
        point=self._OldFixture.accepted_point(self,state,c,f,reason)
        point['independent_coordinates_binary64']=point.pop('physical_parameter_coefficients_binary64')
        point['exact_binary64_independent_coordinates']=point.pop('exact_binary64_physical_coefficients')
        point['exact_original_physical_coefficients']=[str(x) for x in self.problem.coordinates.physical_exact(state)]
        return point


def artificial_real_interface_check():
    """Actual SingleQ/height/gate/selected-J APIs on a newly specified tiny ellipse."""
    from frame_five_height_field import artificial_problem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    old,reference=artificial_problem(1)
    nodes=['0','9/250','9/100','117/1000','33/50','153/200','39/50','423/500','9/10']
    t=np.array([float(Q(x)) for x in nodes]);theta=np.arange(8)*np.pi/4
    original_data=old.geometry(reference,t,theta,2)
    original_gate=HeightAffineGate.from_frozen_problem(old,reference,original_data)
    field=FiveHeightField(old,reference);state=field.initial_state()
    lower=np.r_[np.full(154,-8.),np.full(9,-1.)];upper=-lower
    gate=FiveNullHeightGate.from_original(original_gate,field,lower,upper)
    cfg=configuration(recovery_configuration(start_configuration(),target='13/50',curvature_cap='58'))
    obj=EntryTailHeight159Objective(field,gate,t,theta,2,gate.coordinate_lower,gate.coordinate_upper,
        cfg=cfg,radial_nodes_exact=nodes)
    obj.evaluate(obj.vector(state));obj.fine_decision(state)
    before=(obj.geometry_evaluations,obj.fine_evaluations)
    obj.install_reference(state);views=obj.full_views(state)
    initial_invariant=obj.invariant_diagnostic(state,fine_present=True)
    same_count=before==(obj.geometry_evaluations,obj.fine_evaluations)
    moved=state.copy();moved[154:]=.0001*np.array([1.,-.3,.2,.4,-.2])
    obj.evaluate(obj.vector(moved));obj.fine_decision(moved)
    changed=obj.invariant_diagnostic(moved,fine_present=True)
    data=obj.geometry_cache
    current_height_changed=float(np.max(abs(data['height']['b']-original_data['height']['b'])))>0
    # One row of every group on each grid exercises complete selected two-jet J.
    def ids(nt):
        return np.array([g*len(t)*nt+6*nt+(g%nt) for g in range(11)],np.int64)
    obj.set_pool(ids(len(theta)),{'kind':'new-artificial159-complete-group-interface'})
    obj.set_fine_pool(ids(len(obj.fine_theta)),{'kind':'new-artificial159-complete-group-interface'})
    base,J,groups,tols=obj.linear_rows(obj.vector(moved))
    direction=np.cos(np.arange(N)+.4);direction/=np.linalg.norm(direction)
    eps=2e-7
    vectors=[]
    for sign in [1,-1]:
        q=moved+sign*eps*direction
        obj.evaluate(obj.vector(q));obj.fine_decision(q)
        vectors.append(np.r_[obj.constraint_fun(obj.vector(q)),
            obj.fine_rows(q).reshape(-1)[obj.fine_pool]])
    fd=(vectors[0]-vectors[1])/(2*eps);pred=J@direction
    error=float(np.max(abs(fd-pred))/max(1.,float(np.max(abs(fd)))))
    original=field.coordinates.reference_exact
    bad=state.copy()
    # Pivot coordinate envelopes permit a combination which overfills compensation c3.
    bad[154:157]=.9
    box=field.coordinates.exact_box_decision(bad,lower,upper)
    decision=gate.decision(bad,original_data,gate.coordinate_lower,gate.coordinate_upper,
        height_tolerance=cfg['height_tolerance'],reconstruction_tolerance=cfg['height_reconstruction_tolerance'])
    records=obj.snapshot()
    checks={
        'actual_parent_objective_accepts159_columns_and_exact_null_gate':J.shape==(22,N),
        'complete_coarse_and_fine_group_Jacobian_direction':error<3e-7,
        'new_height_changes_true_cached_b_and_positions':current_height_changed,
        'full_views_and_invariant_readout_do_not_evaluate':same_count,
        'exact_zero_coordinate_original_canonical':field.identity(state)==old.identity(reference),
        'outside_sixjets_and_height_primitive_restored':all(
            max(g['outside_six_jet_max_difference'].values())==0
            and max(g['full_frozen_metric_jet_max_difference'].values())==0
            and g['outside_common_center_max_difference']==0
            and max(g['outside_height_jet_max_difference'].values())==0 for g in changed['grids'].values()),
        'coupled_box_rejects_even_inside_pivot_envelope':not box['exact_original_box_pass']
            and not decision['eligible_under_declared_numerical_gate_tolerances'],
        'original_physical_bounds_not_159_envelope_in_snapshot':len(records['physical_box_lower'])==P
            and len(records['independent_coordinate_outer_envelope_lower'])==N,
        'coarse_records_do_not_mislabel159_numbers_as163_physical_coefficients':all(
            'exact_binary64_physical_coefficients' not in v and len(v['exact_original_physical_coefficients'])==P
            for v in obj.saved_coarse_trials.values()),
        'fine_records_relabel_actual_coordinate_storage':all(
            'exact_binary64_physical_coefficients' not in v
            and len(v['exact_original_physical_coefficients'])==P for v in obj.saved_fine_trials)}
    return {'passed':all(checks.values()),'checks':checks,
        'relative_complete_group_directional_Jacobian_error':error,
        'artificial_core_exact':{'A':'9/10','B':'18/25','L':'9/10'},
        'research_candidate_constructed_or_evaluated':False,'optimizer_calls':0}


def developer_check():
    """Only new mapped-array controller branches and a small artificial geometry API."""
    from frame_entry_tail_height_blocks import developer_check as array_check
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(recovery_configuration(start_configuration(),target='13/50',curvature_cap='58'))
    cfg.update(max_linear_models=1,max_physical_evaluations=12,max_seconds=20.,linear_program_seconds=3.)
    continuation={'trust_evaluated':float(Q(1,4000)),'trust_binary64_exact':'1/4000',
        'success_streak':1,'schema':'artificial154-controller-input','unfinished_last_model_not_counted_as_success':False}
    # Use the exact binary64 rational actually passed to the controller.
    continuation['trust_binary64_exact']=str(Q.from_float(continuation['trust_evaluated']))
    unchanged=copy.deepcopy(continuation)
    objective=_MappedArrayObjective(cfg);initial=objective.subspace.coordinates.initial_state()
    stage=run_mapped_recovery(objective,initial,restored_controller=continuation,artificial_inputs_only=True)
    point=stage['checkpoint'].get('selected_two_grid_physical_point')
    selected=None if point is None else np.array(point['independent_coordinates_binary64'])
    failed=_MappedArrayObjective(cfg,fail_after=1)
    failstage=run_mapped_recovery(failed,initial,restored_controller=continuation,artificial_inputs_only=True)
    tiny=dict(continuation,trust_evaluated=float(Q(1,100000000)),success_streak=0)
    tiny['trust_binary64_exact']=str(Q.from_float(tiny['trust_evaluated']))
    small=_MappedArrayObjective(cfg)
    below=run_mapped_recovery(small,initial,restored_controller=tiny,artificial_inputs_only=True)
    arrays=array_check();real=artificial_real_interface_check()
    checks={
        'new_coupled_array_model':arrays['passed'],
        'complete_real_artificial_cache_gate_and_Jacobian_API':real['passed'],
        'one_new_primary_and_no_extra_nonlinear_optimizer':stage['solver']['primary_LP_invocation_count']==1
            and stage['solver']['nonlinear_minimize_invocation_count']==0,
        'new_height_coordinates_can_be_accepted_with_coupled_box_and_exact_cap':bool(
            point and point['accepted_index']>=1 and selected is not None and np.any(selected[154:]!=0)
            and objective.subspace.coordinates.exact_box_decision(selected,objective.physical_lower,objective.physical_upper)['exact_original_box_pass']),
        'actual154_radius_and_success_streak_inherited':stage['solver']['inherited154_plus_new_height_controller'][
            'inherited_success_streak']==1 and continuation==unchanged,
        'below_original_minimum_exits_before_J_or_LP':below['status']=='inherited154-controller-below-original-minimum-trust'
            and below['solver']['linear_program_invocation_count']==0 and small.last_full_J_shape is None,
        'new_value_failure_retains_initial_exact_null_state':failstage.get('error',{}).get('type')=='FloatingPointError'
            and failstage['checkpoint']['selected_two_grid_physical_point']['independent_coordinates_binary64']==initial.tolist()}
    return {'schema':POLICY+'-new-artificial-development','passed':all(checks.values()),'checks':checks,
        'array_check':arrays,'real_artificial_API':real,
        'one_primary_controller':stage,'value_failure_controller':failstage,'below_minimum_controller':below,
        'research_input_loaded_or_evaluated':False}
