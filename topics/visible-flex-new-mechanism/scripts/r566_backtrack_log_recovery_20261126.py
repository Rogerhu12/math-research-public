#!/usr/bin/env python3
"""Recover one completed B030 job as metadata; no scientific code is imported.

The original log is streamed exactly once, hashed and parsed in memory. Only
the compact complete-parse receipt and the last exact complete state are
printed. No raw file, artifact, release, Git write, or physical evaluation.
"""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REPOSITORY = "Rogerhu12/math-research-public"
RUN = 45851261982
JOB = 140017925998
COMMIT = "d99eef5312b0c49d78431cc9596f4d48fbc4baa8"
SCHEMA = "r566-working-backtrack-terminal-log-recovery-v1"
LINE = re.compile(r"^(?P<time>\S+Z) (?P<tag>[A-Z][A-Z0-9_]+) (?P<body>[\[{].*)$")
SNAPSHOT_TAGS = {"WORKING_ROWS_COMPLETE_CHECKPOINT", "WORKING_ROWS_OUTER_COMPLETE",
                 "WORKING_ROWS_FINAL"}

def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)

def emit(tag, value):
    print(tag+" "+compact(value), flush=True)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def reject_constant(value):
    raise ValueError("nonfinite JSON constant "+value)

def load_json(text):
    return json.loads(text, parse_constant=reject_constant)

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None

def api_request(path, token):
    # The authenticated URL is built from a fixed approved repository only.
    url = "https://api.github.com/repos/"+REPOSITORY+path
    return urllib.request.Request(url, headers={
        "Authorization": "Bearer "+token,
        "Accept": "application/vnd.github+json",
        "Accept-Encoding": "identity",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": SCHEMA})

def api_json(path, token):
    with urllib.request.build_opener(NoRedirect).open(api_request(path, token), timeout=45) as response:
        return load_json(response.read().decode("utf-8"))

def original_log_response(token):
    request = api_request("/actions/jobs/"+str(JOB)+"/logs", token)
    try:
        return urllib.request.build_opener(NoRedirect).open(request, timeout=45)
    except urllib.error.HTTPError as error:
        if error.code not in (301, 302, 303, 307, 308):
            raise
        location = error.headers.get("Location")
        error.close()
        address = urllib.parse.urlsplit(location or "")
        if address.scheme != "https" or not address.netloc or address.username or address.password:
            raise ValueError("invalid HTTPS download location")
        # Never forward the GitHub credential to the signed storage download.
        clean = urllib.request.Request(location, headers={
            "Accept-Encoding": "identity", "User-Agent": SCHEMA})
        return urllib.request.urlopen(clean, timeout=60)

def selected(mapping, keys):
    return {key: mapping.get(key) for key in keys}

def snapshot_outline(value, timestamp):
    qualification = value.get("actual_retained_qualification") or {}
    cost = value.get("cost") or {}
    return {
        "timestamp": timestamp, "reason": value.get("reason"), "outer": value.get("outer"),
        "phase": value.get("phase"), "q_sha256": value.get("actual_q_binary64_sha256"),
        "actual_eta": qualification.get("accepted_eta_max"),
        "actual_geometry_violation": qualification.get("accepted_geometry_violation_max"),
        "radial_nodes": len(value.get("actual_complete_required_radial_nodes", [])),
        "peak_orbits": len(value.get("actual_complete_required_peak_orbits", [])),
        "pending_physical_peaks": len(value.get("recorded_unapplied_physical_peak_orbits", [])),
        "working_rows": len(value.get("actual_working_field_orbit_rows", [])),
        "pending_working_rows": len(value.get("recorded_unapplied_working_rows", [])),
        "actual_trust": value.get("actual_backend_local_trust"),
        "proposed_trust": value.get("proposed_next_local_trust"),
        "trust_decision_completed": value.get("post_backend_trust_decision_completed"),
        "elapsed_scientific_seconds": cost.get("elapsed_seconds"),
        "working_base_extra": value.get("retained_working_feasible_base_extra"),
        "last_selected_backtrack_fraction": (value.get("last_working_backtrack") or {}).get("selected_fraction"),
        "accepted_counts": selected(cost.get("counts") or {},(
            "accepted_metric_steps","accepted_restoration_steps",
            "backtracked_fully_qualified_acceptances"))}

def parse_stream(response):
    started = time.monotonic()
    raw_hash = hashlib.sha256()
    raw_bytes = lines = parsed = 0
    tags, reasons = Counter(), Counter()
    failures, metadata, restriction, stops = [], {}, [], []
    first_snapshot = last_snapshot = last_snapshot_text = last_snapshot_tag = None
    first_snapshot_time = last_snapshot_time = None
    last_q = None
    q_changes = []
    previous_counts = {}
    count_decreases = []
    source_identity = None
    last_backend_start = last_jacobian = None
    jacobian_totals = {"completed_records": 0, "sum_record_seconds": 0.,
                       "largest_rows": 0, "largest_sub_radial_grid": 0,
                       "maximum_block_value_difference": 0.}
    final_count = 0
    http_headers = selected(dict(response.headers), ("Content-Type", "Content-Encoding", "Content-Length"))
    for line in response:
        raw_hash.update(line)
        raw_bytes += len(line)
        lines += 1
        try:
            text = line.decode("utf-8").rstrip("\r\n")
        except UnicodeDecodeError:
            failures.append({"line": lines, "kind": "invalid_utf8", "bytes": len(line), "sha256": sha(line)})
            continue
        match = LINE.match(text)
        if match is None:
            continue
        tag, body, timestamp = match.group("tag", "body", "time")
        tags[tag] += 1
        try:
            value = load_json(body)
        except (ValueError, TypeError) as error:
            failures.append({"line": lines, "kind": "invalid_JSON", "tag": tag,
                             "bytes": len(body.encode()), "sha256": sha(body.encode()),
                             "error_type": type(error).__name__})
            continue
        parsed += 1
        if tag.startswith("INVERSE_ACTIONS_"):
            metadata[tag] = value
        if tag == "WORKING_ROWS_BACKTRACK_DEFINITION":
            source_identity = {
                "source_state_sha256": value.get("source_state_sha256"),
                "schema": value.get("schema"),
                "physical_parameters": value.get("physical_parameters"),
                "geometry_parameters": value.get("geometry_parameters"),
                "solver_arguments": value.get("solver_arguments"),
                "complete_definition_JSON_bytes": len(body.encode()),
                "complete_definition_JSON_sha256": sha(body.encode())}
        elif tag == "WORKING_ROWS_NEW_RESTRICTION_MAP":
            restriction.append({"timestamp": timestamp, "observation": value})
        elif tag == "WORKING_ROWS_STOP":
            stops.append({"timestamp": timestamp, "stop": value})
        elif tag == "WORKING_ROWS_BACKEND_START":
            last_backend_start = {"timestamp": timestamp, "record": value}
        elif tag == "WORKING_ROWS_JACOBIAN":
            last_jacobian = {"timestamp": timestamp, "record": value}
            jacobian_totals["completed_records"] += 1
            jacobian_totals["sum_record_seconds"] += float(value.get("seconds", 0.))
            jacobian_totals["largest_rows"] = max(jacobian_totals["largest_rows"], value.get("rows", 0))
            jacobian_totals["largest_sub_radial_grid"] = max(
                jacobian_totals["largest_sub_radial_grid"], value.get("largest_sub_radial_grid", 0))
            jacobian_totals["maximum_block_value_difference"] = max(
                jacobian_totals["maximum_block_value_difference"],
                value.get("counts", {}).get("maximum_block_value_difference", 0.))
        if tag not in SNAPSHOT_TAGS:
            continue
        if not isinstance(value, dict):
            failures.append({"line": lines, "tag": tag, "kind": "snapshot_not_object"})
            continue
        reasons[str(value.get("reason"))] += 1
        actual_q = value.get("actual_retained_q")
        if not isinstance(actual_q, list) or len(actual_q) != 81:
            failures.append({"line": lines, "tag": tag, "kind": "actual_81q_missing"})
        else:
            actual_binary = struct.pack("<81d", *actual_q)
            if sha(actual_binary) != value.get("actual_q_binary64_sha256"):
                failures.append({"line": lines, "tag": tag, "kind": "actual_q_binary_identity_differs"})
        for key, count in value.get("cost", {}).get("counts", {}).items():
            if key in previous_counts and count < previous_counts[key]:
                count_decreases.append({"line": lines, "key": key,
                                        "before": previous_counts[key], "after": count})
            previous_counts[key] = count
        if first_snapshot is None:
            first_snapshot, first_snapshot_time = value, timestamp
        if value.get("actual_q_binary64_sha256") != last_q:
            q_changes.append(snapshot_outline(value, timestamp))
            last_q = value.get("actual_q_binary64_sha256")
        last_snapshot, last_snapshot_text = value, body
        last_snapshot_tag, last_snapshot_time = tag, timestamp
        final_count += tag == "WORKING_ROWS_FINAL"
    complete = not failures and not count_decreases
    result = {
        "schema": SCHEMA, "source_run": RUN, "source_job": JOB, "source_commit": COMMIT,
        "HTTP_raw_bytes": raw_bytes, "HTTP_raw_sha256": raw_hash.hexdigest(),
        "HTTP_response_headers": http_headers, "raw_line_count": lines,
        "tagged_JSON_records": sum(tags.values()), "successfully_parsed_JSON_records": parsed,
        "tag_counts": dict(tags), "all_tagged_JSON_and_q_identities_parsed": complete,
        "parse_or_identity_failures": failures, "cumulative_count_decreases": count_decreases,
        "source_definition_identity": source_identity,
        "rules_and_runner_metadata": metadata,
        "new_restriction_map_observations": restriction,
        "all_explicit_stops": stops, "snapshot_reason_counts": dict(reasons),
        "first_complete_state": None if first_snapshot is None else snapshot_outline(first_snapshot, first_snapshot_time),
        "last_complete_state": None if last_snapshot is None else snapshot_outline(last_snapshot, last_snapshot_time),
        "all_actual_retained_q_changes_including_initial": q_changes,
        "completed_Jacobian_record_totals_not_added_again_to_final_counters": jacobian_totals,
        "last_backend_start": last_backend_start,
        "last_complete_Jacobian": last_jacobian,
        "natural_FINAL_record_count": final_count,
        "last_complete_original_tag": last_snapshot_tag,
        "last_complete_original_JSON_bytes": None if last_snapshot_text is None else len(last_snapshot_text.encode()),
        "last_complete_original_JSON_sha256": None if last_snapshot_text is None else sha(last_snapshot_text.encode()),
        "unflushed_work_after_last_state_unknown_if_no_FINAL": final_count == 0,
        "last_trial_not_promoted_to_accepted_state": True,
        "prior_or_final_cumulative_costs_not_summed_from_snapshots": True,
        "metadata_recovery_elapsed_seconds_not_scientific_work": time.monotonic()-started,
        "scientific_evaluations": 0,
        "raw_files_artifacts_releases_or_Git_writes": False,
        "continuous_geometry_or_README_completion_claim": False}
    return result, last_snapshot_tag, last_snapshot_text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise RuntimeError("this terminal-log reader runs only in its declared public Actions job")
    request_path = Path(args.request)
    request_bytes = request_path.read_bytes()
    request = load_json(request_bytes.decode())
    if (request.get("schema") != SCHEMA or request.get("source_run") != RUN
            or request.get("source_job") != JOB or request.get("source_commit") != COMMIT
            or request.get("scientific_evaluations") != 0):
        raise ValueError("wrong terminal-log metadata scope")
    repository = Path(__file__).resolve().parents[3]
    for relative, expected in request["source_sha256"].items():
        path = (repository/relative).resolve()
        if repository not in path.parents or sha(path.read_bytes()) != expected:
            raise ValueError("metadata source binding differs: "+relative)
    token = os.environ.pop("GH_LOG_READ_TOKEN")
    run = api_json("/actions/runs/"+str(RUN), token)
    job = api_json("/actions/jobs/"+str(JOB), token)
    if (run.get("id") != RUN or run.get("head_sha") != COMMIT or run.get("status") != "completed"
            or job.get("id") != JOB or job.get("run_id") != RUN or job.get("status") != "completed"):
        raise ValueError("original run/job is not the declared natural terminal identity")
    emit("WORKING_RECOVERY_TERMINAL_IDENTITY", {
        "request_bytes": len(request_bytes), "request_sha256": sha(request_bytes),
        "run": selected(run, ("id", "head_sha", "status", "conclusion", "path", "created_at", "updated_at")),
        "job": selected(job, ("id", "run_id", "head_sha", "status", "conclusion", "started_at", "completed_at", "steps")),
        "source_stdout_read_only_after_terminal": True,
        "scientific_code_imported_or_run": False})
    with original_log_response(token) as response:
        token = None
        receipt, tag, original_json = parse_stream(response)
    emit("WORKING_RECOVERY_COMPLETE_PARSE_RECEIPT", receipt)
    if original_json is not None:
        # One complete actual state, exactly the original JSON bytes excluding
        # the original timestamp/tag. This is not a replay of the raw log.
        print("RECOVERED_"+tag+" "+original_json, flush=True)
    if not receipt["all_tagged_JSON_and_q_identities_parsed"] or original_json is None:
        raise RuntimeError("terminal log read completely, but original state accounting is incomplete")

if __name__ == "__main__":
    main()
