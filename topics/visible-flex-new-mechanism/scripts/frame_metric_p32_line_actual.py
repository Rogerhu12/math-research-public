#!/usr/bin/env python3
"""Original full physical gates for at most three new scalar-line trial points."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import time
import traceback
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_entry_tail_height159 import EntryTailHeight159Objective
from frame_metric_height159_soc_hold import compact_with_all_actual_gates
from frame_metric_budget_recovery import EvaluationBudgetReached, require_public_research_environment
from frame_metric_paid_cone_vector import actual_acceptance
from frame_metric_p32_line_envelope import (
    POLICY, LineMethodLedger, SOURCE_ORIGINAL_VALUES, require, finite_array)

SOURCE_CFG_SHA = "1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19"
SOURCE_FIELD_SHA = "8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1"
SOURCE_PHYSICAL_SHA = "0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21"
SOURCE_ACCEPTED_INDEX = 52
POOL_POLICY = "original-value-only-learning; failed-trial-new-row-stops-this-fixed-line"


class ScalarLineActualObjective(EntryTailHeight159Objective):
    """Fresh ordinary-method identity; source physical data remain exact."""
    def __init__(self, *args, replay, ledger, coarse_pool, fine_pool, **kwargs):
        require(isinstance(ledger, LineMethodLedger), "independent scalar-method ledger required")
        self.line_ledger, self.line_replay = ledger, replay
        self.actual_value_events = []
        self._actual_ready = False
        self.validation_trace = None
        super().__init__(*args, **kwargs)
        cp, point = replay["source_checkpoint"], replay["source_current_point"]
        require(digest(self.cfg) == SOURCE_CFG_SHA
                and digest(self.problem.evaluation_definition()) == SOURCE_FIELD_SHA,
                "original mathematical cfg and direct ordinary field changed")
        require(point["accepted_index"] == SOURCE_ACCEPTED_INDEX
                and point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "true accepted52 is the only initial physical point")
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
        self.set_pool(coarse_pool, {"kind": "scalar-line-exact-current52-pool-restoration"})
        self.set_fine_pool(fine_pool, {"kind": "scalar-line-exact-current52-pool-restoration"})
        require(self.pool.tolist() == cp["coarse_pool"] and self.fine_pool.tolist() == cp["fine_pool"],
                "source actual row order changed")
        self.pool_version, self.fine_pool_version = cp["coarse_pool_version"], cp["fine_pool_version"]
        self.pool_history = copy.deepcopy(cp["coarse_pool_history"])
        self.fine_pool_history = copy.deepcopy(cp["fine_pool_history"])
        require((len(self.pool), len(self.fine_pool), self.pool_version, self.fine_pool_version)
                == (4448, 4544, 13, 13), "the true post-cone32 pools are required")
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
            independent_scalar_line_method=True,
            original_ordinary_field_evaluation_sha256=SOURCE_FIELD_SHA,
            source_objective_evaluation_sha256=self.source_objective_evaluation_sha256,
            original_configuration_unchanged=True,
            original_cfg_160_1800_are_closed_ancestor_scope_not_new_limits=True,
            actual_value_cap_this_method=6, scientific_seconds_this_method=600,
            all_source_bank_gamma_and_controller_records_carried_passively=True,
            selected_J_primary_factory_and_old_solver_entrypoints_disabled=True,
            initial_paid_gate_receipts_referenced_without_replaying_geometry=True)
        self.evaluation_sha256 = digest(self.evaluation_definition)
        require(self.evaluation_sha256 != self.source_objective_evaluation_sha256,
                "new actual-only identity may not impersonate the source model")
        self._actual_ready = True
        self._wall()

    def _wall(self):
        ledger = getattr(self, "line_ledger", None)
        if ledger is not None:
            ledger.check()
        if getattr(self, "_actual_ready", False):
            require(self.full_value_evaluations <= 6, "new actual6 cap exceeded")

    def _call_event(self, label, state):
        self._wall()
        physical = digest(self.problem.identity(state))
        return self.line_ledger.charge_actual_value(label, physical)

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
        self.actual_value_events.append(event)

    def physical_geometry(self, state):
        state = np.asarray(state, float)
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
        point["scalar_line_local_accepted_index"] = local
        return point

    def _no_derivatives(self, *args, **kwargs):
        raise RuntimeError("scalar-line physical validation cannot call J/factories/old solvers")
    linear_rows = active_derivatives = fine_derivatives = constraint_jac = _no_derivatives
    primary_observable_model = guarded_primary = _no_derivatives

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

    def zero_derivative_receipt(self):
        require(self.jacobian_geometry_batches == self.jacobian_refreshes
                == self.fine_Jacobian_batches == self.fine_Jacobian_refreshes == 0,
                "ordinary-only entry unexpectedly requested selected derivatives")
        return {"selected159_J_batches": 0, "selected159_J_refreshes": 0,
                "primary_affine_factories": 0, "old_LP_SOC_cone_calls": 0,
                "ordinary_geometry_for_initial_or_independent_final_audit": 0}

    def value_account(self):
        started = sum(int(e.get("geometry_calls_started", 0)) for e in self.actual_value_events)
        return {"source_original_values_closed": SOURCE_ORIGINAL_VALUES,
                "new_value_budget_debits": self.line_ledger.actual_values,
                "new_adapter_geometry_calls_started": started,
                "new_coarse_counter": self.geometry_evaluations,
                "new_fine_counter": self.fine_evaluations,
                "new_counter_sum": self.full_value_evaluations,
                "total_source_plus_new_started_values": SOURCE_ORIGINAL_VALUES+started,
                "new_value_cap": 6,
                "old96_and160_caps_not_rewritten_or_reopened": True}


def learn_current_actual_values(objective, candidate, trial, fine_present):
    before = objective.full_value_evaluations
    added, detail = objective.expand_pool(
        objective.vector(candidate), "scalar-line-coarse-original-value-only-learning")
    trial.update(
        coarse_omitted_rows=detail["omitted_violating_count"],
        coarse_omitted_hard_rows=detail["omitted_hard_violating_count"],
        new_coarse_rows=len(added["added_row_indices"]) if added else 0,
        added_coarse_rows=copy.deepcopy(added), coarse_learning_detail=copy.deepcopy(detail))
    fine_capacity = False
    if fine_present:
        added_fine, detail_fine = objective.learn_fine_violations(
            candidate, "scalar-line-fine-original-value-only-learning")
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


def run_scalar_line_actual_trials(objective, initial, paid_direction, envelope, best_query,
                                  *, query_emitter=None, trial_emitter=None):
    require_public_research_environment()
    require(isinstance(objective, ScalarLineActualObjective),
            "new scalar-line actual-only objective required")
    result = {
        "schema": POLICY+"-actual-trials", "status": "started", "error": None,
        "budget_message": None, "trials": [], "source_accepted_index": SOURCE_ACCEPTED_INDEX,
        "source_backend_status_preserved": "AlmostSolved",
        "source32_complete_model_did_not_return_a_candidate": True,
        "new_scalar_model_and_actual_gates_are_separate": True,
        "pool_policy": POOL_POLICY, "initial_actual_geometry_replays": 0}
    objective.validation_trace = result
    old = objective.accepted_iterates[0]
    old_eta = old["maximum_eta_on_both_grids"]
    drop = float(Q(objective.cfg["minimum_accepted_eta_decrease_exact"]))
    base = envelope.records[0]["phi"]
    floor = float(objective.cfg["linear_model_improvement_floor"])
    tried = {old["physical_state_sha256"]}
    width = np.asarray(objective.physical_upper)-np.asarray(objective.physical_lower)
    try:
        p = finite_array(paid_direction, (159,), "paid32 direction")
        if best_query is None:
            result["status"] = "no-observed-model-descent-no-physical-trial"
        else:
            first_alpha = best_query["alpha"]
            for division in (1., 2., 4.):
                objective._wall()
                alpha = first_alpha/division
                found = next((r for r in envelope.records
                              if r["status"] == "complete" and r["alpha"] == alpha), None)
                query = found if found is not None else envelope.query(alpha)
                if found is None and query_emitter is not None:
                    query_emitter(query)
                if not (alpha > 0 and base-query["phi"] > floor):
                    result["status"] = "remaining-half-line-point-has-no-observed-model-gain"
                    break
                scaled = alpha*p
                candidate = objective.subspace.apply(initial, scaled[objective.subspace.columns])
                delta = candidate-initial
                trial = {
                    "number": len(result["trials"])+1, "kind": "new-scalar-line-physical-trial",
                    "alpha": alpha, "alpha_exact_binary64": str(Q.from_float(float(alpha))),
                    "relative_to_first_alpha": str(Q.from_float(1./division)),
                    "model_query_number": query["query_number"],
                    "model_gain_at_ideal_alpha_p": base-query["phi"],
                    "actual_rounding_delta_not_substituted_for_ideal_cached_direction": True,
                    "exact_binary64_scaled_paid_direction": [str(Q.from_float(float(x))) for x in scaled],
                    "exact_binary64_actual_total_step": [str(Q.from_float(float(x))) for x in delta],
                    "exact_binary64_independent_coordinates": [str(Q.from_float(float(x))) for x in candidate],
                    "accepted_as_next_iterate": False, "attempt_status": "candidate-formed-before-gates"}
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
                        trial["attempt_status"] = "original-exact-box-rejected-before-geometry"
                        continue
                    if physical in tried:
                        trial["attempt_status"] = "duplicate-rounded-point-not-reevaluated"
                        continue
                    tried.add(physical)
                    trial["charged_actual_point"] = objective.line_ledger.charge_trial()
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
                            "kind": "independent-paid32-scalar-line-actual-descent",
                            "alpha_exact_binary64": trial["alpha_exact_binary64"],
                            "model_query_number": query["query_number"],
                            "old52_eta": old_eta,
                            "old32_status_not_promoted_to_new_solver_eligibility": True})
                        trial.update(accepted_as_next_iterate=True,
                                     accepted_index=point["accepted_index"])
                    learned = learn_current_actual_values(objective, candidate, trial, fine is not None)
                    if acceptance["accepted"]:
                        result["status"] = "new-scalar-line-two-grid-strict-descent-accepted"
                        break
                    if learned:
                        result["status"] = "new-actual-row-stops-fixed-line-source-best-retained"
                        break
                finally:
                    if trial_emitter is not None:
                        trial_emitter(trial)
            else:
                result["status"] = "three-declared-line-scales-completed-source-best-retained"
    except EvaluationBudgetReached as error:
        result.update(status="new-line-method-time-or-value-budget-exit", budget_message=str(error))
    except Exception as error:
        result.update(status="new-line-method-actual-trial-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    result["selected_two_grid_physical_point"] = copy.deepcopy(objective.accepted_iterates[-1])
    result["new_acceptances"] = len(objective.accepted_iterates)-1
    result["value_account"] = objective.value_account()
    result["ledger_at_trial_finish"] = objective.line_ledger.report()
    result["zero_derivative_or_old_solver_execution"] = objective.zero_derivative_receipt()
    result["terminal_trust"] = objective.line_replay["source_checkpoint"]["terminal_trust"]
    result["terminal_legacy_streak"] = objective.line_replay["source_checkpoint"]["terminal_success_streak"]
    result["terminal_covered_streak"] = objective.line_replay["source_checkpoint"]["terminal_covered_ordinary_growth_streak"]
    result["bank_gamma_and_controller_carried_passively_without_unavailable_model_feedback"] = True
    return result
