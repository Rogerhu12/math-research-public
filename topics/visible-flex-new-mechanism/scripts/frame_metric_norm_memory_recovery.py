#!/usr/bin/env python3
"""Explicit memory-seeded outer variant of the published complete159 method.

The body below is source-derived from frame_metric_height159_affine_spectral.py
SHA256 5506a1696290869f1d0d7a2ef914663c09435d5d6f17b75c94ddb6cea8aae86d.
Only the primary-solver call is changed to the explicit memory-seeded solver.
No frozen function or module-global binding is monkeypatched.
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
    initial_restriction_decision, selected_model, solve_correction,
    predicted_slack, mapped_parabolic_candidate, curvature_arc_slack_bound,
    curvature_trial_diagnostics, trial_quality, EvaluationBudgetReached,
    require_public_research_environment, model_binding, next_soc_hold_trust)
from frame_metric_norm_direction_memory import (
    POLICY, RememberingCompleteObjective, solve_remembered_primary)
from frame_metric_height159_complete_affine import attach_complete_model_reports

def run_memory_outer(objective,initial,*,known_metric_locations=(),restored_controller=None,artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,AffineSpectralHeight159Objective):
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
            'affine_ef_spectral_primary_definition':model_definition(),
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
            affine=objective.primary_observable_model(primary)
            lp={}
            model={'number':len(meta['models'])+1,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'coarse_pool_version':versions[0],'fine_pool_version':versions[1],
                'trust_before_model':trust,'scale_feedback_trials':[],
                'SOC_hold_model_binding':model_binding(primary,model_center,accepted['physical_state_sha256'],versions),
                'linear_program':lp,'trials':[],'corrections':[]}; meta['models'].append(model)
            p,lp=solve_remembered_primary(primary,affine,local,meta,progress=lp,wall=objective._wall,
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
                record['affine_metric_error_decomposition']=objective.actual_metric_error(
                    affine,candidate,fine_present=f is not None)
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
                prediction={'predicted_slack':affine.slack(candidate-model_center),
                    'model_kind':'accepted-base-affine-e-f-spectral-norm-at-actual-total-step',
                    'observable_binding_sha256':affine.binding_sha256,
                    'pool_versions':list(versions),'full_fine_actual_required_for_eta_ratio':True}
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
        return finish('height159-affine-spectral-recovery-error',error={'type':type(error).__name__,'message':str(error)})




def run_memory_recovery(objective, initial, *, known_metric_locations=(),
                        restored_controller=None, artificial_inputs_only=False,
                        evaluate_only=False):
    if not isinstance(objective, RememberingCompleteObjective):
        raise ValueError("explicit norm-memory objective required")
    result = run_memory_outer(objective, initial,
        known_metric_locations=known_metric_locations,
        restored_controller=restored_controller,
        artificial_inputs_only=artificial_inputs_only, evaluate_only=evaluate_only)
    result = attach_complete_model_reports(result, objective)
    legacy = result.pop("frozen_outer_recovery_function_was_called_without_monkeypatch")
    result.setdefault("inherited_scope_labels", {})[
        "frozen_outer_recovery_function_was_called_without_monkeypatch"] = legacy
    result["frozen_outer_recovery_function_was_called_without_monkeypatch"] = False
    result["explicit_source_derived_outer_without_monkeypatch"] = True
    result["outer_primary_call_change"] = "solve_remembered_primary"
    result["solver"]["inherited_complete_method"] = result["solver"]["method"]
    result["solver"]["method"] = POLICY
    result["cross_center_norm_memory"] = objective.direction_bank.report()
    return result
