#!/usr/bin/env python3
"""Original RHS/complete-BC checks at the explicitly lifted field dimension.

Choose scalar or boundary.  The accepted source file is never rewritten or
relabelled: its M96 physical values are only initial guesses for M112.
The boundary path calls the entire original Richardson procedure and its
unchanged 5e-5 gate, with all new physical/core/tail rows.  The ready.linearD
reference remains explicitly distinguished from a real nonlinear DN J.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import json
from pathlib import Path
import sys
import numpy as np

from geometry_20261114_lifted_modes_prepare import build, validate_source, read
from geometry_20261114_lifted_modes_profile import (
    LiftedModesPrefixProfile, SCHEMA, FIELD_SCHEMA, lift_physical, sha)
from geometry_20261114_full_dn_augmented import response_check

HERE = Path(__file__).resolve().parent


def binding(M, N, accepted):
    return dict(scalar_schema=SCHEMA, field_schema=FIELD_SCHEMA,
        source_prefix_M=int(accepted["M"]), field_modes=M, tail_modes=M,
        angular_quadrature=N, original_accepted_source_relabelled=False,
        adapter_source_sha256=sha(__file__),
        profile_source_sha256=sha(HERE / "geometry_20261114_lifted_modes_profile.py"),
        original_boundary_check_source_sha256=sha(HERE / "geometry_20261114_full_dn_response.py"),
        original_RHS_source_sha256=sha(HERE / "geometry_20261114_full_dn_augmented.py"))


def scalar():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ("accepted", "port", "out"):
        p.add_argument("--" + key, type=Path, required=True)
    p.add_argument("--field-modes", type=int, default=112)
    p.add_argument("--angles", type=int, default=2048)
    p.add_argument("--peak-curvature", type=float, default=2.5)
    args = p.parse_args()
    accepted, port = read(args.accepted), read(args.port)
    profile, q, flow, core = build(accepted, port, args.field_modes, args.angles, args.peak_curvature)
    mesh = np.asarray(accepted["mesh"])
    field = lift_physical(accepted["states"], accepted["M"], q.M)
    import geometry_20261114_r225_free_core_bvp as base
    indices = np.array([0, len(mesh) // 2, len(mesh) - 1])
    before = base.BatchedFFTFlow(q)(mesh[indices], field[indices].T)
    after = flow.physical(mesh[indices], field[indices].T, np.zeros((flow.k, len(indices))))
    difference = float(np.max(abs(before - after)))
    if not np.isfinite(difference) or difference > 1e-12:
        raise ValueError("The wrapper changed the original finite RHS at the new dimension")
    checks = []
    for j, bump in enumerate(profile.bumps):
        index = int(np.argmin(abs(mesh - (bump.left + bump.right) / 2)))
        if not bump.left < mesh[index] < bump.right:
            raise ValueError("The probe must lie in its actual scalar-control support")
        item = response_check(flow, float(mesh[index]), field[index], np.zeros(flow.k), j)
        item.update(state_kind="complete-original-accepted-M96-values-embedded-as-an-unaccepted-M112-initial-state",
                    source_accepted_node=index, source_modes=int(accepted["M"]),
                    control_support=[bump.left, bump.right])
        checks.append(item)
    report = dict(scope=__doc__, lifted_modes_implementation=binding(q.M, q.N, accepted),
        scalar_profile=profile.description(), physical_state_dimension=flow.n,
        augmented_state_dimension=flow.dimension, left_rows=3 * q.M + 5, right_rows=q.M,
        zero_control_original_RHS_max_difference=difference,
        scalar_control_directional_checks=checks, accepted_sha256=sha(args.accepted),
        new_field_accepted=False, full_DN_evaluated=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    print(json.dumps(dict(M=q.M, N=q.N, zero_control_original_RHS_max_difference=difference)), flush=True)
    return 0


def boundary():
    def path(name):
        return Path(sys.argv[sys.argv.index(name) + 1])
    accepted, prepared = read(path("--accepted")), read(path("--prepared"))
    validate_source(accepted)
    M, N = int(prepared["M"]), int(prepared["N"])
    if (prepared.get("field_representation", {}).get("schema") != FIELD_SCHEMA
            or prepared["complete_scalar_profile"].get("schema") != SCHEMA
            or int(prepared["complete_scalar_profile"]["base_prefix_M"]) != int(accepted["M"])
            or int(prepared["complete_scalar_profile"]["field_modes"]) != M
            or int(prepared["complete_scalar_profile"]["tail_modes"]) != M):
        raise ValueError("Use the correctly bound complete new-dimensional prepared field")
    import geometry_20261114_full_dn_response as original
    original_constructor = original.original.native.outward.FullCoreProbe
    def constructor(core, source_M, source_N, velocity, length, k0):
        if (int(source_M), int(source_N)) != (int(accepted["M"]), int(accepted["N"])):
            raise ValueError("The source identity changed inside the original response setup")
        padded = np.pad(np.asarray(core), (0, M - source_M))
        return original_constructor(padded, M, N, velocity, length, k0)
    def profile(source, port, peak, source_tail_modes):
        if int(source_tail_modes) != int(accepted["M"]):
            raise ValueError("Do not reinterpret the old source's mode count as new controls")
        return LiftedModesPrefixProfile(source, port, peak, M)
    # Only setup dimensions and their explicit scalar identity differ.  The
    # complete original direct/augmented BC, FD directions, three steps,
    # extrapolation, acceptance threshold and reference label run unchanged.
    original.CompleteProfile = profile
    original.original.native.outward.FullCoreProbe = constructor
    original.__file__ = __file__
    result = original.main()
    output = path("--out") / "response-check.json"
    record = json.loads(output.read_text())
    record["lifted_modes_implementation"] = binding(M, N, accepted)
    output.write_text(json.dumps(record, indent=2, allow_nan=False) + "\n")
    return result


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Execute numerical responses only in the public repository's Actions")
    if len(sys.argv) < 2 or sys.argv[1] not in ("scalar", "boundary"):
        raise ValueError("Choose scalar or boundary, followed by its explicit original arguments")
    action = sys.argv.pop(1)
    return scalar() if action == "scalar" else boundary()


if __name__ == "__main__":
    raise SystemExit(main())
