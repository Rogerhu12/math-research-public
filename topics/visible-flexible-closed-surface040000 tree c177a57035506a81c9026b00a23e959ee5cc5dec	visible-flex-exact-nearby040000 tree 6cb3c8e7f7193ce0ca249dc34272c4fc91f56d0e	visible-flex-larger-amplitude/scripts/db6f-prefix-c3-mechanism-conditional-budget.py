#!/usr/bin/env python3
"""Exact scalar budgets for a conditional C3 core/transition interface.

No curve, prefix, angular root, RK flow, optimizer or geometry backend is run.
The convex-hull enclosure is a hypothesis on a future whole map, not a map.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parent.parent
NOTES = TOPIC / 'notes'
FINITE = NOTES / '2026-11-09-db6f-prefix-c3-finite-bounds.json'
FINITE_SHA = '2d5e300efe5f7fd33756235ee59e9c64466c5c0b0c441327f9248a8cb5c532fa'
OLD = NOTES / '2026-11-09-db6f-root-closed-budget-m12-critical-r01.json'
OLD_SHA = '50410a4e57b8a21937dd3a99c25942b36cebd5c5819f1e10982584412ae601a7'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def frac(record):
    return Q(record['numerator']) / Q(record['denominator'])


def exact(value):
    return {'numerator': str(value.numerator),
            'denominator': str(value.denominator),
            'display_only': float(value)}


def item(path):
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': sha(path)}


def calculate():
    assert sha(FINITE) == FINITE_SHA
    assert sha(OLD) == OLD_SHA
    cases = json.loads(FINITE.read_text())['cases']
    case, = [x for x in cases if x['Fejer_order'] == 7 and frac(x['r']) == Q(3, 20)]
    r = frac(case['r'])
    delta = frac(case['delta']['lower'])
    diameter = frac(case['diameter_upper']['upper'])
    assert delta < frac(case['delta_exact'])
    assert diameter > frac(case['diameter_upper_exact'])
    b1 = frac(case['positive_fourier_b'][0])
    q1 = (1-r)*b1/4
    rho_max = frac(case['rho_max_exact'])
    # Published rounded endpoints are used in every enclosure comparison.
    eta, band, cap_radius, cap_height = Q(1, 1000), Q(1, 10), Q(3, 10), Q(11, 10)
    radius, inradius = (3-r)/2, (1+r)/2
    whole_D = Q(23, 10)
    central_pair = (diameter+2*eta)**2 + (2*band)**2
    cap_pair = 4*(cap_radius**2+cap_height**2)
    cross_pair = (radius+eta+cap_radius)**2 + (cap_height+band)**2
    held = delta-eta
    old_height = Q(json.loads(OLD.read_text())['held_region_diameter_lower']['exact'])
    margins = {
        'cap_disk_inside_core': inradius-cap_radius,
        'central_pairs_below_cap_pair': cap_pair-central_pair,
        'cross_pairs_below_cap_pair': cap_pair-cross_pair,
        'whole_D_squared': whole_D**2-cap_pair,
        'held_above_one_fifth_whole_D': held-whole_D/5,
        'core_rho_above_three_percent_whole_D_only': r-3*whole_D/100,
        'old_actual_axis_separation_exceeds_new_total_height': old_height-2*cap_height,
        'first_support_coefficient_exceeds_current_guard_literal': q1-Q(31, 250),
        'naive_chart_warp_e_exceeds_one': 8*q1-1,
    }
    assert all(v > 0 for v in margins.values())
    assert q1 == Q(357, 1720) and rho_max == Q(8833, 860)
    assert cap_pair == Q(26, 5)
    return {
        'status': 'CONDITIONAL_POSITION_BUDGET_AND_STATIC_INPUT_LIMITS_ONLY',
        'source_bindings': [item(FINITE), item(OLD), item(Path(__file__).resolve())],
        'core': {'Fejer_order': 7, 'C3_support_modes': 14, 'rho_min': exact(r),
                 'rho_max': exact(rho_max), 'minimum_curvature': exact(1/rho_max),
                 'rotated_first_support_coefficient': exact(q1),
                 'support_gap_published_lower': exact(delta),
                 'diameter_published_upper': exact(diameter),
                 'centered_radius_upper': exact(radius),
                 'centered_inradius_lower': exact(inradius)},
        'enclosure_parameters': {'projection_leakage': exact(eta),
                                 'central_half_height': exact(band),
                                 'end_disk_radius': exact(cap_radius),
                                 'end_half_height': exact(cap_height)},
        'pair_distance_squared_upper': {'central_central': exact(central_pair),
                                       'disk_disk': exact(cap_pair),
                                       'central_disk': exact(cross_pair)},
        'conditional_whole_D_squared_upper': exact(cap_pair),
        'conditional_whole_D_clean_upper': exact(whole_D),
        'conditional_held_lower': exact(held),
        'old_M12_actual_fixed_axis_separation_lower': exact(old_height),
        'strict_rational_margins': {k: exact(v) for k, v in margins.items()},
        'all_strict_rational_comparisons_passed': True,
        'solver_root_RK_geometry_backend_calls': 0,
        'same_as_current_frozen_g_claimed': False,
        'enclosure_realized_by_an_ODE_solution': False,
        'whole_reach_or_closed_flex_asserted': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = calculate()
    raw = (json.dumps(report, indent=2, allow_nan=False)+'\n').encode()
    assert len(raw) < 100_000
    with args.out.open('xb') as handle:
        handle.write(raw)
    args.out.chmod(0o444)
    print(json.dumps({'status': report['status'], 'all_checks_passed': True,
                      'solver_calls': 0, 'output_bytes': len(raw),
                      'output_sha256': sha(args.out)}))


if __name__ == '__main__':
    main()
