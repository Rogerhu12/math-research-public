#!/usr/bin/env python3
"""Request91 byte-only transport: complete actual83 or one original73 J chunk.

The original standard-library HTTPS, cross-origin Authorization stripping,
metadata, complete ZIP SHA/size, safe publication and cleanup kernel is unchanged.
Original73 selection preserves just the single exact raw stage8..11 J chunk;
unselected payloads are not inflated or claimed independently CRC checked.
"""
from __future__ import annotations
import argparse
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

KERNEL_NAME='exact_20261114_fetch_pinned_public_artifact.py'
KERNEL_SHA='51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859'
REPOSITORY='Rogerhu12/math-research-public'
PINS={
 'actual83':dict(run_id=43668743706,artifact_id=14143009723,
  artifact_name='visible-mainline-modelresponse-43668743706-1',expected_size=48375172,
  expected_sha256='9eadec9633a1260597268a760b5870bf59bd18ef808e8c5eb6ac5e006df5634c'),
 'original73-j-chunk':dict(run_id=43657001633,artifact_id=14141540502,
  artifact_name='visible-mainline-nojprimalnative-43657001633-1',expected_size=1752742419,
  expected_sha256='3430597bc72c02c387b62fd908b229c87c7caa01d4d14e2599c66f834480eef9'),
}
SOURCES={'actual83':'8d199eda5c1f1df162ded244e8dfd012e0c8d127',
 'original73-j-chunk':'9515d5aaf7c68f8efd366438d6bd81ce73c3486f'}
SCHEMAS={'actual83':'pinned-public-actual83-complete-four-row-input-fetch-v1',
 'original73-j-chunk':'pinned-public-actual73-one-original-J-chunk-fetch-v1'}
CHUNK_PATH='native-noj-primal-current576-damped/iteration-002/snapshot/large-arrays/stage-jacobians-0002.f64le'
CHUNK_SHA='fd117e2d3cfdd26ddfa584e5c75e521209f12ca16f098596ec61cab3e47f8677'
CHUNK_BYTES=1605632


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

        extract(CHUNK_PATH, CHUNK_SHA, CHUNK_BYTES,
                'the exact original stage8..11 raw J chunk, later cross-bound to actual83 input-binding')
    return dict(zip_member_count=len(infos), original_archive_file_count=original_files,
        file_count=len(files), directory_count=len(directories),
        total_extracted_bytes=sum(row['bytes'] for row in files), files=files,
        directories=sorted(directories), original_stage_start=8, original_stage_stop=12,
        original_chunk_index=2, original_chunk_sha256=CHUNK_SHA,
        original_chunk_shape=[4,224,224], original_chunk_order='C', original_chunk_dtype='<f8',
        zip_paths_checked_before_any_extraction=True,
        traversal_symlinks_special_files_duplicates_and_encryption_rejected=True,
        per_file_size_CRC_and_SHA256_verified=True,
        per_file_verification_scope='Only the single extraction.files member; the complete original ZIP size/SHA was verified first',
        all_original_payloads_extracted=False,
        unselected_original_file_count=original_files-len(files),
        unselected_original_payloads_inflated_or_CRC_checked=False,
        original_scientific_modules_imported=False, scientific_computation_performed=False)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',required=True,choices=tuple(PINS))
    parser.add_argument('--out',required=True,type=Path)
    args=parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!=REPOSITORY:
        raise RuntimeError('Run only in this public repository Actions')
    kernel_path=Path(__file__).resolve().with_name(KERNEL_NAME)
    if hashlib.sha256(kernel_path.read_bytes()).hexdigest()!=KERNEL_SHA:
        raise RuntimeError('The frozen public artifact transport kernel changed')
    spec=importlib.util.spec_from_file_location('_request91_original_transport_kernel',kernel_path)
    kernel=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=kernel
    spec.loader.exec_module(kernel)
    if kernel.REPOSITORY!=REPOSITORY or kernel.SCHEMA!='pinned-public-actions-artifact-fetch-v3':
        raise RuntimeError('The original standard-library transport interface changed')
    old_read_metadata,old_public_metadata=kernel.read_metadata,kernel.public_metadata
    chosen=dict(PINS[args.input])
    identity=dict(schema='request91-two-actual-artifact-input-transport-v1',
        source_file=Path(__file__).name,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        kernel_source_file=KERNEL_NAME,kernel_source_sha256=KERNEL_SHA,input_kind=args.input,
        actual_pin=chosen,original_source_commit=SOURCES[args.input],
        overridden_names=['PIN','SCHEMA','read_metadata','public_metadata']+
          (['extract_verified_archive'] if args.input=='original73-j-chunk' else []),
        kernel_network_and_final_publication_unchanged=True,
        selected_extraction_only=args.input=='original73-j-chunk',
        adapter_does_not_read_credentials=True,scientific_computation_performed=False)
    def read_metadata(opener,token):
        metadata,canonical=old_read_metadata(opener,token)
        if metadata.get('workflow_run',{}).get('head_sha')!=SOURCES[args.input]:
            kernel.fail('ACTUAL_SOURCE_COMMIT','The original public artifact source commit differs.')
        return metadata,canonical
    def public_metadata(metadata):
        value=old_public_metadata(metadata)
        value['local_request91_input_transport']=identity
        return value
    kernel.PIN=chosen
    kernel.SCHEMA=SCHEMAS[args.input]
    kernel.read_metadata=read_metadata
    kernel.public_metadata=public_metadata
    if args.input=='original73-j-chunk':
        kernel.extract_verified_archive=lambda archive,payload:selected_extractor(kernel,archive,payload)
    sys.argv=[str(kernel_path),'--run-id',str(chosen['run_id']),
        '--artifact-id',str(chosen['artifact_id']),'--artifact-name',chosen['artifact_name'],
        '--expected-size',str(chosen['expected_size']),'--expected-sha256',chosen['expected_sha256'],
        '--out',str(args.out)]
    try:
        return kernel.main()
    except (KeyboardInterrupt,SystemExit):
        raise
    except Exception:
        kernel.public_event('request91_input_transport_failed',success=False,
            error_code='REQUEST91_INPUT_ADAPTER_FAILURE',
            message='Pinned original input transport failed; no credential or URL is logged.')
        return 2


if __name__=='__main__':
    raise SystemExit(main())
