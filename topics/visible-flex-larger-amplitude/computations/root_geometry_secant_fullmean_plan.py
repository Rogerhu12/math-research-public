#!/usr/bin/env python3
"""Prepare full-mean common-grid secant screens from two accepted fields.

The supplied baseline plan must use the current accepted original field and
its complete common grid. Every candidate uses the unchanged production
secant constructor, original all-core restart and complete physical mean.
No new field, true-H tail, derivative matrix or accepted solution is computed
by this planner. Scale one/two mean one/two actual previous accepted steps.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-plan', type=Path, required=True)
    parser.add_argument('--previous-reference', type=Path, required=True)
    parser.add_argument('--previous-raw', type=Path, required=True)
    parser.add_argument('--scales', type=float, nargs='+', default=[2.,1.])
    parser.add_argument('--hold-initial-height', action='store_true')
    parser.add_argument('--out-prefix', type=Path, required=True)
    options = parser.parse_args()
    import strong_secant_actual_bvp_v2 as secant
    import root_actual_secant_geometry_complete_mean as adapter
    plan = json.loads(options.baseline_plan.read_text())
    if Path.cwd() != Path(plan['cwd']):
        raise ValueError('Preserve the exact baseline plan working directory')
    for path, wanted in plan['source_and_input_sha256'].items():
        if sha(path) != wanted:
            raise ValueError('A completed baseline plan source/input changed: '+path)
    baseline = next(row for row in plan['candidates'] if row['name'] == 'baseline')
    wrapper = Path(__file__).with_name('root_actual_secant_geometry_complete_mean.py').resolve()
    result = Path(str(options.out_prefix)+'-plan.json')
    if result.exists() or len(set(options.scales)) != len(options.scales):
        raise ValueError('Use a fresh output and distinct secant scales')
    hashes = dict(plan['source_and_input_sha256'])
    for path in (options.baseline_plan, options.previous_reference, options.previous_raw,
                 Path(__file__), wrapper, Path(secant.__file__)):
        hashes[str(path)] = sha(path)
    rows = []
    for ordinal, scale in enumerate(options.scales):
        row = copy.deepcopy(baseline)
        command = row['command']
        if any(flag in command for flag in ('--response-data','--neutral-control-step')):
            raise ValueError('Use a true zero-step current baseline plan')
        match = [i for i, token in enumerate(command)
                 if Path(token).name == 'root_actual_geometry_field_complete_mean.py']
        if len(match) != 1:
            raise ValueError('The baseline command must use the original complete-mean geometry wrapper')
        command[match[0]] = str(wrapper)
        if command.count('--target-core') != 1:
            raise ValueError('The baseline explicit core layout differs')
        index = command.index('--target-core')
        del command[index:index+4]
        name = 'secant'+str(ordinal)+'-scale'+format(scale, '.12g').replace('.', 'p')
        prefix = Path(str(options.out_prefix)+'-'+name)
        if list(prefix.parent.glob(prefix.name+'*')):
            raise FileExistsError('A secant candidate output already exists')
        paths = {key:Path(str(prefix)+suffix) for key,suffix in (
            ('report','-screen.json'),('resource','-resource.json'),
            ('field','-field.json'),('log','-log.txt'))}
        for flag, value in (('--out', paths['resource']), ('--out-prefix', prefix),
                            ('--inspect-warm-output', paths['report']),
                            ('--geometry-array', paths['field'])):
            command[command.index(flag)+1] = str(value)
        cfg = SimpleNamespace(secant_previous_reference=options.previous_reference,
            secant_previous_raw=options.previous_raw, secant_scale=scale,
            secant_hold_initial_height=options.hold_initial_height)
        record, warm = secant.prepare(cfg, command)
        grid = adapter.check_grid(record, command)
        hashes.update(record['source_sha256'])
        profile = dict(secant.read(record['current_reference'])['frozen_profile'])
        for field, step in record['external_shifts'].items():
            profile[field] += step
        for field, step in record['geometry_increment'].items():
            profile[field] += step
        command += ['--secant-previous-reference',str(options.previous_reference),
                    '--secant-previous-raw',str(options.previous_raw),
                    '--secant-scale',repr(scale)]
        if options.hold_initial_height:
            command += ['--secant-hold-initial-height']
        row.update(name=name, direction=None, step=None, secant_scale=scale,
            expected_core=record['target_core'], expected_profile=profile,
            command=command, original_secant=record, common_grid=grid,
            **{key:str(value) for key,value in paths.items()})
        rows.append(row)
    result.parent.mkdir(parents=True, exist_ok=True)
    result.write_text(json.dumps(dict(schema='actual-secanted-fullmean-geometry-plan-v1',
        scope=__doc__, prepared_only=True, executed=False, nonlinear_solution=False,
        new_tail_evaluation=False, cwd=plan['cwd'], grid=plan['grid'],
        geometry_wrapper=str(wrapper), source_and_input_sha256=hashes,
        baseline_core=plan['baseline_core'], modes=plan['modes'], directions=[],
        previous_reference=str(options.previous_reference), previous_raw=str(options.previous_raw),
        candidates=rows, selection_rule='Explicit positive scales of the two actual accepted fields.',
        original_full_production_mean_retained=True,
        limitations=['Unsolved physical-C2-cubic geometry samples only.',
                     'No true-H tail evaluation, continuous curvature, reach or complete closed-surface certificate.']),
        indent=2)+'\n')
    print(json.dumps(dict(plan=str(result), sha256=sha(result), cases=len(rows),
        original_current_parameter_count=rows[0]['common_grid']['original_parameter_count'],
        target_cores=[row['expected_core'] for row in rows])), flush=True)


if __name__ == '__main__':
    main()
