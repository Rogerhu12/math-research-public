#!/usr/bin/env python3
"""Rational full-domain projected-speed and area bounds from accurate Γ95/R205 ports."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--budgets",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    data=json.loads(args.budgets.read_text())
    if data["schema"]!="actual-accurate-Gamma95-and-R205-whole-polar-control-budgets-v1":
        raise ValueError("Full physical polar endpoint budget required")
    def rng(which,key):
        v=data["exactHull"][which][key]
        return F(v["lo"]),F(v["hi"])
    L=max(map(F,(data["L"]["lo"],data["L"]["hi"])))
    Lmin=F(data["L"]["lo"])
    # Includes both accurate ports. The lower and upper log bounds follow from
    # e>1+1+1/2 and e^(1/2)>1+1/2. No numerical logarithms are used.
    side_controls=[]
    for side in ("left","right"):
        rlo,rhi=rng(side,"radius")
        if not (rlo>F(2,5) and rhi<F(3,2)):raise ValueError("Log enclosure failed")
        rslo,rshi=rng(side,"fixedRadiusSpeed")
        rsslo,rsshi=rng(side,"fixedRadiusAcceleration")
        q1=max(abs(rslo),abs(rshi))/rlo
        q2=max(abs(rsslo),abs(rsshi))/rlo+q1*q1
        side_controls.append((q1,q2))
    q1=max(c[0] for c in side_controls);q2=max(c[1] for c in side_controls)
    extension=2*L*q1/5+L*L*q2/20
    # Quintic control positions are log(r)+j L q_s/5 (+L² q_ss/20 at j=2).
    q_abs=1+extension
    if q_abs>=3:raise ValueError("Requested compact global exponent bound not available")
    # e<3 since 1/k! <= 1/(2^(k-1)) for k>=2 (strict for k>=3).
    rmin=F(1,27);rmax=F(27)
    deriv=5*(F(3,2)+2*extension)/Lmin
    rsmax=rmax*deriv
    eps=F(.15)
    mass=F(data["freeControlMass"]["lo"])
    bmin=mass*eps**2/(28*(eps**2+rsmax**2))
    if bmin<=0:raise ValueError("Free mass must be strictly positive")
    vl=min(rng("left","height0")[0],rng("left","height1")[0],bmin)
    # At the right endpoint the last derivative control is q_s=r_s/r<0.
    qright=rng("right","fixedRadiusSpeed")[1]/rng("right","radius")[1]
    T=F(999,1000)
    qnear=qright*T**4+deriv*(1-T**4)
    if qnear>=0:raise ValueError("Right angular-uniform radial-speed cone did not close")
    zout=vl*(1-T**30*(31-30*T))
    wmin=min(zout,rmin*(-qnear))
    dmin=F(data["minimumClockControl"])
    area=dmin*rmin*wmin
    assert area>0
    tmp=dict(radialInterpolantAbsoluteLogUpper=q_abs,fullRadiusLower=rmin,
        fullRadiusUpper=rmax,absLogRadialDerivativeUpper=deriv,absRadialDerivativeUpper=rsmax,
        positiveInteriorCommonControlLower=bmin,nearRightThreshold=T,rightLogDerivativeUpper=qnear,
        leftAndMiddleHeightSpeedLower=zout,fullProjectedRadialPlaneSpeedLower=wmin,
        fullAreaElementLower=area,clockDerivativeLower=dmin)
    out=dict(schema="accurate-original-weighted-polar-full-continuous-area-v1",
        budgetsSHA256=sha(args.budgets),sourceSHA256=sha(__file__),
        fractions={k:str(q) for k,q in tmp.items()},display={k:float(q) for k,q in tmp.items()})
    with args.output.open("x") as fp:json.dump(out,fp,indent=2);fp.write("\n")
    print(json.dumps(out["display"]))


if __name__=="__main__":
    main()
