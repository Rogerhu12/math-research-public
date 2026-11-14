#!/usr/bin/env python3
"""Independent Cech-formula verification of the54 actual Abel tangents.

This does not use the dual-number PicChart calculation in the generator.
Instead it constructs a meromorphic section with principal part1/t, cancels
the poles explicitly, and checks that the resulting tangent is global.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
import numpy as np
import p41_r2_matrix as r
from p41_group_operations47 import load_sources, make_model
from p41_formal47_chart import make_chart, chart_record
from p41_cm4_divisor47 import kernel


def check_section(record, prefix, point, W, derivative):
    seed = r.column(record[prefix+'_seed'])
    coeff = r.column(record[prefix+'_coefficients'])
    pivot = record[prefix+'_pivot_column_1based']-1
    for side in range(2):
        keep = [k for k in range(73) if k != pivot]
        assert np.array_equal(seed[side][keep], coeff[side][keep])
    values = r.mm(W, coeff)
    assert r.iszero(r.rows(values, [point]))
    assert np.all(r.units(r.rows(values, [k for k in range(820) if k != point])))
    dv = r.mm(r.rows(derivative, [point]), coeff)
    assert np.all(r.units(dv))
    return values, dv


def cech_tangent(record, M, chart, derivative, model):
    point = record['point_1based']-1
    assert point not in chart['C']
    v, dv = check_section(record, 'v', point, M['W'], derivative)
    t, _ = check_section(record, 't', point, M['W'], derivative)
    U, up, _, _ = r.normalize(r.mul(v, M['V2']), 199)
    scaled = r.mul(t, M['V2'])
    R = r.sub(scaled, r.mm(U, r.rows(scaled, up)))
    rr, cc = r.rank_pivots(R)
    assert len(rr) == record['residual_rank'] == 125
    K, _, _ = r.kernel_from_rows(r.rows(R, rr), rr, cc)
    assert r.iszero(r.mm(R, K)) and K[0].shape == (199, 74)
    Wres = r.mm(M['V2'], K)
    choices = np.flatnonzero(r.units(r.rows(Wres, [point]))[0])
    assert len(choices)
    w = r.cols(Wres, [int(choices[0])])
    w = r.mul(w, r.mul(dv, r.inverse_values(r.rows(w, [point]))))
    # tau=w/v has principal part1/t at P, in the fixed weight-two frame.
    remaining = [k for k in range(820) if k != point]
    tau = r.zeros(820, 1)
    ratio = r.mul(r.rows(w, remaining), r.inverse_values(r.rows(v, remaining)))
    for side in range(2):
        tau[side][remaining] = ratio[side]
    coeff_C = r.zeros(73, 1)
    pivots = [n-1 for n in model['pivot_rows_1based']]
    for j, p in enumerate(pivots):
        if j != chart['omitted']:
            for side in range(2):
                coeff_C[side][j, 0] = tau[side][p, 0]
    sC = r.mm(M['W'], coeff_C)
    assert r.equal(r.rows(sC, chart['C']), r.rows(tau, chart['C']))
    v0 = chart['v']
    v0P, sP = r.rows(v0, [point]), r.rows(M['W'], [point])
    bracket = r.sub(r.mul(v0, sP), r.mul(v0P, M['W']))
    assert r.iszero(r.rows(bracket, [point]))
    delta = r.add(r.mul(tau, bracket), r.mul(r.mul(v0P, sC), M['W']))
    dP = r.rows(derivative, [point])
    dv0P = r.cols(dP, [chart['omitted']])
    atP = r.add(r.sub(r.mul(dv0P, sP), r.mul(v0P, dP)),
               r.mul(r.mul(v0P, r.rows(sC, [point])), sP))
    for side in range(2):
        delta[side][point] = atP[side][0]
    # This is an independent full global section identity, not just a match
    # of the54 coordinates eventually selected from the chart.
    assert r.equal(r.mm(M['V2'], r.rows(delta, M['P2'])), delta)
    assert r.iszero(r.rows(delta, chart['C']))
    normalized = r.mm(delta, chart['U0_inverse'])
    normalized = r.sub(normalized, r.mm(chart['U0'], r.rows(normalized, chart['chart_rows'])))
    assert r.iszero(r.rows(normalized, chart['chart_rows']))
    return normalized


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path,
                        default=Path(__file__).with_name('data')/'p41_abel_tangents47_checkpoint.json.gz')
    parser.add_argument('--limit', type=int)
    args = parser.parse_args()
    raw = args.path.read_bytes()
    data = json.loads(gzip.decompress(raw))
    data_dir = Path(__file__).with_name('data')
    sources, hashes = load_sources(data_dir)
    for name, digest in data['source_sha256'].items():
        assert hashlib.sha256((data_dir/name).read_bytes()).hexdigest() == digest
    jets = json.loads(gzip.decompress((data_dir/'p41_evaluation_jets47_checkpoint.json.gz').read_bytes()))
    M = make_model(sources)
    chart = make_chart(M, sources[0])
    if 'chart' in data:
        assert data['chart'] == chart_record(chart)
    derivative = r.from_json(jets['evaluation_derivatives'])
    partial = 'partial_abel_derivatives' in data
    coordinate_key = 'candidate_coordinate_indices_1based' if partial else 'verification_coordinate_indices_1based'
    matrix_key = 'partial_abel_derivatives' if partial else 'abel_derivatives_for_verification'
    coordinates = [n-1 for n in data[coordinate_key]]
    expected = r.from_json(data[matrix_key])
    records = data['direction_records'][:args.limit]
    start = time.monotonic()
    for k, record in enumerate(records):
        tangent = cech_tangent(record, M, chart, derivative, sources[0])
        flat = tangent[0].reshape(1, -1), tangent[1].reshape(1, -1)
        assert r.equal(r.cols(flat, coordinates), r.rows(expected, [k]))
        print('Independent Cech tangent', k+1, '/', len(records), 'PASS; seconds',
              round(time.monotonic()-start, 1), flush=True)
    if not partial and args.limit is None:
        assert data['directions'] == len(records) == 54
        divs = sources[1]
        K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'],
                                divs['canonical_kernel_block']))
        beta = -3*pow(4+27*32**2, -1, r.Q) % r.Q
        assert data['kodaira_spencer_scalar_rational'] == [-3, 27652]
        assert data['kodaira_spencer_scalar_mod47power4'] == beta and beta % 47 == 38
        points = [n-1 for n in data['point_indices_1based']]
        Omega = tuple(x*beta % r.Q for x in r.rows(r.mm(M['W'], K1), points))
        assert r.equal(Omega, r.from_json(data['normalized_differential_values']))
        selected_positions = [data[coordinate_key].index(n) for n in data['flattened_chart_coordinate_indices_1based']]
        D = r.cols(expected, selected_positions)
        assert r.equal(D, r.from_json(data['selected_abel_derivatives']))
        inverse = r.inverse_matrix(D)
        assert r.equal(r.mm(inverse, Omega), r.from_json(data['chart_to_differential_transform']))
        print('Full54-dimensional actual Kodaira-Spencer-normalized Lie calibration PASS.', flush=True)
    print('SHA256', hashlib.sha256(raw).hexdigest(), flush=True)


if __name__ == '__main__':
    main()
