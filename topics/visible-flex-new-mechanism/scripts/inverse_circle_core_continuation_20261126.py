#!/usr/bin/env python3
"""A new circular-core entry, followed by explicitly changing the design core.

At p=q the core and the full background are rotationally symmetric. The
first solve therefore uses only the 17 radial variables (for radial_count=8)
and restores the same geometric inequalities as the identified hard scope.
After this actual finite-grid restoration, p is continued toward its target
and the angular variables are unlocked. Changing p or q-design coordinates
changes the metric: this is never a fixed-metric refinement calculation.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize

HARD_SOURCE_SHA256 = "befd444bfb96efc6721d1b0bad20deb25b32e915c1f789ab4d285085c2afcce4"
hard_path = Path(__file__).with_name("inverse_hard_exchange_resume_20261126.py")
if hashlib.sha256(hard_path.read_bytes()).hexdigest() != HARD_SOURCE_SHA256:
    raise RuntimeError("circular continuation requires the declared hard-row source")
import inverse_hard_exchange_resume_20261126 as hard

Model, Parameters, emit = hard.Model, hard.Parameters, hard.emit
SCHEMA = "inverse-r566-circular-core-radial-entry-and-design-continuation-v2-resolved-circle-grid"


class StageReached(RuntimeError):
    pass


class ActiveRows:
    """Exact active-column restriction, without finite-difference derivatives."""
    def __init__(self, full, fixed_q, active):
        self.full = full
        self.fixed_q = np.asarray(fixed_q, dtype=float).copy()
        self.active = np.asarray(active, dtype=int)

    def expand(self, value):
        q = self.fixed_q.copy()
        q[self.active] = np.asarray(value[:-1], dtype=float)
        return np.r_[q, float(value[-1])]

    def fun(self, value):
        return self.full.fun(self.expand(value))

    def jac(self, value):
        full_jac = self.full.jac(self.expand(value))
        return full_jac[:, np.r_[self.active, full_jac.shape[1] - 1]]


def fine_model(par, nodes, angular_nodes, original_radial_nodes):
    points = hard.merged_nodes(np.r_[nodes, (nodes[:-1] + nodes[1:]) / 2,
                                       np.linspace(0, par.length, 2 * original_radial_nodes - 1)], par.length)
    return Model(par, points, 2 * angular_nodes)


def run_stage(stage, par, q, nodes, angular_nodes, trust, circular, args, deadline):
    """Return an identified best scanned state; backend success never qualifies it."""
    q = np.asarray(q, dtype=float).copy()
    nodes = np.asarray(nodes, dtype=float).copy()
    initial_model = Model(par, nodes, angular_nodes)
    lower, upper = initial_model.bounds()
    active = np.arange(2 * initial_model.block, initial_model.size) if circular else np.arange(initial_model.size)
    if circular and np.max(np.abs(q[:2 * initial_model.block])) > 1e-14:
        raise ValueError("the circular entry must keep all angular coefficients exactly zero")
    scales = np.full(initial_model.size, .5)
    scales[2 * initial_model.block:2 * initial_model.block + par.radial_count] = .2
    scales[2 * initial_model.block + par.radial_count:-1] = .15
    scales[-1] = .1
    started = time.monotonic()
    termination = "stage_exchange_budget_returned"
    completed = 0
    totals = {"constraint_evaluations": 0, "callback_scans": 0,
              "accepted_geometry_improvements": 0, "accepted_metric_improvements": 0}
    emit("CIRCLE_CONTINUATION_STAGE_DEFINITION", {
        "stage": stage, "physical_parameters": asdict(par), "circular_entry": circular,
        "active_coordinate_indices": active.tolist(), "active_dimension": len(active),
        "initial_coordinates": q.tolist(), "constraint_radial_nodes": nodes.tolist(),
        "constraint_theta_nodes": angular_nodes, "local_step_trust": trust,
        "stage_eta_goal": args.stage_eta_goal,
        "p_is_a_design_parameter_not_the_isometric_family_parameter": True,
        "rotational_symmetry_makes_circular_entry_metric_exact_in_the_continuous_formula": circular,
        "fixed_metric_refinement_claim": False, "README_completion_claim": False})
    for outer in range(args.outer_per_stage):
        if time.monotonic() >= deadline:
            termination = "scientific_clock_checkpoint_not_complete"
            break
        coarse = Model(par, nodes, angular_nodes)
        fine = fine_model(par, nodes, angular_nodes, args.radial_nodes)
        initial, _, _ = hard.complete_scan(fine, q, args.mean_E_floor, args.det_floor,
                                           include_circles=(outer == 0))
        viable = initial["geometry_violation_max"] <= args.feasibility_tolerance
        if viable and (circular or initial["eta_max"] <= args.stage_eta_goal):
            if circular and initial["eta_max"] > 1e-9:
                raise ArithmeticError("the numerical circular model lost its exact angular metric symmetry")
            termination = "circular_geometry_restored" if circular else "stage_finite_geometry_and_design_eta_goal_reached"
            break
        phase = "geometry_restoration" if not viable else "metric"
        coarse_scan, _, _ = hard.complete_scan(coarse, q, args.mean_E_floor, args.det_floor)
        extra = (coarse_scan["geometry_violation_max"] + .01 if phase == "geometry_restoration"
                 else coarse_scan["eta_max"] + 1e-8)
        full_rows = hard.NonlinearRows(coarse, args.mean_E_floor, args.det_floor,
                                       phase, deadline, args.geometry_margin)
        rows = ActiveRows(full_rows, q, active)
        x0 = np.r_[q[active], extra]
        emit("CIRCLE_CONTINUATION_OUTER_START", {
            "stage": stage, "outer": outer, "p": par.p, "phase": phase,
            "initial_fine_scan": initial, "local_step_trust": trust,
            "constraint_radial_nodes": nodes.tolist(), "constraint_theta_nodes": angular_nodes,
            "tail_quadrature": fine.tail_quadrature})
        best_q, best_scan = q.copy(), initial
        pending_nodes, pending_angle = [], False
        callbacks, accepted = 0, 0

        def callback(value, terminal=False):
            nonlocal best_q, best_scan, pending_nodes, pending_angle, callbacks, accepted
            callbacks += 1
            full_value = rows.expand(value)
            trial = full_value[:-1]
            extra_value = float(full_value[-1])
            scan, fields, eta = hard.complete_scan(fine, trial, args.mean_E_floor, args.det_floor)
            feasible = scan["geometry_violation_max"] <= args.feasibility_tolerance
            if phase == "geometry_restoration":
                accept = scan["geometry_violation_max"] < best_scan["geometry_violation_max"] - 1e-10
            else:
                accept = feasible and scan["eta_max"] < best_scan["eta_max"] - 1e-12
            if accept:
                best_q, best_scan = trial.copy(), scan
                accepted += 1
            added, angle = hard.new_peak_nodes(
                fine, fields, eta, nodes, angular_nodes, args.feasibility_tolerance,
                metric_limit=extra_value + 1e-8 if phase == "metric" else None,
                geometry_slack=extra_value if phase == "geometry_restoration" else 0.0,
                working_margin=args.geometry_margin if phase == "geometry_restoration" else 0.0)
            pending_nodes.extend(added)
            pending_angle = pending_angle or angle
            if phase == "geometry_restoration":
                cutoff = max(args.feasibility_tolerance, args.restoration_exchange_absolute,
                             args.restoration_exchange_relative * max(0.0, extra_value))
                urgent, urgent_angle = hard.new_peak_nodes(
                    fine, fields, eta, nodes, angular_nodes, cutoff,
                    geometry_slack=extra_value, working_margin=args.geometry_margin)
            else:
                urgent, urgent_angle = hard.new_peak_nodes(
                    fine, fields, eta, nodes, angular_nodes,
                    max(args.feasibility_tolerance, args.restoration_exchange_absolute))
                cutoff = max(args.metric_exchange_absolute,
                             args.metric_exchange_relative * max(0.0, extra_value))
                extra_nodes, extra_angle = hard.new_peak_nodes(
                    fine, {}, eta, nodes, angular_nodes, cutoff, metric_limit=extra_value + 1e-8)
                urgent.extend(extra_nodes)
                urgent_angle = urgent_angle or extra_angle
            emit("CIRCLE_CONTINUATION_ITERATE", {
                "stage": stage, "outer": outer, "iteration": callbacks, "p": par.p,
                "phase": phase, "backend_extra": extra_value,
                "fine_geometry_violation": scan["geometry_violation_max"],
                "fine_eta": scan["eta_max"], "worst_geometry_group": scan["worst_geometry_group"],
                "accepted_as": ("feasibility_improvement_only" if phase == "geometry_restoration"
                                else "feasible_metric_improvement") if accept else "not_accepted",
                "new_radial_peaks": added, "angular_upgrade_needed": angle,
                "urgent_new_radial_peaks": urgent, "urgent_angular_upgrade": urgent_angle,
                "immediate_exchange_cutoff": cutoff, "terminal_backend_scan": terminal})
            if time.monotonic() >= deadline:
                raise hard.EndSegment("scientific clock reached after full fine scan")
            if phase == "geometry_restoration" and feasible:
                best_q, best_scan = trial.copy(), scan
                raise hard.GeometryRestored("fine-grid geometry restored")
            if phase == "metric" and feasible and scan["eta_max"] <= args.stage_eta_goal:
                best_q, best_scan = trial.copy(), scan
                raise StageReached("finite design stage reached its declared metric threshold")
            if urgent or urgent_angle:
                raise hard.ExchangeGrid("significant uncovered fine peak adds actual constraints")
            if terminal and (pending_nodes or pending_angle):
                raise hard.ExchangeGrid("backend returned; all pending fine peaks enter together")

        outcome = None
        try:
            objective_jac = np.zeros(len(x0))
            objective_jac[-1] = 1
            outcome = minimize(lambda value: value[-1], x0,
                jac=lambda value: objective_jac, method="SLSQP",
                bounds=list(zip(np.r_[np.maximum(lower[active], q[active] - trust * scales[active]), 0.0],
                                np.r_[np.minimum(upper[active], q[active] + trust * scales[active]), np.inf])),
                constraints={"type": "ineq", "fun": rows.fun, "jac": rows.jac},
                callback=callback, options={"maxiter": args.maxiter, "ftol": 1e-9, "disp": False})
            callback(outcome.x, terminal=True)
            status = "backend_returned"
        except (hard.ExchangeGrid, hard.GeometryRestored, StageReached) as error:
            status = str(error)
        except hard.EndSegment as error:
            status = str(error)
            termination = "scientific_clock_checkpoint_not_complete"
        except Exception as error:
            emit("CIRCLE_CONTINUATION_ERROR_CHECKPOINT", {
                "stage": stage, "outer": outer, "physical_parameters": asdict(par),
                "type": type(error).__name__, "message": str(error),
                "coordinates": best_q.tolist(), "accepted_fine_scan": best_scan,
                "README_completion_claim": False})
            raise
        q = best_q.copy()
        completed += 1
        totals["constraint_evaluations"] += full_rows.evaluations
        totals["callback_scans"] += callbacks
        totals["accepted_geometry_improvements" if phase == "geometry_restoration"
               else "accepted_metric_improvements"] += accepted
        if accepted:
            before = initial["geometry_violation_max"] if phase == "geometry_restoration" else initial["eta_max"]
            after = best_scan["geometry_violation_max"] if phase == "geometry_restoration" else best_scan["eta_max"]
            if after < .75 * before:
                trust = min(4.0, 1.5 * trust)
        else:
            trust = max(1 / 64, trust / 2)
        new_nodes = hard.merged_nodes(np.r_[nodes, pending_nodes], par.length)
        new_nt = angular_nodes * 2 if pending_angle else angular_nodes
        emit("CIRCLE_CONTINUATION_OUTER", {
            "stage": stage, "outer": outer, "p": par.p, "phase": phase,
            "solver_status": status,
            "backend_result": None if outcome is None else {
                "status": int(outcome.status), "success": bool(outcome.success),
                "message": str(outcome.message), "nit": int(outcome.nit),
                "nfev": int(outcome.nfev), "njev": int(outcome.njev), "extra": float(outcome.x[-1])},
            "callback_scans": callbacks, "accepted_scanned_improvements": accepted,
            "actual_constraint_evaluations": full_rows.evaluations,
            "coordinates": q.tolist(), "accepted_fine_scan": best_scan,
            "next_constraint_radial_nodes": new_nodes.tolist(), "next_constraint_theta_nodes": new_nt,
            "next_local_step_trust": trust, "elapsed_seconds": time.monotonic() - started})
        if len(new_nodes) > args.maximum_radial_nodes or new_nt > args.maximum_theta_nodes:
            termination = "unresolved_fine_peaks_exceed_declared_grid_capacity"
            break
        nodes, angular_nodes = new_nodes, new_nt
        if termination == "scientific_clock_checkpoint_not_complete":
            break
        if outcome is not None and not pending_nodes and not pending_angle and accepted == 0 and trust <= 1 / 64:
            termination = "backend_stalled_without_accepted_full_scan_progress"
            break
    final_model = fine_model(par, nodes, angular_nodes, args.radial_nodes)
    final, _, _ = hard.complete_scan(final_model, q, args.mean_E_floor, args.det_floor, include_circles=True)
    geo_ok = final["geometry_violation_max"] <= args.feasibility_tolerance
    stage_ok = geo_ok and (final["eta_max"] <= (1e-9 if circular else args.stage_eta_goal))
    result = {"stage": stage, "physical_parameters": asdict(par), "circular_entry": circular,
              "termination": termination, "completed_outer": completed, "totals": totals,
              "coordinates": q.tolist(), "constraint_radial_nodes": nodes.tolist(),
              "constraint_theta_nodes": angular_nodes, "local_step_trust": trust,
              "final_full_scan": final, "finite_geometry_feasible": geo_ok,
              "design_stage_qualified": stage_ok, "elapsed_seconds": time.monotonic() - started,
              "fixed_metric_refinement_claim": False, "continuous_reach_certified": False,
              "README_completion_claim": False}
    emit("CIRCLE_CONTINUATION_STAGE_FINAL", result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, default in (("radial-basis", 8), ("modes", 4), ("radial-nodes", 49),
                          ("circle-theta-nodes", 32), ("theta-nodes", 96),
                          ("outer-per-stage", 60), ("maxiter", 80), ("maximum-stages", 40),
                          ("maximum-radial-nodes", 385), ("maximum-theta-nodes", 768)):
        parser.add_argument("--" + name, type=int, default=default)
    for name, default in (("target-core-p", .8), ("core-q", .18), ("rounding-radius", .2),
                          ("length", .9), ("initial-log-radius", -.35), ("initial-cap-height", .62),
                          ("initial-p-step", .02), ("maximum-p-step", .04), ("minimum-p-step", .0005),
                          ("stage-eta-goal", 1e-4), ("mean-E-floor", .25), ("det-floor", .1),
                          ("geometry-margin", 1e-3), ("feasibility-tolerance", 1e-8),
                          ("restoration-exchange-relative", .05), ("restoration-exchange-absolute", 1e-6),
                          ("metric-exchange-relative", .02), ("metric-exchange-absolute", 1e-7),
                          ("maximum-seconds", 2400.0)):
        parser.add_argument("--" + name, type=float, default=default)
    args = parser.parse_args()
    minimum_angular_nodes = 4 * args.modes + 4
    if (args.target_core_p < args.core_q or args.core_q <= 0 or args.stage_eta_goal <= 0
            or args.mean_E_floor <= 0 or args.det_floor <= 0
            or args.circle_theta_nodes < minimum_angular_nodes or args.circle_theta_nodes % 4
            or args.theta_nodes < minimum_angular_nodes or args.theta_nodes % 4
            or not 0 < args.minimum_p_step <= args.initial_p_step <= args.maximum_p_step):
        raise ValueError("invalid circular entry or continuation range; both angular grids must resolve 4*modes+4 nodes")
    started = time.monotonic()
    deadline = started + args.maximum_seconds
    par = Parameters(p=args.core_q, q=args.core_q, offset=args.rounding_radius,
                     length=args.length, radial_count=args.radial_basis, modes=args.modes)
    knots = np.linspace(par.core_collar_end, par.length, par.radial_count - 4)
    nodes = hard.merged_nodes(np.r_[np.linspace(0, par.length, args.radial_nodes),
                                    par.core_collar_end, par.length - .08, knots], par.length)
    model = Model(par, nodes, args.circle_theta_nodes)
    q = model.initial(args.initial_cap_height)
    q[2 * model.block:2 * model.block + par.radial_count] = args.initial_log_radius
    emit("CIRCLE_CONTINUATION_DEFINITION", {
        "schema": SCHEMA, "arguments": vars(args), "hard_source_sha256": HARD_SOURCE_SHA256,
        "physical_schema": hard.physical.SCHEMA, "tail_source_sha256": hard.TAIL_SOURCE_SHA256,
        "reference_source_sha256": hard.physical.REFERENCE_SHA256,
        "fresh_circular_input_not_a_replay_of_either_anisotropic_restoration": True,
        "first_stage_only_radial_coefficients_active": True,
        "subsequent_stages_unlock_all_angular_and_radial_coefficients": True,
        "p_continuation_changes_the_design_metric": True,
        "intermediate_p_does_not_claim_the_required_displacement_ratio": True,
        "same_fixed_ball_strip_curvature_geometry_targets": True,
        "stage_eta_goal_is_not_README_completion_tolerance": True,
        "no_fixed_metric_convergence_or_continuous_reach_claim": True})
    circular = run_stage(0, par, q, nodes, args.circle_theta_nodes, 1.0, True, args, deadline)
    accepted = circular if circular["design_stage_qualified"] else None
    last = circular
    stage_summaries = [{"stage": 0, "p": par.p, "qualified": circular["design_stage_qualified"],
                        "termination": circular["termination"],
                        "geometry_violation": circular["final_full_scan"]["geometry_violation_max"],
                        "eta": circular["final_full_scan"]["eta_max"],
                        "elapsed_seconds": circular["elapsed_seconds"]}]
    termination = "circular_entry_not_yet_geometrically_qualified"
    step = args.initial_p_step
    if accepted is not None:
        termination = "declared_design_stage_budget_returned"
        for stage in range(1, args.maximum_stages):
            old_p = float(accepted["physical_parameters"]["p"])
            if old_p >= args.target_core_p - 1e-14:
                termination = "target_core_design_reached_not_README_complete"
                break
            if time.monotonic() >= deadline:
                termination = "scientific_clock_checkpoint_not_complete"
                break
            trial_p = min(args.target_core_p, old_p + step)
            par = Parameters(p=trial_p, q=args.core_q, offset=args.rounding_radius,
                             length=args.length, radial_count=args.radial_basis, modes=args.modes)
            # This is a new design input. The accepted previous-p point is only
            # an initial guess at trial_p; no isometry between those inputs is claimed.
            trial = run_stage(stage, par, accepted["coordinates"],
                              accepted["constraint_radial_nodes"],
                              max(args.theta_nodes, accepted["constraint_theta_nodes"]),
                              accepted["local_step_trust"], False, args, deadline)
            last = trial
            stage_summaries.append({"stage": stage, "p": trial_p,
                                    "qualified": trial["design_stage_qualified"],
                                    "termination": trial["termination"],
                                    "geometry_violation": trial["final_full_scan"]["geometry_violation_max"],
                                    "eta": trial["final_full_scan"]["eta_max"],
                                    "elapsed_seconds": trial["elapsed_seconds"]})
            if trial["design_stage_qualified"]:
                accepted = trial
                step = min(args.maximum_p_step, step * 1.5)
                if trial_p >= args.target_core_p - 1e-14:
                    termination = "target_core_design_reached_not_README_complete"
                    break
            else:
                if trial["termination"] == "scientific_clock_checkpoint_not_complete":
                    termination = trial["termination"]
                    break
                step /= 2
                if step < args.minimum_p_step:
                    termination = "design_continuation_step_exhausted_not_a_nonexistence_result"
                    break
    final = {"schema": SCHEMA, "arguments": vars(args), "termination": termination,
             "stage_summaries": stage_summaries, "last_qualified_design_stage": accepted,
             "last_attempted_design_stage": last,
             "next_p_step": step, "elapsed_seconds": time.monotonic() - started,
             "fixed_metric_refinement_demonstrated": False, "continuous_reach_certified": False,
             "README_completion_claim": False}
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("CIRCLE_CONTINUATION_FINAL", final)
    emit("CIRCLE_CONTINUATION_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
