#!/usr/bin/env python3
"""Exact finite-field certificate excluding R53's primitive index equation.

Only the Python standard library is needed.  The large q is reconstructed
from R53's defining product.  Its primality and the global number-field
facts are proved in R53; this certificate checks the new prime 521 data.
Both W signs and every short Weierstrass model with the required
discriminant are enumerated.  No class-group or Mordell--Weil computation
is used.
"""
import json
import math
import sys
from collections import Counter

sys.dont_write_bytecode = True


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


p, ell = 43, 521
assert is_prime(p) and is_prime(ell)
small_primes = [r for r in range(2, 462) if is_prime(r)]
assert len(small_primes) == 89
n = 116 * math.prod(small_primes)
q = 432 * n * n - 1
assert len(str(q)) == 387
assert n % ell == 182 and q % ell == 302
assert q % ell and ell % 8 == 1

cubes = [x * x * x % ell for x in range(ell)]
square_roots = [[] for _ in range(ell)]
for y in range(ell):
    square_roots[y*y % ell].append(y)
root_counts = [len(r) for r in square_roots]


def curve_data(X, W):
    """F: y^2=x^3-X*x-2*W; return (number of rational 2-roots, trace)."""
    values = [(cubes[x] - X*x - 2*W) % ell for x in range(ell)]
    number_of_points = 1 + sum(root_counts[t] for t in values)
    trace = ell + 1 - number_of_points
    assert trace * trace <= 4 * ell
    return values.count(0), trace


L_roots = [x for x in range(ell) if (cubes[x] - x - 8*n) % ell == 0]
assert L_roots == []
A_two_roots, a_A = curve_data(1, 0)
assert A_two_roots == 3 and a_A == -22
delta = -pow(q, p, ell) % ell
Delta = 64 * delta % ell
assert delta == 201 and Delta == 360
quartic_sign = pow(Delta, (ell-1)//4, ell)
assert quartic_sign == 1
fourth_root_Delta = next(x for x in range(1, ell) if pow(x, 4, ell) == Delta)
square_root_2 = square_roots[2][0]
assert square_root_2 * square_root_2 % ell == 2
assert pow(2, (ell-1)//2, ell) == 1
trace_candidates = [a for a in range(-math.isqrt(4*ell), math.isqrt(4*ell)+1)
                    if a % p == a_A % p]
assert trace_candidates == [-22, 21]
assert not any(a % 4 == (-quartic_sign) % 4 for a in trace_candidates)

# Independent full model enumeration, including both W signs.
histograms = {0: Counter(), 1: Counter(), 3: Counter()}
survivors = []
for X in range(ell):
    for W in range(ell):
        if (cubes[X] - 27*W*W) % ell != delta:
            continue
        number_of_roots, trace = curve_data(X, W)
        assert number_of_roots in histograms
        histograms[number_of_roots][trace] += 1
        if number_of_roots == 0 and trace % p == a_A % p:
            survivors.append([X, W, trace])

counts = {r: sum(h.values()) for r, h in histograms.items()}
assert counts == {0: 348, 1: 0, 3: 173}
assert sum(counts.values()) == 521
assert survivors == []
assert all(a % 4 == 3 for a in histograms[0])
assert 21 not in histograms[0] and -22 not in histograms[0]
assert histograms[3][-22] == 5

# The known nonprimitive scaling still exists and fails the mod-43 trace test.
scaled_X = pow(q, 14, ell)
scaled_W = 4*n*pow(q, 21, ell) % ell
scaled_type, scaled_trace = curve_data(scaled_X, scaled_W)
assert scaled_type == 0 and scaled_trace == 35
assert (scaled_X**3 - 27*scaled_W**2) % ell == delta

result = {
    "p": p, "ell": ell, "small_prime_count": len(small_primes),
    "q_decimal_digits": len(str(q)), "n_mod_ell": n % ell,
    "q_mod_ell": q % ell, "L_polynomial_mod_ell": [107, -1, 0, 1],
    "L_polynomial_roots": L_roots,
    "index_rhs_signs_mod_ell": [2*pow(q, 21, ell) % ell,
                                -2*pow(q, 21, ell) % ell],
    "X_cubed_minus_27W_squared": delta, "Frey_discriminant": Delta,
    "fourth_root_of_discriminant": fourth_root_Delta,
    "quartic_discriminant_sign": quartic_sign,
    "square_root_of_2": square_root_2,
    "A_point_count": ell + 1 - a_A, "A_trace": a_A,
    "Hasse_and_mod43_candidates": trace_candidates,
    "required_trace_mod4": 3,
    "model_counts_by_cubic_root_count": counts,
    "irreducible_cubic_trace_histogram": sorted(histograms[0].items()),
    "same_L_and_mod43_survivors": survivors,
    "split_cubic_models_with_trace_minus22": histograms[3][-22],
    "nonprimitive_scaled_point": {
        "u_mod_ell": pow(q, 7, ell), "v_mod_ell": 0,
        "X_mod_ell": scaled_X, "W_mod_ell": scaled_W, "trace": scaled_trace,
    },
}
print(json.dumps(result, indent=2))
