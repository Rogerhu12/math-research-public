#!/usr/bin/env python3
"""Exact finite group-ring checks for the original-unit CM5 work note.

The universal proof is in the note.  These checks independently compute
integer Smith forms, then retain their p-primary factors.
"""
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def valuation(number, prime):
    number = abs(int(number))
    assert number
    exponent = 0
    while number % prime == 0:
        number //= prime
        exponent += 1
    return exponent


checks = []
cases = []
for p in (3, 5):
    for n in (1, 2, 3):
        for e in (0, 1, 2):
            d, u, k = p ** (n - 1), 1 + p, p**e
            shift = sp.zeros(d)
            for j in range(d):
                shift[(j + 1) % d, j] = 1
            theta = shift - u * sp.eye(d)
            quotient, power = sp.zeros(d), sp.eye(d)
            for j in range(k):
                quotient += u ** (k - 1 - j) * power
                power = power * shift
            assert theta * quotient == power - u**k * sp.eye(d)
            checks.append(f"p={p}, n={n}, e={e}: exact central product")
            smith = smith_normal_form(quotient, domain=ZZ)
            actual = sorted(valuation(smith[j, j], p) for j in range(d))
            expected = (
                [e + 1 - n] + [e + 1] * (d - 1)
                if n <= e + 1
                else [0] * (d - (k - 1)) + [n] * (k - 1)
            )
            assert actual == sorted(expected)
            checks.append(f"p={p}, n={n}, e={e}: all p-primary Smith factors")
            cases.append(dict(p=p, n=n, e=e, dimension=d, smith_exponents=actual))

point_count_5 = 1 + sum(
    1 for x in range(5) for y in range(5) if (y * y - x**3 + 17 * x) % 5 == 0
)
assert point_count_5 == 10
checks.append("E17 over F5: trace -4")
roots_13_squared = [a for a in range(169) if (a * a + 1) % 169 == 0]
fermat_residues = [pow((a - 2) % 169, 12, 169) for a in roots_13_squared]
assert roots_13_squared == [70, 99] and fermat_residues == [27, 157]
checks.append("Both p=13 embeddings: e=0 for lambda=-2+i")

output = dict(
    status="PASS",
    number_of_checks=len(checks),
    checks=checks,
    group_ring_cases=cases,
    point_count_5=point_count_5,
    p13_i_roots=roots_13_squared,
    p13_fermat_residues=fermat_residues,
)
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(dict(status="PASS", checks=len(checks), output=str(destination))))
