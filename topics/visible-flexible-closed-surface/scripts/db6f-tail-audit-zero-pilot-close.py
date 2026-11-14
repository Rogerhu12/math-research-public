#!/usr/bin/env python3
"""Independent read-only audit of the closed zero-start pilot; no numerical solve."""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'
STEM = '2026-11-09-db6f-prefix-zero-initial-s025-original-pilot01'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def checkpoint(value):
    response = value.get('response', value)
    return response.get('checkpoint', response)


def bind(path):
    path = Path(path)
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    launch_path = NOTES/'2026-11-09-db6f-prefix-zero-initial-s025-launch.json'
    observed_path = NOTES/'2026-11-09-db6f-root-zero-initial-s025-observed-execution.json'
    root_audit_path = NOTES/'2026-11-09-db6f-root-zero-initial-s025-closed-audit.json'
    response_path = NOTES/(STEM+'_tail_0001.json.gz')
    summary_path = NOTES/(STEM+'-summary.json')
    reproduction_path = NOTES/(STEM+'-reproduction.json')
    config_path = NOTES/(STEM+'-config.json')
    trace_path = NOTES/(STEM+'-trace.jsonl')
    trials_path = NOTES/(STEM+'-trials.jsonl')
    launch, observed, root_audit = map(read, (launch_path, observed_path, root_audit_path))
    assert observed['status'] == 'observed-process-completed'
    assert observed['observer'] == '/root' and observed['session_id'] == 18291
    assert type(observed['actual_exit_code']) is int and observed['actual_exit_code'] == 0
    assert observed['converged'] is False
    for row in launch['bound_files'] + observed['files'] + root_audit['files']:
        file = Path(row['path'])
        assert file.stat().st_size == row['bytes'] and sha(file) == row['sha256']
    assert len(launch['bound_files']) == 61
    record, summary, reproduction, config = map(read,
        (response_path, summary_path, reproduction_path, config_path))
    assert sha(response_path) == '7a5f0b57fabdd58000905d61644513a292ab5f7d6b8fe7ee0fc0375866301442'
    assert summary['response_record_sha256'] == sha(response_path)
    assert summary['actual_worker_exit_code'] == 0
    assert summary['converged'] is False
    # The original client deliberately raises after saving a nonconverged
    # response; the original runner catches that exception and exits normally.
    assert isinstance(summary['error'], str)
    assert summary['error'].startswith('FloatingPointError("Weighted finite DN trial failed ')
    assert not summary['response_failed']
    assert canonical(reproduction['command']) == canonical(launch['command'])
    assert reproduction['script_sha256'] == sha(HERE/'db6f-prefix-tail-trial-run.py')
    assert reproduction['client_sha256'] == sha(HERE/'db6f-prefix-tail-trial-client.py')
    for prefix in ('input_config', 'input_checkpoint', 'diagnostic_config', 'source_map'):
        assert sha(reproduction[prefix]) == reproduction[prefix+'_sha256']
    assert canonical(record['config']) == canonical(config) == canonical(read(reproduction['input_config']))
    assert config['correctInitialBoundary'] is False and config['maxIterations'] == 8
    assert config['solveTolerance'] == 2e-9
    seed = checkpoint(read(reproduction['input_checkpoint']))
    response, request = record['response'], record['request']
    state = checkpoint(record)
    assert response['converged'] is False and not response.get('failed')
    assert response['audit'] is None
    assert request['jacobian'] is True and request['audit'] is False
    assert canonical({key: request[key] for key in ('jacobian', 'audit')}) == canonical(reproduction['request'])
    assert canonical(request['height']) == canonical(seed['cutHeight']) == canonical(state['cutHeight'])
    assert len(request['height']) == 15 and all(number(x) and x != 0 for x in request['height'])
    target = read(NOTES/'2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz')['predicted_cut_height']
    assert request['height'] == [math.ldexp(x, -2*(j+1)) for j, x in enumerate(target)]
    assert all(number(x) and x == 0 for row in seed['states'] for x in row)
    assert len(state['states']) == 865 and len(state['rawStates']) == 13
    assert all(len(row) == 30 and all(number(x) for x in row) for row in state['states'])
    assert state['rawStates'] == [state['states'][n] for n in state['rawNode']]
    assert state['parameters']['projectionFloor'] == .05
    expected_sources = {'db6f-prefix-tail-trial-client.py', 'db6f-prefix-tail-trial-worker.mjs',
        'db6f-prefix-tail-trial-core.mjs', 'db6f-prefix-tail-trial-split.mjs',
        '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
        'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs'}
    assert set(record['source_sha256']) == expected_sources
    for name, digest in record['source_sha256'].items():
        assert sha(HERE/name) == digest
    trace = [json.loads(line) for line in trace_path.read_text().splitlines() if line]
    trials = [json.loads(line) for line in trials_path.read_text().splitlines() if line]
    history = response['history']
    assert len(history) == 8 and [row['iteration'] for row in history] == list(range(8))
    bases = [row for row in trace if row.get('event') == 'iteration' and 'phase' not in row]
    corrections = [row for row in trace if row.get('event') == 'iteration' and row.get('phase') == 'correction']
    assert len(bases) == len(corrections) == 8
    assert [row['norm'] for row in bases] == [row['norm'] for row in history]
    assert all(b['minA'] == h['minA'] and b['minD'] == h['minD'] for b, h in zip(bases, history))
    assert history[0]['norm'] == history[0]['minA'] == history[0]['minD'] == 1
    accepted = [row for row in trials if row['kind'] == 'accepted']
    rejected = [row for row in trials if row['kind'] == 'residual-not-decreasing']
    assert len(trials) == 66 and len(accepted) == 8 and len(rejected) == 58
    assert [row['iteration'] for row in accepted] == list(range(8))
    assert all(number(row['trialNorm']) and row['trialNorm'] >= row['baseNorm'] for row in rejected)
    for i, row in enumerate(accepted):
        assert row['baseNorm'] == history[i]['norm']
        assert row['trialNorm'] < row['baseNorm']
        assert row['step'] == history[i]['step'] == 2**(-row['trial'])
        if i < 7:
            assert row['trialNorm'] == history[i+1]['norm']
    final = response['residual']
    assert final == summary['residual'] == accepted[-1]['trialNorm'] == .9163518748162202
    assert final > config['solveTolerance']
    completed = [row for row in trace if row.get('event') == 'response']
    assert len(completed) == 1 and completed[0]['converged'] is False and completed[0]['residual'] == final
    assert root_audit['final_residual'] == final and root_audit['converged'] is False
    assert root_audit['trial_records'] == 66 and root_audit['accepted_updates'] == 8
    files = [Path(__file__), launch_path, observed_path, root_audit_path, response_path,
             summary_path, reproduction_path, config_path, trace_path, trials_path]
    report = dict(status='INDEPENDENT_CLOSED_ZERO_PILOT_EVIDENCE_CHECK_PASS_UNSOLVED',
        script_sha256=sha(__file__), observer_of_process_exit='/root', root_observed_session=18291,
        root_observed_tool_exit_code=0, saved_worker_exit_code=0, reviewer='/root/tail_theory',
        saved_client_nonconvergence_exception=summary['error'],
        new_solver_calls=0, physical_equations_or_tolerance_changed=False,
        original_solve_tolerance=config['solveTolerance'], converged=False,
        launch_bindings_rehashed=61, direct_response_sources_rehashed=8,
        history_base_evaluations=8, correction_trace_records=8,
        accepted_updates=8, trial_records=66, residual_rejections=58,
        initial_residual=history[0]['norm'], final_residual=final,
        initial_min_A=history[0]['minA'], initial_min_D=history[0]['minD'],
        last_saved_base_min_A=history[-1]['minA'], last_saved_base_min_D=history[-1]['minD'],
        accepted_steps=[row['step'] for row in accepted],
        history_norms=[row['norm'] for row in history],
        final_residual_is_last_accepted_norm_not_last_history_base=True,
        state_counts=dict(staged_nodes=865, shape_slots=30, raw_nodes=13),
        all_saved_shape_states_finite=True, exact_nonzero_quarter_target=True,
        explicit_zero_shape_seed=True, correctInitialBoundary=False,
        bound_files=[bind(p) for p in files],
        scope='Read-only independent file and log cross-check. The root observer, not this reviewer, observed process exit. Eight iterations were insufficient for the original tolerance; no claim of nonexistence or failure of eventual convergence is made. This failed response is not a successful continuation warm or a complete surface.')
    with args.out.open('x') as handle:
        json.dump(report, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps(dict(status=report['status'], final_residual=final, converged=False,
        trial_records=66, accepted_updates=8, new_solver_calls=0, output_sha256=sha(args.out))))


if __name__ == '__main__':
    main()
