#!/usr/bin/env python3
"""R113 exact geometric budget for a new elliptic central core.

This checks a complete fixed-cap geometry and conditional global inequalities.
It does not solve the nonlinear common-g active core or certify a sampled mesh.
The central ellipse is exact; its mean radius and optional Fourier coefficients
are numerical readings, never substituted for the exact ellipse in the proof.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad

A, B = Q(7, 5), Q(9, 20)
R = Q(17, 125)
LAM = Q(1, 100)
A_NECK, A_CUFF = Q(3, 10), Q(8, 25)
EPS, DELTA = Q(1, 10000), Q(1, 1000000)
A_BASE = Q(11, 25) + 2 * DELTA
MARK_B, MARK_H, MARK_TOP = Q(137, 100), Q(17, 10), Q(2249, 1000)
BALL = Q(9, 4)
HALFWIDTH = Q(3, 4)


def ratio(value: Q) -> dict:
    return dict(fraction=str(value), float=float(value))


def ellipse_support(phi):
    """Return exact-form support h, h_phi, and curvature radius rho."""
    phi = np.asarray(phi)
    c, s = np.cos(phi), np.sin(phi)
    aa, bb = float(A), float(B)
    h = np.sqrt(aa * aa * c * c + bb * bb * s * s)
    hp = (bb * bb - aa * aa) * c * s / h
    rho = aa * aa * bb * bb / h**3
    return h, hp, rho


def ellipse_curve(phi):
    h, hp, _ = ellipse_support(phi)
    phi = np.asarray(phi)
    return np.stack((h * np.cos(phi) - hp * np.sin(phi),
                     h * np.sin(phi) + hp * np.cos(phi)), axis=-1)


def summary() -> dict:
    gap = A - B
    side_seed = MARK_B - R
    r2 = A * A * MARK_B * MARK_B / (A * A + MARK_B * MARK_B)
    r_lower = Q(979, 1000)
    neck_min = A_NECK - R * (1 + 2 * LAM)
    bounds = dict(
        core_minimum_curve_radius=B * B / A,
        core_axis_gap=gap,
        maximum_whole_diameter=2 * BALL,
        neck_minimum_radius=neck_min,
        collar_width=A_CUFF - A_NECK,
        base_flat_disk_margin=A_BASE - DELTA - A_NECK - R,
        side_ball_squared_margin=(BALL - R - EPS)**2 - side_seed**2 - MARK_H**2,
        square_ball_squared_margin=(BALL - R - EPS)**2 - 2 * A_BASE**2 - MARK_H**2,
        top_ball_margin=BALL - MARK_TOP - EPS,
        body_bottom_height=MARK_H - EPS - R,
        fixed_cap_x_halfwidth_upper=A_BASE + R + EPS,
        polygon_inradius_condition=MARK_TOP**2 - (MARK_TOP - MARK_H)**2 - MARK_B**2,
        ideal_marker_inradius_squared=r2,
        ideal_marker_inradius_lower_margin=r2 - r_lower**2,
        marker_position_error=EPS,
        grip_diameter_lower=2 * MARK_TOP - 2 * EPS,
        cuff_height_strict_lower=MARK_H - EPS - 3 * R - R * LAM * Q(22, 7),
        cuff_height_strict_upper=MARK_H - EPS - 3 * R - 2 * R * LAM,
        held_over_D_lower_if_active_input=gap / (2 * BALL),
        deltaE_over_D_strict_lower_if_active_input=(r_lower - EPS - HALFWIDTH) / (2 * BALL),
        reach_over_D_lower_if_active_input=R / (2 * BALL),
    )
    assert neck_min > R and A_NECK < A_CUFF
    assert B * B / A > R
    for key in ('base_flat_disk_margin', 'side_ball_squared_margin',
                'square_ball_squared_margin', 'top_ball_margin',
                'polygon_inradius_condition', 'ideal_marker_inradius_lower_margin'):
        assert bounds[key] > 0
    assert bounds['fixed_cap_x_halfwidth_upper'] < HALFWIDTH
    assert bounds['cuff_height_strict_lower'] > gap
    assert bounds['held_over_D_lower_if_active_input'] >= Q(1, 5)
    assert bounds['deltaE_over_D_strict_lower_if_active_input'] > Q(1, 20)
    assert bounds['reach_over_D_lower_if_active_input'] > Q(3, 100)
    integral, integral_error = quad(lambda t: math.sqrt(max(0., math.sin(t))),
                                    0., math.pi, epsabs=2e-14, epsrel=2e-14)
    h = lambda t: math.hypot(float(A) * math.cos(t), float(B) * math.sin(t))
    mean, mean_error = quad(h, 0., 2 * math.pi, epsabs=1e-13, epsrel=1e-13)
    mean /= 2 * math.pi
    coeffs = []
    for j in range(1, 9):
        value, error = quad(lambda t: h(t) * math.cos(2 * j * t),
                            0., 2 * math.pi, epsabs=1e-13, epsrel=1e-13)
        coeffs.append(dict(mode=2 * j, normalized_support_coefficient=value / math.pi / mean,
                           quadrature_reported_error=error / math.pi / mean))
    return dict(
        theorem='R113',
        variant='curvature-margin' if B == Q(1, 2) else 'original',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        status='proved_fixed_caps_and_conditional_global_grafting',
        nonlinear_active_core_solved=False,
        complete_problem_solution=False,
        parameters={k: ratio(v) for k, v in dict(
            ellipse_long_semiaxis=A, ellipse_short_semiaxis=B, R=R, neck_lambda=LAM,
            neck_radius=A_NECK, cuff_radius=A_CUFF, epsilon=EPS,
            mollifier_radius=DELTA, base_square_halfwidth=A_BASE,
            side_marker_radius=MARK_B, side_marker_height=MARK_H,
            top_marker_height=MARK_TOP, whole_ball_radius=BALL,
            active_halfwidth=HALFWIDTH).items()},
        exact_bounds={k: ratio(v) for k, v in bounds.items()},
        numerical_readings_not_certificates=dict(
            neck_integral=integral, integral_error=integral_error,
            cuff_height=float(MARK_H - EPS - 3 * R) - float(R * LAM) * integral,
            core_metric_a0=mean, mean_radius_quadrature_error=mean_error / (2 * math.pi),
            ideal_marker_inradius=math.sqrt(float(r2)),
            normalized_support_coefficients=coeffs),
        missing_inputs=[
            'actual common-g elliptic or controlled-nearby active core',
            'actual all-phase reach >= .136 before grafting',
            'whole active ball, height, halfwidth, and held protection inequalities',
            'new physical tail nonlinear matching and complete collar closure'],
    )


def main():
    global B
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--variant', choices=('original', 'curvature-margin'), default='original')
    args = parser.parse_args()
    if args.variant == 'curvature-margin':
        B = Q(1, 2)
    report = summary()
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(theorem=report['theorem'],
        status=report['status'],
        cuff_height=report['numerical_readings_not_certificates']['cuff_height'],
        ratios={k: v for k, v in report['exact_bounds'].items() if '_over_D_' in k})))


if __name__ == '__main__':
    main()
