#!/usr/bin/env python3
"""Use two accepted full fields as a secant predictor for the actual BVP.

Only the initial guess changes. Both input surfaces must have completed the
original actual-tail and physical audits. Their gauge, spectrum, reference
charts and tail problem agree; their physical prefix profiles may differ.
Every new candidate still runs the original full Newton, true-H nonlinear
tail, full Jacobian, final audit, RMS and physical boundary acceptance gates.
This predictor is not a control derivative or an accepted solution.
The optional initial-height hold subtracts a C2 quintic taper from the warm
height field only. This enables exact reuse of the current audited tail at
the first outer anchor; every changed H still requires the original solve.
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
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PRIMARY = ('delta', 'boost_length', 'boost_speed')
EXTERNAL = ('vu', 'vd', 'start_acceleration', 'descending_turn_curvature',
            'descending_sync_curvature', 'coast_outward', 'loop_ratio')
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}
_ACTIVE = None


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def argument(argv, name):
    if argv.count(name) != 1:
        raise ValueError('Require exactly one original argument '+name)
    return argv[argv.index(name)+1]


def verified_secant(reference, raw, target, shifts, payload=False):
    """Bind the explicit alternate predictor to the exact production inputs."""
    if _ACTIVE is None:
        raise ValueError('No complete two-accepted-field secant was prepared')
    record, warm = _ACTIVE
    if (str(reference) != record['current_reference'] or str(raw) != record['current_raw']
            or sha(reference) != record['current_reference_sha256']
            or sha(raw) != record['current_raw_sha256']
            or list(target) != record['target_core'] or dict(shifts) != record['external_shifts']):
        raise ValueError('The secant predictor belongs to different production inputs')
    return warm if payload else True


def prepare(options, argv):
    import numpy as np
    from scipy.interpolate import PPoly
    from strong_actual_fixed_control_response import raw_flat
    current_path = Path(argument(argv, '--actual-reference'))
    current_raw_path = Path(argument(argv, '--actual-reference-raw'))
    previous_path, previous_raw_path = options.secant_previous_reference, options.secant_previous_raw
    current, current_raw, previous, previous_raw = map(read,
        (current_path, current_raw_path, previous_path, previous_raw_path))
    sources = {str(path): sha(path) for path in
               (Path(__file__), current_path, current_raw_path, previous_path, previous_raw_path)}
    for surface, raw, path in ((current, current_raw, current_raw_path),
                                (previous, previous_raw, previous_raw_path)):
        if (not surface.get('solver_success') or surface.get('audit_pending', True)
                or not surface['config'].get('actual_nonlinear_tail')
                or not raw.get('solver_success') or raw.get('physical_surface') is not False
                or surface['raw_collocation_checkpoint']['sha256'] != sha(path)):
            raise ValueError('Two completely audited accepted actual states are required')
        for old_key, new_key in (('gauge', 'gauge_amplitude'), ('profile', 'frozen_profile'),
                ('reference_coefficients', 'chart_reference_coefficients'),
                ('reference_frequencies', 'chart_reference_frequencies'),
                ('physical_tail_parameters', 'physical_tail_parameters'),
                ('physical_tail_cut', 'physical_tail_cut')):
            if raw['identity'][old_key] != surface[new_key]:
                raise ValueError('Accepted raw/physical identity differs: '+old_key)
        if raw['identity']['numerical_reference_knots'] != surface['numerical_meridian_chart']['reference_t']:
            raise ValueError('Accepted raw/physical reference grid differs')
    for key in ('modes', 'gauge_amplitude', 'angular_chart', 'chart_reference_coefficients',
                'chart_reference_frequencies', 'central_correction_scales',
                'physical_tail_parameters', 'physical_tail_cut'):
        if previous[key] != current[key]:
            raise ValueError('Two-state secant changed the common representation: '+key)
    if (previous['config']['angular'] != current['config']['angular']
            or previous['numerical_meridian_chart']['reference_t'] != current['numerical_meridian_chart']['reference_t']):
        raise ValueError('The spectrum, angular resolution and material reference must agree')
    if ({key: value for key, value in previous['actual_tail']['config'].items() if key not in IO}
            != {key: value for key, value in current['actual_tail']['config'].items() if key not in IO}):
        raise ValueError('Two-state secant changed the complete finite-tail problem')
    if not 0 < options.secant_scale <= 4:
        raise ValueError('Use a finite positive secant step no larger than four prior steps')
    M = int(current['modes'])
    n = 3*M+1
    values = []
    for path, raw in ((previous_raw_path, previous_raw), (current_raw_path, current_raw)):
        arrays = {name: np.asarray(raw_flat(path, raw, name, sources), dtype=float).reshape(raw['arrays'][name]['shape'])
                  for name in ('x', 'y', 'p', 'cubic')}
        if (arrays['y'].shape != (n, len(arrays['x']))
                or arrays['cubic'].shape != (4, len(arrays['x'])-1, n)
                or arrays['p'].shape not in ((M,), (M+3,))
                or not np.array_equal(arrays['p'], raw['parameter_state'])):
            raise ValueError('The full accepted secant field dimensions differ')
        values.append(arrays)
    old, now = values
    if old['x'][0] != now['x'][0] or old['x'][-1] != now['x'][-1]:
        raise ValueError('The two material coordinate intervals differ')
    same_mesh = np.array_equal(old['x'], now['x'])
    prior_on_current = old['y'] if same_mesh else PPoly.construct_fast(
        old['cubic'], old['x'], extrapolate=False, axis=1)(now['x'])
    if not np.isfinite(prior_on_current).all():
        raise ValueError('The previous complete cubic did not cover the current mesh')
    old_core, new_core = np.asarray(previous['core']['coefficients']), np.asarray(current['core']['coefficients'])
    if not new_core[0] > old_core[0] > 0:
        raise ValueError('This continuation requires a real prior amplitude increase')
    scale = float(options.secant_scale)
    target = (new_core[:3]+scale*(new_core[:3]-old_core[:3])).tolist()
    old_profile, new_profile = previous['frozen_profile'], current['frozen_profile']
    for key in set(old_profile) | set(new_profile):
        if key not in PRIMARY+EXTERNAL and old_profile.get(key) != new_profile.get(key):
            raise ValueError('A profile change lies outside the explicit continuation controls: '+key)
    shifts = {key: scale*(new_profile[key]-old_profile[key]) for key in EXTERNAL
              if key in new_profile and new_profile[key] != old_profile[key]}
    direction = np.r_[scale*(now['y']-prior_on_current).ravel(order='F'),
                      scale*(now['p'][:M]-old['p'][:M])]
    pure_sha = hashlib.sha256(direction.astype('<f8').tobytes()).hexdigest()
    held = None
    if options.secant_hold_initial_height:
        field = direction[:now['y'].size].reshape(now['y'].shape, order='F')
        coordinate = (now['x']-now['x'][0])/(now['x'][-1]-now['x'][0])
        taper = coordinate**3*(10-15*coordinate+6*coordinate**2)
        taper[0], taper[-1] = 0., 1.
        removed = field[2*M+1:, -1].copy()
        correction = removed[:, None]*taper[None, :]
        field[2*M+1:] -= correction
        baseline_H = -float(current['gauge_amplitude'])*now['y'][2*M+1:, -1]
        first_H = -float(current['gauge_amplitude'])*(now['y'][2*M+1:, -1]+field[2*M+1:, -1])
        if baseline_H.tobytes() != first_H.tobytes():
            raise ValueError('The held initial complete H is not bitwise identical')
        held = dict(scope='Initial guess only; no boundary condition or accepted state is changed.',
            material_taper='u^3 (10 - 15u + 6u^2), u normalized over the accepted material interval',
            taper_value_first_second_jet_zero_at_inlet=True,
            taper_value_one_and_first_second_jet_zero_at_terminal=True,
            removed_terminal_raw_state_increment=removed.tolist(),
            maximum_raw_field_change=float(np.max(abs(correction))),
            maximum_physical_field_change=float(current['gauge_amplitude'])*float(np.max(abs(correction))),
            baseline_complete_H=baseline_H.tolist(),
            predicted_complete_H_bitwise_equal=True,
            complete_H_float64le_sha256=hashlib.sha256(baseline_H.astype('<f8').tobytes()).hexdigest(),
            original_near_inlet_correction_has_zero_terminal_weight=True,
            original_exact_audited_packet_guard_still_required_for_reuse=True,
            changed_H_always_requires_original_nonlinear_tail_and_full_J=True)
    geometry = np.asarray([scale*(new_profile[key]-old_profile[key]) for key in PRIMARY])
    record = dict(scope=__doc__, current_reference=str(current_path), current_raw=str(current_raw_path),
        current_reference_sha256=sha(current_path), current_raw_sha256=sha(current_raw_path),
        previous_reference=str(previous_path), previous_raw=str(previous_raw_path),
        source_sha256=sources, target_core=target, external_shifts=shifts, scale=scale,
        original_current_mesh_preserved=True, previous_mesh_identical=same_mesh,
        previous_field_evaluation='exact saved nodal array' if same_mesh else 'complete accepted numerical cubic at the current material nodes',
        geometry_increment=dict(zip(PRIMARY, map(float, geometry))),
        full_direction_shape=list(direction.shape),
        full_direction_float64le_sha256=hashlib.sha256(direction.astype('<f8').tobytes()).hexdigest(),
        pure_secant_direction_float64le_sha256=pure_sha,
        initial_complete_height_hold=held,
        warm_only=True, control_derivative_claim=False, nonlinear_solution=False,
        original_complete_Newton_tail_RMS_boundary_and_audit_required=True)
    warm = dict(fixed_parameter_and_field_increment=direction, geometry_increment=geometry,
                provenance=record)
    return record, warm


def main():
    global _ACTIVE
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--secant-previous-reference', type=Path, required=True)
    parser.add_argument('--secant-previous-raw', type=Path, required=True)
    parser.add_argument('--secant-scale', type=float, required=True)
    parser.add_argument('--secant-hold-initial-height', action='store_true')
    options, remaining = parser.parse_known_args()
    if any(key in remaining for key in ('--response-data', '--target-core', '--neutral-control-step',
            '--resume-actual-iterate', '--resume-tail-config', '--inspect-local-output')):
        raise ValueError('The explicitly accepted two-state secant supplies its own target, controls and warm field')
    _ACTIVE = prepare(options, remaining)
    record, _ = _ACTIVE
    remaining += ['--target-core', *map(repr, record['target_core'])]
    for name, value in record['external_shifts'].items():
        remaining += ['--neutral-control-step', name+'='+repr(value)]
    output = Path(argument(remaining, '--out-prefix'))
    output.parent.mkdir(parents=True, exist_ok=True)
    metadata = Path(str(output)+'-secant-predictor.json')
    if metadata.exists():
        raise ValueError('Use a fresh secant output prefix')
    sys.modules['strong_secant_actual_bvp'] = sys.modules[__name__]
    import strong_cached_prefix_actual_bvp as production
    original_build = production.build_wrapper

    def install(build, config):
        original = original_build(build, config)

        def wrapped(*args):
            source, provenance = original(*args)
            edits = [
                ('import types\n', 'import types\nfrom strong_secant_actual_bvp import verified_secant\n'),
                ('    if external_shifts and not options.response_data:\n',
                 '    if external_shifts and not options.response_data and not verified_secant(\n'
                 '            options.actual_reference, options.actual_reference_raw, target, external_shifts):\n'),
                ('    warm = None\n',
                 '    warm = verified_secant(options.actual_reference, options.actual_reference_raw,\n'
                 '        target, external_shifts, payload=True)\n'),
                ("complete_actual_tangent_warm=warm['provenance'] if warm else None",
                 "complete_accepted_secant_warm=warm['provenance'] if warm else None"),
                ('Complete actual-J warm field on the original residual quadrature and a complete-mean C2 cubic physical image; unsolved comparison only.',
                 'Complete two-accepted-field secant warm on the original residual quadrature and original physical cubic screen; no control derivative or new solution is claimed.'),
            ]
            for before, after in edits:
                if source.count(before) != 1:
                    raise ValueError('The original secant initial-guess source anchor changed')
                source = source.replace(before, after, 1)
            ast.parse(source, filename='<actual-secanted-initial-guess>')
            provenance['explicit_accepted_field_secant'] = dict(record,
                source_transforms=[dict(before=a, after=b, count=1) for a, b in edits],
                transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
                original_source_files_unchanged=True)
            metadata.write_text(json.dumps(provenance['explicit_accepted_field_secant'], indent=2)+'\n')
            return source, provenance

        return wrapped

    production.build_wrapper = install
    old_argv = sys.argv
    sys.argv = [old_argv[0], *remaining]
    try:
        production.main()
    finally:
        production.build_wrapper = original_build
        sys.argv = old_argv
        _ACTIVE = None


if __name__ == '__main__':
    main()
