#!/usr/bin/env python3
"""Stream a completed offline piecewise normal into a lossless gzip capsule.

No normal, field, matrix, pickle, objective, or solver is loaded.  The
original normal manifest is stored byte-for-byte. Restore recreates its
declared directory name and writes manifest.json last; mathematical binding
validation remains the job of the unchanged original normal loader.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import time
import uuid


LIMIT = 1_000_000
CHUNK = 1 << 16
SCHEMA = 'fd2d-lossless-piecewise-normal-gzip-capsule-v1'
NORMAL_SCHEMA = 'fd2d-offline-piecewise-ordered-normal-v1'


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def stream_identity(path):
    h, count = hashlib.sha256(), 0
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            h.update(block)
            count += len(block)
    return dict(bytes=count, sha256=h.hexdigest())


def basename(value, suffix=None):
    if not isinstance(value, str) or Path(value).name != value or value in ('', '.', '..'):
        raise ValueError('Only a single ordinary file basename is allowed')
    if suffix is not None and not value.endswith(suffix):
        raise ValueError('Unexpected capsule filename suffix')
    return value


def temporary_sibling(destination):
    destination = Path(destination).absolute()
    if destination.exists():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name+'.tmp-'+uuid.uuid4().hex)
    temporary.mkdir()
    return destination, temporary


def write_bytes(path, raw):
    with Path(path).open('xb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())


def stream_inflate(source, expected, output=None):
    count, digest = 0, hashlib.sha256()
    with gzip.open(source, 'rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            count += len(block)
            if count > expected['bytes']:
                raise ValueError('Inflated piece exceeds its original exact byte count')
            digest.update(block)
            if output is not None:
                output.write(block)
    if count != expected['bytes'] or digest.hexdigest() != expected['sha256']:
        raise ValueError('Inflated bytes do not equal the original checkpoint SHA')
    return dict(bytes=count, sha256=digest.hexdigest())


def _read_original_manifest(path, expected_sha256=None):
    path = Path(path)
    raw = path.read_bytes()
    if not 0 < len(raw) < LIMIT:
        raise ValueError('Original manifest must fit in one sub-megabyte text file')
    if expected_sha256 is not None and sha_bytes(raw) != expected_sha256:
        raise ValueError('The actual normal manifest identity differs')
    obj = json.loads(raw)
    if obj.get('schema') != NORMAL_SCHEMA or obj.get('complete') is not True:
        raise ValueError('Only an already-complete original normal checkpoint may be packed')
    basename(obj['directory_name'])
    names = []
    for row in obj['pieces']:
        names.append(basename(row['file'], '.npz'))
        if not 0 < row['bytes'] < LIMIT:
            raise ValueError('An original numerical piece exceeds its declared size limit')
    if len(set(names)) != len(names) or not names:
        raise ValueError('Duplicate or missing original checkpoint pieces')
    return raw, obj


def create_normal_capsule(normal_manifest, destination, *, expected_manifest_sha256=None):
    started = time.monotonic()
    normal_manifest = Path(normal_manifest).absolute()
    raw_manifest, original = _read_original_manifest(normal_manifest, expected_manifest_sha256)
    if normal_manifest.name != 'manifest.json' or normal_manifest.parent.name != original['directory_name']:
        raise ValueError('The original manifest is not in its completed named directory')
    destination, temporary = temporary_sibling(destination)
    try:
        rows = []
        for row in original['pieces']:
            source = normal_manifest.parent/row['file']
            if source.stat().st_size != row['bytes']:
                raise ValueError('An original checkpoint file changed size')
            compressed_name = row['file']+'.gz'
            compressed = temporary/compressed_name
            actual_hash, actual_bytes = hashlib.sha256(), 0
            with source.open('rb') as src, compressed.open('xb') as dst:
                with gzip.GzipFile(filename='', mode='wb', fileobj=dst,
                                   compresslevel=9, mtime=0) as zipped:
                    for block in iter(lambda: src.read(CHUNK), b''):
                        actual_hash.update(block)
                        actual_bytes += len(block)
                        zipped.write(block)
                dst.flush()
                os.fsync(dst.fileno())
            if actual_bytes != row['bytes'] or actual_hash.hexdigest() != row['sha256']:
                raise ValueError('An original checkpoint piece differs from its manifest')
            packed = stream_identity(compressed)
            if not 0 < packed['bytes'] < LIMIT:
                raise ValueError('An actual compressed file is not below one megabyte')
            original_identity = dict(bytes=row['bytes'], sha256=row['sha256'])
            # A complete stream-decompression check is part of creation,
            # before the capsule can acquire a final index.
            stream_inflate(compressed, original_identity)
            rows.append(dict(original_file=row['file'], original=original_identity,
                compressed_file=compressed_name, compressed=packed,
                decompressed_byte_identity_verified=True))
        if normal_manifest.read_bytes() != raw_manifest:
            raise ValueError('The source manifest changed during packing')
        write_bytes(temporary/'original-manifest.json', raw_manifest)
        index = dict(schema=SCHEMA, complete=True,
            source_sha256=sha_bytes(Path(__file__).read_bytes()),
            restored_directory_name=original['directory_name'],
            original_manifest=dict(file='original-manifest.json', bytes=len(raw_manifest),
                sha256=sha_bytes(raw_manifest)),
            original_binding_sha256=original['binding_sha256'],
            original_mapping_sha256=original['mapping_sha256'],
            original_metadata_sha256=original['metadata_sha256'],
            pieces=rows, piece_count=len(rows),
            original_numerical_bytes=sum(r['original']['bytes'] for r in rows),
            compressed_numerical_bytes=sum(r['compressed']['bytes'] for r in rows),
            largest_compressed_piece_bytes=max(r['compressed']['bytes'] for r in rows),
            original_manifest_preserved_byte_for_byte=True,
            mathematical_binding_validation='fd2d_gc_piecewise_normal_transport.load_piecewise_normal(problem, restored_manifest, expected_binding=...)',
            original_normal_schema=NORMAL_SCHEMA,
            original_loader_source=original['piece_consumer_source'],
            numerical_operations_performed=False, seconds=time.monotonic()-started)
        index_bytes = (json.dumps(index, indent=2, sort_keys=True, allow_nan=False)+'\n').encode()
        if len(index_bytes) >= LIMIT:
            raise ValueError('The capsule index exceeds the single-file size limit')
        write_bytes(temporary/'index.json', index_bytes)  # final capsule file
        os.rename(temporary, destination)
        return destination/'index.json'
    except BaseException:
        shutil.rmtree(temporary, ignore_errors=True)
        raise


def restore_normal_capsule(index_path, destination, *, expected_manifest_sha256=None):
    index_path = Path(index_path).absolute()
    index = json.loads(index_path.read_text())
    if index.get('schema') != SCHEMA or index.get('complete') is not True:
        raise ValueError('This is not a complete supported capsule')
    manifest_row = index['original_manifest']
    manifest_file = index_path.parent/basename(manifest_row['file'])
    raw_manifest, original = _read_original_manifest(manifest_file,
        expected_manifest_sha256 or manifest_row['sha256'])
    if len(raw_manifest) != manifest_row['bytes'] or sha_bytes(raw_manifest) != manifest_row['sha256']:
        raise ValueError('Original-manifest bytes differ from the capsule index')
    if (original['directory_name'] != index['restored_directory_name']
            or original['binding_sha256'] != index['original_binding_sha256']
            or original['mapping_sha256'] != index['original_mapping_sha256']
            or original['metadata_sha256'] != index['original_metadata_sha256']):
        raise ValueError('Capsule and original identities differ')
    destination = Path(destination).absolute()
    if destination.name != original['directory_name']:
        raise ValueError('Restore to the original declared basename: '+original['directory_name'])
    if index['piece_count'] != len(original['pieces']) or len(index['pieces']) != len(original['pieces']):
        raise ValueError('Capsule coverage differs from the complete original manifest')
    original_rows = {r['file']: r for r in original['pieces']}
    names = [basename(r['original_file'], '.npz') for r in index['pieces']]
    if set(names) != set(original_rows) or len(set(names)) != len(names):
        raise ValueError('Duplicate, missing, or extra capsule pieces')
    destination, temporary = temporary_sibling(destination)
    try:
        for row in index['pieces']:
            name = row['original_file']
            expected = {k:original_rows[name][k] for k in ('bytes', 'sha256')}
            if row['original'] != expected:
                raise ValueError('A piece binding differs from the original manifest')
            packed = row['compressed']
            if not 0 < packed['bytes'] < LIMIT:
                raise ValueError('The compressed piece exceeds the declared size limit')
            compressed = index_path.parent/basename(row['compressed_file'], '.npz.gz')
            if stream_identity(compressed) != packed:
                raise ValueError('Compressed bytes differ from the capsule index')
            with (temporary/name).open('xb') as output:
                stream_inflate(compressed, expected, output)
                output.flush()
                os.fsync(output.fileno())
        # The original loader sees neither a partial directory nor a
        # reconstructed/modified metadata document.
        write_bytes(temporary/'manifest.json', raw_manifest)
        os.rename(temporary, destination)
        return destination/'manifest.json'
    except BaseException:
        shutil.rmtree(temporary, ignore_errors=True)
        raise


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='command', required=True)
    p = sub.add_parser('pack')
    p.add_argument('--manifest', type=Path, required=True)
    p.add_argument('--destination', type=Path, required=True)
    p.add_argument('--expected-manifest-sha256')
    p = sub.add_parser('restore')
    p.add_argument('--index', type=Path, required=True)
    p.add_argument('--destination', type=Path, required=True)
    p.add_argument('--expected-manifest-sha256')
    args = ap.parse_args()
    if args.command == 'pack':
        path = create_normal_capsule(args.manifest, args.destination,
            expected_manifest_sha256=args.expected_manifest_sha256)
        index = json.loads(path.read_text())
        result = dict(index=str(path), **stream_identity(path),
            pieces=index['piece_count'], original_numerical_bytes=index['original_numerical_bytes'],
            compressed_numerical_bytes=index['compressed_numerical_bytes'],
            largest_compressed_piece_bytes=index['largest_compressed_piece_bytes'],
            seconds=index['seconds'])
    else:
        path = restore_normal_capsule(args.index, args.destination,
            expected_manifest_sha256=args.expected_manifest_sha256)
        result = dict(restored_manifest=str(path), **stream_identity(path),
            all_pieces_stream_verified=True, original_loader_binding_check_still_required=True)
    print(json.dumps(result, allow_nan=False))


if __name__ == '__main__':
    main()
