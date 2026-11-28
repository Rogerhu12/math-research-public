"""Memoize repeated original R53 integrals on exactly the same finite input.

The cache is local to one material-core object.  Its context digest covers every
instance attribute, recursively including the complete original support core,
except the original two output caches and this memo's own storage.  Array dtype,
shape and every byte enter the digest; the normalized theta vector is bound in
the same way.  No rounded key, interpolated angle or changed quadrature is used.
Executed provider identities and the original evaluator source are recorded.

Protected entries contain private read-only copies.  Every cache hit restores
fresh, writable copies of the original _cache_theta/_cache_jets side effects and
returns fresh copies of the entire result.  A caller's writes therefore cannot
change a later return.  Unknown state types bypass memoization.  The entry and
byte limits only evict cached copies; a miss calls the unchanged evaluator.
"""
from collections import OrderedDict
import hashlib
import inspect
import struct
import time

import numpy as np


_MEMO = '_held10_complete_evaluate_memo'
_OUTPUT_CACHES = {'_cache_theta', '_cache_jets', _MEMO}


def _feed(digest, value, *, exclude=()):
    """Hash actual numerical state; unsupported types explicitly bypass reuse."""
    if isinstance(value, np.ndarray):
        array = np.ascontiguousarray(value)
        if array.dtype.hasobject:
            raise TypeError('Object array state is not memoized')
        _feed(digest, ('array', value.dtype.str, value.shape))
        digest.update(memoryview(array).cast('B'))
    elif isinstance(value, np.generic):
        digest.update(b'G')
        _feed(digest, np.asarray(value))
    elif value is None:
        digest.update(b'N;')
    elif isinstance(value, bool):
        digest.update(b'T;' if value else b'F;')
    elif isinstance(value, int):
        digest.update(b'I'+str(value).encode()+b';')
    elif isinstance(value, float):
        digest.update(b'R'+struct.pack('!d', value))
    elif isinstance(value, complex):
        digest.update(b'C'+struct.pack('!dd', value.real, value.imag))
    elif isinstance(value, (str, bytes)):
        data = value.encode() if isinstance(value, str) else value
        digest.update((b'S' if isinstance(value, str) else b'B')+
                      str(len(data)).encode()+b':'+data)
    elif isinstance(value, (list, tuple)):
        digest.update(b'L' if isinstance(value, list) else b'Q')
        _feed(digest, len(value))
        for item in value:
            _feed(digest, item)
    elif isinstance(value, dict):
        digest.update(b'D')
        keys = sorted((key for key in value if key not in exclude), key=repr)
        _feed(digest, len(keys))
        for key in keys:
            _feed(digest, key)
            _feed(digest, value[key])
    elif callable(value):
        _feed(digest, ('provider', type(value).__module__, type(value).__qualname__,
                      getattr(value, '__module__', None),
                      getattr(value, '__qualname__', None), id(value),
                      id(getattr(value, '__code__', None))))
    elif hasattr(value, '__dict__'):
        _feed(digest, ('object', type(value).__module__, type(value).__qualname__))
        _feed(digest, vars(value))
    else:
        raise TypeError('Unsupported core state type: '+type(value).__qualname__)


def context_digest(core):
    digest = hashlib.sha256()
    _feed(digest, ('R53-original-core-instance', type(core).__module__,
                  type(core).__qualname__))
    _feed(digest, vars(core), exclude=_OUTPUT_CACHES)
    return digest.hexdigest()


def _clone(value, readonly=False):
    if isinstance(value, np.ndarray):
        result = value.copy(order='K')
        if readonly:
            result.flags.writeable = False
        return result
    if isinstance(value, dict):
        return {key: _clone(item, readonly) for key, item in value.items()}
    if isinstance(value, tuple):
        return tuple(_clone(item, readonly) for item in value)
    if isinstance(value, list):
        return [_clone(item, readonly) for item in value]
    return value


def _bytes(value):
    if isinstance(value, np.ndarray):
        return value.nbytes
    if isinstance(value, dict):
        return sum(_bytes(item) for item in value.values())
    if isinstance(value, (tuple, list)):
        return sum(map(_bytes, value))
    return 0


def install(core_class, max_entries=2, max_bytes=128*1024*1024):
    if max_entries < 1 or max_bytes < 1:
        raise ValueError('Positive cache limits are required')
    original = core_class.evaluate
    if getattr(original, '_held10_complete_memo_stats', None) is not None:
        return original._held10_complete_memo_stats
    stats = dict(enabled=True, hits=0, misses=0, context_changes=0, bypasses=0,
        evictions=0, context_key_seconds=0., original_evaluate_seconds=0.,
        copy_seconds=0., max_entries_per_core=max_entries, max_bytes_per_core=max_bytes,
        peak_cached_bytes_one_core=0, peak_entry_bytes=0,
        original_evaluator_sha256=hashlib.sha256(inspect.getsource(original).encode()).hexdigest(),
        complete_instance_state_bound=True, complete_theta_bytes_bound=True,
        original_output_cache_side_effects_restored=True,
        returned_arrays_are_independent_writable_copies=True,
        quadrature_or_model_changed=False)

    def evaluate(core, theta):
        if not stats['enabled']:
            return original(core, theta)
        theta = np.asarray(theta, float).reshape(-1)
        begin = time.monotonic()
        try:
            context = context_digest(core)
        except (TypeError, RecursionError):
            stats['bypasses'] += 1
            return original(core, theta)
        key = (theta.dtype.str, theta.shape, theta.tobytes())
        stats['context_key_seconds'] += time.monotonic()-begin
        memo = getattr(core, _MEMO, None)
        if memo is None or memo['context'] != context:
            if memo is not None:
                stats['context_changes'] += 1
            memo = dict(context=context, entries=OrderedDict(), bytes=0)
            setattr(core, _MEMO, memo)
        entry = memo['entries'].get(key)
        if entry is not None:
            stats['hits'] += 1
            memo['entries'].move_to_end(key)
            begin = time.monotonic()
            core._cache_theta = _clone(entry['theta'])
            core._cache_jets = _clone(entry['jets'])
            result = _clone(entry['value'])
            stats['copy_seconds'] += time.monotonic()-begin
            return result
        stats['misses'] += 1
        begin = time.monotonic()
        result = original(core, theta)
        stats['original_evaluate_seconds'] += time.monotonic()-begin
        begin = time.monotonic()
        entry = dict(theta=_clone(core._cache_theta, True),
                     jets=_clone(core._cache_jets, True), value=_clone(result, True))
        size = _bytes(entry)+len(key[2])
        stats['peak_entry_bytes'] = max(stats['peak_entry_bytes'], size)
        if size <= max_bytes:
            while memo['entries'] and (len(memo['entries']) >= max_entries or
                                       memo['bytes']+size > max_bytes):
                _, removed = memo['entries'].popitem(last=False)
                memo['bytes'] -= removed['bytes']
                stats['evictions'] += 1
            entry['bytes'] = size
            memo['entries'][key] = entry
            memo['bytes'] += size
            stats['peak_cached_bytes_one_core'] = max(
                stats['peak_cached_bytes_one_core'], memo['bytes'])
        stats['copy_seconds'] += time.monotonic()-begin
        return result

    evaluate._held10_complete_memo_stats = stats
    core_class.evaluate = evaluate
    return stats
