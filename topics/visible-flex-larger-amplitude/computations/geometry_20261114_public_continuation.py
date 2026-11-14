#!/usr/bin/env python3
"""Resume the complete M96 positive-curvature BVP on this public repository.

The first stage uses the exact .99 profile, normal terminal matrix, native
seed, and complete fourth-Jacobian checkpoint recovered from the interrupted
run. The recorded ENOSPC is an execution failure, not solver convergence.
Later stages start only from a completed nonlinear solve and append the
explicit scalar turn using geometry_20261114_normal_bvp_continue.py.

All first 32 support modes, all 290 state variables, the original equations,
normal boundary conditions, tolerance and unfiltered Fourier RHS remain.
Subsequent endpoints define new design problems: their free core modes may
change, so this is not evidence of convergence for one fixed metric.
"""
from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".tmp")
    partial.write_text(json.dumps(content, indent=2, allow_nan=False) + "\n")
    partial.replace(path)


def argument(command, name, value):
    if command.count(name) != 1:
        raise ValueError("Expected exactly one command argument " + name)
    command[command.index(name) + 1] = str(value)


def verify_recovery(directory):
    manifest = read(directory / "manifest.json")
    for row in manifest["files"]:
        path = directory / row["name"]
        if path.name != row["name"] or not path.is_file():
            raise ValueError("Recovery contains a missing or nonlocal file")
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            raise ValueError("Recovery file identity differs: " + row["name"])
    for filename, expected in manifest["solver_source_sha256"].items():
        if sha(HERE / filename) != expected:
            raise ValueError("Recorded mathematical solver differs: " + filename)
    data = read(directory / "newton-checkpoint.json.gz")
    if (data["M"], data["N"], len(data["mesh"]), data["mesh"][-1]) != (96, 1024, 423, .99):
        raise ValueError("Recovery is not the complete recorded M96 checkpoint")
    if data["global_jacobian_call"] != 4:
        raise ValueError("Expected the fourth-Jacobian entry checkpoint")
    if any(len(row) != 290 for row in data["states"] + data["rhs"]):
        raise ValueError("A recovery row lost state components")
    return manifest


def initial_command(recovery, stage, work, workers):
    return [sys.executable, "-u", str(HERE / "geometry_20261114_projected_core_bvp.py"),
        "--profile", str(recovery / "profile.json"),
        "--seed", str(recovery / "seed.json.gz"),
        "--warm", str(recovery / "newton-checkpoint.json.gz"),
        "--M", "96", "--N", "1024", "--fixed-modes", "32", "--end", ".99",
        "--base-step", ".005", "--extension-step", ".001",
        "--seed-interpolation", "hermite", "--seed-predictor", "taylor2",
        "--terminal-projector", str(recovery / "projector.json.gz"),
        "--linear-solver", "separated-qr", "--linear-workdir", str(work / "qr-00"),
        "--jac-workers", str(workers), "--jac-chunk", "16",
        "--tol", "1e-6", "--max-nodes", "640", "--out", str(stage / "actual.json.gz")]


def run(command, log, deadline):
    remaining = deadline - time.monotonic()
    if remaining < 30:
        raise TimeoutError("Runner budget exhausted before a new child was launched")
    with Path(log).open("wb") as stream:
        result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                timeout=remaining, check=False)
    return int(result.returncode)


def accepted_summary(path):
    result = read(path)
    tolerance = float(result["parameters"]["tol"])
    rms = result.get("collocation_rms_max")
    boundary = result.get("boundary_residual_max")
    finite_acceptance = (result.get("success") is True and result.get("status") == 0
                        and isinstance(rms, (int, float)) and 0 <= rms <= tolerance
                        and isinstance(boundary, (int, float)) and 0 <= boundary <= 1e-11)
    return dict(finite_BVP_accepted=finite_acceptance,
                success=result.get("success"), status=result.get("status"),
                message=result.get("message"), end=result.get("end"),
                modes=result.get("M"), angles=result.get("N"),
                nodes=len(result.get("mesh", [])), collocation_rms_max=rms,
                boundary_residual_max=boundary, geometry=result.get("summary"),
                core_axis_support_gap=result.get("core", {}).get("axis_support_gap"),
                core_rho_sample_min=result.get("core", {}).get("rho_sample_min"),
                result_sha256=sha(path), complete_closed_surface=False,
                fixed_metric_refinement=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recovery", type=Path,
                        default=TOPIC / "notes/2026-11-14-public-M96-099-recovery")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--work", type=Path)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--next-durations", type=float, nargs="*", default=[])
    parser.add_argument("--budget-seconds", type=float, default=18000)
    parser.add_argument("--plan-only", action="store_true")
    args = parser.parse_args()
    if args.jac_workers < 1 or args.budget_seconds <= 0 or any(d <= 0 for d in args.next_durations):
        raise ValueError("Positive resources and continuation durations are required")
    if not args.plan_only and os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Run numerical work in this public repository's GitHub Actions")
    if not args.plan_only and os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("The numerical job belongs to Rogerhu12/math-research-public")
    recovery, out = args.recovery.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    manifest = verify_recovery(recovery)
    work = args.work.resolve() if args.work else Path(tempfile.mkdtemp(
        prefix="visible-M96-continuation-", dir=os.environ.get("RUNNER_TEMP")))
    work.mkdir(parents=True, exist_ok=True)
    if work == out or out in work.parents:
        raise ValueError("Large QR scratch must stay outside the uploaded output directory")
    command = initial_command(recovery, out / "stage-00", work, args.jac_workers)
    state = dict(scope=__doc__, started=now(), ended=None, phase="prepared",
                 source_sha256=sha(__file__), recovery_manifest_sha256=sha(recovery / "manifest.json"),
                 original_failure=manifest["original_failure"],
                 first_command=command, work=str(work), stages=[],
                 requested_next_durations=args.next_durations,
                 source_repository=os.environ.get("GITHUB_REPOSITORY"),
                 source_commit=os.environ.get("GITHUB_SHA"),
                 complete_closed_surface=False, new_accepted_result=False)
    status_path = out / "driver-status.json"
    write(status_path, state)
    if args.plan_only:
        print(json.dumps(dict(event="plan-prepared", command=command,
                              numerical_work_performed=False)), flush=True)
        return 0
    deadline = time.monotonic() + args.budget_seconds
    last_accepted = None
    exitcode = 1
    try:
        for index in range(1 + len(args.next_durations)):
            stage = out / ("stage-" + str(index).zfill(2))
            stage.mkdir(parents=True, exist_ok=True)
            if index:
                prefix = stage / "continued"
                prepare_command = [sys.executable, "-u", str(HERE / "geometry_20261114_normal_bvp_continue.py"),
                    "--input", str(last_accepted), "--duration", repr(args.next_durations[index - 1]),
                    "--fixed-modes", "32", "--jac-workers", str(args.jac_workers),
                    "--tol", "1e-6", "--max-nodes", "640", "--out-prefix", str(prefix)]
                code = run(prepare_command, stage / "prepare.log", deadline)
                if code:
                    state["stages"].append(dict(stage=index, phase="preparation-failed", returncode=code))
                    exitcode = code
                    break
                plan = read(Path(str(prefix) + "-plan.json"))
                command = list(plan["command"])
                argument(command, "--linear-workdir", work / ("qr-" + str(index).zfill(2)))
                argument(command, "--out", stage / "actual.json.gz")
            write(stage / "command.json", command)
            state.update(phase="running", current_stage=index)
            write(status_path, state)
            print(json.dumps(dict(event="actual-continuation-start", stage=index, command=command)), flush=True)
            code = run(command, stage / "run.log", deadline)
            record = dict(stage=index, returncode=code, ended=now(), output=str(stage / "actual.json.gz"))
            if (stage / "actual.json.gz").is_file():
                record.update(accepted_summary(stage / "actual.json.gz"))
            state["stages"].append(record)
            if code or not record.get("finite_BVP_accepted"):
                state["phase"] = "continuation-not-accepted"
                exitcode = code or 2
                write(status_path, state)
                break
            last_accepted = stage / "actual.json.gz"
            state.update(phase="accepted-open-prefix", new_accepted_result=True,
                         latest_accepted_file=str(last_accepted), latest_accepted_end=record["end"])
            write(status_path, state)
            print(json.dumps(dict(event="finite-BVP-accepted", **record)), flush=True)
            # Each stage's final field and latest Newton snapshot are sufficient
            # for restarting; obsolete local factors are reproducible scratch.
            scratch = work / ("qr-" + str(index).zfill(2))
            if scratch.is_dir():
                shutil.rmtree(scratch)
            exitcode = 0
    except subprocess.TimeoutExpired as error:
        state.update(phase="runner-budget-checkpoint", exception=str(error))
        exitcode = 124
    except Exception as error:
        state.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        exitcode = 1
    finally:
        state.update(ended=now(), returncode=exitcode)
        write(status_path, state)
        print(json.dumps(dict(event="actual-continuation-exit", phase=state["phase"],
                              returncode=exitcode, stages=len(state["stages"]),
                              latest_accepted_end=state.get("latest_accepted_end"))), flush=True)
    return exitcode


if __name__ == "__main__":
    raise SystemExit(main())
