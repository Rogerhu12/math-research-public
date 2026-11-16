#!/usr/bin/env python3
"""R501 actual63 prefix to live128 current-H/J, original affine FD and fullDN.

The original actual63 complete prefix warm remains unaccepted. Actual91's
failed native state is only the independently declared first tail guess.
There is no completed61 bootstrap, no old accepted native cache, and no
continuous-C substitution. Every uncached current H uses new original64
capture/R273 and its complete same-call128 owner/components/explicit RN64.
All original7ba prefix/FD/fullDN mathematical functions and gates remain.
"""
from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import time
import traceback

import numpy as np

import geometry_20261114_full_dn_solve as original
import geometry_20261114_physical_test_full_dn as full_entry
from geometry_20261114_full_dn_augmented import AugmentedFlow, SeparatedBoundary
from geometry_20261114_full_dn_response import refined_directional_check
from geometry_20261114_lifted_modes_profile import LiftedModesPrefixProfile, field_spec
from geometry_20261114_lifted_modes_prepare import validate_source
from geometry_20261114_lifted_modes_response import binding as lifted_binding
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary, SCHEMA as PHYSICAL_SCHEMA
from geometry_20261114_physical_test_response import make_directions
from geometry_20261114_actual_direction_probe import clean


HERE = Path(__file__).resolve().parent
SCHEMA = "R501-live128-actual63-H-original-FD-and-complete-fullDN-v1"
FINITE_SCHEME = "physical-phi-complete-DN-v1"
CLIENT_NAME = "geometry_20261116_live128_tail_client.py"
ACCEPTED_SHA = "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff"
CONFIG_SHA = "01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5"
HISTORICAL_ZERO_SHA = "e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51"
FIXED_BINARY_BYTES_PER_NATIVE_CORRECTION = 704385296
SOURCE_PINS = {
    "geometry_20261114_full_dn_solve.py": "c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162",
    "geometry_20261114_full_dn_augmented.py": "f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e",
    "geometry_20261114_full_dn_boundary.py": "4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2",
    "geometry_20261114_full_dn_response.py": "38d21971b3b0d462f8cf1b8f0a1cd174a28db3dcba450e89d0d0baecc5e26e74",
    "geometry_20261114_lifted_modes_profile.py": "13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5",
    "geometry_20261114_lifted_modes_prepare.py": "9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db",
    "geometry_20261114_lifted_modes_response.py": "c216d2a857670fc859c5edb567d10336482d617c984e2ad00793d271104fd5f7",
    "geometry_20261114_physical_test_boundary.py": "3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681",
    "geometry_20261114_physical_test_response.py": "83ce387778fb90209e841fc841a81ed3d99e15181d6e86210ec1244fde017e79",
    "geometry_20261114_physical_test_cut_audit.py": "7a548961ff0bd3e5171db18f1133d42f606be19e65e5d2e919432514042ba420",
    "geometry_20261114_physical_test_full_dn.py": "abbf1a53cb454effc7e90e97166a469b84eb61cd7d75832dc3c2ab0f81add10b",
    "geometry_20261114_lifted_modes_full_dn.py": "d885ebc8de5ebd02f006c4104d8b67e856047b4e58f0e125651b38187fb251a5",
    "geometry_20261114_lifted_modes_banded_full_dn.py": "390387db4700f64302b76ee684f9a810a611c57c6617eb67d4597a9fa18905c4",
    "geometry_20261114_banded_collocation.py": "0780dcc4e331f6cde64141b0fa9ebdd1325eec2af87d94fc455e72405a0524f1",
    "geometry_20261114_constrained_trust_response.py": "7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78",
    "exact_20261114_true_tail_client.py": "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
    "exact_20261114_seeded_zero_tail_client.py": "a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776",
    "geometry_20261114_current576_live_tail_client.py": "c9f3377748480d4905a32f7f858e2b9a5bcb8a697b7b7806ffc409e635ed1189",
    CLIENT_NAME: "9f32e5ddd376016e51f678d9f0328727e63d8aacb5c4583046dc705949cc1894",
    "geometry_20261114_current576_live_tail_client_hook.mjs": "7e83b398fe0f8a8801700d50c640b1e97bc185ec07627468f94fc54de61a58f5",
    "exact_20261114_live_current576_damped_system.py": "9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a",
    "exact_20261114_live_current576_damped_chain_qr.py": "ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f",
    "geometry_20261116_live128_current_call.mjs": "c20af799243d35a045c9c5be7900fbd19bb8b391acb9efb26fe9c5265566cd21",
    "geometry_20261116_live128_worker.mjs": "8cc51b3e1a1c232c8b5769ef1cfc39261deb7aba84d0b8365b62cbf88c270b72",
    "geometry_20261116_live128_call_pipeline.py": "137cc95996dca1d876640fb81e4fd3290d41e32e9b23027cb29d103b5cb0eda8",
    "geometry_20261116_live128_same_call_owner.py": "5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5",
    "geometry_20261116_live128_response_assembly.py": "08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb",
    "geometry_20261116_live128_final_components.py": "2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866",
    "geometry_20261116_native128_live_scalar_source.py": "06a257765276863a487c1b2db6a13990c0dd6ec7dca4bc5422eda4af63d3bb2b",
    "exact_20261116_binary128_live_response_projection.py": "b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e",
    "exact_20261116_live128_current576_system.py": "e37b13457b9dd9cbd0e918a2bf98988b5027b49fad5c54ffd824016dd2efa7c2",
    "exact_20261116_live128_current576_chain_qr.py": "faac8b013b9151ba92760962d4303c847301a9057834e7230ab37ea6d0c04b49",
    "geometry_20261116_live128_actual91_seed.py": "219f5f8b26af05c17e596a1534e1fe5390c72ecb895de3b5606505525b8e429a",
    "geometry_20261116_live128_owned_process.py": "1516306f3ead5a5e8b54f389da172ef9544298b13ccf659c390cb874d26ed6a7",
    "geometry_20261115_native_trace_variation128_bridge.mjs": "61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7",
    "geometry_20261115_native_final128_packet.mjs": "824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2",
    "geometry_20261115_native_primal128_bridge.mjs": "3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8",
    "geometry_20261115_native_primal128.cpp": "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d",
    "exact_20261114_native_damped_chain_qr.py": "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    "exact_20261114_native_allrows_dyadic_residual.py": "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def receipt(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size, sha256=sha(path))


def array_identity(value):
    value = np.asarray(value, dtype="<f8", order="C")
    return dict(shape=list(value.shape), dtype="<f8", order="C",
        raw_sha256=hashlib.sha256(value.tobytes(order="C")).hexdigest(),
        negative_zero_columns=np.flatnonzero((value.reshape(-1) == 0)
            & np.signbit(value.reshape(-1))).tolist())


def same(left, right, label):
    if left != right:
        raise ValueError("Actual input identity differs: " + label)


def require_sha(path, expected, label):
    if not re.fullmatch(r"[0-9a-f]{64}", str(expected)):
        raise ValueError("Supply an actual full SHA256, not a future placeholder: " + label)
    same(sha(path), expected, label)


def vector(value, shape, label):
    result = np.asarray(value, dtype=float)
    if result.shape != shape or not np.all(np.isfinite(result)):
        raise ValueError("A complete finite saved field is required: " + label)
    return result


def source_inventory():
    for name, expected in SOURCE_PINS.items():
        require_sha(HERE / name, expected, name)
    return {Path(__file__).name: sha(__file__), **SOURCE_PINS,
        "geometry_20261114_actual_direction_probe.py": sha(HERE / "geometry_20261114_actual_direction_probe.py")}


def build_context(args):
    """Use the unchanged v3 scalar and all 453 saved endpoint coordinates."""
    require_sha(args.accepted, ACCEPTED_SHA, "actual accepted96 source")
    require_sha(args.tail_config, CONFIG_SHA, "unchanged complete native configuration")
    require_sha(args.warm, args.warm_sha256, "actual warm")
    require_sha(args.warm_status, args.warm_status_sha256, "actual warm status")
    require_sha(args.live128_policy, args.live128_policy_sha256, "actual one-job live128 policy")
    policy = original.read(args.live128_policy)
    if policy["schema"] != "R493-current-H-live128-client-policy-v1":
        raise ValueError("Explicit actual live128 policy, not an old completed61 response")
    accepted, warm, status, port, config = [original.read(path) for path in
        (args.accepted, args.warm, args.warm_status, args.port, args.tail_config)]
    validate_source(accepted)
    optimization = warm.get("optimization_warm", {})
    history = status.get("identity")
    if (not isinstance(history, dict) or not isinstance(optimization, dict)
            or not isinstance(optimization.get("source_sha256"), dict)
            or not optimization.get("schema")
            or warm.get("success") is not False
            or warm.get("new_coupled_finite_acceptance") is not False
            or status.get("success") is not False
            or status.get("new_coupled_finite_acceptance") is not False):
        raise ValueError("Supply the actual explicitly unaccepted complete optimization warm/status")
    same(status.get("schema"), optimization["schema"], "warm/status schema")
    same(status.get("latest_warm_sha256"), args.warm_sha256, "status latest warm")
    for key, value in history.items():
        same(optimization.get(key), value, "warm/status common provenance " + key)
    same(optimization.get("source_accepted_sha256"), ACCEPTED_SHA, "historical accepted prefix")
    same(optimization.get("actual_tail_config_sha256"), CONFIG_SHA, "historical native configuration")
    same(optimization.get("actual_zero_anchor_sha256"), HISTORICAL_ZERO_SHA, "historical zero-H anchor")
    same(warm.get("finite_boundary_scheme"), FINITE_SCHEME, "current finite boundary scheme")
    for name, expected in optimization["source_sha256"].items():
        if Path(name).name != name:
            raise ValueError("The recorded producer sources must be local computation basenames")
        require_sha(HERE / name, expected, "actual warm producer " + name)
    for key in ("execution_wrapper_source_sha256", "mathematical_producer_source_sha256"):
        if key in status:
            same(warm.get(key), status[key], "warm/status " + key)
    M, N = int(warm["M"]), int(warm["N"])
    specification = warm["complete_scalar_profile"]
    if ((M, N) != (112, 2048)
            or warm.get("field_representation") != field_spec(M, N)
            or specification.get("accepted_prefix_sha256") != ACCEPTED_SHA
            or specification.get("base_prefix_geometry") != accepted["fixed_scalar_profile"]["geometry"]
            or specification.get("complete_original_port") != port
            or specification.get("field_modes") != M
            or specification.get("tail_modes") != M):
        raise ValueError("Retain the full actual field, scalar formula and original port")
    for key, expected in port["parameters"].items():
        same(config.get(key), expected, "unchanged physical port " + key)
    if config.get("modes") != M or config.get("spacing") != 2:
        raise ValueError("The current complete prefix and tail must use all 112 even modes")
    profile = LiftedModesPrefixProfile(accepted, port, specification["peak_curvature"],
        M, supports=specification["control_supports_binary64"])
    mesh = np.asarray(warm["mesh"], dtype=float)
    states = vector(warm.get("augmented_states", warm["states"]),
        (len(mesh), 4*M+5), "all physical/core/three-control states")
    vector(warm.get("augmented_rhs", warm["rhs"]), states.shape, "all saved derivatives")
    if (mesh.ndim != 1 or len(mesh) < 2 or not np.all(np.isfinite(mesh))
            or np.any(np.diff(mesh) <= 0) or mesh[0] != 0
            or abs(mesh[-1] - profile.end) > 1e-12):
        raise ValueError("The saved warm must cover the same full original scalar interval")
    law = accepted["original_metric_identity"]["law"]
    q = original.original_solver.native.outward.FullCoreProbe(states[0, 3*M+2:4*M+2],
        M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile, args.jac_workers)
    affine = original.AffineTail(M)
    boundary = PhysicalTestBoundary(profile, np.asarray(accepted["core"]["coefficients"])[:3],
        flow.point_rhs, flow.point_jacobian, affine, angular=args.material_angles,
        physical_angles=args.physical_angles)
    height = vector(original.true_height(boundary, states[-1]), (M,), "actual unquantized current native H")
    provenance = dict(schema=optimization["schema"], source_sha256=optimization["source_sha256"],
        historical_zero_anchor_sha256=optimization["actual_zero_anchor_sha256"],
        historical_zero_anchor_used_for_this_FD=False,
        historical_warm_producer_dictionary_rewritten=False,
        original_warm_bytes_rewritten=False,
        original_prepared_sha256=optimization.get("source_prepared_sha256"),
        resume_sha256=optimization.get("resume_sha256"),
        accepted_warm_steps=status.get("accepted_warm_steps"),
        optimization_progress=status.get("optimization_progress"))
    return dict(accepted=accepted, warm=warm, status=status, port=port, config=config,
        profile=profile, flow=flow, affine=affine, boundary=boundary, mesh=mesh,
        states=states, height=height, M=M, N=N, specification=specification,
        warm_provenance=provenance)


def actual_response_binding(client, response, context, anchor_path):
    """Bind an actual return of this same worker; retain original cache semantics."""
    M, H, config = context["M"], context["height"], context["config"]
    if (client.M != M or client.N != config["quadrature"]
            or response.get("converged") is not True or response.get("failed")
            or response.get("actual_nonlinear_solve") is not True
            or not np.isfinite(response["residual"])
            or not 0 <= response["residual"] < config["solveTolerance"]):
        raise ValueError("The actual current H/J must satisfy the unchanged original native gate")
    full_J = vector(response["heightJetJacobian"], ((3*M+2)*M,), "complete native height Jacobian")
    checkpoint_H = vector(response["checkpoint"]["cutHeight"], (M,), "actual response request H")
    if (not np.array_equal(checkpoint_H, H) or client.cache_value is not response
            or not np.array_equal(client.cache_key, H)):
        raise ValueError("The live worker response and its original same-H cache do not bind current H")
    record = client.record_prefix.with_name(client.record_prefix.name + ("_%04d.json.gz" % client.calls))
    stored = original.read(record)
    same(stored["response"], response, "live and actually saved native response")
    return dict(actual_anchor_file=receipt(anchor_path), native_request_record=receipt(record),
        actual_protocol_call=client.calls, complete_H_entries=M, complete_J_entries=full_J.size,
        complete_H_identity=array_identity(H), complete_J_identity=array_identity(full_J),
        literal_response_H_identity=array_identity(checkpoint_H),
        original_same_H_cache_numeric_equality=True,
        response_H_and_current_H_same_binary64_bits=bool(checkpoint_H.tobytes() == H.tobytes()),
        unexported_original_response_negative_zeros_not_invented=True,
        residual=response["residual"], solve_tolerance=config["solveTolerance"],
        current_worker_actual_response=True, old_process_response_cache_imported=False,
        full_J_method=response.get("heightJetJacobianMethod"),
        requested_audit=False, original_final_fresh_audit_still_required=True)


def response_check(context, client, response, args, output, sources, write):
    """The frozen original directions, perturbations and Richardson checker."""
    before = client.calls
    context["affine"].set(context["height"], response)
    flow, boundary = context["flow"], context["boundary"]
    separated = SeparatedBoundary(boundary)
    ya, yb = context["states"][0].copy(), context["states"][-1].copy()
    # These are the literal original constrained_trust_response trial
    # perturbations. They are not a native request or a changed warm.
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
    if (client.calls != before or client.cache_value is not response
            or not np.array_equal(client.cache_key, context["height"])):
        raise RuntimeError("An explicitly affine FD unexpectedly changed the native worker")
    report = dict(schema=SCHEMA, scope=__doc__, direct_boundary=direct, separated_boundary=augmented,
        maximum_relative_directional_error=error, maximum_fourth_order_relative_directional_error=error,
        maximum_second_order_relative_directional_error=coarse,
        second_order_truncation_contracts=contracts, verification_threshold=5e-5,
        verification_estimator="two fourth-order Richardson levels",
        implementation_check_passed=bool(np.isfinite(error) and error <= 5e-5 and contracts),
        physical_test_schema=PHYSICAL_SCHEMA, physical_test=boundary.description(),
        finite_boundary_scheme=FINITE_SCHEME,
        lifted_modes_implementation=lifted_binding(flow.M, flow.q.N, context["accepted"]),
        accepted_sha256=sha(args.accepted), prepared_sha256=sha(args.warm),
        tail_config_sha256=sha(args.tail_config), tail_anchor_sha256=sha(output / "actual-anchor-tail.json.gz"),
        source_sha256=sha(__file__), consumed_source_sha256=sources,
        warm_provenance=context["warm_provenance"], actual_anchor=context["actual_anchor"],
        actual_warm_native_height=context["height"].tolist(),
        affine_anchor_native_height=context["height"].tolist(), current_H_equals_affine_anchor=True,
        linear_reference_source="This live worker's complete actual response/J at the actual current warm H, held explicitly affine only for FD",
        nonlinear_DN_evaluated=True, nonlinear_DN_evaluated_during_FD=False,
        nonlinear_native_at_current_H_solved=True, actual_completed_nonlinear_J_reused=True,
        native_worker_calls_during_FD=0, ready_linear_graph_used=False,
        complete_current_warm_boundary_FD_actually_recomputed=True,
        original_directions_perturbations_steps_Richardson_threshold_retained=True,
        old_response_pass_or_warm_SHA_relabelled=False,
        same_live_client_retained=bool(np.isfinite(error) and error <= 5e-5 and contracts),
        cross_process_nonzero_cache_created=False,
        full_BVP_solved=False, full_Cartesian_closed_surface=False)
    write(output / "response-check.json", clean(report))
    return report


def full_argv(args, context, response_path, output):
    values = [str(HERE / "geometry_20261114_physical_test_full_dn.py")]
    options = dict(accepted=args.accepted, port=args.port, warm=args.warm,
        response_check=response_path, tail_client=HERE / CLIENT_NAME,
        tail_config=args.tail_config, tail_source_root=args.tail_source_root,
        out=output, work=args.work, peak_curvature=context["specification"]["peak_curvature"],
        extension_step=args.extension_step, taper_fraction=args.taper_fraction,
        jac_workers=args.jac_workers, max_nodes=args.max_nodes,
        material_angles=args.material_angles, physical_angles=args.physical_angles,
        node_heap=args.node_heap, tol=1e-6, outer_iterations=args.outer_iterations)
    for key, value in options.items():
        values += ["--"+key.replace("_", "-"), str(value)]
    return values


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Execute this numerical orchestration only in this public repository's Actions")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "warm", "warm-status", "port", "tail-config", "tail-source-root",
                 "live128-policy", "out", "work"):
        parser.add_argument("--"+name, type=Path, required=True)
    for name in ("warm-sha256", "warm-status-sha256", "live128-policy-sha256"):
        parser.add_argument("--"+name, required=True)
    parser.add_argument("--node-heap", type=int, default=6144)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--max-nodes", type=int, default=1200)
    parser.add_argument("--material-angles", type=int, default=4096)
    parser.add_argument("--physical-angles", type=int, default=4096)
    parser.add_argument("--outer-iterations", type=int, default=8)
    parser.add_argument("--extension-step", type=float, default=.005)
    parser.add_argument("--taper-fraction", type=float, default=.4)
    parser.add_argument("--native-eta", default="1")
    parser.add_argument("--native-exact-workers", type=int, default=2)
    parser.add_argument("--native-max-factor-bytes", type=int, default=2147483648)
    args = parser.parse_args()
    output, work = args.out.resolve(), args.work.resolve()
    if output == work or output in work.parents or work in output.parents:
        raise ValueError("Use independent full output and reproducible prefix-factor work directories")
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError("Use a fresh orchestration output; no checkpoint or response is silently overwritten")
    work.mkdir(parents=True, exist_ok=True)
    sources = source_inventory()
    # Keep an unwrapped writer: the original full-DN entries annotate their
    # own outputs by installing writers, without changing these receipts.
    write = original.write
    started = time.monotonic()
    state = dict(schema=SCHEMA, phase="validating-actual-inputs", source_sha256=sha(__file__),
        source_repository=os.environ.get("GITHUB_REPOSITORY"), source_commit=os.environ.get("GITHUB_SHA"),
        sources=sources, full_DN_returncode=None, full_BVP_accepted=False,
        full_Cartesian_closed_surface=False, task_completed=False)
    write(output / "orchestration-status.json", state)
    client = None
    saved_argv = sys.argv[:]
    saved_load = original.load_client
    live_policy = original.read(args.live128_policy)
    require_sha(args.live128_policy, args.live128_policy_sha256, "actual live128 policy")
    same(live_policy["factor_parameters"]["eta_cli_text"], args.native_eta, "same original R273 eta")
    same(live_policy["factor_parameters"]["exact_workers"], args.native_exact_workers, "same original R273 workers")
    same(live_policy["factor_parameters"]["max_factor_bytes"], args.native_max_factor_bytes, "same complete factor cap")
    live_environment = {
        "VISIBLE_FLEX_LIVE128_POLICY": str(args.live128_policy.resolve()),
    }
    old_environment = {key: os.environ.get(key) for key in live_environment}
    handoff = dict(load_client_calls=0, full_driver_solve_calls=[], original_full_DN_entry_called=False)
    try:
        context = build_context(args)
        inputs = {name: receipt(getattr(args, name)) for name in
            ("accepted", "warm", "warm_status", "port", "tail_config", "live128_policy")}
        max_native_calls = 1 + 2*args.outer_iterations + 1
        resources = dict(maximum_protocol_calls_from_declared_original_outer_loop=max_native_calls,
            terms=dict(actual91_initial_guess_not_a_protocol_solve=True, actual_warm_anchor=1,
                maximum_outer_anchor_and_end=2*args.outer_iterations, final_fresh_audit=1),
            job_science_clock=live_policy["job_deadline"],
            original_science_total_seconds=19200, workflow_job_minutes=350,
            component_and_owner_caps_clip_same_clock=live_policy["resources"],
            complete_current_H128_component_bytes_additional_to_original64_bound=True,
            no_completed61_bootstrap_or_response_injected=True,
            same_H_original_cache_can_reduce_actual_calls=True,
            original_native_max_iterations=context["config"]["maxIterations"],
            fixed_binary_bytes_per_native_correction=FIXED_BINARY_BYTES_PER_NATIVE_CORRECTION,
            conservative_fixed_binary_bytes_all_calls=(max_native_calls
                * context["config"]["maxIterations"] * FIXED_BINARY_BYTES_PER_NATIVE_CORRECTION),
            excludes_variable_JSON_logs_and_prefix_work=True,
            single_call_32GiB_not_claimed_as_total_full_DN_capacity=True,
            disk_at_start=dict(zip(("total", "used", "free"), shutil.disk_usage(output))),
            no_original_iteration_or_tolerance_changed=True,
            no_retained_snapshot_or_factor_deleted=True)
        state.update(phase="starting-one-live-native-client", inputs=inputs,
            actual_warm_height_identity=array_identity(context["height"]),
            warm_provenance=context["warm_provenance"], resources=resources)
        write(output / "orchestration-status.json", state)
        write(output / "input-binding.json", dict(schema=SCHEMA, inputs=inputs, sources=sources,
            warm_provenance=context["warm_provenance"], current_height=context["height"].tolist(),
            current_height_identity=array_identity(context["height"]),
            native_initial_guess_is_independent_of_prefix_warm=True,
            actual91_is_not_a_completed_response_or_prefix=True,
            completed61_bootstrap_not_called=True, live_policy=receipt(args.live128_policy)))
        response_output = output / "actual-response"
        response_output.mkdir()
        full_output = output / "full-dn"
        full_output.mkdir()
        os.environ.update(live_environment)
        client = saved_load(HERE / CLIENT_NAME, args.tail_config, args.tail_source_root,
            full_output / "true-tail", args.node_heap)
        for key in ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond"):
            if not np.isclose(float(client.cut[key]), float(context["profile"].cut[key]),
                    rtol=2e-11, atol=2e-13):
                raise ValueError("The actual native client and unchanged full scalar use different cuts: " + key)
        state["phase"] = "actual-current-warm-H-and-complete-native-J"
        write(output / "orchestration-status.json", state)
        response = client.solve(context["height"], jacobian=True, audit=False)
        anchor_path = response_output / "actual-anchor-tail.json.gz"
        write(anchor_path, response)
        context["actual_anchor"] = actual_response_binding(client, response, context, anchor_path)
        state.update(phase="original-affine-boundary-FD", actual_anchor=context["actual_anchor"],
            actual_protocol_calls_before_FD=client.calls)
        write(output / "orchestration-status.json", state)
        report = response_check(context, client, response, args, response_output, sources, write)
        report_path = response_output / "response-check.json"
        state.update(implementation_check_passed=report["implementation_check_passed"],
            actual_response_check=receipt(report_path))
        if not report["implementation_check_passed"]:
            state["phase"] = "actual-current-anchor-FD-failed-at-original-gate"
            return 2
        observed_solve = client.solve

        def solve(height, jacobian=True, audit=False):
            # Observe only: original live solve/cache/worker request decides
            # what is evaluated. In particular a changed first H is not
            # replaced by the FD anchor and is not rejected as a new gate.
            h = vector(height, (context["M"],), "full-DN current requested H")
            row = dict(full_driver_call=len(handoff["full_driver_solve_calls"]),
                height_identity=array_identity(h), jacobian=bool(jacobian), audit=bool(audit),
                equals_FD_anchor_numerically=bool(np.array_equal(h, context["height"])),
                equals_FD_anchor_binary64_bits=bool(h.tobytes() == context["height"].tobytes()),
                actual_protocol_calls_before=client.calls, no_anchor_substitution=True)
            handoff["full_driver_solve_calls"].append(row)
            write(output / "same-live-client-handoff.json", handoff)
            try:
                value = observed_solve(h, jacobian=jacobian, audit=audit)
                row.update(completed=True, residual=value["residual"],
                    actual_protocol_calls_after=client.calls,
                    original_same_process_cache_hit=client.calls == row["actual_protocol_calls_before"],
                    audit_returned=value.get("audit") is not None)
                return value
            except Exception as error:
                row.update(completed=False, actual_error=repr(error), actual_protocol_calls_after=client.calls)
                raise
            finally:
                write(output / "same-live-client-handoff.json", handoff)

        client.solve = solve

        def load(module_path, configuration, source_root, prefix, heap):
            handoff["load_client_calls"] += 1
            if handoff["load_client_calls"] != 1:
                raise RuntimeError("The original full-DN entry requested an unexpected second client")
            same(Path(module_path).resolve(), (HERE / CLIENT_NAME).resolve(), "handoff client module")
            same(Path(configuration).resolve(), args.tail_config.resolve(), "handoff native config path")
            same(sha(configuration), CONFIG_SHA, "handoff native config bytes")
            same(Path(source_root).resolve(), args.tail_source_root.resolve(), "handoff restored original sources")
            same(Path(prefix).resolve(), (full_output / "true-tail").resolve(), "handoff original output prefix")
            same(heap, args.node_heap, "handoff original Node heap")
            if client.proc is None or client.proc.poll() is not None:
                raise RuntimeError("The real response/FD worker ended before full-DN handoff")
            handoff.update(same_python_client=True, same_worker_pid=client.proc.pid,
                actual_protocol_calls_at_handoff=client.calls,
                full_actual_response_and_worker_predictor_retained=True,
                imported_nonzero_cache=False, fresh_final_audit_retained=True)
            write(output / "same-live-client-handoff.json", handoff)
            return client

        original.load_client = load
        sys.argv = full_argv(args, context, report_path, full_output)
        handoff.update(original_full_DN_entry_called=True, original_full_DN_argv=sys.argv[:],
            entry_source_sha256=SOURCE_PINS["geometry_20261114_physical_test_full_dn.py"])
        state["phase"] = "original-full-DN-with-same-live-client"
        write(output / "same-live-client-handoff.json", handoff)
        write(output / "orchestration-status.json", state)
        code = int(full_entry.main())
        state["full_DN_returncode"] = code
        actual_path, driver_path = full_output / "actual.json.gz", full_output / "driver-status.json"
        if driver_path.is_file():
            state["original_full_driver_status"] = receipt(driver_path)
        if actual_path.is_file():
            actual = original.read(actual_path)
            state["original_full_actual"] = receipt(actual_path)
            state["full_BVP_accepted"] = bool(code == 0 and actual.get("success") is True)
        state["phase"] = ("original-full-DN-returned-accepted" if state["full_BVP_accepted"]
            else "original-full-DN-returned-without-complete-acceptance")
        return code
    except Exception as error:
        state.update(phase="exception", actual_error=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        original.load_client = saved_load
        sys.argv = saved_argv
        if client is not None:
            client.close()
            state["actual_native_protocol_calls"] = client.calls
            state["actual_worker_exit_code"] = client.proc.poll() if client.proc is not None else None
            state["actual_live_worker_quiet"] = client.live_quiet
            state["actual_live_session_directory"] = str(client.live_session_directory)
        for key, value in old_environment.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        state.update(elapsed_seconds=time.monotonic()-started,
            disk_at_end=dict(zip(("total", "used", "free"), shutil.disk_usage(output))),
            original_full_DN_entry_and_nonlinear_gates_unmodified=True,
            original_native_final_sensitivity_and_audit_not_redirected=False,
            current_H128_stage_boundary_mixed_endpoint_audit_explicitly_supplied=True,
            all_original_full112_affine_FD_fullDN_gates_retained=True,
            actual128_raw_is_not_recovered_from_historical_receipts=True)
        write(output / "same-live-client-handoff.json", clean(handoff))
        write(output / "orchestration-status.json", clean(state))
        print(json.dumps(dict(event="R501_live128_original_full_DN_orchestration_return",
            phase=state["phase"], full_DN_returncode=state["full_DN_returncode"],
            full_BVP_accepted=state["full_BVP_accepted"],
            actual_native_protocol_calls=state.get("actual_native_protocol_calls"),
            elapsed_seconds=state["elapsed_seconds"])), flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
