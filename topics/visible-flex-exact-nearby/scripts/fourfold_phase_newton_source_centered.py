#!/usr/bin/env python3
"""R117 source with midpoint Fourier products and a complete Wiener error.

Every nonconstant midpoint below is an exactly representable dyadic.  Their
uncertainty, rounding, and infinite primitive tails are paid in the complete
A0 norm before the next Fourier multiplication. The real constant box is
kept separately so exact nonmean projection removes its uncertainty. This
avoids sending one
coefficient box repeatedly through forward/backward interval FFTs.

The source formula, same initial target, exact scalar germs, whole affine
parameter interval, and angular-cell cover are those of the original R117
producer.  This program does not change the candidate or delete mean modes.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np
from flint import arb

import fourfold_phase_two_jet_newton_source as source
from fourfold_phase_correlated_curvature import Polynomial, sha
from fourfold_phase_beta_bulk_box import Box, CBox, zeros, reduce_box
from fourfold_phase_uniform_tail import up


def midpoint_and_fee(coefficient):
    """Choose a dyadic polynomial and bound the complete A0 difference."""
    mids=[];radii=[]
    for part in (coefficient.real,coefficient.imag):
        midpoint=part.lo/2+part.hi/2
        midpoint=np.minimum(np.maximum(midpoint,part.lo),part.hi)
        mids.append(midpoint)
    # Choose an exactly real trigonometric polynomial.  This is a choice of
    # reference, not an intersection that discards coefficient uncertainty.
    n=len(mids[0]);pos=np.arange(1,(n+1)//2)
    real=mids[0][pos]/2+mids[0][-pos]/2
    imag=mids[1][pos]/2-mids[1][-pos]/2
    mids[0][pos]=real;mids[0][-pos]=real
    mids[1][pos]=imag;mids[1][-pos]=-imag
    mids[1][0]=0
    if n%2==0:mids[1][n//2]=0
    for midpoint,part in zip(mids,(coefficient.real,coefficient.imag)):
        radius=np.maximum(up(abs(midpoint-part.lo)),up(abs(part.hi-midpoint)))
        radii.append(radius)
    radii[0][0]=0;radii[1][0]=0
    radius=Box(up(radii[0]+radii[1]))
    fee=arb(float(reduce_box(radius).hi)).upper()
    result=CBox(Box(mids[0]),Box(mids[1]))
    if coefficient.imag.lo[0]>0 or coefficient.imag.hi[0]<0:
        raise ValueError("real constant coefficient lost zero imaginary part")
    result[0]=CBox(coefficient.real[0],0.)
    return result,fee


class CenteredPolynomial(Polynomial):
    def __init__(self,coefficient,error,degree,fft):
        # Fourier support is mathematical, not an observed numerical cutoff.
        n=len(coefficient.real.lo)
        modes=np.asarray([k if k<n//2 else k-n for k in range(n)])
        out=np.abs(modes)>degree
        coefficient=CBox(Box(coefficient.real.lo.copy(),coefficient.real.hi.copy()),
                         Box(coefficient.imag.lo.copy(),coefficient.imag.hi.copy()))
        if np.any(coefficient.real.lo[out]>0) or np.any(coefficient.real.hi[out]<0):
            raise ValueError("exact zero Fourier support lost its real enclosure")
        if np.any(coefficient.imag.lo[out]>0) or np.any(coefficient.imag.hi[out]<0):
            raise ValueError("exact zero Fourier support lost its imaginary enclosure")
        coefficient[out]=0
        midpoint,fee=midpoint_and_fee(coefficient)
        super().__init__(midpoint,arb(error)+fee,degree,fft)

    def coerce(self,value):
        if isinstance(value,Polynomial):
            if value.grid!=self.grid or value.fft is not self.fft:
                raise ValueError("different polynomial algebras")
            return value
        c=zeros((self.grid,));c[0]=CBox.from_acb(source.acb(value))
        return CenteredPolynomial(c,arb(0),0,self.fft)

    def __add__(self,value):
        value=self.coerce(value)
        return CenteredPolynomial(self.c+value.c,self.error+value.error,
                                  max(self.degree,value.degree),self.fft)
    __radd__=__add__

    def __neg__(self):
        return CenteredPolynomial(-self.c,self.error,self.degree,self.fft)

    def __mul__(self,value):
        value=self.coerce(value)
        degree=self.degree+value.degree
        if degree>=self.grid//2:
            raise ValueError("aliased finite polynomial product refused")
        a0,b0=self.c[0],value.c[0]
        if self.degree==0:
            coefficient=value.c*a0
        elif value.degree==0:
            coefficient=self.c*b0
        else:
            sa=self.samples_without_constant();sb=value.samples_without_constant()
            coefficient=self.fft.fft(sa*sb)/self.grid
            a=CBox(Box(self.c.real.lo.copy(),self.c.real.hi.copy()),
                   Box(self.c.imag.lo.copy(),self.c.imag.hi.copy()))
            b=CBox(Box(value.c.real.lo.copy(),value.c.real.hi.copy()),
                   Box(value.c.imag.lo.copy(),value.c.imag.hi.copy()))
            a[0]=0;b[0]=0
            coefficient=coefficient+a*b0+b*a0
            coefficient[0]=coefficient[0]+a0*b0
        error=self.norm()*value.error+value.norm()*self.error+self.error*value.error
        return CenteredPolynomial(coefficient,error,degree,self.fft)
    __rmul__=__mul__


class CenteredSource(source.TwoJetNewtonSource):
    def lift(self,finite,error):
        c=zeros((self.product_grid,))
        frequency=np.asarray(self.frequency)//4
        c[frequency%self.product_grid]=finite
        c[(-self.nodes//2)%self.product_grid]=0
        return CenteredPolynomial(c,error,self.nodes//2-1,self.polynomial_fft)


def main():
    source.Polynomial=CenteredPolynomial
    source.TwoJetNewtonSource=CenteredSource
    source.main()
    position=sys.argv.index('--out')
    path=Path(sys.argv[position+1])
    if path.suffix=='.gz':
        import gzip
        doc=json.loads(gzip.decompress(path.read_bytes()))
    else:doc=json.loads(path.read_text())
    doc['kind']='actual_R117_centered_polynomial_two_jet_Newton_source'
    doc['centered_convolution_source_sha256']=sha(__file__)
    doc['centered_convolution_contract']='Exact dyadic nonconstant polynomial and real constant box plus full A0 error; nonconstant coefficient boxes converted to complete Wiener error at every algebra operation; mathematical support retained.'
    source.save(path,doc)


if __name__=='__main__':main()
