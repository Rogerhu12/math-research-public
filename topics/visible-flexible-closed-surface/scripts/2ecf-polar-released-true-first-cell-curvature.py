#!/usr/bin/env python3
"""Include the true characteristic outlet and every endpoint error in the first cell curvature."""
import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
p=Path(__file__).parent/'2ecf-polar-released-directed-full-polynomial-curvature.py'
sp=importlib.util.spec_from_file_location('first_with_true_outlet',p);D=importlib.util.module_from_spec(sp);sys.modules[sp.name]=D;sp.loader.exec_module(D)
def run(a):
    edge=json.load(a.edge.open());assert edge['fieldSHA256']==D.shape.digest(a.field) and edge['closedPrimitiveTrue']
    errs=[[Q(v) for v in row] for row in edge['accurateMinusStoredPhysicalDerivativeMaxUpper']]
    knots=np.load(a.field)['knots'];h=Q(knots[1])-Q(knots[0])
    q0=[[Q(1),0,0],[Q(1),h/5,0],[Q(1),2*h/5,h*h/20],[0,0,0],[0,0,0],[0,0,0]]
    controls=[q0]
    for n in (5,4):
        r=controls[-1];controls.append([[(r[i+1][j]-r[i][j])*n/h for j in range(3)] for i in range(n)])
    class TruePhase(D.Phase):
        def vals(self,ctrl,j):
            lo,hi=super().vals(ctrl,j);dc=controls[6-len(lo)]
            eb=np.array([np.nextafter(float(sum(abs(w)*errs[k][j] for k,w in enumerate(row))),np.inf) for row in dc])[:,None,None]
            return np.nextafter(lo-eb,-np.inf),np.nextafter(hi+eb,np.inf)
    D.Phase=TruePhase;a.start_cell=0;a.end_cell=1
    from tempfile import TemporaryDirectory
    dest=a.output
    with TemporaryDirectory(dir=dest.parent) as tmp:
        inner=Path(tmp)/'proof.json';a.output=inner;D.run(a);q=json.load(inner.open())
    assert len(q['pieces'])==1 and Q(q['pieces'][0]['left'])==Q(knots[0]) and Q(q['pieces'][0]['right'])==Q(knots[1])
    q.update(firstNonpolynomialCellIncluded=True,trueEndpointInputSHA256=D.shape.digest(a.edge),trueFirstCellEntrySHA256=D.shape.digest(__file__),outletCorrectionAppliedToEveryRealBernsteinControl=True)
    with dest.open('x') as f:json.dump(q,f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for n in ('scripts','state','field','spatial','edge','output'):p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--threshold',type=Q,default=Q(1041,100));p.add_argument('--quarter-angles',type=int,default=1024);p.add_argument('--radial-depth',type=int,default=7);run(p.parse_args())
