#!/usr/bin/env python3
"""Uniform true-port seams, all compact point bounds, projections and H for two explicit spatial maps."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
    A=Q.from_float(float.fromhex('0x1.68493d1d794f0p+0'));eta=Q(1,100)
    R=Q(65,100);ball=Q(8,5)
    sqrt2hi=Q(141422,100000);assert sqrt2hi**2>2
    threshold=A-R*sqrt2hi
    assert threshold>Q(488,1000)
    assert (A+Q(112,10000))**2+Q(1,10**8)<(Q(148,100)-Q(35,1000))**2
    assert Q(1,2)<Q(885,1000)-Q(65,1000) and Q(4,5)<Q(895,1000)-Q(83,1000)
    assert Q(4,5)<Q(885,1000)-Q(65,1000)
    assert Q(18078,100000)>Q(135,1000)
    # True four-jet port (through exact P,Ps,Pss and their angular derivatives).
    # Both plane guards lie strictly outside their active cutoff, even at epsilon=.07.
    assert Q(501,1000)**2>Q(1,2)**2+eta**2 and Q(801,1000)**2>Q(4,5)**2+eta**2
    assert Q(501,1000)-Q(18078,100000)-threshold<-Q(7,100)
    assert Q(801,1000)-Q(387,1000)-threshold<-Q(7,100)
    assert Q(18175,100000)<Q(415,1000)-Q(2,1000)
    assert Q(523901,10**6)<Q(528,1000)-Q(2,1000)
    assert Q(673,1000)-Q(1,10000)>Q(54,100)
    assert Q(886,1000)**2>Q(885,1000)**2+eta**2
    assert Q(886,1000)-threshold < Q(415,1000)-Q(2,1000)
    assert Q(83999,100000)>R+Q(7,100)
    assert (A-Q(4,5))**2+Q(387,1000)**2>(R+Q(7,100))**2
    assert Q(523901,10**6)<Q(60,100)-Q(5,100)
    assert (A-Q(895,1000))**2+Q(55,100)**2>R**2
    assert A-(R+Q(7,100))>0 and Q(895,1000)**2+(R+Q(7,100))**2<Q(148,100)**2
    assert Q(148,100)**2+Q(60,100)**2<ball**2
    assert (Q(14,10)-Q(10561,10000))**2+Q(614,1000)**2>R**2
    width=Q(895,1000);sphereSupport=Q(10559,10000);delta=sphereSupport-width
    assert delta==Q(1609,10000) and delta/(2*ball)>Q(5,100) and R/(2*ball)>Q(2,10)
    out=dict(proofScriptSHA256=sha(__file__),planeSourceSHA256=sha(a.plane),sphereSourceSHA256=sha(a.sphere),materialAnchor=str(A),rectangles=['R273','R282'],thresholdLower=str(threshold),newCompactSetsDiameterUpper=str(2*ball),newCompactSetsHeldLower=str(R),newCompactSetsEuclideanQuotientLower=str(delta),newHeldOverDiameterLower=str(R/(2*ball)),newEuclideanOverDiameterLower=str(delta/(2*ball)),oppositeConnectorSeparationLower='1/5',allTruePortsAndWholeCapsPreserved=True,wholeEmbeddingProved=False,wholeReachProved=False)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(R/(2*ball),delta/(2*ball))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('plane','sphere','output'):p.add_argument('--'+k,required=True,type=Path)
    main(p.parse_args())
