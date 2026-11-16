"""One bounded, new primal-dual solve of the paid true53 finite master LP.

Import-only numerical core.  The driver owns the original-log read, input
assembly, source bindings, stdout and FINAL_CLOCK.  This module neither reads
files nor constructs geometry/gradients nor calls any previous solver.

Problem: min -x[160], subject to original_A @ x <= original_b.
The first 160 coordinates have the supplied finite outer box.  Those bounds
must already be present among the original rows; this core does not append
rows.  Only literal lo[j] == hi[j] is eliminated.  Only literal all-zero
reduced coefficient rows are removed from the Newton arrays.

The algorithm is the infeasible-start predictor-corrector in the published
design, equations (6)--(8), with positive row scaling and optional *exact
diagonal congruence* of the normal system.  There is no jitter, regularization,
least-squares fallback, clipping of near-fixed coordinates, or solver retry.
All comparisons and diagnostics are binary64, without outward rounding.
"""

from __future__ import annotations

import hashlib
import math
import time
from typing import Any

import numpy as np


POLICY = "same159-true53-all-paid-finite-master-central-path-v1"
VARIABLES = 161
OUTER_VARIABLES = 160
GAMMA_INDEX = 160
MAX_ITERATIONS = 96
MAX_SYSTEMS = 192
MAX_SECONDS = 240.0
FRACTION_TO_BOUNDARY = 0.995
RESIDUAL_TOL = 1.0e-9
COMPLEMENTARITY_TOL = 1.0e-9


class NewMasterLimitReached(RuntimeError):
    """A shared new-work limit, not an infeasibility or optimality finding."""

    def __init__(self, reason: str, stage: str, elapsed_seconds: float):
        super().__init__(reason + " at " + stage)
        self.reason = reason
        self.stage = stage
        self.elapsed_seconds = float(elapsed_seconds)
        self.recorded = False


class _NumericalFailure(RuntimeError):
    def __init__(self, reason: str, stage: str, details: dict | None = None):
        super().__init__(reason + " at " + stage)
        self.reason = reason
        self.stage = stage
        self.details = details or {}
        self.recorded = False


class NewMasterLedger:
    """Shared clock: construct before ALL original-log input and assembly.

    A pre-import time.monotonic() value may be supplied as started_monotonic.
    check(), elapsed(), and report() are public driver interfaces.  The time
    origin and the 96 / 192 / 240 limits are never reset by solve_paid_master.
    A BLAS/LAPACK call is checked immediately before and after; an indivisible
    call that crosses the deadline is recorded as an overrun, never retried.
    """

    def __init__(
        self,
        started_monotonic: float | None = None,
        *,
        policy: str = POLICY,
    ):
        now = time.monotonic()
        start = now if started_monotonic is None else float(started_monotonic)
        if policy != POLICY:
            raise ValueError("unexpected new-master policy")
        if not math.isfinite(start) or start > now:
            raise ValueError("started_monotonic must be finite and not future")
        self.started_monotonic = start
        self.policy = policy
        self.iterations_started = 0
        self.iterations_completed = 0
        self.newton_systems = 0
        self.predictor_systems = 0
        self.corrector_systems = 0
        self.system_failures = 0
        self.core_calls = 0
        self.failures: list[dict] = []
        self.system_records: list[dict] = []
        self.events: list[dict] = []

    def elapsed(self) -> float:
        return float(time.monotonic() - self.started_monotonic)

    def check(self, stage: str = "") -> float:
        elapsed = self.elapsed()
        if elapsed >= MAX_SECONDS:
            raise NewMasterLimitReached("time_limit", stage, elapsed)
        return elapsed

    def note(self, stage: str, **fields: Any) -> None:
        """Small driver/core metadata only; never pass original arrays here."""
        self.events.append(
            {"stage": str(stage), "elapsed_seconds": self.elapsed(), **fields}
        )

    def _record_failure(self, error: Exception, stage: str) -> None:
        if getattr(error, "recorded", False):
            return
        self.failures.append(
            {
                "kind": getattr(error, "reason", type(error).__name__),
                "stage": getattr(error, "stage", stage),
                "message": str(error),
                "elapsed_seconds": self.elapsed(),
                "details": getattr(error, "details", {}),
            }
        )
        try:
            error.recorded = True
        except (AttributeError, TypeError):
            pass

    def _claim_core(self) -> None:
        self.check("core.entry")
        if self.core_calls != 0:
            raise ValueError("this shared ledger permits exactly one core solve")
        self.core_calls += 1

    def _begin_iteration(self) -> int:
        self.check("iteration.before")
        if self.iterations_started >= MAX_ITERATIONS:
            raise NewMasterLimitReached(
                "iteration_limit", "iteration.before", self.elapsed()
            )
        self.iterations_started += 1
        return self.iterations_started

    def _begin_system(self, iteration: int, phase: str) -> dict:
        self.check("system." + phase + ".before")
        if self.newton_systems >= MAX_SYSTEMS:
            raise NewMasterLimitReached(
                "system_limit", "system." + phase + ".before", self.elapsed()
            )
        self.newton_systems += 1
        if phase == "predictor":
            self.predictor_systems += 1
        elif phase == "corrector":
            self.corrector_systems += 1
        else:
            raise ValueError("invalid Newton phase")
        item = {
            "system": self.newton_systems,
            "iteration": iteration,
            "phase": phase,
            "started_elapsed_seconds": self.elapsed(),
            "status": "started",
        }
        self.system_records.append(item)
        return item

    def _end_system(self, item: dict, status: str, **fields: Any) -> None:
        if item["status"] != "started":
            raise RuntimeError("a Newton system was finalized twice")
        item.update(fields)
        item["status"] = status
        item["finished_elapsed_seconds"] = self.elapsed()
        item["elapsed_seconds"] = (
            item["finished_elapsed_seconds"] - item["started_elapsed_seconds"]
        )
        if status != "solved":
            self.system_failures += 1

    def report(self) -> dict:
        elapsed = self.elapsed()
        counts: dict[str, int] = {}
        for item in self.failures:
            key = str(item["kind"])
            counts[key] = counts.get(key, 0) + 1
        return {
            "policy": self.policy,
            "limits": {
                "iterations": MAX_ITERATIONS,
                "newton_systems": MAX_SYSTEMS,
                "seconds": MAX_SECONDS,
            },
            "elapsed_seconds": elapsed,
            "remaining_seconds": max(0.0, MAX_SECONDS - elapsed),
            "deadline_observed_exceeded": elapsed >= MAX_SECONDS,
            "observed_overrun_seconds": max(0.0, elapsed - MAX_SECONDS),
            "core_calls": self.core_calls,
            "iterations_started": self.iterations_started,
            "iterations_completed": self.iterations_completed,
            "newton_systems": self.newton_systems,
            "predictor_systems": self.predictor_systems,
            "corrector_systems": self.corrector_systems,
            "system_failures": self.system_failures,
            "failure_count": len(self.failures),
            "failure_counts": counts,
            "failures": [dict(item) for item in self.failures],
            "systems": [dict(item) for item in self.system_records],
            "events": [dict(item) for item in self.events],
        }


def _inf(values: np.ndarray) -> float:
    return float(np.max(np.abs(values))) if values.size else 0.0


def _array_digest(values: np.ndarray) -> dict:
    """New-system hash, separate from the driver's original-input binding.

    SHA-256 is over raw C-order little-endian binary64 bytes; shape and dtype
    are explicit metadata.  No dense matrix/vector payload is emitted here.
    """
    canonical = np.ascontiguousarray(values, dtype=np.dtype("<f8"))
    return {
        "encoding": "raw-c-order-little-endian-float64",
        "shape": [int(size) for size in canonical.shape],
        "sha256": hashlib.sha256(canonical.tobytes(order="C")).hexdigest(),
    }


def _finite_array(values: np.ndarray, stage: str) -> None:
    if not bool(np.all(np.isfinite(values))):
        raise _NumericalFailure(
            "nonfinite_array",
            stage,
            {"nonfinite_entries": int(np.count_nonzero(~np.isfinite(values)))},
        )


def _finite_scalar(value: float, stage: str) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise _NumericalFailure("nonfinite_scalar", stage)
    return value


def _vector(value: Any, length: int, name: str) -> np.ndarray:
    array = np.array(value, dtype=np.float64, copy=True)
    if array.ndim != 1 or array.shape[0] != length:
        raise ValueError(name + " has the wrong vector shape")
    _finite_array(array, "input." + name)
    return array


def _max_step(positive: np.ndarray, direction: np.ndarray) -> float:
    # Only ratios strictly below one are evaluated.  This avoids overflow
    # from harmless huge ratios without clipping a small coefficient.
    crosses_before_one = direction < -positive
    if not bool(np.any(crosses_before_one)):
        return 1.0
    ratios = -positive[crosses_before_one] / direction[crosses_before_one]
    result = float(np.min(ratios))
    if not math.isfinite(result) or not 0.0 < result <= 1.0:
        raise _NumericalFailure("invalid_boundary_step", "step_length")
    return result


def _prepare(
    original_A: Any,
    original_b: Any,
    row_tol: Any,
    row_kind: Any,
    outer_lo: Any,
    outer_hi: Any,
    initial_x: Any,
    ledger: NewMasterLedger,
    recovery: dict,
) -> tuple[dict, dict]:
    ledger.check("input.copy.before")
    A0 = np.array(original_A, dtype=np.float64, copy=True, order="C")
    if A0.ndim != 2 or A0.shape[1] != VARIABLES:
        raise ValueError("A must have shape (number_of_original_rows, 161)")
    m0 = A0.shape[0]
    b0 = _vector(original_b, m0, "b")
    tolerances = _vector(row_tol, m0, "row_tol")
    lo = _vector(outer_lo, OUTER_VARIABLES, "outer_lo")
    hi = _vector(outer_hi, OUTER_VARIABLES, "outer_hi")
    x = _vector(initial_x, VARIABLES, "initial_x")
    recovery["input_x"] = x.copy()
    _finite_array(A0, "input.A")
    if bool(np.any(tolerances < 0.0)):
        raise ValueError("row_tol must be nonnegative")
    if bool(np.any(lo > hi)):
        raise ValueError("literal outer lower bound exceeds upper bound")
    kinds = list(row_kind)
    if len(kinds) != m0 or any(
        not isinstance(kind, str) or not kind for kind in kinds
    ):
        raise ValueError("row_kind must contain one nonempty string per row")
    ledger.check("input.copy.after")

    fixed = np.flatnonzero(lo == hi)
    fixed_set = set(fixed.tolist())
    free = np.array(
        [index for index in range(VARIABLES) if index not in fixed_set],
        dtype=np.int64,
    )
    x[fixed] = lo[fixed]
    recovery["input_x"] = x.copy()
    recovery["fixed_values_restored"] = True
    ledger.check("literal_substitution.before")
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        reduced_b = b0.copy()
        if fixed.size:
            reduced_b = reduced_b - A0[:, fixed] @ lo[fixed]
        reduced_A = A0[:, free].copy()
    _finite_array(reduced_b, "literal_substitution.rhs")
    _finite_array(reduced_A, "literal_substitution.matrix")
    zero = np.all(reduced_A == 0.0, axis=1)
    active = np.flatnonzero(~zero)
    inactive = np.flatnonzero(zero)
    constant_conflicts = inactive[reduced_b[inactive] < 0.0]
    constant_tol_conflicts = inactive[
        reduced_b[inactive] + tolerances[inactive] < 0.0
    ]
    ledger.check("literal_substitution.after")

    if active.size:
        unscaled_free_A = reduced_A[active, :].copy()
        unscaled_rhs = reduced_b[active].copy()
        scale = np.maximum(
            np.max(np.abs(unscaled_free_A), axis=1), np.abs(unscaled_rhs)
        )
        if not bool(np.all(np.isfinite(scale) & (scale > 0.0))):
            raise _NumericalFailure("invalid_positive_row_scale", "row_scaling")
        A = unscaled_free_A / scale[:, None]
        B = unscaled_rhs / scale
    else:
        unscaled_free_A = np.empty((0, free.size), dtype=np.float64)
        scale = np.empty(0, dtype=np.float64)
        A = np.empty((0, free.size), dtype=np.float64)
        B = np.empty(0, dtype=np.float64)

    c = np.zeros(free.size, dtype=np.float64)
    gamma_free = int(np.flatnonzero(free == GAMMA_INDEX)[0])
    c[gamma_free] = -1.0
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        gap = B - A @ x[free]
        slack = np.maximum(1.0, gap)
    dual = np.ones(active.size, dtype=np.float64)
    _finite_array(slack, "initial.slack")
    _finite_array(A, "row_scaling.A")
    _finite_array(B, "row_scaling.B")
    ledger.check("initial_state.after")

    data = {
        "A0": A0,
        "b0": b0,
        "tol": tolerances,
        "kind": kinds,
        "lo": lo,
        "hi": hi,
        "fixed": fixed,
        "free": free,
        "reduced_b": reduced_b,
        "active": active,
        "inactive": inactive,
        "constant_conflicts": constant_conflicts,
        "constant_tol_conflicts": constant_tol_conflicts,
        "unscaled_free_A": unscaled_free_A,
        "row_scale": scale,
        "A": A,
        "B": B,
        "c": c,
    }
    state = {"x": x, "s": slack, "lam": dual, "accepted_iteration": 0}
    ledger.note(
        "input.prepared",
        original_rows=int(m0),
        active_rows=int(active.size),
        literal_zero_rows=int(inactive.size),
        literal_fixed_coordinates=int(fixed.size),
        free_coordinates=int(free.size),
    )
    return data, state


def _residuals(data: dict, state: dict) -> dict:
    A, B, c = data["A"], data["B"], data["c"]
    x, slack, dual = state["x"][data["free"]], state["s"], state["lam"]
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        Ax = A @ x
        ATdual = A.T @ dual
        rp = Ax + slack - B
        rd = ATdual + c
        products = slack * dual
        complementarity = float(np.sum(products))
        mu = complementarity / slack.size if slack.size else 0.0
        primal_objective = float(c @ x)
        dual_objective = -float(B @ dual)
        primal_dual_gap = float(np.subtract(primal_objective, dual_objective))
    for name, value in (("rp", rp), ("rd", rd), ("products", products)):
        _finite_array(value, "iterate." + name)
    for name, value in (
        ("mu", mu),
        ("complementarity", complementarity),
        ("primal_objective", primal_objective),
        ("dual_objective", dual_objective),
        ("primal_dual_gap", primal_dual_gap),
    ):
        _finite_scalar(value, "iterate." + name)
    objective_scale = max(1.0, abs(primal_objective), abs(dual_objective))
    relative_complementarity = (complementarity / objective_scale) / (
        1.0 / objective_scale
        + abs(primal_objective) / objective_scale
        + abs(dual_objective) / objective_scale
    )
    return {
        "rp": rp,
        "rd": rd,
        "mu": mu,
        "primal_residual_relative": _inf(rp) / (1.0 + _inf(B)),
        "dual_residual_relative": _inf(rd) / (1.0 + _inf(c) + _inf(ATdual)),
        "complementarity_sum": complementarity,
        "complementarity_relative": relative_complementarity,
        "primal_objective": primal_objective,
        "dual_objective_reduced": dual_objective,
        "scaled_primal_dual_gap": primal_dual_gap,
    }


def _original_units(data: dict, state: dict) -> dict:
    x, slack, dual = state["x"], state["s"], state["lam"]
    active, inactive = data["active"], data["inactive"]
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        row_residual = data["A0"] @ x - data["b0"]
        original_slack = np.empty(data["b0"].size, dtype=np.float64)
        original_dual = np.zeros(data["b0"].size, dtype=np.float64)
        original_slack[active] = data["row_scale"] * slack
        original_dual[active] = dual / data["row_scale"]
        # Constant rows retain their actual nonnegative, zero, or conflicting
        # constant slack; they never receive a fictitious interior multiplier.
        original_slack[inactive] = data["reduced_b"][inactive]
        equation_residual = row_residual + original_slack
        stationarity = data["A0"].T @ original_dual
        stationarity[GAMMA_INDEX] -= 1.0
        excess = row_residual - data["tol"]
    for name, value in (
        ("row_residual", row_residual),
        ("slack", original_slack),
        ("dual", original_dual),
        ("equation_residual", equation_residual),
        ("stationarity", stationarity),
        ("tol_excess", excess),
    ):
        _finite_array(value, "original_units." + name)

    by_kind: dict[str, dict] = {}
    for kind in dict.fromkeys(data["kind"]):
        ids = np.array(
            [i for i, label in enumerate(data["kind"]) if label == kind],
            dtype=np.int64,
        )
        raw = row_residual[ids]
        over = excess[ids]
        by_kind[kind] = {
            "count": int(ids.size),
            "max_signed_row_residual": float(np.max(raw)),
            "max_positive_violation": max(0.0, float(np.max(raw))),
            "max_positive_tolerance_excess": max(0.0, float(np.max(over))),
            "violated_original_tolerance_count": int(np.count_nonzero(over > 0.0)),
            "worst_raw_row_index": int(ids[int(np.argmax(raw))]),
            "worst_tolerance_row_index": int(ids[int(np.argmax(over))]),
            "tolerance_min": float(np.min(data["tol"][ids])),
            "tolerance_max": float(np.max(data["tol"][ids])),
        }
    lower_excess = data["lo"] - x[:OUTER_VARIABLES]
    upper_excess = x[:OUTER_VARIABLES] - data["hi"]
    _finite_array(lower_excess, "original_units.outer_lower")
    _finite_array(upper_excess, "original_units.outer_upper")
    return {
        "dual": original_dual,
        "slack": original_slack,
        "row_residual": row_residual,
        "equation_residual": equation_residual,
        "stationarity": stationarity,
        "by_kind": by_kind,
        "rows_within_original_tolerances": bool(np.all(excess <= 0.0)),
        "max_positive_violation": max(0.0, float(np.max(row_residual)))
        if row_residual.size else 0.0,
        "max_positive_tolerance_excess": max(0.0, float(np.max(excess)))
        if excess.size else 0.0,
        "max_primal_equation_residual": _inf(equation_residual),
        "free_stationarity_inf": _inf(stationarity[data["free"]]),
        "full_stationarity_inf_before_fixed_equalities": _inf(stationarity),
        "fixed_equality_multipliers": -stationarity[data["fixed"]],
        "outer_box": {
            "max_lower_excess": max(0.0, float(np.max(lower_excess))),
            "max_upper_excess": max(0.0, float(np.max(upper_excess))),
            "literal_fixed_values_exactly_restored": bool(
                np.all(x[data["fixed"]] == data["lo"][data["fixed"]])
            ),
        },
    }


def _summary(data: dict, state: dict, residuals: dict, original: dict) -> dict:
    return {
        "accepted_iteration": int(state["accepted_iteration"]),
        "gamma": float(state["x"][GAMMA_INDEX]),
        "h_coordinate": float(state["x"][OUTER_VARIABLES - 1]),
        "scaled_primal_residual_inf": _inf(residuals["rp"]),
        "scaled_dual_residual_inf": _inf(residuals["rd"]),
        "scaled_primal_residual_relative": residuals["primal_residual_relative"],
        "scaled_dual_residual_relative": residuals["dual_residual_relative"],
        "mu": residuals["mu"],
        "complementarity_sum": residuals["complementarity_sum"],
        "complementarity_relative": residuals["complementarity_relative"],
        "primal_objective": residuals["primal_objective"],
        "dual_objective_reduced": residuals["dual_objective_reduced"],
        "scaled_primal_dual_gap": residuals["scaled_primal_dual_gap"],
        "minimum_scaled_slack": float(np.min(state["s"]))
        if state["s"].size else None,
        "minimum_scaled_dual": float(np.min(state["lam"]))
        if state["lam"].size else None,
        "original_rows_within_tolerances": original[
            "rows_within_original_tolerances"
        ],
        "original_max_positive_violation": original["max_positive_violation"],
        "original_max_positive_tolerance_excess": original[
            "max_positive_tolerance_excess"
        ],
        "original_primal_equation_residual_inf": original[
            "max_primal_equation_residual"
        ],
        "original_free_stationarity_inf": original["free_stationarity_inf"],
        "original_by_kind": original["by_kind"],
        "outer_box": original["outer_box"],
    }


def _converged(residuals: dict, original: dict) -> bool:
    return (
        original["rows_within_original_tolerances"]
        and residuals["primal_residual_relative"] <= RESIDUAL_TOL
        and residuals["dual_residual_relative"] <= RESIDUAL_TOL
        and residuals["complementarity_relative"] <= COMPLEMENTARITY_TOL
    )


def _newton_system(
    data: dict,
    state: dict,
    residuals: dict,
    rc: np.ndarray,
    ledger: NewMasterLedger,
    iteration: int,
    phase: str,
    prepared: dict | None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict]:
    item = ledger._begin_system(iteration, phase)
    A, slack, dual = data["A"], state["s"], state["lam"]
    rp, rd = residuals["rp"], residuals["rd"]
    try:
        _finite_array(rc, "system." + phase + ".rc")
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            if prepared is None:
                weight = dual / slack
                _finite_array(weight, "system." + phase + ".weight")
                if not bool(np.all(weight > 0.0)):
                    raise _NumericalFailure("nonpositive_weight", phase)
                weighted_A = np.sqrt(weight)[:, None] * A
                normal = weighted_A.T @ weighted_A
                _finite_array(normal, "system." + phase + ".normal")
                diagonal = np.diag(normal).copy()
                if not bool(np.all(diagonal > 0.0)):
                    raise _NumericalFailure(
                        "nonpositive_normal_diagonal",
                        phase,
                        {"nonpositive_entries": int(np.count_nonzero(diagonal <= 0.0))},
                    )
                equilibration = 1.0 / np.sqrt(diagonal)
                balanced = (
                    equilibration[:, None] * normal * equilibration[None, :]
                )
                _finite_array(balanced, "system." + phase + ".balanced_normal")
                prepared = {
                    "weight": weight,
                    "normal": normal,
                    "balanced": balanced,
                    "equilibration": equilibration,
                    "diagonal": diagonal,
                    "normal_digest": _array_digest(normal),
                    "balanced_digest": _array_digest(balanced),
                }
                item["normal_matrix_reused"] = False
            else:
                item["normal_matrix_reused"] = True
            weight = prepared["weight"]
            normal = prepared["normal"]
            equilibration = prepared["equilibration"]
            rhs = -rd + A.T @ (rc / slack) - A.T @ (weight * rp)
            balanced_rhs = equilibration * rhs
            _finite_array(rhs, "system." + phase + ".rhs")
            _finite_array(balanced_rhs, "system." + phase + ".balanced_rhs")
            item.update({
                "normal_matrix_digest": prepared["normal_digest"],
                "balanced_normal_matrix_digest": prepared["balanced_digest"],
                "normal_rhs_digest": _array_digest(rhs),
                "balanced_rhs_digest": _array_digest(balanced_rhs),
                "complementarity_rhs_digest": _array_digest(rc),
            })
            ledger.check("system." + phase + ".before_solve")
            # The sole factor/solve call for this charged Newton system.
            # No diagonal addition, pseudoinverse, fallback or refinement.
            balanced_dx = np.linalg.solve(prepared["balanced"], balanced_rhs)
            ledger.check("system." + phase + ".after_solve")
            dx = equilibration * balanced_dx
            Adx = A @ dx
            ds = -rp - Adx
            dlam = (-rc + dual * rp + dual * Adx) / slack
            for name, value in (("dx", dx), ("ds", ds), ("dlam", dlam)):
                _finite_array(value, "system." + phase + "." + name)

            normal_residual = normal @ dx - rhs
            scaled_primal = Adx + ds + rp
            scaled_dual = A.T @ dlam + rd
            complementarity = dual * ds + slack * dlam + rc

            # Independently return to unscaled equations (5); fixed columns
            # have dx=0 and their stationarity is an equality multiplier.
            scale = data["row_scale"]
            original_dual = dual / scale
            original_slack = scale * slack
            original_dlam = dlam / scale
            original_ds = scale * ds
            original_rp = (
                data["A0"][data["active"], :] @ state["x"]
                + original_slack
                - data["b0"][data["active"]]
            )
            original_rd = data["unscaled_free_A"].T @ original_dual + data["c"]
            original_eq_primal = (
                data["unscaled_free_A"] @ dx + original_ds + original_rp
            )
            original_eq_dual = (
                data["unscaled_free_A"].T @ original_dlam + original_rd
            )
            original_eq_complementarity = (
                original_dual * original_ds
                + original_slack * original_dlam
                + rc
            )
        for name, value in (
            ("normal_residual", normal_residual),
            ("scaled_primal", scaled_primal),
            ("scaled_dual", scaled_dual),
            ("complementarity", complementarity),
            ("original_eq_primal", original_eq_primal),
            ("original_eq_dual", original_eq_dual),
            ("original_eq_complementarity", original_eq_complementarity),
        ):
            _finite_array(value, "system." + phase + "." + name)
        relative = _inf(normal_residual) / max(
            1.0, _inf(rhs), _inf(normal @ dx)
        )
        ledger.check("system." + phase + ".after_diagnostics")
        ledger._end_system(
            item,
            "solved",
            free_dimension=int(A.shape[1]),
            active_rows=int(A.shape[0]),
            weight_min=float(np.min(weight)),
            weight_max=float(np.max(weight)),
            normal_diagonal_min=float(np.min(prepared["diagonal"])),
            normal_diagonal_max=float(np.max(prepared["diagonal"])),
            equilibration_min=float(np.min(equilibration)),
            equilibration_max=float(np.max(equilibration)),
            rhs_inf=_inf(rhs),
            dx_inf=_inf(dx),
            ds_inf=_inf(ds),
            dlam_inf=_inf(dlam),
            normal_equation_residual_inf=_inf(normal_residual),
            normal_equation_residual_relative=relative,
            residual_warning_only=relative > 1.0e-7,
            scaled_equation5_primal_inf=_inf(scaled_primal),
            scaled_equation5_dual_inf=_inf(scaled_dual),
            scaled_equation5_complementarity_inf=_inf(complementarity),
            original_equation5_primal_inf=_inf(original_eq_primal),
            original_equation5_free_dual_inf=_inf(original_eq_dual),
            original_equation5_complementarity_inf=_inf(original_eq_complementarity),
        )
        return dx, ds, dlam, prepared
    except Exception as error:
        ledger._record_failure(error, "system." + phase)
        ledger._end_system(
            item,
            "limit_reached" if isinstance(error, NewMasterLimitReached) else "failed",
            exception_type=type(error).__name__,
            error=str(error),
        )
        raise


def _recover_tolerated_outer_box(data: dict) -> dict:
    """Recover only the original, tagged literal +/- unit bound rows.

    Physical/norm rows may coincide numerically with bound rows.  They remain
    extra constraints and are deliberately excluded from this identification.
    No tolerance is inferred from a generic row or from a global constant.
    """
    A0, b0, tolerances = data["A0"], data["b0"], data["tol"]
    tagged = np.array(
        [i for i, kind in enumerate(data["kind"]) if kind == "bound"],
        dtype=np.int64,
    )
    fixed_set = set(data["fixed"].tolist())
    metadata: dict[str, Any] = {
        "required_row_kind": "bound",
        "tagged_bound_row_count": int(tagged.size),
        "expected_bound_row_count": 2 * OUTER_VARIABLES,
        "identification": "literal single +/-1 coefficient; literal hi/-lo RHS",
        "fixed_coordinates_remain_exact": data["fixed"].tolist(),
        "fixed_coordinate_scope": (
            "original-row-tolerated region intersected with the exact "
            "literal-fixed-coordinate affine subspace"
        ),
        "coordinates": [],
    }
    if tagged.size != 2 * OUTER_VARIABLES:
        metadata.update(
            available=False,
            reason="tagged_bound_row_count_is_not_320",
        )
        return metadata

    unit_mask = np.count_nonzero(A0[tagged, :], axis=1) == 1
    tagged_units = tagged[unit_mask]
    lower_tolerance = np.zeros(OUTER_VARIABLES, dtype=np.float64)
    upper_tolerance = np.zeros(OUTER_VARIABLES, dtype=np.float64)
    complete = True
    for j in range(OUTER_VARIABLES):
        plus = tagged_units[
            (A0[tagged_units, j] == 1.0) & (b0[tagged_units] == data["hi"][j])
        ]
        minus = tagged_units[
            (A0[tagged_units, j] == -1.0) & (b0[tagged_units] == -data["lo"][j])
        ]
        item = {
            "coordinate": j,
            "strict_lower": float(data["lo"][j]),
            "strict_upper": float(data["hi"][j]),
            "literal_fixed_exact": j in fixed_set,
            "lower_matching_bound_row_count": int(minus.size),
            "upper_matching_bound_row_count": int(plus.size),
            "lower_bound_row": int(minus[0]) if minus.size == 1 else None,
            "upper_bound_row": int(plus[0]) if plus.size == 1 else None,
        }
        if minus.size == 1 and plus.size == 1:
            lower_tolerance[j] = tolerances[int(minus[0])]
            upper_tolerance[j] = tolerances[int(plus[0])]
            item["lower_original_row_tolerance"] = float(lower_tolerance[j])
            item["upper_original_row_tolerance"] = float(upper_tolerance[j])
        else:
            complete = False
        metadata["coordinates"].append(item)
    if not complete:
        metadata.update(
            available=False,
            reason="a_tagged_literal_unit_bound_side_is_missing_or_not_unique",
        )
        return metadata

    try:
        with np.errstate(over="raise", invalid="raise"):
            lower = data["lo"] - lower_tolerance
            upper = data["hi"] + upper_tolerance
        # Fixed coordinates were exactly eliminated from the LP.  Their
        # tolerated-domain bound is explicitly the same affine subspace.
        lower[data["fixed"]] = data["lo"][data["fixed"]]
        upper[data["fixed"]] = data["hi"][data["fixed"]]
        _finite_array(lower, "dual_box_bound.tolerated_lower")
        _finite_array(upper, "dual_box_bound.tolerated_upper")
    except (FloatingPointError, _NumericalFailure) as error:
        metadata.update(
            available=False,
            reason="nonfinite_expanded_tolerated_outer_box",
            detail=str(error),
        )
        return metadata
    metadata.update(
        available=True,
        tolerated_lower=lower.tolist(),
        tolerated_upper=upper.tolist(),
    )
    return metadata


def _dual_box_bounds(data: dict, original: dict) -> dict:
    dual = original["dual"]
    bounds = _recover_tolerated_outer_box(data)
    if not bool(np.all(dual >= 0.0)):
        return {
            "available": False,
            "reason": "negative_original_dual",
            "tolerated_bounds_metadata": bounds,
        }
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        nu = float(dual @ data["A0"][:, GAMMA_INDEX])
        q = data["A0"][:, :OUTER_VARIABLES].T @ dual
        lambda_b = float(dual @ data["b0"])
        lambda_tolerance = float(dual @ data["tol"])
        strict_terms = np.where(q >= 0.0, q * data["lo"], q * data["hi"])
        strict_minimum = float(np.sum(strict_terms))
    for name, value in (
        ("nu", nu),
        ("lambda_b", lambda_b),
        ("lambda_tolerance", lambda_tolerance),
        ("strict_box_minimum", strict_minimum),
    ):
        _finite_scalar(value, "dual_box_bound." + name)
    _finite_array(q, "dual_box_bound.q")
    if nu <= 0.0:
        return {
            "available": False,
            "reason": "nonpositive_gain_coefficient",
            "nu": nu,
            "tolerated_bounds_metadata": bounds,
        }
    strict = (lambda_b - strict_minimum) / nu
    _finite_scalar(strict, "dual_box_bound.strict")
    strict_gap = _finite_scalar(
        strict - float(original["x_gamma"]), "dual_box_bound.strict_gap"
    )
    result = {
        "available": True,
        "strict_available": True,
        "tolerated_available": False,
        "units": "gamma",
        "nu": nu,
        "lambda_dot_original_b": lambda_b,
        "lambda_dot_original_tolerance": lambda_tolerance,
        "strict_outer_box_minimum": strict_minimum,
        "tolerated_outer_box_minimum": None,
        "strict_gamma_upper_bound_binary64": strict,
        "original_tolerance_gamma_upper_bound_binary64": None,
        "strict_bound_minus_last_gamma": strict_gap,
        "tolerated_bound_minus_last_gamma": None,
        "strict_outer_box": {
            "lower": data["lo"].tolist(),
            "upper": data["hi"].tolist(),
        },
        "tolerated_bounds_metadata": bounds,
        "outward_rounding": False,
        "is_rigorous_numerical_certificate": False,
    }
    if not bounds["available"]:
        result["tolerated_unavailable_reason"] = bounds["reason"]
        return result

    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            lower = np.asarray(bounds["tolerated_lower"], dtype=np.float64)
            upper = np.asarray(bounds["tolerated_upper"], dtype=np.float64)
            tolerated_terms = np.where(q >= 0.0, q * lower, q * upper)
            tolerated_minimum = float(np.sum(tolerated_terms))
            tolerated = float(
                np.divide(
                    np.add(lambda_b, lambda_tolerance) - tolerated_minimum,
                    nu,
                )
            )
        _finite_scalar(tolerated_minimum, "dual_box_bound.tolerated_box_minimum")
        _finite_scalar(tolerated, "dual_box_bound.tolerated")
        tolerated_gap = _finite_scalar(
            tolerated - float(original["x_gamma"]), "dual_box_bound.tolerated_gap"
        )
    except (FloatingPointError, _NumericalFailure) as error:
        result["tolerated_unavailable_reason"] = "nonfinite_tolerated_bound_diagnostic"
        result["tolerated_unavailable_detail"] = str(error)
        return result
    result.update(
        tolerated_available=True,
        tolerated_outer_box_minimum=tolerated_minimum,
        original_tolerance_gamma_upper_bound_binary64=tolerated,
        tolerated_bound_minus_last_gamma=tolerated_gap,
    )
    return result


def solve_paid_master(
    A: Any,
    b: Any,
    row_tol: Any,
    row_kind: Any,
    outer_lo: Any,
    outer_hi: Any,
    initial_x: Any,
    *,
    ledger: NewMasterLedger,
) -> dict:
    """Solve one finite LP; return the last accepted finite state on every stop.

    Required driver-facing fields are status, last_finite_x (161 numbers or
    None), original_unit_dual and original_unit_slack.  All rows and tolerances
    are original units.  initial_x is not projected, except literal fixed
    coordinates are replaced by their exact supplied bound values.

    A status of converged is only a binary64 finite-LP diagnostic.  It grants
    no complete-grid feasibility or actual geometric acceptance.  Other stop
    statuses do not assert infeasibility, unboundedness or stationarity.
    """
    if not isinstance(ledger, NewMasterLedger):
        raise TypeError("ledger must be the shared NewMasterLedger")
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
        data, state = _prepare(
            A, b, row_tol, row_kind, outer_lo, outer_hi, initial_x, ledger, recovery
        )
        residuals = _residuals(data, state)
        original = _original_units(data, state)
        initial_record = _summary(data, state, residuals, original)

        if data["constant_conflicts"].size:
            status = "literal_constant_row_conflict"
        elif not data["active"].size:
            status = "no_nonzero_newton_rows"
        elif _converged(residuals, original):
            status = "converged"
        else:
            status = "iteration_limit"
            for _ in range(MAX_ITERATIONS):
                iteration = ledger._begin_iteration()
                current_iteration = {
                    "iteration": iteration,
                    "started_elapsed_seconds": ledger.elapsed(),
                    "status": "started",
                    "before": _summary(data, state, residuals, original),
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
                original = _original_units(data, state)
                current_iteration["after"] = _summary(
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
            "scope": "paid finite LP only",
            "binary64_without_outward_rounding": True,
            "actual_grid_or_geometry_acceptance": False,
            "iteration_limit_is_infeasibility_proof": False,
            "regularization_or_fallback_used": False,
            "fixed_coordinates_use_literal_equality_only": True,
            "zero_rows_use_literal_zero_coefficients_only": True,
            "gamma_objective_coefficient": -1.0,
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
            "literal_fixed_values": data["lo"][data["fixed"]].tolist(),
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
            original = _original_units(data, state)
            result["original_unit_dual"] = original["dual"].tolist()
            result["original_unit_slack"] = original["slack"].tolist()
            result["original_row_residual"] = original["row_residual"].tolist()
            result["original_primal_equation_residual"] = original[
                "equation_residual"
            ].tolist()
            result["original_stationarity_before_fixed_equalities"] = original[
                "stationarity"
            ].tolist()
            result["fixed_equality_multipliers_original_units"] = original[
                "fixed_equality_multipliers"
            ].tolist()
            result["last_summary"] = _summary(data, state, residuals, original)
            original["x_gamma"] = float(state["x"][GAMMA_INDEX])
            result["dual_outer_box_bound"] = _dual_box_bounds(data, original)
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
    if ledger.elapsed() >= MAX_SECONDS and result["status"] == "converged":
        result["algorithm_status_before_result_recovery"] = "converged"
        result["status"] = "time_limit"
        limit = NewMasterLimitReached(
            "time_limit", "result_recovery.completed", ledger.elapsed()
        )
        ledger._record_failure(limit, "result_recovery.completed")
    result["ledger"] = ledger.report()
    return result
