#!/usr/bin/env python3
"""One-column height initialization from already evaluated, frozen arrays.

The only CLI is a small artificial array test. Actual candidate evaluation and
parameter selection must be invoked by an Actions-only research driver. This
module never calls a geometry evaluator and never mutates a parameter vector.
Its finite cubic-root search is numerical, not a continuous-domain certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

LD = np.longdouble


def exact_delta(new, old):
    value = Fraction.from_float(float(new)) - Fraction.from_float(float(old))
    return value, LD(value.numerator) / LD(value.denominator)


def scalar_record(value):
    if not np.isfinite(value):
        raise ValueError('finite scalar required')
    number = float(value)
    return {'binary64': number, 'exact_binary64_rational': str(Fraction.from_float(number))}


def row_field(values, shape, name):
    values = np.asarray(values, dtype=LD)
    if values.shape == (shape[0],):
        values = values[:, None]
    try:
        answer = np.broadcast_to(values, shape)
    except ValueError as error:
        raise ValueError(name + ' must broadcast to the position sample grid') from error
    if not np.all(np.isfinite(answer)):
        raise ValueError(name + ' contains nonfinite values')
    return answer


def quartic_coefficients(U, T, velocity_column):
    """Ascending coefficients of .5*mean(e(d)^2+2*q(d)^2)."""
    U, T = np.asarray(U, dtype=LD), np.asarray(T, dtype=LD)
    if U.ndim != 3 or U.shape[-1] != 3 or min(U.shape[:2]) < 1 or T.shape != U.shape:
        raise ValueError('Xs and T must have shape (radial,angular,3)')
    if not np.all(np.isfinite(U)) or not np.all(np.isfinite(T)):
        raise ValueError('nonfinite frozen tangent data')
    C = row_field(velocity_column, U.shape[:2], 'velocity column')
    e = np.sum(U * U, axis=-1) - 1
    q = np.sum(U * T, axis=-1)
    p, r, s = 2 * C * U[..., 2], C * C, C * T[..., 2]
    return np.array([
        np.mean(e * e + 2 * q * q) / 2,
        np.mean(e * p + 2 * q * s),
        np.mean(p * p + 2 * e * r + 2 * s * s) / 2,
        np.mean(p * r), np.mean(r * r) / 2], dtype=LD)


def quartic_value(coefficients, delta):
    return np.polynomial.polynomial.polyval(LD(delta), coefficients)


class LinearInterval:
    """Intersect a*d+b>=0 constraints, preserving the tight witnesses."""
    def __init__(self, lower, upper):
        self.lower, self.upper = LD(lower), LD(upper)
        self.lower_witness = {'constraint': 'coefficient_box_lower'}
        self.upper_witness = {'constraint': 'coefficient_box_upper'}
        self.constraints = []
        self.fixed_failures = []

    def add(self, name, a, b):
        a, b = np.broadcast_arrays(np.asarray(a, dtype=LD), np.asarray(b, dtype=LD))
        if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
            raise ValueError('nonfinite linear constraint: ' + name)
        self.constraints.append((name, a.copy(), b.copy()))
        fixed_bad = (a == 0) & (b < 0)
        if np.any(fixed_bad):
            flat = int(np.flatnonzero(fixed_bad)[0])
            self.fixed_failures.append({'constraint': name,
                'index': [int(v) for v in np.unravel_index(flat, a.shape)], 'fixed_margin': float(b.flat[flat])})
        for positive in (True, False):
            mask = a > 0 if positive else a < 0
            if not np.any(mask):
                continue
            indices = np.flatnonzero(mask)
            endpoints = -b.flat[indices] / a.flat[indices]
            j = int(np.argmax(endpoints) if positive else np.argmin(endpoints))
            endpoint, flat = endpoints[j], int(indices[j])
            witness = {'constraint': name, 'index': [int(v) for v in np.unravel_index(flat, a.shape)],
                'a': float(a.flat[flat]), 'b': float(b.flat[flat]), 'delta_boundary': float(endpoint)}
            if positive and endpoint > self.lower:
                self.lower, self.lower_witness = endpoint, witness
            if not positive and endpoint < self.upper:
                self.upper, self.upper_witness = endpoint, witness

    def margins(self, delta):
        answer = {}
        for name, a, b in self.constraints:
            values = a * LD(delta) + b
            flat = int(np.argmin(values))
            answer[name] = {'minimum': float(values.flat[flat]),
                'index': [int(v) for v in np.unravel_index(flat, values.shape)]}
        return answer

    def feasible(self, delta):
        return (not self.fixed_failures and self.lower <= delta <= self.upper
                and all(np.all(a * delta + b >= 0) for _, a, b in self.constraints))

    def record(self):
        return {'lower': float(self.lower), 'upper': float(self.upper),
            'lower_witness': self.lower_witness, 'upper_witness': self.upper_witness,
            'fixed_uncontrollable_failures': self.fixed_failures,
            'empty': bool(self.fixed_failures or self.lower > self.upper),
            'constraints_are_sampled_frozen_array_inequalities': True,
            'roundoff_enclosure_is_not_proved': True}


def choose_height_coefficient(data, velocity_column, primitive_column, *, current_coefficient,
        coefficient_bounds, cap_height, cap_height_gain, minimum_cap_height,
        side=1, ball_radius=None, minimum_signed_height=None):
    """Return a reviewable scalar proposal, without evaluating or mutating a state.

    The cap-height threshold is supplied explicitly by the caller (including
    any chosen numerical margin). Ball and signed-height constraints are
    optional, sampled conditions on this same frozen a,T chart. Strip and
    curvature are untouched by this helper and require the driver's audit.
    """
    X = np.asarray(data['X'], dtype=LD)
    U, T = np.asarray(data['Xs'], dtype=LD), np.asarray(data['T'], dtype=LD)
    if X.ndim != 3 or X.shape[-1] != 3 or U.shape != X.shape or T.shape != X.shape:
        raise ValueError('X, Xs and T must have the same sample-grid vector shape')
    if not np.all(np.isfinite(X)) or side not in (-1, 1):
        raise ValueError('finite positions and side +/-1 required')
    numeric = [current_coefficient, *coefficient_bounds, cap_height,
               cap_height_gain, minimum_cap_height]
    if not all(np.isfinite(v) for v in numeric):
        raise ValueError('finite coefficient and height inputs required')
    current = float(current_coefficient)
    lo, hi = map(float, coefficient_bounds)
    if not lo <= current <= hi:
        raise ValueError('the unchanged input coefficient is outside its declared box')
    I = row_field(primitive_column, X.shape[:2], 'primitive column')
    coefficients = quartic_coefficients(U, T, velocity_column)
    interval = LinearInterval(LD(lo) - LD(current), LD(hi) - LD(current))
    interval.add('cap_height_lower', LD(cap_height_gain), LD(cap_height) - LD(minimum_cap_height))
    if minimum_signed_height is not None:
        if not np.isfinite(minimum_signed_height):
            raise ValueError('finite selected signed-height target required')
        interval.add('signed_height_lower', side * I, side * X[..., 2] - LD(minimum_signed_height))
    if ball_radius is not None:
        if not np.isfinite(ball_radius) or ball_radius <= 0:
            raise ValueError('positive finite ball radius required')
        horizontal_squared = np.sum(X[..., :2] ** 2, axis=-1)
        remaining = LD(ball_radius) ** 2 - horizontal_squared
        interval.add('ball_fixed_horizontal', np.zeros_like(remaining), remaining)
        # A negative radicand is already an explicit uncontrollable failure.
        zlimit = np.sqrt(np.maximum(remaining, 0))
        interval.add('ball_z_lower', I, X[..., 2] + zlimit)
        interval.add('ball_z_upper', -I, zlimit - X[..., 2])
    answer = {'schema': 'single-height-quartic-initialization-proposal-v1',
        'current_coefficient': scalar_record(current), 'coefficient_bounds': [lo, hi],
        'sample_shape': list(X.shape[:2]), 'normalization': '0.5*uniform_mean(e^2+2*q^2)',
        'quartic_coefficients_ascending': [float(v) for v in coefficients],
        'cap_height_input': float(cap_height), 'cap_height_gain_input': float(cap_height_gain),
        'minimum_cap_height_input': float(minimum_cap_height),
        'minimum_signed_height_input': None if minimum_signed_height is None else float(minimum_signed_height),
        'ball_radius_input': None if ball_radius is None else float(ball_radius),
        'side': side, 'interval': interval.record(), 'candidate_table': [],
        'state_mutated': False, 'geometry_evaluated': False,
        'metric_function_a_or_tangent_T_changed': False,
        'original_smooth_shape_objective_is_not_this_quartic': True,
        'continuous_feasibility_or_global_minimum_certified': False,
        'complete_metric_curvature_embedding_reach_gates_paid': False}
    if answer['interval']['empty']:
        answer['status'] = 'no_feasible_sample_interval'
        return answer
    derivative = np.array([(j+1) * coefficients[j+1] for j in range(4)], dtype=LD)
    while len(derivative) > 1 and derivative[-1] == 0:
        derivative = derivative[:-1]
    roots = (np.polynomial.polynomial.polyroots(np.asarray(derivative / np.max(abs(derivative)), float))
             if np.any(derivative) and len(derivative) > 1 else [])
    answer['numerical_derivative_roots'] = [[float(np.real(v)), float(np.imag(v))] for v in roots]
    proposals = [(interval.lower, 'lower_boundary'), (interval.upper, 'upper_boundary')]
    proposals.append((min(max(LD(0), interval.lower), interval.upper), 'closest_to_unchanged'))
    for root in roots:
        if abs(np.imag(root)) <= 1e-8 * max(1., abs(np.real(root))):
            delta = LD(np.real(root))
            if interval.lower <= delta <= interval.upper:
                proposals.append((delta, 'numerical_quartic_stationary_point'))
    seen = set()
    for requested_delta, label in proposals:
        rounded = float(LD(current) + requested_delta)
        # Adjacent binary64 choices let a rounded boundary move inward without
        # clipping a state or pretending the exact threshold was attained.
        for proposed in (rounded, np.nextafter(rounded, -np.inf), np.nextafter(rounded, np.inf)):
            proposed = float(proposed)
            if proposed in seen or not lo <= proposed <= hi:
                continue
            seen.add(proposed)
            rational_delta, delta = exact_delta(proposed, current)
            margin = interval.margins(delta)
            candidate = {'source': label, 'new_coefficient': scalar_record(proposed),
                'exact_coefficient_difference': str(rational_delta),
                'difference_evaluated': float(delta), 'uniform_metric_cost': float(quartic_value(coefficients, delta)),
                'linear_constraint_margins': margin, 'sample_feasible_in_current_arithmetic': bool(interval.feasible(delta))}
            answer['candidate_table'].append(candidate)
    feasible = [v for v in answer['candidate_table'] if v['sample_feasible_in_current_arithmetic']]
    if not feasible:
        answer['status'] = 'no_representable_feasible_candidate_found'
        return answer
    selected = min(feasible, key=lambda v: (v['uniform_metric_cost'], abs(v['difference_evaluated']),
                                            v['new_coefficient']['binary64']))
    answer['selected'] = selected
    answer['status'] = 'finite_numeric_quartic_candidate_search_complete'
    answer['selected_height_predicted'] = float(LD(cap_height) + LD(cap_height_gain) *
        exact_delta(selected['new_coefficient']['binary64'], current)[1])
    answer['driver_must_rebuild_same_chart_and_audit_full_smooth_objective'] = True
    return answer


def developer_check():
    X = np.zeros((2, 4, 3)); X[1, :, 2] = .2
    U = np.zeros_like(X); U[..., 2] = .6
    T = np.zeros_like(X); T[..., 1] = 1
    data = {'X': X, 'Xs': U, 'T': T}
    saved = {k: v.copy() for k, v in data.items()}
    C, I = np.array([.5, .5]), np.array([0., .3])
    coefficients = quartic_coefficients(U, T, C)
    error = LD(0)
    for d in np.linspace(-.5, 1.5, 17):
        changed = np.asarray(U, dtype=LD).copy(); changed[..., 2] += LD(d)*C[:, None]
        direct = np.mean((np.sum(changed*changed, axis=-1)-1)**2 +
                         2*np.sum(changed*T, axis=-1)**2)/2
        error = max(error, abs(direct-quartic_value(coefficients, d)))
    common = dict(current_coefficient=-.5, coefficient_bounds=(-1.,1.),
        cap_height=.1, cap_height_gain=.3, minimum_cap_height=.25, ball_radius=1., minimum_signed_height=0.)
    result = choose_height_coefficient(data, C, I, **common)
    assert result['status'] == 'finite_numeric_quartic_candidate_search_complete'
    assert abs(result['selected']['difference_evaluated']-.8) < 1e-12
    assert result['selected']['sample_feasible_in_current_arithmetic']
    assert all(np.array_equal(data[k], saved[k]) for k in data)
    wrong_height = choose_height_coefficient(data, C, I, **dict(common, minimum_cap_height=5.))
    assert wrong_height['status'] == 'no_feasible_sample_interval'
    outside = {k: v.copy() for k, v in data.items()}; outside['X'][0,0,0] = 1.1
    impossible_ball = choose_height_coefficient(outside, C, I, **common)
    assert impossible_ball['status'] == 'no_feasible_sample_interval'
    negative = LinearInterval(-2,3); negative.add('lower',2,1); negative.add('upper',-1,2)
    assert negative.lower == LD(-.5) and negative.upper == LD(2)
    assert negative.feasible(LD(0)) and not negative.feasible(LD(3))
    fixed = LinearInterval(-1,1); fixed.add('fixed',0,-1)
    assert fixed.record()['empty']
    mirror = {k: v.copy() for k,v in data.items()}
    mirror['X'][...,2] *= -1; mirror['Xs'][...,2] *= -1
    mirrored = choose_height_coefficient(mirror, -C, -I, **dict(common,side=-1))
    assert abs(mirrored['selected']['difference_evaluated']-.8) < 1e-12
    for full_result in (result, wrong_height, impossible_ball, mirrored):
        decoded = json.loads(json.dumps(full_result, allow_nan=False))
        assert decoded['status'] == full_result['status']
    assert error < LD('1e-14')
    return {'schema':'single-height-quartic-artificial-check-v1', 'passed':True,
        'maximum_quartic_vs_direct_array_cost_error':float(error),
        'artificial_expected_interior_delta':.8,
        'selected_delta':result['selected']['difference_evaluated'],
        'infeasible_cap_height_and_fixed_horizontal_ball_rejected':True,
        'both_sides_and_negative_constraint_slopes_checked':True,
        'frozen_input_arrays_unchanged':True, 'actual_candidate_evaluated':False,
        'complete_success_and_failure_reports_JSON_roundtrip_checked':True,
        'actual_coefficient_step_applied':False,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=developer_check()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')


if __name__=='__main__':
    main()
