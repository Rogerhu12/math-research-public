#!/usr/bin/env python3
"""Bounded exact whole-function test for the reciprocal-pair pure fourth drift.

No profile value, numerical integration, geometry, optimization, or ODE is
evaluated. The research target is compiled only in this public repository's
GitHub Actions. Local --toy-only is restricted to small exact identities.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import sys
import time

import literature_range_profile_algebra as formal

EXPECTED_COMPILER_GIT_BLOB = "01c7424af3a96f2c2a0f0cb0c782b2037ff3ec74"
PARAMETERS = ("p0", "p1", "p2", "r0", "r1", "s0", "s1", "t1")
ZERO_MONOMIAL = (0, ())


class Limits:
    def __init__(self, seconds=240, nodes=500000, atoms=60000, terms=80000,
                 rewrites=250000, memory_mib=2048, rational_bits=8192):
        self.formal = formal.Budget(max_nodes=nodes, max_atoms=atoms,
                                   max_terms=terms, max_seconds=seconds)
        self.max_rewrites = rewrites
        self.memory_mib = memory_mib
        self.rational_bits = rational_bits
        self.calls = 0
        original_time_check = self.formal.time_check

        def guarded_time_check():
            original_time_check()
            # Polling threshold, not an operating-system hard memory limit.
            # Also covers the inherited constant-compiler time-check sites.
            rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if rss_kib > self.memory_mib * 1024:
                raise formal.CompilationBudgetExceeded("declared resident-memory polling threshold")

        self.formal.time_check = guarded_time_check

    def check(self):
        self.calls += 1
        if self.calls % 64 == 0:
            self.formal.time_check()


    def rational(self, value):
        value = F(value)
        if max(value.numerator.bit_length(), value.denominator.bit_length()) > self.rational_bits:
            raise formal.CompilationBudgetExceeded("declared rational bit-length budget")
        return value


class Expr:
    """A polynomial in xi, actual jets, and signed right Volterra primitives."""

    def __init__(self, ring, terms=None):
        self.ring = ring
        self.terms = {m: F(v) for m, v in (terms or {}).items() if v}
        if len(self.terms) > ring.limits.formal.max_terms:
            raise formal.CompilationBudgetExceeded("declared rational expression term budget")
        self._key = None

    def key(self):
        if self._key is None:
            self._key = tuple(sorted((m, c.numerator, c.denominator)
                                     for m, c in self.terms.items()))
        return self._key

    def __add__(self, other):
        other = self.ring.coerce(other)
        result = dict(self.terms)
        for m, c in other.terms.items():
            result[m] = result.get(m, F(0)) + c
            if not result[m]:
                del result[m]
        self.ring.limits.check()
        return Expr(self.ring, result)

    __radd__ = __add__

    def __neg__(self):
        return Expr(self.ring, {m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.ring.coerce(other))

    def __rsub__(self, other):
        return self.ring.coerce(other) - self

    def __mul__(self, other):
        other = self.ring.coerce(other)
        result = {}
        for index, (m, c) in enumerate(self.terms.items()):
            if index % 16 == 0:
                self.ring.limits.check()
            for n, d in other.terms.items():
                p = self.ring.p.multiply(m, n)
                result[p] = result.get(p, F(0)) + c*d
            if len(result) > self.ring.limits.formal.max_terms:
                raise formal.CompilationBudgetExceeded("declared rational product term budget")
        return Expr(self.ring, result)

    __rmul__ = __mul__

    def __truediv__(self, value):
        value = F(value)
        if not value:
            raise ZeroDivisionError("scalar expression division")
        return self * (1/value)

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError("only nonnegative polynomial powers are permitted")
        result = self.ring.number(1)
        base = self
        while power:
            if power & 1:
                result = result*base
            power >>= 1
            if power:
                base = base*base
        return result

    def D(self):
        return self.ring.derivative(self)

    def I(self):
        # I(F)(xi) = integral from the common right endpoint r to xi of F.
        return Expr(self.ring, {self.ring.p.primitive(m): c
                                for m, c in self.terms.items()})

    def J(self):
        # Positive right-tail integral; J' = -identity.
        return -self.I()


class Ring:
    def __init__(self, limits, algebra=None):
        self.limits = limits
        self.algebra = algebra or formal.Algebra(limits.formal)
        self.p = self.algebra.p
        self._derivatives = {}
        self._atom_hashes = {}

    def coerce(self, value):
        if isinstance(value, Expr):
            if value.ring is not self:
                raise ValueError("expressions must use the same right anchor and profile algebra")
            return value
        return self.number(value)

    def number(self, value):
        return Expr(self, {ZERO_MONOMIAL: F(value)} if value else {})

    def monomial(self, value):
        return Expr(self, {value: F(1)})

    def jet(self, order=0):
        return self.monomial(self.p.jet("q", order))

    def x(self):
        return self.monomial((1, ()))

    def derivative(self, expr):
        key = expr.key()
        if key in self._derivatives:
            return self._derivatives[key]
        result = {}
        for m, c in expr.terms.items():
            for n, count in self.p.derivative(m).items():
                result[n] = result.get(n, F(0)) + c*count
        out = Expr(self, result)
        self._derivatives[key] = out
        return out

    def variation(self, expr, direction):
        """Exact Frechet derivative: actual jets and a fixed Volterra anchor."""
        direction = self.coerce(direction)
        atom_cache = {}
        monomial_cache = {}
        direction_jets = {0: direction}

        def direction_jet(order):
            while order not in direction_jets:
                j = max(direction_jets)
                direction_jets[j+1] = direction_jets[j].D()
            return direction_jets[order]

        def atom_variation(atom):
            if atom in atom_cache:
                return atom_cache[atom]
            node = self.p.atoms[atom]
            if node[0] == "jet":
                if node[1] != "q":
                    raise ValueError("this pure-mode producer has one ordinary complex profile q")
                out = direction_jet(node[2])
            elif node[0] == "int_right":
                out = monomial_variation(node[1]).I()
            else:
                raise AssertionError(node)
            atom_cache[atom] = out
            return out

        def monomial_variation(m):
            if m in monomial_cache:
                return monomial_cache[m]
            power, atoms = m
            out = self.number(0)
            for atom, count in Counter(atoms).items():
                remaining = list(atoms)
                remaining.remove(atom)
                out += count*self.monomial((power, tuple(remaining)))*atom_variation(atom)
            monomial_cache[m] = out
            return out

        out = self.number(0)
        for m, c in expr.terms.items():
            out += c*monomial_variation(m)
        return out

    def atom_hash(self, atom):
        if atom in self._atom_hashes:
            return self._atom_hashes[atom]
        node = self.p.atoms[atom]
        if node[0] == "jet":
            payload = list(node)
        else:
            power, factors = node[1]
            payload = ["int_r_to_x", power, sorted(self.atom_hash(a) for a in factors)]
        value = hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()
        self._atom_hashes[atom] = value
        return value

    def digest(self, expr):
        rows = []
        for (power, factors), value in expr.terms.items():
            rows.append([power, sorted(self.atom_hash(a) for a in factors),
                         value.numerator, value.denominator])
        rows.sort()
        return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()

    def homogeneous_weight(self, expr):
        weights = {self.p.weight(m) for m in expr.terms}
        return next(iter(weights)) if len(weights) == 1 else (None if not weights else sorted(weights))


class RightIBP:
    """Sound, deliberately incomplete right-collar integration by parts.

    Each rewrite is exactly I(D F)=F for a positive-profile-weight F, hence
    F=0 on the common right collar. No left-tail value is set to zero.
    A failure of this normalizer to expose a dependence is not nonmembership
    in the space of actual profile functions.
    """

    def __init__(self, ring):
        self.ring = ring
        self.atom_cache = {}
        self.monomial_cache = {}
        self.primitive_cache = {}
        self.active = set()
        self.stats = {"primitive_calls": 0, "unique_high_jet_rewrites": 0,
                      "first_level_shuffle_rewrites": 0, "power_shuffle_rewrites": 0,
                      "cycle_fallbacks": 0, "weight_zero_not_rewritten": 0}

    def expression(self, expr):
        out = self.ring.number(0)
        for m, c in expr.terms.items():
            out += c*self.monomial(m)
        return out

    def monomial(self, m):
        if m in self.monomial_cache:
            return self.monomial_cache[m]
        out = self.ring.monomial((m[0], ()))
        for atom in m[1]:
            out = out*self.atom(atom)
        self.monomial_cache[m] = out
        return out

    def atom(self, atom):
        if atom in self.atom_cache:
            return self.atom_cache[atom]
        node = self.ring.p.atoms[atom]
        if node[0] == "jet":
            out = self.ring.monomial((0, (atom,)))
        elif node[0] == "int_right":
            out = self.primitive(self.monomial(node[1]))
        else:
            raise AssertionError(node)
        self.atom_cache[atom] = out
        return out

    def primitive(self, expr):
        # Linearity is exact. The integrand supplied by atom() has already
        # normalized all its factors; recursive remainders are normalized here.
        expr = self.expression(expr)
        out = self.ring.number(0)
        for m, c in expr.terms.items():
            out += c*self.primitive_monomial(m)
        return out

    def _local_integrand(self, m):
        return all(self.ring.p.atoms[a][0] == "jet" for a in m[1])

    def _integrand_order(self, m):
        # Semantic ordering, independent of atom allocation order.
        return m[0], tuple(sorted(tuple(self.ring.p.atoms[a]) for a in m[1]))

    def primitive_monomial(self, m):
        if m in self.primitive_cache:
            return self.primitive_cache[m]
        self.stats["primitive_calls"] += 1
        if self.stats["primitive_calls"] > self.ring.limits.max_rewrites:
            raise formal.CompilationBudgetExceeded("declared right-IBP rewrite budget")
        self.ring.limits.check()
        raw = self.ring.monomial(m).I()
        if self.ring.p.weight(m) == 0:
            self.stats["weight_zero_not_rewritten"] += 1
            return raw
        if m in self.active:
            # This is an exact no-op, never a declaration that the term is zero.
            self.stats["cycle_fallbacks"] += 1
            return raw
        self.active.add(m)
        try:
            local = [(self.ring.p.atoms[a][2], a) for a in m[1]
                     if self.ring.p.atoms[a][0] == "jet"]
            out = None
            if local:
                largest = max(order for order, atom in local)
                hits = [atom for order, atom in local if order == largest]
                kinds = {self.ring.p.atoms[a][1] for order, a in local}
                if largest >= 1 and len(hits) == 1 and kinds == {"q"}:
                    factors = list(m[1])
                    factors.remove(hits[0])
                    factors.extend(self.ring.p.jet("q", largest-1)[1])
                    antiderivative_monomial = (m[0], tuple(sorted(factors)))
                    antiderivative = self.ring.monomial(antiderivative_monomial)
                    differential = antiderivative.D()
                    coefficient = differential.terms.get(m, F(0))
                    if coefficient:
                        remainder = differential - coefficient*self.ring.monomial(m)
                        out = (self.monomial(antiderivative_monomial)
                               - self.primitive(remainder))/coefficient
                        self.stats["unique_high_jet_rewrites"] += 1
            if out is None:
                integrals = [a for a in m[1] if self.ring.p.atoms[a][0] == "int_right"]
                local_factors = tuple(a for a in m[1] if self.ring.p.atoms[a][0] == "jet")
                local_monomial = (m[0], local_factors)
                if integrals and len(set(integrals)) == 1:
                    atom = integrals[0]
                    integrand = self.ring.p.atoms[atom][1]
                    if self._local_integrand(integrand) and local_monomial == integrand:
                        # I((I f)^n f)=(I f)^(n+1)/(n+1), same right endpoint.
                        out = self.ring.monomial((0, tuple([atom]*(len(integrals)+1))))/(len(integrals)+1)
                        self.stats["power_shuffle_rewrites"] += 1
                if out is None and len(integrals) == 1:
                    atom = integrals[0]
                    integrand = self.ring.p.atoms[atom][1]
                    if (self._local_integrand(integrand) and
                            self.ring.p.weight(local_monomial) > 0 and
                            self._integrand_order(integrand) > self._integrand_order(local_monomial)):
                        other = self.ring.p.primitive(local_monomial)[1][0]
                        product = self.ring.monomial((0, tuple(sorted((atom, other)))))
                        remainder = self.ring.p.multiply((0, (other,)), integrand)
                        out = product - self.primitive(self.ring.monomial(remainder))
                        self.stats["first_level_shuffle_rewrites"] += 1
            if out is None:
                out = raw
            self.primitive_cache[m] = out
            return out
        finally:
            self.active.remove(m)


def matrix_operator(ring, parameters):
    """The actual eight-coordinate, trace-zero bridge-difference operator."""
    p0, p1, p2, r0, r1, s0, s1, t1 = map(F, parameters)
    x = ring.x()
    t0 = p0/4 + s1/2
    A0 = -p1/2 - p2*x
    A1 = p0 + p1*x + p2*x*x
    A2 = r1 + (s1-p0/2)*x + (t1-p1/2)*x*x - p2*x*x*x/2
    B0 = r0 + r1*x - p0*x*x/4
    B1 = s0 + s1*x - p1*x*x/4
    B2 = t0 + t1*x - p2*x*x/4

    def apply(f, g):
        fp, gp = f.D(), g.D()
        fpp, gpp = fp.D(), gp.D()
        J0 = (fpp*gpp).J()
        J1 = (x*fpp*gpp).J()
        J2 = (x*x*fpp*gpp + 2*fp*gp).J()
        return (A0*f*g + A1*(f*gp+fp*g)/2 + A2*fp*gp
                + B0*J0 + B1*J1 + B2*J2)
    return apply


def operator_basis(ring):
    return [matrix_operator(ring, [int(i == j) for i in range(8)]) for j in range(8)]


def positive_constant_operator(ring):
    # h=1, k=+1, omega=+1, so x=e and d=h*omega-k=0.
    return matrix_operator(ring, [F(-1, 2), 0, F(-1, 2), F(-1, 8), 0, 0, 0, 0])


class ConstantCompiler(formal.Compiler):
    def __init__(self, algebra, sign):
        if sign not in (-1, 1):
            raise ValueError("this target uses the reciprocal k=+/-1 pair")
        self.a = algebra
        c = algebra.c
        self.h = c.constant(1)
        self.k = c.constant(sign)
        self.omega = c.constant(sign)
        self.gamma = c.zero
        self.nu = c.zero
        self.ih = c.one
        self.ih2 = c.one
        self.zero = algebra.number(0)
        x = algebra.profile((1, ()))
        self.z = x.add(algebra.number(sign))
        self.e = x
        self.K0 = self.z.multiply(self.z).scale(sign).add(self.z.scale(-2))
        self.lam = self.zero
        self.records = []
        self.physical_fourth = {}


def evaluate_coefficients_at_zero_histories(algebra):
    """Differentiate first, specialize second; state RHS terms remain genuine."""
    values = []
    for node in algebra.c.nodes:
        tag = node[0]
        if tag == "c":
            value = F(node[1], node[2])
        elif tag == "st":
            value = F(0)
        elif tag == "add":
            value = sum((F(n, d)*values[child] for child, n, d in node[1]), F(0))
        elif tag == "mul":
            value = F(node[1], node[2])
            for child, power in node[3]:
                if not values[child] and power < 0:
                    raise AssertionError("a history was inverted")
                value *= values[child]**power
        else:
            raise AssertionError(("unfrozen coefficient in constant producer", node))
        values.append(value)
    return values


def extract_expr(ring, separated, values):
    return Expr(ring, {m: values[c] for m, c in separated.terms.items() if values[c]})


def compile_reciprocal_target(ring):
    roots = []
    records = []
    for sign in (1, -1):
        compiler = ConstantCompiler(ring.algebra, sign)
        first = compiler.initial("q")
        second, _ = compiler.forcing_range([(1, first, first)], 2,
                                           "constant_%s_B" % sign, True)
        third, _ = compiler.forcing_range([(1, first, second)], 3,
                                          "constant_%s_U" % sign, True)
        _, data = compiler.forcing_range([(F(-1, 16), second, second),
                                          (F(-1, 4), first, third)], 4,
                                         "constant_%s_pure_fourth" % sign, False)
        roots.append(data["period_rhs"])
        records.append({"sign": sign, "records": compiler.records})
    values = evaluate_coefficients_at_zero_histories(ring.algebra)
    target = sum((extract_expr(ring, root, values) for root in roots), ring.number(0))
    if ring.homogeneous_weight(target) != 4:
        raise AssertionError("reciprocal pure target must be quartic")
    return target, records


def assert_zero(ring, expr, label, normalizer=None):
    result = (normalizer or RightIBP(ring)).expression(expr)
    if result.terms:
        raise AssertionError("%s: %s unreduced terms, digest=%s" %
                             (label, len(result.terms), ring.digest(result)))
    return True


def small_exact_toys():
    limits = Limits(seconds=90, nodes=50000, atoms=10000, terms=15000,
                    rewrites=20000, memory_mib=1024)
    ring = Ring(limits)
    n = RightIBP(ring)
    q, x = ring.jet(), ring.x()
    g, h, j = q.D(), q.D().D(), q.D().D().D()
    Q, L = 1+x*x, x*x-1
    checks = {}
    checks["signed_I_derivative"] = (q*q.I()).I().D().terms == (q*q.I()).terms
    checks["I_q_qprime"] = assert_zero(ring, (q*g).I()-q*q/2, "first exact right IBP", n)
    checks["I_qprime_qthird"] = assert_zero(ring, (g*j).I()-g*h+(h*h).I(),
                                           "jet integration by parts", n)
    J0_signed = (h*h).I()
    checks["right_shuffle_square"] = assert_zero(ring, (J0_signed*h*h).I()-J0_signed*J0_signed/2,
                                                 "right shuffle", n)
    basis = operator_basis(ring)
    P, R = basis[3], basis[4]
    tau = P(q, R(q, q))-R(q, P(q, q))
    tau0 = (h*h*h).I()/3
    checks["actual_matrix_commutator_tau0"] = assert_zero(ring, tau-tau0, "P,Q commutator sign", n)
    A = positive_constant_operator(ring)
    J = (Q*h*h+2*g*g).J()
    a_expected = x*q*q/2-Q*q*g/2+Q*x*g*g/4+L*J/8
    checks["constant_plus_operator"] = assert_zero(ring, A(q, q)-a_expected, "constant k+ operator", n)
    direct = (ring.variation(tau0, A(q, q))-2*A(q, tau0))/8
    I3 = (h*h*h).J()
    m = q-x*g
    density_F = (-q*g*h*h+x*g*g*h*h/2+2*x*m*h*h*h/3
                 +x*(2*x*x-1)*h*h*h*h/12-J*h*h/4)
    density_G = -x*h*h*h*h/2+2*g*h*h*h/3
    independent = ((x*q-Q*g/2)*I3/3+density_F.J()-L*density_G.J()/4)/8
    checks["tau0_response_independent_right_IBP"] = assert_zero(
        ring, direct-independent, "independently derived tau0 response", n)
    # The raw free algebra may have nontrivial dependencies. This is a
    # positive identity toy, not a test of completeness of our normalizer.
    checks["no_profile_or_geometry_evaluation"] = True
    if not all(checks.values()):
        raise AssertionError("a small exact interface toy failed")
    return {"checks": checks, "right_IBP_statistics": n.stats,
            "profile_atoms": len(ring.p.atoms),
            "independent_tau0_response_digest": ring.digest(n.expression(independent))}


def sparse_span(columns, target, limits):
    """Exact rational span of the displayed rewritten representatives only."""
    basis = {}
    column_count = len(columns)
    independent_columns = []
    for index, column in enumerate(columns):
        vec = dict(column.terms)
        representation = {index: F(1)}
        while vec:
            limits.check()
            pivot = min(vec)
            if pivot not in basis:
                scale = vec[pivot]
                vec = {m: limits.rational(v/scale) for m, v in vec.items()}
                representation = {j: limits.rational(v/scale) for j, v in representation.items()}
                basis[pivot] = (vec, representation)
                independent_columns.append(index)
                break
            other, rep = basis[pivot]
            scale = vec[pivot]
            for m, value in other.items():
                vec[m] = limits.rational(vec.get(m, F(0))-scale*value)
                if not vec[m]:
                    del vec[m]
            for j, value in rep.items():
                representation[j] = limits.rational(representation.get(j, F(0))-scale*value)
                if not representation[j]:
                    del representation[j]
    vec = dict(target.terms)
    coefficients = {j: F(0) for j in range(column_count)}
    while vec:
        limits.check()
        pivot = min(vec)
        if pivot not in basis:
            break
        other, rep = basis[pivot]
        scale = vec[pivot]
        for m, value in other.items():
            vec[m] = limits.rational(vec.get(m, F(0))-scale*value)
            if not vec[m]:
                del vec[m]
        for j, value in rep.items():
            coefficients[j] = limits.rational(coefficients[j]+scale*value)
    return coefficients, Expr(target.ring, vec), independent_columns


def compiler_dependency():
    path = Path(formal.__file__)
    data = path.read_bytes()
    blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    if blob != EXPECTED_COMPILER_GIT_BLOB:
        raise RuntimeError("the R56 producer changed; review and bind the new dependency explicitly")
    return {"filename": path.name, "git_blob_sha1": blob,
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--max-seconds", type=int, default=240)
    parser.add_argument("--max-coefficient-nodes", type=int, default=500000)
    parser.add_argument("--max-profile-atoms", type=int, default=60000)
    parser.add_argument("--max-terms", type=int, default=80000)
    parser.add_argument("--max-IBP-calls", type=int, default=250000)
    parser.add_argument("--max-memory-mib", type=int, default=2048)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    args = parser.parse_args()
    if not args.toy_only and not (
            os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("research compilation only in the named public repository GitHub Actions")
    numeric_limits = [args.max_seconds, args.max_coefficient_nodes, args.max_profile_atoms,
                      args.max_terms, args.max_IBP_calls, args.max_memory_mib, args.max_rational_bits]
    if any(value <= 0 for value in numeric_limits):
        parser.error("every resource bound must be positive")
    sys.setrecursionlimit(12000)
    started = time.monotonic()
    payload = {
        "schema": "visible-flex-reciprocal-pure-whole-function-membership-v1",
        "kind": "small_exact_toys" if args.toy_only else "bounded_exact_whole_function_span_test",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "compiler_dependency": None,
        "github": {key: os.environ.get(key) for key in
                   ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
        "completion": "not_started",
        "phase": "small_exact_toys",
        "signed_primitive": "I(F)(xi)=integral_r^xi F; positive tails J=-I; no left-tail reset",
        "profile_domain": "one arbitrary complex C-infinity profile, zero on a common right collar; I compactly inside (1,infinity)",
        "ordinary_complex_products": True,
        "target": "R65 pure local reciprocal pair P[q]/16, generated by R56 with h=1,k=+/-1,omega=+/-1",
        "target_derivative_ordering": "compile all physical derivatives with actual history RHS; only then set incoming second/third history values to zero",
        "positive_verification": "fresh residual from the unnormalized true R56 target and the original unnormalized matrix brackets; every IBP boundary is the common zero right collar",
        "zero_left_tail_assumed": False,
        "columns": "H_A([Phi_i,Phi_j])=(D[Phi_i,Phi_j](q)[A(q,q)]-2A(q,[Phi_i,Phi_j](q)))/8",
        "loop_realization": "R71 T_loop=2*t*[Phi_i,Phi_j] for a fixed small parameter interval. For any finite coefficient c, choose a fixed finite m and concatenate m copies with t=c/(2*m) inside that interval; M=0 makes T add exactly. One m may be fixed on a compact coefficient neighborhood.",
        "common_positive_pair_duration_divided_out": True,
        "baseline_true_bridge_T_included": False,
        "rational_span_scope": "the 28 actual commutator directions, modulo only the explicitly justified incomplete right-IBP rewrites",
        "negative_result_scope": "failure to produce a verified identity here does not prove functional nonmembership, nor rule out a fixed profile or other actual third holonomy",
        "full_fourth_range_satisfied": False,
        "P0_satisfied": False,
        "finite_isometric_family_certified": False,
        "embedded_closed_surface_certified": False,
        "profile_or_geometry_integrals_evaluated": False,
        "resource_limits": {
            "seconds": args.max_seconds, "coefficient_nodes": args.max_coefficient_nodes,
            "profile_atoms": args.max_profile_atoms, "terms": args.max_terms,
            "IBP_calls": args.max_IBP_calls, "memory_mib": args.max_memory_mib,
            "rational_bits": args.max_rational_bits,
            "rational_bit_scope": "exact rational span elimination",
            "memory_scope": "polled RSS threshold, including inherited compiler time-check sites; not an OS hard cap",
        },
    }
    exit_code = 0
    ring = None
    normalizer = None
    try:
        payload["compiler_dependency"] = compiler_dependency()
        payload["small_exact_toys"] = small_exact_toys()
        if args.toy_only:
            payload["completion"] = "toy_only"
        else:
            limits = Limits(args.max_seconds, args.max_coefficient_nodes, args.max_profile_atoms,
                            args.max_terms, args.max_IBP_calls, args.max_memory_mib, args.max_rational_bits)
            ring = Ring(limits)
            normalizer = RightIBP(ring)
            payload["phase"] = "compile_true_reciprocal_drift"
            target_raw, records = compile_reciprocal_target(ring)
            payload["constant_compiler_records"] = records
            target = normalizer.expression(target_raw)
            payload["target_summary"] = {
                "raw_terms": len(target_raw.terms), "rewritten_terms": len(target.terms),
                "raw_sha256": ring.digest(target_raw), "rewritten_sha256": ring.digest(target),
            }
            payload["phase"] = "compile_28_actual_commutator_responses"
            q = ring.jet()
            A = positive_constant_operator(ring)
            a = A(q, q)
            ops = operator_basis(ring)
            pairs = list(itertools.combinations(range(8), 2))
            raw_columns, raw_cubic_brackets, columns, summaries = [], [], [], []
            for i, j in pairs:
                tau_raw = ops[i](q, ops[j](q, q))-ops[j](q, ops[i](q, q))
                tau = normalizer.expression(tau_raw)
                response_raw = (ring.variation(tau, a)-2*A(q, tau))/8
                response = normalizer.expression(response_raw)
                if ring.homogeneous_weight(tau) not in (3, None) or ring.homogeneous_weight(response) not in (4, None):
                    raise AssertionError("commutator homogeneity")
                raw_columns.append(response_raw)
                raw_cubic_brackets.append(tau_raw)
                columns.append(response)
                summaries.append({
                    "pair": [PARAMETERS[i], PARAMETERS[j]],
                    "tau_terms": len(tau.terms), "response_terms": len(response.terms),
                    "tau_sha256": ring.digest(tau), "response_sha256": ring.digest(response),
                })
            payload["column_summaries"] = summaries
            payload["phase"] = "exact_rational_span"
            coefficients, remainder, independent = sparse_span(columns, -target, limits)
            payload["rewritten_representative_rank"] = len(independent)
            payload["independent_column_indices"] = independent
            payload["span_remainder"] = {"terms": len(remainder.terms), "sha256": ring.digest(remainder)}
            found = not remainder.terms
            payload["relation_in_rewritten_representatives_found"] = found
            payload["verified_whole_function_identity"] = False
            if found:
                payload["phase"] = "fresh_original_expression_verification"
                residual = target_raw
                relation = []
                for index, coefficient in coefficients.items():
                    if coefficient:
                        original_tau = raw_cubic_brackets[index]
                        original_response = (ring.variation(original_tau, a)-2*A(q, original_tau))/8
                        residual += coefficient*original_response
                        i, j = pairs[index]
                        relation.append({
                            "pair": [PARAMETERS[i], PARAMETERS[j]],
                            "response_coefficient": [coefficient.numerator, coefficient.denominator],
                            "nominal_total_loop_parameter": [(coefficient/2).numerator, (coefficient/2).denominator],
                            "finite_small_parameter_subdivision_required": True,
                        })
                fresh = RightIBP(ring)
                verification = fresh.expression(residual)
                payload["candidate_relation"] = relation
                payload["fresh_residual"] = {"terms": len(verification.terms),
                                             "sha256": ring.digest(verification),
                                             "IBP_statistics": fresh.stats}
                payload["verified_whole_function_identity"] = not verification.terms
            payload["completion"] = "complete"
            payload["phase"] = "finished"
    except formal.CompilationBudgetExceeded as error:
        payload["completion"] = "resource_budget_exceeded"
        payload["budget_failure"] = str(error)
        exit_code = 2
    except Exception as error:
        payload["completion"] = "implementation_check_failed"
        payload["error_type"] = type(error).__name__
        payload["error"] = str(error)
        exit_code = 1
    if ring is not None:
        payload["actual_sizes"] = {
            "coefficient_DAG_nodes": len(ring.algebra.c.nodes),
            "profile_atoms": len(ring.p.atoms),
            "history_states": len(ring.algebra.c.state_rhs),
        }
    if normalizer is not None:
        payload["right_IBP_statistics"] = normalizer.stats
    payload["elapsed_seconds"] = time.monotonic()-started
    payload["peak_resident_mib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    output = json.dumps(payload, indent=2, sort_keys=True)+"\n"
    if len(output.encode()) >= 95000:
        raise RuntimeError("bounded summary must remain below 95 KB")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(output, encoding="utf-8")
    print(json.dumps({"output": str(args.out), "bytes": len(output.encode()),
                      "sha256": hashlib.sha256(output.encode()).hexdigest(),
                      "completion": payload["completion"],
                      "verified_whole_function_identity": payload.get("verified_whole_function_identity", False)}))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
