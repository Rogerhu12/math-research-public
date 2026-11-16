#!/usr/bin/env python3
"""Dimension-free 170-variable engine for one new smaller physical-domain ledger.

Import-only.  The owner starts the clock before imports and all input reads.
Only dimension-free algebra is imported from the frozen true53 implementation;
no old finite instance, old 161-variable preparation, geometry, or suite runs.
Every later finite problem requires a strictly augmented original metric-row
set.  A finite residual or stop is not a full-grid or geometric certificate.
"""
from __future__ import annotations
import copy
import math
import time
from fractions import Fraction
from typing import Any
import numpy as np
from frame_entry_body_subspace import array_digest
from frame_metric_true53_paid_master_central_path import (
    NewMasterLedger, NewMasterLimitReached, _NumericalFailure,
    _residuals, _newton_system, _max_step, _finite_array, _finite_scalar,
    _inf, _converged, FRACTION_TO_BOUNDARY, RESIDUAL_TOL,
    COMPLEMENTARITY_TOL)

from frame_metric_true56_small168_scope import (
    POLICY, VARIABLES, INDEPENDENT, RHO_INDEX, H_INDEX, NORM_WEIGHT,
    LIMITS, PER_PROBLEM_ITERATIONS, PER_PROBLEM_SYSTEMS,
    Joint168Ledger, Joint168Limit, require)

def vector_record(value):
    a = np.asarray(value, dtype=np.float64)
    require(a.ndim == 1 and np.all(np.isfinite(a)), "a real finite vector is required")
    return {"length": len(a), "binary64": a.tolist(),
            "exact_binary64": [str(Fraction.from_float(float(v))) for v in a],
            "array_sha256": array_digest(a)}

class _OneProblemLedger(NewMasterLedger):
    def __init__(self, owner, binding, added_row_count):
        require(isinstance(owner, Joint168Ledger), "one new joint168 owner is required")
        # Only initializes metadata; the overridden check always uses owner300.
        super().__init__(owner.started)
        self.owner = owner
        self.policy = POLICY+"-one-new-finite-problem"
        self.binding, self.added_row_count = binding, added_row_count
        self.outer_event = None
    def elapsed(self):
        return self.owner.elapsed()
    def check(self, stage=""):
        return self.owner.check(stage)
    def _claim_core(self):
        self.check("joint168-core.entry")
        require(self.core_calls == 0, "one local problem has already been started")
        self.outer_event = self.owner.claim_problem(self.binding, self.added_row_count)
        self.core_calls += 1
    def _begin_iteration(self):
        self.check("iteration.before")
        if self.iterations_started >= PER_PROBLEM_ITERATIONS:
            raise Joint168Limit("per_problem_iterations", self.iterations_started+1,
                                 PER_PROBLEM_ITERATIONS, elapsed=self.elapsed())
        self.owner.charge("finite_master_iterations")
        return super()._begin_iteration()
    def _begin_system(self, iteration, phase):
        self.check("system."+str(phase)+".before")
        require(phase in ("predictor", "corrector"), "a real Newton phase is required")
        if self.newton_systems >= PER_PROBLEM_SYSTEMS:
            raise Joint168Limit("per_problem_newton_systems", self.newton_systems+1,
                                 PER_PROBLEM_SYSTEMS, elapsed=self.elapsed())
        self.owner.charge("finite_master_newton_systems")
        return super()._begin_system(iteration, phase)
    def finish(self, result):
        if self.outer_event is not None and self.outer_event.get("status") == "started":
            self.owner.end(self.outer_event, result.get("terminal"),
                           solver_status=result.get("status"),
                           iterations_started=self.iterations_started,
                           iterations_completed=self.iterations_completed,
                           newton_systems=self.newton_systems)
    def report(self):
        return {
            "schema": self.policy, "problem_binding_sha256": self.binding,
            "additional_original_metric_rows": self.added_row_count,
            "per_problem_limits": {"iterations": PER_PROBLEM_ITERATIONS,
                                   "newton_systems": PER_PROBLEM_SYSTEMS},
            "shared_scientific_seconds": self.elapsed(),
            "core_calls": self.core_calls,
            "iterations_started": self.iterations_started,
            "iterations_completed": self.iterations_completed,
            "newton_systems": self.newton_systems,
            "predictor_systems": self.predictor_systems,
            "corrector_systems": self.corrector_systems,
            "system_failures": self.system_failures,
            "failures": copy.deepcopy(self.failures),
            "systems": copy.deepcopy(self.system_records),
            "events": copy.deepcopy(self.events),
            "no_local_clock_or_global_counter_reset": True}

def _vector(value, length, name):
    array = np.array(value, dtype=np.float64, copy=True)
    require(array.shape == (length,), name+" has the wrong vector shape")
    _finite_array(array, "input."+name)
    return array

def _prepare170(A, b, row_tol, row_kind, initial_x, ledger, recovery):
    ledger.check("input.copy.before")
    A0 = np.array(A, dtype=np.float64, copy=True, order="C")
    require(A0.ndim == 2 and A0.shape[1] == VARIABLES,
            "the new matrix has exactly [delta168,rho,h] 170 columns")
    m = len(A0)
    b0 = _vector(b, m, "b")
    tol = _vector(row_tol, m, "row_tol")
    x = _vector(initial_x, VARIABLES, "initial_x")
    recovery["input_x"] = x.copy()
    kinds = list(row_kind)
    require(len(kinds) == m and all(isinstance(v, str) and v for v in kinds),
            "one original-unit row role is required for every row")
    require(np.all(tol >= 0), "row tolerances must be nonnegative")
    _finite_array(A0, "input.A")
    # All 170 coordinates are genuinely free, including all current 168
    # geometry coefficients.  The original physical172 box and
    # h >= 4*||M172x168 delta||_infinity are explicit original rows.
    free = np.arange(VARIABLES, dtype=np.int64)
    zero = np.all(A0 == 0., axis=1)
    active, inactive = np.flatnonzero(~zero), np.flatnonzero(zero)
    conflicts = inactive[b0[inactive] < 0.]
    tol_conflicts = inactive[b0[inactive]+tol[inactive] < 0.]
    unscaled = A0[active].copy()
    if len(active):
        scale = np.maximum(np.max(np.abs(unscaled), axis=1), np.abs(b0[active]))
        require(np.all(np.isfinite(scale) & (scale > 0.)),
                "positive finite row scaling is required")
        scaled = unscaled/scale[:, None]
        rhs = b0[active]/scale
    else:
        scale = np.empty(0)
        scaled = np.empty((0, VARIABLES))
        rhs = np.empty(0)
    c = np.r_[np.zeros(INDEPENDENT), 1., NORM_WEIGHT]
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        slack = np.maximum(1., rhs-scaled@x)
    _finite_array(scaled, "row_scaling.A")
    _finite_array(rhs, "row_scaling.b")
    _finite_array(slack, "initial.slack")
    data = {
        "A0": A0, "b0": b0, "tol": tol, "kind": kinds,
        "free": free, "fixed": np.empty(0, dtype=np.int64),
        "active": active, "inactive": inactive, "reduced_b": b0.copy(),
        "constant_conflicts": conflicts, "constant_tol_conflicts": tol_conflicts,
        "unscaled_free_A": unscaled, "row_scale": scale,
        "A": scaled, "B": rhs, "c": c}
    state = {"x": x, "s": slack, "lam": np.ones(len(active)),
             "accepted_iteration": 0}
    ledger.note("input.prepared", original_rows=m, active_rows=len(active),
                variable_count=VARIABLES, literal_zero_rows=len(inactive),
                objective="rho+1e-6*h", all_168_geometry_columns_are_free=True)
    ledger.check("input.prepared.after")
    return data, state

def _original170(data, state):
    x, slack, dual = state["x"], state["s"], state["lam"]
    active, inactive = data["active"], data["inactive"]
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        residual = data["A0"]@x-data["b0"]
        primal_slack = np.empty(len(data["b0"]))
        original_dual = np.zeros(len(data["b0"]))
        primal_slack[active] = data["row_scale"]*slack
        primal_slack[inactive] = data["b0"][inactive]
        original_dual[active] = dual/data["row_scale"]
        equation = residual+primal_slack
        stationarity = data["A0"].T@original_dual+data["c"]
        excess = residual-data["tol"]
    for name, arr in (("rows", residual), ("slack", primal_slack),
                      ("dual", original_dual), ("equation", equation),
                      ("stationarity", stationarity), ("tolerance", excess)):
        _finite_array(arr, "original170."+name)
    by_kind = {}
    for kind in dict.fromkeys(data["kind"]):
        ids = np.asarray([i for i, label in enumerate(data["kind"]) if label == kind])
        raw, over = residual[ids], excess[ids]
        by_kind[kind] = {
            "count": len(ids), "max_signed_row_residual": float(np.max(raw)),
            "max_positive_violation": max(0., float(np.max(raw))),
            "max_positive_tolerance_excess": max(0., float(np.max(over))),
            "violated_original_tolerance_count": int(np.count_nonzero(over > 0.)),
            "worst_original_row_index": int(ids[int(np.argmax(over))]),
            "tolerance_min": float(np.min(data["tol"][ids])),
            "tolerance_max": float(np.max(data["tol"][ids]))}
    return {
        "dual": original_dual, "slack": primal_slack,
        "row_residual": residual, "equation_residual": equation,
        "stationarity": stationarity, "by_kind": by_kind,
        "rows_within_original_tolerances": bool(np.all(excess <= 0.)),
        "max_positive_violation": max(0., float(np.max(residual, initial=0.))),
        "max_positive_tolerance_excess": max(0., float(np.max(excess, initial=0.))),
        "max_primal_equation_residual": _inf(equation),
        "free_stationarity_inf": _inf(stationarity)}

def _summary170(data, state, residuals, original):
    return {
        "accepted_iteration": int(state["accepted_iteration"]),
        "rho_actual_metric_upper_bound": float(state["x"][RHO_INDEX]),
        "h_coordinate": float(state["x"][H_INDEX]),
        "delta168_coordinate_infinity_norm": float(np.max(np.abs(state["x"][:INDEPENDENT]), initial=0.)),
        "scaled_primal_residual_inf": _inf(residuals["rp"]),
        "scaled_dual_residual_inf": _inf(residuals["rd"]),
        "scaled_primal_residual_relative": residuals["primal_residual_relative"],
        "scaled_dual_residual_relative": residuals["dual_residual_relative"],
        "mu": residuals["mu"], "complementarity_sum": residuals["complementarity_sum"],
        "complementarity_relative": residuals["complementarity_relative"],
        "primal_objective": residuals["primal_objective"],
        "dual_objective": residuals["dual_objective_reduced"],
        "scaled_primal_dual_gap": residuals["scaled_primal_dual_gap"],
        "minimum_scaled_slack": float(np.min(state["s"])) if len(state["s"]) else None,
        "minimum_scaled_dual": float(np.min(state["lam"])) if len(state["lam"]) else None,
        "original_rows_within_tolerances": original["rows_within_original_tolerances"],
        "original_max_positive_violation": original["max_positive_violation"],
        "original_max_positive_tolerance_excess": original["max_positive_tolerance_excess"],
        "original_primal_equation_residual_inf": original["max_primal_equation_residual"],
        "original_stationarity_inf": original["free_stationarity_inf"],
        "original_by_kind": original["by_kind"]}

def solve_joint168(
    A: Any,
    b: Any,
    row_tol: Any,
    row_kind: Any,
    initial_x: Any,
    *,
    ledger: Joint168Ledger,
    problem_binding: str,
    added_row_count: int,
) -> dict:
    """Solve one finite LP; return the last accepted finite state on every stop.

    Required driver-facing fields are status, last_finite_x (170 numbers or
    None), original_unit_dual and original_unit_slack.  All rows and tolerances
    are original units.  initial_x is not projected.  Every one of the 168
    geometry coordinates is free; the full physical172 box and physical-step
    norm are retained as explicit original rows supplied by the new model.

    A status of converged is only a binary64 finite-LP diagnostic.  It grants
    no complete-grid feasibility or actual geometric acceptance.  Other stop
    statuses do not assert infeasibility, unboundedness or stationarity.
    """
    if not isinstance(ledger, Joint168Ledger):
        raise TypeError("the shared Joint168Ledger is required")
    ledger = _OneProblemLedger(ledger, problem_binding, added_row_count)
    data: dict | None = None
    state: dict | None = None
    initial_record: dict | None = None
    history: list[dict] = []
    status = "not_started"
    terminal: dict | None = None
    current_iteration: dict | None = None
    recovery: dict = {}

    try:
        ledger._claim_core()
        data, state = _prepare170(
            A, b, row_tol, row_kind, initial_x, ledger, recovery
        )
        residuals = _residuals(data, state)
        original = _original170(data, state)
        initial_record = _summary170(data, state, residuals, original)

        if data["constant_conflicts"].size:
            status = "literal_constant_row_conflict"
        elif not data["active"].size:
            status = "no_nonzero_newton_rows"
        elif _converged(residuals, original):
            status = "converged"
        else:
            status = "iteration_limit"
            for _ in range(PER_PROBLEM_ITERATIONS):
                iteration = ledger._begin_iteration()
                current_iteration = {
                    "iteration": iteration,
                    "started_elapsed_seconds": ledger.elapsed(),
                    "status": "started",
                    "before": _summary170(data, state, residuals, original),
                }
                history.append(current_iteration)
                with np.errstate(over="raise", invalid="raise", divide="raise"):
                    rc_affine = state["s"] * state["lam"]
                dx_aff, ds_aff, dl_aff, prepared = _newton_system(
                    data, state, residuals, rc_affine, ledger,
                    iteration, "predictor", None
                )
                alpha_aff_primal = _max_step(state["s"], ds_aff)
                alpha_aff_dual = _max_step(state["lam"], dl_aff)
                with np.errstate(over="raise", invalid="raise", divide="raise"):
                    s_aff = state["s"] + alpha_aff_primal * ds_aff
                    l_aff = state["lam"] + alpha_aff_dual * dl_aff
                    mu_aff = float(s_aff @ l_aff) / state["s"].size
                _finite_scalar(mu_aff, "predictor.mu_affine")
                mu = residuals["mu"]
                if not mu > 0.0:
                    raise _NumericalFailure(
                        "nonpositive_current_complementarity", "corrector"
                    )
                # Equivalent to clip((mu_aff / mu)**3, 0, 1), without an
                # avoidable overflow when mu_aff / mu is already above one.
                if mu_aff <= 0.0:
                    sigma = 0.0
                elif mu_aff >= mu:
                    sigma = 1.0
                else:
                    sigma = (mu_aff / mu) ** 3
                with np.errstate(over="raise", invalid="raise", divide="raise"):
                    rc_corrector = (
                        state["s"] * state["lam"]
                        + ds_aff * dl_aff
                        - sigma * mu
                    )
                dx, ds, dlam, _ = _newton_system(
                    data, state, residuals, rc_corrector, ledger,
                    iteration, "corrector", prepared
                )
                alpha_primal = FRACTION_TO_BOUNDARY * _max_step(state["s"], ds)
                alpha_dual = FRACTION_TO_BOUNDARY * _max_step(state["lam"], dlam)
                ledger.check("iteration.before_candidate")
                with np.errstate(over="raise", invalid="raise", divide="raise"):
                    next_x = state["x"].copy()
                    next_x[data["free"]] += alpha_primal * dx
                    next_s = state["s"] + alpha_primal * ds
                    next_lam = state["lam"] + alpha_dual * dlam
                for name, value in (
                    ("x", next_x), ("s", next_s), ("lam", next_lam)
                ):
                    _finite_array(value, "candidate." + name)
                if not bool(np.all(next_s > 0.0) & np.all(next_lam > 0.0)):
                    raise _NumericalFailure(
                        "nonpositive_candidate",
                        "candidate",
                        {
                            "slack_min": float(np.min(next_s)),
                            "dual_min": float(np.min(next_lam)),
                        },
                    )
                # Accept atomically.  A subsequent diagnostic/budget failure
                # still returns this complete finite positive state.
                state = {
                    "x": next_x,
                    "s": next_s,
                    "lam": next_lam,
                    "accepted_iteration": iteration,
                }
                ledger.iterations_completed += 1
                current_iteration.update(
                    {
                        "status": "accepted",
                        "affine_primal_step": alpha_aff_primal,
                        "affine_dual_step": alpha_aff_dual,
                        "affine_slack_min": float(np.min(s_aff)),
                        "affine_dual_min": float(np.min(l_aff)),
                        "mu_affine": mu_aff,
                        "sigma": sigma,
                        "primal_step": alpha_primal,
                        "dual_step": alpha_dual,
                    }
                )
                residuals = _residuals(data, state)
                original = _original170(data, state)
                current_iteration["after"] = _summary170(
                    data, state, residuals, original
                )
                current_iteration["finished_elapsed_seconds"] = ledger.elapsed()
                ledger.check("iteration.after_diagnostics")
                if _converged(residuals, original):
                    status = "converged"
                    break

    except Exception as error:
        ledger._record_failure(error, "core")
        if isinstance(error, NewMasterLimitReached):
            status = error.reason
        elif data is None:
            status = "input_or_preparation_failure"
        else:
            status = "numerical_failure"
        terminal = {
            "type": type(error).__name__,
            "reason": getattr(error, "reason", type(error).__name__),
            "stage": getattr(error, "stage", "core"),
            "message": str(error),
            "details": getattr(error, "details", {}),
        }
        if current_iteration is not None:
            current_iteration["stop"] = dict(terminal)
            current_iteration["finished_elapsed_seconds"] = ledger.elapsed()
            if current_iteration["status"] == "started":
                current_iteration["status"] = "stopped_before_acceptance"

    # Essential result recovery is performed even after a deadline.  It does
    # no Newton system, retry, geometry call or new scientific query, and its
    # elapsed time is included in this same ledger and the driver's last clock.
    result: dict[str, Any] = {
        "schema": POLICY,
        "status": status,
        "last_finite_x": None,
        "original_unit_dual": None,
        "original_unit_slack": None,
        "original_row_residual": None,
        "original_primal_equation_residual": None,
        "original_stationarity_before_fixed_equalities": None,
        "fixed_equality_multipliers_original_units": None,
        "last_summary": None,
        "initial_summary": initial_record,
        "iterations": history,
        "terminal": terminal,
        "interpretation": {
            "scope": "one genuinely augmented finite LP; all preceding problems remain closed",
            "binary64_without_outward_rounding": True,
            "actual_grid_or_geometry_acceptance": False,
            "iteration_limit_is_infeasibility_proof": False,
            "regularization_or_fallback_used": False,
            "fixed_coordinates_use_literal_equality_only": True,
            "zero_rows_use_literal_zero_coefficients_only": True,
            "variable_order": "delta168,rho,h",
            "objective": "rho+1e-6*h",
            "all_168_geometry_coordinates_are_free": True,
            "physical172_norm_is_encoded_in_original_model_rows": True,
            "fraction_to_boundary": FRACTION_TO_BOUNDARY,
            "relative_residual_tolerance": RESIDUAL_TOL,
            "relative_complementarity_tolerance": COMPLEMENTARITY_TOL,
        },
    }
    if state is None and "input_x" in recovery:
        result["last_finite_x"] = recovery["input_x"].tolist()
        result["last_finite_x_origin"] = "validated_input_before_newton_preparation"
        result["input_fixed_values_restored"] = bool(
            recovery.get("fixed_values_restored", False)
        )
    if data is not None:
        result["preprocessing"] = {
            "original_rows": int(data["b0"].size),
            "active_newton_rows": int(data["active"].size),
            "free_coordinate_indices": data["free"].tolist(),
            "literal_fixed_coordinate_indices": data["fixed"].tolist(),
            "literal_fixed_values": [],
            "literal_zero_rows": [
                {
                    "original_index": int(i),
                    "original_kind": data["kind"][int(i)],
                    "reduced_rhs": float(data["reduced_b"][int(i)]),
                    "original_tolerance": float(data["tol"][int(i)]),
                    "strict_constant_conflict": bool(
                        data["reduced_b"][int(i)] < 0.0
                    ),
                    "tolerated_constant_conflict": bool(
                        data["reduced_b"][int(i)] + data["tol"][int(i)] < 0.0
                    ),
                }
                for i in data["inactive"]
            ],
            "strict_constant_conflict_count": int(
                data["constant_conflicts"].size
            ),
            "tolerated_constant_conflict_count": int(
                data["constant_tol_conflicts"].size
            ),
            "row_scale_min_active": float(np.min(data["row_scale"]))
            if data["active"].size else None,
            "row_scale_max_active": float(np.max(data["row_scale"]))
            if data["active"].size else None,
        }
    if state is not None and data is not None:
        result["last_finite_x"] = state["x"].tolist()
        result["last_finite_x_origin"] = "accepted_core_state"
        result["last_accepted_iteration"] = int(state["accepted_iteration"])
        try:
            residuals = _residuals(data, state)
            original = _original170(data, state)
            result["original_unit_dual"] = original["dual"].tolist()
            result["original_unit_slack"] = original["slack"].tolist()
            result["original_row_residual"] = original["row_residual"].tolist()
            result["original_primal_equation_residual"] = original[
                "equation_residual"
            ].tolist()
            result["original_stationarity_before_fixed_equalities"] = original[
                "stationarity"
            ].tolist()
            result["fixed_equality_multipliers_original_units"] = []
            result["last_summary"] = _summary170(data, state, residuals, original)
            result["last_finite_x_record"] = vector_record(state["x"])
            result["last_scaled_slack"] = state["s"].tolist()
            result["last_scaled_dual"] = state["lam"].tolist()
            result["active_original_row_indices"] = data["active"].tolist()
            result["active_row_scales"] = data["row_scale"].tolist()
        except Exception as error:
            ledger._record_failure(error, "result_recovery")
            result["recovery_failure"] = {
                "type": type(error).__name__,
                "message": str(error),
                "stage": getattr(error, "stage", "result_recovery"),
            }
            result["last_scaled_slack"] = state["s"].tolist()
            result["last_scaled_dual"] = state["lam"].tolist()
            result["active_original_row_indices"] = data["active"].tolist()
            result["active_row_scales"] = data["row_scale"].tolist()
            if result["status"] == "converged":
                result["status"] = "result_diagnostic_failure"
    if ledger.elapsed() >= ledger.owner.limits["science_seconds"] and result["status"] == "converged":
        result["algorithm_status_before_result_recovery"] = "converged"
        result["status"] = "time_limit"
        limit = NewMasterLimitReached(
            "time_limit", "result_recovery.completed", ledger.elapsed()
        )
        ledger._record_failure(limit, "result_recovery.completed")
    if result.get("last_finite_x") is not None:
        result["last_finite_x_record"] = vector_record(result["last_finite_x"])
    result["all_returned_finite170_values_retained"] = bool(
        result.get("last_finite_x_record") is not None
        and result["last_finite_x_record"]["length"] == VARIABLES)
    ledger.finish(result)
    result["ledger"] = ledger.report()
    return result
