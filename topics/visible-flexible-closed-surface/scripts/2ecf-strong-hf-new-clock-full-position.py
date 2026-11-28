#!/usr/bin/env python3
"""Full Cartesian corrections of a genuine material-warped HF surface at fixed new g."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import copy
import gc
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


two = load(Path(__file__).with_name("2ecf-strong-hf-two-material-clocks.py"), "newHFmaterial")
hf = two.hf
c = hf.c
lm = hf.d.lm


def prepare(args):
    saved, definition, chart, mods, groups, _ = hf.build(args)
    target = json.loads(args.diagonal.read_text())
    warp = json.loads(args.warp.read_text())
    spec = target["definition"]
    same = (target["definitionSHA256"] == c.stable(spec)
            and spec["entry"] == c.sha(hf.__file__)
            and spec["basePositionFile"] == c.sha(args.field)
            and spec["baseAngleClock"] == c.sha(args.angular_clock)
            and spec["parentPrepared"] == c.sha(args.prepared)
            and spec["parentDesign"] == c.sha(args.parent)
            and target["parentObserver"] == c.sha(args.observer)
            and warp["entry"] == c.sha(two.__file__)
            and warp["target"] == c.sha(args.diagonal)
            and warp["fixedMetric"] == target["definitionSHA256"])
    if not same:
        raise ValueError("Complete source, material warp and frozen metric must match")
    take = warp["actualG10Trials"][warp["chosen"]]
    factor = take["factor"]
    arb = two.ArbitraryHF(args)
    if not np.array_equal(warp["radialKnots"], arb.orig.knots):
        raise ValueError("Warp radial knots differ")
    p = two.Wave(arb.orig.knots, warp["pFrequencies"], False)
    q = two.Wave(arb.orig.knots, warp["qFrequencies"], True)
    pv = factor * np.array([float.fromhex(v) for v in warp["pCoefficientHex"]])
    qv = factor * np.array([float.fromhex(v) for v in warp["qCoefficientHex"]])
    for group in groups.values():
        xx = group["cache"].nodes
        u = group["cache"].u
        live = np.flatnonzero((xx >= chart.c) & (xx <= chart.end))
        if factor:
            for j in range(0, len(live), 12):
                part = live[j:j+12]
                group["jets"][part] = arb.actual(xx[part], u, p, q, pv, qv)
    ce = np.array([float.fromhex(v) for v in spec["CEradialHex"]])
    ca = np.array([float.fromhex(v) for v in spec["CGangularHex"]])
    clock, cache = hf.physical(args, groups, chart, ce, ca)
    basis = c.physical_basis(chart, clock, target["definitionSHA256"])
    radius = load(args.helpers / "2ecf-polar-log-radius-operator.py", "physical_radius_cache")
    g11 = cache.pop("independent")
    weights = {n: {k: .5*np.asarray(w)*obj.h for k, w in saved["caches"][n]["weights"].items()}
               for n, obj in cache.items()}
    physical = {n: radius.ArrayCache(obj.nodes, obj.u, obj.jets, obj.radius) for n, obj in cache.items()}
    metadata = dict(schema="new-length-two-material-clock-HF-fixed-g-full-Cartesian-v1",
        entry=c.sha(__file__), physicalSource=c.sha(args.field), baseAngleClock=c.sha(args.angular_clock),
        target=c.sha(args.diagonal), actualMetric=target["definitionSHA256"], warp=c.sha(args.warp),
        prepared=c.sha(args.prepared), parent=c.sha(args.parent), observer=c.sha(args.observer),
        ramp=c.sha(args.ramp), coast=c.sha(args.coast), inputMaterialWarpAccept=int(warp["accepted"]),
        angularFrequency=chart.M, xyzColumns=basis.dimension, physicalBasis=basis.definition,
        rows=4291840, metricSextic=args.metric_sextic, curvatureTau=args.curvature_tau, h2="physical ds",
        G11NeverInTraining=True, fullCartesianCrosses=True)
    expected = (sum(v["original"] for v in take["G10"].values()), warp["actualG11"]["metric"])
    return definition, basis, clock, physical, g11, weights, mods, radius, metadata, expected


def main(args):
    tic = time.monotonic()
    definition, basis, clock, physical, g11, weights, mods, radius, mod, expected = prepare(args)
    gc.collect()
    direct = load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","actual_G11").direct_packet
    stream = mods["stream"]
    basecfg = stream.point.PointConfig(**definition["pointConfig"])
    enhcfg = stream.point.PointConfig(**dict(definition["pointConfig"], curvature_tau=args.curvature_tau))
    basepoint, enhpoint = load(args.helpers/"2ecf-polar-peak-sextic-point.py", "newHFpeak").install(stream,args.metric_sextic)
    deps = radius.dependencies(args.scripts)
    area, joint = deps["area"], deps["joint"]
    load(args.helpers/"2ecf-polar-complete-two-grid-streamed.py", "newHFjoint").install(joint)
    normal = load(args.helpers/"2ecf-polar-complete-sparse-jet-normal.py", "newHFnormal")
    recipe = copy.deepcopy(definition["recipe"])
    recipe["cachePointBlocks"] = False
    recipe["basis"].update(radialBasisCount=basis.nb, maxAngularFrequency=basis.M, support="clocked b..S")
    ar = dict(targetAreaRatio=.5, strength=1., reciprocalPower=2)
    modelsha = c.stable(mod)
    damping = args.damping
    own = 0
    z = np.zeros((basis.nb, basis.na))
    if args.state:
        last = json.loads(args.state.read_text())
        if last["modelSHA256"] != modelsha:
            raise ValueError("Changed fixed-g problem")
        z = np.asarray(last["z"]).reshape(basis.nb, basis.na)
        damping = last["nextDamping"]
        own = last["own"]
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
    if not args.state:
        error = max(abs(base["squaredNorm"]-expected[0]), abs(ind["maxRelativeMetric"]-expected[1]))
        if error > 2e-10:
            raise ArithmeticError(("New true source / complete parent rows differ",error))
    def out(step,accepted,trace):
        obj=dict(model=mod,modelSHA256=modelsha,z=z.ravel().tolist(),own=own,nextDamping=damping,accepted=accepted,
            fullG10Original=base,fullG10Enhanced=enh,G11=ind,trace=trace,
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


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    hf.args_hf(ap)
    for name in ("diagonal", "warp", "prefix"):
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--state", type=Path)
    ap.add_argument("--steps", type=int, default=3)
    ap.add_argument("--damping", type=float, default=.035)
    ap.add_argument("--curvature-tau", type=float, default=2.)
    ap.add_argument("--metric-sextic", type=float, default=.2)
    main(ap.parse_args())
