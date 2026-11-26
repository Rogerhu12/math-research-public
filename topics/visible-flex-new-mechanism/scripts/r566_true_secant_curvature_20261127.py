#!/usr/bin/env python3
"""Actual same-Lagrangian secants across evidenced working-row exchanges.

This is a solver-initialization heuristic, not a physical certificate.  It
consumes the J already requested by the original SLSQP Python wrapper, and the
actual QP multipliers/LDL in that same invocation.  It never evaluates an old
model, fabricates an unlogged H, or changes the external acceptance callback.
Scientific use is restricted to the declared public Actions.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict
import tempfile
import time

import numpy as np

import r566_build_seeded_slsqp_20261127 as native_build


SCHEMA = "r566-real-frozen-multiplier-native-initial-H-v1"
DIMENSION = 82
EIGENVALUE_FLOOR = 1.e-6
EIGENVALUE_CEILING = 1.e6
MAX_CHECKPOINT_BYTES = 512*1024


def canonical(value):
    """Typed parameter identity; floats retain their complete binary64 value."""
    if isinstance(value, dict):
        return {str(k): canonical(v) for k, v in sorted(value.items())}
    if isinstance(value, (list, tuple)):
        return [canonical(v) for v in value]
    if isinstance(value, np.ndarray):
        return canonical(value.tolist())
    if isinstance(value, (np.floating, float)):
        value = float(value)
        if not math.isfinite(value):
            raise ValueError("A semantic field parameter must be finite.")
        return {"binary64_hex": value.hex()}
    if isinstance(value, (np.integer, int)) and not isinstance(value, (bool, np.bool_)):
        return int(value)
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if value is None or isinstance(value, str):
        return value
    raise TypeError("Unbound semantic parameter type: "+type(value).__name__)


def json_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(json_bytes(value)).hexdigest()


def row_key(row):
    if row["field"] == "mean_E_floor":
        angle = ["ring_mean", 0]
    elif row["kind"] == "uniform":
        angle = ["uniform", int(row["angular_index"])]
    else:
        angle = ["actual", float(row["theta"]).hex()]
    return json_bytes([row["field"], float(row["s"]).hex(), angle]).decode()


def identity_packed(n):
    result = np.zeros(n*(n+1)//2, dtype=np.float64)
    offset = 0
    for column in range(n):
        result[offset] = 1.
        offset += n-column
    return result


def unpack_ldl(packed, n):
    """The original native column-packed unit-lower L, diagonal D convention."""
    packed = np.asarray(packed, dtype=np.float64)
    if packed.shape != (n*(n+1)//2,) or not np.all(np.isfinite(packed)):
        raise ValueError("Native LDL packing is not finite or has the wrong dimension.")
    lower = np.eye(n)
    diagonal = np.empty(n)
    offset = 0
    for column in range(n):
        diagonal[column] = packed[offset]
        lower[column+1:, column] = packed[offset+1:offset+n-column]
        offset += n-column
    if np.any(diagonal <= 0):
        raise ValueError("The actual native LDL has a nonpositive diagonal.")
    result = (lower*diagonal)@lower.T
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("Native finite factors overflowed as a physical-coordinate H.")
    return (result+result.T)/2


def pack_spd(matrix):
    """Numerical SPD seed packing; all matrix algebra is charged in Actions."""
    matrix = (np.asarray(matrix, dtype=np.float64)+np.asarray(matrix, dtype=np.float64).T)/2
    factor = np.linalg.cholesky(matrix)
    n = len(matrix)
    result = np.empty(n*(n+1)//2)
    offset = 0
    for column in range(n):
        result[offset] = factor[column, column]**2
        result[offset+1:offset+n-column] = factor[column+1:, column]/factor[column, column]
        offset += n-column
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("The prepared native LDL seed is nonfinite.")
    return result


class TrueSecantSLSQP:
    """A drop-in minimize endpoint for the unchanged 81q+e B030 caller.

    model_identity must name the complete bound field/model source and literal
    parameter recipe in the new request.  Actual phase, par, geo, FFT count and
    row identities are added here from the actual WorkingRows object.  The
    original minimize, its callback, every original constraint value/Jacobian
    and all original physical bounds are passed through unchanged.
    """
    def __init__(self, original_minimize, model_identity, emit, check_clock,
                 checkpoint=None):
        native_build.require_public_actions()
        self.original_minimize = original_minimize
        self.model_identity = canonical(model_identity)
        self.emit, self.check_clock = emit, check_clock
        self.signature = None
        self.packed = None
        self.pending = None
        self.native = self.directory = None
        self.native_build_receipt = {"started": False, "completed": False}
        self.last = {"reason": "first_scope_has_no_saved_native_H_or_multiplier"}
        self.counts = {"backend_calls": 0, "native_calls": 0,
            "native_seconds": 0., "seed_preparations": 0, "seed_seconds": 0.,
            "actual_QP_observations": 0, "frozen_multiplier_updates": 0,
            "damped_updates": 0, "skipped_updates": 0, "semantic_resets": 0,
            "native_gradient_updates_consumed_pending": 0,
            "eigenvalue_clipped_seeds": 0, "invalid_curvature_identity_resets": 0,
            "additional_model_value_evaluations": 0, "additional_model_Jacobians": 0}
        if checkpoint is not None:
            if (checkpoint.get("schema") != SCHEMA or checkpoint.get("dimension") != DIMENSION
                    or checkpoint.get("model_identity_sha256") != digest(self.model_identity)):
                raise ValueError("A supplied curvature checkpoint belongs to another model/protocol.")
            self.signature = checkpoint.get("row_function_signature")
            saved = checkpoint.get("actual_native_or_prepared_packed_LDL")
            self.packed = None if saved is None else np.asarray(saved, dtype=float)
            self.pending = checkpoint.get("pending_frozen_multiplier_secant")
            self.last = {"reason": "loaded_actual_declared_curvature_checkpoint",
                         "source_last": checkpoint.get("last")}
            # This is prior cost, never relabeled as work in the new run.
            self.prior_cost = {
                "source_curvature_checkpoint_sha256": digest(checkpoint),
                "source_curvature_cost_sha256": digest(checkpoint.get("cost")),
                "complete_source_terminal_ledger_must_retain_all_prior_cost": True}
        else:
            self.prior_cost = None

    def _signature(self, active):
        values = {"model_identity": self.model_identity,
                  "dimension": DIMENSION, "objective": "unchanged_physical_epigraph_e",
                  "phase": active.phase, "actual_parameters": canonical(asdict(active.par)),
                  "actual_geometry_thresholds": canonical(active.geo),
                  "actual_FFT_angles": int(active.batches[0][0].uniform.nt),
                  "actual_numpy_version": np.__version__,
                  "row_function": "original_minimum_of_same_four_orbit_values",
                  "parameter_order": "original_B030_81q_then_epigraph"}
        return digest(values)

    def _prepare(self, x, gradient, jacobian, keys, signature, deadline):
        started = time.monotonic()
        self.counts["seed_preparations"] += 1
        self.check_clock(deadline)
        report = {"same_original_J_already_paid": True,
                  "additional_model_values_or_Jacobians": 0,
                  "row_function_signature": signature,
                  "current_x_binary64_sha256": hashlib.sha256(np.asarray(x, float).tobytes()).hexdigest()}
        try:
            if self.signature is not None and self.signature != signature:
                self.packed, self.pending = None, None
                self.counts["semantic_resets"] += 1
                report["semantic_reset"] = "phase_objective_model_parameter_or_angle_semantics_changed"
            self.signature = signature
            if self.packed is None:
                self.pending = None
                report["reason"] = "original_identity_initialization_no_unlogged_H_restored"
                self.last = report
                return None
            try:
                matrix = unpack_ldl(self.packed, DIMENSION)
            except (ValueError, FloatingPointError):
                self.packed, self.pending = None, None
                self.counts["invalid_curvature_identity_resets"] += 1
                report["reason"] = "invalid_actual_factor_explicit_identity_reset"
                self.last = report
                return None

            pending = self.pending
            # Consumption is transactional: this exact secant is never applied
            # twice if the following native call or the scientific clock stops.
            self.pending = None
            if pending is None:
                report["secant"] = "no_pending_same_QP_data"
            else:
                index = {key: i for i, key in enumerate(keys)}
                missing = [item[0] for item in pending["nonzero_multipliers"] if item[0] not in index]
                if pending["row_function_signature"] != signature or missing:
                    self.counts["skipped_updates"] += 1
                    report["secant"] = "missing_old_nonzero_multiplier_row_or_changed_semantics"
                    report["missing_nonzero_multiplier_rows"] = missing
                else:
                    old_x = np.asarray(pending["actual_J_QP_anchor"], float)
                    old_weighted = np.asarray(pending["actual_fixed_multiplier_gradient"], float)
                    weighted = np.asarray(gradient, float).copy()
                    for key, multiplier in pending["nonzero_multipliers"]:
                        weighted -= float(multiplier)*jacobian[index[key]]
                    step = np.asarray(x, float)-old_x
                    difference = weighted-old_weighted
                    bs = matrix@step
                    h = float(step@bs)
                    sy = float(step@difference)
                    scale = max(1., float(np.max(np.abs(x))), float(np.max(np.abs(old_x))))
                    if (not np.all(np.isfinite(difference)) or not math.isfinite(h)
                            or not math.isfinite(sy) or h <= 0
                            or float(np.max(np.abs(step))) <= 16*np.finfo(float).eps*scale):
                        self.counts["skipped_updates"] += 1
                        report["secant"] = "zero_unresolved_or_nonfinite_actual_secant"
                    else:
                        theta = 1. if sy >= .2*h else .8*h/(h-sy)
                        r = theta*difference+(1.-theta)*bs
                        sr = float(step@r)
                        if not math.isfinite(sr) or sr <= 0:
                            self.counts["skipped_updates"] += 1
                            report["secant"] = "floating_damped_denominator_not_positive"
                        else:
                            proposed = matrix-np.outer(bs, bs)/h+np.outer(r, r)/sr
                            if np.all(np.isfinite(proposed)):
                                matrix = (proposed+proposed.T)/2
                                self.counts["frozen_multiplier_updates"] += 1
                                self.counts["damped_updates"] += int(theta != 1.)
                                report.update(secant="actual_frozen_multiplier_Powell_update",
                                    step_H_step=h, step_gradient_difference=sy,
                                    damping_theta=theta, step_damped_difference=sr,
                                    old_QP= pending["actual_QP_identity"],
                                    retained_nonzero_multipliers=len(pending["nonzero_multipliers"]))
                            else:
                                self.counts["skipped_updates"] += 1
                                report["secant"] = "nonfinite_update_retained_previous_finite_H"
            # This explicit spectral projection is an approximate-QP strategy,
            # never a statement that the physical Hessian has these bounds.
            eigenvalues, vectors = np.linalg.eigh(matrix)
            clipped = np.clip(eigenvalues, EIGENVALUE_FLOOR, EIGENVALUE_CEILING)
            clipped_any = bool(np.any(clipped != eigenvalues))
            self.counts["eigenvalue_clipped_seeds"] += int(clipped_any)
            report["approximate_eigenvalue_regularization"] = {
                "raw_minimum": float(eigenvalues[0]), "raw_maximum": float(eigenvalues[-1]),
                "floor": EIGENVALUE_FLOOR, "ceiling": EIGENVALUE_CEILING,
                "clipped": clipped_any}
            regularized = (vectors*clipped)@vectors.T
            self.packed = pack_spd(regularized)
            report["reason"] = "prepared_actual_positive_approximate_H_for_first_QP_only"
            report["prepared_LDL_binary64_sha256"] = hashlib.sha256(self.packed.tobytes()).hexdigest()
            self.last = report
            self.check_clock(deadline)
            return self.packed.copy()
        except np.linalg.LinAlgError as error:
            self.packed, self.pending = None, None
            self.counts["invalid_curvature_identity_resets"] += 1
            report.update(reason="explicit_numerical_factor_failure_identity_reset", error=str(error))
            self.last = report
            return None
        finally:
            seconds = time.monotonic()-started
            self.counts["seed_seconds"] += seconds
            report["seconds"] = seconds
            self.emit("R566_TRUE_SECANT_INITIAL_H", report)

    def _observe(self, state, buffer, multipliers, keys, signature, incoming_mode,
                 incoming_iteration, backend_number):
        n, m = int(state["n"]), int(state["m"])
        n2, n1 = n*(n+1)//2, n+1
        actual_packed = np.asarray(buffer[:n2], float).copy()
        diagonal, offset = [], 0
        for column in range(n):
            diagonal.append(offset)
            offset += n-column
        if (not np.all(np.isfinite(actual_packed))
                or np.any(actual_packed[diagonal] <= 0)):
            self.packed, self.pending = None, None
            self.counts["invalid_curvature_identity_resets"] += 1
            self.last = {"reason": "actual_native_factor_invalid_no_nonfinite_checkpoint",
                         "actual_factor_sha256": hashlib.sha256(actual_packed.tobytes()).hexdigest()}
            self.emit("R566_ACTUAL_QP_CURVATURE_UNAVAILABLE", self.last)
            return
        self.packed = actual_packed
        if incoming_mode == -1:
            # MODEM1 already used the previous native secant.  Never replay it
            # externally when the native solver actually had time to continue.
            self.pending = None
            self.counts["native_gradient_updates_consumed_pending"] += 1
        if int(state["iter"]) <= incoming_iteration:
            return
        self.pending = None
        if int(state["mode"]) not in (0, 1):
            return
        x0 = np.asarray(buffer[n2:n2+n], float)
        v_offset = n2+n+m+2*n1
        weighted = np.asarray(buffer[v_offset:v_offset+n], float)
        actual_multipliers = np.asarray(multipliers[:m], float)
        if (n != DIMENSION or len(keys) != m or not np.all(np.isfinite(x0))
                or not np.all(np.isfinite(weighted)) or not np.all(np.isfinite(actual_multipliers))):
            self.last = {"reason": "native_QP_observation_not_finite_pending_secant_not_created"}
            return
        nonzero = [[keys[i], float(value)] for i, value in enumerate(actual_multipliers) if value != 0.]
        identity = {"backend_number": backend_number, "native_major_iteration": int(state["iter"]),
                    "native_mode": int(state["mode"]), "native_reset_counter": int(state["reset"]),
                    "row_order_sha256": digest(keys),
                    "actual_J_QP_anchor_sha256": hashlib.sha256(x0.tobytes()).hexdigest()}
        self.pending = {"row_function_signature": signature,
            "actual_QP_identity": identity, "actual_J_QP_anchor": x0.tolist(),
            "actual_fixed_multiplier_gradient": weighted.tolist(),
            "nonzero_multipliers": nonzero,
            "zero_multipliers_omitted_exactly_without_threshold": True,
            "native_bounds_are_linear_and_have_zero_fixed_multiplier_secant": True}
        self.counts["actual_QP_observations"] += 1
        self.emit("R566_ACTUAL_QP_CURVATURE_STATE", {
            **identity, "native_packed_LDL_sha256": hashlib.sha256(self.packed.tobytes()).hexdigest(),
            "actual_nonzero_working_multipliers": len(nonzero),
            "callback_raw_trial_is_not_the_J_QP_anchor": True})

    def minimize(self, *args, **kwargs):
        native_build.require_public_actions()
        constraints = kwargs.get("constraints")
        if (kwargs.get("method") != "SLSQP" or not isinstance(constraints, dict)
                or constraints.get("type") != "ineq"):
            raise ValueError("This exact endpoint only wraps the original B030 inequality SLSQP call.")
        active = getattr(constraints.get("jac"), "__self__", None)
        if active is None or getattr(constraints.get("fun"), "__self__", None) is not active:
            raise ValueError("The exact same current WorkingRows object must supply values and J.")
        keys = [row_key(row) for row in active.rows]
        if len(keys) != len(set(keys)) or active.size+1 != DIMENSION:
            raise ValueError("The actual working rows or physical dimension differ from the declaration.")
        signature = self._signature(active)
        deadline = active.deadline
        self.check_clock(deadline)
        if self.native is None:
            self.directory = tempfile.TemporaryDirectory(prefix="r566_initial_H_")
            self.native = native_build.build(self.directory.name, deadline,
                                            self.native_build_receipt, self.emit)
        import scipy.optimize._slsqp_py as wrapper
        previous_native = wrapper.slsqp
        self.counts["backend_calls"] += 1
        backend_number = self.counts["backend_calls"]
        first_call = True

        def initialized_native(state, fx, gradient, jacobian, values, x, multipliers,
                               lower, upper, buffer, indices):
            nonlocal first_call
            self.check_clock(deadline)
            incoming_mode, incoming_iteration = int(state["mode"]), int(state["iter"])
            if first_call:
                if incoming_mode != 0 or int(state["n"]) != DIMENSION or int(state["m"]) != len(keys):
                    raise ValueError("Unexpected actual first native SLSQP state.")
                seed = self._prepare(x, gradient, jacobian, keys, signature, deadline)
                if seed is not None:
                    state["_r566_initial_ldl"] = seed
                first_call = False
            started = time.monotonic()
            self.counts["native_calls"] += 1
            try:
                self.native.slsqp(state, fx, gradient, jacobian, values, x, multipliers,
                                  lower, upper, buffer, indices)
                self._observe(state, buffer, multipliers, keys, signature,
                              incoming_mode, incoming_iteration, backend_number)
            finally:
                state.pop("_r566_initial_ldl", None)
                self.counts["native_seconds"] += time.monotonic()-started
            self.check_clock(deadline)

        wrapper.slsqp = initialized_native
        try:
            # Every original argument, original physical bounds, and the exact
            # original callback are forwarded without replacing their arrays.
            return self.original_minimize(*args, **kwargs)
        finally:
            wrapper.slsqp = previous_native

    def checkpoint(self):
        output = {"schema": SCHEMA, "dimension": DIMENSION,
            "model_identity_sha256": digest(self.model_identity),
            "row_function_signature": self.signature,
            "actual_native_or_prepared_packed_LDL": None if self.packed is None else self.packed.tolist(),
            "pending_frozen_multiplier_secant": self.pending, "last": self.last,
            "cost": {"current_scope": dict(self.counts), "native_build": dict(self.native_build_receipt),
                     "prior_curvature_scope_cost": self.prior_cost},
            "no_complete_Jacobian_or_large_native_workspace_saved": True,
            "all_original_physical_qualifications_still_required": True}
        data = json_bytes(output)
        # Leave room for the final small payload identity below.  Historical
        # complete costs remain in the caller's bound original terminal ledger,
        # not recursively duplicated in this necessary curvature input.
        if len(data) > MAX_CHECKPOINT_BYTES-1024:
            output["pending_frozen_multiplier_secant"] = None
            output["pending_omitted_for_declared_necessary_input_limit"] = {
                "full_bytes": len(data), "maximum_bytes": MAX_CHECKPOINT_BYTES,
                "all_nonzero_multipliers_omitted_together_not_thresholded": True}
            data = json_bytes(output)
        if len(data) > MAX_CHECKPOINT_BYTES-1024:
            raise ValueError("Even the necessary H-only input exceeds its declared size limit.")
        output["payload_without_this_receipt"] = {"bytes": len(data),
                                                   "sha256": hashlib.sha256(data).hexdigest()}
        return output
