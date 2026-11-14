#!/usr/bin/env python3
"""Small actual-input check of the explicit physical-bump native reader.

Only field/jet and body-RHS evaluations are done; no body ODE or BVP is run.
The derived nonzero-delta archive is a declared test fixture, not an accepted
candidate. The exact stored mesh is retained unchanged.
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
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_bump_native_field import RawBumpNativeField

HERE = Path(__file__).resolve().parent


def maximum(value):
    return float(np.max(np.abs(value), initial=0.))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh diagnostic stem')
    started = time.monotonic()
    source_paths = [Path(__file__)]+[HERE/name for name in
        ('fd2d_gc_bump_native_field.py', 'fd2d_gc_raw_native_field.py',
         'fd2d_gc_radial_bump_profile.py', 'fd2d_gc_raw_bump_dae.py',
         'fd2d-metric-bump-body-screen.py', 'fd2d-metric-raw-body-screen.py')]
    sources = [identity(path) for path in source_paths]
    saved = load_npz(args.field)
    if str(saved['profile_kind']) != 'physical_bumps' or str(saved['candidate_sha256']) != identity(args.candidate)['sha256']:
        raise ValueError('Wrong explicitly saved physical-bump candidate')
    K = (saved['corrections'].shape[1]-2)//3
    model = RawBumpDAE(args.candidate, modes=K, max_step=.04,
        base_kind=str(saved['base_kind']), supports=saved['profile_supports'],
        profile_count=int(saved['profile_count']))
    if not np.array_equal(model.x, saved['mesh']):
        raise ValueError('This finite provider comparison requires its exact recorded grid; reader itself does not rebuild it')
    actual = {key: value.copy() for key, value in saved.items()}
    delta = .0003*np.cos(.7+1.3*np.arange(model.J))
    actual['parameters'][model.profile_parameter_slice] = delta
    actual['blend'] = np.asarray(model.blend)
    actual['diagnostic_fixture_only'] = np.array(True)
    actual['fixture_source_field_sha256'] = np.array(identity(args.field)['sha256'])
    field_row = save_npz(Path(str(stem)+'-fixture.npz'), **actual)
    reader = RawBumpNativeField(field_row['path'], args.candidate)
    definition_path = Path(str(stem)+'-definition.json')
    definition_path.write_text(json.dumps(reader.definition(), indent=2, allow_nan=False)+'\n')
    restored = RawBumpNativeField.from_definition(definition_path)
    vector = np.r_[actual['corrections'].ravel(), actual['parameters']]
    _, data = model.evaluate(vector)
    angles = np.asarray(model.chart.theta, float)
    native = reader.evaluate_native(model.x[None, :], angles[:, None])
    fields = np.stack([native[key] for key in ('n', 'm', 'l')], axis=-1)
    y, _ = model.unpack(vector)
    first_expected = np.stack((model.Ex@y[:, :model.e].T,
                              model.Ox@y[:, model.e:model.d].T,
                              model.Ex@y[:, model.d:].T), axis=-1)+data['lift']['xi']
    first = np.stack([native[key+'_xi'] for key in ('n', 'm', 'l')], axis=-1)
    field_error = maximum(fields-data['fields'])
    angle_error = maximum(first-first_expected)
    # Shared P1 node values and all angular derivatives are independent of
    # which cell supplies the one-sided radial derivative.
    selected = np.unique(np.linspace(1, len(reader.nodes)-2, 11, dtype=int))
    x = reader.nodes[selected]
    xi = .13+.37*np.arange(len(x))
    left = reader.evaluate_native(x, xi, side='left')
    right = reader.evaluate_native(x, xi, side='right')
    continuity = {suffix: max(maximum(left[key+suffix]-right[key+suffix]) for key in ('n', 'm', 'l'))
                  for suffix in ('', '_xi', '_xixi')}
    # Fixed-material conversion at actual interior points: compare fields,
    # angle inversion and the chain-rule radial derivative with finite probes.
    widths = np.diff(reader.nodes)
    valid = np.flatnonzero(widths > 1e-4)
    ids = valid[np.unique(np.linspace(0, len(valid)-1, 9, dtype=int))]
    s = reader.nodes[ids]+.41*widths[ids]
    u = .18+.39*np.arange(len(s))
    phys = reader.physical(s, u)
    hx = np.minimum(2e-6, .1*widths[ids])
    plus, minus = reader.physical(s+hx, u), reader.physical(s-hx, u)
    radial_rows = {}
    for key in ('n', 'm', 'l'):
        finite = (plus[key]-minus[key])/(2*hx)
        exact = phys[key+'_s']
        radial_rows[key] = dict(absolute_maximum=maximum(finite-exact),
            relative_l2=float(np.linalg.norm(finite-exact)/max(1., np.linalg.norm(exact))))
    other = restored.physical(s, u)
    roundtrip = max(maximum(other[key]-phys[key]) for key in ('n', 'm', 'l', 'l_u', 'm_u', 'l_uu', 'm_uu', 'a'))
    cut_u = 2*np.pi*(np.arange(32)+.13)/32
    cut = reader.physical(reader.nodes[-1], cut_u, side='left')
    tail = reader.tail.cut_port(cut_u)
    cut_error = max(maximum(cut[key]-tail[key]) for key in ('n', 'm', 'l'))
    initial = reader.body_initial(cut_u[:8])
    body_rhs = reader.body_rhs(s[0], initial, cut_u[:8])
    body_jets = reader.body_jets(0., initial, cut_u[:8])
    profile_delta_effect = maximum(reader.profile.jet(s)['a']-reader.profile.base.profile(s)[0])
    checks = dict(saved_mesh_unchanged=np.array_equal(reader.nodes, saved['mesh']),
        all_saved_delta_parameters_retained=np.array_equal(reader.parameters[reader.profile_parameter_slice], delta),
        physical_clock_exactly_one=np.array_equal(phys['J'], np.ones_like(s)),
        physical_coordinate_equals_saved_s=np.array_equal(phys['s'], s),
        actual_nonzero_metric_change=profile_delta_effect > 1e-8,
        node_fields_match_actual_provider=field_error < 2e-10,
        full_angular_first_jets_match=angle_error < 2e-9,
        shared_node_values_and_angular_jets=max(continuity.values()) == 0.,
        fixed_material_angle_inverse=maximum(phys['angle_inverse_error']) < 2e-12,
        fixed_material_radial_chain_rule=max(row['relative_l2'] for row in radial_rows.values()) < 2e-5,
        definition_roundtrip_identical=roundtrip == 0.,
        actual_cut_II_keeps_full_tail=cut_error < 2e-10,
        body_RHS_24_columns_finite=body_rhs.shape == (8, 24) and np.all(np.isfinite(body_rhs)),
        initial_actual_twojet_finite=all(np.all(np.isfinite(body_jets[key])) for key in ('X', 'X_s', 'X_u', 'X_ss', 'X_su', 'X_uu')),
        source_bytes_unchanged=all(before['sha256'] == identity(path)['sha256'] for before, path in zip(sources, source_paths)))
    report = dict(schema='fd2d-physical-bump-native-reader-check-v1', sources=sources,
        input_field=identity(args.field), candidate=identity(args.candidate), fixture=field_row,
        actual_definition=identity(definition_path), modes=K, nodes=len(reader.nodes),
        actual_test_delta=delta.tolist(), provider_node_fields_maximum_difference=field_error,
        provider_full_angular_first_jets_maximum_difference=angle_error,
        shared_node_continuity=continuity, physical_radial_chain_rule=radial_rows,
        angular_inverse_error=maximum(phys['angle_inverse_error']), definition_roundtrip_difference=roundtrip,
        cut_full_II_difference=cut_error, nonzero_profile_effect_at_test_points=profile_delta_effect,
        checks=checks, implementation_checks_passed=all(checks.values()),
        actual_body_integration_run=False, BVP_run=False, continuous_certificate=False,
        seconds=time.monotonic()-started,
        scope='Actual archived field binding, spatial jets, fixed-material body RHS only; no ODE, geometry success, or same-g refinement claim')
    report_path = Path(str(stem)+'-report.json')
    report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(report_path), checks=checks,
        field_error=field_error, angle_error=angle_error, cut_error=cut_error,
        radial_chain_rule=radial_rows, seconds=report['seconds'])), flush=True)
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
