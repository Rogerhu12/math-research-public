#!/usr/bin/env python3
"""Finite Schur predictor LP with actual core second-form inequalities.

This is a floating sampled linear feasibility test. No new Newton solve and
no assertion of a nonlinear or infinite-dimensional feasible family is made.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from fourfold_phase_geometry import load_phase, raw_phase_data, PhaseGeometry
from fourfold_phase_type_control import finite_body_type


def sampled_inequalities(geometry, solver, xs, angles):
    theta = np.arange(angles)*(np.pi/2)/angles
    all_n, all_k, dn, dk = [], [], [], []
    for start in range(0, len(xs), 4):
        x = xs[start:start+4]
        xx, tt = np.broadcast_arrays(x[:, None], theta[None, :])
        raw = raw_phase_data(geometry, solver, xx.ravel(), tt.ravel(), columns=True)
        area, n, delta = raw["area"], raw["n"], raw["delta"]
        all_n.append(n/area)
        all_k.append(-delta/area**4)
        dn.append((raw["n_columns"]/area[None, :]
                   -n[None, :]*raw["area_columns"]/area[None, :]**2).T)
        dk.append((-raw["delta_columns"]/area[None, :]**4
                   +4*delta[None, :]*raw["area_columns"]/area[None, :]**5).T)
    return dict(x=np.repeat(xs, angles), theta=np.tile(theta, len(xs)),
                N=np.concatenate(all_n), K=np.concatenate(all_k),
                N_columns=np.concatenate(dn), K_columns=np.concatenate(dk))


def fit(outer_k, outer_columns, core, compatibility, *,
        target_margin=.05, n_margin=.1, core_k_margin=None,
        max_step=.1, maximize_outer=False):
    # Four variables: the three actual mean coefficients and either their
    # infinity-norm bound or the largest simultaneously achievable outer K.
    matrices, rhs = [], []
    if maximize_outer:
        matrices.append(np.column_stack((-outer_columns, np.ones(len(outer_k)))))
        rhs.append(outer_k)
        bounds = [(-max_step, max_step)]*3+[(None, None)]
        objective = [0., 0., 0., -1.]
    else:
        matrices.extend((np.column_stack((-outer_columns, np.zeros(len(outer_k)))),
                         np.column_stack((np.eye(3), -np.ones(3))),
                         np.column_stack((-np.eye(3), -np.ones(3)))))
        rhs.extend((outer_k-target_margin, np.zeros(3), np.zeros(3)))
        bounds = [(-max_step, max_step)]*3+[(0., max_step)]
        objective = [0., 0., 0., 1.]
    matrices.append(np.column_stack((core["N_columns"], np.zeros(len(core["N"])))))
    rhs.append(-n_margin-core["N"])
    if core_k_margin is not None:
        use = core["x"] <= .20+1e-12
        matrices.append(np.column_stack((core["K_columns"][use], np.zeros(np.sum(use)))))
        rhs.append(-core_k_margin-core["K"][use])
    solution = linprog(objective, A_ub=np.vstack(matrices), b_ub=np.concatenate(rhs),
                       A_eq=np.r_[compatibility, 0.][None, :], b_eq=[0.],
                       bounds=bounds, method="highs")
    result = dict(success=bool(solution.success), status=int(solution.status),
                  message=solution.message, N_upper_target=-n_margin,
                  inner_K_upper_target=None if core_k_margin is None else -core_k_margin,
                  parameter_box=max_step, maximize_outer=bool(maximize_outer))
    if solution.success:
        d = solution.x[:3]
        result.update(mean_increment=d.tolist(), objective_value=float(solution.fun),
                      predicted_outer_target_K_min=float(np.min(outer_k+outer_columns@d)),
                      predicted_core_N_max=float(np.max(core["N"]+core["N_columns"]@d)),
                      predicted_inner_K_max=float(np.max(
                          (core["K"]+core["K_columns"]@d)[core["x"] <= .20+1e-12])),
                      compatibility_residual=float(compatibility@d))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--directions", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--linear-data", type=Path)
    p.add_argument("--angles", type=int, default=128)
    p.add_argument("--evaluate-existing-report", type=Path)
    p.add_argument("--trial-checkpoint", type=Path)
    args = p.parse_args()
    digest = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    with np.load(args.directions, allow_pickle=False) as z:
        metadata = json.loads(str(z["metadata"]))
        directions = z["directions"].copy()
    if metadata["checkpoint_sha256"] != digest:
        raise ValueError("source and direction objects differ")
    geometry, solver, vector, source_metadata = load_phase(args.checkpoint, directions=directions)
    if args.evaluate_existing_report:
        report = json.loads(args.evaluate_existing_report.read_text())
        if (report["checkpoint_sha256"] != digest or
                report["directions_sha256"] != hashlib.sha256(args.directions.read_bytes()).hexdigest()):
            raise ValueError("existing report has different source geometry")
        selected = next(test for test in report["tests"]
                        if test["success"] and not test["maximize_outer"]
                        and test["N_upper_target"] == -.2
                        and test["inner_K_upper_target"] == -.02)
        increment = np.array(selected["mean_increment"])
        trial_vector = vector+increment@directions
        trial_geometry = PhaseGeometry(solver, trial_vector, geometry.nodes)
        report["selected_trial"] = dict(selected)
        report["selected_trial"]["finite_linear_metric_weighted_l2"] = float(np.sqrt(
            max(0., increment@np.array(metadata["schur_matrix"])@increment)))
        report["selected_trial"]["maximum_control_variation"] = float(np.max(abs(increment@directions)))
        report["selected_trial"]["new_alpha"] = trial_geometry.alpha.tolist()
        report["selected_trial"]["Newton_corrected"] = False
        if args.trial_checkpoint:
            trial_metadata = dict(source_metadata)
            trial_metadata.update(
                kind="floating_type_constrained_Schur_predictor_without_Newton",
                predictor_source_checkpoint=args.checkpoint.name,
                predictor_source_sha256=digest,
                predictor_directions_file=args.directions.name,
                predictor_directions_sha256=report["directions_sha256"],
                predictor_mean_increment=increment.tolist(),
                predictor_Newton_corrected=False,
                predictor_linear_constraints=selected)
            with np.load(args.checkpoint, allow_pickle=False) as z:
                saved = {key:z[key] for key in z.files}
            saved["vector"] = trial_vector
            saved["metadata"] = np.array(json.dumps(trial_metadata))
            np.savez_compressed(args.trial_checkpoint, **saved)
            report["trial_checkpoint"] = args.trial_checkpoint.name
            report["trial_sha256"] = hashlib.sha256(args.trial_checkpoint.read_bytes()).hexdigest()
        solver.prepare(source_metadata["beta_waist"], gauss=3, angles=geometry.nodes)
        report["trial_whole_body_diagnostic"] = solver.diagnostic(
            trial_vector, samples=1201, angles=geometry.nodes)
        args.out.write_text(json.dumps(report, indent=2)+"\n")
        print(json.dumps({"progress": "type-constrained predictor whole-body diagnostic",
                          "selected_trial":report["selected_trial"],
                          "diagnostic":report["trial_whole_body_diagnostic"]}), flush=True)
        report["trial_finite_body_type"] = finite_body_type(
            trial_geometry, solver, trial_vector)
        args.out.write_text(json.dumps(report, indent=2)+"\n")
        print(json.dumps({"progress": "type-constrained predictor finite-body signs",
                          "type":{k:v for k,v in report["trial_finite_body_type"].items()
                                  if k != "rows"}}), flush=True)
        return
    core = sampled_inequalities(geometry, solver, np.linspace(0., .30, 121), args.angles)
    outer = geometry.radial_target_metric(np.linspace(.3, .6, 181), with_variations=True)
    eigenvalues, eigenvectors = np.linalg.eigh(np.array(metadata["schur_matrix"]))
    compatibility = eigenvectors[:, -1]
    if args.linear_data:
        np.savez_compressed(args.linear_data, **core, outer_K=outer["K"],
                            outer_K_columns=-outer["minus_K_columns"].T,
                            compatibility_row=compatibility)
    report = dict(kind="floating_sampled_linear_core_type_and_outer_target_LP",
                  checkpoint=args.checkpoint.name, checkpoint_sha256=digest,
                  directions_sha256=hashlib.sha256(args.directions.read_bytes()).hexdigest(),
                  core_sample_shape=[121, args.angles], core_interval=[0., .30],
                  inner_K_interval=[0., .20], outer_target_interval=[.3, .6],
                  source_core_N_max=float(core["N"].max()),
                  schur_eigenvalues=eigenvalues.tolist(),
                  compatibility_row=compatibility.tolist(),
                  tests=[], limitations=[
                      "ordinary floating LP; no interval or exact Farkas certificate",
                      "finite sampled inequalities and Schur directions",
                      "compatibility row removes only the largest finite Gram eigendirection",
                      "linear feasibility does not imply actual nonlinear geometry or PDE feasibility"])
    for k_margin in (None, .02):
        for n_margin in (.02, .1, .2):
            report["tests"].append(fit(
                outer["K"], -outer["minus_K_columns"].T, core, compatibility,
                n_margin=n_margin, core_k_margin=k_margin))
            report["tests"].append(fit(
                outer["K"], -outer["minus_K_columns"].T, core, compatibility,
                n_margin=n_margin, core_k_margin=k_margin, maximize_outer=True))
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
