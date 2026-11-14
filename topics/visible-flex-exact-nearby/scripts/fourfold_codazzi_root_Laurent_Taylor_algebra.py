#!/usr/bin/env python3
"""Complete Laurent/Taylor ball algebra for exact old-radial root jets.

Fourier indices are j in exp(4 i j phi). All products are non-circular.
A finite Taylor prefix never silently supplies uncomputed higher coefficients.
No numerical work is performed at import.
"""
from __future__ import annotations
import math
from fractions import Fraction as Q
from functools import lru_cache
from flint import acb,arb,acb_poly

def ex(q):
    q=Q(q);return arb(q.numerator)/q.denominator
def rec(v,digits=110):
    v=arb(v)
    if not v.is_finite():raise ValueError("nonfinite Laurent/Taylor bound")
    return v.str(digits)
def cpack(v):return [rec(v.real),rec(v.imag)]
def cunpack(v):
    if not isinstance(v,list) or len(v)!=2:raise ValueError("bad complex coefficient record")
    z=acb(arb(v[0]),arb(v[1]))
    if not z.is_finite():raise ValueError("nonfinite saved complex coefficient")
    return z
def up(z):return abs(z).upper()

class LP:
    __slots__=("lo","c")
    def __init__(self,lo=0,coefficients=None):
        a=[acb(0)] if coefficients is None else [acb(z) for z in coefficients]
        if not a:a=[acb(0)];lo=0
        first=0
        while first<len(a)-1 and a[first]==0:first+=1
        last=len(a)
        while last>first+1 and a[last-1]==0:last-=1
        self.lo=int(lo)+first;self.c=a[first:last]
        if len(self.c)==1 and self.c[0]==0:self.lo=0
        if not all(v.is_finite() for v in self.c):raise ValueError("nonfinite Fourier ball")
    @staticmethod
    def scalar(value):return LP(0,[acb(value)])
    @staticmethod
    def zero():return LP()
    @staticmethod
    def one():return LP.scalar(1)
    @property
    def hi(self):return self.lo+len(self.c)-1
    @property
    def degree(self):return max(abs(self.lo),abs(self.hi))
    def is_zero(self):return len(self.c)==1 and self.c[0]==0
    def coefficient(self,j):
        return self.c[j-self.lo] if self.lo<=j<=self.hi else acb(0)
    def scalar_value(self):
        if self.lo!=0 or len(self.c)!=1:
            raise ValueError("a required radial scalar has nonconstant Fourier output")
        return self.c[0]
    def mean(self):return self.coefficient(0)
    def __add__(self,other):
        if not isinstance(other,LP):other=LP.scalar(other)
        if self.is_zero():return LP(other.lo,other.c)
        if other.is_zero():return LP(self.lo,self.c)
        lo=min(self.lo,other.lo);hi=max(self.hi,other.hi)
        return LP(lo,[self.coefficient(j)+other.coefficient(j) for j in range(lo,hi+1)])
    __radd__=__add__
    def __neg__(self):return LP(self.lo,[-v for v in self.c])
    def __sub__(self,other):return self+(-other if isinstance(other,LP) else -acb(other))
    def __rsub__(self,other):return (-self)+other
    def scale(self,value):
        z=acb(value)
        if z==0 or self.is_zero():return LP.zero()
        return LP(self.lo,[z*v for v in self.c])
    def __mul__(self,other):
        if not isinstance(other,LP):return self.scale(other)
        if self.is_zero() or other.is_zero():return LP.zero()
        if self.lo==0 and len(self.c)==1:return other.scale(self.c[0])
        if other.lo==0 and len(other.c)==1:return self.scale(other.c[0])
        product=acb_poly(self.c)*acb_poly(other.c)
        cc=product.coeffs()
        if len(cc)>len(self.c)+len(other.c)-1:
            raise ValueError("a full polynomial product exceeded its exact support")
        return LP(self.lo+other.lo,cc)
    __rmul__=__mul__
    def divide_scalar(self,z):
        z=acb(z)
        if z.contains(0):raise ValueError("a scalar denominator contains zero")
        return self.scale(1/z)
    def theta(self,q=1):
        if q<0 or int(q)!=q:raise ValueError("angular derivative order must be nonnegative")
        result=[]
        for j,z in enumerate(self.c,self.lo):
            factor=acb(1)
            for _ in range(q):factor*=acb(0,4*j)
            result.append(z*factor)
        return LP(self.lo,result)
    def primitive(self):
        return LP(self.lo,[acb(0) if j==0 else z/acb(0,4*j)
            for j,z in enumerate(self.c,self.lo)])
    def constant_part(self):return LP.scalar(self.mean())
    def norm(self,width,q=0):
        width=Q(width)
        if width<0:raise ValueError("negative Fourier width")
        total=arb(0)
        for j,z in enumerate(self.c,self.lo):
            if q and j==0:continue
            factor=(4*abs(j))**q if q else 1
            total+=up(z)*factor*fourier_weight(abs(j),str(width))
        return total.upper()
    def record(self):
        return dict(first_Fourier_index=self.lo,coefficients=[cpack(z) for z in self.c],
            physical_angle_frequency_multiplier=4,noncircular_full_support=True)
    @classmethod
    def restore(cls,v):
        if v.get("physical_angle_frequency_multiplier")!=4 or v.get("noncircular_full_support") is not True:
            raise ValueError("a saved Fourier polynomial changed convention")
        return cls(v["first_Fourier_index"],[cunpack(x) for x in v["coefficients"]])

@lru_cache(maxsize=None)
def fourier_weight(j,width):
    return (4*j*ex(Q(width))).exp().upper()

def known_zero_view(value,identity):
    """Caller must supply a proved exact identity; the ball is only a consistency gate."""
    if not identity:raise ValueError("an exact-zero projection requires its mathematical identity")
    if not all(v.contains(0) for v in value.c):
        raise ValueError("an exact structural zero is absent from its complete Fourier balls: "+identity)
    return LP.zero()

def known_scalar_view(value,scalar,identity):
    if not identity:raise ValueError("a scalar identity must be explicitly named")
    scalar=acb(scalar)
    for j,z in enumerate(value.c,value.lo):
        if j and not z.contains(0):
            raise ValueError("an exact scalar identity lost a nonconstant zero: "+identity)
    z=value.mean()
    if not (z.real.overlaps(scalar.real) and z.imag.overlaps(scalar.imag)):
        raise ValueError("two balls of the same exact scalar are disjoint: "+identity)
    return LP.scalar(scalar)

def require(a,count):
    if count<0 or len(a)<count:
        raise ValueError("a Taylor operation requested an unpaid higher coefficient")
def zeros(count):return [LP.zero() for _ in range(count)]
def constant(value,count):
    if count<1:raise ValueError("a constant series needs its zero coefficient")
    return [LP.scalar(value)]+zeros(count-1)
def take(a,count):
    require(a,count);return a[:count]
def sc(a,n):
    if n<0:return LP.zero()
    require(a,n+1);return a[n]
def add(a,b,count):
    require(a,count);require(b,count);return [a[j]+b[j] for j in range(count)]
def sub(a,b,count):
    require(a,count);require(b,count);return [a[j]-b[j] for j in range(count)]
def scale(a,value,count=None):
    count=len(a) if count is None else count;require(a,count)
    return [a[j].scale(value) for j in range(count)]
def conv_coefficient(a,b,n):
    if n<0:return LP.zero()
    require(a,n+1);require(b,n+1)
    return sum((a[j]*b[n-j] for j in range(n+1)),LP.zero())
def mul(a,b,count):
    require(a,count);require(b,count)
    return [conv_coefficient(a,b,n) for n in range(count)]
def dr(a):
    return [a[j+1].scale(j+1) for j in range(len(a)-1)]
def theta(a,q=1):return [v.theta(q) for v in a]
def mean(a):return [LP.scalar(v.mean()) for v in a]
def primitive(a):return [v.primitive() for v in a]
def shift(a,k,count):
    if k<0:raise ValueError("negative Taylor shift must use an explicitly paid derivative")
    if count>k:require(a,count-k)
    return [LP.zero() if j<k else a[j-k] for j in range(count)]
def inverse(a,count):
    require(a,count);z=a[0].scalar_value()
    if z.contains(0):raise ValueError("the exact radial series constant is not invertible")
    out=[LP.scalar(1/z)]
    for n in range(1,count):
        out.append(sum((a[j]*out[n-j] for j in range(1,n+1)),LP.zero()).divide_scalar(-z))
    return out
def power(a,p,count,normalized=False):
    """Full finite prefix of a^p; normalized=True returns (a/a0)^p exactly."""
    require(a,count);p=Q(p);z=a[0].scalar_value()
    if not z.real>0:raise ValueError("the paid positive-real-part series branch is unresolved")
    y0=acb(1) if normalized else (z.log()*acb(ex(p))).exp()
    out=[LP.scalar(y0)]
    for n in range(1,count):
        total=a[n].scale(acb(ex(p*n))*y0)
        for j in range(1,n):
            total+=a[j]*out[n-j].scale(acb(ex((p+1)*j-n)))
        out.append(total.divide_scalar(n*z))
    return out
def exp_integral(g,count):
    """Y'=gY, Y0=1; only the first count-1 known g coefficients are used."""
    if count>1:require(g,count-1)
    out=[LP.one()]
    for n in range(1,count):
        out.append(sum((g[j]*out[n-1-j] for j in range(n)),LP.zero()).divide_scalar(n))
    return out
def pack_series(a):return [v.record() for v in a]
def unpack_series(a):return [LP.restore(v) for v in a]
