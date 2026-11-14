#!/usr/bin/env python3
"""Independent moving-root ray finite differences along the saved mean curve.

First and second difference quotients are numerical diagnostics, not uniform
Taylor bounds. The base geometry and fixed phase-vector direction are named
by hashes, and the synchronous target is recomputed at every displacement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_conjugacy_nodes import CurveGeometry,evaluate_polynomial
from fourfold_phase_geometry import load_phase,PhaseGeometry
from fourfold_phase_principal_map import PrincipalMap
from fourfold_phase_principal_parameter_map import ParameterMap


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--directions",type=Path,required=True)
    parser.add_argument("--parameter-map",type=Path,required=True)
    parser.add_argument("--dyadic-conjugacy",type=Path,required=True)
    parser.add_argument("--conjugacy-angle",type=float,default=0.)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--curve-eigen-increment",type=float,nargs=3,default=[.002,.0002,0.])
    parser.add_argument("--steps",type=float,nargs="+",default=[.05,.025])
    parser.add_argument("--tolerance",type=float,default=2e-11)
    args=parser.parse_args()
    source_sha=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    directions_sha=hashlib.sha256(args.directions.read_bytes()).hexdigest()
    parameter=json.loads(args.parameter_map.read_text())
    if directions_sha!=parameter["direction_sha256"]:
        raise ValueError("Schur input changed")
    with np.load(args.directions,allow_pickle=False) as saved:unit=saved["directions"].copy()
    eta=np.array(args.curve_eigen_increment)
    direction=(np.array(parameter["eigenbasis_columns"])@eta)@unit
    curve_sha=hashlib.sha256(direction.tobytes()).hexdigest()
    definitions=json.loads(args.dyadic_conjugacy.read_text())
    x=np.array([args.conjugacy_angle])
    theta=float((x+evaluate_polynomial(definitions,x))[0]/4)
    geometry,solver,vector,_=load_phase(args.checkpoint)
    variational=ParameterMap(CurveGeometry(solver,vector,geometry.nodes,direction),solver,
                              [.235,.24],source_sha256=source_sha,direction_sha256=curve_sha)
    r,j,c=variational.round_trip(np.array([theta]),args.tolerance)
    values={}
    for displacement in [0.]+[sign*h for h in args.steps for sign in (-1.,1.)]:
        shifted=vector+displacement*direction
        mapper=PrincipalMap(PhaseGeometry(solver,shifted,geometry.nodes),solver,[.235,.24])
        returned,jac=mapper.round_trip(np.array([theta]),args.tolerance)
        values[str(displacement)]=dict(displacement=displacement,returned=float(returned[0]),
                                       angular_derivative=float(jac[0]),target_root=mapper.root,
                                       vector_sha256=hashlib.sha256(shifted.tobytes()).hexdigest(),
                                       rhs_calls=mapper.calls)
        print(json.dumps(values[str(displacement)]),flush=True)
    center=values[str(0.)]
    differences=[]
    for h in args.steps:
        minus,plus=values[str(-h)],values[str(h)]
        first=(plus["returned"]-minus["returned"])/(2*h)
        second=(plus["returned"]-2*center["returned"]+minus["returned"])/(h*h)
        cross=(plus["angular_derivative"]-minus["angular_derivative"])/(2*h)
        differences.append(dict(step=h,first_parameter_difference=first,
                                 second_parameter_difference=second,
                                 mixed_angle_parameter_difference=cross,
                                 difference_from_variational=first-float(c[0,0]),
                                 root_first_difference=(plus["target_root"]-minus["target_root"])/(2*h),
                                 root_second_difference=(plus["target_root"]-2*center["target_root"]+minus["target_root"])/(h*h)))
    result=dict(kind="floating_actual_curve_first_second_ray_differences_not_uniform_Taylor_bounds",
                source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                original_schur_sha256=directions_sha,curve_direction_sha256=curve_sha,
                curve_eigen_increment=eta.tolist(),conjugacy_angle=args.conjugacy_angle,
                physical_initial_angle=theta,ode_rtol=args.tolerance,
                variational=dict(returned=float(r[0]),angular_derivative=float(j[0]),
                                 parameter_column=float(c[0,0]),
                                 root_parameter_column=float(variational.root_columns[0])),
                independent_samples=values,differences=differences,
                limitations=["ordinary floating ODE; no outward integration or Taylor interval bound",
                             "second quotients do not upper-bound parameter second derivatives",
                             "original radial reflection defect remains unpaid",
                             "parameter is a local phase-vector curve with synchronous radial target",
                             "R31 analytic P/Q/T/B and exact PDE family remain unpaid"])
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(differences),flush=True)


if __name__=="__main__":
    main()
