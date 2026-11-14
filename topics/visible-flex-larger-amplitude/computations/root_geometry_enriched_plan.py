#!/usr/bin/env python3
"""Prepare a common geometry grid retaining original knots and known peaks.

The preceding coarse field remains unchanged.  This only prepares commands;
all cases retain the original complete raw cubic, all modes, and full mean.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np
from root_neck_chart import NeckChart
from strong_actual_fixed_control_response import raw_flat


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--original-plan', type=Path, required=True)
    ap.add_argument('--known-geometry', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    original = json.loads(args.original_plan.read_text())
    for name, expected in original['source_and_input_sha256'].items():
        if sha(name) != expected:
            raise ValueError('Original preparation changed: '+name)
    first = original['candidates'][0]['command']
    actual_path = Path(first[first.index('--actual-reference')+1])
    raw_path = Path(first[first.index('--actual-reference-raw')+1])
    with gzip.open(actual_path, 'rt') as stream:
        actual = json.load(stream)
    with gzip.open(raw_path, 'rt') as stream:
        raw = json.load(stream)
    hashes = {}
    x = np.asarray(raw_flat(raw_path, raw, 'x', hashes)).reshape(raw['arrays']['x']['shape'])
    chart_record = actual['numerical_meridian_chart']
    if chart_record['kind'] != 'C2-all-physical-knots-v1':
        raise ValueError('The saved physical chart interface changed')
    chart = NeckChart(chart_record['reference_t'], chart_record['physical_s'])
    known = json.loads(args.known_geometry.read_text())
    geometry = known['warm_physical_cubic_geometry']
    if (not known.get('finished') or not known.get('finite_domain_passed')
            or known.get('nonlinear_solution') or known.get('worker_start_attempts')
            or known['actual_core'] != actual['core']['coefficients']):
        raise ValueError('The old curvature witness is not from this complete reference')
    witness = geometry['curvature_witness']
    physical = np.unique(np.r_[np.linspace(chart.s[0], chart.s[-1], 241),
        *[np.linspace(a, b, 33) for a, b in zip(chart.s[:-1], chart.s[1:])], witness['s']])
    mapped = chart.inverse(physical)
    roundtrip = float(np.max(abs(chart.evaluate(mapped)[0]-physical)))
    if roundtrip > 1e-12:
        raise ValueError('Saved chart inversion did not retain the physical anchors')
    grid = np.unique(np.r_[x, mapped, np.asarray(chart_record['reference_t']), np.linspace(0, 1, 257)])
    if grid[0] != 0. or grid[-1] != 1. or not np.all(np.diff(grid) > 0):
        raise ValueError('The complete common grid changed orientation or endpoints')
    angular = 384
    index = int(round(witness['psi']*angular/(2*np.pi))) % angular
    if abs(index*2*np.pi/angular-witness['psi']) > 1e-13:
        raise ValueError('The new angular grid would omit the known witness')
    tw = float(chart.inverse(np.asarray([witness['s']]))[0])
    wi = int(np.argmin(abs(grid-tw)))
    if abs(chart.evaluate(grid[wi])[0]-witness['s']) > 1e-12:
        raise ValueError('The common radial grid would omit the known witness')
    prefix = args.out_prefix
    grid_path = prefix.with_name(prefix.name+'-grid.json')
    plan_path = prefix.with_name(prefix.name+'-plan.json')
    if grid_path.exists() or plan_path.exists():
        raise FileExistsError('Use a fresh enriched plan prefix')
    grid_path.write_text(json.dumps(dict(numerical_t=grid.tolist(), angular=angular,
        grid_only=True, all_original_raw_nodes_used_in_cubic=True,
        all_original_raw_nodes_evaluated=True, raw_sha256=sha(raw_path),
        original_raw_nodes=len(x), saved_physical_knots=len(chart.s),
        mapped_physical_anchors=len(physical), chart_roundtrip_max=roundtrip,
        rule='Every original raw knot, uniform257 in t, uniform241 in physical s, 33 per physical knot interval, and old curvature witness.',
        known_reference_witnesses=[dict(radial_index=wi, angular_index=index,
            reference_s=witness['s'], eta=witness['psi'], material_theta=witness['material_theta'],
            reference_max_abs_curvature=geometry['kappa_sample'], source=str(args.known_geometry))]),
        indent=2)+'\n')
    wrapper = Path(__file__).with_name('root_actual_geometry_field_chunks.py')
    planned = []
    for old in original['candidates']:
        row = dict(old)
        name = old['name']
        case = prefix.with_name(prefix.name+'-'+name)
        row.update(report=str(case.with_name(case.name+'-screen.json')),
                   field=str(case.with_name(case.name+'-field.json')),
                   resource=str(case.with_name(case.name+'-resource.json')),
                   log=str(case.with_name(case.name+'-log.txt')))
        command = old['command'].copy()
        split = command.index('--')
        command[0] = sys.executable
        command[split+1] = sys.executable
        command[split+2] = str(wrapper)
        for flag, value in [('--out', row['resource']), ('--out-prefix', str(case)),
                ('--inspect-warm-output', row['report']), ('--geometry-grid', str(grid_path)),
                ('--geometry-array', row['field'])]:
            command[command.index(flag)+1] = value
        row['command'] = command
        planned.append(row)
    inputs = dict(original['source_and_input_sha256'])
    for path in (Path(__file__), wrapper, Path(__file__).with_name('root_geometry_array_io.py'),
                 Path(__file__).with_name('root_neck_chart.py'), actual_path, raw_path,
                 args.original_plan, args.known_geometry, grid_path):
        inputs[str(path)] = sha(path)
    inputs.update(hashes)
    plan_path.write_text(json.dumps(dict(scope=__doc__, executed=False,
        nonlinear_solution=False, new_tail_evaluation=False, grid=str(grid_path),
        geometry_wrapper=str(wrapper), source_and_input_sha256=inputs,
        baseline_core=original['baseline_core'], directions=original['directions'],
        candidates=planned, limitations=original['limitations'],
        earlier_coarse_plan=str(args.original_plan), prior_fields_unchanged=True),indent=2)+'\n')
    print(json.dumps(dict(plan=str(plan_path), sha256=sha(plan_path), radial=len(grid),
                         angular=angular, witness_retained=True, cases=len(planned))))


if __name__ == '__main__':
    main()
