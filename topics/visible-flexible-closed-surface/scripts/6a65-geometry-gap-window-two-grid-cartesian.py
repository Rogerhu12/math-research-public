#!/usr/bin/env python3
"""Actual same-field fixed-g Cartesian LM on both frozen source grids.

Both the 128-angle and 192-angle source caches contribute all thirteen
point rows with weight 1/2. All 2400 periodic Cartesian columns and the
exactly fixed entire prefix/true tail are retained. This is an explicit
new finite quadrature, with its own baseline and acceptance counters.
"""
from __future__ import annotations
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[name]="1"
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
from scipy.sparse.linalg import LinearOperator,lsmr

SCHEMA="6a65-gap105-window-two-grid-fixed-g-Cartesian-v1"
BASE_SHA="ca22b417066c3e7f46470b876eabb57ed4d1673858000d31d4c99d8acc3f2f86"


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()


def write(path,value):
    path=Path(path)
    if path.exists():
        raise FileExistsError("Fresh actual combined-grid output required")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,separators=(",",":"),allow_nan=False)+"\n")
    return sha(path)


def emit(event,**x):
    print(json.dumps(dict(event=event,**x),allow_nan=False),flush=True)


def combine(stream,values):
    total=None
    for label,value in values.items():
        row=copy.deepcopy(value)
        for key in ("worstMetric","worstCurvature"):
            row[key]["grid"]=label
        total=stream._merge_statistics(total,row)
    total["bothFrozenSourceGridsIncluded"]=True
    return total


class TwoGrid:
    def __init__(self,stream,basis,caches,weights,coefficient,config,recipe):
        self.stream,self.basis=stream,basis
        self.names=("training","observer")
        allnodes=np.concatenate([caches[k].nodes for k in self.names])
        allweights=np.concatenate([weights[k]["metric"] for k in self.names])
        common=stream.BandedSobolev(basis,allnodes,allweights,recipe["preconditioner"])
        self.preconditioner=common
        self.groups={}
        for key in self.names:
            g=stream.CompleteStreamingLinearized(
                basis,caches[key].nodes,weights[key],caches[key],coefficient,len(caches[key].u),
                config,block=recipe["radialBlock"],preconditioner=recipe["preconditioner"],
                cache_point_blocks=True)
            # Both groups now use the SAME invertible column coordinate map.
            g.preconditioner=common
            self.groups[key]=g
        self.residual=np.concatenate([self.groups[k].residual for k in self.names])
        self.boundaries=np.cumsum([0]+[self.groups[k].shape[0] for k in self.names])
        self.shape=(len(self.residual),basis.dimension)
        self.operator=LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=np.float64)
        self.group_values={k:self.groups[k].statistics for k in self.names}
        self.statistics=combine(stream,self.group_values)

    def unpack(self,x):
        return self.preconditioner.unpack(x)

    def matvec(self,x):
        return np.concatenate([self.groups[k].matvec(x) for k in self.names])

    def rmatvec(self,x):
        x=np.asarray(x,float)
        if x.shape!=(self.shape[0],):
            raise ValueError("Complete two-grid residual cotangent required")
        return sum((self.groups[k].rmatvec(x[self.boundaries[j]:self.boundaries[j+1]])
                    for j,k in enumerate(self.names)),np.zeros(self.shape[1]))


def observe(stream,basis,caches,weights,z,config,recipe):
    values={key:stream.observe(
        basis,cache.nodes,weights[key],cache,z,len(cache.u),config,recipe["radialBlock"])
        for key,cache in caches.items()}
    return combine(stream,values),values


def run(args):
    started=time.monotonic()
    if sha(args.base_entry)!=BASE_SHA:
        raise ValueError("Original actual prepared-source loader identity changed")
    base=module(args.base_entry,"gap_joint_base_loader")
    stream=module(args.scripts/"6a65-cartesian-complete-stream.py","gap_joint_complete_stream")
    background=module(args.background,"gap_joint_bound_background")
    prepared,definition,basis,caches=base.validate_prepared(args,stream,background)
    prefix=args.prefix.resolve()
    if any(prefix.parent.glob(prefix.name+"-*")):
        raise FileExistsError("Fresh actual two-grid experiment prefix required")
    recipe=copy.deepcopy(definition["recipe"])
    recipe["lsmr"]["maxIterations"]=160
    recipe["lm"]["maxDampingAttempts"]=3
    joint=dict(
        kind="arithmetic mean of both complete frozen quadrature rules",
        groupScales=dict(training=.5,observer=.5),
        allThirteenRowsInEachGroup=True, allCartesianColumns=True,
        sameSourceAndMetric=True, backgroundProjection=False)
    model=dict(preparedDefinitionSHA256=prepared["definitionSHA256"],
        preparedSHA256=sha(args.prepared),basis=basis.definition,
        jointQuadrature=joint,recipe=recipe,pointConfig=definition["pointConfig"],
        operatorSources=definition["operatorSources"],baseEntrySHA256=BASE_SHA,
        entrySHA256=sha(__file__))
    model_hash=canonical(model)
    state=json.loads(args.state.read_text())
    if state.get("preparedSHA256")!=sha(args.prepared):
        raise ValueError("Actual parent belongs to another frozen source/cache")
    if state.get("schema")==base.SCHEMA+"-checkpoint":
        if (state.get("entrySHA256")!=BASE_SHA or
            state.get("definitionSHA256")!=prepared["definitionSHA256"] or
            state.get("basis")!=basis.definition or state.get("pointConfig")!=definition["pointConfig"] or
            state.get("correctionSupport")!=definition["correctionSupport"] or
            state.get("targetMetricFrozen") is not True):
            raise ValueError("Original six-step actual Cartesian state changed model")
        carried=state["ownAcceptedSteps"]
        prior_joint=joint_attempts=0
    elif state.get("schema")==SCHEMA+"-checkpoint":
        if state.get("modelDefinitionSHA256")!=model_hash or state.get("entrySHA256")!=sha(__file__):
            raise ValueError("Actual joint-model continuation changed definition")
        carried=state["carriedParentAcceptedSteps"]
        prior_joint=state["jointAcceptedSteps"]
        joint_attempts=state["jointAttemptCount"]
    else:
        raise ValueError("An actual own Cartesian state is required")
    z=np.asarray(state["z"],float).reshape(basis.nb,basis.na)
    if not np.all(np.isfinite(z)):
        raise ValueError("Complete finite actual parent coefficients required")
    config=stream.point.PointConfig(**definition["pointConfig"])
    weights={key:{name:.5*np.asarray(values,float)
        for name,values in prepared["caches"][key]["weights"].items()} for key in caches}
    values,groups=observe(stream,basis,caches,weights,z,config,recipe)
    parent_hash=sha(args.state)
    common=dict(schema=SCHEMA+"-checkpoint",modelDefinitionSHA256=model_hash,
        preparedSHA256=sha(args.prepared),sourceIdentity=definition["sourceIdentity"],
        modelDefinition=model,basis=basis.definition,dimension=basis.dimension,
        correctionSupport=definition["correctionSupport"],
        entireCertifiedPrefixFixed=True,trueR205TailAndCuffFixed=True,
        targetMetricFrozen=True,originalCauchyStateUnchanged=True,
        allThirteenRowsInEachGroup=True,all2400ColumnsRetained=basis.dimension==2400,
        pointConfig=asdict(config),entrySHA256=sha(__file__),
        continuousCertificate=False,strongTargetComplete=False)
    initial=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_hash,
        carriedParentAcceptedSteps=carried,jointAcceptedSteps=prior_joint,
        jointAttemptCount=joint_attempts,actualTotalCartesianAcceptedSteps=carried+prior_joint,
        accepted=False,evaluation=values,groupValues=groups,
        actualOwnJointBaseline=True,oldObjectiveBaselineNotBorrowed=True)
    initial_sha=write(str(prefix)+"-initial.json",initial)
    emit("joint_actual_initial",initialSHA256=initial_sha,columns=basis.dimension,
        rows=values["rowCount"],R2=values["squaredNorm"],metric=values["maxRelativeMetric"],
        curvature=values["maxCurvature"],minImmersion=values["minImmersion"],
        held=values["minHeldDistance"],jointAcceptedSteps=prior_joint,
        actualCarriedParentSteps=carried)
    damping=recipe["lm"]["damping"]
    outputs=[]
    adjoint=None
    for iteration in range(1,args.steps+1):
        linear=TwoGrid(stream,basis,caches,weights,z,config,recipe)
        baseline=linear.statistics
        if adjoint is None:
            rng=np.random.default_rng(20261126)
            x=rng.normal(size=linear.shape[1])
            y=rng.normal(size=linear.shape[0])
            lhs=float(linear.matvec(x)@y)
            rhs=float(x@linear.rmatvec(y))
            relative=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs))
            if relative>1e-10:
                raise ArithmeticError("Actual two-grid shared-coordinate adjoint failed")
            adjoint=dict(actualSourceBothGrids=True,relativeDotError=relative,
                completeRows=linear.shape[0],completeColumns=linear.shape[1],
                solverOrContinuumCertificate=False)
            emit("joint_actual_adjoint",**adjoint)
            del x,y
        gradient=linear.rmatvec(linear.residual)
        trace=[]
        accepted=False
        selected=None
        value=baseline
        for attempt in range(1,recipe["lm"]["maxDampingAttempts"]+1):
            tick=time.monotonic()
            r=lsmr(linear.operator,-linear.residual,damp=math.sqrt(damping),
                atol=recipe["lsmr"]["atol"],btol=recipe["lsmr"]["btol"],
                conlim=recipe["lsmr"]["conditionLimit"],maxiter=recipe["lsmr"]["maxIterations"])
            y=r[0]
            if not np.all(np.isfinite(y)):
                raise ArithmeticError("Actual joint solve direction is nonfinite")
            dz=linear.unpack(y)
            jv=linear.matvec(y)
            slope=float(gradient@y)
            predicted=float(-2*slope-jv@jv)
            row=dict(kind="complete_two_grid_LSMR",attempt=attempt,damping=damping,
                istop=int(r[1]),iterations=int(r[2]),normr=float(r[3]),normar=float(r[4]),
                normA=float(r[5]),condition=float(r[6]),normx=float(r[7]),
                slope=slope,predictedReduction=predicted,
                completeRows=linear.shape[0],completeColumns=linear.shape[1],
                seconds=time.monotonic()-tick)
            trace.append(row)
            emit("joint_actual_LSMR",iteration=iteration,**row)
            if slope<0 and predicted>0:
                for alpha in recipe["lm"]["alphas"]:
                    candidate=z+alpha*dz
                    try:
                        trial,group=observe(stream,basis,caches,weights,candidate,config,recipe)
                        ok=(trial["squaredNorm"]<baseline["squaredNorm"] and
                            trial["squaredNorm"]<=baseline["squaredNorm"]+
                            2*recipe["lm"]["armijo"]*alpha*slope)
                        row=dict(kind="actual_complete_two_grid_trial",alpha=alpha,
                            actualValueEvaluated=True,accepted=bool(ok),R2=trial["squaredNorm"],
                            metric=trial["maxRelativeMetric"],curvature=trial["maxCurvature"],
                            minImmersion=trial["minImmersion"],held=trial["minHeldDistance"])
                        trace.append(row)
                        emit("joint_actual_trial",iteration=iteration,**row)
                        if ok:
                            z,value,groups=candidate,trial,group
                            accepted=True
                            selected=alpha
                            break
                    except (ValueError,ArithmeticError,FloatingPointError) as error:
                        row=dict(kind="actual_two_grid_domain_rejection",alpha=alpha,
                            actualValueEvaluated=False,accepted=False,error=str(error))
                        trace.append(row)
                        emit("joint_actual_trial",iteration=iteration,**row)
            if accepted:
                break
            damping*=10
        joint_attempts+=1
        prior_joint+=int(accepted)
        value,groups=observe(stream,basis,caches,weights,z,config,recipe)
        current=dict(common,z=z.ravel().tolist(),parentStateSHA256=parent_hash,
            actualJointInitialSHA256=initial_sha,carriedParentAcceptedSteps=carried,
            jointAcceptedSteps=prior_joint,jointAttemptCount=joint_attempts,
            actualTotalCartesianAcceptedSteps=carried+prior_joint,
            accepted=accepted,actualJointAcceptedStepsAdded=int(accepted),
            alpha=selected,baseline=baseline,evaluation=value,groupValues=groups,
            trace=trace,actualCompositeAdjointCheck=adjoint)
        state_path=Path(str(prefix)+f"-step{iteration:02d}-state.json")
        parent_hash=write(state_path,current)
        outputs.append(dict(stateFile=str(state_path),stateSHA256=parent_hash,
            jointAcceptedSteps=prior_joint,actualTotalAcceptedSteps=carried+prior_joint,
            accepted=accepted,evaluation=value,groupValues=groups))
        emit("joint_actual_state",iteration=iteration,stateSHA256=parent_hash,
            accepted=accepted,jointAcceptedSteps=prior_joint,totalAcceptedSteps=carried+prior_joint,
            R2=value["squaredNorm"],metric=value["maxRelativeMetric"],
            curvature=value["maxCurvature"],held=value["minHeldDistance"],
            minImmersion=value["minImmersion"],seconds=time.monotonic()-started)
        del linear,gradient
        gc.collect()
        if not accepted:
            break
    for row in prepared["caches"].values():
        for key in ("jets","radius"):
            if sha(row["files"][key])!=row["SHA256"][key]:
                raise ArithmeticError("Frozen source array changed during actual solve")
    output=dict(schema=SCHEMA+"-report",modelDefinition=model,modelDefinitionSHA256=model_hash,
        preparedSHA256=sha(args.prepared),inputStateSHA256=sha(args.state),
        initialSHA256=initial_sha,carriedParentAcceptedSteps=carried,
        jointAcceptedSteps=prior_joint,actualTotalAcceptedSteps=carried+prior_joint,
        jointAttemptCount=joint_attempts,outputs=outputs,
        allFrozenSourceCachesUnchanged=True,all13RowsInBothGrids=True,
        fieldOnlyChangedBySavedCompleteCoefficients=True,
        independentThirdObserverNotComputed=True,
        seconds=time.monotonic()-started,OSExitCode=None,externalExitReceiptRequired=True,
        continuousCertificate=False,strongTargetComplete=False)
    h=write(str(prefix)+"-report.json",output)
    emit("joint_actual_complete",reportSHA256=h,jointAcceptedSteps=prior_joint,
         totalAcceptedSteps=carried+prior_joint,seconds=output["seconds"])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scripts",type=Path,required=True)
    ap.add_argument("--base-entry",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-cartesian.py"))
    ap.add_argument("--background",type=Path,default=Path(__file__).with_name("6a65-geometry-gap-window-background.py"))
    ap.add_argument("--prepared",type=Path,required=True)
    ap.add_argument("--state",type=Path,required=True)
    ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--steps",type=int,default=3)
    args=ap.parse_args()
    if not 1<=args.steps<=20:
        raise ValueError("Explicit finite actual attempt batch required")
    if args.scripts.parents[2] in args.prefix.resolve().parents:
        raise ValueError("Actual coefficients and raw arrays must stay outside Git")
    try:
        run(args)
    except BaseException as error:
        f=Path(str(args.prefix)+"-failure.json")
        if not f.exists():
            f.parent.mkdir(parents=True,exist_ok=True)
            f.write_text(json.dumps(dict(schema=SCHEMA+"-actual-failure",error=str(error),
                traceback=traceback.format_exc(),acceptedStepsNotInferred=True),indent=2)+"\n")
        raise


if __name__=="__main__":
    main()

