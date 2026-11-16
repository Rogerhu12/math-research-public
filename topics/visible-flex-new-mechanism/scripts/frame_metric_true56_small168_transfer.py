#!/usr/bin/env python3
"""Restore true56 and the closed joint168 input for a different physical domain.

Import-only. The current point and paid U/T come from actual56, permanent
constructor data from55, and J/g plus eight new rows from the closed joint
task. No old ordinary, derivative, optimizer or development instance is run.
"""
from __future__ import annotations
import copy
from pathlib import Path
import time
import read_original_actions_log as reader
from frame_height_null_coordinates import digest
from frame_metric_true56_joint168_transfer import (
    read_source as read_actual56, prepare as prepare_actual56,
    _read_records, PHYSICAL_SHA, STATE_SHA, CFG_SHA)
from frame_metric_true56_small168_scope import POLICY, Joint168Ledger, require

REPO="Rogerhu12/math-research-public"
PAID_PINS={"run_id":"43847611444","job_id":"133231619868",
    "source_commit":"a9da16278c336ec5d6ce3be88502263d04429324",
    "workflow":".github/workflows/visible-true56-joint168.yml",
    "log_bytes":46110806,
    "log_sha256":"28eeef350781fd1a341adad4da553abbc4918bf8aa129ee01a61a6ecc9e3a489"}
PAID_RECORDS=[
 {"tag":"INPUT","ordinal":3,"JSON_plus_LF_bytes":21504677,
  "JSON_plus_LF_sha256":"058becbdcdc8746328f702cd0f92e04d622bc387b8c206cc98489beba602691e"},
 {"tag":"MODEL","ordinal":1,"JSON_plus_LF_bytes":1047239,
  "JSON_plus_LF_sha256":"86b10a9a76794839239e678a7af9d545bc627f661d80d746c84b352dfbeb6d4b"},
 {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":2122368,
  "JSON_plus_LF_sha256":"f8b2bf46220044084bf3726c2062b66e472abeffdd6e44c3e70d6a98a1048473"},
 {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":76487,
  "JSON_plus_LF_sha256":"39d760b534c554833d6b47f515d417838be64f10fd3a5af440ea10c36a7ad305"}]
PAID_REQUEST={"path":"topics/visible-flex-new-mechanism/computations/request-true56-joint168.json",
    "bytes":60590,
    "sha256":"9272179a7cafad1cde180b5709b548a544e4fdc2b5eb1cff6fb813b5719cedc9"}
INPUT_BINDING="b36f43c371c84644dbe9a96d9acf0bdb107b722eefb5a5a2a2200283099ee431"
MODEL_BINDING="0eb0dc10dac2acddaea88566b9a18a025c8601d7b2759f38668723fdb2699a4e"
ANCESTOR_SECONDS=2421.953314364
ANCESTOR_VALUES=141

def read_source(request,ledger,*,capture=None):
    require(isinstance(ledger,Joint168Ledger),"one new small-domain task ledger required")
    progress={} if capture is None else capture
    require(not progress,"fresh source input capture required")
    started=time.monotonic()
    progress.update(status="started",original_logs_requested=0,
        ordinary_geometry_calls=0,old_J_model_optimizer_or_development_calls=0,
        actual56_source_read={})
    try:
        completed=read_actual56(request,ledger,capture=progress["actual56_source_read"])
        require(request["paid_joint_source"]==PAID_PINS
            and request["paid_joint_records"]==PAID_RECORDS
            and request["paid_joint_request"]==PAID_REQUEST,
            "the already paid current168 input must have its literal source")
        raw=Path(PAID_REQUEST["path"]).read_bytes()
        require(len(raw)==PAID_REQUEST["bytes"]
            and reader.digest(raw)==PAID_REQUEST["sha256"],
            "the closed full168 request changed")
        old_request=reader.decode_json(raw)
        require(old_request["source"]==request["source"]
            and old_request["original_input_arguments"]==request["original_input_arguments"]
            and old_request["fixed_complete_metric_sha256"]==request["fixed_complete_metric_sha256"]
            and old_request["fixed_b0_definition_sha256"]==request["fixed_b0_definition_sha256"],
            "same actual56, same original24 inputs and same g/b0 required")
        api=reader.GitHubReader(REPO)
        records,receipts=_read_records(api,PAID_PINS,"TRUE56_JOINT_",
            PAID_RECORDS,ledger,progress)
        inp=records[("INPUT",3)]
        model=records[("MODEL",1)]
        report=records[("COMPLETE",1)]
        clock=records[("FINAL_CLOCK",1)]
        require(report["status"]==clock["status_at_final_emit"]==
                "complete-true56-full168-original-actual-observation"
            and report["github_sha"]==PAID_PINS["source_commit"]
            and str(report["github_run_id"])==PAID_PINS["run_id"]
            and report["github_repository"]==REPO
            and report["new_acceptances"]==0
            and report["old_checks_executed"]==report["new_development_executed"]==0
            and report["source_files_sha256"]==old_request["source_sha256"]
            and clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True
            and not clock["scope_exhausted"],
            "the paid input belongs to the closed original actual-rejection task")
        final=clock["ledger"]
        require(final["scientific_seconds"]==188.38691980800002
            and final["total_ancestor_plus_new_scientific_seconds"]==ANCESTOR_SECONDS
            and final["total_source_plus_new_started_values"]==ANCESTOR_VALUES
            and final["started_counts"]=={
                "necessary_model_grid_values":2,"selected_J_grid_builds":2,
                "full_separations":3,"new_metric_rows":8,"finite_master_calls":3,
                "finite_master_iterations":126,"finite_master_newton_systems":252,
                "scalar_sessions":1,"scalar_queries":62,
                "actual_trial_pairs":1,"actual_grid_values":1},
            "the closed full168 costs and all started calls must be retained")
        require(report["selected_two_grid_physical_point"]==completed["point"]
            and report["actual_stage"]["selected_two_grid_physical_point"]==completed["point"]
            and report["source56_actual_point"]==completed["point"]
            and digest(report["configuration"])==CFG_SHA
            and completed["point"]["physical_state_sha256"]==PHYSICAL_SHA,
            "the rejected trial cannot become the current56 point")
        require(inp["binding_sha256"]==INPUT_BINDING==digest(inp["binding"])
            and model["input_binding_sha256"]==INPUT_BINDING
            and model["model_binding_sha256"]==MODEL_BINDING==digest(model["model_binding"])
            and report["joint168_input_receipt"]["binding_sha256"]==INPUT_BINDING
            and inp["binding"]["current_independent168_sha256"]==STATE_SHA
            and inp["binding"]["source_physical_state_sha256"]==PHYSICAL_SHA,
            "complete paid input/model/current-state binding changed")
        for tag,receipt in (("INPUT",report["complete_current168_input_stdout_receipt"]),
                            ("MODEL",report["model_stdout_receipt"])):
            pin=next(p for p in PAID_RECORDS if p["tag"]==tag)
            require(receipt["JSON_plus_LF_bytes"]==pin["JSON_plus_LF_bytes"]
                and receipt["JSON_plus_LF_sha256"]==pin["JSON_plus_LF_sha256"],
                "the old COMPLETE must point to the identical paid record")
        require(len(inp["original_domain"]["hard_original_row_tags"])==3132
            and len(inp["original_domain"]["selected_metric_original_row_tags"])==5870
            and len(model["new_original_metric_rows_with_paid_gradients168"])==8,
            "all9002 original rows and all8 paid new gradients are required")
        stage=report["actual_stage"]
        for label,size,version in (("coarse",4454,15),("fine",4549,14)):
            pool=stage[label+"_pool"]
            old_pool=completed["source_stage"][label+"_pool"]
            require(len(pool)==size and len(set(pool))==size
                and stage[label+"_pool_version"]==version
                and set(old_pool).issubset(pool)
                and set(pool)-set(old_pool)==({104448} if label=="coarse" else set()),
                "the latest actual separation is one new original coarse metric row")
            grid_binding=inp["binding"]["grids"][label]
            paid_cache=completed["accepted_cache"]["grids"][label]
            require(grid_binding["baseline_e_sha256"]==paid_cache["e"]["array_sha256"]
                and grid_binding["baseline_f_sha256"]==paid_cache["f"]["array_sha256"],
                "the original paid U/T baseline and current168 derivative point disagree")
        receipt={"schema":POLICY+"-paid-input-source",
            "source":copy.deepcopy(PAID_PINS),"records":receipts,
            "source_request":copy.deepcopy(PAID_REQUEST),
            "input_binding_sha256":INPUT_BINDING,"model_binding_sha256":MODEL_BINDING,
            "closed_ancestor_scientific_seconds":ANCESTOR_SECONDS,
            "closed_ancestor_values":ANCESTOR_VALUES,
            "old_task_remaining_balance_not_reopened":True,
            "actual56_source":copy.deepcopy(completed["receipt"]),
            "all_completed_9002_current168_rows_and8_added_gradients_reused":True,
            "only_new_actual_metric_tag":{"grid":"coarse","flat_row_id":104448},
            "ordinary_or_derivative_reexecutions":0}
        cost={"ancestor_final_original_scientific_seconds":ANCESTOR_SECONDS,
            "source_global_scientific_seconds":ANCESTOR_SECONDS,
            "source_original_full_values":ANCESTOR_VALUES,
            "source_original_values":ANCESTOR_VALUES,
            "closed_full168_final_clock":copy.deepcopy(clock),
            "closed_actual56_cost":copy.deepcopy(completed["ancestor_cost_receipt"]),
            "old_task_remaining_balance_not_reopened":True}
        completed.update(paid_joint_input=inp,paid_joint_model=model,
            paid_joint_receipt=receipt,paid_joint_final_clock=clock,
            source_stage=copy.deepcopy(stage),receipt=receipt,
            ancestor_cost_receipt=cost)
        progress["original_logs_requested"]+=progress["actual56_source_read"]["original_logs_requested"]
        progress.update(status="complete",accepted_index=56,receipt=receipt)
        ledger.check("small168.source.complete")
        return completed
    except Exception as error:
        progress.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
        raise
    finally:
        progress["elapsed_source_input_seconds"]=time.monotonic()-started

def prepare(request,output,completed,ledger,*,process_started):
    # The closed actual evaluator appends new IDs; its literal pool order is
    # authoritative.  The older constructor accepts only sorted source pools.
    # Give that constructor its original56 pool, then install the current
    # authenticated pool without changing an ID, order, capacity or gate.
    constructor=dict(completed)
    constructor["source_stage"]=completed["report"]["actual_stage"]
    prepared=prepare_actual56(request,output,constructor,ledger,process_started=process_started)
    stage=completed["source_stage"]
    for label in ("coarse","fine"):
        values=stage[label+"_pool"]
        grid=prepared["row_grids"][label]
        capacity=int(prepared["cfg"]["max_pool_rows" if label=="coarse"
                                     else "max_fine_physical_pool_rows"])
        require(isinstance(values,list) and all(type(v) is int for v in values)
            and len(values)==len(set(values)) and len(values)<=capacity
            and all(0<=v<11*grid.point_count for v in values),
            "the literal actual pool must retain unique legal IDs within its original capacity")
        prepared[label+"_pool"]=list(values)
        prepared["replay"]["source_checkpoint"][label+"_pool"]=list(values)
        prepared["replay"]["source_checkpoint"][label+"_pool_version"]=stage[label+"_pool_version"]
    restoration=prepared["replay"]["source_input_restoration"]
    restoration.pop("all24_original_inputs_loaded_once",None)
    restoration.update(original24_inputs_restored_once_in_this_process=True,
        input_restore_attempts_in_this_same_task=2,
        closed_actual_pool_literal_order_preserved=True,
        old_constructor_only_used_original56_pool=True,
        current_model_uses_complete_latest_pool=True)
    prepared.update(paid_joint_input=completed["paid_joint_input"],
        paid_joint_model=completed["paid_joint_model"],
        paid_joint_receipt=completed["paid_joint_receipt"])
    prepared["replay"]["source_input_restoration"].update(
        closed_ancestor_scientific_seconds=ANCESTOR_SECONDS,
        closed_ancestor_ordinary_values=ANCESTOR_VALUES,
        current168_paid_J_source=copy.deepcopy(PAID_PINS),
        current168_paid_input_binding_sha256=INPUT_BINDING,
        smaller_physical_domain_is_a_new_finite_instance=True,
        old_master_or_large_domain_direction_not_reexecuted=True)
    ledger.check("small168.prepare.complete")
    return prepared
