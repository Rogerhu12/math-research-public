#!/usr/bin/env python3
"""One J6 raw-rational probe using an archived implicit 43-column pivot.

The complete old 42-square matrix is reused. The 43rd column is D0, whose
old pivot coordinates and full modular residual polynomials are already
published. Only J6 and one old-42-root combination are newly evaluated.
No missing old row is filled and no old column is individually evaluated.
Only if the new modular residual is zero, try one bounded Q reconstruction
and verify its new pure/balanced original differences. No old pure solve,
old kernel relation, old normal form, or response/forcing compile is rerun.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import gzip
import json
from math import gcd, isqrt
import os
from pathlib import Path
import resource
import time

import literature_J6_balanced_original_difference as bound

base = bound.solver.target_io
axis, layer = base.axis, base.layer
static, old, exact, colored, formal = base.static, base.old, base.exact, base.colored, base.formal
poly, dual = base.poly, base.dual
canonical, sha = base.canonical, base.sha
MODES, PRIME, TOPIC, REPOSITORY = base.MODES, base.PRIME, base.TOPIC, base.REPOSITORY
SCHEMA = "visible-flex-J6-implicit43-original-separation-v1"
BOUND_DRIVER = {"filename": "literature_J6_balanced_original_difference.py", "bytes": 31517,
    "sha256": "5994a0837aa7e9a4657de09b085b93b6b23ca0ba8fbe809b2914dec2264e1022"}
OLD_DRIVER = {"filename": "literature_D0_pivot_residual_probe.py", "bytes": 32755,
    "sha256": "e6a4c15bfe95c587c4cde0cae26b33cf0bf4f54f0ea7b9cfb5c83026c98afbcd"}
OLD_RUN = "43658922081"
OLD_COMMIT = "a63985719537feab6649745ecb9b8736bf094ff9"
OLD_LANE = "D0_pivot_residual"
OLD_MAIN = {"filename": "D0-pivot-residual.json", "bytes": 21050,
    "sha256": "b91b06cdb452d1d938341231c1a85de4c45dfd46bec1ca44c498413c345ae89e"}
OLD_RECEIPT = {"filename": "receipt.json", "bytes": 36978,
    "sha256": "6876bfe2741a083533d1a5e62c37f28c6394c94ab425041054c1fe9eab84fd00"}
OLD_COMPLETE = {"filename": "D0-pivot-residual-complete-report.json.gz", "stored_bytes": 32740,
    "stored_sha256": "5c89ab45b79e32021d6466736be2d28a83841bad665f7789150c670e55a762ed",
    "raw_bytes": 83465,
    "raw_sha256": "54a1ac32eb1895c512d533b6deb30853c60f92ee2d9e87c125fd5f2ae7f482dc"}
OLD_EXPORT = {"filename": "D0-pivot-residual-original-residual.json.gz", "stored_bytes": 71856,
    "stored_sha256": "eeac6ff33f19d75c5621fec7c615d400aa6a0119fe3383073d3768986795844b",
    "raw_bytes": 294020,
    "raw_sha256": "29c18008975301e472c4ddbb9e2791ff42f8e7543f4001cdc8ba1a98f62ccb50"}
OLD_EXTRA = {"component": "real", "mode": -2, "t": "1/70", "xi": "141/70"}
OLD_RESIDUE = 379682857
OLD_DETERMINANT43 = 267072587
OLD_RESIDUAL_COEFFICIENTS_SHA = "906c75134d3946af1f843db2e1b7fac57dc123b38dcefe97bfbb9618390de2fd"
OLD_RESIDUAL_HASHES = {
    "-4": "e46d442ad42c86ba53fb766fd3eeeba663d47f9ed8bac531012dab02139901a1",
    "-2": "7d2ef970187788c0a43f19ee46fda22156af9aa6dd4aeff37e8a256c8f3dc66e",
}
BALANCED_RUN = "43661460271"
BALANCED_COMMIT = "ae7e5af322c13ba8bbff6130a284272b48446568"
BALANCED_LANE = "J6_balanced_original_difference"
BALANCED_MAIN = {"filename": "J6-balanced-original-difference.json", "bytes": 66143,
    "sha256": "932cd382bdec6909f090dfca703698332f71cf4d1912600fcb655a0bb19cebc6"}
BALANCED_RECEIPT = {"filename": "receipt.json", "bytes": 37457,
    "sha256": "255c964d54ed356b8aef61d33861519bcecb6f159d8dd6ddd52c2afa2ee2fc99"}
BALANCED_RAW_SHA = "b9de00e7990fa22153498a8f909ee43098083435fea0610bad8a8fe09f178391"
BALANCED_NF_SHA = "2bdbf31812a548604e6eace83a1d67db8d11e9d416414b1da6b6537d8806c07c"


def source_identity():
    inputs = bound.source_identity()
    if inputs["driver"] != BOUND_DRIVER or base.source_identity()["driver"] != OLD_DRIVER:
        raise ValueError("the completed original input readers changed")
    return {**inputs, "driver": static.identity(__file__),
            "bound_balanced_input_reader": inputs["driver"], "archived_pivot_reader": OLD_DRIVER}


def bind_arguments(args):
    base.bind_response_arguments(args)
    args.J_report = args.family_directory / bound.prior.FAMILY["main"]["filename"]
    args.J_publication = args.family_directory / bound.prior.FAMILY["receipt"]["filename"]
    args.J_export = args.family_directory / bound.prior.FAMILY["export"]["filename"]
    args.J_complete_report = args.family_directory / base.J_COMPLETE["filename"]
    args.response_report = args.response_directory / bound.prior.RESPONSE["main"]["filename"]
    args.response_publication = args.response_directory / bound.prior.RESPONSE["receipt"]["filename"]
    args.response_export = args.response_directory / bound.prior.RESPONSE["export"]["filename"]


def load_J6(args, ring, report):
    expected = report["source_hashes"]["completed_pure_producer"]["complete_five_family_producer"]
    data, info = bound.read_original_bundle(args.family_directory, bound.prior.FAMILY, expected)
    row = bound.completed.select_record(data.get("family_records", []),
        bound.completed.FAMILY_NAME, bound.completed.STATE_KEY, bound.completed.TARGET_HASHES)
    if (row.get("roots") != bound.completed.TARGET_NAMES
        or row.get("profile_weights") != [-2]
        or row.get("requested_weight_original_mode_sha256") != bound.completed.TARGET_HASHES
        or data.get("state_coordinate_order") != ["h", "k", "omega", "logh"]
        or data.get("selected_weight") != -2):
        raise ValueError("the complete two-mode J6 source identity changed")
    names = row["roots"]
    roots = axis.subset_decode(ring, data, names.values())
    modes = {m: roots[names[str(m)]] for m in MODES}
    if {str(m): ring.digest(x) for m, x in modes.items()} != bound.completed.TARGET_HASHES:
        raise ValueError("the two J6 original roots differ from the completed pure input")
    report["J6_input"] = {**info, "complete_family_record": row,
        "original_mode_sha256": bound.completed.TARGET_HASHES,
        "old_balanced_original_difference_or_word_representative_read": False,
        "new_response_or_geometry_reconstructed": False}
    return modes


def check_residue_coefficients(rows, prime):
    if set(rows) != {str(m) for m in MODES}:
        raise ValueError("both complete archived residual polynomials are required")
    for pairs in rows.values():
        if not isinstance(pairs, (list, tuple)):
            raise ValueError("the archived polynomial must be a complete coefficient array")
        for pair in pairs:
            if (not isinstance(pair, (list, tuple)) or len(pair) != 2
                or any(type(x) is not int or not 0 <= x < prime for x in pair)):
                raise ValueError("malformed modular Gaussian polynomial coefficient")
        if pairs and tuple(pairs[-1]) == (0, 0):
            raise ValueError("the archived polynomial is not in its saved trimmed representation")


def load_archived_D0_step(args, ring, matrix, queries, labels, profiles, report):
    directory = args.previous_directory
    main = layer.read_bound_json(directory / OLD_MAIN["filename"], OLD_MAIN)
    publication = layer.read_bound_json(directory / OLD_RECEIPT["filename"], OLD_RECEIPT)
    expected_sources = base.source_identity()
    checkpoint = main.get("checkpoint", {})
    complete, original = main.get("complete_report_file", {}), main.get("portable_new_residual_export", {})
    if (main.get("schema") != base.SCHEMA or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != OLD_RUN or main.get("github_sha") != OLD_COMMIT
        or main.get("source_hashes") != expected_sources
        or checkpoint.get("outcome") != "D0_original_nonmembership_certified"
        or checkpoint.get("comparison_space_true_dimension") != 42
        or checkpoint.get("new_augmented_order") != 43
        or checkpoint.get("new_augmented_determinant_mod_p_by_Schur_identity") != OLD_DETERMINANT43
        or checkpoint.get("functional_D0_value_mod_p") != OLD_RESIDUE
        or checkpoint.get("extra_query", {}).get("label") != OLD_EXTRA
        or not checkpoint.get("rational_nonmembership_certified")
        or not complete.get("persisted") or not original.get("persisted")
        or any(complete.get(k) != v for k, v in OLD_COMPLETE.items())
        or any(original.get(k) != v for k, v in OLD_EXPORT.items())):
        raise ValueError("the completed original 43-column separation changed")
    full_binding = layer.check_publication(publication,
        run=OLD_RUN, commit=OLD_COMMIT, lane=OLD_LANE, driver=OLD_DRIVER,
        main_name=OLD_MAIN["filename"], main_info=OLD_MAIN, export_info=complete)
    original_binding = layer.check_publication(publication,
        run=OLD_RUN, commit=OLD_COMMIT, lane=OLD_LANE, driver=OLD_DRIVER,
        main_name=OLD_MAIN["filename"], main_info=OLD_MAIN, export_info=original)
    data = layer.read_bound_export(directory / OLD_COMPLETE["filename"], complete)
    if (data.get("schema") != base.SCHEMA or data.get("completion") != "complete"
        or data.get("github_repository") != REPOSITORY
        or str(data.get("github_run_id")) != OLD_RUN or data.get("github_sha") != OLD_COMMIT
        or data.get("source_hashes") != expected_sources
        or data.get("checkpoint") != checkpoint
        or data.get("fixed_pivot_input", {}).get("matrix_mod_p") != matrix
        or data["fixed_pivot_input"].get("selected_evaluation_labels") != queries
        or data["fixed_pivot_input"].get("fixed_profiles") != profiles
        or data.get("comparison_space", {}).get("original_column_labels") != labels
        or data.get("response_input") != report.get("response_input")
        or data.get("coefficient_checkpoint", {}).get("prime") != PRIME
        or not data.get("coefficient_checkpoint", {}).get("all_encountered_rational_denominators_invertible")):
        raise ValueError("the archived residual does not use the same old matrix, columns, and profile")
    solved, checked = data.get("new_pivot_solve", {}), data.get("combined_original_check", {})
    cD, dvals = solved.get("modular_candidate_coordinates"), solved.get("D0_pivot_values_mod_p")
    if (solved != main.get("new_pivot_solve")
        or not isinstance(cD, list) or len(cD) != 42
        or not isinstance(dvals, list) or len(dvals) != 42
        or any(type(v) is not int or not 0 <= v < PRIME for v in cD + dvals)
        or not checked.get("all_saved_pivot_residuals_zero")
        or checked.get("residual_original_mode_sha256") != OLD_RESIDUAL_HASHES):
        raise ValueError("the archived original D0 pivot step is incomplete")
    coefficients = checked.get("residual_modular_polynomial_coefficients", {})
    check_residue_coefficients(coefficients, PRIME)
    if (sha(canonical(coefficients)) != OLD_RESIDUAL_COEFFICIENTS_SHA
        or main.get("combined_original_check", {}).get("residual_coefficients_sha256")
            != OLD_RESIDUAL_COEFFICIENTS_SHA):
        raise ValueError("the complete archived residual polynomial coefficients changed")
    portable = layer.read_bound_export(directory / OLD_EXPORT["filename"], original)
    if (portable.get("schema") != base.SCHEMA + "-original-expressions"
        or portable.get("content_scope") != "D0-and-one-old-root-combination-with-explicit-modular-integer-lifts"
        or portable.get("source_hashes") != expected_sources
        or portable.get("github_repository") != REPOSITORY
        or str(portable.get("github_run_id")) != OLD_RUN or portable.get("github_sha") != OLD_COMMIT
        or portable.get("prime") != PRIME or portable.get("integer_lift_coefficients") != cD
        or portable.get("original_control_labels") != labels
        or portable.get("coefficients_are_not_claimed_to_be_rational_pivot_coordinates") is not True):
        raise ValueError("the old raw residual expression is not the polynomial's bound source")
    names = {m: "residual_with_integer_lifts_%d" % m for m in MODES}
    roots = axis.subset_decode(ring, portable, names.values())
    old_residual = {m: roots[names[m]] for m in MODES}
    if {str(m): ring.digest(e) for m, e in old_residual.items()} != OLD_RESIDUAL_HASHES:
        raise ValueError("the archived residual original hashes changed")
    report["archived_D0_step"] = {
        "publication": full_binding, "original_publication": original_binding,
        "main": OLD_MAIN, "receipt": OLD_RECEIPT, "complete_report": complete,
        "original_export": original, "old_coordinate_vector_mod_p": cD,
        "old_extra_query": OLD_EXTRA, "old_extra_residual_mod_p": OLD_RESIDUE,
        "old_true_43_determinant_mod_p": OLD_DETERMINANT43,
        "residual_coefficients_sha256": OLD_RESIDUAL_COEFFICIENTS_SHA,
        "residual_modular_polynomial_coefficients": coefficients,
        "residual_mode_polynomials": checked["residual_mode_polynomials"],
        "residual_original_mode_sha256": OLD_RESIDUAL_HASHES,
        "old_denominator_certificate": data["coefficient_checkpoint"],
        "old_43rd_row_individual_values_present": False,
        "old_D0_or_old_residual_raw_evaluation_repeated": False,
        "old_matrix_determinant_or_old_separation_recomputed": False,
    }
    return cD, coefficients, checked["residual_mode_polynomials"], old_residual


def restore_polynomials(context, rows, summaries):
    check_residue_coefficients(rows, context.prime)
    answer = {m: poly.Polynomial(context, rows[str(m)]) for m in MODES}
    for m, value in answer.items():
        if {"degree": len(value.coefficients) - 1, "sha256": value.digest()} != summaries[str(m)]:
            raise ValueError("the restored old polynomial differs from its archived digest")
    return answer


def schur43_coefficient(new_first_residual, old_residual, prime):
    if not 0 < old_residual < prime:
        raise ValueError("the old extra pivot must be a nonzero residue")
    return new_first_residual * pow(old_residual, prime - 2, prime) % prime


def bounded_rational_reconstruction(residue, prime, bound):
    """One verified candidate n/d with |n|,d<=bound and 2*bound^2<prime.

    Two different fractions in this box cannot have the same residue:
    their cross-difference has absolute value <prime and is divisible by
    prime. Failure supplies no membership or nonmembership conclusion.
    """
    if (type(prime) is not int or prime <= 2 or type(bound) is not int
        or bound <= 0 or 2*bound*bound >= prime
        or type(residue) is not int or not 0 <= residue < prime):
        raise ValueError("invalid bounded rational reconstruction parameters")
    if residue == 0:
        return F(0)
    r0, r1, t0, t1 = prime, residue, 0, 1
    while r1 > bound:
        quotient = r0 // r1
        r0, r1 = r1, r0-quotient*r1
        t0, t1 = t1, t0-quotient*t1
    numerator, denominator = r1, t1
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    if (not denominator or denominator > bound or abs(numerator) > bound
        or gcd(numerator, denominator) != 1
        or (numerator-residue*denominator) % prime):
        return None
    return F(numerator, denominator)


def Q_combination(ring, controls, coefficients):
    """Keep exact fractions; the old modular-only helper intentionally uses int."""
    if len(controls) != len(coefficients):
        raise ValueError("the Q coefficient count differs from the original columns")
    return {m: sum((F(c)*column[m] for c, column in zip(coefficients, controls)),
                   ring.number(0)) for m in MODES}


def consume_identical_balanced_remainder(args):
    """Do not normalize R161's identical original balanced difference again."""
    main = layer.read_bound_json(args.balanced_directory / BALANCED_MAIN["filename"], BALANCED_MAIN)
    publication = layer.read_bound_json(args.balanced_directory / BALANCED_RECEIPT["filename"], BALANCED_RECEIPT)
    proof = main.get("one_balanced_proposal", {})
    if (main.get("schema") != bound.SCHEMA or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != BALANCED_RUN
        or main.get("github_sha") != BALANCED_COMMIT
        or main.get("source_hashes") != bound.source_identity()
        or main.get("result", {}).get("status") != "undecided_one_balanced_original_remainder"
        or proof.get("balanced_original_difference_sha256") != BALANCED_RAW_SHA
        or proof.get("fresh_original_normal_form", {}).get("terms") != 176
        or proof.get("fresh_original_normal_form", {}).get("sha256") != BALANCED_NF_SHA
        or proof.get("balanced_original_identity_proved") is not False):
        raise ValueError("the completed identical balanced-remainder record changed")
    binding = layer.check_publication(publication, run=BALANCED_RUN, commit=BALANCED_COMMIT,
        lane=BALANCED_LANE, driver=BOUND_DRIVER, main_name=BALANCED_MAIN["filename"],
        main_info=BALANCED_MAIN, export_info=main["portable_original_certificate"])
    return {"publication": binding, "main": BALANCED_MAIN, "receipt": BALANCED_RECEIPT,
        "original_difference_sha256": BALANCED_RAW_SHA,
        "original_identity_proved": False, "fresh_original_normal_form": proof["fresh_original_normal_form"],
        "previous_nonzero_representative_is_not_nonmembership": True,
        "identical_original_R161_check_consumed_not_rerun": True}


def check_new_Q_originals(ring, difference, args, *, known_pure_sha=None,
                         previous_balanced=None):
    """Verify one new Q relation via pure zero followed by faithful balanced zero."""
    if ring.color_degrees(difference[-4]) - {(("q", 4),)}:
        raise ValueError("the proposed pure original difference changed its profile colors")
    if ring.color_degrees(difference[-2]) - bound.MIXED_DEGREES:
        raise ValueError("the proposed mixed original difference is not canonical quartic")
    balanced = bound.project_color_degree(ring, difference[-2])
    pure_sha, balanced_sha = ring.digest(difference[-4]), ring.digest(balanced)
    proof = {"new_original_mode_sha256": {str(m): ring.digest(e) for m, e in difference.items()},
        "balanced_original_difference_sha256": balanced_sha,
        "balanced_original_difference_terms": len(balanced.terms),
        "same_exact_Q_coefficients_for_both_modes": True,
        "original_identity_proved": False, "normalizer_sound_but_not_complete": True,
        "nonzero_representative_is_not_nonmembership": True,
        "implication_source": "R159: a canonical pure-zero real function is determined by its balanced bidegree(2,2) part"}
    if pure_sha == known_pure_sha:
        pure_proof = {"original_difference_sha256": pure_sha,
            "original_identity_proved": True, "completed_R160_pure_identity_consumed_not_rerun": True}
    else:
        normalizer = colored.ColoredNormalizer(ring, args.max_IBP_calls, args.max_terms)
        remainder = normalizer.word.expression(difference[-4])
        pure_proof = {"original_difference_sha256": pure_sha,
            "original_identity_proved": not remainder.terms,
            "fresh_original_normal_form": normalizer.word.summary(remainder),
            "original_word_remainder_rows": bound.pure.word_rows(remainder),
            "normalizer_statistics": dict(normalizer.word.stats)}
    proof["pure"] = pure_proof
    if previous_balanced is not None:
        balanced_proof = previous_balanced
    else:
        normalizer = colored.ColoredNormalizer(ring, args.max_IBP_calls, args.max_terms)
        remainder = normalizer.word.expression(balanced)
        balanced_proof = {"original_difference_sha256": balanced_sha,
            "original_identity_proved": not remainder.terms,
            "fresh_original_normal_form": normalizer.word.summary(remainder),
            "original_word_remainder_rows": bound.pure.word_rows(remainder),
            "normalizer_statistics": dict(normalizer.word.stats)}
    proof["balanced"] = balanced_proof
    proof["original_identity_proved"] = (
        pure_proof["original_identity_proved"] and balanced_proof["original_identity_proved"])
    return balanced, proof


def try_one_Q_candidate(args, ring, target, controls, old_raw, cD, coordinates, report, named):
    """Only the all-zero modular branch; at most one Q proposal, same budget."""
    proposed = [bounded_rational_reconstruction(c, PRIME, args.reconstruction_bound) for c in coordinates]
    record = {"attempted_only_after_all_new_modular_residual_polynomials_zero": True,
        "one_proposal_only": True, "numerator_absolute_bound": args.reconstruction_bound,
        "positive_denominator_bound": args.reconstruction_bound,
        "strict_uniqueness_inequality": 2*args.reconstruction_bound**2 < PRIME,
        "modular_coordinates_are_not_accepted_as_a_Q_relation": True,
        "coordinates_reconstructed": [None if c is None else str(c) for c in proposed]}
    report["one_bounded_Q_proposal"] = record
    if any(c is None for c in proposed):
        record["outcome"] = "bounded_reconstruction_failed_no_member_conclusion"
        return
    # This is algebraic decoding of an already published raw original, not
    # another D0 evaluation or another response. Fractions are never int-cast.
    old_lifts = base.build_combination(ring, controls, cD)
    D0 = {m: old_raw[m] + old_lifts[m] for m in MODES}
    if {str(m): ring.digest(e) for m, e in D0.items()} != base.D0_HASH:
        raise ValueError("recovering the published original D0 from its saved residual changed its hash")
    combination = Q_combination(ring, [*controls, D0], proposed)
    difference = {m: target[m]-combination[m] for m in MODES}
    for m in MODES:
        named["new_Q_candidate_difference_%d" % m] = difference[m]
    balanced = bound.project_color_degree(ring, difference[-2])
    named["new_Q_candidate_balanced_difference"] = balanced
    previous = (consume_identical_balanced_remainder(args)
                if ring.digest(balanced) == BALANCED_RAW_SHA else None)
    balanced, proof = check_new_Q_originals(ring, difference, args,
        known_pure_sha=report["completed_pure_input"]["proved_original_difference_sha256"],
        previous_balanced=previous)
    record["original_proposal"] = proof
    proved = proof["original_identity_proved"]
    record["outcome"] = "complete_original_member_identity_proved" if proved else "undecided_one_new_Q_original_difference"
    if proved:
        report["checkpoint"] = {
            "outcome": "J6_complete_two_mode_member_in_existing43_proved",
            "original_membership_certified": True, "real_span_nonmembership_certified": False,
            "rational_nonmembership_certified": False,
            "same_Q_coefficients_old42_then_D0": [str(c) for c in proposed],
            "same_exact_Q_coefficients_for_both_modes": True,
            "pure_and_balanced_original_identities_verified": True,
            "R159_implication_gives_complete_canonical_function_identity": True,
            "R8_membership_proved_by_this_relation": all(not c for c in proposed[40:]),
            "membership_in_previously_proved_lineality_if_J_D0_coefficients_zero":
                not proposed[41] and not proposed[42],
            "J_D0_coefficients_not_automatically_zero": True,
            "new_signed_control_or_full_ruling_paid": False}


def save_new_originals(args, ring, named, report, coefficients, a):
    path = args.output.with_name(args.output.stem + "-original-residual.json.gz")
    payload = {
        "schema": SCHEMA + "-original-expressions",
        "content_scope": "one-J6-implicit43-residual-with-explicit-modular-lifts",
        "github_repository": report["github_repository"], "github_run_id": report["github_run_id"],
        "github_sha": report["github_sha"], "source_hashes": report["source_hashes"],
        "prime": PRIME, "first_42_candidate_integer_lifts": coefficients,
        "D0_residual_multiplier_integer_lift": a,
        "archived_D0_coordinates_mod_p": report["archived_D0_step"]["old_coordinate_vector_mod_p"],
        "coefficients_are_not_true_Q_member_coordinates": True,
        "separate_Q_candidate_if_any": report.get("one_bounded_Q_proposal"),
        "complete_old43_matrix_is_not_claimed_stored": True,
        "original_old42_labels": report["comparison_space"]["old42_original_column_labels"],
        "original_D0_residual_provenance": {k: report["archived_D0_step"][k]
            for k in ("main", "receipt", "complete_report", "original_export",
                      "residual_coefficients_sha256", "residual_original_mode_sha256")},
        **old.serialize_expressions(ring, named),
    }
    raw, info = canonical(payload), {"filename": path.name, "persisted": False,
        "supplemental_not_a_mathematical_gate": True, "content_scope": payload["content_scope"],
        "root_count": len(named)}
    packed = gzip.compress(raw, mtime=0)
    info.update({"stored_bytes": len(packed), "stored_sha256": sha(packed),
                 "raw_bytes": len(raw), "raw_sha256": sha(raw)})
    if len(packed) <= args.max_export_bytes and len(raw) <= layer.MAX_RAW_INPUT:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(packed)
        info["persisted"] = True
    else:
        info["reason"] = "supplemental export ceiling; the completed mathematical status is retained"
    report["portable_new_residual_export"] = info


def study(args, report, started):
    limits = exact.Limits(args.max_seconds, 500000, 100000, args.max_terms, 500000, args.memory_mib, 8192)
    limits.formal.start = started
    ring = colored.ColoredRing(limits)
    report["phase"] = "consume_R160_pure_evidence_and_original_J6_without_word_reduction"
    bound.load_completed_pure(args, report)
    target = load_J6(args, ring, report)
    J, j_response = axis.load_J(args, ring, report)
    controls, labels = layer.load_response_block(args, ring, report)
    if (len(controls) != 41
        or j_response["retained_original_control_labels"] != report["response_input"]["retained_original_control_labels"]
        or j_response["publication"] != report["response_input"]["publication"]):
        raise ValueError("the completed old comparison columns disagree")
    controls, labels = base.append_published_J(controls, labels, J)
    if sha(canonical(labels)) != base.OLD_LABELS_SHA:
        raise ValueError("old 42-column original order changed")
    matrix, queries, profiles, old_response = base.load_pivot(args, report)
    if old_response != report["response_input"]:
        raise ValueError("the old original matrix and response source differ")
    cD, stored_polynomials, old_summaries, old_raw = load_archived_D0_step(
        args, ring, matrix, queries, labels, profiles, report)
    report["comparison_space"] = {
        "true_dimension": 43, "R8_weight_minus_two": 40, "G_orbit_at_this_weight": 1,
        "J": 1, "D0": 1, "pure_image_dimension_already_proved": 9,
        "pure_kernel_dimension_already_proved": 34,
        "old42_original_column_labels": labels,
        "old_42_labels_sha256": base.OLD_LABELS_SHA,
        "D0_original_mode_sha256": base.D0_HASH,
        "same_real_coefficients_for_both_modes": True,
        "old_43rd_row_individual_values_available": False,
        "old_individual_columns_evaluated": 0, "old_response_compositions": 0,
        "old_upper_bound_independence_and_pure_kernel_consumed_not_reproved": True,
    }
    report["input_regularity"] = dual.reachable_jet_bound(ring,
        list(target.values()) + [x for modes in controls for x in modes.values()])
    if report["input_regularity"]["maximum_input_jet"] > 7:
        raise ValueError("the existing C7 fixed pair is insufficient for the new original target")
    remaining = args.max_seconds - (time.monotonic() - started)
    if remaining <= 0:
        raise poly.PolynomialBudgetExceeded("time before the new original evaluation")
    context = poly.PolynomialContext(PRIME, 2, 3, seconds=remaining, max_degree=args.max_degree,
        memory_mib=args.memory_mib, max_operations=args.max_operations)
    try:
        _, _, actual_profiles = dual.fixed_profiles(context, 8)
        if actual_profiles != profiles:
            raise ValueError("the archived real profile pair or right anchor changed")
        archived_polys = restore_polynomials(context, stored_polynomials, old_summaries)
        evaluator = poly.RawExpressionEvaluator(ring.p, context, context.colors)
        report["phase"] = "new_J6_raw_values_and_one_old42_combination"
        values = {m: evaluator.expression(target[m]) for m in MODES}
        pivot_values = [base.scalar_value(values, label) for label in queries]
        cX = base.solve_new_coordinates(matrix, pivot_values, PRIME)
        combination = base.build_combination(ring, controls, cX)
        # These are the only old-control evaluations: one whole sum per mode.
        combined_values = {m: evaluator.expression(combination[m]) for m in MODES}
        first_residual = {m: values[m] - combined_values[m] for m in MODES}
        pivot_residues = [base.scalar_value(first_residual, label) for label in queries]
        if any(pivot_residues):
            raise AssertionError("the one combined original does not match the archived 42-square matrix")
        new_extra = base.scalar_value(first_residual, OLD_EXTRA)
        a = schur43_coefficient(new_extra, OLD_RESIDUE, PRIME)
        final_values = {m: first_residual[m] - a*archived_polys[m] for m in MODES}
        if base.scalar_value(final_values, OLD_EXTRA):
            raise AssertionError("the implicit 43rd pivot was not cancelled")
        c43 = [(x-a*d) % PRIME for x, d in zip(cX, cD)] + [a]
        raw_first = {m: target[m] - combination[m] for m in MODES}
        raw_final = {m: raw_first[m] - a*old_raw[m] for m in MODES}
        report["new_pivot_solve"] = {
            "J6_first42_values_mod_p": pivot_values, "first42_modular_coordinates": cX,
            "first_residual_at_old_extra_mod_p": new_extra, "D0_multiplier_mod_p": a,
            "implicit43_modular_coordinates": c43, "true_Q_coordinates_not_computed": True,
            "coefficient_order": "old42 full columns followed by D0",
            "integer_lifts_are_only_for_exact_reduction_mod_p": True,
        }
        report["combined_original_check"] = {
            "first42_pivot_residues": pivot_residues, "old_extra_final_residue": 0,
            "all43_pivots_zero_using_the_archived_D0_zero_pivot_proof": True,
            "old_extra_row_individual_values_reconstructed": False,
            "old_D0_raw_or_residual_raw_evaluated": False,
            "old_column_polynomials_individually_evaluated": False,
            "new_evaluated_raw_functions": "J6 and one old42-root sum, both modes",
            "word_representatives_or_R161_normal_form_used": False,
            "combined_original_mode_sha256": {str(m): ring.digest(e) for m, e in combination.items()},
            "final_original_mode_sha256": {str(m): ring.digest(e) for m, e in raw_final.items()},
            "J6_mode_polynomials": {str(m): {"degree": len(p.coefficients)-1,
                "sha256": p.digest()} for m, p in values.items()},
            "first_residual_mode_polynomials": {str(m): {"degree": len(p.coefficients)-1,
                "sha256": p.digest()} for m, p in first_residual.items()},
            "final_residual_mode_polynomials": {str(m): {"degree": len(p.coefficients)-1,
                "sha256": p.digest()} for m, p in final_values.items()},
            "new_target_modular_polynomial_coefficients": {str(m): p.coefficients for m, p in values.items()},
            "first_residual_modular_polynomial_coefficients": {str(m): p.coefficients for m, p in first_residual.items()},
            "residual_modular_polynomial_coefficients": {str(m): p.coefficients for m, p in final_values.items()},
        }
        query = base.nonzero_polynomial_query(final_values)
        if query is None:
            report["checkpoint"] = {
                "outcome": "undecided_fixed_pair_implicit43_modular_residual_zero",
                "real_span_nonmembership_certified": False, "original_membership_certified": False,
                "a_modular_zero_is_not_a_Q_identity": True,
                "new_profile_or_new_control_search_performed": False}
        else:
            label, residue = query["label"], query["residue"]
            if label in queries or label == OLD_EXTRA:
                raise AssertionError("the separating row was one of the cancelled old pivots")
            determinant44 = OLD_DETERMINANT43 * residue % PRIME
            if not determinant44:
                raise AssertionError("the unit 43 determinant lost its nonzero Schur complement")
            report["checkpoint"] = {
                "outcome": "J6_original_nonmembership_in_complete43_certified",
                "rational_nonmembership_certified": True, "real_span_nonmembership_certified": True,
                "original_membership_certified": False, "comparison_space_true_dimension": 43,
                "old_true_43_determinant_mod_p": OLD_DETERMINANT43,
                "new_augmented_order": 44, "new_augmented_determinant_mod_p_by_Schur_identity": determinant44,
                "new_functional_J6_value_mod_p": residue, "extra_query": query,
                "new_first_residual_value_mod_p": base.scalar_value(first_residual, label),
                "archived_D0_residual_value_mod_p": base.scalar_value(archived_polys, label),
                "functional_over_Q": "Lambda_Xi = L_Xi - L_Xi(D0)/L_e(D0) * L_e; L_z = ev_z-row_z(U42)*A_Q^-1*ev_old42",
                "all43_controls_annihilated_over_Q_by_definition": True,
                "why_real_membership_is_excluded": "a hypothetical real relation has the unique coordinates of the invertible rational 43-pivot, hence Q coordinates whose mod-p reduction is the computed one",
                "modular_coordinate_lifts_are_not_a_Q_member_relation": True,
                "complete_upper_bound_source": "R131/R136/R153: 40+G3+J+D0=43; R157/R159: pure image 9 and pure kernel 34",
                "R159_balanced_quotient_nonmembership_follows_from_consumed_pure_proof": True,
                "same_profile_and_common_right_anchor_for_all_rows": True,
                "signed_cost_or_full_ruling_paid": False,
            }
        names = {}
        for m in MODES:
            names["J6_%d" % m] = target[m]
            names["old42_combination_%d" % m] = combination[m]
            names["first_residual_%d" % m] = raw_first[m]
            names["archived_D0_residual_%d" % m] = old_raw[m]
            names["final_integer_lift_residual_%d" % m] = raw_final[m]
        if query is None:
            report["phase"] = "one_bounded_Q_reconstruction_and_only_its_new_original_difference"
            try:
                try_one_Q_candidate(args, ring, target, controls, old_raw, cD, c43, report, names)
            except formal.CompilationBudgetExceeded as error:
                # The completed original modular test remains a valid zero-
                # residual observation; its optional Q check is inconclusive.
                report.setdefault("one_bounded_Q_proposal", {}).update({
                    "outcome": "undecided_candidate_original_check_budget", "error": str(error)})
        report["phase"] = "preserve_new_original_residual_and_complete_polynomial_certificate"
        save_new_originals(args, ring, names, report, cX, a)
        report["completion"], report["phase"] = "complete", "complete_one_implicit43_original_probe"
    finally:
        report["coefficient_checkpoint"] = context.coefficient_report()


def small_toy():
    """Only the new two-step Schur and archived-polynomial interfaces."""
    checks = {}
    p = 103
    A, d, x = [[2, 1], [1, 3]], [1, 4], [3, 2]
    cD = base.solve_new_coordinates(A, d, p)
    cX = base.solve_new_coordinates(A, x, p)
    old_row, d_old, x_old = [3, 4], 7, 9
    RD = (d_old-sum(a*b for a, b in zip(old_row, cD))) % p
    RX = (x_old-sum(a*b for a, b in zip(old_row, cX))) % p
    a = schur43_coefficient(RX, RD, p)
    final_coeff = [(u-a*v) % p for u, v in zip(cX, cD)] + [a]
    A3 = [A[0] + [d[0]], A[1] + [d[1]], old_row + [d_old]]
    direct = poly.solve(A3, x + [x_old], p)
    if final_coeff != direct:
        raise AssertionError("two-step implicit solve disagrees with the tiny direct solve")
    checks["implicit_old_extra_pivot_matches_artificial_direct_solve"] = True
    last, d_last, x_last = [2, -1], 6, 8
    RD_last = (d_last-sum(u*v for u, v in zip(last, cD))) % p
    RX_last = (x_last-sum(u*v for u, v in zip(last, cX))) % p
    residue = (RX_last-a*RD_last) % p
    A4 = [row+[value] for row, value in zip(A3, x+[x_old])] + [last+[d_last, x_last]]
    if not residue or poly.determinant(A4, p) != poly.determinant(A3, p)*residue % p:
        raise AssertionError("the second Schur determinant identity changed")
    checks["new_augmented_minor_uses_old_determinant_times_one_residue"] = True
    exact_coordinates = [F(9, 5), F(-13, 5), F(2)]
    reduced = [v.numerator*pow(v.denominator, p-2, p) % p for v in exact_coordinates]
    if reduced != final_coeff or final_coeff == exact_coordinates:
        raise AssertionError("modular coordinates were confused with Q coordinates")
    checks["modular_lifts_are_distinct_from_true_Q_coordinates"] = True
    try:
        schur43_coefficient(1, 0, p)
    except ValueError:
        checks["zero_archived_extra_pivot_is_rejected"] = True
    else:
        raise AssertionError("zero extra pivot accepted")
    context = poly.PolynomialContext(p, 2, 3, seconds=20, max_degree=32,
        memory_mib=256, max_operations=100000)
    t = context.variable()
    old = {-4: context.number(0), -2: (1+t)*t}
    rows = {str(m): value.coefficients for m, value in old.items()}
    summaries = {str(m): {"degree": len(value.coefficients)-1,
        "sha256": value.digest()} for m, value in old.items()}
    restored = restore_polynomials(context, json.loads(canonical(rows)), summaries)
    if any(restored[m].coefficients != old[m].coefficients for m in MODES):
        raise AssertionError("archived polynomial restore changed coefficients")
    checks["archived_whole_polynomial_restoration_does_not_use_raw_evaluator"] = True
    corrupted = json.loads(canonical(rows));corrupted["-2"][1][0] += 1
    try:
        restore_polynomials(context, corrupted, summaries)
    except ValueError:
        checks["changed_archived_polynomial_digest_is_rejected"] = True
    else:
        raise AssertionError("changed polynomial accepted")
    e = {"mode": -2, "component": "real", "t": "1/2", "xi": "5/2"}
    old_value = base.scalar_value(restored, e)
    gap = t*(t-F(1, 2))
    first = {-4: context.number(0), -2: 7*restored[-2]+gap}
    multiplier = schur43_coefficient(base.scalar_value(first, e), old_value, p)
    final = {m: first[m]-multiplier*restored[m] for m in MODES}
    found = base.nonzero_polynomial_query(final)
    if multiplier != 7 or base.scalar_value(final, e) or not found or found["label"] == e:
        raise AssertionError("the archived extra query was not eliminated before the new row")
    checks["restored_polynomial_update_cancels_only_the_old_extra_query"] = True
    if base.nonzero_polynomial_query({m: first[m]-first[m] for m in MODES}) is not None:
        raise AssertionError("modular zero was made a member or separating witness")
    checks["zero_modular_remainder_retains_undecided_status"] = True
    # New Q branch only: unrelated small fractions and artificial originals.
    for candidate in (F(0), F(1), F(-1), F(9, 5), F(-13, 5), F(32767), F(-7, 32767)):
        reduced = candidate.numerator*pow(candidate.denominator, PRIME-2, PRIME) % PRIME
        if bounded_rational_reconstruction(reduced, PRIME, 32767) != candidate:
            raise AssertionError("the bounded Q candidate changed")
    checks["bounded_Q_reconstruction_recovers_small_verified_fractions"] = True
    if bounded_rational_reconstruction(2, p, 1) is not None:
        raise AssertionError("a residue outside the permitted Q box was accepted")
    try:
        bounded_rational_reconstruction(1, p, 8)
    except ValueError:
        checks["nonunique_Q_box_and_unreconstructed_residue_rejected"] = True
    else:
        raise AssertionError("a nonunique rational box was accepted")
    limits = exact.Limits(20, 10000, 2000, 8000, 20000, 256, 8192)
    ring = colored.ColoredRing(limits)
    q, qb = ring.color("q"), ring.color("qbar")
    phi4 = q*q*q*q
    psi = q*q*qb*qb
    toy_column = {-4: phi4, -2: psi}
    fractional = Q_combination(ring, [toy_column], [F(-2, 7)])
    if fractional[-4].key() != (-F(2, 7)*phi4).key():
        raise AssertionError("the Q candidate was cast to an integer")
    checks["new_Q_combination_preserves_fractional_coefficients"] = True
    artificial_difference = {-4: phi4.D().I()-phi4, -2: psi.D().I()-psi}
    class ToyArgs:
        max_IBP_calls, max_terms = 20000, 8000
    _, proof = check_new_Q_originals(ring, artificial_difference, ToyArgs())
    if not proof["original_identity_proved"]:
        raise AssertionError("the two artificial fresh original identities did not cancel")
    checks["new_pure_and_balanced_original_checks_can_certify_one_Q_candidate"] = True
    _, failed = check_new_Q_originals(ring, {-4: ring.number(0), -2: psi}, ToyArgs())
    if failed["original_identity_proved"] or not failed["nonzero_representative_is_not_nonmembership"]:
        raise AssertionError("a nonzero sound representative was treated as a positive or negative certificate")
    checks["nonzero_fresh_Q_difference_remains_undecided"] = True
    return {"checks": checks, "all_passed": all(checks.values()),
        "published_inputs_read": False, "old_or_new_research_profile_evaluated": False,
        "old_42_columns_or_old_43rd_row_evaluated": False,
        "R161_normal_form_repeated": False}


def publish(args, report):
    full_raw = canonical(report)
    full_path = args.output.with_name(args.output.stem + "-complete-report.json.gz")
    packed = gzip.compress(full_raw, mtime=0)
    full_info = {"filename": full_path.name, "persisted": False,
        "stored_bytes": len(packed), "stored_sha256": sha(packed),
        "raw_bytes": len(full_raw), "raw_sha256": sha(full_raw)}
    if len(packed) <= args.max_full_report_bytes:
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_bytes(packed)
        full_info["persisted"] = True
    else:
        full_info["reason"] = "supplemental complete-report ceiling"
    compact = copy.deepcopy(report)
    for section, fields in {
        "fixed_pivot_input": ("matrix_mod_p",),
        "comparison_space": ("old42_original_column_labels",),
        "archived_D0_step": ("residual_modular_polynomial_coefficients",),
        "combined_original_check": ("new_target_modular_polynomial_coefficients",
            "first_residual_modular_polynomial_coefficients", "residual_modular_polynomial_coefficients"),
        "response_input": ("retained_original_control_labels",),
    }.items():
        if section in compact:
            for field in fields:
                value = compact[section].pop(field, None)
                if value is not None:
                    compact[section][field+"_sha256"] = sha(canonical(value))
            compact[section]["full_data_in_complete_report"] = full_info["persisted"]
    compact["complete_report_file"] = full_info
    if "one_bounded_Q_proposal" in compact:
        proposal = compact["one_bounded_Q_proposal"]
        for item in proposal.get("original_proposal", {}).values():
            if isinstance(item, dict) and "original_word_remainder_rows" in item:
                rows = item.pop("original_word_remainder_rows")
                item["original_word_remainder_rows_sha256"] = sha(canonical(rows))
        compact["one_bounded_Q_proposal_summary"] = {
            k: proposal[k] for k in ("outcome", "error", "coordinates_reconstructed",
                "numerator_absolute_bound", "positive_denominator_bound") if k in proposal}
    raw = canonical(compact)
    if len(raw) > args.max_main_bytes:
        keep = ("schema", "github_repository", "github_run_id", "github_sha", "source_hashes",
            "completion", "phase", "error", "elapsed_seconds", "peak_rss_mib", "checkpoint",
            "portable_new_residual_export", "coefficient_checkpoint", "complete_report_file", "limits", "toy")
        keep += ("one_bounded_Q_proposal_summary",)
        compact = {k: compact[k] for k in keep if k in compact}
        compact["details_in_complete_report"] = full_info["persisted"]
        raw = canonical(compact)
    if len(raw) > args.max_main_bytes:
        raise ValueError("the source-bound compact report exceeds the reserved ceiling")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    return {"filename": args.output.name, "bytes": len(raw), "sha256": sha(raw),
            "completion": report["completion"], "complete_report": full_info}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pure-directory", type=Path,
        default=TOPIC / ("notes/actions-"+bound.PURE_RUN+"-1-"+bound.PURE_LANE))
    parser.add_argument("--family-directory", type=Path, default=bound.prior.directory(bound.prior.FAMILY))
    parser.add_argument("--response-directory", type=Path, default=bound.prior.directory(bound.prior.RESPONSE))
    parser.add_argument("--previous-directory", type=Path,
        default=TOPIC / ("notes/actions-"+OLD_RUN+"-1-"+OLD_LANE))
    parser.add_argument("--balanced-directory", type=Path,
        default=TOPIC / ("notes/actions-"+BALANCED_RUN+"-1-"+BALANCED_LANE))
    parser.add_argument("--max-seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-degree", type=int, default=256)
    parser.add_argument("--max-operations", type=int, default=20000000)
    parser.add_argument("--reconstruction-bound", type=int, default=isqrt((PRIME-1)//2))
    parser.add_argument("--max-IBP-calls", type=int, default=120000)
    parser.add_argument("--max-terms", type=int, default=120000)
    parser.add_argument("--max-main-bytes", type=int, default=90000)
    parser.add_argument("--max-full-report-bytes", type=int, default=2000000)
    parser.add_argument("--max-export-bytes", type=int, default=1500000)
    args = parser.parse_args()
    bind_arguments(args)
    if min(args.max_seconds, args.memory_mib, args.max_degree, args.max_operations,
           args.max_main_bytes, args.max_full_report_bytes, args.max_export_bytes,
           args.reconstruction_bound, args.max_IBP_calls, args.max_terms) <= 0:
        parser.error("positive finite budgets required")
    if 2*args.reconstruction_bound**2 >= PRIME:
        parser.error("the rational box must have 2*B^2 < p")
    if (args.max_main_bytes >= 100000
        or args.max_main_bytes + args.max_full_report_bytes + args.max_export_bytes > static.TOTAL_BYTES):
        parser.error("main below100KB and total bounded outputs required")
    if not args.toy_only and not bound.completed.actual_environment_allowed(os.environ):
        parser.error("the new original evaluation is named-public-repository-Actions-only")
    started, code = time.monotonic(), 0
    report = {"schema": SCHEMA, "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "scope": "only J6 and one old42-root sum; implicit43 plus at most one bounded new Q original proposal",
        "completion": "not_started", "phase": "bind_frozen_original_interfaces",
        "work_scope": {"new_target_original_evaluations": 0 if args.toy_only else 1,
            "old42_combined_original_evaluations": 0 if args.toy_only else 1,
            "old_individual_columns_or_extra_row_entries_evaluated": 0,
            "old_D0_or_archived_residual_original_evaluations": 0,
            "old_pure_solve_or_old_balanced_normal_forms_repeated": 0,
            "maximum_new_Q_proposals_on_the_zero_modular_branch": 1,
            "old_response_forcing_or_new_geometric_targets_compiled": 0},
        "limits": {"seconds": args.max_seconds, "memory_soft_polling_mib": args.memory_mib,
            "max_degree": args.max_degree, "max_operations": args.max_operations,
            "Q_reconstruction_bound": args.reconstruction_bound,
            "IBP_calls_per_new_original_check": args.max_IBP_calls,
            "original_and_word_terms": args.max_terms,
            "main_bytes": args.max_main_bytes, "complete_report_bytes": args.max_full_report_bytes,
            "original_export_bytes": args.max_export_bytes}}
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["phase"] = "new_artificial_two_step_Schur_and_saved_polynomial_interfaces"
            report["toy"] = small_toy()
            report["completion"] = "toy_passed"
        else:
            study(args, report, started)
    except (formal.CompilationBudgetExceeded, poly.PolynomialBudgetExceeded) as error:
        report["completion"], report["error"], code = "resource_limit", str(error), 2
    except Exception as error:
        report["completion"], code = "implementation_check_failed", 1
        report["error"] = {"type": type(error).__name__, "message": str(error)}
    report["elapsed_seconds"] = time.monotonic() - started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    result = publish(args, report)
    print(json.dumps({"output": str(args.output), **result}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
