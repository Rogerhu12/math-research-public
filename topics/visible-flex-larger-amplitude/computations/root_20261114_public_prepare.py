#!/usr/bin/env python3
"""Restore the pinned 91-file subset from this public repository by content.

Migration preserved files, not private history. Prefer the current public
tree when its bytes equal the recorded manifest. Only a missing or changed
source needs the original private revision, using an ephemeral MR_TOKEN.
No credentials or authentication headers are written to files.
"""
from __future__ import annotations
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

TOPIC_NAME = 'visible-flex-larger-amplitude'


def make_runtime_topic(repo, work):
    """Link only already checked-out public topic inputs into scratch."""
    topic = Path(repo) / 'topics' / TOPIC_NAME
    runtime = Path(work) / 'runtime/topics' / TOPIC_NAME
    runtime.mkdir(parents=True, exist_ok=True)
    computations = runtime / 'computations'
    if not computations.exists():
        computations.symlink_to(topic / 'computations', target_is_directory=True)
    notes = runtime / 'notes'
    notes.mkdir(exist_ok=True)
    for original in (topic / 'notes').iterdir():
        target = notes / original.name
        if not target.exists() and not target.is_symlink():
            target.symlink_to(original, target_is_directory=original.is_dir())
    return runtime


def git_environment(token=None, private_source=False):
    env = os.environ.copy()
    settings = [('remote.origin.promisor', 'true'),
                ('remote.origin.partialclonefilter', 'blob:none')]
    if private_source:
        settings += [('remote.private-pinned-source.url', 'https://github.com/Rogerhu12/math-research.git'),
                     ('remote.private-pinned-source.promisor', 'true'),
                     ('remote.private-pinned-source.partialclonefilter', 'blob:none')]
    if token:
        settings += [('http.https://github.com/.extraheader', ''),
                     ('http.https://github.com/.extraheader', 'AUTHORIZATION: basic '+
                      base64.b64encode(('x-access-token:'+token).encode()).decode())]
    count = int(env.get('GIT_CONFIG_COUNT', '0'))
    for key, value in settings:
        env['GIT_CONFIG_KEY_'+str(count)] = key
        env['GIT_CONFIG_VALUE_'+str(count)] = value
        count += 1
    env['GIT_CONFIG_COUNT'] = str(count)
    env['GIT_TERMINAL_PROMPT'] = '0'
    return env


def prepare(repo, work, report, restore_a_raw=False):
    started = time.monotonic()
    repo, work, report = (Path(x).resolve() for x in (repo, work, report))
    topic = repo/'topics'/TOPIC_NAME
    manifest = topic/'computations/source-dependencies.json'
    rec = json.loads(manifest.read_text())
    revision = rec['source_revision']
    source_root = work/'source'
    work.mkdir(parents=True, exist_ok=True)
    report.parent.mkdir(parents=True, exist_ok=True)
    public_env = git_environment(os.environ.get('GH_TOKEN'))
    private_env = None
    private_fetched = False
    restored = []
    for entry in rec['files']:
        rel = Path(entry['path'])
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError('Invalid pinned source path')
        target = source_root/rel
        data = target.read_bytes() if target.exists() else b''
        where = 'existing-verified-bytes'
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            current = subprocess.run(['git', '-C', str(repo), 'show', 'HEAD:'+entry['path']],
                                     env=public_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            data = current.stdout
            where = 'current-public-tree'
            if current.returncode or hashlib.sha256(data).hexdigest() != entry['sha256']:
                if not private_fetched:
                    token = os.environ.get('MR_TOKEN') or os.environ.get('GH_TOKEN')
                    if not token:
                        raise RuntimeError('Pinned source absent from public tree; MR_TOKEN is needed for '+entry['path'])
                    private_env = git_environment(token, private_source=True)
                    subprocess.run(['git', '-C', str(repo), 'fetch', '--filter=blob:none', '--depth=1',
                                    '--no-tags', 'private-pinned-source', revision],
                                   env=private_env, check=True)
                    private_fetched = True
                data = subprocess.check_output(['git', '-C', str(repo), 'show', revision+':'+entry['path']],
                                               env=private_env)
                where = 'original-private-revision'
            if hashlib.sha256(data).hexdigest() != entry['sha256']:
                raise ValueError('Pinned source hash mismatch: '+entry['path'])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        restored.append(dict(path=entry['path'], sha256=entry['sha256'], origin=where))
    source_topic = source_root/'topics/visible-flexible-closed-surface'
    origin = dict(source_revision=revision, files=len(rec['files']), bytes=rec['total_bytes'],
                  manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest())
    (source_topic/'source-origin.json').write_text(json.dumps(origin, indent=2)+'\n')
    runtime_topic = make_runtime_topic(repo, work)
    notes = runtime_topic / 'notes'
    recovery_report = None
    if restore_a_raw:
        recovery_report = report.with_name(report.stem+'-A-raw.json')
        subprocess.run([sys.executable, str(topic/'computations/strong_gzip_chunk_recovery.py'),
                        '--recipe', str(topic/'notes/2026-11-13-strong-q126-m32-tail2-actual-r1-exact-raw-gzip-recovery.json'),
                        '--archive-topic', str(topic), '--output-directory', str(notes),
                        '--report', str(recovery_report)], check=True)
        if not json.loads(recovery_report.read_text())['all_original_target_bytes_reconstructed_and_read_back']:
            raise RuntimeError('Incomplete accepted A raw recovery')
    result = dict(scope=__doc__, source_revision=revision,
                  source_manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),
                  source_topic=str(source_topic), runtime_topic=str(runtime_topic),
                  source_origin=origin, restored_files=restored,
                  fetched_private_revision=private_fetched, restored_a_raw=restore_a_raw,
                  raw_recovery_report=str(recovery_report) if recovery_report else None,
                  seconds=time.monotonic()-started,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    report.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='public-source-prepared', files=len(restored),
                          fetched_private_revision=private_fetched, restored_a_raw=restore_a_raw)), flush=True)
    return result


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[3])
    p.add_argument('--work', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--restore-a-raw', action='store_true')
    a = p.parse_args()
    prepare(a.repo, a.work, a.report, a.restore_a_raw)
