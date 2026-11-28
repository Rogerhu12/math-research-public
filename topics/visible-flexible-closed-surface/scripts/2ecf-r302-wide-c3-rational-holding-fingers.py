#!/usr/bin/env python3
"""Exact rational support and bilateral thick-arm budgets for the C3 wide-cap candidate."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import factorial, floor, ceil
from pathlib import Path

BINARY=2**58


def enclose(a,b=None):
    b=a if b is None else b
    return Q(floor(a*BINARY),BINARY), Q(ceil(b*BINARY),BINARY)


def iv(x):
    return x if isinstance(x,tuple) else (Q(x),Q(x))


def add(a,b):
    a,b=iv(a),iv(b)
    return enclose(a[0]+b[0],a[1]+b[1])


def neg(a):
    a=iv(a)
    return -a[1],-a[0]


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    a,b=iv(a),iv(b)
    products=[x*y for x in a for y in b]
    return enclose(min(products),max(products))


def absmax(a):
    return max(abs(a[0]),abs(a[1]))


def trig_point(x,cosine):
    offset=0 if cosine else 1
    val=sum((-1)**k*x**(2*k+offset)/factorial(2*k+offset) for k in range(8))
    error=abs(x)**(16+offset)/factorial(16+offset)
    return enclose(val-error,val+error)


def trig(x):
    x=iv(x)
    assert max(map(abs,x))<=Q(3,2)
    s=(trig_point(x[0],False)[0],trig_point(x[1],False)[1])
    hi=1 if x[0]<=0<=x[1] else trig_point(min(abs(x[0]),abs(x[1])),True)[1]
    return (trig_point(absmax(x),True)[0],hi),s


def rotate(p,a):
    c,s=trig(a)
    return sub(mul(c,p[0]),mul(s,p[1])),add(mul(s,p[0]),mul(c,p[1]))


def turn(t,omega,short):
    if not short:
        return omega*t**3*(10-15*t+6*t*t)
    e=Q(1,20)
    if t<e:
        v=t/e
        z=e*v**3*(1-v/2)
    elif t<=1-e:
        z=t-e/2
    else:
        v=(1-t)/e
        z=1-e-e*v**3*(1-v/2)
    return omega*z/(1-e)


def body(omega,last,short,db,b,tip,fr,fp,n):
    length=Q(43,100) if short else Q(78,100)
    d,t=add(db,Q(24,100)),iv(0)
    # Each pair denotes axis displacement intervals from the true planar base.
    rows=[(iv(0),iv(0),Q(233,1000),iv(0)),((0,d[1]),iv(0),Q(233,1000),iv(0))]
    for i in range(n):
        lo=turn(Q(i,n),omega,short);hi=turn(Q(i+1,n),omega,short)
        beta=(min(lo,hi),max(lo,hi))
        co,si=trig(beta)
        dd,dt=mul(length/n,co),mul(length/n,si)
        rows.append((add(d,mul((0,1),dd)),add(t,mul((0,1),dt)),b[1],beta))
        d,t=add(d,dd),add(t,dt)
    co,si=trig(omega)
    span=add(last,tip)
    rows.append((add(d,mul((0,span[1]),co)),add(t,mul((0,span[1]),si)),b[1],iv(omega)))
    d,t=add(d,mul(span,co)),add(t,mul(span,si))
    maximum=None
    for xx,yy,rad,angle in rows:
        c,s=trig(angle)
        axis=add(mul(xx,fr),mul(yy,fp))
        trans=sub(mul(c,fp),mul(s,fr))
        bound=axis[1]+rad*absmax(trans)
        maximum=bound if maximum is None else max(maximum,bound)
    return d,t,maximum


def run(a):
    report=json.loads(a.ports.read_text())
    low=Q(report['low']['offset']);high=Q(report['high']['offset'])
    assert low<Q(5862,10**6) and high<Q(65942,10**6)
    r=Q(23,200);ra=Q(233,1000)
    b=tuple(map(Q,report['tubeBounds']))
    db=ra-b[1],ra-b[0]
    tip=r,r+2*(b[1]-r)
    k=(Q(173,100),Q(433,250))
    A=(Q(627,1000),Q(634,1000))
    B=(Q(1234,1000),Q(1242,1000))
    rc=(1/k[1],1/k[0])
    C0=sub(A,5);C1=sub(B,rc)
    k0=Q(1,5);v=Q(1,4)
    cs,ss=trig(k0*v)
    f0=add(mul(10,cs),mul(3,ss));g0=add(mul(-10,ss),mul(3,cs))
    cs,ss=trig(mul(k,v))
    f1=add(mul(-10,ss),mul(3,cs));g1=add(mul(-10,cs),mul(-3,ss))
    lowbase=add(mul(10,C0),mul(add(5,(-low,0)),f0))
    highbase=add(mul(3,C1),mul(add(rc,(-high,0)),f1))
    wd,wt,lowmax=body(Q(-135,100),Q(92,100),False,db,b,tip,f0,g0,a.bins)
    _,_,highmax=body(Q(-95,100),Q(74,100),True,db,b,tip,f1,g1,a.bins)
    # L_high,.5^{-1} of the compact-phase low tip, now compared with phase zero.
    pr=rotate((add(add(5,(-low,0)),wd),wt),-k0*v)
    qr=rotate((add(C0,pr[0]),sub(pr[1],C1)),mul(k,Q(1,2)))
    witness=add(mul(10,qr[0]),mul(3,add(qr[1],C1)))[0]
    rootNorm=Q(10441,1000)
    assert rootNorm**2>109
    upper=[(Q(14,10)+high)*rootNorm,lowbase[1]+lowmax,highbase[1]+highmax]
    gap=(witness-max(upper))/rootNorm
    assert gap>Q(9,10)
    lowLength=db[1]+Q(24,100)+Q(78,100)+Q(92,100)+tip[1]
    lowY=Q(1,4)+max(ra+db[1]/20,lowLength/20+b[1])
    highY=C1[0]+(rc[0]-high)*(1-(k[1]/4)**2/2)-max(ra*k[1]/4,b[1])
    assert highY-lowY>Q(51,100)
    spineLow=Q(78,100)/(Q(15,8)*Q(135,100))
    spineHigh=Q(43,100)*Q(19,20)/Q(95,100)
    assert min(spineLow,spineHigh)>b[1]+r and 2/(1-Q(675,1000)**2/2)<Q(314,100)
    assert Q(135,100)<Q(157,100) and Q(157,100)-k[1]/4-Q(95,100)>0
    grasp=(db[0]+Q(24,100)+Q(43,100)+Q(74,100)+tip[0])*(1-Q(475,1000)**2/2)
    assert grasp>Q(14,10)
    out=dict(schema='C3-wide-real-fingers-rational-all-angle-budget',
             entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             portsSHA256=hashlib.sha256(a.ports.read_bytes()).hexdigest(),bins=a.bins,
             strongCentralReach=str(r),spineCurvatureRadiiLower=list(map(str,(spineLow,spineHigh))),
             mutualArmSeparationLower=str(highY-lowY),wholeHighArmGraspDiameterLower=str(grasp),
             supportDirection=[10,3,0],lowTipHighFrameSupportLower=str(witness),
             entireExpandedCentralSupportUpper=list(map(str,upper)),centralHeldWitnessDistanceLower=str(gap),
             closedHeldCondition='remaining closure and caps have |z|>=.78, giving whole held>=.78')
    with a.output.open('x') as f:
        json.dump(out,f,indent=2)
        f.write('\n')
    print(float(gap),float(grasp))


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--ports',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--bins',type=int,default=128)
    run(p.parse_args())
