#!/usr/bin/env python3
"""Complete exact finite auxiliary weights, with their own storage identity.

The degree-seven radial polynomial algebra is shared with the earlier BC
candidate.  These objects are explicitly weights, have initial value (1,1),
and neither claim to be BC candidates nor inherit their initial constraints.
Every exact dyadic coefficient and real mean is retained in byte shards.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction
import gzip,hashlib,io,json
from pathlib import Path
import numpy as np
from fourfold_phase_codazzi_dense_candidate import polynomial_jet,full_coefficients
from fourfold_phase_codazzi_continuation_validate import ExactCandidate


KIND='exact_finite_piecewise_degree7_Fourier_comparison_weights'
STORAGE='exact_full_finite_positive_comparison_weight_byte_shards'
def digest(raw):return hashlib.sha256(raw).hexdigest()


def weight_bytes(path):
    path=Path(path);raw=path.read_bytes()
    if raw[:2]==b'\x1f\x8b':return raw
    manifest=json.loads(raw)
    if manifest.get('kind')!=STORAGE or not manifest.get('complete'):
        raise ValueError('unknown complete finite weight storage')
    output=[];cursor=0
    for row in manifest['shards']:
        p=Path(row['file'])
        if p.is_absolute() or '..' in p.parts:raise ValueError('weight shard leaves its local directory')
        stored=(path.parent/p).read_bytes()
        if len(stored)!=row['compressed_bytes'] or digest(stored)!=row['compressed_sha256']:
            raise ValueError('weight shard storage changed')
        value=gzip.decompress(stored)
        if row['offset']!=cursor or len(value)!=row['payload_bytes'] or digest(value)!=row['payload_sha256']:
            raise ValueError('weight shard interval changed')
        output.append(value);cursor+=len(value)
    raw=b''.join(output)
    if len(raw)!=manifest['original_bytes'] or digest(raw)!=manifest['original_sha256']:
        raise ValueError('full weight byte identity mismatch')
    return raw


def arrays(path):
    raw=weight_bytes(path)
    with np.load(io.BytesIO(gzip.decompress(raw)),allow_pickle=False) as z:
        values={k:z[k].copy() for k in z.files}
    return values,raw


def validate(values):
    meta=json.loads(str(values['metadata']))
    nodes=values['time_nodes'];ends=values['positive_endpoint_coefficients']
    cc=values['positive_dense_corrections'];degree=ends.shape[1]-1
    if meta.get('kind')!=KIND:raise ValueError('a complete finite weight object is required')
    if nodes[0]!=0 or np.any(np.diff(nodes)<=0):raise ValueError('invalid weight radial partition')
    if list(map(lambda x:str(Fraction.from_float(float(x))),nodes))!=meta['time_nodes_exact_fractions']:
        raise ValueError('exact dyadic weight time metadata differs')
    if ends.shape!=(len(nodes),degree+1,2) or cc.shape!=(len(nodes)-1,6,degree+1,2):
        raise ValueError('incomplete finite weight coefficient arrays')
    for x in (ends,cc):
        if not np.all(np.isfinite(x)) or np.any(x[...,0,:].imag!=0):
            raise ValueError('nonfinite weight or nonreal weight mean')
    initial=np.zeros_like(ends[0]);initial[0]=1
    if not np.array_equal(ends[0],initial):raise ValueError('both initial weights must be exactly one')
    return meta


class DenseWeightCandidate:
    def __init__(self,path):
        self.path=Path(path);self.data,raw=arrays(path);self.metadata=validate(self.data)
        self.original_payload_sha256=digest(raw)
        self.nodes=self.data['time_nodes'];self.ends=self.data['positive_endpoint_coefficients']
        self.corrections=self.data['positive_dense_corrections'];self.grid=int(self.metadata['angular_grid'])

    def evaluate(self,r,angles=None):
        if not self.nodes[0]<=r<=self.nodes[-1]:raise ValueError('weight point outside exact finite interval')
        piece=min(len(self.nodes)-2,bisect_right(self.nodes,float(r))-1)
        h=self.nodes[piece+1]-self.nodes[piece];x=(r-self.nodes[piece])/h
        v,dx=polynomial_jet(self.ends[piece],self.ends[piece+1],self.corrections[piece],x)
        angles=angles or 2*self.grid
        if angles<2*len(v):raise ValueError('finite weight Fourier support is truncated')
        full=full_coefficients(v,angles);rfull=full_coefficients(dx/h,angles)
        f=4*np.fft.fftfreq(angles,1/angles)
        sample=lambda c:(angles*np.fft.ifft(c,axis=0)).real
        return dict(piece=piece,W=sample(full),W_r=sample(rfull),W_theta=sample(1j*f[:,None]*full))


class ExactWeightCandidate:
    def __init__(self,path,target):
        self.path=Path(path);values,raw=arrays(path);self.metadata=validate(values)
        self.original_payload_sha256=digest(raw)
        self.times=[Fraction.from_float(float(x)) for x in values['time_nodes']]
        self.ends=values['positive_endpoint_coefficients'];self.corrections=values['positive_dense_corrections']
        self.degree=self.ends.shape[1]-1;self.target=target;self.grid=target.product_grid
        self.frequencies=4*np.asarray([j if j<self.grid//2 else j-self.grid for j in range(self.grid)])
        self.pieces=len(self.times)-1
        if self.grid<=2*self.degree:raise ValueError('finite weight support would alias')

    def polynomials(self,piece,left,right):
        # This is only a common exact polynomial evaluator.  Object identity,
        # full coefficient arrays and initial conditions are checked above.
        raw=ExactCandidate.polynomials(self,piece,left,right)
        return {'Wp'+k[1:] if k.startswith('B') else 'Wq'+k[1:]:v for k,v in raw.items()}


def pack(source,manifest_path,chunk_bytes=4*1024*1024):
    source=Path(source);manifest_path=Path(manifest_path)
    if manifest_path.exists():raise FileExistsError('new weight manifest required')
    values,raw=arrays(source);meta=validate(values)
    rows=[]
    for i,start in enumerate(range(0,len(raw),chunk_bytes)):
        payload=raw[start:start+chunk_bytes];stored=gzip.compress(payload,compresslevel=6,mtime=0)
        p=manifest_path.with_name(manifest_path.stem+f'.part-{i:03d}.gz')
        if p.exists() or len(stored)>5_000_000:raise ValueError('new weight shard under 5 MB required')
        p.write_bytes(stored)
        rows.append(dict(file=p.name,offset=start,payload_bytes=len(payload),payload_sha256=digest(payload),
                         compressed_bytes=len(stored),compressed_sha256=digest(stored)))
    out=dict(kind=STORAGE,complete=True,positivity_certified=False,continuation_certified=False,
        original_bytes=len(raw),original_sha256=digest(raw),original_metadata=meta,
        complete_endpoint_shape=list(values['positive_endpoint_coefficients'].shape),
        complete_dense_correction_shape=list(values['positive_dense_corrections'].shape),
        source_sha256=digest(Path(__file__).read_bytes()),shards=rows)
    manifest_path.write_text(json.dumps(out,indent=2)+'\n')
    if weight_bytes(manifest_path)!=raw:raise ValueError('complete exact weight reconstruction differs')
    return out
