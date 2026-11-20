#!/usr/bin/env python3
"""New R929 shifted-Legendre window; execute only in public repository Actions.

This does not recompute R929's theorem.  It tests the still-open same-label
factor for p == 5 (mod 12), using q_n = n! P_n(x), x^2 = -1/3.  No claim of
uniform nonvanishing follows from a finite scan.  Output is ephemeral; retain
only script, arguments, run ID and SHA-256 in the repository.
"""

import argparse
import hashlib
import json
import math
import time


def primes_up_to(bound):
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for n in range(2, math.isqrt(bound) + 1):
        if sieve[n]:
            sieve[n * n : bound + 1 : n] = b"\x00" * ((bound - n * n) // n + 1)
    return (n for n in range(41, bound + 1, 12) if sieve[n])


def factorial_legendre(p):
    """Return q_(m-4), q_(m-1)/x, q_m and m! in F_p; m=(p-1)/2."""
    m = (p - 1) // 2
    y = -pow(3, -1, p) % p
    previous, current = 1, 1  # q_0=1 and q_1=x, with x removed in odd degree
    factorial = 1
    target = None
    for n in range(2, m + 1):
        x_multiplier = y if n % 2 == 0 else 1
        following = ((2 * n - 1) * x_multiplier * current - (n - 1) ** 2 * previous) % p
        previous, current = current, following
        factorial = factorial * n % p
        if n == m - 4:
            target = current
    return target, previous, current, factorial


def independent_even_value(p, n):
    """Evaluate P_n(x) by its finite coefficient formula (n is even)."""
    assert n % 2 == 0 and 0 <= 2 * n < p
    factorials = [1] * (2 * n + 1)
    for k in range(1, 2 * n + 1):
        factorials[k] = factorials[k - 1] * k % p
    inverse_factorials = [1] * (2 * n + 1)
    inverse_factorials[-1] = pow(factorials[-1], -1, p)
    for k in range(2 * n, 0, -1):
        inverse_factorials[k - 1] = inverse_factorials[k] * k % p
    y = -pow(3, -1, p) % p
    value = 0
    terms = []
    for k in range(n // 2 + 1):
        coefficient = factorials[2 * n - 2 * k]
        coefficient = coefficient * inverse_factorials[k] % p
        coefficient = coefficient * inverse_factorials[n - k] % p
        coefficient = coefficient * inverse_factorials[n - 2 * k] % p
        if k % 2:
            coefficient = -coefficient % p
        term = coefficient * pow(y, n // 2 - k, p) % p
        terms.append(term)
        value = (value + term) % p
    value = value * pow(pow(2, n, p), -1, p) % p
    return value, terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bound", type=int, default=200000)
    parser.add_argument("--stop-after", type=int, default=1)
    parser.add_argument("--allowed-mod9", action="store_true",
                        help="Restrict to the original R317/R925 prime classes p == 2 or 5 (mod 9).")
    parser.add_argument("--output", default="legendre-shift-window.json")
    args = parser.parse_args()
    start = time.monotonic()
    tested = 0
    zeros = []
    last_prime = None
    digest = hashlib.sha256()
    for p in primes_up_to(args.bound):
        if args.allowed_mod9 and p % 9 not in (2, 5):
            continue
        target, q_previous, q_m, factorial = factorial_legendre(p)
        m = (p - 1) // 2
        inv_factorial = pow(factorial, -1, p)
        A = q_m * inv_factorial % p
        C_scalar = m * q_previous * inv_factorial % p
        x_A_prime = (C_scalar - A) * pow(8, -1, p) % p
        shifted = (169 * A + 896 * x_A_prime) * pow(105, -1, p) % p
        target_factorial = factorial
        for k in range(m, m - 4, -1):
            target_factorial = target_factorial * pow(k, -1, p) % p
        direct = target * pow(target_factorial, -1, p) % p
        assert direct == shifted
        assert A != 0, "Contradicts the existing R929 theorem; inspect normalization."
        tested += 1
        last_prime = p
        digest.update(f"{p},{A},{x_A_prime},{direct}\n".encode())
        if direct == 0:
            independent, terms = independent_even_value(p, m - 4)
            assert independent == 0
            item = {"p": p, "h": (p + 9) // 2, "m": m, "n": m - 4,
                    "admissible_for_R317": p % 9 in (2, 5),
                    "A": A, "x_A_prime": x_A_prime, "C_scalar": C_scalar,
                    "shifted": direct, "q_m": q_m, "q_m_minus_1_scalar": q_previous,
                    "independent_coefficient_sum": independent,
                    "independent_terms_sha256": hashlib.sha256(json.dumps(terms, separators=(",", ":")).encode()).hexdigest()}
            # A short exact coefficient transcript is useful if the first zero is small.
            if len(terms) <= 150:
                item["independent_terms_before_2_minus_n"] = terms
            zeros.append(item)
            print(json.dumps({"zero": item}, sort_keys=True), flush=True)
            if args.stop_after and len(zeros) >= args.stop_after:
                break
        if tested % 500 == 0:
            print(json.dumps({"tested": tested, "last_prime": p, "elapsed_seconds": time.monotonic() - start}), flush=True)
    report = {"status": "finite-window-only", "prime_class": "p >= 41, p == 5 (mod 12)",
              "allowed_mod9_only": args.allowed_mod9,
              "requested_bound": args.bound, "last_prime": last_prime, "tested": tested,
              "stop_after": args.stop_after, "zeros": zeros,
              "all_rows_sha256": digest.hexdigest()}
    encoded = (json.dumps(report, indent=2, sort_keys=True) + "\n").encode()
    with open(args.output, "wb") as handle:
        handle.write(encoded)
    print(json.dumps({"report": report, "output_sha256": hashlib.sha256(encoded).hexdigest()}, sort_keys=True), flush=True)
    print(json.dumps({"elapsed_seconds": time.monotonic() - start}), flush=True)


if __name__ == "__main__":
    main()
