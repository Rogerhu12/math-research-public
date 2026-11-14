#!/usr/bin/env python3
"""Certified material-weighted means of fixed-seed normal-angle modes.

For rho_raw, the strip |Im(phi)|<=1/20 has |rho_raw|<=r+D: the exponential
argument has imaginary part <=12*sinh(1/10)<pi/2. Trapezoidal Fourier aliases
therefore have an explicit geometric bound. Exact moment corrections and a0
are consumed as intervals from the already completed Taylor-moment report.
This defines accurate zero-material-mean central directions; no BVP is run.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import mpmath as mp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fd2d_weighted_balanced_source', HERE/'fd2d_balanced_oval_core.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def dyadic(parts):
    sign, man, exponent, bits = [int(x) for x in parts]
    if man < 0 or sign not in (0, 1): raise ValueError('Invalid exact endpoint')
    value = Fraction((-1 if sign else 1)*man)
    return value*(2**exponent) if exponent >= 0 else value/Fraction(2**(-exponent))


def to_iv(q):
    return mp.iv.mpf(q.numerator)/q.denominator


def read_interval(record):
    lo, hi = dyadic(record['binary_lower']), dyadic(record['binary_upper'])
    if lo > hi: raise ValueError('Reversed endpoint record')
    return mp.iv.mpf([to_iv(lo).a, to_iv(hi).b])


def encode(value):
    return dict(interval=str(value), binary_lower=[int(x) for x in value._mpi_[0]],
                binary_upper=[int(x) for x in value._mpi_[1]])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--moments', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--count', type=int, default=95)
    p.add_argument('--angular', type=int, default=2048)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Use a new weighted-mean certificate')
    if args.angular % 4 or 2*args.count >= args.angular:
        raise ValueError('Fourfold grid and distinct retained modes required')
    mp.iv.dps = 70
    iv = mp.iv
    started = time.monotonic()
    moments = json.loads(args.moments.read_text())
    if moments['parameters'] != core.PARAMETERS:
        raise ValueError('Exact moment parameters and current fixed seed differ')
    a0, u2, u4 = [read_interval(moments['enclosures'][name]) for name in ('a0', 'u2', 'u4')]
    r, D, c, k = [iv.mpf(core.PARAMETERS[name]) for name in ('r', 'D', 'c', 'k')]
    delta = iv.mpf(1)/20
    imaginary_argument_bound = 2*k*(iv.exp(2*delta)-iv.exp(-2*delta))/2
    if not bool(imaginary_argument_bound < iv.pi/2):
        raise ArithmeticError('Claimed analytic strip was not paid')
    magnitude = r+D
    sums = [iv.mpf(0) for _ in range(args.count)]
    quarter = args.angular//4
    for index in range(quarter+1):
        phi = 2*iv.pi*index/args.angular
        x = iv.cos(2*phi)
        rho = r+D/(1+iv.exp(2*k*(x-c)))
        weight = 2 if index in (0, quarter) else 4
        previous, value = iv.mpf(1), x
        for j in range(1, args.count+1):
            sums[j-1] += weight*rho*value/args.angular
            previous, value = value, 2*x*value-previous
    rows = []
    largest_width = iv.mpf(0)
    for j, raw in enumerate(sums, 1):
        mode = 2*j
        alias_bound = 2*magnitude*iv.exp(-(args.angular-mode)*delta)/(1-iv.exp(-args.angular*delta))
        coefficient = raw+iv.mpf([-1, 1])*alias_bound
        if j == 1: coefficient += u2/2
        if j == 2: coefficient += u4/2
        mean = coefficient/a0
        width = mean.b-mean.a
        if bool(width > largest_width): largest_width = width
        rows.append(dict(j=j, angular_mode=mode, raw_trapezoid=encode(raw),
            alias_absolute_upper=str(alias_bound.b), corrected_fourier_coefficient=encode(coefficient),
            material_weighted_mean=encode(mean), width=str(width)))
    report = dict(schema='fd2d-fixed-normal-material-weighted-means-v1', scope=__doc__,
        source=identity(__file__), provider=identity(HERE/'fd2d_balanced_oval_core.py'),
        exact_moment_report=identity(args.moments), parameters=core.PARAMETERS,
        interval_dps=70, angular=args.angular, evaluated_quarter_nodes=quarter+1,
        strip_halfwidth='1/20', strip_magnitude_upper=str(magnitude.b),
        imaginary_exponent_bound=str(imaginary_argument_bound),
        mean_definition='mu_j=(1/(2*pi*a0))*integral_0^(2*pi) rho_seed(phi)*cos(2*j*phi) dphi',
        exact_direction_definition='psi_j(phi)=cos(2*j*phi)-mu_j; physical u=arc_seed(phi)/a0',
        rows=rows, maximum_mean_interval_width=str(largest_width),
        all_mean_widths_below_1e_16=bool(largest_width < iv.mpf('1e-16')),
        source_moment_precision_preference_met=moments['passed'],
        source_moment_intervals_remain_valid=True,
        BVP_solved=False, seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), seconds=report['seconds'],
        maximum_width=report['maximum_mean_interval_width'],
        all_mean_widths_below_1e_16=report['all_mean_widths_below_1e_16'],
        first_four=[dict(j=row['j'], mean=row['material_weighted_mean']['interval']) for row in rows[:4]],
        highest_alias_bound=rows[-1]['alias_absolute_upper'])), flush=True)


if __name__ == '__main__': main()
