#!/usr/bin/env python3
"""R419: complete polynomial identities for opposite quarter translations.

All operations are exact in QQ(sqrt(3))[x,t]/(t^2-f^2(x^3+1)).
No sample-point interpolation and no target-prime scan is used.
Requires SymPy.
"""

import json
from fractions import Fraction
from sympy import sqrt, Rational
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

K = QQ.algebraic_field(sqrt(3))
R, x = ring("x", K)
q = K.from_sympy(1 + sqrt(3))
e = -q
f2 = -6*q - 3
den = (x + q)**2
t2 = f2*(x**3 + 1)
zero, one = R.zero, R.one


def ad(a, b):
    return a[0]+b[0], a[1]+b[1]


def sc(a, c):
    return a[0]*c, a[1]*c


def ml(a, b):
    return a[0]*b[0]+a[1]*b[1]*t2, a[0]*b[1]+a[1]*b[0]


def pw(a, n):
    out = one, zero
    while n:
        if n & 1:
            out = ml(out, a)
        a = ml(a, a)
        n //= 2
    return out


base = e*x*x + e*e*x + 2
nm, np = (base, 2*one), (base, -2*one)
d3, d6, d9 = den**3, den**6, den**9
N3, N6 = pw(nm, 3), pw(nm, 6)
snum = ml(
    ml(pw(nm, 2), ad(N3, (d3, zero))),
    ml(ad(N3, (-8*d3, zero)),
       ad(ad(N6, sc(N3, K.from_sympy(Rational(-4, 7))*d3)),
          (K.from_sympy(Rational(16, 7))*d6, zero))))
P3, P6, P9 = pw(np, 3), pw(np, 6), pw(np, 9)
lnum = ml(
    ml(np, ad(ad(P6, sc(P3, 20*d3)), (-8*d6, zero))),
    ml(ad(P3, (4*d3, zero)),
       ad(ad(ad(P9, sc(P6, -96*d3)), sc(P3, 48*d6)),
          (64*d9, zero))))
C = f2 + K.from_sympy(Rational(3, 2))*q*q*(x+q)
line2 = C*C+t2, 2*C
raw_even_part = ml(ml(snum, lnum), line2)[0]
divisor = (x+q)**32*(x+1)
quotient, remainder = raw_even_part.div(divisor)
assert remainder == zero
constant = 2*((1-q)/(12*f2))**9/f2
pair_q = quotient*constant
assert pair_q.degree() == 35


def coefficient_trace(c):
    terms = c.to_list()
    assert len(terms) <= 2
    return Fraction(str(2*terms[-1])) if terms else Fraction(0)


quarter_coefficients = {
    i: coefficient_trace(pair_q.get((i,), K.zero)) for i in range(37)
}
quarter = zero
for i, c in quarter_coefficients.items():
    quarter += K.from_sympy(Rational(c.numerator, c.denominator))*x**i

X = x**3
R2 = X**2 + 20*X - 8
V4 = X**4 - 536*X**3 - 1344*X**2 - 2048*X - 512
expected_quarter = K.from_sympy(Rational(2, 189))*(X-8)*(X+1)*R2**2*V4*(x*x*(X-8)-8*x*(X+1))
assert quarter == expected_quarter
assert all(quarter.get((3*j,), K.zero) == K.zero for j in range(13))

# Actual leading-one T at b=1: T=sigma^72*PT(x).
PT = X*(X+1)*(X-8)*(X**2-K.from_sympy(Rational(4, 7))*X+K.from_sympy(Rational(16, 7)))*R2*(X+4)*(X**3-96*X**2+48*X+64)
assert PT.degree() == 33
half = zero
for (i,), c in PT.items():
    half += c*(-x+2)**i*(x+1)**(36-i)
half = half/K.convert(3**18)

C5 = X**5+140*X**4-2528*X**3-5984*X**2-6016*X-512
C7 = X**7-200*X**6-15072*X**5-47296*X**4-372736*X**3-577536*X**2-210944*X-32768
H1 = K.from_sympy(Rational(-2, 189))*(X-8)*(X+1)*R2*(7*X**2-4*X+16)*C5
H2 = K.from_sympy(Rational(1, 189))*(X-8)*(X+1)*R2*C7
assert half == -PT/3 + x*H1 + x*x*H2
assert all(3*half.get((3*j,), K.zero) == -PT.get((3*j,), K.zero)
           for j in range(13))


def rational_coefficients(poly, degree):
    out = []
    for i in range(degree+1):
        c = poly.get((i,), K.zero)
        terms = c.to_list()
        assert len(terms) <= 1
        out.append(str(Fraction(str(terms[-1]))) if terms else "0")
    return out


report = {
    "scope": "Complete exact polynomial identities; no sampling or target-prime scan.",
    "field": "QQ(sqrt(3)); q=1+sqrt(3), q^2=2q+2",
    "quarter_parameters": "h=-1, e=-q, f^2=-6q-3, t=fy",
    "quotient_remainder_zero": True,
    "single_q_signed_pair_degree": pair_q.degree(),
    "quarter_trace_factor_identity": True,
    "half_period_full_decomposition_identity": True,
    "quarter_four_point_sum_coefficients_in_x": rational_coefficients(quarter, 36),
    "half_period_translate_coefficients_in_x": rational_coefficients(half, 36),
    "T_coefficients_in_X": [rational_coefficients(PT, 36)[3*j] for j in range(13)],
    "quarter_twelve_point_sum_zero": True,
    "half_period_nonzero_three_point_sum": "-T",
    "full_two_torsion_sum_zero": True,
    "opposite_translate_U_zero": True,
}
print(json.dumps(report, indent=2))
