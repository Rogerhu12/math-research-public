#!/usr/bin/env python3
"""Run the genuine divisor chain at selected rational supersingular centers.

The published common degree125 divisor is reused unchanged.  Only the
final point restriction changes.  The existing exact scalar and formal
endpoint engines are called directly, so all principal sections can be
captured by p41_SS_Abel_with_transports47.py.
"""
import argparse
from pathlib import Path
import sys

import p41_ordinary_Abel_multiply47 as frozen

read, save, sha = frozen.read, frozen.save, frozen.sha
multiply = frozen.multiply
extract_Abel = frozen.extract_Abel


def based_points(a, atlas_path, common_path, disks, output):
    r, np, M = a.r, a.np, a.M
    from p41_formal47_multiply import point_hash
    common = read(common_path)
    assert common['complete19_actual_based_points']
    assert common['colon_rank'] == 125 and common['colon_dimension'] == 74
    for name, digest in a.inputs.items():
        if name in common['input_sha256']:
            assert common['input_sha256'][name] == digest
    DB = r.from_json(common['colon_coordinates'])
    fb_coeff = r.from_json(common['f_b_coefficients'])
    fb = r.mm(M['W'], fb_coeff)
    assert np.all(r.units(fb)) and DB[0].shape == (199, 74)
    assert len(r.rank_pivots(DB)[0]) == 74
    inverse_fb = r.inverse_values(fb)
    for raw in common['colon_test_section_coefficients']:
        section = r.from_json(raw)
        hv = r.mm(M['W'], section)
        scaled = r.mul(r.mul(hv, inverse_fb), M['V2'])
        residual = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        assert r.iszero(r.mm(residual, DB))
    raw_path = a.folder / 'data' / 'p41_cm_quadratic_jets47_raw.json.gz'
    base = next(x for x in read(raw_path)['records'] if x['label'] == 'P_minus3')
    vb = r.from_json([base['normalized_weight2_coefficients'][0]])
    db = r.from_json([base['normalized_weight2_coefficients'][1]])
    assert r.iszero(r.mm(vb, fb_coeff)) and r.units(r.mm(db, fb_coeff))[0, 0]
    atlas = read(atlas_path)
    assert atlas['complete_SS_rational_disk_inventory']
    known_CM_disks = {'SS_j0_10', 'SS_j44_02', 'SS_j9_19', 'SS_j9_11', 'SS_j10_05'}
    records = []
    for disk in disks:
        assert disk not in known_CM_disks
        rec = next(x for x in atlas['SS_disk_records'] if x['disk_id'] == disk)
        chart = atlas['charts'][rec['chart_0based']]
        row = rec['chart_row_0based']
        W = r.from_json([chart['W_coefficients_0to3'][0][row]])
        assert np.all(r.units(r.mm(W, fb_coeff)))
        assert np.all(r.units(r.mm(W, a.fc)))
        W = r.mul(W, r.inverse_values(r.mm(W, a.fc)))
        assert r.equal(r.mm(W, M['A1']), r.conjugate(W))
        # The selected center must avoid the complete old evaluation fibre.
        WW = r.mul(M['W'], r.inverse_values(r.mm(M['W'], a.fc)))
        matches = np.all((WW[0]-W[0]) % 47 == 0, axis=1) & np.all((WW[1]-W[1]) % 47 == 0, axis=1)
        assert not np.any(matches), 'Choose a different evaluation fibre; do not suppress unit assertions.'
        V2, _ = a.evaluate(W)
        restriction = r.mm(V2, DB)
        rr, cc = r.rank_pivots(restriction)
        assert len(rr) == 1
        K, _, _ = r.kernel_from_rows(r.rows(restriction, rr), rr, cc)
        E, er, _, _ = r.normalize(r.mm(DB, K), 73)
        A = r.rows(r.mm(M['A2'], r.conjugate(E)), er)
        assert r.equal(r.mm(E, A), r.mm(M['A2'], r.conjugate(E)))
        assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))
        assert r.iszero(r.mm(V2, E))
        V2b, _ = a.evaluate(vb)
        assert len(r.rank_pivots(r.mm(V2b, E))[0]) == 1
        records.append({
            'disk_id': disk, 'point_coordinates': r.to_json(E),
            'point_frobenius': r.to_json(A), 'point_sha256': point_hash(E, A),
            'normalization_rows_1based': [i+1 for i in er],
            'actual_divisor': 'E_P=div(f_b)-b+P; E_P-div(f0)=P-b+div(f_b/f0)',
            'source_atlas_record': rec,
            'actual_center_W_fc_normalized_mod47four': r.to_json(W),
            'all820_evaluation_rows_disjoint_mod47': True,
            'not_in_the_five_known_rational_CM_SS_disks': True,
        })
    out = {
        'result': 'R329', 'level': 41, 'auxiliary_prime': 47, 'precision': 4,
        'complete_selected_SS_actual_based_points': True,
        'selected_disks': disks, 'all_Abel_constants_complete': False,
        'f_b_coefficients': common['f_b_coefficients'],
        'f_b_derivative_at_b': common['f_b_derivative_at_b'],
        'common_degree125_divisor_reused_unchanged': True,
        'all_saved_colon_sections_reverified_on_current_model': True,
        'records': records,
        'input_sha256': dict(a.inputs, **{atlas_path.name: sha(atlas_path),
            common_path.name: sha(common_path), raw_path.name: sha(raw_path)}),
        'source_sha256': sha(__file__),
        'unchanged_underlying_multiply_and_extract_source_sha256': sha(frozen.__file__),
    }
    save(output, out)
    print('PASS actual selected SS based points', disks, 'SHA', sha(output), flush=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'SS-atlas', 'common-based-points', 'based-points', 'workdir']:
        ap.add_argument('--' + name, type=Path, required=True)
    ap.add_argument('--disk', action='append', required=True)
    ap.add_argument('--max-bits', type=int, default=304)
    ap.add_argument('--tiny', type=Path)
    ap.add_argument('--prepare-only', action='store_true')
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    args.workdir.mkdir(parents=True, exist_ok=True)
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_native_r2_linear47 import install
    install_exact_float_mm(r)
    linear_manifest = install(r, args.workdir / 'native-build')
    a = ActualModel(args.script_dir.resolve())
    a.linear_manifest = linear_manifest
    if args.based_points.exists():
        points = read(args.based_points)
        assert points['complete_selected_SS_actual_based_points']
        assert points['selected_disks'] == args.disk
        assert points['input_sha256'][args.SS_atlas.name] == sha(args.SS_atlas)
        assert points['input_sha256'][args.common_based_points.name] == sha(args.common_based_points)
    else:
        points = based_points(a, args.SS_atlas, args.common_based_points, args.disk, args.based_points)
    if args.prepare_only:
        return
    for disk in args.disk:
        point = next(p for p in points['records'] if p['disk_id'] == disk)
        checkpoint = args.workdir / (disk + '_multiply47.json.gz')
        data = multiply(a, point, args.based_points, checkpoint, args.max_bits)
        if data['bits_done'] == 304 and args.tiny is not None:
            output = args.workdir / (disk + '_Abel47.json.gz')
            if output.exists():
                completed = read(output)
                assert completed['complete_actual_center_Abel_constant']
                assert completed['input_sha256'][checkpoint.name] == sha(checkpoint)
            else:
                extract_Abel(a, data, checkpoint, args.tiny, output)


if __name__ == '__main__':
    main()
