#!/usr/bin/env python3
"""Actual f_C,S(T2*A0(mC)) by whole-disc cancellation and shifted unit preparation.

Nonunit sections use their own exact4e+3 target jets.  Initial, negative,
current and final complete ideals are checked on every target disc.  No
division by47 or evaluation of a0/0 expression is performed.
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import sys
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def release():
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--class-name', choices=['cm12', 'cm7'], required=True)
    parser.add_argument('--miller', type=Path, required=True)
    parser.add_argument('--endpoint', type=Path, required=True)
    parser.add_argument('--jets', type=Path, default=Path('/tmp/p41_t2_first_family_cubic47_checkpoint.json.gz'))
    parser.add_argument('--discs', type=Path, default=Path('/tmp/p41_t2_quadratic_discs47_checkpoint.json.gz'))
    parser.add_argument('--inventory', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_cm4_divisor47 import kernel
    from p41_hecke3_hessian47 import section_jets
    from p41_weierstrass_unit47 import prepare_unit
    from p41_poincare_norms47 import pair_mul, pair_inverse
    from p41_formal47_multiply import point_hash, write_checkpoint
    started = time.monotonic()
    discriminant = int(args.class_name[2:])
    coefficients = {1: [], 2: [], 3: []}
    lookup = {}

    def add_section(label, encoded, degree):
        lookup[label] = degree, len(coefficients[degree])
        coefficients[degree].append(r.from_json(encoded))

    slp, slpsha = read(args.miller)
    assert slp['bits_done'] == 304 and len(slp['steps']) == 454
    assert slp['sign'] == 1 and slp['magnitude'] == slp['target_multiplier']
    assert slp['point_label'] == 'P_minus'+str(discriminant) and slp['status'].startswith('complete actual')
    hashes = slp['source_sha256']
    m = slp['target_multiplier']
    inputs = {'miller': slpsha}
    steps = []
    for index, step in enumerate(slp['steps']):
        encoded = step['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest() == step['principal_coefficient_sha256']
        add_section('step'+str(index), encoded, 3)
        steps.append({k: step[k] for k in ['operation', 'sign', 'principal_coefficient_sha256']})
    add_section('negative', slp['negative_quadratic_coefficients'], 2)
    points_full = {}
    for label, prefix in [('current', ''), ('negative', 'negative_')]:
        K, A = r.from_json(slp[prefix+'point_coordinates']), r.from_json(slp[prefix+'point_frobenius'])
        assert point_hash(K, A) == slp[prefix+'point_sha256']
        points_full[label] = K
    initial_sha = slp['initial_source_sha256']
    initial_point_sha = slp['initial_point_sha256']
    current_point_sha = slp['point_sha256']
    del slp, step, encoded, K, A
    release()
    endpoint, esha = read(args.endpoint)
    assert endpoint['source_sha256'] == hashes and endpoint['frame'] == 'newS'
    assert endpoint['class_name'] == args.class_name and endpoint['input_sha256']['miller'] == slpsha
    assert endpoint['old_final_point_sha256'] == current_point_sha
    inputs['endpoint'] = esha
    for label, field, degree in [('end_new', 'new_section_coefficients', 2), ('end_old', 'old_section_coefficients', 2), ('vS', 'v1_coefficients', 1)]:
        add_section(label, endpoint['transport'][field], degree)
    expected_newsha = endpoint['new_formal_point_sha256']
    expected_target_cert_sha = endpoint['input_sha256']['formal_endpoints']
    del endpoint
    release()
    target, target_sha = read(folder/('data/p41_t2_cm'+str(discriminant)+'_formal_transport47_checkpoint.json.gz'))
    assert target_sha == expected_target_cert_sha and target['source_sha256'] == hashes
    e = target['endpoints'][0]
    K, A = r.from_json(e['point_coordinates']), r.from_json(e['point_frobenius'])
    assert point_hash(K, A) == e['point_sha256'] == expected_newsha
    points_full['target'] = K
    inputs['new_S_target'] = target_sha
    expected_cm_sha = target['CM_formal_endpoints_sha256']
    del target, e, K, A
    initial, isha = read(folder/'data/p41_cm_based_points47_checkpoint.json.gz')
    assert isha == initial_sha and initial['source_sha256'] == hashes
    e = next(v for v in initial['records'] if v['point_label'] == 'P_minus'+str(discriminant))
    K, A = r.from_json(e['point_coordinates']), r.from_json(e['point_frobenius'])
    assert point_hash(K, A) == initial_point_sha
    points_full['initial'] = K
    add_section('h', initial['f_b_coefficients'], 1)
    inputs['initial_CM'] = isha
    del initial, e, K, A
    release()
    cm, cmsha = read(folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    assert cmsha == expected_cm_sha and cm['source_sha256'] == hashes
    first = cm['targets']['x'+str(discriminant)]['targets']['m']['exponentials'][0]
    assert first['family_index'] == 0
    first_sha = first['point_sha256']
    parameter_json = first['parameters'][0]
    par = r.from_json(first['parameters'])
    inputs['CM_formal_endpoints'] = cmsha
    del cm, first
    release()
    raw, jsha = read(args.jets)
    assert raw['source_sha256'] == hashes
    source_points = raw['points_1based']
    Wraw = [r.from_json([row for target in raw['targets'] for row in target['evaluation_coefficients'][k]]) for k in range(4)]
    labels = ['T2_'+str(branch)+'_P'+str(point) for branch in range(3) for point in source_points]
    inputs['actual_target_cubic'] = jsha
    del raw
    inv, invsha = read(args.inventory)
    assert inv['source_sha256'] == hashes and inv['input_sha256']['target_cubic'] == jsha
    assert all(not a['target_intersections'] for a in inv['actual_CM_support_disjointness'].values())
    actual_disjointness = inv['actual_CM_support_disjointness']
    inputs['support_inventory'] = invsha
    del inv
    discs, dsha = read(args.discs)
    assert discs['source_sha256'] == hashes and discs['target_cubic_sha256'] == jsha
    inputs['actual_integral_discs'] = dsha
    records = discs['records']
    disc_position = {a['label']: index for index, a in enumerate(records)}
    maximum_order = max(a['order'] for a in records)
    count = len(records)
    Wdeep = [r.from_json([a['normalized_weight2_coefficients'][k] if k <= a['order'] else [[0, 0]]*73 for a in records]) for k in range(maximum_order+1)]
    records = [{k: a[k] for k in ['label', 'order', 'branch_index_0based', 'first_family_position_0based', 'parameter_cubic_in_original_source_t', 'jets_sha256']} for a in records]
    del discs
    release()
    sources, checked_hashes = load_sources(folder/'data')
    assert hashes == checked_hashes
    M = make_model(sources)
    divs = sources[1]
    canon = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    f0 = r.mm(canon, r.column(divs['canonical_coefficients']))
    Vraw2, Vraw3 = section_jets(Wraw, sources, M, r)
    Vdeep2, Vdeep3 = section_jets(Wdeep, sources, M, r)
    rawvalues, deepvalues = {1: Wraw, 2: Vraw2, 3: Vraw3}, {1: Wdeep, 2: Vdeep2, 3: Vdeep3}
    tt = (np.tile(par[0].T, (3, 1)), np.tile(par[1].T, (3, 1)))
    assert tt[0].shape == (162, 1) and all(np.all(v % 47 == 0) for v in tt)
    moving = {}
    for degree in [1, 2, 3]:
        value = r.zeros(162, rawvalues[degree][0][0].shape[1])
        for a in reversed(rawvalues[degree]):
            value = r.add(r.mul(value, tt), a)
        moving[degree] = value
    fconstant, fmoving = r.mm(Wraw[0], f0), r.mm(moving[1], f0)
    assert np.all(r.units(fconstant)) and np.all(r.units(fmoving))
    assert r.equal(r.mm(Wdeep[0], f0), r.column([[1, 0]]*count))
    assert all(r.iszero(r.mm(v, f0)) for v in Wdeep[1:])
    ifconstant, ifmoving = r.inverse_values(fconstant), r.inverse_values(fmoving)
    invconstant, invmoving = r.column([[1, 0]]*162), r.column([[1, 0]]*162)
    fast, deep, unit_masks = {}, {}, {}
    normalized_constant_V2 = None
    for degree in [1, 2, 3]:
        invconstant, invmoving = r.mul(invconstant, ifconstant), r.mul(invmoving, ifmoving)
        C = r.hcat(*coefficients[degree])
        const = r.mul(r.mm(rawvalues[degree][0], C), invconstant)
        shifted = r.mul(r.mm(moving[degree], C), invmoving)
        fast[degree] = const, shifted
        unit_masks[degree] = r.units(const)
        deep[degree] = [r.mm(v, C) for v in deepvalues[degree]]
        if degree == 2:
            normalized_constant_V2 = r.mul(rawvalues[degree][0], invconstant)
    del M, sources, divs, canon, f0, Wraw, Vraw2, Vraw3, Wdeep, Vdeep3, rawvalues, deepvalues, moving, C, coefficients, par, tt
    release()

    def add(a, b):
        return [(a[0]+b[0]) % r.Q, (a[1]+b[1]) % r.Q]

    def scale(a, c):
        return [a[0]*c % r.Q, a[1]*c % r.Q]

    def product(a, b):
        out = [[0, 0] for _ in range(len(a)+len(b)-1)]
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] = add(out[i+j], pair_mul(x, y))
        return out

    def divide(a, b):
        assert a[-1] == b[-1] == [1, 0] and len(a) >= len(b)
        remainder = [x[:] for x in a]
        quotient = [[0, 0] for _ in range(len(a)-len(b)+1)]
        for k in range(len(quotient)-1, -1, -1):
            value = remainder[k+len(b)-1]
            quotient[k] = value[:]
            for j, x in enumerate(b):
                remainder[k+j] = add(remainder[k+j], scale(pair_mul(value, x), -1))
        assert all(x == [0, 0] for x in remainder), 'Actual monic disc factors failed exact cancellation'
        assert quotient[-1] == [1, 0] and all(a % 47 == b % 47 == 0 for a, b in quotient[:-1])
        return quotient

    def power(a, exponent):
        assert exponent >= 0
        value = [1, 0]
        while exponent:
            if exponent & 1:
                value = pair_mul(value, a)
            a = pair_mul(a, a)
            exponent >>= 1
        return value

    def pair_at(matrix, row, column=0):
        return [int(matrix[0][row, column]), int(matrix[1][row, column])]

    # Each disc can use its own integral parameter.  Individual stripped
    # factors need not have a rational product; rationality is required only
    # after all genuine divisor factors have cancelled.
    shifts = []
    for rec in records:
        t = parameter_json[rec['first_family_position_0based']]
        result = [0, 0]
        for value in reversed(rec['parameter_cubic_in_original_source_t']):
            result = add(pair_mul(result, t), value)
        assert result[0] % 47 == result[1] % 47 == 0
        shifts.append(result)
    release()
    one = [[1, 0]]
    maximum_e = 0

    def prepared(label, point):
        nonlocal maximum_e
        degree, column = lookup[label]
        if unit_masks[degree][point, column]:
            u0, ua = pair_at(fast[degree][0], point, column), pair_at(fast[degree][1], point, column)
            return {'degree': 0, 'weierstrass_coefficients': one,
                    'unit_constant': u0, 'shifted_unit_constant': ua,
                    'unit_ratio': pair_mul(ua, pair_inverse(u0))}
        assert labels[point] in disc_position, ('Missing actual nonunit disc', labels[point], label)
        pos = disc_position[labels[point]]
        order = records[pos]['order']
        germ = [pair_at(v, pos, column) for v in deep[degree][:order+1]]
        actual = prepare_unit(germ, precision=4)
        e = actual['degree']
        maximum_e = max(maximum_e, e)
        assert order >= 4*e+3, ('Insufficient shifted-unit precision', labels[point], label, e, order)
        shift = shifts[pos]
        powers = [[1, 0], shift, pair_mul(shift, shift), power(shift, 3)]
        shifted_germ = []
        for j in range(4*e+1):
            value = [0, 0]
            for k in range(j, j+4):
                value = add(value, scale(pair_mul(germ[k], powers[k-j]), comb(k, j)))
            shifted_germ.append(value)
        shifted = prepare_unit(shifted_germ, precision=4, degree=e)
        w = actual['weierstrass_coefficients']
        expected = []
        for j in range(e+1):
            value = [0, 0]
            for k in range(j, e+1):
                value = add(value, scale(pair_mul(w[k], power(shift, k-j)), comb(k, j)))
            expected.append(value)
        assert shifted['weierstrass_coefficients'] == expected
        return {**actual, 'shifted_unit_constant': shifted['unit_constant'],
                'unit_ratio': pair_mul(shifted['unit_constant'], pair_inverse(actual['unit_constant'])),
                'required_last_jet_for_shifted_unit': 4*e+3,
                'shifted_distinguished_factor_verified': True}

    def ideal_factors(K):
        constants = r.mm(normalized_constant_V2, K)
        constant_units = r.units(constants)
        zero_rows = {j for j in range(162) if not np.any(constant_units[j])}
        values = [r.mm(v, K) for v in Vdeep2] if zero_rows else None
        masks = [r.units(v) for v in values] if values else None
        result = []
        for j in range(162):
            if j not in zero_rows:
                column = int(np.flatnonzero(constant_units[j])[0])
                result.append({'column_1based': column+1, 'degree': 0, 'weierstrass_coefficients': one})
                continue
            assert labels[j] in disc_position, ('Ideal needs missing actual disc', labels[j])
            pos = disc_position[labels[j]]
            order = records[pos]['order']
            e = next((k for k in range(order+1) if np.any(masks[k][pos])), None)
            assert e is not None
            column = int(np.flatnonzero(masks[e][pos])[0])
            germ = [pair_at(v, pos, column) for v in values[:order+1]]
            prep = prepare_unit(germ, precision=4, degree=e)
            result.append({'column_1based': column+1, 'degree': e,
                           'weierstrass_coefficients': prep['weierstrass_coefficients']})
        return result

    ideals = {label: ideal_factors(K) for label, K in points_full.items()}
    del points_full, Vdeep2, normalized_constant_V2
    release()
    initial_h = [prepared('h', j) for j in range(162)]
    negative = [prepared('negative', j) for j in range(162)]
    initialW = [a['weierstrass_coefficients'] for a in ideals['initial']]
    negativeW = [a['weierstrass_coefficients'] for a in ideals['negative']]
    for j in range(162):
        assert initialW[j] == initial_h[j]['weierstrass_coefficients']
        assert divide(negative[j]['weierstrass_coefficients'], initialW[j]) == negativeW[j]
    minusU = [pair_inverse(a['unit_ratio']) for a in negative]
    currentW = [[x[:] for x in w] for w in initialW]
    currentU = [[1, 0] for _ in range(162)]
    sign = 1
    step_records = []
    for index, step in enumerate(steps):
        nonunit = []
        total_unit_ratio = [1, 0]
        for j in range(162):
            a = prepared('step'+str(index), j)
            if step['operation'] == 'double':
                denominator = product(currentW[j], currentW[j])
                unit = pair_mul(currentU[j], currentU[j])
            else:
                assert step['operation'] == 'add'
                denominator = product(currentW[j], initialW[j] if sign == 1 else negativeW[j])
                unit = pair_mul(currentU[j], [1, 0] if sign == 1 else minusU[j])
            currentW[j] = divide(a['weierstrass_coefficients'], denominator)
            currentU[j] = pair_inverse(pair_mul(unit, a['unit_ratio']))
            total_unit_ratio = pair_mul(total_unit_ratio, a['unit_ratio'])
            if a['degree']:
                nonunit.append({'label': labels[j], **a})
        sign = -sign
        assert sign == step['sign']
        step_records.append({'step_index_1based': index+1, 'principal_coefficient_sha256': step['principal_coefficient_sha256'],
                             'product_of_prepared_unit_ratios': total_unit_ratio, 'nonunit_disc_factors': nonunit})
    assert sign == 1 and [a['weierstrass_coefficients'] for a in ideals['current']] == currentW
    transition = []
    final_ratios = []
    for j in range(162):
        new, old, vS = prepared('end_new', j), prepared('end_old', j), prepared('vS', j)
        Wtarget = ideals['target'][j]['weierstrass_coefficients']
        assert Wtarget == vS['weierstrass_coefficients'], 'New moving S divisor should avoid all target discs'
        assert product(new['weierstrass_coefficients'], currentW[j]) == product(old['weierstrass_coefficients'], Wtarget)
        g = pair_mul(new['unit_ratio'], pair_inverse(pair_mul(old['unit_ratio'], vS['unit_ratio'])))
        f = pair_mul(currentU[j], pair_inverse(pair_mul(g, power(initial_h[j]['unit_ratio'], m))))
        assert f[0] % 47 == 1 and f[1] % 47 == 0
        final_ratios.append(f)
        transition.append({'label': labels[j], 'new': new, 'old': old, 'vS': vS,
                           'actual_prepared_g_ratio': g, 'complete_f_C_S_ratio': f})
    branch_norms = []
    for branch in range(3):
        value = [1, 0]
        for f in final_ratios[54*branch:54*(branch+1)]:
            value = pair_mul(value, f)
        branch_norms.append(value)
    complete = [1, 0]
    for value in branch_norms:
        complete = pair_mul(complete, value)
    assert complete[1] == 0 and complete[0] % 47 == 1
    z = (complete[0]-1) % r.Q
    logarithm = (z-z*z*pow(2, -1, r.Q)+z*z*z*pow(3, -1, r.Q)) % r.Q
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'class_name': args.class_name,
           'source_sha256': hashes, 'input_sha256': inputs, 'target_multiplier': m,
           'first_formal_point_sha256': first_sha, 'new_S_formal_point_sha256': expected_newsha,
           'actual_CM_support_disjointness': actual_disjointness, 'labels': labels,
           'actual_point_ideal_factors': ideals, 'initial_h_preparation': initial_h,
           'negative_section_preparation': negative, 'steps': step_records,
           'maximum_residual_degree': maximum_e, 'endpoint_transition': transition,
           'actual_branch_norms': branch_norms, 'actual_Hecke_norm': complete[0],
           'log_actual_Hecke_norm': logarithm, 'nonunit_divisions': 0,
           'formula': 'f_C,S=F_chain/(g_S*(f_b/f0)^m); evaluate on T2(A_family0(mC)) after exact whole-disc cancellation',
           'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'weierstrass_source_sha256': hashlib.sha256((folder/'p41_weierstrass_unit47.py').read_bytes()).hexdigest(),
           'status': 'complete actual CM Hecke norm on all162 moving/fixed target pairs; initial, negative, current and final ideals and all shifted unit factors verified; no full global height claimed'}
    sha, size = write_checkpoint(args.output, out)
    print('ACTUAL CM HECKE NORM COMPLETE', discriminant, complete[0], 'log', logarithm,
          'maxe', maximum_e, 'bytes', size, 'sha', sha,
          'seconds', round(time.monotonic()-started, 2),
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
