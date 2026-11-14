#!/usr/bin/env python3
"""Complete boundary QR with bounded factor memory and exact block recomputation.

Only orthonormal boundary row spaces are checkpointed. Each solve rebuilds
the same full local factors in short segments, in both directions. No
Fourier entry, equation, parameter column or backward-residual gate changes.
"""
from __future__ import annotations
import resource
import time
import warnings
import numpy as np
import scipy.integrate._bvp as bvp
from scipy.linalg import LinAlgWarning,lu_factor
from scipy.sparse.linalg import LinearOperator
from fourfold_codazzi_block_qr_collocation import (
    FullBoundaryQR,CheckedFullQRSolve,orthonormal_rows,householder,apply_qt)
from fourfold_codazzi_matrix_free_fft_collocation_v5 import state_action


class CheckpointBoundaryQR(FullBoundaryQR):
    def __init__(self,n,nodes,left,right,parameter,block_factory,history,span=32):
        tick=time.monotonic()
        if span<1:raise ValueError("positive checkpoint span required")
        self.n,self.nodes,self.history=n,nodes,history
        self.span,self.block_factory=span,block_factory
        self.left_rows=np.flatnonzero(np.any(left!=0,axis=1))
        self.right_rows=np.flatnonzero(~np.any(left!=0,axis=1))
        if np.any(right[self.left_rows]!=0):
            raise RuntimeError("full QR requires the actual separated boundary rows")
        self.p=p=self.left_rows.size
        if p==0 or p>n or left.shape!=(n+1,n):
            raise RuntimeError("unsupported full boundary dimensions")
        self.c0,self.initial_r=orthonormal_rows(
            np.column_stack((left[self.left_rows],parameter[self.left_rows,0])))
        self.right_boundary=np.column_stack(
            (right[self.right_rows],parameter[self.right_rows,0]))
        self.right_scale=1/np.maximum(1.,np.max(abs(self.right_boundary),axis=1))
        self.right_boundary*=self.right_scale[:,None]
        self.seeds={0:self.c0.copy()}
        self.cache_start=-1;self.cache=[]
        self.file=None
        self.minimum_local_diagonal=float("inf")
        current=self.c0
        for i,(a,b,c) in enumerate(block_factory(0,nodes-1)):
            item,current=self.step(current,a,b,c)
            packed=item[0]
            self.minimum_local_diagonal=min(self.minimum_local_diagonal,
                float(np.min(abs(np.diag(packed[:n])))))
            if (i+1)%span==0:self.seeds[i+1]=current.copy()
            if (i+1)%64==0 or i==nodes-2:
                print(dict(full_checkpointed_QR_blocks=i+1,expected_blocks=nodes-1,
                    elapsed_seconds=time.monotonic()-tick,
                    retained_boundary_row_bytes=sum(v.nbytes for v in self.seeds.values()),
                    peak_resident_KiB=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        if i!=nodes-2:raise RuntimeError("incomplete full block stream")
        self.end=np.vstack((current,self.right_boundary))
        if self.end.shape!=(n+1,n+1):
            raise RuntimeError("the full final boundary matrix is not square")
        self.end_condition=float(np.linalg.cond(self.end))
        with warnings.catch_warnings():
            warnings.simplefilter("error",LinAlgWarning)
            try:self.end_lu=lu_factor(self.end,check_finite=False)
            except (ValueError,LinAlgWarning) as error:
                raise RuntimeError(f"complete final boundary factor failed: {error}") from error
        # One segment may be kept. Larger node counts do not retain all factors.
        shapes=((n+p,n),(n,),(n,n),(n,),(p,p),(n,))
        self.record_bytes=8*sum(int(np.prod(s)) for s in shapes)
        item=dict(kind="full_checkpointed_boundary_QR_factorization",
            radial_nodes=nodes,state_dimension=n,parameter_dimension=1,
            all_Fourier_couplings_retained=True,no_entry_drop=True,
            recomputation_segment_length=span,
            retained_boundary_row_bytes=sum(v.nbytes for v in self.seeds.values()),
            maximum_cached_factor_bytes=span*self.record_bytes,
            final_boundary_condition_2=self.end_condition,
            minimum_local_QR_diagonal=self.minimum_local_diagonal,
            seconds=time.monotonic()-tick)
        history.append(item);print(item,flush=True)

    def step(self,current,a,b,c):
        n,p=self.n,self.p
        scale=1/np.maximum(1.,np.maximum.reduce((
            np.max(abs(a),axis=1),np.max(abs(b),axis=1),abs(c))))
        packed,tau=householder(np.vstack((current[:,:n],scale[:,None]*a)))
        coefficients=np.zeros((n+p,n+1))
        coefficients[:p,n]=current[:,n]
        coefficients[p:,:n]=scale[:,None]*b
        coefficients[p:,n]=scale*c
        transformed=apply_qt(packed,tau,coefficients)
        next_rows,norm_r=orthonormal_rows(transformed[n:])
        return (packed,tau,transformed[:n,:n].copy(),
                transformed[:n,n].copy(),norm_r,scale),next_rows

    def read(self,index):
        if self.cache_start<=index<self.cache_start+len(self.cache):
            return self.cache[index-self.cache_start]
        start=(index//self.span)*self.span;stop=min(start+self.span,self.nodes-1)
        self.cache=[];self.cache_start=start
        current=self.seeds[start].copy()
        for a,b,c in self.block_factory(start,stop):
            item,current=self.step(current,a,b,c)
            self.cache.append(item)
        if len(self.cache)!=stop-start:
            raise RuntimeError("incomplete recomputed exact factor segment")
        return self.cache[index-start]


def make_prepare_sys(mode_indices,*,system,band,drop,chunk,history,
                     storage="checkpoint",scratch=None,span=32):
    if span%chunk:
        raise ValueError("checkpoint segments must align with full Jacobian chunks")
    def prepare(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        if k!=1 or len(mode_indices)!=n or m<2:
            raise ValueError("this complete branch has one metric parameter")
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
            factor=CheckpointBoundaryQR(n,m,left,right,parameter,blocks,history,span=span)
            endpoints=state_action(system,x,y,p);midpoints=state_action(system,middle,ym,p)
            def matvec(vector):
                v=vector[:n*m].reshape(n,m,order="F");dp=float(vector[-1])
                df=endpoints(v,dp)
                vm=(v[:,:-1]+v[:,1:])/2-h*(df[:,1:]-df[:,:-1])/8
                dm=midpoints(vm,dp)
                result=v[:,1:]-v[:,:-1]-h*(df[:,:-1]+df[:,1:]+4*dm)/6
                boundary=left@v[:,0]+right@v[:,-1]+parameter[:,0]*dp
                return np.r_[result.ravel(order="F"),boundary]
            operator=LinearOperator((n*m+1,n*m+1),matvec=matvec,dtype=float)
            return CheckedFullQRSolve(operator,factor,history)
        return col_fun,jac
    return prepare
