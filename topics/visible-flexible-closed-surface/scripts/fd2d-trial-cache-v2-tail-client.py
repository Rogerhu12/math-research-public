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
import threading
import time

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('geometric_original_trial_client', HERE/'db6f-prefix-tail-trial-client.py')
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)


def implementation(backend='original', predictor='linear', trial='momentum', root_precision='original',
                   partition_refinement=False, stage_workers=0):
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
    if stage_workers not in (0, 1, 2, 4):
        raise ValueError('Explicit stage workers must be 0, 1, 2 or 4')
    if stage_workers in (1, 2, 4):
        if backend != 'fourier-root' or trial != 'geometric-centered' or root_precision != 'original':
            raise ValueError('Parallel stages currently use Fourier-root, centered trials and original root precision')
        worker = 'fd2d-trial-cache-v2-tail-stage-worker.mjs'
        replacement = {'78718-tail-geometric-trial-core.mjs': 'fd2d-bounded-tail-stage-core.mjs',
                       '78718-tail-geometric-trial-split.mjs': 'fd2d-bounded-tail-stage-split.mjs'}
        sources = [replacement.get(name, name) for name in sources]
        sources += ['fd2d-geometric-trial-cache-v2.mjs', 'fd2d-single-tail-stage-pool.mjs', 'fd2d-cached-tail-stage-pool.mjs', 'fd2d-stage-map-cache.mjs', '78718-tail-partition-warm-remesh.mjs']
        sources = list(dict.fromkeys(sources))
    return {'worker': worker, 'additional_sources': sources,
            'stage_workers': stage_workers,
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
        stage_workers = int(os.environ.get('VISIBLE_FLEX_TAIL_STAGE_WORKERS', '0'))
        selected = implementation(backend, predictor, trial, root_precision, partition_refinement, stage_workers)
        worker = HERE/selected['worker']
        source_root = Path(source_root)
        env = dict(os.environ, VISIBLE_FLEX_SOURCE_ROOT=str(source_root),
                   CLOSING_TAIL_CACHE=str(source_root/'topics/large-amplitude-twist-flex/scripts'),
                   NODE_OPTIONS='')
        # A global --max-old-space-size overrides nested Worker limits.
        # The small launcher has no such V8 flag; the solver and its stage
        # workers each receive their own effective resourceLimits instead.
        launcher = HERE/'fd2d-bounded-worker-launcher.mjs'
        self.proc = subprocess.Popen(['node', str(launcher), str(worker), str(self.config), str(node_heap)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1, env=env)
        self._monitor_stop = threading.Event()
        self._monitor_thread = threading.Thread(target=self._observe_runtime, daemon=True)
        self._monitor_thread.start()
        self.calls = 0
        self.cache_key = self.cache_value = None
        line = self.proc.stdout.readline()
        if not line:
            self._observe_exception(RuntimeError('Worker stopped before its ready record'))
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
        if self.ready.get('tailStageWorkers', 0) != stage_workers:
            raise RuntimeError('Worker did not announce the selected stage thread count')
        self.cut = self.ready['cut']
        self.linearD = np.asarray(self.ready['linearSlope'])
        self.M = len(self.linearD)
        names = ['db6f-prefix-tail-trial-client.py', 'fd2d-bounded-worker-launcher.mjs', Path(__file__).name,
                 worker.name, '78718-tail-geometric-warm-remesh.mjs',
                 '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
                 'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs']
        names += selected['additional_sources']
        self.sources = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names}

    def _observation_path(self, suffix):
        return self.record_prefix.with_name(self.record_prefix.name+suffix)

    def _write_observation(self, path, value):
        # Scalar infrastructure evidence only. Observation failure must never
        # change an otherwise valid mathematical request or response.
        try:
            raw = (json.dumps(value, indent=2, allow_nan=False)+'\n').encode()
            if len(raw) >= 100_000:
                return
            temporary = path.with_name(path.name+'.tmp')
            temporary.write_bytes(raw)
            temporary.replace(path)
        except Exception:
            pass

    def _observe_runtime(self):
        last_live_memory = None
        path = self._observation_path('-worker-runtime.json')
        while True:
            now = time.time()
            code = self.proc.poll()
            memory = {}
            try:
                for line in Path(f'/proc/{self.proc.pid}/status').read_text().splitlines():
                    key, value = line.split(':', 1)
                    if key in ('VmRSS', 'VmHWM', 'VmData', 'Threads', 'State'):
                        memory[key] = value.strip()
                if memory:
                    last_live_memory = {'unix_time': now, **memory}
            except OSError:
                pass
            system_memory = {}
            try:
                for line in Path('/proc/meminfo').read_text().splitlines():
                    key, value = line.split(':', 1)
                    if key in ('MemAvailable', 'MemFree', 'SwapFree'):
                        system_memory[key] = value.strip()
            except OSError:
                pass
            parent_memory = {}
            cpu = None
            limits = None
            try:
                for line in Path('/proc/self/status').read_text().splitlines():
                    key, value = line.split(':', 1)
                    if key in ('VmRSS', 'VmHWM', 'VmData', 'Threads'):
                        parent_memory[key] = value.strip()
                stat = Path(f'/proc/{self.proc.pid}/stat').read_text().split(') ', 1)[1].split()
                cpu = {'utime_ticks': int(stat[11]), 'stime_ticks': int(stat[12]),
                       'clock_ticks_per_second': os.sysconf('SC_CLK_TCK')}
                limits = Path(f'/proc/{self.proc.pid}/limits').read_text()
            except (OSError, ValueError, IndexError):
                pass
            self._write_observation(path, {
                'scope': 'Observed own Node/Python and global available memory; no solver or geometry claim.',
                'parent_python_memory': parent_memory,
                'worker_cpu': cpu, 'worker_inherited_limits': limits,
                'system_memory': system_memory,
                'unix_time': now, 'worker_pid': self.proc.pid,
                'worker_returncode': code, 'status_file_available': bool(memory),
                'last_live_memory': last_live_memory,
            })
            if code is not None or self._monitor_stop.wait(5):
                return

    def _observe_exception(self, error):
        code = self.proc.poll()
        waited = 0.0
        # EOF may precede the final process exit notification by a few ms.
        # Observe that natural exit before inherited cleanup can terminate it.
        # Ordinary mathematical exceptions do not wait on a live worker.
        if code is None and 'worker stopped' in str(error).lower():
            began = time.monotonic()
            try:
                code = self.proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                code = self.proc.poll()
            waited = time.monotonic()-began
        self._write_observation(self._observation_path(f'-worker-exception-{getattr(self, "calls", 0):04d}.json'), {
            'scope': 'Actual client exception and own worker state; not a fabricated DN response.',
            'unix_time': time.time(), 'worker_pid': self.proc.pid,
            'worker_returncode': code, 'exception': repr(error),
            'natural_exit_observation_seconds': waited,
            'call': getattr(self, 'calls', 0),
            'expected_response_exists': self._observation_path(f'_{getattr(self, "calls", 0):04d}.json.gz').exists(),
        })

    def solve(self, height, jacobian=True, audit=False):
        try:
            return super().solve(height, jacobian=jacobian, audit=audit)
        except Exception as error:
            self._observe_exception(error)
            raise

    def close(self):
        try:
            super().close()
        finally:
            if hasattr(self, '_monitor_stop'):
                self._monitor_stop.set()
                self._monitor_thread.join(timeout=1)
