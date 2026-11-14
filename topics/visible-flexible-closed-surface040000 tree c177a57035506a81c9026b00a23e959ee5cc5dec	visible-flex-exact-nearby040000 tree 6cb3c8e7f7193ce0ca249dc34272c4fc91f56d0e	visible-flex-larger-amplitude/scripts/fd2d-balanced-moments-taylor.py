#!/usr/bin/env python3
"""Tight interval moments of the exact R118 balanced oval.

Each moment is integrated by a composite midpoint Taylor polynomial with an
interval enclosure of its full-cell derivative remainder. No unvalidated
quadrature error estimate is used. The original ellipse a0 is enclosed by a
positive rational binomial series and an explicit geometric tail bound.
This tightens definition constants only; it does not solve the strong BVP.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time
import mpmath as mp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fd2d_balanced_exact_constants', HERE/'fd2d_balanced_oval_core.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def to_iv(q):
    q = Fraction(q)
    return mp.iv.mpf(q.numerator)/q.denominator


def ellipse_a0(terms):
    q, C, b, total = Fraction(9, 19), Fraction(19, 20), Fraction(1), Fraction(1)
    for j in range(1, terms+1):
        b *= q*Fraction(2*j-3, 2*j)
        total += b*b
    next_b = b*q*Fraction(2*terms-1, 2*(terms+1))
    lower = C*total
    tail = C*next_b*next_b/(1-q*q)
    upper = lower+tail
    interval = mp.iv.mpf([to_iv(lower).a, to_iv(upper).b])
    return interval, dict(terms=terms, q='9/19', C='19/20',
        exact_lower_numerator=str(lower.numerator), exact_lower_denominator=str(lower.denominator),
        exact_tail_numerator=str(tail.numerator), exact_tail_denominator=str(tail.denominator),
        geometric_tail_interval=str(to_iv(tail)))


def trig_jet(x, order, frequency=1):
    si, co = mp.iv.sin(frequency*x), mp.iv.cos(frequency*x)
    ss, cc, factor = [], [], Fraction(1)
    for j in range(order+1):
        if j: factor *= Fraction(frequency, j)
        scale = to_iv(factor)
        ss.append((si, co, -si, -co)[j % 4]*scale)
        cc.append((co, -si, -co, si)[j % 4]*scale)
    return ss, cc


def multiply(a, b):
    zero = mp.iv.mpf(0)
    return [sum((a[j]*b[n-j] for j in range(n+1)), zero) for n in range(len(a))]


def exp_jet(a):
    result = [mp.iv.exp(a[0])]
    for n in range(1, len(a)):
        result.append(sum((j*a[j]*result[n-j] for j in range(1, n+1)), mp.iv.mpf(0))/n)
    return result


def reciprocal_jet(a):
    result = [1/a[0]]
    for n in range(1, len(a)):
        result.append(-result[0]*sum((a[j]*result[n-j] for j in range(1, n+1)), mp.iv.mpf(0)))
    return result


def moment_jets(x, order, parameters):
    r, D, c, k = [mp.iv.mpf(parameters[name]) for name in ('r', 'D', 'c', 'k')]
    si, co = trig_jet(x, order)
    _, double_co = trig_jet(x, order, 2)
    exponent = [2*k*v for v in double_co]
    exponent[0] -= 2*k*c
    denominator = exp_jet(exponent)
    denominator[0] += 1
    logistic = reciprocal_jet(denominator)
    rho = [D*v for v in logistic]
    rho[0] += r
    return rho, multiply(rho, si), multiply(rho, co)


def interval_data(value):
    # Keep exact internal dyadic endpoints as well as human-readable decimals.
    return dict(interval=str(value), binary_lower=[int(x) for x in value._mpi_[0]],
                binary_upper=[int(x) for x in value._mpi_[1]])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--cells', type=int, default=128)
    p.add_argument('--order', type=int, default=24)
    p.add_argument('--dps', type=int, default=70)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Use a new exact-constant certificate')
    if args.order < 4 or args.order % 2 or args.cells < 8:
        raise ValueError('An even Taylor order and at least eight cells are required')
    mp.iv.dps = args.dps
    iv = mp.iv
    started = time.monotonic()
    provider = identity(HERE/'fd2d_balanced_oval_core.py')
    a0, a0_proof = ellipse_a0(96)
    L, half = iv.pi/2, iv.pi/(4*args.cells)
    totals = [iv.mpf(0) for _ in range(3)]
    remainders = [iv.mpf(0) for _ in range(3)]
    for cell in range(args.cells):
        center = (2*cell+1)*half
        point = moment_jets(center, args.order-1, core.PARAMETERS)
        whole = moment_jets(center+iv.mpf([-1, 1])*half, args.order, core.PARAMETERS)
        for which in range(3):
            polynomial = sum((2*point[which][j]*half**(j+1)/(j+1)
                              for j in range(0, args.order, 2)), iv.mpf(0))
            remainder = whole[which][args.order]*2*half**(args.order+1)/(args.order+1)
            totals[which] += polynomial+remainder
            remainders[which] += abs(remainder)
    I0, Is, Ic = totals
    A, B = iv.mpf(core.PARAMETERS['A']), iv.mpf(core.PARAMETERS['B'])
    da, db = A-Is, B-Ic
    u0 = a0-I0/L
    u2 = iv.mpf('1.5')*(db-da)
    u4 = -iv.mpf('7.5')*(da+db-2*u0)
    enclosures = dict(a0=a0, raw_radius_integral=I0,
        raw_radius_sin_integral=Is, raw_radius_cos_integral=Ic,
        u0=u0, u2=u2, u4=u4)
    widths = {key: value.b-value.a for key, value in enclosures.items()}
    threshold = iv.mpf('1e-24')
    checks = {key: bool(width < threshold) for key, width in widths.items()}
    if provider != identity(HERE/'fd2d_balanced_oval_core.py'):
        raise RuntimeError('Actual definition provider changed during integration')
    report = dict(schema='fd2d-balanced-oval-tight-moment-intervals-v1', scope=__doc__,
        source=identity(__file__), provider=provider, parameters=core.PARAMETERS,
        cells=args.cells, taylor_order=args.order, interval_dps=args.dps,
        ellipse_positive_rational_series=a0_proof,
        enclosures={key: interval_data(value) for key, value in enclosures.items()},
        widths={key: str(value) for key, value in widths.items()},
        sum_absolute_integral_remainders=[str(value) for value in remainders],
        requested_width='1e-24', width_checks=checks, passed=all(checks.values()),
        whole_surface_proved=False, seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), seconds=report['seconds'], passed=report['passed'],
        widths=report['widths'], enclosures={key: str(value) for key, value in enclosures.items()})), flush=True)
    if not report['passed']: raise SystemExit(1)


if __name__ == '__main__': main()
