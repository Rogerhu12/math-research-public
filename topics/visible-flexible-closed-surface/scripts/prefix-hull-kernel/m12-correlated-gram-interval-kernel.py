#!/usr/bin/env python3
"""Directed long-double intervals, real jets, and tensor-Chebyshev enclosures.

All inputs are exact dyadic floating values or rational enclosures. Arithmetic
uses NumPy longdouble basic operations, each widened by nextafter. Transcendental
values do not use unchecked libm values: sin/cos use a rational Taylor remainder,
and square-root endpoints are verified with integer arithmetic. This module is
an enclosure engine, not a certificate for any particular source or field.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
import numpy as np
LD=np.longdouble
NINF=LD('-inf');PINF=LD('inf')

def down(x):return np.nextafter(np.asarray(x,dtype=LD),NINF)
def up(x):return np.nextafter(np.asarray(x,dtype=LD),PINF)
def exact(x):
    if isinstance(x,F):return x
    if isinstance(x,(int,np.integer)):return F(int(x))
    p,q=LD(x).as_integer_ratio();return F(p,q)
def qinterval(q):
    q=F(q);v=LD(q.numerator)/LD(q.denominator)
    lo=v;hi=v
    while exact(lo)>q:lo=np.nextafter(lo,NINF)
    while exact(hi)<q:hi=np.nextafter(hi,PINF)
    return lo,hi

class I:
    __array_priority__=10000
    def __init__(self,lo=0,hi=None):
        if isinstance(lo,I):self.lo=lo.lo;self.hi=lo.hi;return
        if isinstance(lo,F) or (isinstance(lo,(int,np.integer)) and abs(int(lo))>2**63):
            if hi is not None:raise TypeError('Use I.bounds for rational endpoints')
            self.lo,self.hi=map(np.asarray,qinterval(F(int(lo)) if not isinstance(lo,F) else lo));return
        self.lo=np.asarray(lo,dtype=LD);self.hi=np.asarray(lo if hi is None else hi,dtype=LD)
        if np.any(self.lo>self.hi):raise ValueError('Reversed interval')
    @staticmethod
    def bounds(a,b):return I(qinterval(F(a))[0],qinterval(F(b))[1])
    @property
    def shape(self):return np.broadcast_shapes(self.lo.shape,self.hi.shape)
    def __getitem__(self,k):return I(self.lo[k],self.hi[k])
    def reshape(self,*shape):return I(self.lo.reshape(*shape),self.hi.reshape(*shape))
    def __neg__(self):return I(-self.hi,-self.lo)
    def __add__(self,b):
        if isinstance(b,Jet):return b+self
        b=asI(b);return I(down(self.lo+b.lo),up(self.hi+b.hi))
    __radd__=__add__
    def __sub__(self,b):
        if isinstance(b,Jet):return -b+self
        return self+-asI(b)
    def __rsub__(self,b):return asI(b)+-self
    def __mul__(self,b):
        if isinstance(b,Jet):return b*self
        b=asI(b)
        v=np.broadcast_arrays(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return I(down(np.minimum.reduce(v)),up(np.maximum.reduce(v)))
    __rmul__=__mul__
    def reciprocal(self):
        if np.any((self.lo<=0)&(self.hi>=0)):raise ZeroDivisionError('Interval contains zero')
        return I(down(1/self.hi),up(1/self.lo))
    def __truediv__(self,b):
        if isinstance(b,Jet):return b.reciprocal()*self
        return self*asI(b).reciprocal()
    def __rtruediv__(self,b):return asI(b)*self.reciprocal()
    def __pow__(self,n):
        if not isinstance(n,(int,np.integer)) or n<0:raise TypeError('Nonnegative integer power only')
        if n==0:return I(1)
        if n==1:return self
        if n==2:return self.square()
        h=self**(n//2);v=h.square();return v*self if n%2 else v
    def square(self):
        l=np.minimum(self.lo*self.lo,self.hi*self.hi);h=np.maximum(self.lo*self.lo,self.hi*self.hi)
        l=np.where((self.lo<=0)&(self.hi>=0),LD(0),down(l))
        return I(np.maximum(l,LD(0)),up(h))
    def abs_upper(self):return up(np.maximum(np.abs(self.lo),np.abs(self.hi)))
    def widen(self,e):e=asI(e).abs_upper();return I(down(self.lo-e),up(self.hi+e))
    def sum(self,axis=None):
        if axis is None:return self.reshape(-1).sum(0)
        a=np.moveaxis(self.lo,axis,0);b=np.moveaxis(self.hi,axis,0)
        lo=np.zeros(a.shape[1:],dtype=LD);hi=np.zeros(b.shape[1:],dtype=LD)
        for l,h in zip(a,b):lo=down(lo+l);hi=up(hi+h)
        return I(lo,hi)
    def sqrt(self):
        if np.any(self.lo<0):raise ValueError('Square root of negative interval')
        shape=np.broadcast_shapes(self.lo.shape,self.hi.shape)
        a=np.broadcast_to(self.lo,shape).reshape(-1);b=np.broadcast_to(self.hi,shape).reshape(-1)
        lo=np.sqrt(a,dtype=LD);hi=np.sqrt(b,dtype=LD)
        for k,(aa,bb) in enumerate(zip(a,b)):
            aq=exact(aa);bq=exact(bb)
            while exact(lo[k])**2>aq:lo[k]=np.nextafter(lo[k],NINF)
            while exact(hi[k])**2<bq:hi[k]=np.nextafter(hi[k],PINF)
        return I(lo.reshape(shape),hi.reshape(shape))
    def __repr__(self):return f'I({self.lo!r}, {self.hi!r})'

def asI(x):return x if isinstance(x,I) else I(x)
def pi_bounds():
    def atan_inv(n,terms=90):
        total=sum((F((-1)**k,(2*k+1)*n**(2*k+1)) for k in range(terms)),F(0))
        nxt=F((-1)**terms,(2*terms+1)*n**(2*terms+1))
        return (total,total+nxt) if nxt>0 else (total+nxt,total)
    a,b=atan_inv(5);c,d=atan_inv(239)
    return 16*a-4*d,16*b-4*c
PI=I.bounds(*pi_bounds())

def sincos(x):
    if isinstance(x,Jet):return x.sincos()
    x=asI(x)
    mid=x.lo/2+x.hi/2
    k=np.rint(mid/LD('1.570796326794896619231321691639751442')).astype(np.int64)
    if np.any(np.abs(k)>=2**62):raise ValueError('Trigonometric reduction requires bounded arguments')
    y=x-I(k)*PI/2
    broad=y.abs_upper()>LD(2)
    yy=I(np.where(broad,LD(0),y.lo),np.where(broad,LD(0),y.hi))
    y2=yy.square()
    sp=I(F((-1)**24,factorial(49)));cp=I(F((-1)**24,factorial(48)))
    for j in range(23,-1,-1):
        sp=sp*y2+F((-1)**j,factorial(2*j+1));cp=cp*y2+F((-1)**j,factorial(2*j))
    s=yy*sp;c=cp;mag=I(yy.abs_upper())
    s=s.widen((mag**50)/factorial(50));c=c.widen((mag**49)/factorial(49))
    quadrant=np.mod(k,4)
    sl=np.choose(quadrant,[s.lo,c.lo,-s.hi,-c.hi]);sh=np.choose(quadrant,[s.hi,c.hi,-s.lo,-c.lo])
    cl=np.choose(quadrant,[c.lo,-s.hi,-c.hi,s.lo]);ch=np.choose(quadrant,[c.hi,-s.lo,-c.lo,s.hi])
    return I(np.where(broad,-LD(1),np.maximum(sl,-LD(1))),np.where(broad,LD(1),np.minimum(sh,LD(1)))),I(np.where(broad,-LD(1),np.maximum(cl,-LD(1))),np.where(broad,LD(1),np.minimum(ch,LD(1))))

class Jet:
    """Univariate real Taylor coefficients f^(j)/j!, with interval base point."""
    __array_priority__=20000
    def __init__(self,c):self.c=[asI(x) for x in c]
    @property
    def order(self):return len(self.c)-1
    @classmethod
    def constant(cls,x,n):return cls([asI(x)]+[I(0)]*n)
    @classmethod
    def variable(cls,x,n,scale=1):return cls([asI(x),asI(scale)]+[I(0)]*(n-1)) if n else cls([asI(x)])
    def __getitem__(self,k):return Jet([c[k] for c in self.c])
    def lift(self,x):
        if isinstance(x,Jet):
            if x.order!=self.order:raise ValueError('Jet order differs')
            return x
        return Jet.constant(x,self.order)
    def __neg__(self):return Jet([-a for a in self.c])
    def __add__(self,b):
        if not isinstance(b,Jet):return Jet([self.c[0]+b]+self.c[1:])
        b=self.lift(b);return Jet([a+c for a,c in zip(self.c,b.c)])
    __radd__=__add__
    def __sub__(self,b):return self+-self.lift(b)
    def __rsub__(self,b):return self.lift(b)+-self
    def __mul__(self,b):
        if not isinstance(b,Jet):return Jet([a*b for a in self.c])
        b=self.lift(b);return Jet([sum((self.c[k]*b.c[n-k] for k in range(n+1)),I(0)) for n in range(self.order+1)])
    __rmul__=__mul__
    def reciprocal(self):
        c=[self.c[0].reciprocal()]
        for n in range(1,self.order+1):c.append(-c[0]*sum((self.c[k]*c[n-k] for k in range(1,n+1)),I(0)))
        return Jet(c)
    def __truediv__(self,b):return self*(b.reciprocal() if isinstance(b,Jet) else asI(b).reciprocal())
    def __rtruediv__(self,b):return self.lift(b)*self.reciprocal()
    def __pow__(self,n):
        if not isinstance(n,(int,np.integer)) or n<0:raise TypeError('Nonnegative integer power only')
        if n==0:return self.lift(1)
        if n==1:return self
        h=self**(n//2);v=h*h;return v*self if n%2 else v
    def sqrt(self):
        c=[self.c[0].sqrt()]
        for n in range(1,self.order+1):c.append((self.c[n]-sum((c[k]*c[n-k] for k in range(1,n)),I(0)))/(2*c[0]))
        return Jet(c)
    def sincos(self):
        s0,c0=sincos(self.c[0]);s=[s0];c=[c0]
        for n in range(1,self.order+1):
            s.append(sum((k*self.c[k]*c[n-k] for k in range(1,n+1)),I(0))/n)
            c.append(-sum((k*self.c[k]*s[n-k] for k in range(1,n+1)),I(0))/n)
        return Jet(s),Jet(c)

def base(x):return x.c[0] if isinstance(x,Jet) else asI(x)
def const_like(x,value):return Jet.constant(value,x.order) if isinstance(x,Jet) else asI(value)
def drop_constant_jet(x):
    if isinstance(x,Jet) and all(np.all(c.lo==0) and np.all(c.hi==0) for c in x.c[1:]):return x.c[0]
    return x
def poly(coeff,x):
    out=const_like(x,0)
    for c in reversed(coeff):out=out*x+c
    return out

def implicit_angle(e,u):
    """Unique real psi solving psi-e sin(3 psi)/3=u, |e|<1.

    A floating Newton iterate is a proposal only. A directed residual divided
    by the global positive derivative lower bound encloses the true root.
    The implicit real-jet recurrence then encloses each derivative.
    """
    ej=isinstance(e,Jet);uj=isinstance(u,Jet)
    n=e.order if ej else (u.order if uj else 0)
    eb=base(e);ub=base(u);m=up(np.maximum(np.abs(eb.lo),np.abs(eb.hi)))
    if np.any(m>=1):raise ValueError('Implicit chart requires |e|<1')
    em=(eb.lo+eb.hi)/2;um=(ub.lo+ub.hi)/2;p=np.broadcast_arrays(em,um)[1].copy()
    for _ in range(14):p-=(p-em*np.sin(3*p)/3-um)/(1-em*np.cos(3*p))
    pp=I(p);s,c=sincos(3*pp);res=pp-eb*s/3-ub
    rad=(res/I(down(1-m))).abs_upper();p0=pp.widen(rad)
    # An interval Newton contraction for the whole parameter family. The
    # derivative interval covers the segment from the proposal to every old
    # enclosed root. The original global monotonic enclosure remains the
    # existence argument; these intersections only tighten it.
    if np.any(p0.hi-p0.lo>LD('1e-10')):
        for _ in range(3):
            segment=I(np.minimum(p0.lo,pp.lo),np.maximum(p0.hi,pp.hi))
            deriv=1-eb*sincos(3*segment)[1]
            contracted=pp-res/deriv
            p0=I(np.maximum(p0.lo,contracted.lo),np.minimum(p0.hi,contracted.hi))
    if not (ej or uj):return p0
    e=e if ej else Jet.constant(e,n);u=u if uj else Jet.constant(u,n)
    s0,c0=sincos(3*p0);ps=[p0];ss=[s0];cc=[c0];den=1-e.c[0]*c0
    for j in range(1,n+1):
        sk=sum((3*k*ps[k]*cc[j-k] for k in range(1,j)),I(0))/j
        ck=-sum((3*k*ps[k]*ss[j-k] for k in range(1,j)),I(0))/j
        pj=(u.c[j]+(e.c[0]*sk+sum((e.c[k]*ss[j-k] for k in range(1,j+1)),I(0)))/3)/den
        ps.append(pj);ss.append(3*pj*c0+sk);cc.append(-3*pj*s0+ck)
    return Jet(ps)

def cheb_nodes(n):
    q=[I(F(2*j+1,2*n)) for j in range(n)]
    args=I(np.array([a.lo for a in q]),np.array([a.hi for a in q]))*PI
    return sincos(args)[1]

def cheb_matrix(n):
    rows=[]
    for k in range(n):
        args=[I(F(k*(2*j+1),2*n))*PI for j in range(n)]
        ar=I(np.array([a.lo for a in args]),np.array([a.hi for a in args]))
        rows.append(sincos(ar)[1]*F(1 if k==0 else 2,n))
    return I(np.array([a.lo for a in rows]),np.array([a.hi for a in rows]))

def apply_cheb_axis(values,axis):
    values=asI(values);n=values.shape[axis];weights=cheb_matrix(n)
    v=I(np.moveaxis(values.lo,axis,-1),np.moveaxis(values.hi,axis,-1))
    rows=[]
    for k in range(n):rows.append((v*weights[k]).sum(-1))
    lo=np.stack([r.lo for r in rows],axis=-1);hi=np.stack([r.hi for r in rows],axis=-1)
    return I(np.moveaxis(lo,-1,axis),np.moveaxis(hi,-1,axis))

def tensor_enclose(evaluator,radial,angles,nr=12,na=12,normalized_remainder_evaluator=None):
    """Complete tensor interpolation enclosure on radial x angular boxes.

    evaluator accepts I or Jet arguments and returns a sequence of scalar
    I/Jet expressions. radial and angles have broadcastable box shapes. Node
    values are transformed before absolute values. Real interval jets supply
    the complete Nth-derivative remainder. A sampled bound alone is never
    promoted to a continuous claim.
    """
    radial=asI(radial);angles=asI(angles)
    rc=(I(radial.lo)+I(radial.hi))/2;rh=(I(radial.hi)-I(radial.lo))/2
    ac=(I(angles.lo)+I(angles.hi))/2;ah=(I(angles.hi)-I(angles.lo))/2
    rn=rc.reshape(*rc.shape,1,1)+rh.reshape(*rh.shape,1,1)*cheb_nodes(nr).reshape(nr,1)
    an=ac.reshape(*ac.shape,1,1)+ah.reshape(*ah.shape,1,1)*cheb_nodes(na).reshape(1,na)
    values=evaluator(rn,an)
    rbox=rc+rh*I(-1,1);abox=ac+ah*I(-1,1)
    if normalized_remainder_evaluator is None:
        rder=evaluator(Jet.variable(rbox,nr,rh),Jet.constant(abox,nr))
        ader=evaluator(Jet.constant(rbox,na),Jet.variable(abox,na,ah))
    else:
        # The caller supplies a validated interval family that contains each
        # individual f(rc_i+rh_i*t,theta) for t in [-1,1], including all of its
        # derivatives. Nodes remain individual exact-source evaluations.
        rder=normalized_remainder_evaluator(Jet.variable(I(-1,1),nr),Jet.constant(abox,nr))
        ader=normalized_remainder_evaluator(Jet.constant(I(-1,1),na),Jet.variable(abox,na,ah))
    result=[]
    for v,rd,ad in zip(values,rder,ader):
        coeff=apply_cheb_axis(apply_cheb_axis(v,-2),-1)
        polybound=I(coeff.abs_upper()).sum(-1).sum(-1)
        er=I(rd.c[nr].abs_upper())/2**(nr-1)
        ea=I(ad.c[na].abs_upper())/2**(na-1)
        # Tensor telescoping f-Ir Ia f=(f-Ir f)+Ir(f-Ia f).
        # Explicit DCT cardinal coefficients give ||I_N|| <= 2N-1.
        error1=er+(2*nr-1)*ea;error2=ea+(2*na-1)*er
        error=I(np.minimum(error1.lo,error2.lo),np.minimum(error1.hi,error2.hi))
        total=polybound+error
        result.append({'upper':total.hi,'polynomial_upper':polybound.hi,'remainder_upper':error.hi,
            'radial_remainder_upper':er.hi,'angular_remainder_upper':ea.hi,
            'node_min':np.min(v.lo,axis=(-2,-1)),'node_max':np.max(v.hi,axis=(-2,-1)),
            'node_width_max':np.max(up(v.hi-v.lo),axis=(-2,-1))})
    return result

def matrix_norm_bound(E,Fv,G):
    e=np.maximum(np.abs(E.lo),np.abs(E.hi)) if isinstance(E,I) else np.asarray(E,dtype=LD)
    f=np.maximum(np.abs(Fv.lo),np.abs(Fv.hi)) if isinstance(Fv,I) else np.asarray(Fv,dtype=LD)
    g=np.maximum(np.abs(G.lo),np.abs(G.hi)) if isinstance(G,I) else np.asarray(G,dtype=LD)
    return up(np.maximum(e,g)+f)
