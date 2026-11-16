#!/usr/bin/env python3
"""Read one completed true57/full168 joint research stdout, without scientific imports.

The workflow itself may still be running its report job.  The selected research
job must be completed, with any conclusion.  One raw log is read into memory,
at most224MiB.  Bounded selections, literal JSON+LF identities and declared
omissions are printed; no original cache/log is written or uploaded anywhere.
No NumPy, geometry, derivative, optimizer, or developer module is imported.
"""
from __future__ import annotations
import time
STARTED = time.monotonic()
import argparse
from collections import Counter
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import read_original_actions_log as reader

REPOSITORY = "Rogerhu12/math-research-public"
POLICY = "true57-full168-nonlinear-metric-curvature-finite-candidates-v1"
PREFIX = "TRUE57_NONLINEAR168_"
REPORT_TAG = PREFIX+"READ_ONLY_REPORT"
SCHEMA = POLICY+"-readonly-original-stdout-report-v1"
LOG_CAP = 224*1024*1024
REPORT_CAP = 8*1024*1024
SHA40 = re.compile(r"^[0-9a-f]{40}$")
TAGGED = re.compile(r"^"+re.escape(PREFIX)+r"([A-Z][A-Z0-9_]*)[ \t]+(.*)$")
UNIQUE = {"REQUEST", "PUBLIC_PULL", "PRIVATE_PULL", "COMPLETE", "FINAL_CLOCK"}
HISTORY_KEYS = {"iterations", "systems", "system_records", "iteration_history",
                "newton_system_records"}
DUPLICATE_CONTAINER_KEYS = {
    "real_finite_results_including_each_raw170_dual_slack_residual",
    "finite_results", "attempted_problems", "problems",
    "finite_result_original_stdout_receipts",
}
PULL_TAGS = {"PUBLIC_PULL", "PRIVATE_PULL"}
ERROR_TAG_WORDS = ("ERROR", "FAILURE", "EXCEPTION", "STOP")
NATIVE_VALUE_TAGS = {"FINITE_RESULT", "ACTUAL_TRIAL", "FULL_GRID_SCAN",
                     "ATTAINER_GRADIENT", "LINE_QUERY", "SCALAR_RESULT",
                     "LINE_RESULT", "DIRECTION", "ACTUAL_RESULT"}
KNOWN = PULL_TAGS | NATIVE_VALUE_TAGS | {
    "REQUEST", "PRIOR_WORK_REUSED", "INPUT", "BASE_VALUES", "JET_INPUT",
    "MODEL", "CACHE", "COMPLETE", "FINAL_CLOCK", "OUTPUT_METADATA",
    "REPORTING_ERROR", "TRANSFER_ERROR", "MODEL_ERROR", "ACTUAL_ERROR", "PREDICTION_PARTIAL"}

def require(condition, message):
    reader.require(condition, message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))

def pointer(path):
    return "/" + "/".join(str(v).replace("~", "~0").replace("/", "~1") for v in path) if path else ""

def node_identity(value):
    # Administrative serialization only; not a literal source substring and
    # never a computed norm, gate, convergence measure or numerical summary.
    result = dict(reader.fingerprint(value))
    result["fingerprint_scope"] = "canonical original JSON node, no trailing LF; not literal raw bytes"
    result["json_type"] = (
        "object" if isinstance(value, dict) else "array" if isinstance(value, list)
        else "string" if isinstance(value, str) else "scalar")
    if isinstance(value, (dict, list, str)):
        result["length"] = len(value)
    return result

def retained_exact_vector(value):
    # Required raw170, delta168, q168, exact physical172 and retained
    # source159/physical163 vectors are never length-filtered.
    return (isinstance(value, list) and len(value) in (9, 11, 159, 163, 168, 170, 172)
            and all(scalar(item) for item in value))

def error_or_stop(value):
    if not isinstance(value, dict):
        return False
    if any(value.get(key) is not None for key in (
            "stop", "terminal", "error", "exception", "failure",
            "recovery_failure", "candidate_diagnostic_error")):
        return True
    status = str(value.get("status", "")).lower()
    return any(word in status for word in ("fail", "error", "stop", "limit", "raise"))

class View:
    """Select original data, preserving actual vectors and all scalar verdicts."""
    def __init__(self, *, level=0, tag=""):
        self.level, self.tag = level, tag
        self.omissions = []
        self.history_selections = []
    def omit(self, value, path, reason, *, metadata=None):
        record = {"json_pointer": pointer(path), "reason": reason,
                  "original_stdout_remains_authoritative": True}
        if metadata is None:
            record.update(node_identity(value))
        else:
            record["original_array_metadata"] = copy.deepcopy(metadata)
        self.omissions.append(record)
        return {"not_forwarded": record}
    def history(self, value, path):
        if not isinstance(value, list) or len(value) <= 4:
            return [self.project(item, path+(i,)) for i, item in enumerate(value)]
        keep = {0, len(value)-1}
        if self.level == 0:
            keep.update((1, len(value)-2))
        keep.update(i for i, item in enumerate(value) if error_or_stop(item))
        indices = sorted(keep)
        omitted = len(value)-len(indices)
        record = {"original_count": len(value), "selected_original_indices": indices,
                  "omitted_original_count": omitted, **node_identity(value),
                  "selection": "first/last and every item carrying a stop/error; no numerical recomputation"}
        self.history_selections.append({"json_pointer": pointer(path), **record})
        return {"original_history_identity": record,
                "selected_original_items": [
                    {"original_index": i, "value": self.project(value[i], path+(i,))}
                    for i in indices]}
    def project(self, value, path=()):
        key = str(path[-1]) if path else ""
        if scalar(value):
            if isinstance(value, str) and len(value) > 16000:
                return self.omit(value, path, "oversized original string")
            return value
        if isinstance(value, dict):
            # Array payloads supply their own original dtype/shape/hash.  Avoid
            # repeatedly hashing a many-megabyte coefficient cache.
            if "values" in value and isinstance(value["values"], list) and (
                    "array_sha256" in value or "shape" in value or "dtype" in value):
                raw = value["values"]
                if retained_exact_vector(raw):
                    return {k: self.project(v, path+(k,)) for k, v in value.items()}
                result = {k: self.project(v, path+(k,))
                          for k, v in value.items() if k != "values"}
                meta = {k: copy.deepcopy(value[k]) for k in (
                    "shape", "dtype", "array_sha256", "sha256", "encoding") if k in value}
                result["values"] = self.omit(
                    raw, path+("values",), "original dense array values", metadata=meta)
                return result
            if self.level >= 2 and self.tag == "COMPLETE" and key in DUPLICATE_CONTAINER_KEYS:
                return self.omit(value, path, "repeated finite-result container; native records are selected separately")
            return {k: self.project(v, path+(k,)) for k, v in value.items()}
        if isinstance(value, list):
            if retained_exact_vector(value):
                return copy.deepcopy(value)
            if key in HISTORY_KEYS:
                return self.history(value, path)
            if self.level >= 2 and self.tag == "COMPLETE" and key in DUPLICATE_CONTAINER_KEYS:
                return self.omit(value, path, "repeated finite-result list; native records are selected separately")
            if all(scalar(v) for v in value):
                if len(value) <= (256 if self.level == 0 else 192):
                    return copy.deepcopy(value)
                return self.omit(value, path, "large original scalar/dual/slack/row array")
            # Dense matrices/tensors are metadata even when only two outer
            # grid slices are present.  Lists of semantic dictionaries remain.
            if any(isinstance(v, list) for v in value):
                return self.omit(value, path, "original nested numeric array")
            if len(value) > (2048 if self.level == 0 else 512):
                chosen = [i for i, item in enumerate(value) if error_or_stop(item)]
                chosen = sorted(set([0, len(value)-1]+chosen))
                return {
                    "original_array_identity": node_identity(value),
                    "semantic_list_truncated": True,
                    "original_count": len(value),
                    "selected_original_indices": chosen,
                    "selected_original_items": [
                        {"original_index": i, "value": self.project(value[i], path+(i,))}
                        for i in chosen],
                    "omitted_original_count": len(value)-len(chosen)}
            return [self.project(v, path+(i,)) for i, v in enumerate(value)]
        return self.omit(value, path, "unrecognized parsed JSON node")

def normalize(line):
    value = reader.ANSI.sub("", line.lstrip("\ufeff"))
    match = reader.TIME_PREFIX.match(value)
    return (match.group(1), match.group(2).lstrip("\ufeff")) if match else (None, value)

def parse_records(raw):
    text = raw.decode("utf-8")
    records, errors, tail = [], [], []
    for number, line in enumerate(text.splitlines(), 1):
        timestamp, line = normalize(line)
        match = TAGGED.match(line)
        if match is None:
            if any(word in line for word in ("Traceback", "Error:", "Exception:",
                                              "File \"", "exited with code", "##[error]")):
                tail.append({"line_number": number, "timestamp": timestamp,
                             "original_text_prefix": line[:1800],
                             "original_text_was_truncated": len(line) > 1800})
                tail = tail[-24:]
            continue
        tag, json_text = match.group(1), match.group(2)
        data = json_text.encode("utf-8")
        identity = {
            "sequence": len(records)+len(errors)+1, "line_number": number,
            "timestamp": timestamp, "tag": tag,
            "full_tag": PREFIX+tag,
            "JSON_bytes": len(data), "JSON_sha256": sha(data),
            "JSON_plus_LF_bytes": len(data)+1,
            "JSON_plus_LF_sha256": sha(data+b"\n")}
        try:
            obj = reader.decode_json(data)
            require(isinstance(obj, dict), "tagged source record must be a JSON object")
            records.append({**identity, "data": obj})
        except Exception as error:
            errors.append({**identity, "parse_error": {
                "type": type(error).__name__, "message": str(error)[:800]},
                "unparsed_source_not_treated_as_empty_success": True})
    counts = dict(Counter(row["tag"] for row in records))
    info = {
        "decoded_UTF8_once": True, "line_count": len(text.splitlines()),
        "decoded_record_count": len(records), "unparsed_record_count": len(errors),
        "tag_counts": counts,
        "unknown_uppercase_suffixes_retained": sorted(set(counts)-KNOWN),
        "duplicate_unique_tags": {tag: counts[tag] for tag in UNIQUE if counts.get(tag, 0) > 1},
        "bounded_non_record_failure_tail": tail}
    return records, errors, info

def identity(record):
    return {key: value for key, value in record.items() if key != "data"}

def source_checks(records, run_id, commit):
    checks = []
    for row in records:
        if row["tag"] not in ("REQUEST", "COMPLETE", "FINAL_CLOCK"):
            continue
        obj = row["data"]
        for key, expected in (("github_sha", commit), ("github_run_id", str(run_id))):
            if key in obj:
                checks.append({"record_sequence": row["sequence"], "field": key,
                               "observed": obj[key], "expected": expected,
                               "matches": str(obj[key]) == str(expected)})
        if row["tag"] == "REQUEST" and "source_commit" in obj:
            checks.append({"record_sequence": row["sequence"], "field": "source_commit",
                           "observed": obj["source_commit"], "expected": commit,
                           "matches": obj["source_commit"] == commit})
        if "policy" in obj:
            checks.append({"record_sequence": row["sequence"], "field": "policy",
                           "observed": obj["policy"], "expected": POLICY,
                           "matches": obj["policy"] == POLICY})
    return checks

def actual_receipt_comparisons(records):
    """Compare only explicitly paired literal hash/length fields; no math gates."""
    by_suffix = {}
    for row in records:
        by_suffix.setdefault(row["tag"], []).append(row)
    comparisons = []
    for row in records:
        stack = [(row["data"], ())]
        while stack:
            obj, path = stack.pop()
            if isinstance(obj, dict):
                raw_sha = obj.get("JSON_plus_LF_sha256")
                raw_bytes = obj.get("JSON_plus_LF_bytes")
                if isinstance(raw_sha, str) and isinstance(raw_bytes, int):
                    matches = [v for v in records
                               if v["JSON_plus_LF_sha256"] == raw_sha
                               and v["JSON_plus_LF_bytes"] == raw_bytes]
                    # A receipt can name an ancestor, so absence here is
                    # informational rather than a false current-source failure.
                    comparisons.append({
                        "in_record_sequence": row["sequence"],
                        "json_pointer": pointer(path),
                        "original_JSON_plus_LF_sha256": raw_sha,
                        "original_JSON_plus_LF_bytes": raw_bytes,
                        "matching_current_record_sequences": [v["sequence"] for v in matches],
                        "may_reference_an_ancestor_record": not bool(matches)})
                for key, value in obj.items():
                    if isinstance(value, dict):
                        stack.append((value, path+(key,)))
                    elif isinstance(value, list) and value and isinstance(value[0], dict):
                        stack.extend((v, path+(key, i)) for i, v in enumerate(value)
                                     if isinstance(v, dict))
    return comparisons

def selected_record(record, level):
    tag, data = record["tag"], record["data"]
    result = {"identity": identity(record)}
    if tag in PULL_TAGS:
        result["original_semantics"] = copy.deepcopy(data)
        result["public_or_private_actual_pull_preserved_without_field_filter"] = True
        return result
    view = View(level=level, tag=tag)
    result["original_semantics"] = view.project(data)
    result["selection_scope"] = {
        "original_numbers_not_recomputed": True,
        "actual_small_vectors_preserved_when_present": True,
        "large_arrays_or_histories_not_reconstructible_from_this_report": True,
        "native_record_JSON_plus_LF_identity_is_authoritative": True,
        "omitted_nodes": len(view.omissions),
        "selected_histories": view.history_selections}
    if tag in ("MODEL", "CACHE"):
        result["arrays_remain_in_original_research_stdout"] = True
        result["not_a_replacement_input_cache"] = True
    return result

def make_report(base, records, errors, parse_info, *, level):
    report = copy.deepcopy(base)
    report["projection_level"] = level
    report["parse"] = copy.deepcopy(parse_info)
    report["parse_errors"] = copy.deepcopy(errors)
    report["record_fingerprints"] = [identity(row) for row in records]
    report["records"] = [selected_record(row, level) for row in records]
    present = {row["tag"] for row in records}
    complete = "COMPLETE" in present
    clock = "FINAL_CLOCK" in present
    duplicates = parse_info["duplicate_unique_tags"]
    mismatch = any(not row["matches"] for row in report.get("producer_identity_checks", []))
    declared_budget_stops = []
    for row in records:
        if row["tag"] != "FINAL_CLOCK":
            continue
        # Only explicit NEW final-clock booleans.  Do not compare numeric
        # counts/limits or reinterpret any ancestor's exhausted old scope.
        for name, obj in (("FINAL_CLOCK", row["data"]),
                          ("FINAL_CLOCK.ledger", row["data"].get("ledger", {}))):
            if not isinstance(obj, dict):
                continue
            for key in ("deadline_observed_exceeded", "scope_exhausted",
                        "scientific_scope_exhausted", "scientific_budget_exhausted"):
                if obj.get(key) is True:
                    declared_budget_stops.append({
                        "record_sequence": row["sequence"],
                        "original_field": name+"."+key, "original_value": True})
    report["original_final_clock_declared_budget_stops"] = declared_budget_stops
    report["completion_record_present"] = complete
    report["authoritative_final_clock_present"] = clock
    report["scientific_success_not_inferred_from_job_conclusion_or_report_success"] = True
    report["final_clock_is_not_replaced_by_earlier_COMPLETE_clock"] = True
    report["literal_receipt_comparisons"] = actual_receipt_comparisons(records)
    report["status"] = ("original-output-incomplete-or-inconsistent" if
                        errors or duplicates or mismatch or not complete or not clock or declared_budget_stops
                        else "original-output-selected")
    report["semantic_read_is_incomplete"] = bool(
        errors or duplicates or mismatch or not complete or not clock or declared_budget_stops)
    return report

def fetch_one_log(api, job_id):
    url = reader.API+"/repos/"+REPOSITORY+"/actions/jobs/"+str(job_id)+"/logs"
    data, location = api.get(url, LOG_CAP, api_auth=True)
    redirects = 0
    while location is not None:
        redirects += 1
        require(redirects <= 4, "too many original-log redirects")
        data, location = api.get(location, LOG_CAP, api_auth=False)
    require(data is not None, "empty original log body")
    return data, redirects

def output_path(value):
    if value is None:
        return None
    root = os.environ.get("RUNNER_TEMP")
    require(bool(root), "--out requires RUNNER_TEMP")
    root = Path(root).resolve()
    given = Path(value)
    target = (given if given.is_absolute() else root/given).resolve()
    require(target != root and root in target.parents,
            "--out must remain below RUNNER_TEMP")
    require(not target.exists() or target.is_file(), "--out must be a file")
    return target

def own_sources():
    result = {}
    for label, name in (("observer", __file__), ("stdlib_reader", reader.__file__)):
        path = Path(name)
        data = path.read_bytes()
        result[label] = {"filename": path.name, "bytes": len(data), "sha256": sha(data)}
    return result

def emit(report, path):
    report["observer_seconds_separate_from_all_scientific_ledgers"] = time.monotonic()-STARTED
    data = reader.encoded(report)
    require(len(data)+len(REPORT_TAG)+2 <= REPORT_CAP,
            "bounded semantic stdout limit would be exceeded")
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data+b"\n")
    sys.stdout.buffer.write(REPORT_TAG.encode("ascii")+b" "+data+b"\n")
    sys.stdout.buffer.flush()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--job-id", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--out")
    args = parser.parse_args()
    records, errors, parse_info = [], [], {}
    report = {
        "schema": SCHEMA, "policy": POLICY, "status": "observer-started",
        "original_job_log_request_chains": 0, "original_job_log_reads_completed": 0,
        "raw_log_limit_bytes": LOG_CAP, "semantic_stdout_limit_bytes": REPORT_CAP,
        "scientific_imports": 0, "scientific_recomputations": 0,
        "scientific_or_development_calls": 0,
        "raw_log_or_payload_written_to_artifact_git_or_disk": False,
        "large_arrays_omitted_only_with_original_metadata_or_node_fingerprint": True,
        "research_conclusion_does_not_replace_original_outcome": True,
        "observer_source_commit": os.environ.get("GITHUB_SHA"),
        "observer_run_id": os.environ.get("GITHUB_RUN_ID")}
    path = None
    try:
        require(args.run_id.isdigit() and int(args.run_id) > 0, "invalid --run-id")
        require(args.job_id.isdigit() and int(args.job_id) > 0, "invalid --job-id")
        require(SHA40.fullmatch(args.source_commit), "invalid --source-commit")
        require(args.workflow.startswith(".github/workflows/")
                and args.workflow.endswith((".yml", ".yaml"))
                and ".." not in Path(args.workflow).parts and "@" not in args.workflow,
                "invalid exact repository-relative workflow")
        path = output_path(args.out)
        report["observer_sources"] = own_sources()
        api = reader.GitHubReader(REPOSITORY)
        run = api.api_json("/actions/runs/"+args.run_id)
        job = api.api_json("/actions/jobs/"+args.job_id)
        require(str(run.get("id")) == args.run_id and run.get("head_sha") == args.source_commit,
                "original run/source identity differs")
        require(str(run.get("path", "")).split("@", 1)[0] == args.workflow,
                "original workflow path differs")
        require(str(job.get("id")) == args.job_id and str(job.get("run_id")) == args.run_id
                and job.get("head_sha") == args.source_commit,
                "original research job/source identity differs")
        require(job.get("status") == "completed",
                "research job must be completed; no live polling or speculative result")
        report["source"] = {
            "repository": REPOSITORY, "run_id": args.run_id, "job_id": args.job_id,
            "source_commit": args.source_commit, "workflow": args.workflow,
            "run_url": run.get("html_url"), "job_url": job.get("html_url"),
            "research_status": job.get("status"), "research_conclusion": job.get("conclusion"),
            "research_started_at": job.get("started_at"), "research_completed_at": job.get("completed_at"),
            "observed_workflow_status": run.get("status"),
            "observed_workflow_conclusion": run.get("conclusion"),
            "workflow_may_still_be_running_this_report_job": True}
        report["original_job_log_request_chains"] = 1
        raw, redirects = fetch_one_log(api, args.job_id)
        report["original_job_log_reads_completed"] = 1
        report["source"].update(raw_log_bytes=len(raw), raw_log_sha256=sha(raw),
                                unauthenticated_redirect_count=redirects,
                                original_bytes_including_BOM_hashed=True)
        records, errors, parse_info = parse_records(raw)
        report["producer_identity_checks"] = source_checks(
            records, args.run_id, args.source_commit)
        require(bool(records) or bool(errors),
                "no TRUE57_NONLINEAR168 uppercase source record was found")
        selected = None
        for level in (0, 1, 2):
            candidate = make_report(report, records, errors, parse_info, level=level)
            if len(reader.encoded(candidate)) <= REPORT_CAP-65536:
                selected = candidate
                break
        if selected is None:
            # Last-resort semantic selection still gives every real raw170,
            # trial168/172, FINAL_CLOCK and both actual pulls.  Omitted detail
            # is identified; it cannot turn a missing outcome into success.
            selected = make_report(report, records, errors, parse_info, level=2)
            selected["status"] = "semantic-size-limited-incomplete"
            selected["semantic_read_is_incomplete"] = True
            selected["records"] = [
                selected_record(row, 2) if row["tag"] in
                (PULL_TAGS | NATIVE_VALUE_TAGS | {"FINAL_CLOCK", "COMPLETE"})
                or any(w in row["tag"] for w in ERROR_TAG_WORDS) else {
                    "identity": identity(row),
                    "source_record_metadata": node_identity(row["data"]),
                    "detail_remains_in_original_stdout": True}
                for row in records]
            selected.pop("literal_receipt_comparisons", None)
        if len(reader.encoded(selected)) > REPORT_CAP-65536:
            selected["records"] = [
                selected_record(row, 2) if row["tag"] in
                (PULL_TAGS | {"FINAL_CLOCK", "ACTUAL_TRIAL", "FINITE_RESULT"})
                else {
                    "identity": identity(row),
                    "original_scalar_fields": {k: v for k, v in row["data"].items() if scalar(v)},
                    "omitted_record_metadata": node_identity(row["data"])}
                for row in records]
            selected["status"] = "semantic-size-limited-incomplete"
            selected["semantic_read_is_incomplete"] = True
            selected["complete_semantics_not_available_in_this_report"] = True
        report = selected
        emit(report, path)
        return 1 if report["semantic_read_is_incomplete"] else 0
    except Exception as error:
        # Essential metadata survives, including paid outcomes already parsed.
        # No network retry, solver, alternate data endpoint or traceback occurs.
        failed = {
            **report, "status": "readonly-observer-incomplete",
            "semantic_read_is_incomplete": True,
            "observer_error": {"type": type(error).__name__, "message": str(error)[:1200]},
            "record_fingerprints": [identity(row) for row in records],
            "parse_errors": errors}
        failed["records"] = [
            selected_record(row, 2) if row["tag"] in
            (PULL_TAGS | {"FINAL_CLOCK", "COMPLETE", "ACTUAL_TRIAL", "FINITE_RESULT"})
            else {"identity": identity(row), "metadata": node_identity(row["data"])}
            for row in records]
        if len(reader.encoded(failed)) > REPORT_CAP-65536:
            # The actual full source remains at its pinned raw identity.
            failed = {
                "schema": SCHEMA, "policy": POLICY,
                "status": "readonly-observer-incomplete",
                "semantic_read_is_incomplete": True,
                "observer_error": failed["observer_error"],
                "source": copy.deepcopy(report.get("source")),
                "scientific_recomputations": 0,
                "records": [
                    selected_record(row, 2) for row in records
                    if row["tag"] in PULL_TAGS | {"FINAL_CLOCK"}],
                "omitted_complete_record_manifest": node_identity(
                    [identity(row) for row in records]),
                "original_decisions_not_replaced_or_guessed": True}
        # An optional output-path failure is not retried.  The readback failure
        # and any authoritative final clock still reach normal stdout.
        emit(failed, None)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
