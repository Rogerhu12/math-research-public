#!/usr/bin/env python3
"""Standard-library verification of the actual R117 group operations and norm."""
import gzip
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from verify_p41_makdisi47 import qmul, qinv, qmatmul, qdet
from verify_p41_cm3_makdisi47 import FastRing
from verify_p41_cusp_divisors47 import kernel, select, conjugate, identity, zero_matrix, field_qmatmul


def sub(A, B, q):
    return [[[(a-c) % q, (b-d) % q] for (a, b), (c, d) in zip(row, other)] for row, other in zip(A, B)]


def rowmul(values, A, q):
    return [[list(qmul(value, cell, q)) for cell in row] for value, row in zip(values, A)]


def trace_coefficients(A, seed, coeff, q):
    trace = qmatmul(A, conjugate([[c] for c in seed], q), q)
    assert coeff == [[(a+t[0][0]) % q, (b+t[0][1]) % q] for (a, b), t in zip(seed, trace)]


def unit_minor(R, rr, cc):
    square = select(R, rr, cc)
    det = qdet([[[a % 47, b % 47] for a, b in row] for row in square], 47)
    assert det != (0, 0)
    return det


def verify_flip(record, S, AS, M, q):
    trace_coefficients(AS, record['f_seed'], record['f_coefficients'], q)
    trace_coefficients(AS, record['g_seed'], record['g_coefficients'], q)
    f = [row[0] for row in qmatmul(S, [[c] for c in record['f_coefficients']], q)]
    g = [row[0] for row in qmatmul(S, [[c] for c in record['g_coefficients']], q)]
    assert all((a*a+b*b) % 47 for a, b in f)
    ratio = [qmul(gg, qinv(ff, q), q) for ff, gg in zip(f, g)]
    scaled = rowmul(ratio, M['V2'], q)
    R = sub(scaled, qmatmul(M['V2'], select(scaled, M['P2']), q), q)
    assert len(record['rank_rows_1based']) == len(record['rank_columns_1based']) == 126
    unit_minor(R, record['rank_rows_1based'], record['rank_columns_1based'])
    K = kernel(199, record['rank_columns_1based'], record['free_columns_1based'], record['kernel_block'])
    assert len(K[0]) == 73 and zero_matrix(qmatmul(R, K, q))
    AK = record['frobenius_matrix']
    assert qmatmul(K, AK, q) == qmatmul(M['A2'], conjugate(K, q), q)
    assert qmatmul(AK, conjugate(AK, q), q) == identity(73)
    return K, AK


def main(path):
    encoded = path.read_bytes()
    data = json.loads(gzip.decompress(encoded))
    q = data['modulus']
    assert (data['level'], data['auxiliary_prime'], data['precision'], q) == (41, 47, 4, 47**4)
    sources = {}
    for name, digest in data['source_sha256'].items():
        raw = path.with_name(name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        sources[name] = json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)
    model = sources['p41_makdisi47_certificate.json.gz']
    divs = sources['p41_cusp_divisors47_certificate.json.gz']
    cm4 = sources['p41_cm4_divisor47_certificate.json']
    ck = sources['p41_group47_checkpoint.json.gz']
    assert all(ck['source_sha256'][name] == digest for name, digest in data['source_sha256'].items()
               if name != 'p41_group47_checkpoint.json.gz')
    bound = 2*820*(q-1)**2
    assert data['int64_accumulation_bound'] == bound == 39050494119936000 < 2**63
    W, A1 = model['evaluation_matrix'], model['frobenius_basis_matrix']
    tau = model['frobenius_permutation_1based']
    K1 = kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block'])
    fcoeff = qmatmul(K1, [[c] for c in divs['canonical_coefficients']], q)
    f = [row[0] for row in qmatmul(W, fcoeff, q)]
    assert all((a*a+b*b) % 47 for a, b in f)
    pairs = divs['square_basis_monomials_1based']
    V2 = qmatmul([[qmul(row[a-1], row[b-1], q) for a, b in pairs] for row in W], divs['square_basis_inverse'], q)
    P2 = divs['square_pivot_rows_1based']
    assert select(V2, P2) == identity(199)
    A2 = select(conjugate(select(V2, tau), q), P2)
    KI = kernel(199, divs['K_rank_columns_1based'], divs['K_free_columns_1based'], divs['K_kernel_block'])
    KZ = kernel(93, cm4['restriction_rank_columns_1based'], cm4['restriction_free_columns_1based'], cm4['point_kernel_block'])
    B = qmatmul(KI, KZ, q)
    WB, AB = qmatmul(V2, B, q), cm4['point_frobenius_basis_matrix']
    cpairs = ck['cubic_selected_pairs_1based']
    lambdas = [qmul(W[P2[b-1]-1][a-1], qinv(f[P2[b-1]-1], q), q) for a, b in cpairs]
    residual = []
    for n in range(820):
        row = []
        for (a, b), scalar in zip(cpairs, lambdas):
            scaled = qmul(scalar, f[n], q)
            difference = [(W[n][a-1][0]-scaled[0]) % q, (W[n][a-1][1]-scaled[1]) % q]
            row.append(qmul(V2[n][b-1], difference, q))
        residual.append(row)
    added = qmatmul(residual, ck['cubic_extra_inverse'], q)
    extra = ck['cubic_extra_rows_1based']
    assert select(added, extra) == identity(126) and zero_matrix(select(added, P2))
    V3a = [[list(qmul(qmul(f[n], V2[n][k], q), qinv(f[P2[k]-1], q), q)) for k in range(199)] for n in range(820)]
    V3a = sub(V3a, qmatmul(added, select(V3a, extra), q), q)
    V3 = [a+b for a, b in zip(V3a, added)]
    P3 = P2+extra
    assert P3 == ck['cubic_pivot_rows_1based'] and select(V3, P3) == identity(325)
    A3 = select(conjugate(select(V3, tau), q), P3)
    assert qmatmul(V3, A3, q) == conjugate(select(V3, tau), q)
    M = {'V2': V2, 'P2': P2, 'A2': A2}
    negative = {'f_seed': ck['negative_flip_section_seeds_and_coefficients'][0][0],
                'f_coefficients': ck['negative_flip_section_seeds_and_coefficients'][0][1],
                'g_seed': ck['negative_flip_section_seeds_and_coefficients'][1][0],
                'g_coefficients': ck['negative_flip_section_seeds_and_coefficients'][1][1],
                'rank_rows_1based': ck['negative_rank_rows_1based'],
                'rank_columns_1based': ck['negative_rank_columns_1based'],
                'free_columns_1based': ck['negative_free_columns_1based'],
                'kernel_block': ck['negative_kernel_block'], 'frobenius_matrix': ck['negative_frobenius_matrix']}
    verify_flip(negative, WB, AB, M, q)
    print('The actual full V3 and negative B4 point independently verified.', flush=True)

    d = data['double']
    Bnorm = qmatmul(WB, d['point_basis_inverse'], q)
    assert select(Bnorm, d['point_pivot_rows_1based']) == identity(73)
    products = [[qmul(row[a-1], row[b-1], q) for a, b in d['product_pairs_1based']] for row in Bnorm]
    U = qmatmul(products, d['product_basis_inverse'], q)
    Urows = d['product_pivot_rows_1based']
    assert select(U, Urows) == identity(199)
    trace_coefficients(A1, d['colon_section_seed'], d['colon_section_coefficients'], q)
    v = [row[0] for row in qmatmul(W, [[c] for c in d['colon_section_coefficients']], q)]
    R = rowmul(v, V3, q)
    R = sub(R, qmatmul(U, select(R, Urows), q), q)
    assert len(d['colon_rank_rows_1based']) == len(d['colon_rank_columns_1based']) == 252
    unit_minor(R, d['colon_rank_rows_1based'], d['colon_rank_columns_1based'])
    K = kernel(325, d['colon_rank_columns_1based'], d['colon_free_columns_1based'], d['colon_kernel_block'])
    assert len(K[0]) == 73 and zero_matrix(qmatmul(R, K, q))
    AK = d['colon_frobenius_matrix']
    assert qmatmul(K, AK, q) == qmatmul(A3, conjugate(K, q), q)
    assert qmatmul(AK, conjugate(AK, q), q) == identity(73)
    minus2, Aminus2 = verify_flip(d['minus_two'], qmatmul(V3, K, q), AK, M, q)
    verify_flip(d['plus_two'], qmatmul(V2, minus2, q), Aminus2, M, q)
    print('Actual minus2B4 and plus2B4 verified from all global section identities and unit minors.', flush=True)

    torsion_name = 'p41_local47_torsion_certificate.json'
    traw = path.with_name(torsion_name).read_bytes()
    assert hashlib.sha256(traw).hexdigest() == ck['source_sha256'][torsion_name]
    torsion = json.loads(traw)
    field = FastRing(torsion['field_polynomial_ascending'], q)
    ii = field.element(model['sqrt_minus_one_lift'])
    MD = [[field.element(c) for c in row] for row in divs['cusp_values']]
    cvals, zvals = [], []
    for side, (seed, coeff) in enumerate(ck['norm_section_seeds_and_coefficients']):
        trace_coefficients(A1, seed, coeff, q)
        tvals = qmatmul(W, [[c] for c in coeff], q)
        assert all(sum(x*x for x in row[0]) % 47 for row in tvals)
        zv = [row[0] for row in qmatmul(cm4['coarse_point_values'], [[c] for c in coeff], q)]
        dv = [row[0] for row in field_qmatmul(MD, [[c] for c in coeff], field, ii)]
        assert zv == ck['norm_CM4_values'][side]
        assert dv == [field.element(c) for c in ck['norm_cusp_values'][side]]
        assert all(sum(x*x for x in c) % 47 for c in zv)
        assert all(any(x % 47 for x in c) for c in dv)
        zp, dp = (1, 0), field.one
        for c in zv:
            zp = qmul(zp, c, q)
        for c in dv:
            dp = field.mul(dp, c)
        zvals.append(zp)
        cvals.append(dp)
    nz = qmul(zvals[0], qinv(zvals[1], q), q)
    nd = field.mul(cvals[0], field.inverse(cvals[1]))
    assert list(nz) == ck['CM4_norm_ratio'] and nd == field.element(ck['cusp_norm_ratio'])
    norm = field.mul(field.add(field.element(nz[0]), field.scale(ii, nz[1])), field.inverse(nd))
    assert not any(norm[1:]) and norm[0] == ck['principal_B4_norm'] == 4666447
    t = (pow(norm[0], 46, q)-1) % q
    logarithm = (t-t*t*pow(2, -1, q)+t**3*pow(3, -1, q))*pow(46, -1, q) % q
    assert logarithm == ck['principal_B4_log47'] == 4643130 and logarithm % 47 == 0
    assert logarithm//47 % 47 == 43
    print('The actual principal Poincare norm and normalized47-adic logarithm verified.', flush=True)
    print('SHA256', hashlib.sha256(encoded).hexdigest(), flush=True)


if __name__ == '__main__':
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else
         Path(__file__).with_name('data')/'p41_group_operations47_certificate.json.gz')
