#!/usr/bin/env python3
"""Static core corridor for amplitude continuation with bounded c6 drift.

This constructs a path of planar support curves, not a path of solved
prefixes. All coefficients from physical frequency 6 upward are held at
the saved values. q increases and q4 follows its old linear law, with the
stored q4 roundoff offset retained exactly. Rational inequalities certify
only planar curvature-radius and initial axial-witness budgets.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def fraction_record(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                decimal_display=float(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--response', type=Path, required=True)
    parser.add_argument('--landing-q', default='.402')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    entry_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    raw = args.input.read_bytes()
    saved = json.loads(gzip.decompress(raw) if args.input.suffix == '.gz' else raw)
    local = json.loads(args.response.read_text())
    coeff = np.asarray(saved['core']['coefficients'], dtype=float)
    if (not saved['solver_success'] or saved['core']['frequencies'] != list(range(2, 2*len(coeff)+1, 2))
            or saved['frozen_profile']['start_acceleration'] != .45):
        raise ValueError('Expected successful m2-even core with initial acceleration .45')
    exact = [F.from_float(float(value)) for value in coeff]
    q0, b0 = exact[:2]
    target = F(args.landing_q)
    if target < q0:
        raise ValueError('The core corridor increases q')
    # Exact rational enclosure of 1/sqrt(2), checked by squaring positives.
    mu_lo, mu_hi = F('0.7071067811865475'), F('0.7071067811865476')
    assert 0 < mu_lo*mu_lo < F(1, 2) < mu_hi*mu_hi
    epsilon = max(abs(b0+q0*mu_lo/10), abs(b0+q0*mu_hi/10))
    higher = sum((4*j*j-1)*abs(c) for j, c in enumerate(exact, 1) if j >= 3)
    rho_lower = 1-3*target*mu_hi-15*epsilon-higher
    odd_tail = sum(c for j, c in enumerate(exact, 1) if j >= 3 and j % 2)
    gap = 2*(target+odd_tail)
    starting_gap = 2*(q0+odd_tail)
    starting_axis_rho = 1+3*q0-15*b0-sum((4*j*j-1)*c*((-1)**j)
        for j, c in enumerate(exact, 1) if j >= 3)
    b_lower = b0-(target-q0)*mu_hi/10
    axis_rho_upper = 1+3*target-15*b_lower-sum((4*j*j-1)*c*((-1)**j)
        for j, c in enumerate(exact, 1) if j >= 3)
    witness_upper = F(9, 20)*gap*axis_rho_upper
    diameter_budget = 5*gap
    core_radius_surplus = rho_lower-F(3, 100)*diameter_budget
    assert rho_lower > 0 and starting_gap > 0 and starting_axis_rho > 0
    assert gap > 0 and witness_upper < F(19, 20)
    assert core_radius_surplus > 0
    j = np.arange(1, len(coeff)+1)
    rows = []
    for q in sorted(set([float(q0), .09, .10, .15, .2, .25, .3, .35, .38, .4, float(target)])):
        c = coeff.copy()
        c[0] = q
        c[1] = float(b0)-(q-float(q0))/(10*math.sqrt(2))
        rho = np.r_[1., -(4*j*j-1)*c]
        critical = np.polynomial.chebyshev.chebroots(np.polynomial.chebyshev.chebder(rho))
        points = [-1., 1.]+[z.real for z in critical if abs(z.imag)<1e-9 and -1 <= z.real <= 1]
        values = np.polynomial.chebyshev.chebval(points, rho)
        d = 2*float(np.sum(c[j % 2 == 1]))
        rows.append(dict(q=q, q4=float(c[1]), c6=float(c[2]), axial_phase_witness=d,
                         floating_minimum_rho=float(min(values)),
                         floating_axis_rho=float(np.polynomial.chebyshev.chebval(-1., rho)),
                         core_distance_diameter_budget=5*d))
    directions = {}
    for row in local['rows']:
        if row['direction'] in ('actual_q4', 'boost_speed', 'vu'):
            a = row['core_derivative'][2]
            directions[row['direction']] = dict(dc6=a,
                d_delta=row['parameter_derivative'][0], d_boost_length=row['parameter_derivative'][1],
                extrapolated_step_to_zero_current_c6=-coeff[2]/a,
                scope='Derivative at the old q=.085, vu=.35, M12/N256 solution. The extrapolated zero-c6 step is outside verified local validity and is not an authorized predictor.')
    result = dict(scope=__doc__, nonlinear_solution=False,
                  input=str(args.input), input_sha256=hashlib.sha256(raw).hexdigest(),
                  source_sha256=entry_sha, local_response=str(args.response),
                  local_response_sha256=hashlib.sha256(args.response.read_bytes()).hexdigest(),
                  path='c1=q; c2=b0-(q-q0)/(10*sqrt(2)); cj=cj_saved for j>=3.',
                  source_coefficients=coeff.tolist(), landing_q=str(target),
                  rational_endpoint_certificate=dict(inverse_sqrt_two_interval=[fraction_record(mu_lo), fraction_record(mu_hi)],
                    retained_q4_roundoff_offset_abs_bound=fraction_record(epsilon),
                    higher_weighted_l1_from_frequency_6=fraction_record(higher),
                    all_angle_rho_lower=fraction_record(rho_lower),
                    axial_phase_witness=fraction_record(gap),
                    axis_rho_upper=fraction_record(axis_rho_upper),
                    R7_initial_witness_product_upper=fraction_record(witness_upper),
                    core_distance_diameter_budget=fraction_record(diameter_budget),
                    rho_minus_point03_core_diameter=fraction_record(core_radius_surplus)),
                  whole_path_reason='q increases; the rho lower bound decreases, while the positive axial gap and short-axis rho increase. Endpoint inequalities therefore control this entire planar-core path.',
                  limitations='The BVP leaves higher core harmonics free, so its solutions need not follow this static path. No full-surface diameter, held quantity, reach, tail closure, or amplitude existence is established.',
                  sampled_floating_core_table=rows, old_local_control_directions=directions,
                  missing_local_quantity='No actual_q1 derivative exists in the old response file. The next genuine q=.09 solve or a refreshed full M20 response must provide dc6/dq along the q4 law.')
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(landing_q=str(target), rho_lower=float(rho_lower),
                          axial_witness=float(gap), diameter_budget=float(diameter_budget),
                          R7_upper=float(witness_upper), radius_surplus=float(core_radius_surplus)), indent=2))


if __name__ == '__main__':
    main()
