#!/usr/bin/env python3
"""Exact fixed f_5 in the original E0 sigma normalization; public Actions only.

E0: y^2=x^3-1, x'=2y, (log sigma)''=-x, sigma=z+O(z^7).
With t=z^6, write x=z^-2 X(t) and sigma^6=z^6 E(t).
No prime window is run. The already known mod-41 case is not recomputed.
"""

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
import os
from pathlib import Path


def mul(a, b, degree):
    return [sum((a[j] * b[n-j] for j in range(n+1)), F(0))
            for n in range(degree+1)]


def small_factorization(value, limit=100000):
    remaining = abs(value)
    if remaining == 0:
        return {"factors": [], "unfactored_cofactor": "0",
                "complete": False, "undefined_for_zero": True,
                "trial_limit": limit}
    factors = []
    divisor = 2
    while divisor <= limit and divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors.append([divisor, exponent])
        divisor = 3 if divisor == 2 else divisor + 2
    complete = remaining == 1 or divisor * divisor > remaining
    if remaining > 1 and complete:
        factors.append([remaining, 1])
        remaining = 1
    return {"factors": factors, "unfactored_cofactor": str(remaining),
            "complete": complete, "trial_limit": limit}


def exact_top():
    degree = 5
    # x''=6x^2 and the original g3=4 energy constant determine X.
    x = [F(1), F(1, 7)]
    for n in range(2, degree+1):
        x.append(sum((x[j] * x[n-j] for j in range(1, n)), F(0))
                 / ((n-1) * (6*n+1)))
    # log E = -sum_{n>=1} x_n t^n/[n(6n-1)].
    exponent = [F(0)] + [-x[n] / (n*(6*n-1))
                         for n in range(1, degree+1)]
    sigma6 = [F(1)]
    for n in range(1, degree+1):
        sigma6.append(sum((j * exponent[j] * sigma6[n-j]
                           for j in range(1, n+1)), F(0)) / n)
    f = mul(x, sigma6, degree)

    # Independent energy equation (x'/2)^2=x^3-1, coefficientwise.
    y = [(3*n-1) * x[n] for n in range(degree+1)]
    yy = mul(y, y, degree)
    xxx = mul(mul(x, x, degree), x, degree)
    xxx[1] -= 1
    assert yy == xxx
    assert f[0] == 1 and f[1] == F(4, 35)
    assert f[2] == F(-381, 175175)
    top = f[5]
    a35 = F(factorial(34), 2**17) * top
    c35 = 3 * F(factorial(34), 2**34) * top**2
    assert F(factorial(34), 3) * c35 == a35**2
    return {
        "schema": "original-weight34-sigma-top-v1",
        "curve": "y^2=x^3-1",
        "differential": "dz=dx/(2y)",
        "sigma_normalization": "sigma=z+O(z^7); (log sigma)''=-x; c=0",
        "f_definition": "x*sigma^6=z^4*sum(f_i*z^(6*i))",
        "target_index": 5,
        "f5": str(top),
        "f5_nonzero": bool(top),
        "f5_numerator": str(top.numerator),
        "f5_denominator": str(top.denominator),
        "numerator_factorization": small_factorization(top.numerator),
        "denominator_factorization": small_factorization(top.denominator),
        "A35": str(a35),
        "C35": str(c35),
        "energy_identity_through_t5": True,
        "known_f0_f1_f2_normalization_check": True,
        "R697_square_identity": True,
        "new_prime_window_run": False,
        "all_prime_unit_claimed": False,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("/tmp/weight34-sigma-top.json"))
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY")
            != "Rogerhu12/math-research-public"):
        raise SystemExit("New arithmetic is permitted only in public repository Actions.")
    report = exact_top()
    encoded = (json.dumps(report, sort_keys=True, indent=2) + "\n").encode()
    args.output.write_bytes(encoded)
    print(json.dumps(report, sort_keys=True))
    print("OUTPUT_SHA256=" + sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
