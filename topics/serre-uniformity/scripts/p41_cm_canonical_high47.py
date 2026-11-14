#!/usr/bin/env python3
"""Evaluate actual based-CM Miller SLPs on the canonical high102 algebra.

Only Python integers and FLINT polynomials are used.  In particular this does
not construct another Makdisi model or repeat a Jacobian group operation.
Every inverse used in the evaluation is checked to be a 47-adic unit.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

Q = 47**4


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(',', ':')).encode()).hexdigest()


def save(path, value):
    raw = (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(raw, mtime=0)
    assert len(packed) < 5_000_000
    temporary = path.with_suffix(path.suffix+'.new')
    temporary.write_bytes(packed)
    temporary.replace(path)
    return len(packed), hashlib.sha256(packed).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--discriminant', type=int, choices=[7, 12], required=True)
    parser.add_argument('--algebra', type=Path, default=Path('/tmp/p41_canonical_restriction47_candidate1_raw.json.gz'))
    parser.add_argument('--low-points', type=Path)
    parser.add_argument('--miller', type=Path, required=True)
    parser.add_argument('--endpoint', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    from flint import fmpz_poly, nmod_poly
    started = time.monotonic()
    data, algebra_sha = read(args.algebra)
    slp, slp_sha = read(args.miller)
    initial_path = args.script_dir/'data/p41_cm_based_points47_checkpoint.json.gz'
    initial, initial_sha = read(initial_path)
    low_path = args.low_points or args.script_dir/'data/p41_canonical_low_points47_certificate.json.gz'
    low, low_sha = read(low_path)
    hashes = data['source_sha256']
    assert hashes == slp['source_sha256'] == initial['source_sha256']
    for name, expected in hashes.items():
        assert hashlib.sha256((args.script_dir/'data'/name).read_bytes()).hexdigest() == expected
    assert low['canonical_algebra_sha256'] == algebra_sha
    assert slp['initial_source_sha256'] == initial_sha
    assert slp['point_label'] == 'P_minus'+str(args.discriminant)
    assert slp['initial_principal_transport_coefficients'] == initial['f_b_coefficients']
    point = next(rec for rec in initial['records'] if rec['point_label'] == slp['point_label'])
    assert point['point_sha256'] == slp['initial_point_sha256']
    assert data['etale_mod47']
    Phi = {degree: data['Phi'+str(degree)] for degree in [1, 2, 3]}
    H = low['high_factor_ascending']
    Hz = fmpz_poly(H)
    Hp = nmod_poly([a % 47 for a in H], 47)
    assert Hp.degree() == 102 and Hp.gcd(Hp.derivative()).degree() == 0
    factors = [f for f, exponent in Hp.factor()[1]]
    assert sorted(f.degree() for f in factors) == [6, 8, 22, 31, 35]

    def evaluate(label, coefficient_rows, degree, keep_polynomial=False):
        coefficients = [row[0] for row in coefficient_rows]
        assert len(coefficients) == len(Phi[degree][0])
        polynomial = []
        for row in Phi[degree]:
            real = sum(a*c-b*d for (a, b), (c, d) in zip(row, coefficients)) % Q
            imag = sum(a*d+b*c for (a, b), (c, d) in zip(row, coefficients)) % Q
            assert imag == 0, 'The actual rational section did not descend in the fixed rational algebra'
            polynomial.append(real)
        reduced = nmod_poly([a % 47 for a in polynomial], 47)
        common = Hp.gcd(reduced)
        value = int(Hz.resultant(fmpz_poly(polynomial))) % Q
        common_indices = [i+1 for i, factor in enumerate(factors) if reduced % factor == 0]
        assert sum(factors[i-1].degree() for i in common_indices) == common.degree()
        assert bool(value % 47) == (common.degree() == 0)
        answer = {'label': label, 'actual_norm_mod47four': value,
                  'polynomial_sha256': digest(polynomial),
                  'common_factor_indices_1based': common_indices,
                  'common_factor_degree_mod47': common.degree()}
        if keep_polynomial:
            answer['polynomial_ascending_mod47four'] = polynomial
        return answer

    negative = evaluate('actual_negative_CM_quadratic', slp['negative_quadratic_coefficients'], 2, True)
    h = evaluate('actual_initial_h_equals_f_b_over_f0', initial['f_b_coefficients'], 1, True)
    assert negative['common_factor_degree_mod47'] == h['common_factor_degree_mod47'] == 0
    inverse_negative = pow(negative['actual_norm_mod47four'], -1, Q)
    records = []
    cumulative = 1
    sign = 1
    valid = True
    magnitude = 1
    for index, step in enumerate(slp['steps'], 1):
        coefficients = step['principal_section_coefficients']
        assert digest(coefficients) == step['principal_coefficient_sha256']
        rec = evaluate('actual_AddFlip_'+str(index), coefficients, 3)
        rec.update({'step_index_1based': index, 'operation': step['operation'],
                    'bit': step['bit'], 'sign': step['sign'],
                    'principal_coefficient_sha256': step['principal_coefficient_sha256']})
        valid = valid and rec['common_factor_degree_mod47'] == 0
        if valid:
            if step['operation'] == 'double':
                cumulative = pow(cumulative*cumulative % Q*rec['actual_norm_mod47four'] % Q, -1, Q)
                magnitude *= 2
            else:
                assert step['operation'] == 'add'
                extra = 1 if sign == 1 else inverse_negative
                cumulative = pow(cumulative*extra % Q*rec['actual_norm_mod47four'] % Q, -1, Q)
                magnitude += 1
            rec['cumulative_actual_norm_F_signed_n'] = cumulative
        sign = -sign
        assert sign == step['sign']
        records.append(rec)
    if valid:
        assert magnitude == slp['magnitude'] and sign == slp['sign']
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
              'discriminant': -args.discriminant, 'point_label': slp['point_label'],
              'source_sha256': hashes,
              'input_sha256': {'canonical_algebra': algebra_sha, 'low_points': low_sha,
                               'miller': slp_sha, 'initial': initial_sha},
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'canonical_candidate': data['canonical_candidate'], 'degree': 102,
              'high_polynomial_ascending': H,
              'factor_polynomials_ascending_mod47': [[int(a) for a in f.coeffs()] for f in factors],
              'factor_degrees_mod47': [f.degree() for f in factors],
              'bits_done': slp['bits_done'], 'steps_done': len(records),
              'actual_initial_h': h, 'actual_negative_quadratic': negative,
              'steps': records, 'all_step_norms_units': valid,
              'nonunit_steps_1based': [rec['step_index_1based'] for rec in records if rec['common_factor_degree_mod47']],
              'cumulative_actual_norm_F_signed_n': cumulative if valid else None,
              'nonunit_divisions': 0,
              'status': 'actual canonical high102 norms through the saved CM SLP prefix; no height claimed'}
    if args.endpoint:
        endpoint, endpoint_sha = read(args.endpoint)
        assert valid and slp['bits_done'] == 304 and len(records) == 454 and sign == 1
        assert slp['magnitude'] == slp['target_multiplier']
        assert endpoint['source_sha256'] == hashes
        assert endpoint['input_sha256']['miller'] == slp_sha
        assert endpoint['old_final_point_sha256'] == slp['point_sha256']
        assert endpoint['discriminant'] == -args.discriminant
        transport = endpoint['transport']
        components = {}
        for label, key, degree in [('new', 'new_section_coefficients', 2),
                                    ('old', 'old_section_coefficients', 2),
                                    ('v1', 'v1_coefficients', 1)]:
            components[label] = evaluate(label, transport[key], degree, True)
            assert components[label]['common_factor_degree_mod47'] == 0
        gt = components['new']['actual_norm_mod47four']*pow(
            components['old']['actual_norm_mod47four']*components['v1']['actual_norm_mod47four'] % Q, -1, Q) % Q
        m = slp['target_multiplier']
        true_norm = cumulative*pow(gt*pow(h['actual_norm_mod47four'], m, Q) % Q, -1, Q) % Q
        result['input_sha256']['endpoint'] = endpoint_sha
        result.update({'endpoint_components': components,
                       'actual_endpoint_transport_norm_mod47four': gt,
                       'target_multiplier': m,
                       'actual_based_function_norm_mod47four': true_norm,
                       'actual_function': 'f_C=F_chain/(g_transport*h^m); div(f_C)=m(P-b)-A_formal',
                       'old_and_new_effective_ideals_avoid_high_support': True,
                       'ideal_avoidance_reason': 'the actual old/new transport sections belong to those ideals and have unit determinant norm in the entire high102 algebra',
                       'status': 'complete actual based-CM function norm on high102 canonical support, including initial h and true endpoint transport; no height claimed'})
    output = args.output or Path('/tmp/p41_cm'+str(args.discriminant)+'_canonical_high47_checkpoint.json.gz')
    size, sha = save(output, result)
    print('ACTUAL BASED CM HIGH102 NORMS', args.discriminant, slp['bits_done'], 'bits', len(records),
          'steps; all units', valid, 'nonunit steps', result['nonunit_steps_1based'],
          'bytes', size, 'sha', sha, 'seconds', round(time.monotonic()-started, 2),
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)
    if 'actual_based_function_norm_mod47four' in result:
        print('FINAL ACTUAL BASED CM HIGH102 NORM', result['actual_based_function_norm_mod47four'], flush=True)


if __name__ == '__main__':
    main()
