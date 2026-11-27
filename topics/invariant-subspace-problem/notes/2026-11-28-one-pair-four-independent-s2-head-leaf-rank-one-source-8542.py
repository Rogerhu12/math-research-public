"""Original S2 via the physical head source and the three-leaf Schur.

The failed full four-dimensional spectral gate is frozen. This new source
first proves the original one-dimensional head-minus-pair S2 inequality.
It then keeps every cross term in the actual head/leaf Schur complement,
using a rank-one determinant identity to define three different conditional
source coefficients. No old c2 coefficient or trace certificate is tested.

All complete physical inverses and the original lower metric are preserved.
Companion coordinates are only a distinct-root representation; collisions
are handled through the original continuous forms. Only positive elementary
factors may be removed, with exact polynomial multiplication back.
Fixed 180 seconds, 4 GiB; small ordinary summaries, no expanded output files.
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



def positive_original_factors():
    aa, ss, pp, qq = CTX.gens()
    return [
        ("a", aa), ("s", ss), ("p", pp), ("q", qq),
        ("a+1", aa+1),
        ("e1", aa+ss+2),
        ("e2", pp+aa*ss+2*aa+2*ss+1),
        ("e3", qq+aa*pp+2*pp+2*aa*ss+aa+ss),
        ("e4", aa*ss+(2*aa+1)*pp+(aa+2)*qq),
        ("e5", aa*pp+(2*aa+1)*qq),
    ]


def remove_strictly_positive_factors(num):
    removed = []
    for name, factor in positive_original_factors():
        count = 0
        while num and num.gcd(factor).total_degree() == factor.total_degree():
            quotient = num//factor
            assert quotient*factor == num, "positive factor return failed"
            num = quotient
            count += 1
        if count:
            removed.append({"factor": name, "power": count})
    return num, removed


def certify_head_leaf_target(value, target_index, target_label):
    reference = value.d(1, 3, 3, 1)
    assert reference, "uncancelled coordinate pole at a positive collision"
    num = value.n if reference > 0 else -value.n
    before = {"degree": int(num.total_degree()), "terms": len(num),
              "sha256": polynomial_digest(num)}
    num, removed = remove_strictly_positive_factors(num)
    weight = (1, 1, 2, 3)
    degree = max(sum(weight[i]*int(e[i]) for i in range(4))
                 for e, _ in num.terms())
    homogeneous = HOM_CTX.from_dict({
        tuple(int(e) for e in exponent)
        + (degree-sum(weight[i]*int(exponent[i]) for i in range(4)),): coefficient
        for exponent, coefficient in num.terms()})
    emit("original_head_leaf_target",
         target_index=target_index, target_label=target_label,
         raw_numerator=before, removed_positive_factors=removed,
         numerator_degree=int(num.total_degree()), numerator_weighted_degree=degree,
         numerator_terms=len(num), denominator_terms=len(value.d),
         equal_weight_denominator=str(reference),
         numerator_sha256=polynomial_digest(num))
    for k, numerators, tau in parameter_chambers():
        pullback = homogeneous.compose(*numerators, tau)
        if not square_source(pullback, k, target_index):
            emit("INCONCLUSIVE_ORIGINAL_HEAD_LEAF_SOURCE",
                 target_index=target_index, target_label=target_label,
                 failed_chamber=k, later_chambers_not_computed=4-k,
                 later_head_leaf_targets_not_computed=3-target_index)
            return False
    emit("ORIGINAL_HEAD_LEAF_TARGET_ALL_CHAMBERS_POSITIVE",
         target_index=target_index, target_label=target_label)
    return True


def main():
    e1, e2 = original_sources()
    bridge, deep = actual_cubic_bridges(e1, e2)
    w1, w2 = metric(1), metric(2)
    u1 = mm(transpose(e1), w1, e1)
    u0 = mm(transpose(e2), w2, e2)
    ui = inverse(u0, "full-original-upper-six-source-metric")
    lower = {}
    for height in (1, 2, 3):
        full_inverse = inverse(complete_gram(1, height),
                               "full-original-lower-five-gram-"+str(height))
        lower[height] = mm(transpose(e1), full_inverse, e1)
    l1, l2, l3 = lower[1], lower[2], lower[3]
    l2i = inverse(l2, "original-four-source-Gamma2")
    l3i = inverse(l3, "original-four-source-Gamma3")

    hfull = ma(ms(eye(dimension(2)), a+s+2), occupation_operator(2), -2)
    hhat = mm(transpose(e2), w2, hfull, e2)
    bt = transpose(bridge)
    m = mm(bt, l2, bridge)
    c1hat = ma(hhat, m, -1)
    symmetric(c1hat, "actual-upper-C1-from-full-two-band-identity")
    c1i = inverse(c1hat, "entire-original-upper-six-source-C1")
    emit("FULL_ORIGINAL_S2_SOURCE_PRECISIONS_READY",
         upper_source_dimension=6, lower_source_dimension=4,
         full_lower_physical_dimension=5, S1_not_retested=True)

    # X is the same original low-source bilinear form. The three middle
    # matrices are dual forms, so these products include all physical
    # metrics without inserting or omitting any U1 factor.
    x = mm(l2, l3i, l2)
    kbb = mm(bridge, ui, bt)
    kbc = mm(bridge, ui, c1hat, ui, bt)
    kbg = mm(bridge, c1i, bt)
    emit("ORIGINAL_ALL_UPPER_SOURCE_ELIMINATION_READY",
         three_blocks=["BBstar", "BC1Bstar", "BG1Bstar"])

    four = ma(ma(mm(l2, kbc, l2), mm(l2, kbb, x)),
              mm(x, kbb, l2))
    four = ma(four, mm(x, kbg, x))
    cost = ms(four, Rat(1)/4)
    symmetric(cost, "same-source-Astar-G1-A-with-both-cross-terms")
    lowcost = mm(l1, l2i, l1)
    deficit = ma(ma(u1, cost, -1), lowcost, -1)
    symmetric(deficit, "entire-original-four-source-S2-deficit")
    emit("ORIGINAL_HEAD_LEAF_S2_DEFICIT_READY",
         full_upper_source_used=True, both_mixed_terms_used=True,
         source_cost_terms=4, original_low_cost_retained=True)


    # The first target is the actual head-minus-pair direction, not the
    # already paid full trace or the unreturned old second spectral coefficient.
    head = deficit[0][0]
    if not certify_head_leaf_target(head, 0, "actual-head-source-S2"):
        emit("ORIGINAL_HEAD_LEAF_RESULT", all_targets_positive=False,
             head_source_paid=False, full_S2_proved=False)
        signal.alarm(0)
        return

    leaf = [row[1:] for row in deficit[1:]]
    cross = [deficit[0][1:]]
    col = [[deficit[i][0]] for i in range(1, 4)]
    g = [row[1:] for row in u1[1:]]
    gi = inverse(g, "original-positive-three-leaf-source-metric")
    relative_leaf = mm(gi, leaf)
    v = mm(gi, col)
    mu0 = mm(cross, v)[0][0]
    e1 = sum(relative_leaf[i][i] for i in range(3))
    emit("ORIGINAL_HEAD_LEAF_RANK_ONE_SOURCE_READY",
         head_source_already_positive=True,
         reference_metric="actual three leaf-minus-pair sources",
         invariant_identity="det(tG+Zll-zl0*z0l/head)/det(G)",
         old_four_source_c2_not_used=True)

    # det(tI+R-v*w/head) =
    # t^3 + (head*e1-mu0)/head*t^2
    #     + (head*e2-e1*mu0+mu1)/head*t
    #     + (head*e3-e2*mu0+e1*mu1-mu2)/head.
    # Only a positive factor head is omitted from each sign test.
    passed = certify_head_leaf_target(head*e1-mu0, 1,
                                     "conditional-leaf-Schur-first-coefficient-times-head")
    if passed:
        e2 = sum(relative_leaf[i][i]*relative_leaf[j][j]
                 -relative_leaf[i][j]*relative_leaf[j][i]
                 for i in range(3) for j in range(i+1, 3))
        mu1 = mm(cross, relative_leaf, v)[0][0]
        passed = certify_head_leaf_target(head*e2-e1*mu0+mu1, 2,
                                         "conditional-leaf-Schur-second-coefficient-times-head")
    if passed:
        e3 = determinant(relative_leaf)
        mu2 = mm(cross, relative_leaf, relative_leaf, v)[0][0]
        passed = certify_head_leaf_target(head*e3-e2*mu0+e1*mu1-mu2, 3,
                                         "conditional-leaf-Schur-determinant-times-head")

    emit("ORIGINAL_HEAD_LEAF_RESULT",
         all_targets_positive=passed, head_source_paid=True,
         original_symmetric_four_source_S2_proved_only_if_all_passed=passed,
         old_full_trace_not_retested=True, old_four_source_c2_not_used=True,
         S1_not_retested=True,
         no_expanded_data_or_encoding_exported=True)
    signal.alarm(0)


if __name__ == "__main__":
    main()
