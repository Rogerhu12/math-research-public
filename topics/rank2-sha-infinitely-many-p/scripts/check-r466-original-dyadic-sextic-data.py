#!/usr/bin/env python3
"""Exact local certificates for the five original D_k=8*(-17)^k sources.

The two dyadic vectors use the full Rao kernel, including its cross-term
sign on odd functions.  The norm-one generators are -1, omega and g_*.
The 17-adic vectors are the actual finite Weil projectors, not fitted
theta coefficients.  No target-prime experiment is used.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as sp
from flint import fmpq as Q, fmpq_poly as Poly


class Field:
    def __init__(self, n):
        self.n = n
        x = sp.Symbol("x")
        c = sp.Poly(sp.cyclotomic_poly(n, x), x)
        self.mod = Poly([int(c.nth(j)) for j in range(c.degree()+1)])
        self.degree = c.degree()
        self.zero, self.one, self.z = self(0), self(1), self([0, 1])
        self.powers = [self.one]
        for _ in range(1, n):
            self.powers.append(self.powers[-1] * self.z)

    def __call__(self, a):
        if isinstance(a, Element):
            assert a.F is self
            return a
        if isinstance(a, Fraction):
            a = Q(a.numerator, a.denominator)
        if not isinstance(a, (list, Poly)):
            a = [a]
        return Element(self, Poly(a) % self.mod)


class Element:
    def __init__(self, F, p):
        self.F, self.p = F, p

    def __add__(self, b):
        return Element(self.F, self.p + self.F(b).p)
    __radd__ = __add__

    def __neg__(self):
        return Element(self.F, -self.p)

    def __sub__(self, b):
        return self + (-self.F(b))

    def __rsub__(self, b):
        return self.F(b) - self

    def __mul__(self, b):
        return Element(self.F, (self.p * self.F(b).p) % self.F.mod)
    __rmul__ = __mul__

    def __truediv__(self, b):
        g, v, _ = self.F(b).p.xgcd(self.F.mod)
        assert g == Poly([1])
        return self * Element(self.F, v)

    def __pow__(self, n):
        if n < 0:
            return (self.F.one / self)**(-n)
        out, a = self.F.one, self
        while n:
            if n & 1:
                out = out * a
            a = a * a
            n //= 2
        return out

    def __eq__(self, b):
        return self.p == self.F(b).p

    def conj(self):
        return sum((self.F.powers[-j % self.F.n] * self.p[j]
                    for j in range(len(self.p))), self.F.zero)

    def coeffs(self):
        return [str(self.p[j]) for j in range(self.F.degree)]


def mm(A, B):
    F = A[0][0].F
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F.zero)
             for j in range(len(B[0]))] for i in range(len(A))]


def mv(A, v):
    return [sum((a*b for a, b in zip(row, v)), row[0].F.zero) for row in A]


def eye(F, n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def chi4(a):
    assert a % 2
    return 1 if a % 4 == 1 else -1


def chi8(a):
    assert a % 2
    return 1 if a % 8 in (1, 7) else -1


def main():
    checks = []
    def check(name, val):
        assert val, name
        checks.append(name)
    F = Field(96)
    om, z32, z8 = F.z**32, F.z**3, F.z**12
    sq2 = z8 + z8**-1
    mu = -om**2*z8
    check("positive square root of 2 has square 2", sq2*sq2 == 2)

    # Actual alpha=17 full Rao kernel.  The eighth-coset complement cancels
    # using v(a+8)=(-1)^a*v(a), leaving this complete eight-dimensional space.
    O = [[mu/(2*sq2)*z32**(-51*(a*a+b*b+4*a*b))
          for b in range(8)] for a in range(8)]
    G, R = [[F.zero for _ in range(8)] for _ in range(8)], [
        [F.zero for _ in range(8)] for _ in range(8)]
    for b in range(8):
        if b % 2:
            a, phase = b, 1
        else:
            a, phase = (b+4) % 8, (-1 if b % 4 == 2 else 1)
        numerator = 33*(a*a+b*b)+78*a*b
        check("g-star full phase "+str(b),
              numerator % 16 == 0 and z8**(1-17*numerator//16) == phase)
        G[a][b] = F(phase)
    for a in range(8):
        b = (-a) % 16
        R[a][b % 8] = F((-1)**(b % 8) if b >= 8 else 1)
    check("omega has order three", mm(mm(O, O), O) == eye(F, 8))
    check("principal torus generator is an involution on this module", mm(G, G) == eye(F, 8))
    check("full torus generators commute", mm(G, O) == mm(O, G))
    check("ordinary reflection commutes", mm(R, O) == mm(O, R))

    hs = [
        [F(int(a in (0, 4))) for a in range(8)],
        [F(int(a == 2)-int(a == 6)) for a in range(8)],
    ]
    vectors = []
    for parity, seed in zip((1, -1), hs):
        check("seed fixed by full principal generator "+str(parity), mv(G, seed) == seed)
        v = [a+b+c for a, b, c in zip(seed, mv(O, seed), mv(mm(O, O), seed))]
        check("whole dyadic omega invariance "+str(parity), mv(O, v) == v)
        check("whole dyadic principal-generator invariance "+str(parity), mv(G, v) == v)
        check("correct original minus-one splitting "+str(parity),
              mv(R, v) == [parity*a for a in v])
        check("dyadic squared norm three "+str(parity),
              sum((a*a.conj() for a in v), F.zero)/2 == 3)
        check("dyadic vector real "+str(parity), all(a.conj() == a for a in v))
        allv = v+[(-1)**a*v[a] for a in range(8)]
        formula = []
        for a in range(16):
            if parity == 1:
                val = F(int(a % 4 == 0)) if a % 2 == 0 else (
                    om**2*z32**(a*a)+om*z32**(-a*a))/sq2
            else:
                if a % 2 == 0:
                    val = F(chi4(a//2) if a % 4 == 2 else 0)
                else:
                    val = -chi4(a)*(om**2*z8**3*z32**(a*a) +
                                    om*z8**-3*z32**(-a*a))/sq2
            formula.append(val)
        check("complete sixteen coefficients "+str(parity), allv == formula)
        check("actual dyadic half shift "+str(parity),
              all(allv[(a+8) % 16] == (-1)**a*allv[a] for a in range(16)))
        vectors.append(allv)

    # Complete conductor-eight Gauss sums in O_K/8, with psi_K/2 and c=4.
    gauss = {}
    for twist in (2, -2):
        val = F.zero
        for a in range(8):
            for b in range(8):
                norm = a*a-a*b+b*b
                if norm % 2 == 0:
                    continue
                teich = {(1, 0): F.one, (0, 1): om, (1, 1): om**2}[(a % 2, b % 2)]
                quad = chi8(norm)*(chi4(norm) if twist == -2 else 1)
                val += (teich*quad)**-1*z8**(-(2*a-b))
        expect = 8 if twist == -2 else -8
        check("complete dyadic epsilon Gauss "+str(twist), val == expect)
        gauss[str(twist)] = expect

    # The original inert-17 Weil representation.
    K = Field(51)
    z, w = K.z**3, K.z**17
    leg = lambda a: 0 if a % 17 == 0 else (1 if pow(a % 17, 8, 17) == 1 else -1)
    s17 = sum((leg(a)*z**a for a in range(1, 17)), K.zero)
    check("positive quadratic Gauss square seventeen", s17*s17 == 17)
    def mul(a, b):
        return ((a[0]*b[0]-3*a[1]*b[1]) % 17,
                (a[0]*b[1]+a[1]*b[0]) % 17)
    gs = [(1, 0)]
    for _ in range(18):
        gs.append(mul(gs[-1], (2, 4)))
    check("seventeen torus exact order eighteen", gs[18] == (1, 0) and len(set(gs[:18])) == 18)
    def W(g):
        x, y = g
        if y == 0:
            return [[K(int(a == (b if x == 1 else -b) % 17))
                     for b in range(17)] for a in range(17)]
        c = 3*pow(2*y, -1, 17) % 17
        return [[-leg(y)*s17/17*z**(c*(x*(a*a+b*b)-2*a*b))
                 for b in range(17)] for a in range(17)]
    mats = [W(g) for g in gs[:18]]
    data17 = []
    for k in range(1, 6):
        tau = -(-w**2)**k
        seed = [K(int(a == 0)) for a in range(17)] if k % 2 else [
            K(int(a == 1)-int(a == 16)) for a in range(17)]
        v = [K.zero for _ in range(17)]
        tr = K.zero
        for j, M in enumerate(mats):
            v = [a+tau**(-j)*b for a, b in zip(v, mv(M, seed))]
            tr += tau**(-j)*sum((M[a][a] for a in range(17)), K.zero)
        v = [s17/2*a for a in v]
        check("original finite multiplicity one k="+str(k), tr/18 == 1)
        check("original seventeen vector nonzero k="+str(k), any(a != 0 for a in v))
        check("original seventeen whole eigenline k="+str(k),
              mv(mats[1], v) == [tau*a for a in v])
        parity = 1 if k % 2 else -1
        check("seventeen parity k="+str(k),
              all(v[-a % 17] == parity*v[a] for a in range(17)))
        check("seventeen reality k="+str(k), all(a.conj() == a for a in v))
        norm = sum((a*a.conj() for a in v), K.zero)
        check("seventeen nonzero norm k="+str(k), norm != 0)
        data17.append({"k": k, "tau_at_generator": tau.coeffs(),
                       "squared_norm": norm.coeffs(),
                       "vector": [a.coeffs() for a in v]})

    # Exact Kummer identities for two independent rational points on E_2312.
    r = sp.sqrt(2)
    ap, aq = 85+34*r, 204+34*r
    check("two original rational points", 85**2 == 17**3+2312 and 204**2 == 34**3+2312)
    check("Kummer unit product", sp.expand(ap*aq-(17*r)**3*(1+r)) == 0)
    check("split-prime uniformizer norm", sp.expand((5+2*r)*(5-2*r)) == 17)
    check("second Kummer factorization", sp.expand(6+r-(1+r)*r*(5-2*r)) == 0)
    check("normalizations of the rational support", pow(51, -1, 16) == 11 and pow(12, -1, 17) == 10)
    out = {
        "curves": [8*(-17)**k for k in range(1, 6)],
        "hermitian_alpha": 17,
        "rational_support": "n/204",
        "coefficients": "v_{(-1)^(k+1)}(11*n mod16)*f_k(10*n mod17)",
        "dyadic_squared_norms": [3, 3],
        "dyadic_gauss": gauss,
        "dyadic_vectors_zeta96": [[a.coeffs() for a in v] for v in vectors],
        "seventeen_data_zeta51": data17,
        "checks": checks,
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    print("All", len(checks), "original dyadic, tame, and Kummer checks passed.")


if __name__ == "__main__":
    main()
