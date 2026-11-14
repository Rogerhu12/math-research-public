#!/usr/bin/env python3
"""Independently replay the initial two flips using bounded integer matrices.

This rechecks the original point, the single removable source evaluation,
both rank126 colons, complete cross products, and the exact moving scale.
It does not claim a second scalar chain or any local height constant.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys


def read(path):
    p = Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_bytes())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'based-points', 'common-based-points', 'SS-atlas', 'output']:
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import ProjectiveJetFrames
    from p41_formal47_multiply import point_hash
    # Deliberately retain the original bounded int64 multiplication, not BLAS.
    assert not getattr(r.mm, 'exact_nonnegative_float64', False)
    a = ActualModel(args.script_dir)
    M = a.M
    frames = ProjectiveJetFrames(a, exact_blas=False)
    raw = read(args.based_points)
    common = read(args.common_based_points)
    atlas = read(args.SS_atlas)
    assert raw['complete_selected_SS_actual_based_points'] and raw['result'] == 'R399'
    for path in [args.common_based_points, args.SS_atlas]:
        assert raw['input_sha256'][path.name] == sha(path)
    for name, h in a.inputs.items():
        assert raw['input_sha256'][name] == h
    DB = r.from_json(common['colon_coordinates'])
    freeDB = [i for i in range(199) if i not in {j-1 for j in common['colon_rank_columns_1based']}]
    assert r.equal(r.rows(DB, freeDB), r.eye(74))
    fb = r.from_json(common['f_b_coefficients'])
    assert raw['f_b_coefficients'] == common['f_b_coefficients']
    fbval = r.mm(M['W'], fb)
    assert np.all(r.units(fbval))
    for coeff in common['colon_test_section_coefficients']:
        ratio = r.mul(r.mm(M['W'], r.from_json(coeff)), r.inverse_values(fbval))
        scaled = r.mul(ratio, M['V2'])
        assert r.iszero(r.mm(r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2']))), DB))
    family = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
    I12 = [[i-1 for i in f['points_1based']] for f in family['families']]
    WW = r.mul(M['W'], r.inverse_values(a.f))
    results = []

    def unit_minor(X, rows, cols, size):
        Y = r.cols(r.rows(X, rows), cols)
        assert Y[0].shape == (size, size)
        Yp = tuple(v % 47 for v in Y)
        inverse = r.inverse_matrix(Yp, 47)
        assert r.equal(r.mm(Yp, inverse, 47), r.eye(size))

    def rational_point(K, A):
        assert K[0].shape == (199, 73) and A[0].shape == (73, 73)
        assert r.equal(r.mm(K, A), r.mm(M['A2'], r.conjugate(K)))
        assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))

    for rec in raw['records']:
        disk = rec['disk_id']
        tr = rec['initial_moving_transport']
        f1 = tr['first_flip']
        index = rec['original_source_is_exact_evaluation_row_0based']
        ar = next(z for z in atlas['SS_disk_records'] if z['disk_id'] == disk)
        ch = atlas['charts'][ar['chart_0based']]
        P = r.from_json([ch['W_coefficients_0to3'][0][ar['chart_row_0based']]])
        assert r.equal(P, r.rows(WW, [index]))
        assert rec['actual_center_W_fc_normalized_mod47four'] == r.to_json(P)
        assert M['tau'][index] == index and all(index not in I for I in I12)
        E, AE = r.from_json(tr['original_point_coordinates']), r.from_json(tr['original_point_frobenius'])
        F, AF = r.from_json(f1['residual_point_coordinates']), r.from_json(f1['residual_point_frobenius'])
        Enew, Anew = r.from_json(rec['point_coordinates']), r.from_json(rec['point_frobenius'])
        for K, A in [(E, AE), (F, AF), (Enew, Anew)]:
            rational_point(K, A)
        assert [point_hash(E, AE), point_hash(F, AF), point_hash(Enew, Anew)] == [tr['original_point_sha256'], f1['residual_point_sha256'], rec['point_sha256']]
        assert r.equal(E, r.mm(DB, r.rows(E, freeDB)))
        V2P = a.evaluate(P)[0]
        assert r.iszero(r.mm(V2P, E))
        er, ec = r.rank_pivots(E)
        unit_minor(E, er, ec, 73)
        ES = r.mm(M['V2'], E)
        assert np.flatnonzero(~np.any(r.units(ES), axis=1)).tolist() == [index]
        J = frames.local_jets(P, r.from_json(f1['frame']), r.from_json(f1['coordinate']), order=2)
        assert [r.to_json(v) for v in J['W']] == f1['actual_P_W_jets_0to2']
        assert [r.to_json(v) for v in J['V2']] == f1['actual_P_V2_jets_0to2']
        assert np.any(r.units(r.mm(J['V2'][1], E)))
        fc, gc = r.from_json(f1['f_V2_coefficients']), r.from_json(f1['g_V2_coefficients'])
        for coeff, small, seed in [(fc, 'f_small_coefficients', 'f_seed'), (gc, 'g_small_coefficients', 'g_seed')]:
            c, s = r.from_json(f1[small]), r.from_json(f1[seed])
            assert r.equal(c, r.add(s, r.mm(AE, r.conjugate(s))))
            assert r.equal(coeff, r.mm(E, c))
            assert r.equal(r.mm(M['A2'], r.conjugate(coeff)), coeff)
        fv, gv = r.mm(M['V2'], fc), r.mm(M['V2'], gc)
        assert np.flatnonzero(~r.units(fv)[:, 0]).tolist() == [index]
        assert r.iszero(r.rows(fv, [index])) and r.iszero(r.rows(gv, [index]))
        fp, gp = r.mm(J['V2'][1], fc), r.mm(J['V2'][1], gc)
        assert np.all(r.units(fp)) and r.to_json(fp) == f1['actual_f_first_derivative']
        assert r.to_json(gp) == f1['actual_g_first_derivative']
        quotient_at_P = r.mul(gp, r.inverse_values(fp))
        ratio = r.from_json(f1['all820_ratio_values'])
        other = [i for i in range(820) if i != index]
        assert r.equal(r.rows(ratio, [index]), quotient_at_P)
        assert r.equal(r.rows(ratio, other), r.mul(r.rows(gv, other), r.inverse_values(r.rows(fv, other))))
        scaled = r.mul(ratio, M['V2'])
        R = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        assert f1['colon_rank'] == 126 and f1['colon_dimension'] == 73
        unit_minor(R, f1['rank_rows_0based'], f1['rank_columns_0based'], 126)
        assert r.iszero(r.mm(R, F)) and r.equal(r.rows(F, f1['free_columns_0based']), r.eye(73))
        FS = r.mm(M['V2'], F)
        assert np.all(np.any(r.units(FS), axis=1))
        H = r.from_json(f1['quotient_section_coordinates_for_all73_residual_basis'])
        HV = r.mm(M['V2'], H)
        assert r.equal(HV, r.mul(ratio, FS))
        assert r.equal(r.mul(fv, HV), r.mul(gv, FS))
        assert r.equal(r.mul(fp, r.mm(V2P, H)), r.mul(gp, r.mm(V2P, F)))
        second = tr['second_flip_witness']
        h = r.mm(F, r.column(second['f_coefficients']))
        g2 = r.mm(F, r.column(second['g_coefficients']))
        assert r.to_json(h) == tr['second_flip_h_V2_coefficients']
        hv, g2v = r.mm(M['V2'], h), r.mm(M['V2'], g2)
        assert np.all(r.units(hv))
        ratio2 = r.mul(g2v, r.inverse_values(hv))
        scaled2 = r.mul(ratio2, M['V2'])
        R2 = r.sub(scaled2, r.mm(M['V2'], r.rows(scaled2, M['P2'])))
        unit_minor(R2, [i-1 for i in second['rank_rows_1based']], [i-1 for i in second['rank_columns_1based']], 126)
        assert r.iszero(r.mm(R2, Enew))
        assert r.equal(r.rows(Enew, [i-1 for i in second['free_columns_1based']]), r.eye(73))
        assert np.all(np.any(r.units(r.mm(M['V2'], Enew)), axis=1))
        leading = r.mul(r.mul(r.mm(P, fb), r.mm(V2P, h)), r.inverse_values(fp))
        assert np.all(r.units(leading)) and r.to_json(leading) == tr['initial_function_chart_leading_unit_at_P']
        assert tr['initial_function_order_at_P'] == -1
        assert all(np.all(r.units(r.rows(fv, I))) and np.all(r.units(r.rows(hv, I))) for I in I12)
        results.append({'disk_id': disk, 'actual_evaluation_row_0based': index,
                        'both_actual_rank126_colons_and_full_kernel_dimensions': True,
                        'all820_by73_first_flip_cross_products': 820*73,
                        'all73_first_derivative_cross_products_at_removable_row': True,
                        'only_one_simple_nonunit_f_value_and_correct_removable_ratio': True,
                        'second_h_and_both_residual_divisors_disjoint_from_all820': True,
                        'same_original_V2_V3_bases_P2_P3_and_actual_point_class': True,
                        'initial_function': 'f_b*h/(f_c*f)', 'order_at_P': -1,
                        'chart_leading_unit_at_P': r.to_json(leading),
                        'all108_family_values_of_f_h_are_units': True,
                        'no_nonunit_or47_division': True})
        print('PASS independent integer moving flips', disk, flush=True)
    out = {'result': 'R399', 'all_four_initial_moving_transports_independently_replayed': True,
           'records': results, 'input_sha256': dict(a.inputs, **{str(p): sha(p) for p in [args.based_points, args.common_based_points, args.SS_atlas]}),
           'source_sha256': sha(__file__), 'arithmetic': 'Original bounded integer matrix multiplication; no exact-float BLAS installed.',
           'scope': 'Both actual initial flips and their full global basis/jet/divisor/scale certificates. No second 304-bit scalar chain, Norm evaluation, or local height claimed.'}
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    print('COMPLETE', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
