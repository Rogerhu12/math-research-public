#!/usr/bin/env python3
"""Compact a completed three-stage, four-term RK addition comparison.

Only stored numeric identities and execution provenance are checked here.
No RHS, flow, nonlinear tail, or prefix calculation is repeated.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
from record_fixed_actual import load, scalar_tree, sha
from record_tail_initialization import numeric_identity


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def numeric_sha(values):
    return hashlib.sha256(packed(values)).hexdigest()


def identity(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('summary', 'resource', 'log', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    s, resource = load(a.summary), load(a.resource)
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('The controlled comparison needs an observed successful terminal')
    if s['states_changed'] or s['checkpoint_written'] or s['full_tail_replay_performed'] or s['nonlinear_solver_invoked']:
        raise ValueError('Only the declared read-only three-stage scope is supported')
    if s['named_stages'] != [43, 38, 175] or s['originalGate'] != 2e-9:
        raise ValueError('The predefined rows or original gate changed')
    for key in ('source_sha256', 'additional_current_root_source_sha256'):
        for path, digest in s[key].items():
            if sha(path) != digest:
                raise ValueError('A bound comparison source changed: '+path)
    raw = {}
    for key in ('fixtures', 'original', 'compensated'):
        if sha(s[key]['path']) != s[key]['sha256']:
            raise ValueError('An original arithmetic output identity changed')
        raw[key] = load(s[key]['path'])
    cp = load(s['input'])
    if sha(s['input']) != s['input_sha256'] or not cp['response'].get('failed'):
        raise ValueError('Exact original failed state required')
    if numeric_sha([x for row in cp['response']['checkpoint']['states'] for x in row]) != s['complete_input_states_sha256']:
        raise ValueError('The complete source state identity differs')
    for data in raw.values():
        if numeric_identity(data['config']) != numeric_identity(cp['config']):
            raise ValueError('The original configuration differs between arms')
        if data['input_sha256'] != s['input_sha256'] or data['source_sha256'] != s['source_sha256']:
            raise ValueError('An arm uses different source state or mathematical code')
    for key, value in raw['fixtures']['trig'].items():
        if numeric_sha([x for row in value for x in row]) != s['trig_float64_le_sha256'][key]:
            raise ValueError('A frozen trigonometric constant identity differs')
    for fixture, old, new, result in zip(raw['fixtures']['fixtures'], raw['original']['rows'],
                                       raw['compensated']['rows'], s['named_results'], strict=True):
        if len(fixture['initial42']) != 42 or len(old['reference42']) != 42 or len(new['state']) != 42:
            raise ValueError('All 40 shooting and both mean outputs must be retained')
        actual = cp['response']['checkpoint']['states'][fixture['inputNode']] + [0., 0.]
        if packed(actual) != packed(fixture['initial42']):
            raise ValueError('The entire original 42-component stage input differs')
        if not packed(old['reference42']) == packed(old['manualPlain42']) == packed(old['state']):
            raise ValueError('The ordinary RK baseline fails complete bitwise identity')
        for field in ('stage', 'inputNode', 'input42_sha256', 'targetNode40_sha256',
                      'grid_sha256', 'sampled_original_geometry_sha256'):
            if len({json.dumps(row[field]) for row in (fixture, old, new, result)}) != 1:
                raise ValueError('Original stage identity changed between arms: '+field)
        if numeric_sha(old['reference42']) != result['original_output42_sha256']:
            raise ValueError('Original 42-output hash differs')
        if numeric_sha(new['state']) != result['compensated_output42_sha256']:
            raise ValueError('Compensated 42-output hash differs')
        if (old['residual']['normalizedResidual'] != result['original_normalized_residual'] or
                new['residual']['normalizedResidual'] != result['compensated_normalized_residual']):
            raise ValueError('Recorded stage scalar result differs')
    result = dict(
        scope='Completed read-only arithmetic comparison at three fixed stages. The only variant is Neumaier addition of the final four RK slope terms; it is not end-to-end higher precision or a true-ODE error certificate.',
        collector=identity(__file__),
        collector_helpers={name: sha(Path(__file__).with_name(name)) for name in
                           ('record_fixed_actual.py', 'record_tail_initialization.py')},
        input=dict(path=s['input'], sha256=s['input_sha256']),
        full_summary=identity(a.summary), frozen_input_fixture=s['fixtures'],
        original_arithmetic_output=s['original'], compensated_arithmetic_output=s['compensated'],
        command=s['command'],
        original_discretization={k: s[k] for k in
            ('modes', 'spacing', 'quadrature', 'independent_quadrature_nodes', 'steps', 'stage_count', 'originalGate')},
        source_sha256=s['source_sha256'],
        additional_current_root_source_sha256=s['additional_current_root_source_sha256'],
        additional_source_scope=s['additional_source_scope'],
        complete_input_states_sha256=s['complete_input_states_sha256'],
        complete_cut_height_sha256=s['complete_cut_height_sha256'],
        trig_float64_le_sha256=s['trig_float64_le_sha256'],
        all_three_baselines_all42_bitwise_identical=True,
        named_results={str(row['stage']): row for row in s['named_results']},
        all_named_peak_flow_values_unchanged=all(row['original_flow_change_at_named_component'] == 0
                                               for row in s['named_results']),
        all_three_stage_maxima_unchanged=all(row['original_normalized_residual'] == row['compensated_normalized_residual']
                                           for row in s['named_results']),
        conclusion='The declared four-term addition change does alter some finite outputs, but it leaves all three named original peaks and stage maxima unchanged. It supplies no improvement of these two above-gate high-mode stages and no reason to install this variant in the production worker. Other arithmetic operations have not been tested by this comparison.',
        comparison_loop_seconds=s['seconds'],
        resource=scalar_tree(resource), resource_identity=identity(a.resource),
        execution_log_sha256=sha(a.log),
        resource_scope='Comparison-loop timing excludes setup; observer timing includes the whole child. Sampled namespace RSS and RUSAGE_CHILDREN remain separate observations, not whole-host peaks.',
        states_changed=False, checkpoint_written=False, full_tail_replay_performed=False,
        nonlinear_solver_invoked=False,
        data_policy='Only three named scalar outcomes and original source/input/output identities are published. Full states, trig constants, sampled geometry and raw stage outputs remain scratch-only.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    if a.out.stat().st_size >= 100000:
        raise ValueError('Compact record must stay below 100 KB')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
