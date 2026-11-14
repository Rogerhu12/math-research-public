#!/usr/bin/env python3
"""Exact rational example for R24; no actual closed surface is certified."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--out',type=Path,required=True)
a=p.parse_args()
rc=F(1,20);k=F(1,160);A=k*rc**2/512;G=k*rc/2;Kb=16*k
d0=3*rc/8;tau0=F(149,1250);tau=F(1183,10000)
left=1/tau0+2*G/d0+4*A/d0**2
right=(1-2*A/d0)**2/tau
linear_cost=k*(rc/d0+rc**2/(128*d0**2)+rc**2/(128*tau*d0))
checks=dict(positive_reach_margin=0<tau<tau0,small_displacement=2*A<d0,
    marker_Hessian=Kb<=1/tau,full_pair_inequality=left<=right,
    simpler_sufficient_inequality=linear_cost<=1/tau-1/tau0,
    height_identity=A==F(1,32768000),normal_change_identity=G==F(1,6400),
    marker_Hessian_identity=Kb==F(1,10),diameter_budget=tau/F(3,100)==F(1183,300))
if not all(checks.values()):raise AssertionError(checks)
quantities=dict(rc=rc,k=k,height_bound=A,normal_change_bound=G,marker_Hessian_bound=Kb,
    separation_lower=d0,base_reach_certificate=tau0,target_reach=tau,
    pair_left=left,pair_right=right,pair_slack=right-left,
    simpler_linear_cost=linear_cost,inverse_reach_margin=1/tau-1/tau0,
    target_diameter_upper=tau/F(3,100))
out=dict(scope=__doc__,checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    exact={n:str(x) for n,x in quantities.items()},display={n:float(x) for n,x in quantities.items()},
    unpaid=['An actual closed unmarked surface with the stated all-pair certificate.',
            'The stated support separation from every part outside its own flat patch.',
            'The continuous diameter upper bound and fixed-g exact family.'])
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(output=str(a.out),all_checks=True,pair_slack=float(right-left))))
