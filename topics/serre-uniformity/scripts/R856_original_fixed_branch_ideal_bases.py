#!/usr/bin/env python3
"""Original Cusp+P0 complete ideal bases; new arithmetic only in public Actions."""

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback

RESULT = 'R856-original-fixed-branch-ideal-bases'
FINAL = 'p41-original-fixed-branch-ideal-bases-certificate.json'
PREFIX = 'R856-'
INVENTORY = 'R856-stage-manifest.json.gz'
SCOPE = 'complete_two_chart_point_and_fixed_branch_ideal_bases'
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
PROOFS = ('proof', 'method', 'finite_RR_proof', 'cusp_proof', 'P0_proof')
EPS = [0]+[1]*144+[2]*127
N = 272
BATCH = 16
FREE = {'file': 'R805-graded-free-basis.json.gz', 'bytes': 11649,
        'sha256': '74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9'}
DEFINITIONS = {
    'R805': {'result': 'R805-original-affine-pencil-free-basis',
             'core_sha256': '730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420',
             'certificate': 'p41-original-affine-pencil-free-basis-certificate.json'},
    'R820': {'result': 'R820-original-cusp-finite-algebra-and-ideals',
             'core_sha256': '25f5582ed0c6dae2cf29d5eb288469067c09d917bfe1f565fb042978ea9b173c',
             'certificate': 'p41-original-cusp-finite-algebra-ideals-certificate.json'},
    'R837': {'result': 'R837-original-fixed-branch-pencil',
             'core_sha256': '5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924',
             'certificate': 'p41-original-fixed-branch-pencil-certificate.json'},
}
H64 = re.compile(r'[0-9a-f]{64}')
ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def guard():
    if os.environ.get('GITHUB_ACTIONS') != 'true' or \
       os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('All new mathematical arithmetic belongs to the public repository Actions.')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    raw = (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if path.suffix == '.gz':
        with temporary.open('wb') as stream:
            with gzip.GzipFile(filename='', fileobj=stream, mode='wb', compresslevel=2, mtime=0) as dest:
                dest.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def plain(value):
    out = {k: value[k] for k in ('file', 'bytes', 'sha256')}
    assert Path(out['file']).name == out['file'] and '\\' not in out['file']
    assert out['file'] not in ('.', '..')
    assert isinstance(out['bytes'], int) and out['bytes'] >= 0 and H64.fullmatch(out['sha256'])
    return out


def spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def pair(q):
    return [str(q.numerator), str(q.denominator)]


def rational(value):
    assert isinstance(value, list) and len(value) == 2
    assert all(isinstance(x, str) for x in value)
    q = Fraction(int(value[0]), int(value[1]))
    assert pair(q) == value
    return q


def encode(a):
    return [pair(a[0]), pair(a[1])]


def decode(value):
    assert isinstance(value, list) and len(value) == 2
    return rational(value[0]), rational(value[1])


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    # zeta^2 = -1-zeta in the original K basis (1,zeta).
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def inverse(a):
    assert a != ZERO
    denominator = a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
    assert denominator != 0
    answer = ((a[0]-a[1])/denominator, -a[1]/denominator)
    assert mul(a, answer) == ONE and mul(answer, a) == ONE
    return answer


def power(a, n):
    assert isinstance(n, int) and n >= 0
    answer = ONE
    while n:
        if n & 1:
            answer = mul(answer, a)
        a = mul(a, a); n //= 2
    return answer


def add_term(out, key, value):
    total = add(out.get(key, ZERO), value)
    if total == ZERO:
        out.pop(key, None)
    else:
        out[key] = total


def scalar_column(column, coefficient):
    if coefficient == ZERO:
        return {}
    return {key: mul(value, coefficient) for key, value in column.items()}


def combine(left, right, coefficient=ONE):
    result = dict(left)
    for key, value in right.items():
        add_term(result, key, mul(coefficient, value))
    return result


def multiply_linear(column, root):
    result = {}
    for (row, degree), value in column.items():
        add_term(result, (row, degree+1), value)
        add_term(result, (row, degree), neg(mul(root, value)))
    return result


def encoded_column(column):
    return [{'normal_basis_row': row, 'power': degree, 'coefficient_K_1_zeta': encode(value)}
            for (row, degree), value in sorted(column.items())]


def decoded_column(terms):
    answer = {}
    for term in terms:
        row, degree = term['normal_basis_row'], term['power']
        assert isinstance(row, int) and 0 <= row < N
        assert isinstance(degree, int) and degree >= 0
        key = (row, degree)
        assert key not in answer
        value = decode(term['coefficient_K_1_zeta'])
        assert value != ZERO
        answer[key] = value
    return answer


def evaluate(column, base_powers, normal_values):
    answer = ZERO
    for (row, degree), coefficient in column.items():
        assert degree < len(base_powers)
        answer = add(answer, mul(coefficient, mul(base_powers[degree], normal_values[row])))
    return answer


class Source:
    def __init__(self, label, item):
        self.label, self.item = label, item
        self.root = Path(item['directory'])
        definition = DEFINITIONS[label]
        assert item['result'] == definition['result']
        assert item['core_sha256'] == definition['core_sha256']
        self.files = {n: plain(s) for n, s in item['files'].items()}
        assert all(n == s['file'] for n, s in self.files.items())
        assert fingerprint({n: self.files[n] for n in sorted(self.files)}) == item['selected_files_sha256']
        for n, s in self.files.items():
            assert spec(self.root/n) == s, (label, n, 'source bytes')
        assert self.files['full-outputs-manifest.json']['sha256'] == item['manifest_sha256']
        manifest = read(self.root/'full-outputs-manifest.json')
        assert manifest['result'] == item['result']
        self.manifest = {s['file']: plain(s) for s in manifest['files']}
        assert len(self.manifest) == len(manifest['files'])
        for n, s in self.files.items():
            if n != 'full-outputs-manifest.json':
                assert self.manifest[n] == s
        run, core, initial = (read(self.root/n) for n in
                              ('run-receipt.json', 'core-receipt.json', 'public-actions-input.json'))
        assert run['result'] == core['result'] == initial['result'] == item['result']
        assert run['source_commit'] == initial['source_commit'] == item['source_commit']
        assert str(run['workflow_run_id']) == str(item['run_id'])
        assert run['complete'] is True and run['process_exit_code'] == 0 and run['error'] is None
        assert core['complete'] is True and core['source_sha256'] == item['core_sha256']
        assert initial['core_sha256'] == initial['job']['core_sha256'] == item['core_sha256']
        assert initial['source_repository'] == 'Rogerhu12/math-research-public'
        assert run['core_receipt_sha256'] == self.files['core-receipt.json']['sha256']
        name = definition['certificate']
        assert plain(item['certificate']) == self.files[name]
        assert core['certificate_sha256'] == self.files[name]['sha256']
        self.certificate = read(self.root/name)
        assert self.certificate['result'] == item['result'] and self.certificate['complete'] is True
        self.tag = self.certificate['configuration']
        assert self.tag['result'] == item['result'] and self.tag['source_sha256'] == item['core_sha256']
        assert fingerprint(self.tag) == item['configuration_sha256']
        self.initial = initial

    def indexed(self, reference):
        s = plain(reference)
        assert self.files[s['file']] == s
        value = read(self.root/s['file'])
        assert value['complete'] is True and value['configuration'] == self.tag
        if 'result' in value:
            assert value['result'] == self.item['result']
        return value

    def identity(self):
        return {**{k: self.item[k] for k in BASE},
                'configuration_sha256': self.item['configuration_sha256'],
                'selected_files_sha256': self.item['selected_files_sha256'],
                'certificate': plain(self.item['certificate'])}


class BudgetStop(Exception):
    pass


class Job:
    def __init__(self, args):
        self.args, self.started = args, time.monotonic()
        self.out = Path(args.out); self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item['result'] == RESULT and self.item['p'] == 41
        assert self.item['requested_stage'] == SCOPE and self.item['producer_inputs_pending'] is False
        assert self.item['core_sha256'] == sha(__file__)
        self.proofs = {}
        for name in PROOFS:
            value = sha(self.item[name])
            assert value == self.item[name+'_sha256']
            self.proofs[name+'_sha256'] = value
        assert set(self.item['sources']) == set(DEFINITIONS)
        self.sources = {label: Source(label, self.item['sources'][label]) for label in DEFINITIONS}
        self.tag = {
            'result': RESULT, 'source_sha256': sha(__file__), 'p': 41,
            'requested_stage': SCOPE, **self.proofs,
            'source_identities': {label: source.identity() for label, source in self.sources.items()},
            'coefficient_field': 'K=Q(zeta), zeta^2+zeta+1=0; original ordered basis (1,zeta)',
            'exact_arithmetic': 'fractions.Fraction; canonical rational pairs',
            'normal_basis_rank': N, 'normal_basis_degrees': EPS, 'charts': ['tau', 'sigma'],
            'original_R805_free_basis': FREE,
            'fixed_divisor': 'original reduced twenty cusps plus original P0=phi(c0)',
            'new_basis_rule': 'first nonzero original C-column P0 evaluation; exact one-row kernel',
            'output_column_order': 'original 0,...,271 in each chart', 'column_block_size': BATCH,
            'no_old_Fourier_rank_cusp_kernel_or_primitive_computation_repeated': True,
            'only_directories_transport_and_budget_excluded_from_mathematical_identity': True,
        }
        self.column_cache = {}

    def budget(self):
        if time.monotonic()-self.started >= 60*self.args.budget_minutes-15:
            raise BudgetStop('Completed original evaluation and ideal column blocks retained.')

    def path(self, name):
        assert Path(name).name == name and name.startswith(PREFIX)
        return self.out/(name if name.endswith('.json.gz') else name+'.json.gz')

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value['configuration'] == self.tag and value['result'] == RESULT and value['complete'] is True
        return value

    def put(self, name, value):
        path = self.path(name)
        assert not path.exists()
        save(path, {'result': RESULT, 'complete': True, 'configuration': self.tag, **value})
        return spec(path)

    def prepare(self):
        r5, r20, r37 = (self.sources[label] for label in ('R805', 'R820', 'R837'))
        c5, c20, c37 = r5.certificate, r20.certificate, r37.certificate
        assert plain(c5['graded_free_basis_stage']) == FREE == plain(r20.tag['original_R805_free_basis'])
        assert {k: r20.tag['producer_identities']['R805'][k] for k in BASE} == {k: r5.item[k] for k in BASE}
        assert c5['affine_free_module_rank'] == N and c5['actual_pencil_n'] == 1
        assert c5['graded_free_basis_degrees'] == [1, 144, 127]
        self.free = r5.indexed(FREE)
        self.pencil = r5.indexed(c5['pencil_stage'])
        assert self.free['degree1_original_indices'] == list(range(2, 146))
        self.degree2 = self.free['degree2_original_indices']
        assert len(self.degree2) == len(set(self.degree2)) == 127
        assert all(isinstance(x, int) and 0 <= x < 418 for x in self.degree2)
        assert self.free['characteristic_zero_complement_certified'] is True
        assert self.free['degree_distribution'] == [1, 144, 127]
        assert self.free['affine_free_module_rank'] == N and self.free['integer_scale'] == str(82**4)
        assert c37['original_P0_evaluation_certified'] is True
        self.p0_spec = plain(c37['original_P0_evaluation'])
        self.v2_spec = r37.files['R837-original-V2-P0-evaluation.json.gz']
        self.p0 = r37.indexed(self.p0_spec)
        self.v2 = r37.indexed(self.v2_spec)
        assert self.p0['value_count'] == 146 and self.v2['value_count'] == 418
        assert self.p0['coefficient_basis'] == ['1', 'zeta=(-1+sqrt(-3))/2']
        assert self.p0['integer_scale_already_in_source'] == str(82**2)
        assert self.p0['additional_scale_inserted'] is False
        assert self.v2['original_integer_scale_already_in_products'] == str(82**4)
        assert self.v2['all_418_original_product_recipes_used_without_rescaling'] is True
        assert plain(self.v2['original_P0_evaluation']) == self.p0_spec
        assert len(self.free['degree2_original_sources']) == 127
        for j, index in enumerate(self.degree2):
            original = self.free['degree2_original_sources'][j]
            assert original['producer'] == 'R786'
            assert plain(original) == plain(self.v2['source_rows'][index])
        assert c20['normal_basis_rank'] == N and c20['normal_basis_degrees'] == EPS
        assert c20['actual_cusp_colengths'] == {'tau': 20, 'sigma': 20}
        for key in ('original_two_chart_cusp_ideals_computed', 'complete_polynomial_kernels_certified',
                    'same_original_cusp_field_and_two_chart_transitions_verified'):
            assert c20[key] is True
        inventory = r20.indexed(c20['stage_manifest'])
        self.old_inventory = {s['file']: plain(s) for s in inventory['files']}
        assert len(self.old_inventory) == len(inventory['files']) == 590
        for n, s in self.old_inventory.items():
            assert r20.manifest[n] == s
        self.cusp_indexes, self.cusp_specs = {}, {}
        for chart in ('tau', 'sigma'):
            s = plain(c20['two_chart_cusp_ideal_indexes'][chart])
            index = r20.indexed(s)
            assert index['chart'] == chart and index['normal_basis_rank'] == N
            assert index['normal_basis_degrees'] == EPS
            assert index['actual_diagonal_degrees'] == [0]*271+[20]
            assert index['actual_total_diagonal_degree'] == index['actual_quotient_dimension_over_Q'] == 20
            for key in ('all_272_original_relations_verified_in_full_finite_algebra',
                        'canonical_lower_triangular_monic_and_reduced_conditions_verified',
                        'complete_polynomial_kernel_certified_by_inclusion_and_equal_colength'):
                assert index[key] is True
            refs = index['Hermite_columns_in_original_basis_order']
            assert len(refs) == N
            for a, ref in enumerate(refs):
                assert self.old_inventory[ref['file']] == plain(ref)
                value = r20.indexed(ref)
                assert value['kind'] == 'first_dependence' and value['chart'] == chart
                assert value['normal_basis_index'] == value['exact_original_normal_basis_column'] == a
                assert value['monic_diagonal_degree'] == (20 if a == 271 else 0)
                assert value['complete_relation_evaluation_zero_in_all_20_original_coordinates'] is True
            self.cusp_indexes[chart], self.cusp_specs[chart] = index, s
        name = 'R856-original-source-audit'
        if self.cached(name) is None:
            self.put(name, {
                'source_file_counts': {label: len(source.files) for label, source in self.sources.items()},
                'source_identities': self.tag['source_identities'],
                'original_free_basis': FREE, 'original_pencil': plain(c5['pencil_stage']),
                'original_P0_values': self.p0_spec, 'original_V2_P0_values': self.v2_spec,
                'original_two_chart_cusp_indexes': self.cusp_specs,
                'all_selected_original_bytes_and_tags_verified': True,
                'all_127_degree2_sources_matched_to_original_V2_values': True,
                'old_complete_cusp_kernels_reused_without_arithmetic': True,
            })
        return spec(self.path(name))

    def normal_values(self):
        name = 'R856-original-P0-normal-values'
        old = self.cached(name)
        if old is not None:
            assert old['source_P0_values'] == self.p0_spec and old['source_V2_P0_values'] == self.v2_spec
            assert old['source_free_basis'] == FREE and old['degree2_original_indices'] == self.degree2
            assert old['all_original_ratio_multiply_backs_verified'] is True
            return old, spec(self.path(name))
        self.budget()
        values1 = [decode(value) for value in self.p0['P0_values_K_1_zeta']]
        values2 = [decode(value) for value in self.v2['P0_values_K_1_zeta']]
        tau, sigma = values1[0], add(values1[1], values1[73])
        assert tau != ZERO and sigma != ZERO
        tau_inverse, sigma_inverse = inverse(tau), inverse(sigma)
        z0, v0 = mul(sigma, tau_inverse), mul(tau, sigma_inverse)
        assert mul(z0, v0) == ONE
        beta = [ONE]+[mul(values1[i], tau_inverse) for i in range(2, 146)]
        beta.extend(mul(values2[i], mul(tau_inverse, tau_inverse)) for i in self.degree2)
        assert len(beta) == N
        for a in range(1, 145):
            assert mul(beta[a], tau) == values1[a+1]
        for j, i in enumerate(self.degree2):
            assert mul(beta[145+j], mul(tau, tau)) == values2[i]
        gamma = [mul(power(v0, degree), value) for degree, value in zip(EPS, beta)]
        for i in range(N):
            assert mul(power(z0, EPS[i]), gamma[i]) == beta[i]
        data = {
            'source_P0_values': self.p0_spec, 'source_V2_P0_values': self.v2_spec,
            'source_free_basis': FREE, 'degree2_original_indices': self.degree2,
            'tau_value_K_1_zeta': encode(tau), 'sigma_value_K_1_zeta': encode(sigma),
            'chart_base_values_K_1_zeta': {'tau': encode(z0), 'sigma': encode(v0)},
            'normal_basis_values_K_1_zeta': {'tau': [encode(x) for x in beta],
                                            'sigma': [encode(x) for x in gamma]},
            'normal_basis_rank': N, 'normal_basis_degrees': EPS,
            'original_P0_in_both_charts_verified': True,
            'all_original_ratio_multiply_backs_verified': True,
            'all_272_two_chart_value_transitions_verified': True,
            'original_82_scales_already_in_source': {'V1': str(82**2), 'V2': str(82**4)},
            'additional_scale_inserted': False,
        }
        ref = self.put(name, data)
        print(json.dumps({'stage': 'original_P0_normal_values', 'normal_basis_rank': N,
                          'both_original_charts': True}), flush=True)
        return self.cached(name), ref

    def cusp_column(self, chart, a):
        key = (chart, a)
        if key in self.column_cache:
            return self.column_cache[key]
        ref = self.cusp_indexes[chart]['Hermite_columns_in_original_basis_order'][a]
        value = self.sources['R820'].indexed(ref)
        out = {}
        for term in value['column_terms']:
            row, degree = term['normal_basis_row'], term['power']
            assert isinstance(row, int) and isinstance(degree, int) and 0 <= row < N and degree >= 0
            q = rational(term['coefficient'])
            assert q != 0 and (row, degree) not in out
            out[row, degree] = (q, Fraction(0))
        if a < 271:
            assert out.get((a, 0)) == ONE
            assert all((row == a and degree == 0) or (row == 271 and degree < 20) for row, degree in out)
        else:
            assert out.get((271, 20)) == ONE
            assert all(row == 271 and degree <= 20 for row, degree in out)
        self.column_cache[key] = out
        return out

    def chart_evaluation(self, chart, normal, normal_spec):
        name = 'R856-chart-'+chart+'-cusp-P0-evaluation'
        old = self.cached(name)
        if old is not None:
            assert old['original_C_index'] == self.cusp_specs[chart]
            assert old['original_normal_values'] == normal_spec and old['evaluation_row_rank'] == 1
            return old, spec(self.path(name))
        self.budget()
        x0 = decode(normal['chart_base_values_K_1_zeta'][chart])
        basis_values = [decode(x) for x in normal['normal_basis_values_K_1_zeta'][chart]]
        powers = [power(x0, n) for n in range(22)]
        values = [evaluate(self.cusp_column(chart, a), powers, basis_values) for a in range(N)]
        selected = next((a for a, value in enumerate(values) if value != ZERO), None)
        assert selected is not None, 'Original cusp ideal must not vanish identically at P0.'
        inv = inverse(values[selected])
        ratios = [mul(value, inv) for value in values]
        assert ratios[selected] == ONE
        assert all(mul(ratio, values[selected]) == value for ratio, value in zip(ratios, values))
        data = {
            'chart': chart, 'original_C_index': self.cusp_specs[chart],
            'original_normal_values': normal_spec, 'base_value_K_1_zeta': encode(x0),
            'C_column_P0_values_K_1_zeta': [encode(x) for x in values],
            'first_nonzero_column': selected, 'pivot_inverse_K_1_zeta': encode(inv),
            'ratios_to_pivot_K_1_zeta': [encode(x) for x in ratios],
            'evaluation_row_rank': 1,
            'exact_nonzero_pivot_and_inverse_multiply_back_verified': True,
            'all_ratio_multiply_backs_verified': True,
            'original_P0_disjoint_from_original_cusp_support_certified': True,
        }
        ref = self.put(name, data)
        print(json.dumps({'stage': 'cusp_P0_evaluation', 'chart': chart,
                          'actual_first_nonzero_column': selected, 'actual_rank': 1}), flush=True)
        return self.cached(name), ref

    def point_ideal(self, chart, normal, normal_spec):
        name = 'R856-chart-'+chart+'-complete-P0-ideal-basis'
        old = self.cached(name)
        if old is not None:
            assert old['source_normal_values'] == normal_spec
            assert old['complete_original_P0_evaluation_kernel_certified'] is True
            return spec(self.path(name))
        self.budget()
        x0 = decode(normal['chart_base_values_K_1_zeta'][chart])
        values = [decode(x) for x in normal['normal_basis_values_K_1_zeta'][chart]]
        powers = [ONE, x0]
        assert values[0] == ONE
        columns = []
        for a in range(N):
            if a == 0:
                column = multiply_linear({(0, 0): ONE}, x0)
            else:
                column = {(a, 0): ONE}
                add_term(column, (0, 0), neg(values[a]))
            assert evaluate(column, powers, values) == ZERO
            columns.append({'column_index': a, 'column_terms': encoded_column(column)})
        return self.put(name, {
            'chart': chart, 'source_normal_values': normal_spec, 'columns': columns,
            'normal_basis_rank': N, 'base_value_K_1_zeta': encode(x0),
            'actual_polynomial_determinant_K_1_zeta': [encode(neg(x0)), encode(ONE)],
            'actual_colength_over_K': 1,
            'all_272_original_point_evaluations_zero': True,
            'complete_original_P0_evaluation_kernel_certified': True,
            'completeness_certificate': 'original e0=1; divide the residual e0 coefficient by x-x0',
        })

    def fixed_group(self, chart, first, stop, normal, normal_spec, evaluation, evaluation_spec):
        name = 'R856-chart-'+chart+'-fixed-ideal-columns-'+f'{first:03d}-{stop:03d}'
        old = self.cached(name)
        if old is not None:
            assert old['first'] == first and old['stop'] == stop
            assert old['source_normal_values'] == normal_spec and old['source_cusp_evaluation'] == evaluation_spec
            assert old['all_source_column_multiply_backs_verified'] is True
            assert old['all_new_original_P0_evaluations_zero'] is True
            return spec(self.path(name))
        self.budget()
        x0 = decode(evaluation['base_value_K_1_zeta'])
        values = [decode(x) for x in normal['normal_basis_values_K_1_zeta'][chart]]
        powers = [power(x0, n) for n in range(22)]
        pivot = evaluation['first_nonzero_column']
        ratios = [decode(x) for x in evaluation['ratios_to_pivot_K_1_zeta']]
        pivot_column = self.cusp_column(chart, pivot)
        refs = self.cusp_indexes[chart]['Hermite_columns_in_original_basis_order']
        columns = []
        for a in range(first, stop):
            original = self.cusp_column(chart, a)
            if a == pivot:
                changed = multiply_linear(original, x0)
                transform = [{'source_C_column': a, 'power': 0, 'coefficient_K_1_zeta': encode(neg(x0))},
                             {'source_C_column': a, 'power': 1, 'coefficient_K_1_zeta': encode(ONE)}]
                # Independent coefficient recurrence for the x-x0 multiply-back.
                for row in range(N):
                    for degree in range(22):
                        expected = sub(original.get((row, degree-1), ZERO),
                                       mul(x0, original.get((row, degree), ZERO)))
                        assert changed.get((row, degree), ZERO) == expected
            else:
                changed = combine(original, pivot_column, neg(ratios[a]))
                transform = [{'source_C_column': a, 'power': 0, 'coefficient_K_1_zeta': encode(ONE)}]
                if ratios[a] != ZERO:
                    transform.append({'source_C_column': pivot, 'power': 0,
                                      'coefficient_K_1_zeta': encode(neg(ratios[a]))})
                assert combine(changed, pivot_column, ratios[a]) == original
            assert evaluate(changed, powers, values) == ZERO
            encoded = encoded_column(changed)
            assert decoded_column(encoded) == changed
            columns.append({'column_index': a, 'source_C_column': plain(refs[a]),
                            'source_C_pivot_column': plain(refs[pivot]),
                            'source_change_of_basis_terms': transform, 'column_terms': encoded})
        ref = self.put(name, {
            'chart': chart, 'first': first, 'stop': stop, 'columns': columns,
            'source_normal_values': normal_spec, 'source_cusp_evaluation': evaluation_spec,
            'original_C_index': self.cusp_specs[chart], 'pivot_column': pivot,
            'all_source_column_multiply_backs_verified': True,
            'all_new_original_P0_evaluations_zero': True,
            'complete_block_in_original_order': True,
        })
        print(json.dumps({'stage': 'fixed_ideal_columns', 'chart': chart, 'first': first, 'stop': stop}), flush=True)
        return ref

    def chart_index(self, chart, normal, normal_spec, evaluation, evaluation_spec, point_spec, groups):
        name = 'R856-chart-'+chart+'-complete-fixed-branch-ideal-index'
        old = self.cached(name)
        if old is not None:
            assert old['column_groups'] == groups and old['source_cusp_evaluation'] == evaluation_spec
            assert old['complete_fixed_branch_ideal_certified'] is True and old['actual_colength_over_K'] == 21
            return spec(self.path(name))
        self.budget()
        x0 = decode(evaluation['base_value_K_1_zeta'])
        last = self.cusp_column(chart, 271)
        source_polynomial = [last.get((271, n), ZERO) for n in range(21)]
        assert source_polynomial[-1] == ONE
        determinant = []
        for n in range(22):
            determinant.append(sub(source_polynomial[n-1] if n else ZERO,
                                   mul(x0, source_polynomial[n]) if n < 21 else ZERO))
        assert determinant[-1] == ONE
        # Horner verification that the new determinant vanishes at the same point.
        value = ZERO
        for coefficient in reversed(determinant):
            value = add(mul(value, x0), coefficient)
        assert value == ZERO
        return self.put(name, {
            'chart': chart, 'normal_basis_rank': N, 'normal_basis_degrees': EPS,
            'column_groups': groups, 'column_count': N,
            'original_C_index': self.cusp_specs[chart], 'source_normal_values': normal_spec,
            'source_cusp_evaluation': evaluation_spec, 'complete_point_ideal_basis': point_spec,
            'actual_pivot_column': evaluation['first_nonzero_column'],
            'source_C_determinant_K_1_zeta': [encode(x) for x in source_polynomial],
            'exact_change_of_basis_determinant_K_1_zeta': [encode(neg(x0)), encode(ONE)],
            'actual_polynomial_determinant_K_1_zeta': [encode(x) for x in determinant],
            'actual_colength_over_K': 21,
            'complete_fixed_branch_ideal_certified': True,
            'ideal_equals_original_C_intersect_P0': True,
            'ideal_equals_original_C_times_P0': True,
            'all_272_source_column_multiply_backs_verified': True,
            'all_272_original_P0_evaluations_zero': True,
            'completeness_certificate': 'one-row evaluation kernel in the original complete C basis; exact polynomial division',
            'determinant_certified_by_original_triangular_C_and_explicit_column_transform': True,
            'new_272_by_272_determinant_or_Hermite_computed': False,
        })

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob(PREFIX+'*.json.gz')):
            if path.name == INVENTORY:
                continue
            value = read(path)
            assert value['result'] == RESULT and value['configuration'] == self.tag and value['complete'] is True
            entries.append(spec(path))
        save(self.out/INVENTORY, {'result': RESULT, 'configuration': self.tag, 'complete': True, 'files': entries})
        return spec(self.out/INVENTORY)

    def finish(self, complete, audit=None, normal=None, indexes=None, points=None, error=None):
        indexes, points = indexes or {}, points or {}
        value = {
            'result': RESULT, 'configuration': self.tag, 'complete': complete, 'p': 41,
            'completed_scope': SCOPE if complete else 'completed_atomic_blocks_only',
            'source_audit': audit, 'original_normal_P0_values': normal,
            'two_chart_fixed_branch_ideal_indexes': indexes,
            'two_chart_point_ideal_bases': points,
            'normal_basis_rank': N, 'normal_basis_degrees': EPS,
            'actual_fixed_branch_colengths': {chart: 21 for chart in indexes},
            'actual_point_colengths': {chart: 1 for chart in points},
            'original_P0_normal_values_certified': normal is not None,
            'complete_two_chart_point_ideals_certified': len(points) == 2,
            'complete_two_chart_fixed_branch_ideals_certified': complete,
            'same_original_global_fixed_branch_ideal_on_both_charts': complete,
            'all_original_scales_and_normal_basis_orders_preserved': complete,
            'old_cusp_kernel_or_Fourier_or_primitive_arithmetic_recomputed': False,
            'new_B_or_D_normal_coordinates_computed': False,
            'new_Gamma_or_multiplication_table_computed': False,
            'actual_eta_or_height_computed': False,
            'stage_manifest': self.inventory(), 'seconds': time.monotonic()-self.started,
            'stop_reason': 'complete' if complete else 'budget', 'error': error,
        }
        save(self.out/FINAL, value)
        save(self.out/'core-receipt.json', {
            'result': RESULT, 'complete': complete, 'source_sha256': sha(__file__),
            'configuration_sha256': fingerprint(self.tag), 'certificate_sha256': sha(self.out/FINAL),
            'complete_two_chart_point_ideals_certified': len(points) == 2,
            'complete_two_chart_fixed_branch_ideals_certified': complete,
            'actual_fixed_branch_colengths': value['actual_fixed_branch_colengths'],
            'seconds': value['seconds'], 'stop_reason': value['stop_reason'], 'error': error,
            'new_B_or_D_normal_coordinates_computed': False, 'actual_eta_or_height_computed': False,
        })
        return value

    def run(self):
        audit, normal_spec, indexes, points = None, None, {}, {}
        try:
            audit = self.prepare()
            final_path = self.out/FINAL
            if final_path.exists():
                prior = read(final_path)
                assert prior['result'] == RESULT and prior['configuration'] == self.tag
                if prior['complete'] is True:
                    inventory = read(self.out/INVENTORY)
                    assert spec(self.out/INVENTORY) == prior['stage_manifest']
                    for entry in inventory['files']:
                        assert spec(self.out/entry['file']) == plain(entry)
                    return self.finish(True, prior['source_audit'], prior['original_normal_P0_values'],
                                       prior['two_chart_fixed_branch_ideal_indexes'], prior['two_chart_point_ideal_bases'])
            normal, normal_spec = self.normal_values()
            for chart in ('tau', 'sigma'):
                evaluation, evaluation_spec = self.chart_evaluation(chart, normal, normal_spec)
                points[chart] = self.point_ideal(chart, normal, normal_spec)
                groups = [self.fixed_group(chart, first, min(N, first+BATCH), normal, normal_spec,
                                           evaluation, evaluation_spec)
                          for first in range(0, N, BATCH)]
                indexes[chart] = self.chart_index(chart, normal, normal_spec, evaluation, evaluation_spec,
                                                  points[chart], groups)
            return self.finish(True, audit, normal_spec, indexes, points)
        except BudgetStop as exc:
            return self.finish(False, audit, normal_spec, indexes, points, str(exc))


def main():
    guard(); sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--budget-minutes', type=float, default=300)
    args = parser.parse_args()
    assert args.budget_minutes > 1
    started = time.monotonic()
    try:
        job = Job(args)
        final = job.run()
        print(json.dumps({'result': RESULT, 'complete': final['complete'],
                          'actual_fixed_branch_colengths': final['actual_fixed_branch_colengths'],
                          'complete_two_chart_fixed_branch_ideals_certified': final['complete_two_chart_fixed_branch_ideals_certified'],
                          'seconds': final['seconds']}, sort_keys=True), flush=True)
        return 0 if final['complete'] else 124
    except BaseException as exc:
        traceback.print_exc()
        out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
        save(out/'core-receipt.json', {'result': RESULT, 'complete': False,
            'source_sha256': sha(__file__), 'seconds': time.monotonic()-started,
            'error': type(exc).__name__+': '+str(exc), 'stop_reason': 'exception',
            'complete_two_chart_fixed_branch_ideals_certified': False,
            'actual_eta_or_height_computed': False})
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
