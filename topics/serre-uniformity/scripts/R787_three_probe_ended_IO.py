#!/usr/bin/env python3
"""Read completed R787 incremental three-probe decisions without new mathematical arithmetic."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

ORIGINAL = "R787-original-power5-function-relation"
RESULT = "R787-three-probe-ended-source-IO-review"
FINAL = "p41-original-power5-function-relation-certificate.json"
BUNDLE = "R787-retained-producer-inputs.tar.gz"
PREVIOUS_BUNDLE = "R787-retained-two-probe-search.tar.gz"
PREVIOUS_RECEIPT = "previous-two-probe-inputs-receipt.json"
REFERENCE = "full-outputs-manifest-reference.json"
PREFIX = "R787-projective-"
S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
LIMIT = 20*1024*1024


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def spec(path):
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    request = read(args.request)
    assert sha(__file__) == request["script_sha256"]
    for label, path in (("root", REPO/"README.md"), ("topic", TOPIC/"README.md")):
        assert sha(path) == request["current_readme_sha256"][label]
    helper = S/"R824_public_original_global_polar_generators.py"
    assert sha(helper) == request["io_helper_sha256"]
    ms = importlib.util.spec_from_file_location("R787_three_probe_frozen_IO", helper)
    IO = importlib.util.module_from_spec(ms)
    ms.loader.exec_module(IO)
    args.output.mkdir(parents=True, exist_ok=True)
    selected = args.output/"selected-original-three-probe"
    selected.mkdir(parents=True, exist_ok=True)
    source = request["source"]
    archive = IO.Archive(source, args.output.parent/"source-range-transfer", whole=False)
    try:
        members = archive.by_name.get(REFERENCE, [])
        assert len(members) == 1 and 0 < members[0].file_size < 1024*1024
        data = archive.zip.read(members[0])
        assert len(data) == members[0].file_size
        (selected/REFERENCE).write_bytes(data)
        reference = read(selected/REFERENCE)
        assert reference["result"] == ORIGINAL and reference["projective_mode"] is True
        assert 0 < reference["manifest_bytes"] < LIMIT
        manifest_path = archive.extract_bound("full-outputs-manifest.json",
            reference["manifest_sha256"], selected/"full-outputs-manifest.json", reference["manifest_bytes"])
        manifest = read(manifest_path)
        assert manifest["result"] == ORIGINAL and manifest["projective_mode"] is True
        entries = {row["file"]: IO.plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == reference["file_count"]
        assert set(archive.by_name) == set(entries) | {"full-outputs-manifest.json", REFERENCE}
        for name, row in entries.items():
            IO.check_spec(row)
            assert len(archive.by_name[name]) == 1
            assert archive.by_name[name][0].file_size == row["bytes"]
        if source.get("manifest_sha256") is not None:
            assert sha(manifest_path) == source["manifest_sha256"]
        assert BUNDLE in entries and PREVIOUS_BUNDLE in entries
        names = sorted(name for name in entries if name not in (BUNDLE, PREVIOUS_BUNDLE))
        assert all(entries[name]["bytes"] <= LIMIT for name in names)
        archive.extract_many([(name, entries[name]["sha256"], selected/name, entries[name]["bytes"])
                              for name in names])
        for name in names:
            assert spec(selected/name) == entries[name]
        initial, run, core, cert = (read(selected/name) for name in
            ("public-actions-input.json", "run-receipt.json", "core-receipt.json", FINAL))
        assert initial["result"] == run["result"] == core["result"] == cert["result"] == ORIGINAL
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == source["core_sha256"]
        assert core["source_sha256"] == source["core_sha256"]
        assert initial["driver_sha256"] == initial["job"]["wrapper_sha256"] == request["original_wrapper_sha256"]
        assert initial["method_sha256"] == initial["job"]["projective_method_sha256"] == request["method_sha256"]
        for label, key in (("root", "root_readme_sha256"), ("topic", "topic_readme_sha256")):
            assert initial[key] == request["original_readme_sha256"][label]
        assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"] == request["core_receipt_sha256"]
        assert core["certificate_sha256"] == entries[FINAL]["sha256"] == request["certificate_sha256"]
        assert run["complete"] is core["complete"] is cert["complete"] is False
        assert run["process_exit_code"] == 2
        for key, expected in request["expected_outcome"].items():
            assert core[key] == cert[key] == expected
        assert cert["actual_y_map_recovered"] is False
        tag = cert["configuration"]
        assert tag["source_sha256"] == source["core_sha256"]
        assert tag["projective_method_sha256"] == request["method_sha256"]
        assert tag["projective_mode"] is True and tag["python_flint"] == "0.9.0"
        assert tag["projective_algorithm"] == "integral-L-incremental-three-probe-56-lattice-v3"
        assert tag["previous_two_probe_source"] == initial["job"]["previous_two_probe_source"]
        assert tag["LLL_integer_lattice_dimension"] == 56
        assert tag["LLL_four_integer_weights"] == [1, 1, 1, 1]
        stages = {}
        for name in names:
            if name.startswith(PREFIX) and name.endswith(".json.gz"):
                obj = read(selected/name)
                assert obj["result"] == ORIGINAL and obj["configuration"] == tag
                assert isinstance(obj["complete"], bool)
                stages[name] = obj
        index_spec = IO.plain(cert["stage_manifest"])
        assert index_spec == entries[index_spec["file"]]
        index = stages[index_spec["file"]]
        assert index["complete"] is True
        assert len(index["files"]) == len({row["file"] for row in index["files"]})
        for row in index["files"]:
            assert IO.plain(row) == entries[row["file"]] and stages[row["file"]]["complete"] is True
        assert {row["file"] for row in index["files"]} == {
            name for name, obj in stages.items() if obj["complete"] and name != index_spec["file"]}
        state_spec = IO.plain(cert["resume_state"])
        assert state_spec == entries[state_spec["file"]]
        state = stages[state_spec["file"]]
        assert state["complete"] is False
        assert len(state["processed_node_ids"]) == cert["completed_search_nodes"]
        assert state["completed_lattice_indices"] == cert["completed_lattice_indices"]
        assert state["next_candidate_position"] == cert["next_candidate_position"]
        assert state["consumed_LLL_candidate_rows"] == cert["consumed_LLL_candidate_rows"]

        basis_spec = IO.plain(cert["previous_basis_and_third_probe"])
        assert basis_spec == entries[basis_spec["file"]]
        basis = stages[basis_spec["file"]]
        assert basis["complete"] is True and basis["third_probe_found"] is True
        assert basis["old_42_rows_are_a_full_integer_lattice_basis"] is True
        assert basis["old_basis_change_times_canonical_equals_saved_basis"] is True
        assert basis["old_basis_change_determinant"] in ("1", "-1")
        assert len(basis["old_basis_change_integer_rows"]) == 42
        assert all(len(row) == 42 for row in basis["old_basis_change_integer_rows"])
        assert basis["old_42_dimensional_LLL_reexecuted"] is False
        assert basis["actual_third_probe_A_index"] == cert["actual_third_probe_A_index"]
        assert basis["previous_two_probe_source"] == tag["previous_two_probe_source"]
        assert basis["previous_lattice_stage"] == tag["previous_two_probe_source"]["lattice_stage"]
        lattice_names = [name for name in stages if name.endswith("-incremental-three-probe-LLL.json.gz")]
        assert len(lattice_names) == 1
        lattice_name = lattice_names[0]
        lattice = stages[lattice_name]
        assert lattice["lattice_dimension"] == 56 and lattice["weights"] == ["1", "1", "1", "1"]
        assert lattice["all_56_reduced_rows_saved"] is True
        assert lattice["all_168_original_probe_congruences_verified"] is True
        assert lattice["new_56_rows_are_a_full_integer_lattice_basis"] is True
        assert lattice["new_basis_change_times_canonical_equals_reduced_basis"] is True
        assert lattice["new_basis_change_determinant"] in ("1", "-1")
        assert len(lattice["new_basis_change_integer_rows"]) == 56
        assert all(len(row) == 56 for row in lattice["new_basis_change_integer_rows"])
        assert lattice["old_42_dimensional_LLL_reexecuted"] is False
        assert lattice["probe_indices_C_then_A"] == [0, 1, 1214+basis["actual_third_probe_A_index"]]
        input_spec, raw_spec = (IO.plain(lattice[key]) for key in ("input_basis_stage", "reduced_basis_stage"))
        assert input_spec == entries[input_spec["file"]] and raw_spec == entries[raw_spec["file"]]
        input_basis, raw_basis = stages[input_spec["file"]], stages[raw_spec["file"]]
        assert input_basis["source_basis_certificate"] == basis_spec
        assert input_basis["previous_lattice_stage"] == basis["previous_lattice_stage"]
        assert input_basis["dimension"] == 56
        assert len(input_basis["augmented_basis_rows"]) == 56
        assert all(len(row) == 56 for row in input_basis["augmented_basis_rows"])
        assert input_basis["old_42_basis_rows_preserved_in_original_order"] is True
        assert input_basis["full_integer_three_probe_lattice_basis_proved"] is True
        assert input_basis["augmented_basis_sha256"] == lattice["lattice_input_sha256"]
        assert raw_basis["input_basis"] == input_spec
        assert raw_basis["lattice_dimension"] == 56 and raw_basis["all_56_reduced_rows_saved"] is True
        assert len(raw_basis["all_56_reduced_rows"]) == 56
        assert all(len(row) == 56 for row in raw_basis["all_56_reduced_rows"])
        candidates = {row["id"]: row for row in lattice["candidates"]}
        assert len(candidates) == len(lattice["candidates"]) == cert["completed_search_nodes"]
        assert set(candidates) == set(state["processed_node_ids"])
        assert set(state["new_exact_candidate_ids"]) == set(candidates)
        assert not state["referenced_previous_rejection_ids"]
        outcomes, closed, order_counts = [], [], {}
        for name, obj in stages.items():
            if name.endswith("-result.json.gz") and name.startswith(PREFIX+"candidate-"):
                assert obj["exact_relation_found"] is False and obj["relation_spec"] is None
                assert obj["previous_exact_rejection_reused"] is False
                assert obj["previous_exact_rejection_reference"] is None
                assert obj["new_exact_candidate_evaluation_performed"] is True
                node = candidates[obj["node_id"]]
                assert obj["denominator"] == node["denominator"]
                assert obj["source_lattice"] == entries[lattice_name]
                assert obj["source_reduced_row"] == node["source_LLL_row"]
                rejection_spec = IO.plain(obj["exact_rejection"])
                assert rejection_spec == entries[rejection_spec["file"]]
                rejection = stages[rejection_spec["file"]]
                assert rejection["node_id"] == obj["node_id"]
                assert rejection["first_nonzero_relation_order"] == obj["first_nonzero_relation_order"]
                assert rejection["not_a_characteristic_zero_relation"] is True
                key = str(obj["first_nonzero_relation_order"])
                order_counts[key] = order_counts.get(key, 0)+1
                outcomes.append({
                    "node_id": obj["node_id"], "source_reduced_row": obj["source_reduced_row"],
                    "source_lattice": entries[lattice_name],
                    "first_nonzero_relation_order": obj["first_nonzero_relation_order"],
                    "outcome": entries[name], "exact_rejection": rejection_spec,
                    "previous_exact_rejection_reused": False})
            elif name.endswith("-closed-work-receipt.json.gz"):
                assert obj["current_or_successful_candidate_payload_never_retired"] is True
                assert obj["retired_payloads_never_recomputed_for_this_completed_candidate"] is True
                assert obj["all_original_56_LLL_rows_and_exact_failure_retained"] is True
                for key in ("completed_rejection", "completed_outcome"):
                    bound = IO.plain(obj[key])
                    assert bound == entries[bound["file"]]
                    assert stages[bound["file"]]["node_id"] == obj["node_id"]
                retired_specs = {row["file"]: IO.plain(row) for row in obj["retired_work_files"]}
                for retired in retired_specs.values():
                    IO.check_spec(retired)
                    assert retired["file"] not in entries
                candidate_name = PREFIX+"candidate-"+obj["node_id"]+"-candidate.json.gz"
                rejected = stages[obj["completed_rejection"]["file"]]
                assert retired_specs[candidate_name]["sha256"] == rejected["candidate_sha256"]
                closed.append(entries[name])
        assert len(outcomes) == len(closed) == cert["completed_search_nodes"] == cert["new_exact_candidate_evaluations"]
        assert cert["previous_exact_candidate_rejections_referenced"] == 0
        assert {row["node_id"] for row in outcomes} == set(state["processed_node_ids"])
        diagnostics = []
        for row in lattice["row_diagnostics"]:
            small = {key: value for key, value in row.items() if key != "weighted_squared_norm"}
            small["weighted_squared_norm_decimal_digits"] = len(row["weighted_squared_norm"])
            diagnostics.append(small)
        previous = read(selected/PREVIOUS_RECEIPT)
        assert previous["result"] == ORIGINAL and previous["complete"] is True
        assert previous["source"] == tag["previous_two_probe_source"]
        assert IO.plain(previous["bundle"]) == entries[PREVIOUS_BUNDLE]
        assert previous["all_selected_old_search_and_original_input_bytes_SHA_verified"] is True
        assert previous["old_search_preserved_under_its_original_configuration"] is True
        assert previous["previous_arithmetic_recomputed"] is False
        assert len(previous["files"]) == previous["file_count"] == 138
        for row in previous["files"]:
            IO.check_spec(row)
        old_source_specs = {row["file"]: IO.plain(row) for row in previous["files"]}
        for key in ("lattice_stage", "search_state", "certificate"):
            row = tag["previous_two_probe_source"][key]
            assert IO.plain(row) == old_source_specs[row["file"]]
        retained = read(selected/"retained-inputs-receipt.json")
        assert retained["complete"] is True and retained["file_count"] == 1380
        assert IO.plain(retained["bundle"]) == entries[BUNDLE]
        assert retained["all_selected_source_and_new_carrier_member_bytes_and_sha256_verified"] is True
        summary = {
            "result": RESULT, "complete": True, "original_source": source,
            "original_run_receipt": run, "original_core_receipt": core,
            "full_manifest": spec(manifest_path), "actual_manifest_file_count": len(entries),
            "actual_ZIP_regular_member_count": len(archive.by_name),
            "all_noncarrier_output_files_actual_bytes_and_SHA_verified": True,
            "noncarrier_files_verified": len(names),
            "carrier_identities_only_not_redownloaded": {BUNDLE: entries[BUNDLE], PREVIOUS_BUNDLE: entries[PREVIOUS_BUNDLE]},
            "original_frozen_verify_recorded_all_138_previous_source_files_verified": True,
            "original_frozen_verify_recorded_all_1380_source_members_verified": True,
            "actual_completed_search_nodes": cert["completed_search_nodes"],
            "actual_remaining_schedule": cert["remaining_schedule"],
            "actual_lattice": {
                "stage": entries[lattice_name], "dimension": lattice["lattice_dimension"],
                "probe_indices_C_then_A": lattice["probe_indices_C_then_A"],
                "actual_A_probe_index": basis["actual_third_probe_A_index"],
                "source_basis_stage": basis_spec, "input_stage": input_spec, "raw_reduced_basis_stage": raw_spec,
                "old_basis_change_determinant": basis["old_basis_change_determinant"],
                "new_basis_change_determinant": lattice["new_basis_change_determinant"],
                "all56_rows_and168_original_congruences_recorded_by_core": True,
                "row_diagnostics": diagnostics, "candidate_count": len(candidates)},
            "actual_first_nonzero_relation_order_counts": order_counts,
            "actual_new_exact_candidates": cert["new_exact_candidate_evaluations"],
            "actual_previous_exact_rejections_referenced": cert["previous_exact_candidate_rejections_referenced"],
            "actual_closed_outcomes": sorted(outcomes, key=lambda row: row["source_reduced_row"]),
            "stage_manifest": index_spec, "resume_state": state_spec,
            "resume_state_content": state,
            "original_core_seconds": cert["seconds"],
            "exhaustion_of_one_56_row_search_is_not_nonexistence": True,
            "original_relation_or_beta_or_eta_or_height_recovered": False,
            "new_mathematical_arithmetic_executed": False,
            "source_transfer": archive.receipt(),
            "selected_files": [spec(selected/REFERENCE), spec(manifest_path)]+[entries[name] for name in names],
            "raw_location": "one-day active public Actions IO artifact"}
        summary_path = args.output/"R787-three-probe-ended-IO-summary.json"
        IO.save(summary_path, summary)
        compact = {key: value for key, value in summary.items() if key not in
                   ("actual_closed_outcomes", "selected_files", "resume_state_content", "actual_lattice")}
        compact["actual_lattice"] = {key: value for key, value in summary["actual_lattice"].items()
                                    if key != "row_diagnostics"}
        compact["actual_D_maximum_bits_by_row"] = [
            {"row": row["LLL_row"], "bits": row["maximum_D_bits"],
             "candidate_status": row["candidate_status"],
             "ell_unit_diagnostic_only": row.get("ell_unit_diagnostic_only")}
            for row in diagnostics]
        compact["complete_IO_summary"] = spec(summary_path)
        compact["core_certificate"] = entries[FINAL]
        compact["core_receipt"] = entries["core-receipt.json"]
        compact["source_receipts"] = [entries["retained-inputs-receipt.json"], entries[PREVIOUS_RECEIPT]]
        print("R787_THREE_PROBE_ENDED_IO_SUMMARY="+json.dumps(compact, sort_keys=True), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.exit(main())
