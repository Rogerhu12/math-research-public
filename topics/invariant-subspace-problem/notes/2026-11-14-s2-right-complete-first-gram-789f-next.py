"""Exact alternate right-column expression using the actual complete first Gram.

No frozen source or submitted Actions path is modified.  A successful numeric
identity check is not a symbolic positivity certificate.
"""

import argparse
import importlib.util
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    's2_first_gram_frozen_core',
    HERE/'2026-11-14-two-group-singleton-bridge-certificates-789f-next.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
Rat, emit = core.Rat, core.emit


def defect():
    upper_zero, upper_one = core.gram(2, 0), core.gram(2, 1)
    lower_zero, lower_one, lower_two, lower_three = [core.gram(1, j) for j in range(4)]
    bridge = [[2*(core.z-1), core.w-1], [Rat(), core.z-1]]
    emit('right_complete_first_gram_inputs_ready')
    column = core.multiply(core.inverse2(upper_zero), core.transpose(bridge),
                           lower_two, core.inverse2(lower_three), lower_two)
    emit('right_complete_first_gram_column_ready', **core.base.profile(column))
    baseline = core.add(lower_zero, core.multiply(lower_one, core.inverse2(lower_two), lower_one), -1)
    fee = core.multiply(core.transpose(column), upper_one, column)
    emit('right_complete_first_gram_fee_ready', **core.base.profile(fee))
    answer = core.add(baseline, fee, -1)
    emit('right_complete_first_gram_defect_ready', **core.base.profile(answer))
    return answer


def check():
    core.q, core.pool, core.z, core.w = map(Rat, (3, 4, 4, 9))
    core.gram.cache_clear()
    core.polynomial_gram.cache_clear()
    previous, current = core.s2_direct_defect('s2-right'), defect()
    assert all(not (previous[i][j]-current[i][j]) for i in range(2) for j in range(2))
    emit('right_complete_first_gram_check_passed', identical_original_source=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        check()
        return
    matrix = defect()
    for size in (1, 2):
        minor = matrix[0][0] if size == 1 else core.base.determinant_leibniz(matrix)
        certificate = core.base.coefficient_certificate(minor)
        emit('right_complete_first_gram_leading_minor', size=size, **certificate)
        if not certificate['passed']:
            emit('right_complete_first_gram_inconclusive')
            return
    emit('right_complete_first_gram_complete', all_passed=True)


if __name__ == '__main__':
    main()
