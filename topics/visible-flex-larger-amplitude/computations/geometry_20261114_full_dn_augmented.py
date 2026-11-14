#!/usr/bin/env python3
"""Constant-state augmentation of the complete nonmean material DN problem.

Appending c'=0 and p'=0 makes the core-angle dependence of the right
boundary local to that endpoint. The original separated-QR collocation
backend can then retain all rows without supporting nonlocal boundaries or
an external parameter border. No physical degree of freedom is introduced:
the left boundary identifies c with the actual inlet support coefficients.

The CLI checks the controlled RHS on real accepted prefix states and on
explicitly labeled circular local states. It does not claim an accepted
full extension, a tail solve, a seam, or a closed surface.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import numpy as np

import geometry_20261114_r225_free_core_bvp as base
from geometry_20261114_full_scalar_profile import CompleteProfile, read


class AugmentedFlow:
    """Unchanged FFT Frenet RHS with explicit, node-local scalar controls.

Each call supplies a fresh original BatchedFFTFlow with that call's scalar
jets already in its cache. In particular, a cache keyed only by s cannot
reuse jets from another parameter iterate. Constant c and p rows have
identically zero derivatives, not small penalty equations.
    """
    def __init__(self, probe, profile, workers=1):
        self.q, self.profile = probe, profile
        self.M, self.k, self.n = probe.M, profile.parameter_count, probe.n
        if probe.M != profile.M:
            raise ValueError("Scalar profile and complete physical field modes differ")
        self.dimension = self.n + self.M + self.k
        self.core_slice = slice(self.n, self.n + self.M)
        self.parameter_slice = slice(self.n + self.M, self.dimension)
        self.workers = int(workers)
        self._base_cache = {}

    def scalar_jets(self, x, parameters):
        x, parameters = np.asarray(x, dtype=float), np.asarray(parameters)
        if parameters.shape != (self.k, len(x)):
            raise ValueError("Supply each node's complete scalar parameter vector")
        key = x.tobytes()
        if key not in self._base_cache:
            self._base_cache[key] = (np.array([self.profile.base_jet(s) for s in x]),
                                    np.stack([self.profile.control_jets(s) for s in x]))
        baseline, controls = self._base_cache[key]
        jets = baseline + np.einsum("mjk,km->mj", controls, parameters)
        return jets

    def physical(self, x, y, parameters):
        x, y = np.asarray(x, dtype=float), np.asarray(y)
        if y.shape != (self.n, len(x)):
            raise ValueError("Every physical state component must be supplied")
        jets = self.scalar_jets(x, parameters)
        # Complex perturbations only differentiate a valid real state. An
        # inadmissible real trial remains invalid for Newton backtracking.
        valid = (np.all(np.isfinite(jets.real), axis=1) & (jets[:, 0].real > 0)
                 & (np.abs(jets[:, 1].real) < 1))
        original = base.BatchedFFTFlow(self.q)
        original.profiles[x.tobytes()] = jets
        value = original(x, y)
        if not np.all(valid):
            value[:, ~valid] = np.nan
        return value

    def __call__(self, x, y):
        y = np.asarray(y)
        if y.shape != (self.dimension, len(x)):
            raise ValueError("The augmented state lost a physical, core or control row")
        answer = np.zeros_like(y)
        answer[:self.n] = self.physical(x, y[:self.n], y[self.parameter_slice])
        return answer

    def jac(self, x, y):
        x, y = np.asarray(x, dtype=float), np.asarray(y)
        result = np.zeros((self.dimension, self.dimension, len(x)))
        step = 1e-25
        active = list(range(self.n)) + list(range(self.n + self.M, self.dimension))
        def column(j):
            trial = y.astype(complex)
            trial[j] += 1j * step
            result[:self.n, j] = self.physical(x, trial[:self.n], trial[self.parameter_slice]).imag / step
        if self.workers == 1:
            for j in active:
                column(j)
        else:
            with ThreadPoolExecutor(max_workers=self.workers) as pool:
                list(pool.map(column, active))
        return result

    def point_rhs(self, s, y, parameters):
        return self.physical(np.array([s]), np.asarray(y)[:, None], np.asarray(parameters)[:, None])[:, 0]

    def point_jacobian(self, s, y, parameters):
        step = 1e-25
        y, parameters = np.asarray(y), np.asarray(parameters)
        Jy, Jp = np.empty((self.n, self.n)), np.empty((self.n, self.k))
        for j in range(self.n):
            yc = y.astype(complex); yc[j] += 1j * step
            Jy[:, j] = self.point_rhs(s, yc, parameters).imag / step
        for j in range(self.k):
            pc = parameters.astype(complex); pc[j] += 1j * step
            Jp[:, j] = self.point_rhs(s, y, pc).imag / step
        return Jy, Jp


class SeparatedBoundary:
    """Algebraically equivalent separated boundary for constant augmentation."""
    def __init__(self, boundary):
        self.original = boundary
        self.n, self.M, self.k = boundary.n, boundary.M, boundary.k
        self.dimension = self.n + self.M + self.k
        self.left_count = boundary.left_count + self.M
        self.core_slice = slice(self.n, self.n + self.M)
        self.parameter_slice = slice(self.n + self.M, self.dimension)
        if self.left_count + boundary.T != self.dimension:
            raise ValueError("The constant-state augmented problem is not square")

    def _endpoint_proxy(self, endpoint):
        proxy = np.zeros(self.n)
        proxy[1:self.M + 1] = endpoint[self.core_slice]
        return proxy

    def __call__(self, ya, yb):
        ya, yb = np.asarray(ya), np.asarray(yb)
        if ya.shape != (self.dimension,) or yb.shape != ya.shape:
            raise ValueError("Both complete augmented endpoints are required")
        b = self.original
        frequency = 2 * np.arange(1, self.M + 1)
        left = np.r_[ya[0] - 1, ya[1:b.K + 1] - b.target,
                     ya[self.M + 1:b.iz] + frequency * ya[1:self.M + 1], ya[b.iz:self.n],
                     ya[self.core_slice] - ya[1:self.M + 1]]
        right = b(self._endpoint_proxy(yb), yb[:self.n], yb[self.parameter_slice])[b.left_count:]
        return np.r_[left, right]

    def jacobian(self, ya, yb):
        b = self.original
        A0, B0, P0 = b.jacobian(self._endpoint_proxy(yb), yb[:self.n], yb[self.parameter_slice])
        A = np.zeros((self.dimension, self.dimension)); B = np.zeros_like(A)
        A[:b.left_count, :self.n] = A0[:b.left_count]
        j = np.arange(self.M)
        A[b.left_count + j, 1 + j] = -1
        A[b.left_count + j, self.n + j] = 1
        B[self.left_count:, :self.n] = B0[b.left_count:]
        B[self.left_count:, self.core_slice] = A0[b.left_count:, 1:self.M + 1]
        B[self.left_count:, self.parameter_slice] = P0[b.left_count:]
        return A, B


def response_check(flow, s, physical, parameters, parameter_index, steps=(2e-6, 1e-6)):
    direction = np.zeros(flow.k); direction[parameter_index] = 1
    analytic = flow.point_rhs(s, physical, parameters.astype(complex) + 1j * 1e-25 * direction).imag / 1e-25
    levels = []
    for step in steps:
        finite = (flow.point_rhs(s, physical, parameters + step * direction)
                  - flow.point_rhs(s, physical, parameters - step * direction)) / (2 * step)
        error = float(np.max(np.abs(finite - analytic)))
        levels.append(dict(step=step, absolute_error=error,
                           relative_error=error / max(1., float(np.max(np.abs(analytic))))))
    return dict(station=s, parameter_index=parameter_index,
                analytic_response_max=float(np.max(np.abs(analytic))), levels=levels)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--accepted", type=Path, required=True)
    p.add_argument("--port", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--peak-curvature", type=float, default=2.5)
    p.add_argument("--tail-modes", type=int)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Perform numerical response checks in the public repository's own Actions")
    accepted, port = read(args.accepted), read(args.port)
    profile = CompleteProfile(accepted, port, args.peak_curvature, args.tail_modes)
    description = profile.description()
    law = accepted["original_metric_identity"]["law"]
    q = base.native.outward.FullCoreProbe(np.array(accepted["core"]["coefficients"]),
        accepted["M"], accepted["N"], law["velocity"], law["length"], law["k0"])
    q.profile = profile.prefix.profile
    base.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile)
    saved_mesh, saved_states = np.array(accepted["mesh"]), np.array(accepted["states"])
    indices = np.array([0, len(saved_mesh) // 2, len(saved_mesh) - 1])
    points, field = saved_mesh[indices], saved_states[indices].T
    original = base.BatchedFFTFlow(q)(points, field)
    controlled = flow.physical(points, field, np.zeros((flow.k, len(points))))
    difference = float(np.max(np.abs(controlled - original)))
    if difference > 1e-12:
        raise ValueError("The zero-control wrapper changed the original physical Frenet RHS")
    checks = []
    for j, bump in enumerate(profile.bumps):
        s = (bump.left + bump.right) / 2
        if j == 0:
            index = int(np.argmin(np.abs(saved_mesh - s)))
            s, y = saved_mesh[index], saved_states[index]
            kind = "actual-accepted-prefix-state"
        else:
            y = np.zeros(flow.n); y[0] = profile.base_jet(s)[0]
            kind = "explicit-circular-local-RHS-calibration-not-an-extension-solution"
        check = response_check(flow, float(s), y, np.zeros(flow.k), j)
        check["state_kind"] = kind
        checks.append(check)
    report = dict(scope=__doc__, scalar_profile=description,
                  physical_state_dimension=flow.n, augmented_state_dimension=flow.dimension,
                  left_rows=2 * flow.M + 5 + flow.M, right_rows=profile.tail_modes,
                  zero_control_original_RHS_max_difference=difference,
                  scalar_control_directional_checks=checks,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  accepted_sha256=hashlib.sha256(args.accepted.read_bytes()).hexdigest(),
                  full_DN_evaluated=False, full_DN_boundary_FD_checked=False,
                  full_extension_solved=False, closed_surface_certified=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps({key: report[key] for key in ("physical_state_dimension", "augmented_state_dimension",
                     "left_rows", "right_rows", "zero_control_original_RHS_max_difference")}), flush=True)


if __name__ == "__main__":
    main()
