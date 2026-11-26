#!/usr/bin/env python3
"""Same-box feasible-length directions from the paid mixed-gauge state.

The exact paid length is never snapped to a bound. When a real full-row
direction points towards the length boundary and its feasible fraction is
unusable, an original rectangular full-row damped solve holds delta-L=0.
Every new state still tries the unconstrained direction, allowing release.
No old center chart, scalar input, entry readout or paid fine is replayed.
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

import r625_paid_gauge_coordinate_continuation_agent as previous

old, mixed = previous.old, previous.mixed
LD, reduced, original, paid = old.LD, old.reduced, old.original, old.paid
ClockCheckpoint, emit = old.ClockCheckpoint, previous.emit


def load_paid_source(request, clock, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update(stage="receive_original_paid_mixed_state", completed=False)
    wanted = request["paid_source"]
    try:
        clock.check("before_paid_mixed_log_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw)!=wanted["log_bytes"] or progress["sha256"]!=wanted["log_sha256"]:
            raise ValueError("The paid mixed-state job log identity differs.")
        events = {}
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE",
                        "R625_PAID_GAUGE_CONTINUATION_FINAL"):
                delimiter = " "+tag+" "
                if delimiter in line:
                    events[tag] = json.loads(line.split(delimiter, 1)[1])
        source = events["INVERSE_ACTIONS_SOURCE"]
        final = events["R625_PAID_GAUGE_CONTINUATION_FINAL"]
        entry = events["R620_FULL_FEEDBACK_STATE"]
        if (source["source_commit"]!=wanted["source_commit"]
                or str(source["run_id"])!=str(wanted["run_id"])
                or source["request_sha256"]!=wanted["request_sha256"]):
            raise ValueError("The precise original mixed-state scientific source differs.")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key:final["actual_last_full_state"][key] for key in keys}
        identity = old.identity(payload)
        if identity!=wanted["state_identity"] or identity!=final["actual_last_full_state_identity"]:
            raise ValueError("The original mixed-state payload identity differs.")
        if (payload["coordinate_order"]!=mixed.COORDINATE_ORDER
                or payload["fixed_gauge_unit"]!=mixed.GAUGE_UNIT_TEXT):
            raise ValueError("The paid original mixed coordinate frame differs.")
        plain = {key:payload[key] for key in keys[:3]}
        if old.identity(plain)!=entry["state_identity"] or plain!=entry["state"]:
            raise ValueError("The paid last checkpoint and actual final state differ.")
        if (final["retained_counters"]["accepted"]!=27
                or final["status"]!="original_mixed_gauge_current_state_stalled"
                or final["fixed_actual_curve_refinement_status"]["state"]!="completed"):
            raise ValueError("This scope consumes the precise naturally stalled paid state.")
        last_linear = final["latest_complete_linear_report"]
        if (last_linear["LU_original_direction"]["original_merit_norm_before"]
                !=entry["unscaled_original_merit_norm"]):
            raise ValueError("The inherited unusable LU report is not for the last original state.")
        progress.update(stage="loaded_original_mixed_state_reports_and_anchor", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"], original_state_identity=identity,
            old_science_seconds=final["new_science_seconds"], old_counters=final["retained_counters"],
            actual_previous_trust=entry["trust"], actual_previous_damping=entry["damping"],
            old_fine_is_already_completed=True, old_LD_anchor_is_already_saved=True,
            old_inherited_report_flag_is_a_known_metadata_error=True,
            source_report_origin="27 actual accepted readouts plus1 fixed fine, as source counters/state show",
            no_old_scientific_qualification_replayed=True)
        clock.check("after_paid_mixed_log_receive_and_parse")
        return {"payload":payload, "final":final, "entry":entry, "source":source}
    finally:
        progress["seconds"] = time.monotonic()-started


class RestoredMixedGaugeChart(mixed.PaidMixedGaugeChart):
    def __init__(self, payload, coefficients, potential, clock, progress):
        reduced.require_public_science()
        started = time.monotonic()
        self.coefficients, self.potential, self.clock = coefficients, potential, clock
        self.unit = LD(payload["fixed_gauge_unit"])
        self.calls = self.coefficient_evaluations = 0
        self.seconds = self.coefficient_seconds = 0.
        self.active_evaluator = None
        self.progress = progress
        progress.update(stage="restore_saved_original_LD_anchor", completed=False)
        try:
            clock.check("before_saved_original_mixed_gauge_anchor_restore")
            self.anchor_decimal = list(payload["fixed_gauge_anchor_LD_decimal"])
            self.anchor = np.asarray([LD(value) for value in self.anchor_decimal], dtype=LD)
            self.initial_parameters = np.asarray(payload["parameters"], float).copy()
            if self.anchor.shape!=(3,) or not np.all(np.isfinite(self.anchor)):
                raise ValueError("The saved original LD anchor has three finite values.")
            self.receipt = {"coordinate_order":mixed.COORDINATE_ORDER,
                "fixed_original_gauge_unit":mixed.GAUGE_UNIT_TEXT,
                "restored_original_LD_gauge_anchor_decimal":self.anchor_decimal,
                "same_actual_initial_parameters":self.initial_parameters.tolist(),
                "exact_paid_length_not_snapped_to_bound":float(self.initial_parameters[-1]),
                "old_center_chart_or_old_scalar_input_evaluations":0,
                "old_fixed_curve_readout_evaluations":0}
            progress.update(stage="restored_saved_original_mixed_frame", completed=True,
                            receipt=self.receipt)
            clock.check("after_saved_original_mixed_gauge_anchor_restore")
        finally:
            progress["seconds"] = time.monotonic()-started


class FeasibleLengthFullFeedback(previous.MixedFullFeedback):
    def __init__(self, x, coefficients, potential, clock, chart_factory,
                 paid_linear_report=None, initial_trust=.25, minimum_fraction=1.e-8):
        super().__init__(x, coefficients, potential, clock, chart_factory)
        self.paid_linear_report = paid_linear_report
        self.initial_trust = initial_trust
        self.minimum_fraction = minimum_fraction
        self.paid_LU_direction_skips = 0
        self.unconstrained_lsmr_attempts = self.fixed_length_lsmr_attempts = 0
        self.fixed_length_direction_selections = self.free_length_direction_selections = 0
        self.length_boundary_activation_requests = 0

    def prepare_linear_cache(self, current, matrix):
        self.clock.check("before_feasible_original_linear_cache")
        started = time.monotonic()
        end_indices = np.asarray([*range(5, 13), 3, 4])+19*(len(self.x)-2)
        free = np.ones(self.size, dtype=bool)
        free[end_indices] = False
        free_indices = np.flatnonzero(free)
        known = -np.asarray(current["terminal"], float)
        ode = matrix[:-10]
        target = -np.asarray(current["differential"], float)-ode[:, end_indices]@known
        full = ode[:, free].tocsc()
        row_scale = 1/np.maximum(1.e-30, np.asarray(abs(full).max(axis=1).toarray()).ravel())
        row_equilibrated = (diags(row_scale)@full).tocsc()
        column_scale = 1/np.maximum(1.e-30,
            np.asarray(abs(row_equilibrated).max(axis=0).toarray()).ravel())
        cache = {"matrix":matrix, "free":free, "free_indices":free_indices,
            "end_indices":end_indices, "known":known, "row_scale":row_scale,
            "row_equilibrated":row_equilibrated, "scaled_target":row_scale*target,
            "column_scale":column_scale, "lu_direction":None, "lu_error":None,
            "direction_requests":0, "paid_LU_report":None,
            "row_scale_range":[float(row_scale.min()), float(row_scale.max())],
            "LU_column_scale_range":[float(column_scale.min()), float(column_scale.max())]}
        self.latest_linear_attempt_report = {"phase":"prepare_complete_original_rows",
            "coordinate_order":mixed.COORDINATE_ORDER,
            "row_scale_range":cache["row_scale_range"],
            "LU_column_scale_range":cache["LU_column_scale_range"],
            "complete_original_rows":True, "all_ten_linear_end_rows_paid":True}
        if self.paid_linear_report is not None:
            inherited = self.paid_linear_report["LU_original_direction"]
            size = inherited["unscaled_coordinate_direction_infinity_norm"]
            reset_fraction = float(min(1., self.initial_trust/max(1.e-30, size)))
            if reset_fraction<self.minimum_fraction:
                cache["paid_LU_report"] = {"same_original_state_LU_report":inherited,
                    "declared_new_initial_trust":self.initial_trust,
                    "inherited_direction_fraction_at_new_trust":reset_fraction,
                    "same_state_LU_factor_not_replayed":True,
                    "choice_is_numerical_globalization_not_a_new_matrix_certificate":True}
                self.paid_LU_direction_skips += 1
                self.latest_linear_attempt_report.update(phase="consumed_paid_unusable_LU_report",
                                                          paid_LU_report=cache["paid_LU_report"])
            self.paid_linear_report = None
        if cache["paid_LU_report"] is None:
            self.clock.check("before_new_state_original_mixed_LU")
            lu_start = time.monotonic()
            self.linear_attempts += 1
            self.lu_attempts += 1
            try:
                factor = splu((row_equilibrated@diags(column_scale)).tocsc())
                solution = factor.solve(cache["scaled_target"])
                direction = np.zeros(self.size)
                direction[free] = column_scale*solution
                direction[end_indices] = known
                if not np.all(np.isfinite(direction)):
                    raise FloatingPointError("The new-state original LU direction is nonfinite.")
                cache["lu_direction"] = direction
            except (RuntimeError, ValueError, FloatingPointError) as error:
                self.lu_failures += 1
                cache["lu_error"] = type(error).__name__+":"+str(error)
            finally:
                cache["lu_seconds"] = time.monotonic()-lu_start
                self.linear_seconds += cache["lu_seconds"]
            self.latest_linear_attempt_report.update(phase="completed_new_state_original_LU",
                seconds=cache["lu_seconds"], error=cache["lu_error"],
                unscaled_coordinate_direction_infinity_norm=None if cache["lu_direction"] is None
                    else float(np.max(np.abs(cache["lu_direction"]))),
                trust_prediction_not_yet_requested=True)
            self.clock.check("after_new_state_original_mixed_LU")
        cache["preparation_seconds"] = time.monotonic()-started
        self.clock.check("after_feasible_original_linear_cache")
        return cache

    def feasible_prediction(self, current, cache, direction, trust, args):
        raw = self.direction_prediction(current, cache["matrix"], direction,
                                        trust, args.minimum_usable_fraction)
        if direction is None:
            return raw
        length = LD(current["parameters"][-1])
        increment = LD(direction[-1])
        if increment<0:
            boundary, maximum = "lower", float((length-LD('2.1'))/-increment)
        elif increment>0:
            boundary, maximum = "upper", float((LD('7.9')-length)/increment)
        else:
            boundary, maximum = None, None
        nonfinite_maximum = maximum is not None and not np.isfinite(maximum)
        if nonfinite_maximum:
            maximum = None
        fraction = raw["trust_fraction"]
        limited = maximum is not None and args.length_boundary_fraction*maximum<fraction
        if limited:
            fraction = max(0., args.length_boundary_fraction*maximum)
        size = raw["unscaled_coordinate_direction_infinity_norm"]
        actual = (self.direction_prediction(current, cache["matrix"], direction,
            fraction*max(1.e-30, size), args.minimum_usable_fraction) if limited else dict(raw))
        actual.update({"requested_trust":trust, "unrestricted_prediction":raw,
            "exact_original_length_before":float(length), "original_length_increment":float(increment),
            "original_length_box":[2.1, 7.9], "boundary_towards_which_direction_points":boundary,
            "maximum_length_feasible_fraction":maximum,
            "maximum_length_fraction_exceeds_finite_float_range":bool(nonfinite_maximum),
            "length_boundary_safety_fraction":args.length_boundary_fraction,
            "length_boundary_limits_fraction":bool(limited),
            "length_boundary_blocks_otherwise_usable_direction":
                bool(limited and raw["usable"] and not actual["usable"]),
            "length_was_snapped_or_changed_before_direction":False})
        return actual

    def lsmr_direction(self, current, cache, trust, regularization, args, report,
                       attempt, hold_length):
        label = "fixed_length_increment" if hold_length else "free_length_increment"
        indices = cache["free_indices"]
        if hold_length:
            column_mask = indices!=self.size-1
            indices = indices[column_mask]
            matrix = cache["row_equilibrated"][:, column_mask]
        else:
            matrix = cache["row_equilibrated"]
        report["last_attempted_damping"] = regularization
        report["inflight_LSMR"] = {"attempt":attempt, "regularization_lambda":regularization,
            "length_mode":label, "phase":"before_solve", "matrix_shape":list(matrix.shape)}
        self.clock.check("before_original_"+label+"_LSMR")
        started = time.monotonic()
        self.linear_attempts += 1
        self.lsmr_attempts += 1
        if hold_length:
            self.fixed_length_lsmr_attempts += 1
        else:
            self.unconstrained_lsmr_attempts += 1
        report["inflight_LSMR"]["phase"] = "solving_all_original_rows"
        result, error_text = None, None
        try:
            result = lsmr(matrix, cache["scaled_target"], damp=np.sqrt(regularization),
                          atol=1.e-11, btol=1.e-11, conlim=1.e12, maxiter=args.lsmr_maxiter)
            direction = np.zeros(self.size)
            direction[indices] = result[0]
            direction[cache["end_indices"]] = cache["known"]
            if not np.all(np.isfinite(direction)):
                raise FloatingPointError("The complete original-row feasible direction is nonfinite.")
        except (RuntimeError, ValueError, FloatingPointError) as error:
            direction = None
            error_text = type(error).__name__+":"+str(error)
        finally:
            seconds = time.monotonic()-started
            self.linear_seconds += seconds
            if result is not None:
                self.linear_lsmr_iterations += int(result[2])
        prediction = self.feasible_prediction(current, cache, direction, trust, args)
        attempt_record = {"attempt":attempt, "regularization_lambda":regularization,
            "length_mode":label, "matrix_shape":list(matrix.shape), "seconds":seconds,
            "error":error_text, "prediction":prediction,
            "all_original_rows_present":True, "all_ten_linear_end_rows_paid":True,
            "original_length_increment_fixed_to_zero":bool(hold_length),
            "exact_actual_length_held":float(current["parameters"][-1]) if hold_length else None,
            "penalty":"Euclidean increment on the original remaining mixed coordinates"}
        if result is not None:
            estimates = dict(zip(("residual_norm_estimate", "normal_residual_norm_estimate",
                "matrix_norm_estimate", "condition_estimate", "solution_norm"),
                [float(value) for value in result[3:8]]))
            nonfinite = [key for key, value in estimates.items() if not np.isfinite(value)]
            attempt_record.update(istop=int(result[1]), iterations=int(result[2]),
                **{key:(None if key in nonfinite else value) for key, value in estimates.items()},
                nonfinite_estimate_fields=nonfinite, estimates_are_not_strict_bounds=True)
        report["new_LSMR_attempts"].append(attempt_record)
        report.pop("inflight_LSMR", None)
        self.clock.check("after_original_"+label+"_LSMR")
        return direction, prediction

    def choose_direction(self, current, cache, trust, damping, args):
        self.clock.check("before_same_box_feasible_original_direction")
        cache["direction_requests"] += 1
        if cache["direction_requests"]>1:
            self.lu_cache_reuses += 1
        lu_prediction = (None if cache["paid_LU_report"] is not None else
                         self.feasible_prediction(current, cache, cache["lu_direction"], trust, args))
        report = {"coordinate_order":mixed.COORDINATE_ORDER,
            "fixed_original_gauge_unit":mixed.GAUGE_UNIT_TEXT,
            "LU_original_direction":lu_prediction, "LU_error":cache["lu_error"],
            "paid_LU_unusable_report_consumed":cache["paid_LU_report"],
            "LU_direction_reused_at_same_state":cache["direction_requests"]>1,
            "row_scale_range":cache["row_scale_range"], "LU_column_scale_range":cache["LU_column_scale_range"],
            "exact_original_length_before":float(current["parameters"][-1]),
            "minimum_usable_LU_or_LSMR_fraction":args.minimum_usable_fraction,
            "new_LSMR_attempts":[], "length_activation_triggers":[],
            "fresh_unconstrained_direction_always_allows_length_release":True,
            "selected":None, "selected_damping":damping}
        self.latest_linear_attempt_report = report
        if lu_prediction is not None and lu_prediction["usable"]:
            report.update(selected="full_original_feasible_length_LU", selected_prediction=lu_prediction,
                          selected_length_increment_fixed_to_zero=False)
            self.free_length_direction_selections += 1
            return cache["lu_direction"], report
        lu_blocked = (lu_prediction is not None and
                      lu_prediction.get("length_boundary_blocks_otherwise_usable_direction", False))
        for attempt in range(args.lsmr_attempts):
            regularization = max(1.e-12, damping)*10.**attempt
            direction, prediction = self.lsmr_direction(current, cache, trust, regularization,
                                                        args, report, attempt, False)
            if prediction["usable"]:
                report.update(selected="full_original_feasible_free_length_LSMR",
                    selected_damping=regularization, selected_prediction=prediction,
                    selected_length_increment_fixed_to_zero=False)
                self.free_length_direction_selections += 1
                return direction, report
            blocked = prediction.get("length_boundary_blocks_otherwise_usable_direction", False)
            if blocked or lu_blocked:
                trigger = {"attempt":attempt,
                    "source":"actual_full_row_LSMR_direction" if blocked else "actual_full_original_LU_direction",
                    "original_direction_prediction":prediction if blocked else lu_prediction,
                    "action":"hold_delta_L_exactly_zero_in_same_full_original_rows",
                    "same_original_length_value":float(current["parameters"][-1])}
                report["length_activation_triggers"].append(trigger)
                self.length_boundary_activation_requests += 1
                active_direction, active_prediction = self.lsmr_direction(current, cache, trust,
                    regularization, args, report, attempt, True)
                if active_prediction["usable"]:
                    report.update(selected="full_original_fixed_length_increment_LSMR",
                        selected_damping=regularization, selected_prediction=active_prediction,
                        selected_length_increment_fixed_to_zero=True)
                    self.fixed_length_direction_selections += 1
                    return active_direction, report
        return None, report


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
    parser.add_argument("--damping", type=float, default=1.234567901234568e-5)
    parser.add_argument("--length-boundary-fraction", type=float, default=.95)
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
        emit("R625_LENGTH_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_LENGTH_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
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
        system = FeasibleLengthFullFeedback(x, coefficients, potential, clock, chart_factory,
            paid_linear_report=source["final"]["latest_complete_linear_report"],
            initial_trust=args.trust, minimum_fraction=args.minimum_usable_fraction)
        systems.append(system)
        emit("R625_NEW_LENGTH_GLOBALIZATION", {
            "actual_previous_trust":source_progress["actual_previous_trust"],
            "actual_previous_damping":source_progress["actual_previous_damping"],
            "declared_new_initial_trust":args.trust,
            "declared_initial_damping_inherits_actual_previous_value":args.damping,
            "old_backend_natural_path_restore_claim":False,
            "original_length_unchanged":float(chart_factory.initial_parameters[-1]),
            "unconstrained_direction_retested_at_each_new_state_for_release":True,
            "all_original_physical_boxes_and_all_original_rows_preserved":True})
        current, actual, summary = previous.solve(system, states, chart_factory.initial_parameters,
            histories, grid, args, retained, paid_entry=source)
        summaries.append(summary)
        status = summary["status"]
        refined_result = None
        if retained["fixed_refinement"]["state"]!="completed":
            refined_result = old.fixed_curve_refinement(retained, histories, args, clock)
        if old.collocation_converged(current, args) and refined_result is not None:
            clock.check("before_conditional_second_original_mixed_BVP_mesh")
            fine_x, fine_grid, refined = refined_result
            emit("R625_LENGTH_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = FeasibleLengthFullFeedback(fine_x, coefficients, potential, clock, chart_factory)
            systems.append(system2)
            current, actual, summary = previous.solve(system2, refined["states_at_observations"],
                current["parameters"], histories, fine_grid, args, retained, level=1)
            summaries.append(summary)
            status = summary["status"]
            old.fixed_curve_refinement(retained, histories, args, clock)
    except ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_last_original_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "feasible_length_continuation_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_FEASIBLE_LENGTH_EXCEPTION", exception)
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
        "paid_same_state_LU_replays_avoided":sum(system.paid_LU_direction_skips for system in systems),
        "unconstrained_length_LSMR_attempts":sum(system.unconstrained_lsmr_attempts for system in systems),
        "fixed_length_increment_LSMR_attempts":sum(system.fixed_length_lsmr_attempts for system in systems),
        "free_length_direction_selections":sum(system.free_length_direction_selections for system in systems),
        "fixed_length_direction_selections":sum(system.fixed_length_direction_selections for system in systems),
        "length_boundary_activation_requests":sum(system.length_boundary_activation_requests for system in systems),
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
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_FEASIBLE_LENGTH_CONTINUATION_FINAL", final)


if __name__ == "__main__":
    main()
