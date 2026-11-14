#!/usr/bin/env python3
"""Exact R239 verification, standard library only.

The only imported arithmetic helper is the already-published R219 verifier.
No class group, numerical root, PARI, or actual relative norm witness is used.
"""
import argparse
import hashlib
import json
from pathlib import Path
from verify_o6_single_real_norm_target import Field44, Fp2, central


def load_element(data, gaussian=False):
    if gaussian:
        values = [tuple(map(int, row)) for row in data['Gaussian_numerators_ascending']]
    else:
        values = [(int(a), 0) for a in data['numerators_ascending']]
    assert len(values) == 44
    return tuple(values) + (int(data['common_denominator']),)


def serialize(a, gaussian=False):
    if gaussian:
        return {'common_denominator': str(a[-1]),
                'Gaussian_numerators_ascending': [[str(x), str(y)] for x, y in a[:-1]]}
    assert all(y == 0 for x, y in a[:-1])
    return {'common_denominator': str(a[-1]),
            'numerators_ascending': [str(x) for x, y in a[:-1]]}


def verify(source, r219_source, certificate):
    raw = Path(source).read_bytes()
    raw219 = Path(r219_source).read_bytes()
    source_data = json.loads(raw)
    old = json.loads(raw219)
    data = json.loads(Path(certificate).read_text())
    assert old['source_sha256'] == hashlib.sha256(raw).hexdigest()
    assert data['source_sha256'] == hashlib.sha256(raw).hexdigest()
    assert data['r219_sha256'] == hashlib.sha256(raw219).hexdigest()
    fz = list(map(int, source_data['factors'][0]['coefficients']))
    g = list(map(int, data['fourth_root_unit_polynomial_ascending']))
    assert len(g) == 45 and g[0] == g[-1] == 1 and g == g[::-1]
    F, K = Field44(fz), Field44(g)
    root = load_element(data['fourth_root_t_in_old_z'])
    assert F.normalize(root[:-1], root[-1]) == root
    assert F.power(root, 4) == F.z
    assert F.evaluate(g, root) == F.zero
    z_new = K.power(K.z, 4)
    assert K.evaluate(fz, z_new) == K.zero
    assert K.compose(root, z_new) == K.z
    # Transport the exact, positively labelled R219 Artin map.  Merely being
    # an automorphism or matching one unlabelled finite root is insufficient.
    old_sigma = load_element(old['labeled_sigma_exact'], True)
    sigma = load_element(data['same_positive_Artin_sigma_t'], True)
    transported = K.compose(F.compose(root, old_sigma), z_new)
    assert sigma == transported
    assert K.evaluate(g, sigma) == K.zero
    roots = [K.z]
    for j in range(1, 44):
        roots.append(K.compose(roots[-1], sigma))
    assert len(set(roots)) == 44
    assert K.compose(roots[-1], sigma) == K.z
    assert K.mul(roots[22], K.z) == K.one
    assert all(K.conj(roots[j]) == roots[-j % 44] for j in range(44))
    base = [K.z] + [K.mul(roots[j], roots[-j]) for j in range(1, 11)]
    inverse = [roots[22]] + [K.mul(roots[22+j], roots[22-j]) for j in range(1, 11)]
    assert all(K.conj(a) == a for a in base)
    assert all(K.mul(a, b) == K.one for a, b in zip(base, inverse))
    powers = []
    for a, b in zip(base, inverse):
        row = {0: K.one}
        for exponent in range(1, 44):
            row[exponent] = K.mul(row[exponent-1], a)
            row[-exponent] = K.mul(row[1-exponent], b)
        powers.append(row)

    def product(exponents):
        answer = K.one
        for row, exponent in zip(powers, exponents):
            answer = K.mul(answer, row[exponent])
        return answer

    finite = Fp2(43)
    omega = (8, 25)
    reals = [finite.power(omega, j)[0] for j in range(11)]
    a = old['single_real_norm_target_exponents_ascending'][:11]
    assert a == [central(15*x, 43) for x in reals]
    root8 = product(a)
    U = K.compose(load_element(old['ordinary_real_norm_target_exact']), z_new)
    assert K.power(root8, 8) == U
    rows, targets = [], {}
    for c in range(1, 43):
        b = [central(c*x, 43) for x in reals]
        target = product(b)
        exponent = 34 * pow(c, -1, 43) % 43
        rows.append({'c': c, 'b': b, 'r': exponent,
                     'readout_factor': 4*exponent % 43,
                     'max_numerator_bits': max(abs(x).bit_length() for x,y in target[:-1]),
                     'denominator_bits': target[-1].bit_length()})
        targets[c] = target
    best = min(rows, key=lambda row: (row['max_numerator_bits'],
                                      row['denominator_bits'], row['c']))
    selected = []
    for c in sorted({7, 15, best['c']}):
        row = next(row for row in rows if row['c'] == c)
        exponent, b = row['r'], row['b']
        d = [(8*x-exponent*y)//43 for x, y in zip(a, b)]
        assert all(8*x-exponent*y == 43*z for x, y, z in zip(a, b, d))
        B = product(d)
        assert K.mul(K.power(targets[c], exponent), K.power(B, 43)) == U
        selected.append({**row, 'base_correction_exponents': d,
                         'target_V_in_t': serialize(targets[c]),
                         'base_correction_B_in_t': serialize(B)})
    expected = {
        'schema': 'o6_short_ordinary_real_norm_targets_v1',
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'r219_sha256': hashlib.sha256(raw219).hexdigest(),
        'fourth_root_unit_polynomial_ascending': [str(c) for c in g],
        'fourth_root_t_in_old_z': serialize(root),
        'same_positive_Artin_sigma_t': serialize(sigma, True),
        'old_z_in_new_t_power': 4,
        'eighth_root_V15_in_t': serialize(root8),
        'ordinary_real_basis_definition': 'b_0=t; b_j=(sigma^j t)(sigma^(-j) t), 1<=j<=10',
        'all_42_target_scores': rows,
        'minimum_coefficient_score_c': best['c'],
        'chosen_targets': selected,
        'same_sigma_order_44_verified': True,
        'same_real_involution_verified': True,
        'U_is_V15_eighth_power_verified': True,
        'actual_norm_preimage_computed': False,
        'actual_L_computed': False,
    }
    assert expected == data
    return {
        'status': 'PASS', 'same_labeled_field_and_Artin': True,
        'exact_fourth_root_z': True, 'exact_eighth_root_U': True,
        'all_42_coordinate_scores_recomputed': True,
        'selected_exact_norm_target_identities': [row['c'] for row in selected],
        'best_coordinate_c': best['c'],
        'best_target_numerator_bits': best['max_numerator_bits'],
        'best_target_denominator_bits': best['denominator_bits'],
        'factor_one_readout_c': 7, 'actual_norm_preimage_computed': False,
        'actual_L_computed': False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('r219_source')
    parser.add_argument('certificate')
    args = parser.parse_args()
    print(json.dumps(verify(args.source, args.r219_source, args.certificate),
                     ensure_ascii=False, separators=(',', ':')))


if __name__ == '__main__':
    main()
