#!/usr/bin/env python3
"""Pay actual normalized-parameter trace bounds for the enlarged R54 head.

Use the original uniform positive derivative and the complete R45 polar
trace constants.  All inequalities use exact Fraction arithmetic.  The
parameter norm includes all46 R54 axis units; no unweighted derivative or
Cartesian/global geometry claim is made.  The height mean constant remains
a separate scalar matching condition.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time
from closure_balance_parameter_axes_v2 import read, upper, lower, floorlog2, pair


def rational(value):
    return F(int(value['numerator']), int(value['denominator']))


def rec(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def rounded(value):
    exponent = floorlog2(value)+1
    if not 0 < value < pair(1, exponent):
        raise ArithmeticError('A strict dyadic outer rounding is required')
    return dict(exact_bound=rec(value), strict_dyadic_upper_log2=exponent)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('expanded', 'cut', 'balanced', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh exact trace ledger')
    started = time.monotonic()
    docs, hashes = {}, {}
    for name in ('expanded', 'cut', 'balanced'):
        path = getattr(args, name)
        docs[name], hashes[str(path)] = read(path)
    expanded, cut, balanced = [docs[name] for name in ('expanded', 'cut', 'balanced')]
    if (not expanded['all_gates'] or not all(expanded['gates'].values())
            or not all(cut['checks'].values()) or not balanced['all_gates']):
        raise ValueError('All original actual certificates must be successful')
    if expanded['input_hashes'].get(str(args.balanced)) != hashes[str(args.balanced)]:
        raise ValueError('The true height/radius conversion belongs to another head')
    density_matches = [value for name, value in cut['input_hashes'].items()
                       if Path(name).name == '2026-11-12-tail-r33-plateau2-density-window.json.gz']
    expanded_matches = [value for name, value in expanded['input_hashes'].items()
                       if Path(name).name == '2026-11-12-tail-r33-plateau2-density-window.json.gz']
    if len(density_matches) != 1 or density_matches != expanded_matches:
        raise ValueError('The cut trace and actual expanded head use different density/strip data')
    if len(expanded['rows']) != 641 or len(expanded['axes']) != 46 or len(expanded['cells']) != 213:
        raise ValueError('The complete expanded head is required')
    weights = [upper(row['inherited_metric_weight']) for row in expanded['rows']]
    if not all(value > 0 for value in weights):
        raise ValueError('Every original distance weight must be positive')
    lam, eta = upper(expanded['lambda_upper']), upper(expanded['fresh_lift_eta'])
    old_ratios = [upper(row['retained_parameter_source_budget'])/weights[i]
                  for i, row in enumerate(expanded['rows'])]
    old_bound = max(old_ratios)
    new_bound = eta*(1+lam)
    source_bound = max(old_bound, new_bound)
    correction_derivative = source_bound/(1-lam)
    indices = [0,213,426,639]
    labels = [('low',12),('near',12),('rest',12),('infinite',None)]
    for i, (block, cell) in zip(indices, labels):
        if expanded['rows'][i]['block'] != block or expanded['rows'][i]['cell'] != cell:
            raise ValueError('The physical cut coordinate was reordered')
    cut_weight = sum((weights[i] for i in indices),F(0))
    cut_lift = upper(expanded['cells'][0]['combined_lift'])
    physical_derivative = cut_lift+cut_weight*correction_derivative
    epsilon = rational(cut['q_cut_A_upper'])
    B = rational(cut['cut_B_lower'])
    b = upper(balanced['true_cut_radius'])
    R0 = rational(cut['R0'])
    if not 0 < b < 1 or B < 4 or R0 != F(1,256) or not 0 < lam < 1:
        raise ValueError('The actual R45 trace domain changed')
    # The fixed real background has w<=1/2.  Mean and inverse terms use the
    # original R45 full Wiener-algebra constants, with outer strip 1/64.
    coefficients = dict(P=epsilon/B, K_perp=epsilon, P_K_perp_joint=epsilon,
        K_complete_mean=F(17,16)*epsilon, G_connection=3*epsilon,
        height_nonmean=b*epsilon/(4*B), height_theta=b*epsilon/(2*B),
        height_theta_theta=3*b*epsilon/(2*B), height_r_complete_mean=F(5,8)*epsilon,
        height_r_theta=F(3,2)*epsilon, height_r_r=144*epsilon,
        polar_jet_max=144*epsilon)
    bounds = {name: rounded(value*physical_derivative) for name,value in coefficients.items()}
    for name, item in bounds.items():
        exponent = item['strict_dyadic_upper_log2']
        item.update(uniform_deviation_on_complex_unit_parameter_ball_log2=exponent,
            quadratic_remainder_coefficient_on_half_ball_log2=exponent+3,
            derivative_remainder_coefficient_times_parameter_norm_on_half_ball_log2=exponent+4)
    gates = dict(same_actual_background_and_cut_strip=True,
        all641_parameter_source_budgets_nonnegative=all(value >= 0 for value in old_ratios),
        original_uniform_contraction=0 < lam < 1,
        complete_cut_state_inside_R45_domain=1+upper(expanded['cells'][0]['combined_total']) < 2,
        full_mean_and_connection_domain=2*epsilon < R0,
        polar_jet_max_covers_each_listed_component=all(coefficients[name] <= coefficients['polar_jet_max']
            for name in ['height_nonmean','height_theta','height_theta_theta','height_r_complete_mean','height_r_theta','height_r_r']),
        actual_all46_parameter_axes_positive=all(lower(row['canonical_Q_axis']) > 0 for row in expanded['axes']),
        every_reported_rounding_strict=all(rational(item['exact_bound']) < pair(1,item['strict_dyadic_upper_log2']) for item in bounds.values()))
    out = dict(scope=__doc__, all_gates=all(gates.values()), gates=gates,
        parameter_norm='sum_j |delta Q_(2j)(b)|/v_j from the complete R54 axes; the complex unit l1 ball.',
        outer_strip=cut['chosen_outer_strip'], original_uniform_lambda=rec(lam),
        old_parameter_source_weighted_bound=rec(old_bound), fresh_parameter_source_weighted_bound=rec(new_bound),
        combined_parameter_source_weighted_bound=rec(source_bound),
        unknown_correction_derivative_in_weighted_norm=rec(correction_derivative),
        cut_weight_total=rec(cut_weight), direct_cut_lift=rec(cut_lift),
        physical_cut_derivative=rounded(physical_derivative), cut_epsilon_upper=rec(epsilon),
        trace_bounds=bounds,
        complex_extension_reason='R51/R53/R54 bounds use absolute Fourier/parameter norms and the same analytic mean, pointwise inverse, and R18 branches. They hold unchanged for complex parameters in the unit l1 ball; all connecting paths stay inside the same strict domains.',
        cauchy_reason='On parameter norm<=1/2, R45 mixed Cauchy circles give ||D2 T||<=16 M, remainder<=8 M ||a||^2 and derivative remainder<=16 M ||a||, where M is the dyadic uniform unit-ball trace deviation.',
        height_mean_constant_included=False, height_mean_constant_reason='The cuff height convention is fixed; its scalar height value at the cut still needs a separate outer matching equation. No per-cell translation is made.',
        polar_not_Cartesian=True, outer_Schur_inverse_paid=False, outer_continuous_solution_paid=False,
        inputs=hashes, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        helper_sha256=hashlib.sha256(Path(__file__).with_name('closure_balance_parameter_axes_v2.py').read_bytes()).hexdigest(),
        new_radial_integrations=0,new_kernels=0,new_matrix_inverses=0,
        seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(all_gates=all(gates.values()),gates=gates,
        physical_cut_log2=out['physical_cut_derivative']['strict_dyadic_upper_log2'],
        trace_log2={name:value['strict_dyadic_upper_log2'] for name,value in bounds.items()},
        bytes=args.out.stat().st_size,sha256=hashlib.sha256(args.out.read_bytes()).hexdigest(),
        seconds=out['seconds'],RSS_KiB=out['peak_RSS_KiB'])),flush=True)
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
