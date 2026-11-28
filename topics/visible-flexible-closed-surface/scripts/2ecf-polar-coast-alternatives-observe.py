#!/usr/bin/env python3
"""Independent G11 for finite coast splice and clamped 18-mode continuation."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys

for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[k]="1"
import numpy as np


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
    return m


def run(args):
    here=Path(__file__).resolve().parent
    prior=load(here/"2ecf-polar-extended-coast-splice.py","coast_splice_inputs")
    modes=load(here/"2ecf-polar-clamped-coast-modes.py","clamped_coast_field")
    saved,definition,basis,_,mods,state=prior.source(args)
    src=prior.read(args.observer)
    if src["sourceIdentity"]!=definition["sourceIdentity"]:raise ValueError("Wrong H65 G11 source")
    for name in ("jets","radius","report"):
        if prior.sha(src["files"][name])!=src["SHA256"][name]:raise ValueError("Changed independent source")
    angles=np.asarray(src["angles"]);nodes=np.asarray(src["physicalNodes"])
    ra=np.load(src["files"]["radius"],mmap_mode="r")
    jets=np.load(src["files"]["jets"],mmap_mode="r")
    old=load(here/"2ecf-polar-c2-independent-g11-resume-observe.py","direct_angular_packet")
    z=np.asarray(state["z"]).reshape(basis.nb,basis.na)
    full=jets+old.direct_packet(basis,nodes,z,angles)
    ix,coast,meta=prior.verified_coast(args.coast,prior.sha(args.observer),"independent",nodes,angles)
    base=full[ix].copy()
    delta=coast-base
    stream=mods["stream"];cfg=stream.point.PointConfig(**definition["pointConfig"]);N=len(angles)
    def stats(position):
        full[ix]=position
        total=None
        for k in range(0,len(nodes),12):
            sl=slice(k,k+12);nr=len(nodes[sl]);w={n:np.ones((nr,1))/N for n in ("metric","curvature","geometry")}
            local=stream.point.PointLinearized(full[sl].swapaxes(1,2),ra[sl,0,None],cfg,w)
            one=stream._block_statistics(local,nodes[sl],N)
            for n in ("worstMetric","worstCurvature"):one[n]["u"]+=float(angles[0])
            total=stream._merge_statistics(total,one)
        return {k:total[k] for k in ("maxRelativeMetric","maxCurvature","minHeldDistance","minImmersion","worstMetric","worstCurvature")}
    if args.mode=="simple":
        sel=prior.read(args.input)
        if prior.sha(args.state)!=sel["parentStateSHA256"]:raise ValueError("Different parent state")
        a=sel["rows"][sel["selectedAlternativeIndex"]]
        variants=[("selected_G10_alternative_no_optimizer_accept",prior.splice(base,coast,nodes[ix],basis.c,a["hold"],a["stop"],a["strength"]))]
    else:
        sel=prior.read(args.input)
        if prior.sha(args.state)!=sel["parentSHA256"]:raise ValueError("Different parent state")
        mats=modes.radial(nodes[ix],basis.c)
        variants=[(str(r["own"]),base+modes.variation(mats,delta,np.asarray(r["amplitudes"]))) for r in sel["history"]]
    rows=[]
    for tag,position in variants:
        row=dict(field=tag,**stats(position))
        rows.append(row)
        print(tag,row["maxRelativeMetric"],row["maxCurvature"],row["minHeldDistance"],flush=True)
    out=dict(schema="independent-shifted-H65-coast-alternatives-v1",parentStateSHA256=prior.sha(args.state),
        correctionReportSHA256=prior.sha(args.input),sourceObserverSHA256=prior.sha(args.observer),
        extendedCoastSHA256=prior.sha(args.coast),entrySHA256=prior.sha(__file__),radials=len(nodes),angles=N,
        mode=args.mode,rows=rows,trainingNeverUsesObserver=True,finiteOnly=True)
    with args.output.open("x") as f:
        json.dump(out,f,indent=2)
        f.write("\n")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for k in ("scripts","state","prepared","observer","coast","input","output"):
        parser.add_argument("--"+k,required=True,type=Path)
    parser.add_argument("--mode",choices=("simple","clamped"),required=True)
    run(parser.parse_args())
