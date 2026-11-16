#!/usr/bin/env python3
"""Read one fresh54-model-exchange Actions stdout; never execute research.

This observer downloads one original job log into memory (at most 128 MiB).
It emits only bounded semantic selections and original-record fingerprints.
Checkpoint/cache payloads remain solely in the original research stdout.
Optional --output writes the compact report below RUNNER_TEMP, never the log.

No NumPy, geometry, model, finite solver, JVP, line search, or trial module is
imported. Original numbers are selected, never reevaluated or repaired here.
"""
from __future__ import annotations

import time
STARTED = time.monotonic()

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Any

import read_original_actions_log as reader

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
POLICY = "same159-true54-fresh-original-model-exchange-v1"
TAG = "TRUE54_FRESH_"
REPORT_TAG = TAG + "READ_ONLY_REPORT"
SCHEMA = POLICY + "-read-only-semantic-report-v1"
LOG_CAP = 128 * 1024 * 1024
REPORT_CAP = 7 * 1024 * 1024
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
PREFIX = re.compile(r"^" + re.escape(TAG) + r"([A-Z][A-Z0-9_]*)[ \t]+(.*)$")
KNOWN_TAGS = {
    "INPUT", "MODEL", "BASE_VALUES", "JET_INPUT", "FULL_GRID_SCAN", "ATTAINER_GRADIENT",
    "LINE_QUERY", "ACTUAL_TRIAL", "CACHE", "COMPLETE", "FINAL_CLOCK",
    "REQUEST", "PUBLIC_PULL", "PRIVATE_PULL", "PRIOR_WORK_REUSED",
    "DIRECTION", "SCALAR_RESULT", "LINE_RESULT", "ACTUAL_RESULT",
    "REPORTING_ERROR", "OUTPUT_METADATA", "FINITE_RESULT", "MASTER_INPUT",
}
UNIQUE_TAGS = {"COMPLETE", "FINAL_CLOCK"}
IMPORTANT_KEYS = {
    "schema", "policy", "status", "reason", "error", "errors", "failure",
    "message", "passed", "accepted", "rejected", "phase", "grid", "branch",
    "kind", "label", "row", "row_id", "flat_row_id", "index", "alpha",
    "value", "gain", "slope", "score", "target", "epsilon", "iteration",
    "iteration_index", "query_index", "trial_index", "candidate_index",
    "accepted_index", "source_accepted_index", "source_actual_values",
    "new_actual_values", "total_actual_values", "complete", "feasible",
    "actual_feasible", "actual_accepted", "finite_positive_primal",
    "maximum", "minimum", "maxima", "four_maxima", "counts", "limits",
    "elapsed", "elapsed_seconds", "scientific_seconds", "total_seconds",
    "first_jet_input_restores", "pair_first_jet_jvps",
    "new_attainer_gradients", "scalar_sessions", "scalar_queries",
    "actual_trial_pairs", "actual_grid_values", "necessary_model_grid_values",
    "hard_J_grid_builds", "first_jet_grid_builds", "full_separations", "new_metric_rows",
}
DATA_LIST_KEYS = {
    "binary64", "exact_binary64", "coefficients", "coefficient_values",
    "data", "values", "array", "flat", "state", "state159", "state163",
    "independent159", "reference163", "direction", "direction159",
    "gradient", "gradient159", "de159", "df159", "e", "f", "de", "df",
    "U", "T", "Ts", "dT", "dTs", "dU", "radial", "theta",
}
LARGE_OBJECT_KEYS = {
    "checkpoint", "cp", "final_cp", "initial_cp",
    "future_projection_checkpoint", "future_checkpoint", "future_fresh54_checkpoint",
    "final_checkpoint", "source_checkpoint", "prepared_checkpoint",
    "cache", "cache_arrays", "first_jet_cache", "line_cache",
    "full_cache", "raw_cache", "arrays", "dense_arrays",
}
SOURCE_NAMES = {
    "repository", "run_id", "job_id", "source_run_id", "source_job_id",
    "github_run_id", "github_job_id", "source_commit", "head_sha",
    "github_sha", "commit", "workflow", "workflow_path", "blob",
    "blob_sha", "blob_sha1", "source_sha", "source_blob",
    "source_bytes", "request_bytes", "raw_log_bytes", "log_bytes",
    "JSON_bytes", "JSON_plus_LF_bytes", "canonical_json_bytes",
    "source_accepted_index", "source_original_values", "accepted_index",
    "source_global_seconds", "total_ancestor_plus_new_scientific_seconds",
    "total_source_plus_new_actual_values", "this_new_scientific_seconds",
}


def require(condition: bool, message: str) -> None:
    reader.require(condition, message)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_pointer(path: tuple[Any, ...]) -> str:
    return "/" + "/".join(str(part).replace("~", "~0").replace("/", "~1")
                           for part in path) if path else ""


def canonical_fingerprint(value: Any) -> dict[str, Any]:
    """Hash a subtree's canonical JSON; never label this its literal log span."""
    result = dict(reader.fingerprint(value))
    result["serialization"] = (
        "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); "
        "allow_nan=False; no trailing LF; not a literal source substring")
    result["json_type"] = (
        "object" if isinstance(value, dict) else
        "array" if isinstance(value, list) else
        "string" if isinstance(value, str) else
        "null" if value is None else
        "boolean" if isinstance(value, bool) else "number")
    if isinstance(value, (dict, list, str)):
        result["length"] = len(value)
    if isinstance(value, dict):
        keys = list(value)
        result["top_level_keys"] = keys[:256]
        if len(keys) > 256:
            result["top_level_keys_not_listed"] = len(keys) - 256
    if isinstance(value, list):
        result["element_kinds"] = sorted({
            "object" if isinstance(item, dict) else
            "array" if isinstance(item, list) else
            "string" if isinstance(item, str) else
            "null" if item is None else
            "boolean" if isinstance(item, bool) else "number"
            for item in value[:64]})
        result["element_kind_sample_length"] = min(len(value), 64)
    return result


def scalar(value: Any) -> bool:
    return value is None or isinstance(value, (bool, int, float, str))


def payload_object(key: str, value: Any) -> bool:
    """Block whole checkpoints/caches, including short or partial versions."""
    if not isinstance(value, (dict, list)):
        return False
    lower = key.lower()
    if key in LARGE_OBJECT_KEYS or lower in LARGE_OBJECT_KEYS:
        return True
    if "checkpoint" in lower:
        return not any(word in lower for word in
                       ("receipt", "metadata", "manifest", "identity", "binding"))
    if lower.endswith("_cache") or lower.endswith("_cache_arrays"):
        return not any(word in lower for word in
                       ("receipt", "metadata", "manifest", "identity", "binding"))
    return False


def identity_leaf(key: str, value: Any) -> bool:
    if not scalar(value):
        return False
    lower = key.lower()
    return (
        key in SOURCE_NAMES or lower in SOURCE_NAMES
        or lower.endswith(("_sha256", "_sha1", "_blob_sha", "_commit",
                           "_run_id", "_job_id", "_workflow"))
        or (isinstance(value, str) and HEX64.fullmatch(value)
            and ("/" in key or key.endswith((".py", ".json", ".yml", ".yaml"))))
    )


class SemanticView:
    """Bounded selection of already-emitted scalars; arrays become metadata."""

    def __init__(self, *, level: int = 0):
        self.level = level
        self.nodes = 0
        self.node_cap = (14000, 6000, 2000)[min(level, 2)]
        self.depth_cap = (16, 12, 8)[min(level, 2)]
        self.list_cap = (64, 32, 12)[min(level, 2)]
        self.string_cap = (4096, 2048, 512)[min(level, 2)]
        self.omissions: list[dict[str, Any]] = []

    def omitted(self, value: Any, path: tuple[Any, ...], reason: str) -> dict[str, Any]:
        record = {"json_pointer": json_pointer(path), "reason": reason,
                  **canonical_fingerprint(value)}
        self.omissions.append(record)
        return {"payload_not_forwarded": record,
                "original_value_retained_in_research_stdout": True}

    def view(self, value: Any, path: tuple[Any, ...] = ()) -> Any:
        self.nodes += 1
        if self.nodes > self.node_cap:
            return self.omitted(value, path, "semantic node budget")
        if len(path) > self.depth_cap:
            return self.omitted(value, path, "semantic depth budget")
        key = str(path[-1]) if path else ""
        if payload_object(key, value):
            return self.omitted(value, path, "checkpoint/cache payload")
        if isinstance(value, str):
            if len(value) <= self.string_cap:
                return value
            return self.omitted(value, path, "long original string")
        if scalar(value):
            return value
        if isinstance(value, dict):
            if len(value) > 512:
                # Source maps have short scalar entries and remain readable.
                if all(identity_leaf(str(k), v) for k, v in value.items()):
                    return dict(value)
                small = {
                    k: self.view(v, path + (k,))
                    for k, v in value.items()
                    if scalar(v) and (k in IMPORTANT_KEYS or identity_leaf(k, v))}
                return {
                    "selected_original_fields": small,
                    "whole_object_metadata": canonical_fingerprint(value),
                    "unselected_fields_not_forwarded": True}
            return {key: self.view(item, path + (key,))
                    for key, item in value.items()}
        if isinstance(value, list):
            if (key in DATA_LIST_KEYS
                    or any(isinstance(item, list) for item in value)
                    or (len(value) > 16 and all(
                        item is None or isinstance(item, (bool, int, float))
                        for item in value))
                    or len(value) > self.list_cap):
                return self.omitted(value, path, "array payload")
            return [self.view(item, path + (index,))
                    for index, item in enumerate(value)]
        return self.omitted(value, path, "unrecognized JSON value")


def provenance(value: Any, path: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    """All emitted source/record identities; never traverse numeric arrays."""
    result: list[dict[str, Any]] = []
    stack = [(value, path)]
    while stack:
        obj, current = stack.pop()
        if isinstance(obj, dict):
            for key, item in reversed(list(obj.items())):
                child = current + (key,)
                if identity_leaf(key, item):
                    result.append({"json_pointer": json_pointer(child),
                                   "value": item})
                elif isinstance(item, (dict, list)):
                    stack.append((item, child))
        elif isinstance(obj, list):
            if any(isinstance(item, (dict, list)) for item in obj):
                for index in range(len(obj) - 1, -1, -1):
                    item = obj[index]
                    if isinstance(item, dict):
                        stack.append((item, current + (index,)))
                    # Dense nested lists are data, not source identities.
    return result


def checkpoint_cache_manifest(value: Any) -> list[dict[str, Any]]:
    """Fingerprint each named payload without expanding its arrays."""
    result: list[dict[str, Any]] = []
    stack = [(value, ())]
    while stack:
        obj, path = stack.pop()
        if isinstance(obj, dict):
            for key, item in reversed(list(obj.items())):
                child = path + (key,)
                if payload_object(key, item):
                    result.append({
                        "json_pointer": json_pointer(child),
                        **canonical_fingerprint(item)})
                    # A top-level payload hash covers all nested data. We do not
                    # repeatedly hash every dense coefficient array inside it.
                elif isinstance(item, (dict, list)):
                    stack.append((item, child))
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                if isinstance(item, dict):
                    stack.append((item, path + (index,)))
    return result


def normalize_line(line: str) -> tuple[str | None, str]:
    # The source Actions runner can insert U+FEFF before an interior timestamp.
    clean = reader.ANSI.sub("", line).lstrip("\ufeff")
    match = reader.TIME_PREFIX.match(clean)
    if match is None:
        return None, clean.lstrip("\ufeff")
    return match.group(1), match.group(2).lstrip("\ufeff")


def parse_records(raw: bytes) -> tuple[list[dict[str, Any]],
                                       list[dict[str, Any]], dict[str, Any]]:
    text = raw.decode("utf-8-sig", errors="strict")
    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    ordinal: Counter[str] = Counter()
    non_record_tail: list[str] = []
    unknown: set[str] = set()
    total_lines = 0
    for line_number, line in enumerate(text.splitlines(), 1):
        total_lines = line_number
        timestamp, body = normalize_line(line)
        match = PREFIX.fullmatch(body)
        if match is None:
            if body.startswith(TAG):
                errors.append({
                    "line_number": line_number,
                    "timestamp": timestamp,
                    "error": "malformed fresh54-model-exchange tag line",
                    "normalized_line_bytes": len(body.encode("utf-8")),
                    "normalized_line_sha256": digest(body.encode("utf-8"))})
            elif not body.startswith("##["):
                # Bounded failure context only, never a substring of a large
                # research record and never raw log output to a file.
                non_record_tail.append(body[:1000])
                non_record_tail = non_record_tail[-20:]
            continue
        name, payload_text = match.groups()
        # Strip only delimiter whitespace outside JSON. All characters inside
        # the original JSON representation are retained in the literal hash.
        payload = payload_text.rstrip(" \t").encode("utf-8")
        ordinal[name] += 1
        entry = {
            "sequence": len(records) + len(errors) + 1,
            "tag": name, "tag_ordinal": ordinal[name],
            "line_number": line_number, "timestamp": timestamp,
            "JSON_bytes": len(payload), "JSON_sha256": digest(payload),
            "JSON_plus_LF_bytes": len(payload) + 1,
            "JSON_plus_LF_sha256": digest(payload + b"\n"),
            "hash_scope": "literal emitted JSON after tag, normalized trailing LF",
        }
        try:
            data = reader.decode_json(payload)
            require(isinstance(data, dict), "record payload must be a JSON object")
        except Exception as error:
            errors.append({**entry, "error_type": type(error).__name__,
                           "error": str(error)[:512]})
            continue
        if name not in KNOWN_TAGS:
            unknown.add(name)
        records.append({**entry, "data": data})
    return records, errors, {
        "decoded_log_lines": total_lines,
        "prefix": TAG, "tag_counts": dict(sorted(ordinal.items())),
        "unknown_tags_preserved": sorted(unknown),
        "non_record_failure_tail": non_record_tail,
        "interior_BOM_and_ANSI_prefix_normalization": True,
        "payload_numbers_not_recomputed": True}


def record_identity(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if key != "data"}


def original_status_fields(value: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value[key] for key in
        ("schema", "policy", "status", "reason", "error", "passed", "accepted",
         "failure_stage", "final_status", "selected_status",
         "original_actual_status", "actual_status")
        if key in value and scalar(value[key])}


def receipt_checks(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Compare emitted byte/hash receipts; this is serialization, not science."""
    lookup: dict[tuple[Any, Any], list[int]] = {}
    for record in records:
        key = (record["JSON_plus_LF_bytes"], record["JSON_plus_LF_sha256"])
        lookup.setdefault(key, []).append(record["sequence"])
    checks = []
    for record in records:
        if record["tag"] not in {"COMPLETE", "FINAL_CLOCK", "OUTPUT_METADATA"}:
            continue
        stack = [(record["data"], ())]
        while stack:
            obj, path = stack.pop()
            if isinstance(obj, dict):
                if ("JSON_plus_LF_bytes" in obj
                        and "JSON_plus_LF_sha256" in obj):
                    key = (obj["JSON_plus_LF_bytes"], obj["JSON_plus_LF_sha256"])
                    matches = lookup.get(key, [])
                    checks.append({
                        "record_sequence": record["sequence"],
                        "json_pointer": json_pointer(path),
                        "emitted_receipt": {
                            "JSON_plus_LF_bytes": obj["JSON_plus_LF_bytes"],
                            "JSON_plus_LF_sha256": obj["JSON_plus_LF_sha256"]},
                        "matching_record_sequences_in_this_log": matches,
                        "interpretation": (
                            "matched literal source record" if matches else
                            "not in this log; may be an ancestor receipt; "
                            "not labeled a failed scientific check")})
                for key, item in obj.items():
                    if isinstance(item, dict) and not payload_object(key, item):
                        stack.append((item, path + (key,)))
                    elif isinstance(item, list) and key not in DATA_LIST_KEYS:
                        for index, element in enumerate(item):
                            if isinstance(element, dict):
                                stack.append((element, path + (key, index)))
    return checks


def record_view(record: dict[str, Any], *, level: int) -> dict[str, Any]:
    data = record["data"]
    projector = SemanticView(level=level)
    result = {"identity": record_identity(record)}
    if record["tag"] in {"CACHE","MODEL"}:
        # CACHE is opaque even when its field names do not use "cache".
        result["whole_cache_or_model_record"] = {
            "literal_JSON_bytes": record["JSON_bytes"],
            "literal_JSON_sha256": record["JSON_sha256"],
            "literal_JSON_plus_LF_bytes": record["JSON_plus_LF_bytes"],
            "literal_JSON_plus_LF_sha256": record["JSON_plus_LF_sha256"],
            **canonical_fingerprint(data)}
        result["original_header"] = {
            key: projector.view(value, (key,))
            for key, value in data.items()
            if scalar(value) or key in
            ("metadata", "manifest", "receipt", "binding", "source_identity")}
        result["checkpoint_cache_payloads"] = checkpoint_cache_manifest(data)
        result["source_identity_leaves"] = provenance(data)
        result["payload_not_printed"] = True
        return result
    if record["tag"] == "COMPLETE":
        result["original_short_outcome"] = {
            key: SemanticView(level=level).view(data[key],(key,))
            for key in ("status","error","final_selection_validation",
                        "actual_value_account","terminal_information_state",
                        "selected_two_grid_physical_point","final_actual_gate_booleans",
                        "accepted_cache_stdout_receipt","current_model_stdout_receipt",
                        "ledger_before_final_report")
            if key in data and key!="ledger_before_final_report"}
    if record["tag"] == "FINAL_CLOCK":
        result["original_short_clock"] = {
            key:value for key,value in data.items() if scalar(value)}
        raw_ledger=data.get("ledger",{})
        result["original_short_clock"]["ledger"] = {
            key:value for key,value in raw_ledger.items()
            if scalar(value) or key in ("started_counts","limits","old_backend_calls","value_account")}
    result["original_semantics"] = projector.view(data)
    result["checkpoint_cache_payloads"] = checkpoint_cache_manifest(data)
    if record["tag"] in {
            "INPUT", "JET_INPUT", "COMPLETE", "FINAL_CLOCK", "REQUEST",
            "PRIOR_WORK_REUSED", "PUBLIC_PULL", "PRIVATE_PULL"}:
        result["source_identity_leaves"] = provenance(data)
    if projector.omissions:
        result["semantic_omission_count"] = len(projector.omissions)
    return result


def build_semantic_report(base: dict[str, Any], records: list[dict[str, Any]],
                          parse_errors: list[dict[str, Any]],
                          parse_info: dict[str, Any], *,
                          level: int) -> dict[str, Any]:
    report = dict(base)
    report["projection_level"] = level
    report["parse"] = {key: value for key, value in parse_info.items()
                       if key != "non_record_failure_tail"}
    report["parse_errors"] = parse_errors
    report["record_fingerprints"] = [record_identity(row) for row in records]
    report["records"] = [record_view(row, level=level) for row in records]
    report["literal_receipt_comparisons"] = receipt_checks(records)
    complete = [row for row in records if row["tag"] == "COMPLETE"]
    clocks = [row for row in records if row["tag"] == "FINAL_CLOCK"]
    duplicates = {name: sum(row["tag"] == name for row in records)
                  for name in UNIQUE_TAGS
                  if sum(row["tag"] == name for row in records) > 1}
    report["duplicate_unique_records"] = duplicates
    report["research_outcome_records"] = [
        {"sequence": row["sequence"], "tag": row["tag"],
         "original_status_fields": original_status_fields(row["data"])}
        for row in records
        if row["tag"] in {"COMPLETE", "FINAL_CLOCK", "REPORTING_ERROR"}]
    report["completion_record_present"] = bool(complete)
    report["final_clock_present"] = bool(clocks)
    report["final_clock_is_authoritative_for_scientific_account"] = bool(clocks)
    report["observer_success_does_not_claim_scientific_success"] = True
    report["status"] = (
        "original-log-read-with-record-errors" if parse_errors or duplicates else
        "original-log-read-complete" if complete and clocks else
        "original-log-read-partial")
    if not complete or base.get("source", {}).get("research_conclusion") != "success":
        report["bounded_non_record_failure_tail"] = (
            parse_info.get("non_record_failure_tail", [])[-12:])
    return report


def fetch_one_log(api: Any, job_id: str) -> tuple[bytes, int]:
    url = reader.API + "/repos/" + REPO + "/actions/jobs/" + job_id + "/logs"
    data, location = api.get(url, LOG_CAP, api_auth=True)
    redirects = 0
    while location is not None:
        redirects += 1
        require(redirects <= 4, "too many log redirects")
        data, location = api.get(location, LOG_CAP, api_auth=False)
    require(data is not None, "empty log response")
    return data, redirects


def source_identity_checks(records: list[dict[str, Any]], *,
                           run_id: str, source_commit: str) -> list[dict[str, Any]]:
    result = []
    # Nested ancestor identities intentionally differ and are never compared
    # against this new source. Only explicit top-level producer fields count.
    for row in records:
        if row["tag"] not in {"COMPLETE", "FINAL_CLOCK", "REQUEST"}:
            continue
        obj = row["data"]
        for key, expected in (
                ("github_sha", source_commit), ("github_run_id", run_id)):
            if key in obj:
                observed = str(obj[key])
                result.append({
                    "record_sequence": row["sequence"], "field": key,
                    "observed": observed, "expected": expected,
                    "matches": observed == expected})
        if row["tag"] == "REQUEST" and "source_commit" in obj:
            result.append({
                "record_sequence": row["sequence"], "field": "source_commit",
                "observed": obj["source_commit"], "expected": source_commit,
                "matches": obj["source_commit"] == source_commit})
        if "policy" in obj:
            result.append({
                "record_sequence": row["sequence"], "field": "policy",
                "observed": obj["policy"], "expected": POLICY,
                "matches": obj["policy"] == POLICY})
    return result


def output_target(value: str | None) -> Path | None:
    if value is None:
        return None
    temp = os.environ.get("RUNNER_TEMP")
    require(bool(temp), "--output requires RUNNER_TEMP")
    base = Path(temp).resolve()
    given = Path(value)
    path = (given if given.is_absolute() else base / given).resolve()
    require(path != base and base in path.parents,
            "--output must be a file below RUNNER_TEMP")
    require(not path.exists() or path.is_file(),
            "--output cannot replace a non-file")
    return path


def own_source_metadata() -> dict[str, Any]:
    result = {}
    for name, filename in (
            ("observer", __file__), ("read_original_actions_log", reader.__file__)):
        path = Path(filename)
        raw = path.read_bytes()
        result[name] = {"filename": path.name, "bytes": len(raw),
                        "sha256": digest(raw)}
    return result


def emit_report(report: dict[str, Any], target: Path | None) -> None:
    report["observer_seconds_not_added_to_research_account"] = time.monotonic() - STARTED
    raw = reader.encoded(report)
    require(len(raw) + len(REPORT_TAG.encode("ascii")) + 2 <= REPORT_CAP,
            "semantic report exceeds bounded stdout cap")
    if target is not None:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw + b"\n")
    sys.stdout.buffer.write(REPORT_TAG.encode("ascii") + b" " + raw + b"\n")
    sys.stdout.buffer.flush()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read one completed fresh54-model-exchange job log without recomputation.")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--job-id", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--workflow", required=True,
                        help="Exact repository-relative workflow path at the research source.")
    parser.add_argument("--expected-log-bytes", type=int)
    parser.add_argument("--expected-log-sha256")
    parser.add_argument("--output",
                        help="Optional compact JSON report path below RUNNER_TEMP.")
    args = parser.parse_args()
    report: dict[str, Any] = {
        "schema": SCHEMA, "policy": POLICY, "status": "observer-started",
        "repository": REPO,
        "scientific_imports": 0, "scientific_recomputations": 0,
        "original_job_log_downloads": 0,
        "original_job_log_reads_completed": 0,
        "raw_log_or_cache_written_to_artifact_git_release": False,
        "large_checkpoint_cache_or_dense_arrays_forwarded": False,
        "research_numbers_selected_without_repair_or_recalculation": True,
        "literal_hashes_distinct_from_canonical_subtree_hashes": True,
        "source_log_cap_bytes": LOG_CAP, "report_cap_bytes": REPORT_CAP,
        "observer_workflow_commit": os.environ.get("GITHUB_SHA"),
        "observer_workflow_run_id": os.environ.get("GITHUB_RUN_ID"),
    }
    target: Path | None = None
    records: list[dict[str, Any]] = []
    try:
        require(args.run_id.isdigit() and int(args.run_id) > 0, "invalid --run-id")
        require(args.job_id.isdigit() and int(args.job_id) > 0, "invalid --job-id")
        require(HEX40.fullmatch(args.source_commit) is not None,
                "invalid --source-commit")
        require(args.workflow.startswith(".github/workflows/")
                and args.workflow.endswith((".yml", ".yaml"))
                and ".." not in Path(args.workflow).parts
                and "@" not in args.workflow,
                "invalid repository-relative --workflow")
        if args.expected_log_bytes is not None:
            require(0 < args.expected_log_bytes <= LOG_CAP,
                    "invalid --expected-log-bytes")
        if args.expected_log_sha256 is not None:
            require(HEX64.fullmatch(args.expected_log_sha256) is not None,
                    "invalid --expected-log-sha256")
        report["requested_source"] = {
            "run_id": args.run_id, "job_id": args.job_id,
            "source_commit": args.source_commit, "workflow": args.workflow,
            "expected_log_bytes": args.expected_log_bytes,
            "expected_log_sha256": args.expected_log_sha256}
        target = output_target(args.output)
        report["observer_sources"] = own_source_metadata()
        api = reader.GitHubReader(REPO)
        run = api.api_json("/actions/runs/" + args.run_id)
        job = api.api_json("/actions/jobs/" + args.job_id)
        require(str(run.get("id")) == args.run_id
                and run.get("head_sha") == args.source_commit,
                "source run identity differs")
        observed_workflow = str(run.get("path", "")).split("@", 1)[0]
        require(observed_workflow == args.workflow,
                "source workflow path differs")
        require(str(job.get("id")) == args.job_id
                and str(job.get("run_id")) == args.run_id
                and job.get("head_sha") == args.source_commit,
                "source job identity differs")
        require(job.get("status") == "completed",
                "source job is not completed; no polling or partial live-log read")
        report["source"] = {
            "repository": REPO, "run_id": args.run_id, "job_id": args.job_id,
            "source_commit": args.source_commit, "workflow": args.workflow,
            "job_name": job.get("name"),
            "run_url": run.get("html_url"), "job_url": job.get("html_url"),
            "research_status": job.get("status"),
            "research_conclusion": job.get("conclusion"),
            "research_started_at": job.get("started_at"),
            "research_completed_at": job.get("completed_at"),
            "workflow_status_observed": run.get("status"),
            "workflow_conclusion_observed": run.get("conclusion"),
            "workflow_may_still_be_running_the_read_only_report": True}
        # One request chain, no retries, alternate endpoints, or artifact reads.
        report["original_job_log_downloads"] = 1
        raw, redirects = fetch_one_log(api, args.job_id)
        report["original_job_log_reads_completed"] = 1
        raw_sha = digest(raw)
        report["source"].update({
            "raw_log_bytes": len(raw), "raw_log_sha256": raw_sha,
            "redirects_without_authorization": redirects,
            "read_once_in_memory": True,
            "original_raw_bytes_including_any_BOM_are_hashed": True,
            "raw_log_not_written": True})
        if args.expected_log_bytes is not None:
            require(len(raw) == args.expected_log_bytes,
                    "original raw log byte count differs")
        if args.expected_log_sha256 is not None:
            require(raw_sha == args.expected_log_sha256,
                    "original raw log SHA256 differs")
        records, parse_errors, parse_info = parse_records(raw)
        checks = source_identity_checks(
            records, run_id=args.run_id, source_commit=args.source_commit)
        report["producer_identity_checks"] = checks
        report["producer_identity_mismatch"] = any(
            not check["matches"] for check in checks)
        require(bool(records) or bool(parse_errors),
                "no fresh54-model-exchange source record found")
        # Reprojection only selects already parsed values; it is never a second
        # log fetch, numerical recomputation, or changed scientific outcome.
        chosen = None
        for level in (0, 1, 2):
            candidate = build_semantic_report(
                report, records, parse_errors, parse_info, level=level)
            if len(reader.encoded(candidate)) < REPORT_CAP - 65536:
                chosen = candidate
                break
        if chosen is None:
            # Preserve every source record's identity plus already-emitted
            # outcome/source/clock fields. Oversized semantic detail is stated,
            # never silently represented as an absent scientific event.
            chosen = dict(report)
            chosen.update({
                "status": "original-log-read-semantic-size-limit",
                "semantic_detail_omitted_due_to_output_cap": True,
                "record_fingerprints": [record_identity(row) for row in records],
                "parse_errors": parse_errors,
                "parse": {k: v for k, v in parse_info.items()
                          if k != "non_record_failure_tail"},
                "records": [
                    record_view(row, level=2) if row["tag"] in
                    {"COMPLETE", "FINAL_CLOCK", "INPUT", "CACHE"} else
                    {"identity": record_identity(row),
                     "original_status_fields": original_status_fields(row["data"]),
                     "canonical_payload": canonical_fingerprint(row["data"]),
                     "detail_remains_in_original_stdout": True}
                    for row in records],
                "scientific_outcome_not_changed": True})
        # This extreme guard prevents oversized stdout even for a malformed
        # source producing an unbounded number of tiny records.
        if len(reader.encoded(chosen)) >= REPORT_CAP - 65536:
            manifest = [record_identity(row) for row in records]
            chosen = dict(report)
            chosen.update({
                "status": "observer-output-cap-exceeded",
                "scientific_status_not_reclassified": True,
                "all_record_identity_manifest": canonical_fingerprint(manifest),
                "original_record_count": len(records),
                "parse_error_count": len(parse_errors),
                "outcome_records": [
                    {"identity": record_identity(row),
                     "original_status_fields": original_status_fields(row["data"]),
                     "canonical_payload": canonical_fingerprint(row["data"])}
                    for row in records
                    if row["tag"] in {"COMPLETE", "FINAL_CLOCK", "REPORTING_ERROR"}],
                "full_manifest_and_semantics_remain_in_original_job_log": True})
        report = chosen
        emit_report(report, target)
        return 1 if (report.get("producer_identity_mismatch")
                     or parse_errors
                     or report.get("duplicate_unique_records")
                     or report.get("status") == "observer-output-cap-exceeded") else 0
    except Exception as error:
        # No traceback/HTTP URL/token is printed. Existing source identities and
        # parsed outcome metadata survive a readback failure.
        report["status"] = "read-only-observer-failure"
        report["observer_error"] = {
            "type": type(error).__name__, "message": str(error)[:1000]}
        if records:
            report["record_fingerprints"] = [record_identity(row) for row in records]
            report["outcome_records"] = [
                {"identity": record_identity(row),
                 "original_status_fields": original_status_fields(row["data"]),
                 "canonical_payload": canonical_fingerprint(row["data"])}
                for row in records if row["tag"] in
                {"COMPLETE", "FINAL_CLOCK", "REPORTING_ERROR"}]
        if len(reader.encoded(report)) >= REPORT_CAP - 65536:
            report = {
                "schema": SCHEMA, "policy": POLICY,
                "status": "read-only-observer-failure",
                "observer_error": {"type": type(error).__name__,
                                   "message": str(error)[:1000]},
                "scientific_imports": 0, "scientific_recomputations": 0,
                "oversized_failure_context": canonical_fingerprint(report)}
        # If the optional output write itself failed, do not attempt it again.
        # The bounded failure record must still reach ordinary stdout.
        emit_report(report, None)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
