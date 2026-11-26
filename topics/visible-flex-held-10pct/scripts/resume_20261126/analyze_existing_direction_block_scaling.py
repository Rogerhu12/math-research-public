#!/usr/bin/env python3
"""Scalar arithmetic on one already-recorded v3 Newton direction.

No model, state vector, Jacobian, LU, BVP, or new trial is constructed. Exact
Fraction comparisons treat the recorded binary64 scalar values as literals.
This counterfactual covers only a uniform linear change of all parameter
coordinates; it does not evaluate a changed nonlinear q API or new solver.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def literal(value):
    if not isinstance(value,(int,float)) or isinstance(value,bool) or not math.isfinite(value):
        raise ValueError('A finite recorded numeric scalar is required')
    return Fraction.from_float(float(value))


def analyze(path):
    data=json.loads(Path(path).read_text())
    direction=data['direction']['merit']
    A,B=literal(direction['state']),literal(direction['controls'])
    if not A>0 or not B>0:
        raise ValueError('Both original direction blocks must have positive norm')
    rows=[];domains=[];gap=0.
    for trial in data['trials']:
        k=int(trial['exponent'])
        if not trial['domain_valid']:
            domains.append(dict(exponent=k,domain_category=trial['domain_category']))
            continue
        a,b=literal(trial['merit']['state']),literal(trial['merit']['controls'])
        gate=literal(trial['original_armijo_factor'])
        Ry,Rp=a/A,b/B
        balanced=(Ry+Rp)/2
        original=(a+b)/(A+B)
        observed=literal(trial['original_cost_ratio'])
        if observed<=0:
            raise ValueError('The recorded positive-cost trial ratio is required')
        gap=max(gap,float(abs(original-observed)/abs(observed)))
        # C_t = a+t*b, t=s^-2; positivity of weights is essential.
        constant=a-gate*A;coefficient=b-gate*B
        upper=(-constant/coefficient if constant<0 and coefficient>0 else None)
        rows.append(dict(exponent=k,alpha=trial['alpha'],
            state_ratio=float(Ry),parameter_ratio=float(Rp),original_armijo_factor=float(gate),
            state_block_pass_exact=bool(Ry<gate),parameter_block_pass_exact=bool(Rp<gate),
            any_positive_two_block_weight_can_pass_exact=bool(min(Ry,Rp)<gate),
            balanced_ratio=float(balanced),balanced_pass_exact=bool(balanced<gate),
            parameter_weight_square_upper_if_state_alone_passes=float(upper) if upper else None,
            original_ratio_recomputed=float(original),original_pass_exact=bool(original<gate)))
    byk={row['exponent']:row for row in rows}
    excluded=list(range(3,16))
    if (set(k for k in byk if 3<=k<=15)!=set(excluded) or
            not all(not byk[k]['any_positive_two_block_weight_can_pass_exact'] for k in excluded)):
        raise ValueError('The stated k3..15 finite-data exclusion is not true of this source')
    first=lambda key:min(row['exponent'] for row in rows if row[key])
    result=dict(scope=__doc__,source_json=str(Path(path).resolve()),source_json_sha256=sha(path),
        model_scope='One actual v3 M24/631-node lambda .004 diagnostic; not v4 or the whole BVP',
        existing_data_only=True,new_trials_evaluated=0,new_factorizations=0,
        solver_invoked=False,accepted_BVP_field=False,
        original_state_cost=float(A),original_parameter_cost=float(B),
        parameter_cost_fraction=float(B/(A+B)),
        coordinate_scale_equalizing_initial_blocks=math.sqrt(float(B/A)),
        corresponding_parameter_weight=math.sqrt(float(A/B)),
        exact_literal_comparisons=True,
        first_passing_exponent_original=first('original_pass_exact'),
        first_passing_exponent_equalized_blocks=first('balanced_pass_exact'),
        first_exponent_possible_for_any_positive_two_block_weight=first('any_positive_two_block_weight_can_pass_exact'),
        all_exponents_3_through_15_excluded_for_positive_two_block_weights=True,
        larger_step_factor_equalized_blocks=2**(first('original_pass_exact')-first('balanced_pass_exact')),
        largest_possible_factor_on_recorded_grid_for_two_block_weights=2**(
            first('original_pass_exact')-first('any_positive_two_block_weight_can_pass_exact')),
        maximum_relative_reconstruction_gap_from_independent_recorded_original_ratio=gap,
        domain_rejected_original_trials=domains,rows=rows,
        limits=['Only uniform linear parameter rescaling relative to one uniform state weight.',
            'No claim for per-mode weights, mixing/preconditioners, changed nonlinear q API, future directions, or an untested alpha.',
            'Exact arithmetic identity plus exact comparisons of recorded literals; not a roundoff certificate for a newly executed scaled solver.',
            'The original residual/physical BC/metric gates are unchanged; no update is performed.'])
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();result=analyze(args.source)
    result['analysis_script_sha256']=sha(__file__)
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ('source_json_sha256',
        'coordinate_scale_equalizing_initial_blocks','first_passing_exponent_original',
        'first_passing_exponent_equalized_blocks',
        'first_exponent_possible_for_any_positive_two_block_weight',
        'maximum_relative_reconstruction_gap_from_independent_recorded_original_ratio')},indent=2))


if __name__=='__main__':
    main()
