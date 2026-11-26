#!/usr/bin/env python3
"""New full fixed-g Cartesian LM with an inverse-square-area residual.

All 5292 columns and original 13 rows on both frozen source grids are kept.
The added power-two reciprocal-area row has its own complete baseline/counter and
reports the original 13-row cost separately on every actual trial.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import copy
from dataclasses import asdict
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
import numpy as np
from scipy.sparse.linalg import lsmr

SCHEMA="6a65-gap105-complete14-reciprocal-area-power-two-fixed-g-Cartesian-v1"
ORIGINAL_AREA_SCHEMA="6a65-gap105-complete14-reciprocal-area-fixed-g-Cartesian-v1"
ORIGINAL_AREA_ENTRY_SHA="6ae25fd9bd29920692794ea12808a634ff4e0a9a6e31502fe346cfa2eea13397"
HASHES=dict(base="ca22b417066c3e7f46470b876eabb57ed4d1673858000d31d4c99d8acc3f2f86",
    joint="26b53da871749b90358cef659dc8c23621f649061e0a65b4b9a7f500a05398b3",
    refined="1596f0f40bbc19aabd4ea28a51a516d1bbfb86cca35f8ff03ae6d34f7349acb1",
    area="d8fb8710d4957430b66b474d79a61d3b7bf4fff9915bba1d62ecfea0f96ee97e")


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()


def write(path,value):
    path=Path(path)
    if path.exists():
        raise FileExistsError("Fresh actual area-model output required")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n")
    return sha(path)


def emit(event,**value):
    print(json.dumps(dict(event=event,**value),allow_nan=False),flush=True)


def scalars(value):
    return dict(R2=value["squaredNorm"],original13R2=value["originalThirteenRowStatistics"]["squaredNorm"],
        areaR2=value["areaBarrierStatistics"]["squaredNorm"],
        metric=value["maxRelativeMetric"],curvature=value["maxCurvature"],
        eta=value["minImmersion"],areaRatio=value["areaBarrierStatistics"]["minAreaRatio"],
        held=value["minHeldDistance"],
        minimumAreaPoint=value["areaBarrierStatistics"]["minimumPoint"],
        worstMetric=value["worstMetric"],worstCurvature=value["worstCurvature"])


def run(args):
    started=time.monotonic()
    paths=dict(base=args.base_entry,joint=args.joint_entry,refined=args.refined_entry,area=args.area_source)
    for name,path in paths.items():
        if sha(path)!=HASHES[name]:
            raise ValueError("Frozen complete source changed: "+name)
    base=module(args.base_entry,"gap_area_base")
    joint=module(args.joint_entry,"gap_area_joint")
    refinement=module(args.refined_entry,"gap_area_refinement")
    areaop=module(args.area_source,"gap_area_complete_operator")
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","gap_area_stream")
    background=module(args.background,"gap_area_background")
    prepared,definition,oldbasis,caches=base.validate_prepared(args,stream,background)
    basis,_=refinement.refined_basis(base,stream,oldbasis)
    prefix=args.prefix.resolve()
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh actual area-model prefix required")
    recipe=copy.deepcopy(definition["recipe"])
    recipe["lsmr"]["maxIterations"]=160
    recipe["basis"].update(radialBasisCount=basis.nb,maxAngularFrequency=basis.M,
        physicalKnotsAuthoritative=True,localKnotRefinement=True)
    area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2,
        formula="sqrt(frozen original metric quadrature weight) * max(0, (.5/sigma)^2-1)",
        sigma="|Xs cross Xu|/a; a is the frozen target metric radius",
        hingeDerivativeAtEquality=0.,positiveAreaDomainRequiredAtEveryActualPoint=True,
        allOriginalThirteenRowsPreserved=True,continuousAreaLowerBoundCertified=False)
    model=dict(preparedSHA256=sha(args.prepared),preparedDefinitionSHA256=prepared["definitionSHA256"],
        sourceIdentity=definition["sourceIdentity"],basis=basis.definition,recipe=recipe,
        pointConfig=definition["pointConfig"],operatorSources=definition["operatorSources"],
        newSources=HASHES,entrySHA256=sha(__file__),operatorSourceEpoch=args.operator_epoch,areaBarrier=area,
        quadrature=dict(trainingScale=.5,observerScale=.5,unchangedCompleteGrids=True,
            originalThirteenRowsUnchanged=True,newAreaWeights="original metric weights"),
        continuousQuadratureAccuracyClaimed=False)
    model_sha=canonical(model)
    state=json.loads(args.state.read_text())
    if (state.get("preparedSHA256")!=sha(args.prepared) or state.get("targetMetricFrozen") is not True or
        state.get("basis")!=basis.definition or state.get("pointConfig")!=definition["pointConfig"] or
        state.get("sourceIdentity")!=definition["sourceIdentity"]):
        raise ValueError("Actual full refined parent must bind the same source, g and 5292-column space")
    if state.get("schema")==refinement.SCHEMA+"-checkpoint":
        if (state.get("entrySHA256")!=HASHES["refined"] or
            canonical(state["modelDefinition"])!=state["modelDefinitionSHA256"] or
            state["modelDefinition"]["preparedDefinitionSHA256"]!=prepared["definitionSHA256"]):
            raise ValueError("Actual full refined parent changed identity")
        carried=state["actualTotalCartesianAcceptedSteps"]
        own=attempt_count=0
    elif state.get("schema")==ORIGINAL_AREA_SCHEMA+"-checkpoint":
        if (state.get("entrySHA256")!=ORIGINAL_AREA_ENTRY_SHA or
            canonical(state["modelDefinition"])!=state["modelDefinitionSHA256"] or
            state["modelDefinition"]["preparedDefinitionSHA256"]!=prepared["definitionSHA256"]):
            raise ValueError("Actual previous power-one area checkpoint changed identity")
        carried=state["actualTotalCartesianAcceptedSteps"]
        own=attempt_count=0
    elif state.get("schema")==SCHEMA+"-checkpoint":
        if state.get("modelDefinitionSHA256")!=model_sha or state.get("entrySHA256")!=sha(__file__):
            raise ValueError("Continued area-model definition changed")
        carried=state["carriedOriginalModelAcceptedSteps"]
        own=state["areaPowerTwoAcceptedSteps"]
        attempt_count=state["areaPowerTwoAttemptCount"]
    else:
        raise ValueError("Actual refined, original power-one area, or same power-two checkpoint required")
    z=np.asarray(state["z"],float).reshape(basis.nb,basis.na)
    if not np.all(np.isfinite(z)):
        raise ValueError("Finite complete actual coefficients required")
    weights={key:{name:.5*np.asarray(value,float) for name,value in prepared["caches"][key]["weights"].items()}
             for key in caches}
    config=stream.point.PointConfig(**definition["pointConfig"])
    value,groups=areaop.observe(joint,stream,basis,caches,weights,z,config,recipe,area)
    parent_sha=sha(args.state)
    common=dict(schema=SCHEMA+"-checkpoint",modelDefinition=model,modelDefinitionSHA256=model_sha,
        sourceIdentity=definition["sourceIdentity"],preparedSHA256=sha(args.prepared),entrySHA256=sha(__file__),
        basis=basis.definition,dimension=basis.dimension,pointConfig=asdict(config),
        correctionSupport=definition["correctionSupport"],targetMetricFrozen=True,
        allOriginalThirteenRowsRetained=True,all5292ColumnsRetained=True,
        entirePrefixPreserved=True,trueR205TailAndCuffFixed=True,
        newObjectiveComparedOnlyWithItsOwnBaseline=True,areaBarrier=area,
        continuousCertificate=False,strongTargetComplete=False)
    initial=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_sha,accepted=False,
        carriedOriginalModelAcceptedSteps=carried,areaPowerTwoAcceptedSteps=own,areaPowerTwoAttemptCount=attempt_count,
        actualTotalCartesianAcceptedSteps=carried+own,evaluation=value,groupValues=groups,
        actualOwnAreaModelBaseline=True,previousModelEvaluation=state["evaluation"])
    initial_sha=write(str(prefix)+"-initial.json",initial)
    emit("area_power_two_actual_initial",initialSHA256=initial_sha,columns=basis.dimension,rows=value["rowCount"],
        actualCarriedSteps=carried,areaPowerTwoAcceptedSteps=own,**scalars(value))
    outputs=[];check=None;damping=recipe["lm"]["damping"]
    for iteration in range(1,args.steps+1):
        linear=areaop.CompleteAreaTwoGrid(joint,stream,basis,caches,weights,z,config,recipe,area)
        baseline=linear.statistics
        if check is None:
            rng=np.random.default_rng(20261129)
            direction=rng.normal(size=linear.shape[1]);direction/=np.linalg.norm(direction)
            cotangent=rng.normal(size=linear.shape[0])
            jv=linear.matvec(direction)
            lhs=float(jv@cotangent);rhs=float(direction@linear.rmatvec(cotangent))
            adjoint_error=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
            if adjoint_error>1e-10:
                raise ArithmeticError("Actual full 14-row shared-column adjoint failed")
            dz=linear.unpack(direction)
            checks=[]
            for epsilon in (1e-6,1e-7):
                plus=areaop.residual(stream,basis,caches,weights,z+epsilon*dz,config,recipe,area)
                minus=areaop.residual(stream,basis,caches,weights,z-epsilon*dz,config,recipe,area)
                fd=(plus-minus)/(2*epsilon)
                relative=float(np.linalg.norm(fd-jv)/max(1.,np.linalg.norm(jv)))
                checks.append(dict(epsilon=epsilon,relativeL2Error=relative,
                    maximumAbsoluteError=float(np.max(np.abs(fd-jv))),actualNonzeroField=True))
                del plus,minus,fd
                if relative<=2e-5:
                    break
            if checks[-1]["relativeL2Error"]>2e-5:
                raise ArithmeticError("Actual complete new nonlinear residual direction check failed")
            check=dict(completeColumns=linear.shape[1],completeRows=linear.shape[0],
                adjointRelativeDotError=adjoint_error,finiteDifference=checks,
                sourceStateNonzero=True,allOriginalAndAreaRowsIncluded=True,
                hingeConvention="zero generalized derivative at sigma=.5",continuumCertificate=False)
            emit("area_power_two_actual_complete_derivative_check",**check)
            del direction,cotangent,jv,dz
            gc.collect()
        gradient=linear.rmatvec(linear.residual)
        trace=[];accepted=False;selected=None
        for attempt in range(1,recipe["lm"]["maxDampingAttempts"]+1):
            tick=time.monotonic()
            r=lsmr(linear.operator,-linear.residual,damp=math.sqrt(damping),
                atol=recipe["lsmr"]["atol"],btol=recipe["lsmr"]["btol"],
                conlim=recipe["lsmr"]["conditionLimit"],maxiter=recipe["lsmr"]["maxIterations"])
            y=r[0]
            if not np.all(np.isfinite(y)):
                raise ArithmeticError("Actual full14 direction is nonfinite")
            dz=linear.unpack(y);jv=linear.matvec(y);slope=float(gradient@y)
            predicted=float(-2*slope-jv@jv)
            row=dict(kind="actual_complete14_LSMR",attempt=attempt,damping=damping,istop=int(r[1]),
                iterations=int(r[2]),normr=float(r[3]),normar=float(r[4]),normA=float(r[5]),
                condition=float(r[6]),normx=float(r[7]),slope=slope,predictedReduction=predicted,
                completeRows=linear.shape[0],completeColumns=linear.shape[1],seconds=time.monotonic()-tick)
            trace.append(row);emit("area_power_two_actual_LSMR",iteration=iteration,**row)
            if slope<0 and predicted>0:
                for alpha in recipe["lm"]["alphas"]:
                    candidate=z+alpha*dz
                    try:
                        trial,trialgroups=areaop.observe(joint,stream,basis,caches,weights,candidate,config,recipe,area)
                        ok=(trial["squaredNorm"]<baseline["squaredNorm"] and
                            trial["squaredNorm"]<=baseline["squaredNorm"]+2*recipe["lm"]["armijo"]*alpha*slope)
                        row=dict(kind="actual_complete14_trial",alpha=alpha,actualValueEvaluated=True,
                            accepted=bool(ok),**scalars(trial))
                        trace.append(row);emit("area_power_two_actual_trial",iteration=iteration,**row)
                        if ok:
                            z,value,groups=candidate,trial,trialgroups
                            accepted=True;selected=alpha
                            break
                    except (ValueError,ArithmeticError,FloatingPointError) as error:
                        row=dict(kind="actual_complete14_domain_rejection",alpha=alpha,
                            actualValueEvaluated=False,accepted=False,error=str(error))
                        trace.append(row);emit("area_power_two_actual_trial",iteration=iteration,**row)
            if accepted:
                break
            damping*=10
        attempt_count+=1;own+=int(accepted)
        value,groups=areaop.observe(joint,stream,basis,caches,weights,z,config,recipe,area)
        current=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_sha,
            actualAreaModelInitialSHA256=initial_sha,carriedOriginalModelAcceptedSteps=carried,
            areaPowerTwoAcceptedSteps=own,areaPowerTwoAttemptCount=attempt_count,
            actualTotalCartesianAcceptedSteps=carried+own,accepted=accepted,
            actualAreaPowerTwoAcceptedStepsAdded=int(accepted),alpha=selected,baseline=baseline,
            evaluation=value,groupValues=groups,trace=trace,actualCompleteDerivativeCheck=check)
        statepath=Path(str(prefix)+f"-step{iteration:02d}-state.json")
        parent_sha=write(statepath,current)
        outputs.append(dict(stateFile=str(statepath),stateSHA256=parent_sha,accepted=accepted,
            areaPowerTwoAcceptedSteps=own,actualTotalAcceptedSteps=carried+own,evaluation=value,groupValues=groups))
        emit("area_power_two_actual_state",iteration=iteration,stateSHA256=parent_sha,accepted=accepted,
            areaPowerTwoAcceptedSteps=own,totalAcceptedSteps=carried+own,seconds=time.monotonic()-started,**scalars(value))
        del linear,gradient
        gc.collect()
        if not accepted:
            break
    for row in prepared["caches"].values():
        for key in ("jets","radius"):
            if sha(row["files"][key])!=row["SHA256"][key]:
                raise ArithmeticError("Frozen source bytes changed during area-model solve")
    report=dict(schema=SCHEMA+"-report",modelDefinition=model,modelDefinitionSHA256=model_sha,
        preparedSHA256=sha(args.prepared),inputStateSHA256=sha(args.state),initialSHA256=initial_sha,
        carriedOriginalModelAcceptedSteps=carried,areaPowerTwoAcceptedSteps=own,areaPowerTwoAttemptCount=attempt_count,
        actualTotalAcceptedSteps=carried+own,outputs=outputs,allFrozenSourceCachesUnchanged=True,
        sameFrozenG=True,all13OriginalRowsPreserved=True,all5292ColumnsPreserved=True,
        independentThirdObserverNotComputed=True,seconds=time.monotonic()-started,
        OSExitCode=None,externalExitReceiptRequired=True,continuousCertificate=False,strongTargetComplete=False)
    h=write(str(prefix)+"-report.json",report)
    emit("area_power_two_actual_complete",reportSHA256=h,areaPowerTwoAcceptedSteps=own,totalAcceptedSteps=carried+own)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--base-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-cartesian.py"))
    ap.add_argument("--joint-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-two-grid-cartesian.py"))
    ap.add_argument("--refined-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-refined-cartesian.py"))
    ap.add_argument("--area-source",type=Path,default=Path(__file__).with_name("6a65-geometry-area-ratio-power-two.py"))
    ap.add_argument("--background",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-background.py"))
    ap.add_argument("--prepared",type=Path,required=True)
    ap.add_argument("--state",type=Path,required=True)
    ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--steps",type=int,default=1)
    ap.add_argument("--operator-epoch",type=str,default=None)
    args=ap.parse_args()
    if args.operator_epoch is not None and (len(args.operator_epoch)!=40 or any(c not in "0123456789abcdef" for c in args.operator_epoch)):
        raise ValueError("An explicitly supplied operator epoch must be a full commit SHA")
    if not 1<=args.steps<=20:
        raise ValueError("Finite explicit actual batch required")
    if args.scripts.parents[2] in args.prefix.resolve().parents:
        raise ValueError("Actual coefficients and raw arrays stay outside Git")
    try:
        run(args)
    except BaseException as error:
        path=Path(str(args.prefix)+"-failure.json")
        if not path.exists():
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(json.dumps(dict(schema=SCHEMA+"-actual-failure",error=str(error),
                traceback=traceback.format_exc(),acceptedStepsNotInferred=True),indent=2)+"\n")
        raise


if __name__=="__main__":
    main()
