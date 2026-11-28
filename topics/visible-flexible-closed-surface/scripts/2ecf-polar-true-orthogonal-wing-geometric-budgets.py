#!/usr/bin/env python3
"""Exact disjoint-support and physical inter-wing separation for the independent long/short-axis port."""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(a):
    S=Q(4,5);cx=Q(7,10);cy=Q(14,25);A=Q(35,100);B=Q(85,100);Z=Q(83,200);R=Q(97,1000)
    assert cx**2+cy**2>S**2
    # Passive coordinate bounds on the opposite material wing, rounded upward.
    px=Q(572,1000);py=Q(388,1000)
    assert px**2>S**2-cy**2 and py**2>S**2-cx**2
    D2=(cx-px)**2+(cy-py)**2
    assert D2>Q(214,1000)**2 and Q(214,1000)>2*R
    k=max(A/(S-cx),B/(S-cy))*Q(315,128)
    assert k<Q(19,2)
    Hx=(S-cx)*A/2;Hy=(S-cy)*B/2
    assert Z-Hx-Q(181563,1000000)>2*R and Hy<Q(108901,1000000) and min(cx,cy)-Q(32,100)>2*R
    min_edge=S-max((S-cx)*A*A/2,(S-cy)*B*B/2)
    assert min_edge>Q(713,1000)
    cosx=1-A*A/2;cosy=1-B*B/2
    jac=cosx*cosy
    assert jac>Q(599,1000)
    prev=json.loads(a.chords.read_text());old=Q(prev['upperBoundOnAllMaterialChords']);L=Q(prev['actualConnectorLength'])
    new=old+(S-cx)*A*A/2;mean=(new/L+Q(3,256))/(1-Q(3,256))
    assert new<Q(713612,10**6) and mean**2<Q(7,8)
    out=dict(entrySHA256=sha(__file__),portSHA256=sha(a.port),oldChordSHA256=sha(a.chords),squaredPhysicalUnlikeWingSeparationLower=str(D2),maxAbsolutePrincipalCurvature=str(k),heightRange=[str(Z-Hx),str(Z+Hy)],newOuterEdgePhysicalRadiusLower=str(min_edge),tipVerticalVelocitiesAbsoluteJacobianLower=str(jac),tipHeightsJacobianLower=str((S-cx)*(S-cy)*jac/4),sameMaterialAllChordNewUpper=str(new),stationaryMeanUpper=str(mean),threePieceFullReachLower=str(R),fullExistingCapsAndBothJets=True)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(float(D2),float(k),float(jac),float(new))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('port','chords','output'):p.add_argument('--'+k,type=Path,required=True)
    run(p.parse_args())
