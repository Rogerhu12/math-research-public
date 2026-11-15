#!/usr/bin/env python3
"""One general pure J membership in the complete published R8 weight -2.

Consume the 40 true full-response basis roots already proved in R131 and
R136's one original J. Only their -4 mode is normalized. Every new discarded
pure column receives its own original-expression difference check. Solve J
once; a positive original identity ends the query. Otherwise evaluate only
J and the retained pure originals once, requiring the proved span upper
bound and a larger original augmented minor for actual nonmembership.

No response, forcing, W, N, v4, power-tail, or mixed-mode computation occurs.
Genuine work is restricted to this public repository's GitHub Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_general_pure_J_identity as prior

pure, layer, orbit = prior.pure, prior.layer, prior.orbit
static, old = prior.static, prior.old
exact, colored, blocks = prior.exact, prior.colored, prior.blocks
formal, quotient = prior.formal, prior.quotient
poly, dual = layer.poly, layer.dual

SCHEMA = "visible-flex-general-pure-J-complete-response-membership-v1"
REPOSITORY = prior.REPOSITORY
PRIOR_DRIVER_SHA = "ddacad3474844368e3546f4e4b0f92e71eb276363cd283ad4f300259e8161f63"
OLD_DEPENDENCIES_SHA = "a6453e43e03f92bc27c9a278e8115d64ece6eed9ddf1f82febdfd12fd05a9498"
RETAINED_FULL = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23, 25, 27, 28, 29, 31, 32, 33, 35, 36,
    39, 40, 41, 46, 47, 48, 49)


def sources():
    bound = prior.sources()
    if bound["driver"]["sha256"] != PRIOR_DRIVER_SHA:
        raise ValueError("explicitly rebind the published original J input helper")
    return {"driver": static.identity(__file__), "bound_original_inputs": bound}


def selected_indices(records, retained):
    if (not isinstance(retained, (list, tuple)) or len(set(retained)) != len(retained)
        or any(type(i) is not int or not 0 <= i < len(records) for i in retained)):
        raise ValueError("the retained original-column index list is malformed")
    return [records[i] for i in retained]


def load_complete_original_basis(directory, data, roots, ring):
    """Use the completed R131 upper bound; never repeat its 10 old relations."""
    main = layer.read_bound_json(directory/prior.RESPONSE["main"]["filename"],
                                prior.RESPONSE["main"])
    checkpoint = main.get("checkpoint") or {}
    upper = checkpoint.get("response_upper_bound") or {}
    if (checkpoint.get("requested_order") != 3
        or checkpoint.get("requested_weight") != prior.WEIGHT
        or upper.get("original_columns") != 50
        or tuple(upper.get("retained_original_columns", [])) != RETAINED_FULL
        or upper.get("proved_true_response_dimension_upper_bound") != 40
        or upper.get("verified_original_dependency_count") != 10
        or upper.get("verified_original_dependencies_sha256") != OLD_DEPENDENCIES_SHA
        or not upper.get("complete_original_dependency_proofs_in_full_report")):
        raise ValueError("the completed full R8 basis certificate changed")
    coverage, records = data.get("response_coverage") or {}, data.get("column_records") or []
    expected = [(i, j) for i, wi in enumerate(blocks.PARAMETER_WEIGHTS)
        for j, wj in enumerate(blocks.THIRD_WEIGHTS) if wi+wj == prior.WEIGHT]
    if (not coverage.get("full_E8") or not coverage.get("all_W36")
        or coverage.get("weight") != prior.WEIGHT or coverage.get("columns") != 50
        or len(records) != 50 or len(expected) != 50
        or not data.get("all_compiled_original_columns_included")):
        raise ValueError("complete original E8 x W36 weight-minus-two coverage is required")
    declared = set()
    for index, (row, pair) in enumerate(zip(records, expected)):
        label = row["label"]
        if (row.get("index") != index
            or (label.get("quadratic_index"), label.get("third_index")) != pair
            or label.get("third_weight") != blocks.THIRD_WEIGHTS[pair[1]]
            or label.get("v2_original_third_index") != blocks.EXPECTED_KEPT[pair[1]]):
            raise ValueError("the archived complete response enumeration changed")
        for mode in (-4, -2):
            name = row["roots"][str(mode)]
            if name not in roots or name in declared:
                raise ValueError("missing or duplicate archived response root")
            declared.add(name)
            if ring.digest(roots[name]) != row["original_mode_sha256"][str(mode)]:
                raise ValueError("the original archived response hash changed")
    translation = checkpoint.get("original_translation_target") or {}
    if data.get("translation") != translation:
        raise ValueError("the archival block and its completed manifest differ")
    for mode in (-4, -2):
        name = data["target_roots"][str(mode)]
        if name not in roots or name in declared:
            raise ValueError("missing or duplicate archival translation root")
        declared.add(name)
        if ring.digest(roots[name]) != translation["original_target_sha256"][str(mode)]:
            raise ValueError("the archival target hash changed")
    if declared != set(roots):
        raise ValueError("the complete original export contains undeclared roots")
    # The qbar roots above are only source-bound hashes. No mixed algebra or
    # evaluation is performed; only the 40 -4 roots enter the new question.
    originals, labels = [], []
    grading = blocks.ScalingGrading(ring)
    for position, row in enumerate(selected_indices(records, RETAINED_FULL)):
        label, name = row["label"], row["roots"]["-4"]
        expression = roots[name]
        pure.require_degree(ring, expression, "q", 4, allow_zero=True)
        if set(grading.split(expression))-{prior.WEIGHT}:
            raise ValueError("an original pure basis root has the wrong weight")
        originals.append(expression)
        labels.append({"position": position, "weight_block_original_column": row["index"],
            "global_R116_column": 8*label["third_index"]+label["quadratic_index"],
            "quadratic_index": label["quadratic_index"],
            "third_index": label["third_index"],
            "third_original_sha256": label["third_original_sha256"],
            "original_root": name, "original_pure_sha256": ring.digest(expression),
            "original_terms": len(expression.terms)})
    return originals, labels, {
        "completed_full_two_mode_upper_bound": upper,
        "full_original_response_columns": 50, "consumed_true_basis_columns": 40,
        "old_original_dependencies_consumed": 10,
        "old_original_dependencies_recomputed": 0,
        "complete_weight_minus_two_pure_span_covered": True,
        "full_two_mode_rank_not_asserted_as_pure_rank": True,
        "G_orbit_added_as_new_control": False,
        "G_orbit_pure_in_response_source": "R138 general-profile identity and affine covariance",
        "retained_original_labels": labels}


def original_proposal(ring, target, originals, coefficients, fresh):
    """The normal-form solve proposes a relation; this tests its raw difference."""
    difference = target
    for index, coefficient in sorted(coefficients.items()):
        if type(index) is not int or not 0 <= index < len(originals):
            raise ValueError("a proposed original relation uses an absent column")
        difference -= F(coefficient)*originals[index]
    reduced = fresh.expression(difference)
    return difference, reduced, {
        "coefficients_in_consumed_original_positions": quotient.coefficient_rows(coefficients),
        "original_difference_sha256": ring.digest(difference),
        "original_difference_terms": len(difference.terms),
        "fresh_original_normal_form": fresh.word.summary(reduced),
        "original_identity_proved": not reduced.terms,
        "nonzero_representative_is_not_nonmembership": bool(reduced.terms)}


def true_cover_indices(independent, proofs, column_count):
    """Unproved proposed dependencies remain actual control columns."""
    independent = list(independent)
    if len(set(independent)) != len(independent) or any(
        type(i) is not int or not 0 <= i < column_count for i in independent):
        raise ValueError("invalid pure representative basis")
    by_index = {}
    for proof in proofs:
        index = proof["dependent_original_position"]
        if (type(index) is not int or not 0 <= index < column_count
            or index in by_index or index in independent):
            raise ValueError("duplicate, invalid, or independent dependency label")
        by_index[index] = proof
    if set(by_index) != set(range(column_count))-set(independent):
        raise ValueError("every omitted pure original requires a recorded proof attempt")
    return sorted(independent+[i for i, row in by_index.items()
        if not row["original_identity_proved"]])


def decode_word_rows(owner, rows):
    """Portable exact pure representatives, not a declaration of independence."""
    def local(value):
        if (not isinstance(value, (tuple, list)) or len(value) != 2
            or type(value[0]) is not int or not isinstance(value[1], (tuple, list))
            or any(type(j) is not int or j < 0 for j in value[1])):
            raise ValueError("malformed pure local word factor")
        if list(value[1]) != sorted(value[1]):
            raise ValueError("pure local jets must use their canonical order")
        return value[0], tuple(value[1])
    terms = {}
    for row in rows:
        if (not isinstance(row, (tuple, list)) or len(row) != 4
            or type(row[2]) is not int or type(row[3]) is not int or row[3] <= 0
            or not isinstance(row[1], (tuple, list))):
            raise ValueError("malformed exact pure word coefficient")
        key = local(row[0]), tuple(local(letter) for letter in row[1])
        value = F(row[2], row[3])
        if not value or key in terms:
            raise ValueError("zero or duplicated portable pure word term")
        terms[key] = value
    return quotient.words.WordExpr(owner, terms)


def polynomial_rows(values, points):
    return [component for point in points for component in values.value(point)]


def raw_pure_evaluation(context, ring, target, originals, retained, points, report):
    """A single shared complex q; evaluate original -4 roots only."""
    if set(context.colors) != {"q"}:
        raise ValueError("the new evaluation must bind only the one pure color q")
    evaluator = poly.RawExpressionEvaluator(ring.p, context, context.colors)
    target_value = evaluator.expression(target)
    target_rows = polynomial_rows(target_value, points)
    rows = [{"t": str(t), "xi": str(context.left+context.width*t),
        "mode": -4, "component": component}
        for t in points for component in ("real", "imaginary")]
    columns, polynomials = [], []
    for index in retained:
        value = evaluator.expression(originals[index])
        columns.append(polynomial_rows(value, points))
        polynomials.append({"original_position": index, "sha256": value.digest(),
            "degree": len(value.coefficients)-1,
            "modular_Gaussian_rational_coefficients": list(value.coefficients)})
        report["checkpoint"]["new_pure_original_columns_evaluated"] = len(columns)
        context.check(0)
    matrix = [[column[i] for column in columns] for i in range(len(rows))]
    witness = poly.full_column_dual(matrix, target_rows, context.prime)
    if witness["rational_nonmembership_certified"]:
        witness["selected_evaluation_labels"] = [rows[i]
            for i in witness["selected_augmented_rows"]]
    return {"single_shared_q": True, "mode": -4,
        "original_roots_evaluated_not_word_representatives": True,
        "same_zero_right_collar_for_every_root": True,
        "retained_original_positions": list(retained),
        "all_evaluation_labels": rows, "matrix": matrix, "target": target_rows,
        "matrix_sha256": pure.sha(pure.data_bytes(matrix)),
        "target_sha256": pure.sha(pure.data_bytes(target_rows)),
        "original_pure_polynomials": polynomials,
        "target_pure_polynomial": {"sha256": target_value.digest(),
            "degree": len(target_value.coefficients)-1,
            "modular_Gaussian_rational_coefficients": list(target_value.coefficients)},
        "dual_certificate": witness}


def certified_nonmember(upper_bound, witness, coefficient_report):
    if not witness.get("rational_nonmembership_certified"):
        return False
    if (type(upper_bound) is not int or upper_bound < 0
        or witness.get("control_columns") != upper_bound
        or witness.get("modular_control_rank") != upper_bound
        or not witness.get("modular_pivot_determinant")
        or not witness.get("modular_augmented_determinant")
        or not witness.get("modular_functional_target_value")
        or witness.get("modular_functional_all_control_values") != [0]*upper_bound
        or not coefficient_report.get("prime_checked_by_trial_division")
        or not coefficient_report.get("all_encountered_rational_denominators_invertible")):
        raise ValueError("a new original pure minor must attain the proved true span upper bound")
    return True


def compact_dual(witness):
    result = dict(witness)
    matrix = result.pop("modular_augmented_matrix", None)
    if matrix is not None:
        result["complete_augmented_matrix_in_original_certificate"] = {
            "rows": len(matrix), "columns": len(matrix[0]) if matrix else 0,
            "sha256": pure.sha(pure.data_bytes(matrix))}
    return result


def save_certificate(args, report, ring, named, certificate):
    payload = {"schema": SCHEMA+"-original-expressions",
        "content_scope": "one J and the complete weight-minus-two pure response membership question",
        "github_repository": report.get("github_repository"),
        "github_run_id": report.get("github_run_id"), "github_sha": report.get("github_sha"),
        "source_hashes": report["source_hashes"],
        "input_family": report.get("input_family"), "input_response": report.get("input_response"),
        "input_basis": report.get("input_basis"), "phase": report["phase"],
        "mathematical_result": report.get("result"), **certificate,
        **old.serialize_expressions(ring, named)}
    path = args.output.with_name(args.output.stem+"-certificate.json.gz")
    metadata = pure.store_gzip(path, payload, args.max_certificate_bytes)
    metadata.update({"content_scope": payload["content_scope"],
        "original_root_count": len(named),
        "new_pure_column_representatives": len(certificate.get("pure_column_representatives", [])),
        "input_original_columns_recompiled": False})
    report["portable_original_certificate"] = metadata


def run_research(args, report, started):
    limits = exact.Limits(args.max_seconds, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.memory_mib, args.max_rational_bits)
    ring = colored.ColoredRing(limits)
    source = report["source_hashes"]["bound_original_inputs"]
    report["phase"] = "consume_one_bound_original_J"
    data, roots, info = prior.load_original(args.family_directory, prior.FAMILY,
        source["five_family_producer"], ring)
    target, target_info = prior.select_original_J(data, roots, ring)
    report["input_family"], report["original_J"] = info, target_info
    report["phase"] = "consume_complete_published_weight_minus_two_basis"
    data, roots, info = prior.load_original(args.response_directory, prior.RESPONSE,
        source["weight_minus_two_producer"], ring)
    originals, labels, basis_info = load_complete_original_basis(args.response_directory, data, roots, ring)
    report["input_response"], report["input_basis"] = info, basis_info
    regularity = dual.reachable_jet_bound(ring, [target]+originals)
    if regularity["colors"] != ["q"]:
        raise ValueError("only pure original q roots may enter the new study")
    report["input_regularity"] = regularity
    named = {"original_J_minus4": target}
    named.update({"original_pure_column_%02d" % i: value for i, value in enumerate(originals)})
    certificate = {"pure_column_representatives": [], "new_pure_dependency_proofs": [],
        "normalizer_sound_but_not_complete": True,
        "old_complete_two_mode_dependencies_recomputed": False}
    report["work_scope"] = {"new_pure_response_formulas": 0, "new_mixed_response_formulas": 0,
        "old_forcing_W_N_v4_recompiled": 0, "new_power_tail_substitutions": 0,
        "new_mixed_root_normalizations_or_evaluations": 0,
        "new_general_pure_targets": 1, "consumed_full_basis_pure_roots": 40,
        "old_fixed_six_column_candidate_repeated": False,
        "conditional_new_pure_profile_pairs": 0,
        "independent_primitive_values_assigned": False, "extra_phase_factor_applied": False}
    report["phase"] = "new_pure_only_word_representatives_of_existing_roots"
    normalizer = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    vectors = []
    for i, expression in enumerate(originals):
        value = normalizer.expression(expression)
        vectors.append(value)
        certificate["pure_column_representatives"].append({"original_position": i,
            "original_root": "original_pure_column_%02d" % i,
            "original_sha256": labels[i]["original_pure_sha256"],
            "word_summary": normalizer.word.summary(value), "word_rows": pure.word_rows(value)})
        report["checkpoint"] = {"normalized_existing_pure_columns": i+1, "total": len(originals)}
        if (i+1) % 10 == 0:
            save_certificate(args, report, ring, named, certificate)
            print(json.dumps({"phase": report["phase"], "columns": i+1, "of": len(originals)}), flush=True)
    target_vector = normalizer.expression(target)
    certificate["target_pure_representative"] = {
        "word_summary": normalizer.word.summary(target_vector), "word_rows": pure.word_rows(target_vector)}
    save_certificate(args, report, ring, named, certificate)
    span = quotient.ExactWordSpan(vectors, limits)
    report["pure_representative_span"] = span.summary()
    report["phase"] = "prove_only_new_pure_dependencies_from_original_differences"
    fresh = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    proofs = certificate["new_pure_dependency_proofs"]
    independent = set(span.independent)
    for index, vector in enumerate(vectors):
        if index in independent:
            continue
        coefficients, remainder = span.reduce(vector)
        if remainder.terms or not set(coefficients) <= independent:
            raise AssertionError("a proposed pure dependence does not use the retained original roots")
        difference, reduced, proof = original_proposal(ring, originals[index], originals, coefficients, fresh)
        name = "new_pure_dependency_%02d_difference" % index
        named[name] = difference
        proof.update({"dependent_original_position": index,
            "weight_block_original_column": labels[index]["weight_block_original_column"],
            "global_R116_column": labels[index]["global_R116_column"],
            "original_difference_root": name,
            "complete_original_difference_representative": pure.word_rows(reduced)})
        proofs.append(proof)
        report["checkpoint"] = {"new_pure_dependency_attempts": len(proofs),
            "new_verified_pure_dependencies": sum(p["original_identity_proved"] for p in proofs)}
        if len(proofs) % 5 == 0:
            save_certificate(args, report, ring, named, certificate)
    retained = true_cover_indices(span.independent, proofs, len(originals))
    verified = sum(p["original_identity_proved"] for p in proofs)
    report["pure_response_upper_bound"] = {
        "input_true_full_basis_columns": len(originals),
        "new_pure_representative_rank": len(span.independent),
        "retained_original_positions": retained,
        "retained_weight_block_original_columns": [labels[i]["weight_block_original_column"] for i in retained],
        "retained_global_R116_columns": [labels[i]["global_R116_column"] for i in retained],
        "proved_true_pure_dimension_upper_bound": len(retained),
        "new_original_pure_dependencies_verified": verified,
        "unresolved_proposed_pure_dependencies_retained": len(proofs)-verified,
        "all_new_original_dependencies_in_certificate": True,
        "new_dependency_proofs_sha256": pure.sha(pure.data_bytes(proofs)),
        "original_pure_span_is_covered": verified+len(retained) == len(originals),
        "true_pure_independence_not_assumed": True}
    if not report["pure_response_upper_bound"]["original_pure_span_is_covered"]:
        raise AssertionError("a source pure column was removed without a proved original identity")
    certificate["pure_response_upper_bound"] = report["pure_response_upper_bound"]
    save_certificate(args, report, ring, named, certificate)
    report["phase"] = "one_J_solve_and_fresh_original_remainder"
    coefficients, remainder = span.reduce(target_vector)
    if not set(coefficients) <= independent:
        raise AssertionError("the one target proposal uses nonretained normal-form columns")
    difference, reduced, proposal = original_proposal(ring, target, originals, coefficients, fresh)
    named["one_J_proposed_original_difference"] = difference
    proposal.update({"word_solve_remainder": normalizer.word.summary(remainder),
        "word_solve_remainder_rows": pure.word_rows(remainder),
        "fresh_original_remainder_rows": pure.word_rows(reduced),
        "original_difference_root": "one_J_proposed_original_difference",
        "fresh_original_difference_checked_even_if_word_solve_unresolved": True})
    certificate["one_J_proposal"] = proposal
    report["one_J_proposal"] = {key: value for key, value in proposal.items()
        if not key.endswith("_rows")}
    positive = proposal["original_identity_proved"]
    report["result"] = {
        "status": "general_pure_member_identity_proved" if positive else "unresolved_original_remainder",
        "general_pure_J_member_proved": positive, "general_pure_J_nonmember_proved": False,
        "all_general_pure_costs_in_response_proved": False,
        "complete_two_mode_J_member_proved": False,
        "actual_cost_sign_or_signed_control_claimed": False,
        "pure_mode": -4, "profile_affine_weight": prior.WEIGHT}
    save_certificate(args, report, ring, named, certificate)
    if not positive:
        report["phase"] = "one_conditional_original_general_pure_rational_witness"
        if regularity["maximum_input_jet"] > args.bump_power-1:
            raise ValueError("the declared fixed pure pair lacks the actual required regularity")
        seconds = args.max_seconds-(time.monotonic()-started)
        if seconds <= 0:
            raise poly.PolynomialBudgetExceeded("time before the single new pure original witness")
        context = poly.PolynomialContext(args.prime, 2, 3, seconds=seconds,
            max_degree=args.max_degree, memory_mib=args.memory_mib, max_operations=args.max_operations)
        try:
            _, _, profiles = dual.fixed_profiles(context, args.bump_power)
            context.colors = {"q": context.colors["q"]}
            report["checkpoint"] = {"new_pure_original_columns_evaluated": 0,
                "retained_original_columns": len(retained)}
            points = [F(j, args.points+1) for j in range(1, args.points+1)]
            report["work_scope"]["conditional_new_pure_profile_pairs"] = 1
            evaluation = raw_pure_evaluation(context, ring, target, originals, retained, points, report)
        finally:
            report["coefficient_checkpoint"] = context.coefficient_report()
        evaluation["fixed_profiles"] = profiles
        certificate["conditional_original_pure_evaluation"] = evaluation
        witness = evaluation["dual_certificate"]
        negative = certified_nonmember(len(retained), witness, report["coefficient_checkpoint"])
        report["conditional_original_pure_evaluation"] = {
            "fixed_profiles": profiles, "mode": -4,
            "evaluated_original_control_columns": len(retained),
            "matrix_sha256": evaluation["matrix_sha256"],
            "target_sha256": evaluation["target_sha256"],
            "full_original_polynomials_and_rows_in_certificate": True,
            "dual_certificate": compact_dual(witness)}
        report["result"].update({
            "status": "general_pure_J_nonmember_certified" if negative else "undecided",
            "general_pure_J_nonmember_proved": negative,
            "true_pure_response_dimension": len(retained) if witness["modular_control_rank"] == len(retained) else None,
            "true_pure_response_dimension_lower_bound": witness["modular_control_rank"],
            "true_pure_response_dimension_upper_bound": len(retained),
            "deficient_modular_rank_not_used_as_upper_bound": True,
            "finite_modular_fit_not_used_as_function_identity": True})
    report["normalizer_statistics"] = {
        "representatives": {"right_IBP": normalizer.legacy.stats, "word": normalizer.word.stats},
        "new_original_differences": {"right_IBP": fresh.legacy.stats, "word": fresh.word.stats}}
    certificate["normalizer_statistics"] = report["normalizer_statistics"]
    report["phase"] = "complete_one_J_general_pure_membership_question"
    report["completion"] = "complete"
    save_certificate(args, report, ring, named, certificate)
    report["coefficient_arithmetic"] = {"field": "Q", "profile_atoms": len(ring.p.atoms),
        "coefficient_nodes": len(ring.algebra.c.nodes), "limits_check_calls": limits.calls}


def artificial_toys():
    """Only this new projection/coverage/proposal/portable/dual adapter."""
    checks = {}
    records = [{"id": 4}, {"id": 9}, {"id": 13}]
    if selected_indices(records, (2, 0)) != [records[2], records[0]]:
        raise AssertionError("retained raw ordering")
    for bad in ((0, 0), (3,), (-1,)):
        try:
            selected_indices(records, bad)
        except ValueError:
            continue
        raise AssertionError("malformed retained originals must be rejected")
    checks["retained_original_order_and_missing_or_duplicate_indices"] = True
    limits = exact.Limits(seconds=30, nodes=6000, atoms=3000, terms=6000,
        rewrites=20000, memory_mib=512)
    ring = colored.ColoredRing(limits)
    q, qb, x = ring.jet(), ring.color("qbar"), ring.x()
    try:
        pure.require_degree(ring, q**3*qb, "q", 4)
    except ValueError:
        checks["a_mixed_root_cannot_enter_the_pure_adapter"] = True
    else:
        raise AssertionError("a mixed input was accepted")
    raw = [q**4, q*q*q.D()*q.D()]
    raw.append(F(2)*raw[0]-F(3)*raw[1])
    norm = quotient.ProfileNormalizer(ring, 20000, 6000)
    vectors = [norm.expression(value) for value in raw]
    span = quotient.ExactWordSpan(vectors, limits)
    if span.independent != [0, 1]:
        raise AssertionError("artificial pure projected basis")
    coefficients, remainder = span.reduce(vectors[2])
    fresh = quotient.ProfileNormalizer(ring, 20000, 6000)
    _, reduced, proof = original_proposal(ring, raw[2], raw, coefficients, fresh)
    if remainder.terms or reduced.terms or not proof["original_identity_proved"]:
        raise AssertionError("new pure dependency needs an original zero")
    proof["dependent_original_position"] = 2
    if true_cover_indices(span.independent, [proof], 3) != [0, 1]:
        raise AssertionError("proved raw dependency covers its original")
    checks["new_pure_dependency_solve_and_original_difference"] = True
    _, bad_nf, bad_proof = original_proposal(ring, raw[2]+q**4, raw, coefficients, fresh)
    bad_proof["dependent_original_position"] = 2
    if not bad_nf.terms or bad_proof["original_identity_proved"]:
        raise AssertionError("a proposed representative identity cannot erase its original remainder")
    if true_cover_indices(span.independent, [bad_proof], 3) != [0, 1, 2]:
        raise AssertionError("unproved pure dependency must remain in the true cover")
    checks["unproved_raw_relation_retains_its_control"] = True
    target = F(5, 7)*raw[0]+F(11, 13)*raw[1]
    coefficients, remainder = span.reduce(norm.expression(target))
    _, reduced, result = original_proposal(ring, target, raw, coefficients, fresh)
    if remainder.terms or reduced.terms or not result["original_identity_proved"]:
        raise AssertionError("one positive original target relation")
    checks["single_target_original_positive_identity"] = True
    for value in vectors:
        rows = json.loads(pure.data_bytes(pure.word_rows(value)))
        if decode_word_rows(norm.word, rows).digest() != value.digest():
            raise AssertionError("new portable pure vector round trip")
    checks["complete_pure_word_rows_round_trip"] = True
    # This is a small artificial polynomial, never the published test pair.
    context = poly.PolynomialContext(101, 2, 3, seconds=20, max_degree=24, memory_mib=512)
    t = context.variable()
    context.colors = {"q": t*(1-t)*(1+context.number((0, 1))*t)}
    toy_report = {"checkpoint": {}}
    evaluation = raw_pure_evaluation(context, ring, x*x*q**4,
        [q**4, x*q**4], [0, 1], [F(1, 5), F(2, 5), F(3, 5)], toy_report)
    witness = evaluation["dual_certificate"]
    if not certified_nonmember(2, witness, context.coefficient_report()):
        raise AssertionError("new original-pure-only rational adapter")
    checks["new_raw_pure_only_rational_adapter"] = True
    try:
        certified_nonmember(3, witness, context.coefficient_report())
    except ValueError:
        checks["a_minor_cannot_exceed_an_unattained_true_upper_bound"] = True
    else:
        raise AssertionError("a partial control minor was promoted")
    return {"checks": checks, "all_passed": all(checks.values()),
        "published_research_DAG_loaded": False,
        "old_research_or_development_query_repeated": False,
        "research_profile_or_geometry_evaluated": False,
        "complete_response_or_forcing_compiled": False}


def write_main(args, report):
    raw = pure.data_bytes(report, pretty=True)
    if len(raw) > args.max_main_bytes:
        path = args.output.with_name(args.output.stem+"-complete-report.json.gz")
        full = pure.store_gzip(path, report, args.max_full_report_bytes)
        keep = ("schema", "completion", "phase", "scope", "github_repository", "github_run_id",
            "github_sha", "source_hashes", "limits", "work_scope", "result", "toy", "error",
            "original_J", "input_regularity", "pure_representative_span", "pure_response_upper_bound",
            "one_J_proposal", "conditional_original_pure_evaluation", "portable_original_certificate",
            "elapsed_seconds", "peak_rss_mib", "checkpoint")
        compact = {key: report.get(key) for key in keep if key in report}
        compact["complete_report_file"] = full
        raw = pure.data_bytes(compact, pretty=True)
        if len(raw) > args.max_main_bytes:
            compact = {"schema": SCHEMA, "completion": "output_limit",
                "github_repository": report.get("github_repository"),
                "github_run_id": report.get("github_run_id"), "github_sha": report.get("github_sha"),
                "source_hashes": report.get("source_hashes"),
                "computation_completion": report.get("completion"), "result": report.get("result"),
                "complete_report_file": full,
                "portable_original_certificate": report.get("portable_original_certificate"),
                "error": "full result preserved; selected main exceeded its byte budget"}
            raw = pure.data_bytes(compact, pretty=True)
        if len(raw) > args.max_main_bytes:
            raise ValueError("source-bound compact main exceeds its byte budget")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    return {"filename": args.output.name, "bytes": len(raw), "sha256": pure.sha(raw),
        "completion": json.loads(raw)["completion"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--family-directory", type=Path, default=prior.directory(prior.FAMILY))
    parser.add_argument("--response-directory", type=Path, default=prior.directory(prior.RESPONSE))
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-nodes", type=int, default=500000)
    parser.add_argument("--max-atoms", type=int, default=100000)
    parser.add_argument("--max-terms", type=int, default=120000)
    parser.add_argument("--max-IBP-calls", type=int, default=500000)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    parser.add_argument("--prime", type=int, default=2147483647)
    parser.add_argument("--bump-power", type=int, default=8)
    parser.add_argument("--points", type=int, default=24)
    parser.add_argument("--max-degree", type=int, default=256)
    parser.add_argument("--max-operations", type=int, default=20000000)
    parser.add_argument("--max-main-bytes", type=int, default=90000)
    parser.add_argument("--max-certificate-bytes", type=int, default=2500000)
    parser.add_argument("--max-full-report-bytes", type=int, default=2000000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.max_rational_bits, args.max_degree,
        args.max_operations, args.bump_power, args.points,
        args.max_certificate_bytes, args.max_full_report_bytes) <= 0:
        parser.error("positive finite resource bounds required")
    if not 10000 <= args.max_main_bytes < 100000:
        parser.error("reserve 10000..99999 bytes for the source-bound compact main")
    if args.max_main_bytes+args.max_certificate_bytes+args.max_full_report_bytes > pure.TOTAL_OUTPUT_BYTES:
        parser.error("declared output exceeds the reserved total byte bound")
    if (not poly.is_prime(args.prime) or args.prime % 4 != 3
        or args.prime <= max(args.points+1, args.max_degree+1)):
        parser.error("use a checked prime 3 mod 4 larger than evaluation denominators")
    if 2*args.points < len(RETAINED_FULL)+1:
        parser.error("enough one-mode real/imaginary rows for every possible retained pure basis")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("the genuine pure membership question is public-repository-Actions-only")
    started, code = time.monotonic(), 0
    report = {"schema": SCHEMA, "completion": "started", "phase": "bind_existing_sources",
        "scope": "one general pure J against the complete original R8 weight-minus-two projection",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {}, "finite_isometric_family_constructed": False,
        "limits": {"seconds": args.max_seconds, "memory_polling_mib": args.memory_mib,
            "nodes": args.max_nodes, "atoms": args.max_atoms, "terms": args.max_terms,
            "IBP_calls_per_normalizer": args.max_IBP_calls, "rational_bits": args.max_rational_bits,
            "prime": args.prime, "bump_power": args.bump_power, "points": args.points,
            "degree": args.max_degree, "operations": args.max_operations,
            "main_bytes": args.max_main_bytes, "certificate_bytes": args.max_certificate_bytes,
            "full_report_bytes": args.max_full_report_bytes}}
    try:
        report["source_hashes"] = sources()
        if args.toy_only:
            report["phase"] = "new_small_artificial_projection_and_proof_interfaces"
            report["toy"] = artificial_toys()
            report["completion"] = "toy_passed"
        else:
            run_research(args, report, started)
    except (formal.CompilationBudgetExceeded, poly.PolynomialBudgetExceeded) as error:
        report["completion"], report["error"], code = "resource_limit", str(error), 2
    except Exception as error:
        report["completion"], code = "implementation_check_failed", 1
        report["error"] = {"type": type(error).__name__, "message": str(error)}
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written = write_main(args, report)
    if written["completion"] == "output_limit":
        code = 2
    print(json.dumps({"output": str(args.output), **written}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
