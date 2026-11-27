"""The remaining five ORIGINAL S1 principal minors for one equal pair.

The first original minor is already proved on all five closed group-order
chambers. It is used only as the first Schur pivot, never retested. All actual
physical source metrics, complete inverses and cross terms are retained.
For each new original minor 2,...,6, all five group-order chambers are tested
by exact coefficients and bounded local rational square certificates.
Only small ordinary summaries are printed; no expanded data is exported.
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

CTX = fmpq_mpoly_ctx.get(("U", "V", "W", "Z"))
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


U, V, W, Z = map(Rat, CTX.gens())
single_weights = (U + V + W + Z, V + W + Z, W + Z, Z)
weights = single_weights + (Rat(1),)
capacities = (1, 1, 1, 1, 2)
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
    # Exact rational Gauss--Jordan, followed by actual multiplication back.
    # No factorial cofactor expansion and no characteristic-coefficient gate.
    n = len(a)
    work = [list(a[i]) + [Rat(int(i == j)) for j in range(n)]
            for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if work[i][k]), None)
        assert pivot is not None, "actual Gram is not invertible"
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
        pp = work[k][k]
        work[k] = [value / pp for value in work[k]]
        for i in range(n):
            if i != k and work[i][k]:
                factor = work[i][k]
                work[i] = [aa - factor*bb
                           for aa, bb in zip(work[i], work[k])]
    result = [row[n:] for row in work]
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
    unit = [tuple(int(k == i) for k in range(NGROUP))
            for i in range(NGROUP)]
    def plus(a, b):
        return tuple(x+y for x, y in zip(a, b))
    if birth == 1:
        columns = [{unit[i]: 1, unit[-1]: -1} for i in range(4)]
    elif birth == 2:
        # Complete source: (Xi-J)(Xj-J), 0 <= i < j < 4.
        columns = [{plus(unit[i], unit[j]): 1,
                    plus(unit[i], unit[-1]): -1,
                    plus(unit[j], unit[-1]): -1,
                    plus(unit[-1], unit[-1]): 1}
                   for i, j in itertools.combinations(range(4), 2)]
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


CHAMBER_CTX = fmpq_mpoly_ctx.get(("A", "B", "C", "D"))
HOM_CTX = fmpq_mpoly_ctx.get(("u", "v", "w", "z", "tau"))


def ordered_chambers():
    # Five positive group values, normalized by their common minimum.
    # The equal pair occupies position k. The other four groups are single.
    values = [CHAMBER_CTX.constant(1)]
    for gap in CHAMBER_CTX.gens():
        values.append(values[-1] + gap)
    for k in range(5):
        tau = values[k]
        singles = [values[j] for j in reversed(range(5)) if j != k]
        # Original (U,V,W,Z) = numerators / tau, exactly.
        numerators = [singles[j] - singles[j+1] for j in range(3)]
        numerators.append(singles[3])
        assert all(p(0, 0, 0, 0) == (1 if j == 3 else 0)
                   for j, p in enumerate(numerators))
        assert tau(0, 0, 0, 0) == 1
        yield k, numerators, tau


def polynomial_digest(poly):
    digest = hashlib.sha256()
    for exponents, coefficient in sorted(poly.terms()):
        exponent = tuple(int(e) for e in exponents)
        digest.update((str(exponent)+":"+str(coefficient)+"\n").encode())
    return digest.hexdigest()


def square_source(pullback, pair_position, minor_order):
    # Only a small readable exact square proof may be emitted, never a
    # coefficient table. The constant is reserved, ensuring strictness.
    work = {tuple(int(e) for e in exponents): coefficient
            for exponents, coefficient in pullback.terms()}
    zeros = (0, 0, 0, 0)
    constant = work.get(zeros, 0)
    negative = sorted(e for e, coefficient in work.items() if coefficient < 0)
    emit("remaining_chamber_original", pair_position=pair_position, minor_order=minor_order,
         numerator_degree=int(pullback.total_degree()),
         numerator_terms=len(pullback), constant=str(constant),
         negative_coefficients=len(negative),
         numerator_sha256=polynomial_digest(pullback))
    if len(negative) > 32:
        emit("INCONCLUSIVE_LOCAL_SQUARE_BUDGET", pair_position=pair_position, minor_order=minor_order,
             negative_coefficients=len(negative), fixed_max_squares=32,
             negative_examples=[[list(e), str(work[e])] for e in negative[:3]])
        return False
    directions = [d for d in itertools.product(range(-2, 3), repeat=4)
                  if any(d) and next(x for x in d if x) > 0]
    squares = CHAMBER_CTX.constant(0)
    for step, center in enumerate(negative, 1):
        beta = -work[center]
        best = None
        for direction in directions:
            upper = tuple(center[i]+direction[i] for i in range(4))
            lower = tuple(center[i]-direction[i] for i in range(4))
            if min(upper) < 0 or min(lower) < 0 or upper == zeros or lower == zeros:
                continue
            available_u, available_v = work.get(upper, 0), work.get(lower, 0)
            if available_u <= 0 or available_v <= 0:
                continue
            product = available_u*available_v
            if 4*product < beta*beta:
                continue
            if best is None or product > best[0]:
                best = (product, upper, lower, available_u, available_v)
        if best is None:
            emit("INCONCLUSIVE_LOCAL_SQUARE_SOURCE", pair_position=pair_position, minor_order=minor_order,
                 completed_squares=step-1, failed_center=list(center),
                 failed_coefficient=str(-beta), radius=2)
            return False
        _, upper, lower, available_u, available_v = best
        if available_u >= beta/2 and available_v >= beta/2:
            aa = cc = beta/2
        elif available_u < beta/2:
            aa = available_u
            cc = beta*beta/(4*aa)
        else:
            cc = available_v
            aa = beta*beta/(4*cc)
        assert 0 < aa <= available_u and 0 < cc <= available_v
        assert 4*aa*cc == beta*beta
        base = tuple(min(upper[i], lower[i]) for i in range(4))
        pos = tuple((upper[i]-base[i])//2 for i in range(4))
        neg = tuple((lower[i]-base[i])//2 for i in range(4))
        assert all(base[i]+pos[i]+neg[i] == center[i] for i in range(4))
        ratio = beta/(2*aa)
        factor = (CHAMBER_CTX.term(coeff=1, exp_vec=pos)
                  - ratio*CHAMBER_CTX.term(coeff=1, exp_vec=neg))
        square = aa*CHAMBER_CTX.term(coeff=1, exp_vec=base)*factor**2
        work[upper] -= aa
        work[lower] -= cc
        work[center] = 0
        squares += square
        if step <= 3:
            emit("exact_rational_square_example", pair_position=pair_position,
                 minor_order=minor_order, step=step,
                 center=list(center), beta=str(beta), upper=list(upper),
                 lower=list(lower), a=str(aa), c=str(cc))
    residual = CHAMBER_CTX.from_dict({e: coefficient
                                     for e, coefficient in work.items()
                                     if coefficient})
    assert pullback == residual+squares, "full original polynomial return failed"
    negative_after = sum(1 for _, coefficient in residual.terms() if coefficient < 0)
    assert negative_after == 0
    assert residual(0, 0, 0, 0) == constant
    passed = constant > 0
    emit("EXACT_ORIGINAL_POLYNOMIAL_SQUARE_RETURN", pair_position=pair_position, minor_order=minor_order,
         passed=bool(passed), full_identity_checked=True,
         squares=len(negative), residual_terms=len(residual),
         residual_negative_coefficients=negative_after,
         strictly_positive_reserved_constant=str(constant),
         residual_sha256=polynomial_digest(residual))
    return bool(passed)


def certify_new_minor(value, minor_order):
    assert 2 <= minor_order <= 6
    reference = value.d(0, 0, 0, 1)
    assert reference, "an original metric denominator vanished at equal weights"
    num = value.n if reference > 0 else -value.n
    degree = int(num.total_degree())
    homogeneous = HOM_CTX.from_dict({
        tuple(int(e) for e in exponents)
        + (degree-sum(int(e) for e in exponents),): coefficient
        for exponents, coefficient in num.terms()})
    emit("new_original_principal_minor", minor_order=minor_order,
         numerator_degree=degree, numerator_terms=len(num),
         denominator_degree=int(value.d.total_degree()),
         denominator_terms=len(value.d),
         numerator_sha256=polynomial_digest(num))
    for k, numerators, tau in ordered_chambers():
        pullback = homogeneous.compose(*numerators, tau)
        if not square_source(pullback, k, minor_order):
            emit("INCONCLUSIVE_NEW_ORIGINAL_MINOR", minor_order=minor_order,
                 first_unpaid_chamber=k, later_chambers_not_computed=4-k,
                 later_original_minors_not_computed=6-minor_order,
                 no_original_counterexample=True)
            return False
    emit("NEW_ORIGINAL_PRINCIPAL_MINOR_ALL_CHAMBERS_POSITIVE",
         minor_order=minor_order)
    return True


def certify_remaining_matrix(a, label):
    symmetric(a, label)

    @lru_cache(None)
    def schur_entry(level, i, j):
        # Demand only entries of the new leading block. No untested later
        # rows are reduced before the current original minor is certified.
        if i > j:
            return schur_entry(level, j, i)
        if level == 0:
            return a[i][j]
        k = level-1
        pivot = schur_entry(k, k, k)
        assert pivot, "identically zero original Schur pivot"
        return (schur_entry(k, i, j)
                - schur_entry(k, i, k)*schur_entry(k, k, j)/pivot)

    leading = Rat(1)
    for k in range(len(a)):
        pivot = schur_entry(k, k, k)
        assert pivot, "identically zero original Schur pivot"
        leading *= pivot
        if k == 0:
            emit("FIRST_MINOR_USED_ONLY_AS_PAID_PIVOT",
                 first_minor_positivity_not_retested=True)
        elif not certify_new_minor(leading, k+1):
            return False
    return True

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
    pairs = list(itertools.combinations(range(4), 2))
    delta = [value - 1 for value in single_weights]
    bridge = [[delta[j] if row == i else delta[i] if row == j else Rat()
               for i, j in pairs] for row in range(4)]
    deep = [[2*delta[i]*delta[j] for i, j in pairs]]
    assert_original_sources(e1, e2, bridge, deep)
    u0 = gram(2, 0)
    ui = inverse(u0, "actual-upper-source-metric")
    l2, l3 = gram(1, 2), gram(1, 3)
    l3i = inverse(l3, "lower-Gamma3")
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
    s1_passed = certify_remaining_matrix(s1, "S1-original-three-tower-remaining-minors")
    emit("S1_REMAINING_ORIGINAL_MINORS_COMPLETE", all_new_minors_passed=s1_passed)

    emit("COMPLETE_ORIGINAL_S1_WITH_PAID_FIRST_MINOR" if s1_passed else
         "REMAINING_ORIGINAL_S1_MINORS_INCONCLUSIVE", S1_all_passed=s1_passed,
         whole_upper_dimension=9, new_fixed_dimension=6,
         original_full_Gram_dimensions=[11, 5],
         S2_not_tested=True,
         coefficient_failure_is_only_inconclusive=True,
         first_original_minor_previously_proved_not_retested=True,
         new_original_minor_orders=[2, 3, 4, 5, 6],
         no_expanded_data_or_encoding_exported=True)
    signal.alarm(0)


if __name__ == "__main__":
    main()
