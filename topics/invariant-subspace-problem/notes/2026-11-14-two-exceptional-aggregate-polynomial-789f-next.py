"""Actual birth-two, two-group/two-exception Gram via eight polynomial rows.

The source is fixed across all heights.  The full eight-dimensional inverse is
taken before source compression.  A coefficient-sign failure is inconclusive,
not a numerical or algebraic counterexample to the adjacent inequality.
"""

import argparse
import importlib.util
import itertools
import math
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    'r273_rat', HERE/'2026-11-14-two-exceptional-first-edge-polynomial-certificate-789f-next.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
CTX, ONE, ZERO = base.CTX, base.ONE, base.ZERO
Rat, emit = base.Rat, base.emit
q, pool, z, w1, w2 = base.q, base.pool, base.z, base.w1, base.w2


def configurations(level):
    return [(r, b, c, level-r-b-c)
            for r in range(level+1) for b in (0, 1) for c in (0, 1)
            if level-r-b-c >= 0]


TARGET = configurations(2)


def multiply_small_polynomials(left, right):
    answer = {}
    for ll, aa in left.items():
        for rr, bb in right.items():
            key = tuple(a+b for a, b in zip(ll, rr))
            answer[key] = answer.get(key, 0)+aa*bb
    return answer


def source_columns():
    xx = {(1, 0, 0, 0): 1, (0, 0, 0, 1): -1}
    yy = {(0, 1, 0, 0): 1, (0, 0, 0, 1): -1}
    zz = {(0, 0, 1, 0): 1, (0, 0, 0, 1): -1}
    pp = [multiply_small_polynomials(left, right)
          for left, right in ((xx, xx), (xx, yy), (xx, zz), (yy, zz))]
    return [[pp[j].get(row, 0) for j in range(4)] for row in TARGET]


E = source_columns()


def choose_nonnegative(n, k):
    return math.comb(n, k) if n >= k >= 0 else 0


def value_polynomial(value):
    assert value.d == ONE
    return value.n


@lru_cache(None)
def polynomial_gram(n):
    matrix = [[ZERO for _ in TARGET] for _ in TARGET]
    for source in configurations(n+2):
        r, b, c, ell = source
        weight = value_polynomial(base.choose(q, r)*base.choose(pool, ell)
                                  *z**r*w1**b*w2**c)
        if not weight:
            continue
        vv = [math.prod(choose_nonnegative(a, x) for a, x in zip(source, row))
              for row in TARGET]
        for i in range(8):
            if not vv[i]:
                continue
            for j in range(i, 8):
                if vv[j]:
                    matrix[i][j] += vv[i]*vv[j]*weight
                    matrix[j][i] = matrix[i][j]
    emit('aggregate_polynomial_gram', height=n,
         max_terms=max(len(x) for row in matrix for x in row),
         max_degree=max(int(x.total_degree()) for row in matrix for x in row))
    return matrix


def exact_quotient(numerator, denominator):
    quotient, remainder = divmod(numerator, denominator)
    if remainder:
        raise AssertionError('fraction-free division had a nonzero remainder')
    return quotient


def fraction_free_solve(matrix, rhs, label):
    """Montante elimination: return adj(matrix)*rhs, det(matrix)."""
    size = len(matrix)
    width = len(rhs[0])
    aa = [list(row) for row in matrix]
    bb = [[x if hasattr(x, 'terms') else CTX.constant(x) for x in row] for row in rhs]
    previous = ONE
    for k in range(size):
        pivot = aa[k][k]
        if not pivot:
            raise AssertionError('positive leading principal pivot vanished')
        next_a = [list(row) for row in aa]
        next_b = [list(row) for row in bb]
        for i in range(size):
            if i == k:
                continue
            for j in range(size):
                if j != k:
                    next_a[i][j] = exact_quotient(pivot*aa[i][j]-aa[i][k]*aa[k][j],
                                                previous)
            for j in range(width):
                next_b[i][j] = exact_quotient(pivot*bb[i][j]-aa[i][k]*bb[k][j], previous)
            next_a[i][k] = ZERO
        aa, bb = next_a, next_b
        previous = pivot
        emit('aggregate_fraction_free_pivot', label=label, column=k,
             pivot_terms=len(pivot), pivot_degree=int(pivot.total_degree()),
             max_rhs_terms=max(len(x) for row in bb for x in row))
    determinant = aa[0][0]
    assert all(aa[i][j] == (determinant if i == j else ZERO)
               for i in range(size) for j in range(size))
    return bb, determinant


@lru_cache(None)
def compressed_gram(n):
    ff = polynomial_gram(n)
    if n == 0:
        result = [[sum(Rat(E[k][i]*E[k][j], ff[k][k]) for k in range(8))
                   for j in range(4)] for i in range(4)]
    else:
        # F_n = P G_n.  Every row has its actual count/weight factor P_ii,
        # leaving G_n of total degree at most 2n.  G_n is not symmetric;
        # the physical inverse metric P^-1 remains in the right-hand side.
        pp = [polynomial_gram(0)[i][i] for i in range(8)]
        common = ONE
        for polynomial in pp:
            common *= exact_quotient(polynomial, common.gcd(polynomial))
        gg = [[exact_quotient(ff[i][j], pp[i]) for j in range(8)] for i in range(8)]
        rhs = [[exact_quotient(common, pp[i])*E[i][j] for j in range(4)] for i in range(8)]
        emit('aggregate_row_factor_removed', height=n,
             max_degree=max(int(x.total_degree()) for row in gg for x in row),
             max_terms=max(len(x) for row in gg for x in row),
             common_metric_degree=int(common.total_degree()))
        solved, determinant = fraction_free_solve(gg, rhs, 'height-'+str(n))
        determinant *= common
        result = [[Rat(sum(E[k][i]*solved[k][j] for k in range(8)), determinant)
                   for j in range(4)] for i in range(4)]
    emit('aggregate_compressed_gram', height=n, **base.profile(result))
    return result


def check_actual_layer():
    global q, pool, z, w1, w2
    import sympy as sp
    spec = importlib.util.spec_from_file_location(
        'r273_full', HERE/'2026-11-14-two-exceptional-schur-789f.py')
    physical = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(physical)
    qv, lv, av, uv, vv = 3, 4, 2, 3, 5
    q, pool, z, w1, w2 = map(Rat, (qv, lv, av*av, uv*uv, vv*vv))
    def exact(value):
        return sp.Rational(str(value.n(1, 1, 1, 1, 1)/value.d(1, 1, 1, 1, 1)))
    assert TARGET == physical.basis(qv, lv, 2)
    counts = [math.comb(qv, r)*math.comb(lv, ell) for r, b, c, ell in TARGET]
    weights = [av**r*uv**b*vv**c for r, b, c, ell in TARGET]
    transform = sp.diag(*[cc*ww for cc, ww in zip(counts, weights)])
    source = transform.inv()*sp.Matrix(E)
    dd, _ = physical.incidence(qv, lv, 1, 1, av, uv, vv)
    assert dd*source == sp.zeros(4, 4)
    assert source.rank() == 4
    for n in range(3):
        incidence, src = physical.incidence(qv, lv, 2, n, av, uv, vv)
        inv_metric = sp.diag(*[sp.Rational(1, math.comb(qv, r)*math.comb(lv, ell))
                              for r, b, c, ell in src])
        physical_gram = incidence*inv_metric*incidence.T
        generated = sp.Matrix([[sp.Rational(str(p(1, 1, 1, 1, 1)))
                                for p in row] for row in polynomial_gram(n)])
        assert generated == transform*physical_gram*transform
        actual = source.T*physical_gram.inv()*source
        recovered = sp.Matrix([[exact(x) for x in row] for row in compressed_gram(n)])
        assert actual == recovered
    emit('aggregate_exact_full_layer_check_passed', all_heights=(0, 1, 2),
         full_layer_dimension=8, primitive_dimension=4,
         fixed_source_and_physical_metric=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--stop-after-gram', type=int, choices=(0, 1, 2))
    parser.add_argument('--max-minor', type=int, default=4, choices=(1, 2, 3, 4))
    args = parser.parse_args()
    if args.check:
        check_actual_layer()
        return
    grams = []
    for n in range(3):
        grams.append(compressed_gram(n))
        if args.stop_after_gram == n:
            emit('aggregate_profile_complete', last_height=n)
            return
    inverse0 = base.inverse(grams[0])
    subtraction = base.multiply(base.multiply(grams[1], inverse0), grams[1])
    difference = [[grams[2][i][j]-subtraction[i][j] for j in range(4)] for i in range(4)]
    for k in range(1, args.max_minor+1):
        minor = base.determinant_leibniz([row[:k] for row in difference[:k]])
        certificate = base.coefficient_certificate(minor)
        emit('aggregate_leading_minor', size=k, **certificate)
        if not certificate['passed']:
            emit('aggregate_inconclusive', reason='coefficient sign criterion did not close')
            return
    emit('aggregate_coefficient_run_complete', all_passed=True,
         full_four_by_four=args.max_minor == 4)


if __name__ == '__main__':
    main()
