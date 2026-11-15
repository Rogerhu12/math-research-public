#!/usr/bin/env python3
"""Continue actual61's failed final raw state with a no-J-primal variational flow.

The initial guess is the exact complete577 binary64 state saved at actual61
iteration3. It is not a successful native response or an imported predictor.
The original no-J root/RHS/rk4 and all original evaluate/trial/guard/tolerance
rules remain unchanged. A separately identified with-J flow follows that
same complete226-state primal and forms fresh captured-root derivatives.
Only the nonlinear core correction call uses the complete current576 R273
square-root model. The original final endpoint sensitivity and audit are
not regularized or replaced. Every current J/state/r/cut/far/sigma/H is saved.

Only public repository Actions may execute science. The inputs are the same
selected actual61 metadata and nine non-J arrays already used by request69;
old saved J arrays and factor payloads are neither read nor relabelled.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import struct
import sys
import time

HERE = Path(__file__).resolve().parent
HOOK_NAME = "geometry_20261114_noj_primal_current576_damped_solve_hook.mjs"
QR_NAME = "exact_20261114_noj_primal_current576_damped_chain_qr.py"
QR_SHA = "70bc10dfb31717b662265485d10a15028365dbba5db85ccf9c8f592226e33955"
ADAPTER_NAME = "exact_20261114_noj_primal_current576_damped_system.py"
ADAPTER_SHA = "48297483617c56179fdd4d6b80e9aeeb1151bf89c90fd816ca41d2e3ccc0bcb3"
FACTOR_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
KERNEL_SHA = "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
MODEL_SCOPE = "R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
VARIABLE = "VISIBLE_FLEX_NOJ_PRIMAL_CURRENT576_DAMPED_SOLVE_SPEC"
INPUT_HELPER = "geometry_20261114_current576_same_state_noj_probe.py"
INPUT_HELPER_SHA = "fc2c61d35e6eb3b1e8d836f46b75c7dc5ec2f2f69bcd483410a289434637099b"
PRIMAL_MODULE = "geometry_20261114_noj_matched_variational_engine.mjs"
PRIMAL_MODULE_SHA = "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9"
ORIGINAL_DEPENDENCIES = {
    "product_jacobian": "205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25",
    "local_cusp_grid": "b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f",
}
PARENT_STATE_SHA = "b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013"
HEIGHT_SHA = "c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f"
SCALES_SHA = "ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc"
FAR_SHA = "395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54"
TARGET_SHA = "e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d"
CORE_SHA = "ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3"
RUNTIME_SHA = "f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f"
EVALUATE_SHA = "9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9"
TRIAL_SHA = "603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def described(path, *, local=False):
    path = Path(path)
    row = dict(file=path.name, bytes=path.stat().st_size, sha256=sha(path))
    if local:
        row["path"] = str(path.resolve())
    return row


def write(path, value, *, compressed=False):
    path = Path(path)
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode()
    stored = gzip.compress(raw, compresslevel=9, mtime=0) if compressed else raw
    # This is a file/publication constraint, not a mathematical truncation.
    if len(stored) >= 4_900_000:
        raise ValueError("Complete metadata must be saved in bounded gzip files; no fields may be truncated")
    with path.open("xb") as stream:
        stream.write(stored)
    row = described(path)
    if compressed:
        row.update(raw_bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest(), encoding="json-gzip")
    return row


def number_record(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("A finite explicit scalar is required")
    return dict(value=value, float64le_hex=struct.pack("<d", value).hex(), classification="finite")


def frozen_sources():
    return {
        QR_NAME: QR_SHA, ADAPTER_NAME: ADAPTER_SHA,
        INPUT_HELPER: INPUT_HELPER_SHA, PRIMAL_MODULE: PRIMAL_MODULE_SHA,
        "exact_20261114_native_damped_chain_qr.py": FACTOR_SHA,
        "exact_20261114_native_allrows_dyadic_residual.py": KERNEL_SHA,
        "geometry_20261114_native_captured_band_correction.py":
            "b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390",
        "exact_20261114_true_tail_client.py":
            "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
        "exact_20261114_seeded_zero_tail_client.py":
            "a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776",
        "tail_frozen_worker.mjs":
            "3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054",
        "tail_resumable_engine.mjs":
            "1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8",
    }


def validate_parent(args, equal, numerical_configuration, numerical_sources):
    # This frozen helper verifies the actual failed native result, all five
    # snapshot metadata records and every byte of all nine non-J inputs.
    # It never imports a saved-J system or runs a scientific calculation.
    import geometry_20261114_current576_same_state_noj_probe as evidence
    if Path(evidence.__file__).resolve() != HERE / INPUT_HELPER:
        raise ValueError("Use the pinned actual61 input reader from this checkout")
    bound = evidence.bind_inputs(args, equal, numerical_configuration, numerical_sources)

    def plain(item):
        return {key: item[key] for key in ("file", "bytes", "sha256")}

    parent = dict(schema="actual61-failed-native-final-snapshot-anchor-v1",
        native_result=plain(bound["native_inputs"]["result.json"]),
        summary=plain(bound["native_inputs"]["current-correction-summary.json"]),
        snapshot_result=plain(bound["snapshot_inputs"]["result"]),
        snapshot_context=plain(bound["snapshot_inputs"]["context"]),
        snapshot_manifest=plain(bound["snapshot_inputs"]["manifest"]),
        state_raw_sha256=PARENT_STATE_SHA, source_native_call=1,
        source_nonlinear_iteration=3, source_snapshot_sequence=3, native_accepted=False)

    def raw_array(name):
        binding=bound["arrays"][name]
        data=b"".join(evidence.verified(Path(binding["directory"]),item).read_bytes()
                      for item in binding["entry"]["chunks"])
        equal(hashlib.sha256(data).hexdigest(),binding["entry"]["raw_sha256"],
              "literal original complete " + name)
        return data

    height_raw=raw_array("physical-height")
    equal(hashlib.sha256(height_raw).hexdigest(),HEIGHT_SHA,"same complete original nonzero H")
    height=[item[0] for item in struct.iter_unpack("<d",height_raw)]
    state_raw=raw_array("base-states")
    equal(hashlib.sha256(state_raw).hexdigest(),PARENT_STATE_SHA,"actual failed61 raw initial guess")
    negative_zeros=sum(word==(1<<63) for (word,) in struct.iter_unpack("<Q",state_raw))
    return dict(inputs=bound["native_inputs"],snapshot_inputs=bound["snapshot_inputs"],
        original_arrays=bound["arrays"],parent_failed61=parent,config=bound["config"],height=height,
        restored_negative_zero_count=negative_zeros,intent=bound["intent"],ready=bound["ready"],
        capacity=bound["capacity"],original_live_identity=bound["live"],
        parent_withJ_norm=bound["context"]["current_original_norm"],
        parent_J_descriptor_only=bound["original_J_descriptor_only"])


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public":
        raise RuntimeError("All native/current QR computations belong only to this public repository Actions")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--native-directory", type=Path, required=True)
    p.add_argument("--native-result-sha256", required=True)
    p.add_argument("--snapshot-directory", type=Path, required=True)
    p.add_argument("--snapshot-result-sha256", required=True)
    p.add_argument("--source-topic", type=Path, required=True)
    p.add_argument("--eta", default="1")
    p.add_argument("--node-heap", type=int, default=6144)
    p.add_argument("--exact-workers", type=int, default=2)
    p.add_argument("--max-factor-bytes", type=int, default=2147483648)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    eta = float(a.eta)
    if not math.isfinite(eta) or eta <= 0:
        raise ValueError("An explicit positive finite R273 eta is required")
    if a.exact_workers < 1 or a.max_factor_bytes < 1 or a.node_heap < 1:
        raise ValueError("Explicit positive resource limits are required")
    a.out = a.out.resolve()
    if (a.out.is_relative_to(a.native_directory.resolve())
            or a.out.is_relative_to(a.snapshot_directory.resolve())):
        raise ValueError("Keep all current outputs independent of immutable failed61 inputs")
    a.out.mkdir(parents=True, exist_ok=True)
    if any(a.out.iterdir()):
        raise ValueError("Use an empty current-native output directory")
    frozen = frozen_sources()
    for name, digest in frozen.items():
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or sha(HERE / name) != digest:
            raise ValueError("Frozen numerical or bridge source changed: " + name)
    from exact_20261114_seeded_zero_tail_client import same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS
    import exact_20261114_true_tail_client as original

    def equal(left, right, label):
        if not same(left, right):
            raise ValueError("Current-native provenance differs: " + label)

    prior = validate_parent(a, equal, numerical_configuration, numerical_sources)
    config_path = a.out / "current-input-config.json"
    write(config_path, prior["config"])
    hook = HERE / HOOK_NAME
    request = dict(height=prior["height"], jacobian=True, audit=True)
    spec = dict(schema="native-noj-primal-current576-damped-solve-spec-v1", source_sha256=sha(__file__), hook_sha256=sha(hook),
        frozen_sources=frozen, parent_failed61=prior["parent_failed61"], inputs=prior["inputs"],
        snapshot_inputs=prior["snapshot_inputs"],original_arrays=prior["original_arrays"],
        parent_saved_J_descriptor_only=prior["parent_J_descriptor_only"],
        parent_failed_withJ_norm=prior["parent_withJ_norm"],
        source_topic=str(a.source_topic.resolve()),
        primal_flow_module=dict(file=PRIMAL_MODULE,bytes=(HERE/PRIMAL_MODULE).stat().st_size,
                               sha256=PRIMAL_MODULE_SHA),
        original_primal_dependencies=ORIGINAL_DEPENDENCIES,
        original_source_sha256=prior["intent"]["source_sha256"], numerical_configuration=prior["config"],
        numerical_parameters=prior["original_live_identity"]["parameters"],
        original_live_identity=prior["original_live_identity"], io_keys=sorted(IO_KEYS), output=str(a.out),
        fresh_request=request, selected_state_float64le_sha256=PARENT_STATE_SHA,
        selected_negative_zero_count=prior["restored_negative_zero_count"],
        exact_height_float64le_sha256=HEIGHT_SHA, original_scales_float64le_sha256=SCALES_SHA,
        original_far_graph_float64le_sha256=FAR_SHA, original_cut_target_float64le_sha256=TARGET_SHA,
        original_core_file_sha256=CORE_SHA, original_runtime_core_sha256=RUNTIME_SHA,
        original_evaluate_source_sha256=EVALUATE_SHA, original_ten_trial_body_sha256=TRIAL_SHA,
        bridge=dict(python_executable=sys.executable, source_file=QR_NAME, source_sha256=QR_SHA,
            system_source_file=ADAPTER_NAME, system_source_sha256=ADAPTER_SHA,
            factor_engine_source_sha256=FACTOR_SHA, kernel_source_sha256=KERNEL_SHA,
            eta_cli_text=a.eta, eta_binary64=number_record(eta), model_scope=MODEL_SCOPE,
            exact_workers=a.exact_workers, max_factor_bytes=a.max_factor_bytes,
            shell=False, stdout_and_stderr_are_iteration_files=True),
        current_state_withJ_required_at_every_original_iteration=True, no_cached_baseline=True,
        only_nonlinear_correction_call_replaced=False, only_core_nonlinear_correction_call_replaced=True,
        independently_identified_withJ_flow_replaced=True, original_ten_trial_body_retained=True,
        original_max_iterations=prior["config"]["maxIterations"], original_solve_tolerance=prior["config"]["solveTolerance"],
        original_final_endpoint_J_and_fresh_audit_retained=True, soft_cut_and_far_direction_not_projected=True,
        no_initialCheckpoint_remesh=True, no_height_threshold=True, no_zero_solve=True, task_completed=False)
    spec_path = a.out / "current-solve-spec.json.gz"
    specification = write(spec_path, spec, compressed=True)
    previous = os.environ.get(VARIABLE)
    os.environ[VARIABLE] = str(spec_path)
    popen = original.subprocess.Popen
    commands = []
    client = None
    response = None
    started = time.monotonic()
    result = dict(schema="native-noj-primal-current576-damped-solve-result-v1", source_sha256=sha(__file__),
        hook_sha256=sha(hook), specification=specification, spec_sha256=sha(spec_path),
        parent_failed61=prior["parent_failed61"], current_direction_source_sha256=QR_SHA,
        current_system_source_sha256=ADAPTER_SHA, factor_engine_source_sha256=FACTOR_SHA,
        eta_cli_text=a.eta, eta_binary64=number_record(eta), model_scope=MODEL_SCOPE,
        native_accepted=False, requested_full_DN_Jacobian=True, requested_full_finite_audit=True,
        complete_original_native_loop_requested=True,
        new_primal_variational_source_sha256=PRIMAL_MODULE_SHA,
        original_ready_describes_original_constructor_only=True, only_nonlinear_correction_call_replaced=False, only_core_nonlinear_correction_call_replaced=True,
        independently_identified_withJ_flow_replaced=True,
        original_tolerance=prior["config"]["solveTolerance"], original_max_iterations=prior["config"]["maxIterations"],
        cached28_or_other_old_baseline_loaded=False, original_final_endpoint_J_and_audit_retained=True,
        accepted_prefix=False, complete_tail_matching=False, task_completed=False)

    def observed_popen(command, *args, **kwargs):
        worker = str(HERE / "tail_frozen_worker.mjs")
        if not isinstance(command, list) or worker not in command:
            return popen(command, *args, **kwargs)
        if len(command) != 8 or command[0] != "node" or command[4] != "--import" or command[6] != worker:
            raise ValueError("Instrument only the unchanged original worker launch")
        actual = list(command[:6]) + ["--import", str(hook)] + list(command[6:])
        commands.append(actual)
        return popen(actual, *args, **kwargs)

    try:
        original.subprocess.Popen = observed_popen
        try:
            client = original.TailClient(config_path, a.source_topic.resolve() / "repro/source-root", a.out / "native", node_heap=a.node_heap)
        finally:
            original.subprocess.Popen = popen
        equal(numerical_configuration(client._configuration), prior["config"], "unchanged current original configuration")
        equal(numerical_sources(client.sources), numerical_sources(prior["intent"]["source_sha256"]), "unchanged current original numerical sources")
        equal(ready_semantics(client.ready), ready_semantics(prior["ready"]), "unchanged original current ready semantics")
        capacity = original.read(client.capacity_record)
        for key in ("name", "capacity", "requestedCapacity", "nodeVersion", "adapterSHA256", "originalConstructorCapacity", "numericalChange", "retained", "files"):
            equal(capacity[key], prior["capacity"][key], "unchanged original capacity " + key)
        if len(commands) != 1 or client.calls != 0 or client.cache_key is not None:
            raise ValueError("Start one fresh original worker with an empty response cache")
        write(a.out / "verified-launch-intent.json", dict(schema="native-noj-primal-current576-damped-verified-launch-v1",
            spec_sha256=sha(spec_path), source_sha256=sha(__file__), hook_sha256=sha(hook),
            parent_failed61=prior["parent_failed61"], inputs=prior["inputs"], request=request,
            actual_command=commands[0], current_sources=client.sources,
            current_capacity_sha256=sha(client.capacity_record), complete_current_ready_sha256=sha(a.out / "native_ready.json.gz"),
            identity_verified_before_request=True, initial_native_solve_calls=0, initial_response_cache_empty=True))
        print(json.dumps(dict(event="noj-primal-current576-failed61-identities-verified", failed61_initial_state_raw_sha256=PARENT_STATE_SHA,
                              same_complete_H=True, eta_cli_text=a.eta, fresh_withJ_each_iteration=True,
                              failed61_state_is_only_initial_guess=True, original_noJ_primal_retained=True)), flush=True)
        response = client.solve(prior["height"], jacobian=True, audit=True)
        result["original_complete_client_response_returned"] = True
        result["residual"] = response["residual"]
        result["audit"] = response["audit"]
        result["jets_summary"] = {key: response["jets"][key] for key in ("meanSlope", "meanSecond", "meanSlopeCorrection", "meanSecondCorrection")}
    except Exception as error:
        result["actual_error"] = repr(error)
    finally:
        original.subprocess.Popen = popen
        if client is not None:
            client.close()
            result["original_native_requests"] = client.calls
            result["actual_worker_exit_code"] = client.proc.poll() if client.proc else None
        if previous is None:
            os.environ.pop(VARIABLE, None)
        else:
            os.environ[VARIABLE] = previous
        response_path = a.out / "native_0001.json.gz"
        if response_path.is_file():
            result["original_response"] = described(response_path)
            actual = read(response_path)["response"]
            result["actual_original_failure_message"] = actual.get("failed")
            result["actual_original_converged_flag"] = actual.get("converged")
        bridge_path = a.out / "current-correction-summary.json"
        if bridge_path.is_file():
            result["current_correction_summary"] = described(bridge_path)
            bridge_summary = read(bridge_path)
            result["fresh_withJ_snapshots"] = bridge_summary.get("snapshots_completed")
            result["current_R273_directions_returned"] = bridge_summary.get("directions_returned")
            result["bridge_failure"] = bridge_summary.get("actual_bridge_failure")
        result["native_accepted"] = bool(response is not None and result.get("original_native_requests") == 1
                                          and result.get("actual_worker_exit_code") == 0 and not result.get("actual_error"))
        result["success"] = result["native_accepted"]
        result["elapsed_seconds"] = time.monotonic() - started
        result["small_output_files"] = [described(f) for f in sorted(a.out.iterdir()) if f.is_file() and f.name != "result.json"]
        write(a.out / "result.json", result)
    print(json.dumps(dict(event="noj-primal-current576-original-loop-finished", native_accepted=result["native_accepted"],
                          snapshots=result.get("fresh_withJ_snapshots"), directions=result.get("current_R273_directions_returned"),
                          residual=result.get("residual"), task_completed=False)), flush=True)
    return 0 if result["native_accepted"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
