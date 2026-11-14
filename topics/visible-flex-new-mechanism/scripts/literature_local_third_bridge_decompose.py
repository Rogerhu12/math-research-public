#!/usr/bin/env python3
"""Exact decomposition of the genuine local third bridge density from R73.

The research target, any concrete profile witness, and the optional enlarged
pure-mode span are run only in this public repository's GitHub Actions.
--toy-only uses a small hand-built geometry/profile polynomial.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import sys
import time

import literature_range_profile_algebra as formal
import literature_pure_bulk_exact_membership as exact

EXPECTED_MEMBERSHIP_BLOB = "f1b4f5fc69dd14c72fbbd02fd7e5347b0345657a"
H, K, O, V, W, HV, KW, LH = range(8)
NAMES = ("h", "k", "omega", "h_s", "k_s", "h_ss", "k_ss", "log_h")
GZERO = (0,)*8


def gshift(key, index, power=1):
    out = list(key)
    out[index] += power
    return tuple(out)


def gmul(a, b):
    return tuple(x+y for x, y in zip(a, b))


def clean_scalar(poly):
    return {m: F(v) for m, v in poly.items() if v}


def sadd(a, b):
    out = dict(a)
    for m, v in b.items():
        out[m] = out.get(m, F(0))+v
        if not out[m]:
            del out[m]
    return out


def smul(a, b, limits):
    out = {}
    for m, c in a.items():
        limits.check()
        for n, d in b.items():
            key = gmul(m, n)
            out[key] = out.get(key, F(0))+c*d
        if len(out) > limits.formal.max_terms:
            raise formal.CompilationBudgetExceeded("geometry Laurent term budget")
    return clean_scalar(out)


def spow(poly, exponent, limits):
    if exponent < 0:
        if len(poly) != 1:
            raise AssertionError("only Laurent monomials may be inverted")
        key, value = next(iter(poly.items()))
        if not value:
            raise ZeroDivisionError("zero Laurent monomial")
        return {tuple(exponent*x for x in key): value**exponent}
    out = {GZERO: F(1)}
    base = poly
    while exponent:
        if exponent & 1:
            out = smul(out, base, limits)
        exponent >>= 1
        if exponent:
            base = smul(base, base, limits)
    return out


class GeometryExpansion:
    """Exact coefficient DAG expansion, after all real s derivatives exist."""

    def __init__(self, algebra, limits):
        self.a = algebra
        self.limits = limits
        self.cache = {}

    def node(self, index):
        if index in self.cache:
            return self.cache[index]
        self.limits.check()
        node = self.a.c.nodes[index]
        tag = node[0]
        if tag == "c":
            out = {GZERO: F(node[1], node[2])} if node[1] else {}
        elif tag == "st":
            # Values vanish, not their already-compiled actual derivatives.
            out = {}
        elif tag == "g":
            lookup = {("h", 0): H, ("k", 0): K, ("omega", 0): O,
                      ("h", 1): V, ("k", 1): W,
                      ("h", 2): HV, ("k", 2): KW}
            if (node[1], node[2]) not in lookup:
                raise AssertionError(("unexpected geometry jet", node))
            out = {gshift(GZERO, lookup[(node[1], node[2])]): F(1)}
        elif tag == "add":
            out = {}
            for child, n, d in node[1]:
                term = {key: F(n, d)*value for key, value in self.node(child).items()}
                out = sadd(out, term)
        elif tag == "mul":
            out = {GZERO: F(node[1], node[2])}
            for child, exponent in node[3]:
                out = smul(out, spow(self.node(child), exponent, self.limits), self.limits)
        else:
            raise AssertionError(tag)
        self.cache[index] = out
        return out

    def separated(self, expr, ring):
        out = {}
        for profile, coefficient in expr.terms.items():
            for geometry, value in self.node(coefficient).items():
                out[geometry] = out.get(geometry, ring.number(0))+value*ring.monomial(profile)
        return GExpr(ring, out)


class GExpr:
    """Geometry Laurent/log polynomial with exact profile-expression values."""

    def __init__(self, ring, terms=None):
        self.ring = ring
        self.terms = {m: v for m, v in (terms or {}).items() if v.terms}
        if len(self.terms) > ring.limits.formal.max_terms:
            raise formal.CompilationBudgetExceeded("separated geometry term budget")

    def __add__(self, other):
        if other.ring is not self.ring:
            raise ValueError("geometry expressions use one shared profile algebra")
        out = dict(self.terms)
        for m, v in other.terms.items():
            out[m] = out.get(m, self.ring.number(0))+v
        return GExpr(self.ring, out)

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self+(-other)

    def scale(self, value):
        return GExpr(self.ring, {m: value*v for m, v in self.terms.items()})

    def shift(self, index, power=1):
        return GExpr(self.ring, {gshift(m, index, power): v for m, v in self.terms.items()})

    def normalized(self, normalizer):
        return GExpr(self.ring, {m: normalizer.expression(v) for m, v in self.terms.items()})

    def partial(self, index):
        out = {}
        for key, value in self.terms.items():
            power = key[index]
            if power:
                target = gshift(key, index, -1)
                out[target] = out.get(target, self.ring.number(0))+power*value
            if index == H and key[LH]:
                # d(log h)/dh=1/h, with h>0.
                target = gshift(gshift(key, LH, -1), H, -1)
                out[target] = out.get(target, self.ring.number(0))+key[LH]*value
        return GExpr(self.ring, out)

    def Ds(self):
        if any(m[HV] or m[KW] for m in self.terms):
            raise AssertionError("a proposed potential depends on acceleration")
        return (self.partial(H).shift(V)+self.partial(K).shift(W)
                +self.partial(O).shift(W).shift(H, -1).scale(F(1, 2))
                +self.partial(V).shift(HV)+self.partial(W).shift(KW))

    def integrate_h_from_one(self):
        out = {}
        for key, value in self.terms.items():
            if key[LH] or any(key[i] for i in (V, W, HV, KW)):
                raise AssertionError("h primitive requires a static Laurent coefficient")
            power = key[H]
            if power == -1:
                target = gshift(gshift(key, H, 1), LH, 1)
                out[target] = out.get(target, self.ring.number(0))+value
            else:
                target = gshift(key, H, 1)
                base = list(key)
                base[H] = 0
                base = tuple(base)
                out[target] = out.get(target, self.ring.number(0))+value/(power+1)
                out[base] = out.get(base, self.ring.number(0))-value/(power+1)
        return GExpr(self.ring, out)

    def static_polynomial_primitive(self, index):
        out = {}
        for key, value in self.terms.items():
            if any(key[i] for i in (V, W, HV, KW, LH)) or key[index] < 0:
                raise AssertionError("polynomial primitive hypotheses")
            target = gshift(key, index, 1)
            out[target] = out.get(target, self.ring.number(0))+value/(key[index]+1)
        return GExpr(self.ring, out)

    def coefficient_for_jets(self, v=0, w=0, hv=0, kw=0):
        out = {}
        for key, value in self.terms.items():
            if tuple(key[i] for i in (V, W, HV, KW)) == (v, w, hv, kw):
                base = list(key)
                for i in (V, W, HV, KW):
                    base[i] = 0
                out[tuple(base)] = value
        return GExpr(self.ring, out)

    def evaluate_static_profile(self, h, k, omega):
        h, k, omega = F(h), F(k), F(omega)
        if h <= 0:
            raise ValueError("h must be positive")
        out = self.ring.number(0)
        for key, value in self.terms.items():
            if any(key[i] for i in (V, W, HV, KW)):
                raise AssertionError("static substitution contains velocity")
            if key[LH]:
                if h == 1:
                    continue
                raise ValueError("nonrational log(h) is not silently approximated")
            out += (h**key[H]*k**key[K]*omega**key[O])*value
        return out

    def summary(self):
        rows = [[list(key), self.ring.digest(value)] for key, value in sorted(self.terms.items())]
        return {"geometry_terms": len(self.terms),
                "total_profile_terms": sum(len(value.terms) for value in self.terms.values()),
                "sha256": hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()}


class SharedCompiler(formal.Compiler):
    def __init__(self, algebra):
        self.a = algebra
        c = algebra.c
        self.h = c.geometry("h")
        self.k = c.geometry("k")
        self.omega = c.geometry("omega")
        self.gamma = c.geometry("h", 1)
        self.nu = c.derivative(self.omega)
        self.ih = c.power(self.h, -1)
        self.ih2 = c.power(self.h, -2)
        self.zero = algebra.number(0)
        self.z = algebra.profile((1, ())).add(algebra.scalar(self.omega))
        self.e = self.z.coefficient(self.h).add(algebra.scalar(self.k).scale(-1))
        self.K0 = self.z.multiply(self.z).coefficient(self.k).add(
            self.z.coefficient(c.multiply(c.add(c.power(self.k, 2), c.one), self.ih)).scale(-1))
        self.lam = self.z.coefficient(self.gamma).add(
            algebra.scalar(c.multiply(self.h, self.nu)).scale(-1)).coefficient(self.ih2)
        self.records = []
        self.physical_fourth = {}


def compile_local_third(ring):
    compiler = SharedCompiler(ring.algebra)
    first = compiler.initial("q")
    second, _ = compiler.forcing_range([(1, first, first)], 2, "local_third_B", True)
    _, third = compiler.forcing_range([(1, first, second)], 3, "local_third_C", False)
    expansion = GeometryExpansion(ring.algebra, ring.limits)
    local = expansion.separated(third["period_rhs"], ring)
    return local, compiler.records, len(expansion.cache)


def decompose(local, normalizer):
    """C = Ds(P_acc+P_h) + Area*(k_s h_ss-h_s k_ss) + Cubic + k_s*R."""
    ring = local.ring
    local = local.normalized(normalizer)
    for key in local.terms:
        if key[LH]:
            raise AssertionError("raw local density unexpectedly contains log")
        jet_weight = key[V]+key[W]+2*key[HV]+2*key[KW]
        if jet_weight not in (1, 3):
            raise AssertionError(("local third reversal/weight structure", key))
        if key[HV]+key[KW] > 1:
            raise AssertionError("local third density is nonlinear in acceleration")
    hh = local.coefficient_for_jets(v=1, hv=1)
    kh = local.coefficient_for_jets(w=1, hv=1)
    hk = local.coefficient_for_jets(v=1, kw=1)
    kk = local.coefficient_for_jets(w=1, kw=1)
    potential_acc = (hh.shift(V, 2).scale(F(1, 2))
                     +kk.shift(W, 2).scale(F(1, 2))
                     +(kh+hk).shift(V).shift(W).scale(F(1, 2)))
    area = (kh-hk).scale(F(1, 2)).normalized(normalizer)
    area_form = area.shift(W).shift(HV)-area.shift(V).shift(KW)
    reduced = (local-potential_acc.Ds()-area_form).normalized(normalizer)
    if any(key[HV] or key[KW] for key in reduced.terms):
        raise AssertionError("symmetric acceleration subtraction failed")
    linear_h = reduced.coefficient_for_jets(v=1)
    linear_k = reduced.coefficient_for_jets(w=1)
    cubic = GExpr(ring, {key: value for key, value in reduced.terms.items()
                        if key[V]+key[W] == 3})
    expected = linear_h.shift(V)+linear_k.shift(W)+cubic
    if (reduced-expected).normalized(normalizer).terms:
        raise AssertionError("velocity decomposition")
    potential_h = linear_h.integrate_h_from_one()
    residual_k = (linear_k-potential_h.partial(K)
                  -potential_h.partial(O).shift(H, -1).scale(F(1, 2))).normalized(normalizer)
    remainder = (area_form+cubic+residual_k.shift(W)).normalized(normalizer)
    potential = potential_acc+potential_h
    reconstruction = (local-potential.Ds()-remainder).normalized(normalizer)
    if reconstruction.terms:
        raise AssertionError("whole local density reconstruction")

    # Necessary and sufficient static-potential tests, when area/cubic vanish.
    # R = a(k,omega)+b(k,omega)/h is forced by an h-independent integration
    # constant C(k,omega); C_k=a and C_omega=2b.
    h_shape_obstruction = residual_k.partial(H).shift(H, 2).partial(H).normalized(normalizer)
    a_form = (residual_k+residual_k.partial(H).shift(H)).normalized(normalizer)
    b_form = residual_k.partial(H).shift(H, 2).scale(-1).normalized(normalizer)
    contact_closure = (a_form.partial(O)-b_form.partial(K).scale(2)).normalized(normalizer)
    endpoint_potential = None
    if not area.terms and not cubic.terms and not h_shape_obstruction.terms and not contact_closure.terms:
        if any(key[H] or key[LH] for key in a_form.terms) or any(key[H] or key[LH] for key in b_form.terms):
            # Incomplete profile normalization can miss this syntactic form.
            endpoint_potential = None
        else:
            correction_a = a_form.static_polynomial_primitive(K)
            correction_b_rhs = (b_form.scale(2)-correction_a.partial(O)).normalized(normalizer)
            if any(key[K] for key in correction_b_rhs.terms):
                raise AssertionError("static-potential compatibility reconstruction")
            correction_b = correction_b_rhs.static_polynomial_primitive(O)
            candidate = potential+correction_a+correction_b
            if (local-candidate.Ds()).normalized(normalizer).terms:
                raise AssertionError("endpoint-potential original-expression verification")
            endpoint_potential = candidate
    return {
        "local": local, "potential_acc": potential_acc, "potential_h": potential_h,
        "potential": potential, "area": area, "cubic": cubic,
        "residual_k": residual_k, "remainder": remainder,
        "h_shape_obstruction": h_shape_obstruction, "contact_closure": contact_closure,
        "endpoint_potential": endpoint_potential,
    }


# Small exact univariate polynomial evaluator, used only for declared toys or
# public-Action witnesses. It never inserts sample values into a span solve.
def pclean(poly):
    return {p: F(c) for p, c in poly.items() if c}


def padd(a, b):
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, F(0))+c
    return pclean(out)


def pscale(poly, value):
    return pclean({p: c*value for p, c in poly.items()})


def pmul(a, b):
    out = {}
    for p, c in a.items():
        for q, d in b.items():
            out[p+q] = out.get(p+q, F(0))+c*d
    if out and max(out) > 256:
        raise formal.CompilationBudgetExceeded("exact witness polynomial degree budget")
    return pclean(out)


def ppow(poly, exponent):
    if exponent < 0:
        raise ValueError("profile xi powers must be nonnegative")
    out = {0: F(1)}
    while exponent:
        if exponent & 1:
            out = pmul(out, poly)
        exponent >>= 1
        if exponent:
            poly = pmul(poly, poly)
    return out


def pd(poly):
    return pclean({p-1: p*c for p, c in poly.items() if p})


def peval(poly, x):
    return sum((value*x**power for power, value in poly.items()), F(0))


class PolynomialProfile:
    def __init__(self, ring, power=8):
        self.ring = ring
        self.power = power
        self.profile = pmul(ppow({1:F(1),0:F(-1)}, power),
                            ppow({0:F(2),1:F(-1)}, power))
        self.atom_cache = {}
        self.monomial_cache = {}

    def atom(self, atom):
        if atom in self.atom_cache:
            return self.atom_cache[atom]
        node = self.ring.p.atoms[atom]
        if node[0] == "jet":
            if node[1] != "q" or node[2] > self.power-2:
                raise AssertionError("piecewise polynomial lacks the requested smooth jets")
            out = self.profile
            for _ in range(node[2]):
                out = pd(out)
        else:
            if self.ring.p.weight(node[1]) == 0:
                raise AssertionError("witness primitive must vanish on the right exterior")
            integrand = self.monomial(node[1])
            out = {p+1: c/F(p+1) for p, c in integrand.items()}
            out = padd(out, {0: -peval(out, F(2))})
        self.atom_cache[atom] = out
        return out

    def monomial(self, m):
        if m in self.monomial_cache:
            return self.monomial_cache[m]
        if m[0] < 0:
            raise AssertionError("unexpected rational xi profile factor")
        out = {m[0]: F(1)}
        for atom in m[1]:
            out = pmul(out, self.atom(atom))
        self.monomial_cache[m] = out
        return out

    def expression(self, expr):
        out = {}
        for m, c in expr.terms.items():
            out = padd(out, pscale(self.monomial(m), c))
        return out


def static_nonzero_witness(geo, evaluator):
    """An exact counterexample to a claimed zero operator, never a fit."""
    if not geo.terms:
        return {"status": "zero_by_exact_rewrite"}
    for h, k, omega in itertools.product((1, 2), (0, 1), (1, 2)):
        try:
            expr = geo.evaluate_static_profile(h, k, omega)
        except ValueError:  # nonrational log(h): do not approximate
            continue
        poly = evaluator.expression(expr)
        for x in (F(5, 4), F(3, 2), F(7, 4)):
            value = peval(poly, x)
            if value:
                return {
                    "status": "exact_nonzero_piecewise_polynomial_witness",
                    "h": h, "k": k, "omega": omega,
                    "xi": [x.numerator, x.denominator],
                    "value": [str(value.numerator), str(value.denominator)],
                    "physical_z_positive": x+omega > 0,
                    "profile": "(xi-1)^8*(2-xi)^8 on [1,2], zero outside; common right endpoint r=3",
                    "regularity": "C7 compact profile; density in the required finite Cj topology gives a smooth compact nonzero witness as well",
                    "no_span_fitting_from_values": True,
                }
    return {"status": "no_witness_in_this_fixed_finite_list",
            "not_a_zero_operator_certificate": True}


def small_toys():
    limits = exact.Limits(seconds=45, nodes=20000, atoms=2000, terms=5000, rewrites=5000)
    ring = exact.Ring(limits)
    n = exact.RightIBP(ring)
    q3 = ring.jet()**3
    unit = GExpr(ring, {GZERO: q3})
    original_potential = unit.shift(V, 2)+unit.shift(V).shift(W).scale(3)+unit.shift(W, 2).scale(2)
    original_potential += unit.shift(H, 2).shift(K)
    true_area = unit.scale(5)
    true_cubic = unit.shift(V, 3).scale(7)
    manual = original_potential.Ds()+true_area.shift(W).shift(HV)-true_area.shift(V).shift(KW)+true_cubic
    out = decompose(manual, n)
    if (out["area"]-true_area).normalized(n).terms:
        raise AssertionError("manual acceleration area")
    if (out["cubic"]-true_cubic).normalized(n).terms:
        raise AssertionError("manual cubic velocity")
    pure = decompose(original_potential.Ds(), n)
    if pure["endpoint_potential"] is None:
        raise AssertionError("manual endpoint potential not reconstructed")
    if (original_potential.Ds()-pure["endpoint_potential"].Ds()).normalized(n).terms:
        raise AssertionError("manual endpoint potential identity")
    evaluator = PolynomialProfile(ring, power=8)
    sample = ring.jet().D()*ring.jet()
    actual = evaluator.expression(sample.I())
    expected = pscale(pmul(evaluator.profile, evaluator.profile), F(1, 2))
    if actual != expected:
        raise AssertionError("small exact piecewise-polynomial right anchor")
    return {"manual_symmetric_acceleration_potential": True,
            "manual_velocity_area": True, "manual_cubic_velocity": True,
            "manual_base_potential_reconstructed": True,
            "exact_piecewise_right_primitive": True,
            "no_research_compiler_called": True}


def dependency_info():
    data = Path(exact.__file__).read_bytes()
    blob = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    if blob != EXPECTED_MEMBERSHIP_BLOB:
        raise RuntimeError("review and explicitly rebind the exact-profile helper")
    return {"membership": {"git_blob": blob, "sha256": hashlib.sha256(data).hexdigest(),
                           "bytes": len(data)},
            "formal_compiler": exact.compiler_dependency()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--include-pure-upper-span", action="store_true")
    parser.add_argument("--max-seconds", type=int, default=240)
    parser.add_argument("--max-coefficient-nodes", type=int, default=600000)
    parser.add_argument("--max-profile-atoms", type=int, default=80000)
    parser.add_argument("--max-terms", type=int, default=100000)
    parser.add_argument("--max-IBP-calls", type=int, default=300000)
    parser.add_argument("--max-memory-mib", type=int, default=2048)
    args = parser.parse_args()
    if not args.toy_only and not (
            os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("actual local-density compilation/witnesses only in this public repository GitHub Actions")
    if min(args.max_seconds, args.max_coefficient_nodes, args.max_profile_atoms,
           args.max_terms, args.max_IBP_calls, args.max_memory_mib) <= 0:
        parser.error("positive budgets required")
    sys.setrecursionlimit(12000)
    started = time.monotonic()
    payload = {
        "schema": "visible-flex-local-third-bridge-exact-decomposition-v1",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "github": {key:os.environ.get(key) for key in
                   ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
        "completion":"not_started","phase":"small_exact_toys",
        "target":"R73 C_s(q;q,q)=local third RHS after full actual derivatives and then zero history values",
        "ordinary_complex_bilinear_products":True,
        "right_anchor":"I(F)=integral_r^xi F; every left tail retained",
        "geometry_relation":"omega_s=k_s/(2h), h>0",
        "research_profile_witness_scope":"fixed exact polynomial counterexamples only; no profile fitting",
        "local_density_columns_proved_reachable":False,
        "baseline_bridge_constructed":False,
        "full_fourth_range_satisfied":False,
        "P0_satisfied":False,
        "finite_isometric_family_certified":False,
        "resource_limits":{"seconds":args.max_seconds,"coefficient_nodes":args.max_coefficient_nodes,
                           "profile_atoms":args.max_profile_atoms,"terms":args.max_terms,
                           "IBP_calls":args.max_IBP_calls,"RSS_polling_mib":args.max_memory_mib,
                           "rational_span_bits":8192},
    }
    exit_code = 0
    ring = None
    n = None
    try:
        payload["dependencies"] = dependency_info()
        payload["toy_checks"] = small_toys()
        if args.toy_only:
            payload["completion"] = "toy_only"
        else:
            limits = exact.Limits(args.max_seconds,args.max_coefficient_nodes,args.max_profile_atoms,
                                  args.max_terms,args.max_IBP_calls,args.max_memory_mib,8192)
            ring = exact.Ring(limits)
            n = exact.RightIBP(ring)
            pure_target_raw = None
            if args.include_pure_upper_span:
                payload["phase"] = "compile_pure_target_for_new_local_density_span"
                pure_target_raw, _ = exact.compile_reciprocal_target(ring)
            payload["phase"] = "compile_genuine_local_third_density"
            local_raw, records, expanded_nodes = compile_local_third(ring)
            payload["compiler_records"] = records
            payload["expanded_coefficient_nodes"] = expanded_nodes
            payload["raw_local"] = local_raw.summary()
            payload["phase"] = "exact_acceleration_and_velocity_decomposition"
            pieces = decompose(local_raw, n)
            payload["decomposition"] = {key:value.summary() for key,value in pieces.items()
                                        if isinstance(value,GExpr)}
            payload["velocity_area_exactly_zero"] = not pieces["area"].terms
            payload["cubic_velocity_exactly_zero"] = not pieces["cubic"].terms
            payload["endpoint_potential_identity_verified"] = pieces["endpoint_potential"] is not None
            payload["h_primitive_anchor"] = "P_h(h=1,k,omega)=0; constant-germ acceleration potential vanishes"
            payload["phase"] = "exact_fixed_profile_nonzero_witnesses"
            evaluator = PolynomialProfile(ring,8)
            payload["operator_witnesses"] = {
                "velocity_area":static_nonzero_witness(pieces["area"],evaluator),
                "h_shape_obstruction":static_nonzero_witness(pieces["h_shape_obstruction"],evaluator),
                "contact_closure":static_nonzero_witness(pieces["contact_closure"],evaluator),
            }
            payload["operator_witnesses"]["cubic_velocity"] = {}
            for power in range(4):
                operator = pieces["cubic"].coefficient_for_jets(v=power,w=3-power)
                payload["operator_witnesses"]["cubic_velocity"]["h_s^%s*k_s^%s"%(power,3-power)] = static_nonzero_witness(operator,evaluator)
            if pieces["endpoint_potential"] is not None:
                static_potential = GExpr(ring,{key:value for key,value in pieces["endpoint_potential"].terms.items()
                                               if not any(key[i] for i in (V,W,HV,KW))})
                endpoint_jump = n.expression(
                    static_potential.evaluate_static_profile(1,-1,-1)
                    -static_potential.evaluate_static_profile(1,1,1))
                payload["reciprocal_endpoint_jump"] = {"terms":len(endpoint_jump.terms),
                                                       "sha256":ring.digest(endpoint_jump)}
            if args.include_pure_upper_span:
                payload["phase"] = "new_formal_local_density_upper_span"
                candidates = list(sorted(pieces["remainder"].terms.items()))
                local_taus = [value for key,value in candidates]
                _, _, independent = exact.sparse_span(local_taus,ring.number(0),limits)
                q = ring.jet()
                A = exact.positive_constant_operator(ring)
                a = A(q,q)
                ops = exact.operator_basis(ring)
                tau_inputs, labels = [], []
                for i,j in itertools.combinations(range(8),2):
                    tau_inputs.append(ops[i](q,ops[j](q,q))-ops[j](q,ops[i](q,q)))
                    labels.append({"kind":"R71_reachable_commutator","pair":[exact.PARAMETERS[i],exact.PARAMETERS[j]]})
                for index in independent:
                    tau_inputs.append(local_taus[index])
                    labels.append({"kind":"formal_local_density_only","geometry_monomial":list(candidates[index][0]),
                                   "geometry_variable_order":list(NAMES)})
                columns = []
                for tau in tau_inputs:
                    response = (ring.variation(tau,a)-2*A(q,tau))/8
                    columns.append(n.expression(response))
                pure_target = n.expression(pure_target_raw)
                coefficients,remainder,cols_independent = exact.sparse_span(columns,-pure_target,limits)
                report = {"local_density_profile_representative_rank":len(independent),
                          "total_response_representative_rank":len(cols_independent),
                          "response_columns":len(columns),
                          "remainder_terms":len(remainder.terms),"remainder_sha256":ring.digest(remainder),
                          "verified_whole_function_identity_in_formal_upper_span":False,
                          "formal_local_columns_are_not_a_reachability_certificate":True,
                          "negative_is_not_functional_nonmembership":True}
                if not remainder.terms:
                    residual = pure_target_raw
                    relation = []
                    for index,coefficient in coefficients.items():
                        if coefficient:
                            tau = tau_inputs[index]
                            residual += coefficient*(ring.variation(tau,a)-2*A(q,tau))/8
                            relation.append({"column":labels[index],
                                             "coefficient":[coefficient.numerator,coefficient.denominator]})
                    fresh = exact.RightIBP(ring)
                    verified = fresh.expression(residual)
                    report["relation"] = relation
                    report["fresh_original_residual_terms"] = len(verified.terms)
                    report["verified_whole_function_identity_in_formal_upper_span"] = not verified.terms
                payload["pure_upper_span"] = report
            payload["completion"] = "complete"
            payload["phase"] = "finished"
    except formal.CompilationBudgetExceeded as error:
        payload["completion"]="resource_budget_exceeded"
        payload["budget_failure"]=str(error)
        exit_code=2
    except Exception as error:
        payload["completion"]="implementation_check_failed"
        payload["error_type"]=type(error).__name__
        payload["error"]=str(error)
        exit_code=1
    if ring is not None:
        payload["actual_sizes"]={"coefficient_DAG_nodes":len(ring.algebra.c.nodes),
                                "profile_atoms":len(ring.p.atoms),
                                "history_states":len(ring.algebra.c.state_rhs)}
    if n is not None:
        payload["right_IBP_statistics"]=n.stats
    payload["elapsed_seconds"]=time.monotonic()-started
    output=json.dumps(payload,indent=2,sort_keys=True)+"\n"
    if len(output.encode())>=95000:
        raise RuntimeError("summary must remain below 95 KB")
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(output,encoding="utf-8")
    print(json.dumps({"output":str(args.out),"bytes":len(output.encode()),
                      "sha256":hashlib.sha256(output.encode()).hexdigest(),
                      "completion":payload["completion"]}))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()

