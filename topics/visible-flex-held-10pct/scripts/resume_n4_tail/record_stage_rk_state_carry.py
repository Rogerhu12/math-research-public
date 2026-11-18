#!/usr/bin/env python3
"""Compact the completed three-stage final-state Kahan carry comparison.

Only stored identities and execution provenance are checked here. No RHS,
flow, nonlinear tail, or prefix calculation is repeated.
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


def require_equal(first, second, description):
    if numeric_identity(first) != numeric_identity(second):
        raise ValueError(description)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('summary', 'resource', 'log', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError('Do not overwrite a completed record')
    s, resource = load(a.summary), load(a.resource)
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('The comparison needs an observed successful terminal')
    if any(s[key] for key in ('states_changed', 'checkpoint_written',
                             'full_tail_replay_performed', 'nonlinear_solver_invoked')):
        raise ValueError('Only the declared read-only three-stage scope is supported')
    if s['named_stages'] != [43, 38, 175] or s['originalGate'] != 2e-9:
        raise ValueError('The prescribed rows or original gate changed')
    for key in ('source_sha256', 'additional_current_root_source_sha256'):
        for path, digest in s[key].items():
            if sha(path) != digest:
                raise ValueError('A bound comparison source changed: '+path)
    raw = {}
    for key in ('inherited_fixture', 'fixtures', 'original', 'compensated'):
        if sha(s[key]['path']) != s[key]['sha256']:
            raise ValueError('An original arithmetic input/output identity changed')
        raw[key] = load(s[key]['path'])
    for path, digest in raw['inherited_fixture']['source_sha256'].items():
        if sha(path) != digest:
            raise ValueError('An inherited fixture source changed: '+path)
    cp = load(s['input'])
    if sha(s['input']) != s['input_sha256'] or not cp['response'].get('failed'):
        raise ValueError('Exact original failed state required')
    checkpoint = cp['response']['checkpoint']
    if numeric_sha([x for row in checkpoint['states'] for x in row]) != s['complete_input_states_sha256']:
        raise ValueError('The complete source state identity differs')
    if numeric_sha(checkpoint['cutHeight']) != s['complete_cut_height_sha256']:
        raise ValueError('The complete original physical cut height differs')
    for name, data in raw.items():
        require_equal(data['config'], cp['config'], 'The original configuration differs: '+name)
        if data['input_sha256'] != s['input_sha256']:
            raise ValueError('An arm or fixture uses a different source state')
        if name != 'inherited_fixture' and data['source_sha256'] != s['source_sha256']:
            raise ValueError('The comparison arms use different mathematical code')
    require_equal(raw['fixtures']['trig'], raw['inherited_fixture']['trig'],
                  'The inherited trig constants changed')
    for key, value in raw['fixtures']['trig'].items():
        if numeric_sha([x for row in value for x in row]) != s['trig_float64_le_sha256'][key]:
            raise ValueError('A frozen trigonometric constant identity differs')
    for fixture, inherited, old, new, result in zip(
            raw['fixtures']['fixtures'], raw['inherited_fixture']['fixtures'],
            raw['original']['rows'], raw['compensated']['rows'], s['named_results'], strict=True):
        require_equal(fixture, inherited, 'An inherited stage input/grid/geometry fixture changed')
        if (len(fixture['initial42']) != 42 or len(fixture['targetNode40']) != 40 or
                len(old['reference42']) != 42 or len(new['state']) != 42 or len(new['carry']) != 42):
            raise ValueError('All 40 shooting and both mean outputs/carries must be retained')
        actual = checkpoint['states'][fixture['inputNode']] + [0., 0.]
        if packed(actual) != packed(fixture['initial42']):
            raise ValueError('The complete original 42-component stage input differs')
        target = checkpoint['states'][fixture['stage']]
        if packed(target) != packed(fixture['targetNode40']):
            raise ValueError('The complete original target node differs')
        if not packed(old['reference42']) == packed(old['manualPlain42']) == packed(old['state']):
            raise ValueError('The ordinary RK baseline fails complete bitwise identity')
        if any(old['carry']) or old['changedStateUpdates'] or old['maximumCarry']:
            raise ValueError('The baseline unexpectedly used a state carry')
        for field in ('stage', 'inputNode', 'input42_sha256', 'targetNode40_sha256',
                      'grid_sha256', 'sampled_original_geometry_sha256'):
            if len({json.dumps(row[field]) for row in (fixture, old, new, result)}) != 1:
                raise ValueError('Original stage identity changed between arms: '+field)
        if numeric_sha(old['reference42']) != result['original_output42_sha256']:
            raise ValueError('Original 42-output hash differs')
        if numeric_sha(new['state']) != result['compensated_output42_sha256']:
            raise ValueError('Compensated 42-output hash differs')
        if numeric_sha(new['carry']) != result['final_carry42_sha256']:
            raise ValueError('Auxiliary carry identity differs')
        for data, prefix in ((old, 'original'), (new, 'compensated')):
            out = [v if j < 20 else v/fixture['portRatio'] for j, v in enumerate(data['state'][:40])]
            signed = [v-target[j] for j, v in enumerate(out)]
            norm = max(abs(v)/fixture['normalizationScale'] for v in signed)
            require_equal(out, data['residual']['out'], 'Stored physical flow differs')
            require_equal(signed, data['residual']['signed'], 'Stored residual differs')
            if norm != data['residual']['normalizedResidual'] or norm != result[prefix+'_normalized_residual']:
                raise ValueError('Recorded stage scalar residual differs')
        differences = [x-y for x, y in zip(new['state'], old['reference42'], strict=True)]
        if (max(map(abs, differences)) != result['maximum_output42_absolute_change'] or
                max(map(abs, differences[40:])) != result['maximum_mean2_absolute_change'] or
                sum(v != 0 for v in differences) != result['changed_output42_components'] or
                max(map(abs, new['carry'])) != result['maximum_final_auxiliary_carry'] or
                new['maximumCarry'] != result['maximum_auxiliary_carry']):
            raise ValueError('Stored complete-output/carry scalar differs')
    results = s['named_results']
    result = dict(
        scope='Completed read-only comparison of three original stages. Restore ordinary four-term RK slope sums; change only final state-plus-increment additions to a per-component Kahan carry, zeroed at the start of each stage. RHS and intermediate formulas read the rounded Float64 state only. Carries are arithmetic auxiliaries, not physical unknowns; in real arithmetic they remain zero.',
        arithmetic_limit='This is neither end-to-end higher precision nor a true-ODE error certificate. A smaller residual against a fixed finite target does not by itself certify a more accurate flow.',
        collector=identity(__file__),
        collector_helpers={name: sha(Path(__file__).with_name(name)) for name in
                           ('record_fixed_actual.py', 'record_tail_initialization.py')},
        input=dict(path=s['input'], sha256=s['input_sha256']),
        full_summary=identity(a.summary), inherited_input_fixture=s['inherited_fixture'],
        inherited_probe_sha256=s['inherited_probe_sha256'], frozen_input_fixture=s['fixtures'],
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
        inherited_fixture_complete_numeric_identity=True,
        all_three_baselines_all42_bitwise_identical=True,
        named_results={str(row['stage']): row for row in results},
        all_three_stage_maxima_improved=all(row['compensated_normalized_residual'] < row['original_normalized_residual']
                                          for row in results),
        all_three_stage_maxima_below_original_gate=all(row['compensated_normalized_residual'] < s['originalGate']
                                                     for row in results),
        conclusion='Final state accumulation changes the selected finite flow residuals materially but not uniformly: both formerly above-gate stages improve and remain above the original gate; the formerly below-gate control stage becomes above-gate. This gives no reason to install this variant in the production worker and does not establish which flow is closer to the exact finite-discretization or continuous solution.',
        comparison_loop_seconds=s['seconds'],
        resource=scalar_tree(resource), resource_identity=identity(a.resource),
        execution_log_sha256=sha(a.log),
        resource_scope='Comparison-loop timing excludes setup; observer timing includes the whole child. Sampled namespace RSS and RUSAGE_CHILDREN remain separate observations, not whole-host peaks.',
        source_checkpoint_states_changed=False, checkpoint_written=False,
        full_tail_replay_performed=False, nonlinear_solver_invoked=False,
        production_worker_changed=False,
        data_policy='Publish three named scalar outcomes and source/input/output identities. Full states, trig constants, sampled geometry, carries and raw stage outputs remain scratch-only.')
    text = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if len(text.encode()) >= 100000:
        raise ValueError('Compact record must stay below 100 KB')
    a.out.write_text(text)
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
