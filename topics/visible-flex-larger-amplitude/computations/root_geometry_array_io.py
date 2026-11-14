"""Lossless bounded-size storage for complete numerical geometry fields.

Every radial row is retained.  The manifest is written only after all gzip
NPY chunks are complete; hashes and contiguous row ranges are checked on
read.  These are samples, not interval bounds or a surface certificate.
"""
from __future__ import annotations
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_chunks(path, values):
    path = Path(path)
    values = np.asarray(values)
    if (path.exists() or path.suffix != '.json' or values.dtype != np.float64
            or values.ndim != 3 or values.shape[2] != 3
            or not np.isfinite(values).all()):
        raise ValueError('Use a fresh JSON manifest for complete finite float64 fields')
    row_bytes = values.shape[1]*values.shape[2]*8
    rows = max(1, 4_000_000//row_bytes)
    if row_bytes > 4_000_000:
        raise ValueError('One complete angular row exceeds the storage budget')
    entries = []
    for number, start in enumerate(range(0, len(values), rows)):
        end = min(len(values), start+rows)
        part = path.with_name(path.stem+'-part'+str(number).zfill(3)+'.npy.gz')
        if part.exists():
            raise FileExistsError('A complete or partial field already uses this prefix')
        with part.open('xb') as stream:
            with gzip.GzipFile(filename='', mode='wb', fileobj=stream, mtime=0) as zipped:
                np.save(zipped, np.ascontiguousarray(values[start:end]), allow_pickle=False)
        if part.stat().st_size >= 5_000_000:
            raise ValueError('A stored chunk exceeded the repository limit')
        entries.append(dict(file=part.name, start=start, end=end,
                            bytes=part.stat().st_size, sha256=sha(part)))
    result = dict(schema='complete-geometry-chunks-v1', dtype='float64',
                  shape=list(values.shape), chunks=entries, complete=True)
    path.write_text(json.dumps(result, indent=2)+'\n')
    return result


def read_chunks(path, destination=None):
    """Return all rows, optionally writing directly into an existing memmap."""
    path = Path(path)
    record = json.loads(path.read_text())
    shape = tuple(record['shape'])
    if (record.get('schema') != 'complete-geometry-chunks-v1'
            or record.get('dtype') != 'float64' or not record.get('complete')
            or len(shape) != 3 or shape[2] != 3):
        raise ValueError('Incomplete or incompatible field manifest')
    output = np.empty(shape, dtype=np.float64) if destination is None else destination
    if output.shape != shape or output.dtype != np.float64:
        raise ValueError('The destination does not match the complete field')
    previous = 0
    for item in record['chunks']:
        name = item['file']
        if Path(name).name != name or item['start'] != previous or not previous < item['end'] <= shape[0]:
            raise ValueError('Noncontiguous or unsafe chunk entry')
        part = path.with_name(name)
        if part.stat().st_size != item['bytes'] or sha(part) != item['sha256']:
            raise ValueError('A complete field chunk changed')
        with gzip.open(part, 'rb') as stream:
            data = np.load(stream, allow_pickle=False)
        if (data.shape != (item['end']-previous, *shape[1:])
                or data.dtype != np.float64 or not np.isfinite(data).all()):
            raise ValueError('A chunk does not match its complete row range')
        output[previous:item['end']] = data
        previous = item['end']
    if previous != shape[0]:
        raise ValueError('The manifest omits final radial rows')
    return output
