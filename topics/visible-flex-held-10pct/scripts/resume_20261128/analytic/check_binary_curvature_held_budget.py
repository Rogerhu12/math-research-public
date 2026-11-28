#!/usr/bin/env python3
"""Exact R54/R67 conditional budgets for the actual binary64 target curvature.

Only rational arithmetic is used. This pays a parameter-definition rounding
interface; it neither supplies a lambda-one field nor runs a BVP, tail, mesh,
or continuous geometric certificate. Existing R54 formulas are inputs.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[2]


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def row(value):
    value = Q(value)
    return dict(exact=str(value), display_only=float(value))


def check():
    k, S, width, phase = Q.from_float(.2), Q(1, 2), Q(27, 50), Q(9, 20)
    sqrt3_lo, sqrt3_hi = Q(433, 250), Q(7, 4)
    pi_lo, pi_hi = Q(3), Q(22, 7)
    assert sqrt3_lo**2 < 3 < sqrt3_hi**2
    assert k-Q(1, 5) == Q(1, 90071992547409920)
    assert 0 < k < 1 and k != Q(1, 5)
    x, y = k*width/2, k*phase/2
    assert 0 < x < 1 and 0 < y < 1
    sinx_lo, siny_lo = x-x**3/6, y-y**3/6
    assert sinx_lo > 0 and siny_lo > 0
    O_lo = 1/k-2*pi_hi/(3*sqrt3_lo)
    held_coefficient_lo = sqrt3_lo/k-2*pi_hi/3
    assert O_lo > 0 and held_coefficient_lo > 0
    chord_lo = (2/k)*sinx_lo
    held_lo = held_coefficient_lo*siny_lo
    chord_threshold, held_threshold = Q(5397, 10000), Q(2953, 10000)
    assert chord_lo > chord_threshold and held_lo > held_threshold
    D, reach = Q(67251, 25000), Q(10, 123)
    ratios = dict(H_diameter=chord_threshold/D, held=held_threshold/D, reach=reach/D)
    required = dict(H_diameter=Q(1, 5), held=Q(1, 10), reach=Q(3, 100))
    assert all(ratios[name] > required[name] for name in ratios)
    left, right = -Q(9, 200)-phase, Q(99, 200)
    assert left == -Q(99, 200) and right == Q(99, 200)
    assert S+left == S-right == Q(1, 200)
    sources = [TOPIC/'results/R54-transverse-held-arc-and-short-cylinder-window.md',
        TOPIC/'results/R67-universal-threefold-marker-and-euclidean-noncongruence.md',
        TOPIC/'notes/2026-11-20-m24-r53-true-core-jet-certificate.md']
    return dict(status='conditional_binary_curvature_R54_R67_rational_budgets_verified',
        source=ref(__file__), formula_sources=[ref(path) for path in sources],
        scope='Existing R54 chord/held formulas and conditional R67 diameter/reach budgets; no new surface or lambda-one solution',
        existing_result_reproved=False, only_parameter_definition_rounding_paid=True,
        lambda_one_field_available_or_constructed=False, nonlinear_solve_executed=False,
        new_continuous_metric_or_geometry_certificate=False, completion_criteria_passed=False,
        k=row(k), decimal_one_fifth=row(Q(1, 5)), k_minus_one_fifth=row(k-Q(1, 5)),
        target_curvature_is_exact_literal_binary_not_one_fifth=True,
        material_halfwidth=row(S), held_material_width=row(width), phase_endpoint=row(phase),
        pi_enclosure=dict(lower=str(pi_lo), upper=str(pi_hi),
            both_strict=True, source='Classical rational bounds already used in R54'),
        sqrt3_enclosure=dict(lower=str(sqrt3_lo), upper=str(sqrt3_hi),
            both_strict=True, lower_square=str(sqrt3_lo**2), upper_square=str(sqrt3_hi**2)),
        sine_bound='For 0<x<1, x-x^3/6 < sin(x) < x; no numerical trigonometric calls',
        chord_argument=row(x), chord_sine_lower=row(sinx_lo), chord_sine_upper=row(x),
        held_argument=row(y), held_sine_lower=row(siny_lo), held_sine_upper=row(y),
        arc_center_absolute_lower=row(O_lo), held_positive_coefficient_lower=row(held_coefficient_lo),
        H_diameter_strict_lower=row(chord_lo), held_strict_lower=row(held_lo),
        H_diameter_threshold=row(chord_threshold), held_threshold=row(held_threshold),
        H_diameter_strict_margin=row(chord_lo-chord_threshold),
        held_strict_margin=row(held_lo-held_threshold),
        assumed_complete_initial_diameter_upper=row(D),
        assumed_complete_all_time_reach_lower=row(reach),
        ratio_lower={name:row(value) for name,value in ratios.items()},
        ratio_strict_margins={name:row(ratios[name]-required[name]) for name in ratios},
        protected_material_swept_interval_relative_center=[str(left), str(right)],
        protected_material_margin_each_end=str(Q(1, 200)),
        noncircular_core_reason='A positive-curvature unit-speed circle of perimeter 2*pi has curvature 1; the actual protected arc has k != 1',
        noncircular_core_statement_conditional_on_actual_lambda_one_core=True,
        exact_held_frame='R_(-(1-k)*alpha) G_alpha + O - R_(k*alpha) O, with this exact binary k and the true arc center',
        finite_cap_amplitude_and_cylinder_costs_not_recertified=True,
        pending_actual_obligations=['lambda-one original complete field', 'true nonlinear full-height tail and shared Cartesian two-jets',
            'complete D/support/curvature/reach hypotheses at every time', 'same-problem refinement'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    record = check()
    with args.out.open('x') as stream:
        stream.write(json.dumps(record, indent=2, allow_nan=False)+'\n')
    print(json.dumps({name:record[name] for name in ('status','k','H_diameter_strict_lower','held_strict_lower','ratio_lower')}, indent=2))


if __name__ == '__main__':
    main()
