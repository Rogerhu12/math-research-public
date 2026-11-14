#!/usr/bin/env python3
"""Hard-link only identical old frozen successful-producer gzip copies.

AI-assisted maintenance, strong_recovery, 2026-11-13.
Parent authorization: old q096/q098/q106/q122 immutable duplicates only;
exclude A/q126 and the current nine-control data. Both paths and all bytes
remain. No scientific result, raw recovery, full-flow content, or source is
discarded. No Git command or recomputation is performed.
"""
from __future__ import annotations
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat

PREFIXES = ('2026-11-13-strong-q096', '2026-11-13-strong-q098',
            '2026-11-13-strong-q106', '2026-11-13-strong-q122')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def snapshot(path):
    value = path.stat()
    if not stat.S_ISREG(value.st_mode) or path.is_symlink():
        raise ValueError('Only ordinary files may be consolidated')
    return dict(device=value.st_dev, inode=value.st_ino, bytes=value.st_size,
                allocated_bytes=value.st_blocks*512, links=value.st_nlink,
                mode=stat.S_IMODE(value.st_mode), mtime_ns=value.st_mtime_ns)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('runtime-notes', 'archive-notes', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh maintenance report')
    runtime, archive = args.runtime_notes.resolve(), args.archive_notes.resolve()
    if runtime == archive:
        raise ValueError('The two immutable copies must initially be distinct')
    owned = []
    for path in runtime.glob('*-resource.json'):
        if not path.name.startswith(PREFIXES):
            continue
        data = path.read_bytes(); record = json.loads(data)
        if record.get('exitcode') == 0 and record.get('wait4_observed') is True and record.get('finished_utc'):
            owned.append((path.name.removesuffix('-resource.json'),
                          dict(file=str(path), sha256=digest(data),
                               finished_utc=record['finished_utc'])))
    owned.sort(key=lambda row: -len(row[0]))
    rows, skipped = [], []
    before_free = shutil.disk_usage(runtime).free
    report = dict(schema='immutable-successful-notes-hardlink-maintenance-v1', scope=__doc__,
        source_sha256=digest(Path(__file__).read_bytes()),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        allowed_name_prefixes=list(PREFIXES), excluded=['q126/A', 'current nine-control',
            'all source files', 'all non-gzip files', 'incomplete/unsuccessful producer files'],
        runtime_notes=str(runtime), archive_notes=str(archive),
        complete_successful_producer_records=len(owned), free_bytes_before=before_free,
        source_or_mathematics_changed=False, Git_commands_executed=0,
        recomputation_or_result_discarded=False, entries=rows, skipped=skipped,
        completed=False)
    def save():
        temporary=args.out.with_name(args.out.name+'.tmp')
        temporary.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
        temporary.replace(args.out)
    save()
    for source in sorted(runtime.iterdir()):
        if (not source.name.startswith(PREFIXES) or not source.name.endswith('.gz')
                or 'q126' in source.name or not source.is_file()):
            continue
        archive_file = archive/source.name
        if not archive_file.is_file():
            continue
        left, right = snapshot(source), snapshot(archive_file)
        if left['bytes'] < 1_000_000 or left['links'] != 1 or left['inode'] == right['inode']:
            continue
        owner = next((record for prefix, record in owned
                      if any(source.name.startswith(prefix+separator) for separator in ('-', '_', '.'))), None)
        if owner is None:
            skipped.append(dict(file=str(source), reason='No completed successful owned producer prefix'))
            continue
        if left['bytes'] != right['bytes'] or left['device'] != right['device'] or left['mode'] != right['mode']:
            skipped.append(dict(file=str(source), reason='Size, filesystem, or mode differs'))
            continue
        source_data, archive_data = source.read_bytes(), archive_file.read_bytes()
        source_sha, archive_sha = digest(source_data), digest(archive_data)
        if source_sha != archive_sha or source_data != archive_data:
            skipped.append(dict(file=str(source), reason='Full SHA256/byte comparison differs'))
            continue
        if snapshot(source) != left or snapshot(archive_file) != right:
            raise ValueError('A candidate changed during immutable verification')
        entry = dict(runtime_file=str(source), archive_file=str(archive_file),
            owning_successful_producer=owner, sha256=source_sha, bytes=len(source_data),
            runtime_before=left, archive_before=right, full_bytes_equal=True,
            operation='planned atomic runtime-path replacement by a hard link to identical archive bytes',
            complete=False)
        rows.append(entry);save()
        temporary=source.with_name(source.name+'.same-bytes-hardlink.tmp')
        if temporary.exists():
            raise FileExistsError('A maintenance temporary already exists')
        os.link(archive_file, temporary)
        try:
            if (snapshot(source) != left or snapshot(archive_file)['inode'] != right['inode']
                    or digest(archive_file.read_bytes()) != source_sha):
                raise ValueError('An immutable candidate changed before replacement')
            os.replace(temporary, source)
        finally:
            if temporary.exists():
                temporary.unlink()
        after, archive_after = snapshot(source), snapshot(archive_file)
        if (after['inode'] != archive_after['inode'] or after['bytes'] != left['bytes']
                or digest(source.read_bytes()) != source_sha):
            raise ValueError('Full original bytes/path were not preserved')
        entry.update(operation='atomic runtime-path replacement by a hard link to identical archive bytes',
            complete=True, runtime_after=after, archive_after=archive_after,
            full_source_sha256_after=source_sha,
            original_runtime_allocated_bytes_deduplicated=left['allocated_bytes'])
        save()
    report.update(completed=True, finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        files_consolidated=sum(row['complete'] for row in rows),
        logical_bytes_consolidated=sum(row['bytes'] for row in rows if row['complete']),
        allocated_bytes_of_old_single_link_copies=sum(row['original_runtime_allocated_bytes_deduplicated']
            for row in rows if row['complete']), free_bytes_after=shutil.disk_usage(runtime).free,
        free_space_change_not_attributed_exclusively_due_to_concurrent_jobs=True,
        all_original_paths_and_bytes_preserved=all(row['complete'] for row in rows))
    save()
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out.read_bytes()),
        completed=True,files=report['files_consolidated'],
        bytes=report['logical_bytes_consolidated'],
        prior_allocated_bytes=report['allocated_bytes_of_old_single_link_copies'],
        free_after=report['free_bytes_after'])),flush=True)


if __name__ == '__main__':
    main()
