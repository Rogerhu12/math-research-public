#!/usr/bin/env python3
"""Pass only the predeclared node-86 negative-neighbor pair to the original worker.

This independent entry permits exactly [(86, 8), (86, 11)] and checks each
binary64 step with math.nextafter. It does not generalize the old one-item entry.

This is a single native request with the complete original physical height,
Jacobian and audit enabled. Only initializer and trace paths change. Neither
a candidate residual nor an external record can supply an accepted response.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from recovering_tail_client_v2 import (sha, payload_sha, read_gzip, write_new_json,
    exact_equal, check_original_reload_boundary, validate_parameter_io_mapping)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--failure', type=Path, required=True)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--candidate-summary', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--sparse-helper', type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=3072)
    args = parser.parse_args()
    topic = args.source_topic.resolve()
    failure, candidate_file = args.failure.resolve(), args.candidate.resolve()
    prefix = args.out_prefix.resolve();prefix.parent.mkdir(parents=True, exist_ok=True)
    summary_file = prefix.with_name(prefix.name+'-summary.json')
    entry_file = prefix.with_name(prefix.name+'-entry.json')
    config_file = prefix.with_name(prefix.name+'-config.json')
    trace_file = prefix.with_name(prefix.name+'-worker.jsonl')
    if any(file.exists() for file in (summary_file, entry_file, config_file, trace_file)):
        raise FileExistsError('Use a fresh original-worker output prefix')
    original, candidate = read_gzip(failure), read_gzip(candidate_file)
    if sha(failure) != 'adf477252c1dc707ce4fe8975aa9c911aca2f9d4c5113ba300d11b82023c4535':
        raise ValueError('Only the predeclared H_old failed state is eligible')
    # The original worker serializes failed as its error string, not a boolean.
    # The complete failed record is separately pinned above by its SHA-256.
    if (original['response'].get('failed') !=
            'Error: multiple-shooting line search failed at 3.671459625080514e-9' or
            original['response']['lastIteration']['norm'] != 3.671459625080514e-9):
        raise ValueError('The exact original failed response is required')
    check = json.loads(args.candidate_summary.read_text())
    if (candidate.get('solver_success') is not False or candidate.get('candidate_only') is not True or
            check['original_solver_invoked'] is not False or
            check['input']['sha256'] != sha(failure) or
            check['candidate']['sha256'] != sha(candidate_file) or
            candidate['input_failure_sha256'] != sha(failure) or
            check['changed_scalars'] != 2 or
            not exact_equal(check['named_changes'], candidate['named_changes']) or
            not check['strict_full_replay_improvement'] or not candidate['strict_full_replay_improvement'] or
            not check['full_candidate_replay']['norm'] < check['before']['norm']):
        raise ValueError('A strictly improved, source-bound candidate-only record is required')
    if (not exact_equal(candidate['request'], original['request']) or
            not exact_equal(candidate['config'], original['config']) or
            not exact_equal(candidate['source_sha256'], original['source_sha256'])):
        raise ValueError('The candidate changed the original request, configuration or sources')
    cp, old = candidate['checkpoint'], original['response']['checkpoint']
    for key in ('parameters', 'rawNode', 'cutHeight'):
        if not exact_equal(cp[key], old[key]):
            raise ValueError('The candidate changed a same-grid identity: '+key)
    changes = check['named_changes'];found=[]
    if [(c['node'], c['component']) for c in changes] != [(86, 8), (86, 11)]:
        raise ValueError('Only the two predeclared components are eligible')
    for change in changes:
        if (change['direction'] != -1 or
                not math.isfinite(change['before']) or not math.isfinite(change['after']) or
                not exact_equal(math.nextafter(change['before'], -math.inf), change['after']) or
                not exact_equal(change['signed_step'], change['after']-change['before'])):
            raise ValueError('Each prescribed change must be exactly the negative binary64 neighbor')
    if len(cp['states']) != len(old['states']):
        raise ValueError('Candidate grid changed')
    for i, (left, right) in enumerate(zip(old['states'], cp['states'])):
        if len(left) != len(right):
            raise ValueError('Candidate state dimension changed')
        for j, (a, b) in enumerate(zip(left, right)):
            if not exact_equal(a, b):found.append((i, j, a, b))
    expected = [(c['node'], c['component'], c['before'], c['after']) for c in changes]
    if not exact_equal(found, expected):
        raise ValueError('This one-shot entry permits exactly the two named scalar changes')
    if not exact_equal(cp['rawStates'], [cp['states'][i] for i in cp['rawNode']]):
        raise ValueError('The candidate raw-node copy differs from its complete states')
    sources = dict(check['source_sha256'])
    for name, digest in original['source_sha256'].items():
        file = topic/'scripts'/name
        if sha(file) != digest:
            raise ValueError('An original native source changed: '+name)
        sources[str(file)] = digest
    sources[str(Path(__file__).resolve())] = sha(__file__)
    sources[str(Path(__file__).with_name('recovering_tail_client_v2.py').resolve())] = sha(
        Path(__file__).with_name('recovering_tail_client_v2.py'))
    sparse = args.sparse_helper.resolve();sources[str(sparse)] = sha(sparse)
    for file, digest in sources.items():
        if sha(file) != digest:raise ValueError('Execution source changed: '+file)
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER'] = str(sparse)
    cfg = copy.deepcopy(original['config'])
    if cfg.get('designInitialCheckpoint') or cfg.get('secantCheckpoint'):
        raise ValueError('This same-state entry requires an exclusive initializer')
    cfg['initialCheckpoint'] = str(candidate_file);cfg['traceFile'] = str(trace_file)
    changes = sorted(k for k in set(cfg)|set(original['config']) if cfg.get(k) != original['config'].get(k))
    if set(changes)-{'initialCheckpoint', 'traceFile'}:
        raise AssertionError('Only initializer and trace paths may change')
    if (cfg['solveTolerance'] != 2e-9 or cfg.get('sharedEngines') or cfg['spacing'] != 3 or
            cfg['modes'] != 8 or cfg['shootingParts'] != 16 or cfg['steps'] != 16):
        raise ValueError('Original nonshared m3 worker gate required')
    write_new_json(config_file, cfg)
    entry = dict(scope=__doc__, command=[sys.executable, *sys.argv],
        failure=dict(path=str(failure), sha256=sha(failure)),
        candidate=dict(path=str(candidate_file), sha256=sha(candidate_file)),
        candidate_summary=dict(path=str(args.candidate_summary.resolve()), sha256=sha(args.candidate_summary)),
        source_sha256=sources, configuration=dict(path=str(config_file), sha256=sha(config_file)),
        configuration_changed_keys=changes, physical_request=old['cutHeight'],
        same_shooting_parts=cfg['shootingParts'], original_gate=cfg['solveTolerance'],
        candidate_only_full_replay=check['full_candidate_replay']['norm'],
        named_changes=check['named_changes'],
        changed_scalars=2, explicit_coordinate_allowlist=[[86, 8], [86, 11]],
        requested_jacobian=True, requested_audit=True, node_heap_resource_only=args.node_heap)
    write_new_json(entry_file, entry)
    file = topic/'scripts/950f-tail-client-v3.py'
    spec = importlib.util.spec_from_file_location('unchanged_candidate_native_client', file)
    native = importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    tail = None;began = time.monotonic()
    result = dict(scope=__doc__, entry=dict(path=str(entry_file), sha256=sha(entry_file)),
                  solver_success=False, prefix_solver_invoked=False)
    print(json.dumps(dict(event='original_candidate_native_entry', entry=str(entry_file),
                         sha256=sha(entry_file))), flush=True)
    try:
        tail = native.WeightedTailPort(config_file, topic/'repro/source-root',
            prefix.with_name(prefix.name+'_tail'), node_heap=args.node_heap)
        result['ready_parameter_metadata_transition'] = validate_parameter_io_mapping(
            cp['parameters'], tail.ready['parameters'], original['config'], cfg)
        result['reload_arithmetic'] = check_original_reload_boundary(
            candidate_file, old['cutHeight'], tail.cut['radius'])
        result['ready_payload_sha256'] = payload_sha(tail.ready)
        response = tail.solve(np.asarray(old['cutHeight'], float), jacobian=True, audit=True)
        J = np.asarray(response['heightJetJacobian'], float)
        if (response.get('converged') is not True or not response['residual'] < cfg['solveTolerance'] or
                J.size != (3*cfg['modes']+2)*cfg['modes'] or not np.all(np.isfinite(J)) or
                response.get('audit') is None):
            raise ValueError('The original worker did not return the required original-gate/Jacobian/audit result')
        result.update(solver_success=True, original_residual=response['residual'],
            finite_jacobian_entries=int(J.size), audit_returned=True,
            final_state_nodes=len(response['checkpoint']['states']),
            native_iterations=len(response['history']))
    except Exception as error:
        result['error'] = repr(error)
    finally:
        if tail is not None:
            try:
                result['native_calls'] = tail.calls
                file = tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
                if file.is_file():
                    saved = read_gzip(file)
                    if not exact_equal(saved['request'], dict(height=old['cutHeight'], jacobian=True, audit=True)):
                        raise AssertionError('Native response belongs to a different physical request')
                    if not exact_equal(saved['config'], cfg):
                        raise AssertionError('Native response belongs to a different configuration')
                    result['native_record'] = dict(path=str(file), sha256=sha(file))
                    if saved['response'].get('lastIteration'):
                        result['last_iteration'] = saved['response']['lastIteration']
            finally:
                tail.close()
        for file, digest in sources.items():
            if sha(file) != digest:raise AssertionError('Executed source changed: '+file)
        result['seconds'] = time.monotonic()-began
        write_new_json(summary_file, result)
        print(json.dumps(dict(event='original_candidate_native_terminal', **result)), flush=True)
    if not result['solver_success']:raise SystemExit(2)


if __name__ == '__main__':
    main()
