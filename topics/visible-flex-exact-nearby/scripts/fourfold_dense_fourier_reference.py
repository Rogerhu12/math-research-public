#!/usr/bin/env python3
"""Define a finite, real Fourier x polynomial-time reference from dense rays.

This is a floating coefficient CONSTRUCTOR. Its saved binary64 coefficients
define exact dyadic real/imaginary numbers. No claim of exact interpolation,
ODE residual, alias control, or true flow is made. Those must be checked on
the final, explicitly defined reference. In the default Bernstein basis,
adjacent intervals share the exact same dyadic endpoint coefficients, so
the defined reference is continuous. The first and last times are exact
signed pi/2, not the binary64 integration endpoints used while constructing.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import re

import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dense_power(F,yold):
    """Floating construction only; final arrays, not this operation, define U/L."""
    result=np.zeros((1,)+yold.shape)
    for i,value in enumerate(reversed(F)):
        result[0]+=value
        new=np.zeros((len(result)+1,)+yold.shape)
        if i%2==0:new[1:]=result
        else:
            new[:-1]+=result;new[1:]-=result
        result=new
    result[0]+=yold
    return result


def affine_coefficients(coefficients,start,step):
    degree=len(coefficients)-1
    result=np.zeros_like(coefficients)
    for j in range(degree+1):
        for n in range(j,degree+1):
            result[j]+=coefficients[n]*math.comb(n,j)*start**(n-j)*step**j
    return result


def exact_time(value,end_sign=None):
    if end_sign is not None:return {'kind':'rational_multiple_of_pi','numerator':end_sign,'denominator':2}
    fraction=Fraction.from_float(float(value))
    return {'kind':'rational','numerator':str(fraction.numerator),'denominator':str(fraction.denominator)}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trace-dir',type=Path,required=True)
    ap.add_argument('--leg',choices=['forward','backward'],required=True)
    ap.add_argument('--rays',type=int,required=True)
    ap.add_argument('--degree',type=int,help='Fourier cutoff, default floor(rays/2)')
    ap.add_argument('--basis',choices=['bernstein','power'],default='bernstein')
    ap.add_argument('--segments-per-file',type=int,default=24)
    ap.add_argument('--out-dir',type=Path,required=True)
    args=ap.parse_args()
    N=args.rays;K=N//2 if args.degree is None else args.degree
    if not 1<=K<=N//2 or args.segments_per_file<1:raise ValueError('invalid finite reference dimensions')
    pattern=re.compile(r'block_(\d+)_'+args.leg+r'\.npz(?:\.gz)?$')
    files=[]
    for path in args.trace_dir.iterdir():
        match=pattern.fullmatch(path.name)
        if match:files.append((int(match.group(1)),path))
    files.sort();blocks=[];cursor=0;identity=None;inputs=[]
    for first,path in files:
        if first!=cursor:raise ValueError('trace blocks do not tile the complete initial grid')
        payload=path.read_bytes()
        if path.suffix=='.gz':payload=gzip.decompress(payload)
        with np.load(io.BytesIO(payload),allow_pickle=False) as stored:
            data={key:stored[key].copy() for key in stored.files}
        meta=json.loads(str(data['metadata']));ident=meta['identity']
        if identity is None:identity=ident
        if ident!=identity or ident['rays']!=N:raise ValueError('mixed trace objects/configurations')
        if meta['state_rows']!=['theta','log_J','fixed_x_parameter_variation']:
            raise ValueError('unexpected state ordering')
        n=len(data['initial_angles']);steps=len(data['dense_h'])
        if data['dense_F'].shape!=(steps,7,3,n) or data['dense_y_old'].shape!=(steps,3,n):
            raise ValueError('unexpected saved polynomial shape')
        direction=1 if ident['finish']>ident['start'] else -1
        if not np.all(direction*np.diff(data['accepted_tau'])>0):raise ValueError('nonmonotone accepted grid')
        if data['accepted_tau'][0]!=ident['start'] or data['accepted_tau'][-1]!=ident['finish']:
            raise ValueError('trace does not span the whole branch')
        if not all(np.all(np.isfinite(data[key])) for key in ['dense_h','dense_F','dense_y_old','accepted_tau']):
            raise ValueError('nonfinite saved value')
        if np.any(data['dense_h']==0):raise ValueError('zero-width source interval')
        power=np.asarray([dense_power(data['dense_F'][i,:,:2,:],data['dense_y_old'][i,:2,:]) for i in range(steps)])
        blocks.append(dict(first=first,count=n,data=data,power=power))
        cursor+=n
        inputs.append(dict(path=str(path),sha256=sha(path),first_node=first,node_count=n,segments=steps))
    if cursor!=N or not files:raise ValueError('incomplete initial grid')
    expected_start=-math.pi/2 if args.leg=='forward' else math.pi/2
    if identity['start']!=expected_start or identity['finish']!=-expected_start:
        raise ValueError('this constructor expects the full normalized turn interval')
    direction=1 if args.leg=='forward' else -1
    times=np.unique(np.concatenate([b['data']['accepted_tau'] for b in blocks]))[::direction]
    if not np.all(direction*np.diff(times)>0):raise ValueError('invalid common grid')
    exact_times=[exact_time(t) for t in times]
    exact_times[0]=exact_time(times[0],-direction);exact_times[-1]=exact_time(times[-1],direction)
    args.out_dir.mkdir(parents=True,exist_ok=True)
    manifest_path=args.out_dir/'manifest.json'
    if manifest_path.exists():raise ValueError('use a new output directory; never overwrite a frozen reference')
    common=dict(kind='defined_dyadic_Fourier_polynomial_reference',source_sha256=sha(__file__),
        leg=args.leg,time_orientation=direction,trace_identity=identity,
        total_initial_grid_nodes=N,Fourier_degree=K,time_degree=7,fields=['U','L'],
        time_basis=args.basis,continuous_by_shared_endpoint_coefficients=args.basis=='bernstein',
        numpy_version=np.__version__,
        exact_definition='Y(tau,x)=x/4+U(tau,x), q(tau,x)=exp(L(tau,x)); u=(tau-left)/(right-left) uses exact time objects',
        coefficient_convention='positive Fourier coefficients stored; negative coefficients conjugate; zero frequency real',
        numerical_construction='floating affine composition and rFFT; stored binary64 values then DEFINE exact rational coefficients',
        exact_time_endpoints=exact_times,input_traces=inputs,
        limitations=['No exact interpolation of the source dense polynomials is asserted',
            'No ODE residual, true-flow tube, field tail, parameter variation or Wiener error is certified',
            'Outer branch endpoints are exact pi/2; binary source times only guide coefficient selection',
            'Discarded modes or construction rounding are absorbed in the definition and must be caught by subsequent actual residual checks'])
    shards=[];buffer=[];buffer_start=0;previous_endpoint=None
    bernstein_matrix=np.asarray([[math.comb(i,j)/math.comb(7,j) if j<=i else 0.
                                 for j in range(8)] for i in range(8)])
    def save_buffer():
        nonlocal buffer,buffer_start
        if not buffer:return
        coefficient=np.asarray(buffer,dtype=np.complex128)
        local=dict(start_segment=buffer_start,segment_count=len(buffer),
                   exact_times=exact_times[buffer_start:buffer_start+len(buffer)+1],
                   source_sha256=common['source_sha256'])
        stream=io.BytesIO()
        np.savez(stream,coefficient_real=coefficient.real,coefficient_imag=coefficient.imag,
                 metadata=np.array(json.dumps(local,sort_keys=True)))
        payload=gzip.compress(stream.getvalue(),mtime=0)
        if len(payload)>5_000_000:raise ValueError('reduce segments-per-file below the 5MB file limit')
        path=args.out_dir/f'segments_{buffer_start:05d}.npz.gz'
        path.write_bytes(payload)
        shards.append(dict(path=path.name,sha256=sha(path),bytes=path.stat().st_size,
                           start_segment=buffer_start,segment_count=len(buffer)))
        buffer_start+=len(buffer);buffer=[]
    for segment,(left,right) in enumerate(zip(times[:-1],times[1:])):
        values=np.zeros((8,2,N))
        for block in blocks:
            d=block['data'];oriented=direction*d['accepted_tau']
            old=int(np.searchsorted(oriented,direction*left,side='right')-1)
            if old<0 or old>=len(d['dense_h']) or direction*right>oriented[old+1]:
                raise ValueError('common segment crosses an unaccounted dense breakpoint')
            start=(float(left)-float(d['dense_t_old'][old]))/float(d['dense_h'][old])
            step=(float(right)-float(left))/float(d['dense_h'][old])
            new=affine_coefficients(block['power'][old],start,step)
            values[:,:,block['first']:block['first']+block['count']]=new
        values[0,0]-=(2*np.pi*np.arange(N)/N)/4
        coefficients=np.fft.rfft(values,axis=-1)/N
        coefficients=coefficients[:,:,:K+1].copy()
        coefficients[:,:,0]=coefficients[:,:,0].real
        if N%2==0 and K==N//2:coefficients[:,:,-1]=coefficients[:,:,-1].real/2
        if args.basis=='bernstein':
            coefficients=np.einsum('ij,jfk->ifk',bernstein_matrix,coefficients)
            if previous_endpoint is not None:coefficients[0]=previous_endpoint
            previous_endpoint=coefficients[-1].copy()
        if not np.all(np.isfinite(coefficients)):raise ValueError('nonfinite reference coefficient')
        buffer.append(coefficients)
        if len(buffer)>=args.segments_per_file:save_buffer()
    save_buffer()
    report=dict(**common,complete=True,segment_count=len(times)-1,shards=shards,
                bytes_total=sum(s['bytes'] for s in shards))
    manifest_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['kind','complete','leg','total_initial_grid_nodes','Fourier_degree','segment_count','bytes_total']},indent=2))
    print('manifest_sha256='+sha(manifest_path),flush=True)


if __name__=='__main__':main()
