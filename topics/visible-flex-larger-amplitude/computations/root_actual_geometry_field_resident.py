#!/usr/bin/env python3
"""Save the unchanged complete warm geometry field with bounded resident storage.

This wraps the existing explicit unsolved actual-J warm inspection. It does
not run its residual quadrature, a tail worker, a Newton solve or a new audit.
Every raw mode and the complete production mean-height integral are retained
in the same physical-s C2 cubic used by the existing warm geometry screen.
The saved signed principal curvatures and twice-radius are samples for local
design comparisons, not a physical quintic, closed surface or reach bound.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
import os
import mmap
import tempfile
import resource
from pathlib import Path
import sys

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--geometry-grid', type=Path, required=True)
    parser.add_argument('--geometry-array', type=Path, required=True)
    parser.add_argument('--resident-rss-guard-mib', type=float, default=144.)
    options, remaining = parser.parse_known_args()
    if '--inspect-warm-output' not in remaining:
        raise ValueError('This entry only supports the explicit unsolved warm inspection')
    output = options.geometry_array
    if output.exists() or output.suffix != '.json':
        raise ValueError('Use a fresh complete geometry chunk manifest')
    import inspect
    import textwrap
    import types
    from types import SimpleNamespace
    import numpy as np
    from scipy.interpolate import CubicSpline
    import strong_actual_three_control_bvp as entry
    import strong_actual_warm_screen as warm
    grid = json.loads(options.geometry_grid.read_text())
    t = np.asarray(grid['numerical_t'], dtype=float)
    angular = int(grid['angular'])
    if (t.ndim != 1 or len(t) < 2 or not np.isfinite(t).all() or
            t[0] != 0. or t[-1] != 1. or not np.all(np.diff(t) > 0) or
            angular < 96 or angular % 4):
        raise ValueError('Use an ordered full [0,1] numerical grid and angular count divisible by four')
    completed = False
    original_inspection = warm.inspect_warm
    def release_values(values):
        values.flush()
        if hasattr(values._mmap, 'madvise'):
            values._mmap.madvise(mmap.MADV_DONTNEED)
    def observed_rss_guard():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > options.resident_rss_guard_mib * 1024:
            raise MemoryError('Observed geometry peak RSS exceeded configured diagnostic guard: '+str(peak)+' KiB')

    def field(obj, x, y, p, baseline_H, **unused):
        nonlocal completed
        obj.select(p)
        flow = obj.flow()
        physical_nodes, unused_ds = obj.chart(x, 0.)
        physical_grid, unused_ds = obj.chart(t, 0.)
        if not np.all(np.diff(physical_nodes) > 0) or not np.all(np.diff(physical_grid) > 0):
            raise ValueError('The physical chart lost orientation')
        cubic = CubicSpline(physical_nodes, y, axis=1)
        sol = SimpleNamespace(x=physical_nodes, y=y, p=p, sol=cubic)
        text = textwrap.dedent(inspect.getsource(flow.height_integral.__func__))
        if text.count('128') != 3:
            raise ValueError('The original independent mean-height batching sites changed')
        transformed = text.replace('128', '8')
        namespace = {'np': np}
        exec(compile(transformed, '<bounded-common-grid-mean>', 'exec'), namespace)
        height = types.MethodType(namespace['height_integral'], flow)(sol, physical_grid, angular, 6)
        B, B1, B2 = flow.basis(angular)
        resident_backing = tempfile.TemporaryFile(prefix='root_geometry_resident_')
        values = np.memmap(resident_backing, mode='w+', shape=(len(t), angular, 3), dtype=np.float64)
        running_kappa = -np.inf
        running_radius = -np.inf
        observed_rss_guard()
        minimum_area = np.inf
        minimum_margin = np.inf
        for first in range(0, len(t), 8):
            sl = slice(first, first+8)
            s = physical_grid[sl]
            Y, Ys, Yss = cubic(s), cubic(s, 1), cubic(s, 2)
            frame, mixed, dW = flow.velocity_s(s, Y, Ys, B1, B2)
            geo = frame['geo']
            Fs = geo['s1'] + obj.q*flow.values(Ys, B)
            Fs[:, :, 2] += np.mean(frame['V'][:, :, 2], axis=1)[:, None]
            Fss = geo['s2'] + obj.q*flow.values(Yss, B)
            Fss[:, :, 2] += np.mean(dW[:, :, 2], axis=1)[:, None]
            # The pinned source velocity_s returns geo.sp+q*Ys.B1 here,
            # the derivative of this actual cubic, not a PDE replacement.
            if not np.array_equal(mixed, geo['sp']+obj.q*flow.values(Ys, B1)):
                raise ValueError('The actual mixed derivative interface changed')
            Ft, Ftt = frame['d'], frame['dd']
            cross = np.cross(Fs, Ft)
            area = np.linalg.norm(cross, axis=2)
            if not np.isfinite(area).all() or float(area.min()) <= 0:
                raise ValueError('Degenerate actual cubic tangent plane')
            normal = cross/area[:, :, None]
            E = np.sum(Fs*Fs, axis=2)
            F = np.sum(Fs*Ft, axis=2)
            G = np.sum(Ft*Ft, axis=2)
            determinant = E*G-F*F
            if float(determinant.min()) <= 0:
                raise ValueError('The actual first fundamental form lost positivity')
            e = np.sum(normal*Fss, axis=2)
            f = np.sum(normal*mixed, axis=2)
            g = np.sum(normal*Ftt, axis=2)
            trace = (e*G-2*f*F+g*E)/determinant
            product = (e*g-f*f)/determinant
            discriminant = trace*trace-4*product
            roundoff = 128*np.finfo(float).eps*(1+trace*trace+4*abs(product))
            if np.any(discriminant < -roundoff):
                raise ValueError('Principal-curvature discriminant exceeded the rounding allowance')
            root = np.sqrt(np.maximum(discriminant, 0.))
            values[sl, :, 0] = (trace-root)/2
            values[sl, :, 1] = (trace+root)/2
            points = geo['pos']+obj.q*flow.values(Y, B)
            points[:, :, 2] += height[sl, None]
            values[sl, :, 2] = 2*np.linalg.norm(points, axis=2)
            minimum_area = min(minimum_area, float(area.min()))
            minimum_margin = min(minimum_margin, float(frame['margin'].min()))
            if not np.isfinite(values[sl]).all():
                raise ValueError('Nonfinite geometry block')
            running_kappa = max(running_kappa, float(np.max(abs(values[sl, :, :2]))))
            running_radius = max(running_radius, float(np.max(values[sl, :, 2])))
            if first % 64 == 0:
                release_values(values)
                observed_rss_guard()
        release_values(values)
        if minimum_margin <= 0:
            raise ValueError('Nonfinite geometry or failed Frenet domain')
        from root_geometry_array_io_resident import write_chunks
        storage = write_chunks(output, values, release=release_values, observe=observed_rss_guard)
        witness_samples = [dict(radial_index=int(item['radial_index']),
            angular_index=int(item['angular_index']),
            actual_s=float(physical_grid[item['radial_index']]),
            numerical_t=float(t[item['radial_index']]),
            eta=float(item['angular_index']*2*np.pi/angular),
            components=values[item['radial_index'], item['angular_index']].tolist())
            for item in grid.get('known_reference_witnesses', [])]
        obj.initial(p)
        observed_rss_guard()
        completed = True
        return dict(scope=__doc__, finite_domain_passed=True,
            full_collocation=dict(performed=False, scope='Only geometry fields requested by this entry'),
            geometry_fields=dict(file=str(output), sha256=sha(output), bytes=sum(item['bytes'] for item in storage['chunks']),
                storage=storage, storage_source_sha256=sha(Path(__file__).with_name('root_geometry_array_io_resident.py')),
                shape=list(values.shape), components=['kappa_minus', 'kappa_plus', 'twice_radius'],
                grid_file=str(options.geometry_grid), grid_sha256=sha(options.geometry_grid),
                common_coordinates='Original computational t and material chart eta; physical s/theta vary with profile.',
                wrapper_sha256=sha(__file__), signed_normal='Fs cross F_eta',
                all_raw_nodes_and_modes_retained=True, complete_mean_height=True, known_reference_witness_samples=witness_samples,
                interpolation='C2 physical-s cubic through every complete warm raw state',
                rms_performed=False, true_new_H_tail_evaluated=False,
                kappa_abs_max_sample=running_kappa,
                twice_radius_max_sample=running_radius,
                minimum_tangent_area_sample=minimum_area, minimum_frenet_margin_sample=minimum_margin,
                actual_core=obj._core.coefficients.tolist(), physical_profile=dict(flow.cfg),
                mean_quadrature=dict(angular=angular, order=6, batch=8,
                    original_source_sha256=hashlib.sha256(text.encode()).hexdigest(),
                    bounded_source_sha256=hashlib.sha256(transformed.encode()).hexdigest())),
            complete_warm_H=obj.tail_height(y[:, -1]).tolist(),
            complete_H_change_max=float(np.max(abs(obj.tail_height(y[:, -1])-baseline_H))))

    previous_argv = sys.argv
    sys.argv = [sys.argv[0]] + remaining
    warm.inspect_warm = field
    try:
        entry.main()
    finally:
        warm.inspect_warm = original_inspection
        sys.argv = previous_argv
    if not completed or not output.exists():
        raise RuntimeError('The requested complete geometry field was not produced')


if __name__ == '__main__':
    main()
