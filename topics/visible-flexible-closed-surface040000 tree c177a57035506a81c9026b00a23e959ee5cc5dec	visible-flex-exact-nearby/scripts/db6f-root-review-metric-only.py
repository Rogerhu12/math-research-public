#!/usr/bin/env python3
"""Independent complete M8 regression of the metric-only storage wrapper."""
import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'notes'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if data[:2] == b'\x1f\x8b' else data)


def main():
    before_path = NOTES / '2026-11-09-db6f-audit-tail-tight-full.json'
    after_path = NOTES / '2026-11-09-db6f-root-metric-only-m8-replay.json'
    before, after = read(before_path), read(after_path)
    row_paths = [p.parent / d['row_data_file']
                 for p, d in [(before_path, before), (after_path, after)]]
    for p, d in zip(row_paths, [before, after]):
        assert sha(p) == d['row_data_sha256']
    rows = [read(p) for p in row_paths]
    assert len(rows[0]) == len(rows[1]) == 5237
    row_keys = ['packet_row', 'span_index', 'metric_operator_upper']
    for a, b in zip(*rows):
        assert all(a[k] == b[k] for k in row_keys)
    global_keys = [
        'manifest_sha256', 'packet_sha256', 'packet_data_sha256',
        'total_finite_spans', 'collar_included', 'packet_intervals',
        'checked_packet_intervals', 'radial_subdivisions',
        'selected_span_interval', 'metric_operator_upper',
        'coordinate_residual_upper', 'worst_metric_packet',
        'entire_finite_tail_and_collar_covered',
        'metric_immersion_certified_on_checked_intervals']
    assert all(before[k] == after[k] for k in global_keys)
    assert after['complete_packet_partition_validated'] is True
    assert after['curvature_evaluated'] is False
    assert after['curvature_certified'] is False
    assert not any(k in after for k in
                   ['principal_curvature_upper', 'direct_curvature_upper',
                    'perturbative_curvature_upper'])
    report = dict(
        status='PASS-static-method-and-complete-independent-metric-regression',
        script_sha256=sha(Path(__file__)),
        reviewed_script_sha256=sha(ROOT / 'scripts/db6f-audit-tail-metric-only.py'),
        reviewed_stream_sha256=sha(ROOT / 'scripts/db6f-audit-tail-stream.py'),
        frozen_backend_sha256=sha(ROOT / 'scripts/db6f-audit-tail-metric-curvature.py'),
        before_report_sha256=sha(before_path), after_report_sha256=sha(after_path),
        before_rows_sha256=sha(row_paths[0]), after_rows_sha256=sha(row_paths[1]),
        all_rows_identical_on_metric_fields=True,
        row_fields_checked=row_keys, checked_rows=len(rows[0]),
        all_global_metric_fields_identical=True, global_fields_checked=global_keys,
        metric_operator_upper=after['metric_operator_upper'],
        no_curvature_claim=True,
        peak_process_rss_bytes=after['peak_process_rss_bytes'],
        completed_process_exit_code=0,
        scope=('Same exact finite map and complete background packet. This verifies '
               'the omission of unused second-jet and curvature calculations. It '
               'does not certify a new source ODE, background supplier, or G5.'))
    output = NOTES / '2026-11-09-db6f-root-review-metric-only.json'
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps({k: report[k] for k in
                      ['status', 'checked_rows', 'metric_operator_upper',
                       'peak_process_rss_bytes']}))


if __name__ == '__main__':
    main()
