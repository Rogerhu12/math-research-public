#!/usr/bin/env python3
"""Exact arithmetic checks for R36; the CLS critical value 6 is cited input."""

from fractions import Fraction


def add_rational(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and y == -v:
        return None
    slope = (v - y) / (u - x) if x != u else (3 * x * x - 17) / (2 * y)
    xx = slope * slope - x - u
    return xx, slope * (x - xx) - y


def multiple(n, P, add):
    result = None
    while n:
        if n & 1:
            result = add(result, P)
        P = add(P, P)
        n //= 2
    return result


def valuation(n, p):
    assert n != 0
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def finite_points(ell):
    return [None] + [
        (x, y)
        for x in range(ell)
        for y in range(ell)
        if (y * y - x * x * x + 17 * x) % ell == 0
    ]


def finite_add(ell):
    def add(P, Q):
        if P is None:
            return Q
        if Q is None:
            return P
        x, y = P
        u, v = Q
        if x == u and (y + v) % ell == 0:
            return None
        if x == u:
            slope = (3 * x * x - 17) * pow(2 * y, -1, ell) % ell
        else:
            slope = (v - y) * pow(u - x, -1, ell) % ell
        xx = (slope * slope - x - u) % ell
        return xx, (slope * (x - xx) - y) % ell

    return add


p = 13
N = len(finite_points(p))
assert N == 20
print("#E(F_13) =", N)

for P in ((-1, 4), (9, 24)):
    point = tuple(Fraction(a) for a in P)
    x, y = multiple(N, point, add_rational)
    t = -x / y
    vp = valuation(t.numerator, p) - valuation(t.denominator, p)
    assert vp == 1
    t_over_p = (t.numerator // p) * pow(t.denominator, -1, p) % p
    log_over_p = t_over_p * pow(N, -1, p) % p
    assert t_over_p == 7 and log_over_p == 1
    print(P, ": v_13(t([20]P)) =", vp,
          "; t([20]P)/13 mod 13 =", t_over_p,
          "; log(P)/13 mod 13 =", log_over_p)

ell, ii = 109, 76
assert (ii * ii + 1) % ell == 0
add = finite_add(ell)
points = finite_points(ell)
assert len(points) == 130


def neg(P):
    return None if P is None else (P[0], -P[1] % ell)


def cm_i(P):
    return None if P is None else (-P[0] % ell, ii * P[1] % ell)


def pi(P):
    return add(neg(multiple(3, P, add)), multiple(2, cm_i(P), add))


kernel = {P for P in points if pi(P) is None}
image = {pi(P) for P in points}
assert len(kernel) == 13 and len(image) == 10
P, Q = (108, 4), (9, 24)
difference = add(P, neg(Q))
assert difference == (26, 28) and difference not in image
print("q = (109, i-76): #E =", len(points),
      "; #ker(pi) =", len(kernel), "; #image(pi) =", len(image))
print("pi kernel affine points:", sorted(x for x in kernel if x is not None))
print("pi image affine points:", sorted(x for x in image if x is not None))
print("P-Q =", difference, "; not in image(pi)")

# Published input: CLS II, corrected Table I, D=17, p=13.
critical_value_over_p_squared = 6
i_at_p = 8
f = 34 * (1 + i_at_p) % p
A = (p + 1 - N) % p
factorial = 1
for j in range(1, p):
    factorial = factorial * j % p
raw_moment = (-2 * pow(f, p, p) * factorial
              * critical_value_over_p_squared) % p
cw = (1 - A) % p
G_center = raw_moment * pow(cw, -1, p) % p
rs_unit = -pow(1 + i_at_p, -1, p) % p
value = rs_unit * G_center % p
assert (f, A, raw_moment, cw, G_center, rs_unit, value) == (7, 7, 6, 7, 12, 10, 3)
print("Using the cited CLS input 6:",
      "raw moment/p^2 =", raw_moment, "; CW_13 =", cw,
      "; G(13) =", G_center, "; RS unit =", rs_unit,
      "; derived value =", value, "mod 13")
