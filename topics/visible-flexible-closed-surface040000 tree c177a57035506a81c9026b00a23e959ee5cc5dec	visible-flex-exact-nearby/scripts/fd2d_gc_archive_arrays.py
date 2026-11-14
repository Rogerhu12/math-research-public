"""Lossless finite-field storage below the repository's single-file limit.

Native defining mesh/value/first/parameter arrays stay in the main NPZ.
If an entire diagnostic archive is too large, other arrays are stored in
numbered flat pieces. The returned complete_arrays index records every
array's original shape, dtype and binary hash. No numerical values change.
"""
import gzip, hashlib, io, json
from pathlib import Path
import numpy as np

LIMIT = 5_000_000
CORE = {'mesh', 'values', 'first', 'parameters', 'physical_s', 'radial_scale'}


def identity(path):
    p = Path(path); b = p.read_bytes()
    return dict(path=str(p.resolve()), bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


def encoded(arrays):
    stream = io.BytesIO(); np.savez_compressed(stream, **arrays)
    data = stream.getvalue()
    return (gzip.compress(data, compresslevel=6, mtime=0), '.gz') if len(data)>1_000_000 else (data, '')


def write(path, arrays):
    data, suffix = encoded(arrays); path = Path(str(path)+suffix)
    if len(data)>=LIMIT:
        raise ValueError('A single defining-array part is still too large')
    if path.exists():
        raise FileExistsError(path)
    tmp = path.with_name(path.name+'.tmp'); tmp.write_bytes(data); tmp.replace(path)
    return identity(path)


def save_npz(path, **arrays):
    path = Path(path); data, suffix = encoded(arrays)
    if len(data)<LIMIT:
        q = Path(str(path)+suffix)
        if q.exists():
            raise FileExistsError(q)
        tmp = q.with_name(q.name+'.tmp'); tmp.write_bytes(data); tmp.replace(q)
        return identity(q)
    primary = {k:v for k,v in arrays.items() if k in CORE}
    index = dict(schema='fd2d-lossless-auxiliary-arrays-v1', arrays={})
    for key, value in arrays.items():
        value = np.asarray(value); raw = np.ascontiguousarray(value)
        entry = dict(shape=list(value.shape), dtype=value.dtype.str,
            binary_sha256=hashlib.sha256(raw.tobytes()).hexdigest())
        if key in primary:
            entry['storage'] = 'main_npz'
        else:
            flat = raw.reshape(-1); count = max(1, 3_000_000//value.dtype.itemsize)
            parts = []
            for number, start in enumerate(range(0,len(flat),count),1):
                end = min(start+count,len(flat))
                part = path.with_name(path.stem+'-aux-'+key+'-'+str(number).zfill(3)+'.npz')
                row = write(part, {'values':flat[start:end]})
                row.update(start=start, end=end); parts.append(row)
            entry.update(storage='flat_parts', parts=parts)
        index['arrays'][key] = entry
    primary['__fd2d_auxiliary_arrays__'] = np.array(json.dumps(index,sort_keys=True))
    result = write(path, primary)
    result.update(complete_arrays=index, defining_arrays_unchanged=True,
                  logical_archive_is_complete=True)
    return result


def load_npz(path):
    """Restore all arrays, including optional diagnostic flat parts."""
    p = Path(path)
    def read(q):
        b=q.read_bytes(); b=gzip.decompress(b) if q.name.endswith('.gz') else b
        with np.load(io.BytesIO(b),allow_pickle=False) as data:
            return {k:data[k].copy() for k in data.files}
    result=read(p); metadata=result.pop('__fd2d_auxiliary_arrays__',None)
    if metadata is None:
        return result
    index=json.loads(str(metadata))
    for key, row in index['arrays'].items():
        if row['storage']=='flat_parts':
            values=[]
            for part in row['parts']:
                original=Path(part['path']); local=p.parent/original.name
                q=local if local.exists() else original
                if identity(q)['sha256']!=part['sha256']:
                    raise ValueError('Changed auxiliary array part: '+str(q))
                values.append(read(q)['values'])
            result[key]=np.concatenate(values).reshape(row['shape'])
        value=result[key]
        if value.dtype.str!=row['dtype'] or hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()!=row['binary_sha256']:
            raise ValueError('Logical array did not reconstruct exactly: '+key)
    return result
