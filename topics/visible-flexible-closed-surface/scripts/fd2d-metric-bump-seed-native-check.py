#!/usr/bin/env python3
"""Read the actual clean/plateau input without changing any saved values.

No solve or body integration. Compare the full native values and jets with
the actual provider, including the explicitly declared central seed weight.
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
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_raw_bump_clean import CleanRawBumpDAE
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField

HERE = Path(__file__).resolve().parent


def maximum(q):
    return float(np.max(np.abs(q), initial=0.))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh report stem')
    started = time.monotonic()
    paths = [Path(__file__)]+[HERE/name for name in
        ('fd2d_gc_bump_seed_native_field.py', 'fd2d_gc_bump_native_field.py',
         'fd2d_gc_raw_native_field.py', 'fd2d_gc_raw_bump_clean.py',
         'fd2d_gc_raw_bump_dae.py', 'fd2d_gc_radial_bump_profile.py',
         'fd2d-metric-bump-body-screen-v2.py')]
    sources = [identity(p) for p in paths]
    saved = load_npz(args.field)
    reader = RawBumpSeedNativeField(args.field, args.candidate)
    model = CleanRawBumpDAE(args.candidate, modes=reader.K, max_step=.04,
        base_kind=reader.base_kind, profile_count=reader.profile_count,
        supports=reader.profile.supports)
    if not np.array_equal(model.x, reader.nodes):
        raise ValueError('This checker needs the actual clean provider grid; reader itself never rebuilds it')
    if model.seed_weight_definition != reader.seed_weight_definition:
        raise ValueError('Actual seed declarations disagree')
    vector = np.r_[saved['corrections'].ravel(), saved['parameters']]
    _, data = model.evaluate(vector)
    xi = np.asarray(model.chart.theta, float)
    native = reader.evaluate_native(reader.nodes[None, :], xi[:, None])
    y, _ = model.unpack(vector)
    expected_first = np.stack((model.Ex@y[:, :model.e].T,
                              model.Ox@y[:, model.e:model.d].T,
                              model.Ex@y[:, model.d:].T), axis=-1)+data['lift']['xi']
    coef_s = reader.state(reader.nodes)[1]
    expected_s = np.stack((model.E@coef_s[:, :model.e].T,
                          model.O@coef_s[:, model.e:model.d].T,
                          model.E@coef_s[:, model.d:].T), axis=-1)+data['lift']['x']
    actual_values = np.stack([native[k] for k in ('n', 'm', 'l')], axis=-1)
    actual_first = np.stack([native[k+'_xi'] for k in ('n', 'm', 'l')], axis=-1)
    actual_s = np.stack([native[k+'_x'] for k in ('n', 'm', 'l')], axis=-1)
    errors = dict(values=maximum(actual_values-data['fields']),
                  full_xi=maximum(actual_first-expected_first), full_s=maximum(actual_s-expected_s))
    # The piecewise slopes may differ across a node; values and angular
    # derivatives must remain shared exactly for the actual C2 body map.
    ids = np.unique(np.linspace(1, len(reader.nodes)-2, 13, dtype=int))
    xp, xpangle = reader.nodes[ids], .17+.29*np.arange(len(ids))
    left = reader.evaluate_native(xp, xpangle, side='left')
    right = reader.evaluate_native(xp, xpangle, side='right')
    continuity = max(maximum(left[k+s]-right[k+s]) for k in ('n', 'm', 'l') for s in ('', '_xi', '_xixi'))
    dp = Path(str(stem)+'-definition.json')
    dp.write_text(json.dumps(reader.definition(), indent=2, allow_nan=False)+'\n')
    restored = RawBumpSeedNativeField.from_definition(dp)
    probes = .37*reader.nodes[ids]+.63*reader.nodes[ids+1]
    material = .22+.41*np.arange(len(probes))
    physical, other = reader.physical(probes, material), restored.physical(probes, material)
    roundtrip = max(maximum(physical[k]-other[k]) for k in
        ('n', 'm', 'l', 'n_s', 'n_u', 'n_uu', 'l_u', 'm_u', 'l_uu', 'm_uu', 'a'))
    # Small analytic-vs-centered probe across the changed seed decay only.
    start, end = (reader.seed_weight_definition[k] for k in ('start', 'end'))
    test_s = start+.371*(end-start)
    probe_u = np.array([.19, .51, 1.02, 1.41])
    p = reader.physical(test_s, probe_u)
    h = 1e-6
    np1, nm1 = reader.physical(test_s+h, probe_u), reader.physical(test_s-h, probe_u)
    finite = (np1['n']-nm1['n'])/(2*h)
    seed_chain_error = float(np.linalg.norm(finite-p['n_s'])/max(1., np.linalg.norm(p['n_s'])))
    initial = reader.body_initial(probe_u)
    rhs = reader.body_rhs(test_s, initial, probe_u)
    source_after = [identity(path) for path in paths]
    checks = dict(actual_saved_mesh_preserved=np.array_equal(reader.nodes, saved['mesh']),
        all_actual_parameters_preserved=np.array_equal(reader.parameters, saved['parameters']),
        actual_plateau_metadata_preserved=reader.seed_weight_definition == model.seed_weight_definition,
        actual_provider_values_and_jets=max(errors.values()) < 3e-9,
        shared_angular_node_jets=continuity == 0., definition_roundtrip_identical=roundtrip == 0.,
        changed_seed_fixed_material_radial_chain=seed_chain_error < 2e-6,
        physical_clock_exactly_one=np.array_equal(physical['J'], np.ones_like(probes)),
        body_rhs_24_columns_finite=rhs.shape == (len(probe_u), 24) and np.all(np.isfinite(rhs)),
        sources_unchanged=all(a['sha256'] == b['sha256'] for a, b in zip(sources, source_after)))
    checks = {k: bool(v) for k, v in checks.items()}
    report = dict(schema='fd2d-actual-explicit-seed-native-check-v1', input_field=identity(args.field),
        candidate=identity(args.candidate), sources=sources, actual_definition=identity(dp),
        seed_weight_definition=reader.seed_weight_definition, representation_kind=reader.representation_kind,
        nodes=len(reader.nodes), minimum_actual_cell=float(np.min(np.diff(reader.nodes))),
        node_field_errors=errors, shared_node_angular_jet_error=continuity,
        definition_roundtrip_error=roundtrip, changed_seed_fixed_material_radial_chain_error=seed_chain_error,
        angular_inverse_error=maximum(physical['angle_inverse_error']),
        checks=checks, implementation_checks_passed=all(checks.values()), seconds=time.monotonic()-started,
        physical_target_changed_by_consumer=False, actual_body_integrated=False, nonlinear_solve_performed=False,
        continuous_certificate=False)
    rp = Path(str(stem)+'-report.json')
    rp.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(rp), checks=checks, errors=errors,
        seed_chain_error=seed_chain_error, seconds=report['seconds'])), flush=True)
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
