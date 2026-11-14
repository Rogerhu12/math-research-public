#!/usr/bin/env python3
"""Restore only exact published Storage C text bytes; execute no recovered code.

The A/B dependency closure and the independent C runtime replay remain separate.
An existing destination is never overwritten on any byte mismatch.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


EXPECTED = {
    'db6f-prefix-angular-metric-storage.py': (24286, '2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c'),
    'db6f-prefix-export-closed-mesh-storage.py': (25497, 'd776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1'),
    'db6f-prefix-review-closed-mesh-storage.py': (11115, '698e8b0528ffa7b1bbe1bc84c574079f60261156f1d3a6ddae048af0f9c0c479'),
    'db6f-prefix-terminal-error-storage.py': (45587, '809cc7ab61903f11847653fda018506f7c2bed38a7501007909200eb0bf69584'),
    'db6f-prefix-terminal-error-storage-v2.py': (48456, 'a00f8210d561983e9d137a848cb7b582e33de8450c0b70497e3933080c297aa1'),
    'db6f-prefix-terminal-error-storage-v3.py': (48711, '8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7'),
    '2026-11-09-db6f-prefix-storage-gates-transformations.json': (24049, '0417ac80883dda492618f8535a06ce0eaab230decf0eec4751d2b8c41b25dd88'),
    '2026-11-09-db6f-prefix-storage-terminal-v2-transformations.json': (5307, '82bbb53a65803c1f2531a6d2544f82d86f820d458acfeb5494f07f3d7b7f3d69'),
    '2026-11-09-db6f-prefix-storage-terminal-v3-transformations.json': (3146, '4299872c6189de869d137682ace26eee965fdabc0af01a2c47a25342bab1e336'),
    'db6f-prefix-check-storage-gates-v4.py': (13975, '59c250c55cfe731753f0ee1639728dd4d8b67fca0134e480ebd9f7ca1e55426c'),
}


def identity(path):
    raw = path.read_bytes()
    return dict(path=str(path.resolve()), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    repo = args.repo.resolve()
    topic = repo / 'topics/visible-flexible-closed-surface'
    index = topic / 'notes/2026-11-09-db6f-prefix-storage-c-recovered-text-index.md'
    if args.out.exists():
        raise FileExistsError(args.out)
    expression = re.compile(
        r'Original path: `([^`]+)`.*?Recovery path: `([^`]+)`.*?'
        r'UTF-8 bytes: ([0-9]+).*?SHA256: `([0-9a-f]{64})`', re.S)
    rows = expression.findall(index.read_text())
    if len(rows) != len(EXPECTED):
        raise ValueError('Recovery index does not list exactly the frozen ten files')
    ready, seen = [], set()
    for original, recovery, size, digest in rows:
        destination, source = repo / original, repo / recovery
        if not destination.resolve().is_relative_to(topic.resolve()):
            raise ValueError('Destination outside the specified topic')
        name = destination.name
        if name in seen or EXPECTED.get(name) != (int(size), digest):
            raise ValueError('Unexpected or duplicate frozen identity: ' + name)
        seen.add(name)
        raw = source.read_bytes()
        if len(raw) != int(size) or hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError('Recovery copy does not match its frozen identity: ' + name)
        present = destination.exists()
        if present and (destination.is_symlink() or destination.read_bytes() != raw):
            raise ValueError('Conflicting existing intended source: ' + str(destination))
        ready.append((source, destination, raw, present))
    # Only after the entire batch passes identity/conflict checks do writes begin.
    records = []
    for source, destination, raw, present in ready:
        if not present:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open('xb') as stream:
                stream.write(raw)
        records.append(dict(recovery_copy=identity(source), restored_source=identity(destination),
                            intended_path_preexisted=present))
    report = dict(status='EXACT_PUBLISHED_STORAGE_C_TEXT_BYTES_RESTORED',
                  scope='Text byte restoration only. No recovered Python is imported or run; no geometry, producer, solver, matrix, or continuous certificate is executed. A/B missing inputs and independent runtime replay are not discharged.',
                  index=identity(index), restorer=identity(Path(__file__)), files=records,
                  actual_numerical_calls=0)
    with args.out.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(status=report['status'], files=len(records),
                          restored=sum(not x['intended_path_preexisted'] for x in records))))


if __name__ == '__main__':
    main()
