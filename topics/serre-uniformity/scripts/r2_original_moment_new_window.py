#!/usr/bin/env python3
"""New original r=2 moment window, for execution only in public Actions.

No mathematical execution is permitted locally by the repository rules.
The only local checks intended for this file are AST parsing and hashing.

Dependencies: python-flint==0.9.0 (binary wheel).
CLI:
    python scripts/r2_original_moment_new_window.py \
        --minimum 1001 --maximum 100000 --budget-seconds 650

Only primes 1000 < p <= 100000 with p == 11 mod 12 and p == 2 or 5
mod 9 are accepted. Old R936/R939 ranges cannot be requested. The first
zero moment stops the scan after an explicit original Cartier-preimage
certificate has been checked. Budget expiration records the unfinished
prime and all remaining coverage honestly. A persistent spawned worker
lets the parent enforce the time budget even during a FLINT C call.

All output is JSONL on stdout. This file writes no data files.
Per-prime raw arrays are returned only for the first zero certificate.
No array, regenerated output, or numerical certificate belongs in Git.

Original normalization, from R936/R939/R958:
    H(0) = 3 (3N+2)! / ((2N+1)! N! 2^N),  p=6N+5.
    C = s*C0,  s^2=-3,  C^p=-s*C0(t)^p.
    R_F/s = 2 D^(2N+1) beta^2 C0^p mod tH.
    c_mom/s = Tr((3-2e0) D C0 / beta^2) = c0mom.
    T = 3 Tr((3-2e0) D^(2N+2) C0^(p+1)).
    moment_over_s = ell_N(R_F/s).
    T = (3/2) c0mom * moment_over_s, S^p = 432 T.
The H and C0 recurrences are O(N). Polynomial powering/reduction uses
FLINT nmod_poly, and trace uses the Euler coefficient with a monic modulus.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import multiprocessing
import os
from pathlib import Path
import sys
import time
import traceback


ABSOLUTE_MINIMUM = 1001
ABSOLUTE_MAXIMUM = 100000
MAX_BUDGET_SECONDS = 650.0


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def require(condition, label, p):
    if not condition:
        raise ArithmeticError(f"p={p}: {label}")


def is_prime(p):
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    return all(p % d for d in range(3, math.isqrt(p) + 1, 2))


def allowed_prime(p):
    return (
        ABSOLUTE_MINIMUM <= p <= ABSOLUTE_MAXIMUM
        and p % 12 == 11
        and p % 9 in (2, 5)
        and is_prime(p)
    )


def candidate_primes(minimum, maximum):
    """Deterministic sieve; does not include any old window prime."""
    flags = bytearray(b"\x01") * (maximum + 1)
    flags[0:2] = b"\x00\x00"
    for q in range(2, math.isqrt(maximum) + 1):
        if flags[q]:
            first = q * q
            flags[first: maximum + 1: q] = b"\x00" * (
                (maximum - first) // q + 1
            )
    return [
        p for p in range(minimum, maximum + 1)
        if flags[p] and p % 12 == 11 and p % 9 in (2, 5)
    ]


def batch_inverses(values, p):
    """Unit inverses with one field inversion and O(len(values)) products."""
    prefix = []
    product = 1
    for value in values:
        value %= p
        require(value != 0, "zero recurrence denominator", p)
        prefix.append(product)
        product = product * value % p
    inverse_product = pow(product, -1, p)
    answer = [0] * len(values)
    for j in range(len(values) - 1, -1, -1):
        answer[j] = inverse_product * prefix[j] % p
        inverse_product = inverse_product * (values[j] % p) % p
    return answer


def original_h0(p, n):
    """The a=0 term of R936's actual Hasse coefficient, not a rescaling."""
    factorial = 1
    chosen = {0: 1}
    targets = {n, 2 * n + 1, 3 * n + 2}
    for j in range(1, 3 * n + 3):
        factorial = factorial * j % p
        if j in targets:
            chosen[j] = factorial
    denominator = chosen[2 * n + 1] * chosen[n] * pow(2, n, p) % p
    return 3 * chosen[3 * n + 2] * pow(denominator, -1, p) % p


def original_coefficients(p, n):
    """Return actual H and C/s from R939.12 and R939.27."""
    h0 = original_h0(p, n)
    require(h0 != 0, "original H(0) is zero", p)
    h = [h0]
    inv_h = batch_inverses(
        [3 * (j + 1) * (3 * j + 4) % p for j in range(n)], p
    )
    for j in range(n):
        h.append(h[-1] * (6 * j + 5) ** 2 * inv_h[j] % p)
    require(h[-1] != 0, "original H has wrong degree", p)

    inv_c = batch_inverses(
        [3 * (2 * j + 1) ** 2 % p for j in range(n + 1)], p
    )
    inv9 = pow(9, -1, p)
    c = [0] * (n + 2)
    for j in range(n, -1, -1):
        c[j] = (
            (j + 1) * (3 * j + 2) * c[j + 1] + inv9 * h[j]
        ) * inv_c[j] % p
    return h, c[:-1]


def moment_weights(p, n):
    inverses = batch_inverses(
        [(6 * j + 7) ** 2 % p for j in range(n)], p
    )
    weights = [1]
    for j in range(n):
        weights.append(
            weights[-1] * (3 * j + 1) * (3 * j + 2) * inverses[j] % p
        )
    return weights


def coefficient(poly, j):
    """nmod_poly indexing is zero outside its nonnegative coefficient range."""
    return int(poly[j]) if 0 <= j < len(poly) else 0


def evaluate_coefficients(coefficients, value, p):
    out = 0
    for entry in reversed(coefficients):
        out = (out * value + entry) % p
    return out


def calculate_prime(p):
    """Return one verified compact row and, only at zero, its certificate."""
    if not allowed_prime(p):
        raise ValueError("require NEW allowed r=2 prime, 1000 < p <= 100000")
    import flint
    from flint import nmod_poly

    started = time.monotonic()
    n = (p - 5) // 6
    h_coeffs, c_coeffs = original_coefficients(p, n)
    H = nmod_poly(h_coeffs, p)
    C0 = nmod_poly(c_coeffs, p)
    t = nmod_poly([0, 1], p)
    D = nmod_poly([1, -4], p)
    x = nmod_poly([1, -8], p)
    one = nmod_poly([1], p)
    zero = nmod_poly([], p)
    inv3 = pow(3, -1, p)
    inv2 = pow(2, -1, p)

    hp = H.derivative()
    require(
        9 * t * D * hp.derivative() + 12 * x * hp - 25 * H == zero,
        "fixed original Hasse ODE failed", p,
    )
    beta_full = -(x * H + 3 * t * D * hp)
    require(
        beta_full.derivative() == -inv3 * H,
        "beta' = -H/3 failed", p,
    )
    cp = C0.derivative()
    lplus = (
        9 * t * D * cp.derivative()
        + 6 * nmod_poly([1, -12], p) * cp
        - 9 * C0
    )
    require(lplus == -inv3 * H, "L_+(C/s) = -H/3 failed", p)
    require(
        evaluate_coefficients(h_coeffs, pow(4, -1, p), p) != 0,
        "unexpected original elliptic Hasse zero", p,
    )

    # Only the modulus is made monic. H and C0 retain their original scales.
    modulus = (t * H) * pow(h_coeffs[-1], -1, p)
    degree = n + 1
    require(
        modulus.degree() == degree and coefficient(modulus, degree) == 1,
        "nonmonic or wrong-degree modulus", p,
    )
    md = modulus.derivative()
    require(modulus.gcd(md).is_one(), "tH is not etale", p)
    beta = beta_full % modulus

    # beta^(p-3) is beta^-2 by the established Baker identity.
    # Verify that identity, not just the intended inverse name.
    reverse_inverse = modulus.reverse().inverse_series_trunc(degree + 1)
    beta_minus2 = beta.pow_mod(p - 3, modulus, reverse_inverse)
    beta2 = (beta * beta) % modulus
    require(
        (beta_minus2 * beta2) % modulus == one,
        "beta^(p-1)=1 failed on the full tH algebra", p,
    )

    d_power = D.pow_mod(2 * n + 1, modulus, reverse_inverse)
    c_power = C0.pow_mod(p, modulus, reverse_inverse)
    # C^p=-s*C0^p, so the original -2C^p becomes +2s*C0^p.
    R_over_s = (((2 * d_power * beta2) % modulus) * c_power) % modulus
    weights = moment_weights(p, n)
    moment = sum(
        coefficient(R_over_s, j) * weights[j] for j in range(n + 1)
    ) % p

    e0 = H * pow(h_coeffs[0], -1, p)
    full_weight = 3 * one - 2 * e0
    require(
        (e0 * e0 - e0) % modulus == zero,
        "t=0 idempotent failed", p,
    )

    def trace(poly):
        return coefficient(((poly % modulus) * md) % modulus, degree - 1)

    cmom_over_s = trace(full_weight * D * C0 * beta_minus2)
    require(cmom_over_s != 0, "proved nonzero c_mom/s became zero", p)
    T_original = 3 * trace(
        full_weight * ((d_power * D) % modulus) * C0 * c_power
    ) % p
    expected_T = 3 * inv2 * cmom_over_s * moment % p
    require(
        T_original == expected_T,
        "original scale T=(3/2)(c_mom/s)(ell(R_F)/s) failed", p,
    )
    S_original_p = 432 * T_original % p
    require(
        S_original_p == 648 * cmom_over_s * moment % p,
        "original S^p scale failed", p,
    )

    arithmetic_row = {
        "p": p,
        "N": n,
        "H0_original": h_coeffs[0],
        "moment_over_s": moment,
        "c_mom_over_s": cmom_over_s,
        "T_original": T_original,
        "S_original_p": S_original_p,
        "checks": "H_ODE,C_negative_ODE,beta_derivative,etale,Baker,weights,original_trace_scale",
    }
    certificate = None
    if moment == 0:
        # Independent, explicit full opposite-deck Cartier preimage.
        # L_- Ktilde=R_F/s; actual K=s*Ktilde and U(h_K)=F.
        diagonal_inverse = batch_inverses(
            [(3 * j + 1) * (3 * j + 2) % p for j in range(n)], p
        )
        k_coeffs = [0] * n
        previous = 0
        for j in range(n):
            rhs = coefficient(R_over_s, j)
            if j:
                rhs += (6 * j + 1) ** 2 * previous
            previous = rhs * diagonal_inverse[j] % p
            k_coeffs[j] = previous
        Ktilde = nmod_poly(k_coeffs, p)
        kp = Ktilde.derivative()
        lminus = (
            9 * t * t * D * kp.derivative()
            + 6 * t * nmod_poly([3, -20], p) * kp
            + nmod_poly([2, -49], p) * Ktilde
        )
        require(lminus == R_over_s, "zero moment did not yield L_- preimage", p)
        require(
            T_original == 0 and S_original_p == 0,
            "moment zero disagrees with original complete trace", p,
        )
        certificate = {
            "kind": "first_original_r2_zero_with_Cartier_preimage",
            "p": p,
            "N": n,
            "field": "Fp(s), s^2=-3, original phase; all listed arrays are Fp",
            "coefficient_order": "ascending",
            "H_original": h_coeffs,
            "C_original_over_s": c_coeffs,
            "R_F_over_s": [coefficient(R_over_s, j) for j in range(n + 1)],
            "ell_N_moments": weights,
            "preimage_K_over_s": k_coeffs,
            "witness": (
                "L_-(K_over_s)=R_F/s; actual Hminus="
                "s*u^2*D^(N+1)*K_over_s(t) satisfies original U(Hminus)=F"
            ),
            "full_point_weights": "t=0 weight 1; every H root weight 3; elliptic zeros retained",
            "arithmetic_row": arithmetic_row,
        }
    return arithmetic_row, certificate, round(time.monotonic() - started, 6)


def worker_loop(connection):
    while True:
        try:
            p = connection.recv()
        except EOFError:
            break
        if p is None:
            break
        try:
            row, certificate, elapsed = calculate_prime(p)
            connection.send({"ok": True, "row": row, "certificate": certificate, "seconds": elapsed})
        except BaseException as exc:
            connection.send({
                "ok": False,
                "p": p,
                "exception": type(exc).__name__,
                "message": str(exc),
                "traceback": traceback.format_exc(),
            })
            break
    connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minimum", type=int, default=ABSOLUTE_MINIMUM)
    parser.add_argument("--maximum", type=int, default=ABSOLUTE_MAXIMUM)
    parser.add_argument("--budget-seconds", type=float, default=MAX_BUDGET_SECONDS)
    args = parser.parse_args()
    if not (
        ABSOLUTE_MINIMUM <= args.minimum <= args.maximum <= ABSOLUTE_MAXIMUM
        and 0 < args.budget_seconds <= MAX_BUDGET_SECONDS
    ):
        parser.error("require 1001 <= minimum <= maximum <= 100000 and 0 < budget <= 650")

    import flint
    flint_version = flint.__version__
    if flint_version != "0.9.0":
        parser.error(f"require pinned python-flint 0.9.0, found {flint_version}")

    started = time.monotonic()
    # Keep time for worker termination and a truthful final JSON summary.
    cleanup_reserve = min(3.0, args.budget_seconds / 4.0)
    deadline = started + args.budget_seconds - cleanup_reserve
    candidates = candidate_primes(args.minimum, args.maximum)
    script_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rows_digest = hashlib.sha256()
    stdout_prefix_digest = hashlib.sha256()

    def emit(value):
        payload = canonical_bytes(value)
        sys.stdout.write(payload.decode("utf-8") + "\n")
        sys.stdout.flush()
        stdout_prefix_digest.update(payload + b"\n")

    emit({
        "event": "start",
        "script_sha256": script_sha256,
        "python_flint_version": flint_version,
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_source_sha": os.environ.get("GITHUB_SHA"),
        "minimum": args.minimum,
        "maximum": args.maximum,
        "allowed_classes": "p prime, p=11 mod12, p=2 or5 mod9",
        "candidate_count": len(candidates),
        "budget_seconds": args.budget_seconds,
        "old_window_excluded": "all p<=1000",
        "normalization": "original H0; C=sC0; R_F/s=+2 D^(2N+1) beta^2 C0^p",
    })

    context = multiprocessing.get_context("spawn")
    parent_connection, child_connection = context.Pipe()
    process = context.Process(target=worker_loop, args=(child_connection,), daemon=True)
    process.start()
    child_connection.close()
    completed = 0
    first_zero = None
    certificate_sha256 = None
    failure = None
    pending_p = None
    reason = "completed"
    try:
        for p in candidates:
            pending_p = p
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                reason = "budget"
                break
            try:
                parent_connection.send(p)
            except (BrokenPipeError, EOFError, OSError) as exc:
                failure = {
                    "p": p, "exception": type(exc).__name__,
                    "message": str(exc), "exitcode": process.exitcode,
                }
                reason = "worker_error"
                break
            if not parent_connection.poll(remaining):
                reason = "budget"
                break
            try:
                result = parent_connection.recv()
            except EOFError:
                failure = {"p": p, "exception": "WorkerExit", "exitcode": process.exitcode}
                reason = "worker_error"
                break
            if not result["ok"]:
                failure = result
                reason = "verification_error"
                emit({"event": "error", **result})
                break
            row = result["row"]
            rows_digest.update(canonical_bytes(row) + b"\n")
            completed += 1
            emit({"event": "row", **row, "seconds": result["seconds"]})
            if result["certificate"] is not None:
                first_zero = p
                certificate_sha256 = hashlib.sha256(
                    canonical_bytes(result["certificate"])
                ).hexdigest()
                emit({
                    "event": "zero_certificate",
                    "certificate_sha256": certificate_sha256,
                    "certificate": result["certificate"],
                })
                reason = "first_zero"
                break
            pending_p = None
    finally:
        if process.is_alive():
            if reason == "completed" or reason == "first_zero":
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

    remaining_candidates = candidates[completed:]
    summary = {
        "event": "summary",
        "status": reason,
        "finite_window_only": True,
        "requested_minimum": args.minimum,
        "requested_maximum": args.maximum,
        "candidate_count": len(candidates),
        "completed_count": completed,
        "first_completed_prime": candidates[0] if completed else None,
        "last_completed_prime": candidates[completed - 1] if completed else None,
        "first_zero": first_zero,
        "zero_certificate_sha256": certificate_sha256,
        "arithmetic_rows_sha256": rows_digest.hexdigest(),
        "stdout_before_summary_sha256": stdout_prefix_digest.hexdigest(),
        "uncompleted_count": len(remaining_candidates),
        "first_uncompleted_prime": remaining_candidates[0] if remaining_candidates else None,
        "last_uncompleted_prime": remaining_candidates[-1] if remaining_candidates else None,
        "uncompleted_prime_list_sha256": hashlib.sha256(canonical_bytes(remaining_candidates)).hexdigest(),
        "incomplete_prime_at_stop": pending_p if reason in ("budget", "verification_error", "worker_error") else None,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "script_sha256": script_sha256,
        "python_flint_version": flint_version,
        "failure": failure,
    }
    summary["summary_payload_sha256"] = hashlib.sha256(canonical_bytes(summary)).hexdigest()
    emit(summary)
    return 1 if reason in ("verification_error", "worker_error") else 0


if __name__ == "__main__":
    raise SystemExit(main())

