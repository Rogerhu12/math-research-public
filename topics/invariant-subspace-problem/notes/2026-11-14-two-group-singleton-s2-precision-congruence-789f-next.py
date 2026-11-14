"""Alternative exact S2 generator using the full lower-birth precision forms.

This is separate from all frozen calculators and the submitted Actions path.
--check verifies the common-source congruences at rational parameters only;
it does not claim the symbolic adjacent inequality.
"""

import argparse
import importlib.util
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    's2_frozen_core', HERE/'2026-11-14-two-group-singleton-bridge-certificates-789f-next.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
Rat, emit = core.Rat, core.emit


def outer(row):
    return [[x*y for y in row] for x in row]


def elementary(n):
    return sum(core.base.choose(core.q, r)*core.base.choose(core.pool, ell)
               *core.z**r*core.w**b for r, b, ell in core.configurations(n))


def diagonal_compression(polynomial):
    weak = polynomial(Rat(1))/core.pool
    head = polynomial(core.z)/(core.q*core.z)
    exceptional = polynomial(core.w)/core.w
    return [[weak+head, weak], [weak, weak+exceptional]]


def precision_data():
    s, e2, e3, e4 = [elementary(n) for n in range(1, 5)]
    k1 = [core.z-1, core.w-1]
    k2 = [core.z**2-1, core.w**2-1]
    k3 = [core.z**3-1, core.w**3-1]
    eta2 = [k2[i]-s*k1[i] for i in range(2)]
    eta3 = [-e2*k1[i]+s*k2[i]-k3[i] for i in range(2)]
    n0 = diagonal_compression(lambda x: Rat(1))
    p1 = core.add(diagonal_compression(lambda x: s-2*x), outer(k1), -1/e2)
    p2 = core.add(diagonal_compression(lambda x: e2-2*s*x+3*x**2), outer(eta2), -1/e3)
    p3 = core.add(core.add(diagonal_compression(lambda x: e3-2*e2*x+3*s*x**2-4*x**3),
                            outer(k1)), outer(eta3), -1/e4)
    upper = core.gram(2, 0)
    ee = core.primitive_source(2)
    pp = [core.polynomial_gram(2, 0)[i][i] for i in range(5)]
    weights = [s-2*(r*core.z+b*core.w+ell) for r, b, ell in core.configurations(2)]
    hhat = [[sum(Rat(ee[k][i]*ee[k][j], pp[k])*weights[k] for k in range(5))
             for j in range(2)] for i in range(2)]
    bridge = [[2*(core.z-1), core.w-1], [Rat(), core.z-1]]
    emit('precision_forms_generated', profiles={str(j): core.base.profile(p)
                                                for j, p in enumerate((n0, p1, p2, p3))})
    return n0, p1, p2, p3, upper, hhat, bridge


def defect(target, data=None):
    n0, p1, p2, p3, upper, hhat, bridge = data if data is not None else precision_data()
    ni, p1i, p2i, ui = map(core.inverse2, (n0, p1, p2, upper))
    b0 = core.multiply(n0, bridge)
    bt = core.transpose(b0)
    if target == 's2-right-swapped':
        cform = core.add(hhat, core.multiply(bt, p2i, b0), -1)
        lower_gap = core.add(core.multiply(p1, ni, p1), p2, -1)
        transport = core.multiply(p1, p2i, p3, p2i, b0)
        answer = core.add(cform, core.multiply(core.transpose(transport),
                          core.inverse2(lower_gap), transport), -1)
        emit('precision_s2_defect_generated', target=target, **core.base.profile(answer))
        return answer
    m0 = core.multiply(b0, ui, bt)
    baseline = core.add(core.multiply(p2, ni, p2),
                        core.multiply(p2, p1i, p2, p1i, p2), -1)
    if target == 's2-left':
        answer = core.add(core.add(baseline, core.multiply(b0, ui, hhat, ui, bt), -1),
                          core.multiply(m0, p2i, m0))
    else:
        e_schur = core.add(p2, core.multiply(b0, core.inverse2(hhat), bt), -1)
        ei = core.inverse2(e_schur)
        if target == 's2-right':
            answer = core.add(core.add(baseline, core.multiply(p3, p2i, p3)),
                              core.multiply(p3, ei, p3), -1)
        else:
            difference = core.add(m0, p3, -1)
            fee = core.add(core.add(core.multiply(b0, ui, hhat, ui, bt),
                                     core.multiply(p3, ei, p3)),
                           core.multiply(difference, p2i, difference), -1)
            answer = core.add(baseline, fee, -Rat(1)/4)
    emit('precision_s2_defect_generated', target=target, **core.base.profile(answer))
    return answer


def matrices_equal(left, right):
    return all(not (left[i][j]-right[i][j]) for i in range(2) for j in range(2))


def check():
    core.q, core.pool, core.z, core.w = map(Rat, (3, 4, 4, 9))
    core.gram.cache_clear()
    core.polynomial_gram.cache_clear()
    data = precision_data()
    n0, p1, p2, p3, upper, hhat, bridge = data
    assert matrices_equal(n0, core.gram(1, 0))
    for j, precision in enumerate((p1, p2, p3), 1):
        actual = core.multiply(n0, core.inverse2(core.gram(1, j)), n0)
        assert matrices_equal(precision, actual)
    cform = core.add(hhat, core.multiply(core.transpose(bridge), core.gram(1, 2), bridge), -1)
    assert matrices_equal(cform, core.multiply(upper, core.inverse2(core.gram(2, 1)), upper))
    transform = core.multiply(core.inverse2(n0), p2)
    for target in ('s2-left', 's2-right', 's2-direct'):
        previous = core.s2_direct_defect(target)
        transformed = core.multiply(core.transpose(transform), previous, transform)
        assert matrices_equal(transformed, defect(target, data))
    l0, l1, l2, l3 = [core.gram(1, j) for j in range(4)]
    lower_gap = core.add(l0, core.multiply(l1, core.inverse2(l2), l1), -1)
    right_column = core.multiply(core.transpose(bridge), l2, core.inverse2(l3), l2)
    swapped = core.add(cform, core.multiply(right_column, core.inverse2(lower_gap),
                                           core.transpose(right_column)), -1)
    assert matrices_equal(swapped, defect('s2-right-swapped', data))
    emit('precision_common_source_check_passed', lower_precisions=(1, 2, 3),
         upper_C1_metric=True, left=True, right=True, full_S2=True, right_schur_swapped=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--target', choices=('s2-left', 's2-right', 's2-direct',
                                            's2-right-swapped'), default='s2-direct')
    args = parser.parse_args()
    if args.check:
        check()
        return
    data = precision_data()
    if args.prepare_only:
        emit('precision_preparation_complete', full_defect_not_expanded=True)
        return
    matrix = defect(args.target, data)
    for size in (1, 2):
        minor = matrix[0][0] if size == 1 else core.base.determinant_leibniz(matrix)
        certificate = core.base.coefficient_certificate(minor)
        emit('precision_s2_leading_minor', target=args.target, size=size, **certificate)
        if not certificate['passed']:
            emit('precision_s2_inconclusive', target=args.target)
            return
    emit('precision_s2_complete', target=args.target, all_passed=True)


if __name__ == '__main__':
    main()
