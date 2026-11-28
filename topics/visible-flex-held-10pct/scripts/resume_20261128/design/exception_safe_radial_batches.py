"""Collect unreachable Flow cycles after every original radial evaluation.

The original batching collected only after a successful multi-block call.
Its short-call and exceptional paths skipped collection, while the actual
Flow stores bound methods that form self cycles.  These wrappers retain the
same calls, slices, output allocation, assignment order, and exceptions, and
add collection in finally clauses.  They do not clear a live physical cache,
alter a domain test, or change a Newton decision.  Statistics contain only
scalars and strings, never exception objects, frames, flows, or result arrays.
"""
import gc
from pathlib import Path
import resource
import time

import numpy as np


def statistics():
    return dict(rhs_calls=0, jacobian_calls=0, rhs_blocks=0, jacobian_blocks=0,
                collections=0, collected_objects=0, collection_seconds=0.,
                exception_blocks=0, exception_types={}, maximum_rss_kib=0,
                successful_and_exceptional_short_calls_collected=True,
                live_caches_cleared=False, original_exceptions_suppressed=False,
                original_numerical_calls_or_arithmetic_changed=False)


def _rss():
    rows = Path('/proc/self/status').read_text().splitlines()
    return next(int(row.split()[1])*1024 for row in rows if row.startswith('VmRSS:'))


def _exception(error):
    # Convert immediately; do not preserve an exception or its traceback.
    return dict(type=type(error).__module__+'.'+type(error).__qualname__,
                message=str(error))


def _release(stats, kind, exception, event):
    before = _rss() if exception is not None else None
    begin = time.monotonic()
    collected = gc.collect()
    elapsed = time.monotonic()-begin
    stats['collections'] += 1
    stats['collected_objects'] += collected
    stats['collection_seconds'] += elapsed
    stats['maximum_rss_kib'] = max(stats['maximum_rss_kib'],
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if exception is not None:
        stats['exception_blocks'] += 1
        name = exception['type']
        stats['exception_types'][name] = stats['exception_types'].get(name, 0)+1
        if event is not None:
            event(dict(event='original_radial_exception_after_collection', kind=kind,
                original_exception=exception, current_rss_before_collection_bytes=before,
                current_rss_after_collection_bytes=_rss(),
                collected_objects=collected, collection_seconds=elapsed,
                exception_propagated_unchanged=True))


def split_rhs(fun, block, stats=None, event=None):
    if block < 1:
        raise ValueError('A positive original radial block is required')
    stats = statistics() if stats is None else stats

    def evaluate(t, y, p):
        stats['rhs_calls'] += 1
        if len(t) <= block:
            exception = None
            stats['rhs_blocks'] += 1
            try:
                return fun(t, y, p)
            except BaseException as error:
                exception = _exception(error)
                raise
            finally:
                _release(stats, 'rhs', exception, event)
        result = np.empty_like(y)
        for first in range(0, len(t), block):
            sl = slice(first, first+block)
            exception = None
            stats['rhs_blocks'] += 1
            try:
                result[:, sl] = fun(t[sl], y[:, sl], p)
            except BaseException as error:
                exception = _exception(error)
                raise
            finally:
                _release(stats, 'rhs', exception, event)
        return result

    return evaluate


def split_jac(fun, block, stats=None, event=None):
    if block < 1:
        raise ValueError('A positive original radial block is required')
    stats = statistics() if stats is None else stats

    def evaluate(t, y, p):
        stats['jacobian_calls'] += 1
        if len(t) <= block:
            exception = None
            stats['jacobian_blocks'] += 1
            try:
                return fun(t, y, p)
            except BaseException as error:
                exception = _exception(error)
                raise
            finally:
                _release(stats, 'jacobian', exception, event)
        n, m, k = y.shape[0], len(t), len(p)
        dy = np.empty((n, n, m))
        dp = np.empty((n, k, m))
        for first in range(0, m, block):
            sl = slice(first, first+block)
            exception = None
            stats['jacobian_blocks'] += 1
            try:
                jy, jp = fun(t[sl], y[:, sl], p)
                dy[:, :, sl], dp[:, :, sl] = jy, jp
                del jy, jp
            except BaseException as error:
                exception = _exception(error)
                raise
            finally:
                _release(stats, 'jacobian', exception, event)
        return dy, dp

    return evaluate


def install(loader_module, event=None):
    """Intercept only the existing original batching module's fresh load."""
    original = loader_module.load_module
    stats = statistics()

    def load(name, filename):
        module = original(name, filename)
        if Path(filename).name == 'streamed_release_prefix_driver.py':
            module.split_rhs = lambda fun, block: split_rhs(fun, block, stats, event)
            module.split_jac = lambda fun, block: split_jac(fun, block, stats, event)
        return module

    loader_module.load_module = load

    def restore():
        loader_module.load_module = original

    return stats, restore
