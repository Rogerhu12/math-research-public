#!/usr/bin/env python3
"""Pure input preparation for ONE closed H0->H1 control pilot; never starts DN.

Keeps the frozen matched-cut physical/numerical config except its five I/O
paths. The target is the original second real request, not a manufactured
success. The first real successful packet is only a bootstrap warm source.
"""
import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
REPO = TOPIC.parents[1]
STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01'
ADAPTER = HERE / 'db6f-prefix-tail-linear-continuation-client.py'
WRAPPER = HERE / 'db6f-prefix-flat-linear-continuation-coupled.py'


def load_helpers():
    # Importing the adapter only defines functions/classes; no original port
    # or engine is constructed by this pure preparer.
    spec = importlib.util.spec_from_file_location('db6f_linear_control_helpers', ADAPTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write_json(path, data):
    encoded = (json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    if len(encoded) >= 100000:
        raise ValueError('Prepared metadata exceeds the small-file limit')
    with path.open('xb') as f:
        f.write(encoded)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-prefix', type=Path, required=True)
    a = ap.parse_args()
    h = load_helpers()
    out = a.out_prefix.resolve()
    h.require(out.parent == NOTES.resolve() and not list(out.parent.glob(out.name + '*')),
              'Use a completely new stem inside this topic notes directory')
    original_bindings = NOTES / (STEM + '-input-bindings.json')
    original = h.read(original_bindings)
    h.require(len(original['bound_files']) == 121, 'Wrong original matched-cut binding closure')
    rows = {row['path']: h.verify(row) for row in original['bound_files']}
    observation_path = NOTES / '2026-11-09-db6f-root-matched-cut-observed-execution-01.json'
    h.require(h.identity(observation_path)['sha256'] == '1f7a7290c5c65a9f73531cd0edddf8f15b0290477be7d0b74eff9a3d5ba57334',
              'Wrong actual matched-cut closure observation')
    observation = h.read(observation_path)
    h.require(observation['status'] == 'observed-process-completed' and observation['observer'] == '/root'
              and observation['session_id'] == 5817 and observation['tool_receipt'] == 'ff466f'
              and observation['actual_exit_code'] == 0 and observation['mathematical_success'] is False,
              'Original matched-cut failure identity changed')
    for row in observation['files']:
        rows[row['path']] = h.verify(row)
    seed_path, target_path = [NOTES / (STEM + f'_tail_{i:04d}.json.gz') for i in (1, 2)]
    seed, target = h.read(seed_path), h.read(target_path)
    h.require(h.identity(seed_path)['sha256'] == '6f4de10c22fc05cedc87994c274c3643b5390add7bfe0ca71001e02a440a7a86'
              and h.identity(target_path)['sha256'] == '44088a6fce132438771fb83267754f32e8d12043379b8f83c1977eccaad0d1de',
              'Wrong closed first/second actual packets')
    h.require(h.canonical(seed['config']) == h.canonical(target['config'])
              and h.canonical(seed['source_sha256']) == h.canonical(target['source_sha256']),
              'Closed packets do not use the same typed original problem')
    h.require(set(target['response']) == {'failed', 'lastIteration', 'checkpoint'}
              and target['response']['failed'] == 'Error: multiple-shooting line search failed at 2489.354194334243',
              'Target source must remain the actual FAILED packet')
    h.require(seed['response']['converged'] is True, 'Bootstrap must be a closed true successful DN')
    M = seed['config']['modes']
    h.validate_response(seed['response'], M, seed['response']['checkpoint']['parameters'],
                        seed['config']['solveTolerance'], True, False)
    for packet in (seed, target):
        h.require(packet['request']['jacobian'] is True and packet['request']['audit'] is False
                  and h.vector(packet['request']['height'], M), 'Wrong closed physical target/flags')
    h.require(h.same_height(seed['request']['height'], seed['response']['checkpoint']['cutHeight']),
              'Bootstrap physical cut label mismatch')
    command = original['command']
    source_root = Path(command[command.index('--source-root') + 1]).resolve()
    node_heap = int(command[command.index('--node-heap') + 1])
    cfg = dict(seed['config'])
    cfg.update(initialCheckpoint=str(seed_path), traceFile=str(out) + '-tail-trace.jsonl',
               iterationCheckpointFile=str(out) + '-iteration.json.gz',
               trialDiagnosticFile=str(out) + '-tail-trials.jsonl', trialStatePrefix=str(out) + '-trial-stage')
    changed = sorted(k for k in set(cfg) | set(seed['config'])
                     if h.canonical(cfg.get(k)) != h.canonical(seed['config'].get(k)))
    h.require(set(changed) == h.IO_KEYS and h.canonical(h.without_io(cfg)) == h.canonical(h.without_io(seed['config'])),
              'Preparation changed a field outside the five I/O paths')
    config_path = Path(str(out) + '-tail-config.json')
    record_prefix = Path(str(out) + '_tail')
    policy_path = record_prefix.with_name(record_prefix.name + '-continuation-policy.json')
    launch_path = Path(str(out) + '-launch.json')
    report_path = Path(str(out) + '-preparation.json')
    direct = [original_bindings, observation_path, seed_path, target_path, ADAPTER, WRAPPER, Path(__file__),
              NOTES / '2026-11-09-db6f-prefix-matched-cut-linear-dn-continuation-plan-v2.md',
              NOTES / '2026-11-09-db6f-prefix-matched-cut-linear-dn-continuation-v2-sources.json']
    for p in direct:
        row = h.identity(p)
        rows[row['path']] = row
    sources = {n: h.identity(HERE / n)['sha256'] for n in h.ORIGINAL_NAMES + [ADAPTER.name]}
    h.require(h.canonical(seed['source_sha256']) == h.canonical({n: sources[n] for n in h.ORIGINAL_NAMES}),
              'Original eight sources changed')
    # All validation above precedes the first write. No future true response or
    # success packet is generated here.
    write_json(config_path, cfg)
    rows[str(config_path)] = h.identity(config_path)
    policy = {'schema': 'db6f-physical-height-continuation-v1', 'status': 'PREPARED_ONLY_NO_DN',
              'scope': 'Same physical/numerical DN; bounded intermediate physical cut heights only.',
              'record_prefix': str(record_prefix), 'source_root': str(source_root),
              'config': h.identity(config_path), 'bootstrap_packet': h.identity(seed_path),
              'control': h.CONTROL, 'source_sha256': sources,
              'journal_file': str(out) + '-continuation-journal.jsonl',
              'last_good_file': str(out) + '-last-good.json',
              'bindings': sorted(rows.values(), key=lambda r: r['path'])}
    write_json(policy_path, policy)
    rows[str(policy_path)] = h.identity(policy_path)
    launch = {'schema': 'db6f-linear-dn-closed-request-pilot-v1', 'status': 'PREPARED_NOT_STARTED',
              'scope': 'Exactly one external request equal to the closed matched-cut H1/Jac=true/audit=false. Prefix remains UNSOLVED.',
              'config': h.identity(config_path), 'policy': h.identity(policy_path),
              'source_root': str(source_root), 'record_prefix': str(record_prefix), 'node_heap': node_heap,
              'target_packet': h.identity(target_path), 'bootstrap_packet': h.identity(seed_path),
              'summary_file': str(out) + '-summary.json', 'stdout_log': str(out) + '-run.log',
              'cwd': str(REPO), 'command': [sys.executable, str(ADAPTER), '--pilot-launch', str(launch_path)],
              'bindings': sorted(rows.values(), key=lambda r: r['path'])}
    write_json(launch_path, launch)
    report = {'status': 'PREPARED_ONLY_NO_DN_NO_BVP', 'scope': __doc__,
              'original_matched_bindings': h.identity(original_bindings),
              'actual_original_failure_observation': h.identity(observation_path),
              'bootstrap_packet': h.identity(seed_path), 'target_packet': h.identity(target_path),
              'source_sha256': sources, 'changed_config_keys': changed,
              'same_non_io_typed_config': True, 'original_source_count': 8, 'new_actual_source_count': 9,
              'policy_binding_count': len(policy['bindings']), 'launch_binding_count': len(launch['bindings']),
              'exact_target_is_original_second_request': True, 'target_flags': {'jacobian': True, 'audit': False},
              'new_prefix_status': 'UNSOLVED', 'actual_dn_calls': 0, 'actual_root_flow_bvp_calls': 0,
              'prepared_files': [h.identity(p) for p in (config_path, policy_path, launch_path)],
              'future_coupled_interface': {'wrapper': h.identity(WRAPPER),
                  'scope': 'The wrapper is frozen for later review/use; this preparer emits no coupled launch. A later coupled run needs a new unused stem and a separately bound five-I/O config/policy.'}}
    write_json(report_path, report)
    print(json.dumps({'status': report['status'], 'launch': h.identity(launch_path),
                      'preparation': h.identity(report_path), 'policy': h.identity(policy_path)}, indent=2))


if __name__ == '__main__':
    main()
