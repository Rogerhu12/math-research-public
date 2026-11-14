#!/usr/bin/env python3
"""Independent rational reconstruction of the frozen N7 diameter/marker proof.

No author imports: four-index integer counts, closed-form Chebyshev powers,
an exact seven-point Bernstein linear system, and decimal-grid bisection.
Only fixed compact-set model constants are read; no actual surface data.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import comb, factorial
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
NOTES = TOPIC / 'notes'
PUBLICATION = NOTES / '2026-11-09-db6f-audit-c3-marker-publication.json'
PUBLICATION_SHA = '66249d2b129aeea2cc4db56066839e7b4d6957c4abae78735f4e8388199ac9ee'
AUTHOR_REPORT = NOTES / '2026-11-09-db6f-audit-c3-marker-bounds.json'


def encode(value):
    if isinstance(value, F):
        return dict(numerator=str(value.numerator), denominator=str(value.denominator))
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def decode(value):
    if isinstance(value, dict) and set(value) == {'numerator', 'denominator'}:
        return F(int(value['numerator']), int(value['denominator']))
    if isinstance(value, dict):
        return {k: decode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [decode(v) for v in value]
    return value


def equal(actual, expected):
    assert json.dumps(encode(actual), sort_keys=True) == json.dumps(encode(expected), sort_keys=True)


def file_record(path):
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def polynomial_value(coefficients, x):
    return sum((value*x**i for i, value in enumerate(coefficients)), F(0))


def closed_chebyshev(n):
    """Explicit factorial formula, not the author's three-term recurrence."""
    p = [F(0)]*(n+1)
    for j in range(n//2+1):
        p[n-2*j] = (F(n, 2)*(-1)**j *
            F(factorial(n-j-1), factorial(j)*factorial(n-2*j))*2**(n-2*j))
    return p


def rational_solve(matrix, values):
    a = [list(row)+[value] for row, value in zip(matrix, values)]
    n = len(a)
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        divisor = a[j][j]
        a[j] = [v/divisor for v in a[j]]
        for i in range(n):
            if i != j:
                q = a[i][j]
                a[i] = [u-q*v for u, v in zip(a[i], a[j])]
    assert all(a[i][j] == int(i == j) for i in range(n) for j in range(n))
    return [row[-1] for row in a]


def decimal_sqrt_box(q):
    """Independent outward rational roots by integer bisection, no isqrt."""
    assert q >= 0
    scale = 10**20
    lo, hi = 0, (q.numerator//q.denominator+2)*scale
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid*mid*q.denominator <= q.numerator*scale*scale:
            lo = mid
        else:
            hi = mid
    lower = F(lo, scale)
    upper = lower if lower*lower == q else F(hi, scale)
    assert lower*lower <= q <= upper*upper
    return lower, upper


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    pub_raw = PUBLICATION.read_bytes()
    assert hashlib.sha256(pub_raw).hexdigest() == PUBLICATION_SHA
    publication = json.loads(pub_raw)
    inputs = [file_record(PUBLICATION)]
    for row in publication['files']:
        path = TOPIC / row['path']
        actual = file_record(path)
        assert actual['sha256'] == row['sha256'] and actual['bytes'] == row['bytes']
        inputs.append(actual)
    report = decode(json.loads(AUTHOR_REPORT.read_bytes()))
    for row in report['sources']:
        actual = file_record(TOPIC / row['path'])
        assert actual['sha256'] == row['sha256'] and actual['bytes'] == row['bytes']
        inputs.append(actual)

    # P_7^2=(1/64) sum_{i,j,k,l=0}^7 exp(i(i-j+k-l) phi).
    counts = Counter(i-j+k-l for i, j, k, l in itertools.product(range(8), repeat=4))
    assert sum(counts.values()) == 4096 and counts[0] == 344
    b = {j: F(counts[j], counts[0]) for j in range(1, 15)}
    equal(report['c0'], F(counts[0], 64))
    equal(report['b_j'], [b[j] for j in range(1, 15)])
    r = F(3, 20)
    equal(report['r'], r)
    p = [F(0)]*8
    for k in range(1, 8):
        for i, v in enumerate(closed_chebyshev(k)):
            p[i] += b[2*k]*v/F(36*k*k-1)
    derivative = [(i+1)*p[i+1] for i in range(7)]
    equal(report['P_power_coefficients'], p)
    equal(report['P_derivative_power_coefficients'], derivative)

    # Seven rational values determine two degree-six polynomials exactly.
    # This is a finite coefficient identity proof, not sampled angle positivity.
    us = [F(j, 6) for j in range(7)]
    matrix = [[F(comb(6, i))*u**i*(1-u)**(6-i) for i in range(7)] for u in us]
    values = [polynomial_value(derivative, -1+2*u) for u in us]
    beta = rational_solve(matrix, values)
    equal(report['bernstein_coefficients'], beta)
    assert min(beta) > F(1, 100)
    for u, value in zip(us, values):
        assert polynomial_value(report['P_derivative_at_minus1_plus_2u_power_coefficients'], u) == value
        assert sum((beta[i]*matrix[us.index(u)][i] for i in range(7)), F(0)) == value
    diameter = 2-4*(1-r)*polynomial_value(p, F(-1))
    assert diameter == F(572416608462667473, 275764086893044750)
    coarse = 2+4*(1-r)*sum((b[2*k]/F(36*k*k-1) for k in range(1, 8)), F(0))
    H = 1+2*(1-r)*sum(((-1)**(j+1)*b[j]/F(9*j*j-1) for j in range(1, 15)), F(0))
    delta = 4*(1-r)*sum((b[j]/F(9*j*j-1) for j in range(1, 15, 2)), F(0))
    hmin = H-delta
    for field, value in [('exact_core_diameter', diameter), ('coarse_core_diameter_bound', coarse),
                         ('H_support_value', H), ('halfphase_support_gap', delta), ('h_min', hmin)]:
        equal(report[field], value)
    assert diameter < coarse and 2*H == 4+delta-coarse and hmin > F(23, 40)
    for field, value in [('diameter', diameter), ('coarse_bound', coarse),
                         ('H', H), ('Delta', delta), ('bernstein_min', min(beta))]:
        assert F(report['decimal_displays_down'][field]) < value

    cases = [
        ('coarse_point_z_1_5', F(1, 5), F(0), F(0), F(0), coarse),
        ('sharp_point_z_4_5', F(4, 5), F(0), F(0), F(0), diameter),
        ('sharp_cap_z_3_10_a_2_25', F(3, 10), F(0), F(2, 25), F(1, 200), diameter),
        ('sharp_cap_z_2_5_a_1_10', F(2, 5), F(0), F(1, 10), F(1, 200), diameter),
        ('positive_band_cap_z_2_5_a_1_10', F(2, 5), F(1, 100), F(1, 10), F(1, 200), diameter),
    ]
    model_checks = []
    for row, (name, z, band, a, error, d) in zip(report['marker_models'], cases):
        equal([row[k] for k in ('name', 'z', 'core_halfheight', 'marker_radius',
                               'epsilon0', 'epsilon1', 'core_diameter_used')],
              [name, z, band, a, error, error, d])
        Z = z+band
        L2, U2 = 4*H*H+Z*Z, d*d+Z*Z
        equal([row['L0_squared'], row['U1_squared']], [L2, U2])
        for label, square in [('L0', L2), ('U1', U2)]:
            lo, hi = row[label+'_lower'], row[label+'_upper']
            assert 0 <= lo <= hi and lo*lo <= square <= hi*hi
            assert hi-lo <= F(1, 2**120)
        Llo, Uhi = row['L0_lower'], row['U1_upper']
        assert a <= row['U1_lower'] and z >= band >= 0
        core2 = d*d+4*band*band
        equal(row['diameter_cases'], dict(core_core_squared=core2,
              marker_marker_upper=2*a, core_marker_upper=Uhi+a))
        assert core2 <= U2 and 2*a <= row['U1_lower']+a
        budget, consumption = 9*Llo-10*Uhi, a+38*error
        lower, upper = Llo+a-2*error, Uhi+a+2*error
        ratio = (lower-upper)/(2*lower)
        for field, value in [('thickness_budget_lower', budget), ('budget_consumption', consumption),
                             ('strict_budget_margin', budget-consumption),
                             ('actual_initial_diameter_lower_after_error', lower),
                             ('actual_final_diameter_upper_after_error', upper),
                             ('rigid_quotient_ratio_lower', ratio)]:
            equal(row[field], value)
        assert lower > 0 and budget > consumption and ratio > F(1, 20)
        assert ratio > F(row['ratio_lower_decimal_down'])
        independently_Llo, _ = decimal_sqrt_box(L2)
        _, independently_Uhi = decimal_sqrt_box(U2)
        independent_lower = independently_Llo+a-2*error
        independent_upper = independently_Uhi+a+2*error
        independent_ratio = (independent_lower-independent_upper)/(2*independent_lower)
        assert independent_ratio > F(row['ratio_lower_decimal_down']) > F(1, 20)
        init = row['complete_initial_diameter_upper_from_R29_ball_bound']-2*error
        assert init >= 2*a and init >= a and init*init >= core2
        assert (init-a)**2 >= (F(57, 40)+H)**2+Z*Z
        model_checks.append(dict(name=name, all_three_diameter_cases=True,
            original_exact_budget_equal=True, independent_decimal_grid_ratio_lower=independent_ratio,
            strict_display_verified=row['ratio_lower_decimal_down'],
            independent_positive_margin=9*independently_Llo-10*independently_Uhi-consumption))
    assert len(report['marker_models']) == len(cases)

    size = report['additional_size_compatibility_only']
    final = report['marker_models'][-1]
    Dstar, c, reach = F(11, 4), F(3, 10), F(33, 400)
    expected_size = dict(Dstar=Dstar, fixed_disk_radius=c, fixed_disk_diameter=2*c,
        README_grip_diameter_required_at_Dstar=Dstar/5, README_reach_target_at_Dstar=reach,
        core_curvature_radius_lower=r, spherical_marker_curvature_radius=F(1, 10),
        marker_to_band_vertical_gap_lower=F(29, 100), disk_to_core_horizontal_gap_lower=F(11, 40),
        local_radius_and_separation_budget_only=True, whole_closed_surface_reach_proved=False,
        fixed_material_H_constructed=False)
    equal(size, expected_size)
    assert final['complete_initial_diameter_upper_from_R29_ball_bound'] < Dstar
    assert 2*c > Dstar/5 and min(r, F(1, 10)) > reach
    assert min(F(29, 100), F(11, 40)) > 2*reach and c < hmin

    # Coordinates (x,y,z) below represent (x,sqrt(3)*y,z) in Euclidean space.
    triangle = [(F(1), F(0), F(0)), (F(-1, 2), F(1, 2), F(0)),
                (F(-1, 2), F(-1, 2), F(0))]
    rotate = lambda p: ((p[0]-3*p[1])/2, (p[0]+p[1])/2, p[2])
    mark = (F(-1), F(0), F(1, 2))
    def squared_pairs(points):
        return [(p[0]-q[0])**2+3*(p[1]-q[1])**2+(p[2]-q[2])**2
                for p, q in itertools.combinations(points, 2)]
    original_pairs = squared_pairs(triangle+[mark])
    rotated_pairs = squared_pairs([rotate(p) for p in triangle]+[mark])
    assert max(original_pairs) == F(17, 4) and max(rotated_pairs) == F(13, 4)
    margin = F(81, 100)*max(original_pairs)-max(rotated_pairs)
    assert margin == F(77, 400) > 0
    tetra = report['finite_four_vertex_model']
    equal([tetra[k] for k in ('initial_diameter_squared', 'halfphase_diameter_squared',
                             'strict_squared_one_twentieth_margin')], [F(17, 4), F(13, 4), margin])

    output = dict(status='PASS_INDEPENDENT_EXACT_N7_DIAMETER_AND_MARKER_MODEL_LEDGER',
        scope=__doc__, script=file_record(Path(__file__).resolve()), input_files=inputs,
        independent_four_index_count=4096, polynomial_degree=7, derivative_degree=6,
        exact_unisolvent_points=7, exact_Bernstein_coefficients_match=True,
        strict_Bernstein_lower=F(1, 100), minimum_Bernstein_coefficient=min(beta),
        exact_diameter=diameter, H=H, delta=delta,
        all_author_scalar_root_boxes_verified_by_exact_squares=True,
        independent_root_method='integer bisection on the decimal 10^20 grid',
        marker_model_checks=model_checks, additional_size_compatibility_verified=True,
        four_vertex_squared_pairs=dict(initial=original_pairs, halfphase=rotated_pairs),
        new_solver_or_optimizer_calls=0, actual_candidate_data_read=False,
        whole_reach_or_connected_isometric_surface_proved=False)
    raw = (json.dumps(encode(output), indent=2, ensure_ascii=False)+'\n').encode()
    with args.out.open('xb') as handle:
        handle.write(raw)
    print(json.dumps(dict(status=output['status'], source_bindings=len(inputs),
        fixed_models=len(model_checks), exact_Bernstein_coefficients=7,
        output_sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw), solver_calls=0)))


if __name__ == '__main__':
    main()
