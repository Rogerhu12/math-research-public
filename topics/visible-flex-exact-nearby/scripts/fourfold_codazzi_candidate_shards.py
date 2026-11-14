#!/usr/bin/env python3
"""Lossless, SHA-bound radial cubic shards below the repository file limit."""
from __future__ import annotations
import gzip,io,json
from hashlib import sha256
from pathlib import Path
import numpy as np
from fourfold_phase_codazzi_two_end_probe import load_candidate as load_single


def digest(path):return sha256(Path(path).read_bytes()).hexdigest()


def save_candidate(path,*,radial_nodes,piece_coefficients,initial_state,metadata):
    path=Path(path)
    if path.suffix!='.json':raise ValueError('the complete sharded candidate index must use .json')
    if path.exists():raise FileExistsError('refusing to overwrite a complete or failed candidate index')
    radial_nodes=np.asarray(radial_nodes,dtype=np.float64);coeff=np.asarray(piece_coefficients,dtype=np.float64)
    if coeff.ndim!=3 or coeff.shape[0]!=4 or coeff.shape[1]!=len(radial_nodes)-1:
        raise ValueError('expected the complete scipy radial cubic coefficient array')
    if np.any(np.diff(radial_nodes)<=0) or not np.all(np.isfinite(coeff)):
        raise ValueError('nonfinite or unordered cubic candidate')
    chunk=max(1,2_800_000//(4*coeff.shape[2]*8));parts=[]
    for count,left in enumerate(range(0,coeff.shape[1],chunk)):
        right=min(left+chunk,coeff.shape[1]);part=path.with_name(path.stem+f'-part{count:03d}.npz.gz')
        if part.exists():raise FileExistsError('refusing to overwrite a candidate polynomial shard')
        data=io.BytesIO();np.savez(data,radial_nodes=radial_nodes[left:right+1],piece_coefficients=coeff[:,left:right,:])
        with gzip.GzipFile(filename=str(part),mode='wb',mtime=0) as stream:stream.write(data.getvalue())
        if part.stat().st_size>5_000_000:raise ValueError('unexpected polynomial shard exceeds repository limit')
        parts.append(dict(file=part.name,sha256=digest(part),bytes=part.stat().st_size,
            first_interval=left,last_interval_exclusive=right,radial_left=float(radial_nodes[left]),radial_right=float(radial_nodes[right])))
    doc=dict(kind='complete_lossless_radial_cubic_shards_v1',metadata=json.loads(str(metadata)),
        polynomial_order='numpy/scipy PPoly descending local powers',coefficient_shape=list(coeff.shape),
        radial_nodes_count=len(radial_nodes),initial_state=np.asarray(initial_state,dtype=np.float64).tolist(),parts=parts)
    path.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')


def load_candidate(path):
    path=Path(path)
    if path.suffix!='.json':return load_single(path)
    doc=json.loads(path.read_text())
    if doc['kind']!='complete_lossless_radial_cubic_shards_v1':raise ValueError('unrecognized cubic shard index')
    nodes=[];coeff=[];endpoint=None;next_interval=0
    for item in doc['parts']:
        if Path(item['file']).name!=item['file']:raise ValueError('a shard filename must be local to its index')
        part=path.parent/item['file']
        if digest(part)!=item['sha256'] or part.stat().st_size!=item['bytes']:raise ValueError('a complete polynomial shard changed')
        data=np.load(io.BytesIO(gzip.decompress(part.read_bytes())),allow_pickle=False)
        r=data['radial_nodes'];c=data['piece_coefficients']
        if item['first_interval']!=next_interval or len(r)!=c.shape[1]+1 or np.any(np.diff(r)<=0):
            raise ValueError('lost polynomial interval coverage')
        if endpoint is not None and r[0].view(np.uint64)!=endpoint.view(np.uint64):
            raise ValueError('polynomial shards do not have the same exact double interface')
        if c.shape[0]!=4 or c.shape[2]!=doc['coefficient_shape'][2] or not np.all(np.isfinite(c)):
            raise ValueError('a polynomial shard has invalid coefficient shape or values')
        nodes.append(r if endpoint is None else r[1:]);coeff.append(c);endpoint=r[-1];next_interval=item['last_interval_exclusive']
    r=np.concatenate(nodes);c=np.concatenate(coeff,axis=1)
    if list(c.shape)!=doc['coefficient_shape'] or len(r)!=doc['radial_nodes_count']:
        raise ValueError('complete cubic shape check failed')
    return dict(radial_nodes=r,piece_coefficients=c,initial_state=np.asarray(doc['initial_state']),metadata=np.array(json.dumps(doc['metadata'])))
