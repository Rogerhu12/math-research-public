#!/usr/bin/env python3
"""Exact bounded checks for R453; no target-prime scan.

The proof uses the displayed floor identities for every n.  This checks their
twelve residue classes, all allowed J, the finite free basis counts, and the
actual rational angular logarithmic derivative.
"""
from fractions import Fraction
import sympy as sp


def ceil_div(a, b):
    return (a + b - 1) // b


def e(m):
    return 3 * ceil_div(3 * m, 4) + 2 * ceil_div(m, 2) + ceil_div(2 * m, 3) - 2


def abc(n):
    return (n + 1) // 4, (n + 1) // 3, n // 2


rows = []
for n in range(12):
    A, B, C = abc(n)
    AA, BB, CC = abc(n + 2)
    da, db, dc = AA - A, BB - B, CC - C
    de = e(n + 3) - e(n + 1)
    assert dc == 1
    assert de == 10 - 3 * da - db
    assert de - (9 - 3 * da - db) == 1
    assert e(n + 13) - e(n + 1) == 47
    assert 3*A + B - C + e(n+1) == (9*n)//2 + 4
    rows.append((n, da, db, de, 1))

returns = []
for J in range(17):
    m = ceil_div(6 * J, 47)
    assert m <= 3
    for n in range(24):
        A, B, C = abc(n)
        AA, BB, CC = abc(n + 12*m)
        assert (AA-A, BB-B, CC-C) == (3*m, 4*m, 6*m)
        assert e(n + 12*m + 1) - e(n + 1) == 47*m
        for j in range(J+1):
            assert e(n+1) + 6*j + 6*(J-j) <= e(n+12*m+1)
    for D in range(21):
        old = (J+1) * sum(e(n+1)+1 for n in range(D+1))
        new = sum(e(n+1)+6*j+1 for n in range(D+1) for j in range(J+1))
        assert new-old == 3*(D+1)*J*(J+1)
    returns.append((J, 12*m, 3*m, 6*m))

t = sp.symbols("t")
d = 1+8*t
h7 = 7+4*t+16*t**2
a = t*(t-1)*h7
V = (1-4*t)*(1-20*t-8*t**2)*(1+96*t+48*t**2-64*t**3)
assert sp.Poly(V, t).degree() == 6
assert sp.Poly(V, t).LC() == -2048
L0 = 1 + t/(t-1) + t*sp.diff(h7,t)/h7 - sp.Rational(152,17)*t/d
actual_L0 = t*sp.diff(a,t)/a - sp.Rational(19,17)*8*t/d
assert sp.cancel(actual_L0-L0) == 0
An, Bn, Cn, k, j = sp.symbols("An Bn Cn k j")
qn_derivative = An*(1+t*sp.diff(h7,t)/h7)+Bn*t/(t-1)-Cn*8*t/d
displayed = (k+An+j+(An+j)*t*sp.diff(h7,t)/h7
             +(Bn+j)*t/(t-1)+8*(-Cn+j*(1-sp.Rational(36,17)))*t/d)
assert sp.cancel(k+qn_derivative+j*L0-displayed) == 0

print("n, delta_A, delta_B, delta_e, degree_slack")
for row in rows:
    print(*row, sep=",")
print("J, return_radial_degree, return_rows, carry_p_factors")
for row in returns:
    print(*row, sep=",")
print("PASS: all exact residue identities, source costs, dimensions, and angular terms")
