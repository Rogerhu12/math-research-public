"""Finite integer-Horner evaluation of the unchanged R48 quartic.

This replaces only the first helper's nonfinite signed-interval power path.
The original source/data are retained. Every new intersection explicitly
requires two finite enclosures; no NaN can silently select the old argument.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import hashlib
from math import comb
from pathlib import Path

from flint import acb, arb
from tail_outer_weighted_compatible import (
    intersection as original_intersection,
    weighted_panel_fields as original_weighted_panel_fields)
from tail_outer_centered_quartic_fields import (
    quartic_coefficients, rational_identity_checks as original_identity_checks)

ORIGINAL_SHA = "16a868a4f59311a7e83d5758d1653b7c64a4836bc77e8c8f39aade459006889a"
if hashlib.sha256(Path(__file__).with_name(
        "tail_outer_centered_quartic_fields.py").read_bytes()).hexdigest() != ORIGINAL_SHA:
    raise ValueError("The preserved original quartic helper changed")


def finite(value):
    value = value if isinstance(value, arb) else arb(value)
    if not value.is_finite():
        raise ArithmeticError("A nonfinite same-polynomial enclosure is forbidden")
    return value


def intersection(a, b):
    return finite(original_intersection(finite(a), finite(b)))


def integer_power(x, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Only nonnegative integer powers are used")
    x, out = finite(x), arb(1)
    for _ in range(n):
        out = out*x
    return finite(out)


def horner(coefficients, x):
    x, out = finite(x), arb(0)
    for coefficient in reversed(coefficients):
        out = out*x+finite(coefficient)
    return finite(out)


def centered_range(coefficients, u):
    u = finite(u)
    midpoint = u.mid()
    delta = u-midpoint
    shifted = [sum((comb(i, j)*finite(coefficients[i])*
                    integer_power(midpoint, i-j)
                    for i in range(j, len(coefficients))), arb(0))
               for j in range(len(coefficients))]
    return horner(shifted, delta)


def weighted_panel_fields(candidate, *, u, u_x, prefix_moments, suffix_moments):
    u, u_x = finite(u), finite(u_x)
    H, K, Kx = original_weighted_panel_fields(candidate, u=u, u_x=u_x,
        prefix_moments=prefix_moments, suffix_moments=suffix_moments)
    u = intersection(u, arb(0).union(arb(1)))
    for m in sorted(candidate["left"]["K"]):
        coefficients = quartic_coefficients(candidate, m)
        derivative = [i*coefficients[i] for i in range(1, len(coefficients))]
        k = centered_range(coefficients, u)/2
        kx = u_x*centered_range(derivative, u)/2
        K[m] = K[-m] = acb(intersection(K[m].real, k))
        Kx[m] = Kx[-m] = acb(intersection(Kx[m].real, kx))
    return H, K, Kx


def rational_identity_checks():
    record = original_identity_checks()
    signed = arb(-1).union(arb(1))
    for j in range(5):
        finite(integer_power(signed, j))
    finite(horner([arb(1), arb(-2), arb(3), arb(-4), arb(5)], signed))
    try:
        intersection(arb(1), arb("nan"))
    except ArithmeticError:
        pass
    else:
        raise AssertionError("A nonfinite interval bypassed the explicit guard")
    record.update(integer_horner_on_signed_intervals_finite=True,
        nonfinite_intersection_rejected=True,
        original_helper_sha256=ORIGINAL_SHA,
        original_general_power_path_used=False)
    return record
