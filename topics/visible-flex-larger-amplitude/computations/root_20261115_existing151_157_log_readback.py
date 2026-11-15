#!/usr/bin/env python3
"""Request163: original151/157 Actions log transport and JSON metadata only.

No model, derivative, norm, interval, matrix, optimizer or scientific module
is executed. The only arithmetic is integer byte/index/record accounting.
Original scalar numeric tokens are opaque strings in RawNumber. The original
large logs stay under this request's RUNNER_TEMP and are removed after all
selected complete semantic output and explicit coverage receipts are emitted.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "existing151157-original-log-metadata-readback-v1"
LIMIT = 90000
WIDTH = 12000
PREFIX = re.compile(r"^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z ")
NUMBER = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\Z")
OUTPUTS = []


class ReadbackError(Exception):
    pass


class RawNumber:
    """Original JSON number lexeme; deliberately no scientific arithmetic."""
    __slots__ = ("text",)
    def __init__(self, text):
        if not NUMBER.fullmatch(text):
            raise ReadbackError("Invalid original JSON numeric token")
        self.text = text


def reject_constant(value):
    raise ReadbackError("Original strict JSON contains nonfinite constant: "+value)


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ReadbackError("Duplicate original JSON object key: "+key)
        out[key] = value
    return out


def decode(raw):
    return json.loads(raw, parse_int=RawNumber, parse_float=RawNumber,
                      parse_constant=reject_constant, object_pairs_hook=unique)


def encode_text(value):
    if isinstance(value, RawNumber):
        return value.text
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=True, allow_nan=False)
    if isinstance(value, list):
        return "["+",".join(encode_text(x) for x in value)+"]"
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise ReadbackError("Non-string JSON metadata key")
        return "{"+",".join(encode_text(key)+":"+encode_text(value[key])
                            for key in sorted(value))+"}"
    raise ReadbackError("Unexpected metadata type: "+type(value).__name__)


def canonical(value, newline=False):
    return (encode_text(value)+("\n" if newline else "")).encode("ascii")


def integer(value):
    if isinstance(value, RawNumber):
        if not re.fullmatch(r"-?(?:0|[1-9][0-9]*)", value.text):
            raise ReadbackError("A record index/count was not an integer token")
        return int(value.text)
    if type(value) is int:
        return value
    raise ReadbackError("Expected integer metadata")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(raw):
    return dict(bytes=len(raw), sha256=sha(raw))


def file_identity(path):
    h = hashlib.sha256()
    size = 0
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
            size += len(block)
    return dict(bytes=size, sha256=h.hexdigest())


def emit(value):
    raw = canonical(value)
    if len(raw) > LIMIT:
        raise ReadbackError("An individual metadata event exceeds 90000 bytes")
    sys.stdout.write(raw.decode("ascii")+"\n")
    sys.stdout.flush()


def stream_text(label, text, scope, original=None):
    """Complete ASCII text, including any original final LF, never truncated."""
    raw = text.encode("ascii")
    count = max(1, (len(text)+WIDTH-1)//WIDTH)
    rec = dict(label=label, **identity(raw), parts=count, scope=scope,
               original_identity=original,
               reconstruction="Concatenate decoded data strings by index; exact ASCII bytes")
    emit(dict(event="readback163-semantic-begin", **rec))
    for index in range(count):
        data = text[index*WIDTH:(index+1)*WIDTH]
        emit(dict(event="readback163-semantic-part", label=label, index=index,
                  parts=count, data=data, data_identity=identity(data.encode("ascii"))))
    emit(dict(event="readback163-semantic-end", label=label,
              bytes=rec["bytes"], sha256=rec["sha256"], parts=count))
    OUTPUTS.append(rec)
    return rec


def stream_value(label, value, scope):
    return stream_text(label, encode_text(value), scope)


class Checks:
    def __init__(self):
        self.count = 0
        self.h = hashlib.sha256()
    def equal(self, label, actual, expected):
        okay = canonical(actual) == canonical(expected)
        row = dict(label=label, matches=okay)
        self.h.update(canonical(row, True))
        self.count += 1
        if not okay:
            stream_value("failed-metadata-comparison", dict(
                label=label, actual=actual, expected=expected),
                "Original metadata comparison failure; not scientific rejection")
            raise ReadbackError(label)
    def bytes(self, label, raw, expected):
        actual = identity(raw)
        self.equal(label+" bytes", actual["bytes"], integer(expected["bytes"]))
        self.equal(label+" SHA256", actual["sha256"], expected["sha256"])
        return actual
    def summary(self):
        return dict(performed=self.count, all_performed_checks_matched=True,
                    ordered_check_results_sha256=self.h.hexdigest(),
                    scientific_arithmetic_performed=False)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


class GitHub:
    def __init__(self, token):
        if not token:
            raise ReadbackError("Actions read token is unavailable")
        self.token = token
        self.opener = urllib.request.build_opener(NoRedirect())
    def request(self, path):
        if not path.startswith("/repos/"+REPOSITORY+"/") or "\n" in path:
            raise ReadbackError("Only explicit repository GET endpoints are allowed")
        return urllib.request.Request("https://api.github.com"+path,
            headers={"Authorization":"Bearer "+self.token,
                     "Accept":"application/vnd.github+json",
                     "X-GitHub-Api-Version":"2022-11-28",
                     "Accept-Encoding":"identity",
                     "User-Agent":"visible-larger-request163-readonly"})
    def metadata(self, path):
        with self.opener.open(self.request(path), timeout=120) as response:
            raw = response.read(4000001)
            if len(raw) > 4000000:
                raise ReadbackError("A GitHub metadata response exceeds its declared scope")
        return json.loads(raw, object_pairs_hook=unique)
    def source(self, row, commit, checks):
        path = row["path"]
        if path.startswith("/") or ".." in path.split("/"):
            raise ReadbackError("Only explicit repository source paths")
        data = self.metadata("/repos/"+REPOSITORY+"/contents/"+
            urllib.parse.quote(path, safe="/")+"?ref="+commit)
        if data.get("type") != "file" or data.get("encoding") != "base64":
            raise ReadbackError("Expected original small source file metadata")
        raw = base64.b64decode(data["content"], validate=False)
        checks.bytes("original frozen source "+path, raw, row)
        return dict(path=path, git_blob=data["sha"], **identity(raw),
                    source_commit=commit, source_not_imported=True)
    def download_job_log_once(self, job_id, path, maximum):
        """Official302 only; no token follows the signed redirect."""
        endpoint="/repos/"+REPOSITORY+"/actions/jobs/"+str(job_id)+"/logs"
        response = None
        redirected = False
        try:
            response = self.opener.open(self.request(endpoint), timeout=120)
        except urllib.error.HTTPError as error:
            if error.code not in (301,302,303,307,308):
                raise
            location = error.headers.get("Location")
            error.close()
            if not location:
                raise ReadbackError("Official job-log redirect has no Location")
            parsed = urllib.parse.urlsplit(location)
            if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
                raise ReadbackError("Official log redirect is not an absolute HTTPS target")
            # This new request carries no Authorization/Cookie. URL/query are
            # deliberately never printed or included in any metadata receipt.
            response = urllib.request.urlopen(urllib.request.Request(location,
                headers={"Accept-Encoding":"identity","User-Agent":"visible-larger-request163-readonly"}),
                timeout=120)
            redirected = True
        h=hashlib.sha256()
        size=0
        try:
            with Path(path).open("xb") as out:
                while True:
                    block=response.read(1048576)
                    if not block:
                        break
                    size += len(block)
                    if size > maximum:
                        raise ReadbackError("Declared original-log byte resource limit exceeded")
                    out.write(block)
                    h.update(block)
                out.flush()
                os.fsync(out.fileno())
        finally:
            if response is not None:
                response.close()
        return dict(bytes=size, sha256=h.hexdigest(), official_job_id=job_id,
                    official_REST_endpoint="/actions/jobs/{job_id}/logs",
                    official_redirect_followed=redirected,
                    authorization_forwarded_to_redirect=False,
                    signed_URL_or_token_printed=False,
                    log_download_count=1)


class NormalizedLines:
    def __init__(self, path):
        self.path=Path(path)
        self.lines=0
        self.prefixes=0
        self.exceptional=[]
        self.normalized=hashlib.sha256()
    def __iter__(self):
        with self.path.open("rb") as stream:
            for raw in stream:
                self.lines += 1
                if raw.endswith(b"\n"):
                    raw=raw[:-1]
                    if raw.endswith(b"\r"):
                        raw=raw[:-1]
                text=raw.decode("utf-8","strict")
                removed=[]
                while True:
                    match=PREFIX.match(text)
                    if not match:
                        break
                    removed.append(match.group(0))
                    text=text[len(match.group(0)):]
                self.prefixes += len(removed)
                if len(removed)>1 or any(x.startswith("\ufeff") for x in removed):
                    self.exceptional.append(dict(line=self.lines,prefixes=removed))
                self.normalized.update((text+"\n").encode("utf-8"))
                yield self.lines,text
    def receipt(self):
        return dict(lines=self.lines,timestamp_prefix_count=self.prefixes,
                    exceptional_transport_prefixes=self.exceptional,
                    normalized_LF_sha256=self.normalized.hexdigest(),
                    only_anchored_GitHub_prefixes_removed=True,
                    science_JSON_words_not_normalized=True,
                    original_log_bytes_separately_hashed=True)


def json_line(line):
    if not line.startswith("{"):
        return None
    try:
        value=decode(line)
    except (ValueError,ReadbackError):
        return None
    return value if isinstance(value,dict) else None


def omitted_descriptor(value, reason):
    raw=canonical(value)
    return dict(**identity(raw), scope=reason,
                original_JSON_type="list" if isinstance(value,list) else type(value).__name__,
                original_list_length=len(value) if isinstance(value,list) else None,
                values_recomputed=False, values_all_printed_or_independently_read_by_root=False)


def source_binding(api, lane, checks):
    run=api.metadata("/repos/"+REPOSITORY+"/actions/runs/"+str(lane["run_id"]))
    job=api.metadata("/repos/"+REPOSITORY+"/actions/jobs/"+str(lane["compute_job_id"]))
    report=api.metadata("/repos/"+REPOSITORY+"/actions/jobs/"+str(lane["original_report_job_id"]))
    checks.equal("official run id",run["id"],lane["run_id"])
    checks.equal("official source commit",run["head_sha"],lane["source_commit"])
    checks.equal("official original attempt",run["run_attempt"],lane["run_attempt"])
    checks.equal("official run completed",run["status"],"completed")
    checks.equal("official compute id",job["id"],lane["compute_job_id"])
    checks.equal("official compute run",job["run_id"],lane["run_id"])
    checks.equal("official compute head",job["head_sha"],lane["source_commit"])
    checks.equal("official compute completed",job["status"],"completed")
    checks.equal("official original job conclusion",job["conclusion"],lane["compute_conclusion"])
    checks.equal("official original report id",report["id"],lane["original_report_job_id"])
    checks.equal("official original report run",report["run_id"],lane["run_id"])
    checks.equal("official original report head",report["head_sha"],lane["source_commit"])
    checks.equal("official original report completed",report["status"],"completed")
    checks.equal("official original report conclusion",report["conclusion"],lane["original_report_conclusion"])
    source_rows=[api.source(row,lane["source_commit"],checks) for row in lane["protocol_sources"]]
    return dict(run={key:run.get(key) for key in
                     ("id","head_sha","run_attempt","status","conclusion","path","html_url")},
                compute={key:job.get(key) for key in
                     ("id","run_id","head_sha","name","status","conclusion","started_at","completed_at")},
                original_report={key:report.get(key) for key in
                     ("id","run_id","head_sha","name","status","conclusion")},
                original_report_log_not_downloaded_again=True,
                protocol_sources=source_rows,
                original_science_not_rerun=True)


class ByteLedger:
    def __init__(self):
        self.count=0
        self.size=0
        self.h=hashlib.sha256()
    def add(self, value):
        raw=canonical(value, True)
        self.h.update(raw)
        self.count += 1
        self.size += len(raw)
    def receipt(self):
        return dict(records=self.count,bytes=self.size,sha256=self.h.hexdigest())


class Read151:
    def __init__(self, lane, checks):
        self.lane,self.checks=lane,checks
        self.active={}
        self.groups={}
        self.nodes={}
        self.cover=set()
        self.coarse=[]
        self.final_ids=[]
        self.final_meta={}
        self.pending_ids=[]
        self.atomic_count=0
        self.unvisited=[]
        self.interrupted=[]
        self.events={}
        self.ledgers={k:ByteLedger() for k in ("evaluated_nodes","current_cover",
            "complete_frontier","complete_cover_transactions")}
        self.frame=None
        self.summaries=[]
    @staticmethod
    def interval(row):
        return {k:row[k] for k in ("numeric_piece","closed_public_u","depth")}
    def accept_group(self, label, raw, descriptor):
        value=decode(raw.decode("ascii"))
        self.checks.equal("151 group canonical with original LF "+label,
                          canonical(value,True).decode("ascii"),raw.decode("ascii"))
        if label in self.lane["original_groups"]:
            wanted=self.lane["original_groups"][label]
            self.checks.bytes("151 actual original "+label,raw,wanted)
            self.checks.equal("151 actual segment count "+label,
                integer(descriptor["segments"]),wanted["segments"])
            if label in self.groups:
                self.checks.equal("151 repeated group identity "+label,
                                  self.groups[label]["identity"],identity(raw))
            else:
                self.groups[label]=dict(value=value,identity=identity(raw),
                    original_segments=integer(descriptor["segments"]))
                if label!="complete-original-Q-node-outward-conversions":
                    stream_text("151-"+label,raw.decode("ascii"),
                        "Complete original151 ASCII JSON with its original final LF",
                        identity(raw))
        elif isinstance(value,dict) and isinstance(value.get("event"),str):
            # emit() in the original consumer structurally segments a large
            # event; process that same complete event, never count its parts
            # as independent scientific node records.
            self.event(value,from_segment=True)
    def event(self, value, from_segment=False):
        name=value.get("event")
        if not isinstance(name,str):
            return
        self.events[name]=self.events.get(name,0)+1
        if name=="request151_complete_metadata_begin":
            label=value["label"]
            if label in self.active:
                raise ReadbackError("151 overlapping metadata group: "+label)
            self.active[label]=dict(descriptor=value,parts=[])
        elif name=="request151_complete_metadata_segment":
            label=value["label"]
            if label not in self.active:
                raise ReadbackError("151 part without original begin: "+label)
            state=self.active[label]
            self.checks.equal("151 original segment order "+label,
                              integer(value["index"]),len(state["parts"]))
            self.checks.equal("151 original segment total "+label,
                              integer(value["segments"]),integer(state["descriptor"]["segments"]))
            text=value["data"]
            if not isinstance(text,str) or not text.isascii():
                raise ReadbackError("151 complete metadata is not its declared ASCII text")
            state["parts"].append(text)
            if len(state["parts"])==integer(state["descriptor"]["segments"]):
                raw="".join(state["parts"]).encode("ascii")
                self.checks.bytes("151 original group "+label,raw,state["descriptor"])
                del self.active[label]
                self.accept_group(label,raw,state["descriptor"])
        elif name=="request151_actual_node_enclosure":
            row=value["record"];node=integer(row["node_id"])
            self.checks.equal("151 sequential original node id",node,len(self.nodes))
            interval=self.interval(row)
            self.nodes[node]=dict(interval=interval,hash=sha(canonical(row)),
                                  original_keys=set(row))
            self.ledgers["evaluated_nodes"].add(row)
            if row["phase_when_evaluated"]=="coarse":
                self.checks.equal("151 coarse piece order",integer(row["numeric_piece"]),len(self.coarse))
                self.coarse.append(interval)
                self.cover.add(node)
                self.ledgers["complete_cover_transactions"].add(dict(
                    kind="coarse-commit",node_id=row["node_id"],interval=interval))
        elif name=="request151_complete_cover_atomic_split":
            parent=integer(value["parent_node_id"])
            children=[integer(x) for x in value["child_node_ids"]]
            self.checks.equal("151 complete atomic child count",len(children),2)
            if parent not in self.cover or any(x not in self.nodes or x in self.cover for x in children):
                raise ReadbackError("151 original atomic cover ownership differs")
            p=self.nodes[parent]["interval"]
            a,b=[self.nodes[x]["interval"] for x in children]
            self.checks.equal("151 child0 piece",a["numeric_piece"],p["numeric_piece"])
            self.checks.equal("151 child1 piece",b["numeric_piece"],p["numeric_piece"])
            self.checks.equal("151 literal left endpoint",a["closed_public_u"][0],p["closed_public_u"][0])
            self.checks.equal("151 literal shared child endpoint",a["closed_public_u"][1],b["closed_public_u"][0])
            self.checks.equal("151 literal right endpoint",b["closed_public_u"][1],p["closed_public_u"][1])
            self.checks.equal("151 child0 depth",integer(a["depth"]),integer(p["depth"])+1)
            self.checks.equal("151 child1 depth",integer(b["depth"]),integer(p["depth"])+1)
            self.checks.equal("151 original union flag",value["exact_children_union_is_parent"],True)
            self.ledgers["complete_cover_transactions"].add(dict(kind="split-begin",
                parent_node_id=value["parent_node_id"],parent_interval=p,child_intervals=[a,b]))
            self.ledgers["complete_cover_transactions"].add(dict(kind="split-commit",
                parent_node_id=value["parent_node_id"],child_node_ids=value["child_node_ids"]))
            self.cover.remove(parent)
            self.cover.update(children)
            self.atomic_count += 1
        elif name=="request151_final_complete_cover_leaf":
            row=value["record"];node=integer(row["node_id"])
            if node not in self.cover or node in self.final_meta:
                raise ReadbackError("151 final cover repeats or changes an original live node")
            original={k:v for k,v in row.items() if k not in
                      ("currently_queued_for_refinement","closed_cover_member_retained_at_stop")}
            if "terminal_reason" in original and "terminal_reason" not in self.nodes[node]["original_keys"]:
                self.checks.equal("151 only original max-depth annotation",original.pop("terminal_reason"),
                    "maximum-depth-with-honest-unresolved-enclosure")
            self.checks.equal("151 complete final enclosure body",sha(canonical(original)),
                              self.nodes[node]["hash"])
            self.checks.equal("151 original final cover retained flag",
                              row["closed_cover_member_retained_at_stop"],True)
            self.ledgers["current_cover"].add(row)
            self.final_ids.append(node)
            self.final_meta[node]=dict(hash=sha(canonical(row)),
                interval=self.interval(row),
                flags={k:row[k] for k in ("accurate_radius_strictly_positive",
                    "accurate_abs_as_strictly_below_one","accurate_domain_proved",
                    "accurate_domain_rigorously_refuted","relative_target_work_goal_met",
                    "currently_queued_for_refinement")})
        elif name=="request151_full_pending_or_refuted_interval":
            row=value["record"];node=integer(row["node_id"])
            if node not in self.final_meta or node in self.pending_ids:
                raise ReadbackError("151 original pending node is missing or duplicated")
            self.checks.equal("151 pending exact retained enclosure",sha(canonical(
                row["retained_complete_enclosure"])),self.final_meta[node]["hash"])
            self.pending_ids.append(node)
            self.ledgers["complete_frontier"].add(row)
        elif name=="request151_full_unvisited_coarse_interval":
            row=value["record"];self.unvisited.append(row)
            self.ledgers["complete_frontier"].add(row)
        elif name=="request151_full_interrupted_transaction":
            row=value["record"];self.interrupted.append(row)
            self.ledgers["complete_frontier"].add(dict(interrupted_transaction=row))
    def line(self, text):
        begin="BEGIN_REQUEST151_COMMON_U_TARGET_SUMMARY"
        end="END_REQUEST151_COMMON_U_TARGET_SUMMARY"
        if text==begin:
            if self.frame is not None:
                raise ReadbackError("151 overlapping original summary")
            self.frame=[]
            return
        if text==end:
            if self.frame is None:
                raise ReadbackError("151 summary end without begin")
            raw=("\n".join(self.frame)+"\n").encode("ascii")
            self.checks.bytes("151 original primary summary",raw,self.lane["original_summary"])
            value=decode(raw.decode("ascii"))
            self.checks.equal("151 summary source",value["source_commit"],self.lane["source_commit"])
            self.checks.equal("151 summary run",value["run_id"],str(self.lane["run_id"]))
            self.summaries.append(dict(identity=identity(raw),value=value))
            self.frame=None
            return
        if self.frame is not None:
            self.frame.append(text)
            return
        value=json_line(text)
        if value is not None:
            self.event(value)
    def finish(self):
        if self.active or self.frame is not None:
            raise ReadbackError("151 original text has an incomplete metadata suffix")
        self.checks.equal("151 expected complete metadata labels",sorted(self.groups),
                          sorted(self.lane["original_groups"]))
        result=self.groups["complete-target-result"]["value"]
        self.checks.equal("151 actual result source",result["source_commit"],self.lane["source_commit"])
        self.checks.equal("151 actual result run",result["run_id"],str(self.lane["run_id"]))
        self.checks.equal("151 actual original source hash",result["source"]["sha256"],
                          self.lane["protocol_sources"][0]["sha256"])
        self.checks.equal("151 original interrupted state",result["interrupted_transaction"],None)
        self.checks.equal("151 original unvisited count",len(self.unvisited),
                          integer(result["complete_unvisited_coarse_count"]))
        self.checks.equal("151 complete evaluated record count",len(self.nodes),
                          integer(result["completed_node_records"]))
        self.checks.equal("151 initial coarse record count",len(self.coarse),
                          integer(result["initial_numeric_pieces"]))
        self.checks.equal("151 complete final live set",sorted(self.cover),sorted(self.final_ids))
        self.checks.equal("151 complete pending record count",len(self.pending_ids)+len(self.unvisited),
                          integer(result["complete_pending_or_refuted_rows"]))
        self.checks.equal("151 actual completed transaction scope",len(self.interrupted),0)
        for key,ledger in self.ledgers.items():
            actual=ledger.receipt()
            expected=result["raw_files"][key]
            self.checks.equal("151 exact original ledger bytes "+key,actual["bytes"],integer(expected["bytes"]))
            self.checks.equal("151 exact original ledger SHA "+key,actual["sha256"],expected["sha256"])
        plan=dict(schema="request151-common-u-complete-nine-target-enclosures-v1-complete-public-query-plan",
            run_id=str(self.lane["run_id"]),source_commit=self.lane["source_commit"],
            closed_public_domain=["0","1"],both_numeric_seam_sides_retained=True,
            original_closed_numeric_pieces=self.coarse)
        self.checks.bytes("151 exact original complete query plan",canonical(plan,True),
                          result["raw_files"]["original_query_plan"])
        self.checks.bytes("151 exact original input binding",canonical(
            self.groups["complete-input-and-rebuilt-definition-binding"]["value"],True),
            result["input_binding"])
        self.checks.bytes("151 exact original grid identity",canonical(
            self.groups["complete-original-Q-node-outward-conversions"]["value"],True),
            result["exact_Q_grid_binding"])
        pieces=[[] for _ in self.coarse]
        flags=dict(leaves=len(self.final_ids),radius_proved=0,speed_proved=0,
            domain_proved=0,rigorously_refuted=0,relative_goal_met=0,unresolved=0)
        queued=0
        previous_piece=-1
        for node in self.final_ids:
            row=self.final_meta[node];p=integer(row["interval"]["numeric_piece"])
            if p<previous_piece or p>=len(pieces):
                raise ReadbackError("151 original final piece order differs")
            previous_piece=p
            pieces[p].append(row["interval"])
            f=row["flags"]
            for dest,src in (("radius_proved","accurate_radius_strictly_positive"),
                ("speed_proved","accurate_abs_as_strictly_below_one"),
                ("domain_proved","accurate_domain_proved"),
                ("rigorously_refuted","accurate_domain_rigorously_refuted"),
                ("relative_goal_met","relative_target_work_goal_met")):
                flags[dest]+=int(f[src] is True)
            if not(f["accurate_domain_proved"] is True and f["relative_target_work_goal_met"] is True):
                flags["unresolved"]+=int(f["accurate_domain_rigorously_refuted"] is not True)
            queued+=int(f["currently_queued_for_refinement"] is True)
        piece_receipts=[]
        for index,items in enumerate(pieces):
            if not items:
                raise ReadbackError("151 a declared complete piece has no original cover members")
            self.checks.equal("151 piece original left",items[0]["closed_public_u"][0],
                              self.coarse[index]["closed_public_u"][0])
            self.checks.equal("151 piece original right",items[-1]["closed_public_u"][1],
                              self.coarse[index]["closed_public_u"][1])
            for a,b in zip(items[:-1],items[1:]):
                self.checks.equal("151 exact adjacent endpoint strings",
                                  a["closed_public_u"][1],b["closed_public_u"][0])
            piece_receipts.append(dict(numeric_piece=index,current_leaf_count=len(items),
                original_closed_public_u=self.coarse[index]["closed_public_u"],
                literal_endpoint_chain_verified=True,
                no_rational_or_interval_quantity_recomputed=True))
        self.checks.equal("151 count original saved Boolean predicates",flags,result["current_cover_counts"])
        self.checks.equal("151 count original queue flags",queued,integer(result["current_refinement_queue_count"]))
        self.checks.equal("151 piece record count",len(piece_receipts),len(result["complete_numeric_piece_cover_records"]))
        for actual,original in zip(piece_receipts,result["complete_numeric_piece_cover_records"]):
            for key in ("numeric_piece","current_leaf_count","original_closed_public_u"):
                self.checks.equal("151 original per-piece saved metadata "+key,actual[key],original[key])
        if not self.summaries:
            raise ReadbackError("151 no complete original bounded summary frame")
        return dict(original_result=self.groups["complete-target-result"]["identity"],
            original_input=self.groups["complete-input-and-rebuilt-definition-binding"]["identity"],
            original_grid=self.groups["complete-original-Q-node-outward-conversions"]["identity"],
            original_grid_list_length=len(self.groups["complete-original-Q-node-outward-conversions"]["value"]),
            complete_original_summaries=self.summaries,
            evaluated_records=len(self.nodes),final_cover_records=len(self.final_ids),
            pending_records=len(self.pending_ids),completed_atomic_splits=self.atomic_count,
            original_ledger_reconstruction={k:v.receipt() for k,v in self.ledgers.items()},
            query_plan_identity=identity(canonical(plan,True)),
            original_flag_counts=flags,queue_count=queued,
            complete_piece_string_coverage=piece_receipts,
            all_node_enclosures_recomputed=False,
            exact_predicate_proofs_repeated=False,
            all_original_node_values_printed_to_new_log=False,
            root_has_independently_read_every_node_value=False,
            scope="All original node/cover/frontier bytes counted and hashed; source-defined transactions and literal endpoint chains checked; no new Q/interval arithmetic")


UNSET=object()


class StringParts:
    def __init__(self, count, expected):
        self.characters=[UNSET]*count
        self.expected=expected


class TreeBuilder:
    def __init__(self, label, checks):
        self.label,self.checks=label,checks
        self.root=UNSET
        self.declared={}
    @staticmethod
    def path(raw):
        return [integer(x) if isinstance(x,RawNumber) else x for x in raw]
    def get(self,path):
        value=self.root
        for key in path:
            if value is UNSET:
                raise ReadbackError("Original structural ancestor is unavailable")
            value=value[key]
        return value
    def put(self,path,value):
        if not path:
            if self.root is not UNSET:
                raise ReadbackError("Duplicate original structural root")
            self.root=value
            return
        parent=self.get(path[:-1]);key=path[-1]
        if isinstance(parent,list):
            if type(key) is not int or key<0 or key>=len(parent) or parent[key] is not UNSET:
                raise ReadbackError("Overlapping original list structural interval")
        elif isinstance(parent,dict):
            if not isinstance(key,str) or key in parent:
                raise ReadbackError("Duplicate original object structural field")
        else:
            raise ReadbackError("Original structural parent is not a container")
        parent[key]=value
    def apply(self,part):
        path=self.path(part["path"]);op=part["operation"]
        if op=="value":
            self.put(path,part["value"])
        elif op=="begin_object":
            self.put(path,{})
            self.declared[tuple(path)]=("object",integer(part["entry_count"]))
        elif op=="begin_list":
            count=integer(part["length"])
            self.put(path,[UNSET]*count)
            self.declared[tuple(path)]=("list",count)
        elif op=="begin_string":
            self.put(path,StringParts(integer(part["codepoint_length"]),
                dict(bytes=part["utf8_bytes"],sha256=part["utf8_sha256"])))
        elif op=="list_items":
            start,stop=integer(part["start"]),integer(part["stop"])
            self.checks.equal("157 exact original list interval",len(part["items"]),stop-start)
            if not isinstance(self.get(path),list):
                raise ReadbackError("Original list interval has no container")
            for j,value in enumerate(part["items"]):
                self.put(path+[start+j],value)
        elif op=="string_slice":
            value=self.get(path)
            start,stop=integer(part["start"]),integer(part["stop"])
            if not isinstance(value,StringParts) or start<0 or stop>len(value.characters):
                raise ReadbackError("Original string interval has no container")
            chars=list(part["text"])
            self.checks.equal("157 exact original codepoint interval",len(chars),stop-start)
            for j,char in enumerate(chars):
                if value.characters[start+j] is not UNSET:
                    raise ReadbackError("Overlapping original string interval")
                value.characters[start+j]=char
        else:
            raise ReadbackError("Unknown original structural operation: "+str(op))
    def finish(self):
        def visit(value,path):
            if value is UNSET:
                raise ReadbackError("Original structural value is missing: "+str(path))
            if isinstance(value,StringParts):
                if any(x is UNSET for x in value.characters):
                    raise ReadbackError("Original string suffix is missing")
                text="".join(value.characters)
                self.checks.bytes("157 complete original string",text.encode("utf-8"),value.expected)
                return text
            if isinstance(value,list):
                return [visit(x,path+[i]) for i,x in enumerate(value)]
            if isinstance(value,dict):
                expected=self.declared.get(tuple(path))
                if expected is not None:
                    self.checks.equal("157 original declared object entries",len(value),expected[1])
                return {key:visit(item,path+[key]) for key,item in value.items()}
            return value
        return visit(self.root,[])


class Read157:
    PRIMARY="original-nine-control-decimal50-residual-quadratic-segmented-complete-readback-v1"
    PART="original-nine-control-decimal50-residual-quadratic-complete-scalar-segment-v1"
    def __init__(self,lane,checks):
        self.lane,self.checks=lane,checks
        self.capture=None
        self.pending_part=None
        self.pending_primary=None
        self.pending_chain=None
        self.stdout=None
        self.stdout_identity=None
        self.stdout_verified=False
        self.primary=None
        self.groups={}
        self.chains=[]
        self.byte_logs={}
        self.byte_current=None
        self.extra_events=[]
    def event(self,value):
        name=value.get("event")
        if name=="visible-nine-decimal50-curvature-scalar-segment-sha256":
            if self.pending_part is None:
                raise ReadbackError("157 descriptor without its original part")
            frame=self.pending_part
            part=frame["value"];desc=value["part"]
            self.checks.equal("157 segment group id",part["group_id"],value["group_id"])
            self.checks.equal("157 segment begin",frame["begin"],desc["begin"])
            self.checks.equal("157 segment end",frame["end"],desc["end"])
            self.checks.bytes("157 complete original segment",frame["raw"],desc)
            self.checks.equal("157 canonical original segment",canonical(part).decode("ascii"),
                              frame["raw"].decode("ascii"))
            self.checks.equal("157 segment schema",part["schema"],self.PART)
            for key in ("part_index","operation","path","start","stop","length",
                        "entry_count","codepoint_length"):
                if key in desc:
                    self.checks.equal("157 original segment descriptor "+key,part[key],desc[key])
            self.checks.equal("157 actual segment run",part["run_id"],str(self.lane["run_id"]))
            self.checks.equal("157 actual segment source",part["source_commit"],self.lane["source_commit"])
            self.checks.equal("157 actual original reader",part["reader_source_sha256"],
                              self.lane["reader_source_sha256"])
            self.checks.equal("157 original status descriptor",part["original_status"],
                              self.lane["original_status"])
            group=part["group_id"]
            if group not in self.groups:
                self.groups[group]=dict(builder=TreeBuilder(group,self.checks),descriptors=[])
            row=self.groups[group]
            self.checks.equal("157 complete original part order",integer(part["part_index"]),
                              len(row["descriptors"]))
            if len(frame["raw"])>90000:
                raise ReadbackError("157 original segment exceeds its own declared bound")
            row["builder"].apply(part)
            row["descriptors"].append(desc)
            self.pending_part=None
        elif name=="visible157-complete-scalar-readout":
            if self.pending_primary is None:
                raise ReadbackError("157 primary descriptor without original frame")
            frame=self.pending_primary
            self.checks.bytes("157 original primary",frame["raw"],value)
            self.checks.bytes("157 original primary compared with report",frame["raw"],
                              self.lane["original_primary"])
            p=frame["value"]
            self.checks.equal("157 canonical original primary",canonical(p).decode("ascii"),
                              frame["raw"].decode("ascii"))
            self.checks.equal("157 original primary schema",p["schema"],self.PRIMARY)
            self.checks.equal("157 primary actual run",p["run_id"],str(self.lane["run_id"]))
            self.checks.equal("157 primary actual source",p["source_commit"],self.lane["source_commit"])
            self.checks.equal("157 primary original status descriptor",p["original_status"],
                              self.lane["original_status"])
            stream_text("157-complete-original-primary",frame["raw"].decode("ascii"),
                "Complete original bounded primary retained before optional complete-view coverage checks",
                identity(frame["raw"]))
            self.primary=p
            self.pending_primary=None
        elif name=="visible157-original-reader-stdout-identity":
            if self.stdout_identity is None:
                raise ReadbackError("157 original reader stdout has no complete frame")
            self.checks.equal("157 complete reader stdout byte count",
                              self.stdout_identity["bytes"],integer(value["stdout"]["bytes"]))
            self.checks.equal("157 complete reader stdout SHA",
                              self.stdout_identity["sha256"],value["stdout"]["sha256"])
            self.stdout_verified=True
        elif name=="visible157-chain-summary-sha256":
            if self.pending_chain is None:
                raise ReadbackError("157 chain identity without original frame")
            frame=self.pending_chain
            self.checks.bytes("157 original chain",frame["raw"],value)
            self.checks.equal("157 original chain run",frame["value"]["run_id"],str(self.lane["run_id"]))
            self.checks.equal("157 original chain source",frame["value"]["source_commit"],self.lane["source_commit"])
            stream_text("157-complete-original-chain-"+str(len(self.chains)),frame["raw"].decode("ascii"),
                "Complete original compute chain JSON; final original identity checked against already read report",
                identity(frame["raw"]))
            self.chains.append(frame)
            self.pending_chain=None
        elif name=="request157-complete-child-log-identity":
            if self.byte_current is not None:
                self.finish_byte_log()
            name=value["file"]
            if name in self.byte_logs:
                raise ReadbackError("157 duplicate original complete child-log declaration")
            self.byte_current=dict(header=value,hash=hashlib.sha256(),size=0,parts=0,
                                   stderr_parts=[] if "stderr" in name else None)
        elif name=="request157-complete-child-log-part":
            state=self.byte_current
            if state is None:
                raise ReadbackError("157 original child-log part has no declaration")
            header=state["header"]
            self.checks.equal("157 child-log exact name",value["file"],header["file"])
            self.checks.equal("157 child-log part order",integer(value["part"]),state["parts"])
            self.checks.equal("157 child-log byte start",integer(value["byte_start"]),state["size"])
            raw=value["utf8_surrogateescape_text"].encode("utf-8","surrogateescape")
            self.checks.bytes("157 original child-log part bytes",raw,value)
            state["hash"].update(raw);state["size"]+=len(raw);state["parts"]+=1
            self.checks.equal("157 child-log byte stop",integer(value["byte_stop"]),state["size"])
            self.checks.equal("157 child-log complete original SHA",value["file_sha256"],header["sha256"])
            if state["stderr_parts"] is not None:
                state["stderr_parts"].append(raw)
        elif isinstance(name,str) and name.startswith(("request157_","request157-","visible157-")):
            # Complete source-generated failure/cleanup/control metadata, not
            # the hundreds of already structurally reconstructed part indexes.
            self.extra_events.append(value)
    def finish_byte_log(self):
        state=self.byte_current
        if state is None:
            return
        header=state["header"]
        self.checks.equal("157 complete child-log parts",state["parts"],integer(header["parts"]))
        self.checks.equal("157 complete child-log bytes",state["size"],integer(header["bytes"]))
        self.checks.equal("157 complete child-log SHA",state["hash"].hexdigest(),header["sha256"])
        self.byte_logs[header["file"]]=dict(bytes=state["size"],sha256=state["hash"].hexdigest(),
                                           parts=state["parts"])
        if state["stderr_parts"] is not None:
            raw=b"".join(state["stderr_parts"])
            # The outer JSON contains an ASCII inner JSON string, so even a
            # lone surrogate never reaches a watcher UTF8 re-encoder.
            stream_value("157-original-"+header["file"],dict(
                original=identity(raw),complete_original_text_json_ascii=
                json.dumps(raw.decode("utf-8","surrogateescape"),ensure_ascii=True),
                reconstruction="json.loads(field).encode('utf-8','surrogateescape')"),
                "Complete original child stderr bytes; no truncation")
        self.byte_current=None
    def line(self,text):
        reader_begin="BEGIN_VISIBLE157_ORIGINAL_READER_STDOUT"
        reader_end="END_VISIBLE157_ORIGINAL_READER_STDOUT"
        if text==reader_begin:
            if self.stdout is not None or self.stdout_identity is not None:
                raise ReadbackError("157 multiple/overlapping original reader sessions")
            self.stdout=dict(hash=hashlib.sha256(),bytes=0)
            return
        if text==reader_end:
            if self.stdout is None:
                raise ReadbackError("157 original reader end without begin")
            self.stdout_identity=dict(bytes=self.stdout["bytes"],sha256=self.stdout["hash"].hexdigest())
            self.stdout=None
            return
        if self.stdout is not None:
            raw=(text+"\n").encode("utf-8")
            self.stdout["hash"].update(raw);self.stdout["bytes"]+=len(raw)
        wanted=(text=="BEGIN_VISIBLE157_PRIMARY" or text=="BEGIN_VISIBLE157_CHAIN_SUMMARY"
                or text.startswith("BEGIN_VISIBLE_NINE_DECIMAL50_CURVATURE_"))
        if wanted:
            if self.capture is not None:
                raise ReadbackError("157 overlapping original JSON frames")
            self.capture=dict(begin=text,end="END_"+text[6:],lines=[])
            return
        if self.capture is not None:
            frame=self.capture
            if text==frame["end"]:
                raw="\n".join(frame.pop("lines")).encode("ascii")
                frame.update(raw=raw,value=decode(raw.decode("ascii")))
                if frame["begin"]=="BEGIN_VISIBLE157_PRIMARY":
                    if self.pending_primary is not None or self.primary is not None:
                        raise ReadbackError("157 duplicate complete primary")
                    self.pending_primary=frame
                elif frame["begin"]=="BEGIN_VISIBLE157_CHAIN_SUMMARY":
                    if self.pending_chain is not None:
                        raise ReadbackError("157 unbound previous chain")
                    self.pending_chain=frame
                else:
                    if self.pending_part is not None:
                        raise ReadbackError("157 previous segment lacks descriptor")
                    self.pending_part=frame
                self.capture=None
            else:
                frame["lines"].append(text)
            return
        value=json_line(text)
        if value is not None:
            self.event(value)
    def finish(self):
        self.finish_byte_log()
        if any(x is not None for x in (self.capture,self.pending_part,self.pending_primary,
                                      self.pending_chain,self.stdout)):
            raise ReadbackError("157 incomplete original transport suffix")
        if self.primary is None or not self.stdout_verified or not self.chains:
            raise ReadbackError("157 no complete original primary/stdout/chain")
        primary=self.primary;meta=primary["segmented_readout"]
        declared=meta["outer_direction_groups"]+[row["group"] for row in meta["moved_primary_fields"]]
        self.checks.equal("157 complete group ID set",sorted(self.groups),
                          sorted(row["group_id"] for row in declared))
        restored={}
        group_rows=[]
        segment_count=0
        for desc in declared:
            group=desc["group_id"];row=self.groups[group]
            self.checks.equal("157 original group part count",len(row["descriptors"]),integer(desc["part_count"]))
            self.checks.bytes("157 original complete group part index",canonical(row["descriptors"]),
                dict(bytes=desc["segment_index"]["canonical_json_bytes"],
                     sha256=desc["segment_index"]["canonical_json_sha256"]))
            value=row["builder"].finish()
            raw=canonical(value)
            self.checks.bytes("157 entire original group",raw,
                dict(bytes=desc["canonical_value_bytes"],sha256=desc["canonical_value_sha256"]))
            restored[group]=value
            group_rows.append(dict(group_id=group,**identity(raw),part_count=len(row["descriptors"]),
                                   original_scope=desc["scope"]))
            segment_count+=len(row["descriptors"])
        self.checks.equal("157 all declared original groups",len(restored),integer(meta["emitted_group_count"]))
        self.checks.equal("157 all declared original segments",segment_count,integer(meta["emitted_segment_count"]))
        view={key:value for key,value in primary.items() if key!="segmented_readout"}
        view["schema"]=meta["original_view"]["schema"]
        view["outer_searches"]=[]
        for i,desc in enumerate(meta["outer_direction_groups"]):
            self.checks.equal("157 original outer order",integer(desc["scope"]["original_outer_index"]),i)
            view["outer_searches"].append(restored[desc["group_id"]])
        for moved in meta["moved_primary_fields"]:
            field=moved["original_field"]
            if field in view:
                raise ReadbackError("157 moved original field already exists")
            view[field]=restored[moved["group"]["group_id"]]
        self.checks.equal("157 full original direction count",len(view["outer_searches"]),
                          integer(meta["original_outer_direction_count"]))
        raw=canonical(view)
        self.checks.bytes("157 original complete scalar view",raw,
            dict(bytes=meta["original_view"]["canonical_json_bytes"],
                 sha256=meta["original_view"]["canonical_json_sha256"]))
        view_identity=identity(raw)
        del raw
        self.checks.equal("157 actual consumed source closure",view["consumed_source_sha256"],
                          self.lane["expected_consumed_source_sha256"])
        self.checks.equal("157 actual four original input identities",view["input_sha256"],
                          self.lane["expected_input_sha256"])
        self.checks.bytes("157 original final chain compared with report",self.chains[-1]["raw"],
                          self.lane["original_chain"])
        source_comparison=compare_literal_binding(self.lane["reference_actual154_literal_binding"],
                                                 view["literal_model_binding"])
        semantic=emit157_semantics(view,self.checks)
        stream_value("157-complete-transport-source-and-literal-comparison",dict(
            groups=group_rows,complete_scalar_view=view_identity,
            original_status=primary["original_status"],reader_stdout=self.stdout_identity,
            original_group_count=len(group_rows),original_segment_count=segment_count,
            original_moved_fields=[x["original_field"] for x in meta["moved_primary_fields"]],
            original_child_error_bytes=self.byte_logs,
            actual154_recorded_literal_comparison=source_comparison,
            original_control_failure_and_cleanup_events=self.extra_events,
            raw_status_file_not_downloaded_or_independently_rehashed=True,
            complete_view_fields_reconstructed_from_original_log=True,
            all_internal_model_cell_values_recomputed=False,
            root_has_independently_read_all_internal_model_cells=False),
            "Original transport and field-selection metadata only")
        return dict(complete_primary=identity(canonical(primary)),complete_scalar_view=view_identity,
            original_status=primary["original_status"],original_chain=identity(self.chains[-1]["raw"]),
            original_chain_fields=self.chains[-1]["value"],semantic_scope=semantic,
            complete_groups=len(group_rows),complete_segments=segment_count,
            original_child_error_bytes=self.byte_logs,
            actual154_recorded_literal_comparison=source_comparison,
            complete_view_reconstructed=True,
            full_internal_model_values_printed=False,
            full_internal_model_values_independently_read_by_root=False)


def compare_literal_binding(old,current):
    arrays=[]
    for key in sorted(set(old["arrays"])|set(current["arrays"])):
        before=old["arrays"].get(key);after=current["arrays"].get(key)
        arrays.append(dict(name=key,actual154=before,actual157=after,
                           exact_recorded_descriptors_equal=canonical(before)==canonical(after)))
    fields={}
    for key in ("cut_scale_exact_binary64_lift","height_sign_exact_binary64_lift",
                "decimal_digits","rounding","parameter_dimension","original_mesh_nodes",
                "field_and_tail_modes","original_three_frequencies","exactly_diagonal_as_original_record"):
        fields[key]=dict(actual154=old.get(key),actual157=current.get(key),
                         exact_recorded_words_equal=canonical(old.get(key))==canonical(current.get(key)))
    return dict(recorded_arrays=arrays,recorded_scalar_fields=fields,
        actual154_binding_sha256=old["canonical_binding_sha256"],
        actual157_binding_sha256=current["canonical_binding_sha256"],
        actual157_original149_binding_sha256=current.get("original149_literal_model_binding_sha256"),
        array_payloads_not_downloaded_or_recomputed=True,
        metadata_comparison_not_a_new_scientific_gate=True)


def emit157_semantics(view, checks):
    """Original fields, never a new optimization or numerical comparison.

    Complete outer physical trials (including their original normal records)
    and complete initial/final diagnostics are emitted. Internal polynomial
    tables are covered by original identities and integer record accounting;
    their millions of scalar cells are not silently advertised as read.
    """
    top_rows=[]
    for key in sorted(view):
        if key=="outer_searches":
            continue
        rec=stream_value("157-original-top-"+key,view[key],
            "Complete original complete-view field; no scientific recalculation")
        top_rows.append(dict(field=key,bytes=rec["bytes"],sha256=rec["sha256"]))
    directions=[]
    all_trials=0
    all_internal_rows=0
    all_eligible_rows=0
    for outer_index,row in enumerate(view["outer_searches"]):
        checks.equal("157 original physical direction order",integer(row["iteration"]),outer_index)
        model=row["direction_model"]
        updates=model.get("model_updates",[])
        base={key:value for key,value in row.items() if key not in ("trials","direction_model")}
        base["direction_model"]={key:value for key,value in model.items() if key!="model_updates"}
        base["direction_model"]["internal_model_updates_readback_scope"]=dict(
            original=omitted_descriptor(updates,
                "Complete table reconstructed and hashed; selected terminal fields and all coverage below"),
            original_table_not_fully_printed=True,
            root_not_claimed_to_have_read_every_internal_model_cell=True)
        stream_value("157-outer-"+str(outer_index)+"-complete-model-and-path-terminal",base,
            "All original outer fields except actual trials emitted separately and the explicitly scoped internal update table")
        coverage=[]
        observed_global_index=0
        internal_rows=0
        chosen_row=None
        reference=model.get("selected_model_reference")
        heavy=("candidate_pool","shift_trials","complete_spectral_guidance",
               "complete_residual_GN_preconditioner","complete_three_by_nine_model_J",
               "complete_nine_model_gradient","complete_nine_by_nine_model_Hessian")
        candidate_columns=[
            "index","label","complete","eligible_direction","reason",
            "original_model_trial_budget","actual_recorded_model_trials",
            "unvisited_model_trial_indices","accepted_model_trial",
            "original_candidate_canonical_bytes","original_candidate_canonical_SHA256",
            "eligible_original_flags","inner_accept_original_flags",
            "complete_original_exception_rows"]
        for ui,update in enumerate(updates):
            checks.equal("157 model update order",integer(update["index"]),ui)
            summary={key:value for key,value in update.items() if key not in heavy}
            summary["original_update_identity"]=identity(canonical(update))
            summary["large_internal_fields"]={
                key:omitted_descriptor(update[key],
                    "Complete original internal field reconstructed/hash covered; not all values printed")
                for key in heavy if key in update and key!="candidate_pool"}
            candidates=[]
            pool=update.get("candidate_pool",[])
            for ci,candidate in enumerate(pool):
                checks.equal("157 model candidate order",integer(candidate["index"]),ci)
                trials=candidate.get("trials",[])
                exceptions=[]
                eligible=0
                inner_accepted=0
                for ti,trial in enumerate(trials):
                    checks.equal("157 original model trial width",len(trial),
                                  len(model["model_trial_columns"]))
                    checks.equal("157 original model trial order",integer(trial[0]),ti)
                    if trial[9] is True:
                        checks.equal("157 original eligible global index",
                                      integer(trial[10]),observed_global_index)
                        observed_global_index+=1
                        eligible+=1
                    elif trial[10] is not None:
                        raise ReadbackError("157 noneligible original trial carries a global index")
                    if trial[11] is True:
                        inner_accepted+=1
                    if trial[12] is not None:
                        exceptions.append(trial)
                    if reference is not None and (
                        ui==integer(reference["update"]) and
                        ci==integer(reference["candidate"]) and
                        ti==integer(reference["trial"])):
                        if chosen_row is not None:
                            raise ReadbackError("157 duplicate selected original model row")
                        chosen_row=trial
                if candidate.get("accepted_model_trial") is not None:
                    ti=integer(candidate["accepted_model_trial"])
                    if ti<0 or ti>=len(trials):
                        raise ReadbackError("157 internal accepted model trial is outside the recorded list")
                    checks.equal("157 recorded inner acceptance flag",trials[ti][11],True)
                raw=canonical(candidate)
                candidates.append([
                    candidate["index"],candidate["label"],candidate.get("complete"),
                    candidate.get("eligible_direction"),candidate.get("reason"),
                    candidate.get("original_model_trial_budget"),len(trials),
                    candidate.get("unvisited_model_trial_indices"),
                    candidate.get("accepted_model_trial"),
                    len(raw),sha(raw),eligible,inner_accepted,exceptions])
                internal_rows+=len(trials)
            selected_candidate=update.get("selected_candidate")
            if selected_candidate is not None:
                ci=integer(selected_candidate);ti=integer(update["selected_model_trial"])
                if ci<0 or ci>=len(pool) or ti<0 or ti>=len(pool[ci]["trials"]):
                    raise ReadbackError("157 update-selected model row is absent")
                selected=pool[ci]["trials"][ti]
                checks.equal("157 selected update point words",update["selected_relative_point"],selected[2])
                checks.equal("157 selected update merit words",update["selected_model_merit"],selected[4])
                checks.equal("157 update selected original inner flag",selected[11],True)
                summary["complete_original_update_selected_model_trial"]=selected
            summary["candidate_coverage_columns"]=candidate_columns
            summary["all_recorded_candidate_coverage_rows"]=candidates
            summary["original_candidate_pool_identity"]=identity(canonical(pool))
            summary["no_model_merit_recomputed_or_ordered_by_reader"]=True
            coverage.append(summary)
        checks.equal("157 stored eligible model pool count",
                      observed_global_index,integer(model.get("global_model_candidate_count",0)))
        if reference is not None:
            if chosen_row is None:
                raise ReadbackError("157 model-selected original row was not found")
            checks.equal("157 model winner original flag",chosen_row[9],True)
            checks.equal("157 model winner global index",chosen_row[10],model["selected_global_candidate"])
            checks.equal("157 model winner point words",chosen_row[2],model["actual_relative_direction"])
            checks.equal("157 model winner merit words",chosen_row[4],model["selected_model_merit"])
            checks.equal("157 model winner residual words",chosen_row[3],model["selected_full_three_model_residual"])
            stream_value("157-outer-"+str(outer_index)+"-complete-original-selected-model-row",
                dict(original_model_trial_columns=model["model_trial_columns"],
                     selected_reference=reference,complete_original_trial=chosen_row),
                "Exact original stored row cross-reference; no minimum or polynomial recomputed")
        for ui,summary in enumerate(coverage):
            stream_value("157-outer-"+str(outer_index)+"-model-update-"+str(ui)+"-coverage",summary,
                "All recorded update/candidate coverage; selected original points and exceptions complete; large internal tables only identified")
        if updates:
            terminal=updates[-1]
            complete_terminal={key:value for key,value in terminal.items()
                               if key not in ("candidate_pool","shift_trials")}
            complete_terminal["candidate_pool_original_identity"]=omitted_descriptor(
                terminal.get("candidate_pool",[]),
                "All candidate counts/flags/exception rows above; full huge tables not repeated")
            complete_terminal["shift_trials_original_identity"]=omitted_descriptor(
                terminal.get("shift_trials",[]),
                "Original complete shift records are reconstructed/hash covered; original terminal shift fields retained")
            stream_value("157-outer-"+str(outer_index)+"-complete-original-last-model-update-terminal",
                complete_terminal,
                "Complete terminal model J/gradient/Hessian/GN/spectral/shift fields except explicitly scoped candidate and shift histories")
        trials=row.get("trials",[])
        for ti,trial in enumerate(trials):
            checks.equal("157 physical trial global order",integer(trial["trial_index"]),ti)
            stream_value("157-outer-"+str(outer_index)+"-complete-physical-trial-"+str(ti),trial,
                "Complete original actual physical trial and complete original normal-correction record; original gates unchanged")
        original_counts={}
        for label,declared in row.get("path_status",{}).items():
            actual=sum(trial.get("path")==label for trial in trials)
            if "trial_count" in declared:
                checks.equal("157 original path physical-trial count",
                              actual,integer(declared["trial_count"]))
            original_counts[label]=dict(recorded_actual_trials=actual,original_path_status=declared)
        direction=dict(index=outer_index,original_outer_identity=identity(canonical(row)),
            actual_physical_trials=len(trials),actual_paths=original_counts,
            original_model_updates=len(updates),recorded_internal_model_trial_rows=internal_rows,
            original_eligible_pool_flag_count=observed_global_index,
            original_finite_points_reported=model.get("complete_finite_model_points_evaluated"),
            finite_points_not_numerically_retested=True,
            original_model_update_unvisited_suffix=model.get("unvisited_model_update_indices"),
            original_accepted=row.get("accepted"),original_radius_update=row.get("radius_update"),
            complete_physical_trials_printed=True,complete_model_terminal_printed=True,
            all_internal_model_cell_values_printed=False,
            no_claim_of_global_optimality_or_rank_certificate=True)
        directions.append(direction)
        all_trials+=len(trials)
        all_internal_rows+=internal_rows
        all_eligible_rows+=observed_global_index
    return dict(top_fields=top_rows,directions=directions,
        total_original_physical_trials=all_trials,
        total_recorded_internal_model_trial_rows=all_internal_rows,
        total_original_eligible_pool_flags=all_eligible_rows,
        complete_initial_final_FD_fields_printed=True,
        original_model_and_original_actual_merit_never_recomputed=True,
        large_internal_records_identity_covered_not_independently_numerically_audited=True)



def redact_transport_text(text, token):
    if token:
        text=text.replace(token,"[REDACTED_ACTIONS_READ_TOKEN]")
    # HTTP failures may contain the temporary official redirect URL. Preserve
    # path/error class but never its query credential or a Bearer value.
    text=re.sub(r"(https?://[^\s?#'\"]+)\?[^\s'\"<>]*",
                r"\1?[REDACTED_QUERY]",text)
    text=re.sub(r"(?i)(authorization\s*[:=]\s*bearer\s+)\S+",
                r"\1[REDACTED]",text)
    return text


def final_summary(value):
    raw=canonical(value)
    if len(raw)>LIMIT:
        stream_value("complete-final-metadata-over-bound",value,
            "Complete original readback metadata; the bounded report index overflowed, so completion is not claimed")
        value=dict(schema=SCHEMA,request_number=163,lane=value.get("lane"),
            source_commit=value.get("source_commit"),run_id=value.get("run_id"),
            complete=False,reader_exit_code=70,
            reason="final metadata index exceeds90000 bytes",
            complete_over_bound_index_identity=identity(raw),
            original_readback_scope=value.get("original_readback_scope"),
            output_semantic_group_count=len(OUTPUTS),
            scientific_computation_performed=False)
        raw=canonical(value)
    print("BEGIN_REQUEST163_READBACK_INDEX",flush=True)
    print(raw.decode("ascii"),flush=True)
    print("END_REQUEST163_READBACK_INDEX",flush=True)
    emit(dict(event="readback163-index-identity",**identity(raw)))
    path=os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path,"a",encoding="ascii",newline="\n") as stream:
            stream.write("summary="+raw.decode("ascii")+"\n")
            stream.write("summary_bytes="+str(len(raw))+"\n")
            stream.write("summary_sha256="+sha(raw)+"\n")
    return integer(value.get("reader_exit_code",70))


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",required=True,type=Path)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--lane",choices=("151","157"),required=True)
    parser.add_argument("--out",required=True,type=Path)
    args=parser.parse_args(argv)
    started=time.monotonic()
    stage="Actions environment"
    token=os.environ.get("GH_TOKEN","")
    out=None
    log=None
    reader=None
    checks=Checks()
    summary=dict(schema=SCHEMA,request_number=163,lane=args.lane,
        run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
        complete=False,reader_exit_code=70,stage=stage,
        original_readback_scope="Only stored text/bytes/JSON/integer record metadata; no model execution",
        scientific_computation_performed=False,
        original_science_rerun=False,old_acceptance_or_domain_gates_changed=False,
        raw_log_or_recomputable_data_uploaded=False,
        new_artifact_Release_or_Git_data_created=False)
    try:
        if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
            raise ReadbackError("This original-log reader runs only in the named repository Actions")
        stage="bind request and this reader"
        raw=args.request.read_bytes()
        if sha(raw)!=args.request_sha256:
            raise ReadbackError("Request file bytes do not match the explicit workflow pin")
        request=json.loads(raw,object_pairs_hook=unique)
        if request.get("schema")!="existing151157-original-log-readback-request-v1":
            raise ReadbackError("Unexpected original-log request schema")
        if request.get("repository")!=REPOSITORY or request.get("request_number")!=163:
            raise ReadbackError("Original-log request owner differs")
        checks.bytes("this independent metadata reader",Path(__file__).read_bytes(),request["reader"])
        summary["request"]=identity(raw)
        summary["reader"]=file_identity(__file__)
        lane=request["lanes"][args.lane]
        summary["original_source"]=dict(run_id=lane["run_id"],source_commit=lane["source_commit"],
            compute_job_id=lane["compute_job_id"],compute_conclusion=lane["compute_conclusion"])
        temp=Path(os.environ["RUNNER_TEMP"]).resolve()
        expected_name="visible-existing151157-"+args.lane+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ.get("GITHUB_RUN_ATTEMPT","1")
        candidate=args.out.resolve()
        if candidate.parent!=temp or candidate.name!=expected_name or candidate.exists():
            raise ReadbackError("Output must be this request's fresh direct RUNNER_TEMP child")
        candidate.mkdir(mode=0o700)
        out=candidate
        log=out/"original-compute.log"
        stage="official original run/job and frozen protocol source binding"
        api=GitHub(token)
        summary["official_original_binding"]=source_binding(api,lane,checks)
        stream_value("official-original-run-job-and-protocol-source-binding",
            summary["official_original_binding"],
            "Official read-only metadata and exact original small source hashes; no source imported")
        stage="single official original compute log download"
        summary["original_log"]=api.download_job_log_once(lane["compute_job_id"],log,
                                                         lane["maximum_log_bytes"])
        emit(dict(event="readback163-original-log-downloaded",
                  lane=args.lane,original_log=summary["original_log"]))
        stage="strict original text and structural JSON reconstruction"
        reader=Read151(lane,checks) if args.lane=="151" else Read157(lane,checks)
        normalized=NormalizedLines(log)
        for line_number,text in normalized:
            reader.line(text)
            if line_number%25000==0:
                emit(dict(event="readback163-original-lines-processed",lane=args.lane,
                    complete_original_lines=line_number,scientific_work_performed=False))
        summary["transport_normalization"]=normalized.receipt()
        stage="complete original protocol/field selection"
        result=reader.finish()
        stream_value("complete-original-reconstruction-scope-and-coverage",result,
            "Complete metadata receipt; original scientific results are never numerically recomputed")
        result_identity=identity(canonical(result))
        if args.lane=="151":
            short={key:result[key] for key in (
                "original_result","original_input","original_grid","original_grid_list_length",
                "evaluated_records","final_cover_records","pending_records","completed_atomic_splits",
                "original_ledger_reconstruction","query_plan_identity","original_flag_counts","queue_count",
                "all_node_enclosures_recomputed","exact_predicate_proofs_repeated",
                "all_original_node_values_printed_to_new_log",
                "root_has_independently_read_every_node_value","scope")}
            short["complete_original_summaries"]=result["complete_original_summaries"]
            short["complete_numeric_piece_coverage_identity"]=identity(canonical(result["complete_piece_string_coverage"]))
            short["complete_numeric_piece_count"]=len(result["complete_piece_string_coverage"])
        else:
            short={key:result[key] for key in (
                "complete_primary","complete_scalar_view","original_status","original_chain",
                "complete_groups","complete_segments","original_child_error_bytes",
                "actual154_recorded_literal_comparison","complete_view_reconstructed",
                "full_internal_model_values_printed","full_internal_model_values_independently_read_by_root")}
            short["original_final_chain_fields"]=result["original_chain_fields"]
            short["physical_trial_count"]=result["semantic_scope"]["total_original_physical_trials"]
            short["internal_model_trial_rows"]=result["semantic_scope"]["total_recorded_internal_model_trial_rows"]
            short["eligible_original_pool_flags"]=result["semantic_scope"]["total_original_eligible_pool_flags"]
            short["original_direction_coverage"]=result["semantic_scope"]["directions"]
        summary.update(complete=True,reader_exit_code=0,original_receipt=short,
            complete_reconstruction_receipt_identity=result_identity,
            checks=checks.summary(),exception=None)
        stage="completed original metadata readback"
    except Exception as error:
        message=redact_transport_text(repr(error),token)
        trace=redact_transport_text(traceback.format_exc(),token)
        stream_value("complete-readback-error",dict(stage=stage,error=message,
            complete_traceback=trace,
            original_scientific_result_not_reinterpreted_as_reader_failure=True),
            "Complete metadata/transport error text with only credentials and signed URL queries redacted")
        summary.update(complete=False,reader_exit_code=70,exception=message,
            failed_stage=stage,completed_comparisons=checks.count,
            completed_check_rows_sha256=checks.h.hexdigest())
    finally:
        # No source/data inputs are under out. The only removable directory
        # was created by this invocation with an exact fixed direct-child name.
        cleanup=dict(attempted=out is not None,owned_fresh_directory_only=True,
                     completed=False,exception=None)
        if out is not None:
            try:
                import shutil
                files=[]
                for path in sorted(out.iterdir()):
                    if path.is_symlink() or not path.is_file():
                        raise ReadbackError("Unexpected non-regular object in the owned log directory")
                    files.append(dict(name=path.name,**file_identity(path)))
                cleanup["original_owned_file_identities"]=files
                shutil.rmtree(out)
                cleanup["completed"]=True
            except Exception as error:
                cleanup["exception"]=redact_transport_text(repr(error),token)
                stream_value("complete-owned-cleanup-error",dict(
                    complete_traceback=redact_transport_text(traceback.format_exc(),token),
                    original_readback_complete_before_cleanup=summary["complete"]),
                    "Owned temporary cleanup error; never a scientific failure")
                summary.update(complete=False,reader_exit_code=70)
        summary["owned_cleanup"]=cleanup
        summary["stage"]=stage
        summary["elapsed_wall_seconds"]=format(time.monotonic()-started,".9f")
        summary["semantic_output_group_count"]=len(OUTPUTS)
        summary["complete_semantic_output_index_identity"]=identity(canonical(OUTPUTS))
        stream_value("complete-semantic-output-index",list(OUTPUTS),
            "Every selected semantic group name/byte count/SHA; no payload omitted by an output size cap")
    return final_summary(summary)


if __name__=="__main__":
    raise SystemExit(main())
