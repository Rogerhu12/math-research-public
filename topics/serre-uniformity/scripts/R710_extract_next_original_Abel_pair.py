#!/usr/bin/env python3
"""Reuse the R706 original-z certificate to extract lower fixed CM weights.

No differential equation is solved and no window is rerun.  All powers of
two and ordinary factorials use the exact R697 formulas, not a weight-
independent mod-p abbreviation.  The input is the full original-z certificate.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

from flint import nmod_poly


def digest(a):
    return hashlib.sha256(json.dumps(a, separators=(',', ':')).encode()).hexdigest()


def run(path):
    raw = path.read_bytes()
    d = json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)
    p, N = d['prime'], d['N']
    assert p == 137147 and N == 22857
    assert hashlib.sha256(raw).hexdigest() == '54fcc49e58f9f53eaf459d2c59379578ed64281874dede30d097e69c115afc05'
    coeff = d['coefficients']
    for key in ('X', 'V', 'Q'):
        assert len(coeff[key]) == N + 1
        assert digest(coeff[key]) == d['coefficient_sha256'][key]
    X, V, Q = (nmod_poly(coeff[key], p) for key in ('X', 'V', 'Q'))
    assert (-2*X + 6*X.derivative().left_shift(1) - V).truncate(N+1).is_zero()
    assert (V.mul_low(V, N+1) - 4*X.mul_low(X, N+1).mul_low(X, N+1)
            + nmod_poly([0, 4], p)).truncate(N+1).is_zero()
    F = X.mul_low(Q, N+1)
    XV = X.mul_low(V, N+1)
    G = -XV.mul_low(Q, N+1)*pow(2, -1, p)
    facts = [1]*p
    for j in range(1, p):
        facts[j] = facts[j-1]*j % p
    out = []
    for k in (p, p-3, p-6, p-9):
        m = k-1
        if m % 6 == 4:
            index = (m-4)//6
            c = int(F[index])
            A = c*facts[m]*pow(pow(2, m//2, p), -1, p) % p
            C = 3*A*A*pow(facts[m], -1, p) % p
            section = 'x_sigma6'
        else:
            assert m % 6 == 1
            index = (m-1)//6
            c = int(G[index])
            A = c*facts[m]*pow(pow(2, (m-1)//2, p), -1, p) % p
            C = -A*A*pow(2*facts[m], -1, p) % p
            section = 'minus_xy_sigma6'
        out.append(dict(weight=k, derivative_order=m, section=section,
                        coefficient_index=index, section_coefficient=c,
                        ordinary_factorial=facts[m], A=A, C=C))
    assert out[0]['A'] == d['A_p'] and out[1]['A'] == d['A_p_minus_3']
    assert out[0]['C'] == d['C_p'] and out[1]['C'] == d['C_p_minus_3']
    n = N-1
    f_summands = [int(X[j])*int(Q[n-j]) % p for j in range(n+1)]
    g_summands = [-int(XV[j])*int(Q[n-j])*pow(2, -1, p) % p
                  for j in range(n+1)]
    assert sum(f_summands) % p == out[2]['section_coefficient']
    assert sum(g_summands) % p == out[3]['section_coefficient']
    assert out[2]['C'] != 0 and out[3]['C'] != 0
    return dict(result='R710-next-actual-Abel-pair-at-first-exception', prime=p,
                input_gzip_sha256=hashlib.sha256(raw).hexdigest(),
                input_source_commit=d['source_commit'],
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                original_arrays_and_full_energy_equation_checked=True,
                differential_equation_or_window_repeated=False,
                rows=out,
                final_convolution_summands_sha256=dict(F=digest(f_summands), G=digest(g_summands)),
                implication_using_R705=dict(actual_M8_valuation=-7,
                                            actual_common_Abel_first_order_upper_bound=3,
                                            first_order_equal_to_3_claimed=False,
                                            height_first_jet_claimed=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = run(args.certificate)
    args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))
