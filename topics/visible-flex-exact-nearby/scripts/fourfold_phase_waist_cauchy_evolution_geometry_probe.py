#!/usr/bin/env python3
"""Floating nonlinear Cauchy evolution with actual curvature diagnostics.

This is a finite Fourier diagnostic, not a validated PDE solve or a global
inverse. The ORIGINAL target is evaluated directly at every RHS call. No
moving target, fitted replacement metric, cap boundary condition, or omitted
mean projection is used. The r evolution imposes the rr/mixed metric
constraints and the genuine Gauss equation simultaneously.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp

from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_core_low_block import uniform_fields
from fourfold_phase_local_correction_probe import (
    sha,dot,angular_derivative,scalar_target,source_and_geometry,correction_norms,
)


def acceleration(F,P,target):
    T=angular_derivative(F);Q=angular_derivative(T);Mvec=angular_derivative(P)
    C=np.cross(T,P);G=dot(C,C);N=dot(C,Q);M=dot(C,Mvec)
    if np.min(G)<=0 or np.min(abs(N))<1e-12:
        raise ValueError('Cauchy metric/curvature denominator failed')
    pp,pt,tt=dot(P,P),dot(P,T),dot(T,T)
    rr=target['E_x']/2;mixed=-dot(P,Mvec)
    alpha=(tt*rr-pt*mixed)/G;beta=(pp*mixed-pt*rr)/G
    normal=(M*M+target['K']*G*G)/(N*G)
    A=alpha[:,None]*P+beta[:,None]*T+normal[:,None]*C
    return A,T,Mvec,Q


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--right',type=float,default=.05);p.add_argument('--samples',type=int,default=51)
    p.add_argument('--rtol',type=float,default=3e-10);p.add_argument('--atol',type=float,default=3e-12)
    p.add_argument('--max-step',type=float,default=.00025)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--state',type=Path,required=True)
    args=p.parse_args();start=time.monotonic()
    geometry,definition=load_exact_object(args.object,args.nodes)
    F0=uniform_fields(geometry,0.,args.angles)[0];t0=scalar_target(geometry,0.)
    P0=np.zeros_like(F0);P0[:,2]=np.sqrt(t0['E'])
    y0=np.stack([F0,P0]).ravel();evaluations=0;last_progress=start
    def rhs(r,y):
        nonlocal evaluations,last_progress
        F,P=y.reshape(2,args.angles,3);target=scalar_target(geometry,r)
        A,*_=acceleration(F,P,target);evaluations+=1
        now=time.monotonic()
        if now-last_progress>20:
            print({'r':r,'rhs_calls':evaluations,'elapsed':now-start},flush=True);last_progress=now
        return np.stack([P,A]).ravel()
    solution=solve_ivp(rhs,(0.,args.right),y0,method='DOP853',rtol=args.rtol,atol=args.atol,
        max_step=args.max_step,t_eval=np.linspace(0.,args.right,args.samples))
    rows=[]
    for r,y in zip(solution.t,solution.y.T):
        F,P=y.reshape(2,args.angles,3);target=scalar_target(geometry,float(r))
        A,T,Mvec,Q=acceleration(F,P,target);updated=(F,P,T,A,Mvec,Q)
        old=uniform_fields(geometry,float(r),args.angles)
        before=source_and_geometry(old,target);after=source_and_geometry(updated,target)
        V=tuple(x-o for x,o in zip(updated,old))
        gg=after['metric'];nu=after['normal']
        determinant=gg[0][0]*gg[1][1]-gg[0][1]**2
        ell,emm,enn=[dot(nu,z) for z in (A,Mvec,Q)]
        mean_curvature=(gg[1][1]*ell-2*gg[0][1]*emm+gg[0][0]*enn)/(2*determinant)
        principal_max=np.abs(mean_curvature)+np.sqrt(np.maximum(0.,mean_curvature**2-after['actual_K']))
        row=dict(r=float(r),
            updated_absolute_principal_curvature_max=float(np.max(principal_max)),
            updated_rr_metric_defect=float(np.max(abs(gg[0][0]-target['E']))),
            updated_mixed_metric_defect=float(np.max(abs(gg[0][1]))),
            updated_angular_metric_defect=float(np.max(abs(gg[1][1]-target['a']**2))),
            original_source_C0=float(np.max(abs(before['q']))),
            updated_source_C0=float(np.max(abs(after['q']))),
            updated_metric_defect_C0=float(np.max(after['metric_norm'])),
            updated_curvature_defect_C0=float(np.max(abs(after['actual_K']-after['K0']))),
            updated_support_min=float(after['support']),**correction_norms(V,before))
        rows.append(row)
    terminal=solution.y[:,-1].reshape(2,args.angles,3)
    np.savez_compressed(args.state,r=solution.t[-1],F=terminal[0],F_r=terminal[1],
        angles=np.arange(args.angles)*(np.pi/2)/args.angles,
        metadata=np.array(json.dumps({'kind':'floating_Cauchy_endpoint','object_sha256':sha(args.object),'source_sha256':sha(__file__)})))
    names=[k for k in rows[0] if k!='r']
    maxima={key:max(row[key] for row in rows) for key in names}
    doc=dict(kind='floating_fixed_target_nonlinear_waist_Cauchy_evolution',complete=bool(solution.success),certified=False,
        source_sha256=sha(__file__),object_sha256=sha(args.object),
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in ('fourfold_phase_local_correction_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py')},
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        exact_center_parameter=definition['delta_fraction'],primitive_nodes=args.nodes,angular_grid=args.angles,
        whole_real_angular_circle=False,whole_parameter_interval=False,whole_radial_domain=False,
        original_target_fixed=True,mean_and_all_grid_modes_retained=True,
        method='DOP853 finite rotating-frame Fourier collocation',rtol=args.rtol,atol=args.atol,max_step=args.max_step,
        requested_radial_interval=[0.,args.right],finished_radial_interval=[float(solution.t[0]),float(solution.t[-1])],
        rhs_calls=solution.nfev,solver_message=solution.message,rows=rows,sampled_maxima=maxima,sampled_updated_support_min=min(row['updated_support_min'] for row in rows),
        endpoint_state_path=str(args.state),endpoint_state_sha256=sha(args.state),wall_seconds=time.monotonic()-start,
        limitations=['No interval time integration, floating roundoff or nonlinear angular aliasing certificate.',
            'The spatial grid omits Fourier modes above its Nyquist frequency; no analytic tail bound is claimed.',
            'Only the center affine parameter and listed radial/angle samples are evaluated; no continuous full-eta cover.',
            'No regular/mean return, global cap closure, graft matching or global Newton inverse is imposed.',
            'Very small metric/source diagnostics depend on a curvature equation imposed by construction and are not independent convergence proofs.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({'complete':doc['complete'],'rhs_calls':solution.nfev,'wall_seconds':doc['wall_seconds'],
           'maxima':maxima,'last':rows[-1]},flush=True)


if __name__=='__main__':main()
