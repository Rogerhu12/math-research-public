#!/usr/bin/env python3
"""Complete finite QR with an independently evaluated full system action.

This adapter accepts nonlinear separated boundary rows and one parameter.
It reuses the complete boundary-row QR algebra, but evaluates the original
backward residual through system.full_action, including its parameter
column. No old B,c-coordinate action is substituted for reciprocal U,V.
All finite Fourier entries and the original 5e-8 solve gate remain present.
"""
from __future__ import annotations
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.sparse.linalg import LinearOperator
from fourfold_codazzi_block_qr_collocation import FullBoundaryQR,CheckedFullQRSolve
from fourfold_codazzi_block_qr_checkpointed import CheckpointBoundaryQR


def make_prepare_sys(*,system,chunk,history,storage='checkpoint',scratch=None,span=32):
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
                factor=CheckpointBoundaryQR(n,m,left,right,parameter,blocks,history,span=span)
            else:
                factor=FullBoundaryQR(n,m,left,right,parameter,blocks(0,m-1),history,
                    storage=storage,scratch=scratch)
            endpoints=system.full_action(x,y,p)
            midpoints=system.full_action(middle,ym,p)
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
