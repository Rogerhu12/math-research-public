#!/usr/bin/env python3
"""Exact finite-core bounds for the actually accepted 96-mode BVP core.

All numerical coefficients are interpreted as their exact binary64 rationals.
This certifies only the planar core, not the continued or closed surface.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path

from root_20261114_scaled_core import r225_coefficients, interval


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    raw = args.accepted.read_bytes()
    data = json.loads(gzip.decompress(raw))
    assert data['success'] is True and data['M'] == 96
    base = [Q(6, 5) * x for x in r225_coefficients()]
    assert [Q(x) for x in data['original_metric_identity']['coefficients_rational']] == base
    exact = [Q(x) for x in data['solved_metric_definition']['core_coefficients_binary64_exact_rational']]
    assert exact == [Q(x) for x in data['core']['coefficients']]
    assert len(exact) == 96
    assert exact[:32] == [Q(float(x)) for x in base]
    delta = [x - (base[n - 1] if n <= 32 else 0) for n, x in enumerate(exact, 1)]
    e0 = sum(abs(x) for x in delta)
    e1 = sum(2*n*abs(x) for n, x in enumerate(delta, 1))
    erho = sum((4*n*n-1)*abs(x) for n, x in enumerate(delta, 1))
    earc = sum(Q(4*n*n-1, 2*n)*abs(x) for n, x in enumerate(delta, 1))
    hplus = 1 + sum(base)
    hminus = 1 + sum((-1)**n*x for n, x in enumerate(base, 1))
    rminus = 1 + sum((1-4*n*n)*x for n, x in enumerate(base, 1))
    rplus = 1 + sum((-1)**n*(1-4*n*n)*x for n, x in enumerate(base, 1))
    gap = 2*sum(x for n, x in enumerate(exact, 1) if n % 2)
    axis_major = 1 + sum(exact)
    axis_minor = 1 + sum((-1)**n*x for n, x in enumerate(exact, 1))
    assert gap == axis_major - axis_minor and gap > 0
    rho_lower = rminus - erho
    rho_upper = rplus + erho
    assert rho_lower > 0 and hminus - e0 > 0
    k0 = Q(float(data['solved_metric_definition']['scalar_initial_law']['k0']))
    ratio = erho/rminus
    bounds = dict(
        coefficient_L1=e0,
        support_derivative_L1=e1,
        curve_displacement_upper=e0+e1,
        rho_change_upper=erho,
        material_arc_change_upper=earc,
        support_positive_lower=hminus-e0,
        rho_positive_lower=rho_lower,
        rho_upper=rho_upper,
        axis_major_support=axis_major,
        axis_minor_support=axis_minor,
        exact_axis_witness_distance=gap,
        core_diameter_upper=2*(hplus+e0),
        core_rotated_Hausdorff_upper=hplus-hminus+2*e0,
        conditional_inlet_curvature_upper=max(1/rho_lower, k0*rho_upper),
        old_normal_angle_metric_relative_upper=2*ratio+ratio*ratio,
    )
    checks = {
        'all_96_binary64_rationals_match_output': True,
        'first_32_are_exact_roundings_of_R236': True,
        'rho_positive_for_all_angles': rho_lower > 0,
        'support_positive_for_all_angles': hminus-e0 > 0,
        'witness_distance_above_0_95999999': gap > Q('0.95999999'),
        'core_diameter_below_2_828235153': bounds['core_diameter_upper'] < Q('2.828235153'),
        'conditional_inlet_curvature_below_6_0199': bounds['conditional_inlet_curvature_upper'] < Q('6.0199'),
    }
    assert all(checks.values())
    enclosures = {k: interval(v) for k, v in bounds.items()}
    assert all(Q(enclosures[k][0]) < v < Q(enclosures[k][1]) for k, v in bounds.items())
    result = dict(
        scope=__doc__,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        base_source_sha256=hashlib.sha256(Path(__file__).with_name('root_20261114_scaled_core.py').read_bytes()).hexdigest(),
        accepted_sha256=hashlib.sha256(raw).hexdigest(),
        coefficients_exact=[str(x) for x in exact],
        differences_from_R236_exact=[str(x) for x in delta],
        exact={k: str(v) for k, v in bounds.items()},
        strict_decimal_enclosures=enclosures,
        checks=checks,
        closed_surface_certified=False,
        continued_prefix_ball_exclusion_certified=False,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(enclosures=result['strict_decimal_enclosures'], checks=checks), indent=2))


if __name__ == '__main__':
    main()
