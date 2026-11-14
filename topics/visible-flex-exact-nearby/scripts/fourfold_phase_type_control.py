#!/usr/bin/env python3
"""Floating root-network and local synchronous-target mean-control diagnostic.

Every derivative is from the same saved phase finite primitive.  Roots and
sampled signs are diagnostics, not interval proofs.  Optional trial vectors
are explicit Schur combinations with no Newton correction and never replace
the canonical checkpoint.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, linprog

from fourfold_phase_geometry import load_phase, raw_phase_data, PhaseGeometry


def bounds(value):
    return [float(np.min(value)), float(np.max(value))]


def actual_roots(geometry, solver, theta, bracket):
    lo, hi = [np.full_like(theta, value) for value in bracket]
    flo = raw_phase_data(geometry, solver, lo, theta)["delta"]
    fhi = raw_phase_data(geometry, solver, hi, theta)["delta"]
    if np.any(flo*fhi >= 0):
        raise ValueError("sampled actual roots are not all bracketed")
    sign_lo = np.sign(flo)
    root = (lo+hi)/2
    for iteration in range(50):
        data = raw_phase_data(geometry, solver, root, theta)
        left = np.sign(data["delta"]) == sign_lo
        lo, hi = np.where(left, root, lo), np.where(left, hi, root)
        step = data["delta"]/data["delta_x"]
        proposed = root-step
        bad = (proposed <= lo) | (proposed >= hi)
        proposed = np.where(bad & (np.abs(step) > 2e-13), (lo+hi)/2, proposed)
        move = proposed-root
        root = proposed
        if np.max(np.abs(move)) < 2e-13:
            break
    else:
        raise RuntimeError("sampled actual roots did not converge")
    data = raw_phase_data(geometry, solver, root, theta)
    ttheta = -data["delta_theta"]/data["delta_x"]
    c0 = -data["m"]/data["n"]
    return dict(
        actual_root_range=bounds(root), actual_roots=root.tolist(),
        actual_root_theta_derivative_range=bounds(ttheta),
        actual_K_x_at_root_range=bounds(-data["delta_x"]/data["area"]**4),
        actual_N_at_root_range=bounds(data["n"]/data["area"]),
        actual_area_at_root_range=bounds(data["area"]),
        root_transversality_range=bounds(1-c0*ttheta),
        raw_root_residual_max=float(np.max(np.abs(data["delta"]))),
        newton_iterations=iteration+1)


def root_network(geometry, solver, angles):
    theta = np.arange(angles)*(np.pi/2)/angles
    entries = []
    for bracket in ((.23, .245), (.42, .435), (.45, .465)):
        root = brentq(lambda x: float(geometry.radial_target_metric([x])[
            "target_discriminant"][0]), *bracket, xtol=5e-14)
        target = geometry.radial_target_metric([root], with_variations=True)
        actual = raw_phase_data(geometry, solver, np.full_like(theta, root), theta)
        entry = dict(bracket=list(bracket), target_root=float(root),
                     target_K_x_at_root=float(-target["minus_K_x"][0]),
                     target_D0_x_at_root=float(target["target_discriminant_x"][0]),
                     target_root_parameter_columns=(
                         -target["discriminant_columns"][:, 0]
                         /target["target_discriminant_x"][0]).tolist(),
                     actual_N_at_target_root_range=bounds(actual["n"]/actual["area"]),
                     actual_K_at_target_root_range=bounds(
                         -actual["delta"]/actual["area"]**4))
        entry.update(actual_roots(geometry, solver, theta, bracket))
        entries.append(entry)
    samples = []
    for x in (0., .1, .2, .25, .3, .4, .425, .435, .445, .455, .465, .5, .6):
        actual = raw_phase_data(geometry, solver, np.full_like(theta, x), theta)
        target = geometry.radial_target_metric([x], with_variations=True)
        samples.append(dict(x=x, target_K=float(target["K"][0]),
                            target_K_columns=(-target["minus_K_columns"][:, 0]).tolist(),
                            actual_K_range=bounds(-actual["delta"]/actual["area"]**4),
                            actual_detII_range=bounds(-actual["delta"]/actual["area"]**2),
                            actual_N_range=bounds(actual["n"]/actual["area"])))
    return dict(angles=angles, angular_period=float(np.pi/2), roots=entries,
                sign_samples=samples,
                symmetric_target_negative_components=[
                    [-entries[0]["target_root"], entries[0]["target_root"]],
                    [entries[1]["target_root"], entries[2]["target_root"]],
                    [-entries[2]["target_root"], -entries[1]["target_root"]]],
                scan_limit=[-.6, .6],
                global_two_turn_geometry_asserted=False)


def finite_body_type(geometry, solver, vector, radial_samples=1201, angles=256):
    """Dense finite-body sign scan from the frozen solver's common primitive."""
    xs = np.linspace(0., solver.length, radial_samples)
    rows = []
    for start in range(0, len(xs), 32):
        x = xs[start:start+32]
        jets = solver.geometry(vector, x, angles)[0]
        _, fx, ft, fxx, fxt, ftt = jets
        cross = np.cross(ft, fx)
        area = np.linalg.norm(cross, axis=-1)
        normal = cross/area[..., None]
        l, m, n = [np.sum(normal*field, axis=-1) for field in (fxx, fxt, ftt)]
        actual_k = (l*n-m*m)/area**2
        E = np.mean(np.sum(fx*fx, axis=-1), axis=-1)
        Ex = 2*np.mean(np.sum(fx*fxx, axis=-1), axis=-1)
        a, ap, app = [solver.mean(x, geometry.alpha, j)[:, 0] for j in range(3)]
        target_k = -app/(a*E)+ap*Ex/(2*a*E**2)
        for index, xx in enumerate(x):
            rows.append(dict(x=float(xx), target_K=float(target_k[index]),
                             actual_K_range=bounds(actual_k[index]),
                             actual_N_range=bounds(n[index]),
                             actual_area_min=float(area[index].min())))
    target_brackets = [[a["x"], b["x"]] for a, b in zip(rows[:-1], rows[1:])
                       if a["target_K"]*b["target_K"] < 0]
    first_elliptic = next((j for j, row in enumerate(rows)
                           if row["actual_K_range"][0] > 0), None)
    subsequent_nonpositive = ([] if first_elliptic is None else
                             [row for row in rows[first_elliptic:]
                              if row["actual_K_range"][0] <= 0])
    result = dict(radial_samples=radial_samples, quarter_angles=angles,
                  finite_body_interval=[0., solver.length], target_sign_change_brackets=target_brackets,
                  first_all_angle_elliptic_sample=None if first_elliptic is None else rows[first_elliptic]["x"],
                  later_nonpositive_actual_rows=subsequent_nonpositive,
                  minimum_sampled_N=min(row["actual_N_range"][0] for row in rows),
                  maximum_sampled_N=max(row["actual_N_range"][1] for row in rows),
                  rows=rows, continuous_uniqueness_proved=False)
    if len(target_brackets) == 1:
        left, right = target_brackets[0]
        target_root = brentq(lambda x: float(geometry.radial_target_metric([x])[
            "target_discriminant"][0]), left, right, xtol=5e-14)
        target = geometry.radial_target_metric([target_root])
        result["central_target_root"] = float(target_root)
        result["central_target_K_x_at_root"] = float(-target["minus_K_x"][0])
        # The surrounding broad bracket is selected from observed all-angle
        # negative/positive rows, not from the target root alone.
        lower = max((row["x"] for row in rows if row["x"] < target_root
                     and row["actual_K_range"][1] < 0), default=None)
        upper = min((row["x"] for row in rows if row["x"] > target_root
                     and row["actual_K_range"][0] > 0), default=None)
        if lower is not None and upper is not None:
            theta = np.arange(128)*(np.pi/2)/128
            result["central_actual_root_diagnostic"] = actual_roots(
                geometry, solver, theta, (lower, upper))
            result["central_actual_common_bracket"] = [lower, upper]
    return result


def local_control(geometry, solver, schur, directions, margin=.02,
                  compatibility_only=False):
    xs = np.linspace(.30, .60, 181)
    target = geometry.radial_target_metric(xs, with_variations=True)
    k = target["K"]
    dk = -target["minus_K_columns"].T
    eig, vec = np.linalg.eigh(schur)
    # Orthogonality to the largest Schur eigenvector removes the dominant
    # finite least-squares incompatibility row; it is not exact PDE solvability.
    compatibility = vec[:, -1]
    response = dict(x=xs.tolist(), target_K=k.tolist(), target_K_columns=dk.tolist(),
                    schur_eigenvalues=eig.tolist(), schur_eigenvectors=vec.tolist(),
                    removed_dominant_compatibility_row=compatibility.tolist())
    variants = [("dominant_compatibility_plane", [compatibility])]
    if not compatibility_only:
        variants.insert(0, ("all_three_means", []))
    for label, rows in variants:
        # Minimize max |d_i| with a prescribed linear curvature margin.
        inequalities = np.vstack((np.column_stack((-dk, np.zeros(len(xs)))),
                                   np.column_stack((np.eye(3), -np.ones(3))),
                                   np.column_stack((-np.eye(3), -np.ones(3)))))
        rhs = np.r_[k-margin, np.zeros(6)]
        fit = linprog([0., 0., 0., 1.], A_ub=inequalities, b_ub=rhs,
                      A_eq=None if not rows else np.column_stack((rows, np.zeros(len(rows)))),
                      b_eq=None if not rows else np.zeros(len(rows)),
                      bounds=[(None, None)]*3+[(0., None)], method="highs")
        item = dict(success=bool(fit.success), message=fit.message,
                    linear_target_margin=margin)
        if fit.success:
            d = fit.x[:3]
            variation = d@directions
            item.update(mean_increment=d.tolist(), linf_parameter_size=float(fit.x[3]),
                        predicted_K_min=float(np.min(k+dk@d)),
                        finite_linear_metric_weighted_l2=float(np.sqrt(max(0., d@schur@d))),
                        maximum_control_variation=float(np.max(np.abs(variation))),
                        dominant_compatibility_residual=float(compatibility@d))
            # The precise trial is reproducible from these three numbers and
            # the source/direction SHA; no canonical vector is overwritten.
            trial = PhaseGeometry(solver, geometry.vector+variation, geometry.nodes)
            actual_k, actual_n, actual_metric_error = [], [], []
            theta = np.arange(64)*(np.pi/2)/64
            for x in np.linspace(.30, .60, 61):
                raw = raw_phase_data(trial, solver, np.full_like(theta, x), theta)
                actual_k.append(bounds(-raw["delta"]/raw["area"]**4))
                actual_n.append(bounds(raw["n"]/raw["area"]))
                _, fx, ft, *_ = trial.paired_jets(np.full_like(theta, x), theta)
                metric = trial.radial_target_metric([x])
                actual_metric_error.append(float(max(
                    np.max(np.abs(np.sum(fx*fx, axis=-1)-metric["E"][0])),
                    np.max(np.abs(np.sum(fx*ft, axis=-1))),
                    np.max(np.abs(np.sum(ft*ft, axis=-1)-metric["a"][0]**2)))))
            trial_target = trial.radial_target_metric(xs)
            core_target = trial.radial_target_metric(np.linspace(0., .20, 41))
            item.update(exact_finite_trial_target_K_min=float(trial_target["K"].min()),
                        exact_finite_trial_target_K_max=float(trial_target["K"].max()),
                        exact_finite_trial_outer_actual_K_range=bounds(actual_k),
                        exact_finite_trial_outer_actual_N_range=bounds(actual_n),
                        exact_finite_trial_outer_metric_residual_max=max(actual_metric_error),
                        exact_finite_trial_inner_target_K_range=bounds(core_target["K"]),
                        exact_finite_trial_alpha=trial.alpha.tolist(),
                        trial_corrected_by_Newton=False)
        response[label] = item
    return response


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--directions", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--angles", type=int, default=128)
    p.add_argument("--control", action="store_true")
    p.add_argument("--margin", type=float, default=.02)
    p.add_argument("--compatibility-only", action="store_true")
    p.add_argument("--reuse-root-report", type=Path)
    p.add_argument("--trial-checkpoint", type=Path)
    p.add_argument("--trial-type-scan", action="store_true")
    args = p.parse_args()
    digest = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    with np.load(args.directions, allow_pickle=False) as z:
        metadata = json.loads(str(z["metadata"]))
        directions = z["directions"].copy()
    if metadata["checkpoint_sha256"] != digest:
        raise ValueError("source and direction candidates differ")
    geometry, solver, vector, source_metadata = load_phase(args.checkpoint, directions=directions)
    if args.reuse_root_report:
        prior = json.loads(args.reuse_root_report.read_text())
        if (prior["source_sha256"] != digest or
                prior["directions_sha256"] != hashlib.sha256(args.directions.read_bytes()).hexdigest()):
            raise ValueError("reused root report belongs to another input")
        network = prior["root_network"]
    else:
        network = root_network(geometry, solver, args.angles)
    report = dict(kind="floating_three_root_network_and_optional_local_mean_trial",
                  source_checkpoint=args.checkpoint.name, source_sha256=digest,
                  directions_file=args.directions.name,
                  directions_sha256=hashlib.sha256(args.directions.read_bytes()).hexdigest(),
                  target_convention="synchronous g0(p)=<|Fx(p)|^2> dx^2+a(p)^2 dtheta^2",
                  quarter_nodes=geometry.nodes, original_alpha=geometry.alpha.tolist(),
                  root_network=network,
                  limitations=["ordinary floating arithmetic, finite sample, no interval certificate",
                               "three actual/target positive roots are not a global tail sign proof",
                               "Schur columns are finite least-squares directions, not exact PDE tangents",
                               "trial is a linear vector increment with nonlinear geometry recomputed, no Newton correction",
                               "no exact closed flexible surface or reach certificate"])
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"progress": "three-root evidence saved",
                      "roots": [{k:v for k,v in row.items() if k != "actual_roots"}
                                for row in report["root_network"]["roots"]]}), flush=True)
    if args.control:
        report["local_control"] = local_control(
            geometry, solver, np.array(metadata["schur_matrix"]), directions,
            args.margin, args.compatibility_only)
        if args.trial_checkpoint:
            item = report["local_control"]["dominant_compatibility_plane"]
            if not item["success"]:
                raise ValueError("no compatible trial to save")
            increment = np.array(item["mean_increment"])
            trial_vector = vector+increment@directions
            trial_metadata = dict(source_metadata)
            trial_metadata.update(
                kind="floating_Schur_predictor_trial_without_Newton_not_exact_surface",
                predictor_source_checkpoint=args.checkpoint.name,
                predictor_source_sha256=digest,
                predictor_directions_file=args.directions.name,
                predictor_directions_sha256=report["directions_sha256"],
                predictor_mean_increment=increment.tolist(),
                predictor_linear_curvature_margin=args.margin,
                predictor_Newton_corrected=False)
            with np.load(args.checkpoint, allow_pickle=False) as z:
                saved = {key:z[key] for key in z.files}
            saved["vector"] = trial_vector
            saved["metadata"] = np.array(json.dumps(trial_metadata))
            np.savez_compressed(args.trial_checkpoint, **saved)
            report["saved_trial_checkpoint"] = args.trial_checkpoint.name
            report["saved_trial_sha256"] = hashlib.sha256(args.trial_checkpoint.read_bytes()).hexdigest()
            # Read-only native diagnostics: use the original solver's actual
            # finite primitive and its dense core/whole-body metric/curvature.
            solver.prepare(source_metadata["beta_waist"], gauss=3, angles=geometry.nodes)
            report["trial_whole_body_diagnostic"] = solver.diagnostic(
                trial_vector, samples=1201, angles=geometry.nodes)
            if args.trial_type_scan:
                trial_geometry = PhaseGeometry(solver, trial_vector, geometry.nodes)
                report["trial_finite_body_type"] = finite_body_type(
                    trial_geometry, solver, trial_vector)
        args.out.write_text(json.dumps(report, indent=2)+"\n")
        print(json.dumps({"progress": "local mean-control trials saved",
                          "trials": {key:value for key,value in report["local_control"].items()
                                     if key in ("all_three_means", "dominant_compatibility_plane")}}),
              flush=True)


if __name__ == "__main__":
    main()
