#!/usr/bin/env python3
"""Solve strictly augmented original-row problems, then original line and actual gates."""
from __future__ import annotations
import time
PROCESS_STARTED=time.monotonic()
import argparse
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import traceback
from frame_metric_true53_augmented_scope import (
    POLICY, LIMITS, AugmentedDirectionLedger, AugmentedDirectionLimit, require,
    SOURCE_PHYSICAL_SHA, SOURCE_ACCEPTED_INDEX, SOURCE_GLOBAL_SECONDS,
    SOURCE_ORIGINAL_VALUES)

TOPIC="topics/visible-flex-new-mechanism"
REPO="Rogerhu12/math-research-public"
SCHEMA=POLICY+"-audit"
TAG="TRUE53_AUGMENTED_"
STAGE="augmented_direction_actual_stage"
COMPLETE="complete-augmented-master-full-grid-and-original-actual-observation"
MAX_MATH_STDOUT_BYTES=96*1024*1024
NEW_SOURCES=(
    "frame_metric_true53_augmented_scope.py",
    "frame_metric_true53_augmented_core.py",
    "frame_metric_true53_augmented_master.py",
    "frame_metric_true53_augmented_domain.py",
    "frame_metric_true53_augmented_first_jets.py",
    "frame_metric_true53_augmented_line.py",
    "frame_metric_true53_augmented_actual.py",
    "frame_metric_true53_augmented_transfer.py",
    "frame_metric_true53_augmented_accepted_cache.py",
    "frame_metric_true53_augmented_audit.py",
    "frame_metric_true53_augmented_report.py",
)
STDOUT_BYTES=0

def load_runtime():
    global np,digest,exact_vector,array_digest,vector_record,EvaluationBudgetReached
    global original_audit,AugmentedDirectionObjective,run_augmented_direction_actual_trials
    global AugmentedFirstJets,AugmentedOriginalDomain,run_guarded_line
    global read_sources,prepare_augmented,SOURCE,PINS
    global extract_accepted_first_jet_cache,AugmentedMaster,exchange_directions
    import numpy as np
    from frame_height_null_coordinates import digest
    from frame_curvature_soc_metric_reserve_audit import exact_vector
    from frame_entry_body_subspace import array_digest
    from frame_metric_true53_paid_master_input import vector_record
    from frame_metric_budget_recovery import EvaluationBudgetReached
    import frame_metric_final_cone32_audit as original_audit
    from frame_metric_true53_augmented_actual import (
        AugmentedDirectionObjective,run_augmented_direction_actual_trials)
    from frame_metric_true53_augmented_first_jets import AugmentedFirstJets
    from frame_metric_true53_augmented_domain import AugmentedOriginalDomain
    from frame_metric_true53_augmented_line import run_guarded_line
    from frame_metric_true53_augmented_transfer import read_sources,prepare_augmented,SOURCE
    from frame_metric_true53_augmented_accepted_cache import extract_accepted_first_jet_cache
    from frame_metric_true53_augmented_master import AugmentedMaster,exchange_directions
    PINS=copy.deepcopy(SOURCE)

def encoded(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,
                      allow_nan=False).encode("utf-8")

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

def emit(suffix,value):
    global STDOUT_BYTES
    raw=encoded(jsonable(value))
    line=(TAG+suffix+" ").encode()+raw+b"\n"
    reserve=0 if suffix in ("FINAL_CLOCK","REPORTING_ERROR") else 131072
    require(STDOUT_BYTES+len(line)+reserve<=MAX_MATH_STDOUT_BYTES,
            "the original mathematical stdout allocation is exhausted")
    sys.stdout.buffer.write(line)
    sys.stdout.buffer.flush()
    STDOUT_BYTES+=len(line)
    return {"tag":TAG+suffix,"JSON_plus_LF_bytes":len(raw)+1,
            "JSON_plus_LF_sha256":hashlib.sha256(raw+b"\n").hexdigest()}

def implementation_hashes(request):
    result={}
    for path,expected in request["source_sha256"].items():
        observed=hashlib.sha256(Path(path).read_bytes()).hexdigest()
        require(observed==expected,"requested source changed: "+path)
        result[path]=observed
    return result

def compact_capture(capture):
    return jsonable({key:value for key,value in capture.items() if not key.startswith("_")})

def array_record(value):
    a=np.asarray(value,dtype=np.float64)
    require(np.all(np.isfinite(a)),"finite paid/new cache array required")
    return {"dtype":"float64","shape":list(a.shape),"array_sha256":array_digest(a),
            "values":a.tolist()}

def compact_scan(scan):
    out={key:copy.deepcopy(value) for key,value in scan.items()
         if key not in ("arrays","direction")}
    out["actual_direction"]=vector_record(scan["direction"])
    out["array_sha256"]={label:{name:array_digest(value)
                               for name,value in arrays.items()}
                          for label,arrays in scan["arrays"].items()}
    return jsonable(out)

def publish_cache(jets,scan,report,*,line_payload=None):
    """Only new completed direction coefficients, or the one qualified line.

    U/T and source e/f are already paid in the pinned source logs and are not
    duplicated.  A newly accepted physical point has its own second CACHE.
    """
    require(not report["cache_emission_attempted"],"one final-direction cache publication only")
    report["cache_emission_attempted"]=True
    tick=time.monotonic()
    try:
        arrays={}
        if line_payload is None and scan is not None:
            for label in ("coarse","fine"):
                for key in ("de","df"):
                    arrays[scan["direction_sha256"]+"/"+label+"/"+key]=array_record(scan["arrays"][label][key])
        partial_arrays={}
        partial_key=getattr(jets,"_last_attempt_key",None)
        if jets is not None and partial_key is not None and partial_key not in jets.scans:
            partial_arrays={key:array_record(value) for key,value in
                            jets.cache_arrays(include_partial=True).items()}
        payload={
            "schema":POLICY+"-new-final-direction-cache",
            "source_physical_state_sha256":SOURCE_PHYSICAL_SHA,
            "source_model_binding_sha256":getattr(jets,"model_binding_sha256",None),
            "source_paid_U_T_cache":copy.deepcopy(PINS),
            "first_jet_input_binding_sha256":getattr(jets,"binding_sha256",None),
            "first_jet_input_binding":copy.deepcopy(getattr(jets,"binding",None)),
            "direction_sha256":None if scan is None else scan["direction_sha256"],
            "binary64_round_trip_arrays":arrays,"line_cache":line_payload,
            "last_failed_direction_completed_arrays":partial_arrays,
            "last_failed_direction_sha256":partial_key if partial_arrays else None,
            "source_U_T_and_e_f_reused_not_duplicated":True,
            "all_new_cuts_are_separate_original_ATTAINER_GRADIENT_records":True,
            "closed_unqualified_scans_are_not_replayed":True,
            "partial":scan is None}
        receipt=emit("CACHE",payload)
        receipt.update(
            binding_sha256=line_payload["binding_sha256"] if line_payload is not None
                else getattr(jets,"binding_sha256",None),
            first_jet_input_binding_sha256=getattr(jets,"binding_sha256",None),
            direction_sha256=None if scan is None else scan["direction_sha256"],
            complete=scan is not None,original_plain_stdout_only=True)
        report["line_cache_stdout_receipt"]=receipt
        return receipt
    except Exception as error:
        report["cache_emission_error"]={"type":type(error).__name__,"message":str(error)}
        raise
    finally:
        report["timing_segments"]["new_cache_serialization_stdout_seconds"]=time.monotonic()-tick

def selected_receipts(point, stage, completed):
    if point["accepted_index"] == SOURCE_ACCEPTED_INDEX:
        require(point["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
                "unchanged source53 has another physical identity")
        return (copy.deepcopy(completed["gates"]["coarse"]), copy.deepcopy(completed["gates"]["fine"]),
                {"kind": "source53-paid-original-two-grid-gates", "new_geometry_replays": 0})
    found = [trial for trial in stage.get("trials", [])
             if trial.get("accepted_as_next_iterate") is True
             and trial.get("accepted_index") == point["accepted_index"]
             and trial.get("physical_state_sha256") == point["physical_state_sha256"]]
    require(point["accepted_index"] == 54 and len(found) == 1,
            "only one actually accepted new54 can replace source53")
    trial = found[0]
    return (copy.deepcopy(trial["coarse_decision"]), copy.deepcopy(trial["fine_decision"]),
            {"kind": "new-augmented-direction-actual-two-grid-trial", "trial_number": trial["number"],
             "model_query_number": trial["model_query_number"]})


def future_checkpoint(prepared, completed, objective, point, report, ledger):
    cp = copy.deepcopy(completed["checkpoint"])
    cp.update(
        schema=POLICY+"-future-direct-checkpoint",
        selected_accepted_index=point["accepted_index"],
        selected_physical_state_sha256=point["physical_state_sha256"],
        selected_two_grid_physical_point=copy.deepcopy(point),
        selected_final159_binary64_exact=copy.deepcopy(point["exact_binary64_independent_coordinates"]),
        selected_final163_physical_exact=copy.deepcopy(point["exact_original_physical_coefficients"]),
        coarse_pool=objective.pool.tolist(), fine_pool=objective.fine_pool.tolist(),
        coarse_pool_version=objective.pool_version, fine_pool_version=objective.fine_pool_version,
        coarse_pool_history=copy.deepcopy(objective.pool_history),
        fine_pool_history=copy.deepcopy(objective.fine_pool_history),
        objective_evaluation_definition=copy.deepcopy(objective.evaluation_definition),
        objective_evaluation_sha256=objective.evaluation_sha256,
        source_previous_objective_evaluation_sha256=completed["checkpoint"]["objective_evaluation_sha256"],
        cumulative_original_actual_values=objective.value_account()["total_source_plus_new_started_values"],
        cumulative_original_scientific_elapsed_seconds_at_checkpoint=SOURCE_GLOBAL_SECONDS+ledger.elapsed(),
        augmented_direction_method_scientific_elapsed_seconds_at_checkpoint=ledger.elapsed(),
        final_FINAL_CLOCK_record_is_later_and_authoritative_for_future_cost=True)
    cp["augmented_direction_method"] = {
        "policy": POLICY, "source": copy.deepcopy(PINS),
        "current_model_stdout_receipt": copy.deepcopy(report.get("first_jet_input_stdout_receipt")),
        "line_cache_receipt": copy.deepcopy(report.get("line_cache_stdout_receipt")),
        "new_accepted_first_jet_cache_receipt": copy.deepcopy(report.get("accepted_cache_stdout_receipt")),
        "source_model_base_physical_state_sha256": SOURCE_PHYSICAL_SHA,
        "complete_direction_original_record": copy.deepcopy(report.get("complete_direction_stdout_receipt")),
        "scalar_optimization_original_record": copy.deepcopy(report.get("scalar_result_stdout_receipt")),
        "full_direction_and_scalar_records_are_in_same_original_stdout": True,
        "source32_and64_permanently_closed": True,
        "ancestor_original_scientific_seconds": SOURCE_GLOBAL_SECONDS,
        "current_ledger_at_checkpoint": ledger.report(),
        "augmented_problem_receipts": [v["original_result_receipt"] for v in report.get("augmented_master",{}).get("attempted_problems",[])],
        "new_gradient_receipts": [v["original_record_receipt"] for v in report.get("exchange_progress",{}).get("new_gradient_records",[])],
        "new_method_is_not_source52_affine_or_scalar53_identity": True,
        "passive_bank_gamma_supplemental_and_controller_records_not_retrained": True,
        "future_model_must_explicitly_rebind_its_context": True}
    original = completed["checkpoint"]
    passive = ("norm_direction_bank_context", "norm_direction_bank_counters",
               "norm_direction_bank_entries", "norm_direction_bank_state_sha256",
               "curvature_defect_guard_learning_checkpoint", "all_retained_supplemental_normals",
               "terminal_trust", "terminal_success_streak", "terminal_covered_ordinary_growth_streak")
    require(all(cp[key] == original[key] for key in passive),
            "a passive source bank/learning/controller record changed")
    return cp


def finish_physical_report(prepared, completed, objective, report, ledger):
    problem, gate = prepared["problem"], prepared["gate"]
    stage = report.get(STAGE) or {
        "status": "no-actual-trial-started", "trials": [], "new_acceptances": 0,
        "selected_two_grid_physical_point": copy.deepcopy(objective.accepted_iterates[-1])}
    report[STAGE] = stage
    point = copy.deepcopy(objective.accepted_iterates[-1])
    state = exact_vector(point["exact_binary64_independent_coordinates"], 159)
    require(np.array_equal(state, np.asarray(point["independent_coordinates_binary64"], float))
            and digest(problem.identity(state)) == point["physical_state_sha256"]
            and [str(v) for v in problem.coordinates.physical_exact(state)]
                == point["exact_original_physical_coefficients"],
            "final exact159/physical163 identities differ")
    box = problem.coordinates.exact_box_decision(state, gate.original_lower, gate.original_upper)
    require(box["exact_original_box_pass"] is True, "final original exact163 box failed")
    copied, same = problem.frozen_metric_copy(state)
    require(copied is problem and same.tobytes() == state.tobytes()
            and copied.metric_model(state) == problem.metric_model(prepared["initial"])
            and copied.height_base_definition == problem.height_base_definition,
            "original g/b0/permanent anchor changed")
    coarse, fine, owner = selected_receipts(point, stage, completed)
    flags = {label: value["actual_gate_booleans"]
             for label, value in (("coarse", coarse), ("fine", fine))}
    require(all(len(v) == 14 and all(x is True for x in v.values()) for v in flags.values())
            and all(value["direct_max_eta"] == point[label]["direct_max_eta"]
                    for label, value in (("coarse", coarse), ("fine", fine))),
            "final14 actual gates and their true physical point must agree")
    report.update(
        selected_two_grid_physical_point=point,
        final_full_grid_constraints=coarse, final_doubled_constraints=fine,
        final_actual_gate_booleans=flags, final_exact_box=box,
        selected_gate_receipt_source=owner,
        final_selection_validation={
            "accepted_index": point["accepted_index"],
            "physical_state_sha256": point["physical_state_sha256"],
            "both_grid_maximum_eta": point["maximum_eta_on_both_grids"],
            "both_grid_maximum_curvature": point["maximum_curvature_on_both_grids"],
            "source_eta": completed["point"]["maximum_eta_on_both_grids"],
            "actual_eta_decrease": completed["point"]["maximum_eta_on_both_grids"]-point["maximum_eta_on_both_grids"],
            "all_original14_gates_and_exact_box_pass": True,
            "new_target_qualified_on_both_grids": point["new_metric_target_qualified_on_both_grids"],
            "new_independent_initial_or_final_geometry_calls": 0},
        actual_value_account=objective.value_account(),
        actual_value_events=copy.deepcopy(objective.actual_value_events),
        execution_receipt=objective.execution_receipt(),
        direct_reference_geometry_timing=problem.timing_snapshot())
    report["future_augmented_direction_checkpoint"] = future_checkpoint(
        prepared, completed, objective, point, report, ledger)
    old = completed["checkpoint"]
    report["terminal_information_state"] = {
        "pool_counts": [len(objective.pool), len(objective.fine_pool)],
        "pool_versions": [objective.pool_version, objective.fine_pool_version],
        "bank_entries": len(old["norm_direction_bank_entries"]),
        "bank_state_sha256": old["norm_direction_bank_state_sha256"],
        "learning_state_sha256": old["curvature_defect_guard_learning_checkpoint"]["state_sha256"],
        "learning_events": len(old["curvature_defect_guard_learning_checkpoint"]["events"]),
        "learning_commits": len(old["curvature_defect_guard_learning_checkpoint"]["commits"]),
        "learning_pending": len(old["curvature_defect_guard_learning_checkpoint"]["pending_event_indices"]),
        "passive_state_unchanged": True, "trust": old["terminal_trust"],
        "legacy_streak": old["terminal_success_streak"],
        "covered_streak": old["terminal_covered_ordinary_growth_streak"]}



def cost_snapshot(ledger,objective):
    cost=ledger.report()
    account=objective.value_account() if objective is not None else {
        "source_original_values_closed":SOURCE_ORIGINAL_VALUES,
        "source_scientific_seconds_closed":SOURCE_GLOBAL_SECONDS,
        "necessary_model_geometry_calls_started":0,
        "new_actual_geometry_calls_started":0,
        "new_adapter_geometry_calls_started":0,
        "total_source_plus_new_started_values":SOURCE_ORIGINAL_VALUES}
    cost.update(
        value_account=account,
        total_source_plus_new_started_values=account["total_source_plus_new_started_values"],
        old_HiGHS_calls_closed=64,old_cone_calls_closed=32,
        old_Hildreth_observation_closed=True,
        one_paid_finite_LP_34_iterations_68_systems_closed=True,
        new_finite_LP_calls=ledger.counts['finite_master_calls'],new_selected_hard_J_calls=0,
        new_source_base_ordinary_values=0,new_development_calls=0,
        all_started_failed_calls_inputs_imports_and_output_in_same_clock=True,
        observed_time_not_clipped_to600=True)
    return cost

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==REPO,
            "only this public repository Actions may execute the research")
    root=Path(__file__).resolve().parents[3]
    output=Path(args.out).resolve()
    require(output!=root and root not in output.parents,
            "machine output belongs only to runner temporary storage")
    output.parent.mkdir(parents=True,exist_ok=True)
    ledger=AugmentedDirectionLedger(PROCESS_STARTED)
    report={
        "schema":SCHEMA,"status":"new-four-cut-exchange-not-yet-started",
        "github_repository":REPO,"github_sha":os.environ.get("GITHUB_SHA"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "timing_segments":{},"cache_emission_attempted":False,
        "new_attainer_gradients":[],"scalar_optimization":None,
        "old_checks_executed":0,"new_development_executed":0,
        "old_finite_LP_selected_J_base_geometry_reexecuted":False,
        "source_original_values_closed":SOURCE_ORIGINAL_VALUES,
        "source_scientific_seconds_closed":SOURCE_GLOBAL_SECONDS,
        "complete_grid_or_actual_descent_not_inferred_from_finite_gain":True}
    sources=prepared=objective=domain=jets=scan=handle=envelope=completed=master=None
    input_capture={}
    jet_capture={}
    exchange_progress={}
    runtime_loaded=False
    try:
        ledger.check()
        request_path=Path(args.request).resolve()
        require(root in request_path.parents,"request belongs to the pinned checkout")
        raw_request=request_path.read_bytes()
        require(len(raw_request)<100000,"one small source/parameter request required")
        request=json.loads(raw_request)
        params=request["parameters"]
        require(params["policy"]==POLICY and params["limits"]==LIMITS
                and params["old_checks_executed"]==params["new_development_executed"]==0
                and params["source_original_actual_values"]==SOURCE_ORIGINAL_VALUES
                and params["ancestor_final_original_scientific_seconds"]==SOURCE_GLOBAL_SECONDS
                and params["maximum_mathematical_stdout_bytes"]==MAX_MATH_STDOUT_BYTES
                and params["seed_original_rows"]==[
                    ["coarse",43322],["coarse",91304],["fine",86645],["fine",182607]],
                "one new augmented scope and whole closed ancestor account required")
        require(request["new_python_sources"]==[TOPIC+"/scripts/"+n for n in NEW_SOURCES],
                "all and only the eleven new production/input/report modules required")
        report["source_files_sha256"]=implementation_hashes(request)
        report["request_identity"]={"bytes":len(raw_request),
                                    "sha256":hashlib.sha256(raw_request).hexdigest()}
        emit("INPUT",{"kind":"bound-request","request_identity":report["request_identity"],
                      "source_files_sha256":report["source_files_sha256"],"parameters":params})
        tick=time.monotonic()
        try:
            load_runtime()
            runtime_loaded=True
        finally:
            report["timing_segments"]["original_imports_seconds"]=time.monotonic()-tick
        tick=time.monotonic()
        try:
            sources=read_sources(request,ledger,capture=input_capture)
        finally:
            report["timing_segments"]["two_paid_source_logs_seconds"]=time.monotonic()-tick
        paid_model=sources["model"]
        completed=sources["prepared_source"]
        receipt=sources["receipt"]
        report["paid_source_receipt"]=copy.deepcopy(receipt)
        emit("INPUT",{"kind":"paid-model-and-new-four-cut-cache","receipt":receipt})
        tick=time.monotonic()
        try:
            prepared=prepare_augmented(
                request,output,sources,ledger,process_started=PROCESS_STARTED)
        finally:
            report["timing_segments"]["original24_input_prepare_seconds"]=time.monotonic()-tick
        report.update(
            configuration=copy.deepcopy(prepared["cfg"]),
            exact_input_storage_metadata=original_audit.frozen.metadata(prepared["bindings"]),
            source_transfer=copy.deepcopy(prepared["replay"]["source_input_restoration"]),
            full_value_sampling_definition=copy.deepcopy(prepared["grid"]),
            source_current_point=copy.deepcopy(completed["point"]))
        tick=time.monotonic()
        try:
            objective=AugmentedDirectionObjective(
                prepared["problem"],prepared["gate"],prepared["radial"],prepared["theta"],
                prepared["order"],prepared["lower"],prepared["upper"],
                cfg=prepared["cfg"],checkpoint=None,
                radial_nodes_exact=prepared["grid"]["radial_nodes_exact"],
                replay=prepared["replay"],ledger=ledger,
                coarse_pool=prepared["coarse_pool"],fine_pool=prepared["fine_pool"])
            domain=AugmentedOriginalDomain(prepared,paid_model,ledger)
            master=AugmentedMaster(paid_model,sources["seed_cuts"],ledger)
        finally:
            report["timing_segments"]["original-domain-new-master-objective_seconds"]=time.monotonic()-tick
        emit("MASTER_INPUT",{
            "original_model_assembly":master.original_receipt,
            "four_paid_original_rows_added_before_first_solve":master.extra,
            "first_problem_row_count":9662,"old_finite_problem_reexecution":False})
        tick=time.monotonic()
        try:
            jets=AugmentedFirstJets(
                prepared,paid_model,sources["source_cache"],ledger,
                known_gradients=sources["seed_cuts"],
                source_receipt=receipt,paid_scan=sources["paid_scan"],
                capture=jet_capture)
            domain.bind_jets(jets)
        finally:
            report["timing_segments"]["paid_cache_and_missing_first_jet_context_seconds"]=time.monotonic()-tick
        report["first_jet_input_stdout_receipt"]=emit("JET_INPUT",jets.report())
        tick=time.monotonic()
        try:
            handle,scan=exchange_directions(
                master,jets,domain,ledger,emit=emit,compact_scan=compact_scan,
                progress=exchange_progress)
        finally:
            report["timing_segments"]["new_augmented_exchange_seconds"]=time.monotonic()-tick
        if handle is not None:
            report["complete_direction"]=copy.deepcopy(handle["report"])
        last_scanned=next((v for v in reversed(exchange_progress.get("rounds",[]))
                           if "full_grid_scan_receipt" in v),None)
        if last_scanned is not None:
            report["complete_direction_stdout_receipt"]=copy.deepcopy(
                last_scanned["full_grid_scan_receipt"])
        ledger.check()
        if handle is not None and handle["qualified"]:
            scalar={}
            report["scalar_optimization"]=scalar
            best,_,envelope=run_guarded_line(
                domain,handle,ledger,
                publish_cache=lambda payload:publish_cache(jets,scan,report,line_payload=payload),
                emit_query=lambda row:emit("LINE_QUERY",row),progress=scalar)
            report["scalar_result_stdout_receipt"]=emit("SCALAR_RESULT",scalar)
            report[STAGE]=run_augmented_direction_actual_trials(
                objective,prepared["initial"],domain,handle,envelope,best,
                query_emitter=lambda row:emit("LINE_QUERY",row),
                trial_emitter=lambda row:emit("ACTUAL_TRIAL",row))
        else:
            if scan is not None:
                publish_cache(jets,scan,report)
            report[STAGE]={
                "status":"no-new-augmented-qualified-complete-grid-direction",
                "exchange_status":exchange_progress.get("status"),"trials":[],
                "new_acceptances":0,"source_accepted_index":SOURCE_ACCEPTED_INDEX,
                "all_new_cuts_retained_for_subsequent_genuinely_changed_problem":True,
                "no_old_solver_or_closed_exchange_replayed":True}
        report["status"]=COMPLETE if report[STAGE].get("error") is None else "new-augmented-actual-error"
    except Exception as error:
        if isinstance(error,AugmentedDirectionLimit) or (
                runtime_loaded and isinstance(error,EvaluationBudgetReached)):
            report.update(status="new-augmented-scope-exhausted",
                          budget_message=str(error),
                          budget_counter=getattr(error,"kind","original-value-scope"))
        else:
            report.update(status="new-augmented-input-or-scientific-error",
                          error={"type":type(error).__name__,"message":str(error),
                                 "traceback":traceback.format_exc()})
    finally:
        report["paid_input_attempts"]=compact_capture(input_capture)
        report["exchange_progress"]=exchange_progress
        report["new_attainer_gradients"]=[
            copy.deepcopy(v["row"]) for v in exchange_progress.get("new_gradient_records",[])]
        if master is not None:
            report["augmented_master"]=master.report()
        if jet_capture:
            report["first_jet_input_and_direction_progress"]=compact_capture(jet_capture)
        if jets is not None:
            computed_rows=jets.new_gradient_records()
            report["new_attainer_gradients"]=computed_rows
            emitted_keys={(v["row"]["grid"],v["row"]["flat_row_id"])
                          for v in exchange_progress.get("new_gradient_records",[])}
            report["computed_but_not_installed_gradient_receipts"]=[]
            for row in computed_rows:
                key=(row["grid"],row["flat_row_id"])
                if key not in emitted_keys:
                    try:
                        receipt=emit("ATTAINER_GRADIENT",row)
                        report["computed_but_not_installed_gradient_receipts"].append(
                            {"grid":key[0],"flat_row_id":key[1],
                             "evaluation_status":row.get("evaluation_status"),
                             "original_record_receipt":receipt})
                    except Exception as error:
                        report["unemitted_gradient_recovery_error"]={
                            "type":type(error).__name__,"message":str(error)}
            report["first_jet_report"]=jets.report()
            if scan is None:
                old_key=sources["paid_scan"]["direction_sha256"]
                completed_new=[v for k,v in jets.scans.items() if k!=old_key]
                if completed_new:
                    scan=completed_new[-1]
        if domain is not None:
            report["paid_original_domain"]=domain.report()
        if runtime_loaded and jets is not None and (scan is not None or
                getattr(jets,"_last_attempt_arrays",{})) and not report["cache_emission_attempted"]:
            try:
                publish_cache(jets,scan,report)
            except Exception as error:
                report["partial_cache_reporting_error"]={
                    "type":type(error).__name__,"message":str(error)}
        if envelope is not None:
            report["all_queries"]=copy.deepcopy(envelope.records)
        else:
            scalar=report.get("scalar_optimization")
            report["all_queries"]=copy.deepcopy(
                scalar.get("all_query_records",[]) if isinstance(scalar,dict) else [])
        if objective is not None:
            accepted_capture={}
            tick=time.monotonic()
            try:
                payload=extract_accepted_first_jet_cache(
                    objective,source_identity={"run_id":os.environ.get("GITHUB_RUN_ID"),
                                              "source_commit":os.environ.get("GITHUB_SHA")},
                    capture=accepted_capture)
                if payload is not None:
                    payload["kind"]="accepted-point-paid-geometry"
                    receipt=emit("CACHE",payload)
                    receipt.update(binding_sha256=payload["binding_sha256"],
                                   accepted_index=SOURCE_ACCEPTED_INDEX+1,
                                   no_ordinary_value_or_JVP_reexecution=True)
                    report["accepted_cache_stdout_receipt"]=receipt
            except Exception as error:
                report["accepted_cache_export_error"]={
                    "type":type(error).__name__,"message":str(error),
                    "actual_acceptance_and_paid_value_counts_retained":True}
                if report["status"]==COMPLETE:
                    report["status"]="new-augmented-accepted-cache-export-error"
            finally:
                report["accepted_cache_extraction"]=compact_capture(accepted_capture)
                report["timing_segments"]["accepted_cache_copy_hash_and_stdout_seconds"]=time.monotonic()-tick
            if objective.validation_trace is not None:
                report[STAGE]=objective.validation_trace
            try:
                finish_physical_report(prepared,completed,objective,report,ledger)
            except Exception as error:
                report["final_receipt_error"]={
                    "type":type(error).__name__,"message":str(error),
                    "traceback":traceback.format_exc()}
                report["status"]="new-augmented-final-receipt-error"
                report["partial_true_accepted_records"]=copy.deepcopy(objective.accepted_iterates)
                report["actual_value_account"]=objective.value_account()
                report["actual_value_events"]=copy.deepcopy(objective.actual_value_events)
    report["ledger_before_final_report"]=cost_snapshot(ledger,objective)
    report["process_elapsed_before_final_report"]=time.monotonic()-PROCESS_STARTED
    report["peak_rss_kib_linux"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report["final_FINAL_CLOCK_tag_is_authoritative_and_later_than_checkpoint"]=True
    report["mathematical_stdout_bytes_before_complete"]=STDOUT_BYTES
    complete_receipt=None
    try:
        raw=encoded(jsonable(report))+b"\n"
        output.write_bytes(raw)
        complete_receipt=emit("COMPLETE",report)
    except Exception as error:
        report["status"]="new-augmented-final-serialization-error"
        emit("REPORTING_ERROR",{
            "error":{"type":type(error).__name__,"message":str(error)},
            "status":report["status"],"ledger":cost_snapshot(ledger,objective),
            "cache_receipt":report.get("line_cache_stdout_receipt"),
            "complete_direction_receipt":report.get("complete_direction_stdout_receipt"),
            "selected_point":report.get("selected_two_grid_physical_point")})
    earlier=report["status"]
    exhausted=False
    try:
        ledger.check()
    except AugmentedDirectionLimit as error:
        exhausted=True
        report["status"]="new-augmented-scope-exhausted-after-output"
        report["final_budget_message"]=str(error)
    emit("FINAL_CLOCK",{
        "schema":POLICY+"-final-clock","status_at_final_emit":report["status"],
        "earlier_COMPLETE_status":earlier,"scope_exhausted":exhausted,
        "scope_check_after_all_large_output":True,
        "budget_message":report.get("final_budget_message"),
        "complete_receipt":complete_receipt,"ledger":cost_snapshot(ledger,objective),
        "process_seconds":time.monotonic()-PROCESS_STARTED,
        "mathematical_stdout_bytes_before_final_clock":STDOUT_BYTES,
        "peak_rss_kib_linux":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "sampled_after_all_large_cache_and_complete_write_and_flush":True,
        "only_this_final_clock_follows_its_sample":True,
        "this_status_supersedes_earlier_COMPLETE_scope_status":True})
    return 0 if report["status"]==COMPLETE else 1

if __name__=="__main__":
    raise SystemExit(main())
