#!/usr/bin/env python3
"""Exact calibration of the explicit R184 source on the original A2/B graph.

Both the fixed-graph norm coefficients and the Lagrange coefficient formula
are computed from rational theta series. Check p-integrality, the genuine
vanishing prefix, and the canonical full-p bound through a finite tail.
No prepared polynomial or AS reduction is used to generate the data.
"""
import importlib.util
import json
from pathlib import Path

from flint import ctx, fmpq, fmpq_series as Series

spec = importlib.util.spec_from_file_location(
    "actual_plane", Path(__file__).with_name("check-theta-plane-saturated-jets.py"))
plane = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plane)


def check(prime):
    r = (prime+1)//4
    period = r*(prime-1)
    cutoff = (prime-1)//2
    required_order = 2*prime+cutoff+1
    last = required_order+6
    degree = 1
    while (degree+1)*(degree+2)//2+8 < last:
        degree += 1
    columns, rows = plane.actual_rows(degree)
    cap = ctx.cap
    a_index = columns.index((1, 0))
    d_index = columns.index((1, 1))
    original_a = Series([row[a_index] for row in rows], prec=cap)
    original_d = Series([row[d_index] for row in rows], prec=cap)
    a_unit = Series([original_a[k+1] for k in range(cap-1)], prec=cap-1)
    d_unit = Series([original_d[k+2] for k in range(cap-2)], prec=cap-2)
    original_ratio = original_d/original_a
    graph = (d_unit/a_unit**2)(original_a.reversion())
    assert graph[0] == -22
    coefficients = []
    for j in range(cutoff+1):
        value = -fmpq(prime, prime-j)*(graph**(prime-j))[j]
        lagrange = -(original_ratio**(prime-j-1)
                     *original_ratio.derivative()/a_unit**prime)[prime-1]
        assert value == lagrange, (prime, j)
        assert plane.vp(value, prime) >= 0, (prime, j)
        coefficients.append(value)
    assert coefficients[0] == 22**prime
    actual_value = original_d**prime
    for j, coefficient in enumerate(coefficients):
        actual_value += coefficient*original_a**(2*prime-j)*original_d**j
    assert all(actual_value[k] == 0 for k in range(required_order))
    omega = prime*(r+2*prime)
    first_nonzero = next(k for k in range(required_order, last+1)
                         if actual_value[k])
    for k in range(required_order, last+1):
        if actual_value[k]:
            assert period*plane.vp(actual_value[k], prime)+prime*k >= omega+period
    assert all(2*prime+2*j <= 3*prime-1 for j in range(cutoff+1))
    print(json.dumps({"p": prime, "degree": 2*prime,
                      "nonzero_homogeneous_degrees": [prime, 2*prime],
                      "coefficient_count": len(coefficients),
                      "required_prefix": required_order,
                      "first_nonzero_coefficient": first_nonzero,
                      "verified_through": last,
                      "norm_and_lagrange_equal": True,
                      "canonical_full_p_bound": True,
                      "constant_weight_three": True,
                      "verified": True}), flush=True)


if __name__ == "__main__":
    for prime in (7, 19):
        check(prime)
