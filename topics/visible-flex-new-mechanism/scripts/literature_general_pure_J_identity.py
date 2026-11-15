#!/usr/bin/env python3
"""Test one fixed general-profile pure relation for R136's acceleration J.

All seven input functions already exist as published original roots. Restore
the J root and six complete R8 response roots; form one original difference
using the published R133 tail-packet coefficients. No new response, forcing,
geometry, profile evaluation, or power-tail substitution is performed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_general_pure_G_identity as pure
import literature_acceleration_layer_mixed as layer
import literature_G_translation_successor as orbit

static, old = pure.static, pure.old
exact, colored, blocks = pure.exact, pure.colored, pure.blocks
formal, quotient = pure.formal, pure.quotient
SCHEMA = "visible-flex-general-pure-J-fixed-original-relation-v1"
REPOSITORY = pure.REPOSITORY
TOPIC = Path(pure.__file__).resolve().parents[1]
PURE_HELPER_SHA = "a6731a1c0b4940aadc689f97b9d516029518697619986aa7577b79a71ba5bcc7"
TARGET_SHA = "2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3"
TARGET_MIXED_SHA = "70f565c5c6d7075ec99bc383fc0ee66e914aff06fbc273bc3c1e431123d7c979"
STATE_KEY = (-4, 0, 0, 0)
WEIGHT = -2
COEFFICIENTS = (
    (0, F("52417629565513761/1575930037032578608")),
    (6, F("1097809599290443/196991254629072326")),
    (12, F("74015947055645095/37822320888781886592")),
    (13, F("164536405113426417/12607440296260628864")),
    (26, F("18912999385454629/3151860074065157216")),
    (34, F("-6818100659546139/787965018516289304")),
)
PROPOSAL_SOURCE = {
    "run": "43653293263", "commit": "2f0add61f44365d713abf836beaa8b0be2806a3d",
    "lane": "derivative_m8_geometry_ibp", "group": "acceleration_quadratic",
    "geometry_coefficient_index": 81,
    "geometry_key": [-4, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    "filename": "geometry-ibp-certificate.json.gz", "stored_bytes": 483512,
    "stored_sha256": "a62173b39804ab7f3b0c1f14a23f840a81813717bb8ce88d7659c0e64e90e2f1",
    "raw_bytes": 4472950,
    "raw_sha256": "3e0b01e2d7e3ed6634420524ea99ab8d4a9a56c280dd9a2da35365dca02067c7",
    "role": "only a fixed rational proposal; general identity is checked from original functions",
    "old_tail_calculation_repeated": False,
}
FAMILY = {
    "run": "43654534244", "commit": "1177f251dc3d9455adf88b585e4c0e4bd6f7e69b",
    "lane": "acceleration_layer_mixed", "schema": layer.SCHEMA,
    "driver": {"filename": "literature_acceleration_layer_mixed.py", "bytes": 47656,
        "sha256": "271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c"},
    "main": {"filename": "acceleration-layer-mixed.json", "bytes": 57753,
        "sha256": "baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745"},
    "receipt": {"filename": "receipt.json", "bytes": 35241,
        "sha256": "3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494"},
    "metadata_key": "portable_acceleration_expression_export",
    "scope": "five-complete-two-mode-normal-acceleration-families",
    "export": {"filename": "acceleration-layer-mixed-original-expressions.json.gz",
        "stored_bytes": 318634,
        "stored_sha256": "b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e",
        "raw_bytes": 1909429,
        "raw_sha256": "7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38"},
    "roots": 648,
}
RESPONSE = {
    "run": "43653293263", "commit": "2f0add61f44365d713abf836beaa8b0be2806a3d",
    "lane": "g_translation_successor", "schema": orbit.SCHEMA,
    "driver": {"filename": "literature_G_translation_successor.py", "bytes": 39670,
        "sha256": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406"},
    "main": {"filename": "G-third-translation.json", "bytes": 25014,
        "sha256": "b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3"},
    "receipt": {"filename": "receipt.json", "bytes": 34619,
        "sha256": "a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523"},
    "metadata_key": "portable_new_block_expression_export",
    "scope": "one-translation-target-and-complete-new-response-block",
    "export": {"filename": "G-third-translation-original-expressions.json.gz",
        "stored_bytes": 157782,
        "stored_sha256": "226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e",
        "raw_bytes": 889438,
        "raw_sha256": "eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7"},
    "roots": 102,
}


def directory(spec):
    return TOPIC/("notes/actions-"+spec["run"]+"-1-"+spec["lane"])


def sources():
    helper = pure.sources()
    if helper["driver"]["sha256"] != PURE_HELPER_SHA:
        raise ValueError("explicitly rebind the frozen original pure identity helpers")
    family, response = layer.source_identity(), orbit.source_identity()
    if family["driver"] != FAMILY["driver"] or response["driver"] != RESPONSE["driver"]:
        raise ValueError("the original family or response producer changed")
    return {"driver": static.identity(__file__), "pure_original_identity_helpers": helper,
        "five_family_producer": family, "weight_minus_two_producer": response}


def load_original(directory_path, spec, expected_sources, ring):
    main = layer.read_bound_json(directory_path/spec["main"]["filename"], spec["main"])
    publication = layer.read_bound_json(directory_path/spec["receipt"]["filename"], spec["receipt"])
    if (main.get("schema") != spec["schema"] or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != spec["run"]
        or main.get("github_sha") != spec["commit"]
        or main.get("source_hashes") != expected_sources):
        raise ValueError("the completed original source manifest changed")
    metadata = (main.get("checkpoint") or {}).get(spec["metadata_key"])
    if (not metadata or not metadata.get("persisted")
        or metadata.get("content_scope") != spec["scope"]
        or any(metadata.get(key) != value for key, value in spec["export"].items())
        or metadata.get("root_count") != spec["roots"]):
        raise ValueError("the complete published original-root export is required")
    binding = layer.check_publication(publication, run=spec["run"], commit=spec["commit"],
        lane=spec["lane"], driver=spec["driver"], main_name=spec["main"]["filename"],
        main_info=spec["main"], export_info=metadata)
    data = layer.read_bound_export(directory_path/spec["export"]["filename"], metadata)
    if (data.get("schema") != spec["schema"]+"-original-expressions"
        or data.get("content_scope") != spec["scope"]
        or data.get("github_repository") != REPOSITORY
        or str(data.get("github_run_id")) != spec["run"]
        or data.get("github_sha") != spec["commit"]
        or data.get("source_hashes") != expected_sources):
        raise ValueError("the original DAG differs from its bound source and scope")
    roots = old.decode_expressions(ring, data)
    if len(roots) != spec["roots"]:
        raise ValueError("an original export omitted declared roots")
    info = {"publication": binding, "main": spec["main"], "receipt": spec["receipt"],
        "complete_export": metadata, "all_original_root_hashes_verified": True,
        "original_producer_or_response_recompiled": False}
    return data, roots, info


def select_original_J(data, roots, ring):
    if (data.get("state_coordinate_order") != ["h", "k", "omega", "logh"]
        or data.get("selected_weight") != WEIGHT
        or len(data.get("family_records", [])) != 314
        or len(data.get("selected_weight_records", [])) != 10):
        raise ValueError("the complete five-family original scope changed")
    seen_names, seen_states = set(), set()
    matches = []
    for row in data["family_records"]:
        family, state = row.get("family"), tuple(row.get("state_key", []))
        if (family not in layer.FAMILIES or len(state) != 4
            or any(not isinstance(x, int) for x in state)
            or any(x < 0 for x in state[1:]) or (family, state) in seen_states):
            raise ValueError("duplicate or malformed original state record")
        seen_states.add((family, state))
        for mode in (-4, -2):
            name = row["roots"][str(mode)]
            if name in seen_names or name not in roots:
                raise ValueError("original family root missing or duplicated")
            seen_names.add(name)
            if ring.digest(roots[name]) != row["original_mode_sha256"][str(mode)]:
                raise ValueError("original family root hash changed")
        if family == "A_hh" and state == STATE_KEY:
            matches.append(row)
    selected = []
    for row in data["selected_weight_records"]:
        for mode in (-4, -2):
            name = row["roots"][str(mode)]
            if name in seen_names or name not in roots:
                raise ValueError("original selected root missing or duplicated")
            seen_names.add(name)
            if ring.digest(roots[name]) != row["original_mode_sha256"][str(mode)]:
                raise ValueError("original selected coefficient hash changed")
        if row.get("id") == 0:
            selected.append(row)
    if seen_names != set(roots) or len(matches) != 1 or len(selected) != 1:
        raise ValueError("the complete export does not identify exactly one J")
    row, chosen = matches[0], selected[0]
    hashes = {"-4": TARGET_SHA, "-2": TARGET_MIXED_SHA}
    if (row.get("profile_weights") != [WEIGHT]
        or row.get("original_mode_sha256") != hashes
        or chosen.get("original_mode_sha256") != hashes
        or chosen.get("aliases") != [{"family": "A_hh", "state_key": list(STATE_KEY)}]):
        raise ValueError("R136's one original acceleration coefficient changed")
    target = roots[row["roots"]["-4"]]
    if len(target.terms) != 80:
        raise ValueError("the exact original J_-4 term count changed")
    pure.require_degree(ring, target, "q", 4)
    if set(blocks.ScalingGrading(ring).split(target)) != {WEIGHT}:
        raise ValueError("J is not the stated complete pure homogeneous root")
    return target, {"family": "A_hh", "state_key": list(STATE_KEY),
        "profile_affine_weight": WEIGHT, "mode": -4,
        "ungraded_root": row["roots"]["-4"], "selected_root": chosen["roots"]["-4"],
        "original_sha256": TARGET_SHA, "original_terms": len(target.terms),
        "whole_state_root_already_homogeneous": True,
        "matrix_N2_and_normalization_corrections_do_not_change_this_acceleration_family": True}


def global_column_map(records):
    """R116 global ID is 8*third+quadratic, not the weight-block row index."""
    answer = {}
    for row in records:
        label = row["label"]
        i, j = label["quadratic_index"], label["third_index"]
        if (not isinstance(i, int) or not isinstance(j, int)
            or not 0 <= i < 8 or not 0 <= j < 36):
            raise ValueError("invalid true quadratic/third label")
        index = 8*j+i
        if index in answer:
            raise ValueError("duplicate original quadratic/third pair")
        answer[index] = row
    return answer


def select_original_responses(data, roots, ring):
    coverage = data.get("response_coverage") or {}
    records = data.get("column_records") or []
    expected = [(i, j) for i, wi in enumerate(blocks.PARAMETER_WEIGHTS)
        for j, wj in enumerate(blocks.THIRD_WEIGHTS) if wi+wj == WEIGHT]
    if (not coverage.get("full_E8") or not coverage.get("all_W36")
        or coverage.get("weight") != WEIGHT or coverage.get("columns") != 50
        or len(records) != 50 or len(expected) != 50
        or not data.get("all_compiled_original_columns_included")):
        raise ValueError("the complete original weight-minus-two block is required")
    used = set()
    for index, (row, pair) in enumerate(zip(records, expected)):
        label = row["label"]
        if (row.get("index") != index
            or (label.get("quadratic_index"), label.get("third_index")) != pair
            or label.get("third_weight") != blocks.THIRD_WEIGHTS[pair[1]]
            or label.get("v2_original_third_index") != blocks.EXPECTED_KEPT[pair[1]]):
            raise ValueError("the full E8/W36 original column enumeration changed")
        for mode in (-4, -2):
            name = row["roots"][str(mode)]
            if name in used or name not in roots:
                raise ValueError("an original response root is missing or duplicated")
            used.add(name)
            if ring.digest(roots[name]) != row["original_mode_sha256"][str(mode)]:
                raise ValueError("the exact original response root changed")
    for mode in (-4, -2):
        name = data["target_roots"][str(mode)]
        if name in used or name not in roots:
            raise ValueError("the archived translation root is missing or duplicated")
        used.add(name)
    if used != set(roots):
        raise ValueError("undeclared roots in the original response export")
    mapping = global_column_map(records)
    selected, labels = {}, []
    grade = blocks.ScalingGrading(ring)
    for index, coefficient in COEFFICIENTS:
        if index not in mapping:
            raise ValueError("the fixed R133 proposal refers outside this true weight block")
        row = mapping[index]
        name = row["roots"]["-4"]
        value = roots[name]
        pure.require_degree(ring, value, "q", 4, allow_zero=True)
        if set(grade.split(value))-{WEIGHT}:
            raise ValueError("a selected original pure response has the wrong weight")
        selected[index] = value
        labels.append({"global_R116_column": index, "weight_block_column": row["index"],
            "coefficient": str(coefficient), "label": row["label"],
            "original_root": name, "original_pure_sha256": ring.digest(value),
            "original_terms": len(value.terms)})
    return selected, labels


def original_difference(ring, target, columns, coefficients):
    result = target
    for index, coefficient in coefficients:
        if index not in columns:
            raise ValueError("a fixed original response is missing")
        result = result-coefficient*columns[index]
    return result


def run_research(args, report):
    limits = exact.Limits(args.max_seconds, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.memory_mib, args.max_rational_bits)
    ring = colored.ColoredRing(limits)
    report["phase"] = "restore_one_published_acceleration_coefficient"
    data, roots, family_info = load_original(args.family_directory, FAMILY,
        report["source_hashes"]["five_family_producer"], ring)
    target, target_info = select_original_J(data, roots, ring)
    report["input_family"] = family_info
    report["original_J"] = target_info
    report["phase"] = "restore_six_already_published_pure_response_roots"
    response_data, response_roots, response_info = load_original(args.response_directory, RESPONSE,
        report["source_hashes"]["weight_minus_two_producer"], ring)
    columns, labels = select_original_responses(response_data, response_roots, ring)
    report["input_response"] = response_info
    report["phase"] = "one_fixed_general_profile_original_difference"
    difference = original_difference(ring, target, columns, COEFFICIENTS)
    pure.require_degree(ring, difference, "q", 4, allow_zero=True)
    if set(blocks.ScalingGrading(ring).split(difference))-{WEIGHT}:
        raise ValueError("the fixed original difference left its true weight block")
    report["fixed_comparison"] = {
        "formula": "J[-4] - sum(a_i * original_R116_column_i[-4])",
        "mode": -4, "profile_affine_weight": WEIGHT,
        "target_original_sha256": TARGET_SHA,
        "coefficients": [[i, str(c)] for i, c in COEFFICIENTS],
        "selected_original_columns": labels,
        "proposal_source": PROPOSAL_SOURCE,
        "target_original_terms": len(target.terms),
        "difference_original_terms": len(difference.terms),
        "difference_original_sha256": ring.digest(difference),
        "new_pure_response_formulas": 0, "new_mixed_response_formulas": 0,
        "new_profile_evaluations": 0, "new_tail_substitutions": 0,
        "old_rank_or_original_dependency_checks_recomputed": 0,
        "old_forcing_W_v4_or_N_responses_compiled": 0,
        "primitive_values_assigned_independently": False,
        "no_extra_phase_factor_applied": True}
    named = {"original_J_minus4": target, "original_fixed_difference": difference}
    named.update({"original_response_"+str(i): value for i, value in columns.items()})
    certificate = {"schema": SCHEMA+"-original-expressions",
        "content_scope": "one general pure J difference with six consumed original response roots",
        "source_hashes": report["source_hashes"],
        "input_family": family_info, "input_response": response_info,
        "fixed_comparison": report["fixed_comparison"], **old.serialize_expressions(ring, named)}
    path = args.output.with_name(args.output.stem+"-certificate.json.gz")
    report["portable_original_certificate"] = pure.store_gzip(path, certificate, args.max_certificate_bytes)
    report["phase"] = "one_sound_original_difference_reduction"
    normalizer = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    reduced = normalizer.expression(difference)
    positive = not reduced.terms
    report["result"] = {
        "status": "original_identity_proved" if positive else "unresolved_nonzero_representative",
        "arbitrary_profile_pure_identity_proved": positive,
        "normal_form": normalizer.word.summary(reduced),
        "original_difference_reduced_directly": True,
        "normalizer_sound_but_not_complete": True,
        "pure_function_nonmembership_proved": False,
        "complete_two_mode_identity_proved": False,
        "all_general_pure_costs_in_response_range_proved": False,
        "true_cost_sign_or_signed_realizability_claimed": False,
        "left_endpoint_or_period_reset": False}
    report["normalizer_statistics"] = {
        "right_IBP": normalizer.legacy.stats, "word": normalizer.word.stats}
    certificate["result"] = report["result"]
    certificate["normalizer_statistics"] = report["normalizer_statistics"]
    certificate["entire_reduced_word_expression"] = pure.word_rows(reduced)
    certificate["nonzero_representative_is_not_function_nonmembership"] = True
    report["portable_original_certificate"] = pure.store_gzip(path, certificate, args.max_certificate_bytes)
    report["coefficient_arithmetic"] = {"field": "Q", "profile_atoms": len(ring.p.atoms),
        "coefficient_nodes": len(ring.algebra.c.nodes), "limits_check_calls": limits.calls}
    report["phase"] = "complete_fixed_original_comparison"
    report["completion"] = "complete"


def artificial_toys():
    # Only the newly introduced raw-column mapping and fixed linear comparison.
    records = [{"index": 0, "label": {"quadratic_index": 5, "third_index": 2}},
               {"index": 1, "label": {"quadratic_index": 2, "third_index": 4}}]
    mapping = global_column_map(records)
    if set(mapping) != {21, 34} or mapping[34]["index"] != 1:
        raise AssertionError("global and homogeneous-block indices were confused")
    duplicate_rejected = False
    try:
        global_column_map(records+[records[0]])
    except ValueError:
        duplicate_rejected = True
    if not duplicate_rejected:
        raise AssertionError("duplicate genuine operator labels must be rejected")
    limits = exact.Limits(seconds=20, nodes=3000, atoms=1000, terms=3000,
        rewrites=10000, memory_mib=512)
    ring = colored.ColoredRing(limits)
    q = ring.jet()
    columns = {21: q**4, 34: q*q*q.D()*q.D()}
    coefficients = ((21, F(7, 13)), (34, F(-11, 17)))
    target = coefficients[0][1]*columns[21]+coefficients[1][1]*columns[34]
    norm = quotient.ProfileNormalizer(ring, 10000, 3000)
    if norm.expression(original_difference(ring, target, columns, coefficients)).terms:
        raise AssertionError("fixed exact rational signs or original columns changed")
    if not norm.expression(original_difference(ring, target+q**4, columns, coefficients)).terms:
        raise AssertionError("an unmatched original term was silently discarded")
    return {"checks": {"global_ID_versus_weight_block_ID": True,
        "duplicate_original_pair_rejected": True,
        "exact_signed_linear_combination_and_unmatched_term": True},
        "all_passed": True, "published_research_DAG_loaded": False,
        "research_target_or_profile_evaluated": False,
        "old_development_or_research_query_repeated": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--family-directory", type=Path, default=directory(FAMILY))
    parser.add_argument("--response-directory", type=Path, default=directory(RESPONSE))
    parser.add_argument("--max-seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-nodes", type=int, default=400000)
    parser.add_argument("--max-atoms", type=int, default=100000)
    parser.add_argument("--max-terms", type=int, default=100000)
    parser.add_argument("--max-IBP-calls", type=int, default=250000)
    parser.add_argument("--max-rational-bits", type=int, default=8192)
    parser.add_argument("--max-main-bytes", type=int, default=90000)
    parser.add_argument("--max-certificate-bytes", type=int, default=2500000)
    parser.add_argument("--max-full-report-bytes", type=int, default=2000000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.max_nodes, args.max_atoms, args.max_terms,
        args.max_IBP_calls, args.max_rational_bits, args.max_certificate_bytes,
        args.max_full_report_bytes) <= 0:
        parser.error("positive finite resource bounds required")
    if not 10000 <= args.max_main_bytes < 100000:
        parser.error("reserve 10000..99999 bytes for the source-bound main")
    if args.max_main_bytes+args.max_certificate_bytes+args.max_full_report_bytes > pure.TOTAL_OUTPUT_BYTES:
        parser.error("declared complete output exceeds the reserved byte bound")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("the genuine original symbolic comparison is public-Actions-only")
    start, code = time.monotonic(), 0
    report = {"schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "scope": "one general pure acceleration J relation; no mixed recomputation or full pure-range claim",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {}, "limits": {"seconds": args.max_seconds,
            "memory_polling_mib": args.memory_mib, "nodes": args.max_nodes,
            "atoms": args.max_atoms, "terms": args.max_terms, "IBP_calls": args.max_IBP_calls,
            "rational_bits": args.max_rational_bits, "main_bytes": args.max_main_bytes,
            "certificate_bytes": args.max_certificate_bytes,
            "full_report_bytes": args.max_full_report_bytes},
        "pure_function_nonmembership_proved": False,
        "finite_isometric_family_constructed": False}
    try:
        report["source_hashes"] = sources()
        if args.toy_only:
            report["phase"] = "small_new_artificial_interfaces"
            report["toy"] = artificial_toys()
            report["completion"] = "toy_passed"
        else:
            run_research(args, report)
    except formal.CompilationBudgetExceeded as error:
        report["completion"] = "resource_limit"
        report["error"] = str(error)
        code = 2
    except Exception as error:
        report["completion"] = "implementation_check_failed"
        report["error"] = {"type": type(error).__name__, "message": str(error)}
        code = 1
    report["elapsed_seconds"] = time.monotonic()-start
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written = pure.write_main(args, report)
    if written["completion"] == "output_limit":
        code = 2
    print(json.dumps({"output": str(args.output), **written}), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
