#!/usr/bin/env python3
"""Prepare one complete warm geometry re-evaluation of a finite LP choice.

The five saved actual-J fields are combined by the original production warm
constructor. No fitted geometry, accepted nonlinear state, new tail response,
closed diameter or reach certificate is inferred from the LP prediction.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan', type=Path, required=True)
    ap.add_argument('--lp', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    plan = json.loads(args.plan.read_text())
    lp = json.loads(args.lp.read_text())
    if (lp['plan_sha256'] != sha(args.plan) or lp['grid_sha256'] != sha(plan['grid'])
            or lp['source_sha256'] != sha(Path(__file__).with_name('root_geometry_streaming_lp_resident.py'))
            or lp['accepted_nonlinear_solution'] or lp['continuous_geometry_certified']
            or lp['actual_reach_certified']):
        raise ValueError('The complete finite diagnostic identity or scope differs')
    for item in lp['inputs']:
        if sha(item['path']) != item['sha256']:
            raise ValueError('A completed LP input changed: ' + item['path'])
    for path, digest in plan['source_and_input_sha256'].items():
        if sha(path) != digest:
            raise ValueError('An original geometry source changed: ' + path)
    candidates = [(i, c) for i, c in enumerate(lp['candidates'])
                  if c.get('success') and c.get('all_finite_rows_checked')]
    if not candidates:
        raise ValueError('No original all-row LP choice is feasible')
    index, selected = min(candidates, key=lambda item: (
        -item[1]['normalized_steps'][0],
        item[1]['predicted_max_abs_curvature'] * item[1]['predicted_max_twice_radius']))
    names = ['actual_q1', 'actual_q4', 'actual_c6', 'vu', 'descending_turn_curvature']
    if [d['name'] for d in plan['directions']] != names:
        raise ValueError('The original complete five-direction plan is required')
    steps = selected['physical_steps']
    for j, d in enumerate(plan['directions']):
        value = steps[d['name']] / d['step']
        if not (-1e-12 if j == 0 else -1-1e-12) <= value <= 1+1e-12:
            raise ValueError('The finite local trust bounds differ')
    baseline = next(row for row in plan['candidates'] if row['name'] == 'baseline')
    row = copy.deepcopy(baseline)
    command = row['command']
    response_path = Path(command[command.index('--response-data')+1])
    response = json.loads(response_path.read_text())
    responses = {r['direction']: r for r in response['prescribed_low_core_responses']}
    responses.update({r['external_field']: r for r in response['additional_core_held_directions']})
    target = list(plan['baseline_core'])
    profile = dict(response['baseline']['profile'])
    for j, name in enumerate(names):
        step = steps[name]
        if j < 3:
            target[j] += step
        elif step:
            command += ['--neutral-control-step', name + '=' + repr(step)]
        for key, derivative in responses[name]['physical_profile_derivative'].items():
            profile[key] += step * derivative
    prefix = args.out_prefix.with_name(args.out_prefix.name + '-combined')
    output = args.out_prefix.with_name(args.out_prefix.name + '-plan.json')
    if output.exists() or list(prefix.parent.glob(prefix.name + '*')):
        raise FileExistsError('Require a fresh complete combined-candidate prefix')
    report = str(prefix.with_name(prefix.name + '-screen.json'))
    resource = str(prefix.with_name(prefix.name + '-resource.json'))
    field = str(prefix.with_name(prefix.name + '-field.json'))
    for flag, value in [('--out', resource), ('--out-prefix', str(prefix)),
                        ('--inspect-warm-output', report), ('--geometry-array', field)]:
        command[command.index(flag)+1] = value
    start = command.index('--target-core') + 1
    command[start:start+3] = list(map(repr, target))
    row.update(name='combined', direction=None, step=None, command=command,
               expected_core=target, expected_profile=profile, report=report,
               field=field, resource=resource,
               log=str(prefix.with_name(prefix.name+'-log.txt')),
               complete_physical_steps=steps)
    hashes = dict(plan['source_and_input_sha256'])
    hashes.update({str(args.plan): sha(args.plan), str(args.lp): sha(args.lp),
                   str(Path(__file__)): sha(__file__)})
    result = dict(scope=__doc__, executed=False, nonlinear_solution=False,
                  new_tail_evaluation=False, grid=plan['grid'],
                  geometry_wrapper=plan['geometry_wrapper'], source_and_input_sha256=hashes,
                  baseline_core=plan['baseline_core'], directions=plan['directions'],
                  candidates=[row], selected_lp_candidate_index=index,
                  selected_lp_candidate=selected,
                  selection_rule='Largest finite normalized q1 step, then smallest predicted sampled curvature-times-radius among returned LP choices',
                  limitations=plan['limitations'])
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(plan=str(output), sha256=sha(output),
                          lp_candidate=index, physical_steps=steps)))


if __name__ == '__main__':
    main()
