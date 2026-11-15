#!/usr/bin/env python3
"""Request176: stream the actual165 log and recover its original38 refutations.

Pure JSON/bytes/metadata. No interval, profile, polynomial, C producer, native
solver or numerical array is imported or evaluated. The old entire log is
streamed once, SHA identified, and never saved as a raw local file.
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
SCHEMA="actual165-original-log-selected38-bounded-columns-readback-v2"
REQUEST_SCHEMA="actual165-original-log-domain-refutations-readback-request-v1"
RUN=43736208020
JOB=132879253906
SOURCE_COMMIT="1f2ec637430e5c6b27b1a93720e106539281a156"
ORIGINAL_SOURCE="root_20261115_continuous_nine_shared_target_enclosures.py"
ORIGINAL_SOURCE_BYTES=94125
ORIGINAL_SOURCE_SHA="61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205"
ORIGINAL_RESULT_BYTES=105512
ORIGINAL_RESULT_SHA="e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619"
EXPECTED_REFUTED=38
EXPECTED_PENDING=32526
EXPECTED_UNRESOLVED=32488
EXPECTED_COVER=32977
MAX_LINE_BYTES=1048576
MAX_RELEVANT_EVENT_BYTES=4194304
TIMESTAMP=re.compile(rb"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ")
EVENT_WORD=re.compile(rb'"event"\s*:\s*"(request165_[A-Za-z0-9_-]+)"')
INTERESTED={
    "request165_final_complete_cover_leaf",
    "request165_full_pending_or_refuted_interval",
    "request165_primary_complete_result_readback_identity",
}
LABELS=INTERESTED|{"complete-target-result"}


class LiteralNumber(str):
    """An original JSON number lexeme, never a new scientific numeric value."""
    pass


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parsed(raw):
    return json.loads(raw.decode("ascii"),parse_int=LiteralNumber,parse_float=LiteralNumber)


def encoded(value):
    """Original number tokens survive; ordinary metadata integers remain ints."""
    if isinstance(value,LiteralNumber):return str(value)
    if value is None:return "null"
    if value is True:return "true"
    if value is False:return "false"
    if isinstance(value,str):return json.dumps(value,ensure_ascii=True)
    if isinstance(value,(int,float)):
        return json.dumps(value,allow_nan=False,separators=(",",":"))
    if isinstance(value,list):return "["+",".join(encoded(v) for v in value)+"]"
    if isinstance(value,dict):
        require(all(isinstance(k,str) for k in value),"String JSON object keys")
        return "{"+",".join(json.dumps(k,ensure_ascii=True)+":"+encoded(value[k])
            for k in sorted(value))+"}"
    raise TypeError("Unsupported literal JSON value "+type(value).__name__)


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
        "User-Agent":"actual165-original-log-readback","Accept-Encoding":"identity"}
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
        "User-Agent":"actual165-original-log-readback","Accept-Encoding":"identity"}
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
            "User-Agent":"actual165-original-log-readback","Accept-Encoding":"identity"})
        response=urllib.request.urlopen(redirected,timeout=60)
        return response,dict(official_job_logs_endpoint=url,official_redirect_status=error.code,
            bearer_token_not_forwarded_to_redirect=True,signed_URL_not_logged=True,
            downloaded_from_official_redirect=True)
    return response,dict(official_job_logs_endpoint=url,official_redirect_status=None,
        bearer_token_not_forwarded_to_redirect=True,signed_URL_not_logged=True,
        downloaded_from_official_redirect=False)


def node_identity(row):
    interval=row.get("closed_public_u")
    require(isinstance(interval,list) and len(interval)==2 and all(isinstance(v,str) for v in interval),
        "Keep both original exact interval strings without rational recomputation")
    return (integer(row["node_id"],"node_id"),integer(row["numeric_piece"],"numeric_piece"),
        interval[0],interval[1],integer(row["depth"],"depth"))


class Scan:
    def __init__(self,deadline,maxbytes):
        self.deadline=deadline;self.maxbytes=maxbytes
        self.log_hash=hashlib.sha256();self.total_bytes=0;self.lines=0
        self.fully_streamed=False;self.segments={}
        self.metadata_events=Counter();self.cover_count=0;self.pending_count=0
        self.unresolved_count=0;self.refuted_occurrences=0
        self.by_reason=Counter();self.by_reason_set=Counter();self.by_piece=Counter();self.by_depth=Counter()
        self.cover_refutations={};self.pending_refutations={}
        self.duplicates=[];self.original_result=None
        self.input_event_counts=Counter();self.input_label_counts=Counter()
        self.nonobject_relevant_count=0;self.nonobject_relevant_examples=[]
        self.utf8_bom_prefixed_raw_lines=0
        self.result_receipt=None;self.original_result_occurrences=[]
        self.original_primary_identity=[];self.malformed_relevant=[]
        self.contradictions=[];self.current_offset=0

    def check(self):
        if time.monotonic()>=self.deadline:raise ResourceStop("explicit-original-log-scan-wall-budget")
        if self.total_bytes>self.maxbytes:raise ResourceStop("explicit-original-log-byte-cap")

    def event(self,value,raw,location):
        if not isinstance(value,dict):return
        event=value.get("event")
        if event not in INTERESTED:return
        self.metadata_events[event]+=1
        if event=="request165_primary_complete_result_readback_identity":
            self.original_primary_identity.append(dict(source_location=location,
                original_event_sha256=sha(raw),original=value))
            return
        record=value["record"]
        if event=="request165_final_complete_cover_leaf":
            self.cover_count+=1
            if record.get("accurate_domain_rigorously_refuted") is not True:return
            key=node_identity(record);body=canonical(record)
            receipt=dict(bytes=len(body),sha256=sha(body),source_location=location,
                original_event_bytes=len(raw),original_event_sha256=sha(raw))
            if key in self.cover_refutations:
                previous=self.cover_refutations[key]
                require(previous["sha256"]==receipt["sha256"],
                    "Duplicate original final-cover identity has unchanged full literal record")
                self.duplicates.append(dict(scope="final-cover-refutation",key=list(key),
                    previous=previous,current=receipt))
            else:self.cover_refutations[key]=receipt
            return
        self.pending_count+=1
        require(record.get("classification") in ("unresolved","rigorous-domain-refutation"),
            "Keep the original pending classification")
        key=node_identity(record)
        reasons=record.get("reasons")
        require(isinstance(reasons,list) and all(isinstance(v,str) for v in reasons),
            "Original reason strings are retained")
        if record["classification"]=="unresolved":
            self.unresolved_count+=1
            self.by_piece[str(key[1])]+=1;self.by_depth[str(key[4])]+=1
            self.by_reason_set[canonical(reasons).decode("ascii").rstrip("\n")]+=1
            for reason in reasons:self.by_reason[reason]+=1
            return
        self.refuted_occurrences+=1
        current=record["retained_complete_enclosure"]
        require(current.get("accurate_domain_rigorously_refuted") is True and node_identity(current)==key,
            "The original pending entry and its retained complete enclosure name the same actual node")
        require(current.get("closed_cover_member_retained_at_stop") is True,
            "Only the original final retained cover member is a selected refutation")
        current_raw=canonical(current);body=canonical(record)
        parent=self.cover_refutations.get(key)
        require(parent is not None and parent["sha256"]==sha(current_raw) and parent["bytes"]==len(current_raw),
            "The full pending enclosure equals the original final-cover record, with original numeric lexemes")
        true_bounds=current.get("accurate_a_as_ass")
        require(isinstance(true_bounds,list) and len(true_bounds)==3,
            "Copy the actual original a/as bounds, without re-evaluating their inequalities")
        item=dict(node_id=record["node_id"],numeric_piece=record["numeric_piece"],
            closed_public_u=record["closed_public_u"],depth=record["depth"],
            classification=record["classification"],reasons=reasons,
            terminal_reason=record.get("terminal_reason"),
            accurate_a=true_bounds[0],accurate_as=true_bounds[1],
            accurate_radius_domain_rigorously_refuted=current.get("accurate_radius_domain_rigorously_refuted"),
            accurate_speed_domain_rigorously_refuted=current.get("accurate_speed_domain_rigorously_refuted"),
            original_pending_record=dict(bytes=len(body),sha256=sha(body)),
            original_complete_enclosure=dict(bytes=len(current_raw),sha256=sha(current_raw)),
            original_final_cover_record=parent,source_location=location,
            original_event_bytes=len(raw),original_event_sha256=sha(raw),
            original_pending_record_sha256=sha(body),
            no_new_interval_or_scientific_inequality_evaluated=True)
        if key in self.pending_refutations:
            previous=self.pending_refutations[key]
            require(previous["original_pending_record_sha256"]==sha(body),
                "Duplicate original pending node has unchanged full literal record")
            self.duplicates.append(dict(scope="pending-refutation",key=list(key),
                previous_source_location=previous["source_location"],current_source_location=location))
        else:self.pending_refutations[key]=item
        # Keep each linked unique row once; column names and repeated metadata
        # are supplied once by necessary_refutation_table(), never per object.

    def complete_segment(self,label,value,raw,location):
        if label=="complete-target-result":
            require(len(raw)==ORIGINAL_RESULT_BYTES and sha(raw)==ORIGINAL_RESULT_SHA,
                "Complete original target result bytes/SHA match the actual165 report")
            require(value.get("schema")=="request165-shared-calibration-complete-nine-target-enclosures-v1"
                and str(value.get("run_id"))==str(RUN) and value.get("source_commit")==SOURCE_COMMIT,
                "This is the actual165 target result, not another run or a recreated result")
            source=value.get("source") or {}
            require(source.get("file")==ORIGINAL_SOURCE and integer(source["bytes"],"original source bytes")==ORIGINAL_SOURCE_BYTES
                and source.get("sha256")==ORIGINAL_SOURCE_SHA,"Original complete source identity")
            self.original_result=value
            self.result_receipt=dict(bytes=len(raw),sha256=sha(raw),source_location=location)
            self.original_result_occurrences.append(self.result_receipt)
        else:self.event(value,raw,location)

    def line(self,line):
        offset=self.total_bytes;self.current_offset=offset
        self.log_hash.update(line);self.total_bytes+=len(line);self.lines+=1
        self.check()
        require(len(line)<=MAX_LINE_BYTES,"Original raw line exceeds explicit metadata transport limit")
        parse_line=line
        if parse_line.startswith(b"\xef\xbb\xbf"):
            self.utf8_bom_prefixed_raw_lines+=1
            parse_line=parse_line[3:]
        # Official concatenated job logs may repeat a UTF8 BOM at file boundaries.
        # Only parsing ignores that prefix; raw line and full-stream hashes keep it.
        payload=TIMESTAMP.sub(b"",parse_line,count=1).rstrip(b"\r\n").lstrip()
        event_word=EVENT_WORD.search(payload)
        if event_word is None:return
        if not payload.startswith(b"{"):
            self.nonobject_relevant_count+=1
            if len(self.nonobject_relevant_examples)<12:
                self.nonobject_relevant_examples.append(dict(raw_log_line=self.lines,
                    raw_log_byte_offset=offset,raw_log_line_bytes=len(line),
                    raw_log_line_sha256=sha(line),
                    recognized_event_word=event_word.group(1).decode("ascii"),
                    prefix_bytes_before_event=event_word.start()))
            return
        # Both canonical and whitespace-separated original JSON event syntax
        # are read. Unknown labels are counted, never guessed as paid leaves.
        try:value=parsed(payload)
        except Exception as error:
            relevant=any(name.encode("ascii") in payload for name in INTERESTED|LABELS|
                {"request165_complete_metadata_begin","request165_complete_metadata_segment"})
            if relevant:
                self.malformed_relevant.append(dict(line=self.lines,byte_offset=offset,
                    bytes=len(line),sha256=sha(line),error_type=type(error).__name__,
                    error_message=str(error)))
            return
        event=value.get("event") if isinstance(value,dict) else None
        if isinstance(event,str):self.input_event_counts[event]+=1
        if event in ("request165_complete_metadata_begin","request165_complete_metadata_segment"):
            label=value.get("label")
            if isinstance(label,str):self.input_label_counts[event+":"+label]+=1
        location=dict(raw_log_line=self.lines,raw_log_byte_offset=offset,
            raw_log_line_bytes=len(line),raw_log_line_sha256=sha(line))
        if event=="request165_complete_metadata_begin":
            label=value.get("label")
            if label not in LABELS:return
            require(label not in self.segments,"A relevant original segmented event may not be silently overwritten")
            size=integer(value["bytes"],"segmented bytes")
            count=integer(value["segments"],"segmented count")
            require(0<=size<=MAX_RELEVANT_EVENT_BYTES and count>0,
                "Bounded original semantic record")
            self.segments[label]=dict(begin=value,location=location,parts=[],next_index=0)
        elif event=="request165_complete_metadata_segment":
            label=value.get("label")
            if label not in LABELS:return
            state=self.segments.get(label)
            require(state is not None,"Relevant original segment has its actual begin receipt")
            require(integer(value["index"],"segment index")==state["next_index"]
                and integer(value["segments"],"segment count")==integer(state["begin"]["segments"],"begin count"),
                "Complete original segment order")
            data=value.get("data")
            require(isinstance(data,str) and data.isascii(),"Original semantic data is exact ASCII")
            state["parts"].append(data);state["next_index"]+=1
            if state["next_index"]==integer(state["begin"]["segments"],"begin count"):
                raw="".join(state["parts"]).encode("ascii")
                require(len(raw)==integer(state["begin"]["bytes"],"begin bytes")
                    and sha(raw)==state["begin"]["sha256"],"Whole original semantic record bytes/SHA")
                original=parsed(raw)
                self.complete_segment(label,original,raw,dict(
                    begin=state["location"],end=location,segments=state["next_index"]))
                del self.segments[label]
        else:self.event(value,payload+b"\n",location)

    def finish(self):
        require(self.fully_streamed,"Whole official log stream completed")
        require(not self.segments and not self.malformed_relevant,
            "No relevant segmented suffix or malformed record is omitted")
        require(self.original_result is not None,"The complete actual original target result was found")
        counts=self.original_result["current_cover_counts"]
        require(self.cover_count==integer(counts["leaves"],"original leaves")==EXPECTED_COVER,
            "All original final-cover events are accounted as metadata")
        require(self.pending_count==integer(self.original_result["complete_pending_or_refuted_rows"],"pending rows")==EXPECTED_PENDING,
            "Every original pending/refuted interval was classified as recorded")
        require(self.unresolved_count==integer(counts["unresolved"],"unresolved rows")==EXPECTED_UNRESOLVED,
            "Complete original unresolved count")
        require(len(self.pending_refutations)==integer(counts["rigorously_refuted"],"refutation count")==EXPECTED_REFUTED,
            "All38 original unique strict-refutation records are recovered")
        require(set(self.pending_refutations)==set(self.cover_refutations),
            "The selected pending set equals the retained refuted cover set")
        return True

    def necessary_refutation_table(self):
        """Only literal field selection/column layout; no a/as comparison."""
        columns=["node_id","numeric_piece","u_left","u_right","depth",
            "classification","reason_indices","terminal_reason_index",
            "radius_refuted","speed_refuted","a_exponent2","a_lower","a_upper",
            "as_exponent2","as_lower","as_upper",
            "pending_bytes","pending_sha256","enclosure_bytes","enclosure_sha256",
            "pending_log_location","pending_event_bytes","pending_event_sha256",
            "cover_log_location","cover_event_bytes","cover_event_sha256"]
        reason_strings=[];terminal_strings=[];rows=[]
        for row in self.pending_refutations.values():
            reason_ids=[]
            for text in row["reasons"]:
                if text not in reason_strings:reason_strings.append(text)
                reason_ids.append(reason_strings.index(text))
            terminal=row["terminal_reason"]
            if terminal not in terminal_strings:terminal_strings.append(terminal)
            a=row["accurate_a"];v=row["accurate_as"]
            for bound in (a,v):
                require(all(k in bound for k in ("binary_exponent","lower_integer","upper_integer")),
                    "Copy the original exact fixed-grid bound fields")
            cover=row["original_final_cover_record"]
            rows.append([row["node_id"],row["numeric_piece"],*row["closed_public_u"],row["depth"],
                row["classification"],reason_ids,terminal_strings.index(terminal),
                row["accurate_radius_domain_rigorously_refuted"],row["accurate_speed_domain_rigorously_refuted"],
                a["binary_exponent"],a["lower_integer"],a["upper_integer"],
                v["binary_exponent"],v["lower_integer"],v["upper_integer"],
                row["original_pending_record"]["bytes"],row["original_pending_record"]["sha256"],
                row["original_complete_enclosure"]["bytes"],row["original_complete_enclosure"]["sha256"],
                row["source_location"],row["original_event_bytes"],row["original_event_sha256"],
                cover["source_location"],cover["original_event_bytes"],cover["original_event_sha256"]])
        return dict(columns=columns,reason_strings=reason_strings,terminal_reason_strings=terminal_strings,
            rows=rows,original_literal_a_as_inequalities_not_recomputed=True,
            complete_enclosure_and_unnecessary_jet_target_fields_not_returned=True)


    def summary(self):
        result=self.original_result or {}
        keys=("schema","run_id","source_commit","source","phase","procedure_complete",
            "scientific_controlled_exit_code","resource_stop_reason","error",
            "target_policy","full_public_u_closed_cover","current_cover_counts",
            "complete_unvisited_coarse_count","complete_pending_or_refuted_rows",
            "full_accurate_radius_positivity_proved","full_accurate_open_unit_speed_domain_proved",
            "full_accurate_nine_parameter_domain_proved",
            "at_least_one_accurate_domain_interval_rigorously_refuted",
            "comparison_work_goal_complete","global_delta_upper",
            "global_radial_relative_target_difference","accurate_total_length",
            "literal_total_length_exact","input_binding","exact_Q_grid_binding")
        return dict(
            actual_original_target_result={k:result[k] for k in keys if k in result},
            actual_original_target_result_receipt=self.result_receipt,
            full_log=dict(bytes=self.total_bytes,sha256=self.log_hash.hexdigest(),
                complete=self.fully_streamed,raw_lines=self.lines,raw_log_saved=False),
            original_final_cover_events=self.cover_count,
            original_pending_or_refuted_events=self.pending_count,
            original_refutation_event_occurrences=self.refuted_occurrences,
            original_unique_refutations=len(self.pending_refutations),
            original_unresolved_events=self.unresolved_count,
            unresolved_reason_counts=dict(sorted(self.by_reason.items())),
            unresolved_reason_combination_counts=dict(sorted(self.by_reason_set.items())),
            unresolved_numeric_piece_counts=dict(sorted(self.by_piece.items(),key=lambda x:int(x[0]))),
            unresolved_depth_counts=dict(sorted(self.by_depth.items(),key=lambda x:int(x[0]))),
            selected_original_refutation_locations_and_bounds=self.necessary_refutation_table(),
            selected38_full_enclosure_links_observed=(
                len(self.pending_refutations)==EXPECTED_REFUTED
                and set(self.pending_refutations)==set(self.cover_refutations)
                and self.original_result is not None),
            selected38_observation_does_not_replace_full_cover_count_check=True,
            utf8_bom_prefixed_raw_line_count=self.utf8_bom_prefixed_raw_lines,
            input_event_counts=dict(sorted(self.input_event_counts.items())),
            input_segment_label_counts=dict(sorted(self.input_label_counts.items())),
            nonobject_relevant_line_count=self.nonobject_relevant_count,
            nonobject_relevant_line_identity_examples=self.nonobject_relevant_examples,
            original_full_result_and_complete_enclosures_verified_in_Actions_only=True,
            complete_scientific_enclosure_payload_reprinted=False,
            identical_original_duplicate_events=self.duplicates,
            incomplete_relevant_segments=[dict(label=k,begin=v["begin"],received_segments=v["next_index"])
                for k,v in self.segments.items()],
            malformed_relevant_record_identities=self.malformed_relevant,
            original_primary_readback_identities=self.original_primary_identity,
            original_result_occurrences=self.original_result_occurrences,
            no_interval_or_scientific_arithmetic=True,
            all_original_interval_bound_strings_and_number_lexemes_preserved=True,
            no_new_C_profile_polynomial_native_FD_or_ODE_call=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Only the authorized public Actions job transports the old large log")
    request=json.loads(args.request.read_bytes())
    require(request.get("schema")==REQUEST_SCHEMA and request.get("request_number")==176,
        "Independent pure original-log reader")
    require(request["source_sha256"]==file_receipt(__file__)["sha256"],"Actual reader source")
    original=(args.code_directory/ORIGINAL_SOURCE).read_bytes()
    require(len(original)==ORIGINAL_SOURCE_BYTES and sha(original)==ORIGINAL_SOURCE_SHA,
        "Read but do not import the actual165 emitter source")
    require(request["original_run_id"]==RUN and request["original_job_id"]==JOB
        and request["original_source_commit"]==SOURCE_COMMIT,"Fixed actual165 tuple")
    root=Path(os.environ["RUNNER_TEMP"]).resolve()
    require(not args.out.exists() and not args.out.is_symlink()
        and args.out.resolve().is_relative_to(root) and args.out.resolve()!=root,
        "Fresh small temporary result directory")
    args.out.mkdir(parents=True)
    started=time.monotonic();deadline=started+request["maximum_scan_seconds"]
    scan=Scan(deadline,request["maximum_original_log_bytes"])
    output=dict(schema=SCHEMA,request=176,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),source=file_receipt(__file__),
        original_run_id=RUN,original_job_id=JOB,original_source_commit=SOURCE_COMMIT,
        readback_complete=False,resource_partial=False,error=None,
        original_scientific_conclusion_not_changed=True,
        request175_or_any_scientific_acceptance_gate=False,
        raw_Git_Release_artifact_uploads=0)
    code=2;response=None
    def interrupted(signum,frame):
        raise ResourceStop("external-signal-"+str(signum))
    signal.signal(signal.SIGTERM,interrupted);signal.signal(signal.SIGINT,interrupted)
    try:
        token=os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        require(bool(token),"The job token is supplied only via process environment")
        run,run_receipt=api_json("/actions/runs/"+str(RUN),token)
        job,job_receipt=api_json("/actions/jobs/"+str(JOB),token)
        require(run.get("id")==RUN and run.get("head_sha")==SOURCE_COMMIT
            and run.get("status")=="completed","Official immutable original run identity")
        require(job.get("id")==JOB and job.get("run_id")==RUN
            and job.get("status")=="completed","Official original completed compute job")
        output["official_run"]=dict(receipt=run_receipt,id=run["id"],head_sha=run["head_sha"],
            status=run["status"],conclusion=run.get("conclusion"))
        output["official_job"]=dict(receipt=job_receipt,id=job["id"],run_id=job["run_id"],
            status=job["status"],conclusion=job.get("conclusion"),name=job.get("name"))
        scan.check()
        response,transport=open_log(token)
        output["official_log_transport"]=transport
        require(response.status==200,"Original job log download returned200")
        encoding=response.headers.get("Content-Encoding")
        require(encoding in (None,"","identity"),"Hash the exact unencoded official log bytes")
        advertised=response.headers.get("Content-Length")
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
        output["readback_complete"]=True;code=0
    except ResourceStop as error:
        output["resource_partial"]=True
        output["error"]=dict(type=type(error).__name__,message=str(error));code=3
    except BaseException as error:
        output["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())
        code=2
    finally:
        signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)
        if response is not None:response.close()
        output.update(scan.summary())
        output["elapsed_metadata_scan_seconds"]=time.monotonic()-started
        output["reader_exit_code"]=code
        output["all38_necessary_original_locations_and_bounds_selected"]=(
            output.get("selected38_full_enclosure_links_observed") is True)
        output["new_output_segment_protocol_used"]=False
        full=write(args.out/"result.json",output)
        summary=dict(output,actual_readback_result=full,summary_complete=True,transport_complete=True,
            complete_necessary38_table_returned=output["all38_necessary_original_locations_and_bounds_selected"])
        raw=canonical(summary)
        if len(raw)>90000:
            # Keep the actual internal scan result, but never split scientific
            # witness data to bypass the one-object transport limit.
            summary={k:output[k] for k in ("schema","request","run_id","source_commit",
                "source","original_run_id","original_job_id","original_source_commit",
                "resource_partial","error","full_log","original_unique_refutations",
                "original_unresolved_events","original_final_cover_events",
                "original_pending_or_refuted_events")}
            summary.update(actual_readback_result=full,summary_complete=False,transport_complete=False,
                original_internal_scan_complete=output["readback_complete"],
                readback_complete=False,reader_exit_code=code,process_exit_code=70,
                transport_error="necessary-original-metadata-exceeds90000bytes",
                necessary_summary_bytes=len(raw),necessary_summary_sha256=sha(raw),
                complete_necessary38_table_returned=False,
                no_new_output_segment_or_reassembly_protocol=True)
            code=70;raw=canonical(summary)
        require(len(raw)<=90000,"Final one-object metadata summary is bounded")
        write(args.out/"summary.json",summary)
        print("BEGIN_REQUEST176_ORIGINAL165_REFUTATIONS_SUMMARY",flush=True)
        sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()
        print("END_REQUEST176_ORIGINAL165_REFUTATIONS_SUMMARY",flush=True)
        emit(dict(event="request176_summary_identity",bytes=len(raw),sha256=sha(raw),
            reader_exit_code=code,hash_includes_final_LF=True,
            no_new_scientific_computation=True))
        write(args.out/"summary-stdout-complete.json",dict(bytes=len(raw),sha256=sha(raw)))
    return code


if __name__=="__main__":
    raise SystemExit(main())
