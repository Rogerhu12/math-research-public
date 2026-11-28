#!/usr/bin/env python3
"""True point lower bounds for three same-g raw Hermite physical refinements."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

import numpy as np


H2=((2,0,0,-20,30,-12),(0,2,0,-12,16,-6),(0,0,1,-3,3,-1),
    (0,0,0,20,-30,12),(0,0,0,-8,14,-6),(0,0,0,1,-2,1))


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def weights(t,L,order):
    return [sum(Q(a,2)*Q(math.factorial(j),math.factorial(j-order))*t**(j-order)
                for j,a in enumerate(row) if j>=order)*L**(p%3-order)
            for p,row in enumerate(H2)]


def exact_native_port(raw,station,quarter,ks,A,B,c):
    if station==0:
        co=(1,0,-1,0)[quarter]
        sn=(0,1,0,-1)[quarter]
        return [[A*co,B*sn,c],[Q(0),Q(0),Q(1)],[Q(0)]*3]
    result=[]
    for port in range(3):
        row=[]
        for d in range(3):
            answer=Q(0)
            for k,z in zip(ks,raw[station,:,port,d]):
                q=(quarter*int(k))%4
                x=(z.real,-z.imag,-z.real,z.imag)[q]
                answer+=Q(float(x))
            row.append(answer)
        result.append(row)
    return result


def witness(path):
    with np.load(path,allow_pickle=False) as a:
        co=a['coefficients'];ks=a['wave'].astype(int);sx=a['sx']
        c,A,B=map(lambda key:Q(float(a[key])),('centralLength','centralA','centralB'))
    best=None
    alphas=np.arange(1,128)/128
    wpoly=np.array([[sum(row[j]*j/2*t**(j-1) for j in range(1,6))
                      for row in H2] for t in alphas])
    # Screen finite candidate points only. The proof recomputes the selected one
    # from the original binary64 master and the exact axis phases (+/-1,+/-i).
    for q in range(4):
        phase=np.array([1.,1j,-1.,-1j])[(q*ks)%4]
        ports=np.einsum('k,nkij->nij',phase,co).real
        ports[0]=np.array([[float(A)*(1,0,-1,0)[q],float(B)*(0,1,0,-1)[q],float(c)],[0,0,1],[0,0,0]])
        for j in range(len(sx)-2):
            L=sx[j+1]-sx[j]
            w=wpoly*np.tile([1/L,1,L],2)
            S=w@np.concatenate([ports[j],ports[j+1]],axis=0)
            E=(S*S).sum(axis=-1)-1
            g=int(np.argmax(abs(E)))
            entry=(abs(E[g]),j,g+1,q)
            if best is None or entry>best:
                best=entry
    unused,j,num,q=best
    t=Q(num,128)
    sx0,sx1=Q(float(sx[j])),Q(float(sx[j+1]))
    L=sx1-sx0
    jets=(exact_native_port(co,j,q,ks,A,B,c)+exact_native_port(co,j+1,q,ks,A,B,c))
    w=weights(t,L,1)
    S=[sum(z[d]*v for z,v in zip(jets,w)) for d in range(3)]
    E=sum(v*v for v in S)-1
    return dict(nodes=len(sx),masterSHA256=sha(path),cell=j,localT=str(t),nativeThetaQuarterTurns=q,
                physicalS=str(c+sx0+t*L),radialVectorExact=list(map(str,S)),radialGramDefectExact=str(E),
                relativeMetricLower=str(abs(E)),display=float(abs(E)),finalNonpolynomialCellNotUsed=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('old','refinement','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    r=json.loads(a.refinement.read_text())
    assert sha(a.old)==r['originalRampSHA256']=='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7'
    rows=[witness(a.old)]
    for n in (33,65):
        path=a.refinement.parent/r['outputs'][str(n)]['file']
        assert sha(path)==r['outputs'][str(n)]['SHA256']
        rows.append(witness(path))
    with a.out.open('x') as f:
        json.dump(dict(schema='strong-same-g-raw-H17-H33-H65-actual-point-lower-bounds-v1',
            entrySHA256=sha(Path(__file__)),refinementSHA256=sha(a.refinement),rows=rows),f,indent=2)
        f.write('\n')
    print(json.dumps([{k:x[k] for k in ('nodes','cell','localT','nativeThetaQuarterTurns','display')}
                      for x in rows]))


if __name__=='__main__':
    main()
