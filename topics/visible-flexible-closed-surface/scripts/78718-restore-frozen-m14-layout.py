#!/usr/bin/env python3
"""Restore exact frozen inputs at their recorded paths in a new environment.

This copies bytes only.  It imports no scientific package and starts no solver.
The recreated directory is not evidence of recovery of the former process.
Every frozen input is checked before any writes, and conflicting existing files
are rejected rather than overwritten.  The extra entry sources retain their
repository bytes; the original reference and its 97 bindings are not rewritten.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

FROZEN_ROOT = Path('/workspace/scratch/db6f0b0e7462/math-research')
TOPIC = Path('topics/visible-flexible-closed-surface')
REFERENCE = TOPIC / 'notes/2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json'
REFERENCE_SHA = 'e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83'
EXTRA_SCRIPTS = (
    'db6f-prefix-direct-csc-foundation-v2.py',
    'db6f-prefix-check-direct-csc-foundation.py',
    'db6f-prefix-test-direct-csc-bytes.py',
    'db6f-prefix-direct-csc-entry-gates.py',
    'db6f-prefix-select-direct-csc.py',
    'db6f-prefix-spectral-true-m14-direct-csc.py',
    'db6f-prefix-prepare-spectral-true-m14-direct-csc.py',
    'db6f-prefix-audit-spectral-true-m14-direct-csc.py',
    'db6f-prefix-spectral-true-m14-release-lu.py',
    'db6f-prefix-prepare-spectral-true-m14-release-lu.py',
    'db6f-prefix-audit-spectral-true-m14-release-lu.py',
    'db6f-prefix-spectral-true-m14.py',
    'db6f-prefix-prepare-spectral-true-m14.py',
    'db6f-prefix-audit-spectral-true-m14.py',
    'db6f-prefix-select-domain-newton-release-lu.py',
    'db6f-prefix-domain-newton-release-lu.py',
    'db6f-prefix-check-domain-newton-release-lu.py',
    'db6f-root-run-space-guarded.py',
)
EXTRA_NOTES = (
    '2026-11-09-db6f-prefix-spectral-true-m14-interface.md',
    '2026-11-09-db6f-prefix-spectral-true-m14-interface-sources.json',
    '2026-11-09-db6f-tail-review-spectral-true-m14-interface.md',
    '2026-11-09-db6f-prefix-spectral-true-m14-implementation.md',
    '2026-11-09-db6f-prefix-newton-release-lu-method.md',
    '2026-11-09-db6f-prefix-newton-release-lu-sources.json',
    '2026-11-09-db6f-prefix-newton-release-lu-protocol.json',
    '2026-11-09-db6f-prefix-newton-release-lu-observed-validation.json',
    '2026-11-09-db6f-prefix-spectral-true-m14-release-lu-implementation.md',
    '2026-11-09-db6f-prefix-direct-csc-foundation-method.md',
    '2026-11-09-db6f-prefix-direct-csc-publication-role-erratum.md',
    '2026-11-09-db6f-tail-review-direct-csc-foundation-v2.md',
    '2026-11-09-db6f-prefix-direct-csc-byte-test-plan.md',
    '2026-11-09-db6f-prefix-direct-csc-byte-test-planned-run.json',
    '2026-11-09-db6f-prefix-spectral-true-m14-direct-csc-method.md',
    '2026-11-09-db6f-prefix-spectral-true-m14-direct-csc-source-transforms.json',
    '2026-11-10-db6f-root-direct-csc-complete-static-adoption.md',
    '2026-11-10-db6f-tail-review-direct-csc-full-entry.md',
    '2026-11-09-db6f-tail-review-direct-csc-byte-test.md',
)


def identity(path: Path) -> dict:
    raw = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def check_destination(path: Path) -> None:
    require(path.is_relative_to(FROZEN_ROOT), 'Destination escaped frozen root')
    for ancestor in (path, *path.parents):
        require(not ancestor.is_symlink(), 'Symlink in frozen layout: ' + str(ancestor))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-repo', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    repo = args.source_repo.resolve()
    require(repo != FROZEN_ROOT, 'Source must be the new checkout')
    require(not args.out.exists(), 'Refuse an existing restoration report')
    reference_path = repo / REFERENCE
    require(identity(reference_path)['sha256'] == REFERENCE_SHA, 'Frozen reference changed')
    reference = json.loads(reference_path.read_text())
    require(len(reference['bindings']) == 97, 'Frozen binding count changed')
    plan = {}
    external = []
    for row in reference['bindings']:
        destination = Path(row['path'])
        if not destination.is_relative_to(FROZEN_ROOT):
            require(identity(destination) == row, 'External source changed: ' + str(destination))
            external.append(row)
            continue
        relative = destination.relative_to(FROZEN_ROOT)
        source = repo / relative
        actual = identity(source)
        require(actual['bytes'] == row['bytes'] and actual['sha256'] == row['sha256'],
                'Frozen source input differs: ' + str(relative))
        plan[destination] = (source, actual, True)
    extras = [REFERENCE]
    extras += [TOPIC / 'scripts' / name for name in EXTRA_SCRIPTS]
    extras += [TOPIC / 'notes' / name for name in EXTRA_NOTES]
    for relative in extras:
        source = repo / relative
        destination = FROZEN_ROOT / relative
        if destination not in plan:
            plan[destination] = (source, identity(source), False)
    # Validate every source and every destination before creating any file.
    for destination, (source, record, frozen) in plan.items():
        check_destination(destination)
        require(identity(source) == record, 'Source changed during planning')
        if destination.exists():
            existing = identity(destination)
            require(existing['bytes'] == record['bytes'] and existing['sha256'] == record['sha256'],
                    'Refuse conflicting existing destination: ' + str(destination))
    root_preexisted = FROZEN_ROOT.exists()
    rows = []
    for destination, (source, record, frozen) in sorted(plan.items()):
        existed = destination.exists()
        if not existed:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open('xb') as handle:
                handle.write(source.read_bytes())
        actual = identity(destination)
        require(actual['bytes'] == record['bytes'] and actual['sha256'] == record['sha256'],
                'Restored file differs: ' + str(destination))
        rows.append({'source': str(source), 'destination': str(destination),
                     'bytes': actual['bytes'], 'sha256': actual['sha256'],
                     'frozen_reference_binding': frozen, 'already_present_identical': existed})
    report = {
        'schema': '78718-exact-frozen-layout-restoration-v1',
        'status': 'COPIED_AND_BYTE_VERIFIED_NO_SOLVER',
        'new_environment_source_repo': str(repo),
        'restored_frozen_root': str(FROZEN_ROOT),
        'frozen_root_preexisted': root_preexisted,
        'reference': identity(reference_path),
        'restorer': identity(Path(__file__)),
        'frozen_bindings_verified': len(reference['bindings']),
        'external_bindings_verified': external,
        'files': rows,
        'copied_bytes': sum(row['bytes'] for row in rows if not row['already_present_identical']),
        'old_process_recovered': False,
        'old_process_exit_known': False,
        'solver_started': False,
        'scope': 'Exact files reconstructed in a new environment; original absolute-path identities retained. No mathematical or process-success claim.',
    }
    encoded = (json.dumps(report, indent=2, sort_keys=True) + '\n').encode()
    require(len(encoded) < 100000, 'Unexpectedly large restoration metadata')
    with args.out.open('xb') as handle:
        handle.write(encoded)
    print(json.dumps({'status': report['status'], 'files': len(rows),
                      'bytes': report['copied_bytes'], 'out': str(args.out.resolve()),
                      'out_sha256': identity(args.out)['sha256']}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
