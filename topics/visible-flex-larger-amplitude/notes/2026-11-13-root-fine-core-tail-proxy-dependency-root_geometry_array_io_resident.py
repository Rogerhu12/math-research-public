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


def write_chunks(path, values, release=lambda value: None, observe=lambda: None):
    path = Path(path)
    resident_values = values
    values = np.asarray(values)
    if (path.exists() or path.suffix != '.json' or values.dtype != np.float64
            or values.ndim != 3 or values.shape[2] != 3):
        raise ValueError('Use a fresh JSON manifest for complete finite float64 fields')
    row_bytes = values.shape[1]*values.shape[2]*8
    rows = max(1, 4_000_000//row_bytes)
    if row_bytes > 4_000_000:
        raise ValueError('One complete angular row exceeds the storage budget')
    entries = []
    for number, start in enumerate(range(0, len(values), rows)):
        end = min(len(values), start+rows)
        if not np.isfinite(values[start:end]).all():
            raise ValueError('Nonfinite complete geometry chunk')
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
        release(resident_values)
        observe()
    result = dict(schema='complete-geometry-chunks-v1', dtype='float64',
                  shape=list(values.shape), chunks=entries, complete=True)
    path.write_text(json.dumps(result, indent=2)+'\n')
    return result

