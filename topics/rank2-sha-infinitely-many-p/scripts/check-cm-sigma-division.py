#!/usr/bin/env python3
"""Exact certificates for the two CM sigma division functions.

Uses SymPy over Q(i). No p-adic approximation, analytic approximation,
or elliptic-curve database is involved.
"""

import sympy as s


x = s.symbols("x")
i = s.I
beta5 = 2 + i
beta13 = 3 + 2 * i
psi5 = beta5 * x**2 - 17 * i
psi13 = (
    beta13 * x**6
    + (119 - 68 * i) * x**4
    + (-3179 + 2890 * i) * x**2
    + 4913
)

# First certificate: the sigma differential equation and Laurent coefficients.
f1, f2, f3 = -s.Rational(17, 60), -s.Rational(289, 4200), -s.Rational(4913, 321750)
u, v, w = s.Rational(34, 5), s.Rational(289, 15), s.Rational(9826, 325)
assert s.expand(beta5 * (f1 * (beta5**4 - 5) - u)) == -17 * i

r1, r2, r3 = [
    s.expand(f * (beta13 ** (4 * j) - 13))
    for j, f in enumerate((f1, f2, f3), start=1)
]
B = s.expand(beta13 * r1 - 3 * beta13 * u)
C = s.expand(beta13 * (r2 + r1**2 / 2) - 3 * beta13 * (u**2 + v) - 2 * B * u)
A = s.expand(
    beta13 * (r3 + r1 * r2 + r1**3 / 6)
    - beta13 * (u**3 + 6 * u * v + 3 * w)
    - B * (u**2 + 2 * v)
    - C * u
)
assert (B, C, A) == (119 - 68 * i, -3179 + 2890 * i, 4913)

# Second certificate: the group law identifies the entire nonzero kernels.
y_squared = x**3 - 17 * x
x2 = (x**2 + 17) ** 2 / (4 * x * (x**2 - 17))
y2_over_y = s.cancel(-1 + (3 * x**2 - 17) * (x - x2) / (2 * y_squared))
usual_psi3 = 3 * x**4 - 102 * x**2 - 289
quartic_factor = x**6 - 85 * x**4 - 1445 * x**2 + 4913
x3 = x - 8 * y_squared * quartic_factor / usual_psi3**2
y3_over_y = s.cancel(
    -1 + (y2_over_y - 1) * (x - x3) / (x2 - x)
)


def check_zero_on_kernel(rational_function, kernel_polynomial):
    numerator, denominator = s.cancel(rational_function).as_numer_denom()
    assert s.rem(numerator, kernel_polynomial, x, extension=i) == 0
    assert s.degree(s.gcd(denominator, kernel_polynomial, x, extension=i), x) == 0


for psi in (psi5, psi13):
    assert s.degree(s.gcd(psi, s.diff(psi, x), x, extension=i), x) == 0
    assert s.degree(s.gcd(psi, y_squared, x, extension=i), x) == 0

# [2]R = -[i]R on psi5 = 0.
check_zero_on_kernel(x2 + x, psi5)
check_zero_on_kernel(y2_over_y + i, psi5)

# [3]R = -[2i]R on psi13 = 0.
check_zero_on_kernel(x3 + x2, psi13)
check_zero_on_kernel(y3_over_y + i * y2_over_y, psi13)

print("Psi_(2+i) =", s.expand(psi5))
print("Psi_(3+2i) =", s.expand(psi13))
print("Passed: exact Laurent coefficients, squarefree kernels, and CM group-law identities.")
