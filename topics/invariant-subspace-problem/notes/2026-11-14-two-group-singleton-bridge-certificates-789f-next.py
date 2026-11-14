"""Exact S1/S2 certificate attempt for the actual old two-group/one-bit model.

Upper primitive birth 2 uses the complete 5D inverse, lower birth 1 the
complete 3D inverse.  A fixed integer source and its true metric are retained.
There is no positivity assertion unless all indicated coefficient checks pass.
"""

import argparse
import importlib.util
import math
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    'r273_aggregate', HERE/'2026-11-14-two-exceptional-aggregate-polynomial-789f-next.py')
aggregate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aggregate)
base = aggregate.base
Rat, CTX, ZERO, ONE, emit = base.Rat, base.CTX, base.ZERO, base.ONE, base.emit
Q, R, Z, U, V = map(Rat, CTX.gens())
q, pool, z, w = Q+3, R+3, Z+1, V


def configurations(level):
    return [(r, b, level-r-b) for r in range(level+1)
            for b in (0, 1) if level-r-b >= 0]


def primitive_source(birth):
    if birth == 1:
        pp = [{(1, 0, 0): 1, (0, 0, 1): -1},
              {(0, 1, 0): 1, (0, 0, 1): -1}]
    else:
        pp = [{(2, 0, 0): 1, (1, 0, 1): -2, (0, 0, 2): 1},
              {(1, 1, 0): 1, (1, 0, 1): -1,
               (0, 1, 1): -1, (0, 0, 2): 1}]
    return [[p.get(row, 0) for p in pp] for row in configurations(birth)]


@lru_cache(None)
def polynomial_gram(birth, n):
    target = configurations(birth)
    size = len(target)
    ff = [[ZERO for _ in range(size)] for _ in range(size)]
    for source in configurations(birth+n):
        r, b, ell = source
        weight = aggregate.value_polynomial(base.choose(q, r)*base.choose(pool, ell)*z**r*w**b)
        if not weight:
            continue
        vv = [math.prod(aggregate.choose_nonnegative(a, x) for a, x in zip(source, row))
              for row in target]
        for i in range(size):
            for j in range(i, size):
                if vv[i] and vv[j]:
                    ff[i][j] += vv[i]*vv[j]*weight
                    ff[j][i] = ff[i][j]
    emit('singleton_polynomial_gram', birth=birth, height=n, dimension=size,
         max_terms=max(len(x) for row in ff for x in row))
    return ff


@lru_cache(None)
def gram(birth, n):
    ff = polynomial_gram(birth, n)
    ee = primitive_source(birth)
    size = len(ff)
    pp = [polynomial_gram(birth, 0)[i][i] for i in range(size)]
    if n == 0:
        result = [[sum(Rat(ee[k][i]*ee[k][j], pp[k]) for k in range(size))
                   for j in range(2)] for i in range(2)]
    else:
        common = ONE
        for polynomial in pp:
            common *= aggregate.exact_quotient(polynomial, common.gcd(polynomial))
        gg = [[aggregate.exact_quotient(ff[i][j], pp[i]) for j in range(size)]
              for i in range(size)]
        rhs = [[aggregate.exact_quotient(common, pp[i])*ee[i][j] for j in range(2)]
               for i in range(size)]
        solved, determinant = aggregate.fraction_free_solve(
            gg, rhs, 'birth-'+str(birth)+'-height-'+str(n))
        result = [[Rat(sum(ee[k][i]*solved[k][j] for k in range(size)), determinant*common)
                   for j in range(2)] for i in range(2)]
    assert result[0][1].n*result[1][0].d == result[1][0].n*result[0][1].d
    emit('singleton_compressed_gram', birth=birth, height=n, **base.profile(result))
    return result


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(*matrices):
    answer = matrices[0]
    for matrix in matrices[1:]:
        answer = base.multiply(answer, matrix)
    return answer


def add(left, right, factor=1):
    return [[left[i][j]+factor*right[i][j] for j in range(len(left[0]))]
            for i in range(len(left))]


def scale(matrix, factor):
    return [[factor*x for x in row] for row in matrix]


def inverse2(matrix):
    aa, bb = matrix[0]
    cc, dd = matrix[1]
    determinant = aa*dd-bb*cc
    return [[dd/determinant, -bb/determinant], [-cc/determinant, aa/determinant]]


def cleared_determinant2(matrix):
    """A square common denominator, with no expensive final gcd cancellation."""
    common = ONE
    for row in matrix:
        for entry in row:
            common *= aggregate.exact_quotient(entry.d, common.gcd(entry.d))
    numerator = [[entry.n*aggregate.exact_quotient(common, entry.d)
                  for entry in row] for row in matrix]
    determinant = numerator[0][0]*numerator[1][1]-numerator[0][1]*numerator[1][0]
    emit('singleton_cleared_determinant',
         numerator_terms=len(determinant), numerator_degree=int(determinant.total_degree()),
         common_terms=len(common), common_degree=int(common.total_degree()))
    return Rat(determinant, common**2, reduced=True)


def defect(which):
    if which == 's1-direct':
        return s1_direct_defect()
    if which in ('s2-direct', 's2-left', 's2-right'):
        return s2_direct_defect(which)
    h0, h1 = gram(2, 0), gram(2, 1)
    l0, l1, l2, l3 = [gram(1, n) for n in range(4)]
    hi0, hi1, li2, li3 = map(inverse2, (h0, h1, l2, l3))
    bridge = [[2*(z-1), w-1], [Rat(), z-1]]
    bt = transpose(bridge)
    if which == 's1':
        delta = scale(add(multiply(hi1, bt, l3), multiply(hi0, bt, l2), -1), Rat(1)/2)
        answer = add(add(multiply(hi1, h0, hi1), inverse2(gram(2, 2)), -1),
                     multiply(delta, li3, transpose(delta)), -1)
    else:
        aa = scale(add(multiply(hi1, bt, l2), multiply(hi0, bt, l2, li3, l2)), Rat(1)/2)
        answer = add(add(l0, multiply(transpose(aa), h1, aa), -1),
                     multiply(l1, li2, l1), -1)
    emit('singleton_defect_generated', target=which, **base.profile(answer))
    return answer


def s1_direct_defect():
    """The exact physical quadratic form, with the upper inverse eliminated.

    Uses the general identity supplied by literature_audit on 2026-11-14.
    This is H0 * (the coordinate s1 defect) * H0, not the same coordinate
    matrix as defect('s1').  Positivity is equivalent by a common congruence.
    """
    h0 = gram(2, 0)
    hi0 = inverse2(h0)
    l2, l3 = gram(1, 2), gram(1, 3)
    ee = primitive_source(2)
    pp = [polynomial_gram(2, 0)[i][i] for i in range(5)]
    source_metric = [[Rat(ee[i][j], pp[i]) for j in range(2)] for i in range(5)]
    total = q*z+pool+w
    commutator = [total-2*(r*z+b*w+ell) for r, b, ell in configurations(2)]
    hhat = [[sum(ee[k][i]*source_metric[k][j]*commutator[k] for k in range(5))
             for j in range(2)] for i in range(2)]
    fhat = multiply(transpose(source_metric),
                    [[Rat(x) for x in row] for row in polynomial_gram(2, 2)], source_metric)
    bridge = [[2*(z-1), w-1], [Rat(), z-1]]
    bt = transpose(bridge)
    mhat = multiply(bt, l2, bridge)
    nhat = multiply(bt, l2, inverse2(l3), l2, bridge)
    jj = [[2*(z-1)**2, 2*(z-1)*(w-1)]]
    e4 = sum(base.choose(q, r)*base.choose(pool, ell)*z**r*w**b
             for r, b, ell in configurations(4))
    answer = add(add(add(multiply(hhat, hi0, hhat), fhat, -1),
                     multiply(mhat, hi0, mhat), -1), scale(nhat, 2))
    answer = add(answer, scale(multiply(transpose(jj), jj), 1/(4*e4)))
    emit('singleton_defect_generated', target='s1-direct', **base.profile(answer))
    return answer


def s2_direct_defect(which):
    """Retain Cbar=H0 H1^-1 H0; preserve the order of both columns."""
    h0, hi0 = gram(2, 0), inverse2(gram(2, 0))
    l0, l1, l2, l3 = [gram(1, n) for n in range(4)]
    ee = primitive_source(2)
    pp = [polynomial_gram(2, 0)[i][i] for i in range(5)]
    total = q*z+pool+w
    hh = [total-2*(r*z+b*w+ell) for r, b, ell in configurations(2)]
    hhat = [[sum(Rat(ee[k][i]*ee[k][j], pp[k])*hh[k] for k in range(5))
             for j in range(2)] for i in range(2)]
    bridge = [[2*(z-1), w-1], [Rat(), z-1]]
    bt = transpose(bridge)
    cbar = add(hhat, multiply(bt, l2, bridge), -1)
    yy = multiply(hi0, bt, l2)
    zz = multiply(bt, l2, inverse2(l3), l2)
    dlow = add(l0, multiply(l1, inverse2(l2), l1), -1)
    if which == 's2-left':
        answer = add(dlow, multiply(transpose(yy), cbar, yy), -1)
    elif which == 's2-right':
        answer = add(dlow, multiply(transpose(zz), inverse2(cbar), zz), -1)
    else:
        rr = add(multiply(cbar, yy), zz)
        answer = add(dlow, multiply(transpose(rr), inverse2(cbar), rr), -Rat(1)/4)
    emit('singleton_defect_generated', target=which, **base.profile(answer))
    return answer


def check_actual_layer():
    global q, pool, z, w
    import sympy as sp
    qv, lv, av, uv = 3, 4, 2, 3
    q, pool, z, w = map(Rat, (qv, lv, av*av, uv*uv))
    def exact(value):
        return sp.Rational(str(value.n(1, 1, 1, 1, 1)/value.d(1, 1, 1, 1, 1)))
    physical_sources = {}
    for birth, heights in ((1, range(4)), (2, range(3))):
        target = configurations(birth)
        transforms = [math.comb(qv, r)*math.comb(lv, ell)*av**r*uv**b
                      for r, b, ell in target]
        source = sp.diag(*[sp.Rational(1, t) for t in transforms])*sp.Matrix(primitive_source(birth))
        physical_sources[birth] = source
        for n in heights:
            inputs = [ii for ii in configurations(birth+n) if ii[0] <= qv and ii[2] <= lv]
            def entry(oo, ii, amplitudes=(av, uv, 1)):
                gaps = [a-b for a, b in zip(ii, oo)]
                if min(gaps) < 0:
                    return 0
                return math.prod(amplitudes[j]**gaps[j]
                                 *aggregate.choose_nonnegative((qv, 1, lv)[j]-oo[j], gaps[j])
                                 for j in range(3))
            incidence = sp.Matrix([[entry(oo, ii) for ii in inputs] for oo in target])
            wi = sp.diag(*[sp.Rational(1, math.comb(qv, r)*math.comb(lv, ell))
                           for r, b, ell in inputs])
            expected = source.T*(incidence*wi*incidence.T).inv()*source
            actual = sp.Matrix([[exact(x) for x in row] for row in gram(birth, n)])
            assert actual == expected
    def single_delete(oo, ii, cubes=False):
        gaps = [a-b for a, b in zip(ii, oo)]
        if min(gaps) < 0 or sum(gaps) != 1:
            return 0
        amplitudes = (av**3, uv**3, 1) if cubes else (av, uv, 1)
        return math.prod(amplitudes[j]**gaps[j]
                         *aggregate.choose_nonnegative((qv, 1, lv)[j]-oo[j], gaps[j])
                         for j in range(3))
    cubic = sp.Matrix([[single_delete(oo, ii, True) for ii in configurations(2)]
                       for oo in configurations(1)])
    kk = sp.Matrix([[2*(av*av-1), uv*uv-1], [0, av*av-1]])
    assert cubic*physical_sources[2] == physical_sources[1]*kk
    for birth in (1, 2):
        dd = sp.Matrix([[single_delete(oo, ii) for ii in configurations(birth)]
                        for oo in configurations(birth-1)])
        assert dd*physical_sources[birth] == sp.zeros(dd.rows, 2)
    for which in ('s1', 's2'):
        dd = defect(which)
        assert dd[0][1].n*dd[1][0].d == dd[1][0].n*dd[0][1].d
    expected_direct = multiply(gram(2, 0), defect('s1'), gram(2, 0))
    actual_direct = s1_direct_defect()
    assert all(not (expected_direct[i][j]-actual_direct[i][j])
               for i in range(2) for j in range(2))
    old_s2, direct_s2 = defect('s2'), s2_direct_defect('s2-direct')
    assert all(not (old_s2[i][j]-direct_s2[i][j]) for i in range(2) for j in range(2))
    emit('singleton_exact_full_layer_check_passed', upper_dimension=5, lower_dimension=3,
         cubic_bridge=True, common_physical_sources=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--target', choices=('s1', 's1-direct', 's2', 's2-direct',
                                            's2-left', 's2-right'), default='s2-direct')
    parser.add_argument('--stop-after-grams', action='store_true')
    parser.add_argument('--uncancelled-determinant', action='store_true')
    args = parser.parse_args()
    if args.check:
        check_actual_layer()
        return
    if args.stop_after_grams:
        for birth, heights in ((2, (0, 1, 2)), (1, (0, 1, 2, 3))):
            for n in heights:
                gram(birth, n)
        emit('singleton_profile_complete')
        return
    dd = defect(args.target)
    for size in (1, 2):
        minor = (dd[0][0] if size == 1 else cleared_determinant2(dd)
                 if args.uncancelled_determinant else base.determinant_leibniz(dd))
        certificate = base.coefficient_certificate(minor)
        emit('singleton_leading_minor', target=args.target, size=size, **certificate)
        if not certificate['passed']:
            emit('singleton_inconclusive', target=args.target,
                 reason='coefficient sign criterion did not close')
            return
    emit('singleton_coefficient_run_complete', target=args.target, all_passed=True)


if __name__ == '__main__':
    main()
