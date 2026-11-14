#!/usr/bin/env python3
"""Evict only verified, recoverable historical native128 export worktree copies.

No numerical process is started or changed.  No Git object or ref is removed.
Every selected byte stream must match both the current source tree and the
actually published tree, with its local blob decoded before any mutation.
"""
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/visible-flexible-closed-surface'
NOTES = TOPIC / 'notes'
BARE = ROOT.parent / 'math-publication-minimal'
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
                           '-c', 'remote.origin.promisor=false',
                           '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0',
                           '-C', str(repo), *args], input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if proc.returncode:
        raise RuntimeError('Offline Git operation failed: '+args[0])
    return proc.stdout


def tree(repo, revision, paths):
    result = {}
    for row in git(repo, 'ls-tree', '-rz', '--full-tree', revision, '--', *paths).split(b'\0'):
        if not row:
            continue
        meta, path = row.split(b'\t', 1)
        mode, kind, oid = meta.decode().split()
        assert kind == 'blob' and mode == '100644'
        result[path.decode()] = (mode, oid)
    return result


def main():
    assert git(ROOT, 'rev-parse', 'HEAD').decode().strip() == HEAD
    pattern = 'topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-inc-flat17-m8-native128-n8-s128-q512-raw*.f64.gz'
    paths = sorted(x.decode() for x in git(ROOT, 'ls-files', '-z', '--', pattern).split(b'\0') if x)
    assert len(paths) == len(set(paths)) == 24
    assert all('flat17-m8-native128-' in p and p.endswith('.f64.gz') for p in paths)

    protected, launch_files = set(), []
    for name, key in [
        ('root-spectral-true-m14q512-02-guard-launch.json', 'bound_files'),
        ('root-linear-dn-pilot-v2-01-guard-launch.json', 'bound_files'),
        ('root-spectral-true-m14q512-release-lu-01-guard-launch.json', 'bound_files'),
    ]:
        path = NOTES / (PREFIX+name)
        launch_files.append(identity(path))
        definition = json.loads(path.read_text())
        for row in definition[key]:
            actual = identity(row['path'])
            assert actual['sha256'] == row['sha256'] and actual['bytes'] == row['bytes']
            protected.add(actual['path'])
    assert not any(str(ROOT/p) in protected for p in paths)

    current = tree(ROOT, HEAD, paths)
    published = tree(BARE, PUBLISHED, paths)
    index = {}
    for row in git(ROOT, 'ls-files', '--stage', '-z', '--', *paths).split(b'\0'):
        if not row:
            continue
        meta, path = row.split(b'\t', 1)
        mode, oid, stage = meta.decode().split()
        assert stage == '0'
        index[path.decode()] = (mode, oid)
    assert current == published == index and len(index) == len(paths)
    assert not git(ROOT, 'status', '--porcelain=v1', '-z', '--', *paths)

    rows, snapshots = [], {}
    for relative in paths:
        path = ROOT / relative
        assert path.is_file() and not path.is_symlink() and path.stat().st_nlink == 1
        before = path.stat()
        data = path.read_bytes()
        oid = current[relative][1]
        local_blob = git(ROOT, 'cat-file', 'blob', oid)
        assert local_blob == data
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == oid
        decoded = gzip.decompress(data)
        snapshots[relative] = (before.st_ino, before.st_mtime_ns, before.st_size)
        rows.append({'path': relative, 'mode': current[relative][0], 'git_blob': oid,
                     'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                     'decoded_bytes': len(decoded),
                     'decoded_sha256': hashlib.sha256(decoded).hexdigest()})

    sparse_path = Path(git(ROOT, 'rev-parse', '--git-path', 'info/sparse-checkout').decode().strip())
    if not sparse_path.is_absolute():
        sparse_path = ROOT / sparse_path
    old_rules = sparse_path.read_bytes()
    assert old_rules.endswith(b'\n') and old_rules.startswith(b'/*\n!/*/\n/topics/\n')
    new_rules = old_rules
    for path in paths:
        rule = ('!/'+path+'\n').encode()
        assert rule not in old_rules
        new_rules += rule
    out = NOTES / (PREFIX+'root-flat17-native128-recoverable-worktree-observed.json')
    assert not out.exists()
    record = {
        'status': 'ALL_LOCAL_RECOVERY_GATES_PASSED_BEFORE_MUTATION',
        'observer': '/root', 'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'script': identity(__file__), 'current_source_head': HEAD,
        'actually_published_anchor': PUBLISHED,
        'published_anchor_repository': str(BARE),
        'protected_launch_files': launch_files,
        'protected_unique_sources_rehashed': len(protected),
        'files': rows, 'file_count': len(rows),
        'total_historical_worktree_bytes': sum(row['bytes'] for row in rows),
        'old_sparse_rules': old_rules.decode(),
        'new_sparse_rules_sha256': hashlib.sha256(new_rules).hexdigest(),
        'free_bytes_before': shutil.disk_usage(ROOT).free,
        'removed_worktree_paths': [],
        'network_calls': 0, 'Git_objects_or_refs_removed': False,
        'solver_calls': 0,
        'restore': 'All blobs remain local and in the published tree. Restore selected paths from the recorded source head with git restore --worktree --ignore-skip-worktree-bits after adjusting their recorded sparse exclusions.',
        'scope': 'Historical native128 export residency only. All active inputs and the current R21 M12 geometry remain resident.',
    }

    def save():
        temp = out.with_name(out.name+'.tmp')
        temp.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
        os.replace(temp, out)

    save()
    git(ROOT, 'sparse-checkout', 'set', '--no-cone', '--stdin', data=new_rules)
    git(ROOT, 'update-index', '--skip-worktree', '-z', '--stdin',
        data=b''.join(p.encode()+b'\0' for p in paths))
    for row in rows:
        path = ROOT / row['path']
        if path.exists():
            stat = path.stat()
            assert (stat.st_ino, stat.st_mtime_ns, stat.st_size) == snapshots[row['path']]
            assert identity(path)['sha256'] == row['sha256']
            path.unlink()
        record['removed_worktree_paths'].append(row['path'])
    assert not any((ROOT/p).exists() for p in paths)
    assert not git(ROOT, 'status', '--porcelain=v1', '-z', '--', *paths)
    assert git(ROOT, 'rev-parse', 'HEAD').decode().strip() == HEAD
    for item in launch_files:
        assert identity(item['path']) == item
    record.update(status='RECOVERABLE_OLD_NATIVE128_EXPORT_COPIES_EVICTED',
                  free_bytes_after=shutil.disk_usage(ROOT).free,
                  current_and_published_blobs_preserved=True,
                  selected_paths_git_status_clean=True)
    save()
    print(json.dumps({'status': record['status'], 'file_count': len(rows),
                      'historical_bytes': record['total_historical_worktree_bytes'],
                      'protected_sources': len(protected),
                      'free_bytes_before': record['free_bytes_before'],
                      'free_bytes_after': record['free_bytes_after'],
                      'observation': identity(out)}))


if __name__ == '__main__':
    main()
