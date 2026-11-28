#!/usr/bin/env python3
"""Evaluate time interpolation of one genuine complete fixed-g QR field.

The field, complete target metric, all spatial charts, final physical H,
finite mean, phase interval, cylinder and marker are fixed for every level.
At each material point the time approximant is the same linear cubic-spline
operator applied to X and all six spatial two-jets. Thus the reported first
derivatives are derivatives of the interpolated surface, not derivatives of
an unrelated position interpolation. No BVP or Fourier mode is truncated.

This is an explicit finite diagnostic, not a continuous spatial/time bound,
an embedding proof or proof of a C2 limit. The exact finite field's sampled
metric floor is reported separately. Increasing only the time sample count
is not called an approximation refinement. Genuine coarse time interpolants
are compared on one common finer time grid with fixed material stations.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.interpolate import CubicSpline

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import material_circle_phase_contract as phase_api
import qr_fixed_actual_cartesian_prefix as reader
from qr_fixed_actual_closed_map import load_closed_map
from qr_fixed_actual_prefix_continuous import write


def rotate(v, angle):
    v = np.asarray(v, dtype=float)
    c, s = np.cos(angle), np.sin(angle)
    return np.stack((c*v[..., 0]-s*v[..., 1],
                     s*v[..., 0]+c*v[..., 1], v[..., 2]), axis=-1)


def circle(theta):
    return np.asarray([np.cos(theta), np.sin(theta), 0.])


def stations(model, angular, cut_width):
    """Fixed finite chart stations; no spatial supremum is asserted."""
    ell, end = model.cylinder_half_length, model.end
    prefix = sorted(set([0., ell/2, ell, ell+model.prefix.center_width/2,
        ell+model.prefix.center_width, ell+end/2,
        ell+end-cut_width, ell+end-cut_width/2, ell+end]))
    tail = sorted(set([model.a, float(model.cap.inner), float(model.cap.deep),
        (float(model.cap.inner)+float(model.cap.deep))/2,
        (float(model.cap.deep)+model.Rcut)/2, model.Rcut]))
    theta = 2*np.pi*np.arange(angular)/angular
    for side in (-1, 1):
        for s in prefix:
            for angle in theta:
                yield dict(chart='prefix', s=side*s, theta=float(angle), side=side)
        for radius in tail:
            for angle in theta:
                yield dict(chart='tail', R=radius, theta=float(angle), side=side)
        # Cartesian pole charts remain regular, including the actual pole.
        yield dict(chart='disk', x=0., y=0., side=side)
        for radius in (model.marker_radius/2, model.marker_radius, 3*model.a/4):
            for angle in theta:
                yield dict(chart='disk', x=float(radius*np.cos(angle)),
                    y=float(radius*np.sin(angle)), side=side)


def target_metric(model, station):
    chart = station['chart']
    if chart == 'prefix':
        u = max(0., abs(station['s'])-model.cylinder_half_length)
        a = float(model.prefix.flow.profile(np.asarray([u]))[0][0])
        metric = np.diag([1., a*a])
    elif chart == 'tail':
        radius = station['R']
        w = float(model.background.sample(radius)['w']) if radius > model.a else 0.
        metric = np.diag([1.+w*w, radius*radius])
    else:
        _, grad, _ = model.marker(station['x'], station['y'])
        grad = np.asarray(grad, float)
        metric = np.eye(2)+np.outer(grad, grad)
    if not np.all(np.isfinite(metric)) or np.min(np.linalg.eigvalsh(metric)) <= 0:
        raise ArithmeticError('The fixed physical target metric must be positive definite')
    return metric


def jets(model, station, phase, held):
    chart, side = station['chart'], station['side']
    if chart == 'prefix':
        value = model.prefix_jets(station['s'], station['theta'], phase)
    elif chart == 'tail':
        value = model.tail_jets(station['R'], station['theta'], side, phase)
    else:
        X, J, H = model.disk_jets(station['x'], station['y'], side)
        value = (X, J[:, 0], H[:, 0, 0], J[:, 1], H[:, 1, 1], H[:, 0, 1])
    value = np.asarray(value, float)
    center, k = held
    value = rotate(value, -(1.-k)*phase)
    value[0] += center-rotate(center, k*phase)
    if value.shape != (6, 3) or not np.all(np.isfinite(value)):
        raise ArithmeticError('A complete original chart two-jet is nonfinite')
    return value


def metric_errors(values, metric):
    inverse_root = np.linalg.inv(np.linalg.cholesky(metric).T)
    jacobian = np.stack((values[:, 1, :], values[:, 3, :]), axis=-1)
    normalized = jacobian@inverse_root
    defect = np.swapaxes(normalized, -1, -2)@normalized-np.eye(2)
    return np.max(np.abs(np.linalg.eigvalsh(defect)), axis=-1)


def update_maximum(row, key, value, station, time_index, denominator):
    if key not in row or value > row[key]:
        row[key] = float(value)
        row[key+'_at'] = dict(station=station,
            t_exact=str(Q(int(time_index), denominator)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run', 'geometry-bundle', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--phase-end', type=Q, required=True)
    parser.add_argument('--held-width', type=Q, default=Q(27, 50))
    parser.add_argument('--cylinder-half-length', type=float, choices=(.0025, .005), default=.0025)
    parser.add_argument('--cut-width', type=float, default=.04)
    parser.add_argument('--intervals', type=int, nargs='+', default=[8, 16, 32, 64])
    parser.add_argument('--angular-stations', type=int, default=7)
    parser.add_argument('--common-time-sampling-factor', type=int, default=4)
    args = parser.parse_args()
    levels = args.intervals
    if (len(levels) < 2 or levels[0] < 4 or levels != sorted(set(levels))
            or any(b % a for a, b in zip(levels[:-1], levels[1:]))
            or args.angular_stations < 3 or args.common_time_sampling_factor < 2):
        raise ValueError('Use nested increasing time grids and one strictly finer common diagnostic grid')
    out = args.outdir.resolve()
    if out == reader.REPO or reader.REPO in out.parents:
        raise ValueError('Complete-field diagnostic outputs belong outside the source repository')
    record, physical, view, provenance = reader.accepted_fixed(args.source_run)
    del physical
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    model = load_closed_map(args.source_run, args.geometry_bundle,
        out/'verified-node-index.json', cylinder_half_length=args.cylinder_half_length,
        cut_width=args.cut_width, canonical_r67_marker=True)
    report = dict(status='evaluating_actual_fixed_field_time_interpolation',
        source=reader.ref(__file__), source_run=reader.ref(args.source_run),
        geometry_bundle=reader.ref(args.geometry_bundle),
        source_kind=reader.SOURCE_KIND, source_model_kind=reader.model.KIND,
        actual_fixed_provenance=provenance, complete_map_definition=model.definition_provenance,
        fixed_problem=record['fixed_problem'], frozen_profile=record['frozen_profile'],
        source_mean_nodes=record['mean_nodes'], source_mean_gauss_order=6,
        final_physical_height=view['height_reference'], final_height_packet=view['packet'],
        interpolation='CubicSpline with not-a-knot boundary conditions on the same [0,1]',
        interpolated_spatial_jet_order=['X', 'X1', 'X11', 'X2', 'X22', 'X12'],
        spatial_jet_interpolation_commutes_with_spatial_differentiation=True,
        original_all_saved_modes_evaluated=True, finite_field_or_target_changed_between_levels=False,
        sample_maximum_is_not_continuous_bound=True,
        global_metric_certified=False, reach_certified=False, embedding_certified=False,
        C2_limit_proved=False, readme_completion_claimed=False,
        levels=[dict(time_intervals=n) for n in levels], exact_field_sampled_floor={},
        stations_completed=0, BVP_or_native_solve_invoked=False)
    try:
        report['phase_contract'] = phase_api.describe(model, args.phase_end, args.held_width)
        frame = phase_api.held_frame(model, args.phase_end, args.held_width, circle)
        report['held_frame_evaluation_only'] = dict(center=frame[0].tolist(),
            exact_binary_k=str(Q.from_float(frame[1])))
        count = args.common_time_sampling_factor*levels[-1]
        times = np.arange(count+1, dtype=float)/count
        phases = float(args.phase_end)*times
        material_stations = list(stations(model, args.angular_stations, args.cut_width))
        report.update(common_time_denominator=count,
            material_station_count=len(material_stations), material_stations=material_stations,
            time_grid_definition='t_j=j/common_time_denominator, j=0,...,denominator')
        for index, station in enumerate(material_stations):
            metric = target_metric(model, station)
            actual = np.stack([jets(model, station, float(phase), frame) for phase in phases])
            floor = metric_errors(actual, metric)
            peak = int(np.argmax(floor))
            update_maximum(report['exact_field_sampled_floor'], 'relative_metric_error',
                floor[peak], station, peak, count)
            previous = None
            for row in report['levels']:
                step = count//row['time_intervals']
                indices = np.arange(0, count+1, step)
                approximant = CubicSpline(times[indices], actual[indices],
                    axis=0, bc_type='not-a-knot')(times)
                defects = metric_errors(approximant, metric)
                peak = int(np.argmax(defects))
                update_maximum(row, 'relative_metric_error', defects[peak], station, peak, count)
                for order, components in ((0, [0]), (1, [1, 3]), (2, [2, 4, 5])):
                    difference = np.max(np.linalg.norm(
                        approximant[:, components]-actual[:, components], axis=-1), axis=-1)
                    peak = int(np.argmax(difference))
                    update_maximum(row, 'jet_order_'+str(order)+'_difference_from_exact_field',
                        difference[peak], station, peak, count)
                if previous is not None:
                    difference = np.max(np.linalg.norm(approximant-previous, axis=-1), axis=-1)
                    peak = int(np.argmax(difference))
                    update_maximum(row, 'complete_two_jet_difference_from_previous_level',
                        difference[peak], station, peak, count)
                previous = approximant
            report.update(stations_completed=index+1, seconds=time.monotonic()-started)
            write(out/'summary.json', report)
            if (index+1) % 8 == 0:
                print(json.dumps(dict(stations=index+1, total=len(material_stations),
                    seconds=report['seconds'])), flush=True)
        errors = [row['relative_metric_error'] for row in report['levels']]
        report.update(status='actual_fixed_field_time_interpolation_diagnostic_returned',
            sampled_metric_errors_monotone_nonincreasing=all(b <= a for a, b in zip(errors[:-1], errors[1:])),
            node_check=reader.ref(out/'verified-node-index.json'), seconds=time.monotonic()-started,
            maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            source_hashes={**reader.reader_sources(),
                **provenance['actual_geometry_provider_sources'],
                **{str(path.resolve()):reader.sha(path) for path in
                    (Path(__file__), HERE/'qr_fixed_actual_closed_map.py',
                     HERE/'qr_fixed_actual_prefix_continuous.py', Path(phase_api.__file__))}})
        write(out/'summary.json', report)
        print(json.dumps(dict(status=report['status'], summary=reader.ref(out/'summary.json'),
            sampled_metric_errors=errors)), flush=True)
    finally:
        model.close()


if __name__ == '__main__':
    main()
