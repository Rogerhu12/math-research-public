#!/usr/bin/env python3
"""Independent finite-difference/full-matrix audit of the full Krylov action.

The tested radial interval includes the support of the metric parameter.
An interval wholly below .05 would have a zero parameter column and cannot
test a nonsingular solve with this unknown parameter.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.interpolate import PPoly
from flint import ctx
from fourfold_codazzi_compact_metric_fast_jacobian import FastCompactNormalized
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_matrix_free_collocation import make_prepare_sys
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--guess',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('preserve an existing audit')
    ctx.prec=192;ctx.cap=6
    saved=load_candidate(args.guess);meta=json.loads(str(saved['metadata']))
    geometry,_=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    m=8;n=2*m+1
    system=FastCompactNormalized(geometry,m,128,body,graft);system.alpha=float(meta['amplitude'])
    x=np.linspace(.04,.18,6);h=np.diff(x);p=np.array([float(meta['nu'])])
    old=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(x).T;pm=int(meta['modes'])
    y=np.r_[old[:m],old[pm:pm+m+1]]
    qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    def bc(left,right,p):
        return np.r_[left[:m],right[m],left[m+1]+1,right[:m]+qstar*right[m+1:]]
    def bc_jac(left,right,p):
        jl=np.zeros((n+1,n));jr=np.zeros_like(jl);jp=np.zeros((n+1,1))
        jl[np.arange(m),np.arange(m)]=1;jr[m,m]=1;jl[m+1,m+1]=1
        jr[np.arange(m+2,n+1),np.arange(m)]=1
        jr[np.arange(m+2,n+1),np.arange(m+1,n)]=qstar
        return jl,jr,jp
    original_col,original_jac=bvp.prepare_sys(n,len(x),1,system.evaluate,bc,system.jacobian,bc_jac,x,h)
    col,ym,f,fm=original_col(y,p);b0=bc(y[:,0],y[:,-1],p)
    matrix=original_jac(y,p,ym,f,fm,b0)
    history=[]
    _,new_jac=make_prepare_sys(np.r_[np.arange(1,m+1),np.arange(m+1)],system=system,
        band=2,drop=0,chunk=2,history=history)(n,len(x),1,system.evaluate,bc,system.jacobian,bc_jac,x,h)
    solver=new_jac(y,p,ym,f,fm,b0)
    rng=np.random.default_rng(20261113);direction=rng.normal(size=n*len(x)+1)
    full=matrix@direction;action=solver.operator@direction
    action_error=float(np.max(abs(full-action)))
    dy=direction[:-1].reshape(n,len(x),order='F');dp=direction[-1:]
    def residual(yy,pp):
        cc,*_=original_col(yy,pp)
        return np.r_[cc.ravel(order='F'),bc(yy[:,0],yy[:,-1],pp)]
    differences=[]
    for step in (1e-5,1e-6,1e-7):
        diff=(residual(y+step*dy,p+step*dp)-residual(y-step*dy,p-step*dp))/(2*step)
        differences.append(dict(step=step,relative_error=float(np.max(abs(diff-action))/(1+np.max(abs(action))))))
    rr=residual(y,p);answer=solver.solve(rr)
    backward=float(np.linalg.norm(matrix@answer-rr)/np.linalg.norm(rr))
    report=dict(kind='independent_full_matrix_free_collocation_direction_and_solve_audit',
        passed=bool(action_error<1e-11 and min(v['relative_error'] for v in differences)<1e-8 and backward<1e-8),
        certified=False,modes=m,angular_grid=128,radial_nodes=x.tolist(),amplitude=system.alpha,nu=float(p[0]),
        source_sha256=sha(__file__),input_sha256=sha(args.guess),object_sha256=sha(args.object),
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_matrix_free_collocation.py','fourfold_codazzi_chunked_collocation.py',
            'fourfold_codazzi_compact_metric_fast_jacobian.py','fourfold_codazzi_compact_metric_branch_probe.py')},
        full_original_matrix_action_maximum_difference=action_error,central_differences=differences,
        original_full_matrix_backward_relative_error=backward,linear_history=history,
        scope='Actual target and finite nonlinear state, exact discrete Jacobian action, separate original scipy full matrix and independent nonlinear directional differences. The band-2 restriction affects only the preconditioner. No PDE or infinite-mode existence is inferred.')
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print({key:report[key] for key in ('passed','full_original_matrix_action_maximum_difference','original_full_matrix_backward_relative_error')},flush=True)


if __name__=='__main__':main()
