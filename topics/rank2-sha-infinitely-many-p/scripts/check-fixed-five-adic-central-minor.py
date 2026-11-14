#!/usr/bin/env python3
"""Exact q=5 input for R195; no unknown Mellin derivative is supplied."""

import importlib.util
import json
from math import factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series


def load_flow():
    path = Path(__file__).with_name("check-theta-hurwitz-integers.py")
    spec = importlib.util.spec_from_file_location("integer_flow", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polys(s):
    h1 = 1 + 4*s + 70*s**2 + 4*s**3 + s**4
    h2 = 1 + 20*s - 26*s**2 + 20*s**3 + s**4
    q8 = (1 + 364*s**2 - 1088*s**3 + 1190*s**4
          - 1088*s**5 + 364*s**6 + s**8)
    common = s*(1 - 2*s + 5*s**2)*(5 - 2*s + s**2)/5
    return (common*(1-s)**2*(1+s)*h1*h2,
            common*(1-s)*(1+s)**2*q8)


def val(n, q):
    assert n
    n = int(n)
    result = 0
    while n % q == 0:
        n //= q
        result += 1
    return result


def trace_at_five(coefficient):
    count = 1
    for x in range(5):
        rhs = (x**3 + coefficient*x) % 5
        count += sum(y*y % 5 == rhs for y in range(5))
    return 6 - count


def main():
    flow = load_flow()
    sigma, theta = flow.universal_sigma_theta(8)
    ctx.cap = 3
    w = Series([0, 1], prec=3)
    th = Series([fmpq(theta[4*j], factorial(4*j))
                 for j in range(3)], prec=3)
    su = Series([fmpq(sigma[4*j+1], factorial(4*j+1))
                 for j in range(2)], prec=3)
    s_actual = w*(su/th)**4
    p_actual, q_actual = polys(s_actual)
    first, second = th**68*p_actual, th**68*q_actual

    # Independent rational s-series and true elliptic-logarithm reversion.
    s = Series([0, 1], prec=3)
    logarithm = Series([0, fmpq(17, 3), fmpq(85, 42)], prec=3)
    z_over_u = Series([1, fmpq(1, 10), fmpq(1, 24)], prec=3)
    inverse = (s*z_over_u**4).reversion()
    p_s, q_s = polys(s)
    alternative = ((logarithm.exp()*p_s)(inverse),
                   (logarithm.exp()*q_s)(inverse))
    for j in range(3):
        assert first[j] == alternative[0][j]
        assert second[j] == alternative[1][j]
    assert first[1] == second[1] == 1
    assert (second-first)[2] == -22

    product = flow.coefficients(8, 1)
    for m in (4, 8):
        assert factorial(m)*first[m//4] == 2**(m-4)*product[m]

    expected = {4: (24, 24), 8: (1042944, 155904)}
    rows = []
    for m in (4, 8):
        raw = [factorial(m)*series[m//4] for series in (first, second)]
        assert all(value.denominator == 1 for value in raw)
        row = list(map(int, raw))
        assert row == list(expected[m])
        assert all(val(value, 5) == 0 for value in row)
        assert all(val(5*value, 5) == 1 for value in row)
        rows.append(row)
    determinant = rows[0][0]*rows[1][1] - rows[0][1]*rows[1][0]
    assert determinant == -21288960
    assert val(determinant, 5) == 1
    assert (determinant//5) % 5 == 3
    assert val(25*determinant, 5) == 3
    traces = [trace_at_five(a) for a in (-1, -17, -1156)]
    assert traces == [-2, -4, -2]
    print(json.dumps({
        "q": 5,
        "original_hurwitz_rows": rows,
        "raw_determinant": determinant,
        "raw_minor_valuation": 1,
        "scaled_individual_valuations": [1, 1, 1, 1],
        "scaled_minor_valuation": 3,
        "raw_minor_div_q_mod_q": 3,
        "traces_E0_E17_E34": traces,
        "integer_flow_equals_rational_reversion": True,
        "a2_six_factor_comparison": True,
        "verified": True,
    }, separators=(",", ":")))


if __name__ == "__main__":
    main()
