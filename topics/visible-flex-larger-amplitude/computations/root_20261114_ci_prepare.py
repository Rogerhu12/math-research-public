#!/usr/bin/env python3
"""Restore the pinned small source subset and, optionally, the accepted A raw.

Intended for root README rule 14 public-runner jobs. Numerical work belongs in
the caller's separate driver. Credentials remain solely in process memory;
neither a token nor an authentication header is written to the work tree.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
TOPIC_NAME = 'visible-flex-larger-amplitude'


def git_environment():
    env = os.environ.copy()
    settings = [('remote.origin.promisor', 'true'),
                ('remote.origin.partialclonefilter', 'blob:none')]
    token = env.get('GH_TOKEN')
    if token:
        # Empty the multi-valued extraheader first, including any checkout
        # helper value. Only these child Git processes see this override.
        settings += [('http.https://github.com/.extraheader', ''),
                     ('http.https://github.com/.extraheader', 'AUTHORIZATION: basic ' +
                      base64.b64encode(('x-access-token:' + token).encode()).decode())]
    count = int(env.get('GIT_CONFIG_COUNT', '0'))
    for key, value in settings:
        env['GIT_CONFIG_KEY_' + str(count)] = key
        env['GIT_CONFIG_VALUE_' + str(count)] = value
        count += 1
    env['GIT_CONFIG_COUNT'] = str(count)
    env['GIT_TERMINAL_PROMPT'] = '0'
    return env


def prepare(repo, work, report, restore_a_raw=False):
    started = time.time()
    repo, work, report = (Path(x).resolve() for x in (repo, work, report))
    topic = repo / 'topics' / TOPIC_NAME
    manifest = topic / 'computations/source-dependencies.json'
    source_record = json.loads(manifest.read_text())
    revision = source_record['source_revision']
    work.mkdir(parents=True, exist_ok=True)
    report.parent.mkdir(parents=True, exist_ok=True)
    env = git_environment()
    exists = subprocess.run(['git', '-C', str(repo), 'cat-file', '-e', revision + '^{commit}'],
                            env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if not exists:
        subprocess.run(['git', '-C', str(repo), 'fetch', '--filter=blob:none', '--depth=1',
                        '--no-tags', 'origin', revision], env=env, check=True)
    source_root = work / 'source'
    subprocess.run([sys.executable, str(topic / 'computations/prepare-source-dependencies.py'),
                    '--repo', str(repo), '--dest', str(source_root)], env=env, check=True)
    source_topic = source_root / 'topics/visible-flexible-closed-surface'
    runtime_topic = work / 'runtime/topics' / TOPIC_NAME
    runtime_topic.mkdir(parents=True, exist_ok=True)
    computations_link = runtime_topic / 'computations'
    if not computations_link.exists():
        computations_link.symlink_to(topic / 'computations', target_is_directory=True)
    notes = runtime_topic / 'notes'
    notes.mkdir(exist_ok=True)
    for original in (topic / 'notes').iterdir():
        target = notes / original.name
        if not target.exists() and not target.is_symlink():
            target.symlink_to(original, target_is_directory=original.is_dir())
    recovery_report = None
    if restore_a_raw:
        recovery_report = report.with_name(report.stem + '-A-raw.json')
        subprocess.run([sys.executable, str(topic / 'computations/strong_gzip_chunk_recovery.py'),
                        '--recipe', str(topic / 'notes/2026-11-13-strong-q126-m32-tail2-actual-r1-exact-raw-gzip-recovery.json'),
                        '--archive-topic', str(topic), '--output-directory', str(notes),
                        '--report', str(recovery_report)], check=True)
        recovered = json.loads(recovery_report.read_text())
        if not recovered['all_original_target_bytes_reconstructed_and_read_back']:
            raise RuntimeError('Incomplete accepted A recovery')
    result = dict(scope=__doc__, source_revision=revision,
                  source_topic=str(source_topic), runtime_topic=str(runtime_topic),
                  source_manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),
                  source_origin=json.loads((source_topic / 'source-origin.json').read_text()),
                  restored_a_raw=restore_a_raw,
                  raw_recovery_report=str(recovery_report) if recovery_report else None,
                  seconds=time.time()-started,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    report.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(event='prepared', source_topic=str(source_topic),
                          runtime_topic=str(runtime_topic), restored_a_raw=restore_a_raw)), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=HERE.parents[2])
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--restore-a-raw', action='store_true')
    args = parser.parse_args()
    prepare(args.repo, args.work, args.report, args.restore_a_raw)


if __name__ == '__main__':
    main()
