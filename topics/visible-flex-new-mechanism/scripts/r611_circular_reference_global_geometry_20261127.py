#!/usr/bin/env python3
"""Outward interval geometry of the actual R582 circular reference.

New scientific scope: complete compact meridian two-jets, combined with the
analytic infinite-tail theorem R608. No seed, optimization, or old positive
chart is rerun. Scientific execution is restricted to its public Actions job.
"""
import argparse
from collections import defaultdict
from decimal import Decimal, localcontext
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import r582_continuous_mean_profile_20261126 as original

I = original.Interval
down, up = original.down, original.up
exp_i, sin_i = original.exp_interval, original.sin_interval
L, C, ELL = original.LENGTH, original.CORE_END, original.ELL
RC, AMP = original.RC, original.AMP
BACKGROUND_END = original.BACKGROUND_END
CONTROL_LEFT, CONTROL_RIGHT = original.CONTROL_LEFT, original.CONTROL_RIGHT
KNOTS, Q = original.KNOTS, original.SOURCE_Q
SCHEMA = 'r611-actual-circular-reference-full-compact-interval-geometry-v1'


def emit(tag, data):
    print('CIRCLE_GLOBAL_' + tag + ' ' + json.dumps(
        data, sort_keys=True, separators=(',', ':'), allow_nan=False), flush=True)


def hull_abs(x):
    return I(0 if x.lo <= 0 <= x.hi else min(abs(x.lo), abs(x.hi)),
             max(abs(x.lo), abs(x.hi)))


def sqrt_i(x):
    if x.lo < 0:
        raise ArithmeticError('negative interval square root')
    with localcontext() as ctx:
        ctx.prec = 90
        low = Decimal.from_float(x.lo).sqrt()
        high = Decimal.from_float(x.hi).sqrt()
        gl = abs(low) * Decimal('1e-70') + Decimal('1e-320')
        gh = abs(high) * Decimal('1e-70') + Decimal('1e-320')
        return I(max(0., down(float(max(Decimal(0), low - gl)))),
                 up(float(high + gh)))


def cos_i(x):
    # The inherited sine endpoint proof applies to arguments below 1200.
    # pi/2 is enclosed before the shift, not rounded to an exact constant.
    with localcontext() as ctx:
        ctx.prec = 90
        half = original.DECIMAL_PI / 2
        guard = Decimal('1e-70')
        pi_half = I(down(float(half - guard)), up(float(half + guard)))
    return sin_i(x + pi_half)


def step_jets(s, left, right):
    width = I(right) - left
    if s.hi <= left:
        return I(0), I(0), I(0), I(0)
    if s.lo >= right:
        return I(1), I(0), I(0), I(0)
    x = (s - left) / width
    x = I(max(0., x.lo), min(1., x.hi))
    if x.lo <= 0 or x.hi >= 1:
        reflected = x.hi >= 1
        if reflected:
            xx = 1 - x
            x = I(max(0., xx.lo), min(1., xx.hi))
        if x.hi > .125:
            raise ArithmeticError('step endpoint requires subdivision')
        h = I(x.hi)
        b = exp_i(-1 / h + 1 / (1 - h))
        ell1 = h ** -2 + (1 - h) ** -2
        ell2_abs = 2 * h ** -3 + 2 * (1 - h) ** -3
        first = b * ell1 / width
        second = b * (ell1 ** 2 + ell2_abs) / width ** 2
        value = I(0, min(1., b.hi))
        return ((1 - value) if reflected else value,
                I(0, min(.25, b.hi)), I(0, first.hi), I(-second.hi, second.hi))
    chi, product, first = original._step_x_intervals(x, width)
    ell1 = (x ** -2 + (1 - x) ** -2) / width
    ell2 = (-2 * x ** -3 + 2 * (1 - x) ** -3) / width ** 2
    second = product * (ell2 + (1 - 2 * chi) * ell1 ** 2)
    return chi, product, first, second


def bump_jets(s):
    width = I(CONTROL_RIGHT) - CONTROL_LEFT
    if s.hi <= CONTROL_LEFT or s.lo >= CONTROL_RIGHT:
        return I(0), I(0), I(0)
    x = (s - CONTROL_LEFT) / width
    x = I(max(0., x.lo), min(1., x.hi))
    if x.lo <= 0 or x.hi >= 1:
        reflected = x.hi >= 1
        if reflected:
            xx = 1 - x
            x = I(max(0., xx.lo), min(1., xx.hi))
        if x.hi > .125:
            raise ArithmeticError('bump endpoint requires subdivision')
        h = I(x.hi)
        # Dropping exp(-1/(1-x)) gives a valid upper bound, including
        # its derivatives by the displayed positive polynomial majorants.
        b = exp_i(4 - 1 / h)
        ell1_abs = h ** -2 + (1 - h) ** -2
        ell2_abs = 2 * h ** -3 + 2 * (1 - h) ** -3
        first = b * ell1_abs / width
        second = b * (ell1_abs ** 2 + ell2_abs) / width ** 2
        return I(0, min(1., b.hi)), I(-first.hi, first.hi), I(-second.hi, second.hi)
    value = exp_i(4 - 1 / x - 1 / (1 - x))
    ell1 = (x ** -2 - (1 - x) ** -2) / width
    ell2 = (-2 * x ** -3 - 2 * (1 - x) ** -3) / width ** 2
    return value, value * ell1, value * (ell2 + ell1 ** 2)


def derivative_spline(knots, coefficients, degree):
    dc = [degree * (coefficients[j + 1] - coefficients[j]) /
          (I(knots[j + degree + 1]) - knots[j + 1])
          for j in range(len(coefficients) - 1)]
    return knots[1:-1], dc, degree - 1


class CompactGeometry:
    def __init__(self, state, deadline, counts, height_target, max_height_cells):
        self.mu, self.nu = I(state['mu']), I(state['nu'])
        self.deadline, self.counts = deadline, counts
        self.height = original.ValidatedTailHeight(
            deadline, counts, height_width_target=height_target,
            maximum_cells=max_height_cells)
        self.width = I(L) - C
        self.fields = []
        for coeffs in (Q[64:72], Q[72:80]):
            item = (KNOTS, [I(v) for v in coeffs], 5)
            jets = [item]
            for _ in range(2):
                item = derivative_spline(*item)
                jets.append(item)
            self.fields.append(jets)

    def check(self):
        if time.monotonic() >= self.deadline:
            raise original.ClockCheckpoint('full compact interval geometry checkpoint')

    def spline_jets(self, s, index):
        x = (s - C) / self.width
        x = I(max(0., x.lo), min(1., x.hi))
        values = []
        for k, (knots, coeffs, degree) in enumerate(self.fields[index]):
            values.append(original.spline_interval(x, knots, coeffs, degree) / self.width ** k)
        return values

    def jets(self, left, right):
        self.check()
        self.counts['complete_two_jet_cells'] += 1
        s = I(left, right)
        bg, _, bg1, bg2 = step_jets(s, C, BACKGROUND_END)
        chi, product, chi1, chi2 = step_jets(s, C, L)
        beta = 4 * product
        beta1 = 4 * chi1 * (1 - 2 * chi)
        beta2 = 4 * chi2 * (1 - 2 * chi) - 8 * chi1 ** 2
        fields = []
        for k in (0, 1):
            p, p1, p2 = self.spline_jets(s, k)
            fields.append((beta * p, beta1 * p + beta * p1,
                           beta2 * p + 2 * beta1 * p1 + beta * p2))
        psi, psi1, psi2 = bump_jets(s)
        alpha, alpha1, alpha2 = [v + self.mu * b for v, b in zip(fields[0], (psi, psi1, psi2))]
        correction, correction1, correction2 = [v + self.nu * b for v, b in zip(fields[1], (psi, psi1, psi2))]
        r0 = I(RC) + L - s
        acore = I(original.CIRCLE_RADIUS)
        abase = (1 - bg) * acore + bg * r0
        abase1 = bg1 * (r0 - acore) - bg
        abase2 = bg2 * (r0 - acore) - 2 * bg1
        ea = exp_i(alpha)
        a = ea * abase
        a1 = ea * (abase1 + abase * alpha1)
        a2 = ea * (abase2 + 2 * abase1 * alpha1 + abase * (alpha2 + alpha1 ** 2))
        delta = (L - s) / ELL
        phase = delta ** -2
        w = AMP * exp_i(-(2 - sin_i(phase)) / delta)
        ws = -w * ((2 - sin_i(phase)) / delta ** 2 - 2 * cos_i(phase) / delta ** 4) / ELL
        H = self.height.height(s)
        central = original.CORE_HALF + s
        tail = float(Q[-1]) + H
        z = (1 - bg) * central + bg * tail + correction
        z1 = 1 - bg + bg1 * (tail - central) + bg * w + correction1
        z2 = -2 * bg1 + bg2 * (tail - central) + 2 * bg1 * w + bg * ws + correction2
        speed2 = a1 ** 2 + z1 ** 2
        if speed2.lo <= 0:
            raise ArithmeticError('speed lower bound unresolved')
        speed = sqrt_i(speed2)
        curvature = hull_abs(a1 * z2 - z1 * a2) / (speed2 * speed)
        return {'a': a, 'a_s': a1, 'a_ss': a2, 'z': z, 'z_s': z1,
                'z_ss': z2, 'speed': speed, 'curvature': curvature}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-state-json', required=True)
    p.add_argument('--source-state-sha256', required=True)
    p.add_argument('--maximum-seconds', type=float, default=2400)
    p.add_argument('--maximum-cells', type=int, default=100000)
    p.add_argument('--maximum-depth', type=int, default=28)
    p.add_argument('--height-width-target', type=float, default=1e-6)
    p.add_argument('--height-maximum-cells', type=int, default=65536)
    args = p.parse_args()
    raw = sys.stdin.buffer.read() if args.source_state_json == '@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest() != args.source_state_sha256:
        raise ValueError('declared reference state changed')
    state = json.loads(raw)
    if state['mu'] != -0.040019082162222074 or state['nu'] != -0.048942275258064924:
        raise ValueError('this scope is the identified actual circular reference')
    if state['target_reach_decimal'] != '0.06072':
        raise ValueError('target reach changed')
    started = time.monotonic()
    counts = defaultdict(int)
    curve = CompactGeometry(state, started + args.maximum_seconds, counts,
                            args.height_width_target, args.height_maximum_cells)
    target_tau = I(6072) / 100000
    target_k = 1 / target_tau
    # The upper endpoint overlaps the exact R608 tail start; no rounded gap.
    tail_start = I(L) - I(ELL) * 2 / 25
    compact_end = up(tail_start.hi)
    points = {C, compact_end, BACKGROUND_END, CONTROL_LEFT, CONTROL_RIGHT}
    for k in range(1, 65):
        points.add(C + (compact_end - C) * k / 65)
    for knot in (1 / 3, 2 / 3):
        points.add(C + (L - C) * knot)
    points = sorted(x for x in points if C <= x <= compact_end)
    stack = [(a, b, 0) for a, b in zip(points[:-1], points[1:])]
    accepted = 0
    examined = 0
    unresolved = []
    digest = hashlib.sha256()
    extrema = {'a_min': math.inf, 'a_max': -math.inf,
               'z_s_min': math.inf, 'speed_min': math.inf, 'curvature_max': 0.}
    peak = None
    failure = None
    emit('DEFINITION', {'schema': SCHEMA, 'source_state_sha256': args.source_state_sha256,
        'source_state': state, 'compact_interval': [C, compact_end],
        'exact_tail_start_enclosure': [tail_start.lo, tail_start.hi],
        'continuous_tail_theorem': 'R608', 'global_reach_theorem': 'R599',
        'new_seed_calls': 0, 'new_ODE_calls': 0, 'new_optimizer_calls': 0,
        'same_analytic_profile_exact_binary64_constants_and_exact_endpoint_differences': True,
        'scientific_scope_is_new_complete_compact_two_jets_not_old_positive_chart_replay': True})
    try:
        while stack:
            curve.check()
            left, right, depth = stack.pop()
            examined += 1
            row = None
            reason = None
            try:
                row = curve.jets(left, right)
                good = (row['a'].lo >= RC and row['z_s'].lo > 0
                        and row['curvature'].hi <= target_k.lo)
                reason = 'radius/height-derivative/curvature enclosure not sufficient'
            except ArithmeticError as exc:
                good, reason = False, str(exc)
            if good:
                accepted += 1
                record = [left, right, {k: [v.lo, v.hi] for k, v in row.items()}]
                digest.update((json.dumps(record, sort_keys=True, separators=(',', ':')) + '\n').encode())
                extrema['a_min'] = min(extrema['a_min'], row['a'].lo)
                extrema['a_max'] = max(extrema['a_max'], row['a'].hi)
                extrema['z_s_min'] = min(extrema['z_s_min'], row['z_s'].lo)
                extrema['speed_min'] = min(extrema['speed_min'], row['speed'].lo)
                if row['curvature'].hi > extrema['curvature_max']:
                    extrema['curvature_max'] = row['curvature'].hi
                    peak = [left, right]
                continue
            if depth >= args.maximum_depth or examined >= args.maximum_cells:
                unresolved.append({'interval': [left, right], 'depth': depth,
                    'reason': reason, 'jets': None if row is None else {
                        k: [v.lo, v.hi] for k, v in row.items()}})
                failure = 'declared_interval_capacity_reached'
                break
            middle = left + (right - left) / 2
            if middle in (left, right):
                raise ArithmeticError('interval bisection lost resolution')
            stack.extend(((left, middle, depth + 1), (middle, right, depth + 1)))
            if examined % 1000 == 0:
                emit('PROGRESS', {'examined': examined, 'accepted': accepted,
                    'pending': len(stack), 'seconds': time.monotonic() - started})
    except (original.ClockCheckpoint, ArithmeticError) as exc:
        failure = type(exc).__name__ + ': ' + str(exc)
    success = failure is None and not stack and not unresolved
    clean_extrema = {k: (v if math.isfinite(v) else None) for k, v in extrema.items()}
    diameter = ratio = None
    if success:
        # R608: tail a<.237; exact core radius is .38; caps radius is .22.
        ar = max(extrema['a_max'], original.CIRCLE_RADIUS, .237)
        diameter = 2 * sqrt_i(I(ar) ** 2 + I(float(Q[-1])) ** 2)
        ratio = target_tau / diameter
    emit('FINAL', {'schema': SCHEMA, 'success': success, 'failure': failure,
        'complete_compact_interval_verified': success,
        'complete_closed_circular_reference_reach_established': success,
        'reach_lower_decimal_if_complete': '0.06072' if success else None,
        'reference_diameter_upper': None if diameter is None else diameter.hi,
        'reference_reach_over_diameter_lower': None if ratio is None else ratio.lo,
        'examined_cells': examined, 'accepted_cells': accepted,
        'pending_cells': len(stack), 'pending_extent': None if not stack else
            [min(x[0] for x in stack), max(x[1] for x in stack)],
        'first_unresolved': unresolved, 'accepted_leaf_stream_sha256': digest.hexdigest(),
        'accepted_leaf_tables_saved': False, 'compact_extrema': clean_extrema,
        'curvature_upper_attaining_cell': peak,
        'height_integral_receipt': getattr(curve.height, 'receipt', None),
        'counts': dict(counts), 'new_scientific_seconds': time.monotonic() - started,
        'noncircular_reach_established': False, 'fixed_metric_family_established': False,
        'README_complete': False})
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
