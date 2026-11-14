#!/usr/bin/env python3
"""Full FFT collocation Jacobian actions, with a sparse Fourier-band preconditioner.

The differentiated endpoint/midpoint equations retain every finite mode
and the complete metric-parameter column.  A band restriction is applied
only to the LU preconditioner. GMRES is checked against the full action.
This v2 keeps the identical full action and backward-residual gate, with a
64-vector restart instead of 32. It remains a floating diagnostic, not a PDE proof.
"""
from __future__ import annotations
import time
import numpy as np
from scipy.sparse.linalg import LinearOperator,gmres,splu
from fourfold_codazzi_chunked_collocation import make_prepare_sys as sparse_prepare


def state_action(system,r,y,p):
    t,B,c,C,A=system.data(r,y,p);a,g,b,K,ell,Cr,dg,dl,dCr=t
    alpha=system.alpha;m=system.modes
    AB=2*alpha*B/C
    Ac=-(ell*Cr*Cr+alpha*alpha*B*B)/(C*C)
    Ap=-dl*c+alpha*dl*c*c/C-alpha*(B*B+ell*c*c)*dCr/(C*C)
    grid=system.angular_grid
    if grid<=2*m:raise ValueError('the real FFT must contain the complete finite support')
    def project_cosine(value):
        answer=(2/grid)*np.fft.rfft(value,axis=0).real[:m+1]
        answer[0]*=.5
        return answer
    baseline_A=project_cosine(A);baseline_b=y[:m].copy()
    def action(v,parameter):
        # These are exactly the original finite sine/cosine evaluations and
        # trapezoidal projection, up to floating arithmetic. Every retained
        # Fourier coupling of the sampled rational coefficients remains.
        spectrum=np.zeros((grid//2+1,v.shape[1]),dtype=complex)
        spectrum[1:m+1]=-.5j*v[:m]
        vb=grid*np.fft.irfft(spectrum,n=grid,axis=0)
        spectrum[0]=v[m];spectrum[1:m+1]=.5*v[m+1:]
        vc=grid*np.fft.irfft(spectrum,n=grid,axis=0)
        va=project_cosine(AB*vb+Ac*vc+Ap*parameter)
        out=np.empty_like(v)
        out[:m]=-g*system.frequency[:,None]*va[1:]-2*b*v[:m]
        out[:m]-=parameter*dg*system.frequency[:,None]*baseline_A[1:]
        out[m:]=b*(va-v[m:]);out[m+1:]+=g*system.frequency[:,None]*v[:m]
        out[m+1:]+=parameter*dg*system.frequency[:,None]*baseline_b
        return out
    return action


class FullCollocationSolve:
    def __init__(self,operator,factor,history):
        self.operator=operator;self.factor=factor;self.history=history
        self.preconditioner=LinearOperator(operator.shape,matvec=factor.solve,dtype=float)

    def solve(self,residual):
        tick=time.monotonic();callbacks=[]
        def callback(value):callbacks.append(float(value))
        answer,info=gmres(self.operator,residual,M=self.preconditioner,
            rtol=1e-10,atol=1e-24,restart=64,maxiter=12,
            callback=callback,callback_type='pr_norm')
        error=self.operator@answer-residual
        denom=float(np.linalg.norm(residual))
        relative=float(np.linalg.norm(error)/max(denom,1e-300))
        item=dict(kind='full_finite_collocation_GMRES',info=int(info),iterations=len(callbacks),
            restart_length=64,maximum_restart_cycles=12,
            full_relative_residual=relative,maximum_absolute_residual=float(np.max(abs(error))),
            preconditioned_residual_history=callbacks,seconds=time.monotonic()-tick,
            all_finite_modes_and_parameter_column_retained=True)
        self.history.append(item)
        print(dict(full_GMRES={key:value for key,value in item.items()
                              if key!='preconditioned_residual_history'}),flush=True)
        if info!=0 or not np.all(np.isfinite(answer)) or relative>5e-8:
            raise RuntimeError('full collocation GMRES did not meet its backward-residual gate')
        return answer


def make_prepare_sys(mode_indices,*,system,band,drop,chunk,history):
    approximate=sparse_prepare(mode_indices,band=band,drop=drop,chunk=chunk,history=history)
    def prepare(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        if k!=1:raise ValueError('this complete normalized branch has one metric parameter')
        system.current_mesh_x=x.copy()
        col_fun,preconditioner_jac=approximate(n,m,k,fun,bc,fun_jac,bc_jac,x,h)
        middle=x[:-1]+h/2
        def jac(y,p,ym,f,fm,bc0):
            tick=time.monotonic();sparse=preconditioner_jac(y,p,ym,f,fm,bc0)
            factor=splu(sparse);nnz=int(factor.nnz);del sparse
            endpoints=state_action(system,x,y,p);midpoints=state_action(system,middle,ym,p)
            left,right,parameter=bc_jac(y[:,0],y[:,-1],p)
            def matvec(vector):
                v=vector[:n*m].reshape(n,m,order='F');dp=float(vector[-1])
                df=endpoints(v,dp)
                vm=(v[:,:-1]+v[:,1:])/2-h*(df[:,1:]-df[:,:-1])/8
                dm=midpoints(vm,dp)
                result=v[:,1:]-v[:,:-1]-h*(df[:,:-1]+df[:,1:]+4*dm)/6
                boundary=left@v[:,0]+right@v[:,-1]+parameter[:,0]*dp
                return np.r_[result.ravel(order='F'),boundary]
            operator=LinearOperator((n*m+1,n*m+1),matvec=matvec,dtype=float)
            history.append(dict(kind='complete_matrix_free_linearization',radial_nodes=m,state_dimension=n,
                preconditioner_LU_nonzeros=nnz,construction_seconds=time.monotonic()-tick,
                full_operator_band_truncated=False,preconditioner_band=band,complete_evaluations_by_real_FFT=True))
            return FullCollocationSolve(operator,factor,history)
        return col_fun,jac
    return prepare
