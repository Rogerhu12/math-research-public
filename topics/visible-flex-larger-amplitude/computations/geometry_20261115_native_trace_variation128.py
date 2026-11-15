#!/usr/bin/env python3
"""Actions-only, source-bound one-direction R283 finite-trace calculation.

This launcher verifies actual packet bytes, compiles the independent C++
consumer and records the complete temporary result hashes.  It does not
construct a native state, solve for a correction or confer native acceptance.
Raw packet ownership stays with the caller.  All newly generated numerical
payloads and the executable are removed after their identities are recorded.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import traceback


CPP_NAME = "geometry_20261115_native_trace_variation128.cpp"
ORIGINAL_CPP_NAME = "geometry_20261115_native_primal128.cpp"
ORIGINAL_BRIDGE_NAME = "geometry_20261115_native_primal128_bridge.mjs"
ORIGINAL_CPP_SHA = "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d"
ORIGINAL_BRIDGE_SHA = "3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8"
BRIDGE_NAME = "geometry_20261115_native_trace_variation128_bridge.mjs"
SCHEMA = "native-finite-root-trace-direction-launch-summary-v1"
MARKER = "NATIVE_TRACE_VARIATION "


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path, root=None):
    path = Path(path)
    return {"file": path.name if root is None else path.relative_to(root).as_posix(),
            "bytes": path.stat().st_size, "sha256": file_sha(path)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def hash_text(value):
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "Complete SHA256 required")
    return value


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "This new scientific arithmetic runs only in the public repository Actions")


def packet_structure(path):
    """Byte-only parser: hashes each independent literal array and schedule.

    No floating values, trigonometric identities or numerical field are
    evaluated here.  Sizes, offsets and counts describe the binary format.
    The C++ Problem reader enforces its original finite/domain prerequisites.
    """
    size = path.stat().st_size
    records = []
    with path.open("rb") as f:
        def take(count, name, shape=None):
            offset = f.tell()
            remaining = count
            h = hashlib.sha256()
            while remaining:
                block = f.read(min(remaining, 1 << 20))
                require(bool(block), "Truncated actual packet: " + name)
                h.update(block)
                remaining -= len(block)
            item = {"name": name, "offset": offset, "bytes": count, "sha256": h.hexdigest()}
            if shape is not None:
                item.update(shape=shape, dtype="<f8", order="C")
            records.append(item)
            return item

        header = f.read(24)
        require(len(header) == 24 and header[:8] == b"QPR11301", "Frozen113 complete packet format required")
        modes, angles, depth, orientation = struct.unpack("<IIII", header[8:])
        require(modes == 112 and depth == 576 and 896 < angles <= 65536 and orientation in (1, 2),
                "The actual complete 112/224/226/576 packet is required")
        records.append({"name": "header", "offset": 0, "bytes": 24, "sha256": hashlib.sha256(header).hexdigest()})
        take(6 * 8, "original-six-constants", [6])
        take(modes * 8, "frequency", [modes])
        take(angles * (modes + 1) * 8, "cosine", [angles, modes + 1])
        take(angles * modes * 8, "sine", [angles, modes])
        take(angles * (2 * modes + 1) * 8, "gram", [angles, 2 * modes + 1])
        take((depth + 1) * 2 * modes * 8, "states", [depth + 1, 2 * modes])
        take((depth + 1) * 2 * modes * 8, "delta", [depth + 1, 2 * modes])
        take(modes * 8, "target", [modes])
        take((depth + 1) * 8, "scales", [depth + 1])
        take(modes * 8, "far", [modes])
        steps = 0
        cells = []
        for stage in range(depth):
            offset = f.tell()
            cell_header = f.read(20)
            require(len(cell_header) == 20, "Truncated cell header")
            count = struct.unpack("<I", cell_header[16:])[0]
            require(0 < count <= 100000, "Frozen113 original cell count bound")
            h = hashlib.sha256(cell_header)
            remaining = count * 16 * 8
            while remaining:
                block = f.read(min(remaining, 1 << 20))
                require(bool(block), "Truncated cell schedule")
                h.update(block)
                remaining -= len(block)
            cells.append({"stage": stage, "offset": offset, "bytes": 20 + count * 16 * 8,
                          "RK_steps": count, "sha256": h.hexdigest()})
            steps += count
        require(f.tell() == size and not f.read(1), "Unparsed packet suffix")
    return {"schema": "native-finite-root-trace-complete-packet-byte-map-v1", "bytes": size,
            "sha256": file_sha(path), "modes": modes, "quadrature": angles, "depth": depth,
            "orientation_flag": orientation, "records": records, "cells": cells,
            "RK_steps": steps, "geometry_samples": 3 * steps,
            "three_angular_tables_independently_hashed": True,
            "w_w2_E_not_reconstructed_from_each_other": True,
            "scientific_arithmetic_in_this_parser": False}


def bind_packet(args, source_dir):
    packet = args.packet.resolve(strict=True)
    binding_file = args.packet_binding.resolve(strict=True)
    require(file_sha(packet) == hash_text(args.expected_packet_sha256), "Actual complete packet SHA mismatch")
    require(file_sha(binding_file) == hash_text(args.expected_binding_sha256), "Actual complete packet binding SHA mismatch")
    binding = json.loads(binding_file.read_bytes())
    require(binding["schema"] == "native-finite-root-trace-packet-binding-v1", "Independent packet binding schema")
    require(binding["original_cpp_sha256"] == ORIGINAL_CPP_SHA and
            binding["original_packet_writer_bridge_sha256"] == ORIGINAL_BRIDGE_SHA, "Exact original source binding")
    require(binding["source_file"] == BRIDGE_NAME and
            file_sha(source_dir / BRIDGE_NAME) == hash_text(binding["source_sha256"]), "Actual independent packet writer source")
    claimed = binding["packet"]
    require(claimed["file"] == packet.name and claimed["bytes"] == packet.stat().st_size and
            claimed["sha256"] == args.expected_packet_sha256, "Complete actual packet descriptor")
    layout = packet_structure(packet)
    rows = {r["name"]: r for r in layout["records"]}
    for name in ("states", "delta", "target", "scales", "far"):
        require(rows[name]["sha256"] == binding["input_array_sha256"][name], "Complete original input bytes: " + name)
    for name, field in (("cosine", "angular_cosine_sha256"), ("sine", "angular_sine_sha256"), ("gram", "angular_gram_sha256")):
        require(rows[name]["sha256"] == claimed[field], "Independent original literal table: " + name)
    for key, actual in (("RK_steps", layout["RK_steps"]), ("geometry_calls", layout["geometry_samples"]),
                        ("schedule_cell_count", 576), ("shape_dimension", 224),
                        ("complete_state_dimension", 226), ("full_stage_count", 576),
                        ("full_residual_count", 129248), ("quadrature", layout["quadrature"])):
        require(claimed[key] == actual, "Actual packet shape/schedule: " + key)
    identity = binding["actual_call_identity"]
    for key in ("source_sha256", "hook_sha256", "fresh_snapshot_result_sha256", "complete_current_delta_sha256"):
        hash_text(identity[key])
    require(type(identity["native_call"]) is int and identity["native_call"] > 0 and
            type(identity["nonlinear_iteration"]) is int and identity["nonlinear_iteration"] >= 0,
            "Actual source call and current nonlinear iteration identity")
    require(identity["original_cuspAwareFlow"] is True, "Original literal cusp schedule identity")
    for name, key in (("states", "base-states"), ("target", "cut-target"),
                      ("scales", "original-scales"), ("far", "original-far-graph")):
        require(rows[name]["sha256"] == identity["complete_current_array_sha256"][key], "Current snapshot packet bytes: " + key)
    require(rows["delta"]["sha256"] == identity["complete_current_delta_sha256"], "Actual complete current direction")
    return packet, binding_file, binding, layout


def owned_out(path):
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    candidate = path.resolve()
    require(candidate != runner and candidate.is_relative_to(runner), "New output must be below actual RUNNER_TEMP")
    require(not candidate.exists() and not candidate.is_symlink(), "Fresh independent output directory required")
    candidate.mkdir(parents=True, exist_ok=False)
    return candidate


def collect_output(work, report):
    """Only filesystem/JSON/hash accounting after the C++ scientific call."""
    items = []
    arrays = {a["file"]: a for a in report.get("arrays", [])}
    trace_count = 0
    root_return_records = 0
    root_failed_records = 0
    for path in sorted(work.iterdir()):
        require(path.is_file() and not path.is_symlink(), "Only owned regular temporary result files")
        item = receipt(path, work)
        if path.name in arrays:
            a = arrays[path.name]
            require(a["bytes"] == item["bytes"] and a["dtype"] == "IEEE754-binary128-little-endian", "Complete binary128 output bytes")
            item.update(shape=a["shape"], dtype=a["dtype"], order=a["order"])
        if path.name.startswith("root-trace-stage-") and path.suffix == ".jsonl":
            trace_count += 1
            count = good = bad = 0
            with path.open("rb") as f:
                for line in f:
                    record = json.loads(line)
                    count += 1
                    require(record["field"] in (0, 1, 2, 3) and 0 <= record["stage"] < 576,
                            "Complete original RK field address")
                    if record["complete_directional_return"]:
                        good += 1
                        require(record["primal_return_selected"] is True and
                                0 <= record["accepted_update_count"] <= 29 and
                                record["return_kind"] in ("normal", "original-fallback"), "Actual successful finite trace")
                    else:
                        bad += 1
            item.update(root_records=count, successful_direction_records=good, failed_direction_records=bad)
            root_return_records += good
            root_failed_records += bad
        items.append(item)
    if report:
        require(set(arrays).issubset({r["file"] for r in items}), "All complete output arrays are present")
        require(root_return_records == report["variation_statistics"]["joint_root_returns"], "All successful root trace records")
    return {"schema": "native-finite-root-trace-temporary-output-manifest-v1", "files": items,
            "file_count": len(items), "root_trace_files": trace_count,
            "successful_root_direction_records": root_return_records,
            "failed_root_direction_records": root_failed_records,
            "array_bytes_are_hashed_not_numerically_recomputed_by_launcher": True,
            "raw_files_will_be_removed_after_manifest_and_compact_summary": True}


def compact_report(report):
    result = {key: value for key, value in report.items() if key != "stage_reports"}
    # This is metadata, not a cap on the scientific stage/RHS/root work.
    stages = report.get("stage_reports", [])
    result["all_stage_accounting"] = [
        {"stage": s["stage"], "complete": s["complete"], "RK_steps": s["RK_steps"],
         "root_calls": s["root"]["calls"], "accepted_updates": s["variation"]["accepted_updates_differentiated"],
         "zero_update_returns": s["variation"]["zero_update_returns"],
         "fallback_returns": s["root"]["fallback_returns"], "error": s["error"]}
        for s in stages]
    result["full_stage_report_is_a_hashed_temporary_result"] = True
    return result


def emit_bounded(summary):
    payload = canonical(summary)
    if len(payload) <= 90000:
        public = summary
    else:
        public = {key: value for key, value in summary.items() if key != "scientific_report"}
        full = summary.get("scientific_report", {})
        public["scientific_report"] = {key: value for key, value in full.items() if key != "all_stage_accounting"}
        public["all_stage_accounting_omitted_only_from_bounded_stdout"] = True
        public["complete_summary_bytes"] = len(payload)
        public["complete_summary_sha256"] = hashlib.sha256(payload).hexdigest()
        if len(canonical(public)) > 90000:
            public = {"schema": SCHEMA, "stdout_size_fallback": True,
                      "complete": summary.get("scientific_report", {}).get("complete", False),
                      "actual_error": summary.get("actual_error"),
                      "source": summary.get("sources"), "run": summary.get("run"),
                      "input_packet": summary.get("input_packet"),
                      "child_exit": summary.get("child_exit"),
                      "complete_summary_bytes": len(payload), "complete_summary_sha256": hashlib.sha256(payload).hexdigest(),
                      "scientific_scalars_not_fabricated_or_zero_filled": True,
                      "native_accepted": False}
    print(MARKER + canonical(public).decode().rstrip("\n"), flush=True)


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--packet-binding", type=Path, required=True)
    parser.add_argument("--expected-packet-sha256", required=True)
    parser.add_argument("--expected-binding-sha256", required=True)
    parser.add_argument("--expected-cpp-sha256", required=True)
    parser.add_argument("--policy", choices=("original", "refined"), required=True)
    parser.add_argument("--state-point", choices=("base", *(f"trial:{k}" for k in range(10))), required=True)
    parser.add_argument("--seconds", type=int, required=True)
    parser.add_argument("--threads", type=int, choices=range(1, 5), required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(60 <= args.seconds <= 14400, "Explicit scientific wall-clock budget 60..14400 seconds")
    source_dir = Path(__file__).resolve().parent
    cpp, original_cpp = source_dir / CPP_NAME, source_dir / ORIGINAL_CPP_NAME
    require(file_sha(cpp) == hash_text(args.expected_cpp_sha256), "Independent consumer C++ source")
    require(file_sha(original_cpp) == ORIGINAL_CPP_SHA, "Included frozen113 primal source")
    require(file_sha(source_dir / ORIGINAL_BRIDGE_NAME) == ORIGINAL_BRIDGE_SHA, "Original packet writer source")
    packet, binding_file, binding, layout = bind_packet(args, source_dir)
    output = owned_out(args.out)
    summary = {"schema": SCHEMA, "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
               "run": {key: os.environ.get(key) for key in ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
               "sources": {"launcher": receipt(Path(__file__).resolve()), "cpp": receipt(cpp),
                           "included_original_cpp": receipt(original_cpp), "packet_writer": receipt(source_dir / BRIDGE_NAME),
                           "original_packet_writer": receipt(source_dir / ORIGINAL_BRIDGE_NAME)},
               "input_packet": receipt(packet), "input_binding": receipt(binding_file),
               "actual_call_identity": binding["actual_call_identity"],
               "command": [sys.executable, *sys.argv],
               "policy": args.policy, "state_point": args.state_point,
               "one_complete_packet_direction_only": True, "native_accepted": False,
               "new_native_solver_or_fullDN_J_or_audit": False, "new_acceptance_gate": False,
               "no_artifact_Release_or_Git_raw_output": True, "actual_error": None}
    layout_file = output / "packet-byte-map.json"
    layout_file.write_bytes(canonical(layout))
    summary["packet_byte_map"] = receipt(layout_file)
    work = Path(tempfile.mkdtemp(prefix="trace-variation-work-", dir=output))
    compile_dir = Path(tempfile.mkdtemp(prefix="trace-variation-build-", dir=output))
    executable = compile_dir / "trace-variation-evaluator"
    report = {}
    returncode = 2
    try:
        compile_command = ["g++", "-O3", "-std=gnu++17", "-fopenmp", "-fno-fast-math", "-ffp-contract=off",
                           "-frounding-math", str(cpp), "-lquadmath", "-o", str(executable)]
        summary["compile_command"] = compile_command
        build_log = output / "compile.log"
        with build_log.open("wb") as log:
            built = subprocess.run(compile_command, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
                                   check=False, timeout=180, env=os.environ.copy())
        summary["compile_exit"] = built.returncode
        summary["compile_log"] = receipt(build_log)
        require(built.returncode == 0 and executable.is_file(), "Independent finite-trace consumer compilation failed")
        summary["executable"] = receipt(executable)
        child_command = [str(executable), str(packet), str(work), str(args.seconds), str(args.threads), args.policy, args.state_point]
        summary["scientific_child_command"] = child_command
        child_log = output / "child.log"
        child_error = None
        with child_log.open("wb") as log:
            try:
                child = subprocess.run(child_command, stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
                                       check=False, timeout=args.seconds + 120,
                                       env={**os.environ, "OMP_NUM_THREADS": str(args.threads)})
                returncode = child.returncode
            except subprocess.TimeoutExpired as error:
                returncode = 3
                child_error = type(error).__name__ + ": " + str(error)
        summary["child_exit"] = {"status": returncode, "timeout_error": child_error}
        summary["child_log"] = receipt(child_log)
        report_file = work / "trace-direction-report.json"
        if report_file.is_file():
            report = json.loads(report_file.read_bytes())
            require(report["schema"] == "native-finite-root-trace-direction-binary128-v1" and
                    report["original_cpp_sha256"] == ORIGINAL_CPP_SHA, "Actual independent complete trace report identity")
            summary["full_scientific_report"] = receipt(report_file)
            summary["scientific_report"] = compact_report(report)
        else:
            summary["scientific_report_missing"] = True
            summary["actual_error"] = "Scientific child did not finish its complete-or-partial report; actual child log retained"
        manifest = collect_output(work, report)
        manifest_file = output / "temporary-output-manifest.json"
        manifest_file.write_bytes(canonical(manifest))
        summary["temporary_output_manifest"] = receipt(manifest_file)
        summary["temporary_output_file_count"] = manifest["file_count"]
        summary["successful_root_direction_records"] = manifest["successful_root_direction_records"]
        summary["failed_root_direction_records"] = manifest["failed_root_direction_records"]
        summary["array_receipts"] = [item for item in manifest["files"] if "dtype" in item]
        require(file_sha(packet) == args.expected_packet_sha256 and file_sha(binding_file) == args.expected_binding_sha256,
                "Independent child did not mutate input packet or binding")
    except Exception as error:
        summary["actual_error"] = repr(error)
        summary["exception_type"] = type(error).__name__
        (output / "launcher-error.log").write_text(traceback.format_exc(), encoding="utf-8")
        summary["error_log"] = receipt(output / "launcher-error.log")
        returncode = 2
        # Preserve byte identities of every completed/partial temporary file,
        # even if parsing a deliberately incomplete final trace line failed.
        summary["partial_temporary_files"] = [receipt(p, work) for p in sorted(work.iterdir()) if p.is_file() and not p.is_symlink()]
    finally:
        shutil.rmtree(work)
        shutil.rmtree(compile_dir)
        summary["owned_numerical_payloads_and_executable_removed"] = True
        summary["caller_input_packet_not_deleted_by_launcher"] = True
        summary_file = output / "summary.json"
        summary_file.write_bytes(canonical(summary))
        emit_bounded(summary)
    return returncode


if __name__ == "__main__":
    raise SystemExit(main())
