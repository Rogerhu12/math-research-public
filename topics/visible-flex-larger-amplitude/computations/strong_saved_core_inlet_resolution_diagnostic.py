#!/usr/bin/env python3
"""Measure the exact accepted core's inlet projection in the unchanged chart.

Only the original PlanarSupportCore, GeneralCoreChart and cylindrical
basis/project/values routines are evaluated. No flow, ODE, BVP, tail worker,
or new solution is constructed. Higher-M rows project the same saved core;
they are not refinements of the accepted surface. All angular metrics are
finite FFT samples, not continuous enclosures.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def raw_y(path, record, sources):
    item = record['arrays']['y']
    flat = []
    count = 0
    for chunk in item['chunks']:
        source = path.parent / chunk['file']
        if Path(chunk['file']).name != chunk['file'] or chunk['first'] != count:
            raise ValueError('Invalid exact original raw chunk layout')
        if sha(source) != chunk['sha256']:
            raise ValueError('Original raw y chunk SHA differs')
        sources[str(source)] = chunk['sha256']
        a = np.load(io.BytesIO(gzip.decompress(source.read_bytes())), allow_pickle=False)
        if a.dtype != np.float64 or a.shape != (chunk['count'],):
            raise ValueError('Original raw y dtype or count differs')
        flat.append(a)
        count += len(a)
    return np.concatenate(flat).reshape(item['shape'])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--raw', type=Path, required=True)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--modes', type=int, nargs='+', default=[28, 32, 36, 40, 48, 64])
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('A fresh diagnostic path is required')
    saved, raw = read(a.checkpoint), read(a.raw)
    if (not saved.get('solver_success') or saved.get('audit_pending', True)
            or not raw.get('solver_success')
            or saved['raw_collocation_checkpoint']['sha256'] != sha(a.raw)):
        raise ValueError('Complete original accepted primary/raw identity required')
    if saved['angular_chart'] != 'general-support-core-blend-v1':
        raise ValueError('This diagnostic requires the original general core chart')
    for rk, sk in [('profile', 'frozen_profile'), ('gauge', 'gauge_amplitude'),
                   ('reference_coefficients', 'chart_reference_coefficients'),
                   ('reference_frequencies', 'chart_reference_frequencies')]:
        if raw['identity'][rk] != saved[sk]:
            raise ValueError('Original accepted identity differs: ' + rk)
    scripts = a.source_topic / 'repro/source-root/topics/large-amplitude-twist-flex/scripts'
    sys.path[:0] = [str(a.source_topic / 'notes'), str(scripts)]
    from fixed_metric_mode3_core import PlanarSupportCore
    from curve_stable_prefix_bvp import CylindricalPrefix
    charts = module('strong_saved_core_inlet_chart', HERE / 'geometric-general-core-chart.py')
    sources = {str(path): sha(path) for path in [Path(__file__), a.checkpoint, a.raw,
        HERE / 'geometric-general-core-chart.py', a.source_topic / 'notes/fixed_metric_mode3_core.py',
        scripts / 'curve_stable_prefix_bvp.py']}
    coef = np.asarray(saved['core']['coefficients'], dtype=np.float64)
    freq = np.asarray(saved['core']['frequencies'], dtype=np.int64)
    base = int(saved['core']['base_mode'])
    if not np.array_equal(freq, base * np.arange(1, len(coef) + 1)):
        raise ValueError('Complete physical support frequencies differ')
    core = PlanarSupportCore(coef[0], coef[1:], base)
    chart = charts.GeneralCoreChart(saved['chart_reference_coefficients'],
                                   saved['chart_reference_frequencies'], saved['meridian_length'])
    original_m = int(saved['modes'])
    original_n = max(2048, 128 * original_m)
    original_y = raw_y(a.raw, raw, sources)
    rows = []
    cases = [(original_m, original_n), (original_m, 2 * original_n)]
    cases += [(int(m), max(4096, 128 * int(m))) for m in a.modes if int(m) != original_m]
    for M, N in cases:
        if M < original_m or M > 128:
            raise ValueError('Only retained or increased projection order is allowed')
        obj = SimpleNamespace(M=M, n=3*M+1, iz=2*M+1, even=base*np.arange(1, M+1))
        B, B1, B2 = CylindricalPrefix.basis(obj, N)
        gi = chart.inlet_geometry(N)
        exact = core.evaluate(gi['theta'])
        state = CylindricalPrefix.project((exact['F']-gi['pos'])[None, :, :], B)[:, 0] / saved['gauge_amplitude']
        mapped = gi['pos'] + saved['gauge_amplitude'] * CylindricalPrefix.values(state[:, None], B)[0]
        first = gi['p1'] + saved['gauge_amplitude'] * CylindricalPrefix.values(state[:, None], B1)[0]
        second = gi['p2'] + saved['gauge_amplitude'] * CylindricalPrefix.values(state[:, None], B2)[0]
        true1 = exact['Ft'] * gi['rho'][:, None]
        true2 = exact['Ftt'] * gi['rho'][:, None]**2 + exact['Ft'] * gi['rhop'][:, None]
        error = np.sum(first*first, axis=1) / gi['rho']**2 - 1
        metric = float(np.sum(abs(np.fft.fft(error)/N)))
        row = dict(modes=M, angular=N, position=float(np.linalg.norm(mapped-exact['F'], axis=1).max()),
            first=float(np.linalg.norm(first-true1, axis=1).max()),
            second=float(np.linalg.norm(second-true2, axis=1).max()), metric_l1=metric,
            arc_inversion_residual=float(np.max(abs(exact['arc_residual']))),
            original_physical_core_and_chart_unchanged=True, is_new_bvp_solution=False)
        if M == original_m:
            row['original_raw_initial_state_difference_max'] = float(abs(state-original_y[:, 0]).max())
        if (M, N) == (original_m, original_n):
            row['stored_inlet_metrics'] = saved['summary']['inlet']
            row['stored_inlet_absolute_differences'] = {k: abs(row[k]-saved['summary']['inlet'][k])
                for k in ('position', 'first', 'second', 'metric_l1')}
            if max(row['stored_inlet_absolute_differences'].values()) > 3e-12:
                raise ValueError('Independent original inlet evaluation did not reproduce the saved diagnostics')
        rows.append(row)
        print(json.dumps(row), flush=True)
        del B, B1, B2
    output = dict(scope=__doc__, input=str(a.checkpoint), input_sha256=sha(a.checkpoint),
        raw=str(a.raw), raw_sha256=sha(a.raw), source_sha256=sources,
        full_physical_core_coefficients=coef.tolist(), frequencies=freq.tolist(),
        physical_profile=saved['frozen_profile'], material_reference_coefficients=chart.coefficients.tolist(),
        material_reference_frequencies=chart.frequencies.tolist(), gauge=saved['gauge_amplitude'],
        original_saved_metric_l1=saved['summary']['metric_l1'], original_saved_flow_defect=saved['summary']['flow_defect'],
        rows=rows, no_ode_or_nonlinear_solve=True, no_accepted_field_modified=True,
        limitations=['A higher-order inlet projection alone does not refine the surface or determine its solved core.',
                     'The original accepted M28 field retains its original inlet and physical metric errors.',
                     'No continuous bound, isometry, closure, held or reach certificate is produced.'])
    with a.out.open('x') as stream:
        json.dump(output, stream, indent=2)
        stream.write('\n')


if __name__ == '__main__':
    main()
