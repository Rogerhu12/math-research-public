#!/usr/bin/env python3
"""Bounded, resumable exact membership blocks for all-state universal P1.

The seven-dimensional physical quadratic space is split by true affine
scaling weight.  No mixed 72/252-column target is compiled.  Each completed
block is saved independently before the next block starts.  Real research
compilation/evaluation is restricted to the public repository's Actions.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import combinations
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


SCHEMA = "visible-flex-total-universal-P1-scaling-blocks-v1"
BLOCK_SCHEMA = SCHEMA+"-block"
DUAL_SHA = "bcfb26b85918a8648ad98bbde7643c4cf6d01d34b35c53bc06c3dbaff31de84f"
POLY_SHA = "6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22"
PARAMETER_WEIGHTS = (-1, 0, 1, -3, -2, -2, -1, 0)
THIRD_WEIGHTS = tuple(PARAMETER_WEIGHTS[i]+PARAMETER_WEIGHTS[j]
                      for i, j in combinations(range(8), 2))+(-4, -3, -3, -2, -1, -2, -1, 0)
EXPECTED_KEPT = list(range(28))+[30, 32, 34, 37, 40, 100, 104, 109]


def unit(index):
    return tuple(F(int(i == index)) for i in range(8))


E_BASIS = (
    ("r0", -3, unit(3)), ("r1", -2, unit(4)), ("s0", -2, unit(5)),
    ("p0", -1, unit(0)), ("s1", -1, unit(6)),
    ("p1_minus_t1_over_4", 0, (F(0), F(1), F(0), F(0), F(0), F(0), F(0), F(-1, 4))),
    ("p2", 1, unit(2)),
)
STANDARD_PARTS = {0: F(-1, 8), 3: F(-1, 2), 6: F(-1, 2)}
EXPECTED_BLOCK_COLUMNS = dict(zip(range(-8, 3), (2, 8, 20, 34, 46, 48, 42, 28, 16, 6, 2)))
PAID = {"target_zero_verified", "member_identity_verified"}
TOTAL_PUBLISHED_BYTES = 4500000


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def dependencies():
    data = dual.dependencies()
    if data["driver"]["sha256"] != DUAL_SHA or data["polynomial_evaluator"]["sha256"] != POLY_SHA:
        raise ValueError("explicitly rebind changed original-formula/evaluation sources")
    data["original_problem_driver"] = data.pop("driver")
    data["driver"] = dual.file_identity(__file__)
    return data


class ScalingGrading:
    """True pullback weight: xi +1, jet_j -j, right primitive +1."""
    def __init__(self, ring):
        self.ring, self.atoms, self.monomials = ring, {}, {}

    def atom(self, identifier):
        if identifier not in self.atoms:
            node = self.ring.p.atoms[identifier]
            if node[0] == "jet":
                value = -node[2]
            elif node[0] == "int_right":
                value = 1+self.monomial(node[1])
            else:
                raise ValueError("unsupported original atom in scaling projection")
            self.atoms[identifier] = value
        return self.atoms[identifier]

    def monomial(self, value):
        if value not in self.monomials:
            self.monomials[value] = value[0]+sum(self.atom(a) for a in value[1])
        return self.monomials[value]

    def split(self, expression):
        pieces = {}
        for monomial, coefficient in expression.terms.items():
            pieces.setdefault(self.monomial(monomial), {})[monomial] = coefficient
        return {weight: exact.Expr(self.ring, terms) for weight, terms in pieces.items()}

    def project(self, expression, weight):
        return exact.Expr(self.ring, {m: c for m, c in expression.terms.items()
                                     if self.monomial(m) == weight})

    def inventory(self, expression):
        return {str(n): {"raw_terms": len(value.terms), "original_sha256": self.ring.digest(value)}
                for n, value in sorted(self.split(expression).items())}


def full_response(ring, third, quadratic):
    """Expanded R78, with an arbitrary actual physical-span quadratic A.

    Uses F-d/2=q symmetric-product qbar /2.  No q+qbar substitution into
    third templates and no repeated A(q,qbar) expansion are needed.
    """
    q, qb = ring.color("q"), ring.color("qbar")
    a, c = quadratic(q, q), quadratic(qb, qb)
    taqq = third(a, q, q)
    tqqa = third(q, q, a)
    tqqq = third(q, q, q)
    aq_tqqq = quadratic(q, tqqq)
    minus4 = taqq/8+tqqa/4-aq_tqqq/4
    minus2 = (-taqq/4-third(c, q, q)/8-third(a, qb, qb)/8
        +(third(q, qb, a)+third(qb, q, a)-tqqa-third(q, q, c)
          +aq_tqqq+quadratic(q, third(q, qb, qb))
          -quadratic(q, third(qb, q, q))-quadratic(qb, tqqq))/4)
    return {-4: minus4, -2: minus2}


def reference_response(ring, third, quadratic):
    """Literal independent K/L formula, used only by small artificial toys."""
    q, qb = ring.color("q"), ring.color("qbar")
    f = (q+qb)/2
    q2 = ((F(1), q, q),)
    d = ((F(1, 2), q, q), (F(1, 2), qb, qb))
    target = ((F(1), f, f),)

    def a(D):
        return sum((v*quadratic(x, y) for v, x, y in D), ring.number(0))

    def t(x, D):
        return sum((v*third(x, y, z) for v, y, z in D), ring.number(0))

    def K(D1, D2):
        return t(a(D1), D2)+t(a(D2), D1)

    def L(E, D):
        aD = a(D)
        return sum((v*(-2*third(x, y, aD)-2*third(y, x, aD)
                       +2*quadratic(x, t(y, D))+2*quadratic(y, t(x, D)))
                    for v, x, y in E), ring.number(0))

    return {-4: (K(q2, q2)-L(q2, q2))/16,
            -2: -(L(target, q2)+K(d, q2)-(L(d, q2)+L(q2, d))/2)/4}


def mode_zero(ring):
    return {mode: ring.number(0) for mode in producer.MODES}


def add_modes(target, source, coefficient=F(1)):
    for mode in producer.MODES:
        target[mode] += coefficient*source[mode]


class BlockProblem:
    def __init__(self, limits, receipt, report):
        self.limits = limits
        self.ring, self.constant, self.templates, self.baseline, self.binding = dual.compile_original_problem(limits, receipt)
        if self.binding["retained_original_indices"] != EXPECTED_KEPT:
            raise AssertionError("the certified homogeneous 36-template basis changed")
        self.grade = ScalingGrading(self.ring)
        self.constant_parts = {mode: self.grade.split(value) for mode, value in self.constant.items()}
        self.baseline_parts = self.grade.split(self.baseline)
        self.normalizer = colored.ColoredNormalizer(self.ring)
        self.working_cache = {}
        self.quadratics = [exact.matrix_operator(self.ring, coordinates) for _, _, coordinates in E_BASIS]
        self.template_proofs = []
        for index, (template, weight) in enumerate(zip(self.templates, THIRD_WEIGHTS)):
            other = template-self.grade.project(template, weight)
            proof = self.normalizer.word.expression(other)
            if proof.terms:
                raise AssertionError("published third basis violated its true scaling weight")
            self.template_proofs.append({"basis_index": index, "v2_original_index": EXPECTED_KEPT[index],
                "weight": weight, "original_sha256": self.ring.digest(template),
                "off_weight_original_difference_zero_sha256": proof.digest()})
        candidates = set().union(*(set(pieces) for pieces in self.constant_parts.values()))
        candidates.update(n+E_BASIS[j][1] for n in self.baseline_parts for j in STANDARD_PARTS)
        self.weights = sorted(candidates, reverse=True)
        self.identity = {"bound_v2_receipt_sha256": dual.RECEIPT_SHA,
            "constant_original_sha256": self.binding["original_target_sha256"],
            "rational_baseline_original_sha256": self.ring.digest(self.baseline),
            "retained_template_original_sha256": self.binding["retained_original_template_sha256"],
            "quadratic_basis": [{"name": name, "weight": weight, "coordinates": list(map(str, coordinates))}
                                for name, weight, coordinates in E_BASIS],
            "third_basis_weights": list(THIRD_WEIGHTS), "mode_formula": "R78 compact exact polarization v1"}
        report["original_problem"] = self.binding
        report["problem_identity"] = self.identity
        report["problem_identity_sha256"] = digest(self.identity)
        report["weight_inventory"] = {"candidate_target_weights_descending": self.weights,
            "constant_modes": {str(mode): self.grade.inventory(value) for mode, value in self.constant.items()},
            "rational_baseline_third": self.grade.inventory(self.baseline),
            "third_basis_homogeneity_proofs": self.template_proofs,
            "predicted_raw_response_columns_by_weight": {str(k): v for k, v in EXPECTED_BLOCK_COLUMNS.items()}}

    def working(self, expression):
        key = expression.key()
        if key not in self.working_cache:
            value = self.normalizer.expression(expression)
            fresh = colored.ColoredNormalizer(self.ring)
            difference = fresh.word.expression(expression-value)
            if difference.terms:
                raise AssertionError("working third representative failed original-form verification")
            self.working_cache[key] = value
        return self.working_cache[key]

    def target(self, weight, working):
        output = {mode: self.constant_parts[mode].get(weight, self.ring.number(0)) for mode in producer.MODES}
        for index, coefficient in STANDARD_PARTS.items():
            expression = self.baseline_parts.get(weight-E_BASIS[index][1])
            if expression is not None:
                third = colored.ThirdOperator(self.ring, self.working(expression) if working else expression)
                add_modes(output, full_response(self.ring, third, self.quadratics[index]), coefficient)
        return output

    def labels(self, weight):
        labels = []
        for quadratic_index, (name, aweight, coordinates) in enumerate(E_BASIS):
            for template_index, tweight in enumerate(THIRD_WEIGHTS):
                if aweight+tweight == weight:
                    labels.append({"column": len(labels), "quadratic_index": quadratic_index,
                        "quadratic_name": name, "quadratic_weight": aweight,
                        "quadratic_coordinates": list(map(str, coordinates)),
                        "third_index": template_index, "third_weight": tweight,
                        "v2_original_third_index": EXPECTED_KEPT[template_index],
                        "third_original_sha256": self.ring.digest(self.templates[template_index])})
        if len(labels) != EXPECTED_BLOCK_COLUMNS.get(weight, 0):
            raise AssertionError("weight-block combinatorial coverage changed")
        return labels

    def column(self, label, working):
        template = self.templates[label["third_index"]]
        third = colored.ThirdOperator(self.ring, self.working(template) if working else template)
        return full_response(self.ring, third, self.quadratics[label["quadratic_index"]])

    def original_linear_combination(self, weight, labels, coefficients, include_target):
        """Fresh original formulas, grouped only by the linear quadratic slot."""
        output = ({mode: self.constant_parts[mode].get(weight, self.ring.number(0)) for mode in producer.MODES}
                  if include_target else mode_zero(self.ring))
        thirds = {index: self.ring.number(0) for index in range(len(E_BASIS))}
        if include_target:
            for index, coefficient in STANDARD_PARTS.items():
                thirds[index] += coefficient*self.baseline_parts.get(weight-E_BASIS[index][1], self.ring.number(0))
        for column, coefficient in coefficients.items():
            label = labels[column]
            thirds[label["quadratic_index"]] += coefficient*self.templates[label["third_index"]]
        for index, expression in thirds.items():
            if expression.terms:
                add_modes(output, full_response(self.ring, colored.ThirdOperator(self.ring, expression),
                                                self.quadratics[index]))
        return output

    def original_zero(self, weight, labels, coefficients, include_target):
        raw = self.original_linear_combination(weight, labels, coefficients, include_target)
        fresh = colored.ColoredNormalizer(self.ring)
        checks = {}
        for mode, value in raw.items():
            reduced = fresh.word.expression(value)
            if reduced.terms:
                raise AssertionError("fresh original full-mode identity failed")
            checks[str(mode)] = {"original_difference_sha256": self.ring.digest(value),
                                 "fresh_zero_sha256": reduced.digest()}
        return checks


def polynomial_evaluation(args, problem, weight, labels, retained, remaining, block):
    context = poly.PolynomialContext(args.prime, 2, 3, seconds=remaining,
        max_degree=args.max_degree, memory_mib=args.memory_mib, max_operations=args.max_operations)
    _, _, profile = dual.fixed_profiles(context, args.bump_power)
    raw = poly.RawExpressionEvaluator(problem.ring.p, context, context.colors)
    quadratics = [exact.matrix_operator(context, coordinates) for _, _, coordinates in E_BASIS]
    target = {mode: raw.expression(problem.constant_parts[mode].get(weight, problem.ring.number(0)))
              for mode in producer.MODES}
    for index, coefficient in STANDARD_PARTS.items():
        expression = problem.baseline_parts.get(weight-E_BASIS[index][1])
        if expression is not None:
            response = full_response(context, poly.EvaluatedThirdOperator(problem.ring.p, context, expression),
                                     quadratics[index])
            add_modes(target, response, coefficient)
    points = [F(j, args.points+1) for j in range(1, args.points+1)]
    row_labels = [{"t": str(t), "xi": str(2+t), "mode": mode, "component": part}
                  for t in points for mode in producer.MODES for part in ("real", "imaginary")]

    def rows_of(expressions):
        return [value for t in points for mode in producer.MODES for value in expressions[mode].value(t)]

    target_rows = rows_of(target)
    columns, identities = [], []
    for number, index in enumerate(retained):
        label = labels[index]
        third = poly.EvaluatedThirdOperator(problem.ring.p, context, problem.templates[label["third_index"]])
        response = full_response(context, third, quadratics[label["quadratic_index"]])
        columns.append(rows_of(response))
        identities.append({"retained_column": number, "original_block_column": index,
            "mode_polynomial_sha256": {str(mode): response[mode].digest() for mode in producer.MODES}})
        block["evaluation_checkpoint"] = {"completed_columns": number+1, "total_columns": len(retained)}
        context.check(0)
    rows = [[column[j] for column in columns] for j in range(len(row_labels))]
    witness = poly.full_column_dual(rows, target_rows, args.prime)
    if witness["rational_nonmembership_certified"]:
        witness["selected_evaluation_labels"] = [row_labels[j] for j in witness["selected_augmented_rows"]]
    return {"original_right_primitive_values_not_word_values": True,
        "profile": profile, "projected_weight": weight,
        "all_evaluation_labels": row_labels, "row_count": len(rows), "column_count": len(retained),
        "all_matrix_modular_values_sha256": digest(rows), "all_target_modular_values_sha256": digest(target_rows),
        "target_mode_polynomial_sha256": {str(mode): target[mode].digest() for mode in producer.MODES},
        "retained_original_column_identities": identities, "coefficient_arithmetic": context.coefficient_report(),
        "dual_certificate": witness,
        "scope": "nonmembership of one homogeneous UNIVERSAL operator block; not a fixed-profile full unprojected P1 obstruction"}


def run_block(args, problem, weight, started, block):
    block["phase"] = "projected_original_target"
    labels = problem.labels(weight)
    block["all_original_block_columns"] = labels
    block["source_template_homogeneity_and_coverage"] = "R94; all 36 original basis weights checked in this run"
    target = problem.target(weight, working=True)
    for mode, expression in target.items():
        outside = expression-problem.grade.project(expression, weight)
        if problem.normalizer.word.expression(outside).terms:
            raise AssertionError("target weight projection inconsistent with arbitrary-A response")
    target_vector = colored.vector_from_modes(target, problem.normalizer)
    block["working_target"] = {"word_terms": len(target_vector), "word_sha256": colored.vector_digest(target_vector),
        "original_formula": {"constant_projected_sha256": {
            str(mode): problem.ring.digest(problem.constant_parts[mode].get(weight, problem.ring.number(0)))
            for mode in producer.MODES},
            "baseline_parts": [{"quadratic_index": index, "coefficient": str(coefficient),
                "third_weight": weight-E_BASIS[index][1],
                "original_third_sha256": problem.ring.digest(problem.baseline_parts.get(
                    weight-E_BASIS[index][1], problem.ring.number(0)))}
                for index, coefficient in STANDARD_PARTS.items()]}}
    if not target_vector:
        block["fresh_original_mode_checks"] = problem.original_zero(weight, labels, {}, True)
        block["outcome"] = "target_zero_verified"
        return
    block["phase"] = "homogeneous_response_columns"
    columns = []
    for label in labels:
        response = problem.column(label, working=True)
        vector = colored.vector_from_modes(response, problem.normalizer)
        columns.append(vector)
        label["working_response_word_terms"] = len(vector)
        label["working_response_word_sha256"] = colored.vector_digest(vector)
        block["response_checkpoint"] = {"completed_columns": len(columns), "total_columns": len(labels)}
        problem.ring.substitution_cache.clear()
        problem.limits.formal.time_check()
        print(json.dumps({"weight": weight, "phase": block["phase"], "completed": len(columns),
                          "of": len(labels)}), flush=True)
    block["phase"] = "sound_response_upper_bound"
    span = colored.JointSpan(columns, problem.limits)
    retained = span.independent
    proofs = []
    for index in range(len(labels)):
        if index in retained:
            continue
        coefficients, remainder = span.reduce(columns[index])
        if remainder or not set(coefficients).issubset(retained):
            raise AssertionError("homogeneous response spanning decomposition")
        combination = {j: -c for j, c in coefficients.items()}
        combination[index] = combination.get(index, F(0))+1
        checks = problem.original_zero(weight, labels, combination, False)
        proofs.append({"discarded_original_block_column": index,
            "retained_original_coefficients": [[j, str(c)] for j, c in sorted(coefficients.items())],
            "fresh_original_mode_checks": checks})
    block["response_reduction"] = {"original_block_columns": len(labels),
        "retained_original_columns": retained, "proved_true_response_dimension_upper_bound": len(retained),
        "verified_original_dependencies": proofs, "actual_function_independence_not_assumed": True}
    coefficients, remainder = span.reduce(target_vector)
    block["word_remainder"] = producer.readable_vector(remainder, 12)
    block["provisional_coefficients_to_subtract"] = [[j, str(c)] for j, c in sorted(coefficients.items())]
    if not remainder:
        block["phase"] = "fresh_original_positive_identity"
        block["fresh_original_mode_checks"] = problem.original_zero(
            weight, labels, {j: -c for j, c in coefficients.items()}, True)
        block["actual_signed_homogeneous_control_coefficients"] = [[j, str(-c)] for j, c in sorted(coefficients.items())]
        block["outcome"] = "member_identity_verified"
        return
    block["phase"] = "original_rational_block_evaluation"
    remaining = args.max_seconds-(time.monotonic()-started)
    if remaining <= 0:
        raise poly.PolynomialBudgetExceeded("overall time budget before original block evaluation")
    block["original_evaluation"] = polynomial_evaluation(
        args, problem, weight, labels, retained, remaining, block)
    witness = block["original_evaluation"]["dual_certificate"]
    block["outcome"] = "nonmember_certified" if witness["rational_nonmembership_certified"] else "undecided"


def response_toys():
    limits = exact.Limits(seconds=60, nodes=15000, atoms=15000, terms=15000,
                          rewrites=100000, memory_mib=256)
    ring = colored.ColoredRing(limits)
    grade = ScalingGrading(ring)
    a, b, c = (ring.color(name) for name in ("a", "b", "c"))
    x = ring.x()
    checks = {}
    example = x*x*a.D()*b+(a*b.D()).I()+a.D().I()*b
    pieces = grade.split(example)
    if sum(pieces.values(), ring.number(0)).key() != example.key():
        raise AssertionError("exact grading reconstruction")
    checks["raw_weight_projection_reconstructs_original"] = True
    for n, piece in pieces.items():
        if set(grade.split(piece.D()))- {n-1} or set(grade.split(piece.I()))-{n+1}:
            raise AssertionError("jet/primitive scaling grade")
    checks["differentiation_lowers_and_right_primitive_raises_weight"] = True
    for index, operator in enumerate(exact.operator_basis(ring)):
        if set(grade.split(operator(a, b))) != {PARAMETER_WEIGHTS[index]}:
            raise AssertionError("quadratic coordinate weight")
    checks["all_eight_quadratic_weights"] = True
    template = a*b*c+(a.D()*b*c).I()
    third = colored.ThirdOperator(ring, template)
    quadratic = lambda f, g: f*g+x*(f.D()*g+f*g.D())/2
    compact = full_response(ring, third, quadratic)
    literal = reference_response(ring, third, quadratic)
    norm = colored.ColoredNormalizer(ring)
    for mode in producer.MODES:
        if norm.word.expression(compact[mode]-literal[mode]).terms:
            raise AssertionError("compact arbitrary-A response versus literal K/L")
    checks["compact_two_modes_equal_literal_R78_for_artificial_tensor"] = True
    small_third = colored.ThirdOperator(ring, a*b*c)
    compact = full_response(ring, small_third, exact.positive_constant_operator(ring))
    previous = colored.full_phase_response(ring, small_third)
    for mode in producer.MODES:
        if norm.word.expression(compact[mode]-previous[mode]).terms:
            raise AssertionError("frozen standard-A interface compatibility")
    checks["compact_response_agrees_with_frozen_standard_interface"] = True
    counts = Counter(aweight+tweight for _, aweight, _ in E_BASIS for tweight in THIRD_WEIGHTS)
    if dict(counts) != EXPECTED_BLOCK_COLUMNS or sum(counts.values()) != 252:
        raise AssertionError("seven by 36 homogeneous coverage")
    checks["exact_252_column_block_counts"] = True
    small_poly = poly.small_toys()
    empty = poly.full_column_dual([[], []], [0, 1], 101)
    if not empty["rational_nonmembership_certified"]:
        raise AssertionError("zero-dimensional block dual")
    checks["zero_dimensional_true_upper_bound_can_be_separated"] = True
    return {"scope": "small artificial colored tensors, exact grades, and artificial modular matrices only",
        "checks": checks, "polynomial_toy": small_poly,
        "all_passed": all(checks.values()) and small_poly["all_passed"],
        "research_target_compiled": False, "research_profile_evaluated": False,
        "geometry_integrated": False}


def write_json(path, payload, maximum):
    raw = (json.dumps(payload, indent=2, sort_keys=True, allow_nan=False)+"\n").encode()
    if len(raw) > maximum:
        raise formal.CompilationBudgetExceeded("declared checkpoint JSON byte limit")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw)
    os.replace(temporary, path)
    return {"filename": path.name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def block_path(output, weight):
    return output.with_name(output.stem+"-weight-"+("p"+str(weight) if weight >= 0 else "m"+str(-weight))+".json")


def load_resume(path, source_hashes, output):
    if path is None:
        return None, [], []
    raw = path.read_bytes()
    index = json.loads(raw)
    if index.get("schema") != SCHEMA or index.get("source_hashes") != source_hashes:
        raise ValueError("resume requires byte-identical mathematical sources and schema")
    blocks, references = [], []
    for reference in index.get("completed_blocks", []):
        oldpath = path.parent/reference["filename"]
        if oldpath.name != reference["filename"]:
            raise ValueError("resume block must use a plain basename")
        data = oldpath.read_bytes()
        if len(data) != reference["bytes"] or hashlib.sha256(data).hexdigest() != reference["sha256"]:
            raise ValueError("completed resume block not preserved byte for byte")
        block = json.loads(data)
        if (block.get("schema") != BLOCK_SCHEMA or block.get("completion") != "complete"
                or block.get("source_hashes") != source_hashes
                or block.get("weight") != reference["weight"]
                or block.get("outcome") != reference.get("outcome")
                or block.get("outcome") not in PAID | {"nonmember_certified", "undecided"}
                or block.get("problem_identity_sha256") != index.get("problem_identity_sha256")):
            raise ValueError("resume block identity/completion mismatch")
        newpath = output.parent/reference["filename"]
        newpath.parent.mkdir(parents=True, exist_ok=True)
        if newpath.resolve() != oldpath.resolve():
            newpath.write_bytes(data)
        references.append(dict(reference))
        blocks.append(block)
    return {"index_bytes": len(raw), "index_sha256": hashlib.sha256(raw).hexdigest(),
            "problem_identity_sha256": index.get("problem_identity_sha256"),
            "prior_run_id": index.get("github_run_id")}, blocks, references


def save_block(args, report, block):
    reserved = args.max_index_bytes+sum(item["bytes"] for item in report["completed_blocks"])
    available = TOTAL_PUBLISHED_BYTES-reserved
    if available <= 0:
        raise formal.CompilationBudgetExceeded("total published-output byte ceiling")
    return write_json(block_path(args.output, block["weight"]), block,
                      min(args.max_block_bytes, available))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--input-receipt", type=Path, default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--resume-index", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--weights", default="auto", help="auto descends from actual raw target inventory; or comma-separated integers")
    parser.add_argument("--max-blocks", type=int, default=3)
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--prime", type=int, default=2147483647)
    parser.add_argument("--points", type=int, default=48)
    parser.add_argument("--bump-power", type=int, default=8)
    parser.add_argument("--max-degree", type=int, default=256)
    parser.add_argument("--max-operations", type=int, default=20000000)
    parser.add_argument("--max-block-bytes", type=int, default=300000)
    parser.add_argument("--max-index-bytes", type=int, default=300000)
    args = parser.parse_args()
    if min(args.max_blocks, args.max_seconds, args.memory_mib, args.points, args.max_degree,
           args.max_operations, args.max_block_bytes, args.max_index_bytes) <= 0 or args.bump_power < 8:
        parser.error("positive budgets and bump-power>=8 required")
    if args.max_blocks > 11 or not 50000 <= args.max_block_bytes <= 350000 or not 50000 <= args.max_index_bytes <= 350000:
        parser.error("at most 11 new blocks; individual JSON limits must lie in [50000,350000]")
    if args.points+1 >= args.prime:
        parser.error("evaluation denominators must be below the prime")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"):
        parser.error("actual target compilation/evaluation is restricted to this public repository's Actions")
    requested = None
    if args.weights != "auto":
        try:
            requested = sorted(set(int(item.strip()) for item in args.weights.split(",")), reverse=True)
        except ValueError:
            parser.error("--weights must be auto or comma-separated integer weights")
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started", "phase": "dependencies",
        "github_sha": os.environ.get("GITHUB_SHA"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_repository": os.environ.get("GITHUB_REPOSITORY"), "source_hashes": {},
        "scope": "homogeneous blocks of the TOTAL all-state UNIVERSAL P1 response space",
        "completed_blocks": [], "partial_block": None,
        "all_blocks_membership_verified": False, "universal_all_positive_states_excluded": False,
        "fixed_profile_or_three_moment_circle_excluded": False,
        "P0_paid": False, "fourth_ruling_paid": False,
        "finite_isometric_family_constructed": False, "embedding_or_reach_certified": False,
        "limits": {"seconds": args.max_seconds, "memory_polling_mib": args.memory_mib,
            "maximum_new_blocks": args.max_blocks, "per_block_bytes": args.max_block_bytes,
            "index_bytes": args.max_index_bytes, "coefficient_nodes": 600000,
            "total_published_bytes": TOTAL_PUBLISHED_BYTES,
            "profile_atoms": 200000, "expression_terms": 120000, "word_calls_per_normalizer": 1000000,
            "elimination_bits": 16384, "modular_prime": args.prime, "points": args.points,
            "bump_power": args.bump_power, "polynomial_degree": args.max_degree,
            "polynomial_operations_per_block": args.max_operations},
        "requested_weights": args.weights}
    code, current, problem = 0, None, None
    completed = []
    try:
        report["source_hashes"] = dependencies()
        if args.toy_only:
            report["phase"] = "small_artificial_interface_toys"
            report["toy"] = response_toys()
            report["completion"] = "toy_passed"
        else:
            resume, completed, references = load_resume(args.resume_index, report["source_hashes"], args.output)
            report["resume"] = resume
            report["completed_blocks"] = references
            if sum(item["bytes"] for item in references)+args.max_index_bytes >= TOTAL_PUBLISHED_BYTES:
                raise formal.CompilationBudgetExceeded("resume artifacts exhaust published-output byte ceiling")
            receipt = dual.read_receipt(args.input_receipt)
            report["input_receipt"] = {"bytes": dual.RECEIPT_BYTES, "sha256": dual.RECEIPT_SHA,
                                        "source_commit": dual.RECEIPT_SOURCE}
            limits = exact.Limits(args.max_seconds, 600000, 200000, 120000,
                                  1000000, args.memory_mib, 16384)
            report["phase"] = "restore_bound_original_formulas_and_project_true_weights"
            problem = BlockProblem(limits, receipt, report)
            if resume is not None and resume["problem_identity_sha256"] != report["problem_identity_sha256"]:
                raise ValueError("resumed actual problem identity changed")
            done = {block["weight"]: block for block in completed}
            order = problem.weights if requested is None else requested
            selected = [weight for weight in order if weight not in done][:args.max_blocks]
            report["selected_new_weights"] = selected
            report["phase"] = "weight_blocks"
            write_json(args.output, report, args.max_index_bytes)
            if any(block.get("outcome") == "nonmember_certified" for block in completed):
                selected = []
            for weight in selected:
                current = {"schema": BLOCK_SCHEMA, "completion": "started", "phase": "initializing",
                    "weight": weight, "source_hashes": report["source_hashes"],
                    "github_sha": report["github_sha"], "github_run_id": report["github_run_id"],
                    "github_repository": report["github_repository"],
                    "input_receipt": report["input_receipt"],
                    "problem_identity_sha256": report["problem_identity_sha256"],
                    "scope": report["scope"], "outcome": "unresolved",
                    "same_real_coefficients_in_both_modes": True,
                    "fixed_profile_full_unprojected_P1_claimed": False}
                block_started = time.monotonic()
                run_block(args, problem, weight, started, current)
                current["completion"] = "complete"
                current["elapsed_seconds"] = time.monotonic()-block_started
                current["max_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
                entry = save_block(args, report, current)
                entry.update({"weight": weight, "outcome": current["outcome"]})
                report["completed_blocks"].append(entry)
                completed.append(current)
                done[weight] = current
                current = None
                report["elapsed_seconds"] = time.monotonic()-started
                write_json(args.output, report, args.max_index_bytes)
                if done[weight]["outcome"] in ("nonmember_certified", "undecided"):
                    break
            report["universal_all_positive_states_excluded"] = any(
                block.get("outcome") == "nonmember_certified" for block in completed)
            report["all_blocks_membership_verified"] = all(
                weight in done and done[weight].get("outcome") in PAID for weight in problem.weights)
            report["remaining_unpaid_weights"] = [weight for weight in problem.weights
                if weight not in done or done[weight].get("outcome") not in PAID]
            report["completion"] = "complete"
            report["phase"] = "bounded_scope_completed"
            report["compiler_size"] = {"coefficient_nodes": len(problem.ring.algebra.c.nodes),
                                        "profile_atoms": len(problem.ring.p.atoms)}
            report["interpretation"] = (
                "Each positive block is verified on fresh original formulas. Each negative block requires a full-rank original rational augmented minor at a proved response upper bound; R91 then excludes universal positive-state identities, not a fixed special profile. A complete bounded scope with unpaid blocks is not full membership. P0 and all geometric completion gates remain unpaid.")
    except (formal.CompilationBudgetExceeded, poly.PolynomialBudgetExceeded) as exc:
        report["completion"], report["error"], code = "resource_limit", str(exc), 2
        report["not_a_negative_mathematical_result"] = True
    except Exception as exc:
        report["completion"], report["error"], code = "implementation_check_failed", type(exc).__name__+": "+str(exc), 2
    if current is not None:
        current["completion"] = report["completion"]
        current["error"] = report.get("error")
        current["not_a_negative_mathematical_result"] = True
        try:
            report["partial_block"] = save_block(args, report, current)
            report["partial_block"]["weight"] = current["weight"]
        except formal.CompilationBudgetExceeded:
            report["partial_block"] = {"weight": current["weight"], "completion": "partial_output_limit",
                "no_mathematical_certificate_published": True}
    report["elapsed_seconds"] = time.monotonic()-started
    report["max_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    # Already completed block files are immutable and survive every later error.
    try:
        final = write_json(args.output, report, args.max_index_bytes)
    except formal.CompilationBudgetExceeded:
        reduced = {key: report[key] for key in ("schema", "source_hashes", "github_sha", "github_run_id",
                   "problem_identity_sha256", "completed_blocks") if key in report}
        reduced.update({"completion": "index_output_limit", "prior_completed_block_files_preserved": True,
                        "full_unpublished_index_sha256": digest(report)})
        final = write_json(args.output, reduced, args.max_index_bytes)
        code = 2
    print(json.dumps({"completion": report["completion"], **final, "output": str(args.output)}), flush=True)
    return code


if __name__ == "__main__":
    sys.exit(main())
