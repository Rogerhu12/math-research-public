#!/usr/bin/env python3
"""Read-only comparison of two CLOSED matched-cut DN packets; no solver imports.

Writes only scalar diagnostics and file identities to a new output path.
This does not inspect the active continuation03 outputs.
"""
import argparse
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path

import numpy as np

TOPIC = Path(__file__).resolve().parents[1]
NOTES = TOPIC / 'notes'
STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01'
OBS = NOTES / '2026-11-09-db6f-root-matched-cut-observed-execution-01.json'
EXPECTED = {
    OBS.name: '1f7a7290c5c65a9f73531cd0edddf8f15b0290477be7d0b74eff9a3d5ba57334',
    STEM + '_tail_0001.json.gz': '6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86',
    STEM + '_tail_0002.json.gz': '44088a6fce132438771fb83267754f32e8d12043379b8f83c1977eccaad0d1de',
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def identity(path):
    p = Path(path).resolve()
    digest = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            digest.update(block)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest.hexdigest()}


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    if p.suffix == '.gz':
        raw = gzip.decompress(raw)
    return json.loads(raw)


def verify(row):
    actual = identity(row['path'])
    assert actual['bytes'] == row['bytes']
    assert actual['sha256'] == row['sha256']
    return actual


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and np.isfinite(x)


def vector(value, n):
    assert isinstance(value, list) and len(value) == n and all(number(x) for x in value)
    return np.asarray(value, dtype=float)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    out = args.out.resolve()
    assert out.parent.is_dir() and not out.exists()

    paths = [OBS, NOTES / (STEM + '_tail_0001.json.gz'), NOTES / (STEM + '_tail_0002.json.gz')]
    for p in paths:
        assert identity(p)['sha256'] == EXPECTED[p.name]
    observed, first, second = map(read, paths)
    assert observed['status'] == 'observed-process-completed'
    assert observed['observer'] == '/root' and observed['session_id'] == 5817
    assert observed['tool_receipt'] == 'ff466f' and observed['actual_exit_code'] == 0
    assert observed['summary_solver_success'] is False
    assert observed['prefix_final_checkpoint_exists'] is False
    closed = [verify(row) for row in observed['files']]
    assert len(closed) == 15
    assert canonical(first['config']) == canonical(second['config'])
    assert canonical(first['source_sha256']) == canonical(second['source_sha256'])
    assert len(first['source_sha256']) == 8
    source_rows = []
    for name, sha in first['source_sha256'].items():
        row = identity(TOPIC / 'scripts' / name)
        assert row['sha256'] == sha
        source_rows.append(row)

    a, b = first['response'], second['response']
    cfg = first['config']
    M = cfg['modes']
    assert M == 15 and cfg['solveTolerance'] == 2e-9 and cfg['maxIterations'] == 36
    assert cfg.get('projectionFloor', .05) == .05
    assert first['request']['jacobian'] is True and first['request']['audit'] is False
    assert second['request']['jacobian'] is True and second['request']['audit'] is False
    assert a['converged'] is True and number(a['residual']) and 0 <= a['residual'] < cfg['solveTolerance']
    assert set(b) == {'failed', 'lastIteration', 'checkpoint'}
    assert b['failed'] == 'Error: multiple-shooting line search failed at 2489.354194334243'
    H0, H1 = vector(first['request']['height'], M), vector(second['request']['height'], M)
    assert np.all(H0 != 0)
    returned = vector(a['jets']['height'], M)
    delta = H1 - H0
    ratio = H1[0] / returned[0]
    oldQ = vector(a['checkpoint']['states'][0], 2 * M)[:M]
    radius = a['jets']['radius']
    correction = H1 / radius**4 - ratio * oldQ
    relative = np.abs(delta / H0)
    maximum = int(np.argmax(np.abs(delta)))
    relative_max = int(np.argmax(relative))
    correction_max = int(np.argmax(np.abs(correction)))
    shape = {'states': [len(a['checkpoint']['states']), len(a['checkpoint']['states'][0])],
             'rawStates': [len(a['checkpoint']['rawStates']), len(a['checkpoint']['rawStates'][0])],
             'heightJetJacobian': len(a['heightJetJacobian']), 'jets_keys': len(a['jets'])}
    assert shape == {'states': [865, 30], 'rawStates': [13, 30], 'heightJetJacobian': 705, 'jets_keys': 17}

    trace_path, trials_path = Path(cfg['traceFile']), Path(cfg['trialDiagnosticFile'])
    trace = [json.loads(line) for line in trace_path.read_text().splitlines() if line]
    trials = [json.loads(line) for line in trials_path.read_text().splitlines() if line]
    iteration_rows = [r for r in trace if r.get('call') == 2 and r.get('event') == 'iteration' and r.get('phase') != 'correction']
    accepted = [r for r in trials if r.get('call') == 2 and r.get('kind') == 'accepted']
    assert [r['step'] for r in accepted] == [1 / 128, 1 / 256, 1 / 256]
    last_trials = [r for r in trials if r.get('call') == 2 and r.get('iteration') == b['lastIteration']['iteration']]
    assert len(last_trials) == 10
    assert all(r['kind'] == 'momentum-root-solver-rejection' for r in last_trials)
    assert all(r.get('rawCell') == 0 and r.get('rawSegment') == 4 for r in last_trials)
    summary_path = NOTES / (STEM + '-summary.json')
    summary = read(summary_path)
    assert summary['solver_success'] is False and summary['tail_calls'] == 2
    assert not (NOTES / (STEM + '.json.gz')).exists()
    input_binding = NOTES / (STEM + '-input-bindings.json')
    binding = read(input_binding)
    assert len(binding['bound_files']) == 121

    report = {
        'status': 'CLOSED_PACKET_SCALAR_COMPARISON_PASS',
        'scope': 'Closed matched-cut packets only. No root, flow, DN, BVP, active continuation03 read, or new candidate.',
        'observed_tool_exit': {k: observed[k] for k in ('status', 'observer', 'session_id', 'tool_receipt', 'actual_exit_code')},
        'closed_observed_file_count_rehashed': len(closed),
        'original_121_binding_scope': 'The binding document is hashed here; its whole 121-file closure was previously checked by root and the preparer reviews, not newly claimed as rehashed by this scalar comparison.',
        'same_typed_config_and_source8': True,
        'first': {'request_jacobian': True, 'request_audit': False, 'response_keys': sorted(a),
                  'converged': a['converged'], 'residual': a['residual'], 'history_count': len(a['history']),
                  'first_history': a['history'][0], 'shape': shape,
                  'returned_request_height_max_difference': float(np.max(np.abs(returned - H0)))},
        'second': {'request_jacobian': True, 'request_audit': False, 'response_keys': sorted(b),
                   'failed': b['failed'], 'lastIteration': b['lastIteration'],
                   'normal_converged_residual_history_fields_absent': all(k not in b for k in ('converged', 'residual', 'history'))},
        'height_difference': {'changed_components': int(np.count_nonzero(delta)),
                              'sign_changes': int(np.count_nonzero(np.signbit(H0) != np.signbit(H1))),
                              'max_absolute': float(abs(delta[maximum])), 'max_absolute_mode': maximum + 1,
                              'relative_l2': float(np.linalg.norm(delta) / np.linalg.norm(H0)),
                              'max_component_relative': float(relative[relative_max]), 'max_component_relative_mode': relative_max + 1,
                              'absolute_at_max_relative': float(abs(delta[relative_max])),
                              'worker_uniform_ratio': float(ratio), 'higher_nonzero_counts': [int(np.count_nonzero(H0[1:])), int(np.count_nonzero(H1[1:]))],
                              'original_linear_boundary_delta_max_abs': float(abs(correction[correction_max])),
                              'original_linear_boundary_delta_max_mode': correction_max + 1,
                              'only_scalar_formula_recomputed': True},
        'trace': {'rows': len(trace), 'second_base_rows': iteration_rows,
                  'trials_rows': len(trials), 'accepted_steps': [r['step'] for r in accepted],
                  'last_iteration_trial_count': len(last_trials),
                  'last_iteration_kinds': dict(Counter(r['kind'] for r in last_trials)),
                  'last_iteration_stages': sorted(set(r['stage'] for r in last_trials))},
        'actual_prefix_status': {'solver_success': summary['solver_success'], 'tail_calls': summary['tail_calls'],
                                 'summary_seconds': summary['seconds'], 'successful_prefix_checkpoint_exists': False},
        'inputs': sorted({r['path']: r for r in [*closed, *source_rows, identity(OBS), identity(input_binding), identity(Path(__file__))]}.values(), key=lambda r: r['path']),
    }
    encoded = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    assert len(encoded) < 100000
    with out.open('xb') as f:
        f.write(encoded)
    print(json.dumps({'status': report['status'], **identity(out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
