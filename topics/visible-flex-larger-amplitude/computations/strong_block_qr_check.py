#!/usr/bin/env python3
"""Compare block QR and sparse LU on one actual finite-neck Jacobian.

Pass --check-output PATH and an otherwise ordinary strong_neck_bvp invocation.
It stops after assembling and solving one actual collocation Jacobian. This is
an inspection, not a nonlinear solve, fixed-g refinement, or surface result.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import hashlib,importlib.util,json,sys,time,gc,weakref
from pathlib import Path
import numpy as np
from scipy.integrate._bvp import prepare_sys
from scipy.sparse.linalg import splu
from strong_block_qr import BlockQRFactor
P=Path(__file__).resolve().parent

def main():
    i=sys.argv.index('--check-output');output=Path(sys.argv[i+1]);del sys.argv[i:i+2]
    source_hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ('strong_block_qr.py','strong_block_qr_check.py','strong_neck_bvp.py')}
    spec=importlib.util.spec_from_file_location('strong_real_qr_runner',P/'strong_neck_bvp.py');runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    original=runner.module;result={}
    def inspect_solver(fun,bc,x,y,p,**kw):
        n,m=y.shape;k=len(p);clock=time.time();h=np.diff(x)
        col,jac=prepare_sys(n,m,k,fun,bc,kw['fun_jac'],kw['bc_jac'],x,h)
        start=time.time();cr,ym,ff,fm=col(y,p);br=bc(y[:,0],y[:,-1],p);value_seconds=time.time()-start
        print(json.dumps(dict(event='actual_values',n=n,nodes=m,parameters=k,seconds=value_seconds)),flush=True)
        start=time.time();J=jac(y,p,ym,ff,fm,br);jac_seconds=time.time()-start
        print(json.dumps(dict(event='actual_jacobian',shape=J.shape,nnz=J.nnz,seconds=jac_seconds)),flush=True)
        rhs=np.r_[cr.ravel(order='F'),br]
        automatic_gc=gc.isenabled();gc.disable()
        csr_copy=J.tocsr(copy=True);jac_reference=weakref.ref(csr_copy)
        start=time.time();qr=BlockQRFactor(csr_copy,n,m,k);qr_seconds=time.time()-start
        del csr_copy
        retained_jacobian_without_gc=jac_reference() is not None
        start=time.time();qx=qr.solve(rhs);qr_solve=time.time()-start
        print(json.dumps(dict(event='actual_qr',factor_seconds=qr_seconds,solve_seconds=qr_solve)),flush=True)
        start=time.time();lu=splu(J);lu_seconds=time.time()-start
        start=time.time();lx=lu.solve(rhs);lu_solve=time.time()-start
        scale=max(float(np.max(abs(J)@abs(qx)+abs(rhs))),np.finfo(float).tiny)
        backward=float(np.max(abs(J@qx-rhs))/scale)
        relative=float(np.max(abs(qx-lx))/max(1.,np.max(abs(lx))))
        result.update(scope=__doc__,inspection_only=True,nonlinear_solution=False,n=n,nodes=m,parameters=k,shape=list(J.shape),nnz=int(J.nnz),value_seconds=value_seconds,jacobian_seconds=jac_seconds,qr_factor_seconds=qr_seconds,qr_solve_seconds=qr_solve,lu_factor_seconds=lu_seconds,lu_solve_seconds=lu_solve,qr_relative_backward_error=backward,qr_vs_lu_relative_difference=relative,step_norm_qr=float(np.max(abs(qx))),step_norm_lu=float(np.max(abs(lx))),source_sha256=source_hashes,seconds=time.time()-clock,profile=dict(fun.__self__.flow(p[0]).cfg))
        rhs_reference=weakref.ref(rhs)
        answer_owner=qx if qx.base is None else qx.base
        answer_reference=weakref.ref(answer_owner)
        del rhs,qx,answer_owner
        result['recursive_closure_retention_without_gc']=dict(jacobian=retained_jacobian_without_gc,rhs=rhs_reference() is not None,answer_storage=answer_reference() is not None)
        if automatic_gc:gc.enable()
        output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
        if not (backward<1e-10 and relative<1e-6):raise RuntimeError('Actual factor comparison outside diagnostic tolerances')
        if any(result['recursive_closure_retention_without_gc'].values()):raise RuntimeError('Recursive closure retains numerical storage without GC')
        raise RuntimeError('Inspection complete; no nonlinear solve requested')
    def module(name,path):
        m=original(name,path)
        if Path(path).name=='root_dual_core_bvp.py':m.solve_bvp=inspect_solver
        return m
    runner.module=module;runner.main()
if __name__=='__main__':main()
