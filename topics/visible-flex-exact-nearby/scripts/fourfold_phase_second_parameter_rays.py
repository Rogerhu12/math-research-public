#!/usr/bin/env python3
"""Floating actual return parameter two-jets in the fixed-tau R62 chart.

The five state rows are physical angle, log angular derivative, actual first
and second parameter derivatives, and parameter derivative of log J. This
diagnostic does not certify a continuous parameter or angular norm.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import numpy as np
from scipy.integrate import solve_ivp

from fourfold_phase_affine_second_variation import ActualAffineSecondField, digest
from fourfold_phase_conjugacy_nodes import evaluate_polynomial
from fourfold_phase_knot_aligned_probe import radial_cuts
from fourfold_phase_symmetric_geometry import load_exact_object


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object",type=Path,required=True)
    parser.add_argument("--root-certificate",type=Path,required=True)
    parser.add_argument("--dyadic-conjugacy",type=Path,required=True)
    parser.add_argument("--comparison",type=Path)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--progress",type=Path)
    parser.add_argument("--grid-nodes",type=int,default=516)
    parser.add_argument("--rays",type=int,default=8)
    parser.add_argument("--tolerance",type=float,default=1e-9)
    args=parser.parse_args()
    geometry,definition=load_exact_object(args.object)
    root=json.loads(args.root_certificate.read_text())
    if (not root["proved"] or root["delta_binary64_hex"] != definition["delta_hex"]
        or root["origin_inputs_sha256"] != definition["origin_inputs"]["sha256"]
        or root["frozen_direction_sha256"] != definition["direction"]["sha256"]):
        raise ValueError("root belongs to another exact affine object")
    field=ActualAffineSecondField(geometry,root["root_center"])
    cuts,metadata=radial_cuts(geometry.frozen,field.root,1e-13)
    indices=np.floor(np.arange(args.rays)*args.grid_nodes/args.rays).astype(int)
    x=indices*2*np.pi/args.grid_nodes
    H=x+evaluate_polynomial(json.loads(args.dyadic_conjugacy.read_text()),x)
    state=np.zeros((5,args.rays));state[0]=H/4
    initial=state[0].copy()
    calls=0;started=time.monotonic();branch_records=[]
    for sign,times in ((-1.,cuts),(1.,cuts[::-1])):
        before=calls;steps=0
        def fun(tau,flat):
            nonlocal calls
            calls+=1
            if args.progress and calls%100==0:
                args.progress.write_text(json.dumps(dict(rhs_calls=calls,tau=float(tau),
                    branch=len(branch_records),elapsed_seconds=time.monotonic()-started))+"\n")
            return field.rhs(tau,flat.reshape(5,args.rays),sign).ravel()
        for left,right in zip(times[:-1],times[1:]):
            sol=solve_ivp(fun,(left,right),state.ravel(),method="DOP853",
                rtol=args.tolerance,atol=args.tolerance/20,
                first_step=min(abs(right-left),np.pi/64),max_step=np.pi/64)
            if not sol.success:raise RuntimeError(sol.message)
            state=sol.y[:,-1].reshape(5,args.rays);steps+=len(sol.t)-1
        branch_records.append(dict(sign=sign,accepted_steps=steps,rhs_calls=calls-before,
            endpoint_state=state.tolist()))
        print(json.dumps(dict(progress="parameter two-jet branch complete",branches=len(branch_records),
            rhs_calls=calls,elapsed_seconds=time.monotonic()-started)),flush=True)
    J=np.exp(state[1]);Rtp=J*state[4]
    report=dict(kind="floating_exact_affine_actual_return_parameter_second_variation",
        object_sha256=digest(args.object),root_certificate_sha256=digest(args.root_certificate),
        dyadic_conjugacy_sha256=digest(args.dyadic_conjugacy),
        source_sha256=digest(Path(__file__)),
        second_source_sha256=digest(Path(__file__).with_name("fourfold_phase_affine_second_variation.py")),
        exact_delta_fraction=root["exact_delta_fraction"],root=field.root,
        root_parameter=field.root_p,root_parameter_parameter=field.root_pp,
        initial_grid_nodes=args.grid_nodes,selected_indices=indices.tolist(),
        input_physical_angles=initial.tolist(),returned_physical_angles=state[0].tolist(),
        angular_derivative=J.tolist(),parameter_first_physical=state[2].tolist(),
        parameter_second_physical=state[3].tolist(),theta_parameter=Rtp.tolist(),
        normalized_parameter_first=(4*state[2]).tolist(),
        normalized_parameter_second=(4*state[3]).tolist(),
        normalized_angle_parameter=Rtp.tolist(),
        branch_records=branch_records,ode_rtol=args.tolerance,knot_alignment=metadata,
        rhs_calls=calls,elapsed_seconds=time.monotonic()-started,
        limitations=["floating selected rays only, no continuous angular or parameter certificate",
            "no finite-difference parameter source; root and actual profile derivatives use R62",
            "finite primitive, root centre, quadrature and floating rounding costs remain unpaid"])
    if args.comparison:
        other=json.loads(args.comparison.read_text())
        if (other["source_sha256"]!=report["object_sha256"]
            or other["root_certificate_sha256"]!=report["root_certificate_sha256"]
            or other["dyadic_conjugacy_sha256"]!=report["dyadic_conjugacy_sha256"]
            or other["rays"]!=args.grid_nodes or other["status"]!="complete"):
            raise ValueError("comparison map identity/grid mismatch")
        take=lambda name: np.concatenate([b[name] for b in other["completed_blocks"]])[indices]
        report["comparison"]=dict(source_sha256=digest(args.comparison),
            input_angle_max_difference=float(np.max(abs(initial-take("input_physical_angles")))),
            return_max_difference=float(np.max(abs(state[0]-take("returned_physical_angles")))),
            J_max_difference=float(np.max(abs(J-take("angular_derivative")))),
            first_parameter_max_difference=float(np.max(abs(state[2]-take("parameter_column_physical")))))
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps(dict(completed=True,rhs_calls=calls,
        maximum_normalized_second=float(np.max(abs(4*state[3]))),
        maximum_normalized_angle_parameter=float(np.max(abs(Rtp))),
        comparison=report.get("comparison"))),flush=True)


if __name__=="__main__":main()
