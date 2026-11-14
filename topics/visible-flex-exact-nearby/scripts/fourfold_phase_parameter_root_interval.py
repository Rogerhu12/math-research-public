#!/usr/bin/env python3
"""A common simple-root collar for the exact affine real R57 family.

Unlike the larger independent control box used for N, radial derivatives
retain the affine parameter correlation: S0^(j)+delta*V^(j). The resulting
root certificate therefore concerns the exact affine family only.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import floor_float,ceiling_float
from fourfold_phase_core_N_interval import CoreNGate,ClosedSpanSplineBox
from fourfold_phase_root_interval import Box


class AffineClosedSpline:
    def __init__(self,base,direction,parameter):
        self.base,self.direction,self.parameter=base,direction,parameter

    def jets(self,x,order=3):
        return self.base.jets(x,order)+self.parameter*self.direction.jets(x,order)


def make_affine_target(frozen,direction,parameter_interval,nodes=256):
    target=CoreNGate(frozen,nodes,4096).target
    delta=Box(*parameter_interval)
    variation=ClosedSpanSplineBox(frozen["phase_knots"],direction["phase_direction_coefficients"],5)
    target.phase=AffineClosedSpline(target.phase,variation,delta)
    target.alpha=[Box(a)+delta*d for a,d in zip(frozen["alpha"],direction["alpha_direction"])]
    return target


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs",type=Path,required=True)
    parser.add_argument("--frozen-direction",type=Path,required=True)
    parser.add_argument("--parameter-radius",type=float,default=.01)
    parser.add_argument("--left",type=float,default=.238394)
    parser.add_argument("--right",type=float,default=.2384)
    parser.add_argument("--collar-center",default="238397/1000000")
    parser.add_argument("--collar-radius",default="1/4096")
    parser.add_argument("--quarter-nodes",type=int,default=256)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    with np.load(args.inputs,allow_pickle=False) as z:frozen={k:z[k].copy() for k in z.files}
    with np.load(args.frozen_direction,allow_pickle=False) as z:direction={k:z[k].copy() for k in z.files}
    metadata=json.loads(str(direction["metadata"]))
    if metadata["origin_inputs_sha256"]!=digest(args.inputs):raise ValueError("direction belongs to another origin")
    parameter=[-args.parameter_radius,args.parameter_radius]
    target=make_affine_target(frozen,direction,parameter,args.quarter_nodes)
    center,radius=Fraction(args.collar_center),Fraction(args.collar_radius)
    exact_collar=[center-radius,center+radius]
    collar=[floor_float(exact_collar[0]),ceiling_float(exact_collar[1])]
    if not exact_collar[0]<Fraction(args.left)<Fraction(args.right)<exact_collar[1]:
        raise ValueError("root bracket must be strictly inside exact collar")
    values=[target.evaluate(Box(args.left)),target.evaluate(Box(args.right)),target.evaluate(Box(*collar))]
    left,right,whole=values
    conditions=dict(left_C_negative=left["C"][1]<0,right_C_positive=right["C"][0]>0,
                    collar_a_positive=whole["a"][0]>0,collar_E_positive=whole["E"][0]>0,
                    collar_Kprime_positive=whole["Kprime"][0]>0)
    proved=all(conditions.values())
    result=dict(kind="directed_common_simple_root_for_exact_real_affine_R57_family",
                proved=proved,origin_inputs_sha256=digest(args.inputs),frozen_direction_sha256=digest(args.frozen_direction),
                exact_parameter_interval=parameter,quarter_nodes=args.quarter_nodes,
                root_bracket=[args.left,args.right],exact_collar=[str(v) for v in exact_collar],
                outward_binary_collar=collar,conditions=conditions,rows=values,
                run_source_sha256=digest(Path(__file__)),
                root_engine_sha256=digest(Path(__file__).with_name("fourfold_phase_root_interval.py")),
                closed_span_engine_sha256=digest(Path(__file__).with_name("fourfold_phase_core_N_interval.py")),
                family=metadata["family"],
                derivative_semantics="phase derivatives are enclosed as S0^(j)+delta*V^(j), retaining one shared real parameter before interval evaluation",
                conclusion="for every parameter a unique positive root lies in the bracket, is simple, and is unique throughout the collar; explicit symmetry supplies its negative partner",
                limitations=["applies to the exact affine family, not every point in the larger independent control box",
                             "does not identify rounded checkpoint controls with an exact affine-family point",
                             "no full-core curvature-sign classification or complex-domain ray bound"])
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("proved","root_bracket","outward_binary_collar","conditions")}),flush=True)
    print(json.dumps(whole),flush=True)
    if not proved:raise SystemExit("common parameter root certificate did not pass")


if __name__=="__main__":main()
