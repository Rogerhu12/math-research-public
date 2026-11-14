#!/usr/bin/env python3
"""Radial/Fourier interval models, reconstructed after executor reset.

Auxiliary coefficient removals are fully charged to the uniform remainder.
The native field is unchanged. Direct finite convolutions, outward gamma
budgets, full angular arcs; no FFT or flush-to-zero arithmetic.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import math
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj;spec.loader.exec_module(obj)
    return obj

poly=module('fd2d_gc_interval_polynomials',HERE/'db6f-audit-metric-polynomial.py')
normal=module('fd2d_gc_interval_normal',HERE/'fd2d-metric-normal-interval-arithmetic.py')
normal.install(poly)
I,P,up,down,qb=poly.I,poly.P,poly.up,poly.down,poly.qbounds
DEGREE=16
FLOOR=math.ldexp(1.,-400)
COMPACT_BUDGET=1e-22

def sum_upper(values):
    values=np.asarray(values,dtype=float)
    return poly.positive_sum_upper(values) if np.any(values) else 0.

def pnorm(p):return sum_upper(np.maximum(abs(p.c.lo),abs(p.c.hi)))
def error_sum(*values):return sum_upper(np.asarray(values))

def exact_binary(parts):
    sign,mantissa,exponent,_=map(int,parts)
    return (-1 if sign else 1)*Q(mantissa)*Q(2)**exponent

def record_interval(row):
    lo,hi=exact_binary(row['binary_lower']),exact_binary(row['binary_upper'])
    return I(float(qb(lo).lo),float(qb(hi).hi))

def exact_midpoint(row):return (exact_binary(row['binary_lower'])+exact_binary(row['binary_upper']))/2
def bound_upper(row):return float(qb(exact_binary(row['binary_upper'])).hi)

def centered(a):
    lo,hi=a.lo,a.hi
    mask=(np.maximum(abs(lo),abs(hi))<FLOOR)&((lo!=0)|(hi!=0))
    if np.any(mask):
        lo=lo.copy();hi=hi.copy();lo[mask]=-FLOOR;hi[mask]=FLOOR
    center=lo/2+hi/2;raw=np.maximum(center-lo,hi-center)
    radius=np.zeros_like(raw);mask=raw>0;radius[mask]=up(raw[mask])
    return center,radius

def direct_radial_convolution(a,b):
    if a.lo.shape[1]<b.lo.shape[1]:a,b=b,a
    da,ma=a.lo.shape;db,mb=b.lo.shape;degree,width=da+db-1,ma+mb-1
    if mb<=3:
        out=I(np.zeros((degree,width)))
        for angular in range(mb):
            lo=np.zeros((degree,da));hi=lo.copy()
            for j in range(da):lo[j:j+db,j]=b.lo[:,angular];hi[j:j+db,j]=b.hi[:,angular]
            product=poly.interval_matmul(I(lo,hi),a)
            value=out[:,angular:angular+ma]+product
            out.lo[:,angular:angular+ma]=value.lo;out.hi[:,angular:angular+ma]=value.hi
        return out
    ac,ar=centered(a);bc,br=centered(b)
    n=2*min(ma,mb)+2;unit=Q(1,2**52)
    gamma=float(qb(n*unit/(1-n*unit)).hi)
    lo=np.zeros((degree,width));hi=lo.copy()
    def pos(x,y):return up(up(np.convolve(x,y)+FLOOR)/down(1-gamma))
    for j in range(da):
        if not (np.any(ac[j]) or np.any(ar[j])):continue
        for k in range(db):
            if not (np.any(bc[k]) or np.any(br[k])):continue
            nominal=np.convolve(ac[j],bc[k]);mag=pos(abs(ac[j]),abs(bc[k]))
            radius=up(pos(abs(ac[j]),br[k])+pos(ar[j],abs(bc[k])))
            radius=up(radius+pos(ar[j],br[k]));radius=up(radius+up(up(gamma*mag)+FLOOR))
            lo[j+k]=down(lo[j+k]+down(nominal-radius));hi[j+k]=up(hi[j+k]+up(nominal+radius))
    if not (np.isfinite(lo).all() and np.isfinite(hi).all()):raise ArithmeticError('Nonfinite interval convolution')
    return I(lo,hi)

poly.interval_convolution=direct_radial_convolution

def compact(p,error=0.):
    lo,hi=p.c.lo,p.c.hi
    if lo.shape[0]>DEGREE+1:
        error=error_sum(error,sum_upper(np.maximum(abs(lo[DEGREE+1:]),abs(hi[DEGREE+1:]))))
        lo,hi=lo[:DEGREE+1],hi[:DEGREE+1]
    radial=lo.shape[0]
    while radial>1 and sum_upper(np.maximum(abs(lo[radial-1]),abs(hi[radial-1])))<=FLOOR*1000:
        error=error_sum(error,sum_upper(np.maximum(abs(lo[radial-1]),abs(hi[radial-1]))));radial-=1
    lo,hi=lo[:radial],hi[:radial]
    first,left,right,spent=p.first,0,lo.shape[1],0.
    while first+left<0<first+right-1:
        candidate=error_sum(sum_upper(np.maximum(abs(lo[:,left]),abs(hi[:,left]))),sum_upper(np.maximum(abs(lo[:,right-1]),abs(hi[:,right-1]))))
        if error_sum(spent,candidate)>COMPACT_BUDGET:break
        spent=error_sum(spent,candidate);left+=1;right-=1
    error=error_sum(error,spent)
    return P(I(lo[:,left:right].copy(),hi[:,left:right].copy()),first+left,p.phase),error

@dataclass
class TM:
    p:P
    error:float=0.

    @classmethod
    def scalar(cls,value):return cls(P.scalar(value))
    @classmethod
    def zero(cls,phase=0):return cls(P(I(np.zeros((1,1))),0,phase))
    @classmethod
    def get(cls,value):return value if isinstance(value,cls) else cls.scalar(value)
    def norm(self):return error_sum(pnorm(self.p),self.error)
    def __neg__(self):return TM(-self.p,self.error)
    def __add__(self,other):
        other=TM.get(other)
        if self.p.phase!=other.p.phase:
            if not pnorm(self.p) and not self.error:return other
            if not pnorm(other.p) and not other.error:return self
            raise ValueError('Adding different real Fourier parities')
        p,e=compact(self.p+other.p,error_sum(self.error,other.error));return TM(p,e)
    __radd__=__add__
    def __sub__(self,other):return self+(-TM.get(other))
    def __rsub__(self,other):return TM.get(other)+(-self)
    def __mul__(self,other):
        other=TM.get(other)
        if (not pnorm(self.p) and not self.error) or (not pnorm(other.p) and not other.error):return TM.zero((self.p.phase+other.p.phase)%2)
        e=(I(pnorm(self.p))*I(other.error)+I(pnorm(other.p))*I(self.error)+I(self.error)*I(other.error)).hi
        p,e=compact(self.p*other.p,max(0.,float(e)));return TM(p,e)
    __rmul__=__mul__
    def __truediv__(self,scalar):return self*TM.scalar(I(1)/I.get(scalar))
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('Nonnegative integer model powers only')
        out,factor=TM.scalar(1.),self
        while n:
            if n%2:out=out*factor
            n//=2
            if n:factor=factor*factor
        return out

def polynomial_model(coefficients,argument):
    out=TM.scalar(0.)
    for value in reversed(coefficients):out=out*argument+TM.scalar(value)
    return out

def variable(center,scale):return TM(P(poly.base.stack([qb(center),qb(scale)],0)[:,None]))

def exp_model(value,*,order=8,minus_one=False):
    radius=value.norm()
    if radius>=1:raise ArithmeticError('Split for the explicit exponential remainder')
    out,power=TM.scalar(0. if minus_one else 1.),TM.scalar(1.)
    for k in range(1,order+1):
        power=power*value;out=out+power*qb(Q(1,math.factorial(k)))
    r=Q(radius);tail=r**(order+1)/(math.factorial(order+1)*(1-r))
    out.error=error_sum(out.error,float(qb(tail).hi));return out

def inverse_power_model(value,*,square_root=False,order=24):
    if value.p.first!=0 or value.p.c.lo.shape[1]!=1 or value.p.phase:raise ValueError('Scalar physical model only')
    center=float(value.p.c.lo[0,0]/2+value.p.c.hi[0,0]/2)
    if center<=0:raise ArithmeticError('Nonpositive reciprocal center')
    deviation=value/I(center)-1.;radius=deviation.norm()
    if radius>=.8:raise ArithmeticError('Split before reciprocal expansion')
    power,out=TM.scalar(1.),TM.scalar(1.)
    for k in range(1,order+1):
        power=power*deviation
        coefficient=Q((-1)**k*math.comb(2*k,k),4**k) if square_root else Q((-1)**k)
        out=out+power*qb(coefficient)
    r=Q(radius);out.error=error_sum(out.error,float(qb(r**(order+1)/(1-r)).hi))
    normalization=I(1)/I(center).sqrt() if square_root else I(1)/I(center)
    return out*normalization

def angular_derivative(p):
    c=p.c*(2*np.arange(p.first,p.first+p.c.lo.shape[1]))[None,:]
    return P(-c if p.phase else c,p.first,1-p.phase)

def real_coefficients(p):
    degree,width=p.c.lo.shape;last=p.first+width-1;K=max(abs(p.first),abs(last))
    lo=np.zeros((degree,2*K+1));hi=lo.copy();offset=p.first+K
    lo[:,offset:offset+width]=p.c.lo;hi[:,offset:offset+width]=p.c.hi;c=I(lo,hi)
    zero=c[:,K:K+1] if p.phase==0 else I(np.zeros((degree,1)))
    negative,positive=c[:,:K][:,::-1],c[:,K+1:]
    rest=negative+positive if p.phase==0 else negative-positive
    return I(np.concatenate((zero.lo,rest.lo),axis=1),np.concatenate((zero.hi,rest.hi),axis=1))

@lru_cache(None)
def centered_bernstein_matrix(degree):
    lo=np.zeros((degree+1,degree+1));hi=lo.copy()
    for row in range(degree+1):
        for col in range(degree+1):
            value=sum((Q(math.comb(col,k)*(-1)**(col-k)*2**k*math.comb(row,k),math.comb(degree,k)) for k in range(min(row,col)+1)),Q())
            z=qb(value);lo[row,col],hi[row,col]=z.lo,z.hi
    return I(lo,hi)

@lru_cache(None)
def trigonometry(modes,count):
    cp=[poly.base.trig_point(Q(2*k,count),True) for k in range(count)]
    sn=[poly.base.trig_point(Q(2*k,count),False) for k in range(count)]
    cl=np.ones((modes+1,count));ch=cl.copy();sl=np.zeros_like(cl);sh=sl.copy()
    def ceil_div(a,b):return -((-a)//b)
    for j in range(1,modes+1):
        if j>=count:cl[j]=-1;ch[j]=1;sl[j]=-1;sh[j]=1;continue
        for k in range(count):
            a,b=(j*k)%count,(j*(k+1))%count
            cl[j,k],ch[j,k]=min(cp[a][0],cp[b][0]),max(cp[a][1],cp[b][1])
            sl[j,k],sh[j,k]=min(sn[a][0],sn[b][0]),max(sn[a][1],sn[b][1])
            left,right=j*k,j*(k+1)
            if ceil_div(left,count)<=right//count:ch[j,k]=1
            if ceil_div(2*left-count,2*count)<=(2*right-count)//(2*count):cl[j,k]=-1
            if ceil_div(4*left-count,4*count)<=(4*right-count)//(4*count):sh[j,k]=1
            if ceil_div(4*left-3*count,4*count)<=(4*right-3*count)//(4*count):sl[j,k]=-1
    return I(cl,ch),I(sl,sh)

def range_polynomial(p,trig=None):
    c=real_coefficients(p);bern=poly.interval_matmul(centered_bernstein_matrix(c.lo.shape[0]-1),c)
    if trig is None:
        if c.lo.shape[1]!=1:raise ValueError('Angular table missing')
        return I(bern.lo[:,0].min(),bern.hi[:,0].max())
    if c.lo.shape[1]>trig[p.phase].lo.shape[0]:raise ValueError('Angular proof table too short')
    radial=I(bern.lo.min(axis=0)[None,:],bern.hi.max(axis=0)[None,:])
    return poly.interval_matmul(radial,trig[p.phase][:c.lo.shape[1]])[0]

def range_model(model,trig=None):return range_polynomial(model.p,trig)+I(-model.error,model.error)

def integrate_polynomial(p,length):
    out=I(np.zeros(p.c.lo.shape[1]))
    for k in range(0,p.c.lo.shape[0],2):out=out+p.c[k]*qb(length/Q(k+1))
    return P(out[None,:],p.first,p.phase)

def primitive_polynomial(p,length,before,mean,offset):
    degree,width=p.c.lo.shape;lo=np.zeros((degree+1,width));hi=lo.copy();constant=I(np.zeros(width))
    for k in range(degree):
        value=p.c[k]*qb(length/Q(2*(k+1)));lo[k+1],hi[k+1]=value.lo,value.hi
        constant=constant-value*((-1)**(k+1))
    lo[0],hi[0]=constant.lo,constant.hi
    a,b=qb(offset+length/2),qb(length/2)
    linear=P(I(np.array([[float(a.lo)],[float(b.lo)]]),np.array([[float(a.hi)],[float(b.hi)]])))
    return P(I(lo,hi),p.first,p.phase)+before-mean*linear
