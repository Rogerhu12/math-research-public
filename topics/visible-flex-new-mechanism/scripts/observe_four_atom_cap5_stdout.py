#!/usr/bin/env python3
"""Read one completed CAP4 research job once; perform no scientific work.

The workflow may still be running because this observer is its report job.
Only this job's original stdout is downloaded.  Normal oracle payloads stay
there; failures, optimizer returns, candidates, certificates and final records
are preserved.  Observer completion is never scientific success.
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
RAW_CAP = 48 * 1024 * 1024
OUTPUT_CAP = 4 * 1024 * 1024
READER_BYTES = 50679
READER_SHA256 = "b7b16d0917bf99e4183421ab6d5c1dd33b9c0fe8009ad59a5141a17d798e5c4a"
TAGS = ("CAP4_RECORD", "CAP4_FINAL_REPORT", "CAP4_FINAL_CLOCK")
TAG = re.compile(r"(?<![A-Za-z0-9_])(CAP4_RECORD|CAP4_FINAL_REPORT|CAP4_FINAL_CLOCK)\s+(?=\{)")
PULL_TAG = re.compile(r"(?<![A-Za-z0-9_])(CAP4_PUBLIC_PULL|CAP4_PRIVATE_PULL)\s+(?=\{)")
ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
SHA40 = re.compile(r"[0-9a-f]{40}")
SHA256 = re.compile(r"[0-9a-f]{64}")
ENCODER = json.JSONEncoder(ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False)
CANDIDATE_MODES = {
    "decimal_complete_value_and_slice_analytic_J",
    "exact_rational_slice_center_complete_value_and_J",
    "rational_interval_complete_slice_value_and_analytic_J",
}
SMALL_FULL_KINDS = {
    "entry_inputs_bound", "new_finite_formula_ready",
    "optimization_start", "optimization_return",
    "optimization_candidate_stop", "optimization_account_stop",
    "optimization_failure", "certificate_box_domain_rejected",
    "rational_contraction_test", "oracle_failed",
    "candidate_physical_minor_attempt", "candidate_physical_minor_selection",
    "candidate_exact_physical_slice", "optimization_per_start_limit",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return ENCODER.encode(value).encode("utf-8")


def encoded(value):
    # Preserve decoded strings without allowing their Actions command spelling.
    return canonical(value).replace(b"##[", b"\\u0023\\u0023[").replace(
        b"::", b"\\u003a\\u003a")


def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key in original tagged record")
        result[key] = value
    return result


def parse_json(text):
    def reject_constant(value):
        raise ValueError("non-finite JSON constant in original tagged record")
    return json.loads(text, object_pairs_hook=no_duplicates,
                      parse_constant=reject_constant)


def load_reader():
    # This module contains only stdlib definitions; its main/run are not called.
    path = Path(__file__).resolve().with_name("read_original_actions_log.py")
    data = path.read_bytes()
    require(len(data) == READER_BYTES and digest(data) == READER_SHA256,
            "pinned stdlib log reader identity changed")
    spec = importlib.util.spec_from_file_location("cap4_readonly_paid_reader", path)
    require(spec is not None and spec.loader is not None, "reader loader unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.LOG_CAP = RAW_CAP
    return module


def concise(obj, keys):
    return {key: obj.get(key) for key in keys}


def record_identity(item):
    obj = item["original"]
    result = {
        "log_line": item["log_line"],
        "json_utf8_bytes": item["json_utf8_bytes"],
        "json_sha256": item["json_sha256"],
        "tagged_line_sha256": item["tagged_line_sha256"],
    }
    if item["tag"] == "CAP4_RECORD":
        result.update(seq=obj.get("seq"), kind=obj.get("kind"),
                      claimed_payload_sha256=obj.get("payload_sha256"),
                      claimed_chain_sha256=obj.get("chain_sha256"))
    return result


def collect_receipts(value, result):
    """Copy referenced sequence identities; do not rank numeric observations."""
    if isinstance(value, dict):
        if (type(value.get("seq")) is int and
                isinstance(value.get("sha256"), str) and
                SHA256.fullmatch(value["sha256"])):
            result.add(value["seq"])
        for item in value.values():
            collect_receipts(item, result)
    elif isinstance(value, list):
        for item in value:
            collect_receipts(item, result)


def observe(args, context):
    require(os.environ.get("GITHUB_ACTIONS") == "true",
            "observer is restricted to the public Actions report job")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    require(repository == REPOSITORY, "repository identity mismatch")
    require(args.run_id > 0 and args.job_id > 0, "run/job IDs must be positive")
    require(SHA40.fullmatch(args.source_commit) is not None,
            "source commit must be an exact lowercase SHA40")
    require(args.workflow.startswith(".github/workflows/") and
            ".." not in Path(args.workflow).parts,
            "--workflow must be the repository-relative workflow path")
    context["requested_original_identity"] = {
        "repository": repository, "run_id": args.run_id, "job_id": args.job_id,
        "source_commit": args.source_commit, "workflow": args.workflow,
    }
    context["reader_identity"] = {
        "path": "topics/visible-flex-new-mechanism/scripts/read_original_actions_log.py",
        "bytes": READER_BYTES, "sha256": READER_SHA256,
    }
    reader = load_reader()
    api = reader.GitHubReader(repository)
    run = api.api_json("/actions/runs/" + str(args.run_id))
    job = api.api_json("/actions/jobs/" + str(args.job_id))
    context["original_run"] = concise(run, (
        "id", "run_attempt", "workflow_id", "path", "name", "status",
        "conclusion", "head_sha", "created_at", "updated_at", "html_url"))
    context["original_job"] = concise(job, (
        "id", "run_id", "run_attempt", "name", "status", "conclusion",
        "head_sha", "started_at", "completed_at", "html_url"))
    context["original_job_steps"] = [
        concise(step, ("name", "number", "status", "conclusion",
                       "started_at", "completed_at"))
        for step in job.get("steps", [])
    ]
    require(run.get("id") == args.run_id and
            run.get("head_sha") == args.source_commit and
            run.get("path") == args.workflow, "run/source/workflow binding mismatch")
    require(job.get("id") == args.job_id and job.get("run_id") == args.run_id,
            "research job/run binding mismatch")
    if job.get("head_sha") is not None:
        require(job["head_sha"] == args.source_commit, "job/source binding mismatch")
    require(job.get("status") == "completed", "research job is not completed")
    # Deliberately do not require the workflow or job conclusion to be success.
    context["workflow_may_still_be_running"] = True
    context["raw_log_downloads_started"] = 1
    raw, redirects = api.job_log(args.job_id)  # The only original log read.
    context["raw_log"] = {
        "bytes": len(raw), "sha256": digest(raw), "cap_bytes": RAW_CAP,
        "redirects": redirects, "downloads_completed": 1,
        "saved_or_uploaded": False,
    }
    text = raw.decode("utf-8-sig")
    items = []
    errors = []
    counts = collections.Counter()
    by_kind = {}
    identity_chain = hashlib.sha256()
    previous = None
    first = None
    last = None
    strictly_increasing = True
    contiguous = True
    for number, original_line in enumerate(text.splitlines(), 1):
        # An internal BOM may precede a timestamp.  No TIME_PREFIX.sub is used.
        line = ANSI.sub("", original_line).lstrip("\ufeff")
        pull = PULL_TAG.search(line)
        if pull is not None:
            original_json = line[pull.end():].strip()
            data = original_json.encode("utf-8")
            try:
                obj = parse_json(original_json)
                require(isinstance(obj, dict), "original pull must be an object")
                context["original_actual_pulls"].append({
                    "tag": pull.group(1), "log_line": number,
                    "json_utf8_bytes": len(data), "json_sha256": digest(data),
                    "original": obj,
                    "all_original_fields_preserved": True})
            except Exception as exc:
                errors.append({
                    "log_line": number, "tag": pull.group(1),
                    "json_utf8_bytes": len(data), "json_sha256": digest(data),
                    "error_type": type(exc).__name__, "error": str(exc)[:500]})
            continue
        match = TAG.search(line)
        if match is None:
            continue
        tag = match.group(1)
        original_json = line[match.end():].strip()
        data = original_json.encode("utf-8")
        try:
            obj = parse_json(original_json)
            require(isinstance(obj, dict), "tagged JSON is not an object")
            if tag == "CAP4_RECORD":
                require(type(obj.get("seq")) is int and obj["seq"] > 0,
                        "record sequence is not a positive integer")
                require(isinstance(obj.get("kind"), str) and
                        isinstance(obj.get("payload"), dict),
                        "record kind/payload structure is invalid")
                require(all(isinstance(obj.get(key), str) and
                            SHA256.fullmatch(obj[key]) for key in
                            ("payload_sha256", "chain_sha256")),
                        "record claimed hash structure is invalid")
        except Exception as exc:
            errors.append({
                "log_line": number, "tag": tag, "json_utf8_bytes": len(data),
                "json_sha256": digest(data), "error_type": type(exc).__name__,
                "error": str(exc)[:500],
            })
            continue
        item = {
            "tag": tag, "log_line": number, "json_utf8_bytes": len(data),
            "json_sha256": digest(data),
            "tagged_line_sha256": digest(tag.encode("ascii") + b" " + data + b"\n"),
            "original": obj,
        }
        items.append(item)
        if tag == "CAP4_RECORD":
            kind, seq = obj["kind"], obj["seq"]
            identity = record_identity(item)
            counts[kind] += 1
            if kind not in by_kind:
                by_kind[kind] = {"first": identity, "last": identity}
            else:
                by_kind[kind]["last"] = identity
            identity_chain.update(canonical(identity) + b"\n")
            if previous is not None:
                strictly_increasing = strictly_increasing and seq > previous
                contiguous = contiguous and seq == previous + 1
            if first is None:
                first = seq
            last = seq
            previous = seq
    refs = set()
    finals = [item for item in items if item["tag"] != "CAP4_RECORD"]
    for item in finals:
        collect_receipts(item["original"], refs)
    for item in items:
        if item["tag"] == "CAP4_RECORD" and item["original"]["kind"] in SMALL_FULL_KINDS:
            collect_receipts(item["original"]["payload"], refs)
    selected = []
    for item in items:
        if item["tag"] != "CAP4_RECORD":
            selected.append(item)
            continue
        obj = item["original"]
        kind = obj["kind"]
        if (kind in SMALL_FULL_KINDS or "fail" in kind.lower() or
                "candidate" in kind.lower() or "certificate" in kind.lower() or
                obj["seq"] in refs or
                (kind == "oracle_completed" and
                 obj["payload"].get("mode") in CANDIDATE_MODES)):
            selected.append(item)
    context["tagged_records"] = {
        "record_count": sum(counts.values()), "kind_counts": dict(sorted(counts.items())),
        "first_seq": first, "last_seq": last,
        "seq_strictly_increasing": strictly_increasing,
        "seq_contiguous_in_observed_order": contiguous,
        "first_and_last_identity_by_kind": by_kind,
        "observed_identity_rows_sha256": identity_chain.hexdigest(),
        "original_payload_and_chain_hashes_are_copied_not_recomputed": True,
        "final_report_count": sum(item["tag"] == "CAP4_FINAL_REPORT" for item in finals),
        "final_clock_count": sum(item["tag"] == "CAP4_FINAL_CLOCK" for item in finals),
        "selected_full_record_count": len(selected),
        "normal_oracle_payloads_remain_in_original_log": True,
    }
    context["parse_errors"] = errors
    context["preserved_original_records"] = selected
    complete = (not errors and strictly_increasing and contiguous and
                context["tagged_records"]["final_report_count"] == 1 and
                context["tagged_records"]["final_clock_count"] == 1)
    context["observer_status"] = (
        "original_stdout_observed" if complete else "incomplete_original_stdout_observation")
    context["scientific_outcomes_as_reported"] = [
        item["original"].get("outcome") for item in finals
        if item["tag"] == "CAP4_FINAL_REPORT"
    ]
    return 0 if complete else 2


def main():
    started = time.perf_counter()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", type=int, required=True)
    parser.add_argument("--job-id", type=int, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    context = {
        "schema": "cap4-readonly-original-stdout-observer-v1",
        "observer_status": "not_completed",
        "raw_log_cap_bytes": RAW_CAP, "stdout_cap_bytes": OUTPUT_CAP,
        "no_science_imported_or_executed": True,
        "no_old_cap_log_read": True,
        "scientific_success_is_not_inferred_from_observer_completion": True,
        "raw_log_downloads_started": 0,
        "original_actual_pulls": [],
    }
    code = 1
    try:
        code = observe(args, context)
    except Exception as exc:
        context["observer_status"] = "observer_failure"
        context["observer_failure"] = {
            "type": type(exc).__name__, "message": str(exc)[:1500]
        }
    context["observer_elapsed_before_output_seconds"] = time.perf_counter() - started
    output = b"CAP4_LOG_OBSERVATION " + encoded(context) + b"\n"
    if len(output) > OUTPUT_CAP:
        # Never hide a cap failure as a complete scientific readback.
        selected = context.pop("preserved_original_records", [])
        context["observer_status"] = "observer_output_cap_exceeded"
        context["required_output_bytes"] = len(output)
        context["full_selection_retained"] = False
        context["omitted_selection_identity"] = [
            {"tag": item["tag"], **record_identity(item)} for item in selected
            if item["tag"] == "CAP4_RECORD"
        ]
        context["preserved_original_records"] = [
            item for item in selected if item["tag"] != "CAP4_RECORD" or
            "fail" in item["original"].get("kind", "").lower()
        ]
        context["detail"] = (
            "The original log remains authoritative.  This is an observer limit, "
            "not a new scientific result or a successful full readback.")
        output = b"CAP4_LOG_OBSERVATION " + encoded(context) + b"\n"
        code = 2
    if len(output) > OUTPUT_CAP:
        # Extremely large original final/failure payloads cannot fit the contract.
        # Preserve all provenance and their exact identities, and say so explicitly.
        selected = context.pop("preserved_original_records", [])
        context["final_or_failure_payloads_exceeded_output_cap"] = [
            {"tag": item["tag"], **record_identity(item)} for item in selected
        ]
        context.pop("omitted_selection_identity", None)
        context["final_payloads_retained"] = False
        output = b"CAP4_LOG_OBSERVATION " + encoded(context) + b"\n"
        code = 2
    require(len(output) <= OUTPUT_CAP, "observer metadata itself exceeds output cap")
    try:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(output)
    except Exception as exc:
        # stdout remains the complete readback if only the temporary file fails.
        context["temporary_output_error"] = {
            "type": type(exc).__name__, "message": str(exc)[:1000]
        }
        output = b"CAP4_LOG_OBSERVATION " + encoded(context) + b"\n"
        require(len(output) <= OUTPUT_CAP, "file-error metadata exceeds output cap")
        code = 2
    sys.stdout.buffer.write(output)
    sys.stdout.buffer.flush()
    return code


if __name__ == "__main__":
    raise SystemExit(main())
