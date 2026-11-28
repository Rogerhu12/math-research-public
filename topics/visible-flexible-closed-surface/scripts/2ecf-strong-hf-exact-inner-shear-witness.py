#!/usr/bin/env python3
"""Outward dyadic first-jet Gram for the true doubly clocked interior HF+W+XYZ field."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import math
import numpy as np


BITS=160
SCALE=1<<BITS


class I:
    __slots__=("l","h")
    def __init__(self,l,h):
        if l>h:raise ArithmeticError("Invalid closed dyadic interval")
        self.l,self.h=int(l),int(h)
    def __add__(a,b):
        b=num(b)
        return I(a.l+b.l,a.h+b.h)
    __radd__=__add__
    def __neg__(a):return I(-a.h,-a.l)
    def __sub__(a,b):return a+(-num(b))
    def __rsub__(a,b):return num(b)+(-a)
    def __mul__(a,b):
        b=num(b)
        v=[x*y for x in (a.l,a.h) for y in (b.l,b.h)]
        return I(min(v)//SCALE,-(-max(v)//SCALE))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=num(b)
        if b.l<=0<=b.h:raise ZeroDivisionError
        v=[(x*SCALE,y) for x in (a.l,a.h) for y in (b.l,b.h)]
        return I(min(x//y for x,y in v),max(-(-x//y) for x,y in v))
    def __rtruediv__(a,b):return num(b)/a
    def __pow__(a,n):
        if n<0:return num(1)/(a**(-n))
        ans=num(1)
        for _ in range(n):ans=ans*a
        return ans
    def bounds(a):return [str(Q(a.l,SCALE)),str(Q(a.h,SCALE))]


def num(v):
    if isinstance(v,I):return v
    q=Q(float(v)) if isinstance(v,(float,np.floating)) else Q(v)
    n=q.numerator*SCALE;d=q.denominator
    return I(n//d,-(-n//d))


def trig(x):
    y=x;doubles=0
    while max(abs(y.l),abs(y.h))*8>SCALE:y=y/2;doubles+=1
    yy=-y*y
    cosine=num(0);sinc=num(0)
    for k in range(16,-1,-1):
        cosine=cosine*yy+num(Q(1,math.factorial(2*k)))
        sinc=sinc*yy+num(Q(1,math.factorial(2*k+1)))
    if Q(1,8)**33/math.factorial(33)>Q(1,SCALE):raise ArithmeticError("Taylor remainder budget")
    co=cosine+I(-1,1);si=sinc*y+I(-1,1)
    for _ in range(doubles):co,si=co*co-si*si,2*co*si
    return co,si


def harmonic(angle,count):
    co,si=trig(angle);seq=[(num(1),num(0))]
    for j in range(count):
        a,b=seq[-1];seq.append((a*co-b*si,b*co+a*si))
    return seq


def span(T,x):
    indices=[i for i in range(len(T)-1) if T[i].h<x.l and x.h<T[i+1].l]
    if len(indices)!=1:raise ArithmeticError("A single strict actual span is required")
    return indices[0]


def basis(T,x):
    k=span(T,x);prev={k:num(1)}
    for p in range(1,6):
        curr={};der={}
        for i in range(k-p,k+1):
            denom=T[i+p]-T[i]
            left=prev.get(i,num(0))/denom if denom.l>0 else num(0)
            denom=T[i+p+1]-T[i+1]
            right=prev.get(i+1,num(0))/denom if denom.l>0 else num(0)
            curr[i]=(x-T[i])*left+(T[i+p+1]-x)*right
            der[i]=p*(left-right)
        prev=curr
    return [(i-3,v,der[i]) for i,v in curr.items() if 3<=i<len(T)-9]


def realwave(modes,ang,coeff,knots,x,sine):
    B=basis(knots,x);waves=harmonic(ang,max(modes));val=num(0);vx=num(0);vu=num(0)
    for i,b,db in B:
        a=num(0);au=num(0)
        for j,k in enumerate(modes):
            co,si=waves[k];w=si if sine else co;wu=k*(co if sine else -si)
            c=num(coeff[i,j]);a+=c*w;au+=c*wu
        val+=b*a;vx+=db*a;vu+=b*au
    return val,vx,vu


def xyz_spline(knots,z,x,u):
    m=(z.shape[1]//3-1)//2;w=harmonic(u,m);B=basis(knots,x)
    Dx=[num(0) for _ in range(3)];Du=Dx.copy()
    for i,b,db in B:
        for k in range(3):
            co=z[i,k*(2*m+1):(k+1)*(2*m+1)]
            v=num(co[0]);vu=num(0)
            for j in range(1,m+1):
                c,s=w[j];a,bb=num(co[2*j-1]),num(co[2*j])
                v+=a*c+bb*s;vu+=j*(-a*s+bb*c)
            Dx[k]+=db*v;Du[k]+=b*vu
    return Dx,Du


HERM=[[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,Q(1,2),Q(-3,2),Q(3,2),Q(-1,2)],
      [0,0,0,10,-15,6],[0,0,0,-4,7,-3],[0,0,0,Q(1,2),-1,Q(1,2)]]


def hffield(T,C,x,u,W,z):
    k=span(T,x)
    if k<1 or k>=len(T)-2:raise ArithmeticError("Actual strict interior Hermite cell required")
    h=T[k+1]-T[k];t=(x-T[k])/h
    trigwave=harmonic(u,C.shape[2]-1)
    dx,du=xyz_spline(W,z,x,u)
    for j in range(6):
        p=HERM[j]
        val=sum(num(p[n])*t**n for n in range(6))*h**(j%3)
        der=sum(n*num(p[n])*t**(n-1) for n in range(1,6))*h**(j%3-1)
        for dim in range(3):
            v=num(0);vu=num(0)
            for m,Z in enumerate(C[k+int(j>=3),j%3,:,dim]):
                c,s=trigwave[m];a,bb=num(Z.real),num(Z.imag)
                v+=a*c-bb*s;vu+=m*(-a*s-bb*c)
            dx[dim]+=der*v;du[dim]+=val*vu
    return dx,du,k


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def exact_knots(x):return [num(a) for a in x]


def main(args):
    ctx=json.loads(args.warp.read_text())
    orig=json.loads(args.angular_clock.read_text())
    diag=json.loads(args.diagonal.read_text())
    if (ctx["target"]!=sha(args.diagonal) or ctx["baseField"]!=sha(args.field)
        or ctx["baseAngleClock"]!=sha(args.angular_clock) or orig["fieldSHA256"]!=sha(args.field)):
        raise ValueError("Complete HF, both carrier clocks and target identity required")
    npz=np.load(args.field)
    T=exact_knots(npz["knots"]);W=exact_knots(npz["Wknots"])
    src=npz["coefficients"];z=npz["physicalW"]
    f=Q(ctx["actualG10Trials"][ctx["chosen"]]["factor"])
    coeff=lambda tag:np.array([Q(float.fromhex(s))*f for s in ctx[tag]],dtype=object).reshape(-1,5)
    p,q=coeff("pCoefficientHex"),coeff("qCoefficientHex")
    B=exact_knots(ctx["radialKnots"]);B0=exact_knots(orig["radialKnots"])
    if B[0].bounds()!=T[0].bounds() or B[-1].bounds()!=T[-1].bounds():raise ValueError("Physical warp domain mismatch")
    own=None
    if args.position:
        prior=json.loads(args.position.read_text())
        if prior["model"]["warp"]!=sha(args.warp) or prior["model"]["actualMetric"]!=ctx["fixedMetric"]:
            raise ValueError("Actual Cartesian state belongs to a different material description")
        own=np.array(prior.get("totalCoefficients",prior["coefficients"])).reshape(z.shape)
        knots=exact_knots(diag["definition"]["basis"]["physicalKnots"])
    x,u=num(Q(args.x)),num(Q(args.u))
    P,Px,Pu=realwave(ctx["pFrequencies"],u,p,B,x,False)
    Qw,Qx,Qu=realwave(ctx["qFrequencies"],u,q,B,x,True)
    y=x+P;v=u+Qw
    h,hx,hu=realwave(orig["frequencies"],v,np.asarray(orig["coefficients"]).reshape(-1,len(orig["frequencies"])),B0,y,False)
    xi=y+h
    xx=(1+hx)*(1+Px)+hu*Qx;xu=(1+hx)*Pu+hu*(1+Qu)
    vx=Qx;vu=1+Qu
    U,V,index=hffield(T,src,xi,v,W,z)
    xs=[a*xx+b*vx for a,b in zip(U,V)]
    us=[a*xu+b*vu for a,b in zip(U,V)]
    if own is not None:
        Xextra,Uextra=xyz_spline(knots,own,x,u)
        xs=[a+b for a,b in zip(xs,Xextra)]
        us=[a+b for a,b in zip(us,Uextra)]
    E=sum(a*a for a in xs);G=sum(a*a for a in us);F=sum(a*b for a,b in zip(xs,us))
    if min(E.l,G.l)<=0 or not (F.h<0 or F.l>0):raise ArithmeticError("Missing strict shear")
    fab=min(abs(F.l),abs(F.h))
    lower=Q(fab*fab,E.h*G.h);e=Q(args.floor)
    if lower<=e*e:raise ArithmeticError(("Requested lower bound fails",float(lower)**.5,args.floor))
    out=dict(schema="exact-interior-HF-warp-first-jet-diagonal-normalized-shear-v1",entry=sha(__file__),
        field=sha(args.field),angularClock=sha(args.angular_clock),warp=sha(args.warp),diagonal=sha(args.diagonal),
        position=sha(args.position) if own is not None else None,x=args.x,u=args.u,bits=BITS,
        physicalCommonTargetArbitraryPositiveDiagonal=True,innerCell=index,curveLabels=[y.bounds(),v.bounds(),xi.bounds()],
        E=E.bounds(),F=F.bounds(),G=G.bounds(),strictRationalSquaredShearLower=str(lower),
        strictRationalMetricLower=str(e),numericalShearForDisplay=float(lower)**.5)
    with args.output.open("x") as fp:json.dump(out,fp,indent=2);fp.write("\n")
    print(json.dumps(dict(SHA=sha(args.output),floor=str(e),sampleDisplay=float(lower)**.5,cell=index)))


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for k in ("field","angular-clock","warp","diagonal","output"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--position",type=Path)
    for k in ("x","u","floor"):ap.add_argument("--"+k,required=True)
    main(ap.parse_args())
