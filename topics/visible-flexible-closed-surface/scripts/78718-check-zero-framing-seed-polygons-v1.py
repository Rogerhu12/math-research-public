#!/usr/bin/env python3
"""Exact finite polygon checks for the frozen zero-framing seed draft.

This checks the fixed rational data uniformly for 43 <= L <= 44.  It does
not evaluate the smoothing integrals, solve a PDE, or certify a flex.
All minima are exact minima of piecewise quadratic distance functions.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def affine(a, b=0):
    return (F(a), F(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def scale(x, s):
    return (x[0] * s, x[1] * s)


def at(x, t):
    return x[0] + x[1] * t


def point(x, y):
    return (x if isinstance(x, tuple) else affine(x), affine(y))


def ordered(x, y):
    if at(x, F(87, 2)) > at(y, F(87, 2)):
        x, y = y, x
    assert at(x, 43) <= at(y, 43) and at(x, 44) <= at(y, 44)
    return x, y


def box(a, b):
    assert a[0] == b[0] or a[1] == b[1]
    return (ordered(a[0], b[0]), ordered(a[1], b[1]))


def exact_distance_squared(first, second):
    """Minimize the distance of two moving axis-aligned boxes exactly."""
    gaps = []
    for axis in range(2):
        a, b = first[axis], second[axis]
        gaps.append([affine(0), sub(a[0], b[1]), sub(b[0], a[1])])
    breaks = {F(43), F(44)}
    for choices in gaps:
        for i, x in enumerate(choices):
            for y in choices[i + 1:]:
                z = sub(x, y)
                if z[1]:
                    t = -z[0] / z[1]
                    if 43 < t < 44:
                        breaks.add(t)
    breaks = sorted(breaks)
    candidates = set(breaks)
    for left, right in zip(breaks, breaks[1:]):
        mid = (left + right) / 2
        selected = [max(choices, key=lambda z: at(z, mid)) for choices in gaps]
        coefficient = sum(z[1] ** 2 for z in selected)
        if coefficient:
            critical = -sum(z[0] * z[1] for z in selected) / coefficient
            if left <= critical <= right:
                candidates.add(critical)

    def value(t):
        return sum(max(at(z, t) for z in choices) ** 2 for choices in gaps)

    return min((value(t), t) for t in candidates)


def check_polygon(vertices, required_squared):
    n = len(vertices)
    edges = [box(vertices[i], vertices[(i + 1) % n]) for i in range(n)]
    segment_rows = []
    vertex_rows = []
    for i in range(n):
        for j in range(i + 1, n):
            if (j - i) % n in (1, n - 1):
                continue
            distance, parameter = exact_distance_squared(edges[i], edges[j])
            assert distance >= required_squared, (i, j, distance, parameter)
            segment_rows.append((distance, parameter, i, j))
        singleton = box(vertices[i], vertices[i])
        for j in range(n):
            if j in (i, (i - 1) % n):
                continue
            distance, parameter = exact_distance_squared(singleton, edges[j])
            assert distance >= required_squared, (i, j, distance, parameter)
            vertex_rows.append((distance, parameter, i, j))
    sm = min(segment_rows)
    vm = min(vertex_rows)
    return {
        "nonadjacent_segment_pairs": len(segment_rows),
        "vertex_nonincident_edge_pairs": len(vertex_rows),
        "minimum_segment_distance_squared": str(sm[0]),
        "minimum_vertex_edge_distance_squared": str(vm[0]),
        "minimum_segment_witness": {"L": str(sm[1]), "first": sm[2], "second": sm[3]},
        "minimum_vertex_edge_witness": {"L": str(vm[1]), "vertex": vm[2], "edge": vm[3]},
        "required_squared": str(required_squared),
        "all_L_in_closed_interval_43_44": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise SystemExit("Refusing to overwrite an existing report")
    p = [point(0, 0), point(affine(0, 1), 0), point(affine(0, 1), -1),
         point(affine(1, 1), -1), point(affine(1, 1), F(11, 10)),
         point(affine(0, 1), F(11, 10)), point(affine(0, 1), F(1, 10)),
         point(0, F(1, 10)), point(0, F(11, 10)), point(-1, F(11, 10)),
         point(-1, -1), point(0, -1)]
    q = [point(0, 0), point(2, 0), point(2, -1), point(6, -1),
         point(6, 3), point(5, 3), point(5, F(-1, 2)), point(3, F(-1, 2)),
         point(3, 2), point(-2, 2), point(-2, -3), point(0, -3)]
    directions = [(1, 0), (0, -1), (1, 0), (0, 1), (-1, 0), (0, -1),
                  (-1, 0), (0, 1), (-1, 0), (0, -1), (1, 0), (0, 1)]
    lengths = [affine(0, 1), affine(1), affine(1), affine(F(21, 10)), affine(1),
               affine(1), affine(0, 1), affine(1), affine(1), affine(F(21, 10)),
               affine(1), affine(1)]
    qlengths = [F(2), F(1), F(4), F(4), F(1), F(7, 2), F(2), F(5, 2),
                F(5), F(5), F(2), F(3)]
    turn_signs = []
    mixed_integral = affine(0)
    for i, (ex, ey) in enumerate(directions):
        before = directions[(i - 1) % 12]
        turn_signs.append(before[0] * ey - before[1] * ex)
        for axis, e in enumerate((ex, ey)):
            assert sub(p[(i + 1) % 12][axis], p[i][axis]) == scale(lengths[i], e)
            assert sub(q[(i + 1) % 12][axis], q[i][axis]) == affine(qlengths[i] * e)
        assert at(lengths[i], 43) >= 1 and at(lengths[i], 44) >= 1
        determinant = q[i][0][0] * ey - q[i][1][0] * ex
        mixed_integral = add(mixed_integral, scale(lengths[i], determinant))
    assert [i for i, s in enumerate(turn_signs) if s == -1] == [0, 1, 6, 7]
    assert turn_signs.count(1) == 8
    assert mixed_integral == affine(F(109, 5), F(-1, 2))
    maximum_q_squared = max(x[0] ** 2 + y[0] ** 2 for x, y in q)
    assert maximum_q_squared == 45
    result = {
        "schema": "78718-zero-framing-seed-rational-polygon-check-v1",
        "status": "PASS_EXACT_FINITE_POLYGON_DATA_ONLY",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "fractions.Fraction only; exact piecewise quadratic minimization",
        "P": check_polygon(p, F(1, 100)),
        "Q": check_polygon(q, F(1, 4)),
        "positive_turns": 8,
        "negative_turns": 4,
        "mixed_integral_constant": str(mixed_integral[0]),
        "mixed_integral_L_coefficient": str(mixed_integral[1]),
        "maximum_Q_vertex_norm_squared": str(maximum_q_squared),
        "solver_calls": 0,
        "scope": "No smoothing-integral evaluation, no PDE or common-metric flex, no amplitude or reach certificate.",
    }
    args.report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "report_bytes": args.report.stat().st_size,
                      "report_sha256": hashlib.sha256(args.report.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
