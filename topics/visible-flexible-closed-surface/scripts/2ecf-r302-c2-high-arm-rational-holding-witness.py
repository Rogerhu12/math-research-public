#!/usr/bin/env python3
"""Exact plane support witness for the C2 high-arm holding frame, independent of the closing surface sampling."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

def run(args):
    charts=json.loads(args.ports.read_text())
    assert Q(charts['low']['offset'])<Q(5862,10**6)
    assert Q(charts['high']['offset'])<Q(65942,10**6)
    r=Q(23,200);a=Q(233,1000);u=Q(1,20)
    bLo,bHi=map(Q,charts['tubeBounds'])
    assert r<bLo<bHi<Q(118,1000)
    dbhi=a-bLo;tiphi=r+2*(bHi-r)
    A0,A1=Q(627,1000),Q(634,1000)
    B0,B1=Q(1234,1000),Q(1242,1000)
    k0,k1=Q(173,100),Q(433,250)
    c0,c1=B0-1/k0,B1-1/k1
    dlo=r+Q(24,100)+(Q(78,100)+Q(85,100)+r)*(1-Q(3,10)**2/2)
    dhi=dbhi+Q(24,100)+Q(78,100)+Q(85,100)+tiphi
    tangentNeg=Q(3,10)*(Q(78,100)+Q(85,100)+tiphi)
    # In the common rotated-back plane at eta=1/2, v=-1/4, so
    # (X,Y)=C0-C1+Rot(-1/20)*(5+hflat+D,T), with -tangentNeg<=T<=0.
    xlo=A0-5+(5-Q(5862,10**6)+dlo)*(1-u*u/2)-tangentNeg*u
    ylo=-c1-(5+dhi)*u-tangentNeg
    al,ah=k0/2,k1/2
    sinlo=al-ah**3/6
    coslo=1-ah*ah/2
    coshi=1-al*al/2+ah**4/24
    gxlo=2*coslo+3*sinlo
    gylo,gyhi=3*coslo-2*ah,3*coshi-2*sinlo
    assert xlo>0 and ylo<0 and gxlo>0 and gylo>0
    witness=3*c0+gxlo*xlo+gyhi*ylo
    rootNorm=Q(3606,1000);assert rootNorm**2>13
    # zero-phase low outward arm turns toward negative material tangent
    g0=2+3*u
    lowbase=2*(A1-5)+5*g0
    lowmax=lowbase+max(dbhi*g0+a*rootNorm,dhi*g0+bHi*rootNorm)
    ba,bh=k0/4,k1/4
    g1=3-2*(ba-bh**3/6)
    highbase=3*c1+g1/k0
    highlen=dbhi+Q(24,100)+Q(43,100)+Q(35,100)+tiphi
    highmax=highbase+max(dbhi*g1+a*rootNorm,highlen*g1+bHi*rootNorm)
    mother=(Q(14,10)+Q(66,1000))*rootNorm
    gap=witness-max(mother,lowmax,highmax)
    assert gap/rootNorm>Q(94,100)
    assert Q(78,100)>Q(1,5)*Q(23,6) and r/Q(23,6)==Q(3,100)
    out=dict(schema="true-C2-high-arm-holding-support-and-height-witness",scriptSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),portsSHA256=hashlib.sha256(args.ports.read_bytes()).hexdigest(),
             initialHalfPhase=True,holding="entire high rigid arm",witness="true tip of the low bent arm at eta=1/2",
             normal=[2,3,0],witnessLinearLower=str(witness),zeroPhaseUpper=list(map(str,(mother,lowmax,highmax))),
             centralEuclideanLower=str(gap/rootNorm),conditionalFullHeld="at least .78 if every remaining material point has |z|>=.78",
             diameterForThreePercentAtR115="23/6")
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")
    print(float(gap/rootNorm))

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--ports",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    run(p.parse_args())
