#!/usr/bin/env python3
"""Independent actual polar source: complete two-grid q=2 physical-H LM.

An absent --state means new zero Cartesian correction coefficients, not a
borrowed Cauchy checkpoint. The complete polar background and its separately
frozen target metric are bound by a new prepared-source definition. All 5292
columns and both complete 13+1 row grids remain in the old Sobolev quadratic.
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

SCHEMA="6a65-nonfold-polar-complete14-q2-full-physical-normal-fixed-g-Cartesian-v2"
FULL_NORMAL_SHA="8e8d40c05ba5b5e15c49be4c7d91c882d93007567f67caa19a4a43ad39bc2084"
HASHES=dict(base="4e6aaee2178c621e1207f6d5b06d58d075aea1c0566f84c8b506cfd588db0ddd",
    background="58e7080d51c0c0a7d584e688c9ec1b995fdffb72c0c0a21eec9a8f23f178c3fd",
    joint="26b53da871749b90358cef659dc8c23621f649061e0a65b4b9a7f500a05398b3",
    area="d8fb8710d4957430b66b474d79a61d3b7bf4fff9915bba1d62ecfea0f96ee97e",
    stream="b8cfd595b535cc33d47e2c0bc3e2b8d6a79c8163a235415115ca42c53416e4a9",
    point="cf475476fb2b5e3a91d4438dd9dd67e54652bfd9594cc577b038ee2fd5e6f08f")


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
        raise FileExistsError("Fresh actual independent-polar output required")
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


def starting_state(state,model,model_sha,basis,definition,prepared_sha,entry_sha):
    """Bind zero initialization or this exact new source's own saved coefficients."""
    if state is None:
        return np.zeros((basis.nb,basis.na)),0,0
    if state.get("schema")!=SCHEMA+"-checkpoint":
        raise ValueError("Only this independent polar source's own checkpoint may continue")
    if (state.get("preparedSHA256")!=prepared_sha or state.get("targetMetricFrozen") is not True or
        state.get("basis")!=basis.definition or state.get("pointConfig")!=definition["pointConfig"] or
        state.get("sourceIdentity")!=definition["sourceIdentity"] or
        state.get("correctionSupport")!=definition["correctionSupport"] or
        state.get("newIndependentPolarSource") is not True):
        raise ValueError("Actual polar parent must bind the same source, g, domain and complete space")
    if (state.get("modelDefinitionSHA256")!=model_sha or state.get("entrySHA256")!=entry_sha or
        canonical(state.get("modelDefinition"))!=model_sha or state.get("modelDefinition")!=model):
        raise ValueError("Continued actual polar model, operator epoch or source changed")
    own=state.get("polarFullBandAcceptedSteps")
    attempts=state.get("polarFullBandAttemptCount")
    if (type(own)is not int or type(attempts)is not int or not 0<=own<=attempts or
        type(state.get("actualTotalCartesianAcceptedSteps"))is not int or
        type(state.get("borrowedOldSourceAcceptedSteps"))is not int or
        state.get("actualTotalCartesianAcceptedSteps")!=own or
        state.get("borrowedOldSourceAcceptedSteps")!=0):
        raise ValueError("Independent actual polar acceptance counters are inconsistent")
    raw=np.asarray(state.get("z"),float)
    if raw.shape!=(basis.dimension,) or not np.all(np.isfinite(raw)):
        raise ValueError("Every finite physical polar correction coefficient is required")
    return raw.reshape(basis.nb,basis.na).copy(),own,attempts


def check_run_binding(definition,current_run_id):
    claimed_run=definition["runIdentity"]["actualRunId"]
    if claimed_run is not None and (type(claimed_run)is not int or claimed_run<=0 or
            str(claimed_run)!=current_run_id):
        raise ValueError("An Actions cache may only be consumed inside its actual source job")


def physical_normal_statistics(normal,gradient):
    """J^T(J dz+r)+lambda*S*dz, measured in the original coefficient coordinates."""
    if not np.all(np.isfinite(normal)) or not np.all(np.isfinite(gradient)):
        raise ArithmeticError("Complete original physical normal or gradient is nonfinite")
    absolute=float(np.linalg.norm(normal))
    initial_gradient=float(np.linalg.norm(gradient))
    relative=absolute/max(np.finfo(float).tiny,initial_gradient)
    if not all(math.isfinite(x) for x in (absolute,initial_gradient,relative)):
        raise ArithmeticError("Physical normal diagnostics overflowed")
    return dict(originalPhysicalNormalAbsoluteResidual=absolute,
        originalPhysicalInitialGradientNorm=initial_gradient,
        originalPhysicalNormalRelativeResidual=relative,
        originalPhysicalNormalMaxOneScaledResidual=absolute/max(1.,initial_gradient),
        originalPhysicalGradientDefinition="J^T r; objective is ||r||^2",
        originalPhysicalRelativeDenominator="max(float64.tiny, ||J^T r||)")


def run(args):
    started=time.monotonic()
    paths=dict(base=args.base_entry,background=args.background,joint=args.joint_entry,area=args.area_source,
        stream=args.scripts/"6a65-cartesian-complete-stream.py",
        point=args.scripts/"6a65-cartesian-complete-point-operator.py")
    for name,path in paths.items():
        if sha(path)!=HASHES[name]:
            raise ValueError("Frozen complete source changed: "+name)
    if sha(args.full_normal_source)!=FULL_NORMAL_SHA:
        raise ValueError("Frozen complete two-grid q=2 physical-normal helper changed")
    fullnormal=module(args.full_normal_source,"gap_q2_full_physical_normal")
    base=module(args.base_entry,"gap_area_base")
    joint=module(args.joint_entry,"gap_area_joint")
    areaop=module(args.area_source,"gap_area_complete_operator")
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","gap_area_stream")
    background=module(args.background,"gap_area_background")
    prepared,definition,basis,caches=base.validate_prepared(args,stream,background)
    check_run_binding(definition,os.environ.get("GITHUB_RUN_ID"))
    if basis.dimension != 5292:
        raise ValueError("Every actual independent-polar 5292-column direction is required")
    prefix=args.prefix.resolve()
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh actual independent-polar prefix required")
    recipe=copy.deepcopy(definition["recipe"])
    recipe["lsmr"]["maxIterations"]=160
    recipe["basis"].update(radialBasisCount=basis.nb,maxAngularFrequency=basis.M,
        physicalKnotsAuthoritative=True,preparedPolarBasisAuthoritative=True)
    area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2,
        formula="sqrt(frozen original metric quadrature weight) * max(0, (.5/sigma)^2-1)",
        sigma="|Xs cross Xu|/a; a is the frozen target metric radius",
        hingeDerivativeAtEquality=0.,positiveAreaDomainRequiredAtEveryActualPoint=True,
        allOriginalThirteenRowsPreserved=True,continuousAreaLowerBoundCertified=False)
    model=dict(preparedSHA256=sha(args.prepared),preparedDefinitionSHA256=prepared["definitionSHA256"],
        sourceIdentity=definition["sourceIdentity"],basis=basis.definition,recipe=recipe,
        pointConfig=definition["pointConfig"],operatorSources=definition["operatorSources"],
        newSources=HASHES,entrySHA256=sha(__file__),operatorSourceEpoch=args.operator_epoch,areaBarrier=area,
        quadrature=dict(trainingScale=.5,observerScale=.5,bothGridsParticipateInObjective=True,
            actualCompleteGrids={key:dict(radialCount=len(cache.nodes),angleCount=len(cache.u),
                cacheSHA256=prepared["caches"][key]["SHA256"]) for key,cache in caches.items()},
            newPolarQuadratureBaseline=True,oldGapGridBaselineBorrowed=False,
            originalThirteenRowsUnchanged=True,newAreaWeights="prepared metric weights"),
        continuousQuadratureAccuracyClaimed=False,
        physicalNormalSolver=dict(helperSHA256=FULL_NORMAL_SHA,
            fullPhysicalHWithoutCrossChannelDropping=True,
            etaPolicy="current-positive-LM-lambda" if args.preconditioner_eta is None else "explicit-fixed-eta",
            fixedEta=args.preconditioner_eta,
            completeAugmentedOperator="[J T; sqrt(lambda) L_S^T T]",
            requiredLSMRDamp=0.,originalSharedSobolevQuadraticPreserved=True,
            preconditioningChangesOnlyLinearCoordinates=True))
    model_sha=canonical(model)
    state=None if args.state is None else json.loads(args.state.read_text())
    z,own,attempt_count=starting_state(state,model,model_sha,basis,definition,sha(args.prepared),sha(__file__))
    weights={key:{name:.5*np.asarray(value,float) for name,value in prepared["caches"][key]["weights"].items()}
             for key in caches}
    config=stream.point.PointConfig(**definition["pointConfig"])
    value,groups=areaop.observe(joint,stream,basis,caches,weights,z,config,recipe,area)
    parent_sha=None if args.state is None else sha(args.state)
    common=dict(schema=SCHEMA+"-checkpoint",modelDefinition=model,modelDefinitionSHA256=model_sha,
        sourceIdentity=definition["sourceIdentity"],preparedSHA256=sha(args.prepared),entrySHA256=sha(__file__),
        basis=basis.definition,dimension=basis.dimension,pointConfig=asdict(config),
        correctionSupport=definition["correctionSupport"],targetMetricFrozen=True,
        allOriginalThirteenRowsRetained=True,all5292ColumnsRetained=True,
        entirePrefixPreserved=True,trueR205TailAndCuffFixed=True,
        newObjectiveComparedOnlyWithItsOwnBaseline=True,areaBarrier=area,
        sameObjectiveAsInputParent=state is not None,newIndependentPolarSource=True,
        borrowedOldSourceAcceptedSteps=0,sourceGeometryAndTargetMetricSeparatelyBound=True,
        originalSharedSobolevQuadraticPreserved=True,fullNormalHelperSHA256=FULL_NORMAL_SHA,
        continuousCertificate=False,strongTargetComplete=False)
    initial=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_sha,accepted=False,
        polarFullBandAcceptedSteps=own,polarFullBandAttemptCount=attempt_count,
        actualTotalCartesianAcceptedSteps=own,evaluation=value,groupValues=groups,
        actualOwnPolarBaseline=True,newZeroCoefficientInitialization=state is None,
        freeCoefficientNonzero=bool(np.count_nonzero(z)),
        previousModelEvaluation=None if state is None else state["evaluation"])
    initial_sha=write(str(prefix)+"-initial.json",initial)
    emit("polar_q2_full_band_actual_initial",initialSHA256=initial_sha,columns=basis.dimension,rows=value["rowCount"],
        borrowedOldSourceSteps=0,polarFullBandAcceptedSteps=own,
        newZeroCoefficientInitialization=state is None,**scalars(value))
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
                    maximumAbsoluteError=float(np.max(np.abs(fd-jv))),
                    actualNewPolarBackground=True,freeCoefficientNonzero=bool(np.count_nonzero(z))))
                del plus,minus,fd
                if relative<=2e-5:
                    break
            if checks[-1]["relativeL2Error"]>2e-5:
                raise ArithmeticError("Actual complete new nonlinear residual direction check failed")
            check=dict(completeColumns=linear.shape[1],completeRows=linear.shape[0],
                adjointRelativeDotError=adjoint_error,finiteDifference=checks,
                actualNewPolarBackground=True,freeCoefficientNonzero=bool(np.count_nonzero(z)),
                allOriginalAndAreaRowsIncluded=True,
                hingeConvention="zero generalized derivative at sigma=.5",continuumCertificate=False)
            emit("polar_q2_full_band_actual_complete_derivative_check",**check)
            del direction,cotangent,jv,dz
            gc.collect()
        trace=[];accepted=False;selected=None
        gradient=None;augmented=None
        for attempt in range(1,recipe["lm"]["maxDampingAttempts"]+1):
            tick=time.monotonic()
            eta=damping if args.preconditioner_eta is None else args.preconditioner_eta
            if augmented is not None:
                del augmented
                gc.collect()
            augmented=fullnormal.SameSobolevAreaFullBandAugmented(linear,damping,eta=eta)
            if gradient is None:
                gradient=augmented.raw_transpose(linear.residual)
            emit("polar_q2_full_band_actual_assembly",iteration=iteration,attempt=attempt,
                damping=damping,eta=eta,assembly=augmented.blocks.receipt,
                originalLMQuadraticUnchanged=True)
            r=lsmr(augmented.operator,augmented.rhs,damp=0.,
                atol=recipe["lsmr"]["atol"],btol=recipe["lsmr"]["btol"],
                conlim=recipe["lsmr"]["conditionLimit"],maxiter=recipe["lsmr"]["maxIterations"])
            y=r[0]
            if not np.all(np.isfinite(y)):
                raise ArithmeticError("Actual full14 direction is nonfinite")
            dz=augmented.unpack(y);jv=augmented.raw_matvec(dz)
            slope=float(gradient.ravel()@dz.ravel())
            physical_normal=augmented.physical_normal_residual(dz)
            normal_statistics=physical_normal_statistics(physical_normal,gradient)
            predicted=float(-2*slope-jv@jv)
            row=dict(kind="actual_complete14_LSMR",attempt=attempt,damping=damping,istop=int(r[1]),
                iterations=int(r[2]),normr=float(r[3]),normar=float(r[4]),normA=float(r[5]),
                condition=float(r[6]),normx=float(r[7]),slope=slope,predictedReduction=predicted,
                completeRows=linear.shape[0],completeColumns=linear.shape[1],seconds=time.monotonic()-tick,
                **normal_statistics,
                physicalDirectionNorm=float(np.linalg.norm(dz)),
                oldLMQuadraticUnchanged=True,LSMRDamp=0.,eta=eta,
                originalRegularizerRows=linear.shape[1],assembly=augmented.blocks.receipt,
                exactAlgebraicNormalSpectrumBounds=[min(1.,damping/eta),max(1.,damping/eta)])
            trace.append(row);emit("polar_q2_full_band_actual_LSMR",iteration=iteration,**row)
            if slope<0 and predicted>0:
                for alpha in recipe["lm"]["alphas"]:
                    candidate=z+alpha*dz
                    try:
                        trial,trialgroups=areaop.observe(joint,stream,basis,caches,weights,candidate,config,recipe,area)
                        ok=(trial["squaredNorm"]<baseline["squaredNorm"] and
                            trial["squaredNorm"]<=baseline["squaredNorm"]+2*recipe["lm"]["armijo"]*alpha*slope)
                        row=dict(kind="actual_complete14_trial",alpha=alpha,actualValueEvaluated=True,
                            accepted=bool(ok),**scalars(trial))
                        trace.append(row);emit("polar_q2_full_band_actual_trial",iteration=iteration,**row)
                        if ok:
                            z,value,groups=candidate,trial,trialgroups
                            accepted=True;selected=alpha
                            break
                    except (ValueError,ArithmeticError,FloatingPointError) as error:
                        row=dict(kind="actual_complete14_domain_rejection",alpha=alpha,
                            actualValueEvaluated=False,accepted=False,error=str(error))
                        trace.append(row);emit("polar_q2_full_band_actual_trial",iteration=iteration,**row)
            if accepted:
                break
            damping*=10
        attempt_count+=1;own+=int(accepted)
        value,groups=areaop.observe(joint,stream,basis,caches,weights,z,config,recipe,area)
        current=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_sha,
            actualPolarModelInitialSHA256=initial_sha,
            polarFullBandAcceptedSteps=own,polarFullBandAttemptCount=attempt_count,
            actualTotalCartesianAcceptedSteps=own,accepted=accepted,
            actualPolarFullBandAcceptedStepsAdded=int(accepted),alpha=selected,baseline=baseline,
            freeCoefficientNonzero=bool(np.count_nonzero(z)),
            evaluation=value,groupValues=groups,trace=trace,actualCompleteDerivativeCheck=check)
        statepath=Path(str(prefix)+f"-step{iteration:02d}-state.json")
        parent_sha=write(statepath,current)
        outputs.append(dict(stateFile=str(statepath),stateSHA256=parent_sha,accepted=accepted,
            polarFullBandAcceptedSteps=own,actualTotalAcceptedSteps=own,evaluation=value,groupValues=groups))
        emit("polar_q2_full_band_actual_state",iteration=iteration,stateSHA256=parent_sha,accepted=accepted,
            polarFullBandAcceptedSteps=own,totalAcceptedSteps=own,seconds=time.monotonic()-started,**scalars(value))
        del linear,gradient,augmented
        gc.collect()
        if not accepted:
            break
    for row in prepared["caches"].values():
        for key in ("jets","radius"):
            if sha(row["files"][key])!=row["SHA256"][key]:
                raise ArithmeticError("Frozen source bytes changed during area-model solve")
    report=dict(schema=SCHEMA+"-report",modelDefinition=model,modelDefinitionSHA256=model_sha,
        preparedSHA256=sha(args.prepared),inputStateSHA256=None if args.state is None else sha(args.state),
        initialSHA256=initial_sha,newZeroCoefficientInitialization=state is None,
        borrowedOldSourceAcceptedSteps=0,polarFullBandAcceptedSteps=own,polarFullBandAttemptCount=attempt_count,
        actualTotalAcceptedSteps=own,outputs=outputs,allFrozenSourceCachesUnchanged=True,
        sameFrozenG=True,all13OriginalRowsPreserved=True,all5292ColumnsPreserved=True,
        baselineOnlyRequested=args.steps==0,actualNewAttemptCount=len(outputs),
        independentThirdObserverNotComputed=True,seconds=time.monotonic()-started,
        OSExitCode=None,externalExitReceiptRequired=True,continuousCertificate=False,strongTargetComplete=False)
    h=write(str(prefix)+"-report.json",report)
    emit("polar_q2_full_band_actual_complete",reportSHA256=h,polarFullBandAcceptedSteps=own,totalAcceptedSteps=own)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--base-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-nonfold-cartesian-prepare-v2.py"))
    ap.add_argument("--joint-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-two-grid-cartesian.py"))
    ap.add_argument("--area-source",type=Path,default=Path(__file__).with_name("6a65-geometry-area-ratio-power-two.py"))
    ap.add_argument("--background",type=Path,default=Path(__file__).with_name("6a65-geometry-nonfold-polar-background-v2.py"))
    ap.add_argument("--full-normal-source",type=Path,
        default=Path(__file__).with_name("6a65-cartesian-complete-radial-normal-two-grid-area.py"))
    ap.add_argument("--preconditioner-eta",type=float,default=None,
        help="Optional fixed eta; default eta=lambda exactly whitens the original physical LM")
    ap.add_argument("--prepared",type=Path,required=True)
    ap.add_argument("--state",type=Path,
        help="Optional exact own polar checkpoint; absent means a new zero free-coefficient baseline")
    ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--steps",type=int,default=1)
    ap.add_argument("--operator-epoch",type=str,default=None)
    args=ap.parse_args()
    if args.operator_epoch is not None and (len(args.operator_epoch)!=40 or any(c not in "0123456789abcdef" for c in args.operator_epoch)):
        raise ValueError("An explicitly supplied operator epoch must be a full commit SHA")
    if args.preconditioner_eta is not None and (not math.isfinite(args.preconditioner_eta) or args.preconditioner_eta<=0):
        raise ValueError("A specified physical preconditioner eta must be finite and positive")
    if not 0<=args.steps<=20:
        raise ValueError("Explicit baseline-only zero or finite actual attempt batch required")
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
