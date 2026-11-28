#!/usr/bin/env python3
"""Fixed-new-metric complete G10 physical Cartesian LM and independent shifted G11."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import copy
import gc
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

c=module(Path(__file__).with_name("2ecf-strong-new-material-clock.py"),"actual_material_clock")
def emit(event,**values):
    print(json.dumps(dict(event=event,**values),allow_nan=False),flush=True)

def labels(stat,clock):
    stat=copy.deepcopy(stat)
    for name in ("worstMetric","worstCurvature"):
        if name in stat:
            x=stat[name].pop("s")
            stat[name]["x"]=x
            stat[name]["s"]=float(clock.jets([x])[0][0])
    return stat

def run(args):
    start=time.monotonic()
    saved,definition,coarse,old,caches,mods,z,alpha,radius,parent=c.inputs(args)
    spec=json.loads(args.clock.read_text())
    meta=spec["definition"]
    if (spec["definitionSHA256"]!=c.stable(meta) or meta["parentPreparedSHA256"]!=c.sha(args.prepared)
            or meta["parentDesignStateSHA256"]!=c.sha(args.parent) or meta["fitEntrySHA256"]!=c.sha(c.__file__)
            or meta["chartBasis"]!=old.definition):
        raise ValueError("Exact newly fitted clock and its true warm parent required")
    clock=c.Clock(old,[float.fromhex(q) for q in meta["gammaHex"]])
    basis=c.physical_basis(old,clock,spec["definitionSHA256"])
    if any(mat.nnz for mat in basis.matrices(np.array([old.c,old.end]))):
        raise ArithmeticError("Clamped physical corrections must vanish through second order at both ports")
    deps=radius.dependencies(args.scripts)
    joint=deps["joint"]
    area=deps["area"]
    here=args.helpers
    normal=module(here/"2ecf-polar-complete-sparse-jet-normal.py","actual_newclock_normal")
    module(here/"2ecf-polar-complete-two-grid-streamed.py","actual_newclock_streamed").install(joint)
    stream=mods["stream"]
    recipe=copy.deepcopy(definition["recipe"])
    recipe["cachePointBlocks"]=False
    recipe["basis"].update(radialBasisCount=basis.nb,support="clocked_b_to_cut")
    config=stream.point.PointConfig(**definition["pointConfig"])
    physical={k:c.physical_cache(radius.LogRadiusCache(coarse,cache,alpha),clock,radius) for k,cache in caches.items()}
    weights={k:{j:.5*np.asarray(v)*physical[k].h for j,v in saved["caches"][k]["weights"].items()} for k in physical}
    aconfig=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    observed=json.loads(args.observer.read_text())
    if (observed["sourceIdentity"]!=definition["sourceIdentity"] or observed["basis"]!=definition["basis"]
            or any(c.sha(p)!=observed["SHA256"][k] for k,p in observed["files"].items())):
        raise ValueError("Complete bound independent source required")
    x=np.asarray(observed["physicalNodes"])
    u=np.asarray(observed["angles"])
    if (len(x),len(u),len(np.setdiff1d(x,caches["training"].nodes)))!=(668,256,540):
        raise ValueError("The prescribed independent G11 requires all 540 fresh chart indices")
    g11raw=SimpleNamespace(nodes=x,u=u,jets=np.load(observed["files"]["jets"],mmap_mode="r"),
        radius=np.load(observed["files"]["radius"],mmap_mode="r"))
    g11=c.physical_cache(radius.LogRadiusCache(coarse,g11raw,alpha),clock,radius)
    direct=module(here/"2ecf-polar-c2-independent-g11-resume-observe.py","newclock_direct_sums").direct_packet
    model=dict(schema="strong-clocked-physical-fixed-g-cartesian-LM-v1",clockDefinitionSHA256=spec["definitionSHA256"],
        prepareSHA256=c.sha(args.prepared),warmParentSHA256=c.sha(args.parent),independentSHA256=c.sha(args.observer),
        solveEntrySHA256=c.sha(__file__),clockEntrySHA256=c.sha(c.__file__),basis=basis.definition,
        pointConfig=definition["pointConfig"],angularFrequency=basis.M,fullRows=4291840,columns=6615,
        incidentCacheSHA256={k:v["SHA256"] for k,v in saved["caches"].items()},
        shiftedObserverCacheSHA256=observed["SHA256"],fixedPhysicalMetric=True,
        originalGuideAndAllCrossTerms=True,minimumPhysicalSpeedBound=meta["speedLowerBound"],
        cutNew=meta["cutNew"],observerNeverInOptimization=True,
        bothOriginalTrainingGroupsRetained=True,physicalSobolevUsesClockedDerivativesAndWeights=True)
    modelsha=c.stable(model)
    if args.state:
        state=json.loads(args.state.read_text())
        if state["modelSHA256"]!=modelsha or state["model"]!=model:
            raise ValueError("Only this fixed new metric and complete physical state may continue")
        z=np.asarray(state["z"]).reshape(old.nb,old.na)
        own=state["ownAccepts"]
        attempts=state["ownAttempts"]
        damping=state["nextDamping"]
    else:
        own=attempts=0
        damping=args.damping
    def observe(q):
        total,groups=area.observe(joint,stream,basis,physical,weights,q,config,recipe,aconfig)
        return labels(total,clock),{k:labels(v,clock) for k,v in groups.items()}
    def independent(q):
        total=None
        for lo in range(0,len(x),12):
            sl=slice(lo,lo+12)
            p=g11.jets[sl]+direct(basis,x[sl],q,u)
            a=g11.radius[sl,0,None]
            linear=stream.point.PointLinearized(p.swapaxes(1,2),a,config,
                {j:np.ones((len(x[sl]),1))/len(u) for j in ("metric","curvature","geometry")})
            part=stream._block_statistics(linear,x[sl],len(u))
            for k in ("worstMetric","worstCurvature"):
                part[k]["u"]+=u[0]
            total=stream._merge_statistics(total,part)
        total.pop("squaredNorm",None)
        total.pop("groupSquaredNorm",None)
        return labels(total,clock)
    value,groups=observe(z)
    g11value=independent(z)
    if not args.state and abs(value["squaredNorm"]-spec["fittedNewMaterialObjective"])>3e-10:
        raise ArithmeticError("New physical six-jet objective and exact full radial power sum disagree")
    def out(step,accepted,trace,prev):
        obj=dict(model=model,modelSHA256=modelsha,z=z.ravel().tolist(),ownAccepts=own,ownAttempts=attempts,
            nextDamping=damping,accepted=accepted,evaluation=value,trainingGroups=groups,independentG11=g11value,
            trace=trace,parentStateSHA256=prev,seconds=time.monotonic()-start,
            continuousMetricCertified=False,wholeClosedReachCertified=False,finiteSampleOnly=True)
        dest=Path(str(args.prefix)+f"-{step:02}.json")
        h=c.save(dest,obj)
        emit("actual_complete_new_s_field",path=str(dest),SHA256=h,ownAccepts=own,accepted=accepted,
            quartic=value["squaredNorm"],trainMetric=value["maxRelativeMetric"],metric=g11value["maxRelativeMetric"],
            curvature=g11value["maxCurvature"],held=g11value["minHeldDistance"],nextDamping=damping,seconds=obj["seconds"])
        return h
    prev=out(0,False,[],c.sha(args.state) if args.state else None)
    for st in range(1,args.steps+1):
        linear=area.CompleteAreaTwoGrid(joint,stream,basis,physical,weights,z,config,recipe,aconfig)
        if linear.shape!=(4291840,6615) or abs(linear.statistics["squaredNorm"]-value["squaredNorm"])>1e-10:
            raise ArithmeticError("Physical baseline, columns or rows changed")
        accepted=False
        trace=[]
        for j in range(6):
            aug=normal.SameSobolevAreaFullBandAugmented(linear,damping,eta=damping)
            del aug.blocks.normal_band,aug.rhs
            grad=aug.raw_transpose(linear.residual)
            dz=-aug.blocks.unpack(aug.blocks.transpose(grad))
            res=aug.physical_normal_residual(dz)
            nr=float(np.linalg.norm(res)/np.linalg.norm(grad))
            for _ in range(3):
                if nr<=1e-10:break
                dz-=aug.blocks.unpack(aug.blocks.transpose(res))
                res=aug.physical_normal_residual(dz)
                nr=float(np.linalg.norm(res)/np.linalg.norm(grad))
            if nr>1e-7:raise ArithmeticError("Full physical normal unresolved")
            image=aug.raw_matvec(dz)
            slope=float(grad.ravel()@dz.ravel())
            j2=float(image@image)
            trace.append(dict(kind="full_normal",lambdaUsed=damping,slope=slope,j2=j2,relative=nr,
                assembly=aug.blocks.receipt))
            emit("full_normal",step=st,normalRelative=nr,slope=slope,seconds=time.monotonic()-start)
            del aug,grad,res,image
            gc.collect()
            if slope<0 and -2*slope-j2>0:
                for length in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
                    trial,trialgroups=observe(z+length*dz)
                    before=value["squaredNorm"]
                    ok=trial["squaredNorm"]<before and trial["squaredNorm"]<=before+2e-4*length*slope
                    trace.append(dict(kind="true_full_nonlinear_trial",length=length,cost=trial["squaredNorm"],
                        trainMetric=trial["maxRelativeMetric"],curvature=trial["maxCurvature"],accepted=ok))
                    if ok:
                        z=z+length*dz
                        value,groups=trial,trialgroups
                        gain=(before-value["squaredNorm"])/(-2*length*slope-length**2*j2)
                        if length==1 and gain>.75:damping=max(1e-12,damping/3)
                        elif length<1 or gain<.25:damping=min(damping*2,1e4)
                        accepted=True
                        break
            if accepted:break
            damping=min(1e4,10*damping)
        attempts+=1
        own+=int(accepted)
        g11value=independent(z)
        prev=out(st,accepted,trace,prev)
        del linear
        gc.collect()
        if not accepted:break

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    c.common_args(ap)
    for k in ("clock","observer","prefix"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--state",type=Path)
    ap.add_argument("--steps",type=int,default=3)
    ap.add_argument("--damping",type=float,default=.012)
    run(ap.parse_args())
