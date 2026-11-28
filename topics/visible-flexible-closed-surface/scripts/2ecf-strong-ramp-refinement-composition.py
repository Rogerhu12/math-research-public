#!/usr/bin/env python3
"""Compose the two new whole-prefix certificates, old lower bounds and exact endpoint chart."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import numpy as np


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_bytes())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('h33','h65','witness','old','coast','results','out'):
        p.add_argument('--'+k,required=True,type=Path)
    a=p.parse_args()
    with np.load(a.old,allow_pickle=False) as m:
        A,B,c,r,v=[Q(float(m[k])) for k in ('centralA','centralB','centralLength','ramp','v')]
    with np.load(a.coast,allow_pickle=False) as m:
        ell=Q(float(m['length']))
    assert sha(a.old)=='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7'
    assert sha(a.coast)=='f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d'
    witness=read(a.witness)
    assert [x['nodes'] for x in witness['rows']]==[17,33,65]
    L={x['nodes']:Q(x['relativeMetricLower']) for x in witness['rows']}
    assert witness['rows'][0]['masterSHA256']==sha(a.old)
    b_exact=c+r+ell
    assert Q(float(c)+float(r))==c+r
    b_literal=Q(float(c+r)+float(ell))
    d=b_exact-b_literal
    ell0=ell-d
    assert d==Q(3,2**58) and ell0>0
    # The endpoint chart uses S5=10x^3-15x^4+6x^5, max S5'=15/8.
    dt=d*Q(15,8)/ell0
    # The accurate ellipse-radius series is (A+B)/2 times a sum of squares.
    # Its explicit terms 0,1,2 already give a lower bound above 1.
    z=(A-B)/(A+B)
    fmin=(A+B)/2*(1+(z/2)**2+(z*z/8)**2)+v*r/2
    de=2*dt+dt**2
    dg=2*v*d/fmin+(v*d/fmin)**2
    assert de<Q('2e-15') and dg<Q('1e-18')
    bounds={}
    cap=Q('9.867915')
    height=Q('.07874442')
    for n,path in ((33,a.h33),(65,a.h65)):
        cert=read(path)
        assert cert['completeRamp'] and cert['selected']==list(range(n-1))
        assert cert['sameAccurateTargetG'] and cert['allTheta']
        assert cert['closedNativeRadialDomain']==['0',str(r)]
        assert cert['source']['old']==sha(a.old) and cert['source']['coast']==sha(a.coast)
        assert cert['source']['master']==next(row['masterSHA256'] for row in witness['rows'] if row['nodes']==n)
        cells=path.with_suffix(path.suffix+'.cells')
        assert cert['rawReceiptSHA256']==[sha(cells/f'cell-{j:03d}.json') for j in range(n-1)]
        u=Q(cert['exactRelativeMetricUpper'])
        k=Q(cert['exactOwnCurvatureUpper'])
        assert k<cap and A/B**2<cap and Q('8.892834503')<cap
        eps=max(de,dg,u)
        assert eps==u and eps<Q('6.1e-7')
        assert L[n]<u<L[17 if n==33 else 33]
        h=r*(1+eps/2)+ell
        gap=h-height
        dz=gap+eps*r
        assert dz<Q('.00126') and 2*h*gap<Q('.0142')**2
        assert Q('.0142')**2+Q('.00126')**2<Q('.0143')**2
        W=1+v*(r/2+ell)/B
        H=Q('.294')
        M=(A*A-B*B)/B
        Ce=(1+M*H**2/(6*B))/(1-H**2/6)
        chord=2/cap
        assert chord<Q('.203') and (H-H**3/6)*2*B>Q('.203')+2*Q('.0142')
        path_bound=(1+eps/2)*W*Ce*(chord+2*Q('.0143'))
        assert path_bound<Q('.279') and path_bound*cap<3
        bounds[n]=dict(nodes=n,ownContinuousCertificateSHA256=sha(path),wholeRelativeMetricUpper=str(u),
                       actualPointLower=str(L[n]),ownRampCurvatureUpper=str(k),
                       maximumMetricCell=cert['maximumMetricCell'],maximumCurvatureCell=cert['maximumCurvatureCell'],
                       angularRadialBoxes=cert['allBoxes'],meridionalLengthFromCentralUpper=str(h),
                       heightExcessUpper=str(dz),horizontalDriftSquaredUpper=str(2*h*gap),
                       nearPairIntrinsicLengthUpper=str(path_bound),reachLower=str(1/cap))
    assert Q(bounds[65]['wholeRelativeMetricUpper'])<Q('2e-9')<L[33]
    inherited=['R232-new-gap-complete-accurate-terminal-port-bounds.md',
               'R233-entire-ramp-accurate-coast-normalization.md',
               'R257-accurate-whole-prefix-global-embedding.md',
               'R259-accurate-whole-prefix-two-sided-reach.md']
    result=dict(schema='strong-H17-H33-H65-complete-two-step-accurate-prefix-v1',
                sourceSHA256=sha(Path(__file__)),oldRawRampSHA256=sha(a.old),coastSHA256=sha(a.coast),
                witnessReportSHA256=sha(a.witness),priorProofs={f:sha(a.results/f) for f in inherited},
                prefixMetricBoundsAndOwnNonlocalReach=bounds,firstStrictDecrease=True,secondStrictDecrease=True,
                reachAsClosedAnnulusIncludingBothBoundaryCircles=True,wholeClosedSurfaceCertified=False,
                exactBreakChart={k:str(z) for k,z in dict(accurateRampEnd=c+r,accuratePrefixEnd=b_exact,
                    literalPrefixEnd=b_literal,delta=d,shortCoastLength=ell0,maximumDerivativeIncrement=dt,
                    targetRadiusLower=fmin,extraNormalizedRadialMetricUpper=de,
                    extraNormalizedAngularMetricUpper=dg).items()})
    with a.out.open('x') as f:
        json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(dict(U33=float(Q(bounds[33]['wholeRelativeMetricUpper'])),
                         U65=float(Q(bounds[65]['wholeRelativeMetricUpper'])),reach=float(1/cap),
                         bDifference=str(d),coastEUpper=float(de),coastGUpper=float(dg))))


if __name__=='__main__':
    main()
