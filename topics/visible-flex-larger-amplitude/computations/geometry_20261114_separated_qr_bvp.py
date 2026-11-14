#!/usr/bin/env python3
"""Disk-backed orthogonal elimination of separated collocation boundaries.

This factors the same finite collocation linear system. Every local left and
right block is retained, and a thin QR transports the nullspace of the left
boundary. Large local blocks are disk-backed; no frequency is removed.
Orthogonal elimination can still be numerically ill-conditioned. Its linear
residual is reported, and it is not a mathematical existence certificate.
"""
import gc
import gzip
import json
import resource
import shutil
import tempfile
import time
import warnings
from pathlib import Path
import numpy as np
from scipy.linalg import lu_factor,lu_solve,qr,solve_triangular,LinAlgWarning
import scipy.integrate._bvp as backend

native_prepare_sys=backend.prepare_sys


def local_blocks(h,A,B,C):
    eye=np.eye(A.shape[0],dtype=A.dtype)
    L=-eye.copy();L-=h/6*(A+2*B)
    L-=h*h/12*backend.stacked_matmul(B[None,:,:],A[None,:,:])[0]
    R=eye.copy();R-=h/6*(C+2*B)
    R+=h*h/12*backend.stacked_matmul(B[None,:,:],C[None,:,:])[0]
    return L,R


class DiskQRFactor:
    def __init__(self,n,m,left,right,left_count,work,verify_residual=True):
        self.n=n;self.m=m;self.nl=left_count;self.k=n-left_count
        self.shape=(n*m,n*m);self.nnz=2*m*n*n
        self.left=np.asarray(left[:self.nl]);self.right=np.asarray(right[self.nl:])
        if np.any(left[self.nl:]!=0)or np.any(right[:self.nl]!=0):
            raise ValueError('This elimination requires purely separated boundary rows')
        self.directory=Path(tempfile.mkdtemp(prefix='separated-qr-',dir=work))
        self.verify_residual=verify_residual;self.solve_count=0;self.started=time.monotonic()
        Q,R=qr(self.left.T,mode='full',check_finite=False)
        self.left_Q=Q[:,:self.nl];self.left_R=R[:self.nl,:]
        self.U=np.empty((m,n,self.k));self.U[0]=Q[:,self.nl:]
        self.transport=np.empty((m-1,self.k,self.k))
        self.next_interval=0

    def append(self,j,L,R):
        if j!=self.next_interval:
            raise ValueError('Intervals must be appended sequentially')
        with warnings.catch_warnings():
            warnings.simplefilter('error',LinAlgWarning)
            try:
                LU,piv=lu_factor(R.copy(order='F'),overwrite_a=True,check_finite=False)
            except LinAlgWarning as error:
                raise RuntimeError('Local right collocation block is singular; QR elimination broke down')from error
        T=lu_solve((LU,piv),-L,check_finite=False)
        self.U[j+1],self.transport[j]=qr(T@self.U[j],mode='economic',check_finite=False)
        np.savez(self.directory/f'{j:05d}.npz',L=L,R=R,LU=LU,piv=piv,T=T)
        self.next_interval+=1

    def finish(self):
        if self.next_interval!=self.m-1:
            raise ValueError('The complete collocation matrix has not been provided')
        small=self.right@self.U[-1]
        with warnings.catch_warnings():
            warnings.simplefilter('error',LinAlgWarning)
            try:
                self.end_factor=lu_factor(small,check_finite=False)
            except LinAlgWarning as error:
                raise RuntimeError('Terminal reduced matrix is singular')from error
        singular=np.linalg.svd(small,compute_uv=False)
        print(json.dumps(dict(event='separated_qr_factor',n=self.n,nodes=self.m,free_dimensions=self.k,
                              reduced_condition=float(singular.max()/singular.min()),
                              seconds=time.monotonic()-self.started,
                              maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        return self

    def solve(self,rhs):
        n,m,k=self.n,self.m,self.k
        rhs=np.asarray(rhs);col=rhs[:(m-1)*n].reshape((m-1,n))
        bcl=rhs[(m-1)*n:(m-1)*n+self.nl];bcr=rhs[(m-1)*n+self.nl:]
        p=np.empty((m,n));offset=np.empty((m-1,k))
        p[0]=self.left_Q@solve_triangular(self.left_R.T,bcl,lower=True,check_finite=False)
        for j in range(m-1):
            with np.load(self.directory/f'{j:05d}.npz')as block:
                raw=block['T']@p[j]+lu_solve((block['LU'],block['piv']),col[j],check_finite=False)
            offset[j]=self.U[j+1].T@raw
            p[j+1]=raw-self.U[j+1]@offset[j]
        coordinate=lu_solve(self.end_factor,bcr-self.right@p[-1],check_finite=False)
        answer=np.empty((m,n));answer[-1]=p[-1]+self.U[-1]@coordinate
        for j in range(m-2,-1,-1):
            coordinate=solve_triangular(self.transport[j],coordinate-offset[j],check_finite=False)
            answer[j]=p[j]+self.U[j]@coordinate
        self.solve_count+=1
        if self.verify_residual:
            residual=np.empty_like(rhs)
            for j in range(m-1):
                with np.load(self.directory/f'{j:05d}.npz')as block:
                    residual[j*n:(j+1)*n]=block['L']@answer[j]+block['R']@answer[j+1]-col[j]
            residual[(m-1)*n:(m-1)*n+self.nl]=self.left@answer[0]-bcl
            residual[(m-1)*n+self.nl:]=self.right@answer[-1]-bcr
            absolute=float(np.max(abs(residual)));scale=float(np.max(abs(rhs)))
            print(json.dumps(dict(event='separated_qr_solve',count=self.solve_count,
                                  linear_residual_max=absolute,rhs_max=scale,
                                  linear_relative_residual=absolute/max(scale,np.finfo(float).tiny),
                                  solution_max=float(np.max(abs(answer))),
                                  maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        return answer.ravel()

    def close(self):
        directory=getattr(self,'directory',None)
        if directory is not None:
            shutil.rmtree(directory,ignore_errors=True)
            self.directory=None

    def __del__(self):
        self.close()


def enable(work,left_count,chunk_size=16,checkpoint=None,M=None,N=None):
    work=Path(work);work.mkdir(parents=True,exist_ok=True)
    counter=0
    def prepare_sys(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        if k or fun_jac is None or bc_jac is None:
            raise ValueError('Separated QR requires the complete analytic no-parameter Jacobian')
        mid=x[:-1]+.5*h
        def col_fun(y,p):
            return backend.collocation_fun(fun,y,p,x,h)
        def sys_jac(y,p,y_mid,f,f_mid,bc0):
            nonlocal counter
            counter+=1
            if checkpoint is not None:
                record=dict(scope='Unconverged full Newton iterate, no solver success implied.',
                            M=M,N=N,mesh=x.tolist(),states=y.T.tolist(),rhs=f.T.tolist(),
                            global_jacobian_call=counter,linear_backend='separated-qr')
                Path(checkpoint).write_bytes(gzip.compress((json.dumps(record)+'\n').encode(),mtime=0))
            left,right,unused=bc_jac(y[:,0],y[:,-1],p)
            factor=DiskQRFactor(n,m,left,right,left_count,work)
            for j0 in range(0,m-1,chunk_size):
                j1=min(m-1,j0+chunk_size)
                node,unused=fun_jac(x[j0:j1+1],y[:,j0:j1+1],p)
                middle,unused=fun_jac(mid[j0:j1],y_mid[:,j0:j1],p)
                for j in range(j0,j1):
                    L,R=local_blocks(h[j],node[:,:,j-j0],middle[:,:,j-j0],node[:,:,j-j0+1])
                    factor.append(j,L,R)
                del node,middle,L,R
                gc.collect()
                print(json.dumps(dict(event='separated_qr_chunk',jacobian=counter,intervals=j1,total=m-1,
                                      maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
            return factor.finish()
        return col_fun,sys_jac
    backend.prepare_sys=prepare_sys


def factor(matrix):
    if not isinstance(matrix,DiskQRFactor):
        raise TypeError('Expected a separated QR collocation system')
    return matrix
