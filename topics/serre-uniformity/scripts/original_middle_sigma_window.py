#!/usr/bin/env python3
"""New original middle sigma coefficients for the already evaluated trace primes.

This computes only the previously unregistered middle coefficients in the
original flat z coordinate. It does not rerun a supersingular trace, the
registered top coefficients f_N/g_N, or either completed Legendre window.
All arithmetic must run in this public repository's GitHub Actions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path


B34 = (6257370208079794820150643464381912640000000000000
       * 1350702136960)


def convolution(a, b, degree, p):
    return [sum(a[j] * b[n-j] for j in range(n+1)
                if j < len(a) and n-j < len(b)) % p
            for n in range(degree+1)]


def original_series(p, degree):
    """X=z^2*x, E=(sigma/z)^6, Y=z^3*y, f=XE, g=-Yf."""
    assert 2 <= degree < (p-5)//6
    x = [1, pow(7, -1, p)]
    for n in range(2, degree+1):
        denominator = (n-1)*(6*n+1) % p
        assert denominator
        x.append(sum(x[j]*x[n-j] for j in range(1, n))
                 * pow(denominator, -1, p) % p)
    logarithm = [0]
    for n in range(1, degree+1):
        denominator = n*(6*n-1) % p
        assert denominator
        logarithm.append(-x[n]*pow(denominator, -1, p) % p)
    e = [1]
    for n in range(1, degree+1):
        e.append(sum(j*logarithm[j]*e[n-j] for j in range(1, n+1))
                 * pow(n, -1, p) % p)
    y = [(3*n-1)*x[n] % p for n in range(degree+1)]
    y_square = convolution(y, y, degree, p)
    x_cube = convolution(convolution(x, x, degree, p), x, degree, p)
    x_cube[1] = (x_cube[1]-1) % p
    assert y_square == x_cube, "independent original curve energy identity"
    f = convolution(x, e, degree, p)
    g = [(-a) % p for a in convolution(y, f, degree, p)]
    assert f[0] == g[0] == 1
    assert f[1] == 4*pow(35, -1, p) % p
    return {"X": x, "E": e, "Y": y, "f": f, "g": g}


def calibrated_ratio_square(p, r, sigma_product, f_reference):
    """R925/R940's exact squared q_1/q_J, without choosing a square-root sign."""
    assert f_reference
    n = (p-5)//6
    j_top = (p-r-3)//6
    assert j_top > 0 and 3*j_top < p
    b = (-1)**(n+1)*math.comb(3*n+2, 2*n+1) % p
    assert b
    factor = (math.factorial(3*j_top) % p)*pow(6, -1, p) % p
    factor = factor*pow(81*pow(b, 6, p) % p, 1-j_top, p) % p
    factor = factor*sigma_product*pow(f_reference, -1, p) % p
    return factor*factor % p


def one_prime(p):
    t = p//12
    n = (p-5)//6
    r = 8 if p % 12 == 5 else 2
    degree = t+2 if r == 8 else t
    series = original_series(p, degree)
    f, g = series["f"], series["g"]
    second = t-1 if r == 8 else t
    central = f[t]*g[second] % p
    reference = 4*pow(35, -1, p) % p if r == 8 else 1
    result = {
        "p": p, "r": r, "N": n, "new_original_z_cutoff": degree,
        "central_h": (p+r+1)//2,
        "central_indices": [t, second],
        "central_f": f[t], "central_g": g[second],
        "central_sigma_product": central,
        "central_Q_prime_over_top_squared": calibrated_ratio_square(p, r, central, reference),
        "central_Legendre_unit_reused": True,
        "central_critical_source_is_nonzero": central != 0,
        "registered_top_fN_gN_regenerated": False,
        "whole_trace_recomputed": False,
        "Legendre_window_recomputed": False,
        "energy_identity_verified": True,
        "coefficient_sha256": hashlib.sha256(
            json.dumps(series, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
    }
    if r == 8:
        product34 = f[t+2]*g[t-3] % p
        f5 = -270862728*pow(5123589312701234375, -1, p) % p
        outside_bad_integer = B34 % p != 0
        result["weight34"] = {
            "h": (p+33)//2, "indices": [t+2, t-3],
            "f": f[t+2], "g": g[t-3], "sigma_product": product34,
            "outside_R937_bad_integer": outside_bad_integer,
            "Q_prime_over_top_squared": (
                calibrated_ratio_square(p, 32, product34, f5)
                if outside_bad_integer and f5 else None),
            "Legendre_factor_not_replaced_by_central_factor": True,
        }
    if not central:
        result["zero_witness_original_series"] = series
    return result


def selected_primes(minimum, maximum):
    sieve = bytearray(b"\x01")*(maximum+1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, math.isqrt(maximum)+1):
        if sieve[q]:
            sieve[q*q:maximum+1:q] = b"\x00"*((maximum-q*q)//q+1)
    return [p for p in range(minimum, maximum+1)
            if sieve[p] and p % 6 == 5 and p % 9 in (2, 5)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--minimum", type=int, default=109)
    parser.add_argument("--maximum", type=int, default=1000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise SystemExit("New arithmetic is permitted only in public repository Actions.")
    # The bounds are the exact already-certified trace window, and are covered
    # by both already-completed central Legendre windows. Widening requires a
    # new source contract, rather than silently asserting those inputs.
    assert args.minimum == 109 and args.maximum == 1000
    rows = []
    for p in selected_primes(args.minimum, args.maximum):
        row = one_prime(p)
        rows.append(row)
        print(json.dumps({"new_middle_sigma": {
            k: v for k, v in row.items() if k != "zero_witness_original_series"
        }}, sort_keys=True), flush=True)
    assert len(rows) == 48 and rows[-1]["p"] == 983
    result = {
        "schema": "original-middle-sigma-and-known-trace-window-v1",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "requested_interval": [args.minimum, args.maximum],
        "prime_count": len(rows), "last_prime": rows[-1]["p"],
        "curve": "y^2=x^3-1; dz=dx/(2y); y~ -z^-3",
        "sigma": "(log sigma)''=-x; sigma=z+O(z^7); c=0",
        "central_Legendre_sources": {
            "p5": {"result": "R934", "run": 44711592515,
                   "bound": 100000, "only_zero": 41},
            "p11": {"run": 44718206366, "bound": 10000,
                    "output_sha256": "f4e7416026c5cf358f6b473185cabf1d105998e8db2e79f2c457cecb7996400a",
                    "zero_primes": []},
        },
        "known_original_trace": {
            "run": 44716895805, "source_commit": "7843407c2633ffd5f9041a137bd9fe7174021b65",
            "output_sha256": "900524ddf9b53e831ec32e9a64a2bc9c394a22a738574877ce6b872d5209d2ab",
            "all_48_complete_sums_nonzero": True,
        },
        "central_sigma_zero_primes": [r["p"] for r in rows if not r["central_sigma_product"]],
        "weight34_sigma_zero_primes": [r["p"] for r in rows
            if "weight34" in r and not r["weight34"]["sigma_product"]],
        "central_trace_nonzero_but_Q_prime_zero_primes": [r["p"] for r in rows
            if not r["central_sigma_product"]],
        "trace_Q_prime_equality_claimed": False,
        "all_prime_nonvanishing_claimed": False,
        "rows": rows,
    }
    payload = (json.dumps(result, sort_keys=True, indent=2)+"\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(json.dumps({
        "prime_count": len(rows),
        "central_sigma_zero_primes": result["central_sigma_zero_primes"],
        "weight34_sigma_zero_primes": result["weight34_sigma_zero_primes"],
        "central_trace_nonzero_but_Q_prime_zero_primes": result["central_trace_nonzero_but_Q_prime_zero_primes"],
        "output_bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest(),
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
