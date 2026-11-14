#!/usr/bin/env python3
"""Extract the actual54 normalized differential logarithms of B_minus4.

Requires the completed signed h*B multiplication and the54-direction actual
Abel calibration.  No local height or QC common-root assertion is made.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
import numpy as np
import p41_r2_matrix as r
from p41_group_operations47 import load_sources, make_model, double, flip
from p41_formal47_multiply import H, zero_test_mod47, point_hash, write_checkpoint
from p41_formal47_chart import make_chart, evaluate_chart, chart_record
from p41_cm4_divisor47 import kernel


def scale(A, k):
    return tuple(x*(k % r.Q) % r.Q for x in A)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    data_dir = Path(__file__).with_name('data')
    parser.add_argument('--multiplication', type=Path,
                        default=data_dir/'p41_formal47_multiplication_checkpoint.json.gz')
    parser.add_argument('--calibration', type=Path,
                        default=data_dir/'p41_abel_tangents47_checkpoint.json.gz')
    parser.add_argument('--output', type=Path,
                        default=data_dir/'p41_formal47_log_certificate.json.gz')
    args = parser.parse_args()
    sources, hashes = load_sources(data_dir)
    raw_point, raw_calibration = args.multiplication.read_bytes(), args.calibration.read_bytes()
    point, calibration = json.loads(gzip.decompress(raw_point)), json.loads(gzip.decompress(raw_calibration))
    assert point['source_sha256'] == hashes and point['target_multiplier'] == point['magnitude'] == H
    assert point['bits_done'] == point['target_bits'] == 304 and 'zero_test_mod47' in point
    assert calibration['directions'] == 54
    assert all(calibration['source_sha256'][name] == digest for name, digest in hashes.items())
    M = make_model(sources)
    chart = make_chart(M, sources[0])
    assert chart_record(chart) == calibration['chart']
    K, A = r.from_json(point['point_coordinates']), r.from_json(point['point_frobenius'])
    assert point_hash(K, A) == point['point_sha256']
    assert r.equal(r.mm(K, A), r.mm(M['A2'], r.conjugate(K)))
    assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))
    zero_test = zero_test_mod47(K, M)
    rng = random.Random(4104712102)
    negative, Anegative, negative_record = flip(r.mm(M['V2'], K), A, M, rng, 'Formal minusY')
    Md = dict(M)
    Md['B'], Md['WB'], Md['AB'] = K, r.mm(M['V2'], K), A
    _, _, double_record = double(Md, rng)
    record = double_record['minus_two']
    negative_two = r.from_json(kernel(199, record['rank_columns_1based'], record['free_columns_1based'],
                                      record['kernel_block']))
    Anegative_two = r.from_json(record['frobenius_matrix'])
    matrices, chart_records = [], []
    for coords, descent, label in ((K, A, 'Y'), (negative, Anegative, '-Y'),
                                   (negative_two, Anegative_two, '-2Y')):
        value, witness = evaluate_chart(coords, descent, M, chart, rng)
        F = r.sub(value, chart['U0'])
        assert all(np.all(x % 47 == 0) for x in F)
        matrices.append(F)
        chart_records.append(witness)
        print('Actual representative-independent formal chart', label, 'computed.', flush=True)
    Lie = scale(r.add(r.sub(scale(matrices[0], 2), scale(matrices[1], 6)), matrices[2]), pow(6, -1, r.Q))
    assert all(np.all(x % 47 == 0) for x in Lie)
    selected = [n-1 for n in calibration['flattened_chart_coordinate_indices_1based']]
    L = r.cols((Lie[0].reshape(1, -1), Lie[1].reshape(1, -1)), selected)
    transform = r.from_json(calibration['chart_to_differential_transform'])
    logY = r.mm(L, transform)
    logB = scale(logY, point['sign']*pow(H, -1, r.Q))
    AK = r.from_json(sources[1]['canonical_frobenius_matrix'])
    assert r.equal(r.mm(logB, AK), r.conjugate(logB))
    assert all(np.all(x % 47 == 0) for x in logB)
    nonzero = [j+1 for j in range(54) if logB[0][0, j] or logB[1][0, j]]
    print('Actual normalized differential logarithm coordinates:', len(nonzero), 'nonzero modulo47^4.', flush=True)
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
              'source_sha256': hashes,
              'algorithm_sha256': {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                   for name in ('p41_formal47_multiply.py', 'p41_abel_tangents47.py',
                                                'p41_formal47_chart.py', 'p41_group_operations47.py', 'p41_r2_matrix.py')},
              'multiplication_source': args.multiplication.name,
              'multiplication_sha256': hashlib.sha256(raw_point).hexdigest(),
              'calibration_source': args.calibration.name,
              'calibration_sha256': hashlib.sha256(raw_calibration).hexdigest(),
              'formal_input_sign': point['sign'], 'formal_input_multiplier': H,
              'formal_input_point_sha256': point['point_sha256'], 'zero_test_mod47': zero_test,
              'negative_record': negative_record, 'double_record': double_record,
              'chart_records': chart_records, 'selected_Lie_coordinates': r.to_json(L),
              'log_of_signed_multiple': r.to_json(logY), 'log_of_B_minus4': r.to_json(logB),
              'nonzero_coordinate_indices_1based': nonzero,
              'differential_basis': 'Kodaira-Spencer images of the R110 canonical weight-two basis; beta(0)=-3/27652 explicitly retained',
              'status': 'actual first-order differential logarithm modulo47^4; no nonprincipal local height or QC roots'}
    digest, size = write_checkpoint(args.output, result)
    print('Actual B_minus4 logarithm saved;', size, 'bytes; SHA256', digest, flush=True)


if __name__ == '__main__':
    main()
