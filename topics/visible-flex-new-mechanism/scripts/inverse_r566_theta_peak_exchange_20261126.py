#!/usr/bin/env python3
"""Identified continuation with separate FFT quadrature and real theta peaks.

The former complete uniform constraint grid is retained. Extra true angular
points use the independent Fourier oracle, with full finer-grid acceptance.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize, minimize_scalar

ORACLE_SOURCE_SHA256 = "46eea6c6da4a94c82106e8a57ff98e70bf8f85bd2d0ef35c26cb649a0ee2f0a7"
if hashlib.sha256(Path(__file__).with_name("inverse_r566_angular_oracle_20261126.py").read_bytes()).hexdigest() != ORACLE_SOURCE_SHA256:
    raise RuntimeError("theta-peak solver requires the declared arbitrary-angle source")
import inverse_r566_angular_oracle_20261126 as angular

hard, physical = angular.hard, angular.physical
SCHEMA = "r566-identified-full-grid-and-continuous-angular-peak-exchange-v1"


def constraint_groups(g, par, mean_floor, det_floor, margin, phase, extra):
    groups = hard.fields_for_geometry(g, par, mean_floor, det_floor)
    groups = {name: field - (0 if name == "positive_height" else margin)
              for name, field in groups.items()}
    flags = {name: phase == "geometry_restoration" for name in groups}
    if phase == "metric":
        norm = (g["e"] * g["e"] + 4 * g["f"] * g["f"] + 1e-24) ** .5
        groups["metric_plus"] = extra - (norm + g["e"]) / 2
        groups["metric_minus"] = extra - (norm - g["e"]) / 2
        flags.update(metric_plus=True, metric_minus=True)
    return groups, flags


class CombinedRows:
    """Old full uniform orbit rows plus every new actual peak-orbit point."""
    def __init__(self, oracle, extra_points, mean_floor, det_floor, margin,
                 phase, deadline, block_size=16):
        self.oracle, self.extra_points = oracle, extra_points
        self.mean_floor, self.det_floor, self.margin = mean_floor, det_floor, margin
        self.phase, self.deadline, self.block_size = phase, deadline, block_size
        self.key, self.values, self.jacobian = None, None, None
        self.actual_group_violation = {}
        self.actual_metric_peak = {}
        self.last_uniform_fields = None
        self.evaluations, self.jacobian_evaluations, self.block_evaluations = 0, 0, 0
        self.maximum_block_value_difference = 0.0

    def check_time(self):
        if time.monotonic() >= self.deadline:
            raise hard.EndSegment("theta-peak scientific clock reached before the next evaluation")

    def pieces(self, state, extra, derivative=False):
        sets = [(state.uniform_fields, True)]
        if self.extra_points is not None:
            sets.append((self.oracle.evaluate(state, self.extra_points), False))
        values, derivatives, extra_columns = [], [], []
        violations, metric_peaks = {}, {}
        for g, uniform in sets:
            groups, flags = constraint_groups(g, self.oracle.uniform.par, self.mean_floor,
                                             self.det_floor, self.margin, self.phase, extra)
            for (name, field), flag in zip(groups.items(), flags.values()):
                if uniform:
                    if derivative:
                        value, jac = hard.reduced_rows(field)
                    else:
                        value = angular.blocked.reduced_values(field)
                else:
                    value = field.v.ravel()
                    if derivative:
                        jac = field.d.reshape(-1, len(state.parameter_indices))
                if name not in ("metric_plus", "metric_minus"):
                    violations[name] = max(violations.get(name, 0.0), float(max(0, -np.min(value))))
                else:
                    metric_peaks[name] = max(metric_peaks.get(name, 0.0),
                                             float(extra - np.min(value)))
                # In restoration preserve the former active-row selection:
                # uniform orbit reduction occurs before adding common sigma.
                if self.phase == "geometry_restoration":
                    value = value + extra
                values.append(value)
                extra_columns.append(np.full(len(value), float(flag)))
                if derivative:
                    derivatives.append(jac)
        return (np.concatenate(values), np.vstack(derivatives) if derivative else None,
                np.concatenate(extra_columns), violations, metric_peaks)

    def fun(self, value):
        value = np.asarray(value, dtype=float)
        key = value.tobytes()
        if key == self.key:
            return self.values
        self.check_time()
        state = self.oracle.prepare(value[:-1])
        values, _, _, violations, metric_peaks = self.pieces(state, float(value[-1]))
        if not np.all(np.isfinite(values)):
            raise FloatingPointError("nonfinite actual uniform/peak constraint values")
        self.key, self.values, self.jacobian = key, values, None
        self.actual_group_violation = violations
        self.actual_metric_peak = metric_peaks
        self.last_uniform_fields = state.uniform_fields
        self.evaluations += 1
        return values

    def jac(self, value):
        value = np.asarray(value, dtype=float)
        self.fun(value)
        if self.jacobian is not None:
            return self.jacobian
        started = time.monotonic()
        size = self.oracle.uniform.size
        answer = np.empty((len(self.values), size + 1))
        for first in range(0, size, self.block_size):
            self.check_time()
            indices = np.arange(first, min(first + self.block_size, size))
            state = self.oracle.prepare(value[:-1], indices)
            reconstructed, jac, extra_column, _, _ = self.pieces(state, float(value[-1]), derivative=True)
            difference = float(np.max(np.abs(reconstructed - self.values)))
            self.maximum_block_value_difference = max(self.maximum_block_value_difference, difference)
            if difference > 1e-12 * max(1.0, float(np.max(np.abs(self.values)))):
                raise ArithmeticError("new uniform/peak block changed actual values or row order")
            answer[:, indices] = jac
            if first == 0:
                answer[:, -1] = extra_column
            self.block_evaluations += 1
            self.oracle.release()
            del state, reconstructed, jac
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError("nonfinite exact uniform/peak Jacobian")
        self.jacobian = answer
        self.jacobian_evaluations += 1
        hard.emit("THETA_PEAK_JACOBIAN", {
            "phase": self.phase, "uniform_radial_nodes": self.oracle.uniform.nr,
            "uniform_constraint_angles": self.oracle.uniform.nt,
            "extra_actual_points": 0 if self.extra_points is None else self.extra_points.size,
            "rows": len(self.values), "value_keys_this_outer": self.evaluations,
            "complete_jacobians_this_outer": self.jacobian_evaluations,
            "direction_blocks_this_outer": self.block_evaluations,
            "maximum_value_reconstruction_difference": self.maximum_block_value_difference,
            "seconds_this_jacobian": time.monotonic() - started})
        return answer


def peak_fields(g, par, mean_floor, det_floor, margin):
    groups = hard.fields_for_geometry(g, par, mean_floor, det_floor)
    fields = {name: -field + (0 if name == "positive_height" else margin)
              for name, field in groups.items()}
    norm = (g["e"] * g["e"] + 4 * g["f"] * g["f"] + 1e-24) ** .5
    fields["metric_plus"] = (norm + g["e"]) / 2
    fields["metric_minus"] = (norm - g["e"]) / 2
    return fields


def full_scan(oracle, state, mean_floor, det_floor):
    g = state.uniform_fields
    fields = hard.fields_for_geometry(g, oracle.uniform.par, mean_floor, det_floor)
    attainers = {name: hard.where_extreme(oracle.uniform, field.v, minimum=True)
                 for name, field in fields.items()}
    worst = min(attainers, key=lambda name: attainers[name]["value"])
    e, f = g["e"].v, g["f"].v
    eta = .5 * (np.abs(e) + np.sqrt(e * e + 4 * f * f))
    curvature = np.maximum(abs(g["curvature"][0].v), abs(g["curvature"][1].v))
    xyz = g["position"]
    return {"radial_nodes": oracle.uniform.nr, "theta_nodes": oracle.uniform.nt,
            "geometry_violation_max": max(0.0, -attainers[worst]["value"]),
            "worst_geometry_group": worst, "geometry_attainers": attainers,
            "eta_max": float(np.max(eta)), "eta_attainer": hard.where_extreme(oracle.uniform, eta),
            "curvature_attainer": hard.where_extreme(oracle.uniform, curvature),
            "ball_radius_max": float(np.max(np.sqrt(sum(p.v * p.v for p in xyz)))),
            "abs_y_max": float(np.max(abs(xyz[1].v))), "z_min": float(np.min(xyz[2].v)),
            "mean_E_min": float(np.min(g["Ebar"].v)), "mean_E_max": float(np.max(g["Ebar"].v)),
            "det_min": float(np.min(g["det"].v)),
            "finite_grid_only": True, "continuous_angular_peak_coverage_certified": False,
            "all_pair_reach_certified": False}


def orbit_angles(theta):
    return np.mod([theta, -theta, np.pi - theta, np.pi + theta], 2 * np.pi)


def extra_point_set(oracle, recorded_peaks):
    if not recorded_peaks:
        return None
    radial, angles = [], []
    for peak in recorded_peaks:
        index = int(np.argmin(np.abs(oracle.uniform.s - peak["s"])))
        if abs(oracle.uniform.s[index] - peak["s"]) > 1e-12:
            raise ValueError("actual peak radial position is missing from the adopted grid")
        radial.extend([index] * 4)
        angles.extend(orbit_angles(peak["theta"]).tolist())
    return oracle.points(radial, angles)


def merge_peaks(old, new):
    # Exact floating coordinate identity; no nearby peak is snapped to a grid.
    found = {(float(p["s"]).hex(), float(p["theta"]).hex()): dict(p) for p in old}
    for peak in new:
        key = (float(peak["s"]).hex(), float(peak["theta"]).hex())
        found[key] = {"s": float(peak["s"]), "theta": float(peak["theta"])}
    return [found[key] for key in sorted(found)]


def locate_peaks(oracle, state, mean_floor, det_floor, margin, metric_limit,
                 deadline, angle_tolerance=1e-10, near_band=.002, maximum_candidates=512):
    """Refine observed angular brackets; not a continuous coverage certificate."""
    fields = peak_fields(state.uniform_fields, oracle.uniform.par, mean_floor, det_floor, margin)
    nt = oracle.uniform.nt
    quarter = np.arange(nt // 4 + 1)
    orbit = np.stack((quarter, (-quarter) % nt, (nt // 2 - quarter) % nt,
                      (nt // 2 + quarter) % nt), axis=-1)
    candidates = []
    for name, field in fields.items():
        if field.v.shape[1] == 1:
            continue
        array = np.max(field.v[:, orbit], axis=-1)
        threshold = metric_limit if name.startswith("metric_") else 0.0
        band = max(near_band, .01 * max(0, metric_limit)) if name.startswith("metric_") else near_band
        maximum = np.unravel_index(int(np.argmax(array)), array.shape)
        selected = {tuple(int(x) for x in maximum)}
        for row in range(len(array)):
            line = array[row]
            previous, following = np.r_[-np.inf, line[:-1]], np.r_[line[1:], -np.inf]
            # A flat core equality is one plateau, not hundreds of distinct
            # peaks. Its endpoints still enter; all fine values remain scanned.
            local = (line >= previous) & (line >= following) & ((line > previous) | (line > following))
            selected.update((row, int(col)) for col in np.flatnonzero(local & (line >= threshold - band)))
        for row, col in sorted(selected):
            candidates.append((name, row, col, float(array[row, col])))
    if len(candidates) > maximum_candidates:
        return {"status": "candidate_capacity_not_angular_coverage", "candidate_count": len(candidates),
                "unresolved_candidate_count": len(candidates), "peaks": [], "evaluations": 0,
                "continuous_angular_coverage_certified": False}
    peaks, evaluations = [], 0
    started = time.monotonic()
    for name, row, col, sampled in candidates:
        if time.monotonic() >= deadline:
            raise hard.EndSegment("theta-peak clock reached between observed angular brackets")
        center = float(oracle.uniform.theta[col])

        def objective(theta):
            nonlocal evaluations
            if time.monotonic() >= deadline:
                raise hard.EndSegment("theta-peak clock reached inside angular localization")
            points = oracle.points([row] * 4, orbit_angles(theta))
            value = oracle.evaluate(state, points)
            fields_here = peak_fields(value, oracle.uniform.par, mean_floor, det_floor, margin)
            evaluations += 1
            return -float(np.max(fields_here[name].v))

        if col == 0 or col == nt // 4:
            theta, value, success = center, -objective(center), True
        else:
            result = minimize_scalar(objective, bounds=(float(oracle.uniform.theta[col - 1]),
                                                        float(oracle.uniform.theta[col + 1])),
                                     method="bounded", options={"xatol": angle_tolerance, "maxiter": 50})
            theta, value, success = float(result.x), -float(result.fun), bool(result.success)
            # Retain the original sampled point if finite localization did not
            # actually improve its value; a backend label is not a bound.
            if value < sampled:
                theta, value = center, -objective(center)
        peaks.append({"field": name, "s": float(oracle.uniform.s[row]), "theta": theta,
                      "value": value, "sampled_value": sampled, "localizer_success": success})
    return {"status": "observed_brackets_localized", "candidate_count": len(candidates),
            "unresolved_candidate_count": sum(not p["localizer_success"] for p in peaks),
            "peaks": peaks, "evaluations": evaluations, "elapsed_seconds": time.monotonic() - started,
            "continuous_angular_coverage_certified": False}


def observation_metrics(scan, observed, margin):
    answer = dict(scan)
    violation, eta = scan["geometry_violation_max"], scan["eta_max"]
    for peak in observed["peaks"]:
        if peak["field"].startswith("metric_"):
            eta = max(eta, peak["value"])
        else:
            violation = max(violation, peak["value"] - (0 if peak["field"] == "positive_height" else margin))
    answer["accepted_geometry_violation_max"] = max(0.0, violation)
    answer["accepted_eta_max"] = eta
    answer["observed_continuous_peak_count"] = len(observed["peaks"])
    performed = observed["status"] == "observed_brackets_localized"
    answer["observed_peak_localization_performed"] = performed
    answer["observed_peak_localization_resolved"] = performed and observed["unresolved_candidate_count"] == 0
    answer["continuous_angular_peak_coverage_certified"] = False
    return answer


def observed_grid_peaks(oracle, state, mean_floor, det_floor, margin, limits, tolerance):
    """Cheap actual fine points for unaccepted intermediate backend trials."""
    peaks = []
    for name, field in peak_fields(state.uniform_fields, oracle.uniform.par,
                                    mean_floor, det_floor, margin).items():
        array = field.v
        radial = np.max(array, axis=1)
        previous, following = np.r_[-np.inf, radial[:-1]], np.r_[radial[1:], -np.inf]
        rows = np.flatnonzero((radial >= previous) & (radial >= following)
                              & ((radial > previous) | (radial > following))
                              & (radial > limits.get(name, 0.0) + tolerance))
        for row in rows:
            col = int(np.argmax(array[row]))
            theta = 0.0 if array.shape[1] == 1 else float(oracle.uniform.theta[col])
            # Fold to the declared reflection orbit, without changing the
            # underlying four material points later inserted as constraints.
            theta = float(theta % np.pi)
            if theta > np.pi / 2:
                theta = float(np.pi - theta)
            peaks.append({"field": name, "s": float(oracle.uniform.s[row]),
                          "theta": theta, "value": float(radial[row]),
                          "source": "actual_fine_grid_point_not_continuous_localizer"})
    return peaks


def new_only(peaks, nodes, extra_peaks, fft_nodes):
    existing = {(float(p["s"]).hex(), float(p["theta"]).hex()) for p in extra_peaks}
    uniform = np.arange(fft_nodes) * (2 * np.pi / fft_nodes)
    result = []
    for peak in peaks:
        s, theta = float(peak["s"]), float(peak["theta"])
        key = (s.hex(), theta.hex())
        if key in existing:
            continue
        same_s = np.min(np.abs(nodes - s)) <= 1e-12
        nearest = int(np.rint(theta * fft_nodes / (2 * np.pi))) % fft_nodes
        if same_s and theta == uniform[nearest]:
            continue
        result.append(peak)
    return result


def quadrature_comparison(coarse_fields, fine_state, coarse_nodes, fine_nodes, tau):
    index = np.array([int(np.argmin(abs(fine_nodes - s))) for s in coarse_nodes])
    fine_fields = fine_state.uniform_fields
    stride = fine_fields["E"].v.shape[1] // coarse_fields["E"].v.shape[1]
    if stride < 1 or stride * coarse_fields["E"].v.shape[1] != fine_fields["E"].v.shape[1]:
        raise ValueError("quadrature comparison requires complete nested angular grids")
    metric_difference = max(float(np.max(abs(coarse_fields[name].v - fine_fields[name].v[index, ::stride])))
                            for name in ("e", "f"))
    mean_difference = float(np.max(abs(coarse_fields["Ebar"].v - fine_fields["Ebar"].v[index])
                                  / np.maximum(fine_fields["Ebar"].v[index], 1e-14)))
    curvature_difference = tau * max(float(np.max(abs(left.v - right.v[index, ::stride])))
                                    for left, right in zip(coarse_fields["curvature"], fine_fields["curvature"]))
    return {"same_q_nested_FFT_metric_components_difference": metric_difference,
            "same_q_relative_mean_E_difference": mean_difference,
            "same_q_tau_curvature_difference": curvature_difference,
            "comparison_is_observational_not_a_continuous_Fourier_tail_bound": True}


def check_new_interface(oracle, q, mean_floor, det_floor, margin, deadline, block_size):
    """One necessary parity and off-grid directional check in the paid run."""
    state = oracle.prepare(q)
    rows = np.unique(np.linspace(0, oracle.uniform.nr - 1, 7, dtype=int))
    columns = np.unique(np.linspace(0, oracle.uniform.nt - 1, 13, dtype=int))
    rr, cc = np.meshgrid(rows, columns, indexing="ij")
    points = oracle.points(rr.ravel(), oracle.uniform.theta[cc.ravel()])
    gathered = oracle.evaluate(state, points)
    reference_model = angular.blocked.Model(oracle.uniform.par, oracle.uniform.s, oracle.uniform.nt)
    reference = reference_model.geometry(q, differentiate=False, ignore_clock=True)
    parity = {}
    for name in ("E", "F", "e", "f", "det", "Ebar"):
        col = np.zeros_like(cc.ravel()) if reference[name].v.shape[1] == 1 else cc.ravel()
        expected = reference[name].v[rr.ravel(), col]
        parity[name] = float(np.max(abs(gathered[name].v[:, 0] - expected)))
    for i in range(2):
        expected = reference["curvature"][i].v[rr.ravel(), cc.ravel()]
        parity["curvature_" + str(i)] = float(np.max(abs(gathered["curvature"][i].v[:, 0] - expected)))
    del reference, reference_model, gathered
    if max(parity.values()) > 1e-9:
        raise ArithmeticError("new prepared uniform values failed the original-operator parity check")
    off_angles = np.mod(oracle.uniform.theta[cc.ravel()] + .371 * (2 * np.pi / oracle.uniform.nt), 2 * np.pi)
    off_points = oracle.points(rr.ravel(), off_angles)
    off_rows = angular.PointRows(oracle, off_points, "metric", mean_floor, det_floor,
                                 margin, block_size, deadline)
    x0 = np.r_[q, 1.0]
    direction = np.sin(np.arange(len(x0)) + .271)
    direction /= np.linalg.norm(direction)
    step = 1e-6
    analytic = off_rows.jac(x0) @ direction
    numeric = (off_rows.fun(x0 + step * direction) - off_rows.fun(x0 - step * direction)) / (2 * step)
    relative = float(np.linalg.norm(analytic - numeric) / max(np.linalg.norm(numeric), 1e-14))
    if relative >= 3e-4:
        raise ArithmeticError("new true-angle parameter Jacobian failed its declared directional check")
    hard.emit("THETA_PEAK_INTERFACE_CHECK", {
        "original_uniform_value_parity_max_by_field": parity,
        "off_grid_directional_relative_l2_difference": relative,
        "actual_off_grid_point_set_SHA256": off_points.identity,
        "actual_off_grid_points": off_points.size,
        "FFT_nodes_unchanged_for_all_parameter_differences": oracle.uniform.nt,
        "all_validation_work_charged_inside_this_same_optimization_run": True,
        "point_row_counts": off_rows.counts, "oracle_counts_so_far": dict(oracle.counts)})
    oracle.release()


def fine_geometry_limits(scan, margin):
    return {name: max(0.0, -entry["value"] + (0 if name == "positive_height" else margin))
            for name, entry in scan["geometry_attainers"].items()}


def backend_record(outcome):
    if outcome is None:
        return None
    return {"status": int(outcome.status), "success": bool(outcome.success),
            "message": str(outcome.message), "nit": int(outcome.nit),
            "nfev": int(outcome.nfev), "njev": int(outcome.njev),
            "extra": float(outcome.x[-1]), "q": outcome.x[:-1].tolist(),
            "backend_return_is_not_full_scan_acceptance": True}


def compact_observation(observed):
    result = {key: value for key, value in observed.items() if key != "peaks"}
    maxima = {}
    for peak in observed["peaks"]:
        if peak["field"] not in maxima or peak["value"] > maxima[peak["field"]]["value"]:
            maxima[peak["field"]] = peak
    result["maximum_observed_peak_by_field"] = maxima
    return result


def source_input(args):
    source = json.loads(args.source_state_json)
    if source.get("schema") != "identified-joint-budget-terminal-and-unapplied-grid-v1":
        raise ValueError("unknown identified joint-budget source state")
    old = source["actual_terminal_state"]
    par = hard.Parameters(**old["physical_parameters"])
    if (abs(par.ball_radius - 1.012) > 1e-14
            or abs(par.strip_half_width - (1 - .6 * par.ball_radius)) > 1e-14
            or abs(par.reach_target - .06 * par.ball_radius) > 1e-14
            or abs(par.p + par.offset - 1) > 1e-14 or par.cap_disk_radius != .22):
        raise ValueError("this scope retains the identified jointly paid physical budget")
    geo = old["geometry_parameters"]
    required_geo = {"mean_E_floor": .25, "det_floor": .1,
                    "geometry_margin": .001, "feasibility_tolerance": 1e-8}
    if geo != required_geo:
        raise ValueError("identified source hard floors, working margin or acceptance gate changed")
    actual_nodes = np.asarray(old["constraint_radial_nodes"], dtype=float)
    proposal = source["last_unapplied_grid_proposal"]
    nodes = hard.merged_nodes(np.r_[actual_nodes, proposal["constraint_radial_nodes"]], par.length)
    if any(np.min(abs(nodes - value)) > 1e-12 for value in actual_nodes):
        raise ValueError("an existing actual uniform radial constraint was lost")
    angles = int(old["constraint_theta_nodes"])
    if angles != 1536 or int(proposal["constraint_theta_nodes"]) != 2 * angles:
        raise ValueError("this identity retains actual 1536 angles and observes the unapplied 3072 proposal")
    q = np.asarray(old["q"], dtype=float)
    trust = float(old["local_step_trust"])
    if not np.all(np.isfinite(q)) or not 0 < trust <= args.maximum_trust:
        raise ValueError("invalid exact identified q or source local trust")
    return source, par, geo, q, nodes, angles, trust


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--radial-base", type=int, default=49)
    parser.add_argument("--outer", type=int, default=120)
    parser.add_argument("--maxiter", type=int, default=80)
    parser.add_argument("--maximum-radial-nodes", type=int, default=257)
    parser.add_argument("--maximum-extra-peaks", type=int, default=1024)
    parser.add_argument("--maximum-localizer-candidates", type=int, default=512)
    parser.add_argument("--block-directions", type=int, default=16)
    parser.add_argument("--point-batch-size", type=int, default=64)
    parser.add_argument("--angle-tolerance", type=float, default=1e-10)
    parser.add_argument("--peak-near-band", type=float, default=.002)
    parser.add_argument("--restoration-exchange-relative", type=float, default=.05)
    parser.add_argument("--restoration-exchange-absolute", type=float, default=1e-6)
    parser.add_argument("--metric-exchange-relative", type=float, default=.02)
    parser.add_argument("--metric-exchange-absolute", type=float, default=1e-7)
    parser.add_argument("--pending-peak-tolerance", type=float, default=1e-8)
    parser.add_argument("--nested-quadrature-tolerance", type=float, default=1e-7)
    parser.add_argument("--minimum-trust", type=float, default=1 / 256)
    parser.add_argument("--maximum-trust", type=float, default=4)
    parser.add_argument("--maximum-seconds", type=float, default=2400)
    parser.add_argument("--final-reserve-seconds", type=float, default=30)
    args = parser.parse_args()
    started = time.monotonic()
    deadline = started + args.maximum_seconds - args.final_reserve_seconds
    if (args.radial_base < 5 or args.outer < 1 or args.maxiter < 1
            or not 1 <= args.block_directions <= 81 or args.point_batch_size < 1
            or args.maximum_radial_nodes < 5 or args.maximum_extra_peaks < 1
            or args.maximum_localizer_candidates < 1
            or not 0 < args.final_reserve_seconds < args.maximum_seconds <= 2400
            or not 0 < args.minimum_trust <= args.maximum_trust <= 4
            or min(args.angle_tolerance, args.peak_near_band,
                   args.restoration_exchange_absolute, args.metric_exchange_absolute,
                   args.pending_peak_tolerance, args.nested_quadrature_tolerance) <= 0
            or min(args.restoration_exchange_relative, args.metric_exchange_relative) < 0):
        raise ValueError("invalid declared peak-exchange solver scope")
    source, par, geo, q, nodes, angles, trust = source_input(args)
    mean_floor, det_floor = geo["mean_E_floor"], geo["det_floor"]
    margin, tolerance = geo["geometry_margin"], geo["feasibility_tolerance"]
    extra_peaks, pending = [], []
    counters = {"outer_started": 0, "outer_completed": 0,
                "fine_callback_scan_attempts": 0, "fine_callback_scans_completed": 0,
                "accepted_metric_improvements": 0, "accepted_restoration_improvements": 0,
                "actual_value_keys": 0, "complete_jacobians": 0, "direction_blocks": 0,
                "maximum_block_value_difference": 0.0, "completed_continuous_localizations": 0,
                "brackets_in_completed_localizations": 0,
                "objective_evaluations_in_completed_localizations": 0,
                "backend_natural_returns": 0, "immediate_uncovered_peak_exchanges": 0,
                "pending_peak_batch_proposals": 0, "oracle_totals": {}}
    definition = {"schema": SCHEMA, "oracle_schema": angular.SCHEMA,
                  "oracle_source_sha256": ORACLE_SOURCE_SHA256,
                  "source_state": source,
                  "source_state_sha256": hashlib.sha256(args.source_state_json.encode()).hexdigest(),
                  "physical_parameters": asdict(par), "geometry_parameters": geo,
                  "solver_arguments": {k: v for k, v in vars(args).items() if k != "source_state_json"},
                  "exact_source_q_and_local_trust_retained": True,
                  "all_actual_and_last_pending_radial_positions_adopted": True,
                  "adopted_initial_radial_nodes": nodes.tolist(),
                  "actual_uniform_constraint_angles_and_FFT_nodes": angles,
                  "unapplied_old_3072_angles_are_full_fine_observations_not_old_optimized_constraints": True,
                  "new_true_angular_peaks_added_as_explicit_orbit_points": True,
                  "no_uniform_constraint_is_dropped": True,
                  "nonuniform_points_never_define_mean_E": True,
                  "one_same_run_uniform_parity_and_offgrid_directional_check": True,
                  "same_run_optimization_follows_successful_interface_check": True,
                  "current_actual_violation_covers_intermediate_infeasibility_before_exchange": True,
                  "small_uncovered_peaks_wait_for_natural_backend_return": True,
                  "all_fine_and_peak_acceptance_work_is_charged": True,
                  "unfinished_localizer_point_work_remains_in_oracle_totals_and_elapsed_seconds": True,
                  "metric_changes_during_inverse_design": True,
                  "fixed_metric_refinement_demonstrated": False,
                  "continuous_geometry_or_reach_certified": False, "README_completion_claim": False}
    hard.emit("THETA_PEAK_DEFINITION", definition)
    termination = "declared_exchange_iterations_returned_not_complete"
    latest_scan, latest_observed, last_trial, last_backend = None, None, None, None
    initial_scan = None
    checked = False
    actual_nodes = nodes.copy()
    actual_extra_peaks = []
    actual_trust = trust
    completed = 0

    def count_oracle(oracle):
        if oracle is not None:
            for key, value in oracle.counts.items():
                counters["oracle_totals"][key] = counters["oracle_totals"].get(key, 0) + value

    def observe(oracle, state, metric_limit, clock):
        observed = locate_peaks(oracle, state, mean_floor, det_floor, margin,
                                metric_limit, clock, args.angle_tolerance,
                                args.peak_near_band, args.maximum_localizer_candidates)
        counters["completed_continuous_localizations"] += 1
        counters["brackets_in_completed_localizations"] += len(observed["peaks"])
        counters["objective_evaluations_in_completed_localizations"] += observed["evaluations"]
        return observed

    def make_oracles(radial):
        coarse = angular.AngularOracle(par, radial, angles, args.point_batch_size)
        fine_nodes = hard.merged_nodes(np.r_[radial, (radial[:-1] + radial[1:]) / 2,
                                             np.linspace(0, par.length, 2 * args.radial_base - 1)], par.length)
        fine = angular.AngularOracle(par, fine_nodes, 2 * angles, args.point_batch_size)
        return coarse, fine

    for outer in range(args.outer):
        if time.monotonic() >= deadline:
            termination = "scientific_clock_checkpoint_not_complete"
            break
        if len(nodes) > args.maximum_radial_nodes or len(extra_peaks) > args.maximum_extra_peaks:
            termination = "unresolved_actual_peak_capacity_checkpoint"
            break
        coarse = fine = rows = None
        outcome = None
        callbacks = accepted = 0
        trust_scales = None
        best_q, best_scan, best_observed = q.copy(), latest_scan, latest_observed
        seed_q = q.copy()
        solver_status = "before_backend"
        pending = []
        phase = None
        counters["outer_started"] += 1
        try:
            coarse, fine = make_oracles(nodes)
            actual_nodes, actual_extra_peaks, actual_trust = nodes.copy(), list(extra_peaks), trust
            if len(q) != coarse.uniform.size:
                raise ValueError("identified source q has the wrong physical dimension")
            lower, upper = coarse.uniform.bounds()
            if np.any(q < lower - 1e-12) or np.any(q > upper + 1e-12):
                raise ValueError("identified q violates unchanged global physical boxes")
            if not checked:
                check_new_interface(coarse, q, mean_floor, det_floor, margin, deadline,
                                    args.block_directions)
                checked = True
            state = fine.prepare(q)
            scan = full_scan(fine, state, mean_floor, det_floor)
            observed = observe(fine, state, scan["eta_max"], deadline)
            current = observation_metrics(scan, observed, margin)
            if initial_scan is None:
                initial_scan = current
            best_scan, best_observed = current, observed
            latest_scan, latest_observed = current, observed
            if not current["observed_peak_localization_resolved"]:
                termination = "unresolved_initial_angular_localization_checkpoint"
                break
            phase = ("geometry_restoration" if current["accepted_geometry_violation_max"] > tolerance
                     else "metric")
            points = extra_point_set(coarse, extra_peaks)
            rows = CombinedRows(coarse, points, mean_floor, det_floor, margin,
                                phase, deadline, args.block_directions)
            # One initial value call gives actual current constraints. A new
            # peak below their current violation is covered in Phase I and
            # must not trigger an endless seed-only exchange loop.
            probe = np.r_[q, 0.0]
            rows.fun(probe)
            actual_working = dict(rows.actual_group_violation)
            extra = (max(actual_working.values()) + .01 if phase == "geometry_restoration"
                     else current["accepted_eta_max"] + args.pending_peak_tolerance)
            x0 = np.r_[q, extra]
            initial_limits = {name: extra if phase == "geometry_restoration" else 0.0
                              for name in actual_working}
            initial_limits.update(metric_plus=extra, metric_minus=extra)
            seed_candidates = [peak for peak in observed["peaks"]
                               if peak["value"] > initial_limits.get(peak["field"], 0.0)
                               + args.pending_peak_tolerance]
            if phase == "geometry_restoration":
                seed_candidates = [peak for peak in seed_candidates
                                   if not peak["field"].startswith("metric_")]
            # Initial observed deficits enter the pending batch. Fine scanning
            # and the explicit uncovered-gap rule then control exchange; a
            # moving near-active peak cannot consume an entire outer pass
            # without giving SLSQP a step.
            seed_new = new_only(seed_candidates, nodes, extra_peaks, angles)
            pending = merge_peaks(pending, seed_new)
            hard.emit("THETA_PEAK_START", {
                "outer": outer, "phase": phase, "q": q.tolist(),
                "actual_constraint_radial_nodes": nodes.tolist(),
                "actual_uniform_angles_and_FFT_nodes": angles,
                "actual_extra_peak_orbits": extra_peaks,
                "local_step_trust": trust, "initial_fine_and_observed_scan": current,
                "initial_observed_peaks": compact_observation(observed),
                "initial_current_actual_working_violation": actual_working,
                "initial_backend_extra": extra,
                "new_initial_peaks_pending_for_this_backend": seed_new,
                "tail_quadrature": fine.uniform.tail_quadrature})
            trust_scales = np.r_[np.full(2 * coarse.uniform.block, .5),
                                 np.full(par.radial_count, .2), np.full(par.radial_count, .15), .1]
            box_lower = np.maximum(lower, q - trust * trust_scales)
            box_upper = np.minimum(upper, q + trust * trust_scales)

            def callback(value, terminal=False):
                nonlocal best_q, best_scan, best_observed, pending, callbacks, accepted
                nonlocal last_trial, termination
                callbacks += 1
                counters["fine_callback_scan_attempts"] += 1
                value = np.asarray(value, dtype=float)
                trial = value[:-1].copy()
                actual_values = rows.fun(value)
                actual_violations = dict(rows.actual_group_violation)
                actual_metric_peaks = dict(rows.actual_metric_peak)
                actual_row_violation = float(max(0.0, -np.min(actual_values)))
                last_trial = {"q": trial.tolist(), "backend_extra": float(value[-1]),
                              "outer": outer, "callback": callbacks, "phase": phase,
                              "terminal_backend_point": terminal,
                              "current_actual_working_geometry_violation": actual_violations,
                              "current_actual_metric_peak_by_group": actual_metric_peaks,
                              "current_actual_constraint_violation_including_extra": actual_row_violation,
                              "full_fine_scan_completed": False, "accepted_as": "not_accepted"}
                fine_state = fine.prepare(trial)
                fine_scan = full_scan(fine, fine_state, mean_floor, det_floor)
                counters["fine_callback_scans_completed"] += 1
                fine_working = fine_geometry_limits(fine_scan, margin)
                comparison = quadrature_comparison(rows.last_uniform_fields, fine_state,
                                                   coarse.uniform.s, fine.uniform.s, par.reach_target)
                # Infeasible intermediate SQP trials are already covered by
                # their actual current constraint violation. They receive a
                # full fine scan; expensive continuous bracket localization
                # is needed for acceptance candidates and terminal points.
                potentially_accepted = (fine_scan["geometry_violation_max"] <= tolerance
                                        or terminal
                                        or (phase == "geometry_restoration"
                                            and fine_scan["geometry_violation_max"]
                                            < best_scan["accepted_geometry_violation_max"] - 1e-10))
                if potentially_accepted:
                    trial_observed = observe(fine, fine_state, float(value[-1]) if phase == "metric"
                                             else fine_scan["eta_max"], deadline)
                else:
                    trial_observed = {"status": "infeasible_trial_full_grid_only",
                                      "unresolved_candidate_count": 0, "peaks": [],
                                      "candidate_count": 0, "evaluations": 0,
                                      "continuous_angular_coverage_certified": False}
                assessment = observation_metrics(fine_scan, trial_observed, margin)
                last_trial.update({"full_fine_scan_completed": True, "fine_scan": assessment,
                                   "fine_working_geometry_violation": fine_working,
                                   "observed_peaks": compact_observation(trial_observed),
                                   "nested_quadrature_comparison": comparison})
                quadrature_ok = max(comparison[key] for key in (
                    "same_q_nested_FFT_metric_components_difference",
                    "same_q_relative_mean_E_difference", "same_q_tau_curvature_difference")) <= args.nested_quadrature_tolerance
                resolved = assessment["observed_peak_localization_resolved"]
                viable = assessment["accepted_geometry_violation_max"] <= tolerance and resolved and quadrature_ok
                if phase == "geometry_restoration":
                    accept = (potentially_accepted and resolved and quadrature_ok
                              and assessment["accepted_geometry_violation_max"]
                              < best_scan["accepted_geometry_violation_max"] - 1e-10)
                else:
                    accept = (viable and assessment["accepted_eta_max"]
                              < best_scan["accepted_eta_max"] - 1e-12)
                if accept:
                    best_q, best_scan, best_observed = trial.copy(), assessment, trial_observed
                    accepted += 1
                    label = ("finite_observed_geometry_improvement_only" if phase == "geometry_restoration"
                             else "fine_and_observed_feasible_metric_improvement")
                    counters["accepted_restoration_improvements" if phase == "geometry_restoration"
                             else "accepted_metric_improvements"] += 1
                    last_trial["accepted_as"] = label
                else:
                    label = "not_accepted"
                limits = {name: float(value[-1]) if phase == "geometry_restoration" else 0.0
                          for name in actual_violations}
                limits.update(metric_plus=float(value[-1]), metric_minus=float(value[-1]))
                grid_candidates = observed_grid_peaks(fine, fine_state, mean_floor, det_floor,
                                                       margin, limits, args.pending_peak_tolerance)
                observed_candidates = [peak for peak in trial_observed["peaks"]
                                       if peak["value"] > limits.get(peak["field"], 0.0)
                                       + args.pending_peak_tolerance]
                candidates = new_only(grid_candidates + observed_candidates, nodes, extra_peaks, angles)
                if phase == "geometry_restoration":
                    candidates = [peak for peak in candidates if not peak["field"].startswith("metric_")]
                pending = merge_peaks(pending, candidates)
                urgent = []
                for peak in candidates:
                    name = peak["field"]
                    if name.startswith("metric_"):
                        covered = max(0.0, float(value[-1]), actual_metric_peaks.get(name, 0.0))
                        gap = max(args.metric_exchange_absolute, args.metric_exchange_relative * covered)
                    else:
                        covered = (max(0.0, float(value[-1]), actual_violations.get(name, 0.0))
                                   if phase == "geometry_restoration"
                                   else actual_violations.get(name, 0.0))
                        gap = max(args.restoration_exchange_absolute,
                                  args.restoration_exchange_relative * covered)
                    if peak["value"] > covered + gap:
                        urgent.append({**peak, "current_covered_violation_or_epigraph": covered,
                                       "required_uncovered_gap": gap})
                hard.emit("THETA_PEAK_ITERATE", {
                    "outer": outer, "callback": callbacks, "phase": phase,
                    "terminal_backend_point": terminal, "backend_extra": float(value[-1]),
                    "actual_working_geometry_violation_by_group": actual_violations,
                    "actual_metric_peak_by_group": actual_metric_peaks,
                    "actual_constraint_violation_including_extra": actual_row_violation,
                    "fine_working_geometry_violation_by_group": fine_working,
                    "full_fine_geometry_violation": fine_scan["geometry_violation_max"],
                    "full_fine_eta": fine_scan["eta_max"],
                    "observed_geometry_violation": assessment["accepted_geometry_violation_max"],
                    "observed_eta": assessment["accepted_eta_max"],
                    "observed_peaks": compact_observation(trial_observed),
                    "nested_quadrature_comparison": comparison,
                    "accepted_as": label, "new_pending_peak_count": len(candidates),
                    "total_pending_peak_orbits": len(pending), "urgent_uncovered_peaks": urgent})
                if not quadrature_ok:
                    termination = "observed_FFT_quadrature_difference_requires_new_resolution_scope"
                    raise hard.EndSegment("new quadrature discrepancy checkpoint; no angular-peak density substitution")
                if potentially_accepted and not resolved:
                    termination = "unresolved_angular_localization_capacity_or_backend_checkpoint"
                    raise hard.EndSegment("observed angular localization unresolved; no new iterate accepted")
                if time.monotonic() >= deadline:
                    termination = "scientific_clock_checkpoint_not_complete"
                    raise hard.EndSegment("scientific clock reached after full fine assessment")
                if phase == "geometry_restoration" and viable:
                    best_q, best_scan, best_observed = trial.copy(), assessment, trial_observed
                    raise hard.GeometryRestored("full finer-grid and observed-point geometry restored")
                if urgent and not terminal:
                    counters["immediate_uncovered_peak_exchanges"] += 1
                    raise hard.ExchangeGrid("genuinely uncovered new fine/real-angle peak entered the actual constraints")

            objective_jac = np.zeros(len(x0))
            objective_jac[-1] = 1
            outcome = minimize(lambda value: value[-1], x0,
                               jac=lambda value: objective_jac, method="SLSQP",
                               bounds=list(zip(np.r_[box_lower, 0.0], np.r_[box_upper, np.inf])),
                               constraints={"type": "ineq", "fun": rows.fun, "jac": rows.jac},
                               callback=callback,
                               options={"maxiter": args.maxiter, "ftol": 1e-9, "disp": False})
            counters["backend_natural_returns"] += 1
            last_backend = backend_record(outcome)
            callback(outcome.x, terminal=True)
            solver_status = "backend_returned_and_terminal_point_fully_scanned"
        except hard.ExchangeGrid as error:
            solver_status = str(error)
        except hard.GeometryRestored as error:
            solver_status = str(error)
        except hard.EndSegment as error:
            solver_status = str(error)
            if termination == "declared_exchange_iterations_returned_not_complete":
                termination = "scientific_clock_checkpoint_not_complete"
        except Exception as error:
            hard.emit("THETA_PEAK_ERROR_CHECKPOINT", {
                "outer": outer, "type": type(error).__name__, "message": str(error),
                "last_accepted_or_restoration_q": best_q.tolist(), "accepted_scan": best_scan,
                "actual_constraint_radial_nodes": actual_nodes.tolist(),
                "actual_uniform_angles_and_FFT_nodes": angles,
                "actual_extra_peak_orbits": actual_extra_peaks,
                "pending_peak_orbits": pending, "last_backend_trial": last_trial,
                "last_natural_OptimizeResult": last_backend,
                "README_completion_claim": False})
            raise
        finally:
            if rows is not None:
                counters["actual_value_keys"] += rows.evaluations
                counters["complete_jacobians"] += rows.jacobian_evaluations
                counters["direction_blocks"] += rows.block_evaluations
                counters["maximum_block_value_difference"] = max(
                    counters["maximum_block_value_difference"], rows.maximum_block_value_difference)
            count_oracle(coarse)
            count_oracle(fine)
        q, latest_scan, latest_observed = best_q.copy(), best_scan, best_observed
        completed += 1
        counters["outer_completed"] += 1
        next_peaks = merge_peaks(extra_peaks, pending)
        next_nodes = hard.merged_nodes(np.r_[nodes, [peak["s"] for peak in pending]], par.length)
        step_in_box = 0.0
        if rows is not None and trust_scales is not None:
            step_in_box = float(np.max(abs(q - seed_q) / np.maximum(trust * trust_scales, 1e-14)))
        # Grid exchange is not evidence of an oversized step. It does not
        # shrink trust. A real accepted step reaching the local box expands
        # it; only a natural no-progress/no-new-constraint return shrinks it.
        if accepted and step_in_box >= .9:
            trust = min(args.maximum_trust, 1.5 * trust)
        elif outcome is not None and accepted == 0 and not pending:
            trust = max(args.minimum_trust, trust / 2)
        if pending:
            counters["pending_peak_batch_proposals"] += 1
        hard.emit("THETA_PEAK_OUTER", {
            "outer": outer, "phase": phase, "solver_status": solver_status,
            "backend_OptimizeResult": backend_record(outcome),
            "callback_scans": callbacks, "accepted_improvements": accepted,
            "last_accepted_or_restoration_q": q.tolist(), "accepted_scan": latest_scan,
            "actual_constraint_radial_nodes": actual_nodes.tolist(),
            "actual_uniform_angles_and_FFT_nodes": angles,
            "actual_extra_peak_orbits": actual_extra_peaks,
            "actual_local_step_trust": actual_trust,
            "pending_new_peak_orbits": pending,
            "proposed_next_constraint_radial_nodes": next_nodes.tolist(),
            "proposed_next_extra_peak_orbits": next_peaks,
            "proposed_next_local_step_trust": trust,
            "step_fraction_of_actual_local_box": step_in_box,
            "elapsed_seconds": time.monotonic() - started,
            "proposal_is_not_an_already_optimized_actual_state": True})
        if len(next_nodes) > args.maximum_radial_nodes or len(next_peaks) > args.maximum_extra_peaks:
            termination = "unresolved_actual_peak_capacity_checkpoint"
            break
        if termination != "declared_exchange_iterations_returned_not_complete":
            break
        if outcome is not None and accepted == 0 and not pending and trust <= args.minimum_trust:
            termination = "natural_backend_stall_without_fine_progress_or_new_peak_constraints"
            break
        # The proposed grid becomes actual only when make_oracles is entered
        # in the next outer pass. Keep final actual and pending records apart.
        nodes, extra_peaks = next_nodes, next_peaks
        del coarse, fine, rows

    # Re-evaluate the retained q on the last actually constructed full fine
    # grid. Finalization is charged, uses the reserved clock, and is neither a
    # certificate nor an authorization to erase pending points or trials.
    final_fine_nodes = hard.merged_nodes(np.r_[actual_nodes, (actual_nodes[:-1] + actual_nodes[1:]) / 2,
                                             np.linspace(0, par.length, 2 * args.radial_base - 1)], par.length)
    final_oracle = angular.AngularOracle(par, final_fine_nodes, 2 * angles, args.point_batch_size)
    final_state = final_oracle.prepare(q)
    final_scan = full_scan(final_oracle, final_state, mean_floor, det_floor)
    final_observed = {"status": "final_full_grid_only_clock_checkpoint",
                      "unresolved_candidate_count": 1, "peaks": [], "candidate_count": 0,
                      "evaluations": 0, "continuous_angular_coverage_certified": False}
    try:
        if time.monotonic() < started + args.maximum_seconds:
            final_observed = observe(final_oracle, final_state, final_scan["eta_max"],
                                     started + args.maximum_seconds)
    except hard.EndSegment:
        termination = "scientific_clock_checkpoint_during_final_peak_observation"
    final_assessment = observation_metrics(final_scan, final_observed, margin)
    count_oracle(final_oracle)
    final_pending = merge_peaks(pending, new_only(
        [peak for peak in final_observed["peaks"] if peak["value"] > (
            final_scan["eta_max"] if peak["field"].startswith("metric_") else 0.0)
            + args.pending_peak_tolerance], actual_nodes, actual_extra_peaks, angles))
    final_next_nodes = hard.merged_nodes(np.r_[actual_nodes, [peak["s"] for peak in final_pending]], par.length)
    elapsed = time.monotonic() - started
    final = {"schema": SCHEMA, "definition": definition, "termination": termination,
             "completed_outer": completed, "interface_check_passed": checked,
             "initial_full_fine_and_observed_scan": initial_scan,
             "final_full_fine_and_observed_scan": final_assessment,
             "final_observed_peaks": compact_observation(final_observed),
             "actual_terminal_state": {"schema": "theta-peak-actual-terminal-state-v1",
                 "q": q.tolist(), "physical_parameters": asdict(par), "geometry_parameters": geo,
                 "constraint_radial_nodes": actual_nodes.tolist(),
                 "uniform_constraint_angles_and_FFT_nodes": angles,
                 "extra_actual_peak_orbits": actual_extra_peaks,
                 "local_step_trust_used": actual_trust,
                 "classification": ("finite_grid_and_observed_points_geometry_feasible"
                     if final_assessment["accepted_geometry_violation_max"] <= tolerance
                     and final_assessment["observed_peak_localization_resolved"]
                     else "unqualified_finite_scan_or_restoration_input")},
             "last_unapplied_constraint_proposal": {
                 "constraint_radial_nodes": final_next_nodes.tolist(),
                 "uniform_constraint_angles_and_FFT_nodes": angles,
                 "extra_peak_orbits": merge_peaks(actual_extra_peaks, final_pending),
                 "new_pending_peak_orbits": final_pending,
                 "next_local_step_trust": trust, "not_yet_optimized": True},
             "last_backend_trial": last_trial, "last_natural_OptimizeResult": last_backend,
             "counters": counters, "total_new_scientific_seconds": elapsed,
             "prior_input_chain_scientific_seconds": source["origin"]["accumulated_input_chain_scientific_seconds"],
             "accumulated_input_chain_and_new_scientific_seconds": elapsed + source["origin"]["accumulated_input_chain_scientific_seconds"],
             "fixed_metric_refinement_demonstrated": False,
             "continuous_angular_coverage_certified": False, "continuous_reach_certified": False,
             "README_completion_claim": False}
    hard.emit("THETA_PEAK_FINAL", final)
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    hard.emit("THETA_PEAK_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
