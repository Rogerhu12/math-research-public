#!/usr/bin/env python3
"""Continuous real support/zeta gates for the exact affine R57 family.

Extends the frozen CoreTarget only by the actual affine phase/mean direction.
The exact height primitive is varied as well: leaving it at the origin while
changing the slope would define another graph. No rounded family point is
substituted. The direct interval DFT, full primitive tail, angular gap, and
closed-span radial bounds are inherited unchanged.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from fourfold_phase_core_interval import CoreTarget, ClosedSpline, primitive_spline
from fourfold_phase_parameter_root_interval import AffineClosedSpline
from fourfold_phase_root_interval import Box
from fourfold_phase_uniform_tail import down


class AffineCoreTarget(CoreTarget):
    def __init__(self, frozen, direction, parameter, nodes=256, angular_nodes=4096):
        super().__init__(frozen, nodes, angular_nodes)
        delta = Box(*parameter)
        self.phase = AffineClosedSpline(self.phase, ClosedSpline(
            frozen['phase_knots'], 5, direction['phase_direction_coefficients']), delta)
        self.alpha = [Box(a)+delta*d for a, d in
                      zip(frozen['alpha'], direction['alpha_direction'])]
        height_knots = frozen['height0_slope_knots']
        height_degree = int(frozen['height0_slope_degree'])
        variation = Box(np.zeros_like(frozen['height0_slope_coefficients']))
        for j, d in enumerate(direction['alpha_direction'], 1):
            if not np.array_equal(height_knots, frozen[f'height{j}_slope_knots']):
                raise ValueError('height direction knots differ')
            if height_degree != int(frozen[f'height{j}_slope_degree']):
                raise ValueError('height direction degrees differ')
            variation = variation + Box(d)*Box(frozen[f'height{j}_slope_coefficients'])
        direction_primitive = primitive_spline(height_knots, height_degree, variation)
        self.height_primitive = AffineClosedSpline(self.height_primitive,
                                                   direction_primitive, delta)

    def evaluate_affine_core(self, left, right):
        row = self.evaluate_core(left, right)
        # J=F dot (Ftheta cross Fx)>0 implies area>=J/|F|>0.
        if row['support_numerator_lower'] > 0:
            row['area_lower_from_support'] = float(down(
                row['support_numerator_lower']/row['F_norm_upper']))
        else:
            row['area_lower_from_support'] = None
        row['passed'] = bool(row['passed'] and row['a'][0] > 0)
        return row


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--frozen-direction', type=Path, required=True)
    ap.add_argument('--parameter-left', type=float, default=-.01)
    ap.add_argument('--parameter-right', type=float, default=.01)
    ap.add_argument('--core', type=float, default=.24)
    ap.add_argument('--quarter-nodes', type=int, default=256)
    ap.add_argument('--angular-nodes', type=int, default=4096)
    ap.add_argument('--minimum-width', type=float, default=1e-5)
    ap.add_argument('--max-cells', type=int, default=10000)
    ap.add_argument('--resume', action='store_true')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if not 0 < args.core < 1 or args.parameter_left > args.parameter_right:
        raise ValueError('invalid core or real parameter interval')
    with np.load(args.inputs, allow_pickle=False) as stored:
        frozen = {key: stored[key].copy() for key in stored.files}
    with np.load(args.frozen_direction, allow_pickle=False) as stored:
        direction = {key: stored[key].copy() for key in stored.files}
    origin_sha, direction_sha = digest(args.inputs), digest(args.frozen_direction)
    metadata = json.loads(str(direction['metadata']))
    if metadata['origin_inputs_sha256'] != origin_sha:
        raise ValueError('affine direction belongs to a different exact origin')
    if (direction['phase_direction_coefficients'].shape != frozen['phase_coefficients'].shape
            or direction['alpha_direction'].shape != frozen['alpha'].shape):
        raise ValueError('affine direction dimensions differ from origin')
    parameter = [args.parameter_left, args.parameter_right]
    dependencies = {name: digest(Path(__file__).with_name(name)) for name in [
        'fourfold_phase_core_interval.py', 'fourfold_phase_parameter_root_interval.py',
        'fourfold_phase_core_N_interval.py', 'fourfold_phase_root_interval.py',
        'fourfold_phase_uniform_tail.py', 'fourfold_interval_scalar.py']}
    config = dict(origin_inputs_sha256=origin_sha, frozen_direction_sha256=direction_sha,
                  source_sha256=digest(Path(__file__)), dependency_sha256=dependencies,
                  parameter_interval=parameter, core=args.core,
                  quarter_nodes=args.quarter_nodes, angular_nodes=args.angular_nodes,
                  minimum_width=args.minimum_width)
    target = AffineCoreTarget(frozen, direction, parameter,
                              args.quarter_nodes, args.angular_nodes)
    cuts = np.unique(np.concatenate([np.array([0., args.core])]+[
        np.r_[value, -value] for key, value in frozen.items() if key.endswith('_knots')]))
    cuts = cuts[(cuts >= 0)&(cuts <= args.core)]
    queue = deque([float(left), float(right)] for left, right in zip(cuts[:-1], cuts[1:]))
    initial = len(queue)
    rows, failures, attempts, elapsed_previous = [], [], 0, 0.
    if args.resume and args.out.exists():
        old = json.loads(args.out.read_text())
        if old['configuration'] != config:
            raise ValueError('resume input/direction/source/dependency configuration changed')
        queue = deque(old['pending'])
        rows, failures = old['cells'], old['failed_cells']
        attempts, elapsed_previous = old['attempts'], old['elapsed_seconds']
    started = time.monotonic()

    def exact_coverage():
        cursor, end = Fraction(0), Fraction.from_float(args.core)
        for row in sorted(rows, key=lambda value: value['radial_interval'][0]):
            left, right = map(Fraction.from_float, row['radial_interval'])
            if left != cursor or not left < right <= end:
                return False
            cursor = right
        return cursor == end

    def save():
        covered = exact_coverage()
        complete = bool(not queue and not failures and covered)
        report = dict(kind='continuous_real_core_support_zeta_for_exact_affine_R57_family',
                      configuration=config, family=metadata['family'],
                      exact_parameter_fractions=[str(Fraction.from_float(v)) for v in parameter],
                      radial_core=[-args.core, args.core], initial_radial_cells=initial,
                      attempts=attempts, elapsed_seconds=elapsed_previous+time.monotonic()-started,
                      pending=list(queue), cells=rows, failed_cells=failures,
                      exact_dyadic_radial_coverage=covered, complete=complete,
                      proved_continuous_real_N_support_zeta=complete,
                      geometry=('physical a,beta explicitly even; gamma,Z explicitly odd; '
                                'Z is the exact affine height-slope integral; infinite R33 primitive'),
                      normal_orientation='nu=(Ftheta cross Fx)/area',
                      definitions=dict(Nraw='-a^2 Fx dot (T cross Ttheta)',
                                       N='Nraw/area',
                                       h='F dot nu=J/area',
                                       zeta='h/|F|=J/(area |F|)',
                                       J='a F dot (T cross Fx)'),
                      limitations=['Only the specified real affine parameter/core box',
                          'Not the larger independent control box and not a rounded checkpoint',
                          'No complex tube, actual-Gaussian-curvature classification, or ODE residual proof',
                          'No cap, full-frequency PDE inverse, or closed isometric-family proof'])
        if rows:
            report.update(raw_N_upper=max(r['raw_N_upper'] for r in rows),
                          normalized_N_upper=max(r['normalized_N_upper'] for r in rows),
                          support_numerator_lower=min(r['support_numerator_lower'] for r in rows),
                          support_lower=min(r['support_lower'] for r in rows),
                          zeta_lower=min(r['zeta_lower'] for r in rows),
                          area_lower_from_support=min(r['area_lower_from_support'] for r in rows),
                          area_upper=max(r['area_upper'] for r in rows),
                          F_norm_upper=max(r['F_norm_upper'] for r in rows),
                          Fx_norm_upper=max(r['Fx_norm_upper'] for r in rows),
                          minimum_a=min(r['a'][0] for r in rows),
                          maximum_F_primitive_tail=max(r['F_primitive_tail'] for r in rows),
                          maximum_Fx_primitive_tail=max(r['Fx_primitive_tail'] for r in rows))
        args.out.parent.mkdir(parents=True, exist_ok=True)
        tmp = args.out.with_suffix(args.out.suffix+'.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.out)
        return report

    while queue and attempts < args.max_cells:
        left, right = queue.popleft()
        attempts += 1
        try:
            row = target.evaluate_affine_core(left, right)
        except (ValueError, ZeroDivisionError) as error:
            row = dict(radial_interval=[left, right], passed=False, error=str(error))
        if row['passed']:
            rows.append(row)
        elif right-left > args.minimum_width:
            middle = float((Fraction.from_float(left)+Fraction.from_float(right))/2)
            if left < middle < right:
                queue.appendleft([middle, right])
                queue.appendleft([left, middle])
            else:
                failures.append(row)
        else:
            failures.append(row)
        if attempts % 10 == 0 or not row['passed'] or not queue:
            report = save()
            print(json.dumps(dict(attempts=attempts, accepted=len(rows), pending=len(queue),
                                  failed=len(failures), x=[left, right],
                                  Nraw=row.get('raw_N_upper'), zeta=row.get('zeta_lower'),
                                  elapsed_seconds=report['elapsed_seconds'])), flush=True)
    report = save()
    print(json.dumps({k: v for k, v in report.items() if k not in
                      ['pending', 'cells', 'failed_cells']}, indent=2), flush=True)
    if not report['complete']:
        raise SystemExit('affine real-core proof incomplete; inspect failures or resume')


if __name__ == '__main__':
    main()
