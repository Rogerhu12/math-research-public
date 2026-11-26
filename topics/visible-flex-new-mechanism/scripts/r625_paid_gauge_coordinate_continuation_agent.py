#!/usr/bin/env python3
"""Continue the paid R620/R625 state in equivalent original gauge coordinates.

No old D/root, analytic seed integral, entry true-history readout or paid
fixed fine is replayed. The old log is a checked read-only source. Unstored
LD center data, original tables, current flow and Jacobian are necessarily
reconstructed and charged. Full original equations and gates remain intact.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import lsmr, splu

import r620_free_center_full_feedback_bvp_agent as old
import r625_paid_mixed_gauge_chart_agent as mixed

LD, reduced, original, paid = old.LD, old.reduced, old.original, old.paid
ClockCheckpoint = old.ClockCheckpoint


def json_scalar(value):
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    raise TypeError("Unsupported output type "+type(value).__name__)


def emit(tag, value):
    print(tag+" "+json.dumps(value, sort_keys=True, allow_nan=False,
                            default=json_scalar), flush=True)


# Only the published module's output adapter changes in this process.
# Its original scientific expressions/classes are not rewritten.
old.emit = emit


def load_paid_source(request, clock, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update({"stage":"receive_original_paid_log_from_stdlib_preloader", "completed":False})
    source = request["paid_source"]
    try:
        clock.check("before_paid_original_log_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update({"bytes":len(raw), "sha256":hashlib.sha256(raw).hexdigest()})
        if (len(raw)!=source["log_bytes"] or progress["sha256"]!=source["log_sha256"]):
            raise ValueError("The original paid job log identity changed.")
        clock.check("after_paid_original_log_receive")
        events = {}
        wanted = ("INVERSE_ACTIONS_SOURCE", "R620_TRUE_FREE_CENTER_INPUT",
                  "R620_FULL_FEEDBACK_STATE", "R620_FULL_FEEDBACK_FINAL")
        for line in raw.decode("utf-8").splitlines():
            for name in wanted:
                delimiter = " "+name+" "
                if delimiter in line:
                    events[name] = json.loads(line.split(delimiter, 1)[1])
        original_source = events["INVERSE_ACTIONS_SOURCE"]
        final, entry = events["R620_FULL_FEEDBACK_FINAL"], events["R620_FULL_FEEDBACK_STATE"]
        if (original_source["source_commit"]!=source["source_commit"]
                or str(original_source["run_id"])!=str(source["run_id"])
                or original_source["request_sha256"]!=source["request_sha256"]):
            raise ValueError("The original scientific source identity is not the declared one.")
        payload = {key:final["actual_last_full_state"][key]
                   for key in ("parameters", "x", "original_nineteen_states")}
        identity = old.identity(payload)
        if identity!=source["state_identity"] or identity!=final["actual_last_full_state_identity"]:
            raise ValueError("The paid nineteen-state payload does not match its source identity.")
        if (entry["state_identity"]!=identity or final["retained_counters"]["accepted"]!=0
                or final["fixed_actual_curve_refinement_status"]["state"]!="completed"):
            raise ValueError("This continuation names the precise zero-acceptance paid source.")
        progress.update({"stage":"loaded_original_paid_state_and_reports", "completed":True,
                         "run_id":source["run_id"], "job_id":source["job_id"],
                         "original_state_identity":identity,
                         "old_science_seconds":final["new_science_seconds"],
                         "old_counters":final["retained_counters"],
                         "old_fine_is_already_completed":True,
                         "no_old_scientific_qualification_replayed":True})
        return {"payload":payload, "final":final, "entry":entry,
                "input":events["R620_TRUE_FREE_CENTER_INPUT"], "source":original_source}
    finally:
        progress["seconds"] = time.monotonic()-started


class MixedActualReadouts(old.ActualHistoryReadouts):
    def evaluate(self, model, chart, grid, stored=None):
        result = super().evaluate(model, chart, grid, stored)
        # The inherited report slot meant independent (a,j,f) coordinates.
        # New slots 7,8 are gauge offsets and are never mislabeled as jets.
        result["report"]["center_chart_a_j_f"] = None
        result["report"]["actual_mixed_center_a0"] = float(chart["parameters"][6])
        result["report"]["original_constant_gauge_offset_coordinates"] = (
            np.asarray(chart["parameters"][[7, 8]], float).tolist())
        result["report"]["higher_center_jets_are_implicit_original_flow_values"] = True
        return result


class MixedFullFeedback(old.FullFeedbackCollocation):
    def __init__(self, x, coefficients, potential, clock, chart_factory):
        super().__init__(x, coefficients, potential, clock)
        self.chart_factory = chart_factory
        self.lu_attempts = self.lu_failures = self.lsmr_attempts = 0
        self.jacobian_cache_reuses = self.lu_cache_reuses = 0
        self.latest_linear_attempt_report = None

    def chart(self, parameters):
        self.clock.check("before_complete_mixed_center_chart")
        self.center_charts += 1
        started = time.monotonic()
        try:
            result = self.chart_factory.build(parameters, True)
            self.center_time_coefficient_calls += result["receipt"]["coefficient_time_parameter_evaluations"]
            self.clock.check("after_complete_mixed_center_chart")
            return result
        except Exception:
            self.center_chart_failures += 1
            raise
        finally:
            self.center_seconds += time.monotonic()-started

    def prepare_linear_cache(self, current, matrix):
        self.clock.check("before_original_linear_cache_preparation")
        started = time.monotonic()
        end_indices = np.asarray([*range(5, 13), 3, 4])+19*(len(self.x)-2)
        free = np.ones(self.size, dtype=bool)
        free[end_indices] = False
        known = -np.asarray(current["terminal"], float)
        ode = matrix[:-10]
        target = -np.asarray(current["differential"], float)-ode[:, end_indices]@known
        full = ode[:, free].tocsc()
        row_scale = 1/np.maximum(1.e-30, np.asarray(abs(full).max(axis=1).toarray()).ravel())
        row_equilibrated = (diags(row_scale)@full).tocsc()
        column_scale = 1/np.maximum(1.e-30,
            np.asarray(abs(row_equilibrated).max(axis=0).toarray()).ravel())
        cache = {"matrix":matrix, "free":free, "end_indices":end_indices, "known":known,
                 "row_scale":row_scale, "row_equilibrated":row_equilibrated,
                 "scaled_target":row_scale*target, "column_scale":column_scale,
                 "lu_direction":None, "lu_error":None, "direction_requests":0,
                 "row_scale_range":[float(row_scale.min()), float(row_scale.max())],
                 "LU_column_scale_range":[float(column_scale.min()), float(column_scale.max())]}
        self.latest_linear_attempt_report = {"phase":"before_original_mixed_LU",
            "coordinate_order":mixed.COORDINATE_ORDER,
            "row_scale_range":cache["row_scale_range"],
            "LU_column_scale_range":cache["LU_column_scale_range"],
            "complete_original_rows":True, "all_ten_linear_end_rows_paid":True}
        self.clock.check("before_original_mixed_LU_direction")
        lu_start = time.monotonic()
        self.linear_attempts += 1
        self.lu_attempts += 1
        try:
            equilibrated = (row_equilibrated@diags(column_scale)).tocsc()
            factor = splu(equilibrated)
            solution = factor.solve(cache["scaled_target"])
            direction = np.zeros(self.size)
            direction[free] = column_scale*solution
            direction[end_indices] = known
            if not np.all(np.isfinite(direction)):
                raise FloatingPointError("The mixed-coordinate original LU direction is nonfinite.")
            cache["lu_direction"] = direction
        except (RuntimeError, ValueError, FloatingPointError) as error:
            self.lu_failures += 1
            cache["lu_error"] = type(error).__name__+":"+str(error)
        finally:
            cache["lu_seconds"] = time.monotonic()-lu_start
            self.linear_seconds += cache["lu_seconds"]
        self.latest_linear_attempt_report.update({"phase":"completed_original_mixed_LU",
            "seconds":cache["lu_seconds"], "error":cache["lu_error"],
            "unscaled_coordinate_direction_infinity_norm":None if cache["lu_direction"] is None
                else float(np.max(np.abs(cache["lu_direction"]))),
            "trust_prediction_not_yet_requested":True})
        self.clock.check("after_original_mixed_LU_direction")
        cache["preparation_seconds"] = time.monotonic()-started
        return cache

    @staticmethod
    def direction_prediction(current, matrix, direction, trust, minimum_fraction):
        if direction is None:
            return {"usable":False, "reason":"no_finite_LU_direction"}
        size = float(np.max(np.abs(direction)))
        fraction = float(min(1., trust/max(1.e-30, size)))
        with np.errstate(over="ignore", invalid="ignore"):
            derivative = matrix@direction
            residual = np.asarray(current["residual"], float)
            remainder = residual+derivative
            predicted = residual+fraction*derivative
            finite = bool(np.all(np.isfinite(derivative)) and np.all(np.isfinite(predicted))
                          and np.all(np.isfinite(remainder)))
            predicted_norm = float(np.linalg.norm(predicted)) if finite else None
            remainder_max = float(np.max(np.abs(remainder))) if finite else None
            slope = float(np.dot(residual, derivative)) if finite else None
        if slope is not None and not np.isfinite(slope):
            slope = None
        descent = bool(finite and predicted_norm is not None and np.isfinite(predicted_norm)
                       and predicted_norm<current["norm"])
        if predicted_norm is not None and not np.isfinite(predicted_norm):
            predicted_norm = None
        reasons = []
        if fraction<minimum_fraction:
            reasons.append("trust_fraction_below_declared_usable_floor")
        if not descent:
            reasons.append("no_finite_original_linear_predicted_descent")
        return {"usable":bool(not reasons), "reasons":reasons,
                "unscaled_coordinate_direction_infinity_norm":size,
                "trust_fraction":fraction,
                "original_linear_remainder_max":remainder_max,
                "original_merit_norm_before":current["norm"],
                "original_predicted_merit_at_trust_fraction":predicted_norm,
                "original_merit_directional_inner_product":slope,
                "all_ten_linear_end_rows_paid":True,
                "condition_number_inferred_from_size":False}

    def choose_direction(self, current, cache, trust, damping, args):
        self.clock.check("before_original_direction_selection")
        cache["direction_requests"] += 1
        if cache["direction_requests"]>1:
            self.lu_cache_reuses += 1
        lu_prediction = self.direction_prediction(current, cache["matrix"], cache["lu_direction"],
                                                  trust, args.minimum_usable_fraction)
        report = {"coordinate_order":mixed.COORDINATE_ORDER,
                  "fixed_original_gauge_unit":mixed.GAUGE_UNIT_TEXT,
                  "minimum_usable_LU_or_LSMR_fraction":args.minimum_usable_fraction,
                  "LU_original_direction":lu_prediction, "LU_error":cache["lu_error"],
                  "LU_direction_reused_at_same_state":cache["direction_requests"]>1,
                  "row_scale_range":cache["row_scale_range"],
                  "LU_column_scale_range":cache["LU_column_scale_range"],
                  "new_LSMR_attempts":[], "selected":None, "selected_damping":damping}
        self.latest_linear_attempt_report = report
        if lu_prediction["usable"]:
            report["selected"] = "full_original_mixed_coordinate_LU"
            report["selected_prediction"] = lu_prediction
            return cache["lu_direction"], report
        for attempt in range(args.lsmr_attempts):
            regularization = max(1.e-12, damping)*10.**attempt
            report["last_attempted_damping"] = regularization
            report["inflight_LSMR"] = {"attempt":attempt, "regularization_lambda":regularization,
                                      "phase":"before_solve"}
            self.clock.check("before_original_physical_coordinate_damped_LSMR")
            started = time.monotonic()
            self.linear_attempts += 1
            self.lsmr_attempts += 1
            report["inflight_LSMR"]["phase"] = "solving_complete_original_rows"
            result, error_text = None, None
            try:
                # Row scaling keeps every original row. No automatic column
                # inverse is used in the damping penalty: the penalty acts
                # on the actual mixed physical-coordinate step.
                result = lsmr(cache["row_equilibrated"], cache["scaled_target"],
                    damp=np.sqrt(regularization), atol=1.e-11, btol=1.e-11,
                    conlim=1.e12, maxiter=args.lsmr_maxiter)
                direction = np.zeros(self.size)
                direction[cache["free"]] = result[0]
                direction[cache["end_indices"]] = cache["known"]
                if not np.all(np.isfinite(direction)):
                    raise FloatingPointError("The full-row damped original direction is nonfinite.")
            except (RuntimeError, ValueError, FloatingPointError) as error:
                direction = None
                error_text = type(error).__name__+":"+str(error)
            finally:
                seconds = time.monotonic()-started
                self.linear_seconds += seconds
                if result is not None:
                    self.linear_lsmr_iterations += int(result[2])
            prediction = self.direction_prediction(current, cache["matrix"], direction,
                                                    trust, args.minimum_usable_fraction)
            attempt_record = {"attempt":attempt, "regularization_lambda":regularization,
                              "seconds":seconds, "error":error_text, "prediction":prediction,
                              "all_original_rows_present":True,
                              "all_ten_linear_end_rows_paid":True,
                              "penalty":"Euclidean mixed physical-coordinate increment"}
            if result is not None:
                estimates = dict(zip(("residual_norm_estimate", "normal_residual_norm_estimate",
                                      "matrix_norm_estimate", "condition_estimate", "solution_norm"),
                                     [float(value) for value in result[3:8]]))
                nonfinite = [key for key, value in estimates.items() if not np.isfinite(value)]
                attempt_record.update({"istop":int(result[1]), "iterations":int(result[2]),
                    **{key:(None if key in nonfinite else value) for key, value in estimates.items()},
                    "nonfinite_estimate_fields":nonfinite,
                    "estimates_are_not_strict_condition_or_error_bounds":True})
            report["new_LSMR_attempts"].append(attempt_record)
            report.pop("inflight_LSMR", None)
            self.clock.check("after_original_physical_coordinate_damped_LSMR")
            if prediction["usable"]:
                report.update({"selected":"full_original_row_damped_LSMR",
                               "selected_damping":regularization,
                               "selected_prediction":prediction})
                return direction, report
        return None, report


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
            "trust":trust, "damping":damping, "phase":"necessary_current_Jacobian_and_LU_cache"}
        if cache is None:
            matrix = system.jacobian(current)
            cache = system.prepare_linear_cache(current, matrix)
        else:
            system.jacobian_cache_reuses += 1
        counters["direction_requests"] += 1
        retained["inflight_linear"] = {"level":level, "iteration":iteration,
            "trust":trust, "damping":damping, "phase":"select_original_full_row_direction"}
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
                    emit("R625_PAID_ORIGINAL_TRIAL", {**trial_info, "accepted":False,
                         "reason":"original_field_or_chart_domain", "error":type(error).__name__+":"+str(error)})
                    retained.pop("inflight_trial", None)
                    continue
                old_end = float(np.max(np.abs(current["terminal"])))
                new_end = float(np.max(np.abs(trial["terminal"])))
                good = bool(trial["norm"]<current["norm"]*(1-1.e-4*fraction)
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
                emit("R625_PAID_ORIGINAL_TRIAL", {**trial_info, "accepted":bool(good),
                     "unscaled_original_merit_norm":trial["norm"],
                     "original_differential_max":float(np.max(np.abs(trial["differential"]))),
                     "all_ten_original_terminal_max":new_end,
                     "actual_curve_ruling_max":None if trial_actual is None else
                        trial_actual["report"]["actual_original_ruling_max"]})
                retained.pop("inflight_trial", None)
                if good:
                    previous_norm = current["norm"]
                    current, actual = trial, trial_actual
                    counters["accepted"] += 1
                    accepted = True
                    if backtrack == 0 and current["norm"]<.8*previous_norm:
                        trust = min(args.maximum_trust, 1.5*trust)
                    elif backtrack:
                        trust = max(args.minimum_trust, .5*trust)
                    damping = max(1.e-12, linear["selected_damping"]/3)
                    retained.update(system=system, current=current, actual=actual, counters=counters)
                    retained["fixed_refinement"] = {"state":"pending", "attempted":False,
                                                     "reason":"new_accepted_original_BVP_state"}
                    old.checkpoint(system, current, actual, iteration,
                        "accepted_original_mixed_gauge_merit", counters, trust, damping)
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
    parser.add_argument("--trust", type=float, default=.25)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--minimum-trust", type=float, default=1.e-8)
    parser.add_argument("--damping", type=float, default=1.e-6)
    parser.add_argument("--minimum-usable-fraction", type=float, default=1.e-8)
    parser.add_argument("--lsmr-attempts", type=int, default=3)
    parser.add_argument("--lsmr-maxiter", type=int, default=1600)
    parser.add_argument("--ode-tol", type=float, default=1.e-7)
    parser.add_argument("--end-tol", type=float, default=1.e-8)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    parser.add_argument("--maximum-science-seconds", type=float, default=3300.)
    parser.add_argument("--final-reserve-seconds", type=float, default=180.)
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
        emit("R625_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
             "full_positive_Gram":potential.stats, "full_positive_potential_coefficient":1,
             "same_R598_mother":True, "old_identity_or_seed_qualification_replayed":False})
        chart_factory = mixed.PaidMixedGaugeChart(source["payload"]["parameters"],
                                                  coefficients, potential, clock, anchor_progress)
        emit("R625_NECESSARY_LD_GAUGE_ANCHOR", anchor_progress)
        x = np.asarray(source["payload"]["x"], float)
        if len(x)!=2*args.intervals+1:
            raise ValueError("The declared continuation must use the paid 65-node grid.")
        states = np.asarray(source["payload"]["original_nineteen_states"], float)
        histories = MixedActualReadouts(coefficients, potential, clock)
        grid = old.ObservedIntegralGrid(args.intervals, args.order, x, clock)
        system = MixedFullFeedback(x, coefficients, potential, clock, chart_factory)
        systems.append(system)
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
            emit("R625_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = MixedFullFeedback(fine_x, coefficients, potential, clock, chart_factory)
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
        status = "paid_mixed_gauge_continuation_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_PAID_GAUGE_EXCEPTION", exception)
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
        "original_paid_source":source_progress, "necessary_original_LD_anchor":anchor_progress,
        "actual_last_full_state":state,
        "actual_last_full_state_identity":None if state is None else old.identity(state),
        "actual_last_full_state_uses_paid_legacy_coordinates":bool("current" not in retained and source is not None),
        "actual_last_original_differential_max":paid_final.get("actual_last_original_differential_max") if "current" not in retained else
            float(np.max(np.abs(retained["current"]["differential"]))),
        "actual_last_original_terminal_rows":paid_final.get("actual_last_original_terminal_rows") if "current" not in retained else
            np.asarray(retained["current"]["terminal"], float).tolist(),
        "actual_last_true_curve_report":paid_final.get("actual_last_true_curve_report") if "actual" not in retained else retained["actual"]["report"],
        "actual_last_true_report_inherited_without_new_evaluation":
            bool(retained.get("actual", {}).get("paid_report_only", source is not None)),
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
        "old_D_root_seed_or_paid_fixed_fine_replayed":False,
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_PAID_GAUGE_CONTINUATION_FINAL", final)


if __name__ == "__main__":
    main()
