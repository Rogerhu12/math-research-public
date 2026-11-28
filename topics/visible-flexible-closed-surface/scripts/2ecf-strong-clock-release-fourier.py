#!/usr/bin/env python3
"""Fixed new material metric, frozen angular coast lifting, and full larger Fourier XYZ LM."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
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

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

local=Path(__file__).resolve().parent
lift=load(local/"2ecf-strong-clock-angular-coast.py","source_angular_coast")
c=lift.clockmod
lm=lift.lm

def main(args):
    tic=time.monotonic()
    saved,definition,coarse,old,raw,mods,warmz,alpha,radius,parent=c.inputs(args)
    clockrec=json.loads(args.clock.read_text())
    meta=clockrec["definition"]
    warm=json.loads(args.warm.read_text())
    g=json.loads(args.lifting.read_text())
    if (meta["chartBasis"]!=old.definition or meta["parentPreparedSHA256"]!=c.sha(args.prepared) or meta["parentDesignStateSHA256"]!=c.sha(args.parent)
        or clockrec["definitionSHA256"]!=c.stable(meta) or warm["model"]["clockDefinitionSHA256"]!=clockrec["definitionSHA256"]
        or g["warm"]!=c.sha(args.warm) or g["clock"]!=c.sha(args.clock) or g["entry"]!=c.sha(lift.__file__)
        or g["prepared"]!=c.sha(args.prepared) or g["observer"]!=c.sha(args.observer) or g["parent"]!=c.sha(args.parent)
        or g["radialInterior"]!=list(lift.RADIAL) or g["harmonics"]!=list(lift.FREQ)):
        raise ValueError("Identical transformed target, source and actual coast lifting required")
    clock=c.Clock(old,[float.fromhex(x) for x in meta["gammaHex"]])
    coeff=np.asarray([float.fromhex(x) for x in g["history"][-1]["controlsHex"]])
    z0=np.asarray(warm["z"]).reshape(old.nb,old.na)
    fhelper=load(args.helpers/"2ecf-polar-fourier-refinement.py","actual_newclock_extended_frequency")
    new,mapping=fhelper.refine(old,args.frequency)
    z,transfer=fhelper.prolongate(old,new,mapping,z0)
    basis=c.physical_basis(new,clock,clockrec["definitionSHA256"])
    prep=load(args.helpers/"2ecf-polar-extended-coast-splice.py","actual_clocked_coast_rebuild")
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","actual_shifted_angular_series").direct_packet
    obs=json.loads(args.observer.read_text())
    if obs["sourceIdentity"]!=definition["sourceIdentity"] or any(c.sha(p)!=obs["SHA256"][k] for k,p in obs["files"].items()):
        raise ValueError("Changed G11 source")
    raw["independent"]=SimpleNamespace(nodes=np.asarray(obs["physicalNodes"]),u=np.asarray(obs["angles"]),
        jets=np.load(obs["files"]["jets"],mmap_mode="r"),radius=np.load(obs["files"]["radius"],mmap_mode="r"))
    physical={}
    for name,cache in raw.items():
        xx=cache.nodes;u=cache.u
        independent=name=="independent"
        path=args.coast_dir/("polar-extended-coast-"+name+"-extended-coast.json")
        if c.sha(path)!=g["coasts"][name]:raise ValueError("Changed coast supplier")
        ix,coast,_=prep.verified_coast(path,c.sha(args.observer if independent else args.prepared),name,xx,u)
        _,h,hx=clock.jets(xx)
        p0=cache.jets[ix]+(direct(old,xx[ix],z0,u) if independent else old.packet(old.matrices(xx[ix]),z0,len(u)))
        delta=c.physical_jet(coast-p0,h[ix],hx[ix])
        q=c.physical_cache(radius.LogRadiusCache(coarse,cache,alpha),clock,radius)
        A=lift.angular(u)
        for j in range(0,len(ix),8):
            sl=slice(j,j+8)
            var=lift.variations(delta[sl],lift.radial(old.c,xx[ix[sl]],clock),A)
            q.jets[ix[sl]]+=np.einsum("rujcn,n->rujc",var,coeff,optimize=True).swapaxes(1,2)
        physical[name]=q
    g11=physical.pop("independent")
    stream=mods["stream"]
    basecfg=stream.point.PointConfig(**definition["pointConfig"])
    enhcfg=stream.point.PointConfig(**dict(definition["pointConfig"],curvature_tau=g["curvatureTau"]))
    basepoint,enhpoint=load(args.helpers/"2ecf-polar-peak-sextic-point.py","actual_newclock_peak").install(stream,g["metricSextic"])
    deps=radius.dependencies(args.scripts)
    area,joint=deps["area"],deps["joint"]
    load(args.helpers/"2ecf-polar-complete-two-grid-streamed.py","actual_newclock_joint").install(joint)
    normal=load(args.helpers/"2ecf-polar-complete-sparse-jet-normal.py","actual_newclock_full_normal")
    weights={n:{k:.5*np.asarray(v)*physical[n].h for k,v in saved["caches"][n]["weights"].items()} for n in physical}
    recipe=copy.deepcopy(definition["recipe"])
    recipe["cachePointBlocks"]=False
    recipe["basis"].update(radialBasisCount=basis.nb,maxAngularFrequency=basis.M,support="clocked b..S")
    ar=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    mod=dict(schema="new-clock-frozen-angular-coast-carrier-full-Fourier-XYZ-LM-v1",entry=c.sha(__file__),clock=c.sha(args.clock),
        actualMetric=clockrec["definitionSHA256"],prepared=c.sha(args.prepared),parent=c.sha(args.parent),warm=c.sha(args.warm),
        observer=c.sha(args.observer),lifting=c.sha(args.lifting),angularCarrier=coeff.tolist(),frequency=args.frequency,
        liftSpace=g["additionalPositionColumns"],oldM=old.M,xyzColumns=basis.dimension,rows=4291840,physicalBasis=basis.definition,
        metricSextic=g["metricSextic"],curvatureTau=g["curvatureTau"],cutS=meta["cutNew"],h2="physical ds",
        newMetricDesignAccepts=0,G11NeverInTraining=True,fullCartesianCrosses=True)
    modelsha=c.stable(mod)
    damping=args.damping;own=0
    if args.state:
        last=json.loads(args.state.read_text())
        if last["modelSHA256"]!=modelsha:raise ValueError("Changed fixed-g problem")
        z=np.asarray(last["z"]).reshape(basis.nb,basis.na)
        damping=last["nextDamping"]
        own=last["own"]
    def observe(zz):
        stream.point.PointLinearized=basepoint
        try:
            base=area.observe(joint,stream,basis,physical,weights,zz,basecfg,recipe,ar)[0]
        finally:
            stream.point.PointLinearized=enhpoint
        enhanced=area.observe(joint,stream,basis,physical,weights,zz,enhcfg,recipe,ar)[0]
        return lm.labels(base,clock),lm.labels(enhanced,clock)
    def observe11(zz):
        total=None;x=g11.nodes;u=g11.u
        for start in range(0,len(x),12):
            sl=slice(start,start+12)
            packet=g11.jets[sl]+direct(basis,x[sl],zz,u)
            point=basepoint(packet.swapaxes(1,2),g11.radius[sl,0,None],basecfg,
                {k:np.ones((len(x[sl]),1))/len(u) for k in ("metric","curvature","geometry")})
            part=stream._block_statistics(point,x[sl],len(u))
            for key in ("worstMetric","worstCurvature"):part[key]["u"]+=u[0]
            total=stream._merge_statistics(total,part)
        for key in ("squaredNorm","groupSquaredNorm"):total.pop(key,None)
        return lm.labels(total,clock)
    base,enh=observe(z)
    ind=observe11(z)
    parentrow=g["history"][-1]
    if not args.state:
        d0=base["squaredNorm"]-sum(q["original"] for q in parentrow["G10"].values())
        d1=enh["squaredNorm"]-sum(q["enhanced"] for q in parentrow["G10"].values())
        d2=ind["maxRelativeMetric"]-parentrow["G11"]["statistics"]["maxRelativeMetric"]
        if max(abs(d0),abs(d1),abs(d2))>1e-10:raise ArithmeticError(("Real inherited field and costs disagree",d0,d1,d2))
    def out(step,accepted,trace):
        obj=dict(model=mod,modelSHA256=modelsha,z=z.ravel().tolist(),own=own,nextDamping=damping,accepted=accepted,
            fullG10Original=base,fullG10Enhanced=enh,G11=ind,trace=trace,coefficientTransfer=transfer,
            seconds=time.monotonic()-tic,wholeClosedReachCertified=False,continuousMetricCertified=False)
        path=Path(str(args.prefix)+f"-{step:02}.json")
        digest=c.save(path,obj)
        print(json.dumps(dict(step=step,own=own,accepted=accepted,original=base["squaredNorm"],enhanced=enh["squaredNorm"],
            G11Metric=ind["maxRelativeMetric"],G11Curvature=ind["maxCurvature"],held=ind["minHeldDistance"],
            columns=basis.dimension,rows=4291840,seconds=obj["seconds"],SHA256=digest)),flush=True)
    out(0,False,[])
    for it in range(1,args.steps+1):
        linear=area.CompleteAreaTwoGrid(joint,stream,basis,physical,weights,z,enhcfg,recipe,ar)
        if linear.shape!=(4291840,basis.dimension) or abs(linear.statistics["squaredNorm"]-enh["squaredNorm"])>1e-10:
            raise ArithmeticError("Full enhanced physical linearization mismatch")
        trace=[];accepted=False
        for unused in range(5):
            aug=normal.SameSobolevAreaFullBandAugmented(linear,damping,eta=damping)
            del aug.blocks.normal_band,aug.rhs
            grad=aug.raw_transpose(linear.residual)
            dz=-aug.blocks.unpack(aug.blocks.transpose(grad))
            residual=aug.physical_normal_residual(dz)
            rel=float(np.linalg.norm(residual)/np.linalg.norm(grad))
            for _ in range(3):
                if rel<=1e-10:break
                dz-=aug.blocks.unpack(aug.blocks.transpose(residual))
                residual=aug.physical_normal_residual(dz)
                rel=float(np.linalg.norm(residual)/np.linalg.norm(grad))
            if rel>1e-7:raise ArithmeticError("Full unprojected physical normal residual")
            jv=aug.raw_matvec(dz)
            slope=float(grad.ravel()@dz.ravel());j2=float(jv@jv)
            trace.append(dict(damping=damping,slope=slope,normalRelative=rel,assembly=aug.blocks.receipt))
            del aug,grad,residual,jv
            gc.collect()
            for t in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125):
                b1,e1=observe(z+t*dz)
                ok=(slope<0 and b1["squaredNorm"]<base["squaredNorm"] and e1["squaredNorm"]<enh["squaredNorm"]
                    and e1["squaredNorm"]<=enh["squaredNorm"]+2e-4*t*slope)
                trace.append(dict(length=t,original=b1["squaredNorm"],enhanced=e1["squaredNorm"],accepted=ok))
                if ok:
                    gain=(enh["squaredNorm"]-e1["squaredNorm"])/(-2*t*slope-t*t*j2)
                    z=z+t*dz;base,enh=b1,e1
                    if t==1 and gain>.75:damping=max(1e-12,damping/3)
                    elif t<1 or gain<.25:damping=min(1e4,2*damping)
                    accepted=True
                    break
            if accepted:break
            damping=min(1e4,damping*10)
        own+=int(accepted)
        ind=observe11(z)
        out(it,accepted,trace)
        del linear
        gc.collect()
        if not accepted:break

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    c.common_args(ap)
    for k in ("clock","observer","warm","lifting","coast-dir","prefix"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--state",type=Path)
    ap.add_argument("--frequency",type=int,default=36)
    ap.add_argument("--steps",type=int,default=3)
    ap.add_argument("--damping",type=float,default=.03)
    main(ap.parse_args())
