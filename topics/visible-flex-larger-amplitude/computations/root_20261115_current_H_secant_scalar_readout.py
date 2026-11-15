#!/usr/bin/env python3
"""One bounded necessary Request172 summary from existing Actions output.

Standard-library metadata readback only. No scientific import or arithmetic.
Read source JSON/JSONL/logs internally; export necessary original scalar
decisions and exact-consumer decimal maxima/locations, not reconstructible
chunks of large objects. Full dyadic witnesses, arrays and large stdout are
not exported. Explicit incomplete-summary status prevents active cleanup.
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
import sys
import traceback

SCHEMA="request172-current-H-necessary-secant-scalar-readback-v2"
INCOMPLETE_SCHEMA="request172-current-H-necessary-secant-readback-incomplete-v2"
REQUEST_SCHEMA="public-six-control-current-H-secant-request-v1"
MARKER_SCHEMA="request172-necessary-owned-scalar-readback-marker-v2"
LIMIT=90000
METRICS=("withJ_base","noJ_base","trial","ideal_affine",
         "baseline_path_difference","state_formation","finite_secant",
         "total_difference","realized_affine")


def encode(value):
    return json.dumps(value,ensure_ascii=True,separators=(",",":"),allow_nan=False).encode("ascii")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def object_identity(value):
    raw=json.dumps(value,sort_keys=True,ensure_ascii=True,separators=(",",":"),
                   allow_nan=True).encode("ascii")
    return dict(parsed_JSON_bytes=len(raw),parsed_JSON_sha256=hashlib.sha256(raw).hexdigest(),
                scope="canonical parsed object, not original file bytes")


def atom(value):
    if isinstance(value,float) and not math.isfinite(value):
        return dict(original_nonfinite_JSON_token=repr(value))
    if value is None or isinstance(value,(str,int,float,bool)):return value
    if isinstance(value,dict) and "float64le_hex" in value:
        return [atom(value.get("value")),value.get("classification"),value.get("float64le_hex")]
    return dict(not_a_scalar=True,identity=object_identity(value))


def small_text(text,limit=1200):
    if not isinstance(text,str):return atom(text)
    raw=text.encode("utf-8","surrogateescape")
    if len(raw)<=limit:return text
    return dict(original_bytes=len(raw),original_sha256=hashlib.sha256(raw).hexdigest(),
        selected_prefix_bytes=limit,selected_prefix=raw[:limit].decode("utf-8","surrogateescape"),
        remaining_text_not_exported=True,not_a_reconstruction_protocol=True)


def error_view(value):
    if value is None:return None
    if isinstance(value,str):return small_text(value)
    if not isinstance(value,dict):return dict(identity=object_identity(value))
    wanted=("type","name","message","error","stage","rawCell","rawSegment",
            "tailStage","tailRawCell","tailRawSegment","where","code","resource_partial")
    out={k:small_text(value[k]) if isinstance(value[k],str) else atom(value[k])
         for k in wanted if k in value}
    if not out:out["identity"]=object_identity(value)
    omitted=[k for k in value if k not in wanted]
    if omitted:out["other_error_fields_identity"]=object_identity({k:value[k] for k in omitted})
    return out


def fields(value,names):
    if not isinstance(value,dict):return None
    return {k:error_view(value[k]) if k in ("error","exception","actual_error") else atom(value[k])
            for k in names if k in value}


def packet(label,value):
    """Only a complete independently small metadata record; never large chunks."""
    raw=encode(dict(event="request172-small-metadata",label=label,value=value))
    if len(raw)>LIMIT:raise ValueError("No encoding or chunking of a large object is permitted")
    print(raw.decode("ascii"),flush=True)
    return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def proc(pid):
    try:
        raw=(Path("/proc")/str(pid)/"stat").read_text()
        fields=raw[raw.rfind(")")+2:].split()
        return dict(pid=int(raw[:raw.find(" ")]),state=fields[0],
            ppid=int(fields[1]),pgid=int(fields[2]),sid=int(fields[3]),start_ticks=int(fields[19]))
    except (FileNotFoundError,ProcessLookupError):return None


def group_observation(pgid):
    values=[];errors=[]
    for path in Path("/proc").iterdir():
        if not path.name.isdigit():continue
        try:
            item=proc(int(path.name))
            if item is not None and item["pgid"]==pgid:values.append(item)
        except Exception as error:errors.append(dict(pid=path.name,error=repr(error)))
    live=[item for item in values if item["state"]!="Z"]
    return dict(pgid=pgid,members=values,live_members=live,read_errors=errors,
                quiescent=not live and not errors,
                only_the_original_exclusive_child_group_observed=True)


def owner_observation(root):
    file=root/"process-status.json"
    if not file.is_file():
        return dict(quiescent=False,reason="No actual launcher process receipt",
                    no_process_signalled=True)
    value=json.loads(file.read_bytes())
    pgid=value.get("owned_child_pgid")
    if pgid is None:
        return dict(quiescent=bool(value.get("scientific_child_not_started")),
                    original_status_phase=value.get("phase"),no_owned_group_declared=True,
                    no_process_signalled=True)
    if (type(pgid) is not int or pgid<=1
            or value.get("exclusive_group_created_by_start_new_session") is not True):
        return dict(quiescent=False,reason="Exclusive group ownership is not proved",
                    original_receipt=value,no_process_signalled=True)
    current=group_observation(pgid)
    prior=value.get("child_start")
    leader=proc(pgid)
    if leader is not None and prior is not None and leader["start_ticks"]!=prior["start_ticks"]:
        current["quiescent"]=False
        current["unknown_reused_leader_identity"]=True
    current["launcher_recorded_quiescent"]=value.get("owned_group_quiescent_after_return")
    current["quiescent"]=bool(current["quiescent"] and value.get("owned_group_quiescent_after_return"))
    current["no_process_signalled"]=True
    current["parent_shared_runner_group_not_required_to_be_empty"]=True
    return current

def maximum_view(value):
    if value is None:return None
    ratio=value.get("exact_original_sigma_absolute")
    return [None if not isinstance(ratio,dict) else ratio.get("decimal68"),
        value.get("global_equation_row"),value.get("kind"),value.get("node"),
        value.get("row_in_block"),value.get("coordinate")]


def norm_comparison(value):
    if not isinstance(value,dict):return None
    diff=value.get("absolute_printed_norm_minus_exact_sigma_max")
    # Exact sigma maxima already appear once in global_maxima.
    return [atom(value.get("original")),
        diff.get("decimal68") if isinstance(diff,dict) else None,
        value.get("original_printed_norm_nonfinite"),
        object_identity(value)]

class Collector:
    def __init__(self,root,label,quiescent):
        self.root=root.resolve();self.label=label;self.quiescent=bool(quiescent)
        self.inventory=[];self.errors=[];self.groups={};self.cache={}
        self.trace_rows=[];self.native_trial_rows=[];self.logs=[];self.failure_text=[]
        self.rules=[];self.other_failures=[]
        self.counts=dict(JSON_files=0,JSONL_files=0,JSONL_lines=0,malformed_JSON_records=0,
            log_files=0,log_bytes_read=0,bulk_files_stat_only=0,bulk_bytes_stat_only=0)
        self.report_counts=dict(exact_iterations=0,complete_exact_iterations=0,
            partial_exact_iterations=0,trial_reports=0,whole_row_trial_reports=0,
            actual_original_trials=0,actual_extra_trials=0,baselines=0,
            complete_noJ_returns=0,unreturned_noJ=0)

    def relative(self,path):
        path=Path(path)
        if path.is_symlink() or not path.resolve().is_relative_to(self.root):
            raise ValueError("Only a regular contained original file may be read")
        return path.relative_to(self.root).as_posix()

    def identity(self,path):
        return dict(file=self.relative(path),bytes=path.stat().st_size,sha256=sha(path))

    def group(self,path):
        relative=Path(self.relative(path))
        index=next((i for i,p in enumerate(relative.parts) if re.fullmatch(r"iteration-[0-9]+",p)),None)
        if index is None:return None
        name=Path(*relative.parts[:index+1]).as_posix()
        if name not in self.groups:
            self.groups[name]=dict(directory=name,model=None,loop=None,result=None,
                baseline=None,observations={},trials={},files={})
        return self.groups[name]

    def remember(self,path,value,identity):
        relative=self.relative(path)
        if relative in ("process-status.json","science/adapter-status.json",
                "science/full-DN/driver-status.json","science/height-path/height-path-status.json",
                "science/actual-H-response/response-check.json"):
            self.cache[relative]=value
        if not isinstance(value,dict):return
        schema=value.get("schema","");g=self.group(path)
        if schema=="current-H-secanted-model-input-v1" and g is not None:
            g["model"]=fields(value,("native_call","nonlinear_iteration","snapshot_sequence",
                "current_state_sha256","new_matrix_identity_sha256","original_withJ_norm"))
            g["files"]["model"]=dict(bytes=identity["bytes"],sha256=identity["sha256"])
        elif schema=="current-H-actual-ten-trial-loop-observation-v1" and g is not None:
            g["loop"]=fields(value,("original_trials_visited","all_original_ten_visited",
                "original_loop_accepted","additional_noJ_calls_are_new_science",
                "cache_effects_and_time_not_assumed_zero"))
            g["loop"]["unvisited_extra_scope"]=value.get("unvisited_extra_scope",[])
            g["files"]["loop"]=dict(bytes=identity["bytes"],sha256=identity["sha256"])
        elif schema=="current-H-complete-original576-secant-decomposition-v1" and path.name=="result.json" and g is not None:
            self.report_counts["exact_iterations"]+=1
            self.report_counts["complete_exact_iterations" if value.get("complete") else "partial_exact_iterations"]+=1
            g["result"]=fields(value,("complete","error","completed_original_blocks",
                "completed_original_rows_per_returned_trial","elapsed_seconds","declared_budget_seconds"))
            g["result"]["unpaid_scope"]=value.get("unpaid_scope",[])
            g["result"]["complete_row_ledger"]=value.get("complete_row_ledger")
            g["files"]["result"]=dict(bytes=identity["bytes"],sha256=identity["sha256"])
        elif schema=="current-H-one-observed-trial-exact-decomposition-v1" and g is not None:
            self.report_counts["trial_reports"]+=1
            self.report_counts["whole_row_trial_reports"]+=bool(value.get("full_original_rows_paid"))
            maxima=value.get("maxima",{})
            original=value.get("original_error") or value.get("actual_error")
            row=dict(label=value.get("label"),role=value.get("role"),
                alpha_exponent=value.get("alpha_exponent"),
                returned_complete_residual=value.get("returned_complete_residual"),
                original_norm=atom(value.get("original_norm")),
                original_gate_result=value.get("original_gate_result"),
                original_error=error_view(original),
                processed_original_rows=value.get("processed_original_rows"),
                full_original_rows_paid=value.get("full_original_rows_paid"),
                exact_component_identity_verified=value.get("exact_component_identity_verified"),
                original_norm_comparison_full_domain=value.get("original_norm_comparison_full_domain"),
                global_maxima=[maximum_view(maxima.get("all",{}).get(k)) for k in METRICS],
                all_family_maxima_and_dyadic_row_witnesses_identity=object_identity(maxima),
                full_dyadic_witness_values_not_exported=True,
                norm_comparisons=[norm_comparison(value.get(k)) for k in
                    ("withJ_printed_norm_readback","baseline_printed_norm_readback","trial_printed_norm_readback")],
                original_file=dict(bytes=identity["bytes"],sha256=identity["sha256"]))
            g["trials"][str(value.get("label"))]=row
        elif schema=="current-H-actual-noJ-observation-v1" and g is not None:
            role=value.get("role")
            self.report_counts["actual_original_trials" if role=="original-native-trial" else
                "actual_extra_trials" if role=="post-ten-rejection-diagnostic" else "baselines"]+=1
            self.report_counts["complete_noJ_returns" if value.get("returned_complete_residual") else "unreturned_noJ"]+=1
            entry=value.get("state_input",{});state=entry.get("states",{})
            row=dict(label=value.get("label"),role=role,alpha_exponent=value.get("alpha_exponent"),
                returned_complete_residual=value.get("returned_complete_residual"),
                original_norm=atom(value.get("original_norm")),
                original_minA=atom(value.get("original_minA")),original_minD=atom(value.get("original_minD")),
                original_gate_result=value.get("original_gate_result"),error=error_view(value.get("error")),
                elapsed_seconds=value.get("elapsed_seconds"),
                state_raw_sha256=state.get("raw_sha256"),state_shape=state.get("shape"),
                arrays_descriptor_identity=object_identity(value.get("arrays",[])),
                file=dict(bytes=identity["bytes"],sha256=identity["sha256"]))
            if role=="additional-same-state-noJ-baseline":g["baseline"]=row
            else:g["observations"][str(value.get("label"))]=row
        elif "partial" in schema or "failure" in schema:
            self.other_failures.append(dict(file=relative,identity=identity,
                fields=fields(value,("schema","native_call","nonlinear_iteration","snapshot_sequence",
                    "error","actual_error","reason","complete_decomposition","whole_rows_unpaid",
                    "original_loop_returned","original_loop_accepted")),
                full_parsed_object_identity=object_identity(value)))
        if self.label=="rules":
            selected=fields(value,("schema","phase","run_id","source_commit","status","returncode",
                "return_code","exit_code","reason","error","exception","rules_changed",
                "rule_changed","command_returncode","science_returncode","last_pull_commit",
                "last_pull_utc","new_head","current_head","initial_head"))
            if selected:self.rules.append(dict(file=relative,identity=identity,values=selected))

    def json_file(self,path):
        identity=self.identity(path);raw=path.read_bytes()
        if len(raw)!=identity["bytes"] or hashlib.sha256(raw).hexdigest()!=identity["sha256"]:
            raise ValueError("Original JSON changed while read")
        decoded=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
        try:value=json.loads(decoded)
        except Exception as error:
            self.counts["malformed_JSON_records"]+=1
            self.errors.append(dict(file=identity["file"],error=repr(error),identity=identity,
                original_text_excerpt=small_text(decoded.decode("utf-8","surrogateescape"),1200),
                remainder_not_exported=True))
            self.inventory.append(dict(**identity,scope="original malformed JSON read internally"))
            return
        self.counts["JSON_files"]+=1
        self.inventory.append(dict(**identity,decoded_bytes=len(decoded),
            decoded_sha256=hashlib.sha256(decoded).hexdigest(),scope="original JSON read and parsed internally"))
        self.remember(path,value,identity)

    def jsonl(self,path):
        identity=self.identity(path);digest=hashlib.sha256();total=0;count=0
        with path.open("rb") as stream:
            remaining=identity["bytes"]
            while remaining>0:
                raw=stream.readline(remaining)
                if not raw:break
                remaining-=len(raw);offset=total;total+=len(raw);digest.update(raw);count+=1
                try:
                    value=json.loads(raw)
                    if isinstance(value,dict):
                        wanted=("event","call","native_call","iteration","nonlinear_iteration","trial","k",
                            "step","alpha","norm","baseNorm","trialNorm","minA","minD","accepted",
                            "stage","rawCell","rawSegment","error","exception","actual_error","where",
                            "snapshot_sequence","snapshot_completed","linear_direction_returned",
                            "source_current_withJ_norm")
                        selected=fields(value,wanted)
                        item=dict(file=self.relative(path),line=count,values=selected)
                        if path.name in ("native_trials.jsonl","native_trace.jsonl"):
                            target=self.native_trial_rows if path.name=="native_trials.jsonl" else self.trace_rows
                            target.append(item)
                        elif path.name=="diagnostic-errors.jsonl":
                            self.other_failures.append(item)
                except Exception as error:
                    self.counts["malformed_JSON_records"]+=1
                    self.errors.append(dict(file=identity["file"],line=count,byte_offset=offset,
                        bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),final_LF=raw.endswith(b"\n"),
                        error=repr(error),original_text_excerpt=small_text(raw.decode("utf-8","surrogateescape"),1200),
                        remainder_not_exported=True))
        if total!=identity["bytes"] or digest.hexdigest()!=identity["sha256"]:
            raise ValueError("Original JSONL changed while read")
        self.counts["JSONL_files"]+=1;self.counts["JSONL_lines"]+=count
        self.inventory.append(dict(**identity,scope="all original JSONL bytes read internally",
            parsed_or_failed_lines=count,complete_row_payload_not_exported=True))

    def log_file(self,path):
        identity=self.identity(path);digest=hashlib.sha256();total=0;number=0
        first=[];last=deque(maxlen=3);window=0
        failure=re.compile(rb"(Traceback \(most recent call last\)|(?:Error|Exception|Failed|failed|fatal|FATAL|SyntaxError|TypeError|ValueError|RuntimeError|AssertionError|ResourcePartial)\b)")
        with path.open("rb") as stream:
            remaining=identity["bytes"]
            while remaining>0:
                raw=stream.readline(remaining)
                if not raw:break
                remaining-=len(raw);offset=total;total+=len(raw);digest.update(raw);number+=1
                hit=bool(failure.search(raw)) and not raw.lstrip().startswith((b"{",b"["))
                if b"Traceback (most recent call last)" in raw:window=10
                if hit or window:
                    selected=dict(line=number,byte_offset=offset,
                        original_line_bytes=len(raw),original_line_sha256=hashlib.sha256(raw).hexdigest(),
                        original_text_excerpt=small_text(raw.decode("utf-8","surrogateescape"),500))
                    if len(first)<6:first.append(selected)
                    last.append(selected)
                if window:window-=1
        if total!=identity["bytes"] or digest.hexdigest()!=identity["sha256"]:
            raise ValueError("Original log changed while read")
        self.counts["log_files"]+=1;self.counts["log_bytes_read"]+=total
        self.inventory.append(dict(**identity,scope="all original log bytes hashed internally; large stream not exported"))
        self.logs.append(identity)
        if first or last:
            chosen=[];seen=set()
            for row in first+list(last):
                if row["line"] not in seen:chosen.append(row);seen.add(row["line"])
            self.failure_text.append(dict(file=identity["file"],identity=identity,
                selected_original_lines=chosen,whole_stdout_or_stderr_not_exported=True))

    def walk(self):
        if not self.root.is_dir():
            self.errors.append(dict(directory=str(self.root),error="Original output directory missing"))
            return
        for directory,names,files in os.walk(self.root,followlinks=False):
            names.sort();files.sort();base=Path(directory)
            if ".git" in names:
                names.remove(".git");self.errors.append(dict(path=str(base),error="Unexpected Git tree excluded"))
            for name in list(names):
                folder=base/name
                if folder.is_symlink():
                    names.remove(name);self.errors.append(dict(path=str(folder),error="Symlink not followed"))
                elif name=="large-arrays":
                    for sub,subdirs,subfiles in os.walk(folder,followlinks=False):
                        for child in list(subdirs):
                            if (Path(sub)/child).is_symlink():
                                subdirs.remove(child);self.errors.append(dict(path=str(Path(sub)/child),error="Bulk symlink not followed"))
                        for filename in subfiles:
                            p=Path(sub)/filename
                            if p.is_symlink():
                                self.errors.append(dict(path=str(p),error="Bulk symlink not followed"));continue
                            self.counts["bulk_files_stat_only"]+=1
                            self.counts["bulk_bytes_stat_only"]+=p.stat().st_size
                    names.remove(name)
            for name in files:
                path=base/name
                if path.is_symlink():
                    self.errors.append(dict(path=str(path),error="Symlink not followed"));continue
                try:
                    if name.endswith((".json",".json.gz")):self.json_file(path)
                    elif name.endswith(".jsonl"):self.jsonl(path)
                    elif name.endswith((".log",".stderr",".stdout",".txt",".partial")) or "stderr" in name or "stdout" in name:
                        self.log_file(path)
                    elif name.endswith((".py",".mjs",".md")):
                        self.inventory.append(dict(**self.identity(path),scope="source hash only"))
                    else:
                        self.counts["bulk_files_stat_only"]+=1;self.counts["bulk_bytes_stat_only"]+=path.stat().st_size
                except Exception as error:
                    self.errors.append(dict(file=self.relative(path),error=repr(error),
                        traceback_excerpt=small_text(traceback.format_exc(),1500)))

    def finalized(self):
        # No complete inventory, source tree or large log is transported.
        groups=[]
        for name,g in sorted(self.groups.items()):
            entry={k:v for k,v in g.items() if k not in ("observations","trials")}
            labels=sorted(set(g["observations"])|set(g["trials"]))
            rows=[]
            for label in labels:
                ob=g["observations"].get(label) or {}
                exact=g["trials"].get(label) or {}
                norm=ob.get("original_norm") if ob else exact.get("original_norm")
                if ob and exact and ob.get("original_norm")!=exact.get("original_norm"):
                    norm=dict(observation=ob.get("original_norm"),exact_report=exact.get("original_norm"),
                        original_metadata_values_differ=True)
                oi=ob.get("file");ei=exact.get("original_file")
                rows.append([label,ob.get("role",exact.get("role")),
                    ob.get("alpha_exponent",exact.get("alpha_exponent")),
                    ob.get("returned_complete_residual",exact.get("returned_complete_residual")),
                    norm,ob.get("original_gate_result",exact.get("original_gate_result")),
                    ob.get("error") or exact.get("original_error"),
                    ob.get("state_raw_sha256"),
                    None if oi is None else [oi.get("bytes"),oi.get("sha256")],
                    exact.get("processed_original_rows"),exact.get("full_original_rows_paid"),
                    exact.get("exact_component_identity_verified"),
                    exact.get("global_maxima"),
                    None if ei is None else [ei.get("bytes"),ei.get("sha256")],
                    exact.get("all_family_maxima_and_dyadic_row_witnesses_identity"),
                    exact.get("norm_comparisons"),
                    [ob.get("original_minA"),ob.get("original_minD"),ob.get("elapsed_seconds")],
                    ob.get("arrays_descriptor_identity")])
            entry["trial_rows"]=rows
            groups.append(entry)
        trace_fields=("native_call","call","nonlinear_iteration","iteration","norm","minA","minD","event","error","exception")
        traces=[dict(file=v["file"],line=v["line"],values={k:x for k,x in (v["values"] or {}).items() if k in trace_fields})
                for v in self.trace_rows]
        failure_text=self.failure_text[:2]+self.failure_text[-2:] if len(self.failure_text)>4 else self.failure_text
        return dict(root=self.label,coherent_after_owned_producer_exit=self.quiescent,
            counts=self.counts,exact_scope_counts=self.report_counts,
            internally_read_metadata_file_inventory=object_identity(self.inventory),
            original_log_file_inventory=object_identity(self.logs),
            exact_metric_columns=list(METRICS),
            maximum_columns=["decimal68_original_sigma_absolute","global_equation_row","kind","node","row_in_block","coordinate"],
            trial_columns=["label","role","alpha_exponent","noJ_returned_complete_residual",
                "original_norm_word","original_gate","original_error","actual_state_raw_sha256",
                "observation_file_bytes_SHA256","processed_original_rows","full_129248_rows_paid",
                "exact_component_identity_verified","global_maxima_in_declared_metric_order",
                "exact_report_bytes_SHA256","all_family_maxima_and_dyadic_witness_identity",
                "norm_comparisons_withJ_baseline_trial","original_minA_minD_elapsed",
                "actual_residual_array_descriptor_identity"],
            norm_comparison_columns=["original_norm_word","absolute_printed_minus_exact_sigma_decimal68",
                "original_printed_norm_nonfinite","complete_comparison_object_identity"],
            norm_word_columns=["original_JSON_value","classification","float64le_hex"],
            iterations=groups,native_trace_selected_original_fields=traces,
            native_trial_selected_original_fields=self.native_trial_rows,
            other_original_failures=self.other_failures,
            rules_selected_original_fields=self.rules,
            selected_original_failure_text=failure_text,
            failure_text_scope=dict(files_with_detected_error_lines=len(self.failure_text),
                selected_files=len(failure_text),unexported_error_line_selections_identity=object_identity(self.failure_text),
                first_two_and_last_two_files_selected_if_more_than_four=True,
                large_stdout_and_full_traceback_not_exported=True),
            complete_dyadic_witnesses_full_arrays_and_large_log_streams_not_exported=True,
            no_encoded_chunks_or_semantic_reassembly_protocol=True,errors=self.errors)


def useful_status(cache):
    specs={
      "process-status.json":("schema","phase","scientific_child_returncode","wrapper_returncode",
        "elapsed_seconds","budget_exhausted","external_signal","exception","owned_group_quiescent_after_return"),
      "science/adapter-status.json":("schema","phase","success","new_coupled_finite_acceptance","exception",
        "height_path_outcome","height_path_resource_partial","height_path_endpoint_completed",
        "original_boundary_FD_passed","maximum_boundary_FD_relative_error","original_full_DN_exit_status",
        "native_live_calls","native_owner_closed"),
      "science/height-path/height-path-status.json":("schema","phase","complete_endpoint","resource_partial",
        "last_converged_s","last_converged_call","completed_bootstrap_request_count","proposed_increment"),
      "science/actual-H-response/response-check.json":("implementation_check_passed","verification_threshold",
        "maximum_relative_directional_error","second_order_truncation_contracts",
        "actual_current_H_solved_before_this_FD","native_anchor_response_sha256"),
      "science/full-DN/driver-status.json":("phase","new_coupled_finite_acceptance","physical_RMS_max",
        "physical_node_relative_residual","height_seam","exception")}
    return {name:fields(cache.get(name),wanted) for name,wanted in specs.items() if name in cache}


def bounded_fallback(summary,oversize=None):
    roots=summary.get("readback_roots",[])
    brief=[]
    for root in roots:
        iterations=root.get("iterations",[])
        last=iterations[-1] if iterations else None
        if last is not None:
            last=dict(directory=last.get("directory"),model=last.get("model"),
                loop=last.get("loop"),result=last.get("result"),files=last.get("files"),
                complete_iteration_scalar_identity=object_identity(last),
                complete_iteration_scalar_values_not_exported=True)
        brief.append(dict(root=root.get("root"),counts=root.get("counts"),
            exact_scope_counts=root.get("exact_scope_counts"),
            internally_read_metadata_file_inventory=root.get("internally_read_metadata_file_inventory"),
            last_iteration=last,full_selected_scalar_projection_identity=object_identity(root)))
    return dict(schema=INCOMPLETE_SCHEMA,run_id=summary["run_id"],source_commit=summary["source_commit"],
        reader_sha256=summary["reader_sha256"],request_sha256=summary["request_sha256"],
        recipe_sha256=summary["recipe_sha256"],complete_scalar_readback=False,
        original_scientific_status=summary.get("original_scientific_status"),
        root_scope=brief,errors=[error_view(x) for x in summary.get("errors",[])[:8]],
        complete_error_list_identity=object_identity(summary.get("errors",[])),
        over_limit_necessary_scalar_projection=oversize,
        no_partial_trial_table_claimed_complete=True,
        no_large_object_chunking_or_encoding_fallback=True,
        raw_kept_until_runner_destruction_because_readback_incomplete=True,
        new_scientific_acceptance_gate=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("directory","request","recipe","out"):
        parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--rules-directory",type=Path)
    parser.add_argument("--compute-outcome",default="unknown")
    args=parser.parse_args()
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve()
    root=args.directory.resolve();out=args.out.resolve()
    if (root==temporary or not root.is_relative_to(temporary) or out==temporary
            or not out.is_relative_to(temporary) or out.is_relative_to(root) or out.exists()):
        raise ValueError("Use fresh contained sibling readback output")
    out.mkdir(parents=True)
    summary=dict(schema=SCHEMA,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),reader_sha256=sha(__file__),
        request_sha256=sha(args.request),recipe_sha256=sha(args.recipe),
        compute_step_outcome=args.compute_outcome,complete_scalar_readback=False,
        no_new_scientific_evaluation_or_exact_arithmetic=True,
        original_native_acceptance_not_replaced=True,
        necessary_original_scalar_selection_only=True,
        full_dyadic_row_witnesses_arrays_and_large_logs_not_exported=True,
        not_an_independent_full_array_or_witness_audit=True,
        no_chunk_reassembly_or_large_encoded_return=True,readback_roots=[],errors=[])
    try:
        request=json.loads(args.request.read_bytes());recipe=json.loads(args.recipe.read_bytes())
        if request.get("schema")!=REQUEST_SCHEMA:raise ValueError("Wrong actual request schema")
        if summary["recipe_sha256"]!=request["parameter_recipe"]["sha256"]:
            raise ValueError("Actual recipe bytes changed")
        summary["actual_source_and_policy"]=dict(
            original_source_pin_count=len(request["source_sha256"]),
            source_pin_dictionary_identity=object_identity(request["source_sha256"]),
            original_inputs_identity=object_identity(request["inputs"]),
            execution=request["execution"],diagnostic_policy=request["secant_diagnostic"],
            initial_six_parameters=recipe["initial_six_parameters"],lambda_target=recipe["lambda_target"])
        first_owner=owner_observation(root);summary["owner_before"]=first_owner
        reader=Collector(root,"execution",first_owner["quiescent"]);reader.walk()
        summary["readback_roots"].append(reader.finalized());summary["errors"].extend(reader.errors)
        summary["original_scientific_status"]=useful_status(reader.cache)
        if args.rules_directory is not None:
            rules=args.rules_directory.resolve()
            if rules==temporary or not rules.is_relative_to(temporary):
                raise ValueError("Actual rules receipts must be inside this runner temporary directory")
            rr=Collector(rules,"rules",first_owner["quiescent"]);rr.walk()
            summary["readback_roots"].append(rr.finalized());summary["errors"].extend(rr.errors)
        last_owner=owner_observation(root);summary["owner_after"]=last_owner
        summary["complete_scalar_readback"]=bool(not summary["errors"] and first_owner["quiescent"] and last_owner["quiescent"])
    except Exception as error:
        summary["errors"].append(dict(error=repr(error),traceback_excerpt=small_text(traceback.format_exc(),3000)))
    # The full selected projection stays temporary even if it is too large.
    # It is never encoded/split into connector-returnable reconstruction parts.
    raw=encode(summary)
    over_limit=len(raw)>LIMIT
    if over_limit:
        summary["complete_scalar_readback"]=False
        summary["necessary_scalar_projection_exceeds_transport_limit"]=True
        raw=encode(summary)
    full_projection=dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
    (out/"necessary-scalar-projection.json").write_bytes(raw+b"\n")
    output=summary
    if over_limit:
        output=bounded_fallback(summary,full_projection);raw=encode(output)
    if len(raw)>LIMIT:
        output=dict(schema=INCOMPLETE_SCHEMA,run_id=summary["run_id"],source_commit=summary["source_commit"],
            complete_scalar_readback=False,reader_sha256=summary["reader_sha256"],
            request_sha256=summary["request_sha256"],recipe_sha256=summary["recipe_sha256"],
            necessary_projection_identity=full_projection,
            reason="Even fallback metadata was too large; no complete required scalar table exported",
            raw_kept_until_runner_destruction=True,no_scientific_acceptance_changed=True)
        raw=encode(output)
    (out/"scalar-summary.json").write_bytes(raw+b"\n")
    print("BEGIN_REQUEST172_CURRENT_H_SECANT_SCALAR_SUMMARY",flush=True)
    print(raw.decode("ascii"),flush=True)
    print("END_REQUEST172_CURRENT_H_SECANT_SCALAR_SUMMARY",flush=True)
    print(encode(dict(event="request172-necessary-scalar-summary-identity",bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest(),hash_scope="single compact ASCII JSON excluding LF",
        complete_scalar_readback=output["complete_scalar_readback"],
        full_dyadic_witnesses_and_large_stdout_not_exported=True,
        no_split_or_encoded_reconstruction_protocol=True)).decode(),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a",encoding="utf-8") as stream:
            stream.write("scalar_summary="+raw.decode("ascii")+"\n")
            stream.write("scalar_summary_bytes="+str(len(raw))+"\n")
            stream.write("scalar_summary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
    if output["complete_scalar_readback"]:
        marker=dict(schema=MARKER_SCHEMA,run_id=summary["run_id"],source_commit=summary["source_commit"],
            request_sha256=summary["request_sha256"],recipe_sha256=summary["recipe_sha256"],
            reader_sha256=summary["reader_sha256"],actual_execution_directory=str(root),
            scalar_summary=dict(bytes=len(raw)+1,sha256=sha(out/"scalar-summary.json")),
            internally_read_scalar_projection=full_projection,
            owned_group_quiescent=True,all_selected_metadata_and_failure_streams_read=True,
            selected_small_summary_export_complete=True,
            full_dyadic_witnesses_large_logs_and_arrays_not_exported=True,
            raw_mathematical_payload_not_independently_audited=True)
        (out/"readback-complete.json").write_bytes(encode(marker)+b"\n")
    return 0 if output["complete_scalar_readback"] else 2


if __name__=="__main__":
    raise SystemExit(main())
