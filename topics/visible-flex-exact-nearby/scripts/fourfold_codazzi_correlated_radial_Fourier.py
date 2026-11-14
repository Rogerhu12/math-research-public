#!/usr/bin/env python3
"""Shared radial-polynomial / full finite-Fourier interval algebra.

Intrinsic errors are radial scalar errors.  Consequently every expression
here still has a proved finite angular support, including its uniform
error.  Differentiating that error uses its actual support; no unknown
infinite angular tail is differentiated.  The intrinsic primitive tail is
already included in the true scalar input intervals.
"""
from __future__ import annotations
from fractions import Fraction
from math import factorial
import numpy as np
from flint import arb,acb
from fourfold_phase_beta_bulk_box import Box,CBox,zeros,arb_box,reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    add,mul,scale,evaluate,centre_real,exact_candidate_series,wiener_upper)


def real_cb(z):
    if not np.all((z.imag.lo<=0)&(z.imag.hi>=0)):
        raise ArithmeticError('a genuine real full Fourier field lost reality')
    return z.real


def scalar_arb(value):
    return arb(float(value.lo)).union(arb(float(value.hi)))


class RadialFourier:
    """Real sample-polynomial plus a complete uniform Wiener error."""
    def __init__(self,coefficients,degree,grid,fft,norm,error=arb(0),error_degree=None):
        self.coefficients=list(coefficients);self.degree=int(degree)
        self.grid=int(grid);self.fft=fft;self.norm=arb(norm).upper()
        self.error=arb(error).upper()
        self.error_degree=self.degree if error_degree is None else int(error_degree)
        if not self.coefficients or self.degree<0 or 2*self.degree>=self.grid:
            raise ValueError('complete unaliased finite angular support required')
        if self.error<0 or self.error_degree>self.degree:
            raise ValueError('invalid actual finite-support error budget')
        self._fourier=None

    @classmethod
    def scalar(cls,values,grid,fft):
        c=[];norm=arb(0);error=arb(0)
        for v in values:
            box=v if isinstance(v,Box) else arb_box(arb(v))
            mid,delta=centre_real(box);c.append(mid)
            norm+=arb(float(mid.abs_upper())).upper()
            error+=arb(float(delta.abs_upper())).upper()
        return cls(c,0,grid,fft,norm,error,0)

    def coerce(self,x):
        if isinstance(x,RadialFourier):
            if x.grid!=self.grid or x.fft is not self.fft:
                raise ValueError('incompatible exact Fourier contexts')
            return x
        return self.scalar([x],self.grid,self.fft)

    def __add__(self,x):
        x=self.coerce(x)
        return RadialFourier(add(self.coefficients,x.coefficients),max(self.degree,x.degree),
            self.grid,self.fft,self.norm+x.norm,self.error+x.error,
            max(self.error_degree,x.error_degree))
    __radd__=__add__
    def __neg__(self):
        return RadialFourier(scale(self.coefficients,-1),self.degree,self.grid,self.fft,
            self.norm,self.error,self.error_degree)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x);degree=self.degree+x.degree
        error=self.norm*x.error+x.norm*self.error+self.error*x.error
        es=[]
        if self.error:es.append(self.error_degree+x.degree)
        if x.error:es.append(x.error_degree+self.degree)
        if self.error and x.error:es.append(self.error_degree+x.error_degree)
        return RadialFourier(mul(self.coefficients,x.coefficients),degree,self.grid,self.fft,
            self.norm*x.norm,error,max(es,default=0))
    __rmul__=__mul__
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('only nonnegative finite powers')
        out=self.coerce(1);term=self
        while n:
            if n&1:out=out*term
            n//=2
            if n:term=term*term
        return out

    def Fourier(self):
        if self._fourier is None:
            z=zeros((self.grid,len(self.coefficients)))
            for k,c in enumerate(self.coefficients):z[:,k]=CBox(c)
            z=self.fft.fft(z)/self.grid
            j=np.arange(self.grid);j=np.where(j<self.grid//2,j,j-self.grid)
            outside=abs(j)>self.degree
            if (np.any(z.real.lo[outside]>0) or np.any(z.real.hi[outside]<0)
                or np.any(z.imag.lo[outside]>0) or np.any(z.imag.hi[outside]<0)):
                raise ArithmeticError('an exactly absent Fourier output lost its zero enclosure')
            z[outside]=0;self._fourier=z
        return self._fourier

    def from_Fourier(self,z,degree,error,error_degree):
        samples=real_cb(self.fft.fft(z,inverse=True)*self.grid)
        norm=sum((wiener_upper(z[:,k]) for k in range(z.real.lo.shape[1])),arb(0))
        out=RadialFourier([samples[:,k] for k in range(samples.lo.shape[1])],degree,
            self.grid,self.fft,norm,error,error_degree)
        out._fourier=z
        return out

    def derivative(self):
        if self.degree==0:return self.coerce(0)
        modes=np.arange(self.grid);modes=np.where(modes<self.grid//2,modes,modes-self.grid)
        z=self.Fourier()*CBox(0.,Box((4*modes)[:,None]))
        return self.from_Fourier(z,self.degree,4*self.error_degree*self.error,self.error_degree)

    def primitive(self):
        if self.degree==0:return self.coerce(0)
        z=self.Fourier();factor=zeros((self.grid,1))
        for j in range(-self.degree,self.degree+1):
            if j:factor[j%self.grid,0]=CBox.from_acb(acb(0,-arb(1)/(4*j)))
        out=z*factor
        error=self.error/4 if self.error_degree else arb(0)
        return self.from_Fourier(out,self.degree,error,self.error_degree)

    def mean(self):
        if self.degree==0:return self
        z=self.Fourier()[0]
        cs=real_cb(z)
        norm=sum((arb(float(c.abs_upper())).upper() for c in cs),arb(0))
        return RadialFourier(list(cs),0,self.grid,self.fft,norm,self.error,0)

    def nonmean(self):
        if self.degree==0:return self.coerce(0)
        z=self.Fourier();copy=CBox(Box(z.real.lo.copy(),z.real.hi.copy()),
                                   Box(z.imag.lo.copy(),z.imag.hi.copy()))
        copy[0]=0
        error=self.error if self.error_degree else arb(0)
        return self.from_Fourier(copy,self.degree,error,self.error_degree)

    def scalar_range(self):
        if self.degree:raise ValueError('only an actual constant angular field is scalar')
        value=scalar_arb(evaluate(self.coefficients,Box(-1.,1.)))
        return value+(-self.error).union(self.error)

    def scalar_integral(self,length):
        if self.degree:raise ValueError('only a constant angular field has a scalar integral')
        value=arb(0)
        for j,c in enumerate(self.coefficients):
            if not j%2:value+=scalar_arb(c)/(j+1)
        return exact_arb(length)*(value+(-self.error).union(self.error))


def candidate_fields(cube,knot,left,right,m,N,fft,scale_value=arb(1),background=None):
    fields,_,_=exact_candidate_series(cube,knot,left,right,m,N,fft)
    out=[RadialFourier(x.coefficients,m,N,fft,x.norm,x.error,m)*scale_value for x in fields]
    if background is not None:
        out[1]=out[1]+background
        # The derivative of a radial background in the angular direction
        # is exactly zero. Its radial derivative is supplied separately.
    return out


def circle_pair(x,y):
    """Full zero-mode convolution without evaluating an aliased product."""
    if not x or len(x)!=len(y):raise ValueError('the full real pair is required')
    N=x[0].grid;reverse=(-np.arange(N))%N
    result=x[0].coerce(0)
    for a,b in zip(x,y):
        if a.grid!=b.grid or a.fft is not b.fft:raise ValueError('different Fourier contexts')
        aa,bb=a.Fourier(),b.Fourier();na,nb=aa.real.lo.shape[1],bb.real.lo.shape[1]
        cs=[]
        for k in range(na+nb-1):
            z=CBox(0.)
            for i in range(max(0,k-nb+1),min(na-1,k)+1):
                z=z+(aa[:,i]*bb[reverse,k-i]).sum()
            cs.append(real_cb(z))
        error=a.norm*b.error+b.norm*a.error+a.error*b.error
        norm=sum((arb(float(c.abs_upper())).upper() for c in cs),arb(0))
        result=result+RadialFourier(cs,0,N,a.fft,norm,error,0)
    return result


def legendre_coefficients(z):
    """Exact monomial-to-Legendre conversion; z is (full modes,orders)."""
    n=z.real.lo.shape[1];out=zeros(z.real.lo.shape)
    for k in range(n):
        for j in range(k,n,2):
            odd=1
            for q in range(1,j+k+2,2):odd*=q
            even=2**((j-k)//2)*factorial((j-k)//2)
            coefficient=Fraction((2*k+1)*factorial(j),even*odd)
            out[:,k]=out[:,k]+z[:,j]*CBox.from_acb(acb(exact_arb(coefficient)))
    return out


def norms(pair,length,width):
    """Complete angular norms and exact polynomial radial L2 integrals."""
    N=pair[0].grid;modes=np.arange(N);modes=np.where(modes<N//2,modes,modes-N)
    def box_vector(values):
        boxes=[arb_box(v) for v in values]
        return Box(np.array([float(v.lo) for v in boxes]),np.array([float(v.hi) for v in boxes]))
    freq=4*np.abs(modes);weights={
        'L2':Box(np.ones(N)),
        'H_one_third':box_vector([(arb(1+int(k*k)).log()/3).exp() for k in freq]),
        'H1':Box(1+freq*freq)}
    per=[]
    for p in pair:
        z=p.Fourier();L=legendre_coefficients(z)
        sup=reduce_box(Box(z.magnitude_upper()).transpose()).transpose()
        # reduce_box sums its first axis; transpose sums radial orders.
        sup2=sup*sup;lm=Box(L.magnitude_upper());lsq=lm*lm
        record={}
        for name,w in weights.items():
            finite_sup=arb(float(reduce_box(sup2*w).hi)).upper().sqrt().upper()
            total=arb(0)
            for k in range(L.real.lo.shape[1]):
                total+=arb(float(reduce_box(lsq[:,k]*w).hi)).upper()/(2*k+1)
            finite_integral=(exact_arb(length)*total).sqrt().upper()
            s={'L2':arb(0),'H_one_third':arb(1)/3,'H1':arb(1)}[name]
            factor=(s*arb(1+(4*p.error_degree)**2).log()/2).exp()
            err=(factor*p.error).upper()
            record[name+'_sup']=(finite_sup+err).upper()
            record[name+'_L2_radial']=(finite_integral+exact_arb(length).sqrt()*err).upper()
        finite_A0=sum((wiener_upper(z[:,k]) for k in range(z.real.lo.shape[1])),arb(0))
        weight=box_vector([exact_arb(width*int(k)).exp() for k in freq])
        finite_As=arb(float(reduce_box(sup*weight).hi)).upper()
        record['A0_sup']=(finite_A0+p.error).upper()
        record['A_sigma_sup']=(finite_As+exact_arb(width*4*p.error_degree).exp()*p.error).upper()
        record['uniform_finite_support_remainder_A0']=p.error
        per.append(record)
    combined={}
    for key in per[0]:
        if key.startswith('A') or key=='uniform_finite_support_remainder_A0':
            combined[key]=sum((p[key] for p in per),arb(0)).upper()
        else:combined[key]=sum((p[key]**2 for p in per),arb(0)).sqrt().upper()
    return combined
