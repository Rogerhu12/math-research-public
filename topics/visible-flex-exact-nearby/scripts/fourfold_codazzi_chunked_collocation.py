#!/usr/bin/env python3
"""Memory-bounded collocation Jacobian for the floating Codazzi probes.

The nonlinear collocation residual is scipy's unchanged residual.  The full
analytic Jacobian is computed on short radial chunks; only its linear solver
matrix may omit far Fourier bands or entries below a stated absolute cutoff.
This is an approximate Newton matrix, never a change to the nonlinear system.
"""
from __future__ import annotations
import time
import numpy as np
from scipy.sparse import csr_matrix, hstack
import scipy.integrate._bvp as bvp


def make_prepare_sys(mode_indices, *, band, drop, chunk, history):
    mode_indices=np.asarray(mode_indices,dtype=np.int64)
    if band<0 or drop<0 or chunk<1:raise ValueError('invalid approximate Jacobian controls')
    keep=abs(mode_indices[:,None]-mode_indices[None,:])<=band
    pairs=int(np.count_nonzero(keep))

    def prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        if n!=len(mode_indices) or fun_jac is None or bc_jac is None:
            raise ValueError('this producer requires its complete analytic state/parameter and boundary Jacobians')
        middle=x[:-1]+h/2

        def col_fun(y,p):return bvp.collocation_fun(fun,y,p,x,h)

        def sys_jac(y,p,y_middle,f,f_middle,bc0):
            started=time.monotonic();size=n*m+k
            # Preallocate CSR capacity, not complete dense radial tensors.
            # Unused pages are never filled; resize releases the unused tail.
            capacity=(m-1)*(2*pairs+n*k)+(n+k)*(2*n+k)
            data=np.empty(capacity,dtype=y.dtype)
            indices=np.empty(capacity,dtype=np.int32 if size<2**31 else np.int64)
            indptr=np.zeros(size+1,dtype=indices.dtype);used=0
            max_drop=0.;max_drop_row=0.;max_full_row=0.;identity=np.eye(n,dtype=y.dtype)
            for start in range(0,m-1,chunk):
                stop=min(start+chunk,m-1)
                df,dp=fun_jac(x[start:stop+1],y[:,start:stop+1],p)
                dm,pm=fun_jac(middle[start:stop],y_middle[:,start:stop],p)
                df=np.moveaxis(df,2,0);dm=np.moveaxis(dm,2,0)
                dp=np.moveaxis(dp,2,0);pm=np.moveaxis(pm,2,0)
                for j in range(stop-start):
                    i=start+j;hh=h[i]
                    left=-identity-hh*(df[j]+2*dm[j])/6-hh*hh*(dm[j]@df[j])/12
                    right=identity-hh*(df[j+1]+2*dm[j])/6+hh*hh*(dm[j]@df[j+1])/12
                    parameter=-hh*(dp[j]+dp[j+1]+4*pm[j])/6+hh*hh*(dm[j]@(dp[j+1]-dp[j]))/12
                    left_omitted=(~keep)|(abs(left)<=drop)
                    right_omitted=(~keep)|(abs(right)<=drop)
                    dropped_left=np.where(left_omitted,left,0.)
                    dropped_right=np.where(right_omitted,right,0.)
                    max_drop=max(max_drop,float(np.max(abs(dropped_left))),float(np.max(abs(dropped_right))))
                    max_drop_row=max(max_drop_row,float(np.max(abs(dropped_left).sum(axis=1)+abs(dropped_right).sum(axis=1))))
                    max_full_row=max(max_full_row,float(np.max(abs(left).sum(axis=1)+abs(right).sum(axis=1)+abs(parameter).sum(axis=1))))
                    left[left_omitted]=0.;right[right_omitted]=0.
                    block=hstack((csr_matrix(left),csr_matrix(right),csr_matrix(parameter)),format='csr')
                    count=block.nnz
                    data[used:used+count]=block.data
                    local=block.indices
                    indices[used:used+count]=np.where(local<2*n,i*n+local,n*m+local-2*n)
                    indptr[i*n+1:(i+1)*n+1]=used+block.indptr[1:]
                    used+=count
                del df,dm,dp,pm
            ja,jb,jp=bc_jac(y[:,0],y[:,-1],p)
            boundary=hstack((csr_matrix(ja),csr_matrix(jb),csr_matrix(jp)),format='csr')
            count=boundary.nnz;data[used:used+count]=boundary.data;local=boundary.indices
            indices[used:used+count]=np.where(local<n,local,np.where(local<2*n,(m-1)*n+local-n,n*m+local-2*n))
            indptr[(m-1)*n+1:]=used+boundary.indptr[1:];used+=count
            data.resize(used,refcheck=False);indices.resize(used,refcheck=False)
            matrix=csr_matrix((data,indices,indptr),shape=(size,size)).tocsc()
            item=dict(radial_nodes=m,state_dimension=n,parameter_dimension=k,
                Fourier_band=band,absolute_entry_cutoff=drop,radial_chunk=chunk,
                nonzero_entries=matrix.nnz,maximum_omitted_entry=max_drop,
                maximum_omitted_collocation_row_l1=max_drop_row,
                maximum_full_collocation_row_l1=max_full_row,
                assembly_seconds=time.monotonic()-started,
                nonlinear_residual_unchanged=True,approximate_Newton_matrix=True)
            history.append(item);print(dict(chunked_Jacobian=item),flush=True)
            return matrix
        return col_fun,sys_jac
    return prepare_sys
