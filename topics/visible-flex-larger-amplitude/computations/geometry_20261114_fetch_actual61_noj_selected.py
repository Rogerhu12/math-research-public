#!/usr/bin/env python3
"""Byte-only selected actual61 input transport for the single no-J probe.

The frozen transport still validates the complete original ZIP and public
metadata. This independent extractor inflates only twelve native records,
the final fresh snapshot metadata and its nine non-J input arrays. No
scientific packages, original numerical modules or native processes run.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile
import zlib

KERNEL_NAME = 'exact_20261114_fetch_pinned_public_artifact.py'
KERNEL_SHA = '51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859'
REPOSITORY = 'Rogerhu12/math-research-public'
SOURCE_COMMIT = 'cf6b51193255dfc713610d2919598451ccdd49e2'
PIN = dict(run_id=43645948199, artifact_id=14136633570,
    artifact_name='visible-mainline-current576native-43645948199-1',
    expected_size=2335870174,
    expected_sha256='7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469')
NATIVE = 'native-current576-damped'
SNAPSHOT = NATIVE+'/iteration-003/snapshot'
RESULT_SHA = 'b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef'
SNAPSHOT_SHA = '5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286'
STATE_SHA = 'b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013'
NATIVE_NAMES = (
    'current-correction-summary.json', 'current-input-config.json', 'native_runtime-config.json',
    'native_intent.json', 'native_ready.json.gz', 'native_capacity.json',
    'original-live-identity-before-selected-seed.json', 'actual-current-method-identities.json',
    'core-instrumentation.json', 'native_trace.jsonl', 'native_trials.jsonl',
)
ARRAY_SHAPES = {
    'base-states': [577,224], 'stage-residuals': [576,224], 'stage-out': [576,224],
    'original-scales': [1,577], 'cut-residual': [1,112], 'end-residual': [1,112],
    'original-far-graph': [1,112], 'physical-height': [1,112], 'cut-target': [1,112],
}
SCHEMA = 'pinned-public-actual61-final-snapshot-noJ-selected-fetch-v1'


def selected_extractor(kernel, archive_path, payload):
    """Full ZIP has already passed SHA; preserve only descriptor-bound bytes."""
    files, directories, selected, members = [], set(), {}, {}
    with zipfile.ZipFile(archive_path, 'r') as archive:
        infos = archive.infolist()
        original_files = 0
        for info in infos:
            name, parts, is_directory = kernel.safe_member_name(info)
            if name in members:
                kernel.fail('ZIP_DUPLICATE_PATH', 'The original central directory contains duplicate paths.')
            members[name] = (info, parts, is_directory)
            original_files += int(not is_directory)
        for name, (info, parts, is_directory) in members.items():
            for level in range(1, len(parts)):
                ancestor = '/'.join(parts[:level])
                if ancestor in members and not members[ancestor][2]:
                    kernel.fail('ZIP_PARENT_IS_FILE', 'An original ZIP file is used as a parent directory.')

        def member_path(root, item):
            name = item.get('file')
            rel = PurePosixPath(name) if isinstance(name, str) else None
            if (rel is None or rel.is_absolute() or '..' in rel.parts
                    or not rel.parts or str(rel) != name or '\\' in name
                    or type(item.get('bytes')) is not int or item['bytes'] < 0
                    or not isinstance(item.get('sha256'), str)
                    or not re.fullmatch(r'[0-9a-f]{64}', item['sha256'])):
                kernel.fail('SELECTED_DESCRIPTOR', 'A complete relative original descriptor is required.')
            return root+'/'+name

        def extract(name, expected_sha, expected_bytes=None, reason='descriptor-bound original'):
            if name in selected:
                row = selected[name]
                if row['sha256'] != expected_sha or (expected_bytes is not None and row['bytes'] != expected_bytes):
                    kernel.fail('SELECTED_DUPLICATE_IDENTITY', 'Repeated evidence has conflicting byte descriptors.')
                return payload/name
            if name not in members or members[name][2]:
                kernel.fail('SELECTED_MEMBER_MISSING', 'A required original selected member is missing.')
            info, parts, _ = members[name]
            if expected_bytes is not None and info.file_size != expected_bytes:
                kernel.fail('SELECTED_MEMBER_SIZE', 'A selected member differs from its original descriptor length.')
            for level in range(1, len(parts)):
                parent = '/'.join(parts[:level])
                (payload/parent).mkdir(mode=0o700, parents=True, exist_ok=True)
                directories.add(parent)
            destination = payload.joinpath(*parts)
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0)
            fd = os.open(destination, flags, 0o600)
            count, crc, digest = 0, 0, hashlib.sha256()
            with os.fdopen(fd, 'wb') as out, archive.open(info, 'r') as stream:
                for block in iter(lambda: stream.read(kernel.CHUNK), b''):
                    count += len(block)
                    if count > info.file_size:
                        kernel.fail('SELECTED_MEMBER_OVERSIZE', 'A selected payload exceeded its declared size.')
                    out.write(block)
                    digest.update(block)
                    crc = zlib.crc32(block, crc)
                out.flush()
                os.fsync(out.fileno())
            if count != info.file_size or (crc & 0xffffffff) != info.CRC or digest.hexdigest() != expected_sha:
                kernel.fail('SELECTED_MEMBER_BYTES', 'A selected payload failed its original CRC/SHA256/size.')
            row = dict(path=name, bytes=count, sha256=digest.hexdigest(),
                crc32=f'{crc & 0xffffffff:08x}', final_mode='0444', symlink=False,
                selected_because=reason)
            files.append(row)
            selected[name] = row
            return destination

        def by_descriptor(root, item, reason):
            return extract(member_path(root, item), item['sha256'], item['bytes'], reason)

        def parse(path):
            raw = path.read_bytes()
            if raw[:2] == b'\x1f\x8b':
                raw = gzip.decompress(raw)
            return json.loads(raw)

        result_path = extract(NATIVE+'/result.json', RESULT_SHA, 6891, 'fixed actual61 original native result')
        native_result = parse(result_path)
        inventory = {row['file']: row for row in native_result['small_output_files']}
        if len(inventory) != len(native_result['small_output_files']):
            kernel.fail('NATIVE_INVENTORY_DUPLICATES', 'The original native result inventory must be unique.')
        for name in NATIVE_NAMES:
            by_descriptor(NATIVE, inventory[name], 'one of eleven actual61 native supporting records')
        summary = parse(payload/NATIVE/'current-correction-summary.json')
        current = summary['iterations'][3]
        if (current['native_call'], current['nonlinear_iteration'], current['snapshot_sequence'],
                current['current_state_sha256'], current['snapshot']['sha256']) != (1,3,3,STATE_SHA,SNAPSHOT_SHA):
            kernel.fail('ACTUAL_FINAL_SNAPSHOT', 'The selection is fixed to actual61 final fresh-withJ state.')
        snapshot_path = extract(SNAPSHOT+'/result.json', SNAPSHOT_SHA, current['snapshot']['bytes'],
            'fixed final fresh-withJ snapshot result')
        snapshot = parse(snapshot_path)
        manifest_path = by_descriptor(SNAPSHOT, snapshot['manifest'], 'complete original manifest descriptors')
        context_path = by_descriptor(SNAPSHOT, snapshot['context'], 'complete original current context')
        manifest, context = parse(manifest_path), parse(context_path)
        for key in ('core_instrumentation', 'flow_return_metadata'):
            by_descriptor(SNAPSHOT, context[key], 'original snapshot '+key)
        entries = {row['name']: row for row in manifest['arrays']}
        if len(entries) != len(manifest['arrays']) or set(entries) != set(ARRAY_SHAPES)|{'stage-jacobians'}:
            kernel.fail('SNAPSHOT_ARRAY_INVENTORY', 'The complete original descriptor inventory differs.')
        array_receipts = []
        for name, shape in ARRAY_SHAPES.items():
            entry = entries[name]
            if (entry['shape'] != shape or entry['dtype'] != '<f8' or entry['order'] != 'C'
                    or entry['completed'] is not True):
                kernel.fail('SNAPSHOT_ARRAY_DESCRIPTOR', 'A selected original array descriptor differs.')
            raw_hash, byte_count, row, width = hashlib.sha256(), 0, 0, 8
            for n in shape[1:]:
                width *= n
            for index, item in enumerate(entry['chunks']):
                if (item['array'] != name or item['chunk_index'] != index or item['row_start'] != row
                        or type(item['row_stop']) is not int or not row < item['row_stop'] <= shape[0]
                        or item['bytes'] != (item['row_stop']-row)*width
                        or item['raw_sha256'] != item['sha256']):
                    kernel.fail('SNAPSHOT_CHUNK_DESCRIPTOR', 'Exact raw binary chunk coverage is required.')
                path = by_descriptor(SNAPSHOT, item, 'complete selected non-J array '+name)
                with path.open('rb') as stream:
                    for block in iter(lambda: stream.read(kernel.CHUNK), b''):
                        raw_hash.update(block)
                        byte_count += len(block)
                row = item['row_stop']
            if (row != shape[0] or byte_count != entry['total_bytes']
                    or raw_hash.hexdigest() != entry['raw_sha256']
                    or entry['raw_sha256'] != context['raw_array_sha256'][name]):
                kernel.fail('SNAPSHOT_ARRAY_RAW_IDENTITY', 'A selected complete original raw array differs.')
            array_receipts.append(dict(name=name, shape=shape, bytes=byte_count, raw_sha256=raw_hash.hexdigest(),
                chunks=len(entry['chunks'])))
        if entries['base-states']['raw_sha256'] != STATE_SHA:
            kernel.fail('CURRENT_STATE_IDENTITY', 'The exact final current raw state differs.')
        descriptor_only = entries['stage-jacobians']['raw_sha256']
        if descriptor_only != context['raw_array_sha256']['stage-jacobians']:
            kernel.fail('SAVED_J_DESCRIPTOR_IDENTITY', 'Saved J descriptor identity differs.')
    return dict(zip_member_count=len(infos), original_archive_file_count=original_files,
        file_count=len(files), directory_count=len(directories), total_extracted_bytes=sum(row['bytes'] for row in files),
        files=files, directories=sorted(directories), selected_complete_raw_arrays=array_receipts,
        native_result_sha256=RESULT_SHA, snapshot_result_sha256=SNAPSHOT_SHA, current_state_sha256=STATE_SHA,
        saved_J_descriptor_sha256=descriptor_only, saved_J_payloads_extracted=False,
        selected_native_root_files=12, selected_snapshot_metadata_files=5,
        zip_paths_checked_before_any_extraction=True,
        traversal_symlinks_special_files_duplicates_and_encryption_rejected=True,
        per_file_size_CRC_and_SHA256_verified=True,
        per_file_verification_scope='Only extraction.files; nine complete raw array streams also checked',
        all_original_payloads_extracted=False, unselected_original_file_count=original_files-len(files),
        unselected_original_payloads_inflated_or_CRC_checked=False,
        original_scientific_modules_imported=False, scientific_computation_performed=False)


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise RuntimeError('Run only in this public repository Actions')
    kernel_path = Path(__file__).resolve().with_name(KERNEL_NAME)
    if hashlib.sha256(kernel_path.read_bytes()).hexdigest() != KERNEL_SHA:
        raise RuntimeError('The frozen public artifact transport kernel changed')
    spec = importlib.util.spec_from_file_location('_actual61_selected_transport_kernel', kernel_path)
    kernel = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = kernel
    spec.loader.exec_module(kernel)
    if kernel.REPOSITORY != REPOSITORY or kernel.SCHEMA != 'pinned-public-actions-artifact-fetch-v3':
        raise RuntimeError('The original standard-library transport interface changed')
    old_read_metadata, old_public_metadata = kernel.read_metadata, kernel.public_metadata
    identity = dict(schema='actual61-noJ-selected-transport-adapter-v1',
        source_file=Path(__file__).name, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        kernel_source_file=KERNEL_NAME, kernel_source_sha256=KERNEL_SHA,
        actual_pin=PIN, original_source_commit=SOURCE_COMMIT,
        overridden_names=['PIN','SCHEMA','read_metadata','public_metadata','extract_verified_archive'],
        kernel_network_and_final_publication_unchanged=True, selected_extraction_only=True,
        adapter_does_not_read_credentials=True, scientific_computation_performed=False)

    def read_metadata(opener, token):
        metadata, canonical = old_read_metadata(opener, token)
        if metadata.get('workflow_run',{}).get('head_sha') != SOURCE_COMMIT:
            kernel.fail('ACTUAL_SOURCE_COMMIT', 'The original public artifact source commit differs.')
        return metadata, canonical

    def public_metadata(metadata):
        value = old_public_metadata(metadata)
        value['local_selected_transport_adapter'] = identity
        return value

    kernel.PIN = dict(PIN)
    kernel.SCHEMA = SCHEMA
    kernel.read_metadata = read_metadata
    kernel.public_metadata = public_metadata
    kernel.extract_verified_archive = lambda archive, payload: selected_extractor(kernel, archive, payload)
    try:
        return kernel.main()
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        # Do not print exception objects that might contain a signed URL.
        kernel.public_event('actual61_selected_transport_failed', success=False,
            error_code='SELECTED_ADAPTER_FAILURE', message='Selected original evidence extraction failed; no credential or URL is logged.')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
