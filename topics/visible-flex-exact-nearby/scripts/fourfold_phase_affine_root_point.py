#!/usr/bin/env python3
"""Tight interval-Newton root at one exactly specified R57 affine parameter."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import floor_float,ceiling_float
from fourfold_phase_parameter_root_interval import make_affine_target
from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import up


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--frozen-direction',type=Path,required=True)
    ap.add_argument('--common-root-certificate',type=Path,required=True)
    ap.add_argument('--delta',required=True,help='Exact rational, preferably a numerator/denominator')
    ap.add_argument('--quarter-nodes',type=int,default=256)
    ap.add_argument('--iterations',type=int,default=4)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    root=json.loads(args.common_root_certificate.read_text())
    origin_sha,direction_sha=digest(args.inputs),digest(args.frozen_direction)
    if not root['proved'] or root['origin_inputs_sha256']!=origin_sha or root['frozen_direction_sha256']!=direction_sha:
        raise ValueError('a common root for these same exact affine inputs is required')
    delta=Fraction(args.delta)
    if not Fraction.from_float(root['exact_parameter_interval'][0])<=delta<=Fraction.from_float(root['exact_parameter_interval'][1]):
        raise ValueError('exact parameter lies outside the proved family interval')
    parameter=[floor_float(delta),ceiling_float(delta)]
    with np.load(args.inputs,allow_pickle=False) as saved:frozen={key:saved[key].copy() for key in saved.files}
    with np.load(args.frozen_direction,allow_pickle=False) as saved:direction={key:saved[key].copy() for key in saved.files}
    if json.loads(str(direction['metadata']))['origin_inputs_sha256']!=origin_sha:
        raise ValueError('direction origin hash differs')
    target=make_affine_target(frozen,direction,parameter,args.quarter_nodes)
    current=Box(*root['root_bracket']);steps=[]
    for index in range(args.iterations):
        center=float((Fraction.from_float(float(current.lo))+Fraction.from_float(float(current.hi)))/2)
        point=target.evaluate(Box(center));whole=target.evaluate(current)
        derivative=Box(*whole['Cprime'])
        if derivative.lo<=0:raise ValueError('interval Newton requires the proved positive Cprime here')
        proposal=Box(center)-Box(*point['C'])/derivative
        new=Box(max(float(current.lo),float(proposal.lo)),min(float(current.hi),float(proposal.hi)))
        steps.append(dict(input_interval=current.pair(),center=center,center_evaluation=point,
            interval_evaluation=whole,newton_proposal=proposal.pair(),output_interval=new.pair()))
        unchanged=new.pair()==current.pair();current=new
        if unchanged:break
    result=dict(kind='directed_interval_Newton_root_for_an_exact_R57_affine_parameter',
        proved=True,origin_inputs_sha256=origin_sha,frozen_direction_sha256=direction_sha,
        common_root_certificate_sha256=digest(args.common_root_certificate),
        source_sha256=digest(Path(__file__)),
        dependency_sha256={name:digest(Path(__file__).with_name(name)) for name in [
            'fourfold_phase_parameter_root_interval.py','fourfold_phase_core_N_interval.py',
            'fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
        exact_delta_fraction=str(delta),parameter_enclosure=parameter,
        parameter_is_exact_binary64_singleton=parameter[0]==parameter[1],
        delta_binary64_hex=parameter[0].hex() if parameter[0]==parameter[1] else None,
        quarter_nodes=args.quarter_nodes,initial_common_root_bracket=root['root_bracket'],
        root_interval=current.pair(),root_interval_width_upper=float(up(current.hi-current.lo)),
        root_center=float((Fraction.from_float(float(current.lo))+Fraction.from_float(float(current.hi)))/2),
        steps=steps,
        justification='The common-family certificate already gives the unique exact root inside every current interval; the real mean-value theorem gives t=m-C(m)/Cprime(xi), so each directed intersection retains it',
        limitations=['This is the exact affine graph at the exact rational delta, not a rounded predictor checkpoint',
            'A center float is a reference approximation; the entire reported interval is the proved root enclosure',
            'No new parameter-jet, ODE error, cap, PDE inverse, or isometric-family proof is supplied'])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key!='steps'},indent=2),flush=True)


if __name__=='__main__':main()
