#!/usr/bin/env python3
"""Losslessly archive frozen native binaries after an observed worker exit.

This is reversible scratch-space management, not numerical processing. Every
archive is decompressed and SHA-256 checked before its original is unlinked;
the original is read again to detect a concurrent change. Small JSON, source,
configuration and checkpoint files are never selected. Restore reproduces the
original path, exact bytes, permissions and modification time, retaining the
archive. No archive or numeric array is a repository artifact.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import time

CHUNK = 2**20


def digest_stream(stream):
    digest, size = hashlib.sha256(), 0
    while True:
        block = stream.read(CHUNK)
        if not block:
            return digest.hexdigest(), size
        digest.update(block)
        size += len(block)


def digest_file(path):
    with Path(path).open('rb') as stream:
        return digest_stream(stream)


def save(path, value):
    temporary = path.with_name(path.name + '.tmp')
    with temporary.open('w') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def original_path(root, relative):
    path = root / relative
    if path.is_symlink() or root not in path.resolve().parents:
        raise ValueError('Only ordinary files inside the frozen root are allowed')
    return path


def archive(args):
    root, terminal, journal = (p.resolve() for p in
                              (args.root, args.worker_exit, args.journal))
    if root.name != 'native-runs' or terminal.parent != root.parent:
        raise ValueError('The exit record must belong to this native directory')
    if digest_file(terminal)[0] != args.worker_exit_sha256:
        raise ValueError('The actual terminal record changed')
    events = json.loads(terminal.read_text())['events']
    if (not events or not isinstance(events[-1].get('returncode'), int)
            or time.time() - events[-1]['unix_time'] < 120):
        raise ValueError('An actual terminal older than two minutes is required')
    if journal.exists():
        raise FileExistsError('Use the existing journal for restore; never overwrite it')
    files = sorted(p for p in root.rglob('*.bin')
                   if p.stat().st_size >= args.minimum_bytes)
    result = dict(status='lossless_archival_running', source_root=str(root),
        worker_exit=dict(path=str(terminal), sha256=args.worker_exit_sha256),
        source_sha256=digest_file(__file__)[0], complete_source_bytes_preserved=True,
        current_mathematical_inputs_archived=False,
        current_pipeline_dependencies_confirmed_external_to_this_root=True,
        minimum_bytes=args.minimum_bytes, rows=[], started_unix_time=time.time(),
        scratch_free_before=shutil.disk_usage(root).free)
    save(journal, result)
    for p in files:
        p = original_path(root, p.relative_to(root))
        before = p.stat()
        if before.st_mtime > events[-1]['unix_time'] + 1:
            raise ValueError('A binary changed after the actual terminal: ' + str(p))
        compressed = p.with_name(p.name + '.lossless.gz')
        if compressed.exists():
            raise FileExistsError(compressed)
        initial_hash, size = digest_file(p)
        with compressed.open('xb') as raw:
            with gzip.GzipFile(filename='', fileobj=raw, mode='wb',
                               compresslevel=6, mtime=0) as output:
                with p.open('rb') as source:
                    shutil.copyfileobj(source, output, CHUNK)
            raw.flush()
            os.fsync(raw.fileno())
        with gzip.open(compressed, 'rb') as source:
            restored_hash, restored_size = digest_stream(source)
        after = p.stat()
        if ((restored_hash, restored_size) != (initial_hash, size)
                or digest_file(p) != (initial_hash, size)
                or (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns)
                != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)):
            raise IOError('The original/archive identity was not established; original retained')
        row = dict(relative_path=str(p.relative_to(root)), original_sha256=initial_hash,
            original_bytes=size, original_allocated_bytes=before.st_blocks*512,
            original_mode=stat.S_IMODE(before.st_mode), original_mtime_ns=before.st_mtime_ns,
            archive_relative_path=str(compressed.relative_to(root)),
            archive_sha256=digest_file(compressed)[0], archive_bytes=compressed.stat().st_size,
            archive_allocated_bytes=compressed.stat().st_blocks*512,
            decompressed_complete_bytes_verified=True, original_rehashed_before_unlink=True,
            original_unlinked=False)
        result['rows'].append(row)
        # The durable journal identifies the archive before any original removal.
        save(journal, result)
        if row['archive_allocated_bytes'] < row['original_allocated_bytes']:
            p.unlink()
            row['original_unlinked'] = True
        else:
            compressed.unlink()
            row['archive_removed_because_no_space_saved'] = True
        save(journal, result)
        if len(result['rows']) % 8 == 0:
            print(json.dumps(dict(completed=len(result['rows']), total=len(files),
                scratch_free_bytes=shutil.disk_usage(root).free)), flush=True)
    result.update(status='complete_frozen_native_lossless_archival',
        finished_unix_time=time.time(), scratch_free_after=shutil.disk_usage(root).free,
        total_original_bytes=sum(r['original_bytes'] for r in result['rows']),
        total_archived_bytes=sum(r['archive_bytes'] for r in result['rows'] if r['original_unlinked']),
        allocated_bytes_saved=sum(r['original_allocated_bytes']-r['archive_allocated_bytes']
                                  for r in result['rows'] if r['original_unlinked']))
    save(journal, result)
    print(json.dumps({k:result[k] for k in ('status', 'total_original_bytes',
        'total_archived_bytes', 'allocated_bytes_saved', 'scratch_free_after')}), flush=True)


def restore(args):
    record = json.loads(args.journal.read_text())
    root = Path(record['source_root']).resolve()
    rows = {r['relative_path']:r for r in record['rows']}
    for relative in args.relative:
        row = rows[relative]
        p = original_path(root, relative)
        compressed = original_path(root, row['archive_relative_path'])
        expected = row['original_sha256'], row['original_bytes']
        if p.exists():
            if digest_file(p) != expected:
                raise ValueError('An existing original differs; never overwrite it')
            continue
        if digest_file(compressed)[0] != row['archive_sha256']:
            raise ValueError('The preserved archive changed')
        temporary = p.with_name(p.name + '.restoring')
        with temporary.open('xb') as output, gzip.open(compressed, 'rb') as source:
            shutil.copyfileobj(source, output, CHUNK)
            output.flush()
            os.fsync(output.fileno())
        if digest_file(temporary) != expected:
            raise IOError('Restored bytes differ; original path was not replaced')
        os.chmod(temporary, row['original_mode'])
        os.utime(temporary, ns=(row['original_mtime_ns'], row['original_mtime_ns']))
        temporary.replace(p)
        print(json.dumps(dict(restored=str(p), sha256=expected[0], bytes=expected[1])), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    a = sub.add_parser('archive')
    a.add_argument('--root', required=True, type=Path)
    a.add_argument('--worker-exit', required=True, type=Path)
    a.add_argument('--worker-exit-sha256', required=True)
    a.add_argument('--journal', required=True, type=Path)
    a.add_argument('--minimum-bytes', type=int, default=262144)
    r = sub.add_parser('restore')
    r.add_argument('--journal', required=True, type=Path)
    r.add_argument('relative', nargs='+')
    arguments = parser.parse_args()
    (archive if arguments.action == 'archive' else restore)(arguments)
