#!/usr/bin/env python3
"""One full62 SLSQP session and compact original-return capture.

Import-only; every value/J/backend operation is charged by the external public
Actions scope.  This source contains no CLI, development checks or test suite.
"""
from __future__ import annotations
import copy
import math
import resource
import time
import numpy as np

from frame_metric_current168_full62_whole_suffix import (
    POLICY, Full62WholeSuffixModel, WholeSuffixLimit, NORM_WEIGHT,
    MAX_EVALUATIONS, MAX_BACKEND_EVALUATIONS, SOLVER_SECONDS, SLSQP_OPTIONS,
    LP_ROW_TOLERANCE, _require, _error, _wall, _finite, _same, _vector,
    _raw_numeric, _raw_all_fields, _public, _compact, _array_receipt, array_binding)

class _EvaluationCache:
    def __init__(self, model, wall, started, seconds, maximum_physical, maximum_backend, sink):
        self.model, self.wall, self.started, self.seconds = model, wall, started, seconds
        self.maximum_physical, self.maximum_backend, self.sink = maximum_physical, maximum_backend, sink
        self.entries = {}; self.backend_inputs = {}; self.physical_inputs = set()
        self.counts = {"started": 0, "completed": 0, "failed": 0, "cache_hits": 0}
        self.backend_counts = {"distinct_inputs": 0, "callback_visits": 0, "repeat_visits": 0}
        self.callbacks = {"objective": 0, "objective_J": 0, "constraint_value": 0,
            "constraint_J": 0, "iteration": 0, "initial_value": 0, "initial_J": 0, "returned_vector": 0}
        sink["backend_input_records"] = []; sink["evaluation_records"] = []; sink["iteration_records"] = []

    def check(self, phase):
        _wall(self.wall, POLICY+".solver."+phase)
        elapsed = time.monotonic()-self.started
        if elapsed >= self.seconds:
            raise WholeSuffixLimit("the one new full62 solver clock exhausted: %.17g seconds" % elapsed)

    def touch(self, x, role):
        self.callbacks[role] = self.callbacks.get(role, 0)+1
        self.sink["callback_counts"] = copy.deepcopy(self.callbacks)
        vector = _finite(x, (64,), "literal backend64 callback")
        self.sink["_last_backend_input"] = vector.copy()
        self.check(role)
        key = vector.tobytes()
        self.backend_counts["callback_visits"] += 1
        if key not in self.backend_inputs:
            if len(self.backend_inputs) >= self.maximum_backend:
                self.sink["backend_input_counts"] = copy.deepcopy(self.backend_counts)
                raise WholeSuffixLimit("the declared distinct backend64-input ceiling is exhausted")
            ordinal = len(self.backend_inputs)+1
            self.backend_inputs[key] = ordinal
            self.backend_counts["distinct_inputs"] = ordinal
            self.sink["backend_input_records"].append({"ordinal": ordinal, "first_role": role,
                "backend64_binding": array_binding(vector), "K": float(vector[62]), "h": float(vector[63]),
                "elapsed_seconds": time.monotonic()-self.started})
        else:
            self.backend_counts["repeat_visits"] += 1
        self.sink["backend_input_counts"] = copy.deepcopy(self.backend_counts)
        return vector

    def get(self, x, role):
        vector = self.touch(x, role); key = vector.tobytes()
        if key in self.entries:
            self.counts["cache_hits"] += 1
            entry = self.entries[key]
            self.model.last_entry = entry
            self.sink["_last_complete_evaluation"] = entry
            self.sink["value_evaluation_counts"] = copy.deepcopy(self.counts)
            return entry
        q = self.model.point_from_backend(vector)
        qkey = q.tobytes()
        requires_new_geometry = qkey != self.model.loaded_geometry_key and not _same(q, self.model.ring_candidate168)
        distinct_new_point = requires_new_geometry and qkey not in self.model.seen_geometry_keys
        if distinct_new_point and self.model.full_point_counts["distinct_new_physical_points"] >= self.maximum_physical:
            raise WholeSuffixLimit("the declared distinct new physical q168-point ceiling is exhausted")
        self.physical_inputs.add(qkey)
        self.sink["distinct_actual_q168_inputs"] = len(self.physical_inputs)
        self.counts["started"] += 1; ordinal = self.counts["started"]
        record = {"ordinal": ordinal, "first_role": role, "status": "entered",
            "backend_input_ordinal": self.backend_inputs[key],
            "backend64_binding": array_binding(vector), "state168_binding": array_binding(q),
            "K": float(vector[62]), "h": float(vector[63]),
            "requires_geometric_execution": bool(requires_new_geometry),
            "is_distinct_new_physical_point": bool(distinct_new_point)}
        self.sink["evaluation_records"].append(record)
        self.sink["value_evaluation_counts"] = copy.deepcopy(self.counts)
        tick = time.monotonic()
        try:
            entry = self.model._value(vector, self.sink, state168=q); entry["ordinal"] = ordinal
            self.entries[key] = entry; self.model.last_entry = entry
            self.counts["completed"] += 1
            self.sink["_last_complete_evaluation"] = entry
            record.update(status="complete", whole_suffix_pass=entry["whole_suffix_pass"],
                summaries=copy.deepcopy(entry["summaries"]), constraint_values_binding=array_binding(entry["values"]),
                objective_K_plus_weight_h=float(vector[62]+NORM_WEIGHT*vector[63]))
            self.check("value-complete")
            return entry
        except Exception as error:
            record["error"] = _error(error)
            if record["status"] == "complete":
                record["complete_values_retained_before_post_call_stop"] = True
            else:
                record["status"] = "raised"; self.counts["failed"] += 1
            raise
        finally:
            record["seconds"] = time.monotonic()-tick
            self.sink["value_evaluation_counts"] = copy.deepcopy(self.counts)

    def jacobian(self, entry, role):
        self.callbacks[role] = self.callbacks.get(role, 0)+1
        self.sink["callback_counts"] = copy.deepcopy(self.callbacks)
        self.check(role)
        J = self.model._jacobian(entry, self.sink)
        self.sink["_last_complete_J"] = {"backend64": entry["backend"], "value_ordinal": entry["ordinal"], "matrix": J}
        self.check(role+"-complete")
        return J

    def initialize(self):
        entry = self.get(self.model.x0, "initial_value")
        self.model.initial_entry = entry
        self.sink["_initial_evaluation"] = entry
        self.sink["_initial_geometry"] = self.sink.get("_last_complete_geometry")
        J = self.jacobian(entry, "initial_J")
        self.sink["_initial_J"] = J
        scales = np.maximum(1., np.maximum(abs(entry["values"]), np.max(abs(J), axis=1)))
        scales = _finite(scales, (self.model.constraint_count,), "fixed initial row scales")
        self.model.row_scales = scales; self.sink["_fixed_row_scales"] = scales
        self.sink["fixed_row_scales"] = {"formula": "max(1,abs(initial value),max(abs(initial Jrow)))",
            "binding": array_binding(scales), "never_updated": True, "initial_value_ordinal": entry["ordinal"]}
        self.sink["initial_model_receipt"] = {"value_ordinal": entry["ordinal"],
            "actual_strict_metric_margin_was_evaluated_not_inferred_from_peak_location": True,
            "maximum_scaled_violation": float(max(0., -np.min(entry["values"]/scales))),
            "whole_suffix_pass": entry["whole_suffix_pass"], "summaries": copy.deepcopy(entry["summaries"])}
        self.check("initial-scales-complete")

    def objective(self, x):
        x = self.touch(x, "objective")
        return float(x[62]+NORM_WEIGHT*x[63])

    def objective_J(self, x):
        self.touch(x, "objective_J")
        result = np.zeros(64); result[62] = 1.; result[63] = NORM_WEIGHT
        return result

    def constraint_value(self, x):
        entry = self.get(x, "constraint_value")
        return entry["values"]/self.model.row_scales

    def constraint_J(self, x):
        entry = self.get(x, "constraint_J")
        J = self.jacobian(entry, "requested_analytic_J")
        return J/self.model.row_scales[:, None]

    def iteration(self, x):
        vector = self.touch(x, "iteration")
        entry = self.entries.get(vector.tobytes())
        self.sink["iteration_records"].append({"ordinal": len(self.sink["iteration_records"])+1,
            "backend64_binding": array_binding(vector),
            "K": float(vector[62]), "h": float(vector[63]),
            "objective_K_plus_weight_h": float(vector[62]+NORM_WEIGHT*vector[63]),
            "elapsed_seconds": time.monotonic()-self.started,
            "cached_value_ordinal": None if entry is None else entry["ordinal"],
            "cached_scaled_violation": None if entry is None else float(max(0., -np.min(entry["values"]/self.model.row_scales))),
            "no_new_scientific_evaluation_in_iteration_callback": True})


def _solver_public(sink):
    result = _public(sink)
    raw = result.pop("original_backend_return", None)
    result["original_backend_return_summary"] = None if raw is None else {key: copy.deepcopy(raw.get(key)) for key in
        ("status", "success", "message", "nit", "nfev", "njev", "backend_elapsed_seconds", "actual_finite_raw64_saved", "raw_K", "raw_h")}
    result["unemitted_original_backend_return"] = raw if sink.get("original_result_stdout_receipt") is None else None
    result.pop("evaluation_records", None); result.pop("iteration_records", None)
    result.pop("component_events", None); result.pop("backend_input_records", None)
    result["all_evaluation_iteration_and_partial_records_are_in_caller_SOLVE_TRACE"] = True
    return _compact(result)


def solve_full62_whole_suffix_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_seconds=SOLVER_SECONDS, maxiter=320, max_evaluations=MAX_EVALUATIONS,
        max_backend_evaluations=MAX_BACKEND_EVALUATIONS):
    """Exactly one new minimax call; emit only the actual original backend result."""
    _require(isinstance(model, Full62WholeSuffixModel) and model.status == "ready" and not model.solve_attempted,
             "one ready unattempted new whole-suffix model required")
    _require(callable(wall) and callable(charge_solve) and (emit is None or callable(emit)), "external clock/charge/emitter required")
    _require(type(maxiter) is int and 0 < maxiter <= SLSQP_OPTIONS["maxiter"]
             and type(max_evaluations) is int and 0 < max_evaluations <= MAX_EVALUATIONS
             and type(max_backend_evaluations) is int and 0 < max_backend_evaluations <= MAX_BACKEND_EVALUATIONS,
             "new physical/backend/iteration caps may only be reduced")
    seconds = float(solver_seconds)
    _require(not isinstance(solver_seconds, (bool, np.bool_)) and math.isfinite(seconds) and 0 < seconds <= SOLVER_SECONDS,
             "finite solver limit at most1200 seconds required")
    sink = {} if capture is None else capture
    _require(isinstance(sink, dict) and not sink, "empty one-solver capture required")
    sink.update(schema=POLICY+"-one-solver-attempt", status="entered", model_binding_sha256=model.binding_sha256,
        backend_entered=False, charged=False, qualified_candidate=False, original_backend_return=None,
        original_result_stdout_receipt=None, options={"maxiter": maxiter, "ftol": SLSQP_OPTIONS["ftol"], "disp": False},
        maximum_new_physical_points=max_evaluations,
        maximum_distinct_backend64_inputs=max_backend_evaluations, solver_seconds_limit=seconds,
        physical_point_cap_counts="distinct actual q168 needing new geometry; paid q_R hits separate",
        backend_cap_counts="every distinct literal backend64 input at any callback, including K/h changes",
        one_new_problem_not_a_restart_of_closed_full51_whole34_or_older_scopes=True,
        no_unreturned_intermediate_callback_candidate_promoted=True)
    model.solve_attempted = True; model.solver_sink = sink
    started = time.monotonic(); cache = None; candidate = None; candidate_record = None; raw_vector = None
    try:
        model.assert_context()
        sink["charge_receipt"] = copy.deepcopy(charge_solve({"schema": POLICY+"-solve-charge",
            "backend": "scipy.optimize.minimize(method='SLSQP')", "backend_variables": 64,
            "backend_order": "z62,K,h", "objective": "K+1e-6*h", "model_binding_sha256": model.binding_sha256,
            "whole_suffix_radial_rows": 21, "complete_angular_counts": [384, 768],
            "constraint_count": model.constraint_count, "options": copy.deepcopy(sink["options"]),
            "maximum_new_physical_points": max_evaluations, "solver_seconds": seconds,
            "maximum_distinct_backend64_inputs": max_backend_evaluations,
            "physical_point_cap_counts": sink["physical_point_cap_counts"],
            "backend_cap_counts": sink["backend_cap_counts"],
            "new_geometric_J_only_when_requested_including_initial_scaling_request": True}))
        sink["charged"] = True
        cache = _EvaluationCache(model, wall, started, seconds, max_evaluations, max_backend_evaluations, sink)
        cache.check("before-import")
        import scipy
        from scipy.optimize import minimize
        sink["scipy_version"] = str(scipy.__version__)
        cache.check("after-import")
        cache.initialize()
        bounds = list(model.backend_z_bounds)+[(model.target_lower, 58.), (0., model.maximum_h_float)]
        sink["backend_bounds"] = [list(v) for v in bounds]
        cache.check("before-backend")
        backend_started = time.monotonic(); sink.update(status="backend-entered", backend_entered=True)
        result = minimize(cache.objective, model.x0.copy(), method="SLSQP", jac=cache.objective_J, bounds=bounds,
            constraints=[{"type": "ineq", "fun": cache.constraint_value, "jac": cache.constraint_J}],
            callback=cache.iteration, options=copy.deepcopy(sink["options"]))
        backend_elapsed = time.monotonic()-backend_started
        # Capture the complete real return before any decode, gate, clock, or external decision.
        sink["_original_return_object"] = result
        returned = result.get("x")
        raw = {"schema": POLICY+"-original-nonlinear-backend-return",
            "backend": "scipy.optimize.minimize(method='SLSQP')", "scipy_version": str(scipy.__version__),
            "model_binding_sha256": model.binding_sha256, "backend_variable_order": "z62,K,h",
            "actual_raw_backend64": None if returned is None else _raw_numeric(returned),
            "entire_OptimizeResult_fields": _raw_all_fields(dict(result)),
            "status": None if result.get("status") is None else int(result.get("status")),
            "success": bool(result.get("success", False)), "message": str(result.get("message", "")),
            "nit": None if result.get("nit") is None else int(result.get("nit")),
            "nfev": None if result.get("nfev") is None else int(result.get("nfev")),
            "njev": None if result.get("njev") is None else int(result.get("njev")),
            "backend_elapsed_seconds": float(backend_elapsed), "raw_return_captured_before_filter": True,
            "returned_multipliers_are_internal_QP_approximations_not_strict_certificates": True,
            "unreturned_fields_not_fabricated": True}
        sink["original_backend_return"] = raw
        sink.update(status="backend-returned", backend_elapsed_seconds=float(backend_elapsed))
        finite = False
        if returned is not None:
            vector = np.asarray(returned, dtype=np.float64)
            finite = bool(vector.shape == (64,) and np.all(np.isfinite(vector)))
            if finite:
                raw_vector = _vector(vector)
                raw["raw_K"], raw["raw_h"] = float(vector[62]), float(vector[63])
        raw["actual_finite_raw64_saved"] = bool(finite and raw["actual_raw_backend64"] is not None
            and raw["actual_raw_backend64"].get("shape") == [64]
            and len(raw["actual_raw_backend64"].get("exact_binary64_flat", [])) == 64)
        if not finite:
            raw["raw_K"], raw["raw_h"] = None, None
        decode_error = None
        if finite:
            try:
                proposed, candidate_record = model.point_from_backend(vector, include_record=True)
                sink["returned_candidate_record"] = copy.deepcopy(candidate_record)
                sink["_returned_candidate168"] = proposed
            except Exception as error:
                decode_error = error
                sink["returned_point_decode_error"] = _error(error)
        if emit is not None:
            tick = time.monotonic()
            try:
                sink["original_result_stdout_receipt"] = copy.deepcopy(emit("NONLINEAR_RESULT", copy.deepcopy(raw)))
            except Exception as error:
                sink["raw_result_reporting_error"] = _error(error)
                raise
            finally:
                sink["raw_result_emit_seconds"] = time.monotonic()-tick
        if decode_error is not None:
            raise decode_error
        cache.check("after-original-return-and-decoded-point-saved")
        eligible = bool(finite and raw["success"] and raw["status"] == 0)
        sink["backend_status_eligible"] = eligible
        if not eligible:
            sink["status"] = "no-qualified-backend-return"
        else:
            entry = cache.get(vector, "returned_vector")
            # Qualification uses this exact cached backend value; no evicted geometry is rebuilt for reporting.
            nonlinear_violation = float(max(0., -np.min(entry["values"][:model.nonlinear_constraint_count]/model.row_scales[:model.nonlinear_constraint_count])))
            scaled_violation = float(max(0., -np.min(entry["values"]/model.row_scales)))
            linear_violation = float(max(0., -np.min(entry["values"][model.nonlinear_constraint_count:])))
            passed = bool(scaled_violation <= SLSQP_OPTIONS["ftol"] and linear_violation <= LP_ROW_TOLERANCE
                          and candidate_record["original_box_and_K_h_pass"]
                          and candidate_record["rounded_physical_norm_le_raw_h_exact_pass"]
                          and entry["whole_suffix_pass"])
            sink["candidate_filter"] = {"returned_value_ordinal": entry["ordinal"],
                "maximum_scaled_model_violation": scaled_violation, "maximum_scaled_nonlinear_violation": nonlinear_violation,
                "scaled_model_tolerance": SLSQP_OPTIONS["ftol"],
                "maximum_unscaled_original_linear_violation": linear_violation, "original_linear_tolerance": LP_ROW_TOLERANCE,
                "original_linear_pass": bool(linear_violation <= LP_ROW_TOLERANCE),
                "exact_box_K_h_pass": bool(candidate_record["original_box_and_K_h_pass"]),
                "backend_norm_epigraph_exact_pass": bool(candidate_record["backend_norm_epigraph_exact_pass"]),
                "rounded_physical_norm_le_raw_h_exact_pass": bool(candidate_record["rounded_physical_norm_le_raw_h_exact_pass"]),
                "whole_suffix_unsmoothed_and_unsquared_pass": bool(entry["whole_suffix_pass"]),
                "whole_suffix_summaries": copy.deepcopy(entry["summaries"]), "qualified": passed,
                "wholebody_canonical_prediction_and_actual14_remain_external": True}
            if passed:
                candidate = proposed
                sink.update(status="qualified-whole-suffix-return-needs-canonical-wholebody-prediction", qualified_candidate=True)
            else:
                sink["status"] = "returned-vector-fails-whole-suffix-or-original-exact-box"
        cache.check("complete")
        model.status = sink["status"]
    except WholeSuffixLimit as error:
        sink.update(status="stopped-at-declared-new-solver-limit", error=_error(error), stop_reason=str(error),
                    qualified_candidate=False, no_backend_status_relabelled=True)
        model.status = sink["status"]; candidate = None
    except Exception as error:
        sink.update(status="raised", error=_error(error), qualified_candidate=False,
                    complete_and_partial_scientific_work_retained=True)
        model.status = "solver-raised"; candidate = None
        raise
    finally:
        model.temporary.close()
        sink["local_elapsed_seconds"] = time.monotonic()-started
        sink["observed_nonpreemptive_solver_clock_overrun_seconds"] = max(0., sink["local_elapsed_seconds"]-seconds)
        sink["nonpreemptive_clock_checks_not_a_strict_backend_wall_guarantee"] = True
        sink["new_geometry_counts"] = copy.deepcopy(model.full_point_counts)
        sink["new_J_counts"] = copy.deepcopy(model.jacobian_counts)
        sink["K_independent_derivative_input_counts"] = copy.deepcopy(model.derivative_input_counts)
        sink["temporary_cache_receipt"] = copy.deepcopy(model.build_sink.get("temporary_cache"))
        sink["maximum_process_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if cache is not None:
            sink["value_evaluation_counts"] = copy.deepcopy(cache.counts)
            sink["backend_input_counts"] = copy.deepcopy(cache.backend_counts)
            sink["distinct_actual_q168_inputs"] = len(cache.physical_inputs)
            sink["callback_counts"] = copy.deepcopy(cache.callbacks)
            sink["cached_complete_literal_backend_inputs"] = len(cache.entries)
        record = sink.get("returned_candidate_record")
        sink["actual_returned_candidate168_saved"] = bool(isinstance(record, dict)
            and len(record.get("rounded_independent168", {}).get("values", [])) == 168
            and len(record.get("rounded_independent168", {}).get("exact_binary64", [])) == 168)
        sink["actual_returned_physical172_saved"] = bool(isinstance(record, dict)
            and len(record.get("rounded_physical172_exact", [])) == 172)
    raw = sink.get("original_backend_return")
    return {"status": sink["status"], "qualified": bool(sink["qualified_candidate"]),
        "qualified_candidate": bool(sink["qualified_candidate"]), "candidate168": candidate,
        "candidate": candidate, "candidate_record": copy.deepcopy(candidate_record),
        "actual_backend_raw64": copy.deepcopy(raw_vector),
        "backend_success": None if raw is None else raw["success"],
        "backend_status": None if raw is None else raw["status"], "report": _solver_public(sink)}


def _entry_payload(entry):
    return {"value_ordinal": entry["ordinal"], "backend64_binding": array_binding(entry["backend"]),
        "state168_binding": array_binding(entry["state168"]),
        "original_constraint_values_binding": _array_receipt(entry["values"]),
        "whole_suffix_summaries": copy.deepcopy(entry["summaries"]), "whole_suffix_pass": entry["whole_suffix_pass"]}


def full62_whole_suffix_capture_record(capture, *, include_arrays=False):
    """Compact true completion receipts only; never publish large scientific arrays."""
    _require(isinstance(capture, dict), "full62 capture dictionary required")
    result = _public(capture)
    if result.get("original_result_stdout_receipt") is not None:
        raw = result.pop("original_backend_return", None)
        result["emitted_original_backend_return_summary"] = None if raw is None else {key: copy.deepcopy(raw.get(key)) for key in
            ("status", "success", "message", "nit", "nfev", "njev", "actual_finite_raw64_saved", "backend_elapsed_seconds", "raw_K", "raw_h")}
    result = _compact(result)
    for private, public in (("_new_last3_radial", "completed_new_last3_radial_bindings"),
                            ("_new_linear_arrays", "completed_new_linear_array_bindings"),
                            ("_new_body_height_arrays", "completed_new_body_height_array_bindings"),
                            ("_fixed_row_scales", "actual_fixed_row_scale_binding"),
                            ("_new_backend_bounds", "original_box_backend_bounds")):
        if private in capture:
            result[public] = _compact(capture[private])
    for private, public in (("_last_backend_input", "actual_last_backend64"),
                            ("_returned_candidate168", "actual_returned_candidate168")):
        if private in capture:
            result[public] = _vector(capture[private])
    initial = capture.get("_initial_evaluation"); latest = capture.get("_last_complete_evaluation")
    if isinstance(initial, dict):
        result["actual_initial_evaluation"] = _entry_payload(initial)
    if isinstance(latest, dict):
        result["actual_last_evaluation"] = (
            {"receipt_reference": "actual_initial_evaluation", "same_value_ordinal": True}
            if initial is not None and latest["ordinal"] == initial["ordinal"] else _entry_payload(latest))
    first_geometry = capture.get("_initial_geometry"); last_geometry = capture.get("_last_complete_geometry")
    if isinstance(first_geometry, dict):
        result["actual_initial_geometry_bindings"] = _compact(first_geometry)
    if isinstance(last_geometry, dict):
        same = isinstance(first_geometry, dict) and _same(last_geometry["state168"], first_geometry["state168"])
        result["actual_last_geometry_bindings"] = (
            {"receipt_reference": "actual_initial_geometry_bindings", "same_actual_state": True}
            if same else _compact(last_geometry))
    first_J = capture.get("_initial_J"); last_J_record = capture.get("_last_complete_J")
    if isinstance(first_J, np.ndarray):
        result["actual_initial_analytic_J64_binding"] = _array_receipt(first_J)
    last_J = last_J_record.get("matrix") if isinstance(last_J_record, dict) else None
    if isinstance(last_J, np.ndarray):
        result["actual_last_analytic_J64_binding"] = {
            "backend64_binding": array_binding(last_J_record["backend64"]),
            "value_ordinal": last_J_record["value_ordinal"], "matrix_binding": _array_receipt(last_J)}
    partial = capture.get("_last_geometry_partial")
    if isinstance(partial, dict) and partial.get("status") != "complete":
        result["actual_incomplete_geometry_bindings"] = _compact(partial)
    partial_J = capture.get("_last_jacobian_partial")
    if isinstance(partial_J, dict):
        metadata = _compact({key: value for key, value in partial_J.items() if key != "matrix"})
        matrix = partial_J.get("matrix")
        if isinstance(matrix, np.ndarray):
            if partial_J.get("status") == "complete":
                metadata["complete_matrix_binding"] = _array_receipt(matrix)
            else:
                metadata["matrix_layout"] = {"shape": list(matrix.shape), "dtype": str(matrix.dtype),
                    "unfilled_values_not_hashed_or_emitted": True}
                metadata["actually_completed_column_bindings"] = []
                for block in partial_J.get("completed_column_blocks", []):
                    values = matrix[block["row_start"]:block["row_stop"], block["column_start"]:block["column_stop"]]
                    metadata["actually_completed_column_bindings"].append({
                        **copy.deepcopy(block), "binding": _array_receipt(values)})
        result["last_J_completion_or_partial_receipt"] = metadata
    result["large_scientific_arrays_emitted"] = False
    result["legacy_include_arrays_argument_does_not_publish_large_values"] = bool(include_arrays)
    result["unfilled_values_are_not_hashed_filled_or_recomputed"] = True
    result["new_array_bindings_are_not_future_free_scientific_inputs"] = True
    result["temporary_intermediate_cache_is_not_a_future_free_scientific_input"] = True
    return result
