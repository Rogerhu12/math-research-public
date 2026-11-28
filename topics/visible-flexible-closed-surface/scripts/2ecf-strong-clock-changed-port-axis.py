#!/usr/bin/env python3
"""Reconstruct a selected R205 changed whole tail for an actual axial turning problem."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import numpy as np
def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);sys.modules[n]=m;spec.loader.exec_module(m);return m
local=Path(__file__).resolve().parent
cut=load(local/"2ecf-strong-clock-r205-port-design.py","newport_axial_provider")
c=cut.c
def main(args):
    p=local/("2ecf-strong-short-axis-minimax.py" if args.minimum else "2ecf-strong-axial-curve-physical-design.py")
    nominal=load(p,"actual_axis_BVP")
    get=nominal.c.inputs
    selection=json.loads(args.selection.read_text())
    if selection["prepared"]!=c.sha(args.prepared) or selection["parent"]!=c.sha(args.parent) or selection["clock"]!=c.sha(args.clock):
        raise ValueError("New outer port definition changed")
    row=selection["rows"][args.port_index]
    oldA=selection["oldA"];A=oldA*row["Afraction"];beta=row["betaPi"]*np.pi;frac=row["startFraction"]
    def substituted(a):
        saved,df,coarse,full,caches,mods,z,alpha,radius,parent=get(a)
        h=load(a.scripts/"6a65-geometry-cauchy-unit-t-warm.py","newport_axis_endpoint")
        cache=caches["training"]
        raw,err=cut.changed(h,cache,cache.jets,oldA,A,selection["Z"],full.c,full.end,frac,beta)
        caches["training"]=radius.ArrayCache(cache.nodes,cache.u,raw,cache.radius)
        return saved,df,coarse,full,caches,mods,z,alpha,radius,parent
    nominal.c.inputs=substituted
    out=args.output
    with tempfile.TemporaryDirectory(dir=out.parent) as tmp:
        args.output=Path(tmp)/"axes.json"
        nominal.design(args)
        r=json.loads(args.output.read_text())
    r.update(changedEndSourceEntry=c.sha(__file__),oldAxisEntry=c.sha(p),selection=c.sha(args.selection),
        portIndex=args.port_index,A=A,betaPi=row["betaPi"],startFraction=frac,targetFrozenPhysicalRadiusUnchanged=True)
    print(json.dumps(dict(SHA=c.save(out,r),A=A,axes={k:[v.get("success"),v.get("independent8193MaximumCurvature")] for k,v in r["axes"].items()})),flush=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser();c.common_args(ap)
    for k in ("clock","selection","output"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--port-index",type=int,required=True);ap.add_argument("--minimum",action="store_true")
    ap.add_argument("--spans",type=int,default=24);ap.add_argument("--kappa",type=float,default=9.5)
    ap.add_argument("--smoothing",type=float,default=1e-6);ap.add_argument("--winding",type=int,default=0)
    ap.add_argument("--seed-count",type=int,default=2)
    main(ap.parse_args())
