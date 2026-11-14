#!/usr/bin/env python3
"""R754: exact original p41 CM periods and Hom kernel; public Actions only.

Reuse the completed R735 model, R738 chains, and R745 vector.  No floating
point arithmetic, no old model/topology/torus-average recomputation.
"""
import argparse
from collections import deque
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly, fmpz_poly

RESULT = "R754-original-p41-periods-and-Hom-kernel"
P, N, DEG = 41, 246, 280
FIXED = {
    "p41-original-CM-state.json.gz": "9cd5f6731c7cfa76cd118b5f3a8ab1efb12d0d69ba95ab08817fcb80c2073427",
    "p41-original-torsion-modulus.json.gz": "7063eacd17ffec4c68dea5d8c3a2cab278286653fd12aae07f1c955bb1ad94fb",
    "p41-original-CM-model-certificate.json": "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574",
    "original-cosets-and-markings.json.gz": "6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161",
    "integral-compact-Manin-cycles.json.gz": "d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf",
    "original-p41-Hodge-q-expansions.json.gz": "a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        data = gzip.decompress(data)
    return json.loads(data)


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(obj, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    tmp = path.with_name(path.name+".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)


def ep(a):
    return {"numerator": [str(v) for v in a.numer().coeffs()],
            "denominator": str(a.denom())}


def dp(a):
    return fmpq_poly([int(v) for v in a["numerator"]], int(a["denominator"]))


def eq(a):
    return [str(a.numer()), str(a.denom())]


def dq(a):
    return fmpq(int(a[0]), int(a[1]))


class QKField:
    """Q[t]/modulus with the fixed zeta^2+zeta+1=0 adjoined."""
    def __init__(self, modulus):
        self.mod = modulus
        self.degree = modulus.degree()
        self.zero = QE(self, fmpq_poly([]), fmpq_poly([]))
        self.one = QE(self, fmpq_poly([1]), fmpq_poly([]))
        self.zeta = QE(self, fmpq_poly([]), fmpq_poly([1]))
        self.gen = QE(self, fmpq_poly([0, 1]), fmpq_poly([]))

    def elt(self, a=0, b=0):
        if isinstance(a, QE):
            assert a.F is self and b == 0
            return a
        if not isinstance(a, fmpq_poly):
            a = fmpq_poly([a])
        if not isinstance(b, fmpq_poly):
            b = fmpq_poly([b])
        return QE(self, a, b)

    def decode(self, value):
        return self.elt(dp(value[0]), dp(value[1]))


class QE:
    __slots__ = ("F", "a", "b")
    def __init__(self, field, a, b):
        self.F = field
        self.a, self.b = a % field.mod, b % field.mod

    def __bool__(self):
        return bool(self.a) or bool(self.b)

    def __eq__(self, other):
        other = self.F.elt(other)
        return self.a == other.a and self.b == other.b

    def __neg__(self):
        return self.F.elt(-self.a, -self.b)

    def __add__(self, other):
        other = self.F.elt(other)
        return self.F.elt(self.a+other.a, self.b+other.b)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-self.F.elt(other))

    def __rsub__(self, other):
        return self.F.elt(other)-self

    def __mul__(self, other):
        other = self.F.elt(other)
        ac, bd = self.a*other.a, self.b*other.b
        return self.F.elt(ac-bd,
                         (self.a+self.b)*(other.a+other.b)-ac-2*bd)

    __rmul__ = __mul__

    def inverse(self):
        assert self
        norm = (self.a*self.a-self.a*self.b+self.b*self.b) % self.F.mod
        gcd, x, _ = norm.xgcd(self.F.mod)
        assert gcd == fmpq_poly([1]), "Nonunit in the fixed exact field"
        ans = self.F.elt((self.a-self.b)*x, -self.b*x)
        assert self*ans == 1
        return ans

    def __truediv__(self, other):
        if isinstance(other, (int, fmpq)):
            assert other != 0
            return self.F.elt(self.a/other, self.b/other)
        return self*self.F.elt(other).inverse()

    def __rtruediv__(self, other):
        return self.F.elt(other)*self.inverse()

    def __pow__(self, n):
        n = int(n)
        if n < 0:
            return self.inverse()**(-n)
        ans, a = self.F.one, self
        while n:
            if n & 1:
                ans = ans*a
            n >>= 1
            if n:
                a = a*a
        return ans

    def encode(self):
        return [ep(self.a), ep(self.b)]


class Composer:
    """Exact baby-step/giant-step substitution in the retained field."""
    def __init__(self, at):
        self.F, self.at = at.F, at
        self.block = math.isqrt(self.F.degree)+1
        self.powers = [self.F.one]
        for _ in range(self.block):
            self.powers.append(self.powers[-1]*at)

    def rational(self, poly):
        if not poly:
            return self.F.zero
        count = (poly.degree()+self.block)//self.block
        ans = self.F.zero
        for block in reversed(range(count)):
            ans = ans*self.powers[self.block]
            value = self.F.zero
            for j in range(self.block):
                at = block*self.block+j
                if at <= poly.degree() and poly[at]:
                    value += poly[at]*self.powers[j]
            ans += value
        return ans

    def __call__(self, a):
        assert a.F is self.F
        return self.rational(a.a)+self.F.zeta*self.rational(a.b)


def inv_rational_matrix(a):
    n = len(a)
    m = [list(row)+[fmpq(int(i == j)) for j in range(n)]
         for i, row in enumerate(a)]
    for c in range(n):
        pivot = next(r for r in range(c, n) if m[r][c])
        m[c], m[pivot] = m[pivot], m[c]
        lead = m[c][c]
        m[c] = [x/lead for x in m[c]]
        for r in range(n):
            if r != c and m[r][c]:
                factor = m[r][c]
                m[r] = [x-factor*y for x, y in zip(m[r], m[c])]
    return [row[n:] for row in m]


class Subfield:
    """The actual L=K(b) embedded in the retained M0=K(U)."""
    def __init__(self, M, L, b):
        self.M, self.L = M, L
        self.bp = [M.one]
        for _ in range(6):
            self.bp.append(self.bp[-1]*b)
        assert all(not x.b for x in self.bp)
        pivots, selected = {}, []
        for a in range(M.degree):
            row = [x.a[a] for x in self.bp]
            for c in sorted(pivots):
                if row[c]:
                    value = row[c]
                    row = [x-value*y for x, y in zip(row, pivots[c])]
            if any(row):
                c = next(j for j, x in enumerate(row) if x)
                lead = row[c]
                pivots[c] = [x/lead for x in row]
                selected.append(a)
                if len(selected) == 7:
                    break
        assert len(selected) == 7
        self.selected = selected
        self.inverse = inv_rational_matrix([[x.a[a] for x in self.bp] for a in selected])

    def embed(self, a):
        assert a.F is self.L
        return sum((a.a[j]*self.bp[j] for j in range(7)), self.M.zero)+\
               self.M.zeta*sum((a.b[j]*self.bp[j] for j in range(7)), self.M.zero)

    def descend(self, value):
        aa, bb = [], []
        for row in self.inverse:
            aa.append(sum((row[j]*value.a[self.selected[j]] for j in range(7)), fmpq(0)))
            bb.append(sum((row[j]*value.b[self.selected[j]] for j in range(7)), fmpq(0)))
        ans = self.L.elt(fmpq_poly(aa), fmpq_poly(bb))
        assert self.embed(ans) == value, "Actual coordinate failed descent to K(b)"
        return ans


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def polynomial_add(a, b, F):
    c = [F.zero for _ in range(max(len(a), len(b)))]
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def polynomial_mul(a, b, F):
    if not a or not b:
        return []
    c = [F.zero for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def polynomial_divmod(a, b, F):
    a, b = trim(a), trim(b)
    assert b
    q = [F.zero for _ in range(max(0, len(a)-len(b)+1))]
    lead = b[-1].inverse()
    while a and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]*lead
        q[k] = c
        for i, value in enumerate(b):
            a[k+i] -= c*value
        a = trim(a)
    return trim(q), a


class Tower:
    """L(nu), nu=zeta_7=eta^6; no large compositum is constructed."""
    def __init__(self, L, coefficients):
        self.L = L
        a = [L.elt(x) for x in coefficients]
        while len(a) > 6:
            value, k = a.pop(), len(a)-6
            if value:
                for j in range(6):
                    a[k+j] -= value
        self.c = a+[L.zero]*(6-len(a))

    def coerce(self, x):
        if isinstance(x, Tower):
            assert x.L is self.L
            return x
        return Tower(self.L, [self.L.elt(x)])

    def __bool__(self):
        return any(self.c)

    def __eq__(self, other):
        return self.c == self.coerce(other).c

    def __add__(self, other):
        return Tower(self.L, [a+b for a, b in zip(self.c, self.coerce(other).c)])

    __radd__ = __add__

    def __neg__(self):
        return Tower(self.L, [-x for x in self.c])

    def __sub__(self, other):
        return self+(-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other)-self

    def __mul__(self, other):
        return Tower(self.L, polynomial_mul(self.c, self.coerce(other).c, self.L))

    __rmul__ = __mul__

    def inverse(self):
        assert self
        L = self.L
        r0, r1 = [L.one]*7, trim(self.c)
        s0, s1 = [], [L.one]
        while r1:
            q, r = polynomial_divmod(r0, r1, L)
            s = polynomial_add(s0, [-x for x in polynomial_mul(q, s1, L)], L)
            r0, r1, s0, s1 = r1, r, s1, s
        assert len(r0) == 1
        ans = Tower(L, [x/r0[0] for x in s0])
        assert self*ans == 1
        return ans

    def __truediv__(self, other):
        return self*self.coerce(other).inverse()

    def __pow__(self, n):
        if n < 0:
            return self.inverse()**(-n)
        ans, a = self.coerce(1), self
        while n:
            if n & 1:
                ans *= a
            n >>= 1
            if n:
                a *= a
        return ans

    def trace(self):
        return 6*self.c[0]-sum(self.c[1:], self.L.zero)

    def encode(self):
        return [x.encode() for x in self.c]

    @classmethod
    def decode(cls, L, value):
        return cls(L, [L.decode(x) for x in value])


def point_add(A, B, D):
    if A is None:
        return B
    if B is None:
        return A
    ra, sa = A
    rb, sb = B
    if ra == rb:
        if sa == -sb:
            return None
        assert sa == sb
        slope = 3*ra*ra/(2*D*sa)
    else:
        slope = (sb-sa)/(rb-ra)
    rc = D*slope*slope-ra-rb
    sc = -sa+slope*(ra-rc)
    return (rc, sc)


def point_mul(k, base, D):
    if k < 0:
        return point_mul(-k, (base[0], -base[1]), D)
    ans, at = None, base
    while k:
        if k & 1:
            ans = point_add(ans, at, D)
        k >>= 1
        if k:
            at = point_add(at, at, D)
    return ans


def endomorphism_point(a, b, M):
    a, b = a % P, b % P
    if a > P//2:
        a -= P
    if b > P//2:
        b -= P
    D, base = 1+M.gen/4, (M.one, M.one)
    A, B = point_mul(a, base, D), point_mul(b, base, D)
    if B is not None:
        B = (M.zeta*B[0], B[1])
    return point_add(A, B, D)


def line_ratio(A, B, D):
    """g_(A,B)(zeta P')/g_(A,B)(zeta^2 P'), in K(U)."""
    assert A is not None and B is not None
    ra, sa = A
    rb, sb = B
    zeta, one = ra.F.zeta, ra.F.one
    if ra == rb and sa == -sb:
        return (zeta-ra)/(zeta*zeta-ra), None
    if ra == rb:
        assert sa == sb
        slope = 3*ra*ra/(2*D*sa)
    else:
        slope = (sb-sa)/(rb-ra)
    R = point_add(A, B, D)
    assert R is not None
    plus = (one-sa-slope*(zeta-ra))/(zeta-R[0])
    minus = (one-sa-slope*(zeta*zeta-ra))/(zeta*zeta-R[0])
    return plus/minus, R


class Job:
    def __init__(self, out, inputs):
        assert flint.__version__ == "0.9.0", "R754 requires the pinned python-flint 0.9.0"
        self.out = Path(out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.inputs = Path(inputs)
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
                    "inputs": FIXED, "python_flint": flint.__version__,
                    "normalization": "R751 P'=D_u(Omega0/p), negative-real U root; exact original chains"}
        self.started = time.monotonic()

    def path(self, name):
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if path.exists():
            obj = read(path)
            assert obj["configuration"] == self.tag
            return obj
        return None

    def store(self, name, data):
        data = dict(data, configuration=self.tag)
        save(self.path(name), data)
        print(json.dumps({"stage": name, "complete": data.get("complete", False),
                          "seconds": time.monotonic()-self.started}), flush=True)

    def inputs_read(self):
        ans = {}
        for name, digest in FIXED.items():
            path = self.inputs/name
            assert sha(path) == digest, name
            ans[name] = read(path)
        assert ans["p41-original-CM-state.json.gz"]["complete"]
        h = ans["original-p41-Hodge-q-expansions.json.gz"]
        assert h["p"] == P and h["eta_mod_p"] == [7, 30]
        assert h["torus_average_coefficients_denominator"] == P*(P+1)
        c = ans["original-cosets-and-markings.json.gz"]
        assert c["c1"]["coset"] == 4424
        assert c["c1"]["marked_SL2Z_representative"] == [15130, 123, 123, 1]
        assert c["c0"]["cosets"] == [2876, 2822, 2823]
        return ans

    def fields(self, data):
        model = data["p41-original-CM-model-certificate.json"]
        modulus = data["p41-original-torsion-modulus.json.gz"]
        state = data["p41-original-CM-state.json.gz"]
        M = QKField(dp(modulus["monic_U_modulus"]))
        L = QKField(dp(model["minimal_polynomial"]))
        K = QKField(fmpq_poly([0, 1]))
        assert M.degree == 280 and L.degree == 7
        b = M.elt(dp(state["original_b_in_U"]))
        sub = Subfield(M, L, b)
        prior = self.cached("R754-field-kernel-input")
        if prior and prior["complete"]:
            S, H = M.decode(prior["S"]), M.decode(prior["H"])
        else:
            wn, wd, rn, rd = [M.elt(dp(state[key])) for key in ("wn", "wd", "rn", "rd")]
            S = wn/wd*(1-3**20*(rn/rd)**2)
            H = M.gen**7*S/(1+M.gen)
            assert not S.b and not H.b
            self.store("R754-field-kernel-input", {
                "complete": True, "S": S.encode(), "H": H.encode(),
                "L_embedding_pivot_rows": sub.selected,
                "reused_model_products_not_recomputed": True,
                "original_target_b_reused": True,
                "P_prime_marking": "P'=D_u(Omega0/p); actual real P27=[2+zeta]P'",
                "target_phase_Rc_alpha_s_sqrt3_xstar2": "-6*zeta*U^6*S"})
        return M, L, K, sub, b, S, H

    def pairing(self, M):
        name = "R754-original-Weil-pairing"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return M.decode(prior["xi"])
        bits = bin(P)[3:]
        D, base = 1+M.gen/4, (M.one, M.one)
        if prior:
            index = prior["bits_completed"]
            ratio = M.decode(prior["quotient"])
            point = None if prior["point"] is None else tuple(M.decode(x) for x in prior["point"])
        else:
            index, ratio, point = 0, M.one, base
        for step in range(index, len(bits)):
            factor, point = line_ratio(point, point, D)
            ratio = ratio*ratio*factor
            if bits[step] == "1":
                factor, point = line_ratio(point, base, D)
                ratio *= factor
            self.store(name, {"complete": False, "bits_completed": step+1,
                "quotient": ratio.encode(),
                "point": None if point is None else [x.encode() for x in point],
                "formula": "xi=-zeta^41*f_P(zeta*P')/f_P(zeta^2*P')"})
        assert point is None
        xi = -(M.zeta**P)*ratio
        assert xi != 1 and xi**P == 1
        self.store(name, {"complete": True, "xi": xi.encode(),
            "miller_quotient": ratio.encode(), "p_power_equals_one": True,
            "not_one": True, "arithmetic_in_retained_K_U": True,
            "analytic_orientation": "exp(2*pi*i/41), by R751 sigma and Legendre proof",
            "P_prime_is_not_real_E27_point": True,
            "R738_order_zeta_1_pairing_is_inverse": True})
        return xi

    def projector(self, M, L, sub, b, S):
        name = "R754-original-theta-period-line"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return Tower.decode(L, prior["zstar"]), Tower.decode(L, prior["zstar_inverse"])
        nu = Tower(L, [L.zero, L.one])
        eta = nu**6*(-L.zeta**2)
        assert eta**14 == Tower(L, [L.zeta]) and eta**42 == 1
        checkpoint = self.cached("R754-gamma-descent")
        if checkpoint and checkpoint["complete"]:
            ag = L.decode(checkpoint["sigma_gamma_r_over_r"])
            bg = L.decode(checkpoint["sigma_gamma_b"])
        else:
            point = endomorphism_point(7, 30, M)
            assert point is not None
            Rg, Sg = point
            assert (1+M.gen/4)*Sg*Sg == Rg**3+M.gen/4
            Ug = M.gen/Rg**3
            compose = Composer(Ug)
            assert compose.rational(M.mod) == 0
            a_big = (Rg**(-20))*compose(S)/S
            b_big = compose(b)
            ag, bg = sub.descend(a_big), sub.descend(b_big)
            self.store("R754-gamma-descent", {
                "complete": True, "gamma": [7, 30],
                "sigma_gamma_r_over_r": ag.encode(), "sigma_gamma_b": bg.encode(),
                "both_descents_verified_in_all_280_coordinates": True,
                "sigma_gamma_preserves_original_modulus": True})
        sigma = Composer(bg)
        btest = L.gen
        for _ in range(7):
            btest = sigma(btest)
        assert btest == L.gen
        aj, zstar, ratios = L.one, Tower(L, []), []
        theta_gamma = eta**2
        for j in range(7):
            ratios.append(aj.encode())
            zstar += theta_gamma**(-j)*aj.inverse()
            aj = ag*sigma(aj)
        assert aj == L.zeta**2
        zstar *= fmpq(1, 7)
        assert zstar
        sigma_zstar = Tower(L, [sigma(x) for x in zstar.c])
        assert sigma_zstar == theta_gamma*ag*zstar
        inverse = zstar.inverse()
        self.store(name, {"complete": True, "zstar": zstar.encode(),
            "zstar_inverse": inverse.encode(), "seven_r_ratios": ratios,
            "sigma_gamma_r_over_r": ag.encode(), "sigma_gamma_b": bg.encode(),
            "exact_product_equals_one": True,
            "exact_original_character_covariance": True,
            "nonvanishing_proof": "R725 leading tame ratio gives zstar=1 mod the fixed maximal ideal",
            "theta_gamma": "eta^2", "eta_in_nu_coordinates": "-zeta^2*nu^6"})
        return zstar, inverse

    def xi_powers(self, M, xi):
        name = "R754-exact-xi-powers"
        prior = self.cached(name)
        powers = [M.decode(x) for x in prior["powers"]] if prior else [M.one]
        if prior and prior["complete"]:
            return powers
        while len(powers) <= 40:
            powers.append(powers[-1]*xi)
            if len(powers) % 8 == 0:
                self.store(name, {"complete": False, "powers": [x.encode() for x in powers]})
        assert powers[-1]*xi == 1
        assert sum(powers, M.zero) == 0
        self.store(name, {"complete": True, "powers": [x.encode() for x in powers],
                          "full_cyclotomic_relation_verified": True})
        return powers

    def trace_weights(self, M, sub, H):
        weights = []
        U_poly, derivative = fmpq_poly([0, 1]), M.mod.derivative()
        for j in range(7):
            name = "R754-trace-functional-"+str(j)
            prior = self.cached(name)
            if prior and prior["complete"]:
                weights.append(dp(prior["weights"]))
                continue
            hj = H*sub.bp[j]
            assert not hj.b
            value = (hj.a*derivative) % M.mod
            w = []
            for _ in range(M.degree):
                w.append(value[M.degree-1])
                value = (U_poly*value) % M.mod
            vector = fmpq_poly(w)
            weights.append(vector)
            self.store(name, {"complete": True, "j": j, "weights": ep(vector),
                "identity": "weights[r]=[U^279](H*b^j*U^r*P'(U) mod P)=Tr(H*b^j*U^r)"})
        return weights

    def additive_periods(self, M, L, K, zstar, inverse, powers, weights):
        name = "R754-exact-normalized-additive-periods"
        prior = self.cached(name)
        values = {} if not prior else {int(a): Tower.decode(L, x) for a, x in prior["periods"].items()}
        traces = {} if not prior else prior["traces"]
        if prior and prior["complete"]:
            return values
        for a in range(1, P):
            if a in values:
                continue
            x = powers[9*a % P]
            line = []
            for j in range(7):
                real = sum((weights[j][r]*x.a[r] for r in range(DEG)), fmpq(0))
                imag = sum((weights[j][r]*x.b[r] for r in range(DEG)), fmpq(0))
                line.append(K.elt(real, imag))
            coeff = []
            for i in range(6):
                value = K.zero
                for j in range(7):
                    value += line[j]*K.elt(inverse.c[i].a[j], inverse.c[i].b[j])
                coeff.append(L.elt(value.a[0], value.b[0]))
            trace = Tower(L, coeff)
            values[a] = zstar*trace*(-fmpq(3, P)*L.zeta)
            traces[str(a)] = [x.encode() for x in line]
            if a % 4 == 0:
                self.store(name, {"complete": False,
                    "periods": {str(k): v.encode() for k, v in values.items()}, "traces": traces})
        assert len(values) == 40
        self.store(name, {"complete": True,
            "periods": {str(k): v.encode() for k, v in values.items()}, "traces": traces,
            "definition": "Z_a=R_C*alpha*sqrt(-3)*lambda_1(a/41)",
            "formula": "Z_a=-(3*zeta/41)*zstar*Tr_M0A/A(H*xi^(9a)/zstar)",
            "all_values_exact_in_L_times_A": True,
            "old_target_topology_or_torus_average_recomputed": False})
        return values

    def finite_vectors(self, data):
        name = "R754-original-finite-edge-vectors"
        prior = self.cached(name)
        records = {} if not prior else prior["vectors"]
        if prior and prior["complete"]:
            return records
        hodge = data["original-p41-Hodge-q-expansions.json.gz"]
        cells = data["original-cosets-and-markings.json.gz"]
        chains = data["integral-compact-Manin-cycles.json.gz"]
        modulus = fmpz_poly([int(x) for x in hodge["Phi42"]])
        epowers = [fmpz_poly([1])]
        for _ in range(41):
            epowers.append((epowers[-1]*fmpz_poly([0, 1])) % modulus)
        original = [fmpz_poly([int(x) for x in row])
                    for row in hodge["torus_average_numerators_eta"]]
        assert not original[0] and len(original) == 41
        Wname = "R754-original-Weyl-matrix"
        Wold = self.cached(Wname)
        if Wold and Wold["complete"]:
            W = [[fmpz_poly([int(x) for x in row]) for row in col]
                 for col in Wold["p_times_Weyl_columns"]]
        else:
            logs, g = {}, (1, 0)
            for j in range(42):
                logs[g] = j
                g = ffmul(g, (7, 30))
            assert g == (1, 0) and len(logs) == 42
            points = []
            for a in range(P):
                for b in range(P):
                    if a == b == 0:
                        continue
                    norm, trace = (a*a-a*b+b*b) % P, (2*a-b) % P
                    invnorm = pow(norm, -1, P)
                    inv = ((a-b)*invnorm % P, -b*invnorm % P)
                    conjugate = ((a-b) % P, -b % P)
                    exponent = -logs[ffmul(conjugate, inv)] % 42
                    points.append((norm, trace, exponent))
            W = []
            for r in range(P):
                counts = [[0]*42 for _ in range(P)]
                for norm, trace, exponent in points:
                    counts[(r*norm+trace) % P][exponent] += 1
                raw = [fmpz_poly(row) % modulus for row in counts]
                W.append([raw[0]-v for v in raw])
            self.store(Wname, {"complete": True,
                "p_times_Weyl_columns": [[list(map(str, row.coeffs())) for row in col] for col in W],
                "new_Weyl_matrix_not_a_torus_average": True,
                "theta_direction": "eta^(-log_gamma(bar(y)/y))"})
        relative = chains["relative_basis_edges"]
        for index, edge in enumerate(relative):
            if str(edge) in records:
                continue
            pos = chains["edge_positive_negative_cosets"][edge][0]
            g = [int(v) % P for v in cells["SL2Z_lifts"][pos]]
            a, b, c, d = g
            assert (a*d-b*c) % P == 1
            # Classical right slash: apply the finite LEFT inverse.
            a, b, c, d = d, -b % P, -c % P, a
            if c == 0:
                value = affine(original, a*pow(d, -1, P) % P, b*pow(d, -1, P) % P)
            else:
                delta = (a*d-b*c) % P
                before = affine(original, c*c*pow(delta, -1, P) % P,
                                c*d*pow(delta, -1, P) % P)
                middle = [fmpz_poly([]) for _ in range(P)]
                for r in range(1, P):
                    if not before[r]:
                        continue
                    for target in range(1, P):
                        middle[target] += (before[r]*W[r][target]) % modulus
                middle = [x % modulus for x in middle]
                divided = []
                for row in middle:
                    coeffs = [int(x) for x in row.coeffs()]
                    assert all(x % P == 0 for x in coeffs), "Extra Bruhat denominator did not cancel"
                    divided.append(fmpz_poly([x//P for x in coeffs]))
                value = affine(divided, 1, a*pow(c, -1, P) % P)
            assert not value[0]
            records[str(edge)] = {"positive_coset": pos,
                "d_eta": [[str(row[j]) for j in range(12)] for row in value]}
            if (index+1) % 32 == 0:
                self.store(name, {"complete": False, "vectors": records})
        assert len(records) == len(relative) == 819
        self.store(name, {"complete": True, "vectors": records,
            "all_denominators_equal_original_p_pplus1": True,
            "retained_relative_edges_in_same_order": True,
            "torus_average_or_norm_recomputed": False})
        return records

    def edge_periods(self, data, L, periods, vectors):
        name = "R754-original-relative-periods"
        prior = self.cached(name)
        encoded = {} if not prior else prior["periods"]
        values = {int(e): [L.decode(x) for x in row] for e, row in encoded.items()}
        if prior and prior["complete"]:
            return values
        cells = data["original-cosets-and-markings.json.gz"]
        chains = data["integral-compact-Manin-cycles.json.gz"]
        graph = {tuple(v["matrix"]): tuple(v["image"]) for v in cells["tame_theta_GL2F3"]}
        tame = tame_coefficients()
        C2 = (0, 1, 1, 1)
        powers2 = {matmul(C2, C2, 2): 2, C2: 1, (1, 0, 0, 1): 0}
        nu = Tower(L, [L.zero, L.one])
        eta = nu**6*(-L.zeta**2)
        eta_powers = [Tower(L, [L.one])]
        for _ in range(11):
            eta_powers.append(eta_powers[-1]*eta)
        beta = eta+eta**(-1)
        beta_powers = [Tower(L, [L.one])]
        for _ in range(5):
            beta_powers.append(beta_powers[-1]*beta)
        for index, edge in enumerate(chains["relative_basis_edges"]):
            if edge in values:
                continue
            rec = vectors[str(edge)]
            g = [int(x) for x in cells["SL2Z_lifts"][rec["positive_coset"]]]
            mm = tame[tuple(x % 2 for x in g)]
            xg = L.elt(mm[0])-mm[1]*L.zeta**2
            yg = L.elt(mm[2])-mm[3]*L.zeta**2
            chig = L.zeta**powers2[graph[tuple(x % 3 for x in g)]]
            total = Tower(L, [])
            for r in range(1, P):
                row = rec["d_eta"][r]
                if not any(int(x) for x in row):
                    continue
                dvalue = sum((eta_powers[j]*int(row[j]) for j in range(12)), Tower(L, []))
                at = (-r*pow(6, -1, P)) % P
                assert at != 0
                total += dvalue*(periods[at]*xg+periods[4*at % P]*yg)
            total *= -chig/7
            values[edge] = [(bp*total).trace() for bp in beta_powers]
            encoded[str(edge)] = [x.encode() for x in values[edge]]
            if (index+1) % 16 == 0:
                self.store(name, {"complete": False, "periods": encoded})
        assert len(values) == 819
        self.store(name, {"complete": True, "periods": encoded,
            "normalization": "R_C/Omega0 * integral_(g0 to gInfinity) omega_j",
            "formula": "-chi3(g)/7 * Tr_A/K(beta^j * sum_r d_g,r*(x_g Z_-r/6+y_g Z_-4r/6))",
            "full_6inverse_and_tame_phase_retained": True,
            "c1_phase_not_applied_a_second_time": True,
            "all_periods_in_actual_K_b": True})
        return values

    def hom_kernel(self, data, L, K, relative):
        name = "R754-streamed-original-period-constraints"
        prior = self.cached(name)
        chains = data["integral-compact-Manin-cycles.json.gz"]["compact_cycles_in_oriented_Manin_edges"]
        basis = {} if not prior else {int(p): [K.decode(x) for x in row] for p, row in prior["basis"].items()}
        pivots = [] if not prior else prior["independent_source_rows"]
        closed = [] if not prior else [[L.decode(x) for x in row] for row in prior["closed_periods"]]
        bp = [L.one]
        for _ in range(6):
            bp.append(bp[-1]*L.gen)
        if not (prior and prior["complete"]):
            for i in range(len(closed), len(chains)):
                columns = [sum((int(c)*relative[int(edge)][j] for edge, c in chains[i]), L.zero)
                           for j in range(6)]
                products = [[columns[j]*bp[t] for t in range(7)] for j in range(6)]
                for a in range(1, 7):
                    row = [K.elt(products[j][t].a[a], products[j][t].b[a])
                           for j in range(6) for t in range(7)]
                    if insert_row(basis, row, K):
                        pivots.append([i, a])
                        assert len(basis) <= 36, "Original period constraints exceeded the proven Hom codimension"
                closed.append(columns)
                if (i+1) % 16 == 0:
                    self.store(name, {"complete": False,
                        "basis": {str(p): [x.encode() for x in row] for p, row in basis.items()},
                        "independent_source_rows": pivots,
                        "closed_periods": [[x.encode() for x in row] for row in closed]})
            assert len(closed) == len(chains) == 800
            assert len(basis) == 36
            self.store(name, {"complete": True,
                "basis": {str(p): [x.encode() for x in row] for p, row in basis.items()},
                "independent_source_rows": pivots,
                "closed_periods": [[x.encode() for x in row] for row in closed],
                "all_4800_nonconstant_rows_processed": True, "rank": 36})
        assert len(basis) == 36 and len(closed) == 800
        free = [j for j in range(42) if j not in basis]
        assert len(free) == 6
        kernels = []
        for f in free:
            column = [K.zero for _ in range(42)]
            column[f] = K.one
            for pivot, row in basis.items():
                column[pivot] = -row[f]
            for row in basis.values():
                assert sum((x*y for x, y in zip(row, column)), K.zero) == 0
            kernels.append(column)
        name = "R754-all-original-closed-period-verification"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return prior
        maps = []
        for column in kernels:
            maps.append([L.elt(fmpq_poly([column[7*j+t].a[0] for t in range(7)]),
                               fmpq_poly([column[7*j+t].b[0] for t in range(7)]))
                         for j in range(6)])
        integral = [] if not prior else prior["periods_in_K"]
        for i in range(len(integral), 800):
            row = []
            for mapping in maps:
                value = sum((mapping[j]*closed[i][j] for j in range(6)), L.zero)
                assert all(value.a[t] == 0 and value.b[t] == 0 for t in range(1, 7))
                row.append([eq(value.a[0]), eq(value.b[0])])
            integral.append(row)
            if (i+1) % 32 == 0:
                self.store(name, {"complete": False, "periods_in_K": integral})
        clearing = [1]*6
        for row in integral:
            for k in range(6):
                for scalar in row[k]:
                    clearing[k] = math.lcm(clearing[k], int(scalar[1]))
        for row in integral:
            for k in range(6):
                assert all((clearing[k]*dq(q)).denom() == 1 for q in row[k])
        result = {"complete": True, "kernel_dimension_over_K": 6, "constraint_rank": 36,
            "free_columns": free, "column_order": "(j,t), j=0..5,t=0..6, v_j=sum_t x_jt*b^t",
            "kernel_vectors_K_42_coordinates": [[x.encode() for x in v] for v in kernels],
            "six_L_differential_vectors": [[x.encode() for x in v] for v in maps],
            "periods_in_K": integral, "integer_period_clearing_factors": [str(x) for x in clearing],
            "all_800_original_chains_verified_for_each_of_six_vectors": True,
            "no_clearing_factor_assumed_a_p_unit": True,
            "actual_q_functions_beta_or_height_computed": False}
        self.store(name, result)
        return result


def ffmul(x, y):
    a, b = x
    c, d = y
    return ((a*c-b*d) % P, (a*d+b*c-b*d) % P)


def affine(vector, a, b):
    ans = [fmpz_poly([]) for _ in range(P)]
    for r, value in enumerate(vector):
        ans[(a*r+b) % P] += value
    zero = ans[0]
    return [x-zero for x in ans]


def matmul(a, b, p):
    return tuple(x % p for x in (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                                 a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


def integer_matmul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def tame_coefficients():
    identity = (1, 0, 0, 1)
    generators = [((0, 1, 1, 0), (0, 1, 1, 0)),
                  ((1, 1, 0, 1), (-1, 0, -1, 1))]
    found, queue = {identity: identity}, deque([identity])
    while queue:
        a = queue.popleft()
        for g, mg in generators:
            dest = matmul(a, g, 2)
            image = integer_matmul(mg, found[a])
            if dest in found:
                assert found[dest] == image
            else:
                found[dest] = image
                queue.append(dest)
    assert len(found) == 6
    return found


def insert_row(basis, row, K):
    row = list(row)
    for p in sorted(basis):
        if row[p]:
            factor = row[p]
            row = [x-factor*y for x, y in zip(row, basis[p])]
    if not any(row):
        return False
    pivot = next(j for j, x in enumerate(row) if x)
    inverse = row[pivot].inverse()
    row = [x*inverse for x in row]
    for p, old in list(basis.items()):
        if old[pivot]:
            factor = old[pivot]
            basis[p] = [x-factor*y for x, y in zip(old, row)]
    basis[pivot] = row
    return True


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual exact arithmetic is restricted to the public repository Actions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--inputs", type=Path, required=True)
    args = parser.parse_args()
    job = Job(args.output, args.inputs)
    try:
        data = job.inputs_read()
        final = args.output/"p41-original-period-and-Hom-kernel-certificate.json"
        if final.exists():
            completed = read(final)
            assert completed["configuration"] == job.tag and completed["complete"]
            assert completed["constraint_rank"] == 36 and completed["kernel_dimension_over_K"] == 6
            for stage in completed["stages"]:
                assert sha(args.output/stage["file"]) == stage["sha256"]
            save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
                "source_sha256": sha(__file__), "certificate_sha256": sha(final),
                "rank": 36, "kernel_dimension_over_K": 6,
                "all_800_original_chains_verified": True, "reused_complete": True})
            return
        M, L, K, sub, b, S, H = job.fields(data)
        xi = job.pairing(M)
        zstar, inverse = job.projector(M, L, sub, b, S)
        powers = job.xi_powers(M, xi)
        weights = job.trace_weights(M, sub, H)
        additive = job.additive_periods(M, L, K, zstar, inverse, powers, weights)
        vectors = job.finite_vectors(data)
        relative = job.edge_periods(data, L, additive, vectors)
        result = job.hom_kernel(data, L, K, relative)
        stages = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                  for p in sorted(args.output.glob("R754-*.json.gz"))]
        certificate = {"result": RESULT, "configuration": job.tag, "complete": True,
            "p": P, "source_genus": 400, "c1_coset": 4424, "c0_cosets": [2876, 2822, 2823],
            "actual_target_model": "R735 b in the same retained U algebra",
            "normalized_period_field": "L=K(b), degree7 over K, embedded in retained K(U)",
            "normalized_additive_values_computed": 40, "relative_edges": 819,
            "original_compact_chains": 800, "all_periods_exact": True,
            "constraint_columns": 42, "constraint_rows": 4800,
            "constraint_rank": result["constraint_rank"],
            "kernel_dimension_over_K": result["kernel_dimension_over_K"],
            "all_800_chains_verified_for_all_six_kernel_vectors": True,
            "integer_clearing_factor_bit_lengths": [int(x).bit_length() for x in result["integer_period_clearing_factors"]],
            "old_target_topology_torus_average_or_L_values_recomputed": False,
            "actual_q_functions_beta_or_height_computed": False,
            "stages": stages, "seconds": time.monotonic()-job.started}
        save(final, certificate)
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(final),
            "rank": 36, "kernel_dimension_over_K": 6,
            "all_800_original_chains_verified": True})
        print(json.dumps({"result": RESULT, "complete": True, "rank": 36,
                          "kernel_dimension_over_K": 6}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()


