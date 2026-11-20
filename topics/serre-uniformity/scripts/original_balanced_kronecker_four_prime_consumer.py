#!/usr/bin/env python3
"""A new balanced Kronecker coefficient, at four fixed original primes.

Execute mathematical code only in this public repository's GitHub Actions.
Local use is restricted to reading, AST parsing, and hashing this source.
The canonical curve is y^2=x^3-1, omega=dx/(2y), with no Gaussian shift.
No supersingular trace, old same-label sigma array, or old window is rerun.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
import multiprocessing
import os
from pathlib import Path
import queue
import sys
import time
import traceback


PRIMES = (41, 47, 227, 857)
MAX_BUDGET_SECONDS = 620.0


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def rational_pair(value):
    return [str(value.numer()), str(value.denom())]


def mod_rational(value, p):
    numerator, denominator = int(value.numer()), int(value.denom())
    require(denominator % p != 0, f"p={p}: nonintegral rational reduction")
    return numerator % p * pow(denominator % p, -1, p) % p


def rational_valuation(value, p):
    numerator, denominator = int(value.numer()), int(value.denom())
    if numerator == 0:
        return None
    exponent = 0
    while numerator % p == 0:
        numerator //= p
        exponent += 1
    while denominator % p == 0:
        denominator //= p
        exponent -= 1
    return exponent


def canonical_sigma(maximum, fmpq):
    """Exact rational sigma=z*sum s_j z^(6j), independently inverted.

    x=z^-2+sum x_j z^(6j-2), x_1=1/7, x''=6*x^2.
    log(sigma/z)=sum ell_j z^(6j), ell_j=-x_j/(6j(6j-1)).
    The inverse is exp(-ell), not assigned by the desired coefficient.
    """
    zero, one = fmpq(0), fmpq(1)
    x = [zero] * (maximum + 1)
    ell = [zero] * (maximum + 1)
    sigma, inverse = [one], [one]
    if maximum:
        x[1] = fmpq(1, 7)
    for j in range(1, maximum + 1):
        if j > 1:
            x[j] = sum((x[a] * x[j - a] for a in range(1, j)), zero)
            x[j] /= (6 * j + 1) * (j - 1)
        ell[j] = -x[j] / (6 * j * (6 * j - 1))
        sigma.append(sum((a * ell[a] * sigma[j - a]
                          for a in range(1, j + 1)), zero) / j)
        inverse.append(-sum((a * ell[a] * inverse[j - a]
                             for a in range(1, j + 1)), zero) / j)
    require(sigma[1] == fmpq(-1, 210), "wrong original g3=4 normalization")
    for j in range(1, maximum + 1):
        require(sum((sigma[a] * inverse[j - a] for a in range(j + 1)), zero) == 0,
                f"sigma/inverse identity failed at {j}")
    return sigma, inverse


def exact_balanced(n, sigma, inverse, fmpq):
    require(n % 6 == 3, "the actual CM degree class was changed")
    t = (n - 3) // 6
    result = fmpq(0)
    for u in range(t + 1):
        for v in range(t + 1):
            k = 2 * t + 1 - u - v
            result += inverse[u] * inverse[v] * sigma[k] * comb(6 * k + 1, n + 1 - 6 * u)
    return result


def one_prime(p, sigma, inverse, fmpq):
    require(p >= 41 and p % 6 == 5 and p % 9 in (2, 5), "prime outside original scope")
    r = 2 if p % 12 == 11 else 8
    n, N = p - r, (p - 5) // 6
    t = (n - 3) // 6
    maximum = 2 * t + 1
    # Consume R574R.3's exact original B formula, without a new trace.
    h, m = (p - 1) // 2, (p - 2) // 3
    B = ((-1) ** (h - m) * comb(h, m)) % p
    require(B != 0, "R574 original B vanished")
    low_sigma = [mod_rational(sigma[j], p) for j in range(N + 1)]
    low_inverse = [mod_rational(inverse[j], p) for j in range(t + 1)]
    for j in range(N + 1, maximum + 1):
        require(mod_rational(p * sigma[j], p) == -B * low_sigma[j - N - 1] % p,
                f"p={p}: original single-pole sigma comparison failed at {j}")

    exact = exact_balanced(n, sigma, inverse, fmpq)
    reduced = 0
    low_terms = high_terms = 0
    for u in range(t + 1):
        for v in range(t + 1):
            k = 2 * t + 1 - u - v
            top, bottom = 6 * k + 1, n + 1 - 6 * u
            coefficient = comb(top, bottom)
            require(0 < bottom < p and 0 < top - bottom < p,
                    f"p={p}: binomial digit bounds failed")
            if k <= N:
                low_terms += 1
                term = low_sigma[k] * (coefficient % p)
            else:
                high_terms += 1
                require(p <= top < 2 * p and coefficient % p == 0 and coefficient % (p * p) != 0,
                        f"p={p}: claimed single binomial carry failed")
                term = -B * low_sigma[k - N - 1] * ((coefficient // p) % p)
            reduced = (reduced + low_inverse[u] * low_inverse[v] * term) % p
    require(mod_rational(exact, p) == reduced, f"p={p}: exact and pole-residue methods disagree")
    valuation = rational_valuation(exact, p)
    return {
        "kind": "balanced_kronecker_prime",
        "p": p, "r": r, "source_cm_weight": n + 1,
        "coefficient_modular_weight": 2 * n, "n": n, "t": t,
        "coefficient": "[z^n w^(n-1)] sigma(z+w)/(sigma(z)*sigma(w))",
        "curve": "y^2=x^3-1; omega=dx/(2y); g2=0,g3=4; no Gaussian",
        "rational": rational_pair(exact),
        "rational_sha256": digest(rational_pair(exact)),
        "p_valuation": valuation, "residue_mod_p": reduced,
        "is_unit": valuation == 0,
        "original_B": B,
        "low_summands": low_terms, "single_carry_summands": high_terms,
        "sigma_last_j": maximum,
        "sigma_prefix_sha256": digest([rational_pair(x) for x in sigma[:maximum + 1]]),
        "inverse_prefix_sha256": digest([rational_pair(x) for x in inverse[:t + 1]]),
        "exact_vs_single_carry": True,
        "original_first_pole_scale": True,
        "source_normalization_check": "c_3=-1/6 exactly",
    }


def worker(messages):
    try:
        import flint
        from flint import fmpq
        require(flint.__version__ == "0.9.0", "unfrozen rational runtime")
        maximum = max(2 * ((p - (2 if p % 12 == 11 else 8) - 3) // 6) + 1 for p in PRIMES)
        sigma, inverse = canonical_sigma(maximum, fmpq)
        require(exact_balanced(3, sigma, inverse, fmpq) == fmpq(-1, 6),
                "Kronecker quotient normalization check failed")
        messages.put({"kind": "balanced_kronecker_prefix_ready", "maximum_j": maximum,
                      "source_prefix_sha256": digest([rational_pair(x) for x in sigma])})
        for p in PRIMES:
            messages.put(one_prime(p, sigma, inverse, fmpq))
        messages.put({"kind": "worker_complete"})
    except BaseException as exc:
        messages.put({"kind": "worker_error", "error": str(exc), "traceback": traceback.format_exc()})


def main():
    require(os.environ.get("GITHUB_ACTIONS") == "true", "mathematics requires public GitHub Actions")
    require(os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public", "wrong public repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget-seconds", type=float, default=MAX_BUDGET_SECONDS)
    args = parser.parse_args()
    require(0 < args.budget_seconds <= MAX_BUDGET_SECONDS, "invalid budget")
    started = time.monotonic()
    context = multiprocessing.get_context("spawn")
    messages = context.Queue()
    process = context.Process(target=worker, args=(messages,))
    process.start()
    rows, prefix, error = [], None, None
    completed = False
    while True:
        remaining = args.budget_seconds - (time.monotonic() - started)
        if remaining <= 0:
            error = "budget_exhausted; no claim about uncompleted primes"
            break
        try:
            record = messages.get(timeout=min(5.0, remaining))
        except queue.Empty:
            if not process.is_alive():
                error = "worker_ended_without_completion"
                break
            continue
        if record["kind"] == "worker_complete":
            completed = True
            break
        if record["kind"] == "worker_error":
            error = record
            print(json.dumps(record, sort_keys=True), flush=True)
            break
        if record["kind"] == "balanced_kronecker_prime":
            rows.append(record)
        elif record["kind"] == "balanced_kronecker_prefix_ready":
            prefix = record
        print(json.dumps(record, sort_keys=True), flush=True)
    if process.is_alive():
        if not completed:
            process.terminate()
        process.join(timeout=5.0)
    process.join(timeout=5.0)
    finished_primes = [row["p"] for row in rows]
    complete = completed and finished_primes == list(PRIMES) and process.exitcode == 0
    summary = {
        "kind": "balanced_kronecker_summary", "complete": complete,
        "requested_primes": list(PRIMES), "completed_primes": finished_primes,
        "uncompleted_primes": [p for p in PRIMES if p not in finished_primes],
        "rows_sha256": digest(rows), "prefix_sha256": digest(prefix),
        "unit_primes": [row["p"] for row in rows if row["is_unit"]],
        "nonunit_primes": [row["p"] for row in rows if not row["is_unit"]],
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
        "error": error,
        "scope": "four new balanced coefficients only; no all-prime unit or original-trace identity asserted",
    }
    print(json.dumps(summary, sort_keys=True), flush=True)
    return 0 if complete else 1


if __name__ == "__main__":
    sys.exit(main())
