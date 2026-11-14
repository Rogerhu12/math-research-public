"""Same Lobatto Jacobian, assembled by interval directly into CSC.

This design system has just one ODE parameter: the last parameter T.
All other parameters enter only the boundary equations.  Exact zero ODE
columns are asserted, never thresholded.  No global COO indices or global
endpoint/midpoint Jacobian stacks are allocated.  Residuals stay SciPy's.
"""
import time
import numpy as np
from scipy.sparse import csc_matrix
import scipy.integrate._bvp as bvp

STATUS = dict(phase='not_started', assembled=0)
ORIGINAL_PREPARE = bvp.prepare_sys


def prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
    if fun_jac is None or bc_jac is None or k < 1:
        raise ValueError('This design entry requires analytic Jacobians and the last T parameter')
    if m < 2:
        raise ValueError('At least two radial nodes are required')
    xm = x[:-1]+.5*h

    def col_fun(y, p):
        return bvp.collocation_fun(fun,y,p,x,h)

    def sys_jac(y,p,ym,f,fm,bc0):
        began=time.monotonic();size=n*m+k;bcrow=n*(m-1);nrows=n+k
        STATUS.update(phase='stream_csc',nodes=m,dimension=n,interval=0,intervals=m-1)
        counts=np.empty(size,dtype=np.int64)
        for node in range(m):
            counts[node*n:(node+1)*n]=n*(int(node>0)+int(node<m-1))+nrows*int(node in (0,m-1))
        counts[n*m:]=nrows;counts[-1]+=bcrow
        pointers=np.r_[0,np.cumsum(counts)]
        if pointers[-1]>=2**31:
            raise OverflowError('The declared CSC representation requires 64-bit indices')
        pointers=pointers.astype(np.int32)
        indices=np.empty(int(pointers[-1]),dtype=np.int32)
        data=np.empty(int(pointers[-1]),dtype=np.result_type(y,p))
        for node in range(m):
            rows=[]
            if node>0:rows.append(np.arange((node-1)*n,node*n,dtype=np.int32))
            if node<m-1:rows.append(np.arange(node*n,(node+1)*n,dtype=np.int32))
            if node in (0,m-1):rows.append(np.arange(bcrow,size,dtype=np.int32))
            row=np.concatenate(rows)
            indices[pointers[node*n]:pointers[(node+1)*n]].reshape(n,len(row))[:]=row
        for parameter in range(k):
            column=n*m+parameter
            if parameter==k-1:
                indices[pointers[column]:pointers[column+1]]=np.arange(size,dtype=np.int32)
            else:
                indices[pointers[column]:pointers[column+1]]=np.arange(bcrow,size,dtype=np.int32)
        left,right,param=bc_jac(y[:,0],y[:,-1],p)
        if left.shape!=(nrows,n) or right.shape!=(nrows,n) or param.shape!=(nrows,k):
            raise ValueError('Unexpected boundary Jacobian shape')
        data[pointers[0]:pointers[n]].reshape(n,n+nrows)[:,n:]=left.T
        data[pointers[(m-1)*n]:pointers[m*n]].reshape(n,n+nrows)[:,n:]=right.T
        for parameter in range(k):
            column=n*m+parameter
            data[pointers[column+1]-nrows:pointers[column+1]]=param[:,parameter]

        def point_jac(xx,yy):
            state,parameters=fun_jac(np.asarray([xx]),yy[:,None],p)
            if state.shape!=(n,n,1) or parameters.shape!=(n,k,1):
                raise ValueError('Unexpected point Jacobian shape')
            if np.any(parameters[:,:-1,0]!=0):
                raise ValueError('A previously boundary-only parameter now enters the ODE')
            return state[:,:,0].copy(),parameters[:,-1,0].copy()

        eye=np.eye(n,dtype=data.dtype)
        jl,pl=point_jac(x[0],y[:,0])
        for interval in range(m-1):
            jr,pr=point_jac(x[interval+1],y[:,interval+1])
            jm,pm=point_jac(xm[interval],ym[:,interval])
            hi=h[interval]
            a=-eye.copy();a-=hi/6*(jl+2*jm);a-=hi**2/12*(jm@jl)
            b=eye.copy();b-=hi/6*(jr+2*jm);b+=hi**2/12*(jm@jr)
            pm+=.125*hi*(jm@(pl-pr))
            c=-hi/6*(pl+pr+4*pm)
            start=pointers[interval*n];stop=pointers[(interval+1)*n]
            block=data[start:stop].reshape(n,-1)
            offset=n*int(interval>0);block[:,offset:offset+n]=a.T
            start=pointers[(interval+1)*n];stop=pointers[(interval+2)*n]
            data[start:stop].reshape(n,-1)[:,:n]=b.T
            start=pointers[-2]+interval*n
            data[start:start+n]=c
            jl,pl=jr,pr
            STATUS.update(interval=interval+1,seconds=time.monotonic()-began)
        answer=csc_matrix((data,indices,pointers),shape=(size,size),copy=False)
        answer.eliminate_zeros()
        if not answer.has_sorted_indices or not answer.has_canonical_format:
            raise AssertionError('Direct CSC construction must be sorted with no duplicate entries')
        STATUS.update(phase='assembled',assembled=STATUS['assembled']+1,
                      entries=int(answer.nnz),seconds=time.monotonic()-began,
                      bytes=int(answer.data.nbytes+answer.indices.nbytes+answer.indptr.nbytes))
        return answer

    return col_fun,sys_jac


def install():
    bvp.prepare_sys=prepare_sys
