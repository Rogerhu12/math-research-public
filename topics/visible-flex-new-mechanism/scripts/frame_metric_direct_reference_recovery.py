#!/usr/bin/env python3
"""New direct-reference task, retaining the paid guarded trial/SOC/controller paths.

Source-derived from frame_metric_curvature_defect_guard_recovery.py SHA256
4a3b6dde704e5e18d3a9d91da7032ac69b67c113cf2ddc9538a1efd3ebeefcb1.
Only the independent task entrance, approved resource allocation, direct
initial pools and explicit information-migration reports change. No frozen
module or old epoch ledger is patched. Science is public Actions only.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import time
import numpy as np
import scipy
from frame_height_null_coordinates import digest
from frame_metric_height159_affine_spectral import (
    AffineSpectralHeight159Objective, retention_definition,
    actual_total_step_diagnostic)
from frame_metric_affine_spectral_model import definition as model_definition
from frame_metric_height159_soc_hold import (
    restriction_definition, growth_definition, penalty_definition,
    scaling_definition, floor_definition, strip_floor_definition,
    fixed_domain_summary, compact_with_all_actual_gates,
    initial_restriction_decision, selected_model,
    predicted_slack, mapped_parabolic_candidate, curvature_arc_slack_bound,
    curvature_trial_diagnostics, trial_quality, EvaluationBudgetReached,
    require_public_research_environment, model_binding)
from frame_metric_expanded_pool_soc import (
    POLICY as EXPANDED_POLICY, definition as expanded_definition,
    capture_failed_trial, require_current_layout, rebound_budget,
    solve_rebound_correction, attach_rebound_reports)
from frame_metric_height159_complete_affine import attach_complete_model_reports
from frame_metric_expanded_layout_hold import (
    POLICY as HOLD_POLICY, definition as layout_hold_definition,
    next_expanded_layout_hold_trust, restore_failed_y_layout)
from frame_metric_direct_reference_epoch import (
    POLICY, PAIR_POLICY as ALLOCATION_POLICY, DirectReferenceGuardObjective,
    allocation_definition, primary_allocation, solve_reserved_primary,
    attach_direct_task_reports, definition as direct_task_definition)
from frame_metric_covered_soft_growth import (
    POLICY as COVERED_POLICY, definition as covered_growth_definition,
    register_ordinary_context, next_covered_soft_growth_trust,
    mark_previous_growth_used)
from frame_metric_curvature_defect_guard import (
    POLICY as GUARD_POLICY, definition as guard_definition)

def _run_direct_reference_outer(objective,initial,*,known_metric_locations=(),restored_controller=None,artificial_inputs_only=False,evaluate_only=False):
    if (not isinstance(objective,DirectReferenceGuardObjective)
            or objective.direct_reference_policy != POLICY
            or objective.curvature_defect_guard_policy != GUARD_POLICY
            or objective.expanded_pool_policy != EXPANDED_POLICY
            or objective.expanded_layout_hold_policy != HOLD_POLICY
            or objective.soc_pair_reservation_policy != ALLOCATION_POLICY
            or objective.covered_soft_growth_policy != COVERED_POLICY):
        raise ValueError('the fresh direct-reference438/4 task objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    objective._wall()
    retention_definition(cfg)
    if not isinstance(restored_controller,dict):
        raise ValueError('actual frozen159 controller state from this necessary restoration is required')
    inherited_trust=float(Q(restored_controller['trust_binary64_exact']))
    growth_streak=restored_controller['success_streak']
    covered_streak=restored_controller['covered_ordinary_success_streak']  # Actual paid terminal controller, no reset.
    if (inherited_trust!=restored_controller.get('trust_evaluated') or not np.isfinite(inherited_trust)
            or not 0<inherited_trust<=float(Q(cfg['entry_tail159_maximum_body_radius_exact']))
            or type(growth_streak) is not int or not 0<=growth_streak<2
            or type(covered_streak) is not int or not 0<=covered_streak<2):
        raise ValueError('finite source-bound inherited B radius and complete success streak required')
    if inherited_trust != .00025 or growth_streak != 0 or covered_streak != 0:
        raise ValueError('the paid current-best B=1/4000 and both zero streaks are required')
    continuation={'restored_height159_controller_inherited':copy.deepcopy(restored_controller),
        'inherited_body_radius_exact_binary64':str(Q.from_float(inherited_trust)),
        'inherited_tail_radius_exact_binary64':str(Q.from_float(inherited_trust)/8),
        'inherited_height_radius_exact_binary64':str(4*Q.from_float(inherited_trust)),
        'inherited_success_streak':growth_streak,
        'inherited_covered_ordinary_streak_initial':covered_streak,
        'covered_ordinary_streak_was_not_reset':True,
        'previous_soft_learning_not_recounted_as_new_successes':True,
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
        'primary_SOC_pair_allocation_definition':allocation_definition(),
        'primary_allocation_decisions':[],'unpaired_primary_stop':None,
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'inherited159_controller_without_reset':continuation,
        'direct_reference_new_task_definition':direct_task_definition(),
        'all_science_including_prepare_uses_one_new_clock':True,
        'old_epoch_is_closed_and_ancestral_costs_are_separate':True,
        'covered_soft_ordinary_growth_definition':covered_growth_definition(),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    trust=inherited_trust
    def finish(status,error=None,budget=None):
        objective.finalize_curvature_guard_learning()
        snap=objective.snapshot(); point=snap.get('selected_two_grid_physical_point')
        if objective.checkpoint:objective.checkpoint(snap)
        remaining_LPs=cfg['max_linear_models']-meta['linear_program_invocation_count']
        meta['final_shared_LP_allocation']={
            'original_limit':cfg['max_linear_models'],
            'started_total':meta['linear_program_invocation_count'],
            'started_primary':meta['primary_LP_invocation_count'],
            'started_SOC':meta['correction_LP_invocation_count'],
            'remaining_unspent':remaining_LPs,
            'unspent_due_to_no_unpaired_primary_rule':(
                remaining_LPs if meta['unpaired_primary_stop'] is not None else 0),
            'original_shared_limit_exhausted':remaining_LPs==0,
            'virtual_or_reserved_slots_counted_as_started':False}
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
            'affine_ef_spectral_primary_definition':model_definition(),
            'expanded_pool_same_trial_SOC_definition':expanded_definition(),
            'expanded_layout_SOC_radius_retention_definition':layout_hold_definition(),
            'primary_SOC_pair_allocation_definition':allocation_definition(),
            'new_task_cfg_remained_immutable_after_approved_four_key_changes':True,
            'inherited_scope_labels':{
                'source_configuration_was_not_mutated_for_policy_metadata':
                    'the old stage claim does not identify this new task cfg with the paid cfg'},
            'initial_fixed_domain_and_height_diagnostic':copy.deepcopy(objective.restricted_initial_diagnostic),
            'last_pre_LP_decision':copy.deepcopy(meta.get('last_pre_LP_decision')),
            'last_restricted_trust':trust,
            'final_consecutive_growth_qualifying_models':growth_streak,
            'final_covered_ordinary_growth_streak':covered_streak,
            'covered_soft_ordinary_growth_definition':covered_growth_definition(),
            'legacy_streak_is_actual_next_frozen_controller_input':True,
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    def update_model_scale(model,proposed):
        nonlocal growth_streak,covered_streak
        radius,growth_streak,covered_streak,feedback=next_covered_soft_growth_trust(
            model,proposed,growth_streak,covered_streak,cfg,objective=objective)
        model['scale_feedback_update']=feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius
    try:
        initial=np.asarray(initial,float).copy()
        current=initial.copy(); vector=objective.vector(current)
        meta['initial_ordinary_timing']={}
        cd=objective.evaluate(vector)['decision']
        meta['initial_ordinary_timing']['coarse_after_required_value']=objective.problem.timing_snapshot()
        fd=objective.fine_decision(current)
        meta['initial_ordinary_timing']['fine_after_required_value']=objective.problem.timing_snapshot()
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        meta['initial_paid_scalar_comparison']=objective.compare_initial_paid_scalars(current,cd,fd)
        meta['initial_actual_two_grid_decisions']={
            'coarse':compact_with_all_actual_gates(cd),'fine':compact_with_all_actual_gates(fd)}
        accepted=objective.accepted_point(current,cd,fd,{
            'kind':'new-direct-reference-task-paid-current-best-physical-start',
            'source_physical_state_sha256':objective.direct_replay['canonical_physical_state_sha256'],
            'new_implementation_not_an_old_array_hash_replay':True})
        objective.install_reference(current)
        source=objective.direct_replay['source_checkpoint']
        if (objective.pool.tolist()!=source['coarse_pool']
                or objective.fine_pool.tolist()!=source['fine_pool']
                or (objective.pool_version,objective.fine_pool_version)!=(1,2)):
            raise ValueError('direct input pools changed before the first model')
        meta['initial_pool_handling']={
            'source_sizes':[len(objective.pool),len(objective.fine_pool)],
            'source_versions':[objective.pool_version,objective.fine_pool_version],
            'coarse_expand_calls':0,'fine_initialize_calls':0,
            'all_later_actual_trial_separation_and_learning_retained':True}
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
            allocation=primary_allocation(cfg,meta)
            meta['primary_allocation_decisions'].append(copy.deepcopy(allocation))
            if not allocation['primary_may_start']:
                meta['unpaired_primary_stop']=copy.deepcopy(allocation)
                return finish('new-pair-reservation-stopped-before-unpaired-primary')
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
            primary=objective.guarded_primary(current,base,J,groups,tols,trust,local,len(meta['models'])+1)
            affine=objective.primary_observable_model(primary)
            lp={}
            model={'number':len(meta['models'])+1,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'linearized_at_true_two_grid_max_eta':accepted['maximum_eta_on_both_grids'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'coarse_pool_version':versions[0],'fine_pool_version':versions[1],
                'trust_before_model':trust,'scale_feedback_trials':[],
                'SOC_hold_model_binding':model_binding(primary,model_center,accepted['physical_state_sha256'],versions),
                'primary_allocation_before_factory':copy.deepcopy(allocation),
                'linear_program':lp,'trials':[],'corrections':[]}; meta['models'].append(model)
            register_ordinary_context(objective,primary,affine,model_center,versions,model)
            objective.bind_guarded_primary(primary,affine,model)
            mark_previous_growth_used(meta['models'],model,objective=objective)
            p,lp=solve_reserved_primary(primary,affine,local,meta,progress=lp,wall=objective._wall,
                remaining_seconds=lambda:cfg['max_seconds']-(time.monotonic()-objective.optimization_started))
            objective._wall()
            if p is None:
                if lp.get('proposal_rejected_before_geometry')=='no-evaluated-affine-model-improvement-above-original-floor':
                    model['result']='no-evaluated-affine-spectral-improvement'
                    return finish('affine-spectral-finite-model-stalled')
                trust*=.5;model['result']='primary-LP-failed-trust-shrunk'
                trust=update_model_scale(model,trust)
                if trust<minimum_trust:return finish('minimum-trust-after-primary-failure')
                continue
            if lp['predicted_slack_improvement']<=cfg['linear_model_improvement_floor'] or np.max(abs(p))==0:
                model['result']='no-primary-metric-restoration';return finish('metric-restoration-linear-model-stalled')
            model['exact_binary64_independent_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_eta=accepted['maximum_eta_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None
            def assess(candidate,kind,alpha,need_fine=False,curve=None,prediction=None,curvature_reference=None,rebound_context=None):
                nonlocal current,accepted,succeeded,relearned
                if rebound_context is None:
                    diagnostic_base,diagnostic_J,diagnostic_groups=base,J,groups
                    active_affine,active_center,active_versions=affine,model_center,versions
                else:
                    require_current_layout(objective,rebound_context.failed)
                    diagnostic_base,diagnostic_J,diagnostic_groups=(
                        rebound_context.base,rebound_context.J,rebound_context.groups)
                    active_affine,active_center,active_versions=(
                        rebound_context.affine,rebound_context.failed.x,rebound_context.versions)
                objective.problem.coordinates.validate(candidate)
                exact_height=objective.problem.coordinates.exact_heights(candidate)
                if any(exact_height[j]!=objective.problem.coordinates.reference_exact[j] for j in [4,5]):
                    raise ArithmeticError('candidate changed fixed physical height slots4 or5')
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'physical_state_sha256':digest(objective.problem.identity(candidate)),
                    'exact_binary64_independent_coordinates':[str(Q.from_float(float(x))) for x in candidate],
                    'exact_original_physical_coefficients':[str(x) for x in objective.problem.coordinates.physical_exact(candidate)],
                    'attempt_status':'coarse-value-call-started'}
                if rebound_context is not None:
                    record['expanded_pool_rebound_revision']=1
                    record['rebound_complete_model_binding_sha256']=active_affine.binding_sha256
                    record['rebound_model_binding']=copy.deepcopy(rebound_context.binding)
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
                reference=(diagnostic_base,active_center,'accepted-basepoint-plus-J-total-step') if curvature_reference is None else curvature_reference
                record['curvature_nonlinear_defect_diagnostic']=curvature_trial_diagnostics(
                    objective,candidate,reference[0],diagnostic_J,diagnostic_groups,reference[1],reference[2],fine_present=f is not None)
                objective.observe_first_primary_defect(primary,model,record,candidate,
                    diagnostic_base,diagnostic_J,diagnostic_groups,active_versions)
                record['affine_metric_error_decomposition']=objective.actual_metric_error(
                    active_affine,candidate,fine_present=f is not None)
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
                record['inherited_proposal_prediction']=copy.deepcopy(prediction)
                prediction={'predicted_slack':active_affine.slack(candidate-active_center),
                    'model_kind':'accepted-base-affine-e-f-spectral-norm-at-actual-total-step',
                    'observable_binding_sha256':active_affine.binding_sha256,
                    'pool_versions':list(active_versions),'full_fine_actual_required_for_eta_ratio':True}
                if rebound_context is not None:
                    prediction['expanded_pool_rebound_revision']=1
                quality=trial_quality(old_eta,c,f,prediction,kind,cfg)
                record['scale_feedback']=quality;model['scale_feedback_trials'].append(quality)
                return c,f,record
            for bi in range(int(cfg['maximum_backtracks_per_model'])):
                alpha=str(Q(1,2**bi)); step=float(Q(alpha))*p
                remaining_before_trial=cfg['max_linear_models']-meta['linear_program_invocation_count']
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
                trial['SOC_LP_opportunity_allocation']={
                    'remaining_shared_LPs_before_trial':remaining_before_trial,
                    'original_may_SOC_resource_and_no_prior_arc_condition':bool(may_soc),
                    'original_actual_gates_and_branch_conditions_still_required':True,
                    'source_primary_allocation':copy.deepcopy(lp['primary_SOC_pair_allocation'])}
                if succeeded:model['result']='accepted-two-grid-true-metric-descent';break
                if relearned:
                    model['result']='new-rows-return-to-last-accepted-before-SOC'
                    eligibility={
                        'first_full_primary':bi==0 and alpha=='1' and kind=='primary-metric-short-step',
                        'no_prior_SOC_or_arc':not soc_used and arc is None,
                        'same_trial_not_accepted':trial['accepted_as_next_iterate'] is False,
                        'both_actual_grids_available_and_regular':bool(f is not None
                            and c.get('regularity_screen_pass',False)
                            and f.get('regularity_screen_pass',False)),
                        'original_shared_LP_room':meta['linear_program_invocation_count']<cfg['max_linear_models'],
                        'enlarged_pool_versions':versions!=(objective.pool_version,objective.fine_pool_version)}
                    model['expanded_pool_rebound_eligibility']=eligibility
                    if all(eligibility.values()):
                        # Capture y before any accepted-base restore. All new residuals
                        # come from these already computed complete original grids.
                        soc_used=True
                        trial_index=len(model['trials'])-1
                        cache_record={}
                        model['failed_y_post_learning_cache_restore']=cache_record
                        # Already-paid helper: reassemble only selected-layout caches.
                        # Its measured ordinary-call increment must be zero; miss exits.
                        restore_failed_y_layout(objective,y,cache_record)
                        cache_record['new_outer_scope']='same-y cache identity, original shared budgets'
                        cache_record['paid_helper_schema_and_failure_text_preserved']=True
                        failed=capture_failed_trial(objective,primary,model_center,y,versions,
                            model['SOC_hold_model_binding'],model['number'],trial_index,trial,cfg)
                        model['expanded_pool_same_failed_trial']=copy.deepcopy(failed.report)
                        model['actual_full_step_vs_original_proposal']={
                            'exact_binary64_actual_y_minus_x':[str(Q.from_float(float(v))) for v in failed.step],
                            'maximum_absolute_actual_minus_nominal_step':float(np.max(abs(failed.step-step))),
                            'no_nominal_step_substitution':True}
                        remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
                        local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
                        rebound=objective.rebuild_failed_context(failed,trust,local)
                        model['expanded_pool_rebound_registry_index']=rebound.record['rebound_context_index']
                        budget=rebound_budget(rebound,local)
                        model['expanded_pool_rebound_budget']=copy.deepcopy(budget)
                        objective._wall()
                        if not budget['finite_and_both_original_positive_gain_gates']:
                            model['result']='expanded-pool-model-has-no-positive-scalar-and-complete-gain'
                            break
                        require_current_layout(objective,failed)
                        soc={}
                        correction={
                            'primary_trial_index':trial_index,
                            'primary_trial_physical_sha256':trial['physical_state_sha256'],
                            'coarse_residual_evaluation':trial['coarse_physical_evaluation'],
                            'fine_residual_evaluation':trial['fine_value_evaluation'],
                            'coarse_pool_version':rebound.versions[0],
                            'fine_pool_version':rebound.versions[1],
                            'expanded_pool_rebound_revision':1,
                            'rebound_model_binding':copy.deepcopy(rebound.binding),
                            'rebound_complete_model_binding_sha256':rebound.affine.binding_sha256,
                            'original_primary_model_binding':copy.deepcopy(model['SOC_hold_model_binding']),
                            'same_failed_y_and_original_learning_preserved':True,
                            'linear_program':soc}
                        model['corrections'].append(correction)
                        # The new wrapper charges the ORIGINAL shared ledger before
                        # calling the unchanged original SOC LP math. No duplicate charge.
                        w,soc=solve_rebound_correction(rebound.primary,failed.views,failed.step,local,meta,
                            progress=soc,wall=objective._wall,
                            remaining_seconds=lambda:cfg['max_seconds']-(time.monotonic()-objective.optimization_started))
                        soc['same_step_scalar_and_affine_budget_comparison']={
                            'scalar_rho_source':'new selected minimum at actual y-x in frozen build_correction',
                            'minimum_scalar_slack_at_same_step':budget['new_scalar_slack_at_actual_d'],
                            'evaluated_affine_spectral_slack_at_same_step':budget['new_full_slack_at_actual_d'],
                            'raw_affine_minus_scalar_slack':budget['new_full_slack_at_actual_d']-budget['new_scalar_slack_at_actual_d'],
                            'minimum_scalar_not_above_affine_in_reported_floats':bool(
                                budget['new_scalar_slack_at_actual_d']<=budget['new_full_slack_at_actual_d']),
                            'original_SOC_rhs_if_built':soc.get('metric_slack_budget'),
                            'hypothetical_affine_rhs_not_used':budget['hypothetical_full_SOC_rhs_not_used'],
                            'original_rhs_no_larger_in_reported_floats':None if soc.get('metric_slack_budget') is None else bool(
                                soc['metric_slack_budget']<=budget['hypothetical_full_SOC_rhs_not_used']),
                            'selected_initial_slack_retained':budget['new_scalar_initial_slack'],
                            'full_initial_slack_retained':budget['new_full_initial_slack'],
                            'affine_model_scope':'rebound complete two grids, same actual y-x',
                            'rebound_complete_model_binding_sha256':rebound.affine.binding_sha256,
                            'primary_LP_auxiliary_not_substituted_for_either_minimum':True,
                            'frozen_SOC_rhs_and_solver_not_modified':True}
                        rebound.record.update(status='rebound-correction-returned',
                            correction_index=len(model['corrections'])-1,
                            correction_LP_invoked=bool(soc.get('LP_invoked')))
                        objective._wall()
                        if w is None:
                            model['result']='expanded-pool-SOC-no-qualified-correction-last-accepted-retained'
                            break
                        correction['exact_binary64_independent_correction']=[str(Q.from_float(float(v))) for v in w]
                        require_current_layout(objective,failed)
                        z=objective.subspace.apply(failed.y,w[objective.subspace.columns])
                        assess(z,'metric-SOC-corrected-short-step','1',
                            prediction={'predicted_slack':soc['corrected_actual_trial_linear_metric_slack'],
                                'model_kind':'same-actual-y-new-pool-rows-plus-new-base-J-correction',
                                'pool_versions':list(rebound.versions),
                                'full_fine_actual_required_for_eta_ratio':True},
                            curvature_reference=(rebound.trial_rows,failed.y,
                                'same-primary-y-actual-new-pool-rows-plus-rebuilt-x-J-correction'),
                            rebound_context=rebound)
                        corrected=model['trials'][-1]
                        correction['corrected_trial_index']=len(model['trials'])-1
                        correction['corrected_trial_physical_sha256']=corrected['physical_state_sha256']
                        correction['corrected_trial_added_rows']={
                            'coarse':corrected.get('new_coarse_rows',0),
                            'fine':corrected.get('new_fine_rows',0)}
                        model['original_failed_trial_learning_not_erased_for_SOC_hold']=True
                        if succeeded:
                            model['result']='accepted-full-SOC-two-grid-metric-descent'
                            model['accepted_expanded_pool_same_trial_SOC']=True
                            model['accepted_rebound_SOC_base_total_step_diagnostic']=actual_total_step_diagnostic(
                                rebound.primary,failed.x,failed.y,current,old_eta,
                                corrected['coarse_decision'],corrected['fine_decision'],
                                cfg=cfg,model_context=rebound.binding,
                                base_physical_sha256=failed.report['base_physical_state_sha256'],
                                primary_physical_sha256=failed.report['failed_physical_state_sha256'],
                                accepted_physical_sha256=accepted['physical_state_sha256'],
                                current_pool_versions=(objective.pool_version,objective.fine_pool_version))
                            # Keep original SOC_hold_model_binding/learning records.
                            # A new-pool correction is not an unchanged-layout hold witness.
                            model['accepted_rebound_diagnostic_not_substituted_for_original_hold_guard']=True
                            rebound.record['status']='rebound-corrected-point-accepted-by-original-two-grid-gates'
                        else:
                            new_again=bool(corrected.get('new_coarse_rows',0) or corrected.get('new_fine_rows',0))
                            model['result']=('expanded-pool-corrected-new-rows-last-accepted-retained'
                                if new_again else 'expanded-pool-corrected-trial-rejected-last-accepted-retained')
                            rebound.record['status']=model['result']
                        # Never recursively rebuild or start a new parabolic arc here.
                    break
                if may_soc and f is not None and c.get('regularity_screen_pass',False) and f.get('regularity_screen_pass',False):
                    soc_used=True
                    if versions!=(objective.pool_version,objective.fine_pool_version):
                        raise ArithmeticError('SOC old Jacobian cannot survive pool layout change')
                    trial_rows=np.r_[objective.constraint_fun(objective.vector(y)),
                        objective.fine_rows(y).reshape(-1)[objective.fine_pool]]
                    remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
                    local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
                    soc={}
                    correction={'primary_trial_index':len(model['trials'])-1,
                        'primary_trial_physical_sha256':digest(objective.problem.identity(y)),
                        'coarse_residual_evaluation':trial['coarse_physical_evaluation'],
                        'fine_residual_evaluation':trial['fine_value_evaluation'],
                        'coarse_pool_version':versions[0],'fine_pool_version':versions[1],
                        'same_layout_original_SOC_charged_before_call':True,'linear_program':soc}
                    model['corrections'].append(correction)
                    # The already-paid charged wrapper accepts any original primary
                    # and same-y full views; no rebound context is required here.
                    w,soc=solve_rebound_correction(
                        primary,objective.full_views(y),step,local,meta,progress=soc,
                        wall=objective._wall,
                        remaining_seconds=lambda:cfg['max_seconds']-(
                            time.monotonic()-objective.optimization_started))
                    soc['actual_scope']='same-layout original SOC; original RHS, arrays and scaling'
                    # build_correction recomputes the minimum scalar-row slack
                    # at THIS step; it does not use any primary LP auxiliary.
                    scalar_rho=float(soc['primary_predicted_metric_slack'])
                    affine_rho=affine.slack(step)
                    rho0=float(soc['initial_metric_slack'])
                    retention=float(Q(cfg['SOC_predicted_descent_retention_exact']))
                    hypothetical_affine_rhs=rho0-retention*(rho0-affine_rho)
                    actual_scalar_rhs=soc.get('metric_slack_budget')
                    soc['same_step_scalar_and_affine_budget_comparison']={
                        'scalar_rho_source':'frozen build_correction predicted_slack(primary, actual primary step)',
                        'minimum_scalar_slack_at_same_step':scalar_rho,
                        'evaluated_affine_spectral_slack_at_same_step':affine_rho,
                        'raw_affine_minus_scalar_slack':affine_rho-scalar_rho,
                        'minimum_scalar_not_above_affine_in_reported_floats':bool(scalar_rho<=affine_rho),
                        'original_SOC_rhs_if_built':actual_scalar_rhs,
                        'hypothetical_affine_rhs_not_used':hypothetical_affine_rhs,
                        'original_rhs_no_larger_in_reported_floats':None if actual_scalar_rhs is None else
                            bool(actual_scalar_rhs<=hypothetical_affine_rhs),
                        'primary_LP_auxiliary_not_substituted_for_either_minimum':True,
                        'frozen_SOC_rhs_and_solver_not_modified':True}
                    # The wrapper already charged exactly once before linprog.
                    objective._wall()
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
        return finish('direct-reference-guarded-recovery-error',error={'type':type(error).__name__,'message':str(error)})




def run_direct_reference_recovery(objective, initial, *, known_metric_locations=(),
                                  restored_controller=None, artificial_inputs_only=False,
                                  evaluate_only=False):
    """One independent task; the existing actual-gate and SOC paths are retained."""
    if not isinstance(objective, DirectReferenceGuardObjective):
        raise ValueError("explicit fresh direct-reference task objective required")
    result = _run_direct_reference_outer(objective, initial,
        known_metric_locations=known_metric_locations,
        restored_controller=restored_controller,
        artificial_inputs_only=artificial_inputs_only, evaluate_only=evaluate_only)
    result = attach_complete_model_reports(result, objective)
    legacy = result.pop("frozen_outer_recovery_function_was_called_without_monkeypatch", None)
    result.setdefault("inherited_scope_labels", {})[
        "frozen_outer_recovery_function_was_called_without_monkeypatch"] = legacy
    result["frozen_outer_recovery_function_was_called_without_monkeypatch"] = False
    result["explicit_source_derived_outer_without_monkeypatch"] = True
    result["outer_primary_call_change"] = (
        "paid guarded formula and repaired solver; same allocation rule within the independent64-LP task")
    result["outer_new_branch"] = (
        "direct ordinary evaluation, fresh438 information migration and four supplemental legal supports")
    result["empirical_guard_update_rule_is_inherited"] = True
    result["cross_center_norm_memory"] = objective.direction_bank.report()
    result = attach_rebound_reports(result, objective)
    solver = result["solver"]
    solver.setdefault("inherited_scope_labels", {})[
        "paid_covered_soft_outer_method"] = COVERED_POLICY
    solver["method"] = POLICY
    for model in solver.get("models", []):
        lp = model["linear_program"]
        inherited = lp.pop("original_primary_inner_cap_and_shared_LP_budget_not_changed", None)
        lp.setdefault("inherited_frozen_scope_labels", {})[
            "original_primary_inner_cap_and_shared_LP_budget_not_changed"] = inherited
        lp["original_primary_inner_cap_and_shared_LP_budget_not_changed"] = False
        lp["original_three_inner_upper_bound_retained"] = True
        lp["new_task_shared_primary_plus_SOC_LP_limit"] = 64
        lp["not_the_closed_old_twelve_LP_epoch"] = True
        lp["new_dynamic_primary_ceiling_may_be_stricter"] = True
        lp["primary_allocation_is_separate_from_SOC_eligibility_and_acceptance"] = True
    result["primary_SOC_pair_allocation_definition"] = allocation_definition()
    result["expanded_layout_SOC_radius_retention_definition"] = layout_hold_definition()
    result["initial_complete_checkpoint_bank_input"] = copy.deepcopy(objective.checkpoint_bank_input)
    result["original_radius_controller_and_all_its_fallbacks_retained"] = False
    result["frozen_radius_controller_called_once_and_all_fallbacks_retained"] = True
    result["all_paid_radius_controller_paths_and_covered_two_streak_rules_are_unchanged"] = True
    result["original_true_gates_SOC_RHS_and_per_LP_limit_retained"] = True
    result["new_task_total_limits"] = {"scientific_seconds":1800,"LPs":64,"values":160,"per_LP_seconds":10}
    result["old_stage_all_budgets_unchanged_labels_do_not_describe_this_independent_task"] = True
    result["primary_inner_allocation_and_same_layout_before_call_charge_are_new"] = False
    result["paid_grant_rule_and_before_call_charge_reused_with_new64_shared_limit"] = True
    result["historical_m10_or_previous_stage_replay_or_optimization_calls"] = 0
    result["covered_soft_ordinary_growth_definition"] = covered_growth_definition()
    decisions = []
    by_number = {m.get("number"): m for m in solver.get("models", [])}
    for m in solver.get("models", []):
        d = m.get("scale_feedback_update", {}).get("covered_soft_ordinary_growth")
        if not isinstance(d, dict):
            continue
        next_number = d.get("next_radius_used_by_model_number")
        if next_number is not None:
            following = by_number.get(next_number)
            if following is None or following.get("trust_before_model") != d["new_next_radius"]:
                raise ValueError("growth report lost its actual next-model radius")
            started = int(following.get("linear_program", {}).get("inner_call_count", 0))
            d["next_model_started_primary_LPs"] = started
            d["grown_radius_used_by_started_primary_LP"] = started > 0
            for copied in objective.trust_updates:
                q = copied.get("covered_soft_ordinary_growth")
                if isinstance(q, dict) and q.get("model_number") == m.get("number"):
                    q["next_model_started_primary_LPs"] = started
                    q["grown_radius_used_by_started_primary_LP"] = started > 0
        decisions.append(copy.deepcopy(d))
    result["covered_soft_ordinary_growth_observation"] = {
        "models_with_controller_update": len(decisions),
        "qualified_covered_ordinary_models": sum(
            d["qualified_covered_ordinary_model"] for d in decisions),
        "qualified_with_new_soft_IDs": sum(
            d["qualified_covered_ordinary_model"]
            and d.get("coverage", {}).get("new_soft_ID_count", 0) > 0 for d in decisions),
        "new_pairs_consumed": sum(d["new_pair_consumed"] for d in decisions),
        "new_growth_proposals": sum(d["grew_for_next_model_by_new_rule"] for d in decisions),
        "new_growth_used_by_later_model_factory": sum(
            d["grew_for_next_model_by_new_rule"]
            and d.get("next_radius_used_by_model_number") is not None for d in decisions),
        "new_growth_used_by_started_primary_LP": sum(
            d["grew_for_next_model_by_new_rule"]
            and d.get("grown_radius_used_by_started_primary_LP", False) for d in decisions),
        "frozen_fallback_updates": sum(not d["qualified_covered_ordinary_model"] for d in decisions),
        "final_legacy_streak": result["final_consecutive_growth_qualifying_models"],
        "final_new_covered_streak": result["final_covered_ordinary_growth_streak"],
        "bookkeeping": copy.deepcopy(objective.covered_growth_bookkeeping),
        "new_J_JVP_geometry_LP_value_calls_by_controller": 0,
        "all_old_learning_and_gate_records_retained": True,
        "proposed_growth_is_not_accepted_progress_or_a_convergence_claim": True}
    return attach_direct_task_reports(result, objective)
