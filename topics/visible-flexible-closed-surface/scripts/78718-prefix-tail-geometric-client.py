"""Original recorded true-DN client, selecting the geometric warm worker.

Only process initialization and honest source names differ. solve/close are
the original methods; every returned packet contains the full tail order.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('geometric_original_trial_client', HERE/'db6f-prefix-tail-trial-client.py')
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)


def implementation(backend='original', predictor='linear', trial='momentum', root_precision='original',
                   partition_refinement=False):
    """Select numerical algorithms without adding fields to physical cfg."""
    if backend not in ('original', 'fourier', 'fourier-root'):
        raise ValueError('Unknown actual tail Jacobian backend')
    if predictor not in ('linear', 'tangent'):
        raise ValueError('Unknown actual tail warm predictor')
    if trial not in ('momentum', 'geometric', 'geometric-centered'):
        raise ValueError('Unknown actual tail trial construction')
    if root_precision not in ('original', 'tight'):
        raise ValueError('Unknown implicit root precision')
    if predictor == 'tangent' and backend == 'original':
        raise ValueError('Tangent warm prediction currently requires a Fourier tail backend')
    if trial != 'momentum' and backend == 'original':
        raise ValueError('Geometric trials currently use a Fourier tail worker')
    if root_precision == 'tight' and backend != 'fourier-root':
        raise ValueError('Tight implicit precision currently requires the Fourier-root backend')
    if root_precision == 'tight' and trial == 'geometric-centered':
        raise ValueError('Centered trials currently retain the original implicit root precision')
    if partition_refinement and (trial != 'geometric-centered' or root_precision != 'original'
                                 or backend != 'fourier-root'):
        raise ValueError('The explicit partition warm currently uses centered trials and the original-precision Fourier-root engine')
    tight = root_precision == 'tight'
    combined = predictor == 'tangent' or backend == 'fourier-root' or trial != 'momentum'
    worker = ('78718-prefix-tail-partition-centered-worker.mjs' if partition_refinement else
              '78718-prefix-tail-geometric-precision-worker.mjs' if tight else
              '78718-prefix-tail-geometric-centered-worker.mjs' if trial == 'geometric-centered' else
              '78718-prefix-tail-geometric-trial-worker.mjs' if trial == 'geometric' else
              '78718-prefix-tail-tangent-fourier-worker.mjs' if combined else
              '78718-prefix-tail-geometric-fourier-worker.mjs' if backend == 'fourier' else
              '78718-prefix-tail-geometric-worker.mjs')
    if combined:
        if trial != 'momentum' or tight:
            sources = ['78718-tail-geometric-trial-core.mjs', '78718-tail-geometric-trial-split.mjs',
                       '78718-tail-geometric-newton-retraction.mjs',
                       '78718-tail-geometric-newton-retraction-tight-v3.mjs' if tight else
                       '78718-tail-geometric-newton-retraction-v2.mjs']
            if trial == 'geometric-centered':
                sources += ['78718-tail-geometric-newton-retraction-centered-v3.mjs']
        else:
            sources = ['78718-tail-tangent-core.mjs', '78718-tail-tangent-split.mjs']
        sources += ['78718-tail-tangent-predictor.mjs', '78718-tail-geometric-amplitude-warm.mjs']
    else:
        sources = ['db6f-prefix-tail-trial-core.mjs', 'db6f-prefix-tail-trial-split.mjs']
    if backend != 'original':
        sources += ['78718-tail-fourier-product-flow.mjs', '78718-tail-fourier-product-jacobian.mjs']
    if backend == 'fourier-root':
        sources += (['78718-tail-fourier-root-tight-momentum.mjs',
                     '78718-tail-fourier-root-tight-split-engine.mjs'] if tight else
                    ['78718-tail-fourier-root-momentum.mjs',
                     '78718-tail-fourier-root-split-engine.mjs'])
    if partition_refinement:
        sources += ['78718-tail-partition-warm-remesh.mjs']
    return {'worker': worker, 'additional_sources': sources,
            'jacobian_label': ('fourier-root-and-product-moments-v1' if backend == 'fourier-root' else
                               'fourier-product-moments-v1' if backend == 'fourier' else 'original'),
            'predictor_label': ('full-shooting-tangent-v1' if predictor == 'tangent' else
                                'linear-amplitude-and-boundary-v1'),
            'trial_label': ('same-direction-Q-L-Newton-retraction-centered-v3' if trial == 'geometric-centered' else
                           ('same-direction-Q-L-Newton-retraction-mean-seeded-tight-v3' if tight else
                            'same-direction-Q-L-Newton-retraction-mean-seeded-v2') if trial == 'geometric' else
                           'linear-momentum-trial-v1'),
            'root_precision_label': ('tight-4e-15-fallback-2e-14-v1' if tight else
                                     'original-8e-14-fallback-5e-12')}


class WeightedTailPort(original.WeightedTailPort):
    def __init__(self, config, source_root, record_prefix, node_heap=1536):
        self.config = Path(config)
        self.record_prefix = Path(record_prefix)
        if any(self.record_prefix.parent.glob(self.record_prefix.name+'_????.json.gz')):
            raise FileExistsError('Record prefix already used')
        backend = os.environ.get('VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND', 'original')
        predictor = os.environ.get('VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND', 'linear')
        trial = os.environ.get('VISIBLE_FLEX_TAIL_TRIAL_BACKEND', 'momentum')
        root_precision = os.environ.get('VISIBLE_FLEX_TAIL_ROOT_PRECISION', 'original')
        partition_refinement = os.environ.get('VISIBLE_FLEX_TAIL_PARTITION_REFINEMENT', '0') == '1'
        selected = implementation(backend, predictor, trial, root_precision, partition_refinement)
        worker = HERE/selected['worker']
        source_root = Path(source_root)
        env = dict(os.environ, VISIBLE_FLEX_SOURCE_ROOT=str(source_root),
                   CLOSING_TAIL_CACHE=str(source_root/'topics/large-amplitude-twist-flex/scripts'),
                   NODE_OPTIONS=f'--max-old-space-size={node_heap}')
        self.proc = subprocess.Popen(['node', str(worker), str(self.config)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1, env=env)
        self.calls = 0
        self.cache_key = self.cache_value = None
        line = self.proc.stdout.readline()
        if not line:
            raise RuntimeError('Geometric warm weighted-tail initialization failed')
        self.ready = json.loads(line)
        if self.ready.get('tailJacobian', 'original') != selected['jacobian_label']:
            raise RuntimeError('Selected tail Fourier worker did not announce its implementation')
        if self.ready.get('tailPredictor', 'linear-amplitude-and-boundary-v1') != selected['predictor_label']:
            raise RuntimeError('Selected tail worker did not announce its warm predictor')
        if self.ready.get('tailTrial', 'linear-momentum-trial-v1') != selected['trial_label']:
            raise RuntimeError('Selected tail worker did not announce its trial construction')
        if self.ready.get('tailRootPrecision', 'original-8e-14-fallback-5e-12') != selected['root_precision_label']:
            raise RuntimeError('Selected tail worker did not announce its root precision')
        self.cut = self.ready['cut']
        self.linearD = np.asarray(self.ready['linearSlope'])
        self.M = len(self.linearD)
        names = ['db6f-prefix-tail-trial-client.py', Path(__file__).name,
                 worker.name, '78718-tail-geometric-warm-remesh.mjs',
                 '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
                 'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs']
        names += selected['additional_sources']
        self.sources = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names}
