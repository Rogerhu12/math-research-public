#!/usr/bin/env python3
"""New complete-body nine-fiber at true55; all science only in public Actions."""
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
TAG="TRUE55_NINE_"
POLICY_NAME="fixed159-true55-new9-affine-fiber-v1"
COMPLETE="complete-true55-new9-fiber-original-actual-observation"
MAX_MATH_STDOUT_BYTES=112*1024*1024
SOURCE_SECONDS=2073.56241112
SOURCE_VALUES=134
PRIOR_NEW_SCOPE_SECONDS=75.06856296999999
PRIOR_NEW_SCOPE_COUNTS={"actual_grid_values":0,"actual_trial_pairs":0,"finite_master_calls":0,"finite_master_iterations":0,"finite_master_newton_systems":0,"full_separations":0,"hard_J_grid_builds":0,"metric9_grid_builds":0,"necessary_model_grid_values":1,"new_metric_rows":0,"scalar_queries":0,"scalar_sessions":0}
STDOUT_BYTES=0
NEW_SOURCES=(
 "frame_complete_body_extension168.py",
 "frame_complete_body_extension168_selected.py",
 "frame_metric_true55_nine_fiber_scope.py",
 "frame_metric_true55_nine_fiber_solver.py",
 "frame_metric_true55_nine_fiber_geometry.py",
 "frame_metric_true55_nine_fiber_model.py",
 "frame_metric_true55_nine_fiber_transfer.py",
 "frame_metric_true55_nine_fiber_resume_input.py",
 "frame_metric_true55_nine_fiber_actual.py",
 "frame_metric_true55_nine_fiber_line.py",
 "frame_metric_true55_nine_fiber_audit.py",
 "frame_metric_true55_nine_fiber_report.py",
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
    global read_source,prepare_source,build_new_nine_geometry
    global NineFiberModel,exchange_nine_fiber,NineFiberActual,NineFiberLine,restore_paid_coarse
    import numpy as np
    import scipy
    from frame_height_null_coordinates import digest
    from frame_entry_body_subspace import array_digest
    from frame_metric_true55_nine_fiber_transfer import read_source,prepare as prepare_source
    from frame_metric_true55_nine_fiber_geometry import build_new_nine_geometry
    from frame_metric_true55_nine_fiber_model import NineFiberModel,exchange_nine_fiber
    from frame_metric_true55_nine_fiber_resume_input import restore_paid_coarse
    from frame_metric_true55_nine_fiber_actual import NineFiberActual
    from frame_metric_true55_nine_fiber_line import NineFiberLine
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
        "kind":"new9-affine-observable-direction",
        "direction9":array_record(cache["direction"]),
        "new_finite_model_binding_sha256":model.binding_sha256,
        "grids":{label:{name:array_record(a) for name,a in values.items()}
                 for label,values in cache["grids"].items()},
        "complete_metric9_tensor_not_serialized":True,
        "only_one_chosen_direction_contraction_is_recoverable_here":True,
        "no_ordinary_or_derivative_reexecution_for_output":True}

def partial_input_payload(capture,jets,prepared):
    """Preserve completed new inputs on a genuine construction failure only."""
    out={"schema":POLICY_NAME+"-partial-new-input","status":"partial",
         "progress":compact_capture(capture),"grids":{},
         "partial_is_not_a_completed_model":True,
         "ordinary_derivative_counters_remain_the_original_started_counters":True}
    if jets is not None:
        out["model_input"]={
            "original_domain":jets.original_domain,
            "complete_phi0":jets.phi0,"target":jets.target,
            "binding":copy.deepcopy(jets.binding),"binding_sha256":jets.binding_sha256,
            "center168":jets.center168,"source55":55,
            "domain_receipt":copy.deepcopy(jets.domain_receipt)}
        out["complete_metric9_for_input_recovery"]={
            label:{name:array_record(value) for name,value in rows["metric9"].items()}
            for label,rows in jets.grid_records.items()}
        return out
    for label,rows in capture.get("_arrays",{}).items():
        item={}
        for key in ("hard_ids","hard_J9"):
            if key in rows:
                item[key]=array_record(rows[key])
        if "metric9" in rows:
            item["complete_metric9"]={key:array_record(a) for key,a in rows["metric9"].items()}
        elif isinstance(rows.get("ordinary"),dict):
            ordinary=rows["ordinary"]
            item["paid_ordinary_input"]={
                key:array_record(ordinary[key])
                for key in ("X","Xs","Xt","Xss","Xst","Xtt","T")}
            item["metric"]={key:array_record(ordinary["metric"][key])
                            for key in ("a","a_s","a_ss")}
            item["height"]={key:array_record(ordinary["height"][key])
                            for key in ("b","b_s","b_ss")}
            item["center"]=array_record(ordinary["center"])
            item["radial"]=array_record(ordinary["radial"])
            item["theta"]=array_record(ordinary["theta"])
        values=rows.get("rows",rows.get("rows_with_original_hard_components"))
        if values is not None and "hard_ids" in rows:
            item["same_hard_row_values"]=array_record(
                np.asarray(values).reshape(-1)[np.asarray(rows["hard_ids"],dtype=np.int64)])
        if isinstance(rows.get("bound"),dict):
            item["ordinary_binding_sha256"]=rows["bound"]["binding_sha256"]
            item["ordinary_source_receipt"]=copy.deepcopy(rows["bound"]["source_receipt"])
        out["grids"][label]=item
    if prepared is not None:
        out["source_binding"]=copy.deepcopy(prepared.get("source_binding"))
    return out

def cost_snapshot(ledger):
    if ledger is None:
        current_elapsed=time.monotonic()-PROCESS_STARTED
        elapsed=PRIOR_NEW_SCOPE_SECONDS+current_elapsed
        counts=dict(PRIOR_NEW_SCOPE_COUNTS)
        result={"scientific_seconds":elapsed,"started_counts":counts,
                "prior_same_task_scientific_seconds":PRIOR_NEW_SCOPE_SECONDS,
                "current_process_scientific_seconds":current_elapsed,
                "prior_scope_literal_receipt_not_yet_authenticated_in_this_process":True,
                "limits":{"science_seconds":600},
                "remaining_scientific_seconds":max(0.,600-elapsed),
                "deadline_observed_exceeded":elapsed>=600,
                "observed_overrun_seconds":max(0.,elapsed-600),
                "all_inputs_imports_failures_serialization_share_this_clock":True,
                "bootstrap_error_before_ledger_construction":True}
    else:
        result=ledger.report()
        elapsed=result["scientific_seconds"]
        counts=result["started_counts"]
    values=counts.get("necessary_model_grid_values",0)+counts.get("actual_grid_values",0)
    result.update(source_accepted_index=55,source_original_values_closed=SOURCE_VALUES,
        ancestor_scientific_seconds=SOURCE_SECONDS,
        total_ancestor_plus_new_scientific_seconds=SOURCE_SECONDS+elapsed,
        new_necessary_model_values=counts.get("necessary_model_grid_values",0),
        new_actual_values=counts.get("actual_grid_values",0),
        total_source_plus_new_started_values=SOURCE_VALUES+values,
        old159_J_or_model_calls=0,old_optimizer_instance_calls=0,
        independent_source_acceptance_replays=0,new_development_calls=0,
        no_time_or_started_count_is_reset_or_hidden=True,
        nested_phase_seconds_are_not_added_to_the_final_clock=True)
    return result

def source_closed_receipt():
    return {"source_run":"43832870561","source_job":"133182173190",
            "source_commit":"23b37e90cbc1ac33ca6ff8ac1f91fa7a95c903db",
            "source_final_clock_JSON_plus_LF_sha256":
            "61ac9c3d62f869307d8f2ab1357c438466395997cd31189a2d3e225fea8369bb",
            "ancestor_final_original_scientific_seconds":SOURCE_SECONDS,
            "source_original_full_values":SOURCE_VALUES,
            "closed_scope_not_reopened":True,
            "full_source_receipt_is_authenticated_before_new_geometry":True}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    ledger=prepared=completed=jets=model=handle=scan=cache=line=actual=None
    scope_error_type=()
    source_capture={}
    continuation_capture={}
    build_capture={}
    exchange_progress={}
    report={
        "schema":POLICY_NAME+"-audit","status":"not-started",
        "github_repository":REPO,"github_sha":os.environ.get("GITHUB_SHA"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "timing_segments":{},"old_checks_executed":0,"new_development_executed":0,
        "new_scope_is_only_true55_fixed159_plus_nine":True,
        "full168_joint_problem_not_solved_by_this_fiber":True,
        "model_prediction_is_not_geometric_acceptance":True,
        "main_readme_completion_claim":False}
    output=Path(args.out).resolve()
    model_attempted=cache_attempted=False
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
        from frame_metric_true55_nine_fiber_scope import NineFiberLedger,NineFiberLimit,LIMITS,POLICY
        scope_error_type=(NineFiberLimit,)
        prior=request["continuation"]["prior_scope_receipt"]
        require(prior["scientific_seconds"]==PRIOR_NEW_SCOPE_SECONDS
            and prior["started_counts"]==PRIOR_NEW_SCOPE_COUNTS,
            "the original failed-entry time and started counts precede all new input")
        ledger=NineFiberLedger(PROCESS_STARTED,ancestor_receipt=source_closed_receipt(),
            prior_scope_receipt=prior)
        params=request["parameters"]
        require(POLICY==POLICY_NAME and params["policy"]==POLICY
            and params["limits"]==LIMITS
            and params["maximum_mathematical_stdout_bytes"]==MAX_MATH_STDOUT_BYTES
            and params["source_original_actual_values"]==SOURCE_VALUES
            and params["ancestor_final_original_scientific_seconds"]==SOURCE_SECONDS
            and params["old_checks_executed"]==params["new_development_executed"]==0
            and params["old159_fixed_to_true55"] is True
            and params["new_independent_count"]==168 and params["new_physical_count"]==172,
            "the one new9 scope and unchanged closed ancestor account are required")
        require(request["new_python_sources"]==[TOPIC+"/scripts/"+name for name in NEW_SOURCES],
                "all complete-field, new9-model and reporting sources must be pinned")
        emit("INPUT",{"kind":"new-nine-bound-request",
            "request_identity":report["request_identity"],"parameters":params,
            "source_files_sha256":report["source_files_sha256"]})
        tick=time.monotonic()
        try:
            load_runtime()
        finally:
            report["timing_segments"]["runtime_imports_seconds"]=time.monotonic()-tick
        ledger.check("new9.after-imports")
        tick=time.monotonic()
        try:
            completed=read_source(request,ledger,capture=source_capture)
        finally:
            report["timing_segments"]["source55_stdout_read_seconds"]=time.monotonic()-tick
        report["source55_paid_receipt"]=copy.deepcopy(completed["receipt"])
        report["source55_final_clock_cost"]=copy.deepcopy(completed["ancestor_cost_receipt"])
        report["source55_actual_point"]=copy.deepcopy(completed["point"])
        emit("INPUT",{"kind":"accepted55-original-source","receipt":completed["receipt"]})
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
            restored,receipt=restore_paid_coarse(request,prepared,ledger,capture=continuation_capture)
            prepared["restored_new9_ordinary"]=restored
            report["continued_paid_input_receipt"]=receipt
            emit("INPUT",{"kind":"continued-paid-coarse-ordinary","receipt":receipt})
        finally:
            report["timing_segments"]["continued_paid_coarse_input_seconds"]=time.monotonic()-tick
        tick=time.monotonic()
        try:
            jets=build_new_nine_geometry(prepared,ledger,capture=build_capture)
            report["new9_input_receipt"]=jets.receipt()
            emit("INPUT",{"kind":"new9-two-grid-model-input","receipt":jets.receipt()})
            model=NineFiberModel(prepared,jets,ledger=ledger)
        finally:
            report["timing_segments"]["new9_two_grid_input_and_model_seconds"]=time.monotonic()-tick
        tick=time.monotonic()
        try:
            handle,scan=exchange_nine_fiber(model,jets,ledger,emit=emit,progress=exchange_progress)
        finally:
            report["timing_segments"]["new9_original_row_exchange_seconds"]=time.monotonic()-tick
        if handle is not None:
            report["complete_first_order_direction"]=copy.deepcopy(handle["report"])
        if handle is not None and handle["qualified"]:
            cache=jets.direction_cache(handle["direction"])
            cache_attempted=True
            report["direction_cache_stdout_receipt"]=emit("CACHE",direction_payload(cache,model))
            ledger.check("new9.after-direction-cache-output")
            line=NineFiberLine(prepared,model,handle,cache,ledger,emit=emit)
            tick=time.monotonic()
            try:
                scalar=line.run()
                report["scalar_result_stdout_receipt"]=emit("SCALAR_RESULT",scalar)
                if scalar["qualified_predicted_descent"]:
                    actual=NineFiberActual(prepared,completed,ledger)
                    report["actual_scale_selection"]=line.actual_candidates(actual,emit=emit)
                else:
                    report["actual_scale_selection"]={
                        "status":"no-affine-observable-descent-no-actual-call",
                        "trials":[],"new_acceptances":0}
            finally:
                report["timing_segments"]["new9_scalar_and_actual_seconds"]=time.monotonic()-tick
        else:
            report["actual_scale_selection"]={
                "status":"no-complete-first-order-qualified-direction-no-actual-call",
                "exchange_status":exchange_progress.get("status"),"trials":[],"new_acceptances":0}
        report["status"]=COMPLETE
    except Exception as error:
        report["status"]=("new9-scope-exhausted" if isinstance(error,scope_error_type)
                          else "new9-input-or-scientific-error")
        report["error"]={"type":type(error).__name__,"message":str(error),
                         "traceback":traceback.format_exc(),
                         "budget_kind":getattr(error,"kind",None)}
    finally:
        report["source_input_progress"]=compact_capture(source_capture)
        report["same_task_continuation_progress"]=compact_capture(continuation_capture)
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
                        report["status"]="new9-model-output-error"
        elif build_capture.get("_arrays"):
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
                        accepted_index=56,binding_sha256=payload["binding_sha256"],
                        no_geometry_or_JVP_reexecution=True)
                except Exception as error:
                    report["accepted_cache_output_error"]={"type":type(error).__name__,"message":str(error)}
                    if report["status"]==COMPLETE:
                        report["status"]="new9-accepted-cache-output-error"
        elif completed is not None:
            report["selected_two_grid_physical_point"]=copy.deepcopy(completed["point"])
            report["new_acceptances"]=0
        if prepared is not None:
            report["future_source_restoration"]={
                "original55_source":copy.deepcopy(request.get("source")),
                "original55_source_records":copy.deepcopy(request.get("source_records")),
                "original159_remain_fixed_to55":True,
                "new9_complete_field_definition":(
                    prepared["field168"].evaluation_definition() if "field168" in prepared else None),
                "new_input_model_and_actual_arrays_live_only_in_original_stdout":True,
                "new9_complete_tensor_was_not_saved_unless_partial_input_required":True,
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
        report["status"]="new9-final-serialization-error"
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
    exhausted=report["status"]=="new9-scope-exhausted"
    if ledger is not None:
        try:
            ledger.check("all-large-output.completed")
        except Exception as error:
            exhausted=True
            report["status"]="new9-scope-exhausted-after-output"
            report["final_budget_message"]=str(error)
    elif PRIOR_NEW_SCOPE_SECONDS+time.monotonic()-PROCESS_STARTED>=600:
        exhausted=True
        report["status"]="new9-scope-exhausted-after-output"
        report["final_budget_message"]="same 600-second scope including prior failed entry exceeded before ledger construction"
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
