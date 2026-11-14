#!/usr/bin/env python3
"""R37 radial-target principal map and angular derivative, no mean columns.

The source is one immutable phase checkpoint. The target metric is its true
angular E average and saved circumference a. The output is a floating
principal graph only; no amplitudes, subprincipal phase, or elliptic DtN.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from fourfold_phase_geometry import load_phase, raw_phase_data


class PrincipalMap:
    def __init__(self, geometry, solver, bracket, progress_file=None,
                 branch_checkpoint=None, source_sha256=None):
        self.geometry, self.solver = geometry, solver
        self.root = brentq(lambda x: float(geometry.radial_target_metric([x])[
            "target_discriminant"][0]), *bracket, xtol=5e-14)
        self.calls, self.minimum_qbar, self.maximum_N = 0, float("inf"), -float("inf")
        self.progress_file, self.started = progress_file, time.monotonic()
        self.branches = 0
        self.branch_checkpoint = branch_checkpoint
        self.source_sha256 = source_sha256

    def ksquare(self, tau, x):
        s, cosine = np.sin(tau), max(0., float(np.cos(tau)))
        if abs(abs(tau)-np.pi/2) < 1e-13:
            s, cosine = np.sign(tau), 0.
        if abs(s) < .999:
            k = float(self.geometry.radial_target_metric([x])["minus_K"][0])
            qbar = k/(1-s*s)
        else:
            nodes = (np.array([-np.sqrt(3/5), 0., np.sqrt(3/5)])+1)/2
            weights = np.array([5/18, 4/9, 5/18])
            xx = self.root*(1-nodes*(1-abs(s)))
            derivative = self.geometry.radial_target_metric(xx)["minus_K_x"]
            qbar = -self.root*float(weights@derivative)/(1+abs(s))
        self.minimum_qbar = min(self.minimum_qbar, qbar)
        if qbar <= 0:
            raise ValueError("target left the central hyperbolic interval")
        return cosine*np.sqrt(qbar), cosine

    def branch(self, theta, sign, start, finish, tolerance):
        count = len(theta)
        value = np.vstack((theta, np.zeros_like(theta)))
        def fun(tau, flat):
            self.calls += 1
            angle, _ = flat.reshape(2, count)
            x = self.root*np.sin(tau)
            sqk, cosine = self.ksquare(tau, x)
            raw = raw_phase_data(self.geometry, self.solver,
                                 np.full_like(angle, x), angle)
            a, at = raw["area"], raw["area_theta"]
            m, n, mt, nt = (raw[k] for k in ("m", "n", "m_theta", "n_theta"))
            self.maximum_N = max(self.maximum_N, float(np.max(n/a)))
            if np.max(n) >= 0:
                raise ValueError("actual N<0 chart failed along a principal ray")
            # sqrt(Delta_hat)=A^2 sqrt(-K0), with K0 independent of theta.
            speed = (-m+sign*a*a*sqk)/n
            derivative = (-mt/n+m*nt/(n*n)
                          +sign*sqk*(2*a*at/n-a*a*nt/(n*n)))
            factor = self.root*cosine
            answer = np.vstack((factor*speed, factor*derivative))
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
        result = solved.y[:, -1].reshape(2, count)
        self.branches += 1
        print(json.dumps(dict(progress="principal branch completed", branch=self.branches,
                              rhs_calls=self.calls, elapsed_seconds=time.monotonic()-self.started)),
              flush=True)
        return result[0], result[1]

    def round_trip(self, theta, tolerance):
        reused = False
        if self.branch_checkpoint and self.branch_checkpoint.exists():
            with np.load(self.branch_checkpoint, allow_pickle=False) as saved:
                if (str(saved["source_sha256"]) == self.source_sha256
                        and float(saved["ode_rtol"]) == tolerance
                        and np.array_equal(saved["initial_angles"], theta)):
                    middle, logj1 = saved["middle"], saved["logj1"]
                    self.maximum_N = max(self.maximum_N, float(saved["maximum_N"]))
                    self.minimum_qbar = min(self.minimum_qbar, float(saved["minimum_qbar"]))
                    reused = True
        if not reused:
            middle, logj1 = self.branch(theta, -1., -np.pi/2, np.pi/2, tolerance)
            if self.branch_checkpoint:
                np.savez_compressed(self.branch_checkpoint,
                                    source_sha256=np.array(self.source_sha256),
                                    ode_rtol=np.array(tolerance), initial_angles=theta,
                                    middle=middle, logj1=logj1,
                                    maximum_N=np.array(self.maximum_N),
                                    minimum_qbar=np.array(self.minimum_qbar))
        final, logj2 = self.branch(middle, 1., np.pi/2, -np.pi/2, tolerance)
        return final, np.exp(logj1+logj2)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--progress", type=Path)
    p.add_argument("--turn-bracket", type=float, nargs=2, default=[.235, .24])
    p.add_argument("--rays", type=int, default=64)
    p.add_argument("--tolerance", type=float, default=2e-7)
    p.add_argument("--block-size", type=int, default=8)
    p.add_argument("--resume", action="store_true")
    p.add_argument("--branch-checkpoint", type=Path)
    args = p.parse_args()
    geometry, solver, _, _ = load_phase(args.checkpoint)
    digest = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    branch_file = args.branch_checkpoint or args.out.with_suffix(".branch.npz")
    mapper = PrincipalMap(geometry, solver, args.turn_bracket, args.progress,
                          branch_file, digest)
    angles = np.arange(args.rays)*(np.pi/2)/args.rays
    completed = []
    if args.resume and args.out.exists():
        previous = json.loads(args.out.read_text())
        if (previous["source_sha256"] != digest or previous["ode_rtol"] != args.tolerance
                or previous["requested_rays"] != args.rays):
            raise ValueError("resume output uses a different immutable input or grid")
        if previous["status"] == "complete":
            print(json.dumps(dict(progress="matching complete map already saved", output=str(args.out))),
                  flush=True)
            return
        completed = previous.get("completed_blocks", [])
        mapper.calls = int(previous.get("current_rhs_calls", 0))
        if completed:
            mapper.maximum_N = max(block["maximum_N"] for block in completed)
            mapper.minimum_qbar = min(block["minimum_qbar"] for block in completed)
    start = sum(len(block["initial_angles"]) for block in completed)
    for first in range(start, args.rays, args.block_size):
        block_angles = angles[first:first+args.block_size]
        returned, jacobian = mapper.round_trip(block_angles, args.tolerance)
        completed.append(dict(first_index=first, initial_angles=block_angles.tolist(),
                              returned_angles=returned.tolist(),
                              angular_derivative=jacobian.tolist(),
                              maximum_N=mapper.maximum_N,
                              minimum_qbar=mapper.minimum_qbar))
        partial = dict(status="partial", source_checkpoint=args.checkpoint.name,
                       source_sha256=digest, ode_rtol=args.tolerance,
                       requested_rays=args.rays, block_size=args.block_size,
                       completed_blocks=completed, target_root=mapper.root,
                       current_rhs_calls=mapper.calls,
                       limitations="floating central principal graph only, not PDE scattering or proof")
        args.out.write_text(json.dumps(partial, indent=2)+"\n")
        print(json.dumps(dict(progress="completed ray block saved", first_index=first,
                              completed_rays=first+len(block_angles))), flush=True)
    returned = np.concatenate([block["returned_angles"] for block in completed])
    jacobian = np.concatenate([block["angular_derivative"] for block in completed])
    report = dict(
        kind="floating_R37_central_principal_map_and_angular_derivative",
        status="complete", source_checkpoint=args.checkpoint.name,
        source_sha256=digest, requested_rays=args.rays, block_size=args.block_size,
        completed_blocks=completed,
        angular_period=float(np.pi/2), target_root=mapper.root,
        target="E=<|Fx|^2>, a=saved circumference radius; frozen for this map",
        raw_modified_discriminant="Delta_hat=(-K0)*G_actual^2",
        initial_angles=angles.tolist(), returned_angles=returned.tolist(),
        angular_derivative=jacobian.tolist(),
        displacement_range=[float(np.min(returned-angles)), float(np.max(returned-angles))],
        angular_derivative_range=[float(jacobian.min()), float(jacobian.max())],
        maximum_sampled_N_on_rays=mapper.maximum_N,
        minimum_radial_qbar=mapper.minimum_qbar, rhs_calls=mapper.calls,
        elapsed_seconds=time.monotonic()-mapper.started,
        ode_rtol=args.tolerance,
        limitations=[
            "ordinary floating ODE and finite angular samples",
            "only the central principal graph; no amplitudes or phase/DtN corrections",
            "root uniqueness, continuous sign/transversality and ODE error are not certified",
            "no mean derivatives or claim of an exact PDE family",
            "no closed-surface, held or reach certificate"])
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    if args.progress:
        args.progress.write_text(json.dumps(dict(status="complete", output=str(args.out),
                                                 rhs_calls=mapper.calls))+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in
                      ("initial_angles", "returned_angles", "angular_derivative", "completed_blocks")}), flush=True)


if __name__ == "__main__":
    main()
