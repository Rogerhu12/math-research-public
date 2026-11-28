#!/usr/bin/env python3
"""Rational intrinsic-distance and strong envelope budgets for the prolonged exact affinely warped strip."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sqrt_up(x):
    den=1<<96
    k=isqrt(x.numerator*den*den//x.denominator)
    return F(k if k*k*x.denominator==x.numerator*den*den else k+1,den)


def run(args):
    source=json.loads(args.interval.read_text())
    if (source["schema"]!="actual-Gamma95-prolonged-accurate-affine-coasts-v1" or source["cells"]!=2048
            or source["integerBits"]!=96 or sha(args.ramp)!=source["rampSHA256"]
            or source["allRowsSHA256"]!=args.rows_sha):
        raise ValueError("All original extended-coast interval rows required")
    with np.load(args.ramp) as x:
        A,B,c,r,v=[F.from_float(float(x[k])) for k in ("centralA","centralB","centralLength","ramp","v")]
    K=F("9.867915");eps=F("6.100e-7")
    cases={}
    for length,radius in ((F(".07"),1/K),(F(".08"),F(".099"))):
        row=source["bounds"][str(length)]
        low={k:F(v) for k,v in row["exactLower"].items()}
        high={k:F(v) for k,v in row["exactUpper"].items()}
        h=r*(1+eps/2)+length
        loss=h-low["exitHeightAboveCentral"]
        dz=loss+eps*r
        horizontal=sqrt_up(2*h*loss)
        e=sqrt_up(horizontal**2+dz**2)
        d=2*radius+2*horizontal
        # Sufficient sin(half-angle)>d/(2B). Monotone lower Taylor bound
        # on [0,1] and exact bisection to avoid an inverse-trig assumption.
        lowang,hiang=F(0),F(1)
        if hiang-hiang**3/6<=d/(2*B):raise ArithmeticError("Angle bracket too narrow")
        for _ in range(40):
            mid=(lowang+hiang)/2
            if mid-mid**3/6>d/(2*B):hiang=mid
            else:lowang=mid
        ell_ratio=(1+(A*A-B*B)/B*hiang**2/(6*B))/(1-hiang**2/6)
        f_ratio=1+v*(r/2+length)/B
        distance=(1+eps/2)*f_ratio*ell_ratio*(2*radius+2*e)
        zmax=c+r+length+dz
        ball=sqrt_up((A+horizontal)**2+zmax**2)
        q=dict(radius=radius,meridian=h,verticalSlack=loss,verticalError=dz,horizontalError=horizontal,
            positionError=e,ellipseChord=d,halfAngle=hiang,ellipseRatio=ell_ratio,warpRatio=f_ratio,
            intrinsicDistance=distance,piMinusKDistanceLower=F("3.14159")-K*distance,
            halfWidth=B+horizontal,absoluteHeight=zmax,completePrefixBall=ball,
            excludedSupportDistance=A-B-horizontal)
        if not (loss>0 and high["allCoastPrincipalCurvature"]<K and low["allCoastD"]>0
                and low["allCoastMaterialAngleDerivative"]>0 and q["piMinusKDistanceLower"]>0
                and radius<=1/K and ball<F("1.59") and q["halfWidth"]<F(".885")
                and q["excludedSupportDistance"]>F(".65")):
            raise ArithmeticError("A continuous reach or envelope comparison did not close")
        cases[str(length)]={n:str(v) for n,v in q.items()}
        print(str(length),json.dumps({n:float(v) for n,v in q.items()}))
    out=dict(schema="R259-prolonged-affine-coast-all-pairs-budget-v1",cases=cases,
        intervalEntrySHA256=source["entrySHA256"],intervalReportSHA256=sha(args.interval),
        rowSHA256=args.rows_sha,entrySHA256=sha(__file__),rampSHA256=sha(args.ramp))
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    for k in ("ramp","interval","output"):p.add_argument("--"+k,required=True,type=Path)
    p.add_argument("--rows-sha",required=True)
    run(p.parse_args())
