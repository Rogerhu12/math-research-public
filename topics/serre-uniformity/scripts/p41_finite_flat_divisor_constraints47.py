#!/usr/bin/env python3
"""Integral confluent constraints for one or more pairs of nearby actual points.

Each row is a genuine evaluation or an integral divided difference formed from
four actual projective jets. No division by a nonunit occurs. Clusters of size
larger than two are deliberately unsupported.
"""
from collections import defaultdict


def finite_flat_constraints(a, frames, points):
    r, np = a.r, a.np
    n = points[0].shape[0]
    frame_values = r.mm(points, a.fc)
    assert np.all(r.units(frame_values))
    W = r.mul(points, r.inverse_values(frame_values))
    groups = defaultdict(list)
    for i in range(n):
        groups[tuple(int(x) % 47 for part in W for x in part[i])].append(i)
    rows, records = [], []
    for indices in groups.values():
        assert len(indices) <= 2, 'A cluster of length>2 needs actual higher confluent constraints.'
        first = r.rows(W, [indices[0]])
        if len(indices) == 1:
            rows.append(first)
            records.append({'indices_0based': indices, 'kind': 'single_actual_evaluation'})
            continue
        second = r.rows(W, [indices[1]])
        chart = next(frames.iter_charts(first, order=4, max_points=1, label='finite_flat_pair'))
        assert r.equal(chart['frame'], a.fc)
        coordinate = chart['coordinate']
        delta = r.sub(r.mm(second, coordinate), r.mm(first, coordinate))
        assert all(not np.any(v % 47) for v in delta)
        restored = r.zeros(1, 73)
        for coefficient in reversed(chart['W']):
            restored = r.add(r.mul(restored, delta), coefficient)
        assert r.equal(restored, second)
        divided = r.zeros(1, 73)
        for coefficient in reversed(chart['W'][1:]):
            divided = r.add(r.mul(divided, delta), coefficient)
        assert r.equal(r.sub(second, first), r.mul(delta, divided))
        assert r.equal(r.mm(divided, coordinate), r.column([[1, 0]]))
        assert r.iszero(r.mm(divided, a.fc))
        rows.extend([first, divided])
        records.append({'indices_0based': indices, 'kind': 'integral_divided_difference_pair',
                        'actual_first_W_fc_normalized': r.to_json(first),
                        'actual_second_W_fc_normalized': r.to_json(second),
                        'frame': r.to_json(a.fc), 'coordinate': r.to_json(coordinate),
                        'actual_coordinate_difference': r.to_json(delta),
                        'actual_first_W_jets_0to4': [r.to_json(x) for x in chart['W']],
                        'integral_divided_difference_row_mod47four': r.to_json(divided),
                        'all73_second_coordinates_reconstructed': True,
                        'all73_difference_equals_delta_times_divided_row': True,
                        'divided_row_coordinate_value_is_one': True,
                        'division_by_nonunit_or47_used': False})
    constraints = tuple(np.concatenate([v[k] for v in rows], axis=0) for k in range(2))
    rr, cc = r.rank_pivots(constraints)
    assert len(rr) == n
    return constraints, {'degree': n, 'records': records,
                         'flat_constraint_rows_mod47four': r.to_json(constraints),
                         'unit_rank_mod47': n, 'unit_minor_columns_0based': cc,
                         'all_constraints_integral_and_full_four_digit_precision': True}
