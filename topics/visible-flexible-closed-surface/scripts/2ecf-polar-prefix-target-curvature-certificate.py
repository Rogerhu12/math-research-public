#!/usr/bin/env python3
"""Exact piecewise prefix target K bound for one actual saved alpha.

The base radius on the prefix has the published ellipse/S9/affine formula.
This certifies that target formula on its prefix pieces, not source rounding,
base-target seam compatibility, total position curvature, or whole reach.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,hashlib,importlib.util,json,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def split(control,t):
    levels=[list(control)]
    while len(levels[-1])>1:
        row=levels[-1];levels.append([(1-t)*a+t*b for a,b in zip(row[:-1],row[1:])])
    return [row[0] for row in levels],[row[-1] for row in levels[::-1]]

def derivative(control,width):
    n=len(control)-1
    return [n*(b-a)/width for a,b in zip(control[:-1],control[1:])]

def up(value):
    scale=1<<96;rounded=Q(-((-value.numerator*scale)//value.denominator),scale)
    return dict(exactUpper=str(rounded),displayUpper=float(rounded))

def main():
    ap=argparse.ArgumentParser()
    for key in ('scripts','state','ramp-master','coast-master','output'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--depth',type=int,default=5)
    args=ap.parse_args();start=time.monotonic()
    if args.output.exists():raise FileExistsError(args.output)
    if not 0<=args.depth<=10:raise ValueError('Finite declared exact subdivision depth required')
    state=json.loads(args.state.read_text());model=state['modelDefinition'];target=state['provisionalMetricDefinition']
    if (canonical(model)!=state['modelDefinitionSHA256'] or canonical(target)!=state['provisionalMetricDefinitionSHA256']
            or target['coefficients']!=state['logRadiusCoefficients'] or target['physicalSplineBasis']!=model['basis']):
        raise ValueError('Exact actual saved design model/target required')
    base=model['sourceMetadata'];hashes=base['sourceDefinition']['sourceHashes']
    for key,path in (('rampMaster',args.ramp_master),('coastMaster',args.coast_master),
        ('warm',args.scripts/'6a65-geometry-cauchy-unit-t-warm.py'),
        ('independentMetric',args.scripts/'6a65-geometry-nonfold-fixed-metric-value.py')):
        if sha(path)!=hashes[key]:raise ValueError('Original mathematical source provenance changed: '+key)
    with np.load(args.ramp_master,allow_pickle=False) as ramp:
        A,B,c,L,v=(Q(float(ramp[k])) for k in ('centralA','centralB','centralLength','ramp','v'))
    with np.load(args.coast_master,allow_pickle=False) as coast:
        coast_radius=Q(float(coast['exact_target_radius']))
    if not (A>=B>0 and c==Q(float(base['c'])) and L>0 and v>0 and coast_radius>0):
        raise ValueError('Actual positive ellipse/ramp/coast scalar inputs required')
    endpoint=Q(float(base['b']));basis=model['basis']
    if basis!=target['physicalSplineBasis'] or Q(float(basis['physicalDomain'][0]))!=c:
        raise ValueError('Exact unchanged physical target spline support required')
    correction=module(Path(__file__).with_name('2ecf-polar-c2-correction-bernstein-budget.py'),'prefix_target_exact_extraction')
    helper_path=args.scripts/'6a65-m12-local-bernstein-angular-metric-budget.py'
    helper=module(helper_path,'prefix_target_exact_boehm')
    coefficients=[[Q(float(x))] for x in state['logRadiusCoefficients']]
    pieces=correction.extract([Q(float(x)) for x in basis['physicalKnots']],coefficients,helper.insert_knot)
    # |ellipse velocity| >= B, hence its exact natural mean radius >= B.
    # S9 is increasing 0..1 and S9'=630*t^4*(1-t)^4 <= 630/256.
    # The same bounds cover both one-sided ramp/coast target jets.
    amin=min(B,coast_radius);asmax=v;assmax=v/L*Q(630,256)
    m1=m2=Q(0);rows=[];covered=c
    for lo,hi,full in pieces:
        if lo>=endpoint:break
        control=[row[0] for row in full]
        if hi>endpoint:
            control=split(control,(endpoint-lo)/(hi-lo))[0];hi=endpoint
        if lo!=covered:raise ArithmeticError('Whole prefix piece coverage failed')
        covered=hi;parts=[(lo,hi,control)]
        for unused in range(args.depth):
            nxt=[]
            for left,right,ctrl in parts:
                a,b=split(ctrl,Q(1,2));mid=(left+right)/2
                nxt.extend(((left,mid,a),(mid,right,b)))
            parts=nxt
        local1=local2=Q(0)
        for left,right,ctrl in parts:
            d1=derivative(ctrl,right-left);d2=derivative(d1,right-left)
            local1=max(local1,max(map(abs,d1)));local2=max(local2,max(map(abs,d2)))
        m1=max(m1,local1);m2=max(m2,local2)
        bound=assmax/amin+2*asmax/amin*local1+local2+local1*local1
        rows.append(dict(physicalSpanExact=[str(lo),str(hi)],subintervals=len(parts),
            hFirst=up(local1),hSecond=up(local2),targetGaussianAbsolute=up(bound)))
    if covered!=endpoint:raise ArithmeticError('Prefix did not reach the exact saved coast endpoint')
    bound=max(Q(r['targetGaussianAbsolute']['exactUpper']) for r in rows)
    guide=Q(float(model['pointConfig']['curvature_guide']))
    output=dict(schema='2ecf-actual-saved-alpha-exact-piecewise-prefix-target-K-bound-v1',
        entrySHA256=sha(__file__),stateSHA256=sha(args.state),modelDefinitionSHA256=state['modelDefinitionSHA256'],
        provisionalMetricDefinitionSHA256=state['provisionalMetricDefinitionSHA256'],
        baseSourceDefinitionSHA256=base['sourceDefinitionSHA256'],exactBoehmHelperSHA256=sha(helper_path),
        storedPhysicalKnotsAndAlphaInterpretedAsExactDyadics=True,
        originalBaseScalarRecipe='central natural ellipse radius; v*S9 ramp; fixed positive affine coast',
        exactBasePrefixBounds=dict(aLower=str(amin),absFirstUpper=str(asmax),absSecondUpper=str(assmax),
            proof='ellipse speed >= B; 0<=S9<=1; S9prime=630 t^4(1-t)^4<=630/256; affine coast'),
        exactCertificateDomain=dict(central=[0,float(c)],correctedPrefix=[float(c),float(endpoint)],
            centralGaussianCurvatureZero=True,prefixOneSidedPiecesAndAllInteriorPointsIncluded=True),
        exactHDerivativeBounds=dict(first=up(m1),second=up(m2)),
        exactPrefixTargetGaussianAbsoluteBound=up(bound),
        belowSquaredOwnCurvatureGuide=bool(bound<guide*guide),
        squaredOwnCurvatureGuideExact=str(guide*guide),spans=rows,
        finiteSamplesUsedToProveBounds=False,sourceFloatingPointEvaluationErrorCertified=False,
        baseTargetSeamCompatibilityCertified=False,connectorAndTailTargetKCertified=False,
        actualPositionPrincipalCurvatureCertified=False,wholeClosedReachCertified=False,
        optimizationAttempts=0,optimizationAccepts=0,seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(output,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual_exact_prefix_target_curvature_bound',
        prefixK=output['exactPrefixTargetGaussianAbsoluteBound'],
        h=output['exactHDerivativeBounds'],spans=len(rows),
        belowSquaredOwnCurvatureGuide=output['belowSquaredOwnCurvatureGuide'],seconds=output['seconds'])),flush=True)

if __name__=='__main__':main()
