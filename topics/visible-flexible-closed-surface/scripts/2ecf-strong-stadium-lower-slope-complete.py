#!/usr/bin/env python3
"""Lower true ramp slope, carry a physical Cartesian field, and solve on a fresh stadium metric."""
import argparse
from fractions import Fraction as Q
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


here=Path(__file__).parent
base=load(here/"2ecf-strong-stadium-complete-field.py","stadium_full_base")
orig=base.stream_carrier
original_prefix=base.Prefix
base.shapes=load(here/"2ecf-strong-stadium-support-variable-H65.py","new_stadium_slope")
c=base.c


class MatchedPrefix(original_prefix):
    def rows(self,x,u):
        jets,rad=super().rows(x,u)
        m=self.master
        q=Q.from_float
        error=float(q(m.curve.a)-(1+q(m.v)*q(m.ramp)/2))
        inside=(x>m.c)&(x<m.ramp_end)
        t=(x[inside]-m.c)/m.ramp
        w,wp,wpp=base.step(t)
        rad[inside]+=error*np.column_stack((w,wp/m.ramp,wpp/m.ramp**2))
        return jets,rad


def physical_carrier(args):
    definition,basis,clock,allsets,g11,weights,mods,radius,meta=orig(args)
    st=json.loads(args.stadium_carrier.read_text())
    ref=st["model"]
    if (ref["stadiumEvaluator"]!=c.sha(base.__file__) or ref["physicalBasis"]["sourceChartBasis"]!=basis.definition["sourceChartBasis"]
            or ref["additionalLength"]!=args.extra or ref["originalHFCarrier"]["literalParent"]!=meta["literalParent"]
            or ref["actualPriorNewStadiumStage"] is not None):
        raise ValueError("Real first-generation stadium Cartesian correction at the same material clock required")
    z=np.asarray(st["coefficients"]).reshape(basis.nb,basis.na)
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","lower_slope_shift").direct_packet
    for name,obj in list(allsets.items())+[("independent",g11)]:
        for k in range(0,len(obj.nodes),12):
            sl=slice(k,k+12);x=obj.nodes[sl]
            # B is in the old physical variable here. The calling field applies the new physical clock once.
            obj.jets[sl]+=direct(basis,x,z,obj.u) if name=="independent" else basis.packet(basis.matrices(x),z,len(obj.u))
    meta=dict(meta,priorStadiumPositionOnly=c.sha(args.stadium_carrier),priorStadiumMetric=ref["stadiumTarget"],
        oldSpatialBasisExactlyChartFunctions=True,oldPositionIsFixedBackground=True)
    return definition,basis,clock,allsets,g11,weights,mods,radius,meta


def prepare(args):
    base.Prefix=MatchedPrefix
    base.stream_carrier=physical_carrier
    results=base.field(args)
    definition,basis,clock,phys,g11,w,mods,radius,meta,expected=results
    report=json.loads(Path(str(args.prefix)+"-source.json").read_text())
    src=report["newG"]
    # The named smooth target defines its joins via endpoint jets. Displayed binary Bernstein
    # controls are evaluation approximations, not a second exact polynomial definition.
    exact=dict(schema="stadium-matched-ramp-metric-and-two-end-Hermite-positive-angular-v1",
        evaluationTarget=report["newGSHA"],entry=c.sha(__file__),newRuling=src["coast"],
        newNative=src["ramp"],oldAdditionalPosition=c.sha(args.stadium_carrier),
        fullNewEquation="central radius 1; original radius + (stored F0-(1+v*r/2))*H5(t) on ramp; F0+v*sigma on corrected coast; Hermite or degree-five Bernstein interpolation from (F0+v*ell,v,0) to (.8,-1,0) times exp(B alpha); then .8-(s-cut)",
        positiveAngularMultiplier=src["logExpCoefficientsHex"],clockFormula=src["chart"],ell=src["sewnAtChart"],
        homogeneousUpperEndExtrapolation=True,allDisplayedFloatControlsAreApproximations=True,
        fixedSForThisOptimization=True,retainedOriginalPositionsAsShapeNotMetric=True)
    digest=c.stable(exact)
    meta.update(stadiumEvaluatorV2=c.sha(__file__),actualMetric=digest,matchedMetric=exact,
        stadiumMatchedTarget=digest,newIndependentOwnPositionIterations=0)
    c.save(Path(str(args.prefix)+"-target.json"),dict(exact=exact,SHA256=digest))
    return definition,basis,clock,phys,g11,w,mods,radius,meta,expected


def args_base():
    ap=argparse.ArgumentParser()
    base.hf.args_hf(ap)
    for k in ("diagonal","warp","warm","refined-state","stadium","stadium-ramp","stadium-coast","prefix","stadium-carrier"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--frequency",type=int,default=32)
    ap.add_argument("--extra",type=float,default=.018)
    ap.add_argument("--fit-length",type=float,default=.42)
    ap.add_argument("--fit-smoothing",type=float,default=.00004)
    ap.add_argument("--lengths",type=float,nargs="+",default=[.32,.42,.52,.62,.72,.80])
    ap.add_argument("--metric-scale",type=float,default=.105)
    ap.add_argument("--curvature-scale",type=float,default=13.)
    ap.add_argument("--original-weight",type=float,default=1.)
    ap.add_argument("--coordinate-scale",type=float,default=.035)
    ap.add_argument("--betas",nargs="+",type=float,default=[24.,60.,115.])
    ap.add_argument("--iterations",type=int,default=80)
    ap.add_argument("--ridge",type=float,default=1e-6)
    ap.add_argument("--block",type=int,default=34)
    ap.add_argument("--source-only",action="store_true")
    return ap


if __name__=="__main__":
    args=args_base().parse_args()
    args.resume=None
    if args.source_only:prepare(args)
    else:
        base.core.full.prepare=prepare
        base.core.main(args)
