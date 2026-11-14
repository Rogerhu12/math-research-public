#!/usr/bin/env python3
"""Audit an existing actual zero-height tail response without another solve.

For fixed g=E(r)dr^2+r^2 dtheta^2, E=1+w^2, linearizing Darboux at
z_r=w, z_theta=0 gives h_rr=-(w_r/w)h_r-(w_r/(r*w))h_thetatheta.
Consequently J_second=(w_r/w)*(diag((spacing*j)^2/r)-J_slope).
The complete mean slope/second corrections start at quadratic order, and
the physical Dirichlet height block is the identity. Fourier modes decouple
at this rotational background. These provide independent diagnostics of
the source's extremely small symmetric second-jet differences at H=0.

The actual nonlinear solve, full Jacobian and audit must already be present.
This consumer reports discrepancies; it neither alters that response nor
replaces an acceptance gate or claims an infinite-tail/closed result.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path

import numpy as np


def read(path):
    raw = Path(path).read_bytes()
    value = json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
    return value, hashlib.sha256(raw).hexdigest()


def errors(actual, reference):
    gap = np.asarray(actual)-np.asarray(reference)
    return dict(maximum_absolute=float(np.max(abs(gap))),
                maximum_relative_entry=float(np.max(abs(gap)/np.maximum(1., abs(reference)))),
                maximum_relative_column=float(np.max(np.max(abs(gap), axis=0)
                    / np.maximum(1., np.max(abs(reference), axis=0)))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--response", type=Path, required=True,
                        help="Complete tail_0001.json.gz record produced by the true client")
    parser.add_argument("--ready", type=Path,
                        help="Optional original ready packet, to compare its separate linear graph")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise ValueError("Numerical diagnostics belong to this public repository GitHub Actions")
    if args.out.exists():
        raise FileExistsError("Use a new response-audit output path")
    record, input_sha = read(args.response)
    response = record["response"]
    height = np.asarray(record["request"]["height"], dtype=float)
    M = len(height)
    if (height.shape != (M,) or M < 1 or not np.all(np.isfinite(height)) or np.any(height != 0)
            or response.get("converged") is not True or response.get("actual_nonlinear_solve") is not True
            or record["request"].get("jacobian") is not True or record["request"].get("audit") is not True
            or response.get("audit") is None):
        raise ValueError("An actual converged exact-zero request with complete J and full audit is required")
    jets = response["jets"]
    for name in ("height", "slope", "second"):
        values = np.asarray(jets[name], dtype=float)
        if values.shape != (M,) or not np.all(np.isfinite(values)):
            raise ValueError("A complete finite jet was lost: " + name)
    if np.any(np.asarray(jets["height"]) != 0):
        raise ValueError("The actual solved response does not have exactly zero Dirichlet height")
    matrix = np.asarray(response["heightJetJacobian"], dtype=float)
    if matrix.shape != ((3*M+2)*M,) or not np.all(np.isfinite(matrix)):
        raise ValueError("The complete (3M+2)-by-M physical Jacobian is required")
    matrix = matrix.reshape(3*M+2, M)
    slope, second = matrix[:M], matrix[M:2*M]
    mean_slope, mean_second, identity = matrix[2*M], matrix[2*M+1], matrix[2*M+2:]
    r, w, wr = (float(jets[key]) for key in ("radius", "backgroundSlope", "backgroundSecond"))
    if not r > 0 or not w > 0 or not np.all(np.isfinite([r, w, wr])):
        raise ValueError("A regular positive native radial chart is required")
    spacing = int(record["config"]["spacing"])
    frequencies = spacing*np.arange(1, M+1)
    predicted_second = (wr/w)*(np.diag(frequencies**2/r)-slope)
    slope_diagonal = np.diag(np.diag(slope))
    second_diagonal = np.diag(np.diag(second))
    ready_check = None
    if args.ready:
        ready, ready_sha = read(args.ready)
        linear = np.asarray(ready["linearSlope"], dtype=float)
        if linear.shape != (M,) or not np.all(np.isfinite(linear)):
            raise ValueError("Ready reference has different finite modes")
        ready_check = dict(ready_sha256=ready_sha,
                          actual_shooting_slope_J_minus_ready_linear_graph=errors(slope, np.diag(linear)),
                          distinction="The ready reference uses the precomputed linear stable graphs; the response J uses actual finite shooting variational flow. This comparison does not substitute one for the other.")
    report = dict(
        schema="actual-zero-height-full-tail-J-audit-v1", input_sha256=input_sha,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        actual_nonlinear_solve_already_performed=True, another_tail_solve_performed=False,
        all_requested_height_modes_exactly_zero=True, modes=M, spacing=spacing,
        parameters=response["checkpoint"]["parameters"], residual=response["residual"],
        cut=dict(radius=r, w=w, w_r=wr, E=float(jets["E"]), Ep=float(jets["Ep"])),
        source_J_method=response.get("heightJetJacobianMethod"),
        actual_original_audit=response["audit"],
        physical_background_jet_errors=dict(
            height_max=float(np.max(np.abs(jets["height"]))),
            slope_nonmean_max=float(np.max(np.abs(jets["slope"]))),
            second_nonmean_max=float(np.max(np.abs(jets["second"]))),
            mean_slope_minus_background=abs(float(jets["meanSlope"])-w),
            mean_second_minus_background=abs(float(jets["meanSecond"])-wr)),
        J_second_linearized_Darboux=errors(second, predicted_second),
        J_slope_Fourier_decoupling=errors(slope, slope_diagonal),
        J_second_Fourier_decoupling=errors(second, second_diagonal),
        J_mean_slope_zero_max=float(np.max(abs(mean_slope))),
        J_mean_second_zero_max=float(np.max(abs(mean_second))),
        J_height_identity=errors(identity, np.eye(M)),
        maximum_absolute_slope_J=float(np.max(abs(slope))),
        maximum_absolute_second_J=float(np.max(abs(second))),
        diagonal_slope=np.diag(slope).tolist(), diagonal_second=np.diag(second).tolist(),
        ready_reference_comparison=ready_check,
        scope=__doc__, no_acceptance_threshold_changed=True,
        finite_discretization_only=True, nonzero_height_DN_still_requires_actual_solve=True,
        closed_surface_certified=False, task_completed=False)
    raw = (json.dumps(report, indent=2, allow_nan=False)+"\n").encode()
    if len(raw) >= 1_000_000:
        raise ValueError("The compact zero-height report unexpectedly exceeds 1 MB")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("xb") as stream:
        stream.write(raw)
    print(json.dumps({key: report[key] for key in (
        "modes", "residual", "J_second_linearized_Darboux", "J_mean_slope_zero_max",
        "J_mean_second_zero_max", "J_height_identity", "task_completed")}), flush=True)


if __name__ == "__main__":
    main()
