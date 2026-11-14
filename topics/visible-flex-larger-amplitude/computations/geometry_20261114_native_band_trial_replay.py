#!/usr/bin/env python3
"""Replay one unchanged original native line search with a saved full band direction.

The actual28 original withJac baseline is explicitly CACHED, not recomputed.
Every trial uses the original no-J evaluate, original ten alphas, guards and
strict merit decrease. The first baseline/J and correction are reused; no
original J is rebuilt. Stop after this one line search, preserving an actual
selected state if any. A selected trial is not a complete native/J/audit result.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import struct
import time

HERE=Path(__file__).resolve().parent
BASE_NAME="geometry_20261114_native_candidate_seeded_solve.py"
BASE_SHA="afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7"
BAND_NAME="geometry_20261114_native_captured_band_correction.py"
BAND_SHA="b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390"
CAPTURE_PY_SHA="0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0"
CAPTURE_HOOK_SHA="b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30"
CAPTURE_RESULT_SHA="ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7"
CAPTURE_SUMMARY_SHA="48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1"
CAPTURE_MANIFEST_SHA="3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3"
CORE_SHA="ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3"
VARIABLE="VISIBLE_FLEX_NATIVE_BAND_TRIAL_REPLAY_SPEC"
STOP="VISIBLE_NATIVE_BAND_TRIAL_REPLAY_ACCEPTED_STOP_V1"


def load_base():
    path=HERE/BASE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest()!=BASE_SHA:
        raise ValueError("Frozen actual23/25 history binding source changed")
    spec=importlib.util.spec_from_file_location("frozen_native_trial_seed_history",path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def child(directory,name):
    if not isinstance(name,str) or not name or Path(name).name!=name:
        raise ValueError("A bounded evidence filename is required")
    path=(directory/name).resolve()
    if not path.is_relative_to(directory.resolve()) or not path.is_file():
        raise ValueError("Missing or escaping evidence file: "+name)
    return path


def record_file(B,directory,descriptor):
    path=child(directory,descriptor["file"])
    if B.sha(path)!=descriptor["sha256"] or path.stat().st_size!=descriptor["bytes"]:
        raise ValueError("Changed bounded evidence: "+descriptor["file"])
    return B.read(path),B.described(path)


def validate_capture(a,B,prior,candidate,equal,numerical_sources):
    directory=a.capture_directory.resolve();result_path=directory/"result.json"
    if B.sha(result_path)!=CAPTURE_RESULT_SHA:raise ValueError("Use actual28's completed original capture")
    result=B.read(result_path)
    if (result.get("diagnostic_complete") is not True or result.get("native_accepted") is not False
            or result.get("planned_diagnostic_stop_observed") is not True
            or result.get("trials_executed")!=0 or result.get("original_native_requests")!=1):
        raise ValueError("The original baseline must come from the completed actual28 capture")
    equal(result["source_sha256"],CAPTURE_PY_SHA,"actual28 source")
    equal(result["hook_sha256"],CAPTURE_HOOK_SHA,"actual28 hook")
    listed={row["file"]:row for row in result["small_output_files"]}
    names=("capture-summary.json","capture-manifest.json","capture-begin.json","capture-spec.json",
           "core-instrumentation.json","seed-binding.json","original-live-identity-before-seed.json")
    records={"result":result};inputs={"result":B.described(result_path)}
    for name in names:
        value,descriptor=record_file(B,directory,listed[name])
        key=name.removesuffix(".json").replace("-","_")
        records[key]=value;inputs[key]=descriptor
    summary=records["capture_summary"];manifest=records["capture_manifest"]
    begin=records["capture_begin"];spec=records["capture_spec"];core=records["core_instrumentation"]
    equal(inputs["capture_summary"]["sha256"],CAPTURE_SUMMARY_SHA,"actual28 summary bytes")
    equal(inputs["capture_manifest"]["sha256"],CAPTURE_MANIFEST_SHA,"actual28 original-array manifest bytes")
    equal(inputs["capture_spec"]["sha256"],result["spec_sha256"],"actual28 original specification bytes")
    equal(core["original_core_file_sha256"],CORE_SHA,"actual28 original mathematical core")
    equal(core["exact_insertion_roundtrip_verified"],True,"actual28 core source roundtrip")
    equal(spec["fresh_request"],dict(height=prior["height"],jacobian=True,audit=True),"actual28 same full physical H")
    equal(spec["numerical_configuration"],prior["config"],"same original mathematical configuration")
    equal(numerical_sources(spec["original_source_sha256"]),numerical_sources(prior["intent"]["source_sha256"]),
          "same original consumed source identities")
    equal(records["original_live_identity_before_seed"],candidate["records"]["v3_original_live_identity"],
          "same original methods/graphs/gains/stage layout")
    equal(begin["original_evaluate_completed"],True,"actual28 complete original withJac")
    equal(begin["all_original_withJac_stage_guards_returned"],True,"actual28 returned original stage guards")
    equal((begin["M"],begin["K"],begin["depth"]),(112,224,576),"same complete finite native layout")
    arrays={row["name"]:row for row in manifest["arrays"]}
    for name,digest in (("base-states",B.CANDIDATE_BITS_SHA),("physical-height",B.HEIGHT_BITS_SHA),
                        ("original-scales",B.SCALES_BITS_SHA),("original-far-graph",B.FAR_BITS_SHA)):
        equal(arrays[name]["raw_sha256"],digest,"actual28 original binary identity "+name)
    for name in ("original_norm","original_minA","original_minD"):
        record=summary[name];value=record["value"]
        if not isinstance(value,(int,float)) or not math.isfinite(value):
            raise ValueError("The retained original baseline record is not finite")
        equal(struct.pack("<d",float(value)).hex(),record["float64le_hex"],"retained baseline bits "+name)
        equal(record,begin[name],"actual28 begin/finish baseline "+name)
    equal(summary["capture_completed"],True,"actual28 captured correction completed")
    return dict(inputs=inputs,array_sha256={name:row["raw_sha256"] for name,row in arrays.items()},
        baseline=dict(norm=summary["original_norm"],minA=summary["original_minA"],minD=summary["original_minD"]),
        original_runtime_core_sha256=core["original_runtime_core_sha256"],
        captured_baseline_reused=True,new_baseline_evaluations=0,new_J_evaluations=0)


def validate_band(a,B,capture,equal):
    directory=a.band_directory.resolve();path=directory/"result.json"
    if not re.fullmatch(r"[0-9a-f]{64}",a.band_result_sha256) or B.sha(path)!=a.band_result_sha256:
        raise ValueError("An explicitly pinned actual completed band result is required")
    result=B.read(path)
    if (result.get("schema")!="original-captured-native-full-band-correction-v1"
            or result.get("diagnostic_completed") is not True or result.get("linear_direction_computed") is not True
            or result.get("native_accepted") is not False or result.get("new_J_calls")!=0
            or result.get("original_native_calls")!=0 or result.get("nonlinear_trials")!=0
            or result.get("lapack_factor_info")!=0 or result.get("lapack_solve_info")!=0):
        raise ValueError("Use a complete finite band direction; it is not a native accepted response")
    equal(result["source_sha256"],a.band_source_sha256,"explicit complete direction producer source")
    equal(result["capture_result_sha256"],CAPTURE_RESULT_SHA,"same actual28 linear model")
    equal((result["M"],result["K"],result["depth"],result["dimension"]),(112,224,576,129248),"all band coordinates")
    checkpoint,checkpoint_file=record_file(B,directory,result["direction_checkpoint"])
    array_manifest,array_manifest_file=record_file(B,directory,result["array_manifest"])
    if checkpoint.get("schema")!="complete-original-native-band-direction-v1":raise ValueError("Full direction schema required")
    equal(checkpoint["source_sha256"],a.band_source_sha256,"direction source")
    equal(checkpoint["native_accepted"],False,"direction is not accepted native")
    equal(checkpoint["scaling"],result["scaling"],"recorded actual linear scaling")
    binding=checkpoint["input_binding"]
    equal(binding["capture_result_sha256"],CAPTURE_RESULT_SHA,"direction actual28 result")
    equal(binding["capture_summary_sha256"],CAPTURE_SUMMARY_SHA,"direction actual28 summary")
    equal(binding["capture_manifest_sha256"],CAPTURE_MANIFEST_SHA,"direction actual28 manifest")
    equal(binding["raw_array_sha256"],capture["array_sha256"],"direction complete original-array identity")
    equal(binding["original_core_sha256"],CORE_SHA,"direction original mathematical core")
    equal((checkpoint["M"],checkpoint["K"],checkpoint["depth"]),(112,224,576),"complete direction layout")
    rows=checkpoint["rows"]
    if len(rows)!=577:raise ValueError("Every original native direction node is required")
    delta=[];negative_zeros=0
    for node,row in enumerate(rows):
        if row["node"]!=node or len(row["state"])!=224:
            raise ValueError("Full ordered direction node required")
        if any(type(x) not in (int,float) or not math.isfinite(x) for x in row["state"]):
            raise ValueError("Every saved direction coefficient must be finite")
        values=[float(x) for x in row["state"]];seen=set()
        for column in row["negative_zero_columns"]:
            if type(column) is not int or not 0<=column<224 or column in seen or values[column]!=0:
                raise ValueError("Valid distinct signed-zero columns required")
            seen.add(column);values[column]=-0.;negative_zeros+=1
        delta.append(values)
    digest=B.binary_rows_hash(delta)
    equal(digest,checkpoint["delta_float64le_sha256"],"complete restored direction bytes")
    equal(digest,result["new_delta"]["sha256"],"actual band original-coordinate direction bytes")
    entry=next(row for row in array_manifest["arrays"] if row["name"]=="complete-original-coordinate-delta")
    equal(entry,result["new_delta"],"retained original-coordinate direction manifest entry")
    equal(entry["shape"],[577,224],"all restored direction rows and columns")
    equal(entry["finite"],129248,"all actual direction entries finite")
    equal(entry["negative_zero"],negative_zeros,"complete direction negative-zero sidecar")
    return dict(inputs=dict(result=B.described(path),direction_checkpoint=checkpoint_file,array_manifest=array_manifest_file),
        source_file=a.band_source_file,source_sha256=a.band_source_sha256,result_sha256=a.band_result_sha256,delta_float64le_sha256=digest,
        restored_negative_zero_count=negative_zeros,scaling=result["scaling"],
        mathematical_equations_and_original_scales_reused=True,
        linear_defect_diagnostics=result["linear_defects"],
        exact_original_worst_row=result["exact_original_captured_worst_row"],
        exact_new_worst_row=result["exact_new_floating_worst_row"],
        new_native_acceptance_not_claimed=True)


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
            os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public"):
        raise RuntimeError("Native trial computations belong only to this public repository Actions")
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("failed-directory","cold-probe-summary","first-candidate-summary","v2-candidate-summary",
                 "candidate-directory","capture-directory","band-directory","source-topic","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--band-result-sha256",required=True)
    parser.add_argument("--band-source-file",default=BAND_NAME)
    parser.add_argument("--band-source-sha256",default=BAND_SHA)
    parser.add_argument("--node-heap",type=int,default=6144)
    a=parser.parse_args();a.out=a.out.resolve();a.out.mkdir(parents=True,exist_ok=True)
    if any(a.out.iterdir()):raise ValueError("Use an empty independent trial replay output directory")
    if (Path(a.band_source_file).name!=a.band_source_file or
            not re.fullmatch(r"[0-9a-f]{64}",a.band_source_sha256)):
        raise ValueError("Explicit direction producer filename and SHA256 required")
    B=load_base();history=B.load_frozen_history()
    frozen=dict(history.PINNED_SOURCES,**{B.HISTORY_SOURCE:B.HISTORY_SHA,
        "geometry_20261114_zero_rk_native_probe_v3_hook.mjs":B.V3_HOOK_SHA,
        BASE_NAME:BASE_SHA,a.band_source_file:a.band_source_sha256,
        "tail_resumable_engine.mjs":"1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8"})
    for name,digest in frozen.items():
        if B.sha(HERE/name)!=digest:raise ValueError("Frozen original/provenance source changed: "+name)
    from exact_20261114_seeded_zero_tail_client import same,numerical_configuration,numerical_sources,ready_semantics,IO_KEYS
    import exact_20261114_true_tail_client as original
    def equal(left,right,label):
        if not same(left,right):raise ValueError("Trial replay identity differs: "+label)
    prior=B.validate_history(a,history,equal,numerical_configuration)
    candidate=B.validate_candidate(a,prior,equal,numerical_configuration,numerical_sources)
    capture=validate_capture(a,B,prior,candidate,equal,numerical_sources)
    band=validate_band(a,B,capture,equal)
    config_path=a.out/"trial-input-config.json";original.write(config_path,prior["config"])
    hook=HERE/"geometry_20261114_native_band_trial_replay_hook.mjs"
    request=dict(height=prior["height"],jacobian=True,audit=True)
    spec=dict(schema="original-native-band-trial-replay-spec-v1",source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        frozen_sources=frozen,inputs=prior["inputs"],capture=capture,band=band,
        original_public_run="43598917532",cold_baseline_public_run="43602823170",
        first_candidate_public_run="43603818345",v2_candidate_public_run="43604874829",
        completed_probe_public_run="43605912092",captured_baseline_public_run="43611175099",
        candidate_state_chunks=candidate["state_chunks"],original_graph_scale_chunks=candidate["graph_chunks"],
        candidate_states_float64le_sha256=B.CANDIDATE_BITS_SHA,exact_height_float64le_sha256=B.HEIGHT_BITS_SHA,
        original_scales_float64le_sha256=B.SCALES_BITS_SHA,original_far_graph_float64le_sha256=B.FAR_BITS_SHA,
        restored_negative_zero_count=candidate["restored_negative_zeros"],
        original_source_sha256=prior["intent"]["source_sha256"],numerical_configuration=prior["config"],
        numerical_parameters=candidate["summary"]["numerical_parameters"],io_keys=sorted(IO_KEYS),
        output=str(a.out),fresh_request=request,planned_accepted_trial_stop=STOP,
        original_native_solve_tolerance=prior["config"]["solveTolerance"],
        original_baseline_is_cached_from_actual28=True,new_baseline_evaluations=0,new_J_evaluations=0,
        original_trial_loop_and_guard_and_merit_retained=True,
        no_H_change=True,no_native_acceptance=True,task_completed=False)
    spec_path=a.out/"trial-replay-spec.json";B.write(spec_path,spec)
    previous=os.environ.get(VARIABLE);os.environ[VARIABLE]=str(spec_path)
    popen=original.subprocess.Popen;commands=[];client=None
    started=time.monotonic()
    result=dict(schema="original-native-band-trial-replay-result-v1",replay_completed=False,trial_accepted=False,
        native_accepted=False,task_completed=False,source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        spec_sha256=B.sha(spec_path),band_result_sha256=a.band_result_sha256,
        capture_result_sha256=CAPTURE_RESULT_SHA,cached_withJac_baseline=capture["baseline"],
        original_baseline_is_cached_from_actual28=True,new_baseline_evaluations=0,new_J_evaluations=0)
    def observed_popen(command,*args,**kwargs):
        worker=str(HERE/"tail_frozen_worker.mjs")
        if not isinstance(command,list) or worker not in command:return popen(command,*args,**kwargs)
        if len(command)!=8 or command[0]!="node" or command[4]!="--import" or command[6]!=worker:
            raise ValueError("Instrument only the original native worker launch")
        actual=list(command[:6])+["--import",str(hook)]+list(command[6:]);commands.append(actual)
        return popen(actual,*args,**kwargs)
    try:
        original.subprocess.Popen=observed_popen
        try:client=original.TailClient(config_path,a.source_topic.resolve()/"repro/source-root",a.out/"native",node_heap=a.node_heap)
        finally:original.subprocess.Popen=popen
        equal(numerical_configuration(client._configuration),prior["config"],"current original mathematical config")
        equal(numerical_sources(client.sources),numerical_sources(prior["intent"]["source_sha256"]),"current original sources")
        equal(ready_semantics(client.ready),ready_semantics(prior["ready"]),"current original ready")
        capacity=original.read(client.capacity_record)
        for key in ("name","capacity","requestedCapacity","nodeVersion","adapterSHA256","originalConstructorCapacity","numericalChange","retained","files"):
            equal(capacity[key],prior["capacity"][key],"current original capacity "+key)
        if len(commands)!=1 or client.calls!=0 or client.cache_key is not None:
            raise ValueError("Use one fresh worker with no completed-response cache")
        B.write(a.out/"verified-launch-intent.json",dict(schema="original-native-band-trial-replay-verified-launch-v1",
            spec_sha256=B.sha(spec_path),hook_sha256=B.sha(hook),source_sha256=B.sha(__file__),actual_command=commands[0],
            current_sources=client.sources,current_capacity_sha256=B.sha(client.capacity_record),
            complete_current_ready_sha256=B.sha(a.out/"native_ready.json.gz"),
            identity_verified_before_request=True,initial_native_solve_calls=0,initial_response_cache_empty=True,
            inputs=prior["inputs"],capture_inputs=capture["inputs"],band_inputs=band["inputs"],request=request))
        print(json.dumps(dict(event="original-native-band-trial-replay-identities-verified",modes=112,
            cached_baseline=True,new_baseline_evaluations=0,new_J_evaluations=0,
            band_delta_sha256=band["delta_float64le_sha256"])),flush=True)
        try:
            client.solve(prior["height"],jacobian=True,audit=True)
            result["unexpected_complete_native_response_returned"]=True
        except FloatingPointError as error:
            result["original_client_exception"]=repr(error)
            # The original client truthfully rejects both the intentional stop
            # and an exhausted original line search. Neither is a solved DN.
            path=a.out/"native_0001.json.gz"
            if path.is_file():result["actual_original_failure_message"]=original.read(path)["response"].get("failed")
            else:raise
    except Exception as error:
        result["unexpected_error"]=repr(error)
    finally:
        original.subprocess.Popen=popen
        if client is not None:
            client.close();result["original_native_requests"]=client.calls
            result["worker_exit_code"]=client.proc.poll() if client.proc else None
        if previous is None:os.environ.pop(VARIABLE,None)
        else:os.environ[VARIABLE]=previous
        summary_path=a.out/"trial-replay-summary.json"
        if summary_path.is_file():
            summary=B.read(summary_path)
            result["trial_replay_summary_sha256"]=B.sha(summary_path)
            result["observed_trials"]=summary.get("trials")
            result["selected_state"]=summary.get("selected_state")
            result["fresh_original_no_J_trial_evaluations"]=summary.get("original_no_J_trial_evaluations")
            expected=("Error: "+STOP if summary.get("trial_accepted") else summary.get("expected_original_failure"))
            complete=(summary.get("replay_completed") is True and result.get("actual_original_failure_message")==expected
                and result.get("worker_exit_code")==0 and result.get("original_native_requests")==1)
            result["replay_completed"]=complete
            result["trial_accepted"]=bool(complete and summary.get("trial_accepted") is True)
        result["elapsed_seconds"]=time.monotonic()-started
        result["small_output_files"]=[dict(file=p.name,bytes=p.stat().st_size,sha256=B.sha(p))
            for p in sorted(a.out.iterdir()) if p.is_file() and p.name!="result.json"]
        B.write(a.out/"result.json",result)
    print(json.dumps(dict(event="original-native-band-trial-replay-finished",replay_completed=result["replay_completed"],
        trial_accepted=result["trial_accepted"],native_accepted=False,task_completed=False)),flush=True)
    return 0 if result["replay_completed"] and result["trial_accepted"] else 2

if __name__=="__main__":raise SystemExit(main())
