#!/usr/bin/env python3
"""Interval Fourier metric algebra for the actual finite C2 m3 tail.

This module has no numerical-background assumption.  Callers supply proven
w,w_R intervals at a point or throughout a radial interval.  Laurent
coefficients use frequencies 3k, so all angular products are exact finite
convolutions; no angular sampling or DFT is needed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
import bisect
import importlib.util
import math
import sys
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'finite_closure/m3_m8_closed_map'))
from interval_geometry_kernel import exact,add,sub,neg,mul,scale,div,square,sqrt,dn,up


def rational_interval(x):
    x=Q(x)
    v=float(x)
    lo,hi=math.nextafter(v,-math.inf),math.nextafter(v,math.inf)
    assert Q.from_float(lo)<=x<=Q.from_float(hi)
    return np.asarray(lo),np.asarray(hi)


def magnitude(x):
    return np.maximum(abs(x[0]),abs(x[1]))


def l1_upper(x):
    values=magnitude(x)
    gamma=4*values.size*2.**-53
    return float(up(np.sum(values)/(1-gamma)+values.size*np.nextafter(0.,1.)))


def convolution(a,b):
    """Outward enclosure of a real finite convolution.

    Each center is a stored binary64 number.  Radius bounds include center
    formation error.  A convolution coefficient contains at most n products
    and n-1 additions; 8*n*u exceeds the usual product/sum gamma bound and
    also covers the positive auxiliary convolutions and their summations.
    """
    am=(a[0]+a[1])/2
    bm=(b[0]+b[1])/2
    ar=up(np.maximum(up(abs(am-a[0])),up(abs(a[1]-am))))
    br=up(np.maximum(up(abs(bm-b[0])),up(abs(b[1]-bm))))
    n=max(len(am),len(bm))
    gamma=8*n*2.**-53
    assert gamma<.01
    tiny=n*np.nextafter(0.,1.)
    positive=lambda x,y:up(np.convolve(x,y)/(1-gamma)+tiny)
    absolute=positive(abs(am),abs(bm))
    uncertainty=up(positive(ar,abs(bm))+positive(abs(am),br))
    uncertainty=up(uncertainty+positive(ar,br))
    uncertainty=up(uncertainty+up(gamma*absolute+tiny))
    center=np.convolve(am,bm)
    return dn(center-uncertainty),up(center+uncertainty)


def reverse(a):
    return a[0][::-1],a[1][::-1]


def pad(a,n):
    return np.pad(a[0],(n,n)),np.pad(a[1],(n,n))


def sum_many(*args):
    result=args[0]
    for value in args[1:]:
        result=add(result,value)
    return result


def include_zero_mode(a,value):
    result=(a[0].copy(),a[1].copy())
    k=len(result[0])//2
    lo,hi=add((result[0][k],result[1][k]),value)
    result[0][k],result[1][k]=lo,hi
    return result


def metric_coefficients(V,Vr,Vrr,planar_modes,height_modes,R,w,wr):
    """Return complete Laurent enclosures for relative metric and d/dR.

    Entries rr, rtheta, thetatheta are in the reference orthonormal frame
    (E^-1/2 d_R, R^-1 d_theta).  The off-diagonal coefficient vector below
    stores its imaginary part; its absolute coefficient sum is unchanged.
    """
    assert np.all((planar_modes-1)%3==0) and np.all(height_modes%3==0)
    pk=(planar_modes-1)//3
    hk=height_modes//3
    K=int(max(max(abs(pk)),max(hk)))
    n=2*K+1
    P=len(planar_modes)
    def encode(values):
        p0=np.zeros(n);p1=np.zeros(n);z0=np.zeros(n);z1=np.zeros(n)
        p0[pk+K],p1[pk+K]=values[0][:P],values[1][:P]
        for j,k in enumerate(hk):
            value=(values[0][P+j],values[1][P+j])
            if k:
                value=scale(value,.5)
                z0[K-k],z1[K-k]=value
            z0[K+k],z1[K+k]=value
        return (p0,p1),(z0,z1)
    p,z=encode(V)
    a,zr=encode(Vr)
    aa,zrr=encode(Vrr)
    frequencies=3*np.arange(-K,K+1)
    b=scale(p,1+frequencies)
    br=scale(a,1+frequencies)
    zt=scale(z,frequencies)
    zrt=scale(zr,frequencies)
    even=lambda v:add(v,reverse(v))
    odd=lambda v:sub(v,reverse(v))
    pp=convolution(a,reverse(a))
    ppr=add(convolution(aa,reverse(a)),convolution(a,reverse(aa)))
    A=sum_many(pad(even(a),K),pp,pad(mul(zr,scale(w,2)),K),convolution(zr,zr))
    Ap=sum_many(pad(even(aa),K),ppr,pad(add(mul(zr,scale(wr,2)),mul(zrr,scale(w,2))),K),
                convolution(zrr,zr),convolution(zr,zrr))
    C=sum_many(mul(pad(even(b),K),R),convolution(b,reverse(b)),neg(convolution(zt,zt)))
    Cp=sum_many(pad(even(b),K),mul(pad(even(br),K),R),
                convolution(br,reverse(b)),convolution(b,reverse(br)),
                neg(convolution(zrt,zt)),neg(convolution(zt,zrt)))
    ab=convolution(a,reverse(b))
    abr=add(convolution(aa,reverse(b)),convolution(a,reverse(br)))
    wzr=include_zero_mode(zr,w)
    wrzrr=include_zero_mode(zrr,wr)
    B=sum_many(scale(pad(odd(b),K),.5),neg(mul(scale(pad(odd(a),K),.5),R)),
                scale(odd(ab),-.5),convolution(wzr,zt))
    Bp=sum_many(scale(pad(odd(br),K),.5),scale(pad(odd(a),K),-.5),
                 neg(mul(scale(pad(odd(aa),K),.5),R)),scale(odd(abr),-.5),
                 convolution(wrzrr,zt),convolution(wzr,zrt))
    E=add(exact(1),square(w))
    root=sqrt(E)
    R2=square(R)
    denominator=mul(R,root)
    Er=div(A,E)
    Ef=div(B,denominator)
    Eg=div(C,R2)
    Erp=sub(div(Ap,E),div(mul(A,scale(mul(w,wr),2)),square(E)))
    Efp=div(sub(Bp,mul(B,add(div(exact(1),R),div(mul(w,wr),E)))),denominator)
    Egp=div(sub(Cp,mul(C,div(exact(2),R))),R2)
    norms=[l1_upper(v)for v in [Er,Ef,Eg]]
    dnorms=[l1_upper(v)for v in [Erp,Efp,Egp]]
    return dict(coefficients=[Er,Ef,Eg],derivative_coefficients=[Erp,Efp,Egp],
                component_l1_upper=norms,derivative_component_l1_upper=dnorms,
                operator_upper=float(up(max(norms[0]+norms[1],norms[2]+norms[1]))),
                derivative_operator_upper=float(up(max(dnorms[0]+dnorms[1],dnorms[2]+dnorms[1]))),
                maximum_angular_frequency=6*K,angular_sampling_used=False)


def bernstein_at(coefficients,t):
    rows=coefficients
    omt=sub(exact(1),t)
    while len(rows)>1:
        rows=[add(mul(omt,a),mul(t,b))for a,b in zip(rows[:-1],rows[1:])]
    return rows[0]


def split_bernstein(coefficients,t):
    rows=coefficients
    left,right=[rows[0]],[rows[-1]]
    omt=sub(exact(1),t)
    while len(rows)>1:
        rows=[add(mul(omt,a),mul(t,b))for a,b in zip(rows[:-1],rows[1:])]
        left.append(rows[0]);right.append(rows[-1])
    return left,right[::-1]


def bernstein_range(coefficients,lo,hi):
    assert Q(0)<=lo<=hi<=Q(1)
    if lo==hi:
        return bernstein_at(coefficients,rational_interval(lo))
    if lo:
        _,coefficients=split_bernstein(coefficients,rational_interval(lo))
    if hi<1:
        coefficients,_=split_bernstein(coefficients,rational_interval((hi-lo)/(1-lo)))
    return np.minimum.reduce([v[0]for v in coefficients]),np.maximum.reduce([v[1]for v in coefficients])


class IntervalFiniteTail:
    def __init__(self,manifest,reader):
        spec=importlib.util.spec_from_file_location('metric_finite_reader',reader)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        self.f=module.IntegratedTail(manifest)
        f=self.f
        self.cut=Q.from_float(f.meta['parameters']['rCut'])
        self.outer=Q.from_float(f.meta['radialGeometry']['outerAnchor'])
        self.inner=Q.from_float(f.meta['radialGeometry']['innerAnchor'])
        self.width=Q.from_float(.02)
        self.delta=self.outer-self.cut
        self.lengths=[f.radial_scale*Q.from_float(float(v))for v in f.unscaled_lengths]
        self.rnodes=[self.inner]
        for v in self.lengths:
            self.rnodes.append(self.rnodes[-1]+v)
        assert self.rnodes[-1]==self.outer
        L=mul(exact(f.unscaled_lengths[:,None]),rational_interval(f.radial_scale))
        increment=mul(L,sum_many(mul(rational_interval(Q(7,30)),add(exact(f.first[:-1]),exact(f.first[1:]))),
                     mul(rational_interval(Q(8,15)),exact(f.midpoint)),
                     div(mul(L,sub(exact(f.second[:-1]),exact(f.second[1:]))),exact(60))))
        self.left=(np.empty_like(f.first),np.empty_like(f.first))
        current=exact(f.source_values[0])
        self.left[0][0],self.left[1][0]=current
        for i in range(len(self.lengths)):
            current=add(current,(increment[0][i],increment[1][i]))
            self.left[0][i+1],self.left[1][i+1]=current

    def radial_lift(self,R):
        t=min(Q(1),max(Q(0),(R-(self.cut-self.width))/self.width))
        return R+self.delta*t**3*(10+t*(-15+6*t))

    def lift_derivatives(self,lo,hi):
        tlo=min(Q(1),max(Q(0),(lo-(self.cut-self.width))/self.width))
        thi=min(Q(1),max(Q(0),(hi-(self.cut-self.width))/self.width))
        t=(rational_interval(tlo)[0],rational_interval(thi)[1])
        omt=sub(exact(1),t)
        first=add(exact(1),mul(rational_interval(30*self.delta/self.width),mul(square(t),square(omt))))
        second=mul(rational_interval(60*self.delta/self.width**2),mul(mul(t,omt),sub(exact(1),scale(t,2))))
        assert first[0]>0
        return first,second

    def span_polynomials(self,i):
        f=self.f
        L=rational_interval(self.lengths[i])
        b0=exact(f.first[i]);b4=exact(f.first[i+1])
        b1=add(b0,scale(mul(L,exact(f.second[i])),.25))
        b3=sub(b4,scale(mul(L,exact(f.second[i+1])),.25))
        b2=div(sub(sub(sub(sub(scale(exact(f.midpoint[i]),16),b0),scale(b1,4)),scale(b3,4)),b4),exact(6))
        first=[b0,b1,b2,b3,b4]
        second=[div(scale(sub(first[j+1],first[j]),4),L)for j in range(4)]
        values=[(self.left[0][i],self.left[1][i])]
        for b in first:
            values.append(add(values[-1],div(mul(L,b),exact(5))))
        return values,first,second

    def coefficients(self,lo,hi=None):
        lo=Q(lo);hi=lo if hi is None else Q(hi)
        assert self.inner<=lo<=hi<=self.cut
        vlo,vhi=self.radial_lift(lo),self.radial_lift(hi)
        assert self.inner<=vlo<=vhi<=self.outer
        i0=min(len(self.lengths)-1,bisect.bisect_right(self.rnodes,vlo)-1)
        i1=min(len(self.lengths)-1,bisect.bisect_right(self.rnodes,vhi)-1)
        all_ranges=[]
        for i in range(i0,i1+1):
            tlo=max(Q(0),(vlo-self.rnodes[i])/self.lengths[i])
            thi=min(Q(1),(vhi-self.rnodes[i])/self.lengths[i])
            if tlo>thi:
                continue
            polynomials=self.span_polynomials(i)
            all_ranges.append([bernstein_range(p,tlo,thi)for p in polynomials])
        assert all_ranges
        values=[]
        for j in range(3):
            values.append((np.minimum.reduce([v[j][0]for v in all_ranges]),np.maximum.reduce([v[j][1]for v in all_ranges])))
        r1,r2=self.lift_derivatives(lo,hi)
        return values[0],mul(values[1],r1),add(mul(values[2],square(r1)),mul(values[1],r2))
