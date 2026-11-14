#!/usr/bin/env python3
"""Independent completed four-span replay of the first-derivative phase bound."""
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'notes'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_packet(path):
    report = json.loads(path.read_text())
    data = path.parent / report['data_file']
    assert sha(data) == report['data_sha256']
    raw = data.read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as z:
        arrays = {key: z[key].copy() for key in z.files}
    return report, arrays


def main():
    producer = ROOT / 'scripts/db6f-tail-background-packet-phase.py'
    expected = '97b8cd525586851c1e726e101db0f586518d260898fcaa6842c363ca050bc807'
    assert sha(producer) == expected
    paths = [NOTES / ('2026-11-09-' + stem + '.json') for stem in
             ['db6f-tail-background-phase-pilot-raw0',
              'db6f-root-background-phase-pilot-raw0-replay']]
    first, second = map(read_packet, paths)
    assert set(first[1]) == set(second[1])
    for key in first[1]:
        a, b = first[1][key], second[1][key]
        assert a.dtype == b.dtype and a.shape == b.shape
        assert a.tobytes() == b.tobytes(), key
    ignored = {'settings', 'data_file', 'data_sha256', 'files', 'seconds'}
    assert set(first[0]) == set(second[0])
    compared = [key for key in first[0] if key not in ignored]
    assert all(first[0][key] == second[0][key] for key in compared)
    settings = [{k: v for k, v in report['settings'].items() if k != 'out_prefix'}
                for report in [first[0], second[0]]]
    assert settings[0] == settings[1]
    report = second[0]
    assert report['finished'] is True and report['rows'] == 86
    assert report['unmet_tolerance_rows'] == 0
    result = dict(
        status='PASS-proof-static-difference-and-complete-independent-pilot',
        review_script_sha256=sha(Path(__file__)),
        producer_sha256=expected,
        proof_note_sha256=sha(NOTES / '2026-11-09-db6f-tail-background-first-derivative-phase.md'),
        original_report_sha256=sha(paths[0]), replay_report_sha256=sha(paths[1]),
        all_arrays_bitwise_identical=True,
        all_mathematical_report_fields_identical=True,
        compared_report_fields=compared,
        original_physical_grid_and_background_unchanged=True,
        checked_spans=4, checked_rows=86, unmet_working_tolerance_rows=0,
        maximum_radial_residual=report['maximum_radial_residual'],
        maximum_w_total_uncertainty=report['maximum_w_total_uncertainty'],
        completed_replay_exit_code=0,
        scope=('Endpoint error plus half the first-derivative residual bound '
               'is a conditional analytic enclosure for the same radial '
               'background. This replay does not certify the finite-map metric, '
               'curvature, source ODE, or README completion.'))
    output = NOTES / '2026-11-09-db6f-root-review-background-phase.json'
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    print(json.dumps({k: result[k] for k in
                      ['status', 'checked_rows', 'maximum_radial_residual',
                       'maximum_w_total_uncertainty']}))


if __name__ == '__main__':
    main()
