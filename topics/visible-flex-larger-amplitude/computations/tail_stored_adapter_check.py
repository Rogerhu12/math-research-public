#!/usr/bin/env python3
"""Compare the bounded original-g adapter with the original actual tail worker.

Both workers solve the same small nonlinear Dirichlet problem sequentially and
perform the same full Darboux audit. This checks the worker composition as well
as the independently checked shared linear graph helper. It is a numerical
equivalence check, not a large-amplitude tail or closure certificate.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic', type=Path, required=True)
    p.add_argument('--config', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    a = p.parse_args()
    file = lambda suffix: a.out_prefix.with_name(a.out_prefix.name + suffix)
    cfg = json.loads(a.config.read_text())
    for key in ('initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
                'trialDiagnosticFile', 'trialStatePrefix'):
        cfg.pop(key, None)
    cfg.update(modes=3, quadrature=64, depth=4, shootingParts=4, steps=4,
               auditSteps=4, linearSteps=64, linearFar=12)
    height = [-1e-6, -2e-9, 1e-10]
    config_file = file('-config.json')
    with config_file.open('x') as stream:
        json.dump(cfg, stream, indent=2); stream.write('\n')
    records = []
    for name, module_name in [('original', 'numerical-tail-analytic-client.py'),
                              ('bounded', 'tail_stored_client.py')]:
        module_path = Path(__file__).with_name(module_name)
        spec = importlib.util.spec_from_file_location('tail_check_' + name, module_path)
        module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        started = time.time()
        client = None
        try:
            client = module.WeightedTailPort(config_file, a.source_topic / 'repro/source-root',
                                             file('-' + name + '-response'), node_heap=512)
            response = client.solve(height, jacobian=True, audit=True)
            records.append({'name': name, 'seconds': time.time() - started,
                            'ready': client.ready, 'response': response,
                            'sources': client.sources})
            print(json.dumps({'worker': name, 'converged': response['converged'],
                              'residual': response['residual'],
                              'seconds': records[-1]['seconds']}), flush=True)
        finally:
            if client:
                client.close()
    coarse, fine = records
    compare = {}
    for key in ('parameters', 'cut', 'linearSlope'):
        compare['ready_' + key] = coarse['ready'][key] == fine['ready'][key]
    for key in ('residual', 'jets', 'heightJetJacobian', 'history', 'audit', 'checkpoint'):
        compare['response_' + key] = coarse['response'][key] == fine['response'][key]
    common = coarse['sources'].keys() & fine['sources'].keys()
    compare['common_source_hashes'] = all(coarse['sources'][k] == fine['sources'][k] for k in common)
    report = {'scope': __doc__, 'complete_height': height,
              'config_file': str(config_file),
              'comparison': compare, 'all_compared_values_exactly_equal': all(compare.values()),
              'residual': fine['response']['residual'], 'audit': fine['response']['audit'],
              'common_source_file_count': len(common),
              'bounded_geometry_manifest': fine['ready']['storedMetricAdapter'],
              'bounded_graph_manifest': fine['ready']['stableGraphAdapter'],
              'seconds': {x['name']: x['seconds'] for x in records},
              'peak_child_rss_KiB': resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    for name in ('original', 'bounded'):
        response_file = file('-' + name + '-response_0001.json.gz')
        report[name + '_response_file'] = str(response_file)
        report[name + '_response_sha256'] = hashlib.sha256(response_file.read_bytes()).hexdigest()
    with file('-comparison.json').open('x') as stream:
        json.dump(report, stream, indent=2); stream.write('\n')
    print(json.dumps({'all_compared_values_exactly_equal': all(compare.values()),
                      'comparison': compare,
                      'peak_child_rss_KiB': report['peak_child_rss_KiB']}), flush=True)
    if not all(compare.values()):
        raise AssertionError('Bounded stored worker differs from original worker')


if __name__ == '__main__':
    main()
