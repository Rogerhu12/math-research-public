#!/usr/bin/env python3
"""Independent fixed-perimeter central gap, genuinely integrated 65 physical ramp nodes, new Gamma95."""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np
from scipy.integrate import solve_ivp


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def mod(path, name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj


def run(args):
    started=time.monotonic()
    budget_path=args.scripts/"6a65-geometry-central-gap-held-budget.py"
    warm_path=args.scripts/"6a65-geometry-cauchy-unit-t-warm.py"
    budget=mod(budget_path,"central_perimeter_gap_budget")
    warm=mod(warm_path,"new_gap_cauchy_warm")
    gap=Fraction(args.gap)
    exactA,exactB=budget.central_box(gap,denominator=10**17)
    A,B=(float(sum(x)/2) for x in (exactA,exactB))
    c,r,v,ell=13/128,.06,.045,.02
    candidate=warm.p.Candidate(A,B,r,v)
    flow=warm.p.hybrid.Hybrid(candidate,191,2,30000)
    y=flow.initial()
    y[flow.shape_size:].reshape(flow.work,12)[:,2]=c
    nodes=np.linspace(0,r,65)
    sol=solve_ivp(flow.rhs,(0,r),y,method="DOP853",rtol=2e-12,atol=2e-14/(1+flow.active_wave)**2,
        max_step=.0005,t_eval=nodes)
    if sol.status!=0 or not np.array_equal(sol.t,nodes):
        raise ArithmeticError("New physical Cauchy flow failed")
    coeff=[];row=[]
    for s,state in zip(nodes,sol.y.T):
        frame=flow.frame(float(s),state);native=np.asarray(frame["values"],float)
        acc=(native[:,1]**2+float(frame["K"]))/native[:,0]
        packet=np.stack((native[:,2:5],native[:,5:8],acc[:,None]*native[:,11:14]),axis=1)
        coeff.append(np.fft.fft(packet,axis=0)/flow.work)
        row.append(flow.diagnostics(float(s),state))
    ramp=Path(str(args.prefix)+"-ramp.npz")
    with ramp.open("xb") as ff:np.savez_compressed(ff,sx=nodes,coefficients=np.stack(coeff),wave=np.fft.fftfreq(flow.work,1/flow.work),
        centralA=A,centralB=B,centralLength=c,a0=candidate.ellipse.a0,ramp=r,v=v,modes=191)
    curve=warm.core.Curve(native[:,2:5],95)
    target=float(candidate.profile([r])[0][0])
    coast=Path(str(args.prefix)+"-coast.npz")
    with coast.open("xb") as ff:np.savez_compressed(ff,curve_modes=curve.modes,curve_coefficients=curve.coeff,
        unnormalized_radius=curve.a,exact_target_radius=target,v=v,length=ell,degree=95)
    report=dict(schema="new-physical-central-gap-Cauchy-H65-Gamma95-v1",requestedGap=str(gap),
        intervalAxesForIdealPerimeter=[[str(k) for k in iv] for iv in (exactA,exactB)],
        numericalAxes=[A,B],actualDyadicAxisHex=[A.hex(),B.hex()],
        numericalCentralMean=candidate.ellipse.a0,actualNumericalCentralCurvature=A/B**2,cutAndDevelopedTailUnchanged=True,
        warmSHA256=sha(warm_path),perimeterBudgetSHA256=sha(budget_path),entrySHA256=sha(__file__),
        rampSHA256=sha(ramp),coastSHA256=sha(coast),returnedDenseNodes=len(nodes),actualFFT=flow.work,
        nfev=sol.nfev,diagnosticsOnPhysicalIVPNodesOnly=dict(metric=max(k["metric"] for k in row),
        curvature=max(k["actual_curvature"] for k in row),minimumN=min(k["minimum_n"] for k in row)),
        wholePrefixCertified=False,seconds=time.monotonic()-started)
    with Path(str(args.prefix)+".json").open("x") as ff:json.dump(report,ff,indent=2);ff.write("\n")
    print(json.dumps(report),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--gap",required=True)
    run(ap.parse_args())
