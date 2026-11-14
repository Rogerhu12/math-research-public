#!/usr/bin/env python3
"""Publish an explicit closed payload using terminal Git on the CI runner.

Only this topic and this one publication workflow are owned. The existing
publisher preserves every other tree entry, leaves root LOG untouched, reads
both README differences immediately after every pull, and never force pushes.
No mathematical computation or completion decision is delegated to this job.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

TOPIC = 'topics/visible-flexible-closed-surface/'
WORKFLOW = '.github/workflows/visible-flex-fd2d-publish-checkpoint.yml'
REQUEST = TOPIC + 'notes/2026-11-12-fd2d-ci-publication-request.json'
HELPER = TOPIC + 'scripts/fd2d_publish_rebase_checkpoint.py'


def run(args, data=None):
    result = subprocess.run(args, input=data, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--payload', required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.payload):
        raise ValueError('Expected an exact payload commit')
    args.scratch.mkdir(parents=True, exist_ok=True)
    request = json.loads(run(['git', 'show', args.payload + ':' + REQUEST]))
    paths = request['owned_paths']
    if len(paths) != len(set(paths)):
        raise ValueError('Duplicate owned paths')
    for path in paths:
        p = PurePosixPath(path)
        if p.is_absolute() or '..' in p.parts:
            raise ValueError('Invalid owned path')
        if not (path.startswith(TOPIC) or path == WORKFLOW):
            raise ValueError('Path outside this closed payload')
    required = {TOPIC + 'HANDOFF.md', REQUEST, HELPER, WORKFLOW}
    if not required.issubset(paths):
        raise ValueError('Incomplete publication payload')
    entries = []
    for row in run(['git', 'ls-tree', '-r', '-z', args.payload, '--', *paths]).split('\0'):
        if row:
            bits, path = row.split('\t', 1)
            mode, kind, sha = bits.split()
            if kind != 'blob' or mode != '100644':
                raise ValueError('Only regular payload files are supported')
            entries.append([mode, sha, path])
    if {entry[2] for entry in entries} != set(paths):
        raise ValueError('Payload is missing a requested file')
    handoff = run(['git', 'show', args.payload + ':' + TOPIC + 'HANDOFF.md'])
    rules = re.search(r'`([0-9a-f]{40})`', handoff.split('## 2.', 1)[1].split('## 3.', 1)[0]).group(1)
    base = request['base_commit']
    if not re.fullmatch(r'[0-9a-f]{40}', base):
        raise ValueError('Expected an exact common base')
    helper = args.scratch / 'publisher.py'
    helper.write_text(run(['git', 'show', args.payload + ':' + HELPER]))
    snapshot = args.scratch / 'snapshot.json'
    snapshot.write_text(json.dumps({
        'message': request['message'], 'entries': entries,
        'handoff': handoff, 'base_commit': base,
    }, ensure_ascii=False, indent=2) + '\n')
    # The single-branch clone initially tracks the checkpoint. Main must be
    # explicitly tracked before pull so origin/main always means fresh main.
    run(['git', 'config', '--replace-all', 'remote.origin.fetch', '+refs/heads/main:refs/remotes/origin/main'])
    run(['git', 'config', 'fetch.negotiationAlgorithm', 'skipping'])
    run(['git', 'fetch', '--filter=blob:none', '--depth=64', 'origin',
         'main:refs/remotes/origin/main', base, rules])
    run(['git', 'sparse-checkout', 'init', '--no-cone'])
    run(['git', 'sparse-checkout', 'set', '--no-cone', '--stdin'],
        ''.join('/'+path+'\n' for path in sorted(set(paths) | {'README.md', TOPIC+'README.md'})))
    run(['git', 'checkout', '-b', 'fd2d-ci-publisher', '--track', 'origin/main'])
    receipt = args.scratch / 'main-published.json'
    attempts = args.scratch / 'pull-and-push-history.jsonl'
    result = subprocess.run([sys.executable, str(helper), '--snapshot', str(snapshot),
                             '--receipt', str(receipt), '--attempt-log', str(attempts)])
    if receipt.exists():
        print(receipt.read_text(), flush=True)
    return result.returncode


if __name__ == '__main__':
    sys.exit(main())
