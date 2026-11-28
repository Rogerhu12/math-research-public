"""The complete original collocation Jacobian, directly in sorted CSC.

Every stored entry, including zeros, is retained. The original SciPy block
formulas and stacked_matmul are used with the same per-entry operation order.
Large-matrix products still call the original per-node np.dot. Small matrices
retain the original whole-grid einsum call. Only radial temporary arrays and
the COO row/column/index conversion copies are avoided.
"""
import gc
import hashlib
import inspect
import resource
import time
import numpy as np
from scipy.integrate import _bvp
from scipy.sparse import csc_matrix


def construct(n,m,k,i_jac,j_jac,h,df_dy,df_dy_middle,df_dp,df_dp_middle,
              dbc_dya,dbc_dyb,dbc_dp,*,radial_block=16,record=None):
    if (n<1 or m<2 or k<0 or radial_block<1 or h.shape!=(m-1,)
            or df_dy.shape!=(n,n,m) or df_dy_middle.shape!=(n,n,m-1)
            or dbc_dya.shape!=(n+k,n) or dbc_dyb.shape!=(n+k,n)
            or (k and (df_dp.shape!=(n,k,m) or df_dp_middle.shape!=(n,k,m-1)
                       or dbc_dp.shape!=(n+k,k)))):
        raise ValueError('Complete original collocation array shapes differ')
    arrays=[h,df_dy,df_dy_middle,dbc_dya,dbc_dyb]
    if k:arrays += [df_dp,df_dp_middle,dbc_dp]
    if any(np.asarray(value).dtype!=np.dtype('float64') for value in arrays):
        raise ValueError('This exact-order adapter is restricted to the real binary64 source')
    gc.collect()
    begin=time.monotonic()
    total=n*m+k
    nnz=2*(m-1)*n*n+2*(n+k)*n+(m-1)*n*k+(n+k)*k
    index_dtype=np.int32 if max(nnz,total)<=np.iinfo(np.int32).max else np.int64
    counts=np.full(total,2*n,dtype=index_dtype)
    counts[:n]+=k
    counts[(m-1)*n:m*n]+=k
    counts[m*n:]=total
    indptr=np.empty(total+1,dtype=index_dtype);indptr[0]=0
    np.cumsum(counts,dtype=index_dtype,out=indptr[1:])
    if int(indptr[-1])!=nnz:
        raise ArithmeticError('The full original stored-entry count differs')
    del counts
    data=np.empty(nnz,dtype=np.float64)
    indices=np.empty(nnz,dtype=index_dtype)
    boundary_rows=np.arange((m-1)*n,total,dtype=index_dtype)

    def node_view(array,node):
        return array[indptr[node*n]:indptr[(node+1)*n]].reshape(n,2*n+(k if node in (0,m-1) else 0))

    for node in range(m):
        ix=node_view(indices,node)
        if node==0:
            ix[:,:n]=np.arange(n,dtype=index_dtype)
            ix[:,n:]=boundary_rows
        elif node==m-1:
            ix[:,:n]=np.arange((m-2)*n,(m-1)*n,dtype=index_dtype)
            ix[:,n:]=boundary_rows
        else:
            ix[:,:n]=np.arange((node-1)*n,node*n,dtype=index_dtype)
            ix[:,n:]=np.arange(node*n,(node+1)*n,dtype=index_dtype)
    node_view(data,0)[:,n:]=dbc_dya.T
    node_view(data,m-1)[:,n:]=dbc_dyb.T
    if k:
        parameter_values=data[indptr[m*n]:].reshape(k,total)
        indices[indptr[m*n]:].reshape(k,total)[:]=np.arange(total,dtype=index_dtype)
        parameter_values[:,(m-1)*n:]=dbc_dp.T
        dp=np.transpose(df_dp,(2,0,1))
        dp_middle=np.transpose(df_dp_middle,(2,0,1))
    dy=np.transpose(df_dy,(2,0,1))
    dy_middle=np.transpose(df_dy_middle,(2,0,1))
    hh=h[:,None,None]
    # Preserve the exact original whole-grid einsum layout below its n=50
    # switch. The actual high-M path uses the original per-node BLAS calls.
    block=radial_block if n>50 else m-1
    eye=np.identity(n)
    for first in range(0,m-1,block):
        stop=min(m-1,first+block)
        sl=slice(first,stop)
        hs=hh[sl]
        left=dy[first:stop]
        right=dy[first+1:stop+1]
        middle=dy_middle[sl]
        A=np.empty((stop-first,n,n),dtype=dy.dtype)
        A[:]=-eye
        A-=hs/6*(left+2*middle)
        temp=_bvp.stacked_matmul(middle,left)
        A-=hs**2/12*temp
        for offset,node in enumerate(range(first,stop)):
            view=node_view(data,node)
            view[:,0 if node==0 else n:n if node==0 else 2*n]=A[offset].T
        del A,temp
        B=np.empty((stop-first,n,n),dtype=dy.dtype)
        B[:]=eye
        B-=hs/6*(right+2*middle)
        temp=_bvp.stacked_matmul(middle,right)
        B+=hs**2/12*temp
        for offset,node in enumerate(range(first+1,stop+1)):
            node_view(data,node)[:,:n]=B[offset].T
        del B,temp
        if k:
            temp=_bvp.stacked_matmul(middle,dp[first:stop]-dp[first+1:stop+1])
            # This is also the original caller-visible in-place update.
            dp_middle[sl]+=0.125*hs*temp
            P=-hs/6*(dp[first:stop]+dp[first+1:stop+1]+4*dp_middle[sl])
            parameter_values[:,first*n:stop*n]=P.transpose(2,0,1).reshape(k,-1)
            del P,temp
    result=csc_matrix((data,indices,indptr),shape=(total,total),copy=False)
    result.has_sorted_indices=True
    result.has_canonical_format=True
    if record is not None:
        record(dict(n=n,m=m,k=k,stored_entries=nnz,radial_temporary_block=block,
            index_dtype=np.dtype(index_dtype).str,final_storage_bytes=
                int(data.nbytes+indices.nbytes+indptr.nbytes),
            old_COO_index_arrays_created=False,all_original_stored_zeros_retained=True,
            input_COO_indices_were_none=bool(i_jac is None and j_jac is None),
            original_block_formula_operation_order_preserved=True,
            original_parameter_middle_update_preserved=True,
            final_storage_shared_with_result=bool(np.shares_memory(data,result.data)
                and np.shares_memory(indices,result.indices) and np.shares_memory(indptr,result.indptr)),
            seconds=time.monotonic()-begin,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    return result


def install(radial_block=16,record=None):
    original_indices=_bvp.compute_jac_indices
    original_construct=_bvp.construct_global_jac
    wanted=['n','m','k','i_jac','j_jac','h','df_dy','df_dy_middle','df_dp',
            'df_dp_middle','dbc_dya','dbc_dyb','dbc_dp']
    if list(inspect.signature(original_construct).parameters)!=wanted:
        raise ValueError('The installed original collocation assembly signature changed')
    original_hashes={name:hashlib.sha256(inspect.getsource(value).encode()).hexdigest()
        for name,value in (('compute_jac_indices',original_indices),
                           ('construct_global_jac',original_construct),
                           ('stacked_matmul',_bvp.stacked_matmul))}

    def no_COO_indices(n,m,k):
        return None,None

    def direct(n,m,k,i,j,h,dy,dym,dp,dpm,bca,bcb,bcp):
        return construct(n,m,k,i,j,h,dy,dym,dp,dpm,bca,bcb,bcp,
                         radial_block=radial_block,record=record)

    _bvp.compute_jac_indices=no_COO_indices
    _bvp.construct_global_jac=direct

    def restore():
        _bvp.compute_jac_indices=original_indices
        _bvp.construct_global_jac=original_construct

    return original_hashes,restore
