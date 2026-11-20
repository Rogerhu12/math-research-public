#!/usr/bin/env python3
"""Finite p==11 mod12 test of original central and allowed third-position labels.

Execute new arithmetic only in this repository's public GitHub Actions.
The fixed curve may be supersingular: no ordinary assertion is assumed.
No finite scan is a proof of uniform nonvanishing.
"""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time

from same_label_legendre_window import independent_even_value


def primes_up_to(bound):
    sieve = bytearray(b"\x01") * (bound + 1)
    sieve[:2] = b"\x00\x00"
    for n in range(2, math.isqrt(bound) + 1):
        if sieve[n]:
            sieve[n*n:bound+1:n] = b"\x00" * ((bound-n*n)//n+1)
    return (n for n in range(47, bound+1, 12) if sieve[n])


def evaluate_degrees(p, degrees):
    """P_n/x for odd n and P_n for even n, via q_n=n!P_n."""
    top = max(degrees)
    y = -pow(3, -1, p) % p
    previous, current, factorial = 1, 1, 1
    values = {}
    for n in range(2, top+1):
        following = ((2*n-1) * (y if n % 2 == 0 else 1) * current
                     - (n-1)**2 * previous) % p
        previous, current = current, following
        factorial = factorial*n % p
        if n in degrees:
            values[n] = current*pow(factorial, -1, p) % p
    return values


def one_prime(p):
    m = (p-1)//2
    h0 = (p+3)//2
    labels = [("central", h0), ("central_minus_6", h0-6),
              ("central_plus_6", h0+6)]
    if p % 9 == 5:
        labels.append(("allowed_third", (p-2)//3))
    elif p % 9 == 2:
        labels.append(("allowed_third", (2*p-1)//3))
    targets = {m}
    rows = []
    for name, h in labels:
        assert 7 <= h <= p-4 and h % 6 == 1
        raw_degree = h-1
        degree = min(raw_degree, p-1-raw_degree)
        assert degree % 2 == 0 and 0 < degree < m
        targets.add(degree)
        rows.append({"name": name, "h": h, "original_degree": raw_degree,
                     "reflected_degree": degree, "gcd_h_p_plus_1": math.gcd(h,p+1)})
    values = evaluate_degrees(p, targets)
    for row in rows:
        row["value"] = values[row["reflected_degree"]]
        row["primitive"] = row["gcd_h_p_plus_1"] == 1
        if row["name"] in ("central", "allowed_third"):
            assert row["primitive"]
    central = rows[0]["value"]
    a_scalar = values[m]
    assert central != 0 or a_scalar != 0  # Adjacent Legendre polynomials.
    return {"p": p, "admissible_for_R317": p % 9 in (2,5),
            "A_divided_by_x": a_scalar,
            "auxiliary_curve_ordinary": a_scalar != 0,
            "labels": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bound", type=int, default=100000)
    parser.add_argument("--allowed-mod9", action="store_true")
    parser.add_argument("--stop-after", type=int, default=0)
    parser.add_argument("--output", type=Path,
                        default=Path("/tmp/p11-original-legendre-window.json"))
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY")
            != "Rogerhu12/math-research-public"):
        raise SystemExit("New arithmetic is permitted only in public repository Actions.")
    assert args.bound >= 47 and args.stop_after >= 0
    started = time.monotonic()
    digest = hashlib.sha256()
    zeros = []
    tested = auxiliary_ss = third_zeros = joint_zeros = 0
    last_prime = None
    for p in primes_up_to(args.bound):
        if args.allowed_mod9 and p % 9 not in (2,5):
            continue
        row = one_prime(p)
        digest.update((json.dumps(row, sort_keys=True, separators=(",", ":"))+"\n").encode())
        tested += 1
        last_prime = p
        auxiliary_ss += not row["auxiliary_curve_ordinary"]
        central = row["labels"][0]
        third = next((z for z in row["labels"] if z["name"] == "allowed_third"), None)
        third_zero = third is not None and third["value"] == 0
        third_zeros += third_zero
        joint_zeros += central["value"] == 0 and third_zero
        if central["value"] == 0:
            independent, terms = independent_even_value(p, central["reflected_degree"])
            assert independent == 0
            row["independent_central_value"] = independent
            row["independent_terms_sha256"] = hashlib.sha256(
                json.dumps(terms, separators=(",", ":")).encode()).hexdigest()
            if len(terms) <= 150:
                row["independent_terms_before_2_minus_n"] = terms
            zeros.append(row)
            print(json.dumps({"central_zero": row}, sort_keys=True), flush=True)
            if args.stop_after and len(zeros) >= args.stop_after:
                break
        if tested % 500 == 0:
            print(json.dumps({"tested": tested, "last_prime": p,
                              "elapsed_seconds": time.monotonic()-started}), flush=True)
    report = {"status": "finite-window-only", "prime_class": "p >= 47, p == 11 (mod 12)",
              "allowed_mod9_only": args.allowed_mod9, "requested_bound": args.bound,
              "last_prime": last_prime, "tested": tested, "stop_after": args.stop_after,
              "auxiliary_supersingular_count": auxiliary_ss,
              "allowed_third_zero_count": third_zeros,
              "central_and_allowed_third_zero_count": joint_zeros,
              "central_zeros": zeros, "all_rows_sha256": digest.hexdigest(),
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "finite_sum_source_sha256": hashlib.sha256(
                  Path(__file__).with_name("same_label_legendre_window.py").read_bytes()).hexdigest()}
    encoded = (json.dumps(report, sort_keys=True, indent=2)+"\n").encode()
    args.output.write_bytes(encoded)
    print(json.dumps({"report": report, "output_sha256": hashlib.sha256(encoded).hexdigest()},
                     sort_keys=True), flush=True)
    print(json.dumps({"elapsed_seconds": time.monotonic()-started}), flush=True)


if __name__ == "__main__":
    main()
