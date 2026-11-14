#!/usr/bin/env python3
"""Exact outward dyadic certificate for one explicit closed curve seed.

This checks a derivative sign and one integral only.  It does not solve any
surface PDE, generate a mesh, or certify a closed flexible surface.  All
arithmetic is Python integer/Fraction arithmetic; no floating point is used.
"""
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from math import factorial, isqrt
from datetime import datetime, timezone
import argparse
import json


BITS = 128
SCALE = 1 << BITS
TERMS = 24
BOXES = 1024


def ceildiv(a, b):
    assert b > 0
    return -((-a) // b)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def q(n, d=1):
        f = Fraction(n, d)
        return I((f.numerator * SCALE) // f.denominator,
                 ceildiv(f.numerator * SCALE, f.denominator))

    def __add__(self, other):
        return I(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        p = [self.lo * other.lo, self.lo * other.hi,
             self.hi * other.lo, self.hi * other.hi]
        return I(min(p) // SCALE, ceildiv(max(p), SCALE))

    def __truediv__(self, other):
        assert other.lo > 0, "division requires a strictly positive interval"
        reciprocal = I((SCALE * SCALE) // other.hi,
                       ceildiv(SCALE * SCALE, other.lo))
        return self * reciprocal

    def sqrt(self):
        assert self.lo >= 0
        low = isqrt(self.lo * SCALE)
        high_square = self.hi * SCALE
        high = isqrt(high_square)
        if high * high != high_square:
            high += 1
        return I(low, high)

    def bounds(self):
        return [str(Fraction(self.lo, SCALE)),
                str(Fraction(self.hi, SCALE))]


ZERO, ONE, TWO = I.q(0), I.q(1), I.q(2)


def arctan_bounds(q, count):
    # Alternating series with its exact first omitted term.
    value = sum((Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1))
                 for k in range(count)), Fraction(0))
    nxt = Fraction((-1) ** count, (2 * count + 1) * q ** (2 * count + 1))
    return min(value, value + nxt), max(value, value + nxt)


def pi_interval():
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    # tan(4 atan(1/5)) = 120/119, and subtracting atan(1/239)
    # gives tangent 1; the difference lies in (0, pi/2).
    a0, a1 = arctan_bounds(5, 40)
    b0, b1 = arctan_bounds(239, 12)
    low, high = 16 * a0 - 4 * b1, 16 * a1 - 4 * b0
    assert Fraction(3) < low < high < Fraction(22, 7)
    return I((low.numerator * SCALE) // low.denominator,
             ceildiv(high.numerator * SCALE, high.denominator))


def even_taylor(x, kind):
    assert max(abs(x.lo), abs(x.hi)) <= 6 * SCALE
    xx = x * x
    coeff = [I.q((-1) ** k, factorial(2 * k + (1 if kind == "sinc" else 0)))
             for k in range(TERMS + 1)]
    result = coeff[-1]
    for value in reversed(coeff[:-1]):
        result = result * xx + value
    # Taylor's theorem, or integral sinc(x)=int_0^1 cos(tx)dt.
    degree = 2 * TERMS + 2
    error = Fraction(6 ** degree,
                     factorial(degree + (1 if kind == "sinc" else 0)))
    radius = ceildiv(error.numerator * SCALE, error.denominator)
    return I(result.lo - radius, result.hi + radius)


def cos(x):
    return even_taylor(x, "cos")


def sinc(x):
    return even_taylor(x, "sinc")


def sin(x):
    return x * sinc(x)


def values(t):
    st, ct = sin(t), cos(t)
    twice = TWO * t
    theta = twice + I.q(13, 6) * sin(twice)
    theta_p = TWO + I.q(13, 3) * cos(twice)
    rho2 = ONE - I.q(24, 25) * ct * ct
    assert rho2.lo > 0
    rho = rho2.sqrt()
    sth, cth = sin(theta), cos(theta)
    # This expression is regular at t=0 and equals
    # rho*gamma_y,t/(a*sin(t)) for 0<t<=pi/2.
    theta_over_t = TWO + I.q(13, 3) * sinc(twice)
    f = cth - ct * rho2 * theta_p * theta_over_t * sinc(theta) / sinc(t)
    a = I.q(24, 25).sqrt()
    vx = -a * (st / rho * sth + ct * rho * theta_p * cth)
    vy = a * (st / rho * cth - ct * rho * theta_p * sth)
    return f, vx, vy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    started = datetime.now(timezone.utc).isoformat()
    pi = pi_interval()
    half_pi = pi * I.q(1, 2)
    integral_x, integral_y = ZERO, ZERO
    largest_f_upper = -10 * SCALE
    for j in range(BOXES):
        x_box = I((j * SCALE) // BOXES,
                  ceildiv((j + 1) * SCALE, BOXES))
        t = half_pi * x_box
        f, vx, vy = values(t)
        assert f.hi < 0, f"derivative sign not certified in box {j}"
        largest_f_upper = max(largest_f_upper, f.hi)
        integral_x = integral_x + vx * half_pi * I.q(1, BOXES)
        integral_y = integral_y + vy * half_pi * I.q(1, BOXES)
    assert integral_x.lo > SCALE // 2
    assert integral_y.hi < -SCALE
    source = Path(__file__).read_bytes()
    report = {
        "status": "PASS_EXACT_OUTWARD_DYADIC_CURVE_SEED_ONLY",
        "started_utc": started,
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": sha256(source).hexdigest(),
        "arithmetic": "outward integer dyadic intervals and Fraction; no floating point",
        "bits": BITS, "taylor_terms_plus_constant": TERMS + 1,
        "normalized_parameter_boxes": BOXES,
        "pi_bounds": pi.bounds(),
        "largest_f_upper": str(Fraction(largest_f_upper, SCALE)),
        "gamma_x_pi_over_2_bounds": integral_x.bounds(),
        "gamma_y_pi_over_2_bounds": integral_y.bounds(),
        "strict_gates": "f<0 on [0,pi/2]; X>1/2; Y<-1",
        "scope": "Explicit closed curve derivative/integral only; no surface or cap solution."
    }
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(report["status"])
    print("report_bytes=" + str(args.report.stat().st_size))
    print("report_sha256=" + sha256(args.report.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
