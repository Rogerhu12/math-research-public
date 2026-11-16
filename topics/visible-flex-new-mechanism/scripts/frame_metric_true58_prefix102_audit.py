#!/usr/bin/env python3
"""One fixed-ring prefix102 fullbody problem; at most one original actual candidate."""
from __future__ import annotations
import time
PROCESS_STARTED=time.monotonic()
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import traceback

PREFIX="TRUE58_PREFIX102_"
STDOUT_LIMIT=256*1024*1024
STDOUT_BYTES=0
np=None
POLICY="true58-fixed-ring-prefix102-body-repair-v1"
LABELS=("coarse","fine")

def encoded(value):
    return json.dumps(value,ensure_ascii=True,sort_keys=True,separators=(",",":"),
                      allow_nan=False).encode("utf-8")
def sha(value):
    return hashlib.sha256(value).hexdigest()
def numeric(value):
    if np is not None and isinstance(value,np.ndarray):
        a=np.asarray(value)
        return {"dtype":str(a.dtype),"shape":list(a.shape),
                "array_sha256":array_digest(a),"values":numeric(a.tolist())}
    if np is not None and isinstance(value,np.generic):
        return numeric(value.item())
    if isinstance(value,Q):
        return str(value)
    if isinstance(value,dict):
        return {str(k):numeric(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [numeric(v) for v in value]
    if isinstance(value,float) and not math.isfinite(value):
        return {"original_nonfinite_float":repr(value)}
    if value is None or isinstance(value,(str,bool,int,float)):
        return value
    raise TypeError("unserialized retained original value: "+type(value).__name__)
def public_capture(capture):
    return numeric({k:v for k,v in capture.items() if not k.startswith("_")})
def emit(tag,value):
    global STDOUT_BYTES
    data=encoded(numeric(value))+b"\n"
    full=PREFIX+tag
    total=len(full)+1+len(data)
    if STDOUT_BYTES+total>STDOUT_LIMIT:
        raise RuntimeError("declared original mathematical stdout limit reached")
    sys.stdout.buffer.write(full.encode("ascii")+b" "+data)
    sys.stdout.buffer.flush()
    STDOUT_BYTES+=total
    return {"tag":full,"JSON_plus_LF_bytes":len(data),"JSON_plus_LF_sha256":sha(data)}

def load_runtime():
    global np,scipy,array_digest,digest,read_source,prepare_source
    global bind_current_168_curvature_metric,Prefix58Actual
    global build_fixed_ring_prefix102_model,solve_fixed_ring_prefix102_once
    global fixed_ring_prefix102_capture_record
    import numpy as np
    import scipy
    from frame_entry_body_subspace import array_digest
    from frame_height_null_coordinates import digest
    from frame_metric_true58_prefix102_transfer import read_source,prepare as prepare_source
    from frame_complete_body_extension168_curvature_prediction import bind_current_168_curvature_metric
    from frame_metric_current168_fixed_ring_prefix102 import (
        build_fixed_ring_prefix102_model,solve_fixed_ring_prefix102_once,
        fixed_ring_prefix102_capture_record)
    from frame_metric_true58_prefix102_actual import Prefix58Actual
    require(sys.version_info[:3]==(3,12,14) and np.__version__=="2.3.5"
            and scipy.__version__=="1.17.0","unchanged pinned numerical runtime required")
    for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
        require(os.environ.get(key)=="1","one numerical thread required")

def cost(ledger):
    if ledger is not None:
        return ledger.report()
    elapsed=float(time.monotonic()-PROCESS_STARTED)
    return {"scientific_seconds":elapsed,"started_counts":{},
            "source_original_values_closed":147,"ancestor_scientific_seconds":2974.589423877,
            "total_ancestor_plus_new_scientific_seconds":2974.589423877+elapsed,
            "total_source_plus_new_started_values":147,"bootstrap_failure_before_ledger":True,
            "observed_overrun_seconds":max(0.,elapsed-600)}

def new_fixed_metric(prepared,completed,ledger):
    event=ledger.begin("fixed_metric_evaluations",source_accepted_index=58)
    try:
        field,r=prepared["field168"],prepared["radial"]
        metric=field.metric(prepared["q168"],r,jacobian=False)
        source={"kind":"new-fixed-g-input-for-fixed-ring-prefix102-body-repair",
            "actual58":copy.deepcopy(completed["receipt"]),
            "fixed_g":completed["report"]["fixed_complete_metric_sha256"],
            "this_is_a_new_paid_metric_call_not_an_old_prediction_array":True}
        bound=bind_current_168_curvature_metric(field,r,metric,source)
        ledger.end(event,metric_binding_sha256=bound["binding_sha256"],
            current_metric_evaluation_is_a_new_charged_call=True)
        ledger.check("fixed-metric.complete")
        return bound
    except Exception as error:
        if event["status"]=="started": ledger.end(event,error)
        raise

def main():
    global require
    parser=argparse.ArgumentParser()
    parser.add_argument("--request",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    ledger=None;completed=None;prepared=None;model=None;actual=None
    source_capture={};model_capture={};solve_capture={}
    report={"schema":POLICY+"-complete","status":"started","github_repository":
        os.environ.get("GITHUB_REPOSITORY"),"github_sha":os.environ.get("GITHUB_SHA"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"new_acceptances":0,
        "main_readme_completion_claim":False,"old_checks_executed":0,"new_development_executed":0}
    error=None
    try:
        from frame_metric_true58_prefix102_scope import (
            Prefix58Ledger,require,LIMITS,SOLVER_TIME_LIMIT_SECONDS,SOLVER_MAXITER,
            MAX_COMPLETE_EVALUATIONS,SOLVER_OPTIONS,SOURCE_ETA,MINIMUM_DECREASE_EXACT,
            FIXED_SUFFIX_LOWER_EXACT)
        raw=Path(args.request).read_bytes();request=json.loads(raw)
        require(request["parameters"]["policy"]==POLICY
                and request["parameters"]["limits"]==LIMITS
                and request["parameters"]["solver_time_limit_seconds"]==SOLVER_TIME_LIMIT_SECONDS
                and request["parameters"]["solver_maxiter"]==SOLVER_MAXITER
                and request["parameters"]["maximum_complete_evaluations"]==MAX_COMPLETE_EVALUATIONS
                and request["parameters"]["solver_options"]==SOLVER_OPTIONS
                and request["parameters"]["source_eta_binary64"]==SOURCE_ETA
                and request["parameters"]["minimum_accepted_eta_decrease_exact"]==MINIMUM_DECREASE_EXACT
                and request["parameters"]["fixed_suffix_lower_exact"]==FIXED_SUFFIX_LOWER_EXACT
                and request["parameters"]["maximum_mathematical_stdout_bytes"]==STDOUT_LIMIT,
                "literal one new fixed-ring prefix102 body scope required")
        ledger=Prefix58Ledger(PROCESS_STARTED,ancestor_receipt={
            "source":copy.deepcopy(request["source"]),
            "source_records":copy.deepcopy(request["source_records"]),
            "last_closed_source":copy.deepcopy(request["paid_free_source"]),
            "last_closed_records":copy.deepcopy(request["paid_free_records"]),
            "ancestor_final_original_scientific_seconds":2974.589423877,
            "source_original_full_values":147,"closed_scope_not_reopened":True})
        report["request_identity"]={"path":args.request,"bytes":len(raw),"sha256":sha(raw)}
        report["source_files_sha256"]=copy.deepcopy(request["source_sha256"])
        emit("REQUEST",{"request_identity":report["request_identity"],"parameters":request["parameters"]})
        tick=time.monotonic();load_runtime()
        report["runtime_import_seconds"]=time.monotonic()-tick
        completed=read_source(request,ledger,capture=source_capture)
        prepared=prepare_source(request,Path(args.out),completed,ledger,process_started=PROCESS_STARTED)
        thetas={"coarse":prepared["theta"],"fine":prepared["fine_theta"]}
        report["source58_receipt"]=completed["receipt"]
        report["source58_point"]=completed["point"]
        report["fixed_complete_metric_sha256"]=request["fixed_complete_metric_sha256"]
        report["fixed_b0_definition_sha256"]=request["fixed_b0_definition_sha256"]
        report["configuration"]=copy.deepcopy(prepared["cfg"])
        report["full_value_sampling_definition"]=copy.deepcopy(prepared["grid"])
        require(float(completed["point"]["maximum_eta_on_both_grids"])==SOURCE_ETA
            and prepared["cfg"]["minimum_accepted_eta_decrease_exact"]==MINIMUM_DECREASE_EXACT,
            "original58 baseline eta and original decrease gate must remain")
        metric_budget=SOURCE_ETA-float(Q(MINIMUM_DECREASE_EXACT))
        report["metric_budget_for_new_fullbody_problem"]=metric_budget
        emit("INPUT",{"source58":completed["receipt"],"source_ancestor":completed["ancestor_cost_receipt"],
             "paid_free_source":request["paid_free_source"],"paid_free_records":request["paid_free_records"],
             "unaccepted_ring_record":completed["unaccepted_ring_record"],
             "new_metric_or_geometry_or_J_or_Pi_calls_before_body_input":0,
             "original_field_reconstruction":prepared["replay"]["source_input_restoration"],
             "source58_is_still_the_only_accepted_state":True,
             "missing_free36_prediction_arrays_must_be_paid_anew":True})
        metric_bound=new_fixed_metric(prepared,completed,ledger)
        report["fixed_metric_binding"]=copy.deepcopy(metric_bound["identity"])
        def charged(counter,metadata):
            ordinal=ledger.charge(counter)
            ledger.note(counter+"-started",ordinal=ordinal,**metadata)
            return {"counter":counter,"ordinal":ordinal,
                "started_scientific_seconds":ledger.elapsed(),
                "actual_elapsed_and_partial_status_recorded_by_model":True}
        event=ledger.begin("prefix102_model_builds",
            source_accepted_index=58,unaccepted_ring_candidate=True,
            fixed_suffix_lower_exact=FIXED_SUFFIX_LOWER_EXACT)
        try:
            model=build_fixed_ring_prefix102_model(
                prepared["field168"],prepared["q168"],completed["unaccepted_ring_state168"],
                prepared["radial"],thetas,metric_bound,prepared["cfg"],
                prepared["lower172"],prepared["upper172"],
                source_receipt=completed["receipt"],wall=ledger.check,capture=model_capture,
                metric_budget=metric_budget,
                original_pools={label:np.asarray(prepared[label+"_pool"],dtype=np.int64)
                                for label in LABELS},
                charge_prepare=lambda metadata:charged("new_body_input_preparations",metadata),
                charge_suffix=lambda metadata:charged("fixed_suffix_checks",metadata))
            ledger.end(event,model_binding_sha256=model.binding_sha256,
                model_status=model.status)
        except Exception as problem:
            if event["status"]=="started": ledger.end(event,problem)
            raise
        report["model_summary"]=model.summary()
        report["model_stdout_receipt"]=emit("MODEL",model.full_record())
        solve_event=None
        def charge_solve(metadata):
            nonlocal solve_event
            solve_event=ledger.begin("prefix102_solver_sessions",**metadata)
            return {key:solve_event[key] for key in ("counter","ordinal","started_scientific_seconds")}
        remaining=ledger.limits["science_seconds"]-ledger.check("before-new-prefix102-solve")
        solve=solve_fixed_ring_prefix102_once(
            model,wall=ledger.check,charge_solve=charge_solve,emit=emit,capture=solve_capture,
            solver_time_limit_seconds=min(SOLVER_TIME_LIMIT_SECONDS,remaining),
            maxiter=SOLVER_MAXITER,max_evaluations=MAX_COMPLETE_EVALUATIONS)
        qualified=bool(solve.get("qualified_candidate"))
        if solve_event is not None and solve_event["status"]=="started":
            ledger.end(solve_event,qualified=qualified,status_from_backend=solve.get("status"),
                raw_optimizer_return_is_in_NONLINEAR_RESULT=bool(
                    solve_capture.get("original_result_stdout_receipt")))
        report["solve_trace_stdout_receipt"]=emit("SOLVE_TRACE",
            fixed_ring_prefix102_capture_record(solve_capture,include_arrays=True))
        report["body_solution"]={"status":solve.get("status"),"qualified":qualified,
            "candidate_record":solve.get("candidate_record"),"report":solve.get("report")}
        report["body_solution_stdout_receipt"]=emit("BODY_SOLUTION",report["body_solution"])
        if qualified and solve.get("candidate168") is not None:
            candidate=np.asarray(solve["candidate168"],dtype=np.float64)
            prediction={"schema":POLICY+"-qualified-fullbody-model-prediction",
                "status":solve.get("status"),"qualified_for_original_actual":True,
                "model_binding_sha256":model.binding_sha256,
                "candidate_array_sha256":array_digest(candidate),
                "physical_state_sha256":digest(prepared["field168"].identity(candidate)),
                "source_accepted_index":58,"source_actual_eta":SOURCE_ETA,
                "minimum_accepted_eta_decrease_exact":MINIMUM_DECREASE_EXACT,
                "full_grid_summaries_are_retained_from_actual_paid_values":True,
                "full_grid_arrays_still_available_at_return":bool(
                    (solve.get("report") or {}).get("candidate_filter",{}).get("full_grid_arrays_still_available",False)),
                "full_grid_summaries":copy.deepcopy(
                    (solve.get("report") or {}).get("candidate_filter",{}).get(
                        "full_grid_summaries",report["model_summary"]["initial_full_grid_summaries"])),
                "no_arrays_recomputed_or_fabricated_for_a_returned_cached_point":True,
                "original_fourteen_gates_not_yet_evaluated":True}
            report["prediction_stdout_receipt"]=emit("PREDICTION",prediction)
            report["prediction"]=prediction
            actual=Prefix58Actual(prepared,completed,ledger)
            actual.trial(candidate,1.,prediction,emit=emit)
        else:
            report["actual_not_called_reason"]=(
                "fixed suffix excludes this prefix102 fiber" if
                model.status=="fixed-suffix-excludes-this-numerical-fiber" else
                "one prefix102 solve returned no complete wholebody-qualified rounded candidate")
        report["status"]="complete-true58-prefix102-observation"
    except Exception as problem:
        error=problem
        report.update(status="true58-prefix102-raised",error={
            "type":type(problem).__name__,"message":str(problem),
            "scope_kind":getattr(problem,"kind",None),"traceback":traceback.format_exc()})
    finally:
        if ledger is not None:
            for event in ledger.events:
                if event.get("status")=="started":
                    ledger.end(event,error or RuntimeError("owner exited with an unfinished scientific call"))
        report["source_input_progress"]=public_capture(source_capture)
        if "model_stdout_receipt" not in report and model_capture:
            try:
                report["model_partial_stdout_receipt"]=emit("MODEL_PARTIAL",
                    fixed_ring_prefix102_capture_record(model_capture,include_arrays=True))
            except Exception as reporting_error:
                report.setdefault("partial_reporting_errors",[]).append({
                    "tag":PREFIX+"MODEL_PARTIAL","type":type(reporting_error).__name__,
                    "message":str(reporting_error),"traceback":traceback.format_exc(),
                    "retry_or_substitute_payload_created":False})
                error=error or reporting_error
                report["status"]="true58-prefix102-partial-report-raised"
        if error is not None and solve_capture:
            try:
                report["solve_partial_stdout_receipt"]=emit("SOLVE_PARTIAL",
                    fixed_ring_prefix102_capture_record(solve_capture,include_arrays=True))
            except Exception as reporting_error:
                report.setdefault("partial_reporting_errors",[]).append({
                    "tag":PREFIX+"SOLVE_PARTIAL","type":type(reporting_error).__name__,
                    "message":str(reporting_error),"traceback":traceback.format_exc(),
                    "retry_or_substitute_payload_created":False})
                error=error or reporting_error
                report["status"]="true58-prefix102-partial-report-raised"
        if actual is not None:
            try:
                payload=actual.accepted_cache_payload()
                if payload is not None:
                    report["accepted_cache_stdout_receipt"]=emit("CACHE",payload)
            except Exception as export_error:
                report["accepted_cache_export_error"]={
                    "type":type(export_error).__name__,"message":str(export_error)}
                error=error or export_error
                report["status"]="true58-prefix102-accepted-cache-export-raised"
            report["actual_stage"]=actual.report()
            report["new_acceptances"]=report["actual_stage"]["new_acceptances"]
            report["selected_two_grid_physical_point"]=report["actual_stage"]["selected_two_grid_physical_point"]
        elif completed is not None:
            report["selected_two_grid_physical_point"]=completed["point"]
        report["new_current58_J_or_ordinary_baseline_replays"]=0
        report["main_readme_completion_claim"]=False
        report["ledger_before_complete_output"]=cost(ledger)
        report["peak_rss_kib_linux"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report["scientific_stdout_bytes_before_complete"]=STDOUT_BYTES
        report["final_clock_is_later_and_authoritative"]=True
    complete_receipt=emit("COMPLETE",report)
    final_cost=cost(ledger)
    exhausted=bool(final_cost.get("deadline_observed_exceeded",
                                 final_cost["scientific_seconds"]>=600))
    emit("FINAL_CLOCK",{"schema":POLICY+"-final-clock","earlier_COMPLETE_status":report["status"],
        "status_at_final_emit":("true58-prefix102-scope-exhausted" if exhausted else report["status"]),
        "scope_exhausted":exhausted,"ledger":final_cost,"complete_receipt":complete_receipt,
        "process_seconds":float(time.monotonic()-PROCESS_STARTED),
        "sampled_after_all_large_cache_and_complete_write_and_flush":True,
        "no_scientific_queries_follow_this_record":True})
    return 2 if error is not None or exhausted else 0

if __name__=="__main__":
    raise SystemExit(main())
