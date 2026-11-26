#!/usr/bin/env python3
"""Nonzero full-space transfer, independent rational basis and free-port check."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rational_basis(knots,x,derivative):
    """Independent exact Cox recurrence on the actual binary64 knot rationals."""
    t=tuple(Fraction(float(v)) for v in knots);q=Fraction(float(x))
    if q<t[0] or q>t[-1]:return [Fraction(0)]*(len(t)-6)
    @lru_cache(None)
    def b(i,p,d):
        if d>p:return Fraction(0)
        if p==0:
            return Fraction(int(t[i]<=q<t[i+1] or
                (q==t[-1] and t[i]<t[i+1]==q)))
        left=t[i+p]-t[i];right=t[i+p+1]-t[i+1]
        if d:
            return ((p*b(i,p-1,d-1)/left if left else 0)
                -(p*b(i+1,p-1,d-1)/right if right else 0))
        return (((q-t[i])*b(i,p-1,0)/left if left else 0)
            +((t[i+p+1]-q)*b(i+1,p-1,0)/right if right else 0))
    return [b(i,5,derivative) for i in range(len(t)-6)]


def direct_trigonometric_packet(basis,matrices,z,u):
    amplitudes=[m@z for m in matrices]
    out=np.zeros((len(amplitudes[0]),6,len(u),3))
    for column,(component,k,kind) in enumerate(basis.channels):
        theta=k*u
        if kind=='cos':v0=np.cos(theta);v1=-k*np.sin(theta)
        else:v0=np.sin(theta);v1=k*np.cos(theta)
        v2=-(k*k)*v0
        for jet,rad,angle in ((0,0,v0),(1,1,v0),(2,0,v1),(3,2,v0),(4,1,v1),(5,0,v2)):
            out[:,jet,:,component]+=amplitudes[rad][:,column,None]*angle
    return out


def main():
    ap=argparse.ArgumentParser()
    for name in ('scripts','helper','output'):ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():raise FileExistsError('Fresh finite interface output required')
    start=time.monotonic()
    stream=load(args.scripts/'6a65-cartesian-complete-stream.py','c2_actual_stream')
    base=load(args.scripts/'6a65-geometry-gap-window-cartesian.py','c2_actual_base')
    refined=load(args.scripts/'6a65-geometry-gap-window-refined-cartesian.py','c2_actual_refinement')
    helper=load(args.helper,'c2_new_helper')
    c=.1015625;b=.1815625;end=.9772364498716914
    coarse=base.periodic_basis(stream,b,end,32,12)
    old,_=refined.refined_basis(base,stream,coarse)
    assert old.dimension==5292
    left=np.r_[c+np.arange(17)*(.06/16),b];left[0]=c;left[-1]=b
    new,mapping=helper.extend_left_c2(old,left,[3]*16)
    # Full declared 5292-column coefficient vector: every entry is nonzero.
    values=np.arange(1,old.dimension+1,dtype=float)
    z=(1e-8*(1+values%19)*np.where(values.astype(int)%2,1.,-1.)).reshape(old.nb,old.na)
    znew,transfer=helper.prolongate_exact(old,new,z)
    assert np.count_nonzero(z)==old.dimension and np.all(znew[:new.nb-old.nb]==0)
    probes=np.unique(np.r_[new.breaks,(new.breaks[:-1]+new.breaks[1:])/2,
        b-1e-9,b,b+1e-9,c-.001,end+.001])
    N=128;u=2*np.pi*np.arange(N)/N
    old_matrices=old.matrices(probes);new_matrices=new.matrices(probes)
    before=direct_trigonometric_packet(old,old_matrices,z,u)
    after=new.packet(new_matrices,znew,N)
    errors=np.max(np.abs(before-after),axis=(0,2,3))
    scales=np.max(np.abs(before),axis=(0,2,3))
    if np.any(errors>3e-12*np.maximum(1.,scales)):
        raise ArithmeticError('Transferred actual six-jet field changed')
    exact_checks=0
    for x in (c,(c+b)/2,b,(b+old.breaks[1])/2,old.breaks[12],(old.breaks[-2]+end)/2,end):
        for d in range(3):
            a=rational_basis(old.knots,x,d)
            q=rational_basis(new.knots,x,d)
            for row,target in enumerate(mapping):
                if a[row+3]!=q[target+3]:
                    raise ArithmeticError('Independent rational old/new B-spline identity failed')
                exact_checks+=1
    # Raw endpoint derivatives: do not rely on matrices() forcing endpoint rows to zero.
    endpoint=[]
    for d in range(3):
        raw=new._spline(np.array([c,end]),nu=d)[:,3:-3]
        endpoint.append(float(np.max(np.abs(raw))))
    if max(endpoint)!=0:raise ArithmeticError('Outer endpoint two jets changed')
    h=b-c
    trace=np.stack([new._spline(b,nu=d)[3:-3]*h**d for d in range(3)])
    singular=np.linalg.svd(trace,compute_uv=False)
    if singular[-1]<=1e-8:raise ArithmeticError('Former port two-jet map is not surjective')
    target=np.array([.17,-.23,.31]);v=np.linalg.lstsq(trace,target,rcond=None)[0]
    trace_error=float(np.max(np.abs(trace@v-target)))
    if trace_error>1e-12:raise ArithmeticError('Free-port trace construction failed')
    if np.any(trace[:,new.nb-old.nb:]!=0):
        raise ArithmeticError('Inherited old correction no longer clamps the old port')
    # Two positive Gauss points in each active knot span make the original H2
    # discrete Sobolev matrix positive: a quintic with two triple zeros is zero.
    xg,wg=np.polynomial.legendre.leggauss(2)
    a=new.breaks[:-1];d=new.breaks[1:]
    nodes=((a+d)[:,None]/2+(d-a)[:,None]*xg/2).ravel()
    weights=((d-a)[:,None]*wg/2).ravel()
    sobolev=stream.BandedSobolev(new,nodes,weights,
        dict(kind='banded_sobolev_h2',beta0=.01,beta1=1.,beta2=.001))
    actual_factor_count=len(sobolev.factors)
    # Negative identity and non-C2 receiver cases are relevant to actual input safety.
    rejected=0
    for breaks,mults in (([c,b+1e-7],None),([c,c,b],None),(left,[4]*16),(left,[1.5]*16)):
        try:helper.extend_left_c2(old,breaks,mults)
        except ValueError:rejected+=1
    if rejected!=4:raise ArithmeticError('Invalid new physical space was accepted')
    result=dict(schema='6a65-C2-support-extension-nonzero-finite-interface-v1',
        sourceSHA256=sha(__file__),helperSHA256=sha(args.helper),
        dependencies={p:sha(args.scripts/p) for p in (
            '6a65-cartesian-complete-stream.py','6a65-geometry-gap-window-cartesian.py',
            '6a65-geometry-gap-window-refined-cartesian.py')},
        syntheticNonzeroCoefficients=True,actualResearchStateUsed=False,
        oldRadialBasis=old.nb,newRadialBasis=new.nb,angularChannels=new.na,
        physicalDomain=[c,end],formerPort=b,leftInteriorKnots=16,
        leftInteriorMultiplicity=3,formerPortMultiplicity=3,
        transfer=transfer,actualSixJetProbeCount=len(probes)*N,
        maximumSixJetError=errors.tolist(),oldSixJetScales=scales.tolist(),
        independentExactRationalBasisComparisons=exact_checks,
        exactRationalComparisonFailures=0,rawOuterEndpointDerivatives=endpoint,
        scaledFormerPortTraceSingularValues=singular.tolist(),
        freeFormerPortTwoJetTarget=target.tolist(),freeTraceMaximumError=trace_error,
        originalSobolevAllModesFactorized=True,actualSobolevFactorCount=actual_factor_count,
        positiveGaussNodesPerSpan=2,rejectedInvalidSpaceDefinitions=rejected,
        actualNonlinearAcceptedSteps=0,targetMetricChanged=False,
        continuousNonlinearGeometryCertified=False,seconds=time.monotonic()-start)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,allow_nan=False),flush=True)
    print(json.dumps(dict(outputSHA256=sha(args.output))),flush=True)


if __name__=='__main__':main()
