#!/usr/bin/env python3
"""New original r=8 balanced window, with independent original-source checks.

Mathematical execution is restricted to this public repository's Actions.
R990 supplies the fixed-r hypergeometric main channel.  R989 supplies an
independent sparse Chazy/CDQ channel and a separate E_- sigma/single-carry
contraction.  No old prime <=1000 or old r=2 window is recomputed.
Local use: source reading, AST parsing, file metadata and hashes only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing
import os
from pathlib import Path
import queue
import sys
import time
import traceback


TOPIC = Path(__file__).resolve().parents[1]
MAXIMUM_BUDGET = 620.0
MINIMUM_BOUND = 1000
MAXIMUM_BOUND = 20000
R = 8
R990_SOURCE = "results/R990-original-hypergeometric-fixed-r-coefficient.md"
EXPECTED_R990_SHA256 = "5c35e72804eee83dde2c74af68232dea3a57c5d97ba39026a07329a7db25a7a1"
METHOD_SOURCE = "notes/R989-original-r8-sparse-heat-and-Kronecker-window-method.md"
# None of the registered old r=8 data intersects the default window.
# Any addition here requires an actual earlier receipt and a reviewed request.
ADDITIONAL_REGISTERED_PRIMES = frozenset()


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def emit(value):
    print(json.dumps(value, sort_keys=True), flush=True)


def source_receipts(r990_source):
    paths = (
        METHOD_SOURCE,
        r990_source,
        "results/R975-original-balanced-Kronecker-integral-heat-recurrence.md",
        "results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md",
        "notes/R973-original-balanced-Kronecker-four-prime-execution-method.md",
    )
    receipt = {}
    for name in paths:
        path = (TOPIC / name).resolve()
        relative = path.relative_to(TOPIC)
        require(path.is_file(), f"required source absent: {relative}")
        receipt[str(relative)] = hashlib.sha256(path.read_bytes()).hexdigest()
        if name == r990_source:
            require(receipt[str(relative)] == EXPECTED_R990_SHA256,
                    "R990 source changed: review and refreeze the consumer before execution")
    receipt["scripts/" + Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return receipt


def requested_primes(minimum, maximum):
    """Exact sieve, called only after the public-Actions guard."""
    sieve = bytearray(b"\x01") * (maximum + 1)
    sieve[0:2] = b"\x00\x00"
    d = 2
    while d * d <= maximum:
        if sieve[d]:
            start = d * d
            sieve[start:maximum + 1:d] = b"\x00" * (((maximum - start) // d) + 1)
        d += 1
    candidates = [p for p in range(minimum + 1, maximum + 1)
                  if sieve[p] and p % 12 == 5 and p % 9 in (2, 5)]
    excluded = [p for p in candidates if p in ADDITIONAL_REGISTERED_PRIMES]
    requested = [p for p in candidates if p not in ADDITIONAL_REGISTERED_PRIMES]
    return requested, excluded


def inverses(p):
    values = [0] * p
    values[1] = 1
    for i in range(2, p):
        values[i] = (-(p // i) * values[p % i]) % p
    return values


def coefficients(poly, length):
    return [int(poly[i]) for i in range(length)]


def hypergeometric_coefficient(p, inv, nmod_poly):
    """R990.21, .24, .26, .27 in the actual E_+ frame."""
    require(p > MINIMUM_BOUND and p % 12 == 5 and p % 9 in (2, 5),
            "main channel outside the original new r=8 scope")
    n = p - R
    k, m, resonance = p // 12, n // 3, (p + 1) // 3
    require(n % 6 == 3 and m == 4 * k - 1 and m == resonance - 3,
            f"p={p}: actual r=8 indices changed")
    b = [1]
    for i in range(1, k + 1):
        value = b[-1] * (i - 1 - k) * (3 * k + 3 * i + 1)
        value = value * inv[i] * inv[3 * i + 1] % p
        require(value != 0, f"p={p}: Jacobi polynomial degree dropped")
        b.append(value)
    B = nmod_poly(b, p)
    denominator = B.mul_low(B, resonance + 1).mul_low(nmod_poly([1, p - 1], p), resonance + 1)
    H = denominator.inverse_series_trunc(resonance + 1)
    b_at_one = sum(b) % p
    require(b_at_one != 0, f"p={p}: original Jacobi cusp value vanished")
    require(int(H[resonance]) == inv[b_at_one] ** 2 % p,
            f"p={p}: actual first resonance identity failed")
    f_values = []
    for i in range(m + 1):
        divisor = (1 - 3 * i) % p
        require(divisor != 0, f"p={p}: attempted to cross the first resonance")
        f_values.append(int(H[i]) * inv[divisor] % p)
    f = nmod_poly(f_values, p)
    require(f_values[0] == 1, f"p={p}: original period ratio lost its constant")
    logarithmic_B = B.derivative().mul_low(B.inverse_series_trunc(m), m)
    Q = nmod_poly([4] + [(12 * int(logarithmic_B[i - 1]) - 1) % p
                         for i in range(1, m + 1)], p)
    f_inverse = f.inverse_series_trunc(m + 1)
    target = int(Q.mul_low(f_inverse.pow_trunc(R, m + 1), m + 1)[m])
    # 7!/4 = 1260 is the actual Wilson factor for r=8, not a fitted unit.
    scale = pow((-32) % p, m, p) * 1260 % p
    value = scale * target % p
    return value, {
        "channel": "R990_original_fixed_r_hypergeometric",
        "k": k, "m": m, "first_resonance": resonance,
        "J_p_r": target, "original_scale": scale,
        "c_plus": value, "c_minus": (-value) % p,
        "first_resonance_identity_verified": True,
        "Jacobi_B_sha256": digest(b),
        "period_ratio_prefix_sha256": digest(f_values),
        "H_prefix_sha256": digest(coefficients(H, resonance + 1)),
    }


def chazy_cdq_coefficient(p, inv, nmod_poly):
    """R989M.11--14: two causal convolutions with exact pair ownership."""
    n = p - R
    M = (n - 3) // 3
    length = M + 1
    a, v = [0] * length, [0] * length
    square, weighted_square = [0] * length, [0] * length

    def solve(left, right):
        if right - left == 1:
            index = left
            if index == 0:
                a[0] = 12 % p
            else:
                j = index - 1
                numerator = ((9 * j * j - 9 * j - 8) * square[index]
                             - 45 * weighted_square[index]) % p
                denominator_inverse = (inv[6] * inv[index]
                                       * inv[3 * index + 1] * inv[3 * index + 2]) % p
                a[index] = numerator * denominator_inverse % p
            v[index] = index * a[index] % p
            return
        middle = (left + right) // 2
        solve(left, middle)
        limit = right - left - 1
        prefix_end = min(middle, limit)
        for sequence, accumulator in ((a, square), (v, weighted_square)):
            new = sequence[left:middle]
            prefix = sequence[:prefix_end]
            # new*prefix + previous*new, retaining global prefix exponents.
            for j in range(min(left, prefix_end)):
                prefix[j] = 2 * prefix[j] % p
            product = nmod_poly(new, p).mul_low(nmod_poly(prefix, p), limit)
            for target in range(middle, right):
                accumulator[target] = (accumulator[target]
                                       + int(product[target - 1 - left])) % p
        solve(middle, right)

    solve(0, length)
    value = 420 * a[M] % p
    return value, {
        "channel": "R989_original_Chazy_CDQ",
        "M": M, "a_M": a[M], "c_plus": value,
        "a_prefix_sha256": digest(a),
        "v_weighting": "v_i=i*a_i with the original global index",
    }


def exp_series_from_log(logarithm, length, p, inv, nmod_poly):
    """Exact Newton exponential; no unavailable polynomial API is assumed."""
    result = nmod_poly([1], p)
    known = 1
    while known < length:
        new_length = min(2 * known, length)
        reciprocal = result.inverse_series_trunc(new_length)
        logarithmic_derivative = result.derivative().mul_low(reciprocal, new_length - 1)
        log_result = [0] + [int(logarithmic_derivative[i - 1]) * inv[i] % p
                            for i in range(1, new_length)]
        correction = [(logarithm[i] - log_result[i]) % p for i in range(new_length)]
        correction[0] = (correction[0] + 1) % p
        result = result.mul_low(nmod_poly(correction, p), new_length)
        known = new_length
    return result


def original_sigma_coefficient(p, inv, nmod_poly):
    """Independent original E_- sigma ODE and the exact one-carry product."""
    n, N = p - R, (p - 5) // 6
    t = (n - 3) // 6
    require(t == N - 1, f"p={p}: original r=8 sigma block changed")
    # This direct ODE is independent of the heat/CDQ and hypergeometric paths.
    X = [0] * (N + 1)
    X[1] = inv[7]
    for j in range(2, N + 1):
        total = sum(X[i] * X[j - i] for i in range(1, j)) % p
        X[j] = total * inv[6 * j + 1] * inv[j - 1] % p
    logarithm = [0] + [(-X[j] * inv[6 * j] * inv[6 * j - 1]) % p
                       for j in range(1, N + 1)]
    sigma_poly = exp_series_from_log(logarithm, N + 1, p, inv, nmod_poly)
    inverse_poly = sigma_poly.inverse_series_trunc(N + 1)
    require(sigma_poly.mul_low(inverse_poly, N + 1) == nmod_poly([1], p),
            f"p={p}: original sigma inverse identity failed")
    require(sigma_poly.derivative().truncate(N)
            == nmod_poly(logarithm, p).derivative().mul_low(sigma_poly, N),
            f"p={p}: original sigma exponential identity failed")
    sigma = coefficients(sigma_poly, N + 1)
    inverse_sigma = coefficients(inverse_poly, t + 1)
    require(sigma[1] == (-inv[210 % p]) % p,
            f"p={p}: original E_- sigma phase changed")
    factorial = [1] * p
    for j in range(1, p):
        factorial[j] = factorial[j - 1] * j % p
    inverse_factorial = [1] * p
    inverse_factorial[p - 1] = pow(factorial[p - 1], -1, p)
    for j in range(p - 1, 0, -1):
        inverse_factorial[j - 1] = inverse_factorial[j] * j % p
    d, endpoint = (p - 1) // 2, (p - 2) // 3
    B = factorial[d] * inverse_factorial[endpoint] * inverse_factorial[d - endpoint] % p
    if (d - endpoint) % 2:
        B = (-B) % p
    require(B != 0, f"p={p}: fixed original first-pole B vanished")
    U = nmod_poly([inverse_sigma[i] * inverse_factorial[n + 1 - 6 * i] % p
                   for i in range(t + 1)], p)
    V = nmod_poly([inverse_sigma[i] * inverse_factorial[n - 6 * i] % p
                   for i in range(t + 1)], p)
    product = U.mul_low(V, 2 * t + 1)
    value = 0
    low_terms = high_terms = 0
    for k in range(2 * t + 2):
        if k <= N:
            weight = sigma[k] * factorial[6 * k + 1] % p
            low_terms += 1
        else:
            h = 6 * k + 1 - p
            require(0 < h < p, f"p={p}: actual single-carry factorial crossed its range")
            weight = B * sigma[k - N - 1] * factorial[h] % p
            high_terms += 1
        value = (value + int(product[2 * t + 1 - k]) * weight) % p
    return value, {
        "channel": "R973_original_E_minus_sigma_single_carry_contraction",
        "N": N, "t": t, "original_B": B,
        "c_minus": value, "c_plus": (-value) % p,
        "original_sigma_phase": "g2=0,g3=4; sigma=z-z^7/210+...; no Gaussian",
        "low_contracted_terms": low_terms, "single_carry_contracted_terms": high_terms,
        "wp_low_prefix_sha256": digest(X),
        "sigma_low_prefix_sha256": digest(sigma),
        "sigma_inverse_prefix_sha256": digest(inverse_sigma),
        "original_low_sigma_and_inverse_verified": True,
    }


def worker(messages, requested, check_primes):
    pending_prime = None
    try:
        import flint
        from flint import nmod_poly
        require(flint.__version__ == "0.9.0", "unfrozen python-flint runtime")
        for p in requested:
            pending_prime = p
            inv = inverses(p)
            value, primary = hypergeometric_coefficient(p, inv, nmod_poly)
            zero = value == 0
            if zero:
                messages.put({"kind": "r8_provisional_zero", "p": p,
                              "source_checks_completed": False})
            independent = None
            if p in check_primes or zero:
                heat_value, heat_record = chazy_cdq_coefficient(p, inv, nmod_poly)
                sigma_value, sigma_record = original_sigma_coefficient(p, inv, nmod_poly)
                require(heat_value == value, f"p={p}: original heat and hypergeometric channels disagree")
                require((-sigma_value) % p == value,
                        f"p={p}: original sigma source and E_+ phase comparison failed")
                independent = {"heat": heat_record, "original_sigma": sigma_record,
                               "all_three_original_sources_agree": True}
            row = {"kind": "r8_balanced_prime", "p": p, "r": R, "n": p - R,
                   "prime_mod_12": p % 12, "prime_mod_9": p % 9,
                   "c_plus": value, "c_minus": (-value) % p,
                   "is_zero": zero, "primary": primary,
                   "independent_checks": independent,
                   "original_complete_trace_zero_by_R988": zero}
            messages.put(row)
            if zero:
                messages.put({"kind": "worker_complete", "status": "first_zero_verified", "p": p})
                return
        messages.put({"kind": "worker_complete", "status": "complete_nonzero_window"})
    except BaseException as exc:
        messages.put({"kind": "worker_error", "p": pending_prime,
                      "error": str(exc), "traceback": traceback.format_exc()})


def main():
    require(os.environ.get("GITHUB_ACTIONS") == "true", "mathematics requires public GitHub Actions")
    require(os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public", "wrong public repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--minimum", type=int, default=MINIMUM_BOUND)
    parser.add_argument("--maximum", type=int, default=MAXIMUM_BOUND)
    parser.add_argument("--budget-seconds", type=float, default=MAXIMUM_BUDGET)
    parser.add_argument("--r990-source", default=R990_SOURCE)
    parser.add_argument("--output")
    args = parser.parse_args()
    require(MINIMUM_BOUND <= args.minimum < args.maximum <= MAXIMUM_BOUND,
            "require 1000 <= minimum < maximum <= 20000")
    require(0 < args.budget_seconds <= MAXIMUM_BUDGET, "invalid budget")
    started = time.monotonic()
    receipts = source_receipts(args.r990_source)
    requested, excluded = requested_primes(args.minimum, args.maximum)
    require(requested, "empty new-prime difference set")
    check_primes = set(requested[:2])
    contract = {
        "kind": "r8_balanced_window_contract",
        "minimum_exclusive": args.minimum, "maximum_inclusive": args.maximum,
        "prime_conditions": "p%12==5 and p%9 in (2,5)",
        "r": R, "coefficient_index": "n=p-8",
        "requested_new_primes": requested, "requested_primes_sha256": digest(requested),
        "excluded_registered_primes_in_range": excluded,
        "old_coverage_audit": {
            "R936_R939": "original both-row trace at old finite points and 109<=p<=1000",
            "R973_R983": [41, 47, 227, 857],
            "R963": "1000<p<=100000, r=2 only, p%12==11; disjoint",
        },
        "scheduled_independent_check_primes": sorted(check_primes),
        "first_zero_requires_original_sigma_and_CDQ": True,
        "maximum_budget_seconds": args.budget_seconds,
        "source_sha256": receipts, "runtime": "python-flint==0.9.0",
        "raw_arrays_saved": False, "all_prime_nonvanishing_assumed": False,
    }
    emit(contract)
    context = multiprocessing.get_context("spawn")
    messages = context.Queue()
    process = context.Process(target=worker, args=(messages, requested, check_primes))
    process.start()
    rows, terminal, error, provisional = [], None, None, None
    while True:
        remaining = args.budget_seconds - (time.monotonic() - started)
        if remaining <= 0:
            error = "budget_exhausted; uncompleted tail is not claimed"
            break
        try:
            record = messages.get(timeout=min(5.0, remaining))
        except queue.Empty:
            if not process.is_alive():
                error = "worker_ended_without_terminal_record"
                break
            continue
        if record["kind"] == "worker_complete":
            terminal = record
            break
        if record["kind"] == "worker_error":
            error = record
            emit(record)
            break
        if record["kind"] == "r8_provisional_zero":
            provisional = record["p"]
        elif record["kind"] == "r8_balanced_prime":
            rows.append(record)
        emit(record)
    if process.is_alive() and terminal is None:
        process.terminate()
    process.join(timeout=5.0)
    if process.is_alive():
        process.kill()
        process.join(timeout=5.0)
        error = "worker_did_not_exit_after_terminal_or_termination"
    completed = [row["p"] for row in rows]
    prefix_matches = completed == requested[:len(completed)]
    zero_rows = [row for row in rows if row["is_zero"]]
    checked = [row["p"] for row in rows if row["independent_checks"] is not None]
    status = "incomplete_or_failed"
    successful = False
    if error is None and process.exitcode == 0 and terminal is not None and prefix_matches:
        if terminal["status"] == "complete_nonzero_window":
            successful = completed == requested and not zero_rows and check_primes.issubset(checked)
            if successful:
                status = "complete_nonzero_window"
        elif terminal["status"] == "first_zero_verified":
            successful = (len(zero_rows) == 1 and zero_rows[0] is rows[-1]
                          and zero_rows[0]["independent_checks"] is not None
                          and terminal["p"] == rows[-1]["p"])
            if successful:
                status = "first_zero_verified"
    if not successful and error is None:
        error = "terminal_contract_or_completed_prefix_check_failed"
    summary = {
        "kind": "r8_balanced_window_summary", "status": status,
        "successful_contract_termination": successful,
        "complete_requested_window": completed == requested,
        "contract_sha256": digest(contract), "requested_primes_sha256": digest(requested),
        "requested_new_primes": requested, "completed_new_primes": completed,
        "uncompleted_new_primes": requested[len(completed):] if prefix_matches else requested,
        "completed_prefix_order_verified": prefix_matches,
        "independently_checked_primes": checked,
        "first_zero_verified": zero_rows[0]["p"] if status == "first_zero_verified" else None,
        "first_zero_seen": provisional,
        "unverified_zero": provisional if status != "first_zero_verified" else None,
        "rows_sha256": digest(rows), "completed_row_count": len(rows),
        "error": error,
        "scope": "finite new r=8 coefficients; original complete-trace criterion is R988; no selected Q-prime claim",
        "all_prime_nonvanishing_proved": False, "serre_uniformity_proved": False,
    }
    emit(summary)
    payload = {"contract": contract, "rows": rows, "summary": summary}
    data = encoded(payload) + b"\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
    emit({"kind": "r8_output_receipt", "bytes": len(data),
          "sha256": hashlib.sha256(data).hexdigest(),
          "written_to_scratch": bool(args.output)})
    emit({"kind": "r8_elapsed", "elapsed_seconds": time.monotonic() - started})
    return 0 if successful else 1


if __name__ == "__main__":
    sys.exit(main())
