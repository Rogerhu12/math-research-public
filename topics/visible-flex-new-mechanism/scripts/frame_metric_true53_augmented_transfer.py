#!/usr/bin/env python3
"""Read the paid MODEL and the newly paid four-cut/cache observation once."""
from __future__ import annotations
import copy
import time
import numpy as np
import read_original_actions_log as reader
import frame_metric_true53_paid_master_input as paid_input
from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
from frame_metric_true53_projection_transfer import prepare as prepare_original_inputs
from frame_metric_true53_augmented_scope import (
    POLICY,require,SOURCE_GLOBAL_SECONDS,SOURCE_ORIGINAL_VALUES,
    CARRIED_SCIENCE_SECONDS,CARRIED_FAILED_SOURCE,CARRIED_FINAL_CLOCK,
    SOURCE_ACCEPTED_INDEX,SOURCE_PHYSICAL_SHA,SOURCE_CFG_SHA,SOURCE_FIELD_SHA)

REPO="Rogerhu12/math-research-public"
SOURCE={
    "run_id": "43821568604",
    "job_id": "133145590135",
    "source_commit": "323f36fefc0380898aa1e3c0f195e08a32f1fbc1",
    "workflow": ".github/workflows/visible-true53-positive-direction.yml",
    "log_bytes": 34802985,
    "log_sha256": "cde578ee3e7c1046adbf2f7652aa8243679dca3ee1d1f7439938b82adb9c3454"
}
RECORDS=[
    {
        "tag": "FULL_GRID_SCAN",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 56230,
        "JSON_plus_LF_sha256": "f6f50ef8de93c4557d2d9d839ef0f28026018773fb099685460267be619d45f1"
    },
    {
        "tag": "ATTAINER_GRADIENT",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 8467,
        "JSON_plus_LF_sha256": "ff90aeae35ed1b498b45967c181a43ab1422217b68fbbf20ca60a34ba727cf59"
    },
    {
        "tag": "ATTAINER_GRADIENT",
        "ordinal": 2,
        "JSON_plus_LF_bytes": 7413,
        "JSON_plus_LF_sha256": "cc7ef9e365226471982d71f48e0d184b6ceb331d232f86c1b60628a490061c90"
    },
    {
        "tag": "ATTAINER_GRADIENT",
        "ordinal": 3,
        "JSON_plus_LF_bytes": 8450,
        "JSON_plus_LF_sha256": "083067d2cc0dc4d141974b4dffb73caeb49eee26342fb941b7cfe2395bcd1567"
    },
    {
        "tag": "ATTAINER_GRADIENT",
        "ordinal": 4,
        "JSON_plus_LF_bytes": 7442,
        "JSON_plus_LF_sha256": "1737644444a0fc8a7d6595031676386aaab0e85235029ea116e133c656363e35"
    },
    {
        "tag": "CACHE",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 30232607,
        "JSON_plus_LF_sha256": "0c1826ad8f554b6eb2c440e54a5582a9711a05b023f4e2756c300d947d854b40"
    },
    {
        "tag": "COMPLETE",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 4164232,
        "JSON_plus_LF_sha256": "e75b0e004db38e57f767603e3f9ec0d00af409e0a87d5b0c74e9f84b1a9461f3"
    },
    {
        "tag": "FINAL_CLOCK",
        "ordinal": 1,
        "JSON_plus_LF_bytes": 34073,
        "JSON_plus_LF_sha256": "4aa795cc7408dd99a4df132d9168d884f56ac58e746a81f67e0df824c1c17d2e"
    }
]
SOURCE_CACHE_BINDING="75e07691773d43a00f4aa4192499721ff9490784feaaf18d983ef621e95893e7"
SOURCE_ACTUAL_DIRECTION="62b27d0586b4c1fc3eeca5770565db8afe0e02715b5a42204c6c286cc8a0f87b"
SEED_KEYS=(("coarse",43322),("coarse",91304),("fine",86645),("fine",182607))

def decode_paid_records(raw):
    expected={(v["tag"],v["ordinal"]):v for v in RECORDS}
    found={}
    counts={}
    for line in raw.decode("utf-8-sig").splitlines():
        clean=reader.ANSI.sub("",line).lstrip("\ufeff")
        match=reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body=match.group(2)
        prefix="TRUE53_POSITIVE_DIRECTION_"
        if not body.startswith(prefix):
            continue
        tag,separator,payload=body[len(prefix):].partition(" ")
        if not separator:
            continue
        counts[tag]=counts.get(tag,0)+1
        key=(tag,counts[tag])
        if tag in {v["tag"] for v in RECORDS}:
            require(key in expected,"unexpected repeated paid record: "+str(key))
            pin=expected[key]
            literal=payload.encode("utf-8")+b"\n"
            require(len(literal)==pin["JSON_plus_LF_bytes"]
                    and reader.digest(literal)==pin["JSON_plus_LF_sha256"],
                    "paid original JSON+LF changed: "+str(key))
            found[key]=reader.decode_json(literal)
    require(set(found)==set(expected),"all original paid cache/cuts/outcome records required")
    return found


def read_carried_input_failure(request,ledger,capture):
    """Read the original failed FINAL_CLOCK; no science or cache reconstruction."""
    require(request["input_repair_source"]==CARRIED_FAILED_SOURCE
            and request["input_repair_final_clock"]==CARRIED_FINAL_CLOCK,
            "one original failed input source is carried into this same task")
    tick=time.monotonic()
    capture["failed_input_log_attempts"]=1
    try:
        api=reader.GitHubReader(REPO)
        source=CARRIED_FAILED_SOURCE
        run=api.api_json("/actions/runs/"+source["run_id"])
        job=api.api_json("/actions/jobs/"+source["job_id"])
        require(str(run["id"])==str(job["run_id"])==source["run_id"]
                and str(job["id"])==source["job_id"]
                and run["head_sha"]==job["head_sha"]==source["source_commit"]
                and run["path"]==source["workflow"]
                and run["status"]==job["status"]=="completed"
                and job["conclusion"]=="failure" and job["name"]=="research",
                "the failed original research job identity differs")
        raw,redirects=api.job_log(source["job_id"])
        require(len(raw)==source["log_bytes"]
                and reader.digest(raw)==source["log_sha256"],
                "the failed original stdout differs")
        found=[]
        for line in raw.decode("utf-8-sig").splitlines():
            clean=reader.ANSI.sub("",line).lstrip("\ufeff")
            match=reader.TIME_PREFIX.match(clean)
            if match is None:
                continue
            body=match.group(2)
            prefix="TRUE53_AUGMENTED_FINAL_CLOCK "
            if body.startswith(prefix):
                literal=body[len(prefix):].encode("utf-8")+b"\n"
                require(len(literal)==CARRIED_FINAL_CLOCK["JSON_plus_LF_bytes"]
                        and reader.digest(literal)==CARRIED_FINAL_CLOCK["JSON_plus_LF_sha256"],
                        "the failed original final-clock record differs")
                found.append(reader.decode_json(literal))
        require(len(found)==1,"exactly one original final clock is required")
        receipt={"source":copy.deepcopy(source),
                 "final_clock_record":copy.deepcopy(CARRIED_FINAL_CLOCK),
                 "redirects":redirects,
                 "original_log_read_once_without_scientific_recomputation":True,
                 "carried_failed_scientific_seconds":CARRIED_SCIENCE_SECONDS,
                 "unemitted_context_arrays_are_not_claimed_reusable":True}
        ledger.bind_carried_failed_attempt(found[0],receipt)
        capture["carried_failed_input_receipt"]=copy.deepcopy(receipt)
        return receipt
    except Exception as error:
        capture["failed_input_read_error"]={"type":type(error).__name__,"message":str(error)}
        raise
    finally:
        capture["failed_input_log_seconds"]=time.monotonic()-tick

def read_sources(request,ledger,*,capture=None):
    ledger.check()
    capture={} if capture is None else capture
    require(isinstance(capture,dict) and not capture,"fresh read capture required")
    capture.update(status="started",model_log_attempts=0,new_cache_log_attempts=0)
    failed_receipt=read_carried_input_failure(request,ledger,capture)
    require(request["augmented_source"]==SOURCE
            and request["augmented_source_records"]==RECORDS,
            "one already observed original four-cut/cache source required")
    tick=time.monotonic()
    capture["model_log_attempts"]+=1
    try:
        model,old_complete,old_receipt=paid_input.read_paid_source(
            request["paid_model_request"],ledger)
    finally:
        capture["model_log_seconds"]=time.monotonic()-tick
    capture["paid_model_receipt"]=copy.deepcopy(old_receipt)
    ledger.check()
    api=reader.GitHubReader(REPO)
    tick=time.monotonic()
    try:
        run=api.api_json("/actions/runs/"+SOURCE["run_id"])
        job=api.api_json("/actions/jobs/"+SOURCE["job_id"])
        require(str(run["id"])==str(job["run_id"])==SOURCE["run_id"]
                and str(job["id"])==SOURCE["job_id"]
                and run["head_sha"]==job["head_sha"]==SOURCE["source_commit"]
                and run["path"]==SOURCE["workflow"]
                and run["status"]==job["status"]=="completed"
                and run["conclusion"]==job["conclusion"]=="success"
                and job["name"]=="research","paid source identity/status changed")
        capture["new_cache_log_attempts"]+=1
        raw,redirects=api.job_log(SOURCE["job_id"])
        require(len(raw)==SOURCE["log_bytes"] and reader.digest(raw)==SOURCE["log_sha256"],
                "paid four-cut raw stdout changed")
        ledger.check()
        records=decode_paid_records(raw)
        cache=records[("CACHE",1)]
        complete=records[("COMPLETE",1)]
        clock=records[("FINAL_CLOCK",1)]
        scan=records[("FULL_GRID_SCAN",1)]
        cuts=[records[("ATTAINER_GRADIENT",i)] for i in range(1,5)]
        require(complete["status"]=="complete-paid-direction-full-grid-and-original-actual-observation"
                and complete["positive_direction_actual_stage"]["status"]==
                    "new-complete-grid-direction-unqualified"
                and complete["positive_direction_actual_stage"]["new_acceptances"]==0
                and complete["github_sha"]==SOURCE["source_commit"]
                and str(complete["github_run_id"])==SOURCE["run_id"],
                "only the already observed unchanged53/four-new-cut source is allowed")
        counts=clock["ledger"]["started_counts"]
        require(clock["status_at_final_emit"]==complete["status"]
                and clock["scope_exhausted"] is False
                and clock["ledger"]["scientific_seconds"]==50.40678669899998
                and clock["ledger"]["total_ancestor_plus_new_scientific_seconds"]==SOURCE_GLOBAL_SECONDS
                and clock["ledger"]["total_source_plus_new_full_value_debits"]==SOURCE_ORIGINAL_VALUES
                and counts["pair_first_jet_jvps"]==1
                and counts["new_attainer_gradients"]==4
                and counts["actual_grid_values"]==counts["actual_trial_pairs"]==0
                and counts["scalar_queries"]==counts["scalar_sessions"]==0,
                "the whole paid source account must be inherited, not reopened")
        cp=complete["future_positive_direction_checkpoint"]
        point=complete["selected_two_grid_physical_point"]
        require(cp["selected_accepted_index"]==point["accepted_index"]==SOURCE_ACCEPTED_INDEX
                and cp["selected_physical_state_sha256"]==
                    point["physical_state_sha256"]==SOURCE_PHYSICAL_SHA
                and point["physical_state_sha256"]==
                    old_complete["selected_two_grid_physical_point"]["physical_state_sha256"],
                "source true53 changed")
        require(cache["partial"] is False
                and cache["first_jet_input_binding_sha256"]==SOURCE_CACHE_BINDING
                and digest(cache["first_jet_input_binding"])==SOURCE_CACHE_BINDING
                and cache["source_model_binding_sha256"]==model["binding_sha256"]
                and scan["direction_sha256"]==SOURCE_ACTUAL_DIRECTION
                and scan["qualification"]["qualified_first_order_direction"] is False
                and scan["qualification"]["complete_repaired_gain_d"]==
                    -0.00031326043820264013,
                "complete original input and failed direction identity required")
        require(tuple((r["grid"],r["flat_row_id"]) for r in cuts)==SEED_KEYS
                and all(r["ordinary_geometry_calls"]==0 and r["old_selected_J_calls"]==0
                        for r in cuts),"the four original genuinely new gradients are required")
        cache_pin=next(v for v in RECORDS if v["tag"]=="CACHE")
        receipt={"source":copy.deepcopy(SOURCE),
                 "source_records":copy.deepcopy(RECORDS),
                 "cache_record":copy.deepcopy(cache_pin),
                 "cache_binding_sha256":SOURCE_CACHE_BINDING,
                 "source_model_binding_sha256":model["binding_sha256"],
                 "source_actual_direction_sha256":SOURCE_ACTUAL_DIRECTION,
                 "read_original_model_and_new_cache_logs_once":True,
                 "carried_failed_input":copy.deepcopy(failed_receipt),
                 "redirects":redirects,"scientific_recomputations":0,
                 "source_global_scientific_seconds":SOURCE_GLOBAL_SECONDS,
                 "source_original_values":SOURCE_ORIGINAL_VALUES,
                 "old_model_receipt":copy.deepcopy(old_receipt)}
        prepared_source={
            "checkpoint":cp,"report":complete,"point":point,
            "gates":{"coarse":complete["final_full_grid_constraints"],
                     "fine":complete["final_doubled_constraints"]},
            "receipt":receipt,
            "ancestor_cost_receipt":{
                "source_global_scientific_seconds":SOURCE_GLOBAL_SECONDS,
                "source_original_values":SOURCE_ORIGINAL_VALUES,
                "source_final_clock":copy.deepcopy(clock),
                "source_log":copy.deepcopy(SOURCE)}}
        capture.update(status="complete",new_cache_source=copy.deepcopy(SOURCE),
                       new_cache_record=copy.deepcopy(cache_pin))
        ledger.check()
        return {"model":model,"source_cache":cache,"paid_scan":scan,"seed_cuts":cuts,
                "prepared_source":prepared_source,"receipt":receipt}
    except Exception as error:
        capture.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
        raise
    finally:
        capture["new_cache_log_seconds"]=time.monotonic()-tick

def prepare_augmented(request,output,sources,ledger,*,process_started):
    ledger.check()
    require(len(request["original_input_arguments"])==98,
            "the original24 input arguments remain exact")
    completed=sources["prepared_source"]
    require(completed["ancestor_cost_receipt"]["source_global_scientific_seconds"]==
            SOURCE_GLOBAL_SECONDS,"whole paid source account required")
    tick=time.monotonic()
    prepared=prepare_original_inputs(
        request,output,completed,ledger,process_started=process_started)
    ledger.check()
    field,state=prepared["problem"],prepared["initial159"]
    require(digest(field.identity(state))==SOURCE_PHYSICAL_SHA
            and digest(field.evaluation_definition())==SOURCE_FIELD_SHA
            and digest(prepared["cfg"])==SOURCE_CFG_SHA,
            "source field/configuration/physical point changed")
    require(field.timing_snapshot()["geometry_calls_started"]==0,
            "original input restoration may not evaluate source geometry")
    prepared["replay"]["source_input_restoration"].update(
        augmented_preparation_seconds=time.monotonic()-tick,
        augmented_scope_policy=POLICY,
        original24_reused_for_field_and_grid_only=True,
        source_base_ordinary_geometry_calls=0,
        closed_ancestor_scientific_seconds=SOURCE_GLOBAL_SECONDS,
        closed_ancestor_actual_values=SOURCE_ORIGINAL_VALUES)
    return prepared
