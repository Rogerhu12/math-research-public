#!/usr/bin/env python3
"""Compare sparse ordering on the same actual coarse Codazzi Newton matrix.

This diagnostic concerns factorization fill and backward error only.  It
does not solve the nonlinear BVP or certify a continuous source bound.
"""
from __future__ import annotations
import argparse,gc,json,resource,time
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from scipy.sparse.linalg import splu
import scipy.integrate._bvp as bvp
from flint import ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_compact_metric_fast_jacobian import FastCompactNormalized
from fourfold_codazzi_chunked_collocation import make_prepare_sys
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--guess',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--modes',type=int,default=128);ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--stride',type=int,default=8);ap.add_argument('--band',type=int,default=16)
    args=ap.parse_args();ctx.prec=192;ctx.cap=6
    if args.out.exists():raise FileExistsError(args.out)
    obj=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json')
    saved=load_candidate(args.guess);meta=json.loads(str(saved['metadata']));oldm=meta['modes']
    geo,_=load_exact_object(obj,512);body=RotationalBodyTarget(geo);graft=RotationalGraftTarget(geo,obj)
    m=args.modes;n=2*m+1;s=FastCompactNormalized(geo,m,args.angles,body,graft);s.alpha=meta['amplitude']
    x=np.unique(np.r_[saved['radial_nodes'][::args.stride],saved['radial_nodes'][-1]])
    v=PPoly(saved['piece_coefficients'],saved['radial_nodes'])(x).T;y=np.zeros((n,len(x)));common=min(oldm,m)
    y[:common]=v[:common];y[m:m+common+1]=v[oldm:oldm+common+1];p=np.array([meta['nu']])
    qstar=1/np.sqrt(1+(graft.a_endpoint/(4*graft.omega))**2)
    def bc(a,b,p):return np.r_[a[:m],b[m],a[m+1]+1,b[:m]+qstar*b[m+1:]]
    def bcj(a,b,p):
        A=np.zeros((n+1,n));B=A.copy();P=np.zeros((n+1,1))
        A[np.arange(m),np.arange(m)]=1;B[m,m]=1;A[m+1,m+1]=1
        B[np.arange(m+2,n+1),np.arange(m)]=1;B[np.arange(m+2,n+1),np.arange(m+1,n)]=qstar
        return A,B,P
    history=[];prepare=make_prepare_sys(np.r_[np.arange(1,m+1),np.arange(m+1)],band=args.band,drop=1e-13,chunk=8,history=history)
    col,jac=prepare(n,len(x),1,s.evaluate,bc,s.jacobian,bcj,x,np.diff(x))
    rr,ym,f,fm=col(y,p);bb=bc(y[:,0],y[:,-1],p);residual=np.r_[rr.ravel(order='F'),bb]
    matrix=jac(y,p,ym,f,fm,bb);rows=[]
    for order in ('COLAMD','MMD_AT_PLUS_A','MMD_ATA','NATURAL'):
        tick=time.monotonic();factor=splu(matrix,permc_spec=order);elapsed=time.monotonic()-tick
        solution=factor.solve(residual);back=float(np.max(abs(matrix@solution-residual))/(1+np.max(abs(residual))))
        item=dict(order=order,L_nonzeros=factor.L.nnz,U_nonzeros=factor.U.nnz,
            fill_ratio=float((factor.L.nnz+factor.U.nnz)/matrix.nnz),factor_seconds=elapsed,
            backward_error=back,cumulative_peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        rows.append(item);print(item,flush=True);del factor;gc.collect()
    report=dict(kind='actual_coarse_Codazzi_sparse_ordering_diagnostic',certified=False,source_sha256=sha(__file__),
        input_path=str(args.guess),input_sha256=sha(args.guess),object_sha256=sha(obj),
        modes=m,angular_grid=args.angles,mesh_stride=args.stride,radial_nodes=len(x),band=args.band,
        nonlinear_BVP_solved=False,continuous_PDE_certified=False,
        unchanged_complete_nonlinear_collocation_system=True,
        matrix_shape=list(matrix.shape),matrix_nonzeros=matrix.nnz,assembly_history=history,rows=rows,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_compact_metric_fast_jacobian.py','fourfold_codazzi_chunked_collocation.py',
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_compact_metric_branch_probe.py')})
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':main()
