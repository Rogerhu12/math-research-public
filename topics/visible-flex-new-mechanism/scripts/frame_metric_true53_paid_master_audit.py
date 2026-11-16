#!/usr/bin/env python3
"""One genuinely new finite solve using all already-paid true53 gradients."""
from __future__ import annotations
import time
PROCESS_STARTED = time.monotonic()
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import sys
import traceback
import numpy as np
import read_original_actions_log as reader
from frame_metric_true53_paid_master_central_path import (
    NewMasterLedger, solve_paid_master)
from frame_metric_true53_paid_master_input import (
    POLICY, REPO, SOURCE_GLOBAL_SECONDS, SOURCE_VALUES,
    read_paid_source, assemble_paid_master, finite_candidate, require)

TAG = "TRUE53_PAID_MASTER_"
PRIOR_INPUT_FAILURE = {
    "run_id": "43816639046",
    "job_id": "133130076418",
    "source_commit": "01614a9cbbc2ce1cfe93318915dee05292dc586a",
    "final_clock_JSON_plus_LF_bytes": 1385,
    "final_clock_JSON_plus_LF_sha256": "9c5e533ec4948fb9b8bbc2189cbb185ab75f25b3c0b35a61f3863925e9499e16",
    "science_seconds": 5.828010012000021,
    "finite_LP_calls": 0,
    "newton_systems": 0,
    "source_raw_log_reads": 1
}
PRIOR_SCIENCE_SECONDS = PRIOR_INPUT_FAILURE["science_seconds"]


def emit(suffix, value):
    raw = reader.encoded(value)
    sys.stdout.write(TAG+suffix+" ")
    sys.stdout.write(raw.decode("utf-8"))
    sys.stdout.write("\n")
    sys.stdout.flush()
    return {"tag":TAG+suffix, "JSON_plus_LF_bytes":len(raw)+1,
            "JSON_plus_LF_sha256":reader.digest(raw+b"\n")}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True)
    args=parser.parse_args()
    ledger=NewMasterLedger(started_monotonic=PROCESS_STARTED-PRIOR_SCIENCE_SECONDS)
    ledger.note("prior_input_failure_carried_forward", **PRIOR_INPUT_FAILURE)
    report={"schema":POLICY+"-audit","status":"starting","timing_segments":{},
            "source_log_read_attempts":0,"actual_finite_LP_calls_started":0,
            "new_geometry_values":0,"new_hard_J":0,"new_JVP":0,"new_metric_gradients":0,
            "new_scalar_searches":0,"new_actual_trials":0,"new_actual_acceptances":0,
            "old_HiGHS_cone_Hildreth_or_development_calls":0,
            "full_grid_feasibility_or_main_goal_not_claimed":True,
            "only_original_stdout_new_result_not_Git_artifact_release_or_cache":True,
            "prior_failed_input_receipt":copy.deepcopy(PRIOR_INPUT_FAILURE),
            "same_finite_master_scope_resumed_without_clock_or_LP_reset":True}
    result=None
    try:
        require(os.environ.get("GITHUB_ACTIONS")=="true"
                and os.environ.get("GITHUB_REPOSITORY")==REPO,
                "this research executes only in the authorized public repository Actions")
        require(np.__version__=="2.3.5", "the pinned numerical runtime is required")
        request_raw=Path(args.request).read_bytes()
        request=reader.decode_json(request_raw)
        require(request["repository"]==REPO and request["parameters"]["policy"]==POLICY
                and request["parameters"]["science_seconds"]==240
                and request["parameters"]["maximum_iterations"]==96
                and request["parameters"]["maximum_newton_systems"]==192
                and request["parameters"]["finite_LP_calls"]==1
                and request["resume_after_input_failure"]==PRIOR_INPUT_FAILURE
                and request["parameters"]["earlier_source_log_reads"]==1,
                "the one new finite-method scope is immutable")
        for path,sha in request["source_sha256"].items():
            require(reader.digest(Path(path).read_bytes())==sha,
                    "requested source text changed: "+path)
        report["request"]={"bytes":len(request_raw),"sha256":reader.digest(request_raw),
                           "parameters":copy.deepcopy(request["parameters"]),
                           "source_sha256":copy.deepcopy(request["source_sha256"])}
        report["github_sha"]=os.environ.get("GITHUB_SHA")
        report["github_run_id"]=os.environ.get("GITHUB_RUN_ID")
        report["github_repository"]=os.environ.get("GITHUB_REPOSITORY")
        emit("REQUEST",report["request"])
        ledger.check()
        report["source_log_read_attempts"]+=1
        tick=time.monotonic()
        try:
            source,completed,receipt=read_paid_source(request,ledger)
        finally:
            report["timing_segments"]["once_paid_source_read_seconds"]=time.monotonic()-tick
        report["source_receipt"]=receipt
        emit("SOURCE",receipt)
        tick=time.monotonic()
        try:
            data=assemble_paid_master(source,ledger)
        finally:
            report["timing_segments"]["new_all_paid_row_assembly_seconds"]=time.monotonic()-tick
        report["assembled_model"]=data["receipt"]
        emit("ASSEMBLY",data["receipt"])
        report["actual_finite_LP_calls_started"]+=1
        tick=time.monotonic()
        try:
            result=solve_paid_master(
                data["A"],data["b"],data["row_tol"],data["row_kind"],
                data["outer_lo"],data["outer_hi"],data["initial_x"],ledger=ledger)
        finally:
            report["timing_segments"]["one_new_central_path_solve_seconds"]=time.monotonic()-tick
        report["new_finite_solver_status"]=result["status"]
        report["new_finite_result_receipt"]=emit("RESULT",result)
        ledger.check()
        report["candidate"]=finite_candidate(data,result.get("last_finite_x"))
        report["status"]="new-finite-master-observation-complete"
        report["selected_actual_point_unchanged"]={
            "accepted_index":53,
            "physical_state_sha256":completed["selected_two_grid_physical_point"]["physical_state_sha256"],
            "maximum_eta_on_both_grids":completed["selected_two_grid_physical_point"]["maximum_eta_on_both_grids"],
            "new_metric_target_qualified_on_both_grids":False,
            "original_two_grid_acceptance_receipts_reused_without_geometry":True}
        report["finite_positive_primal_is_only_a_new_direction_for_later_complete_separation"]=True
        ledger.check()
    except Exception as error:
        report["status"]="new-finite-master-input-solve-or-output-error"
        report["error"]={"type":type(error).__name__,"message":str(error),
                         "traceback":traceback.format_exc()}
        # If the core returned a finite object but later output failed, retain
        # this object once as a true partial result, without repeating science.
        if result is not None and "new_finite_result_receipt" not in report:
            try:
                report["new_finite_result_receipt"]=emit("PARTIAL_RESULT",result)
            except Exception as output_error:
                report["partial_output_error"]={"type":type(output_error).__name__,
                                                "message":str(output_error)}
    report["ledger_before_large_complete_emit"]=ledger.report()
    complete_receipt=emit("COMPLETE",report)
    scope_error=None
    try:
        ledger.check()
    except Exception as error:
        scope_error={"type":type(error).__name__,"message":str(error)}
    final_ledger=ledger.report()
    now=time.monotonic()
    elapsed=now-PROCESS_STARTED
    clock={
        "schema":POLICY+"-final-clock",
        "status_at_final_emit":report["status"] if scope_error is None else "new-finite-scope-ended",
        "scope_check_error":scope_error,"complete_receipt":complete_receipt,
        "this_process_scientific_seconds":elapsed,
        "prior_failed_input_scientific_seconds":PRIOR_SCIENCE_SECONDS,
        "this_new_scientific_seconds":PRIOR_SCIENCE_SECONDS+elapsed,
        "ancestor_scientific_seconds":SOURCE_GLOBAL_SECONDS,
        "total_ancestor_plus_new_scientific_seconds":SOURCE_GLOBAL_SECONDS+PRIOR_SCIENCE_SECONDS+elapsed,
        "total_source_raw_log_reads_for_this_finite_master":1+report["source_log_read_attempts"],
        "ancestor_actual_values":SOURCE_VALUES,"new_actual_values":0,
        "total_source_plus_new_actual_values":SOURCE_VALUES,
        "one_new_finite_LP_calls_started":report["actual_finite_LP_calls_started"],
        "newton_ledger":final_ledger,
        "new_science_includes_import_input_assembly_all_failures_and_all_prior_output":True,
        "only_this_final_record_follows_the_time_sample":True,
        "old64_old32_and_true53_projection_accounts_remain_closed":True,
        "no_development_or_old_independent_replay":True}
    emit("FINAL_CLOCK",clock)


if __name__=="__main__":
    main()
