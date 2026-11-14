#!/usr/bin/env python3
"""True short divisor transport for 81*T2(mC)+12*(mC)+3mDb.

All three input points and the final point are complete Makdisi ideals.
The actual section functions and the final full-ideal isomorphism are retained.
The moving-divisor correction is exactly (v_S/f0)^(-93).
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time

LABELS = ['T2Y', 'Y', 'Db']
TARGET = [81, 12, 1]


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(',', ':')).encode()).hexdigest()


def release():
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass


def operation_plan():
    sign = 1
    vector = [1, 0, 0]
    plan = []
    for power in range(5, -1, -1):
        vector = [-2*a for a in vector]
        sign = -sign
        plan.append({'operation': 'double', 'power': power, 'output_expression': vector[:]})
        for index, coefficient in enumerate(TARGET):
            if not ((coefficient >> power) & 1):
                continue
            operand_sign = sign
            vector[index] += operand_sign
            vector = [-a for a in vector]
            sign = -sign
            plan.append({'operation': 'add', 'power': power, 'operand': LABELS[index],
                         'operand_sign': operand_sign, 'output_expression': vector[:]})
    assert vector == [sign*a for a in TARGET]
    if sign == -1:
        vector = [-a for a in vector]
        plan.append({'operation': 'flip', 'output_expression': vector[:]})
    assert vector == TARGET
    assert len(plan) == 12
    assert {op['operand'] for op in plan if op.get('operand_sign') == -1} == {'T2Y'}
    return plan


def prepare_chart(M0, omitted, r):
    keep = [i for i in range(820) if i not in omitted]
    assert len(keep) >= 712 and len(keep) > 5*126
    assert all(M0['tau'][i] in omitted for i in omitted)
    relabel = {j: i for i, j in enumerate(keep)}
    M = dict(M0)
    M['W'] = r.rows(M0['W'], keep)
    M['tau'] = [relabel[M0['tau'][i]] for i in keep]
    M['V2'], M['P2'], columns2, C2 = r.normalize(r.rows(M0['V2'], keep), 199)
    M['V3'], M['P3'], columns3, C3 = r.normalize(r.rows(M0['V3'], keep), 325)
    assert columns2 == list(range(199)) and columns3 == list(range(325))
    C2i, C3i = r.inverse_matrix(C2), r.inverse_matrix(C3)
    M['A2'] = r.mm(r.mm(C2i, M0['A2']), r.conjugate(C2))
    M['A3'] = r.mm(r.mm(C3i, M0['A3']), r.conjugate(C3))
    for V, A in [(M['W'], M['A1']), (M['V2'], M['A2']), (M['V3'], M['A3'])]:
        assert r.equal(r.mm(V, A), r.conjugate(r.rows(V, M['tau'])))
    chart = {'omitted_evaluation_rows_1based': [i+1 for i in sorted(omitted)],
             'remaining_rows': len(keep), 'faithfulness_degree_bound': 630,
             'V2_change_sha256': digest(r.to_json(C2)), 'V3_change_sha256': digest(r.to_json(C3)),
             'stored_basis': 'all points and sections in the original published R102/R110 bases'}
    return M, C2, C2i, C3, chart


def full_frame_transfer(Kold, Aold, Knew, Anew, M, rng, r, C2, norm):
    """g=t/s with div(g)=A_new_full-A_old_full; no moving-frame factor here."""
    import numpy as np
    Sold, Snew = r.mm(M['V2'], Kold), r.mm(M['V2'], Knew)
    for attempt in range(1, 101):
        seed_s, sc = r.rational_trace(Aold, rng)
        s = r.mm(Sold, sc)
        if not np.all(r.units(s)):
            continue
        seed_g, gc_ = r.rational_trace(Aold, rng)
        auxiliary = r.mm(Sold, gc_)
        ratio = r.mul(auxiliary, r.inverse_values(s))
        scaled = r.mul(ratio, Snew)
        residual = r.sub(scaled, r.mm(M['V2'], r.rows(scaled, M['P2'])))
        rows, cols = r.rank_pivots(residual)
        if len(rows) != 72:
            continue
        kernel, free, block = r.kernel_from_rows(r.rows(residual, rows), rows, cols)
        assert len(free) == 1 and r.iszero(r.mm(residual, kernel))
        transformed = r.mm(Anew, r.conjugate(kernel))
        scalar_action = r.rows(transformed, free)
        assert r.equal(r.mm(kernel, scalar_action), transformed)
        for _ in range(100):
            seed, small = r.rational_trace(scalar_action, rng)
            if bool(r.units(small)[0, 0]):
                break
        else:
            raise RuntimeError('No rational unit generator in full transport line')
        c = r.mm(kernel, small)
        assert r.equal(r.mm(Anew, r.conjugate(c)), c)
        t = r.mm(Snew, c)
        assert np.all(r.units(t))
        quotient = r.mul(t, r.inverse_values(s))
        products = r.mul(quotient, Sold)
        prows, pcols = r.rank_pivots(Snew)
        assert len(prows) == 73
        change = r.mm(r.inverse_matrix(r.rows(Snew, prows)), r.rows(products, prows))
        assert r.equal(products, r.mm(Snew, change))
        r.inverse_matrix(change)
        numerator = r.mm(C2, r.mm(Knew, c))
        denominator = r.mm(C2, r.mm(Kold, sc))
        n_norm, d_norm = norm(numerator, 2), norm(denominator, 2)
        result = n_norm*pow(d_norm, -1, r.Q) % r.Q
        return {'attempt': attempt, 'numerator_coefficients': r.to_json(numerator),
                'denominator_coefficients': r.to_json(denominator),
                'auxiliary_coefficients': r.to_json(r.mm(C2, r.mm(Kold, gc_))),
                'denominator_seed': r.to_json(seed_s), 'auxiliary_seed': r.to_json(seed_g),
                'rank_rows_1based': [i+1 for i in rows], 'rank_columns_1based': [i+1 for i in cols],
                'kernel_free_columns_1based': [i+1 for i in free], 'kernel_block': r.to_json(block),
                'isomorphism_matrix': r.to_json(change), 'isomorphism_determinant_unit': True,
                'numerator_norm': n_norm, 'denominator_norm': d_norm, 'actual_full_transfer_norm': result,
                'divisor': 'A_target_full-A_final_short_chain_full'}
    raise RuntimeError('No full endpoint ideal isomorphism')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--class-name', choices=['x12', 'x7'], required=True)
    parser.add_argument('--jets', type=Path, default=Path('/tmp/p41_t2_first_family_cubic47_checkpoint.json.gz'))
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--max-steps', type=int, default=12)
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model, flip
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import point_hash, restore_tuple, write_checkpoint
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_miller47 import addflip_with_section
    from p41_poincare_norms47 import pair_mul, pair_inverse
    start = time.monotonic()
    discriminant = int(args.class_name[1:])
    transport, tsha = read(folder/('data/p41_t2_cm'+str(discriminant)+'_formal_transport47_checkpoint.json.gz'))
    source_hashes = transport['source_sha256']
    source_points = transport['points_1based']
    input_hashes = {'CM_T2_transport': tsha}
    original = {}
    logs = {}
    for label, endpoint in zip(['Y', 'T2Y'], transport['endpoints']):
        K, A = r.from_json(endpoint['point_coordinates']), r.from_json(endpoint['point_frobenius'])
        assert point_hash(K, A) == endpoint['point_sha256']
        original[label] = (K, A)
        logs[label] = r.from_json(endpoint['target_logarithm'])
    expected_base_sha = transport['new_base_sha256']
    del transport, endpoint
    release()
    endpoints, esha = read(folder/'data/p41_translation_formal_endpoints47_checkpoint.json.gz')
    input_hashes['common_formal_endpoints'] = esha
    assert endpoints['source_sha256'] == source_hashes
    for label, key in [('Db', 'three_m_D_b'), ('target', 'three_m_D'+str(discriminant))]:
        e = endpoints['targets'][key]['exponentials']['positive']
        assert e['family_index'] == 1
        K, A = r.from_json(e['point_coordinates']), r.from_json(e['point_frobenius'])
        assert point_hash(K, A) == e['point_sha256']
        original[label] = (K, A)
        logs[label] = r.from_json(e['target_logarithm'])
    relation = r.add(r.add(tuple(a*81 % r.Q for a in logs['T2Y']), tuple(a*12 % r.Q for a in logs['Y'])), logs['Db'])
    assert r.equal(relation, logs['target'])
    del endpoints, e, logs
    release()
    baseS, bsha = read(folder/'data/p41_t2_cm_abel_base47_checkpoint.json.gz')
    assert bsha == expected_base_sha and baseS['source_sha256'] == source_hashes
    assert baseS['family']['points_1based'] == source_points
    vS = r.from_json(baseS['family']['v_coefficients'])
    input_hashes['S_base'] = bsha
    del baseS
    base, bsha = read(folder/'data/p41_hecke3_abel_bases_checkpoint.json.gz')
    assert base['source_sha256'] == source_hashes
    input_hashes['original_Abel_bases'] = bsha
    second_points = base['families'][1]['points_1based']
    first_points = base['families'][0]['points_1based']
    v1 = r.from_json(base['families'][1]['v_coefficients'])
    del base
    cm, cmsha = read(folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    input_hashes['CM_formal_endpoints'] = cmsha
    assert cm['source_sha256'] == source_hashes
    assert cm['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz'] == bsha
    e = cm['targets'][args.class_name]['targets']['m']['exponentials'][0]
    first_parameters = e['parameters']
    first_point_sha = e['point_sha256']
    del cm, e
    release()
    jets, jsha = read(args.jets)
    input_hashes['first_cubic'] = jsha
    assert jets['source_sha256'] == source_hashes and jets['points_1based'] == first_points
    W = [r.from_json(a) for a in jets['source_jets']['evaluation_coefficients']]
    del jets
    release()
    sources, hashes = load_sources(folder/'data')
    assert hashes == source_hashes
    M0 = make_model(sources)
    A2, A3 = M0['A2'], M0['A3']
    divs = sources[1]
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    f0 = r.mm(K1, r.column(divs['canonical_coefficients']))
    V2, V3 = section_jets(W, sources, M0, r)
    values = {1: W, 2: V2, 3: V3}
    parameters = r.from_json(first_parameters)
    t = parameters[0].T, parameters[1].T
    assert all(np.all(a % 47 == 0) for a in t)
    shifted = {}
    for degree, coefficients in values.items():
        total = r.zeros(54, coefficients[0][0].shape[1])
        for coefficient in reversed(coefficients):
            total = r.add(r.mul(total, t), coefficient)
        shifted[degree] = total
    constant = {degree: coefficients[0] for degree, coefficients in values.items()}

    def product(a):
        assert np.all(r.units(a))
        answer = [1, 0]
        for j in range(54):
            answer = pair_mul(answer, [int(a[0][j, 0]), int(a[1][j, 0])])
        return answer

    def raw_norm(coefficient, degree):
        answer = pair_mul(product(r.mm(shifted[degree], coefficient)), pair_inverse(product(r.mm(constant[degree], coefficient))))
        assert answer[1] == 0 and answer[0] % 47 == 1
        return answer[0]

    f0norm = raw_norm(f0, 1)

    def norm(coefficient, degree):
        return raw_norm(coefficient, degree)*pow(f0norm, -degree, r.Q) % r.Q

    hS_norm = norm(vS, 1)
    omitted = {i-1 for i in source_points+second_points}
    assert not (omitted & {i-1 for i in first_points})
    # These exact base sections have no residual zero at an evaluation point
    # outside the specified54 points, by the saved unit construction.
    for v, fixed in [(vS, source_points), (v1, second_points)]:
        outside = [i for i in range(820) if i+1 not in fixed]
        assert np.all(r.units(r.mm(r.rows(M0['W'], outside), v)))
    M, C2, C2i, C3, chart = prepare_chart(M0, omitted, r)
    basepoints = {label: (r.mm(C2i, K), A) for label, (K, A) in original.items()}
    for K, A in original.values():
        assert r.equal(r.mm(A2, r.conjugate(K)), r.mm(K, A))
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    plan = operation_plan()
    rng = random.Random(4104718300+discriminant)
    if args.checkpoint.exists():
        state, _ = read(args.checkpoint)
        assert state['source_sha256'] == hashes and state['input_sha256'] == input_hashes
        assert state['generating_source_sha256'] == source_sha and state['operation_plan'] == plan
        assert state['working_chart'] == chart and state['actual_vS_over_f0_norm'] == hS_norm
        K = r.mm(C2i, r.from_json(state['point_coordinates']))
        A = r.from_json(state['point_frobenius'])
        assert point_hash(r.mm(C2, K), A) == state['point_sha256']
        rng.setstate(restore_tuple(state['random_state']))
        print('ACTUAL FORMAL COMBINATION RESUME', discriminant, len(state['steps']), flush=True)
    else:
        K, A = basepoints['T2Y']
        state = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'class_name': args.class_name,
                 'source_sha256': hashes, 'input_sha256': input_hashes, 'generating_source_sha256': source_sha,
                 'working_chart': chart, 'basis_labels': LABELS, 'target_expression': TARGET,
                 'basis_point_sha256': {label: point_hash(*value) for label, value in original.items()},
                 'operation_plan': plan, 'steps': [], 'current_expression': [1, 0, 0],
                 'actual_Fbuild_norm': 1, 'actual_vS_over_f0_norm': hS_norm,
                 'first_formal_point_sha256': first_point_sha, 'first_parameters': first_parameters,
                 'vS_coefficients': r.to_json(vS), 'base_f0_coefficients': r.to_json(f0),
                 'principal_function_recurrence': 'F_new=(F_left*F_right*(section/f0^3))^-1; flip F_new=(F_old*(section/f0^2))^-1',
                 'status': 'actual complete-point short combination in progress; no final frame or height claimed'}
    # Keep only small independent arrays and the reduced evaluation chart.
    del sources, M0, divs, K1, values, W, V2, V3, original, v1, vS, parameters, t, coefficients, coefficient
    release()

    def checkpoint(message):
        state['point_coordinates'] = r.to_json(r.mm(C2, K))
        state['point_frobenius'] = r.to_json(A)
        state['point_sha256'] = point_hash(r.mm(C2, K), A)
        state['random_state'] = rng.getstate()
        sha, size = write_checkpoint(args.checkpoint, state)
        print(message, discriminant, 'steps', len(state['steps']), 'bytes', size, 'sha', sha,
              'seconds', round(time.monotonic()-start, 2),
              'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)

    if 'negative_T2Y' not in state:
        KP, AP = basepoints['T2Y']
        KN, AN, rec = flip(r.mm(M['V2'], KP), AP, M, rng, 'formal combination negative T2Y')
        q = r.mm(C2, r.mm(KP, r.column(rec['f_coefficients'])))
        assert r.equal(r.mm(A2, r.conjugate(q)), q)
        state['negative_T2Y'] = {'point_coordinates': r.to_json(r.mm(C2, KN)), 'point_frobenius': r.to_json(AN),
                                'point_sha256': point_hash(r.mm(C2, KN), AN),
                                'quadratic_coefficients': r.to_json(q), 'actual_quadratic_norm': norm(q, 2),
                                'flip_record': rec}
        checkpoint('ACTUAL FORMAL COMBINATION NEGATIVE SAVED')
    neg = state['negative_T2Y']
    negative = r.mm(C2i, r.from_json(neg['point_coordinates'])), r.from_json(neg['point_frobenius'])
    assert point_hash(r.mm(C2, negative[0]), negative[1]) == neg['point_sha256']
    negative_norm = pow(neg['actual_quadratic_norm'], -1, r.Q)
    for index in range(len(state['steps']), min(len(plan), args.max_steps)):
        op = plan[index]
        before = state['current_expression'][:]
        previous_norm = state['actual_Fbuild_norm']
        if op['operation'] == 'double':
            K, A, section, rec = addflip_with_section(K, A, K, A, M, rng, 'formal combination double '+str(index+1), r, same=True)
            degree, f = 3, r.mm(C3, section)
            expected = [-2*a for a in before]
            operand_norm = previous_norm
        elif op['operation'] == 'add':
            KP, AP = basepoints[op['operand']] if op['operand_sign'] == 1 else negative
            K, A, section, rec = addflip_with_section(K, A, KP, AP, M, rng, 'formal combination add '+str(index+1), r)
            degree, f = 3, r.mm(C3, section)
            expected = before[:]
            expected[LABELS.index(op['operand'])] += op['operand_sign']
            expected = [-a for a in expected]
            operand_norm = 1 if op['operand_sign'] == 1 else negative_norm
        else:
            assert op['operation'] == 'flip'
            previous = K
            K, A, rec = flip(r.mm(M['V2'], K), A, M, rng, 'formal combination final flip')
            degree = 2
            f = r.mm(C2, r.mm(previous, r.column(rec['f_coefficients'])))
            expected = [-a for a in before]
            operand_norm = 1
        assert expected == op['output_expression']
        assert r.equal(r.mm(A2 if degree == 2 else A3, r.conjugate(f)), f)
        n = norm(f, degree)
        cumulative = pow(previous_norm*operand_norm % r.Q*n % r.Q, -1, r.Q)
        encoded = r.to_json(f)
        rec.update(op)
        rec.update({'input_expression': before, 'principal_section_degree': degree,
                    'principal_section_coefficients': encoded, 'principal_coefficient_sha256': digest(encoded),
                    'actual_principal_norm': n, 'actual_Fbuild_norm': cumulative,
                    'point_sha256': point_hash(r.mm(C2, K), A)})
        state['steps'].append(rec)
        state['current_expression'] = expected
        state['actual_Fbuild_norm'] = cumulative
        checkpoint('ACTUAL FORMAL COMBINATION CHECKPOINT')
    if len(state['steps']) == len(plan):
        assert state['current_expression'] == TARGET
        target, Atarget = basepoints['target']
        if 'full_endpoint_transfer' not in state:
            state['full_endpoint_transfer'] = full_frame_transfer(K, A, target, Atarget, M, rng, r, C2, norm)
        gnorm = state['full_endpoint_transfer']['actual_full_transfer_norm']
        Fsigma = state['actual_Fbuild_norm']*pow(gnorm, -1, r.Q)*pow(hS_norm, -93, r.Q) % r.Q
        assert Fsigma % 47 == 1
        z = (Fsigma-1) % r.Q
        logarithm = (z-z*z*pow(2, -1, r.Q)+z*z*z*pow(3, -1, r.Q)) % r.Q
        state.update({'actual_Fsigma_norm': Fsigma, 'log_actual_Fsigma_norm': logarithm,
                      'actual_formula': 'F_sigma=F_build/(g_full*(v_S/f0)^93)',
                      'principal_divisor': '81*A_S(T2mC)+12*A_S(mC)+A_family1(3mDb)-A_family1(3mD)',
                      'family1_frame_cancellation': 'Db and target have the same v1/f0; their factors cancel exactly',
                      'status': 'complete actual short principal transport and norm on first CM formal frame; all sections, full ideal isomorphism and93-fold frame correction retained; no global height claimed'})
        checkpoint('ACTUAL FORMAL COMBINATION COMPLETE')


if __name__ == '__main__':
    main()
