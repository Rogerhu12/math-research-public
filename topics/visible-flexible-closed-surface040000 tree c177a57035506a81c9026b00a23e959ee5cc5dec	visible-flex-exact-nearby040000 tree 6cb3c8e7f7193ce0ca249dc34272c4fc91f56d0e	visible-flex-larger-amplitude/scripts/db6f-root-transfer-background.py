#!/usr/bin/env python3
"""Transfer a proved background value packet to another grid of the same g.

The packet is a pointwise interval-polynomial enclosure for w and wr; no
derivative of a packet polynomial is asserted. Exact physical intersections
are converted to binary local partitions using both outward neighbours.
Every old piece with positive-length intersection is affinely composed, then
coefficient hulls cover the possibly different pieces on a boundary sliver.
The analytic validity of the input packet remains a separate proof input.
"""
import argparse
from bisect import bisect_left, bisect_right
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
from types import SimpleNamespace
import time

import numpy as np
from db6f_tail_integrated import IntegratedTail
from db6f_tail_interval_elementary import I, qbounds

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'background_transfer_consumer', HERE/'db6f-audit-tail-metric-curvature.py')
consumer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(consumer)

# These fields control numerical solution/evaluation only. Every other
# supplied parameter must agree exactly; an unknown changing field rejects.
NUMERICAL_KEYS = set('''modes spacing depth physicalDepth steps quadrature linearFar
linearSteps linearMethod fastJacobian cuspAwareFlow actualCuspGrid
solveTolerance auditSteps maxIterations traceFile initialCheckpoint
harmonicAmplitudePredictor shootingParts warpSteps quadratureTolerance
cuspAwareQuadrature maxCachedBetas nodeIndex rhsEvaluation projectionFloor
farPadding'''.split())


def check(ok, text):
    if not ok:
        raise ValueError(text)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def grid(path):
    t = IntegratedTail(path)
    if t.unscaled_lengths is None:
        nodes = [Q(float(x)) for x in t.r_display]
    else:
        radial = t.meta['radialGeometry']
        nodes = [Q(radial['innerAnchor'])]
        for length in t.unscaled_lengths:
            check(length > 0, 'nonpositive radial increment')
            nodes.append(nodes[-1]+t.radial_scale*Q(float(length)))
        check(nodes[-1] == Q(radial['outerAnchor']), 'outer anchor mismatch')
    cuff = Q(t.meta['parameters']['rCuff'])
    check(cuff > 0 and cuff < nodes[0], 'invalid cuff or collar')
    check(all(a < b for a, b in zip(nodes[:-1], nodes[1:])),
          'radial grid is not strictly increasing')
    check(nodes[-1] == Q(t.meta['parameters']['rCut']),
          'finite grid does not reach the same cut')
    return t.meta, [cuff]+nodes


def fraction_vectors(values):
    pairs = [(float(qbounds(q).lo), float(qbounds(q).hi)) for q in values]
    return I(np.array([x[0] for x in pairs]), np.array([x[1] for x in pairs]))


def affine_coefficients(low, high, alpha, beta):
    """Vectorized outward power-basis substitution x=alpha+beta*tau."""
    n, size = low.shape
    degree = size-1
    one = I(np.ones(n))
    apow, bpow = [one], [one]
    for _ in range(degree):
        apow.append(apow[-1]*alpha)
        bpow.append(bpow[-1]*beta)
    out_lo, out_hi = np.empty_like(low), np.empty_like(high)
    for j in range(size):
        value = I(np.zeros(n))
        for k in range(j, size):
            value = value+I(low[:, k], high[:, k])*qbounds(Q(math.comb(k, j)))*apow[k-j]
        value = value*bpow[j]
        out_lo[:, j], out_hi[:, j] = value.lo, value.hi
    return out_lo, out_hi


def write_npz(prefix, arrays):
    stream = io.BytesIO()
    np.savez_compressed(stream, **arrays)
    payload = stream.getvalue()
    if len(payload) > 1_000_000:
        payload = gzip.compress(payload, mtime=0)
        path = Path(str(prefix)+'.npz.gz')
    else:
        path = Path(str(prefix)+'.npz')
    check(len(payload) < 5_000_000, 'transfer output exceeds the per-file limit')
    path.write_bytes(payload)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ['old-manifest', 'new-manifest', 'packet', 'out-prefix']:
        parser.add_argument('--'+key, type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    old_meta, old_nodes = grid(args.old_manifest)
    new_meta, new_nodes = grid(args.new_manifest)
    old_p, new_p = old_meta['parameters'], new_meta['parameters']
    different = [k for k in sorted(set(old_p)|set(new_p))
                 if old_p.get(k) != new_p.get(k)]
    check(all(k in NUMERICAL_KEYS for k in different),
          'changing an unapproved physical parameter: '+', '.join(
              k for k in different if k not in NUMERICAL_KEYS))
    check(old_nodes[0] == new_nodes[0] and old_nodes[-1] == new_nodes[-1],
          'physical background domains differ')
    old_info = SimpleNamespace(path=args.old_manifest, N=len(old_nodes)-2)
    packet, source, source_path = consumer.load_packet(args.packet, old_info)
    check(packet.get('finished') is True, 'input packet is not complete')

    left, right = [], []
    for index, a, b in zip(source['span_index'], source['u_left'], source['u_right']):
        k = int(index)+1
        r0, length = old_nodes[k], old_nodes[k+1]-old_nodes[k]
        left.append(r0+length*Q(float(a)))
        right.append(r0+length*Q(float(b)))
    check(left[0] == old_nodes[0] and right[-1] == old_nodes[-1],
          'old packet physical endpoints differ')
    check(all(a < b for a, b in zip(left, right)) and
          all(b == a for b, a in zip(right[:-1], left[1:])),
          'old physical packet has gaps or overlaps')
    boundaries = right[:-1]

    indices, local_left, local_right = [], [], []
    owners, destinations, aq, bq = [], [], [], []
    slivers = 0
    for k, (r0, r1) in enumerate(zip(new_nodes[:-1], new_nodes[1:])):
        length = r1-r0
        partition = {0., 1.}
        for boundary in boundaries[bisect_right(boundaries, r0):bisect_left(boundaries, r1)]:
            u = (boundary-r0)/length
            box = qbounds(u)
            lo, hi = max(0., float(box.lo)), min(1., float(box.hi))
            check(0 <= lo <= hi <= 1, 'invalid rounded partition boundary')
            partition.update((lo, hi))
            slivers += int(lo != hi)
        partition = sorted(partition)
        for a, b in zip(partition[:-1], partition[1:]):
            check(a < b, 'duplicate local partition interval')
            lo, hi = r0+length*Q(a), r0+length*Q(b)
            first = bisect_right(right, lo)
            stop = bisect_left(left, hi)
            check(first < stop, 'new physical box has no old owner')
            check(left[first] <= lo and right[stop-1] >= hi,
                  'old pieces do not cover a new physical box')
            row = len(indices)
            indices.append(k-1)
            local_left.append(a)
            local_right.append(b)
            for owner in range(first, stop):
                check(left[owner] < hi and right[owner] > lo,
                      'an old owner has no positive-length intersection')
                width = right[owner]-left[owner]
                owners.append(owner)
                destinations.append(row)
                aq.append((lo-left[owner])/width)
                bq.append((hi-lo)/width)
    owner = np.array(owners, dtype=np.int64)
    destination = np.array(destinations, dtype=np.int64)
    alpha, beta = fraction_vectors(aq), fraction_vectors(bq)
    n = len(indices)
    arrays = {'span_index': np.array(indices, dtype=np.int64),
              'u_left': np.array(local_left), 'u_right': np.array(local_right)}
    for field in ['w', 'wr']:
        old_low, old_high = source[field+'_lo'], source[field+'_hi']
        transformed_low, transformed_high = affine_coefficients(
            old_low[owner], old_high[owner], alpha, beta)
        low = np.full((n, old_low.shape[1]), np.inf)
        high = np.full((n, old_low.shape[1]), -np.inf)
        np.minimum.at(low, destination, transformed_low)
        np.maximum.at(high, destination, transformed_high)
        remainder = np.zeros(n)
        np.maximum.at(remainder, destination, source[field+'_remainder'][owner])
        check(np.isfinite(low).all() and np.isfinite(high).all() and
              np.all(low <= high), 'invalid transferred coefficients')
        arrays[field+'_lo'], arrays[field+'_hi'] = low, high
        arrays[field+'_remainder'] = remainder
    counts = np.bincount(destination, minlength=n)
    arrays['old_piece_count'] = counts
    data = write_npz(args.out_prefix, arrays)
    report = {
        'status': 'same-background-grid-transfer-conditional-on-reviewed-input-packet',
        'scope': __doc__, 'finished': True,
        'finite_tail_manifest_sha256': sha(args.new_manifest),
        'data_file': data.name, 'data_sha256': sha(data),
        'background_definition_hashes': packet.get('background_definition_hashes', {}),
        'input_packet': str(args.packet), 'input_packet_sha256': sha(args.packet),
        'input_data_sha256': sha(source_path),
        'old_manifest': str(args.old_manifest), 'old_manifest_sha256': sha(args.old_manifest),
        'new_manifest': str(args.new_manifest), 'new_manifest_sha256': sha(args.new_manifest),
        'script_sha256': sha(__file__),
        'reader_sha256': sha(HERE/'db6f_tail_integrated.py'),
        'interval_backend_sha256': sha(HERE/'db6f-audit-continuous-hermite.py'),
        'packet_validator_sha256': sha(HERE/'db6f-audit-tail-metric-curvature.py'),
        'different_numerical_parameter_keys': different,
        'all_other_parameters_identical': True,
        'old_rows': len(left), 'rows': n,
        'old_finite_spans': len(old_nodes)-2, 'new_finite_spans': len(new_nodes)-2,
        'rounded_boundary_pairs': slivers,
        'multiple_old_piece_rows': int(np.count_nonzero(counts > 1)),
        'maximum_old_pieces_per_row': int(counts.max()),
        'coefficient_basis': 'Power coefficients in each new local tau; pointwise interval-polynomial enclosure.',
        'background_curvature_bound': packet.get('background_curvature_bound', 6),
        'mathematical_scope': 'Values of w and wr only. Do not differentiate these packet polynomials.',
        'not_certified': ['analytic validity of original background packet',
                          'metric or curvature of the new finite perturbation',
                          'README completion'],
        'seconds': time.time()-started}
    out = Path(str(args.out_prefix)+'.json')
    out.write_text(json.dumps(report, indent=2)+'\n')
    # Independently authored consumer performs its complete new-grid checks.
    consumer.load_packet(out, SimpleNamespace(path=args.new_manifest, N=len(new_nodes)-2))
    print(json.dumps({k: report[k] for k in ['finished', 'old_rows', 'rows',
                     'multiple_old_piece_rows', 'maximum_old_pieces_per_row', 'seconds']}))


if __name__ == '__main__':
    main()
