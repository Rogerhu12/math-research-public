#!/usr/bin/env python3
"""Audit saved g0 prefix first integrals and expanded-domain dependencies.

Input certificates are read-only.  Direct first-integral and expanded-domain
reports missing from the input manifest are listed for archiving.  Every other
reachable path/SHA pair is checked and listed as an external immutable input.
No field sampling or promotion of an incomplete prefix is performed.
"""
from __future__ import annotations

import argparse
from collections import deque
import gzip
import hashlib
import json
from pathlib import Path


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root = Path.cwd().resolve()
    hashes = {}
    checked = {}
    provenance = {}
    queue = deque()
    visited = set()
    historical = []

    def sha(path):
        path = Path(path).resolve()
        if path not in hashes:
            hashes[path] = hashlib.sha256(path.read_bytes()).hexdigest()
        return hashes[path]

    def name(path):
        path = Path(path).resolve()
        return str(path.relative_to(root)) if path.is_relative_to(root) else str(path)

    def register(path, digest, reason):
        path = Path(path)
        # Finite-rectangle manifests store shard basenames relative to their
        # own directory; topic-qualified paths retain their original meaning.
        if not path.is_absolute() and path.parent == Path('.') and Path(reason).is_file():
            path = Path(reason).parent/path
        path = path.resolve()
        if not path.is_file() or sha(path) != digest:
            raise ValueError('referenced input is absent or changed: '+str(path)+' (from '+reason+')')
        if path in checked and checked[path] != digest:
            raise ValueError('one path has two incompatible certificate hashes')
        checked[path] = digest
        provenance.setdefault(path, set()).add(reason)
        if path.name.endswith(('.json', '.json.gz')) and path not in visited:
            queue.append(path)
        return path

    manifest = read(args.manifest)
    original = set()
    reports = []
    archive = set()
    first_checks = []
    selected_expanded = []
    attempts = []
    for row in manifest['files']:
        path = register(row['path'], row['sha256'], 'original prefix manifest')
        original.add(path)
        doc = read(path)
        if not isinstance(doc, dict) or not doc.get('complete_continuous_true_density_proved'):
            continue
        if not doc.get('complete'):
            raise ValueError('a selected g0 leaf is incomplete')
        reports.append(path)
        link = doc['first_integral_file']
        first_path = register(link['path'], link['sha256'], 'selected complete finite first integral')
        first = read(first_path)
        if (first['identity'] != doc['identity']
            or first['density_coefficient_sha256'] != doc['density_coefficient_sha256']
            or not first.get('coefficients')):
            raise ValueError('finite first integral has a different density identity')
        archive.add(first_path)
        first_checks.append(dict(report_path=name(path), report_sha256=sha(path),
            first_path=name(first_path), first_sha256=sha(first_path),
            positive_coefficient_count=len(first['coefficients']),
            complete_same_density_identity=True))
        expanded = doc.get('expanded_true_field_domain')
        if expanded and expanded.get('path'):
            selected = register(expanded['path'], expanded['sha256'], 'explicit expanded-domain result')
            archive.add(selected)
            if expanded.get('proved'):
                if not read(selected).get('complete'):
                    raise ValueError('selected expanded-domain proof is incomplete')
                selected_expanded.append(dict(report_path=name(path), domain_path=name(selected),
                    domain_sha256=sha(selected)))
            else:
                attempts.append(dict(path=name(selected), sha256=sha(selected),
                    used_as_proved_domain=False, original_small_domain_retained=True))
        if expanded:
            for item in expanded.get('attempts', []):
                attempt = register(item['path'], item['sha256'], 'explicit expanded-domain attempt provenance')
                archive.add(attempt)
                attempts.append(dict(path=name(attempt), sha256=sha(attempt),
                    used_as_proved_domain=bool(item.get('proved'))))

    def walk(value, origin):
        if isinstance(value, dict):
            if isinstance(value.get('path'), str) and isinstance(value.get('sha256'), str):
                register(value['path'], value['sha256'], origin)
            for key, path in value.items():
                if key.endswith('_path') and isinstance(path, str):
                    digest = value.get(key[:-5]+'_sha256')
                    if isinstance(digest, str):
                        if key == 'snapshot_of_index_path':
                            historical.append(dict(recorded_in=origin, path=path,
                                captured_sha256=digest,
                                meaning='historical live-index provenance; the separately checked immutable snapshot is authoritative'))
                            continue
                        register(path, digest, origin)
            dependencies = value.get('dependency_sha256')
            if isinstance(dependencies, dict):
                for filename, digest in dependencies.items():
                    if isinstance(digest, str):
                        register(Path(__file__).with_name(filename), digest, origin+' source dependency')
            for child in value.values():
                walk(child, origin)
        elif isinstance(value, list):
            for child in value:
                walk(child, origin)

    while queue:
        path = queue.popleft()
        if path in visited:
            continue
        visited.add(path)
        walk(read(path), name(path))

    source = Path(__file__).resolve()
    checked[source] = sha(source)
    provenance[source] = {'dependency-closure audit source'}
    archive.add(source)
    archive.difference_update(original)
    rows = []
    for path in sorted(archive):
        size = path.stat().st_size
        if size >= 5_000_000 or size > 1_000_000 and path.suffix != '.gz':
            raise ValueError('archive member violates repository size convention')
        rows.append(dict(path=name(path), sha256=sha(path), bytes=size))
    external = [dict(path=name(path), sha256=digest,
        referenced_by=sorted(provenance[path])) for path, digest in sorted(checked.items())
        if path not in archive and path not in original]
    result = dict(kind='actual_g0_prefix_complete_first_and_domain_dependency_closure',
        complete=True, whole_forward_leg_complete=False, mathematical_values_recomputed=False,
        audit_source_sha256=sha(source), input_manifest_path=str(args.manifest),
        input_manifest_sha256=sha(args.manifest),
        original_completed_segments=manifest['completed_segments'],
        selected_complete_g0_report_count=len(reports),
        all_first_integral_identities_checked=True, first_integral_checks=first_checks,
        selected_expanded_domains=selected_expanded,
        expanded_attempts_preserved_without_promoting_failed_attempts=attempts,
        all_nonhistorical_reachable_explicit_path_SHA_pairs_checked=True,
        historical_snapshot_provenance_not_required_to_match_current_live_file=historical,
        checked_unique_paths=len(checked), checked_json_documents=len(visited),
        archive_required=rows, files=rows, total_files=len(rows),
        total_bytes=sum(row['bytes'] for row in rows), external_required_inputs=external,
        original_manifest_unchanged=True,
        scope='Additional finite first integrals and actual expanded-domain reports; existing immutable ancestors remain explicit external inputs.',
        limitations=['No missing coefficient matrix is reconstructed from its hash.',
            'A stored density hash without a path is not represented as a saved matrix.',
            'No whole-forward, endpoint, twist, or KAM conclusion is asserted.'])
    raw = (json.dumps(result, indent=2)+'\n').encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.suffix == '.gz':
        raw = gzip.compress(raw, mtime=0)
    elif len(raw) > 1_000_000:
        raise ValueError('large audit manifest must use gzip')
    args.out.write_bytes(raw)
    print(dict(path=str(args.out), sha256=sha(args.out), archive_files=len(rows),
        archive_bytes=result['total_bytes'], checked_paths=len(checked),
        external_inputs=len(external)))


if __name__ == '__main__':
    main()
