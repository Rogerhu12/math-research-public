#!/usr/bin/env python3
"""Define one continuous dyadic Fourier/Bernstein reference from shared rays.

Accepts the frozen shared-grid driver's 32-step chunks. The final binary64
coefficients define the reference exactly; interpolation accuracy is not a
proof assumption. Actual residuals must be validated on this definition.
"""
from __future__ import annotations
import argparse
import gzip
import io
import json
import math
from pathlib import Path
import re
import numpy as np
from fourfold_dense_fourier_reference import sha, dense_power, affine_coefficients, exact_time


def load(path):
    payload=path.read_bytes()
    if path.suffix=='.gz':payload=gzip.decompress(payload)
    with np.load(io.BytesIO(payload),allow_pickle=False) as z:
        return {key:z[key].copy() for key in z.files}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--trace-dir',type=Path,required=True)
    ap.add_argument('--leg',choices=['forward','backward'],required=True)
    ap.add_argument('--rays',type=int,required=True)
    ap.add_argument('--degree',type=int)
    ap.add_argument('--segments-per-file',type=int,default=24)
    ap.add_argument('--previous-reference',type=Path,help='Optional previous leg: share its final U exactly, reset the new L normally')
    ap.add_argument('--out-dir',type=Path,required=True)
    args=ap.parse_args()
    N=args.rays;K=N//2 if args.degree is None else args.degree
    if not 1<=K<=N//2 or args.segments_per_file<1:raise ValueError('invalid dimensions')
    pattern=re.compile(r'block_0000_'+args.leg+r'\.part(\d+)\.npz(?:\.gz)?$')
    files=sorted((int(m.group(1)),p) for p in args.trace_dir.iterdir() if (m:=pattern.fullmatch(p.name)))
    if not files:raise ValueError('no shared-grid branch chunks')
    cursor=0;identity=None;times=[];inputs=[];total=None
    for first,path in files:
        d=load(path);meta=json.loads(str(d['metadata']));ident=meta['identity']
        if identity is None:identity=ident;total=meta['branch_total_accepted_segments']
        if ident!=identity or meta['branch_total_accepted_segments']!=total:
            raise ValueError('mixed branch identity or total count')
        count=len(d['dense_h'])
        if first!=cursor or meta['first_accepted_segment']!=first or meta['accepted_segment_stop']!=first+count:
            raise ValueError('chunks do not tile accepted steps')
        if ident['rays']!=N or ident['block_size']!=N or d['dense_F'].shape!=(count,7,3,N):
            raise ValueError('the whole initial grid must use the same time mesh')
        if meta['state_rows']!=['theta','log_J','fixed_x_parameter_variation'] or d['dense_y_old'].shape!=(count,3,N):
            raise ValueError('unexpected state convention')
        if len(d['accepted_tau'])!=count+1 or d['accepted_state'].shape!=(count+1,3,N):
            raise ValueError('unexpected accepted-grid shape')
        if not all(np.all(np.isfinite(d[key])) for key in ['dense_h','dense_F','dense_y_old','accepted_tau']):
            raise ValueError('nonfinite trace values')
        if np.any(d['dense_h']==0):raise ValueError('zero source time interval')
        if times and times[-1]!=float(d['accepted_tau'][0]):raise ValueError('chunk time endpoints disagree')
        times.extend(map(float,d['accepted_tau'] if not times else d['accepted_tau'][1:]))
        inputs.append(dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,
                           first_accepted_segment=first,segment_count=count))
        cursor+=count
    direction=1 if args.leg=='forward' else -1
    if cursor!=total or identity['start']!=-direction*math.pi/2 or identity['finish']!=direction*math.pi/2:
        raise ValueError('incomplete full turn interval')
    if times[0]!=identity['start'] or times[-1]!=identity['finish'] or not np.all(direction*np.diff(times)>0):
        raise ValueError('branch time coverage is not exact and monotone')
    exact_times=[exact_time(t) for t in times]
    exact_times[0]=exact_time(times[0],-direction);exact_times[-1]=exact_time(times[-1],direction)
    prior_U=None;previous_metadata=None
    if args.previous_reference:
        prior=json.loads(args.previous_reference.read_text())
        if not prior.get('complete') or prior['time_basis']!='bernstein' or prior['Fourier_degree']!=K:
            raise ValueError('incompatible previous reference')
        if prior['exact_time_endpoints'][-1]!=exact_times[0] or prior['total_initial_grid_nodes']!=N:
            raise ValueError('previous endpoint/grid does not match')
        for key in ['source_sha256','dyadic_conjugacy_sha256','root_certificate_sha256','exact_delta_fraction']:
            if prior['trace_identity'][key]!=identity[key]:raise ValueError('previous reference belongs to a different object')
        shard=prior['shards'][-1];path=args.previous_reference.parent/shard['path']
        if sha(path)!=shard['sha256']:raise ValueError('previous coefficient hash mismatch')
        saved=load(path);prior_U=saved['coefficient_real'][-1,-1,0]+1j*saved['coefficient_imag'][-1,-1,0]
        previous_metadata=dict(path=str(args.previous_reference),sha256=sha(args.previous_reference),
                               shared_U_at_junction=True,shared_L_at_junction=False)
    args.out_dir.mkdir(parents=True,exist_ok=True)
    manifest_path=args.out_dir/'manifest.json'
    if manifest_path.exists():raise ValueError('use a fresh output directory, do not overwrite a frozen definition')
    source_hash=sha(__file__)
    shards=[];buffer=[];buffer_start=0;previous=None;index=0
    matrix=np.asarray([[math.comb(i,j)/math.comb(7,j) if j<=i else 0. for j in range(8)] for i in range(8)])
    def save():
        nonlocal buffer,buffer_start
        if not buffer:return
        values=np.asarray(buffer,dtype=np.complex128)
        meta=dict(start_segment=buffer_start,segment_count=len(buffer),
                  exact_times=exact_times[buffer_start:buffer_start+len(buffer)+1],source_sha256=source_hash)
        output=io.BytesIO();np.savez(output,coefficient_real=values.real,coefficient_imag=values.imag,
                                   metadata=np.array(json.dumps(meta,sort_keys=True)))
        payload=gzip.compress(output.getvalue(),mtime=0)
        if len(payload)>5_000_000:raise ValueError('reduce shard size below the repository file limit')
        path=args.out_dir/f'segments_{buffer_start:05d}.npz.gz';path.write_bytes(payload)
        shards.append(dict(path=path.name,sha256=sha(path),bytes=len(payload),
                           start_segment=buffer_start,segment_count=len(buffer)))
        buffer_start+=len(buffer);buffer=[]
    for _,path in files:
        d=load(path)
        for j in range(len(d['dense_h'])):
            powers=dense_power(d['dense_F'][j,:,:2,:],d['dense_y_old'][j,:2,:])
            start=(times[index]-float(d['dense_t_old'][j]))/float(d['dense_h'][j])
            step=(times[index+1]-times[index])/float(d['dense_h'][j])
            values=affine_coefficients(powers,start,step)
            values[0,0]-=2*np.pi*np.arange(N)/(4*N)
            coefficient=(np.fft.rfft(values,axis=-1)/N)[:,:,:K+1].copy()
            coefficient[:,:,0]=coefficient[:,:,0].real
            if N%2==0 and K==N//2:coefficient[:,:,-1]=coefficient[:,:,-1].real/2
            coefficient=np.einsum('ij,jfk->ifk',matrix,coefficient)
            if previous is not None:coefficient[0]=previous
            elif prior_U is not None:coefficient[0,0]=prior_U
            if not np.all(np.isfinite(coefficient)):raise ValueError('nonfinite constructed coefficient')
            previous=coefficient[-1].copy();buffer.append(coefficient);index+=1
            if len(buffer)>=args.segments_per_file:save()
    save()
    report=dict(kind='defined_dyadic_Fourier_polynomial_reference',complete=True,source_sha256=source_hash,
        constructor_dependency_sha256=sha(Path(__file__).with_name('fourfold_dense_fourier_reference.py')),
        leg=args.leg,time_orientation=direction,trace_identity=identity,total_initial_grid_nodes=N,
        Fourier_degree=K,time_degree=7,time_basis='bernstein',fields=['U','L'],
        continuous_by_shared_endpoint_coefficients=True,numpy_version=np.__version__,
        exact_definition='Y(tau,x)=x/4+U(tau,x), q=exp(L); exact rational/pi time endpoints define the Bernstein local coordinate',
        coefficient_convention='positive Fourier coefficients saved; negative conjugates; real mean; exact dyadic binary64 values',
        numerical_construction='shared dense time mesh, floating composition and FFT then exact saved coefficient definition',
        exact_time_endpoints=exact_times,input_traces=inputs,previous_reference=previous_metadata,
        segment_count=index,shards=shards,bytes_total=sum(s['bytes'] for s in shards),
        limitations=['This definition does not certify interpolation, ODE residuals, true flow or Fourier alias error.',
            'The geometric function is unchanged by numerical knot representatives; all actual spline knots remain relevant to validation.',
            'The source trajectories are coefficient-selection data. The exact final dyadic reference requires its own residual proof.'])
    manifest_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['complete','leg','segment_count','Fourier_degree','bytes_total']},indent=2),flush=True)
    print('manifest_sha256='+sha(manifest_path),flush=True)


if __name__=='__main__':main()
