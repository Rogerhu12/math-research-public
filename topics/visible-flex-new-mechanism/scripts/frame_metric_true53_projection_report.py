#!/usr/bin/env python3
"""Read this completed research log only; retain semantics and original hashes."""
from __future__ import annotations
import time
STARTED = time.monotonic()
import argparse
import copy
import json
import os
from pathlib import Path
import re
import traceback
import read_original_actions_log as reader

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
POLICY = "same159-true53-complete-grid-maximin-projection-v1"
TAG = "TRUE53_PROJECTION_"
PATTERN = re.compile(r"\b(TRUE53_PROJECTION_[A-Z_]+)\s+(\{.*\})\s*$")
KNOWN = {
    "PUBLIC_PULL", "PRIVATE_PULL", "REQUEST", "DEVELOPMENT", "PRIOR_WORK_REUSED",
    "BASE_VALUES", "MODEL", "PROJECTION_EVENT", "PROJECTION_RESULT", "CACHE",
    "QUERY", "SCALAR_RESULT", "TRIAL", "COMPLETE", "REPORTING_ERROR",
    "FINAL_CLOCK", "OUTPUT_METADATA"}
SEMANTIC_CAP = 800000


def metadata(value):
    raw = reader.encoded(value)
    out = {"JSON_bytes": len(raw), "JSON_sha256": reader.digest(raw)}
    if isinstance(value, (dict, list, tuple, str)):
        out["count"] = len(value)
    return out


def semantic(value):
    """Only select already-emitted values; never reconstruct coefficients."""
    if isinstance(value, dict):
        return {key: semantic(item) for key, item in value.items()}
    if isinstance(value, list):
        if len(value) > 256 or any(isinstance(item, list) for item in value):
            return {"original_large_array_metadata": metadata(value),
                    "values_remain_only_in_original_research_stdout": True}
        return [semantic(item) for item in value]
    return copy.deepcopy(value)


def parse_records(raw):
    rows = []
    for line in raw.decode("utf-8-sig", errors="strict").splitlines():
        match = PATTERN.search(line)
        if match is None:
            continue
        name = match.group(1)[len(TAG):]
        if name not in KNOWN:
            continue
        payload = match.group(2).encode("utf-8")
        value = reader.decode_json(payload)
        rows.append({
            "tag": name, "timestamp_prefix": line[:match.start()].strip(),
            "data": value, "JSON_bytes": len(payload),
            "JSON_sha256": reader.digest(payload),
            "JSON_plus_LF_bytes": len(payload)+1,
            "JSON_plus_LF_sha256": reader.digest(payload+b"\n")})
    return rows


def unique(rows, name, required=False):
    found = [row for row in rows if row["tag"] == name]
    reader.require(len(found) <= 1, "duplicate unique source record: "+name)
    reader.require(not required or len(found) == 1, "missing source record: "+name)
    return found[0] if found else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    args = parser.parse_args()
    report = {
        "schema": POLICY+"-read-only-same-workflow-report", "status": "started",
        "scientific_imports_or_recomputations": 0,
        "dense_coefficient_arrays_not_forwarded_encoded_or_chunked": True,
        "full159_163_trial_vectors_preserved_as_small_semantic_records": True}
    try:
        raw_request = Path(args.request).read_bytes()
        request = json.loads(raw_request)
        source, run_id = os.environ["GITHUB_SHA"], os.environ["GITHUB_RUN_ID"]
        reader.require(request["repository"] == REPO, "unexpected repository")
        for path in (TOPIC+"/scripts/frame_metric_true53_projection_report.py",
                     TOPIC+"/scripts/read_original_actions_log.py",
                     ".github/workflows/visible-true53-projected-direction.yml"):
            reader.require(reader.digest(Path(path).read_bytes()) == request["source_sha256"][path],
                           "read-only source binding differs: "+path)
        api = reader.GitHubReader(REPO)
        run = api.api_json("/actions/runs/"+run_id)
        jobs = api.api_json("/actions/runs/"+run_id+"/jobs?per_page=100")
        selected = [job for job in jobs["jobs"] if job["name"] == "research"]
        reader.require(str(run["id"]) == run_id and run["head_sha"] == source
                       and len(selected) == 1, "unique same-source research job required")
        job = selected[0]
        reader.require(str(job["run_id"]) == run_id and job["head_sha"] == source
                       and job["status"] == "completed",
                       "research job must be complete; success is not assumed")
        raw, redirects = api.job_log(str(job["id"]))
        report["source"] = {
            "run_id": run_id, "job_id": str(job["id"]), "source_commit": source,
            "research_status": job["status"], "research_conclusion": job["conclusion"],
            "workflow_status_observed": run["status"],
            "raw_log_bytes": len(raw), "raw_log_sha256": reader.digest(raw),
            "redirects_without_authorization": redirects,
            "read_once_not_written_to_Git_artifact_release_or_cache": True}
        rows = parse_records(raw)
        report["record_fingerprints"] = [
            {key: value for key, value in row.items() if key != "data"} for row in rows]
        requested = unique(rows, "REQUEST")
        complete = unique(rows, "COMPLETE")
        cache = unique(rows, "CACHE")
        final_clock = unique(rows, "FINAL_CLOCK")
        if requested is not None:
            value = requested["data"]
            reader.require(value["source_commit"] == source
                           and value["request_bytes"] == len(raw_request)
                           and value["request_sha256"] == reader.digest(raw_request)
                           and value["source_sha256"] == request["source_sha256"],
                           "actual request and source closure differ")
            report["request"] = {
                "parameters": copy.deepcopy(value["parameters"]),
                "request_bytes": value["request_bytes"], "request_sha256": value["request_sha256"],
                "source_manifest": metadata(value["source_sha256"]),
                "actual_and_current_source_manifest_equal": True}
        else:
            report["request_record_missing"] = True
        for name, target in (
                ("PUBLIC_PULL", "scientific_public_pull"),
                ("PRIVATE_PULL", "scientific_private_pull"),
                ("DEVELOPMENT", "development"),
                ("PRIOR_WORK_REUSED", "prior_work_reused"),
                ("BASE_VALUES", "necessary_current53_model_values"),
                ("MODEL", "initial_complete_model"),
                ("PROJECTION_RESULT", "projection_result"),
                ("SCALAR_RESULT", "scalar_result"),
                ("REPORTING_ERROR", "scientific_reporting_error")):
            row = unique(rows, name)
            if row is not None:
                report[target] = semantic(row["data"])
                report[target+"_original_record"] = {
                    key: value for key, value in row.items() if key != "data"}
        if complete is not None:
            value = complete["data"]
            reader.require(value["schema"] == POLICY+"-audit"
                           and value["github_sha"] == source and str(value["github_run_id"]) == run_id,
                           "original COMPLETE identity differs")
            expected_py = {Path(path).name: sha for path, sha in request["source_sha256"].items()
                           if path.endswith(".py")}
            reader.require(value["source_files_sha256"] == expected_py,
                           "actual Python source closure differs")
            report["complete"] = semantic(value)
        model_record = unique(rows, "MODEL")
        if model_record is not None and complete is not None:
            receipt = complete["data"].get("model_stdout_receipt")
            reader.require(isinstance(receipt, dict)
                           and receipt["JSON_plus_LF_bytes"] == model_record["JSON_plus_LF_bytes"]
                           and receipt["JSON_plus_LF_sha256"] == model_record["JSON_plus_LF_sha256"],
                           "one original full or partial model and its receipt differ")
            report["model_receipt_matches_original_log_record"] = True
        if complete is None and job["conclusion"] != "success":
            unparsed = [line for line in raw.decode("utf-8-sig", errors="strict").splitlines()
                        if not PATTERN.search(line)]
            report["runtime_failure_tail_without_research_records"] = "\n".join(unparsed[-30:])[-6000:]
        if cache is not None:
            value = cache["data"]
            report["line_cache"] = semantic(value)
            report["line_cache_original_record"] = {
                key: item for key, item in cache.items() if key != "data"}
            report["entire_plain_cache_retained_in_research_stdout"] = True
            if complete is not None:
                receipt = complete["data"].get("line_cache_stdout_receipt")
                reader.require(isinstance(receipt, dict)
                               and receipt["JSON_plus_LF_bytes"] == cache["JSON_plus_LF_bytes"]
                               and receipt["JSON_plus_LF_sha256"] == cache["JSON_plus_LF_sha256"],
                               "single original line cache and its receipt differ")
                report["cache_receipt_matches_original_log_record"] = True
        if final_clock is not None:
            report["final_authoritative_clock"] = copy.deepcopy(final_clock["data"])
            report["scientific_scope_status"] = final_clock["data"]["status_at_final_emit"]
        else:
            report["final_authoritative_clock_missing"] = True
            report["scientific_scope_status"] = "unknown-without-final-clock"
        report["native_trial_records"] = [
            semantic(row["data"]) for row in rows if row["tag"] == "TRIAL"]
        report["projection_events"] = [
            semantic(row["data"]) for row in rows if row["tag"] == "PROJECTION_EVENT"]
        report["native_queries"] = [
            semantic(row["data"]) for row in rows if row["tag"] == "QUERY"]
        report["status"] = "read-only-observation-complete"
        report["source_scientific_pass_not_inferred_from_job_conclusion"] = True
    except Exception as error:
        report.update(status="read-only-observation-error",
                      error={"type": type(error).__name__, "message": str(error),
                             "traceback": traceback.format_exc()})
    report["read_only_report_seconds_separate_from_science"] = time.monotonic()-STARTED
    raw_output = reader.encoded(report)
    if len(raw_output) > SEMANTIC_CAP:
        removed = {}
        # Remove only secondary duplicates. Preserve the complete selected
        # point, all native trial159/163 vectors, terminal gates and final cost.
        whole = report.get("complete", {})
        for key in ("projection", "scalar_optimization", "all_queries",
                    "new_development", "initial_model_record"):
            if key in whole:
                removed["complete."+key] = metadata(whole.pop(key))
        stage = whole.get("projection_actual_stage", {})
        if stage.get("trials") == report.get("native_trial_records"):
            removed["complete.projection_actual_stage.trials"] = metadata(stage.pop("trials"))
        if "projection_events" in report:
            old = report.pop("projection_events")
            removed["secondary_projection_events"] = metadata(old)
        report["priority_secondary_omissions"] = removed
        raw_output = reader.encoded(report)
    report["semantic_output_bytes_before_final_size_field"] = len(raw_output)
    report["semantic_cap_exceeded_after_secondary_omissions"] = len(raw_output) > SEMANTIC_CAP
    print("TRUE53_PROJECTION_REPORT_COMPLETE "+reader.encoded(report).decode("utf-8"), flush=True)
    return 0 if report["status"] == "read-only-observation-complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
