#!/usr/bin/env python3
"""Restore the once-paid coarse ordinary input after the true55/new9 shape failure.

Import-only. No geometry, row, derivative, solver, scalar or actual trial is
evaluated here. The caller's same600-second account already carries the original
75.06856296999999 seconds and one started necessary ordinary value before imports.
One completed failed research stdout supplies only MODEL/COMPLETE/FINAL_CLOCK.
"""
from __future__ import annotations
import copy
import io
import time
import numpy as np
import read_original_actions_log as reader
from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
from frame_metric_true55_nine_fiber_scope import POLICY, NineFiberLedger, require

REPO="Rogerhu12/math-research-public"
PREFIX="TRUE55_NINE_"
PINS={
    "run_id":"43840452377","job_id":"133207481935",
    "source_commit":"09f498cac5d2fad47a35f007b68fe66218420d98",
    "workflow":".github/workflows/visible-true55-nine-fiber.yml",
    "log_bytes":26447484,
    "log_sha256":"9f94dfe7f54bc8f17badf3cc29fd74ccc01e110342492780d6f8a091b0ccfc34"}
RECORDS=[
    {"tag":"MODEL","ordinal":1,"JSON_plus_LF_bytes":26079459,
     "JSON_plus_LF_sha256":"9eb1bb5aa0c494dc03cc21235bff51c94b634fd47ea24c0b9ecdd561db02a6e8"},
    {"tag":"COMPLETE","ordinal":1,"JSON_plus_LF_bytes":217817,
     "JSON_plus_LF_sha256":"b268815ce16d2a25579842450cf2e9a9c7a22c169f9385da972fb577d7d8f275"},
    {"tag":"FINAL_CLOCK","ordinal":1,"JSON_plus_LF_bytes":3461,
     "JSON_plus_LF_sha256":"7c8c5f0dce445d49cb1148c8247ac24ffbc32f96171d17e0243617f28147bc2e"}]
OLD_REQUEST={
    "path":"topics/visible-flex-new-mechanism/computations/request-true55-nine-fiber.json",
    "bytes":56618,
    "sha256":"d3acb7e53fff5263cd3b11cc4fdd18af6a745fd513fdb60bb664452675e162d1"}
PRIOR_SECONDS=75.06856296999999
PHYSICAL55="39e71805432d8e1814032200b8cb70973e95475b4ec02696233a7bb37e57746e"
STATUS="new9-input-or-scientific-error"
EXPECTED_ERROR=("operands could not be broadcast together with remapped shapes "
                "[original->remapped]: (160,)  and requested shape (160,384)")

def source_records(raw,ledger):
    expected={(row["tag"],row["ordinal"]):row for row in RECORDS}
    found,counts={},{}
    for line in io.StringIO(raw.decode("utf-8-sig")):
        clean=reader.ANSI.sub("",line.rstrip("\r\n")).lstrip("\ufeff")
        match=reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body=match.group(2).lstrip("\ufeff")
        if not body.startswith(PREFIX):
            continue
        tag,separator,payload=body[len(PREFIX):].partition(" ")
        if not separator:
            continue
        counts[tag]=counts.get(tag,0)+1
        key=(tag,counts[tag])
        if key not in expected:
            continue
        ledger.check("continued-coarse.original-record")
        literal=payload.encode("utf-8")+b"\n"
        pin=expected[key]
        require(len(literal)==pin["JSON_plus_LF_bytes"]
            and reader.digest(literal)==pin["JSON_plus_LF_sha256"],
            "literal original partial-input record changed: "+str(key))
        found[key]=reader.decode_json(literal)
    require(set(found)==set(expected)
        and all(counts.get(tag)==1 for tag in ("MODEL","COMPLETE","FINAL_CLOCK")),
        "one original partial MODEL and one final source clock required")
    return found

def restore_array(record,shape,label):
    require(isinstance(record,dict) and record.get("dtype")=="float64"
        and record.get("shape")==list(shape)
        and isinstance(record.get("array_sha256"),str)
        and isinstance(record.get("values"),list),
        "complete original array metadata required: "+label)
    array=np.asarray(record["values"],dtype=np.float64)
    require(array.shape==tuple(shape) and np.all(np.isfinite(array))
        and array_digest(array)==record["array_sha256"],
        "literal binary64 source array differs: "+label)
    array.setflags(write=False)
    return array

def restore_paid_coarse(request,prepared,ledger,*,capture=None):
    require(isinstance(ledger,NineFiberLedger),"the same new9 ledger is required")
    ledger.check("continued-coarse.entry")
    progress={} if capture is None else capture
    require(isinstance(progress,dict) and not progress,"fresh restore progress required")
    tick=time.monotonic()
    progress.update(status="started",source=copy.deepcopy(PINS),
        original_logs_requested=0,ordinary_geometry_calls=0,
        old_or_new_derivative_calls=0,started_ordinary_debit_repeated=False)
    try:
        continuation=request["continuation"]
        require(continuation["source"]==PINS and continuation["records"]==RECORDS
            and continuation["original_request"]==OLD_REQUEST
            and continuation["resume_only_paid_coarse_ordinary"] is True,
            "only the actual failed-entry paid coarse source is allowed")
        prior=continuation["prior_scope_receipt"]
        require(ledger.prior_scope_receipt==prior
            and ledger.prior_scientific_seconds==PRIOR_SECONDS
            and ledger.prior_started_counts["necessary_model_grid_values"]==1
            and all(value==0 for key,value in ledger.prior_started_counts.items()
                    if key!="necessary_model_grid_values"),
            "prior same-task time and every started debit must precede this read")
        api=reader.GitHubReader(REPO)
        run=api.api_json("/actions/runs/"+PINS["run_id"])
        job=api.api_json("/actions/jobs/"+PINS["job_id"])
        require(str(run["id"])==str(job["run_id"])==PINS["run_id"]
            and str(job["id"])==PINS["job_id"]
            and run["head_sha"]==job["head_sha"]==PINS["source_commit"]
            and run["status"]==job["status"]=="completed"
            and run["conclusion"]==job["conclusion"]=="failure"
            and str(run["path"]).split("@",1)[0]==PINS["workflow"],
            "the unique completed failed research source is required")
        ledger.check("continued-coarse.before-original-log")
        progress["original_logs_requested"]=1
        raw,redirects=api.job_log(PINS["job_id"])
        require(len(raw)==PINS["log_bytes"] and reader.digest(raw)==PINS["log_sha256"],
            "original failed-entry stdout changed")
        records=source_records(raw,ledger)
        del raw
        model,complete,clock=(records[(tag,1)] for tag in ("MODEL","COMPLETE","FINAL_CLOCK"))
        require(complete["status"]==clock["status_at_final_emit"]==STATUS
            and complete["github_repository"]==REPO
            and str(complete["github_run_id"])==PINS["run_id"]
            and complete["github_sha"]==PINS["source_commit"]
            and complete["error"]["type"]=="ValueError"
            and complete["error"]["message"]==EXPECTED_ERROR
            and complete["request_identity"]=={"bytes":OLD_REQUEST["bytes"],"sha256":OLD_REQUEST["sha256"]}
            and complete["old_checks_executed"]==complete["new_development_executed"]==0
            and complete["new_acceptances"]==0
            and clock["scope_exhausted"] is False
            and clock["sampled_after_all_large_cache_and_complete_write_and_flush"] is True,
            "the original partial-entry failure/outcome differs")
        prior_clock=clock["ledger"]
        for key in ("schema","limits","scientific_seconds","started_counts",
                    "events","attempted_problem_bindings"):
            require(prior[key]==prior_clock[key],"prior task receipt differs: "+key)
        require(prior_clock["scientific_seconds"]==PRIOR_SECONDS
            and prior_clock["total_ancestor_plus_new_scientific_seconds"]==2148.63097409
            and prior_clock["total_source_plus_new_started_values"]==135
            and prior_clock["ancestor_scientific_seconds"]==2073.56241112
            and prior_clock["source_original_values_closed"]==134,
            "the failed entry's final complete clock cannot be reset")
        expected_source={**PINS,"final_clock":next(row for row in RECORDS if row["tag"]=="FINAL_CLOCK")}
        require(prior["source"]==expected_source
            and prior["last_problem_added_count"] is None,
            "the carried clock needs the exact original final-clock receipt")
        require(model["schema"]==POLICY+"-partial-new-input"
            and model["status"]=="partial" and model["partial_is_not_a_completed_model"] is True
            and model["source_binding"]==prepared["source_binding"]
            and complete["configuration"]==prepared["cfg"]
            and complete["selected_two_grid_physical_point"]["accepted_index"]==55
            and complete["selected_two_grid_physical_point"]["physical_state_sha256"]==PHYSICAL55
            and set(model["grids"])=={"coarse"},
            "the partial source must be the same unaltered true55 coarse input")
        for name in ("frame_complete_body_extension168.py",
                     "frame_complete_body_extension168_selected.py"):
            path="topics/visible-flex-new-mechanism/scripts/"+name
            require(complete["source_files_sha256"][path]==request["source_sha256"][path],
                "the complete field or its nine directions changed during input repair")
        receipt_pin=next(row for row in RECORDS if row["tag"]=="MODEL")
        require(complete["partial_input_stdout_receipt"]=={
            "tag":PREFIX+"MODEL",
            "JSON_plus_LF_bytes":receipt_pin["JSON_plus_LF_bytes"],
            "JSON_plus_LF_sha256":receipt_pin["JSON_plus_LF_sha256"]},
            "COMPLETE must bind this exact paid partial MODEL")
        source=model["grids"]["coarse"]
        require(set(source["paid_ordinary_input"])=={"X","Xs","Xt","Xss","Xst","Xtt","T"},
            "the seven complete ordinary arrays must remain intact")
        data={name:restore_array(record,(160,384,3),"ordinary/"+name)
              for name,record in source["paid_ordinary_input"].items()}
        data["metric"]={key:restore_array(source["metric"][key],(160,),"metric/"+key)
            for key in ("a","a_s","a_ss")}
        data["height"]={key:restore_array(source["height"][key],(160,),"height/"+key)
            for key in ("b","b_s","b_ss")}
        for key,shape in (("center",(160,)),("radial",(160,)),("theta",(384,))):
            data[key]=restore_array(source[key],shape,key)
        require(data["radial"].tobytes()==np.asarray(prepared["radial"],dtype=np.float64).tobytes()
            and data["theta"].tobytes()==np.asarray(prepared["theta"],dtype=np.float64).tobytes(),
            "restored original coarse grid identity differs")
        receipt={
            "schema":POLICY+"-continued-paid-coarse-receipt",
            "source":copy.deepcopy(PINS),"records":copy.deepcopy(RECORDS),
            "source_binding":copy.deepcopy(model["source_binding"]),
            "original_request":copy.deepcopy(OLD_REQUEST),
            "prior_task_final_clock_authenticated":True,
            "prior_scientific_seconds":PRIOR_SECONDS,
            "prior_started_counts":copy.deepcopy(prior_clock["started_counts"]),
            "source_ordinary_event":copy.deepcopy(prior_clock["events"][0]),
            "restored_grid":"coarse","complete_position_grid_shape":[160,384,3],
            "ordinary_array_sha256":{key:value["array_sha256"]
                for key,value in source["paid_ordinary_input"].items()},
            "radial_array_sha256":source["radial"]["array_sha256"],
            "theta_array_sha256":source["theta"]["array_sha256"],
            "old_and_new_ordinary_reexecutions":0,
            "started_ordinary_debit_repeated":False,
            "new_derivative_or_scalar_calls":0,
            "failure_and_large_output_seconds_are_retained":True}
        progress.update(status="complete",receipt=copy.deepcopy(receipt),
            elapsed_restore_seconds=float(time.monotonic()-tick),
            original_log_redirects=redirects)
        ledger.note("continued-paid-coarse-input-authenticated",
            original_run=PINS["run_id"],original_job=PINS["job_id"],
            previous_scientific_seconds=PRIOR_SECONDS,ordinary_debits_repeated=0)
        ledger.check("continued-coarse.complete")
        return {"coarse":{"data":data,"source_receipt":receipt}},receipt
    except Exception as error:
        progress.update(status="raised",elapsed_restore_seconds=float(time.monotonic()-tick),
            error={"type":type(error).__name__,"message":str(error)})
        raise
