#!/usr/bin/env python3
"""A separate public-Actions design branch releasing core modes 4 through M.

The complete accepted field is retained as the warm start. Every positive
turn increment rebuilds the original principal normal projector starting at
mode 4 and solves the unchanged finite Frenet BVP with fixed_modes=3. This
is a new metric design problem and an open prefix, not a full tail match or
a same-metric refinement. Original nonlinear acceptance thresholds remain.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

from geometry_20261114_public_continuation import (
    HERE, TOPIC, accepted_summary, argument, now, read, run, sha, write,
)

FROZEN_SOURCES = {
    "geometry_20261114_projected_core_bvp.py": "2326720f124d2edc40e63089f8e07d6671e053ff108281efb59091d919f15c5b",
    "geometry_20261114_separated_qr_bvp.py": "c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39",
    "geometry_20261114_normal_terminal_projector.py": "d6c6f1308f678cae77750b33977d41f2bdb8d355f345d43bcb3f68b1e9e7d47d",
    "geometry_20261114_normal_bvp_continue.py": "3baf49eea03a12baa3da452a53e57bfe6b25e1e77f6ceb8da066a2e7d63c1ce8",
}


def prepare_command(accepted, duration, prefix, workers, max_nodes):
    return [sys.executable, "-u", str(HERE / "geometry_20261114_normal_bvp_continue.py"),
            "--input", str(accepted), "--duration", repr(duration),
            "--fixed-modes", "3", "--jac-workers", str(workers),
            "--tol", "1e-6", "--max-nodes", str(max_nodes), "--out-prefix", str(prefix)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accepted", type=Path, default=TOPIC / "notes/2026-11-14-geometry-resume-scaled-sphere-M96-normal-BVP-r1.json.gz")
    parser.add_argument("--durations", type=float, nargs="+", default=[.006])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--work", type=Path)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--max-nodes", type=int, default=640)
    parser.add_argument("--budget-seconds", type=float, default=18000)
    parser.add_argument("--plan-only", action="store_true")
    args = parser.parse_args()
    if args.jac_workers < 1 or args.budget_seconds <= 0 or any(d <= 0 for d in args.durations):
        raise ValueError("Positive worker, time and continuation budgets are required")
    if not args.plan_only and (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run this numerical branch in the public repository's own GitHub Actions")
    for filename, expected in FROZEN_SOURCES.items():
        if sha(HERE / filename) != expected:
            raise ValueError("The original mathematical source differs: " + filename)
    accepted = args.accepted.resolve()
    summary = accepted_summary(accepted)
    if not summary["finite_BVP_accepted"] or (summary["modes"], summary["angles"]) != (96, 1024):
        raise ValueError("Start with a complete accepted M96/N1024 field")
    data = read(accepted)
    if args.max_nodes < len(data["mesh"]):
        raise ValueError("The node budget cannot discard the complete accepted warm field")
    n, M = 3 * data["M"] + 2, data["M"]
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    work = args.work.resolve() if args.work else Path(tempfile.mkdtemp(
        prefix="visible-M96-free3-", dir=os.environ.get("RUNNER_TEMP")))
    work.mkdir(parents=True, exist_ok=True)
    if work == out or out in work.parents:
        raise ValueError("Reproducible QR scratch must stay outside uploaded output")
    state = dict(scope=__doc__, started=now(), ended=None, phase="prepared",
                 source_sha256=sha(__file__), accepted_input_sha256=sha(accepted),
                 frozen_solver_sources=FROZEN_SOURCES,
                 source_repository=os.environ.get("GITHUB_REPOSITORY"),
                 source_commit=os.environ.get("GITHUB_SHA"), initial_summary=summary,
                 first_three_core_coefficients=data["core"]["coefficients"][:3],
                 state_dimension=n, left_boundary_rows=2 * M + 5,
                 terminal_rows=M - 3, scalar_unknowns=0,
                 normal_first_mode=4, released_core_modes=list(range(4, M + 1)),
                 requested_durations=args.durations, stages=[], complete_closed_surface=False,
                 same_metric_refinement=False, full_material_tail_DN_imposed=False)
    status = out / "driver-status.json"
    state["first_preparation_command"] = prepare_command(accepted, args.durations[0],
        out / "stage-00/continued", args.jac_workers, args.max_nodes)
    write(status, state)
    if args.plan_only:
        print({"event": "free3-plan", "state_dimension": n,
               "left_rows": 2 * M + 5, "right_rows": M - 3,
               "numerical_work_performed": False}, flush=True)
        return 0
    deadline = time.monotonic() + args.budget_seconds
    exitcode = 1
    try:
        for index, duration in enumerate(args.durations):
            stage = out / ("stage-" + str(index).zfill(2))
            stage.mkdir(parents=True, exist_ok=True)
            prefix = stage / "continued"
            preparation = prepare_command(accepted, duration, prefix, args.jac_workers, args.max_nodes)
            state.update(phase="preparing-normal-free3", current_stage=index)
            write(status, state)
            code = run(preparation, stage / "prepare.log", deadline)
            record = dict(stage=index, duration=duration, prepare_returncode=code)
            state["stages"].append(record)
            if code:
                state["phase"] = "preparation-failed"
                exitcode = code
                break
            plan = read(Path(str(prefix) + "-plan.json"))
            command = list(plan["command"])
            argument(command, "--linear-workdir", work / ("qr-" + str(index).zfill(2)))
            argument(command, "--out", stage / "actual.json.gz")
            write(stage / "command.json", command)
            record["plan_sha256"] = sha(Path(str(prefix) + "-plan.json"))
            state["phase"] = "solving-normal-free3"
            write(status, state)
            code = run(command, stage / "run.log", deadline)
            record.update(returncode=code, ended=now())
            actual = stage / "actual.json.gz"
            if actual.is_file():
                record.update(accepted_summary(actual))
            if code or not record.get("finite_BVP_accepted"):
                state["phase"] = "new-design-not-accepted"
                exitcode = code or 2
                break
            accepted = actual
            state.update(phase="accepted-open-free3-prefix", latest_accepted_file=str(actual),
                         latest_accepted_end=record["end"])
            write(status, state)
            record["postprocessing"] = []
            for label, post in [
                ("core", [sys.executable, "-u", str(HERE / "geometry_20261114_core_certificate.py"),
                          "--accepted", str(actual), "--out", str(stage / "core-certificate.json")]),
                ("physical-field", [sys.executable, "-u", str(HERE / "geometry_20261114_material_quintic_readout.py"),
                                    "--input", str(actual), "--angles", "1024", "2048",
                                    "--radial-subdivisions", "2", "4", "--out", str(stage / "material-quintic.json")]),
            ]:
                code = run(post, stage / (label + ".log"), deadline)
                record["postprocessing"].append(dict(kind=label, returncode=code))
                if code:
                    state["phase"] = "accepted-field-postprocessing-incomplete"
                    exitcode = code
                    break
            if any(item["returncode"] for item in record["postprocessing"]):
                break
            state["phase"] = "accepted-open-free3-prefix-with-readout"
            write(status, state)
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
        write(status, state)
        print({"event": "free3-exit", "phase": state["phase"], "returncode": exitcode,
               "stages": len(state["stages"]), "latest_accepted_end": state.get("latest_accepted_end")}, flush=True)
    return exitcode


if __name__ == "__main__":
    raise SystemExit(main())
