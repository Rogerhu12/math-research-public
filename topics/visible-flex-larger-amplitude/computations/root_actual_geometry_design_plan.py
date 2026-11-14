#!/usr/bin/env python3
"""Prepare complete common-grid geometry fields for five saved actual-J columns.

This creates commands only. All eleven cases are unsolved warm diagnostics;
they use the full original raw cubic and the complete production mean.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--neutral-plan', type=Path, required=True)
    ap.add_argument('--response', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    response = json.loads(args.response.read_text())
    if (not response.get('finished') or response.get('new_solution') or
            response.get('schema') != 'fixed-actual-to-three-control-response-v1'):
        raise ValueError('A completed actual-J response is required')
    plan = json.loads(args.neutral_plan.read_text())
    old = plan['candidates'][0]['command']
    command = old[old.index('--')+1:]
    command[0] = sys.executable
    command[1] = str(Path(__file__).with_name('root_actual_geometry_field.py'))
    for flag in ('--neutral-control-step', '--inspect-warm-output', '--response-data'):
        while flag in command:
            i = command.index(flag)
            del command[i:i+2]
    raw_path = Path(command[command.index('--actual-reference-raw')+1])
    with gzip.open(raw_path, 'rt') as stream:
        raw = json.load(stream)
    # The raw reader owns array chunks; the coordinate metadata remains in
    # its main packet. Never substitute a lower-mode or resampled raw state.
    import numpy as np
    from strong_actual_fixed_control_response import raw_flat
    coordinate_hashes = {}
    x = np.asarray(raw_flat(raw_path, raw, 'x', coordinate_hashes), dtype=float)
    x = x.reshape(raw['arrays']['x']['shape'])
    if x[0] != 0 or x[-1] != 1 or not np.all(np.diff(x) > 0):
        raise ValueError('Unexpected original computational coordinate')
    grid = np.unique(np.r_[x[::4], x[-1], np.linspace(0, 1, 129)])
    prefix = args.out_prefix
    grid_path = prefix.with_name(prefix.name+'-grid.json')
    plan_path = prefix.with_name(prefix.name+'-plan.json')
    if grid_path.exists() or plan_path.exists():
        raise FileExistsError('Use a fresh plan prefix')
    core = response['baseline']['core'][:3]
    i = command.index('--target-core')
    if list(map(float, command[i+1:i+4])) != core:
        raise ValueError('The baseline core and command differ')
    directions = [('actual_q1', .001), ('actual_q4', .00003),
                  ('actual_c6', .000002), ('vu', .0002),
                  ('descending_turn_curvature', .0025)]
    cases = [('baseline', None, 0.)]
    for name, step in directions:
        cases.extend([(name+'-plus', name, step), (name+'-minus', name, -step)])
    planned = []
    response_rows = {r['direction']: r for r in response['prescribed_low_core_responses']}
    response_rows.update({r['external_field']: r for r in response['additional_core_held_directions']})
    for name, direction, step in cases:
        case = prefix.with_name(prefix.name+'-'+name)
        report = case.with_name(case.name+'-screen.json')
        field = case.with_name(case.name+'-field.npy.gz')
        resource = case.with_name(case.name+'-resource.json')
        current = command.copy()
        current[current.index('--out-prefix')+1] = str(case)
        target = core.copy()
        profile = dict(response['baseline']['profile'])
        if direction is not None:
            if direction in ('actual_q1', 'actual_q4', 'actual_c6'):
                target[('actual_q1', 'actual_q4', 'actual_c6').index(direction)] += step
            else:
                current += ['--neutral-control-step', direction+'='+repr(step)]
            for key, value in response_rows[direction]['physical_profile_derivative'].items():
                profile[key] += step*value
        i = current.index('--target-core')
        current[i+1:i+4] = list(map(repr, target))
        current += ['--response-data', str(args.response), '--inspect-warm-output', str(report),
                    '--geometry-grid', str(grid_path), '--geometry-array', str(field)]
        wrapped = [sys.executable, str(Path(__file__).with_name('strong_resource_run.py')),
                   '--out', str(resource), '--', *current]
        planned.append(dict(name=name, direction=direction, step=step, command=wrapped,
                            expected_core=target, expected_profile=profile, report=str(report),
                            field=str(field), resource=str(resource),
                            log=str(case.with_name(case.name+'-log.txt'))))
    grid_path.write_text(json.dumps(dict(numerical_t=grid.tolist(), angular=192,
        grid_only=True, all_original_raw_nodes_used_in_cubic=True,
        raw_sha256=digest(raw_path), rule='Every fourth original node plus uniform129 and both endpoints'),
        indent=2)+'\n')
    hashes = {str(p): digest(p) for p in (Path(__file__), Path(command[1]), args.neutral_plan,
                                        args.response, raw_path, grid_path)}
    hashes.update(coordinate_hashes)
    plan_path.write_text(json.dumps(dict(scope=__doc__, executed=False,
        nonlinear_solution=False, new_tail_evaluation=False, grid=str(grid_path),
        source_and_input_sha256=hashes, baseline_core=core,
        directions=[dict(name=n, step=s) for n, s in directions], candidates=planned,
        limitations=['Finite geometry samples and first-order warm fields only.',
                     'No accepted BVP, reach certificate, closed diameter or uniform parameter claim.']),
        indent=2)+'\n')
    print(json.dumps(dict(plan=str(plan_path), sha256=digest(plan_path),
                          cases=len(planned), radial=len(grid), angular=192)))


if __name__ == '__main__':
    main()
