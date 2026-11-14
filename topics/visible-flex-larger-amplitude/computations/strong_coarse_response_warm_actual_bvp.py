#!/usr/bin/env python3
"""Use a genuine M28 control response only as an M32 initial-guess increment.

Both baseline fields must be completely accepted at the same physical metric,
material chart and exact raw mesh. This adapter preserves the complete accepted
M32 field and all 32 core parameters, then embeds a declared linear combination
of the saved M28 response vectors into the original cylindrical channels. New
M32 channels have zero *increment*, not zero baseline. The saved lower-resolution
response is never relabelled as an M32 Jacobian or an accepted new solution.

Only the initial guess is replaced. The corrected original frontload provider,
all-core plus three-geometry layout, inlet correction, original Newton/RMS,
true current-H full tail/Jacobian and final physical audit remain unchanged.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PRIMARY = ('delta', 'boost_length', 'boost_speed')
CORE = ('actual_q1', 'actual_q4', 'actual_c6')
EXTERNAL = ('vu', 'vd', 'start_acceleration', 'descending_turn_curvature',
            'descending_sync_curvature', 'coast_outward', 'loop_ratio',
            'initial_speed_pulse', 'initial_speed_frontload')
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}
EXPECTED = {
    'strong_full_tangent_initial_laws_anchor_actual_bvp.py':
        'd151cb67c2dbfbadd5ba35a9f386c5e15ff98f056df45d89677b989cd887f651',
    'strong_actual_augmented_core.py':
        '74c64ab558953c6d0378948dd4affb5d354d1faaecab7922b83cfdf76041bad7',
    'strong_actual_fixed_control_response.py':
        'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1',
    'strong_sameg_m32_fullflow_refinement_v2.py':
        '202471724125bb567d622be513d2dc3ffd664d7070f8e93502a0e5537dbbe57c',
}
_ACTIVE = None


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def argument(argv, name):
    if argv.count(name) != 1:
        raise ValueError('Require exactly one original argument '+name)
    return argv[argv.index(name)+1]


def checked_source():
    for name, expected in EXPECTED.items():
        if sha(HERE/name) != expected:
            raise ValueError('Frozen original source differs: '+name)


def verified_warm(reference, raw, target, shifts, payload=False):
    if _ACTIVE is None:
        raise ValueError('No real accepted fine-field initial guess was prepared')
    record, warm = _ACTIVE
    if (str(reference) != record['current_reference'] or str(raw) != record['current_raw']
            or sha(reference) != record['current_reference_sha256']
            or sha(raw) != record['current_raw_sha256']
            or list(target) != record['target_core']
            or dict(shifts) != record['external_shifts']):
        raise ValueError('Embedded initial guess belongs to different production inputs')
    return warm if payload else True


def accepted_raw(surface, raw, raw_path, sources):
    import numpy as np
    from strong_actual_fixed_control_response import raw_flat
    if (not surface.get('solver_success') or surface.get('audit_pending', True)
            or not surface['config'].get('actual_nonlinear_tail')
            or not surface['config'].get('fixed_metric')
            or not raw.get('solver_success') or raw.get('physical_surface') is not False
            or not raw['identity'].get('fixed')
            or surface['raw_collocation_checkpoint']['sha256'] != sha(raw_path)):
        raise ValueError('Both baselines must be genuinely accepted fixed actual fields')
    for a, b in (('gauge', 'gauge_amplitude'), ('profile', 'frozen_profile'),
            ('physical_tail_parameters', 'physical_tail_parameters'),
            ('physical_tail_cut', 'physical_tail_cut'),
            ('reference_coefficients', 'chart_reference_coefficients'),
            ('reference_frequencies', 'chart_reference_frequencies')):
        if canonical(raw['identity'][a]) != canonical(surface[b]):
            raise ValueError('Accepted raw and physical identity differ: '+a)
    if (raw['identity']['numerical_reference_knots'] != surface['numerical_meridian_chart']['reference_t']
            or surface['max_rms_collocation_residual'] > surface['config']['tol']
            or surface['summary']['physical_bc_max'] > surface['actual_tail']['actual_physical_bc_tolerance']
            or not surface['actual_tail'].get('audit')):
        raise ValueError('Original complete actual acceptance or numerical reference is missing')
    modes, nodes = int(surface['modes']), int(surface['nodes'])
    arrays = {name: np.asarray(raw_flat(raw_path, raw, name, sources)).reshape(raw['arrays'][name]['shape'])
              for name in ('x', 'y', 'p')}
    if (arrays['x'].shape != (nodes,) or arrays['y'].shape != (3*modes+1, nodes)
            or arrays['p'].shape != (modes,)
            or not all(np.isfinite(a).all() for a in arrays.values())
            or arrays['p'].tolist() != raw['parameter_state']
            or arrays['p'].tolist() != surface['parameters']
            or surface['core']['frequencies'] != list(range(2, 2*modes+1, 2))):
        raise ValueError('Complete accepted raw field/core layout differs')
    core = np.r_[surface['gauge_amplitude']*math.exp(float(arrays['p'][0])),
                 arrays['p'][1:]*np.asarray(surface['central_correction_scales'])]
    core[1] += surface['chart_reference_coefficients'][1]
    if not np.array_equal(core, surface['core']['coefficients']):
        raise ValueError('Original all-core parameter units do not reproduce the saved core')
    return arrays


def prepare(options, argv):
    import numpy as np
    checked_source()
    current_path = Path(argument(argv, '--actual-reference'))
    current_raw_path = Path(argument(argv, '--actual-reference-raw'))
    current_tail_path = Path(argument(argv, '--actual-reference-tail'))
    coarse_path, coarse_raw_path, coarse_tail_path = (
        options.coarse_reference, options.coarse_raw, options.coarse_tail)
    paths = (current_path, current_raw_path, current_tail_path,
             coarse_path, coarse_raw_path, coarse_tail_path, options.coarse_response_data)
    if any(path is None for path in paths):
        raise ValueError('Give all original coarse response/reference/raw/tail paths')
    sources = {str(path): sha(path) for path in (Path(__file__), *paths)}
    current, current_raw, current_tail, coarse, coarse_raw, coarse_tail, response = map(read, paths)
    if (int(coarse['modes']), int(current['modes'])) != (28, 32):
        raise ValueError('This declared initial-guess embedding is exactly M28 to M32')
    for key in ('gauge_amplitude', 'angular_chart', 'chart_reference_coefficients',
            'chart_reference_frequencies', 'frozen_profile', 'physical_tail_parameters',
            'physical_tail_cut', 'physical_port_sha256'):
        if canonical(coarse[key]) != canonical(current[key]):
            raise ValueError('The two accepted fields have different physical g or coordinates: '+key)
    if (coarse['numerical_meridian_chart']['reference_t'] != current['numerical_meridian_chart']['reference_t']
            or coarse['numerical_meridian_chart']['physical_s'] != current['numerical_meridian_chart']['physical_s']
            or coarse['central_correction_scales'] != current['central_correction_scales'][:27]
            or (coarse['config']['angular'], current['config']['angular']) != (1024, 1280)):
        raise ValueError('Original knots, core units or declared angular representations differ')
    for key in set(coarse_tail['config']) | set(current_tail['config']):
        if key not in IO | {'modes'} and canonical(coarse_tail['config'].get(key)) != canonical(current_tail['config'].get(key)):
            raise ValueError('The common physical/numerical tail parameter differs: '+key)
    arrays = [accepted_raw(s, r, p, sources) for s, r, p in
              ((coarse, coarse_raw, coarse_raw_path), (current, current_raw, current_raw_path))]
    old, now = arrays
    if old['x'].tobytes() != now['x'].tobytes():
        raise ValueError('This initial-guess adapter requires the same complete raw mesh; no interpolation is hidden')
    for surface, values, packet in ((coarse, old, coarse_tail), (current, now, current_tail)):
        modes = int(surface['modes'])
        h = -surface['gauge_amplitude']*values['y'][2*modes+1:, -1]
        request, result = packet['request'], packet['response']
        if (np.asarray(request['height'], dtype=np.float64).tobytes() != h.tobytes()
                or not request.get('jacobian') or not request.get('audit')
                or not result.get('converged') or not result.get('audit')
                or result['residual'] > packet['config']['solveTolerance']
                or len(result['heightJetJacobian']) != (3*modes+2)*modes
                or packet['source_sha256'] != surface['actual_tail']['source_sha256']
                or result['audit'] != surface['actual_tail']['audit']):
            raise ValueError('A baseline lacks its exact full-H/full-J/original audit identity')
    if not str(current_path).endswith('.json.gz'):
        raise ValueError('The actual fine primary must be its original gzip file')
    prefix = str(current_path)[:-8]
    prefix_identity = Path(prefix+'-live-physical-identity.json')
    tail_identity = Path(prefix+'-tail-response_sameg-M32-physical-identity.json')
    resource_path = Path(prefix+'-resource.json')
    first, second, resource = map(read, (prefix_identity, tail_identity, resource_path))
    for proof, names in ((first, ('complete_profile_identical', 'all_prefix_and_bridge_segments_identical',
            'all_segment_phase_and_coefficients_identical', 'a_as_ass_callback_samples_bitwise_equal',
            'original_material_chart_identical', 'original_numerical_reference_identical',
            'original_physical_length_identical')),
            (second, ('all_effective_non_mode_non_IO_parameters_equal',
            'complete_calibration_adapter_and_160_original_cells_identical',
            'profile_fingerprints_identical', 'original_cut_scalars_bitwise_equal',
            'new_full_flow_snapshot_not_restored_from_old_M', 'distinct_exact_stage_identity_for_new_M',
            'original_warm_gate_passed'))):
        if not all(proof.get(name) is True for name in names):
            raise ValueError('The actual constructor same-g identity proof is incomplete')
    if (first['original_reference_sha256'] != sha(coarse_path)
            or second['old_reference_sha256'] != sha(coarse_path)
            or resource.get('exitcode') != 0 or not resource.get('wait4_observed')):
        raise ValueError('The real fine constructor/owned acceptance belongs to another baseline')
    sources.update({str(path): sha(path) for path in (prefix_identity, tail_identity, resource_path)})
    if (response.get('schema') != 'fixed-actual-to-three-control-response-v1'
            or not response.get('finished') or response.get('new_solution')
            or response['modes'] != 28 or response['angular'] != 1024
            or response['nodes'] != len(old['x'])
            or response['baseline']['core'] != coarse['core']['coefficients']
            or response['baseline']['profile'] != coarse['frozen_profile']
            or response['baseline']['gauge'] != coarse['gauge_amplitude']):
        raise ValueError('The original coarse response is bound to a different accepted state')
    for path in (coarse_path, coarse_raw_path, coarse_tail_path):
        if response['source_sha256'].get(str(path)) != sha(path):
            raise ValueError('The original coarse response path/SHA binding differs: '+str(path))
    weights = {}
    for text in options.coarse_control:
        name, value = text.split('=', 1)
        if name not in CORE+EXTERNAL or name in weights or not math.isfinite(float(value)):
            raise ValueError('Give distinct finite physical coarse-control increments')
        weights[name] = float(value)
    combined = np.zeros(old['y'].size+28)
    geometry = np.zeros(3)
    used = []
    for name, weight in weights.items():
        if weight == 0.:
            continue
        if name in CORE:
            rows = [r for r in response['prescribed_low_core_responses'] if r['direction'] == name]
            kind = 'prescribed-'
        else:
            rows = [r for r in response['additional_core_held_directions'] if r['external_field'] == name]
            kind = 'core-held-'
        matches = [a for a in response['tangent_arrays'] if a['file'].endswith('-'+kind+name+'.npy.gz')]
        if len(rows) != 1 or len(matches) != 1:
            raise ValueError('The requested complete coarse direction is missing or ambiguous: '+name)
        row, item = rows[0], matches[0]
        path = Path(item['file'])
        if sha(path) != item['sha256']:
            raise ValueError('The original complete coarse vector SHA differs')
        with gzip.open(path, 'rb') as stream:
            value = np.load(stream, allow_pickle=False)
        if value.dtype != np.float64 or value.shape != combined.shape or not np.isfinite(value).all():
            raise ValueError('Complete coarse response field/parameter shape differs')
        combined += weight*value
        geometry += weight*np.asarray([row['physical_profile_derivative'][field] for field in PRIMARY])
        sources[str(path)] = item['sha256']
        used.append(dict(direction=name, weight=weight, file=str(path), sha256=item['sha256']))
    mapping = np.r_[np.arange(29), 33+np.arange(28), 65+np.arange(28)]
    field = np.zeros_like(now['y'])
    field[mapping] = combined[:old['y'].size].reshape(old['y'].shape, order='F')
    parameters = np.zeros(32)
    parameters[:28] = combined[old['y'].size:]
    extra = sorted(set(range(97))-set(map(int, mapping)))
    if (field[mapping].tobytes() != combined[:old['y'].size].reshape(old['y'].shape, order='F').tobytes()
            or not np.all(field[extra] == 0.) or not np.all(parameters[28:] == 0.)):
        raise ValueError('The complete lower-spectrum increment was not exactly embedded')
    direction = np.r_[field.ravel(order='F'), parameters]
    target = (np.asarray(current['core']['coefficients'][:3])+
              np.asarray([weights.get(name, 0.) for name in CORE])).tolist()
    if target[0] <= 0.:
        raise ValueError('The actual fine-core amplitude target must remain positive')
    shifts = {name: value for name, value in weights.items() if name in EXTERNAL and value != 0.}
    record = dict(scope=__doc__, current_reference=str(current_path), current_raw=str(current_raw_path),
        current_reference_sha256=sha(current_path), current_raw_sha256=sha(current_raw_path),
        coarse_reference=str(coarse_path), coarse_raw=str(coarse_raw_path),
        coarse_response=str(options.coarse_response_data), source_sha256=sources,
        coarse_modes=28, actual_modes=32, complete_original_mesh_bits_identical=True,
        original_material_chart_and_physical_metric_identical=True,
        original_both_full_H_J_and_audits_verified=True, fine_original_owned_exitcode=0,
        state_channel_embedding=mapping.tolist(), additional_fine_state_rows=extra,
        all_original_fine_state_and_core_preserved_before_original_warm_correction=True,
        added_fine_channels_have_zero_increment_only=True,
        original_coarse_response_partial_recovery=response.get('partial_recovery'),
        original_coarse_half_or_residual_data_not_upgraded=True,
        weights=used, explicit_controls=weights, target_core=target, external_shifts=shifts,
        fine_baseline_complete_core=current['core']['coefficients'],
        coarse_baseline_complete_core=coarse['core']['coefficients'],
        geometry_increment=dict(zip(PRIMARY, map(float, geometry))),
        full_direction_shape=list(direction.shape),
        full_direction_float64le_sha256=hashlib.sha256(direction.astype('<f8').tobytes()).hexdigest(),
        coarse_direction_float64le_sha256=hashlib.sha256(combined.astype('<f8').tobytes()).hexdigest(),
        warm_only=True, fine_control_derivative_claim=False, nonlinear_solution=False,
        original_inlet_correction_and_low_target_enforcement_preserved=True,
        original_complete_Newton_tail_RMS_boundary_and_audit_required=True)
    return record, dict(fixed_parameter_and_field_increment=direction,
                       geometry_increment=geometry, provenance=record)


def main():
    global _ACTIVE
    checked_source()
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--coarse-reference', type=Path)
    parser.add_argument('--coarse-raw', type=Path)
    parser.add_argument('--coarse-tail', type=Path)
    parser.add_argument('--coarse-response-data', type=Path)
    parser.add_argument('--coarse-control', action='append', default=[])
    parser.add_argument('--coarse-warm-prepare-report', type=Path)
    options, remaining = parser.parse_known_args()
    if any(name in remaining for name in ('--response-data', '--target-core', '--neutral-control-step',
            '--resume-actual-iterate', '--resume-tail-config', '--inspect-local-output')):
        raise ValueError('The explicit coarse increment supplies its own warm target and controls')
    source_only = '--prepare-source-record' in remaining
    if not source_only:
        _ACTIVE = prepare(options, remaining)
        record, _ = _ACTIVE
        if options.coarse_warm_prepare_report:
            with options.coarse_warm_prepare_report.open('x') as stream:
                json.dump(record, stream, indent=2, allow_nan=False)
                stream.write('\n')
            print(json.dumps(dict(prepared=True, real_both_accepted_baselines_verified=True,
                new_solver_or_flow_executed=False, report=str(options.coarse_warm_prepare_report))), flush=True)
            _ACTIVE = None
            return
        remaining += ['--target-core', *map(repr, record['target_core'])]
        for name, value in record['external_shifts'].items():
            remaining += ['--neutral-control-step', name+'='+repr(value)]
    else:
        record = None
    sys.modules['strong_coarse_response_warm_actual_bvp'] = sys.modules[__name__]
    import strong_full_tangent_initial_laws_anchor_actual_bvp as production
    original_build = production.anchor_build

    def transfer_build(original):
        prior_build = original_build(original)
        def build(configuration, disk_configuration):
            source, prior = prior_build(configuration, disk_configuration)
            edits = [
                ('import types\n', 'import types\nfrom strong_coarse_response_warm_actual_bvp import verified_warm\n'),
                ('    if external_shifts and not options.response_data:\n',
                 '    if external_shifts and not options.response_data and not verified_warm(\n'
                 '            options.actual_reference, options.actual_reference_raw, target, external_shifts):\n'),
                ('    warm = None\n',
                 '    warm = verified_warm(options.actual_reference, options.actual_reference_raw,\n'
                 '        target, external_shifts, payload=True)\n'),
                ("complete_actual_tangent_warm=warm['provenance'] if warm else None",
                 "explicit_coarse_increment_warm=warm['provenance'] if warm else None"),
                ('Complete actual-J warm field on the original residual quadrature and a complete-mean C2 cubic physical image; unsolved comparison only.',
                 'Complete accepted fine field plus an explicitly embedded coarse-response increment; initial guess only, not a fine Jacobian or new solution.'),
                ('    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}',
                 "    source_names += ('strong_coarse_response_warm_actual_bvp.py',)\n"
                 '    hashes = {str(HERE/name): sha(HERE/name) for name in source_names}'),
            ]
            changed = source
            for before, after in edits:
                if changed.count(before) != 1:
                    raise ValueError('Original coarse-warm initial-guess source anchor is not unique')
                changed = changed.replace(before, after, 1)
            reverse = changed
            for before, after in reversed(edits):
                if reverse.count(after) != 1:
                    raise ValueError('Original coarse-warm reverse source anchor differs')
                reverse = reverse.replace(after, before, 1)
            if reverse != source:
                raise ValueError('Initial-guess adapter changed another original production site')
            ast.parse(changed, filename='<explicit-coarse-increment-in-original-actual-BVP>')
            provenance = dict(prior)
            provenance['source_sha256'] = {**prior['source_sha256'], str(Path(__file__)): sha(__file__)}
            provenance['prior_transformed_source_sha256'] = prior['transformed_source_sha256']
            provenance['transformed_source_sha256'] = hashlib.sha256(changed.encode()).hexdigest()
            provenance['replacements'] = list(prior['replacements'])+[
                dict(before=a, after=b, count=1) for a, b in edits]
            provenance['explicit_coarse_response_initial_guess'] = dict(scope=__doc__, input_record=record,
                exact_reverse_recovers_original_corrected_initial_laws=True,
                all_original_solver_and_physical_acceptance_gates_preserved=True,
                source_preparation_only=source_only, all_MJS_unchanged=True)
            return changed, provenance
        return build

    previous_argv = sys.argv
    production.anchor_build = transfer_build
    sys.argv = [previous_argv[0], *remaining]
    try:
        production.main()
    finally:
        production.anchor_build = original_build
        sys.argv = previous_argv
        _ACTIVE = None


if __name__ == '__main__':
    main()
