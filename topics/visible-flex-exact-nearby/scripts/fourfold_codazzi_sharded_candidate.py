#!/usr/bin/env python3
"""Lossless byte shards for complete exact finite Codazzi candidates.

Each separately gzipped shard contains a consecutive byte range of the
original complete npz.gz. Concatenation after one decompression reconstructs
that original file bit for bit. This changes storage only, never a Fourier
coefficient, radial endpoint, mean, polynomial or source identity.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np
from fourfold_phase_codazzi_continuation_validate import ExactCandidate
from fourfold_phase_codazzi_dense_candidate import DenseCandidate


def digest(data):
    return hashlib.sha256(data).hexdigest()


def candidate_bytes(path):
    path=Path(path);raw=path.read_bytes()
    if raw[:2]==b'\x1f\x8b':return raw
    manifest=json.loads(raw)
    if manifest.get('kind')!='exact_full_finite_Codazzi_candidate_byte_shards':
        raise ValueError('unknown complete candidate storage representation')
    result=[];cursor=0
    for row in manifest['shards']:
        relative=Path(row['file'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('candidate shard leaves its declared local directory')
        stored=(path.parent/relative).read_bytes()
        if len(stored)!=row['compressed_bytes'] or digest(stored)!=row['compressed_sha256']:
            raise ValueError('candidate shard storage identity changed')
        value=gzip.decompress(stored)
        if row['offset']!=cursor or len(value)!=row['payload_bytes'] or digest(value)!=row['payload_sha256']:
            raise ValueError('candidate shard range or payload changed')
        result.append(value);cursor+=len(value)
    raw=b''.join(result)
    if len(raw)!=manifest['original_bytes'] or digest(raw)!=manifest['original_sha256']:
        raise ValueError('complete original candidate was not recovered exactly')
    return raw


def load_arrays(path):
    raw=candidate_bytes(path)
    with np.load(io.BytesIO(gzip.decompress(raw)),allow_pickle=False) as z:
        arrays={k:z[k].copy() for k in z.files}
    return arrays,raw


class ShardedExactCandidate(ExactCandidate):
    """Same exact finite object and inherited polynomial evaluator."""
    def __init__(self,path,target):
        self.path=Path(path);saved,raw=load_arrays(path)
        self.original_payload_sha256=digest(raw)
        self.times=[Fraction.from_float(float(x)) for x in saved['time_nodes']]
        self.ends=saved['positive_endpoint_coefficients']
        self.corrections=saved['positive_dense_corrections']
        self.metadata=json.loads(str(saved['metadata']))
        self.target=target;self.degree=self.ends.shape[1]-1;self.grid=target.product_grid
        if self.grid<=2*self.degree:raise ValueError('candidate support reaches grid boundary')
        if self.times[0]!=0 or any(b<=a for a,b in zip(self.times,self.times[1:])):
            raise ValueError('candidate has an invalid exact radial partition')
        if list(map(str,self.times))!=self.metadata['time_nodes_exact_fractions']:
            raise ValueError('candidate exact dyadic time metadata changed')
        if (self.ends.shape!=(len(self.times),self.degree+1,2)
            or self.corrections.shape!=(len(self.times)-1,6,self.degree+1,2)):
            raise ValueError('candidate omitted a complete dense coefficient array')
        for values in (self.ends,self.corrections):
            if not np.all(np.isfinite(values)) or np.any(values[...,0,:].imag!=0):
                raise ValueError('candidate contains a nonfinite coefficient or nonreal mean')
        if not np.all(self.ends[0,:,0]==0):raise ValueError('initial B must be exactly zero')
        self.frequencies=4*np.asarray([j if j<self.grid//2 else j-self.grid for j in range(self.grid)])
        self.pieces=len(self.times)-1


class ShardedDenseCandidate(DenseCandidate):
    def __init__(self,path):
        self.path=Path(path);self.data,raw=load_arrays(path)
        self.original_payload_sha256=digest(raw)
        self.nodes=self.data['time_nodes'];self.endpoints=self.data['positive_endpoint_coefficients']
        self.corrections=self.data['positive_dense_corrections']
        self.metadata=json.loads(str(self.data['metadata']));self.grid=int(self.metadata['angular_grid'])


def pack(source,output,chunk_bytes):
    source,output=Path(source),Path(output)
    if output.exists():raise FileExistsError('refusing to overwrite a complete candidate manifest')
    if chunk_bytes<=0 or chunk_bytes>4*1024*1024:raise ValueError('positive byte chunks at most 4 MiB required')
    saved,raw=load_arrays(source);metadata=json.loads(str(saved['metadata']))
    if metadata.get('kind')!='exact_finite_piecewise_degree7_Fourier_BC_candidate':
        raise ValueError('the full exact dense candidate is required')
    rows=[]
    for i,offset in enumerate(range(0,len(raw),chunk_bytes)):
        value=raw[offset:offset+chunk_bytes]
        stored=gzip.compress(value,compresslevel=6,mtime=0)
        path=output.with_name(output.stem+f'.part-{i:03d}.gz')
        if path.exists():raise FileExistsError('candidate shard already exists')
        if len(stored)>5*1024*1024:raise ValueError('individual candidate shard exceeds repository cap')
        path.write_bytes(stored)
        rows.append(dict(file=path.name,offset=offset,payload_bytes=len(value),payload_sha256=digest(value),
                         compressed_bytes=len(stored),compressed_sha256=digest(stored)))
    manifest=dict(kind='exact_full_finite_Codazzi_candidate_byte_shards',complete=True,
        storage_only=True,accuracy_certified=False,continuation_certified=False,
        original_bytes=len(raw),original_sha256=digest(raw),original_metadata=metadata,
        number_of_pieces=len(saved['time_nodes'])-1,
        full_positive_endpoint_shape=list(saved['positive_endpoint_coefficients'].shape),
        full_dense_corrections_shape=list(saved['positive_dense_corrections'].shape),
        all_mean_modes_and_exact_shared_endpoints_retained=True,
        source_sha256=digest(Path(__file__).read_bytes()),shards=rows)
    output.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    if candidate_bytes(output)!=raw:raise ValueError('byte-for-byte complete reconstruction failed')
    print(dict(manifest=str(output),parts=len(rows),original_bytes=len(raw),original_sha256=digest(raw),
               complete_byte_identity_verified=True),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pack',type=Path,required=True)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--chunk-bytes',type=int,default=4*1024*1024)
    a=ap.parse_args();pack(a.pack,a.manifest,a.chunk_bytes)
