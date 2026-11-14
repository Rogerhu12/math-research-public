#!/usr/bin/env python3
"""Actual R240 same-g refinement with all cores free and no design controls.

--accepted remains the original accepted96 design-source file required by
the unchanged underlying driver.  --parent-field is the genuinely accepted
complete design/refinement being refined, independently bound to its true
final tail audit and input config.  The new prepared v4 state freezes that
entire scalar metric, releases every core, and has exactly M true DN rows.

The original outer actual-tail iteration, complete native J/audit,
separated QR, Newton/line search and 1e-6/1e-11 acceptance gates all run.
This is a finite same-metric refinement calculation, not a predeclared
geometry or continuous-frequency certificate.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import copy
import json
from pathlib import Path
import sys

import numpy as np
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_prefix_controls import rms_domain
from geometry_20261114_lifted_modes_prepare import validate_source, domain_minimum
from geometry_20261114_lifted_modes_profile import field_spec, sha
from geometry_20261114_same_metric_profile import SCHEMA, freeze_spec, reconstruct_profile
from geometry_20261114_same_metric_prepare import validate_parent

HERE = Path(__file__).resolve().parent


def argument(name, remove=False):
    if name not in sys.argv:
        raise ValueError("Same-g refinement requires " + name)
    index = sys.argv.index(name)
    result = Path(sys.argv[index + 1])
    if remove:
        del sys.argv[index:index + 2]
    return result


def install_diagnostics(output, write):
    base = original.original_qr.DiskQRFactor
    counter = 0
    class Factor(base):
        def finish(self):
            nonlocal counter
            counter += 1
            try:
                small = self.right @ self.U[-1]
                U, values, Vh = np.linalg.svd(small, full_matrices=False)
                packet = output / f"same-g-reduced-{counter:03d}.npz"
                np.savez_compressed(packet, small=small, U=U, singular_values=values, Vh=Vh,
                                    nullspace_left=self.U[0], nullspace_right=self.U[-1],
                                    boundary_right=self.right)
                write(output / f"same-g-reduced-{counter:03d}.json", dict(
                    field_and_tail_modes=self.k, state_dimension=self.n, nodes=self.m,
                    left_rows=self.nl, right_rows=self.k, fixed_core_modes=0, active_scalar_parameters=0,
                    singular_values=values.tolist(),
                    reduced_condition=float(values[0] / values[-1]) if values[-1] else None,
                    packet_sha256=sha(packet), original_factor_and_linear_residual_check_unchanged=True,
                    mathematical_rank_certified=False))
            except Exception as error:
                print(json.dumps(dict(event="optional_same_g_QR_diagnostic_error", exception=repr(error))), flush=True)
            # All actual LU/QR/linear-residual failures remain original.
            return super().finish()
    original.original_qr.DiskQRFactor = Factor


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Use this public repository's Actions for numerical refinement")
    parent_path = argument("--parent-field", True)
    parent_tail_path = argument("--parent-tail-response", True)
    parent_config_path = argument("--parent-tail-config", True)
    response_path = argument("--response-check", True)
    design_path, warm_path, port_path, output = (argument(name) for name in ("--accepted", "--warm", "--port", "--out"))
    design, parent, warm, response = (original.read(path) for path in
                                     (design_path, parent_path, warm_path, response_path))
    validate_source(design)
    parent_binding = validate_parent(parent, parent_path, parent_tail_path, parent_config_path)
    M, N = int(warm["M"]), int(warm["N"])
    scalar = freeze_spec(parent, M, sha(parent_path))
    specification = scalar["frozen_design_scalar_profile"]
    if (warm.get("complete_scalar_profile") != scalar
            or warm.get("parent_binding") != parent_binding
            or warm.get("field_representation") != field_spec(M, N)
            or warm.get("fixed_core_modes") != 0 or warm.get("active_scalar_parameters") != 0
            or N < int(parent["N"]) or N < 4 * M + 4 or N % 2
            or scalar["accepted_source_prefix_sha256"] != sha(design_path)
            or specification["base_prefix_geometry"] != design["fixed_scalar_profile"]["geometry"]
            or scalar["complete_original_port"] != original.read(port_path)):
        raise ValueError("The parent, frozen whole scalar metric, original source or complete warm differs")
    identity = scalar["canonical_scalar_identity_sha256"]
    check = response.get("same_metric_implementation", {})
    if (response.get("implementation_check_passed") is not True
            or response.get("verification_threshold") != 5e-5
            or response.get("prepared_sha256") != sha(warm_path)
            or response.get("accepted_sha256") != sha(parent_path)
            or check.get("canonical_scalar_identity_sha256") != identity
            or check.get("field_modes") != M or check.get("tail_modes") != M
            or check.get("angular_quadrature") != N or check.get("fixed_core_modes") != 0
            or check.get("active_scalar_parameters") != 0):
        raise ValueError("Complete the original full K=k=0 boundary FD on this exact prepared field first")
    profile_model = reconstruct_profile(scalar)
    mesh = np.asarray(warm["mesh"])
    values = np.asarray(warm.get("augmented_states", warm["states"]))
    rhs = np.asarray(warm.get("augmented_rhs", warm["rhs"]))
    if (values.shape != (len(mesh), 4 * M + 2) or rhs.shape != values.shape
            or profile_model.parameter_count != 0 or profile_model.tail_modes != M):
        raise ValueError("Same-g state must contain all physical/core rows and no scalar-control rows")
    native_config = original.read(argument("--tail-config"))
    parent_config = original.read(parent_config_path)
    if (int(native_config["modes"]) != M
            or int(native_config["quadrature"]) < int(parent_config["quadrature"])):
        raise ValueError("Use the full new tail dimension without coarsening its angle quadrature")
    output.mkdir(parents=True, exist_ok=True)
    write_original = original.write
    source_names = ("geometry_20261114_full_dn_solve.py", "geometry_20261114_full_dn_augmented.py",
        "geometry_20261114_full_dn_boundary.py", "geometry_20261114_separated_qr_bvp.py",
        "geometry_20261114_same_metric_profile.py", "geometry_20261114_same_metric_prepare.py",
        "geometry_20261114_same_metric_response.py")
    binding = dict(scope=__doc__, source_sha256=sha(__file__),
        source_sha256s={name: sha(HERE / name) for name in source_names},
        parent_binding=parent_binding, original_accepted_source_sha256=sha(design_path),
        prepared_sha256=sha(warm_path), full_BC_response_sha256=sha(response_path),
        canonical_scalar_identity_sha256=identity, frozen_design_parameters=scalar["frozen_design_parameters"],
        field_modes=M, angular_quadrature=N, tail_modes=M,
        fixed_core_modes=0, active_scalar_parameters=0,
        state_dimension=4 * M + 2, left_rows=3 * M + 2, right_rows=M,
        unchanged_acceptance=dict(RMS=1e-6, BC=1e-11, original_Newton_and_line_search=True,
                                  complete_new_tail_J_and_final_native_audit=True))
    write_original(output / "same-metric-intent.json", binding)
    def write(path, data):
        if isinstance(data, dict):
            name = Path(path).name
            if name in ("driver-status.json", "prepared.json.gz", "actual.json.gz") or name.endswith("-pending.json.gz"):
                data["field_representation"] = field_spec(M, N)
                data["same_metric_implementation"] = binding
                data["fixed_core_modes"] = 0
                data["active_scalar_parameters"] = 0
                data["canonical_scalar_identity_sha256"] = identity
            if name == "actual.json.gz":
                data["fixed_modes"] = 0
                data["same_metric_refinement"] = True
                data["source_same_metric_parent"] = parent_binding
                data["frozen_design_parameters"] = scalar["frozen_design_parameters"]
                data["constant_parameter_state_drift"] = 0.
                data["sampled_geometry_scalar_identity_sha256"] = identity
                data["sampled_geometry_scope"] = "Original finite point samples on the same completely frozen scalar function; no active controls or continuous certificate."
        write_original(path, data)
    original.write = write
    original.__file__, original.__doc__ = __file__, __doc__
    constructor = original.original_solver.native.outward.FullCoreProbe
    boundary_constructor = original.FullDNBoundary
    def probe(core, source_M, source_N, velocity, length, k0):
        if (int(source_M), int(source_N)) != (int(design["M"]), int(design["N"])):
            raise ValueError("Do not relabel the original accepted96 source to pass its original guard")
        # The real new initial states/core come from the full accepted parent
        # in --warm.  The old setup's coefficients are only constructor data;
        # the finite RHS is local in the complete physical state.
        return constructor(np.pad(np.asarray(core), (0, M - source_M)), M, N, velocity, length, k0)
    def profile(source, port, peak, source_modes):
        if (port != scalar["complete_original_port"]
                or peak != specification["peak_curvature"]
                or int(source_modes) != int(design["M"])):
            raise ValueError("The completely frozen scalar formula must remain identical")
        return profile_model
    def boundary(profile, unused_old_design_targets, *args, **kwargs):
        return boundary_constructor(profile, np.empty(0), *args, **kwargs)
    def frozen_spec(profile, port, active_parameters, source_sha):
        if (np.asarray(active_parameters).shape != (0,) or source_sha != sha(design_path)
                or port != scalar["complete_original_port"]):
            raise ValueError("An active parameter or altered original source entered a frozen-metric refinement")
        return copy.deepcopy(scalar)
    original.original_solver.native.outward.FullCoreProbe = probe
    original.CompleteProfile, original.FullDNBoundary, original.scalar_spec = profile, boundary, frozen_spec
    base_seam = original.final_height_seam
    def seam(boundary, flow, q, endpoint, response):
        result = base_seam(boundary, flow, q, endpoint, response)
        q.profile = profile_model.profile
        return result
    original.final_height_seam = seam
    curve = CubicHermiteSpline(mesh, values, rhs, axis=0)
    original.prepared_guess = lambda source, profile, flow, step, taper: (
        mesh.copy(), lambda x: curve(x), dict(kind="actual-same-metric-complete-preflight-reused",
            parent_sha256=sha(parent_path), prepared_sha256=sha(warm_path), scalar_identity=identity,
            fixed_core_modes=0, active_scalar_parameters=0))
    base_preflight = original.preflight
    def preflight(x, at, flow, max_nodes):
        additions, history = [], []
        for iteration in range(16):
            x, yy, ff, residual, new = base_preflight(x, at, flow, max_nodes)
            additions.extend(new)
            bad, checks = rms_domain(x, yy, ff, flow)
            history.append(dict(iteration=iteration, nodes=len(x), invalid_RMS_points=len(bad), checks=checks))
            report = dict(history=history, added_nodes=additions, canonical_scalar_identity_sha256=identity)
            write_original(output / "RMS-domain-preflight.json", report)
            if not len(bad):
                interpolant = CubicHermiteSpline(x, yy, ff, axis=0)
                minima = dict(nodes=domain_minimum(flow, x, yy))
                for fraction in (.5, .5 - .5 * np.sqrt(3 / 7), .5 + .5 * np.sqrt(3 / 7)):
                    points = x[:-1] + fraction * np.diff(x)
                    minima[str(float(fraction))] = domain_minimum(flow, points, interpolant(points))
                report.update(complete_preflight_passed=True, actual_query_minima=minima)
                write_original(output / "RMS-domain-preflight.json", report)
                return x, yy, ff, residual, additions
            revised = original.original_solver.merge_mesh(x, bad)
            if len(revised) == len(x) or len(revised) > max_nodes:
                raise FloatingPointError("The actual refinement RMS-query domain exceeds its declared budget")
            additions.extend(float(s) for s in revised if s not in set(x))
            x = revised
        raise FloatingPointError("The complete same-g RMS query domain did not resolve")
    original.preflight = preflight
    install_diagnostics(output, write_original)
    return original.main()


if __name__ == "__main__":
    raise SystemExit(main())
