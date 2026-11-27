"""Exact original S1/S2 for three pairs of equal positive Boolean weights.

The first target is S1 on the complete three-dimensional common primitive
source.  The second retains the same source, both crosses and all lower
metrics.  All inverses are on the indicated complete physical group-fixed
layers.  Only small phase / coefficient summaries are printed.  No expanded
matrix, encoded coefficient stream, or reproducible data file is exported.
A failed coefficient-sign test is inconclusive, never a counterexample.
"""
from __future__ import annotations

import signal
import resource
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))

import hashlib
import itertools
import json
import math
import time
from functools import lru_cache
from flint import fmpq, fmpq_mpoly_ctx

CTX = fmpq_mpoly_ctx.get(("U", "V"))
ZERO, ONE = CTX.constant(0), CTX.constant(1)
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
    print(json.dumps({"event": event,
                      "seconds": time.monotonic() - START, **fields},
                     sort_keys=True), flush=True)


U, V = map(Rat, CTX.gens())
x, y = 1 + U + V, 1 + V
weights = (x, y, Rat(1))


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(*matrices):
    a = matrices[0]
    for b in matrices[1:]:
        a = [[sum(a[i][k] * b[k][j] for k in range(len(b)))
              for j in range(len(b[0]))] for i in range(len(a))]
    return a


def ma(a, b, scale=1):
    return [[a[i][j] + scale * b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def ms(a, scale):
    return [[scale * z for z in row] for row in a]


def minor(a, row, col):
    return [[v for j, v in enumerate(rr) if j != col]
            for i, rr in enumerate(a) if i != row]


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j * a[0][j] * determinant(minor(a, 0, j))
               for j in range(len(a)))


def inverse(a, label):
    dd = determinant(a)
    assert dd
    n = len(a)
    if n == 1:
        result = [[1 / dd]]
    else:
        result = [[(-1)**(i+j) * determinant(minor(a, j, i)) / dd
                   for j in range(n)] for i in range(n)]
    # A full exact multiplication, not a numerical inverse check.
    product = mm(a, result)
    assert all(not(product[i][j] - int(i == j))
               for i in range(n) for j in range(n))
    emit("complete_inverse", label=label, dimension=n)
    return result


def symmetric(a, label):
    assert all(not(a[i][j] - a[j][i])
               for i in range(len(a)) for j in range(len(a)))
    emit("same_source_symmetric", label=label, dimension=len(a))


@lru_cache(None)
def configs(level):
    return [p for p in itertools.product(range(3), repeat=3) if sum(p) == level]


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def physical_weight(p):
    return math.prod(math.comb(2, p[i]) for i in range(3)) * \
        weights[0]**p[0] * weights[1]**p[1]


@lru_cache(None)
def full_gram(birth, height):
    """The complete incidence times physical input metric times transpose."""
    target = configs(birth)
    result = [[Rat() for _ in target] for _ in target]
    for source in configs(birth + height):
        p = physical_weight(source)
        row = [math.prod(choose(source[k], target_i[k]) for k in range(3))
               for target_i in target]
        for i in range(len(target)):
            for j in range(i, len(target)):
                result[i][j] += p * row[i] * row[j]
                result[j][i] = result[i][j]
    return result


@lru_cache(None)
def source(birth):
    if birth == 1:
        columns = [
            {(1, 0, 0): 1, (0, 0, 1): -1},
            {(0, 1, 0): 1, (0, 0, 1): -1}]
    elif birth == 2:
        columns = [
            {(2, 0, 0): 1, (1, 0, 1): -2, (0, 0, 2): 1},
            {(1, 1, 0): 1, (1, 0, 1): -1,
             (0, 1, 1): -1, (0, 0, 2): 1},
            {(0, 2, 0): 1, (0, 1, 1): -2, (0, 0, 2): 1}]
    else:
        raise ValueError("only actual birth one/two sources")
    return [[Rat(p.get(row, 0)) for p in columns] for row in configs(birth)]


@lru_cache(None)
def gram(birth, height):
    e = source(birth)
    if height == 0:
        return [[sum(e[k][i] * e[k][j] / physical_weight(row)
                     for k, row in enumerate(configs(birth)))
                 for j in range(len(e[0]))] for i in range(len(e[0]))]
    assert birth == 1
    fi = inverse(full_gram(birth, height),
                 "full-lower-height-" + str(height))
    return mm(transpose(e), fi, e)


def coefficients(value, label):
    """Every denominator is a factor of nonzero physical positive determinants."""
    at_origin = value.d(0, 0)
    assert at_origin, "positive actual metric denominator vanished at equal weights"
    num = value.n if at_origin > 0 else -value.n
    digest = hashlib.sha256()
    negatives, example = 0, []
    for exponents, c in sorted(num.terms()):
        digest.update((str(tuple(exponents)) + ":" + str(c) + "\n").encode())
        if c < 0:
            negatives += 1
            if len(example) < 3:
                example.append([list(exponents), str(c)])
    constant = num(0, 0)
    passed = not negatives and constant > 0
    record = {"label": label, "passed": bool(passed),
              "numerator_terms": len(num), "denominator_terms": len(value.d),
              "numerator_degree": int(num.total_degree()),
              "denominator_degree": int(value.d.total_degree()),
              "negative_coefficients": negatives,
              "negative_examples": example, "constant": str(constant),
              "numerator_sha256": digest.hexdigest()}
    emit("leading_minor", **record)
    return passed


def certify_matrix(a, label):
    symmetric(a, label)
    all_passed = True
    for k in range(1, len(a) + 1):
        small = [row[:k] for row in a[:k]]
        passed = coefficients(determinant(small), label + "-" + str(k))
        all_passed = all_passed and passed
    return all_passed


def assert_original_sources(e1, e2, bridge):
    # Exact incidence and exact cubic derivative in aggregate coordinates.
    target1, target2 = configs(1), configs(2)
    dd = [[Rat(math.prod(choose(ii[k], oo[k]) for k in range(3)))
           for ii in target2] for oo in target1]
    zero = mm(dd, e2)
    assert all(not z for row in zero for z in row)
    assert all(not sum(e1[i][j] for i in range(len(e1)))
               for j in range(2))
    cubic = []
    for oo in target1:
        line = []
        for ii in target2:
            gap = tuple(ii[k] - oo[k] for k in range(3))
            if min(gap) >= 0 and sum(gap) == 1:
                k = gap.index(1)
                line.append(ii[k] * weights[k])
            else:
                line.append(Rat())
        cubic.append(line)
    actual, intended = mm(cubic, e2), mm(e1, bridge)
    assert all(not(a-b) for ra, rb in zip(actual, intended)
               for a, b in zip(ra, rb))
    emit("actual_sources_and_cubic_bridge", upper_dimension=3,
         lower_dimension=2, complete_layer_dimensions=[6, 3])


def main():
    e1, e2 = source(1), source(2)
    bridge = [[2*(x-1), y-1, Rat()],
              [Rat(), x-1, 2*(y-1)]]
    assert_original_sources(e1, e2, bridge)
    u0 = gram(2, 0)
    ui = inverse(u0, "actual-upper-source-metric")
    l0, l1, l2, l3 = [gram(1, j) for j in range(4)]
    l2i, l3i = inverse(l2, "lower-Gamma2"), inverse(l3, "lower-Gamma3")
    target2 = configs(2)
    se = [[e2[i][j] / physical_weight(row) for j in range(3)]
          for i, row in enumerate(target2)]
    total = 2*x + 2*y + 2
    occupation = [total - 2*sum(row[k]*weights[k] for k in range(3))
                  for row in target2]
    hhat = [[sum(e2[k][i]*se[k][j]*occupation[k] for k in range(6))
             for j in range(3)] for i in range(3)]
    fhat = mm(transpose(se), full_gram(2, 2), se)
    bt = transpose(bridge)
    m = mm(bt, l2, bridge)
    n = mm(bt, l2, l3i, l2, bridge)
    deep = [[2*(x-1)**2, 2*(x-1)*(y-1), 2*(y-1)**2]]
    e4 = sum(physical_weight(row) for row in configs(4))
    s1 = ma(ma(ma(mm(hhat, ui, hhat), fhat, -1),
               mm(m, ui, m), -1), ms(n, 2))
    s1 = ma(s1, ms(mm(transpose(deep), deep), 1/(4*e4)))
    s1_passed = certify_matrix(s1, "S1-original-three-tower")
    emit("S1_complete", all_passed=s1_passed)

    # Same U0 and lower source; the exact Cbar = U0 H1^{-1} U0 identity.
    c = ma(hhat, m, -1)
    ci = inverse(c, "actual-upper-first-precision-form")
    yy = mm(ui, bt, l2)
    zz = mm(bt, l2, l3i, l2)
    rr = ma(mm(c, yy), zz)
    dlow = ma(l0, mm(l1, l2i, l1), -1)
    s2 = ma(dlow, mm(transpose(rr), ci, rr), -Rat(1)/4)
    s2_passed = certify_matrix(s2, "S2-original-both-crosses")
    emit("COMPLETE_ORIGINAL_JOINT_RESULT", S1_all_passed=s1_passed,
         S2_all_passed=s2_passed, all_passed=s1_passed and s2_passed,
         coefficient_failure_is_only_inconclusive=True)
    signal.alarm(0)


if __name__ == "__main__":
    main()
