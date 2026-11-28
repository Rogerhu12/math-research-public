#!/usr/bin/env python3
"""Assemble all 64 true gap-0.92 cells, its Gamma95 repair and the entire nonlocal reach budget."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def get(p):return json.loads(Path(p).read_text())
def dy(v):return Q(float(v))

def run(a):
    first,last,port,trace,graph=map(get,(a.first,a.last,a.port,a.trace,a.graph))
    assert first['selected']==list(range(63)) and last['selected']==[63]
    ids={'physical':sha(a.ramp),'coast':sha(a.coast),'first':sha(a.first),'last':sha(a.last),'port':sha(a.port),
         'trace':sha(a.trace),'exit':sha(a.graph),'endpoint':sha(a.endpoint),'entry':sha(__file__)}
    assert first['source']['master']==last['source']['master']==port['source']['fullPhysicalMasterSHA256']==ids['physical']
    assert first['source']['coast']==last['source']['coast']==port['source']['coastMasterSHA256']==trace['source']['coastMasterSHA256']==ids['coast']
    assert last['source']['terminalTrace']==graph['terminalPrimitiveSHA256']==ids['trace']
    assert graph['rampSHA256']==ids['physical'] and graph['coastSHA256']==ids['coast']
    assert trace['source']['completePortReportSHA256']==ids['port']
    assert first['source']['endpointInput']==last['source']['endpointInput']==port['source']['gramReportSHA256']==trace['source']['gramReportSHA256']==graph['endpointInputSHA256']==ids['endpoint']
    for report,path in ((first,a.first),(last,a.last)):
        cells=Path(str(path)+'.cells')
        assert [sha(cells/f'cell-{j:03d}.json') for j in report['selected']]==report['rawReceiptSHA256']
    assert first['allTheta'] and last['allTheta'] and port['fullAngularDomainCertified'] and trace['fullAngularDomainCertified'] and graph['boundaryGraphAndPositiveHeight']
    with np.load(a.ramp) as r:A,B,c,v,delta=[dy(r[k]) for k in ('centralA','centralB','centralLength','v','ramp')]
    with np.load(a.coast) as z:ell=dy(z['length'])
    U=max(Q(x['exactRelativeMetricUpper']) for x in (first,last));Kr=max(Q(x['exactOwnCurvatureUpper']) for x in (first,last))
    Kc=Q(port['allCoastGeometry']['nonzero_principal_curvature']['hi']);below=Q(port['allCoastGeometry']['nonzero_principal_curvature']['lo'])
    K=Q(38,5);assert 0<below<Kc<K and A/B**2<K and Kr<K and U<Q('5e-10')
    Uuse=Q('5e-10');h=delta*(1+Uuse/2)+ell
    z0=Q(graph['exactLower']['aboveCentral']);slack=h-z0
    assert 0<slack<Q('.000782')
    horizontal=Q('.0112');spatial=Q('.01125');zerror=slack+delta*Uuse
    assert 2*h*slack<horizontal**2 and 2*h*slack+zerror**2<spatial**2
    de=2/K+2*horizontal;theta=Q('.30')
    assert de<2*B*(theta-theta**3/6)
    M=(A*A-B*B)/B;chordfactor=(1+M*theta**2/(6*B))/(1-theta**2/6)
    warp=1+v*(delta/2+ell)/B
    short=(1+Uuse/2)*warp*chordfactor*(2/K+2*spatial)
    assert short<Q('3.14')/K
    central_r=Q('1.60')
    assert (central_r-h)**2>A**2+c**2 and B+h<Q('.568') and A-B-h>Q('.83999')
    # b_d is shorter by 3/2^58; S5 coast pullback changes E and G by uniformly small positive amounts.
    rd=Q(3,2**58);cspeed=Q(15,8)*rd/(ell-rd)
    coastE=2*cspeed+cspeed**2
    coastG=2*v*rd/B+(v*rd/B)**2
    assert max(coastE,coastG)<Q('2e-15')<Uuse
    d=dict(rampMetric=U,rampCurvature=Kr,coastCurvatureUpper=Kc,centralCurvature=A/B**2,adoptedK=K,wholePrefixReach=1/K,
        exactExitHeightAboveCentral=z0,meridianLength=h,maximumVerticalSlack=slack,horizontalDisplacementUpper=horizontal,
        spatialDisplacementUpper=spatial,angleHalfWidth=theta,ellipseArcChordFactor=chordfactor,warpingFactor=warp,
        nearChordIntrinsicLengthUpper=short,piOverKLower=Q('3.14')/K,
        fixedShortCoastEAdditional=coastE,fixedShortCoastGAdditional=coastG,
        halfWidthUpper=B+h,heldFromEntirePrefixLower=A-B-h)
    out=dict(schema='exact-new-gap-H65-Gamma95-complete-prefix-all-pairs-reach-v1',ids=ids,
        exactBounds={k:str(q) for k,q in d.items()},metricPeakCell=first['maximumMetricCell'] if Q(first['exactRelativeMetricUpper'])>Q(last['exactRelativeMetricUpper']) else 63,
        physicalRampCells=64,closedNativeCurvatureBoxes=first['allBoxes']+last['allBoxes'],terminalPortBoxes=port['completeClosedCells'],
        trueExitGraphBoxes=graph['cells'],wholeClosedAnnularPrefix=True,fullClosedSurface=False)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print({k:float(q) for k,q in d.items()})
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('ramp','coast','first','last','port','trace','graph','endpoint','output'):
        p.add_argument('--'+k,type=Path,required=True)
    run(p.parse_args())
