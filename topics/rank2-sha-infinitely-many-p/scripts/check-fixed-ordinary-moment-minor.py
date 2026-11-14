#!/usr/bin/env python3
"""Exact fixed ordinary input for R193, without a central-derivative input.

The original A2/B coefficients are obtained from the integer Hurwitz flow
and independently from the rational s-series and the true w(s) reversion.
Only the two fixed weights 12 and 24 are used in the infinite-range theorem.
"""

import importlib.util
import json
from math import factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


def load_integer_flow():
    path = Path(__file__).with_name("check-theta-hurwitz-integers.py")
    spec = importlib.util.spec_from_file_location("integer_flow", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polynomials(s):
    h1 = 1 + 4*s + 70*s**2 + 4*s**3 + s**4
    h2 = 1 + 20*s - 26*s**2 + 20*s**3 + s**4
    q8 = (1 + 364*s**2 - 1088*s**3 + 1190*s**4
          - 1088*s**5 + 364*s**6 + s**8)
    common = s*(1 - 2*s + 5*s**2)*(5 - 2*s + s**2)/5
    return (common*(1-s)**2*(1+s)*h1*h2,
            common*(1-s)*(1+s)**2*q8)


def valuation(value, prime):
    assert value
    numerator, denominator = int(value.numerator), int(value.denominator)
    answer = 0
    while numerator % prime == 0:
        numerator //= prime
        answer += 1
    while denominator % prime == 0:
        denominator //= prime
        answer -= 1
    return answer


def residue(value, modulus):
    return (int(value.numerator)
            * pow(int(value.denominator), -1, modulus)) % modulus


def main():
    flow = load_integer_flow()
    sigma, theta = flow.universal_sigma_theta(24)
    ctx.cap = 7
    w = Series([0, 1], prec=7)
    th = Series([fmpq(theta[4*j], factorial(4*j))
                 for j in range(7)], prec=7)
    su = Series([fmpq(sigma[4*j+1], factorial(4*j+1))
                 for j in range(6)], prec=7)
    original_s = w*(su/th)**4
    polynomial, other = polynomials(original_s)
    first, second = th**68*polynomial, th**68*other

    # Independent rational s-series, including the actual change to w.
    s = Series([0, 1], prec=7)
    hypergeometric, coefficient = [], fmpq(1)
    for j in range(7):
        if j:
            coefficient *= fmpq(2*j-1, 2*j)
        hypergeometric.append(coefficient/(4*j+1))
    w_of_s = s*Series(hypergeometric, prec=7)**4
    inverse = w_of_s.reversion()
    logarithm, derivative_coefficient = [fmpq(0)], fmpq(17, 3)
    for j in range(1, 7):
        logarithm.append(derivative_coefficient/j)
        derivative_coefficient *= fmpq(4*j+1, 4*j+3)
    polynomial_s, other_s = polynomials(s)
    radial = Series(logarithm, prec=7).exp()
    check_first = (radial*polynomial_s)(inverse)
    check_second = (radial*other_s)(inverse)
    assert all(first[j] == check_first[j]
               and second[j] == check_second[j] for j in range(7))
    assert first[1] == second[1] == 1 and (second-first)[2] == -22

    # A2 also agrees with the independently fixed six-factor R57 product.
    six_factor = flow.coefficients(24, 1)
    for m in range(4, 25, 4):
        assert factorial(m)*first[m//4] == 2**(m-4)*six_factor[m]

    expected = {
        12: (78409064448, 178871666688),
        24: (3828459347334561461270740992,
             1168753707306387730587451392),
    }
    rows = []
    for m in (12, 24):
        row = [factorial(m)*series[m//4] for series in (first, second)]
        assert all(value == expected[m][j] for j, value in enumerate(row))
        assert all(valuation(value, 13) == 1 for value in row)
        rows.append(row)
    determinant = rows[0][0]*rows[1][1] - rows[0][1]*rows[1][0]
    assert valuation(determinant, 13) == 3
    assert residue(determinant, 13**5) == 210912
    assert residue(determinant/13**3, 13**2) == 96
    assert residue(determinant/13**3, 13) == 5
    print(json.dumps({
        "q": 13, "weights": [12, 24],
        "original_hurwitz_rows": [list(expected[m]) for m in (12, 24)],
        "individual_valuations": [1, 1, 1, 1],
        "minor_valuation": 3, "minor_div_q3_mod_q": 5,
        "integer_flow_equals_rational_reversion": True,
        "a2_six_factor_comparison": True, "verified": True,
    }, separators=(",", ":")))


if __name__ == "__main__":
    main()
