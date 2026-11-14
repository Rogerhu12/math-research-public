#!/usr/bin/env python3
"""Small provider-only identity and endpoint checks for the explicit pulse hook.

No actual Flow, prefix RHS/Jac/BVP, or Node/tail worker is loaded.  This checks
the actual old provider before/after the hook, not a duplicate implementation.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
import strong_initial_speed_pulse as hook

P = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted-reference', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    start = time.time()
    paths = [Path(__file__), P/'strong_initial_speed_pulse.py', P/'alternative-neck-provider.py',
        P/'strong_angle_boost.py', P/'alternative-neck-flatturn.py', P/'alternative-neck-excursion.py',
        args.accepted_reference]
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    record = json.loads(gzip.decompress(args.accepted_reference.read_bytes()))
    cfg = dict(record['frozen_profile'])
    spec = importlib.util.spec_from_file_location('strong_pulse_actual_provider_check', P/'alternative-neck-provider.py')
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    u = np.unique(np.r_[np.linspace(0., 1., 513), .08, .92])

    def materialize(law):
        data = []
        for segment in law.segments:
            data.extend(np.asarray(z, dtype=np.float64) for z in provider.piece_jet(segment, u))
            data.append(np.asarray(provider.velocity(segment, u), dtype=np.float64))
        return np.concatenate([z.ravel() for z in data]).tobytes()

    old = provider.NeckPrefix(cfg)
    old_data = materialize(old)
    old_metadata = json.dumps(old.segments, sort_keys=True)
    old_knots = old.breaks().tobytes()
    hook.install(provider)
    installed = provider.NeckPrefix
    hook.install(provider)
    default = provider.NeckPrefix(cfg)
    zero = provider.NeckPrefix(dict(cfg, initial_speed_pulse=0.))
    checks = dict(install_idempotent=provider.NeckPrefix is installed,
        absent_key_all_jets_and_velocity_bitwise_equal=materialize(default) == old_data,
        explicit_zero_all_jets_and_velocity_bitwise_equal=materialize(zero) == old_data,
        absent_key_all_segment_metadata_equal=json.dumps(default.segments, sort_keys=True) == old_metadata,
        explicit_zero_all_segment_metadata_equal=json.dumps(zero.segments, sort_keys=True) == old_metadata,
        both_default_reference_breaks_bitwise_equal=default.breaks().tobytes() == old_knots == zero.breaks().tobytes(),
        default_length_and_height_equal=default.end == zero.end == old.end and default.height == zero.height == old.height)
    rows = []
    for b in (-.001, .001, .2, .35, .5, .6):
        law = provider.NeckPrefix(dict(cfg, initial_speed_pulse=b))
        segment = law.segments[0]
        a, v, acc = provider.piece_jet(segment, u)
        initial = np.asarray([float(z) for z in provider.piece_jet(segment, np.asarray(0.))])
        terminal = np.asarray([float(z) for z in provider.piece_jet(segment, np.asarray(1.))])
        interior = np.linspace(.01, .99, 99)
        h = 1e-6
        fd = (provider.velocity(segment, interior+h)-provider.velocity(segment, interior-h))/(2*h*segment['length'])
        analytic = provider.piece_jet(segment, interior)[2]
        fd_error = float(np.max(abs(fd-analytic)))
        later_radius_error = 0.
        later_velocity_error = 0.
        for earlier, later in zip(old.segments[1:], law.segments[1:]):
            left, right = provider.piece_jet(earlier, u), provider.piece_jet(later, u)
            later_radius_error = max(later_radius_error, float(np.max(abs(left[0]-right[0]))))
            later_velocity_error = max(later_velocity_error, float(np.max(abs(left[1]-right[1]))), float(np.max(abs(left[2]-right[2]))))
        row = dict(pulse=b, S=law.S, height=law.height,
            initial_jet=initial.tolist(), terminal_jet=terminal.tolist(),
            expected_initial_jet=[1., 0., cfg['start_acceleration']],
            expected_terminal_jet=[1+cfg['delta'], cfg['vu'], 0.],
            initial_endpoint_error=float(np.max(abs(initial-[1., 0., cfg['start_acceleration']]))),
            terminal_endpoint_error=float(np.max(abs(terminal-[1+cfg['delta'], cfg['vu'], 0.]))),
            all_sample_speeds_in_domain=bool(np.all(v >= -2e-15) and np.all(v < 1)),
            velocity_jet_same_values=provider.velocity(segment, u).tobytes() == np.asarray(v).tobytes(),
            second_jet_finite_difference_max_error=fd_error,
            later_radius_max_float_error=later_radius_error,
            later_velocity_and_acceleration_max_float_error=later_velocity_error,
            segment_and_chart_topology_same=len(law.segments) == len(old.segments) and len(law.breaks()) == len(old.breaks()))
        row['passed'] = (row['initial_endpoint_error'] <= 3e-15 and row['terminal_endpoint_error'] <= 3e-15
            and row['all_sample_speeds_in_domain'] and row['velocity_jet_same_values'] and fd_error < 2e-8
            and later_radius_error < 4e-15 and later_velocity_error == 0. and row['segment_and_chart_topology_same'])
        rows.append(row)
    checks['all_nonzero_pulse_checks'] = all(row['passed'] for row in rows)
    rejected = []
    for b in (float('nan'), float('inf'), .8, -.1):
        try:
            provider.NeckPrefix(dict(cfg, initial_speed_pulse=b))
        except ValueError:
            rejected.append(True)
        else:
            rejected.append(False)
    checks['invalid_pulses_rejected'] = all(rejected)
    result = dict(scope=__doc__, passed=all(checks.values()), checks=checks,
        source_sha256_at_start=hashes, rows=rows, initial_reference_bytes_sha256=hashlib.sha256(old_data).hexdigest(),
        physical_profile_key='initial_speed_pulse', default=0.,
        second_jet_FD_is_only_an_implementation_check=True,
        actual_core_held_response_computed=False, BVP_evaluations=0, Node_workers=0, seconds=time.time()-start)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(passed=result['passed'], checks=checks,
        maximum_FD_error=max(r['second_jet_finite_difference_max_error'] for r in rows))), flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
