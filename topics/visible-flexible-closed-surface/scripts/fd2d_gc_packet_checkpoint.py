"""Lossless, no-pickle transport for an actually evaluated finite GC packet.

This module does not evaluate or change a field or equation. NumPy arrays
and scalars retain dtype and data; native containers retain their kinds.
Each compressed NPZ is bounded by a 700 KiB raw payload. The directory is
published atomically only after all parts and the final manifest exist.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import tempfile
import numpy as np

SCHEMA = 'fd2d-actual-value-packet-no-pickle-v1'
PART_RAW_BYTES = 700 * 1024


def _canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _file(path):
    path = Path(path)
    return dict(name=path.name, bytes=path.stat().st_size,
                sha256=_sha(path.read_bytes()))


def save_actual_packet(packet, directory, *, binding):
    """Return the immutable manifest path after an atomic complete save."""
    destination = Path(directory)
    if destination.exists():
        raise FileExistsError('Never overwrite a saved actual packet')
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Ensure binding itself is exact JSON before starting any writes.
    frozen_binding = json.loads(_canonical(binding))
    arrays, array_ids = [], {}

    def encode(value):
        if isinstance(value, np.ndarray):
            key = id(value)
            if key not in array_ids:
                if value.dtype.hasobject or value.dtype.fields is not None:
                    raise TypeError('Object arrays are not a numerical packet')
                array_ids[key] = len(arrays)
                arrays.append(np.ascontiguousarray(value).reshape(value.shape))
            return {'kind': 'array', 'index': array_ids[key]}
        if isinstance(value, np.generic):
            array = np.asarray(value)
            if array.dtype.hasobject or array.dtype.fields is not None:
                raise TypeError('Object scalar is not supported')
            index = len(arrays)
            arrays.append(array)
            return {'kind': 'numpy_scalar', 'index': index}
        if isinstance(value, dict):
            return {'kind': 'dict', 'items': [[encode(k), encode(v)] for k, v in value.items()]}
        if isinstance(value, tuple):
            return {'kind': 'tuple', 'items': [encode(v) for v in value]}
        if isinstance(value, list):
            return {'kind': 'list', 'items': [encode(v) for v in value]}
        if value is None or type(value) in (bool, int, float, str):
            # json.dumps below refuses NaN and infinities.
            return {'kind': 'native', 'value': value}
        raise TypeError('Unsupported actual-packet value: '+type(value).__name__)

    tree = encode(packet)
    staging = Path(tempfile.mkdtemp(prefix=destination.name+'-writing-', dir=destination.parent))
    parts, descriptions = [], []
    pending, pending_bytes, pending_targets = {}, 0, []

    def flush():
        nonlocal pending, pending_bytes, pending_targets
        if not pending:
            return
        name = 'part-%04d.npz' % len(parts)
        path = staging/name
        np.savez_compressed(path, **pending)
        if path.stat().st_size >= 1024*1024:
            raise ValueError('A supposedly small transport part exceeded 1 MiB')
        parts.append(_file(path))
        for array_index, item in pending_targets:
            descriptions[array_index]['parts'].append(dict(file=name, **item))
        pending, pending_bytes, pending_targets = {}, 0, []

    for index, value in enumerate(arrays):
        flat = value.reshape(-1)
        descriptions.append(dict(shape=list(value.shape), dtype=value.dtype.str,
            bytes=value.nbytes, sha256=_sha(value.tobytes(order='C')), parts=[]))
        count = max(1, PART_RAW_BYTES//max(1, value.dtype.itemsize))
        starts = range(0, len(flat), count) if len(flat) else (0,)
        for start in starts:
            piece = flat[start:min(len(flat), start+count)]
            if pending and (pending_bytes+piece.nbytes > PART_RAW_BYTES or len(pending) >= 64):
                flush()
            key = 'array_%06d_at_%09d' % (index, start)
            pending[key] = piece
            pending_bytes += piece.nbytes
            pending_targets.append((index, dict(key=key, start=start, count=len(piece))))
    flush()
    manifest = dict(schema=SCHEMA, binding=frozen_binding,
        binding_sha256=_sha(_canonical(frozen_binding).encode()),
        arrays=descriptions, parts=parts, tree=tree,
        raw_array_bytes=sum(a.nbytes for a in arrays),
        compressed_part_bytes=sum(q['bytes'] for q in parts),
        native_container_types_preserved=True, pickle_used=False,
        complete=True)
    manifest_path = staging/'manifest.json'
    manifest_path.write_text(json.dumps(manifest, indent=2, allow_nan=False)+'\n')
    # Atomic directory rename is the completion boundary. A killed writer
    # leaves an explicitly incomplete staging directory, not a valid cache.
    os.rename(staging, destination)
    return destination/'manifest.json'


def load_actual_packet(manifest, *, expected_binding):
    """Load only a complete packet with the requested exact binding."""
    path = Path(manifest)
    if path.is_dir():
        path = path/'manifest.json'
    record = json.loads(path.read_text())
    expected = json.loads(_canonical(expected_binding))
    if record.get('schema') != SCHEMA or record.get('complete') is not True:
        raise ValueError('Not a complete actual-packet checkpoint')
    if record['binding'] != expected or record['binding_sha256'] != _sha(_canonical(expected).encode()):
        raise ValueError('Actual-packet binding does not match the requested mathematical input')
    allowed = {p['name']: p for p in record['parts']}
    pieces = {}
    for name, description in allowed.items():
        if Path(name).name != name:
            raise ValueError('Transport part must be a sibling basename')
        part = path.parent/name
        actual = _file(part)
        if actual != description:
            raise ValueError('Transport part checksum or size mismatch: '+name)
        with np.load(part, allow_pickle=False) as source:
            pieces[name] = {key: source[key] for key in source.files}
    arrays = []
    for description in record['arrays']:
        dtype = np.dtype(description['dtype'])
        if dtype.hasobject:
            raise ValueError('Object dtype is forbidden')
        size = int(np.prod(description['shape'], dtype=np.int64))
        flat = np.empty(size, dtype=dtype)
        cursor = 0
        for item in description['parts']:
            if item['file'] not in allowed or item['start'] != cursor:
                raise ValueError('Nonconsecutive or unbound array pieces')
            piece = pieces[item['file']][item['key']]
            if piece.dtype != dtype or piece.shape != (item['count'],):
                raise ValueError('Transport dtype/shape mismatch')
            # Copy raw bytes also for long-double padding and nonnative
            # endianness; no dtype conversion or scalar re-rounding.
            first = cursor*dtype.itemsize
            flat.view(np.uint8)[first:first+piece.nbytes] = np.ascontiguousarray(piece).view(np.uint8)
            cursor += len(piece)
        if cursor != size:
            raise ValueError('Transport array is incomplete')
        array = flat.reshape(description['shape'])
        if array.nbytes != description['bytes'] or _sha(array.tobytes(order='C')) != description['sha256']:
            raise ValueError('Reconstructed actual array checksum mismatch')
        arrays.append(array)

    def decode(value):
        kind = value['kind']
        if kind == 'array':
            return arrays[value['index']]
        if kind == 'numpy_scalar':
            return arrays[value['index']][()]
        if kind == 'native':
            return value['value']
        if kind == 'dict':
            return {decode(k): decode(v) for k, v in value['items']}
        if kind in ('list', 'tuple'):
            result = [decode(v) for v in value['items']]
            return tuple(result) if kind == 'tuple' else result
        raise ValueError('Unknown transport tree tag')
    return decode(record['tree'])
