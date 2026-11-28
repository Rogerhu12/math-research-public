#!/usr/bin/env python3
"""Exact rational constants for all ordered secants of the accurate R233/R232 annulus."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    source = json.loads(args.exit_ring.read_text())
    identity = {"schema":"actual-R233-R232-complete-exit-anisotropic-ray-graph-v1",
                "allRowsSHA256":"ea4c715a8f25007bd49674bbcaafd5eb3bc60627c3069112825b29e0d1782a4c",
                "rampSHA256":"0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7",
                "coastSHA256":"f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d",
                "cells":1024,"integerBits":96}
    if any(source[key] != value for key,value in identity.items()):
        raise ValueError("The entire certified R257 boundary is required")
    if sha(args.ramp) != source["rampSHA256"] or sha(args.coast) != source["coastSHA256"]:
        raise ValueError("Geometric source mismatch")
    with np.load(args.ramp) as data:
        A,B,r = [F.from_float(float(data[k])) for k in ("centralA","centralB","ramp")]
    with np.load(args.coast) as data:
        l,v = [F.from_float(float(data[k])) for k in ("length","v")]
    eps = F("6.100e-7")
    K = F("9.867915")
    h = r*(1+eps/2)+l
    height = F(source["exactLower"]["aboveCentral"])
    loss = h-height
    dz = F(".00126")
    dxy = F(".0142")
    point = F(".0143")
    ambient = F(".203")
    chord = ambient+2*dxy
    t = F(".294")
    M = (A*A-B*B)/B
    arc_ratio = (1+M*t*t/(6*B))/(1-t*t/6)
    warp_ratio = 1+v*(r/2+l)/B
    path_ratio = (1+eps/2)*warp_ratio*arc_ratio
    path = path_ratio*(ambient+2*point)
    bounds = dict(curvatureRadius=1/K,meridianLength=h,exitMinimumHeightAboveCylinder=height,
                  verticalSlack=loss,verticalPositionError=dz,horizontalPositionError=dxy,
                  totalPositionError=point,ellipseChord=chord,halfAngle=t,
                  ellipseSpeedSecondDerivativeUpper=M,ellipseArcToChordRatio=arc_ratio,
                  warpToCentralRatio=warp_ratio,materialPathScale=path_ratio,
                  nearPairIntrinsicDistance=path)
    conditions = dict(centralCurvature=K-A/B**2,coastCurvature=K-F("8.892834503"),
        positiveHeightSlack=loss,heightSlack=dz-loss-eps*r,
        horizontalCone=dxy*dxy-2*h*loss,
        spatialCone=point*point-dz*dz-dxy*dxy,nearDistance=ambient-2/K,
        halfAngle=t-t**3/6-chord/(2*B),arcRatio=F("1.195")-arc_ratio,
        warpRatio=F("1.006")-warp_ratio,pathScale=F("1.203")-path_ratio,
        intrinsicPath=F(".279")-path,shortGeodesic=3-K*path,
        reach=1/K-F(".1013"))
    if min(conditions.values())<=0:
        raise ArithmeticError({k:str(v) for k,v in conditions.items() if v<=0})
    output=dict(schema="R233-R232-whole-accurate-annulus-secant-rational-budget-v1",
                exactBounds={k:str(v) for k,v in bounds.items()},
                strictMargins={k:str(v) for k,v in conditions.items()},
                inputHashes={"ramp":sha(args.ramp),"coast":sha(args.coast),
                             "exitRing":sha(args.exit_ring),"rowStream":source["allRowsSHA256"]},
                entrySHA256=sha(__file__))
    with args.output.open("x") as stream:
        json.dump(output,stream,indent=2)
        stream.write("\n")
    print(json.dumps({k:float(v) for k,v in bounds.items()}))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    for arg in ("ramp","coast","exit-ring","output"):
        parser.add_argument("--"+arg,required=True,type=Path)
    run(parser.parse_args())
