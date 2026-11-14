#!/usr/bin/env python3
"""Close an attempted step without inventing an accepted state.

Storage only: no F, J, direction, or physical field is recomputed. Completed
trials and actual process exits remain distinct from incomplete exceptions.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path


def identity(path):
    path = Path(path)
    return dict(path=str(path), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def write_new(path, value):
    if path.exists():
        raise FileExistsError(path)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--direction-id', required=True)
    parser.add_argument('--reason', required=True)
    parser.add_argument('--extra', type=Path, action='append', default=[])
    args = parser.parse_args()
    request = json.loads(args.request.read_text())
    prefix, root = Path(request['run_prefix']), Path(request['cache_dir'])
    stem, notes = prefix.name, prefix.parent
    if (root / 'accepted-result.json').exists():
        raise ValueError('This closer is only for a step with no saved acceptance')
    direction_path = root / 'directions' / args.direction_id / 'summary.json'
    direction = json.loads(direction_path.read_text())
    files = {args.request, direction_path, Path(direction['direction']['path']),
             Path(direction['saved_Schur_summary']['path']), Path(__file__)}
    trials = []
    for path in sorted((root / 'trials' / args.direction_id).glob('back-*.json')):
        row = json.loads(path.read_text())
        if row.get('accepted'):
            raise ValueError('An accepted trial cannot be closed as rejected')
        trials.append(dict(result=identity(path), alpha=row['alpha'],
            actual_full_residual_evaluated=row['actual_full_residual_evaluated'],
            actual_norm=row.get('objective_norm'), actual_cost=row.get('actual_cost'),
            rejection=row.get('rejection'), diagnostics=row.get('diagnostics'),
            locations=row.get('locations')))
        files.add(path)
    if not trials or not any(t['actual_full_residual_evaluated'] for t in trials):
        raise ValueError('At least one genuine complete trial is required')
    receipts = []
    for path in sorted(notes.glob(stem + '*-process-receipt.json')):
        row = json.loads(path.read_text())
        receipts.append(dict(identity(path), actual_child_returncode=row.get('actual_child_returncode'),
            seconds=row.get('seconds'), peak_rss_kib=row.get('kernel_child_maximum_resident_KiB')))
        files.add(path)
    for pattern in (stem + '*-report.json', stem + '*-progress.jsonl'):
        files.update(notes.glob(pattern))
    for name in ('normal-reference.json', 'normal-partition-plan.json',
                 'normal-partitioned-summary.json', 'baseline-summary.json'):
        path = root / name
        if path.exists():
            files.add(path)
    normal_path = root / 'normal-partitioned/manifest.json'
    normal = json.loads(normal_path.read_text())
    files.add(normal_path)
    tiles = []
    for path in sorted((root / 'normal-tiles').glob('*/manifest.json')):
        row = json.loads(path.read_text())
        tiles.append(dict(id=path.parent.name, manifest=identity(path), schema=row['schema'],
            logical_manifest=row.get('logical_manifest'),
            logical_numerical_bytes=row.get('logical_numerical_bytes'),
            compressed_numerical_bytes=row.get('compressed_numerical_bytes')))
    inventory = write_new(prefix.with_name(stem + '-reproducible-cache-inventory.json'), dict(
        schema='fd2d-regenerable-normal-cache-inventory-v2',
        complete_normal_manifest=identity(normal_path), normal_pieces=normal['pieces'], tiles=tiles,
        matrix_pieces_in_publication=False, original_files_unchanged=True))
    summary = write_new(prefix.with_name(stem + '-closed-summary.json'), dict(
        schema='fd2d-staged-actual-rejected-step-summary-v1',
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        request=identity(args.request), unchanged_latest_accepted_input=identity(request['settings']['warm_start']),
        new_accepted_state=None, reason_for_ending_this_step=args.reason, trials=trials,
        complete_normal=identity(normal_path), actual_process_receipts=receipts,
        numerical_calculations_in_closure=0, strong_target_complete=False,
        continuous_geometry_certificate=False, source=identity(__file__)))
    files.update((summary, inventory)); files.update(args.extra)
    compression = []
    for path in sorted(files.copy()):
        if path.stat().st_size >= 1_000_000:
            raw = path.read_bytes(); compressed = path.with_name(path.name + '.gz')
            if compressed.exists():
                if gzip.decompress(compressed.read_bytes()) != raw:
                    raise ValueError('Existing gzip differs')
            else:
                compressed.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
            if gzip.decompress(compressed.read_bytes()) != raw:
                raise ValueError('Gzip roundtrip differs')
            compression.append(dict(original=identity(path), gzip=identity(compressed),
                                    restore_original_path_before_original_loader=True))
            files.remove(path); files.add(compressed)
    pack = write_new(prefix.with_name(stem + '-publication-compression.json'), dict(
        schema='fd2d-lossless-publication-compression-v1', entries=compression,
        originals_retained_locally=True))
    files.add(pack)
    rows = [identity(path) for path in sorted(files)]
    if max(row['bytes'] for row in rows) >= 5_000_000:
        raise ValueError('An artifact exceeds the publication limit')
    target = write_new(prefix.with_name(stem + '-closed-manifest.json'), dict(
        schema='fd2d-closed-research-artifact-manifest-v1', closed=True,
        scope='Input, complete normal inventory, saved direction, actual rejected trials and process failures; no new acceptance',
        unchanged_latest_accepted_input=identity(request['settings']['warm_start']),
        new_accepted_state=None, strong_target_complete=False, files=rows))
    print(json.dumps(dict(manifest=identity(target), files=len(rows),
                         bytes=sum(r['bytes'] for r in rows), maximum=max(r['bytes'] for r in rows))))


if __name__ == '__main__':
    main()
