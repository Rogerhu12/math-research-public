#!/usr/bin/env python3
"""Original nineteen-state BVP with one frozen positive row metric per iterate.

The full QR/SVD direction, active-row predictions, scalar ray and actual trial
Armijo test now use exactly the same W.  W is recomputed only after acceptance.
All original unscaled convergence and true-curve physical gates are unchanged.
Scientific execution is confined to the declared public Actions.
"""
from __future__ import annotations

from collections import defaultdict
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

import r625_original_ray_minimizing_continuation_agent as ray_source

dense, height = ray_source.dense, ray_source.height
previous, old, mixed = ray_source.previous, ray_source.old, ray_source.mixed
LD, reduced, original, paid = ray_source.LD, ray_source.reduced, ray_source.original, ray_source.paid
ClockCheckpoint, emit = ray_source.ClockCheckpoint, ray_source.emit
RestoredMixedGaugeChart = ray_source.RestoredMixedGaugeChart
factor_receipts = ray_source.factor_receipts
affine_factor_receipts = ray_source.affine_factor_receipts


def load_paid_source(request, clock, progress):
    """Consume the actual ray terminal and its already completed true readouts."""
    reduced.require_public_science()
    started = time.monotonic()
    wanted = request["paid_source"]
    progress.update(stage="receive_actual_ray_terminal", completed=False)
    try:
        clock.check("before_paid_ray_terminal_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw) != wanted["log_bytes"] or progress["sha256"] != wanted["log_sha256"]:
            raise ValueError("The actual completed ray log identity differs.")
        final_tag = "R625_ORIGINAL_RAY_CONTINUATION_FINAL"
        events, final_count = {}, 0
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE", final_tag):
                marker = " " + tag + " "
                if marker in line:
                    literal = line.split(marker, 1)[1]
                    events[tag] = json.loads(literal)
                    if tag == final_tag:
                        final_count += 1
                        progress["original_FINAL_json_bytes"] = len(literal.encode())
                        progress["original_FINAL_json_sha256"] = hashlib.sha256(literal.encode()).hexdigest()
        if final_count != 1:
            raise ValueError("The actual ray log must have its unique complete final.")
        source, final, entry = events["INVERSE_ACTIONS_SOURCE"], events[final_tag], events["R620_FULL_FEEDBACK_STATE"]
        if (source["source_commit"] != wanted["source_commit"]
                or str(source["run_id"]) != str(wanted["run_id"])
                or source["request_sha256"] != wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"] != wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"] != wanted["FINAL_json_sha256"]):
            raise ValueError("The completed ray source or literal final differs.")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key: final["actual_last_full_state"][key] for key in keys}
        identity = old.identity(payload)
        plain = {key: payload[key] for key in keys[:3]}
        if (identity != wanted["state_identity"] or identity != final["actual_last_full_state_identity"]
                or old.identity(plain) != wanted["plain_checkpoint_identity"]
                or old.identity(plain) != entry["state_identity"] or plain != entry["state"]
                or payload["coordinate_order"] != mixed.COORDINATE_ORDER
                or payload["fixed_gauge_unit"] != mixed.GAUGE_UNIT_TEXT):
            raise ValueError("The actual complete ray state or original coordinate frame differs.")
        if (final["status"] != "original_mixed_gauge_current_state_stalled"
                or final["retained_counters"]["accepted"] != 2
                or final["fixed_actual_curve_refinement_status"]["state"] != "completed"
                or any(value != 0.0 for value in final["actual_last_original_terminal_rows"])):
            raise ValueError("This scope starts at the actual completed ray state with exact stored end zeros.")
        progress.update(stage="actual_ray_state_and_paid_reports_loaded", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"], original_state_identity=identity,
            old_science_seconds=final["new_science_seconds"], old_counters=final["retained_counters"],
            actual_previous_trust=entry["trust"], actual_previous_damping=entry["damping"],
            old_fine_is_already_completed=True, old_LD_anchor_is_already_saved=True,
            no_old_scientific_qualification_replayed=True)
        clock.check("after_paid_ray_terminal_receive")
        return {"payload": payload, "final": final, "entry": entry, "source": source}
    finally:
        progress["seconds"] = time.monotonic() - started


class ConsistentWeightedFullFeedback(ray_source.OriginalRayMinimizingFullFeedback):
    """Keep physical equations unchanged and match the objective to the full solve."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.merit_epoch = 0
        self.merit_cache = None
        self.weighted_merit_counts = defaultdict(int)
        self.merit_epoch_receipts = []

    def prepare_linear_cache(self, current, matrix):
        cache = super().prepare_linear_cache(current, matrix)
        # The eliminated ten terminal coordinates have exact zero increments
        # for the present seed and every accepted same-mesh continuation.
        # At a possible later mesh their nonzero affine increments remain
        # fully retained; the solver then checks the actual slope explicitly.
        weights = np.concatenate((cache["row_scale"], np.ones(10)))
        if (weights.shape != current["residual"].shape
                or not np.all(np.isfinite(weights)) or not np.all(weights > 0.)):
            raise FloatingPointError("A finite strictly positive weight is required for every original row.")
        weights.flags.writeable = False
        self.merit_epoch += 1
        cache.update(merit_weights=weights, merit_current=current, merit_epoch=self.merit_epoch)
        self.merit_cache = cache
        value = self.weighted_merit(current, cache)
        receipt = {"epoch": self.merit_epoch,
            "weights_float64_sha256": hashlib.sha256(weights.tobytes()).hexdigest(),
            "all_original_rows": len(weights), "weight_min": float(weights.min()),
            "weight_max": float(weights.max()), "current_weighted_norm": value["norm"],
            "current_weighted_phi": value["phi"], "current_raw_norm": float(current["norm"]),
            "all_stored_terminal_rows_exactly_zero": bool(np.all(current["terminal"] == 0.)),
            "W_from_complete_current_free_Jacobian_and_terminal_unit_weights": True,
            "frozen_for_all_active_sets_lambdas_rays_and_actual_trials": True,
            "cross_epoch_merit_comparison_authorized": False,
            "raw_absolute_completion_gates_changed": False}
        cache["merit_receipt"] = receipt
        self.merit_epoch_receipts.append(receipt)
        emit("R625_CONSISTENT_WEIGHT_EPOCH", receipt)
        return cache

    def weighted_merit(self, state, cache):
        """Evaluate only the already computed complete residual in frozen W."""
        started = time.monotonic()
        self.weighted_merit_counts["attempts"] += 1
        try:
            self.clock.check("before_complete_frozen_weight_merit")
            scaled = cache["merit_weights"] * np.asarray(state["residual"], float)
            norm = float(np.linalg.norm(scaled))
            phi = .5 * float(np.dot(scaled, scaled))
            if not np.all(np.isfinite(scaled)) or not np.isfinite(norm) or not np.isfinite(phi):
                raise FloatingPointError("The full frozen-weight merit is nonfinite.")
            self.weighted_merit_counts["completed"] += 1
            self.weighted_merit_counts["complete_residual_entries"] += len(scaled)
            self.clock.check("after_complete_frozen_weight_merit")
            return {"norm": norm, "phi": phi, "epoch": cache["merit_epoch"]}
        finally:
            self.weighted_merit_counts["seconds"] += time.monotonic() - started

    def _complete_original_ray(self, current, matrix, direction):
        """One original Jd, then the identical fixed W used by every factor."""
        cache = self.merit_cache
        if cache is None or current is not cache["merit_current"] or matrix is not cache["matrix"]:
            raise RuntimeError("A ray must use the live current-state metric and its same complete Jacobian.")
        self.clock.check("before_consistent_full_Jd_ray")
        started = time.monotonic()
        self.original_ray_counts["ray_attempts"] += 1
        progress = {"phase": "complete_Jd_then_same_frozen_W", "completed": False,
            "merit_epoch": cache["merit_epoch"], "complete_matrix_shape": list(matrix.shape),
            "known_end_increments_and_all_original_rows_retained": True}
        self.latest_original_ray_attempt = progress
        try:
            raw_residual = np.asarray(current["residual"], float)
            size = float(np.max(np.abs(direction)))
            self.original_ray_counts["Jd_products_attempted"] += 1
            with np.errstate(over="ignore", invalid="ignore", divide="ignore", under="ignore"):
                raw_derivative = matrix @ direction
                self.original_ray_counts["Jd_products_completed"] += 1
                weights = cache["merit_weights"]
                residual, derivative = weights * raw_residual, weights * raw_derivative
                finite = bool(np.all(np.isfinite(direction)) and np.isfinite(size)
                    and np.all(np.isfinite(raw_residual)) and np.all(np.isfinite(raw_derivative))
                    and np.all(np.isfinite(residual)) and np.all(np.isfinite(derivative)))
                slope = float(np.dot(residual, derivative)) if finite else None
                quadratic = float(np.dot(derivative, derivative)) if finite else None
                norm = float(np.linalg.norm(residual)) if finite else None
                phi = .5 * float(np.dot(residual, residual)) if finite else None
                raw_slope = float(np.dot(raw_residual, raw_derivative)) if finite else None
            slope, quadratic, norm, phi, raw_slope = [self._finite_observation(v)
                for v in (slope, quadratic, norm, phi, raw_slope)]
            ray = {"residual": residual, "derivative": derivative, "size": size,
                "norm": norm, "phi": phi, "slope": slope, "quadratic": quadratic,
                "finite": finite, "merit_epoch": cache["merit_epoch"],
                "raw_slope_observation": raw_slope, "raw_norm_observation": float(current["norm"])}
            progress.update(phase="complete_frozen_weight_ray", completed=True,
                weighted_slope=slope, weighted_Jd_squared_norm=quadratic, weighted_phi=phi,
                raw_slope_observation=raw_slope, raw_norm_observation=float(current["norm"]),
                unscaled_direction_infinity_norm=self._finite_observation(size))
            self.original_ray_counts["rays_completed"] += 1
            if slope is not None and slope >= 0.:
                self.original_ray_counts["nonnegative_weighted_slopes"] += 1
            self.clock.check("after_consistent_full_Jd_ray")
            return ray
        finally:
            progress["seconds"] = time.monotonic() - started
            self.original_ray_counts["full_ray_seconds"] += progress["seconds"]

    def _ray_prediction(self, ray, maximum_fraction, minimum_fraction):
        started = time.monotonic()
        self.original_ray_counts["fraction_prediction_attempts"] += 1
        try:
            cap = float(min(1., max(0., maximum_fraction)))
            slope, quadratic = ray["slope"], ray["quadratic"]
            has_minimizer = bool(ray["finite"] and slope is not None and slope < 0.
                and quadratic is not None and quadratic > 0. and ray["phi"] is not None)
            minimizer_capped = (1. if -slope >= quadratic else float(-slope / quadratic)) if has_minimizer else None
            fraction = min(cap, minimizer_capped) if has_minimizer else cap
            predicted_norm = predicted_phi = threshold = None
            with np.errstate(over="ignore", invalid="ignore", divide="ignore", under="ignore"):
                predicted = ray["residual"] + fraction * ray["derivative"]
                if np.all(np.isfinite(predicted)):
                    predicted_norm = self._finite_observation(np.linalg.norm(predicted))
                    predicted_phi = self._finite_observation(.5 * np.dot(predicted, predicted))
                if has_minimizer:
                    threshold = self._finite_observation(ray["phi"] + 1.e-4 * fraction * slope)
            reasons = []
            if not has_minimizer:
                reasons.append("no_finite_negative_slope_for_same_frozen_weight_merit")
            if fraction < minimum_fraction:
                reasons.append("feasible_fraction_below_declared_usable_floor")
            if predicted_phi is None or ray["phi"] is None or not predicted_phi < ray["phi"]:
                reasons.append("no_finite_same_weight_linear_predicted_descent")
            report = {"usable": not reasons, "reasons": reasons,
                "unscaled_coordinate_direction_infinity_norm": self._finite_observation(ray["size"]),
                "trust_fraction": fraction, "maximum_fraction_before_ray_minimization": cap,
                "weighted_merit_epoch": ray["merit_epoch"], "weighted_merit_phi_before": ray["phi"],
                "weighted_merit_norm_before": ray["norm"], "weighted_merit_directional_inner_product": slope,
                "weighted_Jd_squared_norm": quadratic, "weighted_predicted_phi": predicted_phi,
                "weighted_predicted_norm": predicted_norm,
                "weighted_quadratic_minimizer_capped_at_one": minimizer_capped,
                "weighted_slope_Armijo_threshold": threshold,
                "weighted_linear_Armijo_observation": bool(predicted_phi is not None and threshold is not None
                    and predicted_phi < threshold),
                "raw_original_slope_observation_not_acceptance": ray["raw_slope_observation"],
                "raw_original_norm_observation_not_acceptance": ray["raw_norm_observation"],
                "W_fixed_at_complete_current_J_for_all_active_sets_and_trials": True,
                "same_scalar_fraction_multiplies_complete_original_direction": True,
                "all_ten_linear_end_rows_paid": True, "no_fraction_increase_after_prior_caps": fraction <= cap,
                "linear_prediction_does_not_certify_actual_acceptance_or_root": True}
            self.original_ray_counts["fraction_predictions_completed"] += 1
            self.latest_original_ray_attempt["last_fraction_prediction"] = report
            return report
        finally:
            self.original_ray_counts["fraction_prediction_seconds"] += time.monotonic() - started

    def choose_direction(self, current, cache, trust, damping, args):
        direction, report = super().choose_direction(current, cache, trust, damping, args)
        report["frozen_weight_merit"] = cache["merit_receipt"]
        report["direction_ray_active_set_and_trial_use_identical_W"] = True
        return direction, report


def solve(system, states, parameters, histories, grid, args, retained, level=0, paid_entry=None):
    started = time.monotonic()
    counters = {"accepted":0, "rejected":0, "complete_trials":0, "trial_attempts":0,
                "domain_or_chart_rejections":0, "actual_curve_rejections":0,
                "direction_requests":0, "linear_direction_unavailable":0}
    current = system.evaluate(system.pack(states, parameters))
    curve = old.ActualC2StateCurve(system.x, current["states"], current["parameters"])
    if paid_entry is None:
        actual = histories.evaluate(curve, current["chart"], grid, current["states"])
        fixed = {"state":"pending", "attempted":False, "reason":"new_complete_original_BVP_state"}
    else:
        actual = {"model":curve, "chart":current["chart"],
                  "report":paid_entry["final"]["actual_last_true_curve_report"],
                  "states_at_observations":None, "paid_report_only":True}
        fixed = dict(paid_entry["final"]["fixed_actual_curve_refinement_status"])
        fixed.update({"inherited_paid_completed_readout":True,
                      "new_science_attempted_for_this_unchanged_curve":False,
                      "source_run_id":int(paid_entry["source"]["run_id"])})
    retained.update(system=system, current=current, actual=actual, counters=counters,
                    fixed_refinement=fixed)
    trust, damping = args.trust, args.damping
    old.checkpoint(system, current, actual, 0, "paid_state_equivalent_mixed_gauge_entry",
                   counters, trust, damping)
    status = "original_mixed_gauge_iteration_budget_reached"
    cache, iteration = None, 0
    for iteration in range(1, args.iterations+1):
        system.clock.check("before_paid_original_BVP_iteration")
        if old.collocation_converged(current, args):
            status = ("original_feedback_and_true_integral_discrete_gates_met"
                      if old.actual_converged(current, actual, args) else
                      "original_collocation_converged_actual_curve_gates_pending")
            break
        retained["inflight_linear"] = {"level":level, "iteration":iteration,
            "trust":trust, "damping":damping, "phase":"necessary_complete_current_Jacobian_frozen_W_and_factor_cache"}
        if cache is None:
            matrix = system.jacobian(current)
            cache = system.prepare_linear_cache(current, matrix)
        else:
            system.jacobian_cache_reuses += 1
        frozen_current_merit = system.weighted_merit(current, cache)
        counters["direction_requests"] += 1
        retained["inflight_linear"] = {"level":level, "iteration":iteration,
            "trust":trust, "damping":damping, "phase":"select_complete_same_weight_direction_and_feasible_ray"}
        direction, linear = system.choose_direction(current, cache, trust, damping, args)
        retained["latest_complete_linear_report"] = linear
        emit("R625_COMPLETE_ORIGINAL_LINEAR_DIRECTION", {"level":level,
             "iteration":iteration, "report":linear})
        retained.pop("inflight_linear", None)
        accepted = False
        if direction is None:
            counters["linear_direction_unavailable"] += 1
        else:
            initial_fraction = float(linear["selected_prediction"]["trust_fraction"])
            slope = linear["selected_prediction"]["weighted_merit_directional_inner_product"]
            if slope is None or not np.isfinite(slope) or slope >= 0.:
                raise FloatingPointError("A selected direction must descend in the identical frozen W.")
            for backtrack in range(args.trials):
                system.clock.check("before_paid_original_BVP_backtrack")
                fraction = float(initial_fraction*2.**-backtrack)
                counters["trial_attempts"] += 1
                retained["inflight_trial"] = {"level":level, "iteration":iteration,
                    "backtrack":backtrack, "fraction":fraction,
                    "phase":"original_full_field_evaluation",
                    "mixed_coordinate_parameters":(current["parameters"]+fraction*direction[-10:]).tolist()}
                trial_info = {"level":level, "iteration":iteration, "backtrack":backtrack,
                              "fraction":fraction, "direction_method":linear["selected"]}
                try:
                    trial = system.evaluate(current["z"]+fraction*direction)
                    counters["complete_trials"] += 1
                except (FloatingPointError, ValueError, OverflowError) as error:
                    counters["rejected"] += 1
                    counters["domain_or_chart_rejections"] += 1
                    emit("R625_CONSISTENT_WEIGHTED_TRIAL", {**trial_info, "accepted":False,
                         "reason":"original_field_or_chart_domain", "error":type(error).__name__+":"+str(error)})
                    retained.pop("inflight_trial", None)
                    continue
                old_end = float(np.max(np.abs(current["terminal"])))
                new_end = float(np.max(np.abs(trial["terminal"])))
                trial_merit = system.weighted_merit(trial, cache)
                threshold = frozen_current_merit["phi"] + 1.e-4 * fraction * slope
                good = bool(trial_merit["phi"] < threshold
                            and new_end<=old_end+1.e-13*max(1., old_end))
                trial_actual = None
                if good:
                    retained["inflight_trial"]["phase"] = "actual_curve_true_history_readout"
                    try:
                        candidate = old.ActualC2StateCurve(system.x, trial["states"], trial["parameters"])
                        trial_actual = histories.evaluate(candidate, trial["chart"], grid, trial["states"])
                    except (FloatingPointError, ValueError, OverflowError) as error:
                        good = False
                        counters["actual_curve_rejections"] += 1
                        trial_info["actual_curve_error"] = type(error).__name__+":"+str(error)
                emit("R625_CONSISTENT_WEIGHTED_TRIAL", {**trial_info, "accepted":bool(good),
                     "unscaled_original_merit_norm":trial["norm"],
                     "weighted_merit_epoch":cache["merit_epoch"],
                     "same_weight_current_merit":frozen_current_merit,
                     "same_weight_trial_merit":trial_merit,
                     "same_weight_actual_Armijo_threshold":threshold,
                     "same_weight_directional_slope":slope,
                     "raw_norm_or_cross_epoch_weighted_values_are_not_acceptance":True,
                     "original_differential_max":float(np.max(np.abs(trial["differential"]))),
                     "all_ten_original_terminal_max":new_end,
                     "actual_curve_ruling_max":None if trial_actual is None else
                        trial_actual["report"]["actual_original_ruling_max"]})
                retained.pop("inflight_trial", None)
                if good:
                    previous_norm = frozen_current_merit["norm"]
                    current, actual = trial, trial_actual
                    counters["accepted"] += 1
                    accepted = True
                    if backtrack == 0 and trial_merit["norm"]<.8*previous_norm:
                        trust = min(args.maximum_trust, 1.5*trust)
                    elif backtrack:
                        trust = max(args.minimum_trust, .5*trust)
                    damping = max(1.e-12, linear["selected_damping"]/3)
                    retained.update(system=system, current=current, actual=actual, counters=counters)
                    retained["fixed_refinement"] = {"state":"pending", "attempted":False,
                                                     "reason":"new_accepted_original_BVP_state"}
                    old.checkpoint(system, current, actual, iteration,
                        "accepted_original_equations_consistent_frozen_weight_merit", counters, trust, damping)
                    cache = None
                    break
                counters["rejected"] += 1
        if not accepted:
            trust *= .25
            used_damping = max(damping, linear["selected_damping"],
                               linear.get("last_attempted_damping", damping))
            damping = min(1.e12, 10*used_damping)
            if trust<args.minimum_trust:
                status = "original_mixed_gauge_current_state_stalled"
                break
    if old.collocation_converged(current, args):
        status = ("original_feedback_and_true_integral_discrete_gates_met"
                  if old.actual_converged(current, actual, args) else
                  "original_collocation_converged_actual_curve_gates_pending")
    old.checkpoint(system, current, actual, iteration, status, counters, trust, damping)
    summary = {"status":status, "level":level, "counters":dict(counters),
               "original_collocation_and_stored_end_gate":old.collocation_converged(current, args),
               "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
               "actual_last_trust":trust, "actual_last_damping":damping,
               "seconds":time.monotonic()-started}
    emit("R625_PAID_GAUGE_LEVEL_FINAL", summary)
    return current, actual, summary


def main():
    reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--intervals", type=int, default=32)
    parser.add_argument("--order", type=int, default=16)
    parser.add_argument("--iterations", type=int, default=60)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.09375)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--minimum-trust", type=float, default=1.e-8)
    parser.add_argument("--damping", type=float, default=.008225263339969957)
    parser.add_argument("--boundary-fraction", type=float, default=.95)
    parser.add_argument("--minimum-usable-fraction", type=float, default=1.e-8)
    parser.add_argument("--svd-attempts", type=int, default=3)
    parser.add_argument("--ode-tol", type=float, default=1.e-7)
    parser.add_argument("--end-tol", type=float, default=1.e-8)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    parser.add_argument("--maximum-science-seconds", type=float, default=3300.)
    parser.add_argument("--final-reserve-seconds", type=float, default=180.)
    parser.add_argument("--maximum-active-height-rows",type=int,choices=[16],default=16)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    started = time.monotonic()
    clock = old.ScienceClock(started, args.maximum_science_seconds, args.final_reserve_seconds)
    source_progress, anchor_progress, retained = {}, {}, {}
    coefficients = potential = histories = chart_factory = source = None
    systems, summaries = [], []
    status, exception = "not_initialized", None
    try:
        source = load_paid_source(request, clock, source_progress)
        emit("R625_CONSISTENT_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_CONSISTENT_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
             "full_positive_Gram":potential.stats, "full_positive_potential_coefficient":1,
             "same_R598_mother":True, "old_identity_or_seed_qualification_replayed":False})
        chart_factory = RestoredMixedGaugeChart(source["payload"],
                                                coefficients, potential, clock, anchor_progress)
        emit("R625_RESTORED_PAID_LD_GAUGE_ANCHOR", anchor_progress)
        x = np.asarray(source["payload"]["x"], float)
        if len(x)!=2*args.intervals+1:
            raise ValueError("The declared continuation must use the paid 65-node grid.")
        states = np.asarray(source["payload"]["original_nineteen_states"], float)
        histories = previous.MixedActualReadouts(coefficients, potential, clock)
        grid = old.ObservedIntegralGrid(args.intervals, args.order, x, clock)
        system = ConsistentWeightedFullFeedback(x, coefficients, potential, clock, chart_factory,grid.x)
        systems.append(system)
        emit("R625_CONSISTENT_WEIGHTED_GLOBALIZATION", {
            "actual_previous_trust":source_progress["actual_previous_trust"],
            "actual_previous_damping":source_progress["actual_previous_damping"],
            "declared_new_initial_trust":args.trust,
            "declared_new_initial_damping":args.damping,
            "initial_damping_reason":"last actual ray acceptance next damping before the observed raw-merit ascent sequence",
            "initial_trust_reason":"explicit consistent-merit strategy restart from the paid actual ray state",
            "complete_same_weight_quadratic_ray_minimized_before_L_and_height_caps":True,
            "actual_Armijo_uses_same_frozen_weight_and_true_directional_slope":True,
            "original_raw_absolute_completion_and_physical_gates_unchanged":True,
            "old_backend_natural_path_restore_claim":False,
            "original_length_unchanged":float(chart_factory.initial_parameters[-1]),
            "original_terminal_h_unchanged":float(states[0,-1]),
            "same_complete_rows_QR_SVD_in_new_affine_height_nullspace":True,
            "all_singular_values_retained_without_column_rescaling":True,
            "actual_readout_height_row_activation_only_after_real_fraction_block":True,
            "free_length_preserves_full_cubic_height_chain":True,
            "sampled_height_constraints_do_not_qualify_other_lanes_or_continuous_curve":True,
            "unconstrained_direction_retested_at_each_new_state_for_release":True,
            "all_original_physical_boxes_and_all_original_rows_preserved":True})
        current, actual, summary = solve(system, states, chart_factory.initial_parameters,
            histories, grid, args, retained, paid_entry=source)
        summaries.append(summary)
        status = summary["status"]
        refined_result = None
        if retained["fixed_refinement"]["state"]!="completed":
            refined_result = old.fixed_curve_refinement(retained, histories, args, clock)
        if old.collocation_converged(current, args) and refined_result is not None:
            clock.check("before_conditional_second_original_mixed_BVP_mesh")
            fine_x, fine_grid, refined = refined_result
            emit("R625_CONSISTENT_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = ConsistentWeightedFullFeedback(fine_x, coefficients, potential, clock, chart_factory,fine_grid.x)
            systems.append(system2)
            current, actual, summary = solve(system2, refined["states_at_observations"],
                current["parameters"], histories, fine_grid, args, retained, level=1)
            summaries.append(summary)
            status = summary["status"]
            old.fixed_curve_refinement(retained, histories, args, clock)
    except ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_last_original_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "consistent_weighted_continuation_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_CONSISTENT_WEIGHTED_EXCEPTION", exception)
    if (histories is not None and "actual" in retained
            and retained.get("fixed_refinement", {}).get("state")!="completed"
            and not retained.get("fixed_refinement", {}).get("entry_considered", False)):
        try:
            old.fixed_curve_refinement(retained, histories, args, clock)
        except ClockCheckpoint as error:
            status = "public_clock_checkpoint_with_last_original_state_preserved"
            if exception is None:
                exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
        except Exception as error:
            if exception is None:
                exception = {"type":type(error).__name__, "message":str(error)}
    state = (None if source is None else source["payload"]) if "current" not in retained else {
        "parameters":retained["current"]["parameters"].tolist(),
        "x":retained["system"].x.tolist(),
        "original_nineteen_states":retained["current"]["states"].tolist(),
        "coordinate_order":mixed.COORDINATE_ORDER,
        "fixed_gauge_unit":mixed.GAUGE_UNIT_TEXT,
        "fixed_gauge_anchor_LD_decimal":chart_factory.anchor_decimal}
    paid_final = {} if source is None else source["final"]
    final = {
        "status":status, "exception":exception, "summaries":summaries,
        "original_paid_source":source_progress, "restored_paid_original_LD_anchor":anchor_progress,
        "actual_last_full_state":state,
        "actual_last_full_state_identity":None if state is None else old.identity(state),
        "actual_last_full_state_uses_paid_legacy_coordinates":False,
        "actual_last_original_differential_max":paid_final.get("actual_last_original_differential_max") if "current" not in retained else
            float(np.max(np.abs(retained["current"]["differential"]))),
        "actual_last_original_terminal_rows":paid_final.get("actual_last_original_terminal_rows") if "current" not in retained else
            np.asarray(retained["current"]["terminal"], float).tolist(),
        "actual_last_true_curve_report":paid_final.get("actual_last_true_curve_report") if "actual" not in retained else retained["actual"]["report"],
        "actual_last_true_report_inherited_without_new_evaluation":
            bool(retained["actual"].get("paid_report_only", False)) if "actual" in retained else source is not None,
        "actual_last_collocation_and_stored_end_gate":paid_final.get("actual_last_collocation_and_stored_end_gate") if "current" not in retained else
            old.collocation_converged(retained["current"], args),
        "actual_last_all_true_curve_gates":paid_final.get("actual_last_all_true_curve_gates") if "actual" not in retained else
            old.actual_converged(retained["current"], retained["actual"], args),
        "fixed_actual_curve_refinement_status":retained.get("fixed_refinement", paid_final.get("fixed_actual_curve_refinement_status")),
        "retained_counters":retained.get("counters"),
        "latest_complete_linear_report":retained.get("latest_complete_linear_report"),
        "latest_linear_attempt_reports_including_partial":[system.latest_linear_attempt_report for system in systems],
        "inflight_linear_at_checkpoint":retained.get("inflight_linear"),
        "inflight_trial_at_checkpoint":retained.get("inflight_trial"),
        "public_science_clock":clock.record(),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "center_chart_calls":sum(system.center_charts for system in systems),
        "center_chart_failures":sum(system.center_chart_failures for system in systems),
        "center_time_coefficient_calls":sum(system.center_time_coefficient_calls for system in systems),
        "center_chart_seconds":sum(system.center_seconds for system in systems),
        "mixed_chart_all_attempt_costs":None if chart_factory is None else {
            "calls":chart_factory.calls, "seconds":chart_factory.seconds,
            "coefficient_time_evaluations":chart_factory.coefficient_evaluations,
            "coefficient_time_seconds":chart_factory.coefficient_seconds},
        "full_feedback_state_points":sum(system.feedback_points for system in systems),
        "full_feedback_derivative_state_points":sum(system.feedback_derivative_points for system in systems),
        "full_feedback_seconds":sum(system.feedback_seconds for system in systems),
        "collocation_evaluations":sum(system.evaluations for system in systems),
        "complete_Jacobian_evaluations":sum(system.jacobians for system in systems),
        "Jacobian_cache_reuses_at_unchanged_state":sum(system.jacobian_cache_reuses for system in systems),
        "LU_cache_reuses_at_unchanged_state":sum(system.lu_cache_reuses for system in systems),
        "LU_attempts":sum(system.lu_attempts for system in systems),
        "LU_failures":sum(system.lu_failures for system in systems),
        "old_same_state_LU_LSMR_or_linear_diagnostic_replayed":False,
        "dense_direction_attempts":sum(system.dense_direction_attempts for system in systems),
        "dense_factor_cache_reuses":sum(system.dense_factor_cache_reuses for system in systems),
        "cached_failed_factor_retries_avoided":sum(system.cached_failed_factor_skips for system in systems),
        "dense_factor_and_solve_cost_by_mesh":[system.dense_factor_cost for system in systems],
        "all_actual_factor_receipts_including_uninstalled_partial":factor_receipts(),
        "all_affine_constraint_factor_receipts_including_partial":affine_factor_receipts(),
        "affine_constraint_factor_cost_by_mesh":[system.affine_factor_cost for system in systems],
        "new_actual_C2_height_operator_counts":dict(height.COUNTS),
        "new_full_weighted_ray_counts_by_mesh":[dict(system.original_ray_counts) for system in systems],
        "new_frozen_weight_merit_counts_by_mesh":[dict(system.weighted_merit_counts) for system in systems],
        "frozen_weight_epoch_receipts_by_mesh":[system.merit_epoch_receipts for system in systems],
        "latest_complete_same_weight_ray_attempts_including_partial":[system.latest_original_ray_attempt for system in systems],
        "actual_height_active_counts_by_mesh":[dict(system.height_active_counts) for system in systems],
        "latest_actual_height_value_receipts":[system.latest_height_value_receipt for system in systems],
        "latest_actual_factor_receipts_by_mesh":[system.latest_factor_receipts for system in systems],
        "direction_mode_selections":{name:sum(system.direction_mode_selections.get(name,0) for system in systems)
            for name in sorted(set().union(*(system.direction_mode_selections for system in systems)))},
        "length_boundary_activation_requests":sum(system.length_boundary_activation_requests for system in systems),
        "terminal_h_boundary_activation_requests":sum(system.terminal_h_activation_requests for system in systems),
        "LSMR_attempts":sum(system.lsmr_attempts for system in systems),
        "all_linear_solve_attempts":sum(system.linear_attempts for system in systems),
        "all_linear_solve_seconds":sum(system.linear_seconds for system in systems),
        "all_known_lsmr_iterations":sum(system.linear_lsmr_iterations for system in systems),
        "actual_true_history_readouts":None if histories is None else histories.calls,
        "completed_actual_true_history_readouts":None if histories is None else histories.completed,
        "actual_true_history_points":None if histories is None else histories.points,
        "actual_true_M_points":None if histories is None else histories.true_M_points,
        "actual_original_ruling_reassembly_rows":None if histories is None else histories.ruling_reassembly_rows,
        "actual_true_history_seconds":None if histories is None else histories.seconds,
        "full_history_calls":None if histories is None else histories.full.evaluations,
        "full_history_seconds":None if histories is None else histories.full.seconds,
        "old_D_root_seed_old_center_chart_or_paid_fixed_fine_replayed":False,
        "declared_new_direction_initial_trust":args.trust,
        "declared_new_direction_initial_damping":args.damping,
        "actual_prior_trust_and_damping":{key:source_progress.get(key) for key in ("actual_previous_trust", "actual_previous_damping")},
        "new_feasible_direction_scope_is_not_old_backend_restore":True,
        "same_weight_quadratic_ray_minimization_precedes_L_and_height_caps":True,
        "complete_original_direction_and_known_end_increments_share_one_fraction":True,
        "same_original_row_weights_Euclidean_penalty_and_active_rows":True,
        "nonlinear_acceptance_changed_to_matching_frozen_weight_slope_Armijo":True,
        "different_epoch_merit_values_not_directly_compared":True,
        "original_raw_absolute_completion_and_true_physical_gates_unchanged":True,
        "linear_Armijo_report_is_not_an_added_gate_or_nonlinear_qualification":True,
        "complete_row_Euclidean_damping_without_column_rescaling":True,
        "singular_direction_truncation_or_normal_equations_used":False,
        "all_original_known_end_increments_retained_in_affine_constraint_rhs":True,
        "existing_true_height_constraints_retained_no_new_eta_k_velocity_constraints":True,
        "free_L_complete_cubic_height_chain_and_fixed_L_exact_affine_chain":True,
        "new_sampled_h_constraints_do_not_certify_other_lanes_or_continuous_curve":True,
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_CONSISTENT_WEIGHTED_CONTINUATION_FINAL", final)


if __name__ == "__main__":
    main()
