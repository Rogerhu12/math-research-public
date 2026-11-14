#!/usr/bin/env python3
"""Finite full Gauss/Codazzi samples inside the actual saved P1 cells.

This uses true interpolant derivatives and the declared plateau lifting.
It does not solve a BVP, integrate a body map, or certify continuous bounds.
The trapezoid/Gauss comparisons hold computational xi fixed; they are not
claimed as fixed-material primitive estimates.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField
from fd2d_gc_three_field_residual import native_residuals

HERE = Path(__file__).resolve().parent
COMPONENTS = ('G', 'Rn', 'Rm')


def maximum(q):
    return float(np.max(np.abs(q), initial=0.))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--angles', type=int, default=512)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh actual diagnostic stem')
    if args.angles < 64 or args.angles % 4:
        raise ValueError('Use a positive multiple of four, at least 64, angular samples')
    started = time.monotonic()
    reader = RawBumpSeedNativeField(args.field, args.candidate)
    if args.angles <= 4*reader.K+2:
        raise ValueError('The diagnostic angular grid must resolve the retained Fourier modes')
    sources = [identity(Path(__file__))]+[identity(HERE/name) for name in
        ('fd2d_gc_bump_seed_native_field.py', 'fd2d_gc_bump_native_field.py',
         'fd2d_gc_raw_native_field.py', 'fd2d_gc_three_field_residual.py',
         'fd2d_gc_radial_bump_profile.py')]
    field_id = identity(args.field)
    definition_path = Path(str(stem)+'-definition.json')
    definition_path.write_text(json.dumps(reader.definition(), indent=2, allow_nan=False)+'\n')
    xi = 2*np.pi*np.arange(args.angles)/args.angles
    E = np.cos(xi[:, None]*reader.frequencies)
    O = np.sin(xi[:, None]*reader.frequencies[1:])
    PE = 2*E.T/args.angles; PE[0] *= .5
    PO = 2*O.T/args.angles
    gauss_low = .5-.5/np.sqrt(3.)
    fractions = np.array([0., gauss_low, .25, .5, .75, 1-gauss_low, 1.])
    peaks = {key: dict(maximum=-1.) for key in COMPONENTS}
    global_connection = dict(maximum=-1.)
    maxima, lows, highs, peak_xis, peak_us = [], [], [], [], []
    trap_max, gauss_max, mean_difference, oscillations = [], [], [], []
    trap_low_max, trap_high_max, gauss_low_max, gauss_high_max = [], [], [], []
    s_samples = []
    connection_max = []
    n_extrema, formal_curvature = [], []
    progress_path = Path(str(stem)+'-progress.jsonl')
    kwargs = ('a', 'a_s', 'a_ss', 'l', 'm', 'n', 'J', 'U_x', 'U_xi',
              'l_xi', 'm_xi', 'n_xi', 'm_x', 'n_x')
    last_print = started

    def project(value, component):
        basis, projection = (O, PO) if component == 'Rm' else (E, PE)
        return (basis@(projection@value.T)).T

    for cell, (left, right) in enumerate(zip(reader.nodes[:-1], reader.nodes[1:])):
        ss = left+(right-left)*fractions
        ss[0], ss[-1] = left, right
        q = reader.evaluate_native(ss[:, None], xi[None, :], side='left')
        # At both ends use THIS cell's genuine P1 slope, not the neighboring
        # cell selected by a global default derivative convention.
        qleft = reader.evaluate_native(float(left), xi, side='right')
        for key in q:
            q[key][0] = qleft[key]
        residual = native_residuals(**{key: q[key] for key in kwargs})
        full = np.stack([residual[key] for key in COMPONENTS], axis=-1)
        low = np.stack([project(full[:, :, j], key) for j, key in enumerate(COMPONENTS)], axis=-1)
        high = full-low
        maximum_rows = np.max(abs(full), axis=1)
        maxima.append(maximum_rows)
        lows.append(np.max(abs(low), axis=1)); highs.append(np.max(abs(high), axis=1))
        ii = np.argmax(abs(full), axis=1)
        peak_xis.append(xi[ii])
        peak_us.append(np.take_along_axis(q['u'][:, :, None], ii[:, None, :], axis=1)[:, 0, :])
        s_samples.append(ss)
        endpoint_mean = .5*(full[0]+full[-1])
        gauss_mean = .5*(full[1]+full[-2])
        trap_max.append(np.max(abs(endpoint_mean), axis=0))
        gauss_max.append(np.max(abs(gauss_mean), axis=0))
        mean_difference.append(np.max(abs(gauss_mean-endpoint_mean), axis=0))
        oscillations.append(np.max(abs(full-endpoint_mean[None, :, :]), axis=(0, 1)))
        for collection, values in ((trap_low_max, endpoint_mean), (gauss_low_max, gauss_mean)):
            collection.append(np.array([maximum(project(values[:, j][None, :], key)) for j, key in enumerate(COMPONENTS)]))
        for collection, values in ((trap_high_max, endpoint_mean), (gauss_high_max, gauss_mean)):
            collection.append(np.array([maximum(values[:, j][None, :]-project(values[:, j][None, :], key)) for j, key in enumerate(COMPONENTS)]))
        cn = np.asarray(residual['connection_operator_norm'])
        connection_max.append(np.max(cn, axis=1))
        n_extrema.append([float(np.min(q['n'])), float(np.max(q['n']))])
        r = np.hypot(q['n']-q['l'], 2*q['m'])
        curvature = .5*np.maximum(abs(q['n']+q['l']+r), abs(q['n']+q['l']-r))
        formal_curvature.append(float(np.max(curvature)))
        for k, key in enumerate(COMPONENTS):
            j, angular = np.unravel_index(np.argmax(abs(full[:, :, k])), full.shape[:2])
            magnitude = float(abs(full[j, angular, k]))
            if magnitude > peaks[key]['maximum']:
                peaks[key] = dict(maximum=magnitude, signed_value=float(full[j, angular, k]),
                    cell=cell, endpoints=[float(left), float(right)], fraction=float(fractions[j]),
                    s=float(ss[j]), xi=float(xi[angular]), material_u=float(q['u'][j, angular]),
                    n_m_l=[float(q[z][j, angular]) for z in ('n', 'm', 'l')],
                    a=float(q['a'][j, angular]), a_s=float(q['a_s'][j, angular]),
                    a_ss=float(q['a_ss'][j, angular]),
                    retained_at_same_point=float(low[j, angular, k]),
                    omitted_at_same_point=float(high[j, angular, k]),
                    retained_max_at_same_radial_point=float(np.max(abs(low[j, :, k]))),
                    omitted_max_at_same_radial_point=float(np.max(abs(high[j, :, k]))))
        j, angular = np.unravel_index(np.argmax(cn), cn.shape)
        if float(cn[j, angular]) > global_connection['maximum']:
            global_connection = dict(maximum=float(cn[j, angular]), cell=cell,
                fraction=float(fractions[j]), s=float(ss[j]), xi=float(xi[angular]),
                material_u=float(q['u'][j, angular]),
                vector=np.asarray(residual['connection_vector'][j, angular]).tolist())
        row = dict(cell=cell, right_s=float(right), maxima={key: peaks[key]['maximum'] for key in COMPONENTS},
                   seconds=time.monotonic()-started)
        with progress_path.open('a') as stream:
            stream.write(json.dumps(row)+'\n')
        if cell == 0 or cell == len(reader.nodes)-2 or time.monotonic()-last_print >= 20:
            print(json.dumps(row), flush=True); last_print = time.monotonic()
    arrays = dict(cell_endpoints=np.column_stack((reader.nodes[:-1], reader.nodes[1:])),
        sample_fractions=fractions, physical_s=np.asarray(s_samples),
        residual_absolute_maxima=np.asarray(maxima), retained_maxima=np.asarray(lows),
        omitted_maxima=np.asarray(highs), worst_xi=np.asarray(peak_xis), worst_material_u=np.asarray(peak_us),
        trapezoid_mean_absolute_maxima=np.asarray(trap_max), gauss2_mean_absolute_maxima=np.asarray(gauss_max),
        gauss2_minus_trapezoid_absolute_maxima=np.asarray(mean_difference),
        deviation_from_trapezoid_mean_absolute_maxima=np.asarray(oscillations),
        trapezoid_retained_maxima=np.asarray(trap_low_max), trapezoid_omitted_maxima=np.asarray(trap_high_max),
        gauss2_retained_maxima=np.asarray(gauss_low_max), gauss2_omitted_maxima=np.asarray(gauss_high_max),
        connection_norm_maxima=np.asarray(connection_max), sampled_n_extrema=np.asarray(n_extrema),
        sampled_formal_curvature_maximum=np.asarray(formal_curvature))
    packet = save_npz(Path(str(stem)+'-cell-statistics.npz'), **arrays)

    def worst_cell(array, component):
        j = int(np.argmax(array[:, component]))
        return dict(maximum=float(array[j, component]), cell=j,
                    endpoints=arrays['cell_endpoints'][j].tolist())

    mean_summary = {key: dict(trapezoid=worst_cell(arrays['trapezoid_mean_absolute_maxima'], k),
        gauss2=worst_cell(arrays['gauss2_mean_absolute_maxima'], k),
        gauss2_minus_trapezoid=worst_cell(arrays['gauss2_minus_trapezoid_absolute_maxima'], k),
        interior_deviation_from_trapezoid=worst_cell(arrays['deviation_from_trapezoid_mean_absolute_maxima'], k))
        for k, key in enumerate(COMPONENTS)}
    report = dict(schema='fd2d-actual-P1-cell-full-residual-finite-screen-v1', source=identity(__file__),
        sources=sources, input_field=field_id, candidate=identity(args.candidate),
        actual_definition=identity(definition_path), statistics=packet, components=list(COMPONENTS),
        node_count=len(reader.nodes), angular_points=args.angles, maximum_retained_frequency=2*reader.K,
        angular_sampling='xi=2*pi*j/N; values interpreted through actual U(s,xi)',
        radial_sampling=dict(fractions=fractions.tolist(), endpoints='One-sided slopes of the same P1 cell'),
        maxima=peaks, connection_norm_peak=global_connection, quadrature_diagnostics=mean_summary,
        sampled_n_minimum=float(np.min(arrays['sampled_n_extrema'][:, 0])),
        sampled_formal_curvature_maximum=float(np.max(arrays['sampled_formal_curvature_maximum'])),
        progress=identity(progress_path), seconds=time.monotonic()-started,
        actual_field_bytes_unchanged=identity(args.field)['sha256'] == field_id['sha256'],
        sources_unchanged=all(identity(row['path'])['sha256'] == row['sha256'] for row in sources),
        continuous_certificate=False, body_integration_run=False, nonlinear_solve_performed=False,
        quadrature_is_fixed_xi_not_fixed_material_u=True,
        scope='Full finite samples of the saved P1 field. Low/high refers to the same retained parity basis. Neither sample maxima nor Gauss2/trapezoid differences are continuous error bounds.')
    rp = Path(str(stem)+'-report.json')
    rp.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(rp), maxima=peaks, means=mean_summary,
        seconds=report['seconds'], continuous_certificate=False)), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
