#!/usr/bin/env python3
"""Exact analytic two-mode convex core; not a closed flexible-surface solution.

Use --out for a compact JSON record, and optionally --obj for an OPEN cylinder.
The intervals use rational lower/upper bounds for sqrt(2), checked by integers.
No baseline data, solver, credentials, or external network are needed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path


def encode_interval(lo: F, hi: F) -> dict:
    assert lo <= hi
    return {
        "lower_exact": str(lo),
        "upper_exact": str(hi),
        "lower_decimal_approx": float(lo),
        "upper_decimal_approx": float(hi),
    }


def algebraic_interval(u: F, v: F, sqrt2: tuple[F, F]) -> tuple[F, F]:
    lo, hi = sqrt2
    return (u + v * lo, u + v * hi) if v >= 0 else (u + v * hi, u + v * lo)


def produce(a: F, diameter: F, precision: int) -> dict:
    denominator = 10 ** precision
    numerator = math.isqrt(2 * denominator * denominator)
    sqrt2 = (F(numerator, denominator), F(numerator + 1, denominator))
    assert sqrt2[0] ** 2 < 2 < sqrt2[1] ** 2
    bounds = {
        "c": algebraic_interval(F(0), a / 20, sqrt2),
        "rho_min": algebraic_interval(F(1), -3 * a / 2, sqrt2),
        "rho_max": algebraic_interval(1 + 3 * a, 3 * a / 4, sqrt2),
        "radius_max_A": algebraic_interval(1 + a, -a / 20, sqrt2),
        "radius_min_B": algebraic_interval(1 - a, -a / 20, sqrt2),
    }
    if a <= 0 or bounds["rho_min"][0] <= 0:
        raise ValueError("Need 0 < a < sqrt(2)/3, with certified positive rho_min")
    d = 2 * a
    return {
        "scope": "Proved convex planar core and exact flat OPEN annulus; closed transition remains unsolved.",
        "support_function": "1 + a*cos(2*phi) - c*cos(4*phi)",
        "a_exact": str(a),
        "c_definition": "a/(10*sqrt(2))",
        "sqrt2": encode_interval(*sqrt2),
        "bounds": {key: encode_interval(*value) for key, value in bounds.items()},
        "core_phase_gap_exact": str(d),
        "core_phase_gap_approx": float(d),
        "core_phase_radians": "pi/2",
        "core_phase_period_radians": "pi",
        "core_diameter": encode_interval(2 * bounds["radius_max_A"][0], 2 * bounds["radius_max_A"][1]),
        "assumed_whole_diameter_upper_exact": str(diameter),
        "conditional_whole_gap_ratio_exact": str(d / diameter),
        "conditional_whole_gap_gate": d >= diameter / 5,
        "core_curvature_radius_over_assumed_D": encode_interval(
            bounds["rho_min"][0] / diameter, bounds["rho_min"][1] / diameter),
        "core_curvature_radius_gate": bounds["rho_min"][0] >= 3 * diameter / 100,
        "unpaid_conditions": [
            "C2 isometric transition to both fixed caps for one metric",
            "Whole closed-surface diameter <= assumed bound",
            "Whole-surface witness exclusion inequality",
            "Whole-surface curvature, support, embedding and reach for all phases",
            "Fixed-metric numerical refinement to solver tolerance",
            "Noncongruence under all E(3), including reflection",
        ],
    }


def cylinder_obj(path: Path, a: float, half_length: float, angular: int, axial: int, phase: float) -> None:
    c = a / (10 * math.sqrt(2))
    cp, sp = math.cos(phase), math.sin(phase)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as output:
        output.write("# OPEN exact-metric cylinder, sampled in normal angle; not a closed-surface solution.\n")
        for j in range(axial + 1):
            z = half_length * (2 * j / axial - 1)
            for i in range(angular):
                phi = 2 * math.pi * i / angular
                h = 1 + a * math.cos(2 * phi) - c * math.cos(4 * phi)
                hp = -2 * a * math.sin(2 * phi) + 4 * c * math.sin(4 * phi)
                x = h * math.cos(phi) - hp * math.sin(phi)
                y = h * math.sin(phi) + hp * math.cos(phi)
                output.write(f"v {cp*x-sp*y:.17g} {sp*x+cp*y:.17g} {z:.17g}\n")
        for j in range(axial):
            for i in range(angular):
                k = (i + 1) % angular
                p, q = j * angular + i + 1, j * angular + k + 1
                r, s = (j + 1) * angular + k + 1, (j + 1) * angular + i + 1
                output.write(f"f {p} {q} {r}\nf {p} {r} {s}\n")
    if path.stat().st_size >= 1_000_000:
        raise ValueError("Generated intermediate exceeds 1 MB; use smaller resolution or gzip before committing.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=F, default=F(19, 50))
    parser.add_argument("--diameter", type=F, default=F(19, 5))
    parser.add_argument("--precision", type=int, default=40)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--obj", type=Path)
    parser.add_argument("--half-length", type=float)
    parser.add_argument("--angular", type=int, default=192)
    parser.add_argument("--axial", type=int, default=8)
    parser.add_argument("--phase", type=float, default=0.0)
    args = parser.parse_args()
    if args.diameter <= 0 or args.precision < 5:
        parser.error("Positive diameter and precision >= 5 are required")
    record = produce(args.a, args.diameter, args.precision)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(record, indent=2) + "\n")
    else:
        print(json.dumps(record, indent=2))
    if args.obj:
        if args.angular < 8 or args.axial < 1:
            parser.error("Use angular >= 8 and axial >= 1")
        cylinder_obj(args.obj, float(args.a), args.half_length or 2 * float(args.a),
                     args.angular, args.axial, args.phase)


if __name__ == "__main__":
    main()
