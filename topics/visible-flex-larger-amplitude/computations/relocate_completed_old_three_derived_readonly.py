#!/usr/bin/env python3
"""Preserve 88 completed old derived chunks while relocating them to private RAM.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Root explicitly authorized this storage-only relocation. Original scientific
metadata, accepted/raw files and current A nineteen fields are untouched.
All inventory and per-file receipts are durably written in RAM before/after
each atomic replacement. No mathematical computation is repeated.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import stat
import time

GW = Path('/workspace/scratch/d1aa462cfc02/geometry-work')
DEST = Path('/dev/shm/visible-flex-geometry-readonly-relocation/old-three-20261113')
BOOK = DEST/'bookkeeping'

def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()

def read(p):
    return json.loads(Path(p).read_text())

def save(p, d):
    t = p.with_name(p.name+'.tmp-'+str(os.getpid()))
    with t.open('x') as f:
        json.dump(d, f, indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())
    os.replace(t, p)

def free(p):
    d = os.statvfs(p)
    return d.f_bavail*d.f_frsize

def main():
    start = time.monotonic()
    if Path.cwd() != GW or (BOOK/'result.json').exists() or (BOOK/'receipt.jsonl').exists():
        raise ValueError('Use the fixed private cwd and fresh result/receipt')
    rows, groups, identities = [], [], []
    for kind, directory, manifest_name, resource_name, count in (
        ('geometry', 'm28-q122-r1', 'q130-t256-constant-size-combined-field.json', 'q130-t256-constant-size-combined-resource.json', 18),
        ('packet', 'q106-newg-packet-r1', 'packet-manifest.json', 'resource.json', 35),
        ('packet', 'q098-newg-packet-r1', 'packet-manifest.json', 'resource.json', 35)):
        folder = GW/directory
        mp, rp = folder/manifest_name, folder/resource_name
        manifest, owned = read(mp), read(rp)
        if owned['exitcode'] != 0 or owned['termination_signal'] is not None:
            raise ValueError('Only original formally completed cases may move')
        meta = [mp, rp]
        if kind == 'geometry':
            screen = folder/'q130-t256-constant-size-combined-screen.json'
            outer = folder/'q130-t256-constant-size-owned-resource.json'
            report, outer_owned = read(screen), read(outer)
            if (not manifest['complete'] or not report['finished']
                    or report['geometry_fields']['sha256'] != sha(mp)
                    or outer_owned['exitcode'] != 0 or not outer_owned['wait4_observed']):
                raise ValueError('The original complete negative warm/owned report is required')
            parts = manifest['chunks']
            cursor = 0
            for p in parts:
                if p['start'] != cursor or p['end'] <= cursor:
                    raise ValueError('Geometry coverage changed')
                cursor = p['end']
            if cursor != manifest['shape'][0]:
                raise ValueError('Geometry radial coverage is incomplete')
            meta += [screen, outer, folder/'q130-t256-constant-size-plan.json']
            input_sources = report['source_sha256']
        else:
            if (not manifest['finished'] or not manifest['all_original_intervals_covered']
                    or not manifest['all_radial_state_jets_exactly_enclosed']):
                raise ValueError('The complete original radial packet is required')
            parts = manifest['radial_chunks']
            input_sources = manifest['source_and_input_sha256']
        if len(parts) != count:
            raise ValueError('Unexpected chunk count')
        for n, part in enumerate(parts):
            if kind == 'geometry':
                name = 'q130-t256-constant-size-combined-field-part%03d.npy.gz' % n
                if part['file'] != name:
                    raise ValueError('Unexpected geometry derived filename')
                source = folder/name
            else:
                name = 'packet-radial%03d.json.gz' % n
                if part['path'] != directory+'/'+name:
                    raise ValueError('Unexpected packet derived filename')
                source = GW/part['path']
            target = DEST/directory/name
            st = source.stat()
            if not stat.S_ISREG(st.st_mode) or st.st_size != part['bytes'] or sha(source) != part['sha256']:
                raise ValueError('Original derived bytes changed: '+str(source))
            if source.is_symlink() and source.resolve() != target:
                raise ValueError('A pre-existing link resolves outside this relocation')
            rows.append(dict(original_path=str(source), destination_path=str(target),
                             bytes=part['bytes'], sha256=part['sha256'], group=directory,
                             original_allocated_bytes=st.st_blocks*512,
                             original_link_count=st.st_nlink, already_relocated=source.is_symlink()))
        meta_ids = [dict(path=str(p), sha256=sha(p)) for p in meta]
        identities.extend(meta_ids)
        groups.append(dict(group=directory, original_command=owned['command'],
                           original_resource_schema=sorted(owned), original_resource_exitcode=0,
                           original_wait4_observed_field=owned.get('wait4_observed'),
                           original_source_and_input_hashes=input_sources, metadata=meta_ids))
    total = sum(r['bytes'] for r in rows)
    if len(rows) != 88 or total != 72377249 or len({r['original_path'] for r in rows}) != 88:
        raise ValueError('The exact authorized three-case inventory changed')
    if free(DEST) < total+256*1024**2:
        raise OSError('Insufficient private RAM storage and reserve')
    inventory = dict(schema='completed-old-three-readonly-relocation-inventory-v1',
                     author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
                     authority='Root explicit old completed q106/q098/m28 derived RAM relocation instruction.',
                     files=rows, groups=groups, total_files=len(rows), total_bytes=total,
                     recovery='Original paths retain exact bytes through symlinks. If RAM is lost, regenerate only with the preserved original command/source/input hashes and original scientific gates; no unobserved rerun is completed.')
    save(BOOK/'inventory.json', inventory)
    before = dict(workspace=free(GW), ram=free(DEST))
    moved = 0
    with (BOOK/'receipt.jsonl').open('x') as journal:
        for index, row in enumerate(rows):
            source, target = Path(row['original_path']), Path(row['destination_path'])
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                if target.stat().st_size != row['bytes'] or sha(target) != row['sha256']:
                    raise ValueError('Existing destination differs')
            else:
                tmp = target.with_name(target.name+'.copy-'+str(os.getpid()))
                with source.open('rb') as src, tmp.open('xb') as dst:
                    shutil.copyfileobj(src, dst, 1024*1024)
                    dst.flush(); os.fsync(dst.fileno())
                if tmp.stat().st_size != row['bytes'] or sha(tmp) != row['sha256']:
                    raise ValueError('Complete destination copy differs')
                tmp.chmod(0o444); os.replace(tmp, target)
            if not source.is_symlink():
                if sha(source) != row['sha256']:
                    raise ValueError('Original changed before replacement')
                link = source.with_name(source.name+'.relocation-'+str(os.getpid()))
                os.symlink(target, link); os.replace(link, source); moved += 1
            if source.resolve() != target or source.stat().st_size != row['bytes'] or sha(source) != row['sha256']:
                raise ValueError('Original reader path no longer preserves exact bytes')
            journal.write(json.dumps(dict(index=index, **row, full_SHA_readback_through_original_path=True))+'\n')
            journal.flush(); os.fsync(journal.fileno())
    for d in identities:
        if sha(d['path']) != d['sha256']:
            raise ValueError('Original scientific metadata changed')
    result = dict(schema='completed-old-three-readonly-relocation-result-v1', finished=True,
                  source_sha256=sha(__file__), inventory_sha256=sha(BOOK/'inventory.json'),
                  receipt_sha256=sha(BOOK/'receipt.jsonl'), files=88, bytes_preserved=total,
                  newly_replaced_paths=moved,
                  originally_allocated_bytes_for_new_links=sum(r['original_allocated_bytes'] for r in rows if not r['already_relocated']),
                  all_original_paths_full_SHA_equal=True, original_metadata_SHA_unchanged=True,
                  accepted_raw_certificates_current_A19_and_BVP_untouched=True,
                  no_scientific_bytes_discarded=True, scientific_recomputations=0,
                  free_before=before, free_after=dict(workspace=free(GW), ram=free(DEST)),
                  elapsed_seconds=time.monotonic()-start,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    save(BOOK/'result.json', result)
    print(json.dumps(dict(result=str(BOOK/'result.json'), result_sha256=sha(BOOK/'result.json'),
                          moved=moved, bytes=total, free_after=result['free_after'])), flush=True)

if __name__ == '__main__':
    main()
