#!/usr/bin/env python3
"""Compare independent complete background and consumer replays, without arrays on stdout."""
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT/'notes'
P = '2026-11-09-db6f-'


def path(name):
    return NOTES/(P+name)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(p):
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_bytes())


def arrays(report):
    meta = load(report)
    data = report.parent/meta['data_file']
    assert sha(data) == meta['data_sha256']
    raw = data.read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)
    with np.load(io.BytesIO(raw), allow_pickle=False) as z:
        return {k: np.array(z[k], copy=True) for k in z.files}


def main():
    reports = {}
    files = {}
    def pair(name, a, b):
        pa, pb = path(a), path(b)
        files[name] = {'author': pa.name, 'author_sha256': sha(pa),
                       'replay': pb.name, 'replay_sha256': sha(pb)}
        return load(pa), load(pb)
    a, b = pair('primitive', 'tail-background-primitive-stable-depth2.json.gz',
                 'root-review-background-primitive-stable-depth2.json.gz')
    assert a.keys() == b.keys()
    assert all(a[k] == b[k] for k in a if k not in ['seconds', 'settings'])
    assert {k:v for k,v in a['settings'].items() if k != 'out'} == {
        k:v for k,v in b['settings'].items() if k != 'out'}
    expected = {(n, k) for n in range(2) for k in range(9)}
    assert {(z['n'], z['segment']) for z in a['profiles']} == expected
    assert a['finished'] and b['finished'] and len(a['profiles']) == 18
    reports['primitive'] = {'complete_profiles': 18, 'all_fields_and_inputs_identical': True,
                            'analytic_leaves': sum(z['analyticLeaves'] for z in a['profiles']),
                            'range_leaves': sum(z['rangeLeaves'] for z in a['profiles'])}
    author_prefix = path('tail-background-tight-int2-prefix.json')
    root_prefix = path('root-review-background-packet-prefix.json')
    pair('strict_prefix', author_prefix.name[len(P):], root_prefix.name[len(P):])
    a, b = arrays(author_prefix), arrays(root_prefix)
    mask = a['span_index'] >= 0
    assert a.keys() == b.keys() and all(np.array_equal(a[k][mask], b[k]) for k in a)
    assert len(b['span_index']) == 4999
    c = arrays(path('tail-background-coarse-int2.json'))
    for k in c:
        if k not in a:
            continue
        left, right = c[k][c['span_index'] == -1], a[k][a['span_index'] == -1]
        if left.ndim == 2:
            left = np.pad(left, ((0,0),(0,right.shape[1]-left.shape[1])))
        assert np.array_equal(left, right)
    reports['strict_prefix'] = {'replayed_rows': 4999, 'all_arrays_identical': True,
                                 'collar_equal_to_reviewed_coarse_after_zero_padding': True}
    final_author = path('audit-tail-tight-final-packet.json')
    final_root = path('root-review-final-reconstructed-packet.json')
    pair('assembled_packet', final_author.name[len(P):], final_root.name[len(P):])
    a, b = arrays(final_author), arrays(final_root)
    assert a.keys() == b.keys() and all(np.array_equal(a[k], b[k]) for k in a)
    replay = load(path('root-review-final-background-replay.json'))
    assert replay['all_final_arrays_identical'] and replay['final_rows'] == 5237
    assert all(z['all_arrays_identical'] for z in replay['supplier_cases'])
    reports['assembled_packet'] = {'rows': 5237, 'all_arrays_identical': True,
                                   'replayed_suffix_cases': len(replay['supplier_cases']),
                                   'finite_plan_report_sha256': sha(path('root-review-final-background-replay.json'))}
    a, b = pair('consumer', 'audit-tail-tight-full.json', 'root-tail-tight-full-replay.json')
    excluded = {'packet', 'packet_sha256', 'row_data_file', 'seconds'}
    differences = sorted(k for k in a.keys()|b.keys() if a.get(k) != b.get(k))
    assert set(differences) <= excluded
    ar, br = NOTES/a['row_data_file'], NOTES/b['row_data_file']
    assert sha(ar) == a['row_data_sha256'] and sha(br) == b['row_data_sha256']
    assert load(ar) == load(br)
    assert a['entire_finite_tail_and_collar_covered'] and a['checked_packet_intervals'] == 5237
    reports['consumer'] = {'checked_rows': 5237, 'all_rows_identical': True,
                            'all_mathematical_report_fields_identical': True,
                            'different_metadata_fields': differences,
                            'metric_operator_upper': a['metric_operator_upper'],
                            'principal_curvature_upper': a['principal_curvature_upper'],
                            'author_rows_sha256': sha(ar), 'replay_rows_sha256': sha(br)}
    reviewed = ['db6f-audit-overlay-tail-packet.py', 'db6f-audit-tail-inherit-coarse-wr.py',
                'db6f-tail-background-packet.py', 'db6f_tail_background_primitive.py',
                'db6f-tail-build-background-primitive-stable.py',
                'db6f-audit-tail-metric-curvature.py']
    sources = {f: sha(ROOT/'scripts'/f) for f in reviewed}
    result = {'status': 'independent-complete-background-assembly-and-consumer-replays-PASS',
              'reviewer': 'Astra-visible-flex-db6f0b0e/root',
              'script_sha256': sha(__file__), 'reports': reports, 'files': files,
              'reviewed_sources_sha256': sources,
              'scope': 'Complete source primitive, complete actual finite supplier plan, exact helper assembly and full finite-tail consumer. Analytic input proofs are separately reviewed dependencies; not README completion.'}
    path('root-review-full-tail-replays.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'reports': reports}, indent=2))


if __name__ == '__main__':
    main()
