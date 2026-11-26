#!/usr/bin/env python3
"""Actual fixed-g, full-space Cartesian continuation after knot insertion.

The two frozen complete source grids and all thirteen point rows stay
unchanged. Four local physical knots and every real Fourier mode through
24 enlarge the 2400-column space to 5292 columns. The old field is carried
by Boehm knot insertion, with the actual floating six-jet transfer error
recorded on both complete grids before any new acceptance.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
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
from scipy.interpolate import BSpline
from scipy.sparse.linalg import lsmr

SCHEMA="6a65-gap105-local-knot-full-angular-refinement-v1"
BASE_SHA="ca22b417066c3e7f46470b876eabb57ed4d1673858000d31d4c99d8acc3f2f86"
JOINT_SHA="26b53da871749b90358cef659dc8c23621f649061e0a65b4b9a7f500a05398b3"
CELLS=(3,4,13,14)
NEW_M=24


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
        raise FileExistsError("Fresh actual refinement output required")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n")
    return sha(path)


def emit(event,**value):
    print(json.dumps(dict(event=event,**value),allow_nan=False),flush=True)


def refined_basis(base,stream,old):
    if old.nb!=32 or old.M!=12:
        raise ValueError("This actual refinement binds the complete J32/M12 source space")
    inserts=np.array([(old.breaks[j]+old.breaks[j+1])/2 for j in CELLS])
    physical=np.sort(np.r_[old.breaks,inserts])
    if len(np.unique(physical))!=len(physical):
        raise ValueError("All four new physical knots must be distinct")
    new=base.periodic_basis(stream,old.c,old.end,old.nb+len(inserts),NEW_M)
    # Retain every old binary64 physical knot literally, not by a rounded
    # normalized-coordinate round trip. This makes the spline spaces nested.
    new.breaks=physical
    new.knots=np.r_[np.repeat(old.c,6),physical[1:-1],np.repeat(old.end,6)]
    new.full_count=len(new.knots)-6
    new._spline=BSpline(new.knots,np.eye(new.full_count),5,extrapolate=False)
    new.definition.update(normalizedBreaks=((physical-old.c)/(old.end-old.c)).tolist(),
        physicalBreaks=physical.tolist(),physicalKnots=new.knots.tolist(),
        physicalKnotsAuthoritative=True,oldPhysicalKnotsRetainedExactly=True,
        addedPhysicalKnots=inserts.tolist(),selectedOldCells=list(CELLS),
        fullRadialBasisCount=new.full_count,
        omittedEndpointColumns=[0,1,2,new.full_count-3,new.full_count-2,new.full_count-1])
    if new.dimension!=5292 or new.full_count!=new.nb+6:
        raise ArithmeticError("Full refined dimension changed")
    return new,inserts


def prolongate(old,new,inserts,coefficient,caches):
    original=np.zeros((old.full_count,old.na))
    original[3:-3]=coefficient
    spline=BSpline(old.knots,original,5,extrapolate=False)
    for knot in inserts:
        spline=spline.insert_knot(float(knot),1)
    if not np.array_equal(spline.t,new.knots):
        raise ArithmeticError("Boehm physical knot list differs from the actual refined basis")
    if np.any(spline.c[:3]!=0) or np.any(spline.c[-3:]!=0):
        raise ArithmeticError("Endpoint zero two-jets were not preserved by insertion")
    out=np.zeros((new.nb,new.na))
    oldcolumns={channel:j for j,channel in enumerate(old.channels)}
    for j,channel in enumerate(new.channels):
        if channel in oldcolumns:
            out[:,j]=spline.c[3:-3,oldcolumns[channel]]
    maximum=np.zeros(6)
    pergrid={}
    for name,cache in caches.items():
        oldmat=old.matrices(cache.nodes)
        newmat=new.matrices(cache.nodes)
        errors=np.zeros(6)
        scale=np.zeros(6)
        for first in range(0,len(cache.nodes),12):
            sl=slice(first,first+12)
            a=old.packet(tuple(m[sl] for m in oldmat),coefficient,len(cache.u))
            b=new.packet(tuple(m[sl] for m in newmat),out,len(cache.u))
            errors=np.maximum(errors,np.max(np.abs(a-b),axis=(0,2,3)))
            scale=np.maximum(scale,np.max(np.abs(a),axis=(0,2,3)))
        if np.any(errors>2e-10*np.maximum(1.,scale)):
            raise ArithmeticError("Actual full six-jet transfer error exceeds explicit tolerance")
        maximum=np.maximum(maximum,errors)
        pergrid[name]=dict(maximumAbsoluteByJet=errors.tolist(),oldCorrectionScaleByJet=scale.tolist())
    boundary=new.packet(new.matrices(np.array([new.c,new.end])),out,192)
    if np.any(boundary!=0):
        raise ArithmeticError("Actual refined endpoint six-jets changed")
    return out,dict(method="Boehm insertion, then exact zero extension of new Fourier channels",
        nestedRealSplineSpaces=True,noSourceProjection=True,oldAngularChannelsAllRetained=True,
        allHigherAngularCoefficientsInitiallyZero=True,physicalKnotsIdenticalSubset=True,
        jetOrder=["X","Xs","Xu","Xss","Xsu","Xuu"],groups=pergrid,
        maximumAbsoluteByJet=maximum.tolist(),allEndpointCorrectionJetsExactlyZero=True,
        floatingTransferIntervalErrorCertified=False,
        baselineRecomputedAfterFloatingTransfer=True)


def run(args):
    started=time.monotonic()
    if sha(args.base_entry)!=BASE_SHA or sha(args.joint_entry)!=JOINT_SHA:
        raise ValueError("Frozen complete source loader or two-grid operator changed")
    base=module(args.base_entry,"gap_refinement_base")
    joint=module(args.joint_entry,"gap_refinement_joint")
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","gap_refinement_stream")
    background=module(args.background,"gap_refinement_background")
    prepared,definition,oldbasis,caches=base.validate_prepared(args,stream,background)
    basis,inserts=refined_basis(base,stream,oldbasis)
    prefix=args.prefix.resolve()
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh actual refined experiment prefix required")
    recipe=copy.deepcopy(definition["recipe"])
    recipe["lsmr"]["maxIterations"]=160
    recipe["basis"].update(radialBasisCount=basis.nb,maxAngularFrequency=basis.M,
        physicalKnotsAuthoritative=True,localKnotRefinement=True)
    model=dict(preparedSHA256=sha(args.prepared),preparedDefinitionSHA256=prepared["definitionSHA256"],
        sourceIdentity=definition["sourceIdentity"],basis=basis.definition,recipe=recipe,
        pointConfig=definition["pointConfig"],operatorSources=definition["operatorSources"],
        jointEntrySHA256=JOINT_SHA,baseEntrySHA256=BASE_SHA,entrySHA256=sha(__file__),
        quadrature=dict(trainingScale=.5,observerScale=.5,
            unchangedCompleteGrids=True,allThirteenRows=True,allRefinedColumns=True),
        continuousQuadratureAccuracyClaimed=False)
    model_sha=canonical(model)
    state=json.loads(args.state.read_text())
    if state.get("preparedSHA256")!=sha(args.prepared) or state.get("targetMetricFrozen") is not True:
        raise ValueError("Actual parent must bind this fixed source and metric")
    if state.get("schema")==joint.SCHEMA+"-checkpoint":
        if (state.get("entrySHA256")!=JOINT_SHA or state.get("basis")!=oldbasis.definition or
            state.get("pointConfig")!=definition["pointConfig"] or
            canonical(state["modelDefinition"])!=state["modelDefinitionSHA256"] or
            state["modelDefinition"]["preparedDefinitionSHA256"]!=prepared["definitionSHA256"]):
            raise ValueError("Actual complete coarse parent changed identity")
        oldz=np.asarray(state["z"],float).reshape(oldbasis.nb,oldbasis.na)
        z,transfer=prolongate(oldbasis,basis,inserts,oldz,caches)
        carried=state["actualTotalCartesianAcceptedSteps"]
        own=attempt_count=0
    elif state.get("schema")==SCHEMA+"-checkpoint":
        if state.get("modelDefinitionSHA256")!=model_sha or state.get("entrySHA256")!=sha(__file__):
            raise ValueError("Refined continuation changed full model identity")
        z=np.asarray(state["z"],float).reshape(basis.nb,basis.na)
        transfer=state["initialTransfer"]
        carried=state["carriedCoarseAcceptedSteps"]
        own=state["refinedAcceptedSteps"]
        attempt_count=state["refinedAttemptCount"]
    else:
        raise ValueError("Actual complete joint or refined checkpoint required")
    if not np.all(np.isfinite(z)):
        raise ValueError("Finite complete refined coefficients required")
    weights={key:{name:.5*np.asarray(value,float) for name,value in prepared["caches"][key]["weights"].items()}
             for key in caches}
    config=stream.point.PointConfig(**definition["pointConfig"])
    value,groups=joint.observe(stream,basis,caches,weights,z,config,recipe)
    parent_sha=sha(args.state)
    common=dict(schema=SCHEMA+"-checkpoint",modelDefinition=model,modelDefinitionSHA256=model_sha,
        sourceIdentity=definition["sourceIdentity"],preparedSHA256=sha(args.prepared),
        entrySHA256=sha(__file__),basis=basis.definition,dimension=basis.dimension,
        pointConfig=asdict(config),correctionSupport=definition["correctionSupport"],
        allThirteenRowsInBothGrids=True,all5292ColumnsRetained=True,
        entirePrefixPreserved=True,trueR205TailAndCuffFixed=True,targetMetricFrozen=True,
        initialTransfer=transfer,continuousCertificate=False,strongTargetComplete=False)
    initial=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_sha,
        accepted=False,carriedCoarseAcceptedSteps=carried,refinedAcceptedSteps=own,
        refinedAttemptCount=attempt_count,actualTotalCartesianAcceptedSteps=carried+own,
        actualOwnRefinedBaseline=True,evaluation=value,groupValues=groups,
        coarseParentValue=state["evaluation"])
    initial_sha=write(str(prefix)+"-initial.json",initial)
    emit("refined_actual_initial",initialSHA256=initial_sha,columns=basis.dimension,
        rows=value["rowCount"],R2=value["squaredNorm"],metric=value["maxRelativeMetric"],
        curvature=value["maxCurvature"],eta=value["minImmersion"],held=value["minHeldDistance"],
        transfer=transfer,actualCarriedSteps=carried,refinedAcceptedSteps=own)
    outputs=[]
    damping=recipe["lm"]["damping"]
    adjoint=None
    for iteration in range(1,args.steps+1):
        linear=joint.TwoGrid(stream,basis,caches,weights,z,config,recipe)
        baseline=linear.statistics
        if adjoint is None:
            rng=np.random.default_rng(20261127)
            x=rng.normal(size=linear.shape[1]); y=rng.normal(size=linear.shape[0])
            lhs=float(linear.matvec(x)@y); rhs=float(x@linear.rmatvec(y))
            error=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
            if error>1e-10:
                raise ArithmeticError("Actual refined complete shared-coordinate adjoint failed")
            adjoint=dict(relativeDotError=error,completeRows=linear.shape[0],completeColumns=linear.shape[1])
            emit("refined_actual_adjoint",**adjoint)
            del x,y
        gradient=linear.rmatvec(linear.residual)
        trace=[];accepted=False;selected=None
        for attempt in range(1,recipe["lm"]["maxDampingAttempts"]+1):
            tick=time.monotonic()
            r=lsmr(linear.operator,-linear.residual,damp=math.sqrt(damping),
                atol=recipe["lsmr"]["atol"],btol=recipe["lsmr"]["btol"],
                conlim=recipe["lsmr"]["conditionLimit"],maxiter=recipe["lsmr"]["maxIterations"])
            y=r[0]
            if not np.all(np.isfinite(y)):
                raise ArithmeticError("Complete refined direction is nonfinite")
            dz=linear.unpack(y);jv=linear.matvec(y);slope=float(gradient@y)
            predicted=float(-2*slope-jv@jv)
            row=dict(kind="actual_complete_refined_LSMR",attempt=attempt,damping=damping,
                istop=int(r[1]),iterations=int(r[2]),normr=float(r[3]),normar=float(r[4]),
                normA=float(r[5]),condition=float(r[6]),normx=float(r[7]),slope=slope,
                predictedReduction=predicted,completeRows=linear.shape[0],
                completeColumns=linear.shape[1],seconds=time.monotonic()-tick)
            trace.append(row);emit("refined_actual_LSMR",iteration=iteration,**row)
            if slope<0 and predicted>0:
                for alpha in recipe["lm"]["alphas"]:
                    candidate=z+alpha*dz
                    try:
                        trial,trialgroups=joint.observe(stream,basis,caches,weights,candidate,config,recipe)
                        ok=(trial["squaredNorm"]<baseline["squaredNorm"] and
                            trial["squaredNorm"]<=baseline["squaredNorm"]+2*recipe["lm"]["armijo"]*alpha*slope)
                        row=dict(kind="actual_complete_refined_trial",alpha=alpha,
                            actualValueEvaluated=True,accepted=bool(ok),R2=trial["squaredNorm"],
                            metric=trial["maxRelativeMetric"],curvature=trial["maxCurvature"],
                            eta=trial["minImmersion"],held=trial["minHeldDistance"])
                        trace.append(row);emit("refined_actual_trial",iteration=iteration,**row)
                        if ok:
                            z,value,groups=candidate,trial,trialgroups
                            accepted=True;selected=alpha
                            break
                    except (ValueError,ArithmeticError,FloatingPointError) as error:
                        row=dict(kind="actual_refined_domain_rejection",alpha=alpha,
                            actualValueEvaluated=False,accepted=False,error=str(error))
                        trace.append(row);emit("refined_actual_trial",iteration=iteration,**row)
            if accepted:
                break
            damping*=10
        attempt_count+=1;own+=int(accepted)
        value,groups=joint.observe(stream,basis,caches,weights,z,config,recipe)
        current=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_sha,
            actualRefinedInitialSHA256=initial_sha,carriedCoarseAcceptedSteps=carried,
            refinedAcceptedSteps=own,refinedAttemptCount=attempt_count,
            actualTotalCartesianAcceptedSteps=carried+own,accepted=accepted,
            actualRefinedAcceptedStepsAdded=int(accepted),alpha=selected,baseline=baseline,
            evaluation=value,groupValues=groups,trace=trace,actualCompositeAdjointCheck=adjoint)
        statepath=Path(str(prefix)+f"-step{iteration:02d}-state.json")
        parent_sha=write(statepath,current)
        outputs.append(dict(stateFile=str(statepath),stateSHA256=parent_sha,accepted=accepted,
            refinedAcceptedSteps=own,actualTotalAcceptedSteps=carried+own,evaluation=value,groupValues=groups))
        emit("refined_actual_state",iteration=iteration,stateSHA256=parent_sha,accepted=accepted,
            refinedAcceptedSteps=own,totalAcceptedSteps=carried+own,R2=value["squaredNorm"],
            metric=value["maxRelativeMetric"],curvature=value["maxCurvature"],
            eta=value["minImmersion"],held=value["minHeldDistance"],seconds=time.monotonic()-started)
        del linear,gradient
        gc.collect()
        if not accepted:
            break
    for row in prepared["caches"].values():
        for key in ("jets","radius"):
            if sha(row["files"][key])!=row["SHA256"][key]:
                raise ArithmeticError("Frozen source cache changed during refined solve")
    report=dict(schema=SCHEMA+"-report",modelDefinition=model,modelDefinitionSHA256=model_sha,
        preparedSHA256=sha(args.prepared),inputStateSHA256=sha(args.state),initialSHA256=initial_sha,
        initialTransfer=transfer,carriedCoarseAcceptedSteps=carried,refinedAcceptedSteps=own,
        actualTotalAcceptedSteps=carried+own,refinedAttemptCount=attempt_count,outputs=outputs,
        allFrozenSourceCachesUnchanged=True,sameFrozenG=True,all13RowsInBothGrids=True,
        independentThirdObserverNotComputed=True,seconds=time.monotonic()-started,
        OSExitCode=None,externalExitReceiptRequired=True,continuousCertificate=False,strongTargetComplete=False)
    h=write(str(prefix)+"-report.json",report)
    emit("refined_actual_complete",reportSHA256=h,refinedAcceptedSteps=own,totalAcceptedSteps=carried+own)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--base-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-cartesian.py"))
    ap.add_argument("--joint-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-two-grid-cartesian.py"))
    ap.add_argument("--background",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-background.py"))
    ap.add_argument("--prepared",type=Path,required=True)
    ap.add_argument("--state",type=Path,required=True)
    ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--steps",type=int,default=3)
    args=ap.parse_args()
    if not 1<=args.steps<=20:
        raise ValueError("Explicit finite actual attempt batch required")
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
