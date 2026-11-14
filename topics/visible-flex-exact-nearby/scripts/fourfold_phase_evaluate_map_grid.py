#!/usr/bin/env python3
"""Evaluate a new immutable phase geometry on an explicitly saved angle grid.

Only initial_angles are borrowed from the grid file. No map values, target
metric, roots, or parameter columns are transferred between geometries.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_geometry import load_phase
from fourfold_phase_principal_map import PrincipalMap


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint",type=Path,required=True)
    p.add_argument("--angle-grid",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--progress",type=Path)
    p.add_argument("--branch-checkpoint",type=Path)
    p.add_argument("--turn-bracket",type=float,nargs=2,default=[.235,.24])
    p.add_argument("--block-size",type=int,default=8)
    p.add_argument("--tolerance",type=float,default=2e-7)
    p.add_argument("--resume",action="store_true")
    args=p.parse_args()
    source_sha=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    grid_sha=hashlib.sha256(args.angle_grid.read_bytes()).hexdigest()
    grid=json.loads(args.angle_grid.read_text())
    angles=np.array(grid["initial_angles"])
    if angles[0] != 0 or np.any(np.diff(angles)<=0):
        raise ValueError("need a complete ordered periodic grid")
    geometry,solver,_,_=load_phase(args.checkpoint)
    mapper=PrincipalMap(geometry,solver,args.turn_bracket,progress_file=args.progress,
                        branch_checkpoint=args.branch_checkpoint or args.out.with_suffix(".branch.npz"),
                        source_sha256=source_sha)
    blocks=[]
    if args.resume and args.out.exists():
        previous=json.loads(args.out.read_text())
        if (previous["source_sha256"]!=source_sha or previous["angle_grid_sha256"]!=grid_sha
                or previous["ode_rtol"]!=args.tolerance):
            raise ValueError("resume input or grid changed")
        if previous["status"]=="complete":
            print(json.dumps({"progress":"matching complete map already saved"}),flush=True)
            return
        blocks=previous["completed_blocks"]
        mapper.calls=previous["current_rhs_calls"]
        if blocks:
            mapper.maximum_N=max(block["maximum_N"] for block in blocks)
            mapper.minimum_qbar=min(block["minimum_qbar"] for block in blocks)
    for first in range(sum(len(block["initial_angles"]) for block in blocks),
                       len(angles),args.block_size):
        theta=angles[first:first+args.block_size]
        returned,jac=mapper.round_trip(theta,args.tolerance)
        blocks.append(dict(initial_angles=theta.tolist(),returned_angles=returned.tolist(),
                           angular_derivative=jac.tolist(),maximum_N=mapper.maximum_N,
                           minimum_qbar=mapper.minimum_qbar))
        partial=dict(status="partial",source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                     angle_grid=args.angle_grid.name,angle_grid_sha256=grid_sha,
                     target_root=mapper.root,ode_rtol=args.tolerance,
                     completed_blocks=blocks,current_rhs_calls=mapper.calls)
        args.out.write_text(json.dumps(partial,indent=2)+"\n")
        print(json.dumps({"progress":"new-geometry map block saved",
                          "completed_rays":first+len(theta)}),flush=True)
    returned=np.concatenate([block["returned_angles"] for block in blocks])
    jac=np.concatenate([block["angular_derivative"] for block in blocks])
    result=dict(status="complete",kind="floating_R37_new_geometry_on_saved_angle_grid",
                source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                angle_grid=args.angle_grid.name,angle_grid_sha256=grid_sha,
                target_root=mapper.root,angular_period=float(np.pi/2),
                requested_rays=len(angles),grid_kind="borrowed angles only; new geometry evaluated",
                initial_angles=angles.tolist(),returned_angles=returned.tolist(),
                angular_derivative=jac.tolist(),completed_blocks=blocks,
                ode_rtol=args.tolerance,rhs_calls=mapper.calls,
                displacement_range=[float(min(returned-angles)),float(max(returned-angles))],
                angular_derivative_range=[float(min(jac)),float(max(jac))],
                maximum_sampled_N_on_rays=mapper.maximum_N,minimum_radial_qbar=mapper.minimum_qbar,
                raw_modified_discriminant="Delta_hat=(-K0)*G_actual^2",
                limitations=["ordinary floating ODE and finite angle samples",
                             "tiny binary radial reflection defect ignored and unpaid; not an exact original-input operator map",
                             "principal graph only, not full PDE scattering",
                             "borrowed only initial angles, no old metric/root/map/column input",
                             "no exact closed flex or reach certificate"])
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in
                     ("status","target_root","displacement_range","angular_derivative_range",
                      "maximum_sampled_N_on_rays")}),flush=True)


if __name__=="__main__":
    main()
