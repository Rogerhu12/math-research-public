#!/usr/bin/env python3
"""Verify the completed independent M12 metric replay without a third run."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent/'notes'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    paths = {key: NOTES/('2026-11-09-db6f-'+stem+'.json') for key, stem in {
        'author': 'audit-tail-m12-critical-lowmetric-full',
        'replay': 'root-tail-m12-critical-lowmetric-replay',
        'root_comparison': 'root-review-m12-full-metric-replay'}.items()}
    records = {key: json.loads(path.read_text()) for key, path in paths.items()}
    check(sha(paths['root_comparison']) ==
          '73f3678feb51c2d61ea3378c751311d0b2926ae68cc223ea974575daaa702fae',
          'Unexpected frozen independent comparison')
    author, replay, summary = [records[k] for k in ('author', 'replay', 'root_comparison')]
    row_paths = {}
    rows = {}
    for key, report in [('author', author), ('replay', replay)]:
        row_paths[key] = NOTES/Path(report['row_data_file']).name
        check(sha(row_paths[key]) == report['row_data_sha256'], 'Changed completed row data')
        rows[key] = json.loads(gzip.decompress(row_paths[key].read_bytes()))
        check(report['entire_finite_tail_and_collar_covered'] is True and
              report['collar_included'] is True and
              report['checked_packet_intervals'] == report['packet_intervals'] == 30971,
              'Incomplete finite-domain coverage')
    check(len(rows['author']) == len(rows['replay']) == 30971, 'Wrong completed row count')
    check(rows['author'] == rows['replay'], 'A replayed row differs')
    # Only these three fields actually differ. No input path/hash is ignored.
    allowed = {'row_data_file', 'seconds', 'peak_process_rss_bytes'}
    different = {key for key in set(author)|set(replay) if author.get(key) != replay.get(key)}
    check(different <= allowed, 'A mathematical or input field differs')
    check(max(row['metric_operator_upper'] for row in rows['replay']) ==
          replay['metric_operator_upper'], 'Reported maximum is not the row maximum')
    check(summary['actual_exit_code'] == 0 and summary['all_rows_exactly_equal'] is True and
          summary['all_mathematical_report_fields_exactly_equal'] is True,
          'Independent completion was not recorded')
    for name, label in [('original_report_sha256', 'author'), ('independent_report_sha256', 'replay')]:
        check(summary[name] == sha(paths[label]), 'Unbound completion report')
    for name, label in [('original_rows_sha256', 'author'), ('independent_rows_sha256', 'replay')]:
        check(summary[name] == sha(row_paths[label]), 'Unbound completion rows')
    result = dict(status='PASS-independent-completed-replay-file-and-all-row-check',
        script_sha256=sha(__file__),
        inputs={key: dict(file=str(path), sha256=sha(path)) for key, path in paths.items()},
        rows={key: dict(file=str(path), sha256=sha(path)) for key, path in row_paths.items()},
        rows_exactly_equal=30971, actual_differing_report_fields=sorted(different),
        all_mathematical_and_input_fields_exactly_equal=True,
        maximum_metric_operator_upper=replay['metric_operator_upper'],
        completed_backend_exit_code_recorded_by_operator=0,
        third_backend_run_performed=False, fixed_g_convergence_gate_5_paid=False,
        final_fresh_end_to_end_review_completed=False)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'rows_exactly_equal', 'maximum_metric_operator_upper')}))


if __name__ == '__main__':
    main()
