#!/usr/bin/env python3
"""Check the new original kappa/trace scale at exactly two new primes.

Execution is permitted only in public GitHub Actions, never locally.
Local checks for this file are limited to AST parsing, hashes, and I/O.
Dependency: python-flint==0.9.0 (binary wheel).

CLI:
    python topics/serre-uniformity/scripts/r2_original_kappa_scale_two_prime_consumer.py \
        --budget-seconds 620

The only primes are 1019 and 1031. Their actual original H(0) and T are
consumed from the frozen, completed R963 run; no original moment or trace
is recalculated. New independent calculations are:

    a(x)=(1-x/4)^(N+1) Hrev(x)/H_N, m=2N+1, j=(p^2-1)/3;
    kappa=(1/p)[x^j] a_lift^(2p+2) mod p, using pow_trunc mod p^2;
    Btarget=[x^(m+1)] a(x)^2;
    gp=[Q^p] E4(Q^6)^2/v(Q), from the actual CM eta product.

Here a_lift is the coefficientwise 0,...,p-1 lift of the residual degree-m
polynomial. R960's lift-independence applies. The direct coefficient must
first be divisible by p before the integer division is made.

For P(X)=prod_{n>=1}(1-X^n)^8 and q=Q^6,
    A(q)=sum P_[2j] q^j, B(q)=8P(q^2),
    v(Q)=Q(A(q)+s Q^3 B(q)), s^2=-3,
    gp=[q^(N+1)] E4(q)^2 A(q)/(A(q)^2+3qB(q)^2).
The script checks P(X)_odd=-8X P(X^4), so the oldform phase is audited
independently of the Hasse polynomial. It then checks gp=48Btarget and
kappa=-gp*T modulo p. These are checks of a new formula, not definitions
used to assign kappa or gp.

Only compact JSONL goes to stdout. No arrays, data files, or artifacts
are written. A spawned worker enforces the total budget during FLINT C
calls and records any uncompleted tail rather than claiming completion.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import sys
import time
import traceback


R963_SOURCE_SHA = "efdeebbe23cf971f0d66d39e53964e99a9ccc67c"
R963_RUN_ID = "44731335315"
R963_JOB_ID = "136271559447"
R963_ARITHMETIC_ROWS_SHA256 = "26009267ff3ae699f724fe79d98c0ccabdaf0a81b0dfe41abeb72636cb16cdd5"
CONSUMED_ROWS = {
    1019: {"H0_original": 531, "T_original": 502},
    1031: {"H0_original": 318, "T_original": 394},
}
PRIMES = (1019, 1031)
MAX_BUDGET_SECONDS = 620.0


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def require(condition, message, p):
    if not condition:
        raise ArithmeticError(f"p={p}: {message}")


def coefficient(poly, j):
    return int(poly[j]) if 0 <= j < len(poly) else 0


def actual_hasse_coefficients(p, n):
    """Reuse R939's H recurrence, with the actual H0 consumed from R963."""
    h = [CONSUMED_ROWS[p]["H0_original"]]
    for j in range(n):
        denominator = 3 * (j + 1) * (3 * j + 4) % p
        require(denominator != 0, "zero H recurrence denominator", p)
        h.append(h[-1] * (6 * j + 5) ** 2 * pow(denominator, -1, p) % p)
    require(h[-1] != 0, "H has wrong degree", p)
    return h


def eta_product(p, maximum_degree, nmod_poly):
    """Direct product, independent of H: P(X) modulo X^(maximum_degree+1)."""
    precision = maximum_degree + 1
    binomial_eight = (1, -8, 28, -56, 70, -56, 28, -8, 1)
    result = nmod_poly([1], p)
    for n in range(1, maximum_degree + 1):
        top = min(8, maximum_degree // n)
        factor = [0] * (n * top + 1)
        for e in range(top + 1):
            factor[n * e] = binomial_eight[e] % p
        result = result.mul_low(nmod_poly(factor, p), precision)
    return result


def true_weak_gp(p, n, nmod_poly):
    """Actual original Q^p coefficient, computed only from E4 and eta products."""
    target = n + 1
    precision = target + 1
    product = eta_product(p, 2 * target, nmod_poly)

    # -16*zeta^2=8(1+s). The CM a_2=0 identity converts the rational
    # odd part of F4(Q)/Q into the 8*Q^3*P(Q^12) oldform contribution.
    for j in range(1, 2 * target + 1, 2):
        expected = -8 * coefficient(product, (j - 1) // 4) if j % 4 == 1 else 0
        require(
            coefficient(product, j) == expected % p,
            "eta odd-part / original oldform phase failed", p,
        )

    A = nmod_poly([coefficient(product, 2 * j) for j in range(precision)], p)
    b_coefficients = [0] * precision
    for j in range(target // 2 + 1):
        b_coefficients[2 * j] = 8 * coefficient(product, j) % p
    B = nmod_poly(b_coefficients, p)

    sigma3 = [0] * precision
    for d in range(1, precision):
        d3 = d ** 3 % p
        for j in range(d, precision, d):
            sigma3[j] = (sigma3[j] + d3) % p
    E4 = nmod_poly([1] + [240 * sigma3[j] % p for j in range(1, precision)], p)
    numerator = E4.mul_low(E4, precision).mul_low(A, precision)
    denominator = (
        A.mul_low(A, precision)
        + 3 * B.mul_low(B, precision).left_shift(1)
    ).truncate(precision)
    require(coefficient(denominator, 0) == 1, "eta denominator constant is not one", p)
    inverse = denominator.inverse_series_trunc(precision)
    require(
        denominator.mul_low(inverse, precision).is_one(),
        "eta-series inverse failed", p,
    )
    result = numerator.mul_low(inverse, precision)
    gp = coefficient(result, target)
    require(gp != 0, "proved actual weak Frobenius coefficient became zero", p)
    return gp


def calculate_prime(p, progress=None):
    """Return only compact values for one of the two authorized primes."""
    if p not in CONSUMED_ROWS:
        raise ValueError("this consumer is hard-locked to primes 1019 and 1031")
    import flint
    from flint import nmod_poly

    started = time.monotonic()
    require(flint.__version__ == "0.9.0", "wrong python-flint version", p)
    n = (p - 5) // 6
    m = 2 * n + 1
    j = (p * p - 1) // 3
    require(p == 6 * n + 5 and p % 12 == 11 and p % 9 in (2, 5), "wrong row", p)
    require(j == p * m + 2 * m + 1, "R960 coefficient-index identity failed", p)

    h = actual_hasse_coefficients(p, n)
    Hrev = nmod_poly(list(reversed(h)), p)
    linear = nmod_poly([1, -pow(4, -1, p)], p)
    a = (linear ** (n + 1)) * Hrev * pow(h[-1], -1, p)
    require(a.degree() == m and coefficient(a, 0) == 1, "wrong original a normalization", p)
    Btarget = coefficient(a * a, m + 1)

    gp = true_weak_gp(p, n, nmod_poly)
    require(gp == 48 * Btarget % p, "actual eta gp != 48 Btarget", p)
    if progress is not None:
        progress({
            "event": "stage",
            "stage": "eta_gp_and_primitive_target_checked",
            "p": p,
            "gp_actual_eta": gp,
            "Btarget": Btarget,
            "next": "direct degree-j coefficient modulo p^2",
        })

    # Lift the whole residual a canonically. This uses R960's proved
    # degree-m lift-independence; it does not change any original T.
    p_squared = p * p
    a_lift = nmod_poly([coefficient(a, i) for i in range(m + 1)], p_squared)
    powered = a_lift.pow_trunc(2 * p + 2, j + 1)
    raw_coefficient_mod_p2 = coefficient(powered, j)
    require(
        raw_coefficient_mod_p2 % p == 0,
        "direct formal-group coefficient is not divisible by p", p,
    )
    kappa = (raw_coefficient_mod_p2 // p) % p
    T = CONSUMED_ROWS[p]["T_original"]
    target_kappa = -gp * T % p
    require(kappa == target_kappa, "kappa != -gp * consumed original T", p)
    row = {
        "p": p,
        "N": n,
        "m": m,
        "j": j,
        "H0_consumed": CONSUMED_ROWS[p]["H0_original"],
        "T_original_consumed": T,
        "Btarget": Btarget,
        "gp_actual_eta": gp,
        "coefficient_mod_p2": raw_coefficient_mod_p2,
        "kappa_direct": kappa,
        "minus_gp_T": target_kappa,
        "checks": "eta_oldform_phase,gp_48Btarget,direct_coefficient_divisible_by_p,kappa_minus_gp_T",
        "no_old_moment_or_trace_recomputed": True,
    }
    return row, round(time.monotonic() - started, 6)


def worker_loop(connection):
    while True:
        try:
            p = connection.recv()
        except EOFError:
            break
        if p is None:
            break
        try:
            row, elapsed = calculate_prime(
                p, progress=lambda value: connection.send({"kind": "stage", "value": value})
            )
            connection.send({"kind": "result", "ok": True, "row": row, "seconds": elapsed})
        except BaseException as exc:
            connection.send({
                "kind": "result", "ok": False, "p": p,
                "exception": type(exc).__name__, "message": str(exc),
                "traceback": traceback.format_exc(),
            })
            break
    connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget-seconds", type=float, default=MAX_BUDGET_SECONDS)
    args = parser.parse_args()
    if not 0 < args.budget_seconds <= MAX_BUDGET_SECONDS:
        parser.error("require 0 < budget-seconds <= 620; primes are fixed at 1019,1031")
    import flint
    if flint.__version__ != "0.9.0":
        parser.error(f"require python-flint 0.9.0, found {flint.__version__}")

    started = time.monotonic()
    deadline = started + args.budget_seconds - min(3.0, args.budget_seconds / 4.0)
    script_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rows_digest = hashlib.sha256()
    prefix_digest = hashlib.sha256()

    def emit(value):
        payload = canonical_bytes(value)
        sys.stdout.write(payload.decode("utf-8") + "\n")
        sys.stdout.flush()
        prefix_digest.update(payload + b"\n")

    emit({
        "event": "start",
        "script_sha256": script_sha256,
        "python_flint_version": flint.__version__,
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_source_sha": os.environ.get("GITHUB_SHA"),
        "primes": list(PRIMES),
        "budget_seconds": args.budget_seconds,
        "consumed_R963_source": R963_SOURCE_SHA,
        "consumed_R963_run": R963_RUN_ID,
        "consumed_R963_job": R963_JOB_ID,
        "consumed_R963_rows_sha256": R963_ARITHMETIC_ROWS_SHA256,
        "consumed_rows": {str(p): CONSUMED_ROWS[p] for p in PRIMES},
        "scope": "new exact-scale check only; no moment or trace rescan",
    })

    context = multiprocessing.get_context("spawn")
    parent_connection, child_connection = context.Pipe()
    process = context.Process(target=worker_loop, args=(child_connection,), daemon=True)
    process.start()
    child_connection.close()
    completed = 0
    pending = None
    reason = "completed"
    failure = None
    try:
        for p in PRIMES:
            pending = p
            if deadline - time.monotonic() <= 0:
                reason = "budget"
                break
            try:
                parent_connection.send(p)
            except (BrokenPipeError, EOFError, OSError) as exc:
                reason = "worker_error"
                failure = {"p": p, "exception": type(exc).__name__, "message": str(exc)}
                break
            result = None
            while result is None:
                remaining = deadline - time.monotonic()
                if remaining <= 0 or not parent_connection.poll(remaining):
                    reason = "budget"
                    break
                try:
                    message = parent_connection.recv()
                except EOFError:
                    reason = "worker_error"
                    failure = {"p": p, "exception": "WorkerExit", "exitcode": process.exitcode}
                    break
                if message["kind"] == "stage":
                    emit(message["value"])
                else:
                    result = message
            if reason != "completed":
                break
            if not result["ok"]:
                reason = "verification_error"
                failure = result
                emit({"event": "error", **result})
                break
            row = result["row"]
            rows_digest.update(canonical_bytes(row) + b"\n")
            emit({"event": "row", **row, "seconds": result["seconds"]})
            completed += 1
            pending = None
    finally:
        if process.is_alive():
            if reason == "completed":
                try:
                    parent_connection.send(None)
                except (BrokenPipeError, EOFError):
                    pass
                process.join(timeout=min(1.0, max(0.0, deadline - time.monotonic())))
            if process.is_alive():
                process.terminate()
                process.join(timeout=1.0)
                if process.is_alive():
                    process.kill()
                    process.join(timeout=1.0)
        parent_connection.close()

    summary = {
        "event": "summary",
        "status": reason,
        "finite_two_prime_check_only": True,
        "candidate_count": len(PRIMES),
        "completed_count": completed,
        "completed_primes": list(PRIMES[:completed]),
        "uncompleted_primes": list(PRIMES[completed:]),
        "incomplete_prime_at_stop": pending,
        "arithmetic_rows_sha256": rows_digest.hexdigest(),
        "stdout_before_summary_sha256": prefix_digest.hexdigest(),
        "script_sha256": script_sha256,
        "python_flint_version": flint.__version__,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "failure": failure,
    }
    summary["summary_payload_sha256"] = hashlib.sha256(canonical_bytes(summary)).hexdigest()
    emit(summary)
    return 1 if reason in ("worker_error", "verification_error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
