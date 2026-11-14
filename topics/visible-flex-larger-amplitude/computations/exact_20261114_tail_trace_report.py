#!/usr/bin/env python3
"""Read original tail/driver records without executing or modifying a solver.

This diagnostic consumes actual trace, trial, stderr, complete response,
cache-import and full-DN driver-status records. It retains observed failure
stage/root/line-search messages and original elapsed times. A saved accepted
trial is not promoted to a converged tail; an imported zero response is not
counted as a new worker solve. Missing final responses alone do not identify
an OOM, timeout or live process. No mathematical gate or setting is changed.

Run on this public repository's Actions, including in an always() step after
an unsuccessful full-DN command. All original files remain untouched.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import re


RESPONSE_NAME = re.compile(r".+_[0-9]{4}\.json(?:\.gz)?$")
MAX_STORED_JSON = 8_000_000
MAX_UNCOMPRESSED_JSON = 64_000_000
MAX_EVENT_LINE = 1_000_000
EVENT_KEYS = ("time", "event", "call", "elapsed_ms", "iteration", "norm", "minA", "minD",
              "phase", "chartCondition", "acceptedFromIteration", "acceptedTrial", "acceptedStep",
              "step", "trial", "kind", "baseNorm", "trialNorm", "stage", "rawCell", "rawSegment",
              "backend", "predictor", "maxChartCondition", "error", "converged", "residual")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(262144), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pick(record, keys):
    return {key: record[key] for key in keys if key in record}


def small_event(record):
    result = pick(record, EVENT_KEYS)
    if isinstance(result.get("error"), str) and len(result["error"]) > 8000:
        result["error"] = result["error"][:8000] + " [report excerpt; original retained]"
    return result


def read_json(path):
    if path.stat().st_size > MAX_STORED_JSON:
        raise ValueError("Stored JSON exceeds the diagnostic reader limit")
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if raw[:2] == b"\x1f\x8b":
        import io
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
            plain = stream.read(MAX_UNCOMPRESSED_JSON + 1)
    else:
        plain = raw
    if len(plain) > MAX_UNCOMPRESSED_JSON:
        raise ValueError("Expanded JSON exceeds the diagnostic reader limit")
    return json.loads(plain), digest


def event_log(path, label, issues):
    counts, calls, recent = Counter(), {}, deque(maxlen=32)
    line_count, malformed = 0, 0
    with path.open("rb") as stream:
        while True:
            line = stream.readline(MAX_EVENT_LINE + 1)
            if not line:
                break
            line_count += 1
            if len(line) > MAX_EVENT_LINE:
                while line and not line.endswith(b"\n"):
                    line = stream.readline(MAX_EVENT_LINE + 1)
                malformed += 1
                issues.append(dict(file=label, line=line_count, issue="Oversized original event retained, not parsed"))
                continue
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError("Event is not an object")
            except Exception as error:
                malformed += 1
                issues.append(dict(file=label, line=line_count, issue=repr(error)))
                continue
            kind = row.get("event", row.get("kind", "unlabelled"))
            counts[str(kind)] += 1
            recent.append(small_event(row))
            if "call" not in row:
                continue
            key = str(row["call"])
            call = calls.setdefault(key, dict(original_call=row["call"], event_counts=Counter(),
                                             recent_iterations=deque(maxlen=16), recent_trials=deque(maxlen=16)))
            call["event_counts"][str(kind)] += 1
            if row.get("event") == "request":
                call["request"] = pick(row, ("time", "height", "jacobian", "audit"))
            if row.get("event") == "iteration":
                call["recent_iterations"].append(small_event(row))
            if "kind" in row:
                call["recent_trials"].append(small_event(row))
            if row.get("event") in ("response", "failure", "tangent_predictor_ready", "tangent_predictor_unavailable"):
                call[row["event"]] = small_event(row)
    summaries = []
    for call in calls.values():
        for key in ("recent_iterations", "recent_trials"):
            call[key] = list(call[key])
        call["event_counts"] = dict(call["event_counts"])
        call["request_without_recorded_final_response"] = "request" in call and "response" not in call and "failure" not in call
        summaries.append(call)
    return dict(file=label, sha256=sha(path), bytes=path.stat().st_size, lines=line_count,
                malformed_or_unread_lines=malformed, event_counts=dict(counts), calls=summaries,
                recent_events=list(recent))


def response_summary(path, label):
    record, digest = read_json(path)
    response = record["response"]
    checkpoint = response.get("checkpoint") or {}
    parameters = checkpoint.get("parameters") or {}
    state = checkpoint.get("states") or []
    J = response.get("heightJetJacobian")
    jets = response.get("jets") or {}
    sources = record.get("source_sha256") or {}
    return dict(file=label, sha256=digest, bytes=path.stat().st_size,
                request=record.get("request"), original_request_seconds=record.get("seconds"),
                original_returned_status=pick(response, ("converged", "failed", "residual", "actual_nonlinear_solve",
                                                        "finite_tail_only", "lastIteration")),
                original_audit=response.get("audit"), original_history=response.get("history"),
                original_J_method=response.get("heightJetJacobianMethod"),
                original_endpoint_J_diagnostics=response.get("endpointJacobianDiagnostics"),
                complete_J_entry_count=len(J) if isinstance(J, list) else None,
                saved_state_count=len(state), saved_state_width=len(state[0]) if state else None,
                original_cut_height=checkpoint.get("cutHeight"),
                finite_parameters=pick(parameters, ("modes", "spacing", "quadrature", "steps", "auditSteps",
                                                    "physicalDepth", "depth", "shootingParts", "linearFar",
                                                    "linearSteps", "projectionFloor", "solveTolerance")),
                original_cut_scalars=pick(jets, ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep",
                                                "meanSlope", "meanSecond", "meanSlopeCorrection", "meanSecondCorrection",
                                                "minLeading", "minD", "endpointFullD", "endpointPhi")),
                source_inventory_count=len(sources),
                source_inventory_sha256=hashlib.sha256(json.dumps(sources, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
                checkpoint_scope=checkpoint.get("scope"))


def stderr_summary(path, label):
    with path.open("rb") as stream:
        stream.seek(max(0, path.stat().st_size - 12000))
        tail = stream.read().decode("utf-8", errors="replace")
    return dict(file=label, sha256=sha(path), bytes=path.stat().st_size,
                excerpt_is_terminal_12000_bytes=True, excerpt=tail,
                observed_messages={key: key in tail for key in (
                    "JavaScript heap out of memory", "Reached heap limit", "Allocation failed",
                    "momentum branch D/S/A rejected", "momentum Newton", "multiple-shooting line search failed",
                    "tail graph chart singular", "SIGKILL", "SIGTERM")},
                inference_limit="Only literal messages are classified. An absent response or killed process alone does not establish a cause.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--response-limit", type=int, default=64,
                        help="Maximum saved complete response records to parse; omitted files remain inventoried")
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise ValueError("Tail diagnostics belong to this public repository GitHub Actions")
    if args.response_limit < 1 or args.out.exists():
        raise ValueError("Use a positive response limit and a new output path")
    root = args.directory.resolve()
    files = sorted(path for path in root.rglob("*") if path.is_file()) if root.is_dir() else []
    issues, traces, trials, responses, stderrs, imports, uses, drivers, inventory = [], [], [], [], [], [], [], [], []
    complete_response_paths = [path for path in files if RESPONSE_NAME.fullmatch(path.name)]
    selected_responses = set(complete_response_paths[-args.response_limit:])
    if len(complete_response_paths) > args.response_limit:
        issues.append(dict(issue="Earlier complete responses omitted only from this bounded report",
                           original_count=len(complete_response_paths), parsed_count=args.response_limit))
    for path in files:
        label = str(path.relative_to(root))
        name = path.name
        relevant = (name.endswith(("_trace.jsonl", "_trials.jsonl", "_stderr.log", "_imported-zero.json",
                                   "_imported-zero-uses.jsonl"))
                    or RESPONSE_NAME.fullmatch(name) or name == "driver-status.json")
        if not relevant:
            continue
        inventory.append(dict(file=label, bytes=path.stat().st_size, sha256=sha(path)))
        try:
            if name.endswith("_trace.jsonl"):
                traces.append(event_log(path, label, issues))
            elif name.endswith("_trials.jsonl"):
                trials.append(event_log(path, label, issues))
            elif name.endswith("_stderr.log"):
                stderrs.append(stderr_summary(path, label))
            elif name.endswith("_imported-zero-uses.jsonl"):
                use = event_log(path, label, issues)
                use["new_worker_solves_from_these_archive_uses"] = 0
                uses.append(use)
            elif name.endswith("_imported-zero.json"):
                value, digest = read_json(path)
                imports.append(dict(file=label, sha256=digest, original_record=pick(value, (
                    "schema", "adapter_sha256", "imported_sha256", "prior_public_commit", "current_public_commit",
                    "modes", "quadrature", "full_J_entries", "complete_original_audit", "original_residual",
                    "original_worker_exit_code", "original_response_not_modified", "server_tangent_predictor_imported",
                    "nonzero_height_rounding", "audited_request_can_use_imported_cache", "task_completed"))))
            elif name == "driver-status.json":
                value, digest = read_json(path)
                drivers.append(dict(file=label, sha256=digest, original_status=pick(value, (
                    "phase", "nodes", "state_dimension", "physical_state_dimension", "left_rows", "right_rows",
                    "current_outer_iteration", "outer_history", "exception", "traceback", "elapsed_seconds",
                    "physical_RMS_max", "physical_node_relative_residual", "new_coupled_finite_acceptance",
                    "full_Cartesian_closed_surface", "actual_result_sha256", "height_seam"))))
            elif path in selected_responses:
                responses.append(response_summary(path, label))
        except Exception as error:
            issues.append(dict(file=label, issue=repr(error), original_file_preserved=True))
    result = dict(
        schema="original-tail-record-diagnostic-v1", generated_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__), directory=str(root), input_directory_exists=root.is_dir(),
        github_run_id=os.environ.get("GITHUB_RUN_ID"), github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        original_file_inventory=inventory, original_driver_status=drivers,
        actual_worker_traces=traces, actual_trial_diagnostics=trials, complete_saved_responses=responses,
        original_stderr=stderrs, actual_archive_imports=imports, archive_use_logs=uses,
        diagnostic_read_issues=issues, diagnostic_complete=not issues,
        no_solver_executed=True, original_files_modified=False, no_acceptance_threshold_changed=True,
        no_new_numerical_acceptance_claim=True, task_completed=False,
        limitations=[
            "This report preserves recorded values; it does not rerun root, ODE, Jacobian, metric or BVP calculations.",
            "An accepted trial/iteration checkpoint remains unaccepted until the original full variational and nonlinear gates finish.",
            "Imported completed zero-H responses are separate from new actual worker requests.",
            "The original trace reports iterations after full stage passes; absence of finer progress does not imply a stalled process.",
            "A request without a final response can be running, interrupted, terminated or incompletely copied; this report alone cannot choose the cause.",
            "Large finite chart conditions and actual audit values are retained without changing acceptance or replacing the real J by a ready reference.",
            "Only bounded recent iteration/trial excerpts are repeated here; all original logs are inventoried by byte hash."])
    raw = (json.dumps(result, indent=2, allow_nan=False) + "\n").encode()
    if args.out.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
        if len(raw) >= 5_000_000:
            raise ValueError("Compressed diagnostic unexpectedly exceeds the repository file limit")
    elif len(raw) >= 1_000_000:
        raise ValueError("Use a .json.gz output for this larger diagnostic; original files remain untouched")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("xb") as stream:
        stream.write(raw)
    print(json.dumps(dict(output=str(args.out), actual_saved_responses=len(responses),
                          original_trace_files=len(traces), imported_zero_uses=sum(x["lines"] for x in uses),
                          diagnostic_complete=not issues, no_new_acceptance_claim=True)), flush=True)


if __name__ == "__main__":
    main()
