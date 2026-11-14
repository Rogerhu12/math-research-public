#!/usr/bin/env python3
"""Check every row, partition and binding of a completed metric-only run.

This does not independently recompute Fourier/Bernstein residuals. Their
mathematical backend has separate independent reviews and full regression.
The purpose here is to pay output completeness and same-map input binding.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent


def check(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def locate(path, parent):
    p = Path(path)
    return p if p.exists() else parent/p.name


def raw(path):
    value = Path(path).read_bytes()
    return gzip.decompress(value) if value[:2] == b'\x1f\x8b' else value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--curvature-report', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    report = json.loads(args.report.read_text())
    old = json.loads(args.curvature_report.read_text())
    n = report['total_finite_spans']
    check(n == old['total_finite_spans'] and report['manifest_sha256'] == old['manifest_sha256'], 'Different finite map')
    check(report['entire_finite_tail_and_collar_covered'] is True
          and report['complete_packet_partition_validated'] is True
          and report['collar_included'] is True
          and report['selected_span_interval'] == [-1, n]
          and report['curvature_evaluated'] is False
          and report['curvature_certified'] is False
          and report['metric_immersion_certified_on_checked_intervals'] is True, 'Incomplete or overstated report')
    for name, digest in report['source_sha256'].items():
        check(sha(HERE/name) == digest, 'Changed backend '+name)
    check(sha(HERE/'db6f-audit-tail-metric-only.py') == report['script_sha256'], 'Changed wrapper')
    manifest = locate(report['manifest'], args.report.parent)
    check(sha(manifest) == report['manifest_sha256'], 'Changed manifest')
    packet = locate(report['packet'], args.report.parent)
    check(sha(packet) == report['packet_sha256'], 'Changed packet metadata')
    meta = json.loads(packet.read_text())
    check(meta['finished'] is True and meta['finite_tail_manifest_sha256'] == report['manifest_sha256'], 'Mismatched or unfinished packet')
    data = locate(meta['data_file'], packet.parent)
    check(sha(data) == meta['data_sha256'] == report['packet_data_sha256'], 'Changed polynomial data')
    arrays = np.load(io.BytesIO(raw(data)), allow_pickle=False)
    for name in arrays.files:
        check(np.isfinite(arrays[name]).all(), 'Nonfinite array '+name)
    for symbol in ('w', 'wr'):
        check(np.all(arrays[symbol+'_lo'] <= arrays[symbol+'_hi'])
              and np.all(arrays[symbol+'_remainder'] >= 0), 'Invalid polynomial enclosure')
    spans = arrays['span_index']
    check(np.issubdtype(spans.dtype, np.integer), 'Nonintegral span indices')
    rows_path = locate(report['row_data_file'], args.report.parent)
    check(sha(rows_path) == report['row_data_sha256'], 'Changed residual rows')
    rows = json.loads(raw(rows_path))
    check(len(rows) == len(spans) == report['checked_packet_intervals'] == report['packet_intervals'], 'Incomplete row count')
    position = 0
    for span in range(-1, n):
        previous = Q(0)
        start = position
        while position < len(spans) and spans[position] == span:
            left, right = Q(float(arrays['u_left'][position])), Q(float(arrays['u_right'][position]))
            check(left == previous and left < right <= 1, 'Gap, overlap or reversed packet interval')
            previous = right
            row = rows[position]
            check(row['packet_row'] == position and row['span_index'] == span,
                  'Residual row and polynomial packet differ')
            check(math.isfinite(row['metric_operator_upper']) and 0 <= row['metric_operator_upper'] < 1,
                  'Unproved immersion on a row')
            check(len(row['coordinate_residual_upper']) == 3 and
                  all(math.isfinite(x) and x >= 0 for x in row['coordinate_residual_upper']), 'Invalid coordinate residual')
            position += 1
        check(position > start and previous == 1, 'Missing span or incomplete local coverage')
    check(position == len(rows), 'Out-of-order extra spans')
    maximum = max(row['metric_operator_upper'] for row in rows)
    check(maximum == report['metric_operator_upper'], 'Incorrect global metric maximum')
    coordinate_max = [max(row['coordinate_residual_upper'][j] for row in rows) for j in range(3)]
    check(coordinate_max == report['coordinate_residual_upper'], 'Incorrect coordinate maxima')
    worst = report['worst_metric_packet']
    check(rows[worst['row']]['span_index'] == worst['span']
          and rows[worst['row']]['metric_operator_upper'] == maximum, 'Incorrect worst-row identifier')
    old_packet = locate(old['packet'], args.curvature_report.parent)
    check(sha(old_packet) == old['packet_sha256'], 'Changed curvature packet')
    old_meta = json.loads(old_packet.read_text())
    definitions = meta.get('background_definition_hashes')
    check(isinstance(definitions, dict) and definitions and definitions == old_meta.get('background_definition_hashes'),
          'Metric and curvature refer to different backgrounds')
    for name, item in definitions.items():
        check(sha(locate(item['file'], packet.parent)) == item['sha256'], 'Changed background definition '+name)
    result = dict(status='PASS-complete-metric-rows-partition-and-same-map-binding', scope=__doc__,
        script_sha256=sha(__file__), report=str(args.report), report_sha256=sha(args.report),
        curvature_report=str(args.curvature_report), curvature_report_sha256=sha(args.curvature_report),
        manifest_sha256=sha(manifest), packet_sha256=sha(packet), packet_data_sha256=sha(data),
        rows_sha256=sha(rows_path), checked_rows=len(rows), finite_spans=n,
        collar_and_all_spans_exact_partition=True, global_metric_maximum=maximum,
        coordinate_residual_maxima=coordinate_max, all_backend_hashes_verified=True,
        identical_nonempty_background_definitions=definitions,
        curvature_recomputed=False, fixed_g_convergence_gate_5_paid=False)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], rows=len(rows), metric=maximum)))


if __name__ == '__main__':
    main()
