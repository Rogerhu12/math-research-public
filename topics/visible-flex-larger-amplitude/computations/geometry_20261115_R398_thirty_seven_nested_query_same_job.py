#!/usr/bin/env python3
"""Request188: one unchanged37 model and real warm FD, then same-path nested closed domains.

Actual98 is restored once as the original parent. No actual141/155 warm is
invented from a hash. The independent observation wrapper copies returned
words; original search/FD sources remain byte pinned. Diagnosis starts after
the original model/FD attempt and cannot reclassify their original outcomes.
All recomputable data is job temporary. One bounded necessary scalar/range/error
summary precedes explicit cleanup; full scientific witnesses are never streamed.
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
SCHEMA="actual98-original37-one-model-FD-then-nested-closed-Hermite-domain-v1"
REQUEST_SCHEMA="actual98-original37-nested-closed-Hermite-domain-request-v1"
BASE_RECIPE="public-thirty-seven-model-recipe.json"
BASE_RECIPE_SHA="f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea"
WORKER="geometry_20261115_thirty_seven_temporary_batches.py"
WORKER_SHA="0e5ded8435cd31b7dbedb31dc15a36239ca946f80a346c0c5104cb703f86a89d"
HELPER="root_20261115_thirty_seven_temporary_readout.py"
HELPER_SHA="f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7"
CAPTURE="geometry_20261115_R354_thirty_seven_query_scalar_capture.py"
CAPTURE_SHA="0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90"
CONSUMER="exact_20261115_R398_thirty_seven_nested_query_domain.py"
CONSUMER_SHA="51d12ef4f224f2b579bd4afbda0f9fd568b2c6eea61e13eec4a1bcbd89422365"
OWNED=".request188-owned.json"


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
    require(len(raw)<=90000,"One bounded metadata event; no scientific witness segments")
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
        "One direct RUNNER_TEMP child is owned by request188")
    identity=dict(schema=SCHEMA,request=188,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_commit=os.environ.get("GITHUB_SHA"))
    if create:
        require(not path.exists(),"Fresh request188 namespace")
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
        emit("request188_original_or_diagnostic_child_not_started",report)
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
        report["error_log_retained_for_necessary_bounded_readback"]=True
        report["complete_error_log_forwarded"]=False
    progress["active_child"]=None;progress["children"].append(report)
    write(progress["_path"],{k:v for k,v in progress.items() if k!="_path"})
    emit("request188_original_or_diagnostic_child_returned",report)
    return 124 if timeout else int(code)


def scalar_fields(value):
    return {k:v for k,v in value.items()
        if v is None or isinstance(v,(str,int,float,bool))} if isinstance(value,dict) else {}


def take(value,keys):
    return {k:value[k] for k in keys if k in value} if isinstance(value,dict) else {}


def index_ranges(values):
    """Integer metadata only, never a scientific interval operation."""
    result=[]
    for item in sorted(set(values)):
        require(isinstance(item,int) and not isinstance(item,bool),"Integer metadata index")
        if result and item==result[-1][1]+1:result[-1][1]=item
        else:result.append([item,item])
    return result


def domain_scalar_record(value):
    if not isinstance(value,dict):return None
    answer=scalar_fields(value)
    answer["original_physical_argmax"]=value.get("physical_argmax")
    answer["original_RMS_checks"]=[]
    for row in value.get("RMS_checks",[]):
        points=row.get("first_invalid_point_rows") or []
        answer["original_RMS_checks"].append(dict(
            scalar_fields(row),original_listed_failure_count=len(points),
            original_listed_failure_interval_ranges=index_ranges(
                point[0] for point in points if point and isinstance(point[0],int)),
            original_first_failure_point=None if not points else points[0]))
    answer["original_RMS_failed_point_columns"]=value.get("RMS_failed_point_columns")
    bad=value.get("bad_midpoint_indices") or []
    answer["original_bad_midpoint_ranges"]=index_ranges(bad)
    points=value.get("midpoint_failed_point_rows") or []
    selected=[row for row in points if row and row[0] in bad]
    answer["original_midpoint_failed_point_columns"]=value.get("midpoint_failed_point_columns")
    answer["original_first_bad_midpoint_point"]=selected[0] if selected else None
    answer["all_original_listed_midpoint_rows_count"]=len(points)
    answer["nested_detailed_domain_rows_retained_in_job"]=True
    return answer


def trial_scalar_record(row):
    answer=scalar_fields(row)
    answer.update(take(row,("selected_query_count","selected_query_indices",
        "selected_beta_squared_minima","selected_negative_angle_counts",
        "selected_nonfinite_angle_counts","nearest_failed_selected_queries",
        "selected_linear_beta_squared","all_selected_linear_reserve_slack")))
    answer["domain"]=domain_scalar_record(row.get("domain"))
    answer["complete_original_RMS_query_domain"]=domain_scalar_record(
        row.get("complete_original_RMS_query_domain"))
    raw=encoded(row)
    answer["original_selected_trial_object_identity"]=dict(bytes=len(raw),sha256=sha(raw))
    answer["complete_nested_trial_object_not_returned"]=True
    return answer


def query_step_metadata(result):
    qr=result.get("query_domain_188") or {}
    pairs=qr.get("query_step_results") or []
    lookup={}
    reasons=[]
    for row in pairs:
        q,j=row["query_index"],row["trial_index"]
        require(isinstance(q,int) and isinstance(j,int) and 0<=q<37 and 0<=j<17,
            "Actual declared query/step metadata")
        require((q,j) not in lookup,"No duplicate query/step result is silently merged")
        lookup[q,j]=row
        reason=row.get("missing_endpoint_bound_reason")
        if reason is not None and reason not in reasons:reasons.append(reason)
    steps=[]
    for j in range(17):
        sets={key:[] for key in ("proved","refuted","unresolved","unvisited",
            "gap_available","pair_not_reached")}
        groups={}
        for q in range(37):
            row=lookup.get((q,j))
            if row is None:
                sets["unvisited"].append(q);sets["pair_not_reached"].append(q)
                continue
            if row.get("full453_uniform_gap_available") is True:
                sets["gap_available"].append(q)
            if row.get("complete_accurate_query_domain_proved") is True:
                sets["proved"].append(q)
            elif row.get("any_accurate_query_angle_rigorously_refuted") is True:
                sets["refuted"].append(q)
            elif row.get("complete_closed_query_angle_rows",0):
                sets["unresolved"].append(q)
            else:sets["unvisited"].append(q)
            reason=row.get("missing_endpoint_bound_reason")
            values=[row.get("complete_closed_query_angle_rows"),
                row.get("strictly_proved_angle_count"),row.get("rigorously_refuted_angle_count"),
                row.get("unresolved_angle_count"),
                row.get("direct_angle_evaluations_committed"),
                row.get("inherited_angle_proofs_committed"),
                row.get("direct_strictly_proved_angle_count"),
                row.get("inherited_strictly_proved_angle_count"),
                row.get("unvisited_angle_ranges"),
                None if reason is None else reasons.index(reason)]
            key=encoded(values)
            if key not in groups:groups[key]=dict(values=values,queries=[])
            groups[key]["queries"].append(q)
        steps.append(dict(trial_index=j,
            query_sets={k:index_ranges(v) for k,v in sets.items()},
            complete_query_angle_metadata_groups=[
                [index_ranges(group["queries"])]+group["values"] for group in groups.values()]))
    return dict(global_original_counts_and_flags=scalar_fields(qr),
        original_last_query_angle_transaction=qr.get("last_query_angle_transaction"),
        first_direct_strict_parent_trial_histogram=qr.get("first_direct_strict_parent_trial_histogram"),
        actual_deferred_external_signals=qr.get("actual_deferred_external_signals"),
        method_meanings=dict(direct="all complete polynomial coefficients actually classified",
            inherited="same query/angle actual path restricted to a smaller closed interval",
            inherited_child_coefficient_box_directly_evaluated=False,
            unresolved_refuted_or_unavailable_parent_inherited=False),
        missing_endpoint_reason_strings=reasons,
        query_angle_metadata_columns=["query_ranges","complete_angle_rows",
            "proved_angle_count","refuted_angle_count","unresolved_angle_count",
            "direct_evaluation_count","inclusion_inheritance_count",
            "direct_strict_proof_count","inherited_strict_proof_count",
            "original_unvisited_angle_ranges","missing_endpoint_reason_index"],
        all17_steps=steps,all37_queries_explicit_in_every_step=True,
        integer_sets_only_no_inequality_recomputed=True,
        interval_witness_bounds_and_large_angle_tables_not_returned=True)


def error_log_metadata(path,work):
    """Necessary original error text/locations only; never stream a science log."""
    receipt=dict(file=path.relative_to(work).as_posix(),
        bytes=path.stat().st_size,sha256=file_sha(path))
    records=[];trace=False
    with path.open("rb") as stream:
        for number,raw in enumerate(stream,1):
            text=raw.decode("utf-8","surrogateescape")
            stripped=text.strip()
            if stripped.startswith("{"):
                trace=False
                try:value=json.loads(stripped)
                except (ValueError,TypeError):continue
                if not isinstance(value,dict):continue
                chosen={k:value[k] for k in ("error","exception","scientific_exception",
                    "original_exception","transport_error","traceback")
                    if k in value and value[k] not in (None,False,"",[],{})}
                if chosen:records.append(dict(original_line=number,event=value.get("event"),
                    original_error_fields=chosen))
            else:
                if stripped.startswith("Traceback (most recent call last):"):trace=True
                if trace or "error:" in stripped.lower() or stripped.startswith(
                        ("ValueError:","RuntimeError:","AssertionError:","MemoryError:")):
                    records.append(dict(original_line=number,original_text=text,
                        raw_line_bytes=len(raw),raw_line_sha256=sha(raw)))
            if len(encoded(records))>90000:
                raise ValueError("Necessary original error text exceeds one90000-byte summary: "+receipt["file"])
    return dict(original_log=receipt,necessary_error_records=records,
        complete_log_forwarded=False,no_scientific_log_payload_encoded=True)


def readback(helper,comp,work):
    """One <=90000-byte original scalar/range summary; no scientific recomputation."""
    output=dict(schema=SCHEMA,request=188,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),readback_complete=False,
        summary_complete=False,transport_complete=False,
        no_new_scientific_evaluation=True,original_model_gate_not_reclassified=True,
        new_semantic_segments_or_scientific_witness_reassembly=False)
    receipts=[]
    def existing(name):
        path=work/name
        if not path.is_file():return None
        receipts.append(dict(file=name,bytes=path.stat().st_size,sha256=file_sha(path)))
        return helper.read(path)
    code=70
    try:
        pipeline=existing("pipeline.json") or {}
        original=existing("original-pair-summary.json")
        result=existing("post-model-diagnostic/result.json") or {}
        diagnostic_summary=existing("post-model-diagnostic/summary.json")
        # Full in-job documents remain only as sources of necessary fields and
        # original identities. No complete scientific object is printed.
        full_summary=work/"post-model-diagnostic/summary-complete.json"
        if full_summary.is_file():
            receipts.append(dict(file=full_summary.relative_to(work).as_posix(),
                bytes=full_summary.stat().st_size,sha256=file_sha(full_summary)))
        batch=work/"batch-000";modeldir=batch/"thirty-seven-condensed-warm"
        if original is None:
            reader=helper.load("_request188_existing_original_selectors",
                comp/helper.READER_ENTRY,helper.READER_SHA)
            names=("batch-000/thirty-seven-condensed-warm/model-000.json",
                "batch-000/thirty-seven-condensed-warm/driver-status.json",
                "batch-000/thirty-seven-condensed-warm/condensed-QP-summary.json",
                "batch-000/physical-response/response-check.json")
            values=[existing(name) for name in names]
            if any(v is not None for v in values):
                original=helper.summarize(reader,values[0],values[1] or {},values[2],values[3])
        original=original or {}
        trials=original.get("all_original_trials") or []
        indices=[row["original_trial_index"] for row in trials]
        require(len(indices)==len(set(indices)) and all(isinstance(i,int) and 0<=i<17 for i in indices),
            "Every original visited trial has its declared one-of17 address")
        output["original_science"]=dict(
            metadata=take(original,("status","fixed_weight_merit_before",
                "model_damping","model_accepted","original_model_exit_code","original_FD_exit_code",
                "next_batch_eligible","stop_reason","input_pair","produced_pair","primary_outputs",
                "nearest_rejected_original_trial_index","native_at_current_height_solved",
                "new_full_DN_acceptance")),
            original_typed_queries=original.get("original_typed_queries"),
            all_original_visited_trial_scalar_records=[trial_scalar_record(row) for row in trials],
            original_model_before=domain_scalar_record(original.get("model_before")),
            original_visited_trial_ranges=index_ranges(indices),
            original_unvisited_trial_ranges=index_ranges(i for i in range(17) if i not in indices),
            original_QP_scalar_fields=scalar_fields(original.get("QP")),
            original_FD_readout=original.get("FD"),
            complete_large_trial_JSON_objects_not_returned=True,
            scalar_records_selected_by_unchanged_original_helper=True)
        output["pipeline"]=dict(scalar_fields(pipeline),
            exception=pipeline.get("exception"),active_child=pipeline.get("active_child"),
            children=[{**scalar_fields(row),
                "command":row.get("command"),"signals":row.get("signals")}
                for row in pipeline.get("children",[])])
        output["diagnostic"]=dict(
            original_counts_status_and_flags=scalar_fields(result),
            original_exception=result.get("scientific_exception"),
            original_cursor=result.get("active_cursor"),scope=result.get("scope"),
            actual_input_binding=result.get("complete_input_binding"),
            endpoint_private_adaptation=take(result.get("explicit_published_source_adaptation") or {},(
                "schema","published_source","independent_source","published_selected_design",
                "original175_parent_source","same_path_inclusion_proof","generated_private_module",
                "all_original_numerical_function_bodies_unchanged",
                "original170_main_scientific_order_retained_before_new_query_phase",
                "old_negative_sine_draft_not_used")),
            actual_source_pair=result.get("original_source_pair"),
            original_source_bindings=result.get("original_source_bindings"),
            original_capture_manifest=result.get("original_capture_manifest"),
            original_model_document=result.get("original_model_document"),
            temporary_ledger_identities=result.get("temporary_ledgers"),
            query_steps=query_step_metadata(result),
            pending_endpoint_reference_columns=["variant","node","original_angle_range"],
            pending_endpoint_reference_rows=[
                [r.get("endpoint_variant"),r.get("node"),r.get("angle_range")]
                for r in result.get("pending_reference_scopes",[])],
            pending_JP_variant_ranges=index_ranges(r["endpoint_variant"]
                for r in result.get("pending_complete_JP_action_variants",[])),
            pending_Hermite_formation_query_ranges=index_ranges(r["query_index"]
                for r in result.get("pending_complete_Hermite_formation_queries",[])),
            pending_original_pointwise_transfer_queries_by_step=[
                dict(trial_index=j,query_ranges=index_ranges(r["query_index"] for r in
                    result.get("pending_Hermite_transfer_pairs",[]) if r["trial_index"]==j))
                for j in range(17)],
            bounded_child_summary=take(diagnostic_summary or {},(
                "schema","scientific_completed","resource_partial","scientific_exception","stop_reason",
                "summary_complete","transport_complete","transport_error","original_summary_bytes",
                "original_summary_sha256","original_scientific_exit_code","process_exit_code",
                "post_model_diagnostic_exit_code")),
            result_is_not_a_gate_on_original_model_or_FD=True)
        capture=existing("batch-000/thirty-seven-condensed-warm/R354-query-domain-capture/capture.json")
        if isinstance(capture,dict):
            output["capture"]=dict(
                identity_and_status=take(capture,("schema","source_sha256","source_commit","run_id",
                    "source_input_warm","source_parent_status","query_specs","endpoint_nodes",
                    "midpoint_intervals","original_producer","original_observer","original_domain",
                    "original_FFT","original_engine","original_augmented","original_physical",
                    "original_model_returned","original_model_exit_code","original_exception",
                    "observation_complete","errors","original_runtime_aliases_restored")),
                actual_evaluations=len(capture.get("evaluations",[])),
                actual_angular_returns=len(capture.get("angular_returns",[])),
                actual_domains=len(capture.get("domains",[])),
                actual_final_directions=len(capture.get("chosen_directions",[])),
                full_scalar_cache_words_and_call_tables_retained_only_in_job=True)
        rule_result=work.parent/(work.name+"-rules")/"runner-result.json"
        if rule_result.is_file():
            rule=helper.read(rule_result)
            output["original_rule_monitor"]=dict(
                original_file=dict(bytes=rule_result.stat().st_size,sha256=file_sha(rule_result)),
                scalar_fields=scalar_fields(rule),
                error=rule.get("error"),exception=rule.get("exception"))
        logs={row.get("log_file"):row for row in pipeline.get("children",[])}
        output["necessary_original_errors"]=[]
        for base in (batch,work):
            if not base.is_dir():continue
            for path in sorted(base.glob("*.log")):
                rel=path.relative_to(work).as_posix()
                if logs.get(rel,{}).get("effective_return_code")!=0:
                    output["necessary_original_errors"].append(error_log_metadata(path,work))
        output.update(readback_complete=True,summary_complete=True,transport_complete=True,
            original_document_identities=receipts,
            no_complete_interval_witness_or_polynomial_vector_table_returned=True)
        raw=encoded(output)
        full=write(work/"bounded-readback-candidate.json",output)
        if len(raw)>90000:
            output=dict(schema=SCHEMA,request=188,run_id=os.environ.get("GITHUB_RUN_ID"),
                source_commit=os.environ.get("GITHUB_SHA"),readback_complete=False,
                summary_complete=False,transport_complete=False,process_exit_code=70,
                transport_error="necessary-single-summary-exceeds90000bytes",
                full_in_job_summary=full,original_document_identities=receipts,
                unreturned_scope="necessary17trial+37x17 query-status summary; no split fallback",
                original_model_gate_not_reclassified=True,no_new_scientific_evaluation=True)
        else:code=0
    except BaseException as error:
        output=dict(schema=SCHEMA,request=188,run_id=os.environ.get("GITHUB_RUN_ID"),
            source_commit=os.environ.get("GITHUB_SHA"),readback_complete=False,
            summary_complete=False,transport_complete=False,process_exit_code=70,
            error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()),
            original_document_identities=receipts,original_model_gate_not_reclassified=True,
            no_new_scientific_evaluation=True,
            original_full_outputs_retained_until_runner_destruction=True)
    raw=encoded(output)
    require(len(raw)<=90000,"The single summary or explicit incomplete-transport record must be bounded")
    receipt=write(work/"readback-summary.json",output)
    print("BEGIN_REQUEST188_NECESSARY_SCALAR_SUMMARY",flush=True)
    sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()
    print("END_REQUEST188_NECESSARY_SCALAR_SUMMARY",flush=True)
    emit("request188_necessary_scalar_summary_identity",dict(
        receipt=receipt,hash_includes_final_LF=True,readback_complete=code==0,
        raw_payloads_not_encoded_or_split=True,original_model_gate_not_reclassified=True))
    if code==0:
        write(work/"readback-complete.json",dict(schema=SCHEMA,request=188,
            summary=receipt,readback_complete=True,
            full_witness_data_intentionally_stayed_in_Actions=True))
    return code


def run(args,repo,comp,request,helper):
    # Starts before restoration, transport, original full J/model and FD.
    started=time.monotonic()
    deadline=started+request["global_science_seconds"]
    reserve=request["cleanup_readback_reserve_seconds"]
    work=bind_work(args.work,create=True)
    progress=dict(schema=SCHEMA,request=188,source_commit=os.environ.get("GITHUB_SHA"),
        run_id=os.environ.get("GITHUB_RUN_ID"),source_sha256=file_sha(__file__),
        request_sha256=file_sha(args.request),base_recipe_sha256=BASE_RECIPE_SHA,
        original_model_exit_code=None,original_FD_exit_code=None,
        post_model_diagnostic_exit_code=None,
        original_new_warm_FD_pair_completed=False,original_model_FD_attempt_returned=False,
        diagnostic_started=False,diagnostic_completed=False,
        diagnostic_completed_is_declared_responsibility_completion_not_all_direct_ranges=True,
        diagnostic_completed_not_closed_IEEE_or_native_certification=True,
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
        worker=load("_request188_original37_worker",comp/WORKER,WORKER_SHA)
        reader=helper.load("_request188_original_selectors",comp/helper.READER_ENTRY,helper.READER_SHA)
        inputs=work/"inputs";parent=work/"parent98"
        progress["original_inputs"]=helper.restore_inputs(repo,inputs);save()
        progress["original_parent"]=helper.restore_parent(comp,reader,parent,work);save()
        input_pair=worker.pair_identity(helper,parent)
        reports=work/"source-receipts";reports.mkdir()
        public=helper.load("_request188_original_public_source_restore",
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
        # Save the unchanged original scientific reports before diagnosis.
        # The final one-object readback includes all visited trial scalars;
        # never call the old helper's large-object semantic fallback.
        progress["original_primary_report_saved_before_diagnostic"]=True
        progress["original_scalar_readback_deferred_to_single_bounded_summary"]=True
        progress["independent_endpoint_baseline_sha256"]="84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a"
        progress["complete_closed_query_domain_188_not_original_gate"]=True
        save()
        capture=output/"R354-query-domain-capture"
        if (capture/"capture.json").is_file():
            remaining=deadline-time.monotonic()-reserve
            if remaining>60:
                consumer_seconds=min(request["diagnostic_seconds"],max(1,int(remaining-60)))
                command=[sys.executable,"-u",str(comp/CONSUMER),"--capture",str(capture),
                    "--model-directory",str(output),"--code-directory",str(comp),
                    "--seconds",str(consumer_seconds),"--max-ledger-bytes",
                    str(request["maximum_temporary_uncompressed_ledger_bytes"]),
                    "--out",str(work/"post-model-diagnostic")]
                progress["diagnostic_started"]=True
                progress["actual_diagnostic_seconds"]=consumer_seconds;save()
                diagnostic_code=helper.run_child("post-model-R398-nested-exact-diagnostic",
                    command,repo,env,work)
                progress["post_model_diagnostic_exit_code"]=diagnostic_code
                diag=work/"post-model-diagnostic"/"summary.json"
                if diag.is_file():
                    value=helper.read(diag)
                    progress["diagnostic_summary"]=value
                    progress["diagnostic_completed"]=value.get("scientific_completed") is True
                    progress["resource_partial"]=value.get("resource_partial") is True
            else:
                progress["diagnostic_not_started_reason"]="global resource deadline or insufficient60s result-finalization margin after original scientific attempt"
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
        emit("request188_one_original_pair_and_post_diagnostic_returned",dict(
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
    require(request.get("schema")==REQUEST_SCHEMA and request.get("request")==188
        and request.get("repository")==REPOSITORY,"Independent request188 identity")
    require(request["source_sha256"]==file_sha(__file__),"Actual orchestrator source")
    require(file_sha(comp/BASE_RECIPE)==BASE_RECIPE_SHA,"Original155 recipe retained, not relabelled")
    for name,digest in request["required_source_sha256"].items():
        require(Path(name).name==name and file_sha(comp/name)==digest,"Frozen source: "+name)
    for name,digest in request["required_parameter_sha256"].items():
        require(Path(name).name==name and file_sha(comp/name)==digest,"Frozen parameter: "+name)
    for name,digest in ((WORKER,WORKER_SHA),(HELPER,HELPER_SHA),(CAPTURE,CAPTURE_SHA),(CONSUMER,CONSUMER_SHA)):
        require(request["required_source_sha256"][name]==digest,"Actual new input source closure")
    require(request["global_science_seconds"]==10800 and request["cleanup_readback_reserve_seconds"]==300
        and request["diagnostic_seconds"]==5400
        and request["maximum_temporary_uncompressed_ledger_bytes"]==8589934592,
        "Explicit bounded independent diagnostic and original total resource allocation")
    helper=load("_request188_original37_support",comp/HELPER,HELPER_SHA)
    if args.mode=="run":return run(args,repo,comp,request,helper)
    if not args.work.exists():
        emit("request188_no_owned_scientific_payload",dict(mode=args.mode,
            scientific_child_not_inferred_to_have_run=True,no_cleanup_needed=True))
        return 0
    work=bind_work(args.work)
    if args.mode=="readback":return readback(helper,comp,work)
    require(args.mode=="cleanup","Explicit lifecycle dispatch")
    # Failure to finish readback is printed as such; cleanup is never silently
    # interpreted as a scientific result or an accepted candidate.
    marker=work/"readback-complete.json"
    emit("request188_owned_cleanup_begin",dict(
        work_directory=work.name,complete_readback_marker_present=marker.is_file(),
        unread_output_must_not_be_reported_as_complete=not marker.is_file()))
    require(marker.is_file(),"Read all surviving scalar/trial/range/error output before cleanup")
    shutil.rmtree(work)
    emit("request188_owned_cleanup_complete",dict(
        removed_directory=work.name,recomputable_raw_artifact_uploads=0,
        Release_uploads=0,Git_raw_publication=0))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
