#!/usr/bin/env python3
"""Read-only audit of the closed sixth request, not of the active controller.

No solver, process observation, configuration mutation or acceptance of a new
trial. The immutable response and rotated logs identify the closed attempt.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np


def read(p):
    p = Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_text())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', required=True, type=Path)
    a = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    repo = topic.parents[1]
    n = topic / 'notes'
    pre = '2026-11-09-db6f-'
    stem = pre + 'prefix-flat-v17v18-m15-amplitude-continuation-03'

    def bind(p):
        p = Path(p)
        raw = p.read_bytes()
        return dict(path=str(p.relative_to(repo)), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())

    launchp = n / (pre + 'prefix-amplitude-resume03-launch.json')
    launch = read(launchp)
    for f in launch['bound_files']:
        p = Path(f['path'])
        p = p if p.is_absolute() else repo / p
        now = bind(p)
        assert now['sha256'] == f['sha256'] and now['bytes'] == f['bytes'], str(p)
    bindingp = n / (stem + '-input-bindings.json')
    binding = read(bindingp)
    responsep = n / (stem + '_tail_0006.json.gz')
    packet = read(responsep)
    response = packet['response']
    cp = response['checkpoint']
    assert bind(responsep)['sha256'] == 'fda5867be9b3e8f79c52f43e4678b60d05ef973b51070174b0cef85555263780'
    assert set(response) == {'failed', 'lastIteration', 'checkpoint'}
    assert response['lastIteration']['iteration'] == 3
    assert response['lastIteration']['norm'] == 0.23384170570383042
    goal = np.asarray(binding['target_height'], float)
    want = goal * np.float64(505 / 512) ** np.arange(1, 16)
    assert np.array_equal(np.asarray(packet['request']['height']), want)
    assert np.array_equal(np.asarray(cp['cutHeight']), want)
    assert packet['request']['jacobian'] is False and packet['request']['audit'] is False
    assert packet['config'] == read(n / (stem + '_tail_0005.json.gz'))['config'] == read(n / (stem + '-config.json'))
    assert packet['config']['maxIterations'] == 36 and packet['config']['solveTolerance'] == 2e-9
    for name, digest in packet['source_sha256'].items():
        choices = [f for f in launch['bound_files'] if Path(f['path']).name == name]
        assert any(f['sha256'] == digest for f in choices), name
    assert np.asarray(cp['states']).shape == (865, 30)
    assert np.asarray(cp['rawStates']).shape == (13, 30)
    for key in ['states', 'rawNode', 'rawStates', 'cutHeight']:
        assert np.all(np.isfinite(np.asarray(cp[key], float)))
    closed = [launchp, bindingp, n / (stem + '-config.json'), Path(binding['original_config']),
              Path(binding['target_prefix']), responsep]
    logs = []
    for kind, digest in [('trace', 'e07e32a684851ac742364468efd9134dd33bd17563d05c72a7d8d9df5bc5fcee'),
                         ('trials', 'a2531b5ecf96ee8e399114514daeeb2b1ddff9ddda6abc2f50e08e124fb9c540')]:
        p = n / (stem + '-call006-' + kind + '.jsonl')
        assert bind(p)['sha256'] == digest
        closed.append(p)
        logs.append(dict(kind=kind, rows=sum(1 for _ in p.open()),
                         scope='Closed cumulative diagnostic log; no per-call count inferred from total'))
    report = dict(status='CLOSED_ORIGINAL_MATHEMATICAL_LINE_SEARCH_FAILURE', call=6,
                  scale=505 / 512, step=1 / 1024, response_keys=sorted(response),
                  last_iteration=response['lastIteration'], source_bindings_verified=len(launch['bound_files']),
                  response_source_hashes_verified=len(packet['source_sha256']),
                  exact_request_and_checkpoint_target_equal=True, state_shape=[865, 30], raw_shape=[13, 30],
                  state_and_height_values_finite=True, unchanged_original_config=True,
                  closed_files=[bind(p) for p in closed], log_metadata=logs,
                  root_tool_controller_exit_observed=False, active_progress_or_logs_read=False,
                  source_script=bind(Path(__file__).resolve()),
                  scope='Closed failure provenance only: no new accepted trial, independent solve, nonexistence or controller-completion claim.')
    with a.out.open('x') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps(dict(status=report['status'], call=6, residual=response['lastIteration']['norm'],
                          sources_verified=len(launch['bound_files']), report=bind(a.out.resolve()))))


if __name__ == '__main__':
    main()
