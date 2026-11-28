#!/usr/bin/env python3
"""Exact scalar budget for R91's wider original-support core box.

This uses the exact R53 definition and R87's exact rational window. It does
not recompute a field, certify a binary64 core implementation or relax any
numerical BVP/domain/geometry gate. All certificate arithmetic is Fraction.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def require_positive(value, label):
    if value <= 0:
        raise ArithmeticError(label+' is not positive')
    return str(value)


def main():
    # Machin: tan(4 atan(1/5)-atan(1/239))=1; the angle lies in (0,pi/2).
    x, y = Q(1, 5), Q(1, 239)
    tan2 = 2*x/(1-x*x)
    tan4 = 2*tan2/(1-tan2*tan2)
    if (tan4-y)/(1+tan4*y) != 1:
        raise ArithmeticError('Exact Machin tangent identity failed')
    atan5_lower = sum((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(4))
    pi_lower = 16*atan5_lower-4*y
    pi_gap = require_positive(pi_lower-Q(333, 106), 'Machin lower pi margin')
    # The original degree-nine window: F'=630 t^4(1-t)^4, F(0)=0,F(1)=1.
    polynomial = [Q(v) for v in (0, 0, 0, 0, 0, 126, -420, 540, -315, 70)]
    derivative = [Q(j)*polynomial[j] for j in range(1, len(polynomial))]
    if derivative != [Q(v) for v in (0, 0, 0, 0, 630, -2520, 3780, -2520, 630)]:
        raise ArithmeticError('The exact original window derivative changed')
    if polynomial[0] != 0 or sum(polynomial) != 1:
        raise ArithmeticError('Original window endpoints changed')
    window_integral = sum(c/Q(j+1) for j, c in enumerate(polynomial))
    if window_integral != Q(1, 2):
        raise ArithmeticError('Original window integral changed')
    halfwidth, transition, k = Q(27, 40), Q(3, 10), Q(1, 2)
    J = 2*halfwidth+2*transition*(1-window_integral)
    T_lower = Q(2, 3)*Q(333, 106)
    A = Q(8, 9)
    rho_lower, rho_upper = 1-A, 1+A
    kappa0_lower, kappa0_upper = 1/rho_upper, 1/rho_lower
    beta_upper = (T_lower-k*J)/(T_lower-J)
    curvature_upper = kappa0_upper+beta_upper
    ceiling = Q(123, 10)
    if (J, beta_upper, curvature_upper) != (Q(33, 20), Q(897, 314), Q(3723, 314)):
        raise ArithmeticError('The requested exact compensation constants changed')
    scripts = Path(__file__).resolve().parents[2]
    topic = scripts.parent
    definitions = [topic/'results/R53-material-flattening-homotopy-and-positive-domain.md',
        topic/'results/R87-single-gentle-ramp-half-curvature-held-window.md',
        scripts/'resume_transfer/material_flattened_support_core.py']
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    result = dict(status='proved_exact_scalar_core_budget', source_sha256=sha(Path(__file__)),
        scope='Only the exact R53 core curvature for the R87 rational window and curvature_blend=1; no new field or complete-surface claim',
        source_definitions={str(p): sha(p) for p in definitions},
        rational_parameters=dict(weighted_support_sum_upper=str(A), target_curvature=str(k),
            halfwidth=str(halfwidth), transition=str(transition), window_integral=str(J),
            period_lower_strict=str(T_lower), homotopy_interval=['0', '1']),
        pi_lower_witness=dict(method='Machin identity and four-term alternating lower atan(1/5), upper atan(1/239)<1/239',
            exact_tan_4atan5=str(tan4), lower=str(pi_lower), lower_minus_333_over_106=pi_gap),
        original_window=dict(coefficients=[str(v) for v in polynomial], integral=str(window_integral),
            derivative='630*t^4*(1-t)^4; nonnegative on [0,1]'),
        exact_margins=dict(material_window_fit=require_positive(T_lower/2-halfwidth-transition,'window fit'),
            period_minus_window=require_positive(T_lower-J,'positive compensation denominator'),
            original_curvature_above_target=require_positive(kappa0_lower-k,'positive compensation'),
            core_curvature_ceiling=require_positive(ceiling-curvature_upper,'core curvature margin')),
        exact_conclusions=dict(original_rho_interval=[str(rho_lower),str(rho_upper)],
            original_curvature_interval=[str(kappa0_lower),str(kappa0_upper)],
            compensation_lower='0', compensation_upper_strict=str(beta_upper),
            full_homotopy_curvature_lower=str(k), full_homotopy_curvature_upper_strict=str(curvature_upper),
            old_support_sum_gate='2/3', enlarged_support_sum_gate=str(A)),
        actual_field_recomputed=False, binary64_quadrature_core_certified=False,
        BVP_gates_changed=False, true_tail_or_fixed_g_refinement=False,
        full_surface_geometry_or_held_completed=False)
    print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))


if __name__ == '__main__':
    main()
