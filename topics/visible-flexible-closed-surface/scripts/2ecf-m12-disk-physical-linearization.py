#!/usr/bin/env python3
"""Fixed original physical J rows on disk; all normal contractions streamed.

Only storage and reduction grouping change. Each stored block is read back and
compared byte for byte. No row, Fourier channel, fixed source or g is changed.
The normal gradient retains the original radial-block accumulation order.
Scalar slope/norm use block sums; their floating differences must be recorded.
"""
from __future__ import annotations
import hashlib,json,mmap,shutil,tempfile,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.linalg import cholesky_banded
from scipy.sparse.linalg import LinearOperator


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

class DiskArray:
    def __init__(self,path,shape):
        self.path=Path(path);self.shape=tuple(shape);self.dtype=np.dtype(np.float64)
        self._map=np.lib.format.open_memmap(self.path,mode='w+',dtype=self.dtype,shape=self.shape)
        self.nbytes=int(np.prod(self.shape))*8;self.writes=self.reads=0;self._row_sha=[None]*self.shape[0]
    def _drop(self):
        self._map._mmap.madvise(mmap.MADV_DONTNEED)
    def __setitem__(self,key,value):
        if self._map is None:raise ValueError('Closed physical storage')
        expected=np.asarray(value,dtype=np.float64)
        self._map[key]=expected;self._map.flush()
        actual=np.array(self._map[key],copy=True)
        if actual.shape!=expected.shape or actual.tobytes()!=expected.tobytes():raise ArithmeticError('Disk physical-row write changed actual original values')
        if not isinstance(key,slice) or key.indices(self.shape[0])[2]!=1:raise ValueError('Contiguous radial row slices required')
        rows=range(*key.indices(self.shape[0]))
        for j,row in enumerate(rows):self._row_sha[row]=hashlib.sha256(actual[j].tobytes()).hexdigest()
        self.writes+=1;self._drop()
    def __getitem__(self,key):
        if self._map is None:raise ValueError('Closed physical storage')
        if not isinstance(key,slice) or key.indices(self.shape[0])[2]!=1:raise ValueError('Contiguous radial row slices required')
        out=np.array(self._map[key],copy=True);self._drop()
        for j,row in enumerate(range(*key.indices(self.shape[0]))):
            if hashlib.sha256(out[j].tobytes()).hexdigest()!=self._row_sha[row]:raise ArithmeticError('Stored physical row changed')
        self.reads+=1;return out
    def close(self):
        if self._map is not None:self._map.flush();self._map._mmap.close();self._map=None


def build_linearized(stream,basis,nodes,weights,background,coeff,N,block=24,directory=None):
    """Original StreamingLinearized construction, with five array stores only."""
    began=time.monotonic();root=Path(tempfile.mkdtemp(prefix='physical-J-blocks-',dir=directory))
    linear=SimpleNamespace(basis=basis,nodes=nodes,weights=weights,N=N,block=block)
    linear.B0,linear.B1,linear.B2=basis.matrices(nodes)
    for name,shape in [('Xs',(len(nodes),N,3)),('Xt',(len(nodes),N,3)),('bb',(len(nodes),N)),('weight',(len(nodes),N)),('residual',(len(nodes),N,3))]:
        setattr(linear,name,DiskArray(root/(name+'.npy'),shape))
    linear.statistics=None
    for sl in stream.chunks(len(nodes),block):
        p,bb=background(nodes[sl],N)
        p+=stream.packet(basis,(linear.B0[sl],linear.B1[sl],linear.B2[sl]),coeff,N)
        linear.Xs[sl]=p[:,1];linear.Xt[sl]=p[:,2];linear.bb[sl]=bb
        weight=np.sqrt(weights[sl,None]*bb/N);linear.weight[sl]=weight
        linear.residual[sl]=stream.bvp.gram(p[:,1],p[:,2],bb)*weight[:,:,None]
        linear.statistics=stream.merge_statistics(linear.statistics,stream.bvp.statistics(p,bb,weights[sl]),sl.start)
    mass=linear.B0.T@linear.B0.multiply(weights[:,None]);stiff=linear.B1.T@linear.B1.multiply(weights[:,None])
    linear.bandwidth=5;linear.factors={}
    mass_band=np.array([np.pad(mass.diagonal(-d),(0,d)) for d in range(6)])
    stiff_band=np.array([np.pad(stiff.diagonal(-d),(0,d)) for d in range(6)])
    if mass.nnz and max(abs(mass.tocoo().row-mass.tocoo().col))>5:raise ArithmeticError('Original mass bandwidth changed')
    for k in np.unique(abs(basis.modes)):
        lower=cholesky_banded(stiff_band+(float(k*k)+.01)*mass_band,lower=True,check_finite=False)
        upper=np.zeros_like(lower)
        for d in range(6):upper[5-d,d:]=lower[d,:basis.nb-d]
        linear.factors[int(k)]=(lower,upper)
    linear.shape=(len(nodes)*N*3,basis.nb*basis.na)
    linear.disk_directory=root
    linear.disk_receipt={'schema':'2ecf-M12-original-physical-J-disk-storage-v1','script_sha256':sha(__file__),
       'original_stream_source_sha256':sha(stream.__file__),'physical_rows':linear.shape[0],
       'all_original_rows_and_columns_preserved':True,'all_original_five_arrays_checked_byte_for_byte_after_write':True,
       'every_consumed_physical_row_SHA256_checked':True,'coefficient_bytes_sha256':hashlib.sha256(np.asarray(coeff).tobytes()).hexdigest(),
       'nodes_bytes_sha256':hashlib.sha256(np.asarray(nodes).tobytes()).hexdigest(),
       'actual_block_size':block,'arrays':{n:{'shape':list(getattr(linear,n).shape),'bytes':getattr(linear,n).nbytes,
          'writes':getattr(linear,n).writes} for n in ['Xs','Xt','bb','weight','residual']},
       'MADV_DONTNEED_after_each_read_and_write':True,'no_full_global_Jv_or_residual_sum':True,
       'construction_seconds':time.monotonic()-began}
    return linear


def blocks(linear):
    for left in range(0,len(linear.nodes),linear.block):yield slice(left,min(left+linear.block,len(linear.nodes)))


def raw_matvec_block(linear,coeff,sl,xs=None,xt=None,bb=None,weight=None):
    basis=linear.basis
    if xs is None:xs=linear.Xs[sl];xt=linear.Xt[sl];bb=linear.bb[sl];weight=linear.weight[sl]
    Ws=basis.angular(linear.B1[sl]@coeff,linear.N)
    Wt=basis.angular(linear.B0[sl]@coeff,linear.N,1)
    out=np.empty((sl.stop-sl.start,linear.N,3))
    out[:,:,0]=2*np.sum(xs*Ws,axis=-1)
    out[:,:,1]=np.sqrt(2)*np.sum(xs*Wt+xt*Ws,axis=-1)/bb
    out[:,:,2]=2*np.sum(xt*Wt,axis=-1)/(bb*bb)
    out*=weight[:,:,None];return out


def raw_transpose_block(linear,x,sl,xs=None,xt=None,bb=None,weight=None):
    if xs is None:xs=linear.Xs[sl];xt=linear.Xt[sl];bb=linear.bb[sl];weight=linear.weight[sl]
    z=x*weight[:,:,None];e,f,g=z[...,0],z[...,1],z[...,2]
    V=2*e[...,None]*xs+(np.sqrt(2)*f/bb)[...,None]*xt
    W=(np.sqrt(2)*f/bb)[...,None]*xs+(2*g/(bb*bb))[...,None]*xt
    return linear.B1[sl].T@linear.basis.angular_adjoint(V)+linear.B0[sl].T@linear.basis.angular_adjoint(W,1)


def initial_gradient(linear):
    gradient=np.zeros((linear.basis.nb,linear.basis.na))
    for sl in blocks(linear):gradient+=raw_transpose_block(linear,linear.residual[sl],sl)
    return gradient


def normal_direction(linear,coeff):
    """All original JT(Jd+r) rows; no full Jd or Jd+r array is allocated."""
    gradient=np.zeros((linear.basis.nb,linear.basis.na));slope=0.;norm_squared=0.
    for sl in blocks(linear):
        xs=linear.Xs[sl];xt=linear.Xt[sl];bb=linear.bb[sl];weight=linear.weight[sl];residual=linear.residual[sl]
        jv=raw_matvec_block(linear,coeff,sl,xs,xt,bb,weight)
        slope+=float(np.dot(residual.ravel(),jv.ravel()));norm_squared+=float(np.dot(jv.ravel(),jv.ravel()))
        gradient+=raw_transpose_block(linear,jv+residual,sl,xs,xt,bb,weight)
    return {'physical_normal':gradient,'unregularized_slope':slope,'Jd_norm_squared':norm_squared,
       'scalar_reduction_is_sum_of_block_dots_not_one_global_dot':True,'all_original_physical_rows_retained':True}


def cleanup(linear):
    rec=linear.disk_receipt
    for n in ['Xs','Xt','bb','weight','residual']:
        a=getattr(linear,n);rec['arrays'][n]['actual_reads']=a.reads;a.close()
    shutil.rmtree(linear.disk_directory)
    rec['private_physical_arrays_removed_after_last_use']=True
