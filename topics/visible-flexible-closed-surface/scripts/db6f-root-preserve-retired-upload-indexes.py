#!/usr/bin/env python3
"""Reversibly compress seven inactive, task-owned /tmp upload indexes.

Does not touch either current Git index, any object/ref, candidate or solver.
The publication shell was checked separately for an index override (none).
Only the exact historical byte identities below are eligible.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil

FILES = {
    'db6f-r21v1-upload-index': 'dd40146cf979e3a7b3ec3feb4082d2bceff800ada77935ba842ddee4f3b82673',
    'db6f-lowmetric6-upload-index': '4c1390751498caba1f7e0354cb8d29223c21b08b7fac5e729537a1987bcb26db',
    'db6f-lowmetric-upload-index': '4c1390751498caba1f7e0354cb8d29223c21b08b7fac5e729537a1987bcb26db',
    'db6f-critical2-upload-index': '0cd88662684c8dbfc6030ba084b7fc4615ca414f547a2ae0634dc446f4941f41',
    'db6f-refinement-upload-index': '3f6971afb07cc03f55455e47e31985b978888bcd8eb647c6dab8eb42d0cab438',
    'db6f-git-upload-index': 'd32d9d20a5bc514cf40a9455e63899caebfe7dc0b07c45b073fe8008668b2bfc',
    'db6f-git-small-upload-index': '1071dfffc8455e437636bcc14bc1ecb96801fa9772d7992e600493f39cad84a6',
}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for part in iter(lambda: f.read(1 << 20), b''):
            h.update(part)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    assert 'GIT_INDEX_FILE' not in os.environ
    assert not args.out.exists()
    directory = Path('/tmp/db6f-retired-upload-indexes')
    directory.mkdir(exist_ok=False)
    before = shutil.disk_usage('/tmp').free
    rows = []
    archives = {}
    for name, sha in FILES.items():
        source = Path('/tmp') / name
        assert source.is_file() and not source.is_symlink()
        stat = source.stat()
        assert digest(source) == sha
        archive = directory / (sha + '.gz')
        if sha not in archives:
            with archive.open('xb') as raw:
                with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=6) as packed:
                    with source.open('rb') as f:
                        shutil.copyfileobj(f, packed, 1 << 20)
                raw.flush()
                os.fsync(raw.fileno())
            h = hashlib.sha256()
            count = 0
            with gzip.open(archive, 'rb') as f:
                for part in iter(lambda: f.read(1 << 20), b''):
                    h.update(part)
                    count += len(part)
            assert count == stat.st_size and h.hexdigest() == sha
            archive.chmod(0o444)
            archives[sha] = {'path': str(archive), 'bytes': archive.stat().st_size,
                             'sha256': digest(archive), 'decoded_sha256': sha,
                             'decoded_bytes': count}
        assert archives[sha]['decoded_bytes'] == stat.st_size
        assert source.stat().st_mtime_ns == stat.st_mtime_ns and digest(source) == sha
        rows.append({'original_path': str(source), 'bytes': stat.st_size, 'sha256': sha,
                     'mode': stat.st_mode & 0o777, 'mtime_ns': stat.st_mtime_ns,
                     'archive': str(archive), 'decoded_bytes_verified_before_removal': True})
        source.unlink()
    report = {'status': 'INACTIVE_TASK_TEMP_INDEX_BYTES_PRESERVED_IN_VERIFIED_GZIP',
              'publication_shell_override_observation': {'receipt': 'c5f478', 'override_present': False},
              'files': rows, 'archives': list(archives.values()),
              'logical_bytes_reclaimed': sum(r['bytes'] for r in rows)-sum(r['bytes'] for r in archives.values()),
              'available_bytes_before': before, 'available_bytes_after': shutil.disk_usage('/tmp').free,
              'git_index_object_ref_or_candidate_mutated': False,
              'restoration': 'For the selected original_path, gzip-decompress its archive into a new file; verify byte count and SHA256 against this record before reuse. No Git commands are needed.',
              'scope': 'Local inactive temporary Git index snapshots only. Archives stay in /tmp; no payload is published.'}
    data = json.dumps(report, indent=2) + '\n'
    (directory / 'manifest.json').write_text(data)
    with args.out.open('x') as f:
        f.write(data)
    print(json.dumps({'status': report['status'], 'original_count': len(rows),
                      'archive_count': len(archives), 'logical_bytes_reclaimed': report['logical_bytes_reclaimed'],
                      'available_bytes_after': report['available_bytes_after'], 'report_sha256': digest(args.out)}))


if __name__ == '__main__':
    main()
