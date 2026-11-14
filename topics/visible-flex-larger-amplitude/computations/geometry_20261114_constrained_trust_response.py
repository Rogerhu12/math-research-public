#!/usr/bin/env python3
"""Actual full R252 derivative check on a descended unaccepted warm.

The completed true T112 zero-H Jacobian is held explicitly affine while
checking the original boundary implementation at this actual new endpoint.
Its current H need not equal the affine anchor. No new nonlinear native H
has been solved here. The subsequent unchanged full-DN driver must perform
that actual solve, its full outer iteration and its final fresh audit.
The original three centered steps, Richardson values and 5e-5 gate remain.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from pathlib import Path
import time
import json
import numpy as np

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_augmented import SeparatedBoundary
from geometry_20261114_full_dn_response import refined_directional_check
from geometry_20261114_lifted_modes_response import binding
from geometry_20261114_physical_test_boundary import SCHEMA as PHYSICAL_SCHEMA
from geometry_20261114_physical_test_response import make_directions
from geometry_20261114_actual_direction_probe import clean
from geometry_20261114_constrained_trust_warm import setup, EXPECTED, SCHEMA

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--angles", type=int, default=4096)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Execute numerical response checks in this public Actions")
    for name in ("accepted", "tail_anchor", "tail_config"):
        if original.sha(getattr(args, name)) != EXPECTED[name]:
            raise ValueError("Retain the actual original source and complete true zero response: "+name)
    accepted, prepared, anchor = (original.read(path) for path in
        (args.accepted, args.prepared, args.tail_anchor))
    optimization = prepared.get("optimization_warm", {})
    if (optimization.get("schema") != SCHEMA
            or optimization.get("source_prepared_sha256") != EXPECTED["prepared"]
            or optimization.get("source_accepted_sha256") != EXPECTED["accepted"]
            or optimization.get("actual_zero_anchor_sha256") != EXPECTED["tail_anchor"]
            or prepared.get("success") is not False
            or prepared.get("new_coupled_finite_acceptance") is not False):
        raise ValueError("Supply the real explicitly unaccepted optimization warm")
    for name, digest in optimization["source_sha256"].items():
        if original.sha(HERE/name) != digest:
            raise ValueError("An actual optimization source changed: "+name)
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh actual-response output directory")
    started = time.monotonic()
    profile, flow, boundary = setup(accepted, prepared, anchor, args.angles, 1)
    separated = SeparatedBoundary(boundary)
    values = np.asarray(prepared["states"])
    ya, yb = values[0].copy(), values[-1].copy()
    current_H = original.true_height(boundary, yb)
    # Preserve the previous actual nonzero perturbation that exercises both
    # core-angle chain terms. It is a code check of the explicitly affine map.
    yb[boundary.iz+1] += 1e-5
    yb[boundary.iz+32] += 1e-9
    yb[boundary.iz+flow.M] += 1e-10
    pa, pb, controls = ya[:flow.n], yb[:flow.n], yb[flow.parameter_slice]
    direct_directions, augmented_directions = make_directions(flow, boundary)
    A, B, P = boundary.jacobian(pa, pb, controls)
    direct = refined_directional_check(
        lambda d, h: boundary(pa+h*d["ya"], pb+h*d["yb"], controls+h*d["p"]),
        lambda d: A@d["ya"]+B@d["yb"]+P@d["p"], direct_directions)
    AA, BB = separated.jacobian(ya, yb)
    augmented = refined_directional_check(
        lambda d, h: separated(ya+h*d["ya"], yb+h*d["yb"]),
        lambda d: AA@d["ya"]+BB@d["yb"], augmented_directions)
    augmented.update(right_rows_depend_only_on_right_endpoint=True,
        left_right_jacobian_offblock_max=float(max(np.max(abs(AA[separated.left_count:])),
            np.max(abs(BB[:separated.left_count])))))
    groups = (direct, augmented)
    coarse = max(level["relative_error"] for group in groups
        for direction in group["directions"] for level in direction["levels"])
    error = max(level["relative_error"] for group in groups
        for direction in group["directions"] for level in direction["fourth_order_levels"])
    contracts = all(group["second_order_truncation_contracts"] for group in groups)
    source_names = (Path(__file__).name, "geometry_20261114_constrained_trust_warm.py",
        "geometry_20261114_constrained_collocation.py", "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_physical_test_response.py", "geometry_20261114_full_dn_boundary.py",
        "geometry_20261114_full_dn_response.py", "geometry_20261114_full_dn_augmented.py",
        "geometry_20261114_lifted_modes_profile.py", "geometry_20261114_full_dn_solve.py")
    report = dict(scope=__doc__, direct_boundary=direct, separated_boundary=augmented,
        maximum_relative_directional_error=error,
        maximum_fourth_order_relative_directional_error=error,
        maximum_second_order_relative_directional_error=coarse,
        second_order_truncation_contracts=contracts, verification_threshold=5e-5,
        verification_estimator="two fourth-order Richardson levels",
        implementation_check_passed=bool(np.isfinite(error) and error <= 5e-5 and contracts),
        physical_test_schema=PHYSICAL_SCHEMA, physical_test=boundary.description(),
        lifted_modes_implementation=binding(flow.M, flow.q.N, accepted),
        accepted_sha256=original.sha(args.accepted), prepared_sha256=original.sha(args.prepared),
        tail_anchor_sha256=original.sha(args.tail_anchor), tail_config_sha256=original.sha(args.tail_config),
        source_sha256=original.sha(__file__),
        consumed_source_sha256={name: original.sha(HERE/name) for name in source_names},
        optimization_warm=optimization, actual_warm_native_height=current_H.tolist(),
        affine_anchor_native_height=anchor["checkpoint"]["cutHeight"],
        current_H_equals_affine_anchor=bool(np.array_equal(current_H, anchor["checkpoint"]["cutHeight"])),
        linear_reference_source="Full completed real T112 zero-H J held affine at the actual new warm; no actual tail at its new H is asserted",
        ready_linear_graph_used=False, actual_completed_nonlinear_J_reused=True,
        nonlinear_DN_evaluated=False, nonlinear_native_at_current_H_solved=False,
        complete_current_warm_boundary_FD_actually_recomputed=True,
        old_response_pass_or_warm_SHA_relabelled=False,
        full_BVP_solved=False, full_Cartesian_closed_surface=False,
        seconds=time.monotonic()-started)
    original.write(args.out/"response-check.json", clean(report))
    print(json.dumps(dict(event="actual_descended_warm_R252_response",
        implementation_check_passed=report["implementation_check_passed"],
        maximum_relative_directional_error=error, seconds=report["seconds"])), flush=True)
    return 0 if report["implementation_check_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
