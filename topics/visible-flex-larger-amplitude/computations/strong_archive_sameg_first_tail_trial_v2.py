#!/usr/bin/env python3
"""Freeze an actual first-H accepted trial with fresh observed-adapter names.

This only copies original worker data and checks its complete dimensions,
current-H bits, indexed raw states, parameters and recorded actual constructor
identity. The original live solve is not interrupted. A norm below tolerance
does not replace its pending final variational evaluation, audit or prefix.
"""
from __future__ import annotations
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
IO_KEYS = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix', type=Path, required=True)
    p.add_argument('--launch-plan', type=Path, required=True)
    p.add_argument('--iteration-checkpoint', type=Path)
    p.add_argument('--archive-topic', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    a = p.parse_args()
    path = lambda suffix: Path(str(a.prefix)+suffix)
    original_path = path('-tail-iteration.json.gz')
    data = (a.iteration_checkpoint or original_path).read_bytes()
    trial = json.loads(gzip.decompress(data))
    event, c = trial['iteration'], trial['checkpoint']
    if (trial['status'] != 'iteration-recovery-only' or trial['call'] != 1
            or event['phase'] != 'accepted-trial-recovery-only'
            or event['iteration'] < 1 or not np.isfinite(event['norm'])
            or not 0 < event['acceptedStep'] <= 1):
        raise ValueError('Expected an original actual first-H accepted trial')
    cfg, warm = read(path('-config.json')), read(path('-spectral-tail-zero-warm.json.gz'))
    params = c['parameters']
    if ({key:value for key,value in params.items() if key not in IO_KEYS} !=
            {key:value for key,value in warm['parameters'].items() if key not in IO_KEYS}):
        raise ValueError('The complete effective mathematical tail parameters differ')
    config_changes = {key:[value, params.get(key)] for key,value in cfg.items()
                      if key not in IO_KEYS and params.get(key) != value}
    if config_changes != {'depth':[8, 576],
            'linearMethod':['projective', 'stable-momentum-cusp-subdivision']}:
        raise ValueError('The original physical-depth/stable-subdivision constructor relation differs')
    m = int(params['modes'])
    states, raw = np.asarray(c['states'], dtype=np.float64), np.asarray(c['rawStates'], dtype=np.float64)
    idx, height = np.asarray(c['rawNode'], dtype=np.int64), np.asarray(c['cutHeight'], dtype=np.float64)
    if (m != warm['target_mode_count'] or params['physicalDepth'] != warm['parameters']['physicalDepth']
            or states.shape != (params['depth']+1, 2*m) or raw.shape != (len(idx), 2*m)
            or height.shape != (m,) or not np.isfinite(states).all() or not np.isfinite(height).all()
            or np.any(idx < 0) or np.any(idx >= len(states))
            or states[idx].tobytes() != raw.tobytes()
            or not np.array_equal(height, np.asarray(warm['cutHeight'], dtype=np.float64))):
        raise ValueError('The complete same-H states/raw indices/mode embedding differ')
    warm_height = np.asarray(warm['cutHeight'], dtype=np.float64)
    bit_differences = np.flatnonzero(height.view(np.uint64) != warm_height.view(np.uint64))
    if np.any(height[bit_differences] != 0.) or np.any(warm_height[bit_differences] != 0.):
        raise ValueError('The JSON checkpoint changed a nonzero height bit')
    physical_path = path('-tail-response_sameg-M32-physical-identity.json')
    physical = read(physical_path)
    actual_keys = ('all_effective_non_mode_non_IO_parameters_equal',
        'complete_calibration_adapter_and_160_original_cells_identical',
        'profile_fingerprints_identical', 'original_cut_scalars_bitwise_equal',
        'new_full_flow_snapshot_not_restored_from_old_M',
        'distinct_exact_stage_identity_for_new_M', 'original_warm_gate_passed')
    if not all(physical.get(key) is True for key in actual_keys):
        raise ValueError('The actual same-g new-M constructor gate is missing')
    adapter_path = path('-tail-response_full-tangent-adapter.json')
    adapter = read(adapter_path)
    source_hashes = adapter['source_sha256_at_start']
    for name, expected in source_hashes.items():
        if Path(name).name != name or sha((HERE/name).read_bytes()) != expected:
            raise ValueError('A live-start full-flow source changed: '+name)
    trace = [json.loads(line) for line in path('-tail-trace.jsonl').read_text().splitlines()]
    match = [row for row in trace if row.get('event') == 'iteration'
        and row.get('call') == 1 and all(row.get(key) == value for key, value in event.items())]
    if len(match) != 1:
        raise ValueError('The accepted trial does not have a unique original trace receipt')
    observed = [row for row in trace if row.get('event') in ('exact_raw_same_H_initial',
        'exact_initial_stage_seed_saved', 'iteration') and row.get('call') == 1]
    snapshot = Path(str(a.out_prefix)+'.json.gz')
    trace_path = Path(str(a.out_prefix)+'-observed-trace.json')
    for output, payload in ((snapshot, data), (trace_path,
            (json.dumps(observed, indent=2, allow_nan=False)+'\n').encode())):
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('xb') as stream:
            stream.write(payload)
    adapter_snapshot = Path(str(a.out_prefix)+'-full-tangent-adapter-observed.json')
    with adapter_snapshot.open('xb') as stream:
        stream.write(adapter_path.read_bytes())
    files = [snapshot, trace_path, path('-config.json'), physical_path, adapter_snapshot,
             path('-spectral-warm-verified.json'), path('-live-physical-identity.json')]
    entries = []
    for file in files:
        payload = file.read_bytes()
        if len(payload) >= 5_000_000:
            raise ValueError('Original repository per-file cap exceeded')
        target = a.archive_topic/'notes'/file.name
        if target.exists():
            if target.read_bytes() != payload:
                raise ValueError('Existing frozen archive differs: '+str(target))
        else:
            with target.open('xb') as stream:
                stream.write(payload)
        entries.append(dict(file='notes/'+file.name, sha256=sha(payload), bytes=len(payload)))
    result = dict(scope=__doc__, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        archiver_source_sha256=sha(Path(__file__).read_bytes()),
        original_live_file=str(original_path), original_live_bytes_sha256=sha(data),
        original_call=1, original_iteration=event, original_solve_tolerance=params['solveTolerance'],
        modes=m, shooting_states_shape=list(states.shape), raw_states_shape=list(raw.shape),
        all_state_values_finite=True, all_rawNode_and_indexed_rawStates_exact=True,
        complete_current_H_values_equal_original_sameg_spectral_warm=True,
        current_H_bits_equal_original_sameg_spectral_warm=not bool(len(bit_differences)),
        JSON_stringify_signed_zero_differences=bit_differences.tolist(),
        signed_zero_scope='Original worker JSON.stringify writes negative zero as zero; no nonzero value changed.',
        original_request_height_f64le_sha256=sha(warm_height.astype('<f8').tobytes()),
        original_worker_JSON_height_f64le_sha256=sha(height.astype('<f8').tobytes()),
        complete_effective_mathematical_parameters_equal_original_spectral_warm=True,
        original_recorded_config_to_constructor_changes=config_changes,
        actual_sameg_constructor_gates={key:physical[key] for key in actual_keys},
        live_start_full_flow_sources_verified=source_hashes,
        launch_plan=dict(file=str(a.launch_plan), sha256=sha(a.launch_plan.read_bytes())),
        final_full_current_H_Jacobian_pending=True, actual_physical_BC_and_final_audit_pending=True,
        whole_owned_job_exit_pending=True, original_live_job_not_interrupted=True,
        numerical_tail_or_prefix_accepted=False, files=entries,
        total_bytes=sum(row['bytes'] for row in entries))
    manifest = Path(str(a.out_prefix)+'-manifest.json')
    payload = (json.dumps(result, indent=2, allow_nan=False)+'\n').encode()
    with manifest.open('xb') as stream:
        stream.write(payload)
    target = a.archive_topic/'notes'/manifest.name
    if target.resolve() != manifest.resolve():
        with target.open('xb') as stream:
            stream.write(payload)
    print(json.dumps(dict(manifest=str(target), sha256=sha(payload),
        files=len(entries), bytes=result['total_bytes'], norm=event['norm'])), flush=True)


if __name__ == '__main__':
    main()
