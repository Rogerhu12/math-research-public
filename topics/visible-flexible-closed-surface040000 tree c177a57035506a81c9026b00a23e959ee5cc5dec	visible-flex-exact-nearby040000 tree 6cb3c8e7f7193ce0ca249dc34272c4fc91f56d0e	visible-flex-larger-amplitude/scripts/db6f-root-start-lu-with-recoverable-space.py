#!/usr/bin/env python3
"""Recheck recoverable copies and start the bound LU run in one process.

Historical copies can reappear between tool calls; their cause is not inferred.
Only unchanged local published blobs may be evicted.  The 768 MiB start gate,
512 MiB pause gate, all mathematical arguments and bound sources stay intact.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/visible-flexible-closed-surface'
NOTES = TOPIC / 'notes'
SCRIPTS = TOPIC / 'scripts'
PREFIX = '2026-11-09-db6f-'
HEAD = 'e6ee007fa3ecd0cee753a962c4bb7910e85a95cf'
PUBLISHED = 'b77800583068ef38332c690f03a629784373ff82'


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def git(repo, *args, data=None):
    env = dict(os.environ, GIT_NO_LAZY_FETCH='1', GIT_OPTIONAL_LOCKS='0')
    assert 'GIT_INDEX_FILE' not in env
    proc = subprocess.run(['/usr/bin/git', '-c', 'protocol.allow=never',
                           '-c', 'remote.origin.promisor=false', '-c', 'gc.auto=0',
                           '-C', str(repo), *args], input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if proc.returncode:
        raise RuntimeError('Offline Git failure in '+args[0])
    return proc.stdout


def entries(repo, revision, paths):
    found = {}
    for row in git(repo, 'ls-tree', '-rz', '--full-tree', revision, '--', *paths).split(b'\0'):
        if not row:
            continue
        meta, name = row.split(b'\t', 1)
        mode, kind, oid = meta.decode().split()
        assert kind == 'blob'
        found[name.decode()] = (mode, oid)
    return found


def main():
    assert git(ROOT, 'rev-parse', 'HEAD').decode().strip() == HEAD
    launch = NOTES / (PREFIX+'root-spectral-true-m14q512-release-lu-01-guard-launch.json')
    wrapper = SCRIPTS / 'db6f-root-true-m14-release-lu-resource-limited-6g.py'
    assert identity(launch)['sha256'] == '16a99e7b5d2b5e9ca8e064e459285bd79d2423b12faed95163f3272897cd5384'
    assert identity(wrapper)['sha256'] == 'c2f5a48a1a79c49ec37259653ee3ada00a368b8f038b6fa42ec55b73afe9e1d9'
    definition = json.loads(launch.read_text())
    protected = set()
    for row in definition['bound_files']:
        assert identity(row['path']) == row
        protected.add(row['path'])
    numeric_out = Path(definition['out_prefix'])
    assert not Path(str(numeric_out)+'-reproduction.json').exists()

    rows, reports = [], []
    for suffix, expected in [
        ('root-q02-history-recoverable-worktree-observed.json', '0c4c4bdaad4d8f5ac0db7c1045d4a8e449a61727e4500b92ce6d8474b633204c'),
        ('root-q02s64-history-recoverable-worktree-observed.json', '4674a0acc2c18cb09a4dceb34d354990bd55c552eea83266864e289532eb0d02'),
        ('root-flat17-native128-recoverable-worktree-observed.json', '79e7abd577cdc1bece13351126f1fb89cba4ef7e08796ba51c96547fa198984a'),
    ]:
        path = NOTES / (PREFIX+suffix)
        item = identity(path)
        assert item['sha256'] == expected
        reports.append(item)
        report = json.loads(path.read_text())
        assert report['current_source_head'] == HEAD and report['actually_published_anchor'] == PUBLISHED
        rows.extend(report['files'])
    paths = [row['path'] for row in rows]
    assert len(paths) == len(set(paths)) == 66
    assert all(str(ROOT/p) not in protected for p in paths)
    current = entries(ROOT, HEAD, paths)
    published = entries(ROOT.parent/'math-publication-minimal', PUBLISHED, paths)
    assert current == published
    present = []
    for row in rows:
        assert current[row['path']] == (row['mode'], row['git_blob'])
        path = ROOT / row['path']
        if not path.exists():
            continue
        assert path.is_file() and not path.is_symlink() and path.stat().st_nlink == 1
        item = identity(path)
        assert item['bytes'] == row['bytes'] and item['sha256'] == row['sha256']
        blob = git(ROOT, 'cat-file', 'blob', row['git_blob'])
        assert len(blob) == row['bytes'] and hashlib.sha256(blob).hexdigest() == row['sha256']
        stat = path.stat()
        present.append((row, (stat.st_ino, stat.st_mtime_ns, stat.st_size)))

    out = NOTES / (PREFIX+'root-lu-same-process-recovery-and-start.json')
    assert not out.exists()
    observation = {
        'status': 'RECOVERY_VERIFIED_BEFORE_SAME_PROCESS_START',
        'observer': '/root', 'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'launcher': identity(__file__), 'guard_launch': identity(launch),
        'resource_wrapper': identity(wrapper), 'previous_recovery_reports': reports,
        'previous_start_preflight_actual_receipt': '3b7c93',
        'previous_start_preflight_actual_exit_code': 1,
        'previous_preflight_reason': 'Start-space threshold failed before executing wrapper or solver.',
        'protected_source_count': len(protected), 'source_head': HEAD,
        'published_anchor': PUBLISHED, 'historical_paths_currently_present': len(present),
        'free_bytes_before': shutil.disk_usage(ROOT).free,
        'removed_paths': [], 'git_objects_or_refs_removed': False,
        'cause_of_reappearing_copies_not_inferred': True,
        'actual_solver_start_not_yet_observed_by_root': True,
    }

    def save():
        tmp = out.with_name(out.name+'.tmp')
        tmp.write_text(json.dumps(observation, ensure_ascii=False, indent=2)+'\n')
        os.replace(tmp, out)

    save()
    git(ROOT, 'update-index', '--skip-worktree', '-z', '--stdin',
        data=b''.join(p.encode()+b'\0' for p in paths))
    for row, old_stat in present:
        path = ROOT / row['path']
        stat = path.stat()
        assert (stat.st_ino, stat.st_mtime_ns, stat.st_size) == old_stat
        assert identity(path)['sha256'] == row['sha256']
        path.unlink()
        observation['removed_paths'].append(row['path'])
    for row in definition['bound_files']:
        assert identity(row['path']) == row
    free = shutil.disk_usage(ROOT).free
    observation.update(free_bytes_after=free,
                       status='RECOVERY_DONE_HANDING_OFF_TO_ORIGINAL_SPACE_GUARD')
    save()
    assert free >= 768*1024**2, 'Unchanged original start-space threshold is not met'
    print(json.dumps({'event': observation['status'], 'rechecked_bound_sources': len(protected),
                      'reappeared_copies_removed': len(present), 'free_bytes_after': free,
                      'preflight_record': identity(out)}), flush=True)
    argv = [sys.executable, str(wrapper), '--launch', str(launch),
            '--observation', str(NOTES/(PREFIX+'root-spectral-true-m14q512-release-lu-01-guard-completion.json')),
            '--backup-observation', '/tmp/db6f-spectral-true-m14q512-release-lu-01-guard-backup.json']
    os.execv(sys.executable, argv)


if __name__ == '__main__':
    main()
