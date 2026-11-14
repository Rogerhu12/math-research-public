#!/usr/bin/env python3
"""R470: move the additional sixteen non-CM j9 based divisors on the unchanged model.

The first flip evaluates its one removable quotient by actual V2 jets.  The
second flip is the published unit flip.  Both complete V2 principal sections
are retained, so the initial function is f_b*h/(f_c*f), not f_b/f_c.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

Q = 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_bytes())


def save(path, value):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = p.with_suffix(p.suffix+'.new')
    temp.write_bytes(gzip.compress(data, mtime=0))
    temp.replace(p)
    return sha(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for n in ['script-dir', 'SS-atlas', 'common-based-points', 'based-points', 'workdir']:
        ap.add_argument('--'+n, type=Path, required=True)
    ap.add_argument('--disk', action='append', required=True)
    args = ap.parse_args()
    assert args.disk and len(args.disk)==len(set(args.disk))
    sys.path.insert(0, str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm, matrix_digest
    from p41_native_r2_linear47 import install
    from p41_formal47_multiply import point_hash
    from p41_group_operations47 import flip
    install_exact_float_mm(r)
    args.workdir.mkdir(parents=True, exist_ok=True)
    linear = install(r, args.workdir/'native')
    a = ActualModel(args.script_dir)
    M = a.M
    frames = ProjectiveJetFrames(a)
    common = read(args.common_based_points)
    atlas = read(args.SS_atlas)
    assert common['complete19_actual_based_points'] and common['colon_rank'] == 125
    DB = r.from_json(common['colon_coordinates'])
    fb = r.from_json(common['f_b_coefficients'])
    fbsource = r.mm(M['W'], fb)
    assert np.all(r.units(fbsource))
    for raw in common['colon_test_section_coefficients']:
        hv = r.mm(M['W'], r.from_json(raw))
        scaled = r.mul(r.mul(hv, r.inverse_values(fbsource)), M['V2'])
        residual = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        assert r.iszero(r.mm(residual, DB))
    family = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
    I12 = [[i-1 for i in f['points_1based']] for f in family['families']]
    cm = a.read('p41_cm_quadratic_jets47_raw.json.gz')
    base = next(v for v in cm['records'] if v['label'] == 'P_minus3')
    vb = r.from_json([base['normalized_weight2_coefficients'][0]])
    vb = r.mul(vb, r.inverse_values(r.mm(vb, a.fc)))
    V2b, _ = a.evaluate(vb)
    WW = r.mul(M['W'], r.inverse_values(a.f))
    records = []
    for disk in args.disk:
        assert disk in ['SS_j9_05', 'SS_j9_06', 'SS_j9_07', 'SS_j9_08', 'SS_j9_09', 'SS_j9_10', 'SS_j9_12', 'SS_j9_13', 'SS_j9_14', 'SS_j9_15', 'SS_j9_16', 'SS_j9_17', 'SS_j9_18', 'SS_j9_20', 'SS_j9_21', 'SS_j9_22']
        rec = next(z for z in atlas['SS_disk_records'] if z['disk_id'] == disk)
        chart = atlas['charts'][rec['chart_0based']]
        P = r.from_json([chart['W_coefficients_0to3'][0][rec['chart_row_0based']]])
        assert r.equal(r.mm(P, a.fc), r.column([[1, 0]]))
        assert r.equal(r.mm(P, M['A1']), r.conjugate(P))
        hit = np.flatnonzero(np.all((WW[0]-P[0]) % 47 == 0, axis=1) & np.all((WW[1]-P[1]) % 47 == 0, axis=1)).tolist()
        assert len(hit) == 1 and r.equal(r.rows(WW, hit), P)
        index = hit[0]
        assert M['tau'][index] == index
        assert all(index not in I for I in I12), 'A pole in an Abel calibration family needs a separate finite-part argument.'
        assert np.all(r.units(r.mm(P, fb)))
        J = frames.local_jets(P, r.from_json(chart['frame']), r.from_json(chart['coordinate']), order=2)
        assert r.equal(J['frame'], a.fc)
        V2P = J['V2'][0]
        restriction = r.mm(V2P, DB)
        rr, cc = r.rank_pivots(restriction)
        assert len(rr) == 1
        K, _, _ = r.kernel_from_rows(r.rows(restriction, rr), rr, cc)
        E, er, _, _ = r.normalize(r.mm(DB, K), 73)
        AE = r.rows(r.mm(M['A2'], r.conjugate(E)), er)
        assert r.equal(r.mm(E, AE), r.mm(M['A2'], r.conjugate(E)))
        assert r.equal(r.mm(AE, r.conjugate(AE)), r.eye(73))
        assert r.iszero(r.mm(V2P, E))
        assert np.any(r.units(r.mm(J['V2'][1], E)))
        assert len(r.rank_pivots(r.mm(V2b, E))[0]) == 1
        ES = r.mm(M['V2'], E)
        assert np.flatnonzero(~np.any(r.units(ES), axis=1)).tolist() == hit
        rng = random.Random(4104739900+int(disk[-2:]))
        other = [i for i in range(820) if i != index]
        for attempt in range(1, 101):
            seedf, cf = r.rational_trace(AE, rng)
            fcoef = r.mm(E, cf)
            fval = r.mm(M['V2'], fcoef)
            if not np.all(r.units(r.rows(fval, other))):
                continue
            assert r.iszero(r.rows(fval, hit))
            fp = r.mm(J['V2'][1], fcoef)
            if not np.all(r.units(fp)) or not np.all(r.units(r.mm(V2b, fcoef))):
                continue
            seedg, cg = r.rational_trace(AE, rng)
            gcoef = r.mm(E, cg)
            gval = r.mm(M['V2'], gcoef)
            assert r.iszero(r.rows(gval, hit))
            gp = r.mm(J['V2'][1], gcoef)
            ratio = r.zeros(820, 1)
            values = r.mul(r.rows(gval, other), r.inverse_values(r.rows(fval, other)))
            removable = r.mul(gp, r.inverse_values(fp))
            for k in range(2):
                ratio[k][other, :] = values[k]
                ratio[k][index, 0] = removable[k][0, 0]
            scaled = r.mul(ratio, M['V2'])
            residual = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
            rr, cc = r.rank_pivots(residual)
            if len(rr) != 126:
                continue
            F, free, block = r.kernel_from_rows(r.rows(residual, rr), rr, cc)
            assert r.iszero(r.mm(residual, F))
            AF = r.rows(r.mm(M['A2'], r.conjugate(F)), free)
            assert r.equal(r.mm(F, AF), r.mm(M['A2'], r.conjugate(F)))
            assert r.equal(r.mm(AF, r.conjugate(AF)), r.eye(73))
            FS = r.mm(M['V2'], F)
            assert np.all(np.any(r.units(FS), axis=1))
            quotient = r.rows(r.mm(scaled, F), M['P2'])
            qval = r.mm(M['V2'], quotient)
            assert r.equal(qval, r.mul(ratio, FS))
            assert r.equal(r.mul(fval, qval), r.mul(gval, FS))
            # At the sole removable row the differentiated identity has unit f'.
            assert r.equal(r.mul(fp, r.mm(V2P, quotient)), r.mul(gp, r.mm(V2P, F)))
            break
        else:
            raise AssertionError('No full-rank actual first moving flip with one simple removable row')
        moved, Amoved, second = flip(FS, AF, M, rng, disk+' moving second flip')
        hcoef = r.mm(F, r.column(second['f_coefficients']))
        hval = r.mm(M['V2'], hcoef)
        assert np.all(r.units(hval))
        assert np.all(np.any(r.units(r.mm(M['V2'], moved)), axis=1))
        assert r.equal(r.mm(M['A2'], r.conjugate(fcoef)), fcoef)
        assert r.equal(r.mm(M['A2'], r.conjugate(gcoef)), gcoef)
        assert r.equal(r.mm(M['A2'], r.conjugate(hcoef)), hcoef)
        original_hash, residual_hash, moved_hash = point_hash(E, AE), point_hash(F, AF), point_hash(moved, Amoved)
        # f_b*h/(f_c*f) has a simple pole at P with this genuine chart leading unit.
        initial_leading = r.mul(r.mul(r.mm(P, fb), r.mm(V2P, hcoef)), r.inverse_values(fp))
        assert np.all(r.units(initial_leading))
        assert all(np.all(r.units(r.rows(fval, I))) and np.all(r.units(r.rows(hval, I))) for I in I12)
        first = {'attempt': attempt, 'f_seed': r.to_json(seedf), 'f_small_coefficients': r.to_json(cf),
                 'g_seed': r.to_json(seedg), 'g_small_coefficients': r.to_json(cg),
                 'f_V2_coefficients': r.to_json(fcoef), 'g_V2_coefficients': r.to_json(gcoef),
                 'sole_nonunit_source_row_0based': index, 'all_other819_f_values_unit': True,
                 'f_and_g_values_at_source_point_exactly_zero_mod47four': True,
                 'actual_f_first_derivative': r.to_json(fp), 'actual_g_first_derivative': r.to_json(gp),
                 'removable_g_over_f_value': r.to_json(removable),
                 'all820_ratio_values': r.to_json(ratio),
                 'ratio_values_sha256': matrix_digest(ratio),
                 'actual_P_W_jets_0to2': [r.to_json(v) for v in J['W']],
                 'actual_P_V2_jets_0to2': [r.to_json(v) for v in J['V2']],
                 'frame': r.to_json(J['frame']), 'coordinate': r.to_json(J['coordinate']),
                 'colon_rank': 126, 'colon_dimension': 73,
                 'rank_rows_0based': rr, 'rank_columns_0based': cc, 'free_columns_0based': free,
                 'kernel_block': r.to_json(block),
                 'quotient_section_coordinates_for_all73_residual_basis': r.to_json(quotient),
                 'all820_by73_global_cross_products_and_interpolation_verified': True,
                 'actual_first_derivative_cross_products_at_removable_row': True,
                 'residual_point_coordinates': r.to_json(F), 'residual_point_frobenius': r.to_json(AF),
                 'residual_point_sha256': residual_hash, 'residual_divisor_disjoint_from_all820': True,
                 'division_by47_or_nonunit_f_value': False}
        transport = {'first_flip': first, 'second_flip_witness': second,
                     'second_flip_h_V2_coefficients': r.to_json(hcoef),
                     'second_flip_h_unit_on_all820': True,
                     'original_point_coordinates': r.to_json(E), 'original_point_frobenius': r.to_json(AE),
                     'original_point_sha256': original_hash,
                     'original_divisor': 'E=div(f_b)-b+P',
                     'first_divisor_identity': 'div(f)=E+F',
                     'second_divisor_identity': 'div(h)=F+E_moved',
                     'moving_ratio_divisor': 'div(h/f)=E_moved-E',
                     'initial_principal_function': 'f_b*h/(f_c*f)',
                     'initial_principal_divisor': 'E_moved-div(f_c)-(P-b)',
                     'initial_function_order_at_P': -1,
                     'initial_function_chart_leading_unit_at_P': r.to_json(initial_leading),
                     'both_Abel_calibration_families_disjoint_from_P': True,
                     'f_and_h_units_on_all108_Abel_calibration_points': True}
        record = {'disk_id': disk, 'point_coordinates': r.to_json(moved), 'point_frobenius': r.to_json(Amoved),
                  'point_sha256': moved_hash, 'actual_divisor': 'E_moved=E+div(h/f); E-div(f_c)=(P-b)+div(f_b/f_c)',
                  'source_atlas_record': rec, 'actual_center_W_fc_normalized_mod47four': r.to_json(P),
                  'original_source_is_exact_evaluation_row_0based': index,
                  'moved_divisor_disjoint_from_all820_evaluation_rows_mod47': True,
                  'initial_moving_transport': transport}
        records.append(record)
        result = {'result': 'R470', 'level': 41, 'auxiliary_prime': 47, 'precision': 4,
                  'complete_selected_SS_actual_based_points': len(records) == len(args.disk),
                  'selected_disks': args.disk, 'completed_disks': [v['disk_id'] for v in records],
                  'f_b_coefficients': common['f_b_coefficients'], 'f_b_derivative_at_b': common['f_b_derivative_at_b'],
                  'common_degree125_divisor_reused_unchanged': True,
                  'all_saved_colon_sections_reverified_on_current_model': True,
                  'unchanged_original820_V2_V3_bases_and_P2_P3_normalizations': True,
                  'all_Abel_constants_complete': False, 'records': records,
                  'input_sha256': dict(a.inputs, **{args.SS_atlas.name: sha(args.SS_atlas), args.common_based_points.name: sha(args.common_based_points)}),
                  'source_sha256': sha(__file__), 'linear_algebra': linear}
        print('PASS actual two flips', disk, 'source row', index, 'first attempt', attempt,
              'SHA', save(args.based_points, result), flush=True)


if __name__ == '__main__':
    main()
