#!/usr/bin/env python3
"""One explicitly reassigned last-slot primary; original ordinary trials only.

The actual63/64 ledger and257.595331213 scientific seconds are inherited.
No source primary is rerun. The unchanged full-grid acceptance, actual learning
and ordinary backtracking/controller calls operate on the one NEW candidate.
There is no new SOC opportunity after LP64 and no second outer model.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import time
import numpy as np
import scipy
from frame_height_null_coordinates import digest
from frame_metric_height159_soc_hold import (
    restriction_definition, growth_definition, penalty_definition,
    scaling_definition, floor_definition, strip_floor_definition,
    fixed_domain_summary, compact_with_all_actual_gates,
    initial_restriction_decision, predicted_slack, curvature_trial_diagnostics,
    trial_quality, EvaluationBudgetReached, require_public_research_environment,
    model_binding)
from frame_metric_height159_affine_spectral import retention_definition
from frame_metric_height159_complete_affine import attach_complete_model_reports
from frame_metric_expanded_pool_soc import require_current_layout, attach_rebound_reports
from frame_metric_covered_soft_growth import (
    register_ordinary_context, next_covered_soft_growth_trust)
from frame_metric_curvature_defect_guard import attach_guard_reports
from frame_metric_terminal_paid_slot import (
    POLICY, definition, validate_release, prepare_terminal_support_model,
    solve_terminal_last_slot, SOURCE_SCIENCE_SECONDS, SOURCE_VALUES)
from frame_metric_terminal_paid_slot_resume import TerminalPaidSlotObjective
from frame_metric_terminal_paid_slot_transfer import require, IDENTITIES


def _run(objective, initial, *, restored_controller):
    require(isinstance(objective, TerminalPaidSlotObjective)
            and objective.terminal_paid_slot_policy == POLICY,
            "explicit same-task terminal512/4 objective required")
    require_public_research_environment()
    cfg, replay = objective.cfg, objective.resume_replay
    retention_definition(cfg)
    source_model = replay["source_model"]
    trust = float(Q(restored_controller["trust_binary64_exact"]))
    growth_streak = restored_controller["success_streak"]
    covered_streak = restored_controller["covered_ordinary_success_streak"]
    require(trust == restored_controller["trust_evaluated"] == .00025
            and type(growth_streak) is int and growth_streak == 0
            and type(covered_streak) is int and covered_streak == 0,
            "source terminal B and both actual zero streaks required")
    require(digest(objective.evaluation_definition) == IDENTITIES["objective"],
            "original final evaluation definition changed")
    meta = {
        "method": POLICY, "original_model_number": 28, "models": [],
        "nonlinear_minimize_invocation_count": 0,
        "linear_program_invocation_count": 63, "primary_LP_invocation_count": 62,
        "correction_LP_invocation_count": 1,
        "original_paid_ledger": copy.deepcopy(replay["inherited_ledger"]),
        "shared_max_LPs": 64, "shared_max_values": 160, "shared_active_seconds": 1800,
        "new_primary_limit": 1, "new_SOC_limit": 0,
        "old_LPs_or_trials_rerun": 0, "source_unknown_proposed_step_not_reconstructed": True,
        "restored_current_controller": copy.deepcopy(restored_controller),
        "historical_epoch_controller_initialization": copy.deepcopy(
            objective.evaluation_definition["height159_SOC_hold_controller_initialization"]),
        "numpy_version": np.__version__, "scipy_version": scipy.__version__}
    meta["terminal_release_eligibility"] = validate_release(source_model, cfg, meta)
    original_learning_commits = len(objective.curvature_defect_memory.commits)

    def finish(status, error=None, budget=None):
        # Empty source pending state is never committed again. Only a genuinely
        # new observed first trial may require this unchanged finalization.
        pending = list(objective.curvature_defect_memory.pending)
        if pending:
            objective.finalize_curvature_guard_learning()
        meta["final_learning_commit_scope"] = {
            "new_pending_event_indices_before_finalization": pending,
            "new_finalization_call_count": int(bool(pending)),
            "source35_events_and34_commits_not_replayed": True,
            "commits_after": len(objective.curvature_defect_memory.commits),
            "source_commit_count": original_learning_commits}
        snap = objective.snapshot()
        point = snap.get("selected_two_grid_physical_point")
        if objective.checkpoint:
            objective.checkpoint(snap)
        remaining = cfg["max_linear_models"]-meta["linear_program_invocation_count"]
        meta["final_shared_LP_allocation"] = {
            "original_limit": 64, "started_total": meta["linear_program_invocation_count"],
            "started_primary": meta["primary_LP_invocation_count"],
            "started_SOC": meta["correction_LP_invocation_count"],
            "remaining_unspent": remaining, "original_shared_limit_exhausted": remaining == 0,
            "new_primary_calls": meta["linear_program_invocation_count"]-63,
            "new_SOC_calls": meta["correction_LP_invocation_count"]-1,
            "no_slot_reset_or_virtual_charge": True}
        require(meta["linear_program_invocation_count"] in (63, 64)
                and meta["primary_LP_invocation_count"] == meta["linear_program_invocation_count"]-1
                and meta["correction_LP_invocation_count"] == 1,
                "terminal stage changed the original shared ledger")
        return {
            "status": status, "error": error, "budget_message": budget,
            "solver": meta, "checkpoint": snap,
            "last_restricted_trust": trust,
            "final_consecutive_growth_qualifying_models": growth_streak,
            "final_covered_ordinary_growth_streak": covered_streak,
            "new_metric_target_reached_on_both_grids": bool(
                point and point["new_metric_target_qualified_on_both_grids"]),
            "original_true_gate_tolerances_and_strict_descent_retained": True,
            "no_new_SOC_or_rebound_solver_calls": True,
            "original_ordinary_backtracking_learning_and_controller_fallbacks_retained": True,
            "one_model_no_same_stage_extension": True,
            "curvature_proposal_floor": floor_definition(cfg),
            "strip_proposal_floor": strip_floor_definition(cfg),
            "primary_physical_step_cost": penalty_definition(cfg),
            "adaptive_trust_policy": growth_definition(cfg),
            "SOC_reversible_scaling_definition_historical": scaling_definition(cfg),
            "entry_tail_height159": restriction_definition(cfg)}

    def update_model_scale(model, proposed):
        nonlocal growth_streak, covered_streak
        radius, growth_streak, covered_streak, feedback = next_covered_soft_growth_trust(
            model, proposed, growth_streak, covered_streak, cfg, objective=objective)
        model["scale_feedback_update"] = feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius

    try:
        objective._wall()
        initial = np.asarray(initial, float).copy()
        current = initial.copy()
        cd = objective.evaluate(objective.vector(current))["decision"]
        meta["initial_ordinary_timing"] = {"coarse": objective.problem.timing_snapshot()}
        fd = objective.fine_decision(current)
        meta["initial_ordinary_timing"]["fine"] = objective.problem.timing_snapshot()
        meta["restored_current_actual_two_grid_decisions"] = {
            "coarse": compact_with_all_actual_gates(cd),
            "fine": compact_with_all_actual_gates(fd)}
        if not (cd["single_grid_admissible_recovery_point"] and fd["single_grid_admissible_recovery_point"]):
            return finish("restored-center-original-actual-gate-failed")
        accepted = objective.bind_restored_current_cache(current, cd, fd)
        objective.install_reference(current)
        require(objective.pool.tolist() == replay["source_checkpoint"]["coarse_pool"]
                and objective.fine_pool.tolist() == replay["source_checkpoint"]["fine_pool"]
                and (objective.pool_version, objective.fine_pool_version) == (7, 6),
                "terminal pools must not be initialized or expanded")
        flags = {label: compact_with_all_actual_gates(value)["actual_gate_booleans"]
                 for label, value in (("coarse", cd), ("fine", fd))}
        preflight = initial_restriction_decision(
            fixed_domain_summary(objective.subspace, objective.full_views(current)), flags,
            new_target_qualified=bool(accepted["new_metric_target_qualified_on_both_grids"]),
            minimum_drop_exact=cfg["minimum_accepted_eta_decrease_exact"],
            target_exact=cfg["fixed_metric_budget_exact"], actual_eta_tolerance=cfg["direct_eta_tolerance"])
        meta["initial_pre_LP_decision"] = preflight
        if not preflight["may_call_LP"]:
            return finish(preflight["status"])
        if accepted["new_metric_target_qualified_on_both_grids"]:
            return finish("new-metric-target-already-qualified")
        minimum_trust = float(Q(cfg["minimum_trust_box_fraction_exact"]))
        drop = float(Q(cfg["minimum_accepted_eta_decrease_exact"]))
        if trust < minimum_trust:
            return finish("inherited-controller-below-original-minimum")
        objective.begin_optimization()  # Marks a phase only; never resets the inherited clock.
        for terminal_model_once in range(1):
            objective._wall()
            base, J, groups, tols = objective.linear_rows(objective.vector(current))
            versions = (objective.pool_version, objective.fine_pool_version)
            model_center = current.copy()
            primary = objective.guarded_primary(current, base, J, groups, tols, trust, cfg, 28)
            affine = objective.primary_observable_model(primary)
            allocation = {
                "policy": POLICY, "source_original_allocation":
                    copy.deepcopy(source_model["primary_allocation_before_factory"]),
                "shared_LP_limit": 64, "started_shared_LPs_before_primary": 63,
                "remaining_shared_LPs_before_primary": 1,
                "primary_inner_calls_granted": 1, "primary_absolute_ceiling": 64,
                "remaining_SOC_opportunities": 0,
                "only_a_distinct_added_support_authorizes_the_reassignment": True,
                "source_cfg_unchanged": True}
            lp = {}
            model = {
                "number": 28, "source_model_number": 28,
                "continuation_record_ordinal": 1,
                "original_MODEL28_record_not_overwritten": True,
                "linearized_at_accepted_index": accepted["accepted_index"],
                "linearized_at_physical_sha256": accepted["physical_state_sha256"],
                "linearized_at_true_two_grid_max_eta": accepted["maximum_eta_on_both_grids"],
                "coarse_pool_rows": len(objective.pool), "fine_pool_rows": len(objective.fine_pool),
                "coarse_pool_version": versions[0], "fine_pool_version": versions[1],
                "trust_before_model": trust, "scale_feedback_trials": [],
                "SOC_hold_model_binding": model_binding(
                    primary, model_center, accepted["physical_state_sha256"], versions),
                "primary_allocation_before_factory": copy.deepcopy(allocation),
                "linear_program": lp, "trials": [], "corrections": []}
            meta["models"].append(model)
            prepared = prepare_terminal_support_model(
                primary, affine, source_model, cfg, meta, wall=objective._wall, progress=lp)
            if prepared is not None:
                affine = prepared
                objective.complete_models[-1] = affine
                primary.affine_spectral_model = affine
            # The coverage context must own the final live wrapper, not a
            # replaced intermediate model with the same numerical hash.
            register_ordinary_context(objective, primary, affine, model_center, versions, model)
            objective.bind_guarded_primary(primary, affine, model)
            if prepared is None:
                model["result"] = "no-distinct-paid-support-no-new-LP"
                return finish("terminal-slot-no-new-support-kept-unspent")
            p, lp = solve_terminal_last_slot(
                primary, affine, cfg, meta, progress=lp, wall=objective._wall,
                remaining_seconds=lambda: cfg["max_seconds"]-(time.monotonic()-objective.scientific_started))
            model["linear_program"] = lp
            lp["primary_SOC_pair_allocation"] = copy.deepcopy(allocation)
            objective._wall()
            if p is None:
                if lp.get("proposal_rejected_before_geometry") or meta["linear_program_invocation_count"] == 63:
                    model["result"] = "terminal-paid-support-no-returnable-affine-descent"
                    return finish("terminal-slot-without-returnable-step-not-stationarity")
                trust *= .5
                model["result"] = "primary-LP-failed-trust-shrunk"
                trust = update_model_scale(model, trust)
                return finish("terminal-single-primary-failed-original-controller-applied")
            require(meta["linear_program_invocation_count"] == 64,
                    "a returned terminal candidate must have charged LP64")
            if lp["predicted_slack_improvement"] <= cfg["linear_model_improvement_floor"] or np.max(abs(p)) == 0:
                model["result"] = "no-primary-metric-restoration"
                return finish("terminal-returned-step-below-original-descent-floor")
            model["exact_binary64_independent_proposed_step"] = [str(Q.from_float(float(x))) for x in p]
            old_eta = accepted["maximum_eta_on_both_grids"]
            succeeded = False
            relearned = False
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
            for bi in range(int(cfg["maximum_backtracks_per_model"])):
                alpha = str(Q(1, 2**bi))
                step = float(Q(alpha))*p
                y = objective.subspace.apply(current, step[objective.subspace.columns])
                prediction = {
                    "predicted_slack": predicted_slack(primary, step),
                    "model_kind": "basepoint-plus-J-step",
                    "pool_versions": list(versions),
                    "full_fine_actual_required_for_eta_ratio": True}
                c, f, trial = assess(y, "primary-metric-short-step", alpha,
                                     False, None, prediction)
                trial["SOC_LP_opportunity_allocation"] = {
                    "remaining_shared_LPs_before_trial": 0,
                    "original_may_SOC_resource_and_no_prior_arc_condition": False,
                    "source_primary_allocation": copy.deepcopy(allocation),
                    "final_original_slot_was_explicitly_reassigned_to_primary": True,
                    "no_SOC_solver_or_rebound_J_construction": True}
                if succeeded:
                    model["result"] = "accepted-two-grid-true-metric-descent"
                    break
                if relearned:
                    model["result"] = "new-rows-return-to-last-accepted-before-SOC"
                    break
            if succeeded and accepted["new_metric_target_qualified_on_both_grids"]:
                return finish("fixed-new-metric-target-qualified-on-both-grids")
            original_minimum_reached = False
            if not succeeded and not relearned:
                trust *= .5
                model["result"] = "all-proposals-rejected-last-accepted-retained"
                original_minimum_reached = trust < minimum_trust
            trust = update_model_scale(model, trust)
            if trust < minimum_trust:
                return finish("minimum-trust-after-original-backtracking" if original_minimum_reached
                              else "minimum-trust-after-actual-model-quality-feedback")
            return finish("terminal-single-primary-original-ordinary-path-complete")
        return finish("terminal-single-model-interface-complete")
    except EvaluationBudgetReached as error:
        return finish("shared-value-time-or-pool-budget-exit", budget=str(error))
    except Exception as error:
        return finish("terminal-paid-slot-recovery-error",
                      error={"type": type(error).__name__, "message": str(error)})


def run_terminal_paid_slot_recovery(objective, initial, *, restored_controller):
    result = _run(objective, initial, restored_controller=restored_controller)
    result = attach_complete_model_reports(result, objective)
    result = attach_rebound_reports(result, objective)
    result = attach_guard_reports(result, objective)
    result["method"] = POLICY
    result["terminal_paid_slot_definition"] = definition()
    result["terminal_paid_slot_resume"] = copy.deepcopy(objective.resume_metadata)
    result["cross_center_norm_memory"] = objective.direction_bank.report()
    result["initial_complete_checkpoint_bank_input"] = copy.deepcopy(objective.checkpoint_bank_input)
    result["original_bank_replay"] = copy.deepcopy(objective.initial_bank_replay)
    result["new_LPs_started_this_attempt"] = result["solver"]["linear_program_invocation_count"]-63
    result["new_primary_started_this_attempt"] = result["solver"]["primary_LP_invocation_count"]-62
    result["new_SOC_started_this_attempt"] = result["solver"]["correction_LP_invocation_count"]-1
    result["new_shared_values_this_attempt"] = objective.full_value_evaluations-SOURCE_VALUES
    result["new_scientific_seconds_this_attempt"] = (
        time.monotonic()-objective.scientific_started-SOURCE_SCIENCE_SECONDS)
    result["new_candidate_step_record"] = copy.deepcopy(
        getattr(objective.complete_models[-1], "new_candidate_step_record", None)
        if objective.complete_models else None)
    result["full_original_task_ledger_and_clock_retained"] = True
    result["no_old_LP_developer_or_unknown_direction_replay"] = True
    result["source_current_point_and_new_acceptances_have_original_indices"] = True
    result["frozen_end_learning_not_committed_again"] = True
    return result
