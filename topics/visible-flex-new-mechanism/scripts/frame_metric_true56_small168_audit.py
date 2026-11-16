#!/usr/bin/env python3
"""New smaller physical-domain168 model at true56; paid inputs reused in public Actions."""
from __future__ import annotations
import time
PROCESS_STARTED=time.monotonic()
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import traceback

REPO="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-new-mechanism"
TAG="TRUE56_SMALL168_"
POLICY_NAME="true56-full168-small-physical-domain-paid-input-v1"
COMPLETE="complete-true56-small168-original-actual-observation"
MAX_MATH_STDOUT_BYTES=136*1024*1024
SOURCE_SECONDS=2421.953314364
SOURCE_VALUES=141
STDOUT_BYTES=0
NEW_SOURCES=(
 "frame_complete_body_extension168.py",
 "frame_complete_body_extension168_joint_selected.py",
 "frame_complete_body_extension168_metric_selected.py",
 "frame_metric_true56_small168_scope.py",
 "frame_metric_true56_small168_solver.py",
 "frame_metric_true56_small168_geometry.py",
 "frame_metric_true56_small168_model.py",
 "frame_metric_true56_small168_transfer.py",
 "frame_metric_true56_small168_actual.py",
 "frame_metric_true56_small168_line.py",
 "frame_metric_true56_small168_audit.py",
 "frame_metric_true56_small168_report.py",
)

def require(value,message):
    if not bool(value):
        raise ValueError(message)

def jsonable(value):
    if isinstance(value,dict):
        return {str(k):jsonable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [jsonable(v) for v in value]
    if "np" in globals() and isinstance(value,np.ndarray):
        return value.tolist()
    if "np" in globals() and isinstance(value,np.generic):
        return value.item()
    return value

def encoded(value):
    return json.dumps(jsonable(value),sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode("utf-8").replace(
            b"##[",b"\\u0023\\u0023[").replace(b"::",b"\\u003a\\u003a")

def emit(suffix,value):
    global STDOUT_BYTES
    raw=encoded(value)
    line=(TAG+suffix+" ").encode()+raw+b"\n"
    reserve=0 if suffix in ("FINAL_CLOCK","REPORTING_ERROR") else 524288
    require(STDOUT_BYTES+len(line)+reserve<=MAX_MATH_STDOUT_BYTES,
            "one original-stdout mathematical output allocation is exhausted")
    sys.stdout.buffer.write(line)
    sys.stdout.buffer.flush()
    STDOUT_BYTES+=len(line)
    return {"tag":TAG+suffix,"JSON_plus_LF_bytes":len(raw)+1,
            "JSON_plus_LF_sha256":hashlib.sha256(raw+b"\n").hexdigest()}

def implementation_hashes(request):
    result={}
    for path,expected in request["source_sha256"].items():
        actual=hashlib.sha256(Path(path).read_bytes()).hexdigest()
        require(actual==expected,"the published source changed: "+path)
        result[path]=actual
    return result

def load_runtime():
    global np,scipy,digest,array_digest
    global read_source,prepare_source,build_joint168_geometry
    global Joint168Model,exchange_joint168,Joint168Actual,Joint168Line
    import numpy as np
    import scipy
    from frame_height_null_coordinates import digest
    from frame_entry_body_subspace import array_digest
    from frame_metric_true56_small168_transfer import read_source,prepare as prepare_source
    from frame_metric_true56_small168_geometry import build_small168_geometry as build_joint168_geometry
    from frame_metric_true56_small168_model import Joint168Model,exchange_joint168
    from frame_metric_true56_small168_actual import Joint168Actual
    from frame_metric_true56_small168_line import Joint168Line
    require(sys.version.split()[0]=="3.12.14"
        and np.__version__=="2.3.5" and scipy.__version__=="1.17.0",
        "the fixed published Python/numpy/scipy runtime is required")
    for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
        require(os.environ.get(key)=="1","one numerical thread is required")

def compact_capture(capture):
    return {key:copy.deepcopy(value) for key,value in capture.items() if not key.startswith("_")}

def array_record(value):
    a=np.asarray(value)
    require(a.dtype.kind in "fiu" and np.all(np.isfinite(a)),
            "finite already-produced numeric arrays required for output")
    return {"dtype":str(a.dtype),"shape":list(a.shape),"array_sha256":array_digest(a),
            "values":a.tolist()}

def direction_payload(cache,model):
    return {
        **{key:copy.deepcopy(value) for key,value in cache.items()
           if key not in ("grids","direction")},
        "kind":"full168-affine-observable-direction",
        "direction168":array_record(cache["direction"]),
        "new_finite_model_binding_sha256":model.binding_sha256,
        "grids":{label:{name:array_record(a) for name,a in values.items()}
                 for label,values in cache["grids"].items()},
        "complete_grid168_gradient_tensor_not_built_or_serialized":True,
        "only_one_chosen_direction_contraction_is_recoverable_here":True,
        "no_ordinary_or_derivative_reexecution_for_output":True}

def partial_input_payload(capture,jets,prepared):
    """Preserve newly paid metric rows without duplicating closed large inputs."""
    if jets is not None:
        return jets.full_payload(array_encoder=array_record)
    out={"schema":POLICY_NAME+"-partial-new-input","status":"partial",
         "progress":compact_capture(capture),
         "partial_is_not_a_completed_model":True,
         "all_started_metric_row_costs_remain_in_the_same_task_ledger":True,
         "completed_new_metric_gradients":copy.deepcopy(
             capture.get("completed_new_metric_gradients",[])),
         "no_old_ordinary_or_selected_J_was_reexecuted":True}
    if prepared is not None:
        out["source_binding"]=copy.deepcopy(prepared.get("source_binding"))
        out["paid_joint_receipt"]=copy.deepcopy(prepared.get("paid_joint_receipt"))
        out["physical_map_binding"]=copy.deepcopy(prepared.get("physical_map_binding"))
    return out

def cost_snapshot(ledger):
    if ledger is None:
        current_process=time.monotonic()-PROCESS_STARTED
        elapsed=PRIOR_SECONDS+current_process
        counts={}
        result={"scientific_seconds":elapsed,"started_counts":counts,
                "limits":{"science_seconds":300},
                "remaining_scientific_seconds":max(0.,300-elapsed),
                "deadline_observed_exceeded":elapsed>=300,
                "observed_overrun_seconds":max(0.,elapsed-300),
                "all_inputs_imports_failures_serialization_share_this_clock":True,
                "bootstrap_error_before_ledger_construction":True,
                "prior_same_task_scientific_seconds":PRIOR_SECONDS,
                "current_process_scientific_seconds":current_process,
                "prior_time_preserved_even_if_source_authentication_raises":True}
    else:
        result=ledger.report()
        elapsed=result["scientific_seconds"]
        counts=result["started_counts"]
    values=counts.get("necessary_model_grid_values",0)+counts.get("actual_grid_values",0)
    result.update(source_accepted_index=56,source_original_values_closed=SOURCE_VALUES,
        ancestor_scientific_seconds=SOURCE_SECONDS,
        total_ancestor_plus_new_scientific_seconds=SOURCE_SECONDS+elapsed,
        new_necessary_model_values=counts.get("necessary_model_grid_values",0),
        new_actual_values=counts.get("actual_grid_values",0),
        total_source_plus_new_started_values=SOURCE_VALUES+values,
        old159_J_or_model_replays=0,old_optimizer_instance_calls=0,
        independent_source_acceptance_replays=0,new_development_calls=0,
        no_time_or_started_count_is_reset_or_hidden=True,
        nested_phase_seconds_are_not_added_to_the_final_clock=True)
    return result

def source_closed_receipt():
    return {"source_run":"43847611444","source_job":"133231619868",
            "source_commit":"a9da16278c336ec5d6ce3be88502263d04429324",
            "source_final_clock_JSON_plus_LF_sha256":
            "39d760b534c554833d6b47f515d417838be64f10fd3a5af440ea10c36a7ad305",
            "ancestor_final_original_scientific_seconds":SOURCE_SECONDS,
            "source_original_full_values":SOURCE_VALUES,
            "closed_scope_not_reopened":True,
            "full_source_receipt_is_authenticated_before_new_geometry":True}


PRIOR_SECONDS=23.005758439000005
PRIOR_SOURCE={
    "run_id":"43851980835","job_id":"133246562883",
    "source_commit":"8f68ac1675d3f896d1e53c187be59549466a2529",
    "workflow":".github/workflows/visible-true56-small168.yml",
    "log_bytes":406203,
    "log_sha256":"d92f4b5dd5077376c76ce49992c9c734f361c61c34bd469ab9cacb9ea0b41fd2"}
PRIOR_RECORDS={
    "COMPLETE":{"JSON_plus_LF_bytes":243483,
        "JSON_plus_LF_sha256":"358c4b593bafd11e4237e682076800c9b230b7fe151926162ab466a13443f318"},
    "FINAL_CLOCK":{"JSON_plus_LF_bytes":3969,
        "JSON_plus_LF_sha256":"bd27823a8c3f9d607a77a3b8e56677374cffe2b2036f0ae9bdbce95be3e1bf3d"}}
PRIOR_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true56-small168.json",
    "bytes":64925,"sha256":"41bbad4ca582631f8725ffeb03982bf46dba5ad159a384b27e8d7a4ea537344f"}

def read_prior_task_receipt(request,progress):
    """Read the genuine failed process; this is the same300-second account."""
    import io
    import read_original_actions_log as reader
    require(request["same_task_prior_failure"]=={
        "source":PRIOR_SOURCE,"records":PRIOR_RECORDS,"request":PRIOR_REQUEST,
        "scientific_seconds":PRIOR_SECONDS,"same_scope_seconds":300},
        "the exact failed small-domain process and original budget are required")
    progress.update(status="started",source=copy.deepcopy(PRIOR_SOURCE),
        ordinary_J_master_reexecution=0)
    raw_request=Path(PRIOR_REQUEST["path"]).read_bytes()
    require(len(raw_request)==PRIOR_REQUEST["bytes"]
        and reader.digest(raw_request)==PRIOR_REQUEST["sha256"],
        "the original same-task request changed")
    previous_request=reader.decode_json(raw_request)
    require(request["parameters"]==previous_request["parameters"]
        and request["original_input_arguments"]==previous_request["original_input_arguments"]
        and request["paid_joint_source"]==previous_request["paid_joint_source"]
        and request["paid_joint_records"]==previous_request["paid_joint_records"],
        "this continuation may not change the mathematical task or limits")
    api=reader.GitHubReader(REPO)
    run=api.api_json("/actions/runs/"+PRIOR_SOURCE["run_id"])
    job=api.api_json("/actions/jobs/"+PRIOR_SOURCE["job_id"])
    require(str(run["id"])==str(job["run_id"])==PRIOR_SOURCE["run_id"]
        and str(job["id"])==PRIOR_SOURCE["job_id"]
        and run["head_sha"]==job["head_sha"]==PRIOR_SOURCE["source_commit"]
        and run["path"]==PRIOR_SOURCE["workflow"]
        and job["status"]=="completed" and job["conclusion"]=="failure",
        "the actual failed research job is required, not a successful replacement")
    raw,redirects=api.job_log(PRIOR_SOURCE["job_id"])
    require(len(raw)==PRIOR_SOURCE["log_bytes"]
        and reader.digest(raw)==PRIOR_SOURCE["log_sha256"],
        "the original failed stdout identity changed")
    found={}
    counts={}
    for line in io.StringIO(raw.decode("utf-8-sig")):
        clean=reader.ANSI.sub("",line.rstrip("\r\n")).lstrip("\ufeff")
        match=reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body=match.group(2).lstrip("\ufeff")
        if not body.startswith("TRUE56_SMALL168_"):
            continue
        tag,sep,payload=body[len("TRUE56_SMALL168_"):].partition(" ")
        if not sep:
            continue
        counts[tag]=counts.get(tag,0)+1
        if tag not in PRIOR_RECORDS:
            continue
        literal=payload.encode("utf-8")+b"\n"
        pin=PRIOR_RECORDS[tag]
        require(counts[tag]==1 and len(literal)==pin["JSON_plus_LF_bytes"]
            and reader.digest(literal)==pin["JSON_plus_LF_sha256"],
            "the failed process original record identity changed")
        found[tag]=reader.decode_json(literal)
    require(set(found)==set(PRIOR_RECORDS),
        "both original same-task COMPLETE and FINAL_CLOCK are required")
    real,clock=found["COMPLETE"],found["FINAL_CLOCK"]
    require(real["status"]==clock["status_at_final_emit"]=="joint168-input-or-scientific-error"
        and real["github_sha"]==PRIOR_SOURCE["source_commit"]
        and str(real["github_run_id"])==PRIOR_SOURCE["run_id"]
        and real["source_files_sha256"]==previous_request["source_sha256"]
        and real["error"]["message"]==
            "coarse complete source pool is malformed or exceeds the original capacity"
        and clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
        and not clock["scope_exhausted"],
        "the exact original pre-model pool-order failure must be continued")
    prior=copy.deepcopy(clock["ledger"])
    require(prior["scientific_seconds"]==PRIOR_SECONDS
        and prior["limits"]==request["parameters"]["limits"]
        and all(type(v) is int and v==0 for v in prior["started_counts"].values())
        and prior["attempted_problem_bindings"]==[]
        and prior["ancestor_scientific_seconds"]==SOURCE_SECONDS
        and prior["total_source_plus_new_started_values"]==SOURCE_VALUES,
        "all original failed time/counts and closed ancestor must remain")
    prior["source"]={"source":copy.deepcopy(PRIOR_SOURCE),
        "records":copy.deepcopy(PRIOR_RECORDS),"request":copy.deepcopy(PRIOR_REQUEST),
        "same_task_not_a_budget_reset":True}
    progress.update(status="complete",source=copy.deepcopy(PRIOR_SOURCE),
        original_records=copy.deepcopy(PRIOR_RECORDS),
        prior_same_task_scientific_seconds=PRIOR_SECONDS,
        prior_started_counts=copy.deepcopy(prior["started_counts"]),
        log_redirects_without_forwarding_authorization=redirects)
    return prior


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    ledger=prepared=completed=jets=model=handle=scan=cache=line=actual=None
    scope_error_type=()
    source_capture={}
    prior_capture={}
    build_capture={}
    exchange_progress={}
    report={
        "schema":POLICY_NAME+"-audit","status":"not-started",
        "github_repository":REPO,"github_sha":os.environ.get("GITHUB_SHA"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "timing_segments":{},"old_checks_executed":0,"new_development_executed":0,
        "new_scope_is_a_smaller_physical_domain_with_paid_current168_inputs":True,
        "necessary_ordinary_and_old_selected_J_reexecution_counts":0,
        "all168_coordinates_can_move_from_nonzero_new9_center":True,
        "model_prediction_is_not_geometric_acceptance":True,
        "main_readme_completion_claim":False}
    output=Path(args.out).resolve()
    model_attempted=cache_attempted=False
    input_receipt=None
    try:
        require(os.environ.get("GITHUB_ACTIONS")=="true"
                and os.environ.get("GITHUB_REPOSITORY")==REPO,
                "all new scientific work belongs only to this public Actions")
        require("MR_TOKEN" not in os.environ,"the private credential must leave before science")
        root=Path(__file__).resolve().parents[3]
        require(output!=root and root not in output.parents,
                "all machine output belongs only to temporary runner storage")
        output.parent.mkdir(parents=True,exist_ok=True)
        request_path=Path(args.request).resolve()
        require(root in request_path.parents,"request must be in this exact checkout")
        raw=request_path.read_bytes()
        require(len(raw)<100000,"one small source and parameter request is required")
        request=json.loads(raw)
        report["request_identity"]={"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
        report["source_files_sha256"]=implementation_hashes(request)
        from frame_metric_true56_small168_scope import Joint168Ledger,Joint168Limit,LIMITS,POLICY
        scope_error_type=(Joint168Limit,)
        prior=read_prior_task_receipt(request,prior_capture)
        ledger=Joint168Ledger(PROCESS_STARTED,ancestor_receipt=source_closed_receipt(),
                             prior_scope_receipt=prior)
        report["same_task_prior_receipt"]=copy.deepcopy(prior_capture)
        params=request["parameters"]
        require(POLICY==POLICY_NAME and params["policy"]==POLICY
            and params["limits"]==LIMITS
            and params["maximum_mathematical_stdout_bytes"]==MAX_MATH_STDOUT_BYTES
            and params["source_original_actual_values"]==SOURCE_VALUES
            and params["ancestor_final_original_scientific_seconds"]==SOURCE_SECONDS
            and params["old_checks_executed"]==params["new_development_executed"]==0
            and params["all168_coordinates_free_at_actual56"] is True
            and params["physical_norm_factor"]==4. and params["maximum_physical_step"]==1./512.
            and params["maximum_h_exact"]=="1/128"
            and params["new_independent_count"]==168 and params["new_physical_count"]==172,
            "the new full168 scope and unchanged closed ancestor account are required")
        require(request["new_python_sources"]==[TOPIC+"/scripts/"+name for name in NEW_SOURCES],
                "all complete-field, joint168-model and reporting sources must be pinned")
        emit("INPUT",{"kind":"new-full168-bound-request",
            "request_identity":report["request_identity"],"parameters":params,
            "source_files_sha256":report["source_files_sha256"]})
        tick=time.monotonic()
        try:
            load_runtime()
        finally:
            report["timing_segments"]["runtime_imports_seconds"]=time.monotonic()-tick
        ledger.check("joint168.after-imports")
        tick=time.monotonic()
        try:
            completed=read_source(request,ledger,capture=source_capture)
        finally:
            report["timing_segments"]["source56_stdout_read_seconds"]=time.monotonic()-tick
        report["source56_paid_receipt"]=copy.deepcopy(completed["receipt"])
        report["closed_ancestor_cost"]=copy.deepcopy(completed["ancestor_cost_receipt"])
        report["source56_actual_point"]=copy.deepcopy(completed["point"])
        emit("INPUT",{"kind":"accepted56-original-source","receipt":completed["receipt"]})
        tick=time.monotonic()
        try:
            prepared=prepare_source(request,output,completed,ledger,process_started=PROCESS_STARTED)
        finally:
            report["timing_segments"]["original24_inputs_prepare_seconds"]=time.monotonic()-tick
        report.update(configuration=copy.deepcopy(prepared["cfg"]),
            fixed_complete_metric_sha256=request["fixed_complete_metric_sha256"],
            fixed_b0_definition_sha256=request["fixed_b0_definition_sha256"],
            full_value_sampling_definition=copy.deepcopy(prepared["grid"]),
            source_transfer=copy.deepcopy(prepared["replay"]["source_input_restoration"]))
        tick=time.monotonic()
        try:
            jets=build_joint168_geometry(prepared,ledger,capture=build_capture)
            report["joint168_input_receipt"]=jets.receipt()
            input_receipt=emit("INPUT",jets.full_payload(array_encoder=array_record))
            report["complete_current168_input_stdout_receipt"]=input_receipt
            jets.input_record_original_stdout_receipt=copy.deepcopy(input_receipt)
            model=Joint168Model(prepared,jets,ledger=ledger)
        finally:
            report["timing_segments"]["paid_input_restore_new_metric_row_and_small_domain_model_seconds"]=time.monotonic()-tick
        tick=time.monotonic()
        try:
            handle,scan=exchange_joint168(model,jets,ledger,emit=emit,progress=exchange_progress)
        finally:
            report["timing_segments"]["joint168_original_row_exchange_seconds"]=time.monotonic()-tick
        if handle is not None:
            report["complete_first_order_direction"]=copy.deepcopy(handle["report"])
        if handle is not None and handle["qualified"]:
            cache=jets.direction_cache(handle["direction"])
            cache_attempted=True
            report["direction_cache_stdout_receipt"]=emit("CACHE",direction_payload(cache,model))
            ledger.check("joint168.after-direction-cache-output")
            line=Joint168Line(prepared,model,handle,cache,ledger,emit=emit)
            tick=time.monotonic()
            try:
                scalar=line.run()
                report["scalar_result_stdout_receipt"]=emit("SCALAR_RESULT",scalar)
                if scalar["qualified_predicted_descent"]:
                    actual=Joint168Actual(prepared,completed,ledger)
                    report["actual_scale_selection"]=line.actual_candidates(actual,emit=emit)
                else:
                    report["actual_scale_selection"]={
                        "status":"no-affine-observable-descent-no-actual-call",
                        "trials":[],"new_acceptances":0}
            finally:
                report["timing_segments"]["joint168_scalar_and_actual_seconds"]=time.monotonic()-tick
        else:
            report["actual_scale_selection"]={
                "status":"no-complete-first-order-qualified-direction-no-actual-call",
                "exchange_status":exchange_progress.get("status"),"trials":[],"new_acceptances":0}
        report["status"]=COMPLETE
    except Exception as error:
        report["status"]=("joint168-scope-exhausted" if isinstance(error,scope_error_type)
                          else "joint168-input-or-scientific-error")
        report["error"]={"type":type(error).__name__,"message":str(error),
                         "traceback":traceback.format_exc(),
                         "budget_kind":getattr(error,"kind",None)}
    finally:
        report["same_task_prior_input_progress"]=copy.deepcopy(prior_capture)
        report["source_input_progress"]=compact_capture(source_capture)
        report["new_input_progress"]=compact_capture(build_capture)
        report["exchange_progress"]=exchange_progress
        if line is not None:
            report["scalar_observation"]=line.report()
        if model is not None:
            report["finite_model_observation"]=model.report()
            if not model_attempted:
                model_attempted=True
                try:
                    report["model_stdout_receipt"]=emit("MODEL",model.full_record())
                except Exception as error:
                    report["model_output_error"]={"type":type(error).__name__,"message":str(error)}
                    if report["status"]==COMPLETE:
                        report["status"]="joint168-model-output-error"
        elif input_receipt is None and build_capture:
            try:
                report["partial_input_stdout_receipt"]=emit(
                    "MODEL",partial_input_payload(build_capture,jets,prepared))
            except Exception as error:
                report["partial_input_output_error"]={"type":type(error).__name__,"message":str(error)}
        if cache is not None and not cache_attempted:
            cache_attempted=True
            try:
                report["direction_cache_stdout_receipt"]=emit("CACHE",direction_payload(cache,model))
            except Exception as error:
                report["direction_cache_output_error"]={"type":type(error).__name__,"message":str(error)}
        if actual is not None:
            report["actual_stage"]=actual.report()
            report["selected_two_grid_physical_point"]=copy.deepcopy(actual.selected_point)
            report["new_acceptances"]=int(actual.accepted_state is not None)
            if actual.accepted_state is not None:
                try:
                    payload=actual.accepted_cache_payload()
                    report["accepted_cache_stdout_receipt"]=emit("CACHE",payload)
                    report["accepted_cache_stdout_receipt"].update(
                        accepted_index=57,binding_sha256=payload["binding_sha256"],
                        no_geometry_or_JVP_reexecution=True)
                except Exception as error:
                    report["accepted_cache_output_error"]={"type":type(error).__name__,"message":str(error)}
                    if report["status"]==COMPLETE:
                        report["status"]="joint168-accepted-cache-output-error"
        elif completed is not None:
            report["selected_two_grid_physical_point"]=copy.deepcopy(completed["point"])
            report["new_acceptances"]=0
        if prepared is not None:
            report["future_source_restoration"]={
                "actual56_source":copy.deepcopy(request.get("source")),
                "closed_joint168_paid_input_source":copy.deepcopy(request.get("paid_joint_source")),
                "closed_joint168_paid_records":copy.deepcopy(request.get("paid_joint_records")),
                "actual56_source_records":copy.deepcopy(request.get("source_records")),
                "fixed_reference_source":copy.deepcopy(request.get("fixed_reference_source")),
                "fixed_reference_record":copy.deepcopy(request.get("fixed_reference_record")),
                "permanent_constructor_source_is_not_a_current_point_or_derivative":True,
                "all168_coordinates_were_free_at_actual56":True,
                "same_task_prior_failure":copy.deepcopy(request.get("same_task_prior_failure")),
                "complete_field_definition":prepared["field168"].evaluation_definition(),
                "physical_map_binding":copy.deepcopy(prepared["physical_map_binding"]),
                "new_input_model_and_actual_arrays_live_only_in_original_stdout":True,
                "complete_grid168_gradient_tensor_was_not_built_or_saved":True,
                "old159_bank_gamma_and_controller_are_source_provenance_not_new168_certificates":True}
    report["ledger_before_complete_output"]=cost_snapshot(ledger)
    report["process_elapsed_before_complete_output"]=time.monotonic()-PROCESS_STARTED
    report["peak_rss_kib_linux"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["mathematical_stdout_bytes_before_complete"]=STDOUT_BYTES
    report["final_clock_is_later_and_authoritative"]=True
    complete_receipt=None
    try:
        output.write_bytes(encoded(report)+b"\n")
        complete_receipt=emit("COMPLETE",report)
    except Exception as error:
        report["status"]="joint168-final-serialization-error"
        emit("REPORTING_ERROR",{"status":report["status"],
            "error":{"type":type(error).__name__,"message":str(error)},
            "selected_two_grid_physical_point":report.get("selected_two_grid_physical_point"),
            "source_input_progress":report.get("source_input_progress"),
            "new_input_progress":report.get("new_input_progress"),
            "model_stdout_receipt":report.get("model_stdout_receipt"),
            "direction_cache_stdout_receipt":report.get("direction_cache_stdout_receipt"),
            "accepted_cache_stdout_receipt":report.get("accepted_cache_stdout_receipt"),
            "ledger":cost_snapshot(ledger)})
    earlier=report["status"]
    exhausted=report["status"]=="joint168-scope-exhausted"
    if ledger is not None:
        try:
            ledger.check("all-large-output.completed")
        except Exception as error:
            exhausted=True
            report["status"]="joint168-scope-exhausted-after-output"
            report["final_budget_message"]=str(error)
    elif PRIOR_SECONDS+time.monotonic()-PROCESS_STARTED>=300:
        exhausted=True
        report["status"]="joint168-scope-exhausted-after-output"
        report["final_budget_message"]="same 300-second scope exceeded before ledger construction"
    emit("FINAL_CLOCK",{
        "schema":POLICY_NAME+"-final-clock","status_at_final_emit":report["status"],
        "earlier_COMPLETE_status":earlier,"scope_exhausted":exhausted,
        "budget_message":report.get("final_budget_message"),"complete_receipt":complete_receipt,
        "ledger":cost_snapshot(ledger),"process_seconds":time.monotonic()-PROCESS_STARTED,
        "sampled_after_all_large_cache_and_complete_write_and_flush":True,
        "mathematical_stdout_bytes_before_final_clock":STDOUT_BYTES,
        "peak_rss_kib_linux":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "this_status_supersedes_earlier_COMPLETE_scope_status":True,
        "no_scientific_queries_follow_this_record":True})
    return 0 if report["status"]==COMPLETE else 1

if __name__=="__main__":
    raise SystemExit(main())
