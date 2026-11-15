#!/usr/bin/env python3
"""Source-bound public IO for the fixed-C next-digit prefix obstruction.

The runner imports only the frozen standard-library source readers.  Every new
ring, residual, quotient and obstruction operation belongs to the separately
pinned public-Actions core.  An output marked complete is a completed finite
necessary-condition calculation, never a recovered function.
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
REQUEST = TOPIC/"notes/R787_fixed_C_prefix_obstruction-public-request.json"
RESULT = "R787-original-fixed-C-prefix-obstructions"
ORIGINAL_RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-fixed-C-prefix-obstructions-certificate.json"
ORIGINAL_FINAL = "p41-original-power5-function-relation-certificate.json"
PREFIX = "R787-fixed-C-"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R787-retained-producer-inputs.tar.gz"
TWO_BUNDLE = "R787-retained-two-probe-search.tar.gz"
THREE_BUNDLE = "R787-fixed-C-retained-three-probe-source.tar.gz"
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
LEGACY_IO_SHA = "7449600243a81bd31b5109fdadd0da2e3aa1930fea00772761154703555d4ed9"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
THREE_CORE_SHA = "c642ec35823dace0ccac4e225e43581398dcce5737dd51cae6a2a903f6028700"
THREE_METHOD_SHA = "58a7713f7265ec4606f30f36a7eea2536f86068e7606f266b249470e48dd1cfe"
ORIGINAL_CORE_SHA = "93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04"
FIELD_CORE_SHA = "d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751"
H64 = re.compile(r"[0-9a-f]{64}")
INTEGER = re.compile(r"-?(0|[1-9][0-9]*)")
LEGACY = None
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
    relative = PurePosixPath(relative)
    assert not relative.is_absolute() and ".." not in relative.parts
    path = (TOPIC/str(relative)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def source_identity(item):
    return {key: item[key] for key in BASE}


def import_io(item):
    global LEGACY, IO
    path = S/"R787_projective_three_probe_public.py"
    assert sha(path) == LEGACY_IO_SHA == item["source_io_helper_sha256"]
    source = importlib.util.spec_from_file_location("fixed_C_frozen_source_IO", path)
    LEGACY = importlib.util.module_from_spec(source)
    source.loader.exec_module(LEGACY)
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    LEGACY.load_io(item)
    IO = LEGACY.IO


def extract_flat_bundle(bundle, directory, rows, extract):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    expected = {row["file"]: plain(row) for row in rows}
    assert len(expected) == len(rows)
    seen = set()
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            safe_name(member.name)
            assert member.isfile() and member.name in expected and member.name not in seen
            seen.add(member.name)
            row = expected[member.name]
            assert member.size == row["bytes"]
            target = directory/member.name
            temporary = target.with_name(target.name+".download")
            destination = temporary.open("wb") if extract else None
            digest, count = hashlib.sha256(), 0
            try:
                with archive.extractfile(member) as stream:
                    for block in iter(lambda: stream.read(4*1024*1024), b""):
                        digest.update(block)
                        count += len(block)
                        if destination is not None:
                            destination.write(block)
            finally:
                if destination is not None:
                    destination.close()
            assert count == row["bytes"] and digest.hexdigest() == row["sha256"]
            if extract:
                if target.exists():
                    assert file_spec(target) == row
                    temporary.unlink()
                else:
                    temporary.replace(target)
    assert seen == set(expected)
    return len(seen)


def create_flat_bundle(directory, bundle, rows):
    bundle = Path(bundle)
    if not bundle.exists():
        temporary = bundle.with_name(bundle.name+".tmp")
        with tarfile.open(temporary, "w:gz", compresslevel=1) as archive:
            for row in rows:
                path = bound(directory, row)
                info = tarfile.TarInfo(row["file"])
                info.size, info.mode, info.mtime = row["bytes"], 0o644, 0
                info.uid = info.gid = 0
                info.uname = info.gname = ""
                with path.open("rb") as stream:
                    archive.addfile(info, stream)
        temporary.replace(bundle)
    return extract_flat_bundle(bundle, directory, rows, extract=False)


def original_dependency_keys():
    return ("retained_source", "retained_artifacts", "checkpoint",
            "pinned_R787_configuration_sha256", "R787_method_sha256",
            "R786_proof_sha256", "field_core_sha256")


def three_probe_schema(item, directory, two_directory=None):
    source = item["completed_three_probe_source"]
    assert source["result"] == ORIGINAL_RESULT
    assert source["core_sha256"] == THREE_CORE_SHA
    manifest_path = directory/"full-outputs-manifest.json"
    assert sha(manifest_path) == source["manifest_sha256"]
    assert manifest_path.stat().st_size == source["manifest_bytes"]
    manifest, reference = read(manifest_path), read(directory/REFERENCE)
    assert manifest["result"] == reference["result"] == ORIGINAL_RESULT
    assert manifest["projective_mode"] is reference["projective_mode"] is True
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    for key in ("certificate", "stage_manifest", "search_state", "lattice_stage",
                "raw_lattice_stage", "input_stage", "source_basis_stage",
                "input_bundle", "previous_search_bundle"):
        row = plain(source[key])
        assert row == entries[row["file"]]
    assert reference["file_count"] == len(entries)
    assert reference["manifest_sha256"] == source["manifest_sha256"]
    assert reference["manifest_bytes"] == source["manifest_bytes"]
    expected = (set(entries)-{BUNDLE, TWO_BUNDLE}) | {"full-outputs-manifest.json", REFERENCE}
    assert {path.name for path in directory.iterdir() if path.is_file()} == expected
    for name in sorted(expected-{"full-outputs-manifest.json", REFERENCE}):
        bound(directory, entries[name])
    initial = read(directory/"public-actions-input.json")
    run = read(directory/"run-receipt.json")
    core = read(directory/"core-receipt.json")
    final = read(directory/ORIGINAL_FINAL)
    assert initial["result"] == run["result"] == core["result"] == final["result"] == ORIGINAL_RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == initial["job"]["core_sha256"] == core["source_sha256"] == THREE_CORE_SHA
    assert initial["driver_sha256"] == initial["job"]["wrapper_sha256"] == LEGACY_IO_SHA
    assert initial["method_sha256"] == initial["job"]["projective_method_sha256"] == THREE_METHOD_SHA
    assert initial["field_core_sha256"] == item["field_core_sha256"] == FIELD_CORE_SHA
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"] == entries[ORIGINAL_FINAL]["sha256"]
    assert run["process_exit_code"] == 2 and run["error"] is None
    assert run["complete"] is core["complete"] is final["complete"] is False
    old_job = initial["job"]
    for key in original_dependency_keys():
        assert old_job[key] == item[key]
    assert old_job["previous_two_probe_source"] == item["previous_two_probe_source"]
    tag = final["configuration"]
    LEGACY.check_new_tag(tag, old_job)
    assert final["completed_search_nodes"] == 56
    assert final["new_exact_candidate_evaluations"] == 56
    assert final["previous_exact_candidate_rejections_referenced"] == 0
    assert final["original_42_rows_retained_as_unchanged_source"] is True
    assert final["previous_42_dimensional_LLL_recomputed"] is False
    stage_ref = plain(final["stage_manifest"])
    assert stage_ref == entries[stage_ref["file"]]
    indexed = read(bound(directory, stage_ref))
    assert indexed["complete"] is True and indexed["configuration"] == tag
    stage_entries = {row["file"]: plain(row) for row in indexed["files"]}
    assert len(stage_entries) == len(indexed["files"])
    for row in stage_entries.values():
        assert row == entries[row["file"]]
    outcomes, complete_names, current_names = {}, set(), set()
    for name in sorted(expected):
        if not (name.startswith("R787-projective-") and name.endswith(".json.gz")):
            continue
        data = read(directory/name)
        assert data["result"] == ORIGINAL_RESULT and data["configuration"] == tag
        assert type(data["complete"]) is bool
        if data["complete"] and name != stage_ref["file"]:
            complete_names.add(name)
        elif not data["complete"]:
            current_names.add(name)
        if name.endswith("-result.json.gz") and name.startswith("R787-projective-candidate-"):
            assert data["complete"] is True and data["exact_relation_found"] is False
            assert data["relation_spec"] is None
            assert data["new_exact_candidate_evaluation_performed"] is True
            assert data["previous_exact_rejection_reused"] is False
            node = data["node_id"]
            assert fingerprint({"denominator": data["denominator"]}) == node and node not in outcomes
            assert len(data["denominator"]) == 14
            assert all(isinstance(x, str) and INTEGER.fullmatch(x) for x in data["denominator"])
            reject_ref = plain(data["exact_rejection"])
            assert reject_ref == entries[reject_ref["file"]]
            rejected = read(bound(directory, reject_ref))
            assert rejected["complete"] is True and rejected["configuration"] == tag
            assert rejected["node_id"] == node and rejected["not_a_characteristic_zero_relation"] is True
            assert rejected["first_nonzero_relation_order"] == data["first_nonzero_relation_order"]
            outcomes[node] = {"file": entries[name], "D": data["denominator"]}
        elif name.endswith("-closed-work-receipt.json.gz"):
            assert data["complete"] is True
            assert data["current_or_successful_candidate_payload_never_retired"] is True
            assert data["retired_payloads_never_recomputed_for_this_completed_candidate"] is True
            for key in ("completed_rejection", "completed_outcome"):
                row = plain(data[key])
                assert row == entries[row["file"]]
                linked = read(bound(directory, row))
                assert linked["node_id"] == data["node_id"]
                assert linked["complete"] is True and linked["configuration"] == tag
            for row in data["retired_work_files"]:
                plain(row)
                assert row["file"] not in entries
    assert set(stage_entries) == complete_names
    assert len(outcomes) == 56
    queue_ref = plain(final["resume_state"])
    assert queue_ref == entries[queue_ref["file"]] and queue_ref["file"] in current_names
    queue = read(bound(directory, queue_ref))
    assert len(queue["processed_node_ids"]) == len(set(queue["processed_node_ids"])) == 56
    assert set(queue["processed_node_ids"]) == set(outcomes)
    old_receipt = read(directory/"retained-inputs-receipt.json")
    assert old_receipt["file_count"] == 1380 and old_receipt["complete"] is True
    assert plain(old_receipt["bundle"]) == entries[BUNDLE]
    assert old_receipt["original_R787_source"] == item["retained_source"]
    assert old_receipt["original_child_sources"] == item["retained_artifacts"]
    previous_receipt = read(directory/"previous-two-probe-inputs-receipt.json")
    assert previous_receipt["result"] == ORIGINAL_RESULT and previous_receipt["complete"] is True
    assert previous_receipt["source"] == item["previous_two_probe_source"]
    assert plain(previous_receipt["bundle"]) == entries[TWO_BUNDLE]
    assert previous_receipt["previous_arithmetic_recomputed"] is False
    if two_directory is not None:
        review = LEGACY.previous_search_schema(old_job, two_directory)
        assert review == previous_receipt["schema"]
        counts = LEGACY.review_candidate_sources(old_job, directory, entries, two_directory)
        assert counts == {"new_exact_candidate_evaluations": 56,
                          "previous_exact_candidate_rejections_referenced": 0}
    return {"source": source_identity(source), "original_configuration_sha256": fingerprint(tag),
            "old_job": old_job, "input_bundle": entries[BUNDLE], "two_probe_bundle": entries[TWO_BUNDLE],
            "source_certificate": entries[ORIGINAL_FINAL], "source_stage_manifest": stage_ref,
            "source_resume_state": queue_ref,
            "original_input_inventory": old_receipt["selected_source_files"],
            "two_probe_inventory": previous_receipt["files"],
            "actual56_complete_outcomes": [outcomes[node] for node in sorted(outcomes)],
            "unchanged_source_files": [file_spec(directory/name) for name in sorted(expected)],
            "full_original_manifest_bound_and_all_noncarrier_source_files_SHA_verified": True,
            "original_arithmetic_recomputed_during_IO": False}


def review_sources(item, out, retained, candidates):
    three = candidates/"three_probe"
    two = candidates/"two_probe"
    schema = three_probe_schema(item, three)
    bound(out, schema["input_bundle"])
    bound(out, schema["two_probe_bundle"])
    count = LEGACY.verify_or_extract_bundle(out/BUNDLE, retained, schema["original_input_inventory"])
    assert count == 1380
    original = LEGACY.original_source(schema["old_job"], retained)
    old_schema = LEGACY.check_selected_sources(schema["old_job"], retained, original)
    assert old_schema["selected_source_file_counts"] == {"R787": 1242, "R781": 134, "R786": 4}
    assert LEGACY.inventory(retained) == schema["original_input_inventory"]
    old_count = extract_flat_bundle(out/TWO_BUNDLE, two, schema["two_probe_inventory"], extract=True)
    assert old_count == len(schema["two_probe_inventory"])
    schema = three_probe_schema(item, three, two)
    old_review = LEGACY.previous_search_schema(schema["old_job"], two)
    old_nodes = {}
    for row in old_review["old_complete_candidate_outcomes"]:
        value = read(bound(two, row))
        old_nodes[value["node_id"]] = value["denominator"]
    new_nodes = {fingerprint({"denominator": row["D"]}): row["D"]
                 for row in schema["actual56_complete_outcomes"]}
    assert len(old_nodes) == 42 and len(new_nodes) == 56
    assert not set(old_nodes) & set(new_nodes)
    return {"source": schema["source"],
            "source_configuration_sha256": schema["original_configuration_sha256"],
            "source_certificate": schema["source_certificate"],
            "source_stage_manifest": schema["source_stage_manifest"],
            "source_resume_state": schema["source_resume_state"],
            "original1380_input_inventory": schema["original_input_inventory"],
            "source_three_probe_files": schema["unchanged_source_files"],
            "source_two_probe_files": schema["two_probe_inventory"],
            "actual_distinct_candidate_counts": {"two_probe": 42, "three_probe": 56, "total": 98},
            "actual_candidate_ids_by_source": {"two_probe": sorted(old_nodes), "three_probe": sorted(new_nodes)},
            "original_1380_source_schema": old_schema,
            "all_original_source_bytes_configurations_and_complete_outcomes_preserved": True,
            "source_arithmetic_recomputed": False}


def prepare_inputs(item, out, allow_download=True):
    retained = out.parent/"retained"
    candidates = out.parent/"candidates"
    three = candidates/"three_probe"
    three.mkdir(parents=True, exist_ok=True)
    receipt_path = out/"retained-inputs-receipt.json"
    if all((out/name).is_file() for name in (BUNDLE, TWO_BUNDLE, THREE_BUNDLE)) and receipt_path.exists():
        receipt = read(receipt_path)
        assert receipt["result"] == RESULT and receipt["complete"] is True
        assert receipt["source"] == item["completed_three_probe_source"]
        assert receipt["previous_two_probe_source"] == item["previous_two_probe_source"]
        for name in (BUNDLE, TWO_BUNDLE, THREE_BUNDLE):
            bound(out, receipt["carriers"][name])
        extract_flat_bundle(out/THREE_BUNDLE, three, receipt["three_probe_inventory"], extract=True)
        review = review_sources(item, out, retained, candidates)
        assert review == receipt["review"]
        return retained, candidates
    assert allow_download, "All source-bound carriers must be present for read-only verification."
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
        small_names = sorted(set(entries)-{BUNDLE, TWO_BUNDLE})
        assert all(entries[name]["bytes"] <= 32*1024*1024 for name in small_names)
        assert sum(entries[name]["bytes"] for name in small_names) <= 192*1024*1024
        archive.extract_many([(name, entries[name]["sha256"], three/name, entries[name]["bytes"])
                              for name in small_names])
        schema = three_probe_schema(item, three)
        for name in (BUNDLE, TWO_BUNDLE):
            row = entries[name]
            archive.extract_bound(name, row["sha256"], out/name, row["bytes"])
        review = review_sources(item, out, retained, candidates)
        three_rows = review["source_three_probe_files"]
        create_flat_bundle(three, out/THREE_BUNDLE, three_rows)
        receipt = {
            "result": RESULT, "complete": True,
            "source": source, "previous_two_probe_source": item["previous_two_probe_source"],
            "review": review, "three_probe_inventory": three_rows,
            "carriers": {name: file_spec(out/name) for name in (BUNDLE, TWO_BUNDLE, THREE_BUNDLE)},
            "source_transfer": archive.receipt(),
            "all_three_carriers_and_original_members_size_SHA256_verified": True,
            "whole_source_ZIP_rehashed_in_this_Range_transfer": False,
            "original_Dixon_LLL_real_rows_Laurent_or_candidate_checks_recomputed": False,
            "carriers_exist_only_for_active_one_day_continuation": True,
        }
        save(receipt_path, receipt)
        print("FIXED_C_INPUT_REVIEW="+json.dumps({
            "source": source_identity(source),
            "candidate_counts": review["actual_distinct_candidate_counts"],
            "original_input_file_count": 1380,
            "two_probe_source_file_count": len(review["source_two_probe_files"]),
            "three_probe_source_file_count": len(three_rows),
            "all_selected_bytes_SHA_verified": True, "old_arithmetic_recomputed": False,
            "source_transfer": archive.receipt(),
        }, sort_keys=True), flush=True)
        return retained, candidates
    finally:
        archive.close()

def mathematical_job(item):
    keys = ("result", "p", "core_sha256", "proof_sha256", "method_sha256",
            "field_core_sha256", "original_core_sha256",
            "pinned_R787_configuration_sha256", "retained_source", "retained_artifacts",
            "checkpoint", "previous_two_probe_source", "completed_three_probe_source",
            "source_mode", "source_Dixon_digits", "working_Dixon_digits",
            "original_branch", "A_prefix_blocks", "B_prefix_blocks",
            "prefix_equation_count", "complement_equation_count",
            "expected_candidate_count", "source_evaluation_block_size")
    return {key: item[key] for key in keys}


def guard_sources(item):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["original_core_sha256"] == ORIGINAL_CORE_SHA
    assert item["field_core_sha256"] == FIELD_CORE_SHA
    for key in ("core", "original_core", "field_core", "io_helper", "source_io_helper"):
        safe_name(item[key])
        assert sha(S/item[key]) == item[key+"_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert sha(topic_path(item["proof"])) == item["proof_sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    assert sha(REPO/"README.md") == item["current_readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["current_readme_sha256"]["topic"]
    assert item["source_mode"] == "from_original_430_cleared_residual"
    assert item["source_Dixon_digits"] == 430 and item["working_Dixon_digits"] == 431
    assert item["original_branch"] == 0
    assert item["A_prefix_blocks"] == 69 and item["B_prefix_blocks"] == 70
    assert item["prefix_equation_count"] == 1380 and item["complement_equation_count"] == 146
    assert item["expected_candidate_count"] == 98 and item["source_evaluation_block_size"] == 5
    assert item["checkpoint"]["digits"] == 430 and item["checkpoint"]["prime"] == 1000000753
    import_io(item)


def restore_resume(item, out):
    source = item.get("resume")
    if source is None:
        return
    assert source["result"] == RESULT and source["core_sha256"] == item["core_sha256"]
    root = out.parent/"resume-source-metadata"
    root.mkdir(parents=True, exist_ok=True)
    archive = IO.Archive(source, out.parent/"download-fixed-C-continuation", whole=False)
    try:
        path = archive.extract_bound("full-outputs-manifest.json", source["manifest_sha256"],
                                      root/"full-outputs-manifest.json", source.get("manifest_bytes"))
        manifest = read(path)
        assert manifest["result"] == RESULT
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        def metadata(name):
            row = entries[name]
            return read(archive.extract_bound(name, row["sha256"], root/name, row["bytes"]))
        initial = metadata("public-actions-input.json")
        run = metadata("run-receipt.json")
        assert initial["result"] == run["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert initial["core_sha256"] == source["core_sha256"]
        assert mathematical_job(initial["job"]) == mathematical_job(item)
        if "core-receipt.json" in entries:
            core = metadata("core-receipt.json")
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        else:
            assert run["core_receipt_sha256"] is None
        receipt = metadata("retained-inputs-receipt.json")
        assert receipt["result"] == RESULT and receipt["complete"] is True
        assert receipt["source"] == item["completed_three_probe_source"]
        assert receipt["previous_two_probe_source"] == item["previous_two_probe_source"]
        required = {BUNDLE, TWO_BUNDLE, THREE_BUNDLE, "retained-inputs-receipt.json"}
        for name in (BUNDLE, TWO_BUNDLE, THREE_BUNDLE):
            assert plain(receipt["carriers"][name]) == entries[name]
        stages = sorted(name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz"))
        required.update(stages)
        if FINAL in entries:
            final = metadata(FINAL)
            check_tag(final["configuration"], item)
            if final["complete"] is True:
                required.add(FINAL)
        archive.extract_many([(name, entries[name]["sha256"], out/name, entries[name]["bytes"])
                              for name in sorted(required)])
        completed, current = [], []
        for name in stages:
            data = read(out/name)
            assert data["result"] == RESULT
            check_tag(data["configuration"], item)
            assert type(data["complete"]) is bool
            (completed if data["complete"] else current).append(entries[name])
        save(out/"resume-receipt.json", {
            "result": RESULT, "source": source, "source_manifest": file_spec(path),
            "same_mathematical_job_preserved": True,
            "completed_stage_files_restored": completed,
            "atomic_current_files_restored": current,
            "source_carriers_and_receipt_restored": [entries[name] for name in
                (BUNDLE, TWO_BUNDLE, THREE_BUNDLE, "retained-inputs-receipt.json")],
            "retained_complete_certificate": FINAL in required,
            "all_restored_member_bytes_SHA256_verified": True,
            "source_transfer": archive.receipt(),
            "old_completed_mathematical_arithmetic_recomputed": False,
        })
        print("FIXED_C_RESUME_REVIEW="+json.dumps({
            "run_id": source["run_id"], "complete_stages": len(completed),
            "current_stages": len(current), "same_source_and_mathematical_identity": True,
            "all_restored_bytes_SHA_verified": True,
        }, sort_keys=True), flush=True)
    finally:
        archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and (path.name.endswith(".tmp") or path.name.endswith(".download")):
            path.unlink()
    rows = [file_spec(path) for path in sorted(out.iterdir()) if path.is_file()
            and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    save(out/"full-outputs-manifest.json", {
        "result": RESULT, "files": rows,
        "scope": "finite necessary fixed-C prefix obstruction decisions",
        "raw_outputs_and_carriers_published_to_git_or_release": False,
        "reproducible_raw_location": "one-day active public Actions artifact",
    })
    spec = file_spec(out/"full-outputs-manifest.json")
    save(out/REFERENCE, {
        "result": RESULT, "manifest_file": spec["file"],
        "manifest_bytes": spec["bytes"], "manifest_sha256": spec["sha256"],
        "file_count": len(rows),
    })


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": commit, "job": item,
        "core_sha256": sha(S/item["core"]), "driver_sha256": sha(__file__),
        "field_core_sha256": sha(S/item["field_core"]),
        "original_core_sha256": sha(S/item["original_core"]),
        "proof_sha256": sha(topic_path(item["proof"])),
        "method_sha256": sha(topic_path(item["method"])),
        "source_io_helper_sha256": sha(S/item["source_io_helper"]),
        "range_io_helper_sha256": sha(S/item["io_helper"]),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]), "request_sha256": sha(REQUEST),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "function_relation_recovered": False,
    })
    code, error = 1, None
    try:
        guard_sources(item)
        restore_resume(item, out)
        retained, candidates = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(S/item["core"]),
                   "--config", str(config), "--proof", str(topic_path(item["proof"])),
                   "--method", str(topic_path(item["method"])),
                   "--field-core", str(S/item["field_core"]),
                   "--original-core", str(S/item["original_core"]),
                   "--retained", str(retained), "--candidates", str(candidates),
                   "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                error = "Outer budget reached; completed prefix decisions, current and source carriers are preserved."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    path = out/"core-receipt.json"
    core = read(path) if path.exists() else {}
    complete = code == 0 and core.get("complete") is True
    if complete:
        assert (out/FINAL).is_file() and read(out/FINAL)["complete"] is True
    save(out/"run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code, "error": error,
        "core_receipt_sha256": sha(path) if path.exists() else None,
        "source_commit": commit, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "complete_means_only_all_requested_finite_obstruction_decisions": True,
        "original_function_or_exact_C_recovered": False, "beta_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    output_manifest(out)
    print("FIXED_C_RUN_RECEIPT="+json.dumps(read(out/"run-receipt.json"), sort_keys=True), flush=True)
    return code if code else (0 if complete else 1)

def check_tag(tag, item):
    assert tag["result"] == RESULT and tag["p"] == 41
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    for key in ("proof_sha256", "method_sha256", "field_core_sha256",
                "original_core_sha256", "pinned_R787_configuration_sha256",
                "retained_source", "retained_artifacts", "checkpoint",
                "completed_three_probe_source", "previous_two_probe_source",
                "source_mode", "source_Dixon_digits", "working_Dixon_digits",
                "original_branch", "A_prefix_blocks", "B_prefix_blocks",
                "prefix_equation_count", "complement_equation_count",
                "expected_candidate_count", "source_evaluation_block_size"):
        assert tag[key] == item[key]
    for key in ("positive_uncleared_residual", "division_by_M_before_L_branch_evaluation",
                "original_precontent_D_and_qC", "no_Schur_branch_inverse_used",
                "no_normalized_Dixon_lift_computed"):
        assert tag[key] is True


def verify(out):
    """Check actual source/output bytes and schemas, never import a math module."""
    manifest_path = out/"full-outputs-manifest.json"
    manifest, reference = read(manifest_path), read(out/REFERENCE)
    assert manifest["result"] == reference["result"] == RESULT
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    assert {path.name for path in out.iterdir() if path.is_file()} == \
           set(entries) | {"full-outputs-manifest.json", REFERENCE}
    for row in entries.values():
        bound(out, row)
    assert reference["manifest_sha256"] == sha(manifest_path)
    assert reference["manifest_bytes"] == manifest_path.stat().st_size
    assert reference["file_count"] == len(entries)
    initial = read(out/"public-actions-input.json")
    run = read(out/"run-receipt.json")
    item = initial["job"]
    guard_sources(item)
    assert initial["result"] == run["result"] == RESULT
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["field_core_sha256"] == item["field_core_sha256"]
    assert initial["original_core_sha256"] == item["original_core_sha256"]
    assert initial["proof_sha256"] == item["proof_sha256"]
    assert initial["method_sha256"] == item["method_sha256"]
    assert initial["source_io_helper_sha256"] == item["source_io_helper_sha256"]
    assert initial["range_io_helper_sha256"] == item["io_helper_sha256"]
    assert run["complete_means_only_all_requested_finite_obstruction_decisions"] is True
    assert run["original_function_or_exact_C_recovered"] is False
    assert run["beta_eta_or_height_computed"] is False
    retained, candidates = prepare_inputs(item, out, allow_download=False)
    source_receipt = read(out/"retained-inputs-receipt.json")
    assert source_receipt["all_three_carriers_and_original_members_size_SHA256_verified"] is True
    assert source_receipt["original_Dixon_LLL_real_rows_Laurent_or_candidate_checks_recomputed"] is False
    for name in (BUNDLE, TWO_BUNDLE, THREE_BUNDLE):
        assert plain(source_receipt["carriers"][name]) == entries[name]
    old_schema = source_receipt["review"]["original_1380_source_schema"]
    source_counts = source_receipt["review"]["actual_distinct_candidate_counts"]
    assert source_counts == {"two_probe": 42, "three_probe": 56, "total": 98}
    complete_stage_names, current_stage_names = set(), set()
    for name in sorted(entries):
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        data = read(out/name)
        assert data["result"] == RESULT and type(data["complete"]) is bool
        check_tag(data["configuration"], item)
        assert data["configuration"]["field"] == old_schema["original_field"]
        (complete_stage_names if data["complete"] else current_stage_names).add(name)
    core_path = out/"core-receipt.json"
    core = read(core_path) if core_path.exists() else None
    if core is not None:
        assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
    else:
        assert run["core_receipt_sha256"] is None
    final = read(out/FINAL) if FINAL in entries else None
    decisions = []
    if final is not None:
        assert final["result"] == RESULT and type(final["complete"]) is bool
        check_tag(final["configuration"], item)
        assert final["configuration"]["field"] == old_schema["original_field"]
        for key in ("p", "source_Dixon_digits", "working_Dixon_digits", "original_branch",
                    "A_prefix_blocks", "B_prefix_blocks", "prefix_equation_count",
                    "complement_equation_count"):
            assert final[key] == item[key]
        for key in ("actual_exact_C_recovered", "actual_y_map_recovered",
                    "complete_129_function_relation_verified", "beta_or_height_computed"):
            assert final[key] is False
        assert final["new_normalized_Dixon_digits_computed"] == 0
        if core is not None:
            assert core["certificate_sha256"] == entries[FINAL]["sha256"]
        tag = final["configuration"]
        def stage(row, complete=True):
            row = plain(row)
            assert row == entries[row["file"]]
            value = read(bound(out, row))
            assert value["result"] == RESULT and value["configuration"] == tag
            assert value["complete"] is complete
            return value
        indexed = stage(final["stage_manifest"])
        stage_rows = {row["file"]: plain(row) for row in indexed["files"]}
        assert len(stage_rows) == len(indexed["files"])
        assert set(stage_rows) == complete_stage_names-{final["stage_manifest"]["file"]}
        for name, row in stage_rows.items():
            assert row == entries[name]
        current = stage(final["resume_state"], complete=False)
        assert final["resume_state"]["file"] in current_stage_names
        stage(final["source_audit"])
        stage(final["shared_prefix_obstruction"])
        decisions = final["candidate_decisions"]
        assert final["actual_candidate_count"] == len(decisions)
        assert final["actual_source_candidate_count"] == 98
        assert current["next_candidate_position"] == len(decisions)
        assert current["processed_candidate_ids"] == [row["candidate_id"] for row in decisions]
        seen, strict, zero = set(), 0, 0
        source_group_counts = {}
        for row in decisions:
            candidate_id = row["candidate_id"]
            assert candidate_id not in seen
            seen.add(candidate_id)
            assert isinstance(candidate_id, str) and H64.fullmatch(candidate_id)
            assert row["source_group"] in ("two_probe", "three_probe")
            assert candidate_id in source_receipt["review"]["actual_candidate_ids_by_source"][row["source_group"]]
            limit = 42 if row["source_group"] == "two_probe" else 56
            assert type(row["source_LLL_row"]) is int and 0 <= row["source_LLL_row"] < limit
            value = stage(row["stage"])
            for key in ("candidate_id", "source_group", "source_LLL_row",
                        "strict_fixed_C_rejected", "prefix_only_zero"):
                assert value[key] == row[key]
            assert type(row["strict_fixed_C_rejected"]) is bool
            assert type(row["prefix_only_zero"]) is bool
            assert row["strict_fixed_C_rejected"] != row["prefix_only_zero"]
            original_rows = value["original_equation_rows"]
            omega = value["Omega_mod_prime"]
            assert len(original_rows) == len(set(original_rows)) == 146
            assert all(type(x) is int and 0 <= x < 1380 for x in original_rows)
            assert len(omega) == 146
            assert all(type(x) is int and 0 <= x < 1000000753 for x in omega)
            nonzero = [i for i, x in enumerate(omega) if x != 0]
            assert bool(nonzero) is row["strict_fixed_C_rejected"]
            first = value["first_nonzero_complement_position"]
            assert first == (nonzero[0] if nonzero else None)
            assert value["first_nonzero_original_equation_row"] == \
                   (original_rows[first] if first is not None else None)
            assert value["nonzero_is_a_projected_equation_not_raw_Laurent_first_failure"] is True
            assert value["D_branch0_is_field_evaluation_not_constant_coordinate"] is True
            assert value["necessary_condition_only_if_all_146_entries_zero"] is True
            assert value["old_candidate_A_centering_or_rejection_not_used_as_new_proof"] is True
            assert plain(value["shared_prefix_obstruction"]) == plain(final["shared_prefix_obstruction"])
            stage(value["quotient"])
            stage(value["prefix_image"])
            for key in ("actual_exact_C_recovered", "actual_y_map_recovered",
                        "complete_129_function_relation_verified", "beta_or_height_computed"):
                assert value[key] is False
            assert value["new_normalized_Dixon_digits_computed"] == 0
            strict += int(row["strict_fixed_C_rejected"])
            zero += int(row["prefix_only_zero"])
            source_group_counts[row["source_group"]] = source_group_counts.get(row["source_group"], 0)+1
        assert strict == final["strict_fixed_C_rejected_count"]
        assert zero == final["prefix_only_zero_count"]
        assert strict+zero == len(decisions)
        if final["complete"]:
            assert final["actual_candidate_count"] == len(decisions) == 98
            assert source_group_counts == {"two_probe": 42, "three_probe": 56}
    if run["complete"] is not True or core is None or core["complete"] is not True:
        print("FIXED_C_PRESERVED_IO_REVIEW="+json.dumps({
            "result": RESULT, "complete_finite_obstruction_scope": False,
            "process_exit_code": run["process_exit_code"], "error": run["error"],
            "all_output_manifest_bytes_SHA_verified": True,
            "all_original_1380_input_and_both_completed_search_sources_SHA_verified": True,
            "complete_stage_count": len(complete_stage_names),
            "atomic_current_stage_count": len(current_stage_names),
            "completed_candidate_decisions": len(decisions),
            "mathematical_arithmetic_recomputed_by_verifier": False,
            "function_or_exact_C_recovered": False,
        }, sort_keys=True), flush=True)
        return 1
    assert run["process_exit_code"] == 0 and run["error"] is None
    assert final is not None and final["complete"] is True
    assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    print("FIXED_C_COMPLETE_IO_REVIEW="+json.dumps({
        "result": RESULT, "new_core_sha256": item["core_sha256"],
        "complete_finite_obstruction_scope": True,
        "original_checkpoint_digits": 430, "new_normalized_Dixon_digits_computed": 0,
        "original_branch": 0, "prefix_equation_count": 1380, "complement_equation_count": 146,
        "actual_candidate_count": final["actual_candidate_count"],
        "strict_fixed_C_rejected_count": final["strict_fixed_C_rejected_count"],
        "prefix_only_zero_count": final["prefix_only_zero_count"],
        "output_manifest": file_spec(manifest_path), "manifest_file_count": len(entries),
        "source_counts": source_counts, "active_original_input_file_count": 1380,
        "certificate": entries[FINAL], "stage_manifest": plain(final["stage_manifest"]),
        "shared_prefix_obstruction": plain(final["shared_prefix_obstruction"]),
        "core_seconds": final["seconds"],
        "all_output_and_selected_source_bytes_SHA_verified": True,
        "mathematical_core_reimported_or_reexecuted_during_IO_review": False,
        "actual_exact_C_recovered": False, "actual_y_map_recovered": False,
        "beta_or_height_computed": False,
    }, sort_keys=True), flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("compute", "verify"))
    args = parser.parse_args()
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/"R787-fixed-C-prefix-obstructions"/"output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    return verify(out)


if __name__ == "__main__":
    sys.exit(main())
