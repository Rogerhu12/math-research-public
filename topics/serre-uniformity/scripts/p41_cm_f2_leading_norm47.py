#!/usr/bin/env python3
"""Assemble the actual F2 collision norm from the CM and canonical supports.

The function is f_C=F_chain/(g0*h^m), in the fixed first Abel frame.
All factors are leading coefficients in actual parameters; the j-parameter
change is applied at P and b.  The output is not itself a height.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

Q = 47**4


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def mul(a, b):
    return [(a[0]*b[0]-a[1]*b[1]) % Q, (a[0]*b[1]+a[1]*b[0]) % Q]


def inverse(a):
    determinant = (a[0]*a[0]+a[1]*a[1]) % Q
    assert determinant % 47
    d = pow(determinant, -1, Q)
    return [a[0]*d % Q, -a[1]*d % Q]


def power(a, n):
    assert (a[0]*a[0]+a[1]*a[1]) % 47
    if n < 0:
        a, n = inverse(a), -n
    answer = [1, 0]
    while n:
        if n & 1:
            answer = mul(answer, a)
        a = mul(a, a)
        n //= 2
    return answer


def logarithm(a):
    assert a % 47
    u = pow(a, 46, Q)
    assert u % 47 == 1
    z = (u-1) % Q
    answer = (z-z*z*pow(2, -1, Q)+z*z*z*pow(3, -1, Q))*pow(46, -1, Q) % Q
    assert answer % 47 == 0
    return answer


def save(path, payload):
    raw = gzip.compress((json.dumps(payload, sort_keys=True, separators=(',', ':'))+'\n').encode(), mtime=0)
    temporary = path.with_suffix(path.suffix+'.new')
    temporary.write_bytes(raw)
    temporary.replace(path)
    return len(raw), hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--discriminant', type=int, choices=[12, 7], required=True)
    parser.add_argument('--cm', type=Path)
    parser.add_argument('--low', type=Path)
    parser.add_argument('--high', type=Path)
    parser.add_argument('--parameters', type=Path, default=Path('/tmp/p41_cm_j_parameter47_certificate.json'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    prefix = '/tmp/p41_cm'+str(args.discriminant)
    cm, cm_sha = read(args.cm or Path(prefix+'_miller_prepared47_complete.json.gz'))
    low, low_sha = read(args.low or Path(prefix+'_canonical_low_prepared47_complete.json.gz'))
    high, high_sha = read(args.high or Path(prefix+'_canonical_high47_complete.json.gz'))
    parameters, parameters_sha = read(args.parameters)
    hashes = cm['source_sha256']
    assert low['source_sha256'] == high['source_sha256'] == parameters['source_sha256'] == hashes
    for data in [cm, low, high]:
        assert data['discriminant'] == -args.discriminant
        assert data['bits_done'] == 304 and data['steps_done'] == 454
        assert data['nonunit_divisions'] == 0
        assert data['input_sha256']['miller'] == cm['input_sha256']['miller']
        assert data['input_sha256']['endpoint'] == cm['input_sha256']['endpoint']
        assert data['input_sha256']['initial'] == cm['input_sha256']['initial']
    assert high['all_step_norms_units'] and high['old_and_new_effective_ideals_avoid_high_support']
    assert high['degree'] == 102
    m = high['target_multiplier']
    assert parameters['target_multiplier'] == m
    label = 'P_minus'+str(args.discriminant)
    points = {rec['label']: rec for rec in cm['global_based_function_local_values']}
    assert len(points) == 26
    for name, rec in points.items():
        expected_order = m if name == label else -m if name == 'P_minus3' else 0
        assert rec['order_in_fixed_local_parameter'] == expected_order
        assert (rec['ordinary_finite_value'] is None) == bool(expected_order)
    z8 = [name for name in points if name.startswith('Z_minus8_')]
    assert len(z8) == 20
    weights = {name: -27 for name in z8}
    if args.discriminant == 12:
        weights.update({'P_minus12': 85, 'P_minus3': 31, 'P_minus7': -54,
                        'CM48_plus': 27, 'CM48_minus': 27})
    else:
        weights.update({'P_minus7': 4, 'P_minus3': 4, 'P_minus12': 81, 'CM28': 27})
    assert sum(weights.values()) == -424
    cm_product = [1, 0]
    weighted = []
    for name, weight in sorted(weights.items()):
        value = points[name]['leading_unit_mod47four']
        factor = power(value, weight)
        cm_product = mul(cm_product, factor)
        weighted.append({'label': name, 'divisor_coefficient': weight,
                         'function_order': points[name]['order_in_fixed_local_parameter'],
                         'leading_unit_in_computational_parameter': value, 'powered_factor': factor})
    lows = low['global_based_function_local_values']
    assert len(lows) == 4
    assert {a['label'] for a in lows} == {'canonical1_root_'+str(i) for i in [3, 23, 43, 44]}
    low_product = [1, 0]
    for rec in lows:
        assert rec['order_in_fixed_local_parameter'] == 0
        low_product = mul(low_product, rec['leading_unit_mod47four'])
    canonical_norm = mul(low_product, [high['actual_based_function_norm_mod47four'], 0])
    assert canonical_norm[1] == 0
    parameter_record = parameters['F2_leading_norm_parameter_factors'][label]
    assert parameter_record['CM_divisor_coefficient'] == weights[label]
    assert parameter_record['base_divisor_coefficient'] == weights['P_minus3']
    raw_product = mul(cm_product, power(canonical_norm, 4))
    correction = parameter_record['leading_coefficient_norm_j_over_t']
    assert logarithm(correction) == parameter_record['log_factor_mod47four']
    actual = mul(raw_product, [correction, 0])
    assert raw_product[1] == actual[1] == 0
    actual_log = logarithm(actual[0])
    assert actual_log == (logarithm(raw_product[0])+parameter_record['log_factor_mod47four']) % Q
    payload = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'discriminant': -args.discriminant,
               'source_sha256': hashes,
               'input_sha256': {'CM_local_units': cm_sha, 'canonical_low4': low_sha,
                                'canonical_high102': high_sha, 'actual_j_parameters': parameters_sha,
                                'complete_Miller': cm['input_sha256']['miller'],
                                'actual_endpoint_g0': cm['input_sha256']['endpoint']},
               'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'target_multiplier': m, 'CM_weight_sum': -424, 'canonical_degree': 106,
               'canonical_divisor_coefficient': 4, 'complete_second_divisor_degree': 0,
               'actual_CM_leading_factors': weighted, 'CM_product': cm_product,
               'canonical_low4_norm': low_product,
               'canonical_high102_norm': high['actual_based_function_norm_mod47four'],
               'actual_complete_canonical_norm': canonical_norm,
               'leading_product_before_j_parameter_change': raw_product,
               'actual_j_parameter_factor': correction,
               'generalized_f_C_D_P_j_norm': actual[0],
               'log_generalized_f_C_D_P_j_norm': actual_log,
               'nonunit_divisions': 0,
               'formula': 'f_C[D_P]_j=product_CM(lc_t(f_C)^coefficient)*Norm_Kg1(f_C)^4*parameter_factor',
               'status': 'complete collision-corrected actual F2 first-variable Miller norm, with all26 CM and106 canonical support and exact j-parameters; not the full Poincare height'}
    output = args.output or Path(prefix+'_f2_leading_norm47_certificate.json.gz')
    size, sha = save(output, payload)
    print('ACTUAL F2 GENERALIZED CM NORM PASS', args.discriminant, 'norm', actual[0], 'log', actual_log,
          'bytes', size, 'sha', sha, flush=True)


if __name__ == '__main__':
    main()
