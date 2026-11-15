#!/usr/bin/env python3
"""Read completed R787 two-probe decisions and resume metadata, without new arithmetic."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

ORIGINAL = "R787-original-power5-function-relation"
RESULT = "R787-two-probe-ended-source-IO-review"
FINAL = "p41-original-power5-function-relation-certificate.json"
BUNDLE = "R787-retained-producer-inputs.tar.gz"
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
    ms = importlib.util.spec_from_file_location("R787_two_probe_frozen_IO", helper)
    IO = importlib.util.module_from_spec(ms)
    ms.loader.exec_module(IO)
    args.output.mkdir(parents=True, exist_ok=True)
    selected = args.output/"selected-original-two-probe"
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
        assert BUNDLE in entries
        names = sorted(name for name in entries if name != BUNDLE)
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
        lattices, outcomes, closed = [], [], []
        for name, obj in stages.items():
            if name.endswith("-two-probe-LLL.json.gz"):
                assert obj["all_42_reduced_rows_saved"] is True
                assert len(obj["all_42_reduced_rows"]) == 42
                assert all(len(row) == 42 for row in obj["all_42_reduced_rows"])
                assert obj["all_84_original_probe_congruences_verified"] is True
                lattices.append({
                    "stage": entries[name], "probe_pair_index": obj["probe_pair_index"],
                    "probe_indices_C_then_A": obj["probe_indices_C_then_A"],
                    "row_diagnostics": obj["row_diagnostics"],
                    "candidate_count": len(obj["candidates"]),
                    "all42_rows_and84_original_congruences_recorded_by_core": True})
            elif name.endswith("-result.json.gz") and name.startswith(PREFIX+"candidate-"):
                assert obj["exact_relation_found"] is False and obj["relation_spec"] is None
                rejection_spec = IO.plain(obj["exact_rejection"])
                assert rejection_spec == entries[rejection_spec["file"]]
                rejection = stages[rejection_spec["file"]]
                assert rejection["node_id"] == obj["node_id"]
                assert rejection["first_nonzero_relation_order"] == obj["first_nonzero_relation_order"]
                assert rejection["not_a_characteristic_zero_relation"] is True
                outcomes.append({
                    "node_id": obj["node_id"], "source_reduced_row": obj["source_reduced_row"],
                    "source_lattice": IO.plain(obj["source_lattice"]),
                    "first_nonzero_relation_order": obj["first_nonzero_relation_order"],
                    "outcome": entries[name], "exact_rejection": rejection_spec})
            elif name.endswith("-closed-work-receipt.json.gz"):
                assert obj["current_or_successful_candidate_payload_never_retired"] is True
                assert obj["retired_payloads_never_recomputed_for_this_completed_candidate"] is True
                for key in ("completed_rejection", "completed_outcome"):
                    bound = IO.plain(obj[key])
                    assert bound == entries[bound["file"]]
                    assert stages[bound["file"]]["node_id"] == obj["node_id"]
                for retired in obj["retired_work_files"]:
                    IO.check_spec(retired)
                    assert retired["file"] not in entries
                closed.append(entries[name])
        assert len(outcomes) == len(closed) == cert["completed_search_nodes"]
        assert {row["node_id"] for row in outcomes} == set(state["processed_node_ids"])
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
            "carrier_identity_only_not_redownloaded": entries[BUNDLE],
            "original_frozen_verify_recorded_all_1380_source_members_verified": True,
            "actual_completed_search_nodes": cert["completed_search_nodes"],
            "actual_remaining_schedule": cert["remaining_schedule"],
            "actual_lattices": sorted(lattices, key=lambda row: row["probe_pair_index"]),
            "actual_closed_outcomes": sorted(outcomes, key=lambda row: row["source_reduced_row"]),
            "stage_manifest": index_spec, "resume_state": state_spec,
            "resume_state_content": state,
            "original_core_seconds": cert["seconds"],
            "finite_budget_stop_is_not_nonexistence": True,
            "original_relation_or_beta_or_eta_or_height_recovered": False,
            "new_mathematical_arithmetic_executed": False,
            "source_transfer": archive.receipt(),
            "selected_files": [spec(selected/REFERENCE), spec(manifest_path)]+[entries[name] for name in names],
            "raw_location": "one-day active public Actions IO artifact"}
        IO.save(args.output/"R787-two-probe-ended-IO-summary.json", summary)
        print("R787_TWO_PROBE_ENDED_IO_SUMMARY="+json.dumps(summary, sort_keys=True), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.exit(main())
