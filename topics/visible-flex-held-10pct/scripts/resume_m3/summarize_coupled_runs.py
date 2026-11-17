#!/usr/bin/env python3
"""Collect terminal scalars and hashes, never regenerable field arrays."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def summarize(directory):
    p = Path(directory)
    summary = p / 'seed-summary.json'
    if not summary.exists():
        return dict(run=p.name, status='unfinished_no_terminal_summary')
    s = json.loads(summary.read_text())
    result = dict(run=p.name, summary_sha256=sha(summary),
                  status='accepted' if s.get('solver_success') else 'failed_original_gate',
                  solver_success=s.get('solver_success'), error=s.get('error'))
    if 'Weighted stage-tail initialization failed' in str(s.get('error')):
        result['status'] = 'startup_dependency_failure'
    for k in ['frozen_profile', 'gauge_amplitude', 'actual_primary_amplitude',
              'nodes', 'max_rms_collocation_residual', 'seconds', 'tail_calls', 'actual_outer_checks']:
        if k in s:
            result[k] = s[k]
    result['prefix_scalars'] = {k:v for k,v in s.get('summary', {}).items()
                               if isinstance(v, (str, int, float, bool))}
    result['seam_scalars'] = {k:v for k,v in s.get('tail_seam', {}).items()
                             if isinstance(v, (str, int, float, bool))}
    responses = []
    for file in sorted(p.glob('seed_tail_*.json.gz')):
        data = json.load(gzip.open(file, 'rt'))
        r = data['response']
        row = dict(path=file.name, sha256=sha(file),
                   converged=r.get('converged'), residual=r.get('residual'),
                   failed=r.get('failed'), last_iteration=r.get('lastIteration'))
        if r.get('history'):
            row['last_history'] = r['history'][-1]
        if r.get('audit'):
            row['audit'] = r['audit']
        row['source_sha256'] = data.get('source_sha256')
        responses.append(row)
    result['tail_responses'] = responses
    for name in ['continuation-command.json', 'command.json', 'seed-secant-record.json']:
        file = p / name
        if file.exists():
            obj = json.loads(file.read_text())
            if name == 'seed-secant-record.json':
                obj = {k:obj[k] for k in ['source_hashes', 'secant', 'wrapper_returned', 'seconds'] if k in obj}
            result[name] = obj
    result['output_hashes'] = {f.name:sha(f) for f in sorted(p.iterdir())
                               if f.is_file() and f.suffix in ['.gz','.json','.jsonl','.log']}
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('runs', nargs='+', type=Path)
    a = p.parse_args()
    a.out.write_text(json.dumps(dict(scope=__doc__, runs=[summarize(x) for x in a.runs]), indent=2) + '\n')


if __name__ == '__main__':
    main()
