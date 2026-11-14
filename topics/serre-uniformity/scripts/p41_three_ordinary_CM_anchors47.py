#!/usr/bin/env python3
"""Three genuine ordinary CM anchors, using the signed R94 path coefficients.

The modular-symbol identities are checked over Q before reducing modulo
47^4.  Actual physical CM points and local tiny integrals fix the constants
of the ORD_j38, ORD_j39, and ORD_j40 Abel coordinate charts.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

P = 47
Q = P**4
Q3 = P**3
CM_J = {-11: -32768, -19: -884736, -67: -147197952000}
CM_SOURCES = {
    -11: 'https://www.lmfdb.org/EllipticCurve/Q/121/b/1',
    -19: 'https://www.lmfdb.org/EllipticCurve/Q/361/a/1',
    -67: 'https://www.lmfdb.org/EllipticCurve/Q/4489.b2/',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    Path(path).write_bytes(gzip.compress(raw, mtime=0) if str(path).endswith('.gz') else raw)


def pair(x):
    return [int(x.numerator), int(x.denominator)]


def pivot_columns(A, prime):
    """Unit columns of the actual row space, with independent row witnesses."""
    rows = [[int(x) % prime for x in row] for row in A]
    permutation = list(range(len(rows)))
    cols, original_rows = [], []
    k = 0
    for c in range(len(rows[0])):
        choices = [i for i in range(k, len(rows)) if rows[i][c]]
        if not choices:
            continue
        i = choices[0]
        rows[k], rows[i] = rows[i], rows[k]
        permutation[k], permutation[i] = permutation[i], permutation[k]
        inv = pow(rows[k][c], -1, prime)
        rows[k] = [x*inv % prime for x in rows[k]]
        for i in range(k+1, len(rows)):
            scalar = rows[i][c]
            if scalar:
                rows[i] = [(x-scalar*y) % prime for x, y in zip(rows[i], rows[k])]
        cols.append(c)
        original_rows.append(permutation[k])
        k += 1
        if k == len(rows):
            break
    return original_rows, cols


def class_coordinates(script_dir):
    from flint import fmpq, fmpq_mat, fmpq_poly
    from p41_full_chow_heegner import contract_paths, contracted_coefficient, hurwitz_degree, legendre
    full_path = script_dir/'data/p41_full_chow_heegner_certificate.json.gz'
    jacobi_path = script_dir/'data/p41_jacobi_cm_certificate.json'
    inert_path = script_dir/'data/p41_inert_cm_certificate.json'
    full, jacobi, inert = [read(path) for path in (full_path, jacobi_path, inert_path)]
    assert full['jacobi_reference_sha256'] == sha(jacobi_path)
    assert full['inert_reference_sha256'] == sha(inert_path)
    edges, path_rows = contract_paths(jacobi['path_matrices'])
    raw = full['raw_translation_rows']
    source_rows, source_cols = pivot_columns(raw, P)
    assert len(source_rows) == len(source_cols) == 73
    basis = fmpq_mat([[raw[i][c] for c in source_cols] for i in source_rows]).transpose()
    records = []
    for D, j in CM_J.items():
        assert legendre(D) == -1 and hurwitz_degree(D) == 1
        coeffs, forms = contracted_coefficient(D, edges, path_rows)
        if D == -11:
            assert [2*x for x in coeffs] == [x-2*y for x, y in zip(raw[5], raw[1])]
        if D == -19:
            previous = records[0]['raw_contracted_coefficient']
            assert [2*x for x in coeffs] == [x-2*y for x, y in zip(raw[8], previous)]
        rhs = fmpq_mat([[coeffs[c]] for c in source_cols])
        relation = basis.solve(rhs, algorithm='dixon')
        values = [Fraction(int(relation[i, 0].numerator), int(relation[i, 0].denominator))
                  for i in range(len(source_rows))]
        for k in range(len(coeffs)):
            assert sum(v*raw[i][k] for i, v in zip(source_rows, values)) == coeffs[k], (D, k)
        assert all(v.denominator % P for v in values)
        output_fields = []
        for f, jf, inf in zip(full['fields'], jacobi['fields'], inert['fields']):
            assert f['factor_descending'] == jf['factor_descending'] == inf['factor_descending']
            modulus = fmpq_poly(f['factor_descending'][::-1])
            kappa = fmpq_poly([fmpq(c, inf['kappa_denominator']) for c in inf['kappa_numerator_descending'][::-1]])
            gcd, kinverse, other = kappa.xgcd(modulus)
            assert gcd == fmpq_poly([1]) and (kappa*kinverse) % modulus == fmpq_poly([1])
            ratio = fmpq_poly([])
            for row_index, v in zip(source_rows, values):
                den, descending = f['raw_ratios'][row_index]
                poly = fmpq_poly([fmpq(x, den) for x in descending[::-1]])
                ratio += poly*fmpq(v.numerator, v.denominator)
            ratio %= modulus
            coordinate = (10*kinverse*ratio) % modulus
            d = len(f['factor_descending'])-1
            rational = [pair(coordinate[k]) for k in range(d)]
            assert all(den % P for num, den in rational)
            output_fields.append({
                'factor_descending': f['factor_descending'],
                'raw_signed_Jacobi_ratio_ascending': [pair(ratio[k]) for k in range(d)],
                'r_U_ascending_rational': rational,
                'r_U_ascending_mod47four': [num*pow(den, -1, Q) % Q for num, den in rational],
            })
        if D == -11:
            assert output_fields[0]['r_U_ascending_rational'] == [[-25, 8], [-5, 8]]
        records.append({
            'discriminant': D, 'j_integer': j, 'j_mod47': j % P,
            'j_source': CM_SOURCES[D], 'weighted_CM_degree': 1,
            'inert_at41': True, 'class_formula': 'U_D=20*P_D-D_cusp=(10/kappa)*(c(D*1681,r_D)/c(-4,756))*B_minus4',
            'indefinite_form_count': forms, 'raw_contracted_coefficient': coeffs,
            'path_relation_on_source_rows_rational': [pair(v) for v in values],
            'all289_path_entries_equal_over_Q': True, 'fields': output_fields,
            'r_U_mod47four': [x for ff in output_fields for x in ff['r_U_ascending_mod47four']],
        })
        print('Exact signed CM class', D, 'all289 path coordinates verified', flush=True)
    return {
        'complete_three_signed_CM_classes': True,
        'unit_minor_source_row_indices_0based': source_rows,
        'unit_minor_source_column_indices_0based': source_cols,
        'raw_translation_rank_mod47': len(source_rows), 'records': records,
        'input_sha256': {p.name: sha(p) for p in (full_path, jacobi_path, inert_path)},
    }


def physical_jets(at, raw0, A, B, order=3):
    """Actual GM transport for one arbitrary ordinary reference point."""
    from p41_elliptic_coarse_atlas47 import Series, ClassicalInvariants
    from p41_scalar_primitive_atlas47 import scalar_gm
    from p41_supersingular_atlas47 import ck
    a, r = at.a, at.r
    inv = ClassicalInvariants(at)
    aa, bb = scalar_gm((A, 0), (B, 0), False, order)
    assert (bb[0][0]**2+bb[0][1]**2) % P
    rng = random.Random(2370041+A*47+B)
    for attempt in range(30):
        if attempt == 0:
            v, G = at.v, at.G
        else:
            seed = r.column([[rng.randrange(P), rng.randrange(P)] for _ in range(52)])
            vv = r.mm(at.K, seed)
            v = r.add(vv, r.mm(a.M['A1'], r.conjugate(vv)))
            values = r.mul(r.mm(a.M['W'], v), at.delta)
            G = r.rows(values, a.M['P3'])
            assert r.equal(r.mm(a.M['V3'], G), values)
        if r.units(r.mm(raw0, v))[0, 0]:
            break
    else:
        raise AssertionError('No unit clearing section at ordinary point')
    W = [raw0]
    for n in range(order):
        V3 = inv.section_series(W)[1]
        vv = [r.mm(w, v) for w in W]
        iv = Series(a, n+1).inverse(vv)
        GG = [r.mm(v3, G) for v3 in V3]
        rhs = r.zeros(1, 73)
        for k in range(n+1):
            for h in range(n-k+1):
                rhs = r.add(rhs, at.matrix_scale(r.mul(GG[k], iv[h]), bb[n-k-h]))
            rhs = r.sub(rhs, at.matrix_scale(W[n-k], ck(aa[k], 2)))
        W.append(a.scale(rhs, pow(n+1, -1, Q)))
    # Independent homogeneous modular invariants certify the physical scale,
    # including the corrected 20/k ordinary field trace normalization.
    data = inv.series(W)
    vcube = Series(a, order+1).power(data['v'], 3)
    for n in range(order+1):
        assert r.equal(data['Av'][n], a.scale(data['v'][n], A))
        rhs = a.scale(vcube[n], B)
        if n:
            rhs = r.add(rhs, vcube[n-1])
        assert r.equal(data['Bv3'][n], rhs)
    return W, {'clearing_attempt_0based': attempt,
               'Av_equals_Av_all_coefficients': True,
               'Bv3_equals_BplusT_times_v3_all_coefficients': True,
               'physical_parameter': 't=B-B_reference with A fixed'}


def global_series(poly, aa):
    """Based global polynomial along a=a0+a1*y+a2*y^2+a3*y^3."""
    result = [0]*7
    based = poly['based_C']
    for k in range(4):
        result[k] = sum(x*y for x, y in zip(based['linear_vector_mod47four'], aa[k])) % Q
    result[0] += based['constant_mod47four']
    offset = 0
    for block in based['quadratic_blocks_mod47four']:
        d = len(block)
        for k in range(4):
            for ell in range(4):
                result[k+ell] += sum(aa[k][offset+i]*block[i][j]*aa[ell][offset+j]
                                     for i in range(d) for j in range(d))
        offset += d
    assert offset == 54
    result = [x % Q for x in result]
    assert result[5:] == [0, 0]
    return result[:5]


def anchors_and_polynomials(args, classes):
    from p41_elliptic_coarse_atlas47 import setup
    from p41_projective_jet_frames47 import ProjectiveJetFrames
    from p41_global_qc_polynomials47 import eval_blocks
    at = setup(args.script_dir.resolve())
    a, r, np = at.a, at.r, at.np
    frames = ProjectiveJetFrames(a)
    ordinary = read(args.ordinary_atlas)
    physical = read(args.ordinary_values)
    tiny = read(args.tiny)
    polys = read(args.global_polynomials)
    SS = read(args.SS_constants)
    assert ordinary['all19_actual_references_and_projective_jets_complete']
    assert physical['complete_all19_ordinary_reference_values']
    assert tiny['complete_all129_tiny_Abel_integrals']
    assert polys['complete_global_polynomials']
    assert SS['all110_rational_SS_center_constants_complete']
    assert SS['both_actual_Hecke_equations_verified'] and not SS['CM_anchors_used_to_solve']
    r3 = [x % Q3 for f in polys['fields'] for x in f['r_minus3']]
    tiny_disk = {}
    for chart in tiny['charts']:
        for i, disk_id in enumerate(chart['disk_ids']):
            tiny_disk[disk_id] = (chart, i)
    anchors = []
    for record in classes['records']:
        D, j = record['discriminant'], record['j_integer']
        point = next(p for p in physical['points'] if p['j_mod47'] == j % P)
        disk = next(d for d in ordinary['ordinary_disk_records'] if d['j_mod47'] == j % P)
        chart = ordinary['charts'][disk['chart_0based']]
        ri = disk['chart_row_0based']
        A, B = point['curve_A'], point['curve_B']
        assert [A, B] == disk['actual_elliptic_model']
        raw0 = r.from_json([point['W_mod47four']])
        frame, coordinate = r.from_json(chart['frame']), r.from_json(chart['coordinate'])
        normalized0 = r.mul(raw0, r.inverse_values(r.mm(raw0, frame)))
        chart_W = [r.rows(r.from_json(w), [ri]) for w in chart['W_coefficients_0to3']]
        assert r.equal(normalized0, chart_W[0]), 'The chosen ordinary reference is the actual Q47 center'
        Bsquare = 4*A**3*(1728-j)*pow(27*j, -1, Q) % Q
        BCM = B
        for _ in range(2):
            BCM = (BCM-(BCM**2-Bsquare)*pow(2*BCM, -1, Q)) % Q
        assert BCM**2 % Q == Bsquare and (BCM-B) % P == 0
        assert 1728*4*A**3*pow(4*A**3+27*BCM**2, -1, Q) % Q == j % Q
        t = (BCM-B) % Q
        W, transport_checks = physical_jets(at, raw0, A, B, order=3)
        WCM = r.zeros(1, 73)
        for k, wk in enumerate(W):
            WCM = r.add(WCM, a.scale(wk, pow(t, k, Q)))
        WCM = r.mul(WCM, r.inverse_values(r.mm(WCM, frame)))
        w = r.mm(WCM, coordinate)
        center = chart['rational_coordinate_at_center_mod47four'][ri]
        assert int(w[1][0, 0]) == 0
        z = (int(w[0][0, 0])-center) % Q
        assert z % P == 0
        y = z//P
        recovered = r.zeros(1, 73)
        for k, wk in enumerate(chart_W):
            recovered = r.add(recovered, a.scale(wk, pow(z, k, Q)))
        assert r.equal(recovered, WCM), 'All73 physical CM coordinates agree with independent projective jets'
        tch, ti = tiny_disk[disk['disk_id']]
        assert tch['origin'] == 'R231_ordinary' and tch['origin_chart_0based'] == disk['chart_0based']
        tiny_coeffs = [row[ti] for row in tch['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed']]
        delta = [sum(tiny_coeffs[k-1][q]*pow(y, k, Q3) for k in range(1, 4)) % Q3 for q in range(54)]
        point_a = [(x-b)*pow(20, -1, Q3) % Q3 for x, b in zip(record['r_U_mod47four'], r3)]
        center_a = [(x-d) % Q3 for x, d in zip(point_a, delta)]
        component = j % 41
        assert component in polys['component_order']
        aa = [center_a]+tiny_coeffs
        series = [{'n': poly['n'], 'coefficients_0to4_in_y_mod47four': global_series(poly, aa)}
                  for poly in polys['directions']]
        local_values = []
        for poly, ff in zip(polys['directions'], series):
            value = sum(c*pow(y, k, Q) for k, c in enumerate(ff['coefficients_0to4_in_y_mod47four'])) % Q
            assert value == eval_blocks(poly, point_a, 'based_C')
            target = poly['QC_defect_targets_by_component_order'][polys['component_order'].index(component)]
            local_values.append((value-target) % Q)
        anchors.append({
            'discriminant': D, 'j_integer': j, 'disk_id': disk['disk_id'],
            'chart_0based': disk['chart_0based'], 'chart_row_0based': ri,
            'actual_elliptic_model_mod47four': [A, BCM],
            'physical_parameter_t_mod47four': t,
            'physical_CM_W_in_chart_frame_mod47four': r.to_json(WCM),
            'physical_chart_parameter_z_of_CM_point_mod47four': z,
            'rescaled_parameter_y_of_CM_point_mod47cubed': y,
            'actual_CM_U_cyclic_coordinates_mod47cubed': [v % Q3 for v in record['r_U_mod47four']],
            'actual_CM_C_cyclic_coordinates_mod47cubed': point_a,
            'tiny_C_center_to_CM_mod47cubed': delta,
            'actual_center_C_cyclic_coordinates_mod47cubed': center_a,
            'bad_component_at41': component,
            'global_polynomials_at_rational_center': series,
            'local_global_section_heights_at_CM_point_by_global_reciprocity': local_values,
            'local_values_method': 'Global R222 heights and the rational CM point; not an independent local Miller evaluation',
            'all73_physical_CM_coordinates_match_projective_chart': True,
            'physical_transport_checks': transport_checks,
        })
        print('Actual ordinary CM anchor', D, disk['disk_id'], 'all73 physical coordinates and all53 global values verified', flush=True)
    known = {record['disk_id']: record['actual_center_C_cyclic_coordinates_mod47cubed'] for record in anchors}
    for record in SS['rational_SS_center_constants']:
        disk_id = record['disk_id']
        assert disk_id not in known
        known[disk_id] = [(u-b)*pow(20, -1, Q3) % Q3 for u, b in zip(record['U_cyclic_coordinates_mod47cubed'], r3)]
    assert len(known) == 113
    disk_series = []
    for disk_id, center_a in known.items():
        ch, ri = tiny_disk[disk_id]
        coeffs = [cc[ri] for cc in ch['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed']]
        aa = [center_a]+coeffs
        series = [{'n': poly['n'], 'coefficients_0to4_in_y_mod47four': global_series(poly, aa)}
                  for poly in polys['directions']]
        disk_series.append({'disk_id': disk_id, 'actual_center_C_cyclic_coordinates_mod47cubed': center_a,
                            'cyclic_C_coefficients_0to3_in_y_mod47cubed': aa,
                            'global_polynomials': series})
    # Recompute the three independently anchored R230 disks from the solved SS constants.
    by_id = {r['disk_id']: r for r in disk_series}
    for old in tiny['known_CM_anchored_disks']:
        got = by_id[old['disk_id']]
        assert got['actual_center_C_cyclic_coordinates_mod47cubed'] == old['actual_center_cyclic_coordinates_mod47cubed']
        assert got['global_polynomials'] == old['global_polynomials_at_rational_center']
    missing = sorted(set(tiny_disk)-set(known))
    assert len(missing) == 16 and all(x.startswith('ORD_') for x in missing)
    modules = ['p41_elliptic_coarse_atlas47', 'p41_scalar_primitive_atlas47',
               'p41_projective_jet_frames47', 'p41_global_qc_polynomials47']
    inputs = dict(a.inputs, **classes['input_sha256'])
    for path in [args.ordinary_values, args.ordinary_atlas, args.tiny, args.global_polynomials, args.SS_constants]:
        inputs[path.name] = sha(path)
    return {
        'level': 41, 'auxiliary_prime': P, 'modulus': Q, 'precision': 4,
        'cyclic_coordinate_modulus': Q3,
        'complete_three_ordinary_CM_anchors': True,
        'complete_113_actual_global_QC_polynomials': True,
        'complete_all129_Abel_constants': False,
        'complete_local_QC_functions': False, 'complete_common_roots': False,
        'three_ordinary_CM_anchors': anchors,
        'actual_113_rational_disk_global_polynomials': disk_series,
        'remaining16_ordinary_center_constant_disk_ids': missing,
        'old_three_R230_CM_anchor_series_match': True,
        'ordinary_parameter': 'y=z/47, z=W*c/(W*v)-rational_center_coordinate',
        'global_polynomial_degree': 4,
        'tail_bound': 'Integral omega gives omitted a terms in47^3; every global coefficient is in47, so modulo47^4 these vanish. Quadratic terms of degree5 and6 are checked zero.',
        'input_sha256': inputs,
        'module_sha256': {name: sha(sys.modules[name].__file__) for name in modules},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--dependencies', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--ordinary-values', type=Path)
    ap.add_argument('--ordinary-atlas', type=Path)
    ap.add_argument('--tiny', type=Path)
    ap.add_argument('--global-polynomials', type=Path)
    ap.add_argument('--SS-constants', type=Path)
    args = ap.parse_args()
    sys.path.insert(0, str(args.dependencies.resolve()))
    sys.path.insert(0, str(args.script_dir.resolve()))
    out = class_coordinates(args.script_dir.resolve())
    if args.ordinary_values is not None:
        for name in ['ordinary_atlas', 'tiny', 'global_polynomials', 'SS_constants']:
            assert getattr(args, name) is not None, name
        detailed = anchors_and_polynomials(args, out)
        out = dict(detailed, signed_CM_class_calculation=out)
    else:
        out['complete_three_ordinary_CM_anchors'] = False
    out['source_sha256'] = sha(__file__)
    save(args.output, out)
    print('Output SHA', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
