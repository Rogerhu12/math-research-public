#!/usr/bin/env python3
"""Split a completed gzip JSONL comparison into independently compressed parts.

The uncompressed byte stream and every line are preserved. This is storage
only: no bound is recomputed or changed. The source gzip may then be kept in
scratch instead of committed above the repository's single-file limit.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def identity(path):
    path = Path(path)
    return {'file': path.name, 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path, required=True)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--rows-per-part', type=int, default=6000)
    args = ap.parse_args()
    if args.rows_per_part <= 0 or args.manifest.exists():
        raise ValueError('Positive part size and new manifest required')
    whole = hashlib.sha256()
    uncompressed_bytes = 0
    parts, rows = [], 0
    stem = args.manifest.name.removesuffix('-manifest.json')
    with gzip.open(args.input, 'rb') as source:
        while True:
            lines = []
            for _ in range(args.rows_per_part):
                line = source.readline()
                if not line:
                    break
                value = json.loads(line)
                if value['index'] != rows + len(lines):
                    raise ValueError('Row indices are not consecutive')
                lines.append(line)
            if not lines:
                break
            content = b''.join(lines)
            target = args.manifest.parent / f'{stem}-part{len(parts):03d}.jsonl.gz'
            if target.exists():
                raise FileExistsError(target)
            with target.open('wb') as raw:
                with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as out:
                    out.write(content)
            if target.stat().st_size >= 5_000_000:
                raise ValueError('Part exceeds repository limit')
            parts.append({**identity(target), 'first_row': rows,
                          'rows': len(lines), 'uncompressed_bytes': len(content),
                          'uncompressed_sha256': hashlib.sha256(content).hexdigest()})
            whole.update(content)
            uncompressed_bytes += len(content)
            rows += len(lines)
    result = {'schema': 'gzip-jsonl-parts-v1', 'original_gzip': identity(args.input),
              'rows': rows, 'uncompressed_bytes': uncompressed_bytes,
              'uncompressed_sha256': whole.hexdigest(), 'parts': parts,
              'mathematical_data_changed': False, 'packing_script': identity(__file__)}
    args.manifest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'manifest': str(args.manifest), 'rows': rows,
                      'parts': len(parts), 'part_bytes': [p['bytes'] for p in parts]}))


if __name__ == '__main__':
    main()
