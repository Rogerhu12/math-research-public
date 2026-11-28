#!/usr/bin/env python3
"""Exact rational two-point normal-ball obstruction on saved real full fields.

At u=pi/2 every stored integer Fourier mode has rational value and derivative.
All field coefficients, spline knots and correction coefficients are interpreted
as their exact stored binary64 values. No fitted or truncated surrogate is used.
"""
import argparse
from functools import lru_cache
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time
import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rational(x):
    return Q.from_float(float(x))


H = ((1,0,0,-10,15,-6),(0,1,0,-6,8,-3),
     (0,0,Q(1,2),Q(-3,2),Q(3,2),Q(-1,2)),
     (0,0,0,10,-15,6),(0,0,0,-4,7,-3),
     (0,0,0,Q(1,2),-1,Q(1,2)))


def horner(coeff, t, derivative=0):
    p=list(coeff)
    for _ in range(derivative):p=[k*p[k] for k in range(1,len(p))]
    v=Q(0)
    for a in p[::-1]:v=v*t+a
    return v


def trig4(k):
    return ((1,0),(0,1),(-1,0),(0,-1))[k%4]


def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]


def interval(x,scale=10**12):
    lo=x.numerator*scale//x.denominator
    return [str(Q(lo,scale)),str(Q(lo+1,scale))]


def packet(z,s,correction):
    knots=[rational(x) for x in z['knots']]
    cell=next(i for i in range(len(knots)-1) if knots[i]<=s<knots[i+1])
    assert 0<cell<len(knots)-2, 'This witness uses original stored interior traces only'
    h=knots[cell+1]-knots[cell];t=(s-knots[cell])/h
    coeff=z['coeff']
    traces=[]
    for index in (cell,cell+1):
        arr=[]
        for order in range(3):
            val=[];der=[]
            for xyz in range(3):
                total=Q(0);du=Q(0)
                for k in range(coeff.shape[2]):
                    c=coeff[index,order,k,xyz]
                    re,im=rational(c.real),rational(c.imag)
                    cs,sn=trig4(k)
                    total+=re*cs-im*sn
                    du+=-k*(re*sn+im*cs)
                val.append(total);der.append(du)
            arr.append((val,der))
        traces.extend(arr)
    factors=(1,h,h*h,1,h,h*h)
    weights=[[horner(H[i],t,d)*factors[i]/h**d for i in range(6)] for d in range(2)]
    P=[sum(weights[0][i]*traces[i][0][j] for i in range(6)) for j in range(3)]
    Ps=[sum(weights[1][i]*traces[i][0][j] for i in range(6)) for j in range(3)]
    Pu=[sum(weights[0][i]*traces[i][1][j] for i in range(6)) for j in range(3)]
    if correction is not None:
        b,T=map(rational,correction['physicalInterval']);L=T-b
        assert b<s<T
        ns=correction['spans'];m=correction['modes']
        sk=([Q(0)]*6+[rational(i/ns) for i in range(1,ns)]+[Q(1)]*6)
        x=(s-b)/L;n=len(sk)-6
        @lru_cache(None)
        def B(i,p):
            if p==0:return Q(int(sk[i]<=x<sk[i+1]))
            v=Q(0)
            if sk[i+p]!=sk[i]:v+=(x-sk[i])/(sk[i+p]-sk[i])*B(i,p-1)
            if sk[i+p+1]!=sk[i+1]:v+=(sk[i+p+1]-x)/(sk[i+p+1]-sk[i+1])*B(i+1,p-1)
            return v
        def D(i):
            a=Q(0) if sk[i+5]==sk[i] else 5*B(i,4)/(sk[i+5]-sk[i])
            b_=Q(0) if sk[i+6]==sk[i+1] else 5*B(i+1,4)/(sk[i+6]-sk[i+1])
            return (a-b_)/L
        co=np.asarray(correction['coefficients']).reshape(3,n-6,m+1)
        for xyz in range(3):
            for i in range(3,n-3):
                for mode in range(m+1):
                    k=2*mode+int(xyz<2)
                    # x,z use cos(k*u); y uses cos(k*u-pi/2)=sin(k*u).
                    cs,sn=trig4(k-int(xyz==1))
                    a=rational(co[xyz,i-3,mode])
                    P[xyz]+=a*B(i,5)*cs
                    Ps[xyz]+=a*D(i)*cs
                    Pu[xyz]+=-a*B(i,5)*k*sn
    return dict(P=P,Ps=Ps,Pu=Pu,cell=cell,cellEndpoints=[str(knots[cell]),str(knots[cell+1])])


def run(args):
    start=time.monotonic()
    saved=json.loads(args.state.read_text())
    assert saved['fieldSHA256']==sha(args.field)
    corr=None
    if args.correction:
        corr=json.loads(args.correction.read_text())
        assert corr['sourceFieldSHA256']==sha(args.field)
        assert corr['sourceStateSHA256']==sha(args.state)
        assert corr['targetSHA256']==saved['targetSHA256']
    z=np.load(args.field)
    p,q=packet(z,args.s1,corr),packet(z,args.s2,corr)
    d=[y-x for x,y in zip(p['P'],q['P'])];d2=dot(d,d)
    assert d2>0
    n=cross(p['Ps'],p['Pu']);n2=dot(n,n);nd=dot(n,d)
    assert n2>0 and nd!=0
    ratio2=d2*d2*n2/(4*nd*nd)
    margin=args.radius**2-ratio2
    assert margin>0,('Requested exact reach ceiling not achieved',float(ratio2))
    D=Q(14,5)
    assert args.radius/D<Q(3,100)
    output=dict(schema='exact-binary-field-two-point-normal-ball-reach-ceiling-v1',
        checkerSHA256=sha(__file__),fieldSHA256=sha(args.field),stateSHA256=sha(args.state),
        correctionSHA256=sha(args.correction) if args.correction else None,
        targetSHA256=saved['targetSHA256'],s1=str(args.s1),s2=str(args.s2),u='pi/2',
        firstCell=p['cell'],secondCell=q['cell'],firstCellEndpoints=p['cellEndpoints'],secondCellEndpoints=q['cellEndpoints'],
        exactPairPointsEnclosed=[[interval(x) for x in a['P']] for a in (p,q)],
        exactFirstUnnormalizedNormalEnclosed=[interval(x) for x in n],
        exactSquaredDistanceEnclosed=interval(d2),exactSquaredNormalBallRatioEnclosed=interval(ratio2),
        exactPositiveMarginEnclosed=interval(margin),strictReachUpper=str(args.radius),
        unchangedCentralDiameterLower=str(D),strictNormalizedReachUpper=str(args.radius/D),
        predicate='|Xq-Xp|^4*|Xp_s cross Xp_u|^2 < 4*R^2*((Xp_s cross Xp_u) dot (Xq-Xp))^2',
        exactIntegerRationalArithmetic=True,allStoredFourierModesConsumed=int(z['coeff'].shape[2]),
        actualSavedAdditiveCorrectionConsumed=corr is not None,
        appliesToEveryEmbeddedClosedExtensionRetainingTheseTwoJets=True,
        provesNonexistenceForOtherFields=False,seconds=time.monotonic()-start)
    with args.output.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
    print(json.dumps(output),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('state','field','output'):p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--correction',type=Path)
    p.add_argument('--s1',type=Q,default=Q(85,256))
    p.add_argument('--s2',type=Q,default=Q(325,256))
    p.add_argument('--radius',type=Q,default=Q(7,100))
    run(p.parse_args())
