#!/usr/bin/env python3
"""Exact rational R6 bounds for finite Fourier endpoint source packets.

All floating packet coefficients are interpreted as their exact IEEE binary
rationals.  This certifies the explicitly defined Hermite polynomial layer,
conditional on the stated exact fixed background bound.  It does not certify
the source ODE or Fourier interpolation error to an unknown exact solution.
"""
import argparse
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


def f(x):
    return Q.from_float(float(x))


def exact_norm(rows):
    return sum((1 + c['frequency']) ** 2 *
               sum(abs(f(x)) for x in c['cos'] + c['sin']) for c in rows)


def show(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator),
            'display_only': float(x)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path)
    a = ap.parse_args()
    if a.output.exists():
        raise SystemExit('Refusing to overwrite prior check')
    d = json.loads(a.input.read_text())
    B = f(d['settings']['assumedBackgroundCurvature'])
    rows = []
    assert Q(9, 4) ** 2 > 5 and Q(3, 2) ** 2 > 2
    for q in d['rows']:
        r, cuff = f(q['r']), f(q['cuff'])
        L = r - cuff
        assert 0 < L <= cuff and L * B <= 1
        n = [exact_norm(c) for c in q['coefficients']]
        K = n[0] / L ** 2 + n[1] / L + n[2]
        eta1, eta2 = Q(9, 4) * L * K, 15 * K
        metric = 2 * eta1 + eta1 ** 2
        full = Q(3, 2) * B * eta2 + Q(1, 2) * eta2 ** 2 + B ** 2 * metric
        assert eta1 < 1
        curvature = (B + eta2) / (1 - eta1) ** 2
        if d['settings'].get('symmetry') == 'c3':
            for c in q['coefficients']:
                for z in c:
                    m = z['frequency']
                    assert z['sin'][0] == z['cos'][1] == z['sin'][2] == 0
                    if m % 3:
                        assert z['cos'][2] == 0
                        sign = 1 if m % 3 == 1 else -1
                        assert f(z['cos'][0]) == sign * f(z['sin'][1])
                    else:
                        assert z['cos'][0] == z['sin'][1] == 0
        projection_ok = L ** 2 * K / cuff <= Q(1, 10) and 2 * L * K <= Q(1, 4)
        rows.append({'rawNode': q['rawNode'], 'L': show(L), 'norms': [show(x) for x in n],
                     'K': show(K), 'eta1': show(eta1), 'eta2': show(eta2),
                     'metricUpper': show(metric), 'fullTensorUpper': show(full),
                     'curvatureUpper': show(curvature),
                     'nested_projection_sufficient_conditions': projection_ok})
    result = {'status': 'PASS exact arithmetic for conditional finite Hermite layers',
              'scope': 'The finite Fourier polynomials and Hermite formula are exact definitions. Background curvature, outer-piece matching, source-flow error and C2 Cauchy convergence remain separate obligations.',
              'input': str(a.input.resolve()),
              'inputSHA256': hashlib.sha256(a.input.read_bytes()).hexdigest(),
              'scriptSHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'assumedBackgroundCurvature': show(B), 'rows': rows}
    a.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'rows': [
        {'N': z['rawNode'], 'K': z['K']['display_only'],
         'metric': z['metricUpper']['display_only'], 'full': z['fullTensorUpper']['display_only']}
        for z in rows]}))


if __name__ == '__main__':
    main()
