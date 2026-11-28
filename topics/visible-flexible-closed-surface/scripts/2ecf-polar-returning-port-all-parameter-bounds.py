#!/usr/bin/env python3
"""Rational reach and independent endpoint controls for the complete returning port rectangle."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main(args):
    c,L,P,E=Q(13,25),Q(7,25),Q(12,25),Q(1,5)
    z=Q(83,200)
    target=Q(97,1000)
    ib=1024*Q(math.factorial(5)**2,math.factorial(11))
    S9p=Q(315,128)
    Bp=Q(20,3)*Q(8,9)**4
    bound=(P*Bp+E*S9p)/L
    low=-L*E/2
    high=L*(P*ib+E/2)
    slope_floor=1-(P+E)**2/2
    max_diff=P+2*E
    min_r=c+L*slope_floor
    held2=(Q(7,5)-Q(4,5))**2+(z+low)**2
    # Entire parameter rectangle, including terminal angles of both signs.
    assert 0<bound<Q(19,2)<1/target and max_diff<1
    assert z+low-Q(181563,1000000)>2*target
    assert high<Q(23,200) and c-Q(32,100)>2*target
    assert min_r-Q(32,100)>2*target
    assert held2>Q(16,25)**2
    assert Q(4,5)**2+(z+high)**2<Q(8,5)**2
    height_p=L*ib*slope_floor
    jac=height_p*slope_floor
    assert jac>Q(3,50)
    result=dict(sourceSHA256=sha(__file__),portFamilySHA256=sha(args.port),integralB=str(ib),maxAbsoluteBPrime=str(Bp),maxS9Prime=str(S9p),maxNormalCurvature=str(bound),angleDiameterUpper=str(max_diff),cosineLower=str(slope_floor),minimumH=str(low),maximumH=str(high),minimumOuterMaterialEdgeRadius=str(min_r),prefixTailVerticalGap=str(z+low-Q(181563,1000000)),heldSquaredLower=str(held2),tipHeightDerivativeInPeakLower=str(height_p),absoluteTwoControlJacobianLower=str(jac),minimumThreeComponentReach=str(target),newConnectionContinuumChecked=False)
    with args.output.open('x') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps(result))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    main(p.parse_args())
