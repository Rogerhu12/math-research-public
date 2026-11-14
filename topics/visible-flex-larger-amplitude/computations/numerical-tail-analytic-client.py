"""Persistent actual tail client with analytic first-slope/mean Jacobian rows.

Only the owned in-memory worker adapter differs from the frozen source client.
The source solve/close protocol and complete compressed response recording are
reused. Second-jet derivative rows retain the documented symmetric difference.
This is a finite nonlinear DN; it does not assert infinite closure or reach.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


class WeightedTailPort:
    def __init__(self, config, source_root, record_prefix, node_heap=1536):
        self.config = Path(config)
        self.record_prefix = Path(record_prefix)
        if any(self.record_prefix.parent.glob(self.record_prefix.name + '_????.json.gz')):
            raise FileExistsError('Record prefix already used')
        source_root = Path(source_root).resolve()
        source_topic = source_root.parent.parent
        client_path = source_topic / 'scripts/78718-prefix-tail-geometric-client.py'
        spec = importlib.util.spec_from_file_location('numerical_analytic_source_client', client_path)
        client = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(client)
        self._original_class = client.WeightedTailPort
        backend = os.environ.get('VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND', 'fourier-root')
        predictor = os.environ.get('VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND', 'tangent')
        if backend != 'fourier-root' or predictor != 'tangent':
            raise ValueError('Analytic endpoint adapter requires fourier-root/tangent implementation')
        selected = client.implementation(backend, predictor)
        env = dict(os.environ, VISIBLE_FLEX_SOURCE_ROOT=str(source_root),
                   VISIBLE_FLEX_SOURCE_TOPIC=str(source_topic),
                   VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND=backend,
                   VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND=predictor,
                   CLOSING_TAIL_CACHE=str(source_root / 'topics/large-amplitude-twist-flex/scripts'),
                   NODE_OPTIONS=f'--max-old-space-size={node_heap}')
        worker = HERE / 'numerical-tail-analytic-worker.mjs'
        self.proc = subprocess.Popen(['node', str(worker), str(self.config)],
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     text=True, bufsize=1, env=env)
        self.calls = 0
        self.cache_key = self.cache_value = None
        line = self.proc.stdout.readline()
        if not line:
            raise RuntimeError('Analytic endpoint worker initialization failed')
        self.ready = json.loads(line)
        if self.ready.get('tailJacobian') != selected['jacobian_label']:
            raise RuntimeError('Actual tail variational backend mismatch')
        if self.ready.get('tailPredictor') != selected['predictor_label']:
            raise RuntimeError('Actual tail predictor mismatch')
        adapter = self.ready.get('endpointJacobianAdapter', {})
        if adapter.get('name') != 'numerical-analytic-first-slope-and-mean-v1':
            raise RuntimeError('Missing actual analytic endpoint adapter manifest')
        self.cut = self.ready['cut']
        self.linearD = np.asarray(self.ready['linearSlope'])
        self.M = len(self.linearD)
        names = ['db6f-prefix-tail-trial-client.py', client_path.name, selected['worker'],
                 '78718-tail-geometric-warm-remesh.mjs', '950f-tail-subdivision.mjs',
                 '950f-tail-warm-remesh.mjs', 'closing_weighted_tail.mjs',
                 'closing_recalibrated_tail.mjs', *selected['additional_sources']]
        self.sources = {name: hashlib.sha256((source_topic / 'scripts' / name).read_bytes()).hexdigest()
                        for name in names}
        for file in (Path(__file__), worker, HERE / 'numerical-tail-slope-jacobian.mjs'):
            self.sources[file.name] = hashlib.sha256(file.read_bytes()).hexdigest()
        # The source response recorder stores source_sha256; the exact source
        # replacements are also retained as a small sibling JSON manifest.
        manifest = self.record_prefix.with_name(self.record_prefix.name + '_adapter.json')
        with manifest.open('x') as stream:
            json.dump(adapter, stream, indent=2)
            stream.write('\n')

    def solve(self, height, jacobian=True, audit=False):
        return self._original_class.solve(self, height, jacobian=jacobian, audit=audit)

    def close(self):
        return self._original_class.close(self)
