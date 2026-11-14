#!/usr/bin/env python3
"""Screen two exact saved actual-J neutral directions without a new BVP.

Every child uses the complete saved all-core field and the production
unsolved-warm inspector. The low three core coefficients are prescribed at
the accepted baseline. A changed physical profile is explicit. Neither the
affine tail tangent nor the C2 cubic geometry is an accepted new surface.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-command', type=Path, required=True)
    parser.add_argument('--response', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--step-scale', type=float, default=1.)
    parser.add_argument('--only-perturbations', action='store_true')
    args = parser.parse_args()
    if not math.isfinite(args.step_scale) or not 0 < args.step_scale <= 1:
        raise ValueError('The diagnostic step scale must lie in (0,1]')
    old = json.loads(args.baseline_command.read_text())
    command = old[old.index('--')+1:]
    i = command.index('--inspect-local-output')
    del command[i:i+2]
    command[0] = sys.executable
    response = json.loads(args.response.read_text())
    if (not response.get('finished') or response.get('new_solution') or
            response.get('schema') != 'fixed-actual-to-three-control-response-v1'):
        raise ValueError('Expected the completed actual fixed-control response')
    core = response['baseline']['core'][:3]
    i = command.index('--target-core')
    if list(map(float, command[i+1:i+4])) != core:
        raise ValueError('Baseline command low core differs')
    rows = {r['external_field']: r for r in response['additional_core_held_directions']}
    cases = [('baseline', {}), ('vu-plus', {'vu': .002}),
        ('vu-minus', {'vu': -.002}),
        ('firstk-plus', {'descending_turn_curvature': .025}),
        ('firstk-minus', {'descending_turn_curvature': -.025})]
    cases = [(name, {field: value*args.step_scale for field, value in shifts.items()})
        for name, shifts in cases if shifts or not args.only_perturbations]
    outputs = [args.out_prefix.with_suffix('.json'),
        args.out_prefix.with_name(args.out_prefix.name+'-plan.json'),
        args.out_prefix.with_name(args.out_prefix.name+'-ledger.jsonl')]
    if any(p.exists() for p in outputs):
        raise FileExistsError('Use a fresh output prefix')
    files = [Path(__file__), args.baseline_command, args.response, Path(command[1]),
        Path(command[1]).with_name('strong_actual_augmented_core.py'),
        Path(command[1]).with_name('strong_actual_warm_screen.py')]
    hashes = {str(p): sha(p) for p in files}
    plan = []
    for name, shifts in cases:
        prefix = args.out_prefix.with_name(args.out_prefix.name+'-'+name)
        report = prefix.with_name(prefix.name+'-screen.json')
        resource = prefix.with_name(prefix.name+'-resource.json')
        log = prefix.with_name(prefix.name+'-log.txt')
        current = command.copy()
        current[current.index('--out-prefix')+1] = str(prefix)
        current += ['--response-data', str(args.response),
            '--inspect-warm-output', str(report), '--max-nodes', '2400']
        expected = dict(response['baseline']['profile'])
        for field, step in shifts.items():
            current += ['--neutral-control-step', field+'='+repr(step)]
            for key, derivative in rows[field]['physical_profile_derivative'].items():
                expected[key] += step*derivative
        wrapped = [sys.executable, str(Path(command[1]).with_name('strong_resource_run.py')),
            '--out', str(resource), '--', *current]
        plan.append(dict(name=name, shifts=shifts, command=wrapped,
            expected_profile=expected, report=str(report), resource=str(resource), log=str(log)))
    outputs[1].write_text(json.dumps(dict(scope=__doc__, source_sha256=hashes,
        baseline_low_core=core, step_scale=args.step_scale,
        only_perturbations=args.only_perturbations, candidates=plan), indent=2)+'\n')
    results = []
    begin = time.monotonic()
    for row in plan:
        print(json.dumps(dict(event='neutral_geometry_begin', name=row['name'])), flush=True)
        with Path(row['log']).open('w') as stream:
            completed = subprocess.run(row['command'], stdout=stream, stderr=subprocess.STDOUT)
        row['exitcode'] = completed.returncode
        if completed.returncode:
            with outputs[2].open('a') as stream:
                stream.write(json.dumps(row)+'\n')
            raise RuntimeError('Neutral geometry child failed: '+row['name'])
        result = json.loads(Path(row['report']).read_text())
        if (not result.get('finished') or result.get('nonlinear_solution') or
                result.get('true_new_H_tail_evaluated') or result.get('worker_start_attempts')):
            raise ValueError('Unsolved inspection scope changed')
        for field, value in row['expected_profile'].items():
            actual = result['warm_profile'][field]
            if isinstance(value, (float, int)):
                if abs(actual-value) > 3e-14:
                    raise ValueError('Full response profile differs: '+field)
            elif actual != value:
                raise ValueError('Physical profile label differs: '+field)
        row.update(finite_domain_passed=result['finite_domain_passed'],
            report_sha256=sha(row['report']),
            full_collocation=result.get('full_collocation'),
            geometry=result.get('warm_physical_cubic_geometry'))
        results.append(row)
        with outputs[2].open('a') as stream:
            stream.write(json.dumps(row)+'\n')
        geometry = row['geometry'] or {}
        print(json.dumps(dict(event='neutral_geometry_complete', name=row['name'],
            domain=row['finite_domain_passed'], diameter=geometry.get('diameter_sample'),
            kappa_D=geometry.get('kappa_times_D_sample'),
            seconds=time.monotonic()-begin)), flush=True)
    outputs[0].write_text(json.dumps(dict(scope=__doc__, finished=True,
        nonlinear_solution=False, source_sha256=hashes, cases=results,
        seconds=time.monotonic()-begin), indent=2)+'\n')


if __name__ == '__main__':
    main()
