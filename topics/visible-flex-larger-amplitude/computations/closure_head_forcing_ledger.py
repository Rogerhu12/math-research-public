#!/usr/bin/env python3
"""Exact constants for R23's complete nonlinear warped-head source budget.

No ODE or approximate source integral is evaluated. The cell norms below are
required whole-cell hypotheses, not inferred from small saved endpoints.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def two(n):
    return Q(2**n) if n >= 0 else Q(1, 2**(-n))


def floor_q(x):
    return x.numerator // x.denominator


def ceil_q(x):
    return -((-x.numerator) // x.denominator)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', required=True, type=Path)
    args = p.parse_args()
    d0 = Q(3458764513820541, 576460752303423488)
    rc = Q(900719925474099, 18014398509481984)
    eps_phys = Q(3821273729050667, 295147905179352825856)
    eps = eps_phys / rc**7
    rstar = two(-16)
    ratio = Q(257, 256)
    checks = {}
    checks['d0_dyadic_bracket'] = two(-8) < d0 < two(-7)
    checks['radius_bracket'] = Q(3, 64) < rc < two(-4)
    checks['epsilon_normalized_bracket'] = two(14) < eps < two(15)
    checks['mean_cauchy_domain'] = 2*rstar < Q(1, 10000)
    checks['mean_full_field_inflation'] = rstar+40*rstar**2 < 2*rstar
    checks['mean_derivative_inflation'] = 1+160*rstar < 2
    checks['leading_inverse_radius'] = 4*rstar < Q(1, 2)
    checks['positive_D_majorant'] = 5*two(-40) < two(-37)
    checks['source_numerator_constant'] = 4+6*two(-24) < 8
    checks['source_numerator_difference_constant'] = 4+8*two(-24) < 8
    checks['source_lipschitz_constant'] = 16+128*rstar < 32
    for power in (3, 7, 10, 13):
        checks[f'radius_ratio_power_{power}_below2'] = ratio**power < 2
    checks['relative_norm_coefficient'] = 16+64 <= 2**7
    checks['relative_ball_exponents'] = two(7)*two(-23) == rstar
    checks['quadratic_source_prefactor'] = 512**2 < 12*256**2
    checks['cell12_delta_bound'] = d0*two(-12) < two(-19)
    checks['profile_log_variation_at12'] = 5*(12+9) < 2**38
    checks['profile_log_variation_induction'] = Q(22, 21) < 4
    checks['profile_weighted_log_variation'] = 4+1 <= 5
    checks['source_radius_log_term'] = 35*two(-19) < Q(1, 256)
    checks['material_integral_constant'] = 6+Q(6, 256) < 8
    checks['mean_point_constant'] = 10*2**12 < 2**16
    checks['mean_height_constant'] = Q(10*2**12, 256) < 2**8
    rows = []
    for n in (12, 16, 24, 32, 48, 64, 128, 159, 160, 192, 224):
        delta = d0*two(-n)
        radius_exp = floor_q(-Q(19*n, 4)-35)
        source_exp = ceil_q(Q(19*n, 4)+24)
        mean_exp = ceil_q(Q(23*n, 4)+12)
        mean_point_exp = ceil_q(Q(23*n, 4)+24)
        # Fourth powers pay all fractional exponents without transcendental
        # approximation. All bases are positive exact rationals.
        radius4 = two(-92)*eps**4*rc**(-12)*delta**19
        source4 = two(48)*rc**12*eps**(-4)*delta**(-19)
        mean4 = two(32)*rc**28*eps**(-4)*delta**(-23)
        mean_point4 = two(64)*rc**24*eps**(-4)*delta**(-23)
        paid = dict(
            guaranteed_radius=two(4*radius_exp) < radius4,
            source_coefficient=source4 < two(4*source_exp),
            mean_height_coefficient=mean4 < two(4*mean_exp),
            mean_slope_coefficient=mean_point4 < two(4*mean_point_exp),
        )
        checks[f'cell_{n}_dyadic_bounds'] = all(paid.values())
        rows.append(dict(cell=n, delta_exact=str(delta),
            guaranteed_input_radius_log2=radius_exp,
            source_integral_coefficient_log2_upper=source_exp,
            source_lipschitz_coefficient_log2_upper=source_exp+1,
            mean_height_coefficient_log2_upper=mean_exp,
            mean_slope_point_coefficient_log2_upper=mean_point_exp,
            comparison_method='Exact rational comparison after fourth powers',
            checks=paid))
    checks['cell12_example_is_inside_ball'] = two(-140) < two(-92)
    checks['cell12_example_source_exponent'] = 81-2*140 == -199
    if not all(checks.values()):
        raise AssertionError([k for k, v in checks.items() if not v])
    inputs = {}
    for f in (Path('results/R17-explicit-rational-tail-nonlinear-depth.md'),
              Path('results/R22-wide-strip-linear-head-envelope.md'),
              Path('results/R23-warped-head-complete-nonlinear-source-budget.md')):
        if f.exists():
            inputs[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
    out = dict(
        status='Exact constants for a conditional full-Fourier nonlinear SOURCE theorem; no head solution is certified',
        checks=checks, check_count=len(checks),
        parameters=dict(d0_exact=str(d0), radius_exact=str(rc),
            epsilon_physical_exact=str(eps_phys), epsilon_normalized_exact=str(eps)),
        norm='Sum over modes of weighted whole-cell suprema: Q has three angular derivatives and canonical Xi has one',
        relative_ball_radius_exact=str(rstar),
        material_integral_coefficient_upper=8,
        dyadic_cell_bounds=rows,
        example=dict(cell=12, status='CONDITIONAL budget only; whole-cell norm is not measured',
            required_whole_cell_X_log2_upper=-140,
            source_integral_log2_upper=-199,
            mean_height_increment_log2_upper=-199),
        input_hashes=inputs,
        entrypoint_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        hypotheses=[
            'R22 real-source assumptions, including every finite alpha_n in [1/2,2].',
            'Complete angular mean root, not a finite-grid mean substituted without an error bound.',
            'Canonical Xi, not nonlinear connection momentum Pi.',
            'The whole-cell strong norm lies in the stated radius, not just one or two endpoint values.',
        ],
        limits=[
            'The output norm is L1 in physical radius with an angular Wiener norm.',
            'A compatible full-frequency linear or linearized Green bound is separately needed for a correction theorem.',
            'Finite Galerkin compressed inverses are not replaced by pointwise inverses.',
            'Floating radial integration, source quadrature, finite-angle root errors and shallow prefix absorption of high modes remain separate.',
        ],
    )
    args.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out), checks=len(checks),
        relative_ball=str(rstar), cell12=rows[0], example=out['example'])))


if __name__ == '__main__':
    main()
