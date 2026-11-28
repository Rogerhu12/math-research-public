#!/usr/bin/env python3
"""Bisect genuine angular boxes without repeating their validated bounds.

Each new half-box is a subset of one actual old box. All its old box three-
jet enclosures are retained exactly; even point columns are retained exactly.
Only the new odd points are evaluated by the unchanged true-core oracle.
The mathematical prefix, its complete defining jets, target, mean and core
are unchanged. This is angular certificate refinement, not BVP refinement,
and produces no metric certificate by itself.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import json
from pathlib import Path
import time
import traceback

import mpmath as mp
import numpy as np

import cartesian_prefix_metric_tables as original
from cartesian_prefix_interval_geometry import SCRIPTS, load_actual_prefix, save, sha
from phase_angle_chart import PhaseAngleChart


def angular_axis(name):
    if '_basis_' in name or '_center_' in name:
        return 2
    if '_lift_' in name or '_trig_' in name:
        return 1
    raise ValueError('An unrecognized angular table cannot be inherited: '+name)


def same_bits(left, right):
    return (left.dtype == right.dtype and left.shape == right.shape
            and left.tobytes() == right.tobytes())


class RefinedRanges(original.MetricAngularRanges):
    def __init__(self, prefix, parent, arrays, progress):
        self.parent_record = parent
        self.parent_arrays = arrays
        super().__init__(prefix, 2*int(parent['angular_boxes_per_sector']), progress)

    def _build(self, progress):
        I, v, p = self.I, self.v, self.p
        old, N = self.parent_arrays, self.N
        parent_N = N//2
        if (np.any(np.asarray(p.pm) % 3 != 1) or np.any(np.asarray(p.hm) % 3 != 0)
                or p.flow.base_mode != 3 or not abs(p.E0) < 1):
            raise ValueError('The original exact threefold covariance is required')
        expected = {'psi_boxes', 'angular_width'}
        for tag in ('point', 'box'):
            for derivative in range(4):
                expected.update(f'{tag}_basis_{derivative}_{axis}' for axis in range(3))
                expected.update((f'{tag}_lift_{derivative}', f'{tag}_center_{derivative}'))
            expected.update(f'{tag}_trig_{axis}' for axis in range(2))
        if set(old) != expected or old['psi_boxes'].shape != (2, parent_N):
            raise ValueError('The complete original angular schema differs')
        for key, value in old.items():
            if key not in ('psi_boxes', 'angular_width'):
                if value.shape[angular_axis(key)] != parent_N:
                    raise ValueError('A parent table does not have every angular column')
            if not np.all(np.isfinite(value)):
                raise ValueError('A parent angular table is not finite')
        self.projection_data = self.projection_coefficients()
        width = I.raw((old['angular_width'][0], old['angular_width'][1]))/2
        arrays = {key: np.repeat(value, 2, axis=angular_axis(key))
                  for key, value in old.items() if key not in ('psi_boxes', 'angular_width')}
        arrays['angular_width'] = np.asarray(width.x)
        psi_boxes = []
        completed = np.zeros(parent_N, dtype=bool)
        for j in range(parent_N):
            # These are the true exact endpoints: the two half intervals
            # partition [2*pi*j/(3*parent_N),2*pi*(j+1)/(3*parent_N)].
            endpoints = [v.from_mp(2*mp.iv.pi*(2*j+h)/(3*N)) for h in range(3)]
            for h in range(2):
                left, right = endpoints[h], endpoints[h+1]
                box = I(float(left.x[0]), float(right.x[1]))
                if (float(box.x[0]) < float(old['psi_boxes'][0,j])
                        or float(box.x[1]) > float(old['psi_boxes'][1,j])):
                    raise ValueError('A rounded child enclosure escaped its actual parent box')
                psi_boxes.append(box)
            psi = endpoints[1]
            sine, _ = v.sincos(3*psi)
            theta = psi-I(p.E0)*sine/3
            bases, lift, center, trig = self.data(psi, theta, self.hull_core(theta))
            column = 2*j+1
            for derivative in range(4):
                for axis in range(3):
                    arrays[f'point_basis_{derivative}_{axis}'][:,:,column] = np.asarray(
                        bases[derivative][axis].x)
                arrays[f'point_lift_{derivative}'][:,column,:] = np.asarray(lift[derivative].x)
                arrays[f'point_center_{derivative}'][:,:,column,:] = np.asarray(center[derivative].x)
            for axis in range(2):
                arrays[f'point_trig_{axis}'][:,column] = np.asarray(trig[axis].x)
            completed[j] = True
            if (j+1) % 64 == 0:
                progress(dict(stage='new_odd_points_only', completed=j+1, total=parent_N,
                              parent_boxes_inherited=2*(j+1),
                              material_parts=self.total_material_parts))
        if not np.all(completed):
            raise AssertionError('Every new odd point needs its actual complete evaluation')
        arrays['psi_boxes'] = np.asarray(self.matrix(psi_boxes).x)
        unchanged = {}
        for key, parent_value in old.items():
            if key in ('psi_boxes', 'angular_width'):
                continue
            axis = angular_axis(key)
            even = np.take(arrays[key], np.arange(0, N, 2), axis=axis)
            if not same_bits(even, parent_value):
                raise AssertionError('An inherited even column changed: '+key)
            if key.startswith('box_'):
                odd = np.take(arrays[key], np.arange(1, N, 2), axis=axis)
                if not same_bits(odd, parent_value):
                    raise AssertionError('A parent complete-box bound changed: '+key)
            unchanged[key] = True
        if any(not np.all(np.isfinite(value)) for value in arrays.values()):
            raise ArithmeticError('The refined complete angular data is not finite')
        self.inheritance = dict(parent_angular_boxes=parent_N, refined_angular_boxes=N,
            new_true_core_point_evaluations=parent_N,
            old_true_core_point_evaluations_repeated=0,
            old_complete_box_evaluations_repeated=0,
            complete_parent_box_bounds_retained_for_both_halves=True,
            child_boxes_numerically_contained_in_parent_enclosures=True,
            every_inherited_even_column_bitwise=unchanged,
            every_new_odd_point_actually_evaluated=True,
            exact_interval_partition='For parent count P and refined count 2P, the two consecutive halves exactly partition [2*pi*j/(3*P),2*pi*(j+1)/(3*P)].',
            unchanged_Gram_interpolation_rule='Every new interval uses its actual endpoint enclosures and the inherited true whole-parent second-derivative bound; its width is exactly half the parent width.')
        self.arrays = arrays


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-tables', type=Path, required=True)
    ap.add_argument('--outdir', type=Path, required=True)
    args = ap.parse_args()
    out, parent_path = args.outdir.resolve(), args.parent_tables.resolve()
    repo = SCRIPTS.parents[2]
    if out == repo or repo in out.parents:
        raise ValueError('All reproducible interval arrays stay outside Git')
    parent = json.loads(parent_path.read_text())
    if (parent.get('status') != 'complete_angular_three_jet_interval_tables'
            or parent.get('right_sector_endpoint_gram_equals_left_exactly') is not True
            or parent.get('angular_sector') != '[0,2*pi/3]'
            or int(parent['angular_boxes_per_sector']) < 32):
        raise ValueError('An actual complete threefold angular table is required')
    for filename, expected in parent['source_hashes'].items():
        if sha(filename) != expected:
            raise ValueError('A bound parent construction source changed: '+filename)
    for key in ('defining_jets', 'angular_tables'):
        if sha(parent[key]['path']) != parent[key]['sha256']:
            raise ValueError('Actual parent data changed: '+key)
    source_run = Path(parent['source_run'])
    if sha(source_run) != parent['source_run_sha256']:
        raise ValueError('The actual original mathematical input changed')
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    report = dict(status='loading_actual_parent_angular_refinement', scope=__doc__,
        metric_certified=False, whole_surface=False,
        parent_tables=dict(path=str(parent_path), sha256=sha(parent_path)))

    def progress(value):
        report.update(progress=value, seconds=time.monotonic()-started)
        save(out/'summary.json', report)
        print(json.dumps({**value, 'seconds': report['seconds']}), flush=True)

    save(out/'summary.json', report)
    try:
        actual, prefix = load_actual_prefix(source_run)
        if prefix.end_lift is not None:
            raise ValueError('An actual cut repair needs its separate complete contract')
        chart = PhaseAngleChart(prefix)
        current = dict(knots=prefix.rep.x, jets=prefix.rep.jets,
            lift_jets=prefix.core_lift_radial.jets, chart_jets=chart.rep.jets,
            planar_modes=prefix.pm, height_modes=prefix.hm,
            source_initial=prefix.source_initial, E0=np.asarray(prefix.E0),
            Epp=np.asarray(prefix.Epp), q=np.asarray(prefix.q),
            center_width=np.asarray(prefix.center_width))
        with np.load(parent['defining_jets']['path'], allow_pickle=False) as original_jets:
            if set(original_jets.files) != set(current):
                raise ValueError('The complete defining array schema changed')
            for key, value in current.items():
                if not same_bits(np.asarray(value), original_jets[key]):
                    raise ValueError('The actual mathematical field changed: '+key)
        if (actual['physical_sha256'] != parent['physical_sha256']
                or prefix.mean_nodes != parent['mean_nodes']
                or prefix.M != parent['modes']):
            raise ValueError('The actual complete finite field identity differs')
        with np.load(parent['angular_tables']['path'], allow_pickle=False) as data:
            arrays = {key:data[key].copy() for key in data.files}
        report.update(source_run=str(source_run.resolve()), source_run_sha256=sha(source_run),
            modes=prefix.M, physical_sha256=actual['physical_sha256'],
            homotopy=actual['core_settings']['homotopy'], mean_nodes=prefix.mean_nodes,
            radial_spans=len(prefix.rep.x)-1, chart=parent['chart'],
            defining_jets=parent['defining_jets'],
            all_eleven_actual_defining_arrays_bitwise_equal=True,
            different_field_numeric_bounds_reused=False)
        progress(dict(stage='same_actual_complete_map_verified'))
        refined = RefinedRanges(prefix, parent, arrays, progress)
        table = out/'continuous-angular-three-jets.npz'
        np.savez(table, **refined.arrays)
        sources = dict(parent['source_hashes'])
        sources.update({str(Path(__file__).resolve()):sha(__file__),
                        str(Path(original.__file__).resolve()):sha(original.__file__)})
        report.update(status='complete_angular_three_jet_interval_tables',
            angular_sector=parent['angular_sector'], angular_boxes_per_sector=refined.N,
            full_circle_box_equivalent=3*refined.N,
            exact_threefold_covariance=parent['exact_threefold_covariance'],
            right_sector_endpoint_gram_equals_left_exactly=True,
            angular_tables=dict(path=str(table), sha256=sha(table)),
            oracle=refined.oracle_metadata, maximum_material_parts=refined.maximum_material_parts,
            inheritance=refined.inheritance, source_hashes=sources,
            seconds=time.monotonic()-started)
        save(out/'summary.json', report)
        print(json.dumps({key:report[key] for key in
            ('status','angular_boxes_per_sector','seconds')}), flush=True)
    except Exception as error:
        (out/'exception.txt').write_text(traceback.format_exc())
        report.update(status='angular_refinement_execution_failed', error=repr(error),
                      seconds=time.monotonic()-started)
        save(out/'summary.json', report)
        raise


if __name__ == '__main__':
    main()
