#!/usr/bin/env python3
"""Merge actual H-node rays and solve a local true-column interpolation model.

All added map/J/parameter values come from the same saved geometry. The
surrogate F_delta=F_0+delta*d_p F_0 omits parameter Taylor terms, and its
conjugacy must subsequently be tested by fresh actual rays.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicHermiteSpline,CubicSpline

from fourfold_circle_conjugacy import (newton,evaluate,dense_checks,target_value,TWOPI)


def merge(base,nodes):
    if base["source_sha256"]!=nodes["source_sha256"] or nodes["status"]!="complete":
        raise ValueError("map and actual H-node geometry differ, or nodes incomplete")
    period=base["angular_period"]
    theta=np.concatenate([b["input_physical_angles"] for b in nodes["completed_blocks"]])
    y=np.concatenate([b["returned_physical_angles"] for b in nodes["completed_blocks"]])
    j=np.concatenate([b["angular_derivative"] for b in nodes["completed_blocks"]])
    p=np.concatenate([b["parameter_column_physical"] for b in nodes["completed_blocks"]])
    turns=np.floor(theta/period)
    theta,y=theta-turns*period,y-turns*period
    order=np.argsort(theta)
    tx,ty,tj,tp=[a[order] for a in (theta,y,j,p)]
    allx=np.r_[base["initial_angles"],tx]
    ally=np.r_[base["returned_angles"],ty]
    allj=np.r_[base["angular_derivative"],tj]
    order=np.argsort(allx)
    allx,ally,allj=[a[order] for a in (allx,ally,allj)]
    duplicate=np.diff(allx)<1e-12
    if np.any(duplicate):
        raise ValueError("duplicate actual ray angles need explicit comparison before merging")
    return dict(status="complete",kind="same_geometry_actual_primary_and_Hnode_map",
                source_sha256=base["source_sha256"],angular_period=period,
                target_root=base["target_root"],initial_angles=allx.tolist(),
                returned_angles=ally.tolist(),angular_derivative=allj.tolist(),
                parameter_angles=tx.tolist(),parameter_values=tp.tolist(),
                requested_rays=len(allx),new_actual_rays=len(tx),
                curve_direction_sha256=nodes["curve_direction_sha256"],
                limitations=["actual ODE samples, not an interpolation or roundoff certificate",
                             "original radial reflection approximation remains unpaid"])


class LocalJetFamily:
    def __init__(self,data):
        self.length=data["angular_period"];self.scale=TWOPI/self.length
        theta=np.r_[data["initial_angles"],self.length]
        value=np.r_[data["returned_angles"],data["returned_angles"][0]+self.length]
        slope=np.r_[data["angular_derivative"],data["angular_derivative"][0]]
        self.base=CubicHermiteSpline(theta,value,slope)
        ptheta=np.array(data["parameter_angles"])
        pvalue=np.array(data["parameter_values"])
        self.tangent=CubicSpline(np.r_[ptheta,ptheta[0]+self.length],
                                 np.r_[pvalue,pvalue[0]],bc_type="periodic",
                                 extrapolate="periodic")

    def map(self,parameter,x,derivative=0):
        winding=np.floor(np.asarray(x)/TWOPI)
        theta=(np.asarray(x)-winding*TWOPI)/self.scale
        value=self.base(theta,nu=derivative)+parameter*self.tangent(theta,nu=derivative)
        if derivative==0:return winding*TWOPI+self.scale*value
        return self.scale**(1-derivative)*value

    def column(self,x,derivative=0):
        theta=np.mod(x,TWOPI)/self.scale
        return self.scale**(1-derivative)*self.tangent(theta,nu=derivative)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-map",type=Path,required=True)
    parser.add_argument("--actual-Hnodes",type=Path,required=True)
    parser.add_argument("--initial-conjugacy",type=Path,required=True)
    parser.add_argument("--merged-map",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--target",choices=["D5","D8"],default="D5")
    parser.add_argument("--base-global-parameter",type=float,required=True)
    parser.add_argument("--sizes",type=int,nargs="+",default=[257,513])
    args=parser.parse_args()
    base=json.loads(args.base_map.read_text());nodes=json.loads(args.actual_Hnodes.read_text())
    data=merge(base,nodes)
    data.update(base_map_sha256=hashlib.sha256(args.base_map.read_bytes()).hexdigest(),
                actual_Hnodes_sha256=hashlib.sha256(args.actual_Hnodes.read_bytes()).hexdigest())
    args.merged_map.write_text(json.dumps(data,indent=2)+"\n")
    family=LocalJetFamily(data);rho=target_value(args.target)
    with np.load(args.initial_conjugacy,allow_pickle=False) as saved:h=saved["h_values"]
    parameter=0.;levels=[]
    for size in args.sizes:
        if len(h)!=size:h=evaluate(h,np.arange(size)*TWOPI/size)
        h,parameter,steps=newton(family,rho,h,parameter)
        x,hh,hp=dense_checks(h,16*size)
        error=family.map(parameter,x+hh)-x-TWOPI*rho-evaluate(h,x+TWOPI*rho)
        shifted_hp=1+evaluate(h,x+TWOPI*rho,1)
        column=family.column(x+hh)
        level=dict(size=size,local_parameter_step=float(parameter),
                   proposed_global_parameter=float(args.base_global_parameter+parameter),
                   sampled_residual_max=float(np.max(np.abs(error))),
                   sampled_Hprime_range=[float(hp.min()),float(hp.max())],
                   sampled_weighted_twist=float(np.mean(column/shifted_hp)),
                   sampled_twist_integrand_range=[float(np.min(column/shifted_hp)),
                                                  float(np.max(column/shifted_hp))],steps=steps)
        levels.append(level)
        print(json.dumps({key:value for key,value in level.items() if key!="steps"}),flush=True)
    metadata=dict(kind="floating_actual_same_source_tangent_model_conjugacy",
                  source_sha256=data["source_sha256"],
                  curve_direction_sha256=data["curve_direction_sha256"],
                  merged_map_sha256=hashlib.sha256(args.merged_map.read_bytes()).hexdigest(),
                  initial_conjugacy_sha256=hashlib.sha256(args.initial_conjugacy.read_bytes()).hexdigest(),
                  target=args.target,rotation_number=rho,angular_scale=family.scale,
                  base_global_parameter=args.base_global_parameter,
                  parameter=float(parameter),
                  proposed_global_parameter=float(args.base_global_parameter+parameter))
    np.savez_compressed(args.checkpoint,h_values=h,metadata=np.array(json.dumps(metadata)))
    report=dict(**metadata,levels=levels,
                checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                limitations=["interpolated actual map and first parameter column, not the actual nonlinear family",
                             "parameter Taylor terms are omitted by the surrogate and require actual verification",
                             "finite Fourier, real sampling and floating linear solves",
                             "original binary reflection defect remains unpaid",
                             "a new H requires its own dyadic norm certificate and fresh actual ODE residual"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")


if __name__=="__main__":
    main()
