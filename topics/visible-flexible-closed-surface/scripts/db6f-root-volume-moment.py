#!/usr/bin/env python3
"""Rigorous finite-prefix contribution to the third horizontal volume moment.

Uses div(0,0,z(x+iy)^3)=(x+iy)^3. This is a boundary contribution from
the represented prefix and its mirror, not a complete body's moment.
The angular trapezoid is EXACT for the finite trigonometric polynomial;
radial Bernstein enclosures and outward arithmetic control the integral.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('volume_interval',HERE/'db6f-audit-continuous-hermite.py')
iv=importlib.util.module_from_spec(spec);spec.loader.exec_module(iv)
I=iv.I


def integrate(args):
    geom=iv.ExactHermite(args.geometry)
    if geom.meta.get('ell',0.)!=0.:
        raise ValueError('This mirrored moment certificate requires ell=0')
    if min(args.angular,args.radial,args.batch)<=0:
        raise ValueError('Angular count, radial subdivisions and batch size must be positive')
    N=args.angular
    if N<=6*geom.M+1:
        raise ValueError('Angular count must exceed the exact degree 6M+1')
    co=np.empty((geom.M,N,2));si=co.copy()
    for j in range(1,geom.M+1):
        for k in range(N):
            co[j-1,k]=iv.trig_point(Q(2*j*k,N),True)
            si[j-1,k]=iv.trig_point(Q(2*j*k,N),False)
    co=I(co[...,0],co[...,1]);si=I(si[...,0],si[...,1])
    pi0,pi1=iv.pi_bounds()
    pi=I(iv.qbounds(pi0).lo,iv.qbounds(pi1).hi)
    total=I(0.)
    for sub in range(args.radial):
        bounds=[geom.ranges(d,Q(sub,args.radial),Q(sub+1,args.radial)) for d in (0,1)]
        for first in range(0,len(geom.x)-1,args.batch):
            last=min(first+args.batch,len(geom.x)-1)
            X,Xp,_=iv.cylindrical(bounds[0][first:last],co,si,geom.M)
            Xs,_,_=iv.cylindrical(bounds[1][first:last],co,si,geom.M)
            R,T,Z=X[...,0],X[...,1],X[...,2]
            re=(R*R.square()-3*R*T.square())*co[0][None,:]
            re=re-(3*R.square()*T-T*T.square())*si[0][None,:]
            jac=Xp[...,0]*Xs[...,1]-Xp[...,1]*Xs[...,0]
            integrand=Z*re*jac
            angular=I(np.zeros(last-first))
            for k in range(N):angular=angular+integrand[:,k]
            contribution=angular*(2*pi/N)*geom.h[first:last]/args.radial
            for k in range(last-first):total=total+contribution[k]
    mirrored=2*total
    cut=geom.ranges(0,Q(1),Q(1))[-1]
    cut_height=cut[-1]
    for j in range(1,geom.M+1):
        v=float(cut[2*geom.M+j].abs().hi)
        cut_height=cut_height+I(-v,v)
    report={
        'scope':__doc__,'geometry':str(args.geometry),
        'geometry_sha256':iv.sha(args.geometry),'data_sha256':geom.meta['data_sha256'],
        'script_sha256':iv.sha(__file__),
        'interval_backend_sha256':iv.sha(HERE/'db6f-audit-continuous-hermite.py'),
        'angular_points_per_period':N,'exact_angular_degree_bound':6*geom.M+1,
        'radial_subdivisions':args.radial,
        'upper_prefix_real_moment_interval':[float(total.lo),float(total.hi)],
        'mirrored_prefix_real_moment_interval':[float(mirrored.lo),float(mirrored.hi)],
        'complete_cut_height_interval':[float(cut_height.lo),float(cut_height.hi)],
        'imaginary_part_zero_by_exact_reflection_symmetry':True,
        'complete_volume_moment_certified':False}
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--angular',type=int,default=128)
    parser.add_argument('--radial',type=int,default=1)
    parser.add_argument('--batch',type=int,default=16)
    integrate(parser.parse_args())
