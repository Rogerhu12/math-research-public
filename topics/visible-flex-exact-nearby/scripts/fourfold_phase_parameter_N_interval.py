#!/usr/bin/env python3
"""Continuous real parameter tube for the R55 actual N<0 chart.

The family is defined by exact-real affine changes of the frozen raw phase
coefficients and alpha. Explicit reflection and the infinite R33 primitive
are applied afterward. This does not identify old rounded predictor vectors
with exact family points or certify any ray/conjugacy equation.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from fourfold_phase_compare import load
from fourfold_phase_core_N_interval import CoreNGate,ClosedSpanSplineBox
from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import derivative_coefficients


def make_direction(checkpoint,inputs,directions,parameter_map,output):
    saved=json.loads(parameter_map.read_text())
    direction_sha=hashlib.sha256(directions.read_bytes()).hexdigest()
    if saved["direction_sha256"]!=direction_sha:raise ValueError("wrong Schur source")
    with np.load(directions,allow_pickle=False) as z:unit=z["directions"]
    curve=(np.array(saved["eigenbasis_columns"])@np.array([.002,.0002,0.]))@unit
    solver,vector,_=load(checkpoint)
    coeff,alpha=solver.unpack(curve)
    positive=coeff.transpose(2,0,1)
    raw=np.concatenate((positive[::-1]*np.array([1.,-1.]),positive))
    with np.load(inputs,allow_pickle=False) as z:
        assert np.array_equal(solver.knots,z["phase_knots"])
        original_coeff,original_alpha=solver.unpack(vector)
        original_positive=original_coeff.transpose(2,0,1)
        original_raw=np.concatenate((original_positive[::-1]*np.array([1.,-1.]),original_positive))
        assert np.array_equal(original_raw,z["phase_coefficients"])
        assert np.array_equal(original_alpha,z["alpha"])
    metadata=dict(origin_inputs_sha256=hashlib.sha256(inputs.read_bytes()).hexdigest(),
                  origin_checkpoint_sha256=hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
                  Schur_directions_sha256=direction_sha,
                  eigenbasis_file_sha256=hashlib.sha256(parameter_map.read_bytes()).hexdigest(),
                  full_vector_direction_sha256=hashlib.sha256(curve.tobytes()).hexdigest(),
                  family="raw_phase=raw_phase_0+delta*raw_phase_direction; alpha=alpha_0+delta*alpha_direction; exact real arithmetic then explicit symmetry and infinite R33")
    np.savez_compressed(output,phase_direction_coefficients=raw,alpha_direction=alpha,
                        metadata=np.array(json.dumps(metadata)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--inputs",type=Path,required=True)
    parser.add_argument("--directions",type=Path,required=True)
    parser.add_argument("--parameter-map",type=Path,required=True)
    parser.add_argument("--frozen-direction",type=Path,required=True)
    parser.add_argument("--origin-certificate",type=Path,required=True)
    parser.add_argument("--parameter-radius",type=float,default=.01)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--max-depth",type=int,default=10)
    parser.add_argument("--resume",action="store_true")
    args=parser.parse_args();started=time.monotonic()
    if not args.frozen_direction.exists():
        make_direction(args.checkpoint,args.inputs,args.directions,args.parameter_map,args.frozen_direction)
    with np.load(args.inputs,allow_pickle=False) as z:frozen={k:z[k].copy() for k in z.files}
    with np.load(args.frozen_direction,allow_pickle=False) as z:direction={k:z[k].copy() for k in z.files}
    inputs_sha=hashlib.sha256(args.inputs.read_bytes()).hexdigest()
    direction_sha=hashlib.sha256(args.frozen_direction.read_bytes()).hexdigest()
    metadata=json.loads(str(direction["metadata"]))
    if metadata["origin_inputs_sha256"]!=inputs_sha:raise ValueError("frozen direction uses different origin")
    origin=json.loads(args.origin_certificate.read_text())
    if origin["inputs_sha256"]!=inputs_sha or not origin["proved_continuous_N_negative"]:
        raise ValueError("need the completed same-input origin partition")
    gate=CoreNGate(frozen,origin["quarter_nodes"],origin["angular_nodes"])
    delta=Box(-args.parameter_radius,args.parameter_radius)
    raw=Box(frozen["phase_coefficients"])+delta*direction["phase_direction_coefficients"]
    phase=ClosedSpanSplineBox.__new__(ClosedSpanSplineBox);phase.states=[]
    t,k,lo,hi=frozen["phase_knots"],5,raw.lo,raw.hi
    for order in range(6):
        phase.states.append((t,k,lo,hi))
        if order<5:t,k,lo,hi=derivative_coefficients(t,k,lo,hi)
    gate.target.phase=phase
    gate.target.alpha=[Box(a)+delta*d for a,d in zip(frozen["alpha"],direction["alpha_direction"])]
    rows=[];failures=[]
    pending=[(*row["interval"],0) for row in origin["rows"]]
    common=dict(kind="directed_uniform_real_parameter_N_tube_for_explicit_symmetric_R33_family",
                origin_inputs_sha256=inputs_sha,frozen_direction_sha256=direction_sha,
                frozen_direction=str(args.frozen_direction),family=metadata["family"],
                exact_parameter_interval=[-args.parameter_radius,args.parameter_radius],
                core=origin["core"],quarter_nodes=origin["quarter_nodes"],angular_nodes=origin["angular_nodes"],
                origin_certificate_sha256=hashlib.sha256(args.origin_certificate.read_bytes()).hexdigest(),
                run_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                N_gate_source_sha256=hashlib.sha256(Path(__file__).with_name("fourfold_phase_core_N_interval.py").read_bytes()).hexdigest())
    if args.resume and args.out.exists():
        previous=json.loads(args.out.read_text())
        for key in ("origin_inputs_sha256","frozen_direction_sha256","exact_parameter_interval","run_source_sha256"):
            if previous[key]!=common[key]:raise ValueError("resume input changed: "+key)
        if previous["status"]=="complete":print("matching completed tube already saved",flush=True);return
        rows,failures,pending=previous["rows"],previous["failures"],previous["pending"]
    queue=deque(pending);attempts=0
    def save(status):
        result=dict(**common,status=status,rows=rows,failures=failures,pending=list(queue),
                    uniform_parameter_N_negative_proved=bool(status=="complete" and not failures),
                    limitations=["exact affine control-coefficient family, not a claim that every rounded predictor file is exactly one family point",
                                 "real parameter and real angle chart only; no complex tube, parameter Taylor derivative or ray integration bound",
                                 "no exact metric equation, closed surface or reach conclusion"])
        if rows:result.update(minimum_factor=min(r["N_factor_lower"] for r in rows),
                              minimum_raw_minus_n=min(r["raw_minus_n_lower"] for r in rows),
                              maximum_unit_N_upper=max(r["actual_unit_normal_N_upper"] for r in rows))
        if status=="complete" and not failures:
            ordered=sorted(rows,key=lambda r:r["interval"][0])
            assert ordered[0]["interval"][0]==0 and ordered[-1]["interval"][1]==origin["core"][1]
            assert all(a["interval"][1]==b["interval"][0] for a,b in zip(ordered[:-1],ordered[1:]))
            result["closed_interval_coverage_verified"]=True
        args.out.write_text(json.dumps(result,indent=2)+"\n")
        return result
    while queue:
        left,right,depth=queue.popleft();attempts+=1
        row=gate.evaluate(left,right)
        if row["passed"]:rows.append(row)
        else:
            mid=float((left+right)/2)
            if depth<args.max_depth and left<mid<right:
                queue.appendleft((mid,right,depth+1));queue.appendleft((left,mid,depth+1))
            else:failures.append(row)
        if attempts%10==0:
            save("partial")
            print(json.dumps(dict(progress="parameter N cells saved",passed=len(rows),failed=len(failures),
                                  pending=len(queue),elapsed_seconds=time.monotonic()-started)),flush=True)
    result=save("complete")
    print(json.dumps({k:v for k,v in result.items() if k not in ("rows","failures","pending")}),flush=True)
    if failures:raise SystemExit("retained failed parameter cells")


if __name__=="__main__":main()
