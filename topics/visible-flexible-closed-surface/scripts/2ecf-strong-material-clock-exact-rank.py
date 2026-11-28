#!/usr/bin/env python3
"""Exact dyadic clock length, positive speed and nonzero G10 spline minor over F_p."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import qr

P=2147483647

def rat(x):
    return Q.from_float(float(x))

def mod(x):
    return (x.numerator%P)*pow(x.denominator%P,-1,P)%P

def basis_mod(x,T):
    # Base interval membership is tested over the rationals. Subsequent
    # de Boor arithmetic is reduced modulo the prime after each operation.
    vals=[int(a<=x<b) for a,b in zip(T,T[1:])]
    for d in range(1,6):
        out=[]
        for j in range(len(vals)-1):
            a=T[j+d]-T[j]
            b=T[j+d+1]-T[j+1]
            u=0 if a==0 else mod((x-T[j])/a)*vals[j]
            v=0 if b==0 else mod((T[j+d+1]-x)/b)*vals[j+1]
            out.append((u+v)%P)
        vals=out
    return vals[3:-3]

def determinant(A):
    A=[list(row) for row in A]
    det=1
    n=len(A)
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]%P),None)
        if pivot is None:return 0
        if pivot!=j:
            A[pivot],A[j]=A[j],A[pivot]
            det=-det
        d=A[j][j]%P
        det=det*d%P
        inv=pow(d,-1,P)
        for i in range(j+1,n):
            fac=A[i][j]*inv%P
            for k in range(j+1,n):A[i][k]=(A[i][k]-fac*A[j][k])%P
    return det%P

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main(args):
    raw=json.loads(args.clock.read_text())["definition"]
    src=json.loads(args.prepared.read_text())
    if sha(args.prepared)!=raw["parentPreparedSHA256"]:raise ValueError("Clock and G10 must agree")
    coeff=[rat(float.fromhex(c)) for c in raw["gammaHex"]]
    T=list(map(rat,raw["chartBasis"]["physicalKnots"]))
    lo,hi=T[0],T[-1]
    delta=sum((c*(T[i+9]-T[i+3])/6 for i,c in enumerate(coeff)),Q())
    assert len(coeff)==45 and len(T)==57 and Q(".00599999999999")<delta<Q(".00600000000001")
    nodes=src["caches"]["training"]["nodes"]
    weights=src["caches"]["training"]["weights"]["metric"]
    interior=[i for i,x in enumerate(nodes) if lo<rat(x)<hi and weights[i]>0]
    spline=BSpline(list(map(float,T)),np.eye(len(T)-6),5)
    selected=qr(spline([nodes[i] for i in interior])[:,3:-3].T,mode="economic",pivoting=True)[2][:45]
    picks=sorted(interior[i] for i in selected)
    A=[basis_mod(rat(nodes[i]),T) for i in picks]
    det=determinant(A)
    if not det:raise ValueError("Requested rational determinant witness vanished")
    # Integer primality sanity: a composite would require a factor <=sqrt(P).
    if any(P%k==0 for k in range(2,int(P**.5)+1)):raise ArithmeticError("Prime required")
    out=dict(schema="exact-physical-clock-length-and-finite-observation-rank-v1",entrySHA256=sha(__file__),
        clockSHA256=sha(args.clock),preparedSHA256=sha(args.prepared),exactDelta=str(delta),deltaApprox=float(delta),
        exactCut=str(hi+delta),exactCuff=str(rat(src["definition"]["completeHalfDomain"][1])+delta),
        speedLowerExact=str(1+min([Q(0)]+coeff)),speedUpperExact=str(1+max([Q(0)]+coeff)),
        activeRadialColumns=len(coeff),prime=P,orderedZeroBasedG10Rows=picks,
        selectedRadialsHex=[float(nodes[i]).hex() for i in picks],rationalMinorModPrime=det,
        exactRankProof="The reduced rational collocation determinant is nonzero modulo the displayed prime.",
        twoJetPorts="Retained open-knot basis has three omitted modes at each endpoint; v=1,v_x=v_xx=0.",
        wholeDomainMetricOrReachClaim=False)
    with args.output.open("x") as f:
        json.dump(out,f,separators=(",",":"))
        f.write("\n")
    print(json.dumps(dict(SHA256=sha(args.output),rank=len(coeff),det=det,exactDelta=str(delta))),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for name in ("clock","prepared","output"):
        ap.add_argument("--"+name,type=Path,required=True)
    main(ap.parse_args())
