#!/usr/bin/env python3
"""R483 complete coast Bernstein ranges for an already bound accurate ten target.

This library changes interval evaluation only.  It never creates a factory
result, modifies an original module/target, selects a C root, runs a BVP,
or turns an original factory-domain flag into a completed certificate.
Callers retain their original clock, all closed pieces, strict predicates,
full field/material dimensions, output limit, and partial-result policy.
Scientific arithmetic is restricted to the named public Actions.
"""
from __future__ import annotations

from collections import OrderedDict
import copy
from fractions import Fraction as Q
import hashlib
import json
from math import comb
import os
from pathlib import Path
import sys

REPOSITORY = "Rogerhu12/math-research-public"
SCHEMA = "R483-complete-ten-coast-Bernstein-range-adapter-v1"
FACTORY_NAME = "geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py"
FACTORY_SHA = "72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682"
COAST_NAME = "negative-speed-coast"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("Accurate coast arithmetic belongs only to the named public Actions")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False) + "\n").encode()


def receipt(path):
    path = Path(path)
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for raw in iter(lambda: stream.read(1048576), b""):
            h.update(raw)
            size += len(raw)
    return dict(file=path.name, bytes=size, sha256=h.hexdigest())


def value_identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=hashlib.sha256(raw).hexdigest())


def affine_coefficients(coefficients, left, width, degree):
    """All power coefficients of p(left+width*x), including zero high slots."""
    if len(coefficients) > degree + 1:
        raise ValueError("The complete polynomial exceeds its declared degree")
    out = [Q(0)] * (degree + 1)
    for j, value in enumerate(coefficients):
        for k in range(j + 1):
            out[k] += value * comb(j, k) * left**(j-k) * width**k
    return out


def bernstein_coefficients(coefficients, left, right, degree):
    power = affine_coefficients(coefficients, left, right-left, degree)
    return [sum((power[k] * Q(comb(j, k), comb(degree, k))
                 for k in range(j + 1)), Q(0))
            for j in range(degree + 1)]


def _literal_constant(nodes, index):
    # This is a structural source check, not evaluation of a free expression.
    if type(index) is not int or not 0 <= index < len(nodes):
        return None
    row = nodes[index]
    if row.get("op") == "rational":
        return Q(row["value"])
    if (row.get("op") == "neg" and len(row.get("args", [])) == 1
            and type(row["args"][0]) is int and 0 <= row["args"][0] < index):
        value = nodes[row["args"][0]]
        if value.get("op") == "rational":
            return -Q(value["value"])
    return None


def coast_context(Factory, model, values, piece, include_controls):
    """Return the proved local formula context, or retain the original path.

    An unrecognised structural form falls back to Factory.piece_range.  It
    does not become a new scientific rejection or an omitted control term.
    No original value, object, global, or source is modified.
    """
    if piece.get("name") != COAST_NAME:
        return None, "original_noncoast_piece"
    if (model.get("control_terms") != Factory.CONTROL_TERMS
            or len(model.get("parameters", [])) != 10
            or len(model.get("supports", [])) != 3
            or len(piece.get("coefficients", [])) != 2
            or list(map(Q, piece.get("local_interval", []))) != [Q(0), Q(1)]):
        return None, "original_coast_structural_contract_not_selected"
    supports = model["supports"]
    if (piece.get("anchor") != supports[2].get("left")
            or piece.get("width") != supports[2].get("width")
            or piece.get("width") != model["roots"].get("coast_length")):
        return None, "original_coast_shared_indices_not_selected"
    nodes = model["tree"].nodes
    index = piece["coefficients"][1]
    if type(index) is not int or not 0 <= index < len(nodes):
        return None, "original_coast_linear_index_not_selected"
    row = nodes[index]
    args = row.get("args", [])
    if row.get("op") != "mul" or len(args) != 2:
        return None, "original_coast_linear_expression_not_selected"
    width_index = piece["width"]
    if args[0] == width_index:
        coefficient = _literal_constant(nodes, args[1])
    elif args[1] == width_index:
        coefficient = _literal_constant(nodes, args[0])
    else:
        coefficient = None
    if coefficient is None or not -1 < coefficient < 0:
        return None, "original_coast_fixed_kappa_not_selected"
    width = values[width_index]
    anchor = values[piece["anchor"]]
    if width.lo <= 0:
        # The original function remains responsible for its original error.
        return None, "original_coast_positive_width_responsibility"
    for support in supports[:2]:
        support_left = values[support["left"]]
        support_width = values[support["width"]]
        if support_width.lo <= 0:
            return None, "original_other_support_width_responsibility"
        if (support_left + support_width).hi > anchor.lo:
            return None, "original_other_support_not_proved_outside_coast"
    polynomial = [Q(0)] * 9
    selected_terms = []
    excluded_terms = []
    for item in Factory.CONTROL_TERMS:
        support_index = item["support_index"]
        if support_index == 2:
            if item["power"] not in (0, 1, 2):
                return None, "original_coast_degree_contract_not_selected"
            index = item["parameter_index"]
            selected_terms.append(copy.deepcopy(item))
            if include_controls:
                bump = Factory.bump_polynomial(item["power"])
                parameter = Q(model["parameters"][index])
                for j, value in enumerate(bump):
                    polynomial[j] += parameter * value
        elif support_index in (0, 1):
            excluded_terms.append(copy.deepcopy(item))
        else:
            return None, "original_control_support_contract_not_selected"
    if (len(selected_terms) != 3
            or sorted(item["parameter_index"] for item in selected_terms) != [2, 5, 8]
            or len(excluded_terms) != 7):
        return None, "original_complete_ten_term_partition_not_selected"
    kappa = -coefficient
    return dict(
        A=values[piece["coefficients"][0]],
        width=width, kappa=kappa, polynomial=polynomial,
        complete_control_terms=copy.deepcopy(Factory.CONTROL_TERMS),
        coast_terms=selected_terms, outside_terms=excluded_terms,
        include_controls=bool(include_controls)), None


def complete_coast_range(Factory, context, local):
    """Full radius/physical first/second jet on the whole width x local box."""
    Box = Factory.Box
    width, kappa, p = context["width"], context["kappa"], context["polynomial"]
    l0, lh = width.lo, width.hi-width.lo
    t0, th = local.lo, local.hi-local.lo
    px = affine_coefficients(p, t0, th, 8)
    powers = [[Box(0) for _ in range(9)] for _ in range(3)]
    powers[0][0] = Box(context["A"].lo, context["A"].hi)
    powers[0][0] += -kappa*l0*t0
    powers[0][1] += -kappa*l0*th
    powers[1][0] += -kappa*lh*t0
    powers[1][1] += -kappa*lh*th
    ell_squared = (l0*l0, 2*l0*lh, lh*lh)
    for r in range(3):
        for s in range(9):
            powers[r][s] += ell_squared[r]*px[s]
    radius_coefficients = []
    for i in range(3):
        for j in range(9):
            beta = Box(0)
            for r in range(i + 1):
                for s in range(j + 1):
                    beta += powers[r][s] * Q(comb(i, r), comb(2, r)) * Q(comb(j, s), comb(8, s))
            radius_coefficients.append(beta)
    radius = Box(min(x.lo for x in radius_coefficients),
                 max(x.hi for x in radius_coefficients))
    first = Factory.differentiated(p, 1)
    speed_coefficients = []
    for ell in (width.lo, width.hi):
        speed = [ell*x for x in first]
        speed[0] -= kappa
        speed_coefficients.extend(bernstein_coefficients(speed, local.lo, local.hi, 7))
    speed = Box(min(speed_coefficients), max(speed_coefficients))
    second = Factory.differentiated(p, 2)
    curvature_coefficients = bernstein_coefficients(second, local.lo, local.hi, 6)
    second = Box(min(curvature_coefficients), max(curvature_coefficients))
    return [radius, speed, second]


def piece_range(Factory, model, values, piece, local, include_controls, *, context=None):
    """The complete old range contract with one explicit exact-coast branch."""
    require_actions()
    if context is None:
        context, reason = coast_context(Factory, model, values, piece, include_controls)
    else:
        reason = None
    if context is None or not 0 <= local.lo <= local.hi <= 1:
        return Factory.piece_range(model, values, piece, local, include_controls), dict(
            method="original72c_complete_piece_range",
            original_factory_sha256=FACTORY_SHA,
            reason=reason or "original_local_interval_outside_proved_coast_contract",
            complete_ten_controls_retained=True)
    jets = complete_coast_range(Factory, context, local)
    return jets, dict(method=SCHEMA,
        formula="a=A-kappa*ell*t+ell^2*P; a_s=-kappa+ell*P'; a_ss=P''",
        physical_derivative_coordinate="s_true",
        exact_kappa=str(context["kappa"]), complete_width_box=context["width"].record(),
        radius_bidegree=[2, 8], radius_Bernstein_coefficients=27,
        speed_endpoint_polynomials=2, speed_Bernstein_coefficients_per_endpoint=8,
        second_derivative_Bernstein_coefficients=7,
        complete_ten_control_count=10,
        coast_control_indices=[2, 5, 8],
        other_seven_controls_zero_here_by_complete_true_support_and_zero_two_jets=True,
        closed_width_and_local_endpoints_retained=True,
        no_width_samples_or_corner_only_radius_test=True,
        include_controls=bool(include_controls),
        original_scalar_strict_predicate_not_changed=True,
        this_range_is_not_a_factory_global_domain_certificate=True)


class CoastTargetRange:
    """Explicit range adapter; the original bound target is never mutated.

    The inherited target identity describes the same accurate mathematical
    object.  describe() separately records this interval implementation.
    Callers pass this adapter as a local argument to original Prefix.inspect,
    or call its closed_range explicitly.  They do not replace current.target.
    """
    def __init__(self, original):
        require_actions()
        self.original = original
        Factory = original.Factory
        actual_factory = receipt(Factory.__file__)
        if (Path(Factory.__file__).name != FACTORY_NAME
                or actual_factory["sha256"] != FACTORY_SHA
                or original.definition.get("source_sha256") != FACTORY_SHA
                or original.definition.get("schema") != Factory.MODEL_SCHEMA
                or original.model.get("control_terms") != Factory.CONTROL_TERMS
                or len(original.parameters) != 10):
            raise ValueError("Bind the original complete72c accurate ten definition and actual target")
        module = sys.modules.get(type(original).__module__)
        filename = getattr(module, "__file__", None)
        if filename is None:
            raise ValueError("Retain the actually loaded accurate-target implementation identity")
        self.base_target_source = receipt(filename)
        self.base_factory = actual_factory
        self.source = receipt(__file__)
        self.cache = OrderedDict()
        self.contexts = {}
        self.context_scope = []
        for index, piece in enumerate(original.pieces):
            if piece.get("name") != COAST_NAME:
                continue
            context, reason = coast_context(Factory, original.model, original.values, piece, True)
            self.contexts[index] = context
            self.context_scope.append(dict(piece_index=index, name=piece["name"],
                shared_coast_formula_selected=context is not None,
                fallback_reason=reason,
                original_piece_identity=value_identity(piece)))
        self.counters = dict(closed_queries_started=0, closed_queries_completed=0,
            cache_hits=0, complete_piece_candidates=0, coast_formula_candidates=0,
            original_factory_candidates=0)
        self.last_query = None

    def __getattr__(self, name):
        return getattr(self.original, name)

    def describe(self):
        return dict(schema=SCHEMA+"-binding", source=copy.deepcopy(self.source),
            original_factory=copy.deepcopy(self.base_factory),
            actual_original_target_implementation=copy.deepcopy(self.base_target_source),
            original_complete_target_binding_identity=value_identity(self.original.binding),
            original_complete_accurate_definition=copy.deepcopy(
                self.original.binding["complete_accurate_definition"]),
            original_complete_C_input_binding_identity=value_identity(
                self.original.binding["complete_original_C_input_binding"]),
            complete_ten_exact_values=[str(Q(x)) for x in self.original.parameters],
            complete_piece_count=len(self.original.pieces),
            complete_support_count=len(self.original.supports),
            coast_branch_bindings=copy.deepcopy(self.context_scope),
            original_definition_profile_compiler_and_field_not_modified=True,
            original_factory_initial_domain_flags_not_replaced=True,
            same_semantic_C_leaves_and_allowed_root_family=True,
            original_numeric_and_true_lengths_not_identified=True,
            all_possible_accurate_pieces_and_closed_endpoints_retained=True,
            original_prefix_strict_metric_tests_unchanged=True,
            global_scalar_domain_native_BVP_or_metric_success_not_inferred=True,
            owns_no_new_budget_clock_or_acceptance_gate=True)

    def status(self):
        return dict(schema=SCHEMA+"-actual-range-work",
            counters=copy.deepcopy(self.counters), last_query=copy.deepcopy(self.last_query),
            cache_capacity=64, completed_cache_entries=len(self.cache),
            query_counts_do_not_certify_whole_domain_or_all_parameters=True)

    def closed_range(self, left, right):
        require_actions()
        original = self.original
        key = (left, right)
        self.counters["closed_queries_started"] += 1
        self.last_query = dict(numeric_coordinate=[str(left), str(right)], completed=False)
        if key in self.cache:
            self.cache.move_to_end(key)
            self.counters["cache_hits"] += 1
            self.counters["closed_queries_completed"] += 1
            self.last_query["completed"] = True
            self.last_query["used_existing_complete_query"] = True
            return self.cache[key]
        if not 0 <= left <= right <= original.numeric_length:
            raise ValueError("Use an actual complete prefix subinterval")
        F = original.Factory
        Box = F.Box
        public = Box(left/original.numeric_length, right/original.numeric_length)
        radial = original.length*public
        jets = None
        candidates = []
        for index, piece in enumerate(original.pieces):
            anchor, width = original.values[piece["anchor"]], original.values[piece["width"]]
            t = (radial-anchor)/width
            own_left, own_right = map(Q, piece["local_interval"])
            lo, hi = max(t.lo, own_left), min(t.hi, own_right)
            if lo > hi:
                continue
            local = Box(lo, hi)
            row, scope = piece_range(F, original.model, original.values, piece, local, True,
                                    context=self.contexts.get(index))
            self.counters["complete_piece_candidates"] += 1
            self.counters["coast_formula_candidates" if scope["method"] == SCHEMA
                          else "original_factory_candidates"] += 1
            jets = list(row) if jets is None else [a.hull(b) for a, b in zip(jets, row)]
            candidates.append(dict(index=index, name=piece["name"],
                complete_closed_local_interval=local.record(),
                accurate_radius_first_second=[x.record() for x in row],
                actual_range_implementation=scope))
        if jets is None:
            raise ArithmeticError("No complete accurate piece enclosure covers this public-u box")
        scale = original.length/Box(original.numeric_length)
        report = dict(schema=SCHEMA+"-closed-target-cell",
            original_target_implementation=copy.deepcopy(self.base_target_source),
            interval_range_source_sha256=self.source["sha256"],
            numerical_coordinate=[str(left), str(right)], public_u=public.record(),
            same_true_radial_coordinate=radial.record(), all_possible_accurate_pieces=candidates,
            every_original_accurate_piece_examined=len(original.pieces),
            selected_candidate_count=len(candidates),
            accurate_radius_first_second=[x.record() for x in jets],
            radial_metric=(scale*scale).record(),
            closed_endpoints_and_all_support_cases_included=True,
            no_finite_angle_bandwidth_or_sample_selection=True,
            parameter_count=10, all_control_terms_retained=True,
            piece_union_is_conservative_not_a_common_midpoint_choice=True,
            original_factory_initial_domain_certificate_not_rewritten=True)
        result = (jets, scale*scale, report)
        self.cache[key] = result
        while len(self.cache) > 64:
            self.cache.popitem(last=False)
        self.counters["closed_queries_completed"] += 1
        self.last_query["completed"] = True
        self.last_query["used_existing_complete_query"] = False
        return result

