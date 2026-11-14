#!/usr/bin/env python3
"""Join genuine saved six and supplemental two external response columns.

The six original combined rows and arrays are reused byte for byte. Only the
two new core-held combinations are assembled. No ODE/Jacobian is evaluated.
Original missing primary half arrays stay missing: combined half differences
and combined matrix residuals are explicitly null. The separately reported
perturbation estimates are numerical diagnostics, not interval certificates.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OLD_FIELDS = ['delta', 'boost_length', 'boost_speed', 'vu',
              'descending_turn_curvature', 'start_acceleration']
NEW_FIELDS = ['initial_speed_frontload', 'vd']
ANCHOR_SHA = '583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def write_new(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if len(data) >= 5_000_000:
        raise ValueError('A single complete repository artifact is oversized')
    with path.open('xb') as stream:
        stream.write(data)


def arrays(packet, dimension):
    loaded = {}
    for item in packet['tangent_arrays']:
        path = Path(item['file'])
        if sha(path) != item['sha256']:
            raise ValueError('A complete original tangent checksum changed: '+str(path))
        value = np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False)
        if (list(value.shape) != item['shape'] or value.shape != (dimension,)
                or value.dtype != np.float64 or not np.isfinite(value).all()):
            raise ValueError('A complete original tangent shape/value differs')
        loaded[path.name] = value
    return loaded


def one(values, suffix):
    matches = [value for name, value in values.items() if name.endswith(suffix)]
    if len(matches) != 1:
        raise ValueError('Expected exactly one complete stored array: '+suffix)
    return matches[0]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--partial-six', type=Path, required=True)
    p.add_argument('--missing-two', type=Path)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--prepare-only', action='store_true')
    a = p.parse_args()
    if a.prepare_only == bool(a.missing_two):
        raise ValueError('Choose old-six preparation or an actual completed missing-two packet')
    six = read(a.partial_six)
    if (six.get('schema') != 'fixed-actual-to-three-control-response-v1'
            or not six.get('finished') or not six.get('partial_recovery')
            or six.get('new_solution') or six.get('tail_worker_started')
            or six.get('fields') != OLD_FIELDS or six.get('unavailable_fields') != NEW_FIELDS
            or six.get('original_eight_control_job_exitcode') != 1
            or six.get('original_eight_control_job_finished')
            or not six.get('all_six_original_external_full_and_half_gates_observed')):
        raise ValueError('The genuine original six-complete/two-missing boundary is required')
    M, nodes = six['modes'], six['nodes']
    n = 3*M+1
    dimension = n*nodes+M
    old_arrays = arrays(six, dimension)
    units = np.asarray(six['physical_core_parameter_scales'], dtype=np.float64)
    if units.shape != (M,) or not np.isfinite(units).all():
        raise ValueError('The actual complete core units differ')
    physical = np.r_[np.full(n*nodes, six['baseline']['gauge']), units]
    old_rows = {row['field']:row for row in six['external_responses']}
    if list(old_rows) != OLD_FIELDS:
        raise ValueError('The six measured external rows changed order')
    errors = []
    for name in OLD_FIELDS:
        value = one(old_arrays, '-external-'+name+'.npy.gz')
        row = old_rows[name]
        if (row['half_step_response_relative_difference'] > 2e-4
                or not np.array_equal(units*value[n*nodes:], row['physical_core_derivative'])):
            raise ValueError('The original measured external field gate differs: '+name)
        errors.append((row['half_step_response_relative_difference']+2e-14)
                      *float(np.max(abs(physical*value))))
    Z = np.column_stack([one(old_arrays, '-external-'+name+'.npy.gz') for name in OLD_FIELDS[:3]])
    low = units[:3, None]*Z[n*nodes:n*nodes+3]
    if not np.array_equal(low, six['low_three_core_by_physical_control']):
        raise ValueError('The exact saved complete low-core exchange differs')
    if (len(six['prescribed_low_core_responses']) != 3
            or [row['external_field'] for row in six['additional_core_held_directions']] != OLD_FIELDS[3:]
            or six['half_step_low_three_core_by_physical_control'] is not None):
        raise ValueError('The explicit original missing-half boundary changed')
    if sha(HERE/'strong_monotone_initial_speed_anchor.py') != ANCHOR_SHA:
        raise ValueError('The corrected first-append provider source differs')
    prepared = dict(scope=__doc__, prepared=True, actual_new_columns_consumed=False,
        partial_six=dict(file=str(a.partial_six), sha256=sha(a.partial_six)),
        modes=M, nodes=nodes, angular=six['angular'], original_arrays_checked=len(old_arrays),
        original_six_rows_and_all_full_arrays_verified=True,
        original_low_exchange_bitwise_reproduced=True,
        no_future_missing_two_data_created=True, original_missing_half_limitation_preserved=True,
        entry_sha256=sha(__file__), corrected_anchor_sha256=ANCHOR_SHA)
    if a.prepare_only:
        output = a.out_prefix.with_suffix('.json')
        write_new(output, (json.dumps(prepared, indent=2, allow_nan=False)+'\n').encode())
        print(json.dumps(prepared), flush=True)
        return
    two = read(a.missing_two)
    resource_path = a.missing_two.with_name(a.missing_two.stem+'-resource.json')
    resource = read(resource_path)
    if (resource.get('exitcode') != 0 or not resource.get('wait4_observed')
            or two.get('schema') != 'fixed-actual-external-columns-v1'
            or not two.get('finished') or two.get('new_solution') or two.get('tail_worker_started')
            or two.get('fields') != NEW_FIELDS or two.get('original_six_external_fields_recomputed')
            or not two.get('all_new_full_half_and_forcing_arrays_saved')
            or not two.get('full_original_external_half_and_matrix_gates_preserved')
            or not two.get('samechart_response_adapter', {}).get('completed')
            or two['previous_completed_six']['sha256'] != sha(a.partial_six)):
        raise ValueError('The genuinely completed same-state missing-two job is required')
    for key in ('modes', 'nodes', 'angular', 'physical_core_parameter_scales'):
        if canon(two[key]) != canon(six[key]):
            raise ValueError('The exact old/new response identity differs: '+key)
    for key in ('profile', 'core', 'gauge', 'numerical_reference_knots', 'reference_coefficients',
                'accepted_rms_max', 'raw_state_bitwise_equal'):
        if canon(two['baseline'][key]) != canon(six['baseline'][key]):
            raise ValueError('The exact accepted response baseline differs: '+key)
    old_identity = {k:v for k,v in six['input_identity'].items() if k != 'source_sha256'}
    new_identity = {k:v for k,v in two['input_identity'].items() if k != 'source_sha256'}
    if canon(old_identity) != canon(new_identity):
        raise ValueError('The original complete H/raw/tail-J input identity differs')
    stats = two['disk_block_storage']['stats']
    if (stats['assembled_matrices'] != 1 or stats['factors'] != 1
            or stats['linear_solves'] != 4):
        raise ValueError('The supplemental job did not evaluate exactly two original full/half columns')
    new_arrays = arrays(two, dimension)
    if len(new_arrays) != 8:
        raise ValueError('Both full/half directions and forcing pairs are required')
    new_rows = {row['field']:row for row in two['external_responses']}
    if list(new_rows) != NEW_FIELDS:
        raise ValueError('The supplemental external rows differ')
    hashes = dict(six['source_sha256'])
    for key, value in two['source_sha256'].items():
        if key in hashes and hashes[key] != value:
            raise ValueError('A shared original source/input checksum differs: '+key)
        hashes[key] = value
    for file in (a.partial_six, a.missing_two, resource_path, Path(__file__)):
        hashes[str(file)] = sha(file)
    inverse = np.linalg.solve(low, np.eye(3))
    first_errors = np.asarray(errors[:3])
    C = abs(inverse)@np.tile(first_errors, (3, 1))
    rho = float(np.linalg.norm(C, ord=np.inf))
    if not np.isfinite(rho) or rho >= 1:
        raise ValueError('The numerical original primary perturbation majorant is invalid')
    inverse_majorant = np.linalg.solve(np.eye(3)-C, abs(inverse))
    scaled_Z = physical[:, None]*Z
    added_rows, added_arrays = [], []
    for field in NEW_FIELDS:
        full = one(new_arrays, '-external-'+field+'.npy.gz')
        half = one(new_arrays, '-external-half-'+field+'.npy.gz')
        row = new_rows[field]
        norm = float(np.max(abs(physical*full)))
        measured = float(np.max(abs(physical*full-physical*half))/max(norm, np.finfo(float).tiny))
        if (measured > 2e-4 or abs(measured-row['half_step_response_relative_difference']) > 2e-14
                or not np.array_equal(units*full[n*nodes:], row['physical_core_derivative'])):
            raise ValueError('The real saved new full/half field gate failed: '+field)
        weights = -np.linalg.solve(low, units[:3]*full[n*nodes:n*nodes+3])
        combined = full+Z@weights
        core = units*combined[n*nodes:]
        if float(np.max(abs(core[:3]))) > 1e-9 or not np.isfinite(combined).all():
            raise ValueError('The new complete core-held combination failed')
        source_error = (measured+2e-14)*norm
        dw = inverse_majorant@np.full(3, source_error+float(first_errors@abs(weights)))
        bound = source_error+float(np.max(abs(scaled_Z)@dw))+float(first_errors@(abs(weights)+dw))
        combined_norm = float(np.max(abs(physical*combined)))
        added_rows.append(dict(external_field=field,
            physical_profile_derivative={field:1., **{k:float(v) for k,v in zip(OLD_FIELDS[:3], weights)}},
            core_derivative=core.tolist(), low_core_derivative_max=float(np.max(abs(core[:3]))),
            original_external_half_gate_recomputed_from_saved_arrays=measured,
            half_step_combination_relative_difference=None,
            half_step_combination_numerical_perturbation_bound=bound/max(combined_norm,np.finfo(float).tiny),
            original_combined_half_vector_was_not_saved=True,
            equation_relative_backward_error=None, combined_matrix_residual_not_remeasured=True,
            reason='The original three primary half arrays/forcings were not saved; the new external pair is genuine.'))
        stream = io.BytesIO()
        np.save(stream, combined, allow_pickle=False)
        payload = gzip.compress(stream.getvalue(), mtime=0)
        output = Path(str(a.out_prefix)+'-core-held-'+field+'.npy.gz')
        write_new(output, payload)
        added_arrays.append(dict(file=str(output), sha256=hashlib.sha256(payload).hexdigest(),
            bytes=len(payload), shape=list(combined.shape), algebraic_combination_only=True))
    result = copy.deepcopy(six)
    result.update(scope=__doc__, finished=True,
        finished_means='Only assembly of eight genuine external columns with explicit old-half limitations.',
        fields=[*OLD_FIELDS, *NEW_FIELDS], unavailable_fields=[],
        all_eight_external_full_and_half_gates_observed=True,
        all_eight_combined_half_vectors_available=False, complete_eight_combined_half_gate_claimed=False,
        external_responses=[*six['external_responses'], *two['external_responses']],
        additional_core_held_directions=[*six['additional_core_held_directions'], *added_rows],
        tangent_arrays=[*six['tangent_arrays'], *two['tangent_arrays'], *added_arrays],
        source_sha256=hashes,
        partial_recovery=True, original_eight_control_job_finished=False,
        prior_six_combined_rows_and_arrays_reused_unchanged=True,
        original_six_external_fields_recomputed=False,
        supplemental_two=dict(file=str(a.missing_two), sha256=sha(a.missing_two),
            resource_file=str(resource_path), resource_sha256=sha(resource_path),
            owned_exitcode=0, original_matrix_stats=stats, all_full_half_and_forcing_arrays_saved=True),
        assembly_source_sha256=sha(__file__), corrected_anchor_sha256=ANCHOR_SHA,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        limitations=[*six['limitations'],
            'Two genuine supplemental external full/half pairs complete the available eight physical columns.',
            'The old six combined rows/arrays are reused exactly; only two new core-held combinations are assembled.',
            'Missing original primary half vectors prevent direct combined half/matrix measurements; nulls remain.',
            'Every finite-step candidate still requires the original nonlinear solve and physical audit.'])
    if (canon(result['prescribed_low_core_responses']) != canon(six['prescribed_low_core_responses'])
            or canon(result['additional_core_held_directions'][:3]) != canon(six['additional_core_held_directions'])):
        raise ValueError('An old original combined row changed')
    output = a.out_prefix.with_suffix('.json')
    write_new(output, (json.dumps(result, indent=2, allow_nan=False)+'\n').encode())
    print(json.dumps(dict(event='genuine_eight_columns_assembled', file=str(output),sha256=sha(output),
        no_ODE_or_Jacobian_evaluated=True, original_six_reused=True,
        new_external_half_measurements=[r['original_external_half_gate_recomputed_from_saved_arrays'] for r in added_rows],
        direct_eight_combined_half_measurement=False)), flush=True)


if __name__ == '__main__':
    main()
