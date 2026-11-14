"""Conditional outer-design height windows for an exact central extrusion.

All arrays refer only to the suffix translated by delta e_z. Bounds must
cover actual positions and outward normals, not merely formal frame fields.
Plain floating arithmetic here is a screen, not outward interval arithmetic.
"""
from __future__ import annotations
import math
import numpy as np


def _abs_lower(lo,hi):
    return np.maximum(np.maximum(lo,-hi),0.)


def suffix_height_window(position_lower,position_upper,normal_z_lower,
        normal_z_upper,support_lower,*,central_length,
        central_A_interval,held_distance=.9,sphere_radius=2.25,
        slab_half_width=.85,reach_radius=.136,cut_Z_interval=None,
        desired_Z_interval=None,central_radius_upper=None,
        central_gap_lower=None,central_support_lower=None,
        actual_box_certificate_supplied=False):
    lo,hi=np.broadcast_arrays(np.asarray(position_lower,float),np.asarray(position_upper,float))
    if lo.shape[-1]!=3 or np.any(lo>hi) or not np.all(np.isfinite(lo)) or not np.all(np.isfinite(hi)):
        raise ValueError("finite ordered position boxes with last dimension three required")
    shape=lo.shape[:-1]
    vlo=np.broadcast_to(np.asarray(normal_z_lower,float),shape).ravel()
    vhi=np.broadcast_to(np.asarray(normal_z_upper,float),shape).ravel()
    sigma=np.broadcast_to(np.asarray(support_lower,float),shape).ravel()
    if np.any(vlo>vhi) or not all(np.all(np.isfinite(v)) for v in (vlo,vhi,sigma)):
        raise ValueError("finite ordered actual-normal/support boxes required")
    lo,hi=lo.reshape(-1,3),hi.reshape(-1,3)
    C=float(central_length);R=float(sphere_radius);h=float(held_distance);rho=float(reach_radius)
    A0,A1=map(float,central_A_interval)
    if C<=0 or R<=0 or h<0 or rho<=0 or A0>A1:raise ValueError("invalid scalar window")
    lower=[(-C,'positive new central length; strict'),(-float(np.min(lo[:,2])),'upper suffix nonnegative height')]
    upper=[];fail=[]
    dx=_abs_lower(lo[:,0],hi[:,0])
    dy=np.maximum(np.maximum(lo[:,1]-A1,A0-hi[:,1]),0.)
    h2=dx*dx+dy*dy
    ids=np.flatnonzero(h2<h*h)
    if len(ids):
        values=np.sqrt(np.maximum(h*h-h2[ids],0.))-lo[ids,2]
        j=int(np.argmax(values))
        lower.append((float(values[j]),f'held suffix box {int(ids[j])}'))
    r2=np.maximum(abs(lo[:,0]),abs(hi[:,0]))**2+np.maximum(abs(lo[:,1]),abs(hi[:,1]))**2
    bad=np.flatnonzero(r2>R*R)
    if len(bad):fail.append(dict(condition='independent horizontal box exceeds sphere',indices=bad.tolist()))
    else:
        values=np.sqrt(np.maximum(R*R-r2,0.))-hi[:,2]
        j=int(np.argmin(values));upper.append((float(values[j]),f'sphere suffix box {j}'))
    slab=float(np.max(np.maximum(abs(lo[:,1]),abs(hi[:,1]))))
    if slab>slab_half_width:fail.append(dict(condition='suffix slab',upper=slab,target=slab_half_width))
    if (cut_Z_interval is None)!=(desired_Z_interval is None):
        raise ValueError("both cut and desired Z intervals are needed")
    if cut_Z_interval is not None:
        z0,z1=map(float,cut_Z_interval);a,b=map(float,desired_Z_interval)
        if z0>z1 or a>b:raise ValueError("reversed Z interval")
        lower.append((a-z0,'actual cut Z lower'))
        upper.append((b-z1,'actual cut Z upper'))
    if central_radius_upper is not None:
        radius=float(central_radius_upper)
        if radius<0 or radius>R:fail.append(dict(condition='central horizontal radius',upper=radius,target=R))
        else:upper.append((math.sqrt(R*R-radius*radius)-C,'new central cylinder sphere'))
    if central_gap_lower is not None and float(central_gap_lower)<h:
        fail.append(dict(condition='central gap sufficient bound',lower=float(central_gap_lower),target=h))
    if central_support_lower is not None and float(central_support_lower)<rho:
        fail.append(dict(condition='central support sufficient bound',lower=float(central_support_lower),target=rho))
    branches=[]
    for positive in (False,True):
        lows=list(lower);ups=list(upper);local_fail=list(fail)
        (lows if positive else ups).append((0.,'delta nonnegative' if positive else 'delta nonpositive'))
        v=vlo if positive else vhi
        for j,(s,q) in enumerate(zip(sigma,v)):
            if q>0:lows.append(((rho-s)/q,f'support lower box {j}'))
            elif q<0:ups.append(((rho-s)/q,f'support upper box {j}'))
            elif s<rho:local_fail.append(dict(condition='zero vertical normal with inadequate support',box=j))
        low=max(lows,key=lambda q:q[0])
        up=min(ups,key=lambda q:q[0]) if ups else (None,'unbounded')
        feasible=not local_fail and (up[0] is None or low[0]<=up[0])
        low_open=low[0]==-C
        if up[0] is not None and low[0]==up[0] and low_open:feasible=False
        branches.append(dict(sign='nonnegative' if positive else 'nonpositive',
            lower=low[0],upper=up[0],lower_open=low_open,upper_open=False,
            tight_lower_source=low[1],tight_upper_source=up[1],
            feasible_conditional=bool(feasible),failed_sufficient_conditions=local_fail))
    return dict(branches=branches,unchanged_slab_upper=slab,
        actual_box_certificate_supplied=bool(actual_box_certificate_supplied),
        arithmetic_is_outward_certified=False,certificate=False,
        central_conditions_not_supplied=[name for name,value in (
            ('horizontal radius',central_radius_upper),('held gap',central_gap_lower),
            ('outward support',central_support_lower)) if value is None],
        scope="Sufficient box window for a NEW metric obtained from an exact central extrusion; curvature and the original actual surface remain separately required.")
