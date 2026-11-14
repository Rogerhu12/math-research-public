#!/usr/bin/env python3
"""Whole-prefix envelopes and phase-matching Hausdorff upper estimates.

No full-rigid lower bound is computed.  The same-s, shifted-angle matching
is a legitimate correspondence and supplies an upper estimate for rotation
of the finite prefix.  Bernstein bounds control the polynomial nonmean
coefficients; floating rounding is padded but not formally interval-audited.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np


def basis_at(obj,theta):
    n=len(theta);er=np.c_[np.cos(theta),np.sin(theta),np.zeros(n)]
    et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(n)];ez=np.tile([0,0,1.],(n,1))
    B=np.zeros((obj.n,n,3));B[0]=er
    for j,m in enumerate(obj.even):
        B[1+j]=np.cos(m*theta)[:,None]*er
        B[obj.M+1+j]=np.sin(m*theta)[:,None]*et
        B[obj.iz+j]=np.cos(m*theta)[:,None]*ez
    return B


def bernstein_absolute_bounds(poly,scale):
    degree=len(poly.c)-1;h=np.diff(poly.x)
    powers=[scale*poly.c[degree-k]*h[:,None]**k for k in range(degree+1)]
    largest=np.zeros(poly.c.shape[-1])
    for j in range(degree+1):
        terms=np.array([powers[k]*math.comb(j,k)/math.comb(degree,k) for k in range(j+1)])
        value=np.sum(terms,axis=0)
        pad=128*np.finfo(float).eps*np.sum(abs(terms),axis=0)+1e-300
        largest=np.maximum(largest,np.max(abs(value)+pad,axis=0))
    return largest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--angular',type=int,default=512)
    args=parser.parse_args()
    sys.path.insert(0,str(args.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from scipy.interpolate import PPoly
    from curve_stable_prefix_bvp import load_checkpoint
    from f6curve_outward_bridge_linear import read_port
    from repo_scan_gentle import scaled_port,finite_value
    from repo_scan_ellipse_bvp import EllipseBVP
    old=load_checkpoint(args.checkpoint)
    cfg=old['frozen_profile'];M=old['config']['modes'];aspect=old['config']['aspect']
    source=read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    port=scaled_port(source,cfg['cut_radius'],cfg['cut_slope'])
    obj=EllipseBVP(cfg,port,aspect,M,old['config']['angular'])
    p=np.array(old['parameters']);p[0]=0.
    flow=obj.flow(0.);obj.initial(p);core=obj._core
    P=PPoly.construct_fast(np.asarray(old['pp_coefficients']),np.asarray(old['mesh']),extrapolate=True,axis=1)
    sol=SimpleNamespace(x=P.x,sol=P,p=p)
    s=np.unique(np.r_[np.linspace(0,flow.end,401),P.x,(P.x[:-1]+P.x[1:])/2,flow.breaks])
    heights=flow.height_integral(sol,s,args.angular,6)
    theta=2*np.pi*np.arange(args.angular)/args.angular
    B=basis_at(flow,theta)
    phases=np.array([np.pi/8,np.pi/4,3*np.pi/8,np.pi/2])
    shifted=[basis_at(flow,theta+alpha) for alpha in phases]
    phase_max=np.zeros(len(phases))
    rows=[];extreme_x=(0.,0.,0.);extreme_y=(0.,0.,0.)
    for first in range(0,len(s),64):
        t=s[first:first+64];C=flow.base(t)+obj.q*P(t)
        F=flow.values(C,B);F[:,:,2]+=heights[first:first+len(t),None]
        ax=np.max(abs(F[:,:,0]),axis=1);ay=np.max(abs(F[:,:,1]),axis=1)
        zlo=np.min(F[:,:,2],axis=1);zhi=np.max(F[:,:,2],axis=1)
        rmax=np.max(np.linalg.norm(F[:,:,:2],axis=2),axis=1)
        support_floor=C[0]-np.sum(abs(C[1:M+1]),axis=0)
        for i,alpha in enumerate(phases):
            target=flow.values(C,shifted[i]);target[:,:,2]+=heights[first:first+len(t),None]
            rotated=F.copy();c=math.cos(alpha);ss=math.sin(alpha)
            rotated[:,:,0]=c*F[:,:,0]-ss*F[:,:,1]
            rotated[:,:,1]=ss*F[:,:,0]+c*F[:,:,1]
            phase_max[i]=max(phase_max[i],float(np.max(np.linalg.norm(rotated-target,axis=2))))
        ix=np.unravel_index(np.argmax(abs(F[:,:,0])),F[:,:,0].shape)
        iy=np.unravel_index(np.argmax(abs(F[:,:,1])),F[:,:,1].shape)
        if abs(F[ix[0],ix[1],0])>extreme_x[0]:
            extreme_x=(float(abs(F[ix[0],ix[1],0])),float(t[ix[0]]),float(theta[ix[1]]))
        if abs(F[iy[0],iy[1],1])>extreme_y[0]:
            extreme_y=(float(abs(F[iy[0],iy[1],1])),float(t[iy[0]]),float(theta[iy[1]]))
        rows.extend([dict(s=float(v),max_abs_x=float(x),max_abs_y=float(y),z_min=float(z0),
            z_max=float(z1),r_max=float(r),all_horizontal_directions_support_lower=float(su))
            for v,x,y,z0,z1,r,su in zip(t,ax,ay,zlo,zhi,rmax,support_floor)])
    bounds=bernstein_absolute_bounds(P,obj.q)
    weights=np.maximum(np.hypot(bounds[1:M+1],bounds[obj.iz:]),bounds[M+1:2*M+1])
    phase_bounds=[float(2*np.sum(abs(np.sin(flow.even*alpha/2))*weights)) for alpha in phases]
    all_phase_bound=float(2*np.sum(weights))
    exact=core.evaluate(theta)
    core_x=float(np.max(abs(exact['F'][:,0])));core_y=float(np.max(abs(exact['F'][:,1])))
    core_rotation_bound=core.major_radius-core.minor_radius+4*np.sum(abs(core.corrections))/core.raw_a0
    turning=flow.Tu
    ct=flow.base(np.array([turning]))[:,0]+obj.q*P(turning)
    all_direction_floor=float(ct[0]-np.sum(abs(ct[1:M+1])))
    summary=dict(scope=__doc__,checkpoint=args.checkpoint.name,aspect=aspect,modes=M,
        samples_s=len(s),samples_theta=args.angular,
        entire_prefix_max_abs_x_sampled=extreme_x[0],max_x_location_s=extreme_x[1],max_x_theta=extreme_x[2],
        entire_prefix_max_abs_y_sampled=extreme_y[0],max_y_location_s=extreme_y[1],max_y_theta=extreme_y[2],
        exact_core_max_abs_x_sampled=core_x,exact_core_max_abs_y_sampled=core_y,
        all_horizontal_directions_halfwidth_lower_at_outward_turn=all_direction_floor,
        support_lower_justification='For any direction er(theta), dot(F(s,theta),er(theta))=C0+sum(Cr_j cos(m_j theta)) >= C0-sum(abs(Cr_j)). Even modes give antipodal xy points.',
        outward_turn_s=turning,phases=phases.tolist(),
        phase_correspondence_max_distance_sampled=phase_max.tolist(),
        phase_correspondence_upper_bernstein=phase_bounds,
        all_phases_prefix_correspondence_upper_bernstein=all_phase_bound,
        all_phases_exact_core_set_upper=core_rotation_bound,
        all_phases_prefix_union_core_set_upper=max(all_phase_bound,core_rotation_bound),
        bound_qualification='Polynomial Bernstein convex-hull bound with explicit floating-roundoff padding, not an interval certification. Sampled envelope extrema are not all-domain maxima.',
        core_bound_justification='Ellipse radial radii lie in [r,R], and each correction changes position by at most 2|c_j|/raw_a0. Two Hausdorff triangle inequalities give R-r+4sum|c_j|/raw_a0.')
    args.out_prefix.with_name(args.out_prefix.name+'_summary.json').write_text(json.dumps(finite_value(summary),indent=2)+'\n')
    with gzip.open(args.out_prefix.with_name(args.out_prefix.name+'_layers.json.gz'),'wt',compresslevel=9) as h:
        json.dump(dict(scope=__doc__,rows=rows),h,indent=2)
    print(json.dumps(finite_value(summary)),flush=True)


if __name__=='__main__':
    main()
