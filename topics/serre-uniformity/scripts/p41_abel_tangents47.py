#!/usr/bin/env python3
"""Calibrate the actual Abel chart by54 genuine moving curve points.

All first-order arithmetic is exact over R2[e]/e^2.  The base divisor used for
each moving point is a true divisor of a section, so the class at e=0 is zero.
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
from p41_group_operations47 import load_sources, make_model, onebased, vector_json
from p41_formal47_chart import make_chart, chart_record
from p41_cm4_divisor47 import kernel
from p41_formal47_multiply import write_checkpoint, restore_tuple


def dz(A):
    return A, r.zeros(*A[0].shape)


def dmm(A, B):
    return r.mm(A[0], B[0]), r.add(r.mm(A[1], B[0]), r.mm(A[0], B[1]))


def dmul(A, B):
    return r.mul(A[0], B[0]), r.add(r.mul(A[1], B[0]), r.mul(A[0], B[1]))


def dsub(A, B):
    return r.sub(A[0], B[0]), r.sub(A[1], B[1])


def drows(A, ids):
    return r.rows(A[0], ids), r.rows(A[1], ids)


def dcols(A, ids):
    return r.cols(A[0], ids), r.cols(A[1], ids)


def dinverse(A):
    C = r.inverse_matrix(A[0])
    return C, r.neg(r.mm(C, r.mm(A[1], C)))


def dinverse_values(A):
    C = r.inverse_values(A[0])
    return C, r.neg(r.mul(r.mul(C, C), A[1]))


def dkernel(A, rank):
    rr, cc = r.rank_pivots(A[0])
    assert len(rr) == rank
    K0, free, _ = r.kernel_from_rows(r.rows(A[0], rr), rr, cc)
    rhs = r.mm(r.rows(A[1], rr), K0)
    X = r.neg(r.mm(r.inverse_matrix(r.cols(r.rows(A[0], rr), cc)), rhs))
    K1 = r.zeros(*K0[0].shape)
    for side in range(2):
        K1[side][cc] = X[side]
    assert r.iszero(r.mm(A[0], K0))
    assert r.iszero(r.add(r.mm(A[0], K1), r.mm(A[1], K0)))
    return (K0, K1), rr, cc, free


def section_through_point(W, derivative, point, rng):
    row = r.rows(W, [point])
    pivot = int(np.flatnonzero(r.units(row)[0])[0])
    for attempt in range(1, 101):
        seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73)])
        c = (seed[0].copy(), seed[1].copy())
        c[0][pivot, 0] = c[1][pivot, 0] = 0
        value = r.mm(row, c)
        correction = r.neg(r.mul(value, r.inverse_values(r.cols(row, [pivot]))))
        c[0][pivot, 0], c[1][pivot, 0] = correction[0][0, 0], correction[1][0, 0]
        values = r.mm(W, c)
        assert r.iszero(r.rows(values, [point]))
        others = [k for k in range(820) if k != point]
        if not np.all(r.units(r.rows(values, others))):
            continue
        if not np.all(r.units(r.mm(r.rows(derivative, [point]), c))):
            continue
        return seed, c, values, pivot
    raise RuntimeError('No clean actual section through the selected point')


def moving_point_ideal(point, M, derivative, V2derivative, rng):
    v_seed, vc, v, pivot = section_through_point(M['W'], derivative, point, rng)
    U, urows, ucols, _ = r.normalize(r.mul(v, M['V2']), 199)
    assert ucols == list(range(199))
    for attempt in range(1, 31):
        t_seed, tc, t, tpivot = section_through_point(M['W'], derivative, point, rng)
        scaled = r.mul(t, M['V2'])
        R = r.sub(scaled, r.mm(U, r.rows(scaled, urows)))
        rr, cc = r.rank_pivots(R)
        if len(rr) != 125:
            continue
        K, free, _ = r.kernel_from_rows(r.rows(R, rr), rr, cc)
        assert r.iszero(r.mm(R, K)) and K[0].shape == (199, 74)
        break
    else:
        raise RuntimeError('The actual residual degree125 ideal was not obtained')
    residual_values = r.mm(M['V2'], K)
    value = r.rows(residual_values, [point])
    deriv = r.mm(r.rows(V2derivative, [point]), K)
    restriction_kernel, _, _, _ = dkernel((value, deriv), 1)
    point_coords = dmm(dz(K), restriction_kernel)
    space = dmm(dz(M['V2']), point_coords)
    base, rows, _, _ = r.normalize(space[0], 73)
    principal, _, _, _ = r.normalize(r.mul(v, M['W']), 73)
    # Normalize both bases on the same rows before comparing the actual zero class.
    principal = r.mm(principal, r.inverse_matrix(r.rows(principal, rows)))
    assert r.equal(base, principal)
    record = {'point_1based': point+1, 'v_seed': vector_json(v_seed), 'v_coefficients': vector_json(vc),
              'v_pivot_column_1based': pivot+1, 't_seed': vector_json(t_seed),
              't_coefficients': vector_json(tc), 't_pivot_column_1based': tpivot+1,
              'residual_rank': 125, 'moving_restriction_rank': 1}
    return space, record


def chart_tangent(space, point, M, chart, rng):
    restriction = drows(space, chart['C'])
    c, _, _, _ = dkernel(restriction, 72)
    s = dmm(space, c)
    remain = [k for k in chart['remain'] if k != point]
    assert len(remain) == 747 and np.all(r.units(r.rows(s[0], remain)))
    V2small, p2, cols, inverse = r.normalize(r.rows(M['V2'], remain), 199)
    assert cols == list(range(199))
    V2full = r.mm(M['V2'], inverse)
    for attempt in range(1, 31):
        seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(73)])
        t = dmm(space, dz(seed))
        if not np.all(r.units(r.rows(t[0], remain))):
            continue
        ratio = dmul(drows(t, remain), dinverse_values(drows(s, remain)))
        scaled = dmul(ratio, dz(V2small))
        residual = dsub(scaled, dmm(dz(V2small), drows(scaled, p2)))
        rr, cc = r.rank_pivots(residual[0])
        if len(rr) != 126:
            continue
        K, _, _, _ = dkernel(residual, 126)
        U = dmm(dz(V2full), K)
        assert r.iszero(r.rows(U[0], chart['C'])) and r.iszero(r.rows(U[1], chart['C']))
        normalized = dmm(U, dinverse(drows(U, chart['chart_rows'])))
        assert r.equal(normalized[0], chart['U0'])
        assert r.iszero(r.rows(normalized[1], chart['chart_rows']))
        return normalized[1], {'chart_test_seed': vector_json(seed), 'chart_flip_rank': 126,
                               'chart_zero_value_matches': True}
    raise RuntimeError('No complete first-order chart ideal')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directions', type=int, default=54)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('data')/'p41_abel_tangents47_checkpoint.json.gz')
    parser.add_argument('--work', type=Path,
                        default=Path(__file__).with_name('data')/'p41_abel_tangents47_work.json.gz')
    parser.add_argument('--fresh', action='store_true')
    args = parser.parse_args()
    data_dir = Path(__file__).with_name('data')
    sources, hashes = load_sources(data_dir)
    jraw = (data_dir/'p41_evaluation_jets47_checkpoint.json.gz').read_bytes()
    jets = json.loads(gzip.decompress(jraw))
    for name, digest in jets['source_sha256'].items():
        assert hashlib.sha256((data_dir/name).read_bytes()).hexdigest() == digest
    hashes['p41_evaluation_jets47_checkpoint.json.gz'] = hashlib.sha256(jraw).hexdigest()
    M = make_model(sources)
    chart = make_chart(M, sources[0])
    derivative = r.from_json(jets['evaluation_derivatives'])
    divs = sources[1]
    pairs = divs['square_basis_monomials_1based']
    aa, bb = [a-1 for a, b in pairs], [b-1 for a, b in pairs]
    V2derivative = r.mm(r.add(r.mul(r.cols(derivative, aa), r.cols(M['W'], bb)),
                               r.mul(r.cols(M['W'], aa), r.cols(derivative, bb))),
                        r.from_json(divs['square_basis_inverse']))
    K1 = r.from_json(kernel(73, divs['cusp_rank_columns_1based'], divs['cusp_free_columns_1based'],
                            divs['canonical_kernel_block']))
    canonical_values = r.mm(M['W'], K1)
    rr, cc = r.rank_pivots(r.rows(canonical_values, chart['remain']))
    assert len(rr) == 54 and cc == list(range(54))
    points = [chart['remain'][k] for k in rr]
    ks = -3*pow(4+27*32**2, -1, r.Q) % r.Q
    assert ks % 47 == 38
    Omega = tuple(x*ks % r.Q for x in r.rows(canonical_values, points))
    r.inverse_matrix(Omega)
    rng = random.Random(4104712101)
    tangent_rows, records = [], []
    coordinate_rows = [k for k in range(820) if k not in set(chart['C']+chart['chart_rows'])][:20]
    candidate_coordinates = [73*n+k for n in coordinate_rows for k in range(73)]
    if args.work.exists() and not args.fresh:
        work = json.loads(gzip.decompress(args.work.read_bytes()))
        assert work['source_sha256'] == hashes
        assert work['candidate_coordinate_indices_1based'] == onebased(candidate_coordinates)
        assert work['target_directions'] == args.directions
        partial = r.from_json(work['partial_abel_derivatives'])
        tangent_rows = [r.rows(partial, [k]) for k in range(partial[0].shape[0])]
        records = work['direction_records']
        assert len(records) == len(tangent_rows)
        rng.setstate(restore_tuple(work['random_state']))
        print('Resuming Abel calibration after', len(records), 'directions', flush=True)
    start = time.monotonic()
    for k in range(len(records), args.directions):
        point = points[k]
        space, record = moving_point_ideal(point, M, derivative, V2derivative, rng)
        tangent, chart_data = chart_tangent(space, point, M, chart, rng)
        record.update(chart_data)
        flat = tangent[0].reshape(1, -1), tangent[1].reshape(1, -1)
        tangent_rows.append(r.cols(flat, candidate_coordinates))
        records.append(record)
        print('Actual Abel tangent', k+1, '/', args.directions, 'point', point+1,
              'seconds', round(time.monotonic()-start, 1), flush=True)
        if (k+1) % 5 == 0 or k+1 == args.directions:
            partial = tuple(np.concatenate([row[side] for row in tangent_rows], axis=0) for side in range(2))
            work = {'source_sha256': hashes, 'target_directions': args.directions,
                    'candidate_coordinate_indices_1based': onebased(candidate_coordinates),
                    'partial_abel_derivatives': r.to_json(partial), 'direction_records': records,
                    'random_state': rng.getstate(), 'status': 'recoverable exact Abel calibration in progress'}
            digest, size = write_checkpoint(args.work, work)
            print('ABEL CHECKPOINT', k+1, 'directions;', size, 'bytes;', digest, flush=True)
    D = tuple(np.concatenate([row[side] for row in tangent_rows], axis=0) for side in range(2))
    rr, coordinates = r.rank_pivots(D)
    assert len(rr) == args.directions
    selected = r.cols(D, coordinates)
    transform = r.mm(r.inverse_matrix(selected), r.rows(Omega, list(range(args.directions))))
    assert r.equal(r.mm(selected, transform), r.rows(Omega, list(range(args.directions))))
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': r.Q,
              'source_sha256': hashes, 'chart': chart_record(chart), 'directions': args.directions,
              'point_indices_1based': onebased(points[:args.directions]), 'direction_records': records,
              'kodaira_spencer_scalar_rational': [-3, 4+27*32**2],
              'kodaira_spencer_scalar_mod47power4': ks,
              'verification_coordinate_indices_1based': onebased(candidate_coordinates),
              'abel_derivatives_for_verification': r.to_json(D),
              'flattened_chart_coordinate_indices_1based': onebased([candidate_coordinates[k] for k in coordinates]),
              'coordinate_positions_1based': [[candidate_coordinates[k]//73+1, candidate_coordinates[k] % 73+1] for k in coordinates],
              'selected_abel_derivatives': r.to_json(selected),
              'normalized_differential_values': r.to_json(r.rows(Omega, list(range(args.directions)))),
              'chart_to_differential_transform': r.to_json(transform),
              'status': 'actual first-order Abel calibration with all unit checks; independent verification pending'}
    raw = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
    packed = gzip.compress(raw, mtime=0)
    args.output.write_bytes(packed)
    print('CALIBRATION', args.directions, 'directions; bytes', len(packed),
          'SHA256', hashlib.sha256(packed).hexdigest(), flush=True)


if __name__ == '__main__':
    main()
