#!/usr/bin/env python3
"""Exact cap identities and independent complete cross-cap pilot comparison."""
from fractions import Fraction as Q
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


def multiply(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def derivative(a):
    return [Q(i)*a[i] for i in range(1, len(a))]


def value(a, x):
    return sum((c*x**k for k, c in enumerate(a)), Q(0))


def load_packet(path):
    meta = json.loads(path.read_text())
    data_path = path.parent / meta['data_file']
    assert sha(data_path) == meta['data_sha256']
    raw = data_path.read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as data:
        arrays = {key: data[key].copy() for key in data.files}
    return meta, arrays


def main():
    # J(t) is exact. Verify the upper-seam factorization in Q[t].
    J = [Q(0)]*5 + [Q(7), Q(-14), Q(10), Q(-5, 2)]
    high = [2*x for x in J]
    high[0] += 1
    high[1] -= 2
    factor = [Q(1)]
    for _ in range(5):
        factor = multiply(factor, [Q(1), Q(-1)])
    factor = multiply(factor, list(map(Q, [1, 3, 5, 5])))
    assert high == factor
    low_difference, high_difference = J[:], high[:]
    for order in range(5):
        assert value(low_difference, Q(0)) == 0
        assert value(high_difference, Q(1)) == 0
        low_difference = derivative(low_difference)
        high_difference = derivative(high_difference)
    expected = '2c8e3c30cd7a23ee2d4c74fca9833b3454085889a28ac5fcf044029b66a4bdf3'
    assert sha(ROOT / 'scripts/db6f-tail-background-packet-c4.py') == expected
    paths = [NOTES / ('2026-11-09-' + name + '.json') for name in
             ['db6f-tail-background-c4-pilot-cap',
              'db6f-root-background-c4-pilot-cap-replay']]
    inputs = [load_packet(p) for p in paths]
    a, b = inputs[0][1], inputs[1][1]
    assert set(a) == set(b)
    for key in a:
        assert a[key].dtype == b[key].dtype
        assert a[key].shape == b[key].shape
        assert a[key].tobytes() == b[key].tobytes(), key
    fields = ['finished', 'rows', 'finite_tail_manifest_sha256',
              'primitive_sha256', 'background_definition_hashes', 'source_hashes',
              'unmet_tolerance_rows', 'cap_crossing_w_taylor_calls',
              'maximum_w_total_uncertainty', 'maximum_radial_residual',
              'maximum_w_remainder', 'maximum_wr_remainder']
    assert all(inputs[0][0][k] == inputs[1][0][k] for k in fields)
    assert inputs[1][0]['cap_crossing_w_taylor_calls'] == 3
    assert inputs[1][0]['rows'] == 3
    report = dict(
        status='PASS-exact-C4-identities-static-method-and-independent-cross-cap-replay',
        review_script_sha256=sha(Path(__file__)),
        reviewed_script_sha256=expected,
        reviewed_note_sha256=sha(NOTES / '2026-11-09-db6f-tail-cap-c4-taylor.md'),
        report_sha256=[sha(p) for p in paths],
        exact_rational_cap_identity=True,
        exact_derivative_matching_orders=list(range(5)),
        all_pilot_arrays_bitwise_identical=True,
        matching_report_fields=fields, rows=3, cross_cap_taylor_calls=3,
        maximum_w_total_uncertainty=inputs[1][0]['maximum_w_total_uncertainty'],
        completed_replay_exit_code=0,
        scope=('C4 regularity and Taylor enclosure for w(x) within one source '
               'profile only. No C4 assertion for abs(w_x), the radial primitive, '
               'or profile joins. Physical-radius transport still uses the '
               'separately proved Lipschitz bound. No new actual metric bound.'))
    (NOTES / '2026-11-09-db6f-root-review-cap-c4.json').write_text(
        json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps({k: report[k] for k in
                      ['status', 'rows', 'cross_cap_taylor_calls',
                       'maximum_w_total_uncertainty']}))


if __name__ == '__main__':
    main()
