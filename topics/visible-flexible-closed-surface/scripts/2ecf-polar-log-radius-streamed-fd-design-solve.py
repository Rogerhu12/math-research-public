#!/usr/bin/env python3
"""Actual complete 12789 XYZ plus 87 C2 log-radius metric-design LM.

This is an explicitly new metric-design epoch. Moving alpha changes g;
neither decreases here nor input warm accepts are same-g convergence.
The final alpha must later be frozen for independent same-g refinement.
This consumer preserves the original full physical joint derivative; its
raw-direction finite-difference sweep reaches 1e-9/1e-10 and saves diagnostics
before applying the unchanged gate. The preceding short sweep failed and
is retained as a separate natural exit1, with zero nonlinear attempts.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

SCHEMA = '2ecf-polar-full-XYZ-C2-log-radius-new-metric-design-LM-v1'
OPERATOR_SHA = 'f44226464ba3cad0f2c69f7bd9b7d86befa9a311d7ec268e0d81e7a19f36b17c'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out


def write(path,value):
    path=Path(path)
    if path.exists():raise FileExistsError('Fresh actual design outputs required: '+str(path))
    path.write_text(json.dumps(value,separators=(',',':'),allow_nan=False)+'\n')
    return sha(path)


def emit(event,**values):
    print(json.dumps(dict(event=event,**values),allow_nan=False),flush=True)


def scalar(value):
    return dict(R2=value['squaredNorm'],metric=value['maxRelativeMetric'],
        curvature=value['maxCurvature'],sigma=value['areaBarrierStatistics']['minAreaRatio'],
        areaR2=value['areaBarrierStatistics']['squaredNorm'],held=value['minHeldDistance'])


def target_definition(base,basis,alpha,ports):
    return dict(schema=SCHEMA+'-single-provisional-target',baseSourceIdentity=base,
        radiusFormula='a=a0*exp(sum_i B_i alpha_i)',physicalSplineBasis=basis.definition,
        coefficients=[float(x) for x in alpha],exactCoefficientHex=[float(x).hex() for x in alpha],
        firstDerivative='exp(h)*(a0_s+a0*h_s)',
        secondDerivative='exp(h)*(a0_ss+2*a0_s*h_s+a0*(h_ss+h_s*h_s))',
        outsidePhysicalSupport='original a0 unchanged',support=[basis.c,basis.end],
        exactMathematicalEndpointTwoJetsUnchanged=True,sourcePorts=ports,
        positiveForEveryFiniteRealCoefficientVector=True,
        coefficientsStillProvisionalUntilDesignExplicitlyFrozen=True)


def port_records(basis,caches):
    ends=np.asarray([basis.c,basis.end])
    matrices=basis.matrices(ends)
    if any(np.any(B.toarray()!=0.) for B in matrices):
        raise ArithmeticError('Every actual endpoint basis two-jet must vanish')
    records={}
    for key,cache in caches.items():
        indices=np.searchsorted(cache.nodes,ends)
        if not np.array_equal(cache.nodes[indices],ends):
            raise ValueError('The complete physical source ports must actually be cached')
        records[key]=dict(physicalCoordinates=ends.tolist(),angles=cache.u.tolist(),
            radiusTwoJets=cache.radius[indices].tolist(),positionSixJets=cache.jets[indices].tolist(),
            actualEndpointCorrectionMatricesZero=True)
    return records


def run(args):
    started=time.monotonic()
    prepare=module(args.prepare_entry,'metric_design_prepare')
    prepared,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    if (basis.nb,basis.na,basis.dimension)!=(87,147,12789):
        raise ValueError('Complete current physical prefix space required')
    operator_path=Path(__file__).with_name('2ecf-polar-log-radius-operator.py')
    if sha(operator_path)!=OPERATOR_SHA:raise ValueError('Audited complete joint derivative changed')
    operator=module(operator_path,'metric_design_operator')
    deps=operator.dependencies(args.scripts);stream=mods['stream']
    stream_entry=Path(__file__).with_name('2ecf-polar-complete-two-grid-streamed.py')
    memory=module(stream_entry,'metric_design_actual_streamed_two_grid');memory.install(deps['joint'])
    config=stream.point.PointConfig(**definition['pointConfig'])
    recipe=copy.deepcopy(definition['recipe']);recipe['cachePointBlocks']=False
    area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    weights={k:{n:.5*np.asarray(v,float) for n,v in prepared['caches'][k]['weights'].items()} for k in caches}
    ports=port_records(basis,caches)
    model=dict(schema=SCHEMA+'-definition',preparedSHA256=sha(args.prepared),
        preparationEntrySHA256=sha(args.prepare_entry),solveEntrySHA256=sha(__file__),
        streamedPointEntrySHA256=sha(stream_entry),derivedPointPacketsRetained=False,
        unusedUnscaledNormalBandReleasedAfterFactor=True,
        jointOperatorEntrySHA256=OPERATOR_SHA,baseSourceIdentity=definition['sourceIdentity'],
        sourceMetadata=prepared['sourceMetadata'],positionSourceIndependentOfAlpha=True,
        sourcePorts=ports,basis=basis.definition,pointConfig=definition['pointConfig'],recipe=recipe,area=area,
        sourceCacheSHA256={key:prepared['caches'][key]['SHA256'] for key in caches},
        targetMetricDesign=dict(formula='a0*exp(B alpha)',radialColumns=87,
            preservesCompleteEndpointTwoJets=True,allPhysicalWeightsAndPointGuidesIndependentOfAlpha=True,
            metricQuarticAmplificationDerivativeIncluded=True,activeQ2AreaRadiusDerivativeIncluded=True,
            curvatureAndGeometryDependOnXNotTargetRadius=True,
            allCartesianRadiusNormalCrossTermsRetained=True),
        CartesianColumns=12789,totalColumns=12876,allFourteenRowsAtEveryPoint=True,
        parameterOrder='each radial row: all147Cartesian channels, then one log-radius coefficient',
        incrementDamping='original physical Cartesian H2 and same k=0 radial H2 for alpha',
        derivativeAudit=dict(rawEuclideanProbeSeed=2026112819,
            finiteDifferenceSteps=[1e-6,1e-7,1e-8,1e-9,1e-10],
            adjointGate=1e-10,relativeFDGate=2e-5,saveBeforeGate=True),
        initialDamping=args.initial_damping,dampingBounds=[1e-12,1e4],
        dampingUpdate='accepted full gain>.75 divide3; short or gain<.25 multiply2; rejection multiply10',
        targetMetricChangesDuringDesign=True,sameMetricContinuationClaim=False,
        allMetricDesignAcceptsCountedSeparately=True,wholeClosedReachCertified=False)
    model_sha=canonical(model);own=attempts=0;damping=args.initial_damping;checks=None
    if args.state:
        saved=json.loads(args.state.read_text())
        if (saved.get('schema')!=SCHEMA+'-state' or saved['modelDefinitionSHA256']!=model_sha
                or saved['modelDefinition']!=model):
            raise ValueError('The exact same metric-design epoch is required')
        z=np.asarray(saved['z'],float).reshape(87,147);alpha=np.asarray(saved['logRadiusCoefficients'],float)
        own,attempts=saved['ownMetricDesignAcceptedSteps'],saved['ownMetricDesignAttempts']
        provenance=saved['initialProvenance'];checks=saved['actualCompleteDerivativeCheck'];damping=saved['nextDamping']
    elif args.warm_state:
        old=json.loads(args.warm_state.read_text());oldmodel=old['modelDefinition']
        allowed={
            '2ecf-polar-C2-G10-same-g-full-normal-LM-v1-state':'2ecf-polar-c2-g10-solve.py',
            '2ecf-polar-C2-full-prefix-fixed-g-full-normal-LM-v1-state':'2ecf-polar-c2-prefix-solve.py',
            '2ecf-polar-C2-independent-zero-source-fixed-g-full-normal-LM-v1-state':'2ecf-polar-c2-prefix-zero-solve.py'}
        if (old.get('schema') not in allowed or canonical(oldmodel)!=old['modelDefinitionSHA256']
                or oldmodel['basis']!=basis.definition or oldmodel['pointConfig']!=definition['pointConfig']
                or oldmodel['sourceIdentity']!=definition['sourceIdentity']
                or oldmodel['solveEntrySHA256']!=sha(Path(__file__).with_name(allowed[old['schema']]))
                or old['preparedSHA256'] not in (sha(args.prepared),prepared['parentPreparedSHA256'])):
            raise ValueError('Exact actual warm Cartesian field with the identical base target is required')
        z=np.asarray(old['z'],float).reshape(87,147).copy();alpha=np.zeros(87)
        if z.ravel().tolist()!=old['z']:raise ArithmeticError('Warm Cartesian coefficients changed')
        provenance=dict(kind='copy all12789 actual Cartesian coefficients; all87 new alpha coefficients zero',
            parentSHA256=sha(args.warm_state),parentSchema=old['schema'],parentPreparedSHA256=old['preparedSHA256'],
            parentAcceptedSteps=old['ownExtendedAcceptedSteps'],parentCountsBorrowedAsNew=False,
            newDesignBaselinePaidIndependently=True)
    elif args.zero:
        z=np.zeros((87,147));alpha=np.zeros(87)
        provenance=dict(kind='actual source zero XYZ and zero log-radius, independent new metric-design epoch',
            parentCountsBorrowedAsNew=False)
    else:raise ValueError('An explicit actual warm state or independent zero is required')
    if (not np.all(np.isfinite(z)) or alpha.shape!=(87,) or not np.all(np.isfinite(alpha))
            or type(own)is not int or type(attempts)is not int or not 0<=own<=attempts):
        raise ValueError('Complete finite physical coefficients and honest counters required')
    def observe(zz,aa):
        cc={k:operator.LogRadiusCache(basis,c,aa) for k,c in caches.items()}
        return deps['area'].observe(deps['joint'],stream,basis,cc,weights,zz,config,recipe,area)
    def residual(zz,aa):
        cc={k:operator.LogRadiusCache(basis,c,aa) for k,c in caches.items()}
        return deps['area'].residual(stream,basis,cc,weights,zz,config,recipe,area)
    value,groups=observe(z,alpha);prefix=args.prefix.resolve();parent_sha=None if args.state is None else sha(args.state)
    def state_common():
        target=target_definition(definition['sourceIdentity'],basis,alpha,ports)
        return dict(schema=SCHEMA+'-state',modelDefinition=model,modelDefinitionSHA256=model_sha,
            initialProvenance=provenance,preparedSHA256=sha(args.prepared),z=z.ravel().tolist(),
            logRadiusCoefficients=alpha.tolist(),provisionalMetricDefinition=target,
            provisionalMetricDefinitionSHA256=canonical(target),
            targetMetricIsBeingDesigned=True,sameMetricConvergenceClaim=False,
            continuousMetricCertified=False,wholeClosedReachCertified=False)
    initial=dict(state_common(),ownMetricDesignAcceptedSteps=own,ownMetricDesignAttempts=attempts,
        accepted=False,parentStateSHA256=parent_sha,actualCompleteDerivativeCheck=checks,
        nextDamping=damping,evaluation=value,groupValues=groups)
    initial_sha=write(str(prefix)+'-initial.json',initial)
    emit('actual_metric_design_initial',SHA256=initial_sha,columns=12876,rows=value['rowCount'],
        ownAcceptedSteps=own,alphaInfinityNorm=float(np.max(abs(alpha))),**scalar(value))
    outputs=[]
    for step in range(1,args.steps+1):
        linear=operator.FullDesignLinear(deps,stream,basis,caches,weights,z,alpha,config,recipe,area)
        baseline=linear.statistics;gradient=linear.transpose(linear.residual)
        if checks is None:
            rng=np.random.default_rng(2026112819);direction=rng.standard_normal(12876);direction/=np.linalg.norm(direction)
            dz,da=linear.split(direction);jv=linear.matvec(direction);cot=rng.standard_normal(linear.shape[0])
            lhs,rhs=float(jv@cot),float(direction@linear.transpose(cot));adjoint=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
            fd=[]
            for epsilon in (1e-6,1e-7,1e-8,1e-9,1e-10):
                plus=residual(z+epsilon*dz,alpha+epsilon*da);minus=residual(z-epsilon*dz,alpha-epsilon*da)
                error=float(np.linalg.norm((plus-minus)/(2*epsilon)-jv)/max(1.,np.linalg.norm(jv)))
                fd.append(dict(epsilon=epsilon,relativeL2=error));del plus,minus
                if error<2e-5:break
            checks=dict(actualRows=linear.shape[0],actualColumns=12876,
                actualCartesianColumns=12789,actualRadiusColumns=87,adjointRelativeError=adjoint,
                jointFiniteDifferences=fd,allOriginal13AndQ2Rows=True,actualNonzeroCartesianField=bool(np.any(z)),
                actualAlphaInfinityNorm=float(np.max(abs(alpha))))
            write(str(prefix)+'-actual-derivative-check.json',checks)
            emit('actual_metric_design_complete_J_JT_check',**checks)
            if adjoint>1e-10 or error>2e-5:raise ArithmeticError('Actual full joint derivative failed')
            del direction,dz,da,jv,cot
        trace=[];accepted=False;selected=None;factor=None
        for attempt in range(1,7):
            if factor is not None:del factor;gc.collect()
            tick=time.monotonic();factor=operator.FullDesignNormal(linear,damping)
            released=factor.unscaled_band.nbytes;del factor.unscaled_band;gc.collect()
            emit('actual_unused_design_normal_storage_released',bytes=released,
                completeRowsRetained=linear.shape[0],columns=12876)
            direction=-factor.solve(gradient);nr=factor.residual(direction)
            relative=float(np.linalg.norm(nr)/max(1e-300,np.linalg.norm(gradient)));refinements=[]
            for unused in range(3):
                if relative<=1e-10:break
                direction-=factor.solve(nr);nr=factor.residual(direction)
                relative=float(np.linalg.norm(nr)/max(1e-300,np.linalg.norm(gradient)));refinements.append(relative)
            if relative>1e-7:raise ArithmeticError('Actual complete physical design normal residual unresolved')
            image=linear.matvec(direction);slope=float(gradient@direction);j2=float(image@image)
            dz,da=linear.split(direction)
            row=dict(kind='actual_complete_joint_physical_normal',damping=damping,attempt=attempt,
                assembly=factor.receipt,originalPhysicalNormalRelativeResidual=relative,
                refinementResiduals=refinements,slope=slope,predictedFullStepReduction=-2*slope-j2,
                radiusDirectionInfinityNorm=float(np.max(abs(da))),seconds=time.monotonic()-tick)
            trace.append(row);emit('actual_metric_design_full_normal',**{k:v for k,v in row.items() if k!='assembly'})
            if slope<0 and -2*slope-j2>0:
                for length in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
                    try:
                        trial,trialgroups=observe(z+length*dz,alpha+length*da)
                        ok=(trial['squaredNorm']<baseline['squaredNorm'] and trial['squaredNorm']<=baseline['squaredNorm']+2e-4*length*slope)
                        tr=dict(kind='actual_full_metric_design_trial',damping=damping,stepLength=length,
                            accepted=bool(ok),alphaInfinityNorm=float(np.max(abs(alpha+length*da))),**scalar(trial))
                        trace.append(tr);emit('actual_metric_design_trial',**tr)
                        if ok:
                            gain=(baseline['squaredNorm']-trial['squaredNorm'])/(-2*length*slope-length*length*j2)
                            z,alpha=z+length*dz,alpha+length*da;value,groups=trial,trialgroups;accepted=True;selected=length
                            nextdamping=max(1e-12,damping/3) if length==1 and gain>.75 else min(1e4,2*damping) if length<1 or gain<.25 else damping
                            break
                    except (ValueError,ArithmeticError,FloatingPointError) as error:
                        tr=dict(kind='actual_design_domain_rejection',stepLength=length,damping=damping,error=str(error),accepted=False)
                        trace.append(tr);emit('actual_metric_design_trial',**tr)
            if accepted:break
            damping=min(1e4,damping*10)
        attempts+=1;own+=int(accepted)
        if not accepted:gain=None;nextdamping=damping
        current=dict(state_common(),ownMetricDesignAcceptedSteps=own,ownMetricDesignAttempts=attempts,
            accepted=accepted,parentStateSHA256=parent_sha,newDesignInitialSHA256=initial_sha,
            stepLength=selected,dampingUsed=damping,nextDamping=nextdamping,
            actualToPredictedReduction=gain,actualCompleteDerivativeCheck=checks,
            baseline=baseline,evaluation=value,groupValues=groups,trace=trace)
        path=Path(str(prefix)+f'-step{step:02d}-state.json');parent_sha=write(path,current)
        outputs.append(dict(path=str(path),SHA256=parent_sha,accepted=accepted,ownAcceptedSteps=own,
            provisionalMetricDefinitionSHA256=current['provisionalMetricDefinitionSHA256'],**scalar(value)))
        emit('actual_metric_design_state',SHA256=parent_sha,accepted=accepted,ownAcceptedSteps=own,
            alphaInfinityNorm=float(np.max(abs(alpha))),nextDamping=nextdamping,seconds=time.monotonic()-started,**scalar(value))
        damping=nextdamping;del factor,linear,gradient,direction,nr,image,dz,da;gc.collect()
        if not accepted:break
    report=dict(schema=SCHEMA+'-report',modelDefinitionSHA256=model_sha,
        ownMetricDesignAcceptedSteps=own,ownMetricDesignAttempts=attempts,
        newAcceptsThisProcess=sum(int(x['accepted']) for x in outputs),outputs=outputs,
        parentWarmStateSHA256=None if args.warm_state is None else sha(args.warm_state),
        inputStateSHA256=None if args.state is None else sha(args.state),seconds=time.monotonic()-started,
        targetMetricStillBeingDesigned=True,sameMetricConvergenceClaim=False,
        continuousMetricCertified=False,wholeClosedReachCertified=False)
    digest=write(str(prefix)+'-report.json',report)
    emit('actual_metric_design_process_complete',SHA256=digest,ownAcceptedSteps=own,seconds=report['seconds'])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scripts',type=Path,required=True)
    ap.add_argument('--prepare-entry',type=Path,default=Path(__file__).with_name('2ecf-polar-c2-g10-resume-prepare.py'))
    ap.add_argument('--prepared',type=Path,required=True);ap.add_argument('--prefix',type=Path,required=True)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--state',type=Path);group.add_argument('--warm-state',type=Path);group.add_argument('--zero',action='store_true')
    ap.add_argument('--steps',type=int,default=1);ap.add_argument('--initial-damping',type=float,default=1e-4)
    args=ap.parse_args()
    if not 0<=args.steps<=20 or not math.isfinite(args.initial_damping) or args.initial_damping<=0:
        raise ValueError('Explicit finite batch and positive damping required')
    if args.scripts.parents[2] in args.prefix.resolve().parents:raise ValueError('Raw states must remain outside Git')
    run(args)


if __name__=='__main__':main()
