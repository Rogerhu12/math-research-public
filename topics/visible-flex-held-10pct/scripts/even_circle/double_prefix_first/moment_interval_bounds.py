"""Rational enclosures for the defining complementary moment matrices.

Only arithmetic with Fraction enters enclosure inequalities. mpmath supplies
an arbitrary inverse candidate; its correctness is checked by an exact
Neumann residual. This certifies coefficient bounds, not a solved surface.
"""
from fractions import Fraction as F
from functools import lru_cache
import math
import mpmath as mp


def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def mul(a,b):
    v=[a[i]*b[j] for i in (0,1) for j in (0,1)]
    return min(v),max(v)
def divide(a,b):
    if b[0]<=0<=b[1]:raise ArithmeticError('Interval division through zero')
    return mul(a,(1/b[1],1/b[0]))
def upper_abs(a):return max(abs(a[0]),abs(a[1]))
def upper_float(q):return math.nextafter(float(q),math.inf)


@lru_cache(None)
def pi_interval():
    def atan(x,N=60):
        s=sum(F((-1)**j)*x**(2*j+1)/(2*j+1) for j in range(N))
        t=F((-1)**N)*x**(2*N+1)/(2*N+1)
        return min(s,s+t),max(s,s+t)
    return add(scale(atan(F(1,5)),F(16)),scale(atan(F(1,239)),F(-4)))


def sincos(x,degree=160):
    term=F(1);co=F(0);si=F(0)
    for k in range(degree+1):
        if k%4==0:co+=term
        elif k%4==1:si+=term
        elif k%4==2:co-=term
        else:si-=term
        term*=x/F(k+1)
    # Taylor's integral remainder, with |all sine/cosine derivatives|<=1.
    err=abs(term)
    return (si-err,si+err),(co-err,co+err)


def beta_characteristic(z,degree=100):
    """Integral S'(t) exp(i z t), S'=630 t^4(1-t)^4."""
    term=F(1);re=F(0);im=F(0)
    for k in range(degree+1):
        moment=F(15120,math.prod(k+j for j in range(5,10)))
        v=term*moment
        if k%4==0:re+=v
        elif k%4==1:im+=v
        elif k%4==2:re-=v
        else:im-=v
        term*=z/F(k+1)
    err=abs(term) # nonnegative S' has total integral one
    return (re-err,re+err),(im-err,im+err)


@lru_cache(None)
def coefficient_enclosures(n,M,a_text,eps_text,center_half_period,lock_fundamental):
    a,eps=F(a_text),F(eps_text);pi=pi_interval();one=(F(1),F(1))
    W=[add(one,neg(divide((n*(2*a+eps),)*2,scale(pi,F(2)))))]
    for j in range(1,2*M+1):
        si,co=sincos(n*j*a);re,im=beta_characteristic(n*j*eps)
        v=neg(divide(add(mul(si,re),mul(co,im)),scale(pi,F(j))))
        W.append(scale(v,F((-1)**(j*center_half_period))))
    G=[[W[k] if j==0 else W[j] if k==0 else scale(add(W[abs(j-k)],W[j+k]),F(1,2)) for k in range(M+1)] for j in range(M+1)]
    ids=list(range(M+1)) if lock_fundamental else [0]+list(range(2,M+1))
    B=[[G[j][k] for k in ids] for j in ids];size=len(ids)
    with mp.workdps(100):
        midpoint=mp.matrix(size,size)
        for j in range(size):
            for k in range(size):
                q=(B[j][k][0]+B[j][k][1])/2
                midpoint[j,k]=mp.mpf(q.numerator)/q.denominator
        inverse=midpoint**-1
        R=[[F(mp.nstr(inverse[j,k],60)) for k in range(size)] for j in range(size)]
    residual=[]
    for j in range(size):
        row=[]
        for k in range(size):
            v=(F(j==k),F(j==k))
            for l in range(size):v=add(v,neg(scale(B[l][k],R[j][l])))
            row.append(v)
        residual.append(row)
    beta=max(sum(upper_abs(v) for v in row) for row in residual)
    if beta>=1:raise ArithmeticError('Exact inverse residual does not certify invertibility')
    rnorm=max(sum(abs(v) for v in row) for row in R)
    error=beta/(1-beta)*rnorm
    H=[]
    for target in range(2,M+1):
        column=ids.index(target);row=[(F(0),F(0))]*(M+1)
        for j,k in enumerate(ids):row[k]=((R[j][column]-error)/2,(R[j][column]+error)/2)
        H.append(row)
    fundamental=[]
    for row in H:
        v=(F(0),F(0))
        for k in range(M+1):v=add(v,mul(G[1][k],row[k]))
        fundamental.append((F(0),F(0)) if lock_fundamental else scale(v,F(2)))
    return dict(coefficients=H,fundamental=fundamental,neumann_residual=beta,inverse_error=error,
                n=n,M=M,halfwidth=str(a),transition=str(eps),
                defining_identity='H columns are one half of the inverse weighted Gram columns; exact rational interval residual encloses the unique exact coefficients.')
