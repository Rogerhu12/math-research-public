#!/usr/bin/env python3
"""Compare existing original/Neumaier/Kahan outputs to existing MP90; no flow."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import struct
import sys
import mpmath as mp
from record_fixed_actual import load, sha, scalar_tree
from record_tail_initialization import numeric_identity

mp.mp.dps = 140


def ident(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def checked(ref):
    if sha(ref['path']) != ref['sha256']:
        raise ValueError('Changed source/input: ' + ref['path'])
    return load(ref['path'])


def packed(values):
    return struct.pack('<' + 'd' * len(values), *values)


def fhash(values):
    return hashlib.sha256(packed(values)).hexdigest()


def number(value):
    return mp.nstr(value, 32)


def original_terminal(summary_path, summary, node):
    root = summary_path.parent
    rp, lp = root / 'resource.json', root / 'process.log'
    resource = load(rp)
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] != 0:
        raise ValueError('An old executed readout lacks genuine exit0')
    observed = resource['command'][2:] if node else resource['command'][1:]
    recorded = summary['command'][1:] if node else summary['command']
    if observed != recorded:
        raise ValueError('Old observer/summary command mismatch')
    return dict(resource=ident(rp), log=ident(lp), observed=scalar_tree(resource))


def method_errors(state, precise, original, fixture, stored_residual):
    if len(state) != 42:
        raise ValueError('All42, including both means, are required')
    expected = [mp.mpf(v) for v in precise]
    actual = [mp.mpf(float(v)) for v in state]
    old = [mp.mpf(float(v)) for v in original]
    errors = [v - expected[j] for j, v in enumerate(actual)]
    old_errors = [v - expected[j] for j, v in enumerate(old)]
    ratio = mp.mpf(float(fixture['portRatio']))
    scale = mp.mpf(float(fixture['normalizationScale']))
    physical_errors = [errors[j] if j < 20 else errors[j] / ratio for j in range(40)]
    norm_errors = [abs(v) / scale for v in physical_errors]
    peak = max(range(40), key=lambda j: norm_errors[j])
    original_norm_errors = [abs(old_errors[j] if j < 20 else old_errors[j] / ratio) / scale
                            for j in range(40)]
    old_peak = max(range(40), key=lambda j: original_norm_errors[j])
    physical = [v if j < 20 else v / fixture['portRatio'] for j, v in enumerate(state[:40])]
    residual = [v - fixture['targetNode40'][j] for j, v in enumerate(physical)]
    if (packed(residual) != packed(stored_residual['signed']) or
            packed(physical) != packed(stored_residual['out']) or
            max(map(abs, residual)) / fixture['normalizationScale'] != stored_residual['normalizedResidual']):
        raise ValueError('Saved fixed-target residual mismatch')
    improvements = sum(abs(v) < abs(old_errors[j]) for j, v in enumerate(errors))
    worsened = sum(abs(v) > abs(old_errors[j]) for j, v in enumerate(errors))
    unchanged = sum(abs(v) == abs(old_errors[j]) for j, v in enumerate(errors))
    return dict(
        output42_sha256=fhash(state), maximum_all42_absolute_error=number(max(map(abs, errors))),
        maximum_Q20_absolute_error=number(max(map(abs, errors[:20]))),
        maximum_pi20_absolute_error=number(max(map(abs, errors[20:40]))),
        maximum_mean2_absolute_error=number(max(map(abs, errors[40:]))),
        first_mean_signed_error=number(errors[40]), second_mean_signed_error=number(errors[41]),
        maximum_normalized_physical_error=number(max(norm_errors)),
        normalized_error_peak_component=peak, normalized_error_peak_mode=4 * (peak % 20 + 1),
        normalized_error_peak_kind='Q' if peak < 20 else 'pi',
        peak_signed_error=number(errors[peak]),
        original_error_peak_component=old_peak,
        signed_error_at_original_error_peak=number(errors[old_peak]),
        ratio_to_original_maximum_error=number(max(norm_errors) / max(original_norm_errors)),
        components_with_smaller_absolute_error=improvements,
        components_with_larger_absolute_error=worsened,
        components_with_identical_absolute_error=unchanged,
        fixed_target_normalized_residual=max(map(abs, residual)) / fixture['normalizationScale'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('neumaier-summary', 'kahan-summary', 'mp90-summary', 'out'):
        p.add_argument('--' + name, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise ValueError('Do not overwrite an executed comparison record')
    ns, ks, ms = load(a.neumaier_summary), load(a.kahan_summary), load(a.mp90_summary)
    if ms['precision'] != 'mp' or ms['dps'] != 90:
        raise ValueError('This comparison requires the existing MP90 readout')
    cs_ref = dict(path=ms['capsule_summary_path'], sha256=ms['capsule_summary_sha256'])
    cs = checked(cs_ref)
    capsule = checked(cs['coefficients'])
    reference = checked(cs['reference'])
    precise = checked(ms['raw'])
    for key in ('original_coefficients', 'original_reference'):
        checked(ms[key])
    if ms['original_coefficients'] != cs['coefficients'] or ms['original_reference'] != cs['reference']:
        raise ValueError('MP90 used another fixed-coefficient definition')
    source_hashes = {}
    for document, keys in ((ns, ('source_sha256', 'additional_current_root_source_sha256')),
                           (ks, ('source_sha256', 'additional_current_root_source_sha256')),
                           (cs, ('source_sha256', 'additional_original_root_sources'))):
        for key in keys:
            for path, digest in document[key].items():
                if path in source_hashes and source_hashes[path] != digest:
                    raise ValueError('A shared original source has inconsistent identities')
                if sha(path) != digest:
                    raise ValueError('Original source changed: ' + path)
                source_hashes[path] = digest
    old_data = {}
    for label, summary, sp in (('neumaier', ns, a.neumaier_summary), ('kahan', ks, a.kahan_summary)):
        old_data[label] = {key: checked(summary[key]) for key in ('fixtures', 'original', 'compensated')}
        old_data[label]['terminal'] = original_terminal(sp, summary, node=True)
        if summary['named_stages'] != [43, 38, 175] or summary['modes'] != 20 or summary['spacing'] != 4:
            raise ValueError('Unexpected three-stage physical scope')
        if any(summary[k] for k in ('states_changed', 'checkpoint_written', 'full_tail_replay_performed',
                                    'nonlinear_solver_invoked')):
            raise ValueError('Old record scope changed')
    mp_terminal = original_terminal(a.mp90_summary, ms, node=False)
    invariant_keys = ('input_sha256', 'locator_sha256', 'original_run_summary_sha256', 'config',
                      'named_stages', 'modes', 'spacing', 'quadrature', 'independent_quadrature_nodes',
                      'steps', 'originalGate', 'stage_count', 'complete_input_states_sha256',
                      'complete_cut_height_sha256', 'trig_float64_le_sha256')
    for key in invariant_keys:
        if numeric_identity(ns[key]) != numeric_identity(ks[key]):
            raise ValueError('Original input/model mismatch: ' + key)
    if cs['fixture'] != ns['fixtures'] or cs['original_output'] != ns['original']:
        raise ValueError('MP90 capsule does not descend from the saved Neumaier baseline')
    if sha(ns['input']) != ns['input_sha256']:
        raise ValueError('Full original failed state changed')
    nf, kf = old_data['neumaier']['fixtures'], old_data['kahan']['fixtures']
    if numeric_identity(nf['fixtures']) != numeric_identity(kf['fixtures']):
        raise ValueError('The two old runs did not use identical full fixtures')
    if numeric_identity(nf['trig']) != numeric_identity(kf['trig']) or numeric_identity(nf['trig']) != numeric_identity(capsule['trig']):
        raise ValueError('Original state/Jacobian trigonometric coefficients differ')
    stage_results = {}
    for i, fixture in enumerate(nf['fixtures']):
        cp = capsule['fixtures'][i]
        for key, value in fixture.items():
            if key != 'geometry' and numeric_identity(value) != numeric_identity(cp[key]):
                raise ValueError('Frozen MP capsule input differs: ' + key)
        original = reference['rows'][i]['state']
        high = precise['rows'][i]
        if not fixture['stage'] == reference['rows'][i]['stage'] == high['stage']:
            raise ValueError('Stage order mismatch')
        row_results = {}
        baseline_residual = old_data['neumaier']['original']['rows'][i]['residual']
        row_results['original'] = method_errors(original, high['state'], original, fixture, baseline_residual)
        for label in ('neumaier', 'kahan'):
            plain = old_data[label]['original']['rows'][i]
            altered = old_data[label]['compensated']['rows'][i]
            summary = (ns if label == 'neumaier' else ks)['named_results'][i]
            if not plain['baseline42_bitwise_identical'] or any(
                    packed(plain[key]) != packed(original) for key in ('state', 'reference42', 'manualPlain42')):
                raise ValueError('An original all42 baseline differs')
            for key in ('stage', 'portRatio', 'normalizationScale', 'input42_sha256',
                        'targetNode40_sha256', 'grid_sha256', 'sampled_original_geometry_sha256'):
                if numeric_identity(altered[key]) != numeric_identity(fixture[key]):
                    raise ValueError('Saved compensated output belongs to another fixture')
            if fhash(altered['state']) != altered['output42_sha256'] or altered['output42_sha256'] != summary['compensated_output42_sha256']:
                raise ValueError('Saved compensated all42 hash differs')
            result = method_errors(altered['state'], high['state'], original, fixture, altered['residual'])
            result['original_reported_minA'] = altered['minA']
            result['original_reported_minD'] = altered['minD']
            result['original_reported_maximum_point_root_relative_residual'] = altered['maximumRootRelativeResidual']
            if label == 'kahan':
                if fhash(altered['carry']) != summary['final_carry42_sha256']:
                    raise ValueError('Saved auxiliary carry identity differs')
                result['saved_final_carry42_sha256'] = fhash(altered['carry'])
                result['saved_maximum_carry'] = altered['maximumCarry']
            row_results[label] = result
        stage_results[str(fixture['stage'])] = dict(
            stage=fixture['stage'], original_normalization_scale=fixture['normalizationScale'],
            original_port_ratio=fixture['portRatio'], complete_input42_sha256=fixture['input42_sha256'],
            complete_target40_sha256=fixture['targetNode40_sha256'], grid_sha256=fixture['grid_sha256'],
            original_geometry_sha256=fixture['sampled_original_geometry_sha256'], comparisons=row_results)
    output = dict(
        read_only_analysis_created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source=ident(__file__), helpers={name:sha(Path(__file__).with_name(name)) for name in
                                       ('record_fixed_actual.py', 'record_tail_initialization.py')},
        command=sys.argv, analysis_decimal_precision=mp.mp.dps,
        scope='New read-only comparison of already saved full42 Neumaier/Kahan outputs with the already executed frozen MP90. No flow/root/RK reevaluation; no patches combined.',
        provenance=dict(neumaier_summary=ident(a.neumaier_summary), kahan_summary=ident(a.kahan_summary),
                        mp90_summary=ident(a.mp90_summary), original_capsule=cs_ref,
                        original_capsule_coefficients=cs['coefficients'], original_capsule_reference=cs['reference'],
                        mp90_raw=ms['raw'], original_failed_state=ident(ns['input']),
                        neumaier_files={key:ns[key] for key in ('fixtures', 'original', 'compensated')},
                        kahan_files={key:ks[key] for key in ('fixtures', 'original', 'compensated')}),
        old_execution_resources=dict(neumaier=old_data['neumaier']['terminal'], kahan=old_data['kahan']['terminal'],
                                     mp90=mp_terminal), original_source_sha256=source_hashes,
        complete_input_states_sha256=ns['complete_input_states_sha256'],
        complete_cut_height_sha256=ns['complete_cut_height_sha256'],
        original_physical_config=ns['config'], original_gate=ns['originalGate'],
        original_trig_float64_le_sha256=ns['trig_float64_le_sha256'],
        all_three_baselines_all42_bitwise_identical=True, both_mean_components_included=True,
        missing_old_data='Old full RK/root traces for the two compensation runs were not saved. This comparison does not reconstruct their unsaved intermediate operands or local error history.',
        named_results=stage_results, no_new_flow_evaluations=True, no_new_tail_or_DN_acceptance=True,
        production_changed=False, rigorous_ODE_error_bound=False,
        interpretation='Accuracy is assessed against the saved fixed-coefficient MP90 readout, not by closeness to the fixed target node. MP90 stability is finite evidence, not an interval or continuous error certificate.')
    encoded=json.dumps(output, ensure_ascii=False, indent=2)+'\n'
    if len(encoded.encode()) >= 100000:
        raise ValueError('Record must remain below100KB')
    a.out.write_text(encoded)
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out),
                         normalized_errors={stage:{method:v['maximum_normalized_physical_error']
                                                   for method,v in row['comparisons'].items()}
                                            for stage,row in stage_results.items()})))


if __name__ == '__main__':
    main()
