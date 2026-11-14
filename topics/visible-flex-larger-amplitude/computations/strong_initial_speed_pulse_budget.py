#!/usr/bin/env python3
"""Exact one-piece background budget for a new positive initial speed pulse.

This creates no prefix/tail BVP or surface.  It preserves the initial radius,
zero initial radial speed, initial acceleration k0, total radius increase
delta, and final radial speed V with zero final acceleration.  A pulse of
height b shortens the meridian segment.  Exact rational interval Bernstein
bounds certify only this surface-of-revolution background piece, not the
deformed actual field, its global diameter, reach, or a continuation branch.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import time

SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def I(x): return (x, x)
def add(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[1], -a[0])
def mul(a, b):
    q = [x*y for x in a for y in b]
    return (min(q), max(q))
def scale(a, x): return mul(a, I(x))
def poly_add(a, b):
    return [add(a[i] if i < len(a) else I(F(0)),
                b[i] if i < len(b) else I(F(0))) for i in range(max(len(a), len(b)))]
def poly_mul(a, b):
    out = [I(F(0)) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] = add(out[i+j], mul(x, y))
    return out
def derivative(a): return [scale(a[i], F(i)) for i in range(1, len(a))]


def bernstein(power):
    n = len(power)-1
    return [sum_intervals(scale(power[j], F(math.comb(k, j), math.comb(n, j)))
        for j in range(k+1)) for k in range(n+1)]


def sum_intervals(values):
    out = I(F(0))
    for value in values: out = add(out, value)
    return out


def halves(values):
    level, left, right = list(values), [values[0]], [values[-1]]
    while len(level) > 1:
        level = [scale(add(a, b), F(1, 2)) for a, b in zip(level, level[1:])]
        left.append(level[0]); right.append(level[-1])
    return left, list(reversed(right))


def positive_certificate(values, max_depth=14):
    stack, accepted = [(0, 0, values)], []
    while stack:
        depth, index, coefficients = stack.pop()
        lower = min(v[0] for v in coefficients)
        upper = max(v[1] for v in coefficients)
        if lower > 0:
            accepted.append(dict(depth=depth, index=index, lower=str(lower)))
        elif upper < 0:
            return dict(passed=False, negative_interval=dict(depth=depth, index=index,
                upper=str(upper)), meaning='Proved negative on this parameter interval')
        elif depth == max_depth:
            return dict(passed=False, unresolved_interval=dict(depth=depth, index=index),
                meaning='No positivity conclusion from the specified subdivision')
        else:
            a, b = halves(coefficients)
            stack.append((depth+1, 2*index+1, b))
            stack.append((depth+1, 2*index, a))
    return dict(passed=True, all_closed_parameter_intervals_covered=True,
        leaves=accepted, lower=min(float(F(row['lower'])) for row in accepted))


def sqrt_interval(x, bits=80):
    if x < 0: raise ValueError('Negative radicand')
    q = math.isqrt((x.numerator << (2*bits))//x.denominator)
    lower = F(q, 1 << bits)
    upper = lower if lower*lower == x else F(q+1, 1 << bits)
    return lower, upper


def height_interval(speed_bernstein, S, V, b, levels=8):
    blocks = [speed_bernstein]
    for _ in range(levels): blocks = [part for item in blocks for part in halves(item)]
    lower = upper = F(0)
    for coefficients in blocks:
        lo = max(F(0), min(v[0] for v in coefficients))
        hi = min(V+b, max(v[1] for v in coefficients))
        if not 0 <= lo <= hi < 1: raise ValueError('Speed interval left its proved positive domain')
        lower += sqrt_interval(1-hi*hi)[0]
        upper += sqrt_interval(1-lo*lo)[1]
    return S[0]*lower/(1 << levels), S[1]*upper/(1 << levels)


def one(delta, V, k0, b):
    c = V/2+F(16, 35)*b
    lo, hi = F(0), 2*delta/c
    h = lambda s: k0*s*s/12+c*s-delta
    for _ in range(100):
        mid = (lo+hi)/2
        if h(mid) > 0: hi = mid
        else: lo = mid
    assert h(lo) <= 0 <= h(hi) and lo > 0 and hi*k0 <= 3*V and V+b < 1
    S, z = (lo, hi), scale((lo, hi), k0)
    speed = [I(F(0)), z, add(I(3*V), scale(z, F(-2))),
        add(z, I(-2*V+64*b)), I(-192*b), I(192*b), I(-64*b)]
    q = poly_add([I(F(1))], [neg(a) for a in poly_mul(speed, speed)])
    q = [scale(mul(mul(S, S), a), F(64)) for a in q]
    q = poly_add(q, [neg(a) for a in poly_mul(derivative(speed), derivative(speed))])
    certificate = positive_certificate(bernstein(q))
    H = height_interval(bernstein(speed), S, V, b)
    sf = float((lo+hi)/2)
    def v(t): return float(k0)*sf*t+(3*float(V)-2*float(k0)*sf)*t*t+(float(k0)*sf-2*float(V))*t**3+float(b)*64*t**3*(1-t)**3
    def dv(t): return float(k0)*sf+2*(3*float(V)-2*float(k0)*sf)*t+3*(float(k0)*sf-2*float(V))*t*t+float(b)*192*t*t*(1-t)**2*(1-2*t)
    sample = [(t/8192, v(t/8192)) for t in range(8193)]
    curvature = max((abs(dv(t))/(sf*math.sqrt(1-w*w)), t) for t, w in sample)
    return dict(pulse_height=str(b), exact_S_bracket=[str(lo), str(hi)],
        exact_S_root_equation='k0*S^2/12 + (V/2+16*b/35)*S - delta = 0',
        S_midpoint=sf, speed_uniform_bound=float(V+b), speed_sample_max=max(w for _, w in sample),
        meridian_curvature_sample_max=curvature[0], curvature_sample_arg_t=curvature[1],
        radius_minimum_proved=1, parallel_curvature_upper_proved=1,
        meridian_curvature_below_8_certificate=certificate,
        certificate_polynomial='64*S^2*(1-v(t)^2) - (dv/dt)^2',
        certificate_polynomial_power_intervals=[[str(a), str(b)] for a, b in q],
        exact_height_interval=[str(H[0]), str(H[1])],
        height_interval_float=[float(H[0]), float(H[1])], height_panels=256,
        height_and_speed_bounds_cover_closed_t_interval=True, new_physical_metric=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted-reference', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists(): raise FileExistsError('Use a fresh budget record')
    start = time.monotonic()
    raw = args.accepted_reference.read_bytes()
    reference = json.loads(gzip.decompress(raw) if args.accepted_reference.suffix == '.gz' else raw)
    if not reference.get('solver_success') or reference.get('audit_pending', True):
        raise ValueError('An accepted profile is required for this design comparison')
    cfg = reference['frozen_profile']
    delta, V, k0 = [F.from_float(float(cfg[name])) for name in ('delta', 'vu', 'start_acceleration')]
    rows = [one(delta, V, k0, b) for b in (F(0), F(1, 5), F(7, 20), F(1, 2), F(3, 5))]
    H0 = [F(x) for x in rows[0]['exact_height_interval']]
    for row in rows:
        H = [F(x) for x in row['exact_height_interval']]
        row['initial_height_reduction_interval'] = [float(H0[0]-H[1]), float(H0[1]-H[0])]
    report = dict(scope=__doc__, source_sha256_at_start=SELF_SHA,
        accepted_reference=str(args.accepted_reference), accepted_reference_sha256=hashlib.sha256(raw).hexdigest(),
        physical_parameters=dict(delta=str(delta), V=str(V), k0=str(k0)),
        formula='v(t)=k0*S*t+(3*V-2*k0*S)*t^2+(k0*S-2*V)*t^3+b*64*t^3*(1-t)^3',
        exact_radial_increment='S*integral_0^1(v)=delta by the exact positive root equation',
        retained_endpoint_data=dict(radius_start=1, radial_speed_start=0,
            radial_acceleration_start=str(k0), radius_end='1+delta',
            radial_speed_end=str(V), radial_acceleration_end=0),
        higher_endpoint_jets_not_claimed_equal_after_changing_S=True,
        monotone_speed_not_assumed=True,
        rho_core_R7_initial_k0_unchanged=True, rows=rows,
        background_piece_only=True, actual_complete_field_or_BVP_evaluations=0,
        true_tail_workers=0, global_D_or_reach_not_certified=True,
        physical_core_controls_must_be_resolved_in_a_new_actual_BVP=True,
        seconds=time.monotonic()-start)
    with args.out.open('x') as stream: json.dump(report, stream, indent=2); stream.write('\n')
    print(json.dumps(dict(out=str(args.out), seconds=report['seconds'], rows=[{k: r[k] for k in (
        'pulse_height', 'S_midpoint', 'height_interval_float', 'initial_height_reduction_interval',
        'speed_sample_max', 'meridian_curvature_sample_max')}|{'kappa8_certified':r[
        'meridian_curvature_below_8_certificate']['passed']} for r in rows])), flush=True)


if __name__ == '__main__':
    main()
