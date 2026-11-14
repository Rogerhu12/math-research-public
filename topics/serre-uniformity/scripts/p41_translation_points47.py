#!/usr/bin/env python3
"""Actual B_minus8 and U_b=20*b-D, with the missing CM-basepoint jets.

The saved R160 parameter and its 71 equations are kept exactly.  No new
torsion computation or guess of a divisor class is used.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--discs', type=Path)
    parser.add_argument('--cm8', type=Path)
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_translation_points47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_cm4_divisor47 import kernel
    from p41_poincare_norms47 import determinant
    from p41_formal47_multiply import write_checkpoint, point_hash
    start = time.monotonic()
    sources, hashes = load_sources(folder/'data')
    M = make_model(sources)
    divisors = sources[1]
    discs, discs_sha = read(args.discs or folder/'data/p41_cm_quadratic_jets47_raw.json.gz')
    cm8, cm8_sha = read(args.cm8 or folder/'data/p41_cm8_q2_support47_verified.json.gz')
    assert discs['source_sha256'] == hashes
    assert discs['point_source_sha256']['p41_cm8_q2_support47_verified.json.gz'] == cm8_sha
    b = next(rec for rec in discs['records'] if rec['label'] == 'P_minus3')
    assert b['order'] >= 16
    K1 = r.from_json(kernel(73, divisors['cusp_rank_columns_1based'],
                            divisors['cusp_free_columns_1based'], divisors['canonical_kernel_block']))
    fc = r.mm(K1, r.column(divisors['canonical_coefficients']))
    KI = r.from_json(kernel(199, divisors['K_rank_columns_1based'],
                            divisors['K_free_columns_1based'], divisors['K_kernel_block']))
    square_pairs = [(a-1, c-1) for a, c in divisors['square_basis_monomials_1based']]
    pairs = [(a-1, c-1) for a, c in b['selected_quadric_pairs_1based']]
    assert len(pairs) == 71
    S = r.from_json(divisors['square_basis_inverse'])
    wp = r.rows(M['W'], M['P2'])
    coefficients = r.mul(r.cols(wp, [a for a, c in pairs]), r.cols(wp, [c for a, c in pairs]))
    H = r.mm(S, coefficients)
    # The selected equations are global identities in the actual degree252
    # line bundle, certified by the 820-point faithful evaluation.
    actual = r.mul(r.cols(M['W'], [a for a, c in pairs]), r.cols(M['W'], [c for a, c in pairs]))
    assert r.equal(actual, r.mm(M['V2'], coefficients))
    transpose = lambda x: (x[0].T.copy(), x[1].T.copy())

    def monomial(x, y, indices):
        return transpose(r.mul(r.rows(x, [a for a, c in indices]), r.rows(y, [c for a, c in indices])))

    x0 = r.column(b['normalized_weight2_coefficients'][0])
    uc = r.from_json(b['parameter_coefficients'])
    grad = r.zeros(73, 71)
    grad_square = r.zeros(73, 199)
    for target, indices in [(grad, pairs), (grad_square, square_pairs)]:
        for k, (a, c) in enumerate(indices):
            for z in range(2):
                target[z][a, k] = (target[z][a, k]+x0[z][c, 0]) % r.Q
                target[z][c, k] = (target[z][c, k]+x0[z][a, 0]) % r.Q
    jac = transpose(r.sub(grad, r.mm(grad_square, H)))
    J = (np.vstack([jac[0], fc[0].T, uc[0].T]), np.vstack([jac[1], fc[1].T, uc[1].T]))
    Ji = r.inverse_matrix(J)
    assert r.equal(r.mm(J, Ji), r.eye(73))
    assert determinant(J) == b['unit_jacobian_determinant']
    jets = [x0]
    for k in range(1, 20):
        nonlinear = r.zeros(1, 71)
        for j in range(1, k):
            nonlinear = r.add(nonlinear, r.sub(monomial(jets[j], jets[k-j], pairs),
                                               r.mm(monomial(jets[j], jets[k-j], square_pairs), H)))
        rhs = r.zeros(73, 1)
        for z in range(2):
            rhs[z][:71, 0] = -nonlinear[z][0] % r.Q
        rhs[0][72, 0] = int(k == 1)
        value = r.mm(Ji, rhs)
        if k < len(b['normalized_weight2_coefficients']):
            assert r.to_json(transpose(value))[0] == b['normalized_weight2_coefficients'][k]
        jets.append(value)
    Vb = []
    for k in range(20):
        square = r.zeros(1, 199)
        selected = r.zeros(1, 71)
        for j in range(k+1):
            square = r.add(square, monomial(jets[j], jets[k-j], square_pairs))
            selected = r.add(selected, monomial(jets[j], jets[k-j], pairs))
        assert r.equal(selected, r.mm(square, H))
        assert r.equal(r.mm(transpose(jets[k]), M['A1']), r.conjugate(transpose(jets[k])))
        assert r.equal(r.mm(transpose(fc), jets[k]), r.eye(1) if k == 0 else r.zeros(1, 1))
        if k:
            assert r.equal(r.mm(transpose(uc), jets[k]), r.eye(1) if k == 1 else r.zeros(1, 1))
        Vb.append(r.mm(square, S))
    restriction_b = (np.vstack([v[0] for v in Vb]), np.vstack([v[1] for v in Vb]))
    W8 = r.from_json(cm8['weight2_evaluation_coefficients'][0])
    canonical_values = r.mm(W8, fc)
    assert np.all(r.units(canonical_values))
    restriction_8 = r.mm(r.mul(r.cols(W8, [a for a, c in square_pairs]),
                              r.cols(W8, [c for a, c in square_pairs])), S)
    tau8 = [j-1 for j in cm8['fixed_frobenius_permutation_1based']]
    assert r.equal(r.mm(restriction_8, M['A2']), r.conjugate(r.rows(restriction_8, tau8)))

    def actual_point(label, restriction, effective, divisor):
        matrix = r.mm(restriction, KI)
        rows, cols = r.rank_pivots(matrix)
        assert len(rows) == 20
        ker, free, block = r.kernel_from_rows(r.rows(matrix, rows), rows, cols)
        assert len(free) == 73 and r.iszero(r.mm(matrix, ker))
        coordinates, normalized_rows, normalized_cols, change = r.normalize(r.mm(KI, ker), 73)
        assert normalized_cols == list(range(73))
        frobenius = r.rows(r.mm(M['A2'], r.conjugate(coordinates)), normalized_rows)
        assert r.equal(r.mm(coordinates, frobenius), r.mm(M['A2'], r.conjugate(coordinates)))
        assert r.equal(r.mm(frobenius, r.conjugate(frobenius)), r.eye(73))
        assert r.iszero(r.mm(restriction, coordinates))
        minor = r.cols(r.rows(matrix, rows), cols)
        inverse = r.inverse_matrix(minor)
        assert r.equal(r.mm(minor, inverse), r.eye(20))
        return {'point_label': label, 'effective_divisor': effective, 'actual_degree_zero_divisor': divisor,
                'point_coordinates': r.to_json(coordinates), 'point_frobenius': r.to_json(frobenius),
                'point_sha256': point_hash(coordinates, frobenius),
                'restriction_rank': 20, 'rank_columns_1based': [i+1 for i in cols],
                'unit_minor_determinant_mod47four': determinant(minor),
                'unit_minor_inverse': r.to_json(inverse),
                'restriction_kernel_block_sha256': hashlib.sha256(json.dumps(r.to_json(block), separators=(',', ':')).encode()).hexdigest()}

    records = [actual_point('B_minus8', restriction_8, 'K_f+Z_minus8', 'Z_minus8-D_cusp'),
               actual_point('U_b', restriction_b, 'K_f+20*P_minus3', '20*P_minus3-D_cusp')]
    encoded_jets = [r.to_json(transpose(v))[0] for v in jets]
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
              'input_sha256': {'R160_discs': discs_sha, 'actual_CM8': cm8_sha},
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'base_divisor': 'D0=K_f+D_cusp', 'line_bundle_degree': 126,
              'canonical_values_at_CM8': r.to_json(canonical_values),
              'b_parameter_coefficients': b['parameter_coefficients'],
              'b_selected_quadric_pairs_1based': b['selected_quadric_pairs_1based'],
              'b_unit_jacobian_determinant': b['unit_jacobian_determinant'],
              'b_normalized_weight2_jets_through19': encoded_jets,
              'b_jet_sha256': hashlib.sha256(json.dumps(encoded_jets, separators=(',', ':')).encode()).hexdigest(),
              'all_original_b_jets_preserved': True,
              'records': records,
              'status': 'actual complete integral degree126 divisor ideals for B_minus8 and U_b; original R160 parameter extended exactly through order19; no height claimed'}
    sha, size = write_checkpoint(args.output, result)
    print('ACTUAL TRANSLATION INPUT POINTS PASS', [(v['point_label'], v['point_sha256']) for v in records],
          'bytes', size, 'sha', sha, 'seconds', round(time.monotonic()-start, 2),
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
