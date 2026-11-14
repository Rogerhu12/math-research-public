#!/usr/bin/env python3
"""One exact 2D check of R175, including its last normal-step carry.

p=7, total ambient degree 13.  Build the finite Teichmuller averages
in (eta,w), invert both formal variables, and evaluate the actual A_2,
B,A_2^2.  This independently checks the second-band identity and all
the mod-p^2 first-band rows, including h=p-1.
"""
import importlib.util
import json
from math import comb, factorial
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series

spec = importlib.util.spec_from_file_location(
    "actual_plane", Path(__file__).with_name("check-theta-plane-saturated-jets.py"))
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)

PRIME, R, PERIOD, DEGREE = 7, 2, 12, 13
ZERO = fmpq(0)
ONE = {(0, 0): fmpq(1)}
U = {(1, 0): fmpq(1)}
V = {(0, 1): fmpq(1)}


def add(left, right, sign=1):
    result = left.copy()
    for key, value in right.items():
        result[key] = result.get(key, ZERO) + sign * value
        if not result[key]:
            del result[key]
    return result


def multiply(left, right):
    result = {}
    for (i, j), value in left.items():
        for (k, ell), other in right.items():
            if i+j+k+ell <= DEGREE:
                key = (i+k, j+ell)
                result[key] = result.get(key, ZERO) + value * other
    return {key: value for key, value in result.items() if value}


def powers(value):
    result = [ONE]
    for _ in range(DEGREE):
        result.append(multiply(result[-1], value))
    return result


def compose(polynomial, first, second):
    first_powers, second_powers = powers(first), powers(second)
    result = {}
    for (i, j), coefficient in polynomial.items():
        for key, value in multiply(first_powers[i], second_powers[j]).items():
            result[key] = result.get(key, ZERO) + coefficient * value
    return {key: value for key, value in result.items() if value}


def modulo(value, modulus):
    denominator = int(value.denominator) % modulus
    assert denominator % PRIME
    return int(value.numerator) % modulus * pow(denominator, -1, modulus) % modulus


columns, rows = plane.actual_rows(4)
cap = ctx.cap
s = Series([0, 1], prec=cap)
period = Series([fmpq(comb(2*n, n), 4**n*(4*n+1))
                 for n in range(cap)], prec=cap)
sw = (s * period**4).reversion()
logarithm = [ZERO] * cap
coefficient = fmpq(1, 3)
for n in range(1, cap):
    logarithm[n] = coefficient / n
    coefficient *= fmpq(4*n+1, 4*n+3)
aw = Series(logarithm, prec=cap).exp()(sw)
bw = sw * aw
xi = aw - bw/3
u0, kappa = xi[R], xi[R] - bw[R+1]
pi0 = 1/u0
assert plane.vp(pi0, PRIME) == 1
assert plane.vp(kappa, PRIME) >= 0

first_average, second_average = {}, {}
for h in range(DEGREE+1):
    for k in range(DEGREE-h+1):
        if (R*(h-1)+k) % PERIOD == 0 and (h, k) != (0, 0) and xi[k]:
            first_average[h, k] = xi[k] / factorial(h)
        if (R*h+k-1) % PERIOD == 0 and bw[k]:
            second_average[h, k] = bw[k] / factorial(h)
assert first_average[(1, 0)] == second_average[(0, 1)] == 1
first_tail, second_tail = add(first_average, U, -1), add(second_average, V, -1)
inverse_first, inverse_second = U, V
for _ in range(DEGREE):
    inverse_first, inverse_second = (
        add(U, compose(first_tail, inverse_first, inverse_second), -1),
        add(V, compose(second_tail, inverse_first, inverse_second), -1))

ctx.cap = DEGREE+2
eta = Series([fmpq(1, factorial(h)) if h % (PRIME-1) == 1 else ZERO
              for h in range(DEGREE+2)], prec=DEGREE+2).reversion()
radial_a = eta.exp()
radial_b = Series([fmpq(1, factorial(h)) if h % (PRIME-1) == 0 else ZERO
                   for h in range(DEGREE+2)], prec=DEGREE+2)(eta)

ctx.cap = cap
first_w = Series([row[columns.index((1, 0))] for row in rows], prec=cap)(sw)
difference_w = Series([row[columns.index((1, 1))] for row in rows], prec=cap)(sw)
examples = [("A2", 17, first_w),
            ("B", 17, first_w+difference_w),
            ("A2_squared", 34, first_w**2)]
checks = 0
for label, degree, actual in examples:
    original = {(h, k): degree**h * actual[k] / factorial(h)
                for h in range(DEGREE+1)
                for k in range(DEGREE-h+1) if actual[k]}
    transformed = compose(original, inverse_first, inverse_second)
    assert all(plane.vp(value, PRIME) >= 0 for value in transformed.values())
    ctx.cap = DEGREE+2
    for j in range(R+1):
        amplitude = actual[j+R] - degree*u0*actual[j]
        predicted = (radial_a**degree / radial_b**(j+R)
                     * (amplitude + j*kappa*radial_b.derivative()*actual[j]))
        for h in range(DEGREE-j-R+1):
            assert transformed.get((h, j+R), ZERO) == predicted[h], (label, h, j)
            checks += 1
    for j in range(R):
        gj = transformed.get((0, j), ZERO)
        gnext = transformed.get((0, j+R), ZERO)
        for h in range(1, PRIME):
            exact_row = sum((pi0**q * transformed.get((h-q, j+R*q), ZERO)
                             for q in range(h+1)), ZERO)
            if h < PRIME-1:
                rhs = degree**h*gj + pi0*h*degree**(h-1)*gnext
            else:
                rhs = ((degree**h-j)*gj
                       + pi0*h*(degree**(h-1)*gnext+j*kappa*gj))
            assert modulo(factorial(h)*exact_row-rhs, PRIME**2) == 0, (label, h, j)
            checks += 1
    print(json.dumps({"p": PRIME, "source": label, "ambient_degree": DEGREE,
                      "second_band_and_endpoint": True}), flush=True)
    ctx.cap = cap
print(json.dumps({"checks": checks, "verified": True}), flush=True)
