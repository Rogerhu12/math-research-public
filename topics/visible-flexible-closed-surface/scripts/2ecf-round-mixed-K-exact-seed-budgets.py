#!/usr/bin/env python3
"""Rational constants for the exact mixed-curvature doubly-ended round reference."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);a=p.parse_args()
lo=Q(333,106);hi=Q(355,113);eps=Q(7,200);Z=Q(.51);ell=Q(2,5);cut=Q(4,5);K=Q(737,100)
# 2.23 < sqrt(5), sqrt(2)<99/70, 1/sqrt(2)<5/7.
assert Q(223,100)**2<5 and Q(99,70)**2>2 and 2*Q(5,7)**2>1
Bprime=Q(192,25)/Q(223,100)
bumpPhasePrime=135*hi/256+4*eps*Bprime
maxPhasePrime=max(bumpPhasePrime,15*hi/16)
assert maxPhasePrime/ell<K and Q(1)/cut<K
point=3375*hi/65536-4*eps*Q(27,8)
assert point<-Q(31,100)
# The t=1/16 base phase is between 0 and .036; the bump is at most eps.
t=Q(1,16);p0=hi/2*t**3*(10-15*t+6*t*t)
cosPoint=1-(p0+eps)**2/2;negK=point*cosPoint/(ell*(cut+ell))
cmin=Z-ell*Q(5,7);zmax=Z+ell*eps/4
coneCos=(1-eps**2/2-eps)/Q(99,70)
assert negK<-Q(3,5) and 2*cmin>2/K and coneCos>Q(2,3) and 3<lo
assert zmax<Z+Q(1,50) and cut>Q(514,1000) and 1/K>Q(97,1000)
assert (cut+ell)**2+zmax**2<Q(8,5)**2
out=dict(schema='R275-exact-round-reference-with-negative-gaussian-curvature-and-full-kernel-reach-v1',
    entrySHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),turnLength=str(ell),cuffHeight=str(Z),cutRadius=str(cut),
    phaseDerivativeUpper=str(maxPhasePrime),turnPrincipalCurvatureAbsUpper=str(maxPhasePrime/ell),
    gaussianAtOneSixteenthStrictUpper=str(negK),halfCentralCylinderLengthLower=str(cmin),heightUpper=str(zmax),
    containingMeridianConeHalfAngleCosineLower=str(coneCos),kernelReachLower=str(1/K),graftedReachLower='97/1000',
    graftedDiameterUpper='16/5',graftedReachOverDiameterLower='97/3200',
    roundTurnBumpAmplitude=str(eps),fullEndTwoJetsMatch=True,accurateRotationalIsometry=True,nontrivialPhaseAtZero=False)
with a.output.open('x') as h:json.dump(out,h,indent=2);h.write('\n')
print(out)
