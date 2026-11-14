#!/usr/bin/env python3
"""Explicit new 78718 storage envelope for original prefix gzip/NPZ bytes.

This is not the missing historical db6f storage helper.  Its hash-only path
imports no NumPy or SciPy.  It never evaluates Hermite/Fourier expressions or
changes arrays.  Optional NPZ layout inspection is storage validation only;
the original mathematical reader retains its own finite-value and geometry
checks.  The original single-file readers remain separate and unchanged.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import io
from pathlib import Path


HERE = Path(__file__).resolve().parent
CODEC_FILE = HERE/'78718-prefix-byte-shards-v1.py'
CODEC_SHA256 = 'e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39'
SCHEMA = '78718-prefix-original-gzip-npz-storage-v1'
FORMAT = 'original-gzip-npz'
ARRAY_NAMES = ('mesh', 'jets', 'mean_increments')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def codec():
    raw = CODEC_FILE.read_bytes()
    if sha(raw) != CODEC_SHA256:
        raise ValueError('Frozen 78718 byte codec changed')
    spec = importlib.util.spec_from_file_location('prefix_78718_byte_storage_v1', CODEC_FILE)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def inspect_arrays(payload, *, nodes, modes):
    """Check the original saved layout, without changing or resaving arrays.

    NaN payloads and signed zeros are deliberately not normalized.  Original
    mathematical readers, not this storage helper, decide whether nonfinite
    mathematical input is permitted.  Generic arbitrary-array NPZ identity is
    provided by the byte codec independently of this prefix-specific layout.
    """
    import numpy as np
    c = codec()
    c.integer(nodes, 'prefix nodes', 2)
    c.integer(modes, 'prefix modes', 1)
    expected = {'mesh': (nodes,), 'jets': (3, nodes, 3*modes+2),
                'mean_increments': (nodes-1,)}
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as saved:
        c.require(len(saved.files) == 3 and set(saved.files) == set(ARRAY_NAMES),
                  'Prefix NPZ must contain the three original arrays')
        ledger = {}
        for name in ARRAY_NAMES:
            array = saved[name]
            c.require(array.dtype.str == '<f8' and array.shape == expected[name],
                      'Unexpected saved prefix dtype/shape: '+name)
            ledger[name] = {'dtype': array.dtype.str, 'shape': list(array.shape),
                            'c_order_bytes': array.nbytes,
                            'c_order_sha256': sha(array.tobytes(order='C'))}
    return ledger


def write_payload(out_prefix, payload, *, nodes, modes, chunk_bytes=4_600_000):
    """Write bounded storage for already serialized original bytes."""
    c = codec()
    c.integer(nodes, 'prefix nodes', 2)
    c.integer(modes, 'prefix modes', 1)
    storage = c.write_bytes(out_prefix, payload, logical_format=FORMAT,
                            chunk_bytes=chunk_bytes)
    return {'schema': SCHEMA, **storage, 'nodes': nodes, 'modes': modes,
            'codec_sha256': CODEC_SHA256,
            'reader_sha256': sha(Path(__file__).read_bytes())}


def read_payload(meta_path, *, verify_arrays=True):
    """Return (unchanged metadata, exact logical bytes, actual file closure).

    Call this with the *defining base* metadata.  A common-cut adapter must
    resolve that base first; its larger Fourier mode count is not a license
    to reinterpret the base NPZ dimensions.
    """
    c = codec()
    c.require(type(verify_arrays) is bool, 'Expected explicit array-check flag')
    path = Path(meta_path).resolve()
    c.require(path.stat().st_size < c.JSON_LIMIT, 'Prefix metadata is not small JSON')
    raw = path.read_bytes()
    meta = c.parse_json(raw)
    c.require(type(meta) is dict and 'data_storage' in meta and 'data_file' not in meta,
              'This entry requires explicit new 78718 storage metadata')
    storage = meta['data_storage']
    c.fields(storage, ('schema', 'descriptor_file', 'descriptor_bytes',
                       'descriptor_sha256', 'logical_format', 'logical_bytes',
                       'logical_sha256', 'nodes', 'modes', 'codec_sha256',
                       'reader_sha256'), 'prefix storage reference')
    c.require(storage['schema'] == SCHEMA and storage['logical_format'] == FORMAT,
              'Wrong prefix storage schema/format')
    c.require(storage['codec_sha256'] == CODEC_SHA256 and
              storage['reader_sha256'] == sha(Path(__file__).read_bytes()),
              'Prefix storage source identity differs')
    nodes = c.integer(meta['nodes'], 'defining base nodes', 2)
    modes = c.integer(meta['modes'], 'defining base modes', 1)
    c.require(c.integer(storage['nodes'], 'storage nodes', 2) == nodes and
              c.integer(storage['modes'], 'storage modes', 1) == modes,
              'Storage dimensions differ from defining base')
    c.require(c.digest(meta['data_sha256'], 'original logical data SHA256') ==
              storage['logical_sha256'], 'Logical prefix identity differs')
    name = c.basename(storage['descriptor_file'], 'descriptor filename')
    c.require(name.endswith('-storage.json'), 'Wrong descriptor filename suffix')
    payload, parts = c.read_bytes(path.parent/name,
        descriptor_sha256=storage['descriptor_sha256'],
        descriptor_bytes=storage['descriptor_bytes'],
        logical_sha256=storage['logical_sha256'],
        logical_bytes=storage['logical_bytes'], logical_format=FORMAT)
    if verify_arrays:
        inspect_arrays(payload, nodes=nodes, modes=modes)
    records = [c.identity(path, raw), *parts, c.identity(__file__), c.identity(CODEC_FILE)]
    c.require(len({row['file'] for row in records}) == len(records),
              'Repeated storage closure path')
    return meta, payload, records
