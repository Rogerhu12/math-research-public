#!/usr/bin/env python3
"""Sharpen only polynomial ranges of an unchanged continuous R125 consumer.

For each fixed angle the radial polynomial is in the convex hull of its
Bernstein coefficient *functions*. Bound those functions on a complete
angular arc before taking their radial hull. Intersect with the previous
valid independent-coefficient bound. No native coefficient is changed.
"""
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'fd2d_gc_primitive_joint_base', HERE/'fd2d-metric-gc-primitive-continuous.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
M = base.M
old_range = M.range_polynomial
calls = 0


def joint_range(p, trig=None):
    global calls
    if trig is None:
        return old_range(p, trig)
    c = M.real_coefficients(p)
    if c.lo.shape[1] > trig[p.phase].lo.shape[0]:
        raise ValueError('Angular proof table too short')
    bern = M.poly.interval_matmul(
        M.centered_bernstein_matrix(c.lo.shape[0]-1), c)
    table = trig[p.phase][:c.lo.shape[1]]
    angular_coefficients = M.poly.interval_matmul(bern, table)
    joint = M.I(angular_coefficients.lo.min(axis=0),
                angular_coefficients.hi.max(axis=0))
    independent = M.poly.interval_matmul(
        M.I(bern.lo.min(axis=0)[None, :], bern.hi.max(axis=0)[None, :]),
        table)[0]
    lo = np.maximum(joint.lo, independent.lo)
    hi = np.minimum(joint.hi, independent.hi)
    if np.any(lo > hi):
        raise ArithmeticError('Two valid polynomial enclosures must intersect')
    calls += 1
    return M.I(lo, hi)


M.range_polynomial = joint_range


def main():
    base.main()
    output = Path(sys.argv[sys.argv.index('--out')+1])
    report = base.load_json(output)
    report.update(
        polynomial_range_adapter=base.identity(__file__),
        polynomial_range_method='angular interval sum of each Bernstein row, then radial convex hull; intersect previous coefficient hull',
        joint_bernstein_range_calls=calls,
        finite_native_field_and_auxiliary_polynomials_unchanged=True)
    output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(joint_bernstein_range_calls=calls,
                          closed_report=base.identity(output))), flush=True)


if __name__ == '__main__':
    main()
