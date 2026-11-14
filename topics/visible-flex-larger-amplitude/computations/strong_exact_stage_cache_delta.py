#!/usr/bin/env python3
"""Archive only new immutable completed stages relative to recorded archives.

The original archive format and its full member/hash restore checks are used.
The identity text is included, and each predecessor is recorded by checksum.
An incremental or partial set of component evaluations is never an accepted
nonlinear solution. Missing older stages are ordinary cache misses on restore.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile
from strong_exact_stage_cache_archive import atomic, inspect_archive, sha

SELF_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
ARCHIVE_SHA = hashlib.sha256(Path(__file__).with_name(
    'strong_exact_stage_cache_archive.py').read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache-root', type=Path, required=True)
    parser.add_argument('--previous-manifest', type=Path, action='append', required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    root = args.cache_root.resolve()
    if len(root.name) != 64 or any(c not in '0123456789abcdef' for c in root.name):
        raise ValueError('One explicit complete cache identity is required')
    previous, known = [], {}
    for path in args.previous_manifest:
        data = path.read_bytes()
        old = json.loads(data)
        if (old['schema'] != 'exact-stage-cache-immutable-archive-v1'
                or old['stage_identity_sha256'] != root.name):
            raise ValueError('Predecessor cache identity/schema differs')
        for row in old['files']:
            name = row['path']
            if name in known and known[name] != row:
                raise ValueError('Predecessor immutable checksums conflict')
            known[name] = row
        previous.append(dict(path=str(path), bytes=len(data), sha256=sha(data)))
    rows, prior_matches = [], 0
    for path in sorted(root.rglob('*')):
        if not path.is_file() or not (path.suffix == '.bin' or path.name == 'identity.txt'):
            continue
        if path.is_symlink():
            raise ValueError('Refuse a linked cache component')
        data = path.read_bytes()
        row = dict(path=path.relative_to(root.parent).as_posix(), bytes=len(data), sha256=sha(data))
        if row['path'] in known:
            if row != known[row['path']]:
                raise ValueError('An earlier immutable component changed')
            prior_matches += 1
            if path.name != 'identity.txt':
                continue
        rows.append(row)
    if not any(Path(row['path']).name == 'identity.txt' for row in rows):
        raise ValueError('Complete identity text is missing')
    groups, current, size = [], [], 0
    for row in rows:
        if current and size+row['bytes'] > 3_500_000:
            groups.append(current)
            current, size = [], 0
        current.append(row)
        size += row['bytes']
    if current:
        groups.append(current)
    expected, archives = {row['path']: row for row in rows}, []
    for index, group in enumerate(groups):
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode='wb', mtime=0, compresslevel=6) as gz:
            with tarfile.open(fileobj=gz, mode='w|') as tar:
                for row in group:
                    data = (root.parent/row['path']).read_bytes()
                    if len(data) != row['bytes'] or sha(data) != row['sha256']:
                        raise ValueError('A selected immutable input changed')
                    member = tarfile.TarInfo(row['path'])
                    member.size, member.mtime, member.mode = len(data), 0, 0o600
                    tar.addfile(member, io.BytesIO(data))
        data = buffer.getvalue()
        if len(data) >= 5_000_000:
            raise ValueError('Incremental archive exceeds the per-file limit')
        path = args.out_prefix.with_name(args.out_prefix.name+'-%03d.tar.gz'%index)
        atomic(path, data)
        row = dict(path=str(path), bytes=len(data), sha256=sha(data),
            members=[r['path'] for r in group])
        row['all_member_bytes_verified_after_compression'] = (
            inspect_archive(path, row, expected) == len(group))
        archives.append(row)
    manifest = Path(str(args.out_prefix)+'.json')
    report = dict(schema='exact-stage-cache-immutable-archive-v1', scope=__doc__,
        incremental=True, previous_manifests=previous,
        preceding_existing_files_checked=prior_matches,
        stage_identity_sha256=root.name, original_cache_root=str(root),
        stage_files=sum(r['path'].endswith('.bin') for r in rows),
        complete_files=len(rows), files=rows, archives=archives,
        snapshot_tool_sha256=SELF_SHA,
        retained_archive_verifier_and_restore_sha256=ARCHIVE_SHA,
        every_new_completed_original_stage_output_retained=True,
        nonlinear_solution_accepted=False, partial_or_complete_cache_is_not_a_tail_acceptance=True,
        restore_argv=['python', 'computations/strong_exact_stage_cache_archive.py', 'restore',
            '--manifest', str(manifest), '--cache-parent', str(root.parent)],
        restore_predecessors_first_for_all_recorded_stage_hits=True,
        identity_runtime_source_parameter_guard_still_applies=True)
    atomic(manifest, (json.dumps(report, indent=2)+'\n').encode())
    print(json.dumps(dict(manifest=str(manifest), new_stage_files=report['stage_files'],
        previous_existing_files_checked=prior_matches,
        total_archive_bytes=sum(a['bytes'] for a in archives))), flush=True)


if __name__ == '__main__':
    main()
