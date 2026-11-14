#!/usr/bin/env python3
"""Collect returned R685 exact certificates without repeating their computation."""
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect(directory, topic):
    request = read(topic / 'notes/R685-public-window-request.json')
    expected = [p for p in range(request['lower'], request['upper'] + 1)
                if p % 9 in request['residues_mod9']
                and all(p % d for d in range(2, isqrt(p) + 1))]
    arithmetic_sha = digest(topic / 'scripts/R685_modular_kronecker.py')
    rows, inputs, certificates = [], [], []
    for shard in range(request['shards']):
        base = directory / ('shard-' + str(shard))
        initial = read(base / 'public-actions-input.json')
        summary = read(base / 'summary.json')
        assert initial['request'] == request
        assert initial['arithmetic_source_sha256'] == arithmetic_sha
        assert initial['all_window_primes'] == expected
        assert summary['complete'] and summary['error'] is None
        selected = expected[shard::request['shards']]
        assert initial['selected_primes'] == summary['expected_primes'] == selected
        assert [r['p'] for r in summary['rows']] == selected
        assert summary['zeros'] == [r for r in summary['rows'] if r['zero_weights']]
        for row in summary['rows']:
            p = row['p']
            path = base / ('prime-' + str(p) + '.json')
            assert digest(path) == row['certificate_sha256']
            value = read(path)
            residues = {x['k']: x['Ck_mod_p'] for x in value['exact_reductions']}
            assert residues == {p: row['Cp'], p - 3: row['C_p_minus_3']}
            assert all(0 <= a < p for a in residues.values())
            assert row['zero_weights'] == [k for k, a in residues.items() if a == 0]
            rows.append(row)
            certificates.append({'shard': shard, 'prime': p,
                                 'sha256': row['certificate_sha256']})
        inputs.append({'shard': shard, 'source_commit': initial['source_commit'],
                       'summary_sha256': digest(base / 'summary.json'),
                       'input_sha256': digest(base / 'public-actions-input.json'),
                       'count': len(selected)})
    rows.sort(key=lambda x: x['p'])
    assert [r['p'] for r in rows] == expected
    direct = read(topic / 'notes/R687_direct1013.json')
    row = next(x for x in rows if x['p'] == 1013)
    assert row['Cp'] == direct['Cp_predicted_by_R658']
    assert row['C_p_minus_3'] == direct['Cp_minus3_predicted_by_R683']
    return {'result': 'R689', 'finite_window_complete': True,
            'request': request, 'prime_count': len(expected), 'shards': inputs,
            'arithmetic_source_sha256': arithmetic_sha,
            'run_id': '43580270602', 'attempt': 1,
            'rows': rows, 'zeros': [r for r in rows if r['zero_weights']],
            'independent_direct_1013_comparison': {
                'r2': direct['r2'], 'r3': direct['r3'],
                'Cp': row['Cp'], 'C_p_minus_3': row['C_p_minus_3'],
                'direct_certificate_sha256': digest(topic / 'notes/R687_direct1013.json')},
            'all_prime_nonvanishing_claimed': False,
            'computation_repeated_by_collector': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--returned-directory', type=Path, required=True)
    parser.add_argument('--topic', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = collect(args.returned_directory, args.topic)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'count': result['prime_count'], 'zeros': result['zeros'],
                      'independent_1013': result['independent_direct_1013_comparison']}))
