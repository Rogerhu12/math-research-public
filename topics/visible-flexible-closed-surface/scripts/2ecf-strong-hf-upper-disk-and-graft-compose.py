#!/usr/bin/env python3
"""Compose the actual upper-disk cover, held exclusion, and fixed R210 cap estimates."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_bytes())
def root_up(q,decimals):
    scale=10**decimals
    k=isqrt(q.numerator*scale**2//q.denominator)
    if F(k*k,scale**2)<q:k+=1
    return F(k,scale)


def main():
    ap=argparse.ArgumentParser()
    for n in ('scripts','potential','native','coast','interior','edges','tail','window','field','output'):ap.add_argument('--'+n,type=Path,required=True)
    a=ap.parse_args();src=a.scripts.parent/'results';pot=sha(a.potential);field=sha(a.field)
    d={n:read(getattr(a,n)) for n in ('native','coast','interior','edges','tail','window')}
    if not all(d[n]['potentialSHA256']==pot for n in ('native','coast','interior','edges','tail')):raise ValueError('Different angular potentials')
    if not all(d[n]['fieldSHA256']==field for n in ('interior','edges','window')):raise ValueError('Different actual position')
    if d['native']['physicalRampSegments']!=64 or d['native']['masterSHA256']!='479dab51bd77a211f64a256bbb16d67b4382e150af0deee7fa6baf84d8e5464a':
        raise ValueError('Different native H65')
    if d['coast']['coastSHA256']!='f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d' or d['coast']['physicalLengthExact']!=str(F(.02)):
        raise ValueError('Different accurate normalized coast')
    if len({d[n]['sectorSourceSHA256'] for n in ('native','coast','interior','edges','tail')})!=1:raise ValueError('Different sector enclosure')
    import numpy as np
    with np.load(a.field) as z:breaks=sorted(set(map(F,z['knots']))|set(map(F,z['Wknots'])))
    spans=sorted([tuple(map(F,r)) for name in ('edges','interior') for r in d[name]['physicalSpans']])
    if spans!=list(zip(breaks[:-1],breaks[1:])):raise ValueError('Physical suffix cover incomplete')
    pieces=[d['native']['central'],d['native']['completeH65']]+[d[n] for n in ('coast','edges','interior','tail')]
    bounds=[row['bounds'] for row in pieces]
    if any(min(x['angularJacobian'],x['positiveRayNumerator'])<=0 for x in bounds):raise ValueError('Monotonicity incomplete')
    if any(x['minimumHeight']<=0 for x in bounds[1:]):raise ValueError('Upper/lower separation incomplete')
    if d['window']['originalCommonElements']!=len(spans):raise ValueError('Height coverage incomplete')
    Z=F(d['window']['cuffHeightExact'])
    if Z!=F(.51) or F(d['window']['upperHeight'])>=Z+F(1,50) or F(d['window']['lowerRadiusSquaredWheneverHeightExceedsCuff'])<=F(514,1000)**2:
        raise ValueError('R210 height window incomplete')
    radius2=max(F(x['maximumRadiusSquared']) for x in bounds)
    held2=min(F(x['minimumHeldDistanceSquared']) for x in bounds)
    width=max(F(x['maximumAbsoluteY']) for x in bounds)
    held=F(6576,10000);R=F(97,1000);eps=F(1,10000);c=F(3,4);b=F(1011,1000);h=F(37,40);H=F(31,20)
    zcmin=h-eps-3*R-F(1,100)*R*F(22,7);t=Z+F(1,50)-zcmin
    if not h+t>0 or not h+Z+F(1,50)-(h-eps-3*R)>0:raise ValueError('Need positive translated vertex heights')
    corners=c*c+(b-R)**2+(h+t)**2;cap_point=max(root_up(corners,9)+R+eps,H+t+eps)
    cap_ball=max(cap_point,root_up(F(8,25)**2+(h-eps-R)**2,9))
    rad=max(root_up(radius2,9),cap_ball)
    if held2<=held**2 or Z+2*R+F(1,50)<=held or F('1.453')-F(8,25)<=held:raise ValueError('Whole capped held witness incomplete')
    W=max(width,c+R+eps);deltaE=b-eps-W
    D=2*rad
    if not (D<F('3.076642') and held/D>F('.2137') and deltaE/D>F('.0532')):raise ValueError('Strong shape ratios not reached')
    if not (root_up(radius2,9)<F('1.466') and held/(2*root_up(radius2,9))>F('.2243')):raise ValueError('Ungrafted geometric budget insufficient')
    out=dict(schema='2ecf-H65-corrected-HF64-R205-full-kernel-and-actual-fixed-R210-graft-shape-v1',
        entrySHA256=sha(__file__),inputs={n:sha(getattr(a,n)) for n in ('potential','native','coast','interior','edges','tail','window','field')},
        publicGeometryInputs={p.name:sha(p) for p in [next(src.glob('R210-*')),next(src.glob('R204-*')),next(src.glob('R261-*')),next(src.glob('R265-*')),next(src.glob('R270-*'))]},
        strictlyPositiveNoncentralHeight=True,completeUpperDiskPotentialBoxes=sum(q['closedBoxes'] for q in pieces),
        upperKernelRadiusSquared=str(radius2),lowerWholeKernelHeldSquared=str(held2),upperKernelWidth=str(width),
        kernelDiameterUpper=str(2*root_up(radius2,9)),uncappedKernelHeldRatioLower=str(held/(2*root_up(radius2,9))),
        capHeightExact=str(Z),upperCapSphereRadius=str(cap_ball),graftedDiameterUpper=str(D),
        graftedHeldDistanceLower=str(held),graftedAlignedHausdorffLower=str(deltaE),
        graftedHeldOverDiameterLower=str(held/D),graftedAlignedOverDiameterLower=str(deltaE/D),
        completeActualKernelAndGraftEmbedding=True,completeAllPhaseC2Continuity=True,wholeReachCertified=False,wholeFixedMetricAccuracyCertified=False)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    for k in ('completeUpperDiskPotentialBoxes','graftedDiameterUpper','graftedHeldDistanceLower','graftedAlignedHausdorffLower',
        'graftedHeldOverDiameterLower','graftedAlignedOverDiameterLower'):print(k,float(F(out[k])))


if __name__=='__main__':main()
