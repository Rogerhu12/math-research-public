#!/usr/bin/env python3
"""Complete finite QR with a bounded-batch independent full system action.

This adapter accepts nonlinear separated boundary rows and one parameter.
It reuses the complete boundary-row QR algebra, but evaluates the original
backward residual through system.full_action, including its parameter
column. No old B,c-coordinate action is substituted for reciprocal U,V.
All finite Fourier entries and the original 5e-8 solve gate remain present.
Full QR seeds and substitutions are persisted with exact identities.
Only independent radial columns are batched; all coefficients are reevaluated
from immutable full nodal data during each checked operator application.
"""
from __future__ import annotations
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.sparse.linalg import LinearOperator
from fourfold_codazzi_block_qr_collocation import FullBoundaryQR,CheckedFullQRSolve
from fourfold_codazzi_block_qr_persistent import PersistentCheckpointBoundaryQR, array_digest, sha
from pathlib import Path


def chunked_full_action(system,r,y,p,batch=16):
    """Keep immutable nodal input, evaluating every full Fourier row by batches.

    Radial columns are independent in a state Jacobian action. Splitting
    these columns removes no angular coupling or parameter contribution.
    The final full collocation backward gate remains unchanged.
    """
    r=np.asarray(r).copy();y=np.asarray(y).copy();p=np.asarray(p).copy()
    def action(delta,parameter):
        if delta.shape!=y.shape:raise ValueError('incomplete full action state')
        out=np.empty_like(delta)
        for start in range(0,len(r),batch):
            stop=min(start+batch,len(r))
            actual=system.full_action(r[start:stop],y[:,start:stop],p)
            out[:,start:stop]=actual(delta[:,start:stop],parameter)
        return out
    return action


def make_prepare_sys(*,system,chunk,history,storage='checkpoint',scratch=None,span=8):
    if storage not in ('memory','file','checkpoint'):
        raise ValueError('unsupported complete factor storage')
    if chunk<1 or span<1 or span%chunk:
        raise ValueError('checkpoint segments must align with full Jacobian chunks')
    if not callable(getattr(system,'full_action',None)):
        raise TypeError('an independent full action for the actual state chart is required')
    def prepare(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        if k!=1 or m<2:
            raise ValueError('the complete boundary system has one metric parameter')
        system.current_mesh_x=x.copy();middle=x[:-1]+h/2
        def col_fun(y,p):return bvp.collocation_fun(fun,y,p,x,h)
        def jac(y,p,ym,f,fm,bc0):
            left,right,parameter=bc_jac(y[:,0],y[:,-1],p)
            identity=np.eye(n)
            def blocks(begin,end):
                for start in range(begin,end,chunk):
                    stop=min(start+chunk,end)
                    df,dp=fun_jac(x[start:stop+1],y[:,start:stop+1],p)
                    dm,pm=fun_jac(middle[start:stop],ym[:,start:stop],p)
                    df,dm=np.moveaxis(df,2,0),np.moveaxis(dm,2,0)
                    dp,pm=np.moveaxis(dp,2,0),np.moveaxis(pm,2,0)
                    for j in range(stop-start):
                        hh=h[start+j]
                        a=-identity-hh*(df[j]+2*dm[j])/6-hh*hh*(dm[j]@df[j])/12
                        b=identity-hh*(df[j+1]+2*dm[j])/6+hh*hh*(dm[j]@df[j+1])/12
                        c=-hh*(dp[j]+dp[j+1]+4*pm[j])/6
                        c+=hh*hh*(dm[j]@(dp[j+1]-dp[j]))/12
                        yield a,b,c[:,0]
            if storage=='checkpoint':
                label=getattr(system,'factor_checkpoint_identity',None)
                if label is None:raise ValueError('explicit original-system checkpoint identity is required')
                root=Path(scratch or '/workspace/scratch/ac0d699811ad')/'codazzi_complete_QR_state'
                dependencies=''.join(sha(Path(__file__).with_name(name)) for name in (
                    'fourfold_codazzi_block_qr_persistent.py','fourfold_codazzi_block_qr_checkpointed.py',
                    'fourfold_codazzi_block_qr_collocation.py'))
                identity_digest=array_digest(x,h,y,p,ym,left,right,parameter,
                    label=str((n,m,span,label,dependencies)))
                factor=PersistentCheckpointBoundaryQR(n,m,left,right,parameter,blocks,history,
                    directory=root,fingerprint=identity_digest,span=span)
            else:
                factor=FullBoundaryQR(n,m,left,right,parameter,blocks(0,m-1),history,
                    storage=storage,scratch=scratch)
            endpoints=chunked_full_action(system,x,y,p)
            midpoints=chunked_full_action(system,middle,ym,p)
            def matvec(vector):
                v=vector[:n*m].reshape(n,m,order='F');dnu=float(vector[-1])
                df=endpoints(v,dnu)
                vm=(v[:,:-1]+v[:,1:])/2-h*(df[:,1:]-df[:,:-1])/8
                dm=midpoints(vm,dnu)
                result=v[:,1:]-v[:,:-1]-h*(df[:,:-1]+df[:,1:]+4*dm)/6
                boundary=left@v[:,0]+right@v[:,-1]+parameter[:,0]*dnu
                return np.r_[result.ravel(order='F'),boundary]
            operator=LinearOperator((n*m+1,n*m+1),matvec=matvec,dtype=float)
            return CheckedFullQRSolve(operator,factor,history)
        return col_fun,jac
    return prepare
