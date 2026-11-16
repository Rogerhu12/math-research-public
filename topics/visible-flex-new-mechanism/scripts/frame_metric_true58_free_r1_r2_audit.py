#!/usr/bin/env python3
"""One free R1/R2 curvature minimax problem; at most one original actual candidate."""
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

PREFIX="TRUE58_FREE_R1_R2_"
STDOUT_LIMIT=128*1024*1024
STDOUT_BYTES=0
np=None
POLICY="true58-free-R1-R2-original-box-curvature-minimax-v1"
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
def prediction_partial_record(capture):
    catalogue=[]
    seen={}
    def walk(value,path):
        if np is not None and isinstance(value,np.ndarray):
            catalogue.append({"path":path,"dtype":str(value.dtype),"shape":list(value.shape),
                "bytes":int(value.nbytes),"array_sha256":array_digest(value),"values_saved":False})
            return
        if isinstance(value,(dict,list,tuple)):
            if id(value) in seen:
                catalogue.append({"path":path,"same_retained_container_as":seen[id(value)]})
                return
            seen[id(value)]=path
            items=value.items() if isinstance(value,dict) else enumerate(value)
            for key,item in items: walk(item,path+"/"+str(key))
    walk(capture,"")
    return {"schema":POLICY+"-partial-prediction-observation",
        "result":capture.get("result"),"candidate_bounds":capture.get("candidate_bounds",{}),
        "metric_capture":ring17_capture_record(capture.get("metric_capture",{}),include_arrays=False),
        "curvature_capture":ring17_capture_record(capture.get("curvature_capture",{}),include_arrays=False),
        "actual_retained_array_metadata":catalogue,
        "partial_fullbody_array_values_saved":False,
        "partial_arrays_not_available_as_future_free_inputs":True,
        "no_zero_arrays_or_recomputed_values_substituted":True}
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
    global bind_current_168_first_jets,bind_current_168_curvature_metric
    global ActualCandidateMetricPredictor168,predict_current_168_curvature
    global build_free_R1_R2_model,solve_free_R1_R2_once,ring17_capture_record,Free58Actual
    global free_R1_R2_capture_record
    import numpy as np
    import scipy
    from frame_entry_body_subspace import array_digest
    from frame_height_null_coordinates import digest
    from frame_metric_true58_free_r1_r2_transfer import read_source,prepare as prepare_source
    from frame_complete_body_extension168_joint_selected import bind_current_168_first_jets
    from frame_complete_body_extension168_curvature_prediction import (
        bind_current_168_curvature_metric,predict_current_168_curvature)
    from frame_complete_body_extension168_nonlinear_metric_line import ActualCandidateMetricPredictor168
    from frame_metric_current168_ring17 import ring17_capture_record
    from frame_metric_current168_free_R1_R2 import (
        build_free_R1_R2_model,solve_free_R1_R2_once,free_R1_R2_capture_record)
    from frame_metric_true58_free_r1_r2_actual import Free58Actual
    require(sys.version_info[:3]==(3,12,14) and np.__version__=="2.3.5"
            and scipy.__version__=="1.17.0","unchanged pinned numerical runtime required")
    for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
        require(os.environ.get(key)=="1","one numerical thread required")

def cost(ledger):
    if ledger is not None:
        return ledger.report()
    elapsed=float(time.monotonic()-PROCESS_STARTED)
    return {"scientific_seconds":elapsed,"started_counts":{},
            "source_original_values_closed":147,"ancestor_scientific_seconds":2902.366570826,
            "total_ancestor_plus_new_scientific_seconds":2902.366570826+elapsed,
            "total_source_plus_new_started_values":147,"bootstrap_failure_before_ledger":True,
            "observed_overrun_seconds":max(0.,elapsed-600)}

def restored_first_jets(prepared,completed,ledger):
    field,state,r=prepared["field168"],prepared["q168"],prepared["radial"]
    thetas={"coarse":prepared["theta"],"fine":prepared["fine_theta"]}
    event=ledger.begin("fixed_metric_evaluations",source_accepted_index=58)
    try:
        metric=field.metric(state,r,jacobian=False)
        paid_source=completed["paid_ring_model"]["binding"]["source"]
        historical_metric_provenance={
            "kind":"same-frozen-g-radial-metric-for-actual58-ring17",
            "source":copy.deepcopy(paid_source["source_receipt"]),
            "fixed_g":completed["report"]["fixed_complete_metric_sha256"]}
        metric_bound=bind_current_168_curvature_metric(
            field,r,metric,historical_metric_provenance)
        require(metric_bound["binding_sha256"]==paid_source["fixed_metric_binding_sha256"],
                "the original paid fixed-metric identity and current a/a_s/a_ss must match")
        ledger.end(event,metric_binding_sha256=metric_bound["binding_sha256"],
            original_paid_metric_provenance_restored=True,
            current_task_source_receipt_sha256=digest(completed["receipt"]),
            current_metric_evaluation_is_a_new_charged_call=True)
    except Exception as error:
        if event["status"]=="started": ledger.end(event,error)
        raise
    bounds,records={},{}
    for label in LABELS:
        event=ledger.begin("paid_first_jet_bindings",grid=label,source_accepted_index=58)
        try:
            saved=completed["accepted_cache"]["grids"][label]
            data={key:np.asarray(saved[key]["values"],dtype=np.float64)
                  for key in ("U","T","e","f")}
            data["metric"]=metric_bound["data"]
            for key in ("U","T","e","f"):
                require(array_digest(data[key])==saved[key]["array_sha256"],
                        "literal accepted58 saved first jet differs: "+label+"/"+key)
                data[key].setflags(write=False)
            provenance={"kind":"original-accepted58-CACHE2-first-jets",
                "source_receipt":completed["receipt"],
                "source_cache_binding_sha256":completed["accepted_cache"]["binding_sha256"],
                "grid":label,"ordinary_geometry_replays":0,
                "full_grid_two_jets_and_current58_J_not_implied":True}
            bounds[label]=bind_current_168_first_jets(
                field,state,r,thetas[label],data,provenance,wall=ledger.check)
            records[label]={"identity":bounds[label]["identity"],
                "binding_sha256":bounds[label]["binding_sha256"],
                "binding_seconds":bounds[label]["binding_seconds"]}
            ledger.end(event,binding_sha256=bounds[label]["binding_sha256"])
        except Exception as error:
            if event["status"]=="started": ledger.end(event,error)
            raise
    return thetas,bounds,metric_bound,records

def predict_one(prepared,completed,candidate,candidate_record,first_bounds,thetas,
                metric_bound,ledger,capture):
    event=ledger.begin("nonlinear_candidate_predictions",
                       source_accepted_index=58,candidate_array_sha256=array_digest(candidate))
    capture.update(metric_capture={},curvature_capture={},candidate_bounds={})
    field,r,cfg=prepared["field168"],prepared["radial"],prepared["cfg"]
    q=field.validate_state(candidate)
    require(field.exact_full_box_decision(q,prepared["lower172"],prepared["upper172"])
            ["exact_full_box_pass"],"rounded ring candidate original172 box required")
    result={"schema":POLICY+"-one-rounded-candidate-prediction","status":"started",
        "source_accepted_index":58,"candidate168_binary64":q.tolist(),
        "candidate168_exact":[str(Q.from_float(float(x))) for x in q],
        "candidate_array_sha256":array_digest(q),
        "physical_state_sha256":digest(field.identity(q)),
        "ring_candidate_record":copy.deepcopy(candidate_record),
        "combined_exact_embedding_not_mislabelled_as_rounded_ring_neutrality":True,
        "original_fourteen_gates_not_evaluated_in_prediction":True}
    capture["result"]=result
    try:
        predictor=ActualCandidateMetricPredictor168(
            field,prepared["q168"],r,thetas,first_bounds,completed["receipt"],wall=ledger.check)
        predicted=predictor.predict(q,candidate_receipt={
            "kind":"one-final-rounded-free-R1-R2-candidate","source58":completed["receipt"],
            "candidate_array_sha256":array_digest(q),"candidate_record":candidate_record},
            capture=capture["metric_capture"])
        capture["_metric_result"]=predicted
        result["metric_prediction"]={"binding":predicted["binding"],
            "binding_sha256":predicted["binding_sha256"],"diagnostics":predicted["diagnostics"],
            "cumulative_report":predictor.report()}
        candidate_bounds={}
        for label in LABELS:
            data={key:predicted["grids"][label][key] for key in ("U","T","e","f")}
            data["metric"]=metric_bound["data"]
            provenance={"kind":"same-rounded-free-R1-R2-nonlinear-predicted-first-jets",
                "grid":label,"candidate_array_sha256":array_digest(q),
                "metric_prediction_binding_sha256":predicted["binding_sha256"],
                "not_an_original_actual_receipt":True}
            candidate_bounds[label]=bind_current_168_first_jets(
                field,q,r,thetas[label],data,provenance,wall=ledger.check)
            capture["candidate_bounds"][label]={
                "identity":candidate_bounds[label]["identity"],
                "binding_sha256":candidate_bounds[label]["binding_sha256"],
                "binding_seconds":candidate_bounds[label]["binding_seconds"]}
        curvature=predict_current_168_curvature(
            field,q,r,thetas,candidate_bounds,metric_bound,cfg,
            source_receipt={"kind":"same-rounded-free-R1-R2-full-body-curvature-prediction",
                "source58":completed["receipt"],"candidate_array_sha256":array_digest(q),
                "metric_prediction_binding_sha256":predicted["binding_sha256"]},
            wall=ledger.check,capture=capture["curvature_capture"])
        capture["_curvature_result"]=curvature
        result["candidate_first_jet_bindings"]=capture["candidate_bounds"]
        result["curvature_prediction"]={"binding":curvature["binding"],
            "binding_sha256":curvature["binding_sha256"],
            "diagnostics":curvature["diagnostics"],
            "grids":{label:{"identity":curvature["grids"][label]["identity"],
                "binding_sha256":curvature["grids"][label]["binding_sha256"],
                "summary":curvature["grids"][label]["summary"]} for label in LABELS}}
        eta=float(predicted["diagnostics"]["two_grid_predicted_eta"])
        source_eta=float(completed["point"]["maximum_eta_on_both_grids"])
        minimum=float(Q(cfg["minimum_accepted_eta_decrease_exact"]))
        curved=all(curvature["grids"][label]["summary"]["predictor_PSD_with_original_tolerance"]
                   and curvature["grids"][label]["summary"]["predictor_direct_cap_with_original_tolerance"]
                   for label in LABELS)
        result.update(status="complete",predicted_eta=eta,
            source58_actual_eta=source_eta,predicted_eta_decrease=source_eta-eta,
            minimum_original_decrease=minimum,predicted_original_curvature_pass=bool(curved),
            qualified_for_original_actual=bool(curved and eta<source_eta and source_eta-eta>=minimum),
            large_predictor_arrays_not_saved_as_future_free_inputs=True,
            prediction_scope="one same R1+R2 rounded168 candidate, original complete two grids")
        ledger.end(event,qualified=result["qualified_for_original_actual"],predicted_eta=eta)
        return result
    except Exception as error:
        result.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
        if event["status"]=="started": ledger.end(event,error)
        raise

def main():
    global require
    parser=argparse.ArgumentParser()
    parser.add_argument("--request",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    ledger=None;completed=None;prepared=None;model=None;actual=None
    source_capture={};model_capture={};solve_capture={};prediction_capture={}
    report={"schema":POLICY+"-complete","status":"started","github_repository":
        os.environ.get("GITHUB_REPOSITORY"),"github_sha":os.environ.get("GITHUB_SHA"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"new_acceptances":0,
        "main_readme_completion_claim":False,"old_checks_executed":0,"new_development_executed":0}
    error=None
    try:
        from frame_metric_true58_free_r1_r2_scope import (
            Free58Ledger,require,LIMITS,SOLVER_TIME_LIMIT_SECONDS,SOLVER_MAXITER,
            MAX_COMPLETE_EVALUATIONS,K_BOUNDS_EXACT,INITIAL_K_EXACT,NORM_REGULARIZATION_EXACT,SOLVER_OPTIONS,
            TARGET_EXACT,RING_INDEX,METRIC_BUDGET)
        raw=Path(args.request).read_bytes();request=json.loads(raw)
        require(request["parameters"]["policy"]==POLICY
                and request["parameters"]["limits"]==LIMITS
                and request["parameters"]["target_exact"]==TARGET_EXACT
                and request["parameters"]["ring_index"]==RING_INDEX
                and request["parameters"]["maximum_h_exact"] is None
                and request["parameters"]["solver_time_limit_seconds"]==SOLVER_TIME_LIMIT_SECONDS
                and request["parameters"]["solver_maxiter"]==SOLVER_MAXITER
                and request["parameters"]["maximum_complete_evaluations"]==MAX_COMPLETE_EVALUATIONS
                and request["parameters"]["metric_budget_binary64"]==METRIC_BUDGET
                and tuple(request["parameters"]["K_bounds_exact"])==K_BOUNDS_EXACT
                and request["parameters"]["initial_K_exact"]==INITIAL_K_EXACT
                and request["parameters"]["norm_regularization_exact"]==NORM_REGULARIZATION_EXACT
                and request["parameters"]["solver_options"]==SOLVER_OPTIONS,
                "literal one new free R1/R2 scope required")
        ledger=Free58Ledger(PROCESS_STARTED,ancestor_receipt={
            "source":copy.deepcopy(request["source"]),
            "source_records":copy.deepcopy(request["source_records"]),
            "last_closed_source":copy.deepcopy(request["paid_joint_source"]),
            "last_closed_records":copy.deepcopy(request["paid_joint_records"]),
            "ancestor_final_original_scientific_seconds":2902.366570826,
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
        emit("INPUT",{"source58":completed["receipt"],"source_ancestor":completed["ancestor_cost_receipt"],
             "paid_ring_source":request["paid_ring_source"],"paid_ring_records":request["paid_ring_records"],
             "paid_reflection_source":request["paid_reflection_source"],
             "paid_reflection_records":request["paid_reflection_records"],
             "paid_joint_source":request["paid_joint_source"],
             "paid_joint_records":request["paid_joint_records"],
             "paid_ring_metric":completed["receipt"]["paid_ring_metric"],
             "new_metric_or_geometry_or_J_or_Pi_calls_before_free_model":0,
             "original_field_reconstruction":prepared["replay"]["source_input_restoration"],
             "full_baseline_arrays_remain_in_the_bound_original58_CACHE2":True})
        require(completed["paid_ring_model"]["binding"]["source"]["ring_radial_index"]==RING_INDEX,
                "the paid model must use the original radial row")
        require(float(completed["point"]["maximum_eta_on_both_grids"])==METRIC_BUDGET,
                "the R1 budget is the current original two-grid eta, not the .26 target")
        def charge_primitive_batch(metadata):
            ordinal=ledger.charge("new_complete_primitive_batches")
            start=ledger.elapsed()
            ledger.note("new-complete-Pi-batch-started",ordinal=ordinal,**metadata)
            return {"counter":"new_complete_primitive_batches","ordinal":ordinal,
                    "started_scientific_seconds":start,
                    "actual_elapsed_and_partial_status_recorded_by_model":True}
        event=ledger.begin("free_R1_R2_model_builds",ring_index=RING_INDEX,target_exact=TARGET_EXACT)
        try:
            model=build_free_R1_R2_model(
                prepared["field168"],prepared["q168"],completed["paid_ring_model"],
                completed["paid_reflected_model"],prepared["cfg"],
                prepared["lower172"],prepared["upper172"],
                source_receipt=completed["receipt"],wall=ledger.check,capture=model_capture,
                metric_budget=METRIC_BUDGET,target_exact=TARGET_EXACT,
                charge_primitive_batch=charge_primitive_batch)
            ledger.end(event,model_binding_sha256=model.binding_sha256)
        except Exception as problem:
            if event["status"]=="started": ledger.end(event,problem)
            raise
        report["model_summary"]=model.summary()
        report["model_stdout_receipt"]=emit("MODEL",model.full_record())
        solve_event=None
        def charge_solve(metadata):
            nonlocal solve_event
            solve_event=ledger.begin("free_R1_R2_solver_sessions",**metadata)
            return {key:solve_event[key] for key in ("counter","ordinal","started_scientific_seconds")}
        remaining=ledger.limits["science_seconds"]-ledger.check("before-new-free-R1-R2")
        solve=solve_free_R1_R2_once(
            model,wall=ledger.check,charge_solve=charge_solve,emit=emit,capture=solve_capture,
            solver_time_limit_seconds=min(SOLVER_TIME_LIMIT_SECONDS,remaining),
            maxiter=SOLVER_MAXITER,max_evaluations=MAX_COMPLETE_EVALUATIONS)
        qualified=bool(solve.get("qualified_candidate"))
        if solve_event is not None and solve_event["status"]=="started":
            ledger.end(solve_event,qualified=qualified,status_from_backend=solve.get("status"),
                raw_optimizer_return_is_in_NONLINEAR_RESULT=bool(
                    solve_capture.get("original_result_stdout_receipt")))
        report["solve_trace_stdout_receipt"]=emit("SOLVE_TRACE",
            free_R1_R2_capture_record(solve_capture,include_arrays=True))
        report["ring_solution"]={"status":solve.get("status"),"qualified":qualified,
            "candidate_record":solve.get("candidate_record"),"report":solve.get("report")}
        report["ring_solution_stdout_receipt"]=emit("RING_SOLUTION",report["ring_solution"])
        if qualified and solve.get("candidate168") is not None:
            candidate=np.asarray(solve["candidate168"],dtype=np.float64)
            thetas,first_bounds,metric_bound,first_records=restored_first_jets(prepared,completed,ledger)
            report["prediction_input_bindings"]={"first_jet_bindings":first_records,
                "metric_binding":metric_bound["identity"],"only_built_after_new_free_candidate":True}
            prediction=predict_one(prepared,completed,candidate,solve["candidate_record"],
                first_bounds,thetas,metric_bound,ledger,prediction_capture)
            report["prediction_stdout_receipt"]=emit("PREDICTION",prediction)
            report["prediction"]={key:prediction[key] for key in (
                "status","candidate_array_sha256","physical_state_sha256","predicted_eta",
                "predicted_eta_decrease","predicted_original_curvature_pass","qualified_for_original_actual")}
            if prediction["qualified_for_original_actual"]:
                actual=Free58Actual(prepared,completed,ledger)
                actual.trial(candidate,1.,prediction,emit=emit)
            else:
                report["actual_not_called_reason"]="one complete rounded candidate failed original prediction qualification"
        else:
            report["actual_not_called_reason"]="the one free R1/R2 local solver returned no qualified rounded candidate"
        report["status"]="complete-true58-free-r1-r2-observation"
    except Exception as problem:
        error=problem
        report.update(status="true58-free-r1-r2-raised",error={
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
                report["model_partial_stdout_receipt"]=emit("MODEL_PARTIAL",free_R1_R2_capture_record(model_capture,include_arrays=True))
            except Exception as reporting_error:
                report.setdefault("partial_reporting_errors",[]).append({
                    "tag":PREFIX+"MODEL_PARTIAL","type":type(reporting_error).__name__,
                    "message":str(reporting_error),"traceback":traceback.format_exc(),
                    "retry_or_substitute_payload_created":False})
                error=error or reporting_error
                report["status"]="true58-free-r1-r2-partial-report-raised"
        if error is not None and solve_capture:
            try:
                report["solve_partial_stdout_receipt"]=emit("SOLVE_PARTIAL",free_R1_R2_capture_record(solve_capture,include_arrays=True))
            except Exception as reporting_error:
                report.setdefault("partial_reporting_errors",[]).append({
                    "tag":PREFIX+"SOLVE_PARTIAL","type":type(reporting_error).__name__,
                    "message":str(reporting_error),"traceback":traceback.format_exc(),
                    "retry_or_substitute_payload_created":False})
                error=error or reporting_error
                report["status"]="true58-free-r1-r2-partial-report-raised"
        if error is not None and prediction_capture:
            try:
                report["prediction_partial_stdout_receipt"]=emit("PREDICTION_PARTIAL",prediction_partial_record(prediction_capture))
            except Exception as reporting_error:
                report.setdefault("partial_reporting_errors",[]).append({
                    "tag":PREFIX+"PREDICTION_PARTIAL","type":type(reporting_error).__name__,
                    "message":str(reporting_error),"traceback":traceback.format_exc(),
                    "retry_or_substitute_payload_created":False})
                error=error or reporting_error
                report["status"]="true58-free-r1-r2-partial-report-raised"
        if actual is not None:
            try:
                payload=actual.accepted_cache_payload()
                if payload is not None:
                    report["accepted_cache_stdout_receipt"]=emit("CACHE",payload)
            except Exception as export_error:
                report["accepted_cache_export_error"]={
                    "type":type(export_error).__name__,"message":str(export_error)}
                error=error or export_error
                report["status"]="true58-free-r1-r2-accepted-cache-export-raised"
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
    # If stdout itself breaks, neither this record nor FINAL_CLOCK can be
    # guaranteed.  No output retry or made-up terminal receipt is installed.
    complete_receipt=emit("COMPLETE",report)
    final_cost=cost(ledger)
    exhausted=bool(final_cost.get("deadline_observed_exceeded",
                                 final_cost["scientific_seconds"]>=600))
    emit("FINAL_CLOCK",{"schema":POLICY+"-final-clock","earlier_COMPLETE_status":report["status"],
        "status_at_final_emit":("true58-free-r1-r2-scope-exhausted" if exhausted else report["status"]),
        "scope_exhausted":exhausted,"ledger":final_cost,"complete_receipt":complete_receipt,
        "process_seconds":float(time.monotonic()-PROCESS_STARTED),
        "sampled_after_all_large_cache_and_complete_write_and_flush":True,
        "no_scientific_queries_follow_this_record":True})
    return 2 if error is not None or exhausted else 0

if __name__=="__main__":
    raise SystemExit(main())

