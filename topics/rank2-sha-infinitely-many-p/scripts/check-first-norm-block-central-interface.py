#!/usr/bin/env python3
"""Exact calibration of R186 on the original rational A2/B theta graph.

No source relation or central vanishing is assumed. The checks compare the
negative-power formula, the true axis, and the integral p^3 reconstruction.
"""
import importlib.util
import json
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series

spec = importlib.util.spec_from_file_location(
    "actual_plane", Path(__file__).with_name("check-theta-plane-saturated-jets.py"))
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


def truncate(series, degree):
    return Series([series[j] for j in range(degree + 1)], prec=degree + 1)


def divide_by_variable(series, degree):
    assert series[0] == 0
    return Series([series[j + 1] for j in range(degree + 1)], prec=degree + 1)


def modp(value, prime):
    return (int(value.numerator) % prime
            * pow(int(value.denominator) % prime, -1, prime)) % prime


def check(prime):
    r = (prime + 1) // 4
    n = 3 * r - 1
    degree = 1
    while (degree + 1) * (degree + 2) // 2 + 8 < 2 * prime + 4:
        degree += 1
    columns, rows = plane.actual_rows(degree)
    cap = ctx.cap
    variable = Series([0, 1], prec=cap)
    original_a = Series(
        [row[columns.index((1, 0))] for row in rows], prec=cap)
    original_d = Series(
        [row[columns.index((1, 1))] for row in rows], prec=cap)
    a_unit = divide_by_variable(original_a, cap - 2)
    d_unit = Series([original_d[j + 2] for j in range(cap - 2)],
                    prec=cap - 2)
    graph = (d_unit / a_unit**2)(original_a.reversion())
    ratio = original_d / original_a
    inverse_ratio = ratio.reversion()
    h = original_a(inverse_ratio)
    h_unit = divide_by_variable(h, cap - 3)

    negative_power = -(1 / h_unit)**prime
    coefficients = []
    for j in range(prime):
        value = -fmpq(prime, prime - j) * (graph**(prime - j))[j]
        assert value == negative_power[j], (prime, j, "negative-power")
        assert plane.vp(value, prime) >= 0, (prime, j, "integrality")
        coefficients.append(value)
    cp = Series(coefficients, prec=prime)
    recovered_log = -(cp / (22**prime)).log() / prime
    actual_log = (-22 * h_unit).log()
    assert all(recovered_log[j] == actual_log[j] for j in range(prime))

    # The original elliptic logarithm: w(s)=s*L(s)^4.
    hypergeometric = []
    central_binomial = fmpq(1)
    for j in range(cap):
        if j:
            central_binomial *= fmpq(2*j - 1, 2*j)
        hypergeometric.append(central_binomial / (4*j + 1))
    w = variable * Series(hypergeometric, prec=cap)**4
    s_of_w = w.reversion()
    t = [fmpq(0)]
    derivative_coefficient = fmpq(1, 3)
    for j in range(1, cap):
        t.append(derivative_coefficient / j)
        derivative_coefficient *= fmpq(4*j + 1, 4*j + 3)
    theta = Series(t, prec=cap).exp()
    sigma = variable * theta
    u0 = ((theta - sigma/3)(s_of_w))[r]
    b = 17 * u0
    assert plane.vp(b, prime) == -1

    gauge_exponent = [fmpq(0)] * cap
    gauge_exponent[r] = -b
    gauge = Series(gauge_exponent, prec=cap).exp()
    axis_a = (original_a(s_of_w) * gauge)
    axis_b = ((original_a + original_d)(s_of_w) * gauge)
    f_unit = divide_by_variable(axis_a, n)
    g_unit = divide_by_variable(axis_b, n)
    assert all(plane.vp(f_unit[j], prime) >= 0
               and plane.vp(g_unit[j], prime) >= 0 for j in range(n + 1))

    # Y must be known one degree further than K: division by xi loses one.
    y = truncate(ratio(s_of_w), n + 1)
    y_unit = divide_by_variable(y, n)
    positive_exponent = [fmpq(0)] * (n + 1)
    positive_exponent[r] = prime * b
    prefactor = (Series(positive_exponent, prec=n + 1).exp()
                 * (-22 / y_unit)**prime)

    def integral_rows(input_coefficients):
        polynomial = Series(input_coefficients, prec=prime)
        k = truncate(polynomial(y) / (22**prime) * prefactor, n)
        assert k[0] == 1
        rr = (k - 1) / prime
        assert all(plane.vp(rr[j], prime) >= 0 for j in range(n + 1))
        ee = truncate((-rr).exp() * (1 + prime*rr**2/2
                      + prime**2*(rr**4/8 - rr**3/3)), n)
        def drow(hh):
            return (hh[r-1] - hh[2*r-1]/b
                    + 2*hh[3*r-1]/b**2)
        return k, ee, (drow(ee), drow(y * ee))

    k, recovered, two_rows = integral_rows(coefficients)
    exact_k = (1 / f_unit)**prime
    assert all(k[j] == exact_k[j] for j in range(n + 1))
    for j in range(n + 1):
        assert plane.vp(recovered[j] - f_unit[j], prime) >= 3
        assert plane.vp(((1+y)*recovered)[j] - g_unit[j], prime) >= 3

    unit_minor = None
    if r >= 3:
        columns_modp = []
        for index in (r-1, r-2):
            varied = coefficients[:]
            varied[index] += prime
            _, _, changed = integral_rows(varied)
            columns_modp.append([modp(changed[i] - two_rows[i], prime)
                                for i in range(2)])
        determinant = (columns_modp[0][0] * columns_modp[1][1]
                       - columns_modp[1][0] * columns_modp[0][1]) % prime
        expected = pow(-22, 2*r-4, prime)
        assert determinant == expected and determinant != 0
        unit_minor = determinant
    else:
        assert modp(axis_b[r] - axis_a[r], prime) == (-22) % prime != 0

    print(json.dumps({
        "p": prime, "complete_first_block": prime,
        "read_Y_through": n+1, "recovered_axis_through": n+1,
        "negative_power_identity": True, "exact_K_identity": True,
        "central_reconstruction_precision": 3,
        "unit_jacobian_mod_p": unit_minor, "verified": True
    }), flush=True)


if __name__ == "__main__":
    for p in (7, 19, 31):
        check(p)
