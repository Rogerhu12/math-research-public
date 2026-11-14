#!/usr/bin/env python3
"""Exact all-phase sufficient gates for continuous moving/fixed normal balls.

All input numbers are integers or rational/decimal strings. The certificates
are conditional on the complete continuous position and unit-normal balls.
They never certify a complete surface, embedding, curvature or reach alone.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError('Use exact integers or rational/decimal strings')
    return F(value)


def vector(values):
    if len(values) != 3:
        raise ValueError('A three-dimensional rational centre is required')
    return tuple(map(rational, values))


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def sqrt_upper(value, bits):
    if value < 0:
        raise ValueError('Negative square root')
    numerator_root, denominator_root = isqrt(value.numerator), isqrt(value.denominator)
    if numerator_root*numerator_root == value.numerator and denominator_root*denominator_root == value.denominator:
        return F(numerator_root, denominator_root)
    scale = 1 << bits
    number = isqrt(value.numerator * scale * scale // value.denominator)
    if number * number * value.denominator < value.numerator * scale * scale:
        number += 1
    result = F(number, scale)
    assert result*result >= value
    return result


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for j, value in enumerate(a):
        out[j] += value
    for j, value in enumerate(b):
        out[j] += value
    return trim(out)


def mul(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def scaled(a, value):
    return trim([value*x for x in a])


def remainder(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError('Zero divisor polynomial')
    while a != [0] and len(a) >= len(b):
        shift, coefficient = len(a)-len(b), a[-1]/b[-1]
        for j, value in enumerate(b):
            a[j+shift] -= coefficient*value
        a = trim(a)
    return a


def sign(value):
    return (value > 0) - (value < 0)


def variations(signs):
    signs = [value for value in signs if value]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm(poly):
    poly = trim(poly)
    derivative = trim([F(j)*poly[j] for j in range(1, len(poly))] or [F(0)])
    sequence = [poly]
    if derivative != [0]:
        sequence.append(derivative)
        while True:
            rest = scaled(remainder(sequence[-2], sequence[-1]), F(-1))
            if rest == [0]:
                break
            sequence.append(rest)
    minus = [sign(p[-1]) * (-1)**(len(p)-1) for p in sequence]
    plus = [sign(p[-1]) for p in sequence]
    return dict(sequence=[[str(v) for v in p] for p in sequence],
                signs_minus_infinity=minus, signs_plus_infinity=plus,
                variations_minus_infinity=variations(minus),
                variations_plus_infinity=variations(plus),
                distinct_real_roots=variations(minus)-variations(plus))


def normal_ball_possible(normal, radius):
    return max(F(0), 1-radius)**2 <= dot(normal, normal) <= (1+radius)**2


def evaluate(row, bits):
    p, q = vector(row['moving_position']), vector(row['fixed_position'])
    n, m = vector(row['moving_normal_centre']), vector(row['fixed_normal_centre'])
    ep, eq = rational(row['moving_position_radius']), rational(row['fixed_position_radius'])
    en, em = rational(row['moving_normal_radius']), rational(row['fixed_normal_radius'])
    tau = rational(row['tau'])
    if min(ep, eq, en, em) < 0 or tau <= 0:
        raise ValueError('Require nonnegative radii and positive tau')
    if not normal_ball_possible(n, en) or not normal_ball_possible(m, em):
        raise ValueError('A claimed normal ball cannot contain any unit normal')
    x, y = p[:2], q[:2]
    Jx = (-x[1], x[0])
    delta = q[2]-p[2]
    A = dot(x, x)+dot(y, y)+delta*delta
    B, C = dot(y, x), dot(y, Jx)
    distance_harmonic_upper = sqrt_upper(B*B+C*C, bits)
    dmin2 = max(F(0), A-2*distance_harmonic_upper)
    dmax2 = A+2*distance_harmonic_upper
    dmax = sqrt_upper(dmax2, bits)
    e = ep+eq
    distance_pass = dmin2 >= (2*tau+e)**2
    ncoef = (delta*n[2]-dot(x, n[:2]), dot(y, n[:2]), dot(y, (-n[1], n[0])))
    mcoef = (dot(y, m[:2])+delta*m[2], -dot(x, m[:2]), -dot(Jx, m[:2]))
    endpoints = []
    for label, normal, radius, (d0, dc, ds) in [
            ('moving', n, en, ncoef), ('fixed', m, em, mcoef)]:
        # Use the actual unit normal to bound its product with the position error.
        error = 2*dmax*(e+tau*radius)+2*tau*e
        margins = []
        for orientation in (-1, 1):
            h2 = (B+tau*orientation*dc)**2+(C+tau*orientation*ds)**2
            centre_margin = A-2*tau*orientation*d0-2*sqrt_upper(h2, bits)
            margins.append(dict(sign=orientation, centre_lower=str(centre_margin),
                                continuous_lower=str(centre_margin-error)))
        # |d0 cross n0| > e + eta*dmax excludes a true normal chord at this end.
        cross_threshold = e+radius*dmax
        denominator = [F(1), F(0), F(1)]
        dnum = [A-2*B, -4*C, A+2*B]
        nnum = [d0+dc, 2*ds, d0-dc]
        polynomial = add(add(scaled(mul(denominator, dnum), dot(normal, normal)),
                              scaled(mul(nnum, nnum), F(-1))),
                         scaled(mul(denominator, denominator), -cross_threshold**2))
        pi_margin = dot(normal, normal)*(A+2*B)-(d0-dc)**2-cross_threshold**2
        assert (polynomial[4] if len(polynomial) == 5 else 0) == pi_margin
        root_record = sturm(polynomial)
        quartic_pass = (pi_margin > 0 and polynomial[0] > 0
                        and root_record['distinct_real_roots'] == 0)
        projection_upper = abs(d0)+sqrt_upper(dc*dc+ds*ds, bits)
        decoupled_cross_lower = dot(normal, normal)*dmin2-projection_upper**2-cross_threshold**2
        endpoints.append(dict(endpoint=label, normal_squared=str(dot(normal, normal)),
             normal_projection_coefficients=list(map(str, (d0, dc, ds))),
             normal_chord_error_upper=str(error), signed_margins=margins,
             normal_chord_pass=all(F(v['continuous_lower']) >= 0 for v in margins),
             cross_threshold_upper=str(cross_threshold),
             quartic_ascending_coefficients=list(map(str, polynomial)),
             phase_pi_margin=str(pi_margin), sturm=root_record,
             all_phase_non_normal_pass=quartic_pass,
             decoupled_cross_lower=str(decoupled_cross_lower),
             decoupled_cross_pass=decoupled_cross_lower > 0))
    return dict(name=row.get('name'), exact_input=row, distance_coefficients=list(map(str, (A, B, C))),
                centre_distance_squared_lower=str(dmin2), centre_distance_upper=str(dmax),
                all_phase_continuous_distance_pass=distance_pass,
                endpoints=endpoints,
                all_phase_continuous_normal_chord_pass=all(v['normal_chord_pass'] for v in endpoints),
                all_phase_no_double_normal_pass=any(v['all_phase_non_normal_pass'] for v in endpoints),
                complete_continuous_balls_are_required=True,
                full_surface_certified=False, actual_reach_certified=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--sqrt-bits', type=int, default=128)
    args = ap.parse_args()
    if args.out.exists() or not 16 <= args.sqrt_bits <= 4096:
        raise ValueError('Require a fresh output and 16..4096 dyadic root bits')
    incoming = json.loads(args.input.read_text())
    records = [evaluate(row, args.sqrt_bits) for row in incoming['cases']]
    result = dict(scope=__doc__, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  sqrt_bits=args.sqrt_bits, complete_records=records,
                  all_arithmetic_exact_rational_except_proved_upward_dyadic_roots=True,
                  phase_sampling_used=False, full_surface_certified=False,
                  actual_reach_certified=False)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps([dict(name=r['name'], distance=r['all_phase_continuous_distance_pass'],
                          normal_chord=r['all_phase_continuous_normal_chord_pass'],
                          no_double_normal=r['all_phase_no_double_normal_pass']) for r in records]))


if __name__ == '__main__':
    main()
