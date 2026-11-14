#!/usr/bin/env python3
"""Read-only closed-call provenance audit; no worker or active journal access."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    repo = topic.parents[1]
    notes = topic / 'notes'
    pre = '2026-11-09-db6f-'
    stem = pre + 'prefix-flat-v17v18-m15-amplitude-continuation-03'

    def identity(path):
        path = Path(path).resolve()
        data = path.read_bytes()
        return {'path': str(path.relative_to(repo)), 'bytes': len(data),
                'sha256': hashlib.sha256(data).hexdigest()}

    launch_path = notes / (pre + 'prefix-amplitude-resume03-launch.json')
    launch = read(launch_path)
    for row in launch['bound_files']:
        path = Path(row['path'])
        current = identity(path if path.is_absolute() else repo / path)
        assert current['sha256'] == row['sha256'] and current['bytes'] == row['bytes']
    binding_path = notes / (stem + '-input-bindings.json')
    binding = read(binding_path)
    config_path = notes / (stem + '-config.json')
    config = read(config_path)
    assert config['maxIterations'] == 36 and config['solveTolerance'] == 2e-9
    goal = np.asarray(binding['target_height'], dtype=float)
    assert goal.shape == (15,) and np.all(np.isfinite(goal))
    rows = []
    files = [identity(p) for p in (launch_path, binding_path, config_path)]
    cases = [
        (7, 2019/2048, '352afd42a85af071b369b4987558854b0ed37ccc5173e26faca504251e4740aa'),
        (8, 4037/4096, '396cdd758e7b38cfd7d06ae7595210685bf2d9d9ef90e2fa157bafff087f93cf'),
    ]
    scalar_keys = {'radius','backgroundSlope','backgroundSecond','E','Ep','meanSlope',
                   'meanSecond','meanSlopeCorrection','meanSecondCorrection','minLeading',
                   'minD','endpointFullD','endpointPhi','formalCurvature'}
    for call, scale, digest in cases:
        path = notes / f'{stem}_tail_{call:04d}.json.gz'
        row = identity(path)
        assert row['sha256'] == digest
        packet = read(path)
        assert packet['config'] == config
        request, response = packet['request'], packet['response']
        assert request['jacobian'] is False and request['audit'] is False
        expected = goal * np.float64(scale) ** np.arange(1, 16)
        cp = response['checkpoint']
        assert np.array_equal(np.asarray(request['height']), expected)
        assert np.array_equal(np.asarray(cp['cutHeight']), expected)
        assert np.asarray(cp['states']).shape == (865, 30)
        assert np.asarray(cp['rawStates']).shape == (13, 30)
        for name in ('states','rawStates','rawNode','cutHeight'):
            assert np.all(np.isfinite(np.asarray(cp[name], float)))
        assert len(packet['source_sha256']) == 8
        for name, sha in packet['source_sha256'].items():
            assert any(Path(v['path']).name == name and v['sha256'] == sha
                       for v in launch['bound_files'])
        if call == 7:
            assert set(response) == {'failed','lastIteration','checkpoint'}
            last = response['lastIteration']
            assert last['iteration'] == 6 and last['norm'] == 0.020004151516050995
            item = {'call': call, 'scale': scale, 'status': 'ORIGINAL_LINE_SEARCH_FAILURE',
                    'last_iteration': last}
        else:
            assert response['converged'] is True
            assert response['residual'] == 1.251822050474137e-9
            assert response['residual'] < config['solveTolerance']
            assert response['heightJetJacobian'] is None and response['audit'] is None
            jets = response['jets']
            assert set(jets) == scalar_keys | {'height','slope','second'}
            assert all(np.isfinite(jets[k]) for k in scalar_keys)
            assert all(np.asarray(jets[k]).shape == (15,) and np.all(np.isfinite(jets[k]))
                       for k in ('height','slope','second'))
            assert len(response['history']) == 5
            assert all(np.isfinite(v['norm']) for v in response['history'])
            item = {'call': call, 'scale': scale, 'status': 'ACTUAL_FINITE_TAIL_WARM_SUCCESS',
                    'residual': response['residual'], 'history_length': 5,
                    'minLeading': jets['minLeading'], 'minD': jets['minD']}
        item.update(exact_request_and_checkpoint_height=True, source_count=8,
                    finite_state_shape=[865,30], finite_raw_shape=[13,30], packet=row)
        rows.append(item)
        files.append(row)
        for kind in ('trace','trials'):
            log = notes / f'{stem}-call{call:03d}-{kind}.jsonl'
            files.append(identity(log))
    # Rehash closed objects after reading; never infer active-process exit.
    for row in files:
        assert identity(repo / row['path']) == row
    report = {'status': 'CLOSED_CALLS_007_008_AUDITED', 'calls': rows,
              'source_bindings_verified': len(launch['bound_files']),
              'original_config_unchanged': True, 'closed_files': files,
              'source_script': identity(__file__), 'solver_calls': 0,
              'active_progress_or_journal_read': False, 'controller_exit_observed': False,
              'scope': 'One closed failure and one true intermediate warm success; no s=1, final Jacobian/audit, prefix, geometry or G5 completion.'}
    with args.out.open('x') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps({'status': report['status'], 'sources': report['source_bindings_verified'],
                      'calls': [{k:v for k,v in row.items() if k in ('call','scale','status','residual','minLeading','minD')}
                                for row in rows], 'report': identity(args.out)}))


if __name__ == '__main__':
    main()
