#!/usr/bin/env python3
"""Inspect a genuinely accepted current M32 field plus an explicit old increment.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The frozen stale-warm constructor verifies the actual current acceptance and
owns every change of mesh, parameter units and state increment. The old M28
response is never relabelled as a derivative at the current point. A fresh
grid retains all old comparison points, all current raw nodes, current
physical anchors and the current fixed-view quintic witness. No future
accepted primary or witness is fabricated. Geometry is only an unsolved
complete-mean warm diagnostic, with every original physical-domain gate.

Control arguments are increments from the current accepted point. If a
proposal was specified as a total increment from the old baseline, its
already implemented physical controls must first be subtracted explicitly.
No automatic inference of that subtraction is made by this entry.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import ast
import gzip
import hashlib
import inspect
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ORIGINAL_FINE_SHA = 'c986073622d4ebabb2be7d1eea46fe8ac4966a404b56bbc6a6af3b48371092bc'
STALE_SHA = 'e21809f94b1b702481ff30181fc936c5ea9e43d9436b4fe69586efadef10bbd0'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def one(argv, key):
    if argv.count(key) != 1:
        raise ValueError('Require one actual argument: '+key)
    return argv[argv.index(key)+1]


def current_grid(record, old_path, audit_path, destination):
    import numpy as np
    from root_neck_chart import NeckChart
    from strong_actual_fixed_control_response import raw_flat

    old, audit = read(old_path), read(audit_path)
    current_path, raw_path = Path(record['current_reference']), Path(record['current_raw'])
    current, raw = read(current_path), read(raw_path)
    if (record.get('explicitly_stale_response') is not True or
            record.get('current_point_derivative_claim') is not False or
            not record['current_original_acceptance']['complete_original_physical_fields_and_raw_bits_verified']):
        raise ValueError('Use the actual accepted-current stale constructor, not an unverified plan')
    if (not current['solver_success'] or current.get('audit_pending', True) or
            not current['config'].get('actual_nonlinear_tail') or not raw['solver_success'] or
            current['modes'] != 32 or len(current['parameters']) != 32 or
            raw['arrays']['p']['shape'] != [32] or not raw['identity'].get('fixed') or
            current['raw_collocation_checkpoint']['sha256'] != sha(raw_path)):
        raise ValueError('A completed original M32 fixed view and its actual raw bits are required')
    if (old.get('raw_sha256') != sha(record['coarse_raw']) or old['angular'] != 768 or
            audit.get('input_sha256') != sha(current_path) or audit.get('modes') != 32 or
            audit['config'].get('mean_angular') != 1552 or audit['config'].get('angular') != 768):
        raise ValueError('Bind old comparison grid and actual current complete-mean witness explicitly')
    chart_record = current['numerical_meridian_chart']
    if (chart_record['kind'] != 'C2-all-physical-knots-v1' or
            raw['identity']['numerical_reference_knots'] != chart_record['reference_t'] or
            raw['identity']['profile'] != current['frozen_profile']):
        raise ValueError('The current accepted physical profile or material chart differs')
    arrays = {}
    x = np.asarray(raw_flat(raw_path, raw, 'x', arrays)).reshape(raw['arrays']['x']['shape'])
    old_t = np.asarray(old['numerical_t'], dtype=float)
    for values in (x, old_t):
        if (not np.isfinite(values).all() or values.ndim != 1 or values[0] != 0. or
                values[-1] != 1. or not np.all(np.diff(values) > 0.)):
            raise ValueError('Every actual comparison mesh must be oriented on [0,1]')

    chart = NeckChart(chart_record['reference_t'], chart_record['physical_s'])
    physical = np.unique(np.r_[np.linspace(chart.s[0], chart.s[-1], 241),
        *[np.linspace(a, b, 33) for a, b in zip(chart.s[:-1], chart.s[1:])]])
    mapped = chart.inverse(physical)
    roundtrip = float(np.max(abs(chart.evaluate(mapped)[0]-physical)))
    if roundtrip > 1e-12:
        raise ValueError('Current physical anchors failed original chart inversion')
    witnesses = []
    for saved in old.get('known_reference_witnesses', []):
        item = dict(saved)
        item['numerical_t'] = float(old_t[saved['radial_index']])
        item['eta'] = float(saved.get('eta', saved['angular_index']*2*np.pi/768))
        item['old_witness_only'] = True
        item['current_extremum_claimed'] = False
        item['source_grid'] = str(old_path)
        witnesses.append(item)
    peak = audit['top']['kappa']
    physical_s, eta = float(peak['s']), float(peak['psi'])
    if not chart.s[0] <= physical_s <= chart.s[-1]:
        raise ValueError('The actual current quintic curvature witness is outside the chart')
    angle_index = int(round(eta*768/(2*np.pi))) % 768
    if abs(np.angle(np.exp(1j*(angle_index*2*np.pi/768-eta)))) > 1e-13:
        raise ValueError('The complete angular grid omits the current actual witness')
    t_peak = float(chart.inverse(np.asarray([physical_s]))[0])
    witness_roundtrip = float(abs(chart.evaluate(np.asarray([t_peak]))[0][0]-physical_s))
    if witness_roundtrip > 1e-12:
        raise ValueError('The current actual witness failed the original physical chart inverse')
    witnesses.append(dict(numerical_t=t_peak, physical_s=physical_s, eta=eta,
        angular_index=angle_index, source_audit=str(audit_path), source_audit_sha256=sha(audit_path),
        source_audit_input_sha256=sha(current_path), source_polynomial_sample=peak['value'],
        current_accepted_fine_polynomial_witness=True, old_witness_only=False,
        raw_cubic_does_not_replace_actual_quintic_witness=True))
    grid = np.unique(np.r_[old_t, x, mapped, chart.t, np.linspace(0., 1., 257),
        [w['numerical_t'] for w in witnesses]])
    if not np.isin(x, grid).all() or not np.isin(old_t, grid).all():
        raise ValueError('An actual raw or old comparison point was dropped')
    for witness in witnesses:
        index = int(np.searchsorted(grid, witness['numerical_t']))
        if index >= len(grid) or grid[index] != witness['numerical_t']:
            raise ValueError('An actual saved witness was dropped')
        witness['radial_index'] = index
    identity = dict(source_sha256=sha(__file__), original_grid=str(old_path),
        original_grid_sha256=sha(old_path), coarse_raw_sha256=sha(record['coarse_raw']),
        current_reference_sha256=sha(current_path), current_raw_sha256=sha(raw_path),
        current_original_acceptance=record['current_original_acceptance'],
        current_audit=str(audit_path), current_audit_sha256=sha(audit_path),
        original_raw_array_sha256=arrays, all_original_comparison_points_retained=True,
        all_current_raw_nodes_retained=True, all_current_physical_anchors_retained=True,
        current_actual_quintic_witness_retained=True, current_witness_roundtrip=witness_roundtrip,
        old_witnesses_not_relabelled_as_current_extrema=True, no_new_field_evaluation=True,
        old_and_current_physical_charts_claimed_equal=False,
        direction_is_explicitly_stale_initial_guess=True)
    new = dict(numerical_t=grid.tolist(), angular=768, grid_only=True,
        raw_sha256=sha(raw_path), original_raw_nodes=len(x),
        all_original_raw_nodes_used_in_cubic=True, all_original_raw_nodes_evaluated=True,
        saved_physical_knots=len(chart.s), mapped_physical_anchors=len(physical),
        chart_roundtrip_max=roundtrip, known_reference_witnesses=witnesses,
        rule='All old numerical comparison points; all actual current raw nodes; current 241 uniform physical anchors and 33 per physical interval; all material knots; 257 uniform material anchors; actual current fixed-view quintic witness.',
        inherited_witnesses_are_not_claimed_to_be_new_extrema=True,
        actual_current_stale_grid_bridge=identity)
    if destination.exists():
        if read(destination) != new:
            raise ValueError('Existing current grid differs from this actual input identity')
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(new, indent=2)+'\n')
    return identity


def main():
    original_path = HERE/'root_actual_coarse_increment_geometry_complete_mean.py'
    if sha(original_path) != ORIGINAL_FINE_SHA:
        raise ValueError('The original complete-mean fine geometry adapter changed')
    import root_actual_coarse_increment_geometry_complete_mean as original
    before = inspect.getsource(original.main)
    anchor = "    p.add_argument('--coarse-warm-source',type=Path,required=True)\n"
    replacement = (anchor+
        "    p.add_argument('--current-original-accepted',type=Path,required=True)\n"
        "    p.add_argument('--current-owned-resource',type=Path,required=True)\n")
    if before.count(anchor) != 1:
        raise ValueError('The original parser site changed')
    source = before.replace(anchor, replacement, 1)
    if source.replace(replacement, anchor, 1) != before:
        raise ValueError('An undeclared original complete-mean entry site changed')
    ast.parse(source)
    namespace = dict(original.__dict__, __file__=str(Path(__file__).resolve()), __doc__=__doc__,
        COARSE_WARM_SHA=STALE_SHA, fine_grid=current_grid)
    exec(compile(source, '<actual-current-stale-complete-mean-geometry>', 'exec'), namespace)
    namespace['main']()
    prefix = Path(one(sys.argv, '--out-prefix'))
    metadata = Path(str(prefix)+'-coarse-fine-geometry-prepared.json')
    record = read(metadata)
    record['actual_current_stale_geometry_adapter'] = dict(source_sha256=sha(__file__),
        original_fine_adapter_sha256=ORIGINAL_FINE_SHA, actual_stale_constructor_sha256=STALE_SHA,
        original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
        executed_main_sha256=hashlib.sha256(source.encode()).hexdigest(),
        exact_reverse_recovers_original_main=True,
        only_parser_arguments_and_declared_constructor_grid_callbacks_changed=True,
        all_original_complete_mean_geometry_and_physical_domain_formulas_retained=True,
        actual_current_original_acceptance_required=True, future_state_not_fabricated=True,
        controls_are_current_increment_not_old_total=True,
        current_fine_Jacobian_or_new_solution_claim=False)
    record['source_and_input_sha256'][str(original_path)] = ORIGINAL_FINE_SHA
    metadata.write_text(json.dumps(record, indent=2)+'\n')
    if '--coarse-fine-geometry-prepare-only' not in sys.argv:
        output = Path(one(sys.argv, '--inspect-warm-output'))
        report = read(output)
        report['actual_current_stale_geometry_adapter'] = record['actual_current_stale_geometry_adapter']
        report['fine_complete_mean_coarse_warm_adapter']['preparation_sha256'] = sha(metadata)
        report['source_sha256'][str(Path(__file__).resolve())] = sha(__file__)
        report['source_sha256'][str(original_path)] = ORIGINAL_FINE_SHA
        output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(event='actual_current_stale_fullmean_geometry_prepared',
        metadata=str(metadata), sha256=sha(metadata),
        preparation_only='--coarse-fine-geometry-prepare-only' in sys.argv,
        original_complete_mean_geometry_formulas_retained=True)), flush=True)


if __name__ == '__main__':
    main()
