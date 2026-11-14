#!/usr/bin/env python3
"""Small read-only check of one saved R149 atlas field and its true jets.

Two actual cell interiors, eight labels and the two coast interfaces are
queried. No BVP residual/Jacobian matrix or body integration is constructed.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField
from fd2d_gc_raw_bump_ruling_atlas import DirectLabelCoastReference
from fd2d_gc_ruling_reference_second_jets import ruling_reference_second_jets


def packed(q, suffix=''):
    return np.stack([q[k+suffix] for k in ('n', 'm', 'l')], axis=-1)


def maximum(q):
    return float(np.max(abs(q), initial=0.))


def error(got, expected):
    d = got-expected
    return dict(absolute_maximum=maximum(d), scaled_maximum=maximum(d)/max(1., maximum(expected)),
        relative_l2=float(np.linalg.norm(d)/max(1., np.linalg.norm(expected))))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('field', 'candidate', 'inlet', 'cache', 'out-prefix'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args(); start = time.monotonic(); stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh native check prefix')
    here = Path(__file__).resolve().parent
    names = ('fd2d-metric-ruling-atlas-native-check.py', 'fd2d_gc_ruling_atlas_native_field.py',
        'fd2d_gc_ruling_reference_second_jets.py', 'fd2d_gc_frozen_ruling_atlas.py',
        'fd2d_gc_raw_bump_ruling_atlas.py')
    sources = [identity(here/name) for name in names]
    original_input = identity(args.field)
    r = RulingAtlasRawBumpNativeField(args.field, args.candidate,
        reference_inlet=args.inlet, reference_cache=args.cache)
    e, f = r.angular_atlas.entry_s, r.angular_atlas.exit_s
    mids = (r.nodes[:-1]+r.nodes[1:])/2
    coast_ids = np.flatnonzero((mids > e)&(mids < f))
    exit_ids = np.flatnonzero((mids > f)&(mids < r.angular_atlas.exit_stop))
    cells = [int(coast_ids[np.argmin(abs(mids[coast_ids]-(e+.6*(f-e))))]),
             int(exit_ids[np.argmin(abs(mids[exit_ids]-(f+.5*(r.angular_atlas.exit_stop-f))))])]
    indices = np.array([5, 17, 31, 53, 71, 89, 107, 123])
    xi = np.asarray(r.angular_atlas.theta[indices], float)
    records = []; samples = {}
    for index, cell in enumerate(cells):
        x = float(mids[cell]); q = r.evaluate_native(x, xi)
        step = min(2e-5, (r.nodes[cell+1]-r.nodes[cell])/8)
        checks = []
        for h in (step, step/2):
            xp, xm = r.evaluate_native(x+h, xi), r.evaluate_native(x-h, xi)
            up, um = r.evaluate_native(x, xi+h), r.evaluate_native(x, xi-h)
            checks.append(dict(step=h,
                x=error((packed(xp)-packed(xm))/(2*h), packed(q, '_x')),
                xi=error((packed(up)-packed(um))/(2*h), packed(q, '_xi')),
                xixi=error((packed(up, '_xi')-packed(um, '_xi'))/(2*h), packed(q, '_xixi')),
                x_xi=error((packed(xp, '_xi')-packed(xm, '_xi'))/(2*h), packed(q, '_x_xi'))))
        material = r.physical(x, q['u'])
        inverse = dict(material_inverse_residual=maximum(material['angle_inverse_error']),
            recovered_label_error=maximum(material['xi']-xi),
            field_value_roundtrip_error=maximum(packed(material)-packed(q)))
        records.append(dict(actual_saved_cell=cell, physical_s=x, finite_difference_checks=checks,
                            fixed_material_roundtrip=inverse))
        for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'):
            samples[f'point_{index}{suffix}'] = packed(q, suffix)
    reference_s = float(mids[cells[0]])
    chart = r.angular_atlas.coordinates([reference_s], coordinate=xi)
    direct = DirectLabelCoastReference(r.coast_reference, r.angular_atlas)
    first = direct.jet_on_grid(np.array([reference_s]), chart, active_mask=np.array([True]))
    second = ruling_reference_second_jets(r.angular_atlas, reference_s, xi)
    composed = dict(values=second['values'],
        x=second['physical_s']+np.asarray(chart['u_s'][:, 0], float)[:, None]*second['physical_u'],
        xi=np.asarray(chart['u_xi'][:, 0], float)[:, None]*second['physical_u'])
    reference_comparison = {key: maximum(composed[key]-first[key][:, 0]) for key in composed}
    interface_rows = []
    for x in (e, f):
        left, right = r.evaluate_native(x, xi, side='left'), r.evaluate_native(x, xi, side='right')
        cl, cr = r.chart(x, xi, side='left'), r.chart(x, xi, side='right')
        values = {suffix or 'value': maximum(packed(left, suffix)-packed(right, suffix))
                  for suffix in ('', '_xi', '_xixi')}
        physical_left = r.physical(x, left['u'], side='left')
        physical_right = r.physical(x, left['u'], side='right')
        physical = {suffix or 'value': maximum(packed(physical_left, suffix)-packed(physical_right, suffix))
                    for suffix in ('', '_u', '_uu')}
        interface_rows.append(dict(physical_s=x, common_field_trace_errors=values,
            common_physical_trace_errors=physical,
            common_chart_trace_errors={key: maximum(cl[key]-cr[key]) for key in ('u', 'u_xi', 'u_xixi')},
            actual_one_sided_U_s_jump=maximum(cl['u_x']-cr['u_x']),
            actual_one_sided_field_s_jump=maximum(packed(physical_left, '_s')-packed(physical_right, '_s')),
            radial_derivative_continuity_required=False))
    definition_path = stem.with_name(stem.name+'-definition.json')
    definition_path.write_text(json.dumps(r.definition(), indent=2, allow_nan=False)+'\n')
    restored = RulingAtlasRawBumpNativeField.from_definition(definition_path)
    restored_error = 0.
    for index, cell in enumerate(cells):
        q = restored.evaluate_native(mids[cell], xi)
        for suffix in ('', '_x', '_xi', '_xixi', '_x_xi'):
            restored_error = max(restored_error, maximum(packed(q, suffix)-samples[f'point_{index}{suffix}']))
    samples.update(xi=xi, actual_cells=np.array(cells), physical_s=mids[cells])
    arrays = save_npz(stem.with_name(stem.name+'-samples.npz'), **samples)
    fine_max = max(row['finite_difference_checks'][-1][key]['scaled_maximum']
        for row in records for key in ('x', 'xi', 'xixi', 'x_xi'))
    trace_max = max(value for row in interface_rows for key in
        ('common_field_trace_errors', 'common_physical_trace_errors', 'common_chart_trace_errors')
        for value in row[key].values())
    inverse_max = max(row['fixed_material_roundtrip']['material_inverse_residual'] for row in records)
    checks = dict(fine_actual_derivatives=fine_max < 5e-5,
        same_original_direct_label_first_jets=max(reference_comparison.values()) < 1e-10,
        complete_angular_and_physical_interface_traces=trace_max < 5e-10,
        actual_single_sided_chart_jumps_retained=all(row['actual_one_sided_U_s_jump'] > 1e-4 for row in interface_rows),
        material_inverse=inverse_max < 1e-12, exact_definition_roundtrip=restored_error == 0.,
        input_unchanged=identity(args.field) == original_input,
        sources_unchanged=all(identity(row['path'])['sha256'] == row['sha256'] for row in sources))
    report = dict(schema='fd2d-R149-actual-atlas-native-small-check-v1', actual_execution=True,
        passed=all(checks.values()), checks=checks, sources=sources, field=original_input,
        candidate=identity(args.candidate), inlet=identity(args.inlet), cache=identity(args.cache),
        actual_node_count=len(r.nodes), angular_indices=indices.tolist(), point_queries=records,
        reference_first_jet_comparison=reference_comparison, interface_queries=interface_rows,
        maximum_fine_fd_scaled_error=fine_max, maximum_common_trace_error=trace_max,
        maximum_material_inverse_residual=inverse_max, definition_reload_difference=restored_error,
        definition=identity(definition_path), samples=arrays,
        body_integration_run=False, BVP_or_Jacobian_matrix_assembled=False,
        nonlinear_solve_performed=False, continuous_certificate=False,
        seconds=time.monotonic()-start, maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    output = stem.with_name(stem.name+'-report.json')
    output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(output), passed=report['passed'], checks=checks,
        seconds=report['seconds'], maximum_rss_kib=report['maximum_rss_kib'],
        maximum_fine_fd_scaled_error=fine_max, maximum_common_trace_error=trace_max,
        maximum_material_inverse_residual=inverse_max),allow_nan=False),flush=True)
    raise SystemExit(0 if report['passed'] else 1)


if __name__ == '__main__':
    main()
