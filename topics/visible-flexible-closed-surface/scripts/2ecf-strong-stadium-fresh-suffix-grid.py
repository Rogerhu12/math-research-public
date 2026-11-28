#!/usr/bin/env python3
"""Evaluate genuinely new intrinsic radial rings and angular samples of the actual stadium suffix."""
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);o=importlib.util.module_from_spec(sp);sys.modules[n]=o;sp.loader.exec_module(o);return o


here=Path(__file__).parent;src=load(here/"2ecf-strong-stadium-arbitrary-physical-suffix.py","p32_fresh_true_suffix");c=src.c


def evaluate(field,args,return_arrays=False):
    start=time.monotonic();old=field.cutraw.breaks;z=(np.arange(args.subdivisions)+args.offset)/args.subdivisions
    x=np.sort((old[:-1,None]+np.diff(old)[:,None]*z).ravel())
    u=2*np.pi*(np.arange(args.new_angles)+args.angular_offset)/args.new_angles
    if not (0<args.offset<1 and 0<=args.angular_offset<1):raise ValueError("Real interior subcell samples required")
    grids=[np.array(o["nodes"]) for o in field.saved["caches"].values()];g11=np.asarray(src.rd(args.observer)["physicalNodes"])
    d10=min(float(np.min(abs(x[:,None]-g[None,:]))) for g in grids);d11=float(np.min(abs(x[:,None]-g11[None,:])))
    # Count actual distinct radial labels, with a small buffer for near-identical arithmetic variants.
    new10=np.ones(len(x),dtype=bool)
    for g in grids:new10&=np.min(abs(x[:,None]-g[None,:]),axis=1)>1e-13
    new11=np.min(abs(x[:,None]-g11[None,:]),axis=1)>1e-13
    cfg=field.stream.point.PointConfig(**field.definition["pointConfig"]);st=None
    allp=np.zeros((len(x),6,len(u),3)) if return_arrays else None
    ar=np.zeros((len(x),3)) if return_arrays else None
    for j in range(0,len(x),8):
        sl=slice(j,j+8);xx=x[sl];X,rad=field.jets(xx,u)
        pt=field.stream.point.PointLinearized(X.swapaxes(1,2),rad[:,0,None],cfg,{name:np.ones((len(xx),1))/len(u) for name in ("geometry","curvature","metric")})
        ss=field.stream._block_statistics(pt,xx,len(u))
        for key in ("worstMetric","worstCurvature"):ss[key]["u"]+=u[0]
        st=field.stream._merge_statistics(st,ss)
        if return_arrays:allp[sl]=X;ar[sl]=rad
    st=src.joint.full.lm.labels(st,field.dclock)
    out=dict(schema="genuinely-new-ring-actual-physical-broad-stadium-suffix-v1",entry=c.sha(__file__),evaluator=c.sha(src.__file__),metric=field.ident,
        source=c.sha(args.background),additionalPhysicalCoefficients=[c.sha(f) for f in args.extra_state],numberRadii=len(x),numberAngles=len(u),
        numberGenuinelyNewG10Radii=int(new10.sum()),numberGenuinelyNewG11Radii=int(new11.sum()),nearestG10RadiusDistance=d10,
        nearestG11RadiusDistance=d11,fullRadii=x.tolist(),angleOffset=args.angular_offset,subdivisions=args.subdivisions,withinSubcell=args.offset,
        peakMetric=st["maxRelativeMetric"],peakCurvature=st["maxCurvature"],minHeld=st["minHeldDistance"],guide=st["geometryMaximumViolations"],
        worstMetric=st["worstMetric"],worstCurvature=st["worstCurvature"],restrictedToEntireMovableSuffix=True,seconds=time.monotonic()-start)
    c.save(Path(str(args.prefix)+"-fresh-grid.json"),out)
    print(json.dumps({k:out[k] for k in ("numberRadii","numberAngles","numberGenuinelyNewG10Radii","numberGenuinelyNewG11Radii","peakMetric","peakCurvature","minHeld","worstMetric","worstCurvature")}),flush=True)
    if return_arrays:return out,SimpleNamespace(jets=allp,radius=ar,nodes=x,u=u)
    return out


if __name__=="__main__":
    parser=src.parser()
    parser.add_argument("--new-angles",type=int,default=320);parser.add_argument("--subdivisions",type=int,default=4)
    parser.add_argument("--offset",type=float,default=.271);parser.add_argument("--angular-offset",type=float,default=0.)
    args=parser.parse_args();args.resume=None
    evaluate(src.Field(args),args)
