#!/usr/bin/env python3
"""Exact scalar consequences for R93, without a fabricated surface or moment.

The general proof is in R93.  This executable verifies its finite-difference
identities for the requested finite list of orders and records rational
coefficients.  It does not certify an uncomputed activity moment or geometry.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path


def fraction_text(q):
    q = F(q)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def chebyshev(order):
    if order == 0:
        return [F(1)]
    previous, current = [F(1)], [F(0), F(1)]
    for _ in range(1, order):
        following = [F(0)] + [2 * q for q in current]
        for k, q in enumerate(previous):
            following[k] -= q
        previous, current = current, following
    return current


def evaluate(coefficients, x):
    value = F(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def phase_gap_coefficient(j):
    if j < 1:
        raise ValueError("j must be positive")
    return F(2) ** (1 - 3 * j) * F(3) ** j * factorial(j) / (
        F(j) ** j * (2**j - 1)
    )


def euclidean_constant(order, radius, support):
    radius, support = F(radius), F(support)
    if order < 1 or not 0 < support <= radius:
        raise ValueError("Require order >= 1 and 0 < support <= radius")
    pi_upper = F(22, 7)
    extended_radius = radius + support / 2
    radial_lipschitz = 1 + pi_upper * radius**2 / support**2
    symmetric_difference = 4 * pi_upper * extended_radius**2 * radial_lipschitz
    volume = F(4, 3) * pi_upper * radius**3
    tensor_lipschitz = (
        extended_radius**order * symmetric_difference
        + F(3, 2) * order * volume * extended_radius ** (order - 1)
    )
    invariant_lipschitz = 2 * volume * radius**order * tensor_lipschitz
    return {
        "small_distance_cutoff": support / 3,
        "extended_radius": extended_radius,
        "radial_difference_coefficient": radial_lipschitz,
        "symmetric_difference_volume_coefficient": symmetric_difference,
        "volume_upper": volume,
        "tensor_difference_coefficient": tensor_lipschitz,
        "invariant_difference_coefficient": invariant_lipschitz,
    }


def order_certificate(j, radius, support):
    order = 3 * j
    h = F(3, 2 * j)
    xs = [1 - k * h for k in range(j + 1)]
    weights = [(-1) ** (j - k) * comb(j, k) for k in range(j + 1)]
    assert xs[0] == 1 and xs[-1] == -F(1, 2)
    assert sum(abs(q) for q in weights[1:]) == 2**j - 1
    lower_annihilated = []
    for lower in range(j):
        value = sum(w * evaluate(chebyshev(lower), x) for w, x in zip(weights, xs))
        assert value == 0
        lower_annihilated.append(lower)
    top_difference = sum(
        w * evaluate(chebyshev(j), x) for w, x in zip(weights, xs)
    )
    expected = (-h) ** j * factorial(j) * 2 ** (j - 1)
    assert top_difference == expected
    from_difference = abs(expected) * F(2) ** (2 - order) / (2**j - 1)
    coefficient = phase_gap_coefficient(j)
    assert coefficient == from_difference and coefficient > 0
    bounds = euclidean_constant(order, radius, support)
    return {
        "j": j,
        "tensor_order": order,
        "phase_definition": "alpha_k = arccos(x_k)/3, k=0,...,j",
        "exact_x_nodes": [fraction_text(q) for q in xs],
        "finite_difference_weights": weights,
        "lower_chebyshev_orders_annihilated": lower_annihilated,
        "top_chebyshev_finite_difference": fraction_text(top_difference),
        "gap_per_absolute_activity_times_cap_moment": fraction_text(coefficient),
        "gap_per_absolute_core_moment_times_cap_after_two_lengths": fraction_text(coefficient / 400),
        "euclidean_rational_constants": {k: fraction_text(v) for k, v in bounds.items()},
        "distance_per_absolute_core_moment_times_cap_before_cutoff": fraction_text(
            coefficient / (400 * bounds["invariant_difference_coefficient"])
        ),
    }


def certificate(max_j, radius, support):
    if max_j < 1:
        raise ValueError("max_j must be positive")
    topic = Path(__file__).resolve().parents[3]
    names = [
        "results/R67-universal-threefold-marker-and-euclidean-noncongruence.md",
        "results/R87-single-gentle-ramp-half-curvature-held-window.md",
        "results/R88-quantitative-euclidean-hausdorff-from-third-moment.md",
    ]
    sources = {name: hashlib.sha256((topic / name).read_bytes()).hexdigest() for name in names}
    phase_margin = F(4, 5) - F(44, 63)
    assert phase_margin == F(32, 315) > 0
    length_gap = F(1, 100) - F(1, 200)
    assert length_gap / 2 == F(1, 400)
    orders = [order_certificate(j, radius, support) for j in range(1, max_j + 1)]
    assert phase_gap_coefficient(1) == F(3, 4)
    assert phase_gap_coefficient(2) == F(3, 64)
    return {
        "schema": "R93-exact-high-order-finite-phase-and-E3-scalar-contract-v1",
        "status": "exact_scalar_identities_passed_no_new_surface",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proved_source_references": sources,
        "radius_upper": fraction_text(radius),
        "positive_support_lower": fraction_text(support),
        "translation_bound_per_surface_Hausdorff_distance": "3/2",
        "phase_upper": "2*pi/9",
        "phase_upper_rational_bound": "44/63",
        "margin_below_R87_phase_end": fraction_text(phase_margin),
        "lengths": ["1/200", "1/100"],
        "activity_lower_per_absolute_core_moment": "1/400",
        "orders": orders,
        "finite_scalar_orders_only": True,
        "all_order_statement_is_in_full_proof": True,
        "actual_core_moment_or_activity_supplied": False,
        "new_lambda_one_or_BVP_or_tail_or_mesh": False,
        "new_surface_geometry_certified": False,
        "completion_claimed": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-j", type=int, default=8)
    parser.add_argument("--radius", type=F, default=F(27, 10))
    parser.add_argument("--support", type=F, default=F(41, 500))
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = certificate(args.max_j, args.radius, args.support)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "orders": len(result["orders"]),
        "output_sha256": hashlib.sha256(args.out.read_bytes()).hexdigest(),
    }))


if __name__ == "__main__":
    main()
