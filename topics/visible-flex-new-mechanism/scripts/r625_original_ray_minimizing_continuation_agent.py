#!/usr/bin/env python3
"""Continue the actual two-acceptance curve with original-ray minimization.

All complete original rows, Euclidean damping, real height active rows and
the frozen nonlinear solve are retained. Only the full original Jd ray is
minimized before the exact existing L and true-height caps are considered.
Scientific arithmetic runs only in the declared public Actions.
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

import r625_true_height_active_continuation_agent as previous_height

dense = previous_height.dense
height = previous_height.height
previous, old, mixed = previous_height.previous, previous_height.old, previous_height.mixed
LD, reduced, original, paid = previous_height.LD, previous_height.reduced, previous_height.original, previous_height.paid
ClockCheckpoint, emit = previous_height.ClockCheckpoint, previous_height.emit
RestoredMixedGaugeChart = previous_height.RestoredMixedGaugeChart
factor_receipts = previous_height.factor_receipts
affine_factor_receipts = previous_height.affine_factor_receipts
# The full nonlinear loop, true-history gates and conditional second mesh
# remain the published function, including its original Armijo coefficient.
solve = dense.solve


def load_paid_source(request, clock, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update(stage="receive_original_two_acceptance_height_state", completed=False)
    wanted = request["paid_source"]
    try:
        clock.check("before_paid_height_terminal_log_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw) != wanted["log_bytes"] or progress["sha256"] != wanted["log_sha256"]:
            raise ValueError("The paid original height job log identity differs.")
        events, final_count = {}, 0
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE",
                        "R625_TRUE_HEIGHT_FEASIBLE_CONTINUATION_FINAL"):
                delimiter = " " + tag + " "
                if delimiter in line:
                    literal = line.split(delimiter, 1)[1]
                    events[tag] = json.loads(literal)
                    if tag == "R625_TRUE_HEIGHT_FEASIBLE_CONTINUATION_FINAL":
                        final_count += 1
                        progress["original_FINAL_json_bytes"] = len(literal.encode())
                        progress["original_FINAL_json_sha256"] = hashlib.sha256(literal.encode()).hexdigest()
        if final_count != 1:
            raise ValueError("The exact paid job has one complete natural final.")
        source = events["INVERSE_ACTIONS_SOURCE"]
        final = events["R625_TRUE_HEIGHT_FEASIBLE_CONTINUATION_FINAL"]
        entry = events["R620_FULL_FEEDBACK_STATE"]
        if (source["source_commit"] != wanted["source_commit"]
                or str(source["run_id"]) != str(wanted["run_id"])
                or source["request_sha256"] != wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"] != wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"] != wanted["FINAL_json_sha256"]):
            raise ValueError("The precise paid height scientific source differs.")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key: final["actual_last_full_state"][key] for key in keys}
        identity = old.identity(payload)
        if identity != wanted["state_identity"] or identity != final["actual_last_full_state_identity"]:
            raise ValueError("The original two-acceptance complete state identity differs.")
        if (payload["coordinate_order"] != mixed.COORDINATE_ORDER
                or payload["fixed_gauge_unit"] != mixed.GAUGE_UNIT_TEXT):
            raise ValueError("The paid original mixed coordinate frame differs.")
        plain = {key: payload[key] for key in keys[:3]}
        if (old.identity(plain) != entry["state_identity"] or plain != entry["state"]
                or old.identity(plain) != wanted["plain_checkpoint_identity"]):
            raise ValueError("The actual last checkpoint and complete final state differ.")
        if (final["retained_counters"]["accepted"] != 2
                or final["retained_counters"]["linear_direction_unavailable"] != 13
                or final["retained_counters"]["actual_curve_rejections"] != 0
                or final["status"] != "original_mixed_gauge_current_state_stalled"
                or final["fixed_actual_curve_refinement_status"]["state"] != "completed"
                or final["actual_last_true_report_inherited_without_new_evaluation"]
                or payload["parameters"][-1] != 2.100000000002248
                or payload["original_nineteen_states"][0][-1] != 2.9999937048523933
                or final["actual_last_true_curve_report"]["sampled_geometry_ranges"][0][1] != 2.999999999990668
                or final["fixed_actual_curve_refinement_status"]["actual_fine_report"]["actual_curve_points"] != 1153):
            raise ValueError("This scope consumes the exact two-acceptance state and its observed obstruction.")
        progress.update(stage="loaded_original_two_acceptance_state_reports_and_anchor", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"], original_state_identity=identity,
            old_science_seconds=final["new_science_seconds"], old_counters=final["retained_counters"],
            actual_previous_trust=entry["trust"], actual_previous_damping=entry["damping"],
            paid_exact_length=payload["parameters"][-1],
            paid_exact_terminal_h=payload["original_nineteen_states"][0][-1],
            old_fine_is_already_completed=True, old_LD_anchor_is_already_saved=True,
            old_final_report_from_actual_last_of_two_accepted_states=True,
            source_report_origin="two actual accepted coarse readouts and their completed final same-curve fine",
            no_old_scientific_qualification_replayed=True)
        clock.check("after_paid_height_terminal_log_receive_and_parse")
        return {"payload": payload, "final": final, "entry": entry, "source": source}
    finally:
        progress["seconds"] = time.monotonic() - started


class OriginalRayMinimizingFullFeedback(previous_height.TrueHeightActiveFullFeedback):
    """Original full d is unchanged; only its scalar trial prefix is chosen."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_ray_counts = defaultdict(int)
        self.latest_original_ray_attempt = None

    @staticmethod
    def _finite_observation(value):
        return float(value) if value is not None and np.isfinite(value) else None

    def _complete_original_ray(self, current, matrix, direction):
        self.clock.check("before_complete_original_Jd_ray")
        started = time.monotonic()
        self.original_ray_counts["ray_attempts"] += 1
        progress = {"phase": "full_original_Jd", "completed": False,
                    "complete_matrix_shape": list(matrix.shape),
                    "all_eliminated_known_end_increments_in_full_direction": True}
        self.latest_original_ray_attempt = progress
        try:
            residual = np.asarray(current["residual"], float)
            size = float(np.max(np.abs(direction)))
            self.original_ray_counts["Jd_products_attempted"] += 1
            with np.errstate(over="ignore", invalid="ignore", divide="ignore", under="ignore"):
                derivative = matrix @ direction
                self.original_ray_counts["Jd_products_completed"] += 1
                remainder = residual + derivative
                finite = bool(np.all(np.isfinite(direction)) and np.isfinite(size)
                              and np.all(np.isfinite(residual)) and np.all(np.isfinite(derivative))
                              and np.all(np.isfinite(remainder)) and np.isfinite(current["norm"]))
                slope = float(np.dot(residual, derivative)) if finite else None
                quadratic = float(np.dot(derivative, derivative)) if finite else None
                remainder_max = float(np.max(np.abs(remainder))) if finite else None
            slope = self._finite_observation(slope)
            quadratic = self._finite_observation(quadratic)
            remainder_max = self._finite_observation(remainder_max)
            ray = {"residual": residual, "derivative": derivative, "size": size,
                   "norm": float(current["norm"]), "slope": slope, "quadratic": quadratic,
                   "remainder_max": remainder_max, "finite": finite}
            progress.update(phase="complete_full_original_ray", completed=True,
                original_directional_inner_product=slope, original_Jd_squared_norm=quadratic,
                unscaled_full_direction_infinity_norm=self._finite_observation(size),
                complete_original_merit_norm=self._finite_observation(current["norm"]))
            self.original_ray_counts["rays_completed"] += 1
            if slope is not None and slope >= 0.:
                self.original_ray_counts["nonnegative_original_slopes"] += 1
            self.clock.check("after_complete_original_Jd_ray")
            return ray
        finally:
            progress["seconds"] = time.monotonic() - started
            self.original_ray_counts["full_ray_seconds"] += progress["seconds"]

    def _ray_prediction(self, ray, maximum_fraction, minimum_fraction):
        """Every later cap is a direct minimum, never a trust multiply/divide."""
        started = time.monotonic()
        self.original_ray_counts["fraction_prediction_attempts"] += 1
        try:
            cap = float(min(1., max(0., maximum_fraction)))
            slope, quadratic = ray["slope"], ray["quadratic"]
            has_minimizer = bool(ray["finite"] and slope is not None and slope < 0.
                                 and quadratic is not None and quadratic > 0.)
            minimizer, minimizer_capped, beyond_finite = None, None, False
            if has_minimizer:
                # Avoid overflowing a ratio that cannot restrict any cap<=1.
                minimizer_capped = 1. if -slope >= quadratic else float(-slope / quadratic)
                with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
                    full_minimizer = float(np.float64(-slope) / np.float64(quadratic))
                minimizer = self._finite_observation(full_minimizer)
                beyond_finite = minimizer is None
            fraction = min(cap, minimizer_capped) if has_minimizer else cap
            predicted_norm = requested_norm = None
            with np.errstate(over="ignore", invalid="ignore", divide="ignore", under="ignore"):
                predicted = ray["residual"] + fraction * ray["derivative"]
                requested = ray["residual"] + cap * ray["derivative"]
                finite = bool(ray["finite"] and np.all(np.isfinite(predicted))
                              and np.all(np.isfinite(requested)))
                if finite:
                    predicted_norm = self._finite_observation(np.linalg.norm(predicted))
                    requested_norm = self._finite_observation(np.linalg.norm(requested))
                threshold = self._finite_observation(ray["norm"] * (1. - 1.e-4 * fraction))
            reasons = []
            if not has_minimizer:
                reasons.append("no_finite_strictly_negative_original_ray_slope_with_positive_Jd_norm")
            if fraction < minimum_fraction:
                reasons.append("trust_fraction_below_declared_usable_floor")
            if predicted_norm is None or not predicted_norm < ray["norm"]:
                reasons.append("no_finite_original_linear_predicted_descent")
            report = {"usable": bool(not reasons), "reasons": reasons,
                "unscaled_coordinate_direction_infinity_norm": self._finite_observation(ray["size"]),
                "trust_fraction": fraction, "maximum_fraction_before_ray_minimization": cap,
                "original_linear_remainder_max": ray["remainder_max"],
                "original_merit_norm_before": self._finite_observation(ray["norm"]),
                "original_predicted_merit_at_trust_fraction": predicted_norm,
                "original_predicted_merit_at_requested_fraction": requested_norm,
                "original_merit_directional_inner_product": slope,
                "original_Jd_squared_norm": quadratic,
                "original_quadratic_minimizing_fraction": minimizer,
                "quadratic_minimizer_exceeds_finite_float_range": beyond_finite,
                "quadratic_minimizer_capped_at_one": minimizer_capped,
                "ray_minimization_limits_requested_fraction": bool(has_minimizer and fraction < cap),
                "original_linear_Armijo_threshold_at_selected_fraction": threshold,
                "original_linear_Armijo_at_selected_fraction": bool(predicted_norm is not None
                    and threshold is not None and predicted_norm < threshold),
                "linear_Armijo_observation_is_not_an_added_gate_or_true_acceptance": True,
                "all_ten_linear_end_rows_paid": True,
                "same_scalar_fraction_multiplies_full_direction_including_known_end_increments": True,
                "no_fraction_increase_after_explicit_prior_caps": bool(fraction <= cap),
                "condition_number_inferred_from_size": False}
            self.original_ray_counts["fraction_predictions_completed"] += 1
            self.latest_original_ray_attempt["last_fraction_prediction"] = report
            return report
        finally:
            self.original_ray_counts["fraction_prediction_seconds"] += time.monotonic() - started

    def direction_prediction(self, current, matrix, direction, trust, minimum_fraction):
        if direction is None:
            return {"usable": False, "reason": "no_finite_complete_original_row_direction"}
        ray = self._complete_original_ray(current, matrix, direction)
        cap = float(min(1., max(0., trust) / max(1.e-30, ray["size"])))
        return self._ray_prediction(ray, cap, minimum_fraction)

    def feasible_prediction(self, current, cache, direction, trust, args):
        if direction is None:
            return {"usable": False, "reason": "no_finite_complete_original_row_direction"}
        # One full original Jd serves every scalar prediction for this same
        # direction. The full direction, current and matrix remain live here.
        ray = self._complete_original_ray(current, cache["matrix"], direction)
        requested = float(min(1., max(0., trust) / max(1.e-30, ray["size"])))
        raw = self._ray_prediction(ray, requested, args.minimum_usable_fraction)
        length, increment = LD(current["parameters"][-1]), LD(direction[-1])
        if increment < 0:
            boundary, maximum = "lower", float((length - LD("2.1")) / -increment)
        elif increment > 0:
            boundary, maximum = "upper", float((LD("7.9") - length) / increment)
        else:
            boundary, maximum = None, None
        nonfinite = maximum is not None and not np.isfinite(maximum)
        if nonfinite:
            maximum = None
        before_length = raw["trust_fraction"]
        length_limited = maximum is not None and args.boundary_fraction * maximum < before_length
        length_cap = (min(before_length, max(0., args.boundary_fraction * maximum))
                      if length_limited else before_length)
        after_length = (self._ray_prediction(ray, length_cap, args.minimum_usable_fraction)
                        if length_limited else dict(raw))
        h = self.height_rows.sufficient_fraction(current, cache["height_geometry"], direction,
            after_length["trust_fraction"], args.boundary_fraction)
        height_cap = min(after_length["trust_fraction"], h["height_sufficient_fraction"])
        actual = (self._ray_prediction(ray, height_cap, args.minimum_usable_fraction)
                  if h["height_limits_fraction"] else dict(after_length))
        actual.update({"requested_trust": trust, "unrestricted_prediction": raw,
            "after_only_length_bound_prediction": after_length,
            "exact_original_length_before": float(length), "original_length_increment": float(increment),
            "original_length_box": [2.1, 7.9], "length_direction_boundary": boundary,
            "maximum_length_feasible_fraction": maximum,
            "maximum_length_fraction_exceeds_finite_float_range": bool(nonfinite),
            "length_boundary_limits_fraction": bool(length_limited),
            "length_boundary_blocks_otherwise_usable_direction": bool(length_limited
                and raw["usable"] and not after_length["usable"]),
            "boundary_safety_fraction": args.boundary_fraction,
            "exact_original_terminal_h_before": float(current["states"][0, -1]),
            "true_height_prediction": h,
            "true_height_blocks_otherwise_usable_direction": bool(h["height_limits_fraction"]
                and after_length["usable"] and not actual["usable"]),
            "complete_actual_height_map_values": self.latest_height_value_receipt,
            "original_terminal_h_cap_replaced_by_all_original_actual_height_points": True,
            "free_length_uses_complete_cubic_height_chain": True,
            "original_values_snapped_or_changed_before_direction": False,
            "explicit_fraction_caps_never_reconstructed_through_trust_times_direction_norm": True,
            "sampled_height_feasibility_is_not_complete_physical_or_continuous_qualification": True})
        self.clock.check("after_original_ray_and_existing_L_height_caps")
        return actual


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
    parser.add_argument("--damping", type=float, default=.0740273700597296)
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
        emit("R625_RAY_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_RAY_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
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
        system = OriginalRayMinimizingFullFeedback(x, coefficients, potential, clock, chart_factory,grid.x)
        systems.append(system)
        emit("R625_ORIGINAL_RAY_GLOBALIZATION", {
            "actual_previous_trust":source_progress["actual_previous_trust"],
            "actual_previous_damping":source_progress["actual_previous_damping"],
            "declared_new_initial_trust":args.trust,
            "declared_new_initial_damping":args.damping,
            "initial_damping_reason":"last actual accepted state next damping, before the observed full-step overshoot sequence",
            "initial_trust_reason":"last actual accepted trust; explicit new ray strategy, not terminal backend restoration",
            "full_original_quadratic_ray_minimized_before_L_and_height_caps":True,
            "original_fixed_coefficient_Armijo_actual_acceptance_unchanged":True,
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
            emit("R625_RAY_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = OriginalRayMinimizingFullFeedback(fine_x, coefficients, potential, clock, chart_factory,fine_grid.x)
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
        status = "original_quadratic_ray_continuation_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_ORIGINAL_RAY_EXCEPTION", exception)
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
        "new_full_original_ray_counts_by_mesh":[dict(system.original_ray_counts) for system in systems],
        "latest_full_original_ray_attempts_including_partial":[system.latest_original_ray_attempt for system in systems],
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
        "original_quadratic_ray_minimization_precedes_L_and_height_caps":True,
        "complete_original_direction_and_known_end_increments_share_one_fraction":True,
        "same_original_row_weights_Euclidean_penalty_active_rows_and_nonlinear_acceptance":True,
        "linear_Armijo_report_is_not_an_added_gate_or_nonlinear_qualification":True,
        "complete_row_Euclidean_damping_without_column_rescaling":True,
        "singular_direction_truncation_or_normal_equations_used":False,
        "all_original_known_end_increments_retained_in_affine_constraint_rhs":True,
        "only_new_true_height_constraints_no_eta_k_velocity_constraints":True,
        "free_L_complete_cubic_height_chain_and_fixed_L_exact_affine_chain":True,
        "new_sampled_h_constraints_do_not_certify_other_lanes_or_continuous_curve":True,
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_ORIGINAL_RAY_CONTINUATION_FINAL", final)


if __name__ == "__main__":
    main()
