#!/usr/bin/env python3
"""Continuous metric-only bounds for an exact finite tail and its R6 collar.

Use the reviewed low-memory geometry adapter and the frozen coefficient
metric_residuals function. The complete background partition is validated
even for a selected-range run. Only value and first-radial fields are
restricted and expanded; no curvature formula is evaluated. The shared
span cache may construct its unused second-derivative polynomial, but this
wrapper neither expands that polynomial nor makes a curvature claim.

Analytic validity of the supplied w packets is a separate proof input.
This program does not certify source ODE convergence or README completion.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as Q
import gzip
import importlib.util
import json
import math
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('db6f_metric_only_stream', HERE/'db6f-audit-tail-stream.py')
stream = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = stream
spec.loader.exec_module(stream)
frozen, poly, qbounds = stream.frozen, stream.poly, stream.qbounds


def first_fields(geom, index, left, right):
    """The first two entries of the reviewed fields method, unchanged."""
    raw_polys = geom.collar if index == -1 else geom.span_polys(index)
    result = []
    for raw in raw_polys[:2]:
        local = poly.compose(raw, qbounds(left), qbounds(right-left))
        result.append(geom.expand(local))
    return result


def run(args):
    started = time.monotonic()
    frozen.check(args.radial > 0, 'Positive radial subdivision count required')
    frozen.check(args.block_size > 0, 'Positive streaming block size required')
    frozen.check(args.progress >= 0, 'Progress interval must be nonnegative')
    source_hashes = {name: frozen.sha(HERE/name) for name in (
        Path(__file__).name, 'db6f-audit-tail-stream.py',
        'db6f-audit-tail-metric-curvature.py', 'db6f-audit-metric-polynomial.py',
        'db6f-audit-continuous-hermite.py', 'db6f_tail_integrated.py')}
    geom = stream.StreamingExactIntegratedTail(args.manifest, block_size=args.block_size)
    meta, data, data_path = frozen.load_packet(args.packet, geom)
    frozen.check(meta.get('finished') is True, 'Background packet is not marked complete')
    stop = geom.N if args.maximum_span_exclusive is None else args.maximum_span_exclusive
    frozen.check(-1 <= args.minimum_span < stop <= geom.N, 'Invalid selected span range')
    selected = np.flatnonzero((data['span_index'] >= args.minimum_span)
                              & (data['span_index'] < stop))
    if args.limit is not None:
        frozen.check(args.limit > 0, 'A pilot limit must be positive')
        selected = selected[:args.limit]
    frozen.check(len(selected) > 0, 'No selected packet intervals')

    rows = []
    out = dict(
        status='continuous-finite-tail-metric-only-conditional-on-background-packet',
        scope=__doc__, script_sha256=source_hashes[Path(__file__).name],
        source_sha256=source_hashes,
        manifest=str(args.manifest.resolve()), manifest_sha256=frozen.sha(args.manifest),
        packet=str(args.packet.resolve()), packet_sha256=frozen.sha(args.packet),
        packet_data_sha256=frozen.sha(data_path),
        supplier_definition=meta.get('analytic_definition'),
        supplier_independently_verified=False,
        total_finite_spans=geom.N, packet_intervals=len(data['span_index']),
        checked_packet_intervals=len(selected), selected_span_interval=[args.minimum_span, stop],
        collar_included=args.minimum_span == -1,
        radial_subdivisions=args.radial, block_size=args.block_size,
        complete_packet_partition_validated=True,
        entire_finite_tail_and_collar_covered=(args.minimum_span == -1 and stop == geom.N
                                             and len(selected) == len(data['span_index'])),
        metric_operator_upper=0., coordinate_residual_upper=[0., 0., 0.],
        worst_metric_packet=None,
        curvature_evaluated=False, curvature_certified=False,
        complete_closed_surface=False,
        not_certified=['analytic validity of supplier packets', 'principal curvature or reach',
                       'source ODE or nonlinear infinite-tail solution',
                       'complete closed-surface metric', 'README completion'])
    for row in selected:
        span = int(data['span_index'][row])
        ua, ub = frozen.exact(data['u_left'][row]), frozen.exact(data['u_right'][row])
        w0 = poly.target_scalar(data, 'w', row)
        result = dict(packet_row=int(row), span_index=span, metric_operator_upper=0.,
                      coordinate_residual_upper=[0., 0., 0.])
        for child in range(args.radial):
            a, b = Q(child, args.radial), Q(child+1, args.radial)
            left, right = ua+(ub-ua)*a, ua+(ub-ua)*b
            fields = first_fields(geom, span, left, right)
            r, _, _ = geom.interval_radius(span, left, right)
            w = frozen.restricted(w0, a, b)
            metric, errors, _, _, _, _ = frozen.metric_residuals(fields, r, w)
            frozen.check(math.isfinite(metric) and metric >= 0
                         and all(math.isfinite(x) and x >= 0 for x in errors),
                         'Nonfinite or invalid metric bound')
            result['metric_operator_upper'] = max(result['metric_operator_upper'], metric)
            result['coordinate_residual_upper'] = [max(x, y) for x, y in
                                                   zip(result['coordinate_residual_upper'], errors)]
            if metric > out['metric_operator_upper']:
                out['metric_operator_upper'] = metric
                out['worst_metric_packet'] = dict(row=int(row), span=span, child=child)
            out['coordinate_residual_upper'] = [max(x, y) for x, y in
                                                zip(out['coordinate_residual_upper'], errors)]
        rows.append(result)
        if args.progress and len(rows) % args.progress == 0:
            print(json.dumps(dict(checked=len(rows), total=len(selected),
                                  metric=out['metric_operator_upper'])), flush=True)

    out['metric_immersion_certified_on_checked_intervals'] = out['metric_operator_upper'] < 1
    out['seconds'] = time.monotonic()-started
    out['peak_process_rss_bytes'] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
    row_file = args.out.with_suffix('.rows.json.gz')
    row_file.write_bytes(gzip.compress(json.dumps(rows, separators=(',', ':'), allow_nan=False).encode(), mtime=0))
    frozen.check(row_file.stat().st_size < 5_000_000, 'Row report exceeds the repository file-size limit')
    out['row_data_file'], out['row_data_sha256'] = row_file.name, frozen.sha(row_file)
    args.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: out[key] for key in (
        'checked_packet_intervals', 'entire_finite_tail_and_collar_covered',
        'metric_operator_upper', 'curvature_evaluated', 'seconds', 'peak_process_rss_bytes')}))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'packet', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--radial', type=int, default=1)
    ap.add_argument('--minimum-span', type=int, default=-1)
    ap.add_argument('--maximum-span-exclusive', type=int)
    ap.add_argument('--limit', type=int)
    ap.add_argument('--progress', type=int, default=1000)
    ap.add_argument('--block-size', type=int, default=128)
    run(ap.parse_args())
