#!/usr/bin/env python3
"""One necessary request208 scalar readback, after confirmed owned-process quiet.

Standard-library JSON/byte/metadata work only. No scientific import, model,
RHS, finite-root derivative, matrix action, norm, FD or audit is recomputed.
Original decisions remain authoritative. Large arrays and full root/row
witnesses remain temporary, with original identities only. One ASCII summary
must fit 90000 bytes; no semantic splitting or encoded-tree fallback.
"""
from __future__ import annotations
import argparse
from collections import deque
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import sys
import time
import traceback

SCHEMA="request208-original64-contracted-trace-r273-necessary-readback-v1"
MARKER="request208-owned-complete-necessary-readback-v1"
REQUEST_SCHEMA="public-six-control-contracted-trace-r273-request-v1"
LIMIT=90000
FULL="science/full-DN"
R273=FULL+"/true-tail-contracted-trace-r273"
TRIAL_COLUMNS=("call","iteration","trial","step","baseNorm","kind","trialNorm",
    "error","stage","rawCell","rawSegment","stageInputSHA256","stageInputBytes")
COUNTERS=("root_returns","zero_update_returns","normal_returns","fallback_returns",
    "original_root_evaluations","original_line_trials","differentiated_accepted_updates",
    "complete_local_jacobians")


def encode(value):
    return json.dumps(value,ensure_ascii=True,separators=(",",":"),allow_nan=False).encode("ascii")


def digest(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def identity(value):
    raw=json.dumps(value,ensure_ascii=True,sort_keys=True,separators=(",",":"),
                   allow_nan=True).encode("ascii")
    return dict(canonical_parsed_JSON_bytes=len(raw),
        canonical_parsed_JSON_sha256=hashlib.sha256(raw).hexdigest(),
        original_serialization_not_claimed=True)


def text(value,limit=1600):
    if not isinstance(value,str):return atom(value)
    raw=value.encode("utf-8","surrogateescape")
    if len(raw)<=limit:return value
    return dict(original_text_bytes=len(raw),original_text_sha256=hashlib.sha256(raw).hexdigest(),
        necessary_prefix=raw[:limit].decode("utf-8","surrogateescape"),
        text_not_returned_in_full=True,no_reassembly_protocol=True)


def atom(value):
    if isinstance(value,float) and not math.isfinite(value):
        return dict(original_nonfinite_JSON_token=repr(value))
    if isinstance(value,str):return text(value)
    if value is None or isinstance(value,(int,float,bool)):return value
    if isinstance(value,dict) and "float64le_hex" in value:
        return {k:atom(value[k]) for k in ("value","classification","float64le_hex") if k in value}
    return dict(only_original_object_identity=identity(value))


def selected(value,names):
    if not isinstance(value,dict):return None
    return {k:atom(value[k]) for k in names if k in value}


def scalars(value,exclude=()):
    if not isinstance(value,dict):return None
    return {k:atom(v) for k,v in value.items()
        if k not in exclude and (v is None or isinstance(v,(str,bool,int,float)))}


def small_original(value):
    """Small audit/domain structures only; numerical arrays are not serialized."""
    if not isinstance(value,dict):return atom(value)
    out=scalars(value)
    for k,v in value.items():
        if isinstance(v,dict):out[k]=small_original(v)
        elif isinstance(v,list):
            if len(v)<=8 and all(x is None or isinstance(x,(str,bool,int,float)) for x in v):
                out[k]=[atom(x) for x in v]
            else:out[k]=dict(count=len(v),original_object_identity=identity(v),
                large_numeric_or_nested_array_not_exported=True)
    return out


ADDRESS_LIST_KEYS=frozenset(("invalid_nodes","invalid_node_s","invalid_midpoint_intervals",
    "invalid_midpoint_s","invalid_boundary_rows","failed_nodes","failed_intervals",
    "unvisited_nodes","unvisited_intervals","unvisited_stages","unvisited_rows",
    "invalid_node_indices","invalid_midpoint_indices"))


def original_domain(value):
    """Retain actual failure addresses; never infer them from extrema or counts."""
    if not isinstance(value,dict):return atom(value)
    out=small_original(value)
    for key,member in value.items():
        if key in ADDRESS_LIST_KEYS and isinstance(member,list):
            out[key]=[atom(x) for x in member]
        elif isinstance(member,dict):
            out[key]=original_domain(member)
    return out


def root_failure(value):
    if not isinstance(value,dict):return atom(value)
    out=small_original(value)
    original=value.get("original_root_trace")
    if isinstance(original,dict):
        trace=small_original(original)
        for key in ("accepted_updates","line_decisions"):
            if isinstance(original.get(key),list):
                trace[key]=[scalars(x) if isinstance(x,dict) else atom(x)
                    for x in original[key]]
        out["original_root_trace"]=trace
    return out


def original_trial_coverage(traces,trials,response_calls):
    scopes={}
    for row in traces+trials:
        if not isinstance(row,dict):continue
        call=row.get("call");iteration=row.get("iteration")
        if type(call) is not int or type(iteration) is not int:continue
        if not 0<=iteration<32:continue
        key=(call,iteration);scopes.setdefault(key,set())
    for row in trials:
        if not isinstance(row,dict):continue
        key=(row.get("call"),row.get("iteration"));trial=row.get("trial")
        if key in scopes and type(trial) is int:scopes[key].add(trial)
    return dict(original_native_iteration_limit=32,original_trial_indices=list(range(10)),
        observed_iteration_scopes=[dict(call=key[0],iteration=key[1],
            actual_recorded_trial_indices=sorted(indices),
            trial_indices_without_original_record=[k for k in range(10) if k not in indices])
            for key,indices in sorted(scopes.items())],
        observed_protocol_response_count=len(response_calls),
        absent_trial_record_is_not_a_mathematical_refusal=True,
        unobserved_iterations_or_inflight_calls_not_invented=True)


def proc(pid):
    try:
        p=Path("/proc")/str(pid);raw=(p/"stat").read_text()
        x=raw[raw.rfind(")")+2:].split()
        return dict(pid=int(raw[:raw.find(" ")]),state=x[0],ppid=int(x[1]),
            pgid=int(x[2]),sid=int(x[3]),start_ticks=int(x[19]),uid=p.stat().st_uid)
    except (FileNotFoundError,ProcessLookupError):return None


def same_process(now,old):
    return (now is not None and isinstance(old,dict) and
        all(now.get(k)==old.get(k) for k in ("pid","start_ticks","pgid","sid")))


def group(pgid):
    members=[];errors=[]
    for path in Path("/proc").iterdir():
        if not path.name.isdigit():continue
        try:
            item=proc(int(path.name))
            if item is not None and item["pgid"]==pgid:members.append(item)
        except Exception as error:errors.append(dict(pid=path.name,error=repr(error)))
    return dict(members=members,live=[x for x in members if x["state"]!="Z"],errors=errors)


def quiet_owned(root,stop=False):
    """Only actual same-boot recorded PID/start/session identities may be signalled."""
    file=root/"process-status.json"
    answer=dict(quiescent=False,signals=[],readback_is_not_a_scientific_gate=True)
    if not file.is_file():
        return dict(**answer,reason="No actual process ownership receipt; raw is retained")
    receipt=json.loads(file.read_bytes())
    answer["original_receipt"]=dict(bytes=file.stat().st_size,sha256=digest(file))
    wrapper=receipt.get("wrapper_process") or receipt.get("parent_process")
    now=proc(wrapper["pid"]) if isinstance(wrapper,dict) and type(wrapper.get("pid")) is int else None
    if now is not None and not same_process(now,wrapper):
        return dict(**answer,reason="Wrapper PID reused; no signal sent")
    if now is not None and now["state"]!="Z":
        if not stop:return dict(**answer,reason="Original wrapper still alive",wrapper=now)
        if now["uid"]!=os.getuid() or now["pid"] in (os.getpid(),os.getppid()):
            return dict(**answer,reason="Original wrapper cannot safely be owned",wrapper=now)
        command=(Path("/proc")/str(now["pid"])/"cmdline").read_bytes()
        if (b"root_20261116_six_control_contracted_trace_r273_run.py" not in command
                or str(root).encode() not in command):
            return dict(**answer,reason="Recorded wrapper command is not this request")
        try:os.kill(now["pid"],signal.SIGTERM)
        except ProcessLookupError:pass
        answer["signals"].append(dict(pid=now["pid"],signal="TERM"))
        until=time.monotonic()+10
        while time.monotonic()<until:
            current=proc(now["pid"])
            if current is None or current["state"]=="Z":break
            if not same_process(current,wrapper):
                return dict(**answer,reason="Wrapper identity changed while waiting")
            time.sleep(.1)
        current=proc(now["pid"])
        if current is not None and current["state"]!="Z":
            try:os.kill(now["pid"],signal.SIGKILL)
            except ProcessLookupError:pass
            answer["signals"].append(dict(pid=now["pid"],signal="KILL"))
            time.sleep(.2)
    # Re-read after the wrapper's own finally may have finished.
    receipt=json.loads(file.read_bytes())
    answer["original_receipt_after_wrapper"]=dict(bytes=file.stat().st_size,sha256=digest(file))
    pgid=receipt.get("owned_child_pgid")
    if pgid is None:
        latest=proc(wrapper["pid"]) if isinstance(wrapper,dict) else None
        answer["quiescent"]=bool(receipt.get("scientific_child_not_started") and
            (latest is None or latest["state"]=="Z"))
        answer["scientific_child_not_started"]=receipt.get("scientific_child_not_started")
        return answer
    old=receipt.get("child_start")
    if (type(pgid) is not int or pgid<=1 or pgid==os.getpgrp()
            or receipt.get("exclusive_group_created_by_start_new_session") is not True
            or not isinstance(old,dict) or old.get("pid")!=pgid
            or old.get("pgid")!=pgid or old.get("sid")!=pgid
            or receipt.get("boot_id")!=Path("/proc/sys/kernel/random/boot_id").read_text().strip()):
        return dict(**answer,reason="Actual exclusive child ownership is incomplete")
    def observation():
        leader=proc(pgid);g=group(pgid)
        safe=(not g["errors"] and (leader is None or same_process(leader,old)) and
            all(x["sid"]==pgid and x["uid"]==os.getuid() and
                x["start_ticks"]>=old["start_ticks"] for x in g["members"]))
        return g,safe
    g,safe=observation();answer["group_before"]=g
    if not safe:return dict(**answer,reason="Owned group identity cannot be confirmed")
    if stop and g["live"]:
        for number,label in ((signal.SIGTERM,"TERM"),(signal.SIGKILL,"KILL")):
            g,safe=observation()
            if not safe:return dict(**answer,reason="Owned group identity changed")
            if not g["live"]:break
            try:os.killpg(pgid,number)
            except ProcessLookupError:pass
            answer["signals"].append(dict(pgid=pgid,signal=label))
            until=time.monotonic()+8
            while time.monotonic()<until:
                g,safe=observation()
                if not safe or not g["live"]:break
                time.sleep(.1)
    g,safe=observation();answer["group_after"]=g
    latest=proc(wrapper["pid"]) if isinstance(wrapper,dict) else None
    answer["quiescent"]=bool(safe and not g["live"] and
        (latest is None or latest["state"]=="Z"))
    answer["parent_rules_runner_group_not_signalled"]=True
    answer["launcher_reap_claim"]=receipt.get("owned_group_quiescent_after_return")
    return answer


class Reader:
    def __init__(self,root):
        self.root=root.resolve();self.files={};self.cache={};self.errors=[];self.log_errors=[]

    def path(self,name):
        p=self.root/name
        if p.is_symlink() or not p.resolve().is_relative_to(self.root):
            raise ValueError("Only original regular contained output files may be read")
        return p

    def record(self,p,raw=None):
        name=p.relative_to(self.root).as_posix()
        value=dict(bytes=p.stat().st_size,sha256=digest(p) if raw is None else hashlib.sha256(raw).hexdigest())
        if raw is not None and len(raw)!=value["bytes"]:raise ValueError("Original file changed during read")
        self.files[name]=value
        return dict(file=name,**value)

    def json(self,name):
        if name in self.cache:return self.cache[name]
        p=self.path(name)
        if not p.is_file():return None
        raw=p.read_bytes();self.record(p,raw)
        try:
            decoded=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
            result=json.loads(decoded);self.cache[name]=result;return result
        except Exception as error:
            self.errors.append(dict(file=name,error=repr(error),identity=self.files[name],
                original_text_prefix=text(raw.decode("utf-8","surrogateescape"),1000)))
            return None

    def jsonl(self,name):
        p=self.path(name)
        if not p.is_file():return []
        rows=[];h=hashlib.sha256();total=0
        with p.open("rb") as f:
            for line,raw in enumerate(f,1):
                h.update(raw);total+=len(raw)
                try:rows.append(json.loads(raw))
                except Exception as error:self.errors.append(dict(file=name,line=line,error=repr(error),
                    bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),text=text(raw.decode("utf-8","surrogateescape"),1000)))
        if total!=p.stat().st_size:raise ValueError("Original JSONL changed during read")
        self.files[name]=dict(bytes=total,sha256=h.hexdigest(),records=len(rows))
        return rows

    def log(self,name):
        p=self.path(name)
        if not p.is_file():return
        h=hashlib.sha256();total=0;first=[];last=deque(maxlen=3);window=0
        with p.open("rb") as f:
            for line,raw in enumerate(f,1):
                h.update(raw);total+=len(raw)
                hit=(re.search(rb"(Traceback|Error:|Exception|SyntaxError|FATAL|fatal|ResourcePartial)",raw)
                     and not raw.lstrip().startswith((b"{",b"[")))
                if b"Traceback" in raw:window=10
                if hit or window:
                    row=dict(line=line,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
                        original_text=text(raw.decode("utf-8","surrogateescape"),800))
                    if len(first)<6:first.append(row)
                    last.append(row)
                if window:window-=1
        if total!=p.stat().st_size:raise ValueError("Original log changed during read")
        self.files[name]=dict(bytes=total,sha256=h.hexdigest())
        if first or last:
            chosen={x["line"]:x for x in first+list(last)}
            self.log_errors.append(dict(file=name,identity=self.files[name],
                necessary_error_lines=list(chosen.values()),full_log_not_exported=True))


CONTRACTION_COUNTERS=("calls_started","calls_completed","preassemblies_started","preassemblies_completed",
    "contracted_updates_completed","explicit_original_fallbacks_started",
    "explicit_original_fallbacks_completed","complete_direction_columns_returned",
    "exact_backsolve_defect_components","exact_nonzero_backsolve_defect_components",
    "backsolve_defect_projection_changed_components",
    "nonzero_backsolve_defect_projection_lost_components",
    "backsolve_defect_projection_overflow_components","exact_zero_backsolve_defect_updates")
CONTRACTION_SCOPE=("schema","local_model","all_literal_Gram_moments_retained",
    "actual_recorded_factor_used_for_both_solves",
    "exact_backsolve_defect_formed_before_explicit_binary64_projection",
    "general_variable_defect_derivatives_silently_discarded",
    "binary64_word_equivalence_to_explicit_factor_loops_claimed",
    "contraction_roundoff_error_bound_paid","original_noJ_primal_modified",
    "zero_update_root_path_modified","numerical_fallback_is_original_195_factor_loop")


def contraction_stats(rows):
    """Only actual scalar counters/scope and last original fallback address."""
    totals={k:0 for k in CONTRACTION_COUNTERS};missing=[];reasons={};scopes={};unfinished=[]
    for row in rows:
        counters=row.get("counters")
        c=counters.get("factor_contraction") if isinstance(counters,dict) else None
        if not isinstance(c,dict):
            missing.append(dict(engine=row.get("engine_index"),counter="factor_contraction"));continue
        for key in CONTRACTION_COUNTERS:
            if type(c.get(key)) is int:totals[key]+=c[key]
            else:missing.append(dict(engine=row.get("engine_index"),counter=key))
        for reason,count in (c.get("fallback_reason_counts") or {}).items():
            if type(count) is int:reasons[reason]=reasons.get(reason,0)+count
            else:missing.append(dict(engine=row.get("engine_index"),fallback_reason=reason))
        declaration=selected(c,CONTRACTION_SCOPE)
        key=json.dumps(declaration,sort_keys=True,separators=(",",":"),allow_nan=False)
        scopes.setdefault(key,[]).append(row.get("engine_index"))
        if (c.get("last_numerical_fallback") is not None
                or c.get("calls_started")!=c.get("calls_completed")):
            unfinished.append(dict(engine_index=row.get("engine_index"),
                first_stage=row.get("first_stage"),stage_count=row.get("stage_count"),
                last_started_update=small_original(c.get("last_started_update")),
                last_numerical_fallback=small_original(c.get("last_numerical_fallback")),
                calls_started=c.get("calls_started"),calls_completed=c.get("calls_completed")))
    return dict(actual_integer_counter_totals=totals,actual_fallback_reason_counts=reasons,
        missing_counter_scopes=missing,
        declared_model_groups=[dict(scope=json.loads(k),actual_engine_indices=v) for k,v in scopes.items()],
        engines_with_unfinished_solve_or_last_fallback=unfinished,
        per_update_full_fallback_history_not_recorded=True,
        original_primal_values_or_new_error_bounds_not_reconstructed=True,
        counters_do_not_prove_complete_current_J_or_native_acceptance=True)


def trace_stats(value):
    if not isinstance(value,dict):return None
    rows=value.get("engines",[])
    totals={k:0 for k in COUNTERS};hist=[0]*30;missing=[];schemas=set();sources={}
    for row in rows:
        c=row.get("counters")
        if not isinstance(c,dict):
            missing.append(row.get("engine_index"));continue
        schemas.add(c.get("schema"))
        for k in COUNTERS:
            if type(c.get(k)) is int:totals[k]+=c[k]
            else:missing.append(dict(engine=row.get("engine_index"),counter=k))
        h=c.get("return_iteration_histogram")
        if isinstance(h,list) and len(h)==30 and all(type(x) is int for x in h):
            for i,x in enumerate(h):hist[i]+=x
        else:missing.append(dict(engine=row.get("engine_index"),counter="histogram"))
        key=(row.get("implementation"),row.get("local_field_source_sha256"),
            row.get("stage_variation_source_sha256"),row.get("original_noJ_RK_source_sha256"))
        sources.setdefault(key,[]).append(row.get("engine_index"))
    return dict(actual_engine_count=len(rows),original_all576_stages_addressed=value.get("all576_stages_addressed"),
        metadata_counter_totals=totals,return_iteration_histogram=hist,
        recorded_factor_contraction=contraction_stats(rows),
        missing_counter_scopes=missing,counter_schemas=sorted(x for x in schemas if isinstance(x,str)),
        original_full_statistics_identity=identity(value),
        implementation_groups=[dict(implementation=k[0],local_field_source_sha256=k[1],
            stage_variation_source_sha256=k[2],original_noJ_RK_source_sha256=k[3],
            actual_engine_indices=v) for k,v in sources.items()],
        only_integer_metadata_counts_added=True,counters_are_cumulative_actual_calls_not_unique_states=True,
        all_stage_variations_or_final_J_not_inferred_from_counters=True)


def maximum(value):
    if not isinstance(value,dict):return None
    absolute=value.get("exact_absolute_scaled_residual") or {}
    signed=value.get("exact_signed_scaled_residual") or {}
    out=selected(value,("kind","node","row","global_equation_row","component","mode","original_sigma_float64le_hex"))
    out.update(absolute_decimal=absolute.get("decimal_display_64_significant_digits"),
        signed_decimal=signed.get("decimal_display_64_significant_digits"),
        original_full_witness_identity=identity(value),decimal_is_only_original_display=True)
    return out


def current_corrections(r):
    base=r.path(R273)
    if not base.is_dir():return dict(started=False,completed_current_directions_not_observed=True)
    lifetime=r.json(R273+"/live-current-corrections-summary.json")
    client=r.json(R273+"/contracted-trace-r273-client-summary.json")
    manifest=r.json(R273+"/finite-trace-source-manifest.json")
    calls=[];iterations=[]
    for cd in sorted(base.glob("call-*")):
        if not cd.is_dir() or not re.fullmatch(r"call-[0-9]+",cd.name):continue
        cr=cd.relative_to(r.root).as_posix()
        context=r.json(cr+"/request.json");summary=r.json(cr+"/current-correction-summary.json") or {}
        ret=r.json(cr+"/finite-trace-native-return.json")
        journal=r.jsonl(cr+"/current-corrections.jsonl")
        by={x.get("nonlinear_iteration"):x for x in journal if isinstance(x,dict)}
        calls.append(dict(call=summary.get("native_call"),directory=cr,
            request_identity=None if context is None else identity(context),
            snapshots_completed=summary.get("snapshots_completed"),directions_returned=summary.get("directions_returned"),
            actual_bridge_failure=atom(summary.get("actual_bridge_failure")),
            native_completion=None if ret is None else dict(kind=ret.get("kind"),
                original_return=small_original(ret.get("original_return")),
                original_failure=root_failure(ret.get("original_failure"))),
            finite_trace_statistics=trace_stats((ret or summary).get("finite_trace_statistics")),
            original_journal_rows=len(journal)))
        for it in sorted(cd.glob("iteration-*")):
            if not it.is_dir() or not re.fullmatch(r"iteration-[0-9]+",it.name):continue
            rel=it.relative_to(r.root).as_posix();index=int(it.name.split("-")[-1])
            snapshot=r.json(rel+"/snapshot/result.json") or {}
            context=r.json(rel+"/snapshot/context.json.gz")
            returned=r.json(rel+"/returned-correction.json") or {}
            qr=r.json(rel+"/qr/summary.json") or {}
            exit_=r.json(rel+"/qr-exit.json")
            launch=r.json(rel+"/qr-launch.json")
            failure=r.json(rel+"/bridge-failure.json")
            retired=r.json(rel+"/temporary-payload-retirement.json")
            retire_error=r.json(rel+"/temporary-retirement-failure.json")
            original=by.get(index) or failure or {}
            exact=qr.get("original_exact_readback") or {}
            r.log(rel+"/qr.stderr.log");r.log(rel+"/qr.stdout.log")
            iterations.append(dict(directory=rel,native_call=original.get("native_call",snapshot.get("native_call")),
                iteration=index,snapshot_sequence=original.get("snapshot_sequence",snapshot.get("snapshot_sequence")),
                snapshot_completed=original.get("snapshot_completed",snapshot.get("snapshot_completed")),
                linear_direction_returned=original.get("linear_direction_returned"),
                current_state_sha256=original.get("current_state_sha256",snapshot.get("current_state_sha256")),
                source_current_withJ_norm=atom(original.get("source_current_withJ_norm",snapshot.get("actual_current_original_norm"))),
                current_minA=atom(snapshot.get("actual_current_original_minA")),
                current_minD=atom(snapshot.get("actual_current_original_minD")),
                current_context_identity=None if context is None else identity(context),
                new_matrix_identity_sha256=returned.get("new_matrix_identity_sha256",qr.get("new_matrix_identity_sha256")),
                native_delta_sha256=(returned.get("native_delta") or qr.get("native_delta") or {}).get("sha256"),
                QR_exit=small_original(exit_),QR_launch_identity=None if launch is None else identity(launch),
                QR_status=selected(qr,("diagnostic_completed","linear_direction_computed","eta_cli_text",
                    "elapsed_seconds","maximum_RSS_kib","actual_error")),
                factor_summary=small_original(qr.get("factor_summary")),
                exact_readback=selected(exact,("exact_rows","completed_stages","original_product_positions",
                    "direction_float64le_sha256","used_as_new_nonlinear_acceptance_gate")),
                exact_affine_maximum=maximum(exact.get("exact_global_original_sigma_norm")),
                exact_stored_base_maximum=maximum(exact.get("exact_stored_base_sigma_norm")),
                exact_ledger_identity=exact.get("all_exact_residual_rows"),
                formed_model_diagnostic=small_original(qr.get("formed_model_diagnostic")),
                actual_error=atom(original.get("actual_error")),bridge_failure=small_original(failure),
                retirement=selected(retired,("removed_file_count","removed_bytes","retirement_completed")),
                retirement_error=small_original(retire_error)))
    return dict(started=True,client=selected(client,("schema","original_protocol_calls",
            "actual_error","actual_worker_exit_code","elapsed_seconds","tangent_implementation")),
        external_calls=None if not isinstance(client,dict) else
            [scalars(x) for x in client.get("external_calls",[])],
        source_manifest=small_original(manifest),
        final_statistics=trace_stats((lifetime or {}).get("finite_trace_statistics")),
        call_completions=calls,all_observed_current_corrections=iterations,
        correction_count=len(iterations),no_retired_matrix_or_factor_payload_reopened=True,
        exact_affine_readback_not_a_noJ_derivative_or_native_gate=True,
        protocol_source_and_complete_native_responses_remain_authoritative=True)


def native(r):
    calls=[];base=r.path(FULL);first_height=None
    if base.is_dir():
        for path in sorted(base.glob("true-tail_[0-9][0-9][0-9][0-9].json.gz")):
            rel=path.relative_to(r.root).as_posix();v=r.json(rel)
            if not isinstance(v,dict):continue
            req=v.get("request") or {};res=v.get("response") or {};jets=res.get("jets")
            if first_height is None:first_height=req.get("height")
            checkpoint=res.get("checkpoint");J=res.get("heightJetJacobian")
            calls.append(dict(file=rel,original_file=r.files[rel],
                request=selected(req,("jacobian","audit")),height_identity=identity(req.get("height")),
                response=selected(res,("converged","failed","residual","lastIteration","iterations",
                    "actual_nonlinear_solve","finite_tail_only","error","message")),
                last_iteration=small_original(res.get("lastIteration")),
                history_count=len(res["history"]) if isinstance(res.get("history"),list) else None,
                full_J_present=J is not None,full_J_scalar_count=len(J) if isinstance(J,list) else None,
                full_J_identity=None if J is None else identity(J),
                all112_jet_identities=None if not isinstance(jets,dict) else
                    {k:identity(jets[k]) for k in ("height","slope","second") if k in jets},
                means=selected(jets,("meanSlope","meanSecond","meanSlopeCorrection","meanSecondCorrection")),
                cut_jet_scalar_fields=scalars(jets),audit=small_original(res.get("audit")),
                checkpoint_present=isinstance(checkpoint,dict),
                checkpoint_identity=None if checkpoint is None else identity(checkpoint),
                source_map_identity=identity(v.get("source_sha256")),seconds=v.get("seconds")))
    traces=r.jsonl(FULL+"/true-tail_trace.jsonl");trials=r.jsonl(FULL+"/true-tail_trials.jsonl")
    ready=r.json(FULL+"/true-tail_ready.json.gz")
    selected_trace=[]
    for row in traces:
        if not isinstance(row,dict):continue
        x=scalars(row,("time",))
        if "height" in row:x["height_identity"]=identity(row["height"])
        if "finite_trace_failure" in row:x["finite_trace_failure"]=root_failure(row["finite_trace_failure"])
        for k in ("lastIteration","finite_trace_variation","original_root_trace"):
            if k in row:x[k]=small_original(row[k])
        selected_trace.append(x)
    r.log(FULL+"/true-tail_stderr.log");r.log("science-stdout-stderr.log")
    ready_short=selected(ready,("event","tailJacobian","tailPredictor","cut"))
    if isinstance(ready,dict):
        ready_short["parameters"]=scalars(ready.get("parameters"))
        ready_short["storedMetricAdapter"]=scalars(ready.get("storedMetricAdapter"))
    return dict(ready=ready_short,first_actual_requested_H=first_height,
        actual_protocol_response_records=calls,all_original_trace_scalar_events=selected_trace,
        all_original_trial_columns=list(TRIAL_COLUMNS),
        all_original_trial_rows=[[atom(row.get(k)) for k in TRIAL_COLUMNS] for row in trials],
        actual_original_trial_count=len(trials),all_stored_native_responses_retained_in_scope=True,
        trial_scope=original_trial_coverage(traces,trials,calls),
        full338_by112_J_and_two_means_not_inferred_from_any_stage_counter=True)


def height_path(r):
    v=r.json("science/height-path/height-path-status.json")
    if not isinstance(v,dict):return None
    out=selected(v,("schema","phase","complete_endpoint","resource_partial","last_converged_s",
        "last_converged_call","completed_bootstrap_request_count","proposed_increment",
        "original_full_DN_accepted","final_original_audit_done_by_bootstrap",
        "current_withJ_implementation","same_worker_and_owner"))
    out["H_star"]=v.get("H_star")
    out["H_star_identity"]=v.get("H_star_array")
    out["policy"]=v.get("policy")
    out["requests"]=[]
    for x in v.get("requests",[]):
        row=selected(x,("request_index","native_call","phase","proposed_s","previous_converged_s",
            "proposed_increment","requested_jacobian","requested_audit","exact_H_star_copy","zero_request",
            "accepted","response_observed","original_request_seconds","original_trace_count",
            "original_trial_count","mathematical_refusal","original_python_cache_unchanged",
            "python_exception","binding_or_protocol_exception"))
        row["requested_H_identity"]=x.get("requested_H")
        row["original_record"]=x.get("original_record")
        row["response"]=small_original(x.get("original_response"))
        context=x.get("existing_failure_context") or {}
        row["source_failure_context"]=scalars(context)
        out["requests"].append(row)
    return out


def summarize(r,request,recipe):
    process=r.json("process-status.json");adapter=r.json("science/adapter-status.json")
    driver=r.json(FULL+"/driver-status.json");result=r.json(FULL+"/actual.json.gz")
    fd=r.json("science/actual-H-response/response-check.json")
    seed=r.json("science/initial-guess/prepared.json.gz")
    out=dict(process=selected(process,("phase","scientific_wall_clock_seconds","scientific_child_returncode",
        "wrapper_returncode","elapsed_seconds","budget_exhausted","external_signal","exception",
        "owned_group_quiescent_after_return","engineering_readback_incomplete")),
        adapter=selected(adapter,("schema","phase","success","new_coupled_finite_acceptance",
            "full_Cartesian_closed_surface","prepared_sha256","initial_collocation_max",
            "original_boundary_FD_passed","maximum_boundary_FD_relative_error","response_check_sha256",
            "original_full_DN_exit_status","original_full_DN_phase","native_live_calls",
            "native_owner_close_attempted","native_owner_closed","native_owner_close_exception",
            "native_close_exception","exception","height_path_outcome","height_path_resource_partial",
            "height_path_endpoint_completed","original_FD_or_full_DN_entered_after_height_path_stop")),
        actual_H=None if not isinstance(adapter,dict) else adapter.get("actual_current_H"),
        initial_guess=None if not isinstance(seed,dict) else dict(
            scalar_fields=selected(seed,("M","N","initial_collocation_max","preflight_added_nodes",
                "success","new_coupled_finite_acceptance","true_nonzero_native_parent_claimed")),
            original_mesh_node_count=len(seed.get("mesh",[])),
            full_original_object_identity=identity(seed)),
        boundary_FD=selected(fd,("implementation_check_passed","verification_threshold",
            "maximum_relative_directional_error","maximum_second_order_relative_directional_error",
            "maximum_fourth_order_relative_directional_error","second_order_truncation_contracts",
            "actual_current_H_solved_before_this_FD","FD_perturbed_states_use_explicit_affine_map",
            "zero_anchor_J_not_relabelled_as_current_H_J","same_live_client_will_be_retained_if_FD_passes",
            "native_anchor_response_sha256")),
        boundary_FD_groups=None if not isinstance(fd,dict) else {k:small_original(fd.get(k))
            for k in ("direct_boundary","separated_boundary")},
        original_full_DN=selected(driver,("phase","state_dimension","physical_state_dimension","left_rows",
            "right_rows","nodes","initial_collocation_max","preflight_added_nodes","current_outer_iteration",
            "new_coupled_finite_acceptance","physical_RMS_max","physical_node_relative_residual",
            "actual_result_sha256","height_seam","elapsed_seconds","exception")),
        accepted_result=selected(result,("success","status","message","M","N","fixed_modes","end","seconds",
            "collocation_rms_max","boundary_residual_max","physical_frozen_control_RMS_max",
            "physical_node_relative_residual","constant_core_state_drift","constant_parameter_state_drift",
            "height_seam","full_Cartesian_closed_surface")),
        original_outer_history=None if not isinstance(driver,dict) else
            [original_domain(x) for x in (driver.get("outer_history") or [])],
        full_result_identity=None if result is None else identity(result))
    out["preflight"]={}
    for label,name in (("initial","science/initial-guess/RMS-domain-preflight.json"),
                        ("fullDN",FULL+"/RMS-domain-preflight.json")):
        v=r.json(name)
        out["preflight"][label]=None if v is None else dict(
            scalar_fields=scalars(v),actual_query_minima=original_domain(v.get("actual_query_minima")),
            history=[original_domain(x) for x in (v.get("history") or [])],
            full_original_identity=identity(v))
    evaluations=r.jsonl(FULL+"/original-newton-domain-evaluations.jsonl")
    out["all_original_full_DN_evaluations"]=[original_domain(x) for x in evaluations]
    out["native"]=native(r);out["height_path"]=height_path(r)
    out["current_R273"]=current_corrections(r)
    bands=[];base=r.path(FULL+"/banded-linear")
    if base.is_dir():
        for file in sorted(base.glob("factor-*-solve-*.json")):
            v=r.json(file.relative_to(r.root).as_posix())
            bands.append(small_original(v))
    out["all_original_banded_solve_reports"]=bands
    out["missing_phases_are_not_passed"]=True
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("directory","request","recipe","out"):p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--rules-directory",type=Path);p.add_argument("--compute-outcome",default="unknown")
    args=p.parse_args();temporary=Path(os.environ["RUNNER_TEMP"]).resolve()
    root=args.directory.resolve();out=args.out.resolve()
    if (root==temporary or not root.is_relative_to(temporary) or args.directory.is_symlink()
            or out==temporary or not out.is_relative_to(temporary) or out.is_relative_to(root) or out.exists()):
        raise ValueError("Use a fresh contained sibling readback output")
    out.mkdir(parents=True)
    summary=dict(schema=SCHEMA,request=208,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),reader_sha256=digest(__file__),
        request_sha256=digest(args.request),recipe_sha256=digest(args.recipe),
        compute_step_outcome=args.compute_outcome,summary_complete=False,transport_complete=False,
        original_acceptance_not_reclassified=True,no_new_scientific_computation=True,
        full_root_tapes_arrays_and_exact_ledgers_not_exported=True,
        no_semantic_segments_or_encoded_scientific_tree=True,errors=[])
    try:
        request=json.loads(args.request.read_bytes());recipe=json.loads(args.recipe.read_bytes())
        if request.get("schema")!=REQUEST_SCHEMA:raise ValueError("Wrong request208 schema")
        if summary["recipe_sha256"]!=request["parameter_recipe"]["sha256"]:
            raise ValueError("The actual recipe identity differs")
        summary["source_and_policy"]=dict(source_count=len(request["source_sha256"]),
            source_manifest_identity=identity(request["source_sha256"]),
            inputs={k:{"bytes":v["bytes"],"sha256":v["sha256"]} for k,v in request["inputs"].items()},
            initial_six_parameters=recipe["initial_six_parameters"],lambda_target=recipe["lambda_target"],
            execution=request["execution"],finite_trace_tangent=request["finite_trace_tangent"],
            R273=request["r273"],proof=request["finite_trace_proof"],
            recorded_factor_contraction_proof=request["recorded_factor_contraction_proof"])
        before=quiet_owned(root,stop=True);summary["owned_processes_before_read"]=before
        if not before["quiescent"]:
            raise RuntimeError("Owned science or wrapper is not proved quiet; mutable science not read or deleted")
        r=Reader(root);summary["actual"]=summarize(r,request,recipe)
        summary["errors"].extend(r.errors)
        summary["necessary_original_error_text"]=r.log_errors
        summary["selected_original_file_identities"]=r.files
        if args.rules_directory is not None:
            rules=args.rules_directory.resolve()
            if rules==temporary or not rules.is_relative_to(temporary) or args.rules_directory.is_symlink():
                raise ValueError("Only actual owned rules receipts may be read")
            rr=Reader(rules);v=rr.json("runner-result.json")
            summary["rules"]=small_original(v);summary["rule_file_identities"]=rr.files
            summary["errors"].extend(rr.errors)
        after=quiet_owned(root,stop=False);summary["owned_processes_after_read"]=after
        summary["summary_complete"]=bool(not summary["errors"] and before["quiescent"] and after["quiescent"])
    except Exception as error:
        summary["errors"].append(dict(error=repr(error),traceback=text(traceback.format_exc(),2400)))
    summary["transport_complete"]=summary["summary_complete"]
    raw=encode(summary)
    full=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    if len(raw)>LIMIT:
        summary["summary_complete"]=False;summary["transport_complete"]=False
        (out/"full-necessary-projection.json").write_bytes(encode(summary)+b"\n")
        summary=dict(schema=SCHEMA,request=208,run_id=summary["run_id"],source_commit=summary["source_commit"],
            reader_sha256=summary["reader_sha256"],request_sha256=summary["request_sha256"],
            recipe_sha256=summary["recipe_sha256"],summary_complete=False,transport_complete=False,
            reason="Necessary single summary exceeded90000 bytes; no splitting/reassembly permitted",
            over_limit_projection_identity=full,original_acceptance_not_reclassified=True,
            raw_retained_until_runner_destruction=True,
            process=(summary.get("actual") or {}).get("process"),
            adapter=(summary.get("actual") or {}).get("adapter"),
            no_partial_trial_table_claimed_complete=True)
        raw=encode(summary)
    if len(raw)>LIMIT:raise RuntimeError("Necessary fallback itself exceeded the fixed transport limit")
    (out/"scalar-summary.json").write_bytes(raw+b"\n")
    print("BEGIN_REQUEST208_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY",flush=True)
    print(raw.decode("ascii"),flush=True)
    print("END_REQUEST208_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY",flush=True)
    print(encode(dict(event="request208_necessary_summary_identity",bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest(),hash_includes_final_LF=False,
        summary_complete=summary["summary_complete"],transport_complete=summary["transport_complete"],
        original_science_status_independent_of_transport=True)).decode(),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a",encoding="utf-8") as f:
            f.write("scalar_summary="+raw.decode("ascii")+"\n")
            f.write("scalar_summary_bytes="+str(len(raw))+"\n")
            f.write("scalar_summary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
    if summary["summary_complete"]:
        marker=dict(schema=MARKER,run_id=summary["run_id"],source_commit=summary["source_commit"],
            request_sha256=summary["request_sha256"],recipe_sha256=summary["recipe_sha256"],
            reader_sha256=summary["reader_sha256"],execution_directory=str(root),
            owned_processes_quiescent=True,necessary_single_summary_complete=True,
            scalar_summary=dict(bytes=len(raw)+1,sha256=digest(out/"scalar-summary.json")),
            no_independent_large_array_or_full_witness_audit_claim=True)
        (out/"readback-complete.json").write_bytes(encode(marker)+b"\n")
    return 0 if summary["summary_complete"] and summary["transport_complete"] else 70


if __name__=="__main__":
    raise SystemExit(main())
