#!/usr/bin/env python3
"""Same fixed-g R252 refinement with one actual live TailClient throughout.

--with-response first computes the new complete native H/J at the exact
prepared endpoint and verifies the original affine boundary chain rule.
The identical live client and frozen scalar object then enter the existing
v4 full solver.  Its native predictor is preserved in memory.  There is no
nonzero checkpoint-cache import and no rounding of heights.  The original
complete QR, or the existing complete pivoted band LU, solves all rows.

Original full and frozen-physical RMS=1e-6, BC=1e-11, Newton/backtracking,
all new-H nonlinear tail solves and the final fresh audit remain.  R_phi
acceptance is explicitly distinct from the independently measured R_theta
and full-angle seam defects.  This entry does not declare closed geometry,
frequency convergence, a continuous metric bound, reach or task completion.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import json
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np

import geometry_20261114_same_metric_full_dn as sameg
import geometry_20261114_lifted_modes_banded_full_dn as banded
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA as BOUNDARY_SCHEMA
from geometry_20261114_physical_test_cut_audit import audit_cut
from geometry_20261114_full_prefix_operator import export_scalar_descriptor
from geometry_20261114_same_metric_physical_response import (
    run_response, actions_only, equal, FINITE_SCHEME, SCHEMA as RESPONSE_SCHEMA)


HERE = Path(__file__).resolve().parent
ORIGINAL_SAME_G_SHA = "8aebffdb0047aed04f640d540e1c44255d995307ba7aa9b8ff3c5b5529cf57f6"
ORIGINAL_BAND_WRAPPER_SHA = "390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4"


def maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value), initial=0)) if np.all(np.isfinite(value)) else None


def strip_arguments(arguments, values, flags):
    """Remove only this wrapper's arguments before the original parsers."""
    answer, j = [arguments[0]], 1
    while j < len(arguments):
        token = arguments[j]
        if token in flags:
            j += 1
        elif token in values:
            if j + 1 >= len(arguments):
                raise ValueError("Missing wrapper argument value: " + token)
            j += 2
        elif any(token.startswith(name + "=") for name in values):
            j += 1
        else:
            answer.append(token)
            j += 1
    return answer


def main():
    actions_only()
    original = sameg.original
    sha, read = original.sha, original.read
    if sha(sameg.__file__) != ORIGINAL_SAME_G_SHA or sha(banded.__file__) != ORIGINAL_BAND_WRAPPER_SHA:
        raise ValueError("The unchanged original same-g or complete-band driver bytes differ")
    parser = argparse.ArgumentParser(add_help=False)
    for name in ("accepted", "parent-field", "parent-tail-response", "parent-tail-config",
                 "port", "warm", "tail-client", "tail-config", "tail-source-root", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--with-response", action="store_true", required=True)
    parser.add_argument("--response-out", type=Path)
    parser.add_argument("--parent-scalar-descriptor", type=Path)
    parser.add_argument("--linear-backend", choices=("qr", "banded"), default="qr")
    parser.add_argument("--material-angles", type=int, default=4096)
    parser.add_argument("--physical-angles", type=int, default=4096)
    parser.add_argument("--node-heap", type=int, default=6144)
    parser.add_argument("--peak-curvature", type=float, default=2.5)
    args, _ = parser.parse_known_args()
    if "--response-check" in sys.argv or "--prepare-only" in sys.argv:
        raise ValueError("This live entry produces its own FD report; use the original separate preparation entry")
    output = args.out.resolve()
    output.mkdir(parents=True, exist_ok=True)
    response_output = args.response_out or output / "response"
    response_args = SimpleNamespace(**vars(args))
    response_args.prepared, response_args.out = args.warm, response_output
    session = run_response(response_args, retain_live=True)
    try:
        if not session.report["implementation_check_passed"]:
            return 2
        return solve_session(args, session)
    finally:
        # Covers identity/output failures before the narrower solver-hook
        # finally, as well as every actual solver return or exception.
        session.close()


def solve_session(args, session):
    original = sameg.original
    sha = original.sha
    output = args.out.resolve()
    client, context = session.client, session.context
    report, profile = session.report, context["profile"]
    M, N, scalar = context["M"], context["N"], context["scalar"]
    if report.get("schema") != RESPONSE_SCHEMA or session.closed:
        session.close()
        raise RuntimeError("Only this successfully checked live response can enter the full solve")
    for name, expected in report["consumed_source_sha256"].items():
        if sha(HERE / name) != expected:
            session.close()
            raise ValueError("A numerical source changed after the actual response check: " + name)

    sources = [Path(__file__).name, "geometry_20261114_same_metric_physical_response.py",
        "geometry_20261114_same_metric_full_dn.py", "geometry_20261114_same_metric_profile.py",
        "geometry_20261114_same_metric_prepare.py", "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_physical_test_cut_audit.py", "geometry_20261114_full_dn_solve.py",
        "geometry_20261114_full_dn_augmented.py", "geometry_20261114_full_dn_boundary.py",
        "geometry_20261114_full_prefix_operator.py", "geometry_20261114_separated_qr_bvp.py"]
    if args.linear_backend == "banded":
        sources += ["geometry_20261114_lifted_modes_banded_full_dn.py",
                    "geometry_20261114_banded_collocation.py"]
    identity = dict(schema="same-metric-physical-test-live-full-DN-v1", scope=__doc__,
        finite_boundary_scheme=FINITE_SCHEME, physical_test_schema=BOUNDARY_SCHEMA,
        source_sha256={name: sha(HERE / name) for name in sources},
        parent_binding=context["parent_binding"],
        prepared_sha256=sha(args.warm), response_check_sha256=sha(session.report_path),
        tail_config_sha256=sha(args.tail_config), actual_anchor_sha256=report["tail_anchor_sha256"],
        canonical_scalar_identity_sha256=scalar["canonical_scalar_identity_sha256"],
        complete_scalar_binding=context["scalar_binding"],
        frozen_design_parameters=scalar["frozen_design_parameters"],
        scalar_end=float(profile.end), field_modes=M, tail_modes=M,
        field_angles=N, material_angles=args.material_angles, physical_angles=args.physical_angles,
        state_dimension=4*M+2, fixed_core_modes=0, active_scalar_parameters=0,
        left_rows=3*M+2, right_rows=M, linear_backend=args.linear_backend,
        boundary_residual_definition="All unchanged inlet/constant rows and R_phi=v_nonmean-cut_scale*S*D(epsilon_h*P*z_nonmean)",
        original_material_boundary_residual_definition="R_theta=P*v_nonmean-cut_scale*D(epsilon_h*P*z_nonmean), measured separately",
        old_material_test_equivalent=False, original_Newton_and_17_trials_retained=True,
        unchanged_numeric_tolerances=dict(collocation_and_frozen_physical_RMS=1e-6, boundary=1e-11),
        true_final_native_full_audit_required=True,
        same_live_client_and_worker_predictor_retained=True,
        same_live_frozen_scalar_object_retained=True,
        nonzero_cross_process_cache_created=False,
        scalar_descriptor_file="frozen-scalar-descriptor.json",
        full_angle_cut_audit_is_a_measurement_not_an_extra_Newton_gate=True)
    plain_write = original.write
    plain_write(output / "same-metric-physical-intent.json", identity)
    live = dict(boundary=None, final_cut=None, load_count=0, first_request_done=False,
        worker_calls_at_handoff=client.calls,
        actual_native_record_prefix=str(client.record_prefix),
        original_input_config_sha256=client.sources["input_config"],
        original_runtime_config_sha256=client.sources["runtime_config"],
        process_id=client.proc.pid, same_live_worker=True)
    handoff_path = output / "live-tail-handoff.json"

    def write_handoff():
        plain_write(handoff_path, {key: value for key, value in live.items()
            if key not in ("boundary", "final_cut")})

    def make_boundary(*positional, **keywords):
        value = PhysicalTestBoundary(*positional, physical_angles=args.physical_angles, **keywords)
        if value.K != 0 or value.k != 0 or value.profile is not profile:
            raise ValueError("The full same-g boundary must use this exact K=k=0 scalar object")
        live["boundary"] = value
        return value

    previous_seam = original.final_height_seam
    def final_height_seam(boundary, flow, q, endpoint, native_response):
        legacy = previous_seam(boundary, flow, q, endpoint, native_response)
        legacy.update(old_material_test_not_the_acceptance_gate=True,
                      finite_boundary_scheme=FINITE_SCHEME)
        cut = audit_cut(boundary, flow, endpoint, native_response,
            angular_levels=(args.material_angles, 2*args.material_angles))
        live["final_cut"] = cut
        path = output / "physical-test-final-cut-audit.json"
        plain_write(path, cut)
        legacy.update(physical_test_final_cut_audit_file=path.name,
                      physical_test_final_cut_audit_sha256=sha(path))
        return legacy

    def pending_material_report(data):
        boundary = live["boundary"]
        if boundary is None or "states" not in data:
            return None
        values = np.asarray(data["states"])
        if values.ndim != 2 or values.shape[1] != 4*M+2:
            return None
        endpoint = values[-1]
        proxy = np.zeros(boundary.n)
        proxy[1:M+1] = endpoint[boundary.n:boundary.n+M]
        try:
            _, _, _, trace, tail, slope, _ = boundary.data(proxy, endpoint[:boundary.n], np.empty(0))
            return dict(original_material_Rtheta_nonmean_max=maximum(trace.derivative_s-boundary.cut_scale*slope),
                tail_map_actual_nonlinear_solve=tail["actual_nonlinear_solve"],
                scope="Current explicitly affine inner map; not a fresh native audit",
                original_material_acceptance_claim=False)
        except (ValueError, FloatingPointError, RuntimeError) as error:
            return dict(available=False, diagnostic_error=repr(error), original_material_acceptance_claim=False)

    def physical_write(path, data):
        name = Path(path).name
        if isinstance(data, dict):
            if (name in ("driver-status.json", "prepared.json.gz", "actual.json.gz", "same-metric-intent.json")
                    or name.endswith("-pending.json.gz")):
                data.update(finite_boundary_scheme=FINITE_SCHEME,
                    boundary_residual_definition=identity["boundary_residual_definition"],
                    same_metric_physical_implementation=identity,
                    old_material_boundary_success_inherited=False,
                    live_tail_handoff_file=handoff_path.name)
            if name in ("driver-status.json", "same-metric-intent.json"):
                data["scope"] = __doc__
            if name.endswith("-pending.json.gz"):
                data["independent_original_material_test"] = pending_material_report(data)
            if name == "actual.json.gz":
                if live["final_cut"] is None:
                    raise RuntimeError("The original accepted path did not produce its actual complete-cut report")
                data.update(scope=__doc__,
                    message="Complete fixed-g physical-phi finite DN accepted with a fresh actual tail audit; closed geometry and continuous estimates remain separate.",
                    physical_test_final_cut_audit=live["final_cut"],
                    boundary_residual_max_refers_to="complete physical-phi system and unchanged left boundary",
                    scalar_descriptor_file=identity["scalar_descriptor_file"])
            if name == "driver-status.json" and data.get("new_coupled_finite_acceptance"):
                data.update(phase="same-metric-finite-physical-phi-DN-accepted-assembly-open",
                    new_coupled_finite_acceptance_refers_to=FINITE_SCHEME)
        result = plain_write(path, data)
        if name == "actual.json.gz" and isinstance(data, dict):
            descriptor = export_scalar_descriptor(profile, scalar,
                producer_checkpoint_sha256=sha(path), origin="actual-live-profile")
            equal(descriptor["mathematical_expression"], context["scalar_descriptor"]["mathematical_expression"],
                "unchanged actual live scalar through final acceptance")
            plain_write(output / identity["scalar_descriptor_file"], descriptor)
        return result

    actual_solve = client.solve
    def traced_solve(height, jacobian=True, audit=False):
        before = client.calls
        first = not live["first_request_done"]
        same_anchor = bool(np.array_equal(np.asarray(height), context["height"]))
        response = actual_solve(height, jacobian=jacobian, audit=audit)
        if first:
            live.update(first_request_done=True,
                first_full_request_exactly_completed_H=same_anchor,
                first_full_request_jacobian=bool(jacobian), first_full_request_audit=bool(audit),
                actual_worker_calls_in_first_full_request=client.calls-before,
                initial_actual_response_reused_in_same_live_client=bool(
                    same_anchor and not audit and client.calls == before and response is session.response),
                no_height_threshold_or_quantization=True)
        if audit:
            live.update(final_audited_request_sent_to_actual_worker=client.calls > before,
                actual_audited_response_completed=True)
        live["native_worker_calls_observed"] = client.calls
        write_handoff()
        return response

    def existing_client(module_path, config, sources_root, requested_prefix, heap):
        if live["load_count"] or session.closed or client.proc.poll() is not None:
            raise RuntimeError("The unique actual native client cannot be replaced or reused after close")
        if (sha(module_path) != sha(args.tail_client) or sha(config) != sha(args.tail_config)
                or Path(sources_root).resolve() != args.tail_source_root.resolve()
                or int(heap) != args.node_heap):
            raise ValueError("The full solve requested another actual client configuration or source tree")
        equal(client.sources["input_config"], sha(config), "live client input configuration")
        if (not np.array_equal(client.cache_key, context["height"])
                or client.cache_value is not session.response):
            raise RuntimeError("The actual checked anchor was changed before handoff")
        live.update(load_count=1, requested_original_record_prefix=str(Path(requested_prefix).resolve()),
            original_record_prefix_relocated=False,
            native_predictor_initialized_by_actual_anchor=True)
        write_handoff()
        return client

    def same_profile(geometry):
        equal(geometry, scalar, "the full original v4 scalar specification")
        return profile

    # Preserve the mutable entry hooks, including the original solver's
    # own changes, so importing this module does not leave a new backend.
    snapshots = []
    def keep(obj, *names):
        snapshots.extend((obj, name, getattr(obj, name)) for name in names)
    keep(original, "FullDNBoundary", "final_height_seam", "load_client", "write", "__file__", "__doc__",
         "CompleteProfile", "scalar_spec", "prepared_guess", "preflight")
    keep(sameg, "reconstruct_profile", "install_diagnostics")
    keep(original.original_solver.native.outward, "FullCoreProbe")
    keep(original.original_solver, "released_newton", "original_splu")
    keep(original.original_qr, "DiskQRFactor", "enable")
    keep(original.backend, "prepare_sys", "solve_newton")
    keep(banded, "continuation", "BASE_DRIVER_SHA", "write")
    saved_argv = sys.argv[:]
    try:
        original.FullDNBoundary, original.final_height_seam = make_boundary, final_height_seam
        original.load_client, original.write = existing_client, physical_write
        sameg.reconstruct_profile = same_profile
        client.solve = traced_solve
        sys.argv = strip_arguments(saved_argv,
            {"--response-out", "--parent-scalar-descriptor", "--linear-backend", "--physical-angles"},
            {"--with-response"})
        sys.argv += ["--response-check", str(session.report_path)]
        if "--node-heap" not in sys.argv and not any(v.startswith("--node-heap=") for v in sys.argv):
            sys.argv += ["--node-heap", str(args.node_heap)]
        write_handoff()
        if args.linear_backend == "qr":
            return sameg.main()
        bridge = SimpleNamespace(original=original, __file__=sameg.__file__)
        def bridge_main():
            sameg.install_diagnostics = lambda out, write: bridge.install_qr_diagnostics(out, M, write)
            return sameg.main()
        bridge.main = bridge_main
        banded.continuation, banded.BASE_DRIVER_SHA = bridge, ORIGINAL_SAME_G_SHA
        previous_band_write = banded.write
        def band_write(path, data, *positional, **keywords):
            if isinstance(data, dict) and Path(path).name == "complete-banded-intent.json":
                data.update(scope=__doc__, mathematical_BC_changed=True,
                    equation_row_permutation_only=False,
                    linear_backend_is_only_row_permutation_of_current_physical_test=True,
                    finite_boundary_scheme=FINITE_SCHEME,
                    same_metric_physical_implementation=identity,
                    fixed_core_modes=0, active_scalar_parameters=0,
                    same_live_actual_native_client_retained=True)
            return previous_band_write(path, data, *positional, **keywords)
        banded.write = band_write
        return banded.main()
    finally:
        try:
            client.solve = actual_solve
            session.close()
            live.update(live_client_closed=True, native_worker_calls_observed=client.calls,
                native_worker_exit_code=client.proc.poll())
            write_handoff()
        finally:
            sys.argv = saved_argv
            for obj, name, value in reversed(snapshots):
                setattr(obj, name, value)


if __name__ == "__main__":
    raise SystemExit(main())
