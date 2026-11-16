#!/usr/bin/env python3
"""Source-bound small integer and Picard-equation inputs for original Y at 7.

All arithmetic is restricted to the public repository's Actions runtime.
The old T7 matrix, factorization, CRT projectors and ideal DAGs are inputs.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import sys
import time
import traceback

REPOSITORY = 'Rogerhu12/math-research-public'
RESULT = 'R870-original-Y-rational-torsion-and-Hecke-support-inputs'
FINAL = 'p41-original-Y-rational-torsion-and-Hecke-support-inputs-certificate.json'
PREFIX = 'R870-'
LABELS = ('R865', 'GLOBAL', 'FIBRES')
BASE = ('result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256')
PROOF_KEYS = ('R870', 'R865', 'RF', 'YP')
STRATEGY = {
    'scope': 'exact_integer_torsion_bounds_and_source_bound_Picard_test_inputs',
    'original_curve': 'Y=W41; original minus3 twist of the level82 G curve',
    'p': 41, 'good_prime': 7, 'holomorphic_dimension': 127,
    'original_Hecke_operator': 'R865 genuine cyclic7-isogeny pull-push; scalar diamond7 is identity',
    'local_twist_character': 1,
    'point_field': 'Q, for the complete original norm divisors and frames',
    'torsion_test': '(T7-8)R=0 iff R is torsion in JY(Q)',
    'torsion_annihilator': 'm7(8), with m7 the actual source squarefree minimal polynomial',
    'finite_field_order': 'chi7(8)=#JY(F7)',
    'factor_annihilator': 'fi(8) on rational torsion in image of Pi(T7)',
    'integer_projector_multiple': 'retain each original di and Pi=di Ei',
    'uniform_correspondence_denominator': 'lcm of completed original di, not claimed minimal',
    'Picard_test_polynomial': '(X-8)Pi, unreduced in Z[X] to retain an actual correspondence recipe',
    'ideal_sign': 'I_Z=O(-Z), xi=-[I_Z], eta=xi/qj',
    'principal_calibration_direction': 'A/B=h O; rigidified A-to-B is c0/h; fibre scalar c0/c1',
    'all_full_Hecke_blocks_separated_only_if_all_source_multiplicities_one': True,
    'old_T7_matrix_charpoly_factorization_CRT_or_polar_ideal_recomputed': False,
    'large_opaque_producer_carriers_consumed': False,
    'budget_and_transport_excluded_from_mathematical_identity': True,
}


class BudgetStop(Exception):
    pass


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    opener = gzip.open if path.name.endswith('.gz') else open
    with opener(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    payload = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if path.name.endswith('.gz'):
        with temporary.open('wb') as raw:
            with gzip.GzipFile(filename='', fileobj=raw, mode='wb', mtime=0) as stream:
                stream.write(payload)
    else:
        temporary.write_bytes(payload)
    os.replace(temporary, path)


def plain(row):
    value = {key: row[key] for key in ('file', 'bytes', 'sha256')}
    name = PurePosixPath(value['file'])
    assert len(name.parts) == 1 and name.name not in ('', '.', '..') and '\\' not in value['file']
    assert type(value['bytes']) is int and value['bytes'] >= 0
    assert len(value['sha256']) == 64
    return value


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


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly or [0]


def ints(poly):
    return trim([int(x) for x in poly])


def write_poly(poly):
    return [str(x) for x in trim(poly)]


def add(left, right):
    output = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        output[i] += value
    for i, value in enumerate(right):
        output[i] += value
    return trim(output)


def scale(poly, value):
    return trim([value * x for x in poly])


def times_X_minus_8(poly):
    return add([0] + list(poly), scale(poly, -8))


def evaluate(poly, value=8):
    total = 0
    for coefficient in reversed(poly):
        total = total * value + coefficient
    return total


def quotient_at_8(poly):
    assert len(poly) >= 2
    quotient = [0] * (len(poly) - 1)
    quotient[-1] = poly[-1]
    for i in range(len(poly) - 2, 0, -1):
        quotient[i - 1] = poly[i] + 8 * quotient[i]
    value = poly[0] + 8 * quotient[0]
    assert add(times_X_minus_8(quotient), [value]) == trim(poly)
    assert evaluate(poly) == value
    return trim(quotient), value


def monic_divmod(numerator, denominator):
    assert denominator[-1] == 1
    remainder = trim(numerator)
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1]
        quotient[shift] += coefficient
        for i, value in enumerate(denominator):
            remainder[i + shift] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


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
        index = self.stage(self.certificate['stage_manifest'])
        stage_rows = index['stages'] if label == 'FIBRES' else index['files']
        indexed = {row['file']: plain(row) for row in stage_rows}
        assert len(indexed) == len(stage_rows)
        for name in self.files:
            if name.endswith('.json.gz') and name != self.certificate['stage_manifest']['file']:
                assert indexed[name] == self.files[name]

    def stage(self, row):
        row = plain(row)
        assert self.files[row['file']] == row
        value = read(bound(self.directory, row))
        assert value['complete'] is True and value['configuration'] == self.configuration
        assert value['result'] == self.item['result']
        return value


class Job:
    def __init__(self, config, output, budget):
        self.config, self.out = config, Path(output)
        self.started = time.monotonic()
        self.deadline = self.started + 60 * budget
        self.out.mkdir(parents=True, exist_ok=True)
        assert config['result'] == RESULT and config['core_sha256'] == sha(__file__)
        assert config['p'] == 41 and set(config['proofs_sha256']) == set(PROOF_KEYS)
        assert set(config['sources']) == set(LABELS)
        self.sources = {label: Source(label, config['sources'][label]) for label in LABELS}
        self.tag = {'result': RESULT, 'source_sha256': sha(__file__),
                    'arithmetic': 'Python_stdlib_exact_integer_and_Fraction_polynomials',
                    'p': 41, 'proofs_sha256': config['proofs_sha256'],
                    'method_sha256': config['method_sha256'],
                    'sources': {label: source_identity(config['sources'][label]) for label in LABELS},
                    'strategy': STRATEGY}
        self.inputs()

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop('Budget ended between complete original Hecke integer stages.')

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
        previous = self.load(name)
        if previous is None:
            save(self.path(name), value)
        else:
            assert previous == value
        return value

    def inputs(self):
        hecke, global_source, fibres = (self.sources[label] for label in LABELS)
        hc = hecke.certificate
        assert hc['genuine_original_Y_T7_matrix_certified'] is True
        assert hc['actual_original_Q_fixed_basis_matrix_certified'] is True
        assert hc['full560_times127_original_Hecke_equations_verified'] is True
        assert hc['exact_single_operator_spectral_projectors_certified'] is True
        assert hecke.configuration['proofs_sha256']['R865'] == self.config['proofs_sha256']['R865']
        assert hecke.configuration['strategy']['first_galois_mod41'] == 6
        assert hecke.configuration['strategy']['second_galois_mod41'] == 7
        assert hecke.configuration['strategy']['new_scale_relative_to_original_e_i_coefficients'] == [1, 1]
        self.factorization = hecke.stage(hc['characteristic_polynomial_and_factorization'])
        self.index = hecke.stage(hc['spectral_projectors'])
        assert self.index['source_factorization'] == hc['characteristic_polynomial_and_factorization']
        assert self.factorization['all_factor_products_exactly_verified'] is True
        assert self.factorization['minimal_polynomial_squarefree_from_original_Rosati_selfadjointness'] is True
        assert self.index['sum_is_identity_mod_true_minimal_polynomial_verified'] is True
        assert self.index['dimensions_sum_to_127_verified'] is True
        self.factors = self.factorization['irreducible_factors']
        self.projector_specs = self.index['projectors']
        assert len(self.factors) == len(self.projector_specs) > 0
        self.projectors = [hecke.stage(row) for row in self.projector_specs]
        for i, (factor, projector) in enumerate(zip(self.factors, self.projectors)):
            assert factor['factor_index'] == projector['factor_index'] == i
            assert projector['factor'] == factor
            assert projector['source_factorization'] == hc['characteristic_polynomial_and_factorization']
            assert projector['exact_Bezout_idempotence_and_all_factor_residues_verified'] is True
        self.chi = ints(self.factorization['characteristic_polynomial_ascending'])
        self.minimal = ints(self.factorization['minimal_polynomial_ascending'])
        assert len(self.chi) == 128 and self.chi[-1] == self.minimal[-1] == 1
        assert sum(row['degree'] * row['multiplicity'] for row in self.factors) == 127
        gc, fc = global_source.certificate, fibres.certificate
        assert gc['original_eta_Picard_input_DAGs_defined'] is True
        assert fc['all_five_original_rigidified_Poincare_fibres_constructed'] is True
        assert fc['original_full_Picard_correction_and_theta_torsion_transport_preserved'] is True
        assert fibres.configuration['proof_sha256'] == self.config['proofs_sha256']['RF']
        for key in BASE:
            assert fibres.configuration['source_identities']['GLOBAL'][key] == global_source.item[key]
        assert fibres.configuration['source_identities']['GLOBAL']['configuration_sha256'] == \
               global_source.item['configuration_sha256']
        self.global_program = global_source.stage(gc['exact_expression_DAG'])
        self.fibre_program = fibres.stage(fc['exact_expression_DAG'])
        assert plain(self.fibre_program['original_global_program']) == plain(gc['exact_expression_DAG'])
        global_nodes = {row['id']: row for row in self.global_program['graph_nodes']}
        fibre_nodes = {row['id']: row for row in self.fibre_program['graph_nodes']}
        self.original_points = []
        global_outputs = self.global_program['five_original_polar_and_eta_outputs']
        fibre_outputs = self.fibre_program['five_original_fibre_and_section_outputs']
        assert len(global_outputs) == len(fibre_outputs) == 5
        for j, rf in enumerate(fibre_outputs, 1):
            gp = global_outputs[str(j)]
            assert rf['j'] == j and (rf['p'], rf['q']) == (gp['p'], gp['q'])
            assert gp['source_original_hj_index'] == j
            assert gp['eta_Picard_class']['sign'] == -1
            assert gp['eta_Picard_class']['rational_denominator'] == gp['q']
            assert gp['eta_Picard_class']['ideal_nodes'] == gp['eta_degree_zero_fractional_ideal']
            for node in gp['eta_degree_zero_fractional_ideal'].values():
                assert node in global_nodes
            original_ideal = fibre_nodes[rf['original_ideal']]
            xi = fibre_nodes[rf['xi']]
            vector = fibre_nodes[rf['Poincare_v']]
            assert original_ideal['operation'] == 'original_two_chart_invertible_sheaf'
            assert original_ideal['data']['convention'] == 'O_Y(-Z_j)'
            assert plain(original_ideal['data']['global_transition_source']) == gc['exact_expression_DAG']
            assert xi['operation'] == 'negative_of_ideal_Picard_class'
            assert xi['inputs'] == [rf['original_ideal']]
            assert vector['data']['actual_Q_fibre'] is True
            assert rf['c0_order_Z'] == -7 * (gp['p'] - gp['q'])
            self.original_points.append({
                'j': j, 'p_j': gp['p'], 'q_j': gp['q'],
                'xi_sign_relative_to_I_Z': -1,
                'eta_equals_xi_divided_by_q_j': True,
                'original_global_program': {'source_group': 'GLOBAL', **gc['exact_expression_DAG']},
                'two_chart_I_Z_nodes': gp['eta_degree_zero_fractional_ideal'],
                'original_fibre_program': {'source_group': 'FIBRES', **fc['exact_expression_DAG']},
                'original_I_Z_line_node': rf['original_ideal'], 'original_integral_xi_node': rf['xi'],
                'original_Poincare_vector_node': rf['Poincare_v'],
                'c0_frame': {'parameter': 't=a^3', 'power': rf['c0_order_Z']},
                'c1_frame': '1', 'point_field': 'Q',
                'Q_Cartier_descent_proof': {'proof': 'R870.1; RF section5',
                                          'sha256': self.config['proofs_sha256']['R870']},
                'real_descent_ideal_not_substituted': True})
        name = 'source-audit'
        if self.load(name) is None:
            self.put(name, {
                'source_identities': self.tag['sources'],
                'source_factorization': {'source_group': 'R865', **hc['characteristic_polynomial_and_factorization']},
                'source_projector_index': {'source_group': 'R865', **hc['spectral_projectors']},
                'original_five_integral_Picard_inputs': self.original_points,
                'all_selected_original_source_bytes_and_stage_tags_verified': True,
                'no_old_matrix_factorization_CRT_norm_or_polar_ideal_recomputed': True,
                'large_carrier_materialized_or_claimed_hashed': False})

    def integers(self):
        name = 'universal-rational-torsion-integer'
        if self.load(name) is None:
            self.budget()
            quotient, N = quotient_at_8(self.minimal)
            full = evaluate(self.chi)
            assert N > 0 and full > 0
            source = self.sources['R865'].certificate['characteristic_polynomial_and_factorization']
            self.put(name, {
                'source_audit': self.ref('source-audit'),
                'source_factorization': {'source_group': 'R865', **source},
                'good_prime': 7, 'evaluation_point': 8,
                'minimal_polynomial_ascending': write_poly(self.minimal),
                'quotient_Q0_ascending': write_poly(quotient),
                'torsion_annihilator_N0': str(N),
                'finite_field_Jacobian_order': str(full),
                'identity': 'm7(X)=(X-8)Q0(X)+N0',
                'identity_all_coefficients_exactly_verified': True,
                'kills_all_original_JY_Q_torsion_including_7_primary': True,
                'N0_can_clear_actual_YP_f_minus_d_torsion_after_e_eta_identified': True,
                'original_active_eta_support_or_principal_function_computed': False})
        universal = self.load(name)
        N = int(universal['torsion_annihilator_N0'])
        full = int(universal['finite_field_Jacobian_order'])
        n_product = full_product = 1
        for i, (factor, projector) in enumerate(zip(self.factors, self.projectors)):
            name = 'factor-%03d-torsion-and-Picard-test' % i
            if self.load(name) is None:
                self.budget()
                f = ints(factor['polynomial_ascending'])
                quotient, n = quotient_at_8(f)
                assert n > 0 and len(f) == factor['degree'] + 1 and f[-1] == 1
                d = int(projector['integer_multiple'])
                P = ints(projector['integral_correspondence_polynomial'])
                assert d > 0
                e = [Fraction(int(x[0]), int(x[1])) for x in projector['projector_polynomial']]
                assert trim([d * x for x in e]) == P
                A = times_X_minus_8(P)
                # New certificate of the exact factor annihilator on this integral image.
                relation, remainder = monic_divmod(multiply(f, P), self.minimal)
                assert remainder == [0]
                assert multiply(self.minimal, relation) == multiply(f, P)
                self.put(name, {
                    'source_projector': {'source_group': 'R865', **self.projector_specs[i]},
                    'source_universal_integer': self.ref('universal-rational-torsion-integer'),
                    'factor_index': i, 'factor': factor,
                    'source_integral_projector_multiple': str(d),
                    'source_integral_correspondence_polynomial_ascending': write_poly(P),
                    'factor_value_n_i': str(n), 'quotient_Qi_ascending': write_poly(quotient),
                    'factor_division_identity_all_coefficients_verified': True,
                    'factor_times_Pi_equals_minimal_times_relation_quotient': write_poly(relation),
                    'factor_annihilates_original_integral_projector_image_certified': True,
                    'Picard_test_polynomial_ascending': write_poly(A),
                    'Picard_test_polynomial_not_reduced_mod_minimal': True,
                    'alternative_integer_test_multiple': str(n),
                    'zero_test_equivalence': 'Ei(T)eta_j=0 in Q tensor iff Ai(T)xi_j=0 iff ni Pi(T)xi_j=0',
                    'actual_isotypic_block_separated_by_source_multiplicity_one': factor['multiplicity'] == 1,
                    'actual_eta_projection_zero_decisions': [None] * 5,
                    'actual_norm_RR_or_principal_function_computed': False})
            current = self.load(name)
            n_product *= int(current['factor_value_n_i'])
            full_product *= int(current['factor_value_n_i']) ** factor['multiplicity']
        assert n_product == N and full_product == full

    def denominator_and_plan(self):
        name = 'uniform-integer-correspondence-denominator'
        if self.load(name) is None:
            self.budget()
            d = 1
            for row in self.projectors:
                d = math.lcm(d, int(row['integer_multiple']))
            assert d > 0
            rows = []
            for i, row in enumerate(self.projectors):
                di = int(row['integer_multiple'])
                assert d % di == 0
                P = ints(row['integral_correspondence_polynomial'])
                rows.append({'factor_index': i, 'original_di': str(di),
                             'integer_scalar_d_over_di': str(d // di),
                             'common_denominator_correspondence_polynomial_ascending': write_poly(scale(P, d // di)),
                             'source_projector': {'source_group': 'R865', **self.projector_specs[i]}})
            self.put(name, {
                'source_audit': self.ref('source-audit'), 'uniform_denominator_d_star': str(d),
                'integral_spectral_correspondences': rows,
                'every_d_star_Ei_coefficient_integral_verified': True,
                'denominator_is_lcm_of_actual_completed_source_denominators': True,
                'denominator_minimality_claimed': False, 'R862_A_projector_not_used': True,
                'actual_YP_e_eta_or_its_specific_d_selected': False})
        name = 'original-five-Picard-test-and-calibration-plan'
        if self.load(name) is None:
            self.budget()
            equations = []
            for i in range(len(self.factors)):
                for point in self.original_points:
                    equations.append({
                        'factor_index': i, 'j': point['j'],
                        'integer_test_source': self.ref('factor-%03d-torsion-and-Picard-test' % i),
                        'original_Picard_input': point,
                        'operator': 'H(L)=Nm_target(source_pullback L) on original cyclic7 correspondence',
                        'ideal_recipe': 'tensor over r of H^r(I_Zj) to integral Ai coefficient ar',
                        'ideal_Picard_class': '-Ai(T7)xi_j',
                        'degree': 0, 'required_complete_RR_dimension': '0_or_1',
                        'is_zero_iff_complete_RR_dimension_one': True,
                        'actual_complete_RR_dimension': None,
                        'actual_principal_generator': None})
            all_separated = all(row['multiplicity'] == 1 for row in self.factors)
            self.put(name, {
                'source_audit': self.ref('source-audit'),
                'source_universal_integer': self.ref('universal-rational-torsion-integer'),
                'source_uniform_denominator': self.ref('uniform-integer-correspondence-denominator'),
                'original_five_integral_Picard_inputs': self.original_points,
                'exact_Picard_equation_plans': equations,
                'actual_single_T7_factor_count': len(self.factors),
                'actual_all_T7_blocks_isotypically_separated': all_separated,
                'isotypic_separation_reason': 'R870 section7 and the actual factor multiplicities',
                'active_factor_indices': None,
                'rigidified_principal_transport': {
                    'identity': 'A tensor B_inverse = h O',
                    'local_scalar': 'cnu=(h/(eA_nu/eB_nu))(Pnu)',
                    'A_to_B_zero_rigidification': 'multiply by c0/h',
                    'P1_fibre_scalar': 'c0/c1',
                    'original_RF_example': 'kappa_j/R_j(P1)',
                    'principal_function_source': None},
                'all_large_ideal_sources_only_referenced_not_evaluated': True,
                'actual_eta_active_support_computed': False,
                'actual_YP_e_eta_selected': False,
                'actual_principal_comparison_functions_computed': False,
                'actual_non_p_local_heights_computed': False,
                'actual_original_height_computed': False})

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
        inventory = {'result': RESULT, 'configuration': self.tag, 'complete': True,
                     'files': files, 'actual_complete_stage_count': len(files)}
        if manifest_path.exists():
            assert read(manifest_path) == inventory
        else:
            save(manifest_path, inventory)
        current = self.out / (PREFIX + 'current.json.gz')
        save(current, {'result': RESULT, 'configuration': self.tag, 'complete': False,
                       'scope_complete': complete, 'stop_reason': reason,
                       'actual_stage_manifest': spec(manifest_path)})
        refs = {}
        for key, name in (
            ('source_audit', 'source-audit'),
            ('universal_rational_torsion_integer', 'universal-rational-torsion-integer'),
            ('uniform_integer_correspondence_denominator', 'uniform-integer-correspondence-denominator'),
            ('original_Picard_equation_and_calibration_plan', 'original-five-Picard-test-and-calibration-plan')):
            refs[key] = self.ref(name) if self.path(name).exists() else None
        factor_refs = [self.ref('factor-%03d-torsion-and-Picard-test' % i) for i in range(len(self.factors))
                       if self.path('factor-%03d-torsion-and-Picard-test' % i).exists()]
        if complete:
            assert all(refs.values()) and len(factor_refs) == len(self.factors)
        universal = self.load('universal-rational-torsion-integer')
        denominator = self.load('uniform-integer-correspondence-denominator')
        plan = self.load('original-five-Picard-test-and-calibration-plan')
        cert = {'result': RESULT, 'configuration': self.tag, 'complete': complete, 'p': 41, **refs,
                'factor_torsion_and_Picard_test_certificates': factor_refs,
                'rational_torsion_annihilator_N0': None if universal is None else universal['torsion_annihilator_N0'],
                'finite_field_Jacobian_order': None if universal is None else universal['finite_field_Jacobian_order'],
                'uniform_spectral_integer_denominator_d_star': None if denominator is None else
                    denominator['uniform_denominator_d_star'],
                'rational_torsion_annihilator_certified': complete,
                'T7_minus_8_exact_torsion_test_certified': complete,
                'uniform_spectral_integer_correspondence_denominator_certified': complete,
                'actual_all_T7_blocks_isotypically_separated': False if plan is None else
                    plan['actual_all_T7_blocks_isotypically_separated'],
                'actual_factor_count': len(self.factors),
                'actual_five_integral_Picard_inputs_bound': 5,
                'actual_Picard_equation_plan_count': 0 if plan is None else len(plan['exact_Picard_equation_plans']),
                'stage_manifest': spec(manifest_path), 'resume_state': spec(current),
                'old_matrix_factorization_CRT_ideal_or_fibre_arithmetic_recomputed': False,
                'actual_eta_active_support_computed': False, 'actual_YP_e_eta_selected': False,
                'actual_YP_specific_d_selected': False,
                'actual_principal_comparison_functions_computed': False,
                'actual_non_p_local_heights_computed': False,
                'actual_original_height_computed': False, 'actual_height_nonzero_proved': False,
                'stop_reason': reason, 'seconds': time.monotonic() - self.started}
        save(self.out / FINAL, cert)
        return cert

    def run(self):
        final_path = self.out / FINAL
        if final_path.exists():
            old = read(final_path)
            assert old['result'] == RESULT and old['configuration'] == self.tag
            if old['complete']:
                for row in read(bound(self.out, old['stage_manifest']))['files']:
                    bound(self.out, row)
                return old
        self.integers()
        self.denominator_and_plan()
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
               'process_exit_code': code, 'error': error,
               'configuration': None if job is None else job.tag,
               'certificate_sha256': sha(args.output / FINAL) if final is not None else None,
               'seconds': time.monotonic() - started}
    save(args.output / 'core-receipt.json', receipt)
    print('R870_CORE_RECEIPT=' + json.dumps(receipt, sort_keys=True), flush=True)
    if final is not None:
        keys = ('complete', 'rational_torsion_annihilator_N0', 'finite_field_Jacobian_order',
                'uniform_spectral_integer_denominator_d_star', 'actual_factor_count',
                'actual_all_T7_blocks_isotypically_separated', 'seconds')
        print('R870_RESULT=' + json.dumps({key: final[key] for key in keys}, sort_keys=True), flush=True)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
