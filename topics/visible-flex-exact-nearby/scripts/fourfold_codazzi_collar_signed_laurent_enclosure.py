"""Noncircular Laurent interval coefficients and a separate complete strip remainder."""
from functools import lru_cache
from fractions import Fraction as Q
from math import factorial
from flint import acb,acb_poly,arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check

DEGREE=128
WIDTH=Q(1,512)


@lru_cache(maxsize=2048)
def weight(j):
    return (exact(4*abs(j)*WIDTH)).exp().upper()


class Field:
    """The unknown holomorphic remainder has supremum at most error on the strip."""
    __slots__=('lo','p','error','size')

    def __init__(self,lo,coeff,error=0):
        p=coeff if isinstance(coeff,acb_poly) else acb_poly(coeff)
        e=arb(error).upper()
        if len(p) and (lo < -DEGREE or lo+len(p)-1 > DEGREE):
            keep=[]
            for k,z in enumerate(p,lo):
                if -DEGREE<=k<=DEGREE:keep.append(z)
                else:e+=abs(z).upper()*weight(k)
            p=acb_poly(keep);lo=max(-DEGREE,lo)
        self.lo=lo if len(p) else 0
        self.p=p;self.error=e.upper()
        self.size=sum((abs(z).upper()*weight(k) for k,z in enumerate(p,self.lo)),arb(0)).upper()
        check(self.size.is_finite() and self.error.is_finite() and self.error>=0,'finite signed Laurent and tail')

    @classmethod
    def scalar(cls,z):
        return cls(0,[acb(z)])

    def coeff(self,k):
        return self.p[k-self.lo] if self.lo<=k<self.lo+len(self.p) else acb(0)

    def cap(self):return (self.size+self.error).upper()

    def inflate(self,e):return Field(self.lo,self.p,self.error+e)

    def scale(self,v):
        z=acb(v)
        return Field(self.lo,self.p*z,self.error*abs(z).upper())

    def __neg__(self):return Field(self.lo,-self.p,self.error)

    def __add__(self,b):
        if not isinstance(b,Field):b=Field.scalar(b)
        lo=min(self.lo,b.lo)
        return Field(lo,self.p.left_shift(self.lo-lo)+b.p.left_shift(b.lo-lo),self.error+b.error)

    __radd__=__add__

    def __sub__(self,b):return self+(-b)
    def __rsub__(self,b):return -self+b

    def __mul__(self,b):
        if not isinstance(b,Field):return self.scale(b)
        return Field(self.lo+b.lo,self.p*b.p,self.error*b.cap()+self.size*b.error)

    __rmul__=__mul__

    def separated_mean(self):
        c=list(self.p);z=self.coeff(0)
        if self.lo<=0<self.lo+len(c):c[-self.lo]=acb(0)
        return z,Field(self.lo,c,self.error)

    def reciprocal(self):
        z,rem=self.separated_mean()
        check(abs(z).lower()>0,'true nonzero angular constant interval of the rational denominator')
        u=rem.scale(-1/z);m=u.cap();check(m<1,'uniform angular reciprocal series')
        term=Field.scalar(1);total=term
        for _ in range(8):
            term=term*u;total=total+term
        return total.inflate(m**9/(1-m)).scale(1/z)

    def exponential(self):
        v=self.cap();check(v<24,'complete nonconstant phase exponential disk')
        K=64;total=Field.scalar(1)
        for k in range(K,0,-1):total=(total*self).scale(arb(1)/k)+1
        return total.inflate(v.exp()*v**(K+1)/factorial(K+1))


def angular_taylor(t,coeff,bound,derivative=0,order=4):
    """Taylor in NONCONSTANT t only, true whole radial and frequency interval retained."""
    from math import comb,factorial
    z,u=t.separated_mean()
    check(z.imag.contains(0),'real original radial-parameter centre')
    z=z.real
    rad=(1-abs(z).upper()).lower();v=u.cap();K=len(coeff)
    check(rad>0 and v<rad and derivative+order<K,'qualified nonconstant angular Taylor disk')
    g=[]
    for k in range(order+1):
        d=derivative+k;value=arb(0)
        for i in range(K-1,d-1,-1):value=value*z+coeff[i]*comb(i,d)
        zabs=abs(z).upper();ratio=zabs*exact(Q(K+1,K+1-d))
        check(ratio<1,'full infinite normalized scalar coefficient tail')
        tail=bound*comb(K,d)*(zabs**(K-d))/(1-ratio)
        value=(value+arb(0,tail.upper()))*(factorial(d)//factorial(k))
        g.append(value)
    total=Field.scalar(g[-1])
    for c in reversed(g[:-1]):total=total*u+c
    # Cauchy on the circle around z of radius rad (global disk radius one).
    # f^(d)(z+u) has normalized kth term bounded M (k+d)!/k! rad^(-k-d).
    k=order+1;ratio=(v/rad)*exact(Q(k+derivative+1,k+1))
    check(ratio<1,'complete differentiated nonconstant angular tail')
    fee=bound*exact(factorial(k+derivative)//factorial(k))*v**k/rad**(k+derivative)/(1-ratio)
    return total.inflate(fee)
