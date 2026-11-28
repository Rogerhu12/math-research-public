#!/usr/bin/env python3
"""Saved metric-design target: actual K_g samples and exact h derivative hulls.

No position, objective, accepted step, or alpha is changed. Finite K_g samples
are distinct from exact scalar spline hull bounds. The latter do not supply
an unproved continuous bound on the independent base target a0.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def exact_spline_hulls(basis,alpha):
    knots=[Q(float(x)) for x in basis['physicalKnots']]
    control=[Q(0)]*3+[Q(float(x)) for x in alpha]+[Q(0)]*3
    if (basis['degree']!=5 or len(knots)!=len(control)+6
            or len(control)!=93 or knots[:6]!=[knots[0]]*6 or knots[-6:]!=[knots[-1]]*6):
        raise ValueError('Complete exact physical clamped quintic scalar basis required')
    if any(knots.count(t)>3 for t in sorted(set(knots))[1:-1]):
        raise ValueError('C2 internal scalar spline continuity required')
    rows=[];degree=5
    for order in range(4):
        lo,hi=min(control),max(control)
        rows.append(dict(order=order,exactLower=str(lo),exactUpper=str(hi),
            exactAbsoluteUpper=str(max(abs(lo),abs(hi))),displayAbsoluteUpper=float(max(abs(lo),abs(hi))),
            controls=len(control),allSpansAndBothOneSidedKnotLimitsCovered=True))
        if order<=2 and (control[0]!=0 or control[-1]!=0):
            raise ArithmeticError('Actual exact scalar endpoint two-jet trace failed')
        if order==3:break
        den=[knots[i+degree+1]-knots[i+1] for i in range(len(control)-1)]
        if any(x<=0 for x in den):raise ArithmeticError('Actual spline derivative denominator failed')
        control=[degree*(b-a)/d for a,b,d in zip(control[:-1],control[1:],den)]
        degree-=1;knots=knots[1:-1]
    return rows


def main():
    ap=argparse.ArgumentParser()
    for key in ('scripts','prepare-entry','prepared','state','output'):ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--observer',type=Path)
    args=ap.parse_args();start=time.monotonic()
    prepare=module(args.prepare_entry,'target_audit_prepare')
    saved,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    state=json.loads(args.state.read_text())
    if state['preparedSHA256']!=sha(args.prepared) or canonical(state['modelDefinition'])!=state['modelDefinitionSHA256']:
        raise ValueError('Actual same prepared and complete saved model required')
    designed='logRadiusCoefficients' in state
    if designed:
        if state['schema']!='2ecf-polar-full-XYZ-C2-log-radius-new-metric-design-LM-v1-state':
            raise ValueError('Explicit actual metric-design state required')
        alpha=np.asarray(state['logRadiusCoefficients'],float)
        target=state['provisionalMetricDefinition']
        if (canonical(target)!=state['provisionalMetricDefinitionSHA256'] or target['coefficients']!=alpha.tolist()
                or target['physicalSplineBasis']!=basis.definition):
            raise ValueError('The actual saved target g identity differs')
    else:alpha=np.zeros(basis.nb)
    if alpha.shape!=(87,) or not np.all(np.isfinite(alpha)):raise ValueError('Every finite target parameter required')
    inputs={name:(cache.nodes,cache.radius) for name,cache in caches.items()}
    if args.observer:
        obs=json.loads(args.observer.read_text())
        if obs['sourceIdentity']!=definition['sourceIdentity'] or obs['basis']!=basis.definition:
            raise ValueError('Actual independent target observer source differs')
        if sha(obs['files']['radius'])!=obs['SHA256']['radius']:raise ValueError('Actual observer target samples changed')
        inputs['independent']=(np.asarray(obs['physicalNodes']),np.load(obs['files']['radius'],mmap_mode='r'))
    rows={}
    for name,(nodes,base) in inputs.items():
        h,hs,hss=(matrix@alpha for matrix in basis.matrices(nodes))
        a0,a0s,a0ss=base.T;exp=np.exp(h)
        a=a0*exp;first=(a0s+a0*hs)*exp;second=(a0ss+2*a0s*hs+a0*(hss+hs*hs))*exp
        if not np.all(np.isfinite(a)) or not np.all(np.isfinite(second)) or np.min(a)<=0:
            raise ArithmeticError('The declared target is not finite positive on actual samples')
        curvature=-second/a;identity=-a0ss/a0-2*(a0s/a0)*hs-hss-hs*hs
        i=int(np.argmax(abs(curvature)))
        rows[name]=dict(radials=len(nodes),maxAbsoluteTargetGaussianCurvature=float(abs(curvature[i])),
            signedTargetGaussianCurvatureAtMaximum=float(curvature[i]),physicalSAtMaximum=float(nodes[i]),
            targetTwoJetAtMaximum=[float(a[i]),float(first[i]),float(second[i])],
            minTargetRadius=float(np.min(a)),maxTargetRadius=float(np.max(a)),
            maxAbsH=float(np.max(abs(h))),maxAbsHs=float(np.max(abs(hs))),maxAbsHss=float(np.max(abs(hss))),
            curvatureIdentityMaxRoundoff=float(np.max(abs(curvature-identity))),
            finiteSampleOnly=True,continuousTargetCurvatureBound=False)
    hulls=exact_spline_hulls(basis.definition,alpha)
    out=dict(schema='2ecf-saved-designed-target-finite-K-and-exact-log-spline-hulls-v1',
        preparedSHA256=sha(args.prepared),stateSHA256=sha(args.state),entrySHA256=sha(__file__),
        provisionalMetricDefinitionSHA256=state.get('provisionalMetricDefinitionSHA256'),
        metricDesignState=designed,ownMetricDesignAcceptedSteps=state.get('ownMetricDesignAcceptedSteps',0),
        ownFixedMetricAcceptedSteps=state.get('ownExtendedAcceptedSteps',0),
        targetFormula='a=a0 exp(h)',GaussianCurvatureFormula='K=K0-2(a0_s/a0)h_s-h_ss-h_s^2',
        finiteActualTargetObservations=rows,exactGlobalScalarSplineHulls=hulls,
        exactGlobalRadiusRatioBounds=dict(lowerExpression='exp('+hulls[0]['exactLower']+')',
            upperExpression='exp('+hulls[0]['exactUpper']+')',baseA0PositiveAssumedFromSameSourceDefinition=True),
        exactEndpointTwoJetsOfHZero=True,allParametersAndKnotsInterpretedAsExactStoredDyadics=True,
        noPositionOrMetricParameterChanged=True,notUsedToAlterOriginal14RowObjective=True,
        continuousTargetCurvatureCertified=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start)
    if args.output.exists():raise FileExistsError('Fresh actual target audit required')
    args.output.write_text(json.dumps(out,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual_saved_target_audit',SHA256=sha(args.output),
        finiteObservations=rows,exactScalarSplineHulls=hulls,seconds=out['seconds'])),flush=True)


if __name__=='__main__':main()
