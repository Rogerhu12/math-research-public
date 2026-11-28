#!/usr/bin/env python3
"""C2 physical meridian-Taylor and circular continuations of the actual Gamma95 inlet."""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"

import argparse
import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from numpy.polynomial import polynomial as poly


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


full = load(Path(__file__).with_name("2ecf-strong-hf-new-clock-full-position.py"), "front_actual_material_source")
hf, c = full.hf, full.c
SERIES = [np.array([1/math.factorial(2*i+j) for i in range(14)]) for j in (0,1)]
GL, GW = np.polynomial.legendre.leggauss(24)


def directed_tangent(port, distance, decay):
    # Finite degree polynomials define the actual curve even at A=0. The
    # trigonometric representation motivates the coefficients only.
    if decay:
        length = -decay*np.expm1(-distance/decay)
        speed = np.exp(-distance/decay)
    else:
        length, speed = distance, np.ones_like(distance)
    length, speed = length[:,None], speed[:,None]
    acc, au, auu = (port[k] for k in ("A","Au","Auu"))
    dot = lambda a,b: np.sum(a*b,axis=-1)
    k, ku, kuu = dot(acc,acc), 2*dot(acc,au), 2*(dot(au,au)+dot(acc,auu))
    z, zu, zuu = -k*length**2, -ku*length**2, -kuu*length**2
    zs = -2*k*length*speed
    out = [np.zeros(z.shape+(3,)) for i in range(4)]
    for j, name in enumerate(("V","A")):
        f = poly.polyval(z,SERIES[j])
        fz = poly.polyval(z,poly.polyder(SERIES[j]))
        fzz = poly.polyval(z,poly.polyder(SERIES[j],2))
        fac = length if j else 1.
        v, vu, vuu = (port[name+"u"*d] for d in range(3))
        a, b, cc = fac*f, fac*fz*zu, fac*(fzz*zu**2+fz*zuu)
        dd = fac*fz*zs + (speed*f if j else 0.)
        out[0] += a[...,None]*v
        out[1] += b[...,None]*v + a[...,None]*vu
        out[2] += cc[...,None]*v + 2*b[...,None]*vu + a[...,None]*vuu
        out[3] += dd[...,None]*v
    return out


def continuation(port, distance, family):
    d = distance[:,None,None]
    out = np.empty((len(d),6,len(port["P"]),3))
    if family == "quadratic":
        for col, order in ((0,0),(2,1),(5,2)):
            tag = "u"*order
            out[:,col] = port["P"+tag]+d*port["V"+tag]+.5*d*d*port["A"+tag]
        out[:,1] = port["V"]+d*port["A"]
        out[:,3] = port["A"]
        out[:,4] = port["Vu"]+d*port["Au"]
        return out
    decay = float(family)
    for i in range(0,len(d),8):
        sl = slice(i,i+8)
        x = distance[sl]
        t, tu, _, ts = directed_tangent(port,x,decay)
        out[sl,1],out[sl,3],out[sl,4] = t,ts,tu
        y = .5*x[:,None]*(GL+1)
        vals = directed_tangent(port,y.ravel(),decay)
        for col,order in ((0,0),(2,1),(5,2)):
            v = vals[order].reshape(len(x),len(GL),len(port["P"]),3)
            out[sl,col] = port["P"+"u"*order]+.5*x[:,None,None]*np.einsum("j,ijuc->iuc",GW,v)
    return out


def variation(packet, cont, distance, window):
    t = distance/window
    w = (1-t)**3*(1+3*t+6*t*t)
    ws = -30*t*t*(1-t)**2/window
    wss = -60*t*(1-t)*(1-2*t)/window**2
    w, ws, wss = (v[:,None,None] for v in (w,ws,wss))
    diff = cont-packet
    out = w[:,None]*diff
    out[:,1] += ws*diff[:,0]
    out[:,3] += 2*ws*diff[:,1]+wss*diff[:,0]
    out[:,4] += ws*diff[:,2]
    return out


def main(args):
    tic = time.monotonic()
    # Build complete 6615-space parent at zero, independently of that space's
    # later accepted coefficients. Only its true six-jet background is used.
    args.metric_sextic=.2
    args.curvature_tau=2.
    definition,basis,clock,physical,ind,weights,mods,radius,identity,expect = full.prepare(args)
    physical["independent"] = ind
    weights["independent"] = {k:np.ones(len(ind.nodes)) for k in ("metric","geometry","curvature")}
    stream=mods["stream"]
    cfg=stream.point.PointConfig(**definition["pointConfig"])
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","front_full_area")
    master=full.two.ArbitraryHF(args)
    data={}
    for name,v in physical.items():
        por=master.ports[0](v.u)
        distance=clock.jets(v.nodes)[0]-clock.jets([basis.c])[0][0]
        data[name]=dict(pts=v,port=por,distance=distance,weights=weights[name])
    def segment(name,ix,packet):
        obj=data[name];pts=obj["pts"];n=len(pts.u);tot=None;abar=0.
        for i in range(0,len(ix),12):
            sl=slice(i,i+12);j=ix[sl]
            a=pts.radius[j,0,None]
            w={k:v[j,None]/n for k,v in obj["weights"].items()}
            jets=packet[sl]
            pt=stream.point.PointLinearized(jets.swapaxes(1,2),a,cfg,w)
            s=stream._block_statistics(pt,pts.nodes[j],n)
            for key in ("worstMetric","worstCurvature"):s[key]["u"]+=pts.u[0]
            tot=stream._merge_statistics(tot,s)
            abar+=area.AreaPacket(jets,a,w["metric"],.5).stats["squaredNorm"]
        return tot,abar
    def merge(outside,inside):
        a,b=outside;c0,d0=inside
        total=stream._merge_statistics(copy.deepcopy(a),c0)
        t=full.lm.labels(total,clock)
        return dict(rows=14*t["pointCount"],metric=t["maxRelativeMetric"],curvature=t["maxCurvature"],
            original=t["squaredNorm"]+b+d0,area=b+d0,held=t["minHeldDistance"],guide=t["geometryMaximumViolations"],
            worstMetric=t["worstMetric"],worstCurvature=t["worstCurvature"])
    def disjoint(name,wid):
        ds=data[name]["distance"]
        i=np.flatnonzero((ds>=0.)&(ds<=wid));j=np.flatnonzero((ds<0.)|(ds>wid))
        pts=data[name]["pts"]
        return i,segment(name,j,pts.jets[j])
    def eval_window(names,wid,families,scales):
        split={n:disjoint(n,wid) for n in names}
        conts={}
        for name,(ix,_) in split.items():
            obj=data[name];pts=obj["pts"];d=obj["distance"][ix]
            for family in families:
                cont=continuation(obj["port"],d,family)
                conts[name,family]=variation(pts.jets[ix],cont,d,wid)
        values=[]
        for family in families:
            for scale in scales:
                groups={}
                for n,(ix,out) in split.items():
                    pts=data[n]["pts"]
                    groups[n]=merge(out,segment(n,ix,pts.jets[ix]+scale*conts[n,family]))
                values.append(dict(window=wid,family=family,scale=scale,stats=groups))
        return values
    rows=[eval_window(("training","observer"),.05,["quadratic"],[0.])[0]]
    rows[0].update(family="identity",window=0.)
    training=lambda r:max(z["metric"] for z in r["stats"].values())
    curvature=lambda r:max(z["curvature"] for z in r["stats"].values())
    cost=lambda r:sum(z["original"] for z in r["stats"].values())
    if abs(cost(rows[0])-expect[0])>1e-10:raise ArithmeticError("Complete unchanged original rows differ")
    for wid in args.windows:
        batch=eval_window(("training","observer"),wid,args.families,args.scales)
        rows.extend(batch)
        best=min(batch,key=curvature)
        print(json.dumps(dict(window=wid,bestK=curvature(best),G10Metric=training(best),original=cost(best),
            selection=[best["family"],best["scale"]])),flush=True)
    # Choose independently of G11. Register both nondominated extremes of a
    # useful 5% metric allowance plus a joint dimensionless minimax score.
    ok=[i for i,r in enumerate(rows) if training(r)<=1.05*training(rows[0])]
    minimax=lambda r:max(training(r)/training(rows[0]),curvature(r)/curvature(rows[0]))
    idx=dict(curvatureUnderMetricBudget=min(ok,key=lambda i:curvature(rows[i])),
             joint=min(range(len(rows)),key=lambda i:minimax(rows[i])),
             lowestCurvature=min(range(len(rows)),key=lambda i:curvature(rows[i])))
    independent={}
    for i in set(idx.values()):
        r=rows[i]
        a=eval_window(("independent",),r["window"] or .05,[r["family"] if i else "quadratic"],[r["scale"]])[0]
        independent[i]=a["stats"]["independent"]
    ans=dict(schema="true-HF-new-g-local-C2-Gamma95-front-continuation-v1",entry=c.sha(__file__),
        ownerSourceEntry=c.sha(full.__file__),identity=identity,diagonal=c.sha(args.diagonal),warp=c.sha(args.warp),
        actualG10=rows,chosenByG10=idx,actualG11=independent,curvatureSeriesDegree=13,positionIntegralGauss=24,
        G11UsedForSelection=False,timeSeconds=time.monotonic()-tic,wholeClosedReachCertified=False)
    digest=c.save(args.output,ans)
    print(json.dumps(dict(SHA=digest,chosen=idx,G11={i:(s["metric"],s["curvature"],s["held"]) for i,s in independent.items()})),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    hf.args_hf(ap)
    for k in ("diagonal","warp","output"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--windows",type=float,nargs="+",default=[.018,.035,.065,.11,.18,.26])
    ap.add_argument("--families",nargs="+",default=["quadratic","0",".035",".09"])
    ap.add_argument("--scales",type=float,nargs="+",default=[1.,.65,.35])
    main(ap.parse_args())
