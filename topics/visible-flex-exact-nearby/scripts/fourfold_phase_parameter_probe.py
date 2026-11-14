#!/usr/bin/env python3
"""A small immutable synchronous-target parameter probe and sampled C2 gates.

The canonical checkpoint is never changed. The saved probe is a finite
Schur predictor, not a Newton-corrected solution or exact PDE family.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_geometry import load_phase, PhaseGeometry
from fourfold_phase_type_control import finite_body_type


def c2_gate_samples(solver, vector, trial, angles=256):
    sections = []
    for label, xs in (("core_N", np.linspace(0., .30, 121)),
                      ("strict_negative_core", np.linspace(0., .20, 81)),
                      ("outer_positive_window", np.linspace(.30, .60, 121))):
        ratio_n, ratio_area, ratio_d, margin_n = [], [], [], []
        for start in range(0, len(xs), 24):
            x=xs[start:start+24]
            old=solver.geometry(vector,x,angles)[0]
            new=solver.geometry(trial,x,angles)[0]
            _,fx,ft,fxx,fxt,ftt=old
            _,wx,wt,wxx,wxt,wtt=[b-a for a,b in zip(old,new)]
            cross=np.cross(ft,fx);area=np.linalg.norm(cross,axis=-1)
            dot=lambda a,b:np.sum(a*b,axis=-1)
            norm=lambda a:np.linalg.norm(a,axis=-1)
            l,m,n=[dot(cross,a) for a in (fxx,fxt,ftt)]
            q=norm(ft)*norm(wx)+norm(fx)*norm(wt)+norm(wx)*norm(wt)
            rl,rm,rn=[q*norm(f)+(area+q)*norm(w) for f,w in
                       ((fxx,wxx),(fxt,wxt),(ftt,wtt))]
            error=np.abs(n)*rl+np.abs(l)*rn+rl*rn+2*np.abs(m)*rm+rm*rm
            ratio_n.extend((rn/(-n)).ravel())
            ratio_area.extend((q/area).ravel())
            ratio_d.extend((error/np.abs(l*n-m*m)).ravel())
            margin_n.extend((-n-rn).ravel())
        entry=dict(region=label, interval=[float(xs[0]),float(xs[-1])],
                   radial_samples=len(xs),quarter_angles=angles,
                   max_q_over_area=float(max(ratio_area)),
                   max_rn_over_minus_n=float(max(ratio_n)),
                   minimum_minus_n_minus_rn=float(min(margin_n)))
        if label != "core_N":
            entry["max_determinant_error_over_old_abs_D"]=float(max(ratio_d))
        sections.append(entry)
    return dict(kind="R44_finite_actual_W_gates_at_samples_only",sections=sections,
                actual_W_used=True,continuous_bounds_or_roundoff_certified=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint",type=Path,required=True)
    p.add_argument("--directions",type=Path,required=True)
    p.add_argument("--parameter-map",type=Path,required=True)
    p.add_argument("--trial-checkpoint",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--eigen-parameters",type=float,nargs=3,default=[.002,.0002,0.])
    args=p.parse_args()
    source_sha=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    direction_sha=hashlib.sha256(args.directions.read_bytes()).hexdigest()
    param=json.loads(args.parameter_map.read_text())
    if param["source_sha256"] != source_sha or param["direction_sha256"] != direction_sha:
        raise ValueError("parameter response and geometry must be the same saved input")
    with np.load(args.directions,allow_pickle=False) as z:directions=z["directions"].copy()
    basis=np.array(param["eigenbasis_columns"]);eta=np.array(args.eigen_parameters)
    increment=basis@eta
    geometry,solver,vector,metadata=load_phase(args.checkpoint)
    trial=vector+increment@directions
    probe=PhaseGeometry(solver,trial,geometry.nodes)
    with np.load(args.checkpoint,allow_pickle=False) as z:saved={key:z[key] for key in z.files}
    probe_meta=dict(metadata)
    probe_meta.update(kind="floating_small_positive_twist_probe_not_Newton",
                      source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                      direction_sha256=direction_sha,eigen_parameters=eta.tolist(),
                      mean_increment=increment.tolist(),Newton_corrected=False)
    saved["vector"]=trial;saved["metadata"]=np.array(json.dumps(probe_meta))
    np.savez_compressed(args.trial_checkpoint,**saved)
    response=np.array(param["eigen_columns"])@eta
    report=dict(kind="floating_parameter_probe_actual_geometry_and_C2_gates",
                source_checkpoint=args.checkpoint.name,source_sha256=source_sha,
                direction_sha256=direction_sha,
                trial_checkpoint=args.trial_checkpoint.name,
                trial_sha256=hashlib.sha256(args.trial_checkpoint.read_bytes()).hexdigest(),
                eigen_parameters=eta.tolist(),mean_increment=increment.tolist(),
                new_alpha=probe.alpha.tolist(),
                first_order_return_response_range=[float(response.min()),float(response.max())],
                response_sample_count=len(response),
                parameter_target_convention="synchronous E=<|Fx|^2>,a=saved circumference radius",
                Newton_corrected=False,
                limitations=["ordinary floating samples; no continuous certificate",
                             "finite Schur predictor, not an exact PDE family",
                             "canonical checkpoint unchanged"])
    solver.prepare(metadata["beta_waist"],gauss=3,angles=geometry.nodes)
    report["diagnostic"]=solver.diagnostic(trial,samples=1201,angles=geometry.nodes)
    report["sampled_C2_gates"]=c2_gate_samples(solver,vector,trial,geometry.nodes)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({key:report[key] for key in
                      ("trial_sha256","mean_increment","new_alpha","diagnostic","sampled_C2_gates")}),flush=True)
    report["finite_body_type"]=finite_body_type(probe,solver,trial)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"progress":"probe type scan completed","type":{
        key:value for key,value in report["finite_body_type"].items() if key not in
        ("rows","central_actual_root_diagnostic")}}),flush=True)


if __name__=="__main__":
    main()
