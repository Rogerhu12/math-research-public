#!/usr/bin/env python3
"""Resumable actual Miller SLP for the common point 3*D_b.

The starting divisor is the completed short-combination representative.
Its explicit transport h_D=R_g1^2*h^324/F_build is retained by hash; this
driver does not silently replace the starting divisor by 3*D_b itself.
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--initial', type=Path, default=Path('/tmp/p41_translation_build47_complete.json.gz'))
    parser.add_argument('--checkpoint', type=Path, default=Path('/tmp/p41_translation_slp47_rolling.json.gz'))
    parser.add_argument('--max-bits', type=int, default=304)
    parser.add_argument('--save-bits', type=int, default=1)
    args = parser.parse_args()
    assert args.save_bits >= 1
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    sys.path.insert(0, str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model, flip
    from p41_poincare_miller47 import addflip_with_section
    from p41_formal47_multiply import write_checkpoint, restore_tuple, point_hash, zero_test_mod47
    from p41_translation_build47 import prepare_chart, TARGET, operation_plan
    started = time.monotonic()
    sources, hashes = load_sources(folder/'data')
    M0 = make_model(sources)
    initial, initial_sha = read(args.initial)
    assert initial['source_sha256'] == hashes and initial['current_expression'] == TARGET
    assert len(initial['steps']) == len(initial['operation_plan']) == len(operation_plan())
    assert initial['operation_plan'] == operation_plan()
    assert initial['status'].startswith('complete actual integral point 3*D_b')
    original_C = r.from_json(initial['point_coordinates'])
    AC = r.from_json(initial['point_frobenius'])
    initial_point_sha = initial['point_sha256']
    assert point_hash(original_C, AC) == initial_point_sha
    chart = initial['working_chart']
    M, C2, C2i, C3 = prepare_chart(M0, chart, r)
    original_A2, original_A3 = M0['A2'], M0['A3']
    C = r.mm(C2i, original_C)
    assert r.equal(r.mm(M['A2'], r.conjugate(C)), r.mm(C, AC))
    published, published_sha = read(folder/'data/p41_formal47_multiplication_saved.json.gz')
    assert published['source_sha256'] == hashes
    m = published['target_multiplier']
    bits = bin(m)[2:]
    assert len(bits) == 304 and m % 47 == 9
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    helper_sha = hashlib.sha256(Path(prepare_chart.__code__.co_filename).read_bytes()).hexdigest()
    rng = random.Random(4104717503)
    # These large decoded inputs are not needed by the arithmetic loop.
    del sources, M0, initial, published
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass
    rss = [line for line in Path('/proc/self/status').read_text().splitlines() if line.startswith(('VmRSS:', 'VmHWM:'))]
    print('ACTUAL COMMON 3D_b MEMORY RELEASE', '; '.join(rss), flush=True)
    if args.checkpoint.exists():
        data, old_sha = read(args.checkpoint)
        assert data['source_sha256'] == hashes and data['initial_source_sha256'] == initial_sha
        assert data['initial_point_sha256'] == initial_point_sha
        assert data['generating_source_sha256'] == source_sha and data['chart_helper_source_sha256'] == helper_sha
        assert data['working_chart'] == chart and data['target_multiplier'] == m
        original_K = r.from_json(data['point_coordinates'])
        A = r.from_json(data['point_frobenius'])
        original_negative = r.from_json(data['negative_point_coordinates'])
        Anegative = r.from_json(data['negative_point_frobenius'])
        assert point_hash(original_K, A) == data['point_sha256']
        assert point_hash(original_negative, Anegative) == data['negative_point_sha256']
        K, negative = r.mm(C2i, original_K), r.mm(C2i, original_negative)
        rng.setstate(restore_tuple(data['random_state']))
        print('ACTUAL COMMON 3D_b SLP RESUME', data['bits_done'], 'bits', len(data['steps']), 'steps', flush=True)
    else:
        negative, Anegative, record = flip(r.mm(M['V2'], C), AC, M, rng, 'common 3D_b true negative')
        qnegative = r.mm(original_C, r.column(record['f_coefficients']))
        assert r.equal(r.mm(original_A2, r.conjugate(qnegative)), qnegative)
        K, A = C, AC
        data = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
                'point_label': 'three_D_b', 'initial_source_sha256': initial_sha,
                'initial_point_sha256': initial_point_sha, 'generating_source_sha256': source_sha,
                'chart_helper_source_sha256': helper_sha, 'working_chart': chart,
                'target_multiplier': m, 'bits_done': 1, 'magnitude': 1, 'sign': 1, 'steps': [],
                'actual_initial_divisor': 'A_initial=3*D_b+div(h_D)',
                'actual_initial_transport': 'h_D=R_g1^2*(f_b/f0)^324/F_build; all actual coefficients retained in initial_source_sha256',
                'true_final_function': 'f_D=F_chain/(g_transport*h_D^m), div(f_D)=3*m*D_b-A_formal',
                'negative_point_coordinates': r.to_json(r.mm(C2, negative)),
                'negative_point_frobenius': r.to_json(Anegative),
                'negative_point_sha256': point_hash(r.mm(C2, negative), Anegative),
                'negative_quadratic_coefficients': r.to_json(qnegative),
                'negative_flip_record_in_working_chart': record,
                'point_coordinates': r.to_json(original_C), 'point_frobenius': r.to_json(AC),
                'point_sha256': initial_point_sha, 'random_state': rng.getstate(),
                'status': 'actual common 3D_b signed304-bit SLP in progress; full initial principal transport retained; no height claimed'}
        sha, size = write_checkpoint(args.checkpoint, data)
        print('ACTUAL COMMON 3D_b INITIAL SAVED', size, sha, flush=True)
    start_steps = len(data['steps'])

    def record_step(record, section, operation, bit):
        old = r.mm(C3, section)
        assert r.equal(r.mm(original_A3, r.conjugate(old)), old)
        encoded = r.to_json(old)
        record.update({'operation': operation, 'bit': bit, 'sign': data['sign'],
                       'working_point_sha256': record['point_sha256'],
                       'point_sha256': point_hash(r.mm(C2, K), A),
                       'principal_section_coefficients': encoded,
                       'principal_coefficient_sha256': hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest()})
        data['steps'].append(record)

    for n in range(data['bits_done'], min(304, args.max_bits)):
        K, A, section, record = addflip_with_section(K, A, K, A, M, rng, 'common 3D_b double bit'+str(n+1), r, same=True)
        data['sign'] *= -1
        data['magnitude'] *= 2
        record_step(record, section, 'double', n+1)
        if bits[n] == '1':
            QP, AQ = (C, AC) if data['sign'] == 1 else (negative, Anegative)
            K, A, section, record = addflip_with_section(K, A, QP, AQ, M, rng, 'common 3D_b add bit'+str(n+1), r)
            data['sign'] *= -1
            data['magnitude'] += 1
            record_step(record, section, 'add', n+1)
        data['bits_done'] = n+1
        assert data['magnitude'] == int(bits[:n+1], 2)
        data['point_coordinates'] = r.to_json(r.mm(C2, K))
        data['point_frobenius'] = r.to_json(A)
        data['point_sha256'] = point_hash(r.mm(C2, K), A)
        data['random_state'] = rng.getstate()
        if (n+1) % args.save_bits == 0 or n+1 == min(304, args.max_bits):
            sha, size = write_checkpoint(args.checkpoint, data)
            print('ACTUAL COMMON 3D_b SLP CHECKPOINT', n+1, 'bits', len(data['steps']), 'steps',
                  'bytes', size, 'sha', sha, 'seconds', round(time.monotonic()-started, 2),
                  'newsteps', len(data['steps'])-start_steps,
                  'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)
    if data['bits_done'] == 304:
        assert data['sign'] == 1 and data['magnitude'] == m and len(data['steps']) == 454
        data['zero_test_mod47_in_working_chart'] = zero_test_mod47(K, M)
        data['status'] = 'complete actual m*(3*D_b) point and full signed304-bit SLP; complete zero reduction PASS; actual formal endpoint transport and height still require evaluation'
        sha, size = write_checkpoint(args.checkpoint, data)
        print('ACTUAL COMMON 3D_b SLP COMPLETE', size, sha, flush=True)


if __name__ == '__main__':
    main()
