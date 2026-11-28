#!/usr/bin/env python3
"""Exact strict radial normal curvature and full two-coordinate warp orientation for HF64+W."""
import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s)
    sys.modules[n]=m;s.loader.exec_module(m);return m


ev=load(Path(__file__).with_name("2ecf-strong-hf-exact-inner-shear-witness.py"),"dyadic_HF_derivatives")
zero=ev.num(0)


def curvature(T,coef,W,z,x,u):
    vx,vu,k=ev.hffield(T,coef,x,u,W,z)
    h=T[k+1]-T[k];t=(x-T[k])/h
    tr=ev.harmonic(u,coef.shape[2]-1)
    dd=[zero for _ in range(3)]
    for j in range(6):
        scale=sum(n*(n-1)*ev.num(ev.HERM[j][n])*t**(n-2) for n in range(2,6))*h**(j%3-2)
        for a in range(3):
            val=zero
            for m,b in enumerate(coef[k+int(j>=3),j%3,:,a]):
                co,si=tr[m];val+=co*ev.num(b.real)-si*ev.num(b.imag)
            dd[a]+=scale*val
    # Twice differentiate the actual cardinal recurrence on this one strict
    # original W span. All three clamped controls at each endpoint are zero.
    ix=ev.span(W,x);vals={ix:ev.num(1)};ders={ix:zero};seconds={}
    for degree in range(1,6):
        d0={};d1={};d2={}
        for i in range(ix-degree,ix+1):
            dl=W[i+degree]-W[i];dr=W[i+degree+1]-W[i+1]
            l=vals.get(i,zero)/dl if dl.l>0 else zero
            r=vals.get(i+1,zero)/dr if dr.l>0 else zero
            ld=ders.get(i,zero)/dl if dl.l>0 else zero
            rd=ders.get(i+1,zero)/dr if dr.l>0 else zero
            d0[i]=(x-W[i])*l+(W[i+degree+1]-x)*r
            d1[i]=degree*(l-r)
            d2[i]=degree*(ld-rd)
        vals,ders,seconds=d0,d1,d2
    M=(z.shape[1]//3-1)//2
    for i,q in seconds.items():
        if not 3<=i<len(W)-9:continue
        for dim in range(3):
            A=z[i-3,dim*(2*M+1):(dim+1)*(2*M+1)];v=ev.num(A[0])
            for m in range(1,M+1):
                co,si=tr[m];v+=co*ev.num(A[2*m-1])+si*ev.num(A[2*m])
            dd[dim]+=q*v
    cr=[vx[(i+1)%3]*vu[(i+2)%3]-vx[(i+2)%3]*vu[(i+1)%3] for i in range(3)]
    dot=lambda a,b:sum(y*z for y,z in zip(a,b))
    g=dot(vx,vx);w2=dot(cr,cr);vol=dot(dd,cr)
    if min(g.l,w2.l)<=0 or vol.l<=0<=vol.h:raise ArithmeticError("Nondegenerate curvature witness required")
    num=min(abs(vol.l),abs(vol.h))
    lower=Q(num*num*ev.SCALE,w2.h*g.h*g.h)
    return dict(cell=k,Wspan=ix,xs=[q.bounds() for q in vx],xu=[q.bounds() for q in vu],
        xss=[q.bounds() for q in dd],metricE=g.bounds(),WnormSquared=w2.bounds(),
        determinantSecondNormal=vol.bounds(),squaredNormalCurvatureLower=str(lower)),lower


def bounds(knots,modes,coeff):
    n=len(modes);rad=len(knots)-6
    if len(coeff)!=(rad-6)*n or len(knots)<12:raise ValueError("Complete clamped coefficients required")
    zeros=[Q(0)]*n
    A=[zeros]*3+[coeff[i:i+n] for i in range(0,len(coeff),n)]+[zeros]*3
    D=[[(5*(b-a))/(knots[i+6]-knots[i+1]) for a,b in zip(A[i],A[i+1])] for i in range(rad-1)]
    return max(sum(abs(v) for v in row) for row in D),max(sum(abs(v)*m for v,m in zip(row,modes)) for row in A)


def main(args):
    warp=json.loads(args.warp.read_text());old=json.loads(args.angular_clock.read_text())
    diag=json.loads(args.diagonal.read_text());td=diag["definition"]
    actual=ev.sha(args.field)
    if (actual!=warp["baseField"] or actual!=old["fieldSHA256"] or actual!=td["basePositionFile"]
        or warp["baseAngleClock"]!=ev.sha(args.angular_clock) or warp["target"]!=ev.sha(args.diagonal)
        or td["baseAngleClock"]!=ev.sha(args.angular_clock) or warp["fixedMetric"]!=diag["definitionSHA256"]):
        raise ValueError("All original exact numerical field and clock identities required")
    f=Q(warp["actualG10Trials"][warp["chosen"]]["factor"])
    T=list(map(Q,warp["radialKnots"]))
    pc=[Q(float.fromhex(v))*f for v in warp["pCoefficientHex"]]
    qc=[Q(float.fromhex(v))*f for v in warp["qCoefficientHex"]]
    px,pu=bounds(T,warp["pFrequencies"],pc);qx,qu=bounds(T,warp["qFrequencies"],qc)
    ow,_=bounds(list(map(Q,old["radialKnots"])),old["frequencies"],list(map(Q,old["coefficients"])))
    jac=(1-px)*(1-qu)-pu*qx
    levels=[min([Q(0)]+[Q(float.fromhex(v)) for v in td[tag]])+1 for tag in ("CEradialHex","CGangularHex")]
    if (ow>=1 or max(px,qu)>=1 or jac<=Q("0.68245") or min(levels)<=0):
        raise ArithmeticError("Exact entire-annulus diffeomorphism test failed")
    with np.load(args.field) as a:
        witness,val=curvature(ev.exact_knots(a["knots"]),a["coefficients"],ev.exact_knots(a["Wknots"]),
            a["physicalW"],ev.num(Q(args.x)),ev.num(Q(args.u)))
    floor=Q(args.kappa)
    if val<=floor**2:raise ArithmeticError(("Strict actual curvature lower bound fails",float(val)**.5))
    out=dict(schema="actual-HF-plus-all-W-interior-strict-curvature-ceiling-and-new-metric-warp-orientation-v1",
        entry=ev.sha(__file__),arithmetic=ev.sha(ev.__file__),field=actual,angularClock=ev.sha(args.angular_clock),
        warp=ev.sha(args.warp),diagonal=ev.sha(args.diagonal),trueDomainPoint=[args.x,args.u],bits=ev.BITS,
        oldClockDerivativeLower=str(1-ow),totalClockSquaredSpeedLower=str(levels[0]),
        angularRadiusSquaredRatioLower=str(levels[1]),fullWarpBounds=list(map(str,(px,pu,qx,qu))),
        entireWarpDetLower=str(jac),actualStrictCurvatureLower=str(floor),reachStrictUpper=str(1/floor),
        completeSourceDiameterAtLeast="14/5",normalizedReachStrictUpper=str(Q(5,14)/floor),witness=witness)
    with args.output.open("x") as fp:json.dump(out,fp,indent=2);fp.write("\n")
    print(json.dumps(dict(SHA=ev.sha(args.output),kLowerDisplay=float(val)**.5,JacLowerDisplay=float(jac),
        strictReachCeiling=float(1/floor),strictNormalizedCeiling=float(Q(5,14)/floor))))


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for n in ("field","angular-clock","warp","diagonal","output"):ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--x",default="17/80");ap.add_argument("--u",default="11/10")
    ap.add_argument("--kappa",default="602/25")
    main(ap.parse_args())
