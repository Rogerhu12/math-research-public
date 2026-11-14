#!/usr/bin/env python3
"""Solve R252 with the original complete separated-QR linear backend.

The complete original field/constant-core/scalar ODE, real prepared699,
actual native tail, original Newton and its 17 trials, RMS=1e-6 and
BC=1e-11 are retained.  All M=T112 right rows instead test the pulled-back
native slope in physical phi.  This is a new finite discretization; an
accepted R_phi is never relabelled as an accepted old R_theta.

The original complete separated-QR backend solves the entire new
linearization. Request13 measured a well-resolved new right-boundary block
on the same original Uend; the old material-test QR failure does not test
this new boundary. No cutoff, inverse projection or deleted mode is used.
Final fresh native audit, fixed-p physical RMS, old material height seam
and independent full-angle cut audit remain.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from pathlib import Path
import sys

import numpy as np

import geometry_20261114_lifted_modes_banded_full_dn as banded
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA


HERE = Path(__file__).resolve().parent
FINITE_SCHEME = "physical-phi-complete-DN-v1"
BAND_DRIVER_SHA = "390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4"


def maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value), initial=0)) if np.all(np.isfinite(value)) else None


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Execute the actual full numerical problem in public Actions")
    original = banded.continuation.original
    sha, read = original.sha, original.read
    if sha(banded.__file__) != BAND_DRIVER_SHA:
        raise ValueError("The frozen complete-band continuation source changed")
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--warm", type=Path, required=True)
    parser.add_argument("--response-check", type=Path, required=True)
    parser.add_argument("--tail-config", type=Path, required=True)
    parser.add_argument("--physical-angles", type=int, default=4096)
    parser.add_argument("--material-angles", type=int, default=4096)
    args, _ = parser.parse_known_args()
    if "--physical-angles" in sys.argv:
        index = sys.argv.index("--physical-angles")
        del sys.argv[index:index + 2]
    response = read(args.response_check)
    if (response.get("implementation_check_passed") is not True
            or response.get("verification_threshold") != 5e-5
            or response.get("physical_test_schema") != SCHEMA
            or response.get("prepared_sha256") != sha(args.warm)
            or response.get("tail_config_sha256") != sha(args.tail_config)
            or response.get("ready_linear_graph_used") is not False
            or response.get("actual_completed_nonlinear_J_reused") is not True
            or response["physical_test"]["physical_angles"] != args.physical_angles
            or response["physical_test"]["material_angles"] != args.material_angles):
        raise ValueError("Complete the new full-J affine boundary FD at the unchanged original threshold")
    for name, expected in response["consumed_source_sha256"].items():
        if sha(HERE / name) != expected:
            raise ValueError("A mathematical source changed since the actual new boundary FD: " + name)
    from geometry_20261114_physical_test_cut_audit import audit_cut
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    source_names = (Path(__file__).name, "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_physical_test_response.py", "geometry_20261114_physical_test_cut_audit.py",
        "geometry_20261114_lifted_modes_banded_full_dn.py", "geometry_20261114_banded_collocation.py",
        "geometry_20261114_lifted_modes_full_dn.py", "geometry_20261114_full_dn_solve.py",
        "geometry_20261114_full_dn_augmented.py", "geometry_20261114_full_dn_boundary.py")
    identity = dict(schema=SCHEMA, finite_boundary_scheme=FINITE_SCHEME,
        scope=__doc__, entry_source_sha256=sha(__file__),
        source_sha256={name: sha(HERE / name) for name in source_names},
        response_check_sha256=sha(args.response_check), warm_sha256=sha(args.warm),
        tail_config_sha256=sha(args.tail_config), material_angles=args.material_angles,
        physical_angles=args.physical_angles,
        boundary_residual_definition="All original left rows and R_phi = v_nonmean - cut_scale*S*D(epsilon_h*P*z_nonmean)",
        original_material_boundary_residual_definition="R_theta = P*v_nonmean - cut_scale*D(epsilon_h*P*z_nonmean), independently audited",
        old_material_test_equivalent=False, native_height_and_true_tail_unchanged=True,
        full_original_ODE_and_core_scalar_rows_retained=True,
        complete_band_LU_retained=False, original_complete_separated_QR_retained=True,
        original_17_Newton_trials_retained=True,
        unchanged_numeric_tolerances=dict(collocation_and_frozen_physical_RMS=1e-6, boundary=1e-11),
        final_true_native_full_audit_required=True,
        full_angle_cut_audit_is_a_measurement_not_an_extra_Newton_gate=True)
    plain_write = original.write
    plain_write(output / "physical-test-intent.json", identity)
    context = dict(boundary=None, final_cut_audit=None)

    def make_boundary(*positional, **keywords):
        value = PhysicalTestBoundary(*positional, physical_angles=args.physical_angles, **keywords)
        context["boundary"] = value
        return value

    original.FullDNBoundary = make_boundary
    previous_seam = original.final_height_seam

    def final_height_seam(boundary, flow, q, endpoint, native_response):
        # Preserve the original helper and its frozen-profile side effect;
        # the independently lifted wrapper also explicitly binds p* later.
        legacy = previous_seam(boundary, flow, q, endpoint, native_response)
        legacy["old_material_test_not_the_acceptance_gate"] = True
        legacy["finite_boundary_scheme"] = FINITE_SCHEME
        cut = audit_cut(boundary, flow, endpoint, native_response,
                        angular_levels=(args.material_angles, 2 * args.material_angles))
        context["final_cut_audit"] = cut
        plain_write(output / "physical-test-final-cut-audit.json", cut)
        legacy["physical_test_final_cut_audit_file"] = "physical-test-final-cut-audit.json"
        legacy["physical_test_final_cut_audit_sha256"] = sha(output / "physical-test-final-cut-audit.json")
        return legacy

    original.final_height_seam = final_height_seam

    def pending_material_report(data):
        boundary = context["boundary"]
        if boundary is None or "states" not in data:
            return None
        values = np.asarray(data["states"])
        if values.ndim != 2 or values.shape[1] != 4 * boundary.M + 5:
            return None
        endpoint = values[-1]
        core = endpoint[boundary.n:boundary.n + boundary.M]
        controls = endpoint[boundary.n + boundary.M:]
        proxy = np.zeros(boundary.n); proxy[1:boundary.M + 1] = core
        try:
            _, _, _, trace, tail, slope, J = boundary.data(proxy, endpoint[:boundary.n], controls)
            return dict(original_material_Rtheta_nonmean_max=maximum(
                trace.derivative_s - boundary.cut_scale * slope),
                tail_map_actual_nonlinear_solve=tail["actual_nonlinear_solve"],
                scope="Same current explicitly affine inner map only; not a fresh native-tail audit",
                original_material_acceptance_claim=False)
        except (ValueError, FloatingPointError, RuntimeError) as error:
            return dict(available=False, diagnostic_error=repr(error),
                        original_material_acceptance_claim=False)

    def physical_write(path, data):
        if isinstance(data, dict):
            name = Path(path).name
            if (name in ("driver-status.json", "prepared.json.gz", "actual.json.gz",
                         "lifted-modes-intent.json") or name.endswith("-pending.json.gz")):
                data["finite_boundary_scheme"] = FINITE_SCHEME
                data["boundary_residual_definition"] = identity["boundary_residual_definition"]
                data["physical_test_implementation"] = identity
                data["old_material_boundary_success_inherited"] = False
                if name in ("driver-status.json", "lifted-modes-intent.json"):
                    data["scope"] = __doc__
            if name.endswith("-pending.json.gz"):
                data["independent_original_material_test"] = pending_material_report(data)
            if name == "actual.json.gz":
                data["scope"] = __doc__
                data["message"] = ("Complete finite physical-phi Galerkin DN accepted with fresh actual tail audit; "
                    "the old material test, full angular seam and closed geometry have separate measured reports.")
                data["physical_test_final_cut_audit"] = context["final_cut_audit"]
                data["boundary_residual_max_refers_to"] = "complete new physical-phi system and unchanged left boundary"
                if context["final_cut_audit"] is None:
                    raise RuntimeError("A successful new finite test requires its independently measured cut report")
            if name == "driver-status.json" and data.get("new_coupled_finite_acceptance"):
                data["phase"] = "finite-physical-phi-DN-accepted-assembly-open"
                data["new_coupled_finite_acceptance_refers_to"] = FINITE_SCHEME
        return plain_write(path, data)

    original.write = physical_write
    # Deliberately bypass banded.main(): that function replaces the original
    # QR factor and diagnostics. The independent-mode continuation below
    # keeps its original complete QR, now with the same PhysicalTestBoundary.
    return banded.continuation.main()


if __name__ == "__main__":
    raise SystemExit(main())
