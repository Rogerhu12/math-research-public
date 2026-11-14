#!/usr/bin/env python3
"""Exact signed-right word/shuffle layer for the frozen pure P1 producer.

The research target and all 28 responses are compiled only by public Actions.
--toy-only checks small formal identities, without a profile or geometry.
This module does not change the old producer or claim a complete differential
normal form. A negative span result remains inconclusive for actual functions.
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

import literature_pure_bulk_exact_membership as old


EXPECTED_PRODUCER_SHA256 = "f7f3e3c6c8732ad9da047fb6005d314dc8568c189fe3cc0c9edef8843051eb70"
SCHEMA = "signed-right-local-word-shuffle-ibp-v1"
ONE = (0, ())


def add_term(terms, key, value):
    value = terms.get(key, F(0)) + value
    if value:
        terms[key] = value
    else:
        terms.pop(key, None)


def local_product(left, right):
    return left[0] + right[0], tuple(sorted(left[1] + right[1]))


def local_derivative(monomial):
    power, jets = monomial
    result = {}
    if power:
        add_term(result, (power-1, jets), F(power))
    for order, count in Counter(jets).items():
        remaining = list(jets)
        remaining.remove(order)
        remaining.append(order+1)
        add_term(result, (power, tuple(sorted(remaining))), F(count))
    return result


def local_text(monomial):
    power, jets = monomial
    parts = []
    if power:
        parts.append("x" if power == 1 else "x^%s" % power)
    for order, count in sorted(Counter(jets).items()):
        label = "q%s" % order
        parts.append(label if count == 1 else "%s^%s" % (label, count))
    return "*".join(parts) or "1"


class WordExpr:
    """Sum c L(x,q_j) I_word; every letter of word is a local monomial."""

    def __init__(self, owner, terms=None):
        self.owner = owner
        self.terms = {key: F(value) for key, value in (terms or {}).items() if value}
        owner.check_terms(self.terms)

    def __add__(self, other):
        if not isinstance(other, WordExpr) or other.owner is not self.owner:
            raise ValueError("one exact right anchor and one word owner are required")
        terms = dict(self.terms)
        for key, value in other.terms.items():
            add_term(terms, key, value)
        return WordExpr(self.owner, terms)

    def __neg__(self):
        return WordExpr(self.owner, {key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def scale(self, scalar):
        return WordExpr(self.owner, {key: F(scalar)*value for key, value in self.terms.items()})

    def digest(self):
        rows = [[local, word, value.numerator, value.denominator]
                for (local, word), value in sorted(self.terms.items())]
        return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


class WordNormalizer:
    """Sound all-depth shuffle and local-jet IBP, not a completeness claim.

    I_w(x) = integral_r^x f1(t) I_tail(t) dt. All products of I_w use the
    full shuffle identity. The integration rule is I(D F I_w) = F I_w -
    I(F D I_w). Its right boundary is zero if w is nonempty; for empty w
    this rule is used only when F has positive profile weight, so F(r)=0.
    No left endpoint is reset. Cycle fallback retains the exact raw word.
    """

    def __init__(self, ring, max_calls=250000, max_terms=80000,
                 max_weight=4, max_shuffle_entries=100000):
        self.ring = ring
        self.limits = ring.limits
        self.max_calls = max_calls
        self.max_terms = max_terms
        self.max_weight = max_weight
        self.max_shuffle_entries = max_shuffle_entries
        self.atom_cache = {}
        self.monomial_cache = {}
        self.primitive_cache = {}
        self.shuffle_cache = {}
        self.to_old_word_cache = {}
        self.active = set()
        self.stats = {
            "primitive_calls": 0,
            "unique_high_jet_IBP": 0,
            "nonempty_word_polynomial_IBP": 0,
            "all_depth_shuffle_calls": 0,
            "shuffle_cache_entries": 0,
            "max_shuffle_product_word_length": 0,
            "max_word_length_seen": 0,
            "cycle_fallbacks": 0,
        }

    def check_terms(self, terms):
        if len(terms) > self.max_terms:
            raise old.formal.CompilationBudgetExceeded("word expression term budget")
        self.limits.check()
        for (local, word), coefficient in terms.items():
            weight = len(local[1]) + sum(len(letter[1]) for letter in word)
            if weight > self.max_weight:
                raise old.formal.CompilationBudgetExceeded("declared word profile weight")
            if any(not letter[1] for letter in word):
                raise AssertionError("zero-profile-weight word letters must be eliminated with their boundary")
            self.stats["max_word_length_seen"] = max(self.stats["max_word_length_seen"], len(word))

    def zero(self):
        return WordExpr(self)

    def term(self, local=ONE, word=(), coefficient=F(1)):
        return WordExpr(self, {(local, tuple(word)): F(coefficient)} if coefficient else {})

    def shuffle(self, left, right):
        if not left:
            return {right: 1}
        if not right:
            return {left: 1}
        key = (left, right) if left <= right else (right, left)
        if key in self.shuffle_cache:
            return self.shuffle_cache[key]
        self.stats["all_depth_shuffle_calls"] += 1
        self.stats["max_shuffle_product_word_length"] = max(
            self.stats["max_shuffle_product_word_length"], len(left)+len(right))
        self.limits.check()
        answer = {}
        for tail, multiplicity in self.shuffle(left[1:], right).items():
            word = (left[0],) + tail
            answer[word] = answer.get(word, 0) + multiplicity
        for tail, multiplicity in self.shuffle(left, right[1:]).items():
            word = (right[0],) + tail
            answer[word] = answer.get(word, 0) + multiplicity
        self.shuffle_cache[key] = answer
        self.stats["shuffle_cache_entries"] = len(self.shuffle_cache)
        if len(self.shuffle_cache) > self.max_shuffle_entries:
            raise old.formal.CompilationBudgetExceeded("word shuffle cache budget")
        return answer

    def multiply(self, left, right):
        terms = {}
        for (lm, lw), lc in left.terms.items():
            for (rm, rw), rc in right.terms.items():
                product = local_product(lm, rm)
                for word, multiplicity in self.shuffle(lw, rw).items():
                    add_term(terms, (product, word), lc*rc*multiplicity)
            self.limits.check()
            if len(terms) > self.max_terms:
                raise old.formal.CompilationBudgetExceeded("word shuffle expansion term budget")
        return WordExpr(self, terms)

    def integral(self, expression):
        result = self.zero()
        for (local, word), coefficient in expression.terms.items():
            result += self.primitive(local, word).scale(coefficient)
        return result

    def primitive(self, local, word):
        key = (local, word)
        if key in self.primitive_cache:
            return self.primitive_cache[key]
        self.stats["primitive_calls"] += 1
        if self.stats["primitive_calls"] > self.max_calls:
            raise old.formal.CompilationBudgetExceeded("word primitive call budget")
        self.limits.check()
        if key in self.active:
            if not local[1]:
                raise AssertionError("polynomial-letter IBP must strictly shorten the word")
            self.stats["cycle_fallbacks"] += 1
            return self.term(ONE, (local,) + word)
        self.active.add(key)
        try:
            power, jets = local
            answer = None
            if jets and max(jets) >= 1 and jets.count(max(jets)) == 1:
                order = max(jets)
                factors = list(jets)
                factors.remove(order)
                factors.append(order-1)
                antiderivative = (power, tuple(sorted(factors)))
                differential = local_derivative(antiderivative)
                coefficient = differential.pop(local, F(0))
                if coefficient:
                    answer = self.term(antiderivative, word)
                    for remainder, value in differential.items():
                        answer -= self.primitive(remainder, word).scale(value)
                    if word:
                        answer -= self.primitive(local_product(antiderivative, word[0]), word[1:])
                    answer = answer.scale(1/coefficient)
                    self.stats["unique_high_jet_IBP"] += 1
            elif not jets:
                if not word:
                    raise ValueError("I of a pure x-polynomial needs an explicit anchor r; no boundary constant is discarded")
                if power == -1:
                    raise ValueError("logarithmic polynomial-letter antiderivative is outside this declared layer")
                antiderivative = (power+1, ())
                answer = (self.term(antiderivative, word)
                          - self.primitive(local_product(antiderivative, word[0]), word[1:]))
                answer = answer.scale(F(1, power+1))
                self.stats["nonempty_word_polynomial_IBP"] += 1
            if answer is None:
                answer = self.term(ONE, (local,) + word)
            self.primitive_cache[key] = answer
            return answer
        finally:
            self.active.remove(key)

    def atom(self, atom):
        if atom in self.atom_cache:
            return self.atom_cache[atom]
        node = self.ring.p.atoms[atom]
        if node[0] == "jet":
            if node[1] != "q":
                raise ValueError("the pure operator has one ordinary complex profile q")
            answer = self.term((0, (node[2],)))
        elif node[0] == "int_right":
            answer = self.integral(self.monomial(node[1]))
        else:
            raise AssertionError(node)
        self.atom_cache[atom] = answer
        return answer

    def monomial(self, monomial):
        if monomial in self.monomial_cache:
            return self.monomial_cache[monomial]
        answer = self.term((monomial[0], ()))
        for atom in monomial[1]:
            answer = self.multiply(answer, self.atom(atom))
        self.monomial_cache[monomial] = answer
        return answer

    def expression(self, expression):
        if expression.ring is not self.ring:
            raise ValueError("different profile or right anchor")
        result = self.zero()
        for monomial, coefficient in expression.terms.items():
            result += self.monomial(monomial).scale(coefficient)
        return result

    def to_old_local(self, monomial):
        factors = []
        for order in monomial[1]:
            factors.extend(self.ring.p.jet("q", order)[1])
        return self.ring.monomial((monomial[0], tuple(sorted(factors))))

    def to_old_word(self, word):
        if word in self.to_old_word_cache:
            return self.to_old_word_cache[word]
        if not word:
            answer = self.ring.number(1)
        else:
            answer = (self.to_old_local(word[0])*self.to_old_word(word[1:])).I()
        self.to_old_word_cache[word] = answer
        return answer

    def to_old(self, expression):
        answer = self.ring.number(0)
        for (local, word), coefficient in expression.terms.items():
            answer += coefficient*self.to_old_local(local)*self.to_old_word(word)
        return answer

    def summary(self, expression):
        return {"terms": len(expression.terms), "sha256": expression.digest(),
                "max_word_length": max((len(w) for _, w in expression.terms), default=0),
                "max_local_jet_order": max((j for (l, w) in expression.terms
                                              for piece in (l,)+w for j in piece[1]), default=0)}


def word_span(columns, target, limits):
    """Exact representative span, retaining all null relations as certificates."""
    basis = {}
    independent, null_relations = [], []
    for index, column in enumerate(columns):
        vec, representation = dict(column.terms), {index: F(1)}
        while vec:
            limits.check()
            pivot = min(vec)
            if pivot not in basis:
                factor = vec[pivot]
                vec = {m: limits.rational(v/factor) for m, v in vec.items()}
                representation = {j: limits.rational(v/factor) for j, v in representation.items()}
                basis[pivot] = (vec, representation)
                independent.append(index)
                break
            other, rep = basis[pivot]
            factor = vec[pivot]
            for m, value in other.items():
                add_term(vec, m, limits.rational(-factor*value))
                if m in vec:
                    vec[m] = limits.rational(vec[m])
            for j, value in rep.items():
                add_term(representation, j, limits.rational(-factor*value))
                if j in representation:
                    representation[j] = limits.rational(representation[j])
        if not vec:
            null_relations.append(representation)
    vec = dict(target.terms)
    coefficients = {}
    # Reduce every available pivot, retaining unmatched rows. The old helper
    # stopped at the first unmatched pivot. This does not change membership,
    # but a fully reduced residual is much easier to inspect on paper.
    for pivot in sorted(basis):
        if pivot not in vec:
            continue
        other, rep = basis[pivot]
        factor = vec[pivot]
        for m, value in other.items():
            add_term(vec, m, limits.rational(-factor*value))
            if m in vec:
                vec[m] = limits.rational(vec[m])
        for j, value in rep.items():
            add_term(coefficients, j, limits.rational(factor*value))
            if j in coefficients:
                coefficients[j] = limits.rational(coefficients[j])
    return coefficients, WordExpr(target.owner, vec), independent, null_relations


def dependency_record():
    path = Path(old.__file__)
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_PRODUCER_SHA256:
        raise RuntimeError("frozen original pure producer changed; bind a new dependency explicitly")
    return {"original_producer": {"filename": path.name, "bytes": len(data), "sha256": digest},
            "formal_compiler": old.compiler_dependency()}


def coefficient_rows(coefficients, pairs):
    return [{"column": index, "pair": [old.PARAMETERS[i] for i in pairs[index]],
             "coefficient": str(coefficient)}
            for index, coefficient in sorted(coefficients.items()) if coefficient]


def readable_export(owner, expressions, coefficients, pairs):
    """Finite shared word DAG for paper inspection, not a sampled profile."""
    words = set()
    for expression in expressions.values():
        for _, word in expression.terms:
            for start in range(len(word)):
                words.add(word[start:])
    ordered = sorted(words, key=lambda word: (len(word), word))
    names = {word: "W%s" % (i+1) for i, word in enumerate(ordered)}
    definitions = [{"name": names[word], "letter": local_text(word[0]),
                    "inner": names.get(word[1:], "1"),
                    "definition": "I(letter*inner)"} for word in ordered]
    reports = {}
    for name, expression in expressions.items():
        reports[name] = {
            "sha256": expression.digest(), "total_terms": len(expression.terms),
            "rows": [{"coefficient": str(value), "local": local_text(local),
                       "word": names.get(word, "1")}
                      for (local, word), value in sorted(expression.terms.items())],
        }
    payload = {
        "schema": SCHEMA+"-readable-expressions",
        "definition": "qj=d^j q/dx^j; I(f)(x)=integral_r^x f; ordinary complex products",
        "right_boundary": "q is zero on a common open right collar; no left-tail reset",
        "normal_form_complete": False,
        "relation": "remainder = -target - sum(elimination_coefficient[column]*response[column])",
        "elimination_coefficients": coefficient_rows(coefficients, pairs),
        "word_definitions": definitions,
        "expressions": reports,
        "all_expression_rows_included": True,
    }
    data = json.dumps(payload, indent=2, sort_keys=True)+"\n"
    if len(data.encode()) >= 95000:
        # Keep the explanatory output readable without hiding that it is only
        # an excerpt. The exact entire expression is regenerated by this file.
        payload["all_expression_rows_included"] = False
        payload["omission_reason"] = "95 KB readable-expression cap; full exact hashes and generation script retained"
        cap = 40
        while True:
            used_words = set()
            for report in reports.values():
                report["rows"] = report["rows"][:cap]
                report["displayed_terms"] = len(report["rows"])
                used_words.update(row["word"] for row in report["rows"] if row["word"] != "1")
            definition_map = {row["name"]: row for row in definitions}
            todo = list(used_words)
            while todo:
                name = todo.pop()
                inner = definition_map[name]["inner"]
                if inner != "1" and inner not in used_words:
                    used_words.add(inner)
                    todo.append(inner)
            payload["word_definitions"] = [row for row in definitions if row["name"] in used_words]
            data = json.dumps(payload, indent=2, sort_keys=True)+"\n"
            if len(data.encode()) < 95000:
                break
            cap //= 2
            if cap < 1:
                raise RuntimeError("readable expression metadata exceeds declared cap")
    return payload, data


def small_word_toys():
    limits = old.Limits(seconds=90, nodes=50000, atoms=12000, terms=15000,
                        rewrites=25000, memory_mib=1024)
    ring = old.Ring(limits)
    n = WordNormalizer(ring, max_calls=30000, max_terms=15000)
    q, x = ring.jet(), ring.x()
    checks = {}

    def zero(label, expression):
        normalized = n.expression(expression)
        if normalized.terms:
            raise AssertionError((label, n.summary(normalized)))
        checks[label] = True

    f, g, h = q, x*q, q*q
    # A primitive times a nested primitive has three, not two, shuffles.
    depth_two = f.I()*(g*h.I()).I()
    shuffled = ((f*(g*h.I()).I()).I() + (g*(f*h.I()).I()).I()
                + (g*(h*f.I()).I()).I())
    missing_old_identity = depth_two-shuffled
    old_form = old.RightIBP(ring).expression(missing_old_identity)
    zero("one_by_two_word_all_three_shuffles", missing_old_identity)
    all_six = ring.number(0)
    for letters in itertools.permutations((f, g, h)):
        value = ring.number(1)
        for letter in reversed(letters):
            value = (letter*value).I()
        all_six += value
    zero("three_primitives_six_shuffles", f.I()*g.I()*h.I()-all_six)
    repeated = ring.number(1)
    for _ in range(4):
        repeated = (q*repeated).I()
    zero("repeated_letters_keep_multiplicity_24", q.I()**4-24*repeated)
    nested = (q*q*q.I()).I()
    zero("IBP_derivative_hits_arbitrary_nested_word",
         (q.D()*nested).I()-q*nested+(q*q*q*q.I()).I())
    nested2 = (q*q.I()).I()
    zero("polynomial_letter_boundary_nonempty_word",
         (x*x*nested2).I()-x**3*nested2/3+(x**3*q*q.I()).I()/3)
    zero("local_high_jet_IBP", (q.D()*q.D().D().D()).I()
         -q.D()*q.D().D()+(q.D().D()**2).I())
    ops = old.operator_basis(ring)
    tau_raw = ops[3](q, ops[4](q, q))-ops[4](q, ops[3](q, q))
    tau0 = (q.D().D()**3).I()/3
    zero("matrix_bracket_tau0_signed_right_anchor", tau_raw-tau0)
    # Derivative of the word reconstruction is checked independently by the
    # old exact profile derivative, not by a second implementation of shuffle.
    sample = depth_two+(x*q.D()*nested).I()
    sample_word = n.expression(sample)
    zero("back_conversion_true_derivative", n.to_old(sample_word).D()-sample.D())
    zero("back_conversion_identity", n.to_old(sample_word)-sample)
    rejected = False
    try:
        n.expression(ring.number(1).I())
    except ValueError as error:
        rejected = "explicit anchor" in str(error)
    checks["pure_polynomial_primitive_does_not_drop_right_boundary"] = rejected
    if not rejected:
        raise AssertionError("a pure polynomial integral lost its right anchor")
    # Small representative elimination covers a nonpivot row preceding a
    # later eliminable pivot, and an exact dependent-column certificate.
    a, b, c = n.term((0, (0,))), n.term((0, (1,))), n.term((0, (2,)))
    coeff, remainder, independent, nulls = word_span([b, b.scale(2), c], -a-b-c, limits)
    checks["full_span_reduction_keeps_unmatched_rows"] = remainder.terms == (-a).terms
    checks["span_null_relation_saved"] = len(nulls) == 1 and len(independent) == 2
    checks["span_exact_reconstruction"] = (-a-b-c-remainder-b.scale(coeff.get(0, 0))
                                           -b.scale(2*coeff.get(1, 0))-c.scale(coeff.get(2, 0))).terms == {}
    if not all(checks.values()):
        raise AssertionError("a small signed-right word identity failed")
    return {"checks": checks, "known_zero_missed_by_old_layer_terms": len(old_form.terms),
            "word_statistics": n.stats,
            "profile_or_geometry_integrals_evaluated": False,
            "scope": "small exact formal identities only; no research target compiled"}


def run_research(args, payload):
    limits = old.Limits(args.max_seconds, args.max_coefficient_nodes, args.max_profile_atoms,
                        args.max_terms, args.max_IBP_calls, args.max_memory_mib, args.max_rational_bits)
    ring = old.Ring(limits)
    legacy = old.RightIBP(ring)
    normalizer = WordNormalizer(ring, max_calls=args.max_IBP_calls, max_terms=args.max_terms)
    payload["phase"] = "compile_unchanged_true_reciprocal_target"
    target_raw, _ = old.compile_reciprocal_target(ring)
    target_legacy = legacy.expression(target_raw)
    target = normalizer.expression(target_legacy)
    payload["target"] = {"raw_terms": len(target_raw.terms), "raw_sha256": ring.digest(target_raw),
                         "legacy_terms": len(target_legacy.terms), "word": normalizer.summary(target)}
    payload["phase"] = "compile_28_original_commutators"
    q = ring.jet()
    operators = old.operator_basis(ring)
    A = old.positive_constant_operator(ring)
    a = A(q, q)
    pairs = list(itertools.combinations(range(8), 2))
    columns, original_taus, summaries = [], [], []
    for i, j in pairs:
        original_tau = operators[i](q, operators[j](q, q))-operators[j](q, operators[i](q, q))
        tau = normalizer.expression(legacy.expression(original_tau))
        rewritten_tau = normalizer.to_old(tau)
        response_raw = (ring.variation(rewritten_tau, a)-2*A(q, rewritten_tau))/8
        column = normalizer.expression(legacy.expression(response_raw))
        columns.append(column)
        original_taus.append(original_tau)
        summaries.append({"pair": [old.PARAMETERS[i], old.PARAMETERS[j]],
                          "tau": normalizer.summary(tau), "response": normalizer.summary(column)})
    payload["column_summaries"] = summaries
    payload["phase"] = "rational_span_of_word_representatives"
    coefficients, remainder, independent, null_relations = word_span(columns, -target, limits)
    payload["representative_rank"] = len(independent)
    payload["independent_column_indices"] = independent
    payload["span_remainder"] = normalizer.summary(remainder)
    payload["relation_in_word_representatives_found"] = not remainder.terms
    payload["elimination_coefficients"] = coefficient_rows(coefficients, pairs)
    payload["phase"] = "verify_dependencies_from_original_unnormalized_brackets"
    original_responses = {}

    def original_response(index):
        if index not in original_responses:
            tau = original_taus[index]
            original_responses[index] = (ring.variation(tau, a)-2*A(q, tau))/8
        return original_responses[index]

    dependency_certificates = []
    # This is a real positive certificate: after checking all null relations,
    # the displayed rank is an upper bound on the universal function span.
    # It is still not its exact dimension, and does not prove nonmembership.
    for relation in null_relations:
        residual = sum((coefficient*original_response(index) for index, coefficient in relation.items()),
                       ring.number(0))
        fresh_legacy = old.RightIBP(ring)
        fresh_words = WordNormalizer(ring, max_calls=args.max_IBP_calls, max_terms=args.max_terms)
        check = fresh_words.expression(fresh_legacy.expression(residual))
        dependency_certificates.append({"coefficients": coefficient_rows(relation, pairs),
                                        "verified_zero_from_original_brackets": not check.terms,
                                        "residual": fresh_words.summary(check)})
        if check.terms:
            raise AssertionError("a claimed column dependence did not verify from the original expression")
    payload["column_dependency_certificates"] = dependency_certificates
    payload["verified_function_span_dimension_upper_bound"] = len(independent)
    payload["function_span_dimension_equals_upper_bound_proved"] = False
    payload["verified_whole_function_identity"] = False
    if not remainder.terms:
        payload["phase"] = "verify_target_identity_from_original_unnormalized_brackets"
        residual = target_raw
        for index, coefficient in coefficients.items():
            residual += coefficient*original_response(index)
        fresh_legacy = old.RightIBP(ring)
        fresh_words = WordNormalizer(ring, max_calls=args.max_IBP_calls, max_terms=args.max_terms)
        check = fresh_words.expression(fresh_legacy.expression(residual))
        payload["fresh_original_target_residual"] = fresh_words.summary(check)
        payload["verified_whole_function_identity"] = not check.terms
        if check.terms:
            raise AssertionError("the proposed target identity failed fresh original-expression verification")
    export, data = readable_export(normalizer, {"target": target, "remainder": remainder}, coefficients, pairs)
    export_path = args.expressions_out or args.out.with_name(args.out.stem+"-expressions.json")
    export_path.parent.mkdir(parents=True, exist_ok=True)
    export_path.write_text(data, encoding="utf-8")
    payload["readable_expressions"] = {"filename": export_path.name, "bytes": len(data.encode()),
                                       "sha256": hashlib.sha256(data.encode()).hexdigest(),
                                       "all_rows_included": export["all_expression_rows_included"]}
    payload["legacy_statistics"] = legacy.stats
    payload["word_statistics"] = normalizer.stats
    payload["actual_sizes"] = {"coefficient_DAG_nodes": len(ring.algebra.c.nodes),
                                "profile_atoms": len(ring.p.atoms),
                                "history_states": len(ring.algebra.c.state_rhs)}
    payload["completion"] = "complete"
    payload["phase"] = "finished"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--expressions-out", type=Path)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--max-seconds", type=int, default=240)
    parser.add_argument("--max-coefficient-nodes", type=int, default=500000)
    parser.add_argument("--max-profile-atoms", type=int, default=60000)
    parser.add_argument("--max-terms", type=int, default=80000)
    parser.add_argument("--max-IBP-calls", type=int, default=250000)
    parser.add_argument("--max-memory-mib", type=int, default=2048)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    args = parser.parse_args()
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true" and
                                  os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("research compilation only in the named public repository GitHub Actions")
    if any(getattr(args, name) <= 0 for name in (
            "max_seconds", "max_coefficient_nodes", "max_profile_atoms", "max_terms",
            "max_IBP_calls", "max_memory_mib", "max_rational_bits")):
        parser.error("resource bounds must be positive")
    sys.setrecursionlimit(12000)
    started = time.monotonic()
    payload = {
        "schema": SCHEMA,
        "kind": "small_exact_word_toys" if args.toy_only else "bounded_universal_word_span_test",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "github": {key: os.environ.get(key) for key in
                   ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
        "completion": "not_started", "phase": "dependencies_and_small_word_toys",
        "profile_domain": "one arbitrary ordinary-complex smooth q, zero on a common right collar, x in a compact subinterval of (1,infinity)",
        "signed_primitive": "I(f)=integral_r^x f, J=-I; no left-tail value is reset",
        "new_rules": ["full shuffle of words at every depth",
                      "I(D F Iword)=F Iword-I(F D Iword), with right-boundary conditions explicit",
                      "pure x-polynomial front letter removed only when the remaining word is nonempty"],
        "normal_form_complete": False,
        "negative_result_scope": "no function nonmembership or fixed-profile impossibility follows from a nonzero rewritten residual",
        "baseline_true_bridge_T_included": False,
        "full_fourth_range_satisfied": False, "P0_satisfied": False,
        "finite_isometric_family_certified": False, "embedded_closed_surface_certified": False,
        "profile_or_geometry_integrals_evaluated": False,
        "verified_whole_function_identity": False,
        "limits": {name: getattr(args, name) for name in (
            "max_seconds", "max_coefficient_nodes", "max_profile_atoms", "max_terms",
            "max_IBP_calls", "max_memory_mib", "max_rational_bits")},
        "memory_limit_scope": "RSS polling at compiler and word operation sites, not an OS hard cap",
        "rational_bit_limit_scope": "exact rational span elimination",
    }
    code = 0
    try:
        payload["dependencies"] = dependency_record()
        payload["small_word_toys"] = small_word_toys()
        if args.toy_only:
            payload["completion"] = "toy_only"
            payload["phase"] = "finished"
        else:
            run_research(args, payload)
    except old.formal.CompilationBudgetExceeded as error:
        payload["completion"] = "resource_budget_exceeded"
        payload["budget_failure"] = str(error)
        code = 2
    except Exception as error:
        payload["completion"] = "implementation_check_failed"
        payload["error_type"] = type(error).__name__
        payload["error"] = str(error)
        code = 1
    payload["elapsed_seconds"] = time.monotonic()-started
    payload["peak_resident_mib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    output = json.dumps(payload, indent=2, sort_keys=True)+"\n"
    if len(output.encode()) >= 95000:
        raise RuntimeError("word result summary must remain below 95 KB")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(output, encoding="utf-8")
    print(json.dumps({"output": str(args.out), "bytes": len(output.encode()),
                      "sha256": hashlib.sha256(output.encode()).hexdigest(),
                      "completion": payload["completion"],
                      "verified_whole_function_identity": payload["verified_whole_function_identity"]}))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
