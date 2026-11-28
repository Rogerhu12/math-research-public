#!/usr/bin/env python3
"""Use complete block QR with acyclic factor ownership in prefix Newton.

The selected resource driver still owns the original source, geometry, domain,
residual, merit, mesh refinement, and all finite acceptance tests. Only sparse
linear factorization/solve is replaced. Every replacement factor and its direct
original-matrix residual diagnostics are logged, with no field arrays. No claim
of floating-point bit identity is made. This never truncates a singular column. The separate v2 entry only removes
the logging wrapper reference cycle; the BlockQR numerical core is unchanged.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

from block_qr import BlockQR


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def wrap_factor(result, event, identifier):
    """Keep only a one-way wrapper-to-factor reference; never replace solve."""
    original_apply = result.solve

    def apply(rhs):
        answer = original_apply(rhs)
        event('solve_return', factor=identifier, stats=dict(result.stats))
        return answer

    return SimpleNamespace(solve=apply)


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--base-driver', type=Path,
                        default=here/'design/prefix_resource_driver.py')
    args, rest = parser.parse_known_args()
    sys.path.insert(0, str(args.base_driver.resolve().parent))
    base = load('_held10_block_qr_resource_base', args.base_driver.resolve())
    # The cached resource v2 delegates to the unchanged resource v1 module.
    target = getattr(base, 'previous', base)
    original_loader = target.load_module
    portable = here.parent/'resume_m3/portable_prefix_continue.py'
    out = Path(rest[rest.index('--outdir')+1]).resolve() if '--outdir' in rest else None
    path = out.with_name(out.name+'-block-qr.jsonl') if out is not None else None
    if path is not None and path.exists():
        raise FileExistsError(path)
    started, number = time.monotonic(), 0

    def event(kind, **fields):
        if path is not None:
            with path.open('a') as stream:
                stream.write(json.dumps(dict(event=kind, seconds=time.monotonic()-started,
                    maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                    **fields), allow_nan=False)+'\n')

    hashes = {str(file): hashlib.sha256(file.read_bytes()).hexdigest() for file in
              (Path(__file__).resolve(), here/'block_qr.py', args.base_driver.resolve(), portable)}
    event('replacement_requested', source_hashes=hashes, command=list(sys.argv),
          equations_changed=False, numerical_linear_arithmetic_changed=True,
          original_nonlinear_gates_changed=False,
          factor_wrapper_has_no_back_reference=True)

    def source_loader(name, file):
        module = original_loader(name, file)
        if Path(file).resolve() != portable:
            return module
        original_solve = module.solve_bvp

        def qr_solve(fun, bc, x, y, p, **kwargs):
            import f6curve_domain_newton as domain
            original_factor = domain.splu
            n, k = y.shape[0], len(p)

            def factor(matrix):
                nonlocal number
                number += 1
                total = matrix.shape[0]-k
                if total % n:
                    raise ValueError('Refined collocation node count is not integral')
                m = total//n
                event('factor_start', factor=number, n=n, m=m, k=k,
                      matrix_nonzeros=int(matrix.nnz))
                result = BlockQR(matrix, n, m, k)
                event('factor_return', factor=number, stats=dict(result.stats))
                # The base resource driver clears its obsolete factor before
                # constructing the next complete J. This wrapper must not make
                # result -> apply -> result a cycle that delays that release.
                return wrap_factor(result, event, number)

            domain.splu = factor
            try:
                return original_solve(fun, bc, x, y, p, **kwargs)
            finally:
                domain.splu = original_factor

        module.solve_bvp = qr_solve
        return module

    target.load_module = source_loader
    sys.argv = [str(args.base_driver.resolve()), *rest]
    try:
        return base.main()
    finally:
        event('driver_return_or_exception', factor_count=number,
              source_hashes=hashes, complete_surface=False)


if __name__ == '__main__':
    main()
