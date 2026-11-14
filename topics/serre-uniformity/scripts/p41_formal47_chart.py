#!/usr/bin/env python3
"""An actual representative-independent local Abel chart for the level41 model."""
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
from p41_group_operations47 import load_sources, make_model, onebased, vector_json
from p41_formal47_multiply import point_hash


def make_chart(M, model):
    pivots = [n-1 for n in model['pivot_rows_1based']]
    assert r.equal(r.rows(M['W'], pivots), r.eye(73))
    for omitted in range(73):
        C = [k for j, k in enumerate(pivots) if j != omitted]
        remain = [k for k in range(820) if k not in set(C)]
        v = r.cols(M['W'], [omitted])
        if not np.all(r.units(r.rows(v, remain))):
            continue
        assert r.iszero(r.rows(v, C))
        U0, chart_rows, chart_cols, U0inv = r.normalize(r.mul(v, M['W']), 73)
        assert chart_cols == list(range(73))
        V2small, p2, cc, C2 = r.normalize(r.rows(M['V2'], remain), 199)
        assert cc == list(range(199))
        fullV2 = r.mm(M['V2'], C2)
        assert r.equal(r.rows(fullV2, remain), V2small)
        print('Actual chart uses omitted basis column', omitted+1, '; fixed divisor degree72;',
              'all748 residual evaluations are units.', flush=True)
        return {'C': C, 'remain': remain, 'omitted': omitted, 'v': v, 'U0': U0,
                'chart_rows': chart_rows, 'U0_inverse': U0inv,
                'V2small': V2small, 'V2full': fullV2, 'V2small_rows': p2, 'V2small_inverse': C2}
    raise RuntimeError('No valid fixed Abel chart among the73 tested divisors')


def evaluate_chart(KP, AP, M, chart, rng):
    S = r.mm(M['V2'], KP)
    restriction = r.rows(S, chart['C'])
    rr, cc = r.rank_pivots(restriction)
    assert len(rr) == 72
    c, free, block = r.kernel_from_rows(r.rows(restriction, rr), rr, cc)
    assert len(free) == 1 and r.iszero(r.mm(restriction, c))
    s = r.mm(S, c)
    ssmall = r.rows(s, chart['remain'])
    assert np.all(r.units(ssmall))
    for attempt in range(1, 31):
        seed, tc = r.rational_trace(AP, rng)
        t = r.mm(S, tc)
        if not np.all(r.units(t)):
            continue
        ratio = r.mul(r.rows(t, chart['remain']), r.inverse_values(ssmall))
        scaled = r.mul(ratio, chart['V2small'])
        R = r.sub(scaled, r.mm(chart['V2small'], r.rows(scaled, chart['V2small_rows'])))
        kr, kc = r.rank_pivots(R)
        if len(kr) != 126:
            continue
        Ucoeff, kfree, kblock = r.kernel_from_rows(r.rows(R, kr), kr, kc)
        assert r.iszero(r.mm(R, Ucoeff))
        U = r.mm(chart['V2full'], Ucoeff)
        assert r.iszero(r.rows(U, chart['C']))
        inv = r.inverse_matrix(r.rows(U, chart['chart_rows']))
        normalized = r.mm(U, inv)
        assert r.equal(r.rows(normalized, chart['chart_rows']), r.eye(73))
        record = {'input_point_sha256': point_hash(KP, AP),
                  'restriction_rank_columns_1based': onebased(cc),
                  'restriction_rank_rows_1based': onebased(rr),
                  'restriction_free_column_1based': onebased(free),
                  'restriction_kernel_block': r.to_json(block),
                  't_seed': vector_json(seed), 't_coefficients': vector_json(tc),
                  'flip_rank_rows_1based': onebased(kr), 'flip_rank_columns_1based': onebased(kc),
                  'flip_free_columns_1based': onebased(kfree), 'flip_kernel_block': r.to_json(kblock),
                  'chart_normalization_inverse': r.to_json(inv)}
        return normalized, record
    raise RuntimeError('No full residual ideal found for the actual Abel chart')


def chart_record(chart):
    return {'fixed_divisor_rows_1based': onebased(chart['C']),
            'remaining_rows_1based': onebased(chart['remain']),
            'omitted_basis_column_1based': chart['omitted']+1,
            'chart_rows_1based': onebased(chart['chart_rows']),
            'zero_chart_basis_inverse': r.to_json(chart['U0_inverse']),
            'restricted_V2_rows_1based': onebased(chart['V2small_rows']),
            'restricted_V2_basis_inverse': r.to_json(chart['V2small_inverse'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('data')/'p41_formal47_chart_checkpoint.json.gz')
    args = parser.parse_args()
    sources, hashes = load_sources(Path(__file__).with_name('data'))
    M = make_model(sources)
    chart = make_chart(M, sources[0])
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
              'source_sha256': hashes, 'chart': chart_record(chart),
              'status': 'actual fixed local Abel chart at zero; no nonzero formal logarithm yet'}
    raw = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(raw, mtime=0)
    args.output.write_bytes(packed)
    print('Saved', len(packed), 'bytes SHA256', hashlib.sha256(packed).hexdigest(), flush=True)


if __name__ == '__main__':
    main()
