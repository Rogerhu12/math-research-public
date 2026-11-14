#!/usr/bin/env python3
"""Public Actions wrapper for the disjoint R698 exact finite window."""
import argparse
import datetime as dt
import gzip
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import traceback
from R698_fast_scalar_window import run, primes_in_interval
from p41_public_actions_recovery import publish, sha, read, REPO, TOPIC


def save_atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode()
    tmp = path.with_name(path.name+'.tmp')
    if path.suffix == '.gz':
        raw = gzip.compress(raw, mtime=0)
    tmp.write_bytes(raw)
    tmp.replace(path)


def stop(signum, frame):
    raise InterruptedError('Received signal '+str(signum))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['compute', 'publish', 'verify'])
    parser.add_argument('--shard', type=int, required=True)
    args = parser.parse_args()
    request_path = TOPIC/'notes/R698-public-window-request.json'
    request = read(request_path)
    assert request['lower'] > 2000
    assert request['residues_mod9'] == [2, 5]
    assert 0 <= args.shard < request['shards']
    result = 'R698-window-'+str(args.shard)
    out = Path(os.environ['RUNNER_TEMP'])/'serre-cartier'/result
    out.mkdir(parents=True, exist_ok=True)
    if args.mode == 'publish':
        return publish({'result': result}, out, artifact_prefix='serre-cartier')
    if args.mode == 'verify':
        return 0 if read(out/'summary.json')['complete'] else 1
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    arithmetic = Path(__file__).with_name('R698_fast_scalar_window.py')
    hashes = {'arithmetic_source_sha256': sha(arithmetic),
              'wrapper_source_sha256': sha(Path(__file__)),
              'publisher_source_sha256': sha(Path(__file__).with_name('p41_public_actions_recovery.py')),
              'parameters_sha256': sha(request_path),
              'root_readme_sha256': sha(REPO/'README.md'),
              'topic_readme_sha256': sha(TOPIC/'README.md')}
    primes = primes_in_interval(request['lower'], request['upper'])
    selected = primes[args.shard::request['shards']]
    initial = {'source_commit': source, 'result': result,
               'repository': 'Rogerhu12/math-research-public', 'request': request,
               'selected_primes': selected, 'all_window_primes': primes,
               'mathematical_scope': 'Exact finite window only; a zero is a valid result.',
               'all_prime_nonvanishing_proved': False, **hashes}
    save_atomic(out/'public-actions-input.json', initial)
    # Preserve exact executable and parameter bytes with deterministic gzip.
    for path in [arithmetic, Path(__file__), request_path]:
        (out/(path.name+'.gz')).write_bytes(gzip.compress(path.read_bytes(), mtime=0))
    import flint
    rows = []
    error = None

    def checkpoint(complete=False):
        save_atomic(out/'rows.json.gz', rows)
        save_atomic(out/'summary.json', {
            'complete': complete, 'result': result, 'source_commit': source,
            'expected_primes': selected, 'tested_count': len(rows),
            'zeros': [row for row in rows if row['zero_channels']],
            'rows_file': 'rows.json.gz', 'rows_sha256': sha(out/'rows.json.gz'),
            'error': error, 'python_flint_version': flint.__version__,
            'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'all_prime_nonvanishing_proved': False, **hashes})

    checkpoint()
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    try:
        for p in selected:
            value = run(p)
            value.update({'source_commit': source, 'python_flint_version': flint.__version__, **hashes})
            cert = out/('prime-'+str(p)+'.json.gz')
            save_atomic(cert, value)
            row = {key: value[key] for key in ['prime', 'N', 'A_p', 'A_p_minus_3',
                   'C_p', 'C_p_minus_3', 'coefficient_TC', 'coefficient_TZ3',
                   'zero_channels', 'runtime_seconds']}
            row.update({'certificate': cert.name, 'certificate_sha256': sha(cert)})
            rows.append(row)
            checkpoint()
            print(json.dumps(row), flush=True)
    except BaseException as exc:
        error = type(exc).__name__+': '+str(exc)
        (out/'failure.txt').write_text(traceback.format_exc())
    complete = error is None and [row['prime'] for row in rows] == selected
    checkpoint(complete=complete)
    return 0 if complete else 1


if __name__ == '__main__':
    sys.exit(main())
