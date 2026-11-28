#!/usr/bin/env python3
"""Fresh weighted physical radius-jet queries for the frozen HF metric on true inserted nodes."""
import os
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[k]="1"

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


def load(p,n):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s)
    sys.modules[n]=m
    s.loader.exec_module(m)
    return m


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def nodes(prepared,observer,b,S):
    train=np.asarray(prepared["caches"]["training"]["nodes"])
    ind=set(observer["physicalNodes"])
    tr=train[(train>=b)&(train<=S)]
    first=.5*(tr[:-1]+tr[1:])
    # Refine the entire HF suffix. Each first 0.14 physical chart chart
    # interval also receives its two distinct extra quarter locations.
    early=tr[:-1]<=b+.14
    pool=np.unique(np.r_[first,.75*tr[:-1][early]+.25*tr[1:][early],
        .25*tr[:-1][early]+.75*tr[1:][early]])
    recorded=set(map(float,train))|ind
    fresh=sorted(float(x) for x in pool if x not in recorded)
    return tr,np.asarray(fresh)


def main(args):
    start=time.monotonic()
    p=json.loads(args.prepared.read_text());o=json.loads(args.observer.read_text())
    g=json.loads(args.diagonal.read_text())["definition"]
    b,S=g["basis"]["physicalDomain"]
    tr,fresh=nodes(p,o,b,S)
    supplier=load(args.scripts/"6a65-geometry-nonfold-fixed-metric-value.py","actual_new_nodes_radius")
    target=supplier.FrozenWindowMetric(args.scripts,args.candidate,args.window_target,args.ramp,args.coast)
    samples=[]
    try:
        expected=np.load(p["caches"]["training"]["files"]["radius"],mmap_mode="r")
        orig=np.asarray(p["caches"]["training"]["nodes"])
        check=tr[np.unique(np.linspace(0,len(tr)-1,9,dtype=int))]
        mismatch=max(float(np.max(abs(expected[np.searchsorted(orig,x)]-target.radius(x)))) for x in check)
        if mismatch>5e-8:raise ValueError(("Fresh radius provider differs from actual stored physical jets",mismatch))
        for i,x in enumerate(fresh):
            samples.append(target.radius(x))
            if i%48==0:print(json.dumps(dict(index=i,total=len(fresh),seconds=time.monotonic()-start)),flush=True)
    finally:
        exit_receipt=target.close()
    m=dict(schema="fresh-physical-oracle-radius-jets-G10-suffix-mid-and-front-quarter-v1",
        entry=sha(__file__),supplier=sha(supplier.__file__),prepared=sha(args.prepared),observer=sha(args.observer),
        diagonal=sha(args.diagonal),target=sha(args.window_target),ramp=sha(args.ramp),coast=sha(args.coast),
        candidate=sha(args.candidate),chartNodes=fresh.tolist(),baseRadiusJets=samples,
        allOriginalAndIndependentRadialsExcluded=True,originalNineRowMaxDifference=mismatch,
        oracleExit=exit_receipt,seconds=time.monotonic()-start)
    with args.output.open("x") as fp:json.dump(m,fp,separators=(",",":"),allow_nan=False);fp.write("\n")
    print(json.dumps(dict(output=sha(args.output),nodes=len(fresh),seconds=m["seconds"])),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    for n in ("scripts","prepared","observer","diagonal","ramp","coast","candidate","window-target","output"):
        ap.add_argument("--"+n,type=Path,required=True)
    main(ap.parse_args())
