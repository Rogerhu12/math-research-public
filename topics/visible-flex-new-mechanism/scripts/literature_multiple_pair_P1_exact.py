#!/usr/bin/env python3
"""Two genuinely different positive reciprocal pairs: full P1 exact gate.

States (H,d)=(1,0),(1,1) have equal positive complete-frame periods.
The same global profile and right anchor are used throughout.  Original
two-mode response dependencies are verified before any modular rank bound.
Only public repository Actions may compile/evaluate the research target.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

import literature_colored_profile_algebra as colored
import literature_full_phase_bridge_exact as producer
import literature_full_phase_rational_dual as dual
import literature_pure_bulk_exact_membership as exact
import literature_range_profile_algebra as formal
import literature_rational_volterra_polynomial as poly


SCHEMA = "visible-flex-two-positive-pairs-complete-P1-v1"
STATES = ((F(1), F(0)), (F(1), F(1)))
DUAL_SHA = "bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f"
POLY_SHA = "6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def dependencies():
    data = dual.dependencies()
    if data["driver"]["sha256"] != DUAL_SHA or data["polynomial_evaluator"]["sha256"] != POLY_SHA:
        raise ValueError("explicitly rebind changed rational-evaluation dependencies")
    data["single_pair_evaluation_driver"] = data.pop("driver")
    data["driver"] = dual.file_identity(__file__)
    return data


class AffinePullback:
    """Conjugate a complete original profile expression by x=H*xi+d.

    Each input jet of order m gains H^-m. Every genuine right primitive
    gains H, with its anchor transformed at the same time. No left reset.
    """
    def __init__(self, ring, scale, offset):
        self.ring, self.scale, self.offset = ring, F(scale), F(offset)
        if self.scale <= 0:
            raise ValueError("the true geometry covariance requires H>0")
        self.identity = self.scale == 1 and self.offset == 0
        self.x = self.scale*ring.x()+self.offset
        self.atoms, self.monomials, self.expressions = {}, {}, {}
        self.powers = {0: ring.number(1), 1: self.x}

    def atom(self, identifier):
        if identifier not in self.atoms:
            node = self.ring.p.atoms[identifier]
            if node[0] == "jet":
                value = self.scale**(-node[2])*self.ring.monomial(self.ring.p.jet(node[1], node[2]))
            elif node[0] == "int_right":
                value = self.scale*self.monomial(node[1]).I()
            else:
                raise ValueError("unsupported original affine profile atom")
            self.atoms[identifier] = value
        return self.atoms[identifier]

    def monomial(self, monomial):
        if monomial not in self.monomials:
            power, atoms = monomial
            if power < 0:
                raise ValueError("this polynomial affine map does not invert xi")
            if power not in self.powers:
                self.powers[power] = self.x**power
            value = self.powers[power]
            for atom in atoms:
                value = value*self.atom(atom)
            self.monomials[monomial] = value
        return self.monomials[monomial]

    def expression(self, expression):
        if self.identity:
            return expression
        key = expression.key()
        if key not in self.expressions:
            value = self.ring.number(0)
            for monomial, coefficient in expression.terms.items():
                value += coefficient*self.monomial(monomial)
            self.expressions[key] = value
        return self.expressions[key]

    def modes(self, expressions):
        return {mode: self.expression(expression) for mode, expression in expressions.items()}


def source_pair_label(pair_index):
    scale, offset = STATES[pair_index]
    return {"pair": pair_index, "H": str(scale), "d": str(offset),
            "positive_complete_frame_turns_per_N": 1,
            "bulk_duration_per_N": "sqrt(2)*pi",
            "relative_positive_weight": "1"}


def exact_problem(limits, receipt, report):
    ring, constant, templates, baseline, binding = dual.compile_original_problem(limits, receipt)
    normalizer = colored.ColoredNormalizer(ring)
    baseline_small = normalizer.expression(baseline)
    fresh = colored.ColoredNormalizer(ring)
    baseline_zero = fresh.word.expression(baseline-baseline_small)
    if baseline_zero.terms:
        raise AssertionError("baseline representative failed original-form verification")
    report["original_problem"] = binding
    report["baseline_working_representative"] = {
        "original_terms": len(baseline.terms), "working_terms": len(baseline_small.terms),
        "original_sha256": ring.digest(baseline), "working_sha256": ring.digest(baseline_small),
        "fresh_original_difference_zero_sha256": baseline_zero.digest(),
        "negative_evaluation_uses_original_not_this_representative": True}
    standard_baseline = colored.full_phase_response(ring, colored.ThirdOperator(ring, baseline_small))
    standard_target = {mode: constant[mode]+standard_baseline[mode] for mode in producer.MODES}
    pullbacks = [AffinePullback(ring, H, d) for H, d in STATES]
    target = {mode: sum((pullback.expression(standard_target[mode]) for pullback in pullbacks), ring.number(0))
              for mode in producer.MODES}
    target_vector = colored.vector_from_modes(target, normalizer)
    columns, originals, labels = [], [], []
    for template_index, template in enumerate(templates):
        standard = colored.full_phase_response(ring, colored.ThirdOperator(ring, template))
        for pair_index, pullback in enumerate(pullbacks):
            started = time.monotonic()
            original = pullback.modes(standard)
            column = colored.vector_from_modes(original, normalizer)
            index = len(columns)
            columns.append(column)
            originals.append(original)
            labels.append({"original_column": index, **source_pair_label(pair_index),
                "standard_template_index": template_index,
                "v2_original_template_index": binding["retained_original_indices"][template_index],
                "standard_original_template_sha256": ring.digest(template),
                "original_response_sha256": {str(mode): ring.digest(original[mode]) for mode in producer.MODES},
                "word_response_sha256": colored.vector_digest(column),
                "word_terms": len(column), "normalization_seconds": time.monotonic()-started})
            report["response_checkpoint"] = {"completed_columns": len(columns), "total_columns": 72}
        ring.substitution_cache.clear()
        if template_index % 6 == 0:
            print(json.dumps({"phase": "two_state_original_response_columns", "completed": len(columns),
                              "profile_atoms": len(ring.p.atoms)}), flush=True)
        limits.formal.time_check()
    report["all_original_columns"] = labels
    report["phase"] = "sound_joint_response_reduction"
    span = colored.JointSpan(columns, limits)
    retained = span.independent
    retained_set = set(retained)
    fresh = colored.ColoredNormalizer(ring)
    proofs = []
    for index, original in enumerate(originals):
        if index in retained_set:
            continue
        coefficients, remainder = span.reduce(columns[index])
        if remainder or not set(coefficients).issubset(retained_set):
            raise AssertionError("response spanning decomposition")
        zeros = {}
        for mode in producer.MODES:
            value = original[mode]-sum((coefficient*originals[j][mode]
                for j, coefficient in coefficients.items()), ring.number(0))
            reduced = fresh.word.expression(value)
            if reduced.terms:
                raise AssertionError("discarded response failed fresh original two-mode verification")
            zeros[str(mode)] = reduced.digest()
        proofs.append({"discarded_original_column": index,
            "retained_original_coefficients": [[j, str(c)] for j, c in sorted(coefficients.items())],
            "fresh_original_mode_zero_sha256": zeros})
        limits.formal.time_check()
    report["response_reduction"] = {"original_columns": len(columns),
        "retained_original_columns": retained, "proved_true_response_dimension_upper_bound": len(retained),
        "verified_original_two_mode_dependencies": proofs,
        "actual_function_independence_not_assumed": True}
    coefficients, remainder = span.reduce(target_vector)
    report["joint_word_target"] = {"terms": len(target_vector), "sha256": colored.vector_digest(target_vector)}
    report["joint_word_remainder"] = producer.readable_vector(remainder, 16)
    report["provisional_coefficients_to_subtract"] = [[j, str(c)] for j, c in sorted(coefficients.items())]
    if not remainder:
        report["phase"] = "positive_original_whole_function_verification"
        corrected_modes = {mode: ring.number(0) for mode in producer.MODES}
        for pair_index, pullback in enumerate(pullbacks):
            corrected = baseline-sum((value*templates[labels[j]["standard_template_index"]]
                for j, value in coefficients.items() if labels[j]["pair"] == pair_index), ring.number(0))
            response = colored.full_phase_response(ring, colored.ThirdOperator(ring, corrected))
            for mode in producer.MODES:
                corrected_modes[mode] += pullback.expression(constant[mode]+response[mode])
        fresh = colored.ColoredNormalizer(ring)
        checks = {}
        for mode in producer.MODES:
            value = fresh.word.expression(corrected_modes[mode])
            if value.terms:
                raise AssertionError("positive joint identity failed original baseline and true-state verification")
            checks[str(mode)] = value.digest()
        report["whole_function_positive_identity_verified"] = True
        report["positive_certificate"] = {"fresh_original_mode_zero_sha256": checks,
            "actual_control_coefficients_relative_to_true_rational_baseline": [
                {"pair": labels[j]["pair"], "standard_template_index": labels[j]["standard_template_index"],
                 "coefficient": str(-value)} for j, value in sorted(coefficients.items())],
            "both_positive_pair_weights": ["1", "1"],
            "same_global_profile_and_target": True,
            "true_finite_bridge_existence_source": "R80/R89; no quantitative length or embedding assertion"}
    return ring, constant, templates, baseline, retained, labels


def evaluate_original_pairs(args, ring, constant, templates, baseline, retained, labels, started, report):
    points = [F(j, args.points+1) for j in range(1, args.points+1)]
    row_labels = [{"global_t": str(t), "global_xi": str(2+t), "mode": mode, "component": part}
                  for t in points for mode in producer.MODES for part in ("real", "imaginary")]
    contexts, targets, third_caches, arithmetic = [], [], [], []
    for pair_index, (H, d) in enumerate(STATES):
        remaining = args.max_seconds-(time.monotonic()-started)
        if remaining <= 0:
            raise poly.PolynomialBudgetExceeded("total budget exhausted before original modular evaluation")
        context = poly.PolynomialContext(args.prime, 2*H+d, 3*H+d, seconds=remaining,
            max_degree=args.max_degree, memory_mib=args.memory_mib, max_operations=args.max_operations)
        # The coefficients in the *same t* are identical. Only the standard
        # coordinate x=H*xi+d and its true derivative/integral scales change.
        f, g, _ = dual.fixed_profiles(context, args.bump_power)
        context.colors = {"q": f+context.number((0, 1))*g,
                          "qbar": f-context.number((0, 1))*g}
        raw = poly.RawExpressionEvaluator(ring.p, context, context.colors)
        base_response = colored.full_phase_response(context,
            poly.EvaluatedThirdOperator(ring.p, context, baseline))
        targets.append({mode: raw.expression(constant[mode])+base_response[mode] for mode in producer.MODES})
        contexts.append(context)
        third_caches.append({})
    prime = args.prime
    target_rows = [sum(targets[j][mode].value(t)[part] for j in range(len(STATES))) % prime
                   for t in points for mode in producer.MODES for part in (0, 1)]
    columns, identities = [], []
    for new_index, original_index in enumerate(retained):
        label = labels[original_index]
        pair_index, template_index = label["pair"], label["standard_template_index"]
        context = contexts[pair_index]
        if template_index not in third_caches[pair_index]:
            third_caches[pair_index][template_index] = colored.full_phase_response(context,
                poly.EvaluatedThirdOperator(ring.p, context, templates[template_index]))
        response = third_caches[pair_index][template_index]
        columns.append([value for t in points for mode in producer.MODES for value in response[mode].value(t)])
        identities.append({"retained_column": new_index, "original_column": original_index,
            "pair": pair_index, "standard_template_index": template_index,
            "mode_polynomial_sha256": {str(mode): response[mode].digest() for mode in producer.MODES}})
        report["modular_checkpoint"] = {"completed_retained_columns": new_index+1,
                                         "total_retained_columns": len(retained)}
        if new_index % 12 == 0:
            print(json.dumps({"phase": "original_two_pair_modular_values", "completed": new_index+1,
                              "of": len(retained)}), flush=True)
        for current in contexts:
            current.check(0)
    rows = [[column[i] for column in columns] for i in range(len(row_labels))]
    certificate = poly.full_column_dual(rows, target_rows, prime)
    if certificate["rational_nonmembership_certified"]:
        certificate["selected_evaluation_labels"] = [row_labels[i]
                                                       for i in certificate["selected_augmented_rows"]]
    for pair_index, context in enumerate(contexts):
        arithmetic.append({**source_pair_label(pair_index), **context.coefficient_report()})
    return {"same_global_profile": {"support": ["2", "3"], "t": "xi-2",
            "f": "[t*(1-t)]^m", "g": "[t*(1-t)]^m*(1+2*t+3*t^2+5*t^3)",
            "m": args.bump_power, "three_moment_conditions_imposed": False},
        "original_affine_conjugacy_evaluated_not_word_representatives": True,
        "all_evaluation_labels": row_labels, "row_count": len(rows),
        "column_count_equal_to_proved_upper_bound": len(retained),
        "retained_column_identities": identities,
        "all_modular_matrix_values_sha256": hashlib.sha256(canonical(rows)).hexdigest(),
        "all_modular_target_values_sha256": hashlib.sha256(canonical(target_rows)).hexdigest(),
        "coefficient_arithmetic_by_state": arithmetic, "dual_certificate": certificate}


def small_toys():
    limits = exact.Limits(seconds=60, nodes=5000, atoms=3000, terms=3000,
                          rewrites=10000, memory_mib=256)
    ring = colored.ColoredRing(limits)
    a, b = ring.color("a"), ring.color("b")
    x = ring.x()
    expression = (x*a*b.D()).I()+x*x*a.D()*b
    transform = AffinePullback(ring, 2, 3)
    norm = colored.ColoredNormalizer(ring)
    checks = {}

    def zero(value, name):
        if norm.expression(value).terms:
            raise AssertionError(name)
        checks[name] = True

    zero(transform.expression(expression.D())-transform.expression(expression).D()/2,
         "affine_derivative_scale")
    zero(transform.expression(expression.I())-2*transform.expression(expression).I(),
         "affine_true_right_primitive_scale")
    composed = AffinePullback(ring, 3, -1).expression(transform.expression(expression))
    zero(composed-AffinePullback(ring, 6, 1).expression(expression),
         "affine_composition_on_all_nested_original_atoms")
    global_context = poly.PolynomialContext(101, 2, 5, seconds=30, max_degree=30)
    standard_context = poly.PolynomialContext(101, 7, 13, seconds=30, max_degree=30)
    global_t, standard_t = global_context.variable(), standard_context.variable()
    direct_global = poly.RawExpressionEvaluator(ring.p, global_context,
        {"a": global_t*global_t, "b": 1+2*global_t+global_t**3})
    direct_standard = poly.RawExpressionEvaluator(ring.p, standard_context,
        {"a": standard_t*standard_t, "b": 1+2*standard_t+standard_t**3})
    if direct_global.expression(transform.expression(expression)).key() != direct_standard.expression(expression).key():
        raise AssertionError("affine pullback versus original standard-coordinate evaluation")
    checks["affine_original_expression_agrees_with_transformed_interval_evaluator"] = True
    # Small artificial TWO-mode response columns, not a P1 target/compiler.
    original = [{-4: a*b, -2: a.D()*b}, {-4: a*b.D(), -2: a*b},
                {-4: 2*a*b-3*a*b.D(), -2: 2*a.D()*b-3*a*b}]
    vectors = [colored.vector_from_modes(value, norm) for value in original]
    span = colored.JointSpan(vectors, limits)
    coefficients, residual = span.reduce(vectors[2])
    if span.independent != [0, 1] or residual:
        raise AssertionError("artificial two-mode response span")
    fresh = colored.ColoredNormalizer(ring)
    for mode in producer.MODES:
        value = original[2][mode]-sum((c*original[j][mode] for j, c in coefficients.items()), ring.number(0))
        if fresh.expression(value).terms:
            raise AssertionError("artificial fresh original two-mode dependency")
    checks["same_coefficients_and_fresh_original_response_dependence"] = True
    poly_toy = poly.small_toys()
    return {"scope": "artificial affine algebra and three small joint columns only",
        "checks": checks, "all_passed": all(checks.values()) and poly_toy["all_passed"],
        "polynomial_dual_toy": poly_toy,
        "research_target_compiled": False, "research_profile_evaluated": False,
        "real_geometry_integrated": False}


def write_report(path, payload, maximum):
    raw = (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n").encode()
    if len(raw) > maximum:
        payload = {"schema": SCHEMA, "completion": "output_limit",
            "full_bytes": len(raw), "full_sha256": hashlib.sha256(raw).hexdigest(),
            "source_hashes": payload.get("source_hashes"),
            "whole_function_positive_identity_verified": False,
            "rational_nonmembership_certified": False,
            "reason": "a complete independently checkable certificate was not published"}
        raw = (json.dumps(payload, indent=2, sort_keys=True)+"\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return len(raw), hashlib.sha256(raw).hexdigest(), payload["completion"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--input-receipt", type=Path, default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=480)
    parser.add_argument("--memory-mib", type=int, default=2048)
    parser.add_argument("--prime", type=int, default=2147483647)
    parser.add_argument("--points", type=int, default=48)
    parser.add_argument("--bump-power", type=int, default=8)
    parser.add_argument("--max-degree", type=int, default=256)
    parser.add_argument("--max-operations", type=int, default=20000000)
    parser.add_argument("--max-output-bytes", type=int, default=650000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.points, args.max_degree,
           args.max_operations, args.max_output_bytes) <= 0 or args.bump_power < 8:
        parser.error("positive budgets and bump-power>=8 required")
    if args.points+1 >= args.prime:
        parser.error("evaluation denominators must be below the prime")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("the real two-pair target is restricted to this public repository's Actions")
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started", "phase": "dependencies",
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"), "source_hashes": {},
        "states": [source_pair_label(i) for i in range(len(STATES))],
        "limits": {"seconds": args.max_seconds, "memory_polling_mib": args.memory_mib,
            "output_bytes": args.max_output_bytes, "coefficient_nodes": 600000,
            "profile_atoms": 240000, "expression_terms": 180000, "word_rewrite_calls": 1500000,
            "elimination_rational_bits": 16384, "modular_polynomial_degree": args.max_degree,
            "modular_prime": args.prime, "evaluation_points": args.points,
            "bump_power": args.bump_power, "modular_operations_per_state": args.max_operations},
        "whole_function_positive_identity_verified": False,
        "rational_nonmembership_certified": False,
        "scope": "two fixed different real reciprocal states with equal positive complete-frame bulk times",
        "same_global_profile_and_right_anchor": True,
        "independent_true_internal_bridges": True,
        "cross_pair_M0_connectors_costs_retained_in_P0": True,
        "P0_paid": False, "fourth_ruling_paid": False,
        "finite_isometric_family_constructed": False, "embedding_or_reach_certified": False,
        "all_profiles_excluded": False, "all_multiple_state_configurations_excluded": False}
    code = 0
    try:
        report["source_hashes"] = dependencies()
        if args.toy_only:
            report["phase"] = "small_artificial_affine_and_span_toys"
            report["toy"] = small_toys()
            report["completion"] = "toy_passed"
        else:
            receipt = dual.read_receipt(args.input_receipt)
            report["input_receipt"] = {"bytes": dual.RECEIPT_BYTES, "sha256": dual.RECEIPT_SHA,
                "source": dual.RECEIPT_SOURCE, "driver_sha256": producer.dependencies()["driver"]["sha256"]}
            limits = exact.Limits(args.max_seconds, 600000, 240000, 180000,
                                  1500000, args.memory_mib, 16384)
            report["phase"] = "original_standard_problem_and_two_affine_states"
            ring, constant, templates, baseline, retained, labels = exact_problem(limits, receipt, report)
            if not report["whole_function_positive_identity_verified"]:
                report["phase"] = "direct_original_values_after_proved_response_upper_bound"
                report["original_evaluation"] = evaluate_original_pairs(
                    args, ring, constant, templates, baseline, retained, labels, started, report)
                report["rational_nonmembership_certified"] = report["original_evaluation"]["dual_certificate"]["rational_nonmembership_certified"]
            report["completion"] = "complete"
            report["compiler_size"] = {"coefficient_nodes": len(ring.algebra.c.nodes),
                                        "profile_atoms": len(ring.p.atoms)}
            report["interpretation"] = (
                "A positive result is verified on both original whole-function modes with the same real controls. A negative result requires a nonzero rational augmented minor at the proved full response dimension; otherwise the result is undecided. Neither outcome pays P0, the fourth ruling, higher orders, or the main embedded thick-surface task.")
    except (formal.CompilationBudgetExceeded, poly.PolynomialBudgetExceeded) as exc:
        report["completion"], report["error"], code = "resource_limit", str(exc), 2
        report["not_a_negative_mathematical_result"] = True
    except Exception as exc:
        report["completion"], report["error"], code = "implementation_check_failed", type(exc).__name__+": "+str(exc), 2
        report["whole_function_positive_identity_verified"] = False
        report["rational_nonmembership_certified"] = False
    report["elapsed_seconds"] = time.monotonic()-started
    report["max_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    size, digest, completion = write_report(args.output, report, args.max_output_bytes)
    if completion == "output_limit":
        code = 2
    print(json.dumps({"completion": completion, "bytes": size, "sha256": digest,
                      "output": str(args.output)}), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
