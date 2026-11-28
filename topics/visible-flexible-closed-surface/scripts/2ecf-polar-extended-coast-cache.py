#!/usr/bin/env python3
"""Actual R137 coat prolongation, material six-jets for a prospective C2 suffix splice."""
import argparse
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


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    started=time.monotonic()
    spec_path=args.scripts/"6a65-geometry-cauchy-unit-t-warm.py"
    sys.path.insert(0,str(args.scripts.resolve()))
    spec=importlib.util.spec_from_file_location("extended_coast_supplier",spec_path)
    warm=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(warm)
    model=warm.WarmMaster(args.ramp,args.coast,coast_length=.02)
    if (sha(args.ramp)!="479dab51bd77a211f64a256bbb16d67b4382e150af0deee7fa6baf84d8e5464a"
        or sha(args.coast)!="f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d"):
        raise ValueError("Physical H65 ramp and actual shared Gamma95 required")
    saved=json.loads(args.source.read_text())
    if args.group=="independent":
        nodes=np.asarray(saved["physicalNodes"])
        u=np.asarray(saved["angles"])
    else:
        record=saved["caches"][args.group]
        nodes=np.asarray(record["nodes"])
        u=np.asarray(record["angles"])
    selected=np.flatnonzero((nodes>=model.coast_end)&(nodes<=model.coast_end+args.length))
    radials=nodes[selected]
    jets=np.zeros((len(radials),6,len(u),3))
    keys=("X","Xs","Xu","Xss","Xsu","Xuu")
    for j,s in enumerate(radials):
        port=model.coast_port(float(s-model.ramp_end),u)
        packet=warm.packet_from_port(port)
        jets[j]=np.stack([packet[k] for k in keys])
        if (j+1)%32==0:
            print("completed",j+1,len(radials),flush=True)
    path=Path(str(args.prefix)+"-extended-coast.npz")
    with path.open("xb") as stream:
        np.savez(stream,jets=jets,indices=selected,nodes=radials,angles=u)
    manifest=dict(schema="actual-H65-original-Gamma95-prolonged-coast-sixjet-cache-v1",
        numericalOnly=True,rampSHA256=sha(args.ramp),coastSHA256=sha(args.coast),
        warmSupplierSHA256=sha(spec_path),entrySHA256=sha(__file__),sourceSHA256=sha(args.source),
        group=args.group,radials=len(selected),angles=len(u),offsetEnd=args.length,
        maxAbsoluteZ=float(abs(jets[:,0,:,2]).max()),packetSHA256=sha(path),packet=str(path.resolve()),
        elapsed=time.monotonic()-started)
    with Path(str(args.prefix)+"-extended-coast.json").open("x") as stream:
        json.dump(manifest,stream,indent=2)
        stream.write("\n")
    print(json.dumps(manifest),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for name in ("scripts","ramp","coast","source","prefix"):
        parser.add_argument("--"+name,required=True,type=Path)
    parser.add_argument("--length",required=True,type=float)
    parser.add_argument("--group",choices=("training","observer","independent"),required=True)
    run(parser.parse_args())
