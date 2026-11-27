"""Original remaining three-dimensional S1 Schur spectrum in leaf moments.

The star block is ALREADY positive. The new target is the three coefficients
of det(t*G+S)/det(G) for the original remaining Schur form S and the original
triangle metric G. Three distinct leaf weights permit companion coordinates;
their Vandermonde factors cancel in this invariant ratio. Collision points
are covered through the original continuous forms, never by pretending that
a degenerate moment basis is invertible. All physical layers, lower complete
inverses and both cross terms are retained. No old leading-minor positivity
gate is rerun. Only small ordinary summaries are printed, with no data files.
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

CTX = fmpq_mpoly_ctx.get(("a", "s", "p", "q"))
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



a, s, p, q = map(Rat, CTX.gens())
CHAMBER_CTX = fmpq_mpoly_ctx.get(("A", "B", "C", "D"))
HOM_CTX = fmpq_mpoly_ctx.get(("a", "s", "p", "q", "tau"))


def eye(n):
    return [[Rat(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Rat() for _ in range(m)] for _ in range(n)]


@lru_cache(None)
def power_sum(n):
    if n == -1:
        return p/q
    if n == 0:
        return Rat(3)
    if n == 1:
        return s
    if n == 2:
        return s*s-2*p
    assert n >= 3
    return s*power_sum(n-1)-p*power_sum(n-2)+q*power_sum(n-3)


VROW = [[power_sum(i) for i in range(3)]]
E0COL = [[Rat(1)], [Rat()], [Rat()]]
COMPANION = [[Rat(), Rat(), q], [Rat(1), Rat(), -p],
             [Rat(), Rat(1), s]]
PINC = ma(mm(E0COL, VROW), eye(3), -1)
HMINUS = [[power_sum(i+j-1) for j in range(3)] for i in range(3)]
HPLUS = [[power_sum(i+j+1) for j in range(3)] for i in range(3)]


def leaf_dimension(l):
    return 3 if l in (1, 2) else 1


@lru_cache(None)
def layer(level):
    ans, offset = [], 0
    for epsilon in range(2):
        for j in range(3):
            for l in range(4):
                if epsilon+j+l == level:
                    size = leaf_dimension(l)
                    ans.append(((epsilon, j, l), offset, size))
                    offset += size
    return ans


def dimension(level):
    return sum(size for _, _, size in layer(level))


def offsets(level):
    return {kind: offset for kind, offset, _ in layer(level)}


def put_block(target, row, col, block, scale=1):
    for i in range(len(block)):
        for j in range(len(block[0])):
            target[row+i][col+j] += scale*block[i][j]


@lru_cache(None)
def down(level, cubic=False):
    target = zeros(dimension(level-1), dimension(level))
    rows = offsets(level-1)
    if cubic:
        leaf_maps = {
            1: mm(VROW, COMPANION),
            2: ma(ma(ms(PINC, s), mm(COMPANION, PINC), -1),
                  mm(PINC, COMPANION), -1),
            3: mm(COMPANION, E0COL)}
    else:
        leaf_maps = {1: VROW, 2: PINC, 3: E0COL}
    for (epsilon, j, l), col, size in layer(level):
        if epsilon:
            put_block(target, rows[(0, j, l)], col, eye(size),
                      a if cubic else 1)
        if j:
            put_block(target, rows[(epsilon, j-1, l)], col, eye(size), j)
        if l:
            put_block(target, rows[(epsilon, j, l-1)], col, leaf_maps[l])
    return target


@lru_cache(None)
def leaf_metric(l):
    if l == 0:
        return [[Rat(1)]]
    if l == 1:
        return HMINUS
    if l == 2:
        return ms(HPLUS, 1/q)
    return [[1/q]]


@lru_cache(None)
def leaf_inverse_metric(l):
    if l == 0:
        return [[Rat(1)]]
    if l == 1:
        return inverse(HMINUS, "distinct-leaf-one-physical-metric")
    if l == 2:
        return ms(inverse(HPLUS, "distinct-leaf-two-physical-metric"), q)
    return [[q]]


@lru_cache(None)
def metric(level, inverted=False):
    target = zeros(dimension(level), dimension(level))
    for (epsilon, j, l), offset, size in layer(level):
        scale = a**epsilon*math.comb(2, j)
        if inverted:
            put_block(target, offset, offset, leaf_inverse_metric(l), scale)
        else:
            put_block(target, offset, offset, leaf_metric(l), 1/scale)
    return target


@lru_cache(None)
def divided_down(birth, height):
    ans = eye(dimension(birth))
    for level in range(birth+1, birth+height+1):
        ans = mm(ans, down(level))
    return ms(ans, Rat(1)/math.factorial(height))


@lru_cache(None)
def complete_gram(birth, height):
    aa = divided_down(birth, height)
    return mm(aa, metric(birth+height, True), transpose(aa))


def original_sources():
    # Lower coordinates: one head-minus-pair scalar, then three leaf moments.
    e1 = zeros(dimension(1), 4)
    rows1 = offsets(1)
    put_block(e1, rows1[(1, 0, 0)], 0, [[Rat(1)]])
    put_block(e1, rows1[(0, 0, 1)], 1, eye(3))
    put_block(e1, rows1[(0, 1, 0)], 0, [[Rat(-1)]])
    put_block(e1, rows1[(0, 1, 0)], 1, VROW, -1)

    # Upper coordinates: star_i=(X_head-J)(X_i-J), followed by
    # triangle_i=(X_j-J)(X_k-J), where {i,j,k} is the leaf set.
    e2 = zeros(dimension(2), 6)
    rows2 = offsets(2)
    put_block(e2, rows2[(1, 0, 1)], 0, eye(3))
    put_block(e2, rows2[(0, 0, 2)], 3, eye(3))
    put_block(e2, rows2[(0, 1, 1)], 0, eye(3), -1)
    put_block(e2, rows2[(0, 1, 1)], 3, PINC, -1)
    put_block(e2, rows2[(1, 1, 0)], 0, VROW, -1)
    put_block(e2, rows2[(0, 2, 0)], 0, VROW)
    put_block(e2, rows2[(0, 2, 0)], 3, VROW)
    return e1, e2


def actual_cubic_bridges(e1, e2):
    vm = mm(VROW, ma(COMPANION, eye(3), -1))
    bridge = zeros(4, 6)
    put_block(bridge, 0, 0, vm)
    put_block(bridge, 1, 0, eye(3), a-1)
    tri = ma(ma(ms(PINC, s-1), mm(COMPANION, PINC), -1),
             mm(PINC, COMPANION), -1)
    put_block(bridge, 1, 3, tri)
    bottom = [[a-1] + vm[0]]
    deep = mm(bottom, bridge)
    assert all(not value for row in mm(down(1), e1) for value in row)
    assert all(not value for row in mm(down(2), e2) for value in row)
    assert all(not(aa-bb)
               for ra, rb in zip(mm(down(2, True), e2), mm(e1, bridge))
               for aa, bb in zip(ra, rb))
    assert all(not(aa-bb)
               for aa, bb in zip(mm(down(1, True), down(2, True), e2)[0],
                                 deep[0]))
    emit("actual_companion_sources_and_both_cubic_bridges",
         complete_layer_dimensions=[dimension(k) for k in range(7)],
         upper_source_dimension=6, lower_source_dimension=4)
    return bridge, deep


def occupation_operator(level):
    target = zeros(dimension(level), dimension(level))
    for (epsilon, j, l), offset, size in layer(level):
        if l == 0:
            leaf = [[Rat()]]
        elif l == 1:
            leaf = COMPANION
        elif l == 2:
            leaf = ma(ms(eye(3), s), COMPANION, -1)
        else:
            leaf = [[s]]
        block = ma(ms(eye(size), epsilon*a+j), leaf)
        put_block(target, offset, offset, block)
    return target


def split3(a6, row, col):
    return [rr[col:col+3] for rr in a6[row:row+3]]


def parameter_chambers():
    values = [CHAMBER_CTX.constant(1)]
    for gap in CHAMBER_CTX.gens():
        values.append(values[-1]+gap)
    for k in range(5):
        tau = values[k]
        singles = [values[j] for j in reversed(range(5)) if j != k]
        head, leaves = singles[0], singles[1:]
        es = sum(leaves, CHAMBER_CTX.constant(0))
        ep = sum((leaves[i]*leaves[j] for i in range(3) for j in range(i+1, 3)),
                 CHAMBER_CTX.constant(0))
        eq = leaves[0]*leaves[1]*leaves[2]
        yield k, [head, es, ep, eq], tau

def polynomial_digest(poly):
    digest = hashlib.sha256()
    for exponents, coefficient in sorted(poly.terms()):
        exponent = tuple(int(e) for e in exponents)
        digest.update((str(exponent)+":"+str(coefficient)+"\n").encode())
    return digest.hexdigest()


def square_source(pullback, pair_position, coefficient_order):
    # Only a small readable exact square proof may be emitted, never a
    # coefficient table. The constant is reserved, ensuring strictness.
    work = {tuple(int(e) for e in exponents): coefficient
            for exponents, coefficient in pullback.terms()}
    zeros = (0, 0, 0, 0)
    constant = work.get(zeros, 0)
    negative = sorted(e for e, coefficient in work.items() if coefficient < 0)
    emit("remaining_chamber_original", pair_position=pair_position, coefficient_order=coefficient_order,
         numerator_degree=int(pullback.total_degree()),
         numerator_terms=len(pullback), constant=str(constant),
         negative_coefficients=len(negative),
         numerator_sha256=polynomial_digest(pullback))
    if len(negative) > 32:
        emit("INCONCLUSIVE_LOCAL_SQUARE_BUDGET", pair_position=pair_position, coefficient_order=coefficient_order,
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
            emit("INCONCLUSIVE_LOCAL_SQUARE_SOURCE", pair_position=pair_position, coefficient_order=coefficient_order,
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
                 coefficient_order=coefficient_order, step=step,
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
    emit("EXACT_ORIGINAL_POLYNOMIAL_SQUARE_RETURN", pair_position=pair_position, coefficient_order=coefficient_order,
         passed=bool(passed), full_identity_checked=True,
         squares=len(negative), residual_terms=len(residual),
         residual_negative_coefficients=negative_after,
         strictly_positive_reserved_constant=str(constant),
         residual_sha256=polynomial_digest(residual))
    return bool(passed)



def certify_schur_spectral_coefficient(value, coefficient_order):
    # The original continuous determinant ratio is regular also when all
    # leaf weights coincide. No Hankel positivity is asserted at collisions.
    reference = value.d(1, 3, 3, 1)
    assert reference, "uncancelled coordinate pole at a positive collision"
    num = value.n if reference > 0 else -value.n
    weight = (1, 1, 2, 3)
    degree = max(sum(weight[i]*int(e[i]) for i in range(4))
                 for e, _ in num.terms())
    homogeneous = HOM_CTX.from_dict({
        tuple(int(e) for e in exponent)
        + (degree-sum(weight[i]*int(exponent[i]) for i in range(4)),): coefficient
        for exponent, coefficient in num.terms()})
    emit("original_relative_schur_spectral_coefficient",
         coefficient_order=coefficient_order,
         numerator_degree=int(num.total_degree()), numerator_weighted_degree=degree,
         numerator_terms=len(num), denominator_terms=len(value.d),
         equal_weight_denominator=str(reference),
         numerator_sha256=polynomial_digest(num))
    for k, numerators, tau in parameter_chambers():
        pullback = homogeneous.compose(*numerators, tau)
        if not square_source(pullback, k, coefficient_order):
            emit("INCONCLUSIVE_NEW_SCHUR_SPECTRAL_SOURCE",
                 coefficient_order=coefficient_order, failed_chamber=k,
                 later_chambers_not_computed=4-k,
                 later_spectral_coefficients_not_computed=3-coefficient_order)
            return False
    emit("ORIGINAL_SCHUR_SPECTRAL_COEFFICIENT_ALL_CHAMBERS_POSITIVE",
         coefficient_order=coefficient_order)
    return True


def main():
    e1, e2 = original_sources()
    bridge, deep = actual_cubic_bridges(e1, e2)
    w2 = metric(2)
    u0 = mm(transpose(e2), w2, e2)
    ui = inverse(u0, "full-original-upper-six-source-metric")
    lower = {}
    for height in (2, 3):
        full_inverse = inverse(complete_gram(1, height),
                               "full-original-lower-five-gram-"+str(height))
        lower[height] = mm(transpose(e1), full_inverse, e1)
    l2, l3 = lower[2], lower[3]
    l3i = inverse(l3, "original-four-source-Gamma3")
    hfull = ma(ms(eye(dimension(2)), a+s+2), occupation_operator(2), -2)
    hhat = mm(transpose(e2), w2, hfull, e2)
    fhat = mm(transpose(e2), w2, complete_gram(2, 2), w2, e2)
    bt = transpose(bridge)
    m = mm(bt, l2, bridge)
    n = mm(bt, l2, l3i, l2, bridge)
    e4 = a*s+(2*a+1)*p+(a+2)*q
    assert not(complete_gram(0, 4)[0][0]-e4)
    original = ma(ma(ma(mm(hhat, ui, hhat), fhat, -1),
                     mm(m, ui, m), -1), ms(n, 2))
    original = ma(original, ms(mm(transpose(deep), deep), 1/(4*e4)))
    symmetric(original, "same-original-six-source-S1-in-leaf-moments")
    emit("ORIGINAL_S1_COMPANION_MATRIX_READY",
         old_leading_minors_not_retested=True)
    star, cross, triangle = (split3(original, 0, 0),
                             split3(original, 0, 3),
                             split3(original, 3, 3))
    star_inverse = inverse(star, "already-positive-original-star-three-block")
    schur = ma(triangle, mm(transpose(cross), star_inverse, cross), -1)
    g = split3(u0, 3, 3)
    gi = inverse(g, "original-positive-triangle-source-metric")
    relative = mm(gi, schur)
    assert all(not(aa-bb)
               for ra, rb in zip(mm(g, relative), schur)
               for aa, bb in zip(ra, rb))
    symmetric(schur, "actual-original-three-source-Schur-form")
    emit("ORIGINAL_THREE_SOURCE_RELATIVE_SCHUR_READY",
         collision_interpretation="det(tG+S)/det(G), original continuous forms")

    passed = True
    for order in (1, 2, 3):
        if order == 1:
            coefficient = sum(relative[i][i] for i in range(3))
        elif order == 2:
            coefficient = sum(relative[i][i]*relative[j][j]
                              -relative[i][j]*relative[j][i]
                              for i in range(3) for j in range(i+1, 3))
        else:
            coefficient = determinant(relative)
        if not certify_schur_spectral_coefficient(coefficient, order):
            passed = False
            break
    emit("ORIGINAL_REMAINING_SCHUR_SPECTRAL_RESULT",
         all_three_original_spectral_coefficients_positive=passed,
         full_S1_proved_only_if_all_passed=passed,
         already_paid_star_block_not_retested=True,
         no_original_leading_minor_4_gate=True, S2_not_tested=True,
         no_expanded_data_or_encoding_exported=True)
    signal.alarm(0)


if __name__ == "__main__":
    main()
