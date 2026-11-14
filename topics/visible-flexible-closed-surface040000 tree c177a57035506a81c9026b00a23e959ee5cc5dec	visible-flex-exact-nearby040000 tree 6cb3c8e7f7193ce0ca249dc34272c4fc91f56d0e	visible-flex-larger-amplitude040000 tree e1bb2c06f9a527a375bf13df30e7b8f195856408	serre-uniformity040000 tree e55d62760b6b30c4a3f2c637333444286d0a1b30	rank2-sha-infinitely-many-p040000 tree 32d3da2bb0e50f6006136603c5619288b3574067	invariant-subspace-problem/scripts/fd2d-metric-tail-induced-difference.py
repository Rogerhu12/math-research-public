#!/usr/bin/env python3
"""Convert completed tail-difference rows in the actual old induced metric.

Radial and angular directions are scaled separately by the same exact
rotational background. No tail integration or nonlinear solver is called.
An existing background packet supplies continuous w/w_r bounds. The old
reference is explicitly the R21 first-critical M12 surface.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location('fd2d_tail_own_difference',
                                            HERE/'fd2d-metric-tail-c2-difference.py')
diff = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = diff
spec.loader.exec_module(diff)
I, qbounds, frozen = diff.I, diff.qbounds, diff.stream.frozen


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def local_path(path, directory):
    path = Path(path)
    if path.exists():
        return path
    return directory/path.name


def radial_nodes(manifest):
    """Read only radial coordinates/increments, one checked raw shard at a time."""
    meta = json.loads(manifest.read_text())
    values, increments, last = [], [], None
    for entry in meta['files']:
        path = local_path(entry['path'], manifest.parent)
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != entry['sha256']:
            raise ValueError('Radial source hash mismatch')
        data = np.frombuffer(gzip.decompress(raw), dtype='<f8').reshape(entry['rows'], entry['columns'])
        start = 0
        if last is not None:
            if not np.array_equal(data[0], last):
                raise ValueError('Raw interface differs')
            start = 1
        values.extend(Q(float(x)) for x in data[start:, 0])
        increments.extend(Q(float(x)) for x in data[start:, -1])
        last = data[-1].copy()
    if 'radialGeometry' in meta:
        radial = meta['radialGeometry']
        scale = Q(int(radial['normalization']['numerator']),
                  int(radial['normalization']['denominator']))
        values = [Q(float(radial['innerAnchor']))]
        for increment in increments[1:]:
            values.append(values[-1]+scale*increment)
        if values[-1] != Q(float(radial['outerAnchor'])):
            raise ValueError('Normalized radial increments miss outer anchor')
    nodes = [Q(float(meta['parameters']['rCuff']))]+values
    if any(a >= b for a, b in zip(nodes, nodes[1:])):
        raise ValueError('Nonpositive radial span')
    return meta, nodes


def input_rows(args, report):
    if args.rows_manifest:
        path = args.rows_manifest
        manifest = json.loads(path.read_text())
        if manifest['schema'] != 'gzip-jsonl-parts-v1':
            raise ValueError('Unknown row storage')
        if manifest['original_gzip']['sha256'] != report['continuous_rows']['sha256']:
            raise ValueError('Parts are not bound to original comparison rows')
        whole, count = hashlib.sha256(), 0
        for part in manifest['parts']:
            source = path.parent/part['file']
            if sha(source) != part['sha256'] or part['first_row'] != count:
                raise ValueError('Part identity or order mismatch')
            raw = gzip.decompress(source.read_bytes())
            if hashlib.sha256(raw).hexdigest() != part['uncompressed_sha256']:
                raise ValueError('Part logical stream mismatch')
            whole.update(raw)
            lines = raw.splitlines()
            if len(lines) != part['rows']:
                raise ValueError('Part row count mismatch')
            for line in lines:
                count += 1
                yield json.loads(line)
        if count != manifest['rows'] or whole.hexdigest() != manifest['uncompressed_sha256']:
            raise ValueError('Complete logical row stream mismatch')
    else:
        path = local_path(report['continuous_rows']['file'], args.comparison.parent)
        if sha(path) != report['continuous_rows']['sha256']:
            raise ValueError('Comparison row hash mismatch')
        with gzip.open(path, 'rt') as source:
            for line in source:
                yield json.loads(line)


def quadratic_upper(rr, rt, tt, E, r):
    A = rr/E
    B = rt/(r*E.sqrt())
    C = tt/r.square()
    return (A+C+((A-C).square()+4*B.square()).sqrt())/2


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--comparison', type=Path, required=True)
    ap.add_argument('--rows-manifest', type=Path)
    ap.add_argument('--packet', type=Path, required=True)
    ap.add_argument('--packet-manifest', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    started = time.monotonic()
    report = json.loads(args.comparison.read_text())
    if (not report['entire_tail_and_own_collar_covered']
            or report['old']['sha256'] != diff.M12_SHA):
        raise ValueError('Requires complete comparison against R21 M12')
    if sha(args.packet_manifest) not in (report['old']['sha256'], report['new']['sha256']):
        raise ValueError('Background radial partition is not one of the compared tails')
    meta, nodes = radial_nodes(args.packet_manifest)
    packet_meta, packet, packet_data = frozen.load_packet(
        args.packet, SimpleNamespace(path=args.packet_manifest, N=len(nodes)-2))
    segments = []
    for k, span in enumerate(packet['span_index']):
        index = int(span)+1
        length = nodes[index+1]-nodes[index]
        left = nodes[index]+length*Q(float(packet['u_left'][k]))
        right = nodes[index]+length*Q(float(packet['u_right'][k]))
        w = frozen.value_range(frozen.poly.target_scalar(packet, 'w', k))
        wr = frozen.value_range(frozen.poly.target_scalar(packet, 'wr', k))
        segments.append((left, right, max(1., float((1+w.square()).lo)),
                         float(wr.abs().hi)))
    if any(a[1] != b[0] for a, b in zip(segments, segments[1:])):
        raise ValueError('Background physical packet has a gap')
    if [str(segments[0][0]), str(segments[-1][1])] != report['exact_domain']:
        raise ValueError('Background does not cover complete comparison domain')
    ends = [entry[1] for entry in segments]
    c = qbounds(Q(99999997, 100000000))
    maxima = {key: {'upper': 0.} for key in ('eta', 'beta', 'Qu', 'QX')}
    count = 0
    previous = Q(report['exact_domain'][0])
    for row in input_rows(args, report):
        left, right = Q(row['left_exact']), Q(row['right_exact'])
        if row['index'] != count or left != previous or left >= right:
            raise ValueError('Comparison rows have a gap or wrong index')
        first = bisect.bisect_right(ends, left)
        last = first
        while segments[last][1] < right:
            last += 1
        if segments[first][0] > left or segments[last][1] < right:
            raise ValueError('Missing background interval')
        background = segments[first:last+1]
        E = I(min(entry[2] for entry in background))
        wr = I(max(entry[3] for entry in background))
        r = qbounds(left)
        U = {key: I(value['total']) for key, value in row['difference'].items()}
        V = {key: I(value['total']) for key, value in row['old_perturbation'].items()}
        eta = (U['r1theta0'].square()/E+U['r0theta1'].square()/r.square()).sqrt()/c.sqrt()
        Qu = quadratic_upper(U['r2theta0'], U['r1theta1'], U['r0theta2'], E, r)
        QX = quadratic_upper(wr+V['r2theta0'], 1+V['r1theta1'],
                             qbounds(right)+V['r0theta2'], E, r)
        beta = (Qu+eta*QX)/c
        for key, value in (('eta', eta), ('beta', beta), ('Qu', Qu), ('QX', QX)):
            upper = float(value.hi)
            if upper > maxima[key]['upper']:
                maxima[key] = {'upper': upper, 'index': count,
                               'left_exact': str(left), 'right_exact': str(right),
                               'background_E_lower': float(E.lo),
                               'background_wr_absolute_upper': float(wr.hi)}
        previous = right
        count += 1
    if count != report['common_spans_total'] or str(previous) != report['exact_domain'][1]:
        raise ValueError('Incomplete final comparison coverage')
    output = {'status': 'CONTINUOUS_ACTUAL_TAIL_INDUCED_DIFFERENCE',
              'comparison': diff.identity(args.comparison),
              'old_reference_sha256': diff.M12_SHA,
              'packet': diff.identity(args.packet), 'packet_data': diff.identity(packet_data),
              'packet_manifest': diff.identity(args.packet_manifest),
              'script': diff.identity(__file__),
              'complete_tail_and_own_collars': True, 'covered_spans': count,
              'exact_domain': report['exact_domain'],
              'reference_actual_metric_lower_factor_exact': str(Q(99999997,100000000)),
              'background_identity_reference': 'R21 fixed source/exact bridge and original background packet suppliers',
              'maxima': maxima, 'eta_upper': maxima['eta']['upper'],
              'beta_upper': maxima['beta']['upper'],
              'coordinate_formula': 'D=diag(1/sqrt(E),1/r); Q=lambda_max([[Urr/E,Urtheta/(r sqrt(E))],[same,Uthetatheta/r^2]])',
              'connection_formula': 'dX Gamma_h=P_TX D2X; beta <= (Qu+eta QX)/(1-e0)',
              'prefix_mean_gauge_included': False, 'whole_closed_surface_transfer': False,
              'new_metric_certificate': False, 'nonlinear_solver_calls': 0,
              'tail_integrations': 0, 'seconds': time.monotonic()-started}
    if args.rows_manifest:
        output['row_storage'] = diff.identity(args.rows_manifest)
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'out': str(args.out), 'covered': count, 'maxima': maxima,
                      'seconds': output['seconds']}, indent=2))


if __name__ == '__main__':
    main()
