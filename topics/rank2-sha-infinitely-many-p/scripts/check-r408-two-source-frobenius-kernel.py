#!/usr/bin/env python3
"""Fixed algebra checks for R408; no search over target primes.

The theorem is proved by the divisor calculation in R408.  This script checks
the exact fixed discriminants/resultants and the residue formula, then gives
one example showing that the new source-saturation range is larger.
"""
import json
from fractions import Fraction
import sympy as sp

t = sp.symbols("t")
h = 16*t*t+4*t+7
V = (1-4*t)*(1-20*t-8*t*t)*(1+96*t+48*t*t-64*t**3)
fixed = [t, t-1, h, V, 1+8*t]
discriminants = [int(sp.discriminant(f, t)) for f in fixed]
resultants = {
    f"{i},{j}": int(sp.resultant(fixed[i], fixed[j], t))
    for i in range(5) for j in range(i)
}
assert discriminants[2] == -2**4*3**3
assert discriminants[3] == 2**52*3**39
expected = {
    "1,0": 1, "2,0": 7, "2,1": 3**3,
    "3,0": 1, "3,1": 3**8, "3,2": 2**22*3**16,
    "4,0": -1, "4,1": -9, "4,2": 2**4*3**3,
    "4,3": -2**11*3**8,
}
assert resultants == expected


def e(m):
    return 3*((3*m+3)//4)+2*((m+1)//2)+(2*m+2)//3-2


def exponents(p, n, j):
    A, B, C = (n+1)//4, (n+1)//3, n//2
    Ej = 19*j*pow(17, -1, p) % p
    r, u, v, z = (-(A+j)) % p, (-(B+j)) % p, (-j) % p, (C+Ej) % p
    assert (r+A+j) % p == 0
    assert (u+B+j) % p == 0
    assert (v+j) % p == 0
    assert (17*(z-C)-19*j) % p == 0
    return r, u, v, z


def kernel_dimension(p, D, J):
    total = 0
    contributing = []
    for n in range(D+1):
        A, B, C = (n+1)//4, (n+1)//3, n//2
        assert 3*A+B-C+e(n+1) == 9*n//2+4
        for j in range(J+1):
            r, u, v, z = exponents(p, n, j)
            mu = 3*r+u+6*v+z
            dim = max(0, 1+(e(n+1)-mu)//p)
            total += dim
            if dim:
                contributing.append({"n": n, "j": j, "dimension": dim, "degree": mu})
    return total, contributing


example = {"p": 101, "D": 21, "J": 16}
p, D, J = (example[x] for x in ("p", "D", "J"))
example["f_D"] = 9*D//2+4
example["old_required_lower_bound"] = max(17*example["f_D"]+151*J, 17*(D//2)+19*J)
example["kernel_dimension"], example["contributing_components"] = kernel_dimension(p, D, J)
assert example["kernel_dimension"] == 2
assert example["contributing_components"] == [
    {"n": 0, "j": 0, "dimension": 1, "degree": 0},
    {"n": 1, "j": 0, "dimension": 1, "degree": 0},
]
assert example["f_D"] < p < example["old_required_lower_bound"]
print(json.dumps({"status": "passed", "discriminants": discriminants,
                  "resultants": resultants, "range_example": example}, indent=2))
