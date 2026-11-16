#!/usr/bin/env python3
"""Unchanged predictor/corrector algebra on each new, strictly augmented matrix.

No old finite task is resumed.  Every solve has at least the four newly paid
original rows, a new row-set identity, and debits the one exchange owner.
The original pure algebra helpers retain literal equality/zero-row handling,
original-unit residuals, exact diagonal congruence, no regularization and no
solver fallback.  Per-problem 96/192 and whole-task 3072/6144 are both charged.
"""
from __future__ import annotations
from typing import Any
import numpy as np
from frame_metric_true53_paid_master_central_path import (
    NewMasterLedger,NewMasterLimitReached,_NumericalFailure,
    _prepare,_residuals,_original_units,_summary,_converged,_newton_system,
    _max_step,_finite_scalar,_finite_array,_dual_box_bounds,
    MAX_ITERATIONS,FRACTION_TO_BOUNDARY,RESIDUAL_TOL,COMPLEMENTARITY_TOL,
    GAMMA_INDEX)
from frame_metric_true53_augmented_scope import (
    POLICY,LIMITS,AugmentedDirectionLedger,AugmentedDirectionLimit,require)
NEW_SCIENCE_LIMIT=LIMITS["science_seconds"]

class AugmentedFiniteLedger(NewMasterLedger):
    def __init__(self,owner,*,problem_binding,added_row_count):
        require(isinstance(owner,AugmentedDirectionLedger),"one new exchange owner required")
        # Metadata initialization only; no numerical task or old budget starts.
        super().__init__(owner.started)
        self.owner=owner
        self.policy=POLICY+"-one-new-finite-problem"
        self.problem_binding=problem_binding
        self.added_row_count=added_row_count
        self.outer_event=None
    def elapsed(self):
        return self.owner.elapsed()
    def check(self,stage=""):
        return self.owner.check(stage)
    def _claim_core(self):
        self.check("augmented-core.entry")
        require(self.core_calls==0,"one finite system may be attempted only once")
        self.outer_event=self.owner.claim_problem(self.problem_binding,self.added_row_count)
        self.core_calls+=1
    def _begin_iteration(self):
        self.owner.charge("finite_master_iterations")
        return super()._begin_iteration()
    def _begin_system(self,iteration,phase):
        self.owner.charge("finite_master_newton_systems")
        return super()._begin_system(iteration,phase)
    def report(self):
        # Override the inherited report: its 240-second old task is closed.
        return {
            "policy":self.policy,"problem_binding_sha256":self.problem_binding,
            "additional_original_metric_rows":self.added_row_count,
            "per_problem_limits":{"iterations":96,"newton_systems":192},
            "shared_science_limit":NEW_SCIENCE_LIMIT,
            "global_elapsed_seconds":self.elapsed(),
            "core_calls":self.core_calls,
            "iterations_started":self.iterations_started,
            "iterations_completed":self.iterations_completed,
            "newton_systems":self.newton_systems,
            "predictor_systems":self.predictor_systems,
            "corrector_systems":self.corrector_systems,
            "system_failures":self.system_failures,
            "failures":[dict(v) for v in self.failures],
            "systems":[dict(v) for v in self.system_records],
            "events":[dict(v) for v in self.events],
            "no_per_problem_time_origin_reset":True}
    def finish(self,result):
        if self.outer_event is not None and self.outer_event.get("status")=="started":
            terminal=result.get("terminal")
            self.owner.end(self.outer_event,terminal,
                           solver_status=result.get("status"),
                           iterations_started=self.iterations_started,
                           iterations_completed=self.iterations_completed,
                           newton_systems=self.newton_systems)

def solve_augmented_master(
    A: Any,
    b: Any,
    row_tol: Any,
    row_kind: Any,
    outer_lo: Any,
    outer_hi: Any,
    initial_x: Any,
    *,
    ledger: AugmentedFiniteLedger,
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
    if not isinstance(ledger, AugmentedFiniteLedger):
        raise TypeError("ledger must be one AugmentedFiniteLedger attached to the task owner")
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
        if isinstance(error, (NewMasterLimitReached, AugmentedDirectionLimit)):
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
    if ledger.elapsed() >= NEW_SCIENCE_LIMIT and result["status"] == "converged":
        result["algorithm_status_before_result_recovery"] = "converged"
        result["status"] = "time_limit"
        limit = NewMasterLimitReached(
            "time_limit", "result_recovery.completed", ledger.elapsed()
        )
        ledger._record_failure(limit, "result_recovery.completed")
    result["ledger"] = ledger.report()
    return result
