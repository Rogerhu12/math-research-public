#!/usr/bin/env python3
"""Read only the ended R815 two-known-column checkpoint's small source-bound diagnostics.

This program imports no mathematical core and does not recompute any lattice,
residue, reconstruction, multiplier, or exact commutator.  Large source carriers
remain in their original one-day checkpoint artifact.
"""
import argparse
import collections
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys

REPOSITORY = "Rogerhu12/math-research-public"
RESULT = "R815-original-normal-derivation-operators"
FINAL = "p41-original-normal-derivation-operator-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R815-retained-producer-inputs.tar.gz"
HELPER_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
CORE_SHA = "0008796890a0cfcf0b9aaaa40e26f0d8d26be38f8168c8fe918d86a7585a0ec1"
WRAPPER_SHA = "58d65088e16469651d9895b5fa3e8f93bd0f9c8db309852d1bf6d68b753bf8cd"
METHOD_SHA = "c373d52ed9f39f221ddb0674087930c44284ede22b559d9151c7e49a6fe99bf9"
MODE = "two-known-columns-and-three-dimensional-Q-common-denominator"
KNOWN = "R815-two-known-columns-exact-original-input.json.gz"
IMPORTED = "R815-two-known-columns-imported-scalar-scan.json.gz"
PREVIOUS_RECEIPT = "R815-two-columns-previous-scan-input-receipt.json"
PREVIOUS_BUNDLE = "R815-two-columns-previous-scan-inputs.tar.gz"
ROOT = Path(__file__).resolve().parents[1]
PAIR = re.compile(r"R815-projective-probe-pair-([0-9]{6})[.]json[.]gz")
LLL = re.compile(r"R815-projective-pair-([0-9]{6})-weight-(plus|minus)([0-9]+)-LLL[.]json[.]gz")
DEFINITION = re.compile(r"(R815-projective-g-candidate-[0-9a-f]{32})-definition[.]json[.]gz")
EARLY = re.compile(r"(R815-projective-g-candidate-[0-9a-f]{32})-early-exact-entry-([0-9]{2})[.]json[.]gz")
REJECTION = re.compile(r"(R815-projective-g-candidate-[0-9a-f]{32})-rejected[.]json[.]gz")
H64 = re.compile(r"[0-9a-f]{64}")
MAX_MEMBER = 16*1024*1024
MAX_TOTAL = 192*1024*1024
MAX_JSON = 96*1024*1024


def guard():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPOSITORY


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def save(path, value):
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    path = Path(path)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rb") as stream:
        raw = stream.read(MAX_JSON+1)
    assert len(raw) <= MAX_JSON, "Unexpected large diagnostics JSON; not a small-member review."
    return json.loads(raw)


def plain(entry):
    answer = {key: entry[key] for key in ("file", "bytes", "sha256")}
    assert Path(answer["file"]).name == answer["file"]
    assert type(answer["bytes"]) is int and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def spec(path):
    return {"file": Path(path).name, "bytes": Path(path).stat().st_size, "sha256": sha(path)}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def decimal_metadata(value):
    """Integer representation metadata only: no lattice or field arithmetic."""
    assert isinstance(value, str) and re.fullmatch(r"-?[0-9]+", value)
    absolute = value.removeprefix("-").lstrip("0") or "0"
    return {"decimal_digits": len(absolute), "is_zero": absolute == "0",
            "negative": value.startswith("-") and absolute != "0",
            "integer_bit_length": int(value).bit_length(),
            "integer_text_sha256": hashlib.sha256(value.encode()).hexdigest()}


def source_spec(source):
    return {key: source[key] for key in (
        "result", "run_id", "source_commit", "core_sha256", "artifact_id",
        "artifact_name", "archive_bytes", "archive_sha256", "expected_conclusion")}


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)
    assert item["reader_sha256"] == sha(__file__)
    source = item["source"]
    assert source["result"] == RESULT and source["core_sha256"] == CORE_SHA
    assert str(source["run_id"]) == "43755027718"
    assert source["source_commit"] == "e1d8a95631eb11d1df0ccba4a781b05b6dd45c62"
    assert source["expected_conclusion"] == "failure"
    helper_path = ROOT/"scripts/R824_public_original_global_polar_generators.py"
    assert sha(helper_path) == HELPER_SHA
    module_spec = importlib.util.spec_from_file_location("R815_two_known_columns_ended_range_IO", helper_path)
    helper = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(helper)
    out = args.output
    original = out/"original"
    original.mkdir(parents=True, exist_ok=True)
    archive = helper.Archive(source, out/"range-transfer", whole=False)
    try:
        def unique_small(name):
            members = archive.by_name.get(name, [])
            assert len(members) == 1 and members[0].file_size <= MAX_MEMBER
            with archive.zip.open(members[0]) as stream:
                raw = stream.read(MAX_MEMBER+1)
            assert len(raw) == members[0].file_size
            path = original/name
            path.write_bytes(raw)
            return path

        reference_path = unique_small(REFERENCE)
        reference = read(reference_path)
        assert reference["result"] == RESULT
        assert reference["manifest_file"] == "full-outputs-manifest.json"
        assert H64.fullmatch(reference["manifest_sha256"])
        manifest_path = archive.extract_bound(
            reference["manifest_file"], reference["manifest_sha256"],
            original/reference["manifest_file"], reference["manifest_bytes"])
        if source.get("manifest_sha256") is not None:
            assert sha(manifest_path) == source["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == RESULT
        files = {entry["file"]: plain(entry) for entry in manifest["files"]}
        assert len(files) == len(manifest["files"]) == reference["file_count"]
        assert set(archive.by_name) == set(files) | {REFERENCE, "full-outputs-manifest.json"}
        for name, entry in files.items():
            members = archive.by_name[name]
            assert len(members) == 1 and members[0].file_size == entry["bytes"]
        mandatory = {
            "public-actions-input.json", "public-actions-expanded-job.json",
            "retained-inputs-receipt.json", "run-receipt.json", "core-receipt.json",
            FINAL, "R815-projective-original-425-source-audit.json.gz",
            "R815-projective-probe-scan-current.json.gz", KNOWN, IMPORTED, PREVIOUS_RECEIPT,
        }
        assert mandatory.issubset(files)
        selected = sorted(name for name, entry in files.items()
                          if name not in (BUNDLE, PREVIOUS_BUNDLE) and entry["bytes"] <= MAX_MEMBER and
                          (name in mandatory or name == "public-actions-run.log"
                           or name.startswith("R815-projective-")
                           or name.startswith("R815-two-known-columns-")
                           or name.startswith("R815-stage-manifest-")
                           or "exact-commutator" in name
                           or "certified-multiplier-index" in name))
        assert mandatory.issubset(selected)
        assert sum(files[name]["bytes"] for name in selected) <= MAX_TOTAL
        archive.extract_many([(name, files[name]["sha256"], original/name, files[name]["bytes"])
                              for name in selected])
        for name in selected:
            assert spec(original/name) == files[name]
        metadata = {name: read(original/name) for name in mandatory
                    if not name.startswith("R815-projective-")}
        initial = metadata["public-actions-input.json"]
        expanded = metadata["public-actions-expanded-job.json"]
        run = metadata["run-receipt.json"]
        core = metadata["core-receipt.json"]
        final = metadata[FINAL]
        retained = metadata["retained-inputs-receipt.json"]
        assert initial["result"] == run["result"] == core["result"] == final["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["source_repository"] == REPOSITORY
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == core["source_sha256"] == CORE_SHA
        assert initial["driver_sha256"] == initial["job"]["wrapper_sha256"] == WRAPPER_SHA
        assert initial["projective_method_sha256"] == initial["job"]["projective_method_sha256"] == METHOD_SHA
        assert initial["expanded_job_sha256"] == files["public-actions-expanded-job.json"]["sha256"]
        assert expanded["core_sha256"] == CORE_SHA
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
        assert core["certificate_sha256"] == files[FINAL]["sha256"]
        assert run["complete"] is core["complete"] is final["complete"] is False
        assert run["process_exit_code"] == 2 and run["error"] is None
        assert core["search_stop"] == final["search_stop"]
        assert final["projective_mode"] == core["projective_mode"] == MODE
        assert final["completed_scope"] == "projective_candidate_search_only"
        assert final["old_425_prime_arithmetic_recomputed"] is False
        assert final["candidate_failure_proves_original_matrix_nonexistence_or_insufficient_CRT"] is False
        tag = final["configuration"]
        assert tag == initial["actual_projective_configuration"]
        assert tag["source_sha256"] == CORE_SHA and tag["projective_method_sha256"] == METHOD_SHA
        assert tag["python_flint"] == "0.9.0"
        target_tags = final["target_configurations"]
        assert set(target_tags) == {"g", "h", "Gamma"}
        stage_manifest_spec = plain(final["stage_manifest"])
        assert stage_manifest_spec == files[stage_manifest_spec["file"]]
        stage_manifest = read(original/stage_manifest_spec["file"])
        assert stage_manifest["complete"] is True and stage_manifest["configuration"] == tag
        inventory = {entry["file"]: plain(entry) for entry in stage_manifest["files"]}
        currents = {entry["file"]: plain(entry) for entry in stage_manifest["current_checkpoints"]}
        assert len(inventory) == len(stage_manifest["files"])
        assert len(currents) == len(stage_manifest["current_checkpoints"])
        assert not set(inventory) & set(currents)
        for entry in list(inventory.values())+list(currents.values()):
            assert entry == files[entry["file"]]
        stages = {}
        for name in selected:
            if not (name.startswith("R815-") and name.endswith(".json.gz")):
                continue
            value = read(original/name)
            assert value["configuration"] == tag
            if name in currents:
                assert value["complete"] is False
            else:
                assert value["complete"] is True
            if "target_configuration" in value:
                target = value["target"]
                assert value["target_configuration"] == target_tags[target]
                assert value["target_configuration_sha256"] == fingerprint(target_tags[target])
            stages[name] = value
        audit_name = "R815-projective-original-425-source-audit.json.gz"
        scan_name = "R815-projective-probe-scan-current.json.gz"
        audit, scan = stages[audit_name], stages[scan_name]
        assert plain(final["original_425_source_audit"]) == files[audit_name]
        assert audit["source_original_current"] == final["source_original_current"]
        assert audit["source_original_latest_receipt"] == final["source_original_latest_receipt"]
        assert audit["coefficient_count"] == 295936 and audit["prime_count"] == 425
        assert audit["modulus_bits"] == 12707 and audit["latest_prime"] == 1000008791
        assert audit["source_original_425_prime_arithmetic_recomputed"] is False
        assert scan["source_original_current"] == final["source_original_current"]
        assert retained["input_bundle"] == files[BUNDLE]
        assert retained["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
        assert retained["old_completed_arithmetic_recomputed"] is False

        known, imported = stages[KNOWN], stages[IMPORTED]
        assert plain(final["exact_two_known_columns_input"]) == files[KNOWN]
        assert known["source_original_current"] == final["source_original_current"]
        assert known["source_original_425_identity"] == final["source_original_425_identity"]
        assert known["source_imported_previous_scalar_scan"] == final["completed_original_scalar_scan_reused"]
        assert imported["source_previous_scalar_scan_identity"] == final["completed_original_scalar_scan_reused"]
        assert imported["source_original_current"] == final["source_original_current"]
        assert known["original_g_reduced_denominator"] == audit["actual_reduced_g_first_column_denominator"]
        assert known["known_column_indices"] == [0, 1]
        assert known["known_column_coefficient_counts"] == [690, 962]
        assert known["normal_affine_basis_rank"] == 272
        assert known["coefficient_layout"] == "[known_input_column=0,1][power=0..4][output_row=0..271]"
        known_flags = (
            "both_weighted_supports_verified_coefficientwise",
            "common_denominator_is_positive_and_jointly_reduced",
            "all1652_original_current_congruences_verified",
            "new_exact_multiplication_of_original_W_and_vg_actually_performed",
            "all_original_scalar_and_field_normalizations_preserved",
        )
        for key in known_flags:
            assert known[key] is True
        assert known["original_known_first_column_arithmetic_recomputed"] is False
        for key in ("old_scalar_RR_checks_recomputed",
                    "old_first_nonzero_positions_reused_as_new_positions",
                    "old_candidate_rejection_reused_for_changed_two_column_candidate"):
            assert imported[key] is False
        numerators = known["column_integer_numerators"]
        assert len(numerators) == 2
        known_column_metadata = []
        for column, coefficients in enumerate(numerators):
            assert len(coefficients) == 5 and all(len(row) == 272 for row in coefficients)
            entries = [(power, row, decimal_metadata(value))
                       for power, values in enumerate(coefficients)
                       for row, value in enumerate(values)]
            nonzero = [(power, row, value) for power, row, value in entries if not value["is_zero"]]
            known_column_metadata.append({
                "input_column": column, "padded_integer_entry_count": len(entries),
                "nonzero_integer_text_count": len(nonzero),
                "maximum_integer_decimal_digits": max(value["decimal_digits"] for _, _, value in entries),
                "maximum_integer_bit_length": max(value["integer_bit_length"] for _, _, value in entries),
                "first_nonzero_integer_text_location_power_row": None if not nonzero else list(nonzero[0][:2]),
                "first_nonzero_integer_text_metadata": None if not nonzero else nonzero[0][2],
            })
        known_summary = {
            "file": files[KNOWN],
            "known_column_indices": known["known_column_indices"],
            "known_column_coefficient_counts": known["known_column_coefficient_counts"],
            "denominators": {key: decimal_metadata(known[key]) for key in (
                "original_g_reduced_denominator", "original_W_common_positive_denominator",
                "initial_common_positive_denominator", "removed_joint_integer_content",
                "common_positive_denominator")},
            "columns": known_column_metadata,
            "source_g_vector": known["source_original_g_vector"],
            "source_M_w": known["source_original_M_w"],
            "source_flags": {key: known[key] for key in known_flags},
            "original_known_first_column_arithmetic_recomputed":
                known["original_known_first_column_arithmetic_recomputed"],
            "full_known_integer_arrays_preserved_only_in_one_day_output_artifact": True,
            "this_IO_reader_does_not_recheck_matrix_multiplication_gcd_or_congruence": True,
        }
        imported_summary = {key: imported[key] for key in (
            "completed_old_prefix_stop", "original_failed_scalar_indices",
            "remaining_unknown_column_failure_indices", "old_scalar_RR_checks_recomputed",
            "old_first_nonzero_positions_reused_as_new_positions",
            "old_candidate_rejection_reused_for_changed_two_column_candidate")}
        previous_receipt = metadata[PREVIOUS_RECEIPT]
        assert previous_receipt["input_bundle"] == files[PREVIOUS_BUNDLE]
        assert previous_receipt["new_mathematical_arithmetic_performed"] is False

        pairs, lattices, definitions, early, rejections = [], [], {}, {}, {}
        all_row_D, admissible_D = [], set()
        rejected_by_reason = collections.Counter()
        for name, value in stages.items():
            if PAIR.fullmatch(name):
                assert all(probe["weighted_location"][1] not in (0, 1) for probe in value["probes"])
                pairs.append({"file": files[name], "pair_number": value["pair_number"],
                    "probes": [{"coefficient_index": probe["coefficient_index"],
                                "weighted_location": probe["weighted_location"],
                                "residue": decimal_metadata(probe["residue_mod_original_M"])}
                               for probe in value["probes"]],
                    "fallback_after_exhausting_actual_coordinate_order":
                        value["fallback_after_exhausting_actual_coordinate_order"],
                    "resume_after_pair": {key: value["resume_after_pair"][key] for key in (
                        "next_coefficient_index", "unpaired_failure", "completed_pair_count",
                        "scalar_RR_failure_count", "scan_finished")}})
            elif LLL.fullmatch(name):
                assert value["source_exact_two_known_columns"] == files[KNOWN]
                assert len(value["candidates"]) == 3
                rows_out = []
                for candidate in value["candidates"]:
                    D = candidate["D"]
                    all_row_D.append(D)
                    reason = candidate["search_rejection_reason"]
                    if reason is None:
                        admissible_D.add(D)
                    else:
                        rejected_by_reason[reason] += 1
                    rows_out.append({"LLL_row": candidate["LLL_row"], "row_sign": candidate["row_sign"],
                        "D": decimal_metadata(D),
                        "probe_numerators": [decimal_metadata(x) for x in candidate["probe_numerators"]],
                        "search_rejection_reason": reason,
                        "original_congruences_verified": candidate["original_congruences_verified"],
                        "denominator_is_multiple_of_actual_d01": candidate["denominator_is_multiple_of_actual_d01"],
                        "no_height_rectangle_used": candidate["no_height_rectangle_used"]})
                lattices.append({"file": files[name], "pair_number": value["pair_number"],
                    "shift": value["shift"], "candidates": rows_out,
                    "zero_denominator_rows": sum(c["search_rejection_reason"] == "zero_denominator" for c in value["candidates"]),
                    "nonunit_denominator_rows": sum(c["search_rejection_reason"] == "denominator_not_a_unit_at_original_CRT" for c in value["candidates"]),
                    "full_basis_change_equality_verified": value["full_basis_change_equality_verified"],
                    "actual_LLL_rows_preserved_in_original_file": True})
            elif DEFINITION.fullmatch(name):
                candidate_id = value["projective_candidate_id"]
                assert candidate_id not in definitions
                assert value["source_exact_two_known_columns"] == files[KNOWN]
                assert value["D_is_positive_multiple_of_actual_reduced_d01_and_unit_mod_M"] is True
                assert value["both_known_columns_use_exact_unbounded_lift"] is True
                assert value["commutator_column0_is_a_construction_identity"] is True
                definitions[candidate_id] = {"file": files[name], "D": decimal_metadata(value["D"]),
                    "source_kind": value["source_kind"],
                    "source_candidate_generator": value["source_candidate_generator"],
                    "source_LLL_row": value["source_LLL_row"],
                    "probes": [{"coefficient_index": p["coefficient_index"],
                                "weighted_location": p["weighted_location"]} for p in value["probes"]],
                    "early_exact_commutator_entries": value["early_exact_commutator_entries"]}
            elif EARLY.fullmatch(name):
                match = EARLY.fullmatch(name)
                assert value["input_column"] not in (0,)
                entry = {"file": files[name], "ordinal": int(match.group(2)),
                    "exact_integer_point": value["exact_integer_point"],
                    "output_row": value["output_row"], "input_column": value["input_column"],
                    "zero": value["zero"],
                    "exact_integer_commutator_residual": decimal_metadata(value["exact_integer_commutator_residual"])}
                early.setdefault(match.group(1), []).append(entry)
            elif REJECTION.fullmatch(name):
                candidate_id = value["candidate_id"]
                assert value["only_inactive_rejected_large_candidate_blocks_pruned"] is True
                assert value["original_source_current_or_Krylov_cache_deleted"] is False
                assert value["no_exact_characteristic_zero_multiplier_claimed"] is True
                rejections[candidate_id] = {"file": files[name], "reason": value["reason"],
                    "additional": value["additional"],
                    "discarded_candidate_file_history_count": len(value["discarded_candidate_file_history"])}
        candidate_summaries = []
        for candidate_id, definition in sorted(definitions.items()):
            checks = sorted(early.get(candidate_id, []), key=lambda x: x["ordinal"])
            failed = next((entry for entry in checks if not entry["zero"]), None)
            rejection = rejections.get(candidate_id)
            if rejection and "failed_exact_entry" in rejection["additional"]:
                entry = plain(rejection["additional"]["failed_exact_entry"])
                assert entry == files[entry["file"]]
                assert failed is not None and failed["file"] == entry
            candidate_summaries.append(dict(definition, candidate_id=candidate_id,
                actual_early_entries_checked=len(checks), all_actual_early_entries=checks,
                first_failed_exact_entry=failed, rejection=rejection))
        control_keys = ("next_coefficient_index", "unpaired_failure", "completed_pair_count",
                        "first_nonzero_nonfirst_column_positions", "scalar_RR_failure_count", "scan_finished")
        scan_summary = {key: scan[key] for key in control_keys}
        scan_summary["known_remaining_failure_in_source_prefix"] = scan["known_remaining_failure_in_source_prefix"]
        scan_summary["algorithm_excludes_known_input_columns"] = [0, 1]
        d = scan["all_scalar_RR_denominator_if_no_failure"]
        scan_summary["all_scalar_RR_denominator_if_no_failure"] = None if d is None else decimal_metadata(d)
        scanned_expected = final["search_stop"]["actual_completed_probe_pairs"]
        assert scanned_expected == scan["completed_pair_count"]
        assert final["search_stop"]["actual_scalar_RR_failure_count"] == scan["scalar_RR_failure_count"]
        pairs.sort(key=lambda x: x["pair_number"])
        lattices.sort(key=lambda x: (x["pair_number"], x["shift"]))
        omitted = [files[name] for name in sorted(files) if name not in selected]
        summary = {
            "result": "R815-two-known-columns-ended-small-IO-review",
            "mathematical_result": RESULT, "complete_IO_review": True,
            "reader_sha256": sha(__file__), "source": source_spec(source),
            "source_manifest": spec(manifest_path), "source_manifest_reference": spec(reference_path),
            "source_file_count": len(files), "source_ZIP_member_count": len(archive.by_name),
            "source_run_receipt": files["run-receipt.json"], "source_core_receipt": files["core-receipt.json"],
            "source_false_certificate": files[FINAL], "source_stage_manifest": stage_manifest_spec,
            "source_public_input": files["public-actions-input.json"],
            "source_expanded_job": files["public-actions-expanded-job.json"],
            "source_configuration_sha256": fingerprint(tag),
            "source_search_stop": final["search_stop"], "actual_core_seconds": final["seconds"],
            "original_425_source_audit": files[audit_name],
            "original_reduced_g_first_column_denominator": decimal_metadata(audit["actual_reduced_g_first_column_denominator"]),
            "original_current": final["source_original_current"],
            "original_latest_CRT_receipt": final["source_original_latest_receipt"],
            "source_input_bundle": files[BUNDLE],
            "original_selected_input_count_reported_by_source": retained["actual_selected_file_count"],
            "exact_two_known_columns": known_summary,
            "imported_scalar_scan": {"file": files[IMPORTED], "fields": imported_summary},
            "previous_scan_input_receipt": files[PREVIOUS_RECEIPT],
            "previous_scan_input_bundle": files[PREVIOUS_BUNDLE],
            "previous_scan_carrier_not_downloaded_or_rehashed_in_this_review": True,
            "input_carrier_not_downloaded_or_rehashed_in_this_review": True,
            "scan_current": files[scan_name], "scan_current_fields": scan_summary,
            "probe_pair_count": len(pairs), "probe_pairs": pairs,
            "LLL_stage_count": len(lattices), "LLL_row_count": len(all_row_D),
            "LLL_distinct_raw_denominator_text_count": len(set(all_row_D)),
            "LLL_repeated_raw_denominator_row_count": len(all_row_D)-len(set(all_row_D)),
            "LLL_distinct_admissible_denominator_text_count": len(admissible_D),
            "LLL_search_rejection_counts": dict(rejected_by_reason),
            "lattices": lattices,
            "distinct_candidate_definitions_count": len(definitions),
            "baseline_d01_candidate_count": sum(x["source_kind"] == "actual_two_known_columns_denominator"
                                               for x in definitions.values()),
            "actual_early_checked_candidate_count": len(early),
            "candidate_rejection_receipt_count": len(rejections),
            "candidate_summaries": candidate_summaries,
            "complete_exact_commutator_stage_names": [name for name in selected if "exact-commutator-z-" in name],
            "complete_candidate_index_stage_names": [name for name in selected
                if name.endswith("-candidate-index.json.gz") or name.endswith("-certified-multiplier-index.json.gz")],
            "all_selected_original_files": [files[name] for name in selected],
            "omitted_original_files": omitted,
            "all_selected_member_sizes_and_SHA256_verified": True,
            "new_lattice_RR_matrix_or_residual_arithmetic_performed": False,
            "new_exact_operator_or_nonexistence_certificate_claimed": False,
            "transport": archive.receipt(),
        }
        save(out/"R815-two-known-columns-ended-small-IO-summary.json", summary)
        save(out/"R815-two-known-columns-ended-small-IO-files.json", {
            "files": [spec(path) for path in sorted(original.iterdir()) if path.is_file()],
            "summary": spec(out/"R815-two-known-columns-ended-small-IO-summary.json"),
            "reproducible_data_kept_only_in_active_one_day_artifact": True})
        compact = {key: value for key, value in summary.items()
                   if key not in ("all_selected_original_files", "omitted_original_files",
                                  "candidate_summaries", "lattices")}
        compact["lattices"] = [{"pair": row["pair_number"], "shift": row["shift"],
            "file": row["file"], "zero_denominator_rows": row["zero_denominator_rows"],
            "nonunit_denominator_rows": row["nonunit_denominator_rows"],
            "rows": [{"row": c["LLL_row"], "D_digits": c["D"]["decimal_digits"], "D_bits": c["D"]["integer_bit_length"],
                      "D_text_sha256": c["D"]["integer_text_sha256"],
                      "search_rejection": c["search_rejection_reason"]} for c in row["candidates"]]}
            for row in lattices]
        compact["candidates"] = [{"id": row["candidate_id"], "source_kind": row["source_kind"],
            "D_digits": row["D"]["decimal_digits"], "D_bits": row["D"]["integer_bit_length"], "source_LLL_row": row["source_LLL_row"],
            "source_generator": row["source_candidate_generator"],
            "actual_early_entries_checked": row["actual_early_entries_checked"],
            "first_failure": row["first_failed_exact_entry"],
            "rejection_reason": None if row["rejection"] is None else row["rejection"]["reason"]}
            for row in candidate_summaries]
        compact["summary_file"] = spec(out/"R815-two-known-columns-ended-small-IO-summary.json")
        print("R815_TWO_KNOWN_COLUMNS_ENDED_IO_SUMMARY="+json.dumps(compact, sort_keys=True, separators=(",", ":")), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.exit(main())
