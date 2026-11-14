#!/usr/bin/env python3
"""Prepare an explicitly unaccepted higher-mode full-DN initial guess.

The actual accepted source remains M96/N1024.  Every old prefix coefficient
and every old full-interval mesh node is retained; the later circular seed
is freshly projected with all 112 physical modes.  The actual original
finite RHS is checked at every node, midpoint and both Lobatto RMS points.
No tail or QR solve is started here, so this output can be reused while the
independent T112 zero-height/J/audit calculation is running.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from pathlib import Path
import time
import traceback

import numpy as np
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_augmented import AugmentedFlow
from geometry_20261114_full_dn_prefix_controls import rms_domain
from geometry_20261114_lifted_modes_profile import (
    LiftedModesPrefixProfile, scalar_spec, field_spec, lift_physical, sha)

HERE = Path(__file__).resolve().parent
read, write = original.read, original.write


def validate_source(accepted):
    if (accepted.get("success") is not True or accepted.get("status") != 0
            or (int(accepted["M"]), int(accepted["N"])) != (96, 1024)
            or not 0 <= accepted["collocation_rms_max"] <= 1e-6
            or not 0 <= accepted["boundary_residual_max"] <= 1e-11):
        raise ValueError("Retain the actual accepted M96/N1024 source prefix identity")


def build(accepted, port, M, N, peak, workers=1):
    validate_source(accepted)
    if M < accepted["M"] or N < 4 * M + 4 or N % 2:
        raise ValueError("Keep every old mode and the original resolved even-angle projection")
    profile = LiftedModesPrefixProfile(accepted, port, peak, M)
    law = accepted["original_metric_identity"]["law"]
    core = np.pad(np.asarray(accepted["core"]["coefficients"]), (0, M - accepted["M"]))
    q = original.original_solver.native.outward.FullCoreProbe(
        core, M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    return profile, q, AugmentedFlow(q, profile, workers), core


def make_seed(accepted, profile, flow, step, taper, source_warm=None):
    M0, M = int(accepted["M"]), flow.M
    core = np.pad(np.asarray(accepted["core"]["coefficients"]), (0, M - M0))
    # This object supplies values to the old analytic seed constructor only.
    # It is deliberately not an accepted BVP, nor passed to its acceptance
    # check or to the scalar constructor.
    embedding = dict(success=False, M=M, N=flow.q.N,
        mesh=accepted["mesh"], states=lift_physical(accepted["states"], M0, M),
        rhs=lift_physical(accepted["rhs"], M0, M), core=dict(coefficients=core))
    mesh, analytic, info = original.prepared_guess(embedding, profile, flow, step, taper)
    source_x, source_values = np.asarray(accepted["mesh"]), np.asarray(accepted["states"])
    source_derivatives = np.asarray(accepted["rhs"])
    n0 = 3 * M0 + 2
    if source_warm is not None:
        if (int(source_warm["M"]), int(source_warm["N"])) != (M0, int(accepted["N"])):
            raise ValueError("The preserved whole mesh must come from the original source warm")
        source_x = np.asarray(source_warm["mesh"])
        vv = np.asarray(source_warm.get("augmented_states", source_warm["states"]))
        ff = np.asarray(source_warm.get("augmented_rhs", source_warm["rhs"]))
        if (vv.shape != (len(source_x), n0 + M0 + 3) or ff.shape != vv.shape
                or np.any(vv[:, -3:] != 0)
                or not np.all(vv[:, n0:n0 + M0] == core[:M0])
                or source_warm["complete_scalar_profile"]["base_prefix_geometry"] != profile.fixed_geometry
                or source_x[0] != 0 or abs(source_x[-1] - profile.end) > 1e-12):
            raise ValueError("Do not reinterpret an unrelated/nonzero-control source warm")
        source_values, source_derivatives = vv[:, :n0], ff[:, :n0]
        mesh = original.original_solver.merge_mesh(source_x, mesh)
    source_curve = CubicHermiteSpline(source_x, source_values, source_derivatives, axis=0)
    def initial_at(points):
        points = np.asarray(points)
        answer = analytic(points)
        prefix = points <= profile.prefix_end
        if np.any(prefix):
            xp = points[prefix]
            old = source_curve(xp)
            where = np.searchsorted(source_x, xp)
            safe = np.minimum(where, len(source_x) - 1)
            exact = (where < len(source_x)) & (source_x[safe] == xp)
            old[exact] = source_values[where[exact]]
            answer[prefix, :flow.n] = lift_physical(old, M0, M)
        return answer
    info.update(source_prefix_modes=M0, new_field_modes=M,
                source_prefix_is_still_accepted_only_at_its_original_modes=True,
                lifted_prefix_is_only_an_initial_guess=True,
                source_full_interval_nodes_retained=len(source_x) if source_warm is not None else None,
                source_prefix_saved_values_retained_exactly=True,
                extension_recomputed_at_new_field_modes=True,
                all_new_core_coefficients_initially_zero=True)
    return mesh, initial_at, info


def domain_minimum(flow, points, values):
    """Read the original point-domain expression in bounded-size batches."""
    worst = None
    q = flow.q
    fft = original.original_solver.BatchedFFTFlow(q)
    for start in range(0, len(points), 24):
        x = np.asarray(points[start:start + 24])
        y = np.asarray(values[start:start + 24])
        d, dd = fft.synth_real(y[:, :flow.n].T)
        lam2 = np.sum(d * d, axis=-1)
        tangent = d / np.sqrt(lam2)[..., None]
        normal = dd - np.sum(dd * tangent, axis=-1)[..., None] * tangent
        curvature = np.sqrt(np.sum(normal * normal, axis=-1)) / lam2
        jets = flow.scalar_jets(x, y[:, flow.parameter_slice].T)
        beta2 = 1 - (jets[:, 1, None] / (jets[:, 0, None] * curvature)) ** 2
        i, j = np.unravel_index(np.argmin(beta2), beta2.shape)
        item = dict(minimum_beta_squared=float(beta2[i, j]), s=float(x[i]),
                    phi=float(2 * np.pi * j / q.N), a=float(jets[i, 0]), ap=float(jets[i, 1]))
        if worst is None or item["minimum_beta_squared"] < worst["minimum_beta_squared"]:
            worst = item
    return worst


def complete_preflight(mesh, initial_at, flow, max_nodes, output):
    original_mesh = np.array(mesh, copy=True)
    history, additions = [], []
    for iteration in range(16):
        mesh, values, rhs, residual, new = original.preflight(mesh, initial_at, flow, max_nodes)
        additions.extend(new)
        bad, rows = rms_domain(mesh, values, rhs, flow)
        history.append(dict(iteration=iteration, nodes=len(mesh), invalid_RMS_points=len(bad), checks=rows))
        report = dict(scope="Every actual original finite-RHS node/midpoint/Lobatto query; finite samples, not a continuous certificate.",
                      field_modes=flow.M, angular_quadrature=flow.q.N,
                      history=history, added_nodes=additions,
                      every_input_mesh_node_retained=bool(np.all(np.isin(original_mesh, mesh))))
        write(output / "RMS-domain-preflight.json", report)
        if not len(bad):
            curve = CubicHermiteSpline(mesh, values, rhs, axis=0)
            checks = dict(nodes=domain_minimum(flow, mesh, values))
            for fraction in (.5, .5 - .5 * np.sqrt(3 / 7), .5 + .5 * np.sqrt(3 / 7)):
                points = mesh[:-1] + fraction * np.diff(mesh)
                checks[str(float(fraction))] = domain_minimum(flow, points, curve(points))
            report.update(complete_preflight_passed=True, actual_query_minima=checks)
            write(output / "RMS-domain-preflight.json", report)
            return mesh, values, rhs, residual, additions
        revised = original.original_solver.merge_mesh(mesh, bad)
        if len(revised) == len(mesh) or len(revised) > max_nodes:
            raise FloatingPointError("The actual complete RMS-query domain exceeds the unchanged node budget")
        additions.extend(float(x) for x in revised if x not in set(mesh))
        mesh = revised
    raise FloatingPointError("The actual full RMS-query domain did not resolve")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "port", "out"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--source-warm", type=Path)
    p.add_argument("--field-modes", type=int, default=112)
    p.add_argument("--angles", type=int, default=2048)
    p.add_argument("--peak-curvature", type=float, default=2.5)
    p.add_argument("--extension-step", type=float, default=.005)
    p.add_argument("--taper-fraction", type=float, default=.4)
    p.add_argument("--max-nodes", type=int, default=1200)
    args = p.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Numerical preparation belongs to the public repository's Actions")
    for filename, digest in original.FROZEN_SOURCES.items():
        if sha(HERE / filename) != digest:
            raise ValueError("Original mathematical source changed: " + filename)
    accepted, port = read(args.accepted), read(args.port)
    source_warm = read(args.source_warm) if args.source_warm else None
    if source_warm is not None and source_warm["complete_scalar_profile"]["accepted_prefix_sha256"] != sha(args.accepted):
        raise ValueError("The source whole warm is bound to another accepted prefix file")
    profile, q, flow, core = build(accepted, port, args.field_modes, args.angles, args.peak_curvature)
    args.out.mkdir(parents=True, exist_ok=True)
    begin = time.monotonic()
    state = dict(scope=__doc__, phase="preparing", source_sha256=sha(__file__),
        source_repository=os.environ.get("GITHUB_REPOSITORY"), source_commit=os.environ.get("GITHUB_SHA"),
        accepted_input_sha256=sha(args.accepted), accepted_input_modes=int(accepted["M"]),
        source_warm_sha256=sha(args.source_warm) if args.source_warm else None,
        port_sha256=sha(args.port), scalar_profile=profile.description(),
        field_representation=field_spec(q.M, q.N), state_dimension=flow.dimension,
        left_rows=3 * flow.M + 5, right_rows=profile.tail_modes,
        source_original_functions_sha256={name: sha(HERE / name) for name in (
            "geometry_20261114_full_dn_solve.py", "geometry_20261114_full_dn_prefix_controls.py",
            "geometry_20261114_full_dn_augmented.py", "geometry_20261114_lifted_modes_profile.py")},
        new_coupled_finite_acceptance=False)
    write(args.out / "driver-status.json", state)
    try:
        mesh, initial_at, info = make_seed(accepted, profile, flow, args.extension_step,
                                          args.taper_fraction, source_warm)
        state["initial_guess"] = info
        mesh, values, rhs, residual, additions = complete_preflight(mesh, initial_at, flow, args.max_nodes, args.out)
        prepared = dict(scope="New higher-mode full initial guess; no BVP or tail acceptance.",
            M=q.M, N=q.N, mesh=mesh.tolist(), states=values.tolist(), rhs=rhs.tolist(),
            state_layout="All 3M+2 physical rows including z0, then M constant core rows, then 3 constant scalar rows.",
            field_representation=field_spec(q.M, q.N), initial_guess=info,
            initial_collocation_max=original.finite_max(residual), preflight_added_nodes=additions,
            complete_scalar_profile=scalar_spec(profile, port, values[-1, flow.parameter_slice], sha(args.accepted)),
            source_accepted_prefix=dict(M=int(accepted["M"]), N=int(accepted["N"]), sha256=sha(args.accepted)),
            source_warm_sha256=state["source_warm_sha256"], source_sha256=sha(__file__),
            success=False, complete_closed_surface=False)
        write(args.out / "prepared.json.gz", prepared)
        state.update(phase="prepared-full-interval", nodes=len(mesh),
                     initial_collocation_max=prepared["initial_collocation_max"],
                     prepared_sha256=sha(args.out / "prepared.json.gz"))
        print(__import__("json").dumps(dict(event="lifted_full_profile_prepared", M=q.M, N=q.N,
              nodes=len(mesh), initial_collocation_max=prepared["initial_collocation_max"])), flush=True)
        return 0
    except Exception as error:
        state.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        state["elapsed_seconds"] = time.monotonic() - begin
        write(args.out / "driver-status.json", state)


if __name__ == "__main__":
    raise SystemExit(main())
