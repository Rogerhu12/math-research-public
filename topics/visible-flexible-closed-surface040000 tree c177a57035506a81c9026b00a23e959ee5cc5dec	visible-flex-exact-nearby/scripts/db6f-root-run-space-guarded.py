#!/usr/bin/env python3
"""Run an immutable bound argv with a disk-space process-group guard.

This outer supervisor changes no numerical input, solver, or reproduction file.
Its completion record still requires /root to observe the actual tool exit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def free_bytes(path):
    stat = os.statvfs(path)
    return stat.f_bavail * stat.f_frsize


def save_record(path, record):
    raw = (json.dumps(record, indent=2, allow_nan=False) + "\n").encode()
    if len(raw) >= 1_000_000:
        raise ValueError("Unexpected large supervisor record")
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def supervise(binding_path, observation_path, backup_path, minimum_free,
              resume_free, poll_seconds, available=free_bytes):
    binding_path = Path(binding_path).resolve()
    observation_path = Path(observation_path).resolve()
    backup_path = Path(backup_path).resolve()
    binding = json.loads(binding_path.read_text())
    cwd = Path(binding["cwd"]).resolve()
    output = Path(binding["out_prefix"]).resolve()
    log_path = Path(str(output) + "-run.log")
    if not 0 < minimum_free < resume_free or not 0 < poll_seconds <= 10:
        raise ValueError("Invalid disk guard limits")
    if observation_path == backup_path:
        raise ValueError("Backup must have a distinct path")
    for path in (log_path, observation_path, backup_path):
        if path.exists():
            raise FileExistsError(path)
    if observation_path == Path(str(output) + "-reproduction.json"):
        raise ValueError("Never overwrite controller reproduction")
    for row in binding["bound_files"]:
        path = Path(row["path"])
        if path.stat().st_size != row["bytes"] or digest(path) != row["sha256"]:
            raise ValueError("Bound input changed: " + str(path))
    if available(cwd) < resume_free:
        raise RuntimeError("Insufficient free space to start this computation")
    command = binding["command"]
    if not isinstance(command, list) or not command or not all(isinstance(x, str) for x in command):
        raise ValueError("Expected an explicit bound argv, not a shell command")
    record = dict(status="RUNNING_BOUND_CHILD", binding=str(binding_path),
                  binding_sha256=digest(binding_path), command=command, cwd=str(cwd),
                  stem=output.name, wrapper_sha256=digest(__file__),
                  minimum_free=minimum_free, resume_free=resume_free,
                  poll_seconds=poll_seconds, events=[],
                  numerical_inputs_or_argv_changed=False,
                  tool_exit_observed_by_root=False)
    start = time.monotonic()
    process = None
    paused = False

    def event(kind, space=None):
        row = dict(event=kind, elapsed_seconds=time.monotonic()-start)
        if space is not None:
            row["available_bytes"] = space
        record["events"].append(row)
        print(json.dumps(row), flush=True)
        save_record(backup_path, record)

    try:
        with log_path.open("x") as log:
            process = subprocess.Popen(command, cwd=cwd, stdout=log,
                                       stderr=subprocess.STDOUT, start_new_session=True)
            record["child_pid_and_process_group"] = process.pid
            event("started")
            while process.poll() is None:
                space = available(cwd)
                if not paused and space < minimum_free:
                    try:
                        os.killpg(process.pid, signal.SIGSTOP)
                    except ProcessLookupError:
                        pass
                    else:
                        paused = True
                        event("paused_own_process_group_for_space", space)
                elif paused and space >= resume_free:
                    try:
                        os.killpg(process.pid, signal.SIGCONT)
                    except ProcessLookupError:
                        pass
                    else:
                        paused = False
                        event("resumed_same_process_group", space)
                time.sleep(poll_seconds)
            record.update(status="CHILD_COMPLETED_AWAITING_ROOT_TOOL_OBSERVATION",
                          actual_child_exit_code=process.returncode,
                          seconds=time.monotonic()-start)
    except BaseException as exc:
        record.update(status="SUPERVISOR_EXCEPTION", exception=repr(exc))
        if process is not None and process.poll() is None:
            # This is our new process group only. Do not leave a stopped orphan.
            for sig in (signal.SIGCONT, signal.SIGTERM):
                try:
                    os.killpg(process.pid, sig)
                except ProcessLookupError:
                    pass
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.wait()
            record["actual_child_exit_code"] = process.returncode
        save_record(backup_path, record)
        raise
    save_record(backup_path, record)
    try:
        save_record(observation_path, record)
    except OSError as exc:
        record["primary_observation_write_error"] = repr(exc)
        save_record(backup_path, record)
    print(json.dumps(dict(status=record["status"],
                         actual_child_exit_code=process.returncode,
                         root_tool_observation_still_required=True,
                         primary_record_available=observation_path.exists(),
                         backup_record=str(backup_path))), flush=True)
    return process.returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--launch", type=Path, required=True)
    parser.add_argument("--observation", type=Path, required=True)
    parser.add_argument("--backup-observation", type=Path, required=True)
    parser.add_argument("--minimum-free", type=int, default=512*1024*1024)
    parser.add_argument("--resume-free", type=int, default=768*1024*1024)
    parser.add_argument("--poll-seconds", type=float, default=2)
    args = parser.parse_args()
    code = supervise(args.launch, args.observation, args.backup_observation,
                     args.minimum_free, args.resume_free, args.poll_seconds)
    raise SystemExit(code if code >= 0 else 128-code)


if __name__ == "__main__":
    main()
