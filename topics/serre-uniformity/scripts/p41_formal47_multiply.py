#!/usr/bin/env python3
"""Resumeable exact multiplication of the actual CM class into the formal group.

The rolling checkpoint is an intermediate calculation, not a completion claim.
Every completed AddFlip checks full kernels, unit ranks and Frobenius descent.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys
import time

sys.dont_write_bytecode = True
import numpy as np
import p41_r2_matrix as r
from p41_group_operations47 import load_sources, make_model, replay_negative, flip, onebased, vector_json

H = 21113421681728164076758160383370947105909472013138012462421148345826995695660466565589785072


def point_hash(K, A):
    payload = json.dumps([r.to_json(K), r.to_json(A)], separators=(',', ':')).encode()
    return hashlib.sha256(payload).hexdigest()


def addflip(KP, AP, KQ, AQ, M, rng, label, same=False):
    WP, WQ = r.mm(M['V2'], KP), r.mm(M['V2'], KQ)
    P, prows, pcols, pinv = r.normalize(WP, 73)
    assert pcols == list(range(73))
    if same:
        Q = P
    else:
        square = r.rows(WQ, prows)
        qr, qc = r.rank_pivots(square)
        if len(qr) == 73:
            Q = r.mm(WQ, r.inverse_matrix(square))
        else:
            Q, _, qcols, _ = r.normalize(WQ, 73)
            assert qcols == list(range(73))
    pairs = [[k, k] for k in range(73)]+[[k, (k+1) % 73] for k in range(73)]
    while True:
        pairs += [[rng.randrange(73), rng.randrange(73)] for _ in range(100)]
        products = r.mul(r.cols(P, [a for a, b in pairs]), r.cols(Q, [b for a, b in pairs]))
        rr, cc = r.rank_pivots(products)
        if len(rr) == 199:
            break
        assert len(rr) < 199 and len(pairs) < 746
    U, Urows, _, _ = r.normalize(products, 199)
    for attempt in range(1, 31):
        seed, coeff = r.rational_trace(M['A1'], rng)
        v = r.mm(M['W'], coeff)
        R = r.mul(v, M['V3'])
        R = r.sub(R, r.mm(U, r.rows(R, Urows)))
        rr, cc = r.rank_pivots(R)
        if len(rr) != 252:
            continue
        K, free, _ = r.kernel_from_rows(r.rows(R, rr), rr, cc)
        assert r.iszero(r.mm(R, K))
        transformed = r.mm(M['A3'], r.conjugate(K))
        A = r.rows(transformed, free)
        assert r.equal(r.mm(K, A), transformed)
        assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))
        break
    else:
        raise RuntimeError('No complete unit colon after30 actual choices')
    result, Aresult, record = flip(r.mm(M['V3'], K), A, M, rng, label)
    return result, Aresult, {'product_rank': 199, 'colon_rank': 252, 'flip_rank': 126,
                              'colon_attempts': attempt, 'point_sha256': point_hash(result, Aresult)}


def write_checkpoint(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(raw, mtime=0)
    assert len(packed) < 5_000_000
    tmp = path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(packed)
    tmp.replace(path)
    return hashlib.sha256(packed).hexdigest(), len(packed)


def restore_tuple(value):
    return tuple(restore_tuple(v) for v in value) if isinstance(value, list) else value


def zero_test_mod47(K, M):
    """Full V1*(-) ideal test, not equality of noncanonical representatives."""
    W = tuple(x % 47 for x in M['W'])
    V2 = tuple(x % 47 for x in M['V2'])
    K = tuple(x % 47 for x in K)
    S, pp, cc, _ = r.normalize(r.mm(V2, K, 47), 73, 47)
    assert cc == list(range(73))
    for index in range(73):
        residual = r.mul(r.cols(W, [index]), W, 47)
        residual = r.sub(residual, r.mm(S, r.rows(residual, pp), 47), 47)
        rr, cc = r.rank_pivots(residual)
        if len(rr) != 72:
            continue
        T, free, _ = r.kernel_from_rows(r.rows(residual, rr), rr, cc, 47)
        s = r.mm(W, T, 47)
        complete = r.mul(s, W, 47)
        complete = r.sub(complete, r.mm(S, r.rows(complete, pp), 47), 47)
        if r.iszero(complete):
            return {'dimension': 1, 'test_section_1based': index+1,
                    'rank_rows_1based': onebased(rr), 'rank_columns_1based': onebased(cc),
                    'kernel': r.to_json(T), 'point_pivot_rows_1based': onebased(pp)}
    raise AssertionError('The completed multiple has not passed the full zero test modulo47')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path,
                        default=Path(__file__).with_name('data')/'p41_formal47_multiplication_checkpoint.json.gz')
    parser.add_argument('--fresh', action='store_true')
    parser.add_argument('--max-bits', type=int, default=304)
    args = parser.parse_args()
    sources, hashes = load_sources(Path(__file__).with_name('data'))
    M = make_model(sources)
    minusB, AminusB = replay_negative(M, sources[3])
    rng = random.Random(4104711704)
    bits = bin(H)[2:]
    assert len(bits) == 304 and H % 47 != 0
    data = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
            'source_sha256': hashes, 'target_multiplier': H, 'target_bits': len(bits),
            'status': 'incomplete actual multiplication; no logarithm extracted',
            'steps': [], 'bits_done': 1, 'magnitude': 1, 'sign': 1}
    K, A = M['B'], M['AB']
    if args.checkpoint.exists() and not args.fresh:
        data = json.loads(gzip.decompress(args.checkpoint.read_bytes()))
        assert data['source_sha256'] == hashes and data['target_multiplier'] == H
        K, A = r.from_json(data['point_coordinates']), r.from_json(data['point_frobenius'])
        assert point_hash(K, A) == data['point_sha256']
        rng.setstate(restore_tuple(data['random_state']))
        assert data['magnitude'] == int(bits[:data['bits_done']], 2)
        print('Resuming after', data['bits_done'], 'bits', flush=True)
    started = time.monotonic()
    for n in range(data['bits_done'], min(len(bits), args.max_bits)):
        K, A, record = addflip(K, A, K, A, M, rng, 'double bit'+str(n+1), same=True)
        data['sign'] *= -1
        data['magnitude'] *= 2
        record.update({'operation': 'double', 'bit': n+1, 'sign': data['sign']})
        data['steps'].append(record)
        if bits[n] == '1':
            B0, AB0 = (M['B'], M['AB']) if data['sign'] == 1 else (minusB, AminusB)
            K, A, record = addflip(K, A, B0, AB0, M, rng, 'add bit'+str(n+1))
            data['sign'] *= -1
            data['magnitude'] += 1
            record.update({'operation': 'add', 'bit': n+1, 'sign': data['sign']})
            data['steps'].append(record)
        data['bits_done'] = n+1
        assert data['magnitude'] == int(bits[:n+1], 2)
        data['point_coordinates'], data['point_frobenius'] = r.to_json(K), r.to_json(A)
        data['point_sha256'] = point_hash(K, A)
        data['random_state'] = rng.getstate()
        if (n+1) % 5 == 0 or n+1 == min(len(bits), args.max_bits):
            digest, size = write_checkpoint(args.checkpoint, data)
            print('CHECKPOINT', n+1, '/', len(bits), 'bits;', len(data['steps']), 'operations;',
                  size, 'bytes;', digest, '; seconds', round(time.monotonic()-started, 1), flush=True)
    if data['bits_done'] == len(bits):
        data['zero_test_mod47'] = zero_test_mod47(K, M)
        data['status'] = 'actual signed h*B computed; full zero test modulo47 passed; logarithm not yet extracted'
        digest, size = write_checkpoint(args.checkpoint, data)
        print('FORMAL GROUP ENTRY VERIFIED', 'sign', data['sign'], 'SHA256', digest, 'bytes', size, flush=True)


if __name__ == '__main__':
    main()
