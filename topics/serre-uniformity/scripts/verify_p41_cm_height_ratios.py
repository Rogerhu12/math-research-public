#!/usr/bin/env python3
"""Exact rational checker for R79's Hecke-field height ratios.

No number-field package is used: polynomial identities, a 54-dimensional
integer matrix, and the actual twist rows suffice. All checks are over Q.
"""

from fractions import Fraction
from functools import reduce
import hashlib
import json
from math import lcm
from pathlib import Path
import sys


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def multiply(a, b):
    out = [Fraction(0)]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return trim(out)


def divide(a, b):
    out = list(a)
    quotient = [Fraction(0)]*max(1, len(a)-len(b)+1)
    while len(out) >= len(b) and out != [0]:
        k = len(out)-len(b)
        c = out[-1]/b[-1]
        quotient[k] += c
        for j, bj in enumerate(b):
            out[j+k] -= c*bj
        trim(out)
    return trim(quotient), trim(out)


def subtract(a, b):
    out = [Fraction(0)]*max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] -= v
    return trim(out)


def evaluate_row_scaled(row, poly, integer_matrix, denominator, degree, scale):
    """Return scale*denominator**degree * row*poly(integer_matrix/denominator)."""
    assert degree >= len(poly)-1
    coefficients = [
        int(scale*c*denominator**(degree-i)) for i, c in enumerate(poly)
    ]
    assert all(Fraction(coefficients[i]) == scale*c*denominator**(degree-i)
               for i, c in enumerate(poly))
    columns = list(zip(*integer_matrix))
    out = [0]*len(row)
    for c in reversed(coefficients):
        out = [sum(a*b for a, b in zip(out, col))+c*v
               for col, v in zip(columns, row)]
    return out


def main(path):
    data = json.loads(path.read_text())
    assert (data["level"], data["weight"], data["star"], data["fricke"]) == (1681, 2, -1, 1)
    assert data["new"] and data["dimension"] == 54
    assert data["one_algebraic_square_root_no_point_sign"]
    reference = path.with_name(data["twist_reference"])
    assert hashlib.sha256(reference.read_bytes()).hexdigest() == data["twist_reference_sha256"]
    twists = json.loads(reference.read_text())
    v4, v8 = twists["twist4_exact"], twists["twist8_exact"]
    h6 = data["six_times_hecke_matrix"]
    assert len(h6) == 54 and all(len(row) == 54 for row in h6)
    denom = data["hecke_denominator"]
    assert denom == 6
    factors = [[Fraction(x) for x in reversed(item["factor_descending"])]
               for item in data["fields"]]
    assert [len(f)-1 for f in factors] == [2, 3, 3, 4, 4, 8, 12, 18]
    total = reduce(multiply, factors, [Fraction(1)])
    for item, f in zip(data["fields"], factors):
        rho = [Fraction(x, item["ratio_denominator"])
               for x in reversed(item["ratio_numerator_descending"])]
        root = [Fraction(x, item["root_denominator"])
                for x in reversed(item["root_numerator_descending"])]
        assert divide(subtract(multiply(root, root), rho), f)[1] == [0]
        cofactor, remainder = divide(total, f)
        assert remainder == [0]
        left_poly = [4*x for x in multiply(rho, cofactor)]
        right_poly = cofactor
        degree = max(len(left_poly), len(right_poly))-1
        scale = lcm(*(c.denominator for c in left_poly+right_poly))
        left = evaluate_row_scaled(v4, left_poly, h6, denom, degree, scale)
        right = evaluate_row_scaled(v8, right_poly, h6, denom, degree, scale)
        assert left == right
        print(f"Degree {len(f)-1}: root^2 = ratio; 4 v4 ratio(H) cofactor(H) = v8 cofactor(H)")
    print("All eight exact rational certificates passed; no point signs inferred.")


if __name__ == "__main__":
    default = Path(__file__).with_name("data") / "p41_cm_ratio_certificate.json"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
