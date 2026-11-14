#!/usr/bin/env python3
"""Exact rational presentation bounds for the executed R70 source functional.

This consumes the completed interval certificate; it does not rerun an ODE,
change a candidate, or replace the original rigorous interval computation.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint(obj):
    return Fraction(int(obj['mantissa'])) * Fraction(2) ** int(obj['binary_exponent'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh exact presentation ledger')
    d = json.loads(args.input.read_text())
    if not d['all_gates'] or d['modes'] != [2, 4] or d['counts']['original_material'] != 5545:
        raise ValueError('The whole executed source certificate is required')
    rows = {row['mode']: row for row in d['rows']}
    checks = []
    specs = {
        2: {
            'signed_canonical_cut_forcing_contribution': ('-9.347006e-57', '1.242606e-56'),
            'absolute_canonical_cut_forcing_upper': ('0', '1.242929e-56'),
            'complete_candidate_centre_residual_canonical_Q': ('9.6530184e-48', '9.6530185e-48'),
            'complete_candidate_centre_residual_axis_ratio_upper': ('1.2118595e11', '1.2118596e11'),
        },
        4: {
            'signed_canonical_cut_forcing_contribution': ('-1.058163e-52', '1.409053e-52'),
            'absolute_canonical_cut_forcing_upper': ('0', '1.409051e-52'),
            'complete_candidate_centre_residual_canonical_Q': ('-1.057652e-52', '1.409564e-52'),
            'complete_candidate_centre_residual_axis_ratio_upper': ('0', '1.415677e7'),
        },
    }
    for m, fields in specs.items():
        for field, (lo, hi) in fields.items():
            rec = rows[m][field]
            passed = Fraction(lo) < endpoint(rec['lower']) <= endpoint(rec['upper']) < Fraction(hi)
            checks.append(dict(mode=m, field=field, strict_decimal_lower=lo,
                               strict_decimal_upper=hi, passed=passed))
            if not passed:
                raise ArithmeticError('A printed strict enclosure failed: '+str((m, field)))
    signs = {
        'mode2_centre_strictly_positive': endpoint(rows[2]['complete_candidate_centre_residual_canonical_Q']['lower']) > 0,
        'mode4_centre_interval_contains_zero': endpoint(rows[4]['complete_candidate_centre_residual_canonical_Q']['lower']) < 0 < endpoint(rows[4]['complete_candidate_centre_residual_canonical_Q']['upper']),
        'no_unknown_outer_nonlinearity_claim': not any(row['unknown_outer_correction_nonlinearity_included'] for row in rows.values()),
        'complete_outer_problem_not_claimed': not d['complete_outer_correction_Green_and_Schur_inverse_paid'] and not d['full46_or_infinite_frequency_outer_problem_paid'],
    }
    if not all(signs.values()):
        raise ArithmeticError('A scope or sign guard failed')
    out = dict(status='Exact rational presentation of the completed cell11 functional',
               checks=checks, signs_and_scope=signs, all_gates=True,
               input_path=str(args.input), input_sha256=sha(args.input),
               source_sha256=sha(Path(__file__)))
    args.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(event='complete', output=str(args.out), all_gates=True,
                          exact_decimal_checks=len(checks), scope_checks=len(signs))))


if __name__ == '__main__':
    main()
