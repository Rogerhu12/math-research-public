#!/usr/bin/env python3
"""Check the real actual-coupling loader's prefix-only Flow cache wiring.

The actual class, its original physical prefix constructor, and a small
warm mesh are created through root_actual_bounded_neck.main. Before any
coupled solve, only three-point prefix Jacobians are compared. ensure_tail
is replaced by a hard failure guard, so no tail worker or BVP can start.
The expected inspection exception is not a nonlinear solver outcome.
"""
from __future__ import annotations
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import gc
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import root_actual_bounded_neck as bounded

HERE = Path(__file__).resolve().parent


def main():
    i = sys.argv.index('--check-output')
    out = Path(sys.argv[i+1])
    del sys.argv[i:i+2]
    source_hashes = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                     for name in ('strong_actual_cache_check.py', 'root_actual_bounded_neck.py',
                                  'root_actual_neck_bvp.py', 'strong_neck_bvp.py', 'strong_flow_lru.py')}
    adapter = bounded.adapter
    original_module = adapter.module
    counts = dict(guarded_tail_start_attempts=0, coupled_solve_inspections=0)

    def inspect(self, fun, bc, x, y, p, **kw):
        counts['coupled_solve_inspections'] += 1
        if self.tail is not None:
            raise AssertionError('Tail initialized before the local prefix inspection')
        cache = getattr(self, '_strong_geometric_flow_cache', None)
        if cache is None or cache.size != 8:
            raise AssertionError('Actual nested loading chain did not install cache size 8')
        indices = np.unique(np.round(np.linspace(0, len(x)-1, 5)[1:-1]).astype(int))
        t, state = x[indices], y[:, indices]
        first = kw['fun_jac'](t, state, p)
        after_first = dict(cache.stats)
        second = kw['fun_jac'](t, state, p)
        after_second = dict(cache.stats)
        equality = [bool(np.array_equal(a, b)) for a, b in zip(first, second)]
        errors = [float(np.max(abs(a-b))) for a, b in zip(first, second)]
        if not all(equality) or after_second['hits'] <= after_first['hits']:
            raise AssertionError('Repeated actual-prefix Jacobian did not reuse identical Flows')
        if counts['guarded_tail_start_attempts'] or self.tail is not None:
            raise AssertionError('Unexpected tail start in prefix-only inspection')
        result = dict(scope=__doc__, nonlinear_solve_run=False, tail_worker_started=False,
                      loader_chain='root_actual_bounded_neck.main -> actual.module=adapter.module -> cached root_dual.make_dual -> Actual(Base)',
                      actual_class=type(self).__qualname__, modes=self.M, angular=self.nt,
                      warm_nodes=len(x), selected_radial_points=t.tolist(),
                      cache_size=cache.size, prefix_J_PJ_array_equal=equality,
                      prefix_J_PJ_max_abs_difference=errors, cache_after_first=after_first,
                      cache_after_second=after_second, cache_instance_records=adapter.FLOW_CACHE_RECORDS,
                      actual_recovery_context=self.raw_recovery_context,
                      source_sha256=source_hashes, counts=dict(counts), memory=adapter.memory_record())
        out.write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(dict(event='actual_prefix_cache_inspection_passed',
                              memory=result['memory'], cache=after_second)), flush=True)
        raise RuntimeError('Actual prefix cache inspection complete; no BVP or tail worker requested')

    def guarded_tail(self):
        counts['guarded_tail_start_attempts'] += 1
        raise AssertionError('Tail worker forbidden in this local cache-wiring inspection')

    def module(name, path):
        loaded = original_module(name, path)
        if Path(path).name == 'root_dual_core_bvp.py':
            original_main = loaded.main

            def instrumented_main():
                # Actual.main has already replaced loaded.make_dual with its
                # real Actual factory by the time it calls loaded.main.
                actual_factory = loaded.make_dual

                def factory(*args, **kwargs):
                    actual = actual_factory(*args, **kwargs)
                    actual.ensure_tail = guarded_tail
                    actual.solve_coupled = inspect
                    return actual

                loaded.make_dual = factory
                return original_main()

            loaded.main = instrumented_main
        return loaded

    adapter.module = module
    bounded.main()
    gc.collect()
    if not out.is_file() or counts != dict(guarded_tail_start_attempts=0, coupled_solve_inspections=1):
        raise RuntimeError('Expected one completed local actual-prefix inspection')


if __name__ == '__main__':
    main()
