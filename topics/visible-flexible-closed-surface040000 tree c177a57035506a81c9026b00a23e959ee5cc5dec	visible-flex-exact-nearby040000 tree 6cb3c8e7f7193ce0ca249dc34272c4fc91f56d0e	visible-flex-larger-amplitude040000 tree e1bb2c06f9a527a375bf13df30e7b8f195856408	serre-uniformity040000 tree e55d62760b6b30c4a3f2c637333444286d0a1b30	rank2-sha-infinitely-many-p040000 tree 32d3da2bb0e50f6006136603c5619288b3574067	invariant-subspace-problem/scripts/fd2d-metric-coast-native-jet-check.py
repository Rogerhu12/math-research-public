#!/usr/bin/env python3
"""Small actual-field check of the explicit R144 native reader.

Two already used Gauss2 radial points and eight angles suffice to exercise
the rim, plateau, angular chain and true cell derivatives. This is a finite
interface/derivative check, not a global residual or geometry certificate.
No BVP operator, large matrix or body integration is constructed.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_bump_coast_native_field import RawBumpCoastNativeField, window
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField


def packed(q, suffix=''):
    return np.stack([q[name+suffix] for name in ('n', 'm', 'l')], axis=-1)


def errors(actual, exact):
    difference = np.asarray(actual)-np.asarray(exact)
    return dict(absolute_maximum=float(np.max(abs(difference))),
        scaled_maximum=float(np.max(abs(difference))/max(1., np.max(abs(exact)))),
        relative_l2=float(np.linalg.norm(difference)/max(1., np.linalg.norm(exact))))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ('field', 'candidate', 'inlet', 'cache', 'prefill-report', 'out-prefix'):
        ap.add_argument('--'+key, type=Path, required=True)
    args = ap.parse_args(); start = time.monotonic()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Preserve earlier checks and use a fresh output prefix')
    input_identity = identity(args.field)
    source_names = ('fd2d-metric-coast-native-jet-check.py', 'fd2d_gc_bump_coast_native_field.py',
                    'fd2d_gc_frozen_coast_second_jets.py', 'fd2d_gc_frozen_coast_reference.py')
    here = Path(__file__).resolve().parent
    sources = [identity(here/name) for name in source_names]
    reader = RawBumpCoastNativeField(args.field, args.candidate,
        reference_inlet=args.inlet, reference_cache=args.cache)
    prefill = json.loads(args.prefill_report.read_text())
    if prefill['inlet']['sha256'] != identity(args.inlet)['sha256']:
        raise ValueError('The recorded Gauss2 points bind a different inlet')
    gauss = [row['physical_s'] for row in prefill['rows'] if row['Gauss2_point']]
    entry, length = reader.coast_reference.entry_s, reader.coast_reference.length
    rim = length*reader.reference_rim_fraction
    first_rim = next(x for x in gauss if entry < x < entry+rim)
    plateau = next(x for x in gauss if entry+rim < x < entry+length-rim)
    points = [first_rim, plateau]
    angular_indices = np.array([5, 17, 31, 53, 71, 89, 107, 123])
    xi = 2*np.pi*angular_indices/256
    rows, samples = [], {}
    for index, x in enumerate(points):
        q = reader.evaluate_native(x, xi)
        plain = RawBumpSeedNativeField.evaluate_native(reader._plain_lifting_view, x, xi)
        correction = reader._correction_jets(np.full(len(xi), x), xi, 'right')
        ref = reader.coast_reference.jet_on_grid(np.array([x]),
            dict(u=q['u'][:, None], u_s=q['U_x'][:, None], u_xi=q['U_xi'][:, None]),
            active_mask=np.array([True]))
        w, ws = window(x, entry, length, reader.reference_rim_fraction)
        first_matches = {}
        for key, suffix in (('values', ''), ('x', '_x'), ('xi', '_xi')):
            expected = correction[key]+(1-w)*packed(plain, suffix)+w*ref[key][:, 0]
            if key == 'x':
                expected += ws*(ref['values'][:, 0]-packed(plain))
            first_matches[key] = errors(packed(q, suffix), expected)
        j = int(q['cell'][0])
        cell_distance = min(x-reader.nodes[j], reader.nodes[j+1]-x)
        h = min(2e-5, cell_distance/8)
        if h <= 1e-8:
            raise ValueError('The selected actual Gauss2 point is too close to its saved node for this check')
        finite = []
        for step in (h, h/2):
            plus_x = reader.evaluate_native(x+step, xi)
            minus_x = reader.evaluate_native(x-step, xi)
            plus_u = reader.evaluate_native(x, xi+step)
            minus_u = reader.evaluate_native(x, xi-step)
            estimates = dict(
                x=errors((packed(plus_x)-packed(minus_x))/(2*step), packed(q, '_x')),
                xi=errors((packed(plus_u)-packed(minus_u))/(2*step), packed(q, '_xi')),
                xixi=errors((packed(plus_u, '_xi')-packed(minus_u, '_xi'))/(2*step), packed(q, '_xixi')),
                x_xi=errors((packed(plus_x, '_xi')-packed(minus_x, '_xi'))/(2*step), packed(q, '_x_xi')))
            finite.append(dict(step=float(step), comparisons=estimates))
        rows.append(dict(physical_s=float(x), actual_saved_cell=j, weight=float(w), weight_s=float(ws),
            query_kind='previously evaluated actual Gauss2 point',
            original_first_jet_cache_formula_comparisons=first_matches,
            derivative_checks=finite))
        for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'):
            samples[f'point_{index}_field{suffix}'] = packed(q, suffix)
        samples[f'point_{index}_material_u'] = q['u']

    # Outside the reference support and at its exact endpoints the archived
    # P1 field must remain exactly the existing explicit-seed field.
    plain_actual = RawBumpSeedNativeField(args.field, args.candidate)
    outside = []
    for x in (0., entry, reader.coast_reference.exit_s, reader.profile.end):
        q, old = reader.evaluate_native(x, xi), plain_actual.evaluate_native(x, xi)
        outside.append(dict(physical_s=float(x), differences={suffix or 'value':
            float(np.max(abs(packed(q, suffix)-packed(old, suffix))))
            for suffix in ('', '_x', '_xi', '_xixi', '_x_xi')}))
    definition_path = stem.with_name(stem.name+'-definition.json')
    definition_path.write_text(json.dumps(reader.definition(), indent=2, allow_nan=False)+'\n')
    restored = RawBumpCoastNativeField.from_definition(definition_path)
    restore_max = 0.
    for index, x in enumerate(points):
        q = restored.evaluate_native(x, xi)
        for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'):
            restore_max = max(restore_max, float(np.max(abs(packed(q, suffix)-samples[f'point_{index}_field{suffix}']))))
    samples.update(physical_s=np.array(points), xi=xi, angular_indices=angular_indices)
    arrays = save_npz(stem.with_name(stem.name+'-samples.npz'), **samples)
    max_first = max(v['absolute_maximum'] for row in rows for v in row['original_first_jet_cache_formula_comparisons'].values())
    max_fd = max(v['scaled_maximum'] for row in rows for v in row['derivative_checks'][-1]['comparisons'].values())
    max_outside = max(v for row in outside for v in row['differences'].values())
    inputs_unchanged = input_identity == identity(args.field)
    sources_unchanged = sources == [identity(here/name) for name in source_names]
    passed = bool(max_first < 2e-10 and max_fd < 5e-5 and max_outside < 2e-12
                  and restore_max == 0 and inputs_unchanged and sources_unchanged)
    report = dict(schema='fd2d-R144-actual-native-small-jet-check-v1', passed=passed,
        actual_execution=True, field=input_identity, candidate=identity(args.candidate), inlet=identity(args.inlet),
        cache=identity(args.cache), previous_prefill=identity(args.prefill_report), sources=sources,
        actual_saved_mesh_node_count=len(reader.nodes), actual_saved_parameters_unchanged=inputs_unchanged,
        reference_binding_sha256=reader.coast_reference.binding_sha256,
        finite_angular_indices=angular_indices.tolist(), finite_angular_work=256,
        rows=rows, outside_and_endpoint_comparisons=outside,
        maximum_first_jet_comparison=max_first, maximum_fine_fd_scaled_error=max_fd,
        maximum_outside_and_endpoint_difference=max_outside, exact_definition_reload_difference=restore_max,
        reference_second_jets=reader.coast_second_jets.definition(),
        definition=identity(definition_path), samples=arrays, source_bytes_unchanged=sources_unchanged,
        fixed_material_body_interface_inherited=True, body_integration_run=False,
        large_matrix_assembled=False, nonlinear_solve_performed=False,
        complete_residual_or_geometry_certified=False, seconds=time.monotonic()-start,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    output = stem.with_name(stem.name+'-report.json')
    output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(output), passed=passed, seconds=report['seconds'],
        maximum_first_jet_comparison=max_first, maximum_fine_fd_scaled_error=max_fd,
        maximum_outside_and_endpoint_difference=max_outside,
        definition_reload_difference=restore_max, maximum_rss_kib=report['maximum_rss_kib']), allow_nan=False), flush=True)
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
