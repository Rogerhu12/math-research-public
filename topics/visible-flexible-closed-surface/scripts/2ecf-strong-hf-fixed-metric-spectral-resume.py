#!/usr/bin/env python3
"""Resume the full joint spectral surface solve on unchanged material g and basis."""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key]="1"

import argparse
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


core=load(Path(__file__).with_name("2ecf-strong-hf-fixed-metric-full-spectral-position.py"),"joint_spectral_core")
original_prepare=core.full.prepare


def inherit(args):
    result=list(original_prepare(args))
    definition,basis,clock,physical,g11,weights,mods,radius,meta,expect=result
    previous=json.loads(args.warm.read_text())
    old=previous["model"]
    if (old["actualMetric"]!=meta["actualMetric"] or old["warp"]!=meta["warp"]
        or old["entry"]!=core.c.sha(core.__file__) or old["sourceEvaluator"]!=core.c.sha(core.full.__file__)
        or old["physicalBasis"]!=meta["physicalBasis"] or previous["modelSHA256"]!=core.c.stable(old)):
        raise ValueError("Exact previous spectral basis, g, source and coefficient carrier required")
    z=np.asarray(previous.get("totalCoefficients",previous["coefficients"])).reshape(basis.nb,basis.na)
    direct=core.load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","spectral_resume_G11").direct_packet
    for name,cache in list(physical.items())+[("independent",g11)]:
        for start in range(0,len(cache.nodes),24):
            s=slice(start,start+24);xx=cache.nodes[s]
            if name=="independent":d=direct(basis,xx,z,cache.u)
            else:d=basis.packet(basis.matrices(xx),z,len(cache.u))
            cache.jets[s]+=d
    last=previous["stages"][-1]
    result[-1]=(last["allG10"]["original"],last["independent"]["metric"])
    meta.update(resumeEntry=core.c.sha(__file__),sameFixedGParentState=core.c.sha(args.warm),
        totalBaseCoefficientCount=z.size,initialCarrierParentStage=last["stage"]+1)
    return result


def main(args):
    previous=json.loads(args.warm.read_text())
    coeff=np.asarray(previous.get("totalCoefficients",previous["coefficients"]))
    core.full.prepare=inherit
    save=core.c.save
    def store(path,data):
        inc=np.asarray(data["coefficients"])
        if len(inc)!=len(coeff):raise ValueError("Full coefficient count differs")
        data["coefficientsAreIncrementsFromParent"]=True
        data["totalCoefficients"]=(coeff+inc).tolist()
        return save(path,data)
    core.c.save=store
    core.main(args)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    core.hf.args_hf(ap)
    for name in ("diagonal","warp","prefix","warm"):ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--metric-scale",type=float,default=.080)
    ap.add_argument("--curvature-scale",type=float,default=19.)
    ap.add_argument("--original-weight",type=float,default=1.)
    ap.add_argument("--coordinate-scale",type=float,default=.035)
    ap.add_argument("--betas",nargs="+",type=float,default=[35.,80.,160.])
    ap.add_argument("--iterations",type=int,default=80)
    ap.add_argument("--ridge",type=float,default=1e-6)
    ap.add_argument("--block",type=int,default=54)
    main(ap.parse_args())
