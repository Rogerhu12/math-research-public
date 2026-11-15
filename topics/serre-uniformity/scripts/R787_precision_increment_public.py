#!/usr/bin/env python3
"""Public IO for a source-bound precision increment of the original 56-dimensional lattice.

The mathematical core consumes a genuinely published deeper original current.
This module imports only frozen standard-library source readers.  It does not
compute a Dixon digit, lattice row, candidate, or original function relation.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R787_precision_increment-public-request.json"
RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-power5-function-relation-certificate.json"
PREFIX = "R787-projective-"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R787-retained-producer-inputs.tar.gz"
TWO_BUNDLE = "R787-retained-two-probe-search.tar.gz"
THREE_BUNDLE = "R787-precision-retained-three-probe-source.tar.gz"
NEW_BUNDLE = "R787-precision-retained-deeper-current.tar.gz"
OLD_RECEIPT = "precision-old-sources-receipt.json"
NEW_RECEIPT = "precision-deeper-current-source-receipt.json"
SCHEMA_HELPER_SHA = "d363d0e90db1332bee54512c28a1ef14d2d2bbeed62cc65178cf14d3470bfeea"
SOURCE_IO_SHA = "7449600243a81bd31b5109fdadd0da2e3aa1930fea00772761154703555d4ed9"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
OLD_CORE_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
LEGACY_CORE_SHA = "c642ec35823dace0ccac4e225e43581398dcce5737dd51cae6a2a903f6028700"
FIELD_CORE_SHA = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
OLD_CONFIGURATION_SHA = "71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d"
METHOD_SHA = "bc91a89140d912b1e3f7da9ec9c12b742884084e60860cc408cbacb9d7b54f0f"
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
H64 = re.compile(r"[0-9a-f]{64}")
PRECISION_STRATEGY = {
    "old_complete_basis": "unchanged full 56 rows from the actual completed C0,C1,A0 lattice",
    "fixed_original_probe_indices_C_then_A": [0, 1, 1214],
    "full_A_and_C_reduction_compatibility_required": True,
    "residual": "((N_i-D*x_i_new) mod M_new)/M_old in the original integral 14-coordinate order",
    "minor": "first independent original rows of E mod ell; all42 target columns retained",
    "inverse": "42x42 prime inverse, then V*(2I-U*V) with precision doubling modulo ell^d",
    "kernel_rows": "free_rows_then_pivot_rows; K=[I,-E_F*U_inverse;0,qI]*Pi",
    "new_basis": "H_new=K*H_old over Z",
    "LLL": "one new 56-dimensional LLL; all rows and a full canonical-graph unimodular witness",
    "candidate_lift": "nonfree coordinates=center(D*new_original_lift); actual chosen free C=D",
    "old_exact_or_Omega_rejection_reused": False,
    "success": "unchanged complete original129-by280 equations and nonzero B",
    "output_names": "new configuration only: R787-projective-*.json.gz and original RECIPE",
    "normalized_Dixon_digits_computed": 0,
}
SCHEMA = None
IO = None


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temporary.write_bytes(raw)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name
    assert name not in ("", ".", "..") and "\\" not in name


def plain(row):
    answer = {key: row[key] for key in ("file", "bytes", "sha256")}
    safe_name(answer["file"])
    assert type(answer["bytes"]) is int and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def bound(directory, row):
    row = plain(row)
    path = Path(directory)/row["file"]
    assert path.is_file() and file_spec(path) == row
    return path


def topic_path(relative):
    value = PurePosixPath(relative)
    assert not value.is_absolute() and ".." not in value.parts
    path = (TOPIC/str(value)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def source_identity(source):
    return {key: source[key] for key in BASE}


def import_io(item):
    global SCHEMA, IO
    path = S/item["source_schema_helper"]
    assert path.name == "R787_fixed_C_prefix_obstruction_public.py"
    assert sha(path) == item["source_schema_helper_sha256"] == SCHEMA_HELPER_SHA
    spec = importlib.util.spec_from_file_location("precision_frozen_original_source_schema", path)
    SCHEMA = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SCHEMA)
    assert item["source_io_helper"] == "R787_projective_three_probe_public.py"
    assert item["source_io_helper_sha256"] == SOURCE_IO_SHA
    assert item["io_helper_sha256"] == RANGE_SHA
    SCHEMA.import_io(item)
    IO = SCHEMA.IO


def prepare_old_sources(item, out, allow_download=True):
    """Transport the completed 56 source and its original carriers, never their arithmetic."""
    retained = out.parent/"retained"
    candidates = out.parent/"candidates"
    three = candidates/"three_probe"
    three.mkdir(parents=True, exist_ok=True)
    receipt_path = out/OLD_RECEIPT
    carriers = (BUNDLE, TWO_BUNDLE, THREE_BUNDLE)
    if all((out/name).is_file() for name in carriers) and receipt_path.exists():
        receipt = read(receipt_path)
        assert receipt["result"] == RESULT and receipt["complete"] is True
        assert receipt["completed_three_probe_source"] == item["completed_three_probe_source"]
        assert receipt["previous_two_probe_source"] == item["previous_two_probe_source"]
        for name in carriers:
            bound(out, receipt["carriers"][name])
        SCHEMA.extract_flat_bundle(out/THREE_BUNDLE, three, receipt["three_probe_inventory"], extract=True)
        review = SCHEMA.review_sources(item, out, retained, candidates)
        assert review == receipt["review"]
        return retained, candidates
    assert allow_download, "The existing source-bound carriers are required for read-only verification."
    source = item["completed_three_probe_source"]
    archive = IO.Archive(source, out.parent/"download-completed56-source", whole=False)
    try:
        manifest_path = archive.extract_bound("full-outputs-manifest.json", source["manifest_sha256"],
            three/"full-outputs-manifest.json", source["manifest_bytes"])
        manifest = read(manifest_path)
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
        members = archive.by_name.get(REFERENCE, [])
        assert len(members) == 1 and members[0].file_size < 1024*1024
        raw = archive.zip.read(members[0])
        assert len(raw) == members[0].file_size
        (three/REFERENCE).write_bytes(raw)
        assert set(archive.by_name) == set(entries) | {"full-outputs-manifest.json", REFERENCE}
        for name, row in entries.items():
            members = archive.by_name[name]
            assert len(members) == 1 and members[0].file_size == row["bytes"]
        selected = sorted(set(entries)-{BUNDLE, TWO_BUNDLE})
        assert all(entries[name]["bytes"] <= 32*1024*1024 for name in selected)
        assert sum(entries[name]["bytes"] for name in selected) <= 192*1024*1024
        archive.extract_many([(name, entries[name]["sha256"], three/name, entries[name]["bytes"])
                              for name in selected])
        SCHEMA.three_probe_schema(item, three)
        for name in (BUNDLE, TWO_BUNDLE):
            row = entries[name]
            archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
        review = SCHEMA.review_sources(item, out, retained, candidates)
        rows = review["source_three_probe_files"]
        SCHEMA.create_flat_bundle(three, out/THREE_BUNDLE, rows)
        receipt = {
            "result": RESULT, "complete": True,
            "completed_three_probe_source": source,
            "previous_two_probe_source": item["previous_two_probe_source"],
            "review": review, "three_probe_inventory": rows,
            "carriers": {name: file_spec(out/name) for name in carriers},
            "source_transfer": archive.receipt(),
            "all_old_carriers_and_original_members_size_SHA256_verified": True,
            "whole_source_ZIP_rehashed_in_this_Range_transfer": False,
            "old_Dixon_LLL_real_rows_Laurent_or_candidate_arithmetic_recomputed": False,
            "old_98_rejections_reused_as_new_precision_candidate_results": False,
            "raw_carriers_exist_only_in_active_one_day_artifact": True,
        }
        save(receipt_path, receipt)
        print("PRECISION_OLD_SOURCE_REVIEW="+json.dumps({
            "source": source_identity(source), "original_input_file_count": 1380,
            "old_two_probe_file_count": len(review["source_two_probe_files"]),
            "old_three_probe_file_count": len(rows),
            "all_selected_bytes_SHA_verified": True, "old_arithmetic_recomputed": False,
            "source_transfer": archive.receipt()}, sort_keys=True), flush=True)
        return retained, candidates
    finally:
        archive.close()


def review_new_current_source(item, directory, retained):
    """Only source hashes and small source metadata; the core reads the complete current once."""
    source, checkpoint = item["new_current_source"], item["new_checkpoint"]
    assert source is not None and checkpoint is not None
    assert source["result"] == RESULT and source["core_sha256"] == OLD_CORE_SHA
    assert source["configuration_sha256"] == OLD_CONFIGURATION_SHA
    assert checkpoint["prime"] == 1000000753
    assert type(checkpoint["digits"]) is int and checkpoint["digits"] > 430
    expected_lift = "R787-prime-1000000753-dixon-"+str(checkpoint["digits"]).zfill(8)+".json.gz"
    assert checkpoint["lift_file"] == expected_lift == source["current"]["file"]
    rows = {name: plain(row) for name, row in source["files"].items()}
    assert set(path.name for path in directory.iterdir() if path.is_file()) == set(rows)
    for name, row in rows.items():
        assert name == row["file"] and file_spec(directory/name) == row
    assert rows["full-outputs-manifest.json"]["sha256"] == source["manifest_sha256"]
    assert rows["full-outputs-manifest.json"]["bytes"] == source["manifest_bytes"]
    manifest = read(directory/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    for name, row in rows.items():
        if name != "full-outputs-manifest.json":
            assert row == entries[name]
    assert plain(source["current"]) == rows[expected_lift]
    initial = read(directory/"public-actions-input.json")
    run = read(directory/"run-receipt.json")
    core = read(directory/"core-receipt.json") if "core-receipt.json" in rows else None
    assert initial["result"] == run["result"] == RESULT
    if core is not None:
        assert core["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == initial["job"]["core_sha256"] == OLD_CORE_SHA
    if core is not None:
        assert core["source_sha256"] == OLD_CORE_SHA
    assert initial["driver_sha256"] == source["wrapper_sha256"]
    if core is not None:
        assert run["core_receipt_sha256"] == rows["core-receipt.json"]["sha256"]
        assert type(core["complete"]) is bool
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
        assert run["process_exit_code"] != 0
    assert run["process_exit_code"] in source["accepted_checkpoint_exit_codes"]
    assert type(run["complete"]) is bool
    if run["process_exit_code"] == 0:
        assert core is not None and run["complete"] is core["complete"] is True
    else:
        assert run["complete"] is False
    assert initial["field_core_sha256"] == item["field_core_sha256"] == FIELD_CORE_SHA
    assert initial["method_sha256"] == item["R787_method_sha256"]
    assert initial["proof_sha256"] == item["R786_proof_sha256"]
    assert initial["job"]["retained_artifacts"] == item["retained_artifacts"]
    original = SCHEMA.LEGACY.original_source(item, retained)
    for key in ("chart_file", "selection_file"):
        name = checkpoint[key]
        assert name == item["checkpoint"][key]
        assert rows[name] == plain(original.files[name])
        stage = read(directory/name)
        assert stage["complete"] is True
        assert stage["configuration"] == original.tag
        assert fingerprint(stage["configuration"]) == OLD_CONFIGURATION_SHA
    assert checkpoint["rational_blocks_file"] == item["checkpoint"]["rational_blocks_file"]
    assert initial["job"]["result"] == RESULT
    return {
        "source": source_identity(source), "configuration_sha256": OLD_CONFIGURATION_SHA,
        "current": plain(source["current"]), "declared_digits": checkpoint["digits"],
        "selected_files": [rows[name] for name in sorted(rows)],
        "all_selected_source_bytes_and_SHA256_verified": True,
        "chart_selection_original_field_and_child_identities_unchanged": True,
        "large_current_JSON_loaded_by_this_IO_runner": False,
        "complete_current_shapes_normalization_and_full_AC_compatibility_are_core_checks": True,
        "new_normalized_Dixon_digits_computed_by_this_IO_runner": 0,
    }


def prepare_new_current_source(item, out, retained, allow_download=True):
    directory = out.parent/"future_current"
    directory.mkdir(parents=True, exist_ok=True)
    receipt_path = out/NEW_RECEIPT
    if (out/NEW_BUNDLE).exists() and receipt_path.exists():
        receipt = read(receipt_path)
        assert receipt["result"] == RESULT and receipt["complete"] is True
        assert receipt["new_current_source"] == item["new_current_source"]
        assert receipt["new_checkpoint"] == item["new_checkpoint"]
        bound(out, receipt["input_bundle"])
        SCHEMA.extract_flat_bundle(out/NEW_BUNDLE, directory, receipt["files"], extract=True)
        review = review_new_current_source(item, directory, retained)
        assert review == receipt["review"]
        return directory
    assert allow_download, "The actual deeper-current carrier is required for verification."
    source = item["new_current_source"]
    assert source is not None, "No deeper original current has been bound to this request."
    archive = IO.Archive(source, out.parent/"download-actual-deeper-current", whole=False)
    try:
        files = source["files"]
        manifest = plain(files["full-outputs-manifest.json"])
        archive.extract_bound(manifest["file"], manifest["sha256"], directory/manifest["file"], manifest["bytes"])
        rows = {entry["file"]: plain(entry) for entry in read(directory/manifest["file"])["files"]}
        for name, entry in files.items():
            if name != "full-outputs-manifest.json":
                assert plain(entry) == rows[name]
        archive.extract_many([(name, entry["sha256"], directory/name, entry["bytes"])
                              for name, entry in files.items()])
        review = review_new_current_source(item, directory, retained)
        selected = review["selected_files"]
        SCHEMA.create_flat_bundle(directory, out/NEW_BUNDLE, selected)
        save(receipt_path, {
            "result": RESULT, "complete": True, "new_current_source": source,
            "new_checkpoint": item["new_checkpoint"], "review": review,
            "files": selected, "input_bundle": file_spec(out/NEW_BUNDLE),
            "source_transfer": archive.receipt(),
            "whole_source_ZIP_rehashed_in_this_Range_transfer": False,
            "new_Dixon_lattice_or_candidate_arithmetic_performed": False,
        })
        print("PRECISION_NEW_CURRENT_SOURCE_REVIEW="+json.dumps({
            "source": source_identity(source), "current": plain(source["current"]),
            "declared_digits": item["new_checkpoint"]["digits"],
            "all_selected_bytes_SHA_verified": True,
            "large_current_JSON_not_materialized_in_IO": True,
            "full_AC_and_probe_compatibility_remain_explicit_core_checks": True,
            "source_transfer": archive.receipt()}, sort_keys=True), flush=True)
        return directory
    finally:
        archive.close()


def expected_tag(item, retained):
    original = SCHEMA.LEGACY.original_source(item, retained)
    tag = dict(original.tag)
    digits = item["new_checkpoint"]["digits"]
    increment = digits-430
    assert increment > 0
    tag.update({
        "result": RESULT, "source_sha256": item["core_sha256"],
        "projective_mode": True,
        "projective_algorithm": "integral-L-fixed-three-probe-precision-kernel-56-lattice-v1",
        "projective_method_sha256": item["projective_method_sha256"],
        "legacy_three_probe_core_sha256": item["legacy_core_sha256"],
        "pinned_R787_configuration_sha256": OLD_CONFIGURATION_SHA,
        "retained_source": item["retained_source"], "checkpoint": item["checkpoint"],
        "previous_two_probe_source": item["previous_two_probe_source"],
        "completed_three_probe_source": item["completed_three_probe_source"],
        "new_current_source": item["new_current_source"],
        "new_checkpoint": item["new_checkpoint"],
        "precision_increment_strategy": PRECISION_STRATEGY,
        "LLL_integer_lattice_dimension": 56,
        "original_lifting_reexecuted": False,
        "old_branch_inverse_used": False,
        "old_42_or_56_dimensional_LLL_reexecuted": False,
        "old_exact_or_Omega_rejection_reused": False,
        "parent_module_globals_or_source_identity_modified": False,
        "old_Dixon_digits": 430, "new_Dixon_digits": digits,
        "precision_increment_digits": increment,
        "actual_precision_increment_modulus": str(1000000753**increment),
        "fixed_original_probe_indices_C_then_A": [0, 1, 1214],
        "new_normalized_Dixon_digits_computed": 0,
    })
    return tag


def mathematical_job(item):
    keys = ("result", "p", "core_sha256", "legacy_core_sha256",
            "projective_method_sha256", "field_core_sha256",
            "pinned_R787_configuration_sha256", "R787_method_sha256", "R786_proof_sha256",
            "retained_source", "retained_artifacts", "checkpoint",
            "previous_two_probe_source", "completed_three_probe_source",
            "new_current_source", "new_checkpoint")
    return {key: item[key] for key in keys}


def guard_sources(item):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["new_current_source"] is not None and item["new_checkpoint"] is not None
    assert item["checkpoint"]["digits"] == 430 and item["checkpoint"]["prime"] == 1000000753
    assert item["new_checkpoint"]["prime"] == 1000000753
    assert type(item["new_checkpoint"]["digits"]) is int and item["new_checkpoint"]["digits"] > 430
    assert item["legacy_core_sha256"] == LEGACY_CORE_SHA
    assert item["field_core_sha256"] == FIELD_CORE_SHA
    assert item["pinned_R787_configuration_sha256"] == OLD_CONFIGURATION_SHA
    assert item["projective_method_sha256"] == METHOD_SHA
    for key in ("core", "legacy_core", "field_core", "source_schema_helper", "source_io_helper", "io_helper"):
        safe_name(item[key])
        assert sha(S/item[key]) == item[key+"_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert sha(topic_path(item["method"])) == item["projective_method_sha256"]
    assert sha(REPO/"README.md") == item["current_readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["current_readme_sha256"]["topic"]
    assert set(item["projective_search_controls"]) == {"maximum_nodes", "maximum_lattices"}
    assert type(item["projective_search_controls"]["maximum_nodes"]) is int
    assert item["projective_search_controls"]["maximum_nodes"] > 0
    assert item["projective_search_controls"]["maximum_lattices"] == 1
    import_io(item)


def restore_resume(item, out):
    previous = item.get("resume")
    if previous is None:
        return
    assert previous["result"] == RESULT and previous["core_sha256"] == item["core_sha256"]
    directory = out.parent/"previous-precision-metadata"
    directory.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(previous, out.parent/"download-precision-continuation", whole=False)
    try:
        path = archive.extract_bound("full-outputs-manifest.json", previous["manifest_sha256"],
                                     directory/"full-outputs-manifest.json", previous["manifest_bytes"])
        manifest = read(path)
        assert manifest["result"] == RESULT
        entries = {entry["file"]: plain(entry) for entry in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        def metadata(name):
            row = entries[name]
            return read(archive.extract_bound(name, row["sha256"], directory/name, row["bytes"]))
        initial, run = metadata("public-actions-input.json"), metadata("run-receipt.json")
        assert initial["result"] == run["result"] == RESULT
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["source_commit"] == run["source_commit"] == previous["source_commit"]
        assert str(run["workflow_run_id"]) == str(previous["run_id"])
        assert initial["core_sha256"] == item["core_sha256"]
        assert initial["driver_sha256"] == previous.get("wrapper_sha256", item["wrapper_sha256"])
        assert mathematical_job(initial["job"]) == mathematical_job(item)
        if "core-receipt.json" in entries:
            core = metadata("core-receipt.json")
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        else:
            assert run["core_receipt_sha256"] is None
            assert run["complete"] is False and run["process_exit_code"] != 0
        old_receipt, new_receipt = metadata(OLD_RECEIPT), metadata(NEW_RECEIPT)
        assert old_receipt["result"] == new_receipt["result"] == RESULT
        assert old_receipt["complete"] is new_receipt["complete"] is True
        assert old_receipt["completed_three_probe_source"] == item["completed_three_probe_source"]
        assert new_receipt["new_current_source"] == item["new_current_source"]
        required = {BUNDLE, TWO_BUNDLE, THREE_BUNDLE, NEW_BUNDLE, OLD_RECEIPT, NEW_RECEIPT}
        for name in (BUNDLE, TWO_BUNDLE, THREE_BUNDLE):
            assert plain(old_receipt["carriers"][name]) == entries[name]
        assert plain(new_receipt["input_bundle"]) == entries[NEW_BUNDLE]
        names = sorted(name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz"))
        required.update(names)
        recipe_name = "R787-original-function-recipe.json.gz"
        if recipe_name in entries:
            required.add(recipe_name)
        final = metadata(FINAL) if FINAL in entries else None
        if final is not None:
            assert final["result"] == RESULT
            assert final["configuration"]["source_sha256"] == item["core_sha256"]
            if final["complete"]:
                required.add(FINAL)
        for name in sorted(required):
            row = entries[name]
            archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
        retained, candidates = prepare_old_sources(item, out, allow_download=False)
        new_current = prepare_new_current_source(item, out, retained, allow_download=False)
        tag = expected_tag(item, retained)
        assert initial["actual_precision_configuration"] == tag
        for name in names:
            stage = read(out/name)
            assert stage["result"] == RESULT and stage["configuration"] == tag
            assert type(stage["complete"]) is bool
            if not stage["complete"]:
                assert name.endswith("-current.json.gz")
        if recipe_name in required:
            recipe = read(out/recipe_name)
            assert recipe["configuration"] == tag and recipe["complete"] is True
        if final is not None and final["complete"]:
            assert final["configuration"] == tag
            # Inventory is immutable for a successful relation; failed FINAL may
            # precede newer complete stages and is deliberately not restored.
            ref = plain(final["stage_manifest"])
            inventory = read(bound(out, ref))
            assert inventory["configuration"] == tag and inventory["complete"] is True
            for row in inventory["files"]:
                bound(out, row)
            bound(out, final["resume_state"])
        save(out/"precision-restore-receipt.json", {
            "result": RESULT, "complete": True, "source": previous,
            "restored_files": [entries[name] for name in sorted(required)],
            "completed_new_math_stages_preserve_original_new_tag": True,
            "old_precision_42_or_56_stages_relabelled": False,
            "completed_Dixon_LLL_or_candidate_arithmetic_reexecuted": False,
            "new_false_FINAL_restored_as_frozen_current": False,
            "source_transfer": archive.receipt(),
        })
    finally:
        archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and path.name.endswith((".tmp", ".partial", ".download")):
            path.unlink()
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = [dict(file_spec(path), artifact=artifact, included_in_git=False)
               for path in sorted(out.iterdir()) if path.is_file()
               and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    save(out/"full-outputs-manifest.json", {
        "result": RESULT, "projective_mode": True, "files": entries,
        "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "raw_outputs_or_carriers_in_git_or_release": False,
    })
    save(out/REFERENCE, {
        "result": RESULT, "projective_mode": True,
        "manifest_file": "full-outputs-manifest.json",
        "manifest_sha256": sha(out/"full-outputs-manifest.json"),
        "manifest_bytes": (out/"full-outputs-manifest.json").stat().st_size,
        "file_count": len(entries), "full_outputs_artifact": artifact,
        "automatic_git_or_release_publication": False,
    })


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    initial = {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(S/item["core"]),
        "legacy_core_sha256": sha(S/item["legacy_core"]),
        "field_core_sha256": sha(S/item["field_core"]),
        "method_sha256": sha(topic_path(item["method"])),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "source_schema_helper_sha256": sha(S/item["source_schema_helper"]),
        "source_io_helper_sha256": sha(S/item["source_io_helper"]),
        "io_helper_sha256": sha(S/item["io_helper"]),
        "root_readme_sha256": sha(REPO/"README.md"),
        "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "old_Dixon_digits": 430, "new_checkpoint": item["new_checkpoint"],
        "new_normalized_Dixon_digits_computed_by_this_consumer": 0,
        "old_42_56_LLL_or_old_candidates_recomputed": False,
    }
    save(out/"public-actions-input.json", initial)
    code, error = 1, None
    try:
        guard_sources(item)
        restore_resume(item, out)
        retained, candidates = prepare_old_sources(item, out)
        new_current = prepare_new_current_source(item, out, retained)
        initial["actual_precision_configuration"] = expected_tag(item, retained)
        save(out/"public-actions-input.json", initial)
        config = out.parent/"precision-expanded-job.json"
        save(config, item)
        command = [sys.executable, str(S/item["core"]),
                   "--config", str(config), "--method", str(topic_path(item["method"])),
                   "--field-core", str(S/item["field_core"]),
                   "--retained", str(retained),
                   "--previous-search", str(candidates/"two_probe"),
                   "--previous-three-probe", str(candidates/"three_probe"),
                   "--new-current", str(new_current),
                   "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"core.log").open("w", encoding="utf-8") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=float(item["budget_minutes"])*60+900)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait(timeout=30)
                code, error = 124, "Outer timeout; completed atomic mathematical stages and source carriers retained."
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
        print("PRECISION_PUBLIC_ERROR="+json.dumps({"error": error}), flush=True)
    core = read(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None
    final = read(out/FINAL) if (out/FINAL).exists() else None
    complete = code == 0 and core is not None and final is not None and core.get("complete") is True and final.get("complete") is True
    save(out/"run-receipt.json", {
        "result": RESULT, "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_run_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "core_receipt_sha256": sha(out/"core-receipt.json") if core is not None else None,
        "process_exit_code": code, "complete": complete, "error": error,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "old_Dixon_LLL_or_candidate_arithmetic_recomputed": False,
    })
    output_manifest(out)
    print("PRECISION_RUN_RECEIPT="+json.dumps(read(out/"run-receipt.json"), sort_keys=True), flush=True)
    return code if not complete else 0


def verify(item, out):
    """All output/source byte identities and the complete mathematical certificate interface."""
    guard_sources(item)
    initial = read(out/"public-actions-input.json")
    run = read(out/"run-receipt.json")
    core = read(out/"core-receipt.json")
    assert initial["job"] == item
    assert initial["result"] == run["result"] == core["result"] == RESULT
    assert initial["core_sha256"] == core["source_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["legacy_core_sha256"] == item["legacy_core_sha256"]
    assert initial["field_core_sha256"] == item["field_core_sha256"]
    assert initial["method_sha256"] == item["projective_method_sha256"]
    assert initial["source_commit"] == run["source_commit"]
    assert run["complete"] is core["complete"] is True
    assert run["process_exit_code"] == 0 and run["error"] is None
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["certificate_sha256"] == sha(out/FINAL)
    retained, candidates = prepare_old_sources(item, out, allow_download=False)
    prepare_new_current_source(item, out, retained, allow_download=False)
    tag = expected_tag(item, retained)
    assert initial["actual_precision_configuration"] == tag
    certificate = read(out/FINAL)
    assert certificate["result"] == RESULT and certificate["complete"] is True
    assert certificate["configuration"] == tag and certificate["projective_mode"] is True
    assert certificate["p"] == 41
    assert certificate["original_map_index"] == 4 and certificate["original_map_degree"] == "1206"
    assert certificate["original_full_L_retained"] is True
    for key in ("exact_nonzero_A_B_relation_verified", "same_normalized_1186_direction_verified",
                "actual_y_map_recovered"):
        assert certificate[key] is True
    assert certificate["beta_or_height_computed"] is False
    assert certificate["exact_verified_Laurent_exponents"] == [-1, 127]
    assert certificate["exact_verified_t_coordinates"] == 20
    assert certificate["exact_verified_Q_coordinates_per_order"] == 280
    assert certificate["exact_verified_orders"] == 129
    assert certificate["actual_auxiliary_prime"] == 1000000753
    assert certificate["actual_Dixon_digits"] == item["new_checkpoint"]["digits"]
    assert certificate["source_Dixon_digits"] == item["new_checkpoint"]["digits"]
    assert certificate["old_Dixon_digits"] == 430
    assert certificate["precision_increment_digits"] == item["new_checkpoint"]["digits"]-430
    assert certificate["new_normalized_Dixon_digits_computed"] == 0
    assert certificate["new_current_source"] == item["new_current_source"]
    assert certificate["previous_exact_candidate_rejections_referenced"] == 0
    inventory_ref = plain(certificate["stage_manifest"])
    inventory = read(bound(out, inventory_ref))
    assert inventory["result"] == RESULT and inventory["configuration"] == tag
    assert inventory["complete"] is True
    stages = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(stages) == len(inventory["files"])
    recipe_name = "R787-original-function-recipe.json.gz"
    for name, row in stages.items():
        assert name.startswith(PREFIX) and name.endswith(".json.gz") or name == recipe_name
        value = read(bound(out, row))
        assert value["result"] == RESULT and value["configuration"] == tag
        assert value["complete"] is True
        if name.endswith("-result.json.gz") and "previous_exact_rejection_reused" in value:
            assert value["previous_exact_rejection_reused"] is False
            assert value["previous_exact_rejection_reference"] is None
            assert value["new_exact_candidate_evaluation_performed"] is True
    queue_ref = plain(certificate["resume_state"])
    queue = read(bound(out, queue_ref))
    assert queue_ref["file"].startswith(PREFIX) and queue_ref["file"].endswith("-current.json.gz")
    assert queue["result"] == RESULT and queue["configuration"] == tag and queue["complete"] is False
    assert queue["referenced_previous_rejection_ids"] == []
    assert len(queue["processed_node_ids"]) == len(set(queue["processed_node_ids"]))
    assert set(queue["processed_node_ids"]) == set(queue["new_exact_candidate_ids"])
    assert len(queue["processed_node_ids"]) == certificate["completed_search_nodes"]
    assert len(queue["new_exact_candidate_ids"]) == certificate["new_exact_candidate_evaluations"]
    recipe_ref = plain(certificate["relation_spec"])
    assert recipe_ref == plain(certificate["function_recipe"]) == stages[recipe_name]
    recipe = read(bound(out, recipe_ref))
    assert recipe["candidate_only_until_full_exact_verification"] is False
    assert recipe["full_129_original_relations_verified"] is True
    assert recipe["same_normalized_1186_direction_verified"] is True
    verify_precision_interfaces(item, out, certificate, stages, tag)
    manifest = read(out/"full-outputs-manifest.json")
    assert manifest["result"] == RESULT and manifest["projective_mode"] is True
    output_files = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(output_files) == len(manifest["files"])
    for row in output_files.values():
        bound(out, row)
    expected = {path.name for path in out.iterdir() if path.is_file()}-{"full-outputs-manifest.json", REFERENCE}
    assert set(output_files) == expected
    reference = read(out/REFERENCE)
    assert reference["result"] == RESULT and reference["projective_mode"] is True
    assert reference["manifest_sha256"] == sha(out/"full-outputs-manifest.json")
    assert reference["manifest_bytes"] == (out/"full-outputs-manifest.json").stat().st_size
    assert reference["file_count"] == len(output_files)
    print("PRECISION_COMPLETE_IO_REVIEW="+json.dumps({
        "result": RESULT, "complete": True, "output_file_count": len(output_files),
        "new_current": item["new_current_source"]["current"],
        "actual_Dixon_digits": certificate["actual_Dixon_digits"],
        "precision_increment_digits": certificate["precision_increment_digits"],
        "new_normalized_Dixon_digits_computed": 0,
        "completed_new_candidates": certificate["completed_search_nodes"],
        "old_candidate_rejections_reused": 0,
        "full129_by280_relation_certified": True,
        "all_selected_source_and_output_bytes_SHA256_verified": True,
        "mathematical_core_imported_by_IO_verifier": False,
        "certificate": file_spec(out/FINAL)}, sort_keys=True), flush=True)
    return 0


def verify_precision_interfaces(item, out, certificate, stages, tag):
    """Structural and source identity checks only; no matrix products or lattice arithmetic."""
    def stage(entry):
        entry = plain(entry)
        assert entry == stages[entry["file"]]
        value = read(bound(out, entry))
        assert value["configuration"] == tag and value["complete"] is True
        return value
    def rectangle(values, height, width):
        assert len(values) == height
        assert all(len(row) == width and all(isinstance(x, str) for x in row) for row in values)

    old = item["completed_three_probe_source"]
    assert plain(certificate["old_complete_basis"]) == plain(old["raw_lattice_stage"])
    old_directory = out.parent/"candidates"/"three_probe"
    old_basis = read(bound(old_directory, old["raw_lattice_stage"]))
    old_witness = read(bound(old_directory, old["lattice_stage"]))
    assert old_basis["configuration"]["source_sha256"] == LEGACY_CORE_SHA
    assert old_basis["configuration"] == old_witness["configuration"]
    assert old_basis["all_56_reduced_rows_saved"] is True
    rectangle(old_basis["all_56_reduced_rows"], 56, 56)
    assert old_witness["new_56_rows_are_a_full_integer_lattice_basis"] is True
    assert old_witness["new_basis_change_determinant"] in ("1", "-1")
    assert certificate["new_current_stage"] == plain(item["new_current_source"]["current"])
    assert certificate["fixed_probe_indices_C_then_A"] == [0, 1, 1214]
    assert certificate["actual_third_probe_A_index"] == 0
    assert certificate["complete_new_precision_lattice_basis_certified"] is True
    assert certificate["all_full_A_and_C_source_reductions_verified"] is True
    assert certificate["small42_precision_residual_inverse_computed"] is True
    assert certificate["composite_modulus_matrix_inversion"] is (item["new_checkpoint"]["digits"]-430 > 1)
    assert certificate["original_large_Schur_or_A_inverse_recomputed"] is False
    assert certificate["old_42_or_56_dimensional_LLL_recomputed"] is False
    assert certificate["old_exact_or_Omega_rejections_reused"] is False

    old_manifest = read(out.parent/"retained"/"R787"/"full-outputs-manifest.json")
    old_entries = {entry["file"]: plain(entry) for entry in old_manifest["files"]}
    old_lift = old_entries[item["checkpoint"]["lift_file"]]
    assert old_lift["sha256"] == item["retained_source"]["files"][item["checkpoint"]["lift_file"]]
    compatibility = stage(certificate["source_compatibility"])
    assert compatibility["old_current"] == old_lift
    assert compatibility["new_current"] == plain(item["new_current_source"]["current"])
    assert compatibility["old_Dixon_digits"] == 430
    assert compatibility["new_Dixon_digits"] == item["new_checkpoint"]["digits"]
    assert compatibility["prime"] == 1000000753
    assert compatibility["increment_modulus"] == tag["actual_precision_increment_modulus"]
    assert compatibility["A_dimensions"] == [1234, 14] and compatibility["C_dimensions"] == [1214, 14]
    assert compatibility["A_coordinate_count"] == 17276 and compatibility["C_coordinate_count"] == 16996
    for key in ("all_A_reductions_verified", "all_C_reductions_verified",
                "same_original_chart_and_full_free_C_pattern_verified",
                "three_probe_reductions_verified"):
        assert compatibility[key] is True
    assert compatibility["old_exact_or_Omega_rejections_reused"] is False
    assert compatibility["new_normalized_Dixon_digits_computed"] == 0

    source_basis = stage(certificate["source_basis"])
    assert source_basis["old_complete_basis"] == plain(old["raw_lattice_stage"])
    assert source_basis["old_complete_basis_witness"] == plain(old["lattice_stage"])
    assert source_basis["source_compatibility"] == plain(certificate["source_compatibility"])
    assert source_basis["old_configuration_sha256"] == fingerprint(old_basis["configuration"])
    assert source_basis["fixed_original_probe_indices_C_then_A"] == [0, 1, 1214]
    rectangle(source_basis["old_probes"], 3, 14)
    rectangle(source_basis["new_probes"], 3, 14)
    for key in ("old_full_56_basis_consumed_with_unchanged_configuration",
                "old_basis_unimodular_witness_consumed_not_recomputed",
                "old_third_probe_selection_not_reexecuted"):
        assert source_basis[key] is True
    assert source_basis["old_42_or_56_dimensional_LLL_reexecuted"] is False
    assert source_basis["old_exact_or_Omega_rejections_reused"] is False

    residual = stage(certificate["precision_residual_matrix"])
    assert residual["old_complete_basis"] == plain(old["raw_lattice_stage"])
    assert residual["new_current"] == plain(item["new_current_source"]["current"])
    assert residual["source_compatibility"] == plain(certificate["source_compatibility"])
    assert residual["shape"] == [56, 42]
    assert residual["increment_modulus"] == tag["actual_precision_increment_modulus"]
    rectangle(residual["residual_integer_rows_mod_increment"], 56, 42)
    assert residual["all56_source_rows_and168_original_order_products_completed"] is True
    assert residual["all2352_integer_divisions_by_old_modulus_verified"] is True
    assert residual["branch_evaluation_or_Schur_inverse_used"] is False
    assert residual["new_normalized_Dixon_digits_computed"] == 0
    assert len(residual["row_stages"]) == 56
    for index, entry in enumerate(residual["row_stages"]):
        row = stage(entry)
        assert row["old_basis_row"] == index
        assert row["old_complete_basis"] == plain(old["raw_lattice_stage"])
        assert row["new_current"] == plain(item["new_current_source"]["current"])
        assert row["source_compatibility"] == plain(certificate["source_compatibility"])
        assert row["all42_integer_divisions_by_old_modulus_verified"] is True
        assert len(row["residual_values_mod_increment"]) == 42
        assert row["residual_values_mod_increment"] == residual["residual_integer_rows_mod_increment"][index]
        assert row["new_normalized_Dixon_digits_computed"] == 0

    minor = stage(certificate["unit_minor"])
    assert minor["residual_matrix"] == plain(certificate["precision_residual_matrix"])
    assert minor["prime"] == 1000000753 and minor["minor_rank"] == 42
    pivots, free = minor["pivot_original_row_indices"], minor["free_original_row_indices"]
    assert len(pivots) == 42 and len(free) == 14
    assert sorted(pivots+free) == list(range(56))
    assert pivots == sorted(pivots) and free == sorted(free)
    assert minor["all42_target_columns_retained"] is True
    rectangle(minor["minor_integer_rows_mod_prime"], 42, 42)
    rectangle(minor["minor_inverse_integer_rows_mod_prime"], 42, 42)
    assert 0 < int(minor["actual_minor_determinant_mod_prime"]) < 1000000753
    assert minor["both_prime_inverse_products_verified"] is True
    assert minor["selection"] == PRECISION_STRATEGY["minor"]
    assert minor["surjectivity_witness_actually_computed"] is True

    inverse = stage(certificate["precision_inverse"])
    assert inverse["residual_matrix"] == plain(certificate["precision_residual_matrix"])
    assert inverse["unit_minor"] == plain(certificate["unit_minor"])
    assert inverse["precision_increment_exponent"] == certificate["precision_increment_digits"]
    assert inverse["modulus"] == tag["actual_precision_increment_modulus"]
    rectangle(inverse["inverse_integer_rows"], 42, 42)
    assert inverse["both_inverse_products_verified_mod_actual_power"] is True
    assert inverse["old_normalized_Dixon_or_large_branch_inverse_computed"] is False
    seen_inverse = set()
    cursor, expected_precision = plain(certificate["precision_inverse"]), certificate["precision_increment_digits"]
    while cursor is not None:
        assert cursor["file"] not in seen_inverse
        seen_inverse.add(cursor["file"])
        value = stage(cursor)
        assert value["residual_matrix"] == plain(certificate["precision_residual_matrix"])
        assert value["unit_minor"] == plain(certificate["unit_minor"])
        assert value["prime"] == 1000000753
        assert value["precision_increment_exponent"] == expected_precision
        assert value["both_inverse_products_verified_mod_actual_power"] is True
        assert value["old_normalized_Dixon_or_large_branch_inverse_computed"] is False
        rectangle(value["inverse_integer_rows"], 42, 42)
        previous = value["previous_inverse"]
        if previous is None:
            assert expected_precision == 1
        else:
            previous_data = stage(previous)
            previous_precision = previous_data["precision_increment_exponent"]
            assert 1 <= previous_precision < expected_precision
            assert expected_precision == min(2*previous_precision, certificate["precision_increment_digits"])
            expected_precision = previous_precision
        cursor = previous

    kernel = stage(certificate["kernel_basis"])
    assert kernel["old_complete_basis"] == plain(old["raw_lattice_stage"])
    assert kernel["residual_matrix"] == plain(certificate["precision_residual_matrix"])
    assert kernel["unit_minor"] == plain(certificate["unit_minor"])
    assert kernel["precision_inverse"] == plain(certificate["precision_inverse"])
    assert kernel["free_original_row_indices"] == free and kernel["pivot_original_row_indices"] == pivots
    assert kernel["coefficient_row_permutation_F_then_P"] == free+pivots
    assert kernel["dimension"] == 56 and kernel["residual_rank"] == 42
    assert kernel["permutation_determinant"] in (-1, 1)
    rectangle(kernel["W_negative_E_free_times_U_inverse_mod_q"], 14, 42)
    rectangle(kernel["kernel_integer_rows_in_original_basis_order"], 56, 56)
    rectangle(kernel["new_full_basis_rows"], 56, 56)
    for key in ("kernel_determinant_derived_from_explicit_block_permutation_not_guessed",
                "kernel_times_E_zero_mod_q_verified", "new_basis_is_exact_K_times_old_basis",
                "all168_new_probe_congruences_verified",
                "complete_kernel_basis_certified_by_unit_minor_and_explicit_free_parameterization",
                "complete_new_precision_lattice_basis_certified"):
        assert kernel[key] is True
    assert kernel["old_complete_basis_or_LLL_reexecuted"] is False
    assert kernel["new_normalized_Dixon_digits_computed"] == 0

    lattice = stage(certificate["new_lattice"])
    for key in ("source_compatibility", "old_complete_basis", "unit_minor", "precision_inverse"):
        assert lattice[key] == certificate[key]
    assert lattice["new_current"] == plain(item["new_current_source"]["current"])
    assert lattice["residual_matrix"] == plain(certificate["precision_residual_matrix"])
    assert lattice["kernel_basis_stage"] == plain(certificate["kernel_basis"])
    assert lattice["probe_indices_C_then_A"] == [0, 1, 1214]
    assert lattice["lattice_dimension"] == 56 and lattice["weights"] == ["1", "1", "1", "1"]
    for key in ("all_56_reduced_rows_saved", "all_168_new_probe_congruences_verified",
                "new_basis_change_times_new_canonical_equals_reduced_basis",
                "new_56_rows_are_a_full_integer_lattice_basis",
                "all_nonzero_distinct_denominators_retained",
                "sufficient_uniqueness_bound_not_used",
                "all_candidates_use_new_original_normalized_lift_directly",
                "LLL_is_only_candidate_generation"):
        assert lattice[key] is True
    assert lattice["old_42_or_56_dimensional_LLL_reexecuted"] is False
    assert lattice["old_exact_or_Omega_rejection_reused"] is False
    assert lattice["new_normalized_Dixon_digits_computed"] == 0
    assert lattice["new_basis_change_determinant"] in ("-1", "1")
    rectangle(lattice["new_basis_change_integer_rows"], 56, 56)
    assert sorted(lattice["candidate_order_by_exact_squared_norm"]) == list(range(56))
    assert len(lattice["row_diagnostics"]) == 56
    raw = stage(lattice["reduced_basis_stage"])
    assert raw["input_basis_stage"] == plain(certificate["kernel_basis"])
    assert raw["old_complete_basis"] == plain(old["raw_lattice_stage"])
    assert raw["new_current"] == plain(item["new_current_source"]["current"])
    assert raw["lattice_dimension"] == 56
    assert raw["all_56_reduced_rows_saved"] is True
    assert raw["old_42_or_56_dimensional_LLL_reexecuted"] is False
    rectangle(raw["all_56_reduced_rows"], 56, 56)


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("compute", "verify"))
    args = parser.parse_args()
    request = read(REQUEST)
    item = request["job"]
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if args.mode == "compute":
        return compute(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())

