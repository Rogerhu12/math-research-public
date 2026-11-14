#!/usr/bin/env python3
"""Exact rational certificate for the four-even-mode Volterra reduction.

This is finite algebra, not a numerical search for a flexible surface.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from pathlib import Path


def leading(m: int, n: int, alpha: Q, beta: Q) -> tuple[Q, Q]:
    total = m + n
    product = m * n
    fourth = product * (m - 1) * (n - 1)
    second_moment = product * ((m - 1) * (n - 1) + 2)
    p = (Q(total, 2) + Q(fourth, 4 * (total - 3))
         - Q(fourth, 2 * (total - 2)) + Q(second_moment, 4 * (total - 1)))
    c = (2 * alpha * product - 2 * (1 - beta) * Q(fourth, total - 2)
         - (2 * beta - 1) * Q(second_moment, total - 1))
    return p, c


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    rows = []
    for k, ell in combinations(range(4, 8), 2):
        r, s = k - 1, ell - 1
        alpha = Q(r * s, s - r + 1)
        beta = -Q(2 * (r + s) * (r - 1), s - r + 1)
        for m, n in combinations((8, 10, 12, 14), 2):
            p0, c0 = leading(n, n, alpha, beta)
            p1, c1 = leading(m, n, alpha, beta)
            det = p0 * c1 - p1 * c0
            if det <= 0:
                raise ArithmeticError(f'Unexpected nonpositive determinant {(k, ell, m, n, det)}')
            rows.append(dict(vanishing_orders=[k, ell], degree_pivots=[m, n],
                             alpha=str(alpha), beta=str(beta),
                             matrix=[[str(p0), str(c0)], [str(p1), str(c1)]],
                             determinant=str(det), strictly_positive=True))
    payload = dict(status='exact_rational_finite_certificate', arithmetic='fractions.Fraction',
                   profile_space='(1-x^2)^4 span(1,x^2,x^4,x^6)',
                   cases=len(rows), all_determinants_strictly_positive=True,
                   rows=rows, not_a_surface_existence_result=True,
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(dict(cases=len(rows), all_determinants_strictly_positive=True)))


if __name__ == '__main__':
    main()
