#!/usr/bin/env python3
"""Exact finite arithmetic in R118 and the two-row theta comparison.

The rank proof and infinite descent are in the associated note.  This
certificate checks their stated points, isogeny formulas, finite counts,
and the complete polynomial identity used in the convolution comparison.
"""
from fractions import Fraction as F
import sympy as s

x, y, X, v = s.symbols("x y X v")
xp = x + 289 / x
yp = y * (1 - 289 / x**2)
assert s.cancel((yp**2 - xp**3 + 1156*xp).subs(y**2, x**3+289*x)) == 0
xback = (xp - 1156/xp) / 4
xdouble = (3*x**2+289)**2 / (4*(x**3+289*x)) - 2*x
assert s.cancel(xback-xdouble) == 0
yback = yp * (1+1156/xp**2) / 8
ydouble = (3*x**2+289) / (2*y) * (x-xdouble) - y
numerator, _ = s.fraction(s.cancel((yback-ydouble)*y))
assert s.expand(numerator.subs(y**2, x**3+289*x)) == 0

phi = lambda a,b: (a+289/a, b*(1-289/a**2))
hatphi = lambda a,b: ((a-1156/a)/4, b*(1+1156/a**2)/8)
P, Q = (F(68), F(578)), (F(144), F(1740))
R, S = (F(-2), F(48)), (F(34), F(0))
for a,b in (P,Q):
    assert b*b == a*a*a+289*a
for a,b in (R,S):
    assert b*b == a*a*a-1156*a
assert hatphi(*R) == Q
assert hatphi(*S) == (0,0)
assert phi(*P) == (F(289,4), F(4335,8))
assert phi(*Q) == (F(21025,144), F(2964815,1728))
for b in (289,-1156):
    for q, expected in ((3,4),(5,8)):
        count = 1+sum((a*a*a+b*a-c*c) % q == 0
                      for a in range(q) for c in range(q))
        assert count == expected

f = 5*X**2-2*X+1
q8 = X**8+364*X**6-1088*X**5+1190*X**4-1088*X**3+364*X**2+1
h1 = X**4+4*X**3+70*X**2+4*X+1
h2 = X**4+20*X**3-26*X**2+20*X+1
d = 16*X*(X-1)**2
g = 5*(X+1)**12+3*(X+1)**8*d-(X+1)**4*d**2+d**3
assert s.expand(g-(X**2-2*X+5)*f*h1*h2) == 0
mult = (X+1)*q8 / ((X-1)*h1*h2)
assert s.cancel(mult.subs(X,1/X)+mult) == 0
assert s.series(mult.subs(X,1/v),v,0,4).removeO() == 1-22*v+770*v**2-17430*v**3
assert 16*F(97,60)-22 == F(58,15)
assert 4624*68//34 == 9248
assert F(4624,4)*F(1,2)*F(16,17)**2 == 512
print("PASS: isogeny/composition, points, finite counts, theta multiplier, scales")
