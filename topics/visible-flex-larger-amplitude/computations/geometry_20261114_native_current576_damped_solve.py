#!/usr/bin/env python3
"""Continue actual59's selected state through the original complete native loop.

Only the original nonlinear correction(ev, states, target) call is replaced.
Every correction consumes that iteration's freshly returned original with-J
arrays and runs the complete current576 R273 square-root model with explicit
eta. The original ten no-J trials, guards, strict infinity-norm decrease,
tolerance, iteration limit, final endpoint Jacobian and audit remain original.
The selected state is restored by its full binary64 words, including signed
zero, with no cut/far projection, checkpoint geometry remapping or H threshold.

All scientific execution is restricted to this public repository's Actions.
The input contract needs only actual59's thirteen small retained trial files,
the unchanged original public78 numerical sources and their normal calibration
assets. Old actual28 arrays are not a current baseline and are not loaded.
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
HOOK_NAME = "geometry_20261114_native_current576_damped_solve_hook.mjs"
QR_NAME = "exact_20261114_current576_damped_chain_qr.py"
QR_SHA = "ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f"
ADAPTER_NAME = "exact_20261114_current576_damped_system.py"
ADAPTER_SHA = "695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90"
FACTOR_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
KERNEL_SHA = "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
MODEL_SCOPE = "R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
VARIABLE = "VISIBLE_FLEX_NATIVE_CURRENT576_DAMPED_SOLVE_SPEC"
PARENT_RESULT_SHA = "c0a9b191e843e9036e84707ffa1855d5881dce13e4b71bf94812e9526b59d00e"
PARENT_SUMMARY_SHA = "770b97e62eda7cbcc10b045c42298b95ef2c55a0f2dd5ac1930690175a156709"
PARENT_CP_SHA = "7659016c0218b8c2e9ba220ca81a0b410b7e38005ea609e417b9b534d76c3556"
PARENT_BINARY_SHA = "8ade070f746caed9a45c582c7485a060e55ee589858f5f88255d8ffd0d9112cb"
PARENT_STATE_SHA = "384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03"
PARENT_PY_SHA = "c337d880c29aaa865b6516fd679ffffe9410d30c893ff2f8e0cc4092f6adbec7"
PARENT_HOOK_SHA = "c104ff11b356cb3993ffd5ae97988259b2f27c91e492c7736d7a96a9ad450e36"
HEIGHT_SHA = "c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f"
SCALES_SHA = "ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc"
FAR_SHA = "395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54"
TARGET_SHA = "e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d"
CORE_SHA = "ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3"
RUNTIME_SHA = "f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f"
EVALUATE_SHA = "9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9"
TRIAL_SHA = "603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99"
INPUT_NAMES = (
    "result.json", "trial-replay-summary.json", "trial-replay-spec.json.gz",
    "selected-state-checkpoint.json.gz", "selected-state.f64le.gz", "trial-input-config.json",
    "native_intent.json", "native_ready.json.gz", "native_capacity.json",
    "restored-original-mathematical-identity-before-seed.json", "core-instrumentation.json",
    "actual-replay-method-identities.json", "native_trials.jsonl",
)


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


def validate_parent(directory, equal, numerical_configuration, numerical_sources):
    directory = Path(directory).resolve()
    paths = {name: directory / name for name in INPUT_NAMES}
    for name, path in paths.items():
        if not path.is_file() or not path.resolve().is_relative_to(directory):
            raise ValueError("Missing or escaping actual59 input: " + name)
    equal(sha(paths["result.json"]), PARENT_RESULT_SHA, "actual59 completed trial result")
    result = read(paths["result.json"])
    for key, value in dict(schema="original-native576-damped-trial-replay-result-v1", replay_completed=True,
            trial_accepted=True, native_accepted=False, task_completed=False, original_native_requests=1,
            worker_exit_code=0, new_J_evaluations=0, new_baseline_evaluations=0,
            fresh_original_no_J_trial_evaluations=1, returned_original_no_J_trial_evaluations=1,
            source_sha256=PARENT_PY_SHA, hook_sha256=PARENT_HOOK_SHA).items():
        equal(result[key], value, "actual59 result " + key)
    listed = {row["file"]: row for row in result["small_output_files"]}
    if len(listed) != len(result["small_output_files"]):
        raise ValueError("Unique complete actual59 file inventory required")
    for name in INPUT_NAMES[1:]:
        equal(described(paths[name]), listed[name], "actual59 retained input " + name)
    values = {name: read(path) for name, path in paths.items()
              if name not in ("selected-state.f64le.gz", "native_trials.jsonl")}
    summary = values["trial-replay-summary.json"]
    packet = values["selected-state-checkpoint.json.gz"]
    prior_spec = values["trial-replay-spec.json.gz"]
    intent = values["native_intent.json"]
    ready = values["native_ready.json.gz"]
    capacity = values["native_capacity.json"]
    live = values["restored-original-mathematical-identity-before-seed.json"]
    core = values["core-instrumentation.json"]
    methods = values["actual-replay-method-identities.json"]
    config = values["trial-input-config.json"]
    equal(sha(paths["trial-replay-summary.json"]), PARENT_SUMMARY_SHA, "actual59 summary")
    equal(sha(paths["selected-state-checkpoint.json.gz"]), PARENT_CP_SHA, "actual59 selected checkpoint")
    equal(sha(paths["selected-state.f64le.gz"]), PARENT_BINARY_SHA, "actual59 selected compressed binary")
    equal(result["spec_sha256"], sha(paths["trial-replay-spec.json.gz"]), "actual59 complete specification")
    equal(summary["spec_sha256"], result["spec_sha256"], "actual59 summary specification")
    equal(summary["source_sha256"], PARENT_PY_SHA, "actual59 source")
    equal(summary["hook_sha256"], PARENT_HOOK_SHA, "actual59 hook")
    equal(summary["replay_completed"], True, "actual59 trial finished")
    equal(summary["trial_accepted"], True, "actual59 original acceptance")
    equal(summary["trials"], result["observed_trials"], "actual59 complete trial list")
    if len(summary["trials"]) != 1:
        raise ValueError("This initializer is bound to actual59's one actually accepted original trial")
    trial = summary["trials"][0]
    equal((trial["iteration"], trial["trial"], trial["step"], trial["kind"]), (0, 0, 1, "accepted"),
          "actual59 original alpha1")
    trial_lines = [json.loads(line) for line in paths["native_trials.jsonl"].read_text().splitlines() if line]
    if len(trial_lines) != 1:
        raise ValueError("One original trial diagnostic is required")
    for key in ("iteration", "trial", "step", "kind", "baseNorm", "trialNorm"):
        equal(trial_lines[0][key], trial[key], "actual original callback " + key)
    equal(result["actual_original_failure_message"],
          "Error: VISIBLE_NATIVE_ORIGINAL576_DAMPED_TRIAL_REPLAY_ACCEPTED_STOP_V1", "actual59 planned stop")
    for key in ("native_accepted", "endpoint_J_computed", "fresh_endpoint_audit_computed", "task_completed"):
        equal(summary[key], False, "actual59 scope " + key)
    for key in ("success", "converged", "native_tail_response", "endpoint_J_computed",
                "fresh_endpoint_audit_computed", "task_completed"):
        equal(packet[key], False, "selected state is not a complete response: " + key)
    equal(packet["schema"], "original-native-one-trial-selected-state-v1", "actual selected schema")
    equal(packet["selected_by_original_strict_norm_decrease"], True, "original selection criterion")
    equal(packet["trial"], trial, "checkpoint selected trial")
    equal(packet["states_binary"], summary["selected_state_binary"], "actual binary descriptor")
    equal(packet["selected_state_float64le_sha256"], PARENT_STATE_SHA, "actual selected words")
    equal(packet["spec_sha256"], result["spec_sha256"], "actual checkpoint specification")
    equal(packet["source_sha256"], PARENT_PY_SHA, "actual checkpoint producer")
    equal(packet["hook_sha256"], PARENT_HOOK_SHA, "actual checkpoint hook")
    raw = gzip.decompress(paths["selected-state.f64le.gz"].read_bytes())
    equal(len(raw), 577 * 224 * 8, "full selected-state byte count")
    equal(hashlib.sha256(raw).hexdigest(), PARENT_STATE_SHA, "full selected-state raw bytes")
    if len(packet["rows"]) != 577:
        raise ValueError("Retain all577 actual original shooting nodes")
    rebuilt = bytearray()
    negative_zero = 0
    for node, row in enumerate(packet["rows"]):
        if row["node"] != node or len(row["state"]) != 224:
            raise ValueError("Complete ordered original selected rows required")
        state = list(row["state"])
        if any(type(x) not in (int, float) or not math.isfinite(x) for x in state):
            raise ValueError("All selected input words must represent finite binary64 values")
        seen = set()
        for j in row["negative_zero_columns"]:
            if type(j) is not int or not 0 <= j < 224 or j in seen or state[j] != 0:
                raise ValueError("Valid distinct signed-zero columns required")
            state[j] = -0.0
            seen.add(j)
            negative_zero += 1
        rebuilt.extend(struct.pack("<224d", *state))
    equal(bytes(rebuilt), raw, "selected CP/raw complete words with negative zero")
    equal(negative_zero, 8, "actual selected signed-zero count")
    height = packet["cutHeight"]
    if len(height) != 112 or any(type(x) not in (int, float) or not math.isfinite(x) for x in height):
        raise ValueError("Preserve the complete actual112-mode physical H")
    equal(hashlib.sha256(struct.pack("<112d", *height)).hexdigest(), HEIGHT_SHA, "full nonzero H bits")
    equal(prior_spec["fresh_request"], dict(height=height, jacobian=True, audit=True), "actual59 full request")
    equal(numerical_configuration(config), config, "only original mathematical input configuration")
    equal(prior_spec["numerical_configuration"], config, "same original configuration")
    if "initialCheckpoint" in config or ready["warmEmbedding"] is not None:
        raise ValueError("Do not introduce a geometric-remapping checkpoint")
    equal(config["maxIterations"], 32, "unchanged original iteration limit")
    equal(config["solveTolerance"], 2e-9, "unchanged original nonlinear tolerance")
    equal(config["modes"], 112, "complete original modes")
    equal(config["quadrature"], 2048, "complete original angular rule")
    equal(numerical_sources(prior_spec["original_source_sha256"]), numerical_sources(intent["source_sha256"]),
          "actual59 complete original numerical source map")
    equal(numerical_configuration(packet["parameters"]), live["parameters"], "selected complete physical parameters")
    equal(packet["rawNode"], live["rawNode"], "selected original physical-node map")
    equal(live["far_graph_float64le_sha256"], FAR_SHA, "original far boundary graph")
    equal(live["evaluate_function_sha256"], EVALUATE_SHA, "actual59 restored original evaluate")
    equal(core["original_core_file_sha256"], CORE_SHA, "original source core")
    equal(core["original_runtime_core_sha256"], RUNTIME_SHA, "original runtime core")
    equal(core["exact_all_replay_and_evaluate_observer_roundtrip_verified"], True, "actual59 source restoration")
    equal(core["original_trial_loop_sha256"], TRIAL_SHA, "original ten-trial source")
    equal(methods["core_instrumentation_sha256"], sha(paths["core-instrumentation.json"]), "actual59 method/core identity")
    equal(methods["evaluate_source_identity"]["original_evaluate_source_sha256"], EVALUATE_SHA,
          "actual59 evaluate comparison scope")
    receipts = {name: described(path, local=True) for name, path in paths.items()}
    parent = dict(public_run="43640772654", result=described(paths["result.json"]),
                  summary=described(paths["trial-replay-summary.json"]),
                  checkpoint=described(paths["selected-state-checkpoint.json.gz"]),
                  binary=described(paths["selected-state.f64le.gz"]),
                  states_float64le_sha256=PARENT_STATE_SHA, height_float64le_sha256=HEIGHT_SHA)
    return dict(inputs=receipts, parent_selected59=parent, config=config, height=height,
                intent=intent, ready=ready, capacity=capacity, original_live_identity=live,
                restored_negative_zero_count=negative_zero, prior_trial=trial)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public":
        raise RuntimeError("All native/current QR computations belong only to this public repository Actions")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--selected-directory", type=Path, required=True)
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
    if a.out.is_relative_to(a.selected_directory.resolve()):
        raise ValueError("Keep all current outputs independent of immutable selected inputs")
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

    prior = validate_parent(a.selected_directory, equal, numerical_configuration, numerical_sources)
    config_path = a.out / "current-input-config.json"
    write(config_path, prior["config"])
    hook = HERE / HOOK_NAME
    request = dict(height=prior["height"], jacobian=True, audit=True)
    spec = dict(schema="native-current576-damped-solve-spec-v1", source_sha256=sha(__file__), hook_sha256=sha(hook),
        frozen_sources=frozen, parent_selected59=prior["parent_selected59"], inputs=prior["inputs"],
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
        only_nonlinear_correction_call_replaced=True, original_ten_trial_body_retained=True,
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
    result = dict(schema="native-current576-damped-solve-result-v1", source_sha256=sha(__file__),
        hook_sha256=sha(hook), specification=specification, spec_sha256=sha(spec_path),
        parent_selected59=prior["parent_selected59"], current_direction_source_sha256=QR_SHA,
        current_system_source_sha256=ADAPTER_SHA, factor_engine_source_sha256=FACTOR_SHA,
        eta_cli_text=a.eta, eta_binary64=number_record(eta), model_scope=MODEL_SCOPE,
        native_accepted=False, requested_full_DN_Jacobian=True, requested_full_finite_audit=True,
        complete_original_native_loop_requested=True, only_nonlinear_correction_call_replaced=True,
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
        write(a.out / "verified-launch-intent.json", dict(schema="native-current576-damped-verified-launch-v1",
            spec_sha256=sha(spec_path), source_sha256=sha(__file__), hook_sha256=sha(hook),
            parent_selected59=prior["parent_selected59"], inputs=prior["inputs"], request=request,
            actual_command=commands[0], current_sources=client.sources,
            current_capacity_sha256=sha(client.capacity_record), complete_current_ready_sha256=sha(a.out / "native_ready.json.gz"),
            identity_verified_before_request=True, initial_native_solve_calls=0, initial_response_cache_empty=True))
        print(json.dumps(dict(event="current576-native-selected59-identities-verified", selected_state_raw_sha256=PARENT_STATE_SHA,
                              same_complete_H=True, eta_cli_text=a.eta, fresh_withJ_each_iteration=True)), flush=True)
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
    print(json.dumps(dict(event="current576-native-original-loop-finished", native_accepted=result["native_accepted"],
                          snapshots=result.get("fresh_withJ_snapshots"), directions=result.get("current_R273_directions_returned"),
                          residual=result.get("residual"), task_completed=False)), flush=True)
    return 0 if result["native_accepted"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
