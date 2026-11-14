#!/usr/bin/env python3
"""Continuous finite-reference bounds, without asserting an ODE residual.

The saved binary64 Fourier/Bernstein coefficients DEFINE exact dyadic
coefficients. Bernstein convexity in real time and exact Fourier reality
give bounds on the entire complex initial-angle strip. Arb performs every
transcendental operation and all nontrivial bound arithmetic. This checks
the defined reference, not the numerical integrator that selected it.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np
from flint import arb, ctx


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rat(q):
    q = Fraction(q)
    return arb(q.numerator) / q.denominator


def exact_time(row):
    q = arb(int(row['numerator'])) / int(row['denominator'])
    if row['kind'] == 'rational_multiple_of_pi':
        return q * arb.pi()
    if row['kind'] != 'rational':
        raise ValueError('unknown exact time representation')
    return q


def up(value):
    answer = math.nextafter(float(value.upper()), math.inf)
    if not math.isfinite(answer):
        raise ValueError('nonfinite upper bound')
    return answer


def down(value):
    answer = math.nextafter(float(value.lower()), -math.inf)
    if not math.isfinite(answer):
        raise ValueError('nonfinite lower bound')
    return answer


def coefficient_bounds(real, imag):
    """A rectangular coefficient hull, followed by directed Euclidean norm.

    np.abs and np.max only select exact finite binary64 inputs here. There
    is no floating summation, product, or square root in these selections.
    Axis 0 consists of the Bernstein coefficients at one real-time span.
    """
    rm = np.max(np.abs(real), axis=0)
    im = np.max(np.abs(imag), axis=0)
    return [[(arb(float(rm[f, k]))**2 + arb(float(im[f, k]))**2).sqrt().upper()
             for k in range(real.shape[-1])] for f in range(real.shape[-2])]


def strip_bounds(real, imag, width, sinh, cosh):
    c = coefficient_bounds(real, imag)
    image = width / 4 + 2*sum((c[0][k]*sinh[k] for k in range(1, len(sinh))), arb(0))
    variation = 2*sum((c[1][k]*cosh[k] for k in range(1, len(cosh))), arb(0))
    lmin = arb(float(np.min(real[:, 1, 0]))) - variation
    lmax = arb(float(np.max(real[:, 1, 0]))) + variation
    qmin, qmax = lmin.exp(), lmax.exp()
    if not qmin > 0:
        raise ValueError('positive reference modulus not resolved')
    return dict(imaginary_Y_absolute_upper=up(image),
                real_L_lower=down(lmin), real_L_upper=up(lmax),
                q_modulus_lower=down(qmin), q_modulus_upper=up(qmax))


def initial_error(real, imag, conjugacy, width):
    """The exact Fourier norm of E0=H-4Y0, enclosed with Arb."""
    h = conjugacy['h_nonnegative_integer_coefficients']
    denominator = 2**int(conjugacy['denominator_power_of_two'])
    K = max(len(h), real.shape[-1]) - 1
    total = arb(0)
    for k in range(K+1):
        hr, hi = (arb(int(h[k][0]))/denominator, arb(int(h[k][1]))/denominator) if k < len(h) else (arb(0), arb(0))
        ur, ui = (arb(float(real[0, k])), arb(float(imag[0, k]))) if k < real.shape[-1] else (arb(0), arb(0))
        magnitude = ((hr-4*ur)**2 + (hi-4*ui)**2).sqrt()
        total += magnitude * (1 if k == 0 else 2*(k*width).exp())
    return total


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--conjugacy', type=Path, required=True)
    ap.add_argument('--widths', nargs='+', default=['1/512', '1/256', '1/128'])
    ap.add_argument('--bits', type=int, default=192)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.bits < 128:
        raise ValueError('use at least 128 bits')
    ctx.prec = args.bits
    m = json.loads(args.manifest.read_text())
    h = json.loads(args.conjugacy.read_text())
    if not m.get('complete') or m['time_basis'] != 'bernstein' or m['time_degree'] != 7:
        raise ValueError('a complete degree-seven Bernstein reference is required')
    if m['fields'] != ['U', 'L'] or not m['continuous_by_shared_endpoint_coefficients']:
        raise ValueError('unexpected reference convention')
    if h['kind'] != 'exact_dyadic_trigonometric_polynomials_H_and_q' or sha(args.conjugacy) != m['trace_identity']['dyadic_conjugacy_sha256']:
        raise ValueError('conjugacy identity mismatch')
    if int(h['h_nonnegative_integer_coefficients'][0][1]) != 0:
        raise ValueError('non-real H mean')
    times = m['exact_time_endpoints']
    direction = int(m['time_orientation'])
    if direction not in [-1, 1] or len(times) != m['segment_count']+1:
        raise ValueError('invalid time grid')
    expected_first = dict(kind='rational_multiple_of_pi', numerator=-direction, denominator=2)
    expected_last = dict(kind='rational_multiple_of_pi', numerator=direction, denominator=2)
    if times[0] != expected_first or times[-1] != expected_last:
        raise ValueError('the whole branch must have exact pi endpoints')
    widths = [Fraction(s) for s in args.widths]
    if any(s <= 0 for s in widths):
        raise ValueError('strip widths must be positive')
    K = int(m['Fourier_degree'])
    caches = [(rat(s), [(k*rat(s)).sinh() for k in range(K+1)],
               [(k*rat(s)).cosh() for k in range(K+1)]) for s in widths]
    previous = None
    first_real = first_imag = None
    cursor = 0
    rows = []
    for shard in m['shards']:
        path = args.manifest.parent / shard['path']
        if sha(path) != shard['sha256'] or path.stat().st_size != shard['bytes']:
            raise ValueError('coefficient shard hash/size mismatch')
        with np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False) as z:
            real, imag = z['coefficient_real'].copy(), z['coefficient_imag'].copy()
            meta = json.loads(str(z['metadata']))
        count = int(shard['segment_count'])
        if shard['start_segment'] != cursor or meta['start_segment'] != cursor or meta['segment_count'] != count:
            raise ValueError('shards do not exactly tile the branch')
        if meta['exact_times'] != times[cursor:cursor+count+1] or meta['source_sha256'] != m['source_sha256']:
            raise ValueError('mixed reference construction')
        if real.shape != (count, 8, 2, K+1) or imag.shape != real.shape:
            raise ValueError('wrong coefficient shape')
        if not np.all(np.isfinite(real)) or not np.all(np.isfinite(imag)) or np.any(imag[:, :, :, 0] != 0):
            raise ValueError('invalid exact real Fourier coefficients')
        for j in range(count):
            index = cursor+j
            if not direction*(exact_time(times[index+1])-exact_time(times[index])) > 0:
                raise ValueError('nonpositive exact time interval')
            if previous is not None and (not np.array_equal(previous[0], real[j, 0]) or not np.array_equal(previous[1], imag[j, 0])):
                raise ValueError('nonzero reference jump at a shared endpoint')
            previous = (real[j, -1].copy(), imag[j, -1].copy())
            if index == 0:
                first_real, first_imag = real[j, 0].copy(), imag[j, 0].copy()
            rows.append(dict(segment=index, widths={str(s):strip_bounds(real[j], imag[j], *cache)
                                                   for s, cache in zip(widths, caches)}))
        cursor += count
    if cursor != m['segment_count']:
        raise ValueError('missing final coefficient shard')
    summaries = {}
    for s, cache in zip(widths, caches):
        w = str(s)
        initial = strip_bounds(first_real[None], first_imag[None], *cache)
        error = initial_error(first_real, first_imag, h, cache[0])
        summaries[w] = dict(
            imaginary_Y_absolute_upper=max(r['widths'][w]['imaginary_Y_absolute_upper'] for r in rows),
            real_L_lower=min(r['widths'][w]['real_L_lower'] for r in rows),
            real_L_upper=max(r['widths'][w]['real_L_upper'] for r in rows),
            q_modulus_lower=min(r['widths'][w]['q_modulus_lower'] for r in rows),
            q_modulus_upper=max(r['widths'][w]['q_modulus_upper'] for r in rows),
            initial_q_modulus_lower=initial['q_modulus_lower'],
            initial_H_minus_four_Y_Wiener_upper=up(error),
            initial_R60_radius_upper=up(error/(4*arb(initial['q_modulus_lower']))))
    report = dict(kind='continuous_finite_Fourier_Bernstein_reference_bounds', complete=True,
        source_sha256=sha(__file__), manifest_path=str(args.manifest), manifest_sha256=sha(args.manifest),
        conjugacy_sha256=sha(args.conjugacy), bits=args.bits, segment_count=cursor,
        Fourier_degree=K, time_degree=7, time_basis='bernstein', widths=[str(s) for s in widths],
        exact_time_endpoints_checked=True, exact_continuity_checked=True,
        all_internal_Y_and_L_jumps_exactly_zero=True,
        initial_L_exactly_zero=bool(np.all(first_real[1] == 0) and np.all(first_imag[1] == 0)),
        global_bounds=summaries, segments=rows,
        proof='Bernstein convexity for real time; |ImY|<=S/4+2 sum C_U,k sinh(kS); ReL between extrema of L_0 +/-2 sum C_L,k cosh(kS); |q|=exp(ReL). All coefficients are exact dyadics and all bound arithmetic is Arb.',
        limitations=['No ODE residual or actual characteristic-flow error is asserted.',
            'Time is real in each segment; only the initial angle is complex.',
            'These bounds do not pay for the actual geometric field or its infinite primitive.',
            'The saved finite polynomial is the reference definition; construction interpolation accuracy is not assumed.'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    payload=(json.dumps(report, indent=2)+'\n').encode()
    if args.out.suffix == '.gz':
        payload=gzip.compress(payload, mtime=0)
    elif len(payload) > 1_000_000:
        raise ValueError('large output must be saved as .gz')
    if len(payload)>5_000_000:
        raise ValueError('output exceeds repository single-file limit')
    args.out.write_bytes(payload)
    print(json.dumps(dict(complete=True, segment_count=cursor, global_bounds=summaries), indent=2), flush=True)


if __name__ == '__main__':
    main()
