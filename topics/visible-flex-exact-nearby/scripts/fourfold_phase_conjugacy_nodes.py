#!/usr/bin/env python3
"""Actual principal rays at a defined dyadic H, with the true curve derivative.

All estimates below remain floating ray diagnostics, including the unpaid
radial reflection approximation. Unlike an interpolation-only conjugacy,
R(H), R'(H), and the moving-root parameter column are integrated anew here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from fourfold_circle_conjugacy import target_value
from fourfold_phase_geometry import (load_phase,PhaseGeometry,reflected_spline,
                                    phase_jets,tangent_variation_jets)
from fourfold_phase_principal_parameter_map import ParameterMap


class CurveGeometry(PhaseGeometry):
    """One actual vector direction, leaving the frozen three-mean adapter intact."""
    def __init__(self,solver,vector,nodes,direction):
        super().__init__(solver,vector,nodes)
        self.directions=np.asarray(direction)[None,:]
        coeff,mean=solver.unpack(direction)
        self.curve_spline=reflected_spline(solver,coeff)
        self.curve_mean=mean

    def variation_radial_coefficients(self,x):
        data=self.radial_coefficients(x)
        if "variation_radial" in data:
            return data["variation_radial"]
        unique=np.atleast_1d(x)
        z,mean,aux=data["primitive"],data["mean"],data["auxiliary"]
        dm=np.stack([sum((coefficient*sp(unique,nu=j) for coefficient,sp in
                         zip(self.curve_mean,self.solver.mean_splines)),
                        np.zeros((len(unique),3))) for j in range(3)])
        dphase=phase_jets(self.solver,self.curve_spline,unique,order=2)
        dz=self.primitive_coefficients(tangent_variation_jets(aux,dphase,self.sine))
        radial=[]
        for j in range(3):
            coefficient=sum(math.comb(j,k)*(
                dm[k,:,0,None,None]*z[j-k]+mean[k,:,0,None,None]*dz[j-k])
                for k in range(j+1))
            coefficient[:,0,2]+=dm[j,:,2]
            radial.append(coefficient)
        result=[dict(radial=radial,mean=dm)]
        data["variation_radial"]=result
        return result


def evaluate_polynomial(definitions,x,derivative=0):
    degree=definitions["H_degree"]
    denominator=1<<definitions["denominator_power_of_two"]
    pos=np.array([complex(int(a),int(b))/denominator
                  for a,b in definitions["h_nonnegative_integer_coefficients"]])
    coeff=np.r_[np.conj(pos[:0:-1]),pos]
    k=np.arange(-degree,degree+1)
    return np.real(np.exp(1j*np.outer(np.asarray(x),k))
                   @ (coeff*(1j*k)**derivative))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--directions",type=Path,required=True)
    parser.add_argument("--parameter-map",type=Path,required=True)
    parser.add_argument("--dyadic-conjugacy",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--branch-checkpoint",type=Path,required=True)
    parser.add_argument("--progress",type=Path)
    parser.add_argument("--target",choices=["D5","D8"],default="D5")
    parser.add_argument("--rays",type=int,default=64)
    parser.add_argument("--block-size",type=int,default=8)
    parser.add_argument("--tolerance",type=float,default=2e-8)
    parser.add_argument("--curve-eigen-increment",type=float,nargs=3,default=[.002,.0002,0.])
    parser.add_argument("--turn-bracket",type=float,nargs=2,default=[.235,.24])
    parser.add_argument("--resume",action="store_true")
    args=parser.parse_args()
    source_sha=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    directions_sha=hashlib.sha256(args.directions.read_bytes()).hexdigest()
    polynomial_sha=hashlib.sha256(args.dyadic_conjugacy.read_bytes()).hexdigest()
    param=json.loads(args.parameter_map.read_text())
    if param["direction_sha256"]!=directions_sha:
        raise ValueError("Schur directions changed")
    with np.load(args.directions,allow_pickle=False) as saved:
        unit=saved["directions"].copy()
    basis=np.array(param["eigenbasis_columns"])
    eta=np.array(args.curve_eigen_increment)
    direction=(basis@eta)@unit
    curve_sha=hashlib.sha256(direction.tobytes()).hexdigest()
    original,solver,vector,metadata=load_phase(args.checkpoint)
    geometry=CurveGeometry(solver,vector,original.nodes,direction)
    padded=PhaseGeometry(solver,vector,original.nodes,
                         np.stack([direction,np.zeros_like(direction),np.zeros_like(direction)]))
    check_x=np.array([0.,.17,.238]);check_theta=np.array([.13,.29,.71])
    adapter_error=max(float(np.max(np.abs(a-b))) for a,b in zip(
        geometry.variation_jets(check_x,check_theta)[0],
        padded.variation_jets(check_x,check_theta)[0]))
    if adapter_error!=0.:
        raise ValueError("single-direction adapter disagrees with the frozen three-column evaluator")
    mapper=ParameterMap(geometry,solver,args.turn_bracket,
                        direction_sha256=curve_sha,source_sha256=source_sha,
                        branch_checkpoint=args.branch_checkpoint,
                        progress_file=args.progress)
    definitions=json.loads(args.dyadic_conjugacy.read_text())
    rho=target_value(args.target);alpha=2*np.pi*rho;scale=4.
    x=np.arange(args.rays)*2*np.pi/args.rays
    H=x+evaluate_polynomial(definitions,x)
    shifted_H=x+alpha+evaluate_polynomial(definitions,x+alpha)
    Hp=1+evaluate_polynomial(definitions,x,1)
    shifted_Hp=1+evaluate_polynomial(definitions,x+alpha,1)
    blocks=[]
    if args.resume and args.out.exists():
        previous=json.loads(args.out.read_text())
        if (previous["source_sha256"]!=source_sha or
                previous["curve_direction_sha256"]!=curve_sha or
                previous["dyadic_conjugacy_sha256"]!=polynomial_sha or
                previous["ode_rtol"]!=args.tolerance or previous["rays"]!=args.rays):
            raise ValueError("resume source, H, direction, or solver input changed")
        if previous["status"]=="complete":
            print(json.dumps({"progress":"matching completed H-node rays already saved"}),flush=True)
            return
        blocks=previous["completed_blocks"]
        mapper.calls=previous["current_rhs_calls"]
        if blocks:
            mapper.maximum_N=max(b["maximum_N"] for b in blocks)
            mapper.minimum_qbar=min(b["minimum_qbar"] for b in blocks)
    common=dict(source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                original_schur_source_sha256=param["source_sha256"],
                original_schur_directions_sha256=directions_sha,
                curve_direction_sha256=curve_sha,
                curve_eigen_increment=eta.tolist(),curve_mean_increment=(basis@eta).tolist(),
                dyadic_conjugacy_file=args.dyadic_conjugacy.name,
                dyadic_conjugacy_sha256=polynomial_sha,
                target=args.target,target_rotation=rho,angular_scale=scale,
                target_root=mapper.root,root_parameter_derivative=float(mapper.root_columns[0]),
                ode_rtol=args.tolerance,rays=args.rays,
                curve_adapter_comparison_max=adapter_error,
                family_convention="local affine phase-vector curve through saved source; synchronous target g0(p); saved radius_shift fixed")
    for first in range(sum(len(b["x"]) for b in blocks),args.rays,args.block_size):
        sl=slice(first,first+args.block_size)
        returned,jac,column=mapper.round_trip(H[sl]/scale,args.tolerance)
        block=dict(x=x[sl].tolist(),input_physical_angles=(H[sl]/scale).tolist(),
                   returned_physical_angles=returned.tolist(),angular_derivative=jac.tolist(),
                   parameter_column_physical=column[0].tolist(),
                   maximum_N=mapper.maximum_N,minimum_qbar=mapper.minimum_qbar)
        blocks.append(block)
        partial=dict(**common,status="partial",completed_blocks=blocks,current_rhs_calls=mapper.calls)
        args.out.write_text(json.dumps(partial,indent=2)+"\n")
        print(json.dumps({"progress":"actual H-node block saved","completed_rays":first+len(returned)}),flush=True)
    returned=np.concatenate([b["returned_physical_angles"] for b in blocks])
    jac=np.concatenate([b["angular_derivative"] for b in blocks])
    column=scale*np.concatenate([b["parameter_column_physical"] for b in blocks])
    error=scale*returned-shifted_H
    errorprime=jac*Hp-shifted_Hp
    weighted=column/shifted_Hp
    result=dict(**common,status="complete",kind="floating_actual_ray_conjugacy_error_and_real_parameter_twist",
                completed_blocks=blocks,rhs_calls=mapper.calls,
                conjugacy_error=error.tolist(),conjugacy_error_derivative=errorprime.tolist(),
                parameter_column_normalized=column.tolist(),
                weighted_twist_integrand=weighted.tolist(),
                sampled_error_max=float(np.max(np.abs(error))),
                sampled_error_derivative_max=float(np.max(np.abs(errorprime))),
                sampled_weighted_error_mean=float(np.mean(error/shifted_Hp)),
                sampled_weighted_twist_mean=float(np.mean(weighted)),
                sampled_twist_integrand_range=[float(weighted.min()),float(weighted.max())],
                proposed_linear_parameter_correction=float(-np.mean(error/shifted_Hp)/np.mean(weighted)),
                maximum_sampled_N=mapper.maximum_N,minimum_radial_qbar=mapper.minimum_qbar,
                limitations=["actual rays freshly integrated at H nodes; still floating with no ODE or quadrature certificate",
                             "original binary radial reflection defect remains unpaid",
                             "H is the exact dyadic polynomial, but its node evaluation here uses floating exp",
                             "real-node twist and residual do not supply analytic Wiener E0/P/Q/T/B bounds",
                             "original Schur direction is a finite least-residual column, not a PDE tangent",
                             "no exact conjugacy, PDE inverse, or closed-flex conclusion"])
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in
                     ("status","target_root","root_parameter_derivative","sampled_error_max",
                      "sampled_error_derivative_max","sampled_weighted_error_mean",
                      "sampled_weighted_twist_mean","sampled_twist_integrand_range",
                      "proposed_linear_parameter_correction")}),flush=True)


if __name__=="__main__":
    main()
