#!/usr/bin/env python3
"""Check the full material-DN boundary glue and constant-state augmentation.

The actual public worker's ready.linearD is used only as an explicitly
identified original-linear-graph reference matrix. It is not reported as a
computed nonlinear finite DN Jacobian. A nonzero-height trial at the real
physical cut makes core-angle derivatives visible in the response test.
No nonlinear BVP or tail acceptance is inferred from these checks.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

import geometry_20261114_projected_core_bvp as original
from geometry_20261114_full_scalar_profile import CompleteProfile, read
from geometry_20261114_full_dn_boundary import FullDNBoundary, directional_check
from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
from geometry_20261114_full_dn_solve import load_client


def separated_directional_check(boundary, ya, yb, directions, steps=(2e-6, 1e-6)):
    A, B = boundary.jacobian(ya, yb)
    rows = []
    for direction in directions:
        da, db = direction["ya"], direction["yb"]
        analytic = A @ da + B @ db
        levels = []
        for step in steps:
            finite = (boundary(ya + step * da, yb + step * db)
                      - boundary(ya - step * da, yb - step * db)) / (2 * step)
            error = float(np.max(np.abs(finite - analytic)))
            levels.append(dict(step=step, absolute_error=error,
                               relative_error=error / max(1., float(np.max(np.abs(analytic))))))
        rows.append(dict(direction=direction["name"], levels=levels,
                         analytic_response_max=float(np.max(np.abs(analytic)))))
    return dict(directions=rows, right_rows_depend_only_on_right_endpoint=True,
                left_right_jacobian_offblock_max=float(max(np.max(np.abs(A[boundary.left_count:])),
                                                          np.max(np.abs(B[:boundary.left_count])))))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--accepted", type=Path, required=True)
    p.add_argument("--prepared", type=Path, required=True)
    p.add_argument("--port", type=Path, required=True)
    p.add_argument("--tail-client", type=Path, required=True)
    p.add_argument("--tail-config", type=Path, required=True)
    p.add_argument("--tail-source-root", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--node-heap", type=int, default=1536)
    p.add_argument("--material-angles", type=int, default=4096)
    p.add_argument("--peak-curvature", type=float, default=2.5)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Run response computations in this public repository's own Actions")
    accepted, prepared, port = read(args.accepted), read(args.prepared), read(args.port)
    profile = CompleteProfile(accepted, port, args.peak_curvature, accepted["M"])
    law = accepted["original_metric_identity"]["law"]
    coefficients = np.asarray(accepted["core"]["coefficients"])
    q = original.native.outward.FullCoreProbe(coefficients, accepted["M"], accepted["N"],
        law["velocity"], law["length"], law["k0"])
    original.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile)
    states = np.asarray(prepared.get("augmented_states", prepared["states"]))
    if states.shape != (len(prepared["mesh"]), flow.dimension) or abs(prepared["mesh"][-1] - profile.end) > 1e-12:
        raise ValueError("Use a complete prepared field on the identical scalar interval")
    args.out.mkdir(parents=True, exist_ok=True)
    client = load_client(args.tail_client, args.tail_config, args.tail_source_root,
                         args.out / "original-linear-graph-reference", args.node_heap)
    try:
        for key in ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond"):
            if not np.isclose(float(client.cut[key]), float(profile.cut[key]), rtol=2e-11, atol=2e-13):
                raise ValueError("The original linear reference has another physical cut")
        J = np.diag(client.linearD)
        def reference(height):
            return dict(slope=J @ height, jacobian=J, actual_nonlinear_solve=False,
                        scope="Original ready.linearD graph reference only; not an evaluated nonlinear finite DN Jacobian")
        boundary = FullDNBoundary(profile, coefficients[:3], flow.point_rhs, flow.point_jacobian,
                                  reference, angular=args.material_angles)
        separated = SeparatedBoundary(boundary)
        ya, yb = states[0].copy(), states[-1].copy()
        # Nonzero height is an explicitly unaccepted local trial. Otherwise
        # a zero-height circle would make every core-angle Jacobian vanish.
        yb[boundary.iz + 1] += 1e-5
        yb[boundary.iz + 32] += 1e-9
        yb[boundary.iz + flow.M] += 1e-10
        yb[flow.core_slice] = ya[1:flow.M + 1]
        pa, pb = ya[:flow.n].copy(), yb[:flow.n].copy()
        controls = yb[flow.parameter_slice].copy()
        directions, augmented = [], []
        for j in (0, 31, flow.M - 1):
            scale = 1 / (1 + (2 * (j + 1)) ** 2)
            da, db, dp = np.zeros(flow.n), np.zeros(flow.n), np.zeros(flow.k)
            da[j + 1] = scale
            directions.append(dict(name="core-angle-" + str(j + 1), ya=da, yb=db, p=dp))
            aa, bb = np.zeros(flow.dimension), np.zeros(flow.dimension)
            bb[flow.n + j] = scale
            augmented.append(dict(name="right-constant-core-" + str(j + 1), ya=aa, yb=bb))
        for name, index, scale in (("radial-mean", 0, .1), ("tangent-first", flow.M + 1, .05),
                                    ("height-first", boundary.iz + 1, .01),
                                    ("height-last", boundary.iz + flow.M, 1 / (1 + (2 * flow.M) ** 2))):
            da, db, dp = np.zeros(flow.n), np.zeros(flow.n), np.zeros(flow.k)
            db[index] = scale
            directions.append(dict(name=name, ya=da, yb=db, p=dp))
            aa, bb = np.zeros(flow.dimension), np.zeros(flow.dimension)
            bb[index] = scale
            augmented.append(dict(name=name, ya=aa, yb=bb))
        for j in range(flow.k):
            da, db, dp = np.zeros(flow.n), np.zeros(flow.n), np.zeros(flow.k)
            dp[j] = 1
            directions.append(dict(name="cut-fixed-scalar-control-" + str(j), ya=da, yb=db, p=dp))
            aa, bb = np.zeros(flow.dimension), np.zeros(flow.dimension)
            bb[flow.n + flow.M + j] = 1
            augmented.append(dict(name="right-scalar-control-" + str(j), ya=aa, yb=bb))
        direct = directional_check(boundary, pa, pb, controls, directions)
        separated_result = separated_directional_check(separated, ya, yb, augmented)
        worst = max(level["relative_error"] for group in (direct, separated_result)
                    for row in group["directions"] for level in row["levels"])
        report = dict(scope=__doc__, direct_boundary=direct, separated_boundary=separated_result,
                      maximum_relative_directional_error=worst,
                      implementation_check_passed=bool(np.isfinite(worst) and worst <= 5e-5),
                      linear_reference_source="Actual public worker ready.linearD; original linear stable graphs",
                      physical_cut=client.cut, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      accepted_sha256=hashlib.sha256(args.accepted.read_bytes()).hexdigest(),
                      prepared_sha256=hashlib.sha256(args.prepared.read_bytes()).hexdigest(),
                      nonlinear_DN_evaluated=False, nonlinear_finite_DN_J_evaluated=False,
                      full_BVP_solved=False, full_Cartesian_closed_surface=False)
        (args.out / "response-check.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
        print(json.dumps(dict(maximum_relative_directional_error=worst,
                              implementation_check_passed=report["implementation_check_passed"])), flush=True)
        return 0 if report["implementation_check_passed"] else 2
    finally:
        client.close()


if __name__ == "__main__":
    raise SystemExit(main())
