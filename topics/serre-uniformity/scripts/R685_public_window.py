#!/usr/bin/env python3
"""Compute a disjoint exact finite window; zeros are recorded, not guessed."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
from R685_modular_kronecker import run
from p41_public_actions_recovery import publish, save, sha, read, REPO, TOPIC

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['compute', 'publish', 'verify'])
    parser.add_argument('--shard', type=int, required=True)
    args = parser.parse_args()
    request = read(TOPIC / 'notes/R685-public-window-request.json')
    assert 0 <= args.shard < request['shards']
    result = 'R685-window-' + str(args.shard)
    out = Path(os.environ['RUNNER_TEMP']) / 'serre-cartier' / result
    out.mkdir(parents=True, exist_ok=True)
    if args.mode == 'publish':
        return publish({'result': result}, out, artifact_prefix='serre-cartier')
    if args.mode == 'verify':
        return 0 if read(out / 'summary.json')['complete'] else 1
    from math import isqrt
    primes = [p for p in range(request['lower'], request['upper'] + 1)
              if p % 9 in request['residues_mod9']
              and all(p % d for d in range(2, isqrt(p) + 1))]
    selected = primes[args.shard::request['shards']]
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    save(out / 'public-actions-input.json', {'source_commit': source, 'result': result,
        'repository': 'Rogerhu12/math-research-public', 'request': request,
        'selected_primes': selected, 'all_window_primes': primes,
        'mathematical_scope': 'Exact finite window only; no all-prime nonvanishing claim.',
        'arithmetic_source_sha256': sha(Path(__file__).with_name('R685_modular_kronecker.py')),
        'root_readme_sha256': sha(REPO / 'README.md'),
        'topic_readme_sha256': sha(TOPIC / 'README.md')})
    rows = []
    error = None
    try:
        for p in selected:
            value = run(p)
            save(out / ('prime-' + str(p) + '.json'), value)
            values = {r['k']: r['Ck_mod_p'] for r in value['exact_reductions']}
            row = {'p': p, 'Cp': values[p], 'C_p_minus_3': values[p - 3],
                   'zero_weights': [k for k, v in values.items() if v == 0],
                   'certificate_sha256': sha(out / ('prime-' + str(p) + '.json'))}
            rows.append(row)
            save(out / 'summary.json', {'complete': False, 'rows': rows,
                'expected_primes': selected, 'zeros': [r for r in rows if r['zero_weights']]})
            print(json.dumps(row), flush=True)
    except Exception as exc:
        error = type(exc).__name__ + ': ' + str(exc)
    complete = error is None and [r['p'] for r in rows] == selected
    save(out / 'summary.json', {'complete': complete, 'rows': rows,
        'expected_primes': selected, 'zeros': [r for r in rows if r['zero_weights']],
        'error': error, 'source_commit': source,
        'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'all_prime_nonvanishing_proved': False})
    return 0 if complete else 1

if __name__ == '__main__':
    sys.exit(main())
