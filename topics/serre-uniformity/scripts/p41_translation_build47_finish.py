#!/usr/bin/env python3
"""Memory-bounded resumption of the actual short SLP for 3*D_b, retaining its complete initial transport.

The five input divisors are the actual CM12/CM7 based representatives,
B_minus8, B_minus4 and U_b.  The final point differs from 3*D_b by the
explicit function R_omega^2*h^324/F_build.  This is a resumable construction;
every principal numerator is saved in the original R102/R110 basis.
"""
import argparse
import gzip
import gc
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time

LABELS = ['C12', 'C7', 'B8', 'B4', 'Ub']
TARGET = [486, -162, -81, -6, 17]


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(',', ':')).encode()).hexdigest()


def operation_plan():
    sign = 1
    vector = [1, 0, 0, 0, 0]
    operations = []
    for power in range(7, -1, -1):
        vector = [-2*a for a in vector]
        sign = -sign
        operations.append({'operation': 'double', 'power': power, 'output_expression': vector[:]})
        for index, coefficient in enumerate(TARGET):
            if not ((abs(coefficient) >> power) & 1):
                continue
            operand_sign = sign*(1 if coefficient > 0 else -1)
            vector[index] += operand_sign
            vector = [-a for a in vector]
            sign = -sign
            operations.append({'operation': 'add', 'power': power, 'operand': LABELS[index],
                               'operand_sign': operand_sign, 'output_expression': vector[:]})
    assert vector == [sign*a for a in TARGET]
    if sign == -1:
        vector = [-a for a in vector]
        operations.append({'operation': 'flip', 'output_expression': vector[:]})
    assert vector == TARGET
    assert sum(op['operation'] == 'double' for op in operations) == 8
    assert sum(op['operation'] == 'add' for op in operations) == 15
    return operations


def prepare_chart(M0, chart, r):
    """Exactly the published CM7 faithful819-point chart."""
    omitted = {i-1 for i in chart['omitted_evaluation_rows_1based']}
    keep = [i for i in range(820) if i not in omitted]
    assert omitted == {253} and len(keep) == 819
    assert all(M0['tau'][i] in omitted for i in omitted)
    relabel = {j: i for i, j in enumerate(keep)}
    M = dict(M0)
    M['W'] = r.rows(M0['W'], keep)
    M['tau'] = [relabel[M0['tau'][i]] for i in keep]
    M['V2'], M['P2'], cols2, C2 = r.normalize(r.rows(M0['V2'], keep), 199)
    M['V3'], M['P3'], cols3, C3 = r.normalize(r.rows(M0['V3'], keep), 325)
    assert cols2 == list(range(199)) and cols3 == list(range(325))
    assert digest(r.to_json(C2)) == chart['V2_change_sha256']
    assert digest(r.to_json(C3)) == chart['V3_change_sha256']
    C2i, C3i = r.inverse_matrix(C2), r.inverse_matrix(C3)
    M['A2'] = r.mm(r.mm(C2i, M0['A2']), r.conjugate(C2))
    M['A3'] = r.mm(r.mm(C3i, M0['A3']), r.conjugate(C3))
    for V, A in [(M['W'], M['A1']), (M['V2'], M['A2']), (M['V3'], M['A3'])]:
        assert r.equal(r.mm(V, A), r.conjugate(r.rows(V, M['tau'])))
    return M, C2, C2i, C3


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--points', type=Path, default=Path('/tmp/p41_translation_points47_checkpoint.json.gz'))
    parser.add_argument('--cm12-prefix', type=Path)
    parser.add_argument('--cm7-prefix', type=Path)
    parser.add_argument('--canonical', type=Path)
    parser.add_argument('--checkpoint', type=Path, default=Path('/tmp/p41_translation_build47_rolling.json.gz'))
    parser.add_argument('--max-steps', type=int)
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model, flip
    from p41_cm4_divisor47 import kernel
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint, restore_tuple, point_hash
    started = time.monotonic()
    sources, hashes = load_sources(folder/'data')
    M0 = make_model(sources)
    original_A2, original_A3 = M0['A2'], M0['A3']
    initial, initial_sha = read(folder/'data/p41_cm_based_points47_checkpoint.json.gz')
    points, points_sha = read(args.points)
    cp12, cp12_sha = read(args.cm12_prefix or folder/'data/p41_cm12_slp47_30_fixed.json.gz')
    cp7, cp7_sha = read(args.cm7_prefix or folder/'data/p41_cm7_slp47_15_fixed.json.gz')
    canonical, canonical_sha = read(args.canonical or folder/'data/p41_canonical_restriction47_candidate1_compact.json.gz')
    for obj in [initial, points, cp12, cp7, canonical]:
        assert obj['source_sha256'] == hashes
    assert cp12['initial_source_sha256'] == cp7['initial_source_sha256'] == initial_sha
    input_hashes = {'actual_based_CM_initial': initial_sha, 'actual_B8_Ub': points_sha,
                    'CM12_negative_source': cp12_sha, 'CM7_negative_source': cp7_sha,
                    'actual_canonical_g1': canonical_sha}
    divs = sources[1]
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'], divs['canonical_kernel_block']))
    fc = r.mm(K1, r.column(divs['canonical_coefficients']))
    g1c = r.mm(K1, r.from_json(canonical['canonical_coefficients']))
    assert r.to_json(fc) == canonical['denominator_coefficients']
    for coefficient in [fc, g1c]:
        assert r.equal(r.mm(M0['A1'], r.conjugate(coefficient)), coefficient)
    chart = cp7['working_chart']
    M, C2, C2i, C3 = prepare_chart(M0, chart, r)
    base = {}
    for label, name in [('C12', 'P_minus12'), ('C7', 'P_minus7')]:
        rec = next(a for a in initial['records'] if a['point_label'] == name)
        base[label] = (r.from_json(rec['point_coordinates']), r.from_json(rec['point_frobenius']))
    for label, name in [('B8', 'B_minus8'), ('Ub', 'U_b')]:
        rec = next(a for a in points['records'] if a['point_label'] == name)
        base[label] = (r.from_json(rec['point_coordinates']), r.from_json(rec['point_frobenius']))
    base['B4'] = (M0['B'], M0['AB'])
    for K, A in base.values():
        assert r.equal(r.mm(original_A2, r.conjugate(K)), r.mm(K, A))
    positive = {label: (r.mm(C2i, K), A) for label, (K, A) in base.items()}
    negative = {}
    qcoeff = {}
    for label, cp in [('C12', cp12), ('C7', cp7)]:
        K, A = r.from_json(cp['negative_point_coordinates']), r.from_json(cp['negative_point_frobenius'])
        assert point_hash(K, A) == cp['negative_point_sha256']
        assert point_hash(*base[label]) == cp['initial_point_sha256']
        negative[label] = (r.mm(C2i, K), A)
        qcoeff[label] = cp['negative_quadratic_coefficients']
    old = sources[3]
    Kneg = r.from_json(kernel(199, old['negative_rank_columns_1based'], old['negative_free_columns_1based'], old['negative_kernel_block']))
    Aneg = r.from_json(old['negative_frobenius_matrix'])
    assert r.equal(r.mm(original_A2, r.conjugate(Kneg)), r.mm(Kneg, Aneg))
    negative['B4'] = (r.mm(C2i, Kneg), Aneg)
    qcoeff['B4'] = r.to_json(r.mm(M0['B'], r.column(old['negative_flip_section_seeds_and_coefficients'][0][1])))
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rng = random.Random(4104717501)
    plan = operation_plan()
    if args.checkpoint.exists():
        data, checkpoint_sha = read(args.checkpoint)
        assert data['source_sha256'] == hashes and data['input_sha256'] == input_hashes
        assert data['generating_source_sha256'] in [source_sha, 'd61260cd44a0e038563ff78938dbbb0c5375097cc76bbb521c95075c72e60294'] and data['operation_plan'] == plan
        if data['generating_source_sha256'] != source_sha:
            data.setdefault('driver_history', []).append({'previous_source_sha256': data['generating_source_sha256'], 'replacement_source_sha256': source_sha, 'reason': '137 recovery; release decoded sources and unused original evaluation matrices, with unchanged group operations, RNG and principal-section bases'})
            data['generating_source_sha256'] = source_sha
        assert data['working_chart'] == chart
        rng.setstate(restore_tuple(data['random_state']))
        for label, rec in data['new_negative_points'].items():
            K, A = r.from_json(rec['point_coordinates']), r.from_json(rec['point_frobenius'])
            assert point_hash(K, A) == rec['point_sha256']
            negative[label] = (r.mm(C2i, K), A)
            qcoeff[label] = rec['negative_quadratic_coefficients']
        K, A = r.mm(C2i, r.from_json(data['point_coordinates'])), r.from_json(data['point_frobenius'])
        assert point_hash(r.mm(C2, K), A) == data['point_sha256']
    else:
        K, A = positive['C12']
        data = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
                'input_sha256': input_hashes, 'generating_source_sha256': source_sha,
                'point_label': 'three_D_b', 'working_chart': chart,
                'basis_labels': LABELS, 'target_expression': TARGET, 'current_expression': [1, 0, 0, 0, 0],
                'operation_plan': plan, 'steps': [], 'new_negative_points': {},
                'basis_point_sha256': {label: point_hash(*base[label]) for label in LABELS},
                'initial_h_coefficients': initial['f_b_coefficients'],
                'base_f0_coefficients': r.to_json(fc), 'actual_g1_coefficients': r.to_json(g1c),
                'principal_function_recurrence': 'F_R=(F_P*F_Q*(s/f0^3))^(-1); for a final flip use F_R=(F_P*(s/f0^2))^(-1); F_positive_basis=1 and F_negative_basis=(q_basis/f0^2)^(-1)',
                'actual_initial_transport': 'h_D=R_g1^2*(f_b/f0)^324/F_build; div(h_D)=A_new-3*D_b',
                'actual_R_function': 'R_g1=Delta_E/W_g1^6=(dj/omega_g1)^6/(j^4*(j-1728)^3)',
                'canonical_change_identity': 'R_g1=R_f0*(g1/f0)^(-6); h_D=R_f0^2*(g1/f0)^(-12)*(f_b/f0)^324/F_build',
                'actual_base_divisor': 'D_b=162*P_minus12+8*P_minus3-27*Q2+4*K_g1',
                'point_coordinates': r.to_json(base['C12'][0]), 'point_frobenius': r.to_json(A),
                'point_sha256': point_hash(*base['C12']), 'random_state': rng.getstate(),
                'status': 'actual common-translation short SLP in progress; no long multiplication or height claimed'}

    # All needed sections/points have independent integer-array copies.
    # Do not retain decoded source dictionaries or the original820 matrices
    # through the memory-heavy exact group-operation loop.
    del sources, M0, initial, points, cp12, cp7, cp, canonical, old, rec
    gc.collect()

    def checkpoint(message):
        data['point_coordinates'] = r.to_json(r.mm(C2, K))
        data['point_frobenius'] = r.to_json(A)
        data['point_sha256'] = point_hash(r.mm(C2, K), A)
        data['random_state'] = rng.getstate()
        data['negative_basis_quadratic_coefficients'] = qcoeff
        sha, size = write_checkpoint(args.checkpoint, data)
        print(message, 'steps', len(data['steps']), 'bytes', size, 'sha', sha,
              'seconds', round(time.monotonic()-started, 2),
              'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)

    for label in ['B8', 'Ub']:
        if label in negative:
            continue
        KB, AB = positive[label]
        KN, AN, record = flip(r.mm(M['V2'], KB), AB, M, rng, 'true negative '+label)
        q = r.mm(base[label][0], r.column(record['f_coefficients']))
        assert r.equal(r.mm(original_A2, r.conjugate(q)), q)
        negative[label] = (KN, AN)
        qcoeff[label] = r.to_json(q)
        data['new_negative_points'][label] = {'point_coordinates': r.to_json(r.mm(C2, KN)),
                                              'point_frobenius': r.to_json(AN),
                                              'point_sha256': point_hash(r.mm(C2, KN), AN),
                                              'negative_quadratic_coefficients': r.to_json(q),
                                              'flip_record': record}
        checkpoint('ACTUAL COMMON TRANSLATION NEGATIVE '+label)
    limit = min(len(plan), args.max_steps if args.max_steps is not None else len(plan))
    for index in range(len(data['steps']), limit):
        op = plan[index]
        before = data['current_expression'][:]
        if op['operation'] == 'double':
            K, A, section, record = addflip_with_section(K, A, K, A, M, rng, 'common translation double '+str(index+1), r, same=True)
            degree = 3
            original_section = r.mm(C3, section)
            expected = [-2*a for a in before]
        elif op['operation'] == 'add':
            QP, AQ = (positive if op['operand_sign'] == 1 else negative)[op['operand']]
            K, A, section, record = addflip_with_section(K, A, QP, AQ, M, rng, 'common translation add '+str(index+1), r)
            degree = 3
            original_section = r.mm(C3, section)
            expected = before[:]
            expected[LABELS.index(op['operand'])] += op['operand_sign']
            expected = [-a for a in expected]
        else:
            assert op['operation'] == 'flip'
            previous = K
            K, A, record = flip(r.mm(M['V2'], K), A, M, rng, 'common translation final positive flip')
            degree = 2
            original_section = r.mm(C2, r.mm(previous, r.column(record['f_coefficients'])))
            expected = [-a for a in before]
        assert expected == op['output_expression']
        assert r.equal(r.mm(original_A2 if degree == 2 else original_A3, r.conjugate(original_section)), original_section)
        encoded = r.to_json(original_section)
        record.update(op)
        record.update({'step_index_1based': index+1, 'input_expression': before,
                       'principal_section_degree': degree, 'principal_section_coefficients': encoded,
                       'principal_coefficient_sha256': digest(encoded),
                       'point_sha256': point_hash(r.mm(C2, K), A)})
        data['steps'].append(record)
        data['current_expression'] = expected
        checkpoint('ACTUAL COMMON TRANSLATION SHORT CHECKPOINT')
    if len(data['steps']) == len(plan):
        assert data['current_expression'] == TARGET
        data['status'] = 'complete actual integral point 3*D_b with retained short SLP F_build and explicit initial transport R_g1^2*h^324/F_build; long multiplication and height remain to compute'
        checkpoint('ACTUAL COMMON TRANSLATION SHORT COMPLETE')


if __name__ == '__main__':
    main()
