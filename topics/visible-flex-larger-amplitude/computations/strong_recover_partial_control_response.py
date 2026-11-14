#!/usr/bin/env python3
"""Recover completed full directions from an interrupted larger response batch.

The six original external fields passed their actual full/half-step and full
matrix checks before an unrelated later provider failed. Their saved complete
full directions are retained exactly. Only low-core exchange and core-held
linear combinations are assembled here. Original half vectors and forcing
vectors were not saved: no direct combined half-step or combined matrix
residual measurement is invented. Numerical perturbation bounds are labeled
separately, and all data remain local warm/design information, not a solution.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np
import strong_actual_fixed_control_response as original
import strong_initial_laws_disk_control_response as source_entry

HERE = Path(__file__).resolve().parent
FIELDS = ('delta', 'boost_length', 'boost_speed', 'vu',
          'descending_turn_curvature', 'start_acceleration')
EXPECTED_ORIGINAL = 'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    value = path.read_bytes()
    return json.loads(gzip.decompress(value) if path.suffix == '.gz' else value)


def write_new(path, data):
    if path.exists():
        raise FileExistsError('Fresh recovery output required: '+str(path))
    if len(data) >= 5_000_000:
        raise ValueError('Single original archive cap exceeded')
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint', 'raw', 'tail', 'failed-prefix', 'out-prefix'):
        p.add_argument('--'+name, type=Path, required=True)
    a = p.parse_args()
    if sha(HERE/'strong_actual_fixed_control_response.py') != EXPECTED_ORIGINAL:
        raise ValueError('Original complete response implementation differs')
    hashes = {str(Path(__file__)): sha(__file__),
              str(HERE/'strong_actual_fixed_control_response.py'): EXPECTED_ORIGINAL}
    saved, raw, tail, vectors, identity = original.validate_inputs(a.checkpoint, a.raw, a.tail, hashes)
    _, producer = source_entry.transformed_source()
    hashes.update(producer['source_sha256'])
    resource_path = Path(str(a.failed_prefix)+'-resource.json')
    log_path = Path(str(a.failed_prefix)+'-stdout.log')
    adapter_path = Path(str(a.failed_prefix)+'-samechart-adapter.json')
    storage_path = Path(str(a.failed_prefix)+'-disk-adapter.json')
    resource, adapter, storage = (document(x) for x in (resource_path, adapter_path, storage_path))
    if (resource['exitcode'] != 1 or resource['termination_signal'] is not None
            or not resource['wait4_observed'] or adapter['completed'] is not False
            or adapter['read_calls'] != 2 or adapter['restored_objects'] != 1
            or adapter['physical_profile_or_raw_arrays_modified'] or adapter['worker_started']
            or adapter['input_raw']['sha256'] != sha(a.raw)
            or adapter['input_checkpoint']['sha256'] != sha(a.checkpoint)
            or not all(x['original_full_raw_reader_passed'] for x in adapter['observations'])
            or storage['stats']['assembled_matrices'] != 1 or storage['stats']['factors'] != 1
            or storage['stats']['linear_solves'] != 12):
        raise ValueError('The actual six-complete/one-later-error boundary differs')
    events = []
    for line in log_path.read_text().splitlines():
        try:
            events.append(json.loads(line))
        except (json.JSONDecodeError, TypeError):
            continue
    rows = [j for j in events if j.get('event') == 'actual_fixed_external_response']
    solves = [j for j in events if j.get('event') == 'disk_linear_solve_checked']
    factor_events = [j for j in events if j.get('event') == 'actual_fixed_control_factor']
    errors = [j for j in events if j.get('event') == 'error']
    if (tuple(j['field'] for j in rows) != FIELDS or len(solves) != 12
            or len(factor_events) != 1 or not all(j['passed'] for j in solves)
            or not any(j.get('error') == "KeyError('a0')" for j in errors)):
        raise ValueError('Original complete column receipts or later provider failure differ')
    M, nodes, q = int(saved['modes']), identity['nodes'], saved['gauge_amplitude']
    n = 3*M+1
    units = np.r_[saved['core']['coefficients'][0], saved['central_correction_scales']]
    physical = np.r_[np.full(n*nodes, q), units]
    if units.shape != (M,):
        raise ValueError('Original full fixed-core parameter units differ')
    directions, arrays, column_bounds = {}, [], []
    for row in rows:
        name = row['field']
        path = Path(str(a.failed_prefix)+'-external-'+name+'.npy.gz')
        data = path.read_bytes()
        direction = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
        if (direction.dtype != np.float64 or direction.shape != (n*nodes+M,)
                or not np.isfinite(direction).all()
                or not np.array_equal(units*direction[n*nodes:], row['physical_core_derivative'])
                or row['half_step_response_relative_difference'] > 2e-4
                or row['half_width'] != row['width']/2):
            raise ValueError('Saved complete external direction or actual half gate differs: '+name)
        directions[name] = direction
        norm = float(np.max(abs(physical*direction)))
        # This is an explicitly numerical estimate, not a directed-rounding
        # interval theorem. The measured original scalar is retained verbatim.
        bound = (row['half_step_response_relative_difference']+2e-14)*norm
        column_bounds.append(bound)
        arrays.append(dict(file=str(path), sha256=hashlib.sha256(data).hexdigest(),
                           bytes=len(data), shape=list(direction.shape), original_completed_external=True))
        hashes[str(path)] = sha(path)
    for path in (resource_path, log_path, adapter_path, storage_path):
        hashes[str(path)] = sha(path)
    Z = np.column_stack([directions[name] for name in FIELDS[:3]])
    low = units[:3, None]*Z[n*nodes:n*nodes+3]
    inverse = np.linalg.solve(low, np.eye(3))
    singular = np.linalg.svd(low, compute_uv=False)
    scaled_Z = physical[:, None]*Z
    error = np.asarray(column_bounds[:3])
    C = abs(inverse)@np.tile(error, (3, 1))
    rho = float(np.linalg.norm(C, ord=np.inf))
    if not np.isfinite(rho) or rho >= 1:
        raise ValueError('Original external half errors do not control low-core exchange numerically')
    inverse_majorant = np.linalg.solve(np.eye(3)-C, abs(inverse))
    if np.min(inverse_majorant) < -1e-12:
        raise ValueError('The numerical positive perturbation majorant is invalid')

    def save_array(name, value):
        stream = io.BytesIO()
        np.save(stream, np.asarray(value), allow_pickle=False)
        data = gzip.compress(stream.getvalue(), mtime=0)
        path = Path(str(a.out_prefix)+'-'+name+'.npy.gz')
        write_new(path, data)
        item = dict(file=str(path), sha256=hashlib.sha256(data).hexdigest(), bytes=len(data),
                    shape=list(np.shape(value)), algebraic_combination_only=True)
        arrays.append(item)
        return item

    def perturbation_estimate(weights, source_error=0.):
        forcing = np.full(3, source_error+float(error@abs(weights)))
        dw = inverse_majorant@forcing
        bound = source_error+float(np.max(abs(scaled_Z)@dw))+float(error@(abs(weights)+dw))
        return bound, dw

    prescribed, neutral = [], []
    for j, name in enumerate(('actual_q1', 'actual_q4', 'actual_c6')):
        weights = inverse[:, j]
        direction = Z@weights
        core = units*direction[n*nodes:]
        bound, dw = perturbation_estimate(weights)
        norm = float(np.max(abs(physical*direction)))
        prescribed.append(dict(direction=name,
            physical_profile_derivative={key:float(value) for key, value in zip(FIELDS[:3], weights)},
            core_derivative=core.tolist(), low_core_target_error=float(np.max(abs(core[:3]-np.eye(3)[:, j]))),
            half_step_exchange_response_relative_difference=None,
            half_step_exchange_numerical_perturbation_bound=bound/max(norm, np.finfo(float).tiny),
            original_combined_half_vector_was_not_saved=True,
            equation_relative_backward_error=None, combined_matrix_residual_not_remeasured=True))
        save_array('prescribed-'+name, direction)
    for index, name in enumerate(FIELDS[3:], start=3):
        source = directions[name]
        weights = -np.linalg.solve(low, units[:3]*source[n*nodes:n*nodes+3])
        direction = source+Z@weights
        core = units*direction[n*nodes:]
        bound, dw = perturbation_estimate(weights, column_bounds[index])
        norm = float(np.max(abs(physical*direction)))
        neutral.append(dict(external_field=name,
            physical_profile_derivative={name:1., **{key:float(value) for key, value in zip(FIELDS[:3], weights)}},
            core_derivative=core.tolist(), low_core_derivative_max=float(np.max(abs(core[:3]))),
            half_step_combination_relative_difference=None,
            half_step_combination_numerical_perturbation_bound=bound/max(norm, np.finfo(float).tiny),
            original_combined_half_vector_was_not_saved=True,
            equation_relative_backward_error=None, combined_matrix_residual_not_remeasured=True))
        save_array('core-held-'+name, direction)
    if max([j['low_core_target_error'] for j in prescribed]+[j['low_core_derivative_max'] for j in neutral]) > 1e-9:
        raise ValueError('Recovered complete full directions did not enforce low-core targets')
    rms = original.raw_flat(a.raw, raw, 'rms', hashes)
    result = dict(scope=__doc__, schema='fixed-actual-to-three-control-response-v1',
        finished=True, finished_means='Only this six-column recovery/algebraic assembly finished.',
        inspection_only=True, new_solution=False, tail_worker_started=False,
        partial_recovery=True, original_eight_control_job_finished=False,
        original_eight_control_job_exitcode=1, original_failure="KeyError('a0') at first nonzero frontload",
        original_requested_fields=[*FIELDS, 'initial_speed_frontload', 'vd'],
        unavailable_fields=['initial_speed_frontload', 'vd'], fields=list(FIELDS),
        input_identity=identity, source_sha256=hashes,
        original_producer_provenance=producer,
        baseline=dict(profile=saved['frozen_profile'], core=saved['core']['coefficients'], gauge=q,
            numerical_reference_knots=raw['identity']['numerical_reference_knots'],
            reference_coefficients=saved['chart_reference_coefficients'],
            actual_physical_bc_max=saved['summary']['physical_bc_max'],
            actual_physical_bc_source='Original fully accepted physical summary; no new RHS evaluated here.',
            accepted_rms_max=max(rms), raw_state_bitwise_equal=True),
        modes=M, angular=identity['angular'], nodes=nodes,
        external_responses=rows, original_external_full_and_half_steps_recomputed=False,
        all_six_original_external_full_and_half_gates_observed=True,
        physical_core_parameter_scales=units.tolist(), low_three_core_by_physical_control=low.tolist(),
        control_order=list(FIELDS[:3]), half_step_low_three_core_by_physical_control=None,
        low_exchange_condition=dict(singular_values=singular.tolist(), condition_2=float(singular[0]/singular[-1]),
            observed_half_step_matrix_perturbation_norm=None, numerical_infinity_perturbation_majorant=rho,
            scope='Numerical propagation of original measured per-column errors; not an interval certificate.'),
        prescribed_low_core_responses=prescribed, additional_core_held_directions=neutral,
        tangent_arrays=arrays, radial_batch_size=48, collocation_batch_size=24,
        original_resources=resource, original_disk_adapter=storage,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        limitations=['Original six full external arrays and their measured half-step receipts are genuine.',
            'The half arrays and forcing arrays were not persisted, so combined direct checks are null.',
            'The separately named perturbation bounds are numerical estimates, not substitute measured results.',
            'Only local warm construction/geometry screening is authorized by this packet; every new BVP gate remains.'])
    path = a.out_prefix.with_suffix('.json')
    write_new(path, (json.dumps(result, indent=2, allow_nan=False)+'\n').encode())
    print(json.dumps(dict(event='six_completed_columns_recovered', output=str(path), sha256=sha(path),
        original_eight_control_job_finished=False, available_fields=list(FIELDS),
        low_exchange_condition_2=float(singular[0]/singular[-1]), half_perturbation_majorant=rho,
        prescribed_half_estimates=[j['half_step_exchange_numerical_perturbation_bound'] for j in prescribed],
        neutral_half_estimates=[j['half_step_combination_numerical_perturbation_bound'] for j in neutral])), flush=True)


if __name__ == '__main__':
    main()
