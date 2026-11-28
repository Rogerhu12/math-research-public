#!/usr/bin/env python3
"""Generate two actual finer fields from the same Cauchy IVP and fixed exact coast port."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
from scipy.integrate import solve_ivp


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def module(p):
    spec=importlib.util.spec_from_file_location('strong_physical_h_original_warm',p)
    m=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=m
    spec.loader.exec_module(m)
    return m


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('scripts','ramp','coast','out'):
        ap.add_argument('--'+name,required=True,type=Path)
    a=ap.parse_args()
    started=time.monotonic()
    assert sha(a.ramp)=='0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7'
    assert sha(a.coast)=='f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d'
    a.out.mkdir(exist_ok=False)
    with np.load(a.ramp,allow_pickle=False) as raw:
        master={k:raw[k].copy() for k in raw.files}
    A,B,c,r,v=[float(master[k]) for k in ('centralA','centralB','centralLength','ramp','v')]
    warm=a.scripts/'6a65-geometry-cauchy-unit-t-warm.py'
    producer=a.scripts/'6a65-geometry-coupled-gap-prefix.py'
    w=module(warm)
    candidate=w.p.Candidate(A,B,r,v)
    flow=w.p.hybrid.Hybrid(candidate,191,2,30000)
    y=flow.initial()
    y[flow.shape_size:].reshape(flow.work,12)[:,2]=c
    # The old IVP producer used these 65 actual dense-output nodes.
    nodes=np.linspace(0,r,65)
    assert np.array_equal(nodes[::4],master['sx'])
    sol=solve_ivp(flow.rhs,(0,r),y,method='DOP853',rtol=2e-12,
                  atol=2e-14/(1+flow.active_wave)**2,max_step=.0005,t_eval=nodes)
    assert sol.status==0 and np.array_equal(nodes,sol.t)
    actual=[]
    for i,(s,state) in enumerate(zip(nodes,sol.y.T)):
        packet=flow.frame(float(s),state)
        native=np.asarray(packet['values'],float)
        ell=(native[:,1]**2+float(packet['K']))/native[:,0]
        jets=np.stack((native[:,2:5],native[:,5:8],ell[:,None]*native[:,11:14]),axis=1)
        actual.append(np.fft.fft(jets,axis=0)/flow.work)
    actual=np.array(actual)
    previous=master['coefficients']
    assert actual.shape==(65,768,3,3)
    restart_error=float(np.max(np.abs(actual[::4]-previous)))
    actual[::4]=previous
    outputs={}
    for step in (2,1):
        coeff=actual[::step];sx=nodes[::step]
        assert np.array_equal(coeff[::4//step],previous)
        output=a.out/f'ramp-{len(sx)}.npz'
        np.savez_compressed(output,**dict(master,sx=sx,coefficients=coeff))
        outputs[str(len(sx))]=dict(file=output.name,SHA256=sha(output),positionJetShape=list(coeff.shape),
                maxInsertedVsEndpointLinearMeanDiagnostic=float(np.max(abs(coeff[1::2]-(coeff[:-2:2]+coeff[2::2])/2))))
    d=dict(schema='strong-coupled-gap-physical-H17-H33-H65-fixed-g-v1',sourceSHA256=sha(Path(__file__)),
           originalRampSHA256=sha(a.ramp),exactCoastMasterSHA256=sha(a.coast),
           historicalProducerSHA256=sha(producer),warmProducerSHA256=sha(warm),
           sourceDependencies={name:sha(a.scripts/name) for name in ('6a65-geometry-central-cauchy-r137.py',
                      'fd2d-gc-ellipse-hybrid-flow.py','6a65-geometry-central-cauchy-tail.py')},
           nfev=sol.nfev,cauchyRHSCalls=flow.calls,actualDenseOutputs=len(sol.t),
           oldNodesMaxRestartComparison=restart_error,old17NodesBitwisePreserved=True,
           exactGeometryDefinition='Same dyadic A,B,c,r,v, exact ellipse mean target, exact original R232 Gamma95 fixed coast PVA repair; R233 integral normalization with new inner-node actual positions.',
           physicalSubdivisionIsNotKnotInsertionOfOldSpline=True,completeContinuousMetricCertified=False,
           outputs=outputs,seconds=time.monotonic()-started)
    (a.out/'report.json').write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
    print(json.dumps(d),flush=True)


if __name__=='__main__':
    main()
