#!/usr/bin/env python3
"""Explicit finite-cone primary/ordinary-trial outer; no legacy LP or SOC call."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import time
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_height159_soc_hold import (
    restriction_definition, growth_definition, penalty_definition,
    floor_definition, strip_floor_definition, fixed_domain_summary,
    compact_with_all_actual_gates, initial_restriction_decision,
    predicted_slack, curvature_trial_diagnostics, trial_quality,
    EvaluationBudgetReached, require_public_research_environment, model_binding)
from frame_metric_height159_affine_spectral import retention_definition
from frame_metric_expanded_pool_soc import require_current_layout
from frame_metric_covered_soft_growth import (
    register_ordinary_context, next_covered_soft_growth_trust)
from frame_metric_curvature_defect_guard import attach_guard_reports
from frame_metric_finite_cone_primary import (
    POLICY, FiniteConePrimary, snapshot_binding, solve_finite_cone_once, require)
from frame_metric_finite_cone_epoch import (
    FiniteConeObjective, LIMITS, MAX_CONES_PER_MODEL, SETTINGS, CANDIDATE_STATUSES,
    SOURCE_SCIENCE_SECONDS, SOURCE_VALUES, SOURCE_LEGACY_COUNTS, definition)


def _initial_tags(model):
    """Keep every selected metric branch; bank/support tags add legitimate rows."""
    raw = list(model.selected_model.tags)
    raw += [item["original_row"] for item in model.bank.entries.values()]
    raw += [item["original_row"] for item in model.supplemental_normals]
    result, seen = [], set()
    for tag in raw:
        key = (tag["grid"], tag["flat_row_id"])
        if key not in seen:
            seen.add(key)
            result.append(copy.deepcopy(tag))
    return result


def solve_cone_model(objective, primary, model, progress):
    """At most four separately charged cones, using the actual whole-grid oracle.

    Existing supporting rows are assembled once and retained throughout this
    model. New full cone rows come only from actually observed violating original
    attainers. Upward full-rho repair makes an earlier incumbent feasible for every
    later cone; that property is checked again before a return.
    """
    ledger, cfg = objective.cone_ledger, objective.cfg
    start_count = ledger.cone_started
    ceiling = min(start_count+MAX_CONES_PER_MODEL, LIMITS["max_new_cone_calls"])
    progress.update(
        policy=POLICY, backend="clarabel", LP_invoked=False,
        inherited_container_name_is_not_an_LP_invocation=True,
        cone_calls=[], cone_expansions=[], inner_call_count=0,
        new_legacy_LP_calls=0, new_SOC_calls=0,
        independent_absolute_cone_ceiling=ceiling,
        original_shared_HiGHS_counts=copy.deepcopy(SOURCE_LEGACY_COUNTS),
        model=model.summary(), status="finite-cone-primary-not-started")
    A, b, support = model.initial_cuts()
    progress["retained_support_bundle"] = copy.deepcopy(support)
    tags = _initial_tags(model)
    seen = {(t["grid"], t["flat_row_id"]) for t in tags}
    incumbent, last_prepared, stop = None, None, None
    for inner in range(MAX_CONES_PER_MODEL):
        objective._wall()
        if ledger.cone_started >= ceiling:
            stop = "new-cone-total-or-per-model-call-limit"
            break
        prepared = FiniteConePrimary(
            primary, model, cfg, tags, retained_A=A, retained_b=b,
            retained_record=support, expected_current_binding=snapshot_binding(primary, model, cfg),
            wall=objective._wall)
        last_prepared = prepared
        candidate, event = solve_finite_cone_once(
            prepared, ledger=ledger, absolute_primary_ceiling=ceiling,
            settings_parameters=SETTINGS, candidate_statuses=CANDIDATE_STATUSES,
            progress=progress)
        progress["inner_call_count"] = ledger.cone_started-start_count
        event["inner_index"] = inner
        if candidate is None:
            stop = "cone-return-not-eligible-under-original-repair-gates"
            break
        candidate["inner_index"] = inner
        if incumbent is None or candidate["objective"] < incumbent["objective"]:
            incumbent = candidate
        # These are the already-paid full affine values of this returned vector.
        # Reading the oracle cache does not re-evaluate physical geometry.
        observed = model.oracle.evaluate(candidate["step"])
        event["complete_original_grid_attainers"] = copy.deepcopy(observed["attainers"])
        event["complete_original_grid_maxima"] = np.asarray(observed["phi"]).tolist()
        bank_before = model.bank.state_digest()
        for attainer in observed["attainers"]:
            model.bank.remember(model, attainer["original_row"],
                                attainer["affine_e"], attainer["affine_f"])
        event["direction_memory_after_actual_observation"] = {
            "before_sha256": bank_before, "after_sha256": model.bank.state_digest(),
            "original_retained_A_b_remain_in_this_model": True}
        if candidate["gap_met"]:
            stop = "full-affine-epigraph-gap-met"
            break
        added = []
        raw_rho = event["original_solver_rho"]
        for attainer in observed["attainers"]:
            tag = attainer["original_row"]
            if float(attainer["phi"])-model.target-raw_rho <= candidate["gap_tolerance"]:
                continue
            key = (tag["grid"], tag["flat_row_id"])
            if key not in seen:
                seen.add(key)
                tags.append(copy.deepcopy(tag))
                added.append(copy.deepcopy(tag))
        progress["cone_expansions"].append({
            "after_inner_index": inner, "new_original_cone_rows": added,
            "total_distinct_cone_rows": len(tags),
            "source_direction_sha256": observed["direction_sha256"],
            "new_rows_from_actual_full_grid_attainers_only": True,
            "retained_support_A_sha256": support["A_sha256"],
            "retained_support_b_sha256": support["b_sha256"]})
        if not added:
            stop = "no-new-violated-original-cone-row-in-observed-four-maxima"
            break
        if ledger.cone_started >= ceiling:
            stop = "new-cone-total-or-per-model-call-limit-after-new-row-observation"
            break
    if stop is None:
        stop = "declared-four-cone-loop-ended"
    progress["status"] = stop
    progress["inner_call_count"] = ledger.cone_started-start_count
    progress["new_cone_calls_started"] = ledger.cone_started-start_count
    progress["all_new_solver_calls_charged_before_backend_constructor"] = True
    progress["finite_cone_count_final"] = len(tags)
    if incumbent is None:
        progress.update(returned_candidate=False,
                        proposal_rejected_before_geometry="no-original-gate-qualified-cone-candidate")
        return None, progress
    objective._wall()
    # Rebuild only if the final observation appended unassembled original cones.
    # This involves necessary row/J binding, not another solver or physical value.
    if last_prepared is None or last_prepared.tags != tags:
        last_prepared = FiniteConePrimary(
            primary, model, cfg, tags, retained_A=A, retained_b=b,
            retained_record=support, expected_current_binding=snapshot_binding(primary, model, cfg),
            wall=objective._wall)
    final_linear = last_prepared.linear.residual(incumbent["variables"])
    final_cones = last_prepared.cone_residual(incumbent["variables"])
    require(max(final_linear["maximum_original_linear_row_violation"],
                final_linear["maximum_original_linear_bound_violation"],
                final_cones["maximum_metric_violation"]) <= cfg["linear_model_residual_limit"],
            "earlier full-rho incumbent failed a later valid original cone")
    step = incumbent["step"]
    norms = primary.subspace.step_norms(step, primary.width)
    physical = primary.subspace.M@step
    progress.update(
        returned_candidate=bool(incumbent["gain"] > cfg["linear_model_improvement_floor"]),
        returned_inner_index=incumbent["inner_index"],
        returned_epigraph_gap_met=incumbent["gap_met"],
        returned_inexact_finite_cone_model=not incumbent["gap_met"],
        # This inherited name is an interface for ordinary control only.
        returned_inexact_cut_model=not incumbent["gap_met"],
        predicted_metric_slack=incumbent["rho"],
        predicted_slack_improvement=incumbent["gain"],
        normalized_step_norm=incumbent["norm_auxiliary"],
        maximum_linear_row_violation=final_linear["maximum_original_linear_row_violation"],
        maximum_linear_bound_violation=final_linear["maximum_original_linear_bound_violation"],
        maximum_absolute_physical_step=float(np.max(abs(physical))),
        maximum_absolute_independent_step=float(np.max(abs(step))),
        repaired_original_residual=final_linear,
        repaired_included_cone_residual=final_cones,
        primary_step_cost_diagnostic={
            "returned_weighted_objective": incumbent["objective"],
            "returned_predicted_metric_slack": incumbent["rho"],
            "repaired_rho_auxiliary": incumbent["repaired_rho_auxiliary"],
            "retained_solver_norm_auxiliary": incumbent["norm_auxiliary"],
            "actual_physical_box_normalized_step_norm": norms["physical_infinity"],
            "actual_common_body_radius_norm": norms["common_body_radius_norm"],
            "actual_trust_normalized_step_norm": norms["common_body_radius_norm"]/primary.trust,
            "actual_block_box_normalized_step_norm": norms["common_body_radius_norm"],
            "body_utilization": norms["body_physical_normalized"]/primary.trust,
            "tail_utilization": norms["tail_physical_normalized"]/(primary.trust/8),
            "height_utilization": norms["height_physical_normalized"]/(4*primary.trust)},
        new_candidate_step_record={
            "exact_binary64_independent_step": [str(Q.from_float(float(x))) for x in step],
            "array_sha256": array_digest(step),
            "source_cone_inner_index": incumbent["inner_index"],
            "source": "actual returned repaired cone incumbent"})
    if not progress["returned_candidate"]:
        progress["proposal_rejected_before_geometry"] = "no-evaluated-affine-model-improvement-above-original-floor"
        return None, progress
    return step.copy(), progress


def _run(objective, initial, *, restored_controller):
    require(isinstance(objective, FiniteConeObjective)
            and objective.finite_cone_policy == POLICY, "explicit finite-cone objective required")
    require_public_research_environment()
    cfg, ledger, replay = objective.cfg, objective.cone_ledger, objective.finite_cone_replay
    retention_definition(cfg)
    trust = float(Q(restored_controller["trust_binary64_exact"]))
    growth_streak = restored_controller["success_streak"]
    covered_streak = restored_controller["covered_ordinary_success_streak"]
    require(trust == restored_controller["trust_evaluated"] == .000125
            and growth_streak == covered_streak == 0
            and type(growth_streak) is int and type(covered_streak) is int,
            "actual latest B=1/8000 and two zero streaks required")
    meta = {
        "method": POLICY, "models": [], "new_limits": copy.deepcopy(LIMITS),
        "max_cone_calls_per_model": MAX_CONES_PER_MODEL,
        "nonlinear_minimize_invocation_count": 0,
        **copy.deepcopy(SOURCE_LEGACY_COUNTS),
        "new_legacy_LP_invocation_count": 0, "new_SOC_invocation_count": 0,
        "SOC_reservation_policy": "none; no legacy/SOC calls authorized",
        "restored_actual_controller": copy.deepcopy(restored_controller),
        "source_legacy_counts_are_history_not_available_solver_allowance": True,
        "original_cfg_limits_retained_for_derivative_identity_and_global_caps": True,
        "source_current_accepted_index": 27,
        "new_method_identity": copy.deepcopy(objective.evaluation_definition["finite_cone_primary_method"]),
        "numpy_version": np.__version__}
    minimum_trust = float(Q(cfg["minimum_trust_box_fraction_exact"]))
    drop = float(Q(cfg["minimum_accepted_eta_decrease_exact"]))

    def finish(status, error=None, budget=None):
        pending = list(objective.curvature_defect_memory.pending)
        if pending:
            objective.finalize_curvature_guard_learning()
        meta["final_learning_commit"] = {
            "pending_before": pending, "new_finalize_call_count": int(bool(pending)),
            "source_pending0_never_replayed": True}
        meta["new_cone_ledger"] = ledger.report()
        require(all(meta[k] == v for k, v in SOURCE_LEGACY_COUNTS.items()),
                "a closed legacy solver counter changed")
        snapshot = objective.snapshot()
        point = snapshot.get("selected_two_grid_physical_point")
        if objective.checkpoint:
            objective.checkpoint(snapshot)
        return {
            "status": status, "error": error, "budget_message": budget,
            "solver": meta, "checkpoint": snapshot,
            "last_restricted_trust": trust,
            "final_consecutive_growth_qualifying_models": growth_streak,
            "final_covered_ordinary_growth_streak": covered_streak,
            "new_metric_target_reached_on_both_grids": bool(
                point and point["new_metric_target_qualified_on_both_grids"]),
            "finite_cone_definition": definition(),
            "adaptive_trust_policy": growth_definition(cfg),
            "curvature_proposal_floor": floor_definition(cfg),
            "strip_proposal_floor": strip_floor_definition(cfg),
            "primary_physical_step_cost": penalty_definition(cfg),
            "entry_tail_height159": restriction_definition(cfg),
            "original_two_grid_gates_and_strict_descent_unchanged": True,
            "original_ordinary_learning_backtracking_and_controller_fallbacks_retained": True,
            "no_new_SOC_or_legacy_solver_calls": True,
            "stopping_is_not_a_stationarity_or_continuous_feasibility_claim": True}

    def update_scale(model, proposed):
        nonlocal growth_streak, covered_streak
        radius, growth_streak, covered_streak, feedback = next_covered_soft_growth_trust(
            model, proposed, growth_streak, covered_streak, cfg, objective=objective)
        model["scale_feedback_update"] = feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius

    try:
        current = np.asarray(initial, float).copy()
        objective._wall()
        coarse_record = objective.evaluate(objective.vector(current))
        cd = coarse_record["decision"]
        meta["initial_ordinary_timing"] = {"coarse": objective.problem.timing_snapshot()}
        fd = objective.fine_decision(current)
        meta["initial_ordinary_timing"]["fine"] = objective.problem.timing_snapshot()
        meta["initial_actual_two_grid_decisions"] = {
            label: compact_with_all_actual_gates(value)
            for label, value in (("coarse", cd), ("fine", fd))}
        accepted = objective.bind_restored_current_cache(current, cd, fd)
        objective.install_reference(current)
        require((objective.pool_version, objective.fine_pool_version) == (8, 6)
                and objective.pool.tolist() == replay["source_checkpoint"]["coarse_pool"]
                and objective.fine_pool.tolist() == replay["source_checkpoint"]["fine_pool"],
                "initial ordinary reads must not initialize or expand either pool")
        flags = {label: compact_with_all_actual_gates(value)["actual_gate_booleans"]
                 for label, value in (("coarse", cd), ("fine", fd))}
        preflight = initial_restriction_decision(
            fixed_domain_summary(objective.subspace, objective.full_views(current)), flags,
            new_target_qualified=bool(accepted["new_metric_target_qualified_on_both_grids"]),
            minimum_drop_exact=cfg["minimum_accepted_eta_decrease_exact"],
            target_exact=cfg["fixed_metric_budget_exact"], actual_eta_tolerance=cfg["direct_eta_tolerance"])
        meta["initial_pre_solver_decision"] = preflight
        if not preflight["may_call_LP"]:
            return finish(preflight["status"])
        if accepted["new_metric_target_qualified_on_both_grids"]:
            return finish("new-metric-target-already-qualified")
        if trust < minimum_trust:
            return finish("inherited-controller-below-original-minimum")
        objective.begin_optimization()
        while ledger.cone_started < LIMITS["max_new_cone_calls"]:
            objective._wall()
            base, J, groups, tols = objective.linear_rows(objective.vector(current))
            versions = (objective.pool_version, objective.fine_pool_version)
            model_center = current.copy()
            number = len(meta["models"])+1
            primary = objective.guarded_primary(current, base, J, groups, tols, trust, cfg, number)
            affine = objective.primary_observable_model(primary)
            lp = {}
            model = {
                "number": number, "historical_models_not_relabelled_as_this_new_method": True,
                "linearized_at_accepted_index": accepted["accepted_index"],
                "linearized_at_physical_sha256": accepted["physical_state_sha256"],
                "linearized_at_true_two_grid_max_eta": accepted["maximum_eta_on_both_grids"],
                "coarse_pool_rows": len(objective.pool), "fine_pool_rows": len(objective.fine_pool),
                "coarse_pool_version": versions[0], "fine_pool_version": versions[1],
                "trust_before_model": trust, "scale_feedback_trials": [],
                "SOC_hold_model_binding": model_binding(
                    primary, model_center, accepted["physical_state_sha256"], versions),
                "linear_program": lp,
                "linear_program_key_is_only_an_inherited_controller_container": True,
                "trials": [], "corrections": []}
            meta["models"].append(model)
            register_ordinary_context(objective, primary, affine, model_center, versions, model)
            objective.bind_guarded_primary(primary, affine, model)
            if len(meta["models"]) > 1:
                old = meta["models"][-2].get("scale_feedback_update", {}).get("covered_soft_ordinary_growth")
                if isinstance(old, dict) and old.get("any_actual_radius_growth"):
                    require(old["new_next_radius"] == trust, "actual next factory radius changed")
                    old.update(next_radius_used_by_model_number=number,
                               next_model_factory_used_radius=True,
                               next_model_started_cone_calls=None)
            p, lp = solve_cone_model(objective, primary, affine, lp)
            model["linear_program"] = lp
            if len(meta["models"]) > 1:
                old = meta["models"][-2].get("scale_feedback_update", {}).get("covered_soft_ordinary_growth")
                if isinstance(old, dict) and old.get("next_radius_used_by_model_number") == number:
                    old["next_model_started_cone_calls"] = lp["inner_call_count"]
            objective._wall()
            affine.oracle.set_post_primary_phase()
            if p is None:
                model["result"] = "no-returnable-finite-cone-affine-step"
                return finish("finite-cone-model-no-returnable-step-not-stationarity")
            if lp["predicted_slack_improvement"] <= cfg["linear_model_improvement_floor"] or np.max(abs(p)) == 0:
                model["result"] = "no-primary-metric-restoration"
                return finish("finite-cone-returned-step-below-original-descent-floor")
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
                objective._wall()
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
                trial["new_solver_opportunity"] = {
                    "new_cone_calls_remaining": LIMITS["max_new_cone_calls"]-ledger.cone_started,
                    "new_SOC_calls_authorized": 0,
                    "closed_old_HiGHS_calls": 64,
                    "no_SOC_solver_or_rebound_J_construction": True}
                if succeeded:
                    model["result"] = "accepted-two-grid-true-metric-descent"
                    break
                if relearned:
                    model["result"] = "new-rows-return-to-last-accepted-no-SOC-authorized"
                    break
            if succeeded and accepted["new_metric_target_qualified_on_both_grids"]:
                return finish("fixed-new-metric-target-qualified-on-both-grids")
            original_minimum_reached = False
            if not succeeded and not relearned:
                trust *= .5
                model["result"] = "all-proposals-rejected-last-accepted-retained"
                original_minimum_reached = trust < minimum_trust
            trust = update_scale(model, trust)
            if trust < minimum_trust:
                return finish("minimum-trust-after-original-backtracking" if original_minimum_reached
                              else "minimum-trust-after-actual-model-quality-feedback")
        return finish("new-finite-cone-solver-allowance-exhausted")
    except EvaluationBudgetReached as error:
        return finish("finite-cone-new-or-global-value-time-or-pool-budget-exit", budget=str(error))
    except Exception as error:
        return finish("finite-cone-recovery-error",
                      error={"type": type(error).__name__, "message": str(error)})


def run_finite_cone_recovery(objective, initial, *, restored_controller):
    result = _run(objective, initial, restored_controller=restored_controller)
    # Do not reuse the old attach function's literal claim that its frozen LP
    # inner cap and outer budget are unchanged. This is an explicitly new method.
    models = result["solver"]["models"]
    require(len(models) <= len(objective.complete_models),
            "model records outnumber actual complete factories")
    for record, actual in zip(models, objective.complete_models):
        record["complete_model"] = actual.complete_report()
        record["linear_program"]["complete_original_grid_model"] = copy.deepcopy(record["complete_model"])
        record["all_original_linear_rows_and_retained_supports_kept"] = True
        record["new_solver_kind"] = "clarabel-finite-lorentz-cones"
    result = attach_guard_reports(result, objective)
    inherited_guard = result.pop("curvature_defect_guard_observation")
    result["inherited_guard_observation_full_history"] = inherited_guard
    result["finite_cone_learning_observation"] = {
        "source_events": 36, "source_commits": 35,
        "new_first_primary_samples": len(objective.curvature_defect_memory.events)-36,
        "new_commits": len(objective.curvature_defect_memory.commits)-35,
        "pending": len(objective.curvature_defect_memory.pending),
        "initial_learning_state": copy.deepcopy(objective.initial_curvature_learning_state),
        "final_learning_state": objective.curvature_defect_memory.state_record()}
    result["complete_original_grid_oracle_progress"] = [x.report() for x in objective.complete_oracles]
    result["cross_center_norm_memory"] = objective.direction_bank.report()
    result["initial_complete_checkpoint_bank_input"] = copy.deepcopy(objective.checkpoint_bank_input)
    result["original_bank_replay"] = copy.deepcopy(objective.initial_bank_replay)
    result["finite_cone_new_task_account"] = objective.cone_ledger.report()
    result["new_actual_values"] = objective.full_value_evaluations-SOURCE_VALUES
    result["source_global_scientific_seconds"] = SOURCE_SCIENCE_SECONDS
    result["cumulative_original_scientific_seconds"] = (
        time.monotonic()-objective.global_scientific_started)
    result["new_exact_step_records_present"] = [
        "new_candidate_step_record" in event
        for record in models for event in record["linear_program"].get("cone_calls", [])]
    result["saved_exact_step_record_count"] = sum(result["new_exact_step_records_present"])
    result["every_finite_returned_solver_vector_captured_before_status_filter"] = all(
        bool(event.get("new_candidate_step_record")) == bool(event.get("finite_original161_vector"))
        for record in models for event in record["linear_program"].get("cone_calls", []))
    return result
