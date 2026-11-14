#!/usr/bin/env python3
"""Exact algebra certificate for the closed-geometry zero-period-operator proof.

This performs rational arithmetic only.  It does not select a finite repetition
count, solve a geometric ODE, optimize a curve, or certify embedding/reach.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
from pathlib import Path

def det(matrix):
    a = [[F(x) for x in row] for row in matrix]
    result = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        p = a[j][j]
        result *= p
        for i in range(j + 1, len(a)):
            ratio = a[i][j] / p
            for k in range(j + 1, len(a)):
                a[i][k] -= ratio * a[j][k]
            a[i][j] = F(0)
    return result

def qadd(x, y):
    return x[0] + y[0], x[1] + y[1]

def qmul(x, y):
    # Q(sqrt(33)), represented in the basis (1, sqrt(33)).
    return x[0]*y[0] + 33*x[1]*y[1], x[0]*y[1] + x[1]*y[0]

def qscale(c, x):
    return c*x[0], c*x[1]

def outer(x, y):
    return [[a*b for b in y] for a in x]

def string_matrix(a):
    return [[str(x) for x in row] for row in a]

def certificate():
    states = [(F(1), F(0)), (F(1), F(1)),
              (F(1), F(-1)), (F(2), F(0))]
    columns = []
    state_records = []
    for h, d in states:
        w = [(d*d+1)/(4*h), d/2, h/4]
        av = [F(0), 1/h, -2*d/(h*h)]
        bv = [F(-2), 2*d/h, -2*(d*d-1)/(h*h)]
        assert sum(x*y for x, y in zip(w, av)) == 0
        assert sum(x*y for x, y in zip(w, bv)) == 0
        matrices = []
        for vec in (av, bv):
            mat = outer(w, vec)
            assert sum(mat[i][i] for i in range(3)) == 0
            columns.append([mat[i][j] for i in range(3)
                            for j in range(3) if (i, j) != (2, 2)])
            matrices.append(string_matrix(mat))
        state_records.append({
            "h": str(h), "d": str(d),
            "w": list(map(str, w)), "A": list(map(str, av)),
            "B": list(map(str, bv)), "directions_wA_wB": matrices,
        })
    matrix = [list(row) for row in zip(*columns)]
    determinant = det(matrix)
    assert determinant == F(63, 2048)

    b = (F(9, 8), F(1, 8))  # a^2.
    bm1 = qadd(b, (F(-1), F(0)))
    relation = qadd(qscale(F(4), qmul(bm1, bm1)),
                    qscale(F(-1), qadd(b, (F(1), F(0)))))
    assert relation == (0, 0)

    representatives = [[F(x) for x in row] for row in
                       [(1, 0, 1), (2, 2, 1), (2, -2, 1), (1, 0, 4)]]
    first_three_determinant = det(representatives[:3])
    relation_fourth = [
        7*representatives[0][j]
        - F(3, 2)*representatives[1][j]
        - F(3, 2)*representatives[2][j]
        for j in range(3)
    ]
    assert first_three_determinant != 0
    assert relation_fourth == representatives[3]

    return {
        "status": "all_exact_algebra_assertions_passed",
        "method": "Python fractions.Fraction; no floating-point arithmetic",
        "scope": "circle balance and eight-dimensional matrix rank only",
        "curvature_square": {
            "expression": "(9+sqrt(33))/8",
            "basis_1_sqrt33": list(map(str, b)),
            "relation_4_bminus1_squared_minus_bplus1":
                list(map(str, relation)),
            "positive_branch_interval": ["7/4", "15/8"],
            "interval_reason": "5 < sqrt(33) < 6; therefore a^2>1",
            "circle_relation": "2*(a^2-1)/sqrt(1+a^2)=1",
        },
        "states": state_records,
        "rank_coordinates": "row-major 3x3, omitting (3,3), one-based",
        "rank_column_order": "w1*A1, w1*B1, ..., w4*A4, w4*B4",
        "rank_matrix": string_matrix(matrix),
        "rank_matrix_determinant": str(determinant),
        "rank": 8,
        "projective_representatives": string_matrix(representatives),
        "first_three_row_determinant": str(first_three_determinant),
        "fourth_combination": ["7", "-3/2", "-3/2"],
        "bulk_derivative_scales": {
            "alpha": "4*pi*a*(a^2+3)/(1+a^2)^(3/2) > 0",
            "beta": "4*pi/(1+a^2)^(3/2) > 0",
        },
        "not_claimed": [
            "numerical finite N or corrected parameters",
            "numerically evaluated geometric trajectory",
            "embedding or reach certificate",
            "finite continuous isometric family",
        ],
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    result = certificate()
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
        print(json.dumps({
            "status": result["status"],
            "determinant": result["rank_matrix_determinant"],
            "rank": result["rank"], "out": str(args.out),
        }, ensure_ascii=False))
    else:
        print(payload, end="")

if __name__ == "__main__":
    main()

