#!/usr/bin/env python3
"""Bound the original prefix RHS at entry as well as inside collocation.

This uses the existing radial batching and stale-LU-release implementation.
The additional initial-domain evaluation visits every original node in blocks,
preserving all state components, physical parameters, errors and acceptance
gates.  It does not repair an invalid initial field or reduce the final sparse
factorization memory.  Execution provenance records both original and executed
function hashes; floating-point bit identity is not asserted.
"""
import argparse
import gc
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import sys


def sha(value):
    return hashlib.sha256(value).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--rhs-block', type=int, default=8)
    options, original_arguments = parser.parse_known_args()
    if options.rhs_block < 1:
        raise ValueError('A positive radial block is required')
    scripts = Path(__file__).resolve().parents[2]
    existing_path = scripts / 'resume_20261126/streamed_release_prefix_driver.py'
    existing = load_module('_held10_existing_batching_20261128', existing_path)
    original = scripts / 'resume_m3/portable_prefix_continue.py'
    driver = load_module('_held10_original_portable_20261128', original)
    original_solve = driver.solve_bvp

    def bounded_solve(fun, bc, x, y, p, **kwargs):
        if kwargs.get('fun_jac') is None:
            raise ValueError('The original analytic Jacobian must remain active')
        gc.collect()
        kwargs['fun_jac'] = existing.split_jac(kwargs['fun_jac'], options.rhs_block)
        return original_solve(existing.split_rhs(fun, options.rhs_block), bc, x, y, p, **kwargs)

    driver.solve_bvp = bounded_solve
    original_guard = driver.install_rms_domain_guard
    release_record = {}

    def guard_and_release():
        original_guard()
        import f6curve_domain_newton as domain_newton
        before = inspect.getsource(domain_newton.solve_newton)
        marker = '            try:factor=splu(jac(y,p,ym,ff,fm,br))'
        if before.count(marker) != 1:
            raise ValueError('Original sparse-LU refresh statement differs')
        after = before.replace(marker, '            factor=None\n' + marker)
        exec(compile(after, str(Path(__file__).resolve()) + '::released_newton', 'exec'),
             domain_newton.__dict__)
        domain_newton.install()
        release_record.update(original_function_sha256=sha(before.encode()),
                              executed_function_sha256=sha(after.encode()),
                              arithmetic_changed=False,
                              scope='Discard only the obsolete factor before required refresh')

    driver.install_rms_domain_guard = guard_and_release
    original_main = inspect.getsource(driver.main)
    marker = '        rhs = o.fun(x,y,par)'
    if original_main.count(marker) != 1:
        raise ValueError('Original initial-domain RHS statement differs')
    executed_main = original_main.replace(marker,
        '        rhs = _held10_entry_rhs(o.fun)(x,y,par)')
    driver.__dict__['_held10_entry_rhs'] = lambda fun: existing.split_rhs(fun, options.rhs_block)
    exec(compile(executed_main, str(Path(__file__).resolve()) + '::bounded_entry', 'exec'),
         driver.__dict__)
    command = list(sys.argv)
    sys.argv = [str(original), *original_arguments]
    try:
        driver.main()
    finally:
        if '--outdir' in original_arguments:
            out = Path(original_arguments[original_arguments.index('--outdir') + 1])
            if out.is_dir():
                result = dict(command=command,
                    wrapper_sha256=sha(Path(__file__).read_bytes()),
                    original_driver_sha256=sha(original.read_bytes()),
                    existing_batching_sha256=sha(existing_path.read_bytes()),
                    original_main_sha256=sha(original_main.encode()),
                    executed_main_sha256=sha(executed_main.encode()),
                    initial_domain_rhs_batched=True,
                    radial_rhs_jacobian_block=options.rhs_block,
                    released_stale_factor=release_record,
                    collect_unreachable_flow_cycles_after_each_block=True,
                    original_all_nodes_and_components_evaluated=True,
                    mathematical_parameters_changed=False,
                    floating_point_bit_identity_claimed=False,
                    original_gates_relaxed=False, scope=__doc__)
                (out / 'radial-batching.json').write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
