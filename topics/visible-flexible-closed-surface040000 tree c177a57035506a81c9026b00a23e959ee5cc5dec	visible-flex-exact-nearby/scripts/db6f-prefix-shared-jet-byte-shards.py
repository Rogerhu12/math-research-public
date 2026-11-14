#!/usr/bin/env python3
"""Lossless storage codec for an existing shared-Hermite gzip/NPZ byte stream.

This module does not construct geometry, resave arrays, patch any reader, or
write files.  Its return value is a new storage descriptor and in-memory gzip
parts.  A future producer/consumer must explicitly bind this new storage
identity; legacy data_file readers cannot silently consume the descriptor.
"""
from __future__ import annotations

import gzip
import hashlib
import io
import json
from pathlib import Path
import re
from typing import Mapping

import numpy as np


SCHEMA = 'db6f-shared-hermite-logical-byte-shards-v1'
LOGICAL_FORMAT = 'original-gzip-npz-shared-nodal-two-jet'
FILE_LIMIT = 5_000_000
MAX_RAW_PART = 4_000_000
ARRAY_NAMES = ('mesh', 'jets', 'mean_increments')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def integer(value, name, minimum=0):
    require(type(value) is int and value >= minimum, 'Invalid integer: '+name)
    return value


def digest(value, name):
    require(type(value) is str and re.fullmatch(r'[0-9a-f]{64}', value) is not None,
            'Invalid SHA256: '+name)
    return value


def keys(value, expected, name):
    require(type(value) is dict and set(value) == set(expected),
            'Unexpected fields: '+name)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      allow_nan=False).encode()


def inspect_container(payload, *, nodes, modes):
    """Read only the three saved arrays; no polynomial/geometric evaluation."""
    require(type(payload) is bytes and len(payload) > 0, 'Empty/non-bytes container')
    integer(nodes, 'nodes', 2)
    integer(modes, 'modes', 1)
    expected = {'mesh': (nodes,), 'jets': (3, nodes, 3*modes+2),
                'mean_increments': (nodes-1,)}
    try:
        with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as saved:
            require(len(saved.files) == 3 and set(saved.files) == set(ARRAY_NAMES),
                    'Logical container must contain exactly the three original arrays')
            result = {}
            for name in ARRAY_NAMES:
                array = saved[name]
                require(array.dtype.str == '<f8', 'Unexpected original dtype: '+name)
                require(array.shape == expected[name], 'Unexpected original shape: '+name)
                require(bool(np.isfinite(array).all()), 'Nonfinite original array: '+name)
                if name == 'mesh':
                    require(bool(np.all(np.diff(array) > 0)), 'Non-increasing original mesh')
                result[name] = dict(dtype='<f8', shape=list(array.shape),
                                    c_order_bytes=array.nbytes,
                                    c_order_sha256=sha(array.tobytes(order='C')))
    except (OSError, EOFError, KeyError, TypeError) as exc:
        raise ValueError('Invalid logical gzip/NPZ container') from exc
    return result


def validate_descriptor(descriptor, *, nodes, modes, logical_sha256):
    """Validate typed metadata, every contiguous byte range and array shape."""
    integer(nodes, 'expected nodes', 2)
    integer(modes, 'expected modes', 1)
    digest(logical_sha256, 'expected logical SHA256')
    keys(descriptor, ('schema', 'logical_format', 'logical_bytes', 'logical_sha256',
                      'nodes', 'modes', 'arrays', 'parts'), 'descriptor')
    require(descriptor['schema'] == SCHEMA and descriptor['logical_format'] == LOGICAL_FORMAT,
            'Unsupported storage schema/format')
    total = integer(descriptor['logical_bytes'], 'logical_bytes', 1)
    digest(descriptor['logical_sha256'], 'logical_sha256')
    require(descriptor['logical_sha256'] == logical_sha256, 'Wrong expected logical identity')
    integer(descriptor['nodes'], 'nodes', 2)
    integer(descriptor['modes'], 'modes', 1)
    require(descriptor['nodes'] == nodes and descriptor['modes'] == modes,
            'Storage shape differs from the defining base metadata')
    shapes = {'mesh': [nodes], 'jets': [3, nodes, 3*modes+2],
              'mean_increments': [nodes-1]}
    keys(descriptor['arrays'], ARRAY_NAMES, 'array ledger')
    for name in ARRAY_NAMES:
        item = descriptor['arrays'][name]
        keys(item, ('dtype', 'shape', 'c_order_bytes', 'c_order_sha256'), 'array '+name)
        require(item['dtype'] == '<f8', 'Wrong array dtype '+name)
        require(type(item['shape']) is list and
                all(type(x) is int and x > 0 for x in item['shape']) and
                item['shape'] == shapes[name], 'Wrong array dimensions '+name)
        size = 8
        for length in shapes[name]:
            size *= length
        require(integer(item['c_order_bytes'], name+' bytes', 1) == size,
                'Wrong array byte count '+name)
        digest(item['c_order_sha256'], name+' SHA256')
    parts = descriptor['parts']
    require(type(parts) is list and len(parts) > 0, 'Empty/non-list parts')
    offset = 0
    names = set()
    for index, item in enumerate(parts):
        keys(item, ('index', 'offset', 'raw_bytes', 'raw_sha256', 'file',
                    'stored_bytes', 'stored_sha256'), 'part')
        require(integer(item['index'], 'index') == index, 'Noncanonical part order/index')
        require(integer(item['offset'], 'offset') == offset, 'Gap/overlap in logical bytes')
        length = integer(item['raw_bytes'], 'raw_bytes', 1)
        require(length <= MAX_RAW_PART, 'Raw part exceeds its bounded storage contract')
        digest(item['raw_sha256'], 'raw_sha256')
        filename = item['file']
        require(type(filename) is str and
                re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*\.bin\.gz', filename) is not None,
                'Part name must be a simple gzip basename')
        require(filename not in names, 'Duplicate part filename')
        names.add(filename)
        require(integer(item['stored_bytes'], 'stored_bytes', 1) < FILE_LIMIT,
                'Stored part violates the strict repository file limit')
        digest(item['stored_sha256'], 'stored_sha256')
        offset += length
        require(offset <= total, 'Part exceeds the logical byte count')
    require(offset == total, 'Parts do not cover all logical bytes')
    return descriptor


def encode_bytes(payload, *, nodes, modes, part_stem, chunk_bytes=MAX_RAW_PART):
    """Return metadata + gzip parts without changing a byte of the input stream."""
    integer(chunk_bytes, 'chunk_bytes', 1)
    require(chunk_bytes <= MAX_RAW_PART, 'Chunk exceeds the safe raw-part maximum')
    require(type(part_stem) is str and
            re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', part_stem) is not None,
            'Invalid part stem')
    arrays = inspect_container(payload, nodes=nodes, modes=modes)
    records, stored = [], {}
    for index, offset in enumerate(range(0, len(payload), chunk_bytes)):
        raw = payload[offset:offset+chunk_bytes]
        compressed = gzip.compress(raw, mtime=0)
        require(len(compressed) < FILE_LIMIT, 'Compressed part is too large; nothing has been written')
        filename = f'{part_stem}.part-{index:05d}.bin.gz'
        records.append(dict(index=index, offset=offset, raw_bytes=len(raw),
                            raw_sha256=sha(raw), file=filename,
                            stored_bytes=len(compressed), stored_sha256=sha(compressed)))
        stored[filename] = compressed
    descriptor = dict(schema=SCHEMA, logical_format=LOGICAL_FORMAT,
                      logical_bytes=len(payload), logical_sha256=sha(payload),
                      nodes=nodes, modes=modes, arrays=arrays, parts=records)
    validate_descriptor(descriptor, nodes=nodes, modes=modes, logical_sha256=sha(payload))
    return descriptor, stored


def decode_bytes(descriptor, stored_parts: Mapping[str, bytes], *, nodes, modes,
                 logical_sha256):
    """Reassemble and verify original bytes; never write a large logical file."""
    validate_descriptor(descriptor, nodes=nodes, modes=modes, logical_sha256=logical_sha256)
    expected = {part['file'] for part in descriptor['parts']}
    require(set(stored_parts) == expected, 'Missing/extra storage part')
    chunks = []
    for part in descriptor['parts']:
        payload = stored_parts[part['file']]
        require(type(payload) is bytes, 'Storage part must be bytes')
        require(len(payload) == part['stored_bytes'] and sha(payload) == part['stored_sha256'],
                'Stored part size/SHA256 mismatch')
        try:
            raw = gzip.decompress(payload)
        except (OSError, EOFError) as exc:
            raise ValueError('Invalid gzip part') from exc
        require(len(raw) == part['raw_bytes'] and sha(raw) == part['raw_sha256'],
                'Raw part size/SHA256 mismatch')
        chunks.append(raw)
    logical = b''.join(chunks)
    require(len(logical) == descriptor['logical_bytes'] and sha(logical) == logical_sha256,
            'Reconstructed logical container identity mismatch')
    require(canonical(inspect_container(logical, nodes=nodes, modes=modes)) ==
            canonical(descriptor['arrays']), 'Reconstructed array ledger mismatch')
    return logical


def parse_descriptor(payload):
    """Reject duplicate JSON fields/nonfinite tokens before typed validation."""
    require(type(payload) is bytes and 0 < len(payload) < FILE_LIMIT,
            'Invalid descriptor size/type')
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate JSON field')
            result[key] = value
        return result
    def no_constant(value):
        raise ValueError('Nonfinite JSON token: '+value)
    return json.loads(payload, object_pairs_hook=no_duplicates, parse_constant=no_constant)


def read_bytes(descriptor_path, *, descriptor_sha256, nodes, modes, logical_sha256):
    """Optional storage-only entry; future consumers must bind this explicitly.

    The expected descriptor hash and logical hash come from the new outer
    storage metadata, not from an untrusted descriptor's self-assertion.
    No legacy metadata dispatch or geometric construction occurs here.
    """
    descriptor_path = Path(descriptor_path)
    digest(descriptor_sha256, 'descriptor SHA256')
    blob = descriptor_path.read_bytes()
    require(sha(blob) == descriptor_sha256, 'Descriptor SHA256 mismatch')
    descriptor = parse_descriptor(blob)
    validate_descriptor(descriptor, nodes=nodes, modes=modes, logical_sha256=logical_sha256)
    parts = {part['file']: (descriptor_path.parent/part['file']).read_bytes()
             for part in descriptor['parts']}
    return decode_bytes(descriptor, parts, nodes=nodes, modes=modes,
                        logical_sha256=logical_sha256)
