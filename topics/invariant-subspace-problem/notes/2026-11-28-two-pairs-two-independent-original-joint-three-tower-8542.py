"""Original joint S1/S2 for two equal pairs and two independent positive weights.

The new target is the original four-dimensional upper primitive source and
three-dimensional lower source.  All full lower Grams, actual metrics, the
deep vacuum tower, and both S2 cross terms are retained.  This is not a
replay of the six-independent-weight characteristic gate or of the known
ordinary first edge for this family.

Only small mathematical summaries are printed.  No expanded matrix,
encoded coefficient stream, or reproducible data output file is exported.
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
from flint import fmpq_mpoly_ctx

CTX = fmpq_mpoly_ctx.get(("U", "V", "W"))
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


U, V, W = map(Rat, CTX.gens())
x, y, z = 1 + U, V + W, W
weights = (x, y, z, Rat(1))
capacities = (2, 1, 1, 2)
NGROUP = len(capacities)


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
    return [[scale * value for value in row] for row in a]


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
    return [p for p in itertools.product(
        *(range(c + 1) for c in capacities)) if sum(p) == level]


def choose(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def physical_weight(p):
    result = Rat(math.prod(math.comb(capacities[i], p[i])
                           for i in range(NGROUP)))
    for i in range(NGROUP):
        result *= weights[i]**p[i]
    return result


@lru_cache(None)
def full_gram(birth, height):
    target = configs(birth)
    result = [[Rat() for _ in target] for _ in target]
    for src in configs(birth + height):
        p = physical_weight(src)
        row = [math.prod(choose(src[k], target_i[k]) for k in range(NGROUP))
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
            {(1, 0, 0, 0): 1, (0, 0, 0, 1): -1},
            {(0, 1, 0, 0): 1, (0, 0, 0, 1): -1},
            {(0, 0, 1, 0): 1, (0, 0, 0, 1): -1}]
    elif birth == 2:
        # (X-J)^2, (X-J)(Y-J), (X-J)(Z-J), (Y-J)(Z-J).
        columns = [
            {(2, 0, 0, 0): 1, (1, 0, 0, 1): -2, (0, 0, 0, 2): 1},
            {(1, 1, 0, 0): 1, (1, 0, 0, 1): -1,
             (0, 1, 0, 1): -1, (0, 0, 0, 2): 1},
            {(1, 0, 1, 0): 1, (1, 0, 0, 1): -1,
             (0, 0, 1, 1): -1, (0, 0, 0, 2): 1},
            {(0, 1, 1, 0): 1, (0, 1, 0, 1): -1,
             (0, 0, 1, 1): -1, (0, 0, 0, 2): 1}]
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
    """The connected original domain is U,V >= 0, W > 0."""
    reference = value.d(0, 0, 1)
    assert reference, "a positive actual metric denominator vanished"
    num = value.n if reference > 0 else -value.n
    digest = hashlib.sha256()
    negatives, examples, axis_terms, axis_examples = 0, [], 0, []
    for exponents, c in sorted(num.terms()):
        digest.update((str(tuple(exponents)) + ":" + str(c) + "\n").encode())
        if c < 0:
            negatives += 1
            if len(examples) < 3:
                examples.append([list(exponents), str(c)])
        if exponents[0] == 0 and exponents[1] == 0 and c > 0:
            axis_terms += 1
            if len(axis_examples) < 3:
                axis_examples.append([int(exponents[2]), str(c)])
    # A positive W-only term stays strictly positive on every allowed W > 0.
    passed = not negatives and axis_terms > 0
    emit("leading_minor", label=label, passed=bool(passed),
         numerator_terms=len(num), denominator_terms=len(value.d),
         numerator_degree=int(num.total_degree()),
         denominator_degree=int(value.d.total_degree()),
         negative_coefficients=negatives, negative_examples=examples,
         strict_axis_terms=axis_terms, strict_axis_examples=axis_examples,
         numerator_sha256=digest.hexdigest())
    return passed


def certify_matrix(a, label):
    symmetric(a, label)
    all_passed = True
    for k in range(1, len(a) + 1):
        passed = coefficients(determinant([row[:k] for row in a[:k]]),
                              label + "-" + str(k))
        all_passed = all_passed and passed
    return all_passed


def assert_original_sources(e1, e2, bridge, deep):
    target1, target2 = configs(1), configs(2)
    dd = [[Rat(math.prod(choose(ii[k], oo[k]) for k in range(NGROUP)))
           for ii in target2] for oo in target1]
    assert all(not value for row in mm(dd, e2) for value in row)
    assert all(not sum(e1[i][j] for i in range(len(e1)))
               for j in range(len(e1[0])))
    cubic = []
    for oo in target1:
        line = []
        for ii in target2:
            gap = tuple(ii[k] - oo[k] for k in range(NGROUP))
            if min(gap) >= 0 and sum(gap) == 1:
                k = gap.index(1)
                line.append(ii[k] * weights[k])
            else:
                line.append(Rat())
        cubic.append(line)
    actual, intended = mm(cubic, e2), mm(e1, bridge)
    assert all(not(a-b) for ra, rb in zip(actual, intended)
               for a, b in zip(ra, rb))
    last = [[sum(row[k] * weights[k] for k in range(NGROUP))
             for row in target1]]
    actual_deep = mm(last, cubic, e2)
    assert all(not(a-b) for a, b in zip(actual_deep[0], deep[0]))
    emit("actual_sources_and_two_cubic_bridges",
         upper_dimension=len(e2[0]), lower_dimension=len(e1[0]),
         complete_layer_dimensions=[len(target2), len(target1)])


def main():
    e1, e2 = source(1), source(2)
    updim = len(e2[0])
    bridge = [[2*(x-1), y-1, z-1, Rat()],
              [Rat(), x-1, Rat(), z-1],
              [Rat(), Rat(), x-1, y-1]]
    deep = [[2*(x-1)**2, 2*(x-1)*(y-1), 2*(x-1)*(z-1),
             2*(y-1)*(z-1)]]
    assert_original_sources(e1, e2, bridge, deep)
    u0 = gram(2, 0)
    ui = inverse(u0, "actual-upper-source-metric")
    l0, l1, l2, l3 = [gram(1, j) for j in range(4)]
    l2i, l3i = inverse(l2, "lower-Gamma2"), inverse(l3, "lower-Gamma3")
    target2 = configs(2)
    se = [[e2[i][j] / physical_weight(row) for j in range(updim)]
          for i, row in enumerate(target2)]
    total = sum(capacities[k] * weights[k] for k in range(NGROUP))
    occupation = [total - 2*sum(row[k]*weights[k] for k in range(NGROUP))
                  for row in target2]
    hhat = [[sum(e2[k][i]*se[k][j]*occupation[k]
                  for k in range(len(target2)))
             for j in range(updim)] for i in range(updim)]
    fhat = mm(transpose(se), full_gram(2, 2), se)
    bt = transpose(bridge)
    m = mm(bt, l2, bridge)
    n = mm(bt, l2, l3i, l2, bridge)
    e4 = sum(physical_weight(row) for row in configs(4))
    s1 = ma(ma(ma(mm(hhat, ui, hhat), fhat, -1),
               mm(m, ui, m), -1), ms(n, 2))
    s1 = ma(s1, ms(mm(transpose(deep), deep), 1/(4*e4)))
    emit("S1_actual_matrix_ready", dimension=updim)
    s1_passed = certify_matrix(s1, "S1-original-three-tower")
    emit("S1_complete", all_passed=s1_passed)

    c = ma(hhat, m, -1)
    ci = inverse(c, "actual-upper-first-precision-form")
    yy = mm(ui, bt, l2)
    zz = mm(bt, l2, l3i, l2)
    rr = ma(mm(c, yy), zz)
    dlow = ma(l0, mm(l1, l2i, l1), -1)
    s2 = ma(dlow, mm(transpose(rr), ci, rr), -Rat(1)/4)
    emit("S2_actual_matrix_ready", dimension=len(e1[0]))
    s2_passed = certify_matrix(s2, "S2-original-both-crosses")
    emit("COMPLETE_ORIGINAL_JOINT_RESULT", S1_all_passed=s1_passed,
         S2_all_passed=s2_passed, all_passed=s1_passed and s2_passed,
         coefficient_failure_is_only_inconclusive=True)
    signal.alarm(0)


if __name__ == "__main__":
    main()
