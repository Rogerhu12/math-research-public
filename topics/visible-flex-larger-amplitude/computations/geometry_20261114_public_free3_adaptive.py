#!/usr/bin/env python3
"""Continue an already accepted free3 prefix after a failed Taylor projector.

Only a principal-elliptic guard failure during preparation triggers step
halving. Actual nonlinear solver failures are retained and are not renamed
as acceptance. The original preparer, projector, BVP equations, RMS and BC
thresholds remain unchanged. Successful earlier stages are never repeated.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

from geometry_20261114_public_continuation import (
    HERE, accepted_summary, now, read, run, sha, write,
)

ELLIPTIC_FAILURE = "Principal elliptic boundary requires strictly positive sampled det II and nonzero II_phi_phi"


def actual_projector_check(accepted, output):
    import numpy as np
    import geometry_20261114_normal_terminal_projector as normal
    data = read(accepted)
    law = data["original_metric_identity"]["law"]
    driver = normal.driver
    q = driver.native.outward.FullCoreProbe(np.asarray(data["core"]["coefficients"]),
        data["M"], data["N"], law["velocity"], law["length"], law["k0"])
    q.profile = driver.fixed.FixedProfile(data["fixed_scalar_profile"]["geometry"]).profile
    driver.fixed.fft.enable_fft(q)
    s, y = float(data["mesh"][-1]), np.asarray(data["states"][-1])
    try:
        matrix, norms, diagnostic = normal.projector(q, s, y, 4)
        result = dict(scope="The original principal-normal test at the actual accepted field, without any extrapolation.",
                      actual_reference_elliptic=True, station=s, diagnostic=diagnostic,
                      accepted_sha256=sha(accepted), original_source_sha256=sha(HERE / "geometry_20261114_normal_terminal_projector.py"))
    except ValueError as error:
        if str(error) != ELLIPTIC_FAILURE:
            raise
        result = dict(scope="Original principal-normal test at the actual accepted field.",
                      actual_reference_elliptic=False, station=s, error=str(error),
                      accepted_sha256=sha(accepted))
    write(output, result)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--accepted", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--duration", type=float, default=.006)
    p.add_argument("--minimum-duration", type=float, default=.0001875)
    p.add_argument("--maximum-duration", type=float, default=.012)
    p.add_argument("--target-end", type=float, default=1.05)
    p.add_argument("--max-stages", type=int, default=40)
    p.add_argument("--jac-workers", type=int, default=2)
    p.add_argument("--max-nodes", type=int, default=900)
    p.add_argument("--budget-seconds", type=float, default=18000)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise RuntimeError("Run numerical continuation in this public repository's own Actions")
    if not 0 < args.minimum_duration <= args.duration <= args.maximum_duration or args.max_stages < 1:
        raise ValueError("Provide positive ordered continuation step bounds")
    accepted = args.accepted.resolve()
    summary = accepted_summary(accepted)
    if not summary["finite_BVP_accepted"] or (summary["modes"], summary["angles"]) != (96, 1024):
        raise ValueError("Resume a complete actually accepted M96/N1024 field")
    if args.target_end <= summary["end"]:
        raise ValueError("The target must extend beyond the accepted endpoint")
    out, work = args.out.resolve(), args.work.resolve()
    out.mkdir(parents=True, exist_ok=True); work.mkdir(parents=True, exist_ok=True)
    if work == out or out in work.parents:
        raise ValueError("Large QR scratch belongs outside the uploaded output")
    state = dict(scope=__doc__, source_sha256=sha(__file__), started=now(),
                 phase="checking-actual-reference", input_sha256=sha(accepted), initial_summary=summary,
                 latest_accepted_file=str(accepted), latest_accepted_end=summary["end"],
                 target_end=args.target_end, requested_step=args.duration, minimum_step=args.minimum_duration,
                 attempts=[], accepted_stages=0, full_material_tail_DN_imposed=False,
                 complete_closed_surface=False)
    status = out / "driver-status.json"
    write(status, state)
    deadline = time.monotonic() + args.budget_seconds
    h, streak = args.duration, 0
    returncode = 1
    try:
        actual = actual_projector_check(accepted, out / "initial-actual-projector.json")
        if not actual["actual_reference_elliptic"]:
            state["phase"] = "accepted-field-principal-ellipticity-test-failed"
            returncode = 5
            return returncode
        for index in range(args.max_stages):
            remaining_distance = args.target_end - state["latest_accepted_end"]
            if remaining_distance <= 2e-13:
                state["phase"] = "requested-open-prefix-target-reached"
                returncode = 0
                break
            if deadline - time.monotonic() < 60:
                state["phase"] = "runner-budget-checkpoint"
                returncode = 124
                break
            step = min(h, remaining_distance)
            attempt = out / ("attempt-" + str(index).zfill(2))
            attempt.mkdir(parents=True, exist_ok=True)
            command = [sys.executable, "-u", str(HERE / "geometry_20261114_public_free3.py"),
                       "--accepted", str(accepted), "--out", str(attempt / "run"),
                       "--work", str(work / ("attempt-" + str(index).zfill(2))),
                       "--durations", repr(step), "--jac-workers", str(args.jac_workers),
                       "--max-nodes", str(args.max_nodes),
                       "--budget-seconds", repr(max(1., deadline - time.monotonic() - 10))]
            write(attempt / "command.json", command)
            state.update(phase="actual-free3-attempt", current_attempt=index)
            write(status, state)
            code = run(command, attempt / "driver.log", deadline)
            child = read(attempt / "run/driver-status.json")
            record = dict(attempt=index, start=state["latest_accepted_end"], duration=step,
                          returncode=code, child_phase=child["phase"], source_accepted_sha256=sha(accepted))
            state["attempts"].append(record)
            if child["phase"] == "preparation-failed":
                log = (attempt / "run/stage-00/prepare.log").read_text()
                if ELLIPTIC_FAILURE not in log:
                    state["phase"] = "other-preparation-failure"
                    returncode = code or 2
                    break
                record["taylor_principal_elliptic_prediction_failed"] = True
                if step / 2 < args.minimum_duration:
                    state["phase"] = "principal-predictor-step-floor"
                    returncode = 6
                    break
                h, streak = step / 2, 0
                state["phase"] = "halving-only-the-failed-preparation-step"
                write(status, state)
                continue
            actual_path = attempt / "run/stage-00/actual.json.gz"
            if actual_path.is_file():
                record.update(accepted_summary(actual_path))
            if code or child["phase"] != "accepted-open-free3-prefix-with-readout" or not record.get("finite_BVP_accepted"):
                state["phase"] = "actual-solver-or-readout-not-accepted"
                returncode = code or 2
                break
            accepted = actual_path
            state.update(latest_accepted_file=str(accepted), latest_accepted_end=record["end"],
                         accepted_stages=state["accepted_stages"] + 1,
                         phase="accepted-new-open-prefix")
            write(status, state)
            print({"event": "accepted-free3-successor", "end": record["end"],
                   "duration": step, "nodes": record["nodes"]}, flush=True)
            streak += 1
            if streak >= 2:
                h, streak = min(args.maximum_duration, 2 * step), 0
            returncode = 0
        else:
            state["phase"] = "stage-budget-checkpoint"
    except subprocess.TimeoutExpired as error:
        state.update(phase="runner-budget-checkpoint", exception=str(error))
        returncode = 124
    except Exception as error:
        state.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        returncode = 1
    finally:
        state.update(ended=now(), returncode=returncode)
        write(status, state)
        print({"event": "adaptive-free3-exit", "phase": state["phase"],
               "latest_accepted_end": state["latest_accepted_end"], "returncode": returncode}, flush=True)
    return returncode


if __name__ == "__main__":
    raise SystemExit(main())
