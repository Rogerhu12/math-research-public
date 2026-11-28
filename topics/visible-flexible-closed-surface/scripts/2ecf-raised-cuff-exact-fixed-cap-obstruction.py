#!/usr/bin/env python3
"""R292 exact point on the full raised source versus an actual old flat cap.

The stored binary field is evaluated rationally at u=pi/2. The cap point
has the same x,y and its exact height involves I=int_0^pi sqrt(sin t)dt;
only the strict analytic bounds 2<I<22/7 are needed.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def run(a):
    src=a.scripts/'2ecf-released-cuff-exact-two-point-reach-obstruction.py'
    sp=importlib.util.spec_from_file_location('r290_exact_point',src)
    module=importlib.util.module_from_spec(sp);sp.loader.exec_module(module)
    state=json.loads(a.state.read_text());corr=json.loads(a.correction.read_text())
    assert state['fieldSHA256']==corr['sourceFieldSHA256']==sha(a.field)
    assert corr['sourceStateSHA256']==sha(a.state)
    assert corr['targetSHA256']==state['targetSHA256']
    z=np.load(a.field);p=module.packet(z,a.s,corr)
    b,T=map(module.rational,corr['physicalInterval']);t=(a.s-b)/(T-b)
    assert 0<t<1
    delta=module.rational(.08)
    step=10*t**3-15*t**4+6*t**5
    p['P'][2]+=delta*step
    x,y,h=p['P'];R=Q(97,1000)
    caplo=Q(53,100)+2*R+Q(1,100)*R*2
    caphi=Q(53,100)+2*R+Q(1,100)*R*Q(22,7)
    # This rectangle is in the exactly flat bottom before and after smoothing.
    assert abs(x)<Q(789999,1000000) and abs(y)<Q(958999,1000000)
    assert x*x+y*y>Q(3,10)**2
    assert 0<h<caplo
    ceiling=Q(47,1000)
    assert (caphi-h)/2<ceiling
    out=dict(schema='R292-exact-full-raised-field-old-cap-obstruction-v1',
        entrySHA256=sha(__file__),exactEvaluatorSHA256=sha(src),
        stateSHA256=sha(a.state),fieldSHA256=sha(a.field),correctionSHA256=sha(a.correction),
        targetSHA256=state['targetSHA256'],materialS=str(a.s),materialU='pi/2',
        heightShift=str(delta),stepValue=module.interval(step),
        actualCorePointEnclosed=[module.interval(v) for v in p['P']],
        exactCapBottomLower=str(caplo),exactCapBottomUpper=str(caphi),
        capNormal='(0,0,1)',capPointHorizontalCoordinatesEqualActualCore=True,
        squaredHorizontalRadius=module.interval(x*x+y*y),
        normalBallRatioUpper=module.interval((caphi-h)/2),
        strictReachUpper=str(ceiling),unchangedDiameterLower='14/5',
        strictNormalizedReachUpper=str(ceiling/Q(14,5)),
        allFieldModes=int(z['coeff'].shape[2]),allAdditiveControls=len(corr['coefficients']),
        integerRationalArithmetic=True,oldCap='R219 with Z+eta=53/100',
        scope='This actual field with these fixed caps only; other caps and fields not excluded')
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('scripts','state','field','correction','output'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--s',type=Q,default=Q(259,256))
    run(p.parse_args())
