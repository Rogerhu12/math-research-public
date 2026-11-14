#!/usr/bin/env python3
"""Coefficient-first metric residual bounds for a shared-jet Fourier map.

Input target packets enclose the SAME analytic a(s), e(s), e'(s), on each
listed interval, in the local variable u=(s-left)/(right-left). Interval
power coefficients and uniform remainder bounds are allowed. This backend
does not establish the supplier's analytic enclosures. It never imports
the nonlinear solver, and subtracts coefficients before taking norms.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import time
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent_continuous_geometry',HERE/'db6f-audit-continuous-hermite.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
I,up,down,qbounds=base.I,base.up,base.down,base.qbounds


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def positive_sum_upper(v):
    v=np.asarray(v,dtype=np.float64)
    if np.any(v<0):raise ValueError('Expected nonnegative terms')
    n=max(1,v.size);u=Q(1,2**52);g=float(qbounds(n*u/(1-n*u)).hi)
    observed=np.sum(v,dtype=np.float64)
    return float(up(up(observed+n*np.nextafter(0.,1.))/down(1-g)))


def interval_convolution(a,b):
    """Direct convolution with a standard gamma_(2n+2) rounding budget.

    np.convolve uses finite multiply/add dot products. The bound permits
    arbitrary addition order and correctly-rounded fused multiply/add.
    Underflow is also charged by (2n+2)*minimum-positive-subnormal.
    """
    na,ma=a.lo.shape;nb,mb=b.lo.shape
    stride=ma+mb-1
    def flat(x,width):
        z=np.zeros((x.shape[0],width));z[:,:x.shape[1]]=x
        return z.ravel()
    ac=(a.lo/2+a.hi/2);bc=(b.lo/2+b.hi/2)
    ar=up(np.maximum(ac-a.lo,a.hi-ac));br=up(np.maximum(bc-b.lo,b.hi-bc))
    ar=np.maximum(ar,0);br=np.maximum(br,0)
    ac,bc,ar,br=(flat(x,stride) for x in (ac,bc,ar,br))
    n=2*min(len(ac),len(bc))+2;unit=Q(1,2**52)
    gamma=float(qbounds(n*unit/(1-n*unit)).hi)
    tiny=float(up(n*np.nextafter(0.,1.)))
    def nonnegative_upper(x,y):
        z=np.convolve(x,y)
        return up(up(z+tiny)/down(1-gamma))
    nominal=np.convolve(ac,bc)
    mag=nonnegative_upper(abs(ac),abs(bc))
    rad=up(nonnegative_upper(abs(ac),br)+nonnegative_upper(ar,abs(bc)))
    rad=up(rad+nonnegative_upper(ar,br))
    rad=up(rad+up(up(gamma*mag)+tiny))
    outshape=(na+nb-1,stride)
    # Final padding contributes an unused suffix; every physical coefficient
    # has a unique mixed-radix index because stride>=ma+mb-1.
    size=outshape[0]*outshape[1]
    lo=down(nominal[:size]-rad[:size]).reshape(outshape)
    hi=up(nominal[:size]+rad[:size]).reshape(outshape)
    if not (np.isfinite(lo).all() and np.isfinite(hi).all()):raise ArithmeticError('Nonfinite convolution')
    return I(lo,hi)


@lru_cache(None)
def bernstein_matrix(degree):
    lo=np.zeros((degree+1,degree+1));hi=lo.copy()
    for k in range(degree+1):
        for j in range(k+1):
            z=qbounds(Q(math.comb(k,j),math.comb(degree,j)))
            lo[k,j]=z.lo;hi[k,j]=z.hi
    return I(lo,hi)


def interval_matmul(a,b):
    ac=a.lo/2+a.hi/2;bc=b.lo/2+b.hi/2
    ar=up(np.maximum(ac-a.lo,a.hi-ac));br=up(np.maximum(bc-b.lo,b.hi-bc))
    n=2*a.lo.shape[1]+2;unit=Q(1,2**52)
    gamma=float(qbounds(n*unit/(1-n*unit)).hi);tiny=float(up(n*np.nextafter(0.,1.)))
    def pos(x,y):return up(up(x@y+tiny)/down(1-gamma))
    nominal=ac@bc;mag=pos(abs(ac),abs(bc))
    rad=up(pos(abs(ac),br)+pos(ar,abs(bc)))
    rad=up(rad+pos(ar,br));rad=up(rad+up(up(gamma*mag)+tiny))
    return I(down(nominal-rad),up(nominal+rad))


@dataclass
class P:
    c:I
    first:int=0
    phase:int=0  # coefficients multiplied by i**phase; phase=0 or 1

    @classmethod
    def scalar(cls,x):return cls(I.get(x)[None,None])

    def __neg__(self):return P(-self.c,self.first,self.phase)

    def __add__(self,b):
        if not isinstance(b,P):b=P.scalar(b)
        if self.phase!=b.phase:raise ValueError('Different coefficient phases')
        low=min(self.first,b.first);high=max(self.first+self.c.lo.shape[1],b.first+b.c.lo.shape[1])
        degree=max(self.c.lo.shape[0],b.c.lo.shape[0])
        def pad(v):
            l=np.zeros((degree,high-low));h=l.copy()
            sl=(slice(0,v.c.lo.shape[0]),slice(v.first-low,v.first-low+v.c.lo.shape[1]))
            l[sl]=v.c.lo;h[sl]=v.c.hi
            return I(l,h)
        return P(pad(self)+pad(b),low,self.phase)

    __radd__=__add__
    def __sub__(self,b):return self+(-b)
    def __mul__(self,b):
        if not isinstance(b,P):return P(self.c*I.get(b),self.first,self.phase)
        c=interval_convolution(self.c,b.c);phase=self.phase+b.phase
        if phase>=2:c=-c;phase-=2
        return P(c,self.first+b.first,phase)
    __rmul__=__mul__

    def theta(self):
        c=self.c*(3*np.arange(self.first,self.first+self.c.lo.shape[1]))[None,:]
        return P(-c if self.phase else c,self.first,1-self.phase)

    def norm(self):
        bern=interval_matmul(bernstein_matrix(self.c.lo.shape[0]-1),self.c)
        by_frequency=np.maximum(abs(bern.lo),abs(bern.hi)).max(axis=0)
        return positive_sum_upper(by_frequency)


def compose(c,a,b):
    """Power coefficients of c(a+b*u); coefficient array degree x state."""
    out=[];d=c.lo.shape[0]-1
    for k in range(d+1):
        v=I(np.zeros(c.lo.shape[1]))
        for j in range(k,d+1):
            power=I(1.)
            for _ in range(j-k):power=power*a
            for _ in range(k):power=power*b
            v=v+math.comb(j,k)*power*c[j]
        out.append(v)
    return base.stack(out,0)


def geometry_coefficients(geom,left,right):
    index=min(int(np.searchsorted(geom.x,left,side='right')-1),len(geom.x)-2)
    if index<0 or right>geom.x[index+1]:raise ValueError('Target packet crosses a geometry knot')
    h=geom.h[index]
    a=(I(left)-I(geom.x[index]))/h;b=(I(right)-I(left))/h
    raw=geom.power[index]
    val=compose(raw,a,b)
    der=compose(raw[1:]*np.arange(1,6)[:,None]/h,a,b)
    def expand(v):
        M=geom.M;d=v.lo.shape[0]
        fields=[]
        for axis in range(3):
            l=np.zeros((d,2*M+1));hh=l.copy()
            if axis==0:
                l[:,M]=v.lo[:,0];hh[:,M]=v.hi[:,0]
            if axis==2:
                l[:,M]=v.lo[:,-1];hh[:,M]=v.hi[:,-1]
            for j in range(1,M+1):
                z=v[:,axis*M+j]/2
                if axis==1:
                    l[:,M-j]=z.lo;hh[:,M-j]=z.hi
                    l[:,M+j]=-z.hi;hh[:,M+j]=-z.lo
                else:
                    l[:,M-j]=l[:,M+j]=z.lo;hh[:,M-j]=hh[:,M+j]=z.hi
            fields.append(P(I(l,hh),-M,1 if axis==1 else 0))
        return fields
    r,t,z=expand(val);rs,ts,zs=expand(der)
    rp,tp,zp=r.theta()-t,r+t.theta(),z.theta()
    E=rs*rs+ts*ts+zs*zs
    F=rs*rp+ts*tp+zs*zp
    G=rp*rp+tp*tp+zp*zp
    return E,F,G


def target_scalar(data,name,index):
    lo=np.array(data[name+'_lo'][index],copy=True);hi=np.array(data[name+'_hi'][index],copy=True)
    error=float(data[name+'_remainder'][index]) if name+'_remainder' in data else 0.
    if error<0 or np.any(lo>hi):raise ValueError('Invalid supplier enclosure')
    lo[0]=down(lo[0]-error);hi[0]=up(hi[0]+error)
    return P(I(lo[:,None],hi[:,None]))


def lower_value(poly):
    assert poly.first==0 and poly.c.lo.shape[1]==1
    tail=positive_sum_upper(np.maximum(abs(poly.c.lo[1:,0]),abs(poly.c.hi[1:,0])))
    return float(down(poly.c.lo[0,0]-tail))


def run(args):
    start=time.monotonic();geom=base.ExactHermite(args.geometry)
    target=json.loads(args.target.read_text());path=args.target.parent/target['data_file']
    if sha(path)!=target['data_sha256']:raise ValueError('Target packet hash mismatch')
    raw=np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False)
    left,right=raw['left'],raw['right']
    if not (left.shape==right.shape and np.all(right>left)):raise ValueError('Invalid audit intervals')
    if not (left[0]==geom.x[0] and right[-1]==geom.x[-1] and np.array_equal(right[:-1],left[1:])):
        raise ValueError('Target intervals do not partition the complete prefix')
    cosine=P(I(np.array([[.5,0,.5]])),-1,0)
    sine=P(I(np.array([[.5,0,-.5]])),-1,1)
    out=dict(scope=__doc__,geometry_sha256=sha(args.geometry),geometry_data_sha256=geom.meta['data_sha256'],
             target_sha256=sha(args.target),target_data_sha256=sha(path),script_sha256=sha(__file__),
             backend_sha256=sha(HERE/'db6f-audit-continuous-hermite.py'),
             supplier_claim=target.get('analytic_definition'),
             residual_norm='Bernstein convex-hull bound for each Fourier coefficient, then Fourier l1',
             target_supplier_independently_verified=False,complete_closed_surface=False,
             intervals=len(left),metric_operator_upper=0.,coordinate_residual_upper=[0.,0.,0.],
             minimum_a_lower=float('inf'),minimum_chart_rho_lower=float('inf'),worst_interval=None)
    count=len(left) if args.limit is None else min(args.limit,len(left))
    for k in range(count):
        A,e,ep=(target_scalar(raw,name,k) for name in ('a','e','ep'))
        rho=P.scalar(1.)-e*cosine;theta_s=ep*sine*qbounds(Q(-1,3))
        a2=A*A
        targetE=P.scalar(1.)+a2*theta_s*theta_s
        targetF=a2*theta_s*rho
        targetG=a2*rho*rho
        E,F,G=geometry_coefficients(geom,float(left[k]),float(right[k]))
        err=[(E-targetE).norm(),(F-targetF).norm(),(G-targetG).norm()]
        amin=lower_value(A);rmin=float(down(1-e.norm()))
        if min(amin,rmin)<=0:raise ArithmeticError('Supplier chart or radius lower bound not positive')
        v=float((I(ep.norm())/(3*I(rmin))).hi);ar=float(down(amin*rmin))
        ee=I(err[0])+2*I(v)*I(err[1])+I(v).square()*I(err[2])
        ef=(I(err[1])+I(v)*I(err[2]))/I(ar);eg=I(err[2])/I(ar).square()
        op=float(max((ee+ef).hi,(ef+eg).hi))
        if op>out['metric_operator_upper']:out['metric_operator_upper']=op;out['worst_interval']=k
        out['coordinate_residual_upper']=[max(x,y) for x,y in zip(out['coordinate_residual_upper'],err)]
        out['minimum_a_lower']=min(out['minimum_a_lower'],amin)
        out['minimum_chart_rho_lower']=min(out['minimum_chart_rho_lower'],rmin)
    out['intervals_checked']=count;out['entire_prefix_covered']=count==len(left)
    out['seconds']=time.monotonic()-start
    args.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('scope','supplier_claim')},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--target',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--limit',type=int)
    run(p.parse_args())
