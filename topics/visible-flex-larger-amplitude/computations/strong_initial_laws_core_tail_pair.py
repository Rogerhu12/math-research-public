#!/usr/bin/env python3
"""Exact one-dimensional tail cancellation in the saved current tangent model.

AI-assisted research, strong_recovery, 2026-11-13.
For a unit frontload increment and a decrease r in start_acceleration, minimize
sum_{m>=floor}(m^2-1)|dc_frontload[m]-r*dc_k0[m]|. A weighted median gives an
exact minimizer for these saved binary coefficients; its subgradient condition
is checked with Fractions. This is not a finite warm field or a solved design,
and does not predict its geometry or certify its numerical BVP derivative.
"""
from __future__ import annotations
import argparse
import datetime
from fractions import Fraction
import hashlib
import json
from pathlib import Path

READER_SHA = '0e17682e0feaab068ae30a1beff2c36155018623c1f64c09d4c4bd7cc7e5700f'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact(value):
    return Fraction.from_float(float(value))


def rational(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator), display=float(value))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('budget','budget-owned','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh result path')
    budget=json.loads(args.budget.read_text());resource=json.loads(args.budget_owned.read_text())
    checks={}
    def check(name,value):
        if not value:raise ValueError('Saved-model pair check failed: '+name)
        checks[name]=True
    check('original_full_vector_core_reader_identity',budget['source_sha256']==READER_SHA
          and budget['schema']=='actual-complete-nine-control-core-design-budget-v1'
          and budget['modes']==32 and budget.get('all_checks') is True)
    check('reader_actually_owned_exit_zero',resource.get('exitcode')==0
          and resource.get('wait4_observed') is True)
    command=resource['command']
    check('owned_resource_binds_exact_budget_path',command.count('--out')==1
          and Path(command[command.index('--out')+1]).resolve()==args.budget.resolve())
    directions={row['direction']:row for row in budget['directions']}
    front,k0=directions['initial_speed_frontload'],directions['start_acceleration']
    check('physical_unit_frontload_and_k0_directions',
          front['physical_profile_derivative']['initial_speed_frontload']==1.
          and front['physical_profile_derivative'].get('start_acceleration',0.)==0.
          and k0['physical_profile_derivative']['start_acceleration']==1.
          and k0['physical_profile_derivative'].get('initial_speed_frontload',0.)==0.)
    u=list(map(exact,front['complete_core_derivative']))
    v=list(map(exact,k0['complete_core_derivative']))
    check('complete_32_mode_vectors',len(u)==len(v)==32)
    frequencies=list(range(2,65,2));baseline=list(map(exact,budget['baseline']['core']))
    gap=2*sum(baseline[::2]);rho=1+sum((m*m-1)*(-1)**j*c for j,(m,c) in enumerate(zip(frequencies,baseline)))
    initial=exact(budget['baseline']['profile']['start_acceleration'])
    rows=[]
    for floor in (16,24,32,40,48):
        pairs=sorted((a/b,(m*m-1)*abs(b)) for m,a,b in zip(frequencies,u,v) if m>=floor and b)
        total=sum(weight for unused,weight in pairs);check(f'floor_{floor}_positive_total_weight',total>0)
        cumulative=Fraction(0)
        for ratio,weight in pairs:
            cumulative+=weight
            if 2*cumulative>=total:break
        left=sum(weight for value,weight in pairs if value<ratio)
        right=sum(weight for value,weight in pairs if value>ratio)
        check(f'floor_{floor}_exact_weighted_median_subgradient',2*left<=total and 2*right<=total)
        combined=[a-ratio*b for a,b in zip(u,v)]
        before=sum((m*m-1)*abs(a) for m,a in zip(frequencies,u) if m>=floor)
        after=sum((m*m-1)*abs(a) for m,a in zip(frequencies,combined) if m>=floor)
        check(f'floor_{floor}_nonincreasing_saved_tail_seminorm',0<=after<=before)
        dg=2*sum(combined[::2])
        drho=sum((m*m-1)*(-1)**j*c for j,(m,c) in enumerate(zip(frequencies,combined)))
        dr7=-ratio*gap*rho+initial*dg*rho+initial*gap*drho
        names=set(front['physical_profile_derivative'])|set(k0['physical_profile_derivative'])
        profile={name:exact(front['physical_profile_derivative'].get(name,0.))
                 -ratio*exact(k0['physical_profile_derivative'].get(name,0.)) for name in sorted(names)}
        rows.append(dict(frequency_floor=floor,exact_optimal_k0_decrease_per_unit_frontload=rational(ratio),
            exact_positive_weight=rational(total),exact_weight_below=rational(left),exact_weight_above=rational(right),
            weighted_tail_l1_before=rational(before),weighted_tail_l1_after=rational(after),
            reduction_factor=float(before/after) if after else None,
            full_core_derivative=[rational(c) for c in combined],
            physical_profile_derivative={name:rational(value) for name,value in profile.items()},
            full_axis_gap_derivative=rational(dg),rho_short_derivative=rational(drho),
            first_order_R7_product_derivative=rational(dr7),
            complete_5_tail_seminorms={str(lo):rational(sum((m*m-1)*abs(c)
                for m,c in zip(frequencies,combined) if m>=lo)) for lo in (16,24,32,40,48)}))
    result=dict(schema='saved-current-frontload-k0-tail-pair-v1',scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_sha256=sha(__file__),
        input_sha256={str(args.budget):sha(args.budget),str(args.budget_owned):sha(args.budget_owned)},
        checks=checks,all_checks=True,baseline_modes=32,
        exact_saved_binary_baseline_gap=rational(gap),exact_saved_binary_baseline_R7_product=rational(initial*gap*rho),
        parameterization='delta(initial_speed_frontload)=t; delta(start_acceleration)=-r*t',
        exact_optimality_only_in_this_1D_saved_linear_model=True,
        no_finite_step_selected_or_geometry_or_BVP_claim=True,rows=rows,
        new_ODE_Node_Jacobian_QR_or_geometry_calls=0)
    with args.out.open('x') as stream:json.dump(result,stream,indent=2,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),checks=len(checks),
        rows=[dict(floor=row['frequency_floor'],ratio=row['exact_optimal_k0_decrease_per_unit_frontload']['display'],
                   reduction=row['reduction_factor'],gap_derivative=row['full_axis_gap_derivative']['display'],
                   R7_derivative=row['first_order_R7_product_derivative']['display']) for row in rows])),flush=True)


if __name__=='__main__':
    main()
