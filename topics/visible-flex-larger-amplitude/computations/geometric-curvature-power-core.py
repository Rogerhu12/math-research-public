#!/usr/bin/env python3
"""Exact rational finite-support-spectrum convex core, not a closed flex solution."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from math import comb, factorial
from pathlib import Path


def pair(value: F) -> dict:
    return {"exact": str(value), "approx": float(value)}


def generate(n: int, r: F, diameter: F = F(19, 5)) -> dict:
    if n < 1 or not 0 < r < 1 or diameter <= 0:
        raise ValueError("Need N >= 1, 0 < r < 1 and diameter > 0")
    mu = F(comb(2 * n, n), 4 ** n)
    w = 1 - r
    coeff = [F(2) * w * (-1) ** j * F(comb(2*n, n-j), comb(2*n, n)) /
             (1 - 4*j*j) for j in range(1, n+1)]
    A = 1 + sum(coeff)
    B = 1 + sum(c * (-1) ** j for j, c in enumerate(coeff, 1))
    I = F(4 ** n * factorial(n) ** 2, factorial(2*n+1))
    # These exact equalities connect support values to the independent integrals.
    assert A == r + w * I / mu
    assert B == r + w / (mu * (2*n+1))
    rho_max = r + w / mu
    gap = A - B
    return {
        "scope": "Proved analytic planar convex core; C2 isometric closed transition remains unsolved.",
        "rho_definition": "r + (1-r)*sin(phi)^(2*N)/mu_N",
        "support_definition": "1 + sum_j c_j*cos(2*j*phi)",
        "N": n,
        "r": pair(r),
        "mu_N": pair(mu),
        "coefficients_exact": [str(c) for c in coeff],
        "coefficients": [float(c) for c in coeff],
        "frequencies": [2*j for j in range(1, n+1)],
        "radius_max_A": pair(A),
        "radius_min_B": pair(B),
        "core_diameter": pair(2*A),
        "core_phase_gap": pair(gap),
        "core_phase_radians": "pi/2",
        "rho_min": pair(r),
        "rho_max": pair(rho_max),
        "kappa_min": pair(1/rho_max),
        "kappa_max": pair(1/r),
        "assumed_whole_diameter_upper": pair(diameter),
        "conditional_gap_ratio": pair(gap/diameter),
        "conditional_core_reach_ratio": pair(r/diameter),
        "core_gap_gate": gap >= diameter/5,
        "core_curvature_gate": r >= 3*diameter/100,
        "unpaid_conditions": [
            "Actual C2 isometric transition from this core to two fixed caps",
            "Actual whole diameter and witness exclusion inequality",
            "All-time whole-surface curvature, support, embedding and reach",
            "Fixed-metric refinement to numerical solver tolerance",
            "Noncongruence under full E(3)",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--r", type=F, default=F(3, 20))
    parser.add_argument("--diameter", type=F, default=F(19, 5))
    parser.add_argument("--out", type=Path)
    parser.add_argument("--table", action="store_true")
    args = parser.parse_args()
    result = generate(args.N, args.r, args.diameter)
    if args.table:
        result = {"scope": "Different physical cores, not a fixed-metric refinement sequence.",
                  "rows": [generate(n, r, args.diameter) for n, r in
                           [(3,F(3,20)), (4,F(3,20)), (6,F(3,20)),
                            (8,F(3,25)), (12,F(3,20))]]}
    encoded = json.dumps(result, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(encoded)
    else:
        print(encoded)


if __name__ == "__main__":
    main()
