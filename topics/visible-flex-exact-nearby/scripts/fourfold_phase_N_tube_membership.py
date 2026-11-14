#!/usr/bin/env python3
"""Exact dyadic control-box membership for the R57 real N tube.

The interval N computation forgets all correlations between raw coefficients.
Consequently its conclusion applies to every explicitly symmetrized R33 graph
whose raw phase controls and alpha lie in that same box, with all background
inputs identical. The test below only compares finite exact binary64 numbers;
it does not identify a rounded checkpoint with the exact affine family.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_core_N_interval import materialize
from fourfold_phase_root_interval import Box


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint",type=Path,required=True)
    parser.add_argument("--candidate-inputs",type=Path,required=True)
    parser.add_argument("--origin-inputs",type=Path,required=True)
    parser.add_argument("--frozen-direction",type=Path,required=True)
    parser.add_argument("--tube-certificate",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    tube=json.loads(args.tube_certificate.read_text())
    if not tube.get("uniform_parameter_N_negative_proved") or not tube.get("closed_interval_coverage_verified"):
        raise ValueError("need a completed continuous tube certificate")
    if digest(args.origin_inputs)!=tube["origin_inputs_sha256"] or digest(args.frozen_direction)!=tube["frozen_direction_sha256"]:
        raise ValueError("origin or direction differs from certified box")
    if not args.candidate_inputs.exists():materialize(args.checkpoint,args.candidate_inputs)
    with np.load(args.origin_inputs,allow_pickle=False) as z:origin={k:z[k].copy() for k in z.files}
    with np.load(args.frozen_direction,allow_pickle=False) as z:direction={k:z[k].copy() for k in z.files}
    with np.load(args.candidate_inputs,allow_pickle=False) as z:candidate={k:z[k].copy() for k in z.files}
    source_sha=digest(args.checkpoint)
    if json.loads(str(candidate["metadata"]))["checkpoint_sha256"]!=source_sha:
        raise ValueError("candidate snapshot belongs to another checkpoint")
    if set(origin)!=set(candidate):raise ValueError("candidate input schema changed")
    variable={"phase_coefficients":"phase_direction_coefficients","alpha":"alpha_direction"}
    fixed=[k for k in origin if k not in {*variable,"metadata"}]
    fixed_checks={k:bool(np.array_equal(origin[k],candidate[k])) for k in fixed}
    interval=Box(*tube["exact_parameter_interval"])
    checks={}
    for name,dname in variable.items():
        envelope=Box(origin[name])+interval*direction[dname]
        values=candidate[name]
        if values.shape!=envelope.lo.shape or not np.all(np.isfinite(values)):
            raise ValueError("candidate has wrong shape or nonfinite coefficient")
        inside=(envelope.lo<=values)&(values<=envelope.hi)
        checks[name]=dict(count=int(values.size),inside=int(inside.sum()),
                         all_inside=bool(np.all(inside)),
                         outside_indices=np.argwhere(~inside).tolist(),
                         lower_box_sha256=hashlib.sha256(envelope.lo.tobytes()).hexdigest(),
                         upper_box_sha256=hashlib.sha256(envelope.hi.tobytes()).hexdigest())
    passed=all(fixed_checks.values()) and all(v["all_inside"] for v in checks.values())
    report=dict(kind="exact_dyadic_membership_in_independent_R57_control_box",
                proved=passed,source_checkpoint=str(args.checkpoint),source_sha256=source_sha,
                candidate_inputs=str(args.candidate_inputs),candidate_inputs_sha256=digest(args.candidate_inputs),
                origin_inputs_sha256=digest(args.origin_inputs),frozen_direction_sha256=digest(args.frozen_direction),
                tube_certificate_sha256=digest(args.tube_certificate),
                run_source_sha256=digest(Path(__file__)),
                fixed_input_exact_equal=fixed_checks,coefficient_membership=checks,
                comparison_semantics="stored finite binary64 endpoints and controls are exact dyadic reals; ordered comparisons introduce no rounding",
                conclusion=(dict(core=tube["core"],minimum_raw_minus_n=tube["minimum_raw_minus_n"],
                                 maximum_unit_N_upper=tube["maximum_unit_N_upper"],
                                 geometry="explicit reflection of candidate controls followed by the infinite R33 primitive") if passed else None),
                limitations=["does not prove candidate lies exactly on the affine one-parameter curve",
                             "does not convert approximate-mirror floating rays into the certified symmetric graph",
                             "no complex-domain, metric equation, closed surface or reach conclusion"])
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("proved","source_sha256","candidate_inputs_sha256","coefficient_membership","conclusion")}),flush=True)
    if not passed:raise SystemExit("candidate is outside the certified control box")


if __name__=="__main__":main()
