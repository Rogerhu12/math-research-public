#!/usr/bin/env python3
"""Integer interval geometry for the rational-action background mu=484/89.

The only imported numerical machinery is the directed integer interval class
and certified positive Taylor exponential from mu4_background_interval.py.
All predicates use integers. Decimal JSON fields are for display only.
This certifies an undeformed background, not a finite-amplitude isometry.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from mu4_background_interval import BITS, I, SCALE, exp_nonnegative, exact_record


MU = I.rational(484, 89)
MU2 = MU.square()
STRENGTH = MU2 + MU / 4


def profile(j, divisions):
    x = I.rational(j, divisions)
    exponential = exp_nonnegative(2 * x)
    sech2 = 4 * exponential / (exponential + 1).square()
    tanh = (exponential - 1) / (exponential + 1)
    return MU2 - STRENGTH * sech2, sech2, tanh


def certify(divisions):
    if divisions <= 0 or (3 * divisions) % 2:
        raise ValueError("divisions must be a positive even integer")
    count = 3 * divisions // 2
    dt = I.rational(1, divisions)
    tau = I(0, dt.hi, raw=True)
    points = [profile(j, divisions) for j in range(count + 1)]
    h, v, z = I(1), I(0), I(0)
    records = {}
    for j in range(count):
        q0, s0, t0 = points[j]
        q1, s1, t1 = points[j + 1]
        q = I(q0.lo, q1.hi, raw=True)
        sech2 = I(s1.lo, s0.hi, raw=True)
        tanh = I(t0.lo, t1.hi, raw=True)
        qp = 2 * STRENGTH * sech2 * tanh
        hmax, vmax, qmax = (I(a.abs_upper(), raw=True) for a in (h, v, q))
        denominator = 1 - dt.square() * qmax
        if not denominator.lower_gt(0):
            raise AssertionError("slab integral bound denominator is not positive")
        habs = (hmax + dt * vmax) / denominator
        vabs = vmax + dt * qmax * habs
        hs = h + tau * I(-vabs.hi, vabs.hi, raw=True)
        vs = v + tau * I(-(qmax * habs).hi, (qmax * habs).hi, raw=True)
        for _ in range(4):
            hs = hs.intersect(h + tau * vs)
            vs = vs.intersect(v + tau * q * hs)
        if not hs.lower_gt(0):
            raise AssertionError(f"h is not certified positive in cell {j}")
        zs = z + tau / hs.square()
        normalizer = (1 + vs.square()).sqrt()
        parallel = hs / normalizer
        meridian = q * parallel * parallel * parallel
        gauss = q * parallel.square().square()
        support = (hs.reciprocal() + zs * vs) / normalizer
        radius2 = hs.reciprocal().square() + zs.square()
        tests = {
            "radius_squared_below_49_over_36": radius2.upper_lt(49, 36),
            "parallel_curvature_below_4": parallel.upper_lt(4),
            "meridian_curvature_abs_below_4": meridian.abs_upper() < 4 * SCALE,
            "support_above_4_over_5": support.lower_gt(4, 5),
            "gauss_below_4": gauss.upper_lt(4),
        }
        if not all(tests.values()):
            raise AssertionError(json.dumps({
                "cell": j, "tests": tests, "h": exact_record(hs),
                "v": exact_record(vs), "z": exact_record(zs),
                "radius_squared": exact_record(radius2),
                "parallel": exact_record(parallel),
                "meridian": exact_record(meridian),
                "support": exact_record(support), "gauss": exact_record(gauss),
            }))
        quantities = {
            "radius_squared_upper": (radius2.hi, "upper"),
            "parallel_curvature_upper": (parallel.hi, "upper"),
            "meridian_curvature_abs_upper": (meridian.abs_upper(), "upper"),
            "support_lower": (support.lo, "lower"),
            "gauss_upper": (gauss.hi, "upper"),
            "h_lower": (hs.lo, "lower"),
        }
        for name, (value, direction) in quantities.items():
            if (name not in records
                    or (direction == "upper" and value > records[name]["numerator"])
                    or (direction == "lower" and value < records[name]["numerator"])):
                records[name] = {
                    "numerator": value, "denominator": SCALE,
                    "cell": j, "direction": direction, "decimal_display": value / SCALE,
                }
        third = qp * hs + q * vs
        hnext = h + dt * v + dt.square() * q0 * h / 2 + dt.square() * dt * third / 6
        vnext = v + dt * q0 * h + dt.square() * third / 2
        znext = z + dt / h.square() - dt.square() * vs / (hs.square() * hs)
        h, v, z = hnext, vnext, znext

    endpoint_tests = {
        "h_above_20": h.lower_gt(20),
        "log_slope_above_9_over_2": (v / h).lower_gt(9, 2),
        "z_above_81_over_100": z.lower_gt(81, 100),
        "z_below_9_over_10": z.upper_lt(9, 10),
        "Q_above_22": points[-1][0].lower_gt(22),
        "mu_squared_below_30": MU2.upper_lt(30),
    }
    if not all(endpoint_tests.values()):
        raise AssertionError(json.dumps({
            "tests": endpoint_tests, "h": exact_record(h), "v": exact_record(v),
            "z": exact_record(z), "w": exact_record(v / h),
            "Q": exact_record(points[-1][0]),
        }))
    # Exact rational checks for the analytic tail, using only these endpoint gates.
    tail_tests = {
        "riccati_lower_barrier": 22 * 4 > 81,
        "height_below_91_over_100": (I.rational(9, 10) + I.rational(1, 3600)).upper_lt(91, 100),
        "radius_squared_below_49_over_36": (I.rational(1, 400) + I.rational(91, 100).square()).upper_lt(49, 36),
        "parallel_curvature_below_4": I.rational(2, 9).upper_lt(4),
        "meridian_curvature_below_4": I.rational(240, 729).upper_lt(4),
        "gauss_below_4": I.rational(480, 6561).upper_lt(4),
        "support_denominator_below_101_over_100": (1 + I.rational(1, 90).square()).upper_lt(10201, 10000),
        "support_above_4_over_5": I.rational(81, 101).lower_gt(4, 5),
    }
    if not all(tail_tests.values()):
        raise AssertionError(tail_tests)
    for item in records.values():
        item["numerator"] = str(item["numerator"])
        item["denominator"] = str(item["denominator"])
    sources = [Path(__file__), Path(__file__).with_name("mu4_background_interval.py")]
    return {
        "kind": "exact_integer_dyadic_interval_certificate",
        "status": "undeformed_background_only",
        "parameters": {"p": 11, "q": 89, "mu": "484/89", "nu": "495/89", "A": "245025/7921"},
        "background": "h''=(mu^2-(mu^2+mu/4)*sech(x)^2)h; h(0)=1,h'(0)=0,z'=h^-2,z(0)=0",
        "arithmetic": {"bits": BITS, "denominator": str(SCALE),
                       "predicates": "integer comparisons only",
                       "exp": "64-term positive Taylor sum with geometric remainder",
                       "ode": "continuous slab enclosures with Taylor integral remainders"},
        "interval": {"left": "0", "right": "3/2", "step": f"1/{divisions}", "cells": count},
        "all_cell_assertions": True, "cell_extreme_enclosures": records,
        "endpoint_tests": endpoint_tests, "tail_tests": tail_tests,
        "endpoint": {"h": exact_record(h), "v": exact_record(v), "z": exact_record(z),
                     "w": exact_record(v / h), "Q": exact_record(points[-1][0])},
        "analytic_tail": "Q>22, w>9/2, h>20 exp((9/2)(x-3/2)), z_infty<91/100",
        "theorem_bounds": {"radius_below": "7/6", "diameter_below": "7/3",
                           "absolute_principal_curvature_below": "4", "support_above": "4/5",
                           "gauss_below": "4", "reach_above": "1/4",
                           "reach_over_diameter_above": "3/28"},
        "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--divisions", type=int, default=400)
    parser.add_argument("--out", type=Path, default=Path(
        "topics/visible-flex-exact-nearby/notes/2026-11-12-rational-background-interval-certificate.json"))
    args = parser.parse_args()
    report = certify(args.divisions)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.out), "cell_extremes": report["cell_extreme_enclosures"],
                      "endpoint_tests": report["endpoint_tests"], "tail_tests": report["tail_tests"]}, indent=2))


if __name__ == "__main__":
    main()
