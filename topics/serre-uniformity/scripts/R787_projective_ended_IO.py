#!/usr/bin/env python3
"""Read an actually ended projective search without rerunning its arithmetic."""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

ORIGINAL = "R787-original-power5-function-relation"
RESULT = "R787-projective-ended-source-IO-review"
FINAL = "p41-original-power5-function-relation-certificate.json"
BUNDLE = "R787-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
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
    module_spec = importlib.util.spec_from_file_location("projective_ended_frozen_IO", helper)
    IO = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(IO)
    args.output.mkdir(parents=True, exist_ok=True)
    selected = args.output/"selected-original-R787-projective"
    selected.mkdir(parents=True, exist_ok=True)
    source = request["source"]
    archive = IO.Archive(source, args.output.parent/"source-range-transfer", whole=False)
    reviewed = {}
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
        names = [name for name in entries if name != BUNDLE]
        assert BUNDLE in entries
        assert all(entries[name]["bytes"] <= LIMIT for name in names)
        archive.extract_many([(name, entries[name]["sha256"], selected/name, entries[name]["bytes"])
                              for name in sorted(names)])
        for name in names:
            assert spec(selected/name) == entries[name]
            reviewed[name] = entries[name]
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
        assert core["candidate_search_exhausted"] is cert["candidate_search_exhausted"] is True
        assert core["search_node_budget_reached"] is cert["search_node_budget_reached"] is False
        assert cert["exact_verified_orders"] == 0 and cert["actual_y_map_recovered"] is False
        tag = cert["configuration"]
        assert tag["source_sha256"] == source["core_sha256"]
        assert tag["projective_method_sha256"] == request["method_sha256"]
        assert tag["projective_mode"] is True and tag["python_flint"] == "0.9.0"
        stages, nodes, rectangles = {}, {}, []
        order_constant_decimal_digits = None
        for name in names:
            if not (name.startswith("R787-projective-") and name.endswith(".json.gz")):
                continue
            obj = read(selected/name)
            assert obj["result"] == ORIGINAL and obj["configuration"] == tag
            assert isinstance(obj["complete"], bool)
            stages[name] = obj
            node_id = obj.get("node_id")
            if node_id is not None:
                row = nodes.setdefault(node_id, {"node_id": node_id})
                if name.endswith("-scan.json.gz"):
                    row.update({"rectangle_index": obj["rectangle_index"],
                        "accepted_prefix_length": obj["accepted_prefix_length"],
                        "maximum_accepted_numerator_bits": obj["maximum_accepted_numerator_bits"],
                        "all_numerators_in_bound": obj["all_numerators_in_bound"]})
                    failure = obj.get("failure")
                    row["first_failure"] = None if failure is None else {
                        key: failure[key] for key in ("global_index", "source_kind", "source_row")}
                    row["scan_spec"] = entries[name]
                elif name.endswith("-LLL-children.json.gz"):
                    row.update({"rejected_counts": obj["rejected_counts"],
                        "admissible_candidates": obj["admissible_candidates"],
                        "retained_child_count": len(obj["children"]),
                        "LLL_row_dimension": obj["lattice_dimension"],
                        "all_28_congruences_verified_by_original_core": obj["all_28_reduced_rows_exact_congruences_checked"],
                        "children_stage_spec": entries[name]})
                elif name.endswith("-result.json.gz"):
                    row.update({"exact_relation_found": obj["exact_relation_found"],
                                "result_spec": entries[name]})
            if name.endswith("integral-order-and-rectangles.json.gz"):
                order_constant_decimal_digits = len(obj["multiplication_constant"])
                rectangles = [{"shift": rect["shift"],
                    "numerator_bound_decimal_digits": len(rect["numerator_bound"]),
                    "denominator_bound_decimal_digits": len(rect["denominator_bound"])}
                    for rect in obj["rectangles"]]
        index_spec = cert["stage_manifest"]
        assert IO.plain(index_spec) == entries[index_spec["file"]]
        index = stages[index_spec["file"]]
        assert index["complete"] is True
        assert len(index["files"]) == len({row["file"] for row in index["files"]})
        for row in index["files"]:
            assert IO.plain(row) == entries[row["file"]] and stages[row["file"]]["complete"] is True
        assert {row["file"] for row in index["files"]} == {
            name for name, obj in stages.items() if obj["complete"] and name != index_spec["file"]}
        state_spec = cert["resume_state"]
        assert IO.plain(state_spec) == entries[state_spec["file"]]
        state = stages[state_spec["file"]]
        assert state["complete"] is False and state["frontier"] == []
        assert state["finite_search_exhausted"] is True
        receipt = read(selected/"retained-inputs-receipt.json")
        assert receipt["complete"] is True and receipt["file_count"] == 1380
        assert IO.plain(receipt["bundle"]) == entries[BUNDLE]
        assert receipt["all_selected_source_and_new_carrier_member_bytes_and_sha256_verified"] is True
        summary = {
            "result": RESULT, "complete": True, "original_source": source,
            "original_run_receipt": run, "original_core_receipt": core,
            "full_manifest": spec(manifest_path), "actual_manifest_file_count": len(entries),
            "actual_ZIP_regular_member_count": len(archive.by_name),
            "all_noncarrier_output_files_actual_bytes_and_SHA_verified": True,
            "noncarrier_files_verified": len(reviewed),
            "carrier_identity_only_not_redownloaded": entries[BUNDLE],
            "original_frozen_verify_recorded_all_1380_source_members_verified": True,
            "actual_completed_search_nodes": cert["completed_search_nodes"],
            "actual_remaining_search_nodes": cert["remaining_search_nodes"],
            "actual_rectangles_size_metadata": rectangles,
            "actual_order_multiplication_constant_decimal_digits": order_constant_decimal_digits,
            "actual_nodes": sorted(nodes.values(), key=lambda value: (value.get("rectangle_index", -1), value["node_id"])),
            "stage_manifest": IO.plain(index_spec), "resume_state": IO.plain(state_spec),
            "original_core_seconds": cert["seconds"],
            "finite_search_exhausted_is_not_nonexistence": True,
            "original_relation_or_beta_or_eta_or_height_recovered": False,
            "new_mathematical_arithmetic_executed": False,
            "source_transfer": archive.receipt(),
            "selected_files": [spec(selected/REFERENCE), spec(manifest_path)]+[reviewed[name] for name in sorted(reviewed)],
            "raw_location": "one-day active public Actions audit artifact"}
        IO.save(args.output/"R787-projective-ended-IO-summary.json", summary)
        print("R787_PROJECTIVE_ENDED_IO_SUMMARY="+json.dumps(summary, sort_keys=True), flush=True)
        return 0
    finally:
        archive.close()


if __name__ == "__main__":
    sys.exit(main())
