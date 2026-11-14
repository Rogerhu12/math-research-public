#!/usr/bin/env python3
"""Exact rational certificate for a local internal phase-opening seed.

This is finite polynomial algebra, not a profile boundary-value integration or
a geometric design.  The accompanying note proves local smooth existence;
global compact support, total moments and geometric realization remain open.
"""
from fractions import Fraction as F
import argparse
import json
import math
from pathlib import Path


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(*terms):
    answer = [F(0)]*max(map(len, terms))
    for term in terms:
        for j, value in enumerate(term):
            answer[j] += value
    return trim(answer)


def scale(a, c):
    return trim([F(c)*value for value in a])


def multiply(a, b):
    answer = [F(0)]*(len(a)+len(b)-1)
    for j, u in enumerate(a):
        for k, v in enumerate(b):
            answer[j+k] += u*v
    return trim(answer)


def derivative(a, order=1):
    for _ in range(order):
        a = [j*a[j] for j in range(1, len(a))] or [F(0)]
    return a


def coefficient(a, n):
    return a[n] if n < len(a) else F(0)


C = list(map(F, [1, 0, -2, 0, 1]))
W = list(map(F, [0, 1, 0, 2]))
A1 = list(map(F, [2, 0, -4]))
A2 = add(derivative(C), scale(W, -1))
D = F(-8)


def expressions(f):
    f1, f2, f3, f4 = (derivative(f, j) for j in range(1, 5))
    L = add(multiply(A1, f), scale(multiply(A2, f1), 2),
            scale(multiply(C, f2), -2))
    H = add([2*D], scale(A1, 2), scale(derivative(A2), 4))
    M = add(scale(multiply(derivative(A1), f), 2), multiply(H, f1),
            scale(multiply(W, f2), -4))
    Q = add(multiply(L, f4), scale(multiply(C, multiply(f3, f3)), -2),
            multiply(M, f3), scale(multiply(f2, f2), 3*D))
    P3 = add(M, scale(multiply(C, f3), -4))
    identity = add(P3, scale(derivative(L), -2), scale(f1, -2*D))
    assert all(value == 0 for value in identity)
    return L, P3, Q


def certificate(order=12):
    f = [F(1), F(-1, 2), F(1, 2), F(1, 3)]
    denominators = []
    for n in range(4, order+1):
        zero = f+[F(0)]
        one = f+[F(1)]
        old = coefficient(expressions(zero)[2], n-3)
        slope = coefficient(expressions(one)[2], n-3)-old
        expected = 8*n*(n-1)*(n-2)
        assert slope == expected
        f.append(-old/slope)
        denominators.append(dict(degree=n, actual=str(slope), expected=expected))
    L, P3, Q = expressions(f)
    assert all(coefficient(Q, j) == 0 for j in range(order-2))
    assert coefficient(L, 0) == coefficient(L, 1) == 0
    ell2, ell3 = coefficient(L, 2), coefficient(L, 3)
    p30, p31 = coefficient(P3, 0), coefficient(P3, 1)
    sigma = -p30/ell2
    mu = 6-(ell3*sigma+p31)/ell2
    assert (ell2, ell3, p30, p31, sigma, mu) == (
        F(-34), F(-348), F(8), F(-152), F(4, 17), F(-254, 289))
    jets = [coefficient(f, j)*math.factorial(j) for j in range(order+1)]
    assert jets[:6] == list(map(F, [1, F(-1, 2), 1, 2, 25, 1040]))
    # At x=0 the three local integration constants making O=O'=O''=0.
    J0, J1, J2 = F(44, 9), F(3, 4), F(-14, 9)
    initial_O = [-1+J0+F(5, 2)*J2, 3-4*J1, 8-J0+2*J2]
    assert initial_O == [0, 0, 0]
    # Formal second exponential sector: DQ_F h2 + Q(h1) at its first order.
    second_sector = sigma*sigma/(2*ell2)
    assert second_sector == F(-4, 4913)
    return dict(schema='literature-internal-phase-rational-certificate-v1',
                arithmetic='fractions.Fraction', no_geometry_evaluated=True,
                no_numerical_ode_or_optimization=True,
                coefficients=dict(p0='2', p1='0', p2='-4', r0='1', r1='0',
                                  s0='0', s1='-4', t0='5/2', t1='0'),
                formal_series_order=order,
                formal_series_coefficients=list(map(str, f)),
                formal_derivative_jets=list(map(str, jets)),
                recurrence_denominators=denominators,
                Q_zero_through_degree=order-3,
                L_second_coefficient=str(ell2), L_third_coefficient=str(ell3),
                transverse_P3_constant=str(p30), transverse_P3_linear=str(p31),
                transverse_positive_exponential_rate=str(sigma),
                transverse_formal_power=str(mu),
                formal_second_exponential_sector_leading=str(second_sector),
                local_moment_initial_values=list(map(str, [J0, J1, J2])),
                local_O_jet=list(map(str, initial_O)),
                global_compact_profile_constructed=False,
                global_tail_moments_realized=False,
                geometric_base_realized=False, finite_flex_proved=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = certificate()
    body = json.dumps(report, indent=2)+'\n'
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(body)
    print(body)


if __name__ == '__main__':
    main()
