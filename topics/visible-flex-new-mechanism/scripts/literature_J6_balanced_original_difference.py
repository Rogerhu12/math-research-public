#!/usr/bin/env python3
"""One R159 balanced original difference after R160's proved pure identity.

Read the published exact Q coefficients and successful pure certificate.
Decode only J6's complete mixed root and the six needed old mixed response
roots. Project their single raw difference to color degree (2,2), then make
one sound colored right-Volterra reduction. No pure solve, response compile,
old kernel reconstruction, rank calculation, or profile evaluation occurs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_general_pure_J6_membership as completed

solver, prior = completed.solver, completed.prior
axis, layer = completed.axis, completed.layer
pure, static, old = completed.pure, completed.static, completed.old
exact, colored, blocks = completed.exact, completed.colored, completed.blocks
formal = completed.formal

SCHEMA = "visible-flex-J6-one-balanced-original-difference-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = completed.TOPIC
MODE, WEIGHT = -2, -2
BALANCED = (("q", 2), ("qbar", 2))
MIXED_DEGREES = {
    (("q", 4),), (("q", 3), ("qbar", 1)), BALANCED,
}
PURE_DRIVER = {
    "filename": "literature_general_pure_J6_membership.py", "bytes": 23040,
    "sha256": "48afb00617c5c5251bde7ab2f7782740ff43bf4318cfd78193137c3343c0f745",
}
PURE_RUN = "43660884663"
PURE_COMMIT = "b41c6f13ffbe56543d3593acb0b9023d8320e93c"
PURE_LANE = "general_pure_J6_membership"
PURE_MAIN = {
    "filename": "general-pure-J6-membership.json", "bytes": 64382,
    "sha256": "d52e8cea9d0e7db1ca1b5348336ca18e0d7e38ab1e98d8c5ade79b84c9825660",
}
PURE_RECEIPT = {
    "filename": "receipt.json", "bytes": 37243,
    "sha256": "825cfe157853f75513ece5ae728e9a4db15c718b3195d72ead36afe9d2905ae2",
}
PURE_EXPORT = {
    "filename": "general-pure-J6-membership-certificate.json.gz",
    "stored_bytes": 15080,
    "stored_sha256": "03e4e377632a7bfea3225d8ef27339bf26567f5aaa818ec7d23f9ce1a74568bd",
    "raw_bytes": 101758,
    "raw_sha256": "bd9eabce279313b74dc51adfc1b55c4bac72369544fb7a1ec33c296cfdc246d6",
}
PURE_SCOPE = "one-original-J6-pure-solve-against-nine-archived-originals"
PURE_DIFFERENCE_SHA = "53958fd1febb5dd07595e9a807c3576923dfc8c00408fe463941d3560458cfab"
EXPECTED_COEFFICIENTS = {
    0: F(-1, 64), 88: F(-1, 64), 41: F(-1, 128),
    73: F(-1, 32), 81: F(-5, 128), 193: F(1, 256),
}
ZERO_DIGEST = "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"


def source_identity():
    previous = completed.source_identity()
    if previous["driver"] != PURE_DRIVER:
        raise ValueError("the successful one-J6 pure producer changed")
    return {"driver": static.identity(__file__), "completed_pure_producer": previous}


def parse_coefficients(proof, labels):
    """Bind local-nine and global-column Q coordinates without a new solve."""
    if (not proof.get("original_identity_proved")
        or proof.get("coefficients_are_exact_Q_not_modular_lifts") is not True
        or proof.get("fresh_original_normal_form", {}).get("terms") != 0
        or proof.get("fresh_original_normal_form", {}).get("sha256") != ZERO_DIGEST):
        raise ValueError("a completed exact pure original identity is required")
    if len({row.get("global_R116_column") for row in labels}) != len(labels):
        raise ValueError("duplicate completed pure basis global index")
    by_local = {}
    for entry in proof.get("coefficients_in_consumed_original_positions", []):
        if (len(entry) != 2 or type(entry[0]) is not int
            or not 0 <= entry[0] < len(labels) or entry[0] in by_local
            or not isinstance(entry[1], str)):
            raise ValueError("malformed exact local-nine pure coordinates")
        coefficient = F(entry[1])
        if not coefficient or str(coefficient) != entry[1]:
            raise ValueError("canonical nonzero rational coefficients required")
        by_local[entry[0]] = coefficient
    by_global = {}
    for entry in proof.get("coefficients_in_original_global_columns", []):
        if (len(entry) != 2 or type(entry[0]) is not int
            or entry[0] in by_global or not isinstance(entry[1], str)):
            raise ValueError("malformed exact global pure coordinates")
        coefficient = F(entry[1])
        if not coefficient or str(coefficient) != entry[1]:
            raise ValueError("canonical nonzero rational coefficients required")
        by_global[entry[0]] = coefficient
    translated = {labels[i]["global_R116_column"]: c for i, c in by_local.items()}
    if translated != by_global:
        raise ValueError("local-nine coordinates and global old columns disagree")
    return by_global


def load_completed_pure(args, report):
    directory = args.pure_directory
    main = layer.read_bound_json(directory / PURE_MAIN["filename"], PURE_MAIN)
    publication = layer.read_bound_json(directory / PURE_RECEIPT["filename"], PURE_RECEIPT)
    expected = report["source_hashes"]["completed_pure_producer"]
    result, metadata = main.get("result", {}), main.get("portable_original_certificate", {})
    if (main.get("schema") != completed.SCHEMA or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != PURE_RUN
        or main.get("github_sha") != PURE_COMMIT or main.get("source_hashes") != expected
        or result.get("general_pure_J6_member_proved") is not True
        or result.get("complete_two_mode_J6_member_proved") is not False
        or result.get("pure_mode") != -4 or result.get("profile_affine_weight") != WEIGHT
        or metadata.get("content_scope") != PURE_SCOPE
        or metadata.get("original_root_count") != 11
        or any(metadata.get(k) != v for k, v in PURE_EXPORT.items())):
        raise ValueError("the published successful R160 pure identity changed")
    binding = layer.check_publication(
        publication, run=PURE_RUN, commit=PURE_COMMIT, lane=PURE_LANE,
        driver=PURE_DRIVER, main_name=PURE_MAIN["filename"], main_info=PURE_MAIN,
        export_info=metadata,
    )
    data = layer.read_bound_export(directory / PURE_EXPORT["filename"], metadata)
    if (data.get("schema") != completed.SCHEMA + "-original-expressions"
        or data.get("content_scope") != PURE_SCOPE
        or data.get("github_repository") != REPOSITORY
        or str(data.get("github_run_id")) != PURE_RUN
        or data.get("github_sha") != PURE_COMMIT or data.get("source_hashes") != expected
        or data.get("mathematical_result") != result
        or data.get("input_J6") != main.get("J6_input")
        or data.get("input_pure_basis") != main.get("input_pure_basis")
        or len(data.get("roots", {})) != 11):
        raise ValueError("the pure original certificate is not the same completed result")
    proof = data.get("one_J6_proposal") or {}
    compact_proof = {k: v for k, v in proof.items() if not k.endswith("_rows")}
    if compact_proof != main.get("one_J6_proposal"):
        raise ValueError("the published pure proof summary and certificate disagree")
    labels = data.get("archived_selected_labels") or []
    if (len(labels) != 9
        or tuple(row.get("archived_original_position") for row in labels) != solver.BASIS_POSITIONS
        or tuple(row.get("global_R116_column") for row in labels) != solver.BASIS_GLOBAL
        or labels != main.get("input_pure_basis", {}).get("labels")
        or proof.get("original_difference_root") != "one_J6_proposed_original_difference"
        or proof.get("original_difference_sha256") != PURE_DIFFERENCE_SHA
        or proof.get("original_difference_terms") != 307):
        raise ValueError("the one proved pure proposal or its old-column labels changed")
    declared = data.get("original_root_sha256", {})
    if (declared.get("original_J6_minus4") != completed.TARGET_HASHES["-4"]
        or declared.get(proof["original_difference_root"]) != PURE_DIFFERENCE_SHA):
        raise ValueError("the pure proof does not bind its actual original roots")
    for row in labels:
        name = "archived_original_pure_column_%02d" % row["archived_original_position"]
        if name not in data["roots"] or declared.get(name) != row["original_pure_sha256"]:
            raise ValueError("a proved pure coefficient was detached from its original column")
    coefficients = parse_coefficients(proof, labels)
    if coefficients != EXPECTED_COEFFICIENTS:
        raise ValueError("use exactly the completed six nonzero R160 Q coefficients")
    report["completed_pure_input"] = {
        "publication": binding, "main": PURE_MAIN, "receipt": PURE_RECEIPT,
        "complete_certificate": metadata, "proved_original_difference_sha256": PURE_DIFFERENCE_SHA,
        "coefficients_in_global_columns": [[i, str(c)] for i, c in sorted(coefficients.items())],
        "pure_original_roots_decoded": 0, "pure_normalization_or_solve_repeated": False,
        "R151_old_kernel_relations_recomputed": 0,
        "successful_pure_proof_consumed_without_reexecution": True,
    }
    return coefficients, {row["global_R116_column"]: row for row in labels}


def read_original_bundle(directory, spec, expected):
    """Original byte/source binding only; no response or original evaluation."""
    main = layer.read_bound_json(directory / spec["main"]["filename"], spec["main"])
    publication = layer.read_bound_json(directory / spec["receipt"]["filename"], spec["receipt"])
    if (main.get("schema") != spec["schema"] or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != spec["run"]
        or main.get("github_sha") != spec["commit"] or main.get("source_hashes") != expected):
        raise ValueError("the frozen original bundle source changed")
    metadata = (main.get("checkpoint") or {}).get(spec["metadata_key"], {})
    if (not metadata.get("persisted") or metadata.get("content_scope") != spec["scope"]
        or metadata.get("root_count") != spec["roots"]
        or any(metadata.get(k) != v for k, v in spec["export"].items())):
        raise ValueError("the published complete original export is required")
    binding = layer.check_publication(
        publication, run=spec["run"], commit=spec["commit"], lane=spec["lane"],
        driver=spec["driver"], main_name=spec["main"]["filename"], main_info=spec["main"],
        export_info=metadata,
    )
    data = layer.read_bound_export(directory / spec["export"]["filename"], metadata)
    if (data.get("schema") != spec["schema"] + "-original-expressions"
        or data.get("content_scope") != spec["scope"]
        or data.get("github_repository") != REPOSITORY
        or str(data.get("github_run_id")) != spec["run"]
        or data.get("github_sha") != spec["commit"] or data.get("source_hashes") != expected
        or len(data.get("roots", {})) != spec["roots"]):
        raise ValueError("the original DAG scope or identity changed")
    return data, {"publication": binding, "main": spec["main"], "receipt": spec["receipt"],
                  "complete_export": metadata}


def require_mixed_quartic(ring, value):
    degrees = ring.color_degrees(value)
    if degrees - MIXED_DEGREES:
        raise ValueError("an original mixed root has undeclared colors or profile degree")
    if set(blocks.ScalingGrading(ring).split(value)) - {WEIGHT}:
        raise ValueError("an original root has changed affine profile weight")


def load_mixed_originals(args, ring, coefficients, pure_labels, report):
    sources = report["source_hashes"]["completed_pure_producer"]
    family, family_info = read_original_bundle(
        args.family_directory, prior.FAMILY, sources["complete_five_family_producer"])
    if (family.get("state_coordinate_order") != ["h", "k", "omega", "logh"]
        or family.get("selected_weight") != WEIGHT
        or len(family.get("family_records", [])) != 314
        or len(family.get("selected_weight_records", [])) != 10):
        raise ValueError("the completed five-family original scope changed")
    target_row = completed.select_record(
        family["family_records"], completed.FAMILY_NAME,
        completed.STATE_KEY, completed.TARGET_HASHES)
    if (target_row.get("roots") != completed.TARGET_NAMES
        or target_row.get("profile_weights") != [WEIGHT]
        or target_row.get("requested_weight_original_mode_sha256") != completed.TARGET_HASHES):
        raise ValueError("the requested complete J6 state coefficient changed")
    name = completed.TARGET_NAMES[str(MODE)]
    target = axis.subset_decode(ring, family, [name])[name]
    if ring.digest(target) != completed.TARGET_HASHES[str(MODE)]:
        raise ValueError("the mixed J6 original root is not the source-bound root")
    require_mixed_quartic(ring, target)
    response_sources = sources["completed_pure_basis_producer"]["bound_original_inputs"][
        "weight_minus_two_producer"]
    response, response_info = read_original_bundle(
        args.response_directory, prior.RESPONSE, response_sources)
    coverage = response.get("response_coverage", {})
    records = response.get("column_records", [])
    if (not coverage.get("full_E8") or not coverage.get("all_W36")
        or coverage.get("weight") != WEIGHT or coverage.get("columns") != 50
        or len(records) != 50 or not response.get("all_compiled_original_columns_included")):
        raise ValueError("the old original weight-minus-two block is incomplete")
    mapping = prior.global_column_map(records)
    selected, names, bound_labels = {}, [], []
    for index, coefficient in sorted(coefficients.items()):
        if index not in mapping or index not in pure_labels:
            raise ValueError("a completed pure coefficient has no old full response")
        row, label = mapping[index], pure_labels[index]
        if (row.get("index") != label["weight_block_original_column"]
            or row["label"]["quadratic_index"] != label["quadratic_index"]
            or row["label"]["third_index"] != label["third_index"]
            or row["label"]["third_original_sha256"] != label["third_original_sha256"]
            or row["original_mode_sha256"]["-4"] != label["original_pure_sha256"]):
            raise ValueError("the pure identity and complete mixed root use different old columns")
        mixed_name = row["roots"][str(MODE)]
        names.append(mixed_name)
        bound_labels.append({"global_R116_column": index, "coefficient": str(coefficient),
            "original_weight_block_column": row["index"], "original_root": mixed_name,
            "original_mode_sha256": row["original_mode_sha256"], "original_label": row["label"]})
    decoded = axis.subset_decode(ring, response, names)
    for item in bound_labels:
        value = decoded[item["original_root"]]
        if ring.digest(value) != item["original_mode_sha256"][str(MODE)]:
            raise ValueError("a consumed mixed original column changed")
        require_mixed_quartic(ring, value)
        selected[item["global_R116_column"]] = value
    report["mixed_original_inputs"] = {
        "J6": family_info, "old_response_block": response_info,
        "J6_record": target_row, "selected_columns": bound_labels,
        "original_mixed_J6_sha256": ring.digest(target),
        "decoded_new_target_roots": 1, "decoded_old_mixed_roots": len(selected),
        "old_pure_roots_decoded": 0, "old_other_mixed_roots_decoded": 0,
        "old_response_generation_or_evaluation_repeated": False,
    }
    return target, selected


def project_color_degree(ring, expression, wanted=BALANCED):
    """Project actual nested right primitives, retaining their original anchors."""
    terms = {}
    for monomial, coefficient in expression.terms.items():
        ring.limits.check()
        degree = Counter()
        for atom in monomial[1]:
            degree.update(ring.atom_color_degree(atom))
        if tuple(sorted(degree.items())) == wanted:
            terms[monomial] = coefficient
    return exact.Expr(ring, terms)


def one_original_check(ring, target, originals, coefficients, args):
    combination = sum((coefficient * originals[index]
                       for index, coefficient in sorted(coefficients.items())), ring.number(0))
    difference = target - combination
    balanced = project_color_degree(ring, difference)
    normalizer = colored.ColoredNormalizer(ring, args.max_IBP_calls, args.max_terms)
    remainder = normalizer.word.expression(balanced)
    proof = {
        "mode": MODE, "bidegree": [["q", 2], ["qbar", 2]],
        "fixed_Q_coefficients_in_global_columns": [[i, str(c)] for i, c in sorted(coefficients.items())],
        "unprojected_original_difference_sha256": ring.digest(difference),
        "unprojected_original_difference_terms": len(difference.terms),
        "balanced_original_difference_sha256": ring.digest(balanced),
        "balanced_original_difference_terms": len(balanced.terms),
        "fresh_original_normal_form": normalizer.word.summary(remainder),
        "balanced_original_identity_proved": not remainder.terms,
        "nonzero_sound_remainder_is_not_nonmembership": bool(remainder.terms),
        "normalizer_sound_but_not_complete": True,
        "other_mixed_charges_not_normalized": True,
        "same_common_right_anchor": True,
        "original_word_remainder_rows": pure.word_rows(remainder),
        "normalizer_statistics": dict(normalizer.word.stats),
    }
    return combination, difference, balanced, proof


def save_certificate(args, report, ring, named, extra):
    payload = {
        "schema": SCHEMA + "-original-expressions",
        "content_scope": "one-J6-balanced-original-difference-with-completed-pure-prerequisite",
        "github_repository": report["github_repository"],
        "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
        "source_hashes": report["source_hashes"], "phase": report["phase"],
        "completed_pure_input": report.get("completed_pure_input"),
        "mixed_original_inputs": report.get("mixed_original_inputs"),
        "result": report.get("result"), **extra,
        **old.serialize_expressions(ring, named),
    }
    path = args.output.with_name(args.output.stem + "-certificate.json.gz")
    metadata = pure.store_gzip(path, payload, args.max_certificate_bytes)
    metadata.update({"content_scope": payload["content_scope"],
                     "original_root_count": len(named), "pure_rechecked": False})
    report["portable_original_certificate"] = metadata


def run_research(args, report):
    limits = exact.Limits(args.max_seconds, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.memory_mib, args.max_rational_bits)
    ring = colored.ColoredRing(limits)
    report["phase"] = "consume_successful_R160_Q_identity_without_rechecking"
    coefficients, labels = load_completed_pure(args, report)
    report["phase"] = "decode_only_one_J6_and_six_needed_old_mixed_originals"
    target, originals = load_mixed_originals(args, ring, coefficients, labels, report)
    named = {"original_J6_minus2": target}
    named.update({"original_global_%03d_minus2" % i: value for i, value in originals.items()})
    save_certificate(args, report, ring, named, {})
    report["input_regularity"] = completed.archived.dual.reachable_jet_bound(
        ring, [target] + list(originals.values()))
    report["phase"] = "one_balanced_raw_difference_and_sound_colored_IBP"
    combination, difference, balanced, proof = one_original_check(
        ring, target, originals, coefficients, args)
    named.update({"proved_pure_coefficients_applied_to_mixed": combination,
                  "raw_mixed_difference": difference,
                  "balanced_original_difference": balanced})
    report["one_balanced_proposal"] = {k: v for k, v in proof.items() if not k.endswith("_rows")}
    positive = proof["balanced_original_identity_proved"]
    report["result"] = {
        "status": "complete_J6_response_identity_proved_via_R159"
            if positive else "undecided_one_balanced_original_remainder",
        "completed_pure_identity_consumed": True,
        "balanced_original_identity_proved": positive,
        "complete_two_mode_J6_equals_exact_R160_response_combination": positive,
        "implication_source": "R159: pure zero plus balanced original zero implies the full canonical function is zero",
        "complete_J6_nonmember_proved": False,
        "kernel_or_extended_comparison_membership_searched": False,
        "new_true_cost_dimension_or_signed_control_claimed": False,
        "original_ruling_or_full_research_goal_solved": False,
    }
    report["phase"], report["completion"] = "complete_one_balanced_question", "complete"
    report["arithmetic"] = {"field": "Q", "profile_atoms": len(ring.p.atoms),
        "coefficient_nodes": len(ring.algebra.c.nodes), "limits_check_calls": limits.calls}
    save_certificate(args, report, ring, named, {"one_balanced_proposal": proof})


def artificial_toys():
    """New color/coordinate interfaces only; no published research inputs."""
    checks = {}
    labels = [{"global_R116_column": 17}, {"global_R116_column": 3}]
    proof = {"original_identity_proved": True,
        "coefficients_are_exact_Q_not_modular_lifts": True,
        "fresh_original_normal_form": {"terms": 0, "sha256": ZERO_DIGEST},
        "coefficients_in_consumed_original_positions": [[0, "2/7"], [1, "-3/11"]],
        "coefficients_in_original_global_columns": [[17, "2/7"], [3, "-3/11"]]}
    if parse_coefficients(proof, labels) != {17: F(2, 7), 3: F(-3, 11)}:
        raise AssertionError("exact local/global coefficient binding")
    for changed in (
        {**proof, "original_identity_proved": False},
        {**proof, "coefficients_are_exact_Q_not_modular_lifts": False},
        {**proof, "coefficients_in_original_global_columns": [[3, "2/7"], [17, "-3/11"]]},
        {**proof, "coefficients_in_consumed_original_positions": [[0, 0.5]]},
    ):
        try:
            parse_coefficients(changed, labels)
        except (ValueError, TypeError):
            continue
        raise AssertionError("unproved, modular, relabelled, or non-Q coefficient accepted")
    checks["exact_proved_Q_coordinates_and_original_labels_required"] = True
    limits = exact.Limits(seconds=30, nodes=12000, atoms=8000, terms=12000,
                          rewrites=30000, memory_mib=512)
    ring = colored.ColoredRing(limits)
    q, qb, x = ring.jet(), ring.color("qbar"), ring.x()
    bal = (q.D()*qb.D()).I()*q*qb
    wrong = q**4 + q**3*qb + (q*qb**3).I()
    if ring.digest(project_color_degree(ring, bal + wrong)) != ring.digest(bal):
        raise AssertionError("nested primitive colors were not counted correctly")
    checks["nested_right_primitive_bidegree_is_preserved"] = True
    for transform in (lambda e: e.D(), lambda e: e.I()):
        left = project_color_degree(ring, transform(bal + wrong))
        right = transform(project_color_degree(ring, bal + wrong))
        if ring.digest(left) != ring.digest(right):
            raise AssertionError("projection did not commute with the same-anchor linear operation")
    checks["projection_commutes_with_derivative_and_right_primitive"] = True
    raw = old.serialize_expressions(ring, {"toy_pure": q**4, "toy_mixed": bal})
    decoded = axis.subset_decode(ring, json.loads(pure.data_bytes(raw)), ["toy_mixed"])
    if set(decoded) != {"toy_mixed"} or ring.digest(decoded["toy_mixed"]) != ring.digest(bal):
        raise AssertionError("mixed-only original subset decode")
    checks["only_requested_mixed_original_roots_are_decoded"] = True
    # This raw difference is nonzero before a genuine right-collar IBP.
    z = (q*qb).D().I()*q*qb - q*q*qb*qb
    fake = argparse.Namespace(max_IBP_calls=30000, max_terms=12000)
    originals = {17: q**4 + q*q*qb*qb, 3: q**3*qb}
    coeff = {17: F(2, 7), 3: F(-3, 11)}
    combination = sum((coeff[i]*e for i, e in originals.items()), ring.number(0))
    _, difference, balanced, checked = one_original_check(
        ring, combination + z + q**4, originals, coeff, fake)
    if (not balanced.terms or not checked["balanced_original_identity_proved"]
        or not difference.terms):
        raise AssertionError("one original balanced difference did not use sound right IBP")
    checks["one_new_balanced_raw_difference_soundly_reduces_to_zero"] = True
    _, _, unresolved, pending = one_original_check(
        ring, combination + q*q*qb*qb, originals, coeff, fake)
    if pending["balanced_original_identity_proved"] or not pending["nonzero_sound_remainder_is_not_nonmembership"]:
        raise AssertionError("a nonzero sound remainder was treated as a negative theorem")
    checks["nonzero_representative_is_only_undecided"] = True
    if ring.digest(project_color_degree(ring, difference)) != ring.digest(
            project_color_degree(ring, combination + z + q**4)
            - project_color_degree(ring, combination)):
        raise AssertionError("projecting the original difference changed exact coefficients")
    checks["single_difference_projection_is_exactly_linear"] = True
    payload = old.serialize_expressions(ring, {"difference": difference,
        "balanced": balanced, "unresolved": unresolved})
    restored = old.decode_expressions(ring, json.loads(pure.data_bytes(payload)))
    if any(ring.digest(restored[name]) != ring.digest(value) for name, value in
           {"difference": difference, "balanced": balanced, "unresolved": unresolved}.items()):
        raise AssertionError("new balanced original export round trip")
    checks["new_balanced_certificate_preserves_original_hashes"] = True
    return {"checks": checks, "all_passed": all(checks.values()),
        "published_reports_or_research_roots_read": False,
        "old_pure_or_kernel_proofs_reexecuted": False,
        "research_profile_geometry_or_response_evaluated": False}


def write_main(args, report):
    raw = pure.data_bytes(report, pretty=True)
    if len(raw) > args.max_main_bytes:
        path = args.output.with_name(args.output.stem + "-complete-report.json.gz")
        metadata = pure.store_gzip(path, report, args.max_full_report_bytes)
        compact = {k: v for k, v in report.items() if k not in
                   ("completed_pure_input", "mixed_original_inputs")}
        compact["complete_report_file"] = metadata
        raw = pure.data_bytes(compact, pretty=True)
        if len(raw) > args.max_main_bytes:
            compact = {k: report.get(k) for k in ("schema", "completion", "phase", "scope",
                "github_repository", "github_run_id", "github_sha", "source_hashes", "result",
                "error", "elapsed_seconds", "peak_rss_mib", "portable_original_certificate")}
            compact["complete_report_file"] = metadata
            compact["full_result_preserved"] = True
            raw = pure.data_bytes(compact, pretty=True)
        if len(raw) > args.max_main_bytes:
            raise ValueError("the source-bound main exceeds its reserved budget")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(raw)
    return {"filename": args.output.name, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(), "completion": report["completion"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pure-directory", type=Path,
        default=TOPIC / ("notes/actions-" + PURE_RUN + "-1-" + PURE_LANE))
    parser.add_argument("--family-directory", type=Path, default=prior.directory(prior.FAMILY))
    parser.add_argument("--response-directory", type=Path, default=prior.directory(prior.RESPONSE))
    parser.add_argument("--max-seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-nodes", type=int, default=500000)
    parser.add_argument("--max-atoms", type=int, default=100000)
    parser.add_argument("--max-terms", type=int, default=120000)
    parser.add_argument("--max-IBP-calls", type=int, default=500000)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    parser.add_argument("--max-main-bytes", type=int, default=90000)
    parser.add_argument("--max-certificate-bytes", type=int, default=1500000)
    parser.add_argument("--max-full-report-bytes", type=int, default=1500000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.max_nodes, args.max_atoms,
           args.max_terms, args.max_IBP_calls, args.max_rational_bits,
           args.max_certificate_bytes, args.max_full_report_bytes) <= 0:
        parser.error("positive resource bounds are required")
    if not 10000 <= args.max_main_bytes < 100000:
        parser.error("reserve a complete source-bound main below 100KB")
    if (args.max_main_bytes + args.max_certificate_bytes + args.max_full_report_bytes
            > pure.TOTAL_OUTPUT_BYTES):
        parser.error("declared outputs exceed the reserved total byte budget")
    if not args.toy_only and not completed.actual_environment_allowed(os.environ):
        parser.error("the new balanced question is public-repository-Actions-only")
    started, code = time.monotonic(), 0
    report = {"schema": SCHEMA, "completion": "started", "phase": "bind_frozen_helpers",
        "scope": "one balanced raw J6-minus-K6 difference after the published pure identity",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {},
        "work_scope": {"new_balanced_original_differences": 0 if args.toy_only else 1,
            "new_pure_targets": 0, "new_response_formulas": 0,
            "old_31_kernel_relations_reexecuted": 0, "old_40_columns_regenerated": 0,
            "old_or_new_profile_evaluations": 0, "new_rank_or_Schur_branch": False},
        "limits": {"seconds": args.max_seconds, "memory_polling_mib": args.memory_mib,
            "nodes": args.max_nodes, "atoms": args.max_atoms, "terms": args.max_terms,
            "IBP_calls": args.max_IBP_calls, "rational_bits_guard_not_global": args.max_rational_bits,
            "main_bytes": args.max_main_bytes, "certificate_bytes": args.max_certificate_bytes,
            "full_report_bytes": args.max_full_report_bytes}}
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["phase"] = "artificial_Q_binding_color_projection_and_right_IBP"
            report["toy"] = artificial_toys()
            report["completion"] = "toy_passed"
        else:
            run_research(args, report)
    except formal.CompilationBudgetExceeded as error:
        report["completion"], report["error"], code = "resource_limit", str(error), 2
    except Exception as error:
        report["completion"], code = "implementation_check_failed", 1
        report["error"] = {"type": type(error).__name__, "message": str(error)}
    report["elapsed_seconds"] = time.monotonic() - started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    written = write_main(args, report)
    print(json.dumps({"output": str(args.output), **written}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
