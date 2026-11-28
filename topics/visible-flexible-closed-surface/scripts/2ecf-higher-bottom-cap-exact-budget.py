#!/usr/bin/env python3
"""R293 exact scalar and polar budgets; its full geometric proof is separate."""
from fractions import Fraction as Q
from itertools import combinations
import json


def solve(rows):
    a=[list(n)+[b] for n,b in rows]
    for i in range(3):
        j=next((j for j in range(i,3) if a[j][i]),None)
        if j is None:return None
        a[i],a[j]=a[j],a[i];pivot=a[i][i]
        a[i]=[x/pivot for x in a[i]]
        for j in range(3):
            if j!=i:
                f=a[j][i];a[j]=[x-f*y for x,y in zip(a[j],a[i])]
    return tuple(row[3] for row in a)


def run():
    B,R,a,ac=map(Q,('1.6','.097','.30','.32'))
    lam,eps,delta=map(Q,('.01','.0001','.000001'))
    c,b,h,H,W,A,held=map(Q,('.65','1.056','.86','1.45','.895','1.4','.65'))
    C=Q('.635');Zlo,Zhi=Q('.4799'),Q('.60');etamax=C-Zlo
    low=C+eps+3*R+2*lam*R;high=C+eps+3*R+lam*R*Q(22,7)
    Hlow=H-h+low
    planes=[((Q(-1),Q(0),Q(0)),Q(0)),((Q(0),Q(-1),Q(0)),Q(0)),
            ((Q(0),Q(0),Q(-1)),Q(0)),((A,Q(0),Q(0)),Q(1)),
            ((Q(0),Q(0),Hlow),Q(1)),((c,b,low),Q(1))]
    vs=set()
    for rows in combinations(planes,3):
        v=solve(rows)
        if v is not None and all(sum(x*y for x,y in zip(n,v))<=rhs for n,rhs in planes):vs.add(v)
    assert len(vs)==8
    polar=[]
    for v in sorted(vs):
        margin=1-b*b*sum(x*x for x in v);assert margin>=0
        polar.append({'vertex':list(map(str,v)),'oneMinus_b2_norm2':str(margin)})
    budgets={
        'pyramidHeight':H-R-h,
        'flatBottomRadialClearance':min(c,b-R)-delta-(a+R),
        'throatRadiusMinusR':a-R*(1+2*lam)-etamax/4-R,
        'flatCollarWidth':ac-a,
        'cornerSphereSquared':(B-R-eps)**2-c*c-(b-R)**2-high*high,
        'topSphereMargin':B-(H-h+high+eps),
        'throatSphereSquared':B*B-ac*ac-(C+2*R+lam*R*Q(22,7))**2,
        'capXSlabMargin':W-c-R-eps,
        'upperOldDiskBallsContainThroatBalls':2*R*etamax-etamax**2-(R-(ac-a))**2,
        'smallerReachBallPoint096WithPoint13Protrusion':2*Q('.096')*Q('.13')-Q('.13')**2-(Q('.096')-(ac-a))**2,
        'etaBelowTwoR':2*R-etamax,
        'etaPositive':C-Zhi,
        'oppositeCapsSeparationMinusTwoR':2*Zlo-2*R,
        'throatHeldSquared':(A-ac)**2-held**2,
        'convexCapHeldSquared':(A-b-eps)**2+(C+2*R)**2-held**2,
        'E3AbsoluteGapMinusPoint16':b-eps-W-Q('.16'),
        'reachNormalizedMargin':R/(2*B)-Q('.03'),
        'gripDiameterMinusPoint64':2*Hlow-2*eps-Q('.64'),
    }
    assert all(v>0 for v in budgets.values())
    assert low==Q('.92804') and Hlow==Q('1.51804')
    out=dict(schema='R293-complete-higher-flat-bottom-cap-exact-budgets-v1',
        parameters={k:str(v) for k,v in dict(B=B,R=R,a=a,ac=ac,lam=lam,eps=eps,delta=delta,
                    c=c,b=b,h=h,H=H,W=W,A=A,held=held,Zlo=Zlo,Zhi=Zhi,ZplusEta=C).items()},
        cornerHeightLower=str(low),cornerHeightUpper=str(high),topHeightLower=str(Hlow),
        flatBottomLower=str(C+2*R+2*lam*R),flatBottomUpper=str(C+2*R+lam*R*Q(22,7)),
        polarVertices=polar,strictBudgets={k:str(v) for k,v in budgets.items()},
        allAssertionsPassed=True,wholeCoreMetricEmbeddingReachRemainInputs=True)
    print(json.dumps(out,indent=2))


if __name__=='__main__':run()
