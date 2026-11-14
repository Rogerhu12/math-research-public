#!/usr/bin/env python3
"""Exact algebra and finite-grid convolution checks; no numerical tail solve.

All trigonometric grid identities refer to exact equally spaced angles and
the real orthonormal sine/cosine basis. Binary64 trig tables are not asserted
to satisfy those identities bitwise.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'repro/source-root/topics/large-amplitude-twist-flex/scripts'


class Poly:
    """Minimal exact Q[L,Pt,P,v,s,X] ring for clearing denominators."""
    zero = (0,) * 6

    def __init__(self, value=0):
        self.terms = ({k: F(v) for k, v in value.items() if v}
                      if isinstance(value, dict) else ({self.zero: F(value)} if value else {}))

    @classmethod
    def variable(cls, index):
        powers = [0] * 6
        powers[index] = 1
        return cls({tuple(powers): 1})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        result = dict(self.terms)
        for key, value in other.terms.items():
            result[key] = result.get(key, F(0)) + value
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -(other if isinstance(other, Poly) else Poly(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly(other)
        result = {}
        for a, x in self.terms.items():
            for b, y in other.terms.items():
                key = tuple(i + j for i, j in zip(a, b))
                result[key] = result.get(key, F(0)) + x * y
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = Poly(1)
        for _ in range(n):
            result = result * self
        return result


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def multiply(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def ordinary_basis(kind, k):
    if k == 0:
        assert kind == 'cos'
        return {0: (F(1), F(0))}
    if kind == 'cos':
        return {k: (F(1, 2), F(0)), -k: (F(1, 2), F(0))}
    assert kind == 'sin'
    return {k: (F(0), F(-1, 2)), -k: (F(0), F(1, 2))}


def normalized_triple(factors, period=None):
    poly = {0: (F(1), F(0))}
    nonconstant = 0
    for kind, k in factors:
        nonconstant += k != 0
        result = {}
        for a, x in poly.items():
            for b, y in ordinary_basis(kind, k).items():
                result[a + b] = add(result.get(a + b, (F(0), F(0))), multiply(x, y))
        poly = result
    total = (F(0), F(0))
    for k, z in poly.items():
        if (k == 0) if period is None else (k % period == 0):
            total = add(total, z)
    assert total[1] == 0
    value = total[0] * 2 ** (nonconstant // 2)
    # Return a+b*sqrt(2), with exact rational coefficients.
    return (F(0), value) if nonconstant % 2 else (value, F(0))


def b_expected(i, j, k):
    if i == 0:
        return F(k == j), F(0)
    if j == 0:
        return F(k == i), F(0)
    a = F(i == j and k == 0)
    b = F((k == i + j) + (i != j and k == abs(i - j)), 2)
    return a, b


def flux_expected(j, k, ell):
    if ell == 0:
        return F(j == k), F(0)
    sign = 1 if k > ell else -1 if k < ell else 0
    return F(0), F((j == k + ell) + sign * (j == abs(k - ell)), 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--modes', type=int, default=15)
    ap.add_argument('--spacing', type=int, default=3)
    ap.add_argument('--quadrature', type=int, default=256)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    M, spacing, N = args.modes, args.spacing, args.quadrature
    assert M >= 1 and spacing >= 1 and N > 4 * M * spacing
    period = N // math.gcd(N, spacing)
    assert period > 3 * M

    L, Pt, P, v, s, X = [Poly.variable(j) for j in range(6)]
    E, K, S, A = 1 + v, L - Pt, 1 - v * P * P, 1 + L + v * Pt
    T = 2 * K + K * K + E * P * P
    u, D = v * T, 1 - v * T
    us = 1 - s * s
    # fc is checked after multiplying by 2*s*(1+s)^2; gc and
    # the split identity use S*s*(1+s). Their denominators are positive
    # on the original real guard, so this loses no solution there.
    gc_numerator = v * P * P * (1 + s) + S * us
    identities = {
        'quadratic_q': F(1, 2) * (K * K + E * P * P) + K * Pt
            - F(1, 2) * (L * L + E * P * P - Pt * Pt),
        'fc_identity': s * (1 + s) ** 2 + us * (2 + s) - 2 * (1 + s),
        'gc_identity': gc_numerator - (1 - S * s) * (1 + s),
        'split_factor': K * (1 + s) + us + v * P * P * s * (1 + s)
            - K * S * s * (1 + s) - (1 + K) * gc_numerator,
        'jacobian_polynomial_peel': (L + v * Pt) + (1 + L + v * Pt) * X
            - (L + v * Pt + A * X),
        'jacobian_discriminant': D + v * (1 + K) ** 2 - E * S,
        'jacobian_numerator': 1 + K + E * Pt - A,
    }
    assert all(not value.terms for value in identities.values())
    cos_count = sine_count = 0
    for i in range(M + 1):
        for j in range(M + 1):
            for k in range(M + 1):
                factors = [('cos', i), ('cos', j), ('cos', k)]
                expected = b_expected(i, j, k)
                assert normalized_triple(factors) == expected
                assert normalized_triple(factors, period) == expected
                cos_count += 1
    for j in range(1, M + 1):
        for k in range(1, M + 1):
            for ell in range(M + 1):
                factors = [('sin', j), ('sin', k), ('cos', ell)]
                expected = flux_expected(j, k, ell)
                assert normalized_triple(factors) == expected
                assert normalized_triple(factors, period) == expected
                sine_count += 1
    counter = normalized_triple([('cos', M)] * 3, 3 * M)
    assert normalized_triple([('cos', M)] * 3) == (F(0), F(0))
    assert counter == (F(0), F(1, 2))
    names = ['general_root_tail_momentum.mjs', 'f6tail_momentum_split_flux.mjs',
             'f6tail_fast_split_flux_engine.mjs', 'f6tail_fast_momentum.mjs']
    result = dict(status='PASS: exact symbolic algebra and rational Laurent projection checks',
        scope=__doc__, solver_implemented_or_run=False,
        parameters=dict(M=M, spacing=spacing, N=N, reduced_period=period),
        maximum_polynomial_harmonic=2 * M, maximum_tested_harmonic=3 * M,
        symbolic_identities={name: '0 exactly after denominator clearing' for name in identities},
        exact_cos_cos_cos_cases=cos_count, exact_sin_sin_cos_cases=sine_count,
        equality_boundary_counterexample=dict(reduced_period=3 * M,
            integrand='c_M**3', continuous_mean='0', discrete_mean='sqrt(2)/2'),
        source_sha256={name: sha(SOURCE / name) for name in names},
        script_sha256=sha(__file__))
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(status=result['status'], cosine_cases=cos_count,
                         sine_cases=sine_count, out=str(args.out))))


if __name__ == '__main__':
    main()
