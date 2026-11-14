#!/usr/bin/env python3
"""Relocate the complete immutable nineteen-field arrays without losing bytes.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Root explicitly authorized this scratch-only relocation. Every case must have
an owned zero exit. Full original SHA/bytes/recipes are journaled before any
replacement. Each destination is copied, fsynced and SHA-checked before the
original private path is atomically replaced by a symlink. Existing identical
completed links can be recovered. No Git file, active writer, accepted/raw
input, source, certificate, or mathematical value is modified.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import stat
import time

ROOT = Path('/workspace/scratch/d1aa462cfc02/geometry-work')
PLAN_SHA = '56715b1a962a10412d2913b4187ddcf33baac85ed0f2bd33f189b3fd95855c66'
READER_SHA = 'abf93e019ce9583872de8b3de1205f42864fe69b279594499c178c3034edbbf5'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def atomic_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.tmp-'+str(os.getpid()))
    payload = (json.dumps(value, indent=2)+'\n').encode()
    with temporary.open('xb') as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def free_bytes(path):
    value = os.statvfs(path)
    return value.f_bavail*value.f_frsize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('plan', 'reader', 'reader-resource', 'destination', 'inventory', 'receipt', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if Path.cwd() != ROOT or args.out.exists() or args.receipt.exists():
        raise ValueError('Use the original private cwd and fresh receipts/output')
    if not str(args.destination).startswith('/dev/shm/visible-flex-geometry-readonly-relocation/'):
        raise ValueError('Only the explicit private RAM relocation namespace is permitted')
    plan = read(args.plan)
    reader = read(args.reader)
    reader_owned = read(args.reader_resource)
    if (sha(args.plan) != PLAN_SHA or not reader['all_identity_gates']
            or reader['plan_sha256'] != PLAN_SHA or reader['total_fields'] != 19
            or reader['total_chunks'] != 342 or not reader_owned['wait4_observed']
            or reader_owned['exitcode'] != 0 or reader_owned['termination_signal'] is not None):
        raise ValueError('The complete original nineteen-field owned reader is required')
    sources = []
    fields = []
    metadata = []
    for case in plan['candidates']:
        report_path = ROOT/case['report']
        field_path = ROOT/case['field']
        resource_path = ROOT/case['resource']
        report = read(report_path)
        manifest = read(field_path)
        owned = read(resource_path)
        if (not report['finished'] or not report['finite_domain_passed']
                or report['geometry_fields']['sha256'] != sha(field_path)
                or not owned['wait4_observed'] or owned['exitcode'] != 0
                or owned['termination_signal'] is not None):
            raise ValueError('Only formally completed read-only field cases may move: '+case['name'])
        storage = report['geometry_fields']['storage']
        if not storage['complete'] or storage['shape'] != [3767, 768, 3] or len(storage['chunks']) != 18:
            raise ValueError('The full original common field storage is required')
        cursor = 0
        for part in storage['chunks']:
            source = field_path.parent/part['file']
            if (source.parent != ROOT/'m32-q126-r1' or Path(part['file']).name != part['file']
                    or part['start'] != cursor or not part['start'] < part['end'] <= 3767):
                raise ValueError('Unexpected field location or chunk coverage')
            cursor = part['end']
            destination = args.destination/part['file']
            if source.stat().st_size != part['bytes'] or sha(source) != part['sha256']:
                raise ValueError('A complete original field chunk changed: '+str(source))
            if source.is_symlink() and source.resolve() != destination:
                raise ValueError('An existing private link points elsewhere')
            item = dict(case=case['name'], original_path=str(source), destination_path=str(destination),
                        sha256=part['sha256'], bytes=part['bytes'],
                        original_allocated_bytes=source.stat().st_blocks*512,
                        original_link_count=source.stat().st_nlink,
                        already_relocated=source.is_symlink(), start=part['start'], end=part['end'])
            sources.append(item)
        if cursor != 3767:
            raise ValueError('Incomplete actual radial coverage')
        fields.append(dict(name=case['name'], original_command=case['command'],
                           report=str(report_path), report_sha256=sha(report_path),
                           field_manifest=str(field_path), field_sha256=sha(field_path),
                           owned_resource=str(resource_path), resource_sha256=sha(resource_path),
                           all_original_input_and_source_hashes=report['source_sha256']))
        metadata.extend(dict(path=str(path), sha256=sha(path)) for path in (report_path, field_path, resource_path))
    if len(sources) != 342 or len({row['original_path'] for row in sources}) != 342:
        raise ValueError('Exactly the original 342 unique field chunks are required')
    total = sum(row['bytes'] for row in sources)
    if total != reader['total_compressed_derived_array_bytes']:
        raise ValueError('Original complete reader byte sum changed')
    args.destination.mkdir(parents=True, exist_ok=True)
    remaining = sum(row['bytes'] for row in sources if not Path(row['destination_path']).exists())
    if free_bytes(args.destination) < remaining+256*1024**2:
        raise OSError('The authorized RAM destination lacks the full byte count and reserve')
    input_ids = {str(path): sha(path) for path in (args.plan, args.reader, args.reader_resource)}
    inventory = dict(schema='current19-readonly-array-relocation-inventory-v1',
                     author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
                     input_sha256=input_ids, fields=fields, files=sources,
                     files_count=len(sources), total_original_bytes=total,
                     original_metadata_unchanged=metadata,
                     destination_root=str(args.destination),
                     authority='Root explicit scratch relocation instruction; preserve all actual bytes and reader paths.',
                     recovery='Each original path resolves to the exact SHA below. If RAM storage is lost, reproduce its case using the preserved original command and full source/input hashes; do not label a regenerated field completed without original gates and owned exit zero.')
    if args.inventory.exists():
        old = read(args.inventory)
        if (old['input_sha256'] != input_ids
                or [(x['original_path'],x['destination_path'],x['sha256'],x['bytes']) for x in old['files']]
                != [(x['original_path'],x['destination_path'],x['sha256'],x['bytes']) for x in sources]):
            raise ValueError('The retained relocation inventory is incompatible')
    else:
        atomic_json(args.inventory, inventory)
    before = dict(workspace_free=free_bytes(ROOT), destination_free=free_bytes(args.destination))
    moved = 0
    recovered = 0
    with args.receipt.open('x') as journal:
        for index, row in enumerate(sources):
            source = Path(row['original_path'])
            destination = Path(row['destination_path'])
            if destination.exists():
                if destination.stat().st_size != row['bytes'] or sha(destination) != row['sha256']:
                    raise ValueError('An existing destination does not preserve the full actual bytes')
            else:
                temporary = destination.with_name(destination.name+'.copy-'+str(os.getpid()))
                with source.open('rb') as src, temporary.open('xb') as dst:
                    shutil.copyfileobj(src, dst, length=1024*1024)
                    dst.flush()
                    os.fsync(dst.fileno())
                if temporary.stat().st_size != row['bytes'] or sha(temporary) != row['sha256']:
                    raise ValueError('Copied complete array failed exact SHA/bytes verification')
                temporary.chmod(0o444)
                os.replace(temporary, destination)
            if source.is_symlink():
                if source.resolve() != destination:
                    raise ValueError('Unexpected original symlink identity')
                recovered += 1
            else:
                if not stat.S_ISREG(source.stat().st_mode) or sha(source) != row['sha256']:
                    raise ValueError('Original array changed before atomic private-path replacement')
                link = source.with_name(source.name+'.relocation-link-'+str(os.getpid()))
                os.symlink(destination, link)
                os.replace(link, source)
                moved += 1
            if (source.resolve() != destination or source.stat().st_size != row['bytes']
                    or sha(source) != row['sha256']):
                raise ValueError('Original reader path no longer sees the complete exact array')
            journal.write(json.dumps(dict(index=index, **row, copied_and_original_reader_sha_verified=True))+'\n')
            journal.flush()
            os.fsync(journal.fileno())
            if (index+1)%36 == 0:
                print(json.dumps(dict(event='complete_array_readonly_relocation', files=index+1,
                                      workspace_free=free_bytes(ROOT))), flush=True)
    for item in metadata:
        if sha(item['path']) != item['sha256']:
            raise ValueError('An original scientific metadata file changed')
    result = dict(schema='current19-complete-readonly-array-relocation-result-v1',
                  author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
                  inventory_path=str(args.inventory), inventory_sha256=sha(args.inventory),
                  receipt_path=str(args.receipt), receipt_sha256=sha(args.receipt),
                  input_sha256=input_ids, original_cases=19, complete_chunks=342,
                  total_bytes_preserved=total, newly_replaced_private_paths=moved,
                  recovered_already_verified_links=recovered,
                  original_allocated_bytes_for_new_links=sum(row['original_allocated_bytes'] for row in sources if not row['already_relocated']),
                  every_original_reader_path_bytes_and_SHA_unchanged=True,
                  all_owned_completed_cases=True, original_metadata_hashes_unchanged=True,
                  full_raw_accepted_source_certificates_and_current_BVP_untouched=True,
                  free_bytes_before=before,
                  free_bytes_after=dict(workspace_free=free_bytes(ROOT), destination_free=free_bytes(args.destination)),
                  no_scientific_bytes_discarded=True, new_ODE_or_geometry_or_LP_calls=0,
                  elapsed_seconds=time.monotonic()-started,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    atomic_json(args.out, result)
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out), moved=moved,
                         files=342, bytes_preserved=total, free=result['free_bytes_after'])), flush=True)


if __name__ == '__main__':
    main()
