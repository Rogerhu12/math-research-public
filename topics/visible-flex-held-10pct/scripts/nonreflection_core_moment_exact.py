#!/usr/bin/env python3
"""Exact finite Laurent convolution for R17. Requires SymPy."""
import itertools
import sympy as sp

q, epsilon = sp.symbols("q epsilon", real=True)
h = {0: sp.Integer(1), 2: q / 2, -2: q / 2,
     4: -sp.I * epsilon / 2, -4: sp.I * epsilon / 2}
ac_over_pi = sp.expand(sum(
    sp.Rational(1, 2) * (1-a) * (1-b) * (1-d*d)
    * h[a] * h[b] * h[c] * h[d]
    for a, b, c, d in itertools.product(h, repeat=4)
    if a+b+c+d == -2))
real = q * (1-sp.Rational(9, 4)*q*q-sp.Rational(45, 2)*epsilon*epsilon)
imag = epsilon*q*(75*epsilon*epsilon+42*q*q-20)/8
assert sp.simplify(sp.re(ac_over_pi)-real) == 0
assert sp.simplify(sp.im(ac_over_pi)-imag) == 0
parameters = {q: sp.Rational(1, 5), epsilon: sp.Rational(1, 200)}
rho_lower = (1-3*q-15*epsilon).subs(parameters)
real_over_pi = real.subs(parameters)
assert rho_lower == sp.Rational(13, 40)
assert real_over_pi == sp.Rational(14551, 80000)
assert real_over_pi*3 == sp.Rational(43653, 80000)
print("Re AC/pi =", sp.factor(real))
print("Im AC/pi =", sp.factor(imag))
print("Both exact symbolic differences are zero.")
print("rho >=", rho_lower, "; Re AC/pi =", real_over_pi)
print("Using pi > 3: Re AC >", real_over_pi*3)
