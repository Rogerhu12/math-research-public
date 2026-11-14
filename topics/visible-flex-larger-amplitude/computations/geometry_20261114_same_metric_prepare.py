#!/usr/bin/env python3
"""Prepare a same-material-metric refinement of a genuinely accepted full DN.

All original design controls and the complete scalar function are frozen.
Every core coefficient is free, and there are zero active scalar controls.
The parent physical C2 quintic is formed from its complete saved y/RHS and
the same original finite-ODE second-jet rule; refinement only lifts that
entire initial field and optionally subdivides its mesh.  A prepared or
failed parent is rejected before any numerical work starts.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import json
from pathlib import Path
import time
import traceback
import numpy as np

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_augmented import AugmentedFlow
from geometry_20261114_large_core_saved_prefix import PhysicalQuintic
from geometry_20261114_lifted_modes_profile import field_spec, lift_physical, sha
from geometry_20261114_lifted_modes_prepare import complete_preflight
from geometry_20261114_same_metric_profile import SCHEMA, freeze_spec, reconstruct_profile

HERE = Path(__file__).resolve().parent
read, write = original.read, original.write


def validate_parent(parent, parent_path, tail_path, config_path):
    """Bind actual acceptance and the producer's complete final-audit bytes."""
    limits = (("collocation_rms_max", 1e-6), ("boundary_residual_max", 1e-11),
              ("physical_frozen_control_RMS_max", 1e-6))
    if (parent.get("success") is not True or parent.get("status") != 0
            or not parent.get("actual_tail")
            or any(not isinstance(parent.get(key), (int, float))
                   or not np.isfinite(parent[key]) or not 0 <= parent[key] <= bound
                   for key, bound in limits)):
        raise ValueError("Only a genuinely accepted complete full-DN field may define this same-g refinement")
    M, N = int(parent["M"]), int(parent["N"])
    if parent.get("field_representation") != field_spec(M, N):
        raise ValueError("The parent is not the complete finite rotating-phi physical field")
    n = 3 * M + 2
    x, y, dy = (np.asarray(parent[key], float) for key in ("mesh", "states", "rhs"))
    core = np.asarray(parent["core"]["coefficients"], float)
    if (x.ndim != 1 or len(x) < 2 or np.any(np.diff(x) <= 0)
            or y.shape != (len(x), n) or dy.shape != y.shape or core.shape != (M,)
            or not all(np.all(np.isfinite(v)) for v in (x, y, dy, core))):
        raise ValueError("The accepted parent lost a physical, full mean-height, or core coefficient")
    if sha(tail_path) != parent["actual_tail"]["final_response_sha256"]:
        raise ValueError("Supply the actual producer-bound final audited tail response")
    if sha(config_path) != parent["actual_tail"]["sources"]["input_config"]:
        raise ValueError("Supply the original input configuration bound by that actual tail producer")
    tail, config = read(tail_path), read(config_path)
    if (int(config["modes"]) != M or tail.get("converged") is not True
            or tail.get("actual_nonlinear_solve") is not True
            or tail.get("finite_tail_only") is not True or tail.get("failed")
            or not isinstance(tail.get("residual"), (int, float))
            or not np.isfinite(tail["residual"])
            or not 0 <= tail["residual"] < float(config["solveTolerance"])):
        raise ValueError("The parent's complete true finite tail did not pass its unchanged native gate")
    for key in ("height", "slope", "second"):
        value = np.asarray(tail["jets"][key], float)
        if value.shape != (M,) or not np.all(np.isfinite(value)):
            raise ValueError("The parent tail lost a full jet: " + key)
    for key in ("meanSlope", "meanSecond", "meanSlopeCorrection", "meanSecondCorrection"):
        if not isinstance(tail["jets"].get(key), (int, float)) or not np.isfinite(tail["jets"][key]):
            raise ValueError("The parent tail lost a complete mean jet: " + key)
    J = np.asarray(tail.get("heightJetJacobian"), float)
    H = np.asarray(tail.get("checkpoint", {}).get("cutHeight"), float)
    if (J.shape != ((3 * M + 2) * M,) or H.shape != (M,)
            or not np.all(np.isfinite(J)) or not np.all(np.isfinite(H))):
        raise ValueError("The parent's full true tail H/J must be retained")
    audit = tail.get("audit")
    keys = ("fullD", "normalizedFullDefect", "minLeading", "minD", "formalCurvature",
            "maxPhysicalPV", "actualMetric", "holonomy")
    if not isinstance(audit, dict) or any(not isinstance(audit.get(key), (int, float))
                                        or not np.isfinite(audit[key]) for key in keys):
        raise ValueError("The source-bound final full finite audit is incomplete")
    # The bare response has no request.audit flag.  Its exact SHA is bound
    # to the original accepted full-DN producer's final audit path; no such
    # absent flag is invented, and no T96/T112 response is lifted to new M.
    return dict(parent_sha256=sha(parent_path), parent_field_modes=M, parent_angles=N,
                parent_tail_response_sha256=sha(tail_path), parent_tail_input_config_sha256=sha(config_path),
                parent_tail_quadrature=int(config["quadrature"]), parent_tail_residual=tail["residual"],
                full_audit_fields=list(keys), final_audit_binding="Exact SHA from actual_tail.final_response_sha256 and the accepted original producer path",
                new_tail_response_not_created=True)


def build(parent, scalar, M, N, workers=1):
    if N < int(parent["N"]) or N < 4 * M + 4 or N % 2:
        raise ValueError("The new FFT projection must retain every field frequency")
    profile = reconstruct_profile(scalar)
    if profile.M != M or profile.tail_modes != M or profile.parameter_count != 0:
        raise ValueError("Same-g refinement has M=T and no active scalar control")
    source_M = int(parent["M"])
    core = np.pad(np.asarray(parent["core"]["coefficients"]), (0, M - source_M))
    law = parent["original_metric_identity"]["law"]
    q = original.original_solver.native.outward.FullCoreProbe(core, M, N,
        law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    return profile, q, AugmentedFlow(q, profile, workers), core


def parent_quintic(parent):
    """The same saved-RHS C2 convention used for actual complete fields."""
    M, N = int(parent["M"]), int(parent["N"])
    profile = reconstruct_profile(parent["fixed_scalar_profile"]["geometry"])
    law = parent["original_metric_identity"]["law"]
    q = original.original_solver.native.outward.FullCoreProbe(np.asarray(parent["core"]["coefficients"]),
        M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    x, y, dy = (np.asarray(parent[key], float) for key in ("mesh", "states", "rhs"))
    ddy, gap = [], 0.
    for s, value, derivative in zip(x, y, dy):
        frame = q.frame(float(s), value)
        local = q.project(frame["V"])
        gap = max(gap, float(np.max(abs(local - derivative))))
        state = q.project(q.frame(float(s), value.astype(complex) + 1j * 1e-25 * derivative,
                                  strict=False)["V"]).imag / 1e-25
        da = -frame["app"] / (frame["a"] * frame["kap"]) + frame["ap"] ** 2 / (frame["a"] ** 2 * frame["kap"])
        db = -frame["al"] * da / frame["be"]
        ddy.append(state + q.project(da[:, None] * frame["N"] + db[:, None] * frame["B"]))
    return PhysicalQuintic(x, y, dy, np.asarray(ddy)), gap


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("parent-field", "parent-tail-response", "parent-tail-config", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--field-modes", type=int, required=True)
    parser.add_argument("--angles", type=int, required=True)
    parser.add_argument("--subdivisions", type=int, default=1)
    parser.add_argument("--max-nodes", type=int, default=1200)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Refinement computations belong to the public repository's Actions")
    if args.subdivisions < 1:
        raise ValueError("Use a positive mesh subdivision count")
    parent = read(args.parent_field)
    binding = validate_parent(parent, args.parent_field, args.parent_tail_response, args.parent_tail_config)
    scalar = freeze_spec(parent, args.field_modes, sha(args.parent_field))
    profile, q, flow, core = build(parent, scalar, args.field_modes, args.angles)
    args.out.mkdir(parents=True, exist_ok=True)
    begin = time.monotonic()
    state = dict(scope=__doc__, phase="preparing-same-metric-refinement", source_sha256=sha(__file__),
        source_repository=os.environ.get("GITHUB_REPOSITORY"), source_commit=os.environ.get("GITHUB_SHA"),
        parent_binding=binding, complete_scalar_profile=scalar, field_representation=field_spec(q.M, q.N),
        state_dimension=flow.dimension, left_rows=3 * q.M + 2, right_rows=q.M,
        active_scalar_parameters=0, fixed_core_modes=0, success=False)
    write(args.out / "driver-status.json", state)
    try:
        source, source_gap = parent_quintic(parent)
        old_x = np.asarray(parent["mesh"])
        extra = [old_x[:-1] + j * np.diff(old_x) / args.subdivisions for j in range(1, args.subdivisions)]
        points = np.r_[profile.knots, *extra] if extra else np.asarray(profile.knots)
        mesh = original.original_solver.merge_mesh(old_x, points)
        if len(mesh) > args.max_nodes:
            raise ValueError("The explicitly requested refinement mesh exceeds its declared node budget")
        def initial_at(points):
            values = np.zeros((len(points), flow.dimension))
            values[:, :flow.n] = lift_physical(source(points).T, parent["M"], q.M)
            values[:, flow.core_slice] = core
            return values
        mesh, values, rhs, residual, additions = complete_preflight(mesh, initial_at, flow, args.max_nodes, args.out)
        prepared = dict(scope="Same fixed scalar metric; complete higher-resolution initial guess, not an accepted new field.",
            M=q.M, N=q.N, mesh=mesh.tolist(), states=values.tolist(), rhs=rhs.tolist(),
            field_representation=field_spec(q.M, q.N), complete_scalar_profile=scalar,
            state_layout="All 3M+2 physical rows including z0, then M constant core rows; no active scalar rows.",
            parent_binding=binding, parent_saved_vs_local_RHS_max=source_gap,
            initial_collocation_max=original.finite_max(residual), preflight_added_nodes=additions,
            original_parent_nodes_preserved=bool(np.all(np.isin(old_x, mesh))),
            source_field_interpolation="Original complete physical C2 quintic from saved y, saved RHS and original second-jet rule",
            fixed_core_modes=0, active_scalar_parameters=0,
            original_metric_identity=parent["original_metric_identity"],
            source_sha256=sha(__file__), success=False, same_metric_refinement_initial_guess=True)
        write(args.out / "prepared.json.gz", prepared)
        state.update(phase="same-metric-full-preflight-passed", nodes=len(mesh),
                     prepared_sha256=sha(args.out / "prepared.json.gz"),
                     initial_collocation_max=prepared["initial_collocation_max"])
        return 0
    except Exception as error:
        state.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        state["elapsed_seconds"] = time.monotonic() - begin
        write(args.out / "driver-status.json", state)


if __name__ == "__main__":
    raise SystemExit(main())
