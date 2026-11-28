#!/usr/bin/env python3
"""True complete 14-row Gauss–Newton correction of the actual longer-stadium field."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod


here=Path(__file__).parent
source=load(here/"2ecf-strong-stadium-longer-proven-coast.py","stadium_full_normal_source")
joint=source.joint
full=joint.full
c=source.c


def prepare(args):
    # Reconstruct all background shapes at the recorded source-selection scales.
    oms,oks=args.metric_scale,args.curvature_scale
    args.metric_scale,args.curvature_scale=.10,12.
    try:
        definition,big,clock,phys,g11,w,mods,radius,meta,_=source.prepare(args)
    finally:
        args.metric_scale,args.curvature_scale=oms,oks
    bg=json.loads(args.background.read_text())
    if (bg["model"]["physicalBasis"]!=big.definition or bg["model"]["actualMetric"]!=meta["actualMetric"]
            or bg["model"]["trueBlendLength"]!=meta["trueBlendLength"]):
        raise ValueError("Physical p32 parent and true positive frozen target required")
    z=np.asarray(bg["coefficients"]).reshape(big.nb,big.na)
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","stadium_normal_shift").direct_packet
    for name,obj in list(phys.items())+[("independent",g11)]:
        for k in range(0,len(obj.nodes),12):
            sl=slice(k,k+12);x=obj.nodes[sl]
            obj.jets[sl]+=direct(big,x,z,obj.u) if name=="independent" else big.packet(big.matrices(x),z,len(obj.u))
    physical={n:radius.ArrayCache(o.nodes,o.u,o.jets,o.radius) for n,o in phys.items()}
    basis=copy.copy(big);basis.M=args.correction_frequency
    basis.channels=[q for q in big.channels if q[1]<=basis.M]
    basis.modes=np.array([q[1] for q in basis.channels]);basis.na=len(basis.channels)
    basis.dimension=basis.na*basis.nb
    basis.definition=dict(schema="same-physical-clamped-radials-complete-low-angular-Cartesian-correction-v1",
        backgroundBasis=big.definition,backgroundReceipt=c.sha(args.background),channels=basis.channels,
        correctionFrequency=basis.M,dimension=basis.dimension,allUnmodifiedHigherPositionModesInPhysicalSource=True)
    meta.update(schema="true-p32-longer-full-stadium-14-row-sparse-normal-v1",normalDriver=c.sha(__file__),
        physicalBasis=basis.definition,freeXYZ=basis.dimension,physicalBackground=c.sha(args.background),
        retainedOriginalRows=4291840,normalizedFullCartesianCrosses=True,independentG11NeverInTraining=True,
        curvatureTau=args.curvature_tau,metricSextic=args.metric_sextic)
    definition=copy.deepcopy(definition);definition["recipe"]["radialBlock"]=4
    expected=(bg["stages"][-1]["allG10"]["original"],bg["stages"][-1]["independent"]["metric"])
    return definition,basis,clock,physical,g11,w,mods,radius,meta,expected


if __name__=="__main__":
    ap=joint.slope.args_base()
    for name in ("fixed-stadium","prior-guide","projected","redesigned-state","background"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--guide-scale",type=float,default=.0025);ap.add_argument("--directions",type=int,default=20)
    ap.add_argument("--divisions",type=int,default=9);ap.add_argument("--box",type=float,default=.25)
    ap.add_argument("--first",type=float,default=3.);ap.add_argument("--second",type=float,default=65.)
    ap.add_argument("--extension",type=float,default=.04);ap.add_argument("--add-length",type=float,default=.014)
    ap.add_argument("--radius-blend",type=float,default=.18);ap.add_argument("--blends",type=float,nargs="+",default=[.06,.095,.14,.19,.25,.33,.42])
    ap.add_argument("--correction-frequency",type=int,default=12);ap.add_argument("--steps",type=int,default=3)
    ap.add_argument("--damping",type=float,default=.035);ap.add_argument("--curvature-tau",type=float,default=2.)
    ap.add_argument("--metric-sextic",type=float,default=.2);ap.add_argument("--state",type=Path)
    args=ap.parse_args();args.resume=None
    if not 1<=args.correction_frequency<=32:raise ValueError("Declared proper half-turn angular space required")
    full.prepare=prepare
    full.main(args)
