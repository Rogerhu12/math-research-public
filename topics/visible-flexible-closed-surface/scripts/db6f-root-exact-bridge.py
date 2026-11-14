#!/usr/bin/env python3
"""Rational certificate for the exact meridian bridge and metric transfer.

The Decimal root is only a seed. Root existence is certified by exact rational
Taylor-integral sign enclosures at two rational endpoints. All subsequent
parameter and metric error budgets use rational interval arithmetic.
The physical tail cut identities and positive exact tail calibration are
separate analytic inputs, not inferred from a sampled tail evaluator.
"""
import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path


@dataclass(frozen=True)
class J:
    lo: Q
    hi: Q = None

    def __post_init__(self):
        object.__setattr__(self,'lo',Q(self.lo))
        object.__setattr__(self,'hi',self.lo if self.hi is None else Q(self.hi))
        if self.lo>self.hi:raise ValueError('Reversed rational interval')
    @staticmethod
    def get(x):return x if isinstance(x,J) else J(Q(x))
    def __add__(self,b):
        b=J.get(b);return J(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return J(-self.hi,-self.lo)
    def __sub__(self,b):return self+-J.get(b)
    def __rsub__(self,b):return J.get(b)+-self
    def __mul__(self,b):
        b=J.get(b);v=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return J(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=J.get(b)
        if b.lo<=0<=b.hi:raise ValueError('Division interval contains zero')
        return self*J(1/b.hi,1/b.lo)
    def __rtruediv__(self,b):return J.get(b)/self
    def __pow__(self,n):
        if n<0:return J(1)/(self**(-n))
        if n==0:return J(1)
        if n%2:return J(self.lo**n,self.hi**n)
        return J(0 if self.lo<=0<=self.hi else min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def absmax(self):return max(abs(self.lo),abs(self.hi))


def hull(x,bits=384):
    x=J.get(x);scale=2**bits
    lo=x.lo*scale;hi=x.hi*scale
    return J(Q(lo.numerator//lo.denominator,scale),Q(-((-hi.numerator)//hi.denominator),scale))


def atan(x,n=200):
    x=Q(x);s=Q(0)
    if not 0<x<1:raise ValueError('Atan series input not in (0,1)')
    for k in range(n):s+=(-1)**k*x**(2*k+1)/(2*k+1)
    next_term=(-1)**n*x**(2*n+1)/(2*n+1)
    return hull(J(min(s,s+next_term),max(s,s+next_term)))


def sqrtq(x,bits=384):
    x=Q(x);scale=2**bits
    n=math.isqrt((x.numerator*scale*scale)//x.denominator)
    lo=Q(n,scale)
    return J(lo,lo if lo*lo==x else Q(n+1,scale))


def phase_upper(L,pt,ps):
    """Bernstein hull of the cubic over 32 rational t subintervals."""
    a=3*pt-L*ps;b=-2*pt+L*ps
    if a.lo<=0 or b.hi>=0 or (a+b).lo<=0:
        raise ValueError('Could not prove positive phase t**2*(a+b*t)')
    peak=Q(0)
    for n in range(32):
        l=Q(n,32);h=Q(1,32)
        c=[a*l*l+b*l**3,(2*a*l+3*b*l*l)*h,(a+3*b*l)*h*h,b*h**3]
        for k in range(4):
            z=sum((c[i]*Q(math.comb(k,i),math.comb(3,i)) for i in range(k+1)),J(0))
            peak=max(peak,z.hi)
    return peak


def gap(L,pt,ps,c,terms=27):
    """Exact integral of the Taylor polynomial in a*t²+b*t³."""
    L=Q(L);a=3*pt-L*ps;b=-2*pt+L*ps
    maxpower=2*terms-1
    ap=[a**k for k in range(maxpower+1)]
    bp=[b**k for k in range(maxpower+1)]
    value=J(0)
    for m in range(terms):
        k=2*m+1
        integral=sum((math.comb(k,j)*ap[k-j]*bp[j]/(2*k+j+1) for j in range(k+1)),J(0))
        value+=integral*Q((-1)**m,math.factorial(k))
    # Phase is separately proved between 0 and pi/2<2. Taylor degree 53
    # has the generic Lagrange remainder 2**54/54! when terms=27.
    order=2*terms
    error=Q(2**order,math.factorial(order))
    return L*(value+J(-error,error))-(1-c)


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def enc(x):
    x=hull(x,256);return {'lo':str(x.lo),'hi':str(x.hi),'display':[float(x.lo),float(x.hi)]}
def upper(x):
    x=Q(x);f=float(x)
    return math.nextafter(f,math.inf) if Q.from_float(f)<x else f


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--target',type=Path,required=True)
    p.add_argument('--tail-manifest',type=Path,required=True)
    p.add_argument('--metric-certificate',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    g=json.loads(args.geometry.read_text());target=json.loads(args.target.read_text())
    tail=json.loads(args.tail_manifest.read_text());certificate=json.loads(args.metric_certificate.read_text())
    if certificate['geometry_sha256']!=sha(args.geometry):raise ValueError('Metric certificate geometry mismatch')
    if certificate['target_sha256']!=sha(args.target):raise ValueError('Metric certificate target mismatch')
    c=Q.from_float(tail['parameters']['rCut']);w=Q.from_float(tail['parameters']['wCut'])
    if not (Q(59,100)<c<Q(61,100) and w==Q(1,2)):raise ValueError('This certificate is specialized to the frozen macro cut')
    pi=16*atan(Q(1,5))-4*atan(Q(1,239))
    pt=hull(pi/2-atan(w));E=1+w*w
    ps=hull((-7*w/c)/(J(E)*sqrtq(E)))
    old={k:Q(v) for k,v in target['bridge_constants'].items() if k in ('L','pt','ps')}
    # Fast untrusted seed in the standard library. The exact sign test below
    # is the only root proof; errors here can merely make that test fail.
    with localcontext() as context:
        context.prec=90
        dd=lambda x:Decimal(x.numerator)/Decimal(x.denominator)
        pm=dd((pt.lo+pt.hi)/2);sm=dd((ps.lo+ps.hi)/2);cm=dd(c)
        def fn(L):
            a=3*pm-L*sm;b=-2*pm+L*sm
            ap=[a**k for k in range(54)];bp=[b**k for k in range(54)]
            value=Decimal(0)
            for m in range(27):
                k=2*m+1
                value+=sum((Decimal(math.comb(k,j))*ap[k-j]*bp[j]/Decimal(2*k+j+1) for j in range(k+1)),Decimal(0))*Decimal((-1)**m)/Decimal(math.factorial(k))
            return L*value-(1-cm)
        left=dd(old['L'])-Decimal('1e-12');right=dd(old['L'])+Decimal('1e-12')
        if not fn(left)<0<fn(right):raise ValueError('Untrusted seed bracket failed')
        for _ in range(128):
            mid=(left+right)/2
            if fn(mid)<0:left=mid
            else:right=mid
        seed=Q(str((left+right)/2))
    radius=Q(1,10**40);length=J(seed-radius,seed+radius)
    peak=phase_upper(length,pt,ps)
    if not (peak<pi.lo/2 and length.lo>Q(3,5) and length.hi<Q(7,10)):
        raise ValueError('Phase or length box verification failed')
    flo=gap(length.lo,pt,ps,c);fhi=gap(length.hi,pt,ps,c)
    if not (flo.hi<0<fhi.lo):raise ValueError('Exact rational Taylor signs did not bracket a root')
    # For t>=1/2, phi>=pt/2>1/2. Concavity gives sin phi>1/4;
    # cos(phi)*ps*(t^3-t^2)>=0. Thus gap'(L)>1/8 on this box.
    if not (pt.lo>1 and ps.hi<0 and pi.hi<4):raise ValueError('Monotonicity hypotheses fail')
    prefix_end=Q(target['exact_prefix_end']);old_end=Q(target['frozen_total_end'])
    exact_end=prefix_end+length;lam=old_end/exact_end
    dL=(length-old['L']).absmax();dp=(pt-old['pt']).absmax();ds=(ps-old['ps']).absmax()
    endpoint_shift=(exact_end-old_end).absmax()
    # On u<=.7, L in [.6,.7], t<=1.2, pt in [1,1.2], |ps|<=5,
    # uniform phase parameter derivatives are bounded by 8,3,64.
    if not (pt.hi<Q(6,5) and ps.lo>-5 and -5<old['ps']<0
            and 1<old['pt']<Q(6,5) and Q(3,5)<old['L']<Q(7,10)
            and prefix_end>0 and 0<old_end-prefix_end<Q(7,10)):
        raise ValueError('Metric perturbation box hypotheses fail')
    da=endpoint_shift+8*dp+3*ds+64*dL
    amin=Q(59,100)
    perturb=max((lam**2-1).absmax(),2*da/amin+(da/amin)**2)
    old_error=Q.from_float(certificate['metric_operator_upper'])
    new_error=old_error*(1+perturb)+perturb
    report={
        'status':'exact-rational-root-and-prefix-metric-transfer-certificate-pending-independent-review',
        'script_sha256':sha(__file__),'geometry_sha256':sha(args.geometry),
        'target_sha256':sha(args.target),'tail_manifest_sha256':sha(args.tail_manifest),
        'metric_certificate_sha256':sha(args.metric_certificate),
        'physical_cut_radius_exact':str(c),'physical_cut_slope_exact':str(w),
        'physical_cut_second_derivative_exact':str(-7*w/c),
        'exact_pt':enc(pt),'exact_ps':enc(ps),'exact_L':enc(length),
        'gap_at_left':enc(flo),'gap_at_right':enc(fhi),
        'phase_upper':upper(peak),'gap_derivative_lower_exact':'1/8',
        'unique_root_in_box':True,'arclength_rescale':enc(lam),
        'uniform_radius_difference_upper':upper(da),
        'relative_target_metric_difference_upper':upper(perturb),
        'transferred_metric_operator_upper':upper(new_error),
        'original_metric_operator_upper':certificate['metric_operator_upper'],
        'tail_cut_identity_and_positive_exact_calibration_are_analytic_inputs':True,
        'complete_closed_surface':False,
        'not_certified':['positive exact tail calibration alpha','tail metric error','common Cartesian two-jet seam','infinite nonlinear solution','README completion']}
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('unique_root_in_box','phase_upper','uniform_radius_difference_upper','relative_target_metric_difference_upper','transferred_metric_operator_upper')},indent=2))


if __name__=='__main__':main()
