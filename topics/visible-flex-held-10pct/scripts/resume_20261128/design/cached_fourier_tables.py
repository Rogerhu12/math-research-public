"""Share only geometry-independent Fourier assembly CSR arrays across Flows.

The original builder depends on n, M, the complete even-frequency vector and
the actual cylindrical basis B (through N and its norms).  The key binds all
of those values, including the entire B bytes.  Each returned dictionary has
fresh diagnostic counters.  Only the two read-only sparse arrays are shared;
no physical Flow, field, core, parameter, frame or numerical response is cached.
"""
import hashlib
import inspect
import time
import numpy as np


def array_sha(value):
    array = np.ascontiguousarray(value)
    digest = hashlib.sha256()
    digest.update(array.dtype.str.encode())
    digest.update(repr(array.shape).encode())
    digest.update(memoryview(array).cast('B'))
    return digest.hexdigest()


def install(module):
    original = module.build_tables
    templates = {}
    stats = dict(hits=0, misses=0, key_seconds=0., build_seconds=0.,
                 original_builder_sha256=hashlib.sha256(
                     inspect.getsource(original).encode()).hexdigest(),
                 full_basis_and_frequency_bytes_bound=True,
                 live_flow_or_physical_response_cached=False,
                 shared_diagnostic_dictionary=False)

    def build(flow):
        begin = time.monotonic()
        key = (int(flow.n), int(flow.M), int(flow.B.shape[1]),
               array_sha(np.asarray(flow.even)), array_sha(flow.B))
        stats['key_seconds'] += time.monotonic() - begin
        template = templates.get(key)
        if template is None:
            begin = time.monotonic()
            template = original(flow)
            stats['build_seconds'] += time.monotonic() - begin
            for name in ('first', 'second'):
                for member in ('data', 'indices', 'indptr'):
                    getattr(template[name], member).flags.writeable = False
            templates[key] = template
            stats['misses'] += 1
        else:
            stats['hits'] += 1
        # The original builder has just constructed these zero diagnostic
        # counters.  Return a new dictionary for every Flow, retaining the
        # original sparse matrices and all original field values.
        result = dict(template)
        result.update(imaginary_max=0., evaluated_points=0, calls=0)
        return result

    module.build_tables = build
    return stats
