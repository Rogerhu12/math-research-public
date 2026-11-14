#!/usr/bin/env python3
"""An eight-row exact support certificate for two finite point sets.

This checks the rational entries of the accompanying conditional theorem's
toy table. It evaluates no actual surface, support optimizer or solver.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parent.parent
METHOD = TOPIC / 'notes/2026-11-09-db6f-prefix-euclidean-support-lower-bound.md'


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def transpose(a):
    return list(map(list, zip(*a)))


def mv(a, x):
    return [dot(row, x) for row in a]


def mm(a, b):
    return [[dot(row, column) for column in transpose(b)] for row in a]


def det(a):
    return sum((a[0][j]*(a[1][(j+1)%3]*a[2][(j+2)%3]
                 -a[1][(j+2)%3]*a[2][(j+1)%3]) for j in range(3)), Q(0))


def rotation(q):
    w, x, y, z = q
    n = dot(q, q)
    return [[v/n for v in row] for row in [
        [w*w+x*x-y*y-z*z, 2*(x*y-w*z), 2*(x*z+w*y)],
        [2*(x*y+w*z), w*w-x*x+y*y-z*z, 2*(y*z-w*x)],
        [2*(x*z-w*y), 2*(y*z+w*x), w*w-x*x-y*y+z*z]]]


def support(points, direction):
    return max(dot(point, direction) for point in points)


def encode(value):
    if isinstance(value, Q):
        return f'{value.numerator}/{value.denominator}'
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(x) for x in value]
    return value


def item(path):
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def calculate():
    identity = [[Q(int(i == j)) for j in range(3)] for i in range(3)]
    reflection = [[Q(-1), Q(0), Q(0)], [Q(0), Q(1), Q(0)], [Q(0), Q(0), Q(1)]]
    p0 = [[Q(3), Q(0), Q(0)], [Q(-3), Q(0), Q(0)]]
    p1 = [[Q(1), Q(0), Q(0)], [Q(-1), Q(0), Q(0)]]
    directions = p1
    weights = [Q(1, 2), Q(1, 2)]
    assert all(dot(u, u) == 1 for u in directions)
    assert sum(abs(w) for w in weights) == 1
    assert all(sum(weights[i]*directions[i][j] for i in range(2)) == 0 for j in range(3))
    radius, rotation_radius, target = Q(1), Q(7, 4), Q(1, 5)
    assert all(dot(p, p) <= radius*radius for p in p1)
    # Paper coverage: max_j |q_j| >= 1/2 on S^3 and op-distance squared <= 3.
    assert Q(3) < rotation_radius**2
    rows = []
    for j in range(4):
        quaternion = [Q(int(k == j)) for k in range(4)]
        r = rotation(quaternion)
        assert mm(transpose(r), r) == identity and det(r) == 1
        for branch, factor in [('proper', identity), ('reflected', reflection)]:
            center = mm(r, factor)
            assert mm(transpose(center), center) == identity
            assert det(center) == (1 if branch == 'proper' else -1)
            support0 = [support(p0, u) for u in directions]
            support1 = [support(p1, mv(transpose(center), u)) for u in directions]
            lower = sum(weights[i]*(support0[i]-support1[i]) for i in range(2))
            certified = lower-radius*rotation_radius
            margin = certified-target
            assert lower == 2 and certified == Q(1, 4) and margin == Q(1, 20)
            rows.append({'branch': branch, 'quaternion_axis_index': j,
                         'rotation_center': center, 'cell_radius_upper': rotation_radius,
                         'directions': directions, 'weights': weights,
                         'support0_exact': support0, 'support1_exact': support1,
                         'balanced_center_gap_lower': lower,
                         'whole_cell_distance_lower': certified, 'target': target,
                         'strict_margin': margin})
    # This is a fixed-orientation C3 witness, not an E(3) quotient certificate.
    tri_u = [[Q(1), Q(0), Q(0)], [Q(0), Q(1), Q(0)], [Q(-3, 5), Q(-4, 5), Q(0)]]
    tri_w = [Q(1, 4), Q(1, 3), Q(5, 12)]
    assert all(dot(u, u) == 1 for u in tri_u) and sum(tri_w) == 1
    assert all(sum(w*u[j] for w, u in zip(tri_w, tri_u)) == 0 for j in range(3))
    c3 = 2*sum(w*(4*u[0]**3-3*u[0]) for w, u in zip(tri_w, tri_u))
    assert c3 == Q(32, 25)
    return encode({'status': 'EXACT_TOY_TABLE_ONLY_NO_ACTUAL_SURFACE_BOUND',
        'source_bindings': [item(Path(__file__).resolve()), item(METHOD)],
        'sets': {'S0': p0, 'S1': p1}, 'enclosing_radius_S1': radius,
        'coverage': {'rule': 'C_j={R(q): q in S^3, |q_j|>=1/2}; j=0,1,2,3',
                     'operator_distance_squared_upper': Q(3),
                     'declared_operator_radius_upper': rotation_radius,
                     'reflection': reflection,
                     'coverage_is_the_proved_lemma_not_a_sampled_check': True},
        'rows': rows, 'all_eight_rows_have_strict_positive_margin': True,
        'certified_minimum_over_E3_lower': Q(1, 4),
        'declared_target': target, 'minimum_strict_margin': Q(1, 20),
        'analytic_exact_minimum_with_separate_identity_upper_bound': Q(2),
        'c3_fixed_orientation_witness': {'directions': tri_u, 'weights': tri_w,
            'support_gap_coefficient_multiplying_q': c3,
            'quotient_lower_bound_asserted': False},
        'solver_support_optimizer_geometry_backend_calls': 0})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    report = calculate()
    raw = (json.dumps(report, indent=2, allow_nan=False)+'\n').encode()
    assert len(raw) < 100_000
    with args.out.open('xb') as handle:
        handle.write(raw)
    args.out.chmod(0o444)
    print(json.dumps({'all_checks_passed': True, 'rows': 8,
                      'lower_bound': '1/4', 'strict_margin_above_1_5': '1/20',
                      'solver_calls': 0, 'bytes': len(raw),
                      'sha256': hashlib.sha256(raw).hexdigest()}))


if __name__ == '__main__':
    main()
