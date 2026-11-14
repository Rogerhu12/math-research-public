#!/usr/bin/env python3
"""Freeze immutable selected g0 inputs without fabricating a prefix sum.

At the exact requested length, a double index-read guard also captures the
actual saved accumulator.  If the live index has advanced, only the complete
immutable leaf inputs are selected; no new truncated sum is asserted.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def read_bytes(path):
    p = Path(path)
    raw = p.read_bytes()
    return raw, json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index', type=Path, required=True)
    p.add_argument('--count', type=int, required=True)
    p.add_argument('--directory', type=Path, required=True)
    a = p.parse_args()
    if not 0 < a.count <= 550:
        raise ValueError('invalid selected segment count')
    if a.directory.exists() and any(a.directory.iterdir()):
        raise ValueError('refuse to replace an existing immutable snapshot')
    for attempt in range(20):
        raw, index = read_bytes(a.index)
        if index['completed_segments'] < a.count:
            raise ValueError('the live cover has not yet completed the requested prefix')
        accumulated = None
        if index['completed_segments'] == a.count:
            accumulated = Path(index['accumulator_path']).read_bytes()
            if sha_bytes(accumulated) != index['accumulator_sha256']:
                time.sleep(.2)
                continue
        if a.index.read_bytes() == raw:
            break
        time.sleep(.2)
    else:
        raise ValueError('no stable index/accumulator pair was observed')
    selected = [row for row in index['leaves'] if row['segment'] < a.count]
    for segment in range(a.count):
        rows = sorted((r for r in selected if r['segment'] == segment),
                      key=lambda r: Fraction(r['normalized_subspan'][0]))
        spans = [tuple(map(Fraction, r['normalized_subspan'])) for r in rows]
        if (not spans or spans[0][0] != 0 or spans[-1][1] != 1
            or any(x[1] != y[0] for x, y in zip(spans, spans[1:]))):
            raise ValueError('selected complete leaves have a partition gap')
    first_files = []
    for row in selected:
        report_raw, report = read_bytes(row['path'])
        if (sha_bytes(report_raw) != row['sha256'] or not report.get('complete')
            or not report.get('complete_continuous_true_density_proved')):
            raise ValueError('selected actual g0 report changed or is incomplete')
        link = report['first_integral_file']
        first_raw, first = read_bytes(link['path'])
        if (sha_bytes(first_raw) != link['sha256']
            or first['identity'] != report['identity']
            or first['density_coefficient_sha256'] != report['density_coefficient_sha256']):
            raise ValueError('selected finite first integral changed its actual density')
        first_files.append(dict(path=link['path'], sha256=link['sha256'], bytes=len(first_raw)))
    a.directory.mkdir(parents=True, exist_ok=True)
    (a.directory/'observed_index.json').write_bytes(raw)
    source_sha = sha_bytes(Path(__file__).read_bytes())
    if accumulated is not None:
        target = a.directory/'ordered_accumulator.json.gz'
        target.write_bytes(accumulated)
        frozen = dict(index)
        frozen['accumulator_path'] = str(target)
        frozen['snapshot_of_index_path'] = str(a.index)
        frozen['snapshot_of_index_sha256'] = sha_bytes(raw)
        frozen['snapshot_audit_source_sha256'] = source_sha
    else:
        frozen = dict(kind='immutable_selected_g0_prefix_inputs_without_new_accumulator',
            source_sha256=source_sha, descriptor_sha256=index['descriptor_sha256'],
            pipeline_sources=index['pipeline_sources'], leaves=selected,
            completed_segments=a.count, complete=False, whole_forward_leg=False,
            label_strip=index['label_strip'], inner_strip=index['inner_strip'],
            no_truncated_chronological_sum_claimed=True,
            snapshot_of_index_path=str(a.index), snapshot_of_index_sha256=sha_bytes(raw))
    frozen_path = a.directory/'index.json'
    frozen_path.write_text(json.dumps(frozen, indent=2)+'\n')
    witness = dict(kind='checked_immutable_g0_prefix_inputs', complete=True,
        source_sha256=source_sha, requested_segments=a.count,
        observed_completed_segments=index['completed_segments'],
        observed_index_path=str(a.directory/'observed_index.json'),
        observed_index_sha256=sha_bytes(raw),
        exact_double_read_guard_passed=True,
        actual_accumulator_captured=accumulated is not None,
        new_truncated_accumulator_created=False,
        frozen_index_path=str(frozen_path), frozen_index_sha256=sha_bytes(frozen_path.read_bytes()),
        all_selected_reports_and_first_integrals_hashed=True,
        selected_leaves=selected, selected_first_integrals=first_files)
    out = a.directory/'snapshot.json'
    out.write_text(json.dumps(witness, indent=2)+'\n')
    print(dict(path=str(out), sha256=sha_bytes(out.read_bytes()),
        segments=a.count, actual_accumulator_captured=accumulated is not None))


if __name__ == '__main__':
    main()
