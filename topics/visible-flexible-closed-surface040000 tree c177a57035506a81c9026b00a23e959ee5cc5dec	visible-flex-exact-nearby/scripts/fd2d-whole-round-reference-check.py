#!/usr/bin/env python3
"""Small real point/jet and nonzero-direction check; no whole F/J or BVP."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import resource
import time

import numpy as np

from fd2d_balanced_curvature_core import BalancedCurvatureCore
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_gc_whole_round_reference import (FrozenRoundPrefixReference, digest,
    round_increment_residual, round_increment_jvp, fixed_scale_gap)


def absolute(value):
    return float(np.max(np.abs(value))) if np.size(value) else 0.


def scaled(a, b):
    return absolute((a-b)/np.maximum(1., np.maximum(np.abs(a), np.abs(b))))


def synthetic_increment(s, xi, direction=False):
    s, x = s[None, :], xi[:, None]
    if not direction:
        Y = np.stack((.012*s*np.cos(2*x), .009*s*s*np.sin(2*x),
                      .017*(1+s)*np.cos(4*x)), axis=-1)
        Ys = np.stack((np.broadcast_to(.012*np.cos(2*x), Y.shape[:2]),
                       .018*s*np.sin(2*x),
                       np.broadcast_to(.017*np.cos(4*x), Y.shape[:2])), axis=-1)
        Yx = np.stack((-.024*s*np.sin(2*x), .018*s*s*np.cos(2*x),
                       -.068*(1+s)*np.sin(4*x)), axis=-1)
    else:
        Y = np.stack((.013*(1+s)*np.cos(4*x), .011*s*np.sin(2*x),
                      -.007*s*s*np.cos(2*x)), axis=-1)
        Ys = np.stack((np.broadcast_to(.013*np.cos(4*x), Y.shape[:2]),
                       np.broadcast_to(.011*np.sin(2*x), Y.shape[:2]),
                       -.014*s*np.cos(2*x)), axis=-1)
        Yx = np.stack((-.052*(1+s)*np.sin(4*x), .022*s*np.cos(2*x),
                       .014*s*s*np.sin(2*x)), axis=-1)
    return Y, Ys, Yx


def direct_original(reference, Y, Ys, Yx, target, Us, Ux):
    fields, radial = reference['values']+Y, reference['ds']+Ys
    a, c, K = (target[k] for k in ('a', 'c', 'K'))
    adv, inv = Us/Ux, 1/(a*Ux)
    Cn = radial[..., 0]-adv*Yx[..., 0]-inv*Yx[..., 1]-c*(fields[..., 2]-fields[..., 0])
    Cm = radial[..., 1]-adv*Yx[..., 1]-inv*Yx[..., 2]+2*c*fields[..., 1]
    G = fields[..., 2]*fields[..., 0]-fields[..., 1]**2-K
    return dict(codazzi=np.stack((Cn, Cm), axis=-1), gauss=G)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    started = time.monotonic()
    ref = FrozenRoundPrefixReference()
    pieces = ref.base.segments
    feedback = [p for p in pieces if p['kind'] == 'hermite'][20]
    spacer = next(p for p in pieces if p['label'] == 'outward_peak_spacer')
    entry = next(p for p in pieces if p['label'] == 'partial_return_acceleration_entry')
    redeepen = next(p for p in pieces if p['label'] == 'redeepen_after_partial_return')
    brake = pieces[-1]
    sample = np.array([0., feedback['s0']+.43*feedback['L'],
        spacer['s0']+.41*spacer['L'], entry['s0']+.43*entry['L'],
        redeepen['s0']+.31*redeepen['L'], brake['s0']+.37*brake['L'],
        np.nextafter(ref.end, -np.inf), ref.end])
    packet = ref.jet(sample)
    values, ds = packet['values'], packet['ds']
    independent_gc = dict(
        gauss=absolute(values[:, 0]*values[:, 2]-packet['K0']),
        n_codazzi=absolute(ds[:, 0]-packet['c0']*(values[:, 2]-values[:, 0])),
        m_codazzi=absolute(ds[:, 1]))
    original_a, original_v, original_acc = ref.base.profile(sample)
    profile_roundoff = dict(a=absolute(original_a-packet['a']),
        a_s=absolute(original_v-packet['a_s']),
        a_ss=absolute(original_acc-packet['a_ss']))
    cut_zero = bool(np.array_equal(values[-1], np.zeros(3)))
    near = dict(s=float(sample[-2]), distance_to_cut=float(ref.end-sample[-2]),
        n=float(values[-2, 0]), l=float(values[-2, 2]),
        finite=bool(np.all(np.isfinite(values[-2]))))
    jet_differences = []
    for s in (sample[1], sample[5]):
        h = 2e-7
        analytical = ref.jet([s])['ds']
        difference = (ref.jet([s+h])['values']-ref.jet([s-h])['values'])/(2*h)
        jet_differences.append(dict(s=float(s), step=h,
            absolute_difference=absolute(analytical-difference),
            scaled_difference=scaled(analytical, difference)))

    # Actual physical bump profile at two points, nonzero delta and a
    # nonzero independent delta direction. No saved main solver is loaded.
    s = np.array([.64, 1.10])
    xi = np.array([.17, .53, 1.10])
    r = ref.jet(s)
    profile = RadialBumpProfile(ref.source, count=7)
    delta = np.array([.0002, -.0003, .0001, .0004, -.0002, .0001, -.00015])
    dd = np.array([.002, -.003, .001, -.002, .004, -.001, .003])
    profile.set_parameters(delta)
    target = profile.jet(s)
    dtarget = profile.jvp(s, dd)
    Y, Ys, Yx = synthetic_increment(s, xi)
    DY, DYs, DYx = synthetic_increment(s, xi, direction=True)
    Us = .03*np.sin(2*xi[:, None])
    Ux = 1+.06*s[None, :]*np.cos(2*xi[:, None])
    common = dict(a=target['a'], c=target['c'], K=target['K'], U_s=Us, U_xi=Ux)
    result = round_increment_residual(r, Y, Ys, Yx, **common)
    direct = direct_original(r, Y, Ys, Yx, target, Us, Ux)
    comparison = {k:dict(absolute=absolute(result[k]-direct[k]),
                         scaled=scaled(result[k], direct[k]))
                  for k in ('codazzi', 'gauss')}
    derivative = round_increment_jvp(r, Y, Ys, Yx, DY, DYs, DYx,
        **common, a_direction=dtarget['a'], c_direction=dtarget['c'],
        K_direction=dtarget['K'])
    h = 1e-5
    displaced = []
    for sign in (1., -1.):
        profile.set_parameters(delta+sign*h*dd)
        displaced.append(direct_original(r, Y+sign*h*DY, Ys+sign*h*DYs,
            Yx+sign*h*DYx, profile.jet(s), Us, Ux))
    jvp = {}
    for k in ('codazzi', 'gauss'):
        finite = (displaced[0][k]-displaced[1][k])/(2*h)
        jvp[k] = dict(step=h, absolute=absolute(derivative[k]-finite),
                      scaled=scaled(derivative[k], finite))

    zero = np.zeros((len(sample), 3))
    round_zero = round_increment_residual(packet, zero, zero, zero,
        a=packet['a'], c=packet['c0'], K=packet['K0'])
    core = BalancedCurvatureCore(np.zeros(2), base_kind='circle')
    core_values = core.curvature(xi)
    axes = core.axis_intercepts_and_jacobian()
    gap = fixed_scale_gap(float(axes['gap']), 0., scale=.9)
    central = dict(core_definition=core.definition(),
        reference_a0=float(ref.a0), core_a0=float(core.a0),
        a0_evaluation_difference=float(np.longdouble(ref.a0)-core.a0),
        n_evaluation_difference=absolute(np.asarray(core_values['n'], float)-values[0, 0]),
        actual_gap=float(axes['gap']), normalized_zero_gap=float(gap['value']),
        fixed_gap_scale=gap['scale'],
        normalization_derivative_actual=gap['actual_gap_derivative'],
        normalization_derivative_target=gap['target_gap_derivative'])
    passed = bool(
        cut_zero and near['finite'] and near['n'] > 0 and near['l'] > 0
        and max(independent_gc.values()) < 1e-12
        and all(q['scaled_difference'] < 5e-7 for q in jet_differences)
        and all(q['scaled'] < 1e-12 for q in comparison.values())
        and all(q['scaled'] < 1e-8 for q in jvp.values())
        and absolute(round_zero['gauss']) == 0 and absolute(round_zero['codazzi']) == 0
        and central['actual_gap'] == 0 and central['normalized_zero_gap'] == 0
        and central['n_evaluation_difference'] < 1e-13)
    report = dict(schema='fd2d-whole-round-reference-local-check-v1',
        actual_execution=True, passed=passed, reference=ref.definition(),
        check_source_sha256=digest(__file__),
        radial_profile_source_sha256=digest(__import__('fd2d_gc_radial_bump_profile').__file__),
        scalar_points=sample.tolist(), scalar_values=values.tolist(),
        scalar_physical_one_jets=ds.tolist(), independent_gc_roundoff=independent_gc,
        old_reader_scalar_evaluation_difference=profile_roundoff,
        exact_flat_cut_values_returned=cut_zero,
        final_l_s_prefix_left=float(ds[-1, 2]), flat_tail_l_s=0.,
        no_C1_second_fundamental_form_claim=True, nextafter_inside_cut=near,
        one_jet_centered_difference=jet_differences,
        local_increment=dict(radial_points=s.tolist(), angles=xi.tolist(),
            actual_profile_delta=delta.tolist(), delta_direction=dd.tolist(),
            fixed_chart='U=xi+.03*s*sin(2*xi)', original_equation_comparison=comparison,
            nonzero_direction_jvp_comparison=jvp),
        zero_increment_exact_floating_residual=dict(
            gauss=absolute(round_zero['gauss']), codazzi=absolute(round_zero['codazzi'])),
        circle_central=central, seconds=time.monotonic()-started,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        scope='Eight scalar locations, two physical bump-profile points times three angles, one nonzero direction and zero-gap circle reuse only. No main saved field, whole objective, whole Jacobian, body integration, continuation or nonlinear existence claim.')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(passed=passed, seconds=report['seconds'],
        maximum_rss_kib=report['maximum_rss_kib'],
        independent_gc_roundoff=independent_gc, profile_roundoff=profile_roundoff,
        cut_left_l_s=report['final_l_s_prefix_left'], local_comparison=comparison,
        jvp=jvp, circle_gap=central['actual_gap']), allow_nan=False))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
