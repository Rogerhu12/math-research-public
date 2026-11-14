#!/usr/bin/env python3
"""Provisional new-metric prefix design for a wider, less flat tail cut.

The prescribed m2 slope is an explicit DESIGN TARGET, not a solved DN map.
This screen also changes the intermediate contraction speed, because merely
reducing the last deep phase leaves the old common-prefix amplification.
All residuals/extrema are finite diagnostics. No full-tail height or actual
closed geometry is supplied by this program.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from scipy.optimize import brentq
import fd2d_moderate_deep_screen as moderate
from fd2d_monotone_ellipse_screen import acceleration_piece

lin, fm = moderate.lin, moderate.fm


def provisional_bundle(source, vmid, rcut, wcut, slope, pdeep):
    b = copy.deepcopy(source)
    labels = {p.get('label'):j for j,p in enumerate(b['segments'])}
    entry = labels['partial_return_acceleration_entry']
    plateau = labels['partial_return_acceleration_plateau']
    exit_piece = labels['partial_return_acceleration_exit']
    first = labels['early_shallow_return']
    coast = labels['partial_return_matching_coast']
    down = labels['redeepen_after_partial_return']
    deep = labels['final_deep_coast']
    brake = labels['cut_second_jet_brake']
    parameters = b['partial_return_design_parameters']
    acceleration, transition = parameters['acceleration'], parameters['transition']
    jet = list(b['segments'][entry]['jet1'])
    duration = (-vmid+acceleration*transition/2-jet[1])/(-acceleration)
    if duration <= 0:
        raise ValueError('The requested moderate speed has no positive plateau')
    b['segments'][plateau], jet = acceleration_piece(jet, duration, -acceleration,
                                                   'partial_return_acceleration_plateau')
    b['segments'][exit_piece], jet = acceleration_piece(jet, transition, 0.,
                                                      'partial_return_acceleration_exit')
    turn = fm.turn(math.asin(jet[1]), -parameters['return_phase'], parameters['K'])
    turn.update(start_from_previous=True, length_from_turn_rate=True,
                label='early_shallow_return')
    b['segments'][first] = turn
    b['segments'][coast]['L'] = .01
    b['segments'][down]['p1'] = -pdeep
    b['segments'][deep].update(p0=-pdeep, p1=-pdeep, radius_after_next=rcut)
    wr = -7*wcut/rcut
    phase = -math.atan2(1., wcut)
    phase_speed = -wr/(1+wcut*wcut)**1.5
    b['segments'][brake].update(p0=-pdeep, p1=phase,
                               L=2*(phase+pdeep)/phase_speed)
    b['cut_reference'] = dict(r=rcut, w=wcut, wr=wr)
    b['cut'] = dict(r=rcut, w=wcut, wr=wr, cuff_radius=.32,
                    a_prime=-1/math.sqrt(1+wcut*wcut),
                    a_second=-wcut*wr/(1+wcut*wcut)**2,
                    z_prime=wcut/math.sqrt(1+wcut*wcut),
                    physical_upper_background_height_r_sign=-1,
                    linear_slopes={'2':slope},
                    tail_height_span=0., tail_height_span_known=False,
                    zero_tail_height_is_unused_placeholder=True,
                    solved_tail_port=False)
    parameters.update(vmid=vmid, epsilon=math.pi/2-pdeep, coast_length=.01)
    b['inputs']['historical_tail_port_only'] = b['inputs'].pop('tail_port', None)
    b['inputs']['historical_tail_port_sha256_only'] = b['inputs'].pop('tail_port_sha256', None)
    b['inputs']['historical_tail_config_sha256_only'] = b['inputs'].pop('tail_config_sha256', None)
    b['provisional_tail_target'] = dict(mode=2, slope=slope, actual_DN_solved=False,
        changed_physical_metric=True, cut_radius=rcut, cut_w=wcut,
        reason='Design for the separately calibrated layered R64 tail; actual port must replace this target')
    b['finite_linear_screen'] = dict(terminal_direction=[-wcut*(rcut*slope-4)/3, 1.],
                                     scope='Prescribed provisional direction, not an actual tail solve')
    for key in ('metric_diagnostics', 'full_m2_amplification', 'moderate_deep_design'):
        b.pop(key, None)
    b['status'] = dict(metric_frozen=False, nonlinear_prefix_solved=False,
        nonlinear_tail_matched=False, closed_surface=False, reach_certified=False,
        strong_target_complete=False)
    return b


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--rcut', type=float, default=.5)
    parser.add_argument('--wcut', type=float, default=.3)
    parser.add_argument('--slope', type=float, default=8.)
    parser.add_argument('--vmid', type=float, nargs='+', default=[.75,.85,.95,.98])
    parser.add_argument('--pdeep', type=float, nargs='+', default=[1.30,1.34,1.40])
    args = parser.parse_args()
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh wider-cut screen stem')
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    source = json.loads(args.source.read_text())
    started = time.monotonic()
    report_path = args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    result = dict(schema='fd2d-provisional-wider-cut-prefix-screen-v1', scope=__doc__,
        source_sha256=fm.digest(__file__), original_candidate_sha256=fm.digest(args.source),
        rcut=args.rcut, wcut=args.wcut, prescribed_m2_slope=args.slope,
        actual_tail_port=False, nonlinear_solution=False, continuous_certificate=False,
        rows=[], roots=[], selected=None)
    best = math.inf

    def save():
        result['elapsed_seconds'] = time.monotonic()-started
        result['maximum_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        tmp = report_path.with_name(report_path.name+'.tmp')
        tmp.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
        tmp.replace(report_path)

    for vmid in args.vmid:
        initial = provisional_bundle(source, vmid, args.rcut, args.wcut,
                                     args.slope, args.pdeep[0])
        tag = str(vmid).replace('.', 'p')
        path = args.out_prefix.with_name(args.out_prefix.name+f'-vmid{tag}-base.json')
        path.write_text(json.dumps(initial, indent=2)+'\n')
        family = moderate.ModerateFamily(path)
        print(json.dumps(dict(event='family', vmid=vmid,
                              prefix_fg=family.prefix_fg.tolist())), flush=True)
        for deep in args.pdeep:
            previous = None
            try:
                upper = family.Tmax(deep)
            except Exception as exc:
                result['rows'].append(dict(vmid=vmid, pdeep=deep, error=repr(exc)))
                save()
                continue
            for fraction in (0., .05, .15, .35, .6, .9, .99):
                T = fraction*upper
                try:
                    residual, end = family.shoot(deep, T)
                    row = dict(vmid=vmid, pdeep=deep, T=T, Tmax=upper,
                               fraction=fraction, residual=residual,
                               terminal_fg=end.tolist())
                    if previous is not None and previous[1]*residual < 0:
                        root = brentq(lambda t: family.shoot(deep,t)[0],
                                      previous[0], T, xtol=5e-13, rtol=1e-14)
                        bundle = family.bundle(deep, root)
                        candidate = fm.Candidate(bundle)
                        trace = lin.LinearTrace(candidate, rtol=3e-14,
                                                atol=3e-16, max_step=.02)
                        extrema = trace.extrema(65)
                        final = trace.endpoint()
                        normres = ((final[0]*family.target[1]-final[1]*family.target[0])/
                                   (np.linalg.norm(final)*np.linalg.norm(family.target)))
                        metric = candidate.metric_diagnostics()
                        record = dict(vmid=vmid, pdeep=deep, T=float(root), Tmax=upper,
                            normalized_terminal_residual=float(normres), terminal_fg=final.tolist(),
                            maximum_eta=extrema['global_extrema']['eta'],
                            maximum_zeta=extrema['global_extrema']['zeta'],
                            minimum_b=min(p['minimum_b'] for p in extrema['pieces']),
                            minimum_n_reference=min(p['minimum_n_reference'] for p in extrema['pieces']),
                            maximum_background_meridian_curvature=max(p['maximum_rotational_meridian_curvature'] for p in extrema['pieces']),
                            background_height_PREFIX_ONLY=metric['background_height'],
                            actual_tail_height_UNKNOWN=True, full_geometry_checked=False)
                        result['roots'].append(record)
                        bundle['finite_linear_screen'] = dict(
                            normalized_direction_residual=float(normres),
                            terminal_height_gain_at_exact_direction_match=float(final[1]),
                            terminal_direction=family.target.tolist(),
                            prefix_line=family.prefix_fg.tolist(),
                            scope='Matched to a prescribed ideal m2 direction only, not a solved tail port')
                        bundle['full_m2_amplification'] = record
                        bundle['status']['metric_frozen'] = False
                        score = max(record['maximum_eta']['absolute'], record['maximum_zeta']['absolute'])
                        if score < best:
                            best = score
                            number = len(result['roots'])
                            chosen = args.out_prefix.with_name(args.out_prefix.name+f'-candidate-{number:03d}.json')
                            trajectory = args.out_prefix.with_name(args.out_prefix.name+f'-trajectory-{number:03d}.npz')
                            chosen.write_text(json.dumps(bundle, indent=2)+'\n')
                            np.savez_compressed(trajectory, **trace.sample())
                            result['selected'] = dict(candidate=chosen.name, candidate_sha256=fm.digest(chosen),
                                trajectory=trajectory.name, trajectory_sha256=fm.digest(trajectory),
                                criterion='Smallest measured full-prefix relative m2 amplification among actual tried roots',
                                full_geometry_or_tail_NOT_accepted=True, root=record)
                        print(json.dumps(dict(event='root', **record)), flush=True)
                    previous = T, residual
                except Exception as exc:
                    row = dict(vmid=vmid, pdeep=deep, T=T, fraction=fraction,
                               error=repr(exc))
                    previous = None
                result['rows'].append(row)
                save()
                print(json.dumps(row), flush=True)
    result['body_finished'] = True
    save()
    print(json.dumps(dict(event='completed', roots=len(result['roots']),
                          selected=result['selected'], seconds=result['elapsed_seconds'])), flush=True)


if __name__ == '__main__':
    main()
