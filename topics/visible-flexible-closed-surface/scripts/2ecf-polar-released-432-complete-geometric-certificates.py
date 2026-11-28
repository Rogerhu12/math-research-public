#!/usr/bin/env python3
"""Compose the new 432-coefficient exact shape and curvature enclosures with the true higher caps."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import numpy as np
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rd(p):return json.loads(Path(p).read_text())
def run(a):
    state=rd(a.spatial);closed=rd(a.closed);pre=rd(a.prefix);npz=sha(a.field);ident=sha(a.spatial);kn=list(map(Q,np.load(a.field)['knots']))
    assert state['sourceFieldSHA256']==npz and closed['solutionSHA256']==ident and state['controls']==432 and state['ownActual']==540
    cap=closed['fixedCompleteGeometry'];Z=Q(cap['Z']);eta=Q(cap['eta']);R=Q(97,1000);eps=Q(1,10000);b=Q(132,125)
    assert cap['cap']=='R293' and Z+eta==Q(127,200) and Q(4799,10000)<Z<Q(3,5)
    assert pre['wholeClosedAnnularPrefix'] and pre['physicalRampCells']==64
    common=dict(entrySHA256=sha(__file__),spatialSHA256=ident,sourceFieldSHA256=npz,completePhysicalFieldSHA256=sha(a.closed),newClosedMetricSHA256=closed['closedTrueTargetSHA256'],originalCompletePrefixReceiptSHA256=sha(a.prefix),R293CapProofSourceSHA256=sha(a.cap_source),trueCuffZ=str(Z),trueThroatEta=str(eta))
    if a.mode=='shape':
        s=rd(a.shape);assert s['sourceFieldSHA256']==npz and s['cartesianCorrectionSHA256']==ident and s['strongClosedShapePass']
        A=Q(float.fromhex('0x1.68493d1d794f0p+0'));B=Q(7911,5000);Y=Q(889603,1000000);held=Q(652115,1000000);hZ=Q(162601,175000)
        corner=(B-R-eps)**2-Q(cap['c'])**2-(b-R)**2-hZ**2;top=B-(Q(cap['H'])-Q(cap['h'])+hZ+eps)
        assert corner>0 and top>0
        assert Q(s['upperAbsY'])<Y and Q(s['upperNormSquared'])<B*B and Q(s['lowerWitnessDistanceSquared'])>held*held
        assert (A+Q(112,10000))**2+Q(182,1000)**2<B*B
        assert Q(32,100)**2+Q(84,100)**2<B*B
        assert min(A-Q(498568,1000000),A-Q(400001,1000000),Q(829,1000))>held
        assert Q(cap['c'])+R+eps<Y and Q(498568,1000000)<Y
        dx=b-eps-Y
        common.update(shapeCertificateSHA256=sha(a.shape),closedShapeBoxCount=s['nonemptyBoxCount'],R293NewAllCapCornerSquaredMargin=str(corner),R293NewAllCapAxialMargin=str(top),actualWholeDUpper=str(2*B),actualHeldStrictLower=str(held),actualEuclideanQuotientStrictLower=str(dx),actualHeldOverDStrictLower=str(held/(2*B)),actualQuotientOverDStrictLower=str(dx/(2*B)),fixedGripDiameterStrictLower='75897/25000',trueCoreZ=s['trueConnectorZInterval'],radialConditionalUpperZ=s['radialConditionalUpperZ'])
    else:
        cov={i:[] for i in range(len(kn)-1)};K=Q(1041,100);inputs=[]
        for path in a.parts:
            pp=rd(path);assert pp['fieldSHA256']==npz and pp['spatialSHA256']==ident and Q(pp['threshold'])==K
            if pp['sourceCells'][0]==0:assert pp['firstNonpolynomialCellIncluded'] and pp['trueEndpointInputSHA256']==sha(a.edge)
            for row in pp['pieces']:
                if row['failedTerminalBoxes']==0:
                    j=row['sourceCell'];lo,hi=Q(row['left']),Q(row['right']);assert kn[j]<=lo<hi<=kn[j+1];cov[j].append((lo,hi))
            inputs.append(sha(path))
        for j,segments in cov.items():
            cursor=kn[j]
            for lo,hi in sorted(set(segments)):
                if lo<=cursor:cursor=max(cursor,hi)
            assert cursor==kn[j+1],(j,cursor,kn[j+1])
        e=rd(a.edge);assert e['closedPrimitiveTrue'] and e['nativeClosedCells']==2048 and e['fieldSHA256']==npz
        assert K<Q(1,1)/Q(96,1000) and Q(1,1)/R<K and Q(76,10)<K
        common.update(curvatureCertificatePartSHA256=inputs,trueMaterialOutletReceiptSHA256=sha(a.edge),completeTruePhysicalHermiteCells=len(cov),fullMaterialAngles=True,continuousCoreAbsolutePrincipalCurvatureStrictUpper=str(K),closedFamilyLocalAbsolutePrincipalCurvatureStrictUpper=str(K),localRadiusLower=str(1/K),reachClaimed=False)
    with a.output.open('x') as f:json.dump(common,f,indent=2);f.write('\n')
    print(common.get('actualWholeDUpper'),common.get('continuousCoreAbsolutePrincipalCurvatureStrictUpper'))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('shape','curvature'),required=True)
    for v in ('field','spatial','closed','cap-source','prefix','shape','edge','output'):p.add_argument('--'+v,type=Path)
    p.add_argument('--parts',nargs='+',type=Path);run(p.parse_args())
