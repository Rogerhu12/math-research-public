#!/usr/bin/env python3
"""Small exact jet identities for the pure reciprocal fourth drift.

This does not evaluate a profile, a real curve, or a research quadrature.
All tails are independent algebraic symbols with their exact differential
identities.  The final formula is valid by ordinary bilinear complex extension.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def certificate() -> dict:
    x = sp.symbols("x", real=True)
    y = sp.symbols("y0:5", real=True)
    tail, mixed_tail = sp.symbols("A C", real=True)
    Q, L = 1 + x * x, x * x - 1
    vec = sp.Matrix([-y[1] / 2, y[0] - x * y[1] / 2])
    vec_prime = sp.Matrix([-y[2] / 2, y[1] / 2 - x * y[2] / 2])
    tail_prime = -vec_prime.dot(vec_prime) / 2
    mixed_tail_prime = sp.Integer(0)

    def derivative(expr):
        return (
            sp.diff(expr, x)
            + sum(sp.diff(expr, y[j]) * y[j + 1] for j in range(4))
            + sp.diff(expr, tail) * tail_prime
            + sp.diff(expr, mixed_tail) * mixed_tail_prime
        )

    norm = vec.dot(vec)
    aux = -y[0] * y[1] + x * y[1] ** 2 / 2
    # The target is zero: the second forcing is minus H(Y_y,Y_y).
    b = -(L * tail + (x * norm + aux) / 2)
    vec_b = sp.Matrix([-derivative(b) / 2, b - x * derivative(b) / 2])
    mixed_tail_prime = -vec_prime.dot(vec_b.applyfunc(derivative)) / 2
    states = []
    for k in (sp.Integer(1), sp.Integer(-1)):
        p = x + k
        r = -tail - norm / (2 * p)
        t = y[0] / p - y[1] / 2
        r_u = -p * p * derivative(r)
        t_u = -p * p * derivative(t)
        y_u = vec - p * vec_prime
        y_d = k * vec_b / p
        r_yd = k * (mixed_tail + vec.dot(vec_b) / (2 * p))
        eta = sp.cancel(-t * r_u / 2 + r * t_u / 2 + y_d.dot(y_u) / 2 - r_yd)
        G_u = (
            (eta - p * derivative(eta)) * sp.Matrix([1, x])
            - p * eta * sp.Matrix([0, 1])
        )
        ss_vec = r * sp.Matrix([k, 1]) + y_d
        D_ss = -ss_vec.dot(ss_vec) - 2 * t * (2 * r_yd + eta)
        D_uu = -r_u * r_u - 2 * y_u.dot(G_u)
        states.append((p, sp.cancel(p * p * D_ss), sp.cancel(D_uu / (p * p))))

    # J_sum/L = (p_+^2 Dss_+ + p_-^2 Dss_-)/(2L) + rho_+ - rho_-.
    # Each true right-anchored rho has xi derivative -Duu/(2p^2).
    obtained = sp.cancel(
        derivative((states[0][1] + states[1][1]) / (2 * L))
        - states[0][2] / 2 + states[1][2] / 2
    )
    P1 = (
        16 * x * tail
        + 4 * (y[0] - x * y[1] / 2) ** 2
        + (x * y[1] - L * y[2]) ** 2
        + 2 * L * y[2] ** 2
    )
    matrix = sp.Matrix([
        [4 * x, -2 * (2 * x * x - 1), 2 * x * L],
        [-2 * (2 * x * x - 1), 2 * x * (2 * x * x - 1), -L * (2 * x * x + 1)],
        [2 * x * L, -L * (2 * x * x + 1), x * L * Q],
    ])
    jets = sp.Matrix(y[:3])
    P2 = 16 * tail + (jets.T * matrix * jets)[0]
    identity_error = sp.cancel(obtained - P1 * P2 / (64 * L * L))
    assert identity_error == 0
    H = 2 * x * x - 1
    P2_squares = (
        16 * tail
        + 4 * x * (y[0] - H * y[1] / (2 * x) + L * y[2] / 2) ** 2
        + H / x * (y[1] - 2 * x * L * y[2] / H) ** 2
        + 2 * x * L / H * y[2] ** 2
    )
    assert sp.cancel(P2 - P2_squares) == 0
    principal_minors = [sp.factor(matrix[:j, :j].det()) for j in (1, 2, 3)]
    assert all(sp.cancel(actual - expected) == 0 for actual, expected in zip(
        principal_minors, [4 * x, 4 * (2 * x * x - 1), 8 * x * L]
    ))
    assert not sp.cancel(P1 * P2).has(mixed_tail, y[3], y[4])
    return {
        "schema": "reciprocal-pure-fourth-drift-exact-algebra-v1",
        "checks": {
            "true_right_anchor_derivative_factorization": True,
            "P2_sum_of_squares_identity": True,
            "positive_leading_minors_for_x_greater_than_one": True,
            "mixed_tail_and_third_fourth_jets_eliminated": True,
        },
        "matrix_leading_principal_minors": [str(v) for v in principal_minors],
        "remaining_tail": "A_q = 1/2 integral_x^r V_q_prime dot V_q_prime",
        "ordinary_bilinear_complex_extension": True,
        "complex_positivity_claimed": False,
        "whole_closed_geometry_period_claimed": False,
        "target_and_lower_range_paid": False,
        "real_profile_integrals_or_geometry_evaluated": False,
        "task_complete": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    result = json.dumps(certificate(), indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result, encoding="utf-8")
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
