#!/usr/bin/env python3
"""Rational bounds for the inverted tail, the increased cap lift, and the full-space transport."""
import argparse
from fractions import Fraction as F
from math import factorial
import hashlib
import json
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def S(x):return x**5*(126+x*(-420+x*(540+x*(-315+70*x))))
def up(x):
    d=10**16
    return F(-((-x.numerator*d)//x.denominator),d)
def run(a):
    assert sha(a.prefix_proof)=='cdf47a7f031f879f1d80bd8b1c6eb03a674abd8effd14801e53f94e6416ead4b'
    old=json.loads(a.prefix_proof.read_text())['exactBounds']
    Z,eta,R=F('.415'),F('.115'),F('.097')
    A0=F(.8746432018013935);top=F('.875')
    ae=F(float.fromhex('0x1.68493d1d794f0p+0'));be=F(float.fromhex('0x1.f31079949d8dep-2'))
    Y=be+F(old['horizontalDisplacementUpper']);V=F(13,128)+F(old['meridianLength'])
    A=F('.85');wid=F('.28');n=512
    h=F(0)
    for i in range(1,n+1):
        x=A*S(F(i,n))
        h+=wid/n*up(sum((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(7)))
    kap=315*A/(128*F('.24'))
    # Geometry exact with the old Z taken as the stored dyadic or its nominal .51.
    ds=F(.51)-Z
    dsMax=max(ds,F('.095'))
    assert dsMax<F('.095001')
    rise=F(15,8)/F('.29')
    theta=top/2
    cosBound=1-top**2/2;tanBound=theta/(1-theta**2/2)
    activeCoefficient=cosBound-tanBound*top
    timeSlope=1-rise*dsMax
    determinant=cosBound*timeSlope
    q=top*S(F('.165')/F('.46'))
    prefixInverseCEnd=F('.34')+F('.165')*(1-q*q/2)
    prefixH=F('.165')*q
    throatMin=F('.30')-R*(1+2*F('.01'))-eta/4
    out=dict(raisedTailHeightAboveCuff=h,curvatureUpper=kap,heightSpare=eta-h,
             outerCutHorizontalRadiusLower=F('.52')+F('.24')*(1-A*A/2),
             wholeRaisedTailAbovePrefix=Z-V,tailHeldSquared=(ae-F('.8'))**2+Z**2,
             tallThroatMinimumRadiusLower=throatMin,
             wholeThroatRadiusSquaredUpper=F('.32')**2+(Z+eta+2*R+F('.01')*R*F(22,7))**2,
             unchangedConvexCapTrueOldZ=Z+eta-F('.02'),
             shellVerticalMarginToConvexCap=eta+2*R+2*F('.01')*R-h,
             inverseCEndLower=prefixInverseCEnd,actualPrefixYUpper=Y,
             actualPrefixNeutralHeightUpper=V+prefixH,
             horizontalSlopeLower=cosBound,tanOldHalfUpper=tanBound,
             activeHeightCoefficientLower=activeCoefficient,radialTimeSlopeLower=timeSlope,
             globalSpaceJacobianLower=determinant)
    assert h<F('.109')<eta and kap<F('8.72') and throatMin>R
    assert Z-V>2*R and out['tailHeldSquared']>F('.64')**2
    assert out['shellVerticalMarginToConvexCap']>2*R and out['wholeThroatRadiusSquaredUpper']<F('1.6')**2
    assert out['outerCutHorizontalRadiusLower']>F('.32')+2*R
    assert prefixInverseCEnd>Y and V+prefixH<F('.21')
    assert A<A0<top and activeCoefficient>0 and timeSlope>F('.385') and determinant>F('.237')
    schema=dict(schema='R267-gap092-true-raised-disk-tall-throat-ambient-diffeomorphism-v1',
       prefixProofSHA256=sha(a.prefix_proof),sourceSHA256=sha(__file__),closedAngleCells=n,
       bounds={k:str(v) for k,v in out.items()})
    with a.output.open('x') as f:json.dump(schema,f,indent=2);f.write('\n')
    for key,v in out.items():print(key,float(v))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--prefix-proof',required=True,type=Path);p.add_argument('--output',required=True,type=Path);run(p.parse_args())
