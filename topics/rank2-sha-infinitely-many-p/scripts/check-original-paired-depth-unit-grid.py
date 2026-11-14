#!/usr/bin/env python3
"""Exact fixed coefficients for R427; no scan over target primes."""

from fractions import Fraction as F
import json


def pair_coefficient(r, t):
    return F(r+t-(r-t)**2, 2)


sigma = {1: F(1), 7: F(1, 210), 13: F(-1, 1801800)}
c0 = pair_coefficient(1, 1)*sigma[1]**2
c1 = sum(pair_coefficient(r, t)*sigma[r]*sigma[t]
         for r, t in [(1, 7), (7, 1)])
c2 = sum(pair_coefficient(r, t)*sigma[r]*sigma[t]
         for r, t in [(1, 13), (7, 7), (13, 1)])
assert (c0, c1, c2) == (F(1), F(-2, 15), F(4, 17325))
theta12_independent = F(1, 637)-F(1, 735)+F(1, 22050)-F(1, 42042)
assert theta12_independent == c2
assert 17325 == 3**2*5**2*7*11
assert 11 % 3 == 2

report = {
    "scope": "Fixed exact pair aggregation; no target-prime scan.",
    "sigma_coefficients_after_removing_b_powers": {str(k): str(v) for k, v in sigma.items()},
    "all_pair_collisions": {
        "total_2": [[1, 1]],
        "total_8": [[1, 7], [7, 1]],
        "total_14": [[1, 13], [7, 7], [13, 1]]
    },
    "pair_weights": {f"{r},{t}": str(pair_coefficient(r, t))
                     for r, t in [(1, 1), (7, 1), (7, 7), (13, 1)]},
    "theta_coefficients_after_removing_b_powers": [str(c0), str(c1), str(c2)],
    "theta12_independent_x_sigma_identity": str(theta12_independent),
    "last_denominator_factorization": "3^2*5^2*7*11",
    "prime_11_inert": True,
    "grid": "five unweighted inputs share one depth; each Theta pair shares one depth",
    "chosen_m": "ceil(((p-7)/6)/2)",
    "number_of_independent_depths": "1+m",
    "coefficient": "(p-1)*(p-3)!*I_{-(p-2)}*Omega^(p-2)*product(q_h^(6*k_h)*theta_(6*k_h))",
    "scope_of_nonvanishing": "Some point in every sufficiently deep full Cartesian grid; no assertion for every point."
}
print(json.dumps(report, indent=2))
