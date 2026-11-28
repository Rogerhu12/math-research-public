#!/usr/bin/env python3
"""Continuous projected physical polar ray, with rigorous attainable speed against every warp target."""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from fractions import Fraction as F
from pathlib import Path

for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[name]="1"
import numpy as np


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m);return m


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def endpoint_func(c,x,f):
    return c.hull(f(c.lower_i(x)),f(c.upper_i(x)))


def log_i(c,x):
    def point(x):
        z=(x-1)/(x+1);p=z;tot=z
        if z.absupper()*10>=c.SCALE*6:raise ValueError("log series radius exceeded")
        for k in range(1,60):
            p=p*z.square();tot+=p/(2*k+1)
        error=F(2)*F(3,5)**121/(121*(1-F(3,5)**2))
        return 2*tot+c.I(-error,error)
    return endpoint_func(c,x,point)


def exp_i(c,x):
    def point(x):
        if x.absupper()>3*c.SCALE:raise ValueError("exp Taylor budget exceeded")
        tot=p=c.I(1)
        for k in range(1,49):
            p=p*x/k;tot+=p
        err=F(27*3**49,math.factorial(49))
        return tot+c.I(-err,err)
    return endpoint_func(c,x,point)


def bern(c,coeff,t):
    t=c.I(t); n=len(coeff)-1
    return sum((y*math.comb(n,i)*t**i*(1-t)**(n-i) for i,y in enumerate(coeff)),c.I(0))


def main():
    ap=argparse.ArgumentParser()
    for name in ("scripts","ramp","coast","output"):
        ap.add_argument("--"+name,type=Path,required=True)
    args=ap.parse_args();Ipath=args.scripts/"6a65-m12-r137-continuous-domain.py"
    Fpath=args.scripts/"6a65-geometry-final-ramp-port-certificate.py"
    Ppath=Path(__file__).with_name("2ecf-strong-accurate-polar-port-budgets.py")
    c=load(Ipath,"ray_int");g=load(Fpath,"ray_series");p=load(Ppath,"ray_ports")
    if sha(args.coast)!=g.COAST_SHA or sha(args.ramp)!=g.RAMP_SHA:raise ValueError("Original Γ95 masters required")
    I=c.I
    with np.load(args.coast) as z:
        co,si=g.real_curve(z["curve_modes"],z["curve_coefficients"])
        length,v=[I(F(float(z[key]))) for key in ("length","v")]
    arc=I(g.ARC_LO,g.ARC_HI);scale=I(1-F("2.453e-17"),1+F("2.453e-17"))
    curve=g.Fourier(co,si,c,8);J=g.Series(c)
    # Choose the true left ray by Γ95 inlet native η=π/2 at the true exit.
    # Fourier modes at this phase have exact integer sines/cosines.
    def phase(k,n):
        return [(I(a),I(b)) for a,b in ((0,1),(1,0),(0,-1),(-1,0))][k%4]
    vjets=curve.point(0,2,phase,order=6)
    port=p.left_port(c,J,curve.series(vjets,6),arc,arc*scale,scale,v,length,[I(y) for y in co[0]])
    x,y=port["P"][:2];cs2=x.square()/(x.square()+y.square())
    sin8=(y.square()/(x.square()+y.square()))**4
    sin8=I.raw(max(0,sin8.lo),min(c.SCALE,sin8.hi))
    if y.lo<=0:raise ArithmeticError("Physical ray did not select upper pole")
    fixed=p.RightPort(c,512)
    # For the matching right R205 ray |cos(uR)| = (rho_R/r)|cos(theta)|.
    # Projection contracts planar distances around the origin, so rho_R<=r.
    maxCos=c.upper_i(cs2.sqrt())
    cu=I.raw(0,maxCos.hi);su=(1-cu.square()).sqrt()
    L0=F(.7956739498716915);b=F(.1815625);S=F(float(b)+float(L0))
    L=I(min(S-b,L0),max(S-b,L0))
    left=p.budgets(port,L,"left")
    right=p.budgets(fixed.port(su,cu),L,"right")
    def Qcontrols(d,sign):
        r=d["radius"];q=log_i(c,r);v=d["fixedRadiusSpeed"]/r
        a=d["fixedRadiusAcceleration"]/r-v.square()
        return [q,q+sign*L*v/5,q+sign*2*L*v/5+L.square()*a/20]
    poly=Qcontrols(left,1)+Qcontrols(right,-1)[::-1]
    deriv=[(b-a)*5/L for a,b in zip(poly,poly[1:])]
    def rs(t):
        return exp_i(c,bern(c,poly,t))*bern(c,deriv,t)
    eps=I(F(.15));n=31
    M=32*(right["z"]-left["z"])/L-sum(d[k] for d in (left,right) for k in ("height0","height1"))
    weights=[1/(eps.square()+rs(F(j,n)).square()) for j in range(2,n-1)]
    total=sum(weights,I(0))
    free=[M*((1-sin8)/(n-3)+sin8*w/total) for w in weights]
    terms=[left["height0"],left["height1"]]+free+[right["height1"],right["height0"]]
    probes=[]
    for j in range(1,64):
        t=F(j,64)
        r_s=rs(t);z_s=bern(c,terms,t)
        probes.append((r_s.square()+z_s.square(),t,r_s,z_s))
    best=min(probes,key=lambda item:item[0].hi)
    # The witness t is an exact rational and its value uses the actual
    # normalized weights for the same one physical polar ray.
    speed,t,rs_,zs=best
    floor=1-speed
    B=F(2,10**9)
    change=(1-I(B)).sqrt()-speed.sqrt()
    def split(ctrl):
        rows=[list(ctrl)]
        while len(rows[-1])>1:
            q=rows[-1]
            rows.append([(a+b)/2 for a,b in zip(q,q[1:])])
        return [q[0] for q in rows],[q[-1] for q in reversed(rows)]
    pairs=[(poly,deriv)]
    for unused in range(8):
        nxt=[]
        for q,dq in pairs:
            ql,qr=split(q);dl,dr=split(dq)
            nxt.extend(((ql,dl),(qr,dr)))
        pairs=nxt
    variation=I(0)
    for q,dq in pairs:
        qhi=I.raw(max(x.hi for x in q),max(x.hi for x in q))
        ap=I.raw(max(x.absupper() for x in dq),max(x.absupper() for x in dq))
        variation+=exp_i(c,qhi)*ap*L/len(pairs)
    rise=right["z"]-left["z"]
    ray_length_upper=c.upper_i(variation+rise)
    allheight_floor=1-(ray_length_upper/L).square()
    required_variation=L*(1-I(B)).sqrt()-rise
    out=dict(schema="accurate-original-weighted-polar-physical-ray-metric-lower-v1",
        sources={k.name:sha(k) for k in (Ipath,Fpath,Ppath,Path(__file__))},
        rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),nativeLeftPhase="pi/2",t=str(t),
        physicalS=(I(b)+L*t).display(),physicalCosSquared=cs2.display(),
        prescribedWindowMaterialTangent="partial_s-(Theta_s/Theta_u) partial_u",
        fullProjectedRadialSpeedSquared=speed.display(),fixedPolarRho_s=rs_.display(),
        fixedPolarZ_s=zs.display(),requiredRelativeMetricErrorLower=str(floor.lower()),
        requiredCorrectionAlongSameMaterialVectorAtB=change.display(),
        intervalDiagnosticFamilies={side:{k:q.display() for k,q in d.items()} for side,d in (("left",left),("right",right))},
        rayPanels=len(pairs),radialTotalVariationUpper=str(variation.upper()),heightGain=rise.display(),
        wholeRayLengthUpperForEveryMonotoneHeight=str(ray_length_upper.upper()),
        allPositiveHeightAllocationsAndClocksMetricLower=str(allheight_floor.lower()),
        necessaryProjectedRadiusVariationAtB=required_variation.display(),
        necessaryAdditionalProjectedRadiusVariationAtB=(required_variation-variation).display(),
        freeMass=M.display(),completeWeightDenominator=total.display(),
        coefficientDirections="28 positive weights, common denominator, original sin^8 lateral mix")
    with args.output.open("x") as fp:json.dump(out,fp,indent=2);fp.write("\n")
    print("t",t,"s",out["physicalS"]["display"],"rho_s",rs_.display()["display"],
          "z_s",zs.display()["display"],"speed2",speed.display()["display"],"floor",float(floor.lower()),
          "correction",change.display()["display"])
    print("TV <=",float(variation.upper()),"dz",rise.display()["display"],"length <=",float(ray_length_upper.upper()),
          "all-height floor",float(allheight_floor.lower()),"additional TV",float((required_variation-variation).lower()))
    if floor.lower()<=0:raise ArithmeticError("The source ray did not certify a positive metric lower")


if __name__=="__main__":
    main()
