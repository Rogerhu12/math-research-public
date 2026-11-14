#!/usr/bin/env python3
"""Colored right-Volterra algebra for unsymmetrized third operators.

This module contains no research entry point.  It extends the frozen pure
algebra without changing it.  Every color has the same zero right collar.
Only exact expression manipulation is performed; the caller owns the public
Actions gate for a genuine research target.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
import hashlib
import json

import literature_pure_bulk_exact_membership as exact
import literature_pure_bulk_word_normal_form as words


class ColoredRing(exact.Ring):
    def __init__(self, limits, algebra=None):
        super().__init__(limits, algebra)
        self.substitution_cache = {}
        self.color_degree_cache = {}

    def color(self, kind, order=0):
        if not isinstance(kind, str) or not kind or order < 0:
            raise ValueError("a color is a nonempty name and a nonnegative jet")
        return self.monomial(self.p.jet(kind, order))

    def substitute(self, expression, replacements):
        """Simultaneous substitution, including every actual right primitive."""
        expression = self.coerce(expression)
        replacements = {kind: self.coerce(value) for kind, value in replacements.items()}
        cache_key = (expression.key(), tuple(sorted((k, v.key()) for k, v in replacements.items())))
        if cache_key in self.substitution_cache:
            return self.substitution_cache[cache_key]
        atoms, monomials = {}, {}
        jets = {kind: {0: value} for kind, value in replacements.items()}

        def jet(kind, order):
            if kind not in replacements:
                return self.color(kind, order)
            while order not in jets[kind]:
                j = max(jets[kind])
                jets[kind][j+1] = jets[kind][j].D()
            return jets[kind][order]

        def atom(index):
            if index not in atoms:
                node = self.p.atoms[index]
                if node[0] == "jet":
                    value = jet(node[1], node[2])
                elif node[0] == "int_right":
                    value = monomial(node[1]).I()
                else:
                    raise AssertionError(node)
                atoms[index] = value
            return atoms[index]

        def monomial(key):
            if key not in monomials:
                value = self.monomial((key[0], ()))
                for index in key[1]:
                    value *= atom(index)
                monomials[key] = value
            return monomials[key]

        result = self.number(0)
        for key, coefficient in expression.terms.items():
            self.limits.check()
            result += coefficient*monomial(key)
        self.substitution_cache[cache_key] = result
        return result

    def atom_color_degree(self, atom):
        if atom not in self.color_degree_cache:
            node = self.p.atoms[atom]
            if node[0] == "jet":
                value = Counter({node[1]: 1})
            else:
                value = Counter()
                for child in node[1][1]:
                    value.update(self.atom_color_degree(child))
            self.color_degree_cache[atom] = value
        return self.color_degree_cache[atom]

    def color_degrees(self, expression):
        result = set()
        for _, atoms in expression.terms:
            value = Counter()
            for atom in atoms:
                value.update(self.atom_color_degree(atom))
            result.add(tuple(sorted(value.items())))
        return result


def colored_local_derivative(monomial):
    power, jets = monomial
    result = {}
    if power:
        words.add_term(result, (power-1, jets), F(power))
    for jet, count in Counter(jets).items():
        remaining = list(jets)
        remaining.remove(jet)
        remaining.append((jet[0], jet[1]+1))
        words.add_term(result, (power, tuple(sorted(remaining))), F(count))
    return result


class ColoredWords(words.WordNormalizer):
    """The same sound shuffle/IBP rules with named, independent jet colors.

    The unique-highest-derivative rule only fires when that derivative order
    occurs once across *all* colors.  A cycle is retained as the exact raw
    word.  No completeness or actual-function independence is asserted.
    """

    def primitive(self, local, word):
        key = (local, word)
        if key in self.primitive_cache:
            return self.primitive_cache[key]
        self.stats["primitive_calls"] += 1
        if self.stats["primitive_calls"] > self.max_calls:
            raise exact.formal.CompilationBudgetExceeded("colored word primitive call budget")
        self.limits.check()
        if key in self.active:
            if not local[1]:
                raise AssertionError("polynomial-letter IBP must shorten the word")
            self.stats["cycle_fallbacks"] += 1
            return self.term(words.ONE, (local,)+word)
        self.active.add(key)
        try:
            power, jets = local
            answer = None
            largest = max((j[1] for j in jets), default=-1)
            hits = [j for j in jets if j[1] == largest]
            if largest >= 1 and len(hits) == 1:
                selected = hits[0]
                factors = list(jets)
                factors.remove(selected)
                factors.append((selected[0], selected[1]-1))
                antiderivative = (power, tuple(sorted(factors)))
                differential = colored_local_derivative(antiderivative)
                coefficient = differential.pop(local, F(0))
                if coefficient:
                    answer = self.term(antiderivative, word)
                    for remainder, value in differential.items():
                        answer -= self.primitive(remainder, word).scale(value)
                    if word:
                        answer -= self.primitive(words.local_product(antiderivative, word[0]), word[1:])
                    answer = answer.scale(1/coefficient)
                    self.stats["unique_high_jet_IBP"] += 1
            elif not jets:
                if not word:
                    raise ValueError("I of a zero-profile polynomial needs its explicit right-end boundary")
                if power == -1:
                    raise ValueError("logarithmic xi primitive is outside the declared layer")
                antiderivative = (power+1, ())
                answer = (self.term(antiderivative, word)
                          - self.primitive(words.local_product(antiderivative, word[0]), word[1:]))
                answer = answer.scale(F(1, power+1))
                self.stats["nonempty_word_polynomial_IBP"] += 1
            if answer is None:
                answer = self.term(words.ONE, (local,)+word)
            self.primitive_cache[key] = answer
            return answer
        finally:
            self.active.remove(key)

    def atom(self, atom):
        if atom not in self.atom_cache:
            node = self.ring.p.atoms[atom]
            if node[0] == "jet":
                value = self.term((0, ((node[1], node[2]),)))
            elif node[0] == "int_right":
                value = self.integral(self.monomial(node[1]))
            else:
                raise AssertionError(node)
            self.atom_cache[atom] = value
        return self.atom_cache[atom]

    def to_old_local(self, monomial):
        factors = []
        for kind, order in monomial[1]:
            factors.extend(self.ring.p.jet(kind, order)[1])
        return self.ring.monomial((monomial[0], tuple(sorted(factors))))

    def summary(self, expression):
        return {"terms": len(expression.terms), "sha256": expression.digest(),
                "max_word_length": max((len(w) for _, w in expression.terms), default=0),
                "max_local_jet_order": max((j[1] for (l, w) in expression.terms
                                            for piece in (l,)+w for j in piece[1]), default=0),
                "colors": sorted({j[0] for (l, w) in expression.terms
                                   for piece in (l,)+w for j in piece[1]})}


class ColoredNormalizer:
    """Adapter returning the original exact Expr after a sound word rewrite."""

    def __init__(self, ring, max_calls=None, max_terms=None):
        self.ring = ring
        self.word = ColoredWords(ring, max_calls=max_calls or ring.limits.max_rewrites,
                                 max_terms=max_terms or ring.limits.formal.max_terms,
                                 max_weight=4)

    def expression(self, expression):
        return self.word.to_old(self.word.expression(expression))


class ThirdOperator:
    """A true exterior color a and symmetric interior colors b,c."""

    def __init__(self, ring, template, label=None):
        self.ring, self.template, self.label = ring, template, label
        allowed = (("a", 1), ("b", 1), ("c", 1))
        if any(degree != allowed for degree in ring.color_degrees(template)):
            raise AssertionError("third template must be trilinear with separate exterior slot")
        self.cache = {}

    def __call__(self, exterior, first, second):
        # The original compiled tensor is symmetric in b,c.  Its identity is
        # checked in the research entry point before this cache is used.
        pair = (first, second) if first.key() <= second.key() else (second, first)
        key = (exterior.key(), pair[0].key(), pair[1].key())
        if key not in self.cache:
            self.cache[key] = self.ring.substitute(self.template,
                                                  {"a": exterior, "b": pair[0], "c": pair[1]})
        return self.cache[key]


def full_phase_response(ring, third):
    """R78: one same third control applied simultaneously to modes -4,-2."""
    A = exact.positive_constant_operator(ring)
    q, qb = ring.color("q"), ring.color("qbar")
    f = (q+qb)/2
    q2 = ((F(1), q, q),)
    d = ((F(1, 2), q, q), (F(1, 2), qb, qb))
    target = ((F(1), f, f),)

    def apply_a(D):
        return sum((value*A(x, y) for value, x, y in D), ring.number(0))

    def apply_t(exterior, D):
        return sum((value*third(exterior, x, y) for value, x, y in D), ring.number(0))

    def K(D1, D2):
        return apply_t(apply_a(D1), D2)+apply_t(apply_a(D2), D1)

    def L(E, D):
        aD = apply_a(D)
        answer = ring.number(0)
        for value, x, y in E:
            answer += value*(-2*third(x, y, aD)-2*third(y, x, aD)
                             +2*A(x, apply_t(y, D))+2*A(y, apply_t(x, D)))
        return answer

    return {-4: (K(q2, q2)-L(q2, q2))/16,
            -2: -(L(target, q2)+K(d, q2)-(L(d, q2)+L(q2, d))/2)/4}


def vector_from_modes(modes, normalizer):
    result = {}
    for mode, expression in sorted(modes.items()):
        value = normalizer.word.expression(expression)
        for (monomial, word), coefficient in value.terms.items():
            result[(mode, monomial, word)] = coefficient
    return result


def vector_digest(vector):
    rows = [[mode, monomial, word, str(coefficient)]
            for (mode, monomial, word), coefficient in sorted(vector.items())]
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


class JointSpan:
    """Exact joint rational elimination, with one coefficient for both modes."""

    def __init__(self, columns, limits):
        self.limits, self.basis, self.independent = limits, {}, []
        self.column_count = len(columns)
        for index, column in enumerate(columns):
            value, representation = dict(column), {index: F(1)}
            while value:
                self.limits.check()
                pivot = min(value)
                if pivot not in self.basis:
                    scale = value[pivot]
                    value = {key: limits.rational(c/scale) for key, c in value.items()}
                    representation = {key: limits.rational(c/scale) for key, c in representation.items()}
                    self.basis[pivot] = (value, representation)
                    self.independent.append(index)
                    break
                row, rep = self.basis[pivot]
                scale = value[pivot]
                self.subtract(value, row, scale)
                self.subtract(representation, rep, scale)

    def subtract(self, target, source, factor):
        for key, value in source.items():
            words.add_term(target, key, self.limits.rational(-factor*value))
            if key in target:
                target[key] = self.limits.rational(target[key])
        self.limits.check()

    def reduce(self, target):
        residual, coefficients = dict(target), {}
        for pivot in sorted(self.basis):
            if pivot not in residual:
                continue
            row, rep = self.basis[pivot]
            factor = residual[pivot]
            self.subtract(residual, row, factor)
            for index, value in rep.items():
                words.add_term(coefficients, index, self.limits.rational(factor*value))
        return coefficients, residual

    def summary(self):
        return {"columns": self.column_count, "representative_rank": len(self.independent),
                "independent_indices": self.independent,
                "actual_function_independence_claimed": False}


def small_colored_toys():
    limits = exact.Limits(seconds=90, nodes=50000, atoms=20000, terms=20000,
                          rewrites=100000, memory_mib=512)
    ring = ColoredRing(limits)
    norm = ColoredNormalizer(ring)
    a, b, c, q, x = (ring.color(k) for k in ("a", "b", "c", "q", "x_dummy"))
    checks = {}

    def zero(expr, name):
        if norm.expression(expr).terms:
            raise AssertionError(name)
        checks[name] = True

    zero((a.D()*b+a*b.D()).I()-a*b, "colored_product_IBP_with_zero_right_boundary")
    zero(a.I()*(b*c.I()).I()
         -(a*(b*c.I()).I()).I()-(b*(a*c.I()).I()).I()-(b*(c*a.I()).I()).I(),
         "all_depth_three_colored_shuffle")
    sample = (a*b.D()).I()+a.D()*b*c
    replacements = {"a": q+q.D(), "b": q*q, "c": q.D()}
    zero(ring.substitute(sample.D(), replacements)-ring.substitute(sample, replacements).D(),
         "simultaneous_substitution_commutes_with_derivative")
    zero(ring.substitute(sample.I(), replacements)-ring.substitute(sample, replacements).I(),
         "simultaneous_substitution_keeps_exact_right_anchor")
    lost_slot = a.D()*b*c-a*(b.D()*c+b*c.D())/2
    zero(ring.substitute(lost_slot, {"a": q, "b": q, "c": q}),
         "nonzero_unsymmetrized_template_can_have_zero_diagonal")
    if not lost_slot.terms:
        raise AssertionError("outer-slot toy collapsed")
    checks["exterior_slot_not_recovered_from_diagonal"] = True
    fresh = ColoredNormalizer(ring)
    zero(fresh.expression(sample)-sample, "word_to_expression_semantics")
    # A joint coefficient must work in both channels; no mode-wise fitting.
    joint = JointSpan([{(-4, words.ONE, ()): F(1), (-2, words.ONE, ()): F(2)}], limits)
    coefficients, residual = joint.reduce({(-4, words.ONE, ()): F(3), (-2, words.ONE, ()): F(6)})
    if residual or coefficients != {0: F(3)}:
        raise AssertionError("joint channel coefficient")
    _, residual = joint.reduce({(-4, words.ONE, ()): F(3), (-2, words.ONE, ()): F(7)})
    if not residual:
        raise AssertionError("independent channel coefficients were silently admitted")
    checks["same_control_coefficient_across_both_modes"] = True
    return {"scope": "small artificial colored algebra only; no target compiler or profile values",
            "checks": checks, "all_passed": all(checks.values()),
            "profile_atoms": len(ring.p.atoms), "word_statistics": norm.word.stats}
