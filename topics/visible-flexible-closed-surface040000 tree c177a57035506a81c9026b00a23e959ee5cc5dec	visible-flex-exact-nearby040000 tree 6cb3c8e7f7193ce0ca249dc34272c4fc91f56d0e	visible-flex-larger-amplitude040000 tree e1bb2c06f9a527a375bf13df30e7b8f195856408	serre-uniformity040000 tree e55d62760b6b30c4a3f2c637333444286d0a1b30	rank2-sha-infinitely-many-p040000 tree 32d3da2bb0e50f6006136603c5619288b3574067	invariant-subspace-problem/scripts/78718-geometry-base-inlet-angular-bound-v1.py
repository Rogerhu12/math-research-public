#!/usr/bin/env python3
"""Exact full-angle G bound at the first position jet of a defining prefix base.

This reads the stored Cartesian Fourier map, not source CP coefficients.
The same flat-profile inlet has a=1 and the exact frozen material-angle warp.
No complete target supplier, BVP, tail solve or geometric modification is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path).resolve(); raw=path.read_bytes()
    return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--reciprocal-order',type=int,default=96)
    args=ap.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    started=time.monotonic()
    storage_path=HERE/'78718-prefix-storage-v1.py'
    storage=load('base_inlet_storage',storage_path)
    meta,payload,bindings=storage.read_payload(args.geometry,verify_arrays=True)
    if meta.get('representation')=='exact-common-cut-prefix':
        raise ValueError('Use the defining prefix base, not a common-cut facade')
    if meta['frozen_profile'].get('ramp_law')!='flat' or meta['ell']!=0:
        raise ValueError('This theorem applies to the declared flat-profile central inlet')
    if meta['chart']['knots'][0]!=0 or meta['chart']['values'][0]!=1:
        raise ValueError('Inlet angular chart differs')
    with np.load(io.BytesIO(gzip.decompress(payload)),allow_pickle=False) as data:
        if data['mesh'][0]!=0: raise ValueError('Wrong first physical node')
        p=np.array(data['jets'][0,0,:],copy=True)
    m=int(meta['modes'])
    if len(p)!=3*m+2: raise ValueError('Wrong absolute Cartesian Fourier layout')
    y=[Q.from_float(float(v)) for v in p]
    math_path=HERE/'78718-geometry-inlet-angular-bound-v1.py'
    pol=load('base_inlet_laurent_math',math_path)
    a={};b={0:y[0]};c={}
    for j in range(1,m+1):
        av=(3*j*y[j]+y[m+j])/2
        bv=(y[j]+3*j*y[m+j])/2
        cv=3*j*y[2*m+j]/2
        a[j]=av;a[-j]=-av;b[j]=bv;b[-j]=bv;c[j]=cv;c[-j]=-cv
    a={k:v for k,v in a.items() if v};b={k:v for k,v in b.items() if v};c={k:v for k,v in c.items() if v}
    w=8*Q.from_float(float(meta['warp_reference_q']))
    if not 0<w<1: raise ValueError('Invalid reciprocal series domain')
    rho={0:Q(1),1:-w/2,-1:-w/2}
    numerator=pol.add(pol.add(pol.add(pol.scale(pol.mul(a,a),-1),pol.mul(b,b)),
                             pol.scale(pol.mul(c,c),-1)),pol.scale(pol.mul(rho,rho),-1))
    kmax=args.reciprocal_order
    if kmax<0:raise ValueError('Nonnegative reciprocal order required')
    d={1:w/2,-1:w/2};power={0:Q(1)};reciprocal=dict(power)
    for k in range(1,kmax+1):
        power=pol.mul(power,d);reciprocal=pol.add(reciprocal,pol.scale(power,k+1))
    tail=w**(kmax+1)*((kmax+2)-(kmax+1)*w)/(1-w)**2
    finite=pol.mul(numerator,reciprocal)
    remainder=pol.norm(numerator)*tail
    upper=pol.norm(finite)+remainder
    unit=10**18;count=(upper.numerator*unit+upper.denominator-1)//upper.denominator
    axis={}
    for sig,name in ((1,'psi_zero'),(-1,'psi_pi_over_3')):
        tangent=y[0]+sum((sig**j*(y[j]+3*j*y[m+j]) for j in range(1,m+1)),Q(0))
        g=tangent*tangent/(1-sig*w)**2-1
        axis[name]=dict(exact=str(g),float=float(g),abs_above_2e_minus9=abs(g)>Q(1,500000000))
    report=dict(schema='78718-defining-base-inlet-angular-upper-v1',scope=__doc__,
                geometry=identity(args.geometry),storage_bindings=bindings,
                script=identity(__file__),storage_reader=identity(storage_path),
                laurent_helpers=identity(math_path),modes=m,source_modes=meta['source_modes'],
                position_jet_origin='defining base payload jets[0,0,:]',
                material_radius_exact='1',warp_exact=str(w),reciprocal_order=kmax,
                source_checkpoint_sha256=meta['checkpoint_sha256'],
                numerator_Fourier_l1=pol.fraction_row(pol.norm(numerator)),
                polynomial_G_Fourier_l1=pol.fraction_row(pol.norm(finite)),
                reciprocal_remainder=pol.fraction_row(remainder),
                continuous_G_Fourier_l1_upper=pol.fraction_row(upper),
                safe_upper_1e_minus18_grid_exact=str(Q(count,unit)),safe_upper_grid_count=count,
                strictly_below_original_2e_minus9=upper<Q(1,500000000),axes=axis,
                whole_prefix_bound=False,final_common_map_identity_transfer=False,
                BVP_calls=0,tail_calls=0,new_geometry=False,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=identity(args.out),modes=m,source_modes=meta['source_modes'],
                         upper_float=float(upper),safe_upper_grid_count=count,
                         below_2e_minus9=upper<Q(1,500000000),
                         axis_G={k:v['float'] for k,v in axis.items()},seconds=report['seconds']),sort_keys=True))


if __name__=='__main__':main()
