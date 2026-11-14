#!/usr/bin/env python3
"""Actual width-five signed-window Miller DAG for the common point3D_b.

All nodes retain their actual principal function and exact integer exponent.
The precomputed actual points are saved once; the running checkpoint contains
only its current point, every function node, the fixed DAG cursor and RNG.
The original binary driver and both running CM chains are untouched.
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


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def digest(data):
    return hashlib.sha256(json.dumps(data, separators=(',', ':')).encode()).hexdigest()


def signed_digits(integer, width=5):
    value = integer
    digits = []
    while value:
        digit = 0
        if value & 1:
            digit = value % (1 << width)
            if digit >= 1 << (width-1):
                digit -= 1 << width
            value -= digit
        digits.append(digit)
        value //= 2
    return digits


def make_plan(integer):
    digits = signed_digits(integer)
    assert len(digits) == 303 and digits[-1] > 0
    assert max(abs(x) for x in digits) == 15
    plan = []
    exponents = {0: 1}

    def node(operation, left, right=None, phase='precompute', power=None, digit=0):
        number = len(plan)+1
        exponent = -exponents[left] if operation == 'flip' else -(exponents[left]+exponents[right])
        item = {'node': number, 'operation': operation, 'left': left,
                'exponent': exponent, 'phase': phase, 'remaining_power': power, 'signed_digit': digit}
        if right is not None:
            item['right'] = right
        plan.append(item)
        exponents[number] = exponent
        return number

    positive = {1: 0}
    negative = {1: node('flip', 0)}
    negative[2] = node('double', 0, 0)
    positive[2] = node('flip', negative[2])
    for odd in range(3, 16, 2):
        negative[odd] = node('addflip', positive[odd-2], positive[2])
        positive[odd] = node('flip', negative[odd])
    precompute_count = len(plan)
    assert precompute_count == 17
    current = positive[digits[-1]]
    sign, magnitude = 1, digits[-1]
    for power in range(len(digits)-2, -1, -1):
        digit = digits[power]
        current = node('double', current, current, 'window', power, digit)
        sign, magnitude = -sign, 2*magnitude
        if digit:
            operand = sign*digit
            point = positive[operand] if operand > 0 else negative[-operand]
            current = node('addflip', current, point, 'window', power, digit)
            sign, magnitude = -sign, magnitude+digit
        assert magnitude > 0 and exponents[current] == sign*magnitude
    assert magnitude == integer
    if sign == -1:
        current = node('flip', current, phase='final_sign')
    assert exponents[current] == integer
    return digits, plan, precompute_count, current


def independently_expand(plan, integer):
    """An independent recurrence on integer expressions, with no elliptic data."""
    coefficients = {0: 1}
    counts = {'flip': 0, 'double': 0, 'addflip': 0}
    for expected_number, item in enumerate(plan, 1):
        assert item['node'] == expected_number and item['left'] < expected_number
        if item['operation'] == 'flip':
            coefficient = -coefficients[item['left']]
            assert 'right' not in item
        else:
            assert item['right'] < expected_number
            coefficient = -coefficients[item['left']]-coefficients[item['right']]
            if item['operation'] == 'double':
                assert item['left'] == item['right']
        assert coefficient == item['exponent']
        coefficients[expected_number] = coefficient
        counts[item['operation']] += 1
    assert coefficients[len(plan)] == integer
    assert counts == {'flip': 9, 'double': 303, 'addflip': 57}
    assert len(plan) == 369
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--initial', type=Path, default=Path('/tmp/p41_translation_build47_complete.json.gz'))
    parser.add_argument('--checkpoint', type=Path, default=Path('/tmp/p41_translation_window47_rolling.json.gz'))
    parser.add_argument('--precomputation', type=Path, default=Path('/tmp/p41_translation_window47_precomputation.json.gz'))
    parser.add_argument('--max-nodes', type=int, default=369)
    parser.add_argument('--plan-only', action='store_true')
    parser.add_argument('--plan-output', type=Path, default=Path('/tmp/p41_translation_window47_plan.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    published, published_sha = read(folder/'data/p41_formal47_multiplication_saved.json.gz')
    multiplier = published['target_multiplier']
    assert multiplier.bit_length() == 304 and multiplier % 47 == 9
    digits, plan, precompute_count, final_node = make_plan(multiplier)
    counts = independently_expand(plan, multiplier)
    assert sum(d*(1 << k) for k, d in enumerate(digits)) == multiplier
    plan_sha = digest(plan)
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.plan_only:
        output = {'target_multiplier': multiplier, 'published_multiplier_sha256': published_sha,
                  'width': 5, 'signed_digits_ascending': digits, 'plan': plan,
                  'plan_sha256': plan_sha, 'counts': counts, 'precomputation_nodes': precompute_count,
                  'generating_source_sha256': source_sha,
                  'status': 'independent integer DAG expansion equals the exact published m; no group operations in this plan check'}
        packed = gzip.compress((json.dumps(output, sort_keys=True, separators=(',', ':'))+'\n').encode(), mtime=0)
        args.plan_output.write_bytes(packed)
        print('INDEPENDENT INTEGER WINDOW DAG PASS', counts, 'nodes', len(plan),
              'plan', plan_sha, 'file', hashlib.sha256(packed).hexdigest(), 'bytes', len(packed), flush=True)
        return
    sys.path.insert(0, str(folder))
    sys.path.insert(0, str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model, flip
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint, restore_tuple, point_hash, zero_test_mod47
    from p41_translation_build47 import prepare_chart, TARGET
    started = time.monotonic()
    sources, hashes = load_sources(folder/'data')
    assert published['source_sha256'] == hashes
    M0 = make_model(sources)
    initial, initial_sha = read(args.initial)
    assert initial['source_sha256'] == hashes and initial['current_expression'] == TARGET
    assert len(initial['steps']) == 24 and initial['status'].startswith('complete actual integral point 3*D_b')
    chart = initial['working_chart']
    M, C2, C2i, C3 = prepare_chart(M0, chart, r)
    original_A2, original_A3 = M0['A2'], M0['A3']
    Kinitial, Ainitial = r.from_json(initial['point_coordinates']), r.from_json(initial['point_frobenius'])
    initial_point_sha = initial['point_sha256']
    assert point_hash(Kinitial, Ainitial) == initial_point_sha
    assert r.equal(r.mm(original_A2, r.conjugate(Kinitial)), r.mm(Kinitial, Ainitial))
    helper_sha = hashlib.sha256(Path(prepare_chart.__code__.co_filename).read_bytes()).hexdigest()
    rng = random.Random(4104717805)
    cache = {0: (r.mm(C2i, Kinitial), Ainitial)}
    if args.checkpoint.exists():
        data, previous_sha = read(args.checkpoint)
        assert data['source_sha256'] == hashes and data['initial_source_sha256'] == initial_sha
        assert data['initial_point_sha256'] == initial_point_sha and data['plan_sha256'] == plan_sha
        assert data['generating_source_sha256'] == source_sha and data['chart_helper_source_sha256'] == helper_sha
        assert data['target_multiplier'] == multiplier and data['working_chart'] == chart
        assert data['published_multiplier_sha256'] == published_sha
        rng.setstate(restore_tuple(data['random_state']))
        if data.get('precomputation_sha256'):
            precomputed, pre_sha = read(args.precomputation)
            assert pre_sha == data['precomputation_sha256']
            assert precomputed['plan_sha256'] == plan_sha and precomputed['source_sha256'] == hashes
            assert precomputed['initial_source_sha256'] == initial_sha and precomputed['initial_point_sha256'] == initial_point_sha
            assert precomputed['generating_source_sha256'] == source_sha and precomputed['working_chart'] == chart
            encoded_cache = precomputed['points']
        else:
            encoded_cache = data['precomputation_cache']
        cache = {}
        for key, record in encoded_cache.items():
            old, action = r.from_json(record['point_coordinates']), r.from_json(record['point_frobenius'])
            assert point_hash(old, action) == record['point_sha256']
            cache[int(key)] = r.mm(C2i, old), action
        current_node = data['current_node']
        current_K, current_A = r.mm(C2i, r.from_json(data['point_coordinates'])), r.from_json(data['point_frobenius'])
        assert point_hash(r.mm(C2, current_K), current_A) == data['point_sha256']
        for expected, record in zip(plan, data['nodes']):
            for key, value in expected.items():
                assert record[key] == value
            assert digest(record['principal_section_coefficients']) == record['principal_coefficient_sha256']
        assert current_node == len(data['nodes'])
        if data.get('precomputation_sha256'):
            del precomputed
        del encoded_cache, record, old, action
        print('ACTUAL COMMON WINDOW RESUME', current_node, 'of369 nodes', flush=True)
    else:
        current_node, (current_K, current_A) = 0, cache[0]
        data = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'point_label': 'three_D_b',
                'source_sha256': hashes, 'initial_source_sha256': initial_sha, 'initial_point_sha256': initial_point_sha,
                'published_multiplier_sha256': published_sha, 'target_multiplier': multiplier,
                'generating_source_sha256': source_sha, 'chart_helper_source_sha256': helper_sha,
                'working_chart': chart, 'width': 5, 'signed_digits_ascending': digits,
                'plan_sha256': plan_sha, 'plan': plan, 'integer_counts': counts,
                'nodes': [], 'precomputation_sha256': None,
                'actual_initial_transport': 'h_D=R_g1^2*(f_b/f0)^324/F_build, div(h_D)=A_initial-3D_b',
                'function_invariant': 'div(F_node)=exponent_node*A_initial-A_node; F_0=1; addflip uses inverse(F_left*F_right*s/f0^3); flip uses inverse(F_left*s/f0^2)',
                'true_final_function': 'f_D=F_final/(g_transport*h_D^m), div(f_D)=3mD_b-A_formal',
                'status': 'actual common3Db width5 signed-window SLP in progress; no final height claimed'}
    del sources, M0, initial, published, Kinitial
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass
    print('ACTUAL COMMON WINDOW MEMORY RELEASE', '; '.join(line for line in Path('/proc/self/status').read_text().splitlines()
          if line.startswith(('VmRSS:', 'VmHWM:'))), flush=True)

    def encode_point(point):
        coordinates, action = point
        original = r.mm(C2, coordinates)
        return {'point_coordinates': r.to_json(original), 'point_frobenius': r.to_json(action),
                'point_sha256': point_hash(original, action)}

    def checkpoint(message):
        data.update(encode_point((current_K, current_A)))
        data['current_node'] = current_node
        data['current_exponent'] = 1 if current_node == 0 else plan[current_node-1]['exponent']
        data['actual_sign'] = 1 if data['current_exponent'] > 0 else -1
        nxt = plan[current_node] if current_node < len(plan) else None
        data['window_cursor'] = None if nxt is None else {k: nxt[k] for k in ['node', 'phase', 'remaining_power', 'operation']}
        data['random_state'] = rng.getstate()
        if not data.get('precomputation_sha256'):
            data['precomputation_cache'] = {str(k): encode_point(v) for k, v in cache.items()}
        sha, size = write_checkpoint(args.checkpoint, data)
        print(message, current_node, 'nodes', 'bytes', size, 'sha', sha,
              'seconds', round(time.monotonic()-started, 2),
              'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)

    def point(number):
        if number in cache:
            return cache[number]
        assert number == current_node
        return current_K, current_A

    if current_node == 0:
        checkpoint('ACTUAL COMMON WINDOW INITIAL SAVED')
    for item in plan[current_node:min(len(plan), args.max_nodes)]:
        KP, AP = point(item['left'])
        if item['operation'] == 'flip':
            out_K, out_A, details = flip(r.mm(M['V2'], KP), AP, M, rng, 'common window flip '+str(item['node']))
            original_section = r.mm(C2, r.mm(KP, r.column(details['f_coefficients'])))
            degree = 2
            record = {k: value for k, value in details.items() if k not in ['kernel_block', 'frobenius_matrix']}
            record['reconstructible_kernel_block_sha256'] = digest(details['kernel_block'])
            del details
        else:
            KQ, AQ = point(item['right'])
            out_K, out_A, section, record = addflip_with_section(KP, AP, KQ, AQ, M, rng,
                'common window '+item['operation']+' '+str(item['node']), r, same=item['operation'] == 'double')
            original_section = r.mm(C3, section)
            degree = 3
        assert r.equal(r.mm(original_A2 if degree == 2 else original_A3, r.conjugate(original_section)), original_section)
        encoded = r.to_json(original_section)
        record.update(item)
        record.update({'principal_section_degree': degree, 'principal_section_coefficients': encoded,
                       'principal_coefficient_sha256': digest(encoded),
                       'point_sha256': point_hash(r.mm(C2, out_K), out_A)})
        data['nodes'].append(record)
        current_node, current_K, current_A = item['node'], out_K, out_A
        if item['phase'] == 'precompute':
            cache[current_node] = current_K, current_A
        if current_node == precompute_count:
            precomputed = {'source_sha256': hashes, 'initial_source_sha256': initial_sha,
                           'initial_point_sha256': initial_point_sha, 'generating_source_sha256': source_sha,
                           'plan_sha256': plan_sha, 'working_chart': chart,
                           'points': {str(k): encode_point(v) for k, v in cache.items()},
                           'nodes': data['nodes'][:], 'random_state': rng.getstate(),
                           'status': 'complete actual signed odd multiples through15 and all principal functions; cached once for the window SLP'}
            pre_sha, pre_size = write_checkpoint(args.precomputation, precomputed)
            data['precomputation_sha256'] = pre_sha
            data.pop('precomputation_cache', None)
            del precomputed
            gc.collect()
            print('ACTUAL COMMON WINDOW PRECOMPUTATION COMPLETE', pre_size, pre_sha, flush=True)
        checkpoint('ACTUAL COMMON WINDOW CHECKPOINT')
    if current_node == final_node:
        assert data['current_exponent'] == multiplier and len(data['nodes']) == 369
        data['zero_test_mod47_in_working_chart'] = zero_test_mod47(current_K, M)
        data['status'] = 'complete actual m*(3D_b) point and full width5 signed-window DAG; all360 AddFlip and9 flip nodes retained; zero reduction PASS; true formal endpoint and height evaluation remain'
        checkpoint('ACTUAL COMMON WINDOW COMPLETE')


if __name__ == '__main__':
    main()
