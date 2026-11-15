#!/usr/bin/env python3
"""Public IO runner for a projective reconstruction from the original R787 430-digit lift.

All new arithmetic is delegated to the separately pinned Actions core.  This
runner imports only standard-library IO code, verifies original bytes and
schemas, and preserves complete stages and the minimal active input carrier.
"""
import argparse
import ast
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
import time

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R787_projective-public-request.json"
RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-power5-function-relation-certificate.json"
BUNDLE = "R787-retained-producer-inputs.tar.gz"
PREFIX = "R787-projective-"
REFERENCE = "full-outputs-manifest-reference.json"
OLD_BUNDLE = "R787-retained-producer-inputs.tar.gz"
R786_INDEX = "R786-exact-power5-basis-index.json.gz"
META = ("full-outputs-manifest.json", "run-receipt.json",
        "core-receipt.json", "public-actions-input.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
H64 = re.compile(r"[0-9a-f]{64}")
INTEGER = re.compile(r"-?(0|[1-9][0-9]*)")
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
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as raw:
            with gzip.GzipFile(fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(payload)
    else:
        temporary.write_bytes(payload)
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def plain(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name
    assert name not in ("", ".", "..") and "\\" not in name


def check_spec(row):
    safe_name(row["file"])
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert H64.fullmatch(row["sha256"])


def bound_file(directory, row):
    check_spec(row)
    path = Path(directory)/row["file"]
    assert path.is_file() and file_spec(path) == plain(row)
    return path


def topic_path(relative):
    relative = PurePosixPath(relative)
    assert not relative.is_absolute() and ".." not in relative.parts
    path = (TOPIC/str(relative)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def same_identity(left, right):
    for key in BASE:
        assert str(left[key]) == str(right[key]), ("Changed producer", key)
    if left.get("certificate_name") is not None:
        name = left["certificate_name"]
        assert right["certificate_name"] == name
        assert left["files"][name] == right["files"][name]


def load_io(item):
    global IO
    source = S/item["io_helper"]
    assert sha(source) == item["io_helper_sha256"]
    ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    spec = importlib.util.spec_from_file_location("R787_projective_frozen_IO", source)
    IO = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(IO)


def original_source(item, root, archive=None):
    spec = item["retained_source"]
    original = IO.Producer("R787", spec, Path(root)/"R787", archive)
    assert original.certificate is None
    assert (original.directory/"full-outputs-manifest.json").stat().st_size == spec["manifest_bytes"]
    assert len(original.files) == spec["manifest_file_count"]
    assert fingerprint(original.tag) == item["pinned_R787_configuration_sha256"]
    initial = original.initial
    assert initial["driver_sha256"] == item["original_wrapper_sha256"]
    assert initial["root_readme_sha256"] == item["original_readme_sha256"]["root"]
    assert initial["topic_readme_sha256"] == item["original_readme_sha256"]["topic"]
    assert initial["field_core_sha256"] == item["field_core_sha256"]
    assert initial["method_sha256"] == item["R787_method_sha256"]
    assert initial["proof_sha256"] == item["R786_proof_sha256"]
    assert original.tag["R787_method_sha256"] == item["R787_method_sha256"]
    assert original.tag["R786_proof_sha256"] == item["R786_proof_sha256"]
    assert original.tag["R781_field_core_sha256"] == item["field_core_sha256"]
    assert original.tag["basis_integer_scale"] == "13744803133596058624"
    assert original.tag["ordinary_power"] == 5 and original.tag["basis_dimension"] == 1234
    assert original.tag["qY_bound"] == 128 and original.tag["Laurent_exponents"] == [-1, 127]
    assert original.tag["t_coordinates"] == 20
    assert set(initial["job"]["retained_artifacts"]) == {"R781", "R786"}
    assert original.tag["retained_artifacts"] == initial["job"]["retained_artifacts"]
    assert initial["job"]["retained_artifacts"] == item["retained_artifacts"]
    run, core = (original.raw(name) for name in ("run-receipt.json", "core-receipt.json"))
    assert run["process_exit_code"] == 1 and run["complete"] is False
    assert core["complete"] is False and core["error"].startswith("BudgetStop:")
    assert core["all_completed_stages_preserved"] is True
    return original


def child_metadata(root, label, item, original):
    spec = item["retained_artifacts"][label]
    same_identity(spec, original.tag["retained_artifacts"][label])
    directory = Path(root)/label
    manifest_path = directory/"full-outputs-manifest.json"
    assert sha(manifest_path) == spec["manifest_sha256"]
    manifest = read(manifest_path)
    assert manifest["result"] == spec["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for row in entries.values():
        check_spec(row)
    run = read(bound_file(directory, entries["run-receipt.json"]))
    assert run["result"] == spec["result"] and run["complete"] is True and run["process_exit_code"] == 0
    assert str(run["workflow_run_id"]) == str(spec["run_id"])
    assert run["source_commit"] == spec["source_commit"]
    cert_name = spec["certificate_name"]
    assert entries[cert_name]["sha256"] == spec["files"][cert_name]
    cert = read(bound_file(directory, entries[cert_name]))
    assert cert["result"] == spec["result"] and cert["complete"] is True
    tag = cert["configuration"]
    assert tag["source_sha256"] == spec["core_sha256"] and tag["python_flint"] == "0.9.0"
    if label == "R781":
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["actual_cusp_order"] == 1 and cert["normalized_Laurent_R_bound"] == 142
        assert cert["all_original_real_tangent_phases_verified"] is True
        assert cert["all_recurrence_coefficients_verified_exactly"] is True
    else:
        assert label == "R786"
        assert cert["exact_power5_basis_dimension"] == 1234
        assert cert["exact_K_basis_prefix_bound_qY"] == 128
        assert cert["basis_integer_scale"] == "13744803133596058624"
        assert cert["all_original_R775_mod739_short_series_compared"] is True
        assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
        assert cert["basis_index"]["file"] == R786_INDEX
    return {"directory": directory, "spec": spec, "entries": entries, "certificate": cert, "tag": tag}


def child_stage(child, row):
    if isinstance(row, str):
        row = child["entries"][row]
    assert plain(row) == plain(child["entries"][row["file"]])
    data = read(bound_file(child["directory"], row))
    assert data["complete"] is True and data["configuration"] == child["tag"]
    return data


def selected_child_names(item):
    answer = {}
    for label in ("R781", "R786"):
        answer[label] = {"full-outputs-manifest.json", "run-receipt.json",
                         item["retained_artifacts"][label]["certificate_name"]}
    answer["R781"].add("R781-original-real-field-input.json.gz")
    answer["R781"].update("R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz" for n in range(130))
    answer["R786"].add(R786_INDEX)
    assert len(answer["R781"]) == 134 and len(answer["R786"]) == 4
    return answer


def extract_original_carrier(bundle, root, item, original):
    """Hash all 1372 actual old members; retain only 134+4 needed child members."""
    wanted = selected_child_names(item)
    seen = {}
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            assert member.isfile() and not name.is_absolute() and ".." not in name.parts
            assert "\\" not in member.name and len(name.parts) == 2
            label, filename = name.parts
            assert label in wanted and member.name not in seen
            safe_name(filename)
            write = filename in wanted[label]
            path = Path(root)/label/filename
            if write:
                path.parent.mkdir(parents=True, exist_ok=True)
                temporary = path.with_name(path.name+".download")
                destination = temporary.open("wb")
            else:
                destination = None
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
            assert count == member.size
            row = {"file": filename, "bytes": count, "sha256": digest.hexdigest()}
            seen[member.name] = row
            if write:
                if path.exists():
                    assert file_spec(path) == row
                    temporary.unlink()
                else:
                    temporary.replace(path)
    assert len(seen) == 1372
    children = {label: child_metadata(root, label, item, original) for label in wanted}
    index = child_stage(children["R786"], children["R786"]["certificate"]["basis_index"])
    assert index["dimension"] == 1234 and index["bound_qY"] == 128
    assert len(index["basis_rows"]) == 1234
    full_expected = {label: set(names) for label, names in wanted.items()}
    full_expected["R786"].update(row["file"] for row in index["basis_rows"])
    for label, child in children.items():
        actual = {PurePosixPath(name).name for name in seen if name.startswith(label+"/")}
        assert actual == full_expected[label]
        for filename in actual:
            row = seen[label+"/"+filename]
            if filename == "full-outputs-manifest.json":
                assert row["sha256"] == child["spec"]["manifest_sha256"]
            else:
                assert row == plain(child["entries"][filename])
    assert len(full_expected["R781"]) == 134 and len(full_expected["R786"]) == 1238
    return {"original_bundle": file_spec(bundle), "all_1372_original_members_bytes_and_sha256_verified": True,
            "original_member_count": 1372, "selected_child_file_counts": {"R781": 134, "R786": 4},
            "discarded_original_xi_basis_rows_are_already_represented_by_verified_R787_real_rows": True}


def check_selected_sources(item, root, original):
    children = {label: child_metadata(root, label, item, original) for label in ("R781", "R786")}
    c781, c786 = children["R781"], children["R786"]
    field_input = child_stage(c781, "R781-original-real-field-input.json.gz")
    assert field_input["field"] == original.tag["field"]
    previous = None
    for n in range(130):
        name = "R781-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
        data = child_stage(c781, name)
        assert data["order"] == n and data["exact_differential_identity_at_this_order"] is True
        if previous is None:
            assert data["input_stage_sha256"] == c781["entries"]["R781-original-real-field-input.json.gz"]["sha256"]
        else:
            assert data["previous_stage_sha256"] == c781["entries"][previous]["sha256"]
        assert "kappa_power" in data["coefficients"]
        if n < 129:
            assert "R" in data["coefficients"]
        previous = name
    index = child_stage(c786, c786["certificate"]["basis_index"])
    rows = index["basis_rows"]
    assert index["dimension"] == 1234 and index["bound_qY"] == 128
    assert len(rows) == 1234 and [row["index"] for row in rows] == list(range(1234))
    for i, row in enumerate(rows):
        assert plain(row) == plain(c786["entries"][row["file"]])
        real_name = "R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
        data = original.stage(real_name)
        assert data["index"] == i and data["R786_row_sha256"] == row["sha256"]
        assert data["all_original_phase_involutions_verified"] is True
        assert data["averaging_used"] is False
        matrix = data["integer_t_coefficients"]
        assert len(matrix) == 129 and all(len(vector) == 20 for vector in matrix)
        assert all(isinstance(x, str) and INTEGER.fullmatch(x) for vector in matrix for x in vector)
    checkpoint = item["checkpoint"]
    chart = original.stage(checkpoint["chart_file"])
    selection = original.stage(checkpoint["selection_file"])
    blocks = original.stage(checkpoint["rational_blocks_file"])
    assert chart["actual_modular_rank"] == 1186 and chart["chosen_free_column"] == 1186
    assert chart["prime"] == selection["prime"] == checkpoint["prime"] == 1000000753
    assert blocks["prime"] == checkpoint["prime"]
    assert blocks["exact_E0_Z_zero_verified"] is True
    assert len(blocks["B_constant_pivot_columns"]) == 20
    assert len(blocks["B_constant_free_columns"]) == 1214
    assert len(blocks["Z_pivot_integer_rows"]) == 20
    assert all(len(row) == 1214 for row in blocks["Z_pivot_integer_rows"])
    assert INTEGER.fullmatch(blocks["Z_free_diagonal"]) and int(blocks["Z_free_diagonal"]) > 0
    lift = original.stage(checkpoint["lift_file"])
    assert lift["prime"] == checkpoint["prime"] and lift["digits"] == checkpoint["digits"] == 430
    assert lift["chart_sha256"] == original.files[checkpoint["chart_file"]]["sha256"]
    assert lift["full_original_modular_relations_verified"] is True
    for key, count in (("A_L_coordinates", 1234), ("C_L_coordinates", 1214)):
        assert len(lift[key]) == count and all(len(row) == 14 for row in lift[key])
        assert all(isinstance(x, str) and INTEGER.fullmatch(x) for row in lift[key] for x in row)
    del lift, blocks
    expected = set(META) | {checkpoint[k] for k in
        ("lift_file", "chart_file", "rational_blocks_file", "selection_file")}
    expected.update("R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(1234))
    assert set(original.selected) == expected
    for label, names in selected_child_names(item).items():
        actual = {path.name for path in (Path(root)/label).iterdir() if path.is_file()}
        assert actual == names
    return {"selected_source_file_counts": {"R787": len(expected), "R781": 134, "R786": 4},
            "original_field": field_input["field"],
            "R786_basis_index": plain(c786["certificate"]["basis_index"]),
            "all_selected_source_schemas_and_parent_child_identity_links_verified": True,
            "no_original_Dixon_or_real_basis_or_Laurent_arithmetic_repeated": True,
            "no_fourteen_branch_inverse_files_downloaded": True}


def inventory(root):
    result = {}
    for label in ("R787", "R781", "R786"):
        directory = Path(root)/label
        rows = [file_spec(path) for path in sorted(directory.iterdir()) if path.is_file()]
        assert len(rows) == len({row["file"] for row in rows})
        result[label] = rows
    return result


def verify_or_extract_bundle(bundle, root, inventories, extract=True):
    expected = {}
    for label, rows in inventories.items():
        assert label in ("R787", "R781", "R786")
        for row in rows:
            check_spec(row)
            key = label+"/"+row["file"]
            assert key not in expected
            expected[key] = row
    seen = set()
    with tarfile.open(bundle, "r|gz") as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            assert member.isfile() and not name.is_absolute() and ".." not in name.parts
            assert "\\" not in member.name and len(name.parts) == 2
            assert member.name in expected and member.name not in seen
            seen.add(member.name)
            row = expected[member.name]
            assert member.size == row["bytes"]
            path = Path(root)/str(name)
            if extract:
                path.parent.mkdir(parents=True, exist_ok=True)
                temporary = path.with_name(path.name+".download")
                destination = temporary.open("wb")
            else:
                destination = None
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
                if path.exists():
                    assert file_spec(path) == plain(row)
                    temporary.unlink()
                else:
                    temporary.replace(path)
    assert seen == set(expected)
    return len(seen)


def create_bundle(root, bundle, inventories):
    bundle = Path(bundle)
    if not bundle.exists():
        temporary = bundle.with_name(bundle.name+".tmp")
        with tarfile.open(temporary, "w:gz", compresslevel=1) as archive:
            for label in sorted(inventories):
                for row in inventories[label]:
                    path = bound_file(Path(root)/label, row)
                    info = tarfile.TarInfo(label+"/"+row["file"])
                    info.size, info.mtime, info.mode = row["bytes"], 0, 0o644
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    with path.open("rb") as stream:
                        archive.addfile(info, stream)
        temporary.replace(bundle)
    return verify_or_extract_bundle(bundle, root, inventories, extract=False)


def prepare_inputs(item, out):
    root = out.parent/"retained"
    previous = out/"retained-inputs-receipt.json"
    if (out/BUNDLE).exists():
        receipt = read(previous)
        assert receipt["result"] == RESULT and receipt["projective_mode"] is True
        assert receipt["original_R787_source"] == item["retained_source"]
        assert receipt["original_R787_configuration_sha256"] == item["pinned_R787_configuration_sha256"]
        assert file_spec(out/BUNDLE) == plain(receipt["bundle"])
        count = verify_or_extract_bundle(out/BUNDLE, root, receipt["selected_source_files"])
        original = original_source(item, root)
        schema = check_selected_sources(item, root, original)
        assert receipt["source_schema"] == schema
        assert receipt["file_count"] == count == 1380
        assert inventory(root) == receipt["selected_source_files"]
        print("PROJECTIVE_INPUT_REVIEW="+json.dumps({
            "result": RESULT, "selected_source_file_count": count,
            "all_active_bundle_members_bytes_and_sha256_verified": True,
            "old_sources_recomputed": False, "active_input_bundle_reused": True}), flush=True)
        return root
    archive = IO.Archive(item["retained_source"], out.parent/"download-original-R787", whole=False)
    try:
        original = original_source(item, root, archive)
        checkpoint = item["checkpoint"]
        names = [checkpoint[key] for key in ("lift_file", "chart_file",
                                            "rational_blocks_file", "selection_file")]
        names += ["R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(1234)]
        original.prefetch(names)
        bundle_row = original.files[OLD_BUNDLE]
        assert bundle_row["sha256"] == item["retained_source"]["files"][OLD_BUNDLE]
        old_bundle = out.parent/"original-carrier-transfer"/OLD_BUNDLE
        archive.extract_bound(OLD_BUNDLE, bundle_row["sha256"], old_bundle, bundle_row["bytes"])
        old_review = extract_original_carrier(old_bundle, root, item, original)
        schema = check_selected_sources(item, root, original)
        files = inventory(root)
        assert sum(map(len, files.values())) == 1380
        count = create_bundle(root, out/BUNDLE, files)
        receipt = {
            "result": RESULT, "projective_mode": True, "complete": True,
            "original_R787_source": item["retained_source"],
            "original_R787_configuration_sha256": item["pinned_R787_configuration_sha256"],
            "original_child_sources": item["retained_artifacts"],
            "original_carrier_complete_streamed_IO_review": old_review,
            "original_source_transfer": archive.receipt(),
            "selected_source_files": files, "source_schema": schema,
            "file_count": count, "selected_total_bytes": sum(row["bytes"] for rows in files.values() for row in rows),
            "bundle": file_spec(out/BUNDLE),
            "all_selected_source_and_new_carrier_member_bytes_and_sha256_verified": True,
            "new_mathematical_arithmetic_executed_during_input_review": False}
        save(previous, receipt)
        old_bundle.unlink()
        print("PROJECTIVE_INPUT_REVIEW="+json.dumps({
            "result": RESULT, "source": {key: item["retained_source"][key] for key in BASE},
            "original_carrier_member_count": 1372,
            "selected_source_file_count": count, "selected_source_counts": schema["selected_source_file_counts"],
            "bundle": receipt["bundle"], "all_SHA_verified": True,
            "no_fourteen_branch_inverse_files_downloaded": True,
            "actual_http_range_bytes_transferred": archive.receipt().get("actual_http_range_bytes_transferred"),
            "whole_original_ZIP_rehashed_in_this_subset_transfer": False,
            "new_mathematical_arithmetic_executed": False}), flush=True)
        return root
    finally:
        archive.close()


def stable_job(item):
    keys = ("result", "p", "core_sha256", "field_core_sha256",
            "projective_method_sha256", "R787_method_sha256", "R786_proof_sha256",
            "pinned_R787_configuration_sha256", "retained_source", "retained_artifacts", "checkpoint")
    return {key: item[key] for key in keys}


def check_new_tag(tag, item):
    assert tag["result"] == RESULT
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
    assert tag["R787_method_sha256"] == item["R787_method_sha256"]
    assert tag["R781_field_core_sha256"] == item["field_core_sha256"]
    assert tag["projective_method_sha256"] == item["projective_method_sha256"]
    assert tag["pinned_R787_configuration_sha256"] == item["pinned_R787_configuration_sha256"]
    assert tag["retained_source"] == item["retained_source"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]


def restore_resume(item, out):
    source = item.get("resume")
    if source is None:
        return
    assert source["result"] == RESULT and source["core_sha256"] == item["core_sha256"]
    assert source["source_commit"] and source["run_id"]
    archive = IO.Archive(source, out.parent/"download-projective-resume", whole=False)
    target = out.parent/"projective-resume-metadata"
    target.mkdir(parents=True, exist_ok=True)
    try:
        manifest_path = archive.extract_bound("full-outputs-manifest.json", source["manifest_sha256"],
                                              target/"full-outputs-manifest.json",
                                              source.get("manifest_bytes"))
        manifest = read(manifest_path)
        assert manifest["result"] == RESULT and manifest["projective_mode"] is True
        entries = {row["file"]: row for row in manifest["files"]}
        assert len(entries) == len(manifest["files"])
        for row in entries.values():
            check_spec(row)
        def metadata(name):
            row = entries[name]
            return read(archive.extract_bound(name, row["sha256"], target/name, row["bytes"]))
        initial, run = metadata("public-actions-input.json"), metadata("run-receipt.json")
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == source["core_sha256"]
        assert initial["projective_mode"] is True and run["projective_mode"] is True
        assert stable_job(initial["job"]) == stable_job(item)
        if "core-receipt.json" in entries:
            core = metadata("core-receipt.json")
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
            assert core["source_sha256"] == item["core_sha256"] and core["result"] == RESULT
        else:
            assert run["core_receipt_sha256"] is None
        receipt = metadata("retained-inputs-receipt.json")
        assert receipt["original_R787_source"] == item["retained_source"]
        assert plain(receipt["bundle"]) == plain(entries[BUNDLE])
        needed = [BUNDLE, "retained-inputs-receipt.json"]
        stages = []
        for name, row in entries.items():
            if name.startswith(PREFIX) and name.endswith(".json.gz"):
                stages.append(name)
            elif name == "R787-original-function-recipe.json.gz":
                stages.append(name)
        needed += stages
        if FINAL in entries:
            certificate = metadata(FINAL)
            check_new_tag(certificate["configuration"], item)
            if certificate["complete"] is True:
                needed.append(FINAL)
        archive.extract_many([(name, entries[name]["sha256"], out/name, entries[name]["bytes"])
                              for name in sorted(set(needed))])
        complete, current = 0, 0
        for name in stages:
            data = read(out/name)
            check_new_tag(data["configuration"], item)
            assert isinstance(data["complete"], bool)
            if data["complete"]:
                complete += 1
            else:
                current += 1
        save(out/"resume-receipt.json", {
            "result": RESULT, "projective_mode": True, "source": source,
            "source_manifest": file_spec(manifest_path), "complete_stages_restored": complete,
            "atomic_current_or_queue_stages_restored": current,
            "retained_complete_certificate": FINAL in needed,
            "all_restored_files_bytes_and_sha256_verified": True,
            "restored_files": [plain(entries[name]) for name in sorted(set(needed))],
            "source_transfer": archive.receipt(), "mathematical_recomputation_performed": False})
        print("PROJECTIVE_RESTORE_REVIEW="+json.dumps({
            "source_run_id": source["run_id"], "source_commit": source["source_commit"],
            "complete_stages": complete, "current_or_queue": current,
            "all_restored_bytes_SHA_verified": True, "old_arithmetic_recomputed": False}), flush=True)
    finally:
        archive.close()


def output_manifest(out):
    for path in out.iterdir():
        if path.is_file() and (path.name.endswith(".tmp") or path.name.endswith(".download")):
            path.unlink()
    rows = [file_spec(path) for path in sorted(out.iterdir())
            if path.is_file() and path.name not in ("full-outputs-manifest.json", REFERENCE)]
    save(out/"full-outputs-manifest.json", {
        "result": RESULT, "projective_mode": True, "files": rows,
        "reproducible_raw_location": "one-day active public Actions artifact",
        "outputs_or_carriers_published_to_git_or_release": False})
    path = out/"full-outputs-manifest.json"
    save(out/REFERENCE, {
        "result": RESULT, "projective_mode": True,
        "manifest_bytes": path.stat().st_size, "manifest_sha256": sha(path),
        "file_count": len(rows)})


def guard_and_sources(item):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert sha(__file__) == item["wrapper_sha256"]
    assert sha(S/item["core"]) == item["core_sha256"]
    assert sha(S/item["field_core"]) == item["field_core_sha256"]
    assert sha(topic_path(item["method"])) == item["projective_method_sha256"]
    assert sha(topic_path(item["original_method"])) == item["R787_method_sha256"]
    assert sha(topic_path(item["proof"])) == item["R786_proof_sha256"]
    assert sha(REPO/"README.md") == item["current_readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["current_readme_sha256"]["topic"]
    assert item["checkpoint"]["prime"] == 1000000753 and item["checkpoint"]["digits"] == 430
    for name in (item["core"], item["field_core"], item["io_helper"]):
        safe_name(name)
        path = S/name
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    load_io(item)


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "projective_mode": True, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "core_sha256": sha(S/item["core"]), "driver_sha256": sha(__file__),
        "field_core_sha256": sha(S/item["field_core"]),
        "method_sha256": sha(topic_path(item["method"])),
        "original_method_sha256": sha(topic_path(item["original_method"])),
        "proof_sha256": sha(topic_path(item["proof"])),
        "workflow_sha256": sha(REPO/item["workflow"]), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "job": item, "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_relation_claimed_before_exact_core_verification": False})
    code, error = 1, None
    try:
        guard_and_sources(item)
        restore_resume(item, out)
        retained = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(S/item["core"]),
                   "--config", str(config), "--method", str(topic_path(item["method"])),
                   "--field-core", str(S/item["field_core"]), "--retained", str(retained),
                   "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                error = "Outer budget reached; atomic projective stages and the active carrier remain available."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    core_path = out/"core-receipt.json"
    core = read(core_path) if core_path.exists() else {}
    complete = code == 0 and core.get("complete") is True
    if complete:
        assert (out/FINAL).exists() and read(out/FINAL)["complete"] is True
    save(out/"run-receipt.json", {
        "result": RESULT, "projective_mode": True, "p": 41,
        "complete": complete, "process_exit_code": code, "error": error,
        "core_receipt_sha256": sha(core_path) if core_path.exists() else None,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "actual_y_map_recovered": complete, "beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print("PROJECTIVE_RUN_RECEIPT="+json.dumps(read(out/"run-receipt.json")), flush=True)
    return code if code else (0 if complete else 1)


def verify(out):
    """Verify all actual output/carrier bytes and schemas without mathematical imports."""
    manifest_path = out/"full-outputs-manifest.json"
    manifest, reference = read(manifest_path), read(out/REFERENCE)
    assert manifest["result"] == RESULT and manifest["projective_mode"] is True
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    actual = {path.name for path in out.iterdir() if path.is_file()}
    assert actual == set(entries) | {"full-outputs-manifest.json", REFERENCE}
    for row in entries.values():
        bound_file(out, row)
    assert reference["manifest_sha256"] == sha(manifest_path)
    assert reference["manifest_bytes"] == manifest_path.stat().st_size
    assert reference["file_count"] == len(entries)
    initial, run = read(out/"public-actions-input.json"), read(out/"run-receipt.json")
    item = initial["job"]
    guard_and_sources(item)
    assert initial["result"] == run["result"] == RESULT
    assert initial["projective_mode"] is True and run["projective_mode"] is True
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["field_core_sha256"] == item["field_core_sha256"]
    assert initial["method_sha256"] == item["projective_method_sha256"]
    assert initial["original_method_sha256"] == item["R787_method_sha256"]
    assert initial["proof_sha256"] == item["R786_proof_sha256"]
    core_path = out/"core-receipt.json"
    if not core_path.exists():
        assert run["core_receipt_sha256"] is None
        raise AssertionError("No complete mathematical core receipt; preserved IO is not a completed relation.")
    core = read(core_path)
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
    receipt = read(out/"retained-inputs-receipt.json")
    assert receipt["original_R787_source"] == item["retained_source"]
    assert receipt["original_child_sources"] == item["retained_artifacts"]
    assert receipt["all_selected_source_and_new_carrier_member_bytes_and_sha256_verified"] is True
    assert plain(receipt["bundle"]) == plain(entries[BUNDLE])
    retained = out.parent/"retained"
    count = verify_or_extract_bundle(out/BUNDLE, retained, receipt["selected_source_files"])
    original = original_source(item, retained)
    schema = check_selected_sources(item, retained, original)
    assert count == receipt["file_count"] == 1380 and schema == receipt["source_schema"]
    assert receipt["selected_source_files"] == inventory(retained)
    if run["complete"] is not True or core["complete"] is not True:
        print("PROJECTIVE_PRESERVED_IO_REVIEW="+json.dumps({
            "complete_relation": False, "all_manifest_bytes_SHA_verified": True,
            "all_1380_active_input_files_bytes_SHA_verified": True,
            "process_exit_code": run["process_exit_code"], "core_receipt": core}), flush=True)
        return 1
    assert run["process_exit_code"] == 0
    assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True
    assert cert["p"] == 41 and cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["original_full_L_retained"] is True
    assert cert["exact_nonzero_A_B_relation_verified"] is True
    assert cert["same_normalized_1186_direction_verified"] is True
    assert cert["exact_verified_Laurent_exponents"] == [-1, 127]
    assert cert["exact_verified_t_coordinates"] == 20
    assert cert["exact_verified_Q_coordinates_per_order"] == 280 and cert["exact_verified_orders"] == 129
    assert cert["actual_y_map_recovered"] is True and cert["beta_or_height_computed"] is False
    tag = cert["configuration"]
    check_new_tag(tag, item)
    assert tag["field"] == schema["original_field"]
    assert tag["basis_integer_scale"] == "13744803133596058624"
    def stage(row):
        assert plain(row) == plain(entries[row["file"]])
        data = read(bound_file(out, row))
        assert data["complete"] is True and data["configuration"] == tag
        return data
    recipe = stage(cert["relation_spec"])
    assert cert["relation_spec"]["file"] == "R787-original-function-recipe.json.gz"
    assert recipe["field"] == schema["original_field"]
    assert recipe["basis_integer_scale"] == "13744803133596058624"
    assert recipe["R786_producer"] == item["retained_artifacts"]["R786"]
    assert plain(recipe["R786_basis_index"]) == schema["R786_basis_index"]
    assert recipe["original_R786_basis_order"] is True
    assert recipe["exact_original_A_equals_yB"] is True and recipe["B_nonzero"] is True
    assert recipe["full_129_original_relations_verified"] is True
    assert recipe["candidate_only_until_full_exact_verification"] is False
    for key in ("A_integer_L_coordinates", "B_integer_L_coordinates"):
        matrix = recipe[key]
        assert len(matrix) == 1234 and all(len(row) == 14 for row in matrix)
        assert all(isinstance(x, str) and INTEGER.fullmatch(x) for row in matrix for x in row)
    assert any(x != "0" for row in recipe["B_integer_L_coordinates"] for x in row)
    assert int(recipe["common_rational_denominator_cleared"]) > 0
    assert int(recipe["common_integer_content_removed"]) > 0
    listed = stage(cert["stage_manifest"])
    stage_rows = listed["files"]
    assert len(stage_rows) == len({row["file"] for row in stage_rows})
    for row in stage_rows:
        stage(row)
    actual_complete = set()
    for name in entries:
        if (name.startswith(PREFIX) and name.endswith(".json.gz")) or name == "R787-original-function-recipe.json.gz":
            if name == cert["stage_manifest"]["file"]:
                continue
            data = read(out/name)
            assert data["configuration"] == tag and isinstance(data["complete"], bool)
            if data["complete"]:
                actual_complete.add(name)
    assert {row["file"] for row in stage_rows} == actual_complete
    print("PROJECTIVE_COMPLETE_IO_REVIEW="+json.dumps({
        "result": RESULT, "new_core_sha256": item["core_sha256"],
        "complete_relation": True, "original_source_run_id": item["retained_source"]["run_id"],
        "original_checkpoint_digits": 430, "same_normalized_1186_direction_verified": True,
        "exact_original_relations": {"orders": 129, "Q_coordinates_per_order": 280},
        "output_manifest": file_spec(manifest_path), "manifest_file_count": len(entries),
        "active_input_file_count": count, "relation_spec": plain(cert["relation_spec"]),
        "stage_manifest": plain(cert["stage_manifest"]), "core_seconds": cert.get("seconds"),
        "all_output_and_active_input_bytes_SHA_verified": True,
        "mathematical_core_reimported_or_reexecuted_during_IO_review": False}), flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("compute", "verify"))
    args = parser.parse_args()
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/"R787-projective"/"output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    return verify(out)


if __name__ == "__main__":
    sys.exit(main())
