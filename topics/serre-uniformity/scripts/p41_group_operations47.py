#!/usr/bin/env python3
"""Actual negative and double CM points using bounded, exact R2 matrices."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import time

import numpy as np
import p41_r2_matrix as r
from p41_cm4_divisor47 import kernel


def vector_json(c):
    return [row[0] for row in r.to_json(c)]


def onebased(indices):
    return [int(k)+1 for k in indices]


def load_sources(data_dir):
    names = ['p41_makdisi47_certificate.json.gz', 'p41_cusp_divisors47_certificate.json.gz',
             'p41_cm4_divisor47_certificate.json', 'p41_group47_checkpoint.json.gz']
    raw = [(data_dir/n).read_bytes() for n in names]
    decoded = [json.loads(gzip.decompress(b) if n.endswith('.gz') else b) for n, b in zip(names, raw)]
    return decoded, {n: hashlib.sha256(b).hexdigest() for n, b in zip(names, raw)}


def make_model(sources):
    model, divisors, cm4, checkpoint = sources
    W, A1 = r.from_json(model['evaluation_matrix']), r.from_json(model['frobenius_basis_matrix'])
    tau = [n-1 for n in model['frobenius_permutation_1based']]
    K1 = r.from_json(kernel(73, divisors['cusp_rank_columns_1based'], divisors['cusp_free_columns_1based'], divisors['canonical_kernel_block']))
    c = r.column(divisors['canonical_coefficients'])
    f = r.mm(W, r.mm(K1, c))
    assert np.all(r.units(f))
    pairs = divisors['square_basis_monomials_1based']
    V2 = r.mm(r.mul(r.cols(W, [a-1 for a, b in pairs]), r.cols(W, [b-1 for a, b in pairs])),
              r.from_json(divisors['square_basis_inverse']))
    P2 = [n-1 for n in divisors['square_pivot_rows_1based']]
    assert r.equal(r.rows(V2, P2), r.eye(199))
    A2 = r.rows(r.conjugate(r.rows(V2, tau)), P2)
    assert r.equal(r.mm(V2, A2), r.conjugate(r.rows(V2, tau)))
    KI = r.from_json(kernel(199, divisors['K_rank_columns_1based'], divisors['K_free_columns_1based'], divisors['K_kernel_block']))
    KZ = r.from_json(kernel(93, cm4['restriction_rank_columns_1based'], cm4['restriction_free_columns_1based'], cm4['point_kernel_block']))
    B = r.mm(KI, KZ)
    WB = r.mm(V2, B)
    AB = r.from_json(cm4['point_frobenius_basis_matrix'])
    assert r.equal(r.mm(WB, AB), r.conjugate(r.rows(WB, tau)))
    cpairs = checkpoint['cubic_selected_pairs_1based']
    aa, bb = [a-1 for a, b in cpairs], [b-1 for a, b in cpairs]
    oldrows = [P2[b] for b in bb]
    numerator = W[0][oldrows, aa][None, :], W[1][oldrows, aa][None, :]
    denom = f[0][oldrows].T, f[1][oldrows].T
    coefficient = r.mul(numerator, r.inverse_values(denom))
    residual = r.mul(r.cols(V2, bb), r.sub(r.cols(W, aa), r.mul(f, coefficient)))
    added = r.mm(residual, r.from_json(checkpoint['cubic_extra_inverse']))
    newrows = [n-1 for n in checkpoint['cubic_extra_rows_1based']]
    assert r.equal(r.rows(added, newrows), r.eye(126)) and r.iszero(r.rows(added, P2))
    fP2 = f[0][P2].T, f[1][P2].T
    V3a = r.mul(r.mul(f, V2), r.inverse_values(fP2))
    V3 = r.hcat(r.sub(V3a, r.mm(added, r.rows(V3a, newrows))), added)
    P3 = P2+newrows
    assert onebased(P3) == checkpoint['cubic_pivot_rows_1based']
    assert r.equal(r.rows(V3, P3), r.eye(325))
    A3 = r.rows(r.conjugate(r.rows(V3, tau)), P3)
    assert r.equal(r.mm(V3, A3), r.conjugate(r.rows(V3, tau)))
    print('Actual V2 and V3 reconstructed exactly from published model and the GP checkpoint.', flush=True)
    return {'W': W, 'A1': A1, 'tau': tau, 'V2': V2, 'P2': P2, 'A2': A2,
            'V3': V3, 'P3': P3, 'A3': A3, 'B': B, 'WB': WB, 'AB': AB}


def replay_negative(M, checkpoint):
    section = []
    for seed, coeff in checkpoint['negative_flip_section_seeds_and_coefficients']:
        seed, coeff = r.column(seed), r.column(coeff)
        assert r.equal(coeff, r.add(seed, r.mm(M['AB'], r.conjugate(seed))))
        section.append(r.mm(M['WB'], coeff))
    f, g = section
    assert np.all(r.units(f))
    ratio = r.mul(g, r.inverse_values(f))
    scaled = r.mul(ratio, M['V2'])
    R = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
    rows = [n-1 for n in checkpoint['negative_rank_rows_1based']]
    cols = [n-1 for n in checkpoint['negative_rank_columns_1based']]
    K, free, block = r.kernel_from_rows(r.rows(R, rows), rows, cols)
    assert onebased(free) == checkpoint['negative_free_columns_1based']
    assert r.to_json(block) == checkpoint['negative_kernel_block']
    assert r.iszero(r.mm(R, K))
    AK = r.from_json(checkpoint['negative_frobenius_matrix'])
    assert r.equal(r.mm(K, AK), r.mm(M['A2'], r.conjugate(K)))
    assert r.equal(r.mm(AK, r.conjugate(AK)), r.eye(73))
    print('The actual negative B4 checkpoint matches the exact int64 computation entry by entry.', flush=True)
    return K, AK


def flip(S, AS, M, rng, label):
    for attempt in range(1, 31):
        seed_f, cf = r.rational_trace(AS, rng)
        f = r.mm(S, cf)
        if not np.all(r.units(f)):
            continue
        seed_g, cg = r.rational_trace(AS, rng)
        g = r.mm(S, cg)
        ratio = r.mul(g, r.inverse_values(f))
        scaled = r.mul(ratio, M['V2'])
        R = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        rr, cc = r.rank_pivots(R)
        if len(rr) != 126:
            continue
        K, free, block = r.kernel_from_rows(r.rows(R, rr), rr, cc)
        assert r.iszero(r.mm(R, K))
        transformed = r.mm(M['A2'], r.conjugate(K))
        AK = r.rows(transformed, free)
        assert r.equal(r.mm(K, AK), transformed)
        assert r.equal(r.mm(AK, r.conjugate(AK)), r.eye(73))
        record = {'f_seed': vector_json(seed_f), 'f_coefficients': vector_json(cf),
                  'g_seed': vector_json(seed_g), 'g_coefficients': vector_json(cg),
                  'rank_rows_1based': onebased(rr), 'rank_columns_1based': onebased(cc),
                  'free_columns_1based': onebased(free), 'kernel_block': r.to_json(block),
                  'frobenius_matrix': r.to_json(AK)}
        print(label, 'actual residual divisor after', attempt, 'tries', flush=True)
        return K, AK, record
    raise RuntimeError('No unit residual divisor found')


def double(M, rng):
    Bnorm, Brows, Bcols, Binverse = r.normalize(M['WB'], 73)
    assert Bcols == list(range(73))
    pairs = [[k, k] for k in range(73)]+[sorted([k, (k+1) % 73]) for k in range(73)]
    while True:
        target = len(pairs)+100
        while len(pairs) < target:
            a, b = rng.randrange(73), rng.randrange(73)
            if a != b:
                pairs.append(sorted([a, b]))
        products = r.mul(r.cols(Bnorm, [p[0] for p in pairs]), r.cols(Bnorm, [p[1] for p in pairs]))
        rr_products, _ = r.rank_pivots(products)
        if len(rr_products) == 199:
            break
        assert len(rr_products) < 199 and len(pairs) < 746
    U, Urows, Ucols, Uinverse = r.normalize(products, 199)
    Upairs = [pairs[k] for k in Ucols]
    for attempt in range(1, 31):
        seed, coeff = r.rational_trace(M['A1'], rng)
        v = r.mm(M['W'], coeff)
        R = r.mul(v, M['V3'])
        R = r.sub(R, r.mm(U, r.rows(R, Urows)))
        rr, cc = r.rank_pivots(R)
        if len(rr) != 252:
            continue
        K, free, block = r.kernel_from_rows(r.rows(R, rr), rr, cc)
        assert r.iszero(r.mm(R, K))
        transformed = r.mm(M['A3'], r.conjugate(K))
        AK = r.rows(transformed, free)
        assert r.equal(r.mm(K, AK), transformed)
        assert r.equal(r.mm(AK, r.conjugate(AK)), r.eye(73))
        break
    else:
        raise RuntimeError('Actual V3 colon did not have rank252')
    print('Actual complete V3(-2 E_B), dimension73.', flush=True)
    minus2, Aminus2, minus_record = flip(r.mm(M['V3'], K), AK, M, rng, 'Minus2B4')
    plus2, Aplus2, plus_record = flip(r.mm(M['V2'], minus2), Aminus2, M, rng, 'Plus2B4')
    record = {'point_pivot_rows_1based': onebased(Brows), 'point_basis_inverse': r.to_json(Binverse),
              'product_pairs_1based': [[a+1, b+1] for a, b in Upairs],
              'product_pivot_rows_1based': onebased(Urows), 'product_basis_inverse': r.to_json(Uinverse),
              'colon_section_seed': vector_json(seed), 'colon_section_coefficients': vector_json(coeff),
              'colon_rank_rows_1based': onebased(rr), 'colon_rank_columns_1based': onebased(cc),
              'colon_free_columns_1based': onebased(free), 'colon_kernel_block': r.to_json(block),
              'colon_frobenius_matrix': r.to_json(AK), 'minus_two': minus_record, 'plus_two': plus_record}
    return plus2, Aplus2, record


def main():
    script = Path(__file__).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=script.with_name('data')/'p41_group_operations47_certificate.json.gz')
    args = parser.parse_args()
    sources, hashes = load_sources(script.with_name('data'))
    start = time.monotonic()
    M = make_model(sources)
    replay_negative(M, sources[3])
    plus2, Aplus2, record = double(M, random.Random(4104711703))
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
              'source_sha256': hashes, 'double': record,
              'int64_accumulation_bound': 2*820*(r.Q-1)**2,
              'result': 'actual -B4, -2B4 and +2B4; principal Poincare norm in bound checkpoint; no nonprincipal height'}
    encoded = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    compressed = gzip.compress(encoded, mtime=0)
    args.output.write_bytes(compressed)
    print('Raw bytes', len(encoded), 'gzip bytes', len(compressed), 'SHA256', hashlib.sha256(compressed).hexdigest())
    print('Elapsed seconds', round(time.monotonic()-start, 3))


if __name__ == '__main__':
    main()
