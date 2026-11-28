#!/usr/bin/env python3
"""Archive only explicitly inventoried cold native inputs without changing bytes.

Each independent gzip base stores a complete literal static template. Each input
stores gzip(input XOR base), using the already reviewed v1 restoration routine.
The manifest is durable before any original is removed. Outputs, records, packet
files, unequal-size inputs and all files outside the explicit plan stay intact.
Scientific arrays remain local scratch files, outside the Git repository.
"""
import argparse
import gzip
import json
import os
from pathlib import Path
import shutil
import time

import numpy as np

import lossless_native_xor_archive as codec


RESERVE = 128 * 1024**2


def guard(root, size):
    while shutil.disk_usage(root).free < RESERVE + size + 2 * 1024**2:
        print(json.dumps(dict(event='cold_archive_disk_guard_waiting',
                              free=shutil.disk_usage(root).free,
                              required=RESERVE + size + 2 * 1024**2)), flush=True)
        time.sleep(5)


def write_bytes(path, data):
    guard(path.parent, len(data))
    with path.open('xb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def original_bytes(row):
    p = Path(row['path'])
    data = codec.checked(row)
    if len(data) != row['bytes']:
        raise ValueError('Original length changed: ' + str(p))
    return data


def archive(args):
    plan_path = args.plan.resolve()
    plan = json.loads(plan_path.read_text())
    out = args.outdir.resolve()
    repo = Path(__file__).resolve().parents[5]
    if out.exists() or out == repo or repo in out.parents:
        raise ValueError('Use a new scratch directory outside Git')
    if plan['schema'] != 'held10-five-cold-native-roots-plan-v1':
        raise ValueError('An explicit frozen inventory is required')
    for item in plan['roots']:
        terminal = json.loads(codec.checked(item['terminal_summary']))
        if terminal['status'] != item['terminal_status'] or terminal['status'] not in (
                'original_tail_route_failed', 'original_intermediate_mode_returned'):
            raise ValueError('No matching original terminal controller status')
        root = Path(item['root']).resolve()
        if root == repo or repo in root.parents:
            raise ValueError('Native inputs must remain outside Git')
        for row in [item['base']] + item['inputs']:
            if Path(row['path']).resolve().parent != root:
                raise ValueError('The inventory escapes its explicit cold root')
    out.mkdir(parents=True)
    summary = dict(schema='held10-five-cold-native-roots-archive-v1', status='running',
                   source=codec.ref(__file__), restoration_source=codec.ref(codec.__file__),
                   plan=codec.ref(plan_path), scientific_bytes_changed=False,
                   large_payloads_in_git=False, reserve_bytes=RESERVE,
                   started_unix_time=time.time(), roots=[])
    summary_path = out / 'summary.json'
    codec.save(summary_path, summary)
    for number, item in enumerate(plan['roots']):
        root = Path(item['root']).resolve()
        dest = out / ('root-%02d' % number)
        dest.mkdir()
        (dest / 'deltas').mkdir()
        base_row = item['base']
        base = original_bytes(base_row)
        base_archive = dest / 'base-static-template.bin.gz'
        write_bytes(base_archive, gzip.compress(base, compresslevel=9, mtime=0))
        manifest = dict(schema=codec.SCHEMA, status='archiving', source=codec.ref(__file__),
                        restoration_source=codec.ref(codec.__file__), plan=codec.ref(plan_path),
                        terminal_summary=item['terminal_summary'], source_root=str(root),
                        construction='direct_complete_raw_bytes_to_lossless_xor',
                        base=dict(codec='gzip_of_complete_raw_template', depends_on_delta=False,
                                  archive=codec.ref(base_archive), original_bytes=len(base),
                                  original_sha256=base_row['sha256'],
                                  original_path=base_row['path'], original_mode=base_row['mode'],
                                  original_mtime_ns=base_row['mtime_ns'],
                                  original_allocated_bytes=base_row['allocated_bytes'],
                                  original_unlinked=False),
                        target_codec='gzip(target_original_bytes XOR complete_template_bytes)',
                        scientific_bytes_changed=False, large_payloads_in_git=False,
                        rows=[], excluded_inputs=item['excluded_inputs'])
        manifest_path = dest / 'manifest.json'
        codec.save(manifest_path, manifest)
        if codec.base_bytes(manifest) != base:
            raise ValueError('Independent complete-base restoration changed bytes')
        for old in item['inputs']:
            raw = original_bytes(old)
            if len(raw) != len(base):
                raise ValueError('Inventoried complete input has another length')
            delta = np.bitwise_xor(np.frombuffer(base, dtype=np.uint8),
                                  np.frombuffer(raw, dtype=np.uint8)).tobytes()
            packed = gzip.compress(delta, compresslevel=9, mtime=0)
            if len(packed) >= len(raw):
                raise ValueError('Proposed archive does not reduce storage')
            source = Path(old['path'])
            target = dest / 'deltas' / (source.name + '.xor.gz')
            write_bytes(target, packed)
            row = dict(relative_path=source.name, original_bytes=len(raw),
                       original_sha256=old['sha256'], original_mode=old['mode'],
                       original_mtime_ns=old['mtime_ns'],
                       original_allocated_bytes=old['allocated_bytes'],
                       delta_archive=codec.ref(target), delta_gzip_bytes=len(packed),
                       delta_allocated_bytes=target.stat().st_blocks * 512,
                       delta_ready=True, all_restored_bytes_equal_original=False,
                       original_unlinked=False)
            if codec.recover(manifest, row) != raw:
                raise ValueError('Independent restoration changed complete original bytes')
            row['all_restored_bytes_equal_original'] = True
            manifest['rows'].append(row)
            codec.save(manifest_path, manifest)
            if original_bytes(old) != raw or codec.base_bytes(manifest) != base:
                raise ValueError('Original or permanent independent base changed before unlink')
            source.unlink()
            row['original_unlinked'] = True
            codec.save(manifest_path, manifest)
            print(json.dumps(dict(event='cold_complete_input_archived', root=str(root),
                                  file=source.name, original_bytes=len(raw),
                                  archive_bytes=len(packed))), flush=True)
        if original_bytes(base_row) != codec.base_bytes(manifest):
            raise ValueError('The complete retained base differs from original template')
        # Permanent archive and complete restoration metadata precede unlink.
        manifest['base']['all_restored_bytes_equal_original'] = True
        codec.save(manifest_path, manifest)
        Path(base_row['path']).unlink()
        manifest['base']['original_unlinked'] = True
        manifest.update(status='complete_frozen_native_raw_xor_archival',
                        completed_unix_time=time.time(),
                        total_original_bytes=len(base) + sum(r['original_bytes'] for r in manifest['rows']),
                        total_archive_bytes=base_archive.stat().st_size + sum(r['delta_gzip_bytes'] for r in manifest['rows']),
                        allocated_bytes_saved=base_row['allocated_bytes'] - base_archive.stat().st_blocks * 512
                            + sum(r['original_allocated_bytes'] - r['delta_allocated_bytes'] for r in manifest['rows']))
        codec.save(manifest_path, manifest)
        summary['roots'].append(dict(manifest=codec.ref(manifest_path), input_count=len(manifest['rows']),
                                     allocated_bytes_saved=manifest['allocated_bytes_saved'],
                                     root=str(root)))
        codec.save(summary_path, summary)
    summary.update(status='complete_frozen_five_root_lossless_archival',
                   completed_unix_time=time.time(),
                   allocated_bytes_saved=sum(x['allocated_bytes_saved'] for x in summary['roots']),
                   free_bytes_after=shutil.disk_usage(out).free)
    codec.save(summary_path, summary)
    print(json.dumps(dict(event='cold_native_archival_complete', summary=codec.ref(summary_path),
                          allocated_bytes_saved=summary['allocated_bytes_saved'],
                          free_bytes=summary['free_bytes_after'])), flush=True)


def restore(args):
    manifest = json.loads(args.manifest.resolve().read_text())
    if args.relative_path != 'static-template.bin':
        codec.restore(args)
        return
    row = manifest['base']
    raw = codec.base_bytes(manifest)
    root = Path(manifest['source_root']).resolve()
    target = root / 'static-template.bin'
    if str(target) != row['original_path']:
        raise ValueError('Original base path differs from manifest root')
    if not args.verify_only:
        if target.exists():
            if target.read_bytes() != raw:
                raise ValueError('Refusing to replace another template')
        else:
            guard(root, len(raw))
            temporary = target.with_name(target.name + '.restore-' + str(os.getpid()))
            write_bytes(temporary, raw)
            os.chmod(temporary, row['original_mode'])
            os.utime(temporary, ns=(row['original_mtime_ns'], row['original_mtime_ns']))
            os.link(temporary, target)
            temporary.unlink()
    print(json.dumps(dict(status='complete_original_bytes_verified' if args.verify_only
                         else 'complete_original_bytes_restored', original_path=str(target),
                          bytes=len(raw), sha256=codec.sha(raw))), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    a = sub.add_parser('archive')
    a.add_argument('--plan', type=Path, required=True)
    a.add_argument('--outdir', type=Path, required=True)
    r = sub.add_parser('restore')
    r.add_argument('--manifest', type=Path, required=True)
    r.add_argument('--relative-path', required=True)
    r.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    archive(args) if args.command == 'archive' else restore(args)


if __name__ == '__main__':
    main()
