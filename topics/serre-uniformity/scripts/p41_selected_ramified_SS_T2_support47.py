#!/usr/bin/env python3
"""True T2 support at a rational SS atlas center above ramified coarse j=0 or1728.

Recover the physical deformation by its etale rational coordinate, match
all 73 source coordinates, and perform actual Velu and full-level transport.
No assertion identifying the source with an unshifted reference is suppressed.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'work-dir', 'output']:
        ap.add_argument('--' + name, type=Path, required=True)
    ap.add_argument('--disk-id', required=True)
    ap.add_argument('--result-id', required=True)
    args = ap.parse_args()
    scripts = args.script_dir.resolve()
    sys.path.insert(0, str(scripts))
    from p41_dag_level_transport47 import initialize, FullLevelTransport
    from p41_projective_jet_frames47 import ProjectiveJetFrames, ordinary_physical_jets
    from p41_native_r2_linear47 import install
    from p41_coprime_kernel_dag47 import velu_model
    from p41_supersingular_atlas47 import ca, cs, cm, ci, ck, cp, cn
    from p41_actual_differentials47 import save, digest

    started = time.monotonic()
    at = initialize(scripts)
    a, r, np = at.a, at.r, at.np
    install(r, args.work_dir / 'native')
    frames = ProjectiveJetFrames(a)
    level = FullLevelTransport(at)
    data = scripts / 'data'
    inputs = {}

    def load(name):
        p = data / name
        inputs[name] = sha(p)
        return read(p)

    atlas = load('p41_rational_SS_residue_atlas47_complete.json.gz')
    graph = load('p41_SS_Hecke_graph47.json.gz')
    coarse = load('p41_elliptic_coarse_atlas47_verified.json.gz')
    disk = args.disk_id
    chart = next(c for c in atlas['charts'] if disk in c['disk_ids'])
    row = chart['disk_ids'].index(disk)
    reference = chart['reference_key']
    assert reference in {'0', '36'}
    source_row = chart['original_input_rows_0based'][row]
    assert r.equal(r.from_json(chart['frame']), a.fc)
    W0 = r.rows(r.from_json(chart['W_coefficients_0to3'][0]), [row])
    members = {(m['reference_key'], m['necklace_label_1based']): v['vertex_0based']
               for v in graph['vertices'] for m in v['members']}
    source_vertex = members[(reference, source_row + 1)]
    source_pos = graph['source_input_labels_0based'][reference].index(source_row)
    physical, physical_certs = {}, {}

    def physical_coefficients(key, index):
        if key not in physical:
            obj = ordinary_physical_jets(at, int(key), order=3,
                                        coarse_path=data / 'p41_elliptic_coarse_atlas47_verified.json.gz')
            physical[key] = obj
            physical_certs[key] = {
                'coefficient_sha256': [digest(r.to_json(v)) for v in obj['W']],
                'clearing_patches': obj['clearing_patches'], 'degree': 3}
        obj = physical[key]
        assert index in obj['ordinary_indices_0based']
        return [r.rows(v, [index]) for v in obj['W']]

    def eval_matrix(coefficients, parameter):
        assert all(v % 47 == 0 for v in parameter)
        out = r.zeros(1, 73)
        for coefficient in reversed(coefficients):
            out = r.add(at.matrix_scale(out, parameter), coefficient)
        return out

    def scalar_value(value):
        assert value[0].shape == (1, 1)
        return int(value[0][0, 0]), int(value[1][0, 0])

    def poly_value(coefficients, parameter):
        out = (0, 0)
        for coefficient in reversed(coefficients):
            out = ca(cm(out, parameter), coefficient)
        return out

    source_coefficients = physical_coefficients(reference, source_row)
    coordinate = r.from_json(chart['coordinate'])
    desired = (chart['rational_coordinate_at_center_mod47four'][row], 0)
    f_coefficients = [scalar_value(r.mm(v, a.fc)) for v in source_coefficients]
    c_coefficients = [scalar_value(r.mm(v, coordinate)) for v in source_coefficients]
    equation = [cs(c, cm(desired, f)) for c, f in zip(c_coefficients, f_coefficients)]
    assert all(v % 47 == 0 for v in equation[0])
    derivative = [ck(v, n) for n, v in enumerate(equation) if n]
    assert sum(v * v for v in derivative[0]) % 47 != 0
    source_parameter = (0, 0)
    for _ in range(3):
        source_parameter = cs(source_parameter,
                              cm(poly_value(equation, source_parameter),
                                 ci(poly_value(derivative, source_parameter))))
    assert all(v % 47 == 0 for v in source_parameter)
    assert poly_value(equation, source_parameter) == (0, 0)
    source_raw = eval_matrix(source_coefficients, source_parameter)
    source_normalized = r.mul(source_raw, r.inverse_values(r.mm(source_raw, a.fc)))
    assert r.equal(source_normalized, W0), 'All 73 actual source coordinates must match the rational atlas center.'
    assert r.equal(r.mm(W0, coordinate), r.column([list(desired)]))
    ref = level.refs[reference]
    A = ca(tuple(ref['A']), source_parameter) if reference == '0' else tuple(ref['A'])
    B = tuple(ref['B']) if reference == '0' else ca(tuple(ref['B']), source_parameter)
    P0, Q0 = level.F.point(ref['P']), level.F.point(ref['Q'])
    assert level.F.on_curve(P0, level.F.embed(A), level.F.embed(B))
    assert level.F.on_curve(Q0, level.F.embed(A), level.F.embed(B))
    print('PASS actual rational source', disk, 'physical parameter', source_parameter, flush=True)

    def point_key(W, modulus=r.Q):
        values = r.mm(W, frames.candidates)
        j = next(j for j in range(146) if r.units(values)[0, j])
        values = r.mul(values, r.inverse_values(r.cols(values, [j])))
        return tuple(int(v) % modulus for part in values for v in part[0])

    targets, records, raw_regular_targets = [], [], []
    for branch in range(3):
        frozen = graph['constant_branches'][reference + '/2/' + str(branch)]
        assert tuple(frozen['source_A']) == tuple(ref['A'])
        assert tuple(frozen['source_B']) == tuple(ref['B'])
        assert frozen['source_reference_key'] == reference
        assert frozen['ell'] == frozen['degree'] == frozen['determinant_mod41'] == 2
        root = cn(tuple(frozen['kernel'][0]))
        for _ in range(3):
            error = ca(ca(cp(root, 3), cm(A, root)), B)
            root = cs(root, cm(error, ci(ca(ck(cp(root, 2), 3), A))))
        assert ca(ca(cp(root, 3), cm(A, root)), B) == (0, 0)
        assert tuple(v % 47 for v in root) == tuple((-v) % 47 for v in frozen['kernel'][0])
        kernel = [cn(root), (1, 0)]
        target_A, target_B = velu_model(2, kernel, A, B)
        node = {'ell': 2, 'source_A': A, 'source_B': B,
                'A': target_A, 'B': target_B, 'kernel': kernel}
        P1, Q1 = level.raw_pair(node, P0, Q0)
        actual = level.record(target_A, target_B, P1, Q1, 2, [source_row])
        assert actual['reference_key'] == frozen['reference_key']
        assert actual['raw_level_matrix_mod41'] == frozen['raw_level_matrix_mod41']
        assert actual['image_indices_1based'][0] == frozen['image_indices_1based'][source_pos]
        key = actual['reference_key']
        label = actual['image_indices_1based'][0]
        coarse_target = (key, label) not in members
        if coarse_target:
            co = actual['coarse']
            old_co = frozen['coarse']
            assert co['raw_level_matrix_mod41'] == old_co['raw_level_matrix_mod41']
            assert co['image_indices_1based'][0] == old_co['image_indices_1based'][source_pos]
            key, label = co['reference_key'], co['image_indices_1based'][0]
            cc = next(c for c in coarse['elliptic_charts'] if c['kind'] == key)
            ix = cc['indices_1based'].index(label)
            coeff = [r.rows(r.from_json(v), [ix]) for v in cc['coarse_values']]
            parameter = tuple(co['invariant_parameter'])
            Wraw = eval_matrix(coeff, parameter)
        else:
            parameter = tuple(actual['reference_parameter'])
            Wraw = eval_matrix(physical_coefficients(key, label - 1), parameter)
            Wraw = at.matrix_scale(Wraw, cp(tuple(actual['homothety']), 2))
            raw_regular_targets.append(Wraw)
        frame_value = r.mm(Wraw, a.fc)
        assert np.all(r.units(frame_value))
        W = r.mul(Wraw, r.inverse_values(frame_value))
        expected_vertex = frozen['target_vertices_0based'][source_pos]
        vertex = graph['vertices'][expected_vertex]
        assert point_key(W, 47) == tuple(vertex['projective_146_mod47_real'] + vertex['projective_146_mod47_imag'])
        assert r.equal(r.mm(W, a.fc), r.column([[1, 0]]))
        targets.append(W)
        actual.update(node)
        records.append({'branch_0based': branch, 'actual_saved_full_level_record': actual,
                        'frozen_reference_full_level_record': frozen,
                        'target_vertex_0based': expected_vertex,
                        'used_true_elliptic_coarse_chart': coarse_target,
                        'all146_projective_reduction_coordinates_match_graph': True,
                        'W_actual_values_in_R2': r.to_json(W)[0],
                        'target_reference_key': key, 'target_necklace_label_1based': label,
                        'actual_kernel_root_in_R2': list(root),
                        'actual_full_level_recomputed_and_same_residual_matrix': True})
        print('PASS shifted actual T2 target', disk, branch, key, label, expected_vertex, flush=True)

    keys = [point_key(W) for W in targets]
    assert len(set(keys)) == 3
    conjugated = [point_key(r.mm(r.conjugate(W), r.conjugate(a.M['A1']))) for W in targets]
    assert set(keys) == set(conjugated)
    assert point_key(W0, 47) not in [point_key(W, 47) for W in targets]
    checked_weight_two_sum = False
    if len(raw_regular_targets) == 3:
        hecke = load('p41_hecke47_full_saved.json.gz')['operators']['2']
        total = r.zeros(1, 73)
        for Wraw in raw_regular_targets:
            total = r.add(total, Wraw)
        assert r.equal(a.scale(total, pow(2, -1, r.Q)),
                       r.mm(source_raw, r.from_json(hecke['weight2_operator'])))
        checked_weight_two_sum = True
    numerator = ck(cp(A, 3), 4)
    j_value = ck(cm(numerator, ci(ca(numerator, ck(cp(B, 2), 27)))), 1728)
    assert j_value[1] == 0 and j_value[0] % 47 == int(reference)
    out = {
        'result': args.result_id, 'source_disk_id': disk, 'level': 41,
        'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
        'source_reference_key': reference, 'source_row_0based': source_row,
        'coarse_j_ramification_index_at_residue': 3 if reference == '0' else 2,
        'source_physical_parameter_name': 'A-A_reference' if reference == '0' else 'B-B_reference',
        'source_vertex_0based': source_vertex,
        'actual_source_W_fc_normalized': r.to_json(W0)[0],
        'actual_source_physical_parameter': source_parameter,
        'source_coordinate_equation_coefficients': equation,
        'source_physical_raw_W_mod47four': r.to_json(source_raw)[0],
        'actual_source_model': [A, B], 'actual_source_j_mod47four': j_value[0],
        'actual_T2_targets_fc_normalized': [r.to_json(W)[0] for W in targets],
        'actual_target_vertices_0based': [v['target_vertex_0based'] for v in records],
        'actual_target_Frobenius_permutation_0based': [keys.index(k) for k in conjugated],
        'all_three_true_targets_Frobenius_stable': True,
        'all_three_targets_separate_from_source': True,
        'source_all73_equals_original_rational_SS_center': True,
        'source_etale_physical_parameter_recovered_and_verified': True,
        'source_raw_reference_center_identical': source_parameter == (0, 0),
        'physical_jet_certificates': physical_certs,
        'actual_branches': records, 'branch_records': records,
        'complete_actual_T2_support': True,
        'actual_full73_weight2_Hecke_sum_verified_when_all_targets_regular': checked_weight_two_sum,
        'kernel_polynomial_ascending': [list(B), list(A), [0, 0], [1, 0]],
        'kernel_polynomial_coefficient_ring': 'R2=Z/47^4[i], i^2=-1',
        'actual1681_reference_point_tables': {k: v['certificate'] for k, v in level.lookup_tables.items()},
        'input_sha256': dict(a.inputs, **inputs), 'source_sha256': sha(__file__),
        'runtime_seconds': round(time.monotonic() - started, 3)}
    print('PASS actual shifted SS T2 support', save(args.output, out), flush=True)


if __name__ == '__main__':
    main()
