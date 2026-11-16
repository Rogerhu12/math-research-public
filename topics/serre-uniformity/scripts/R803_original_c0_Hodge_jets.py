#!/usr/bin/env python3
"""Original c0 first jets and comparison leading coefficients, only in Actions."""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

RESULT = 'R803-original-c0-Hodge-jets-and-comparison-leading-coefficients'
FINAL = 'p41-original-c0-Hodge-jets-and-comparison-leading-coefficients-certificate.json'
PREFIX = 'R803-c0-'
FIELD_BASIS = 'b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b'
K_BASIS = ['1', 's=1+2*zeta; s^2=-3']
LABELS = ['R803', 'R837', 'R791']
BASE = ['result', 'run_id', 'source_commit', 'core_sha256', 'manifest_sha256',
        'configuration_sha256', 'certificate_name', 'selected_files_sha256']
EXTRA = {
    690: {'kind': 'elliptic_layer_product', 'factor': 'E4', 'power': 1, 'index': 0},
    691: {'kind': 'elliptic_layer_product', 'factor': 'E4', 'power': 1, 'index': 73},
    692: {'kind': 'level_one', 'name': 'E6'},
    693: {'kind': 'level_one', 'name': 'eta12'},
}
SCOPE = {
    'p': 41, 'original_point_on_X': 'c0', 'original_point_on_Y': 'P0=phi(c0)',
    'original_coarse_parameter': 't=a^3', 'first_jet_order': 1,
    'original_target': 'C:y^2=x^3+b; omega_C=dx/(2*y)',
    'M6_dimension': 694, 'original_M6_integer_scale': '304006671424',
    'original_regular_Phi_integer_scale': '6724',
    'original_M6_rows_used': [690, 691, 692, 693],
    'original_Phi_indices_used': [0, 73],
    'original_U_indices': [0, 1, 2, 3, 4, 5],
    'coefficient_field_basis': FIELD_BASIS,
    'relative_norm_degree': 7, 'relative_norm_target_basis': K_BASIS,
    'comparison_indices': [1, 2, 3, 4, 5],
    'leading_constants_representation': 'exact integer-power DAG of actual original norms',
    'no_cubic_root_chosen': True,
    'no_global_A_B_or_Fourier_or_period_or_CM_torsion_recomputed': True,
}


class BudgetStop(Exception):
    pass


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == '.gz' else open)(path, 'rt', encoding='utf-8') as stream:
        return json.load(stream)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.tmp')
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if path.suffix == '.gz':
        with temporary.open('wb') as stream:
            with gzip.GzipFile(fileobj=stream, mode='wb', mtime=0, compresslevel=2) as compressed:
                compressed.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def plain(value):
    return {key: value[key] for key in ('file', 'bytes', 'sha256')}


def file_spec(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path)}


def rational(value):
    assert isinstance(value, (list, tuple)) and len(value) == 2
    return Fraction(int(value[0]), int(value[1]))


def pair(value):
    value = Fraction(value)
    return [str(value.numerator), str(value.denominator)]


def source_identity(value):
    answer = {key: value[key] for key in BASE}
    answer['files'] = {name: plain(spec) for name, spec in sorted(value['files'].items())}
    return answer


class Source:
    def __init__(self, label, spec):
        self.label, self.item = label, spec
        self.root = Path(spec['directory'])
        self.files = {name: plain(value) for name, value in spec['files'].items()}
        assert fingerprint([self.files[name] for name in sorted(self.files)]) == spec['selected_files_sha256']
        for name, value in self.files.items():
            assert Path(name).name == name and name == value['file']
            assert file_spec(self.root/name) == value
        manifest = read(self.root/'full-outputs-manifest.json')
        assert self.files['full-outputs-manifest.json']['sha256'] == spec['manifest_sha256']
        assert manifest['result'] == spec['result']
        self.inventory = {row['file']: plain(row) for row in manifest['files']}
        assert len(self.inventory) == len(manifest['files'])
        for name, value in self.files.items():
            if name != 'full-outputs-manifest.json':
                assert self.inventory[name] == value
        initial = read(self.root/'public-actions-input.json')
        run = read(self.root/'run-receipt.json')
        core = read(self.root/'core-receipt.json')
        assert run['source_commit'] == initial['source_commit'] == spec['source_commit']
        assert str(run['workflow_run_id']) == str(spec['run_id'])
        assert run['process_exit_code'] == 0 and run['complete'] is True
        assert core['complete'] is True and core['source_sha256'] == spec['core_sha256']
        if label == 'R791':
            assert initial['job']['core_sha256'] == spec['core_sha256']
            assert 'core_receipt_sha256' not in run and 'core_sha256' not in initial
        else:
            assert initial['core_sha256'] == spec['core_sha256']
            assert run['core_receipt_sha256'] == self.files['core-receipt.json']['sha256']
        self.certificate = read(self.root/spec['certificate_name'])
        assert self.certificate['result'] == spec['result'] and self.certificate['complete'] is True
        assert core['certificate_sha256'] == self.files[spec['certificate_name']]['sha256']
        self.tag = self.certificate['configuration']
        assert self.tag['result'] == spec['result'] and self.tag['source_sha256'] == spec['core_sha256']
        assert fingerprint(self.tag) == spec['configuration_sha256']

    def get(self, name):
        assert name in self.files
        value = read(self.root/name)
        assert value['complete'] is True and value['configuration'] == self.tag
        if 'result' in value:
            assert value['result'] == self.item['result']
        return value

    def indexed(self, spec):
        assert plain(spec) == self.files[spec['file']]
        return self.get(spec['file'])

    def ref(self, name):
        return dict(self.files[name], producer=self.label)


def trim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return poly


def poly_add(a, b):
    answer = [Fraction(0)]*max(len(a), len(b))
    for j, value in enumerate(a):
        answer[j] += value
    for j, value in enumerate(b):
        answer[j] += value
    return trim(answer)


def poly_sub(a, b):
    return poly_add(a, [-value for value in b])


def poly_mul(a, b):
    if not a or not b:
        return []
    answer = [Fraction(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i+j] += x*y
    return trim(answer)


def poly_divmod(a, b):
    a, b = trim(a), trim(b)
    assert b
    quotient = [Fraction(0)]*max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        shift = len(a)-len(b)
        value = a[-1]/b[-1]
        quotient[shift] += value
        for i, x in enumerate(b):
            a[i+shift] -= value*x
        a = trim(a)
    return trim(quotient), a


class OriginalField:
    """The unaltered field Q(b,s), b from R803, s^2=-3; rational exact arithmetic."""
    def __init__(self, model):
        assert set(model) == {'numerator', 'denominator'}
        self.model = model
        denominator = int(model['denominator'])
        self.polynomial = tuple(Fraction(int(value), denominator) for value in model['numerator'])
        assert len(self.polynomial) == 8 and self.polynomial[-1] == 1
        self.zero = (Fraction(0),)*14
        self.one = self.scalar(1)
        self.s = self.embed_K((Fraction(0), Fraction(1)))
        self.inverse_cache = {}

    def scalar(self, value):
        return (Fraction(value),)+(Fraction(0),)*13

    def embed_K(self, value):
        a, b = value
        return (Fraction(a),)+(Fraction(0),)*6+(Fraction(b),)+(Fraction(0),)*6

    def decode(self, rows):
        assert len(rows) == 14
        return tuple(rational(value) for value in rows)

    def encode(self, value):
        assert len(value) == 14
        return [pair(x) for x in value]

    def f_reduce(self, value):
        _, remainder = poly_divmod(value, self.polynomial)
        return tuple(remainder+[Fraction(0)]*(7-len(remainder)))

    def f_mul(self, a, b):
        return self.f_reduce(poly_mul(a, b))

    def f_inverse(self, value):
        r0, r1 = list(self.polynomial), trim(value)
        assert r1
        t0, t1 = [], [Fraction(1)]
        while r1:
            quotient, remainder = poly_divmod(r0, r1)
            r0, r1 = r1, remainder
            t0, t1 = t1, poly_sub(t0, poly_mul(quotient, t1))
        assert len(r0) == 1 and r0[0]
        answer = self.f_reduce([x/r0[0] for x in t0])
        assert self.f_mul(value, answer) == (Fraction(1),)+(Fraction(0),)*6
        return answer

    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x-y for x, y in zip(a, b))

    def scale(self, a, c):
        return tuple(Fraction(c)*x for x in a)

    def mul(self, a, b):
        aa, ab = a[:7], a[7:]
        ba, bb = b[:7], b[7:]
        ac, bd = self.f_mul(aa, ba), self.f_mul(ab, bb)
        ad, bc = self.f_mul(aa, bb), self.f_mul(ab, ba)
        return tuple(x-3*y for x, y in zip(ac, bd))+tuple(x+y for x, y in zip(ad, bc))

    def inverse(self, a):
        assert a != self.zero
        if a in self.inverse_cache:
            return self.inverse_cache[a]
        aa, ab = a[:7], a[7:]
        x, y = self.f_mul(aa, aa), self.f_mul(ab, ab)
        denominator = tuple(u+3*v for u, v in zip(x, y))
        inverse = self.f_inverse(denominator)
        answer = self.f_mul(aa, inverse)+tuple(-x for x in self.f_mul(ab, inverse))
        assert self.mul(a, answer) == self.one
        self.inverse_cache[a] = answer
        return answer

    def div(self, a, b):
        answer = self.mul(a, self.inverse(b))
        assert self.mul(answer, b) == a
        return answer

    def power(self, a, exponent):
        if exponent < 0:
            a, exponent = self.inverse(a), -exponent
        answer = self.one
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, a)
            exponent //= 2
            if exponent:
                a = self.mul(a, a)
        return answer

    def multiplication_matrix_over_K(self, value):
        columns = []
        for j in range(7):
            e = [Fraction(0)]*14
            e[j] = Fraction(1)
            product = self.mul(value, tuple(e))
            columns.append([(product[i], product[i+7]) for i in range(7)])
        return [[columns[j][i] for j in range(7)] for i in range(7)]


KZERO = (Fraction(0), Fraction(0))
KONE = (Fraction(1), Fraction(0))


def k_add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def k_sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def k_scale(a, value):
    return (Fraction(value)*a[0], Fraction(value)*a[1])


def k_mul(a, b):
    return (a[0]*b[0]-3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def k_inverse(value):
    assert value != KZERO
    denominator = value[0]*value[0]+3*value[1]*value[1]
    answer = (value[0]/denominator, -value[1]/denominator)
    assert k_mul(value, answer) == KONE
    return answer


def k_encode(value):
    return [pair(x) for x in value]


def k_decode(value):
    assert len(value) == 2
    return tuple(rational(x) for x in value)


def k_matrix_encode(matrix):
    return [[k_encode(value) for value in row] for row in matrix]


def k_determinant(matrix):
    a = [list(row) for row in matrix]
    assert len(a) == 7 and all(len(row) == 7 for row in a)
    answer, steps = KONE, []
    for k in range(7):
        pivot_row = next((i for i in range(k, 7) if a[i][k] != KZERO), None)
        assert pivot_row is not None, 'Norm input unexpectedly zero.'
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            answer = k_scale(answer, -1)
        pivot = a[k][k]
        inverse = k_inverse(pivot)
        answer = k_mul(answer, pivot)
        for i in range(k+1, 7):
            multiplier = k_mul(a[i][k], inverse)
            for j in range(k, 7):
                a[i][j] = k_sub(a[i][j], k_mul(multiplier, a[k][j]))
            assert a[i][k] == KZERO
        steps.append({'column': k, 'pivot_row_before_swap': pivot_row,
                      'pivot_K': k_encode(pivot), 'pivot_inverse_verified': True})
    return answer, steps


class Job:
    def __init__(self, args):
        self.args = args
        self.started = time.monotonic()
        self.item = read(args.config)
        self.out = args.out
        self.out.mkdir(parents=True, exist_ok=True)
        self.limit = float(args.budget_minutes)*60
        assert self.item['result'] == RESULT and self.item['p'] == 41
        assert self.item['producer_inputs_pending'] is False
        assert sha(__file__) == self.item['core_sha256']
        for key in ('proof', 'method'):
            assert sha(self.item[key+'_absolute_path']) == self.item[key+'_sha256']
        assert set(self.item['sources']) == set(LABELS)
        self.sources = {name: Source(name, self.item['sources'][name]) for name in LABELS}
        self.tag = {'result': RESULT, 'source_sha256': sha(__file__),
                    'arithmetic': 'Python exact Fraction, original Q(b,s) quotient and K determinant',
                    'proof_sha256': self.item['proof_sha256'],
                    'method_sha256': self.item['method_sha256'],
                    'sources': {name: source_identity(self.item['sources'][name]) for name in LABELS},
                    **SCOPE}
        self.r803, self.r837, self.r791 = (self.sources[name] for name in LABELS)
        self.c803 = self.r803.certificate
        assert self.c803['M6_dimension'] == 694 and self.c803['full_original_coordinate_rows'] == 1680
        assert self.c803['basis_integer_scale'] == '304006671424'
        assert self.c803['all84_rational_RHS_columns_verified_in_all1680_original_rows'] is True
        assert self.c803['all_original_1722_and_82power6_scales_preserved'] is True
        self.index = self.r803.indexed(self.c803['basis_index'])
        assert self.index['integer_scale'] == '304006671424'
        assert self.index['original_basis_order_and_recipes_preserved'] is True
        assert len(self.index['basis_rows']) == 694
        for j, row in enumerate(self.index['basis_rows']):
            assert row['index'] == j
            if j < 690:
                assert row['recipe'] == {'kind': 'power_basis', 'power': 3, 'index': j}
            else:
                assert row['recipe'] == EXTRA[j]
                extra = self.r803.indexed(row['source'])
                assert extra['recipe'] == EXTRA[j] and extra['integer_scale'] == '304006671424'
        self.ratios = self.r803.indexed(self.c803['ratio_interface'])
        assert self.ratios['coordinate_stages'] == self.c803['coordinate_stages']
        assert self.ratios['all_six_exact_forms_identified_by_full42_term_injective_prefix'] is True
        mixed = self.r803.get('R803-mixed-original-Hodge-scalars-j1.json.gz')
        assert mixed['mixed_formula'] == '4*w_j*v_f*v_f/1722^3; exact mixed multiplicities; s^2=-3'
        assert mixed['extra_rho_j_or_c1_phase_applied'] is False
        self.field = OriginalField(mixed['original_b_model'])
        self.p0 = self.r837.indexed(self.r837.certificate['original_P0_evaluation'])
        assert self.p0['original_target_point'] == 'P0=phi(c0)'
        assert self.p0['original_frame'] == 'Phi_i=(82**2*T_i)*E6/E4**2, same frame at P0 and P1'
        assert self.p0['integer_scale_already_in_source'] == '6724'
        assert self.p0['additional_scale_inserted'] is False
        assert self.p0['all_146_reflected_outputs_verified'] is True
        assert self.p0['both_exact_dual_systems_multiplied_back'] is True
        self.eta = self.r791.get('R791-original-real-descent-and-eta-basis-inputs.json.gz')
        assert self.eta['all_original_F0_directions_covered'] is True
        assert [row['j'] for row in self.eta['degree_zero_basis']] == [1, 2, 3, 4, 5]
        self.pq = []
        for row in self.eta['degree_zero_basis']:
            original_ratio = rational(row['degree_zero_coefficient_dj_over_d0'])
            degree_ratio = 2+original_ratio
            p, q = degree_ratio.numerator, degree_ratio.denominator
            assert p > 0 and q > 0
            self.pq.append((p, q))

    def budget(self):
        if time.monotonic()-self.started >= self.limit:
            raise BudgetStop('Original c0 calculation reached its budget between atomic stages.')

    def path(self, name):
        if not name.endswith('.json.gz'):
            name += '.json.gz'
        assert name.startswith(PREFIX) and Path(name).name == name
        return self.out/name

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value['configuration'] == self.tag and value['result'] == RESULT
        assert value['complete'] is True
        return value

    def store(self, name, value):
        assert self.cached(name) is None
        save(self.path(name), dict(value, result=RESULT, configuration=self.tag, complete=True))
        return file_spec(self.path(name))

    def source_audit(self):
        name = PREFIX+'original-source-audit'
        if self.cached(name) is None:
            self.budget()
            self.store(name, {'source_identities': self.tag['sources'],
                'original_M6_basis_index': self.r803.ref(self.c803['basis_index']['file']),
                'original_Hodge_ratio_interface': self.r803.ref(self.c803['ratio_interface']['file']),
                'original_b_model_source': self.r803.ref('R803-mixed-original-Hodge-scalars-j1.json.gz'),
                'original_b_model': self.field.model,
                'original_P0_evaluation': self.r837.ref(self.r837.certificate['original_P0_evaluation']['file']),
                'original_eta_normalization': self.r791.ref('R791-original-real-descent-and-eta-basis-inputs.json.gz'),
                'original_pq': [{'j': j+1, 'p': p, 'q': q} for j, (p, q) in enumerate(self.pq)],
                'all_selected_original_source_bytes_SHA_and_configuration_verified': True,
                'original_1722_and_82_power_scales_preserved': True,
                'unscaled_original_M6_coordinates_used_without_rescaling': True,
                'new_field_or_target_or_Hom_normalization_introduced': False})
        return file_spec(self.path(name))

    def phi_value(self, index):
        assert self.p0['coefficient_basis'] == ['1', 'zeta=(-1+sqrt(-3))/2']
        values = self.p0['P0_values_K_1_zeta'][index]
        assert len(values) == 2
        a, b = (rational(value) for value in values)
        return self.field.embed_K((a-b/2, b/2))

    def V_jet(self, j):
        name = PREFIX+'U-over-E6-first-jet-j'+str(j)
        old = self.cached(name)
        if old is None:
            self.budget()
            f = self.field
            spec = self.c803['coordinate_stages'][str(j)]
            source = self.r803.indexed(spec)
            assert source['j'] == j and source['basis_dimension'] == 694
            assert source['basis_integer_scale'] == '304006671424'
            assert source['coefficient_field_basis'] == FIELD_BASIS
            assert source['all1680_original_coordinates_verified'] is True
            rows = source['coefficients_in_unscaled_original_M6_basis']
            assert len(rows) == 694 and all(len(row) == 14 for row in rows)
            a690, a691, a692, a693 = (f.decode(rows[k]) for k in (690, 691, 692, 693))
            phi0, phi73 = self.phi_value(0), self.phi_value(73)
            inverse_s = f.inverse(f.s)
            e0, e1 = f.scale(inverse_s, Fraction(-1, 24)), f.scale(inverse_s, Fraction(-1, 12))
            value = f.add(a692, f.mul(a693, e0))
            derivative = f.add(f.scale(f.add(f.mul(a690, phi0), f.mul(a691, phi73)), Fraction(-4, 6724)),
                               f.mul(a693, e1))
            assert value != f.zero, 'The original U_j/E6 value unexpectedly vanishes at c0.'
            self.store(name, {'j': j, 'function': 'V_'+str(j)+'=U_'+str(j)+'/E6',
                'parameter': 't=a^3', 'point': 't=0=P0',
                'source_coordinates': self.r803.ref(spec['file']),
                'source_M6_basis_index': self.r803.ref(self.c803['basis_index']['file']),
                'source_P0_evaluation': self.r837.ref(self.r837.certificate['original_P0_evaluation']['file']),
                'original_four_unscaled_M6_coordinate_rows': {str(k): rows[k] for k in (690, 691, 692, 693)},
                'original_Phi_values_in_K_1_s': {'0': k_encode((phi0[0], phi0[7])),
                                               '73': k_encode((phi73[0], phi73[7]))},
                'R_value_and_derivative': [pair(0), pair(-4)],
                'eta12_over_E6_value_K': k_encode((e0[0], e0[7])),
                'eta12_over_E6_derivative_K': k_encode((e1[0], e1[7])),
                'value_L': f.encode(value), 'derivative_t_L': f.encode(derivative),
                'actual_value_nonzero': True,
                'ordinary_690_basis_rows_have_factor_R_squared': True,
                'no_Phi_derivative_needed_at_this_order': True,
                'no_extra_82_power_or_1722_power_inserted': True,
                'old_Fourier_Hodge_products_or_CM_evaluations_recomputed': False})
            del source
            old = self.cached(name)
        return self.field.decode(old['value_L']), self.field.decode(old['derivative_t_L']), file_spec(self.path(name))

    def W_jet(self, j):
        name = PREFIX+'W-and-lambda-cube-first-jet-j'+str(j)
        old = self.cached(name)
        if old is None:
            self.budget()
            f = self.field
            v0, d0, ref0 = self.V_jet(0)
            original_base_logarithmic = f.div(d0, v0)
            if j == 0:
                w, dw, ratio, dratio = v0, d0, f.one, f.zero
                logarithmic = original_base_logarithmic
                refs = [ref0]
                expression = 'W_0=V_0'
            else:
                vj, dj, refj = self.V_jet(j)
                numerator, dnumerator = f.add(v0, vj), f.add(d0, dj)
                assert numerator != f.zero, 'The actual nonzero Hom f+T^j f has zero c0 tangent.'
                ratio = f.div(numerator, v0)
                dratio = f.sub(f.div(dnumerator, v0), f.mul(ratio, original_base_logarithmic))
                w = f.mul(v0, f.power(ratio, 3))
                logarithmic = f.sub(f.scale(f.div(dnumerator, numerator), 3),
                                    f.scale(original_base_logarithmic, 2))
                dw = f.mul(w, logarithmic)
                assert f.mul(w, f.power(v0, 2)) == f.power(numerator, 3)
                assert f.mul(ratio, v0) == numerator
                assert f.add(f.mul(dratio, v0), f.mul(ratio, d0)) == dnumerator
                refs = [ref0, refj]
                expression = 'W_j=(V_0+V_j)^3/V_0^2'
            assert w != f.zero
            assert f.mul(logarithmic, w) == dw
            self.store(name, {'j': j, 'original_map': 'f4' if j == 0 else 'f4+T^'+str(j)+' f4',
                'W_expression': expression, 'source_V_jets': refs,
                'W_value_L': f.encode(w), 'W_derivative_t_L': f.encode(dw),
                'W_logarithmic_derivative_t_L': f.encode(logarithmic),
                'lambda_cube_value_L': f.encode(f.scale(w, 108)),
                'lambda_cube_derivative_t_L': f.encode(f.scale(dw, 108)),
                'lambda_over_lambda_f_value_L': f.encode(ratio),
                'lambda_over_lambda_f_derivative_t_L': f.encode(dratio),
                'common_lambda_cube_unit_factor': '(1-2*t)/(1-t)^2; value1 and derivative0 at t0',
                'actual_W_and_lambda_cube_nonzero': True,
                'all_field_inverses_and_displayed_quotients_multiplied_back': True,
                'original_lambda_cube_constant': 108,
                'cubic_root_selected_or_extra_target_phase_inserted': False})
            old = self.cached(name)
        return old, file_spec(self.path(name))

    def norm_and_trace(self, j):
        name = PREFIX+'original-norm-and-trace-j'+str(j)
        old = self.cached(name)
        if old is None:
            self.budget()
            f = self.field
            data, ref = self.W_jet(j)
            cube = f.decode(data['lambda_cube_value_L'])
            log_derivative = f.decode(data['W_logarithmic_derivative_t_L'])
            matrix = f.multiplication_matrix_over_K(cube)
            norm, pivots = k_determinant(matrix)
            assert norm != KZERO
            trace_matrix = f.multiplication_matrix_over_K(log_derivative)
            trace = KZERO
            for i in range(7):
                trace = k_add(trace, trace_matrix[i][i])
            self.store(name, {'j': j, 'source_W_jet': ref,
                'norm_expression': 'N_{L/K}(108*W_j(0))',
                'norm_K_1_s': k_encode(norm),
                'trace_expression': 'Tr_{L/K}(W_j_prime(0)/W_j(0))',
                'trace_K_1_s': k_encode(trace),
                'multiplication_basis_over_K': ['1', 'b', 'b^2', 'b^3', 'b^4', 'b^5', 'b^6'],
                'original_norm_multiplication_matrix_K': k_matrix_encode(matrix),
                'norm_pivot_transcript': pivots,
                'original_trace_multiplication_matrix_K': k_matrix_encode(trace_matrix),
                'actual_norm_nonzero': True,
                'all_pivot_inverses_multiplied_back': True,
                'actual_norm_and_trace_in_original_K_basis_computed': True,
                'Norm_is_actual_field_norm_not_same_target_T_product': True,
                'no_original_Galois_or_target_scaling_constant_discarded': True})
            old = self.cached(name)
        return old, file_spec(self.path(name))

    def comparison(self, j):
        name = PREFIX+'original-comparison-leading-jet-j'+str(j)
        old = self.cached(name)
        if old is None:
            self.budget()
            base, ref0 = self.norm_and_trace(0)
            other, refj = self.norm_and_trace(j)
            p, q = self.pq[j-1]
            n0, nj = k_decode(base['norm_K_1_s']), k_decode(other['norm_K_1_s'])
            tr0, trj = k_decode(base['trace_K_1_s']), k_decode(other['trace_K_1_s'])
            assert n0 != KZERO and nj != KZERO
            derivative = k_scale(k_sub(k_scale(trj, q), k_scale(tr0, p)), Fraction(-1, 2))
            nodes = [
                {'id': 'norm_f', 'operation': 'exact_original_K_constant', 'value': k_encode(n0), 'source': ref0},
                {'id': 'norm_g', 'operation': 'exact_original_K_constant', 'value': k_encode(nj), 'source': refj},
                {'id': 'numerator', 'operation': 'integer_power', 'input': 'norm_f', 'exponent': 2*p},
                {'id': 'denominator', 'operation': 'integer_power', 'input': 'norm_g', 'exponent': 2*q},
                {'id': 'kappa', 'operation': 'divide', 'numerator': 'numerator', 'denominator': 'denominator',
                 'denominator_nonzero_proof': 'actual nonzero norm_g; positive integer exponent'},
            ]
            self.store(name, {'j': j, 'p': p, 'q': q,
                'source_original_eta_basis': self.r791.ref('R791-original-real-descent-and-eta-basis-inputs.json.gz'),
                'original_degree_zero_ratio': self.eta['degree_zero_basis'][j-1]['degree_zero_coefficient_dj_over_d0'],
                'original_comparison_function': 'R_j=N(y_(f+T^j f)^2-b)^q/N(y_f^2-b)^p',
                'parameter': 't=a^3', 'order_in_t': 14*(p-q),
                'leading_constant_expression': 'N(108*V0)^(2*p)/N(108*Wj)^(2*q)',
                'leading_constant_DAG': {'nodes': nodes, 'output': 'kappa', 'coefficient_field_basis': K_BASIS},
                'leading_constant_DAG_sha256': fingerprint(nodes),
                'unit_first_logarithmic_derivative_expression': '-(q*Tr(Wj_prime/Wj)-p*Tr(V0_prime/V0))/2',
                'unit_first_logarithmic_derivative_K_1_s': k_encode(derivative),
                'series_identity': 'R_j=kappa_j*t^order*(1+d_j*t+O(t^2))',
                'actual_all_DAG_denominators_nonzero': True,
                'actual_leading_constant_defined_and_nonzero': True,
                'actual_unit_first_logarithmic_derivative_computed': True,
                'leading_constant_large_integer_powers_expanded': False,
                'unit_first_logarithmic_derivative_second_K_coordinate_is_zero': derivative[1] == 0,
                'both_original_K_coordinates_retained_without_projection': True,
                'global_Picard_rigidification_or_height_computed': False})
            old = self.cached(name)
        return old, file_spec(self.path(name))

    def inventory(self):
        path = self.path(PREFIX+'stage-manifest')
        files = []
        for candidate in sorted(self.out.glob(PREFIX+'*.json.gz')):
            if candidate == path:
                continue
            data = read(candidate)
            assert data['complete'] is True and data['configuration'] == self.tag
            assert data['result'] == RESULT
            files.append(file_spec(candidate))
        save(path, {'result': RESULT, 'configuration': self.tag, 'complete': True,
                    'files': files, 'completed_stage_count': len(files),
                    'only_complete_current_source_stages_listed': True})
        return file_spec(path)

    def finish(self, complete, reason):
        stages = {}
        for group, stem, indices in (
                ('V_jets', 'U-over-E6-first-jet-j', range(6)),
                ('W_jets', 'W-and-lambda-cube-first-jet-j', range(6)),
                ('norm_and_trace', 'original-norm-and-trace-j', range(6)),
                ('comparison_leading_jets', 'original-comparison-leading-jet-j', range(1, 6))):
            stages[group] = {str(j): file_spec(self.path(PREFIX+stem+str(j))) for j in indices
                             if self.cached(PREFIX+stem+str(j)) is not None}
        if complete:
            assert [len(stages[key]) for key in ('V_jets', 'W_jets', 'norm_and_trace', 'comparison_leading_jets')] == [6, 6, 6, 5]
        source = self.path(PREFIX+'original-source-audit')
        cert = {'result': RESULT, 'p': 41, 'configuration': self.tag, 'complete': complete,
                'source_audit': file_spec(source) if source.exists() else None,
                **stages, 'stage_manifest': self.inventory(), 'stop_reason': reason,
                'all_six_original_U_over_E6_values_and_first_jets_computed': complete,
                'all_six_original_lambda_cubes_and_logarithmic_derivatives_computed': complete,
                'all_six_true_relative_norms_and_traces_computed': complete,
                'all_five_original_comparison_leading_constants_DAG_and_unit_jets_computed': complete,
                'all_original_nonzero_values_and_division_denominators_checked': complete,
                'original_1722_82_and_108_normalizations_preserved': complete,
                'original_pq_eta_directions_and_true_norm_constants_preserved': complete,
                'large_integer_powers_of_leading_constants_expanded': False,
                'cubic_root_or_new_CM_period_normalization_chosen': False,
                'original_global_A_B_Fourier_Hom_periods_or_torsion_recomputed': False,
                'global_Picard_rigidification_or_height_computed': False,
                'actual_eta_zero_or_uniformity_proved': False,
                'seconds': time.monotonic()-self.started}
        save(self.out/FINAL, cert)
        return cert

    def run(self):
        final = self.out/FINAL
        if final.exists():
            previous = read(final)
            assert previous['configuration'] == self.tag and previous['result'] == RESULT
            if previous['complete'] is True:
                spec = previous['stage_manifest']
                assert file_spec(self.out/spec['file']) == spec
                for row in read(self.out/spec['file'])['files']:
                    assert file_spec(self.out/row['file']) == row
                return previous
        self.source_audit()
        for j in range(6):
            self.V_jet(j)
        for j in range(6):
            self.W_jet(j)
            self.norm_and_trace(j)
        for j in range(1, 6):
            self.comparison(j)
        return self.finish(True, 'all_original_c0_first_jets_and_comparison_leading_constants_certified')


def main():
    sys.set_int_max_str_digits(0)
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise SystemExit('All new mathematical arithmetic must run in the original public GitHub Actions repository.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--budget-minutes', type=float, default=300)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    job, certificate, code, error = None, None, 1, None
    try:
        job = Job(args)
        certificate = job.run()
        code = 0
    except BudgetStop as exception:
        error, code = str(exception), 124
        if job is not None:
            certificate = job.finish(False, 'budget_between_atomic_original_c0_stages')
    except Exception as exception:
        error = type(exception).__name__+': '+str(exception)
        import traceback
        traceback.print_exc()
    receipt = {'result': RESULT, 'p': 41, 'source_sha256': sha(__file__),
               'complete': code == 0, 'process_exit_code': code, 'error': error,
               'configuration_sha256': fingerprint(job.tag) if job is not None else None,
               'certificate_sha256': sha(args.out/FINAL) if certificate is not None else None,
               'all_six_original_U_over_E6_values_and_first_jets_computed': code == 0,
               'all_five_original_comparison_leading_constants_DAG_and_unit_jets_computed': code == 0,
               'global_Picard_rigidification_or_height_computed': False,
               'seconds': time.monotonic()-started}
    save(args.out/'core-receipt.json', receipt)
    print(json.dumps(receipt, sort_keys=True), flush=True)
    raise SystemExit(code)


if __name__ == '__main__':
    main()
