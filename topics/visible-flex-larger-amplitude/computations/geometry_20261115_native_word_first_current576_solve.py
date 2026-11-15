#!/usr/bin/env python3
"""Try one adjacent input word inside the full original native continuation.

Initial data are actual73 iteration2's complete failed raw BASE preserved
in the complete actual91 archive. The rejected83 trial is not the seed.
An independent one-coordinate proposal is screened on all original129248
saved affine rows and all first fresh129248 affine rows. If selected, it
occupies the first original correction; the original ten no-J trials alone
accept a step. All subsequent corrections, or a nonselected first proposal,
use the complete frozen R273 current576 QR. The original32 total iterations,
all boundaries, sigma, H, tolerance2e-9, final endpoint J and audit remain.

Old ready/capacity payload and old base flow-output are absent from91; no
comparison to those missing bytes is invented. The new worker checks its
own original constructor, original mathematical source/configuration and
all original parameters, raw-node map, cells, graphs, gains and far words.
Science is restricted to the public repository Actions; outputs are complete.
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
import traceback
import importlib

HERE = Path(__file__).resolve().parent
HOOK_NAME = "geometry_20261115_native_word_first_current576_solve_hook.mjs"
QR_NAME = "exact_20261115_native_word_first_current576_chain_qr.py"
QR_SHA = "4c887fbb4a16e0d2219969043e708c2d49c446f0ac75ba1dc3e6e17f7d2ee314"
ADAPTER_NAME = "exact_20261115_native_word_first_current576_system.py"
ADAPTER_SHA = "2c6c012d9f2306f2ac13d240510eb8086b74d2b60ff318aa9e359dd72c05a3a8"
FACTOR_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
KERNEL_SHA = "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
MODEL_SCOPE = "R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
VARIABLE = "VISIBLE_FLEX_NATIVE_WORD_FIRST_CURRENT576_SOLVE_SPEC"
INPUT_HELPER = "exact_20261115_native_word_first_parent.py"
INPUT_HELPER_SHA = "8cd7027df2f7039302dbdc1ed15068c6cf48d6645bc236d74e6e5b1e7dd387e8"
CANDIDATE_NAME = "exact_20261115_native_word_first_candidate.py"
CANDIDATE_SHA = "d9692107d197dcb4478fc2027beec21e3e611e67109af9d4b13ae09fb506e226"
PRIMAL_MODULE = "geometry_20261114_noj_matched_variational_engine.mjs"
PRIMAL_MODULE_SHA = "f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9"
ORIGINAL_DEPENDENCIES = {
    "product_jacobian": "205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25",
    "local_cusp_grid": "b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f",
}
PARENT_STATE_SHA = "f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6"
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
        INPUT_HELPER: INPUT_HELPER_SHA, PRIMAL_MODULE: PRIMAL_MODULE_SHA, CANDIDATE_NAME: CANDIDATE_SHA,
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
    path=HERE/INPUT_HELPER
    if sha(path)!=INPUT_HELPER_SHA:raise ValueError("The complete actual91 parent binder changed")
    evidence=importlib.import_module(path.stem)
    if Path(evidence.__file__).resolve()!=path:raise ValueError("The exact parent helper path is required")
    bound=evidence.bind_parent91(args.original91_directory,args.out/"parent91")
    parent_path=args.out/"parent91/input-binding.json.gz"
    def raw_array(name):
        desc=bound["original_arrays"][name]
        p=evidence.verified(parent_path.parent,desc)
        return p.read_bytes()
    height_raw=raw_array("physical-height");state_raw=raw_array("base-states")
    equal(hashlib.sha256(height_raw).hexdigest(),HEIGHT_SHA,"same complete original nonzero H")
    equal(hashlib.sha256(state_raw).hexdigest(),PARENT_STATE_SHA,"actual failed73 raw BASE")
    height=[item[0] for item in struct.iter_unpack("<d",height_raw)]
    negative_zeros=sum(word==(1<<63) for (word,) in struct.iter_unpack("<Q",state_raw))
    return dict(parent_binding=described(parent_path,local=True),parent_binding_directory=str(parent_path.parent),
        original_arrays=bound["original_arrays"],parent_failed73=bound["parent_failed73"],
        config=bound["numerical_configuration"],height=height,original_context=bound["original_context"],
        original_sources=bound["original_sources"],restored_negative_zero_count=negative_zeros,
        parent_withJ_norm=bound["original_context"]["current_original_norm"],
        old_complete_model_screen=bound["old_complete_model_screen"])


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public":
        raise RuntimeError("All native/current QR computations belong only to this public repository Actions")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--original91-directory", type=Path, required=True)
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
    if (a.out.is_relative_to(a.original91_directory.resolve())
            or a.original91_directory.resolve().is_relative_to(a.out)):
        raise ValueError("Keep outputs independent of immutable original91 inputs")
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

    try:
        prior = validate_parent(a, equal, numerical_configuration, numerical_sources)
    except Exception as error:
        write(a.out/"parent-binding-failure.json",dict(schema="native-word-first-parent-binding-failure-v1",
            source_sha256=sha(__file__),actual_error=repr(error),traceback=traceback.format_exc(),
            native_calls_started=0,native_accepted=False,task_completed=False))
        raise
    config_path = a.out / "current-input-config.json"
    write(config_path, prior["config"])
    hook = HERE / HOOK_NAME
    request = dict(height=prior["height"], jacobian=True, audit=True)
    spec = dict(schema="native-word-first-current576-damped-solve-spec-v1", source_sha256=sha(__file__), hook_sha256=sha(hook),
        frozen_sources=frozen,parent_failed73=prior["parent_failed73"],parent_binding=prior["parent_binding"],
        parent_binding_directory=prior["parent_binding_directory"],original_arrays=prior["original_arrays"],
        parent_failed_withJ_norm=prior["parent_withJ_norm"],source_topic=str(a.source_topic.resolve()),
        primal_flow_module=dict(file=PRIMAL_MODULE,bytes=(HERE/PRIMAL_MODULE).stat().st_size,sha256=PRIMAL_MODULE_SHA),
        original_primal_dependencies=ORIGINAL_DEPENDENCIES,
        original_source_sha256=prior["original_sources"],numerical_configuration=prior["config"],
        numerical_parameters=prior["original_context"]["parameters"],io_keys=sorted(IO_KEYS),output=str(a.out),
        fresh_request=request,selected_state_float64le_sha256=PARENT_STATE_SHA,
        selected_negative_zero_count=prior["restored_negative_zero_count"],
        exact_height_float64le_sha256=HEIGHT_SHA,original_scales_float64le_sha256=SCALES_SHA,
        original_far_graph_float64le_sha256=FAR_SHA,original_cut_target_float64le_sha256=TARGET_SHA,
        original_core_file_sha256=CORE_SHA,original_runtime_core_sha256=RUNTIME_SHA,
        original_evaluate_source_sha256=EVALUATE_SHA,original_ten_trial_body_sha256=TRIAL_SHA,
        bridge=dict(python_executable=sys.executable,source_file=QR_NAME,source_sha256=QR_SHA,
            system_source_file=ADAPTER_NAME,system_source_sha256=ADAPTER_SHA,
            factor_engine_source_sha256=FACTOR_SHA,kernel_source_sha256=KERNEL_SHA,
            eta_cli_text=a.eta,eta_binary64=number_record(eta),model_scope=MODEL_SCOPE,
            exact_workers=a.exact_workers,max_factor_bytes=a.max_factor_bytes,
            shell=False,stdout_and_stderr_are_iteration_files=True),
        word_candidate=dict(source_file=CANDIDATE_NAME,source_sha256=CANDIDATE_SHA,
            parent_source_sha256=INPUT_HELPER_SHA,only_original_iteration=0,
            old_complete_model_predicted_strict_decrease=prior["old_complete_model_screen"]["predicted_strict_decrease"],
            candidate_coordinate=dict(node=11,column=75,component="Q",mode=76),
            original_total32_and_ten_trial_body_not_extended=True,
            no_extra_step_accepted_before_original_loop=True,
            same_fresh_snapshot_R273_fallback_if_not_model_selected=True),
        current_state_withJ_required_at_every_original_iteration=True,no_cached_baseline=True,
        only_nonlinear_correction_call_replaced=False,only_core_nonlinear_correction_call_replaced=True,
        independently_identified_withJ_flow_replaced=True,original_ten_trial_body_retained=True,
        original_max_iterations=prior["config"]["maxIterations"],original_solve_tolerance=prior["config"]["solveTolerance"],
        original_final_endpoint_J_and_fresh_audit_retained=True,soft_cut_and_far_direction_not_projected=True,
        no_initialCheckpoint_remesh=True,no_height_threshold=True,no_zero_solve=True,task_completed=False)
    spec_path = a.out / "current-solve-spec.json.gz"
    specification = write(spec_path, spec, compressed=True)
    previous = os.environ.get(VARIABLE)
    os.environ[VARIABLE] = str(spec_path)
    popen = original.subprocess.Popen
    commands = []
    client = None
    response = None
    started = time.monotonic()
    result = dict(schema="native-word-first-current576-damped-solve-result-v1", source_sha256=sha(__file__),
        hook_sha256=sha(hook), specification=specification, spec_sha256=sha(spec_path),
        parent_failed73=prior["parent_failed73"], parent_binding=prior["parent_binding"],
        word_candidate_source_sha256=CANDIDATE_SHA,current_direction_source_sha256=QR_SHA,
        current_system_source_sha256=ADAPTER_SHA, factor_engine_source_sha256=FACTOR_SHA,
        eta_cli_text=a.eta, eta_binary64=number_record(eta), model_scope=MODEL_SCOPE,
        native_accepted=False, requested_full_DN_Jacobian=True, requested_full_finite_audit=True,
        complete_original_native_loop_requested=True,
        new_primal_variational_source_sha256=PRIMAL_MODULE_SHA,
        original_ready_describes_original_constructor_only=True, only_nonlinear_correction_call_replaced=False, only_core_nonlinear_correction_call_replaced=True,
        independently_identified_withJ_flow_replaced=True,
        original_tolerance=prior["config"]["solveTolerance"], original_max_iterations=prior["config"]["maxIterations"],
        old_saved_model_used_only_for_first_candidate_selection=True,
        old_J_never_substituted_for_current_fresh_J=True,
        first_word_correction_counts_inside_original_total32=True,
        original_final_endpoint_J_and_audit_retained=True,
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
        equal(numerical_sources(client.sources),numerical_sources(prior["original_sources"]),"unchanged current original numerical sources")
        capacity=original.read(client.capacity_record)
        # TrueTailClient has performed its original constructor/ready/capacity
        # checks. Actual91 did not include the old ready/capacity bytes, so
        # retain this complete fresh record without claiming an old-byte audit.
        write(a.out/"fresh-constructor-provenance.json",dict(schema="native-word-first-fresh-constructor-provenance-v1",
            current_sources=client.sources,current_capacity=capacity,current_ready=client.ready,
            old_ready_capacity_payload_not_present_in91=True,old_ready_capacity_bitwise_comparison_not_claimed=True,
            original_true_client_validation_not_bypassed=True,native_accepted=False))
        if len(commands) != 1 or client.calls != 0 or client.cache_key is not None:
            raise ValueError("Start one fresh original worker with an empty response cache")
        write(a.out / "verified-launch-intent.json", dict(schema="native-word-first-current576-damped-verified-launch-v1",
            spec_sha256=sha(spec_path), source_sha256=sha(__file__), hook_sha256=sha(hook),
            parent_failed73=prior["parent_failed73"], parent_binding=prior["parent_binding"], request=request,
            actual_command=commands[0], current_sources=client.sources,
            current_capacity_sha256=sha(client.capacity_record), complete_current_ready_sha256=sha(a.out / "native_ready.json.gz"),
            identity_verified_before_request=True, initial_native_solve_calls=0, initial_response_cache_empty=True))
        print(json.dumps(dict(event="word-first-current576-failed73-identities-verified", failed73_initial_state_raw_sha256=PARENT_STATE_SHA,
                              same_complete_H=True, eta_cli_text=a.eta, fresh_withJ_each_iteration=True,
                              failed73_state_is_only_initial_guess=True, original_noJ_primal_retained=True)), flush=True)
        response = client.solve(prior["height"], jacobian=True, audit=True)
        result["original_complete_client_response_returned"] = True
        result["residual"] = response["residual"]
        result["audit"] = response["audit"]
        result["jets_summary"] = {key: response["jets"][key] for key in ("meanSlope", "meanSecond", "meanSlopeCorrection", "meanSecondCorrection")}
    except Exception as error:
        result["actual_error"] = repr(error)
        result["actual_traceback"] = traceback.format_exc()
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
            result["current_directions_returned"] = bridge_summary.get("directions_returned")
            result["current_R273_directions_returned"] = bridge_summary.get("R273_directions_returned")
            result["word_directions_returned"] = bridge_summary.get("word_directions_returned")
            result["bridge_failure"] = bridge_summary.get("actual_bridge_failure")
        result["native_accepted"] = bool(response is not None and result.get("original_native_requests") == 1
                                          and result.get("actual_worker_exit_code") == 0 and not result.get("actual_error"))
        result["success"] = result["native_accepted"]
        result["elapsed_seconds"] = time.monotonic() - started
        result["small_output_files"] = [described(f) for f in sorted(a.out.iterdir()) if f.is_file() and f.name != "result.json"]
        write(a.out / "result.json", result)
    print(json.dumps(dict(event="word-first-current576-original-loop-finished", native_accepted=result["native_accepted"],
                          snapshots=result.get("fresh_withJ_snapshots"), directions=result.get("current_R273_directions_returned"),
                          residual=result.get("residual"), task_completed=False)), flush=True)
    return 0 if result["native_accepted"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
