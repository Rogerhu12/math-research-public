#!/usr/bin/env python3
"""Actual new-M/new-H tail and R252 response check on a frozen v4 metric.

Only an actually accepted complete parent can supply the v4 preparation.
The original three design controls and the entire scalar interval remain
frozen.  This module evaluates the complete new native H/J once, then uses
that explicitly affine map for the existing directional FD checks.  A
successful caller may retain the identical live TailClient, including its
real worker predictor.  No nonzero response is imported into another
worker, and no finite field or whole-surface acceptance is created here.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import time
import traceback

import numpy as np

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
from geometry_20261114_full_dn_response import refined_directional_check
from geometry_20261114_lifted_modes_prepare import validate_source
from geometry_20261114_lifted_modes_profile import field_spec
from geometry_20261114_same_metric_prepare import validate_parent
from geometry_20261114_same_metric_profile import freeze_spec, reconstruct_profile, SCHEMA as SCALAR_SCHEMA
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA as BOUNDARY_SCHEMA
from geometry_20261114_physical_test_response import make_directions
from geometry_20261114_full_prefix_operator import export_scalar_descriptor
from exact_20261114_seeded_zero_tail_client import (
    IO_KEYS, same, numerical_configuration, ready_semantics, command_semantics)


HERE = Path(__file__).resolve().parent
SCHEMA = "same-metric-physical-test-actual-live-response-v1"
FINITE_SCHEME = "physical-phi-complete-DN-v1"
TRUE_CLIENT_SHA = "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09"
GRID_KEYS = frozenset(("modes", "quadrature", "steps", "auditSteps"))
INPUT_KEYS = IO_KEYS | frozenset(("initialCheckpoint",))
SOURCE_NAMES = (
    Path(__file__).name, "geometry_20261114_same_metric_profile.py",
    "geometry_20261114_same_metric_prepare.py", "geometry_20261114_lifted_modes_profile.py",
    "geometry_20261114_full_dn_solve.py", "geometry_20261114_full_dn_augmented.py",
    "geometry_20261114_full_dn_boundary.py", "geometry_20261114_full_dn_response.py",
    "geometry_20261114_physical_test_boundary.py", "geometry_20261114_physical_test_response.py",
    "geometry_20261114_material_quintic_readout.py", "geometry_20261114_full_prefix_operator.py",
    "exact_20261114_true_tail_client.py", "exact_20261114_seeded_zero_tail_client.py")


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run this actual numerical response only in the public repository's Actions")


def equal(left, right, label):
    if not same(left, right):
        raise ValueError("The complete live response identity differs: " + label)


def vector(value, shape, label):
    result = np.asarray(value, dtype=float)
    if result.shape != shape or not np.all(np.isfinite(result)):
        raise ValueError("A complete finite vector is required: " + label)
    return result


def validate_configuration(config, parent_config, port, M):
    """Keep all original physical/solver settings; allow declared refinements."""
    for key, expected in port["parameters"].items():
        equal(config.get(key), expected, "original physical port parameter " + key)
    if (type(config.get("modes")) is not int or config["modes"] != M
            or config.get("spacing") != 2
            or type(config.get("quadrature")) is not int
            or config["quadrature"] <= 4 * M * config["spacing"]):
        raise ValueError("Use all new even tail modes and the original strict angular guard")
    for key in ("quadrature", "steps", "auditSteps"):
        if (type(config.get(key)) is not int or config[key] < parent_config[key]):
            raise ValueError("Do not coarsen a parent native resolution: " + key)
    frozen = lambda value: {key: item for key, item in value.items()
        if key not in GRID_KEYS and key not in INPUT_KEYS}
    equal(frozen(config), frozen(parent_config), "all unchanged native physical/solver settings")
    return dict(parent={key: parent_config[key] for key in GRID_KEYS},
        current={key: config[key] for key in GRID_KEYS},
        original_solve_tolerance_unchanged=True,
        original_physical_depth_partition_Newton_and_line_search_unchanged=True,
        initialization_is_not_a_response_cache=True,
        explicit_initial_checkpoint_sha256=(original.sha(config["initialCheckpoint"])
            if config.get("initialCheckpoint") else None))


def build_context(args):
    """Read genuine identities and construct one fixed scalar object."""
    actions_only()
    design, parent, warm, port, config, parent_config = [original.read(path) for path in
        (args.accepted, args.parent_field, args.prepared, args.port,
         args.tail_config, args.parent_tail_config)]
    validate_source(design)
    parent_binding = validate_parent(parent, args.parent_field,
        args.parent_tail_response, args.parent_tail_config)
    if parent.get("finite_boundary_scheme") != FINITE_SCHEME:
        raise ValueError("This R252 refinement entry requires an actual R252 complete parent")
    M, N = int(warm["M"]), int(warm["N"])
    scalar = freeze_spec(parent, M, original.sha(args.parent_field))
    specification = scalar["frozen_design_scalar_profile"]
    if (warm.get("complete_scalar_profile") != scalar
            or warm.get("parent_binding") != parent_binding
            or warm.get("field_representation") != field_spec(M, N)
            or warm.get("fixed_core_modes") != 0 or warm.get("active_scalar_parameters") != 0
            or N < parent["N"] or N < 4 * M + 4 or N % 2
            or scalar["accepted_source_prefix_sha256"] != original.sha(args.accepted)
            or specification["base_prefix_geometry"] != design["fixed_scalar_profile"]["geometry"]
            or scalar["complete_original_port"] != port
            or float(args.peak_curvature) != specification["peak_curvature"]):
        raise ValueError("Use the same complete prepared v4 field, original design and frozen scalar")
    for count in (args.material_angles, args.physical_angles):
        if type(count) is not int or count <= 4 * M or count % 2:
            raise ValueError("Resolve every field/tail mode on both fixed boundary quadratures")
    if original.sha(args.tail_client) != TRUE_CLIENT_SHA:
        raise ValueError("Use the unchanged original persistent true TailClient, without an imported cache")
    configuration = validate_configuration(config, parent_config, port, M)
    profile = reconstruct_profile(scalar)
    mesh = np.asarray(warm["mesh"], dtype=float)
    states = vector(warm.get("augmented_states", warm["states"]),
        (len(mesh), 4 * M + 2), "all physical/core rows; no active scalar rows")
    vector(warm.get("augmented_rhs", warm["rhs"]), states.shape, "complete saved RHS")
    if (mesh.ndim != 1 or len(mesh) < 2 or not np.all(np.isfinite(mesh))
            or np.any(np.diff(mesh) <= 0) or mesh[0] != 0
            or abs(mesh[-1] - profile.end) > 1e-12
            or profile.M != M or profile.tail_modes != M or profile.parameter_count != 0):
        raise ValueError("Keep the complete original scalar interval and all K=k=0 rows")
    law = design["original_metric_identity"]["law"]
    q = original.original_solver.native.outward.FullCoreProbe(states[0, 3*M+2:], M, N,
        law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile)
    affine = original.AffineTail(M)
    boundary = PhysicalTestBoundary(profile, np.empty(0), flow.point_rhs,
        flow.point_jacobian, affine, angular=args.material_angles,
        physical_angles=args.physical_angles)
    height = vector(original.true_height(boundary, states[-1]), (M,), "new actual native height")
    descriptor = export_scalar_descriptor(profile, scalar, origin="unspecified-runtime-object")
    scalar_binding = dict(canonical_scalar_identity_sha256=scalar["canonical_scalar_identity_sha256"],
        current_mathematical_identity_sha256=descriptor["mathematical_identity_sha256"],
        parent_live_descriptor_provided=False, parent_live_mathematical_identity_verified=False,
        unchanged_complete_v3_formula_and_original_three_p_star=True,
        literal_floating_evaluator_error_verified=False)
    parent_descriptor_path = getattr(args, "parent_scalar_descriptor", None)
    if parent_descriptor_path:
        parent_descriptor = original.read(parent_descriptor_path)
        producer = parent_descriptor["producer"]
        if (producer.get("origin") != "actual-live-profile"
                or producer.get("checkpoint_sha256") != original.sha(args.parent_field)):
            raise ValueError("The supplied parent descriptor must bind its actual accepted live producer")
        equal(parent_descriptor["mathematical_expression"], descriptor["mathematical_expression"],
              "actual parent/current complete finite-Gauss expression")
        equal(parent_descriptor["mathematical_identity_sha256"], descriptor["mathematical_identity_sha256"],
              "actual parent/current complete finite-Gauss identity")
        scalar_binding.update(parent_live_descriptor_provided=True,
            parent_descriptor_sha256=original.sha(parent_descriptor_path),
            parent_live_mathematical_identity_verified=True)
    return dict(design=design, parent=parent, warm=warm, port=port, config=config,
        scalar=scalar, parent_binding=parent_binding, profile=profile, flow=flow,
        boundary=boundary, affine=affine, states=states, mesh=mesh, M=M, N=N,
        height=height, configuration=configuration, scalar_descriptor=descriptor,
        scalar_binding=scalar_binding)


def validate_live_response(client, response, context):
    """Full H/J/state/config/source checks on this actual, still-live worker."""
    M, config, height = context["M"], context["config"], context["height"]
    if (client.M != M or client.N != config["quadrature"]
            or response.get("converged") is not True or response.get("failed")
            or response.get("actual_nonlinear_solve") is not True
            or response.get("finite_tail_only") is not True
            or not isinstance(response.get("residual"), (int, float))
            or not np.isfinite(response["residual"])
            or not 0 <= response["residual"] < config["solveTolerance"]):
        raise ValueError("The full current native solve did not satisfy its original gate")
    equal(numerical_configuration(config), numerical_configuration(client._configuration),
        "input/current runtime numerical configuration")
    if client.sources["input_config"] != original.sha(client.input_config):
        raise ValueError("The actual client input configuration SHA changed")
    parent_sources = context["parent"]["actual_tail"]["sources"]
    for name, value in client.sources.items():
        if name not in ("input_config", "runtime_config"):
            equal(parent_sources.get(name), value, "unchanged native numerical source " + name)
    intent_path = client.record_prefix.with_name(client.record_prefix.name + "_intent.json")
    intent = original.read(intent_path)
    equal(intent["source_sha256"], client.sources, "actual intent/source inventory")
    equal(intent["config_sha256"], original.sha(client.config), "actual runtime configuration bytes")
    command_semantics(intent["command"])
    ready_semantics(client.ready)
    if client.calls != 1:
        raise ValueError("This fresh true client must have exactly one actual anchor request")
    request_path = client.record_prefix.with_name(client.record_prefix.name + "_0001.json.gz")
    request_record = original.read(request_path)
    equal(request_record["request"], dict(height=height.tolist(), jacobian=True, audit=False),
        "complete actual first request")
    equal(request_record["response"], response, "recorded and live actual response")
    equal(request_record["source_sha256"], client.sources, "recorded actual numerical sources")
    equal(request_record["config"], client._configuration, "recorded actual runtime settings")
    checkpoint = response["checkpoint"]
    equal(checkpoint["parameters"], client.ready["parameters"], "actual ready/checkpoint parameters")
    equal(checkpoint["cutHeight"], height.tolist(), "complete actual native request H")
    depth = checkpoint["parameters"]["depth"]
    if type(depth) is not int or depth < 1:
        raise ValueError("The actual shooting partition is absent")
    vector(checkpoint["states"], (depth+1, 2*M), "all shooting states")
    nodes = checkpoint["rawNode"]
    if (not isinstance(nodes, list) or not nodes or nodes[0] != 0 or nodes[-1] != depth
            or any(type(j) is not int or not 0 <= j <= depth for j in nodes)
            or any(a >= b for a, b in zip(nodes, nodes[1:]))):
        raise ValueError("The complete actual raw-node index is invalid")
    equal(checkpoint["rawStates"], [checkpoint["states"][j] for j in nodes],
        "all raw shooting state copies")
    vector(response["heightJetJacobian"], ((3*M+2)*M,), "all actual 3T+2 Jacobian rows")
    equal(response["heightJetJacobianMethod"], dict(
        slope="analytic actual shooting tangent plus exact cut chain rule",
        meanSlopeCorrection="analytic actual shooting tangent plus exact cut chain rule",
        second="source symmetric difference on actual tangent graph",
        meanSecondCorrection="source symmetric difference on actual tangent graph",
        height="source symmetric difference; mathematically identity", sourceSecondDifferenceStep=1e-4),
        "unchanged complete native Jacobian methods")
    for key in ("height", "slope", "second"):
        vector(response["jets"][key], (M,), "complete native " + key)
    for key in ("meanSlope", "meanSecond", "meanSlopeCorrection", "meanSecondCorrection"):
        if type(response["jets"].get(key)) not in (int, float) or not np.isfinite(response["jets"][key]):
            raise ValueError("The complete actual mean jet is absent: " + key)
    for key in ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond"):
        equal(response["jets"][key], client.cut[key], "actual response/ready cut " + key)
        if not np.isclose(client.cut[key], context["profile"].cut[key], rtol=2e-11, atol=2e-13):
            raise ValueError("The current tail is not at the original physical cut: " + key)
    if (client.cache_value is not response or
            not np.array_equal(client.cache_key, height)):
        raise ValueError("The live worker/client did not retain its own completed response")
    return dict(complete_H_entries=M, complete_J_entries=(3*M+2)*M,
        complete_shooting_state_shape=[depth+1, 2*M], raw_nodes=len(nodes),
        raw_node_states_equal_saved_full_states=True, actual_ready_checkpoint_parameters_identical=True,
        actual_request_record_file=request_path.name,
        actual_request_record_sha256=original.sha(request_path),
        unchanged_parent_native_mathematical_sources=True,
        actual_native_request_audit=False, final_full_audit_still_required=True,
        actual_J_method=response.get("heightJetJacobianMethod"),
        residual=response["residual"], solve_tolerance=config["solveTolerance"])


@dataclass
class LiveResponse:
    context: dict
    client: object
    response: dict
    report: dict
    report_path: Path
    closed: bool = False

    def close(self):
        if not self.closed:
            self.client.close()
            self.closed = True


def run_response(args, *, retain_live=False):
    """Return one successful live session only when explicitly requested.

    On any exception or a failed FD report the worker is closed here.
    The receiving full driver owns cleanup of a successfully retained one.
    """
    context = build_context(args)
    output = Path(args.out).resolve()
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError("Use a fresh response output directory")
    started = time.monotonic()
    status = dict(schema=SCHEMA, phase="starting-actual-complete-native-anchor", success=False,
        source_sha256=original.sha(__file__), accepted_parent_sha256=original.sha(args.parent_field),
        prepared_sha256=original.sha(args.prepared), full_BVP_accepted=False)
    original.write(output / "response-status.json", status)
    original.write(output / "scalar-runtime-definition.json", context["scalar_descriptor"])
    client = None
    try:
        client = original.load_client(args.tail_client, args.tail_config, args.tail_source_root,
            output / "native-tail", args.node_heap)
        response = client.solve(context["height"], jacobian=True, audit=False)
        anchor_path = output / "actual-anchor-tail.json.gz"
        original.write(anchor_path, response)
        actual = validate_live_response(client, response, context)
        calls_before = client.calls
        context["affine"].set(context["height"], response)
        flow, boundary = context["flow"], context["boundary"]
        separated = SeparatedBoundary(boundary)
        ya, yb = context["states"][0].copy(), context["states"][-1].copy()
        # The same explicit nonzero local FD trial as the original checker.
        # It is not a changed native solve, preparation or acceptance input.
        yb[boundary.iz + 1] += 1e-5
        yb[boundary.iz + 32] += 1e-9
        yb[boundary.iz + flow.M] += 1e-10
        yb[flow.core_slice] = ya[1:flow.M+1]
        pa, pb = ya[:flow.n].copy(), yb[:flow.n].copy()
        controls = yb[flow.parameter_slice].copy()
        directions, augmented = make_directions(flow, boundary)
        A, B, Pp = boundary.jacobian(pa, pb, controls)
        direct = refined_directional_check(
            lambda d, h: boundary(pa+h*d["ya"], pb+h*d["yb"], controls+h*d["p"]),
            lambda d: A@d["ya"]+B@d["yb"]+Pp@d["p"], directions)
        AA, BB = separated.jacobian(ya, yb)
        separate = refined_directional_check(
            lambda d, h: separated(ya+h*d["ya"], yb+h*d["yb"]),
            lambda d: AA@d["ya"]+BB@d["yb"], augmented)
        separate.update(right_rows_depend_only_on_right_endpoint=True,
            left_right_jacobian_offblock_max=float(max(np.max(abs(AA[separated.left_count:])),
                np.max(abs(BB[:separated.left_count])))))
        groups = (direct, separate)
        coarse = max(v["relative_error"] for g in groups for d in g["directions"] for v in d["levels"])
        worst = max(v["relative_error"] for g in groups for d in g["directions"] for v in d["fourth_order_levels"])
        contracts = all(g["second_order_truncation_contracts"] for g in groups)
        if (client.calls != calls_before or client.cache_value is not response or
                not np.array_equal(client.cache_key, context["height"])):
            raise RuntimeError("An affine FD check unexpectedly changed the actual native worker")
        scalar = context["scalar"]
        identity = dict(scalar_schema=SCALAR_SCHEMA,
            canonical_scalar_identity_sha256=scalar["canonical_scalar_identity_sha256"],
            parent_sha256=original.sha(args.parent_field), field_modes=flow.M,
            angular_quadrature=context["N"], tail_modes=flow.M,
            fixed_core_modes=0, active_scalar_parameters=0,
            state_dimension=flow.dimension, left_rows=separated.left_count, right_rows=flow.M,
            frozen_design_parameters=scalar["frozen_design_parameters"],
            complete_scalar_binding=context["scalar_binding"])
        report = dict(schema=SCHEMA, scope=__doc__, physical_test_schema=BOUNDARY_SCHEMA,
            finite_boundary_scheme=FINITE_SCHEME, physical_test=boundary.description(),
            same_metric_implementation=identity, parent_binding=context["parent_binding"],
            direct_boundary=direct, separated_boundary=separate,
            maximum_relative_directional_error=worst,
            maximum_second_order_relative_directional_error=coarse,
            maximum_fourth_order_relative_directional_error=worst,
            verification_threshold=5e-5, verification_estimator="two fourth-order Richardson levels",
            second_order_truncation_contracts=contracts,
            implementation_check_passed=bool(np.isfinite(worst) and worst <= 5e-5 and contracts),
            accepted_sha256=original.sha(args.parent_field),
            original_design_source_sha256=original.sha(args.accepted),
            prepared_sha256=original.sha(args.prepared), tail_config_sha256=original.sha(args.tail_config),
            tail_anchor_file=anchor_path.name, tail_anchor_sha256=original.sha(anchor_path),
            consumed_source_sha256={name: original.sha(HERE/name) for name in SOURCE_NAMES},
            original_native_configuration=context["configuration"], actual_anchor=actual,
            physical_cut=client.cut, native_sources=client.sources,
            native_record_prefix=str(client.record_prefix), native_worker_calls=calls_before,
            native_worker_calls_during_FD=0, ready_linear_graph_used=False,
            actual_completed_nonlinear_J_reused=True,
            new_native_H_solved_without_quantization=context["height"].tolist(),
            same_live_client_available=bool(retain_live and np.isfinite(worst) and worst <= 5e-5 and contracts),
            nonzero_cross_process_cache_created=False,
            full_BVP_solved=False, full_Cartesian_closed_surface=False,
            seconds=time.monotonic()-started)
        report_path = output / "response-check.json"
        original.write(report_path, report)
        status.update(phase="actual-anchor-and-affine-FD-completed",
            success=report["implementation_check_passed"],
            implementation_check_passed=report["implementation_check_passed"],
            response_check_sha256=original.sha(report_path), native_worker_calls=client.calls,
            maximum_relative_directional_error=worst)
        session = LiveResponse(context, client, response, report, report_path)
        if not retain_live or not report["implementation_check_passed"]:
            session.close()
        status["live_client_retained_for_same_process"] = not session.closed
        print(json.dumps(dict(event="same_metric_physical_response",
            field_modes=flow.M, maximum_relative_directional_error=worst,
            implementation_check_passed=report["implementation_check_passed"],
            actual_native_worker_calls=client.calls, live_client_retained=not session.closed)), flush=True)
        return session
    except Exception as error:
        status.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        if client is not None:
            client.close()
        raise
    finally:
        status["seconds"] = time.monotonic()-started
        try:
            original.write(output / "response-status.json", status)
        except Exception:
            if client is not None:
                client.close()
            raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "parent-field", "parent-tail-response", "parent-tail-config",
                 "prepared", "port", "tail-client", "tail-config", "tail-source-root", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--parent-scalar-descriptor", type=Path)
    parser.add_argument("--node-heap", type=int, default=6144)
    parser.add_argument("--material-angles", type=int, default=4096)
    parser.add_argument("--physical-angles", type=int, default=4096)
    parser.add_argument("--peak-curvature", type=float, default=2.5)
    session = run_response(parser.parse_args(), retain_live=False)
    return 0 if session.report["implementation_check_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
