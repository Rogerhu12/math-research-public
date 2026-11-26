#!/usr/bin/env python3
"""Hard geometry restoration and adaptive full-domain inverse metric search.

This new scope uses the R566 oscillatory-tail physical model. Geometry is
restored first by a uniform slack problem; only an actually scanned feasible
iterate enters metric optimization. Every optimizer callback is scanned on
the complete finer product grid. New violating radial peaks enter the next
constraint grid; unresolved angular peaks increase the whole angular grid.
Finite-grid feasibility is never a continuous reach or completion claim.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize

TAIL_SOURCE_SHA256 = "b9c778fbeafb0d9beb061b3f472b8db1661daec5a78a63eb886a8e4770574f9b"
tail_path = Path(__file__).with_name("inverse_flat_oscillatory_tail_20261126.py")
if hashlib.sha256(tail_path.read_bytes()).hexdigest() != TAIL_SOURCE_SHA256:
    raise RuntimeError("hard exchange requires the declared R566 model source")
import inverse_flat_oscillatory_tail_20261126 as physical

Model, Parameters = physical.Model, physical.Parameters
Dual, dot, emit = physical.Dual, physical.dot, physical.emit
SCHEMA = "inverse-r566-hard-geometry-adaptive-exchange-v1"


class EndSegment(RuntimeError):
    pass


class ExchangeGrid(RuntimeError):
    pass


class GeometryRestored(RuntimeError):
    pass


def merged_nodes(values, length):
    ordered = np.sort(np.asarray(values, dtype=float))
    selected = [0.0]
    for value in ordered:
        if 0 < value < length and value - selected[-1] > 1e-12 * max(1.0, length):
            selected.append(float(value))
    if length - selected[-1] <= 1e-12 * max(1.0, length):
        selected[-1] = length
    else:
        selected.append(length)
    return np.asarray(selected)


def fields_for_geometry(g, par, mean_floor, det_floor):
    x, y, z = g["position"]
    normal_z = g["normal"][2]
    return {
        "ball": 1 - dot(g["position"], g["position"]) / par.ball_radius ** 2,
        "strip": 1 - y * y / par.strip_half_width ** 2,
        "curvature_plus": 1 - par.reach_target * g["curvature"][0].absolute(),
        "curvature_minus": 1 - par.reach_target * g["curvature"][1].absolute(),
        "positive_height": (z - par.core_half_width) / par.reach_target,
        "mean_E_floor": g["Ebar"] / mean_floor - 1,
        "det_floor": g["det"] / det_floor - 1,
        "mirror_necessary": z * z / par.reach_target ** 2 - normal_z * normal_z,
    }


def reduced_rows(field):
    """An orbit minimum retains every product-grid inequality exactly.

    Each theta index belongs to one of these reflection/half-turn orbits.
    Enforcing their minima >= 0 is equivalent to enforcing all original rows,
    including floating differences. The chosen row's actual Jacobian is used.
    This is not a selected subset of unchecked constraints.
    """
    nr, nt = field.v.shape
    if nt == 1:
        return field.v.ravel(), field.d.reshape(nr, field.size)
    if nt % 4:
        raise ValueError("the complete angular grid must be divisible by four")
    j = np.arange(nt // 4 + 1)
    orbit = np.stack((j, (-j) % nt, (nt // 2 - j) % nt, (nt // 2 + j) % nt), axis=-1)
    options = field.v[:, orbit]
    choices = np.argmin(options, axis=-1)
    index = orbit[np.arange(len(j))[None, :], choices]
    radial = np.arange(nr)[:, None]
    return field.v[radial, index].ravel(), field.d[radial, index].reshape(-1, field.size)


def flatten_fields(fields):
    rows = [reduced_rows(field) for field in fields.values()]
    return np.concatenate([row[0] for row in rows]), np.vstack([row[1] for row in rows])


def where_extreme(model, array, *, minimum=False):
    flat = int(np.argmin(array) if minimum else np.argmax(array))
    row, col = np.unravel_index(flat, array.shape)
    return {"value": float(array[row, col]), "s": float(model.s[row]),
            "theta": None if array.shape[1] == 1 else float(model.theta[col]),
            "radial_index": int(row), "angular_index": int(col)}


def complete_scan(model, q, mean_floor, det_floor, include_circles=False):
    g = model.geometry(q, differentiate=False, ignore_clock=True)
    fields = fields_for_geometry(g, model.par, mean_floor, det_floor)
    attainers = {name: where_extreme(model, field.v, minimum=True) for name, field in fields.items()}
    worst_name = min(attainers, key=lambda name: attainers[name]["value"])
    violation = max(0.0, -attainers[worst_name]["value"])
    e, f = g["e"].v, g["f"].v
    eta = .5 * (np.abs(e) + np.sqrt(e * e + 4 * f * f))
    curvature = np.maximum(np.abs(g["curvature"][0].v), np.abs(g["curvature"][1].v))
    result = {"radial_nodes": model.nr, "theta_nodes": model.nt,
              "geometry_violation_max": violation, "worst_geometry_group": worst_name,
              "geometry_attainers": attainers, "eta_max": float(np.max(eta)),
              "eta_attainer": where_extreme(model, eta),
              "curvature_attainer": where_extreme(model, curvature),
              "mean_E_min": float(np.min(g["Ebar"].v)),
              "mean_E_max": float(np.max(g["Ebar"].v)),
              "det_min": float(np.min(g["det"].v)),
              "ball_radius_max": float(model.par.ball_radius * np.sqrt(max(0, 1 - attainers["ball"]["value"]))),
              "abs_y_max": float(model.par.strip_half_width * np.sqrt(max(0, 1 - attainers["strip"]["value"]))),
              "z_min": float(np.min(g["position"][2].v)),
              "area_min": float(np.min(g["area"].v)),
              "finite_grid_only": True, "all_pair_reach_certified": False}
    if include_circles:
        result["same_geometry_physical_summary"] = model.summary(q)
        result["per_circle"] = {"s": model.s.tolist(), "eta_max": np.max(eta, axis=1).tolist(),
                                "curvature_max": np.max(curvature, axis=1).tolist(),
                                "mean_E": g["Ebar"].v[:, 0].tolist(),
                                "det_min": np.min(g["det"].v, axis=1).tolist()}
    return result, fields, eta


def new_peak_nodes(scan_model, fields, eta, existing_nodes, existing_nt, tolerance,
                   metric_limit=None, geometry_slack=0.0, working_margin=0.0):
    additions = []
    angular_upgrade = False
    # During restoration, only a peak not covered by the current uniform
    # slack is a missing constraint. Negative raw slacks already below sigma
    # must not force one-step restarts and endless subdivision of the seed.
    arrays = [(name, -field.v - geometry_slack
               + (0 if name == "positive_height" else working_margin))
              for name, field in fields.items()]
    if metric_limit is not None:
        arrays.append(("metric_epigraph", eta - metric_limit))
    for name, array in arrays:
        radial_worst = np.max(array, axis=1)
        candidates = {int(np.argmax(radial_worst))}
        candidates.update(i for i in range(1, len(radial_worst) - 1)
                          if radial_worst[i] >= radial_worst[i - 1]
                          and radial_worst[i] >= radial_worst[i + 1])
        for index in sorted(candidates):
            if radial_worst[index] <= tolerance:
                continue
            s = float(scan_model.s[index])
            if np.min(np.abs(existing_nodes - s)) > 1e-10:
                additions.append(s)
            if array.shape[1] > 1:
                angle = int(np.argmax(array[index]))
                ratio = scan_model.nt // existing_nt
                coarse_angle_peak = float(np.max(array[index, ::ratio]))
                hidden_violation = coarse_angle_peak <= tolerance < radial_worst[index]
                substantial_new_peak = radial_worst[index] - coarse_angle_peak > max(
                    1e-6, .02 * max(1.0, float(radial_worst[index])))
                if angle % ratio and (hidden_violation or substantial_new_peak):
                    angular_upgrade = True
    return additions, angular_upgrade


class NonlinearRows:
    def __init__(self, model, mean_floor, det_floor, phase, deadline, margin):
        self.model, self.mean_floor, self.det_floor = model, mean_floor, det_floor
        self.phase, self.deadline = phase, deadline
        self.margin = margin
        self.key, self.values, self.jacobian = None, None, None
        self.evaluations = 0

    def evaluate(self, value):
        value = np.asarray(value, dtype=float)
        key = value.tobytes()
        if key == self.key:
            return self.values, self.jacobian
        if time.monotonic() >= self.deadline:
            raise EndSegment("scientific segment reached; retain the explicitly scanned iterate")
        q, extra = value[:-1], value[-1]
        g = self.model.geometry(q, differentiate=True, ignore_clock=True)
        groups = fields_for_geometry(g, self.model.par, self.mean_floor, self.det_floor)
        # A modest strictly stronger working target leaves interpolation room.
        # The exact core has z=wc at s=0, so height keeps its unshifted target.
        groups = {name: field - (0 if name == "positive_height" else self.margin)
                  for name, field in groups.items()}
        geo, gj = flatten_fields(groups)
        if self.phase == "geometry_restoration":
            values = geo + extra
            jacobian = np.column_stack((gj, np.ones(len(geo))))
        else:
            # A 1e-24 regularization makes this epigraph stricter by at most
            # 5e-13; it does not relax the true spectral metric inequality.
            norm = (g["e"] * g["e"] + 4 * g["f"] * g["f"] + 1e-24) ** .5
            metric = {"plus": extra - (norm + g["e"]) / 2,
                      "minus": extra - (norm - g["e"]) / 2}
            metric_values, mj = flatten_fields(metric)
            values = np.r_[geo, metric_values]
            jacobian = np.vstack((np.column_stack((gj, np.zeros(len(geo)))),
                                  np.column_stack((mj, np.ones(len(metric_values))))))
        if not np.all(np.isfinite(values)) or not np.all(np.isfinite(jacobian)):
            raise FloatingPointError("nonfinite actual hard constraints or their derivatives")
        self.key, self.values, self.jacobian = key, values, jacobian
        self.evaluations += 1
        return values, jacobian

    def fun(self, value):
        return self.evaluate(value)[0]

    def jac(self, value):
        return self.evaluate(value)[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, default in (("radial-basis", 8), ("modes", 4), ("radial-nodes", 49),
                          ("theta-nodes", 96), ("outer", 16), ("maxiter", 60),
                          ("maximum-radial-nodes", 257), ("maximum-theta-nodes", 384)):
        parser.add_argument("--" + name, type=int, default=default)
    for name, default in (("core-p", .8), ("core-q", .18), ("rounding-radius", .2),
                          ("length", .9), ("cap-height", .62), ("initial-log-radius", -.35),
                          ("mean-E-floor", .25), ("det-floor", .10),
                          ("geometry-margin", 1e-3), ("feasibility-tolerance", 1e-8),
                          ("initial-trust", 1.0), ("maximum-seconds", 2400.0)):
        parser.add_argument("--" + name, type=float, default=default)
    parser.add_argument("--directional-check", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    deadline = started + args.maximum_seconds
    par = Parameters(p=args.core_p, q=args.core_q, offset=args.rounding_radius,
                     length=args.length, radial_count=args.radial_basis, modes=args.modes)
    if args.mean_E_floor <= 0 or args.det_floor <= 0 or args.theta_nodes % 4:
        raise ValueError("positive mean/determinant floors and a multiple-of-four angular grid required")
    fixed_knots = par.core_collar_end + (par.length - par.core_collar_end) * np.linspace(
        0, 1, par.radial_count - 4)
    nodes = merged_nodes(np.r_[np.linspace(0, par.length, args.radial_nodes),
                               .46875 * par.length, par.core_collar_end,
                               par.length - physical.TAIL_EXTENT, fixed_knots], par.length)
    angular_nodes = args.theta_nodes
    baseline_model = Model(par, nodes, angular_nodes)
    q = baseline_model.initial(args.cap_height)
    q[2 * baseline_model.block:2 * baseline_model.block + par.radial_count] = args.initial_log_radius
    lower, upper = baseline_model.bounds()
    trust_scales = np.full(baseline_model.size, .5)
    trust_scales[2 * baseline_model.block:2 * baseline_model.block + par.radial_count] = .2
    trust_scales[2 * baseline_model.block + par.radial_count:-1] = .15
    trust_scales[-1] = .1
    trust = args.initial_trust
    if np.any(q < lower) or np.any(q > upper):
        raise ValueError("the explicitly new initial parameter vector violates its model bounds")
    definition = {"schema": SCHEMA, "physical_schema": physical.SCHEMA,
                  "physical_parameters": asdict(par), "solver_arguments": vars(args),
                  "tail_source_sha256": TAIL_SOURCE_SHA256,
                  "reference_source_sha256": physical.REFERENCE_SHA256,
                  "initial_q": "all zero except all log-radius coefficients and cap-height as declared",
                  "failed_previous_trial_reused": False,
                  "geometry_phase_objective": "uniform nonnegative constraint slack only",
                  "metric_phase_objective": "spectral metric epigraph subject to unrelaxed geometry rows",
                  "working_geometry_margin": "subtract declared margin from each normalized slack except positive_height",
                  "local_step_trust_scales": trust_scales.tolist(),
                  "trust_boxes_do_not_change_global_physical_parameter_bounds": True,
                  "mean_E_and_det_floors_are_radial_gauge_restrictions": True,
                  "every_callback_scans_complete_finer_product_grid": True,
                  "orbit_minima_retain_every_original_product_grid_inequality": True,
                  "frozen_metric_convergence_claim": False, "README_completion_claim": False}
    emit("HARD_EXCHANGE_DEFINITION", definition)
    completed = 0
    termination = "declared_exchange_iterations_returned"
    checked_derivative = False
    final_scan = None
    for outer in range(args.outer):
        if time.monotonic() >= deadline:
            termination = "segment_time_checkpoint_not_complete"
            break
        coarse = Model(par, nodes, angular_nodes)
        fine_nodes = merged_nodes(np.r_[nodes, (nodes[:-1] + nodes[1:]) / 2,
                                        np.linspace(0, par.length, 2 * args.radial_nodes - 1)], par.length)
        fine = Model(par, fine_nodes, 2 * angular_nodes)
        initial, initial_fields, initial_eta = complete_scan(
            fine, q, args.mean_E_floor, args.det_floor, include_circles=(outer == 0))
        coarse_seed, _, _ = complete_scan(coarse, q, args.mean_E_floor, args.det_floor)
        restoring_seed = initial["geometry_violation_max"] > args.feasibility_tolerance
        # Incorporate already observed geometric peaks before this optimizer
        # call. Do not spend successive whole outer rounds merely rediscovering
        # the same infeasible seed's moving sampled maximum.
        initial_added, initial_upgrade = new_peak_nodes(
            fine, initial_fields, initial_eta, nodes, angular_nodes, args.feasibility_tolerance,
            metric_limit=None if restoring_seed else coarse_seed["eta_max"] + 1e-8,
            geometry_slack=coarse_seed["geometry_violation_max"] + .01 if restoring_seed else 0.0,
            working_margin=args.geometry_margin if restoring_seed else 0.0)
        proposed_nodes = merged_nodes(np.r_[nodes, initial_added], par.length)
        proposed_angles = angular_nodes * 2 if initial_upgrade else angular_nodes
        if len(proposed_nodes) > args.maximum_radial_nodes or proposed_angles > args.maximum_theta_nodes:
            termination = "unresolved_initial_scan_peaks_exceed_this_segment_grid_capacity"
            break
        if initial_added or initial_upgrade:
            nodes, angular_nodes = proposed_nodes, proposed_angles
            coarse = Model(par, nodes, angular_nodes)
            fine_nodes = merged_nodes(np.r_[nodes, (nodes[:-1] + nodes[1:]) / 2,
                                            np.linspace(0, par.length, 2 * args.radial_nodes - 1)], par.length)
            fine = Model(par, fine_nodes, 2 * angular_nodes)
            initial, initial_fields, initial_eta = complete_scan(
                fine, q, args.mean_E_floor, args.det_floor, include_circles=(outer == 0))
        phase = "geometry_restoration" if initial["geometry_violation_max"] > args.feasibility_tolerance else "metric"
        emit("HARD_EXCHANGE_START", {"outer": outer, "phase": phase, "constraint_radial_nodes": nodes.tolist(),
              "constraint_theta_nodes": angular_nodes, "initial_fine_scan": initial, "coordinates": q.tolist(),
              "tail_quadrature": fine.tail_quadrature, "local_step_trust": trust})
        row_model = NonlinearRows(coarse, args.mean_E_floor, args.det_floor, phase, deadline, args.geometry_margin)
        coarse_initial, _, _ = complete_scan(coarse, q, args.mean_E_floor, args.det_floor)
        extra = (coarse_initial["geometry_violation_max"] + .01 if phase == "geometry_restoration"
                 else coarse_initial["eta_max"] + 1e-8)
        x0 = np.r_[q, extra]
        if args.directional_check and not checked_derivative:
            direction = np.sin(np.arange(len(x0)) + .37)
            direction /= np.linalg.norm(direction)
            step = 1e-6
            analytic = row_model.jac(x0) @ direction
            numeric = (row_model.fun(x0 + step * direction) - row_model.fun(x0 - step * direction)) / (2 * step)
            relative = float(np.linalg.norm(analytic - numeric) / max(np.linalg.norm(numeric), 1e-14))
            emit("HARD_EXCHANGE_DIRECTIONAL_DERIVATIVE", {"relative_l2_difference": relative,
                  "same_actual_inequalities": True, "scientific_cost_is_in_this_run": True})
            if relative >= 3e-4:
                raise ArithmeticError("hard inequality derivative failed the one declared directional check")
            checked_derivative = True
        best_q = q.copy()
        best_scan = initial
        new_nodes, upgrade_angle = [], False
        callbacks = 0
        accepted = 0

        def callback(value):
            nonlocal best_q, best_scan, new_nodes, upgrade_angle, callbacks, accepted
            callbacks += 1
            trial = np.asarray(value[:-1], dtype=float)
            scan, fields, eta = complete_scan(fine, trial, args.mean_E_floor, args.det_floor)
            viable = scan["geometry_violation_max"] <= args.feasibility_tolerance
            if phase == "geometry_restoration":
                accept = scan["geometry_violation_max"] < best_scan["geometry_violation_max"] - 1e-10
            else:
                accept = viable and scan["eta_max"] < best_scan["eta_max"] - 1e-12
            if accept:
                best_q, best_scan = trial.copy(), scan
                accepted += 1
            added, need_angle = new_peak_nodes(fine, fields, eta, nodes, angular_nodes,
                                             args.feasibility_tolerance,
                                             metric_limit=float(value[-1]) + 1e-8 if phase == "metric" else None,
                                             geometry_slack=float(value[-1]) if phase == "geometry_restoration" else 0.0,
                                             working_margin=args.geometry_margin if phase == "geometry_restoration" else 0.0)
            new_nodes.extend(added)
            upgrade_angle = upgrade_angle or need_angle
            emit("HARD_EXCHANGE_ITERATE", {"outer": outer, "iteration": callbacks, "phase": phase,
                  "backend_extra": float(value[-1]), "fine_geometry_violation": scan["geometry_violation_max"],
                  "fine_eta": scan["eta_max"], "worst_geometry_group": scan["worst_geometry_group"],
                  "accepted_as": ("feasibility_improvement_only" if phase == "geometry_restoration" else "feasible_metric_improvement") if accept else "not_accepted",
                  "new_radial_peaks": added, "angular_upgrade_needed": need_angle})
            if time.monotonic() >= deadline:
                raise EndSegment("segment ended after the full finer-grid scan")
            if phase == "geometry_restoration" and viable:
                best_q, best_scan = trial.copy(), scan
                raise GeometryRestored("fine-grid geometry restored; begin the unrelaxed metric phase")
            if added or need_angle:
                raise ExchangeGrid("finer-grid peak adds actual constraints before continuing")

        outcome = None
        try:
            objective_jac = np.zeros(len(x0))
            objective_jac[-1] = 1
            outcome = minimize(lambda value: value[-1], x0,
                               jac=lambda value: objective_jac, method="SLSQP",
                               bounds=list(zip(np.r_[np.maximum(lower, q - trust * trust_scales), 0.0],
                                               np.r_[np.minimum(upper, q + trust * trust_scales), np.inf])),
                               constraints={"type": "ineq", "fun": row_model.fun, "jac": row_model.jac},
                               callback=callback, options={"maxiter": args.maxiter, "ftol": 1e-9, "disp": False})
            # The terminal point is scanned even if this SciPy backend did
            # not issue a final callback. Backend success is not acceptance.
            callback(outcome.x)
            solver_status = "backend_returned"
        except ExchangeGrid as error:
            solver_status = str(error)
        except GeometryRestored as error:
            solver_status = str(error)
        except EndSegment as error:
            solver_status = str(error)
            termination = "segment_time_checkpoint_not_complete"
        except Exception as error:
            emit("HARD_EXCHANGE_ERROR_CHECKPOINT", {"outer": outer, "type": type(error).__name__,
                  "message": str(error), "coordinates": best_q.tolist(), "accepted_fine_scan": best_scan,
                  "geometrically_qualified": best_scan["geometry_violation_max"] <= args.feasibility_tolerance,
                  "README_completion_claim": False})
            raise
        q = best_q.copy()
        completed += 1
        final_scan = best_scan
        if accepted:
            reference_merit = initial["geometry_violation_max"] if phase == "geometry_restoration" else initial["eta_max"]
            achieved_merit = best_scan["geometry_violation_max"] if phase == "geometry_restoration" else best_scan["eta_max"]
            if achieved_merit < .75 * reference_merit:
                trust = min(4.0, 1.5 * trust)
        else:
            trust = max(1 / 64, trust / 2)
        new_grid = merged_nodes(np.r_[nodes, new_nodes], par.length)
        next_angle = angular_nodes * 2 if upgrade_angle else angular_nodes
        emit("HARD_EXCHANGE_OUTER", {"outer": outer, "phase": phase, "solver_status": solver_status,
              "backend_result": None if outcome is None else {"status": int(outcome.status),
                  "success": bool(outcome.success), "message": str(outcome.message),
                  "nit": int(outcome.nit), "nfev": int(outcome.nfev), "njev": int(outcome.njev),
                  "extra": float(outcome.x[-1])},
              "callback_scans": callbacks, "accepted_scanned_improvements": accepted,
              "actual_constraint_evaluations": row_model.evaluations,
              "accepted_fine_scan": best_scan, "coordinates": q.tolist(),
              "next_constraint_radial_nodes": new_grid.tolist(), "next_constraint_theta_nodes": next_angle,
              "next_local_step_trust": trust, "elapsed_seconds": time.monotonic() - started,
              "metric_improvement_accepted_only_after_geometry_feasible": True})
        if len(new_grid) > args.maximum_radial_nodes or next_angle > args.maximum_theta_nodes:
            termination = "unresolved_scan_peaks_exceed_this_segment_grid_capacity"
            break
        nodes, angular_nodes = new_grid, next_angle
        if termination == "segment_time_checkpoint_not_complete":
            break
        if outcome is not None and not new_nodes and not upgrade_angle and accepted == 0 and trust <= 1 / 64:
            termination = "backend_stalled_without_accepted_full_scan_progress"
            break
    final_nodes = merged_nodes(np.r_[nodes, (nodes[:-1] + nodes[1:]) / 2,
                                     np.linspace(0, par.length, 2 * args.radial_nodes - 1)], par.length)
    final_model = Model(par, final_nodes, 2 * angular_nodes)
    final_scan, _, _ = complete_scan(final_model, q, args.mean_E_floor, args.det_floor, include_circles=True)
    final = {"definition": definition, "termination": termination, "completed_outer": completed,
             "coordinates": q.tolist(), "final_full_scan": final_scan,
             "finite_scan_geometry_feasible": final_scan["geometry_violation_max"] <= args.feasibility_tolerance,
             "elapsed_seconds": time.monotonic() - started, "fixed_metric_refinement_demonstrated": False,
             "continuous_reach_certified": False, "README_completion_claim": False}
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    emit("HARD_EXCHANGE_FINAL", final)
    emit("HARD_EXCHANGE_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
