#!/usr/bin/env python3
"""Exact formulas for the high material jets of a frozen cosine flat core.

The physical identity and material inversion are supplied by the unchanged
cosine_rectifying_core module.  This module adds Cartesian gamma^(5), scalar
Frenet derivatives, and the complete two-jets of T and B at fixed material
coordinates (s, theta).  Floating evaluation and its development checks are
not continuous certificates or research-candidate validation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from cosine_rectifying_core import CosineRectifyingCore, identity_hash


def dot(left, right):
    return np.sum(left * right, axis=-1)


def scaled(scalar, vector):
    return np.asarray(scalar)[..., None] * vector


def curve_jets_through_five(core, phi):
    """Return physical Cartesian gamma^(0),...,gamma^(5), all at fixed phi.

    If gamma_xy = r exp(i phi), its fifth derivative in the *same* radial
    frame is (r5 - 10 r3 + 5 r1, 5 r4 - 10 r2 + r0).  These are the
    components of the physical derivative, not ordinary derivatives of
    fourth-jet frame components.
    """
    phi = np.asarray(phi, float)
    result = list(core.raw_jets(phi))
    if len(result) != 5:
        raise ValueError('the frozen base interface must supply gamma jets 0 through 4')
    c, s = np.cos(phi), np.sin(phi)
    c3, s3 = np.cos(3 * phi), np.sin(3 * phi)
    c6, s6 = np.cos(6 * phi), np.sin(6 * phi)
    r0 = 1 + core.a * c3 + core.b * c6
    r1 = -3 * core.a * s3 - 6 * core.b * s6
    r2 = -9 * core.a * c3 - 36 * core.b * c6
    r3 = 27 * core.a * s3 + 216 * core.b * s6
    r4 = 81 * core.a * c3 + 1296 * core.b * c6
    r5 = -243 * core.a * s3 - 7776 * core.b * s6
    radial = r5 - 10 * r3 + 5 * r1
    angular = 5 * r4 - 10 * r2 + r0
    phase = phi[..., None] * core.frequencies
    vertical = -np.sum(np.sin(phase) *
                       (core.heights * core.frequencies ** 5), axis=-1)
    result.append(np.stack((radial * c - angular * s,
                            radial * s + angular * c, vertical), axis=-1))
    return result


def frame_invariants_through_two(core, phi):
    """Evaluate kappa, tau, their needed arclength jets, q_ell and q_ell_ell.

    Derivatives denoted phi are construction-angle derivatives; derivatives
    denoted ell use exact physical arclength.  No division by the torsion
    determinant is used, so zeros of tau (including symmetry axes) are valid.
    """
    x, v1, v2, v3, v4, v5 = curve_jets_through_five(core, phi)
    speed = np.linalg.norm(v1, axis=-1)
    cross = np.cross(v1, v2)
    cross_p = np.cross(v1, v3)
    cross_pp = np.cross(v2, v3) + np.cross(v1, v4)
    omega = np.linalg.norm(cross, axis=-1)
    if np.any(speed <= 0) or np.any(omega <= 0):
        raise ValueError('positive speed and curvature are required; no regularization is used')

    speed_p = dot(v1, v2) / speed
    speed_pp = (dot(v2, v2) + dot(v1, v3) - speed_p ** 2) / speed
    omega_p = dot(cross, cross_p) / omega
    omega_pp = (dot(cross_p, cross_p) + dot(cross, cross_pp) - omega_p ** 2) / omega
    determinant = dot(cross, v3)
    determinant_p = dot(cross, v4)
    determinant_pp = dot(cross_p, v4) + dot(cross, v5)

    tangent = v1 / speed[..., None]
    binormal = cross / omega[..., None]
    normal = np.cross(binormal, tangent)
    kappa = omega / speed ** 3
    tau = determinant / omega ** 2
    kappa_phi = omega_p / speed ** 3 - 3 * omega * speed_p / speed ** 4
    tau_phi = determinant_p / omega ** 2 - 2 * determinant * omega_p / omega ** 3

    factor = speed ** 3 / omega ** 3
    log_factor_p = 3 * (speed_p / speed - omega_p / omega)
    log_factor_pp = 3 * (speed_pp / speed - (speed_p / speed) ** 2
                         - omega_pp / omega + (omega_p / omega) ** 2)
    q = factor * determinant
    q_phi = factor * (determinant_p + determinant * log_factor_p)
    q_phi_phi = factor * (determinant_pp + 2 * determinant_p * log_factor_p
                           + determinant * (log_factor_p ** 2 + log_factor_pp))
    q_ell = q_phi / speed
    q_ell_ell = q_phi_phi / speed ** 2 - q_phi * speed_p / speed ** 3

    return {
        'x': x, 'speed': speed, 'speed_phi': speed_p,
        'T': tangent, 'N': normal, 'B': binormal,
        'kappa': kappa, 'tau': tau,
        'kappa_ell': kappa_phi / speed, 'tau_ell': tau_phi / speed,
        'q': q, 'q_phi': q_phi, 'q_phi_phi': q_phi_phi,
        'q_ell': q_ell, 'q_ell_ell': q_ell_ell,
    }


def material_frame_two_jets(core, s, theta):
    """Complete T/B two-jets in the original fixed material (s, theta).

    To use the outward coordinate t on side sigma in {-1,+1}, set
    s = sigma * (width + t).  Then T_t = sigma T_s, T_tt = T_ss,
    V = sigma B, V_t = B_s, V_tt = sigma B_ss.  The same signs apply to
    mixed theta derivatives.  Do not extrapolate outside a certified core:
    this evaluator retains the frozen base module's |s| <= width check.
    """
    if identity_hash(core.identity) != core.identity_sha256:
        raise ValueError('the physical identity changed after construction')
    s, theta = np.broadcast_arrays(np.asarray(s, float), np.asarray(theta, float))
    phi, inversion_error = core.phase(s, theta)
    f = frame_invariants_through_two(core, phi)
    q = f['q']; ql = f['q_ell']; qll = f['q_ell_ell']
    k = f['kappa']; kl = f['kappa_ell']; tau = f['tau']; taul = f['tau_ell']
    tangent, normal, binormal = f['T'], f['N'], f['B']
    J = 1 + s * ql
    if np.any(J <= 0):
        raise ValueError('nonpositive sampled J; no material jets exist at these points')

    ell_s = -q / J
    ell_theta = core.a0 / J
    ell_ss = 2 * q * ql / J ** 2 - s * q ** 2 * qll / J ** 3
    ell_st = -core.a0 * ql / J ** 2 + core.a0 * s * q * qll / J ** 3
    ell_tt = -core.a0 ** 2 * s * qll / J ** 3

    T_ell = scaled(k, normal)
    T_ell_ell = scaled(kl, normal) - scaled(k ** 2, tangent) + scaled(k * tau, binormal)
    B_ell = -scaled(tau, normal)
    B_ell_ell = scaled(tau * k, tangent) - scaled(taul, normal) - scaled(tau ** 2, binormal)

    answer = dict(f)
    answer.update({
        'phi': phi, 's': s, 'theta': theta, 'J': J,
        'ell_s': ell_s, 'ell_theta': ell_theta,
        'ell_ss': ell_ss, 'ell_st': ell_st, 'ell_tt': ell_tt,
        'Ts': scaled(ell_s, T_ell),
        'Ttheta': scaled(ell_theta, T_ell),
        'Tss': scaled(ell_s ** 2, T_ell_ell) + scaled(ell_ss, T_ell),
        'Tst': scaled(ell_s * ell_theta, T_ell_ell) + scaled(ell_st, T_ell),
        'Ttt': scaled(ell_theta ** 2, T_ell_ell) + scaled(ell_tt, T_ell),
        'Bs': scaled(ell_s, B_ell),
        'Btheta': scaled(ell_theta, B_ell),
        'Bss': scaled(ell_s ** 2, B_ell_ell) + scaled(ell_ss, B_ell),
        'Bst': scaled(ell_s * ell_theta, B_ell_ell) + scaled(ell_st, B_ell),
        'Btt': scaled(ell_theta ** 2, B_ell_ell) + scaled(ell_tt, B_ell),
        'frozen_physical_identity': core.identity,
        'frozen_physical_identity_sha256': core.identity_sha256,
        'a0_numerical': core.a0,
        'material_equation_residual_max': inversion_error,
        'arclength_quadrature_cells': core.arc_cells,
        'arclength_quadrature_order': core.quadrature,
        'global_J_certificate_available': core.global_J_certificate_available,
        'floating_evaluation_is_not_interval_certificate': True,
    })
    return answer


def relative_max(actual, expected):
    actual = np.asarray(actual); expected = np.asarray(expected)
    return float(np.max(np.abs(actual - expected), initial=0.) /
                 max(1., float(np.max(np.abs(expected), initial=0.))))


def developer_check():
    """Small artificial examples only; no research candidate is evaluated."""
    def fixture(a, b, heights, width):
        return {'height_basis': 'cosine', 'a': a, 'b': b, 'half_width': width,
                'height_coefficients': heights, 'height_offset': '1/11'}

    circle = CosineRectifyingCore(fixture('0', '0', ['0'], '1/10'),
                                   arc_cells=32, quadrature=8)
    angles = np.array([.17, .51, 1.03, 1.57, 2.31, 3.23, 5.73])
    exact = material_frame_two_jets(circle, .031, angles)
    circle_error = max(relative_max(exact['Tss'], 0),
                       relative_max(exact['Bss'], 0),
                       relative_max(exact['Ttt'], -exact['T']),
                       relative_max(exact['q_ell_ell'], 0))

    # This deliberately mild artificial curve is unrelated to any design run.
    core = CosineRectifyingCore(fixture('1/20', '1/200',
                                       ['1/25', '-1/100', '1/1000'], '1/100'),
                                 arc_cells=64, quadrature=16)
    point_s = .0017
    phi = np.array([.11, .37, .72, 1.19, 2.17, 3.72, 5.44])
    hp = 2e-6
    fifth = curve_jets_through_five(core, phi)[5]
    fifth_fd = (core.raw_jets(phi + hp)[4] - core.raw_jets(phi - hp)[4]) / (2 * hp)
    f = frame_invariants_through_two(core, phi)
    qll_fd = (core.frame(phi + hp)['q_ell'] - core.frame(phi - hp)['q_ell']) / (2 * hp * f['speed'])
    tau_l_fd = (core.frame(phi + hp)['tau'] - core.frame(phi - hp)['tau']) / (2 * hp * f['speed'])

    evaluated = material_frame_two_jets(core, point_s, angles)
    radial_errors = []
    # Genuine fixed-theta second differences of the old T evaluator.  The
    # two h values expose truncation/roundoff; they do not refit the model.
    for h in [2e-4, 1e-4]:
        plus = core.evaluate(point_s + h, angles)['Xtheta'] / core.a0
        minus = core.evaluate(point_s - h, angles)['Xtheta'] / core.a0
        center = core.evaluate(point_s, angles)['Xtheta'] / core.a0
        radial_errors.append({'h': h, 'relative_error':
                              relative_max(evaluated['Tss'], (plus - 2 * center + minus) / h ** 2)})

    hs = 2e-6
    ht = 2e-6
    sp = material_frame_two_jets(core, point_s + hs, angles)
    sm = material_frame_two_jets(core, point_s - hs, angles)
    tp = material_frame_two_jets(core, point_s, angles + ht)
    tm = material_frame_two_jets(core, point_s, angles - ht)
    checks = {'physical_gamma_fifth': relative_max(fifth, fifth_fd),
              'q_ell_ell': relative_max(f['q_ell_ell'], qll_fd),
              'tau_ell': relative_max(f['tau_ell'], tau_l_fd)}
    for letter in ['T', 'B']:
        checks[letter + 'ss_from_first'] = relative_max(
            evaluated[letter + 'ss'], (sp[letter + 's'] - sm[letter + 's']) / (2 * hs))
        checks[letter + 'st_from_radial'] = relative_max(
            evaluated[letter + 'st'], (sp[letter + 'theta'] - sm[letter + 'theta']) / (2 * hs))
        checks[letter + 'st_from_angle'] = relative_max(
            evaluated[letter + 'st'], (tp[letter + 's'] - tm[letter + 's']) / (2 * ht))
        checks[letter + 'tt'] = relative_max(
            evaluated[letter + 'tt'], (tp[letter + 'theta'] - tm[letter + 'theta']) / (2 * ht))

    compact_Tss = (scaled(evaluated['tau'] ** 2 / evaluated['J'] ** 2,
                           scaled(evaluated['q'], evaluated['B']) - evaluated['T'])
                    + scaled((evaluated['q'] * evaluated['tau_ell']
                              + evaluated['tau'] * evaluated['q_ell']
                              - point_s * evaluated['tau'] * evaluated['q']
                              * evaluated['q_ell_ell'] / evaluated['J'])
                             / evaluated['J'] ** 2, evaluated['N']))
    checks['compact_Tss_identity'] = relative_max(evaluated['Tss'], compact_Tss)
    passed = (circle_error < 1e-12 and max(checks.values()) < 2e-5
              and min(row['relative_error'] for row in radial_errors) < 2e-4)
    return {'schema': 'cosine-core-high-jets-developer-check-v1',
            'artificial_inputs_only': True, 'passed': passed,
            'circle_error': circle_error, 'checks': checks,
            'fixed_theta_Tss_second_difference': radial_errors,
            'material_equation_residual_max': evaluated['material_equation_residual_max'],
            'frozen_artificial_identity': core.identity,
            'frozen_artificial_identity_sha256': core.identity_sha256,
            'research_candidate_or_continuous_certificate': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true', required=True)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = developer_check()
    encoded = json.dumps(report, indent=2) + '\n'
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(encoded)
    else:
        print(encoded, end='')
    if not report['passed']:
        raise SystemExit('artificial high-jet derivative check failed')


if __name__ == '__main__':
    main()
