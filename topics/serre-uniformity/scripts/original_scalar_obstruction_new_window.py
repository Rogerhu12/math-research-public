#!/usr/bin/env python3
"""A disjoint public-Actions search for an original f_N obstruction.

The arithmetic is the already proved R698 algorithm.  This consumer never
tests p <= 200000 and does not assert an all-prime unit theorem.  All raw
outputs remain in runner scratch; only compact receipts are printed.
"""

import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback


class MathDeadline(Exception):
    pass


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(kind, value):
    print(kind + "=" + canonical(value).decode(), flush=True)


def alarm_handler(signum, frame):
    raise MathDeadline("The declared arithmetic budget has expired")


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
        "GITHUB_REPOSITORY"
    ) != "Rogerhu12/math-research-public":
        raise RuntimeError("Mathematical execution is restricted to the public repository Actions")
    started = time.monotonic()
    topic = Path(__file__).resolve().parents[1]
    repo = topic.parents[1]
    request_path = topic / "notes/original-scalar-obstruction-new-window-request.json"
    request = json.loads(request_path.read_text())
    assert request["execution_id"] == "scalar-obstruction-20261127-v1"
    lower, upper = request["lower"], request["upper"]
    assert 200000 < lower <= upper <= 500000
    assert request["residues_mod9"] == [2, 5]
    total_seconds = request["total_seconds"]
    reserve_seconds = request["reserve_seconds"]
    assert 180 <= total_seconds <= 1200 and reserve_seconds >= 90
    deadline = started + total_seconds

    for relative, expected in request["source_sha256"].items():
        path = (repo / relative).resolve()
        path.relative_to(repo)
        assert sha(path) == expected, ("changed_source_or_rules", relative)
    source_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repo, text=True
    ).strip()
    import flint
    from R698_fast_scalar_window import run, primes_in_interval

    requested = primes_in_interval(lower, upper)
    contract = {
        "execution_id": request["execution_id"],
        "source_commit": source_commit,
        "request_sha256": sha(request_path),
        "source_sha256": request["source_sha256"],
        "lower": lower,
        "upper": upper,
        "residues_mod9": [2, 5],
        "requested_count": len(requested),
        "requested_list_sha256": hashlib.sha256(canonical(requested)).hexdigest(),
        "old_primes_recomputed": [],
        "python_flint_version": flint.__version__,
        "total_seconds": total_seconds,
        "reserve_seconds": reserve_seconds,
        "scope": "original f_N only; original g_N is retained as a byproduct",
    }
    emit("CONTRACT", contract)
    rows = []
    g_zeros = []
    pending_prime = None
    zero_check = None
    failure = None
    status = "running"
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, max(0.001, deadline - reserve_seconds - time.monotonic()))

    try:
        for p in requested:
            pending_prime = p
            value = run(p, full=False)
            row = {
                "prime": p,
                "N": value["N"],
                "f_N": value["coefficient_TC"],
                "g_N": value["coefficient_TZ3"],
                "A_p": value["A_p"],
                "A_p_minus_3": value["A_p_minus_3"],
                "C_p": value["C_p"],
                "C_p_minus_3": value["C_p_minus_3"],
                "full_exponential_recurrence_checked": value["full_exponential_recurrence_checked"],
                "maximum_divisor": value["maximum_divisor"],
                "first_excluded_H_denominator": value["first_excluded_H_denominator"],
                "coefficient_sha256": value["coefficient_sha256"],
            }
            assert row["full_exponential_recurrence_checked"]
            assert row["maximum_divisor"] < p == row["first_excluded_H_denominator"]
            rows.append(row)
            del value
            if row["g_N"] == 0:
                g_zeros.append(p)
                emit("NEW_G_ZERO_BYPRODUCT", row)
            if row["f_N"] == 0:
                status = "candidate_f_zero_unverified"
                emit("NEW_F_ZERO_CANDIDATE", row)
                signal.setitimer(signal.ITIMER_REAL, max(0.001, deadline - 30 - time.monotonic()))
                from R698_verify_original_z import run as original_z_run

                independent = original_z_run(p, full=False)
                assert independent["coefficient_x_sigma6"] == row["f_N"]
                assert independent["coefficient_minus_xy_sigma6"] == row["g_N"]
                for name in ["A_p", "A_p_minus_3", "C_p", "C_p_minus_3"]:
                    assert independent[name] == row[name], ("normalization_mismatch", p, name)
                zero_check = independent
                status = "verified_f_zero"
                emit("VERIFIED_F_ZERO", {"main": row, "original_z": independent})
                break
            if len(rows) % 100 == 0:
                emit("PROGRESS", {"completed": len(rows), "last_prime": p,
                                  "elapsed_seconds": time.monotonic() - started})
            pending_prime = None
        else:
            status = "complete_no_f_zero"
    except MathDeadline:
        if status != "candidate_f_zero_unverified":
            status = "budget_prefix_no_f_zero"
    except BaseException as exc:
        status = "error"
        failure = type(exc).__name__ + ": " + str(exc)
        emit("ERROR", {"message": failure, "traceback": traceback.format_exc()[-4000:]})
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)

    observed_f_zeros = [row["prime"] for row in rows if row["f_N"] == 0]
    if observed_f_zeros and status not in {"verified_f_zero", "error"}:
        status = "candidate_f_zero_unverified"
        pending_prime = observed_f_zeros[0]
    completed = [row["prime"] for row in rows]
    assert completed == requested[:len(completed)]
    assert all(p > 200000 for p in completed)
    summary = {
        "status": status,
        "execution_id": request["execution_id"],
        "source_commit": source_commit,
        "requested_count": len(requested),
        "completed_count": len(rows),
        "completed_list_sha256": hashlib.sha256(canonical(completed)).hexdigest(),
        "rows_sha256": hashlib.sha256(canonical(rows)).hexdigest(),
        "first_completed_prime": completed[0] if completed else None,
        "last_completed_prime": completed[-1] if completed else None,
        "all_completed_form_exact_requested_prefix": True,
        "whole_requested_interval_completed": len(completed) == len(requested),
        "new_f_zeros": observed_f_zeros,
        "new_g_zero_byproducts": g_zeros,
        "independent_original_z_zero_check": zero_check,
        "resume_lower": (pending_prime if status == "candidate_f_zero_unverified" else
                         requested[len(completed)] if len(completed) < len(requested) else None),
        "error": failure,
        "old_primes_recomputed": [],
        "division_by_p_used": False,
        "all_prime_unit_claimed": False,
        "elapsed_seconds": time.monotonic() - started,
    }
    assert summary["elapsed_seconds"] < total_seconds
    payload = {"contract": contract, "rows": rows, "summary": summary}
    raw = canonical(payload) + b"\n"
    target = Path(os.environ["RUNNER_TEMP"]) / "serre-original-scalar-obstruction.json"
    target.write_bytes(raw)
    emit("SUMMARY", summary)
    emit("OUTPUT_RECEIPT", {"payload_sha256": hashlib.sha256(raw).hexdigest(),
                            "bytes": len(raw), "runner_scratch_only": True})
    elapsed = time.monotonic() - started
    emit("BUDGET_RECEIPT", {"elapsed_seconds": elapsed, "budget_seconds": total_seconds,
                            "within_budget": elapsed <= total_seconds,
                            "all_prime_unit_claimed": False})
    return 0 if elapsed <= total_seconds and status in {
        "complete_no_f_zero", "budget_prefix_no_f_zero", "verified_f_zero"
    } else 2


if __name__ == "__main__":
    sys.exit(main())
