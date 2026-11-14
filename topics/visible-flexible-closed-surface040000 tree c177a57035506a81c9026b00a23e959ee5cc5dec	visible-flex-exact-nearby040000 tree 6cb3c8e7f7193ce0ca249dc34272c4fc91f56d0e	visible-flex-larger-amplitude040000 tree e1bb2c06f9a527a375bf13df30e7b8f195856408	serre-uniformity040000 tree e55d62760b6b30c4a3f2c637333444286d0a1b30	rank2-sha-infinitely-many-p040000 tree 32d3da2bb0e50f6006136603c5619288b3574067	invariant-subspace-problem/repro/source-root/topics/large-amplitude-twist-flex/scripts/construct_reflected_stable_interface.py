#!/usr/bin/env python3
"""Match an exact reflected rectifying core to a LINEAR stable cycle mode.

The triangular radius cycle is only a transfer-matrix benchmark: its slope
jumps are not C2, and no collar or complete annulus is constructed here.
The central block, its metric, and its reflection are exact.  The nonlinear
port's leading m=2 coefficients are matched to a linear stable eigenline.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.special import ellipe
from construct_rectifying_wavy_core import evaluate, geometry

WIDTH_CONVENTION = ('Every planned width/budget field here means L_band=2*(core halfwidth + one prefix length), '
                    'the meridian-length budget. It is not automatically the problem annular width W. '
                    'PV/L_band and curvature*L_band are conservative interface screens, not complete W certificates.')


def sharp_wt_bound(R, A, m=2):
    """Exact one-variable maximum of |d(tau/kappa)/dt|, up to rounding.

    Squaring the derivative and differentiating leaves a quadratic whose
    only possible maximum in (0,1) is explicitly evaluated below.
    """
    u=A/R; d=m*m*u*u; c=1+m*m*d; e=(m*m-1)*d
    p0=c*(c*(8*d-1)+9*e)
    p1=-12*d*c*c+8*d*c*e-10*c*e+6*e*e
    p2=-3*d*c*e-(d+4)*e*e
    q=0. if p0<=0 else 2*p0/(-p1+np.sqrt(p1*p1-4*p2*p0))
    q=float(np.clip(q,0,1))
    N=c+(4*d*c+2*e)*q-d*e*q*q
    value=m*m*(m*m-1)*u/R*np.sqrt(1-q)*N/(c-e*q)**2.5
    return float(value),q


def triangle_transfer(delta, speed, m=2):
    """Two constant +/- speed cone legs, radius 1 -> 1+delta -> 1."""
    k=m*m; rr=speed/np.sqrt(1-speed*speed)
    aa=1-2*k*(k-1)*delta*delta/(1+delta)
    bb=-2*k*delta*(1+k*delta)/(1+delta)
    cc=2*(k-1)*delta*(1-(k-1)*delta)/(1+delta)
    M=np.array([[aa,bb/rr],[cc*rr,aa]])
    if aa>=-1:
        return dict(matrix=M,hyperbolic=False)
    lam=aa+np.sqrt(aa*aa-1)
    rho=rr*np.sqrt(aa*aa-1)/bb
    return dict(matrix=M,hyperbolic=True,stable_eigenvalue=float(lam),
                stable_height_over_radial=float(rho),
                linear_halfwidth=float(-1/(k*rho)),
                cycle_length=float(2*delta/speed))


def radius_for_unit_perimeter(A,m=2):
    if not 0<A<np.pi/(2*m):
        raise ValueError('Amplitude cannot have orbit radius a0=1')
    fun=lambda R:2*R*ellipe(-(m*A/R)**2)/np.pi-1
    return float(brentq(fun,1e-7,1.,xtol=3e-15,rtol=3e-15))


def leading_port(R,A,h,m=2,n=512):
    theta=2*np.pi*np.arange(n)/n
    g=evaluate(h,theta,R,A,m)
    if np.max(abs(g['residual']))>2e-11:
        raise ValueError('Implicit exact-core inversion did not converge')
    F=g['F']; er=np.c_[np.cos(theta),np.sin(theta),np.zeros(n)]
    et=np.c_[-np.sin(theta),np.cos(theta),np.zeros(n)]
    f=np.sum(F*er,axis=1)-g['a0']; tang=np.sum(F*et,axis=1)
    z=F[:,2]-np.mean(F[:,2]); cm=np.cos(m*theta); sm=np.sin(m*theta)
    lead=np.array([2*np.mean(f*cm),2*np.mean(z*cm)])
    return lead,dict(radial_cos=float(lead[0]),height_cos=float(lead[1]),
                     radial_sin=float(2*np.mean(f*sm)),height_sin=float(2*np.mean(z*sm)),
                     tangential_sin=float(2*np.mean(tang*sm)),
                     linear_angular_constraint_defect=float(2*np.mean(tang*sm)+lead[0]/m),
                     height_PV=float(np.ptp(F[:,2])),
                     full_radial_rms=float(np.std(f)),full_height_rms=float(np.std(z)))


def core_bounds(R,A,h,m=2):
    wt,q=sharp_wt_bound(R,A,m); wc=m*(m*m-1)*A/R
    kb=np.sqrt(R*R+m**4*A*A)/(R*R); den=1-h*wt
    u=A/R; dz_nonnegative=m*m*(m*m-1)*u*u<=1
    # Proven sufficient global embedding condition, not a sampling test.
    embedding=bool(den>0 and dz_nonnegative and h*m*m*A<R*R)
    out=dict(sharp_wt_bound=wt,sharp_wt_maximizer_sin_squared=q,
             implicit_denominator_lower=float(den),
             principal_curvature_upper=float(kb*(1+wc*wc)/den) if den>0 else None,
             diameter_upper=float(2*(np.hypot(R,A)+h*np.sqrt(1+wc*wc))),
             binormal_development_vertical_nonnegative=bool(dz_nonnegative),
             embedding_margin=float(1-h*m*m*A/(R*R)),embedding_sufficient=embedding)
    return out


def solve_interface(delta,speed,ratio=.05,m=2):
    tr=triangle_transfer(delta,speed,m)
    if not tr['hyperbolic']:
        return dict(delta=delta,speed=speed,target_central_PV_over_budget=ratio,status='not hyperbolic')
    rho=tr['stable_height_over_radial']; L=tr['cycle_length']
    def setup(h,n=256):
        A=ratio*(h+L); R=radius_for_unit_perimeter(A,m)
        bounds=core_bounds(R,A,h,m)
        if bounds['implicit_denominator_lower']<.04:
            raise ValueError('Core too near its regression singularity')
        lead,port=leading_port(R,A,h,m,n)
        return float((lead[1]-rho*lead[0])/A),R,A,bounds,lead,port
    h0=tr['linear_halfwidth']; records=[]; interval=None; previous=None
    maxh=min(4.,.98*np.pi/(2*m*ratio)-L)
    if maxh>0:
        grid=np.unique(np.r_[0.,np.linspace(.01,min(maxh,2*h0+.2),81)])
        for h in grid:
            try:
                z=setup(h)
            except (ValueError,FloatingPointError):
                continue
            records.append((h,z))
            if previous is not None and z[0]*previous[1]<=0:
                interval=(previous[0],h);break
            previous=(h,z[0])
    base=dict(delta=delta,speed=speed,target_central_PV_over_budget=ratio,
              width_convention=WIDTH_CONVENTION,a0=1.,prefix_radial_excursion=delta,
              triangle_matrix=tr['matrix'].tolist(),triangle_stable_eigenvalue=tr['stable_eigenvalue'],
              stable_height_over_radial=rho,linear_halfwidth=h0,one_cycle_length=L)
    if interval is None:
        if records:
            h,z=min(records,key=lambda r:abs(r[1][0]));base.update(best_halfwidth=float(h),
               best_normalized_line_defect=float(z[0]),best_bounds=z[3])
        return dict(**base,status='no regular core match in search interval')
    h=float(brentq(lambda h:setup(h)[0],*interval,xtol=5e-13,rtol=5e-13))
    z,R,A,bounds,lead,port=setup(h,2048)
    width=2*(h+L)
    phi=2*np.pi*np.arange(16384)/16384
    gg=geometry(phi,R,A,m)
    sample_k=gg['kappa']*(1+gg['w']**2)/(1-h*abs(gg['wt']))
    port_k=gg['kappa']/(1+h*gg['wt'])
    port_k_min=float(np.min(port_k))
    # This checks the exact reflection of the complete port, not only m=2.
    theta=2*np.pi*np.arange(1024)/1024
    left=evaluate(-h,theta,R,A,m)['F']
    right=evaluate(h,theta+np.pi/m,R,A,m)['F'].copy()
    right[:,2]*=-1
    angle=-np.pi/m
    Q=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
    right[:,:2]=right[:,:2]@Q.T
    base.update(status='exact core / linear leading-mode match only',
       core_R=R,core_amplitude=A,core_halfwidth=h,planned_total_width=width,
       planned_Lband=width,
       central_PV_over_budget=float(2*A/width),exact_port=port,
       stable_line_defect=float(z),reflection_max_error=float(np.max(abs(left-right))),
       exact_core_bounds=bounds,
       curvature_bound_times_budget=float(bounds['principal_curvature_upper']*width),
       sampled_max_core_curvature_times_budget=float(np.max(sample_k)*width),
       sampled_port_curve_curvature_min=port_k_min,
       instantaneous_triangle_slope_root_min=float(1-(speed/port_k_min)**2),
       core_diameter_bound_over_budget=float(bounds['diameter_upper']/width),
       projected_linear_contraction=float(np.linalg.norm(tr['matrix']@lead)/np.linalg.norm(lead)),
       full_completion=False)
    return base


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',required=True)
    ap.add_argument('--ratios',default='.05,.2');ap.add_argument('--deltas',default='.4,.5,.6,.8,1.')
    ap.add_argument('--speeds',default='.5,.6,.7,.8,.9');args=ap.parse_args()
    records=[]
    for ratio in map(float,args.ratios.split(',')):
        for delta in map(float,args.deltas.split(',')):
            for speed in map(float,args.speeds.split(',')):
                records.append(solve_interface(delta,speed,ratio))
    out=dict(author='constructive_geometry; GPT-6 Astra Pro; AI-assisted',scope=__doc__,
             width_convention=WIDTH_CONVENTION,records=records)
    Path(args.out).write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    good=[r for r in records if r.get('exact_core_bounds',{}).get('embedding_sufficient') and r.get('curvature_bound_times_budget',1e99)<=100]
    print(json.dumps(dict(records=len(records),regular_matches=sum('core_R' in r for r in records),
        conservatively_feasible_cores=len(good),
        best=sorted(good,key=lambda r:abs(r['triangle_stable_eigenvalue']))[:4]),indent=2),flush=True)


if __name__=='__main__':main()
