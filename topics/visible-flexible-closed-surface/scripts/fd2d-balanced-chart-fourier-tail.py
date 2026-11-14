#!/usr/bin/env python3
"""Strict C4 tail budgets for the unchanged exact balanced material chart.

The input interval means enclose the exact coefficients. The finite reference
polynomial uses the EXACT rational midpoint of each dyadic interval. No BVP,
new central shape, or physical metric is defined by this calculation.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, math
from fractions import Fraction
from pathlib import Path
import mpmath as mp


def identity(path):
    path = Path(path)
    data = path.read_bytes()
    return dict(file=path.name, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def read_json(path):
    path = Path(path)
    data = path.read_bytes()
    if path.suffix == '.gz':
        data = gzip.decompress(data)
    return json.loads(data), data


def dyadic(parts):
    sign, man, exponent, bits = map(int, parts)
    if sign not in (0, 1) or man < 0:
        raise ValueError('Invalid exact interval endpoint')
    value = Fraction((-1 if sign else 1)*man)
    return value*2**exponent if exponent >= 0 else value/Fraction(2**(-exponent))


def as_iv(q):
    q = Fraction(q)
    return mp.iv.mpf(q.numerator)/q.denominator


def endpoints(record):
    a, b = dyadic(record['binary_lower']), dyadic(record['binary_upper'])
    if a > b:
        raise ValueError('Reversed coefficient interval')
    return a, b


def encode(v):
    return dict(interval=str(v), binary_lower=list(map(int, v._mpi_[0])),
                binary_upper=list(map(int, v._mpi_[1])))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--means', type=Path, required=True)
    p.add_argument('--moments', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new chart-tail report')
    means, means_raw = read_json(args.means)
    moments, moments_raw = read_json(args.moments)
    if means['exact_moment_report']['sha256'] != hashlib.sha256(moments_raw).hexdigest():
        raise ValueError('The means bind a different exact moment packet')
    if means['parameters'] != moments['parameters']:
        raise ValueError('The exact seed parameters disagree')
    if not means['source_moment_intervals_remain_valid']:
        raise ValueError('The input does not assert valid moment enclosures')
    J = len(means['rows'])
    if J < 2 or [v['j'] for v in means['rows']] != list(range(1, J+1)):
        raise ValueError('Need consecutive exact even angular modes, including the moment corrections')
    mp.iv.dps = 80
    iv = mp.iv
    a0_lo, a0_hi = endpoints(moments['enclosures']['a0'])
    a0 = iv.mpf([as_iv(a0_lo).a, as_iv(a0_hi).b])
    M = (iv.mpf(means['parameters']['r'])+iv.mpf(means['parameters']['D']))/a0
    delta = iv.mpf(1)/20
    r = iv.exp(-2*delta)
    first = J+1
    first_power = iv.exp(-2*first*delta)
    standard_sums = [1/(1-r), r/(1-r)**2, r*(1+r)/(1-r)**3,
                     r*(1+4*r+r*r)/(1-r)**4]
    radii = [(endpoints(row['material_weighted_mean'])[1]-
              endpoints(row['material_weighted_mean'])[0])/2 for row in means['rows']]
    rows = []
    for k in range(5):
        if k == 0:
            tail = M*first_power*standard_sums[0]/first
            finite = sum((e/Fraction(j) for j, e in enumerate(radii, 1)), Fraction(0))
        else:
            power = k-1
            shifted_sum = sum(math.comb(power, q)*first**(power-q)*standard_sums[q]
                              for q in range(power+1))
            tail = 2**k*M*first_power*shifted_sum
            finite = sum((2**k*j**power*e for j, e in enumerate(radii, 1)), Fraction(0))
        rows.append(dict(derivative_order=k, omitted_modes_uniform_bound=encode(tail),
                         finite_interval_midpoint_error=encode(as_iv(finite)),
                         total_uniform_error=encode(tail+as_iv(finite))))
    report = dict(schema='fd2d-exact-balanced-material-chart-C4-Fourier-tail-v1',
                  scope=__doc__, source=identity(__file__), means=identity(args.means),
                  means_uncompressed_sha256=hashlib.sha256(means_raw).hexdigest(),
                  moments=identity(args.moments), retained_even_modes=J,
                  exact_chart='U(phi)=phi+sum_{j>=1}(mu_j/j)*sin(2*j*phi)',
                  reference_polynomial='Use the exact rational midpoint of every input dyadic coefficient interval; no rounding is hidden',
                  coefficient_strip_bound='|mu_j| <= ((r+D)/a0)*exp(-2*j/20) for j>2',
                  strip_halfwidth='1/20', first_omitted_j=first, interval_dps=80, rows=rows,
                  original_95_mean_packet_unchanged=True, physical_metric_changed=False,
                  nonlinear_core_solved=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(args.out), rows=[dict(derivative_order=v['derivative_order'],
         omitted=v['omitted_modes_uniform_bound']['interval'], total=v['total_uniform_error']['interval'])
         for v in rows]), indent=2), flush=True)


if __name__ == '__main__':
    main()
