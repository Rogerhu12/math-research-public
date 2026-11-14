#!/usr/bin/env python3
"""Small geometry checks for the inward reference and exact ellipse inlet.

This does not optimize a connector. The reference is a surface of revolution,
not the requested noncircular isometric half-band.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from scipy.special import ellipe

from core_to_tail_bvp import InwardMeridian, Problem, ellipse_inlet


def closed_reference_pair_screen(ref, cylinder_height, cut_radius):
    """Sample normal-chord radii of the round reference, including both caps."""
    u = np.linspace(0, 1, 401)
    aa, zz = ref.evaluate(u)
    beta = ref.beta(u)
    cylz = np.linspace(0, cylinder_height, 65, endpoint=False)
    capr = np.linspace(cut_radius, 0, 81)[1:]
    pos = np.vstack((np.column_stack((np.full_like(cylz, ref.a0), cylz)),
                     np.column_stack((aa[0], zz[0])),
                     np.column_stack((capr, np.full_like(capr, zz[0][-1])))))
    normal = np.vstack((np.column_stack((-np.ones_like(cylz), np.zeros_like(cylz))),
                        np.column_stack((-np.sin(beta), np.cos(beta))),
                        np.column_stack((np.zeros_like(capr), -np.ones_like(capr)))))
    pos = np.vstack((pos, pos * [1., -1.]))
    normal = np.vstack((normal, normal * [1., -1.]))
    dz = pos[None, :, 1] - pos[:, None, 1]
    answer = np.inf
    for sign in (1., -1.):
        dr = sign * pos[None, :, 0] - pos[:, None, 0]
        distance2 = dr * dr + dz * dz
        den = 2 * np.abs(normal[:, None, 0] * dr + normal[:, None, 1] * dz)
        valid = (distance2 > 1e-16) & (den > 1e-16)
        answer = min(answer, float(np.min(distance2[valid] / den[valid])))
    return dict(sample_normal_chord_radius=answer,
                sample_normal_chord_over_target_diameter_2_3=answer / 2.3,
                meridian_points=len(pos), includes_both_flat_disks=True,
                exact_ellipse_connector_checked=False, reach_proved=False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    a0 = 2 * ellipe(.91) / np.pi
    rows = []
    choices = [(.2, .8, .55, .06, .3), (1.45, .7, .75, .19, .28),
               (1.53, .67, .8, .23, .28), (1.5, .68, .8, .25, .28)]
    theta = np.arange(1024) * 2 * np.pi / 1024
    for eta, fraction, length, height, cut_radius in choices:
        row = dict(overshoot=eta, first_fraction=fraction, length=length,
                   cylinder_height=height, cut_radius=cut_radius)
        try:
            ref = InwardMeridian(a0, 0, 0, length, cut_radius, [0, 0, height], 48, eta, fraction)
            u = np.linspace(0, 1, 1601)
            aa, zz = ref.evaluate(u)
            beta = ref.beta(u)
            curv = np.maximum(np.abs(ref.beta(u, 1) / length),
                              np.abs(np.sin(beta) / aa[0]))
            start = ellipse_inlet(theta, 1., .3, height)[0][0]
            end = np.column_stack((cut_radius * np.sin(theta), -cut_radius * np.cos(theta),
                                   np.full_like(theta, zz[0][-1])))
            chord = float(np.max(np.linalg.norm(end - start, axis=-1)))
            row.update(active_length=ref.control, first_length=ref.u1 * length,
                       second_length=(ref.u2 - ref.u1) * length,
                       flat_length=(1 - ref.u2) * length,
                       end_height=float(zz[0][-1]), max_height=float(zz[0].max()),
                       min_radius=float(aa[0].min()), max_radius=float(aa[0].max()),
                       max_sample_principal_curvature=float(curv.max()),
                       min_sample_meridian_radius=float(1 / curv.max()),
                       a_prime_max=float(aa[1].max()), closure_error=ref.closure_error,
                       max_corresponding_ellipse_port_chord=chord,
                       sampled_port_chord_necessary_condition_passes=(chord <= length),
                       corresponding_chord_lower_bound_on_max_E_error=max(0., (chord / length)**2 - 1),
                       reference_only=True)
            if chord <= length and np.min(zz[0]) > 0:
                row['closed_round_reference_screen'] = closed_reference_pair_screen(ref, height, cut_radius)
        except ValueError as exc:
            row['closure_error_message'] = str(exc)
        rows.append(row)
    theta = np.arange(513) * 2 * np.pi / 513
    pos, a0, err = ellipse_inlet(theta, 1., .3, .06, 0)
    p1 = ellipse_inlet(theta, 1., .3, .06, 1)[0]
    p2 = ellipse_inlet(theta, 1., .3, .06, 2)[0]
    ends = ellipse_inlet(np.array([0., 2 * np.pi]), 1., .3, .06, 0)[0]
    jets = dict(arclength_radius=a0, phase_inversion_error=err,
                unit_metric_error=float(np.max(np.abs(np.sum(p1[0]**2, axis=1) / a0**2 - 1))),
                dot_xt_xtt=float(np.max(np.abs(np.sum(p1[0] * p2[0], axis=1)))),
                cyclic_endpoint_position_error=float(np.max(np.abs(ends[0, 0] - ends[0, 1]))),
                exact_rho_min=.09, exact_rho_max=1 / .3)
    # A nontrivial exact round control tests the entire inlet/background/Hermite
    # assembly, without running least squares.
    control_args = SimpleNamespace(radial_free=3, modes=4, design_metric=True,
        core_profile='ellipse', ellipse_major=.7, ellipse_minor=.7, inlet_angles=64,
        inlet_s=.06, quadrature=48, background='inward', length=.55, cut_radius=.3,
        flat_start=.28, cuff_radius=.25, inward_overshoot=.2, inward_first_fraction=.8,
        tail_height=None, tail_plus=0., tail_minus=0.)
    control = Problem(control_args)
    round_audit = control.audit(control.seed(), 81, 128)
    payload = dict(status='development_geometry_checks_only_no_solve', ellipse=jets,
                   inward_reference_profiles=rows, exact_round_seed_audit=round_audit,
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps(dict(ellipse=jets,
         round_metric=round_audit['relative_metric_operator_sample_max'],
         round_endpoint_jets=round_audit['endpoint_two_jet_matching_sample_max'])))


if __name__ == '__main__':
    main()
