#!/usr/bin/env python3
"""Bind the selected complete convex-cap geometry and its true throat to the physical dense observations."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
p=Path(__file__).parent/'2ecf-polar-released-physical-cap-roof-and-exit-curvature.py'
sp=importlib.util.spec_from_file_location('selected_actual_physical_cap',p);cap=importlib.util.module_from_spec(sp);sys.modules[sp.name]=cap;sp.loader.exec_module(cap)
def run(a):
    q=cap.base.read(a.solution);name=q['completeRigidCaps'];assert name in ('R219','R293')
    delta=Q.from_float(q['raisedCuffDelta']);Z=Q(83,200)+delta;total=Q(127,200) if name=='R293' else Q(53,100)
    actual=dict(connectorFixedTarget=q['targetSHA256'],cap=name,c='13/20' if name=='R293' else '79/100',supportB='132/125',h='43/50',H='29/20' if name=='R293' else '31/20',Z=str(Z),eta=str(total-Z),R='97/1000',openCuffRadius='8/25',lambdaValue='1/100',shortenedMeridian='R210 L=8eta/(3pi)',symmetricTwoOriginalConvexBodiesAtNewFixedParameter=True)
    deschash=hashlib.sha256(json.dumps(actual,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    dst=a.output
    with TemporaryDirectory(dir=dst.parent) as tmp:
        inner=Path(tmp)/'full.json';a.output=inner;a.mode='observe';cap.run(a);res=cap.base.read(inner)
    res.update(closedCapConsumerEntrySHA256=cap.base.sha(__file__),fixedCompleteGeometry=actual,closedTrueTargetSHA256=deschash,finiteConnectorOnly=True)
    cap.base.stores(dst,res)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','solution','output'):p.add_argument('--'+k,type=Path,required=True)
    run(p.parse_args())
