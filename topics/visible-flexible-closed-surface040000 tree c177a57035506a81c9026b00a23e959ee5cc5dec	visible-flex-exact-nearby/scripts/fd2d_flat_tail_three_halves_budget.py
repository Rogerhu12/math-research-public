#!/usr/bin/env python3
"""R177: exact rational geometry budget for 0 <= P <= 3/2.

This evaluates proven scalar inequalities only. It does not change a tail
provider, parameter-domain guard, solver state, cap or physical candidate.
The old R168 cap inequalities are reused with their actual source binding;
all new tail inequalities are evaluated with exact Fraction arithmetic.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import time

import fd2d_smaller_corner_caps as caps


UPPER = Q(3, 2)
CUFF = Q(8, 25)
FLAT = Q(17, 50)
CUT = Q(4, 5)
WIDTH = CUT - FLAT
CURVATURE = Q(630, 256) * UPPER / WIDTH
NORMAL_RADIUS = 1 / CURVATURE
DEPRESSION = UPPER * WIDTH / 2
NEW_ZMIN = {'D4': Q(197, 200), 'D375': Q(461, 500)}


def record(value):
    value = Q(value)
    return {'exact': str(value), 'approximate': float(value)}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def variant_budget(name):
    old = caps.budget(name)
    v = caps.VARIANTS[name]
    D, R, Zmax = (v[k] for k in ('D', 'R', 'Zmax'))
    A = caps.COMMON['A']
    slab = caps.COMMON['slab']
    sphere = D / 2
    held = D / 5
    Zmin = NEW_ZMIN[name]
    support_lower = min(Zmin, FLAT * Q(99, 100) + Zmin * Q(7, 100))
    cap_margins = {
        k: Q(item['exact']) for k, item in old['exact_margins'].items()
        if not k.startswith('tail_')
    }
    new_margins = {
        'tail_radius_above_required_global_core_radius': NORMAL_RADIUS - R,
        'tail_curvature_below_local_cap': 1 / R - CURVATURE,
        'whole_tail_held_squared': (A - CUT)**2 + (Zmin - DEPRESSION)**2 - held**2,
        'tail_actual_Z_above_cap_minimum': Zmin - held,
        'tail_actual_Z_window_width': Zmax - Zmin,
        'opposite_tail_separation_beyond_twice_R': 2 * (Zmin - DEPRESSION) - 2 * R,
        'whole_tail_origin_ball_squared': sphere**2 - CUT**2 - Zmax**2,
        'whole_tail_phase_zero_slab': slab - CUT,
        'whole_tail_support_above_two_fifths': support_lower - Q(2, 5),
    }
    for key, value in cap_margins.items():
        assert value > 0, (name, key, str(value))
    for key, value in new_margins.items():
        assert value >= 0 if key == 'whole_tail_held_squared' else value > 0, (name, key, str(value))
    assert held <= Zmin <= Zmax < Q(old['values']['reference_Z_lower']['exact'])
    values = {
        'diameter_upper': D,
        'whole_core_origin_ball_radius': sphere,
        'held_radius': held,
        'required_whole_core_reach': R,
        'central_axis_support_lower': A,
        'active_halfwidth': slab,
        'actual_Z_lower': Zmin,
        'actual_Z_upper': Zmax,
        'tail_z_lower': Zmin - DEPRESSION,
        'tail_support_lower': support_lower,
        'held_ratio_lower': held / D,
        'quotient_ratio_lower': Q(old['values']['quotient_ratio_lower']['exact']),
        'reach_ratio_lower': R / D,
        'optional_before_column_deletion_Z_lower_Delta_7_over_50': Zmin + Q(7, 50),
        'optional_before_column_deletion_Z_upper_Delta_7_over_50': Zmax + Q(7, 50),
    }
    return {
        'variant': name,
        'cap_definition_unchanged_from': 'R168',
        'cap_construction': old['definition'],
        'values': {k: record(x) for k, x in values.items()},
        'retained_cap_rational_margins': {k: record(x) for k, x in cap_margins.items()},
        'new_tail_rational_margins': {k: record(x) for k, x in new_margins.items()},
        'all_required_rational_comparisons_passed': True,
        'remaining_actual_core_conditions': old['remaining_actual_conditions'],
        'column_deletion_warning': 'Only actual Z is shifted; central gap is unchanged, and opposite-half normal balls and the whole-core held ball must still be paid.',
        'actual_core_solved': False,
        'strong_target_completed': False,
    }


def make_report():
    # Alternating Taylor lower polynomials at x = 3/2; omitted tails have
    # positive sign and decreasing terms. Their proof is in R177.
    x = UPPER
    sin_lower = x - x**3 / 6 + x**5 / 120 - x**7 / 5040
    cos_lower = 1 - x**2 / 2 + x**4 / 24 - x**6 / 720
    weight_integral = Q(630 * factorial(4)**2, factorial(9))
    smoothstep_integral = Q(126, 6) - Q(420, 7) + Q(540, 8) - Q(315, 9) + Q(70, 10)
    assert weight_integral == 1
    assert smoothstep_integral == Q(1, 2)
    assert sin_lower > Q(99, 100)
    assert cos_lower > Q(7, 100)
    assert CURVATURE == Q(23625, 2944)
    assert NORMAL_RADIUS == Q(2944, 23625)
    assert DEPRESSION == Q(69, 200)
    assert NORMAL_RADIUS < Q(17, 125)  # old .136 radius is not reused
    proof_dir = Path(__file__).resolve().parent.parent / 'results'
    names = [
        'R130-global-normal-balls-for-the-exact-flat-tail.md',
        'R132-positive-bernstein-controls-for-the-exact-flat-tail.md',
        'R168-smaller-corner-caps-and-shorter-cylinder-window.md',
        'R170-dyadic-Bernstein-box-for-the-same-flat-tail.md',
    ]
    return {
        'schema': 'fd2d-R177-three-halves-tail-exact-geometry-budget-v1',
        'theorem': 'R177',
        'source_sha256': digest(__file__),
        'cap_budget_source_sha256': digest(caps.__file__),
        'proof_dependencies': [{'path': 'results/' + name, 'sha256': digest(proof_dir / name)} for name in names],
        'definition': {
            'same_tail_function_as': 'R132/R170',
            'function_domain': '0 <= P(q) <= 3/2 for every q in [0,1]',
            'sufficient_degree15_domain': '0 <= S b <= 3/2, with the unchanged exact eight-cell R170 subdivision matrix S',
            'global_coefficients_may_be_negative': True,
            'new_software_domain_installed': False,
        },
        'values': {k: record(v) for k, v in {
            'function_upper': UPPER,
            'cuff_radius': CUFF,
            'flat_collar_radius': FLAT,
            'cut_radius': CUT,
            'bending_width': WIDTH,
            'curvature_upper': CURVATURE,
            'complete_cylinder_reach_lower': NORMAL_RADIUS,
            'total_turn_upper': 2 * UPPER,
            'depression_upper': DEPRESSION,
            'sin_three_halves_taylor_lower': sin_lower,
            'cos_three_halves_taylor_lower': cos_lower,
            'normalized_curvature_weight_integral': weight_integral,
            'S9_integral': smoothstep_integral,
            'strict_domain_extension_constant_witness': Q(13, 10),
        }.items()},
        'old_R130_uniform_radius_point136_available': False,
        'normal_ball_scope': 'Complete boundaryless generalized cylinder; inherited surface-normal pairs on the tail and same-side flat disk. Not arbitrary finite-patch boundary reach.',
        'variants': [variant_budget(name) for name in ('D4', 'D375')],
        'all_arithmetic_certificates_rational': True,
        'proof_of_total_turn_less_than_pi': '2B = 3 < pi',
        'body_or_BVP_runs': 0,
        'solver_or_saved_field_mutations': 0,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new exact-budget report path')
    start = time.perf_counter()
    report = make_report()
    report['elapsed_seconds'] = time.perf_counter() - start
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({
        'report': str(args.out), 'passed': True,
        'curvature_upper': float(CURVATURE), 'normal_radius_lower': float(NORMAL_RADIUS),
        'variants': {v['variant']: {k: v['values'][k]['exact'] for k in
            ('actual_Z_lower', 'actual_Z_upper', 'held_ratio_lower', 'quotient_ratio_lower', 'reach_ratio_lower')}
            for v in report['variants']},
        'elapsed_seconds': report['elapsed_seconds'],
    }), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
