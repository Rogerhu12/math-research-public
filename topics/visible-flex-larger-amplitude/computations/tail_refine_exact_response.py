#!/usr/bin/env python3
"""Refine one successful finite-tail response at exactly its saved complete H.

Select one change of discretization: the angular retained order, the radial
steps, or only the audit grid. Physical constructor parameters and solve
tolerance remain unchanged. Added angular Dirichlet coefficients are zero.
This does not change or solve the originating prefix and does not certify an
infinite collar.
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


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--response', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--warm-iteration', type=Path,
                   help='Optional recovery-only guess at precisely the refined H and discretization')
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument('--modes', type=int)
    group.add_argument('--steps', type=int)
    group.add_argument('--audit-steps', type=int)
    p.add_argument('--node-heap', type=int, default=1536)
    p.add_argument('--client', choices=('analytic-first', 'stored-bounded', 'stored-resumable'),
                   default='analytic-first',
                   help='The stored-bounded adapter changes storage and shared graph evaluation only')
    a = p.parse_args()
    started = time.time()
    old = json.loads(gzip.decompress(a.response.read_bytes()))
    if not old['response'].get('converged') or old['response'].get('failed'):
        raise ValueError('A successful actual finite-tail response is required')
    cfg = dict(old['config'])
    if a.modes is not None:
        if not cfg['modes'] < a.modes <= 64:
            raise ValueError('Require strictly increased modes, at most 64')
        if 4 * cfg['spacing'] * a.modes >= cfg['quadrature']:
            raise ValueError('Existing angular quadrature cannot resolve the new Fourier-product Jacobian')
        cfg['modes'] = a.modes
    elif a.steps is not None:
        if a.steps <= cfg['steps']:
            raise ValueError('Require strictly increased radial steps')
        cfg['steps'] = cfg['auditSteps'] = a.steps
    else:
        if a.audit_steps <= cfg['auditSteps']:
            raise ValueError('Require strictly increased audit steps')
        cfg['auditSteps'] = a.audit_steps
    height = list(old['request']['height'])
    height.extend([0.0] * (cfg['modes'] - len(height)))
    if height[:len(old['request']['height'])] != old['request']['height']:
        raise AssertionError('Complete original height was not preserved')
    if any(height[len(old['request']['height']):]):
        raise AssertionError('Added Dirichlet modes must be strictly zero')
    recovery = None
    if a.warm_iteration:
        recovery = json.loads(gzip.decompress(a.warm_iteration.read_bytes()))
        if (recovery.get('status') != 'iteration-recovery-only'
                or recovery['checkpoint']['cutHeight'] != height):
            raise ValueError('Recovery guess must explicitly preserve the complete refined H')
        parameters = recovery['checkpoint']['parameters']
        for key in ('modes', 'spacing', 'steps', 'quadrature', 'linearFar',
                    'linearSteps', 'shootingParts'):
            if parameters.get(key) != cfg.get(key):
                raise ValueError('Recovery discretization differs: ' + key)
        if parameters.get('physicalDepth', parameters['depth']) != cfg['depth']:
            raise ValueError('Recovery physical depth differs')
    file = lambda suffix: a.out_prefix.with_name(a.out_prefix.name + suffix)
    cfg.update(initialCheckpoint=str((a.warm_iteration or a.response).resolve()),
               traceFile=str(file('-trace.jsonl').resolve()),
               iterationCheckpointFile=str(file('-iteration.json.gz').resolve()),
               trialDiagnosticFile=str(file('-trials.jsonl').resolve()))
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    config_file = file('-config.json')
    with config_file.open('x') as stream:
        json.dump(cfg, stream, indent=2); stream.write('\n')
    changes = {k: [old['config'].get(k), cfg.get(k)]
               for k in sorted(old['config'].keys() | cfg.keys())
               if old['config'].get(k) != cfg.get(k)}
    allowed = {'modes', 'steps', 'auditSteps', 'initialCheckpoint', 'traceFile',
               'iterationCheckpointFile', 'trialDiagnosticFile'}
    if set(changes) - allowed:
        raise ValueError('Unexpected nonnumerical constructor change')
    origin = json.loads((a.source_topic / 'source-origin.json').read_text())
    report = {'scope': __doc__, 'source_origin': origin,
              'input_file': str(a.response), 'input_sha256': digest(a.response),
              'complete_physical_height_preserved_exactly': True,
              'added_height_modes_strictly_zero': True,
              'physical_constructor_fields_preserved_exactly': True,
              'configuration_changes': changes, 'height': height,
              'config_file': str(config_file),
              'script_sha256': digest(Path(__file__)), 'client': a.client,
              'converged': False}
    if recovery:
        report['recovery_only_guess'] = {
            'file': str(a.warm_iteration), 'sha256': digest(a.warm_iteration),
            'iteration': recovery['iteration'],
            'scope': 'Initial guess only; the refined solve and full audit still run normally'}
    save = lambda: file('-summary.json').write_text(json.dumps(report, indent=2) + '\n')
    save()
    module_path = Path(__file__).with_name({
        'analytic-first': 'numerical-tail-analytic-client.py',
        'stored-bounded': 'tail_stored_client.py',
        'stored-resumable': 'tail_resumable_client.py'}[a.client])
    spec = importlib.util.spec_from_file_location('fixed_tail_actual_client', module_path)
    client = importlib.util.module_from_spec(spec); spec.loader.exec_module(client)
    os.environ['VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND'] = 'fourier-root'
    os.environ['VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND'] = 'tangent'
    tail = None
    try:
        tail = client.WeightedTailPort(config_file, a.source_topic / 'repro/source-root',
                                       file('-response'), node_heap=a.node_heap)
        common = old['source_sha256'].keys() & tail.sources.keys()
        changed_sources = [key for key in common
                           if old['source_sha256'][key] != tail.sources[key]]
        if changed_sources:
            raise ValueError('Actual source changed: ' + ','.join(changed_sources))
        report.update(ready=tail.ready, common_source_hashes_equal=True,
                      common_source_file_count=len(common), source_sha256=tail.sources)
        save()
        print(json.dumps({'event': 'ready', 'modes': cfg['modes'],
                          'steps': cfg['steps'], 'auditSteps': cfg['auditSteps'],
                          'exact_complete_height': True}), flush=True)
        response = tail.solve(height, jacobian=True, audit=True)
        report.update(converged=bool(response['converged']), residual=response['residual'],
                      audit=response.get('audit'), jets=response.get('jets'),
                      response_file=str(file('-response_0001.json.gz')),
                      response_sha256=digest(file('-response_0001.json.gz')))
        if report['audit']:
            report['original_profile_normalized_full_defect'] = (
                cfg['shootingParts'] * report['audit']['normalizedFullDefect'])
        # The full successful response is already durably recorded by the
        # original client. Preserve its summary before graceful worker shutdown.
        report['seconds'] = time.time() - started
        save()
    except Exception as exc:
        report['error'] = repr(exc)
        if tail:
            report['worker_returncode_at_error'] = tail.proc.poll()
        print(json.dumps({'event': 'error', 'error': repr(exc)}), flush=True)
    finally:
        if tail:
            tail.close()
            report['worker_returncode_final'] = tail.proc.poll()
        report['peak_child_rss_KiB'] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        report['seconds'] = time.time() - started
        save()
    print(json.dumps({'event': 'done', 'converged': report['converged'],
                      'residual': report.get('residual'), 'audit': report.get('audit'),
                      'seconds': report['seconds']}), flush=True)


if __name__ == '__main__':
    main()
