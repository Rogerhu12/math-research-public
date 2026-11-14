#!/usr/bin/env python3
"""Native scalar Arb DFT, coefficientwise on truncated power series.

Reconstructed after the second executor loss; this is a new source version.
It preserves all input balls and changes only the finite Fourier algorithm.
It proves no omitted-frequency or time-tail bound.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, acb, arb_series, acb_series, ctx
from fourfold_phase_beta_interval import NativeFFT


class NativeSeriesFFT:
    def fft(self, values, inverse=False):
        values = np.asarray(values, dtype=object)
        if not values.ndim or not values.shape[0]:
            raise ValueError('nonempty Fourier axis required')
        n = values.shape[0]
        matrix = values.reshape(n, -1)
        result = np.empty(matrix.shape, dtype=object)
        oldcap = ctx.cap
        try:
            for column in range(matrix.shape[1]):
                row = list(matrix[:, column])
                is_series = [isinstance(value, (arb_series, acb_series)) for value in row]
                if any(is_series):
                    if not all(is_series) or len({value.prec for value in row}) != 1:
                        raise ValueError('series must have one common declared precision')
                    m = row[0].prec
                    ctx.cap = max(oldcap, m)
                    transformed = [acb.dft([acb(value[i]) for value in row], inverse=inverse)
                                   for i in range(m)]
                    for j in range(n):
                        result[j, column] = acb_series([transformed[i][j] for i in range(m)], prec=m)
                else:
                    result[:, column] = acb.dft([acb(value) for value in row], inverse=inverse)
            return result.reshape(values.shape)
        finally:
            ctx.cap = oldcap


def overlaps(a, b):
    return a.real.overlaps(b.real) and a.imag.overlaps(b.imag)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--nodes', type=int, default=2048)
    parser.add_argument('--terms', type=int, default=53)
    parser.add_argument('--fields', type=int, default=3)
    parser.add_argument('--bits', type=int, default=320)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    n, m, count = args.nodes, args.terms, args.fields
    if n < 2 or n & (n-1) or min(m, count) < 1:
        raise ValueError('power of two nodes and positive dimensions required')
    ctx.prec, ctx.cap = args.bits, m
    values = np.empty((n, count), object)
    for j in range(n):
        for c in range(count):
            values[j, c] = acb_series([
                acb(arb(((17*j+11*i+3*c)%101-50, -5-3*i)),
                    arb(((7*j+19*i+5*c)%89-44, -5-3*i))) for i in range(m)], prec=m)
    timings = {}
    outputs = []
    for name, engine in [('previous_python_butterflies', NativeFFT()), ('native_coefficientwise', NativeSeriesFFT())]:
        wall, cpu = time.monotonic(), time.process_time()
        output = engine.fft(values)
        timings[name] = {'wall_seconds': time.monotonic()-wall, 'cpu_seconds': time.process_time()-cpu}
        outputs.append(output)
    for key in np.ndindex(values.shape):
        for i in range(m):
            if not overlaps(outputs[0][key][i], outputs[1][key][i]):
                raise AssertionError('finite transforms do not overlap')
    recovered = NativeSeriesFFT().fft(outputs[1], inverse=True)
    for key in np.ndindex(values.shape):
        for i in range(m):
            original, value = values[key][i], recovered[key][i]
            if not value.real.contains(original.real) or not value.imag.contains(original.imag):
                raise AssertionError('DFT round trip does not contain exact input')
    scalars = NativeSeriesFFT().fft(np.array([1, 2, 3, 4], object))
    expected = [acb(10), acb(-2, 2), acb(-2), acb(-2, -2)]
    if not all(v.real.contains(e.real) and v.imag.contains(e.imag) for v,e in zip(scalars,expected)):
        raise AssertionError('scalar Fourier sign convention mismatch')
    report = {'kind':'reconstructed_native_series_fft_finite_map_benchmark',
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'nodes':n, 'terms':m, 'fields':count, 'bits':args.bits, 'timings':timings,
              'all_finite_coefficients_overlap':True, 'exact_input_roundtrip_contained':True,
              'four_point_scalar_sign_check':True,
              'limitations':['No continuous angle or omitted time estimate is asserted.']}
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
