#!/usr/bin/env python3
"""Four exact coefficients for the frozen eight-packet R183/R187 width gate.

No forcing, geometric integration, old compiler, W basis, or LP is run here.
Actual frozen-profile arithmetic is allowed only in the named public Actions repo.
--toy-only uses small invented polynomials and never calls actual().
Reports are ephemeral: publish only source/parameters/run/output SHA, in accordance
with README 15. This module does not call GitHub or publish an artifact.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
from fractions import Fraction as Q

SCHEMA = "visible-flex-derivative-packet-four-coefficient-gate-v1"
REPOSITORY = "Rogerhu12/math-research-public"
DEFINITION = {
    "constant_state": {"k": 0, "h": 1, "omega": 0},
    "rho": "51480*t^7*(1-t)^7 on [0,1], zero outside",
    "step": "S(t)=integral_0^t rho, extended by 0 and 1",
    "eta": "65536*t^8*(1-t)^8 on [0,1], zero outside",
    "f0": "S(x-8)-S(x-12)",
    "g0": "S(x-10)-S(x-14)",
    "left_bump_origins": [1, 3, 5],
    "left_square_amplitudes": ["7*A/B", "-16*A/B", "9*A/B"],
    "A": "integral_0^1 (rho')^2",
    "B": "integral_0^1 (eta'')^2",
    "packet_translations": [20*j for j in range(8)],
    "packet_cubes": [(-1)**j*math.comb(7, j) for j in range(8)],
    "dilation": "q_lambda(x)=q_raw(x/lambda), lambda>0",
    "undilated_support": [1, 155],
    "physical_strip_condition": "[lambda,155*lambda] is compactly inside I",
    "moment_convention": "ordinary complex squares, no complex conjugation",
    "regularity": "C7; C-infinity transfer requires the stated strictness argument",
}
START = time.monotonic()
LIMITS = None

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()

def sha(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()

class Stop(Exception):
    pass

class Unresolved(Stop):
    pass

class Limits:
    def __init__(self, seconds, memory_mib, fraction_bits):
        self.seconds, self.memory_mib, self.fraction_bits = seconds, memory_mib, fraction_bits
        self.polls = 0
    def check(self):
        self.polls += 1
        if time.monotonic()-START > self.seconds:
            raise Stop("time_budget")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024*self.memory_mib:
            raise Stop("polled_peak_rss_budget")
    def rational(self, x):
        if max(abs(x.numerator).bit_length(), x.denominator.bit_length()) > self.fraction_bits:
            raise Stop("exact_fraction_bit_budget")

def check():
    if LIMITS:
        LIMITS.check()

def trim(p):
    p = list(map(Q, p))
    while p and not p[-1]:
        p.pop()
    if LIMITS:
        for a in p:
            LIMITS.rational(a)
    return tuple(p)

def pc(a):
    return trim([a])

def padd(*polys):
    n = max((len(p) for p in polys), default=0)
    out = [Q(0)]*n
    for p in polys:
        for i, a in enumerate(p):
            out[i] += a
    return trim(out)

def pscale(p, a):
    return trim([Q(a)*v for v in p])

def pneg(p):
    return pscale(p, -1)

def pmul(p, q):
    check()
    if not p or not q:
        return ()
    out = [Q(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                if b:
                    out[i+j] += a*b
    return trim(out)

def ppow(p, n):
    if n < 0:
        raise ValueError("polynomial powers must be nonnegative")
    out = pc(1)
    while n:
        if n & 1:
            out = pmul(out, p)
        n //= 2
        if n:
            p = pmul(p, p)
    return out

def pdiff(p):
    return trim([i*p[i] for i in range(1, len(p))])

def pint(p):
    return trim([Q(0)]+[a/Q(i+1) for i, a in enumerate(p)])

def peval(p, x):
    v = Q(0)
    for a in reversed(p):
        v = v*x+a
    return v

def integral01(p):
    return sum((a/Q(i+1) for i, a in enumerate(p)), Q(0))

def pdump(p):
    return [str(a) for a in p]

def densities(phi, left, transverse_constant_squared):
    """The four REAL densities before the common factor 1/128.

    A piece is phi+i*c or c+i*phi, with x=t+left. The formula is identical
    for either orientation and uses c^2, never a Hermitian substitution.
    """
    x = trim([left, 1])
    p, r = pdiff(phi), pdiff(pdiff(phi))
    x2, r2, p2 = ppow(x, 2), ppow(r, 2), ppow(p, 2)
    r3, r4, p4 = pmul(r2, r), ppow(r, 4), ppow(p, 4)
    A = padd(phi, pneg(pmul(x, p)), pscale(pmul(x2, r), Q(1, 6)))
    B = padd(p, pscale(pmul(x, r), Q(-1, 3)))
    U = padd(phi, pneg(pmul(x, p)))
    V = padd(phi, pscale(pmul(x, p), Q(-1, 3)))
    c2 = Q(transverse_constant_squared)
    d0 = pscale(r4, Q(1, 12))
    d2 = padd(pscale(pmul(r2, ppow(B, 2)), 2),
              pscale(pmul(A, r3), Q(-2, 3)),
              pscale(pmul(x2, r4), Q(5, 36)))
    d4 = padd(pscale(pmul(r2, ppow(U, 2)), 2),
              pscale(pmul(pmul(x2, r2), ppow(B, 2)), 2),
              pscale(pmul(ppow(x, 4), r4), Q(1, 36)),
              pscale(p4, Q(2, 3)), pscale(r2, -2*c2))
    d6 = padd(pscale(pmul(pmul(x2, r2), ppow(A, 2)), 2),
              pscale(pmul(ppow(x, 6), r4), Q(1, 36)),
              pscale(pmul(p2, ppow(V, 2)), 4),
              pscale(pmul(x2, p4), Q(2, 9)),
              pscale(pmul(x2, r2), -2*c2), pscale(p2, -4*c2))
    return [d0, d2, d4, d6]

EXP = [(i, j, k) for i in range(3) for j in range(3) for k in range(3)]
INDEX = {e: i for i, e in enumerate(EXP)}
RADICANDS = (7, 21, 35)

class Alg:
    """Exact expressions in positive cube roots, with rational slot arithmetic.

    A nonzero slot vector is NOT used as a real nonzero test. Every real sign
    decision is made by a strict rational interval, or by exact slot-zero.
    """
    def __init__(self, values=None):
        self.v = tuple(Q(0) for _ in EXP) if values is None else tuple(map(Q, values))
        if len(self.v) != 27:
            raise ValueError("27 slots required")
        if LIMITS:
            for a in self.v:
                LIMITS.rational(a)
    @staticmethod
    def of(x):
        if isinstance(x, Alg):
            return x
        v = [Q(0)]*27
        v[0] = Q(x)
        return Alg(v)
    @staticmethod
    def monomial(e, c=1):
        v = [Q(0)]*27
        v[INDEX[tuple(e)]] = Q(c)
        return Alg(v)
    def __add__(self, other):
        other = Alg.of(other)
        return Alg([a+b for a, b in zip(self.v, other.v)])
    __radd__ = __add__
    def __neg__(self):
        return Alg([-a for a in self.v])
    def __sub__(self, other):
        return self+-Alg.of(other)
    def __rsub__(self, other):
        return Alg.of(other)+-self
    def __mul__(self, other):
        check()
        other = Alg.of(other)
        out = [Q(0)]*27
        for i, a in enumerate(self.v):
            if not a:
                continue
            for j, b in enumerate(other.v):
                if not b:
                    continue
                ex = [EXP[i][k]+EXP[j][k] for k in range(3)]
                factor = Q(1)
                for k in range(3):
                    if ex[k] >= 3:
                        ex[k] -= 3
                        factor *= RADICANDS[k]
                out[INDEX[tuple(ex)]] += a*b*factor
        return Alg(out)
    __rmul__ = __mul__
    def __pow__(self, n):
        if n < 0:
            raise ValueError("only nonnegative algebraic powers")
        out = Alg.of(1)
        for _ in range(n):
            out = out*self
        return out
    def rational_scale(self, x):
        return Alg([Q(x)*a for a in self.v])
    def zero(self):
        return not any(self.v)
    def dump(self):
        return [[list(EXP[i]), str(a)] for i, a in enumerate(self.v) if a]

def ivadd(a, b):
    return (a[0]+b[0], a[1]+b[1])

def ivmul(a, b):
    t = [x*y for x in a for y in b]
    return (min(t), max(t))

def ivdiv_positive(a, b):
    if b[0] <= 0:
        raise Unresolved("nonpositive interval denominator")
    return ivmul(a, (1/b[1], 1/b[0]))

def ivsqrt(a, bits):
    if a[0] < 0:
        raise Unresolved("negative square-root interval")
    d = 1 << bits
    lo = math.isqrt((a[0].numerator*d*d)//a[0].denominator)
    hi = math.isqrt((a[1].numerator*d*d)//a[1].denominator)+1
    return (Q(lo, d), Q(hi, d))

class SignWorld:
    def __init__(self, max_bits=1024):
        self.max_bits, self.bits = max_bits, 0
        self.roots = [(Q(0), Q(4)) for _ in RADICANDS]
        self.events = []
    def refine(self, bits):
        bits = min(bits, self.max_bits)
        while self.bits < bits:
            check()
            new = []
            for n, (lo, hi) in zip(RADICANDS, self.roots):
                mid = (lo+hi)/2
                if mid**3 < n:
                    lo = mid
                elif mid**3 > n:
                    hi = mid
                else:
                    lo = hi = mid
                new.append((lo, hi))
            self.roots = new
            self.bits += 1
    def interval(self, x):
        x = Alg.of(x)
        out = (Q(0), Q(0))
        for e, c in zip(EXP, x.v):
            if not c:
                continue
            term = (Q(1), Q(1))
            for j in range(3):
                for _ in range(e[j]):
                    term = ivmul(term, self.roots[j])
            out = ivadd(out, ivmul((c, c), term))
        return out
    def sign(self, x, label):
        x = Alg.of(x)
        if x.zero():
            self.events.append({"label": label, "sign": 0, "proof": "exact_slot_zero"})
            return 0
        if not any(x.v[1:]):
            ans = 1 if x.v[0] > 0 else -1
            self.events.append({"label": label, "sign": ans, "proof": "exact_rational"})
            return ans
        self.refine(max(16, self.bits))
        while True:
            lo, hi = self.interval(x)
            if lo > 0 or hi < 0:
                ans = 1 if lo > 0 else -1
                self.events.append({"label": label, "sign": ans, "proof": "strict_rational_interval",
                                    "root_bits": self.bits, "lower": str(lo), "upper": str(hi),
                                    "expression_sha256": sha(x.dump())})
                return ans
            if self.bits >= self.max_bits:
                raise Unresolved("algebraic sign not separated: "+label)
            self.refine(min(self.max_bits, max(self.bits+16, 2*self.bits)))

def algebraic_value(coeffs, u):
    out = Alg.of(0)
    for a in reversed(coeffs):
        out = out*u+a
    return out

def negative_witness(coeffs, world, location):
    """Return a strictly certified rational lambda>0, not a modular/float witness."""
    if location in ("zero", "infinity"):
        for j in range(1, world.max_bits+1):
            lam = Q(1, 1 << j) if location == "zero" else Q(1 << j)
            value = algebraic_value(coeffs, lam*lam)
            if world.sign(value, "witness_%s_%d" % (location, j)) < 0:
                return {"lambda": str(lam), "u": str(lam*lam),
                        "value": value.dump(), "strict_sign": -1,
                        "physical_support": [str(lam), str(155*lam)]}
        raise Unresolved("no dyadic negative witness within budget")
    degree = len(coeffs)-1
    refinement_levels = []
    blevel = 16
    while blevel < world.max_bits:
        refinement_levels.append(blevel)
        blevel *= 2
    refinement_levels.append(world.max_bits)
    for bits in refinement_levels:
        world.refine(bits)
        if degree == 2:
            c, b, a = coeffs
            numerator = world.interval(-b)
            denominator = world.interval(2*a)
        elif degree == 3:
            d, c, b, a = coeffs
            delta = b*b-3*a*c
            di = world.interval(delta)
            if di[0] <= 0:
                continue
            numerator = ivadd(world.interval(-b), ivsqrt(di, bits))
            denominator = world.interval(3*a)
        else:
            raise ValueError("internal minimum requires degree 2 or 3")
        if denominator[0] <= 0:
            continue
        ri = ivdiv_positive(numerator, denominator)
        if ri[0] <= 0:
            continue
        li = ivsqrt(ri, bits)
        lam = (li[0]+li[1])/2
        value = algebraic_value(coeffs, lam*lam)
        if world.sign(value, "internal_minimum_witness_%d" % bits) < 0:
            return {"lambda": str(lam), "u": str(lam*lam),
                    "minimum_u_enclosure": list(map(str, ri)),
                    "value": value.dump(), "strict_sign": -1,
                    "physical_support": [str(lam), str(155*lam)]}
    raise Unresolved("internal negative minimum lacks a rational witness within budget")

def halfline_gate(coeffs, world):
    """Exact global sign on u>=0, with a rational lambda witness when negative."""
    coeffs = list(map(Alg.of, coeffs))
    while coeffs and world.sign(coeffs[-1], "leading_%d" % (len(coeffs)-1)) == 0:
        coeffs.pop()
    if not coeffs:
        return {"classification": "identically_zero", "degree": -1,
                "nonnegative_for_all_positive_lambda": True,
                "cubic_compactified_strict_positive": False}
    degree = len(coeffs)-1
    if world.sign(coeffs[-1], "leading_nonzero") < 0:
        return {"classification": "negative_at_some_positive_width", "degree": degree,
                "reason": "negative_leading_coefficient",
                "witness": negative_witness(coeffs, world, "infinity")}
    sd = world.sign(coeffs[0], "constant")
    if sd < 0:
        return {"classification": "negative_at_some_positive_width", "degree": degree,
                "reason": "negative_at_zero_limit",
                "witness": negative_witness(coeffs, world, "zero")}
    strict = sd > 0
    if degree <= 1:
        return {"classification": "nonnegative_at_all_widths", "degree": degree,
                "nonnegative_for_all_positive_lambda": True,
                "strict_on_nonnegative_u": strict,
                "cubic_compactified_strict_positive": False}
    if degree == 2:
        c, b, a = coeffs
        if world.sign(b, "quadratic_linear") < 0:
            sm = world.sign(4*a*c-b*b, "quadratic_minimum_numerator")
            if sm < 0:
                return {"classification": "negative_at_some_positive_width", "degree": degree,
                        "reason": "negative_internal_minimum",
                        "witness": negative_witness(coeffs, world, "internal")}
            strict = strict and sm > 0
        return {"classification": "nonnegative_at_all_widths", "degree": degree,
                "nonnegative_for_all_positive_lambda": True,
                "strict_on_nonnegative_u": strict,
                "cubic_compactified_strict_positive": False}
    if degree != 3:
        raise ValueError("this gate is only for degree at most three")
    d, c, b, a = coeffs
    delta = b*b-3*a*c
    sdelta = world.sign(delta, "cubic_delta")
    sb = world.sign(b, "cubic_b")
    sc = world.sign(c, "cubic_c")
    if sdelta > 0 and (sb < 0 or sc < 0):
        T = 2*b**3-9*a*b*c+27*a*a*d
        sT = world.sign(T, "cubic_T")
        if sT <= 0:
            return {"classification": "negative_at_some_positive_width", "degree": degree,
                    "reason": "negative_internal_minimum_T",
                    "witness": negative_witness(coeffs, world, "internal")}
        discriminant_test = T*T-4*delta**3
        sm = world.sign(discriminant_test, "cubic_minimum_squared_test")
        if sm < 0:
            return {"classification": "negative_at_some_positive_width", "degree": degree,
                    "reason": "negative_internal_minimum_squared_test",
                    "witness": negative_witness(coeffs, world, "internal")}
        strict = strict and sm > 0
    return {"classification": "nonnegative_at_all_widths", "degree": degree,
            "nonnegative_for_all_positive_lambda": True,
            "strict_on_nonnegative_u": strict,
            "cubic_compactified_strict_positive": strict}

def endpoint_zero(p, derivative_orders):
    out = []
    for j in derivative_orders:
        d = p
        for _ in range(j):
            d = pdiff(d)
        out.append(peval(d, Q(0)) == 0 and peval(d, Q(1)) == 0)
    return all(out)

def translate_moment(phi, left, which):
    r = pdiff(pdiff(phi))
    p = pdiff(phi)
    x = trim([left, 1])
    if which == 0:
        return integral01(ppow(r, 2))
    if which == 1:
        return integral01(pmul(x, ppow(r, 2)))
    return integral01(padd(pmul(ppow(x, 2), ppow(r, 2)), pscale(ppow(p, 2), 2)))

def frozen_polynomials():
    t, one_minus_t = trim([0, 1]), trim([1, -1])
    rho = pscale(pmul(ppow(t, 7), ppow(one_minus_t, 7)), 51480)
    S = pint(rho)
    eta = pscale(pmul(ppow(t, 8), ppow(one_minus_t, 8)), 65536)
    return rho, S, eta

def actual(report, args):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise Stop("actual_requires_the_named_public_Actions_repository")
    report["stage"] = "frozen_profile_exact_moments"
    rho, S, eta = frozen_polynomials()
    if integral01(rho) != 1 or peval(S, Q(1)) != 1:
        raise AssertionError("step normalization")
    if not endpoint_zero(rho, range(7)) or not endpoint_zero(eta, range(8)):
        raise AssertionError("C7 endpoint jets")
    A = integral01(ppow(pdiff(rho), 2))
    B = integral01(ppow(pdiff(pdiff(eta)), 2))
    if A <= 0 or B <= 0:
        raise AssertionError("positive exact Sobolev energies")
    z = [Q(n)*A/B for n in (7, -16, 9)]
    f_origins, g_origins = (8, 12), (10, 14)
    moments = []
    for order in range(3):
        defect = sum((translate_moment(S, x, order) for x in f_origins), Q(0))
        defect -= sum((translate_moment(S, x, order) for x in g_origins), Q(0))
        patch = sum((zj*translate_moment(eta, x, order)
                     for zj, x in zip(z, (1, 3, 5))), Q(0))
        if defect+patch:
            raise AssertionError("three ordinary complex moments must be zero")
        moments.append({"order": order, "rectangle": str(defect), "left_patches": str(patch),
                        "total": "0"})
    if [row["rectangle"] for row in moments] != ["0", str(-4*A), str(-92*A)]:
        raise AssertionError("frozen moment defect identity")
    report["moments"] = {"A": str(A), "B": str(B), "square_amplitudes": list(map(str, z)),
                         "three_exact_complex_moments": moments,
                         "single_packet_real_I0_f": str(18*A), "single_packet_real_I0_g": str(18*A),
                         "cross_moments_zero_by_derivative_disjointness": True,
                         "C7_endpoint_jets_verified": True}
    report["stage"] = "four_rational_packet_coefficients"
    raw_I4 = 4*integral01(ppow(pdiff(rho), 4))
    raw_I4 += sum((zj*zj for zj in z), Q(0))*integral01(ppow(pdiff(pdiff(eta)), 4))
    if raw_I4 <= 0:
        raise AssertionError("positive ordinary-complex fourth derivative energy")
    packet_coefficients = []
    groups = {n: [Q(0)]*4 for n in (1, 7, 21, 35)}
    for j in range(8):
        values = [Q(0)]*4
        pieces = [(S, 8+20*j, 0, Q(1)),
                  (S, 10+20*j, 1, Q(1)),
                  (padd(pc(1), pneg(S)), 12+20*j, 1, Q(1)),
                  (padd(pc(1), pneg(S)), 14+20*j, 0, Q(1))]
        pieces += [(eta, left+20*j, 0, zj*zj) for left, zj in zip((1, 3, 5), z)]
        for phi, left, c2, fourth_amplitude in pieces:
            check()
            for k, density in enumerate(densities(phi, left, c2)):
                values[k] += fourth_amplitude*integral01(density)/128
        if values[0] != raw_I4/1536:
            raise AssertionError("packet lambda^-7 coefficient")
        n = math.comb(7, j)
        for k in range(4):
            groups[n][k] += values[k]
        packet_coefficients.append({"packet": j, "translation": 20*j,
                                    "amplitude_cubed": (-1)**j*n,
                                    "four_coefficients": list(map(str, values))})
    report["four_coefficients_complete"] = True
    report["packet_coefficients"] = packet_coefficients
    report["radical_group_coefficients"] = [
        {"binomial": n, "multiplier": "%d^(4/3)" % n, "values": list(map(str, groups[n]))}
        for n in (1, 7, 21, 35)]
    coeffs = []
    for k in range(4):
        c = Alg.of(groups[1][k])
        c += Alg.monomial((1, 0, 0), 7*groups[7][k])
        c += Alg.monomial((0, 1, 0), 21*groups[21][k])
        c += Alg.monomial((0, 0, 1), 35*groups[35][k])
        coeffs.append(c)
    report["lambda7_ReF_coefficients"] = [
        {"lambda_power": 2*i, "exact_positive_cube_root_slots": c.dump()}
        for i, c in enumerate(coeffs)]
    report["raw_single_packet_I4"] = str(raw_I4)
    report["four_coefficient_sha256"] = sha(report["lambda7_ReF_coefficients"])
    report["stage"] = "positive_halfline_algebraic_gate"
    world = SignWorld(args.max_root_bits)
    try:
        report["gate"] = halfline_gate(coeffs, world)
        if report["gate"]["classification"] == "negative_at_some_positive_width":
            report["gate"]["positive_width_real_part_zero_exists_by_IVT"] = True
            report["gate"]["that_real_part_zero_does_not_pay_the_complex_gate"] = True
        report["completion"] = "complete"
    finally:
        report["algebraic_sign_proofs"] = world.events
        report["final_cube_root_intervals"] = [list(map(str, z)) for z in world.roots]
        report["final_root_bits"] = world.bits
    report["stage"] = "finished"

class CQ:
    """Tiny Gaussian rationals, used only by artificial direct identity checks."""
    def __init__(self, a=0, b=0):
        self.a, self.b = Q(a), Q(b)
    @staticmethod
    def of(x):
        return x if isinstance(x, CQ) else CQ(x)
    def __add__(self, x):
        x = CQ.of(x)
        return CQ(self.a+x.a, self.b+x.b)
    __radd__ = __add__
    def __neg__(self):
        return CQ(-self.a, -self.b)
    def __sub__(self, x):
        return self+-CQ.of(x)
    def __rsub__(self, x):
        return CQ.of(x)+-self
    def __mul__(self, x):
        x = CQ.of(x)
        return CQ(self.a*x.a-self.b*x.b, self.a*x.b+self.b*x.a)
    __rmul__ = __mul__
    def __pow__(self, n):
        out = CQ(1)
        for _ in range(n):
            out = out*self
        return out

def direct_Q(x, z, p, r):
    Qx = 1+x*x
    return (2*Qx*r*r*((z-x*p+Q(1, 6)*(x*x-1)*r)**2+(p-Q(1, 3)*x*r)**2)
            +Q(1, 36)*Qx**3*r**4
            +4*p*p*(z-Q(1, 3)*x*p)**2
            +Q(2, 9)*(x*x+3)*p**4)

def toy(report):
    checks = []
    def ok(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    ok("artificial_polynomial_product", pmul((Q(1), Q(1)), (Q(1), Q(-1))) == (Q(1), Q(0), Q(-1)))
    ok("artificial_exact_integral", integral01((Q(1), Q(2), Q(3))) == 3)
    alpha = Alg.monomial((1, 0, 0))
    ok("cube_root_formal_relation", (alpha**3-7).zero())
    world = SignWorld(128)
    ok("strict_cube_root_sign", world.sign(alpha-1, "toy") == 1)
    oracle_examples = [
        ([1], "nonnegative_at_all_widths"),
        ([-1, 1], "negative_at_some_positive_width"),
        ([1, -3, 1], "negative_at_some_positive_width"),
        ([1, -2, 1], "nonnegative_at_all_widths"),
        ([1, 1, 1, 1], "nonnegative_at_all_widths"),
        ([1, -2, -2, 1], "negative_at_some_positive_width"),
        ([2, -3, 0, 1], "nonnegative_at_all_widths"),
        ([1, 0, 0, -1], "negative_at_some_positive_width"),
        ([1, -1], "negative_at_some_positive_width"),
        ([0, 0, 0, 0], "identically_zero"),
    ]
    for j, (coeffs, expected) in enumerate(oracle_examples):
        got = halfline_gate(coeffs, SignWorld(128))
        ok("artificial_halfline_case_%d" % j, got["classification"] == expected)
        if "witness" in got:
            lam = Q(got["witness"]["lambda"])
            ok("artificial_witness_%d" % j, peval(tuple(map(Q, coeffs)), lam*lam) < 0)
    phi = trim([1, -1, 1])
    d = densities(phi, 3, 4)
    t = Q(2, 5)
    x = 3+t
    v, p, r = peval(phi, t), peval(pdiff(phi), t), peval(pdiff(pdiff(phi)), t)
    for width in (Q(2, 3), Q(3)):
        target = sum((peval(d[j], t)*width**(2*j) for j in range(4)), Q(0))
        for orientation in (0, 1):
            z, qp, qr = (CQ(v, 2), CQ(p/width), CQ(r/width**2)) if orientation == 0 else (
                CQ(2, v), CQ(0, p/width), CQ(0, r/width**2))
            got = width**8*direct_Q(width*x, z, qp, qr).a
            ok("artificial_density_%s_%d" % (width, orientation), got == target)
    report.update({"completion": "toy_passed", "checks": checks, "check_count": len(checks),
                   "actual_profile_integrations": 0, "frozen_definition_evaluated": False})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", help="Ephemeral report path; never publish the machine report")
    parser.add_argument("--seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=512)
    parser.add_argument("--fraction-bits", type=int, default=16384)
    parser.add_argument("--max-root-bits", type=int, default=1024)
    args = parser.parse_args()
    if not (0 < args.seconds <= 600 and 64 <= args.memory_mib <= 2048
            and 512 <= args.fraction_bits <= 65536 and 16 <= args.max_root_bits <= 4096):
        parser.error("bounded resource arguments are required")
    global LIMITS
    LIMITS = Limits(args.seconds, args.memory_mib, args.fraction_bits)
    source_bytes = Path(__file__).read_bytes()
    report = {
        "schema": SCHEMA, "completion": "started",
        "driver": {"bytes": len(source_bytes), "sha256": hashlib.sha256(source_bytes).hexdigest()},
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_source_commit": os.environ.get("GITHUB_SHA"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "parameters": vars(args),
        "profile_definition": DEFINITION,
        "profile_definition_sha256": sha(DEFINITION),
        "scope": {
            "only_standard_constant_state": True, "original_eight_packets_unchanged": True,
            "ordinary_complex_local_quartic_formula": True,
            "no_forcing_or_geometry_recompiled": True,
            "no_fourth_range_or_geometric_embedding_certified": True,
            "a_zero_real_part_does_not_pay_the_complex_gate": True,
            "global_width_algebra_does_not_fit_all_widths_in_one_fixed_strip": True,
            "C_infinity_transfer_only_under_stated_strictness_conditions": True,
            "output_is_ephemeral_not_a_repository_or_release_artifact": True,
        },
        "resource_limits": {
            "wall_seconds": args.seconds, "polled_peak_rss_mib": args.memory_mib,
            "fraction_bits": args.fraction_bits, "cube_root_refinement_bits": args.max_root_bits,
            "rss_limit_is_polling_not_an_OS_hard_cap": True,
        },
    }
    code = 0
    try:
        if args.toy_only:
            toy(report)
        else:
            actual(report, args)
    except Unresolved as exc:
        report["completion"] = "sign_unresolved"
        report["reason"] = str(exc)
        code = 2
    except Stop as exc:
        report["completion"] = "budget_or_environment_exit"
        report["reason"] = str(exc)
        code = 2
    except Exception as exc:
        report["completion"] = "implementation_check_failed"
        report["error"] = {"type": type(exc).__name__, "message": str(exc)}
        code = 1
    report["seconds"] = time.monotonic()-START
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    payload = canonical(report)+b"\n"
    report_sha = hashlib.sha256(payload).hexdigest()
    if args.output:
        destination = Path(args.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
    # The action publisher records only this digest and source/parameters/run.
    # Mathematical coefficients/verdict remain available in the ephemeral report
    # for a human conclusion; the script never uploads a report or certificate.
    summary = {"schema": SCHEMA, "completion": report["completion"], "output_bytes": len(payload),
               "output_sha256": report_sha, "driver_sha256": report["driver"]["sha256"],
               "run_id": report["github_run_id"], "source_commit": report["github_source_commit"],
               "four_coefficients_complete": report.get("four_coefficients_complete", False),
               "gate": report.get("gate"), "check_count": report.get("check_count"),
               "reason": report.get("reason"), "error": report.get("error")}
    print(json.dumps(summary, sort_keys=True))
    if not args.toy_only and report.get("four_coefficients_complete"):
        print("MATHEMATICAL_FOUR_COEFFICIENTS="+json.dumps(report["lambda7_ReF_coefficients"], sort_keys=True))
        print("MATHEMATICAL_ALGEBRAIC_SIGN_PROOFS="+json.dumps(report.get("algebraic_sign_proofs", []), sort_keys=True))
    return code

if __name__ == "__main__":
    sys.exit(main())
