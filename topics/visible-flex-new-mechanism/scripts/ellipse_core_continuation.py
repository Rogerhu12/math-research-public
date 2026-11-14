#!/usr/bin/env python3
"""Design continuation from a round cylinder to a fixed-perimeter ellipse.

The nonlinear work is intended for this public repository's GitHub Actions.
--plan-only performs only the exact round control and one-dimensional reference
checks. Every continuation stage is a metric design, not fixed-g refinement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from types import SimpleNamespace

import numpy as np
from scipy.special import ellipe

from core_to_tail_bvp import Problem, ellipse_inlet


def axes(t, major, minor):
    a0 = 2 * major * ellipe(1 - (minor / major)**2) / np.pi
    ratio = np.exp(t * np.log(major / minor))
    aa = a0 * np.pi / (2 * ellipe(1 - ratio**-2))
    return float(aa), float(aa / ratio), float(a0)


def command(args, t, output, warm=None):
    aa, bb, _ = axes(t, args.target_major, args.target_minor)
    solver = Path(__file__).with_name('core_to_tail_bvp.py')
    pairs = [('--core-profile', 'ellipse'), ('--ellipse-major', aa), ('--ellipse-minor', bb),
             ('--inlet-s', args.h0), ('--background', 'unit'), ('--length', args.length),
             ('--beta-wiggle', args.beta_wiggle), ('--cut-radius', args.cut_radius),
             ('--flat-start', args.flat_start), ('--cuff-radius', args.cuff_radius),
             ('--tail-plus', 0), ('--tail-minus', 0),
             ('--tail-plus-min', -args.tail_angle_max), ('--tail-minus-min', -args.tail_angle_max),
             ('--tail-angle-max', args.tail_angle_max),
             ('--tail-height-min', args.h0 + args.target_reach),
             ('--tail-height-max', args.tail_height_max),
             ('--radius-floor', args.radius_floor), ('--radius-ceiling', args.radius_ceiling),
             ('--radial-free', args.radial_free), ('--modes', args.modes),
             ('--angular', args.angular), ('--radial-gauss', args.radial_gauss),
             ('--inlet-angles', args.inlet_angles), ('--max-nfev', args.max_nfev),
             ('--out', output)]
    cmd = [sys.executable, str(solver)]
    for key, value in pairs:
        cmd.extend((key, str(value)))
    if warm is not None:
        cmd.extend(('--warm', str(warm)))
    return cmd


def preflight(args):
    aa, bb, a0 = axes(0., args.target_major, args.target_minor)
    settings = SimpleNamespace(radial_free=args.radial_free, modes=args.modes, design_metric=True,
        core_profile='ellipse', ellipse_major=aa, ellipse_minor=bb, inlet_angles=args.inlet_angles,
        inlet_s=args.h0, quadrature=48, background='unit', length=args.length,
        cut_radius=args.cut_radius, flat_start=args.flat_start, cuff_radius=args.cuff_radius,
        beta_wiggle=args.beta_wiggle, tail_height=None, tail_plus=0., tail_minus=0.)
    problem = Problem(settings)
    round_audit = problem.audit(problem.seed(), 81, 128)
    grid = np.linspace(0, 1, 1001)
    ar, zz = problem.reference.evaluate(grid)
    theta = np.arange(1024) * 2 * np.pi / 1024
    target = ellipse_inlet(theta, args.target_major, args.target_minor, args.h0)[0][0]
    port = np.column_stack((args.cut_radius * np.sin(theta), -args.cut_radius * np.cos(theta),
                           np.full_like(theta, zz[0][-1])))
    ref_diagnostic = problem.reference.diagnostics()
    for key in ('diameter_box_upper', 'sample_curvature_times_003_diameter_box',
                'sample_min_normal_chord_radius_over_diameter_box'):
        ref_diagnostic.pop(key, None)
    report = dict(constant_perimeter_radius=a0,
                  reference_geometry=ref_diagnostic,
                  reference_ball_radius_sample=float(np.max(np.sqrt(ar[0]**2 + zz[0]**2))),
                  reference_tail_height=float(zz[0][-1]),
                  tail_height_bounds=[args.h0 + args.target_reach, args.tail_height_max],
                  reference_height_in_bounds=bool(args.h0 + args.target_reach <= zz[0][-1]
                                                  <= args.tail_height_max),
                  target_ellipse_corresponding_chord_sample_max=float(np.max(np.linalg.norm(port-target, axis=1))),
                  round_seed_metric_error=round_audit['relative_metric_operator_sample_max'],
                  round_seed_two_jet_error=round_audit['endpoint_two_jet_matching_sample_max'],
                  round_reference_is_not_target_ellipse_connector=True)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir', type=Path, required=True)
    parser.add_argument('--prefix', default='ellipse-continuation')
    parser.add_argument('--target-major', type=float, default=1.)
    parser.add_argument('--target-minor', type=float, default=.3)
    parser.add_argument('--length', type=float, default=1.)
    parser.add_argument('--h0', type=float, default=.23)
    parser.add_argument('--beta-wiggle', type=float, default=.8)
    parser.add_argument('--cut-radius', type=float, default=.28)
    parser.add_argument('--flat-start', type=float, default=.26)
    parser.add_argument('--cuff-radius', type=float, default=.23)
    parser.add_argument('--target-reach', type=float, default=.069)
    parser.add_argument('--tail-angle-max', type=float, default=.1)
    parser.add_argument('--tail-height-max', type=float, default=1.05)
    parser.add_argument('--radius-floor', type=float, default=.24)
    parser.add_argument('--radius-ceiling', type=float, default=.95)
    parser.add_argument('--radial-free', type=int, default=9)
    parser.add_argument('--modes', type=int, default=12)
    parser.add_argument('--angular', type=int, default=96)
    parser.add_argument('--radial-gauss', type=int, default=6)
    parser.add_argument('--inlet-angles', type=int, default=256)
    parser.add_argument('--max-nfev', type=int, default=250)
    parser.add_argument('--initial-step', type=float, default=.125)
    parser.add_argument('--min-step', type=float, default=1/128)
    parser.add_argument('--max-attempts', type=int, default=40)
    parser.add_argument('--accept-metric', type=float, default=1e-4)
    parser.add_argument('--warm-json', type=Path)
    parser.add_argument('--plan-only', action='store_true')
    args = parser.parse_args()
    if not 0 < args.target_minor <= args.target_major:
        parser.error('Need 0 < target minor <= target major')
    if not 0 < args.min_step <= args.initial_step <= 1:
        parser.error('Need 0 < min step <= initial step <= 1')
    if not 0 < args.cuff_radius < args.flat_start < args.cut_radius:
        parser.error('Need cuff radius < flat start < cut radius')
    if args.h0 + args.target_reach >= args.tail_height_max:
        parser.error('Tail height bounds are empty')
    if '/' in args.prefix or '\\' in args.prefix:
        parser.error('Prefix must be a filename component')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    summary_path = args.out_dir / f'{args.prefix}-summary.json'
    metadata = {key: (str(value) if isinstance(value, Path) else value)
                for key, value in vars(args).items()}
    report = dict(status='prepared', task_complete=False, target_design_reached=False,
                  design_is_not_fixed_metric_refinement=True,
                  accepted_metric_threshold=args.accept_metric, parameters=metadata,
                  preflight=preflight(args), attempts=[], accepted=[],
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  solver_sha256=hashlib.sha256(Path(__file__).with_name('core_to_tail_bvp.py').read_bytes()).hexdigest())

    def save():
        temporary = summary_path.with_suffix('.tmp')
        temporary.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
        temporary.replace(summary_path)

    if not report['preflight']['reference_height_in_bounds']:
        report['status'] = 'reference_height_outside_required_bounds_no_solve'
        save()
        print(json.dumps(dict(status=report['status'], preflight=report['preflight'])))
        return
    if args.plan_only:
        values = np.linspace(0, 1, int(np.ceil(1 / args.initial_step)) + 1)
        previous = None
        report['planned_commands'] = []
        for index, t in enumerate(values):
            out = args.out_dir / f'{args.prefix}-attempt-{index:03d}-t{t:.6f}.json'
            report['planned_commands'].append(command(args, float(t), out, previous))
            previous = out
        report['status'] = 'plan_only_no_solve'
        save()
        print(json.dumps(dict(status=report['status'], summary=str(summary_path), preflight=report['preflight'])))
        return

    accepted_t = None
    warm = None
    if args.warm_json:
        old = json.loads(args.warm_json.read_text())
        d = old['definition']
        if d.get('core_profile') != 'ellipse':
            parser.error('--warm-json must contain an ellipse continuation candidate')
        aa, bb = d['ellipse_major'], d['ellipse_minor']
        old_a0 = 2 * aa * ellipe(1 - (bb / aa)**2) / np.pi
        if abs(old_a0 - report['preflight']['constant_perimeter_radius']) > 1e-10:
            parser.error('Warm candidate does not have the same prescribed perimeter')
        if args.target_major == args.target_minor:
            accepted_t = 0.
        else:
            accepted_t = float(np.log(aa / bb) / np.log(args.target_major / args.target_minor))
        if not -1e-12 <= accepted_t <= 1 + 1e-12:
            parser.error('Warm ellipse lies outside this axis-ratio path')
        if old['audits'][-1]['relative_metric_operator_sample_max'] > args.accept_metric:
            parser.error('Warm candidate exceeds the requested acceptance metric threshold')
        warm = args.warm_json
        report['accepted'].append(dict(t=accepted_t, file=str(warm), imported=True))
    step = args.initial_step
    started = time.perf_counter()
    environment = os.environ.copy()
    environment['OPENBLAS_NUM_THREADS'] = '1'
    for attempt in range(args.max_attempts):
        t = 0. if accepted_t is None else min(1., accepted_t + step)
        output = args.out_dir / f'{args.prefix}-attempt-{attempt:03d}-t{t:.6f}.json'
        cmd = command(args, t, output, warm)
        print(json.dumps(dict(event='continuation_stage', attempt=attempt, t=t,
                              axes=axes(t,args.target_major,args.target_minor)[:2], step=step)), flush=True)
        result = subprocess.run(cmd, env=environment, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
        record = dict(attempt=attempt, t=t, output=str(output), command=cmd,
                      process_returncode=result.returncode)
        if result.returncode != 0 or not output.exists():
            record['output_tail'] = result.stdout[-3000:]
            report['attempts'].append(record)
            report['status'] = 'solver_process_failed'
            save()
            break
        candidate = json.loads(output.read_text())
        audit = candidate['audits'][-1]
        accepted = (audit['relative_metric_operator_sample_max'] <= args.accept_metric
                    and audit['endpoint_two_jet_matching_sample_max'] < 1e-9
                    and audit['min_area_density_sample'] > 0)
        record.update(accepted=accepted,
                      metric=audit['relative_metric_operator_sample_max'],
                      principal_curvature_sample=audit['max_abs_principal_curvature_sample'],
                      tail=candidate['definition']['tail_final'],
                      solver=candidate['solver'])
        report['attempts'].append(record)
        if accepted:
            accepted_t = t
            warm = output
            report['accepted'].append(dict(t=t, file=str(output), metric=record['metric']))
            if t >= 1 - 1e-12:
                report['status'] = 'target_design_reached_requires_fixed_metric_refinement_and_geometry'
                report['target_design_reached'] = True
                save()
                break
            step = min(args.initial_step, step * 1.5)
        else:
            if accepted_t is None:
                report['status'] = 'exact_round_control_not_recovered'
                save()
                break
            step /= 2
            if step < args.min_step - 1e-15:
                report['status'] = 'design_continuation_stalled_at_minimum_step'
                save()
                break
        report['status'] = 'running'
        report['last_accepted_t'] = accepted_t
        report['last_accepted_candidate'] = str(warm) if warm else None
        report['elapsed_seconds'] = time.perf_counter() - started
        save()
        print(json.dumps(dict(event='continuation_result', t=t, accepted=accepted,
                              metric=record['metric'], next_step=step)), flush=True)
    else:
        report['status'] = 'design_attempt_budget_exhausted'
    report['last_accepted_t'] = accepted_t
    report['last_accepted_candidate'] = str(warm) if warm else None
    report['elapsed_seconds'] = time.perf_counter() - started
    save()
    print(json.dumps(dict(summary=str(summary_path), status=report['status'],
                          target_design_reached=report['target_design_reached'],
                          last_accepted_t=accepted_t)), flush=True)


if __name__ == '__main__':
    main()
