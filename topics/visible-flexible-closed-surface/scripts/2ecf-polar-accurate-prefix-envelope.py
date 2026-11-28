#!/usr/bin/env python3
"""Exact rational R233/R232 prefix ruler, visibility, normal tilt and focal bounds."""
import argparse,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def scalar(npz,key):return Q.from_float(float(npz[key]))
def frac(x):return str(x.numerator)+'/'+str(x.denominator)


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for k in ('ramp','coast','output'):ap.add_argument('--'+k,required=True,type=Path)
    a=ap.parse_args()
    if sha(a.ramp)!='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7' or sha(a.coast)!='f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d':
        raise ValueError('Physical R233/R232 masters required')
    r=np.load(a.ramp);coast=np.load(a.coast)
    A,B,c,length=[scalar(r,k) for k in ('centralA','centralB','centralLength','ramp')]
    ell=scalar(coast,'length');epsilon=Q('0.0000006100')
    k1=Q('9.867915');k2=Q('8.892834503');R=Q('.097')
    # sqrt(1+e) <= 1+e/2.
    ramp_path=length*(1+epsilon/2);h=ramp_path+ell
    phi=k1*ramp_path+k2*ell
    cos_lower=1-phi**2/2+phi**4/24-phi**6/720
    assert phi<Q('.771') and cos_lower>Q('.717')
    outer=Q('1.538')
    assert (outer-h)**2 > A*A+c*c and outer>h
    width=B+h;held=A-B-h;height=c+h
    focal_gap=1-R*max(k1,k2,A/(B*B))
    assert width<Q('.484') and held>Q('.96999') and height<Q('.181563') and focal_gap>Q('.0428')
    vals=dict(A=A,B=B,c=c,rampLength=length,coastLength=ell,rampPathUpper=ramp_path,
              entireMeridionalPathUpper=h,halfWidthUpper=width,heldLower=held,heightUpper=height,
              ballRadiusUpper=outer,normalAngleUpper=phi,verticalTangentProjectionLower=cos_lower,
              focalDifferentialMinSingularLower=focal_gap)
    with a.output.open('x') as out:
        json.dump(dict(schema='certified-accurate-R233-R232-prefix-envelope-v1',
                       exactRationalBounds={k:frac(v) for k,v in vals.items()},
                       rampSHA256=sha(a.ramp),coastSHA256=sha(a.coast),
                       literalFloatingSourceNotCertified=True,nonlocalReachNotCertified=True),out,indent=2)
        out.write('\n')
    print(json.dumps({k:float(v) for k,v in vals.items()}))
