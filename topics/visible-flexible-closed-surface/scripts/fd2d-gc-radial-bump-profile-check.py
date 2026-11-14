#!/usr/bin/env python3
"""Actual local checks of the physical radial design interface, not a BVP."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
from pathlib import Path
import platform
import time
import numpy as np
import scipy
from fd2d_gc_radial_bump_profile import (RadialBumpProfile,identity,
    positive_tail_kappa_yy,tail_lifting_profile_jacobian)
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_raw_lifted_dae import CertifiedReference,step5


def maximum(q):
    return float(np.max(abs(np.asarray(q)),initial=0.))


def actual_tail_lifting(jet,coords,tail,w,ws):
    U,Us,Ux=(np.asarray(coords[k],float) for k in ('u','u_s','u_xi'))
    a,av=np.asarray(jet['a']),np.asarray(jet['a_s'])
    sn,cs=np.sin(U),np.cos(U);y=a[None,:]*sn
    ys=av[None,:]*sn+a[None,:]*cs*Us;yx=a[None,:]*cs*Ux
    q=tail.angle_jets(y);k,ky=q['kappa'],q['kappa_y']
    v=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
    vu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
    raw=k[...,None]*v
    return dict(values=w[None,:,None]*raw,
        s=ws[None,:,None]*raw+w[None,:,None]*(ky[...,None]*ys[...,None]*v+k[...,None]*Us[...,None]*vu),
        xi=w[None,:,None]*(ky[...,None]*yx[...,None]*v+k[...,None]*Ux[...,None]*vu))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--base-lower-packet',type=Path)
    args=ap.parse_args();started=time.monotonic()
    if args.out.exists():
        raise FileExistsError('Choose a new check report')
    profile=RadialBumpProfile(args.candidate,count=7)
    s=np.unique(np.r_[profile.breaks,np.linspace(0,profile.end,161)])
    base=profile.base.profile(s);zero=profile.jet(s)
    zero_error={key:maximum(zero[key]-old) for key,old in zip(('a','a_s','a_ss'),base)}
    endpoints=[]
    for k in range(5):
        for j,(left,right) in enumerate(profile.supports):
            endpoints.append(maximum(profile.basis(np.array([left,right]),k)[:,j]))
    delta=np.array([.003,-.002,.0025,-.0015,.001,.002,-.001])
    direction=np.array([1.,-.3,.7,-.4,.2,.6,-.5]);direction/=np.linalg.norm(direction)
    profile.set_parameters(delta);jet=profile.jet(s);analytic=profile.jvp(s,direction)
    rows=[]
    for h in (1e-5,3e-6,1e-6):
        profile.set_parameters(delta+h*direction);plus=profile.jet(s)
        profile.set_parameters(delta-h*direction);minus=profile.jet(s)
        for key in ('a','a_s','a_ss','c','K'):
            finite=(plus[key]-minus[key])/(2*h);error=finite-analytic[key]
            rows.append(dict(step=h,field=key,absolute_maximum=maximum(error),
                relative_l2=float(np.linalg.norm(error)/max(1.,np.linalg.norm(analytic[key])))))
    profile.set_parameters(delta)
    protected=np.unique(np.r_[np.linspace(0,profile.central_end,9),
        np.linspace(profile.end-profile.collar_guard,profile.end,9)])
    orig=profile.base.profile(protected);new=profile.jet(protected)
    protected_error={key:maximum(new[key]-old) for key,old in zip(('a','a_s','a_ss'),orig)}
    sample=profile.check_positive(points_per_piece=9)
    conditional=None
    if args.base_lower_packet is not None:
        conditional=profile.check_positive(base_lower_bound='4/5',
            base_lower_provenance=identity(args.base_lower_packet),points_per_piece=9)
    geometry=FixedBalancedGeometry()
    chart=BlendedIntrinsicGC(profile,maximum_mode=31,oversample=4,
        reference=CertifiedReference(geometry),blend_interval=(.58,min(1.4,.94*profile.end)))
    coords=chart.coordinates(s,coordinate=np.arange(64)*2*np.pi/64)
    w,wq=step5((s-.42*profile.end)/(.58*profile.end));ws=wq/(.58*profile.end)
    tail=PositiveFlatDevelopableFamily(.9+.15*np.sin(np.arange(16)),
        cut_radius=.8,flat_radius=.34,cuff_radius=.32,plane_height=1.25)
    jac=tail_lifting_profile_jacobian(profile.jet(s),coords,tail,w,ws)
    exact={key:values@direction for key,values in jac.items()}
    tail_rows=[]
    for h in (1e-5,3e-6,1e-6):
        profile.set_parameters(delta+h*direction)
        plus=actual_tail_lifting(profile.jet(s),coords,tail,w,ws)
        profile.set_parameters(delta-h*direction)
        minus=actual_tail_lifting(profile.jet(s),coords,tail,w,ws)
        for key in ('values','s','xi'):
            fd=(plus[key]-minus[key])/(2*h);error=fd-exact[key]
            tail_rows.append(dict(step=h,field=key,absolute_maximum=maximum(error),
                relative_l2=float(np.linalg.norm(error)/max(1.,np.linalg.norm(exact[key])))))
    profile.set_parameters(delta)
    y=np.linspace(-.95,.95,701);k2=positive_tail_kappa_yy(tail,y)['kappa_yy']
    kyfd=(tail.angle_jets(y+1e-6)['kappa_y']-tail.angle_jets(y-1e-6)['kappa_y'])/(2e-6)
    k2error=maximum(kyfd-k2)
    report=dict(schema='fd2d-physical-radial-bump-check-v1',source=identity(__file__),
        module=identity(Path(__file__).with_name('fd2d_gc_radial_bump_profile.py')),
        candidate=identity(args.candidate),definition=profile.definition(),
        actual_delta=delta.tolist(),zero_delta_exact_base_errors=zero_error,
        basis_endpoint_jets_0_to_4_maximum=max(endpoints),
        protected_cylinder_and_cut_errors=protected_error,profile_direction_checks=rows,
        actual_positive_domain_screen=sample,conditional_positive_certificate=conditional,
        positive_tail_kappa_yy_fd_error=k2error,tail_lifting_direction_checks=tail_rows,
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        seconds=time.monotonic()-started,scope='Actual finite implementation check of profile and lifting derivatives; no nonlinear GC solve or geometry certificate')
    selected=[r for r in rows+tail_rows if r['step']==1e-6]
    report['passed']=bool(max(zero_error.values())==0 and max(protected_error.values())==0
        and max(endpoints)==0 and sample['sampled_screen']['passed']
        and max(r['relative_l2'] for r in selected)<2e-6 and k2error<2e-5)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out),passed=report['passed'],seconds=report['seconds'],
        maximum_direction_relative_l2=max(r['relative_l2'] for r in selected),
        exact_protected_errors=protected_error,kappa_yy_fd_error=k2error)),flush=True)
    return 0 if report['passed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
