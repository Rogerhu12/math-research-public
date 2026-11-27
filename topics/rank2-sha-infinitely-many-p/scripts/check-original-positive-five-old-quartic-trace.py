#!/usr/bin/env python3
"""Exact complete quartic trace for the original positive five-old source.

This evaluates the single proven formula in the original unitary note.
No prime scan or theta spectrum is computed. All polynomial operations are
over Q, and every inverse is returned with a complete Bezout identity.
Mathematical execution is restricted to the public Actions runner.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import os

if os.environ.get("GITHUB_ACTIONS") != "true":
    raise RuntimeError("Run mathematical checks only in public GitHub Actions")
if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise RuntimeError("The original public repository is required")


def trim(a):
    a = [Q(x) for x in a]
    while a and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def scale(a, s):
    return trim([Q(s) * x for x in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    if not a or not b:
        return []
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError("Zero polynomial")
    quotient = [Q(0)] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        quotient[shift] += coefficient
        a = sub(a, [Q(0)] * shift + scale(b, coefficient))
    return trim(quotient), a


def remainder(a, b):
    return divrem(a, b)[1]


def bezout_unit(a, b):
    r0, r1 = trim(a), trim(b)
    s0, s1 = [Q(1)], []
    t0, t1 = [], [Q(1)]
    while r1:
        quotient, r = divrem(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, sub(s0, mul(quotient, s1))
        t0, t1 = t1, sub(t0, mul(quotient, t1))
    if len(r0) != 1:
        raise ArithmeticError("The complete denominator is not a unit")
    u, v = scale(s0, 1 / r0[0]), scale(t0, 1 / r0[0])
    assert add(mul(u, a), mul(v, b)) == [Q(1)]
    return u, v


def fixed_trace(b):
    b = Q(b)
    q = [-256*b**4, -1600*b**3, -240*b**2, 380*b, Q(5)]
    derivative = [Q(i) * q[i] for i in range(1, len(q))]
    x = [Q(0), Q(1)]
    # The entire polynomial is squarefree; all original zeroes are retained.
    bezout_unit(derivative, q)
    numerator = mul(mul([4*b, Q(1)], [16*b*b, -4*b, Q(7)]),
                    [64*b**3, 48*b*b, -96*b, Q(1)])
    denominator = mul(x, mul(derivative, derivative))
    inverse, relation = bezout_unit(denominator, q)
    value = remainder(mul(numerator, inverse), q)
    assert remainder(sub(mul(denominator, value), numerator), q) == []

    # Full four-dimensional multiplication operator, with every entry retained.
    basis = [[Q(0)] * j + [Q(1)] for j in range(4)]
    columns = [remainder(mul(value, e), q) for e in basis]
    matrix = [[columns[j][i] if i < len(columns[j]) else Q(0)
               for j in range(4)] for i in range(4)]
    complete_trace = sum((matrix[i][i] for i in range(4)), Q(0))

    # Independent Lagrange residue identity:
    # sum f(alpha)/(alpha*q'(alpha)^2) is coeff(X^3,g)/lead(q),
    # where g is the unique remainder of f/(X*q') modulo q.
    first_denominator = mul(x, derivative)
    first_inverse, first_relation = bezout_unit(first_denominator, q)
    lagrange = remainder(mul(numerator, first_inverse), q)
    assert remainder(sub(mul(first_denominator, lagrange), numerator), q) == []
    residue_trace = (lagrange[3] if len(lagrange) > 3 else Q(0)) / q[-1]
    assert complete_trace == residue_trace
    return complete_trace, {
        "b": str(b),
        "quartic": [str(x) for x in q],
        "squarefree": True,
        "full_denominator_bezout_verified": True,
        "full_quotient_multiplication_dimension": 4,
        "full_return_verified": True,
        "lagrange_residue_identity_verified": True,
        "trace": str(complete_trace),
        "m0_over_delta": str(-complete_trace / 42),
        "positive_old_Y_coefficient": str(2 * complete_trace / 3),
        "nonzero": bool(complete_trace),
    }


t1, one = fixed_trace(1)
t17, original = fixed_trace(17)
assert t17 * 17 == t1
payload = {
    "kind": "original_positive_five_old_complete_quartic_trace",
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "source_commit": os.environ.get("GITHUB_SHA"),
    "normalization": "T_b=Tr[(X+4b)Q2(X)P3(X)/(X*q_b'(X)^2)]",
    "parameters": [one, original],
    "original_b": 17,
    "homogeneity_T17_equals_T1_over_17": True,
    "original_m0_over_delta": str(-t17 / 42),
    "original_c_plus": str(2 * t17 / 3),
    "complete_exact_check": "PASS",
    "outputs_persisted": False,
}
print(json.dumps(payload, sort_keys=True))
