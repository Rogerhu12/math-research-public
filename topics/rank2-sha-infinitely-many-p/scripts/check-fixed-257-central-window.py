#!/usr/bin/env python3
"""Exact fixed-prime certificate for the original A2/B central window.

Two independent constructions are compared through z-degree 512:
  (1) the rational s-series and the elliptic-logarithm reversion;
  (2) the integer Hurwitz ODE for sigma and theta, without reversion.
No p-adic L-value, unknown derivative, or vanishing hypothesis is input.
"""
import importlib.util
import json
from math import factorial, isqrt
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


PRIME = 257
CAP = 129


def polynomials(s):
    h1 = 1 + 4*s + 70*s**2 + 4*s**3 + s**4
    h2 = 1 + 20*s - 26*s**2 + 20*s**3 + s**4
    q8 = (1 + 364*s**2 - 1088*s**3 + 1190*s**4
          - 1088*s**5 + 364*s**6 + s**8)
    common = s*(1-2*s+5*s**2)*(5-2*s+s**2)/5
    return (common*(1-s)**2*(1+s)*h1*h2,
            common*(1-s)*(1+s)**2*q8)


def by_reversion():
    ctx.cap = CAP
    s = Series([0, 1], prec=CAP)
    p, q = polynomials(s)
    log_coefficients = [fmpq(0)]*CAP
    derivative = fmpq(17, 3)
    for j in range(1, CAP):
        log_coefficients[j] = derivative/j
        derivative *= fmpq(4*j+1, 4*j+3)
    logarithm = Series(log_coefficients, prec=CAP)
    hypergeometric = []
    coefficient = fmpq(1)
    for j in range(CAP):
        if j:
            coefficient *= fmpq(2*j-1, 2*j)
        hypergeometric.append(coefficient/(4*j+1))
    w = s*Series(hypergeometric, prec=CAP)**4
    s_of_w = w.reversion()
    return ((p*logarithm.exp())(s_of_w),
            (q*logarithm.exp())(s_of_w),
            (logarithm/68).exp()(s_of_w))


def by_integer_ode():
    path = Path(__file__).with_name("check-theta-hurwitz-integers.py")
    spec = importlib.util.spec_from_file_location("integer_flow", path)
    flow = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(flow)
    sigma, theta = flow.universal_sigma_theta(512)
    ctx.cap = CAP
    th = Series([fmpq(theta[4*j], factorial(4*j))
                 for j in range(CAP)], prec=CAP)
    # The missing z^513 coefficient affects only w^129 and higher in s.
    sigma_over_z = Series([fmpq(sigma[4*j+1], factorial(4*j+1))
                          for j in range(CAP-1)], prec=CAP)
    w = Series([0, 1], prec=CAP)
    s = w*(sigma_over_z/th)**4
    p, q = polynomials(s)
    return th**68*p, th**68*q, th


def valuation(value):
    if not value:
        raise ValueError("valuation of zero is not part of this certificate")
    numerator, denominator = abs(int(value.numerator)), int(value.denominator)
    answer = 0
    while numerator % PRIME == 0:
        numerator //= PRIME
        answer += 1
    while denominator % PRIME == 0:
        denominator //= PRIME
        answer -= 1
    return answer


def normalized_residue(value, precision=1):
    order = valuation(value)
    unit = value/fmpq(PRIME)**order
    modulus = PRIME**precision
    residue = (int(unit.numerator)*pow(int(unit.denominator), -1, modulus)) % modulus
    return order, residue


def frobenius_trace(parameter):
    total = 0
    for x in range(PRIME):
        value = (x**3-parameter*x) % PRIME
        if value:
            symbol = pow(value, (PRIME-1)//2, PRIME)
            total += 1 if symbol == 1 else -1
    return -total


def main():
    assert all(PRIME % d for d in range(2, isqrt(PRIME)+1))
    assert PRIME % 8 == 1
    assert pow(17, (PRIME-1)//4, PRIME) == 1
    assert pow(34, (PRIME-1)//2, PRIME) == 1
    assert [frobenius_trace(d) for d in (1, 17, 1156)] == [2, 2, 2]
    first = by_reversion()
    second = by_integer_ode()
    for f, g in zip(first, second):
        assert all(f[j] == g[j] for j in range(CAP))
    a, b, theta = first
    assert a[1] == b[1] == 1 and b[2]-a[2] == -22
    records, rows = [], []
    expected = {256: [(1, 179), (1, 188), (0, 1)],
                512: [(1, 202), (1, 238), (0, 2)]}
    for weight in (256, 512):
        values = [factorial(weight)*f[weight//4] for f in first]
        assert all(value.denominator == 1 for value in values)
        assert [normalized_residue(value) for value in values] == expected[weight]
        rows.append(values)
        records.append({"weight": weight,
                        "orders_and_unit_residues": expected[weight]})
    determinant = rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0]
    assert normalized_residue(determinant) == (3, 224)
    assert normalized_residue(determinant, 3) == (3, 13356000)
    normalized = determinant/(2*PRIME**2*rows[0][2]*rows[1][2])
    assert normalized_residue(normalized) == (1, 56)
    print(json.dumps({"q": PRIME, "frobenius_traces": [2, 2, 2],
                      "compared_coefficients_through_z_degree": 512,
                      "two_independent_exact_constructions": True,
                      "rows": records,
                      "original_minor_order": 3,
                      "original_minor_unit_mod_q": 224,
                      "normalized_divided_difference_unit_mod_q": 56,
                      "verified": True}, separators=(",", ":")))


if __name__ == "__main__":
    main()
