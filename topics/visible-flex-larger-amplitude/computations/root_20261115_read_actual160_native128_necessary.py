#!/usr/bin/env python3
"""Request182: necessary original160 owner and four-component metadata.

One official completed job-log stream. No old raw log is saved, no scientific
library/source is imported, and no residual/J/norm/domain calculation occurs.
Use original direct scientific projections first. Old typed metadata only
supplements missing fields; no full component tree is reconstructed. Original
diagnostic byte streams are hashed internally. Output is ONE <=90000-byte
necessary summary, never new fragments.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import sys
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="actual160-original-native128-necessary-log-readback-v1"
REQUEST_SCHEMA="actual160-original-compute-log-necessary-readback-request-v1"
RUN=43729874541
JOB=132859748674
SOURCE_COMMIT="b34692d09c8d5ecdd7b859e43489da4413f1468e"
COMPONENTS=("stages","boundary","endpoint","audit")
COMPONENT_SCHEMA="native-persistent128-qualified-JSON-and-statistics-contracted-trace-components-launch-v2"
RUNTIME_SHA="024a3c67ada93c908d86c68c4ba0326270d81d314a9c154439f5fc42266b8d2d"
COMPONENT_SHA="5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf"
OWNER_SHA="767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322"
MAX_LINE_BYTES=16777216
MAX_UNIQUE_MATCHES=1000000
MAX_SUMMARY_BYTES=90000
TIMESTAMP=re.compile(rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ")
ERROR_WORD=re.compile(rb"(?i)(traceback|(?:^|[ :])(?:error|exception|fatal|runtimeerror|valueerror|assertionerror|systemerror|memoryerror|typeerror|syntaxerror|keyerror|timeout|timeouterror)(?:[: (]|$)|no space left|killed|terminated|signal [0-9]+|budget.exhaust|segmentation fault)")
OWNER_EVENTS={
    "persistent128_initial","persistent128_need_direction",
    "persistent128_direction_lifted","persistent128_trial",
    "persistent128_iteration_closed","persistent128_owner_final",
    "persistent128_independent_fresh_replay","persistent128_matched_trace",
    "persistent128_final_stage_column",
}
FINAL_EVENTS={
    "persistent128_launcher_final","persistent128_final",
    "global_final128_child_exit","global_final128_partial",
    "persistent128_bridge_returned","native_persistent128_controlled_worker_stop",
    "native_persistent128_fresh_direction_for_trace",
    "persistent128_source_procedure_start","global_final128_start",
    "persistent128_summary_transport_error","persistent128_final_transport_error",
}
UNFINISHED_STAGE_COLUMNS=(
    "stage","input_node","output_node","requested","complete","completed",
    "atomic_steps_total","atomic_steps_completed","unfinished_step_suffix",
    "queries_completed","queries_requested","unfinished_query_suffix",
    "atomic_advances_completed","active_phase","active_query",
    "active_query_advance_completed","active_query_advance_count","error",
)
MISSING=object()

class LiteralNumber(str):
    """An original JSON number lexeme, never a new scientific numeric value."""
    pass


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parsed(raw):
    return json.loads(raw.decode("utf-8"),parse_int=LiteralNumber,parse_float=LiteralNumber,
        object_pairs_hook=unique_pairs,
        parse_constant=lambda x: (_ for _ in ()).throw(ValueError("Non-JSON token: "+x)))


def encoded(value, ascii=True):
    """Original number tokens survive; ordinary metadata integers remain ints."""
    if isinstance(value,LiteralNumber):return str(value)
    if value is None:return "null"
    if value is True:return "true"
    if value is False:return "false"
    if isinstance(value,str):return json.dumps(value,ensure_ascii=ascii)
    if isinstance(value,(int,float)):
        return json.dumps(value,allow_nan=False,separators=(",",":"))
    if isinstance(value,list):return "["+",".join(encoded(v,ascii) for v in value)+"]"
    if isinstance(value,dict):
        require(all(isinstance(k,str) for k in value),"String JSON object keys")
        return "{"+",".join(json.dumps(k,ensure_ascii=ascii)+":"+encoded(value[k],ascii)
            for k in sorted(value))+"}"
    raise TypeError("Unsupported literal JSON value "+type(value).__name__)


def unique_pairs(pairs):
    answer={}
    for key,value in pairs:
        require(key not in answer,"No duplicate original JSON keys")
        answer[key]=value
    return answer


def original_canonical(value):
    return encoded(value,False).encode("utf-8")


def original_receipt(value):
    raw=original_canonical(value)
    return dict(canonical_bytes=len(raw),canonical_sha256=sha(raw),
        canonical_UTF8_without_final_LF=True)


def canonical(value):
    return (encoded(value)+"\n").encode("ascii")


def integer(value,label):
    text=str(value)
    require(re.fullmatch(r"-?(?:0|[1-9][0-9]*)",text) is not None,
        "Original integer metadata required: "+label)
    return int(text)


def emit(value):
    raw=canonical(value)
    require(len(raw)<=90000,"One bounded original-metadata object; no segmented fallback")
    sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()


def file_receipt(path):
    raw=Path(path).read_bytes()
    return dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))


def write(path,value):
    raw=canonical(value);temporary=path.with_suffix(path.suffix+".writing")
    temporary.write_bytes(raw);temporary.replace(path)
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


class ResourceStop(RuntimeError):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None


def api_json(path,token):
    url="https://api.github.com/repos/"+REPOSITORY+path
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"actual160-original-log-readback","Accept-Encoding":"identity"}
    if token:headers["Authorization"]="Bearer "+token
    request=urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(request,timeout=45) as response:
        raw=response.read(2097153)
        require(len(raw)<=2097152,"Bounded official metadata response")
        require(response.status==200,"Official metadata returned200")
        value=json.loads(raw)
    return value,dict(endpoint=path,bytes=len(raw),sha256=sha(raw))


def open_log(token):
    """Only the official API receives a token; the redirect request never does."""
    url="https://api.github.com/repos/"+REPOSITORY+"/actions/jobs/"+str(JOB)+"/logs"
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"actual160-original-log-readback","Accept-Encoding":"identity"}
    if token:headers["Authorization"]="Bearer "+token
    request=urllib.request.Request(url,headers=headers)
    opener=urllib.request.build_opener(NoRedirect())
    try:
        response=opener.open(request,timeout=60)
    except urllib.error.HTTPError as error:
        if error.code not in (301,302,303,307,308):raise
        location=error.headers.get("Location")
        require(isinstance(location,str),"Official job log redirect has a location")
        target=urllib.parse.urlparse(location)
        require(target.scheme=="https" and target.hostname and not target.username,
            "Only the HTTPS location returned by the official job log API is used")
        # Do not put the signed URL or original bearer token in any output.
        redirected=urllib.request.Request(location,headers={
            "User-Agent":"actual160-original-log-readback","Accept-Encoding":"identity"})
        response=urllib.request.urlopen(redirected,timeout=60)
        return response,dict(official_job_logs_endpoint=url,official_redirect_status=error.code,
            bearer_token_not_forwarded_to_redirect=True,signed_URL_not_logged=True,
            downloaded_from_official_redirect=True)
    return response,dict(official_job_logs_endpoint=url,official_redirect_status=None,
        bearer_token_not_forwarded_to_redirect=True,signed_URL_not_logged=True,
        downloaded_from_official_redirect=False)


ORIGINAL_SOURCES = [
    {
        "file": "geometry_20261115_native_operator_qualified_v2_final128_same_job.py",
        "bytes": 41364,
        "sha256": "024a3c67ada93c908d86c68c4ba0326270d81d314a9c154439f5fc42266b8d2d"
    },
    {
        "file": "geometry_20261115_native_persistent128.py",
        "bytes": 43371,
        "sha256": "767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322"
    },
    {
        "file": "geometry_20261115_native_persistent128_probe.py",
        "bytes": 17879,
        "sha256": "2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107"
    },
    {
        "file": "geometry_20261115_native128_qualified_json_components_v2.py",
        "bytes": 17484,
        "sha256": "5e68f581d75f3a9fe61acadd016f8c7b6f3bcec245fb39b342a3fecdd0b267bf"
    },
    {
        "file": "geometry_20261115_native_operator_final128.py",
        "bytes": 21548,
        "sha256": "a2ee773ccc553f8e77567efc1e4f43f7f6aae3ebea6d06833e1f4a4554306fef"
    },
    {
        "file": "geometry_20261115_native_persistent128.cpp",
        "bytes": 22364,
        "sha256": "7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd"
    },
    {
        "file": "geometry_20261115_native_trace122_probe.py",
        "bytes": 26740,
        "sha256": "05ad668da4bec72cedb0fa2f14d4c59a7ab99a280c47b137c94a5fafcf99105f"
    },
    {
        "file": "public-native-operator-qualified-v2-final128-request.json",
        "bytes": 37592,
        "sha256": "cfa6fe343d227a98a3a755263ea7302ad7f3437f71adc82effd5a639d88ee697"
    }
]

class NecessaryErrors:
    """Select diagnostic matching lines; a match is not an error classification."""
    def __init__(self):
        self.counts={};self.matching=0;self.oversized=0
        self.first=[];self.last=[];self.selected={}
        self.all_metadata=hashlib.sha256()
    def add(self,raw,origin,force=False):
        if not force and not ERROR_WORD.search(raw):return
        self.matching+=1;key=sha(raw)
        self.all_metadata.update(original_canonical(dict(bytes=len(raw),sha256=key,
            original_location=origin))+b"\n")
        if key in self.counts:
            self.counts[key]+=1
            return
        if len(self.counts)>=MAX_UNIQUE_MATCHES:
            raise ResourceStop("explicit-unique-matching-line-identity-memory-budget")
        self.counts[key]=1
        if len(raw)>12000:
            self.oversized+=1
            item=dict(original_text_bytes=len(raw),original_text_sha256=key,
                selected_text_returned=False,reason="indivisible-original-matching-line-over12000bytes",
                original_location=origin)
        else:
            item=dict(original_text_bytes=len(raw),original_text_sha256=key,
                text=raw.decode("utf-8","surrogateescape"),
                selected_text_returned=True,original_location=origin)
        if len(self.first)<6:
            self.first.append(key);self.selected[key]=item
        else:
            self.last.append(key);self.selected[key]=item
            if len(self.last)>6:
                removed=self.last.pop(0)
                if removed not in self.first:self.selected.pop(removed,None)
    def record(self):
        keys=list(dict.fromkeys(self.first+self.last))
        records=[dict(self.selected[key],occurrences=self.counts[key]) for key in keys]
        # Necessary original lines have a shared 16000-byte text allowance.
        # Larger indivisible lines are explicitly identity-only, never cut up.
        used=0
        for item in records:
            if item.get("selected_text_returned"):
                size=item["original_text_bytes"]
                if used+size>16000:
                    item.pop("text",None);item["selected_text_returned"]=False
                    item["reason"]="necessary-matching-text-shared16000byte-allowance"
                else:used+=size
        return dict(original_matching_diagnostic_line_occurrences=self.matching,
            unique_matching_diagnostic_lines=len(self.counts),
            matching_line_metadata_sha256=self.all_metadata.hexdigest(),
            selection="first6 and last6 unique actual matching lines; whole lines within shared16000bytes",
            all_matching_lines_returned=len(keys)==len(self.counts) and
                all(item.get("selected_text_returned") for item in records),
            omitted_unique_line_count=len(self.counts)-len(keys),
            oversized_indivisible_matching_line_count=self.oversized,
            matches_are_not_error_classification=True,
            false_budget_exhausted_flags_can_also_match=True,
            necessary_original_matching_lines=records)

class OriginalTree:
    """Optional old typed-path selector; never reconstruct the full large tree.

    The original direct scientific projection is authoritative.  Old tree
    members only add genuinely missing metadata, especially audit advance
    counters, or serve as a stated fallback when no direct return exists.
    This selector's missing or unverified scope is not a new science gate.
    """
    def __init__(self,label):
        self.label=label;self.count=0;self.meta=hashlib.sha256()
        self.part_bytes=0;self.duplicate_parts=0;self.complete=False
        self.final_receipt=None;self.first_location=None;self.last_location=None
        self.header={};self.report={};self.stage_rows={};self.strings={}
        self.issues=[];self.issue_count=0
        self.selected_bytes=0;self.selection_incomplete=False
    def issue(self,message,index=None):
        self.issue_count+=1
        if len(self.issues)<8:self.issues.append(dict(message=str(message),index=index))
    def needed(self,path):
        if path==["scientific_report"]:return True
        if len(path)==1 and path[0] in (
            "schema","component","source_sha256","run","scientific_complete","procedure_complete",
            "summary_complete","transport_complete","resource_partial","scientific_started",
            "actual_error","traceback","budget"):
            return True
        if len(path)>=2 and path[0]=="scientific_report":
            if path[1]=="column_records":return False
            if path[1]=="stages":
                return len(path)==3 or len(path)==4 and path[3] in UNFINISHED_STAGE_COLUMNS
            return True
        return False
    def remember(self,path,value):
        # Bound optional selected metadata only.  No original large array is
        # retained, and reaching this bound merely records an unpaid supplement.
        raw=canonical(value)
        if self.selected_bytes+len(raw)>2097152:
            self.selection_incomplete=True;return
        self.selected_bytes+=len(raw)
        if path==["scientific_report"]:
            if isinstance(value,dict):
                self.report.update(ordinary({k:v for k,v in value.items()
                    if k not in ("stages","column_records")}))
            else:self.issue("Original scientific report is not an object")
            return
        if len(path)==1:
            self.header[path[0]]=ordinary(value);return
        if path[0]!="scientific_report":return
        if path[1]=="stages":
            index=integer(path[2],"original stage-list index")
            require(0<=index<576,"Original complete576 stage index")
            if len(path)==3 and isinstance(value,dict):
                self.stage_rows[index]={key:actual_error(value.get(key)) if key=="error"
                    else value[key] for key in UNFINISHED_STAGE_COLUMNS if key in value}
            elif len(path)==4:
                row=self.stage_rows.setdefault(index,{})
                row[path[3]]=actual_error(value) if path[3]=="error" else value
        elif len(path)==2:
            self.report[path[1]]=ordinary(value)
        else:
            key="original_nested_metadata_by_typed_path"
            self.report.setdefault(key,[]).append(dict(path=path[1:],value=ordinary(value)))
    def add(self,row,location):
        entry={k:v for k,v in row.items()
            if k not in ("event","lifecycle_schema","part_canonical_bytes","part_canonical_sha256")}
        raw=original_canonical(entry);index=integer(row["index"],"tree part index")
        require(len(raw)==integer(row["part_canonical_bytes"],"tree metadata bytes") and
            sha(raw)==row["part_canonical_sha256"],"Original optional typed metadata part identity")
        if index<self.count:
            self.duplicate_parts+=1
            return
        if index!=self.count:
            self.issue("Nonconsecutive old optional typed-part index",index)
            self.selection_incomplete=True
        if self.first_location is None:self.first_location=location
        self.last_location=location
        path=row["path"];kind=row["kind"]
        require(isinstance(path,list),"Original typed metadata path")
        self.meta.update(original_canonical(dict(index=index,path=path,kind=kind,
            bytes=len(raw),sha256=sha(raw)))+b"\n")
        self.count=index+1;self.part_bytes+=len(raw)
        if not self.needed(path):return
        if kind=="value":
            self.remember(path,row["value"])
        elif kind=="string":
            # Strings may be gigantic diagnostic text.  Record their original
            # identity; retain no more than6000 actual characters as one string.
            size=integer(row["utf8_bytes"],"original selected string bytes")
            self.strings[tuple(path)]=dict(position=0,characters=integer(row["character_count"],
                "original string characters"),bytes=size,sha256=row["utf8_sha256"],
                hash=hashlib.sha256(),actual_bytes=0,parts=[] if size<=6000 else None)
        elif kind=="string-part":
            state=self.strings.get(tuple(path))
            require(state is not None,"Original selected string header")
            start=integer(row["character_start"],"string range start")
            stop=integer(row["character_stop"],"string range stop")
            value=row["value"];raw_value=value.encode("utf-8")
            require(start==state["position"] and stop-start==len(value),
                "Original selected string character coverage")
            state["hash"].update(raw_value);state["actual_bytes"]+=len(raw_value)
            state["position"]=stop
            if state["parts"] is not None:state["parts"].append(value)
        # Object and array skeletons are deliberately not materialized.
    def finish(self,row,location):
        marker_ok=(row.get("label")==self.label and row.get("complete") is True and
            integer(row["part_count"],"tree part count")==self.count and
            row["part_metadata_jsonl_sha256"]==self.meta.hexdigest())
        if not marker_ok:self.issue("Old optional complete-tree metadata identity differs")
        for path,state in self.strings.items():
            good=(state["position"]==state["characters"] and state["actual_bytes"]==state["bytes"]
                and state["hash"].hexdigest()==state["sha256"])
            if not good:
                self.issue("Old selected diagnostic string incomplete")
                self.selection_incomplete=True;continue
            value=("".join(state["parts"]) if state["parts"] is not None else dict(
                original_bytes=state["bytes"],original_sha256=state["sha256"],
                original_whole_text_not_returned=True,reason="optional-original-tree-string-over6000bytes"))
            self.remember(list(path),value)
        source_ok=(self.header.get("schema")==COMPONENT_SCHEMA and
            self.header.get("source_sha256")==COMPONENT_SHA and
            self.header.get("component")==self.label.removesuffix("-complete-component-summary"))
        run=self.header.get("run") or {}
        if not (source_ok and str(run.get("GITHUB_RUN_ID"))==str(RUN)
                and run.get("GITHUB_SHA")==SOURCE_COMMIT):
            self.issue("Optional old tree source/run header not completely verified")
        self.complete=bool(marker_ok and self.issue_count==0)
        self.final_receipt=dict(label=self.label,original_file=row.get("original_file"),
            original_canonical_bytes=row.get("canonical_bytes"),
            original_canonical_sha256=row.get("canonical_sha256"),
            full_semantic_object_reconstructed=False,full_semantic_object_SHA_recomputed=False,
            full_canonical_identity_is_original_producer_receipt=True,
            emitted_part_bytes_and_metadata_stream_verified=self.complete,
            optional_selected_metadata_complete=not self.selection_incomplete and self.complete,
            selected_metadata_storage_bytes=self.selected_bytes,
            part_count=self.count,part_metadata_jsonl_sha256=self.meta.hexdigest(),
            repeated_part_indexes_skipped=self.duplicate_parts,
            repeated_payload_equality_not_claimed=self.duplicate_parts!=0,
            complete_marker_location=location,first_part_location=self.first_location,
            last_part_location=self.last_location,issues=self.issues,
            issue_count=self.issue_count,optional_scope_not_new_acceptance_gate=True)
        return self.header
    def missing_stage_fields(self,projection):
        columns=projection.get("unfinished_stage_columns") if isinstance(projection,dict) else None
        rows=projection.get("unfinished_stages") if isinstance(projection,dict) else None
        direct=(isinstance(columns,list) and isinstance(rows,list) and "stage" in columns)
        available=({str(row[columns.index("stage")]) for row in rows} if direct else None)
        tables=[];by_keys={}
        for i,row in sorted(self.stage_rows.items()):
            if direct:
                if str(row.get("stage")) not in available:continue
                extra={k:v for k,v in row.items() if k not in columns}
            else:
                if row.get("complete") is True or row.get("completed") is True:continue
                extra=dict(row);extra.pop("stage",None)
            if not extra:continue
            keys=tuple(sorted(extra))
            if keys not in by_keys:
                by_keys[keys]=len(tables)
                tables.append(dict(columns=["original_stage_list_index","original_stage"]+list(keys),
                    all_original_rows=[]))
            tables[by_keys[keys]]["all_original_rows"].append(
                [i,row.get("stage")]+[extra[key] for key in keys])
        return dict(only_missing_direct_projection_fields=direct,
            direct_unfinished_stage_projection_unavailable=not direct,
            original_missing_column_tables=tables,
            original_key_presence_preserved_by_separate_tables=True,
            optional_producer_identity_verified=self.complete,
            optional_selection_complete=not self.selection_incomplete and self.complete,
            complete_old_array_not_reconstructed=True)

class OriginalText:
    """Stream old 12000-byte diagnostic frames, never save the original log."""
    def __init__(self,label,errors):
        self.label=label;self.errors=errors;self.count=0;self.position=0
        self.hash=hashlib.sha256();self.meta=hashlib.sha256()
        self.pending=b"";self.lines=0;self.complete=False;self.original=None
        self.parts={};self.duplicate_parts=0;self.final_receipt=None
    def add(self,row,location):
        index=integer(row["index"],"original text part index")
        original_text=json.loads(row["text_json_ascii"])
        require(isinstance(original_text,str),"Original UTF8-surrogateescape text")
        raw=original_text.encode("utf-8","surrogateescape")
        require(len(raw)==integer(row["original_part_bytes"],"original text part bytes")
            and sha(raw)==row["original_part_sha256"],"Original diagnostic part bytes")
        if index<self.count:
            require(self.parts.get(index)==sha(raw),"Repeated diagnostic part bytes identical")
            self.duplicate_parts+=1;return
        require(not self.complete and index==self.count,"Original diagnostic part order")
        require(integer(row["byte_start"],"text start")==self.position
            and integer(row["byte_stop"],"text stop")==self.position+len(raw),
            "Complete original diagnostic byte coverage")
        original=row["original_file"]
        if self.original is None:self.original=original
        require(original==self.original,"One original diagnostic file identity")
        self.hash.update(raw);self.position+=len(raw)
        metadata={k:v for k,v in row.items()
            if k not in ("event","lifecycle_schema","text_json_ascii")}
        self.meta.update(original_canonical(metadata)+b"\n")
        self.parts[index]=sha(raw);self.count+=1
        self.pending+=raw
        require(len(self.pending)<=MAX_LINE_BYTES,"Bounded diagnostic original line")
        while b"\n" in self.pending:
            line,self.pending=self.pending.split(b"\n",1)
            self.errors.add(line+b"\n",dict(label=self.label,original_file=self.original,
                original_text_line_index=self.lines,outer_log_location=location))
            self.lines+=1
    def finish(self,row,location):
        require(row.get("complete") is True and row.get("present") is True,
            "Actual original diagnostic complete marker")
        require(integer(row["part_count"],"text part count")==self.count
            and integer(row["concatenated_original_bytes"],"text complete bytes")==self.position
            and row["part_metadata_jsonl_sha256"]==self.meta.hexdigest(),
            "All original diagnostic part metadata accounted")
        if self.original is None:self.original=row["original_file"]
        require(self.original==row["original_file"]
            and self.position==integer(self.original["bytes"],"original diagnostic bytes")
            and self.hash.hexdigest()==self.original["sha256"],
            "Complete original diagnostic bytes/hash")
        if self.pending:
            self.errors.add(self.pending,dict(label=self.label,original_file=self.original,
                original_text_line_index=self.lines,outer_log_location=location))
            self.lines+=1;self.pending=b""
        self.complete=True
        self.final_receipt=dict(label=self.label,original_file=self.original,
            parts=self.count,part_metadata_jsonl_sha256=self.meta.hexdigest(),
            complete_original_bytes_verified=True,whole_original_text_returned=False,
            actual_text_lines=self.lines,identical_duplicate_parts=self.duplicate_parts,
            selected_original_error_lines_in_separate_summary=True,
            complete_marker_location=location)

def actual_error(value):
    """Return original short error text; oversized text gets a stated selection."""
    if value is None:return None
    if not isinstance(value,str):return value
    raw=value.encode("utf-8","surrogateescape")
    if len(raw)<=6000:return value
    lines=raw.splitlines(keepends=True)
    selected=[line for line in lines if ERROR_WORD.search(line)]
    candidates=(selected[:4]+selected[-4:]) if selected else (lines[:3]+lines[-3:])
    unique=[]
    for line in candidates:
        if line not in unique:unique.append(line)
    kept=[];size=0
    for line in unique:
        if size+len(line)>6000:continue
        kept.append(line.decode("utf-8","surrogateescape"));size+=len(line)
    return dict(original_bytes=len(raw),original_sha256=sha(raw),
        whole_original_text_returned=False,selected_actual_lines=kept,
        original_matching_line_count=len(selected),
        selection="first4 and last4 matching original lines; fallback first3 and last3",
        no_error_cause_inferred=True)

def ordinary(value):
    """Drop only declared bulky source/array payload, preserve scalar lexemes."""
    if isinstance(value,dict):
        answer={}
        for key,item in value.items():
            if key in ("stages","column_records","owner_records","QR_directions",
                       "final_stage_columns","complete_packet_structure","output_arrays",
                       "files","sources","source_receipts","source_sha256s",
                       "literal_field_records","all_angular_rows","arrays"):
                answer[key+"_identity_only"]=original_receipt(item)
            elif key in ("traceback","actual_traceback","actual_error","error","evaluation_error"):
                answer[key]=actual_error(item)
            elif key=="failed_stages" and isinstance(item,list):
                answer[key]=failed_stage_projection(item)
            elif key in ("stdout","stderr","stdout_tail","stderr_tail") and isinstance(item,str):
                answer[key]=actual_error(item)
            elif key in ("command","scientific_command","actual_executed_command",
                         "original_requested_compile_command","inputs","original_owner_binding",
                         "qualification_source_factory","compiler_readout_source_binding"):
                answer[key+"_identity_only"]=original_receipt(item)
            else:answer[key]=ordinary(item)
        return answer
    if isinstance(value,list):return [ordinary(item) for item in value]
    return value

def failed_stage_projection(rows):
    """Share equal original error metadata while retaining every stage address."""
    if not all(isinstance(row,dict) and "stage" in row for row in rows):
        return ordinary(rows)
    groups=[];lookup={}
    for index,row in enumerate(rows):
        fields={key:value for key,value in row.items() if key!="stage"}
        identity=original_canonical(fields)
        if identity not in lookup:
            lookup[identity]=len(groups)
            groups.append(dict(original_common_fields=ordinary(fields),
                all_original_addresses=[]))
        groups[lookup[identity]]["all_original_addresses"].append([index,row["stage"]])
    return dict(original_row_count=len(rows),original_identity=original_receipt(rows),
        address_columns=["original_failed_stage_list_index","stage"],groups=groups,
        all_original_addresses_retained=True,
        grouping_only_exact_equal_original_error_fields=True)

def direct_scientific_projection(report):
    """Keep the original projection; share only exactly equal suffix metadata."""
    if not isinstance(report,dict):return ordinary(report)
    columns=report.get("unfinished_stage_columns")
    rows=report.get("unfinished_stages")
    if not (isinstance(columns,list) and isinstance(rows,list) and "stage" in columns):
        return ordinary(report)
    answer=ordinary({key:value for key,value in report.items()
        if key not in ("unfinished_stage_columns","unfinished_stages")})
    addresses=[i for i,key in enumerate(columns) if key in ("stage","input_node","output_node")]
    fields=[i for i in range(len(columns)) if i not in addresses]
    if not all(isinstance(row,list) and len(row)==len(columns) for row in rows):
        answer["original_unfinished_stage_columns"]=columns
        answer["original_unfinished_stages"]=ordinary(rows)
        answer["original_unfinished_stage_table_shape_not_grouped"]=True
        return answer
    groups=[];index={}
    for row_index,row in enumerate(rows):
        original_values=[row[i] for i in fields]
        key=original_canonical(original_values)
        if key not in index:
            index[key]=len(groups)
            groups.append(dict(original_common_values=[
                actual_error(row[i]) if columns[i]=="error" else ordinary(row[i])
                for i in fields],all_original_addresses=[]))
        groups[index[key]]["all_original_addresses"].append(
            [row_index]+[row[i] for i in addresses])
    answer["complete_original_unfinished_stage_table"]=dict(
        original_columns=columns,original_row_count=len(rows),
        original_table_identity=original_receipt(rows),
        common_columns=[columns[i] for i in fields],
        address_columns=["original_direct_projection_row_index"]+[columns[i] for i in addresses],
        groups=groups,all_original_rows_retained=True,
        sharing_only_exact_equal_original_nonaddress_fields=True,
        every_original_address_explicit=True,
        address_ranges_not_inferred=True)
    return answer

class Scan:
    def __init__(self,deadline,maxbytes):
        self.deadline=deadline;self.maxbytes=maxbytes
        self.log_hash=hashlib.sha256();self.total_bytes=0;self.lines=0;self.fully_streamed=False
        self.bom_lines=0;self.events=Counter();self.wrapper_events=Counter()
        self.trees={};self.tree_results={};self.texts={};self.log_absent=[]
        self.owner_rows=[];self.owner_keys={};self.owner_duplicates=Counter()
        self.component_start={};self.component_return={};self.all_components=None
        self.component_compact={};self.final_events={};self.auxiliary=[]
        self.errors=NecessaryErrors();self.protocol_errors=[];self.protocol_error_count=0
        self.optional_old_protocol_issues=[];self.optional_old_issue_count=0
        self.original_line_records=Counter();self.original_line_identities={}
        self.parse_error_events=[];self.native_markers=0;self.unknown_json=0
        self.current_location=None
    def check(self):
        if time.monotonic()>=self.deadline:raise ResourceStop("explicit-original160-log-scan-wall-budget")
        if self.total_bytes>self.maxbytes:raise ResourceStop("explicit-original160-log-byte-cap")
    def fail(self,error,location,event=None):
        self.protocol_error_count+=1
        row=dict(type=type(error).__name__,message=str(error),
            original_location=location,event=event)
        if len(self.protocol_errors)<20:self.protocol_errors.append(row)
    def optional_issue(self,error,location,event=None):
        self.optional_old_issue_count+=1
        if len(self.optional_old_protocol_issues)<20:
            self.optional_old_protocol_issues.append(dict(type=type(error).__name__,
                message=str(error),original_location=location,event=event,
                direct_scientific_projection_is_not_discarded=True))
    def owner(self,row,location,container):
        event=row.get("event")
        if event not in OWNER_EVENTS:return
        if event=="persistent128_trial":
            key=(event,str(row["iteration"]),str(row["trial"]))
        elif event in ("persistent128_need_direction","persistent128_direction_lifted",
                       "persistent128_iteration_closed","persistent128_matched_trace"):
            key=(event,str(row["iteration"]))
        elif event=="persistent128_final_stage_column":
            key=(event,str(row.get("column")))
        else:key=(event,)
        body=original_canonical(row);identity=sha(body)
        if key in self.owner_keys:
            previous=self.owner_keys[key]
            require(previous["canonical_sha256"]==identity,
                "Repeated actual owner event must preserve all original parsed fields")
            self.owner_duplicates[event]+=1;return
        rec=dict(canonical_bytes=len(body),canonical_sha256=identity,
            original_location=location,original_container=container)
        self.owner_keys[key]=rec
        self.owner_rows.append(dict(original=row,identity=rec))
    def event(self,value,location):
        if not isinstance(value,dict):return
        outer=value.get("event")
        if (value.get("marker")=="NATIVE_PERSISTENT128"
                and isinstance(value.get("record"),dict)):
            self.wrapper_events[str(outer)]+=1
            value=value["record"]
        event=value.get("event")
        if not isinstance(event,str):return
        self.events[event]+=1
        if event=="persistent128_raw_owner_record":
            self.owner(value["record"],location,event)
            return
        if event in OWNER_EVENTS:
            self.owner(value.get("record",value),location,event);return
        if event=="qualified_same_job_scalar_tree_part":
            label=value["label"]
            if label not in {name+"-complete-component-summary" for name in COMPONENTS}:return
            tree=self.trees.get(label)
            if tree is None:
                tree=OriginalTree(label);self.trees[label]=tree
            try:tree.add(value,location)
            except ResourceStop:raise
            except Exception as error:
                tree.issue(str(error));tree.selection_incomplete=True
                self.optional_issue(error,location,event)
            return
        if event=="qualified_same_job_scalar_tree_complete":
            rec=value["result"];label=rec["label"]
            if label not in {name+"-complete-component-summary" for name in COMPONENTS}:return
            tree=self.trees.get(label)
            if tree is None:
                tree=OriginalTree(label);self.trees[label]=tree
            try:
                if tree.final_receipt is None:tree.finish(rec,location)
                self.tree_results[label.removesuffix("-complete-component-summary")]=tree
            except ResourceStop:raise
            except Exception as error:
                tree.issue(str(error));tree.selection_incomplete=True
                self.optional_issue(error,location,event)
            return
        if event=="qualified_same_job_original_log_part":
            label=value["label"]
            state=self.texts.get(label)
            if state is None:
                state=OriginalText(label,self.errors);self.texts[label]=state
            try:state.add(value,location)
            except ResourceStop:raise
            except Exception as error:self.optional_issue(error,location,event)
            return
        if event=="qualified_same_job_original_log_complete":
            label=value["label"];rec=value["result"]
            state=self.texts.get(label)
            if state is None:
                state=OriginalText(label,self.errors);state.original=rec.get("original_file")
                self.texts[label]=state
            try:
                if not state.complete:state.finish(rec,location)
            except ResourceStop:raise
            except Exception as error:self.optional_issue(error,location,event)
            return
        if event in ("qualified_same_job_log_absent","qualified_same_job_scalar_file_absent"):
            self.log_absent.append(dict(label=value.get("label"),original=value.get("result"),
                original_location=location));return
        if event=="qualified_same_job_scalar_parse_error":
            self.parse_error_events.append(dict(label=value.get("label"),
                original=ordinary(value.get("result")),original_location=location));return
        if event=="qualified_component_original_log_line":
            text=value["text_including_original_line_ending"]
            raw=text.encode("utf-8")
            require(len(raw)==integer(value["original_line_bytes"],"original diagnostic line bytes")
                and sha(raw)==value["original_line_sha256"],"Old direct original-log line identity")
            source=value["original_file"]
            key=(str(value.get("label")),source["sha256"])
            self.original_line_records[key]+=1
            self.original_line_identities[key]=source
            self.errors.add(raw,dict(label=value.get("label"),
                original_file=source,original_line_index=value.get("line_index"),
                outer_log_location=location));return
        if event=="precleanup_component_start":
            component=value["component"];require(component in COMPONENTS,"Original component name")
            self.component_start[component]=dict(original=ordinary(value),location=location);return
        if event=="precleanup_component_return":
            component=value["component"];require(component in COMPONENTS,"Original component name")
            rec=value["actual_record"]
            if component in self.component_return:
                require(original_canonical(self.component_return[component]["original"])==original_canonical(rec),
                    "Repeated original component return identity")
            self.component_return[component]=dict(original=rec,location=location,
                identity=original_receipt(rec));return
        if event=="precleanup_all_components_return":
            rec=value["actual_record"]
            require(rec.get("source_sha256")==RUNTIME_SHA
                and rec.get("component_launcher_sha256")==COMPONENT_SHA
                and rec.get("frozen_owner_source_sha256")==OWNER_SHA,
                "The actual precleanup owner/component source identities")
            if self.all_components is not None:
                require(original_canonical(self.all_components["original"])==original_canonical(rec),
                    "Repeated original all-component return identity")
            self.all_components=dict(original=rec,location=location,identity=original_receipt(rec));return
        if event=="contracted_trace_final_component":
            rec=value.get("summary",{});name=rec.get("component")
            if name in COMPONENTS:self.component_compact[name]=dict(
                original=rec,identity=original_receipt(rec),location=location)
            return
        if event in FINAL_EVENTS:
            self.final_events[event]=dict(original=value,identity=original_receipt(value),location=location)
            return
        if event=="persistent128_complete_chord_QR":
            small={k:v for k,v in value.items() if k not in ("current_input","formed_model_readback")}
            small["current_input_identity"]=original_receipt(value.get("current_input"))
            small["original_formed_model_readback"]=ordinary(value.get("formed_model_readback"))
            self.auxiliary.append(dict(original=ordinary(small),location=location));return
        if (event.startswith("persistent128_") or event.startswith("native_persistent128_")
                or event in ("operator_same_job_entry_error","qualified_same_job_component_logs_return",
                    "qualified_component_original_log_readback","global_final128_start")):
            if any(key in value for key in ("error","actual_error","traceback")):
                for key in ("error","actual_error","traceback"):
                    if isinstance(value.get(key),str):
                        for line in value[key].encode("utf-8","surrogateescape").splitlines(keepends=True):
                            self.errors.add(line,dict(event=event,key=key,original_location=location),force=True)
            if event in ("qualified_same_job_component_logs_return","qualified_component_original_log_readback"):
                result=value.get("result",{})
                self.auxiliary.append(dict(event=event,label=value.get("label"),
                    identity=original_receipt(value),location=location,
                    original_flags={k:result[k] for k in ("present","complete","readback_error",
                        "truncated","lines_forwarded","original_file") if k in result},
                    original_unforwarded_indivisible_lines=result.get("unforwarded_indivisible_lines")))
            else:
                self.auxiliary.append(dict(original=ordinary(value),location=location))
    def line(self,line):
        offset=self.total_bytes;self.total_bytes+=len(line);self.log_hash.update(line)
        self.lines+=1
        self.check()
        if len(line)>MAX_LINE_BYTES:raise ResourceStop("explicit-original160-log-single-line-cap")
        location=dict(physical_line=self.lines,raw_byte_offset=offset,
            raw_line_bytes=len(line),raw_line_sha256=sha(line))
        view=line
        if view.startswith(b"\xef\xbb\xbf"):
            self.bom_lines+=1;view=view[3:]
        view=TIMESTAMP.sub(b"",view,count=1).rstrip(b"\r\n")
        if view.startswith(b"NATIVE_PERSISTENT128 "):
            self.native_markers+=1;view=view[len(b"NATIVE_PERSISTENT128 "):]
        if not view.startswith(b"{"):
            # Cyan Actions command echoes are source text, not executed error records.
            if not view.startswith(b"\x1b[36;1m"):
                self.errors.add(view,location)
            return
        try:
            value=parsed(view)
            self.event(value,location)
        except ResourceStop:raise
        except Exception as error:
            if (b"persistent128" in view or b"qualified_" in view
                    or b"precleanup_" in view or b"operator_" in view):
                self.fail(error,location)
            else:self.unknown_json+=1
    def finish(self):
        # Optional large old protocols are scope evidence, never a precondition
        # for reading the genuine already-bounded direct scientific projections.
        for label,tree in self.trees.items():
            if not tree.complete:
                self.optional_issue(ValueError("Optional old tree metadata not completely verified"),
                    None,label)
        for label,text in self.texts.items():
            if not text.complete:
                self.optional_issue(ValueError("Old diagnostic byte stream not completely verified"),
                    None,label)
        if self.all_components is not None:
            record=self.all_components["original"]
            require(set(record["components"])==set(COMPONENTS),"All four actual component states")
            for name,ret in self.component_return.items():
                require(original_canonical(record["components"][name])==original_canonical(ret["original"]),
                    "Per-component direct return equals actual final state: "+name)
        final=self.last_owner("persistent128_owner_final")
        trials=[row["original"] for row in self.owner_rows
                if row["original"].get("event")=="persistent128_trial"]
        if final is not None:
            require(integer(final["trial_evaluations"],"original trial count")==len(trials),
                "All actual owner trial rows retained")
            addresses=[[row["iteration"],row["trial"]] for row in trials]
            require(original_canonical(addresses)==original_canonical(final["attempted_trial_addresses"]),
                "Original complete trial addresses and final record agree")
        self.check()
    def last_owner(self,event):
        return next((row["original"] for row in reversed(self.owner_rows)
                     if row["original"].get("event")==event),None)
    def owner_view(self):
        originals={name:[] for name in OWNER_EVENTS}
        identities=[];evaluations=[];evaluation_index={};evaluation_keys=set()
        def reference(value):
            if not isinstance(value,dict):return value
            key=original_canonical(value)
            if key not in evaluation_index:
                evaluation_index[key]=len(evaluations);evaluations.append(value)
                evaluation_keys.update(value)
            return dict(original_evaluation_index=evaluation_index[key])
        for row in self.owner_rows:
            original=row["original"];event=original["event"]
            body={key:(reference(value) if key in ("evaluation","current","final") else ordinary(value))
                for key,value in original.items()}
            originals[event].append(body)
            identities.append([event,original.get("iteration"),original.get("trial"),
                row["identity"]["canonical_bytes"],row["identity"]["canonical_sha256"],
                row["identity"]["original_location"]["physical_line"]])
        trials=originals["persistent128_trial"]
        def presence(rows):
            sets=[];lookup={};indices=[]
            for row in rows:
                keys=tuple(sorted(row))
                if keys not in lookup:
                    lookup[keys]=len(sets);sets.append(list(keys))
                indices.append(lookup[keys])
            return sets,indices
        trial_key_sets,trial_key_set_indices=presence(trials)
        evaluation_key_sets,evaluation_key_set_indices=presence(evaluations)
        columns=["iteration","trial","directory","alpha","base_norm","accepted","reason",
            "changed128_state_words","changed128_with_same64_cast_values",
            "elapsed_seconds","evaluation"]
        extra=sorted({key for row in trials for key in row if key not in columns and key!="event"})
        columns+=extra
        trial_rows=[[row.get(k) for k in columns] for row in trials]
        brief={}
        for event,rows in originals.items():
            if event=="persistent128_trial":continue
            if event in ("persistent128_matched_trace","persistent128_final_stage_column"):
                brief[event]=dict(count=len(rows),identity=original_receipt(rows),
                    complete_successful_trace_arrays_or_column_records_not_returned=True,
                    original_failure_records=[row for row in rows if row.get("complete") is False or
                        isinstance(row.get("report"),dict) and row["report"].get("complete") is False])
            else:brief[event]=rows
        fields=sorted(evaluation_keys)
        evaluation_rows=[[actual_error(row.get(k)) if k=="evaluation_error"
            else failed_stage_projection(row[k]) if k=="failed_stages" and isinstance(row.get(k),list)
            else ordinary(row.get(k)) for k in fields] for row in evaluations]
        final=self.last_owner("persistent128_owner_final")
        return dict(original_rows=brief,trial_columns=columns,
            all_original_trial_rows=trial_rows,trial_count=len(trials),
            original_trial_key_sets=trial_key_sets,
            original_trial_key_set_index_by_row=trial_key_set_indices,
            original_evaluation_key_sets=evaluation_key_sets,
            original_evaluation_key_set_index_by_row=evaluation_key_set_indices,
            missing_key_and_explicit_null_distinguished_by_original_key_sets=True,
            evaluation_columns=fields,all_distinct_original_evaluation_rows=evaluation_rows,
            evaluation_identities=[original_receipt(row) for row in evaluations],
            evaluations_shared_only_if_every_original_parsed_field_is_equal=True,
            complete_original_trial_root_statistics_and_norms_retained_in_evaluation_table=True,
            owner_identity_columns=["event","iteration","trial","canonical_bytes",
                "canonical_sha256","original_physical_log_line"],
            all_owner_event_identity_rows=identities,
            duplicate_original_event_counts=dict(self.owner_duplicates),
            original_final_record_observed=final is not None,
            original_final_trial_addresses_and_count_verified=final is not None,
            original_unvisited_direction_and_trial_lists_from_final_record_only=True,
            binary128_state_arrays_not_downloaded_or_recomputed=True)
    def components_view(self):
        answer={};all_rec=self.all_components["original"] if self.all_components else {}
        for name in COMPONENTS:
            entry=dict(original_component_name=name,
                original_return_observed=name in self.component_return,
                original_tree_complete_marker_observed=name in self.tree_results)
            item=(self.component_return.get(name) or {}).get("original")
            if item is None:item=all_rec.get("components",{}).get(name)
            tree=self.tree_results.get(name)
            if item is not None:
                # One body only: the original already-compact direct return.
                excluded=("scientific_report","full_component_log_readback",
                    "complete_original_summary_readback","component_lifecycle")
                entry["actual_lifecycle_return"]=ordinary({k:v for k,v in item.items()
                    if k not in excluded})
                entry["actual_complete_return_identity"]=original_receipt(item)
                entry["original_scientific_report"]=direct_scientific_projection(item.get("scientific_report"))
                entry["scientific_report_origin"]="original precleanup component direct projection"
                for key in ("full_component_log_readback","complete_original_summary_readback",
                            "component_lifecycle"):
                    if key in item:entry[key+"_identity_only"]=original_receipt(item[key])
                if tree is not None and tree.complete:
                    entry["missing_direct_projection_metadata"]=tree.missing_stage_fields(
                        item.get("scientific_report") or {})
                elif tree is not None:
                    entry["optional_missing_fields_not_certified"]=True
            elif tree is not None and tree.complete:
                entry["actual_original_direct_state_unreported"]=True
                entry["original_scientific_report"]=tree.report
                entry["scientific_report_origin"]="only selected original typed-path fields; direct return absent"
                entry["original_unfinished_stage_metadata"]=tree.missing_stage_fields({})
                entry["original_selected_lifecycle_header"]=tree.header
                entry["full_old_tree_or_scientific_report_not_reconstructed"]=True
            else:
                entry["actual_original_state_unreported"]=True
                entry["not_started_or_complete_not_inferred"]=True
            if name in self.component_start:
                entry["original_start_identity"]=original_receipt(self.component_start[name]["original"])
                start=self.component_start[name]["original"]
                entry["original_start_resource_fields"]={k:v for k,v in start.items()
                    if k not in ("event","lifecycle_schema","command","scientific_command")}
            if tree is not None:entry["optional_original_tree_scope"]=tree.final_receipt
            if name in self.component_compact:
                entry["original_compact_summary_identity"]=self.component_compact[name]["identity"]
            answer[name]=entry
        top={k:v for k,v in all_rec.items() if k!="components"}
        return dict(all_four_original_components=answer,
            original_all_component_flags_and_global_lifecycle=ordinary(top) if self.all_components else None,
            original_all_component_return_identity=self.all_components["identity"] if self.all_components else None,
            original_component_bodies_returned_once=True)
    def terminal_view(self):
        """Return original terminal flags once; alias already retained owner data."""
        result={};seen={};owner_final=self.last_owner("persistent128_owner_final")
        keep=("schema","run","source_sha256","cpp_source_sha256","actual_error","actual_traceback",
            "procedure_complete","summary_complete","transport_complete","summary_transport_exit_code",
            "owner_final","final_scalar_flags","final_state128","final_residual128",
            "final_full226_stage_outputs128","fresh_replay_residual128","fresh_replay_all226_outputs128",
            "fresh_replay_full_residual_words_equal_owner","fresh_replay_all226_output_words_equal_owner",
            "independent_fresh_replay_complete","full_stage_J_complete",
            "endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete",
            "native_accepted","fullDN_completed","full_summary_bytes","full_summary_sha256",
            "actual_original_result","actual_original_response","original_response_scalars",
            "controlled_protocol_failure_not_math_rejection","original_driver_exit_code",
            "QR_direction_count","elapsed_seconds","bounded_final_stdout_fallback",
            "owner_final_complete_record_bytes","owner_final_complete_record_sha256")
        def owner_reference(value):
            if not isinstance(value,dict) or not isinstance(owner_final,dict):return ordinary(value)
            same=[key for key in value if key in owner_final and
                original_canonical(value[key])==original_canonical(owner_final[key])]
            if not same:return ordinary(value)
            other={key:item for key,item in value.items() if key not in same}
            return dict(original_identity=original_receipt(value),
                identical_original_fields_at="owner.original_rows.persistent128_owner_final[0]",
                identical_original_field_names=sorted(same),other_original_fields=ordinary(other),
                comparison_performed_on_original_records_before_summary_projection=True)
        def selected(value,path):
            small={key:(owner_reference(value[key]) if key=="owner_final"
                else ordinary(value[key])) for key in keep if key in value}
            key=original_canonical(small)
            if key in seen:
                return dict(identical_selected_original_fields_at=seen[key],
                    selected_fields_identity=original_receipt(small))
            seen[key]=path;return small
        for name,row in self.final_events.items():
            value=row["original"]
            small=ordinary({key:item for key,item in value.items()
                if key not in ("summary","result","generation")})
            summary=value.get("summary")
            if isinstance(summary,dict):
                small["original_selected_summary"]=selected(summary,name+".original_selected_summary")
                small["complete_original_summary_identity"]=original_receipt(summary)
                if isinstance(summary.get("independent_fresh_replay"),dict):
                    replay=summary["independent_fresh_replay"]
                    small["independent_fresh_replay_process"]=ordinary(
                        {key:item for key,item in replay.items() if key!="records"})
                for key in ("persistent128_scientific_summary","persistent128_bridge","post_owner_components"):
                    if key not in summary:continue
                    small[key+"_identity"]=original_receipt(summary[key])
                    if key=="persistent128_scientific_summary" and isinstance(summary[key],dict):
                        small["original_forwarded_owner_fields"]=selected(
                            summary[key],name+".original_forwarded_owner_fields")
                    elif key=="post_owner_components" and self.all_components is not None:
                        if original_canonical(summary[key])==original_canonical(self.all_components["original"]):
                            small["post_owner_components_same_original_record_at"]="components"
                        else:
                            small["post_owner_components_not_identical_to_direct_return"]=True
                            if isinstance(summary[key],dict):
                                small["different_post_owner_original_flags"]=ordinary(
                                    {k:v for k,v in summary[key].items() if k!="components"})
            if isinstance(value.get("result"),dict):
                rec=value["result"]
                names=("schema","independent_experiment_returned","transport_complete",
                    "child_exit","actual_error","error","owner_temporary_root",
                    "raw_outputs_cleaned","native_accepted","fullDN_completed")
                small["original_bridge_result"]=ordinary({key:rec[key] for key in names if key in rec})
                small["complete_original_bridge_result_identity"]=original_receipt(rec)
                if isinstance(rec.get("scientific_summary"),dict):
                    small["original_bridge_scientific_fields"]=selected(
                        rec["scientific_summary"],name+".original_bridge_scientific_fields")
            result[name]=dict(original=small,identity=row["identity"],location=row["location"])
        return result
    def summary(self):
        text_receipts=[state.final_receipt for state in self.texts.values() if state.complete]
        unfinished_text=[dict(label=label,bytes_seen=state.position,parts_seen=state.count,
            prefix_sha256=state.hash.hexdigest(),complete=False,original_file=state.original)
            for label,state in self.texts.items() if not state.complete]
        return dict(full_log=dict(bytes=self.total_bytes,sha256=self.log_hash.hexdigest(),
                physical_lines=self.lines,complete=self.fully_streamed,
                original_raw_log_saved=False),
            parsed_physical_line_BOM_count=self.bom_lines,
            timestamp_BOM_removed_only_in_parse_view=True,
            original_event_counts=dict(self.events),original_wrapper_counts=dict(self.wrapper_events),
            original_native_marker_line_count=self.native_markers,
            nonprotocol_JSON_line_count=self.unknown_json,
            owner=self.owner_view(),components=self.components_view(),
            original_terminal_events=self.terminal_view(),
            original_QR_resource_error_and_lifecycle_events=self.auxiliary,
            optional_original_typed_tree_scope_is_in_each_component_entry=True,
            unfinished_original_component_semantic_trees=[
                dict(label=label,parts_seen=tree.count,part_metadata_sha256=tree.meta.hexdigest())
                for label,tree in self.trees.items() if not tree.complete],
            verified_original_diagnostic_byte_streams=text_receipts,
            unfinished_original_diagnostic_byte_streams=unfinished_text,
            declared_absent_original_logs_or_summaries=self.log_absent,
            original_component_parse_errors=self.parse_error_events,
            selected_original_diagnostic_matching_text=self.errors.record(),
            original_direct_error_line_protocol_files=[
                dict(label=key[0],original_file=self.original_line_identities[key],
                    original_lines_with_individual_bytes_SHA_verified=count)
                for key,count in self.original_line_records.items()],
            optional_old_protocol_issue_count=self.optional_old_issue_count,
            optional_old_protocol_issues=self.optional_old_protocol_issues,
            original_direct_projection_does_not_require_full_old_tree_reconstruction=True,
            protocol_error_count=self.protocol_error_count,
            protocol_errors=self.protocol_errors,
            complete_successful_binary_arrays_and_factors_not_downloaded=True,
            complete_successful_stage_and_column_metadata_returned_only_as_identities=True,
            no_new_numeric_array_residual_norm_J_domain_or_interval_computation=True,
            no_original_native_or_BVP_acceptance_reclassification=True)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Only this public Actions job reads the original completed large log")
    request_raw=args.request.read_bytes();request=json.loads(request_raw)
    require(request.get("schema")==REQUEST_SCHEMA and request.get("request_number")==182,
        "Independent request182 metadata-only reader")
    source=file_receipt(__file__)
    require(request["source_entry"]==Path(__file__).name and
        request["source_bytes"]==source["bytes"] and request["source_sha256"]==source["sha256"],
        "Bind the actual necessary-reader source")
    require(request["original_run_id"]==RUN and request["original_job_id"]==JOB and
        request["original_source_commit"]==SOURCE_COMMIT,"Fixed actual160 tuple")
    require(request["original_text_sources"]==ORIGINAL_SOURCES,"All eight original text identities")
    require(request["maximum_scan_seconds"]==1200 and
        request["maximum_original_log_bytes"]==34359738368 and
        request["maximum_one_summary_bytes"]==MAX_SUMMARY_BYTES,
        "Explicit metadata transport resources; no scientific resource change")
    original_request=None
    for record in ORIGINAL_SOURCES:
        path=args.code_directory/record["file"]
        require(path.is_file() and not path.is_symlink(),"Plain pinned original source")
        raw=path.read_bytes()
        require(len(raw)==record["bytes"] and sha(raw)==record["sha256"],
            "Read but never import original text: "+record["file"])
        if record["file"]=="public-native-operator-qualified-v2-final128-request.json":
            original_request=json.loads(raw)
    require(original_request is not None and original_request.get("request_number")==160,
        "Exact original160 request")
    for record in ORIGINAL_SOURCES:
        if record["file"].endswith((".py",".cpp")):
            require(original_request["source_sha256"][record["file"]]==record["sha256"],
                "Original160 request source closure agrees: "+record["file"])
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(args.out.name=="visible-actual160-necessary-182" and
        args.out.resolve().parent==temporary and not args.out.exists() and not args.out.is_symlink(),
        "Only the new direct request182 temporary directory is owned")
    args.out.mkdir()
    started=time.monotonic();deadline=started+request["maximum_scan_seconds"]
    scan=Scan(deadline,request["maximum_original_log_bytes"])
    output=dict(schema=SCHEMA,request_number=182,repository=REPOSITORY,
        run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
        source=source,actual_request=dict(file=args.request.name,bytes=len(request_raw),sha256=sha(request_raw)),
        original_run_id=RUN,original_job_id=JOB,original_source_commit=SOURCE_COMMIT,
        original_report_job_id=132921319875,
        original_report_not_downloaded_again=True,
        original_text_sources=ORIGINAL_SOURCES,old_sources_read_not_imported=True,
        original_request_source_closure_verified=True,
        readback_complete=False,resource_partial=False,error=None,
        original_scientific_conclusion_not_changed=True,
        direct_original_projections_are_primary=True,
        optional_old_tree_supplement_not_required_for_direct_readback=True,
        full_original_component_semantic_trees_not_reconstructed=True,
        original_child70_not_reclassified_as_mathematical_failure=True,
        new_scientific_calls=0,raw_Git_Release_artifact_uploads=0,
        old_raw_log_saved=False,new_output_segment_protocol_used=False)
    code=2;response=None
    def interrupted(signum,frame):
        raise ResourceStop("metadata-reader-external-signal-"+str(signum))
    def expired(signum,frame):
        raise ResourceStop("explicit-original160-log-scan-wall-budget")
    signal.signal(signal.SIGTERM,interrupted);signal.signal(signal.SIGINT,interrupted)
    signal.signal(signal.SIGALRM,expired);signal.alarm(request["maximum_scan_seconds"])
    try:
        token=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        require(bool(token),"The read-only job token is supplied only in the process environment")
        run,run_receipt=api_json("/actions/runs/"+str(RUN),token)
        job,job_receipt=api_json("/actions/jobs/"+str(JOB),token)
        require(run.get("id")==RUN and run.get("head_sha")==SOURCE_COMMIT and
            run.get("status")=="completed","Official completed original run identity")
        require(job.get("id")==JOB and job.get("run_id")==RUN and
            job.get("status")=="completed" and job.get("conclusion")=="failure",
            "Original completed compute job, not a newly recreated run")
        output["official_run"]=dict(receipt=run_receipt,id=run["id"],head_sha=run["head_sha"],
            status=run["status"],conclusion=run.get("conclusion"))
        output["official_job"]=dict(receipt=job_receipt,id=job["id"],run_id=job["run_id"],
            status=job["status"],conclusion=job.get("conclusion"),name=job.get("name"))
        scan.check()
        response,transport=open_log(token)
        output["official_log_transport"]=transport
        require(response.status==200,"The one official original log response returned200")
        encoding=response.headers.get("Content-Encoding")
        require(encoding in (None,"","identity"),"Hash the exact unencoded official response bytes")
        advertised=response.headers.get("Content-Length")
        if advertised is not None:
            require(re.fullmatch(r"[0-9]+",advertised) is not None,"Integer original Content-Length")
        output["advertised_original_log_bytes"]=None if advertised is None else int(advertised)
        while True:
            scan.check()
            line=response.readline(MAX_LINE_BYTES+1)
            if not line:break
            scan.line(line)
        scan.fully_streamed=True
        if advertised is not None:
            require(scan.total_bytes==int(advertised),"Whole official response Content-Length")
        scan.finish()
        output["readback_complete"]=scan.protocol_error_count==0
        code=0 if output["readback_complete"] else 2
    except ResourceStop as error:
        output["resource_partial"]=True
        output["error"]=dict(type=type(error).__name__,message=str(error));code=3
    except BaseException as error:
        output["error"]=dict(type=type(error).__name__,message=str(error),
            traceback=actual_error(traceback.format_exc()))
        code=2
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)
        if response is not None:response.close()
        try:
            output.update(scan.summary())
        except BaseException as error:
            output["readback_complete"]=False;code=2
            output["summary_projection_error"]=dict(type=type(error).__name__,message=str(error))
            output["full_log"]=dict(bytes=scan.total_bytes,sha256=scan.log_hash.hexdigest(),
                physical_lines=scan.lines,complete=scan.fully_streamed,original_raw_log_saved=False)
            output["original_event_counts"]=dict(scan.events)
            output["protocol_errors"]=scan.protocol_errors
        output["elapsed_metadata_scan_seconds"]=time.monotonic()-started
        output["reader_exit_code"]=code
        output["scientific_success_not_inferred_from_reader_success"]=True
        output["missing_original_fields_not_recreated"]=True
        full=write(args.out/"result.json",output)
        summary=dict(output,actual_temporary_readback_result=full,
            summary_complete=True,transport_complete=True,
            complete_necessary_scope_returned=output["readback_complete"])
        raw=canonical(summary)
        if len(raw)>MAX_SUMMARY_BYTES:
            # Never return encoded pieces of the discarded large tree or
            # silently remove trial rows to make the necessary result fit.
            keep=("schema","request_number","repository","run_id","source_commit","source",
                "actual_request","original_run_id","original_job_id","original_source_commit",
                "resource_partial","error","full_log","original_event_counts",
                "protocol_error_count","protocol_errors")
            failure={key:output[key] for key in keep if key in output}
            failure.update(actual_temporary_readback_result=full,
                readback_complete=False,summary_complete=False,transport_complete=False,
                original_internal_scan_complete=output["readback_complete"],
                necessary_unreturned_summary_bytes=len(raw),
                necessary_unreturned_summary_sha256=sha(raw),
                original_reader_exit_code=code,process_exit_code=70,
                transport_error="necessary-original-metadata-exceeds90000bytes",
                complete_necessary_scope_returned=False,
                no_trial_or_unfinished_stage_silently_truncated=True,
                no_new_output_segment_or_reassembly_protocol=True,
                original_scientific_conclusion_not_changed=True)
            summary=failure;code=70;raw=canonical(summary)
        require(len(raw)<=MAX_SUMMARY_BYTES,"One final necessary summary remains bounded")
        write(args.out/"summary.json",summary)
        print("BEGIN_REQUEST182_ORIGINAL160_NECESSARY_SUMMARY",flush=True)
        sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()
        print("END_REQUEST182_ORIGINAL160_NECESSARY_SUMMARY",flush=True)
        emit(dict(event="request182_necessary_summary_identity",bytes=len(raw),sha256=sha(raw),
            reader_exit_code=code,hash_includes_final_LF=True,
            no_new_scientific_computation=True,no_new_output_reassembly_protocol=True))
        write(args.out/"summary-stdout-complete.json",dict(bytes=len(raw),sha256=sha(raw)))
    return code


if __name__=="__main__":
    raise SystemExit(main())
