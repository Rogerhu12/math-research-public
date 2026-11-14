#!/usr/bin/env python3
"""Complete the historical Node cache, then inspect literal import closure.

The nine-file Git-blob manifest was already used by the original tail loader.
In particular its CommonJS cell source is not among the 97 reference bindings.
No module is imported or evaluated and no numerical operation is performed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

OLD = Path('/workspace/scratch/db6f0b0e7462/math-research')
REL = Path('topics/visible-flexible-closed-surface')
CACHE = REL / 'repro/source-root/topics/large-amplitude-twist-flex/scripts'


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-repo', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    root = args.source_repo.resolve()
    manifest_path = root / REL / 'notes/closing_tail_dependency_blobs.json'
    manifest = json.loads(manifest_path.read_text())
    records = []
    for name, expected_blob in sorted(manifest.items()):
        if Path(name).name != name:
            raise ValueError('Non-basename in frozen source map')
        source = root / CACHE / name
        raw = source.read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if blob != expected_blob:
            raise ValueError('Frozen Git blob mismatch: ' + name)
        dest = OLD / CACHE / name
        if dest.exists():
            if dest.is_symlink() or dest.read_bytes() != raw:
                raise ValueError('Conflicting frozen destination: ' + str(dest))
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('xb') as stream:
                stream.write(raw)
        records.append({**identity(dest), 'git_blob': blob})
    pending = [p for p in (OLD / REL / 'scripts').glob('*.mjs')]
    pending += [OLD / CACHE / name for name in manifest]
    visited = set()
    relative = re.compile(r'''(?:from\s+|import\s*\(\s*|import\s+|require\s*\(\s*)['"](\.[^'"]+)['"]''')
    source_call = re.compile(r'''source\(\s*['"]([^'"]+)['"]\s*\)''')
    while pending:
        path = pending.pop().resolve()
        if path in visited:
            continue
        if not path.is_file():
            raise FileNotFoundError(path)
        visited.add(path)
        text = path.read_text()
        pending.extend(path.parent / spec for spec in relative.findall(text))
        pending.extend(OLD / CACHE / spec for spec in source_call.findall(text))
    report = {
        'status': 'FROZEN_NODE_CACHE_AND_LITERAL_CLOSURE_PRESENT',
        'manifest': identity(manifest_path), 'restorer': identity(Path(__file__)),
        'frozen_cache': records,
        'literal_dependency_files': [identity(p) for p in sorted(visited)],
        'scope': 'Byte identities and literal file existence only; no module import, numerical execution, or exhaustive proof about arbitrary dynamic paths.',
        'solver_calls': 0,
    }
    encoded = (json.dumps(report, indent=2) + '\n').encode()
    if len(encoded) >= 100000:
        raise ValueError('Unexpectedly large source metadata')
    with args.out.open('xb') as stream:
        stream.write(encoded)
    print(json.dumps({'status': report['status'], 'frozen_cache_files': len(records),
                      'literal_dependency_files': len(visited), 'out': str(args.out.resolve())}))


if __name__ == '__main__':
    main()
