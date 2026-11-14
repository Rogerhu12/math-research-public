"""Optional isolated-thread evaluation of the existing radial RHS batches.

Every worker owns a deepcopy of the current fully constructed Flow. It calls
that Flow's original fun on the same batch boundaries, angular grid and raw
values as root_radial_batching.value. No radial/angle discretization, metric,
formula, tolerance or Newton acceptance rule changes. No process is forked.
The caller keeps state_jacobian and boundary evaluation on their original
paths. This is a speed adapter, not a new solution or a convergence claim.
"""
from __future__ import annotations
import atexit
import copy
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import numpy as np

_WORKERS = 4
_POOL = None
_LOCK = threading.Lock()
STATS = dict(parallel_calls=0, serial_calls=0, radial_batches=0,
             radial_points=0, deepcopy_seconds=0., evaluation_seconds=0.)


def configure(workers):
    global _WORKERS
    workers = int(workers)
    if not 1 <= workers <= 8:
        raise ValueError('Use one through eight independent RHS workers')
    if _POOL is not None:
        raise RuntimeError('Configure before the first parallel evaluation')
    _WORKERS = workers


def close():
    global _POOL
    pool, _POOL = _POOL, None
    if pool is not None:
        pool.shutdown(wait=True, cancel_futures=True)


atexit.register(close)


def value(flow, s, y, p, batch_size=48):
    """Drop-in value interface; preserves the original default signature."""
    global _POOL
    count = len(s)
    if batch_size < 1:
        raise ValueError('Positive radial batch size required')
    if count <= batch_size or _WORKERS == 1:
        STATS['serial_calls'] += 1
        if count <= batch_size:
            return flow.fun(s, y, p)
        output = None
        for lo in range(0, count, batch_size):
            hi = min(lo + batch_size, count)
            block = flow.fun(s[lo:hi], y[:, lo:hi], p)
            if output is None:
                output = np.empty((block.shape[0], count), dtype=block.dtype)
            output[:, lo:hi] = block
        return output
    if not _LOCK.acquire(blocking=False):
        raise RuntimeError('Concurrent top-level RHS adapter calls are unsupported')
    try:
        workers = min(_WORKERS, (count + batch_size - 1)//batch_size)
        start = time.perf_counter()
        clones = [copy.deepcopy(flow) for _ in range(workers)]
        for item in clones:
            if item is flow or getattr(item.fun, '__self__', item) is not item:
                raise TypeError('The Flow callback must bind to its independent copy')
        STATS['deepcopy_seconds'] += time.perf_counter() - start
        original_calls = getattr(flow, 'calls', None)
        initial_calls = [getattr(item, 'calls', None) for item in clones]
        if _POOL is None:
            _POOL = ThreadPoolExecutor(max_workers=_WORKERS, thread_name_prefix='radial-rhs')

        def evaluate(index):
            result = []
            for lo in range(index*batch_size, count, workers*batch_size):
                hi = min(lo + batch_size, count)
                result.append((lo, hi, clones[index].fun(s[lo:hi], y[:, lo:hi], p)))
            return result

        start = time.perf_counter()
        futures = [_POOL.submit(evaluate, i) for i in range(workers)]
        output = None
        try:
            for future in futures:
                for lo, hi, block in future.result():
                    if output is None:
                        output = np.empty((block.shape[0], count), dtype=block.dtype)
                    output[:, lo:hi] = block
        except BaseException:
            for future in futures:
                future.cancel()
            # Finish live immutable evaluations before the caller resets Flow.
            for future in futures:
                if not future.cancelled():
                    try:
                        future.result()
                    except BaseException:
                        pass
            raise
        STATS['evaluation_seconds'] += time.perf_counter() - start
        STATS['parallel_calls'] += 1
        STATS['radial_points'] += count
        STATS['radial_batches'] += (count + batch_size - 1)//batch_size
        if isinstance(original_calls, (int, np.integer)) and all(isinstance(c, (int, np.integer)) for c in initial_calls):
            flow.calls = original_calls + sum(item.calls - before for item, before in zip(clones, initial_calls))
        return output
    finally:
        _LOCK.release()
