#!/usr/bin/env python3
"""Resume a uniform finite-tail path with accepted-trial recovery recording.

An unconverged saved iteration is used only as an initial guess. First genuinely
solve its complete requested H, then solve the original complete target H with
the original acceptance and audit. Storage and shared-graph adapters are the
separately checked original-g implementation. No larger prefix or infinite
closure is claimed, and process failure is not treated as a nonlinear barrier.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time

import numpy as np


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prior-summary', type=Path, required=True)
    p.add_argument('--iteration', type=Path, required=True)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--node-heap', type=int, default=512)
    a = p.parse_args()
    started = time.time()
    prior = json.loads(a.prior_summary.read_text())
    iteration = json.loads(gzip.decompress(a.iteration.read_bytes()))
    if prior['homotopy'] != 'uniform' or iteration['status'] != 'iteration-recovery-only':
        raise ValueError('Require an interrupted uniform path and explicit recovery-only iteration')
    cfg = json.loads(Path(prior['config_file']).read_text())
    height = iteration['checkpoint']['cutHeight']
    base = np.zeros(cfg['modes'])
    base[:len(prior['full_prefix_target_height'])] = prior['full_prefix_target_height']
    multiplier = prior['external_height_multiplier']
    candidates = [row['attempted_scale'] for row in prior['rows'] if not row['success']]
    candidates.append(1.0)
    matching = [scale for scale in candidates
                if (base * (multiplier * scale)).tolist() == height]
    if len(set(matching)) != 1:
        raise ValueError('Cannot identify the exact saved complete physical boundary')
    resume_scale = matching[0]
    target = (base * multiplier).tolist()
    if target != prior['full_target_height']:
        raise AssertionError('Original target vector was not preserved exactly')
    file = lambda suffix: a.out_prefix.with_name(a.out_prefix.name + suffix)
    old_cfg = dict(cfg)
    cfg.update(initialCheckpoint=str(a.iteration.resolve()),
               traceFile=str(file('-trace.jsonl').resolve()),
               iterationCheckpointFile=str(file('-iteration.json.gz').resolve()),
               trialDiagnosticFile=str(file('-trials.jsonl').resolve()))
    changes = {key: [old_cfg.get(key), cfg.get(key)] for key in old_cfg.keys() | cfg.keys()
               if old_cfg.get(key) != cfg.get(key)}
    if set(changes) - {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile'}:
        raise AssertionError('A physical or numerical parameter changed during recovery')
    config_file = file('-config.json')
    with config_file.open('x') as stream:
        json.dump(cfg, stream, indent=2); stream.write('\n')
    report = {'scope': __doc__, 'prior_summary': str(a.prior_summary),
              'prior_summary_sha256': digest(a.prior_summary),
              'unconverged_initial_iteration': str(a.iteration),
              'unconverged_initial_iteration_sha256': digest(a.iteration),
              'initial_iteration_norm': iteration['iteration']['norm'],
              'complete_resume_height': height, 'complete_target_height': target,
              'resume_scale': resume_scale, 'external_height_multiplier': multiplier,
              'configuration_changes': changes,
              'all_physical_and_numerical_configuration_fields_unchanged': True,
              'config_file': str(config_file), 'node_heap_MiB': a.node_heap,
              'rows': [], 'external_boundary_target_reached': False,
              'coupled_prefix_or_infinite_closure': False,
              'script_sha256': digest(Path(__file__)),
              'accepted_trial_recording': 'recovery-only-before-full-variational-recheck-v1'}
    def save():
        report['seconds'] = time.time() - started
        file('-summary.json').write_text(json.dumps(report, indent=2) + '\n')
    save()
    module_path = Path(__file__).with_name('tail_resumable_client.py')
    spec = importlib.util.spec_from_file_location('resume_stored_tail', module_path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    tail = None
    try:
        tail = module.WeightedTailPort(config_file, a.source_topic / 'repro/source-root',
                                       file('-response'), node_heap=a.node_heap)
        common = prior['source_sha256'].keys() & tail.sources.keys()
        if any(prior['source_sha256'][k] != tail.sources[k] for k in common):
            raise AssertionError('A shared actual source changed during interruption recovery')
        report.update(ready=tail.ready, source_sha256=tail.sources,
                      common_source_file_count=len(common), common_source_hashes_equal=True)
        save()
        print(json.dumps({'event': 'ready', 'modes': cfg['modes'],
                          'resume_external_multiplier': multiplier * resume_scale,
                          'target_external_multiplier': multiplier}), flush=True)
        requests = ([(1.0, target, True)] if resume_scale == 1.0 else
                    [(resume_scale, height, False), (1.0, target, True)])
        for scale, vector, final in requests:
            request_start = time.time()
            response = tail.solve(vector, jacobian=final, audit=final)
            response_file = file(f'-response_{tail.calls:04d}.json.gz')
            row = {'success': True, 'scale': scale, 'external_multiplier': multiplier * scale,
                   'physical_height_max': max(map(abs, vector)),
                   'residual': response['residual'],
                   'iterations': len(response['history']),
                   'jets': response['jets'], 'audit': response.get('audit'),
                   'response_file': str(response_file), 'response_sha256': digest(response_file),
                   'seconds': time.time() - request_start}
            if row['audit']:
                row['original_profile_normalized_full_defect'] = (
                    cfg['shootingParts'] * row['audit']['normalizedFullDefect'])
            report['rows'].append(row)
            report['last_successful_response'] = str(response_file)
            if final:
                report['external_boundary_target_reached'] = True
            save()
            print(json.dumps({'event': 'success', 'external_multiplier': row['external_multiplier'],
                              'residual': row['residual'], 'audit': row['audit'],
                              'response_file': str(response_file), 'seconds': row['seconds']}), flush=True)
    except Exception as exc:
        report['error'] = repr(exc)
        if tail:
            report['worker_returncode_at_error'] = tail.proc.poll()
        print(json.dumps({'event': 'error', 'error': repr(exc),
                          'worker_returncode': report.get('worker_returncode_at_error')}), flush=True)
    finally:
        if tail:
            tail.close()
            report['worker_returncode_final'] = tail.proc.poll()
        report['peak_child_rss_KiB'] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        save()
    print(json.dumps({'event': 'done',
                      'external_boundary_target_reached': report['external_boundary_target_reached'],
                      'seconds': report['seconds'],
                      'peak_child_rss_KiB': report['peak_child_rss_KiB']}), flush=True)


if __name__ == '__main__':
    main()
