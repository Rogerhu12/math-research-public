#!/usr/bin/env python3
"""Fresh staggered principal-ray checks of an explicitly defined dyadic H.

The node phase is independent of the earlier conjugacy collocation grid.
Actual rays/J are recomputed from the named saved geometry. Uniform analytic
residual bounds, interval ODE errors, and the reflection defect remain unpaid.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_circle_conjugacy import target_value
from fourfold_phase_conjugacy_nodes import evaluate_polynomial
from fourfold_phase_geometry import load_phase
from fourfold_phase_principal_map import PrincipalMap


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--dyadic-conjugacy",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--branch-checkpoint",type=Path,required=True)
    parser.add_argument("--progress",type=Path)
    parser.add_argument("--target",choices=["D5","D8"],default="D5")
    parser.add_argument("--rays",type=int,default=64)
    parser.add_argument("--offset",type=float,default=.5)
    parser.add_argument("--block-size",type=int,default=32)
    parser.add_argument("--tolerance",type=float,default=2e-9)
    parser.add_argument("--resume",action="store_true")
    args=parser.parse_args()
    if not 0<=args.offset<1:raise ValueError("offset must be in [0,1)")
    source_sha=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    polynomial_sha=hashlib.sha256(args.dyadic_conjugacy.read_bytes()).hexdigest()
    definitions=json.loads(args.dyadic_conjugacy.read_text())
    geometry,solver,_,_=load_phase(args.checkpoint)
    mapper=PrincipalMap(geometry,solver,[.235,.24],source_sha256=source_sha,
                        branch_checkpoint=args.branch_checkpoint,progress_file=args.progress)
    rho=target_value(args.target);alpha=2*np.pi*rho
    x=(np.arange(args.rays)+args.offset)*2*np.pi/args.rays
    H=x+evaluate_polynomial(definitions,x)
    Hp=1+evaluate_polynomial(definitions,x,1)
    HR=x+alpha+evaluate_polynomial(definitions,x+alpha)
    HpR=1+evaluate_polynomial(definitions,x+alpha,1)
    common=dict(source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                dyadic_conjugacy=args.dyadic_conjugacy.name,dyadic_conjugacy_sha256=polynomial_sha,
                target=args.target,target_rotation=rho,target_root=mapper.root,
                rays=args.rays,node_offset=args.offset,ode_rtol=args.tolerance,
                angular_scale=4.)
    blocks=[]
    if args.resume and args.out.exists():
        previous=json.loads(args.out.read_text())
        for key in ("source_sha256","dyadic_conjugacy_sha256","rays","node_offset","ode_rtol"):
            if previous[key]!=common[key]:raise ValueError("resume object or grid changed: "+key)
        if previous["status"]=="complete":
            print(json.dumps({"progress":"matching completed staggered rays already saved"}),flush=True);return
        blocks=previous["completed_blocks"];mapper.calls=previous["current_rhs_calls"]
        if blocks:
            mapper.maximum_N=max(b["maximum_N"] for b in blocks)
            mapper.minimum_qbar=min(b["minimum_qbar"] for b in blocks)
    for first in range(sum(len(b["x"]) for b in blocks),args.rays,args.block_size):
        sl=slice(first,first+args.block_size)
        returned,jac=mapper.round_trip(H[sl]/4,args.tolerance)
        blocks.append(dict(x=x[sl].tolist(),input_physical_angles=(H[sl]/4).tolist(),
                           returned_physical_angles=returned.tolist(),angular_derivative=jac.tolist(),
                           maximum_N=mapper.maximum_N,minimum_qbar=mapper.minimum_qbar))
        partial=dict(**common,status="partial",completed_blocks=blocks,current_rhs_calls=mapper.calls)
        args.out.write_text(json.dumps(partial,indent=2)+"\n")
        print(json.dumps({"progress":"fresh staggered H-node block saved","completed_rays":first+len(returned)}),flush=True)
    returned=np.concatenate([b["returned_physical_angles"] for b in blocks])
    jac=np.concatenate([b["angular_derivative"] for b in blocks])
    error=4*returned-HR;errorprime=jac*Hp-HpR
    report=dict(**common,status="complete",kind="floating_staggered_actual_conjugacy_ray_validation",
                completed_blocks=blocks,rhs_calls=mapper.calls,
                conjugacy_error=error.tolist(),conjugacy_error_derivative=errorprime.tolist(),
                sampled_error_max=float(np.max(np.abs(error))),
                sampled_error_derivative_max=float(np.max(np.abs(errorprime))),
                sampled_weighted_error_mean=float(np.mean(error/HpR)),
                maximum_sampled_N=mapper.maximum_N,minimum_radial_qbar=mapper.minimum_qbar,
                limitations=["fresh actual ray nodes but no interval ODE or analytic interpolation certificate",
                             "dyadic H is defined exactly, but its node evaluation here uses floating exp",
                             "original binary radial reflection approximation remains unpaid",
                             "no true parameter correction, full PDE inverse or closed flex proved"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","sampled_error_max",
                      "sampled_error_derivative_max","sampled_weighted_error_mean")}),flush=True)


if __name__=="__main__":
    main()
