#!/usr/bin/env python3
"""Genuine original-Y T7 from old level82 rows and the completed R866 inverse.

New exact arithmetic is restricted to public Actions.  No old q coefficient,
holomorphic kernel, Fourier prefix, row selection, or inverse is recomputed.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import sys
import time
import traceback

import flint
from flint import fmpq, fmpq_mat, fmpq_poly, fmpz_poly

RESULT = 'R865-original-Y-Hecke-T7-and-spectral-projectors'
FINAL = 'p41-original-Y-Hecke-T7-certificate.json'
PREFIX = 'R865-'
REPOSITORY = 'Rogerhu12/math-research-public'
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
LABELS = ('R786', 'R864', 'R866')
PROOF_KEYS = ('R865', 'R866', 'R864', 'R778', 'R802')
STRATEGY = {
    'scope': 'genuine_original_Y_T7_and_exact_single_operator_spectrum',
    'original_p': 41, 'level': 82, 'holomorphic_dimension': 127,
    'G': 'original_C3_times_nonsplit_Cartan_normalizer_mod41',
    'Gamma': 'inverse_image_of_original_G_intersection_SL2_mod82',
    'g7': [[1, -2], [2, 3]],
    'gamma0': [[1, -12], [2, -23]],
    'gamma_infinity': [[47, -2], [-70, 3]],
    'finite_representatives': 'gamma0 * [[1,82*b],[0,7]], b=0..6',
    'infinite_representative': 'gamma_infinity * diag(7,1)',
    'slash_normalization': 'det(A)*(c*tau+d)^(-2)',
    'first_galois_mod82': 47, 'first_galois_mod41': 6,
    'second_galois_mod82': 7, 'second_galois_mod41': 7,
    'coefficient_field': 'Q(xi41), with K=Q(s),s^2=-3 fixed by sigma_d',
    'original_twist': 'minus3; cY F(qY)=c0(F)(-qY); c0 fixes xi41',
    'qY': 'exp(2*pi*i*tau/82)', 'xi82': '-xi41^21',
    'original_section_integer_scale': '6724',
    'new_scale_relative_to_original_e_i_coefficients': [1, 1],
    'differential_from_F': '82*F*dqY/qY',
    'target_qY_orders_inclusive': [0, 13],
    'maximum_original_qY_order_consumed': 91,
    'original_prefix_qY_bound': 128,
    'original_row_convention': '40*n+r', 'full_coordinate_rows': 560,
    'source_H_J_inverse_reused_without_recomputation': True,
    'source_H_orders_0_to13_reused_without_new_basis_products': True,
    'coordinate_column_block_size': 8,
    'matrix_convention': 'T7(F_j)=sum_i F_i*M[i,j]',
    'Q_basis_matrix': 'K_J*U; unequal_selected_parity_entries_exactly_zero',
    'characteristic_polynomial': 'product_of_actual_even_and_odd_Q_basis_block_charpolys',
    'spectral_projectors': 'CRT_polynomials_in_true_T7; no_expanded_projector_matrices',
    'full_Hecke_isotypic_or_eta_support_claimed': False,
    'budget_resume_and_transport_excluded_from_mathematical_identity': True,
}


class BudgetStop(Exception):
    pass


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            value.update(block)
    return value.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    raw = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if path.suffix == '.gz':
        with temporary.open('wb') as stream:
            with gzip.GzipFile(filename='', mode='wb', fileobj=stream, mtime=0, compresslevel=6) as zipped:
                zipped.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def plain(row):
    row = {key: row[key] for key in ('file', 'bytes', 'sha256')}
    name = PurePosixPath(row['file'])
    assert len(name.parts) == 1 and name.name not in ('', '.', '..') and '\\' not in row['file']
    assert isinstance(row['bytes'], int) and row['bytes'] >= 0 and len(row['sha256']) == 64
    return row


def spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def bound(folder, row):
    row = plain(row)
    path = Path(folder) / row['file']
    assert spec(path) == row
    return path


def identity(source):
    return {key: source[key] for key in BASE}


def source_identity(source):
    return {**identity(source), 'certificate': plain(source['certificate']),
            'configuration_sha256': source['configuration_sha256'],
            'selected_files_sha256': fingerprint(source['files']),
            'selected_file_count': len(source['files'])}


def qread(value):
    assert len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def qwrite(value):
    value = fmpq(value)
    return [str(value.numerator), str(value.denominator)]


def mread(rows, n=None, m=None):
    if n is not None:
        assert len(rows) == n
    if m is not None:
        assert all(len(row) == m for row in rows)
    return fmpq_mat([[qread(x) for x in row] for row in rows])


def mwrite(matrix):
    return [[qwrite(matrix[i, j]) for j in range(matrix.ncols())] for i in range(matrix.nrows())]


def column_block(matrix, first, stop):
    return fmpq_mat([[matrix[i, j] for j in range(first, stop)] for i in range(matrix.nrows())])


def polynomial_write(value):
    return [qwrite(value[i]) for i in range(value.degree() + 1)]


def polynomial_read(rows):
    return fmpq_poly([qread(row) for row in rows])


def integer_polynomial(value):
    result = []
    for i in range(value.degree() + 1):
        coefficient = fmpq(value[i])
        assert coefficient.denominator == 1
        result.append(str(coefficient.numerator))
    return result


class Source:
    def __init__(self, label, item):
        self.label, self.item = label, item
        self.directory = Path(item['directory'])
        self.files = {name: plain(row) for name, row in item['files'].items()}
        assert all(name == row['file'] for name, row in self.files.items())
        for row in self.files.values():
            bound(self.directory, row)
        manifest = read(self.directory / 'full-outputs-manifest.json')
        assert self.files['full-outputs-manifest.json']['sha256'] == item['manifest_sha256']
        assert manifest['result'] == item['result']
        entries = {row['file']: plain(row) for row in manifest['files']}
        assert len(entries) == len(manifest['files']) == item['manifest_file_count']
        for name, row in self.files.items():
            if name != 'full-outputs-manifest.json':
                assert entries[name] == row
        initial, run, core = (read(self.directory / name) for name in
                              ('public-actions-input.json', 'run-receipt.json', 'core-receipt.json'))
        assert initial['source_commit'] == run['source_commit'] == item['source_commit']
        assert str(run['workflow_run_id']) == str(item['run_id'])
        assert initial['core_sha256'] == core['source_sha256'] == item['core_sha256']
        assert run['complete'] is True and run['process_exit_code'] == 0 and core['complete'] is True
        assert run['core_receipt_sha256'] == self.files['core-receipt.json']['sha256']
        assert core['certificate_sha256'] == item['certificate']['sha256']
        self.certificate = read(bound(self.directory, item['certificate']))
        assert self.certificate['complete'] is True and self.certificate['result'] == item['result']
        self.configuration = self.certificate['configuration']
        assert self.configuration['source_sha256'] == item['core_sha256']
        assert fingerprint(self.configuration) == item['configuration_sha256']
        stage_key = 'stages_manifest' if label == 'R786' else 'stage_manifest'
        index = self.stage(self.certificate[stage_key])
        indexed = {row['file']: plain(row) for row in index['files']}
        assert len(indexed) == len(index['files'])
        for name in self.files:
            if name.endswith('.json.gz') and name != self.certificate[stage_key]['file']:
                assert indexed[name] == self.files[name]

    def stage(self, row):
        row = plain(row)
        assert self.files[row['file']] == row
        value = read(bound(self.directory, row))
        assert value['complete'] is True and value['configuration'] == self.configuration
        if self.label == 'R786':
            # This frozen producer's row files carry result only in configuration.
            assert value.get('result', self.configuration['result']) == self.item['result']
        else:
            assert value['result'] == self.item['result']
        return value


class Job:
    def __init__(self, config, output, budget):
        self.config, self.out = config, Path(output)
        self.started = time.monotonic()
        self.deadline = self.started + 60 * budget
        self.out.mkdir(parents=True, exist_ok=True)
        assert config['result'] == RESULT and config['core_sha256'] == sha(__file__)
        assert config['p'] == 41 and flint.__version__ == '0.9.0'
        assert set(config['proofs_sha256']) == set(PROOF_KEYS)
        assert set(config['sources']) == set(LABELS)
        self.sources = {label: Source(label, config['sources'][label]) for label in LABELS}
        self.tag = {'result': RESULT, 'source_sha256': sha(__file__), 'python_flint': flint.__version__,
                    'p': 41, 'proofs_sha256': config['proofs_sha256'], 'method_sha256': config['method_sha256'],
                    'sources': {label: source_identity(config['sources'][label]) for label in LABELS},
                    'strategy': STRATEGY}
        self.inputs()

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop('Budget ended between completed original-T7 stages.')

    def path(self, name):
        return self.out / (PREFIX + name + '.json.gz')

    def ref(self, name):
        return spec(self.path(name))

    def load(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value['result'] == RESULT and value['configuration'] == self.tag and value['complete'] is True
        return value

    def put(self, name, data):
        value = {'result': RESULT, 'configuration': self.tag, 'complete': True, **data}
        if self.path(name).exists():
            assert read(self.path(name)) == value
        else:
            save(self.path(name), value)
        return value

    def inputs(self):
        original, basis_source, shared = (self.sources[label] for label in LABELS)
        cert, c864, c866 = original.certificate, basis_source.certificate, shared.certificate
        assert cert['exact_K_basis_prefix_bound_qY'] == 128
        assert cert['all_original_R775_mod739_short_series_compared'] is True
        assert c864['complete_original_K_holomorphic_basis_certified'] is True
        assert c864['actual_cusp_evaluation_rank'] == 19 and c864['actual_kernel_dimension'] == 127
        assert c866['complete_original_Q_holomorphic_basis_certified'] is True
        assert c866['actual_original_c_Y_semilinear_action_certified'] is True
        assert c866['actual_holomorphic_dimension'] == 127 and c866['full_original_Fourier_coordinate_rows'] == 560
        for label in ('R786', 'R864'):
            assert c866['configuration']['sources'][label] == source_identity(self.config['sources'][label])
        self.basis_spec = plain(c864['holomorphic_differential_basis'])
        basis = basis_source.stage(self.basis_spec)
        assert basis['complete_original_K_holomorphic_basis_certified'] is True
        assert basis['all_original_V1_coordinate_roundtrips_verified'] is True
        assert basis['actual_dimension_over_K'] == 127
        assert len(basis['basis']) == 127
        self.B = fmpq_mat([[qread(basis['basis'][j]['original_V1_coefficients'][i])
                            for j in range(127)] for i in range(146)])
        self.Hspec, self.Uspec = (plain(c866[key]) for key in ('holomorphic_Fourier_matrix', 'selected_exact_inverse'))
        H, inverse = shared.stage(self.Hspec), shared.stage(self.Uspec)
        assert H['source_original_holomorphic_basis'] == self.basis_spec
        assert H['matrix_shape'] == [560, 127] and H['row_convention'] == '40*n+r'
        assert H['matrix_integer_scale'] == '6724' and H['new_scale_relative_to_original_e_i_coefficients'] == [1, 1]
        assert H['differential_coefficients_equal_matrix_times_82'] is True
        assert H['all40_constant_coefficients_exactly_zero'] is True
        assert inverse['source_H'] == self.Hspec and inverse['both_exact_inverse_products_verified'] is True
        assert inverse['actual_exact_minor_determinant'][0] != '0'
        assert inverse['matrix_shape'] == [127, 127] and inverse['section_integer_scale'] == '6724'
        assert inverse['full_original_row_numbers_not_compressed'] is True
        selection = shared.stage(inverse['source_row_selection'])
        self.J = inverse['selected_rows']
        assert self.J == selection['selected_rows'] and len(set(self.J)) == 127
        assert all(40 <= r < 560 for r in self.J)
        self.H = mread(H['matrix_rational_num_den'], 560, 127)
        self.U = mread(inverse['inverse'], 127, 127)
        self.Q = mread(inverse['selected_minor_matrix'], 127, 127)
        # Pure equality to the imported source; do not multiply the old inverse again.
        assert all(self.Q[i, j] == self.H[self.J[i], j] for i in range(127) for j in range(127))
        assert all(not self.H[i, j] for i in range(40) for j in range(127))
        self.signs = [1 if (r // 40) % 2 == 0 else -1 for r in self.J]
        self.fixed_spec = plain(c866['Q_fixed_holomorphic_basis'])
        fixed = shared.stage(self.fixed_spec)
        assert fixed['source_inverse'] == self.Uspec and fixed['dimension_over_Q'] == 127
        assert fixed['complete_original_Q_holomorphic_basis_certified'] is True
        assert fixed['all127_vectors_fixed_by_actual_c_Y'] is True
        assert c866['configuration']['strategy']['Q_fixed_column_rule'] == 'inverse_column_if_even_order_else_inverse_column_over_original_s'
        action = shared.stage(c866['semilinear_action'])
        assert action['source_inverse'] == self.Uspec and action['source_H'] == self.Hspec
        assert action['all560_times127_original_coordinates_verified'] is True
        self.prefix_specs, self.prefix = [], []
        for i in range(146):
            name = 'R786-exact-power-1-row-%04d.json.gz' % i
            row = original.files[name]
            value = original.stage(row)
            assert value['weight'] == 2 and value['recipe']['kind'] == 'det_semilinear_E1_pair_trace'
            assert value['integer_scale'] == '6724' and value['bound_qY'] == 128
            assert value['original_R775_finite_coefficients_verified'] is True
            assert value['recipe']['exact_global_field'] == 'K'
            coeffs = value['integer_qY_xi_coefficients']
            assert len(coeffs) == 129 and all(len(x) == 40 for x in coeffs)
            self.prefix_specs.append(row)
            self.prefix.append(coeffs)
        assert H['source_original_prefixes'] == self.prefix_specs
        if self.load('source-audit') is None:
            self.put('source-audit', {'source_identities': self.tag['sources'],
                'original_holomorphic_basis': self.basis_spec,
                'completed_shared_Fourier_matrix': self.Hspec, 'completed_shared_inverse': self.Uspec,
                'original_Q_fixed_basis': self.fixed_spec, 'original_prefixes': self.prefix_specs,
                'selected_original_rows': self.J, 'original_scale_preserved': '6724',
                'new_rescaling_relative_to_original_e_i': [1, 1],
                'old_cusp_kernel_prefix_products_row_selection_or_inverse_recomputed': False,
                'old_q_coefficients_or_Eisenstein_traces_recomputed': False,
                'all_selected_source_bytes_tags_and_parent_child_identities_verified': True})

    def group_certificate(self):
        name = 'original-double-coset-and-Galois-maps'
        if self.load(name) is not None:
            return
        self.budget()
        def mul(a, b):
            return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        def det(a):
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        g, g0, gi = (STRATEGY[key] for key in ('g7', 'gamma0', 'gamma_infinity'))
        assert det(g) == 7 and det(g0) == det(gi) == 1
        alpha = [mul(gi, [[7, 0], [0, 1]])] + [mul(g0, [[1, 82*b], [0, 7]]) for b in range(7)]
        assert all(det(a) == 7 for a in alpha)
        assert all((a[i][j] - g[i][j]) % 82 == 0 for a in alpha for i in range(2) for j in range(2))
        maps = {}
        for d in (6, 7):
            mapping = [[(d*r) % 41] if (d*r) % 41 < 40 else list(range(40)) for r in range(40)]
            signs = [1 if (d*r) % 41 < 40 else -1 for r in range(40)]
            maps[str(d)] = {'destination_rows': mapping, 'coefficients': signs}
        self.put(name, {'source_audit': self.ref('source-audit'), 'alpha_infinity_then_b0_to6': alpha,
            'all_determinants_and_same_original_mod82_coset_verified': True,
            'original_cyclic_7_correspondence_and_twisted_Q_descent_bound_to_proof': True,
            'galois_maps_on_original_xi41_basis': maps, 's_fixed': True,
            'first_direction_mod82': 47, 'first_direction_mod41': 6,
            'second_direction_mod82': 7, 'second_direction_mod41': 7,
            'cY_twist_and_original_82_differential_normalization_preserved': True})

    def holomorphic_order(self, n):
        assert 0 <= n <= 91
        if n <= 13:
            return fmpq_mat([[self.H[40*n+r, j] for j in range(127)] for r in range(40)]), {
                'source_group': 'R866', 'source': self.Hspec, 'qY_order': n, 'already_completed': True}
        name = 'new-holomorphic-order-%03d' % n
        value = self.load(name)
        if value is None:
            self.budget()
            original = fmpq_mat([[int(self.prefix[i][n][r]) for i in range(146)] for r in range(40)])
            value = self.put(name, {'source_audit': self.ref('source-audit'), 'qY_order': n,
                'matrix_shape': [40, 127], 'matrix': mwrite(original * self.B),
                'source_original_prefixes': self.prefix_specs,
                'original_basis': self.basis_spec, 'new_q_coefficients_generated': False,
                'only_new_basis_linear_combination': True, 'original_scale': '6724'})
        return mread(value['matrix'], 40, 127), {'source_group': 'R865', 'source': self.ref(name),
                                                 'qY_order': n, 'already_completed': False}

    def galois(self, matrix, d):
        answer = fmpq_mat(40, matrix.ncols())
        for r in range(40):
            e = (d*r) % 41
            if e == 40:
                for j in range(matrix.ncols()):
                    for i in range(40):
                        answer[i, j] -= matrix[r, j]
            else:
                for j in range(matrix.ncols()):
                    answer[e, j] += matrix[r, j]
        return answer

    def targets(self):
        specs = []
        for n in range(1, 14):
            name = 'T7-target-order-%02d' % n
            if self.load(name) is None:
                high, high_source = self.holomorphic_order(7*n)
                self.budget()
                target = self.galois(high, 6)
                low_source = None
                if n % 7 == 0:
                    low, low_source = self.holomorphic_order(n//7)
                    target += 7 * self.galois(low, 7)
                self.put(name, {'source_double_coset': self.ref('original-double-coset-and-Galois-maps'),
                    'qY_order': n, 'first_input': high_source, 'second_input': low_source,
                    'matrix_shape': [40, 127], 'matrix': mwrite(target),
                    'first_sigma_mod41': 6, 'second_sigma_mod41': 7, 'second_scalar': 7,
                    'full40_original_cyclotomic_coordinates': True})
            specs.append(self.ref(name))
        name = 'T7-target-index'
        if self.load(name) is None:
            self.put(name, {'source_audit': self.ref('source-audit'), 'order_blocks': specs,
                'qY_order_range_inclusive': [1, 13], 'full_matrix_shape_including_zero_constant': [560, 127],
                'zero_constant_from_original_cusp_forms': True, 'maximum_original_order': 91,
                'original_q_tail_recomputed': False})
        rows = [[[str(0), str(1)] for _ in range(127)] for _ in range(40)]
        for row in self.load(name)['order_blocks']:
            rows += read(bound(self.out, row))['matrix']
        self.K = mread(rows, 560, 127)
        self.KJ = fmpq_mat([[self.K[r, j] for j in range(127)] for r in self.J])

    def coordinates(self):
        blocks = []
        for first in range(0, 127, 8):
            stop = min(first + 8, 127)
            name = 'T7-original-K-columns-%03d-%03d' % (first, stop)
            if self.load(name) is None:
                self.budget()
                target = column_block(self.K, first, stop)
                solution = self.U * column_block(self.KJ, first, stop)
                assert self.H * solution == target
                self.put(name, {'source_target_index': self.ref('T7-target-index'),
                    'source_shared_inverse': self.Uspec, 'source_shared_H': self.Hspec,
                    'first_column': first, 'stop_column': stop, 'matrix_shape': [127, stop-first],
                    'matrix': mwrite(solution), 'full560_original_coordinate_rows_verified': True,
                    'only_selected_row_check_used': False, 'new_inverse_computed': False})
            blocks.append(self.ref(name))
        rows = [[] for _ in range(127)]
        for row in blocks:
            value = read(bound(self.out, row))
            for i in range(127):
                rows[i] += value['matrix'][i]
        self.M = mread(rows, 127, 127)
        name = 'T7-original-K-matrix'
        if self.load(name) is None:
            self.put(name, {'column_blocks': blocks, 'matrix_shape': [127, 127], 'matrix': rows,
                'source_basis': self.basis_spec, 'source_target_index': self.ref('T7-target-index'),
                'all560_times127_original_coordinates_verified': True,
                'global_T7_identity_from_true_correspondence_and_13_order_injectivity': True,
                'original_Y_minus3_twist_preserved': True})

    def rational_basis_matrix(self):
        blocks = []
        for first in range(0, 127, 8):
            stop = min(first + 8, 127)
            name = 'T7-original-Q-columns-%03d-%03d' % (first, stop)
            if self.load(name) is None:
                self.budget()
                Ub = column_block(self.U, first, stop)
                N = self.KJ * Ub
                assert self.M * Ub == self.U * N
                assert all(not N[i, k] for i in range(127) for k in range(stop-first)
                           if self.signs[i] != self.signs[first+k])
                self.put(name, {'source_K_matrix': self.ref('T7-original-K-matrix'),
                    'source_Q_fixed_basis': self.fixed_spec, 'source_shared_inverse': self.Uspec,
                    'first_column': first, 'stop_column': stop, 'matrix_shape': [127, stop-first],
                    'matrix': mwrite(N), 'M_times_Ublock_equals_U_times_Nblock_verified': True,
                    'all_unequal_parity_entries_exactly_zero': True,
                    'original_s_diagonal_basis_factors_cancel_only_on_equal_parity': True})
            blocks.append(self.ref(name))
        rows = [[] for _ in range(127)]
        for row in blocks:
            value = read(bound(self.out, row))
            for i in range(127):
                rows[i] += value['matrix'][i]
        self.N = mread(rows, 127, 127)
        name = 'T7-original-Q-matrix'
        if self.load(name) is None:
            self.put(name, {'source_original_Q_fixed_basis': self.fixed_spec, 'column_blocks': blocks,
                'matrix_shape': [127, 127], 'matrix_over_Q': rows,
                'selected_original_rows': self.J, 'deck_involution_signs': self.signs,
                'actual_even_dimension': self.signs.count(1), 'actual_odd_dimension': self.signs.count(-1),
                'actual_original_Q_basis_matrix_certified': True,
                'cY_not_replaced_by_coefficient_conjugation_only': True,
                'old_Q_fixed_basis_recomputed': False})

    def spectrum(self):
        components = []
        for sign in (1, -1):
            label = 'plus' if sign == 1 else 'minus'
            name = 'T7-characteristic-polynomial-' + label
            if self.load(name) is None:
                self.budget()
                indices = [i for i in range(127) if self.signs[i] == sign]
                block = fmpq_mat([[self.N[i, j] for j in indices] for i in indices])
                cp = block.charpoly()
                assert cp.degree() == len(indices) and cp[cp.degree()] == 1
                integers = integer_polynomial(cp)
                self.put(name, {'source_Q_matrix': self.ref('T7-original-Q-matrix'),
                    'deck_involution_sign': sign, 'original_Q_basis_indices': indices,
                    'actual_dimension': len(indices), 'characteristic_polynomial_ascending': integers,
                    'all_characteristic_coefficients_integral': True,
                    'original_block_not_replaced_by_older_genus54_matrix': True})
            components.append(self.ref(name))
        name = 'T7-characteristic-polynomial-and-factorization'
        if self.load(name) is None:
            self.budget()
            cp = fmpz_poly([1])
            for row in components:
                value = read(bound(self.out, row))
                cp *= fmpz_poly([int(x) for x in value['characteristic_polynomial_ascending']])
            assert cp.degree() == 127 and cp[127] == 1
            content, factors = cp.factor()
            assert content == 1
            factors.sort(key=lambda item: (item[0].degree(), tuple(int(x) for x in item[0].coeffs())))
            product, squarefree = fmpz_poly([1]), fmpz_poly([1])
            rows = []
            for i, (f, multiplicity) in enumerate(factors):
                assert multiplicity >= 1 and f.degree() >= 1 and f[f.degree()] == 1
                product *= f ** multiplicity
                squarefree *= f
                rows.append({'factor_index': i, 'degree': f.degree(), 'multiplicity': multiplicity,
                             'polynomial_ascending': [str(x) for x in f.coeffs()]})
            assert product == cp and squarefree.gcd(squarefree.derivative()) == 1
            self.put(name, {'source_Q_matrix': self.ref('T7-original-Q-matrix'), 'component_polynomials': components,
                'characteristic_polynomial_ascending': [str(x) for x in cp.coeffs()], 'irreducible_factors': rows,
                'all_factor_products_exactly_verified': True,
                'minimal_polynomial_ascending': [str(x) for x in squarefree.coeffs()],
                'minimal_polynomial_squarefree_from_original_Rosati_selfadjointness': True,
                'minimal_polynomial_matrix_evaluation_recomputed': False,
                'full_Hecke_isotypic_decomposition_claimed': False})
        factorization = self.load(name)
        minimal = fmpq_poly([int(x) for x in factorization['minimal_polynomial_ascending']])
        factors = factorization['irreducible_factors']
        projectors = []
        for row in factors:
            i = row['factor_index']
            name = 'T7-spectral-projector-%03d' % i
            if self.load(name) is None:
                self.budget()
                f = fmpq_poly([int(x) for x in row['polynomial_ascending']])
                complement, remainder = divmod(minimal, f)
                assert remainder == 0
                gcd, left, right = f.xgcd(complement)
                assert gcd == 1 and left*f + right*complement == 1
                e = (right * complement) % minimal
                assert (e*e-e) % minimal == 0
                for other in factors:
                    divisor = fmpq_poly([int(x) for x in other['polynomial_ascending']])
                    assert e % divisor == (1 if other['factor_index'] == i else 0)
                denominator = 1
                for x in e.coeffs():
                    denominator = math.lcm(denominator, int(x.denominator))
                integral = integer_polynomial(e * denominator)
                self.put(name, {'source_factorization': self.ref('T7-characteristic-polynomial-and-factorization'),
                    'factor_index': i, 'factor': row, 'Bézout_left': polynomial_write(left),
                    'Bézout_right': polynomial_write(right), 'complement': polynomial_write(complement),
                    'projector_polynomial': polynomial_write(e), 'integer_multiple': str(denominator),
                    'integral_correspondence_polynomial': integral,
                    'actual_spectral_dimension': row['degree'] * row['multiplicity'],
                    'exact_Bezout_idempotence_and_all_factor_residues_verified': True,
                    'original_correspondence_recipe': 'evaluate integral polynomial in genuine original T7',
                    'expanded_projector_matrix_or_fiber_product_computed': False,
                    'Y_active_eta_projector_claimed': False, 'denominator_minimality_claimed': False})
            projectors.append(self.ref(name))
        name = 'T7-spectral-projector-index'
        if self.load(name) is None:
            self.budget()
            total = fmpq_poly([])
            dimension = 0
            for row in projectors:
                value = read(bound(self.out, row))
                total += polynomial_read(value['projector_polynomial'])
                dimension += value['actual_spectral_dimension']
            assert (total - 1) % minimal == 0 and dimension == 127
            self.put(name, {'source_factorization': self.ref('T7-characteristic-polynomial-and-factorization'),
                'projectors': projectors, 'sum_is_identity_mod_true_minimal_polynomial_verified': True,
                'dimensions_sum_to_127_verified': True,
                'orthogonality_from_all_distinct_factor_residues_verified': True,
                'only_one_original_Hecke_operator_used': True,
                'all_Hecke_types_or_modified_diagonal_support_computed': False})

    def finish(self, complete, reason):
        files = []
        for path in sorted(self.out.glob(PREFIX + '*.json.gz')):
            if path.name == PREFIX + 'current.json.gz' or path.name.startswith(PREFIX + 'stage-manifest-'):
                continue
            value = read(path)
            assert value['result'] == RESULT and value['configuration'] == self.tag and value['complete'] is True
            files.append(spec(path))
        digest = fingerprint(files)
        manifest_path = self.out / (PREFIX + 'stage-manifest-' + digest + '.json.gz')
        inventory = {'result': RESULT, 'configuration': self.tag, 'complete': True, 'files': files,
                     'actual_complete_stage_count': len(files)}
        if manifest_path.exists():
            assert read(manifest_path) == inventory
        else:
            save(manifest_path, inventory)
        refs = {}
        for key, name in {'source_audit': 'source-audit', 'double_coset': 'original-double-coset-and-Galois-maps',
                          'target_index': 'T7-target-index', 'matrix_in_original_K_basis': 'T7-original-K-matrix',
                          'matrix_in_original_Q_fixed_basis': 'T7-original-Q-matrix',
                          'characteristic_polynomial_and_factorization': 'T7-characteristic-polynomial-and-factorization',
                          'spectral_projectors': 'T7-spectral-projector-index'}.items():
            refs[key] = self.ref(name) if self.path(name).exists() else None
        if complete:
            assert all(refs.values())
        current_path = self.out / (PREFIX + 'current.json.gz')
        save(current_path, {'result': RESULT, 'configuration': self.tag, 'complete': False,
            'scope_complete': complete, 'stop_reason': reason, 'actual_stage_manifest': spec(manifest_path)})
        cert = {'result': RESULT, 'configuration': self.tag, 'complete': complete, 'p': 41, **refs,
            'genuine_original_Y_T7_matrix_certified': complete,
            'actual_original_Q_fixed_basis_matrix_certified': complete,
            'full560_times127_original_Hecke_equations_verified': complete,
            'exact_single_operator_spectral_projectors_certified': complete,
            'stage_manifest': spec(manifest_path), 'resume_state': spec(current_path),
            'old_Fourier_prefix_kernel_or_inverse_recomputed': False,
            'new_Eisenstein_q_coefficients_or_original_q_tail_generated': False,
            'full_Hecke_isotypic_decomposition_computed': False,
            'Y_active_eta_projector_computed': False, 'original_torsion_clearing_N_computed': False,
            'principal_Hecke_calibration_function_computed': False,
            'non_p_height_support_or_values_computed': False,
            'period_or_height_computed': False, 'height_nonzero_proved': False,
            'stop_reason': reason, 'seconds': time.monotonic() - self.started}
        save(self.out / FINAL, cert)
        return cert

    def run(self):
        final_path = self.out / FINAL
        if final_path.exists():
            old = read(final_path)
            assert old['configuration'] == self.tag and old['result'] == RESULT
            if old['complete']:
                for row in read(bound(self.out, old['stage_manifest']))['files']:
                    bound(self.out, row)
                return old
        self.group_certificate()
        self.targets()
        self.coordinates()
        self.rational_basis_matrix()
        self.spectrum()
        return self.finish(True, 'complete')


def main():
    assert os.environ.get('GITHUB_ACTIONS') == 'true'
    assert os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--budget-minutes', type=float, required=True)
    args = parser.parse_args()
    assert 0 < args.budget_minutes <= 300
    args.output.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    job, final, code, error = None, None, 1, None
    try:
        job = Job(read(args.config), args.output, args.budget_minutes)
        final = job.run()
        code = 0
    except BudgetStop as exc:
        error, code = str(exc), 124
        if job is not None:
            final = job.finish(False, 'budget')
    except Exception:
        error = traceback.format_exc()
        print(error, flush=True)
        if job is not None:
            final = job.finish(False, 'error')
    receipt = {'result': RESULT, 'source_sha256': sha(__file__), 'complete': code == 0,
        'process_exit_code': code, 'error': error, 'configuration': None if job is None else job.tag,
        'certificate_sha256': sha(args.output / FINAL) if final is not None else None,
        'seconds': time.monotonic() - started}
    save(args.output / 'core-receipt.json', receipt)
    print('R865_CORE_RECEIPT=' + json.dumps(receipt, sort_keys=True), flush=True)
    if final is not None:
        print('R865_RESULT=' + json.dumps({key: final[key] for key in
            ('complete', 'genuine_original_Y_T7_matrix_certified', 'seconds')}, sort_keys=True), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
