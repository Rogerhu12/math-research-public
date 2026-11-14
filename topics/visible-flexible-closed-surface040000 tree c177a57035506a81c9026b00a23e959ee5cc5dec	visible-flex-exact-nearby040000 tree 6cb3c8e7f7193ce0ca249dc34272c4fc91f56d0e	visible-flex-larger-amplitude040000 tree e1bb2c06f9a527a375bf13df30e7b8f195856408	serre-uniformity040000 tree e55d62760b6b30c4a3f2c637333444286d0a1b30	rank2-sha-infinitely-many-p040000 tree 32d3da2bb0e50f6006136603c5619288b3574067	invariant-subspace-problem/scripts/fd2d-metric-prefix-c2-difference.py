#!/usr/bin/env python3
"""Continuous C2 difference bounds for two actual shared-Hermite prefixes.

The maps are compared at the same normalized radial coordinate x in [0,1]
and the same saved angular coordinate psi. Their exact rational knot union
is used; polynomial coefficients are subtracted before any Fourier norm.
All Cartesian angular derivatives include rotation of the cylindrical basis.

This supplies coordinate-jet bounds only. Converting them to the reference
induced metric, matching the same physical material chart, and covering tails
and caps are separate requirements. No global geometric transfer is asserted.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'

import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def identity(path):
    path=Path(path).resolve()
    return dict(file=str(path),bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


backend=module('fd2d_difference_metric_backend',HERE/'78718-prefix-metric-polynomial-storage-v1.py')
base=backend.base
I,qb=base.I,base.qbounds
_new_storage_read=base.storage.read_payload


def legacy_or_sharded_payload(path,verify_arrays=True):
    """Read either historical one-file bytes or the later lossless wrapper."""
    path=Path(path)
    meta=json.loads(path.read_text())
    if 'data_file' not in meta:
        return _new_storage_read(path,verify_arrays=verify_arrays)
    if 'data_storage' in meta:
        raise ValueError('Ambiguous defining payload metadata')
    data_path=path.parent/meta['data_file']
    payload=data_path.read_bytes()
    if hashlib.sha256(payload).hexdigest()!=meta['data_sha256']:
        raise ValueError('Historical defining payload hash differs')
    return meta,payload,[identity(data_path)]


base.storage.read_payload=legacy_or_sharded_payload


def load_geometry(path,label):
    """Retain each common-cut producer's actual definition and identity."""
    meta=json.loads(path.read_text())
    bindings=[identity(path)]
    original=base.ExactHermite
    try:
        if meta.get('representation')=='exact-common-cut-prefix':
            wanted=meta['common_cut_implementation_sha256']
            options=[p for p in HERE.glob('*common-cut*.py')
                     if identity(p)['sha256']==wanted]
            if len(options)!=1:
                raise ValueError('Cannot identify the defining common-cut producer')
            common=module('fd2d_difference_common_'+label,options[0])
            common.install(base)
            bindings.append(identity(options[0]))
        geom=base.ExactHermite(path)
    finally:
        base.ExactHermite=original
    if not hasattr(geom,'storage_bindings'):
        raise ValueError('No defining storage identity')
    bindings+=geom.storage_bindings
    if geom.x[0]!=0 or not geom.x[-1]>0:
        raise ValueError('Expected a zero-origin positive radial interval')
    geom.exact_length=Q.from_float(float(geom.x[-1]))
    geom.exact_mesh=[Q.from_float(float(v)) for v in geom.x]
    geom.unit_mesh=[v/geom.exact_length for v in geom.exact_mesh]
    return geom,bindings


def raw_power(geom,span,left,right,derivative):
    """Actual d^derivative/dx^derivative on one common rational interval."""
    length=geom.exact_mesh[span+1]-geom.exact_mesh[span]
    a=(geom.exact_length*left-geom.exact_mesh[span])/length
    b=geom.exact_length*(right-left)/length
    if not 0<=a<a+b<=1:
        raise ValueError('The common interval crosses a source knot')
    raw=geom.power[span,derivative:]
    factors=np.array([math.factorial(k)//math.factorial(k-derivative)
                      for k in range(derivative,6)],dtype=float)[:,None]
    raw=raw*factors*qb((geom.exact_length/length)**derivative)
    # Exact scalar affine coefficients, instead of dividing independently
    # rounded endpoint enclosures by a small source span.
    out=[]
    degree=5-derivative
    for k in range(degree+1):
        value=I(np.zeros(raw.lo.shape[1]))
        for j in range(k,degree+1):
            coefficient=Q(math.comb(j,k))*a**(j-k)*b**k
            if coefficient:
                value=value+raw[j]*qb(coefficient)
        out.append(value)
    return base.stack(out,0)


def pad_modes(power,old,new):
    if old==new:return power
    lo=np.zeros((power.lo.shape[0],3*new+2))
    hi=np.zeros_like(lo)
    lo[:,0],hi[:,0]=power.lo[:,0],power.hi[:,0]
    lo[:,-1],hi[:,-1]=power.lo[:,-1],power.hi[:,-1]
    for axis in range(3):
        source=slice(axis*old+1,(axis+1)*old+1)
        target=slice(axis*new+1,axis*new+old+1)
        lo[:,target],hi[:,target]=power.lo[:,source],power.hi[:,source]
    return I(lo,hi)


def components(power,modes,angular_derivative):
    """Real sin/cos coefficient lists for the full Cartesian derivative."""
    r0=power[:,0:1]
    z0=power[:,-1:]
    r,t,z=[power[:,axis*modes+1:(axis+1)*modes+1] for axis in range(3)]
    n=(3*np.arange(1,modes+1))[None,:]
    zero=I(np.zeros((power.lo.shape[0],1)))
    def join(a,b):
        return I(np.concatenate((a.lo,b.lo),axis=1),
                 np.concatenate((a.hi,b.hi),axis=1))
    if angular_derivative==0:
        return [join(r0,r),join(zero,t),join(z0,z)]
    if angular_derivative==1:
        return [join(zero,-r*n-t),join(r0,r+t*n),join(zero,-z*n)]
    if angular_derivative==2:
        return [join(-r0,-r*(n*n+1)-t*(2*n)),
                join(zero,-r*(2*n)-t*(n*n+1)),join(zero,-z*(n*n))]
    raise ValueError('Only derivatives of total order at most two are requested')


def norm_bound(power,modes,angular_derivative):
    """Bernstein hull in radius and finite Fourier l1 in angle."""
    bounds=[]
    for comp in components(power,modes,angular_derivative):
        bern=backend.interval_matmul(backend.bernstein_matrix(comp.lo.shape[0]-1),comp)
        by_frequency=np.maximum(abs(bern.lo),abs(bern.hi)).max(axis=0)
        bounds.append(backend.positive_sum_upper(by_frequency))
    vector=(I(bounds[0]).square()+I(bounds[1]).square()+I(bounds[2]).square()).sqrt()
    return dict(vector=float(vector.hi),cylindrical_components=bounds)


def rational_column(values):
    endpoints=[qb(v) for v in values]
    return I(np.array([v.lo for v in endpoints])[:,None],
             np.array([v.hi for v in endpoints])[:,None])


def raw_power_batch(geom,spans,intervals,derivative):
    lengths=[geom.exact_mesh[i+1]-geom.exact_mesh[i] for i in spans]
    offsets=[(geom.exact_length*l-geom.exact_mesh[i])/h
             for i,(l,r),h in zip(spans,intervals,lengths)]
    widths=[geom.exact_length*(r-l)/h for (l,r),h in zip(intervals,lengths)]
    if not all(0<=a<a+b<=1 for a,b in zip(offsets,widths)):
        raise ValueError('A batch restriction crosses a source knot')
    source=geom.power[spans,derivative:]
    factors=np.array([math.factorial(k)//math.factorial(k-derivative)
                      for k in range(derivative,6)],dtype=float)[None,:,None]
    scales=rational_column([(geom.exact_length/h)**derivative for h in lengths])
    source=source*factors*I(scales.lo[:,None,:],scales.hi[:,None,:])
    out=[]
    for k in range(6-derivative):
        value=I(np.zeros((len(spans),source.lo.shape[2])))
        for j in range(k,6-derivative):
            weights=[Q(math.comb(j,k))*a**(j-k)*b**k
                     for a,b in zip(offsets,widths)]
            if any(weights):value=value+source[:,j]*rational_column(weights)
        out.append(value)
    return base.stack(out,1)


def pad_batch(power,old,new):
    if old==new:return power
    lo=np.zeros((*power.lo.shape[:2],3*new+2));hi=np.zeros_like(lo)
    lo[:,:,0],hi[:,:,0]=power.lo[:,:,0],power.hi[:,:,0]
    lo[:,:,-1],hi[:,:,-1]=power.lo[:,:,-1],power.hi[:,:,-1]
    for axis in range(3):
        source=slice(axis*old+1,(axis+1)*old+1)
        target=slice(axis*new+1,axis*new+old+1)
        lo[:,:,target],hi[:,:,target]=power.lo[:,:,source],power.hi[:,:,source]
    return I(lo,hi)


def batch_norm_bounds(power,modes,angular_derivative):
    count,degree,_=power.lo.shape
    r0,z0=power[:,:,0:1],power[:,:,-1:]
    r,t,z=[power[:,:,axis*modes+1:(axis+1)*modes+1] for axis in range(3)]
    n=(3*np.arange(1,modes+1))[None,None,:]
    zero=I(np.zeros((count,degree,1)))
    def join(a,b):
        return I(np.concatenate((a.lo,b.lo),axis=2),
                 np.concatenate((a.hi,b.hi),axis=2))
    if angular_derivative==0:components=[join(r0,r),join(zero,t),join(z0,z)]
    elif angular_derivative==1:components=[join(zero,-r*n-t),join(r0,r+t*n),join(zero,-z*n)]
    elif angular_derivative==2:components=[join(-r0,-r*(n*n+1)-t*(2*n)),
        join(zero,-r*(2*n)-t*(n*n+1)),join(zero,-z*(n*n))]
    else:raise ValueError('Unsupported angle derivative')
    bounds=[]
    for component in components:
        flat=I(component.lo.transpose(1,0,2).reshape(degree,-1),
               component.hi.transpose(1,0,2).reshape(degree,-1))
        bern=backend.interval_matmul(backend.bernstein_matrix(degree-1),flat)
        lo=bern.lo.reshape(degree,count,modes+1).transpose(1,0,2)
        hi=bern.hi.reshape(degree,count,modes+1).transpose(1,0,2)
        magnitude=np.maximum(abs(lo),abs(hi)).max(axis=1)
        terms=modes+1;unit=Q(1,2**52)
        gamma=float(qb(terms*unit/(1-terms*unit)).hi)
        observed=np.sum(magnitude,axis=1,dtype=np.float64)
        upper=base.up(base.up(observed+terms*np.nextafter(0.,1.))/base.down(1-gamma))
        bounds.append(upper)
    vectors=(I(bounds[0]).square()+I(bounds[1]).square()+I(bounds[2]).square()).sqrt().hi
    return [dict(vector=float(vectors[i]),cylindrical_components=[float(b[i]) for b in bounds])
            for i in range(count)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--reference',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--rows',type=Path)
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--stop',type=int)
    ap.add_argument('--radial-subdivisions',type=int,default=1)
    ap.add_argument('--batch',type=int,default=64)
    ap.add_argument('--progress-every',type=int,default=1000)
    args=ap.parse_args()
    if args.out.exists() or (args.rows is not None and args.rows.exists()):
        raise FileExistsError('Select new output files')
    if args.radial_subdivisions<1 or args.batch<1:raise ValueError('Positive subdivisions and batch size required')
    started=time.monotonic()
    ref,ref_bindings=load_geometry(args.reference,'reference')
    new,new_bindings=load_geometry(args.candidate,'candidate')
    knots=sorted(set(ref.unit_mesh+new.unit_mesh))
    total=len(knots)-1
    stop=total if args.stop is None else min(total,args.stop)
    if not 0<=args.start<stop:raise ValueError('Empty or invalid selected interval range')
    modes=max(ref.M,new.M)
    names={(0,0):'position',(1,0):'x',(0,1):'psi',
           (2,0):'xx',(1,1):'xpsi',(0,2):'psipsi'}
    maxima={name:dict(vector=0.,components=[0.,0.,0.],cell=None)
            for name in names.values()}
    rows=[];next_progress=args.progress_every
    for first in range(args.start,stop,args.batch):
        last=min(stop,first+args.batch)
        descriptors=[]
        for cell in range(first,last):
            main_left,main_right=knots[cell:cell+2]
            oldspan=min(bisect.bisect_right(ref.unit_mesh,main_left)-1,len(ref.x)-2)
            newsp=min(bisect.bisect_right(new.unit_mesh,main_left)-1,len(new.x)-2)
            for subdivision in range(args.radial_subdivisions):
                left=main_left+(main_right-main_left)*Q(subdivision,args.radial_subdivisions)
                right=main_left+(main_right-main_left)*Q(subdivision+1,args.radial_subdivisions)
                descriptors.append((cell,subdivision,oldspan,newsp,left,right))
        intervals=[(d[4],d[5]) for d in descriptors]
        oldspans=[d[2] for d in descriptors];newspans=[d[3] for d in descriptors]
        differences=[]
        for derivative in range(3):
            a=pad_batch(raw_power_batch(ref,oldspans,intervals,derivative),ref.M,modes)
            b=pad_batch(raw_power_batch(new,newspans,intervals,derivative),new.M,modes)
            differences.append(b-a)
        jet_bounds={name:batch_norm_bounds(differences[d],modes,angle)
                    for (d,angle),name in names.items()}
        for i,(cell,subdivision,oldspan,newsp,left,right) in enumerate(descriptors):
            row=dict(cell=cell,subdivision=subdivision,reference_span=oldspan,
                     candidate_span=newsp,left_exact=str(left),right_exact=str(right),jets={})
            for name in names.values():
                bound=jet_bounds[name][i]
                row['jets'][name]=bound
                if bound['vector']>maxima[name]['vector']:
                    maxima[name].update(vector=bound['vector'],cell=cell,
                        subdivision=subdivision,left_exact=str(left),right_exact=str(right))
                maxima[name]['components']=[max(a,b) for a,b in
                    zip(maxima[name]['components'],bound['cylindrical_components'])]
            if args.rows is not None:rows.append(row)
        if args.progress_every and last-args.start>=next_progress:
            print(json.dumps(dict(progress_cells=last-args.start,selected_cells=stop-args.start,
                elapsed=time.monotonic()-started)),flush=True)
            next_progress+=args.progress_every
    complete=(args.start==0 and stop==total)
    report=dict(schema='fd2d-continuous-prefix-coordinate-c2-difference-v1',
        status='PREFIX_COORDINATE_DIFFERENCE_ONLY__UNVERIFIED_GLOBALLY',
        scope=__doc__,reference=identity(args.reference),candidate=identity(args.candidate),
        script=identity(__file__),backend=identity(HERE/'78718-prefix-metric-polynomial-storage-v1.py'),
        reference_bindings=ref_bindings,candidate_bindings=new_bindings,
        comparison_chart='x in [0,1], psi; X(x,psi)=reference(S_ref*x,psi), Y(x,psi)=candidate(S_new*x,psi)',
        reference_radial_length_exact=str(ref.exact_length),candidate_radial_length_exact=str(new.exact_length),
        same_saved_angular_chart=ref.meta.get('chart')==new.meta.get('chart') and ref.meta.get('warp_reference_q')==new.meta.get('warp_reference_q'),
        same_frozen_profile_metadata=ref.meta.get('frozen_profile')==new.meta.get('frozen_profile'),
        mathematical_qualification='Normalized coordinates coincide with common physical target coordinates only after the two exact bridge/material definitions are identified. This report does not establish that identity.',
        source_modes=[ref.meta.get('source_modes'),new.meta.get('source_modes')],
        representation_modes=[ref.M,new.M],common_modes=modes,
        merged_radial_cells=total,first_cell=args.start,last_cell_exclusive=stop,
        radial_subdivisions=args.radial_subdivisions,complete_prefix_domain=complete,
        coordinate_derivatives_include_rotating_basis=True,
        bound_method='Outward binary64 interval arithmetic; exact rational knot union and affine restrictions; subtract power coefficients; Bernstein hull per Fourier coefficient; Fourier l1 and Euclidean norm',
        maxima=maxima,reference_metric_norms_computed=False,
        whole_surface_covered=False,reach_transfer=False,metric_solution=False,
        solver_calls=0,ode_calls=0,seconds=time.monotonic()-started)
    if args.rows is not None:
        raw=(json.dumps(rows,separators=(',',':'),allow_nan=False)+'\n').encode()
        if args.rows.suffix!='.gz':raise ValueError('Use a .gz path for per-cell data')
        packed=gzip.compress(raw,mtime=0)
        if len(packed)>=5_000_000:raise ValueError('Per-cell file exceeds repository single-file limit')
        args.rows.write_bytes(packed)
        report['row_data']=identity(args.rows)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out),complete_prefix_domain=complete,
        maxima={k:v['vector'] for k,v in maxima.items()},
        seconds=report['seconds'],global_transfer=False),sort_keys=True))


if __name__=='__main__':main()
