#!/usr/bin/env python3
"""Check one prescribed rational point against the published 86-row system.

No LP, RREF, profile expression, original query or path integral is evaluated.
The same archived coordinate map supplies all 107 coordinates, fourteen
coefficient families and the R164 multiplier.  R175/R177 applicability is
checked by exact coefficient comparisons, including all stored degrees.
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

import literature_character_minus2_literal_relation_cuts as raw9

old = raw9.inherited
base = raw9.base
REPOSITORY = raw9.REPOSITORY
SCHEMA = "visible-flex-character-minus2-raw-positive-candidate-v1"
PARENT_SCHEMA = raw9.SCHEMA
PARENT = {
    "run": "43671759155",
    "commit": "26e00d13bc72d2a6d581019b83a2415dd804a7fb",
    "lane": "character_minus2_literal_relation_cuts",
    "report": {"filename": "character-minus2-literal-relation-cuts.json", "bytes": 6961,
        "sha256": "f7c371df8ee3d9faac42a9fd66c392e7397c4065ee773a69072b6ac4807c0881"},
    "publication": {"filename": "receipt.json", "bytes": 40896,
        "sha256": "2d4108f8ead23669957edb24f9f621e60647f266e9fae162cecdd01f60010722"},
    "certificate": {"filename": "character-minus2-literal-relation-cuts-certificate.json.gz",
        "stored_bytes": 12478,
        "stored_sha256": "cf9a5df3eb3914c3bd5dd53b8b79839b42d87c100af744ea70f6327d5d6eb544",
        "raw_bytes": 59431,
        "raw_sha256": "afa554873c635a265275605f7518f774334c08d925c66a028b2a67da5534c1d5"},
    "driver": {"filename": "literature_character_minus2_literal_relation_cuts.py", "bytes": 31639,
        "sha256": "1861db94d22ffb1a7c4e96319fb9fe18fed9121a0d1edfeb20f83e22290aa4f0"},
}
FREE_NORMAL_INDICES = (2, 3, 14, 23, 26, 28, 38, 43, 58, 63, 67, 69, 73,
                       90, 91, 94, 96, 97, 99, 100, 101, 103, 104)
PRESCRIBED_POINT = ("1/4", "0", "-1", "1", "0", "1/4", "0", "-1", "1", "1", "0", "1", "-1/4",
                    "1", "1/4", "-1/4", "1/16", "1/12", "-1/8", "0", "-1/12", "1", "1/4")
EXPECTED_FAMILIES = {
    "F0": {0: "1/4", 2: "1/2", 4: "1/4"},
    "Q2_0": {0: "1", 2: "1/4"}, "Q2_1": {3: "-1"},
    "Q2_2": {0: "1", 2: "1", 4: "1"},
    "A_hh": {0: "1", 2: "1/4"}, "A_hk": {1: "-1/4"}, "A_kk": {0: "1/16"},
    "H1": {1: "1/12"}, "H2": {0: "-1/8"},
    "Q4_0": {}, "Q4_1": {}, "Q4_2": {}, "Q4_3": {1: "-1/12"}, "Q4_4": {0: "1", 2: "1/4"},
}
EXPECTED_SCALARS = {
    "normalized_multiplier": ["0", "1/2", "2", "0", "0", "0", "0", "2"],
    "translation_c": ["0"] * 8,
    "scaling_d": ["0", "1", "6", "0", "0", "0", "0", "4"],
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(path):
    path = Path(path); raw = path.read_bytes()
    return {"filename": path.name, "bytes": len(raw), "sha256": sha(raw)}


def source_identity():
    if identity(raw9.__file__) != PARENT["driver"]:
        raise ValueError("the published raw9 source changed")
    return {"driver": identity(__file__), "published_raw9_producer": PARENT["driver"],
        "frozen_reused_dependencies": raw9.source_identity(),
        "original_function_or_head_modules_imported": False}


def check_publication(publication, main, raw_main, spec=PARENT, schema=PARENT_SCHEMA):
    if (publication.get("schema") != "visible-new-mechanism-actions-v1"
        or publication.get("repository") != REPOSITORY
        or str(publication.get("run_id")) != spec["run"]
        or publication.get("source_commit") != spec["commit"]
        or publication.get("lane") != spec["lane"]):
        raise ValueError("published 86-row receipt identity changed")
    if (main.get("schema") != schema or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != spec["run"]
        or main.get("github_sha") != spec["commit"]
        or main.get("source_hashes", {}).get("driver") != spec["driver"]
        or main.get("target_weight") != -2):
        raise ValueError("the exact complete 86-row main is required")
    rows = publication.get("outputs", [])
    outputs = {Path(row["path"]).name: row for row in rows}
    if len(outputs) != len(rows):
        raise ValueError("ambiguous published output basenames")
    rec = outputs.get(spec["report"]["filename"], {})
    if rec.get("bytes") != len(raw_main) or rec.get("sha256") != sha(raw_main):
        raise ValueError("receipt does not bind main bytes")
    metadata = main.get("complete_necessary_certificate", {})
    if any(metadata.get(k) != v for k, v in spec["certificate"].items()):
        raise ValueError("complete 86-row certificate metadata changed")
    rec = outputs.get(spec["certificate"]["filename"], {})
    for left, right in (("bytes", "stored_bytes"), ("sha256", "stored_sha256"),
                        ("raw_bytes", "raw_bytes"), ("raw_sha256", "raw_sha256")):
        if rec.get(left) != spec["certificate"][right]:
            raise ValueError("receipt does not bind both compressed/raw certificate identities")
    producers = [value for key, value in publication.get("source_files", {}).items()
                 if Path(key).name == spec["driver"]["filename"]]
    if len(producers) != 1 or any(producers[0].get(k) != spec["driver"][k] for k in ("bytes", "sha256")):
        raise ValueError("receipt does not bind the frozen input producer")


def consume(args, report, budget):
    main, raw_main = old.read_small(args.source_report, PARENT["report"])
    publication, _ = old.read_small(args.source_publication, PARENT["publication"])
    check_publication(publication, main, raw_main)
    current = old.read_gzip(args.source_certificate, PARENT["certificate"], budget)
    original = old.read_gzip(args.original_system_certificate, old.archived.PREVIOUS["certificate"], budget)
    if (current.get("schema") != PARENT_SCHEMA + "-certificate"
        or current.get("source_hashes") != main.get("source_hashes")
        or current.get("github_repository") != REPOSITORY
        or str(current.get("github_run_id")) != PARENT["run"]
        or current.get("github_sha") != PARENT["commit"]
        or current.get("input") != main.get("input")
        or current.get("literal_input") != main.get("literal_input")
        or current.get("target_weight") != -2
        or current.get("all_true_positive_weight_minus2_characters_embed_in_this_outer_system") is not True
        or current.get("true_functional_well_definedness_claimed") is not False
        or current.get("old_RREF_paths_or_original_function_relations_recomputed") is not False):
        raise ValueError("complete raw9 certificate scope or identity changed")
    if (original.get("schema") != base.SCHEMA + "-certificate"
        or original.get("source_hashes", {}).get("driver") != old.archived.PREVIOUS["driver"]
        or original.get("target_weight") != -2
        or original.get("all_true_positive_characters_embed_in_this_outer_system") is not True):
        raise ValueError("original complete 107-coordinate/14-family source is required")
    input_original = main.get("input", {})
    if (input_original.get("original_complete_system_certificate") != old.archived.PREVIOUS["certificate"]
        or input_original.get("original_complete_system_run") != old.archived.PREVIOUS["run"]
        or input_original.get("original_complete_system_source") != old.archived.PREVIOUS["commit"]):
        raise ValueError("raw9 does not bind the same original complete coordinate system")
    binds = {
        "old_transform_sha256": original["normal_coordinates_as_free_linear_forms"],
        "old_complete_fourteen_coefficient_forms_sha256": original["corrected_scalar_k_polynomials"],
        "old_multiplier_forms_sha256": {key: original[key] for key in (
            "normalized_multiplier", "translation_c", "scaling_d")},
    }
    if any(current.get(key) != sha(canonical(value)) for key, value in binds.items()):
        raise ValueError("same published B, fourteen forms and multiplier forms are required")
    if (current.get("normal_coordinate_count") != 107 or original.get("normal_coordinate_count") != 107
        or tuple(current.get("free_normal_coordinates", [])) != FREE_NORMAL_INDICES
        or current["free_normal_coordinates"] != original.get("free_normal_coordinates")):
        raise ValueError("the original 23/107 coordinate meanings changed")
    table = current.get("updated_reduced_inequalities", [])
    if (len(table) != 86 or table[:63] != original.get("reduced_inequalities")
        or sha(canonical(table[:68])) != current.get("old_68_row_prefix_sha256")
        or current.get("old_68_row_prefix_sha256") != main.get("increment", {}).get("unchanged_68_row_prefix_sha256")):
        raise ValueError("the complete unchanged 86-row inventory is required")
    addition = current.get("new_published_equalities", {})
    relations = addition.get("relations", [])
    if ([x.get("relation_index") for x in relations] != list(raw9.SELECTED_RELATIONS)
        or addition.get("selected_relation_count") != 9 or addition.get("new_distinct_halfspaces") != 18
        or addition.get("row_count_before") != 68 or addition.get("row_count_after") != 86
        or addition.get("all_equalities_use_both_signs") is not True):
        raise ValueError("all nine published original relations are required")
    for item in relations:
        proof = item.get("fresh_original_check", {})
        if (proof.get("all_modes_exact_original_zero") is not True
            or set(proof.get("mode_checks", {})) != {"-4", "-2"}
            or any(value.get("remaining_terms") != 0 for value in proof["mode_checks"].values())):
            raise ValueError("a relation lacks its previously published two-mode zero check")
    report["input"] = {"parent": deepcopy(PARENT),
        "original_complete_system_certificate": deepcopy(old.archived.PREVIOUS["certificate"]),
        "original_complete_system_run": old.archived.PREVIOUS["run"],
        "original_complete_system_source": old.archived.PREVIOUS["commit"],
        "same_old_transform_and_all_fourteen_forms_consumed": True,
        "source_original_relation_flags_consumed_not_reproved": True}
    return original, current


def evaluate_point(original, records, relations, raw_point, budget):
    dimension = len(original["free_normal_coordinates"])
    point = list(map(F, raw_point))
    if len(point) != dimension or not any(point) or any(abs(x) > 1 for x in point):
        raise ValueError("one nonzero rational point in the unchanged full normalization box is required")
    transform, forms, static_support = old.transformed_families(original, budget)
    normal = [base.apply_row(row, point) for row in transform]
    values = old.evaluate_saved_families(forms, point, budget)
    rows = old.verify_rows(records, point, budget)
    relation_values = {str(item["relation_index"]):
        str(base.apply_row(base.read_row(item["old_free_coordinate_equality"], dimension), point))
        for item in relations}
    scalars = {key: [str(base.apply_row(base.read_row(row, len(normal)), normal)) for row in original[key]]
               for key in ("normalized_multiplier", "translation_c", "scaling_d")}
    return {"free_coordinate_values": list(map(str, point)),
        "normal_coordinate_values": list(map(str, normal)),
        "complete_fourteen_scalar_family_values": old.serialize_polynomials(values),
        "same_R164_multiplier_and_cocycles": scalars,
        "inequality_verification": rows, "all_nine_exact_equality_values": relation_values,
        "all_nine_equalities_satisfied_exactly": all(F(v) == 0 for v in relation_values.values()),
        "all_107_generating_coordinates_covered": len(normal) == original["normal_coordinate_count"],
        "static_support_verification": static_support,
        "only_an_exact_outer_necessary_system_point": True,
        "true_functional_well_definedness_proved": False}


def parse_families(raw, names=None):
    names = tuple(base.FAMILIES) if names is None else tuple(names)
    if set(raw) != set(names):
        raise ValueError("all stored families must be consumed together")
    out = {}
    for family in names:
        out[family] = {}; seen = set()
        for degree, value in raw[family]:
            if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0 or degree in seen:
                raise ValueError("invalid or repeated stored polynomial degree")
            seen.add(degree)
            if isinstance(value, (float, bool)):
                raise ValueError("coefficient comparison requires exact rationals")
            value = F(value)
            if value:
                out[family][degree] = value
    return out


def expected_family_matches(raw, expected=EXPECTED_FAMILIES):
    actual = parse_families(raw, expected)
    return {name: actual[name] == {d: F(c) for d, c in terms.items() if F(c)}
            for name, terms in expected.items()}


def highest_matrix(values):
    names = ("a", "b", "c", "d", "e", "f", "g", "j", "ell", "m")
    if set(values) != set(names):
        raise ValueError("all ten same-candidate highest coefficients are required")
    a, b, c, d, e, f, g, j, ell, m = (F(values[key]) for key in names)
    residuals = (c+b, d-b/4, e+2*b/3+2*f,
                 j+4*b/3+2*f+4*g, m-3*b-4*f-4*g)
    A, B, C = b/4, 3*b/4+3*f/2, 23*b/12+2*f+g
    det = A*C-B*B
    psd = (A > 0 and det >= 0) or (A == 0 and B == 0 and C >= 0)
    return {"ten_coefficients": {name: str(F(values[name])) for name in names},
        "five_raw_relation_residuals": list(map(str, residuals)),
        "five_raw_relations_satisfied": not any(residuals),
        "matrix": [[str(A), str(B)], [str(B), str(C)]], "determinant": str(det),
        "a": str(a), "ell_plus_25_a_over_9": str(ell+25*a/9),
        "matrix_PSD_exact": psd,
        "complete_highest_layer_nonnegative": not any(residuals) and a >= 0 and ell+25*a/9 >= 0 and psd}


def prescribed_action_certificate(interpretation):
    raw = interpretation["complete_fourteen_scalar_family_values"]
    families = parse_families(raw); matches = expected_family_matches(raw)
    get = lambda family, degree: families[family].get(degree, F(0))
    values = {"a": get("A_hh", 0), "b": get("A_hh", 2), "c": get("A_hk", 1),
        "d": get("A_kk", 0), "e": get("H1", 1), "f": get("H2", 0),
        "g": get("Q4_2", 0), "j": get("Q4_3", 1), "ell": get("Q4_4", 0), "m": get("Q4_4", 2)}
    highest = highest_matrix(values)
    multiplier_match = interpretation["same_R164_multiplier_and_cocycles"] == EXPECTED_SCALARS
    all_match = all(matches.values())
    return {"matches_all_prescribed_fourteen_polynomials": matches,
        "same_prescribed_multiplier_and_cocycles": multiplier_match,
        "R175_matrix_check": highest,
        "static_identity": "a(k)=(1+k^2)^2/4>=1/4",
        "Q2_identity": "h^-2*(k_s^2+(1+k^2)*r_s^2+k^2*(k_s-2*k*r_s)^2/4)",
        "highest_integral_identity": "integral(exp(-2r)*((r_ss-2*r_s^2/3)^2+34*r_s^4/9)+psi_s^2/16+11*(r_s*psi)^2/48)",
        "highest_identity_flat_boundary_required": True,
        "r_definition": "log(h)", "psi_definition": "h*D_s(k/h^2)",
        "uniform_complete_action_lower_bound": "integral(h^-2 ds)/4",
        "R175_R177_proved_identities_are_applicable": all_match and multiplier_match and highest["complete_highest_layer_nonnegative"],
        "path_integrals_or_Gram_optimization_recomputed": False,
        "all_stored_degrees_compared_including_zero_and_wrong_parity_entries": True,
        "scalar_action_certificate_is_not_a_true_head_functional_certificate": True}


def actual(args, report, ctx, budget):
    report["phase"] = "consume_bound_86_row_system_and_complete_archived_forms"
    original, current = consume(args, report, budget)
    records = current["updated_reduced_inequalities"]
    relations = current["new_published_equalities"]["relations"]
    immutable = sha(canonical(current))
    report["phase"] = "one_prescribed_rational_point_evaluation_without_LP"
    interpretation = evaluate_point(original, records, relations, PRESCRIBED_POINT, budget)
    action = prescribed_action_certificate(interpretation)
    if sha(canonical(current)) != immutable:
        raise AssertionError("the read-only check mutated the complete parent certificate")
    expected_matrix = [["1/16", "0"], ["0", "11/48"]]
    matrix_match = action["R175_matrix_check"]["matrix"] == expected_matrix
    passed = (interpretation["inequality_verification"]["all_rows_satisfied_exactly"]
        and interpretation["all_nine_equalities_satisfied_exactly"]
        and interpretation["all_107_generating_coordinates_covered"]
        and action["R175_R177_proved_identities_are_applicable"] and matrix_match)
    ctx.update(interpretation=interpretation, action=action,
        inherited_86_rows=deepcopy(records), inherited_nine_equalities=deepcopy(relations),
        unchanged_86_rows_sha256=sha(canonical(records)),
        inherited_complete_certificate_sha256=immutable,
        free_normal_coordinates=list(original["free_normal_coordinates"]),
        original_transform_sha256=current["old_transform_sha256"],
        original_complete_forms_sha256=current["old_complete_fourteen_coefficient_forms_sha256"])
    report.update(completion="complete", phase="prescribed_86_row_positive_scalar_point_complete",
        outcome=("prescribed_outer_point_passes_86_rows_nine_relations_and_complete_scalar_action_certificate"
                 if passed else "prescribed_outer_point_fails_at_least_one_bound_row_or_coefficient_check"),
        prescribed_outer_point_verified=passed, positive_character_excluded=False,
        true_positive_character_constructed=False, complete_functional_relations_paid=False)
    report["prescribed_23_coordinates"] = list(PRESCRIBED_POINT)
    report["inequality_verification"] = {key: value for key, value in interpretation["inequality_verification"].items() if key != "values"}
    report["nine_equality_values"] = interpretation["all_nine_exact_equality_values"]
    report["fourteen_scalar_families"] = interpretation["complete_fourteen_scalar_family_values"]
    report["unique_multiplier_and_cocycles"] = interpretation["same_R164_multiplier_and_cocycles"]
    report["scalar_action_certificate"] = action
    report["checkpoint"] = {"same_23_and_107_coordinates_preserved": True,
        "all_86_archived_halfspaces_and_nine_original_equalities_consumed": True,
        "original_function_relations_beyond_the_published_nine_unpaid": True,
        "no_new_necessary_halfspace_added": True, "no_LP_or_RREF_or_path_integral": True,
        "no_head_or_original_function_evaluation": True,
        "true_positive_character_or_full_research_task_completed": False}


def toy_only():
    budget = base.Budget(30, 256, 16384); checks = {}
    forbidden_names = ("rref", "construct_system", "path_integrals", "certify_zero")
    saved = {name: getattr(base, name) for name in forbidden_names}
    def forbidden(*_args, **_kwargs):
        raise AssertionError("new specified-point check called an old research or LP entry")
    try:
        for name in forbidden_names:
            setattr(base, name, forbidden)
        original = {"normal_coordinate_count": 3, "free_normal_coordinates": [0, 1],
            "normal_coordinates_as_free_linear_forms": [[[0, "1"]], [[1, "1"]], [[0, "2"], [1, "-1"]]],
            "corrected_scalar_k_polynomials": {name: [[0, [[0, "1"]]], [2, [[2, "1"]]]] for name in base.FAMILIES},
            "normalized_multiplier": [[[2, "1"]]] + [[] for _ in range(7)],
            "translation_c": [[] for _ in range(8)], "scaling_d": [[] for _ in range(8)]}
        records = [{"index": 0, "coefficients": [[0, "1"]]}, {"index": 1, "coefficients": [[1, "1"]]}]
        relations = [{"relation_index": 3, "old_free_coordinate_equality": [[0, "1"], [1, "-2"]]}]
        before = sha(canonical([original, records, relations]))
        out = evaluate_point(original, records, relations, ["1", "1/2"], budget)
        assert out["normal_coordinate_values"] == ["1", "1/2", "3/2"]
        assert out["all_nine_equalities_satisfied_exactly"]
        assert out["same_R164_multiplier_and_cocycles"]["normalized_multiplier"][0] == "3/2"
        assert len(out["complete_fourteen_scalar_family_values"]) == 14
        checks["invented_same_point_supplies_all_coordinates_fourteen_families_and_multiplier"] = True
        assert sha(canonical([original, records, relations])) == before
        checks["inherited_rows_relations_and_coordinate_forms_are_not_mutated"] = True
        out_bad = evaluate_point(original, records, relations, ["-1", "1/2"], budget)
        assert out_bad["inequality_verification"]["negative_row_indices"] == [0]
        assert not out_bad["all_nine_equalities_satisfied_exactly"]
        checks["a_negative_archived_halfspace_and_a_nonzero_equality_are_retained_as_failures"] = True
        supplied = {"invented": [[0, "2"], [2, "0"]]}
        assert expected_family_matches(supplied, {"invented": {0: "2"}})["invented"]
        supplied["invented"].append([7, "1/1000000000000"])
        assert not expected_family_matches(supplied, {"invented": {0: "2"}})["invented"]
        checks["all_saved_polynomial_degrees_are_compared_without_dropping_unexpected_terms"] = True
        try:
            parse_families({"invented": [[0, "1"], [0, "0"]]}, ["invented"])
        except ValueError:
            checks["duplicate_zero_polynomial_degrees_are_rejected"] = True
        else:
            raise AssertionError("duplicate stored polynomial degree was silently accepted")
        # A scaled invented matrix case; not the prescribed actual coordinate point.
        v = {"a": 3, "b": 4, "c": -4, "d": 1, "e": F(4,3), "f": -2,
             "g": 0, "j": F(-4,3), "ell": 2, "m": 4}
        mat = highest_matrix(v)
        assert mat["matrix"] == [["1", "0"], ["0", "11/3"]]
        assert mat["complete_highest_layer_nonnegative"]
        changed = dict(v, c=-3)
        assert not highest_matrix(changed)["complete_highest_layer_nonnegative"]
        checks["R175_matrix_and_all_five_raw_relations_are_separately_required"] = True
        bad = deepcopy(original); bad["corrected_scalar_k_polynomials"]["F0"].append([3, [[0, "1"]]])
        try:
            evaluate_point(bad, records, relations, ["1", "1/2"], budget)
        except ValueError:
            checks["unexpected_nonzero_odd_static_support_is_not_truncated"] = True
        else:
            raise AssertionError("unexpected static support was ignored")
        checks["old_LP_RREF_system_and_path_generation_entries_are_not_called"] = True
    finally:
        for name, value in saved.items():
            setattr(base, name, value)
    if not all(checks.values()):
        raise AssertionError("an artificial specified-point interface check failed")
    return {"all_passed": True, "checks": checks, "invented_rational_data_only": True,
        "actual_prescribed_point_or_published_data_evaluated": False,
        "old_development_or_research_repeated": False, "LP_or_path_integral_called": False}


def certificate(report, ctx):
    if "interpretation" not in ctx:
        return None
    return {"schema": SCHEMA + "-certificate", "source_hashes": report["source_hashes"],
        "github_repository": report["github_repository"], "github_run_id": report["github_run_id"],
        "github_sha": report["github_sha"], "target_weight": -2,
        "input": report["input"], "prescribed_point": list(PRESCRIBED_POINT),
        **deepcopy(ctx),
        "all_original_function_relations_paid": False,
        "a_true_positive_character_constructed": False,
        "scalar_SOS_applicability_does_not_establish_functional_well_definedness": True}


def write_outputs(args, report, cert):
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if cert is not None:
        raw = canonical(cert) + b"\n"; packed = gzip.compress(raw, mtime=0)
        if len(packed) > args.max_certificate_bytes:
            raise base.Limit("specified-point complete certificate exceeds its output budget")
        path = args.output.with_name(args.output.stem + "-certificate.json.gz"); path.write_bytes(packed)
        report["complete_candidate_certificate"] = {"filename": path.name,
            "stored_bytes": len(packed), "stored_sha256": sha(packed),
            "raw_bytes": len(raw), "raw_sha256": sha(raw),
            "content_scope": "one-prescribed-point-all-86-rows-nine-equalities-and-fourteen-complete-families"}
    raw = canonical(report) + b"\n"
    if len(raw) > args.max_main_bytes:
        raise base.Limit("specified-point small report exceeds its output budget")
    args.output.write_bytes(raw)
    return {"output": str(args.output), "completion": report["completion"],
            "bytes": len(raw), "sha256": sha(raw)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    for name in ("source-report", "source-publication", "source-certificate", "original-system-certificate"):
        parser.add_argument("--" + name, type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-seconds", type=float, default=60)
    parser.add_argument("--memory-mib", type=int, default=256)
    parser.add_argument("--rational-bits", type=int, default=16384)
    parser.add_argument("--max-main-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=4500000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.rational_bits, args.max_main_bytes, args.max_certificate_bytes) <= 0:
        parser.error("all resource limits must be positive")
    if args.max_main_bytes >= 100000 or args.max_main_bytes + args.max_certificate_bytes > 4800000:
        parser.error("main must be below100KB and all outputs at most4.8MB")
    paths = (args.source_report, args.source_publication, args.source_certificate, args.original_system_certificate)
    if not args.toy_only and not all(paths):
        parser.error("all four published input files are required")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS") != "true"
                              or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        parser.error("actual specified-point arithmetic only in this public repository Actions")
    started = time.monotonic(); budget = base.Budget(args.max_seconds, args.memory_mib, args.rational_bits)
    report = {"schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"), "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"), "source_hashes": {}, "target_weight": -2,
        "positive_character_excluded": False, "true_positive_character_constructed": False,
        "LP_RREF_original_function_query_or_path_integral_performed": False,
        "limits": {"elapsed_seconds": args.max_seconds, "polled_memory_mib": args.memory_mib,
            "rational_bit_ceiling": args.rational_bits, "main_bytes": args.max_main_bytes,
            "certificate_bytes": args.max_certificate_bytes}}
    ctx = {}; code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["toy"] = toy_only()
            report.update(completion="toy_passed", phase="new_artificial_specified_point_interface")
        else:
            actual(args, report, ctx, budget)
    except base.Limit as error:
        code = 2; report.update(completion="resource_limit", error=str(error))
    except Exception as error:
        code = 1; report.update(completion="implementation_check_failed",
            error={"type": type(error).__name__, "message": str(error)})
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    try:
        written = write_outputs(args, report, certificate(report, ctx))
    except base.Limit as error:
        code = 2
        fallback = {key: report[key] for key in ("schema", "phase", "github_repository", "github_run_id",
            "github_sha", "source_hashes", "target_weight", "elapsed_seconds", "peak_rss_mib") if key in report}
        fallback.update(completion="output_limit", error=str(error), positive_character_excluded=False,
            true_positive_character_constructed=False, complete_candidate_certificate_not_saved=True)
        raw = canonical(fallback)+b"\n"; args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_bytes(raw)
        written = {"output": str(args.output), "completion": "output_limit", "bytes": len(raw), "sha256": sha(raw)}
    print(json.dumps(written), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
