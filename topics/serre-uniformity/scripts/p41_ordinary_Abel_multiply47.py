#!/usr/bin/env python3
"""Actual based ordinary points and resumable finite-field-order multiplication.

All inputs are genuine R231 rational curve centers.  No point's Abel
constant is assigned without a completed multiplication and formal chart
extraction.  Each scalar-prefix checkpoint is independently resumable.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    path = Path(path)
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(raw, mtime=0)
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(packed)
    temp.replace(path)
    return sha(path)


def based_points(a, atlas_path, output):
    """One actual degree125 divisor shared by all19 degree126 based points."""
    r, np, M = a.r, a.np, a.M
    from p41_formal47_multiply import point_hash
    jets_path = a.folder/'data/p41_cm_quadratic_jets47_raw.json.gz'
    jets = read(jets_path)
    base = jets['records'][0]
    assert base['label'] == 'P_minus3'
    vb = r.from_json([base['normalized_weight2_coefficients'][0]])
    db = r.from_json([base['normalized_weight2_coefficients'][1]])
    atlas = read(atlas_path)
    assert atlas['all19_actual_references_and_projective_jets_complete']
    points = atlas['ordinary_disk_records']
    raw_W = []
    for point in points:
        ch = atlas['charts'][point['chart_0based']]
        raw_W.append(ch['W_coefficients_0to3'][0][point['chart_row_0based']])
    W = r.from_json(raw_W)
    assert W[0].shape == (19, 73)
    rr, cc = r.rank_pivots(vb)
    HB, free, block = r.kernel_from_rows(r.rows(vb, rr), rr, cc)
    assert HB[0].shape == (73, 72) and r.iszero(r.mm(vb, HB))
    AH = r.rows(r.mm(M['A1'], r.conjugate(HB)), free)
    assert r.equal(r.mm(HB, AH), r.mm(M['A1'], r.conjugate(HB)))
    rng = random.Random(2380041)
    for attempt in range(1, 1001):
        seed, small = r.rational_trace(AH, rng)
        fb_coeff = r.mm(HB, small)
        fb = r.mm(M['W'], fb_coeff)
        if (np.all(r.units(fb)) and np.all(r.units(r.mm(W, fb_coeff)))
                and r.units(r.mm(db, fb_coeff))[0, 0]):
            break
    else:
        raise RuntimeError('No simple f_b disjoint from all actual ordinary centers and source evaluations')
    assert r.iszero(r.mm(vb, fb_coeff))
    assert r.equal(r.mm(M['A1'], r.conjugate(fb_coeff)), fb_coeff)
    inverse_fb = r.inverse_values(fb)
    constraints, colon_sections = [], []
    for trial in range(1, 11):
        hs, hcsmall = r.rational_trace(AH, rng)
        hc = r.mm(HB, hcsmall)
        hv = r.mm(M['W'], hc)
        scaled = r.mul(r.mul(hv, inverse_fb), M['V2'])
        residual = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        constraints.append(residual)
        colon_sections.append(r.to_json(hc))
        R = tuple(np.vstack([val[c] for val in constraints]) for c in range(2))
        rr, cc = r.rank_pivots(R)
        assert len(rr) <= 125
        if len(rr) == 125:
            break
    else:
        raise RuntimeError('Actual common colon did not attain dimension74')
    DB, ff, bb = r.kernel_from_rows(r.rows(R, rr), rr, cc)
    assert DB[0].shape == (199, 74) and r.iszero(r.mm(R, DB))
    V2, V3 = a.evaluate(W)
    records = []
    for row, point in enumerate(points):
        restriction = r.mm(r.rows(V2, [row]), DB)
        pr, pc = r.rank_pivots(restriction)
        assert len(pr) == 1
        reduced, efree, eblock = r.kernel_from_rows(r.rows(restriction, pr), pr, pc)
        E = r.mm(DB, reduced)
        E, er, ec, change = r.normalize(E, 73)
        A = r.rows(r.mm(M['A2'], r.conjugate(E)), er)
        assert r.equal(r.mm(E, A), r.mm(M['A2'], r.conjugate(E)))
        assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))
        assert r.iszero(r.mm(r.rows(V2, [row]), E))
        V2b, V3b = a.evaluate(vb)
        assert len(r.rank_pivots(r.mm(V2b, E))[0]) == 1
        records.append({'disk_id': point['disk_id'],
                        'point_coordinates': r.to_json(E), 'point_frobenius': r.to_json(A),
                        'point_sha256': point_hash(E, A),
                        'normalization_rows_1based': [j+1 for j in er],
                        'actual_divisor': 'E_P=div(f_b)-b+P; E_P-div(f0)=P-b+div(f_b/f0)'})
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
           'complete19_actual_based_points': True, 'all_Abel_constants_complete': False,
           'f_b_attempt': attempt, 'f_b_coefficients': r.to_json(fb_coeff),
           'f_b_derivative_at_b': r.to_json(r.mm(db, fb_coeff)),
           'f_b_at19_ordinary_centers': r.to_json(r.mm(W, fb_coeff)),
           'colon_trials': trial, 'colon_rank': 125, 'colon_dimension': 74,
           'colon_test_section_coefficients': colon_sections,
           'colon_rank_rows_1based': [j+1 for j in rr],
           'colon_rank_columns_1based': [j+1 for j in cc],
           'colon_coordinates': r.to_json(DB), 'records': records,
           'input_sha256': dict(a.inputs, **{atlas_path.name: sha(atlas_path), jets_path.name: sha(jets_path)}),
           'source_sha256': sha(__file__),
           'linear_algebra': a.linear_manifest}
    save(output, out)
    print('PASS actual19 based ordinary points; common colon dimension74; f_b attempt', attempt, 'SHA', sha(output), flush=True)
    return out


def multiply(a, point, input_path, checkpoint, max_bits=304):
    r, M = a.r, a.M
    from p41_formal47_multiply import H, addflip, point_hash, restore_tuple, zero_test_mod47
    from p41_group_operations47 import flip
    rng = random.Random(2380047+int(point['disk_id'][-2:]))
    bits = bin(H)[2:]
    K0, A0 = r.from_json(point['point_coordinates']), r.from_json(point['point_frobenius'])
    assert point_hash(K0, A0) == point['point_sha256']
    K, A = K0, A0
    if checkpoint.exists():
        data = read(checkpoint)
        assert data['target_multiplier'] == H and data['input_sha256'] == sha(input_path)
        assert data['input_point_sha256'] == point['point_sha256']
        K, A = r.from_json(data['point_coordinates']), r.from_json(data['point_frobenius'])
        negative, Anegative = r.from_json(data['negative_input_coordinates']), r.from_json(data['negative_input_frobenius'])
        assert point_hash(K, A) == data['point_sha256']
        rng.setstate(restore_tuple(data['random_state']))
        assert data['magnitude'] == int(bits[:data['bits_done']], 2)
        print('Resuming', point['disk_id'], data['bits_done'], '/', len(bits), 'bits', flush=True)
    else:
        negative, Anegative, negative_record = flip(r.mm(M['V2'], K0), A0, M, rng, point['disk_id']+' initial negative')
        data = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
                'disk_id': point['disk_id'], 'target_multiplier': H, 'target_bits': len(bits),
                'bits_done': 1, 'sign': 1, 'magnitude': 1, 'steps': [],
                'input_sha256': sha(input_path), 'input_point_sha256': point['point_sha256'],
                'negative_input_coordinates': r.to_json(negative), 'negative_input_frobenius': r.to_json(Anegative),
                'negative_input_witness': negative_record,
                'status': 'incomplete actual scalar multiplication; no Abel constant claimed',
                'point_coordinates': r.to_json(K), 'point_frobenius': r.to_json(A),
                'point_sha256': point_hash(K, A), 'random_state': rng.getstate(),
                'linear_algebra': a.linear_manifest}
        save(checkpoint, data)
    start = time.monotonic()
    start_steps = len(data['steps'])
    for n in range(data['bits_done'], min(len(bits), max_bits)):
        before = time.monotonic()
        K, A, witness = addflip(K, A, K, A, M, rng, point['disk_id']+' double bit'+str(n+1), same=True)
        data['sign'] *= -1
        data['magnitude'] *= 2
        witness.update(operation='double', bit=n+1, sign=data['sign'], seconds=time.monotonic()-before)
        data['steps'].append(witness)
        if bits[n] == '1':
            B, AB = (K0, A0) if data['sign'] == 1 else (negative, Anegative)
            before = time.monotonic()
            K, A, witness = addflip(K, A, B, AB, M, rng, point['disk_id']+' add bit'+str(n+1))
            data['sign'] *= -1
            data['magnitude'] += 1
            witness.update(operation='add', bit=n+1, sign=data['sign'], seconds=time.monotonic()-before)
            data['steps'].append(witness)
        data['bits_done'] = n+1
        assert data['magnitude'] == int(bits[:n+1], 2)
        data['point_coordinates'], data['point_frobenius'] = r.to_json(K), r.to_json(A)
        data['point_sha256'] = point_hash(K, A)
        data['random_state'] = rng.getstate()
        data['source_sha256'] = sha(__file__)
        save(checkpoint, data)
        if (n+1) % 5 == 0 or n+1 == min(len(bits), max_bits):
            count = len(data['steps'])-start_steps
            print('CHECKPOINT', point['disk_id'], n+1, '/', len(bits), 'bits;', len(data['steps']), 'operations;',
                  'elapsed', round(time.monotonic()-start, 2), 'mean operation', round((time.monotonic()-start)/count, 3),
                  'SHA', sha(checkpoint), flush=True)
    if data['bits_done'] == len(bits) and 'zero_test_mod47' not in data:
        data['zero_test_mod47'] = zero_test_mod47(K, M)
        data['status'] = 'complete actual signed m*C; full zero test mod47 passed; Abel extraction pending'
        save(checkpoint, data)
        print('PASS formal group entry', point['disk_id'], 'SHA', sha(checkpoint), flush=True)
    return data


def extract_Abel(a, multiple, multiplication_path, tiny_path, output):
    """Cubic-cancelled actual formal logarithm in the R121 canonical basis."""
    r, np, M = a.r, a.np, a.M
    from p41_formal47_multiply import H, addflip, point_hash, zero_test_mod47
    from p41_group_operations47 import flip
    from p41_formal47_chart import make_chart, evaluate_chart, chart_record
    calibration_path = a.folder/'data/p41_abel_tangents47_checkpoint.json.gz'
    calibration = read(calibration_path)
    tiny = read(tiny_path)
    assert tiny['complete_all129_tiny_Abel_integrals']
    assert multiple['target_multiplier'] == multiple['magnitude'] == H
    assert multiple['bits_done'] == multiple['target_bits'] == 304
    assert 'zero_test_mod47' in multiple
    assert calibration['directions'] == 54
    for name in ['p41_makdisi47_certificate.json.gz', 'p41_cusp_divisors47_certificate.json.gz',
                 'p41_cm4_divisor47_certificate.json', 'p41_group47_checkpoint.json.gz']:
        assert calibration['source_sha256'][name] == a.inputs[name]
    chart = make_chart(M, a.model)
    assert chart_record(chart) == calibration['chart']
    K, A = r.from_json(multiple['point_coordinates']), r.from_json(multiple['point_frobenius'])
    assert point_hash(K, A) == multiple['point_sha256']
    assert r.equal(r.mm(K, A), r.mm(M['A2'], r.conjugate(K)))
    assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))
    zero_test = zero_test_mod47(K, M)
    rng = random.Random(2380147+int(multiple['disk_id'][-2:]))
    negative, Anegative, negative_witness = flip(r.mm(M['V2'], K), A, M, rng, multiple['disk_id']+' formal -Y')
    negative_two, Anegative_two, double_witness = addflip(K, A, K, A, M, rng, multiple['disk_id']+' formal -2Y', same=True)
    matrices, chart_witnesses = [], []
    for coords, descent, label in [(K, A, 'Y'), (negative, Anegative, '-Y'), (negative_two, Anegative_two, '-2Y')]:
        value, witness = evaluate_chart(coords, descent, M, chart, rng)
        F = r.sub(value, chart['U0'])
        assert all(np.all(x % 47 == 0) for x in F)
        matrices.append(F)
        chart_witnesses.append(witness)
        print('Actual formal chart', multiple['disk_id'], label, flush=True)
    Lie = a.scale(r.add(r.sub(a.scale(matrices[0], 2), a.scale(matrices[1], 6)), matrices[2]), pow(6, -1, r.Q))
    assert all(np.all(x % 47 == 0) for x in Lie)
    selected = [n-1 for n in calibration['flattened_chart_coordinate_indices_1based']]
    L = r.cols((Lie[0].reshape(1, -1), Lie[1].reshape(1, -1)), selected)
    transform = r.from_json(calibration['chart_to_differential_transform'])
    logY = r.mm(L, transform)
    logC = a.scale(logY, multiple['sign']*pow(H, -1, r.Q))
    AK = r.from_json(a.cusp['canonical_frobenius_matrix'])
    assert r.equal(r.mm(logC, AK), r.conjugate(logC))
    assert all(np.all(x % 47 == 0) for x in logC)
    inverse = r.from_json(tiny['divided_Lie_to_cyclic_mod47cubed'], 47**3)
    divided = tuple(x//47 for x in logC)
    cyclic = r.mm(divided, inverse, 47**3)
    assert not np.any(cyclic[1])
    forward = r.from_json(tiny['cyclic_to_divided_Lie_mod47cubed'], 47**3)
    assert r.equal(r.mm(cyclic, forward, 47**3), divided)
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
           'disk_id': multiple['disk_id'], 'actual_based_class': 'C=P_center-P_minus3',
           'complete_actual_center_Abel_constant': True,
           'complete_local_QC_heights': False, 'complete_common_roots': False,
           'actual_center_C_cyclic_coordinates_mod47cubed': cyclic[0][0].astype(int).tolist(),
           'canonical_log_C_mod47four': r.to_json(logC),
           'canonical_log_signed_mC_mod47four': r.to_json(logY),
           'target_multiplier': H, 'actual_multiple_sign': multiple['sign'],
           'actual_multiple_point_sha256': multiple['point_sha256'],
           'zero_test_mod47': zero_test, 'negative_witness': negative_witness,
           'negative_two_witness': double_witness, 'formal_chart_witnesses': chart_witnesses,
           'selected_Lie_coordinates': r.to_json(L),
           'all54_cyclic_coordinates_rational': True,
           'cyclic_to_Lie_roundtrip_verified': True,
           'formula': 'log C=sign/m * d_chart(2F(Y)-6F(-Y)+F(-2Y))/6 mod47^4; Y=sign*m*C',
           'input_sha256': dict(a.inputs, **{multiplication_path.name: sha(multiplication_path),
                                           calibration_path.name: sha(calibration_path), tiny_path.name: sha(tiny_path)}),
           'linear_algebra': a.linear_manifest, 'source_sha256': sha(__file__)}
    save(output, out)
    print('PASS actual ordinary Abel constant', multiple['disk_id'], 'SHA', sha(output), flush=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--ordinary-atlas', type=Path, required=True)
    ap.add_argument('--based-points', type=Path, required=True)
    ap.add_argument('--workdir', type=Path, required=True)
    ap.add_argument('--disk', action='append')
    ap.add_argument('--max-bits', type=int, default=304)
    ap.add_argument('--tiny', type=Path)
    ap.add_argument('--no-native', action='store_true')
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    args.workdir.mkdir(parents=True, exist_ok=True)
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    install_exact_float_mm(r)
    if not args.no_native:
        from p41_native_r2_linear47 import install
        linear_manifest = install(r, args.workdir/'native-build')
    else:
        linear_manifest = {'method': 'published NumPy exact integer Gaussian elimination'}
    a = ActualModel(args.script_dir.resolve())
    a.linear_manifest = linear_manifest
    if args.based_points.exists():
        points = read(args.based_points)
        assert points['complete19_actual_based_points']
        assert points['input_sha256'][args.ordinary_atlas.name] == sha(args.ordinary_atlas)
    else:
        points = based_points(a, args.ordinary_atlas, args.based_points)
    if not args.disk:
        return
    for disk_id in args.disk:
        point = next(p for p in points['records'] if p['disk_id'] == disk_id)
        checkpoint = args.workdir/(disk_id+'_multiply47.json.gz')
        data = multiply(a, point, args.based_points, checkpoint, args.max_bits)
        if data['bits_done'] == 304 and args.tiny is not None:
            output = args.workdir/(disk_id+'_Abel47.json.gz')
            if output.exists():
                completed = read(output)
                assert completed['complete_actual_center_Abel_constant'] and completed['input_sha256'][checkpoint.name] == sha(checkpoint)
                print('Already complete', disk_id, 'SHA', sha(output), flush=True)
            else:
                extract_Abel(a, data, checkpoint, args.tiny, output)


if __name__ == '__main__':
    main()
