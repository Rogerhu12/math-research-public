#!/usr/bin/env python3
"""Keep a model radius only after a narrowly qualified, accepted full SOC.

The frozen159 geometry, exact null-height coordinates, LPs, old value gates,
budgets and ordinary primary growth/shrink remain. New diagnostics use the
actual accepted-base total displacement. No check has run merely by storing
this source; all artificial and research entry points run on public Actions.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
import numpy as np
import scipy

import frame_metric_entry_tail_height159 as old
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_spectral_soc_scaling import ACTUAL_GATES
from frame_metric_entry_tail_height159 import (
    EntryTailHeight159Objective,restriction_definition,growth_definition,
    penalty_definition,scaling_definition,floor_definition,strip_floor_definition,
    fixed_domain_summary,compact_with_all_actual_gates,initial_restriction_decision,
    selected_model,solve_primary,solve_correction,predicted_slack,
    mapped_parabolic_candidate,curvature_arc_slack_bound,curvature_trial_diagnostics,
    trial_quality,EvaluationBudgetReached,require_public_research_environment)

POLICY='same159-successful-full-SOC-conditionally-retains-model-radius-v1'
N=159
P=163


def implementation_hashes():
    result=old.implementation_hashes()
    p=Path(__file__);result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def configuration(base):
    """Extend an already validated159 configuration; never rebuild its prefixes."""
    restriction_definition(base)
    cfg=copy.deepcopy(base)
    if 'successful_SOC_radius_retention_policy' in cfg:
        raise ValueError('the new controller policy must be installed exactly once')
    cfg.update(successful_SOC_radius_retention_policy=POLICY,
        SOC_hold_minimum_base_total_ratio_exact='1/2',
        SOC_hold_maximum_correction_body_norm_fraction_exact='1/10',
        SOC_hold_maximum_total_body_norm_fraction_exact='11/10',
        SOC_hold_never_grows_radius_and_resets_success_streak=True,
        SOC_hold_all_new_rows_including_soft_must_be_zero=True,
        SOC_hold_uses_actual_rounded_accepted_minus_base_displacement=True)
    retention_definition(cfg)
    return cfg


def retention_definition(cfg):
    restriction_definition(cfg)
    constants={
        'SOC_hold_minimum_base_total_ratio_exact':'1/2',
        'SOC_hold_maximum_correction_body_norm_fraction_exact':'1/10',
        'SOC_hold_maximum_total_body_norm_fraction_exact':'11/10'}
    if cfg.get('successful_SOC_radius_retention_policy')!=POLICY or any(
            Q(cfg.get(k,'0'))!=Q(v) for k,v in constants.items()):
        raise ValueError('explicit accepted-base SOC retention constants required')
    return {'schema':POLICY+'-definition',**constants,
        'changes_next_model_radius_only':True,
        'old_primary_and_SOC_equations_floors_and_original_unit_residual_gate_unchanged':True,
        'old_complete_two_grid_gates_and_minimum_actual_descent_unchanged':True,
        'old_primary_only_controller_and_growth_unchanged':True,
        'old_minimum_maximum_radius_and_shared_budgets_unchanged':True,
        'required_trial_order':['primary alpha1','accepted full SOC alpha1'],
        'all_new_coarse_fine_soft_hard_rows_zero':True,
        'only_primary_direct_curvature_failure_may_be_the_old_shrink_reason':True,
        'base_total_prediction':'max(0,rho_out,max_soft(-v-J@(actual_z-actual_x)))',
        'correction_displacement':'actual_z-actual_y',
        'physical_block_norm':'max(Binf,8*Tinf,Hinf/4) of Dphysical^-1 M displacement',
        'SOC_objective_physical_L1_coefficient_exact':'1',
        'primary_physical_infinity_penalty_coefficient_exact':cfg['step_cost_physical_box_norm_coefficient_exact'],
        'ratio_is_not_the_y_linear_SOC_ratio':True,
        'new_diagnostic_has_no_geometry_Jacobian_LP_or_value_call':True,
        'holding_is_a_floating_controller_heuristic_not_a_continuous_certificate':True,
        'does_not_retroactively_accept_or_reclassify_the_old159_model6':True}


class SOCHold159Objective(EntryTailHeight159Objective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.evaluation_definition.update(successful_SOC_radius_retention=retention_definition(self.cfg),
            source_files_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot()
        result['successful_SOC_radius_retention']=retention_definition(self.cfg)
        return result


def _finite_number(value):
    return isinstance(value,(int,float,np.integer,np.floating)) and bool(np.isfinite(value))


def model_binding(primary,base_state,base_physical_sha256,pool_versions):
    """Bind the existing model; the stored primary signature already hashes v/J."""
    x=np.asarray(base_state,float)
    if x.shape!=(N,) or not np.all(np.isfinite(x)):
        raise ValueError('finite actual159 accepted base required')
    return {'base_independent_array_sha256':array_digest(x),
        'base_physical_state_sha256':base_physical_sha256,
        'coordinate_definition_sha256':primary.subspace.coordinates.definition_sha256,
        'subspace_definition_sha256':primary.subspace.definition_sha256,
        'physical_map_array_sha256':array_digest(primary.subspace.M),
        'original_physical_width_array_sha256':array_digest(primary.width),
        'active_original_row_mapping_sha256':digest(primary.information['active_original_rows']),
        'radius_independent_model_sha256':primary.information['radius_independent_model_sha256'],
        'active_selected_shape':[len(primary.active_values),N],
        'coarse_fine_pool_versions':[int(v) for v in pool_versions]}


def actual_total_step_diagnostic(primary,x,y,z,old_eta,coarse,fine,*,cfg,
        model_context,base_physical_sha256,primary_physical_sha256,accepted_physical_sha256,
        current_pool_versions):
    """Only read existing arrays and values. Mapped exact boxes stay independent."""
    result={'schema':POLICY+'-actual-accepted-base-total-step',
        'available':False,'no_additional_geometry_Jacobian_LP_or_value_call':True,
        'displacements_are_actual_rounded_z_minus_x_and_z_minus_y':True,
        'not_the_y_linear_SOC_model_quality':True}
    vectors=[np.asarray(a,float) for a in (x,y,z)]
    if any(a.shape!=(N,) or not np.all(np.isfinite(a)) for a in vectors):
        return dict(result,unavailable_reason='nonfinite or wrong-shape actual state')
    if coarse is None or fine is None or any(not _finite_number(v) for v in
            [old_eta,coarse.get('direct_max_eta'),fine.get('direct_max_eta')]):
        return dict(result,unavailable_reason='two complete finite actual eta values unavailable')
    x,y,z=vectors;s=z-x;c=z-y
    values=np.asarray(primary.active_values,float);J=np.asarray(primary.active_J,float)
    groups=np.asarray(primary.active_groups,int)
    if (J.shape!=(len(values),N) or groups.shape!=values.shape
            or not np.all(np.isfinite(values)) or not np.all(np.isfinite(J))):
        return dict(result,unavailable_reason='nonfinite or mismatched frozen selected model')
    context=model_binding(primary,x,base_physical_sha256,model_context['coarse_fine_pool_versions'])
    bindings={'same_model_base_rows_mapping_M_and_original_widths':context==model_context,
        'primary_object_base_array_matches_actual_x':array_digest(primary.state)==array_digest(x),
        'complete_current_pool_versions_unchanged':list(map(int,current_pool_versions))==context['coarse_fine_pool_versions']}
    soft=groups<2;linear=values+J@s
    outside=float(primary.information['rho_out'])
    if not np.all(np.isfinite(linear)) or not np.isfinite(outside):
        return dict(result,unavailable_reason='nonfinite accepted-base linear prediction or exterior slack')
    total_rho=max(0.,outside,float(np.max(-linear[soft])) if np.any(soft) else 0.)
    actual_eta=max(float(coarse['direct_max_eta']),float(fine['direct_max_eta']))
    denominator=max(0.,float(old_eta)-float(Q(cfg['fixed_metric_budget_exact'])))-total_rho
    numerator=float(old_eta)-actual_eta
    usable=bool(np.isfinite(denominator) and denominator>cfg['linear_model_improvement_floor'])
    ratio=numerator/denominator if usable else None
    if ratio is not None and not np.isfinite(ratio):usable=False;ratio=None
    total_norm=primary.subspace.step_norms(s,primary.width)
    correction_norm=primary.subspace.step_norms(c,primary.width)
    result.update(available=True,model_binding=context,binding_checks=bindings,
        base_physical_state_sha256=base_physical_sha256,
        primary_physical_state_sha256=primary_physical_sha256,
        accepted_physical_state_sha256=accepted_physical_sha256,
        actual_base_coordinates_sha256=array_digest(x),actual_primary_coordinates_sha256=array_digest(y),
        actual_accepted_coordinates_sha256=array_digest(z),
        actual_total_displacement_sha256=array_digest(s),actual_correction_displacement_sha256=array_digest(c),
        old_true_maximum_eta=float(old_eta),accepted_true_two_grid_maximum_eta=actual_eta,
        fixed_target_exact=cfg['fixed_metric_budget_exact'],rho_out=outside,
        base_total_predicted_slack=float(total_rho),base_total_predicted_eta_improvement=float(denominator),
        actual_two_grid_eta_improvement=float(numerator),
        base_total_ratio_denominator_usable=usable,base_total_actual_to_predicted_ratio=ratio,
        ratio_unavailable_reason=None if usable else 'base total predicted drop is nonfinite or not above the original floor',
        actual_total_physical_norms=total_norm,actual_correction_physical_norms=correction_norm,
        correction_physical_L1_is_not_inferred_from_the_SOC_objective=True)
    return result


_PRIMARY_ALLOWED_FALSE={'curvature_scaled_PSD_row_pass','independent_direct_curvature_pass',
    'single_grid_hard_gate_pass','single_grid_admissible_recovery_point'}


def _trial_gates(trial,label):
    return trial.get(label+'_decision',{}).get('actual_gate_booleans',{})


def next_soc_hold_trust(model,current_trust,streak,cfg):
    """Compute old control first; only the explicit successful-SOC exception differs."""
    retention_definition(cfg)
    old_radius,old_streak,old_report=old.next_mapped_trust(model,current_trust,streak,cfg)
    before=float(model['trust_before_model'])
    ts=model.get('trials',[]);cs=model.get('corrections',[])
    p=ts[0] if len(ts)==2 else {};z=ts[1] if len(ts)==2 else {}
    pq=p.get('scale_feedback',{});zq=z.get('scale_feedback',{})
    lp=cs[0].get('linear_program',{}) if len(cs)==1 else {}
    d=model.get('accepted_SOC_base_total_step_diagnostic',{})
    full=bool(len(ts)==2 and all(t.get('fine_decision') is not None and
        t.get('coarse_decision') is not None and
        t.get('scale_feedback',{}).get('full_two_grid_actual_available') is True for t in ts))
    gate_names=tuple(ACTUAL_GATES)+('cap_and_box_eligible',)
    pflags=[_trial_gates(p,label) for label in ['coarse','fine']]
    zflags=[_trial_gates(z,label) for label in ['coarse','fine']]
    primary_other=bool(full and all(f.get(k) is True for f in pflags
        for k in gate_names if k not in _PRIMARY_ALLOWED_FALSE))
    primary_curvature=bool(full and any(f.get(k) is False for f in pflags
        for k in ['curvature_scaled_PSD_row_pass','independent_direct_curvature_pass']))
    final_all=bool(full and all(f.get(k) is True for f in zflags for k in gate_names))
    qualities=model.get('scale_feedback_trials',[])
    no_other_reason=bool(len(qualities)==2 and qualities==[pq,zq] and
        all(q.get('poor_complete_two_grid_ratio') is False and
            q.get('poor_coarse_upper_bound_without_fine') is False and
            q.get('full_two_grid_actual_available') is True for q in qualities) and
        bool(pq.get('actual_curvature_failure_grids')) and not zq.get('actual_curvature_failure_grids') and
        pq.get('request_shrink') is True and zq.get('request_shrink') is False and
        old_report.get('trigger_trial_indices')==[0])
    ratio=d.get('base_total_actual_to_predicted_ratio')
    cn=d.get('actual_correction_physical_norms',{}).get('common_body_radius_norm')
    sn=d.get('actual_total_physical_norms',{}).get('common_body_radius_norm')
    bindings=d.get('binding_checks',{})
    residuals=[lp.get('maximum_linear_row_violation'),lp.get('maximum_linear_bound_violation')]
    source_index=cs[0].get('primary_trial_index') if len(cs)==1 else None
    complete_drop=pq.get('actual_two_grid_eta_improvement')
    drop=float(Q(cfg['minimum_accepted_eta_decrease_exact']))
    checks={
        'one_full_primary_then_one_accepted_full_SOC_no_backtrack':bool(len(ts)==2 and len(cs)==1
            and p.get('kind')=='primary-metric-short-step' and p.get('alpha_exact')=='1'
            and p.get('accepted_as_next_iterate') is False
            and z.get('kind')=='metric-SOC-corrected-short-step' and z.get('alpha_exact')=='1'
            and z.get('accepted_as_next_iterate') is True
            and model.get('result')=='accepted-full-SOC-two-grid-metric-descent'),
        'both_trials_have_actual_complete_coarse_and_fine_values':full,
        'primary_has_original_required_true_eta_drop':bool(_finite_number(complete_drop) and complete_drop>=drop),
        'primary_other_individual_gates_pass':primary_other,
        'primary_failed_curvature_only':bool(primary_other and primary_curvature),
        'accepted_SOC_all_original_complete_grid_gates_pass':final_all,
        'accepted_SOC_has_original_required_true_eta_drop':bool(_finite_number(
            d.get('actual_two_grid_eta_improvement')) and d['actual_two_grid_eta_improvement']>=drop),
        'all_new_coarse_and_fine_rows_including_soft_zero':bool(len(ts)==2 and all(
            t.get('new_coarse_rows')==0 and t.get('new_fine_rows')==0 for t in ts)),
        'all_omitted_hard_rows_zero':bool(len(ts)==2 and all(
            t.get('coarse_omitted_hard_rows')==0 and t.get('fine_omitted_hard_rows')==0 for t in ts)),
        'primary_SOC_link_and_pool_versions_match':bool(len(cs)==1 and source_index==0
            and cs[0].get('primary_trial_physical_sha256')==p.get('physical_state_sha256')
            and cs[0].get('coarse_pool_version')==model.get('coarse_pool_version')
            and cs[0].get('fine_pool_version')==model.get('fine_pool_version')),
        'same_base_rows_map_width_and_pools_bound':bool(d.get('available') is True and bindings
            and all(v is True for v in bindings.values())
            and d.get('model_binding')==model.get('SOC_hold_model_binding')
            and d.get('base_physical_state_sha256')==model.get('linearized_at_physical_sha256')
            and d.get('primary_physical_state_sha256')==p.get('physical_state_sha256')
            and d.get('accepted_physical_state_sha256')==z.get('physical_state_sha256')),
        'SOC_finite_primal_success_and_original_unit_residual_gate':bool(lp.get('LP_invoked') is True
            and lp.get('success') is True and lp.get('status')==0 and lp.get('SOC_solver_returned_finite_primal') is True
            and all(_finite_number(v) for v in residuals)
            and max(residuals)<=cfg['linear_model_residual_limit']),
        'actual_base_total_prediction_ratio_at_least_one_half':bool(d.get('base_total_ratio_denominator_usable') is True
            and _finite_number(ratio) and ratio>=float(Q(cfg['SOC_hold_minimum_base_total_ratio_exact']))),
        'actual_mapped_correction_at_most_tenth_body_radius':bool(_finite_number(cn)
            and cn<=before*float(Q(cfg['SOC_hold_maximum_correction_body_norm_fraction_exact']))),
        'actual_mapped_total_step_at_most_eleven_tenths_body_radius':bool(_finite_number(sn)
            and sn<=before*float(Q(cfg['SOC_hold_maximum_total_body_norm_fraction_exact']))),
        'only_primary_actual_curvature_caused_old_shrink':no_other_reason,
        'no_original_rejection_or_other_prior_radius_reduction':bool(current_trust==before
            and old_report.get('trust_after_original_controller')==before
            and old_radius==before*float(Q(cfg['adaptive_trust_shrink_factor_exact']))) }
    eligible=bool(all(checks.values()))
    radius=before if eligible else old_radius;count=0 if eligible else old_streak
    diagnostic={'schema':POLICY+'-decision','qualified_to_retain_model_radius':eligible,
        'checks':checks,'failed_conditions':[k for k,v in checks.items() if not v],
        'original_model_radius':before,'old_controller_next_radius':old_radius,'new_next_radius':radius,
        'old_controller_next_success_streak':old_streak,'new_next_success_streak':count,
        'base_total_ratio':ratio,'correction_common_body_norm':cn,'total_common_body_norm':sn,
        'retained_without_growth':eligible,'ordinary_primary_control_result_preserved':not eligible,
        'old_controller_result':copy.deepcopy(old_report),
        'old_quality_and_trial_records_not_modified':True}
    report={'schema':POLICY+'-scale-feedback','model_trust':before,
        'trust_after_original_controller':float(current_trust),
        'next_trust':radius,'next_tail_radius':radius/8,'next_height_radius':4*radius,
        'trigger_trial_indices':copy.deepcopy(old_report['trigger_trial_indices']),
        'successful_SOC_radius_retention':diagnostic}
    return radius,count,report



def run_soc_hold_recovery(objective,initial,*,known_metric_locations=(),restored_controller=None,artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,EntryTailHeight159Objective):
        raise ValueError('the explicit adaptive spectral objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    retention_definition(cfg)
    if not isinstance(restored_controller,dict):
        raise ValueError('actual frozen159 controller state from this necessary restoration is required')
    inherited_trust=float(Q(restored_controller['trust_binary64_exact']))
    growth_streak=restored_controller['success_streak']
    if (inherited_trust!=restored_controller.get('trust_evaluated') or not np.isfinite(inherited_trust)
            or not 0<inherited_trust<=float(Q(cfg['entry_tail159_maximum_body_radius_exact']))
            or type(growth_streak) is not int or not 0<=growth_streak<2):
        raise ValueError('finite source-bound inherited B radius and complete success streak required')
    continuation={'restored_height159_controller_inherited':copy.deepcopy(restored_controller),
        'inherited_body_radius_exact_binary64':str(Q.from_float(inherited_trust)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(inherited_trust)/8),
        'inherited_height_radius_exact_binary64':str(4*Q.from_float(inherited_trust)),
        'inherited_success_streak':growth_streak,
        'height_to_body_radius_unchanged_exact':'4',
        'no_reset_when_restoration_is_below_original_minimum':True}
    objective.evaluation_definition['height159_SOC_hold_controller_initialization']=continuation
    objective.evaluation_sha256=digest(objective.evaluation_definition)
    meta={'method':POLICY,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
        'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
        'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
        'nonlinear_minimize_invocation_count':0,'linear_program_invocation_count':0,
        'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'shared_max_LPs':cfg['max_linear_models'],'shared_max_values':cfg['max_physical_evaluations'],
        'shared_active_seconds':cfg['max_seconds'],'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'inherited159_controller_without_reset':continuation,
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
            'successful_SOC_radius_retention':retention_definition(objective.cfg),
            'initial_fixed_domain_and_height_diagnostic':copy.deepcopy(objective.restricted_initial_diagnostic),
            'last_pre_LP_decision':copy.deepcopy(meta.get('last_pre_LP_decision')),
            'last_restricted_trust':trust,
            'final_consecutive_growth_qualifying_models':growth_streak,
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    def update_model_scale(model,proposed):
        nonlocal growth_streak
        radius,growth_streak,feedback=next_soc_hold_trust(model,proposed,growth_streak,cfg)
        model['scale_feedback_update']=feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius
    try:
        initial=np.asarray(initial,float).copy()
        current=initial.copy(); vector=objective.vector(current)
        cd=objective.evaluate(vector)['decision']; fd=objective.fine_decision(current)
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        accepted=objective.accepted_point(current,cd,fd,{'kind':'temporary-restored159-same-exact-height-reference-start'})
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
        if trust<minimum_trust:return finish('inherited159-controller-below-original-minimum-trust')
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
            model_center=current.copy()
            primary=selected_model(objective,current,base,J,groups,tols,trust,local)
            p,lp=solve_primary(primary,local)
            meta['linear_program_invocation_count']+=1; meta['primary_LP_invocation_count']+=1
            model={'number':len(meta['models'])+1,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'coarse_pool_version':versions[0],'fine_pool_version':versions[1],
                'trust_before_model':trust,'scale_feedback_trials':[],
                'SOC_hold_model_binding':model_binding(primary,model_center,accepted['physical_state_sha256'],versions),
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
                        if succeeded:
                            model['result']='accepted-full-SOC-two-grid-metric-descent'
                            model['accepted_SOC_base_total_step_diagnostic']=actual_total_step_diagnostic(
                                primary,model_center,y,current,old_eta,
                                model['trials'][-1]['coarse_decision'],model['trials'][-1]['fine_decision'],
                                cfg=cfg,model_context=model['SOC_hold_model_binding'],
                                base_physical_sha256=model['linearized_at_physical_sha256'],
                                primary_physical_sha256=trial['physical_state_sha256'],
                                accepted_physical_sha256=accepted['physical_state_sha256'],
                                current_pool_versions=(objective.pool_version,objective.fine_pool_version))
                            break
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
        return finish('height159-SOC-retention-recovery-error',error={'type':type(error).__name__,'message':str(error)})


def _new_array_fixture(actual_ratio=.75):
    """New labelled arrays only; it is not a surface and does not call a solver."""
    from types import SimpleNamespace
    from frame_entry_tail_height_blocks import artificial_arrays
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(old.configuration(recovery_configuration(start_configuration(),
        target='13/50',curvature_cap='58')))
    sub,_,_,x,lo,hi,_=artificial_arrays()
    x=np.asarray(x,float).copy();width=hi-lo;r=float(Q(1,8000))
    p=np.zeros(N);p[0]=.8*r*width[0]
    c=np.zeros(N);c[0]=.01*r*width[0]
    y=sub.apply(x,p);z=sub.apply(y,c);eta=.266
    values=np.array([-.006,-.006,.1]);J=np.zeros((3,N));J[:2,0]=.005
    primary=SimpleNamespace(state=x.copy(),subspace=sub,width=width,
        active_values=values,active_J=J,active_groups=np.array([0,1,8]),
        information={'rho_out':0.,'active_original_rows':[{'grid':'artificial','row':i} for i in range(3)],
            'radius_independent_model_sha256':digest({'pure_artificial_model':'new-SOC-hold'})})
    pred=max(0.,eta-.26)-max(0.,float(np.max(-(values+J@(z-x))[:2])))
    drop=actual_ratio*pred;candidate_eta=eta-drop
    flags={k:True for k in tuple(ACTUAL_GATES)+('cap_and_box_eligible',)}
    def decision(*,failed=False):
        f=copy.deepcopy(flags)
        if failed:
            for key in _PRIMARY_ALLOWED_FALSE:f[key]=False
        return {'actual_gate_booleans':f,'direct_max_eta':candidate_eta,
            'direct_maximum_absolute_principal_curvature':58.0001 if failed else 57.9,
            'single_grid_admissible_recovery_point':not failed,
            'single_grid_new_target_qualified':False}
    pc,pf=decision(),decision(failed=True);zc,zf=decision(),decision()
    psha,zsha=digest(sub.coordinates.physical_identity(y)),digest(sub.coordinates.physical_identity(z))
    bsha=digest(sub.coordinates.physical_identity(x));versions=(2,3)
    primary_prediction={'predicted_slack':max(0.,float(np.max(-(values+J@(y-x))[:2]))),
        'model_kind':'basepoint-plus-J-step'}
    soc_prediction={'predicted_slack':max(0.,eta-.26)-drop,
        'model_kind':'same-actual-y-rows-plus-J-correction'}
    pq=trial_quality(eta,pc,pf,primary_prediction,'primary-metric-short-step',cfg)
    zq=trial_quality(eta,zc,zf,soc_prediction,'metric-SOC-corrected-short-step',cfg)
    def trial(kind,sha,c,f,q,accepted):
        return {'kind':kind,'alpha_exact':'1','accepted_as_next_iterate':accepted,
            'physical_state_sha256':sha,'coarse_decision':c,'fine_decision':f,'scale_feedback':q,
            'new_coarse_rows':0,'new_fine_rows':0,'coarse_omitted_hard_rows':0,'fine_omitted_hard_rows':0}
    context=model_binding(primary,x,bsha,versions)
    diag=actual_total_step_diagnostic(primary,x,y,z,eta,zc,zf,cfg=cfg,model_context=context,
        base_physical_sha256=bsha,primary_physical_sha256=psha,accepted_physical_sha256=zsha,
        current_pool_versions=versions)
    model={'number':1,'trust_before_model':r,'linearized_at_physical_sha256':bsha,
        'coarse_pool_version':2,'fine_pool_version':3,'SOC_hold_model_binding':context,
        'result':'accepted-full-SOC-two-grid-metric-descent',
        'linear_program':{'primary_step_cost_diagnostic':{'actual_trust_normalized_step_norm':.8}},
        'trials':[trial('primary-metric-short-step',psha,pc,pf,pq,False),
            trial('metric-SOC-corrected-short-step',zsha,zc,zf,zq,True)],
        'scale_feedback_trials':[pq,zq],
        'corrections':[{'primary_trial_index':0,'primary_trial_physical_sha256':psha,
            'coarse_pool_version':2,'fine_pool_version':3,
            'linear_program':{'LP_invoked':True,'success':True,'status':0,'SOC_solver_returned_finite_primal':True,
                'maximum_linear_row_violation':0.,'maximum_linear_bound_violation':0.}}],
        'accepted_SOC_base_total_step_diagnostic':diag}
    return cfg,primary,x,y,z,model


def developer_check():
    """Only the new pure-array diagnostics and conditional controller branches."""
    cfg,primary,x,y,z,model=_new_array_fixture()
    r=model['trust_before_model'];saved=copy.deepcopy(model)
    arrays=[a.copy() for a in [x,y,z,primary.active_values,primary.active_J,primary.width,primary.subspace.M]]
    radius,count,report=next_soc_hold_trust(model,r,1,cfg)
    decisions={};reports={}
    def reject(name,change):
        m=copy.deepcopy(model);change(m)
        rr,ss,d=next_soc_hold_trust(m,r,1,cfg)
        oo,os,_=old.next_mapped_trust(m,r,1,cfg)
        decisions[name]=bool(rr==oo and ss==os and not d['successful_SOC_radius_retention']['qualified_to_retain_model_radius'])
        reports[name]=d['successful_SOC_radius_retention']['failed_conditions']
    reject('new_soft_coarse_row',lambda m:m['trials'][1].update(new_coarse_rows=1))
    reject('new_soft_fine_row',lambda m:m['trials'][1].update(new_fine_rows=1))
    reject('omitted_hard_row',lambda m:m['trials'][1].update(fine_omitted_hard_rows=1))
    reject('missing_fine',lambda m:m['trials'][0].pop('fine_decision'))
    reject('unaccepted_SOC',lambda m:m['trials'][1].update(accepted_as_next_iterate=False))
    reject('backtracked_SOC',lambda m:m['trials'][1].update(alpha_exact='1/2'))
    reject('changed_pool_version',lambda m:m['corrections'][0].update(fine_pool_version=4))
    reject('wrong_base_binding',lambda m:m['SOC_hold_model_binding'].update(base_physical_state_sha256='f'*64))
    reject('wrong_row_mapping',lambda m:m['SOC_hold_model_binding'].update(active_original_row_mapping_sha256='e'*64))
    reject('nonfinite_or_missing_SOC_primal',lambda m:m['corrections'][0]['linear_program'].update(SOC_solver_returned_finite_primal=False))
    reject('unsuccessful_SOC_status',lambda m:m['corrections'][0]['linear_program'].update(success=False,status=1))
    reject('original_unit_residual_failure',lambda m:m['corrections'][0]['linear_program'].update(
        maximum_linear_row_violation=2*cfg['linear_model_residual_limit']))
    reject('other_primary_gate_failure',lambda m:m['trials'][0]['fine_decision']['actual_gate_booleans'].update(hard_strip_pass=False))
    reject('other_SOC_gate_failure',lambda m:m['trials'][1]['fine_decision']['actual_gate_booleans'].update(hard_ball_pass=False))
    def poor(m):
        m['scale_feedback_trials'][0]['poor_complete_two_grid_ratio']=True
        m['scale_feedback_trials'][0]['actual_to_predicted_ratio']=.1
        m['trials'][0]['scale_feedback']=copy.deepcopy(m['scale_feedback_trials'][0])
    reject('primary_poor_ratio_is_not_erased',poor)
    def poor_upper(m):
        m['scale_feedback_trials'][0]['poor_coarse_upper_bound_without_fine']=True
        m['trials'][0]['scale_feedback']=copy.deepcopy(m['scale_feedback_trials'][0])
    reject('coarse_only_poor_bound_is_not_erased',poor_upper)
    smaller,smaller_count,smaller_report=next_soc_hold_trust(model,r/2,1,cfg)
    smaller_old,smaller_old_count,_=old.next_mapped_trust(model,r/2,1,cfg)
    low=_new_array_fixture(.3)[-1]
    low_radius,low_count,low_report=next_soc_hold_trust(low,r,1,cfg)
    low_old,low_old_count,_=old.next_mapped_trust(low,r,1,cfg)
    # Recompute actual z-x with modified arrays. No pretend ratio≈1 substitutes for it.
    unavailable=[]
    for kind in ['zero','negative','nonfinite']:
        prim=copy.copy(primary);prim.active_values=primary.active_values.copy();prim.active_J=primary.active_J.copy()
        if kind=='zero':prim.active_J[:]=0.
        elif kind=='negative':prim.active_J[:]=-abs(prim.active_J)
        else:prim.active_J[0,0]=np.inf
        context=model_binding(prim,x,model['linearized_at_physical_sha256'],(2,3))
        d=actual_total_step_diagnostic(prim,x,y,z,.266,
            model['trials'][1]['coarse_decision'],model['trials'][1]['fine_decision'],cfg=cfg,
            model_context=context,base_physical_sha256=model['linearized_at_physical_sha256'],
            primary_physical_sha256=model['trials'][0]['physical_state_sha256'],
            accepted_physical_sha256=model['trials'][1]['physical_state_sha256'],current_pool_versions=(2,3))
        unavailable.append(not d.get('base_total_ratio_denominator_usable',False))
    tail_delta=np.zeros(N);tail_delta[int(primary.subspace.tail_columns[0])]=.02*r*primary.width[int(primary.subspace.tail_columns[0])]
    tail_norms=primary.subspace.step_norms(tail_delta,primary.width)
    height_delta=np.zeros(N);height_delta[154:157]=4*r*.09*primary.width[154]
    height_norms=primary.subspace.step_norms(height_delta,primary.width)
    mapped=primary.subspace.M@height_delta/primary.width
    dependent_amplification=float(np.max(abs(mapped[154:])))>float(np.max(abs(height_delta[154:])))/primary.width[154]
    reject('tail_weighted_correction_limit',lambda m:m['accepted_SOC_base_total_step_diagnostic'].update(
        actual_correction_physical_norms=tail_norms))
    reject('dependent_nine_height_correction_limit',lambda m:m['accepted_SOC_base_total_step_diagnostic'].update(
        actual_correction_physical_norms=height_norms))
    reject('total_weighted_step_limit',lambda m:m['accepted_SOC_base_total_step_diagnostic'].update(
        actual_total_physical_norms={'common_body_radius_norm':1.10001*r}))
    # Ordinary primary-only paths still return exactly the old radius/streak/report.
    ordinary=copy.deepcopy(model);ordinary['trials']=[copy.deepcopy(model['trials'][1])]
    ordinary['trials'][0].update(kind='primary-metric-short-step')
    ordinary['trials'][0]['scale_feedback']['kind']='primary-metric-short-step'
    ordinary['corrections']=[];ordinary['result']='accepted-two-grid-true-metric-descent'
    ordinary['scale_feedback_trials']=[ordinary['trials'][0]['scale_feedback']]
    ordinary['linear_program']['primary_step_cost_diagnostic']['actual_trust_normalized_step_norm']=1.
    ordinary_ok=True
    for streak in [0,1]:
        nr,ns,nreport=next_soc_hold_trust(ordinary,r,streak,cfg)
        oo,os,oreport=old.next_mapped_trust(ordinary,r,streak,cfg)
        ordinary_ok=bool(ordinary_ok and (nr,ns)==(oo,os)
            and nreport['successful_SOC_radius_retention']['old_controller_result']==oreport)
    unchanged=bool(model==saved and all(np.array_equal(a,b,equal_nan=True) for a,b in zip(arrays,
        [x,y,z,primary.active_values,primary.active_J,primary.width,primary.subspace.M])))
    checks={
        'complete_success_holds_model_radius_and_clears_streak':bool(radius==r and count==0
            and report['successful_SOC_radius_retention']['qualified_to_retain_model_radius']),
        'old_rule_would_have_shrunk_exactly_once':bool(report['successful_SOC_radius_retention']['old_controller_next_radius']==r/2),
        'all_individually_disqualifying_branches_preserve_old_result':bool(all(decisions.values())),
        'y_ratio_one_does_not_mask_base_total_ratio_below_half':bool(low['trials'][1]['scale_feedback']['actual_to_predicted_ratio']>.99
            and low_report['successful_SOC_radius_retention']['base_total_ratio']<.5
            and (low_radius,low_count)==(low_old,low_old_count)),
        'zero_negative_and_nonfinite_prediction_denominators_unavailable':bool(all(unavailable)),
        'tail_norm_uses_factor_eight':bool(abs(tail_norms['common_body_radius_norm']-.16*r)<1e-16),
        'nine_physical_height_map_detects_compensation_amplification':bool(dependent_amplification
            and height_norms['height_physical_normalized']==float(np.max(abs(mapped[154:])))),
        'another_existing_radius_reduction_is_never_undone':bool((smaller,smaller_count)==(smaller_old,smaller_old_count)
            and not smaller_report['successful_SOC_radius_retention']['qualified_to_retain_model_radius']),
        'ordinary_primary_only_growth_and_shrink_exactly_preserved':bool(ordinary_ok),
        'state_model_arrays_and_old_trial_records_not_modified':unchanged,
        'only_array_arithmetic_no_geometry_Jacobian_value_or_LP':True}
    return {'schema':POLICY+'-new-controller-array-development','passed':bool(all(checks.values())),
        'checks':checks,'branch_results':decisions,'failed_conditions_by_branch':reports,
        'successful_retention':report,'low_true_base_ratio':low_report,
        'tail_norms':tail_norms,'dependent_height_norms':height_norms,
        'research_candidate_or_prior_suite_executed':False,'geometry_calls':0,'LP_calls':0}

