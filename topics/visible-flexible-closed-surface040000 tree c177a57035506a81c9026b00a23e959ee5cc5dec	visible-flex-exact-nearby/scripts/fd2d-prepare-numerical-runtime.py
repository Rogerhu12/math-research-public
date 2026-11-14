#!/usr/bin/env python3
"""Copy numerical source and its actual inputs outside the live git worktree.

This does not solve or certify a graph. Active outputs are kept in outputs/;
closed recoverable records can subsequently be copied to the repository.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--topic', type=Path, required=True)
    parser.add_argument('--destination', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    args = parser.parse_args()
    original = args.topic.resolve()
    destination = args.destination.resolve()
    if destination.exists() or args.manifest.exists():
        raise FileExistsError('Choose a new runtime directory and manifest')
    destination.mkdir(parents=True)
    copied_topic = destination/'topics/visible-flexible-closed-surface'
    copied_topic.mkdir(parents=True)
    for name in ('scripts', 'repro/source-root'):
        shutil.copytree(original/name, copied_topic/name,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    notes = copied_topic/'notes'
    notes.mkdir()
    # Some legacy prefix modules deliberately live in notes and are imported
    # through that path; copy this small source set as well as scripts.
    for source in (original/'notes').iterdir():
        if source.is_file() and source.suffix in {'.py', '.mjs', '.js'}:
            shutil.copyfile(source, notes/source.name)
    names = [
        'closing_tail_dependency_blobs.json',
        '2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14-frozen-profile.json',
        '2026-11-09-950f-prefix-adaptive-chart.json',
        '2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json',
        '2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz',
        '2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz',
        '2026-11-12-fd2d-numerical-m15-w22-resume-03-tail-warm-input.json.gz',
        '2026-11-12-fd2d-numerical-m15-w22-resume-05-tail-config.json',
    ]
    for name in names:
        shutil.copyfile(original/'notes'/name, notes/name)
    restart = notes/'2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz'
    metadata = json.loads(gzip.decompress(restart.read_bytes()))
    for chunk in metadata.get('pp_coefficient_chunks', []):
        shutil.copyfile(original/'notes'/chunk['file'], notes/chunk['file'])
    (destination/'outputs').mkdir()
    rows = []
    for file in sorted(copied_topic.rglob('*')):
        if not file.is_file():
            continue
        relative = file.relative_to(copied_topic)
        data = file.read_bytes()
        source = original/relative
        source_data = source.read_bytes()
        if data != source_data:
            raise RuntimeError('Source changed during its runtime copy: '+str(relative))
        rows.append({'relative': str(relative), 'original_path': str(source),
                     'copied_path': str(file), 'bytes': len(data),
                     'sha256': hashlib.sha256(data).hexdigest()})
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=original,
                          capture_output=True, text=True, check=True).stdout.strip()
    record = {'scope': 'Independent source/input runtime copy; no numerical solve or certificate',
              'original_topic': str(original), 'copied_topic': str(copied_topic),
              'outputs': str(destination/'outputs'), 'observed_git_HEAD': head,
              'files': rows, 'files_count': len(rows),
              'source_and_input_bytes': sum(row['bytes'] for row in rows),
              'all_copied_bytes_equal_at_copy': True,
              'contains_symlinks': any(p.is_symlink() for p in destination.rglob('*'))}
    encoded = gzip.compress((json.dumps(record, indent=2)+'\n').encode(), mtime=0)
    if len(encoded) >= 5_000_000:
        raise RuntimeError('Runtime manifest too large')
    args.manifest.write_bytes(encoded)
    (destination/'source-input-manifest.json.gz').write_bytes(encoded)
    print(json.dumps({'destination': str(destination), 'files': len(rows),
                      'copied_bytes': record['source_and_input_bytes'],
                      'manifest': str(args.manifest), 'manifest_bytes': len(encoded),
                      'manifest_sha256': hashlib.sha256(encoded).hexdigest(),
                      'contains_symlinks': record['contains_symlinks']}))


if __name__ == '__main__':
    main()
