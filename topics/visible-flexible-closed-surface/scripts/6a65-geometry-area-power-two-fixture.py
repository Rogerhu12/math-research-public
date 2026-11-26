#!/usr/bin/env python3
"""Small complete nonzero-field FD/JT wiring check for the new q=2 objective.

This uses a declared analytic synthetic surface, not any research state,
old checkpoint, real source cache or claimed mathematical solution.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);sys.modules[name]=value
    spec.loader.exec_module(value);return value


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class AnalyticCache:
    def __init__(self,nodes,N):
        self.nodes=np.asarray(nodes,float)
        self.u=2*np.pi*np.arange(N)/N
        s=self.nodes[:,None];u=self.u[None,:]
        a=1.25+.03*s+.03*s*s;ap=.03+.06*s
        c=np.cos(u);sn=np.sin(u);shape=(len(s),N)
        def stack(x,y,z):
            return np.stack(np.broadcast_arrays(x,y,z),axis=-1)
        self.jets=np.stack([
            stack(a*c,a*sn+.08,.15+.5*(s-.2)**2+1.3*c),
            stack(ap*c,ap*sn,(s-.2)+np.zeros(shape)),
            stack(-a*sn,a*c,-1.3*sn+np.zeros(shape)),
            stack(.06*c+np.zeros(shape),.06*sn+np.zeros(shape),np.ones(shape)),
            stack(-ap*sn,ap*c,np.zeros(shape)),
            stack(-a*c,-a*sn,-1.3*c+np.zeros(shape))
        ],axis=1)
        self.bb=np.broadcast_to(a,shape)
    def __call__(self,nodes,N):
        ix=np.searchsorted(self.nodes,nodes)
        if (N!=len(self.u) or np.any(ix>=len(self.nodes))
            or not np.array_equal(self.nodes[ix],nodes)):
            raise ValueError("No interpolation in the fixture either")
        return self.jets[ix],self.bb[ix]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--area-source",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError("Fresh actual fixture result required")
    begun=time.monotonic()
    base=module(args.scripts/"6a65-geometry-gap-window-cartesian.py","power2_fixture_base")
    joint=module(args.scripts/"6a65-geometry-gap-window-two-grid-cartesian.py","power2_fixture_joint")
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","power2_fixture_stream")
    areaop=module(args.area_source,"power2_fixture_area")
    basis=base.periodic_basis(stream,.2,.9,7,3)
    caches=dict(training=AnalyticCache(np.linspace(.2,.9,13),32),
                observer=AnalyticCache(np.linspace(.2,.9,17),48))
    weights={}
    for key,cache in caches.items():
        w=np.ones(len(cache.nodes))/(2*len(cache.nodes))
        weights[key]=dict(metric=w,curvature=.01*w,geometry=10*w)
    recipe=base.default_recipe()
    recipe["radialBlock"]=4
    config=stream.point.PointConfig(metric_tau=.05,curvature_tau=1e6,curvature_guide=9.5,
        central_a=1.4532280772048913,true_cuff_height=.51)
    area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    rng=np.random.default_rng(2026112602)
    z=3e-4*rng.normal(size=(basis.nb,basis.na))
    linear=areaop.CompleteAreaTwoGrid(joint,stream,basis,caches,weights,z,config,recipe,area)
    expected=14*sum(len(c.nodes)*len(c.u) for c in caches.values())
    if linear.shape!=(expected,basis.dimension):raise ArithmeticError("Complete dimensions changed")
    x=rng.normal(size=basis.dimension);x/=np.linalg.norm(x)
    y=rng.normal(size=linear.shape[0])
    jv=linear.matvec(x)
    lhs=float(jv@y);rhs=float(x@linear.rmatvec(y))
    adj=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
    if adj>1e-11:raise ArithmeticError("Complete q=2 J/JT fixture failed")
    dz=linear.unpack(x)
    original_rows=linear.parent.shape[0]
    checks=[]
    for epsilon in (1e-6,1e-7):
        plus=areaop.residual(stream,basis,caches,weights,z+epsilon*dz,config,recipe,area)
        minus=areaop.residual(stream,basis,caches,weights,z-epsilon*dz,config,recipe,area)
        fd=(plus-minus)/(2*epsilon)
        row=dict(epsilon=epsilon)
        for key,sl in (("complete",slice(None)),("original13",slice(0,original_rows)),
                       ("newPowerTwoArea",slice(original_rows,None))):
            row[key]=dict(relativeL2Error=float(np.linalg.norm((fd-jv)[sl])/max(1.,np.linalg.norm(jv[sl]))),
                maximumAbsoluteError=float(np.max(np.abs((fd-jv)[sl]))))
        checks.append(row)
    if max(checks[-1][key]["relativeL2Error"] for key in
           ("complete","original13","newPowerTwoArea"))>2e-5:
        raise ArithmeticError("Complete q=2 finite-difference fixture failed")
    direct=areaop.residual(stream,basis,caches,weights,z,config,recipe,area)
    if not np.array_equal(direct,linear.residual):
        raise ArithmeticError("The complete value and linearization row ordering differ")
    value,groups=areaop.observe(joint,stream,basis,caches,weights,z,config,recipe,area)
    cost=float(direct@direct)
    if abs(cost-value["squaredNorm"])>1e-12*max(1.,cost):
        raise ArithmeticError("Complete residual and own value cost mismatch")
    exact=np.zeros((1,6,1,3));exact[:,1,0,0]=.5;exact[:,2,0,1]=1.
    threshold=areaop.AreaPacket(exact,np.ones((1,1)),np.ones((1,1)),.5)
    if np.any(threshold.residual) or np.any(threshold.gs) or np.any(threshold.gu):
        raise ArithmeticError("Declared zero generalized threshold derivative changed")
    report=dict(schema="6a65-new-area-power-two-complete-small-synthetic-fixture-v1",
        scriptSHA256=sha(__file__),areaOperatorSHA256=sha(args.area_source),
        sources={name:sha(args.scripts/name) for name in (
            "6a65-geometry-gap-window-cartesian.py","6a65-geometry-gap-window-two-grid-cartesian.py",
            "6a65-cartesian-complete-stream.py","6a65-cartesian-complete-point-operator.py")},
        actualRows=linear.shape[0],actualColumns=basis.dimension,actualNonzeroCorrection=True,
        allOriginal13RowsAndNewAreaRow=True,allRealPeriodicColumns=True,
        actualSharedPreconditionerAdjointRelativeError=adj,finiteDifference=checks,
        actualOwnSquaredNorm=cost,actualMinAreaRatio=value["areaBarrierStatistics"]["minAreaRatio"],
        activeAreaPoints=value["areaBarrierStatistics"]["activePoints"],
        totalAreaPoints=value["areaBarrierStatistics"]["pointCount"],
        minimumAreaPoint=value["areaBarrierStatistics"]["minimumPoint"],
        residualValuesExactlyMatched=True,thresholdConventionChecked=True,
        seconds=time.monotonic()-begun,notAResearchState=True,acceptedResearchSteps=0,
        continuousCertificate=False,strongTargetComplete=False,
        OSExitCode=None,externalExitReceiptRequired=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(report,allow_nan=False),flush=True)


if __name__=="__main__":main()
