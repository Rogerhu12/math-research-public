"""Exact FLINT polynomial certificate search for the actual R273 first edge.

Positive variables: q=3+Q, L=3+R, z=1+Z, w1=U+V, w2=V.
This program only reports a proof certificate when every required numerator
coefficient is nonnegative and strictness has a V-only positive monomial.
A negative coefficient is not a counterexample to the matrix inequality.

Requires python-flint. No matrices or expanded polynomials are written out.
"""

import argparse
import hashlib
import itertools
import json
import math
import time
from functools import lru_cache
from flint import fmpq, fmpq_mpoly_ctx


CTX = fmpq_mpoly_ctx.get(('Q', 'R', 'Z', 'U', 'V'))
ONE = CTX.constant(1)
ZERO = CTX.constant(0)
START = time.monotonic()


class Rat:
    __slots__ = ('n', 'd')

    def __init__(self, numerator=0, denominator=None, reduced=False):
        if isinstance(numerator, Rat) and denominator is None:
            self.n, self.d = numerator.n, numerator.d
            return
        nn = numerator if hasattr(numerator, 'terms') else CTX.constant(numerator)
        dd = ONE if denominator is None else (
            denominator if hasattr(denominator, 'terms') else CTX.constant(denominator))
        if not dd:
            raise ZeroDivisionError('zero polynomial denominator')
        if not nn:
            self.n, self.d = ZERO, ONE
            return
        if not reduced:
            gg = nn.gcd(dd)
            nn, dd = nn//gg, dd//gg
        leading = dd.leading_coefficient()
        self.n, self.d = nn/leading, dd/leading

    @staticmethod
    def make(other):
        return other if isinstance(other, Rat) else Rat(other)

    def __bool__(self):
        return bool(self.n)

    def __neg__(self):
        return Rat(-self.n, self.d, reduced=True)

    def __add__(self, other):
        other = Rat.make(other)
        if not self:
            return other
        if not other:
            return self
        common = self.d.gcd(other.d)
        left, right = self.d//common, other.d//common
        nn = self.n*right+other.n*left
        if not nn:
            return Rat()
        cancel = nn.gcd(common)
        return Rat(nn//cancel, (common//cancel)*left*right, reduced=True)

    __radd__ = __add__

    def __sub__(self, other):
        return self+(-Rat.make(other))

    def __rsub__(self, other):
        return Rat.make(other)+(-self)

    def __mul__(self, other):
        other = Rat.make(other)
        if not self or not other:
            return Rat()
        aa = self.n.gcd(other.d)
        bb = other.n.gcd(self.d)
        return Rat((self.n//aa)*(other.n//bb),
                   (self.d//bb)*(other.d//aa), reduced=True)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Rat.make(other)
        return self*Rat(other.d, other.n, reduced=True)

    def __rtruediv__(self, other):
        return Rat.make(other)/self

    def __pow__(self, n):
        if n < 0:
            return Rat(self.d, self.n, reduced=True)**(-n)
        return Rat(self.n**n, self.d**n, reduced=True)


def emit(event, **fields):
    print(json.dumps({'event': event, 'seconds': round(time.monotonic()-START, 3),
                      **fields}, sort_keys=True), flush=True)


def choose(x, k):
    value = Rat(fmpq(1, math.factorial(k)))
    for r in range(k):
        value *= x-r
    return value


Q, R, Z, U, V = map(Rat, CTX.gens())
q, pool, z, w1, w2 = Q+3, R+3, Z+1, U+V, V


@lru_cache(None)
def moments(j):
    ww = [choose(q, i)*choose(pool, j-i)*z**i for i in range(j+1)]
    mm = [sum((i**r)*ww[i] for i in range(j+1)) for r in range(5)]
    ee = mm[0]
    variance = ee*mm[2]-mm[1]**2
    det3 = (ee*(mm[2]*mm[4]-mm[3]**2)
            -mm[1]*(mm[1]*mm[4]-mm[2]*mm[3])
            +mm[2]*(mm[1]*mm[3]-mm[2]**2))
    mean, second = mm[1]/ee, mm[2]/ee
    if j == 0:
        result = (1/ee, mean, second, Rat(), None, Rat())
    else:
        result = (1/ee, mean, second,
                  (ee*mm[3]-mm[1]*mm[2])/variance,
                  ee/variance, det3/variance)
    emit('moments', height=j, terms_e=len(ee.n),
         terms_variance=len(variance.n), terms_det3=len(det3.n))
    return result


def zero_matrix(n, m):
    return [[Rat() for _ in range(m)] for _ in range(n)]


def add_square(matrix, weight, row):
    row = list(map(Rat.make, row))
    for i in range(len(row)):
        if not row[i]:
            continue
        for j in range(i, len(row)):
            if row[j]:
                matrix[i][j] += weight*row[i]*row[j]
                matrix[j][i] = matrix[i][j]


def profile(matrix):
    entries = [a for row in matrix for a in row]
    return {'max_num_terms': max(len(a.n) for a in entries),
            'max_den_terms': max(len(a.d) for a in entries),
            'max_num_degree': int(max(a.n.total_degree() for a in entries)),
            'max_den_degree': int(max(a.d.total_degree() for a in entries))}


@lru_cache(None)
def raw_gram(n):
    dd = [moments(n+k) for k in range(3)]
    aa = dd[0][0]+(w1+w2)*dd[1][0]+w1*w2*dd[2][0]
    difference = dd[0][3]-2*dd[1][3]+dd[2][3]
    increment = dd[2][3]-dd[1][3]
    ff = [x[2]-x[3]*x[1] for x in dd]
    mixed = ff[0]-2*ff[1]+ff[2]
    initial = [moments(k) for k in range(3)]
    mean1 = initial[1][1]
    initial_increment = initial[2][3]-initial[1][3]
    initial_ff = [x[2]-x[3]*x[1] for x in initial]
    initial_mixed = initial_ff[0]-2*initial_ff[1]+initial_ff[2]
    centered_increment = increment-initial_increment
    centered_mixed = (mixed-initial_mixed+difference*dd[0][1]
                      +2*mean1*centered_increment)
    lam = w1*w2/(w1*w2*dd[0][5]+(w1+w2)*dd[1][5]+dd[2][5])
    matrix = zero_matrix(5, 5)
    matrix[0][0] = aa
    for y, z0 in ((0, 0), (1, 0), (0, 1), (1, 1)):
        datum = dd[y+z0]
        if datum[4] is not None:
            centered_mean = datum[1]-dd[0][1]-(y+z0)*mean1
            add_square(matrix, w1**y*w2**z0*datum[4],
                       [-centered_mean, y, z0, 0, 1])
    add_square(matrix, lam,
               [-centered_mixed, -centered_increment, -centered_increment, 1, -difference])
    emit('raw_gram', height=n, **profile(matrix))
    return matrix


@lru_cache(None)
def source_entry(n, i, j):
    if j < i:
        return source_entry(n, j, i)
    matrix = raw_gram(n)
    answer = matrix[i][j]
    if n:
        answer -= matrix[i][4]*matrix[4][j]/matrix[4][4]
    emit('source_entry', height=n, row=i, column=j,
         num_terms=len(answer.n), den_terms=len(answer.d))
    return answer


def gram(n):
    answer = [[source_entry(n, i, j) for j in range(4)] for i in range(4)]
    emit('source_gram', height=n, **profile(answer))
    return answer


def inverse_first_gram():
    """The common source shear makes H0 diagonal plus one rank-one block."""
    d0, d1, d2 = [moments(k) for k in range(3)]
    aa = d0[0]+(w1+w2)*d1[0]+w1*w2*d2[0]
    diagonal = [aa, w1*d1[4], w2*d1[4]]
    vv = [2*d1[1]-d2[1], Rat(1), Rat(1)]
    weight = w1*w2*d2[4]
    denominator = 1+weight*sum(vv[i]**2/diagonal[i] for i in range(3))
    answer = zero_matrix(4, 4)
    for i in range(3):
        for j in range(3):
            answer[i][j] = (Rat(int(i == j))/diagonal[i]
                            -weight*(vv[i]/diagonal[i])*(vv[j]/diagonal[j])/denominator)
    answer[3][3] = d2[5]/(w1*w2)
    emit('first_gram_inverse', **profile(answer))
    return answer


@lru_cache(None)
def first_diagonal_rank_one():
    d0, d1, d2 = [moments(k) for k in range(3)]
    aa = d0[0]+(w1+w2)*d1[0]+w1*w2*d2[0]
    diagonal = (aa, w1*d1[4], w2*d1[4], w1*w2/d2[5])
    vv = (2*d1[1]-d2[1], Rat(1), Rat(1))
    weight = w1*w2*d2[4]
    denominator = 1+weight*sum(vv[i]**2/diagonal[i] for i in range(3))
    return diagonal, vv, weight, denominator


@lru_cache(None)
def adjacent_entry(i, j):
    if j < i:
        return adjacent_entry(j, i)
    diagonal, vv, weight, denominator = first_diagonal_rank_one()
    rowi = [source_entry(1, i, k) for k in range(4)]
    rowj = [source_entry(1, j, k) for k in range(4)]
    schur = sum(rowi[k]*rowj[k]/diagonal[k] for k in range(4))
    si = sum(rowi[k]*vv[k]/diagonal[k] for k in range(3))
    sj = sum(rowj[k]*vv[k]/diagonal[k] for k in range(3))
    schur -= weight*si*sj/denominator
    answer = source_entry(2, i, j)-schur
    emit('adjacent_entry', row=i, column=j,
         num_terms=len(answer.n), den_terms=len(answer.d),
         num_degree=int(answer.n.total_degree()), den_degree=int(answer.d.total_degree()))
    return answer


def inverse(matrix):
    n = len(matrix)
    a = [list(row)+[Rat(int(i == j)) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        value = a[col][col]
        a[col] = [entry/value for entry in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                value = a[i][col]
                a[i] = [entry-value*base for entry, base in zip(a[i], a[col])]
        emit('inverse_pivot', column=col, **profile(a))
    return [row[n:] for row in a]


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def determinant_leibniz(matrix):
    n = len(matrix)
    answer = Rat()
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = Rat((-1)**inversions)
        for i in range(n):
            term *= matrix[i][perm[i]]
        answer += term
    return answer


def coefficient_certificate(value):
    den_value = value.d(1, 1, 1, 1, 1)
    if den_value == 0:
        raise AssertionError('reference denominator unexpectedly zero')
    numerator = value.n if den_value > 0 else -value.n
    digest = hashlib.sha256()
    negative = []
    positive_v_only = False
    count_negative = 0
    for powers, coefficient in numerator.terms():
        digest.update((str(powers)+':'+str(coefficient)+'\n').encode())
        if coefficient < 0:
            count_negative += 1
            if len(negative) < 5:
                negative.append([powers, str(coefficient)])
        if coefficient > 0 and all(exponent == 0 for exponent in powers[:4]):
            positive_v_only = True
    return {'num_terms': len(numerator), 'den_terms': len(value.d),
            'num_degree': int(numerator.total_degree()),
            'den_degree': int(value.d.total_degree()),
            'negative_coefficients': count_negative,
            'negative_examples': negative,
            'positive_v_only': positive_v_only,
            'numerator_sha256': digest.hexdigest(),
            'passed': count_negative == 0 and positive_v_only}


def check_complete_layer():
    """A rational full-layer check of the common shear and scalar CAS path."""
    global q, pool, z, w1, w2
    import importlib.util
    from pathlib import Path
    import sympy as sp
    original = Path(__file__).with_name('2026-11-14-two-exceptional-schur-789f.py')
    spec = importlib.util.spec_from_file_location('r273_physical_check', original)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    q, pool, z, w1, w2 = map(Rat, (3, 4, 4, 9, 25))
    def exact(value):
        return sp.Rational(str(value.n(1, 1, 1, 1, 1)/value.d(1, 1, 1, 1, 1)))
    d0, d1, d2 = [moments(k) for k in range(3)]
    mu = exact(d1[1])
    ee = exact(d2[3]-d1[3])
    ff = exact(d2[2]-d2[3]*d2[1])
    shear = sp.Matrix([[1, 0, 0, 0], [mu, 1, 0, 0], [mu, 0, 1, 0],
                       [ff+2*mu*ee, ee, ee, 1]])
    sign = sp.diag(1, -1, -1, 1)
    actuals = []
    for n in range(3):
        complete = module.full_gram(3, 4, 2, n, sp.Rational(2), sp.Rational(3), sp.Rational(5))
        target = shear.T*sign*complete*sign*shear/(math.factorial(3)**2*4**3)
        actual = sp.Matrix([[exact(value) for value in row] for row in gram(n)])
        assert actual == target
        actuals.append(actual)
    full_difference = actuals[2]-actuals[1]*actuals[0].inv()*actuals[1]
    lazy_difference = sp.Matrix([[exact(adjacent_entry(i, j)) for j in range(4)] for i in range(4)])
    assert full_difference == lazy_difference
    emit('exact_full_layer_check_passed', all_heights=(0, 1, 2),
         common_source_shear=True, complete_adjacent_difference=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stop-after-gram', type=int, choices=(0, 1, 2))
    parser.add_argument('--max-minor', type=int, default=4, choices=(1, 2, 3, 4))
    parser.add_argument('--continue-after-negative', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        check_complete_layer()
        return
    for n in range(3):
        if args.stop_after_gram is not None:
            gram(n)
            if args.stop_after_gram == n:
                emit('profile_complete', last_height=n)
                return
        else:
            raw_gram(n)
    all_passed = True
    for k in range(1, args.max_minor+1):
        minor = determinant_leibniz([[adjacent_entry(i, j) for j in range(k)] for i in range(k)])
        certificate = coefficient_certificate(minor)
        emit('leading_minor', size=k, **certificate)
        all_passed &= certificate['passed']
        if not certificate['passed'] and not args.continue_after_negative:
            emit('inconclusive', reason='coefficient sign criterion did not close')
            return
    emit('coefficient_run_complete', all_passed=all_passed,
         full_four_by_four=args.max_minor == 4)


if __name__ == '__main__':
    main()
