#!/usr/bin/env python3
"""Original holomorphic semilinear action; exact arithmetic only in public Actions."""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback
import flint
from flint import fmpq, fmpq_mat

RESULT = 'R866-original-holomorphic-semilinear-descent'
FINAL = 'p41-original-holomorphic-semilinear-descent-certificate.json'
PREFIX = 'R866-'
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
PROOF_KEYS = ('R802', 'R853', 'R853_method', 'R860', 'R864')
SOURCE_DEFINITIONS = {
    'R786': {'result': 'R786-exact-original-power5-short-basis',
             'core_sha256': '4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851', 'count': 152},
    'R837': {'result': 'R837-original-fixed-branch-pencil',
             'core_sha256': '5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924', 'count': 8},
    'R853': {'result': 'R853-original-semilinear-V1-generator-conjugates',
             'core_sha256': '5b65e7ccf7c6663949155fdd30abc4c765823e861259c8f9b90b26d0bc1511df', 'count': 9},
    'R864': {'result': 'R864-original-canonical-cusp-kernel',
             'core_sha256': '0dfe5d3fde2adfe90c3384266d5d8083ed46221c1b7b96e04030b0c5c2d26ea9', 'count': 9},
}
STRATEGY = {
    'scope': 'original_holomorphic_semilinear_action_and_complete_Q_fixed_basis',
    'original_V1_dimension': 146, 'holomorphic_dimension': 127,
    'qY_orders': 14, 'xi_coordinates_per_order': 40, 'full_original_coordinate_rows': 560,
    'original_section_integer_scale': '6724', 'differential_coefficient_multiplier_from_H': '82',
    'H_coefficients_of': 'original_F_j_without_rescaling',
    'source_e_i_already_integer_scaled_relative_to_T': '6724',
    'original_row_convention': '40*n+r', 'coefficient_c0_action': 's_to_minus_s_xi_fixed',
    'geometric_twist_action': 'qY_to_minus_qY_weight2_automorphy_one',
    'new_row_selection_within_old_R837_146_rows': True,
    'exact_inverse_dimension': 127, 'semilinear_matrix_convention': 'C_times_conjugate_coefficient_column',
    'Q_fixed_column_rule': 'inverse_column_if_even_order_else_inverse_column_over_original_s',
    'original_s_square': -3, 'matrix_column_block_size': 8,
    'original_V1_e73_conversion_already_applied_by_R864': True,
    'normal_transport_e73_correction': 'subtract_original_V1_coefficient1_once',
    'full146_or272_conjugation_matrix_computed': False,
    'only_transport_resume_budget_directories_excluded_from_mathematical_identity': True,
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(4*1024*1024), b''):
            h.update(b)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, 'rt') if path.suffix == '.gz' else path.open()) as f:
        return json.load(f)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def save(path, value):
    path = Path(path)
    tmp = path.with_name(path.name + '.tmp')
    data = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if path.suffix == '.gz':
        with tmp.open('wb') as f:
            with gzip.GzipFile(filename='', mode='wb', fileobj=f, mtime=0) as g:
                g.write(data)
    else:
        tmp.write_bytes(data)
    tmp.replace(path)


def plain(value):
    r = {k: value[k] for k in ('file', 'bytes', 'sha256')}
    assert Path(r['file']).name == r['file'] and '\\' not in r['file']
    return r


def spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(folder, value):
    value = plain(value)
    path = Path(folder) / value['file']
    assert spec(path) == value, path.name
    return path


def identity(value):
    return {key: value[key] for key in BASE}


def source_identity(value):
    return {**identity(value), 'certificate': plain(value['certificate']),
            'configuration_sha256': value['configuration_sha256'],
            'selected_file_count': len(value['files']), 'selected_files_sha256': fingerprint(value['files'])}


def expected_tag(item):
    return {'result': RESULT, 'source_sha256': item['core_sha256'], 'p': 41, 'python_flint': '0.9.0',
            'proofs_sha256': {key: item['proofs'][key]['sha256'] for key in PROOF_KEYS},
            'method_sha256': item['method_sha256'],
            'sources': {key: source_identity(item['sources'][key]) for key in sorted(SOURCE_DEFINITIONS)},
            'strategy': STRATEGY}


def qdecode(value):
    assert isinstance(value, list) and len(value) == 2
    n, d = map(int, value)
    assert d > 0
    q = fmpq(n, d)
    assert int(q.numerator) == n and int(q.denominator) == d
    return q


def qencode(value):
    return [str(value.numerator), str(value.denominator)]


def matrix_decode(value):
    return fmpq_mat([[qdecode(x) for x in row] for row in value])


def matrix_encode(value):
    return [[qencode(value[i, j]) for j in range(value.ncols())] for i in range(value.nrows())]


def eye(n):
    return fmpq_mat([[int(i == j) for j in range(n)] for i in range(n)])


def cols(m, first, stop):
    return fmpq_mat([[m[i, j] for j in range(first, stop)] for i in range(m.nrows())])


class BudgetStop(Exception):
    pass


class Job:
    def __init__(self, item, out, minutes):
        self.item, self.out = item, Path(out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.start = time.monotonic()
        self.deadline = self.start + minutes * 60
        assert str(flint.__version__) == '0.9.0'
        assert item['result'] == RESULT and item['p'] == 41
        assert item['producer_inputs_pending'] is False
        assert item['core_sha256'] == sha(__file__)
        assert set(item['proofs']) == set(PROOF_KEYS)
        for value in item['proofs'].values():
            assert sha(value['path']) == value['sha256']
        assert sha(item['method']) == item['method_sha256']
        assert set(item['sources']) == set(SOURCE_DEFINITIONS)
        self.tag = expected_tag(item)
        self.cert = {}
        for label, source in item['sources'].items():
            d = SOURCE_DEFINITIONS[label]
            assert source['result'] == d['result'] and source['core_sha256'] == d['core_sha256']
            assert len(source['files']) == d['count']
            for name, value in source['files'].items():
                assert name == value['file']
                bound(source['directory'], value)
            cert = read(bound(source['directory'], source['certificate']))
            assert cert['result'] == source['result'] and cert['complete'] is True
            assert cert['configuration']['source_sha256'] == source['core_sha256']
            assert fingerprint(cert['configuration']) == source['configuration_sha256']
            self.cert[label] = cert
        self.B, self.H, self.Qinv, self.C = None, None, None, None

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop('budget reached at completed-stage boundary')

    def source_stage(self, label, reference):
        source = self.item['sources'][label]
        reference = plain(reference)
        assert source['files'][reference['file']] == reference
        value = read(bound(source['directory'], reference))
        assert value['complete'] is True and value['configuration'] == self.cert[label]['configuration']
        return value

    def load(self, name):
        path = self.out / (PREFIX + name + '.json.gz')
        if not path.exists():
            return None
        value = read(path)
        assert value['result'] == RESULT and value['complete'] is True and value['configuration'] == self.tag
        return value

    def put(self, name, value):
        assert self.load(name) is None
        path = self.out / (PREFIX + name + '.json.gz')
        save(path, {'result': RESULT, 'configuration': self.tag, 'complete': True, **value})
        print('R866_STAGE=' + name, flush=True)
        return spec(path)

    def ref(self, name):
        assert self.load(name) is not None
        return spec(self.out / (PREFIX + name + '.json.gz'))

    def inputs(self):
        c853, c864 = self.cert['R853'], self.cert['R864']
        for label in ('R786', 'R837'):
            old = c853['configuration']['sources'][label]
            assert identity(old) == identity(self.item['sources'][label])
            assert old['certificate'] == self.item['sources'][label]['certificate']
        assert c853['original_three_V1_conjugates_certified'] is True
        assert c853['full_original_coordinate_rows'] == 560
        assert c853['configuration']['original_V1_integer_scale'] == '6724'
        assert c853['configuration']['original_tau_index'] == 0
        assert c853['configuration']['actual_sigma_integer_n'] == 1
        assert c853['configuration']['actual_w0_index'] == 2
        assert c864['complete_original_K_holomorphic_basis_certified'] is True
        assert c864['all20_cusps_and_both_original_charts_verified'] is True
        assert c864['actual_cusp_evaluation_rank'] == 19 and c864['actual_kernel_dimension'] == 127
        a853 = self.source_stage('R853', c853['source_audit'])
        a864 = self.source_stage('R864', c864['source_audit'])
        assert a853['original_normal_free_basis'] == a864['original_free_basis']
        minor = self.source_stage('R837', a853['original_reflection_minor'])
        attempt = self.source_stage('R837', a853['original_reflection_successful_attempt'])
        assert minor['successful_attempt'] == a853['original_reflection_successful_attempt']
        for key in ('matrix_shape', 'actual_modular_rank', 'selected_rows', 'selected_columns',
                    'prime', 'prime_index', 'minor_determinant_mod_prime'):
            assert minor[key] == attempt[key]
        assert minor['matrix_shape'] == [560, 146] and minor['actual_modular_rank'] == 146
        assert minor['selected_columns'] == list(range(146)) and minor['minor_determinant_mod_prime'] != 0
        self.old_rows = minor['selected_rows']
        assert len(self.old_rows) == len(set(self.old_rows)) == 146
        assert all(0 <= r < 560 for r in self.old_rows)
        assert a853['selected_original_prefix_rows'] == self.old_rows
        basis = self.source_stage('R864', c864['holomorphic_differential_basis'])
        kernel = self.source_stage('R864', c864['kernel_certificate'])
        assert basis['source_kernel'] == c864['kernel_certificate']
        assert basis['source_free_basis'] == a864['original_free_basis']
        assert basis['complete_original_K_holomorphic_basis_certified'] is True
        assert basis['all_original_V1_coordinate_roundtrips_verified'] is True
        assert basis['actual_dimension_over_K'] == 127 and len(basis['basis']) == 127
        assert kernel['all_free_rows_identity_verified'] is True and kernel['kernel_dimension'] == 127
        for j, value in enumerate(basis['basis']):
            assert value['basis_index'] == j and len(value['original_V1_coefficients']) == 146
        self.B = fmpq_mat([[qdecode(basis['basis'][j]['original_V1_coefficients'][i])
                           for j in range(127)] for i in range(146)])
        self.original_rows = []
        prefix_specs = []
        for i in range(146):
            name = 'R786-exact-power-1-row-%04d.json.gz' % i
            reference = self.item['sources']['R786']['files'][name]
            value = self.source_stage('R786', reference)
            assert value['weight'] == 2 and value['bound_qY'] == 128
            assert value['integer_scale'] == '6724' and value['original_R775_finite_coefficients_verified'] is True
            assert value['recipe']['kind'] == 'det_semilinear_E1_pair_trace'
            assert value['recipe']['exact_global_field'] == 'K'
            coefficients = value['integer_qY_xi_coefficients']
            assert len(coefficients) == 129 and all(len(x) == 40 for x in coefficients)
            self.original_rows.append(coefficients[:14])
            prefix_specs.append(plain(reference))
        assert prefix_specs == a853['original_R786_prefix_rows']
        self.prefix_specs = prefix_specs
        if self.load('source-audit') is None:
            self.put('source-audit', {'source_identities': self.tag['sources'],
                'source_original_holomorphic_basis': c864['holomorphic_differential_basis'],
                'source_original_cusp_kernel': c864['kernel_certificate'],
                'source_original_reflection_minor': a853['original_reflection_minor'],
                'source_original_146_V1_prefixes': prefix_specs,
                'old_selected_rows': self.old_rows, 'all_original_scales_preserved': True,
                'e73_original_V1_conversion_reapplied': False,
                'coefficient_c0_fixes_all_integer_xi_coordinates': True,
                'old_Fourier_rank_three_conjugates_or_cusp_kernel_recomputed': False})

    def Fourier_matrix(self):
        if self.load('original-holomorphic-Fourier-matrix') is None:
            blocks = []
            for n in range(14):
                name = 'holomorphic-Fourier-order-%02d' % n
                if self.load(name) is None:
                    self.budget()
                    a = fmpq_mat([[int(self.original_rows[i][n][r]) for i in range(146)] for r in range(40)])
                    product = a * self.B
                    if n == 0:
                        assert product == fmpq_mat(40, 127)
                    self.put(name, {'source_audit': self.ref('source-audit'), 'qY_order': n,
                        'matrix_shape': [40, 127], 'matrix_rational_num_den': matrix_encode(product),
                        'original_section_integer_scale': '6724', 'rational_coefficients_c0_fixed': True})
                blocks.append(self.ref(name))
            rows = []
            for reference in blocks:
                rows += read(bound(self.out, reference))['matrix_rational_num_den']
            assert len(rows) == 560
            self.put('original-holomorphic-Fourier-matrix', {'source_audit': self.ref('source-audit'),
                'source_original_holomorphic_basis': self.cert['R864']['holomorphic_differential_basis'],
                'source_original_prefixes': self.prefix_specs, 'order_blocks': blocks,
                'matrix_shape': [560, 127], 'matrix_rational_num_den': rows,
                'matrix_integer_scale': '6724', 'differential_coefficients_equal_matrix_times_82': True,
                'new_scale_relative_to_original_e_i_coefficients': [1, 1],
                'row_convention': '40*n+r', 'qY_order_range_inclusive': [0, 13],
                'all40_constant_coefficients_exactly_zero': True})
        self.H = matrix_decode(self.load('original-holomorphic-Fourier-matrix')['matrix_rational_num_den'])

    def inverse(self):
        if self.load('holomorphic-row-selection') is None:
            self.budget()
            rectangular = fmpq_mat([[self.H[i, j] for i in self.old_rows] for j in range(127)])
            reduced, rank = rectangular.rref()
            assert rank == 127
            positions = []
            for i in range(127):
                pivot = next(j for j in range(146) if reduced[i, j])
                assert reduced[i, pivot] == 1
                positions.append(pivot)
            assert positions == sorted(set(positions))
            selected = [self.old_rows[i] for i in positions]
            assert len(selected) == 127 and all(i >= 40 for i in selected)
            self.put('holomorphic-row-selection', {'source_H': self.ref('original-holomorphic-Fourier-matrix'),
                'source_old_reflection_minor': self.load('source-audit')['source_original_reflection_minor'],
                'original_146_selected_rows': self.old_rows, 'selected_positions_within_old_rows': positions,
                'selected_rows': selected, 'actual_exact_rank': rank, 'old_reflection_rank_recomputed': False})
        selection = self.load('holomorphic-row-selection')
        self.selected = selection['selected_rows']
        self.signs = [1 if (i // 40) % 2 == 0 else -1 for i in self.selected]
        self.Q = fmpq_mat([[self.H[i, j] for j in range(127)] for i in self.selected])
        if self.load('holomorphic-selected-exact-inverse') is None:
            self.budget()
            inverse = self.Q.inv()
            unit = eye(127)
            assert self.Q * inverse == unit and inverse * self.Q == unit
            det = self.Q.det()
            assert det
            self.put('holomorphic-selected-exact-inverse', {'source_H': self.ref('original-holomorphic-Fourier-matrix'),
                'source_row_selection': self.ref('holomorphic-row-selection'),
                'source_original_holomorphic_basis': self.cert['R864']['holomorphic_differential_basis'],
                'selected_rows': self.selected, 'matrix_shape': [127, 127],
                'selected_minor_matrix': matrix_encode(self.Q), 'inverse': matrix_encode(inverse),
                'actual_exact_minor_determinant': qencode(det), 'both_exact_inverse_products_verified': True,
                'section_integer_scale': '6724', 'full_original_row_numbers_not_compressed': True})
        self.Qinv = matrix_decode(self.load('holomorphic-selected-exact-inverse')['inverse'])

    def semilinear_action(self):
        if self.load('holomorphic-semilinear-action') is None:
            blocks = []
            for first in range(0, 127, 8):
                stop = min(127, first + 8)
                name = 'semilinear-columns-%03d-%03d' % (first, stop)
                if self.load(name) is None:
                    self.budget()
                    right = fmpq_mat([[self.signs[i] * self.Q[i, j] for j in range(first, stop)] for i in range(127)])
                    block = self.Qinv * right
                    recovered = self.H * block
                    target = fmpq_mat([[(1 if (i // 40) % 2 == 0 else -1) * self.H[i, j]
                                        for j in range(first, stop)] for i in range(560)])
                    assert recovered == target
                    self.put(name, {'source_H': self.ref('original-holomorphic-Fourier-matrix'),
                        'source_inverse': self.ref('holomorphic-selected-exact-inverse'),
                        'first_column': first, 'stop_column': stop, 'matrix': matrix_encode(block),
                        'full560_original_coordinate_rows_verified': True})
                blocks.append(self.ref(name))
            matrix = [[] for _ in range(127)]
            for reference in blocks:
                data = read(bound(self.out, reference))['matrix']
                for i, row in enumerate(data):
                    matrix[i].extend(row)
            C = matrix_decode(matrix)
            assert C * C == eye(127)
            self.put('holomorphic-semilinear-action', {'source_H': self.ref('original-holomorphic-Fourier-matrix'),
                'source_inverse': self.ref('holomorphic-selected-exact-inverse'), 'column_blocks': blocks,
                'matrix_shape': [127, 127], 'matrix_over_Q': matrix,
                'coefficient_action': 'C*bar(x), bar(s)=-s', 'actual_involution_square_verified': True,
                'all560_times127_original_coordinates_verified': True,
                'actual_even_selected_row_count': self.signs.count(1), 'actual_odd_selected_row_count': self.signs.count(-1),
                'full146_or272_conjugation_matrix_computed': False})
        self.C = matrix_decode(self.load('holomorphic-semilinear-action')['matrix_over_Q'])

    def fixed_basis(self):
        blocks = []
        for first in range(0, 127, 8):
            stop = min(127, first + 8)
            name = 'Q-fixed-basis-columns-%03d-%03d' % (first, stop)
            if self.load(name) is None:
                self.budget()
                inv = cols(self.Qinv, first, stop)
                P0 = fmpq_mat([[inv[i, k] if self.signs[first+k] == 1 else 0
                               for k in range(stop-first)] for i in range(127)])
                P1 = fmpq_mat([[-inv[i, k] / 3 if self.signs[first+k] == -1 else 0
                               for k in range(stop-first)] for i in range(127)])
                assert self.C * P0 == P0 and self.C * P1 == -P1
                F0, F1 = self.H * P0, self.H * P1
                for i in range(560):
                    sign = 1 if (i // 40) % 2 == 0 else -1
                    for k in range(stop-first):
                        assert sign * F0[i, k] == F0[i, k]
                        assert -sign * F1[i, k] == F1[i, k]
                V0, V1 = self.B * P0, self.B * P1
                columns = []
                for k, j in enumerate(range(first, stop)):
                    original = [[qencode(V0[i, k]), qencode(V1[i, k])] for i in range(146)]
                    normal = []
                    for i in range(145):
                        if i == 0:
                            coefficients = [[V0[0, k], V1[0, k]], [V0[1, k], V1[1, k]]]
                        else:
                            coefficients = [[V0[i+1, k] - (V0[1, k] if i == 72 else 0),
                                             V1[i+1, k] - (V1[1, k] if i == 72 else 0)]]
                        if any(x for term in coefficients for x in term):
                            normal.append({'normal_basis_index': i,
                                'K_polynomial_low_to_high': [[qencode(x) for x in term] for term in coefficients]})
                    # Full inverse normal-to-original-V1 transport, no second R864 positive change.
                    recovered = [[fmpq(0), fmpq(0)] for _ in range(146)]
                    for term in normal:
                        i = term['normal_basis_index']
                        coefficients = [[qdecode(x) for x in row] for row in term['K_polynomial_low_to_high']]
                        if i == 0:
                            recovered[0] = coefficients[0]
                            recovered[1] = coefficients[1]
                        else:
                            recovered[i+1] = coefficients[0]
                    for component in range(2):
                        recovered[73][component] += recovered[1][component]
                    assert all(recovered[i][0] == V0[i, k] and recovered[i][1] == V1[i, k] for i in range(146))
                    columns.append({'Q_basis_index': j, 'selected_original_row': self.selected[j],
                        'selected_qY_order': self.selected[j] // 40,
                        'selected_scalar_in_original_1_s_basis': [[1, 1], [0, 1]] if self.signs[j] == 1 else [[0, 1], [-1, 3]],
                        'original_V1_coefficients_in_1_s_basis': original,
                        'tau_function_normal_polynomial_in_1_s_basis': normal,
                        'differential': '82*original_V1_section*dqY/qY = normal_function*nu'})
                self.put(name, {'source_semilinear_action': self.ref('holomorphic-semilinear-action'),
                    'source_inverse': self.ref('holomorphic-selected-exact-inverse'),
                    'first_column': first, 'stop_column': stop, 'K_basis': ['1', 's'], 's_square': -3,
                    'coordinates_in_original_K_holomorphic_basis': {'rational_part': matrix_encode(P0), 's_part': matrix_encode(P1)},
                    'basis_columns': columns, 'C_times_conjugate_P_equals_P_verified': True,
                    'all560_original_fixed_expansion_rows_verified': True,
                    'all_original_V1_normal_roundtrips_verified': True})
            blocks.append(self.ref(name))
        if self.load('complete-Q-fixed-holomorphic-basis') is None:
            self.put('complete-Q-fixed-holomorphic-basis', {'source_inverse': self.ref('holomorphic-selected-exact-inverse'),
                'source_semilinear_action': self.ref('holomorphic-semilinear-action'), 'basis_column_blocks': blocks,
                'dimension_over_Q': 127, 'original_field': 'Q(s),s=1+2*zeta,s^2=-3',
                'complete_original_Q_holomorphic_basis_certified': True,
                'all127_vectors_fixed_by_actual_c_Y': True,
                'independence_and_completeness_from_invertible_Qinv_times_nonzero_diagonal': True,
                'original_tau_and_nu_fixed_norms_preserved': True,
                'old_conjugates_or_cusp_kernel_or_Fourier_coefficients_recomputed': False,
                'connection_period_Hecke_or_height_computed': False})

    def finish(self, complete, reason):
        files = []
        for path in sorted(self.out.glob(PREFIX + '*.json.gz')):
            if path.name in ('R866-current.json.gz', 'R866-exact-stages-manifest.json.gz'):
                continue
            value = read(path)
            assert value['result'] == RESULT and value['configuration'] == self.tag and value['complete'] is True
            files.append(spec(path))
        manifest = self.out / 'R866-exact-stages-manifest.json.gz'
        save(manifest, {'result': RESULT, 'configuration': self.tag, 'complete': True,
            'files': files, 'actual_complete_stage_count': len(files)})
        current = self.out / 'R866-current.json.gz'
        save(current, {'result': RESULT, 'configuration': self.tag, 'complete': False,
            'scope_complete': complete, 'stop_reason': reason, 'source_stage_manifest': spec(manifest)})
        refs = {key: self.ref(name) if self.load(name) else None for key, name in {
            'source_audit': 'source-audit', 'holomorphic_Fourier_matrix': 'original-holomorphic-Fourier-matrix',
            'selected_exact_inverse': 'holomorphic-selected-exact-inverse',
            'semilinear_action': 'holomorphic-semilinear-action',
            'Q_fixed_holomorphic_basis': 'complete-Q-fixed-holomorphic-basis'}.items()}
        if complete:
            assert all(refs.values())
        final = {'result': RESULT, 'configuration': self.tag, 'complete': complete, 'p': 41, **refs,
            'complete_original_Q_holomorphic_basis_certified': complete,
            'actual_original_c_Y_semilinear_action_certified': complete,
            'full_original_Fourier_coordinate_rows': 560,
            'actual_holomorphic_dimension': 127 if complete else None,
            'connection_period_Hecke_or_height_computed': False,
            'full146_or272_conjugation_matrix_computed': False,
            'old_source_mathematics_recomputed': False,
            'stage_manifest': spec(manifest), 'resume_state': spec(current),
            'stop_reason': reason, 'seconds': time.monotonic() - self.start}
        save(self.out / FINAL, final)
        return final

    def run(self):
        if (self.out / FINAL).exists():
            final = read(self.out / FINAL)
            assert final['result'] == RESULT and final['configuration'] == self.tag
            if final['complete']:
                for entry in read(bound(self.out, final['stage_manifest']))['files']:
                    bound(self.out, entry)
                return final
        self.inputs()
        self.Fourier_matrix()
        self.inverse()
        self.semilinear_action()
        self.fixed_basis()
        return self.finish(True, 'complete')


def main():
    sys.set_int_max_str_digits(0)
    assert os.environ.get('GITHUB_ACTIONS') == 'true', 'New exact arithmetic requires public Actions'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--budget-minutes', required=True, type=float)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    job, final, code, error = None, None, 1, None
    try:
        job = Job(read(args.config), args.out, args.budget_minutes)
        final = job.run()
        code = 0
    except BudgetStop as exc:
        error = str(exc)
        final = job.finish(False, 'budget')
        code = 124
    except Exception as exc:
        error = type(exc).__name__ + ': ' + str(exc)
        traceback.print_exc()
        if job is not None:
            final = job.finish(False, 'error')
    finally:
        save(args.out / 'core-receipt.json', {'result': RESULT, 'source_sha256': sha(__file__),
            'complete': code == 0, 'process_exit_code': code, 'error': error,
            'certificate_sha256': sha(args.out / FINAL) if final else None,
            'actual_original_c_Y_semilinear_action_certified': code == 0,
            'complete_original_Q_holomorphic_basis_certified': code == 0})
    if final:
        print('R866_RESULT=' + json.dumps({key: final[key] for key in
            ('complete', 'actual_holomorphic_dimension', 'seconds')}), flush=True)
    raise SystemExit(code)


if __name__ == '__main__':
    main()
