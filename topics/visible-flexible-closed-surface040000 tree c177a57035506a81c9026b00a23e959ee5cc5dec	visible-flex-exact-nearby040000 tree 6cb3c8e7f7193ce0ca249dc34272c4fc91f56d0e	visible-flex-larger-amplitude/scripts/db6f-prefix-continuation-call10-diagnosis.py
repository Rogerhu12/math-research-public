#!/usr/bin/env python3
"""Read closed continuation calls 8/9/10; never import or run a solver.

The controller progress is read only to copy already closed attempt rows
and a labelled mutable status observation. No process exit is inferred.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
from pathlib import Path
import numpy as np

TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
STEM = TOPIC/'notes/2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02'
LAUNCH = TOPIC/'notes/2026-11-09-db6f-prefix-amplitude-resume02-launch.json'
IO_KEYS = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile',
           'trialStatePrefix', 'initialCheckpoint'}
SOURCE_NAMES = {'db6f-prefix-tail-continuation-client.py',
    'db6f-prefix-tail-trial-worker.mjs', 'db6f-prefix-tail-trial-core.mjs',
    'db6f-prefix-tail-trial-split.mjs', '950f-tail-subdivision.mjs',
    '950f-tail-warm-remesh.mjs', 'closing_weighted_tail.mjs',
    'closing_recalibrated_tail.mjs'}


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def locate(path):
    p = Path(path)
    if p.is_file():
        return p.resolve()
    for trial in (REPO/p, TOPIC/'notes'/p.name, TOPIC/'scripts'/p.name):
        if trial.is_file():
            return trial.resolve()
    raise FileNotFoundError(path)


def identity(path):
    p = locate(path)
    raw = p.read_bytes()
    return dict(path=str(p.relative_to(REPO)), bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest())


def checked(entry):
    actual = identity(entry.get('path', entry.get('file')))
    assert actual['sha256'] == entry['sha256']
    assert actual['bytes'] == entry['bytes']
    return actual


def load_rows(path, call):
    rows = [json.loads(line) for line in locate(path).read_bytes().splitlines()]
    return [row for row in rows if row.get('call') == call]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    assert not args.out.exists(), 'Use a fresh output; closed records are immutable.'
    launch = read(LAUNCH)
    assert Path(launch['out_prefix']).name == STEM.name
    bound = [checked(entry) for entry in launch['bound_files']]
    assert len(bound) == 66
    by_name = {}
    for entry in bound:
        by_name.setdefault(Path(entry['path']).name, set()).add(entry['sha256'])
    bp = Path(str(STEM)+'-input-bindings.json')
    cp = Path(str(STEM)+'-config.json')
    binding, cfg = read(bp), read(cp)
    assert identity(cp)['sha256'] == binding['config_sha256']
    original_path = locate(binding['original_config'])
    original = read(original_path)
    assert identity(original_path)['sha256'] == binding['original_config_sha256']
    different = {k for k in set(cfg) | set(original)
                 if (k in cfg) != (k in original) or cfg.get(k) != original.get(k)}
    assert different <= IO_KEYS
    assert (cfg['modes'], cfg['quadrature'], cfg['depth'], cfg['shootingParts'],
            cfg['steps'], cfg['maxIterations'], cfg['solveTolerance']) == (15, 256, 12, 8, 32, 36, 2e-9)
    assert cfg.get('projectionFloor', .05) == .05
    assert cfg.get('correctInitialBoundary') is not False
    target_path = locate(binding['target_prefix'])
    assert identity(target_path)['sha256'] == binding['target_prefix_sha256']
    target = read(target_path)
    assert target['config']['actual_nonlinear_tail'] is False
    goal = np.asarray(target['predicted_cut_height'], dtype=float)
    assert goal.shape == (15,) and np.isfinite(goal).all()
    assert binding['target_height'] == target['predicted_cut_height']
    for key, value in target['physical_tail_parameters'].items():
        assert cfg[key] == value
    progress_path = Path(str(STEM)+'-progress.json')
    progress = read(progress_path)
    closed = {row['call']: row for row in progress['attempts'] if row['call'] in (8, 9, 10)}
    assert set(closed) == {8, 9, 10}
    inputs = [identity(p) for p in (LAUNCH, bp, cp, original_path, target_path)]
    reports = []
    records = {}
    for call, scale in ((7, .6875), (8, .75), (9, .8125), (10, .875)):
        path = Path(str(STEM)+f'_tail_{call:04d}.json.gz')
        obj = read(path)
        records[call] = obj
        inputs.append(identity(path))
        assert obj['config'] == cfg
        assert set(obj['source_sha256']) == SOURCE_NAMES
        for name, digest in obj['source_sha256'].items():
            assert digest in by_name[name]
            assert identity(TOPIC/'scripts'/name)['sha256'] == digest
        expected = goal*np.float64(scale)**np.arange(1, 16)
        assert np.array_equal(np.asarray(obj['request']['height']), expected)
        assert obj['request']['jacobian'] is False and obj['request']['audit'] is False
        if call == 7:
            assert obj['response']['converged'] is True
            continue
        row, response = closed[call], obj['response']
        assert row['scale'] == scale and row['response_sha256'] == identity(path)['sha256']
        assert locate(row['response_record']) == path.resolve()
        state = response['checkpoint']
        array = np.asarray(state['states'], dtype=float)
        assert array.shape == (865, 30) and np.isfinite(array).all()
        assert np.array_equal(np.asarray(state['cutHeight']), expected)
        assert state['rawStates'] == [state['states'][i] for i in state['rawNode']]
        assert len(state['rawNode']) == 13
        for key, value in [('modes', 15), ('quadrature', 256), ('steps', 32),
                           ('physicalDepth', 12), ('shootingParts', 8), ('projectionFloor', .05)]:
            assert state['parameters'][key] == value
        logs = [checked(entry) for entry in row['logs']]
        assert len(logs) == 2
        inputs.extend(logs)
        trace_path = Path(str(STEM)+f'-call{call:03d}-trace.jsonl')
        trial_path = Path(str(STEM)+f'-call{call:03d}-trials.jsonl')
        trace = load_rows(trace_path, call)
        trials = load_rows(trial_path, call)
        base_rows = [r for r in trace if r.get('event') == 'iteration' and 'phase' not in r]
        requests = [r for r in trace if r.get('event') == 'request']
        assert len(requests) == 1 and requests[0]['height'] == obj['request']['height']
        if call < 10:
            assert row['converged'] is True and response['converged'] is True
            assert 0 <= response['residual'] < cfg['solveTolerance']
            assert response['history'][-1]['norm'] == response['residual'] == row['residual']
            assert len(base_rows) == len(response['history']) == row['iterations']
            assert all(r['kind'] == 'accepted' and r['step'] == 1 for r in trials)
        else:
            assert row['converged'] is False
            assert set(response) == {'failed', 'lastIteration', 'checkpoint'}
            assert 'multiple-shooting line search failed' in response['failed']
            assert response['lastIteration'] == row['last_iteration']
            assert response['lastIteration']['iteration'] == 3
            assert response['lastIteration']['norm'] == 4892.887571107566
            assert base_rows[-1]['norm'] == response['lastIteration']['norm']
            failures = [r for r in trace if r.get('event') == 'failure']
            assert len(failures) == 1 and failures[0]['error'] == response['failed']
        for r in trials:
            if 'stageInputFile' in r:
                item = identity(r['stageInputFile'])
                assert item['sha256'] == r['stageInputSHA256'] and item['bytes'] == r['stageInputBytes']
                stage = read(r['stageInputFile'])
                assert stage['stage'] == r['stage'] and stage['rawCell'] == r['rawCell'] and stage['rawSegment'] == r['rawSegment']
                assert stage['cutHeight'] == obj['request']['height']
                assert len(stage['inputState']) == 30 and all(math.isfinite(x) for x in stage['inputState'])
                inputs.append(item)
        iteration_summaries = []
        for r in base_rows:
            it = r['iteration']
            tests = [t for t in trials if t['iteration'] == it]
            iteration_summaries.append(dict(base=r, trial_count=len(tests),
                kind_counts=dict(Counter(t['kind'] for t in tests)),
                accepted=[{k:t[k] for k in ('trial','step','trialNorm')} for t in tests if t['kind']=='accepted'],
                rejected_stages=sorted({t['stage'] for t in tests if 'stage' in t}),
                rejected_raw_locations=sorted({(t['rawCell'],t['rawSegment']) for t in tests if 'stage' in t})))
        prev = records[call-1]
        new_h = np.asarray(obj['request']['height']); old_h = np.asarray(prev['request']['height'])
        ratio = float(new_h[0]/prev['response']['jets']['height'][0])
        delta_h = new_h-ratio*old_h
        warm = dict(all_higher_requested_modes_nonzero=bool(np.all(new_h[1:] != 0)),
                    harmonic_predictor_flag=cfg.get('harmonicAmplitudePredictor'),
                    actual_uniform_state_ratio=ratio,
                    maximum_physical_cut_linear_addition=float(np.max(np.abs(delta_h))),
                    addition_max_harmonic_number=int(np.argmax(np.abs(delta_h)))+1,
                    mode15_height_growth=float(new_h[-1]/old_h[-1]),
                    mode15_relative_boundary_addition=float(delta_h[-1]/new_h[-1]),
                    full_warm_state_or_flow_not_recomputed=True)
        assert warm['all_higher_requested_modes_nonzero']
        reports.append(dict(call=call,scale=scale,closed_row=row,
            actual_response_keys=list(response),
            response_converged_key_present='converged' in response,
            response_residual_key_present='residual' in response,
            original_failed_text=response.get('failed'),
            original_last_iteration=response.get('lastIteration'),
            finite_checkpoint_shape=list(array.shape),
            base_evaluation_count=len(base_rows),
            iterations=iteration_summaries,warm_comparison=warm,
            closed_failure_trace_time=next((r['time'] for r in trace if r.get('event')=='failure'),None)))
    assert progress['last_converged_scale'] >= .8125
    observation={k:progress.get(k) for k in ('status','current_attempt','current_requested_scale',
                 'current_step','last_converged_scale','target_reached','target_audited')}
    observation.update(source_file_is_mutable=True,
        observed_utc=datetime.now(timezone.utc).isoformat(),
        worker_exit_key_present='worker_exit_code' in progress,
        recorded_worker_exit_code=progress.get('worker_exit_code'),
        process_exit_inferred=False,
        original_failure_rule_next_scale=.8125+(.875-.8125)/2,
        original_failure_rule_next_step=(.875-.8125)/2)
    uniq={item['path']:item for item in inputs}
    report=dict(status='CLOSED_CALL10_FAILURE_AND_CALL8_9_METADATA_DIAGNOSIS',
        scope='Original closed records preserved. No new solver/root/flow/evaluation or geometric assertion.',
        producer=identity(__file__), launch_source_bindings=bound,
        launch_source_binding_count=len(bound), response_source_count_each=8,
        equation_configuration_unchanged=True, changed_io_keys=sorted(different),
        tolerance=cfg['solveTolerance'], projection_floor=.05,max_iterations=36,
        calls=reports, controller_observation=observation,
        closed_inputs=list(uniq.values()),
        original_response_schema_modified=False,
        solver_calls=0,angular_root_calls=0,rk_calls=0,backend_calls=0,
        unconverged_state_promoted_to_success=False,
        mathematical_nonexistence_asserted=False)
    args.out.write_text(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'],source_bindings=len(bound),
        closed_inputs=len(uniq),failed_call=10,last_norm=response['lastIteration']['norm'],
        observed_controller_scale=observation['current_requested_scale'],
        worker_exit_key_present=observation['worker_exit_key_present'])))


if __name__ == '__main__':
    main()
