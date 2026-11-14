#!/usr/bin/env python3
"""One finite conjugacy Newton prediction from actual ODE values and J.

No global circle-map interpolation supplies the state equation. The initial
finite trigonometric H interpolates the actual ray input points. A local
parameter column may be interpolated from its independently integrated
subset; every new predictor requires a fresh actual ray evaluation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline

from fourfold_circle_conjugacy import TWOPI,target_value


def real_basis(x,count,derivative=0):
    columns=[];labels=[]
    highest=count//2
    for k in range(1,highest+1):
        columns.append(k**derivative*np.cos(k*x+derivative*np.pi/2));labels.append((k,"cos"))
        if count%2 or k<highest:
            columns.append(k**derivative*np.sin(k*x+derivative*np.pi/2));labels.append((k,"sin"))
    return np.array(columns).T,labels


def unpack_nodes(saved):
    keys=("x","input_physical_angles","returned_physical_angles","angular_derivative")
    return [np.concatenate([b[k] for b in saved["completed_blocks"]]) for k in keys]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actual-nodes",type=Path,nargs="+",required=True)
    parser.add_argument("--parameter-nodes",type=Path,required=True)
    parser.add_argument("--base-global-parameter",type=float,required=True)
    parser.add_argument("--target",choices=["D5","D8"],default="D5")
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--checkpoint",type=Path,required=True)
    args=parser.parse_args()
    sets=[json.loads(p.read_text()) for p in args.actual_nodes]
    first=sets[0]
    for saved in sets:
        if (saved["status"]!="complete" or saved["source_sha256"]!=first["source_sha256"]
                or saved["dyadic_conjugacy_sha256"]!=first["dyadic_conjugacy_sha256"]):
            raise ValueError("actual node sets must use exactly one geometry and one H")
    arrays=[unpack_nodes(saved) for saved in sets]
    x,theta,y,jac=[np.concatenate([v[index] for v in arrays]) for index in range(4)]
    order=np.argsort(x);x,theta,y,jac=[v[order] for v in (x,theta,y,jac)]
    count=len(x);ideal=np.arange(count)*TWOPI/count
    grid_error=float(np.max(np.abs(x-ideal)))
    if grid_error>2e-14:raise ValueError("need one complete uniform circle grid, possibly assembled from staggered pieces")
    x=ideal;alpha=TWOPI*target_value(args.target)
    basis,labels=real_basis(x,count)
    shifted,_=real_basis(x+alpha,count)
    displacement=4*theta-x
    constant=float(np.mean(displacement))
    coefficient=np.linalg.lstsq(basis,displacement-constant,rcond=None)[0]
    interpolation_error=float(np.max(np.abs(constant+basis@coefficient-displacement)))
    if interpolation_error>1e-10:raise ValueError("finite initial H does not reproduce actual ray inputs")
    parameter=json.loads(args.parameter_nodes.read_text())
    if parameter["source_sha256"]!=first["source_sha256"] or parameter["dyadic_conjugacy_sha256"]!=first["dyadic_conjugacy_sha256"]:
        raise ValueError("parameter column belongs to another geometry or H")
    px=np.concatenate([b["x"] for b in parameter["completed_blocks"]])
    pg=np.array(parameter["parameter_column_normalized"])
    pspline=CubicSpline(np.r_[px,px[0]+TWOPI],np.r_[pg,pg[0]],bc_type="periodic",extrapolate="periodic")
    column=pspline(x)
    error=4*y-x-alpha-constant-shifted@coefficient
    matrix=np.column_stack((jac[:,None]*basis-shifted,column))
    correction=np.linalg.solve(matrix,-error)
    proposed=coefficient+correction[:-1]
    dp=float(correction[-1])
    dense=np.arange(16*count)*TWOPI/(16*count)
    dbasis,_=real_basis(dense,count,1)
    hprime=1+dbasis@proposed
    if hprime.min()<=0:raise ValueError("predicted trigonometric H loses positive derivative")
    # Precompose with rotation -constant. This exactly removes H's mean
    # displacement without changing a true conjugacy equation. The resulting
    # polynomial can contain both cosine and sine at the old Nyquist mode.
    degree=count//2;export_count=2*degree+1
    xx=np.arange(export_count)*TWOPI/export_count
    export_basis,_=real_basis(xx-constant,count)
    h_values=export_basis@proposed
    metadata=dict(kind="actual_ODE_value_J_finite_conjugacy_Newton_predictor_not_verified_new_solution",
                  source_sha256=first["source_sha256"],source_H_sha256=first["dyadic_conjugacy_sha256"],
                  target=args.target,rotation_number=target_value(args.target),angular_scale=4.,
                  base_global_parameter=args.base_global_parameter,parameter=dp,
                  proposed_global_parameter=args.base_global_parameter+dp,
                  degree=degree,precomposition_angle=-constant,
                  curve_direction_sha256=parameter["curve_direction_sha256"])
    np.savez_compressed(args.checkpoint,h_values=h_values,metadata=np.array(json.dumps(metadata)))
    report=dict(**metadata,actual_samples=count,parameter_samples=len(px),
                actual_node_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in args.actual_nodes},
                parameter_node_sha256=hashlib.sha256(args.parameter_nodes.read_bytes()).hexdigest(),
                checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                complete_grid_error=grid_error,initial_H_interpolation_error=interpolation_error,
                initial_actual_collocation_residual=float(np.max(np.abs(error))),
                linear_residual=float(np.max(np.abs(matrix@correction+error))),
                proposed_Hprime_sample_range=[float(hprime.min()),float(hprime.max())],
                proposed_H_correction_sample_max=float(np.max(np.abs(basis@correction[:-1]))),
                proposed_Hprime_correction_sample_max=float(np.max(np.abs(dbasis@correction[:-1]))),
                matrix_condition_number=float(np.linalg.cond(matrix)),
                basis_labels=labels,initial_coefficients=coefficient.tolist(),
                coefficient_correction=correction[:-1].tolist(),
                limitations=["state values and J are actual rays, but remain floating with unpaid radial reflection defect",
                             "parameter column interpolated from its actual subset; no analytic error bound",
                             "finite circle Newton, no nonlinear acceptance before fresh actual ODE validation",
                             "initial trigonometric H is redefined from node values, not claimed equal off grid to the previous H",
                             "new H requires its own dyadic certificate; no R31 E/P/Q/T/B gate yet"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in
                     ("proposed_global_parameter","parameter","actual_samples","initial_actual_collocation_residual",
                      "linear_residual","proposed_Hprime_sample_range","proposed_H_correction_sample_max",
                      "proposed_Hprime_correction_sample_max","matrix_condition_number")}),flush=True)


if __name__=="__main__":main()
