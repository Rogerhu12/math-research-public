"""(r,phi) Taylor coefficients for one genuine Gauss chart. Complex parameters retain all design derivatives."""
from math import comb
import numpy as np


class J:
    """Orders r<=1, phi<=2, normalized by factorials; never conjugate a varied real parameter."""
    __array_priority__=1000
    def __init__(self,value,dr=0,dp=0):
        self.a={(0,0):np.asarray(value)}
        if not np.isscalar(dr) or dr!=0:self.a[1,0]=np.asarray(dr)
        if not np.isscalar(dp) or dp!=0:self.a[0,1]=np.asarray(dp)
    @classmethod
    def pack(cls,q):
        v=cls.__new__(cls);v.a=q;return v
    @property
    def value(self):return self.a[0,0]
    def jet(self,i,k):
        v=self.a.get((i,k),0)
        return v*(2 if k==2 else 1)
    def __add__(self,o):
        o=lift(o);return J.pack({k:self.a.get(k,0)+o.a.get(k,0) for k in self.a.keys()|o.a.keys()})
    __radd__=__add__
    def __neg__(self):return J.pack({k:-v for k,v in self.a.items()})
    def __sub__(self,o):return self+(-lift(o))
    def __rsub__(self,o):return lift(o)+(-self)
    def __mul__(self,o):
        o=lift(o);q={}
        for (i,j),x in self.a.items():
            for (k,l),y in o.a.items():
                if i+k<=1 and j+l<=2:
                    t=(i+k,j+l);q[t]=q.get(t,0)+x*y
        return J.pack(q)
    __rmul__=__mul__
    def __truediv__(self,o):return self*recip(lift(o))
    def __rtruediv__(self,o):return lift(o)*recip(self)
    def __pow__(self,k):
        if not isinstance(k,int) or k<0:raise ValueError('Nonnegative integer power required.')
        q=J(1);t=self
        while k:
            if k%2:q=q*t
            k//=2
            if k:t=t*t
        return q
    def at(self,cond,other):
        o=lift(other);return J.pack({k:np.where(cond,self.a.get(k,0),o.a.get(k,0)) for k in self.a.keys()|o.a.keys()})


def lift(x):return x if isinstance(x,J) else J(x)
def operation(x,coeff):
    z=J.pack({k:v for k,v in x.a.items() if k!=(0,0)}|{(0,0):0.})
    # The input has order at most three. The scalar coefficients are analytic in a complex-step design.
    return lift(coeff[0])+z*(lift(coeff[1])+z*(lift(coeff[2])+z*coeff[3]))
def recip(x):
    if np.any(abs(x.value)<1.e-300):raise FloatingPointError('Unseparated chart denominator.')
    v=1/x.value;return operation(x,(v,-v*v,v**3,-v**4))
def sine(x):
    s,c=np.sin(x.value),np.cos(x.value);return operation(x,(s,c,-s/2,-c/6))
def cosine(x):
    s,c=np.sin(x.value),np.cos(x.value);return operation(x,(c,-s,-c/2,s/6))
def root(x):
    if np.any(x.value.real<=0):raise FloatingPointError('Unseparated positive square root.')
    r=np.sqrt(x.value);return operation(x,(r,.5/r,-.125/r**3,.0625/r**5))
def arcsine(x):
    z=x.value
    if np.any(abs(z.real)>=1):raise FloatingPointError('Signed latitude left its positive hemisphere.')
    r=np.sqrt(1-z*z);return operation(x,(np.arcsin(z),1/r,z/(2*r**3),(1+2*z*z)/(6*r**5)))
def vecjet(v,i,k,shape):
    return np.stack([np.broadcast_to(t.jet(i,k),shape) for t in v],axis=-1)


def implicit(target,fun,lo_width):
    """Solve the real lift in its global monotonicity bracket, then differentiate the SAME equation."""
    center=np.broadcast_to(target.value.real,fun[0]);lo=center-lo_width;hi=center+lo_width
    x=center.copy()
    for _ in range(48):
        dz,jac=fun[1](x);f=x+dz-center
        if np.any(jac<=0):raise FloatingPointError('Material angular fold.')
        if np.max(abs(f))<5.e-15:break
        lo=np.where(f<0,x,lo);hi=np.where(f>0,x,hi)
        step=x-f/jac;x=np.where((step>=lo)&(step<=hi),step,(lo+hi)/2)
    z=J(x)
    for _ in range(4):
        f,df=fun[2](z)
        z=z-(z+f-target)/(1+df)
    f,_=fun[2](z);res=z+f-target
    err=max(float(np.max(abs(a.real))) for a in res.a.values())
    return z,err


def taper(alpha,left,theta):
    t=(alpha-.025)/.825;inside=(t.value.real>0)&(t.value.real<1)&left
    v=t.at(inside,0.)
    # S11 has five zero derivatives at both joins. Use a stable complementary polynomial above 1/2.
    def poly(x):
        return 2772*sum(((-1)**i*comb(5,i)/(6+i)*x**(6+i) for i in range(6)),J(0))
    small=v.value.real<=.5
    S=poly(v.at(small,0.)).at(small,1-poly((1-v).at(~small,0.)))
    gamma=(theta*(1-S)).at(inside,J(theta).at((t.value.real<=0)&left,0.))
    rate=(-theta*2772/.825*v**5*(1-v)**5).at(inside,0.)
    return gamma,rate

