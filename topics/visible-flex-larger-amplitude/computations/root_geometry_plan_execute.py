#!/usr/bin/env python3
"""Run unchanged complete geometry-plan commands serially and save each outcome.

This driver adds no equations, sampling, tail solve, acceptance criterion, or
live memory cap. It preserves each command's formal wait4 resource report and
stops before the next case if a pause file exists. A completed field is only a
finite warm geometry diagnostic, never an accepted nonlinear surface.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    temporary = path.with_suffix(path.suffix + '.temporary')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan', type=Path, required=True)
    ap.add_argument('--plan-sha256', required=True)
    ap.add_argument('--first', type=int, required=True)
    ap.add_argument('--last', type=int, required=True)
    ap.add_argument('--pause-file', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists() or sha(args.plan) != args.plan_sha256:
        raise ValueError('Require a fresh execution path and the exact saved plan')
    plan = json.loads(args.plan.read_text())
    if not 0 <= args.first <= args.last < len(plan['candidates']):
        raise ValueError('Invalid inclusive candidate range')
    env = os.environ.copy()
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[key] = '1'
    state = dict(scope=__doc__, source_sha256=sha(__file__),
                 plan=str(args.plan), plan_sha256=sha(args.plan),
                 first=args.first, last=args.last, completed=[],
                 started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                 finished=False, active=None, paused=False)
    write(args.out, state)
    for index in range(args.first, args.last + 1):
        if args.pause_file.exists():
            state.update(paused=True, next_index=index, active=None)
            write(args.out, state)
            print(json.dumps(dict(paused=True, next_index=index)), flush=True)
            return
        for path, digest in plan['source_and_input_sha256'].items():
            if sha(path) != digest:
                raise ValueError('Saved source or input changed: ' + path)
        row = plan['candidates'][index]
        prefix = Path(row['command'][row['command'].index('--out-prefix') + 1])
        existing = list(prefix.parent.glob(prefix.name + '*'))
        if existing:
            raise FileExistsError('Candidate already has outputs: ' + row['name'])
        state['active'] = dict(index=index, name=row['name'], command=row['command'])
        write(args.out, state)
        print(json.dumps(dict(start=index, name=row['name'])), flush=True)
        with Path(row['log']).open('xb') as log:
            result = subprocess.run(row['command'], stdout=log, stderr=subprocess.STDOUT,
                                    env=env, check=False)
        resource = json.loads(Path(row['resource']).read_text()) if Path(row['resource']).exists() else None
        outcome = dict(index=index, name=row['name'], driver_child_exitcode=result.returncode,
                       formal_resource=resource)
        if result.returncode != 0 or resource is None or resource.get('exitcode') != 0:
            state.update(active=None, failed=outcome)
            write(args.out, state)
            raise RuntimeError('Original command failed; its complete output is preserved')
        report = json.loads(Path(row['report']).read_text())
        field = json.loads(Path(row['field']).read_text())
        if (not report.get('finished') or not report.get('finite_domain_passed')
                or report.get('nonlinear_solution') or report.get('true_new_H_tail_evaluated')
                or report.get('worker_start_attempts') != 0 or not field.get('complete')
                or report['geometry_fields']['sha256'] != sha(row['field'])):
            raise ValueError('Completed diagnostic scope or field identity differs')
        for chunk in field['chunks']:
            path = Path(row['field']).with_name(chunk['file'])
            if path.stat().st_size != chunk['bytes'] or sha(path) != chunk['sha256']:
                raise ValueError('Complete field chunk mismatch')
        files = []
        for path in sorted(prefix.parent.glob(prefix.name + '*')):
            size = path.stat().st_size
            if size >= 5_000_000 or (size > 1_000_000 and path.suffix != '.gz'):
                raise ValueError('Completed primary file exceeds repository limits')
            files.append(dict(path=str(path), bytes=size, sha256=sha(path)))
        manifest = prefix.with_name(prefix.name + '-stable-files.json')
        values = report['geometry_fields']
        record = dict(scope='Complete finite warm geometry diagnostic, original command unchanged',
                      plan_sha256=sha(args.plan), candidate_index=index, candidate_name=row['name'],
                      formal_exitcode=resource['exitcode'], wall_seconds=resource['wall_seconds'],
                      peak_rss_kib=resource['peak_rss_kib'], files=files,
                      kappa_abs_max_sample=values['kappa_abs_max_sample'],
                      twice_radius_max_sample=values['twice_radius_max_sample'],
                      new_nonlinear_solution=False, actual_reach_certified=False)
        write(manifest, record)
        outcome.update(manifest=str(manifest), manifest_sha256=sha(manifest),
                       kappa_abs_max_sample=record['kappa_abs_max_sample'],
                       twice_radius_max_sample=record['twice_radius_max_sample'])
        state['completed'].append(outcome)
        state['active'] = None
        write(args.out, state)
        print(json.dumps(dict(completed=index, name=row['name'],
                              peak_rss_kib=resource['peak_rss_kib'],
                              kappa=record['kappa_abs_max_sample'])), flush=True)
    state['finished'] = True
    write(args.out, state)


if __name__ == '__main__':
    main()
