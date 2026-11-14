#!/usr/bin/env python3
"""Run the actual missing p41 work on this public repository's Actions.

The mathematical engines and their exact original inputs are unchanged.
Published complete computations are consumed, never silently recomputed.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys

from p41_public_actions_recovery import REPO, S, TOPIC, publish, read, save, sha

REQUEST = TOPIC / 'notes/public-p41-remaining-recovery-request.json'
DRIVERS = {
    'ramified': 'p41_ci_recover_ramified_ss47.py',
    'shifted_j44': 'p41_ci_recover_shifted_j44_ss47.py',
    'moved_j9': 'p41_recover_R470_moved_j9_ss47.py',
    'cm4_prefix': 'p41_ci_continue_true_CM4_chains47.py',
}


def command_for(item, work, out, budget):
    command = [sys.executable, '-u', str(S / DRIVERS[item['kind']]),
               '--result-id', item['result'], '--output', str(out),
               '--budget-minutes', str(budget)]
    if item['kind'] != 'cm4_prefix':
        command += ['--disk-id', item['disk_id']]
    if item['kind'] == 'moved_j9':
        command += ['--script-dir', str(S), '--work-dir', str(work)]
    return command


def prior_completion(item):
    base = TOPIC / 'computations' / item['result']
    for receipt in sorted(base.glob('*/run-receipt.json')):
        value = read(receipt)
        if value.get('complete'):
            return str(receipt.parent.relative_to(REPO))
    return None


def prepare(item, work, out, budget):
    work.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    assert item['kind'] in DRIVERS
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    command = command_for(item, work, out, budget)
    save(out / 'public-actions-input.json', {
        'result': item['result'], 'request_item': item,
        'source_commit': source, 'source_repository': 'Rogerhu12/math-research-public',
        'request_sha256': sha(REQUEST), 'wrapper_sha256': sha(__file__),
        'mathematical_driver_sha256': sha(S / DRIVERS[item['kind']]),
        'root_readme_sha256': sha(REPO / 'README.md'),
        'topic_readme_sha256': sha(TOPIC / 'README.md'),
        'command': command, 'budget_minutes': budget,
        'prior_completed_repository_path': prior_completion(item),
        'run_url': 'https://github.com/Rogerhu12/math-research-public/actions/runs/' +
                   os.environ.get('GITHUB_RUN_ID', 'local-prepare'),
        'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'mathematical_completion_claimed': False,
    })


def run(item, work, out, budget):
    initial = read(out / 'public-actions-input.json')
    if initial['prior_completed_repository_path']:
        save(out / 'run-receipt.json', {
            'result': item['result'], 'complete': True,
            'reused_complete_repository_path': initial['prior_completed_repository_path'],
            'mathematics_repeated': False,
        })
        return 0
    command = command_for(item, work, out, budget)
    assert command == initial['command']
    with (out / 'public-actions-run.log').open('w') as log:
        process = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
    receipt_path = out / 'run-receipt.json'
    receipt = read(receipt_path) if receipt_path.exists() else {
        'result': item['result'], 'complete': False,
        'error': 'Mathematical driver stopped before writing its receipt.',
    }
    receipt.update(execution_environment='public-repository-github-actions',
        source_commit=initial['source_commit'],
        workflow_run_id=os.environ.get('GITHUB_RUN_ID'),
        workflow_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        process_exit_code=process.returncode,
        finished_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    if process.returncode:
        receipt['complete'] = False
    save(receipt_path, receipt)
    print(json.dumps({'result': item['result'], 'complete': receipt['complete'],
                      'process_exit_code': process.returncode}), flush=True)
    return process.returncode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['matrix', 'prepare', 'run', 'publish', 'verify'])
    parser.add_argument('--result')
    parser.add_argument('--budget-minutes', type=int, default=320)
    args = parser.parse_args()
    jobs = read(REQUEST)['jobs']
    if args.mode == 'matrix':
        pending = [item['result'] for item in jobs if prior_completion(item) is None]
        print(json.dumps({'result': pending}, separators=(',', ':')))
        return 0
    item = next(item for item in jobs if item['result'] == args.result)
    base = Path(os.environ['RUNNER_TEMP']) / 'serre-p41-remaining' / args.result
    work, out = base / 'work', base / 'output'
    if args.mode == 'prepare':
        prepare(item, work, out, args.budget_minutes)
        return 0
    if args.mode == 'run':
        return run(item, work, out, args.budget_minutes)
    if args.mode == 'publish':
        initial = read(out / 'public-actions-input.json')
        if initial['prior_completed_repository_path']:
            save(out / 'publication-receipt.json', {
                'published': True, 'mathematics_repeated': False,
                'repository_path': initial['prior_completed_repository_path'],
            })
            return 0
        return publish(item, out, artifact_prefix='serre-p41-remaining',
                       omit_derived_based_points=True)
    return 0 if read(out / 'run-receipt.json')['complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
