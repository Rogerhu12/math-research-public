#!/usr/bin/env python3
"""C2 Cartesian splices to the longer R137 ruling, scored against the original target metric."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):
    os.environ[k]="1"
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def splice(x,coast,nodes,b,hold,stop,strength):
    if not 0<=hold<stop or not 0<strength<=1:
        raise ValueError("Positive C2 splice window required")
    t=np.clip((nodes-(b+hold))/(stop-hold),0.,1.)
    w=strength*(1-t)**3*(1+3*t+6*t*t)
    ws=-strength*30*t*t*(1-t)**2/(stop-hold)
    wss=-strength*60*t*(1-t)*(1-2*t)/(stop-hold)**2
    w,ws,wss=(v[:,None,None] for v in (w,ws,wss))
    delta=coast-x
    new=x+w[:,None]*delta
    new[:,1]+=ws*delta[:,0]
    new[:,3]+=2*ws*delta[:,1]+wss*delta[:,0]
    new[:,4]+=ws*delta[:,2]
    return new


def source(args):
    here=Path(__file__).resolve().parent
    prepare=load(here/"2ecf-polar-raw-ramp-source-compose.py","coast_splice_source")
    saved,definition,fullbasis,caches,mods,*_=prepare.validate_prepared(args)
    basis,_=load(here/"2ecf-polar-fixed-prefix-position-basis.py","coast_splice_basis").restrict(fullbasis)
    state=read(args.state)
    if (state["preparedSHA256"]!=sha(args.prepared) or state["modelDefinition"]["basis"]!=basis.definition
        or state["modelDefinition"]["sourceIdentity"]!=definition["sourceIdentity"]
        or state["modelDefinition"]["solveEntrySHA256"]!=sha(here/"2ecf-polar-raw-ramp-suffix-solve.py")):
        raise ValueError("The actual H65 coarse suffix warm field must remain identified")
    return saved,definition,basis,caches,mods,state


def verified_coast(path,source_sha,group,nodes,angles):
    meta=read(path)
    if (meta["sourceSHA256"]!=source_sha or meta["group"]!=group or sha(meta["packet"])!=meta["packetSHA256"]):
        raise ValueError("Prolonged ruling has changed source or wrong angular grid")
    with np.load(meta["packet"]) as data:
        index=data["indices"].copy()
        if not np.array_equal(nodes[index],data["nodes"]) or not np.array_equal(angles,data["angles"]):
            raise ValueError("Physical node or angle mismatch")
        return index,data["jets"].copy(),meta


def main(args):
    tick=time.monotonic()
    saved,definition,basis,caches,mods,state=source(args)
    z=np.asarray(state["z"]).reshape(basis.nb,basis.na)
    here=Path(__file__).resolve().parent
    zero=np.zeros_like(z)
    joint=load(args.scripts/"6a65-geometry-gap-window-two-grid-cartesian.py","splice_joint")
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","splice_area")
    load(here/"2ecf-polar-complete-two-grid-streamed.py","splice_streaming").install(joint)
    config=mods["stream"].point.PointConfig(**definition["pointConfig"])
    weights={k:{name:.5*np.asarray(v) for name,v in rec["weights"].items()} for k,rec in saved["caches"].items()}
    recipe=copy.deepcopy(definition["recipe"])
    recipe["cachePointBlocks"]=False
    recipe["basis"].update(radialBasisCount=basis.nb,support="b_to_developed_cut")
    area_definition=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    members={}
    coast_only={}
    for key,path in (("training",args.training_coast),("observer",args.observer_coast)):
        cache=caches[key]
        ix,coast,meta=verified_coast(path,sha(args.prepared),key,cache.nodes,cache.u)
        pos=cache.jets+basis.packet(basis.matrices(cache.nodes),z,len(cache.u))
        from_base=pos[ix].copy()
        actual=copy.copy(cache)
        actual.jets=pos
        members[key]=(actual,ix,coast,from_base)
        ex=load(here/"2ecf-polar-source-prefix-spans.py","splice_metric_"+key)
        m,k=ex.extrema(coast,cache.radius[ix,0,None])
        coast_only[key]=dict(fullRawCoastMetricVersusActualTarget=float(m.max()),fullRawCoastCurvature=float(k.max()),
            sampledRulingMaximumHeight=float(coast[:,0,:,2].max()),coastCacheSHA256=sha(path))
    def observe(hold,stop,strength):
        for actual,ix,coast,base in members.values():
            actual.jets[ix]=base if strength==0 else splice(base,coast,actual.nodes[ix],basis.c,hold,stop,strength)
        grouped={k:m[0] for k,m in members.items()}
        val,_=area.observe(joint,mods["stream"],basis,grouped,weights,zero,config,recipe,area_definition)
        return {k:val[k] for k in ("squaredNorm","groupSquaredNorm","maxRelativeMetric","maxCurvature","minHeldDistance","worstMetric","worstCurvature","rowCount")}
    rows=[]
    for hold,stop,strength in [(0.,.1,0.)]+[(h,s,a) for h in (.015,.04) for s in (.12,.18,.24) for a in (.5,1.)]:
        info=observe(hold,stop,strength)
        rows.append(dict(hold=hold,stop=stop,strength=strength,**info))
        print(hold,stop,strength,info["squaredNorm"],info["maxRelativeMetric"],info["maxCurvature"],flush=True)
    base=rows[0]
    if abs(base["squaredNorm"]-state["evaluation"]["squaredNorm"])>1e-11:
        raise ArithmeticError("Unspliced original full field is not identified")
    best=min(range(1,len(rows)),key=lambda j:rows[j]["squaredNorm"])
    out=dict(schema="physical-H65-original-target-complete-G10-extended-coast-splice-selection-v1",
        entrySHA256=sha(__file__),parentStateSHA256=sha(args.state),preparedSHA256=sha(args.prepared),
        unmodifiedTargetAndAllPhysicalRows=True,sourceReplacementOnly=True,coastStandalone=coast_only,
        rows=rows,selectedAlternativeIndex=best,alternativeBettersOriginal=rows[best]["squaredNorm"]<base["squaredNorm"],
        selection="smallest full G10 R14 squared among the twelve genuine alternative splices; original reference recorded separately",
        independentGridNeverRead=True,ownOptimizationAccepts=0,seconds=time.monotonic()-tick)
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for k in ("scripts","prepared","state","training-coast","observer-coast","output"):
        parser.add_argument("--"+k,required=True,type=Path)
    main(parser.parse_args())
