#!/usr/bin/env python3
"""Read the complete current nine-control response as full-core design data.

AI-assisted research, strong_recovery, 2026-11-13.
The exact rational operations below apply to stored Float64 coefficients and
stored numerical tangent entries. They do not certify the numerical tangent,
a continuous BVP, a finite step, or a closed-surface Hausdorff amplitude.
All nine complete prescribed/core-held fields are checked against their saved
SHA256 and all 32 actual core derivatives. No ODE, Jacobian, QR, tail worker,
or new geometric field is evaluated.
"""
from __future__ import annotations
import argparse
import datetime
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
import os
from pathlib import Path
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np
import strong_actual_fixed_control_response as original

HERE = Path(__file__).resolve().parent
ORIGINAL_SHA = 'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1'
PRODUCER_SHA = 'd83947ea4f7457435a272863b9ba88a9a7ddfe551e76dc4db596c63dc61de212'
FIELDS = ('delta', 'boost_length', 'boost_speed', 'vu',
          'descending_turn_curvature', 'start_acceleration',
          'initial_speed_frontload', 'vd', 'descending_sync_curvature')
DIRECTIONS = ('actual_q1', 'actual_q4', 'actual_c6', *FIELDS[3:])


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    payload = Path(path).read_bytes()
    return json.loads(gzip.decompress(payload) if str(path).endswith('.gz') else payload)


def exact(value):
    return Fraction.from_float(float(value))


def rational(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                display=float(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('response', 'owned-resource', 'checkpoint', 'raw', 'tail', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh output path')
    checks, inputs = {}, {str(Path(__file__)): sha(__file__)}

    def check(name, condition):
        if not condition:
            raise ValueError('Current complete-response core check failed: '+name)
        checks[name] = True

    def load(path):
        inputs[str(path)] = sha(path)
        return read(path)

    check('original_input_reader_source', sha(HERE/'strong_actual_fixed_control_response.py') == ORIGINAL_SHA)
    check('actual_current_response_producer_source', sha(HERE/'strong_samechart_initial_laws_anchor_response.py') == PRODUCER_SHA)
    response, resource = load(args.response), load(args.owned_resource)
    check('original_owned_exit_zero', resource.get('exitcode') == 0 and resource.get('wait4_observed') is True)
    command = resource['command']
    for name, path in (('--response-checkpoint', args.checkpoint),
                       ('--response-raw', args.raw), ('--response-tail', args.tail)):
        check('owned_'+name[2:].replace('-', '_'), command.count(name) == 1
              and Path(command[command.index(name)+1]).resolve() == path.resolve())
    check('original_completed_schema', response.get('schema') == 'fixed-actual-to-three-control-response-v1'
          and response.get('finished') is True and response.get('new_solution') is False
          and response.get('tail_worker_started') is False)
    check('actual_nine_physical_fields', response['fields'] == list(FIELDS))
    saved, raw, tail, unused_vectors, identity = original.validate_inputs(
        args.checkpoint, args.raw, args.tail, inputs)
    check('same_32_mode_actual_baseline', saved['modes'] == response['modes'] == 32
          and saved['core']['frequencies'] == list(range(2, 65, 2))
          and response['nodes'] == identity['nodes']
          and response['angular'] == saved['config']['angular'])
    check('same_complete_core_and_physical_profile', response['baseline']['core'] == saved['core']['coefficients']
          and response['baseline']['profile'] == saved['frozen_profile']
          and response['baseline']['gauge'] == saved['gauge_amplitude'])
    for path in (args.checkpoint, args.raw, args.tail):
        check('response_source_'+path.name, response['source_sha256'].get(str(path)) == sha(path))
    check('actual_original_response_provenance', response['source_sha256'].get(
        str(HERE/'strong_samechart_initial_laws_anchor_response.py')) == PRODUCER_SHA)
    M, nodes = saved['modes'], response['nodes']
    units = np.r_[saved['core']['coefficients'][0], saved['central_correction_scales']]
    check('all_32_parameter_units', units.shape == (M,) and np.array_equal(
        units, response['physical_core_parameter_scales']))
    c = list(map(exact, saved['core']['coefficients']))
    modes = list(range(2, 65, 2))
    weights = [2 if m % 4 == 2 else 0 for m in modes]
    gap = sum(w*v for w, v in zip(weights, c))
    rho_weights = [(m*m-1)*((-1)**j) for j, m in enumerate(modes)]
    rho = 1+sum(w*v for w, v in zip(rho_weights, c))
    k0 = exact(saved['frozen_profile']['start_acceleration'])
    floors = (16, 24, 32, 40, 48)
    core_tail = {str(lo): rational(sum((m*m-1)*abs(v) for m, v in zip(modes, c) if m >= lo))
                 for lo in floors}
    check('positive_current_axis_gap_and_short_radius', gap > 0 and rho > 0 and k0 > 0)
    rows = response['prescribed_low_core_responses']+response['additional_core_held_directions']
    check('all_nine_declared_complete_direction_rows',
          [row.get('direction', row.get('external_field')) for row in rows] == list(DIRECTIONS))
    output_rows = []
    for index, (name, row) in enumerate(zip(DIRECTIONS, rows)):
        suffix = '-'+('prescribed-' if index < 3 else 'core-held-')+name+'.npy.gz'
        entries = [item for item in response['tangent_arrays'] if item['file'].endswith(suffix)]
        check(name+'_unique_complete_array', len(entries) == 1)
        item = entries[0]; path = Path(item['file']); payload = path.read_bytes()
        check(name+'_complete_array_sha256', hashlib.sha256(payload).hexdigest() == item['sha256'])
        inputs[str(path)] = item['sha256']
        value = np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False)
        check(name+'_complete_array_shape_and_finiteness', value.shape == ((3*M+1)*nodes+M,)
              and value.dtype == np.float64 and np.isfinite(value).all())
        dc_float = units*value[-M:]
        row_core = np.asarray(row['core_derivative'], dtype=np.float64)
        check(name+'_all_32_core_entries_same_bits', row_core.shape == (M,)
              and dc_float.astype('<f8').tobytes() == row_core.astype('<f8').tobytes())
        dc = list(map(exact, dc_float))
        dg = sum(w*v for w, v in zip(weights, dc))
        drho = sum(w*v for w, v in zip(rho_weights, dc))
        dk0 = exact(row['physical_profile_derivative'].get('start_acceleration', 0.))
        derivative_r7 = dk0*gap*rho+k0*dg*rho+k0*gap*drho
        half_key = ('half_step_exchange_response_relative_difference' if index < 3
                    else 'half_step_combination_relative_difference')
        check(name+'_finite_original_exchange_observations', all(math.isfinite(float(row[key]))
              for key in (half_key, 'equation_relative_backward_error')))
        output_rows.append(dict(direction=name, original_complete_array=item,
            physical_profile_derivative=row['physical_profile_derivative'],
            complete_core_derivative=row['core_derivative'],
            exact_saved_binary_full_axis_gap_derivative=rational(dg),
            twice_low_q_derivative=rational(2*dc[0]),
            contribution_from_other_odd_modes=rational(dg-2*dc[0]),
            exact_saved_binary_short_radius_derivative=rational(drho),
            exact_saved_binary_first_order_R7_product_derivative=rational(derivative_r7),
            weighted_tail_derivative_l1={str(lo): rational(sum((m*m-1)*abs(v)
                for m, v in zip(modes, dc) if m >= lo)) for lo in floors},
            original_half_step_observation=row[half_key],
            original_equation_relative_backward_error=row['equation_relative_backward_error'],
            original_low_core_observation=row.get('low_core_target_error', row.get('low_core_derivative_max'))))
    result = dict(schema='actual-complete-nine-control-core-design-budget-v1', scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256=sha(__file__), input_sha256=inputs, checks=checks, all_checks=True,
        original_owned_response_resource=str(args.owned_resource),
        modes=M, nodes=nodes, angular=response['angular'], complete_baseline_identity=identity,
        baseline=dict(core=saved['core']['coefficients'], profile=saved['frozen_profile'],
            exact_saved_binary_axis_gap=rational(gap), exact_saved_binary_rho_short=rational(rho),
            exact_saved_binary_R7_product=rational(k0*gap*rho), weighted_tail_l1=core_tail),
        full_axis_gap_linear_objective_weights=weights,
        exact_gap_formula='2*sum(c_m for m = 2 mod 4), retaining all 32 core modes',
        low_q_coordinate_alone_is_not_the_objective=True, directions=output_rows,
        original_combined_half_and_backward_observations_only=True,
        no_new_combined_stability_acceptance_gate_imposed=True,
        no_finite_step_or_geometry_predicted=True,
        complete_closed_Hausdorff_or_rigid_registration_not_claimed=True,
        new_ODE_Node_Jacobian_QR_or_geometry_calls=0)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False); stream.write('\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out), checks=len(checks),
        baseline_gap=float(gap), baseline_R7=float(k0*gap*rho),
        directions=[dict(direction=row['direction'],
            gap_derivative=row['exact_saved_binary_full_axis_gap_derivative']['display'],
            R7_derivative=row['exact_saved_binary_first_order_R7_product_derivative']['display'])
            for row in output_rows])), flush=True)


if __name__ == '__main__':
    main()
