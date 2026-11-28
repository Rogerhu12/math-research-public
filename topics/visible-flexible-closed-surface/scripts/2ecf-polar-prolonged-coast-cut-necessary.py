#!/usr/bin/env python3
"""Single exact material meridian certificate excluding long affine coast prolongations."""
import argparse
import hashlib
import importlib.util
import json
import os
from fractions import Fraction as Q
from pathlib import Path

for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(args):
    certpath=args.scripts/"6a65-m12-r137-continuous-domain.py"
    portpath=args.scripts/"6a65-geometry-final-ramp-port-certificate.py"
    c=module(certpath,"cuen_int")
    port=module(portpath,"cuen_fourier")
    if sha(args.coast)!=port.COAST_SHA or sha(args.ramp)!=port.RAMP_SHA:
        raise ValueError("Original accurate Gamma95 geometry required")
    I=c.I
    with np.load(args.ramp) as src:
        central,ramplen=[I(Q.from_float(float(src[k]))) for k in ("centralLength","ramp")]
    with np.load(args.coast) as data:
        co,si=port.real_curve(data["curve_modes"],data["curve_coefficients"])
        v=I(Q.from_float(float(data["v"])))
    four=port.Fourier(co,si,c,6)
    arc=I(port.ARC_LO,port.ARC_HI)
    scale=I(1-Q("2.453e-17"),1+Q("2.453e-17"));f0=scale*arc;r0=f0/v
    # All native Fourier derivatives at exactly theta=0: cos=1 and sin=0.
    vals=[]
    for order in range(5):
        vals.append([I(co[0][j] if order==0 else 0)+sum((a for _,a,_ in four.terms[order][j]),I(0)) for j in range(3)])
    gamma,p,q=vals[:3]
    center=[I(x) for x in co[0]]
    length=I(Q(args.length))
    geo=c.geometry(vals,arc,f0,v,length,center)
    k=geo["ratio"];K=geo["Tu"]
    energy=c.norm2(p);speed=energy.sqrt()
    cross=c.cross(p,q);crossnorm=c.norm2(cross).sqrt()
    T=c.scale(1/speed,p)
    NF=c.scale(speed/crossnorm,c.sub(q,c.scale(c.dot(p,q)/energy,p)))
    BF=c.scale(1/crossnorm,cross)
    d=c.add(c.scale(-v/K,NF),c.scale((1-(v/K).square()).sqrt(),BF))
    delta=length*(2*r0+length)
    w=delta/(r0+(r0.square()+(1+k.square())*delta).sqrt())
    P=c.add(c.add(center,c.scale(scale,c.sub(gamma,center))),c.scale(w,c.sub(d,c.scale(k,T))))
    radial=c.scale(1/(r0+length),c.sub(c.scale(r0+w,d),c.scale(k*w,T)))
    U=c.upper_i(I.raw(0,(w*k/(v*(r0+w))).absupper()))
    smax=I(Q(".977237"))
    targetXupper=I(Q(".800001"));targetZlower=I(Q(".509999"))
    a,b=I(Q(24,25)),I(Q(7,25))
    displacement=a*(P[0]-targetXupper)+b*(targetZlower-P[2])
    initialDot=-a*radial[0]+b*radial[2]
    finalDotUpper=a
    angle0,angle1=I(Q("1.29")),I(Q(".28"))
    sn0,cs0=c.sincos(angle0);sn1,cs1=c.sincos(angle1)
    R=I(Q(".097"))
    # An upper bound on the DELAY before the fixed cut is all we have.
    # If L < R*(alpha+beta), using both disjoint losses would be invalid.
    # In that case L < .153 already contradicts displacement>.69.
    delay=smax-central-ramplen-length
    loss=R*(angle0-sn0+angle1-sn1)
    margins=dict(centralMaterialIsInsideFlatTarget=I(Q(".34"))-targetXupper*U,
        initialAngle=cs0-initialDot,finalAngle=cs1-finalDotUpper,
        disjointAngleIntervalsFromDisplacement=displacement-R*(angle0+angle1),
        forbiddenMeridianTime=displacement+loss-delay)
    quantities=dict(rulingRatio=k,materialAngleAbsUpper=U,exitX=P[0],exitZ=P[2],radialX=radial[0],radialZ=radial[2],
        initialDot=initialDot,cutDirectionProjectionLower=displacement,
        endpointTurningLossLower=loss,requiredLengthLower=displacement+loss,availableLengthUpper=delay)
    out=dict(schema="actual-prolonged-affine-coast-R205-flat-cut-exclusion-v1",length=args.length,
        fullGeometry={"coast":sha(args.coast),"ramp":sha(args.ramp),"entry":sha(__file__),"integer":sha(certpath),"fourier":sha(portpath)},
        exact={k:[str(v.lower()),str(v.upper())] for k,v in quantities.items()},
        margins={k:str(v.lower()) for k,v in margins.items()},
        allStrict=all(v.lo>0 for v in margins.values()))
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")
    print(json.dumps({k:[float(v.lower()),float(v.upper())] for k,v in quantities.items()}))
    print(json.dumps({k:float(v.lower()) for k,v in margins.items()}))
    if not out["allStrict"]:
        raise ArithmeticError("This cut exclusion did not close")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for name in ("scripts","coast","ramp","output"):
        parser.add_argument("--"+name,required=True,type=Path)
    parser.add_argument("--length",required=True)
    run(parser.parse_args())
