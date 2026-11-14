#!/usr/bin/env python3
"""Actual R252 boundary/Jacobian checks with the completed true T112 J.

The saved original 699-node field is reused without a new initial guess.
All FD evaluations use the explicitly affine map anchored at the completed
true zero-height response; they do not call a nonlinear tail at new H.
The original three centered steps, two Richardson values, contraction test
and 5e-5 verification threshold are unchanged.  A saved homogeneous
endspace is used only for a small diagnostic, never as the new solver.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import json
from pathlib import Path
import time

import numpy as np

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_response import refined_directional_check
from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
from geometry_20261114_lifted_modes_profile import LiftedModesPrefixProfile, field_spec
from geometry_20261114_lifted_modes_prepare import validate_source
from geometry_20261114_lifted_modes_response import binding
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA
from geometry_20261114_actual_direction_probe import svd_report, clean


HERE = Path(__file__).resolve().parent
EXPECTED = dict(
    accepted="b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
    prepared="0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714",
    tail_anchor="e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51",
    tail_config="01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5",
    qr_reduced="ef8164f79e5656b18fcb73089cf8d4dbf4ee02ad5d9dd87eb218cdcea9cf36d2")


def make_directions(flow, boundary):
    direct, augmented = [], []
    for j in (0, 31, flow.M - 1):
        scale = 1 / (1 + (2 * (j + 1)) ** 2)
        da, db, dp = np.zeros(flow.n), np.zeros(flow.n), np.zeros(flow.k)
        da[j + 1] = scale
        direct.append(dict(name="core-angle-" + str(j + 1), ya=da, yb=db, p=dp))
        aa, bb = np.zeros(flow.dimension), np.zeros(flow.dimension)
        bb[flow.n + j] = scale
        augmented.append(dict(name="right-constant-core-" + str(j + 1), ya=aa, yb=bb))
    for name, index, scale in (("radial-mean", 0, .1), ("tangent-first", flow.M + 1, .05),
            ("height-first", boundary.iz + 1, .01),
            ("height-last", boundary.iz + flow.M, 1 / (1 + (2 * flow.M) ** 2))):
        da, db, dp = np.zeros(flow.n), np.zeros(flow.n), np.zeros(flow.k)
        db[index] = scale
        direct.append(dict(name=name, ya=da, yb=db, p=dp))
        aa, bb = np.zeros(flow.dimension), np.zeros(flow.dimension)
        bb[index] = scale
        augmented.append(dict(name=name, ya=aa, yb=bb))
    for j in range(flow.k):
        da, db, dp = np.zeros(flow.n), np.zeros(flow.n), np.zeros(flow.k)
        dp[j] = 1
        direct.append(dict(name="cut-fixed-scalar-control-" + str(j), ya=da, yb=db, p=dp))
        aa, bb = np.zeros(flow.dimension), np.zeros(flow.dimension)
        bb[flow.n + flow.M + j] = 1
        augmented.append(dict(name="right-scalar-control-" + str(j), ya=aa, yb=bb))
    return direct, augmented


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run all numerical response checks in the public Actions")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "qr-reduced", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--material-angles", type=int, default=4096)
    parser.add_argument("--physical-angles", type=int, default=4096)
    args = parser.parse_args()
    begin = time.monotonic()
    for name, expected in EXPECTED.items():
        if original.sha(getattr(args, name)) != expected:
            raise ValueError("Use the exact preserved actual input: " + name)
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh output directory for the new finite test")
    accepted, prepared, anchor, config = [original.read(path) for path in
        (args.accepted, args.prepared, args.tail_anchor, args.tail_config)]
    validate_source(accepted)
    M, N = int(prepared["M"]), int(prepared["N"])
    spec = prepared["complete_scalar_profile"]
    if (prepared["field_representation"] != field_spec(M, N)
            or spec["accepted_prefix_sha256"] != original.sha(args.accepted)
            or spec["base_prefix_geometry"] != accepted["fixed_scalar_profile"]["geometry"]):
        raise ValueError("The prepared source, finite field or scalar identity changed")
    profile = LiftedModesPrefixProfile(accepted, spec["complete_original_port"],
        spec["peak_curvature"], M, supports=spec["control_supports_binary64"])
    law = accepted["original_metric_identity"]["law"]
    states = np.asarray(prepared["states"], float)
    physical = 3 * M + 2
    if states.shape != (len(prepared["mesh"]), 4 * M + 5):
        raise ValueError("The complete original augmented field must be retained")
    core = states[0, physical:physical + M]
    q = original.original_solver.native.outward.FullCoreProbe(
        core, M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile)
    H = np.asarray(anchor["checkpoint"]["cutHeight"], float)
    if (anchor.get("converged") is not True or anchor.get("actual_nonlinear_solve") is not True
            or anchor.get("failed", False) or anchor["residual"] != 0
            or H.shape != (M,) or np.any(H != 0) or int(config["modes"]) != M):
        raise ValueError("The complete actual T112 zero anchor and full J are required")
    affine = original.AffineTail(M)
    affine.set(H, anchor)
    boundary = PhysicalTestBoundary(profile, np.asarray(accepted["core"]["coefficients"])[:3],
        flow.point_rhs, flow.point_jacobian, affine, angular=args.material_angles,
        physical_angles=args.physical_angles)
    separated = SeparatedBoundary(boundary)
    ya, yb = states[0].copy(), states[-1].copy()
    if np.any(original.true_height(boundary, yb) != H):
        raise ValueError("The saved warm must have exactly the completed zero native height")
    # Preserve the original nonzero local FD trial.  In particular S_j d
    # and S J P_j z cannot vanish merely because the saved anchor is zero.
    yb[boundary.iz + 1] += 1e-5
    yb[boundary.iz + 32] += 1e-9
    yb[boundary.iz + flow.M] += 1e-10
    yb[flow.core_slice] = ya[1:flow.M + 1]
    pa, pb, controls = ya[:flow.n].copy(), yb[:flow.n].copy(), yb[flow.parameter_slice].copy()
    direct_directions, augmented_directions = make_directions(flow, boundary)
    A, B, Pp = boundary.jacobian(pa, pb, controls)
    direct = refined_directional_check(
        lambda d, h: boundary(pa + h * d["ya"], pb + h * d["yb"], controls + h * d["p"]),
        lambda d: A @ d["ya"] + B @ d["yb"] + Pp @ d["p"], direct_directions)
    AA, BB = separated.jacobian(ya, yb)
    separated_result = refined_directional_check(
        lambda d, h: separated(ya + h * d["ya"], yb + h * d["yb"]),
        lambda d: AA @ d["ya"] + BB @ d["yb"], augmented_directions)
    separated_result.update(right_rows_depend_only_on_right_endpoint=True,
        left_right_jacobian_offblock_max=float(max(np.max(abs(AA[separated.left_count:])),
            np.max(abs(BB[:separated.left_count])))))
    groups = (direct, separated_result)
    coarse = max(v["relative_error"] for g in groups for d in g["directions"] for v in d["levels"])
    worst = max(v["relative_error"] for g in groups for d in g["directions"] for v in d["fourth_order_levels"])
    contracts = all(g["second_order_truncation_contracts"] for g in groups)
    # The old saved Uend depends only on the identical ODE/left constraints.
    # This measures a small matrix, not a new QR or an accepted Newton step.
    left, right = states[0], states[-1]
    AB, BB0 = separated.jacobian(left, right)
    right_matrix = BB0[separated.left_count:]
    raw = np.load(args.qr_reduced)
    endspace = raw["nullspace_right"]
    reduced = right_matrix @ endspace
    original_boundary = original.FullDNBoundary(profile,
        np.asarray(accepted["core"]["coefficients"])[:3], flow.point_rhs, flow.point_jacobian,
        affine, angular=args.material_angles)
    old_separated = SeparatedBoundary(original_boundary)
    oldA, oldB = old_separated.jacobian(left, right)
    old_reduced = oldB[separated.left_count:] @ endspace
    old_reduced_gap = float(np.max(abs(old_reduced - raw["small"])))
    seed_report = dict(new_physical_right=svd_report(right_matrix),
        new_physical_on_saved_original_endspace=svd_report(reduced),
        original_material_right=svd_report(oldB[separated.left_count:]),
        old_reduced_reproduction_max=old_reduced_gap,
        original_left_Jacobian_difference=float(np.max(abs(AB - oldA))),
        new_seed_BC_max=float(np.max(abs(separated(left, right)))),
        old_seed_BC_max=float(np.max(abs(old_separated(left, right)))),
        saved_endspace_used_only_for_readonly_diagnostic=True,
        new_global_factorization=False, new_nonlinear_tail_solve=False)
    original.write(args.out / "physical-test-small-condition.json", clean(seed_report))
    original.write(args.out / "physical-test-small-operators.json.gz", dict(
        right_BC=right_matrix.tolist(), reduced_on_old_endspace=reduced.tolist()))
    source_names = (Path(__file__).name, "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_full_dn_boundary.py", "geometry_20261114_full_dn_response.py",
        "geometry_20261114_full_dn_augmented.py", "geometry_20261114_lifted_modes_profile.py",
        "geometry_20261114_lifted_modes_prepare.py", "geometry_20261114_full_dn_solve.py")
    report = dict(scope=__doc__, direct_boundary=direct, separated_boundary=separated_result,
        maximum_relative_directional_error=worst, maximum_second_order_relative_directional_error=coarse,
        maximum_fourth_order_relative_directional_error=worst,
        verification_threshold=5e-5, verification_estimator="two fourth-order Richardson levels",
        second_order_truncation_contracts=contracts,
        implementation_check_passed=bool(np.isfinite(worst) and worst <= 5e-5 and contracts),
        physical_test=boundary.description(), physical_test_schema=SCHEMA,
        lifted_modes_implementation=binding(M, N, accepted),
        accepted_sha256=original.sha(args.accepted), prepared_sha256=original.sha(args.prepared),
        tail_anchor_sha256=original.sha(args.tail_anchor), tail_config_sha256=original.sha(args.tail_config),
        exact_input_sha256=EXPECTED, consumed_source_sha256={name: original.sha(HERE / name) for name in source_names},
        source_sha256=original.sha(__file__), seconds=time.monotonic() - begin,
        linear_reference_source="Complete actual finite nonlinear T112 zero-H Jacobian, held affine during this implementation check",
        nonlinear_DN_evaluated=False, actual_completed_nonlinear_J_reused=True,
        ready_linear_graph_used=False, full_BVP_solved=False, full_Cartesian_closed_surface=False,
        mathematical_boundary_test_changed=True, old_material_acceptance_claim=False)
    original.write(args.out / "response-check.json", clean(report))
    print(json.dumps(dict(event="R252-complete-response", implementation_check_passed=report["implementation_check_passed"],
        maximum_relative_directional_error=worst, seconds=report["seconds"])), flush=True)
    return 0 if report["implementation_check_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
