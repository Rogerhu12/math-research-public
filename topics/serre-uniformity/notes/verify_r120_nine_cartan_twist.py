#!/usr/bin/env python3
"""Exact, standard-library checks for R120; this does not classify C(Q)."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
from pathlib import Path


@dataclass(frozen=True)
class K:
    """Q(w), w^2=-3."""
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))

    @staticmethod
    def coerce(v):
        return v if isinstance(v, K) else K(v)

    def __add__(self, v):
        v = self.coerce(v)
        return K(self.a + v.a, self.b + v.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, v):
        return self + (-self.coerce(v))

    def __rsub__(self, v):
        return self.coerce(v) - self

    def __mul__(self, v):
        v = self.coerce(v)
        return K(self.a*v.a - 3*self.b*v.b, self.a*v.b + self.b*v.a)

    __rmul__ = __mul__

    def __truediv__(self, v):
        v = self.coerce(v)
        return self * K(v.a, -v.b) * (1/(v.a*v.a+3*v.b*v.b))

    def __rtruediv__(self, v):
        return self.coerce(v) / self

    def __pow__(self, n):
        if n < 0:
            return (1/self)**(-n)
        out, v = K(1), self
        while n:
            if n & 1:
                out = out*v
            v, n = v*v, n//2
        return out

    def __bool__(self):
        return bool(self.a or self.b)

    def conjugate(self):
        return K(self.a, -self.b)

    def pair(self):
        return [str(self.a), str(self.b)]


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def padd(a, b):
    c = [0]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def pscale(a, c):
    return trim([x*c for x in a])


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def ppow(a, n):
    c = [1]
    for _ in range(n):
        c = pmul(c, a)
    return c


def peval(a, x):
    c = 0
    for y in reversed(a):
        c = c*x+y
    return c


def deriv(a):
    return trim([i*a[i] for i in range(1, len(a))])


def assertzero(a):
    assert not any(a), a


def det(M):
    M = [list(map(F, row)) for row in M]
    ans = F(1)
    for k in range(len(M)):
        r = next((r for r in range(k, len(M)) if M[r][k]), None)
        if r is None:
            return 0
        if r != k:
            M[r], M[k] = M[k], M[r]
            ans = -ans
        p = M[k][k]
        ans *= p
        for r in range(k+1, len(M)):
            t = M[r][k]/p
            for c in range(k+1, len(M)):
                M[r][c] -= t*M[k][c]
    assert ans.denominator == 1
    return int(ans)


def resultant(a, b):
    m, n = len(a)-1, len(b)-1
    M = []
    for k in range(n):
        M.append([0]*k+list(reversed(a))+[0]*(n-1-k))
    for k in range(m):
        M.append([0]*k+list(reversed(b))+[0]*(m-1-k))
    return det(M)


def pmod(a, b, q):
    a = trim([v % q for v in a])
    b = trim([v % q for v in b])
    while len(a) >= len(b) and any(a):
        c = a[-1]*pow(b[-1], -1, q) % q
        k = len(a)-len(b)
        for j, v in enumerate(b):
            a[k+j] = (a[k+j]-c*v) % q
        a = trim(a)
    return a


def pgcd(a, b, q):
    while any(b):
        a, b = b, pmod(a, b, q)
    return trim([v*pow(a[-1], -1, q) % q for v in a])


def ppowmod(a, n, b, q):
    c = [1]
    while n:
        if n & 1:
            c = pmod(pmul(c, a), b, q)
        a, n = pmod(pmul(a, a), b, q), n//2
    return c


def matmul(a, b):
    return ((a[0]*b[0]+a[1]*b[2]) % 9,
            (a[0]*b[1]+a[1]*b[3]) % 9,
            (a[2]*b[0]+a[3]*b[2]) % 9,
            (a[2]*b[1]+a[3]*b[3]) % 9)


def cosets(G, H):
    idx, reps = {}, []
    for g in sorted(G):
        if g in idx:
            continue
        i = len(reps)
        reps.append(g)
        for h in H:
            gh = matmul(g, h)
            assert gh not in idx
            idx[gh] = i
    return reps, idx


def cycles(p):
    seen, lengths = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        j, n = i, 0
        while j not in seen:
            seen.add(j)
            j, n = p[j], n+1
        assert j == i
        lengths.append(n)
    return sorted(lengths)


def group_check():
    G = {a for a in product(range(9), repeat=4)
         if (a[0]*a[3]-a[1]*a[2]) % 9 == 1}
    C = {(a, -b % 9, b, a) for a, b in product(range(9), repeat=2)
         if (a*a+b*b) % 9 == 1}
    N = C | {(a, b, b, -a % 9) for a, b in product(range(9), repeat=2)
             if (a*a+b*b) % 9 == 8}
    s, t = (0, 8, 1, 0), (1, 1, 0, 1)
    st = matmul(s, t)
    outputs, data = [], []
    for H in [C, N]:
        reps, idx = cosets(G, H)
        ps = [idx[matmul(s, a)] for a in reps]
        pt = [idx[matmul(t, a)] for a in reps]
        pst = [idx[matmul(st, a)] for a in reps]
        e2 = sum(i == j for i, j in enumerate(ps))
        e3 = sum(i == j for i, j in enumerate(pst))
        cu = cycles(pt)
        genus = 1+F(len(reps), 12)-F(e2, 4)-F(e3, 3)-F(len(cu), 2)
        assert genus.denominator == 1
        outputs.append(dict(order=len(H), index=len(reps), e2=e2, e3=e3,
                            cusp_lengths=cu, genus=int(genus)))
        data.append((reps, idx, ps))
    cr, ci, cs = data[0]
    nr, ni, ns = data[1]
    fixed_lifts = []
    for j, v in enumerate(ns):
        if j == v:
            fiber = [i for i, g in enumerate(cr) if ni[g] == j]
            assert len(fiber) == 2
            fixed_lifts.append(sum(cs[i] == i for i in fiber))
    assert sorted(fixed_lifts) == [0]*6+[2]
    return dict(SL2_order=len(G), curves=outputs,
                fixed_lifts_over_normalizer_elliptic_points=sorted(fixed_lifts))


def ecadd(P, Q, A, q=None):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if q is None:
        if x == u and not y+v:
            return None
        m = (v-y)/(u-x) if x != u else (3*x*x+A)/(2*y)
        xx = m*m-x-u
        return xx, m*(x-xx)-y
    if x == u and (y+v) % q == 0:
        return None
    m = ((v-y)*pow(u-x, -1, q) if x != u
         else (3*x*x+A)*pow(2*y, -1, q)) % q
    xx = (m*m-x-u) % q
    return xx, (m*(x-xx)-y) % q


def ecmul(P, n, A, q):
    R = None
    while n:
        if n & 1:
            R = ecadd(R, P, A, q)
        P, n = ecadd(P, P, A, q), n//2
    return R


def reduce_k(a, w, q):
    return ((a.a.numerator*pow(a.a.denominator, -1, q))+
            w*a.b.numerator*pow(a.b.denominator, -1, q)) % q


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    assert not (args.write and args.check)
    D = [1, -3, 0, 1]
    A1, A2, A3 = [4, -6, 3, 1], [4, 3, 3, 1], [2, -3, -3, 5]
    S = [19, -72, 84, -10, -36, 12, 7]
    Q6 = [4, 0, -6, -4, 9, 3, 1]
    numerator = pscale(pmul(pmul(A1, A2), A3), -3)
    denominator = ppow(D, 3)
    rhs = pscale(pmul(pmul(pmul(pmul([1, 1],
        ppow([1, -1, 1], 2)), ppow([-2, 2, 1], 2)), ppow(Q6, 2)), S), -729)
    assertzero(psub(psub(ppow(numerator, 3), pscale(ppow(denominator, 3), 1728)), rhs))
    res = [resultant(D, a) for a in [A1, A2, A3]]
    assert res == [243, 243, -243]
    disc = -resultant(S, deriv(S))//7
    assert disc == -(2**12)*(3**17)
    sm = [v % 5 for v in S]
    irred = [pmod(psub(ppowmod([0, 1], 5**6, sm, 5), [0, 1]), sm, 5),
             pgcd(psub(ppowmod([0, 1], 5**3, sm, 5), [0, 1]), sm, 5),
             pgcd(psub(ppowmod([0, 1], 5**2, sm, 5), [0, 1]), sm, 5)]
    assert irred == [[0], [1], [1]]

    w = K(0, 1)
    r = (1-w)/2
    f = [(9*w+17)/14, (-9*w-45)/14, (-3*w+6)/7, K(1)]
    fb = [c.conjugate() for c in f]
    P = pmul(ppow([-r, K(1)], 2), [K(1), K(1)])
    H = [(20*w-12)/7, K(0), (-24*w-36)/7, (-10*w+6)/7]
    assertzero(psub(pscale(pmul(f, fb), 7), S))
    assertzero(psub(psub(pmul(deriv(P), f), pmul(P, deriv(f))), pmul([-r, K(1)], H)))
    gamma = (9-w)/14
    aa, bb = -(21+27*w)/2, 28*w-10
    Xnum = padd(pscale(f, w+2), pscale(P, gamma))
    lhs = pscale(pmul(S, ppow(H, 2)), gamma**2/9)
    rhs = padd(padd(pmul(ppow(Xnum, 3), f),
                     pscale(pmul(Xnum, ppow(f, 3)), aa)), pscale(ppow(f, 4), bb))
    assertzero(psub(lhs, rhs))
    PH = ((7-w)/2, 4*w-4)
    P1 = (w+2, (w-1)/2)
    P2 = ((1+w)/2, 2*w+4)
    for Q in [PH, P1, P2]:
        assert not Q[1]**2-Q[0]**3-aa*Q[0]-bb
    assert ecadd(PH, PH, aa) == P1
    for xx, yy, expected in [(-1, 12, P1), (1, 2, P2)]:
        actual = (w+2+gamma*peval(P, xx)/peval(f, xx),
                  gamma*yy*peval(H, xx)/(3*peval(f, xx)**2))
        assert actual == expected
    finite = []
    for q, ww in [(7, 2), (7, 5), (13, 6), (19, 4)]:
        assert (ww*ww+3) % q == 0
        aq, bq = reduce_k(aa, ww, q), reduce_k(bb, ww, q)
        assert (4*aq**3+27*bq*bq) % q != 0
        n = 1+sum(sum((y*y-x*x*x-aq*x-bq) % q == 0 for y in range(q))
                  for x in range(q))
        row = dict(q=q, w=ww, order=n)
        if q == 7:
            images = [ecmul(tuple(reduce_k(c, ww, q) for c in Q), 5, aq, q)
                      for Q in [PH, P2]]
            row['fivefold_images'] = images
            row['mod_two_row'] = [int(v is not None) for v in images]
        finite.append(row)
    assert [r['order'] for r in finite] == [10, 10, 15, 22]
    assert [r['mod_two_row'] for r in finite[:2]] == [[0, 1], [1, 1]]
    assert gcd(gcd(10, 15), 22) == 1

    # Completeness of this nine-item list comes from Baran §5, not this check.
    integral = []
    for u, v in [(-3, -2), (-1, -1), (0, 1), (1, 0), (1, 3), (2, -1),
                 (-1, -2), (-1, 1), (2, 1)]:
        d = u**3-3*u*v*v+v**3
        sh = sum(S[i]*u**i*v**(6-i) for i in range(7))
        assert d in [1, 3]
        integral.append(dict(uv=[u, v], F=d, S=sh, square=isqrt(sh)**2 == sh))
    output = dict(group=group_check(), discriminant=disc, resultants=res,
                  mod5_irreducibility_checks=irred,
                  elliptic_coefficients=[aa.pair(), bb.pair()],
                  independent_points=[[c.pair() for c in Q] for Q in [PH, P2]],
                  reductions=finite, integral_fibers=integral,
                  assertions='all exact identities and finite group checks passed',
                  rational_point_classification='NOT CLAIMED',
                  rank_statement='rank E0(K) >= 2 and rank Jac(C)(Q) >= 2; no upper bound')
    path = Path(__file__).with_name('r120_nine_cartan_twist_certificate.json')
    encoded = (json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True)+'\n').encode()
    if args.write:
        path.write_bytes(encoded)
    if args.check:
        assert path.read_bytes() == encoded
    print('R120 exact checks PASS')
    print('certificate sha256', hashlib.sha256(encoded).hexdigest())


if __name__ == '__main__':
    main()
