#!/usr/bin/env python3
"""Host the single complete R1037 input; preserve full evidence in Actions logs.

Only source, parameters, and hashes enter git. This host performs no mathematics.
It authenticates the exact source set and streams both child pipes safely, so the
complete finite-spectrum records are retained without repository output files.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

REPO = "Rogerhu12/math-research-public"
PREFIX = "topics/rank2-sha-infinitely-many-p/"
WORKFLOW = ".github/workflows/rank2-sha-degree378-complete-spectrum.yml"
WORKFLOW_SHA256 = "70e970500ad9bff262b874e1fc664d08b192f70d8ce310314b6f36ac2feb4867"
SCRIPT = PREFIX + "scripts/check-original-degree378-complete-spectrum.py"
REQUEST = PREFIX + "ci/original-degree378-complete-spectrum-request.json"
TIME_LIMIT = 3300
MARKERS = {
    "R1037_COMPLETE_SOURCE_COORDINATES",
    "R1037_COMPLETE_MASS_ZERO_CANONICAL",
    "R1037_COMPLETE_SPECTRUM_REPORT",
}
MAX_LINE_BYTES = 16 * 1024 * 1024


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def emit(tag, value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"))
    encoded = encoded.replace("##[", "\\u0023\\u0023[").replace("::", "\\u003a\\u003a")
    print(tag + " " + encoded, flush=True)


def terminate_group(process):
    if process.poll() is not None:
        return
    os.killpg(process.pid, signal.SIGTERM)
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait(timeout=5)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPO:
        raise RuntimeError("This source host requires the named public Actions repository.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    args = parser.parse_args()
    if args.request != REQUEST:
        raise RuntimeError("The request path is not the fixed complete-spectrum input.")
    root = Path(os.environ["RANK2_SPECTRUM_DIR"]).resolve()
    if Path.cwd().resolve() != root:
        raise RuntimeError("The host is not in the fixed detached source checkout.")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip()
    if head != os.environ["GITHUB_SHA"]:
        raise RuntimeError("The detached checkout differs from the current public run source.")
    workflow = subprocess.check_output(["git", "show", "HEAD:" + WORKFLOW], cwd=root)
    if sha(workflow) != WORKFLOW_SHA256:
        raise RuntimeError("The fixed workflow identity differs.")
    raw_request = (root / REQUEST).read_bytes()
    request = json.loads(raw_request)
    if request.get("schema") != "rank2-original-degree378-complete-spectrum-v1" or \
            request.get("workers") != 4 or request.get("python_flint_version") != "0.9.0" or \
            request.get("time_limit_seconds") != TIME_LIMIT or \
            request.get("workflow_sha256") != WORKFLOW_SHA256:
        raise RuntimeError("The complete-spectrum resource/source parameters differ.")
    if request.get("original390_necessary_CM_norms") != [7, 19] or \
            request.get("new378_complete_CM_norms") != [13, 19, 31]:
        raise RuntimeError("The complete old/new operator domains differ.")
    for field in ("require_all_original_columns_and_extra_fibers",
                  "require_complete_delta_old_and_seven_old",
                  "require_original_absolute_phase_anchors",
                  "no_generated_coefficient_inputs", "no_generated_output_files"):
        if request.get(field) is not True:
            raise RuntimeError("A required complete-domain gate is missing: " + field)
    pins = request["expected_source_pins"]
    expected_names = {
        "check-original-degree378-complete-spectrum.py",
        "launch-original-degree378-complete-spectrum.py",
        "check-r480-actual-input-cm19.py",
        "check-r466-fixed-two-division-source.py",
        "check-r464-degree102-cm7-exact.py",
    }
    if set(pins) != expected_names:
        raise RuntimeError("The fixed complete source set differs.")
    manifest = {}
    for name, expected in sorted(pins.items()):
        raw = (root / (PREFIX + "scripts/" + name)).read_bytes()
        if sha(raw) != expected:
            raise RuntimeError("A complete source pin differs: " + name)
        manifest[name] = {"bytes": len(raw), "sha256": expected}

    command = [sys.executable, str(root / SCRIPT), "--workers", "4", "--request", REQUEST]
    emit("RANK2_DEGREE378_HOST", {
        "stage": "complete input started", "source_commit": head,
        "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "request_id": request["request_id"], "request_sha256": sha(raw_request),
        "workflow_sha256": WORKFLOW_SHA256, "source_manifest": manifest,
        "workers": 4, "time_limit_seconds": TIME_LIMIT,
        "original_heavy_v10_workflow_modified_or_restarted": False,
    })
    process = subprocess.Popen(command, cwd=root, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, start_new_session=True)
    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ, "stdout")
    selector.register(process.stderr, selectors.EVENT_READ, "stderr")
    pending = {"stdout": b"", "stderr": b""}
    digests = {"stdout": hashlib.sha256(), "stderr": hashlib.sha256()}
    sizes = {"stdout": 0, "stderr": 0}
    records = {marker: [] for marker in MARKERS}
    summaries = []
    started = time.monotonic()
    timed_out = False

    def consume(stream, raw):
        if not raw:
            return
        line = raw.decode("utf-8", errors="strict").rstrip("\r")
        if stream == "stdout":
            value = json.loads(line)
            summaries.append(value)
            emit("RANK2_DEGREE378_SUMMARY", value)
            return
        marker, separator, payload = line.partition(" ")
        if separator and marker in MARKERS:
            value = json.loads(payload)
            payload_bytes = payload.encode()
            records[marker].append({
                "payload_bytes": len(payload_bytes), "payload_sha256": sha(payload_bytes),
                "name": value.get("name"),
            })
            emit(marker, value)
        else:
            emit("RANK2_DEGREE378_PROGRESS", {"stream": stream, "line": line})

    try:
        while selector.get_map():
            if time.monotonic() - started > TIME_LIMIT:
                timed_out = True
                terminate_group(process)
            for key, _ in selector.select(timeout=1):
                stream = key.data
                chunk = os.read(key.fileobj.fileno(), 65536)
                if not chunk:
                    selector.unregister(key.fileobj)
                    consume(stream, pending[stream])
                    pending[stream] = b""
                    continue
                digests[stream].update(chunk)
                sizes[stream] += len(chunk)
                parts = (pending[stream] + chunk).split(b"\n")
                pending[stream] = parts.pop()
                if len(pending[stream]) > MAX_LINE_BYTES:
                    raise RuntimeError("A complete record exceeded its explicit line byte bound.")
                for line in parts:
                    if len(line) > MAX_LINE_BYTES:
                        raise RuntimeError("A complete record exceeded its explicit line byte bound.")
                    consume(stream, line)
        returncode = process.wait(timeout=5)
    finally:
        selector.close()
        terminate_group(process)
        process.stdout.close()
        process.stderr.close()

    full = records["R1037_COMPLETE_SPECTRUM_REPORT"]
    source_records = records["R1037_COMPLETE_SOURCE_COORDINATES"]
    complete = not timed_out and returncode == 0 and len(summaries) == 1 and \
        len(full) == 1 and len(source_records) == 2
    if complete:
        summary = summaries[0]
        complete = summary.get("status") == "PASS" and \
            summary.get("complete_exact_report_in_stderr_sha256") == full[0]["payload_sha256"] and \
            summary.get("generated_coefficients_read_from_files") is False and \
            summary.get("generated_files_written") is False
    emit("RANK2_DEGREE378_HOST_RESULT", {
        "status": "COMPLETE_ORIGINAL_SPECTRUM" if complete else "INCOMPLETE",
        "source_commit": head, "run_id": int(os.environ["GITHUB_RUN_ID"]),
        "request_id": request["request_id"], "request_sha256": sha(raw_request),
        "script": SCRIPT, "script_sha256": manifest[Path(SCRIPT).name]["sha256"],
        "host_sha256": manifest[Path(__file__).name]["sha256"],
        "workflow_sha256": WORKFLOW_SHA256, "exit_code": returncode,
        "timed_out": timed_out, "elapsed_seconds": time.monotonic() - started,
        "raw_child_streams": {
            name: {"bytes": sizes[name], "sha256": digests[name].hexdigest()}
            for name in ("stdout", "stderr")
        },
        "complete_record_identities": records,
        "full_report_hash_matches_summary": complete,
        "all_generated_results_retained_only_in_public_job_logs": True,
        "original_heavy_v10_workflow_modified_or_restarted": False,
        "mathematical_verdict_inferred_from_partial_progress": False,
    })
    if not complete:
        raise SystemExit(124 if timed_out else returncode or 2)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        emit("RANK2_DEGREE378_HOST_FAILED", {
            "error_type": type(exc).__name__, "message": str(exc),
            "mathematical_status": "NOT_CERTIFIED_BY_HOST",
        })
        raise
