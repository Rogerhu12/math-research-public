#!/usr/bin/env python3
"""R493 actual per-H metadata/child orchestration under one original19200s clock.

Only the actual full original64 snapshot can feed the original R273 factor.
Only its new literal/physical packets can feed this call's persistent128 owner.
All large numerical records stay in this job. No historical successful response
is inferred from receipts, and no per-call scientific clock is restarted.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
SCHEMA = "R493-current-H-live128-call-pipeline-v1"
INPUT_SCHEMA = "R493-current-H-live128-call-pipeline-input-v1"
OWNER = "geometry_20261116_live128_same_call_owner.py"
OWNER_SHA = "5c1d4908fe6cca3917ef8ad6ed6269251e29b99efbb81e54b91b4f43391fc3b5"
ASSEMBLER = "geometry_20261116_live128_response_assembly.py"
ASSEMBLER_SHA = "08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb"
QR = "exact_20261116_live128_current576_chain_qr.py"
QR_SHA = "faac8b013b9151ba92760962d4303c847301a9057834e7230ab37ea6d0c04b49"
SYSTEM = "exact_20261116_live128_current576_system.py"
SYSTEM_SHA = "e37b13457b9dd9cbd0e918a2bf98988b5027b49fad5c54ffd824016dd2efa7c2"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")


class ResourceStop(RuntimeError):
    pass


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")+b"\n"


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=file_sha(path))


def checked(desc, root=None):
    supplied = Path(desc["file"])
    require(supplied.is_absolute() and not supplied.is_symlink(),
            "Absolute actual regular input required")
    path = supplied.resolve(strict=True)
    require(path.is_file() and path.stat().st_size == desc["bytes"]
            and file_sha(path) == desc["sha256"], "Actual complete file bytes/SHA")
    if root is not None:
        require(path != root and path.is_relative_to(root), "Same-job owned input")
    return path


def member(root, descriptor):
    relative = Path(descriptor["file"])
    require(not relative.is_absolute() and ".." not in relative.parts,
            "The original member has a contained relative filename")
    path = (root/relative).resolve(strict=True)
    require(path.is_relative_to(root) and not path.is_symlink()
            and path.is_file() and path.stat().st_size == descriptor["bytes"]
            and file_sha(path) == descriptor["sha256"],
            "Complete original member identity")
    return path


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, value):
    with Path(path).open("xb") as f:
        f.write(canonical(value))


def process_identity(pid=None):
    pid = os.getpid() if pid is None else int(pid)
    try:
        raw = Path("/proc", str(pid), "stat").read_text()
    except FileNotFoundError:
        return None
    fields = raw[raw.rfind(")")+2:].split()
    return dict(pid=pid, state=fields[0], ppid=int(fields[1]), pgid=int(fields[2]),
                sid=int(fields[3]), start_ticks=fields[19])


def bind(spec):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Live science belongs only to this public repository Actions")
    require(spec["schema"] == INPUT_SCHEMA and spec["mode"] in ("clock", "factor", "solve-response"),
            "Explicit same-call pipeline mode")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    root = Path(spec["call_directory"]).resolve(strict=True)
    require(root != runner and root.is_relative_to(runner) and root.is_dir(),
            "Existing one real native-call directory")
    require(type(spec["call_number"]) is int and spec["call_number"] >= 1,
            "Actual sequential call number")
    clock_path = checked(spec["job_deadline"], runner)
    clock = read(clock_path)
    require(clock["schema"] == "R493-original-full112-live128-job-deadline-v1"
            and clock["total_seconds"] == 19200
            and type(clock["absolute_monotonic_deadline_ns"]) is int
            and type(clock["readback_cleanup_reserve_seconds"]) is int
            and 60 <= clock["readback_cleanup_reserve_seconds"] <= 600,
            "One original320-minute science clock with its declared final reserve")
    for key in RUN_KEYS:
        require(clock["run"][key] == os.environ.get(key), "Actual original run clock: "+key)
    until = clock["absolute_monotonic_deadline_ns"]-clock["readback_cleanup_reserve_seconds"]*10**9
    def remaining():
        return max(0.0, (until-time.monotonic_ns())/1e9)
    if remaining() <= 0:
        raise ResourceStop("The original scientific deadline is already reached")
    require(set(spec["request"]) == {"jacobian", "audit"}
            and all(type(v) is bool for v in spec["request"].values()),
            "Actual original request flags")
    return root, clock, remaining


def run_child(command, root, label, allowance, record):
    if not math.isfinite(allowance) or allowance <= 0:
        raise ResourceStop("No current original-clock allowance for "+label)
    stdout_path, stderr_path = root/(label+".stdout.log"), root/(label+".stderr.log")
    child = dict(label=label, command=command, start_new_session=False,
                 original_worker_process_group_inherited=True,
                 actual_allowance_seconds=allowance, process=None,
                 actual_returncode=None, reaped=False, resource_timeout=False)
    record["children"].append(child)
    close_file = root/(label+"-process.json")
    with stdout_path.open("xb") as stdout, stderr_path.open("xb") as stderr:
        proc = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                                start_new_session=False, env=os.environ.copy())
        child["process"] = process_identity(proc.pid)
        write(root/(label+"-launch.json"), child)
        try:
            child["actual_returncode"] = proc.wait(timeout=allowance)
        except subprocess.TimeoutExpired:
            child["resource_timeout"] = True
            proc.terminate()
            try:
                child["actual_returncode"] = proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                proc.kill()
                child["actual_returncode"] = proc.wait(timeout=15)
        finally:
            child["reaped"] = proc.poll() is not None
            child["stdout"] = receipt(stdout_path)
            child["stderr"] = receipt(stderr_path)
            child["descendant_quiet_not_inferred_from_parent_reap"] = True
            write(close_file, child)
    if child["resource_timeout"]:
        raise ResourceStop("Same original job deadline stopped actual "+label)
    return child


def source(name, digest):
    path = HERE/name
    require(path.is_file() and file_sha(path) == digest, "Actual pinned source "+name)
    return path


def run_factor(spec, root, remaining, record):
    snapshot = checked(spec["snapshot_result"], root)
    snapshot_record = read(snapshot)
    require(snapshot.name == "result.json" and snapshot_record["snapshot_completed"] is True
            and snapshot_record["native_call"] == spec["call_number"]
            and snapshot_record["nonlinear_iteration"] == snapshot_record["snapshot_sequence"] == 0,
            "One actual current-H complete with-J snapshot")
    bridge = spec["bridge"]
    require(bridge["source_file"] == QR and bridge["source_sha256"] == QR_SHA
            and bridge["system_source_sha256"] == SYSTEM_SHA,
            "Actual R273 source view tuple")
    source(SYSTEM, SYSTEM_SHA)
    eta = float(bridge["eta_cli_text"])
    require(math.isfinite(eta) and eta > 0, "Original positive R273 model damping parameter")
    cap = spec["resources"]["factor_seconds_cap"]
    require(type(cap) is int and cap > 0
            and type(bridge["max_factor_bytes"]) is int and bridge["max_factor_bytes"] > 0
            and type(bridge["exact_workers"]) is int and 1 <= bridge["exact_workers"] <= 4,
            "Explicit original complete factor resources")
    actual = min(cap, max(0.0, remaining()-30))
    if actual <= 0:
        raise ResourceStop("No scientific allowance for the actual full R273 factor")
    command = [sys.executable, "-u", str(source(QR, QR_SHA)),
        "--snapshot-directory", str(snapshot.parent),
        "--snapshot-result-sha256", spec["snapshot_result"]["sha256"],
        "--eta", bridge["eta_cli_text"], "--factor-budget-seconds", str(actual),
        "--max-factor-bytes", str(bridge["max_factor_bytes"]),
        "--exact-workers", str(bridge["exact_workers"]), "--out", str(root/"qr")]
    child = run_child(command, root, "actual-current-QR", min(remaining(), actual+30), record)
    result_file = root/"qr"/"result.json.gz"
    if result_file.is_file():
        result = read(result_file)
        record["actual_full_QR_result"] = receipt(result_file)
        record["actual_QR_flags"] = {k:result.get(k) for k in (
            "diagnostic_completed", "linear_direction_computed", "actual_error",
            "native_call", "nonlinear_iteration", "snapshot_sequence", "elapsed_seconds")}
        if (child["actual_returncode"] != 0 or result.get("diagnostic_completed") is not True
                or result.get("linear_direction_computed") is not True):
            raise RuntimeError("Actual original complete R273 return is incomplete")
    else:
        raise RuntimeError("The actual R273 full result was not returned")
    return dict(qr_directory=str(root/"qr"), actual_QR_result=record["actual_full_QR_result"])


def run_response(spec, root, remaining, record):
    snapshot_file = checked(spec["snapshot_result"], root)
    snapshot = read(snapshot_file)
    require(snapshot["snapshot_completed"] is True
            and snapshot["native_call"] == spec["call_number"]
            and snapshot["nonlinear_iteration"] == snapshot["snapshot_sequence"] == 0,
            "This current-H complete original64 capture")
    context = read(member(snapshot_file.parent, snapshot["context"]))
    manifest = read(member(snapshot_file.parent, snapshot["manifest"]))
    binding_file = checked(spec["packet_binding"], root)
    binding = read(binding_file)
    require(binding["actual_call_identity"]["fresh_snapshot_result_sha256"] == spec["snapshot_result"]["sha256"]
            and binding["actual_call_identity"]["native_call"] == spec["call_number"],
            "The new actual packet binds this H and snapshot")
    for name in ("packet", "physical_packet", "physical_binding"):
        checked(spec[name], root)
    owner_resources = dict(spec["resources"]["owner"])
    owner_resources["audit_seconds_cap"] = (
        owner_resources["audit_seconds_cap"] if spec["request"]["audit"] else 0)
    owner_input = dict(schema="R493-current-H-live128-owner-call-v1-input-v1",
        call_directory=str(root), out=str(root/"owner"), call_number=spec["call_number"],
        job_deadline=spec["job_deadline"], packet=spec["packet"],
        packet_binding=spec["packet_binding"], snapshot_result=spec["snapshot_result"],
        physical_packet=spec["physical_packet"], physical_binding=spec["physical_binding"],
        original_source_root=spec["original_source_root"],
        request_audit=spec["request"]["audit"], resources=owner_resources)
    input_file = root/"owner-input.json"
    write(input_file, owner_input)
    child = run_child([sys.executable, "-u", str(source(OWNER, OWNER_SHA)),
        "--input", str(input_file), "--input-sha256", file_sha(input_file)],
        root, "actual-owner-and-components", remaining(), record)
    owner_file = root/"owner"/"summary.json"
    procedure_file = root/"owner-call-procedure.json"
    if procedure_file.is_file():
        record["actual_owner_call_procedure"] = receipt(procedure_file)
    if not owner_file.is_file():
        raise RuntimeError("The actual same-H owner did not return its complete summary")
    owner = read(owner_file)
    record["actual_owner_summary"] = receipt(owner_file)
    record["actual_owner_child_returncode"] = child["actual_returncode"]
    final = owner.get("owner_final") or {}
    record["actual_owner_final_flags"] = {key:final.get("final", {}).get(key) for key in (
        "complete", "below_original_tolerance", "budget_exhausted", "norm", "stages_completed")}
    record["actual_owner_original_stop_reason"] = final.get("stop_reason")
    record["actual_owner_error"] = owner.get("actual_error")
    # Actual completeness of the mathematical return is independent of old
    # compact child transport70. No mathematical failure is called success.
    if (final.get("final", {}).get("complete") is not True
            or final["final"].get("below_original_tolerance") is not True
            or owner.get("independent_fresh_replay_complete") is not True):
        raise RuntimeError("Actual current-H owner final tolerance/replay has not completed")
    post = owner.get("post_owner_components") or {}
    record["actual_component_flags"] = {key:post.get(key) for key in (
        "complete_stage_maps", "complete_boundary112_response",
        "complete_mixed_endpoint338x112_readout", "complete_original_C_based_physical_program_audit",
        "all_requested_components_completed", "actual_error", "not_started_reason")}
    handoff = member(owner_file.parent, post["actual_owner_handoff"])
    state_file = owner_file.parent/"solve"/"final-state.f128"
    require(state_file.is_file()
            and receipt(state_file)["sha256"] == owner["final_state128"]["sha256"]
            and state_file.stat().st_size == owner["final_state128"]["bytes"],
            "The same actual final128 owner state is still present")
    components = {}
    for name in ("stages", "boundary", "endpoint", "audit"):
        if name == "audit" and not spec["request"]["audit"]:
            continue
        directory = owner_file.parent/"final-components"/name
        file = directory/"summary.json"
        if file.is_file():
            components[name] = dict(directory=str(directory), summary=receipt(file))
    height_rows = [row for row in manifest["arrays"] if row["name"] == "physical-height"]
    require(len(height_rows) == 1 and len(height_rows[0]["chunks"]) == 1,
            "Complete current physical H uses one original raw chunk")
    height_path = member(snapshot_file.parent, height_rows[0]["chunks"][0])
    assembly_input = dict(schema="R493-current-H-live128-response-assembly-v1-input-v1",
        call_directory=str(root), out=str(root/"response"), call_number=spec["call_number"],
        job_deadline=spec["job_deadline"], request=spec["request"],
        owner_summary=receipt(owner_file), owner_source=receipt(HERE/OWNER),
        owner_handoff=receipt(handoff), packet_binding=spec["packet_binding"],
        snapshot_result=spec["snapshot_result"], physical_height=receipt(height_path),
        state=receipt(state_file), parameters=context["parameters"], raw_node=context["rawNode"],
        components=components, retain_optional_tangent_predictor=spec["retain_optional_tangent_predictor"])
    assembly_file = root/"assembly-input.json"
    write(assembly_file, assembly_input)
    assembly_child = run_child([sys.executable, "-u", str(source(ASSEMBLER, ASSEMBLER_SHA)),
        "--input", str(assembly_file), "--input-sha256", file_sha(assembly_file)],
        root, "actual-protocol-projection", remaining(), record)
    result_file = root/"response"/"summary.json"
    if not result_file.is_file():
        raise RuntimeError("Actual complete response projection summary missing")
    result = read(result_file)
    record["actual_response_assembly_summary"] = receipt(result_file)
    record["actual_response_assembly_error"] = result.get("error")
    if assembly_child["actual_returncode"] != 0 or result.get("complete") is not True:
        raise RuntimeError("Actual same-H response projection remains incomplete")
    response_file = checked(result["response_file"], root)
    return dict(response=receipt(response_file),
        optional_predictor_manifest=result.get("optional_predictor_manifest_for_worker"),
        actual_response_assembly_summary=receipt(result_file),
        original_TailClient_acceptance_still_required=True,
        same_current_H_owner_state_and_all_actual_components=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args()
    require(file_sha(args.input) == args.input_sha256, "Actual complete call input")
    spec = read(args.input)
    root = Path(spec["call_directory"]).resolve(strict=True)
    record = dict(schema=SCHEMA, source=receipt(__file__), input=receipt(args.input),
        mode=spec["mode"], call_number=spec["call_number"],
        run={key:os.environ.get(key) for key in RUN_KEYS},
        actual_process=process_identity(), children=[], complete=False, error=None,
        per_call_total_clock_reset=False, native_accepted=False, fullDN_accepted=False,
        original_inputs_and_large_raw_retained_until_necessary_readback=True)
    code, started = 2, time.monotonic()
    try:
        root, clock, remaining = bind(spec)
        record["job_deadline"] = spec["job_deadline"]
        record["original_clock_remaining_before_seconds"] = remaining()
        if spec["mode"] == "clock":
            value = dict(original_clock_remaining_seconds=remaining())
        elif spec["mode"] == "factor":
            value = run_factor(spec, root, remaining, record)
        else:
            value = run_response(spec, root, remaining, record)
        record.update(value)
        record["complete"] = True
        code = 0
    except Exception as error:
        record["error"] = dict(type=type(error).__name__, message=str(error))
        record["traceback"] = traceback.format_exc()
        record["resource_partial"] = isinstance(error, ResourceStop)
        code = 3 if isinstance(error, ResourceStop) else 2
    finally:
        record["elapsed_seconds"] = time.monotonic()-started
        record["actual_returncode"] = code
        write(root/("pipeline-"+spec["mode"]+"-result.json"), record)
    print(json.dumps(dict(event="R493_actual_call_phase_return", mode=spec["mode"],
        call_number=spec["call_number"], actual_returncode=code,
        complete=record["complete"], error=record["error"]), ensure_ascii=True,
        separators=(",", ":"), allow_nan=False), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
