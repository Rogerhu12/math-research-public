#!/usr/bin/env python3
"""Whole-ruling normal-ball screen, with finite angular coverage explicit.

The two radial ruling parameters are minimized analytically as a convex
quadratic over a rectangle.  The normal of the actual finite ruled surface
may vary along a ruling; its full variation is included as a separate error.
This is not a continuous all-angle reach certificate.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import time
from pathlib import Path
import numpy as np
from fd2d_peak_spacer_ruling_consumer import SpectralInlet
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_k0_ruling_segment_geometry import segment_geometry


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rectangle_ball_minimum(X0, G0, W0, N0, X1, G1, W1, radius, sign):
    """Minimize |q-p|^2-2 sign radius N0.(q-p), all 0<=w<=W0,0<=z<=W1.

    X1/G1/W1 may be batches.  N0 is a fixed unit vector for the first
    ruling.  Formula covers parallel directions via the four edge minima.
    Interior candidates are used only for a numerically resolved positive
    determinant.  All arithmetic is ordinary floating evaluation.
    """
    d = X1-X0
    A = float(np.dot(G0,G0))
    B = -np.einsum('...j,j->...',G1,G0)
    C = np.einsum('...j,...j->...',G1,G1)
    shifted = d-sign*radius*N0
    c0 = -np.einsum('...j,j->...',shifted,G0)
    c1 = np.einsum('...j,...j->...',shifted,G1)
    zero = np.zeros_like(W1)
    wi = zero+W0
    candidates = []
    for w in (zero,wi):
        z = np.clip(-(c1+B*w)/C,0,W1)
        candidates.append((w,z))
    for z in (zero,W1):
        w = np.clip(-(c0+B*z)/A,0,W0)
        candidates.append((w,z))
    det = A*C-B*B
    resolved = det > 64*np.finfo(float).eps*A*C
    safe = np.where(resolved,det,1)
    wint = (B*c1-C*c0)/safe
    zint = (B*c0-A*c1)/safe
    valid = resolved & (wint>=0) & (wint<=W0) & (zint>=0) & (zint<=W1)
    candidates.append((np.where(valid,wint,zero),np.where(valid,zint,zero)))
    values=[]
    distances=[]
    for w,z in candidates:
        chord = d + z[...,None]*G1-w[...,None]*G0
        d2 = np.einsum('...j,...j->...',chord,chord)
        values.append(d2-2*sign*radius*np.einsum('...j,j->...',chord,N0))
        distances.append(np.sqrt(d2))
    values=np.stack(values,axis=-1)
    choice=np.argmin(values,axis=-1)
    take=lambda a:np.take_along_axis(np.stack(a,axis=-1),choice[...,None],axis=-1)[...,0]
    max_d2=np.zeros_like(W1)
    for w in (zero,wi):
        for z in (zero,W1):
            chord=d+z[...,None]*G1-w[...,None]*G0
            max_d2=np.maximum(max_d2,np.einsum('...j,...j->...',chord,chord))
    return dict(minimum=take([values[...,j] for j in range(values.shape[-1])]),
        w=take([z[0] for z in candidates]),z=take([z[1] for z in candidates]),
        distance_at_minimum=take(distances),max_distance=np.sqrt(max_d2),
        interior_test_resolved=resolved)


def main():
    root=Path(__file__).resolve().parent.parent
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--angles',type=int,default=384)
    ap.add_argument('--radius',type=float,default=.136)
    ap.add_argument('--stem',type=Path,required=True)
    args=ap.parse_args()
    if list(args.stem.parent.glob(args.stem.name+'*')):
        raise FileExistsError('Use a new output stem')
    tic=time.monotonic()
    saved=np.load(args.inlet,allow_pickle=False)
    geometry=FixedBalancedGeometry()
    inlet=SpectralInlet(saved['frame_fourier'],saved['n_phi_cos'],saved['m_phi_sin'],saved['frequencies'],geometry)
    phi=np.arange(args.angles,dtype=np.longdouble)*2*np.arccos(np.longdouble(-1))/args.angles
    data=inlet.at_phi(phi)
    a,v,L=(float(saved[k]) for k in ('a','v','coast_length'))
    line=segment_geometry(a,v,L,data,[0,geometry.A,0])
    X=np.asarray(data['X'],float);G=np.asarray(line['ruling_direction'],float);W=np.asarray(line['W'],float)
    k=data['m']/data['n'];ku=data['m_u']/data['n']-data['m']*data['n_u']/data['n']**2
    Gt=data['e1_u']-ku[:,None]*data['e2']-k[:,None]*data['e2_u']
    C0=np.cross(line['ruling_direction'],data['X_u']);C1=np.cross(line['ruling_direction'],Gt)
    CW=C0+line['W'][:,None]*C1
    N0=C0/np.linalg.norm(C0,axis=-1)[:,None];N1=CW/np.linalg.norm(CW,axis=-1)[:,None]
    if np.any(np.sum(N0*N1,axis=-1)<=0):
        raise ValueError('The simple endpoint normal-variation formula requires same open hemisphere')
    normal_change=np.asarray(np.linalg.norm(N1-N0,axis=-1),float)
    N0=np.asarray(N0,float)
    report_rows=[]
    minimum=np.inf;worst=None
    bins=[1,2,4,8,16,32,64,args.angles//2+1]
    bin_min={str(b):np.inf for b in bins}
    allj=np.arange(args.angles)
    for i in range(args.angles):
        separation=np.minimum((allj-i)%args.angles,(i-allj)%args.angles)
        active=separation>0
        for sign in (-1,1):
            r=rectangle_ball_minimum(X[i],G[i],W[i],N0[i],X,G,W,args.radius,sign)
            correction=2*args.radius*normal_change[i]*r['max_distance']
            lower=r['minimum']-correction
            lower=np.where(active,lower,np.inf)
            j=int(np.argmin(lower));value=float(lower[j])
            if value<minimum:
                minimum=value
                worst=dict(i=i,j=j,phi_i=float(phi[i]),phi_j=float(phi[j]),sign=sign,
                    analytic_constant_normal_minimum=float(r['minimum'][j]),
                    actual_normal_variation_correction=float(correction[j]),
                    lower=value,w=float(r['w'][j]),z=float(r['z'][j]),
                    distance_at_constant_normal_minimum=float(r['distance_at_minimum'][j]))
            report_rows.append(dict(i=i,sign=sign,minimum=value,j=j))
            lo=1
            for hi in bins:
                selected=(separation>=lo)&(separation<=hi)
                if np.any(selected):bin_min[str(hi)]=min(bin_min[str(hi)],float(np.min(lower[selected])))
                lo=hi+1
    report=dict(schema='fd2d-ruling-whole-radial-normal-ball-screen-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),
        dependencies={name:digest(root/'scripts'/name) for name in ('fd2d_peak_spacer_ruling_consumer.py','fd2d_balanced_curvature_core.py','fd2d_k0_ruling_segment_geometry.py','fd2d_k0_ruling_coast.py')},
        angular_nodes=args.angles,ordered_distinct_angular_pairs=args.angles*(args.angles-1),radius=args.radius,
        full_radial_rectangle_minimized=True,constant_normal_quadratic_candidates='four clipped edge minima and resolved interior stationary point',
        actual_normal_change_along_ruling_max=float(np.max(normal_change)),
        min_Nz=float(np.min(N0[:,2])),max_Nz=float(np.max(N0[:,2])),
        actual_normal_variation_accounted_in_float=True,min_ball_inequality_lower=minimum,worst=worst,
        gap_bins_upper_in_grid_steps=bins,minimum_by_gap_bin=bin_min,
        diagonal_rulings='For equal inlet label, the actual normal is perpendicular to G for every ruling parameter; inequality is |(z-w)G|^2>=0 exactly.',
        angular_continuous_certificate=False,rounding_enclosures=False,full_reach_certificate=False,
        sampled_pair_decision=bool(minimum>=0),seconds=time.monotonic()-tic)
    path=args.stem.with_name(args.stem.name+'-report.json')
    path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path),sha256=digest(path),minimum=minimum,worst=worst,seconds=report['seconds']),allow_nan=False))


if __name__=='__main__':main()
