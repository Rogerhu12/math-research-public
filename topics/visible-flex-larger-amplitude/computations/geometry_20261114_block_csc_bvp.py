#!/usr/bin/env python3
"""Memory-efficient assembly of the exact SciPy 1.17 no-parameter BVP Jacobian.

The collocation equations and Newton method do not change. Each dense local
block is placed directly in sorted CSC storage. This avoids complete COO
row/column arrays and complete temporary arrays of all local dense blocks.
"""
import numpy as np
import json
import resource
from pathlib import Path
from scipy.sparse import csc_matrix
import scipy.integrate._bvp as backend

native_prepare_sys = backend.prepare_sys


def assemble(n,m,h,df_nodes,df_mid,bc_left,bc_right):
    if m<2:
        raise ValueError('The collocation mesh needs at least two nodes')
    dtype=df_nodes.dtype
    count=2*m*n*n
    index_dtype=np.int32 if max(count,m*n)<2**31 else np.int64
    data=np.empty((m,n,2,n),dtype=dtype)
    indices=np.empty((m,n,2,n),dtype=index_dtype)
    local_rows=np.arange(n,dtype=index_dtype)
    for j in range(m):
        indices[j,:,0,:]=(max(0,j-1)*n)+local_rows
        indices[j,:,1,:]=((m-1)*n if j==0 else j*n)+local_rows
    eye=np.eye(n,dtype=dtype)
    for j in range(m-1):
        aa=df_nodes[:,:,j]
        bb=df_mid[:,:,j]
        cc=df_nodes[:,:,j+1]
        step=h[j]
        left=-eye.copy()
        left-=step/6*(aa+2*bb)
        left-=step**2/12*backend.stacked_matmul(bb[None,:,:],aa[None,:,:])[0]
        right=eye.copy()
        right-=step/6*(cc+2*bb)
        right+=step**2/12*backend.stacked_matmul(bb[None,:,:],cc[None,:,:])[0]
        data[j,:,0 if j==0 else 1,:]=left.T
        data[j+1,:,0,:]=right.T
    data[0,:,1,:]=bc_left.T
    data[-1,:,1,:]=bc_right.T
    indptr=np.arange(m*n+1,dtype=index_dtype)*(2*n)
    result=csc_matrix((data.ravel(),indices.ravel(),indptr),shape=(m*n,m*n),copy=False)
    result.has_sorted_indices=True
    result.has_canonical_format=True
    return result


def prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
    if k:
        return native_prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h)
    if fun_jac is None or bc_jac is None:
        return native_prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h)
    mid=x[:-1]+.5*h

    def col_fun(y,p):
        return backend.collocation_fun(fun,y,p,x,h)

    def sys_jac(y,p,y_mid,f,f_mid,bc0):
        df_nodes,unused=fun_jac(x,y,p)
        df_mid,unused=fun_jac(mid,y_mid,p)
        bc_left,bc_right,unused=bc_jac(y[:,0],y[:,-1],p)
        result=assemble(n,m,h,df_nodes,df_mid,bc_left,bc_right)
        status={line.split(':',1)[0]:line.split(':',1)[1].strip() for line in Path('/proc/self/status').read_text().splitlines() if line.startswith(('VmRSS:','VmHWM:'))}
        print(json.dumps(dict(event='block_csc_assembled',n=n,nodes=m,stored_entries=int(result.nnz),
                              maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**status)),flush=True)
        return result

    return col_fun,sys_jac


def enable():
    backend.prepare_sys=prepare_sys
