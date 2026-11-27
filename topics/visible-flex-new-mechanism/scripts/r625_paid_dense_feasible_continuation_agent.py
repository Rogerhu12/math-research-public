#!/usr/bin/env python3
"""Complete-row Euclidean QR/SVD directions at the paid L and h(L) walls.

Original19flow/tenendrows/center/gauges/trueintegrals are inherited unchanged.
No old scalar input, initial curve qualification or already-paid fine is replayed.
All singular directions of each actual remaining-column matrix are retained;
only evidenced original-coordinate bound activations fix deltaL/deltahL to zero.
Scientific execution is confined to the declared public Actions.
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

import r625_paid_feasible_length_continuation_agent as length_scope
from r625_complete_rows_euclidean_qr_svd_agent import EuclideanCompleteRowFactor, factor_receipts

previous = length_scope.previous
old, mixed = previous.old, previous.mixed
LD, reduced, original, paid = old.LD, old.reduced, old.original, old.paid
ClockCheckpoint, emit = old.ClockCheckpoint, previous.emit
RestoredMixedGaugeChart = length_scope.RestoredMixedGaugeChart


def load_paid_source(request, clock, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update(stage="receive_original_paid_feasible_length_state", completed=False)
    wanted = request["paid_source"]
    try:
        clock.check("before_paid_feasible_length_log_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw)!=wanted["log_bytes"] or progress["sha256"]!=wanted["log_sha256"]:
            raise ValueError("The paid feasible-length job log identity differs.")
        events, final_count = {}, 0
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE",
                        "R625_FEASIBLE_LENGTH_CONTINUATION_FINAL"):
                delimiter = " "+tag+" "
                if delimiter in line:
                    payload_text = line.split(delimiter, 1)[1]
                    events[tag] = json.loads(payload_text)
                    if tag=="R625_FEASIBLE_LENGTH_CONTINUATION_FINAL":
                        final_count += 1
                        progress["original_FINAL_json_bytes"] = len(payload_text.encode())
                        progress["original_FINAL_json_sha256"] = hashlib.sha256(payload_text.encode()).hexdigest()
        if final_count!=1:
            raise ValueError("The exact paid job has one natural final.")
        source = events["INVERSE_ACTIONS_SOURCE"]
        final = events["R625_FEASIBLE_LENGTH_CONTINUATION_FINAL"]
        entry = events["R620_FULL_FEEDBACK_STATE"]
        if (source["source_commit"]!=wanted["source_commit"]
                or str(source["run_id"])!=str(wanted["run_id"])
                or source["request_sha256"]!=wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"]!=wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"]!=wanted["FINAL_json_sha256"]):
            raise ValueError("The precise original feasible-length scientific source differs.")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key:final["actual_last_full_state"][key] for key in keys}
        identity = old.identity(payload)
        if identity!=wanted["state_identity"] or identity!=final["actual_last_full_state_identity"]:
            raise ValueError("The original feasible-length payload identity differs.")
        if (payload["coordinate_order"]!=mixed.COORDINATE_ORDER
                or payload["fixed_gauge_unit"]!=mixed.GAUGE_UNIT_TEXT):
            raise ValueError("The paid original mixed coordinate frame differs.")
        plain = {key:payload[key] for key in keys[:3]}
        if (old.identity(plain)!=entry["state_identity"] or plain!=entry["state"]
                or old.identity(plain)!=wanted["plain_checkpoint_identity"]):
            raise ValueError("The paid last checkpoint and actual final state differ.")
        if (final["retained_counters"]["accepted"]!=40
                or final["status"]!="original_mixed_gauge_current_state_stalled"
                or final["fixed_actual_curve_refinement_status"]["state"]!="completed"
                or final["actual_last_true_report_inherited_without_new_evaluation"]
                or payload["parameters"][-1]!=2.1000000000449615
                or payload["original_nineteen_states"][0][-1]!=2.9999999999920437
                or final["LSMR_attempts"]!=93
                or final["all_known_lsmr_iterations"]!=148800):
            raise ValueError("This scope consumes the exact40-acceptance original state and observed walls.")
        progress.update(stage="loaded_original_feasible_state_reports_and_anchor", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"], original_state_identity=identity,
            old_science_seconds=final["new_science_seconds"], old_counters=final["retained_counters"],
            actual_previous_trust=entry["trust"], actual_previous_damping=entry["damping"],
            paid_exact_length=payload["parameters"][-1],
            paid_exact_terminal_h=payload["original_nineteen_states"][0][-1],
            old_fine_is_already_completed=True, old_LD_anchor_is_already_saved=True,
            old_true_report_is_actual40accepted_readouts_plus1fine=True,
            source_report_origin="40 actual accepted readouts plus1 fixed fine",
            no_old_scientific_qualification_replayed=True)
        clock.check("after_paid_feasible_length_log_receive_and_parse")
        return {"payload":payload, "final":final, "entry":entry, "source":source}
    finally:
        progress["seconds"] = time.monotonic()-started


class DenseFeasibleFullFeedback(previous.MixedFullFeedback):
    def __init__(self, x, coefficients, potential, clock, chart_factory):
        super().__init__(x, coefficients, potential, clock, chart_factory)
        self.dense_factor_cost = {}
        self.dense_factor_cache_reuses = self.dense_direction_attempts = 0
        self.cached_failed_factor_skips = 0
        self.length_boundary_activation_requests = self.terminal_h_activation_requests = 0
        self.direction_mode_selections = {"free":0, "length":0, "terminal_h":0,
                                          "length_and_terminal_h":0}
        self.latest_factor_receipts = {}

    @property
    def terminal_h_index(self):
        # z stores all19 states of nodes1..N-1, then the ten physical parameters.
        return 19*(len(self.x)-2)

    def prepare_linear_cache(self, current, matrix):
        self.clock.check("before_complete_rows_dense_linear_cache")
        started = time.monotonic()
        end_indices = np.asarray([*range(5, 13), 3, 4])+self.terminal_h_index
        free = np.ones(self.size, dtype=bool)
        free[end_indices] = False
        free_indices = np.flatnonzero(free)
        known = -np.asarray(current["terminal"], float)
        ode = matrix[:-10]
        target = -np.asarray(current["differential"], float)-ode[:, end_indices]@known
        full = ode[:, free].tocsc()
        # Identical old all-free row weights; every active-column subproblem
        # takes a literal column subset and retains these same row weights.
        row_scale = 1/np.maximum(1.e-30, np.asarray(abs(full).max(axis=1).toarray()).ravel())
        row_equilibrated = (diags(row_scale)@full).tocsc()
        cache = {"matrix":matrix, "free":free, "free_indices":free_indices,
            "end_indices":end_indices, "known":known, "row_scale":row_scale,
            "row_equilibrated":row_equilibrated, "scaled_target":row_scale*target,
            "factors":{}, "factor_failures":{}, "direction_requests":0,
            "row_scale_range":[float(row_scale.min()), float(row_scale.max())]}
        self.latest_factor_receipts = {}
        self.latest_linear_attempt_report = {"phase":"prepared_same_complete_original_rows",
            "coordinate_order":mixed.COORDINATE_ORDER,
            "row_scale_range":cache["row_scale_range"], "column_rescaling":False,
            "all_original_rows_present":True, "all_ten_linear_end_rows_paid":True,
            "old_LU_or_LSMR_replayed":False}
        cache["preparation_seconds"] = time.monotonic()-started
        self.clock.check("after_complete_rows_dense_linear_cache")
        return cache

    @staticmethod
    def mode_name(active):
        if not active:
            return "free"
        if active==frozenset(("length", "terminal_h")):
            return "length_and_terminal_h"
        return next(iter(active))

    def feasible_prediction(self, current, cache, direction, trust, args):
        if direction is None:
            return {"usable":False, "reason":"no_finite_complete_row_QR_SVD_direction"}
        raw = self.direction_prediction(current, cache["matrix"], direction,
                                        trust, args.minimum_usable_fraction)
        length = LD(current["parameters"][-1])
        length_increment = LD(direction[-1])
        terminal_h = LD(current["states"][0, -1])
        h_increment = LD(direction[self.terminal_h_index])
        if length_increment<0:
            length_boundary, maximum_length = "lower", float((length-LD('2.1'))/-length_increment)
        elif length_increment>0:
            length_boundary, maximum_length = "upper", float((LD('7.9')-length)/length_increment)
        else:
            length_boundary, maximum_length = None, None
        maximum_h = float((LD(3)-terminal_h)/h_increment) if h_increment>0 else None
        nonfinite = []
        if maximum_length is not None and not np.isfinite(maximum_length):
            nonfinite.append("maximum_length_feasible_fraction")
            maximum_length = None
        if maximum_h is not None and not np.isfinite(maximum_h):
            nonfinite.append("maximum_terminal_h_upper_feasible_fraction")
            maximum_h = None
        initial_fraction = raw["trust_fraction"]
        length_limited = (maximum_length is not None and
                          args.boundary_fraction*maximum_length<initial_fraction)
        length_fraction = (max(0., args.boundary_fraction*maximum_length)
                           if length_limited else initial_fraction)
        size = raw["unscaled_coordinate_direction_infinity_norm"]
        length_prediction = (self.direction_prediction(current, cache["matrix"], direction,
            length_fraction*max(1.e-30, size), args.minimum_usable_fraction)
            if length_limited else dict(raw))
        height_limited = maximum_h is not None and args.boundary_fraction*maximum_h<length_fraction
        fraction = max(0., args.boundary_fraction*maximum_h) if height_limited else length_fraction
        actual = (self.direction_prediction(current, cache["matrix"], direction,
            fraction*max(1.e-30, size), args.minimum_usable_fraction)
            if height_limited else dict(length_prediction))
        actual.update({"requested_trust":trust, "unrestricted_prediction":raw,
            "after_only_length_bound_prediction":length_prediction,
            "exact_original_length_before":float(length),
            "original_length_increment":float(length_increment), "original_length_box":[2.1,7.9],
            "length_direction_boundary":length_boundary,
            "maximum_length_feasible_fraction":maximum_length,
            "length_boundary_limits_fraction":bool(length_limited),
            "length_boundary_blocks_otherwise_usable_direction":
                bool(length_limited and raw["usable"] and not length_prediction["usable"]),
            "exact_original_terminal_h_before":float(terminal_h),
            "original_terminal_h_increment":float(h_increment), "original_terminal_h_upper_bound":3.,
            "maximum_terminal_h_upper_feasible_fraction":maximum_h,
            "terminal_h_upper_limits_fraction":bool(height_limited),
            "terminal_h_upper_blocks_otherwise_usable_direction":
                bool(height_limited and length_prediction["usable"] and not actual["usable"]),
            "boundary_safety_fraction":args.boundary_fraction,
            "nonfinite_fraction_limits_reported_as_unrestrictive":nonfinite,
            "original_values_snapped_or_changed_before_direction":False,
            "linear_two_coordinate_bound_is_not_complete_curve_feasibility":True})
        return actual

    def dense_direction(self, current, cache, trust, regularization, args, report, attempt, active):
        label = self.mode_name(active)
        indices = cache["free_indices"]
        mask = np.ones(len(indices), dtype=bool)
        if "length" in active:
            mask &= indices!=self.size-1
        if "terminal_h" in active:
            mask &= indices!=self.terminal_h_index
        selected_indices = indices[mask]
        report["last_attempted_damping"] = regularization
        report["inflight_dense_direction"] = {"attempt":attempt, "mode":label,
            "regularization_lambda":regularization, "phase":"factor_or_reuse_complete_original_rows",
            "matrix_shape":[cache["row_equilibrated"].shape[0], len(selected_indices)]}
        self.clock.check("before_complete_original_"+label+"_QR_SVD_direction")
        started = time.monotonic()
        self.dense_direction_attempts += 1
        direction, error_text, solve_report = None, None, None
        factor_reused = active in cache["factors"]
        factor_failure_reused = active in cache["factor_failures"]
        if factor_failure_reused:
            self.cached_failed_factor_skips += 1
        else:
            self.linear_attempts += 1
        try:
            if factor_failure_reused:
                # Lambda does not change this factor's input. Do not pay the
                # same failed QR/SVD again merely for another damping value.
                error_text = cache["factor_failures"][active]
            else:
                if not factor_reused:
                    matrix = cache["row_equilibrated"][:, mask].toarray()
                    factor = EuclideanCompleteRowFactor(matrix, cache["scaled_target"], self.clock,
                                                         self.dense_factor_cost, label)
                    cache["factors"][active] = factor
                    self.latest_factor_receipts[label] = factor.receipt
                    del matrix
                else:
                    factor = cache["factors"][active]
                    self.dense_factor_cache_reuses += 1
                report["inflight_dense_direction"]["phase"] = "all_singular_values_damped_solution"
                solution, solve_report = factor.solve(regularization)
                direction = np.zeros(self.size)
                direction[selected_indices] = solution
                direction[cache["end_indices"]] = cache["known"]
                if not np.all(np.isfinite(direction)):
                    raise FloatingPointError("The complete original-row dense direction is nonfinite.")
        except (RuntimeError, ValueError, FloatingPointError, np.linalg.LinAlgError) as error:
            # The public clock is never a numerical rejection or retry.
            if isinstance(error, ClockCheckpoint):
                raise
            error_text = type(error).__name__+":"+str(error)
            if active not in cache["factors"]:
                cache["factor_failures"][active] = error_text
            direction = None
        finally:
            seconds = time.monotonic()-started
            self.linear_seconds += seconds
        prediction = self.feasible_prediction(current, cache, direction, trust, args)
        attempt_record = {"attempt":attempt, "regularization_lambda":regularization,
            "active_mode":label, "matrix_shape":[cache["row_equilibrated"].shape[0], len(selected_indices)],
            "seconds":seconds, "error":error_text, "prediction":prediction,
            "same_state_mode_factor_reused":bool(factor_reused),
            "same_state_failed_factor_not_retried":bool(factor_failure_reused),
            "factor_receipt_at_this_attempt":(None if label not in self.latest_factor_receipts else
                dict(self.latest_factor_receipts[label])), "damped_solution":solve_report,
            "all_original_rows_present":True, "all_ten_linear_end_rows_paid":True,
            "delta_length_exactly_zero":bool("length" in active),
            "delta_terminal_h_exactly_zero":bool("terminal_h" in active),
            "exact_actual_length_held":float(current["parameters"][-1]) if "length" in active else None,
            "exact_actual_terminal_h_held":float(current["states"][0,-1]) if "terminal_h" in active else None,
            "column_rescaling":False, "rank_cutoff_or_singular_direction_truncation":False,
            "penalty":"Euclidean increment on the original remaining mixed coordinates"}
        report["new_dense_attempts"].append(attempt_record)
        report.pop("inflight_dense_direction", None)
        self.clock.check("after_complete_original_"+label+"_QR_SVD_direction")
        return direction, prediction

    def choose_direction(self, current, cache, trust, damping, args):
        self.clock.check("before_same_box_complete_row_dense_direction")
        cache["direction_requests"] += 1
        report = {"coordinate_order":mixed.COORDINATE_ORDER,
            "fixed_original_gauge_unit":mixed.GAUGE_UNIT_TEXT,
            "row_scale_range":cache["row_scale_range"], "column_rescaling":False,
            "rank_cutoff_or_singular_direction_truncation":False,
            "exact_original_length_before":float(current["parameters"][-1]),
            "exact_original_terminal_h_before":float(current["states"][0,-1]),
            "minimum_usable_fraction":args.minimum_usable_fraction,
            "new_dense_attempts":[], "actual_boundary_activation_triggers":[],
            "every_new_state_and_regularization_starts_free_for_release":True,
            "selected":None, "selected_damping":damping}
        self.latest_linear_attempt_report = report
        for attempt in range(args.svd_attempts):
            regularization = max(1.e-12, damping)*10.**attempt
            pending_modes, seen = [frozenset()], set()
            while pending_modes:
                active = pending_modes.pop(0)
                if active in seen:
                    continue
                seen.add(active)
                direction, prediction = self.dense_direction(current, cache, trust,
                    regularization, args, report, attempt, active)
                if prediction["usable"]:
                    label = self.mode_name(active)
                    report.update(selected="full_original_Euclidean_QR_SVD_"+label,
                        selected_damping=regularization, selected_prediction=prediction,
                        selected_active_mode=label)
                    self.direction_mode_selections[label] += 1
                    return direction, report
                activations = []
                if ("length" not in active and
                        prediction.get("length_boundary_blocks_otherwise_usable_direction", False)):
                    activations.append("length")
                if ("terminal_h" not in active and
                        prediction.get("terminal_h_upper_blocks_otherwise_usable_direction", False)):
                    activations.append("terminal_h")
                for coordinate in activations:
                    target = active|frozenset((coordinate,))
                    report["actual_boundary_activation_triggers"].append({
                        "attempt":attempt, "source_actual_mode":self.mode_name(active),
                        "activated_coordinate":coordinate, "next_actual_mode":self.mode_name(target),
                        "actual_complete_original_direction_prediction":prediction,
                        "action":"hold_only_the_original_increment_exactly_zero",
                        "same_row_weights_and_all_original_rows":True,
                        "current_value_is_not_snapped":True})
                    if coordinate=="length":
                        self.length_boundary_activation_requests += 1
                    else:
                        self.terminal_h_activation_requests += 1
                    if target not in seen and target not in pending_modes:
                        pending_modes.append(target)
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
            "trust":trust, "damping":damping, "phase":"necessary_current_Jacobian_and_dense_factor_cache"}
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
    parser.add_argument("--damping", type=float, default=1.5241579027587257e-8)
    parser.add_argument("--boundary-fraction", type=float, default=.95)
    parser.add_argument("--minimum-usable-fraction", type=float, default=1.e-8)
    parser.add_argument("--svd-attempts", type=int, default=3)
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
        emit("R625_DENSE_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_DENSE_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
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
        system = DenseFeasibleFullFeedback(x, coefficients, potential, clock, chart_factory)
        systems.append(system)
        emit("R625_NEW_DENSE_GLOBALIZATION", {
            "actual_previous_trust":source_progress["actual_previous_trust"],
            "actual_previous_damping":source_progress["actual_previous_damping"],
            "declared_new_initial_trust":args.trust,
            "declared_initial_damping_inherits_actual_previous_value":args.damping,
            "old_backend_natural_path_restore_claim":False,
            "original_length_unchanged":float(chart_factory.initial_parameters[-1]),
            "original_terminal_h_unchanged":float(states[0,-1]),
            "dense_complete_rows_QR_SVD_replaces_unconverged_LSMR":True,
            "all_singular_values_retained_without_column_rescaling":True,
            "h_terminal_activation_only_after_real_upper_bound_block":True,
            "two_linear_bounds_do_not_qualify_all_physical_nodes_or_curve":True,
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
            emit("R625_DENSE_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = DenseFeasibleFullFeedback(fine_x, coefficients, potential, clock, chart_factory)
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
        status = "dense_feasible_continuation_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_DENSE_FEASIBLE_EXCEPTION", exception)
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
        "latest_actual_factor_receipts_by_mesh":[system.latest_factor_receipts for system in systems],
        "direction_mode_selections":{name:sum(system.direction_mode_selections[name] for system in systems)
            for name in ("free", "length", "terminal_h", "length_and_terminal_h")},
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
        "complete_row_Euclidean_damping_without_column_rescaling":True,
        "singular_direction_truncation_or_normal_equations_used":False,
        "two_endpoint_bounds_do_not_certify_all_nodes_or_continuous_curve":True,
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_DENSE_FEASIBLE_CONTINUATION_FINAL", final)


if __name__ == "__main__":
    main()
