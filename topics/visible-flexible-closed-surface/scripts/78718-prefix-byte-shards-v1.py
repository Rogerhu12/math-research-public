#!/usr/bin/env python3
"""New 78718 lossless byte storage; not a recovery of missing db6f A/B.

The logical input is an opaque byte string.  In the prefix application it is
the *original* gzip/NPZ output, including every NPZ and gzip byte.  No array is
decoded, converted, or reserialized here.  Only standard-library modules are
imported.  Mathematical solvers and the original single-file branch are not
changed by this explicitly named representation.
"""
from __future__ import annotations

import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import zlib


SCHEMA = '78718-logical-byte-shards-v1'
FILE_LIMIT = 5_000_000
JSON_LIMIT = 1_000_000
MAX_RAW_PART = 4_600_000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(payload):
    return hashlib.sha256(payload).hexdigest()


def integer(value, label, minimum=0):
    require(type(value) is int and value >= minimum, 'Invalid integer: '+label)
    return value


def digest(value, label):
    require(type(value) is str and re.fullmatch(r'[0-9a-f]{64}', value) is not None,
            'Invalid SHA256: '+label)
    return value


def fields(value, names, label):
    require(type(value) is dict and set(value) == set(names),
            'Unexpected fields: '+label)


def basename(value, label):
    require(type(value) is str and 0 < len(value.encode('utf-8')) <= 240 and
            re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', value) is not None,
            'Expected simple basename: '+label)
    return value


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=True, allow_nan=False)+'\n').encode('utf-8')


def parse_json(raw):
    require(type(raw) is bytes and 0 < len(raw) < JSON_LIMIT,
            'Invalid storage JSON size/type')

    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate storage JSON key')
            result[key] = value
        return result

    def constant(value):
        raise ValueError('Nonfinite storage JSON constant: '+value)

    return json.loads(raw, object_pairs_hook=unique, parse_constant=constant)


def validate_descriptor(descriptor, *, logical_sha256, logical_bytes,
                        logical_format):
    fields(descriptor, ('schema', 'logical_format', 'logical_bytes',
                       'logical_sha256', 'parts'), 'descriptor')
    require(descriptor['schema'] == SCHEMA, 'Wrong byte storage schema')
    require(type(logical_format) is str and bool(logical_format) and
            descriptor['logical_format'] == logical_format, 'Wrong logical format')
    digest(logical_sha256, 'expected logical SHA256')
    integer(logical_bytes, 'expected logical bytes', 1)
    require(integer(descriptor['logical_bytes'], 'logical bytes', 1) == logical_bytes,
            'Wrong logical byte count')
    require(digest(descriptor['logical_sha256'], 'logical SHA256') == logical_sha256,
            'Wrong logical identity')
    parts = descriptor['parts']
    require(type(parts) is list and bool(parts), 'Missing byte parts')
    offset, used = 0, set()
    for index, row in enumerate(parts):
        fields(row, ('index', 'offset', 'raw_bytes', 'raw_sha256', 'file',
                     'stored_bytes', 'stored_sha256'), 'byte part')
        require(integer(row['index'], 'part index') == index,
                'Noncanonical part index/order')
        require(integer(row['offset'], 'part offset') == offset,
                'Logical byte gap or overlap')
        length = integer(row['raw_bytes'], 'raw part bytes', 1)
        require(length <= MAX_RAW_PART, 'Raw byte part exceeds 4,600,000 bytes')
        digest(row['raw_sha256'], 'raw part SHA256')
        name = basename(row['file'], 'part filename')
        require(name.endswith('.bin.gz') and name not in used,
                'Invalid or repeated byte-part filename')
        used.add(name)
        require(integer(row['stored_bytes'], 'stored part bytes', 1) < FILE_LIMIT,
                'Stored byte part violates the strict file limit')
        digest(row['stored_sha256'], 'stored part SHA256')
        offset += length
        require(offset <= logical_bytes, 'Byte part exceeds logical payload')
    require(offset == logical_bytes, 'Byte parts do not cover the logical payload')
    return descriptor


def encode_bytes(payload, *, part_stem, logical_format='original-gzip-npz',
                 chunk_bytes=MAX_RAW_PART):
    """Return a descriptor and gzip members without altering logical bytes."""
    require(type(payload) is bytes and bool(payload), 'Expected nonempty logical bytes')
    basename(part_stem, 'part stem')
    integer(chunk_bytes, 'chunk bytes', 1)
    require(chunk_bytes <= MAX_RAW_PART, 'Requested raw part is too large')
    require(type(logical_format) is str and bool(logical_format), 'Missing logical format')
    rows, compressed_parts = [], {}
    for index, offset in enumerate(range(0, len(payload), chunk_bytes)):
        raw = payload[offset:offset+chunk_bytes]
        compressed = gzip.compress(raw, mtime=0)
        require(len(compressed) < FILE_LIMIT,
                'Compressed byte part exceeds file limit; no file has been written')
        name = basename(f'{part_stem}.part-{index:06d}.bin.gz', 'part filename')
        rows.append(dict(index=index, offset=offset, raw_bytes=len(raw),
                         raw_sha256=sha(raw), file=name,
                         stored_bytes=len(compressed), stored_sha256=sha(compressed)))
        compressed_parts[name] = compressed
    descriptor = dict(schema=SCHEMA, logical_format=logical_format,
                      logical_bytes=len(payload), logical_sha256=sha(payload),
                      parts=rows)
    validate_descriptor(descriptor, logical_sha256=sha(payload),
                        logical_bytes=len(payload), logical_format=logical_format)
    require(len(canonical(descriptor)) < JSON_LIMIT,
            'Descriptor exceeds the small JSON contract; no file has been written')
    return descriptor, compressed_parts


def decode_bytes(descriptor, compressed_parts, *, logical_sha256, logical_bytes,
                 logical_format='original-gzip-npz'):
    """Reassemble exact bytes, with bounded per-part decompression."""
    validate_descriptor(descriptor, logical_sha256=logical_sha256,
                        logical_bytes=logical_bytes, logical_format=logical_format)
    require(type(compressed_parts) is dict and
            set(compressed_parts) == {row['file'] for row in descriptor['parts']},
            'Missing or extra stored byte part')
    chunks = []
    for row in descriptor['parts']:
        stored = compressed_parts[row['file']]
        require(type(stored) is bytes and len(stored) == row['stored_bytes'] and
                sha(stored) == row['stored_sha256'], 'Stored part size/SHA256 mismatch')
        try:
            with gzip.GzipFile(fileobj=io.BytesIO(stored), mode='rb') as stream:
                raw = stream.read(row['raw_bytes']+1)
        except (OSError, EOFError, zlib.error) as exc:
            raise ValueError('Invalid gzip byte part') from exc
        require(len(raw) == row['raw_bytes'] and sha(raw) == row['raw_sha256'],
                'Raw part size/SHA256 mismatch')
        chunks.append(raw)
    payload = b''.join(chunks)
    require(len(payload) == logical_bytes and sha(payload) == logical_sha256,
            'Reassembled logical payload identity mismatch')
    return payload


def identity(path, data=None):
    path = Path(path).resolve()
    if data is None:
        data = path.read_bytes()
    require(type(data) is bytes, 'Identity requires exact bytes')
    require(0 < len(data) < FILE_LIMIT, 'Storage closure file violates size limit')
    return {'file': str(path), 'bytes': len(data), 'sha256': sha(data)}


def _write_exact(path, raw):
    """Reuse identical content-addressed bytes; never replace a conflicting file."""
    path = Path(path)
    require(type(raw) is bytes and 0 < len(raw) < FILE_LIMIT, 'Invalid physical file size')
    if path.exists():
        require(path.is_file() and path.read_bytes() == raw,
                'Existing storage filename has different bytes: '+str(path))
        return
    with path.open('xb') as stream:
        stream.write(raw)


def write_bytes(out_prefix, payload, *, logical_format='original-gzip-npz',
                chunk_bytes=MAX_RAW_PART):
    """Write only bounded members and a small descriptor, descriptor last."""
    prefix = Path(out_prefix)
    require(prefix.parent.is_dir(), 'Output directory does not exist')
    require(type(payload) is bytes and bool(payload), 'Expected nonempty logical bytes')
    stem = basename(prefix.name+'-payload-'+sha(payload), 'content-addressed stem')
    descriptor, parts = encode_bytes(payload, part_stem=stem,
                                     logical_format=logical_format, chunk_bytes=chunk_bytes)
    name = basename(stem+'-storage.json', 'descriptor filename')
    raw = canonical(descriptor)
    writes = [(prefix.parent/row['file'], parts[row['file']]) for row in descriptor['parts']]
    writes.append((prefix.parent/name, raw))
    # Preflight *every* conflict before creating the first member.
    for path, blob in writes:
        if path.exists():
            require(path.is_file() and path.read_bytes() == blob,
                    'Existing storage filename has different bytes: '+str(path))
    for path, blob in writes:
        _write_exact(path, blob)
    return {'descriptor_file': name, 'descriptor_bytes': len(raw),
            'descriptor_sha256': sha(raw), 'logical_format': logical_format,
            'logical_bytes': len(payload), 'logical_sha256': sha(payload)}


def read_bytes(descriptor_path, *, descriptor_sha256, descriptor_bytes,
               logical_sha256, logical_bytes, logical_format='original-gzip-npz'):
    """Read an externally bound descriptor and all its bounded physical files."""
    path = Path(descriptor_path).resolve()
    digest(descriptor_sha256, 'expected descriptor SHA256')
    require(integer(descriptor_bytes, 'expected descriptor bytes', 1) < JSON_LIMIT,
            'Descriptor is not small JSON')
    require(path.stat().st_size == descriptor_bytes, 'Descriptor byte count mismatch')
    raw = path.read_bytes()
    require(sha(raw) == descriptor_sha256, 'Descriptor SHA256 mismatch')
    descriptor = parse_json(raw)
    validate_descriptor(descriptor, logical_sha256=logical_sha256,
                        logical_bytes=logical_bytes, logical_format=logical_format)
    records = [identity(path, raw)]
    parts = {}
    for row in descriptor['parts']:
        member = path.parent/row['file']
        require(member.stat().st_size == row['stored_bytes'], 'Stored part byte count mismatch')
        parts[row['file']] = member.read_bytes()
        records.append(identity(member, parts[row['file']]))
    payload = decode_bytes(descriptor, parts, logical_sha256=logical_sha256,
                           logical_bytes=logical_bytes, logical_format=logical_format)
    return payload, records
