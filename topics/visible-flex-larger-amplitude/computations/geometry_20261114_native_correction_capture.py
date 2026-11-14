#!/usr/bin/env python3
"""Capture the original first native Newton model/correction and stop before trials.

Only the actual25/23 complete fixed seed and original physical H are used.
The original first withJac and original correction arithmetic run once.
A deliberate diagnostic stop is neither a native success nor a new native
mathematical failure. Large original arrays go only in large-arrays/ and
are indexed by raw-binary manifests. All scientific execution is Actions-only.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
BASE_NAME = "geometry_20261114_native_candidate_seeded_solve.py"
BASE_SHA = "afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7"
STOP = "VISIBLE_NATIVE_CORRECTION_CAPTURE_COMPLETE_V1"
VARIABLE = "VISIBLE_FLEX_NATIVE_CORRECTION_CAPTURE_SPEC"
ACTUAL25 = {
    "result.json": "f5f4acdb055c6964fd591ac2da566bc581607b1d32ebc8096af557f4a3f8abbf",
    "native_0001.json.gz": "b836abc69da476967d3b464462fed55f90f10a54d966dd7d1a1fc379f0a55ddc",
    "native_iteration.json.gz": "2e7edf5566f6cd80f7217d8e6a07d3c64d3f3a88050b8e11d782b5c8415d07a5",
    "native_trace.jsonl": "dd1ddbbc7c00911c354fe34baadad331b3145b7cfbdc0c151a08628522b21218",
    "native_trials.jsonl": "6bb65a50911bd095c70985bbbdaa321d21d495e808881f7cff05f5f682470f57",
    "seed-binding.json": "5a60e750c9fae905ee7351d94b66bfb7eb86944c264da05ed37ea1116589355e",
    "instrumentation.json": "9f0668f8e57765926362f1e6fd2a540a4a567e5b5f1186d9d77eecff85e3cdb9",
    "seeded-solve-spec.json": "054b584407917b2038df322751d5f17c5f03a90467a8d85332314bf0e625b923",
    "verified-launch-intent.json": "19f886ed5baf101ed4cc3b053b9d7a67645578ca1434fe5acd50ef9f81ed6cd5",
    "original-live-identity-before-seed.json": "de9bbf01981f1605c0342817ea520005bf2d0a05f5a755986d50b718b16089a7",
}


def load_base():
    path = HERE/BASE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest() != BASE_SHA:
        raise ValueError("The actual25 independent seed-binding source changed")
    spec = importlib.util.spec_from_file_location("frozen_native25_binding", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_actual25(a, B, prior, candidate, equal, numerical_configuration, numerical_sources):
    directory = a.native_failure_directory.resolve()
    inputs = {}
    for name, digest in ACTUAL25.items():
        path = directory/name
        if B.sha(path) != digest:
            raise ValueError("Use the original actual25 complete failure evidence: "+name)
        inputs[name] = B.described(path)
    result = B.read(directory/"result.json")
    response = B.read(directory/"native_0001.json.gz")
    iteration = B.read(directory/"native_iteration.json.gz")
    binding = B.read(directory/"seed-binding.json")
    old_spec = B.read(directory/"seeded-solve-spec.json")
    launch = B.read(directory/"verified-launch-intent.json")
    instrument = B.read(directory/"instrumentation.json")
    live = B.read(directory/"original-live-identity-before-seed.json")
    trace = [json.loads(line) for line in (directory/"native_trace.jsonl").read_text().splitlines()]
    trials = [json.loads(line) for line in (directory/"native_trials.jsonl").read_text().splitlines()]
    expected_error = "Error: multiple-shooting line search failed at 0.04177307820740199"
    if (result["success"] is not False or result["finished"] is not True
            or result["original_native_request_calls"] != 1
            or result["actual_failed"] != expected_error
            or response["response"]["failed"] != expected_error
            or result["actual_full_J_present"] is not False or result["actual_audit_present"] is not False):
        raise ValueError("Bind the real failed original correction, not an accepted native response")
    equal(response["request"], dict(height=prior["height"], jacobian=True, audit=True), "actual25 exact complete request")
    equal(numerical_configuration(response["config"]), prior["config"], "actual25 original numerical config")
    equal(numerical_sources(response["source_sha256"]), numerical_sources(prior["intent"]["source_sha256"]),
          "actual25 original numerical sources")
    for key in ("parameters", "states", "rawNode", "rawStates", "cutHeight"):
        equal(response["response"]["checkpoint"][key], iteration["checkpoint"][key], "actual25 checkpoint "+key)
    cp = response["response"]["checkpoint"]
    equal(cp["cutHeight"], prior["height"], "actual25 unchanged H")
    equal(cp["rawNode"], prior["checkpoint"]["rawNode"], "actual25 raw nodes")
    equal(cp["rawStates"], [cp["states"][j] for j in cp["rawNode"]], "actual25 raw-state layout")
    original_rows = []
    for descriptor in candidate["state_chunks"]:
        original_rows.extend(B.read(descriptor["path"])["rows"])
    equal(cp["states"], [row["state"] for row in original_rows], "actual25 no accepted state update (real-value equality)")
    equal(binding["candidate_states_float64le_sha256"], B.CANDIDATE_BITS_SHA, "actual25 full signed-zero seed")
    equal(binding["height_float64le_sha256"], B.HEIGHT_BITS_SHA, "actual25 H bytes")
    equal(binding["original_scales_float64le_sha256"], B.SCALES_BITS_SHA, "actual25 original scales")
    equal(live, candidate["records"]["v3_original_live_identity"], "actual25 unchanged original methods/layout")
    equal(launch["spec_sha256"], ACTUAL25["seeded-solve-spec.json"], "actual25 launch/spec")
    equal(old_spec["candidate_states_float64le_sha256"], B.CANDIDATE_BITS_SHA, "actual25 specification state bytes")
    if instrument["exact_insertion_roundtrip_verified"] is not True:
        raise ValueError("The actual25 source insertion identity is missing")
    assignments = [row for row in trace if row.get("event") == "actual23_complete_candidate_initial_assignment"]
    if len(assignments) != 1 or len(trials) != 10:
        raise ValueError("Keep the actual25 complete first-assignment/ten-trial evidence")
    for j, row in enumerate(trials):
        if (row["iteration"] != 0 or row["trial"] != j or row["step"] != 2.**(-j)
                or row["kind"] != "momentum-guard-rejection" or row["stage"] != 13
                or row["rawCell"] != 0 or row["rawSegment"] != 7):
            raise ValueError("The actual25 observed correction failure differs")
    return dict(inputs=inputs, original_last_iteration=result["actual_last_iteration"],
        original_trace_events=len(trace), original_trials=len(trials),
        original_error=expected_error, original_native_full_DN_J_and_audit_returned=False)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("Run this original native capture only in this public repository Actions")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("failed-directory", "cold-probe-summary", "first-candidate-summary", "v2-candidate-summary",
                 "candidate-directory", "native-failure-directory", "source-topic", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--node-heap", type=int, default=6144)
    a = parser.parse_args()
    a.out = a.out.resolve(); a.out.mkdir(parents=True, exist_ok=True)
    if any(a.out.iterdir()):
        raise ValueError("Use an empty native-correction-capture output directory")
    B = load_base()
    history = B.load_frozen_history()
    frozen = dict(history.PINNED_SOURCES, **{
        B.HISTORY_SOURCE:B.HISTORY_SHA,
        "geometry_20261114_zero_rk_native_probe_v3_hook.mjs":B.V3_HOOK_SHA,
        BASE_NAME:BASE_SHA,
        "geometry_20261114_native_candidate_seeded_solve_hook.mjs":
            "22fa88aaaf2385a34dc3a373138f1b7fec08c903fd7151717b1f3dfb4d707e8d",
        "tail_resumable_engine.mjs":"1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8"})
    for name, digest in frozen.items():
        if B.sha(HERE/name) != digest:
            raise ValueError("A frozen original or provenance source changed: "+name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original
    def equal(x,y,label):
        if not same(x,y): raise ValueError("Native correction capture identity differs: "+label)
    prior = B.validate_history(a, history, equal, numerical_configuration)
    candidate = B.validate_candidate(a, prior, equal, numerical_configuration, numerical_sources)
    actual25 = validate_actual25(a, B, prior, candidate, equal, numerical_configuration, numerical_sources)
    config_path = a.out/"capture-input-config.json"
    original.write(config_path, prior["config"])
    hook = HERE/"geometry_20261114_native_correction_capture_hook.mjs"
    request = dict(height=prior["height"],jacobian=True,audit=True)
    spec = dict(schema="native-first-correction-capture-spec-v1", original_public_run="43598917532",
        cold_baseline_public_run="43602823170",first_candidate_public_run="43603818345",
        v2_candidate_public_run="43604874829",completed_probe_public_run="43605912092",
        original_native_failure_public_run="43607404925",actual25=actual25,
        source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),frozen_sources=frozen,
        inputs=prior["inputs"],candidate_state_chunks=candidate["state_chunks"],
        original_graph_scale_chunks=candidate["graph_chunks"],
        original_source_sha256=prior["intent"]["source_sha256"],
        numerical_configuration=prior["config"],numerical_parameters=candidate["summary"]["numerical_parameters"],
        io_keys=sorted(IO_KEYS),output=str(a.out),fresh_request=request,
        original_native_solve_tolerance=prior["config"]["solveTolerance"],
        candidate_states_float64le_sha256=B.CANDIDATE_BITS_SHA,exact_height_float64le_sha256=B.HEIGHT_BITS_SHA,
        original_scales_float64le_sha256=B.SCALES_BITS_SHA,original_far_graph_float64le_sha256=B.FAR_BITS_SHA,
        restored_negative_zero_count=candidate["restored_negative_zeros"],
        planned_stop=STOP,planned_stop_after_original_first_correction=True,
        no_original_trial_repetition=True,no_final_DN_J_or_audit_acceptance=True,
        large_array_directory="large-arrays",large_arrays_artifact_only=True,
        original_numerical_arithmetic_before_stop_unchanged=True,task_completed=False)
    spec_path=a.out/"capture-spec.json"; B.write(spec_path,spec)
    previous=os.environ.get(VARIABLE);os.environ[VARIABLE]=str(spec_path)
    popen=original.subprocess.Popen;commands=[];client=None
    started=time.monotonic()
    result=dict(schema="native-first-correction-capture-result-v1",diagnostic_complete=False,
        native_accepted=False,task_completed=False,source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        spec_sha256=B.sha(spec_path),inputs=prior["inputs"],actual25=actual25,
        planned_stop=STOP,no_final_DN_J_or_audit_acceptance=True,large_arrays_artifact_only=True)
    def observed_popen(command,*args,**kwargs):
        worker=str(HERE/"tail_frozen_worker.mjs")
        if not isinstance(command,list) or worker not in command:return popen(command,*args,**kwargs)
        if len(command)!=8 or command[0]!="node" or command[4]!="--import" or command[6]!=worker:
            raise ValueError("Instrument only the original true-client worker")
        actual=list(command[:6])+["--import",str(hook)]+list(command[6:]);commands.append(actual)
        return popen(actual,*args,**kwargs)
    expected_stop=False
    try:
        original.subprocess.Popen=observed_popen
        try:client=original.TailClient(config_path,a.source_topic.resolve()/"repro/source-root",a.out/"native",node_heap=a.node_heap)
        finally:original.subprocess.Popen=popen
        equal(numerical_configuration(client._configuration),prior["config"],"current mathematical config")
        equal(numerical_sources(client.sources),numerical_sources(prior["intent"]["source_sha256"]),"current original sources")
        equal(ready_semantics(client.ready),ready_semantics(prior["ready"]),"current original ready")
        capacity=original.read(client.capacity_record)
        for key in ("name","capacity","requestedCapacity","nodeVersion","adapterSHA256","originalConstructorCapacity","numericalChange","retained","files"):
            equal(capacity[key],prior["capacity"][key],"current capacity "+key)
        if len(commands)!=1 or client.calls!=0 or client.cache_key is not None:
            raise ValueError("Use one fresh original worker and no imported response cache")
        B.write(a.out/"verified-launch-intent.json",dict(
            schema="native-first-correction-capture-verified-launch-v1",spec_sha256=B.sha(spec_path),
            hook_sha256=B.sha(hook),source_sha256=B.sha(__file__),actual_command=commands[0],
            current_sources=client.sources,current_capacity_sha256=B.sha(client.capacity_record),
            complete_current_ready_sha256=B.sha(a.out/"native_ready.json.gz"),
            identity_verified_before_request=True,initial_native_solve_calls=0,initial_response_cache_empty=True,
            inputs=prior["inputs"],actual25=actual25,request=request))
        print(json.dumps(dict(event="native-first-correction-capture-identities-verified",modes=112,
            candidate_sha256=B.CANDIDATE_BITS_SHA,planned_stop_before_trials=True)),flush=True)
        try:
            client.solve(prior["height"],jacobian=True,audit=True)
            result["unexpected_original_response_returned"]=True
        except FloatingPointError as error:
            result["original_client_exception"]=repr(error)
            record_path=a.out/"native_0001.json.gz"
            if record_path.is_file():
                response=original.read(record_path)
                expected_stop=response["response"].get("failed")=="Error: "+STOP
                result["actual_original_failure_message"]=response["response"].get("failed")
            if not expected_stop:raise
    except Exception as error:
        result["unexpected_error"]=repr(error)
    finally:
        original.subprocess.Popen=popen
        if client is not None:
            client.close();result["original_native_requests"]=client.calls
            result["worker_exit_code"]=client.proc.poll() if client.proc else None
        if previous is None:os.environ.pop(VARIABLE,None)
        else:os.environ[VARIABLE]=previous
        trial_file=a.out/"native_trials.jsonl"
        trial_count=sum(bool(x.strip()) for x in trial_file.read_text().splitlines()) if trial_file.is_file() else 0
        result["trials_executed"]=trial_count
        result["planned_diagnostic_stop_observed"]=expected_stop
        summary_path=a.out/"capture-summary.json"
        if summary_path.is_file():
            summary=B.read(summary_path)
            result["capture_summary_sha256"]=B.sha(summary_path)
            result["capture_phase"]=summary.get("phase")
            result["linear_defect_summary"]=summary.get("linear_defect_summary")
            result["maximum_chart_summary"]=summary.get("maximum_chart_summary")
            result["diagnostic_complete"]=(expected_stop and summary.get("capture_completed") is True
                and result.get("worker_exit_code")==0 and result.get("original_native_requests")==1 and trial_count==0)
        result["diagnostic_exit_kind"]=("planned-capture-complete" if result["diagnostic_complete"]
            else "unexpected-original-failure-or-partial-capture")
        result["elapsed_seconds"]=time.monotonic()-started
        result["small_output_files"]=[dict(file=p.name,sha256=B.sha(p),bytes=p.stat().st_size)
            for p in sorted(a.out.iterdir()) if p.is_file() and p.name!="result.json"]
        B.write(a.out/"result.json",result)
    print(json.dumps(dict(event="native-first-correction-capture-finished",
        diagnostic_complete=result["diagnostic_complete"],planned_stop=expected_stop,
        trials=trial_count,native_accepted=False,task_completed=False)),flush=True)
    return 0 if result["diagnostic_complete"] else 2

if __name__=="__main__":raise SystemExit(main())
