#!/usr/bin/env python3
"""Exact all-angle determinant lower bound for the two simultaneous material clocks in normalized coordinates."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(a):
    q=json.loads(a.clock.read_text());s=q['spans'];m=q['modes'];x=list(map(Q,q['clockCoefficients']));kn=[Q(0)]*6+[Q(i/s) for i in range(1,s)]+[Q(1)]*6;rows=len(kn)-6
    bound=[]
    for component in (0,1):
        n=m+1-component;co=[[Q(0)]*n for j in range(rows)]
        for j in range(3,rows-3):co[j]=x[:n];del x[:n]
        u=max(sum(abs(v)*2*(k+component) for k,v in enumerate(r)) for r in co)
        t=max(sum(abs(co[i][k]-co[i-1][k]) for k in range(n))*5/(kn[i+5]-kn[i]) for i in range(1,rows))
        bound.append([t,u])
    assert not x
    (ht,hu),(kt,ku)=bound;D=(1-ht)*(1-ku)-hu*kt;assert ht<1 and ku<1 and D>0
    out=dict(entrySHA256=sha(Path(__file__)),clockSHA256=sha(a.clock),spatialSHA256=q['spatialSHA256'],entireMaterialCoordinateDerivativeAbsUpper=[[str(v) for v in row] for row in bound],strictPositiveTwoClockDeterminantLower=str(D),everyPhaseSameClosedSpatialImage=True,endpointIdenticalTwoJets=True)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(float(D))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--clock',type=Path,required=True);p.add_argument('--output',type=Path,required=True);run(p.parse_args())
