#!/usr/bin/env python3
"""Replay the unchanged original ten-alpha native loop with one complete original576 R273 direction.

The direction targets actual28's original576 saved J/r/cut/far/sigma/H and
base, not the1372 system or a restriction of its direction. The complete
577-node direction includes the soft cut/far rows unchanged. Eta/L2/exact
readback are producer diagnostics, not extra nonlinear acceptance gates.
The original actual28 withJac baseline is explicitly cached; no new baseline
or J is evaluated. Every actual original noJ trial input and complete returned
residuals are observed read-only, including rejected candidates and signed zero.
Stop after the original first line search, retaining any actually selected
state; a selected trial is not a complete native/J/audit response.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import struct
import sys
import time

HERE=Path(__file__).resolve().parent
BASE_NAME="geometry_20261114_native_candidate_seeded_solve.py"
BASE_SHA="afa2588db686ba54b3e434e0ddf40503a74061ecd5fa389dbb41ced7a0b085c7"
DIRECTION_NAME="exact_20261114_original576_damped_chain_qr.py"
DIRECTION_SHA="e1a35bd82433cfe6525047cb3ceb3d0c434c1ebaa62680cb0f1fdab0e76cfaec"
DIRECTION_MODEL_SCOPE="R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
EXACT_KERNEL_SHA="0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
NATIVE_ADAPTER_NAME="exact_20261114_original576_damped_system.py"
NATIVE_ADAPTER_SHA="c78dfc6a5ef64a9de8bbbc857a927c6cd1078bbfb2281be62be4eb942014b207"
NATIVE_FROZEN={
    DIRECTION_NAME:DIRECTION_SHA,NATIVE_ADAPTER_NAME:NATIVE_ADAPTER_SHA,
    "exact_20261114_native_damped_chain_qr.py":"9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
    "exact_20261114_native_allrows_dyadic_residual.py":EXACT_KERNEL_SHA,
    "geometry_20261114_native_band_trial_replay.py":"e357426aa6e81cbab526ea74f7f9fd3e1fd69d917000dd7f9847972745823b80",
    "geometry_20261114_native_band_trial_replay_hook.mjs":"31c9bda7775322e9cc487903f842d755bf1c82d9102a434096ce5683791123fd"}
CAPTURE_PY_SHA="0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0"
CAPTURE_HOOK_SHA="b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30"
CAPTURE_RESULT_SHA="ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7"
CAPTURE_SUMMARY_SHA="48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1"
CAPTURE_MANIFEST_SHA="3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3"
CORE_SHA="ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3"
VARIABLE="VISIBLE_FLEX_NATIVE_ORIGINAL576_DAMPED_TRIAL_REPLAY_SPEC"
STOP="VISIBLE_NATIVE_ORIGINAL576_DAMPED_TRIAL_REPLAY_ACCEPTED_STOP_V1"


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


def validate_direction(a,B,capture,equal):
    """Bind the actual complete original576 direction; no 1372 restriction."""
    directory=a.direction_directory.resolve()
    if not re.fullmatch(r"[0-9a-f]{64}",a.direction_result_sha256):
        raise ValueError("Explicit actual original576 direction result SHA256 required")
    equal(a.direction_source_file,DIRECTION_NAME,"frozen actual original576 producer filename")
    equal(a.direction_source_sha256,DIRECTION_SHA,"frozen actual original576 producer source")
    for name,digest in NATIVE_FROZEN.items():
        equal(B.sha(HERE/name),digest,"frozen original576 provenance "+name)
    module_name="_original576_trial_complete_saved_array_identity"
    mspec=importlib.util.spec_from_file_location(module_name,HERE/NATIVE_ADAPTER_NAME)
    S=importlib.util.module_from_spec(mspec);sys.modules[module_name]=S;mspec.loader.exec_module(S)
    system=S.Original576System(a.capture_directory)
    binding=system.binding;original=binding["original_capture_binding"]
    for key,value in (("capture_result_sha256",CAPTURE_RESULT_SHA),
        ("capture_summary_sha256",CAPTURE_SUMMARY_SHA),("capture_manifest_sha256",CAPTURE_MANIFEST_SHA),
        ("original_core_sha256",CORE_SHA),("raw_array_sha256",capture["array_sha256"])):
        equal(original[key],value,"same complete original28 input "+key)
    for key,value in dict(schema="actual28-original576-complete-linear-system-binding-v1",
        adapter_source_sha256=NATIVE_ADAPTER_SHA,original_capture_result_sha256=CAPTURE_RESULT_SHA,
        modes=112,shape_dimension=224,original_depth=576,depth=576,node_count=577,
        old_to_new=list(range(577))).items():
        equal(binding[key],value,"complete actual original576 binding "+key)
    path=directory/"result.json.gz"
    equal(B.sha(path),a.direction_result_sha256,"actual original576 result bytes")
    result=B.read(path)
    for key,value in dict(schema="complete-native-original576-damped-square-root-direction-v1",
        source_sha256=DIRECTION_SHA,system_source_sha256=NATIVE_ADAPTER_SHA,
        factor_engine_source_sha256="9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
        kernel_source_sha256=EXACT_KERNEL_SHA,model_scope=DIRECTION_MODEL_SCOPE,
        diagnostic_completed=True,linear_direction_computed=True,native_accepted=False,task_completed=False,
        original_native_calls=0,new_RHS_calls=0,new_J_calls=0,new_ODE_steps=0,nonlinear_trials=0).items():
        equal(result.get(key),value,"actual complete original576 R273 direction "+key)
    if result.get("actual_error"):raise ValueError("Only a completed actual finite direction can be replayed")
    eta=result["eta_binary64"];value=eta.get("value")
    if type(value) not in (int,float) or not math.isfinite(value) or value<=0 or not isinstance(result["eta_cli_text"],str):
        raise ValueError("Bind the producer's explicit positive finite eta")
    equal(struct.pack("<d",float(value)).hex(),eta["float64le_hex"],"actual eta bits")
    equal(struct.pack("<d",float(result["eta_cli_text"])).hex(),eta["float64le_hex"],"actual eta original CLI parse")
    equal(eta["classification"],"finite","actual eta scalar classification")
    for key,value in dict(complete=True,rows=129248,columns=129248,augmented_rows=258496,
        stage_count=576,node_count=577,block_width=224,node_penalty_blocks=577,pure_constant_rows=129248).items():
        equal(result["factor_summary"][key],value,"complete original576 QR inventory "+key)
    input_binding,input_file=record_file(B,directory,result["input_binding"])
    equal(input_binding,binding,"same original576 complete input object")
    matrix_sha=binding["new_matrix_identity_sha256"]
    equal(result["new_matrix_identity_sha256"],matrix_sha,"actual original576 matrix identity")
    packet,packet_file=record_file(B,directory,result["native_direction_checkpoint"])
    manifest,manifest_file=record_file(B,directory,result["array_manifest"])
    for key,value in dict(schema="complete-native-original576-damped-direction-arrays-v1",
        source_sha256=DIRECTION_SHA,new_matrix_identity_sha256=matrix_sha,
        factor_engine_source_sha256="9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
        all_arrays_artifact_only=True,native_accepted=False).items():
        equal(manifest[key],value,"actual original576 direction array inventory "+key)
    entries={}
    for entry in manifest["arrays"]:
        name=entry["name"];relative=Path(entry["file"])
        if name in entries or relative.is_absolute() or '..' in relative.parts:
            raise ValueError("Unique safe original576 array descriptors required")
        entries[name]=entry
    name="complete-original-coordinate-delta";entry=result["native_delta"]
    equal(entry,entries[name],"complete actual original576 direction array")
    relative=Path(entry["file"]);raw_path=(directory/relative).resolve()
    if not raw_path.is_relative_to(directory) or not raw_path.is_file():
        raise ValueError("Complete original576 direction payload is missing or escaping")
    equal(raw_path.stat().st_size,entry["bytes"],"complete original576 raw direction size")
    equal(B.sha(raw_path),entry["sha256"],"complete original576 raw direction bytes")
    for key,value in dict(schema="complete-native-original576-damped-direction-v1",
        source_sha256=DIRECTION_SHA,input_binding=binding,M=112,K=224,depth=576,
        system_source_sha256=NATIVE_ADAPTER_SHA,
        factor_engine_source_sha256="9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
        original_depth=576,old_to_new=list(range(577)),eta_binary64=eta,
        model_scope=DIRECTION_MODEL_SCOPE,native_accepted=False,task_completed=False).items():
        equal(packet[key],value,"complete original576 checkpoint "+key)
    if len(packet["rows"])!=577:raise ValueError("Retain all577 original direction rows")
    values=[];negative_zeros=0
    for node,row in enumerate(packet["rows"]):
        if row["node"]!=node or len(row["state"])!=224 or any(type(x) not in (int,float) or not math.isfinite(x) for x in row["state"]):
            raise ValueError("Complete finite ordered original-coordinate rows required")
        state=list(map(float,row["state"]));seen=set()
        for column in row["negative_zero_columns"]:
            if type(column) is not int or not 0<=column<224 or column in seen or state[column]!=0:
                raise ValueError("Distinct valid signed-zero sidecar required")
            state[column]=-0.;seen.add(column);negative_zeros+=1
        values.append(state)
    raw=raw_path.read_bytes();rebuilt=b"".join(struct.pack("<224d",*row) for row in values)
    equal(raw,rebuilt,"all original576 raw/checkpoint f64 bytes")
    digest=hashlib.sha256(raw).hexdigest()
    equal(digest,packet["delta_float64le_sha256"],"original576 checkpoint raw hash")
    equal(entry["shape"],[577,224],"complete original576 direction shape")
    equal(entry["finite"],129248,"complete finite original576 direction count")
    equal(entry["negative_zero"],negative_zeros,"complete original576 negative-zero count")
    return dict(inputs=dict(result=B.described(path),direction_checkpoint=packet_file,
        array_manifest=manifest_file,input_binding=input_file),
        source_file=DIRECTION_NAME,source_sha256=DIRECTION_SHA,
        native_adapter_source_sha256=NATIVE_ADAPTER_SHA,result_sha256=a.direction_result_sha256,
        raw_native_direction=B.described(raw_path),new_matrix_identity_sha256=matrix_sha,
        native_depth=576,old_to_new=list(range(577)),delta_float64le_sha256=digest,
        restored_negative_zero_count=negative_zeros,eta_cli_text=result["eta_cli_text"],
        eta_binary64=eta,model_scope=DIRECTION_MODEL_SCOPE,
        direction_is_complete_original576=True,direction_is_not_a_1372_restriction=True,
        original28_full_input_binding_reconstructed=True,
        target_is_actual28_saved_original576_J=True,new_J_or_RHS_or_ODE_or_QR_called=False,
        original_direction_cut_or_far_entries_modified=False,
        complete_direction_manifest_bound=True,only_complete_direction_payload_consumed=True,
        QR_factor_payloads_not_reloaded=True,model_L2_and_exact_defects_not_used_as_trial_gate=True,
        original576_exact_Newton_claimed=False,native_acceptance_not_claimed=True)


def write_specification(path,value):
    """Retain the complete metadata; all spec SHA fields bind stored gzip bytes."""
    raw=(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    packed=gzip.compress(raw,compresslevel=9,mtime=0)
    if len(packed)>=4_900_000:raise ValueError("Keep complete gzip metadata below the public5MB file limit")
    with path.open('xb') as stream:stream.write(packed)
    return dict(file=path.name,bytes=len(packed),sha256=hashlib.sha256(packed).hexdigest(),
        raw_bytes=len(raw),raw_sha256=hashlib.sha256(raw).hexdigest(),encoding='json-gzip')


def main():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
            os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public"):
        raise RuntimeError("Native trial computations belong only to this public repository Actions")
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("failed-directory","cold-probe-summary","first-candidate-summary","v2-candidate-summary",
                 "candidate-directory","capture-directory","direction-directory","source-topic","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--direction-result-sha256",required=True)
    parser.add_argument("--direction-source-file",default=DIRECTION_NAME)
    parser.add_argument("--direction-source-sha256",default=DIRECTION_SHA)
    parser.add_argument("--node-heap",type=int,default=6144)
    a=parser.parse_args();a.out=a.out.resolve()
    if any(a.out.is_relative_to(p.resolve()) for p in
           (a.capture_directory,a.direction_directory,a.candidate_directory,a.failed_directory)):
        raise ValueError("Keep the replay output independent of every immutable input directory")
    a.out.mkdir(parents=True,exist_ok=True)
    if any(a.out.iterdir()):raise ValueError("Use an empty independent trial replay output directory")
    if (Path(a.direction_source_file).name!=a.direction_source_file or
            not re.fullmatch(r"[0-9a-f]{64}",a.direction_source_sha256)):
        raise ValueError("Explicit direction producer filename and SHA256 required")
    B=load_base();history=B.load_frozen_history()
    frozen=dict(history.PINNED_SOURCES,**{B.HISTORY_SOURCE:B.HISTORY_SHA,
        "geometry_20261114_zero_rk_native_probe_v3_hook.mjs":B.V3_HOOK_SHA,
        BASE_NAME:BASE_SHA,a.direction_source_file:a.direction_source_sha256,
        "tail_resumable_engine.mjs":"1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8"})
    frozen.update(NATIVE_FROZEN)
    for name,digest in frozen.items():
        if B.sha(HERE/name)!=digest:raise ValueError("Frozen original/provenance source changed: "+name)
    from exact_20261114_seeded_zero_tail_client import same,numerical_configuration,numerical_sources,ready_semantics,IO_KEYS
    import exact_20261114_true_tail_client as original
    def equal(left,right,label):
        if not same(left,right):raise ValueError("Trial replay identity differs: "+label)
    prior=B.validate_history(a,history,equal,numerical_configuration)
    candidate=B.validate_candidate(a,prior,equal,numerical_configuration,numerical_sources)
    capture=validate_capture(a,B,prior,candidate,equal,numerical_sources)
    direction=validate_direction(a,B,capture,equal)
    config_path=a.out/"trial-input-config.json";original.write(config_path,prior["config"])
    hook=HERE/"geometry_20261114_native_original576_damped_trial_replay_hook.mjs"
    request=dict(height=prior["height"],jacobian=True,audit=True)
    spec=dict(schema="original-native576-damped-trial-replay-spec-v1",source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        frozen_sources=frozen,inputs=prior["inputs"],capture=capture,direction=direction,
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
        readonly_complete_actual_trial_state_and_residual_observers=True,
        actual_instrumented_evaluate_source_and_restored_original_reference_both_recorded=True,
        observer_does_not_form_candidates_or_change_original_evaluate_returns=True,
        no_H_change=True,no_native_acceptance=True,task_completed=False)
    spec_path=a.out/"trial-replay-spec.json.gz";specification=write_specification(spec_path,spec)
    previous=os.environ.get(VARIABLE);os.environ[VARIABLE]=str(spec_path)
    popen=original.subprocess.Popen;commands=[];client=None
    started=time.monotonic()
    result=dict(schema="original-native576-damped-trial-replay-result-v1",replay_completed=False,trial_accepted=False,
        native_accepted=False,task_completed=False,source_sha256=B.sha(__file__),hook_sha256=B.sha(hook),
        spec_sha256=B.sha(spec_path),specification=specification,direction_result_sha256=a.direction_result_sha256,
        direction_eta_cli_text=direction["eta_cli_text"],direction_eta_binary64=direction["eta_binary64"],
        direction_model_scope=direction["model_scope"],original_direction_cut_or_far_entries_modified=False,
        model_L2_and_exact_defect_not_used_as_trial_gate=True,
        new_matrix_identity_sha256=direction["new_matrix_identity_sha256"],
        target_is_actual28_saved_original576_J=True,direction_is_complete_original576=True,
        direction_is_not_a_1372_restriction=True,original576_exact_Newton_claimed=False,
        readonly_actual_trial_state_and_returned_residual_observation=True,
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
        B.write(a.out/"verified-launch-intent.json",dict(schema="original-native576-damped-trial-replay-verified-launch-v1",
            spec_sha256=B.sha(spec_path),hook_sha256=B.sha(hook),source_sha256=B.sha(__file__),actual_command=commands[0],
            current_sources=client.sources,current_capacity_sha256=B.sha(client.capacity_record),
            complete_current_ready_sha256=B.sha(a.out/"native_ready.json.gz"),
            identity_verified_before_request=True,initial_native_solve_calls=0,initial_response_cache_empty=True,
            inputs=prior["inputs"],capture_inputs=capture["inputs"],direction_inputs=direction["inputs"],request=request))
        print(json.dumps(dict(event="original-native576-damped-trial-replay-identities-verified",modes=112,
            cached_baseline=True,new_baseline_evaluations=0,new_J_evaluations=0,
            complete_native_delta_sha256=direction["delta_float64le_sha256"])),flush=True)
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
            result["returned_original_no_J_trial_evaluations"]=summary.get("original_no_J_trial_returns")
            result["actual_trial_observations"]=summary.get("actual_trial_observations")
            result["observer_failure"]=summary.get("observer_failure")
            expected=("Error: "+STOP if summary.get("trial_accepted") else summary.get("expected_original_failure"))
            complete=(summary.get("replay_completed") is True and result.get("actual_original_failure_message")==expected
                and result.get("worker_exit_code")==0 and result.get("original_native_requests")==1)
            result["replay_completed"]=complete
            result["trial_accepted"]=bool(complete and summary.get("trial_accepted") is True)
        result["elapsed_seconds"]=time.monotonic()-started
        result["small_output_files"]=[dict(file=p.name,bytes=p.stat().st_size,sha256=B.sha(p))
            for p in sorted(a.out.iterdir()) if p.is_file() and p.name!="result.json"]
        B.write(a.out/"result.json",result)
    print(json.dumps(dict(event="original-native576-damped-trial-replay-finished",replay_completed=result["replay_completed"],
        trial_accepted=result["trial_accepted"],native_accepted=False,task_completed=False)),flush=True)
    return 0 if result["replay_completed"] and result["trial_accepted"] else 2

if __name__=="__main__":raise SystemExit(main())
