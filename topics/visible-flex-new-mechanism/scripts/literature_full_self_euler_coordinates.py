#!/usr/bin/env python3
"""Exact full-self coordinates after R314, with the original right anchor.

This module has no scientific entry point. A caller owns source/input binding
and the public-Actions gate. Only a complete same-color quartic mixed root is
mapped. Original primitives are normalized before the outer zero-collar
restriction; their nested increments and all triangular boundary terms remain.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
import hashlib
import json

import literature_color_priority_words as priority

SCHEMA = "visible-flex-full-self-Euler-coordinates-v1"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def add(out, key, value):
    value = out.get(key, F(0)) + F(value)
    if value:
        out[key] = value
    else:
        out.pop(key, None)


def checked(poly, limits):
    if len(poly) > limits.formal.max_terms:
        raise priority.exact.formal.CompilationBudgetExceeded("finite local coordinate term ceiling")
    for key, value in poly.items():
        power, jets = key
        if (type(power) is not int or power < 0
            or tuple(jets) != tuple(sorted(jets))
            or any(type(j) is not int or j < 0 for j in jets)):
            raise ValueError("invalid finite local jet monomial")
        limits.rational(value)
    limits.check()
    return poly


def derivative(poly, limits):
    out = {}
    for (power, jets), value in sorted(poly.items()):
        if power:
            add(out, (power-1, jets), power*value)
        for order, count in Counter(jets).items():
            tail = list(jets)
            tail.remove(order)
            tail.append(order+1)
            add(out, (power, tuple(sorted(tail))), count*value)
        limits.check()
    return checked(out, limits)


def jet_partial(poly, order, limits):
    out = {}
    for (power, jets), value in sorted(poly.items()):
        count = jets.count(order)
        if count:
            tail = list(jets)
            tail.remove(order)
            add(out, (power, tuple(tail)), count*value)
        limits.check()
    return checked(out, limits)


def euler(poly, limits):
    """The full cubic Euler polynomial, not only its highest-jet symbol."""
    if any(len(jets) != 4 or (jets and max(jets) > 3)
           for power, jets in poly):
        raise ValueError("R314 local input must be quartic and of jet order at most three")
    out = {}
    for order in range(4):
        term = jet_partial(poly, order, limits)
        for _ in range(order):
            term = derivative(term, limits)
        for key, value in term.items():
            add(out, key, (-1 if order % 2 else 1)*value)
    checked(out, limits)
    if any(len(jets) != 3 or (jets and max(jets) > 6) for power, jets in out):
        raise AssertionError("the complete Euler image left its proved finite jet class")
    return out


def local_rows(poly):
    return [[power, list(jets), str(value)]
            for (power, jets), value in sorted(poly.items())]


def word_rows(poly):
    return [[[[power, [[color, order] for color, order in jets]]
              for power, jets in word], str(value)]
            for word, value in sorted(poly.items())]


def plain_letter(letter):
    power, jets = priority.local_key(letter, ("q",))
    if any(color != "q" for color, order in jets):
        raise ValueError("full self requires one real global profile color")
    return power, tuple(order for color, order in jets)


def colored_letter(power, jets):
    return power, tuple(("q", j) for j in jets)


def left_coefficient(word_expression, power, scale=F(1), maximum_power=None):
    """Restrict OUTER jets only, after all original anchored words were formed."""
    out = {}
    for (local, word), value in sorted(word_expression.terms.items()):
        if local[1]:
            continue
        if maximum_power is not None and local[0] > maximum_power:
            raise ValueError("the exact whole left polynomial exceeds its proved degree")
        if local[0] == power:
            add(out, word, scale*value)
    return out


def moment_letters(index):
    if index not in (0, 1, 2):
        raise ValueError("the true second moment index is 0, 1, or 2")
    terms = {colored_letter(index, (2, 2)): F(1)}
    if index == 2:
        terms[colored_letter(0, (1, 1))] = F(2)
    return terms


def matrix_words(matrix):
    """N_A = int_(x<y) j(x)^T A j(y); two raw I signs give +."""
    out = {}
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("the actual ordered matrix has shape three by three")
    for i in range(3):
        for j in range(3):
            for left, a in moment_letters(i).items():
                for right, b in moment_letters(j).items():
                    add(out, (left, right), F(matrix[i][j])*a*b)
    return out


def split_self(words, limits, true_cost_weight=None):
    """Exact identity q=N_T+int L, followed by all Euler coordinates.

    An unexpected word is not deleted and is not a nonmembership decision.
    It is a failed structural interface, with no completed mathematical gate.
    R178 sound IBP has already retained all triangle-diagonal local terms.
    """
    local, bilocal = {}, {}
    for word, value in sorted(words.items()):
        for letter in word:
            if not priority.is_remainder_letter(letter, ("q",)):
                raise ValueError("a self word is outside the fixed remainder grammar")
        if sum(len(letter[1]) for letter in word) != 4:
            raise ValueError("the left self word is not homogeneous quartic")
        if true_cost_weight is not None:
            weight = sum(p-sum(j for c, j in jets)+1 for p, jets in word)
            if weight != true_cost_weight-2:
                raise ValueError("the observed self word has the wrong true scaling weight")
        if len(word) == 1:
            key = plain_letter(word[0])
            if max(key[1], default=0) > 3 or key[1].count(3) > 2:
                raise ValueError("the complete local density exceeds the R314 jet bound")
            # I(a) on the left equals minus the complete ordinary integral.
            add(local, key, -value)
        elif len(word) == 2:
            if any(len(letter[1]) != 2 or max((j for c, j in letter[1]), default=0) > 2
                   for letter in word):
                raise ValueError("a bilocal self letter left the complete quadratic second-jet class")
            add(bilocal, word, value)
        else:
            raise ValueError("the exact self retains a word outside the proved double-integral class")
    matrix = [[bilocal.get((colored_letter(i, (2, 2)),
                            colored_letter(j, (2, 2))), F(0))
               for j in range(3)] for i in range(3)]
    expected = matrix_words(matrix)
    residual = dict(bilocal)
    for key, value in expected.items():
        add(residual, key, -value)
    if residual:
        raise ValueError("the complete bilocal words are not exactly the nine true moment kernels")
    full_euler = euler(local, limits)
    coordinates = {}
    for i in range(3):
        for j in range(3):
            value = matrix[i][j]
            if value:
                if true_cost_weight is not None and i+j-6 != true_cost_weight-2:
                    raise ValueError("ordered matrix entry has the wrong observed true weight")
                coordinates[(0, i, j)] = value
    for (power, jets), value in sorted(full_euler.items()):
        if true_cost_weight is not None and power-sum(jets) != true_cost_weight-3:
            raise ValueError("Euler coefficient has the wrong observed true weight")
        coordinates[(1, power, jets)] = value
    reconstructed = matrix_words(matrix)
    for key, value in local.items():
        add(reconstructed, (colored_letter(key[0], key[1]),), -value)
    if reconstructed != words:
        raise AssertionError("fresh whole word reconstruction from T and L failed")
    return {
        "matrix": matrix, "local": local, "euler": full_euler,
        "coordinates": coordinates, "complete_reconstruction_zero": True,
        "nonlocal_matrix_zero": not any(v for row in matrix for v in row),
        "full_self_function_zero": not coordinates,
    }


def coordinate_label(key):
    if key[0] == 0:
        return ["T", key[1], key[2]]
    if key[0] == 1:
        return ["Euler", key[1], list(key[2])]
    raise ValueError("unknown complete self coordinate")


def coordinate_rows(vector):
    return [[coordinate_label(key), str(value)] for key, value in sorted(vector.items())]


class SelfMapper:
    def __init__(self, ring, max_calls=300000, max_terms=100000, max_cache_entries=250000):
        self.ring = ring
        self.words = priority.PriorityWords(
            ring, max_calls=max_calls, max_terms=max_terms,
            max_shuffle_entries=max_cache_entries, max_cache_entries=max_cache_entries,
            color_order=("q",))

    def expression(self, mixed, true_cost_weight=None):
        self.ring.limits.check()
        diagonal = self.ring.substitute(mixed, {"qbar": self.ring.color("q")})
        if self.ring.color_degrees(diagonal) - {(("q", 4),)}:
            raise ValueError("diagonal of the full mixed root is not real one-color quartic")
        normal = self.words.expression(diagonal)
        for local, word in normal.terms:
            if not all(priority.is_remainder_letter(letter, ("q",)) for letter in word):
                raise ValueError("original conversion left the sound fixed-color grammar")
        # For g=0: V=A+B cos^2(theta)+C cos^4(theta), A+B+C=0.
        # The -2 Fourier root is (B+C)/4=-A/4.
        # Thus q=1/4 [x^2] A = -[x^2] M_{-2}(u,u).
        self_words = left_coefficient(normal, 2, F(-1), maximum_power=2)
        result = split_self(self_words, self.ring.limits, true_cost_weight)
        result.update({
            "original_mixed_sha256": self.ring.digest(mixed),
            "original_mixed_terms": len(mixed.terms),
            "global_diagonal_sha256": self.ring.digest(diagonal),
            "global_diagonal_terms": len(diagonal.terms),
            "whole_word_sha256": priority.digest(priority.rows(normal)),
            "whole_word_terms": len(normal.terms),
            "self_words": self_words,
            "self_word_sha256": sha(canonical(word_rows(self_words))),
            "self_word_terms": len(self_words),
            "local_density_sha256": sha(canonical(local_rows(result["local"]))),
            "Euler_sha256": sha(canonical(local_rows(result["euler"]))),
            "coordinate_sha256": sha(canonical(coordinate_rows(result["coordinates"]))),
            "outer_jets_zero_only_after_full_same_anchor_conversion": True,
            "all_diagonal_triangle_terms_retained": True,
        })
        return result
