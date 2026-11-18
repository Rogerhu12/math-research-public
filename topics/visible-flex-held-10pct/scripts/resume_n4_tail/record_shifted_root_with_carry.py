#!/usr/bin/env python3
"""Compact the completed reviewed A-plus-final-carry three-stage readout."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import mpmath as mp
from record_fixed_actual import load, scalar_tree, sha
from record_tail_initialization import numeric_identity

mp.mp.dps = 140


def ident(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def checked(ref):
    if sha(ref['path']) != ref['sha256']:
        raise ValueError('Frozen bound file changed: ' + ref['path'])
    return load(ref['path'])


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def fhash(values):
    return hashlib.sha256(packed(values)).hexdigest()


def exact(left, right):
    return packed([left]) == packed([right])


def differences(state, precise, fixture):
    if len(state) != 42 or len(precise) != 42:
        raise ValueError('Both mean components must be included')
    errors = [mp.mpf(float(v))-mp.mpf(precise[j]) for j, v in enumerate(state)]
    scale, ratio = mp.mpf(float(fixture['normalizationScale'])), mp.mpf(float(fixture['portRatio']))
    physical = [abs(errors[j] if j < 20 else errors[j]/ratio)/scale for j in range(40)]
    return dict(maximum_all42_error_to_mp90=mp.nstr(max(map(abs, errors)), 32),
        maximum_mean2_error_to_mp90=mp.nstr(max(map(abs, errors[40:])), 32),
        maximum_normalized_physical_error_to_mp90=mp.nstr(max(physical), 32),
        mp_error_peak_component=max(range(40), key=lambda j:physical[j]))


def verify_carry(row, fixture):
    events = [event for event in row['events'] if event['event'] == 'rk_final_carry']
    expected_count = 42*sum(len(grid) for grid in fixture['grid'])
    if len(events) != expected_count:
        raise ValueError('Incomplete final-update trace')
    state = list(fixture['initial42'])
    carry = [0.0]*42
    maximum_carry = maximum_difference = 0.0
    changed = 0
    index = 0
    for profile, grid in enumerate(fixture['grid']):
        for step, point in enumerate(grid):
            for component in range(42):
                event = events[index]; index += 1
                if (event['profile'], event['step'], event['component']) != (profile, step, component):
                    raise ValueError('Final-update order differs')
                previous, previous_carry = state[component], carry[component]
                increment = event['stepIncrement']
                corrected = increment-previous_carry
                ordinary = previous+increment
                next_state = previous+corrected
                next_carry = (next_state-previous)-corrected
                values = dict(previous=previous, previousCarry=previous_carry, corrected=corrected,
                              ordinary=ordinary, nextState=next_state, carry=next_carry)
                if any(not exact(event[key], value) for key, value in values.items()):
                    raise ValueError('Recorded final-carry arithmetic mismatch')
                state[component], carry[component] = next_state, next_carry
                changed += not exact(next_state, ordinary)
                maximum_carry = max(maximum_carry, abs(next_carry))
                maximum_difference = max(maximum_difference, abs(next_state-ordinary))
    if packed(state) != packed(row['state']) or packed(carry) != packed(row['carry']):
        raise ValueError('Recorded carry recurrence does not reach the saved complete state')
    return dict(changed_state_updates=changed, maximum_auxiliary_carry=maximum_carry,
        maximum_final_auxiliary_carry=max(map(abs, carry)), maximum_local_update_difference=maximum_difference,
        final_carry42_sha256=fhash(carry)), expected_count


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('plan', 'summary', 'resource', 'log', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError('Do not overwrite a completed record')
    plan, summary, resource = load(a.plan), load(a.summary), load(a.resource)
    for ref in plan['files'].values():
        if sha(ref['path']) != ref['sha256']:
            raise ValueError('Reviewed plan/source/input changed')
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('A genuine successful child terminal is required')
    if resource['command'] != plan['child_command'] or resource['command'][1:] != summary['command']:
        raise ValueError('Actual execution differs from the reviewed frozen plan')
    mapping = {'source':'source', 'shifted_root_source':'shifted_root_source', 'original_base_source':'base',
               'original_kahan_source':'original_kahan_source', 'bridge':'bridge', 'capsule_summary':'capsule',
               'float_baseline':'baseline', 'mp90_summary':'mp90_reference',
               'previously_executed_root_only_A':'existing_A', 'previously_executed_original_root_Kahan':'existing_Kahan'}
    if any(summary[key] != plan['files'][value] for key, value in mapping.items()):
        raise ValueError('Executed source/reference identity differs')
    for key in ('full_flow_jacobian_computed', 'complete_tail_solver_invoked', 'production_source_changed',
                'physical_checkpoint_written', 'carry_read_by_RHS'):
        if summary[key]:
            raise ValueError('The prescribed finite scope changed')
    cs, ms, ss, ks = [load(plan['files'][key]['path']) for key in
                      ('capsule', 'mp90_reference', 'existing_A', 'existing_Kahan')]
    capsule, reference, precise, original_A, original_Kahan, raw = [checked(ref) for ref in
        (cs['coefficients'], cs['reference'], ms['raw'], ss['raw'], ks['compensated'], summary['raw'])]
    if numeric_identity(summary['root_rules']) != numeric_identity(capsule['root_rules']):
        raise ValueError('An original root rule changed')
    for key in ('source_sha256', 'additional_original_root_sources'):
        for path, digest in cs[key].items():
            if sha(path) != digest:
                raise ValueError('A bound original source changed: '+path)
    results = {}
    for i, fixture in enumerate(capsule['fixtures']):
        row, scalar = raw['rows'][i], summary['named_results'][i]
        if not fixture['stage'] == row['stage'] == scalar['stage']:
            raise ValueError('Stage scope differs')
        first_root = next(event for event in row['events'] if event['event'] == 'shifted_root_start')
        if packed(first_root['state']) != packed(fixture['initial42']):
            raise ValueError('The full initial42 differs')
        if fhash(row['state']) != scalar['output42_sha256']:
            raise ValueError('Complete output hash mismatch')
        current = differences(row['state'], precise['rows'][i]['state'], fixture)
        if any(scalar[key] != value for key, value in current.items()):
            raise ValueError('Saved full42 MP90 comparison differs')
        previous = {}
        for label, data in (('original', reference), ('A', original_A), ('Kahan', original_Kahan)):
            if data['rows'][i]['stage'] != fixture['stage']:
                raise ValueError('Existing comparison stage differs')
            previous[label] = differences(data['rows'][i]['state'], precise['rows'][i]['state'], fixture)
        if previous != scalar['existing_saved_comparisons']:
            raise ValueError('Existing saved comparison mismatch')
        physical = [v if j < 20 else v/fixture['portRatio'] for j, v in enumerate(row['state'][:40])]
        residual = [v-fixture['targetNode40'][j] for j, v in enumerate(physical)]
        if packed(residual) != packed(row['residual']) or (
                max(map(abs, residual))/fixture['normalizationScale'] != scalar['fixed_target_normalized_residual']):
            raise ValueError('Saved fixed-target residual differs')
        carry, event_count = verify_carry(row, fixture)
        if numeric_identity(carry) != numeric_identity(scalar['carry_diagnostics']):
            raise ValueError('Carry diagnostics differ from the complete recurrence')
        histogram = {}
        for root in row['root_outcomes']:
            key = str(root['iteration']); histogram[key] = histogram.get(key, 0)+1
        if (len(row['root_outcomes']) != scalar['root_calls'] or histogram != scalar['root_iterations'] or
                sum(root['fallback'] for root in row['root_outcomes']) != scalar['root_fallbacks'] or
                max(root['err']/root['scale'] for root in row['root_outcomes']) != scalar['max_stable_root_relative_residual'] or
                max(root['formedMomentErr']/root['scale'] for root in row['root_outcomes']) != scalar['max_formed_moment_root_relative_residual']):
            raise ValueError('Original returned root diagnostics differ')
        results[str(fixture['stage'])] = dict(**scalar,
            final_carry_recurrence_events_verified=event_count,
            complete_initial42_sha256=fhash(fixture['initial42']),
            normalized_error_ratios={name:mp.nstr(mp.mpf(current['maximum_normalized_physical_error_to_mp90'])/
                mp.mpf(value['maximum_normalized_physical_error_to_mp90']), 32) for name, value in previous.items()})
    rules = dict(capsule['root_rules']); halves = rules.pop('halving_factors')
    rules.update(halving_count=len(halves), halving_float64_sha256=fhash(halves))
    output = dict(scope='Completed isolated reviewed A-plus-final-state-carry comparison. No production or full-tail/DN acceptance.',
        collector=ident(__file__), helpers={name:sha(Path(__file__).with_name(name)) for name in
                                          ('record_fixed_actual.py', 'record_tail_initialization.py')},
        frozen_plan=ident(a.plan), frozen_files=plan['files'], result_summary=ident(a.summary), raw=summary['raw'],
        original_capsule_coefficients=cs['coefficients'], original_capsule_reference=cs['reference'],
        mp90_raw=ms['raw'], previous_A_raw=ss['raw'], previous_Kahan_raw=ks['compensated'],
        original_source_sha256=cs['source_sha256'], additional_original_root_sources=cs['additional_original_root_sources'],
        observer=scalar_tree(resource), observer_identity=ident(a.resource), log=ident(a.log),
        root_rules=rules, named_results=results,
        stopping_scope=summary['stopping_scope'], real_arithmetic_scope=summary['real_arithmetic_scope'],
        conclusion='The combined candidate improves the stage175 dominant error relative to A, but is worse than A at stages43/38. It improves the worst three-stage error compared with original flow; benefits do not simply add. No fixed-target residual selects the arithmetic method.',
        full_flow_jacobian_computed=False, complete_tail_solver_invoked=False, production_installed=False,
        rigorous_error_bound=False, continuous_ODE_solved=False,
        data_policy='Publish sources, frozen commands/identities and scalar diagnostics only. Complete fields and RK/root/carry traces remain scratch-only.')
    encoded = json.dumps(output, ensure_ascii=False, indent=2)+'\n'
    if len(encoded.encode()) >= 100000:
        raise ValueError('Compact record exceeds100KB')
    a.out.write_text(encoded)
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
