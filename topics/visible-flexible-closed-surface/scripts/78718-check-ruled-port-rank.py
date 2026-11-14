#!/usr/bin/env python3
"""Exact six-column endpoint rank for the tilted, closed ruled-port seed.

Only rational scalar algebra is performed.  No curve solver, PDE, interval
continuation, or numerical surface certificate is supplied by this check.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]


def determinant(matrix):
    a = [row[:] for row in matrix]
    result = Q(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        diagonal = a[i][i]
        result *= diagonal
        for j in range(i + 1, len(a)):
            factor = a[j][i] / diagonal
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
            a[j][i] = Q(0)
    return result


def column(c, s, epsilon, eta):
    assert c * c + s * s == 1
    z = epsilon * (c * c - s * s)
    zp = -4 * epsilon * c * s
    zpp = -4 * epsilon * (c * c - s * s)
    position = [c, s, z]
    tangent = [-s, c, zp]
    speed2 = 1 + zp * zp
    q = zp * zpp
    curvature_normal = [-speed2 * c + q * s,
                        -speed2 * s - q * c, zpp]
    assert dot(curvature_normal, tangent) == 0
    assert dot(curvature_normal, [c, s, Q(0)]) == -speed2
    rotation = cross(tangent, curvature_normal)
    w = [x + eta * y for x, y in zip(curvature_normal, rotation)]
    assert dot(w, tangent) == 0 and dot(w, w) > 0
    return w + cross(position, w)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    epsilon, eta = Q(1, 10), Q(1)
    points = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(0)),
              (Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)),
              (Q(-3, 5), Q(4, 5))]
    columns = [column(c, s, epsilon, eta) for c, s in points]
    matrix = [[col[i] for col in columns] for i in range(6)]
    value = determinant(matrix)
    expected = Q(15838112388562926448768487424,
                 9876209658570587635040283203125)
    assert value == expected and value > 0
    report = {
        "status": "PASS_EXACT_SIX_COLUMN_RANK_ONLY",
        "arithmetic": "Python fractions.Fraction; exact elimination",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "epsilon": str(epsilon), "eta": str(eta),
        "column_order": "W then gamma cross W",
        "sample_cos_sin": [[str(c), str(s)] for c, s in points],
        "determinant": str(value), "rank": 6,
        "scope": "Closed seed endpoint derivative only; no nonlinear solver or closed surface."
    }
    args.report.write_text(json.dumps(report, indent=2) + "\n")
    print("PASS_EXACT_SIX_COLUMN_RANK_ONLY")
    print("report_bytes=" + str(args.report.stat().st_size))
    print("report_sha256=" + sha256(args.report.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
