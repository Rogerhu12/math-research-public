#!/usr/bin/env python3
"""Rebuilt exact restriction norms after the 2026-11-12 executor reset.

This is a fresh implementation of the recorded algorithm, not a reconstruction
of the lost binary certificate.  Every quotient is an actual restriction module.
"""
import argparse
import random
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import numpy as np
import p41_r2_matrix as r
from p41_cm4_divisor47 import kernel
from p41_group_operations47 import load_sources, make_model, replay_negative, onebased
from p41_formal47_multiply import write_checkpoint


def pair_mul(a, b):
    return [(int(a[0])*int(b[0])-int(a[1])*int(b[1])) % r.Q,
            (int(a[0])*int(b[1])+int(a[1])*int(b[0])) % r.Q]


def pair_inverse(a):
    c = pow((int(a[0])**2+int(a[1])**2) % r.Q, -1, r.Q)
    return [int(a[0])*c % r.Q, -int(a[1])*c % r.Q]


def determinant(A):
    """Exact unit determinant; None means nonunit, never a claimed zero."""
    a, b = (x.copy() for x in A)
    n = a.shape[0]
    assert a.shape == b.shape == (n, n)
    answer = [1, 0]
    for k in range(n):
        candidates = np.flatnonzero(((a[k:, k] % 47)**2+(b[k:, k] % 47)**2) % 47)
        if not len(candidates):
            return None
        pivot = k+int(candidates[0])
        if pivot != k:
            a[[k, pivot]], b[[k, pivot]] = a[[pivot, k]], b[[pivot, k]]
            answer = [-answer[0] % r.Q, -answer[1] % r.Q]
        value = [int(a[k, k]), int(b[k, k])]
        answer = pair_mul(answer, value)
        iv = pair_inverse(value)
        pr = (a[k, k:]*iv[0]-b[k, k:]*iv[1]) % r.Q
        pi = (a[k, k:]*iv[1]+b[k, k:]*iv[0]) % r.Q
        vr, vi = a[k+1:, k].copy()[:, None], b[k+1:, k].copy()[:, None]
        a[k+1:, k:] = (a[k+1:, k:]-vr*pr+vi*pi) % r.Q
        b[k+1:, k:] = (b[k+1:, k:]-vr*pi-vi*pr) % r.Q
    return answer


def quotient(K):
    n, d = K[0].shape
    pivot, columns = r.rank_pivots(K)
    assert len(pivot) == d and columns == list(range(d))
    inverse = r.inverse_matrix(r.rows(K, pivot))
    normalized = r.mm(K, inverse)
    free = [i for i in range(n) if i not in set(pivot)]
    Q = r.zeros(n-d, n)
    block = r.neg(r.rows(normalized, free))
    for j in range(2):
        Q[j][:, pivot] = block[j]
        Q[j][:, free] = r.eye(n-d)[j]
    assert r.iszero(r.mm(Q, K))
    assert r.equal(r.cols(Q, free), r.eye(n-d))
    return Q, {'ambient_dimension': n, 'pivot_rows_1based': onebased(pivot),
               'free_rows_1based': onebased(free), 'kernel_basis_inverse': r.to_json(inverse),
               'block': r.to_json(block)}


def quotient_from_record(record):
    pivot = [i-1 for i in record['pivot_rows_1based']]
    free = [i-1 for i in record['free_rows_1based']]
    Q = r.zeros(len(free), record['ambient_dimension'])
    block = r.from_json(record['block'])
    for j in range(2):
        Q[j][:, pivot] = block[j]
        Q[j][:, free] = r.eye(len(free))[j]
    return Q


def norm_data(K, u, v, M, rng):
    S = r.mm(M['V2'], K)
    pairs = [(i, i) for i in range(73)]+[(i, (i+1) % 73) for i in range(73)]
    while True:
        pairs += [(rng.randrange(73), rng.randrange(73)) for _ in range(100)]
        values = r.mul(r.cols(M['W'], [i for i, j in pairs]), r.cols(S, [j for i, j in pairs]))
        rr, cc = r.rank_pivots(values)
        if len(rr) == 199:
            break
        assert len(rr) < 199 and len(pairs) < 746
    products = r.cols(values, cc)
    coords = r.rows(products, M['P3'])
    assert r.equal(r.mm(M['V3'], coords), products)
    Q2, rec2 = quotient(K)
    Q3, rec3 = quotient(coords)
    free2 = [i-1 for i in rec2['free_rows_1based']]
    maps = []
    dets = []
    for section in (u, v):
        full = r.mul(section, M['V2'])
        c = r.rows(full, M['P3'])
        assert r.equal(r.mm(M['V3'], c), full)
        assert r.iszero(r.mm(Q3, r.mm(c, K)))
        induced = r.cols(r.mm(Q3, c), free2)
        value = determinant(induced)
        assert value is not None, 'Requested section is not a unit on this divisor'
        maps.append(induced)
        dets.append(value)
    norm = pair_mul(dets[0], pair_inverse(dets[1]))
    return {'product_pairs_1based': [[pairs[i][0]+1, pairs[i][1]+1] for i in cc],
            'product_coordinate_matrix': r.to_json(coords), 'quotient2': rec2, 'quotient3': rec3,
            'numerator_determinant': dets[0], 'denominator_determinant': dets[1], 'norm': norm}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('data')/'p41_poincare_norms47_checkpoint.json.gz')
    args = parser.parse_args()
    sources, hashes = load_sources(Path(__file__).with_name('data'))
    M = make_model(sources)
    negative, _ = replay_negative(M, sources[3])
    divs = sources[1]
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    f = r.mm(M['W'], r.mm(K1, r.column(divs['canonical_coefficients'])))
    D0 = r.rows(r.mul(f, M['W']), M['P2'])
    u, v = [r.mm(M['W'], r.column(c)) for seed, c in sources[3]['norm_section_seeds_and_coefficients']]
    result = {'level': 41, 'auxiliary_prime': 47, 'modulus': r.Q, 'precision': 4,
              'source_sha256': hashes, 'implementation': 'reset-rebuild-v2', 'divisors': {}}
    rng = random.Random(4104712101)
    for label, K in [('D0', D0), ('E_B', M['B']), ('E_minusB', negative)]:
        result['divisors'][label] = norm_data(K, u, v, M, rng)
        print(label, 'actual restriction norm', result['divisors'][label]['norm'], flush=True)
    expected = {'D0': [3467725, 0], 'E_B': [708004, 0], 'E_minusB': [4763767, 0]}
    assert {k: v['norm'] for k, v in result['divisors'].items()} == expected
    assert pair_mul(expected['E_B'], pair_inverse(expected['D0'])) == [4666447, 0]
    result['status'] = 'actual norms re-created; independent verification is separate'
    digest, size = write_checkpoint(args.output, result)
    print('Saved', size, 'bytes; SHA256', digest, flush=True)


if __name__ == '__main__':
    main()
