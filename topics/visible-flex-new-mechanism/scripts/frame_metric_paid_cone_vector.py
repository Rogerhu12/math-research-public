#!/usr/bin/env python3
"""Actual-only trials of one paid MaxTime vector; no solver, J, or affine model."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import time
import traceback
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_entry_tail_height159 import EntryTailHeight159Objective
from frame_metric_height159_soc_hold import compact_with_all_actual_gates
from frame_metric_budget_recovery import EvaluationBudgetReached, require_public_research_environment

POLICY = "same159-paid-MaxTime-vector-actual-only-validation-v1"
SOURCE_NEW_SCIENCE = 657.9451113929999
SOURCE_GLOBAL_SCIENCE = 1014.074931654
SOURCE_COARSE_VALUES = SOURCE_FINE_VALUES = 58
SOURCE_VALUES = 116
SOURCE_CONE_VALUES = 54
SOURCE_ACCEPTED_INDEX = 52
SOURCE_STEP_SHA = "17605ea24e9cefa4a73410913b3287c7b0f4b5303550a38f2da0f99850a0c644"
SOURCE_PHYSICAL_SHA = "0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21"
SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
CLOSED_HIGHS = {"linear_program_invocation_count": 64,
               "primary_LP_invocation_count": 63, "correction_LP_invocation_count": 1}
FRACTIONS = ("1", "1/2", "1/4", "1/8", "1/16", "1/32")
POOL_POLICY = "original-actual-value-only-learning; failed-trial-with-new-rows-stops-fixed-direction"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def finite_number(value):
    return isinstance(value, (float, int, np.floating, np.integer)) and not isinstance(
        value, (bool, np.bool_)) and math.isfinite(float(value))


def definition():
    return {
        "policy": POLICY, "source_backend_status_preserved": "MaxTime",
        "source_cone_ordinal": 31, "source_model_number": 27,
        "source_accepted_index": SOURCE_ACCEPTED_INDEX,
        "only_saved159_vector_is_available": True,
        "missing_solver_rho_and_norm_auxiliaries_not_invented": True,
        "candidate_backend_or_affine_eligibility_not_claimed": True,
        "actual_fractions_exact": list(FRACTIONS), "maximum_new_actual_values": 12,
        "coarse_and_fine_are_original_complete_grids": True,
        "pool_policy": POOL_POLICY, "new_solver_LP_SOC_J_JVP_calls": 0,
        "source_new_science_seconds": SOURCE_NEW_SCIENCE,
        "source_global_science_seconds": SOURCE_GLOBAL_SCIENCE,
        "cone_task_science_cap_seconds": 1200, "original_global_science_cap_seconds": 1800,
        "source_cone_task_values": SOURCE_CONE_VALUES, "cone_task_value_cap": 96,
        "source_global_values": SOURCE_VALUES, "original_global_value_cap": 160,
        "source_cone_calls": 31, "source_cone_cap": 32,
        "remaining_cone_call_is_not_authorized_by_this_entry": True,
        "closed_HiGHS": copy.deepcopy(CLOSED_HIGHS),
        "unchanged_bank_curvature_learning_and_two_streaks": True,
        "no_prediction_ratio_or_covered_growth_from_missing_model": True,
        "initial_two_grid_source_receipts_used_without_geometry_replay": True,
        "no_new_independent_final_geometry_audit": True}


class ContinuationClock:
    """One start before paid-log/input fetch; both existing clocks continue."""
    def __init__(self, started, *, clock=time.monotonic):
        self.clock = clock
        now = clock()
        require(finite_number(started) and float(started) <= now,
                "finite pre-input monotonic start required")
        self.started = float(started)

    def report(self):
        elapsed = self.clock()-self.started
        require(math.isfinite(elapsed) and elapsed >= 0, "nonnegative continuation clock required")
        cone = SOURCE_NEW_SCIENCE+elapsed
        total = SOURCE_GLOBAL_SCIENCE+elapsed
        return {
            "current_validation_scientific_seconds": elapsed,
            "cumulative_cone_task_scientific_seconds": cone,
            "cumulative_original_scientific_seconds": total,
            "source_cone_science_added_once": SOURCE_NEW_SCIENCE,
            "source_global_science_added_once": SOURCE_GLOBAL_SCIENCE,
            "remaining_scientific_seconds_in_intersection": min(1200-cone, 1800-total),
            "cold_calls_are_nonpreemptive_and_actual_elapsed_is_not_clipped": True}

    def check(self):
        report = self.report()
        if report["remaining_scientific_seconds_in_intersection"] <= 0:
            raise EvaluationBudgetReached("continued cone1200/original1800 science clock exhausted")
        return report


def decode_paid_step(record, expected_sha=SOURCE_STEP_SHA):
    raw = record["exact_binary64_independent_step"]
    require(isinstance(raw, list) and len(raw) == 159
            and all(isinstance(x, str) for x in raw), "actual saved exact159 list required")
    rational = [Q(x) for x in raw]
    vector = np.array([float(x) for x in rational], dtype=float)
    require(np.all(np.isfinite(vector))
            and all(Q.from_float(float(x)) == q for x, q in zip(vector, rational)),
            "saved step must be exactly recoverable binary64")
    require(record["array_sha256"] == expected_sha == array_digest(vector),
            "paid actual159 array fingerprint differs")
    require(np.any(vector != 0), "zero paid direction has no new physical trial")
    return vector


def actual_acceptance(old_eta, coarse, fine, minimum_drop):
    """The original true two-grid acceptance predicate, with no model surrogate."""
    if fine is None:
        return {"accepted": False, "reason": "fine-grid-not-evaluated"}
    maximum = max(coarse["direct_max_eta"], fine["direct_max_eta"])
    qualified = bool(coarse["single_grid_new_target_qualified"]
                     and fine["single_grid_new_target_qualified"])
    eligible = bool(coarse["single_grid_admissible_recovery_point"]
                    and fine["single_grid_admissible_recovery_point"])
    strict = bool(math.isfinite(maximum) and maximum < old_eta)
    enough = bool(old_eta-maximum >= minimum_drop or qualified)
    return {"accepted": bool(eligible and strict and enough),
            "both_original_single_grid_admissible": eligible,
            "maximum_eta_on_both_grids": maximum,
            "actual_eta_decrease": old_eta-maximum,
            "strict_true_eta_decrease": strict,
            "minimum_decrease_or_both_new_targets": enough,
            "both_new_metric_targets_qualified": qualified,
            "minimum_drop_uses_original_configuration": minimum_drop}


class PaidConeVectorObjective(EntryTailHeight159Objective):
    """Original ordinary decisions and pool learning; all derivative paths closed."""
    def __init__(self, *args, replay, continuation_clock, coarse_pool, fine_pool, **kwargs):
        self.continuation_clock = continuation_clock
        self.validation_replay = replay
        self.failed_coarse_value_receipts = []
        self.value_call_events = []
        self.validation_trace = None
        self._value_counters_restored = False
        super().__init__(*args, **kwargs)
        cp, point = replay["source_checkpoint"], replay["source_current_point"]
        require(digest(self.cfg) == SOURCE_CFG_SHA
                and digest(self.problem.evaluation_definition()) == SOURCE_FIELD_SHA,
                "original configuration and direct field must remain unchanged")
        require(point["accepted_index"] == SOURCE_ACCEPTED_INDEX
                and point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "actual accepted52 required; no old constructor index reset")
        require(self.cfg["maximum_backtracks_per_model"] == 6
                and self.cfg["minimum_accepted_eta_decrease_exact"] == "1/10000000"
                and self.cfg["max_physical_evaluations"] == 160
                and self.cfg["max_seconds"] == 1800,
                "original backtracking/acceptance/global limits differ")
        require(cp["terminal_trust"] == .00025
                and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
                "actual controller must remain .00025/0/0")
        for label, raw in (("coarse", coarse_pool), ("fine", fine_pool)):
            a = np.asarray(raw)
            require(a.dtype.kind in "iu" and a.ndim == 1
                    and len(np.unique(a)) == len(a), "true original integer unique pool required: "+label)
        self.set_pool(coarse_pool, {"kind": "exact-source52-pool-restoration"})
        self.set_fine_pool(fine_pool, {"kind": "exact-source52-pool-restoration"})
        require(self.pool.tolist() == cp["coarse_pool"]
                and self.fine_pool.tolist() == cp["fine_pool"], "pool order changed")
        self.pool_version = cp["coarse_pool_version"]
        self.fine_pool_version = cp["fine_pool_version"]
        self.pool_history = copy.deepcopy(cp["coarse_pool_history"])
        self.fine_pool_history = copy.deepcopy(cp["fine_pool_history"])
        require((len(self.pool), len(self.fine_pool), self.pool_version, self.fine_pool_version)
                == (4448, 4543, 13, 12), "actual final source pools differ")
        self.geometry_evaluations = SOURCE_COARSE_VALUES
        self.fine_evaluations = SOURCE_FINE_VALUES
        old = replay["source_snapshot_scalar_counters"]
        self.value_geometry_seconds = old["value_geometry_seconds"]
        self.fine_value_seconds = old["doubled_angle_value_seconds"]
        self.accepted_iterates = [copy.deepcopy(point)]
        self.accepted_cache = None
        self.geometry_cache = self.fine_cache = self.epigraph_cache = None
        self._value_counters_restored = True
        self.derivative_cache = self.fine_derivative_cache = None
        self.optimization_started = continuation_clock.started-SOURCE_GLOBAL_SCIENCE
        self.total_started = self.optimization_started
        self.source_objective_evaluation_sha256 = cp["objective_evaluation_sha256"]
        self.evaluation_definition.update(
            schema=POLICY+"-ordinary-evaluation",
            paid_vector_actual_only_method=definition(),
            source_objective_evaluation_sha256=self.source_objective_evaluation_sha256,
            original_ordinary_decisions_and_pool_learning_reused=True,
            derivative_and_affine_factory_entrypoints_disabled=True,
            source_bank_learning_and_supplemental_records_carried_passively=True,
            no_claim_of_numerical_outside_jet_comparison_with_unrestored_base_arrays=True)
        self.evaluation_sha256 = digest(self.evaluation_definition)
        require(self.evaluation_sha256 != self.source_objective_evaluation_sha256,
                "new value-only administrative identity may not impersonate the old solver")
        self._wall()

    def _wall(self):
        clock = getattr(self, "continuation_clock", None)
        if clock is not None:
            clock.check()
        if getattr(self, "_value_counters_restored", False):
            total = self.full_value_evaluations
            used = total-SOURCE_VALUES
            require(used >= 0, "actual source value counters were reset")
            if used > 12 or SOURCE_CONE_VALUES+used > 96 or total > 160:
                raise EvaluationBudgetReached("actual validation/cone96/original160 value cap exceeded")

    def _value_available(self):
        self._wall()
        used = self.full_value_evaluations-SOURCE_VALUES
        if used >= 12 or SOURCE_CONE_VALUES+used >= 96 or self.full_value_evaluations >= 160:
            raise EvaluationBudgetReached("actual validation/cone96/original160 value allowance exhausted")

    def physical_geometry(self, state):
        state = np.asarray(state, float)
        current, saved = self.geometry_cache, self.accepted_cache
        hit = current is not None and np.array_equal(state, current["state"])
        restore = saved is not None and np.array_equal(state, saved["state"]) and isinstance(saved.get("coarse"), dict)
        if not hit and not restore:
            self._value_available()
        before_count = self.geometry_evaluations
        before_calls = self.problem.timing_snapshot()["geometry_calls_started"]
        started = time.monotonic()
        try:
            return super().physical_geometry(state)
        finally:
            calls = self.problem.timing_snapshot()["geometry_calls_started"]-before_calls
            if calls == 1 and self.geometry_evaluations == before_count:
                elapsed = time.monotonic()-started
                self.geometry_evaluations += 1
                self.value_geometry_seconds += elapsed
                self.failed_coarse_value_receipts.append({
                    "coarse_value_ordinal": self.geometry_evaluations,
                    "started_adapter_call_charged_even_on_error": True, "elapsed_seconds": elapsed})
            require(calls in (0, 1), "unexpected extra ordinary geometry in one coarse request")
            if calls:
                self.value_call_events.append({
                    "grid": "coarse", "elapsed_seconds": time.monotonic()-started,
                    "cumulative_coarse_values": self.geometry_evaluations,
                    "direct_reference_timing_after_call": self.problem.timing_snapshot()})

    def fine_decision(self, state):
        state = np.asarray(state, float)
        current, saved = self.fine_cache, self.accepted_cache
        hit = current is not None and np.array_equal(state, current["state"])
        restore = saved is not None and np.array_equal(state, saved["state"]) and isinstance(saved.get("fine"), dict)
        if not hit and not restore:
            self._value_available()
        before = self.fine_evaluations
        started = time.monotonic()
        try:
            return super().fine_decision(state)
        finally:
            if self.fine_evaluations != before:
                require(self.fine_evaluations == before+1, "one fine request charged more than once")
                self.value_call_events.append({
                    "grid": "fine", "elapsed_seconds": time.monotonic()-started,
                    "cumulative_fine_values": self.fine_evaluations,
                    "direct_reference_timing_after_call": self.problem.timing_snapshot()})

    def accepted_point(self, state, coarse, fine, reason):
        point = super().accepted_point(state, coarse, fine, reason)
        local = len(self.accepted_iterates)-1
        require(local == 1 and point is self.accepted_iterates[-1],
                "at most one new acceptance; original same-object storage contract required")
        point["accepted_index"] = SOURCE_ACCEPTED_INDEX+local
        point["paid_vector_validation_local_accepted_index"] = local
        return point

    def _no_derivatives(self, *args, **kwargs):
        raise RuntimeError("this paid-vector entry authorizes ordinary values only; no J/model/solver")
    linear_rows = active_derivatives = fine_derivatives = constraint_jac = _no_derivatives
    primary_observable_model = guarded_primary = _no_derivatives

    def exact_support_invariants(self, state):
        q = self.problem.coordinates.validate(state)
        exact = self.problem.coordinates.exact_heights(q)
        ref = self.problem.coordinates.reference_exact
        integral = sum(self.problem.null_basis.integrals[j]*(exact[j]-ref[j]) for j in range(9))
        fixed = all(exact[j] == ref[j] for j in [4, 5])
        require(integral == 0 and fixed, "exact null-integral or fixed physical height slots failed")
        return {"exact_total_height_integral_change": str(integral),
                "physical_height_c4_c5_unchanged": fixed,
                "all_nine_exact_height_coefficients": [str(x) for x in exact],
                "same_compact_supported_tangent_and_null_height_family": True,
                "base_ordinary_arrays_not_recomputed_or_fabricated": True,
                "outside_jet_numerical_difference_not_evaluated": True}

    def value_account(self):
        added = self.full_value_evaluations-SOURCE_VALUES
        return {"source_coarse": SOURCE_COARSE_VALUES, "source_fine": SOURCE_FINE_VALUES,
                "source_global_values": SOURCE_VALUES,
                "current_validation_values": added,
                "coarse_cumulative": self.geometry_evaluations,
                "fine_cumulative": self.fine_evaluations,
                "cumulative_original_values": self.full_value_evaluations,
                "cumulative_cone_task_values": SOURCE_CONE_VALUES+added,
                "validation_cap": 12, "cone_task_cap": 96, "original_global_cap": 160,
                "new_initial_or_independent_final_values": 0}

    def zero_derivative_receipt(self):
        require(self.jacobian_geometry_batches == self.jacobian_refreshes
                == self.fine_Jacobian_batches == self.fine_Jacobian_refreshes == 0,
                "ordinary-only entry unexpectedly requested a derivative")
        return {"selected_J_batches": 0, "selected_J_refreshes": 0,
                "affine_factories": 0, "full_directional_JVP": 0,
                "new_LP_SOC_or_cone_calls": 0, "new_solver_return_vectors": 0}


def learn_cached_actual_rows(objective, candidate, record, fine_present):
    """Use the inherited functions, with the already-owned ordinary caches."""
    before = objective.full_value_evaluations
    added, detail = objective.expand_pool(
        objective.vector(candidate), "paid-MaxTime-vector-coarse-actual-hard-and-soft-envelope")
    record.update(coarse_omitted_rows=detail["omitted_violating_count"],
                  coarse_omitted_hard_rows=detail["omitted_hard_violating_count"],
                  new_coarse_rows=len(added["added_row_indices"]) if added else 0,
                  coarse_learning_detail=copy.deepcopy(detail),
                  added_coarse_rows=copy.deepcopy(added))
    fine_capacity = False
    if fine_present:
        addf, detailf = objective.learn_fine_violations(
            candidate, "paid-MaxTime-vector-fine-actual-hard-and-soft-envelope")
        record.update(fine_omitted_rows=detailf["omitted_violating_count"],
                      fine_omitted_hard_rows=detailf["omitted_hard_violating_count"],
                      new_fine_rows=len(addf["added_row_indices"]) if addf else 0,
                      fine_learning_detail=copy.deepcopy(detailf),
                      added_fine_rows=copy.deepcopy(addf))
        fine_capacity = bool(detailf.get("pool_capacity_would_be_exceeded"))
    require(objective.full_value_evaluations == before,
            "value-only learning unexpectedly repeated an ordinary physical call")
    record["learning_used_only_current_owned_value_caches"] = True
    record["pool_versions_after_learning"] = [objective.pool_version, objective.fine_pool_version]
    record["curvature_gamma_bank_streak_or_model_feedback_updates"] = 0
    record["new_row_or_capacity_stop"] = bool(
        record["new_coarse_rows"] or record.get("new_fine_rows", 0)
        or detail.get("pool_capacity_would_be_exceeded") or fine_capacity)
    return record["new_row_or_capacity_stop"]


def _validate_direction(objective, initial, paid_step, result):
    """Small explicit actual-trial branch, also used by new array-only fixtures."""
    old = objective.accepted_iterates[0]
    old_eta = old["maximum_eta_on_both_grids"]
    drop = float(Q(objective.cfg["minimum_accepted_eta_decrease_exact"]))
    tried = {old["physical_state_sha256"]}
    width = np.asarray(objective.physical_upper)-np.asarray(objective.physical_lower)
    for alpha in FRACTIONS:
        objective._wall()
        scaled = float(Q(alpha))*paid_step
        candidate = objective.subspace.apply(initial, scaled[objective.subspace.columns])
        actual_delta = candidate-initial
        record = {
            "number": len(result["trials"])+1, "alpha_exact": alpha,
            "kind": "independent-actual-validation-of-paid-MaxTime-vector",
            "source_backend_status": "MaxTime", "accepted_as_next_iterate": False,
            "attempt_status": "candidate-formed-before-gates",
            "exact_binary64_scaled_paid_direction": [str(Q.from_float(float(x))) for x in scaled],
            "exact_binary64_actual_total_step": [str(Q.from_float(float(x))) for x in actual_delta],
            "exact_binary64_independent_coordinates": [str(Q.from_float(float(x))) for x in candidate],
            "model_prediction_and_solver_auxiliaries_not_available": True}
        result["trials"].append(record)
        objective.problem.coordinates.validate(candidate)
        record["physical_state_sha256"] = digest(objective.problem.identity(candidate))
        record["exact_original_physical_coefficients"] = [
            str(x) for x in objective.problem.coordinates.physical_exact(candidate)]
        record["actual_total_step_physical_norms"] = objective.subspace.step_norms(actual_delta, width)
        record["restricted_support_invariants"] = objective.exact_support_invariants(candidate)
        box = objective.problem.coordinates.exact_box_decision(
            candidate, objective.physical_lower, objective.physical_upper)
        record["original_exact163_box"] = box
        if not box["exact_original_box_pass"]:
            record["attempt_status"] = "original-exact-box-rejected-before-geometry"
            continue
        if record["physical_state_sha256"] in tried:
            record["attempt_status"] = "duplicate-or-unchanged-rounded-physical-point-not-reevaluated"
            continue
        tried.add(record["physical_state_sha256"])
        record["attempt_status"] = "coarse-value-call-started"
        rv = objective.evaluate(objective.vector(candidate))
        coarse = rv["decision"]
        record.update(attempt_status="coarse-value-call-complete",
                      coarse_physical_evaluation=rv["physical_geometry_evaluation"],
                      coarse_decision=compact_with_all_actual_gates(coarse))
        fine = None
        # A regular coarse point gets the complete fine decision even if another
        # coarse gate fails. No projection or surrogate can replace either grid.
        if coarse.get("regularity_screen_pass", False):
            record["attempt_status"] = "fine-value-call-started"
            fine = objective.fine_decision(candidate)
            record.update(attempt_status="complete-original-two-grid-value-trial",
                          fine_value_evaluation=objective.fine_evaluations,
                          fine_decision=compact_with_all_actual_gates(fine),
                          actual_fine_evaluated_even_if_coarse_ineligible=
                              not coarse["single_grid_admissible_recovery_point"])
        else:
            record["attempt_status"] = "coarse-nonregular-original-gate-rejection"
        acceptance = actual_acceptance(old_eta, coarse, fine, drop)
        record["actual_acceptance"] = acceptance
        if acceptance["accepted"]:
            objective._wall()
            point = objective.accepted_point(candidate, coarse, fine, {
                "kind": "independent-actual-validation-of-paid-MaxTime-vector",
                "source_cone_ordinal": 31, "alpha_exact": alpha,
                "previous_two_grid_maximum_eta": old_eta,
                "no_solver_status_promotion_or_affine_qualification": True})
            record.update(accepted_as_next_iterate=True, accepted_index=point["accepted_index"])
        learned = learn_cached_actual_rows(objective, candidate, record, fine is not None)
        if acceptance["accepted"]:
            result["status"] = "paid-vector-new-two-grid-strict-descent-accepted"
            return
        if learned:
            result["status"] = "paid-vector-new-rows-stop-fixed-direction-last-accepted-retained"
            return
    result["status"] = "paid-vector-six-fractions-completed-last-accepted-retained"


def run_actual_validation(objective, initial, paid_step):
    require(isinstance(objective, PaidConeVectorObjective), "explicit actual-only objective required")
    require_public_research_environment()
    result = {
        "policy": POLICY, "status": "paid-vector-validation-started", "error": None,
        "budget_message": None, "trials": [], "source_accepted_index": SOURCE_ACCEPTED_INDEX,
        "source_backend_status_preserved": "MaxTime",
        "source_saved159_step_sha256": array_digest(paid_step),
        "no_new_solver_or_original_candidate_repair_call": True,
        "source_rho_norm_auxiliaries_remain_unavailable": True,
        "initial_point_ordinary_geometry_replays": 0,
        "pool_policy": POOL_POLICY}
    objective.validation_trace = result
    try:
        _validate_direction(objective, initial, paid_step, result)
    except EvaluationBudgetReached as error:
        result.update(status="paid-vector-existing-time-value-or-pool-budget-exit",
                      budget_message=str(error))
    except Exception as error:
        result.update(status="paid-vector-actual-validation-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    result["selected_two_grid_physical_point"] = copy.deepcopy(objective.accepted_iterates[-1])
    result["new_acceptances"] = len(objective.accepted_iterates)-1
    result["value_account"] = objective.value_account()
    result["clock_at_stage_finish"] = objective.continuation_clock.report()
    result["zero_derivative_or_solver_execution"] = objective.zero_derivative_receipt()
    result["last_restricted_trust"] = .00025
    result["final_consecutive_growth_qualifying_models"] = 0
    result["final_covered_ordinary_growth_streak"] = 0
    result["controller_preserved_without_unavailable_model_quality_feedback"] = True
    return result
