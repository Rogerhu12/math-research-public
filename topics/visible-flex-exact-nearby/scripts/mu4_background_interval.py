#!/usr/bin/env python3
"""Exact integer/dyadic enclosure of the undeformed mu=4sqrt(2) background.

All validation arithmetic is integer arithmetic with directed dyadic rounding.
The printed decimal approximations are display only. No external ODE solver.
"""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

BITS = 160
SCALE = 1 << BITS


def ceil_div(a, b):
    return -((-a)//b)


class I:
    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = int(lo), int(hi if hi is not None else lo)
        else:
            self.lo = self.hi = int(lo)*SCALE
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def rational(n, d=1):
        return I((n*SCALE)//d, ceil_div(n*SCALE, d), raw=True)

    @staticmethod
    def hull(lo, hi):
        return I(lo, hi, raw=True)

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo+other.lo, self.hi+other.hi, raw=True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, raw=True)

    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -I(other))

    def __rsub__(self, other):
        return I(other)-self

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = [self.lo*other.lo, self.lo*other.hi,
                self.hi*other.lo, self.hi*other.hi]
        return I(min(vals)//SCALE, ceil_div(max(vals), SCALE), raw=True)

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return I((SCALE*SCALE)//self.hi,
                 ceil_div(SCALE*SCALE, self.lo), raw=True)

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        return self*other.reciprocal()

    def square(self):
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo*self.lo, self.hi*self.hi)
        high = max(self.lo*self.lo, self.hi*self.hi)
        return I(low//SCALE, ceil_div(high, SCALE), raw=True)

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("negative square root")
        low = math.isqrt(self.lo*SCALE)
        high = math.isqrt(self.hi*SCALE)
        if high*high < self.hi*SCALE:
            high += 1
        return I(low, high, raw=True)

    def intersect(self, other):
        return I(max(self.lo, other.lo), min(self.hi, other.hi), raw=True)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def lower_gt(self, n, d=1):
        return self.lo*d > n*SCALE

    def upper_lt(self, n, d=1):
        return self.hi*d < n*SCALE


SQRT2 = I(2).sqrt()
STRENGTH = I(32)+SQRT2


def exp_nonnegative(x):
    if x.lo < 0 or x.hi > 4*SCALE:
        raise ValueError("exponential outside declared range")
    term = total = I(1)
    for k in range(1, 65):
        term = term*x/I(k)
        total = total+term
    following = term*x/I(65)
    ratio = I(x.hi, raw=True)/I(66)
    remainder = following/(I(1)-ratio)
    return total + I(0, remainder.hi, raw=True)


def profile(j, divisions):
    """Q and Q' ingredients at the exact rational point x=j/divisions."""
    x = I.rational(j, divisions)
    e = exp_nonnegative(2*x)
    sech2 = 4*e/(e+1).square()
    tanh = (e-1)/(e+1)
    return I(32)-STRENGTH*sech2, sech2, tanh


def exact_record(a):
    return dict(lower=f"{a.lo}/{SCALE}", upper=f"{a.hi}/{SCALE}",
                lower_decimal_display=a.lo/SCALE,
                upper_decimal_display=a.hi/SCALE)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--divisions", type=int, default=400)
    ap.add_argument("--out", type=Path, default=Path(
        "topics/visible-flex-exact-nearby/notes/2026-11-10-mu4-background-interval-certificate.json"))
    args = ap.parse_args()
    if args.divisions <= 0 or (3*args.divisions) % 2:
        raise ValueError("need a positive even denominator")
    count = 3*args.divisions//2
    dt = I.rational(1, args.divisions)
    tau = I(0, dt.hi, raw=True)
    points = [profile(j, args.divisions) for j in range(count+1)]
    h, v, z = I(1), I(0), I(0)
    records = {}
    for j in range(count):
        q0, s0, t0 = points[j]
        q1, s1, t1 = points[j+1]
        q = I(q0.lo, q1.hi, raw=True)  # Q is increasing on x>=0.
        sech = I(s1.lo, s0.hi, raw=True)
        tanh = I(t0.lo, t1.hi, raw=True)
        qp = 2*STRENGTH*sech*tanh
        hmax, vmax, qmax = [I(a.abs_upper(), raw=True) for a in (h, v, q)]
        habs = (hmax+dt*vmax)/(I(1)-dt.square()*qmax)
        vabs = vmax+dt*qmax*habs
        hs = h + tau*I(-vabs.hi, vabs.hi, raw=True)
        vs = v + tau*I(-(qmax*habs).hi, (qmax*habs).hi, raw=True)
        for _ in range(4):
            hs = hs.intersect(h+tau*vs)
            vs = vs.intersect(v+tau*q*hs)
        if not hs.lower_gt(0):
            raise AssertionError(f"positive h enclosure failed at cell {j}")
        zs = z+tau/hs.square()
        p = (I(1)+vs.square()).sqrt()
        kt = hs/p
        km = q*kt*kt*kt
        gauss = q*kt.square().square()
        support = (hs.reciprocal()+zs*vs)/p
        radius2 = hs.reciprocal().square()+zs.square()
        tests = {
            "radius_squared": radius2.upper_lt(529, 400),
            "parallel_curvature": kt.upper_lt(4),
            "meridian_curvature": km.abs_upper() < 4*SCALE,
            "support": support.lower_gt(4, 5),
            "gauss_upper": gauss.upper_lt(4),
        }
        if not all(tests.values()):
            raise AssertionError(json.dumps(dict(cell=j, tests=tests,
                h=exact_record(hs), v=exact_record(vs), z=exact_record(zs),
                radius2=exact_record(radius2), kt=exact_record(kt),
                km=exact_record(km), support=exact_record(support),
                gauss=exact_record(gauss))))
        quantities = {
            "radius_squared_upper": (radius2.hi, "upper"),
            "parallel_curvature_upper": (kt.hi, "upper"),
            "meridian_curvature_abs_upper": (km.abs_upper(), "upper"),
            "support_lower": (support.lo, "lower"),
            "gauss_upper": (gauss.hi, "upper"),
            "h_lower": (hs.lo, "lower"),
        }
        for name, (value, direction) in quantities.items():
            if (name not in records or
                (direction == "upper" and value > records[name]["numerator"]) or
                (direction == "lower" and value < records[name]["numerator"])):
                records[name] = dict(numerator=value, denominator=SCALE,
                                     cell=j, direction=direction,
                                     decimal_display=value/SCALE)
        # h'''=Q'h+Qv, v''=Q'h+Qv, z''=-2v/h^3.
        third = qp*hs+q*vs
        hnext = h+dt*v+dt.square()*q0*h/I(2)+dt.square()*dt*third/I(6)
        vnext = v+dt*q0*h+dt.square()*third/I(2)
        znext = z+dt/h.square()-dt.square()*vs/(hs.square()*hs)
        h, v, z = hnext, vnext, znext
    endpoint_tests = dict(
        h_above_26=h.lower_gt(26),
        log_slope_above_24_over_5=(v/h).lower_gt(24, 5),
        z_above_81_over_100=z.lower_gt(81, 100),
        z_below_33_over_40=z.upper_lt(33, 40),
        Q_above_25=points[-1][0].lower_gt(25),
    )
    if not all(endpoint_tests.values()):
        raise AssertionError(json.dumps(dict(tests=endpoint_tests,
            h=exact_record(h), v=exact_record(v), z=exact_record(z),
            w=exact_record(v/h), q=exact_record(points[-1][0]))))
    for record in records.values():
        record["numerator"] = str(record["numerator"])
        record["denominator"] = str(record["denominator"])
    report = dict(
        kind="exact_integer_dyadic_interval_certificate",
        background="h''=(32-(32+sqrt(2))*sech(x)^2)h; h(0)=1,h'(0)=0,z'=h^-2,z(0)=0",
        arithmetic=dict(bits=BITS, denominator=str(SCALE),
                        sqrt="integer isqrt outward rounding",
                        exp="64-term positive Taylor sum with geometric remainder",
                        ode="rigorous slab enclosure and Taylor integral remainders"),
        interval=dict(left="0", right="3/2", step=f"1/{args.divisions}",
                      cells=count),
        all_cell_assertions=True, cell_extreme_enclosures=records,
        endpoint_tests=endpoint_tests,
        endpoint=dict(h=exact_record(h), v=exact_record(v),
                      z=exact_record(z), w=exact_record(v/h),
                      Q=exact_record(points[-1][0])),
        analytic_tail="R21: Q>=25, w>=24/5, h>=26 exp((24/5)(x-3/2)), z_infty<5/6",
        theorem_bounds=dict(radius_below="23/20", diameter_below="23/10",
                            absolute_principal_curvature_below="4",
                            support_above="4/5", gauss_below="4",
                            reach_above="1/4", reach_over_diameter_above="5/46"),
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(dict(output=str(args.out), cell_extremes=records,
                          endpoint_tests=endpoint_tests), indent=2))


if __name__ == "__main__":
    main()
