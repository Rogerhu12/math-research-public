#!/usr/bin/env python3
"""R37 principal return derivatives for actual phase/mean directions.

Fixed-x variational transport is integrated in the radial turning coordinate.
Both moving endpoints are included. All columns refer to the synchronous
target g0(p), not a homogeneous kernel with one frozen metric.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import linprog

from fourfold_phase_geometry import load_phase, raw_phase_data, preflight
from fourfold_phase_principal_map import PrincipalMap


class ParameterMap(PrincipalMap):
    def __init__(self, geometry, solver, bracket, *, direction_sha256, **kwargs):
        super().__init__(geometry, solver, bracket, **kwargs)
        target = geometry.radial_target_metric([self.root], with_variations=True)
        self.root_columns = (-target["discriminant_columns"][:, 0]
                             /target["target_discriminant_x"][0])
        self.endpoint_qbar = -.5*self.root*float(target["minus_K_x"][0])
        self.direction_sha256 = direction_sha256

    def branch(self, theta, sign, start, finish, tolerance):
        count, columns = len(theta), len(self.root_columns)
        rows = columns+2
        value = np.zeros((rows, count))
        value[0] = theta
        start_side, finish_side = np.sign(start), np.sign(finish)
        start_raw = raw_phase_data(self.geometry, self.solver,
                                  np.full_like(theta, start_side*self.root), theta)
        start_speed = -start_raw["m"]/start_raw["n"]
        def fun(tau, flat):
            self.calls += 1
            val = flat.reshape(rows, count)
            angle = val[0]
            x = self.root*np.sin(tau)
            sqk, cosine = self.ksquare(tau, x)
            qroot = sqk/cosine if cosine else np.sqrt(self.endpoint_qbar)
            raw = raw_phase_data(self.geometry, self.solver,
                                 np.full_like(angle, x), angle, columns=True)
            target = self.geometry.radial_target_metric([x], with_variations=True)
            a, at = raw["area"], raw["area_theta"]
            m, n, mt, nt = (raw[key] for key in ("m", "n", "m_theta", "n_theta"))
            self.maximum_N = max(self.maximum_N, float(np.max(n/a)))
            if np.max(n) >= 0:
                raise ValueError("N<0 chart failed in parameter transport")
            b, h = -m/n, a*a/n
            bt = -mt/n+m*nt/(n*n)
            ht = 2*a*at/n-a*a*nt/(n*n)
            bp = (-raw["m_columns"]/n[None, :]
                  +m[None, :]*raw["n_columns"]/n[None, :]**2)
            hp = (2*a[None, :]*raw["area_columns"]/n[None, :]
                  -a[None, :]**2*raw["n_columns"]/n[None, :]**2)
            kp = target["minus_K_columns"][:, 0, None]
            theta_coefficient = self.root*cosine*(bt+sign*ht*sqk)
            forcing = (self.root*cosine*bp
                       +sign*self.root*cosine*cosine*qroot*hp
                       +sign*self.root*h[None, :]*kp/(2*qroot))
            answer = np.empty_like(val)
            answer[0] = self.root*cosine*(b+sign*h*sqk)
            answer[1] = theta_coefficient
            answer[2:] = theta_coefficient[None, :]*val[2:]+forcing
            if self.progress_file and self.calls % 200 == 0:
                self.progress_file.write_text(json.dumps(dict(
                    status="running", rhs_calls=self.calls, branches=self.branches,
                    tau=float(tau), elapsed_seconds=time.monotonic()-self.started,
                    maximum_N=self.maximum_N, minimum_qbar=self.minimum_qbar))+"\n")
            return answer.ravel()
        solved = solve_ivp(fun, (start, finish), value.ravel(), method="DOP853",
                          rtol=tolerance, atol=tolerance/20,
                          max_step=abs(finish-start)/64)
        if not solved.success:
            raise RuntimeError(solved.message)
        result = solved.y[:, -1].reshape(rows, count)
        jacobian = np.exp(result[1])
        finish_raw = raw_phase_data(self.geometry, self.solver,
                                   np.full_like(theta, finish_side*self.root), result[0])
        finish_speed = -finish_raw["m"]/finish_raw["n"]
        derivative = result[2:]+self.root_columns[:, None]*(
            -jacobian*start_speed*start_side+finish_speed*finish_side)[None, :]
        self.branches += 1
        print(json.dumps(dict(progress="parameter branch completed", branch=self.branches,
                              rhs_calls=self.calls, elapsed_seconds=time.monotonic()-self.started)),
              flush=True)
        return result[0], jacobian, derivative

    def round_trip(self, theta, tolerance):
        reused = False
        if self.branch_checkpoint and self.branch_checkpoint.exists():
            with np.load(self.branch_checkpoint, allow_pickle=False) as saved:
                if (str(saved["source_sha256"]) == self.source_sha256
                        and str(saved["direction_sha256"]) == self.direction_sha256
                        and float(saved["ode_rtol"]) == tolerance
                        and np.array_equal(saved["initial_angles"], theta)):
                    middle, jac1, col1 = saved["middle"], saved["jac1"], saved["col1"]
                    self.maximum_N = max(self.maximum_N, float(saved["maximum_N"]))
                    self.minimum_qbar = min(self.minimum_qbar, float(saved["minimum_qbar"]))
                    reused = True
        if not reused:
            middle, jac1, col1 = self.branch(theta, -1., -np.pi/2, np.pi/2, tolerance)
            if self.branch_checkpoint:
                np.savez_compressed(
                    self.branch_checkpoint, source_sha256=np.array(self.source_sha256),
                    direction_sha256=np.array(self.direction_sha256), ode_rtol=np.array(tolerance),
                    initial_angles=theta, middle=middle, jac1=jac1, col1=col1,
                    maximum_N=np.array(self.maximum_N), minimum_qbar=np.array(self.minimum_qbar))
        returned, jac2, col2 = self.branch(middle, 1., np.pi/2, -np.pi/2, tolerance)
        return returned, jac1*jac2, jac2[None, :]*col1+col2


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--directions", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--progress", type=Path)
    p.add_argument("--branch-checkpoint", type=Path)
    p.add_argument("--turn-bracket", type=float, nargs=2, default=[.235, .24])
    p.add_argument("--rays", type=int, default=16)
    p.add_argument("--block-size", type=int, default=4)
    p.add_argument("--tolerance", type=float, default=2e-7)
    p.add_argument("--resume", action="store_true")
    args = p.parse_args()
    digest = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    direction_digest = hashlib.sha256(args.directions.read_bytes()).hexdigest()
    with np.load(args.directions, allow_pickle=False) as saved:
        metadata = json.loads(str(saved["metadata"]))
        unit_directions = saved["directions"].copy()
    if metadata["checkpoint_sha256"] != digest:
        raise ValueError("parameter columns and immutable geometry are different inputs")
    eig, basis = np.linalg.eigh(np.array(metadata["schur_matrix"]))
    # Compute in the eigenbasis to avoid subtracting two large transported
    # columns when measuring the very soft scale/reparametrization direction.
    directions = basis.T@unit_directions
    geometry, solver, vector, _ = load_phase(args.checkpoint, directions=directions)
    basis_digest = hashlib.sha256(directions.tobytes()).hexdigest()
    mapper = ParameterMap(
        geometry, solver, args.turn_bracket, progress_file=args.progress,
        branch_checkpoint=args.branch_checkpoint or args.out.with_suffix(".branch.npz"),
        source_sha256=digest, direction_sha256=basis_digest)
    completed, checks = [], None
    if args.resume and args.out.exists():
        previous = json.loads(args.out.read_text())
        if (previous["source_sha256"] != digest or previous["direction_sha256"] != direction_digest
                or previous["ode_rtol"] != args.tolerance or previous["requested_rays"] != args.rays):
            raise ValueError("resume source, directions, tolerance or angular grid changed")
        if previous["status"] == "complete":
            print(json.dumps(dict(progress="matching parameter map already complete")), flush=True)
            return
        completed, checks = previous["completed_blocks"], previous["geometry_preflight"]
        report = dict(previous)
        mapper.calls = previous["current_rhs_calls"]
        if completed:
            mapper.maximum_N = max(block["maximum_N"] for block in completed)
            mapper.minimum_qbar = min(block["minimum_qbar"] for block in completed)
    if checks is None:
        checks = preflight(geometry, solver, vector)
    angles = np.arange(args.rays)*(np.pi/2)/args.rays
    for first in range(sum(len(block["initial_angles"]) for block in completed),
                       args.rays, args.block_size):
        theta = angles[first:first+args.block_size]
        returned, jacobian, eigen_columns = mapper.round_trip(theta, args.tolerance)
        eigen_columns = eigen_columns.T
        unit_columns = eigen_columns@basis.T
        completed.append(dict(
            first_index=first, initial_angles=theta.tolist(), returned_angles=returned.tolist(),
            angular_derivative=jacobian.tolist(), mean_columns=unit_columns.tolist(),
            eigen_columns=eigen_columns.tolist(), maximum_N=mapper.maximum_N,
            minimum_qbar=mapper.minimum_qbar))
        report = dict(
            kind="floating_R37_synchronous_target_principal_parameter_map",
            status="partial", source_checkpoint=args.checkpoint.name, source_sha256=digest,
            direction_file=args.directions.name, direction_sha256=direction_digest,
            direction_metadata=metadata, geometry_preflight=checks,
            requested_rays=args.rays, block_size=args.block_size,
            ode_rtol=args.tolerance, target_root=mapper.root,
            eigenvalues=eig.tolist(), eigenbasis_columns=basis.tolist(),
            root_eigen_parameter_columns=mapper.root_columns.tolist(),
            angular_period=float(np.pi/2), completed_blocks=completed,
            current_rhs_calls=mapper.calls,
            parameter_convention="synchronous g0(p); finite Schur directions, not exact PDE tangents",
            limitations=["ordinary floating computation and finite angular samples",
                         "tiny binary radial reflection defect is ignored and unpaid; not an exact original-input operator map",
                         "both radial turning endpoints move with the chosen target parameters",
                         "principal graph only; amplitudes and lower phase/DtN excluded",
                         "no exact closed flex, fixed-target homogeneous kernel or reach certificate"])
        args.out.write_text(json.dumps(report, indent=2)+"\n")
        print(json.dumps(dict(progress="parameter ray block saved", first_index=first,
                              completed_rays=first+len(theta))), flush=True)
    all_columns = np.concatenate([block["mean_columns"] for block in completed])
    eigen_columns = np.concatenate([block["eigen_columns"] for block in completed])
    report.update(status="complete", initial_angles=angles.tolist(),
                  returned_angles=sum((block["returned_angles"] for block in completed), []),
                  angular_derivative=sum((block["angular_derivative"] for block in completed), []),
                  mean_columns=all_columns.tolist(), eigen_columns=eigen_columns.tolist(),
                  mean_column_ranges=np.stack((all_columns.min(axis=0), all_columns.max(axis=0)), axis=-1).tolist(),
                  eigen_column_ranges=np.stack((eigen_columns.min(axis=0), eigen_columns.max(axis=0)), axis=-1).tolist())
    # A pointwise positive parameter response implies a positive rotation twist
    # whenever an orientation-preserving smooth conjugacy exists; no conjugacy
    # is being inferred from these finite samples.
    fit = linprog([0., 0., 0., -1.],
                  A_ub=np.column_stack((-all_columns, np.ones(len(all_columns)))),
                  b_ub=np.zeros(len(all_columns)),
                  A_eq=np.r_[basis[:, -1], 0.][None, :], b_eq=[0.],
                  bounds=[(-1., 1.)]*3+[(None, None)], method="highs")
    if fit.success:
        d = fit.x[:3]
        report["dominant_compatibility_plane_positive_response"] = dict(
            mean_direction=d.tolist(), sampled_response_min=float(np.min(all_columns@d)),
            sampled_response_max=float(np.max(all_columns@d)),
            largest_Gram_row_residual=float(basis[:, -1]@d))
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key:report[key] for key in (
        "status", "target_root", "mean_column_ranges", "eigen_column_ranges",
        "dominant_compatibility_plane_positive_response") if key in report}), flush=True)


if __name__ == "__main__":
    main()
