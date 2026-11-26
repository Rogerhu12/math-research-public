#!/usr/bin/env python3
"""Blockwise full-Gram J/JT with banded H1 preconditioning.

All physical rows and all Cartesian Fourier/B-spline columns are retained.
Only first position derivatives are cached globally; complete position
two-jets and observer quantities are evaluated one radial block at a time.
The quintic B-spline H1 matrix has half-bandwidth five. Its Cholesky factors
are used as triangular band solves, not stored dense inverse square roots.
"""
import importlib.util
from pathlib import Path
import numpy as np
from scipy.linalg import cholesky_banded, solve_banded
from scipy.sparse.linalg import LinearOperator

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('stream_full_gram_bvp',HERE/'6a65-m12-positive-ramp-position-bvp.py')
bvp=importlib.util.module_from_spec(spec);spec.loader.exec_module(bvp)


def chunks(length,block):
    for left in range(0,length,block):yield slice(left,min(length,left+block))


def packet(basis,matrices,coeff,N):
    B0,B1,B2=matrices
    a0,a1,a2=B0@coeff,B1@coeff,B2@coeff
    return np.stack((basis.angular(a0,N),basis.angular(a1,N),basis.angular(a0,N,1),
                     basis.angular(a2,N),basis.angular(a1,N,1),basis.angular(a0,N,2)),axis=1)


def merge_statistics(total,part,offset):
    if total is None:
        result=part.copy();result['peak_radial_index']+=offset;return result
    if part['metric_peak']>total['metric_peak']:
        total['metric_peak']=part['metric_peak']
        total['peak_radial_index']=part['peak_radial_index']+offset
        total['peak_angle_index']=part['peak_angle_index']
    total['weighted_energy']+=part['weighted_energy']
    total['curvature_peak']=max(total['curvature_peak'],part['curvature_peak'])
    total['support_lower']=min(total['support_lower'],part['support_lower'])
    return total


def observe(basis,nodes,weights,background,coeff,N,block=24):
    """Observe the complete same position map, without global two-jet arrays."""
    total=None
    for sl in chunks(len(nodes),block):
        p,bb=background(nodes[sl],N)
        p+=packet(basis,basis.matrices(nodes[sl]),coeff,N)
        total=merge_statistics(total,bvp.statistics(p,bb,weights[sl]),sl.start)
    return total


class StreamingLinearized:
    def __init__(self,basis,nodes,weights,background,coeff,N,block=24):
        self.basis,self.nodes,self.weights,self.N,self.block=basis,nodes,weights,N,block
        self.B0,self.B1,self.B2=basis.matrices(nodes)
        self.Xs=np.empty((len(nodes),N,3));self.Xt=np.empty_like(self.Xs)
        self.bb=np.empty((len(nodes),N));self.weight=np.empty_like(self.bb)
        self.residual=np.empty((len(nodes),N,3))
        self.statistics=None
        for sl in chunks(len(nodes),block):
            p,bb=background(nodes[sl],N)
            p+=packet(basis,(self.B0[sl],self.B1[sl],self.B2[sl]),coeff,N)
            self.Xs[sl]=p[:,1];self.Xt[sl]=p[:,2];self.bb[sl]=bb
            self.weight[sl]=np.sqrt(weights[sl,None]*bb/N)
            self.residual[sl]=bvp.gram(p[:,1],p[:,2],bb)*self.weight[sl,:,None]
            self.statistics=merge_statistics(self.statistics,bvp.statistics(p,bb,weights[sl]),sl.start)
        mass=self.B0.T@self.B0.multiply(weights[:,None])
        stiff=self.B1.T@self.B1.multiply(weights[:,None])
        bandwidth=5;self.bandwidth=bandwidth;self.factors={}
        mass_band=np.array([np.pad(mass.diagonal(-d),(0,d)) for d in range(bandwidth+1)])
        stiff_band=np.array([np.pad(stiff.diagonal(-d),(0,d)) for d in range(bandwidth+1)])
        # Structural zeros outside the quintic overlap must really be zero.
        if mass.nnz and max(abs(mass.tocoo().row-mass.tocoo().col))>bandwidth:
            raise ArithmeticError('B-spline mass exceeds the declared band')
        for k in np.unique(abs(basis.modes)):
            lower=cholesky_banded(stiff_band+(float(k*k)+.01)*mass_band,lower=True,check_finite=False)
            upper=np.zeros_like(lower)
            for d in range(bandwidth+1):upper[bandwidth-d,d:]=lower[d,:basis.nb-d]
            self.factors[int(k)]=(lower,upper)
        self.shape=(len(nodes)*N*3,basis.nb*basis.na)
        self.operator=LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=float)

    def unpack(self,x):
        x=np.asarray(x).reshape(self.basis.na,self.basis.nb);out=np.empty((self.basis.nb,self.basis.na))
        for a,k in enumerate(self.basis.modes):
            out[:,a]=solve_banded((0,self.bandwidth),self.factors[abs(int(k))][1],x[a],check_finite=False)
        return out

    def transpose_precondition(self,gradient):
        out=np.empty((self.basis.na,self.basis.nb))
        for a,k in enumerate(self.basis.modes):
            out[a]=solve_banded((self.bandwidth,0),self.factors[abs(int(k))][0],gradient[:,a],check_finite=False)
        return out.ravel()

    def matvec(self,x):
        coeff=self.unpack(x);out=np.empty((len(self.nodes),self.N,3))
        for sl in chunks(len(self.nodes),self.block):
            Ws=self.basis.angular(self.B1[sl]@coeff,self.N)
            Wt=self.basis.angular(self.B0[sl]@coeff,self.N,1)
            xs,xt,bb=self.Xs[sl],self.Xt[sl],self.bb[sl]
            out[sl,:,0]=2*np.sum(xs*Ws,axis=-1)
            out[sl,:,1]=np.sqrt(2)*np.sum(xs*Wt+xt*Ws,axis=-1)/bb
            out[sl,:,2]=2*np.sum(xt*Wt,axis=-1)/(bb*bb)
            out[sl]*=self.weight[sl,:,None]
        return out.ravel()

    def rmatvec(self,x):
        x=np.asarray(x).reshape(len(self.nodes),self.N,3)
        gradient=np.zeros((self.basis.nb,self.basis.na))
        for sl in chunks(len(self.nodes),self.block):
            z=x[sl]*self.weight[sl,:,None]
            e,f,g=z[...,0],z[...,1],z[...,2]
            xs,xt,bb=self.Xs[sl],self.Xt[sl],self.bb[sl]
            V=2*e[...,None]*xs+(np.sqrt(2)*f/bb)[...,None]*xt
            W=(np.sqrt(2)*f/bb)[...,None]*xs+(2*g/(bb*bb))[...,None]*xt
            gradient+=self.B1[sl].T@self.basis.angular_adjoint(V)+self.B0[sl].T@self.basis.angular_adjoint(W,1)
        return self.transpose_precondition(gradient)
