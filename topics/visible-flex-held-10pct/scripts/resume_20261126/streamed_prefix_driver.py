#!/usr/bin/env python3
"""Run the existing prefix equations with bounded radial RHS/Jacobian batches.

Only evaluation grouping changes. The full collocation matrix, unknowns,
boundary conditions, angular grid, physical parameters, and all numerical
acceptance gates remain those of portable_prefix_continue.py. This does not
reduce the memory needed by the final sparse factorization. A run is still a
finite linear-DN design unless the original driver requests a true tail.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np


def split_rhs(fun, block):
    def evaluate(t, y, p):
        if len(t) <= block:
            return fun(t, y, p)
        result = np.empty_like(y)
        for first in range(0, len(t), block):
            sl = slice(first, first + block)
            result[:, sl] = fun(t[sl], y[:, sl], p)
        return result
    return evaluate


def split_jac(fun, block):
    def evaluate(t, y, p):
        if len(t) <= block:
            return fun(t, y, p)
        n, m, k = y.shape[0], len(t), len(p)
        dy = np.empty((n, n, m))
        dp = np.empty((n, k, m))
        for first in range(0, m, block):
            sl = slice(first, first + block)
            jy, jp = fun(t[sl], y[:, sl], p)
            dy[:, :, sl], dp[:, :, sl] = jy, jp
        return dy, dp
    return evaluate


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--rhs-block', type=int, default=8)
    options, original_arguments = parser.parse_known_args()
    if options.rhs_block < 1:
        raise ValueError('A positive radial block is required')
    original = Path(__file__).resolve().parents[1] / 'resume_m3/portable_prefix_continue.py'
    spec = importlib.util.spec_from_file_location('held10_streamed_original', original)
    driver = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = driver
    spec.loader.exec_module(driver)
    original_solve = driver.solve_bvp

    def streamed_solve(fun, bc, x, y, p, **kwargs):
        if kwargs.get('fun_jac') is None:
            raise ValueError('The original analytical Jacobian must be retained')
        kwargs['fun_jac'] = split_jac(kwargs['fun_jac'], options.rhs_block)
        return original_solve(split_rhs(fun, options.rhs_block), bc, x, y, p, **kwargs)

    driver.solve_bvp = streamed_solve
    command = list(sys.argv)
    sys.argv = [str(original), *original_arguments]
    try:
        driver.main()
    finally:
        if '--outdir' in original_arguments:
            out = Path(original_arguments[original_arguments.index('--outdir') + 1])
            if out.is_dir():
                wrapper = Path(__file__).resolve()
                provenance = {
                    'command': command,
                    'wrapper_sha256': hashlib.sha256(wrapper.read_bytes()).hexdigest(),
                    'original_driver_sha256': hashlib.sha256(original.read_bytes()).hexdigest(),
                    'radial_rhs_jacobian_block': options.rhs_block,
                    'scope': __doc__,
                    'mathematical_parameters_changed': False,
                    'floating_point_bit_identity_claimed': False,
                    'original_gates_relaxed': False,
                }
                (out / 'radial-batching.json').write_text(json.dumps(provenance, indent=2) + '\n')


if __name__ == '__main__':
    main()
