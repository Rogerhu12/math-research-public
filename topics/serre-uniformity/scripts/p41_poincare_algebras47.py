#!/usr/bin/env python3
"""Actual monogenic restriction algebras; rebuilt after the executor reset.

The quotient modules come from actual section restrictions.  A unit Krylov
matrix proves the algebra identification, including nonreduced multiplicities.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
import numpy as np
import p41_r2_matrix as r
from p41_group_operations47 import load_sources, make_model, replay_negative, vector_json
from p41_formal47_multiply import write_checkpoint
from p41_poincare_norms47 import quotient_from_record, determinant
from p41_cm4_divisor47 import kernel


def polycol(A, j):
    return A[0][:, j].copy(), A[1][:, j].copy()


def polynomial_product(a, b, relation):
    d = len(relation[0])-1
    assert len(a[0]) == len(b[0]) == d
    assert 2*d*(r.Q-1)**2 < 2**63
    ar = (np.convolve(a[0], b[0])-np.convolve(a[1], b[1])) % r.Q
    ai = (np.convolve(a[0], b[1])+np.convolve(a[1], b[0])) % r.Q
    for k in range(2*d-2, d-1, -1):
        x, y = int(ar[k]), int(ai[k])
        offset = k-d
        ar[offset:k] = (ar[offset:k]-x*relation[0][:-1]+y*relation[1][:-1]) % r.Q
        ai[offset:k] = (ai[offset:k]-x*relation[1][:-1]-y*relation[0][:-1]) % r.Q
    return ar[:d], ai[:d]


def polynomial_norm(a, relation):
    d = len(relation[0])-1
    M = r.zeros(d, d)
    ar, ai = (x.copy() for x in a)
    for j in range(d):
        M[0][:, j], M[1][:, j] = ar, ai
        x, y = int(ar[-1]), int(ai[-1])
        ar, ai = np.concatenate(([0], ar[:-1])), np.concatenate(([0], ai[:-1]))
        ar = (ar-x*relation[0][:-1]+y*relation[1][:-1]) % r.Q
        ai = (ai-x*relation[1][:-1]-y*relation[0][:-1]) % r.Q
    return determinant(M)


def multiplication(section, Q3, free2, M):
    values = r.mul(section, M['V2'])
    coordinates = r.rows(values, M['P3'])
    assert r.equal(r.mm(M['V3'], coordinates), values)
    return r.cols(r.mm(Q3, coordinates), free2)


def make_algebra(label, K, rec, M, sources, u, v, rng):
    Q2, Q3 = quotient_from_record(rec['quotient2']), quotient_from_record(rec['quotient3'])
    free2 = [j-1 for j in rec['quotient2']['free_rows_1based']]
    assert r.iszero(r.mm(Q2, K))
    Fv = multiplication(v, Q3, free2, M)
    Fvi = r.inverse_matrix(Fv)
    one = r.mm(Q2, r.rows(r.mul(v, v), M['P2']))
    p1 = [i-1 for i in sources[0]['pivot_rows_1based']]
    for attempt in range(1, 101):
        if attempt == 1:
            gc = r.rows(u, p1)
        else:
            gc = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73)])
        g = r.mm(M['W'], gc)
        Mg = r.mm(Fvi, multiplication(g, Q3, free2, M))
        Krylov = r.zeros(126, 126)
        current = one
        for j in range(126):
            Krylov[0][:, j], Krylov[1][:, j] = current[0][:, 0], current[1][:, 0]
            current = r.mm(Mg, current)
        rr, cc = r.rank_pivots(Krylov)
        if len(rr) == 126:
            break
    else:
        raise RuntimeError('No actual monogenic restriction generator in100 attempts')
    Ki = r.inverse_matrix(Krylov)
    coefficients = r.mm(Ki, current)
    relation = (np.concatenate((-coefficients[0][:, 0] % r.Q, [1])),
                np.concatenate((-coefficients[1][:, 0] % r.Q, [0])))
    Phi2 = r.mm(Ki, Q2)
    Phi3 = r.mm(r.mm(Ki, Fvi), Q3)
    vW = r.mul(v, M['W'])
    vWcoords = r.rows(vW, M['P2'])
    assert r.equal(r.mm(M['V2'], vWcoords), vW)
    Phi1 = r.mm(Phi2, vWcoords)
    unit = r.zeros(126, 1)
    unit[0][0, 0] = 1
    assert r.equal(r.mm(Phi1, r.rows(v, p1)), unit)
    assert polynomial_norm(polycol(r.mm(Phi1, r.rows(u, p1)), 0), relation) == rec['norm']
    # All199 actual quadratic basis products, followed by the published basis change.
    pairs = sources[1]['square_basis_monomials_1based']
    products = r.zeros(126, 199)
    for j, (a, b) in enumerate(pairs):
        value = polynomial_product(polycol(Phi1, a-1), polycol(Phi1, b-1), relation)
        products[0][:, j], products[1][:, j] = value
    assert r.equal(r.mm(products, r.from_json(sources[1]['square_basis_inverse'])), Phi2)
    # These199+126 actual cubic products span V3 by its published construction.
    divs = sources[1]
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    fc = r.mm(K1, r.column(divs['canonical_coefficients']))
    f = r.mm(M['W'], fc)
    fp = polycol(r.mm(Phi1, fc), 0)
    actual = r.mm(Phi3, r.rows(r.mul(f, M['V2']), M['P3']))
    for j in range(199):
        expected = polynomial_product(fp, polycol(Phi2, j), relation)
        assert all(np.array_equal(expected[k], actual[k][:, j]) for k in range(2))
    pairs = sources[3]['cubic_selected_pairs_1based']
    actual = r.mm(Phi3, r.rows(r.mul(r.cols(M['W'], [a-1 for a, b in pairs]),
                                   r.cols(M['V2'], [b-1 for a, b in pairs])), M['P3']))
    for j, (a, b) in enumerate(pairs):
        expected = polynomial_product(polycol(Phi1, a-1), polycol(Phi2, b-1), relation)
        assert all(np.array_equal(expected[k], actual[k][:, j]) for k in range(2))
    record = {'primitive_attempt': attempt, 'generator_coefficients': vector_json(gc),
              'denominator_coefficients': vector_json(r.rows(v, p1)),
              'krylov_inverse': r.to_json(Ki),
              'minimal_polynomial_ascending': np.stack(relation, axis=-1).tolist(),
              'comparison_numerator_coefficients': vector_json(r.rows(u, p1)),
              'comparison_norm': rec['norm']}
    print('Actual restriction algebra', label, 'degree126; primitive attempt', attempt,
          '; allV2/V3 multiplication identities PASS.', flush=True)
    return record, (Phi1, Phi2, Phi3, relation)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('data')/'p41_poincare_algebras47_checkpoint.json.gz')
    args = parser.parse_args()
    folder = Path(__file__).with_name('data')
    sources, hashes = load_sources(folder)
    normraw = (folder/'p41_poincare_norms47_checkpoint.json.gz').read_bytes()
    norms = json.loads(gzip.decompress(normraw))
    assert norms['source_sha256'] == hashes
    M = make_model(sources)
    minus, _ = replay_negative(M, sources[3])
    divs = sources[1]
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    f = r.mm(M['W'], r.mm(K1, r.column(divs['canonical_coefficients'])))
    D0 = r.rows(r.mul(f, M['W']), M['P2'])
    uc, vc = [r.column(c) for seed, c in sources[3]['norm_section_seeds_and_coefficients']]
    u, v = r.mm(M['W'], uc), r.mm(M['W'], vc)
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
              'source_sha256': hashes, 'norm_source_sha256': hashlib.sha256(normraw).hexdigest(),
              'implementation': 'reset-rebuild-v2', 'divisors': {}}
    rng = random.Random(4104712102)
    algebras = {}
    for label, K in [('D0', D0), ('E_B', M['B']), ('E_minusB', minus)]:
        record, algebra = make_algebra(label, K, norms['divisors'][label], M, sources, u, v, rng)
        result['divisors'][label], algebras[label] = record, algebra
    tc = r.mm(M['B'], r.column(sources[3]['negative_flip_section_seeds_and_coefficients'][1][1]))
    algebra = algebras['E_minusB']
    tn = polynomial_norm(polycol(r.mm(algebra[1], tc), 0), algebra[3])
    assert tn == [1412636, 0]
    result['quadratic_section_coefficients'] = vector_json(tc)
    result['quadratic_norm_on_E_minusB'] = tn
    for attempt in range(1, 101):
        seed, cubic = r.rational_trace(M['A3'], rng)
        values = {label: polynomial_norm(polycol(r.mm(A[2], cubic), 0), A[3]) for label, A in algebras.items()}
        if all(value is not None and value[1] == 0 for value in values.values()):
            break
    else:
        raise RuntimeError('No cubic section avoiding all three actual divisors')
    result['cubic_section_seed'] = vector_json(seed)
    result['cubic_section_coefficients'] = vector_json(cubic)
    result['cubic_norms'] = values
    result['status'] = 'actual restriction algebras rebuilt; independent verification is separate'
    digest, size = write_checkpoint(args.output, result)
    print('Norms of actual rational cubic', values, flush=True)
    print('Saved', size, 'bytes; SHA256', digest, flush=True)


if __name__ == '__main__':
    main()
