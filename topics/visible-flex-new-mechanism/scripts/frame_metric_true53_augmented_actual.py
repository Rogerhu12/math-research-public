#!/usr/bin/env python3
"""At most three new augmented-direction trials, with all original gates.

The paid true53 baseline is an immutable receipt.  Any request for its
ordinary geometry is rejected, even if a caller attempts a cache route.
No original configuration limit is rewritten into this method's allowance.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import time
import traceback
import numpy as np
from frame_height_null_coordinates import digest
from frame_metric_entry_tail_height159 import EntryTailHeight159Objective
from frame_metric_height159_soc_hold import compact_with_all_actual_gates
from frame_metric_budget_recovery import EvaluationBudgetReached, require_public_research_environment
from frame_metric_paid_cone_vector import actual_acceptance
from frame_metric_true53_augmented_scope import (
    POLICY, AugmentedDirectionLedger, AugmentedDirectionLimit, require,
    SOURCE_CFG_SHA, SOURCE_FIELD_SHA, SOURCE_PHYSICAL_SHA,
    SOURCE_ACCEPTED_INDEX, SOURCE_ORIGINAL_VALUES, SOURCE_GLOBAL_SECONDS)

POOL_POLICY = "original-value-only-learning; failed-trial-new-row-stops-this-fixed-direction"


class AugmentedDirectionObjective(EntryTailHeight159Objective):
    """Fresh ordinary-method identity; source physical data remain exact."""
    def __init__(self, *args, replay, ledger, coarse_pool, fine_pool, **kwargs):
        require(isinstance(ledger, AugmentedDirectionLedger), "the new shared augmented-direction ledger required")
        self.positive_ledger, self.positive_replay = ledger, replay
        self.actual_value_events = []
        self.value_purpose = "new-augmented-direction-actual-trial"
        self.paid_base_geometry_requests_rejected = 0
        self._actual_ready = False
        self.validation_trace = None
        super().__init__(*args, **kwargs)
        cp, point = replay["source_checkpoint"], replay["source_current_point"]
        require(digest(self.cfg) == SOURCE_CFG_SHA
                and digest(self.problem.evaluation_definition()) == SOURCE_FIELD_SHA,
                "original mathematical cfg and direct ordinary field changed")
        require(point["accepted_index"] == SOURCE_ACCEPTED_INDEX
                and point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "true accepted53 is the only initial physical point")
        require(self.cfg["minimum_accepted_eta_decrease_exact"] == "1/10000000"
                and self.cfg["max_physical_evaluations"] == 160
                and self.cfg["max_seconds"] == 1800
                and self.cfg["maximum_backtracks_per_model"] == 6,
                "original actual gates and inherited metadata changed")
        for label, raw in (("coarse", coarse_pool), ("fine", fine_pool)):
            a = np.asarray(raw)
            require(a.dtype.kind in "iu" and a.ndim == 1
                    and len(np.unique(a)) == len(a),
                    "true original integer/unique pool required: "+label)
        self.set_pool(coarse_pool, {"kind": "augmented-direction-exact-current53-pool-restoration"})
        self.set_fine_pool(fine_pool, {"kind": "augmented-direction-exact-current53-pool-restoration"})
        require(self.pool.tolist() == cp["coarse_pool"] and self.fine_pool.tolist() == cp["fine_pool"],
                "source actual row order changed")
        self.pool_version, self.fine_pool_version = cp["coarse_pool_version"], cp["fine_pool_version"]
        self.pool_history = copy.deepcopy(cp["coarse_pool_history"])
        self.fine_pool_history = copy.deepcopy(cp["fine_pool_history"])
        require((len(self.pool), len(self.fine_pool), self.pool_version, self.fine_pool_version)
                == (4448, 4549, 13, 14), "the true post-p32-actual53 pools are required")
        self.geometry_evaluations = self.fine_evaluations = 0
        self.value_geometry_seconds = self.fine_value_seconds = 0.
        self.geometry_cache = self.fine_cache = self.epigraph_cache = None
        self.derivative_cache = self.fine_derivative_cache = None
        self.accepted_cache = None
        self.accepted_iterates = [copy.deepcopy(point)]
        self.optimization_started = self.total_started = ledger.started
        self.source_objective_evaluation_sha256 = cp["objective_evaluation_sha256"]
        self.evaluation_definition.update(
            schema=POLICY+"-ordinary-values",
            independent_paid_augmented_direction_actual_method=True,
            original_ordinary_field_evaluation_sha256=SOURCE_FIELD_SHA,
            source_objective_evaluation_sha256=self.source_objective_evaluation_sha256,
            source_accepted_index=SOURCE_ACCEPTED_INDEX,
            source_physical_state_sha256=SOURCE_PHYSICAL_SHA,
            original_configuration_unchanged=True,
            original_cfg_160_1800_are_closed_ancestor_scope_not_new_limits=True,
            necessary_current_model_value_cap=0, new_actual_value_cap=6,
            total_new_ordinary_value_cap=6, scientific_seconds_this_method=600,
            all_true53_base_ordinary_geometry_requests_are_forbidden=True,
            ancestor_complete_scientific_seconds_closed=SOURCE_GLOBAL_SECONDS,
            all_source_bank_gamma_and_controller_records_carried_passively=True,
            no_old_hard_J_or_geometry_base_rebuild=True,
            original_paid_gate_receipts_not_independently_replayed=True)
        self.evaluation_sha256 = digest(self.evaluation_definition)
        require(self.evaluation_sha256 != self.source_objective_evaluation_sha256,
                "new augmented-direction identity may not impersonate the paid scalar-only source")
        self._actual_ready = True
        self._wall()

    def _wall(self):
        ledger = getattr(self, "positive_ledger", None)
        if ledger is not None:
            ledger.check()
        if getattr(self, "_actual_ready", False):
            require(self.full_value_evaluations <= 6, "new actual-only six-value cap exceeded")

    def _require_new_physical_state(self, state):
        require(getattr(self, "_actual_ready", False),
                "ordinary geometry is not permitted during input/objective construction")
        state = self.problem.coordinates.validate(state)
        physical = digest(self.problem.identity(state))
        if physical == SOURCE_PHYSICAL_SHA:
            self.paid_base_geometry_requests_rejected += 1
            raise ValueError("true53 base geometry is already paid and may not be re-evaluated")
        return physical

    def _call_event(self, label, state):
        self._wall()
        physical = self._require_new_physical_state(state)
        require(self.value_purpose == "new-augmented-direction-actual-trial",
                "only a genuinely new candidate may request ordinary geometry")
        event = self.positive_ledger.begin(
            "actual_grid_values", grid=label, physical_state_sha256=physical,
            purpose=self.value_purpose)
        event["purpose"] = self.value_purpose
        return event

    def _finish_value_event(self, event, label, before_calls, before_count, started):
        snapshot = self.problem.timing_snapshot()
        calls = snapshot["geometry_calls_started"]-before_calls
        require(calls in (0, 1), "one value request made more than one ordinary call")
        count = self.geometry_evaluations if label == "coarse" else self.fine_evaluations
        if calls == 1 and count == before_count:
            elapsed = time.monotonic()-started
            if label == "coarse":
                self.geometry_evaluations += 1
                self.value_geometry_seconds += elapsed
            else:
                self.fine_evaluations += 1
                self.fine_value_seconds += elapsed
            event["failed_started_geometry_count_added_once"] = True
        event.update(
            elapsed_seconds=time.monotonic()-started,
            geometry_calls_started=calls,
            new_coarse_counter=self.geometry_evaluations,
            new_fine_counter=self.fine_evaluations,
            direct_reference_timing_after_call=snapshot)
        self.positive_ledger.end(event, event.get('error'),
                                   geometry_calls_started=calls)
        self.actual_value_events.append(copy.deepcopy(event))

    def physical_geometry(self, state):
        state = np.asarray(state, float)
        self._require_new_physical_state(state)
        current, saved = self.geometry_cache, self.accepted_cache
        hit = current is not None and np.array_equal(state, current["state"])
        restore = (saved is not None and np.array_equal(state, saved["state"])
                   and isinstance(saved.get("coarse"), dict))
        if hit or restore:
            return super().physical_geometry(state)
        event = self._call_event("coarse", state)
        before_calls = self.problem.timing_snapshot()["geometry_calls_started"]
        before_count = self.geometry_evaluations
        started = time.monotonic()
        try:
            value = super().physical_geometry(state)
            event["status"] = "complete"
            return value
        except Exception as error:
            event.update(status="raised", error={"type": type(error).__name__, "message": str(error)})
            raise
        finally:
            self._finish_value_event(event, "coarse", before_calls, before_count, started)

    def fine_decision(self, state):
        state = np.asarray(state, float)
        self._require_new_physical_state(state)
        current, saved = self.fine_cache, self.accepted_cache
        hit = current is not None and np.array_equal(state, current["state"])
        restore = (saved is not None and np.array_equal(state, saved["state"])
                   and isinstance(saved.get("fine"), dict))
        if hit or restore:
            return super().fine_decision(state)
        event = self._call_event("fine", state)
        before_calls = self.problem.timing_snapshot()["geometry_calls_started"]
        before_count = self.fine_evaluations
        started = time.monotonic()
        try:
            value = super().fine_decision(state)
            event["status"] = "complete"
            return value
        except Exception as error:
            event.update(status="raised", error={"type": type(error).__name__, "message": str(error)})
            raise
        finally:
            self._finish_value_event(event, "fine", before_calls, before_count, started)

    def accepted_point(self, state, coarse, fine, reason):
        point = super().accepted_point(state, coarse, fine, reason)
        local = len(self.accepted_iterates)-1
        require(local == 1 and point is self.accepted_iterates[-1],
                "only one new acceptance and the same-object parent record required")
        point["accepted_index"] = SOURCE_ACCEPTED_INDEX+local
        point["augmented_direction_local_accepted_index"] = local
        return point

    def exact_support_invariants(self, state):
        q = self.problem.coordinates.validate(state)
        exact, ref = self.problem.coordinates.exact_heights(q), self.problem.coordinates.reference_exact
        change = sum(self.problem.null_basis.integrals[j]*(exact[j]-ref[j]) for j in range(9))
        fixed = all(exact[j] == ref[j] for j in (4, 5))
        require(change == 0 and fixed, "exact null integral or fixed physical height slots changed")
        return {"exact_total_height_integral_change": str(change),
                "physical_height_c4_c5_unchanged": fixed,
                "all_nine_exact_height_coefficients": [str(x) for x in exact],
                "same_compact_supported_tangent_and_height_family": True,
                "no_old_base_geometry_or_outside_J_replay": True}

    def execution_receipt(self):
        require(self.jacobian_geometry_batches == self.jacobian_refreshes
                == self.fine_Jacobian_batches == self.fine_Jacobian_refreshes == 0,
                "the new adapter unexpectedly invoked a legacy objective J path")
        require(self.positive_ledger.counts["necessary_base_geometry"] == 0,
                "no source53 ordinary geometry allowance exists in this method")
        return {"legacy_objective_selected159_J_batches": 0,
                "legacy_objective_selected159_J_refreshes": 0,
                "new_attainer_gradients_owned_by_shared_first_jet_ledger": True,
                "old_LP_SOC_cone_calls": 0,
                "independent_paid_initial_or_final_geometry_replays": 0,
                "necessary_current_model_geometry_calls": 0,
                "paid_base_geometry_requests_rejected": self.paid_base_geometry_requests_rejected,
                "ordinary_values_are_only_new_candidates": True}

    def value_account(self):
        started = sum(int(e.get("geometry_calls_started", 0)) for e in self.actual_value_events)
        counts = self.positive_ledger.counts
        require(counts["necessary_base_geometry"] == 0,
                "the closed source baseline may not debit new ordinary values")
        require(all(e.get("purpose") == "new-augmented-direction-actual-trial"
                    for e in self.actual_value_events),
                "all new ordinary value events must belong to new candidate trials")
        return {"source_original_values_closed": SOURCE_ORIGINAL_VALUES,
                "source_scientific_seconds_closed": SOURCE_GLOBAL_SECONDS,
                "necessary_current_model_value_debits": 0,
                "new_actual_value_debits": counts["actual_grid_values"],
                "new_ordinary_value_budget_debits": counts["actual_grid_values"],
                "necessary_model_geometry_calls_started": 0,
                "new_actual_geometry_calls_started": started,
                "new_adapter_geometry_calls_started": started,
                "new_coarse_counter": self.geometry_evaluations,
                "new_fine_counter": self.fine_evaluations,
                "new_counter_sum": self.full_value_evaluations,
                "total_source_plus_new_started_values": SOURCE_ORIGINAL_VALUES+started,
                "new_model_value_cap": 0, "new_actual_value_cap": 6, "new_total_value_cap": 6,
                "original_cfg160_and1800_are_closed_not_remaining_allowances": True,
                "old96_and160_caps_not_rewritten_or_reopened": True}


def learn_current_actual_values(objective, candidate, trial, fine_present):
    before = objective.full_value_evaluations
    added, detail = objective.expand_pool(
        objective.vector(candidate), "augmented-direction-coarse-original-value-only-learning")
    trial.update(
        coarse_omitted_rows=detail["omitted_violating_count"],
        coarse_omitted_hard_rows=detail["omitted_hard_violating_count"],
        new_coarse_rows=len(added["added_row_indices"]) if added else 0,
        added_coarse_rows=copy.deepcopy(added), coarse_learning_detail=copy.deepcopy(detail))
    fine_capacity = False
    if fine_present:
        added_fine, detail_fine = objective.learn_fine_violations(
            candidate, "augmented-direction-fine-original-value-only-learning")
        trial.update(
            fine_omitted_rows=detail_fine["omitted_violating_count"],
            fine_omitted_hard_rows=detail_fine["omitted_hard_violating_count"],
            new_fine_rows=len(added_fine["added_row_indices"]) if added_fine else 0,
            added_fine_rows=copy.deepcopy(added_fine),
            fine_learning_detail=copy.deepcopy(detail_fine))
        fine_capacity = bool(detail_fine.get("pool_capacity_would_be_exceeded"))
    require(objective.full_value_evaluations == before,
            "learning repeated geometry instead of using this trial's owned cache")
    stop = bool(trial["new_coarse_rows"] or trial.get("new_fine_rows", 0)
                or detail.get("pool_capacity_would_be_exceeded") or fine_capacity)
    trial.update(learning_used_only_current_actual_value_caches=True,
                 pool_versions_after_learning=[objective.pool_version, objective.fine_pool_version],
                 no_unavailable_J_curvature_gamma_bank_or_growth_feedback=True,
                 new_row_or_capacity_stop=stop)
    return stop



def run_augmented_direction_actual_trials(objective, initial, domain, handle, envelope, best_query,
                                *, query_emitter=None, trial_emitter=None):
    require_public_research_environment()
    require(isinstance(objective, AugmentedDirectionObjective),
            "new true53 augmented-direction objective required")
    result = {
        "schema": POLICY+"-actual-trials", "status": "started", "error": None,
        "budget_message": None, "trials": [], "source_accepted_index": SOURCE_ACCEPTED_INDEX,
        "new_first_jet_model_and_original_actual_gates_are_separate": True,
        "pool_policy": POOL_POLICY,
        "scale_policy": "best then midpoint toward legal lower bound twice",
        "independent_initial_or_final_geometry_replays": 0}
    objective.validation_trace = result
    objective.value_purpose = "new-augmented-direction-actual-trial"
    old = objective.accepted_iterates[0]
    old_eta = old["maximum_eta_on_both_grids"]
    drop = float(Q(objective.cfg["minimum_accepted_eta_decrease_exact"]))
    floor = float(objective.cfg["linear_model_improvement_floor"])
    tried = {old["physical_state_sha256"]}
    width = np.asarray(objective.physical_upper)-np.asarray(objective.physical_lower)
    try:
        if handle is None or best_query is None:
            result["status"] = "no-qualified-model-descent-no-physical-trial"
        else:
            require(handle["qualified"] is True, "unqualified positive direction")
            p = np.asarray(handle["direction"], float)
            require(p.shape == (159,) and np.all(np.isfinite(p)), "finite full159 direction required")
            interval = handle["interval"]["original_numeric_tolerance_interval"]
            require(interval["nonempty"], "a legal numeric alpha interval is required")
            lower, upper = float(interval["lower"]), float(interval["upper"])
            baseline = next(r for r in envelope.records
                            if r["status"] == "complete" and r["alpha"] == 0
                            and r["purpose"] == "physical-zero-baseline")
            base = float(baseline["phi"])
            alpha = float(best_query["alpha"])
            first_alpha = alpha
            result["legal_interval"] = copy.deepcopy(handle["interval"])
            result["true_zero_baseline_query"] = copy.deepcopy(baseline)
            for scale_number in range(1, 4):
                objective._wall()
                if scale_number > 1:
                    alpha = lower+(alpha-lower)/2.
                require(lower <= alpha <= upper, "declared trial alpha left original legal interval")
                found = next((r for r in envelope.records
                              if r["status"] == "complete" and r["alpha"] == alpha), None)
                query = found if found is not None else envelope.query(
                    alpha, purpose="untried-actual-fallback")
                if found is None and query_emitter is not None:
                    query_emitter(query)
                if not (alpha > 0 and base-query["phi"] > floor):
                    result["status"] = "remaining-legal-scale-has-no-observed-model-gain"
                    break
                scaled = alpha*p
                candidate = objective.subspace.apply(initial, scaled[objective.subspace.columns])
                delta = candidate-initial
                trial = {
                    "number": len(result["trials"])+1,
                    "kind": "new-augmented-direction-physical-trial",
                    "scale_number": scale_number, "alpha": alpha,
                    "alpha_exact_binary64": str(Q.from_float(alpha)),
                    "first_alpha_exact_binary64": str(Q.from_float(first_alpha)),
                    "legal_lower_exact_binary64": str(Q.from_float(lower)),
                    "model_query_number": query["query_number"],
                    "model_gain_at_ideal_alpha_p": base-query["phi"],
                    "actual_rounding_delta_not_substituted_for_ideal_cached_direction": True,
                    "exact_binary64_ideal_scaled_direction": [
                        str(Q.from_float(float(x))) for x in scaled],
                    "exact_binary64_actual_total_step": [
                        str(Q.from_float(float(x))) for x in delta],
                    "exact_binary64_independent_coordinates": [
                        str(Q.from_float(float(x))) for x in candidate],
                    "accepted_as_next_iterate": False,
                    "attempt_status": "candidate-formed-before-original-gates"}
                result["trials"].append(trial)
                try:
                    objective.problem.coordinates.validate(candidate)
                    physical = digest(objective.problem.identity(candidate))
                    trial.update(
                        physical_state_sha256=physical,
                        exact_original_physical_coefficients=[
                            str(x) for x in objective.problem.coordinates.physical_exact(candidate)],
                        actual_total_step_physical_norms=objective.subspace.step_norms(delta, width),
                        restricted_support_invariants=objective.exact_support_invariants(candidate))
                    box = objective.problem.coordinates.exact_box_decision(
                        candidate, objective.physical_lower, objective.physical_upper)
                    trial["original_exact163_box"] = box
                    if not box["exact_original_box_pass"]:
                        trial["attempt_status"] = "original-exact163-box-rejected-before-geometry"
                        continue
                    rounded = domain.validate_actual_candidate(candidate)
                    trial["rounded_original_hard_domain_validation"] = rounded
                    if not rounded["eligible"]:
                        trial["attempt_status"] = "rounded-original-hard-domain-rejected-before-geometry"
                        continue
                    if physical in tried:
                        trial["attempt_status"] = "duplicate-rounded-point-not-reevaluated"
                        continue
                    tried.add(physical)
                    trial["charged_actual_point"] = objective.positive_ledger.charge("actual_trial_pairs")
                    trial["attempt_status"] = "coarse-value-started"
                    coarse_result = objective.evaluate(objective.vector(candidate))
                    coarse = coarse_result["decision"]
                    trial.update(
                        attempt_status="coarse-value-complete",
                        coarse_physical_evaluation=coarse_result["physical_geometry_evaluation"],
                        coarse_decision=compact_with_all_actual_gates(coarse))
                    fine = None
                    if coarse.get("regularity_screen_pass", False):
                        trial["attempt_status"] = "fine-value-started"
                        fine = objective.fine_decision(candidate)
                        trial.update(
                            attempt_status="complete-original-two-grid-trial",
                            fine_value_evaluation=objective.fine_evaluations,
                            fine_decision=compact_with_all_actual_gates(fine),
                            fine_even_if_other_coarse_gate_failed=
                                not coarse["single_grid_admissible_recovery_point"])
                    else:
                        trial["attempt_status"] = "coarse-nonregular-original-gate-rejection"
                    acceptance = actual_acceptance(old_eta, coarse, fine, drop)
                    trial["actual_acceptance"] = acceptance
                    if acceptance["accepted"]:
                        objective._wall()
                        point = objective.accepted_point(candidate, coarse, fine, {
                            "kind": "true53-new-augmented-direction-actual-descent",
                            "alpha_exact_binary64": trial["alpha_exact_binary64"],
                            "model_query_number": query["query_number"], "old53_eta": old_eta,
                            "new_finite_direction_ancestor_is_closed": True})
                        trial.update(accepted_as_next_iterate=True,
                                     accepted_index=point["accepted_index"])
                    learned = learn_current_actual_values(
                        objective, candidate, trial, fine is not None)
                    if acceptance["accepted"]:
                        result["status"] = "new-augmented-direction-two-grid-strict-descent-accepted"
                        break
                    if learned:
                        result["status"] = "new-actual-row-stops-fixed-direction-source-best-retained"
                        break
                finally:
                    if trial_emitter is not None:
                        trial_emitter(trial)
            else:
                result["status"] = "three-declared-legal-scales-completed-source-best-retained"
    except (EvaluationBudgetReached, AugmentedDirectionLimit) as error:
        result.update(status="new-augmented-direction-method-time-or-value-budget-exit",
                      budget_message=str(error))
    except Exception as error:
        result.update(status="new-augmented-direction-method-actual-trial-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    result["selected_two_grid_physical_point"] = copy.deepcopy(objective.accepted_iterates[-1])
    result["new_acceptances"] = len(objective.accepted_iterates)-1
    result["value_account"] = objective.value_account()
    result["ledger_at_trial_finish"] = objective.positive_ledger.report()
    result["execution_receipt"] = objective.execution_receipt()
    source = objective.positive_replay["source_checkpoint"]
    result["terminal_trust"] = source["terminal_trust"]
    result["terminal_legacy_streak"] = source["terminal_success_streak"]
    result["terminal_covered_streak"] = source["terminal_covered_ordinary_growth_streak"]
    result["bank_gamma_and_controller_carried_passively_without_model_feedback"] = True
    return result


if __name__ == "__main__":
    raise SystemExit("This module has no standalone execution scope; use the public audit.")
