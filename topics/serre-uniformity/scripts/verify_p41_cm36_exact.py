#!/usr/bin/env python3
"""Standard-library exact identities behind the CM(-36) three-isogenies."""
from fractions import Fraction as F


def add(*polys):
    out={}
    for p in polys:
        for key,value in p.items():out[key]=out.get(key,F(0))+value
    return {k:v for k,v in out.items() if v}


def scale(p,a):return {k:v*a for k,v in p.items() if v*a}


def mul(p,q):
    out={}
    for (a,b),v in p.items():
        for (c,d),w in q.items():out[a+c,b+d]=out.get((a+c,b+d),F(0))+v*w
    return {k:v for k,v in out.items() if v}


def power(p,n):
    out={(0,0):F(1)}
    for _ in range(n):out=mul(out,p)
    return out


def reduce_kernel(p):
    # r^4=1/3-2r^2, equivalent to3r^4+6r^2-1=0.
    p=dict(p)
    while any(a>=4 for a,b in p):
        a,b=max(k for k in p if k[0]>=4);v=p.pop((a,b))
        p=add(p,{(a-4,b):v/3,(a-2,b):-2*v})
    return p


def qm(a,b):return (a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qa(a,b):return (a[0]+b[0],a[1]+b[1])
def qs(a,c):return (a[0]*c,a[1]*c)
def qi(a):
    n=a[0]*a[0]-3*a[1]*a[1]
    return (a[0]/n,-a[1]/n)
def qp(a,n):
    out=(F(1),F(0))
    for _ in range(n):out=qm(out,a)
    return out


def main():
    one={(0,0):F(1)};r={(1,0):F(1)};x={(0,1):F(1)}
    v=add(scale(power(r,2),3),one);w=add(power(r,3),r);d=add(x,scale(r,-1))
    nx=add(mul(x,power(d,2)),scale(mul(v,d),2),scale(w,4))
    ny=add(power(d,3),scale(mul(v,d),-2),scale(w,-8))
    A=add(scale(one,-9),scale(power(r,2),-30));B=add(scale(power(r,3),-70),scale(r,-42))
    identity=add(mul(add(power(x,3),x),power(ny,2)),scale(power(nx,3),-1),
                 scale(mul(mul(A,nx),power(d,4)),-1),scale(mul(B,power(d,6)),-1))
    assert reduce_kernel(identity)=={}
    # Both j values are computed over Q[sqrt3] using B^2, so no root sign is hidden.
    for sign in [-1,1]:
        square=(F(sign),F(2,3))
        if sign==-1:
            ca=(F(21),F(-20));factor=(F(28),F(-140,3));expected=(F(76771008),F(-44330496))
        else:
            ca=(F(-21),F(-20));factor=(F(-28),F(-140,3));expected=(F(76771008),F(44330496))
        cb2=qm(square,qp(factor,2));foura3=qs(qp(ca,3),4)
        j=qs(qm(foura3,qi(qa(foura3,qs(cb2,27)))),1728)
        assert j==expected
        assert qa(qa(qp(j,2),qs(j,-153542016)),(F(-1790957481984),F(0)))==(0,0)
    print('EXACT VÉLU CURVE IDENTITY AND BOTH CM36 j VALUES PASS; all arithmetic rational')


if __name__=='__main__':main()
