#!/usr/bin/env python3
"""Joint whole-function P1 test with a genuine exterior third-operator slot.

The research target and exact five-leg C1 endpoint signature are compiled
only by this public repository's Actions. --toy-only never calls a genuine
target, local density, profile, geometric design, or ODE evaluator.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import comb
import os
from pathlib import Path
import resource
import sys
import time

import literature_colored_profile_algebra as colored
import literature_local_third_bridge_decompose as local
import literature_pure_bulk_exact_membership as exact
import literature_pure_bulk_word_normal_form as words
import literature_range_profile_algebra as formal


SCHEMA = "visible-flex-complete-phase-third-bridge-exact-v2-pre-reduced"
EXPECTED = {
    "exact": "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70",
    "local": "08ada4219df23e50dff2c784c2457dab3c732cd82cacc1477389fdc53fbb6ee0",
    "words": "d39482c9e33e7358f1afa51b073daf5f65e84b4858f9a18f446206e8f9d9ea65",
    "formal": "a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52",
    "colored": "c0d87a214f27a03fb29cd07cc5e9740249580da7f854ed4ff02d6eaf69b1f66f",
}
MODES = (-4, -2)


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def dependencies():
    out = {}
    for name, module in (("exact", exact), ("local", local), ("words", words),
                         ("formal", formal), ("colored", colored)):
        path = Path(module.__file__)
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if name in EXPECTED and digest != EXPECTED[name]:
            raise RuntimeError("explicitly rebind changed dependency: "+name)
        out[name] = {"filename": path.name, "bytes": len(data), "sha256": digest}
    own = Path(__file__).read_bytes()
    out["driver"] = {"filename": Path(__file__).name, "bytes": len(own),
                     "sha256": hashlib.sha256(own).hexdigest()}
    return out


# Exact Q(a), a=2+sqrt(3), represented as u+v*a.  The two embeddings are not
# interchanged: the geometric path always uses the positive larger root.
QZERO, QONE, QA = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))


def qadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def qscale(a, c):
    return F(c)*a[0], F(c)*a[1]


def qmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]+4*a[1]*b[1]


def qpow(a, power):
    if power < 0:
        norm = a[0]*a[0]+4*a[0]*a[1]+a[1]*a[1]
        if not norm:
            raise ZeroDivisionError("quadratic-field zero")
        return qpow(((a[0]+4*a[1])/norm, -a[1]/norm), -power)
    answer = QONE
    while power:
        if power & 1:
            answer = qmul(answer, a)
        power >>= 1
        if power:
            a = qmul(a, a)
    return answer


def integrate_leg(h, omega_intercept, omega_slope, left, right, key):
    """Exact integral h^H*k^K*omega(k)^O*log(h)^L dk on one k leg."""
    H, K, O, V, W, HV, KW, LH = key
    if any((V, W, HV, KW)) or min(K, O, LH) < 0:
        raise ValueError("static Laurent/log coefficient required")
    total = QZERO
    for j in range(O+1):
        exponent = K+j
        scalar = F(right**(exponent+1)-left**(exponent+1), exponent+1)*comb(O, j)
        value = qmul(qpow(omega_intercept, O-j), qpow(omega_slope, j))
        total = qadd(total, qscale(value, scalar))
    return qmul(qpow(h, H), total)


def five_leg_coefficient(key):
    """All terms, not merely three moments, of the fixed scalar path.

    h: 1 -> a at k=1; k:1->0 at h=a; h:a->a^-1 at k=0;
    k:0->-1 at h=a^-1; h:a^-1->1 at k=-1.
    The unique omega integral starts at 1 and ends at -1.
    R dk vanishes on the three h-only legs. P_h vanishes at both h=1 ends.
    """
    inverse = qpow(QA, -1)
    midpoint = qadd(QONE, qscale(inverse, F(-1, 2)))
    plus = integrate_leg(QA, midpoint, qscale(inverse, F(1, 2)), 1, 0, key)
    minus = integrate_leg(inverse, midpoint, qscale(QA, F(1, 2)), 0, -1, key)
    total = qadd(plus, qscale(minus, (-1)**key[local.LH]))
    # log(a^-1)=-log(a), so the power is the same in both legs.
    return {(key[local.LH], basis): value for basis, value in enumerate(total) if value}


def compile_constant_targets(ring):
    roots = {mode: [] for mode in (-4, -2, 0, 2, 4)}
    records = []
    for sign in (1, -1):
        compiler = exact.ConstantCompiler(ring.algebra, sign)
        compiler.compile(max_order=4, progress=False)
        for mode in roots:
            roots[mode].append(compiler.physical_fourth[mode]["period_rhs"])
        records.append({"sign": sign, "records": compiler.records})
    # This specialization is performed before a general-geometry node is
    # introduced. All state RHS derivatives already exist in the roots.
    values = exact.evaluate_coefficients_at_zero_histories(ring.algebra)
    result = {mode: sum((exact.extract_expr(ring, root, values) for root in expressions),
                        ring.number(0)) for mode, expressions in roots.items()}
    for expression in result.values():
        if ring.homogeneous_weight(expression) not in (None, 4):
            raise AssertionError("constant fourth target weight")
    return result, records


def compile_colored_local(ring):
    compiler = local.SharedCompiler(ring.algebra)
    a, b, c = (compiler.initial(name) for name in ("a", "b", "c"))
    second, _ = compiler.forcing_range([(1, b, c)], 2, "colored_B_bc", True)
    _, third = compiler.forcing_range([(1, a, second)], 3, "colored_C_a_bc", False)
    expansion = local.GeometryExpansion(ring.algebra, ring.limits)
    value = expansion.separated(third["period_rhs"], ring)
    allowed = (("a", 1), ("b", 1), ("c", 1))
    for expression in value.terms.values():
        if any(degree != allowed for degree in ring.color_degrees(expression)):
            raise AssertionError("compiled local density lost its exterior/inner slots")
    return value, compiler.records, len(expansion.cache)


def raw_decomposition(density, normalizer):
    """Algebraic geometry decomposition; original profile expressions retained.

    The output coefficients are never replaced by their word representatives.
    This permits an independent final check on the original compiled roots.
    """
    for key in density.terms:
        weight = key[local.V]+key[local.W]+2*key[local.HV]+2*key[local.KW]
        if key[local.LH] or weight not in (1, 3) or key[local.HV]+key[local.KW] > 1:
            raise AssertionError("actual local reversal/weight structure")
    hh = density.coefficient_for_jets(v=1, hv=1)
    kh = density.coefficient_for_jets(w=1, hv=1)
    hk = density.coefficient_for_jets(v=1, kw=1)
    kk = density.coefficient_for_jets(w=1, kw=1)
    pacc = (hh.shift(local.V, 2).scale(F(1, 2))+kk.shift(local.W, 2).scale(F(1, 2))
            +(kh+hk).shift(local.V).shift(local.W).scale(F(1, 2)))
    area = (kh-hk).scale(F(1, 2))
    area_form = area.shift(local.W).shift(local.HV)-area.shift(local.V).shift(local.KW)
    reduced = density-pacc.Ds()-area_form
    lh = reduced.coefficient_for_jets(v=1)
    lk = reduced.coefficient_for_jets(w=1)
    cubic = local.GExpr(density.ring, {key: value for key, value in reduced.terms.items()
                                     if key[local.V]+key[local.W] == 3
                                     and not key[local.HV] and not key[local.KW]})
    ph = lh.integrate_h_from_one()
    rk = lk-ph.partial(local.K)-ph.partial(local.O).shift(local.H, -1).scale(F(1, 2))
    remainder = area_form+cubic+rk.shift(local.W)
    reconstruction = density-(pacc+ph).Ds()-remainder
    if reconstruction.normalized(normalizer).terms:
        raise AssertionError("complete colored local density reconstruction")
    shape = rk.partial(local.H).shift(local.H, 2).partial(local.H)
    aform = rk+rk.partial(local.H).shift(local.H)
    bform = rk.partial(local.H).shift(local.H, 2).scale(-1)
    closure = aform.partial(local.O)-bform.partial(local.K).scale(2)
    return {"area": area, "cubic": cubic, "potential_acc": pacc, "potential_h": ph,
            "residual_k": rk, "h_shape_obstruction": shape,
            "contact_closure": closure, "reconstruction_zero": True}


def c1_endpoint_signature(ring, pieces):
    signature = {}
    for key, expression in pieces["residual_k"].terms.items():
        for component, value in five_leg_coefficient(key).items():
            signature[component] = signature.get(component, ring.number(0))+value*expression
    endpoints = (pieces["potential_h"].evaluate_static_profile(1, -1, -1)
                 -pieces["potential_h"].evaluate_static_profile(1, 1, 1))
    signature[(0, 0)] = signature.get((0, 0), ring.number(0))+endpoints
    return {key: value for key, value in signature.items() if value.terms}, endpoints


def control_templates(ring, pieces, normalizer):
    a, b, c = (ring.color(name) for name in ("a", "b", "c"))
    basis = exact.operator_basis(ring)
    templates, labels = [], []
    for i, j in itertools.combinations(range(8), 2):
        templates.append(basis[i](a, basis[j](b, c))-basis[j](a, basis[i](b, c)))
        labels.append({"kind": "R71_full_third_commutator", "pair": [exact.PARAMETERS[i], exact.PARAMETERS[j]]})
    for name in ("area", "cubic", "h_shape_obstruction", "contact_closure"):
        for key, value in sorted(pieces[name].terms.items()):
            templates.append(value)
            labels.append({"kind": "R77_weight_three" if name in ("area", "cubic") else "R79_closed_C1",
                           "source": name, "geometry_monomial": list(key)})
    seen, kept, kept_labels, duplicates = {}, [], [], []
    for value, label in zip(templates, labels):
        normalized = normalizer.word.expression(value)
        digest = normalized.digest()
        if not normalized.terms:
            duplicates.append({"label": label, "reason": "verified_zero_word_representative"})
            continue
        if digest in seen:
            duplicates.append({"label": label, "same_representative_as": seen[digest]})
            continue
        index = len(kept)
        seen[digest] = index
        kept.append(value)
        kept_labels.append({**label, "original_template_sha256": ring.digest(value),
                            "normalized_template_sha256": digest})
    return kept, kept_labels, duplicates


def verify_inner_symmetry(ring, expressions, normalizer):
    b, c = ring.color("b"), ring.color("c")
    checked = 0
    for expression in expressions:
        delta = expression-ring.substitute(expression, {"b": c, "c": b})
        if normalizer.expression(delta).terms:
            raise AssertionError("actual inner-slot symmetry check failed")
        checked += 1
    ring.substitution_cache.clear()
    return checked


def third_vector(expression, normalizer):
    # Tag zero is only a row namespace for the trilinear-template space.
    # It is not the physical fourth constant Fourier mode.
    return colored.vector_from_modes({0: expression}, normalizer)


def third_from_vector(vector, normalizer):
    terms = {}
    for (tag, monomial, word), coefficient in vector.items():
        if tag != 0:
            raise AssertionError("third-template row tag")
        terms[(monomial, word)] = coefficient
    return normalizer.word.to_old(words.WordExpr(normalizer.word, terms))


def pre_reduce_templates(ring, templates, normalizer):
    """Remove exact dependencies before computing expensive quartic responses.

    The retained templates are an original subset, never independently fitted
    mode columns. Every dropped template is checked from its original formula.
    """
    vectors = [third_vector(template, normalizer) for template in templates]
    span = colored.JointSpan(vectors, ring.limits)
    kept = span.independent
    selected = set(kept)
    fresh = colored.ColoredNormalizer(ring)
    dependencies = []
    for index, (template, vector) in enumerate(zip(templates, vectors)):
        if index in selected:
            continue
        coefficients, residual = span.reduce(vector)
        if residual or not set(coefficients).issubset(selected):
            raise AssertionError("third-template pre-reduction representation")
        original = template-sum((value*templates[j] for j, value in coefficients.items()), ring.number(0))
        zero = fresh.word.expression(original)
        if zero.terms:
            raise AssertionError("third-template dependence failed original-form verification")
        dependencies.append({"original_template_index": index,
                             "original_basis_coefficients": [[j, str(v)] for j, v in sorted(coefficients.items())],
                             "original_zero_sha256": zero.digest()})
    return span, kept, {"input_template_count": len(templates),
                        "retained_original_indices": kept,
                        "template_representative_rank": len(kept),
                        "verified_original_dependencies": dependencies,
                        "actual_function_independence_claimed": False}


def pre_reduce_baseline(ring, signature, all_templates, kept, span, normalizer):
    """Absorb reachable baseline terms before computing the quartic response.

    If baseline=sum(alpha_i*T_i)+R, the later solve uses target+B(R).
    Final cancellation is -(alpha+beta), always checked on the old baseline.
    """
    old_to_new = {old: new for new, old in enumerate(kept)}
    fresh = colored.ColoredNormalizer(ring)
    result = {}
    signature = dict(signature)
    signature.setdefault((0, 0), ring.number(0))
    for key, baseline in sorted(signature.items()):
        coefficients, residual = span.reduce(third_vector(baseline, normalizer))
        if not set(coefficients).issubset(old_to_new):
            raise AssertionError("baseline absorption uses a discarded source column")
        reduced = third_from_vector(residual, normalizer)
        original = baseline-reduced-sum((value*all_templates[j] for j, value in coefficients.items()),
                                       ring.number(0))
        zero = fresh.word.expression(original)
        if zero.terms:
            raise AssertionError("baseline absorption failed original-form verification")
        absorbed = {old_to_new[j]: value for j, value in coefficients.items()}
        result[key] = {"original": baseline, "reduced": reduced, "absorbed": absorbed,
                       "report": {"original_third_sha256": ring.digest(baseline),
                                  "reduced_third_sha256": ring.digest(reduced),
                                  "original_profile_terms": len(baseline.terms),
                                  "reduced_profile_terms": len(reduced.terms),
                                  "absorbed_retained_template_coefficients": [[j, str(v)]
                                      for j, v in sorted(absorbed.items())],
                                  "original_decomposition_zero_sha256": zero.digest()}}
    return result


def expression_summary(ring, expression, normalizer):
    value = normalizer.word.expression(expression)
    return {"original_terms": len(expression.terms), "original_sha256": ring.digest(expression),
            "word": normalizer.word.summary(value)}


def readable_vector(vector, limit=24):
    def local_text(piece):
        power, jets = piece
        factors = (["x^"+str(power)] if power else [])
        for (name, order), count in sorted(__import__("collections").Counter(jets).items()):
            atom = name+"_d"+str(order)
            factors.append(atom if count == 1 else atom+"^"+str(count))
        return "*".join(factors) or "1"

    result = []
    for (mode, monomial, word), value in list(sorted(vector.items()))[:limit]:
        result.append({"mode": mode, "coefficient": str(value), "local": local_text(monomial),
                       "signed_right_word": [local_text(letter) for letter in word]})
    return {"terms": len(vector), "sha256": colored.vector_digest(vector),
            "initial_rows": result, "rows_truncated": len(vector) > limit}


def phase_gate_toy():
    """Check the two Fourier formulas on a complete artificial K/L basis."""
    # Coordinates are q^2, qbar^2, q odot qbar. All arithmetic is rational.
    D = {0: (F(1, 4), F(1, 4), F(0)),
         2: (F(-1, 4), F(0), F(0)), -2: (F(0), F(-1, 4), F(0))}
    target = (F(1, 4), F(1, 4), F(1, 2))
    d, q2 = (F(1, 2), F(1, 2), F(0)), (F(1), F(0), F(0))
    count = 0
    for family in ("K", "L"):
        positions = itertools.combinations_with_replacement(range(3), 2) if family == "K" else itertools.product(range(3), repeat=2)
        for i, j in positions:
            K, L = [[F(0)]*3 for _ in range(3)], [[F(0)]*3 for _ in range(3)]
            matrix = K if family == "K" else L
            matrix[i][j] = F(1)
            if family == "K":
                matrix[j][i] = F(1)

            def pair(M, x, y):
                return sum((M[u][v]*x[u]*y[v] for u in range(3) for v in range(3)), F(0))

            def Q(x, y):
                return pair(K, x, y)-(pair(L, x, y)+pair(L, y, x))/2

            values = {}
            for power, vector in D.items():
                values[power] = values.get(power, F(0))+pair(L, target, vector)
            for power, x in D.items():
                for degree, y in D.items():
                    values[power+degree] = values.get(power+degree, F(0))+Q(x, y)
            if values.get(4, F(0)) != Q(q2, q2)/16:
                raise AssertionError("R78 pure phase coefficient")
            if values.get(2, F(0)) != -(pair(L, target, q2)+Q(d, q2))/4:
                raise AssertionError("R78 mixed phase coefficient")
            if sum(values.values(), F(0)):
                raise AssertionError("zero phase exact seed")
            count += 1
    return {"independent_artificial_K_L_basis_elements": count,
            "both_complex_mode_formulas": True, "theta_zero_seed": True}


def small_toys():
    data = colored.small_colored_toys()
    if qadd(qpow(QA, 2), qadd(qscale(QA, -4), QONE)) != QZERO:
        raise AssertionError("quadratic field defining polynomial")
    if qpow(QA, -1) != (F(4), F(-1)) or qmul(QA, qpow(QA, -1)) != QONE:
        raise AssertionError("quadratic field inverse")
    # An artificial one-leg integral, not the actual endpoint path/density.
    key = [0]*8
    key[local.H], key[local.K], key[local.O] = 2, 1, 1
    got = integrate_leg(QA, QONE, QONE, 0, 1, tuple(key))
    if got != qscale(qpow(QA, 2), F(5, 6)):
        raise AssertionError("quadratic-field polynomial integral")
    data["quadratic_field_arithmetic"] = {"defining_polynomial": "a^2-4*a+1",
                                          "inverse_and_artificial_integral": True}
    data["phase_gate"] = phase_gate_toy()
    toy_limits = exact.Limits(seconds=90, nodes=20000, atoms=5000, terms=5000,
                              rewrites=20000, memory_mib=512)
    toy_ring = colored.ColoredRing(toy_limits)
    toy_normalizer = colored.ColoredNormalizer(toy_ring)
    a, b, c = (toy_ring.color(name) for name in ("a", "b", "c"))
    t0, t1, extra = a*b*c, a.D()*b*c, a*b.D()*c.D()
    toy_templates = [t0, t1, 2*t0-3*t1]
    toy_span, toy_kept, toy_report = pre_reduce_templates(toy_ring, toy_templates, toy_normalizer)
    baseline = pre_reduce_baseline(toy_ring, {(0, 0): 9*t0+t1+extra}, toy_templates,
                                   toy_kept, toy_span, toy_normalizer)[(0, 0)]
    if toy_kept != [0, 1] or toy_normalizer.expression(baseline["reduced"]-extra).terms:
        raise AssertionError("small artificial pre-response elimination")
    if baseline["absorbed"] != {0: F(9), 1: F(1)}:
        raise AssertionError("small artificial absorbed-control map")
    data["pre_response_reduction"] = {"artificial_templates": 3, "retained": toy_kept,
        "original_dependence_checked": len(toy_report["verified_original_dependencies"]) == 1,
        "baseline_absorption_original_checked": True,
        "response_compiler_called": False}
    data["research_compiler_called"] = False
    return data


def write_report(path, payload, max_bytes):
    data = (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n").encode()
    if len(data) > max_bytes:
        # Keep exact coefficients and identities; remove only human previews.
        for component in payload.get("endpoint_components", []):
            if "remainder" in component:
                component["remainder"].pop("initial_rows", None)
        payload.pop("duplicate_template_details", None)
        payload["readable_previews_removed_for_output_limit"] = True
        data = (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n").encode()
    if len(data) > max_bytes:
        payload = {"schema": SCHEMA, "completion": "output_limit",
                   "phase": payload.get("phase"), "full_json_bytes": len(data),
                   "full_json_sha256": hashlib.sha256(data).hexdigest(),
                   "source_hashes": payload.get("source_hashes"),
                   "joint_P1_identity_verified": False,
                   "not_a_negative_mathematical_result": True}
        data = (json.dumps(payload, indent=2, sort_keys=True)+"\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return len(data), hashlib.sha256(data).hexdigest(), payload["completion"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=300)
    parser.add_argument("--max-coefficient-nodes", type=int, default=600000)
    parser.add_argument("--max-profile-atoms", type=int, default=160000)
    parser.add_argument("--max-terms", type=int, default=120000)
    parser.add_argument("--max-rewrites", type=int, default=750000)
    parser.add_argument("--memory-mib", type=int, default=2048)
    parser.add_argument("--rational-bits", type=int, default=8192)
    parser.add_argument("--max-output-bytes", type=int, default=700000)
    args = parser.parse_args()
    if min(args.max_seconds, args.max_coefficient_nodes, args.max_profile_atoms,
           args.max_terms, args.max_rewrites, args.memory_mib,
           args.rational_bits, args.max_output_bytes) <= 0:
        parser.error("all budgets must be positive")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("the actual compiler is allowed only in this public repository's Actions")
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started", "phase": "dependencies",
              "scope": "unsymmetrized full-third operator and both complete-P1 complex modes",
              "source_hashes": {}, "github_sha": os.environ.get("GITHUB_SHA"),
              "github_run_id": os.environ.get("GITHUB_RUN_ID"),
              "github_repository": os.environ.get("GITHUB_REPOSITORY"),
              "limits": {"seconds": args.max_seconds, "coefficient_nodes": args.max_coefficient_nodes,
                         "profile_atoms": args.max_profile_atoms, "terms": args.max_terms,
                         "rewrite_calls": args.max_rewrites, "memory_polling_mib": args.memory_mib,
                         "elimination_rational_bits": args.rational_bits,
                         "output_bytes": args.max_output_bytes},
              "joint_P1_identity_verified": False,
              "profile_or_geometry_numerical_evaluation": False,
              "fourth_ruling_paid": False, "P0_paid": False,
              "finite_isometric_family_constructed": False,
              "embedding_or_reach_certified": False,
              "negative_result_scope": "an unreduced representative is not actual-function nonmembership",
              "physical_profile_domain": "a common compact I inside (1,infinity), further chosen to fit the finite real control words",
              "anchor": "I(F)=integral_r^xi F; all colors zero on the same right collar; no left tail reset",
              "normalization": "P1 divided by the common positive constant bulk time ell",
              "endpoint_scalar_path": {"start": ["1", "1", "1"], "end": ["1", "-1", "-1"],
                    "h_plus": "a=2+sqrt(3)", "h_minus": "a^-1=4-a",
                    "legs": ["h:1->a at k=1", "k:1->0 at h=a", "h:a->a^-1 at k=0",
                             "k:0->-1 at h=a^-1", "h:a^-1->1 at k=-1"],
                    "omega": "unique integral of dk/(2h), never reset",
                    "full_residual_k_integrated": True,
                    "scalar_path_alone_claimed_to_have_M0_or_frame_closure": False},
              "control_scope": "R71 full brackets + R77 full weight3 coefficient operators + R79 closed-C1 coefficient operators; M/frame repairs retained modulo these proved actual spaces"}
    ring = normalizer = None
    exit_code = 0
    try:
        report["source_hashes"] = dependencies()
        if args.toy_only:
            report["phase"] = "small_artificial_toys"
            report["toy"] = small_toys()
            report["completion"] = "toy_passed"
        else:
            limits = exact.Limits(args.max_seconds, args.max_coefficient_nodes,
                                  args.max_profile_atoms, args.max_terms,
                                  args.max_rewrites, args.memory_mib, args.rational_bits)
            ring = colored.ColoredRing(limits)
            normalizer = colored.ColoredNormalizer(ring)
            report["phase"] = "complete_constant_fourth_modes"
            all_targets, constant_records = compile_constant_targets(ring)
            targets = {mode: all_targets[mode] for mode in MODES}
            seed = sum(all_targets.values(), ring.number(0))
            if normalizer.expression(seed).terms:
                raise AssertionError("actual five-mode exact seed cancellation")
            report["constant_target"] = {"exact_theta_zero_seed": True,
                "modes": {str(mode): expression_summary(ring, value, normalizer)
                          for mode, value in targets.items()},
                "records_sha256": hashlib.sha256(canonical_bytes(constant_records)).hexdigest()}
            print(json.dumps({"completed": report["phase"], "nodes": len(ring.algebra.c.nodes)}), flush=True)
            report["phase"] = "colored_local_third_and_true_geometry_decomposition"
            density, local_records, expanded_nodes = compile_colored_local(ring)
            pieces = raw_decomposition(density, normalizer)
            signature, endpoint_potential = c1_endpoint_signature(ring, pieces)
            all_templates, all_labels, duplicates = control_templates(ring, pieces, normalizer)
            symmetry_count = verify_inner_symmetry(ring, all_templates+list(signature.values()), normalizer)
            report["colored_local"] = {"density": density.summary(),
                "pieces": {name: value.summary() for name, value in pieces.items()
                           if isinstance(value, local.GExpr)},
                "expanded_coefficient_nodes": expanded_nodes,
                "records_sha256": hashlib.sha256(canonical_bytes(local_records)).hexdigest(),
                "inner_symmetry_checks": symmetry_count,
                "full_exterior_inner_multidegree": {"a": 1, "b": 1, "c": 1},
                "whole_density_reconstruction": True,
                "endpoint_potential_difference": expression_summary(ring, endpoint_potential, normalizer)}
            report["all_original_control_templates"] = all_labels
            report["duplicate_template_count"] = len(duplicates)
            report["duplicate_template_details"] = duplicates
            print(json.dumps({"completed": report["phase"], "templates": len(all_templates),
                              "endpoint_field_components": len(signature)}), flush=True)
            report["phase"] = "exact_full_third_template_pre_reduction"
            template_span, kept, pre_report = pre_reduce_templates(ring, all_templates, normalizer)
            baseline_data = pre_reduce_baseline(ring, signature, all_templates, kept,
                                                template_span, normalizer)
            templates = [all_templates[index] for index in kept]
            labels = [{**all_labels[index], "original_template_index": index} for index in kept]
            report["control_templates"] = labels
            report["pre_response_reduction"] = pre_report
            report["baseline_pre_reduction"] = [
                {"field_component": {"log_a_power": key[0], "a_power": key[1]}, **value["report"]}
                for key, value in sorted(baseline_data.items())]
            print(json.dumps({"completed": report["phase"], "input_templates": len(all_templates),
                              "retained_templates": len(templates),
                              "baseline_reduced_terms": [len(x["reduced"].terms)
                                                         for x in baseline_data.values()]}), flush=True)
            report["phase"] = "same_control_complete_phase_response_columns"
            columns = []
            for index, template in enumerate(templates):
                column_started = time.monotonic()
                third = colored.ThirdOperator(ring, template, labels[index])
                response = colored.full_phase_response(ring, third)
                vector = colored.vector_from_modes(response, normalizer)
                columns.append(vector)
                labels[index]["joint_response_terms"] = len(vector)
                labels[index]["joint_response_sha256"] = colored.vector_digest(vector)
                labels[index]["response_seconds"] = time.monotonic()-column_started
                report["response_checkpoint"] = {"completed_columns": index+1, "total_columns": len(templates)}
                ring.substitution_cache.clear()
                if index % 16 == 0:
                    print(json.dumps({"column": index, "of": len(templates),
                                      "profile_atoms": len(ring.p.atoms)}), flush=True)
                limits.formal.time_check()
            report["phase"] = "joint_whole_function_span"
            span = colored.JointSpan(columns, limits)
            report["joint_span"] = span.summary()
            report["endpoint_components"] = []
            all_verified = True
            for key, baseline_record in sorted(baseline_data.items()):
                baseline = baseline_record["reduced"]
                third = colored.ThirdOperator(ring, baseline)
                response = colored.full_phase_response(ring, third)
                original = {mode: response[mode]+(targets[mode] if key == (0, 0) else ring.number(0))
                            for mode in MODES}
                vector = colored.vector_from_modes(original, normalizer)
                coefficients, residual = span.reduce(vector)
                total_coefficients = dict(baseline_record["absorbed"])
                for index, value in coefficients.items():
                    words.add_term(total_coefficients, index, value)
                row = {"field_component": {"log_a_power": key[0], "a_power": key[1]},
                       "baseline_third_sha256": ring.digest(baseline_record["original"]),
                       "pre_reduced_baseline_third_sha256": ring.digest(baseline),
                       "joint_target_terms": len(vector), "joint_target_sha256": colored.vector_digest(vector),
                       "remainder": readable_vector(residual),
                       "control_coefficients_for_cancellation": [[index, str(-value)]
                            for index, value in sorted(total_coefficients.items()) if value],
                       "verified_from_original_compiled_expressions": False}
                if residual:
                    all_verified = False
                else:
                    # Fresh positive verification: construct the actual full
                    # third template before applying its nonlinear-looking
                    # (but exactly linear in T) two-mode response.
                    corrected = baseline_record["original"]-sum(
                        (value*templates[index] for index, value in total_coefficients.items()), ring.number(0))
                    fresh_response = colored.full_phase_response(ring, colored.ThirdOperator(ring, corrected))
                    fresh = colored.ColoredNormalizer(ring)
                    checks = {}
                    for mode in MODES:
                        value = fresh_response[mode]+(targets[mode] if key == (0, 0) else ring.number(0))
                        reduced = fresh.word.expression(value)
                        if reduced.terms:
                            raise AssertionError("positive joint identity failed fresh original-root verification")
                        checks[str(mode)] = reduced.digest()
                    row["verified_from_original_compiled_expressions"] = True
                    row["fresh_mode_zero_sha256"] = checks
                report["endpoint_components"].append(row)
                ring.substitution_cache.clear()
            report["joint_P1_identity_verified"] = all_verified
            report["positive_interpretation"] = (
                "If true, the same exact finite third-control coefficients cancel both complex P1 modes for every common smooth profile; R71/R77/R79 supply real finite control existence, not a numerically compiled bridge or P0/ruling solution")
            report["field_reconstruction"] = "sum a^j*log(a)^m*component; a=2+sqrt(3); componentwise zero is sufficient and no transcendence assumption is used"
            report["completion"] = "complete"
    except formal.CompilationBudgetExceeded as exc:
        report["completion"] = "resource_limit"
        report["error"] = str(exc)
        report["not_a_negative_mathematical_result"] = True
        exit_code = 2
    except Exception as exc:
        report["completion"] = "implementation_check_failed"
        report["error"] = type(exc).__name__+": "+str(exc)
        report["joint_P1_identity_verified"] = False
        exit_code = 2
    report["elapsed_seconds"] = time.monotonic()-started
    report["max_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    if ring is not None:
        report["compiler_size"] = {"coefficient_nodes": len(ring.algebra.c.nodes),
                                    "histories": len(ring.algebra.c.state_rhs),
                                    "profile_atoms": len(ring.p.atoms)}
    if normalizer is not None:
        report["word_statistics"] = normalizer.word.stats
    size, digest, completion = write_report(args.output, report, args.max_output_bytes)
    if completion == "output_limit":
        exit_code = 2
    print(json.dumps({"completion": completion, "output": str(args.output),
                      "bytes": size, "sha256": digest,
                      "joint_P1_identity_verified": report["joint_P1_identity_verified"]}), flush=True)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
