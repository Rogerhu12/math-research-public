#!/usr/bin/env python3
"""R993: combined explicit difference sets, with original-source zero checks.

Execute mathematics only in Rogerhu12/math-research-public public Actions.
The frozen R989 consumer is not modified and its window is not reopened.
Every new mathematical function has an explicit row r; old helpers are
imported only after a hash check and are not monkey-patched.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import queue
import sys
import time
import traceback


TOPIC = Path(__file__).resolve().parents[1]
METHOD_SOURCE = "notes/R993-original-combined-disjoint-window-method.md"
MAXIMUM = 200000
LOWER = {8: 20000, 2: 100000}
MAXIMUM_BUDGET = 620.0
FINALIZATION_RESERVE = 15.0
MAXIMUM_EVENT_BYTES = 12000
EVENT_FRAGMENT_CHARACTERS = 4000
FROZEN_SCRIPT = "scripts/original_r8_balanced_new_window.py"
PINS = {
    FROZEN_SCRIPT: "96b3bbf3ec77c3c75a3870adebd9f348e7849f52b17dcda245f56229682f7160",
    "notes/R989-original-r8-sparse-heat-and-Kronecker-window-method.md": "430459e1a80765b48efe83b1255a4f0a0bfbc7998dad5e8c3e039d2a8a76c4c0",
    "results/R990-original-hypergeometric-fixed-r-coefficient.md": "5c35e72804eee83dde2c74af68232dea3a57c5d97ba39026a07329a7db25a7a1",
    "results/R975-original-balanced-Kronecker-integral-heat-recurrence.md": "56ab77273393f6db838daea1a3973e1d9da69525eb120e665dccea88f64de101",
    "results/R988-original-pure-balanced-Cartier-contraction-and-high-trace.md": "db82c7e799a7e54b7d91da329e4e6c113add5a98a519aab82df2a2e70de470a7",
    "notes/R973-original-balanced-Kronecker-four-prime-execution-method.md": "32d4c836cacbb0467c668a4a968be62fe759cd188a3365bdfb9da9583d076269",
    "results/R963-original-r2-moment-window-through-100000.md": "8259c94ba3474395d47debe638bf776c696821df848e310c647d9027c561c826",
    "results/R991-certified-original-r8-balanced-window-through-20000.md": "1dfc30c1e246a778955c6470d7c668a83c017b6ee76055b16f548611c211d354",
}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def emit(value):
    raw = encoded(value)
    if len(raw) <= MAXIMUM_EVENT_BYTES:
        print(raw.decode("ascii"), flush=True)
        return
    # No physical log line is large. Reassembly is exact, not a summary:
    # concatenate json_fragment in chunk_index order, verify its SHA256,
    # then decode the reconstructed original JSON object.
    serialized = raw.decode("ascii")
    count = (len(serialized) + EVENT_FRAGMENT_CHARACTERS - 1) // EVENT_FRAGMENT_CHARACTERS
    event_sha256 = hashlib.sha256(raw).hexdigest()
    for index in range(count):
        fragment = serialized[index * EVENT_FRAGMENT_CHARACTERS:(index + 1) * EVENT_FRAGMENT_CHARACTERS]
        envelope = {"kind": "combined_event_chunk", "event_kind": value["kind"],
                    "event_sha256": event_sha256, "event_bytes": len(raw),
                    "chunk_index": index, "chunk_count": count, "json_fragment": fragment}
        print(json.dumps(envelope, sort_keys=True, separators=(",", ":")), flush=True)


def source_receipts():
    receipt = {}
    for relative, expected in PINS.items():
        path = TOPIC / relative
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual == expected, f"frozen source changed: {relative}")
        receipt[relative] = actual
    for relative in (METHOD_SOURCE, "scripts/" + Path(__file__).name):
        receipt[relative] = hashlib.sha256((TOPIC / relative).read_bytes()).hexdigest()
    return receipt


def load_frozen_helpers():
    path = TOPIC / FROZEN_SCRIPT
    require(hashlib.sha256(path.read_bytes()).hexdigest() == PINS[FROZEN_SCRIPT],
            "frozen R989 helper source changed")
    spec = importlib.util.spec_from_file_location("_r989_frozen_helpers", path)
    require(spec is not None and spec.loader is not None, "cannot load frozen helpers")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def requested_primes():
    """Called only after the public-Actions guard."""
    sieve = bytearray(b"\x01") * (MAXIMUM + 1)
    sieve[0:2] = b"\x00\x00"
    divisor = 2
    while divisor * divisor <= MAXIMUM:
        if sieve[divisor]:
            start = divisor * divisor
            sieve[start:MAXIMUM + 1:divisor] = b"\x00" * (((MAXIMUM - start) // divisor) + 1)
        divisor += 1
    rows = {2: [], 8: []}
    for p in range(min(LOWER.values()) + 1, MAXIMUM + 1):
        if not sieve[p] or p % 9 not in (2, 5):
            continue
        r = 8 if p % 12 == 5 else 2 if p % 12 == 11 else None
        if r is not None and p > LOWER[r]:
            rows[r].append(p)
    merged = sorted(rows[2] + rows[8])
    require(len(merged) == len(set(merged)), "row sets were not disjoint")
    require(all(len(rows[r]) >= 2 for r in (2, 8)), "missing scheduled new calibration points")
    return rows, merged


def validate_new_row(p, r):
    require(r in (2, 8), "unknown original row")
    require(LOWER[r] < p <= MAXIMUM and p % 9 in (2, 5),
            f"p={p},r={r}: outside the exact new difference set")
    require(p % 12 == (11 if r == 2 else 5), f"p={p}: row and prime residue disagree")


def hypergeometric_coefficient(p, r, inv, nmod_poly, helpers):
    validate_new_row(p, r)
    n, k = p - r, p // 12
    m, resonance = n // 3, (p + 1) // 3
    require(n % 6 == 3 and m == resonance - (r + 1) // 3,
            f"p={p}: original coefficient index changed")
    require(m == (4 * k + 3 if r == 2 else 4 * k - 1),
            f"p={p}: fixed-r hypergeometric endpoint changed")
    b = [1]
    for i in range(1, k + 1):
        value = b[-1] * (i - 1 - k) * (3 * k + 3 * i + 1)
        value = value * inv[i] * inv[3 * i + 1] % p
        require(value != 0, f"p={p}: Jacobi degree dropped")
        b.append(value)
    B = nmod_poly(b, p)
    denominator = B.mul_low(B, resonance + 1).mul_low(nmod_poly([1, p - 1], p), resonance + 1)
    H = denominator.inverse_series_trunc(resonance + 1)
    b_at_one = sum(b) % p
    require(b_at_one != 0, f"p={p}: original Jacobi cusp value vanished")
    require(int(H[resonance]) == inv[b_at_one] ** 2 % p,
            f"p={p}: first resonance identity failed")
    f_values = []
    for i in range(m + 1):
        divisor = (1 - 3 * i) % p
        require(divisor != 0, f"p={p}: first resonance was crossed")
        f_values.append(int(H[i]) * inv[divisor] % p)
    require(f_values[0] == 1, f"p={p}: period ratio constant changed")
    f = nmod_poly(f_values, p)
    logarithmic_B = B.derivative().mul_low(B.inverse_series_trunc(m), m)
    Q = nmod_poly([4] + [(12 * int(logarithmic_B[i - 1]) - 1) % p
                         for i in range(1, m + 1)], p)
    inverse_power = f.inverse_series_trunc(m + 1).pow_trunc(r, m + 1)
    target = int(Q.mul_low(inverse_power, m + 1)[m])
    original_factorial = 1
    for i in range(1, r):
        original_factorial *= i
    scale = pow((-32) % p, m, p) * original_factorial * inv[4] % p
    value = scale * target % p
    return value, {
        "channel": "R990_original_fixed_r_hypergeometric",
        "r": r, "k": k, "m": m, "first_resonance": resonance,
        "J_p_r": target, "original_scale": scale,
        "c_plus": value, "c_minus": (-value) % p,
        "first_resonance_identity_verified": True,
        "Jacobi_B_sha256": digest(b),
        "period_ratio_prefix_sha256": digest(f_values),
        "H_prefix_sha256": digest(helpers.coefficients(H, resonance + 1)),
    }


def square_increment(sequence, accumulator, left, middle, right, p, nmod_poly):
    """The proved R989 CDQ ordered-pair increment, with global exponents."""
    limit = right - left - 1
    prefix_end = min(middle, limit)
    prefix = sequence[:prefix_end]
    for j in range(min(left, prefix_end)):
        prefix[j] = 2 * prefix[j] % p
    product = nmod_poly(sequence[left:middle], p).mul_low(nmod_poly(prefix, p), limit)
    for target in range(middle, right):
        accumulator[target] = (accumulator[target] + int(product[target - 1 - left])) % p


def chazy_cdq_coefficient(p, r, inv, nmod_poly):
    validate_new_row(p, r)
    n, M = p - r, (p - r - 3) // 3
    length = M + 1
    a, v = [0] * length, [0] * length
    square, weighted_square = [0] * length, [0] * length

    def solve(left, right):
        if right - left == 1:
            index = left
            if index == 0:
                a[0] = 12
            else:
                j = index - 1
                numerator = ((9 * j * j - 9 * j - 8) * square[index]
                             - 45 * weighted_square[index]) % p
                denominator_inverse = inv[6] * inv[index] * inv[3 * index + 1] * inv[3 * index + 2] % p
                a[index] = numerator * denominator_inverse % p
            v[index] = index * a[index] % p
            return
        middle = (left + right) // 2
        solve(left, middle)
        square_increment(a, square, left, middle, right, p, nmod_poly)
        square_increment(v, weighted_square, left, middle, right, p, nmod_poly)
        solve(middle, right)

    solve(0, length)
    scalar = inv[12] if r == 2 else 420
    value = scalar * a[M] % p
    return value, {
        "channel": "R989_R993_original_Chazy_CDQ",
        "r": r, "n": n, "M": M, "a_M": a[M],
        "original_scale": scalar, "c_plus": value,
        "a_prefix_sha256": digest(a),
        "v_weighting": "v_i=i*a_i with the original global index",
    }


def original_wp_prefix(p, N, inv, nmod_poly):
    """R993M.11, followed by the full independent original ODE residual."""
    y, square = [0] * N, [0] * N

    def solve(left, right):
        if right - left == 1:
            index = left
            y[index] = inv[7] if index == 0 else square[index] * inv[index] * inv[6 * index + 7] % p
            return
        middle = (left + right) // 2
        solve(left, middle)
        square_increment(y, square, left, middle, right, p, nmod_poly)
        solve(middle, right)

    solve(0, N)
    W = nmod_poly([1] + y, p)
    W_prime = W.derivative()
    residual = (W + W_prime.left_shift(1)
                + 6 * W_prime.derivative().left_shift(2)
                - W.mul_low(W, N + 1)).truncate(N + 1)
    require(residual.is_zero(), f"p={p}: complete original wp ODE residual failed")
    require(y[0] == inv[7], f"p={p}: original wp energy normalization changed")
    return [0] + y


def original_sigma_coefficient(p, r, inv, nmod_poly, helpers):
    validate_new_row(p, r)
    n, N = p - r, (p - 5) // 6
    t = (n - 3) // 6
    require(t == (N if r == 2 else N - 1), f"p={p}: original sigma endpoint changed")
    X = original_wp_prefix(p, N, inv, nmod_poly)
    logarithm = [0] + [(-X[j] * inv[6 * j] * inv[6 * j - 1]) % p
                       for j in range(1, N + 1)]
    sigma_poly = helpers.exp_series_from_log(logarithm, N + 1, p, inv, nmod_poly)
    inverse_poly = sigma_poly.inverse_series_trunc(N + 1)
    require(sigma_poly.mul_low(inverse_poly, N + 1) == nmod_poly([1], p),
            f"p={p}: original sigma inverse identity failed")
    require(sigma_poly.derivative().truncate(N)
            == nmod_poly(logarithm, p).derivative().mul_low(sigma_poly, N),
            f"p={p}: original sigma exponential identity failed")
    sigma = helpers.coefficients(sigma_poly, N + 1)
    inverse_sigma = helpers.coefficients(inverse_poly, t + 1)
    require(sigma[1] == (-inv[210]) % p, f"p={p}: E_- sigma phase changed")
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
    require(B != 0, f"p={p}: original first-pole B vanished")
    U = nmod_poly([inverse_sigma[i] * inverse_factorial[n + 1 - 6 * i] % p
                   for i in range(t + 1)], p)
    V = nmod_poly([inverse_sigma[i] * inverse_factorial[n - 6 * i] % p
                   for i in range(t + 1)], p)
    product = U.mul_low(V, 2 * t + 1)
    value = 0
    low_terms = high_terms = 0
    for index in range(2 * t + 2):
        if index <= N:
            weight = sigma[index] * factorial[6 * index + 1] % p
            low_terms += 1
        else:
            h = 6 * index + 1 - p
            require(0 < h < p, f"p={p}: original carry factorial out of range")
            weight = B * sigma[index - N - 1] * factorial[h] % p
            high_terms += 1
        value = (value + int(product[2 * t + 1 - index]) * weight) % p
    return value, {
        "channel": "R973_R993_original_E_minus_sigma_single_carry",
        "r": r, "N": N, "t": t, "original_B": B,
        "c_minus": value, "c_plus": (-value) % p,
        "original_sigma_phase": "g2=0,g3=4; sigma=z-z^7/210+...; no Gaussian",
        "low_contracted_terms": low_terms, "single_carry_contracted_terms": high_terms,
        "wp_low_prefix_sha256": digest(X),
        "sigma_low_prefix_sha256": digest(sigma),
        "sigma_inverse_prefix_sha256": digest(inverse_sigma),
        "complete_original_wp_ODE_verified": True,
        "original_sigma_exponential_and_inverse_verified": True,
    }


def worker(messages, requested, check_primes):
    pending_prime = None
    try:
        import flint
        from flint import nmod_poly
        require(flint.__version__ == "0.9.0", "unfrozen python-flint runtime")
        helpers = load_frozen_helpers()
        for p in requested:
            pending_prime = p
            r = 8 if p % 12 == 5 else 2
            validate_new_row(p, r)
            inv = helpers.inverses(p)
            value, primary = hypergeometric_coefficient(p, r, inv, nmod_poly, helpers)
            zero = value == 0
            if zero:
                messages.put({"kind": "combined_provisional_zero", "p": p, "r": r,
                              "source_checks_completed": False})
            independent = None
            if p in check_primes or zero:
                heat_value, heat_record = chazy_cdq_coefficient(p, r, inv, nmod_poly)
                sigma_value, sigma_record = original_sigma_coefficient(p, r, inv, nmod_poly, helpers)
                if heat_value != value or (-sigma_value) % p != value:
                    messages.put({"kind": "combined_source_disagreement", "p": p, "r": r,
                                  "main_c_plus": value, "heat_c_plus": heat_value,
                                  "original_sigma_c_plus": (-sigma_value) % p})
                    raise ArithmeticError(f"p={p}: the three original sources disagree")
                independent = {"heat": heat_record, "original_sigma": sigma_record,
                               "all_three_original_sources_agree": True}
            messages.put({
                "kind": "combined_balanced_prime", "p": p, "r": r, "n": p - r,
                "prime_mod_12": p % 12, "prime_mod_9": p % 9,
                "c_plus": value, "c_minus": (-value) % p, "is_zero": zero,
                "primary": primary, "independent_checks": independent,
                "original_complete_trace_zero_by_R988": zero,
            })
            if zero:
                messages.put({"kind": "worker_complete", "status": "first_zero_verified",
                              "p": p, "r": r})
                return
        messages.put({"kind": "worker_complete", "status": "complete_nonzero_difference_sets"})
    except BaseException as exc:
        messages.put({"kind": "worker_error", "p": pending_prime,
                      "error": str(exc), "traceback": traceback.format_exc()})


def main():
    require(os.environ.get("GITHUB_ACTIONS") == "true", "mathematics requires public GitHub Actions")
    require(os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public", "wrong public repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget-seconds", type=float, default=MAXIMUM_BUDGET)
    parser.add_argument("--output")
    args = parser.parse_args()
    require(0 < args.budget_seconds <= MAXIMUM_BUDGET, "invalid budget")
    started = time.monotonic()
    finalization_reserve = min(FINALIZATION_RESERVE, args.budget_seconds / 4)
    hard_deadline = started + args.budget_seconds
    computation_deadline = hard_deadline - finalization_reserve
    receipts = source_receipts()
    row_requests, requested = requested_primes()
    check_primes = set(row_requests[2][:2] + row_requests[8][:2])
    contract = {
        "kind": "combined_balanced_disjoint_contract",
        "ranges": {"r8": {"minimum_exclusive": LOWER[8], "maximum_inclusive": MAXIMUM, "p_mod_12": 5},
                   "r2": {"minimum_exclusive": LOWER[2], "maximum_inclusive": MAXIMUM, "p_mod_12": 11}},
        "common_prime_condition": "prime p; p%9 in (2,5)",
        "requested_primes_by_r": {str(r): row_requests[r] for r in (2, 8)},
        "requested_merged_count": len(requested),
        "prime_order": "increasing sorted union of the two disjoint integer lists",
        "requested_primes_sha256": digest(requested),
        "scheduled_independent_check_primes": sorted(check_primes),
        "covered_old_ranges_excluded": {"R991_r8": "p<=20000", "R963_r2": "p<=100000"},
        "old_primes_recomputed": [],
        "first_zero_requires_original_sigma_and_CDQ": True,
        "maximum_budget_seconds": args.budget_seconds,
        "parent_finalization_reserve_seconds": finalization_reserve,
        "acceptance_requires_final_budget_receipt_and_exit_zero": True,
        "large_event_protocol": "concatenate json_fragment by zero-based chunk_index; check event_bytes and event_sha256 on ASCII bytes; JSON-decode the result",
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
        remaining = computation_deadline - time.monotonic()
        if remaining <= 0:
            error = "computation_deadline_reached; finalization time reserved; entire uncompleted tail remains unproved"
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
        if record["kind"] == "combined_provisional_zero":
            provisional = {"p": record["p"], "r": record["r"]}
        elif record["kind"] == "combined_balanced_prime":
            rows.append(record)
        emit(record)
    if process.is_alive() and terminal is None:
        process.terminate()
    process.join(timeout=min(3.0, max(0.0, hard_deadline - time.monotonic())))
    if process.is_alive():
        process.kill()
        process.join(timeout=min(2.0, max(0.0, hard_deadline - time.monotonic())))
        error = "worker_did_not_exit_after_terminal_or_termination"
    if time.monotonic() >= hard_deadline:
        error = "total_budget_exhausted_before_finalization"
    completed = [row["p"] for row in rows]
    prefix_matches = completed == requested[:len(completed)]
    zero_rows = [row for row in rows if row["is_zero"]]
    checked = [row["p"] for row in rows if row["independent_checks"] is not None]
    successful, status = False, "incomplete_or_failed"
    if error is None and process.exitcode == 0 and terminal is not None and prefix_matches:
        if terminal["status"] == "complete_nonzero_difference_sets":
            successful = completed == requested and not zero_rows and check_primes.issubset(checked)
            if successful:
                status = "complete_nonzero_difference_sets"
        elif terminal["status"] == "first_zero_verified":
            required_before_stop = {p for p in check_primes if p <= terminal["p"]}
            successful = (len(zero_rows) == 1 and zero_rows[0] is rows[-1]
                          and zero_rows[0]["independent_checks"] is not None
                          and terminal["p"] == rows[-1]["p"]
                          and terminal["r"] == rows[-1]["r"]
                          and provisional == {"p": rows[-1]["p"], "r": rows[-1]["r"]}
                          and required_before_stop.issubset(checked))
            if successful:
                status = "first_zero_verified"
    if not successful and error is None:
        error = "terminal_contract_or_completed_prefix_check_failed"
    completed_set = set(completed)
    summary = {
        "kind": "combined_balanced_disjoint_summary", "status": status,
        "successful_contract_termination": successful,
        "complete_requested_difference_sets": completed == requested,
        "contract_sha256": digest(contract), "requested_primes_sha256": digest(requested),
        "requested_merged_count": len(requested),
        "completed_primes_sha256": digest(completed),
        "completed_primes_by_r": {str(r): [p for p in row_requests[r] if p in completed_set] for r in (2, 8)},
        "uncompleted_primes_by_r": {str(r): [p for p in row_requests[r] if p not in completed_set] for r in (2, 8)},
        "completed_prefix_order_verified": prefix_matches,
        "independently_checked_primes": checked,
        "first_zero_verified": provisional if status == "first_zero_verified" else None,
        "first_zero_seen": provisional,
        "unverified_zero": provisional if status != "first_zero_verified" else None,
        "rows_sha256": digest(rows), "completed_row_count": len(rows),
        "error": error,
        "scope": "finite new original r=2/r=8 coefficients only; trace interpretation is exactly R988",
        "all_prime_nonvanishing_proved": False,
        "selected_Q_prime_unit_proved": False, "serre_uniformity_proved": False,
    }
    payload = {"contract": contract, "rows": rows, "summary": summary}
    data = encoded(payload) + b"\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(data)
    if time.monotonic() >= hard_deadline:
        successful = False
        summary["status"] = "incomplete_or_failed"
        summary["successful_contract_termination"] = False
        summary["error"] = "total_budget_exhausted_during_finalization"
        data = encoded(payload) + b"\n"
        if args.output:
            output.write_bytes(data)
    emit(summary)
    emit({"kind": "combined_output_receipt", "bytes": len(data),
          "sha256": hashlib.sha256(data).hexdigest(), "written_to_scratch": bool(args.output)})
    elapsed = time.monotonic() - started
    within_budget = elapsed <= args.budget_seconds
    emit({"kind": "combined_final_budget_receipt", "elapsed_seconds": elapsed,
          "within_total_budget": within_budget,
          "successful_contract_termination": successful and within_budget})
    return 0 if successful and within_budget else 1


if __name__ == "__main__":
    sys.exit(main())

