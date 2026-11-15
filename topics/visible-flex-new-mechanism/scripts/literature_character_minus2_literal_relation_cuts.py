#!/usr/bin/env python3
"""Append the nine published fresh literal identities to the old 23-coordinate test.

Consume the archived 68 necessary halfspaces and the complete coefficient forms.
Do not regenerate the head, its old RREF, any path integral, or any original
function relation.  New work is the small augmented necessary system only.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_character_minus2_static_positive_candidate as inherited

base = inherited.base
SCHEMA = "visible-flex-character-minus2-literal-relation-cuts-v1"
REPOSITORY = inherited.REPOSITORY
INHERITED_HELPER = {
    "filename": "literature_character_minus2_static_positive_candidate.py",
    "bytes": 35719,
    "sha256": "644b2897d142964fea9e6b0a11348d6c1eef9be93af1514e06a4d10ae652fa45",
}
LITERAL = {
    "run": "43670254711",
    "commit": "952cf7927d809150ac2579f1a390225c2cf23f52",
    "lane": "character_head_literal_relations",
    "schema": "visible-flex-character-head-literal-relations-v1",
    "report": {"filename": "character-head-literal-relations.json", "bytes": 7103,
        "sha256": "0d3351e00b434292b7b8fce62ac74096ea0fbb96cdf78998bb096d29ab336055"},
    "publication": {"filename": "receipt.json", "bytes": 41254,
        "sha256": "043a234f7cf4c8962d50edc69a441794f562041e2fbf334c8ad570335ae42d73"},
    "certificate": {"filename": "character-head-literal-relations-certificate.json.gz",
        "stored_bytes": 41109,
        "stored_sha256": "5d929f4f45265ee4eec949eace228bf4b639753cd0a4b24a8a3d32d0857dc62e",
        "raw_bytes": 269605,
        "raw_sha256": "ed3bedb70a0f49a058daf578ff9403a7ff89407c55f0954f876bfedaeaeac775"},
    "driver": {"filename": "literature_character_head_literal_relations.py", "bytes": 58885,
        "sha256": "80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995"},
}
SELECTED_RELATIONS = (0, 4, 35, 55, 62, 64, 65, 66, 67)
NEW_STATUS = "new_exact_equality_modulo_archived_map_R168_and_earlier_relations"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path); raw = path.read_bytes()
    return {"filename": path.name, "bytes": len(raw), "sha256": sha(raw)}


def source_identity():
    if identity(inherited.__file__) != INHERITED_HELPER:
        raise ValueError("the published archived-input helper changed")
    dependencies = inherited.source_identity()
    return {"driver": identity(__file__), "archived_input_helper": INHERITED_HELPER,
        "frozen_reused_dependencies": dependencies,
        "literal_original_function_or_head_modules_imported": False}


def check_literal_publication(publication, main, raw_main):
    if (publication.get("schema") != "visible-new-mechanism-actions-v1"
        or publication.get("repository") != REPOSITORY
        or str(publication.get("run_id")) != LITERAL["run"]
        or publication.get("source_commit") != LITERAL["commit"]
        or publication.get("lane") != LITERAL["lane"]):
        raise ValueError("published original-relation receipt identity changed")
    if (main.get("schema") != LITERAL["schema"] or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != LITERAL["run"]
        or main.get("github_sha") != LITERAL["commit"]
        or main.get("source_hashes", {}).get("driver") != LITERAL["driver"]
        or main.get("target_weight") != -2):
        raise ValueError("the completed original-relation main is required")
    outputs = publication.get("outputs", [])
    by_name = {Path(row["path"]).name: row for row in outputs}
    if len(by_name) != len(outputs):
        raise ValueError("ambiguous published output basenames")
    old = by_name.get(LITERAL["report"]["filename"], {})
    if old.get("bytes") != len(raw_main) or old.get("sha256") != sha(raw_main):
        raise ValueError("receipt does not bind the original-relation main")
    metadata = main.get("fresh_original_relation_certificate", {})
    if any(metadata.get(k) != v for k, v in LITERAL["certificate"].items()):
        raise ValueError("published exact relation certificate metadata changed")
    old = by_name.get(metadata["filename"], {})
    for out_key, meta_key in (("bytes", "stored_bytes"), ("sha256", "stored_sha256"),
                              ("raw_bytes", "raw_bytes"), ("raw_sha256", "raw_sha256")):
        if old.get(out_key) != metadata[meta_key]:
            raise ValueError("receipt does not bind both packed/raw relation bytes")
    producers = [value for key, value in publication.get("source_files", {}).items()
                 if Path(key).name == LITERAL["driver"]["filename"]]
    if len(producers) != 1 or any(producers[0].get(k) != LITERAL["driver"][k]
                                   for k in ("bytes", "sha256")):
        raise ValueError("receipt does not bind the frozen original-relation producer")
    comparison = main.get("literal_comparison", {})
    if (comparison.get("completed_columns") != 147
        or comparison.get("fresh_original_dependencies") != 70
        or comparison.get("new_equalities_after_archived_B_and_R168") != 9
        or comparison.get("functional_kernel_complete_claimed") is not False
        or metadata.get("all_relations_have_fresh_two_mode_original_zero_checks") is not True):
        raise ValueError("not the completed, explicitly scoped original-relation result")


def consume_literal(args, report, original, current, budget):
    main, raw_main = inherited.read_small(args.literal_report, LITERAL["report"])
    publication, _ = inherited.read_small(args.literal_publication, LITERAL["publication"])
    check_literal_publication(publication, main, raw_main)
    data = inherited.read_gzip(args.literal_certificate, LITERAL["certificate"], budget)
    if (data.get("schema") != LITERAL["schema"] + "-certificate"
        or data.get("source_hashes") != main.get("source_hashes")
        or str(data.get("github_run_id")) != LITERAL["run"]
        or data.get("github_sha") != LITERAL["commit"]
        or data.get("github_repository") != REPOSITORY or data.get("target_weight") != -2
        or data.get("all_147_columns_processed") is not True
        or data.get("all_dependency_certificates_freshly_checked_in_both_original_modes") is not True
        or data.get("true_function_space_rank_computed") is not False):
        raise ValueError("exact original-relation certificate semantics changed")
    view = data["inherited_view"]
    if sha(canonical(view)) != data.get("inherited_view_sha256"):
        raise ValueError("archived coordinate-view digest mismatch")
    binds = {
        "old_equalities_sha256": original["equalities"],
        "old_rref_sha256": original["rref_equalities"],
        "old_normal_to_free_sha256": original["normal_coordinates_as_free_linear_forms"],
        "old_63_halfspaces_sha256": original["reduced_inequalities"],
        "updated_68_halfspaces_sha256": current["updated_reduced_inequalities"],
    }
    if any(view.get(key) != sha(canonical(value)) for key, value in binds.items()):
        raise ValueError("new relations were not projected through the same archived coordinates")
    if (view.get("free_normal_coordinates") != original["free_normal_coordinates"]
        or view.get("finite", {}).get("artifact") != inherited.archived.PREVIOUS["certificate"]
        or view.get("parity", {}).get("artifact") != inherited.CURRENT["certificate"]):
        raise ValueError("original-relation input chain changed")
    old_parity = current["complete_quadratic_parity"]["wrong_parity_coefficient_rows"]
    expected_parity = [{key: row[key] for key in (
        "family", "degree", "normal_coordinate_linear_form", "free_coordinate_equality")}
        for row in old_parity]
    if view.get("inherited_parity") != expected_parity:
        raise ValueError("the exact inherited R168 relations changed")
    metadata = data.get("column_metadata", [])
    if (len(metadata) != 147 or data.get("column_order") != "R40 first, then normal107"
        or [row["original_metadata"] for row in metadata[40:]]
           != original["normal_coordinate_metadata"]):
        raise ValueError("original normal-column meanings do not match the old coordinate map")
    if data.get("new_equalities_for_the_inherited_23_coordinates") != list(SELECTED_RELATIONS):
        raise ValueError("the complete published list of nine new relations changed")
    if len(data.get("original_dependencies", [])) != 70:
        raise ValueError("the complete published relation inventory changed")
    report["literal_input"] = deepcopy(LITERAL)
    report["literal_input"]["inherited_view_sha256"] = data["inherited_view_sha256"]
    report["literal_input"]["source_certificate_flags_are_consumed_not_reproved"] = True
    return data


def selected_relations(data, total_columns, response_count, normal_count, free_count, indices):
    """Validate serialized meanings, not the already-published original identities."""
    if len(set(indices)) != len(indices) or list(indices) != sorted(indices):
        raise ValueError("new relation indices must be distinct and ordered")
    result = []
    for index in indices:
        record = data["original_dependencies"][index]
        if record.get("relation_index") != index or record.get("new_row_status") != NEW_STATUS:
            raise ValueError("an unproved or previously redundant relation was substituted")
        dense = record["dense_147_original_coefficients"]
        if len(dense) != total_columns:
            raise ValueError("wrong original coefficient-vector length")
        parsed = [F(value) for value in dense]
        if any(value.denominator != 1 for value in parsed):
            raise ValueError("published primitive integer original relation changed")
        sparse = {j: value for j, value in enumerate(parsed) if value}
        if base.read_row(record["original_column_coefficients"], total_columns) != sparse:
            raise ValueError("dense/sparse original relation mismatch")
        normal = {j-response_count: value for j, value in sparse.items() if j >= response_count}
        if (normal_count != total_columns-response_count
            or base.read_row(record["normal_coordinate_equality"], normal_count) != normal):
            raise ValueError("response-zero versus normal coordinates were confused")
        free = base.read_row(record["old_free_coordinate_equality"], free_count)
        if not free or not record.get("residual_after_known_equalities"):
            raise ValueError("a declared new independent equality has an empty published row")
        proof = record.get("fresh_original_check", {})
        if (proof.get("all_modes_exact_original_zero") is not True
            or set(proof.get("mode_checks", {})) != {"-4", "-2"}
            or any(check.get("remaining_terms") != 0 for check in proof["mode_checks"].values())):
            raise ValueError("both original mode-zero certificates are required")
        result.append({"relation_index": index,
            "old_free_coordinate_equality": deepcopy(record["old_free_coordinate_equality"]),
            "normal_coordinate_equality": deepcopy(record["normal_coordinate_equality"]),
            "dense_147_original_coefficients": list(dense),
            "original_column_coefficients": deepcopy(record["original_column_coefficients"]),
            "fresh_original_check": deepcopy(proof),
            "source_record_sha256": sha(canonical(record))})
    return result


def append_relations(table, relations, dimension, budget):
    old = deepcopy(table.records); old_sha = sha(canonical(old)); old_count = len(old)
    appended = []
    for relation in relations:
        row = base.read_row(relation["old_free_coordinate_equality"], dimension)
        budget.check(row); signs = []
        for sign in (1, -1):
            signed = base.row_add((row, sign)); normalized = base.primitive(signed, equality=False)
            if not normalized:
                raise ValueError("a declared new relation normalized to zero")
            key = tuple(sorted(normalized.items()))
            if key in table.keys:
                row_index, status = table.keys[key], "already_present_without_mutation"
            else:
                reason = {"kind": "published_fresh_two_mode_literal_equality",
                    "source_relation_index": relation["relation_index"],
                    "equality_as_halfspace_sign": sign,
                    "source_certificate_raw_sha256": LITERAL["certificate"]["raw_sha256"]}
                row_index, status = table.add(normalized, reason), "new"
            signs.append({"sign": sign, "reduced_row_index": row_index, "status": status,
                          "signed_free_linear_form": base.serial_row(signed)})
        appended.append({**deepcopy(relation), "two_halfspaces": signs})
    if table.records[:old_count] != old or sha(canonical(old)) != old_sha:
        raise AssertionError("adding the nine true equalities changed the archived 68-row prefix")
    return {"selected_relation_count": len(relations), "row_count_before": old_count,
        "row_count_after": len(table.records), "new_distinct_halfspaces": len(table.records)-old_count,
        "unchanged_68_row_prefix_sha256": old_sha, "all_equalities_use_both_signs": True,
        "relations": appended, "old_RREF_or_relation_projection_recomputed": False}


def candidate_interpretation(data, current, system, relations, decision, budget):
    raw = decision.get("outer_candidate")
    if raw is None:
        return None
    point = list(map(F, raw)); dimension = len(system["free"])
    if len(point) != dimension or not any(point) or any(abs(v) > 1 for v in point):
        raise AssertionError("the new exact outer point lacks its complete box normalization")
    values = [base.apply_row(row, point) for row in system["reduced"].rows]
    if any(value < 0 for value in values):
        raise AssertionError("new outer candidate violates a saved exact halfspace")
    equality_values = {str(record["relation_index"]):
        str(base.apply_row(base.read_row(record["old_free_coordinate_equality"], dimension), point))
        for record in relations}
    if any(F(value) for value in equality_values.values()):
        raise AssertionError("a necessary opposite halfspace pair was not respected")
    transform = [base.read_row(row, dimension)
                 for row in data["normal_coordinates_as_free_linear_forms"]]
    normal = [base.apply_row(row, point) for row in transform]
    family_values = {}
    for family in base.FAMILIES:
        family_values[family] = []
        for degree, row in data["corrected_scalar_k_polynomials"][family]:
            value = base.apply_row(base.read_row(row, len(normal)), normal)
            budget.check({0: value}); family_values[family].append([degree, str(value)])
    scalar_values = {name: [str(base.apply_row(base.read_row(row, len(normal)), normal))
        for row in data[name]] for name in ("normalized_multiplier", "translation_c", "scaling_d")}
    return {"free_coordinate_values": list(map(str, point)),
        "normal_coordinate_values": list(map(str, normal)),
        "complete_fourteen_scalar_family_values": family_values,
        "same_R164_multiplier_and_cocycles": scalar_values,
        "all_updated_halfspace_values": list(map(str, values)),
        "all_nine_exact_equality_values": equality_values,
        "all_107_generating_coordinates_are_covered": len(normal) == data["normal_coordinate_count"],
        "unchanged_old_family_forms_sha256": sha(canonical(data["corrected_scalar_k_polynomials"])),
        "only_an_exact_outer_necessary_system_point": True,
        "true_functional_well_definedness_proved": False,
        "old_R172_R173_SOS_is_not_automatically_inherited": True}


def actual(args, report, ctx, budget):
    report["phase"] = "read_archived_68_rows_and_complete_normal_coefficient_forms"
    original, current = inherited.consume(args, report, budget)
    literal = consume_literal(args, report, original, current, budget)
    selected = selected_relations(literal, 147, 40, 107, 23, SELECTED_RELATIONS)
    table = inherited.archived.inherited_table(current["updated_reduced_inequalities"], 23, budget)
    system = {"free": list(original["free_normal_coordinates"]), "reduced": table}
    ctx.update(system=system, original=original, current=current)
    report["phase"] = "append_only_the_nine_published_original_equalities"
    addition = append_relations(table, selected, 23, budget); ctx["addition"] = addition
    report["increment"] = {key: value for key, value in addition.items() if key != "relations"}
    report["increment"]["selected_original_relation_indices"] = list(SELECTED_RELATIONS)
    report["phase"] = "augmented_small_system_exact_dual_or_exact_outer_point"
    print(json.dumps({"phase": report["phase"], "unchanged_free_coordinates": 23,
        "inherited_rows": 68, "new_exact_equalities": 9,
        "new_distinct_halfspaces": addition["new_distinct_halfspaces"]}), flush=True)
    decision = base.certify_zero(system, budget); ctx["decision"] = decision
    interpretation = candidate_interpretation(original, current, system, selected, decision, budget)
    if interpretation is not None:
        ctx["candidate_interpretation"] = interpretation
    excluded = decision["all_coordinates_forced_zero"]
    report.update(completion="complete", phase="nine_literal_equalities_continuation_complete",
        positive_character_excluded=excluded,
        outcome=("all_nonzero_true_positive_weight_minus2_characters_excluded_by_exact_augmented_system"
                 if excluded else "literal_relation_augmented_outer_system_remains_unresolved"))
    report["decision"] = {key: value for key, value in decision.items()
                          if key not in ("certificates", "outer_candidate")}
    report["decision"]["exact_dual_certificate_count"] = len(decision.get("certificates", []))
    report["decision"]["exact_outer_candidate_saved"] = interpretation is not None
    if interpretation is not None:
        report["candidate_fourteen_scalar_families"] = interpretation["complete_fourteen_scalar_family_values"]
        report["candidate_multiplier_and_cocycles"] = interpretation["same_R164_multiplier_and_cocycles"]
    report["checkpoint"] = {"target_weight": -2,
        "all_true_positive_characters_embed_in_the_augmented_outer_system": True,
        "original_23_coordinates_and_all_107_generators_preserved": True,
        "all_nine_new_published_relations_consumed": True,
        "literal_rank_not_used_as_true_function_rank": True,
        "old_RREF_or_path_integrals_or_literal_elimination_recomputed": False,
        "new_original_function_queries_performed": False,
        "true_functional_well_definedness_claimed": False,
        "only_weight_minus2_positive_characters_excluded": excluded,
        "all_weights_positive_characters_excluded": False,
        "complete_period_or_ruling_paid": False}


def fake_relation(index, dense, free):
    sparse = [[j, str(value)] for j, value in enumerate(dense) if value]
    return {"relation_index": index, "new_row_status": NEW_STATUS,
        "dense_147_original_coefficients": list(map(str, dense)),
        "original_column_coefficients": sparse,
        "normal_coordinate_equality": [[j-1, str(value)] for j, value in enumerate(dense) if j and value],
        "old_free_coordinate_equality": free, "residual_after_known_equalities": free,
        "fresh_original_check": {"all_modes_exact_original_zero": True,
            "mode_checks": {str(mode): {"remaining_terms": 0} for mode in (-4, -2)}}}


def toy_only():
    checks = {}; budget = base.Budget(30, 512)
    names = ("rref", "construct_system", "path_integrals")
    saved = {name: getattr(base, name) for name in names}
    def forbidden(*_args, **_kwargs):
        raise AssertionError("new incremental code attempted old research")
    try:
        for name in names:
            setattr(base, name, forbidden)
        toy = {"original_dependencies": [fake_relation(0, [2, -1, 1], [[0, "-1"], [1, "1"]]),
                                          fake_relation(1, [0, 1, 0], [[0, "1"]])]}
        before = sha(canonical(toy))
        selected = selected_relations(toy, 3, 1, 2, 2, (0, 1))
        table = base.RowTable(budget); table.add(base.unit(0), {"kind": "invented_old_row"})
        old = deepcopy(table.records)
        addition = append_relations(table, selected, 2, budget)
        checks["both_signs_of_every_new_published_equality_are_present"] = all(
            [s["sign"] for s in row["two_halfspaces"]] == [1, -1] for row in addition["relations"])
        checks["one_existing_halfspace_is_reused_without_mutating_its_record"] = (
            table.records[:1] == old and addition["relations"][1]["two_halfspaces"][0]["status"]
            == "already_present_without_mutation")
        checks["input_relation_records_are_immutable"] = sha(canonical(toy)) == before
        # x=0 and y-x=0 prove both signs of both coordinates using only exact additions.
        target_x = base.unit(0); target_y = base.unit(1)
        posx = table.keys[tuple(sorted(target_x.items()))]
        negx = table.keys[tuple(sorted(base.row_add((target_x, -1)).items()))]
        rel = {0: F(-1), 1: F(1)}
        posrel = table.keys[tuple(sorted(rel.items()))]
        negrel = table.keys[tuple(sorted(base.row_add((rel, -1)).items()))]
        assert base.verify_farkas(table.rows, target_y, {posx: F(1), posrel: F(1)})
        assert base.verify_farkas(table.rows, base.row_add((target_y, -1)), {negx: F(1), negrel: F(1)})
        assert not base.verify_farkas(table.rows, target_y, {negx: F(1), posrel: F(1)})
        checks["invented_exact_dual_identity_accepts_correct_signs_and_rejects_wrong_sign"] = True
        for label, change in (
            ("one_mode_nonzero_certificate_is_rejected", lambda d: d["original_dependencies"][0]["fresh_original_check"]["mode_checks"]["-2"].update(remaining_terms=1)),
            ("dense_sparse_original_relation_mismatch_is_rejected", lambda d: d["original_dependencies"][0]["dense_147_original_coefficients"].__setitem__(0, "3")),
            ("ambiguous_normal_coordinate_projection_is_rejected", lambda d: d["original_dependencies"][0]["normal_coordinate_equality"].__setitem__(0, [0, "1"]))):
            bad = deepcopy(toy); change(bad)
            try:
                selected_relations(bad, 3, 1, 2, 2, (0, 1))
            except ValueError:
                checks[label] = True
            else:
                raise AssertionError("malformed original certificate accepted")
        data = {"normal_coordinate_count": 2,
            "normal_coordinates_as_free_linear_forms": [[[0, "1"]], [[1, "1"]]],
            "corrected_scalar_k_polynomials": {name: [[0, [[0, "1"]]]] for name in base.FAMILIES},
            "normalized_multiplier": [[]] * 8, "translation_c": [[]] * 8, "scaling_d": [[]] * 8}
        one = base.RowTable(budget); one.add({0: F(1)}, {"kind": "invented_bound"})
        interpretation = candidate_interpretation(data, {}, {"free": [0, 1], "reduced": one}, [],
                                                   {"outer_candidate": ["1", "0"]}, budget)
        assert interpretation["only_an_exact_outer_necessary_system_point"]
        assert not interpretation["true_functional_well_definedness_proved"]
        checks["new_candidate_is_labelled_outer_only_with_all_fourteen_saved_forms"] = (
            len(interpretation["complete_fourteen_scalar_family_values"]) == 14)
        checks["old_RREF_path_and_system_generation_are_never_called"] = True
    finally:
        for name, value in saved.items():
            setattr(base, name, value)
    if not all(checks.values()):
        raise AssertionError("an invented incremental-system check failed")
    return {"checks": checks, "all_passed": True, "artificial_rational_data_only": True,
        "real_published_system_or_relation_files_read": False,
        "old_artificial_suites_or_old_research_repeated": False,
        "new_LP_solver_run_locally": False}


def complete_certificate(report, ctx):
    if "system" not in ctx:
        return None
    original = ctx["original"]; current = ctx["current"]
    return {"schema": SCHEMA + "-certificate", "source_hashes": report["source_hashes"],
        "github_repository": report["github_repository"], "github_run_id": report["github_run_id"],
        "github_sha": report["github_sha"], "target_weight": -2,
        "input": report.get("input"), "literal_input": report.get("literal_input"),
        "free_normal_coordinates": ctx["system"]["free"],
        "normal_coordinate_count": original["normal_coordinate_count"],
        "old_transform_sha256": sha(canonical(original["normal_coordinates_as_free_linear_forms"])),
        "old_complete_fourteen_coefficient_forms_sha256": sha(canonical(original["corrected_scalar_k_polynomials"])),
        "old_multiplier_forms_sha256": sha(canonical({name: original[name] for name in (
            "normalized_multiplier", "translation_c", "scaling_d")})),
        "old_68_row_prefix_sha256": sha(canonical(current["updated_reduced_inequalities"])),
        "new_published_equalities": ctx.get("addition"),
        "updated_reduced_inequalities": ctx["system"]["reduced"].records,
        "decision": ctx.get("decision"), "candidate_interpretation": ctx.get("candidate_interpretation"),
        "all_true_positive_weight_minus2_characters_embed_in_this_outer_system": True,
        "full_original_certificate_required_to_interpret_normal_coordinates": True,
        "literal_rank_is_not_true_function_rank": True,
        "true_functional_well_definedness_claimed": False,
        "old_RREF_paths_or_original_function_relations_recomputed": False}


def write_outputs(args, report, certificate):
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if certificate is not None:
        raw = canonical(certificate) + b"\n"; packed = gzip.compress(raw, mtime=0)
        if len(packed) > args.max_certificate_bytes:
            raise base.Limit("complete augmented-system certificate exceeds its output budget")
        path = args.output.with_name(args.output.stem + "-certificate.json.gz")
        path.write_bytes(packed)
        report["complete_necessary_certificate"] = {"filename": path.name,
            "stored_bytes": len(packed), "stored_sha256": sha(packed),
            "raw_bytes": len(raw), "raw_sha256": sha(raw),
            "content_scope": "unchanged-23-coordinates-and-68-rows-plus-nine-fresh-original-equalities"}
    raw = canonical(report) + b"\n"
    if len(raw) > args.max_main_bytes:
        raise base.Limit("small augmented-system main exceeds its output budget")
    args.output.write_bytes(raw)
    return {"output": str(args.output), "completion": report["completion"],
            "bytes": len(raw), "sha256": sha(raw)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    for name in ("source-report", "source-publication", "source-certificate", "original-system-certificate",
                 "literal-report", "literal-publication", "literal-certificate"):
        parser.add_argument("--" + name, type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=180)
    parser.add_argument("--memory-mib", type=int, default=512)
    parser.add_argument("--rational-bits", type=int, default=16384)
    parser.add_argument("--max-main-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=4500000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.rational_bits, args.max_main_bytes, args.max_certificate_bytes) <= 0:
        parser.error("all resource budgets must be positive")
    if args.max_main_bytes >= 100000 or args.max_main_bytes + args.max_certificate_bytes > 4800000:
        parser.error("main must be below100KB and total outputs at most4.8MB")
    required = (args.source_report, args.source_publication, args.source_certificate,
                args.original_system_certificate, args.literal_report, args.literal_publication,
                args.literal_certificate)
    if not args.toy_only and not all(required):
        parser.error("all seven exact published input paths are required")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS") != "true"
                              or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        parser.error("actual necessary-system continuation only in this public repository Actions")
    started = time.monotonic(); budget = base.Budget(args.max_seconds, args.memory_mib, args.rational_bits)
    report = {"schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "source_hashes": {}, "target_weight": -2, "positive_character_excluded": False,
        "true_positive_character_constructed": False,
        "theorem_prerequisites": ["R163", "R164", "R168", "published_raw147_fresh_original_identities"],
        "old_RREF_path_integrals_literal_elimination_or_44_column_queries_recomputed": False,
        "new_head_or_original_function_evaluations_performed": False,
        "limits": {"elapsed_seconds": args.max_seconds, "polled_memory_mib": args.memory_mib,
                   "rational_bit_ceiling": args.rational_bits, "main_bytes": args.max_main_bytes,
                   "certificate_bytes": args.max_certificate_bytes}}
    ctx = {}; code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["toy"] = toy_only()
            report.update(completion="toy_passed", phase="new_artificial_incremental_relation_tests")
        else:
            actual(args, report, ctx, budget)
    except base.Limit as error:
        code = 2; report.update(completion="resource_limit", error=str(error))
    except Exception as error:
        code = 1; report.update(completion="implementation_check_failed",
            error={"type": type(error).__name__, "message": str(error)})
    report["elapsed_seconds"] = time.monotonic() - started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    try:
        written = write_outputs(args, report, complete_certificate(report, ctx))
    except base.Limit as error:
        code = 2
        fallback = {key: report[key] for key in ("schema", "phase", "github_repository", "github_run_id",
            "github_sha", "source_hashes", "target_weight", "elapsed_seconds", "peak_rss_mib") if key in report}
        fallback.update(completion="output_limit", error=str(error), positive_character_excluded=False,
            true_positive_character_constructed=False, complete_augmented_certificate_not_saved=True)
        raw = canonical(fallback) + b"\n"; args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(raw)
        written = {"output": str(args.output), "completion": "output_limit", "bytes": len(raw), "sha256": sha(raw)}
    print(json.dumps(written), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
