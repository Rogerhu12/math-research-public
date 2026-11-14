#!/usr/bin/env python3
"""Check the explicit root-approved guard argv without running any child."""
import argparse
import hashlib
import json
import os
from pathlib import Path

T = Path(__file__).resolve().parents[1]
R = T.parents[1]
SCRIPT = T / "scripts/db6f-root-run-space-guarded.py"
LAUNCH = T / "notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json"
PRIMARY = T / "notes/2026-11-09-db6f-root-amplitude-resume03-child-execution.json"
BACKUP = Path("/dev/shm/db6f-root-amplitude-resume03-child-execution.json")
TEST = T / "notes/2026-11-09-db6f-root-space-guard-directed-check.json"
ARGV = ["/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python", str(SCRIPT),
        "--launch", str(LAUNCH), "--observation", str(PRIMARY), "--backup-observation", str(BACKUP),
        "--minimum-free", "536870912", "--resume-free", "805306368", "--poll-seconds", "2"]
PINS = {SCRIPT: "cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd",
        LAUNCH: "0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c",
        TEST: "dd55296087499e29723bffa178ae08939acfca32eddcbaccf2492b09d3b6556a"}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binding(path):
    return {"path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    need(not args.out.exists() and args.out.resolve().is_relative_to(T), "Fresh topic audit report")
    for path, digest in PINS.items():
        need(sha(path) == digest, "Frozen source changed")
    launch = json.loads(LAUNCH.read_text())
    need(len(launch["bound_files"]) == 83, "83 bound inputs")
    inputs = set()
    for item in launch["bound_files"]:
        path = Path(item["path"]).resolve()
        need(path not in inputs and path.stat().st_size == item["bytes"] and sha(path) == item["sha256"], "Unique actual binding")
        inputs.add(path)
    inputs.update(PINS)
    output = Path(launch["out_prefix"]).resolve()
    reproduction = Path(str(output) + "-reproduction.json")
    log = Path(str(output) + "-run.log")
    targets = [PRIMARY.resolve(), BACKUP.resolve()]
    temporaries = [p.with_name(p.name + ".tmp") for p in targets]
    need(len(set(targets + temporaries + [log, reproduction])) == 6, "All observation/log/reproduction paths are distinct")
    for path in targets + temporaries + [log]:
        need(path not in inputs and path != reproduction and not path.exists(), "No overwrite or source collision")
        need(path.parent.is_dir(), "Output parent exists")
    need(PRIMARY.parent == T / "notes" and BACKUP.parent == Path("/dev/shm"), "Production output roots")
    need(not PRIMARY.name.startswith(output.name), "Primary observation is outside the controller output prefix")
    st = os.statvfs(R)
    free = st.f_bavail * st.f_frsize
    need(free >= 805306368, "Enough available space at this preflight")
    need(Path(ARGV[0]).is_file(), "Original Python exists")
    need(536870912 == 512 * 1024 ** 2 and 805306368 == 768 * 1024 ** 2, "Exact production thresholds")
    report = {"status": "PASS-explicit-space-guard-production-paths-only",
              "checker_sha256": sha(Path(__file__).resolve()), "sources": [binding(p) for p in PINS],
              "cwd": str(R), "argv": ARGV, "verified_binding_count": 83,
              "observation_paths_distinct_from_inputs_log_and_reproduction": True,
              "observation_and_temporary_paths_fresh_at_check": True,
              "backup_is_explicit_dev_shm_path": True,
              "available_bytes_at_preflight": free, "minimum_free": 536870912,
              "resume_free": 805306368, "poll_seconds": 2,
              "mathematical_command_is_launch_command_unchanged": True,
              "new_child_processes": 0, "solver_calls": 0,
              "heartbeat_test_repeated_by_this_checker": False,
              "no_guarantee_against_arbitrary_shared_disk_bursts": True,
              "root_actual_tool_exit_observation_still_required": True}
    with args.out.open("x") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n")
    print(json.dumps({"status": report["status"], "sha256": sha(args.out), "child_processes": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
