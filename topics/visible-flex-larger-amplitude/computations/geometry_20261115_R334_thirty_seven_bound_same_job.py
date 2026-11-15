#!/usr/bin/env python3
"""Request166: one unchanged37 model and its real warm FD, then R334 arithmetic.

Actual98 is restored once as the original parent. No actual141/155 warm is
invented from a hash. The independent observation wrapper copies returned
words; original search/FD sources remain byte pinned. Diagnosis starts after
the original model/FD attempt and cannot reclassify their original outcomes.
All recomputable data is job temporary; complete scalar/range/error readback
precedes the separate explicit cleanup mode.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import traceback

REPOSITORY="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-larger-amplitude"
SCHEMA="actual98-original37-one-model-FD-then-R334-diagnostic-v2"
REQUEST_SCHEMA="actual98-original37-R334-post-model-request-v2"
BASE_RECIPE="public-thirty-seven-model-recipe.json"
BASE_RECIPE_SHA="f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea"
WORKER="geometry_20261115_thirty_seven_temporary_batches.py"
WORKER_SHA="0e5ded8435cd31b7dbedb31dc15a36239ca946f80a346c0c5104cb703f86a89d"
HELPER="root_20261115_thirty_seven_temporary_readout.py"
HELPER_SHA="f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7"
CAPTURE="geometry_20261115_R334_thirty_seven_bound_return_capture.py"
CAPTURE_SHA="e32e941648cc35aef45f4f19ef050f90798e2ca0759b887afc2fff5b782a962b"
CONSUMER="exact_20261115_R334_thirty_seven_bound_candidate_diagnostic.py"
CONSUMER_SHA="6171fbbbbb79457751b7ba8a26c47c111ba5b1f4f91db8170689441df865eb00"
OWNED=".request166-owned.json"


def require(ok,message):
    if not ok: raise ValueError(message)


def sha(raw):return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def encoded(value):
    return (json.dumps(value,sort_keys=True,ensure_ascii=True,
        separators=(",",":"),allow_nan=False)+"\n").encode("ascii")


def write(path,value):
    raw=encoded(value);temporary=path.with_suffix(path.suffix+".writing")
    temporary.write_bytes(raw);temporary.replace(path)
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


def emit(event,value):
    raw=encoded(dict(event=event,**value))
    require(len(raw)<=88000,"Use complete semantic transport for a large scientific object")
    sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()


def load(name,path,digest):
    require(file_sha(path)==digest,"Exact frozen source: "+path.name)
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def bind_work(path,create=False):
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(not path.is_symlink() and path.resolve().parent==temporary,
        "One direct RUNNER_TEMP child is owned by request166")
    identity=dict(schema=SCHEMA,request=166,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"))
    if create:
        require(not path.exists(),"Fresh request166 namespace")
        path.mkdir();write(path/OWNED,identity)
    else:
        require(path.is_dir() and json.loads((path/OWNED).read_bytes())==identity,
            "Only this actual run's recorded namespace may be read or removed")
    return path.resolve(strict=True)


def process_rows():
    rows={}
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():continue
        try:
            data=(entry/"stat").read_text()
            tail=data[data.rfind(")")+2:].split()
            rows[int(entry.name)]=(int(tail[1]),tail[19])
        except (FileNotFoundError,ProcessLookupError,PermissionError,ValueError,IndexError):
            continue
    return rows


def descendants(root_pid):
    rows=process_rows();family={root_pid};changed=True
    while changed:
        changed=False
        for pid,(parent,_) in rows.items():
            if parent in family and pid not in family:family.add(pid);changed=True
    return {pid:rows[pid][1] for pid in family if pid in rows}


def signal_same_processes(identities,signum):
    rows=process_rows();sent=[]
    for pid,start in sorted(identities.items(),reverse=True):
        if pid==os.getpid() or pid not in rows or rows[pid][1]!=start:continue
        try:os.kill(pid,signum);sent.append(dict(pid=pid,proc_start_time=start))
        except ProcessLookupError:pass
    return sent


def bounded_child(helper,progress,deadline,reserve,label,command,repo,env,work):
    remaining=deadline-time.monotonic()-reserve
    if remaining<=0:
        report=dict(label=label,command=list(map(str,command)),exit_code=124,
            child_started=False,reason="global resource deadline before a new child",
            resource_partial=True,mathematical_refusal=False)
        progress["children"].append(report);write(progress["_path"],{k:v for k,v in progress.items() if k!="_path"})
        emit("request166_original_or_diagnostic_child_not_started",report)
        return 124
    log=work/(label+".log");started=time.monotonic()
    family={};timeout=False;signals=[]
    with log.open("wb") as stream:
        child=subprocess.Popen(command,cwd=repo,env=env,stdout=stream,
            stderr=subprocess.STDOUT,start_new_session=False)
        progress["phase"]=label;progress["active_child"]=dict(pid=child.pid,command=list(map(str,command)))
        write(progress["_path"],{k:v for k,v in progress.items() if k!="_path"})
        try:
            code=child.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            timeout=True;family.update(descendants(child.pid))
            signals.append(dict(signal="TERM",identities=signal_same_processes(family,signal.SIGTERM)))
            try:code=child.wait(timeout=30)
            except subprocess.TimeoutExpired:
                family.update(descendants(child.pid))
                signals.append(dict(signal="KILL",identities=signal_same_processes(family,signal.SIGKILL)))
                code=child.wait()
            # Reap any previously identified child whose parent exited before
            # its numerical workers; never signal a recycled PID.
            signals.append(dict(signal="KILL-remaining-original-descendants",
                identities=signal_same_processes(family,signal.SIGKILL)))
    report=dict(label=label,command=list(map(str,command)),exit_code=code,
        effective_return_code=124 if timeout else code,child_started=True,
        elapsed_seconds=time.monotonic()-started,
        external_resource_deadline_triggered=timeout,resource_partial=timeout,
        mathematical_refusal_not_inferred_from_process_exit=True,
        signals=signals,log_file=log.relative_to(progress["_path"].parent).as_posix(),
        log_bytes=log.stat().st_size,log_sha256=file_sha(log),
        complete_error_bytes_printed=False)
    if code or timeout:
        report["complete_error_stream"]=helper.stream_bytes("request166/"+label,log)
        report["complete_error_bytes_printed"]=True
    progress["active_child"]=None;progress["children"].append(report)
    write(progress["_path"],{k:v for k,v in progress.items() if k!="_path"})
    emit("request166_original_or_diagnostic_child_returned",report)
    return 124 if timeout else int(code)


def readback(helper,comp,work):
    """Existing JSON/bytes only; no capture, model, FFT or diagnostic call."""
    events=[]
    rule_result=work.parent/"visible-R334-166-rules"/"runner-result.json"
    if rule_result.is_file():
        events.append(dict(file="rule-sync/runner-result.json",
            original_rule_monitor_result=helper.stream_complete_json(
                "request166/original-rule-monitor-result",helper.read(rule_result))))
    for name in ("pipeline.json","original-pair-summary.json","post-model-diagnostic/result.json",
                 "post-model-diagnostic/summary.json"):
        path=work/name
        if path.is_file():
            value=helper.read(path)
            streamed=helper.stream_complete_json("request166/"+name,value)
            events.append(dict(file=name,bytes=path.stat().st_size,sha256=file_sha(path),
                complete_semantic_readback=streamed))
    batch=work/"batch-000"
    output=batch/"thirty-seven-condensed-warm"
    if not (work/"original-pair-summary.json").is_file():
        reader=helper.load("_request166_existing_original_selectors",comp/helper.READER_ENTRY,helper.READER_SHA)
        paths=(output/"model-000.json",output/"driver-status.json",
            output/"condensed-QP-summary.json",batch/"physical-response"/"response-check.json")
        values=[helper.read(p) if p.is_file() else None for p in paths]
        if any(v is not None for v in values):
            # Original parsed trials are read even when validation/FD was interrupted.
            summary=helper.summarize(reader,values[0],values[1] or {},values[2],values[3])
            streamed=helper.stream_complete_json("request166/surviving-original-trials",summary)
            events.append(dict(file="surviving-original-selected-reports",complete_semantic_readback=streamed))
    capture=output/"R334-return-capture"/"capture.json"
    if capture.is_file():
        value=helper.read(capture)
        selected={k:value.get(k) for k in ("schema","source_sha256","source_commit","run_id",
            "source_input_warm","source_parent_status","query_specs","endpoint_nodes","midpoint_intervals",
            "original_producer","original_observer","original_domain","original_FFT","original_engine",
            "original_model_returned","original_model_exit_code","original_exception",
            "observation_complete","errors","original_runtime_aliases_restored")}
        selected.update(capture_manifest=dict(file=capture.name,bytes=capture.stat().st_size,
            sha256=file_sha(capture)),actual_evaluations=len(value.get("evaluations",[])),
            actual_angular_returns=len(value.get("angular_returns",[])),
            actual_domain_count=len(value.get("domains",[])),
            actual_domain_control_call_inventory=[dict(
                index=row.get("index"),query_count=len(row.get("queries",[])),
                control_return_count=len(row.get("controls",[])),
                angular_return_count=len(row.get("angular_return_indices",[])),
                all_observed_control_calls=row.get("controls",[]),
                original_query_control_identities=[{key:q.get(key) for key in
                    ("query_index","kind","interval","station_float64le",
                     "original_explicit_scalar_control_identity",
                     "original_explicit_scalar_control_identity_field")}
                    for q in row.get("queries",[])])
                for row in value.get("domains",[])],
            actual_final_direction_count=len(value.get("chosen_directions",[])),
            actual_original_direction_documents=value.get("original_direction_documents",[]))
        events.append(dict(file="capture-original-source-and-completeness",
            complete_semantic_readback=helper.stream_complete_json("request166/capture-status",selected)))
    pipeline=helper.read(work/"pipeline.json") if (work/"pipeline.json").is_file() else {}
    emitted={row.get("log_file") for row in pipeline.get("children",[])
        if row.get("complete_error_bytes_printed")}
    exits={row.get("log_file"):row.get("effective_return_code") for row in pipeline.get("children",[])}
    for base in (batch,work):
        if not base.is_dir():continue
        for path in sorted(base.glob("*.log")):
            rel=path.relative_to(work).as_posix()
            if rel not in emitted and exits.get(rel)!=0:
                events.append(dict(file=rel,complete_error_bytes=helper.stream_bytes("request166/surviving/"+rel,path)))
    receipt=write(work/"readback-complete.json",dict(schema=SCHEMA,request=166,
        phase="complete-existing-readback",events=events,no_new_scientific_evaluation=True,
        all_original_model_and_diagnostic_acceptance_flags_unchanged=True))
    emit("request166_complete_existing_readback_returned",dict(receipt=receipt,
        original_model_gate_not_reclassified=True,raw_payloads_remain_until_explicit_cleanup=True))
    return 0


def run(args,repo,comp,request,helper):
    # Starts before restoration, transport, original full J/model and FD.
    started=time.monotonic()
    deadline=started+request["global_science_seconds"]
    reserve=request["cleanup_readback_reserve_seconds"]
    work=bind_work(args.work,create=True)
    progress=dict(schema=SCHEMA,request=166,source_commit=os.environ.get("GITHUB_SHA"),
        run_id=os.environ.get("GITHUB_RUN_ID"),source_sha256=file_sha(__file__),
        request_sha256=file_sha(args.request),base_recipe_sha256=BASE_RECIPE_SHA,
        original_model_exit_code=None,original_FD_exit_code=None,
        post_model_diagnostic_exit_code=None,
        original_new_warm_FD_pair_completed=False,original_model_FD_attempt_returned=False,
        diagnostic_started=False,diagnostic_completed=False,
        diagnostic_does_not_gate_original_model_or_FD=True,
        scientific_native_or_fullDN_accepted=False,phase="restore-original-actual98",
        children=[],active_child=None,resource_partial=False,exception=None,
        global_science_seconds=request["global_science_seconds"],
        cleanup_readback_reserve_seconds=reserve,
        global_deadline_includes_transport_source_restore_model_J_QR_FD_and_diagnostic=True)
    progress["_path"]=work/"pipeline.json"
    def save():
        progress["elapsed_seconds"]=time.monotonic()-started
        write(progress["_path"],{k:v for k,v in progress.items() if k!="_path"})
    original_run_child=helper.run_child
    helper.run_child=lambda label,command,repo0,env,child_work:bounded_child(
        helper,progress,deadline,reserve,label,command,repo0,env,child_work)
    original_entry=helper.MODEL_ENTRY
    final_code=2
    try:
        save()
        recipe=json.loads((comp/BASE_RECIPE).read_bytes())
        require(recipe.get("schema")=="actual98-thirty-seven-model-and-FD-recipe-v1"
            and recipe["parent_artifact"]==helper.PARENT and recipe["model_flags"]==helper.MODEL_FLAGS,
            "Exact original one-model flags and true actual98 parent")
        worker=load("_request166_original37_worker",comp/WORKER,WORKER_SHA)
        reader=helper.load("_request166_original_selectors",comp/helper.READER_ENTRY,helper.READER_SHA)
        inputs=work/"inputs";parent=work/"parent98"
        progress["original_inputs"]=helper.restore_inputs(repo,inputs);save()
        progress["original_parent"]=helper.restore_parent(comp,reader,parent,work);save()
        input_pair=worker.pair_identity(helper,parent)
        reports=work/"source-receipts";reports.mkdir()
        public=helper.load("_request166_original_public_source_restore",
            comp/"exact_20261114_public_resume.py",
            recipe["source_sha256"]["exact_20261114_public_resume.py"])
        public_source=public.prepare_public_source(repo,work/"public-source",reports)
        progress["actual_original78_public_source"]=str(public_source)
        env=dict(os.environ,VISIBLE_SOURCE_TOPIC=str(public_source),PYTHONDONTWRITEBYTECODE="1",
            OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1",NUMEXPR_NUM_THREADS="1")
        for token in ("GITHUB_TOKEN","GH_TOKEN","MR_TOKEN"):env.pop(token,None)
        # Only this private helper's launched entry changes to an observer that
        # invokes the original ENTRY/main. No scientific module file is edited.
        helper.MODEL_ENTRY=CAPTURE
        batch=work/"batch-000"
        summary,output,eligible,code=worker.run_batch(helper,reader,repo,comp,env,inputs,
            parent,input_pair,batch,0,None)
        helper.MODEL_ENTRY=original_entry
        progress["original_model_exit_code"]=summary["original_model_exit_code"]
        progress["original_FD_exit_code"]=summary["original_FD_exit_code"]
        progress["original_model_FD_attempt_returned"]=True
        progress["original_new_warm_FD_pair_completed"]=eligible
        progress["original_pair_summary"]=write(work/"original-pair-summary.json",summary)
        # The primary original scientific values are preserved before diagnosis.
        progress["original_complete_readback"]=worker.print_batch(helper,reader,summary)
        save()
        capture=output/"R334-return-capture"
        if (capture/"capture.json").is_file():
            remaining=deadline-time.monotonic()-reserve
            if remaining>0:
                consumer_seconds=min(request["diagnostic_seconds"],max(1,int(remaining)))
                command=[sys.executable,"-u",str(comp/CONSUMER),"--capture",str(capture),
                    "--model-directory",str(output),"--code-directory",str(comp),
                    "--seconds",str(consumer_seconds),"--max-ledger-bytes",
                    str(request["maximum_temporary_uncompressed_ledger_bytes"]),
                    "--out",str(work/"post-model-diagnostic")]
                progress["diagnostic_started"]=True
                progress["actual_diagnostic_seconds"]=consumer_seconds;save()
                diagnostic_code=helper.run_child("post-model-R334-exact-diagnostic",
                    command,repo,env,work)
                progress["post_model_diagnostic_exit_code"]=diagnostic_code
                diag=work/"post-model-diagnostic"/"summary.json"
                if diag.is_file():
                    value=helper.read(diag)
                    progress["diagnostic_summary"]=value
                    progress["diagnostic_completed"]=value.get("scientific_completed") is True
                    progress["resource_partial"]=value.get("resource_partial") is True
            else:
                progress["diagnostic_not_started_reason"]="global resource deadline after original scientific attempt"
                progress["resource_partial"]=True
        else:
            progress["diagnostic_not_started_reason"]="original observation manifest absent"
        final_code=(code if code else progress["post_model_diagnostic_exit_code"])
        if final_code is None:final_code=3
        progress["phase"]="original-science-returned-and-independent-diagnostic-finished"
    except BaseException as error:
        progress["exception"]=dict(type=type(error).__name__,message=str(error),
            traceback=traceback.format_exc())
        progress["phase"]="controlled-or-program-interruption"
        final_code=2
    finally:
        helper.MODEL_ENTRY=original_entry;helper.run_child=original_run_child
        progress["private_runtime_overrides_restored"]=True
        progress["pipeline_exit_code"]=final_code
        progress["resource_partial"]=progress["resource_partial"] or any(
            item.get("resource_partial") is True for item in progress["children"])
        save()
        helper.stream_complete_json("request166/pipeline-final",
            {k:v for k,v in progress.items() if k!="_path"})
        emit("request166_one_original_pair_and_post_diagnostic_returned",dict(
            pipeline_receipt=dict(file="pipeline.json",bytes=(work/"pipeline.json").stat().st_size,
                sha256=file_sha(work/"pipeline.json")),
            original_model_exit_code=progress["original_model_exit_code"],
            original_FD_exit_code=progress["original_FD_exit_code"],
            original_new_warm_FD_pair_completed=progress["original_new_warm_FD_pair_completed"],
            post_model_diagnostic_exit_code=progress["post_model_diagnostic_exit_code"],
            diagnostic_completed=progress["diagnostic_completed"],
            resource_partial=progress["resource_partial"],pipeline_exit_code=final_code,
            original_acceptance_not_changed_by_diagnostic=True,
            raw_cleanup_deferred_until_complete_same_job_readback=True))
    return final_code


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root",type=Path,required=True)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--work",type=Path,required=True)
    parser.add_argument("--mode",choices=("run","readback","cleanup"),default="run")
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Only public Actions execute or read these original scientific children")
    repo=args.repo_root.resolve(strict=True);comp=repo/TOPIC/"computations"
    request=json.loads(args.request.read_bytes())
    require(request.get("schema")==REQUEST_SCHEMA and request.get("request")==166
        and request.get("repository")==REPOSITORY,"Independent request166 identity")
    require(request["source_sha256"]==file_sha(__file__),"Actual orchestrator source")
    require(file_sha(comp/BASE_RECIPE)==BASE_RECIPE_SHA,"Original155 recipe retained, not relabelled")
    for name,digest in request["required_source_sha256"].items():
        require(Path(name).name==name and file_sha(comp/name)==digest,"Frozen source: "+name)
    for name,digest in request["required_parameter_sha256"].items():
        require(Path(name).name==name and file_sha(comp/name)==digest,"Frozen parameter: "+name)
    for name,digest in ((WORKER,WORKER_SHA),(HELPER,HELPER_SHA),(CAPTURE,CAPTURE_SHA),(CONSUMER,CONSUMER_SHA)):
        require(request["required_source_sha256"][name]==digest,"Actual new input source closure")
    require(request["global_science_seconds"]==6000 and request["cleanup_readback_reserve_seconds"]==180
        and request["diagnostic_seconds"]==1800
        and request["maximum_temporary_uncompressed_ledger_bytes"]==8589934592,
        "Explicit bounded independent diagnostic and original total resource allocation")
    helper=load("_request166_original37_support",comp/HELPER,HELPER_SHA)
    if args.mode=="run":return run(args,repo,comp,request,helper)
    if not args.work.exists():
        emit("request166_no_owned_scientific_payload",dict(mode=args.mode,
            scientific_child_not_inferred_to_have_run=True,no_cleanup_needed=True))
        return 0
    work=bind_work(args.work)
    if args.mode=="readback":return readback(helper,comp,work)
    require(args.mode=="cleanup","Explicit lifecycle dispatch")
    # Failure to finish readback is printed as such; cleanup is never silently
    # interpreted as a scientific result or an accepted candidate.
    marker=work/"readback-complete.json"
    emit("request166_owned_cleanup_begin",dict(
        work_directory=work.name,complete_readback_marker_present=marker.is_file(),
        unread_output_must_not_be_reported_as_complete=not marker.is_file()))
    require(marker.is_file(),"Read all surviving scalar/trial/range/error output before cleanup")
    shutil.rmtree(work)
    emit("request166_owned_cleanup_complete",dict(
        removed_directory=work.name,recomputable_raw_artifact_uploads=0,
        Release_uploads=0,Git_raw_publication=0))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
