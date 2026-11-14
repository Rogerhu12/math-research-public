#!/usr/bin/env python3
"""Check the stated R67 decimal bounds against exact saved dyadic endpoints.

Pure Fraction arithmetic; no Arb, source evaluation, ODE or new numerical
certificate is used. The already paid complete packages are immutable.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time


def dyadic(d):
    m, e = int(d['mantissa']), int(d['binary_exponent'])
    return F(m*(1 << e)) if e >= 0 else F(m, 1 << (-e))


def ends(d):
    return dyadic(d['lower']), dyadic(d['upper'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ledger', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh exact-decimal verification file')
    began = time.monotonic()
    d = json.loads(a.ledger.read_text())
    if not d['all_gates'] or not all(d['gates'].values()):
        raise ValueError('The actual complete source/Schur ledger must be paid')
    checks = []
    def upper(name, value, bound):
        q = ends(value)[1]
        target = F(bound)
        checks.append(dict(name=name, relation='<', bound=str(target), passed=q < target))
    def lower(name, value, bound):
        q = ends(value)[0]
        target = F(bound)
        checks.append(dict(name=name, relation='>', bound=str(target), passed=q > target))
    lower('entire_cell11_w_min', d['cell11_slope_lower'], '2.713198e-17')
    upper('original_relative_A1', d['candidate_original_relative_A1_upper'], '3.429795e-18')
    upper('candidate_relative_A1_change', d['candidate_relative_A1_shift_upper'], '3.982867e-38')
    upper('recentred_complete_mean_domain', d['candidate_recentred_relative_A1_upper'], '1/64')
    upper('mean_slope_change', d['complete_mean_slope_change_upper'], '2.185667e-54')
    upper('mean_height_change', d['complete_mean_height_change_upper'], '2.643039e-63')
    for cell in d['cell_rows']:
        node = cell['endpoint_physical_node']
        upper(f'node{node}_all46_two_output_l1_columns',
              cell['selected_two_output_l1_column_norm_upper'], '4.441e-8')
        if len(cell['selected_two_output_normalized_column_sums']) != 46:
            raise ValueError('An input parameter was omitted')
        for row in cell['modes']:
            m = row['mode']
            if m == 2:
                lower(f'node{node}_old_m2_cut_ratio_lower', row['cut_only_axis_ratio_lower'], '3198.4771')
                upper(f'node{node}_old_m2_cut_ratio_upper', row['cut_only_axis_ratio_upper'], '3198.4778')
                upper(f'node{node}_new_m2_cut_ratio', row['recentred_cut_only_axis_ratio_upper'], '.000298351')
            elif m == 4:
                upper(f'node{node}_old_m4_cut_ratio', row['cut_only_axis_ratio_upper'], '.004140540')
                upper(f'node{node}_new_m4_cut_ratio', row['recentred_cut_only_axis_ratio_upper'], '.004114770')
            else:
                raise ValueError('Unexpected displayed mode')
    r = next(r for r in d['recentring_rows'] if r['mode'] == 2)
    upper('m2_bump_height', r['height_sup_shift'], '2.143442e-60')
    upper('m2_bump_first_derivative', r['first_derivative_sup_shift'], '3.490420e-55')
    upper('m2_bump_second_derivative', r['second_derivative_sup_shift'], '1.010465e-49')
    B = [F(0), F(1), F(0), F(-6), F(8), F(-3)]
    D = [F(i)*B[i] for i in range(1, len(B))]
    DD = [F(i)*D[i] for i in range(1, len(D))]
    def ev(poly, x):
        return sum((c*x**j for j, c in enumerate(poly)), F(0))
    identities = dict(B0=ev(B,F(0)) == 0, B1=ev(B,F(1)) == 0,
        D0=ev(D,F(0)) == 1, D1=ev(D,F(1)) == 0,
        DD0=ev(DD,F(0)) == 0, DD1=ev(DD,F(1)) == 0,
        B_at_1over3=ev(B,F(1,3)) == F(16,81),
        D_at_3over5=ev(D,F(3,5)) == -F(64,125),
        first_factor_coefficients=D == [F(1),F(0),F(-18),F(32),F(-15)],
        second_factor_coefficients=DD == [F(0),F(-36),F(96),F(-60)])
    passed = all(r['passed'] for r in checks) and all(identities.values())
    if not passed:
        raise ArithmeticError('A stated strict decimal bound or bump identity failed')
    result = dict(status='Strict R67 bounds compared to exact dyadic endpoints',
        all_checks=True, inequalities=checks, polynomial_identities=identities,
        continuous_polynomial_bounds='Sign and factor arguments are in R67(67.24)-(67.25); checking selected values alone is not their proof.',
        input_hashes={str(a.ledger):hashlib.sha256(a.ledger.read_bytes()).hexdigest()},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        new_Arb_operations=0, new_radial_integrals=0, new_ODE_solves=0,
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='complete', all_checks=True,
        inequalities=len(checks), polynomial_identities=len(identities),
        seconds=result['elapsed_seconds'], peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__ == '__main__':
    main()
