#!/usr/bin/env python3
"""Exact algebraic checks for R456, without a target-prime search.

The cube is multiplied first in the actual divided-power relation
    w**s = p*epsilon, epsilon**3 = 0,
and only then read in the three integral blocks.  This independently checks
the two first-lift coefficients 6 and 1 and the strict boundary rows.
"""
from fractions import Fraction
import sympy as sp


def ceil_div(a, b):
    return (a + b - 1) // b


def e_bound(m):
    return (3*ceil_div(3*m, 4) + 2*ceil_div(m, 2)
            + ceil_div(2*m, 3) - 2)


for n in range(24):
    A, B, C = (n+1)//4, (n+1)//3, n//2
    fn = (9*n)//2 + 4
    assert 3*A+B-C+e_bound(n+1) == fn
    for j in range(17):
        actual_t_degree = n-C+3*A+B+5*j+e_bound(n+1)+6*j
        assert actual_t_degree == (11*n)//2+4+11*j
        # The exact lower bound for the nonzero-j Frobenius kernel.
        if j:
            p = sp.Symbol('p')
            mu_lower = 4*p-3*A-B-4*j
            allowed = e_bound(n+1)+6*j
            assert sp.expand(mu_lower-allowed-(4*p-fn-C-10*j)) == 0
assert Fraction(26*83, 9)-160 > 0

w, ep, pi, a = sp.symbols('w ep pi a')


def trunc_w(expr, bound):
    return sp.Add(*(coef*w**power[0]
                    for power, coef in sp.Poly(sp.expand(expr), w).terms()
                    if power[0] < bound))


def divided_blocks_mod_p2(expr, s, ell):
    """Keep coefficients of 1 and pi in each actual epsilon block."""
    out = [[sp.Integer(0), sp.Integer(0)] for _ in range(3)]
    for (rw, re, rp), coef in sp.Poly(sp.expand(expr), w, ep, pi).terms():
        carry, residue = divmod(rw, s)
        block, vp = re+carry, rp+carry
        if block >= 3 or vp >= 2:
            continue
        if block == 2 and residue >= ell:
            continue
        out[block][vp] += coef*w**residue
    return [[sp.expand(v) for v in row] for row in out]


# Finite formal-window checks; the letter pi is an indeterminate, not a
# selected target prime.  Include both equality boundaries excluded by the
# theorem, and the ell=1 escape when s is odd.
windows = [(4, 2, 1), (5, 3, 2), (5, 3, 1),
           (6, 4, 3), (8, 5, 3), (9, 5, 2)]
for s, h, ell in windows:
    assert 1 <= ell <= h < s and 2*h >= s
    xis = sp.symbols(f'xi0:{h}')
    xi = sum(xis[i]*w**i for i in range(h))
    u = 1+2*w+3*w*w
    first = 2+3*w+w*w
    second = 3+4*w
    f = w**h*u+pi*xi
    physical_root = f+a*ep*first+a*a*ep*ep*second/2
    blocks = divided_blocks_mod_p2(physical_root**3, s, ell)
    assert all(sp.expand(row[0]) == 0 for row in blocks)
    assert blocks[0][1] == 0
    k = 2*h-s
    want1 = trunc_w(w**h*u*(6*a*xi*first+w**k*u*u), s)
    want2 = trunc_w(3*a*first*(a*xi*first+w**k*u*u), ell)
    assert sp.expand(blocks[1][1]-want1) == 0
    assert sp.expand(blocks[2][1]-want2) == 0

# The two normalized rows have one and the same correction variable.
zeta, leading = sp.symbols('zeta leading')
row1 = 6*a*zeta+leading
row2 = a*zeta+leading
assert sp.expand(row1-6*row2) == -5*leading

# Exact visibility of the two leading rows for minimal cubic contact.
for s in range(15, 150):
    h = (s+1)//2
    k = 2*h-s
    for ell in range(1, h+1):
        visible = k < min(s-h, ell)
        assert visible == (s % 2 == 0 or ell >= 2)

print('PASS: full source bidegrees and sharpened Frobenius-kernel bound')
print('PASS: cube multiplication in w^s=pi*epsilon, including both carries')
print('PASS: normalized first-lift rows differ by the nonzero factor 5')
print('PASS: strict row boundaries and the odd-s, ell=1 escape')
