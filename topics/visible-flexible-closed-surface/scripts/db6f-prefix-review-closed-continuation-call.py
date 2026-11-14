#!/usr/bin/env python3
"""Independent metadata supplements for frozen continuation02 call001 only.

No numerical engine or solver is imported or executed. Compare the already
completed original-auditor replay, then explicitly link launch selectors,
the exact response source set, and raw/full checkpoint snapshots.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def bind(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    author_path = NOTES / '2026-11-09-db6f-root-continuation02-call001-closed-audit.json'
    replay_path = NOTES / '2026-11-09-db6f-prefix-review-continuation02-call001-metadata-replay.json'
    author, replay = read(author_path), read(replay_path)
    if author_path.read_bytes() != replay_path.read_bytes() or author != replay:
        raise ValueError('Original-auditor independent replay differs')
    launch_path = NOTES / '2026-11-09-db6f-prefix-amplitude-resume02-launch.json'
    launch = read(launch_path)
    command = launch['command']
    stem = Path(launch['out_prefix'])
    binding_path = Path(str(stem)+'-input-bindings.json')
    binding = read(binding_path)
    links = {}
    for flag, key in [('--config', 'original_config'), ('--target-prefix', 'target_prefix'),
                      ('--resume-checkpoint', 'resume_record')]:
        from_launch = Path(command[command.index(flag)+1]).resolve()
        from_controller = Path(binding[key]).resolve()
        if from_launch != from_controller:
            raise ValueError('Runtime selector is not the frozen launch input: '+key)
        links[key] = bind(from_launch)
    controller_path = Path(command[1])
    client_path = HERE / 'db6f-prefix-tail-continuation-client.py'
    if bind(controller_path)['sha256'] != binding['script_sha256']:
        raise ValueError('Controller source identity differs')
    if bind(client_path)['sha256'] != binding['client_sha256']:
        raise ValueError('Client source identity differs')
    record_path = Path(author['closed_row']['response_record'])
    record = read(record_path)
    response = record['response']
    cp = response['checkpoint']
    params = cp['parameters']
    sources = {'db6f-prefix-tail-continuation-client.py', 'db6f-prefix-tail-trial-worker.mjs',
               'db6f-prefix-tail-trial-core.mjs', 'db6f-prefix-tail-trial-split.mjs',
               '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
               'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs'}
    if set(record['source_sha256']) != sources:
        raise ValueError('The complete eight-source response set is not present')
    for name, digest in record['source_sha256'].items():
        if bind(HERE/name)['sha256'] != digest:
            raise ValueError('Source digest mismatch: '+name)
    M = params['modes']
    if len(cp['states']) != params['depth']+1:
        raise ValueError('Stage-state count differs from resolved stage depth')
    if not all(len(row) == 2*M and all(math.isfinite(v) for v in row) for row in cp['states']):
        raise ValueError('Invalid full-state shape/value')
    raw = cp['rawNode']
    if len(raw) != params['physicalDepth']+1 or len(raw) != len(cp['rawStates']):
        raise ValueError('Raw-node count differs from physical depth')
    if raw != sorted(set(raw)) or raw[0] != 0 or raw[-1] != params['depth']:
        raise ValueError('Raw-node ordering or endpoint differs')
    if cp['rawStates'] != [cp['states'][i] for i in raw]:
        raise ValueError('Raw states do not equal the indexed full states')
    if response.get('failed') is not None or response['heightJetJacobian'] is not None or response['audit'] is not None:
        raise ValueError('Intermediate response has unexpected failure/Jacobian/audit metadata')
    core_path = HERE/'db6f-prefix-tail-trial-core.mjs'
    if 'projectionFloor=.05' not in core_path.read_text() or params['projectionFloor'] != .05:
        raise ValueError('Reviewed default guard or resolved checkpoint guard differs')
    files = {Path(__file__).resolve(), author_path, replay_path, launch_path, binding_path,
             controller_path, client_path, record_path, core_path}
    result = dict(verdict='PASS-closed-call001-metadata-supplements', scope=__doc__,
        original_auditor_replay_actual_exit_code=0, original_auditor_replay_bytes_equal=True,
        original_auditor_sha256=author['script']['sha256'],
        launch_selector_links=links, exact_eight_response_sources=True,
        stage_state_count=len(cp['states']), stage_depth=params['depth'],
        raw_state_count=len(raw), physical_depth=params['physicalDepth'],
        raw_state_index_identity=True, original_default_and_recorded_guard=.05,
        response_scope='True original converged finite-DN warm at s=.3125; no independent solver replay or final target/source audit.',
        numerical_solver_calls=0, bound_files=[bind(path) for path in sorted(files)])
    with args.output.open('x') as handle:
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps(dict(verdict=result['verdict'], shape_nodes=len(cp['states']),
                         raw_nodes=len(raw), numerical_solver_calls=0,
                         output=str(args.output), sha256=bind(args.output)['sha256'])))


if __name__ == '__main__':
    main()
