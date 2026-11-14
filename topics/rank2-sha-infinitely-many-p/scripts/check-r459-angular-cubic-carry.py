#!/usr/bin/env python3
"""Exact R459 source/three-block checks; no target-prime scan.

In particular H is NOT divided by w**r.  Its three Gaussian jets are kept
independent while the true products are reduced by w**s=pi*epsilon.
"""
import sympy as sp


def ceil_div(a, b):
    return (a+b-1)//b


def eb(m):
    return 3*ceil_div(3*m, 4)+2*ceil_div(m, 2)+ceil_div(2*m, 3)-2


def A(n):
    return (n+1)//4


def angle_layer(D, J, r, enlarged=True):
    return [(n, j) for n in range(D+1) for j in range(J+1)
            if A(n)+j <= r <= A(n)+j+eb(n+1)+(6*j if enlarged else 0)]


assert angle_layer(12, 16, 0) == [(0, 0), (1, 0), (2, 0)]
assert sorted(angle_layer(12, 16, 1)) == sorted(
    [(n, 0) for n in range(7)]+[(n, 1) for n in range(3)])
assert sp.Matrix([[1, 1, 1], [0, 1, 2], [0, 1, 4]]).det() == 2

t, radial = sp.symbols('t radial')
d, h7 = 1+8*t, 7+4*t+16*t*t
source = sp.Poly(t*(t-1)*h7*(radial-1)**3, radial)
for n in range(4):
    qn = ((t*h7)**A(n)*(t-1)**((n+1)//3)
          / d**(n//2))
    quotient = sp.cancel(source.coeff_monomial(radial**n)/qn)
    assert sp.denom(quotient) == 1
    assert sp.Poly(quotient, t).degree() <= eb(n+1)

w, ep, pi, a = sp.symbols('w ep pi a')


def trunc(expr, bound):
    return sp.Add(*(c*w**pw[0]
                    for pw, c in sp.Poly(sp.expand(expr), w).terms()
                    if pw[0] < bound))


def divided_blocks(expr, s, ell):
    out = [[sp.Integer(0), sp.Integer(0)] for _ in range(3)]
    for (rw, re, rp), coef in sp.Poly(sp.expand(expr), w, ep, pi).terms():
        carry, residue = divmod(rw, s)
        block, vp = re+carry, rp+carry
        if block >= 3 or vp >= 2:
            continue
        if block == 2 and residue >= ell:
            continue
        out[block][vp] += coef*w**residue
    return [[sp.expand(x) for x in row] for row in out]


# Formal windows including h<ell, 2h<s and the padded equality r+2h=s.
windows = [(7, 1, 3, 1), (8, 1, 4, 2), (10, 2, 4, 2),
           (10, 3, 4, 2), (11, 3, 5, 3), (11, 3, 5, 6)]
for s, r, h, ell in windows:
    k = 2*h+r-s
    assert r >= 1 and r+2*h >= s and r+h >= ell
    assert 0 <= k < min(s-h, ell, h)
    xis = sp.symbols(f'xi0:{h}')
    hs = sp.symbols(f'H0:{k+2}')
    js = sp.symbols(f'Hprime0:{k+2}')
    ks = sp.symbols(f'Hsecond0:{k+2}')
    xi = sum(xis[i]*w**i for i in range(h))
    H = sum(hs[i]*w**i for i in range(k+2))
    EH = sum(js[i]*w**i for i in range(k+2))
    E2H = sum(ks[i]*w**i for i in range(k+2))
    u, e, e2, C = 2+3*w+w*w, 3+4*w, 5+w, 3+7*w
    f = w**h*u+pi*xi
    root_phys = f+a*ep*e+a*a*ep*ep*e2/2
    H_phys = H+a*ep*EH+a*a*ep*ep*E2H/2
    # First solve for completely arbitrary R_1,R_2, without putting R in
    # the F^2 ideal.  These are the actual first-lift forcing rows.
    base_blocks = divided_blocks(w**r*C*root_phys**3, s, ell)
    assert base_blocks[0][1] == 0
    required_R1 = -base_blocks[1][1]/a
    required_R2 = -2*base_blocks[2][1]/(a*a)
    inv_e = sp.series(1/e, w, 0, 2*h+k+1).removeO()
    normal_derivative = trunc(
        required_R1-w**h*u*inv_e*required_R2, h+k+1)
    assert trunc(normal_derivative, h+k) == 0
    assert sp.expand(normal_derivative).coeff(w, h+k) == 120/a
    if 2*h+k < s:
        assert r > 2*k
        normal_value = trunc(-w**h*u*inv_e*required_R1
                             +w**(2*h)*u*u*inv_e*inv_e*required_R2/2,
                             2*h+k+1)
        assert trunc(normal_value, 2*h+k) == 0
        assert sp.expand(normal_value).coeff(w, 2*h+k) == -32/a

    actual = w**r*C*root_phys**3+pi*root_phys**2*H_phys
    blocks = divided_blocks(actual, s, ell)
    assert all(row[0] == 0 for row in blocks)
    assert sp.expand(blocks[0][1]-trunc(w**(2*h)*u*u*H, s)) == 0

    zeta = H+3*w**r*C*xi
    predicted1 = w**h*u*(2*a*e*zeta+w**k*C*u*u)
    predicted2 = a*e*(a*e*zeta+3*w**k*C*u*u)
    assert sp.expand(trunc(blocks[1][1]-predicted1, h+k+1)) == 0
    assert sp.expand(trunc(blocks[2][1]-predicted2, k+1)) == 0

    # Normalize only actual units and read only rows that exist.
    inv_u = sp.series(1/u, w, 0, k+1).removeO()
    inv_ae = sp.series(1/(a*e), w, 0, k+1).removeO()
    first_row = trunc(sp.cancel(blocks[1][1]/w**h)*inv_u, k+1)
    second_row = trunc(blocks[2][1]*inv_ae, k+1)
    difference = trunc(first_row-2*second_row, k+1)
    assert sp.expand(difference+5*w**k*C*u*u).coeff(w, k) == 0
    assert trunc(difference, k) == 0
    assert sp.expand(difference).coeff(w, k) == -60

for s in range(15, 120):
    for r in range(1, s-2):
        h = (s-r+1)//2
        if h < 2:
            continue
        k = 2*h+r-s
        for ell in range(1, min(s-13, r+h)+1):
            visible = k < min(s-h, ell, h)
            assert visible == ((s-r) % 2 == 0 or ell >= 2)

print('PASS: exact angular charge layers and mandatory t content')
print('PASS: explicit padded cubic is a genuine W_(3,0) source')
print('PASS: unrestricted first-lift normal derivative has unit coefficient 5')
print('PASS: normal value has unit coefficient -2 only when 2h+k<s')
print('PASS: actual p F^2 H correction retains all Gaussian jets')
print('PASS: two integral carry rows give the unit factor 5 without dividing t^r')
print('PASS: padded minimal-contact boundary and ell=1 escape')
