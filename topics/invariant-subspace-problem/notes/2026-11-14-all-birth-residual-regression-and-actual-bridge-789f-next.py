#!/usr/bin/env python3
"""Exact full-incidence check of the all-birth residual/bridge interface.

Two fixed rational models cover a genuine deeper birth and both a regular
second height and the hard endpoint.  This is not a positivity scan.
"""
from functools import lru_cache
from itertools import combinations
from math import prod

import sympy as sp


def check_model(weights, birth):
    weights = tuple(map(sp.Rational, weights))
    count = len(weights)

    @lru_cache(None)
    def layer(r):
        return tuple(combinations(range(count), r))

    @lru_cache(None)
    def diagonal(r):
        return sp.diag(*[prod(weights[i] for i in I) for I in layer(r)])

    @lru_cache(None)
    def incidence(low, high, power=1):
        return sp.Matrix([
            [prod(weights[i] ** power for i in set(I) - set(J))
             if set(J) <= set(I) else 0 for I in layer(high)]
            for J in layer(low)
        ])

    @lru_cache(None)
    def kernel(r):
        if r == 0:
            return sp.ones(1, 1)
        return sp.Matrix.hstack(*incidence(r - 1, r).nullspace())

    @lru_cache(None)
    def source_metric(r):
        basis = kernel(r)
        return basis.T * basis

    @lru_cache(None)
    def feature(k, r):
        return sp.Matrix([
            [sp.S.One / prod(weights[i] for i in J) if set(J) <= set(I) else 0
             for J in layer(r)] for I in layer(k)
        ])

    @lru_cache(None)
    def residual(k, r):
        target = feature(k, r) * kernel(r)
        if r == 0:
            return target
        nuisance = feature(k, r - 1)
        metric = diagonal(k) ** 2
        return target - nuisance * (nuisance.T * metric * nuisance).inv() \
            * nuisance.T * metric * target

    @lru_cache(None)
    def precision(k, r):
        value = residual(k, r)
        return source_metric(r).inv() * value.T * diagonal(k) ** 2 * value

    @lru_cache(None)
    def gram(k, r):
        return precision(k, r).inv()

    @lru_cache(None)
    def bridge(r):
        return source_metric(r - 1).inv() * kernel(r - 1).T \
            * incidence(r - 1, r, 3) * kernel(r)

    def up(k):
        return sp.Matrix([
            [int(set(J) <= set(I)) for J in layer(k)]
            for I in layer(k + 1)
        ])

    def zero(matrix):
        assert matrix == sp.zeros(*matrix.shape)

    # Full physical inverse agrees with the weighted residual construction.
    for height in (0, 1):
        k = birth + height
        full_row = incidence(birth, k)
        full_gram = full_row * full_row.T
        c = precision(k, birth)
        zero(diagonal(k) * residual(k, birth)
             - full_row.T * full_gram.inv() * kernel(birth) * c)
        if birth > 0:
            zero(feature(k, birth - 1).T * diagonal(k) ** 2
                 * residual(k, birth))

    # The two actual consecutive low-birth regression coefficients.
    bmap = bridge(birth)
    theta = []
    for n in (1, 2):
        k = birth + n
        coefficient = gram(k, birth - 1) * bmap * precision(k - 1, birth)
        theta.append(coefficient)
        zero(up(k - 1) * residual(k - 1, birth)
             - n * residual(k, birth)
             + residual(k, birth - 1) * coefficient)

    k = birth + 1
    innovation = (theta[1] - theta[0]) / 2
    joint = (up(k) * residual(k, birth)
             + residual(k + 1, birth - 1) * theta[0]) / 2
    zero(joint - residual(k + 1, birth)
         + residual(k + 1, birth - 1) * innovation)
    zero(joint.T * diagonal(k + 1) ** 2 * joint
         - source_metric(birth) * precision(k + 1, birth)
         - innovation.T * source_metric(birth - 1)
         * precision(k + 1, birth - 1) * innovation)

    # The deep C^2 term in the twice-raised source remains present.
    twice = up(birth + 1) * up(birth) * residual(birth, birth)
    expected = (2 * residual(birth + 2, birth)
                - residual(birth + 2, birth - 1)
                * (theta[1] + 3 * theta[0])
                + residual(birth + 2, birth - 2)
                * gram(birth + 2, birth - 2)
                * bridge(birth - 1) * bmap)
    zero(twice - expected)
    print(f"PASS: M={count}, birth={birth}, weights={weights}")


def main():
    check_model((1, 2, 3, 4, 5), 2)
    check_model((1, 2, 3, 4, 5, 6), 2)
    print("PASS: full inverse, all lower nuisance, two bands, joint innovation, deep tower")


if __name__ == "__main__":
    main()
