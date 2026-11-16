#!/usr/bin/env python3
"""R860 standard-library source transport and exact-expression runner.

This module imports only the frozen standard-library R837/Range transport.
The separate core constructs the mathematical expression DAG in Actions.
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
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R860-semilinear-resolvent-DAG-public-request.json"
RESULT = "R860-original-semilinear-resolvent-DAG"
FINAL = "p41-original-semilinear-resolvent-DAG-certificate.json"
PREFIX = "R860-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R860-retained-original-inputs.tar.gz"
INVENTORY = "R860-original-source-inventory.json"
INPUT_RECEIPT = "R860-retained-inputs-receipt.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOF_KEYS = ("R802", "R805", "R806", "R813", "R853", "FM", "R860")
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
SOURCE_DEFINITIONS = {
    "R805": {
        "result": "R805-original-affine-pencil-free-basis",
        "core_sha256": "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420",
        "certificate": "p41-original-affine-pencil-free-basis-certificate.json", "count": 7,
    },
    "R806": {
        "result": "R806-original-primitive-multiplication",
        "core_sha256": "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d",
        "certificate": "p41-original-primitive-multiplication-certificate.json", "count": 45,
    },
    "R853": {
        "result": "R853-original-semilinear-V1-generator-conjugates",
        "core_sha256": "5b65e7ccf7c6663949155fdd30abc4c765823e861259c8f9b90b26d0bc1511df",
        "certificate": "p41-original-semilinear-V1-conjugates-certificate.json", "count": 9,
    },
}
EPS = [0] + [1] * 144 + [2] * 127
STRATEGY = {
    "scope": "two_original_cofactor_expressions_and_fixed_differential",
    "normal_basis_rank": 272,
    "original_target_normal_basis_index": 72,
    "original_target_V1_index": 73,
    "matrix_convention": "row_output_column_input",
    "denominator_deleted_row": 0,
    "denominator_deleted_column": 0,
    "numerator_deleted_row": 72,
    "numerator_deleted_column": 0,
    "numerator_cofactor_sign": 1,
    "denominator_T_degree": 271,
    "denominator_total_degree_bound": 271,
    "numerator_T_degree_bound": 270,
    "numerator_total_degree_bound": 272,
    "denominator_nonzero_basis": "monic_T_degree271_below_original_minimal_degree272",
    "source_coefficients": "original_R806_numerator_over_original_column_denominator",
    "old_integer_scale_reinserted": False,
    "full_characteristic_zero_Krylov_inverse_computed": False,
    "expanded_bivariate_cofactors_computed": False,
    "expanded_power_basis_coordinates_computed": False,
    "original_RR_kernel_or_connection_or_period_computed": False,
    "derivation_action": "c_Y_delta_equals_delta_c_Y",
    "differential_action": "c_Y_nu_equals_nu",
    "original_D0": "qY/82*d/dqY",
    "original_nu": "82*tau*dqY/qY",
    "only_transport_directory_resume_and_budget_excluded_from_mathematical_identity": True,
}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.suffix == ".gz"
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name and name not in (".", "..")
    assert "\\" not in name
    return name


def plain(value):
    result = {key: value[key] for key in ("file", "bytes", "sha256")}
    safe_name(result["file"])
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert re.fullmatch(r"[0-9a-f]{64}", result["sha256"])
    return result


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(folder, reference):
    reference = plain(reference)
    path = Path(folder) / reference["file"]
    assert file_spec(path) == reference, path.name
    return path


def identity(source):
    return {key: source[key] for key in BASE}


def source_identity(source):
    return {
        **identity(source), "certificate": plain(source["certificate"]),
        "configuration_sha256": source["configuration_sha256"],
        "selected_files_sha256": fingerprint(source["files"]),
        "selected_file_count": len(source["files"]),
    }


def topic_path(value):
    path = PurePosixPath(value)
    assert not path.is_absolute() and ".." not in path.parts
    result = (TOPIC / str(path)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def load_transport(item):
    path = S / safe_name(item["transport_helper"])
    assert path.name == "R837_original_branch_pencil_public.py"
    assert sha(path) == item["transport_helper_sha256"] == TRANSPORT_SHA
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    module_spec = importlib.util.spec_from_file_location("R860_frozen_R837_transport", path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.load_io(item)
    return module


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R860 runs only in the public repository Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == "R860_original_semilinear_resolvent_DAG.py"
    assert item["wrapper"] == "R860_public_original_semilinear_resolvent_DAG.py"
    assert sha(S / item["core"]) == item["core_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300
    assert set(item["proofs"]) == set(PROOF_KEYS)
    for entry in item["proofs"].values():
        assert sha(topic_path(entry["path"])) == entry["sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    assert sha(REPO / "README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC / "README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(SOURCE_DEFINITIONS)
    for label, source in item["sources"].items():
        definition = SOURCE_DEFINITIONS[label]
        assert source["result"] == definition["result"]
        assert source["core_sha256"] == definition["core_sha256"]
        assert source["expected_conclusion"] == "success"
        assert source["certificate"]["file"] == definition["certificate"]
        assert len(source["files"]) == source["selected_file_count"] == definition["count"]
        assert fingerprint(source["files"]) == source["selected_files_sha256"]
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
        if label in ("R805", "R806"):
            assert source["transport_source"]["type"] == "unchanged_original_input_carrier"
            assert source["transport_source"]["original_group"] == label
        else:
            assert source.get("transport_source") is None
    return load_transport(item)


def selected_names(label, directory):
    certificate = read(directory / SOURCE_DEFINITIONS[label]["certificate"])
    names = {MANIFEST, *META, SOURCE_DEFINITIONS[label]["certificate"]}
    if label == "R805":
        names.update(certificate[key]["file"] for key in ("pencil_stage", "graded_free_basis_stage"))
    elif label == "R806":
        names.update(certificate[key]["file"] for key in (
            "stage_manifest", "coordinate_chart", "accepted_candidate", "polynomial_multiplier"))
        accepted = read(directory / certificate["accepted_candidate"]["file"])
        interface = read(directory / certificate["polynomial_multiplier"]["file"])
        names.add(accepted["candidate_definition"]["file"])
        names.add(interface["actual_cyclic_witness"]["file"])
        names.update(row["file"] for row in interface["coordinate_groups"])
    else:
        assert label == "R853"
        names.update(certificate[key]["file"] for key in (
            "source_audit", "three_conjugate_coordinates", "function_field_action_DAG", "stage_manifest"))
    assert len(names) == SOURCE_DEFINITIONS[label]["count"]
    return names


def source_review(label, source, directory):
    directory = Path(directory)
    files = {name: plain(entry) for name, entry in source["files"].items()}
    assert len(files) == SOURCE_DEFINITIONS[label]["count"]
    assert all(name == entry["file"] for name, entry in files.items())
    for entry in files.values():
        bound(directory, entry)
    assert fingerprint(files) == source["selected_files_sha256"]
    assert files[MANIFEST]["sha256"] == source["manifest_sha256"]
    assert files[MANIFEST]["bytes"] == source["manifest_bytes"]
    manifest = read(directory / MANIFEST)
    assert manifest["result"] == source["result"]
    entries = {entry["file"]: plain(entry) for entry in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    for name, entry in files.items():
        if name != MANIFEST:
            assert entries[name] == entry
    assert set(files) == selected_names(label, directory)
    initial, run, core = (read(directory / name) for name in META)
    assert initial["result"] == run["result"] == core["result"] == source["result"]
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
    assert run["process_exit_code"] == 0 and run["complete"] is True
    assert run["error"] is None and core["complete"] is True
    assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    certificate_spec = plain(source["certificate"])
    assert files[certificate_spec["file"]] == certificate_spec
    assert core["certificate_sha256"] == certificate_spec["sha256"]
    certificate = read(directory / certificate_spec["file"])
    assert certificate["result"] == source["result"] and certificate["complete"] is True
    tag = certificate["configuration"]
    assert tag["source_sha256"] == source["core_sha256"]
    assert tag["result"] == source["result"]
    assert fingerprint(tag) == source["configuration_sha256"]
    for name in files:
        if name.endswith(".json.gz") and not (label == "R806" and "-group-" in name):
            value = read(directory / name)
            assert value["complete"] is True and value["configuration"] == tag, (label, name)
    if label == "R805":
        assert certificate["actual_pencil_n"] == 1 and certificate["affine_free_module_rank"] == 272
        assert certificate["graded_free_basis_degrees"] == [1, 144, 127]
    elif label == "R806":
        assert certificate["normal_affine_basis_rank"] == 272
        assert certificate["original_function_field_primitive_generator_certified"] is True
        assert certificate["all272_columns_verified_in_all820_original_rows"] is True
        assert certificate["actual_cyclic_minor_certified"] is True
        assert len(certificate["exact_coordinate_groups"]) == 34
        for row in certificate["exact_coordinate_groups"]:
            assert files[row["file"]] == plain(row)
    else:
        assert certificate["original_three_V1_conjugates_certified"] is True
        assert certificate["original_semilinear_function_field_generator_action_certified"] is True
        assert certificate["full_original_coordinate_rows"] == 560
    return {**identity(source), "certificate": certificate_spec,
            "configuration_sha256": source["configuration_sha256"],
            "selected_files_sha256": fingerprint(files), "files": files}


def cross_source_review(sources, retained):
    c805 = read(retained / "R805" / SOURCE_DEFINITIONS["R805"]["certificate"])
    c806 = read(retained / "R806" / SOURCE_DEFINITIONS["R806"]["certificate"])
    c853 = read(retained / "R853" / SOURCE_DEFINITIONS["R853"]["certificate"])
    interface = read(retained / "R806" / c806["polynomial_multiplier"]["file"])
    dag = read(retained / "R853" / c853["function_field_action_DAG"]["file"])
    assert interface["original_R805_free_basis"] == c805["graded_free_basis_stage"]
    assert dag["original_normal_free_basis"] == c805["graded_free_basis_stage"]
    assert dag["original_polynomial_multiplier_index"] == c806["polynomial_multiplier"]
    assert identity(c806["configuration"]["retained_artifacts"]["R805"]) == identity(sources["R805"])
    assert identity(c853["configuration"]["sources"]["R806"]) == identity(sources["R806"])


def expected_tag(item, sources):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "arithmetic": "stdlib_exact_source_and_determinant_expression_program",
        "proofs_sha256": {key: item["proofs"][key]["sha256"] for key in PROOF_KEYS},
        "method_sha256": item["method_sha256"],
        "sources": {key: source_identity(sources[key]) for key in sorted(SOURCE_DEFINITIONS)},
        "normal_basis_degrees": EPS, "strategy": STRATEGY,
    }


def extract_carrier_group(bundle, members, selected_group, selected_files, destination):
    expected = {}
    for group, files in members.items():
        for name, entry in files.items():
            safe_name(group)
            assert safe_name(name) == entry["file"]
            expected[group + "/" + name] = plain(entry)
    assert members[selected_group] == selected_files
    seen = set()
    with tarfile.open(bundle, "r:gz") as archive:
        for entry in archive:
            name = PurePosixPath(entry.name)
            assert entry.isfile() and not name.is_absolute() and len(name.parts) == 2
            assert ".." not in name.parts and entry.name not in seen and entry.name in expected
            seen.add(entry.name)
            reference = expected[entry.name]
            assert entry.size == reference["bytes"]
            target = destination / name.parts[1] if name.parts[0] == selected_group else None
            temporary = target.with_name(target.name + ".transfer") if target is not None else None
            output = temporary.open("wb") if temporary is not None else None
            digest, total = hashlib.sha256(), 0
            stream = archive.extractfile(entry)
            assert stream is not None
            try:
                for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
                    digest.update(block)
                    total += len(block)
                    if output is not None:
                        output.write(block)
            finally:
                stream.close()
                if output is not None:
                    output.close()
            assert total == reference["bytes"] and digest.hexdigest() == reference["sha256"]
            if temporary is not None:
                temporary.replace(target)
    assert seen == set(expected)
    return len(seen)


def download_carried_source(label, item, retained, out, transport):
    source = item["sources"][label]
    route = source["transport_source"]
    carrier_source = route["source"]
    assert route["type"] == "unchanged_original_input_carrier"
    assert route["original_group"] == label
    directory = retained / label
    directory.mkdir(parents=True, exist_ok=True)
    metadata = out.parent / ("carrier-metadata-" + label)
    metadata.mkdir(parents=True, exist_ok=True)
    print("R860_SOURCE_CARRIER_START=" + label, flush=True)
    archive = transport.IO.Archive(carrier_source, out.parent / ("download-carrier-" + label), whole=False)
    try:
        archive.extract_bound(MANIFEST, carrier_source["manifest_sha256"], metadata / MANIFEST,
                              carrier_source["manifest_bytes"])
        manifest = read(metadata / MANIFEST)
        assert manifest["result"] == carrier_source["result"]
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == carrier_source["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name, entry in route["metadata_files"].items():
            assert name == entry["file"] and entries[name] == plain(entry)
        archive.extract_many([(name, entry["sha256"], metadata / name, entry["bytes"])
                              for name, entry in route["metadata_files"].items()])
        initial, run = (read(metadata / name) for name in ("public-actions-input.json", "run-receipt.json"))
        assert initial["result"] == run["result"] == carrier_source["result"]
        assert initial["source_commit"] == run["source_commit"] == carrier_source["source_commit"]
        assert str(run["workflow_run_id"]) == str(carrier_source["run_id"])
        assert initial["core_sha256"] == carrier_source["core_sha256"]
        assert run["process_exit_code"] == route["actual_process_exit_code"]
        assert run["complete"] is (route["actual_process_exit_code"] == 0)
        if "core-receipt.json" in route["metadata_files"]:
            core = read(metadata / "core-receipt.json")
            assert core["result"] == carrier_source["result"]
            assert core["source_sha256"] == carrier_source["core_sha256"]
            assert run["core_receipt_sha256"] == route["metadata_files"]["core-receipt.json"]["sha256"]
        else:
            assert label == "R806" and run["complete"] is False
            assert run["core_receipt_sha256"] is None and "core-receipt.json" not in entries
        carrier_receipt = read(bound(metadata, route["input_receipt"]))
        if label == "R806":
            assert carrier_source["result"] == "R815-original-normal-derivation-operators"
            assert identity(initial["job"]["retained_artifacts"][label]) == identity(source)
            original_producer = carrier_receipt["producer_identities"][label]
            assert identity(original_producer) == identity(source)
            assert original_producer["certificate_name"] == source["certificate"]["file"]
            assert original_producer["certificate_sha256"] == source["certificate"]["sha256"]
            members = {group: {entry["file"]: plain(entry) for entry in files}
                       for group, files in carrier_receipt["selected_files"].items()}
            assert set(members) == {"R806", "R813"}
            assert carrier_receipt["all_selected_bundle_members_individually_size_and_sha256_verified"] is True
            assert carrier_receipt["no_old_arithmetic_recomputed"] is True
            bundle = plain(carrier_receipt["input_bundle"])
            member_count = carrier_receipt["actual_selected_file_count"]
        else:
            assert label == "R805" and carrier_source["result"] == "R856-original-fixed-branch-ideal-bases"
            assert identity(initial["job"]["sources"][label]) == identity(source)
            inventory = read(bound(metadata, route["source_inventory"]))
            assert inventory["result"] == carrier_source["result"] and inventory["complete"] is True
            assert carrier_receipt["result"] == carrier_source["result"] and carrier_receipt["complete"] is True
            assert plain(carrier_receipt["source_inventory"]) == plain(route["source_inventory"])
            assert identity(inventory["sources"][label]) == identity(source)
            members = {group: {name: plain(entry) for name, entry in value["files"].items()}
                       for group, value in inventory["sources"].items()}
            assert set(members) == {"R820", "R805", "R837"}
            bundle = plain(carrier_receipt["source_bundle"])
            member_count = carrier_receipt["minimal_bundle_member_count"]
        assert bundle == plain(route["input_bundle"]) == entries[bundle["file"]]
        assert member_count == route["actual_carrier_member_count"]
        assert members[label] == source["files"]
        archive.extract_bound(bundle["file"], bundle["sha256"], metadata / bundle["file"], bundle["bytes"])
        count = extract_carrier_group(metadata / bundle["file"], members, label, source["files"], directory)
        assert count == member_count
        reviewed = source_review(label, source, directory)
        metadata_output = []
        for name in (MANIFEST, *sorted(route["metadata_files"])):
            target = out / ("R860-transport-" + label + "-" + name)
            shutil.copyfile(metadata / name, target)
            metadata_output.append({"original_file": name, "retained_file": file_spec(target)})
        receipt = {
            "type": route["type"], "carrier_producer": identity(carrier_source),
            "actual_transport_process_exit_code": run["process_exit_code"],
            "transport_success_not_required_for_unchanged_original_input_bytes": label == "R806",
            "input_bundle": bundle, "all_carrier_member_count_and_hashes_verified": count,
            "actual_original_group_retained": label, "actual_selected_original_file_count": len(source["files"]),
            "original_mathematical_producer_preserved": identity(source),
            "transport_metadata_original_bytes": metadata_output,
            "range_transport": archive.receipt(), "new_mathematics_executed": False,
        }
        print("R860_SOURCE_CARRIER_COMPLETE=" + json.dumps({"label": label,
              "all_carrier_members_hashed": count, "selected_original_files": len(source["files"]),
              "original_producer_preserved": identity(source)}, sort_keys=True), flush=True)
        return reviewed, receipt
    finally:
        archive.close()


def download_source(label, item, retained, out, transport):
    source = item["sources"][label]
    if source.get("transport_source") is not None:
        return download_carried_source(label, item, retained, out, transport)
    directory = retained / label
    directory.mkdir(parents=True, exist_ok=True)
    print("R860_SOURCE_START=" + label, flush=True)
    archive = transport.IO.Archive(source, out.parent / ("download-" + label), whole=False)
    try:
        archive.extract_bound(MANIFEST, source["manifest_sha256"], directory / MANIFEST,
                              source["manifest_bytes"])
        manifest = read(directory / MANIFEST)
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert manifest["result"] == source["result"]
        assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name, row in entries.items():
            assert len(archive.by_name[name]) == 1
            assert archive.by_name[name][0].file_size == row["bytes"]
        requested = []
        for name, row in source["files"].items():
            if name == MANIFEST:
                continue
            assert plain(row) == entries[name]
            requested.append((name, row["sha256"], directory / name, row["bytes"]))
        archive.extract_many(requested)
        reviewed = source_review(label, source, directory)
        print("R860_SOURCE_COMPLETE=" + json.dumps({"label": label, "files": len(reviewed["files"]),
              "selected_files_sha256": reviewed["selected_files_sha256"]}, sort_keys=True), flush=True)
        return reviewed, archive.receipt()
    finally:
        archive.close()


def prepare_sources(item, out, transport, allow_download=True):
    retained = out.parent / "retained-original-R860"
    retained.mkdir(parents=True, exist_ok=True)
    if all((out / name).exists() for name in (INPUT_RECEIPT, INVENTORY, BUNDLE)):
        receipt, inventory = read(out / INPUT_RECEIPT), read(out / INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is True and inventory["complete"] is True
        assert receipt["source_mathematical_identities"] == {
            key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)}
        bound(out, receipt["source_inventory"])
        bound(out, receipt["source_bundle"])
        for label, transfer in receipt["range_transport"].items():
            if transfer.get("type") == "unchanged_original_input_carrier":
                assert transfer["original_mathematical_producer_preserved"] == identity(item["sources"][label])
                for entry in transfer["transport_metadata_original_bytes"]:
                    assert entry["retained_file"]["file"] == "R860-transport-" + label + "-" + entry["original_file"]
                    bound(out, entry["retained_file"])
        count = transport.unpack_sources(out / BUNDLE, retained, inventory)
        reviewed = {key: source_review(key, item["sources"][key], retained / key)
                    for key in sorted(SOURCE_DEFINITIONS)}
        assert reviewed == inventory["sources"]
        assert count == receipt["minimal_bundle_member_count"] == 61
        cross_source_review(reviewed, retained)
        return retained, receipt, reviewed
    assert allow_download, "The exact source carrier is required for verification."
    reviewed, transfers = {}, {}
    for key in sorted(SOURCE_DEFINITIONS):
        reviewed[key], transfers[key] = download_source(key, item, retained, out, transport)
    cross_source_review(reviewed, retained)
    inventory = {"result": RESULT, "complete": True, "sources": reviewed,
                 "all_original_bytes_preserved": True}
    save(out / INVENTORY, inventory)
    transport.pack_sources(retained, inventory, out / BUNDLE)
    receipt = {
        "result": RESULT, "complete": True,
        "source_mathematical_identities": {key: source_identity(item["sources"][key])
                                          for key in sorted(SOURCE_DEFINITIONS)},
        "source_inventory": file_spec(out / INVENTORY), "source_bundle": file_spec(out / BUNDLE),
        "minimal_bundle_member_count": 61, "range_transport": transfers,
        "new_mathematics_executed_in_source_preparation": False,
    }
    save(out / INPUT_RECEIPT, receipt)
    print("R860_INPUT_REVIEW=" + json.dumps(receipt, sort_keys=True), flush=True)
    return retained, receipt, reviewed


def stable_job(item):
    result = {key: value for key, value in item.items()
              if key not in ("resume", "budget_minutes", "rules_last_read_commit", "readme_sha256", "sources")}
    result["sources"] = {key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)}
    return result


def restore(item, out, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    directory = out.parent / "resume-metadata"
    directory.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(resume, out.parent / "download-R860-continuation", whole=False)
    try:
        archive.extract_bound(MANIFEST, resume["manifest_sha256"], directory / MANIFEST, resume["manifest_bytes"])
        manifest = read(directory / MANIFEST)
        assert manifest["result"] == RESULT
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == resume["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name in (*META, INPUT_RECEIPT, INVENTORY, BUNDLE):
            if name == "core-receipt.json" and name not in entries:
                continue
            row = entries[name]
            destination = out / name if name in (INPUT_RECEIPT, INVENTORY, BUNDLE) else directory / name
            archive.extract_bound(name, row["sha256"], destination, row["bytes"])
        initial = read(directory / "public-actions-input.json")
        run = read(directory / "run-receipt.json")
        assert initial["result"] == run["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == resume["source_commit"]
        assert str(run["workflow_run_id"]) == str(resume["run_id"])
        assert initial["core_sha256"] == item["core_sha256"]
        assert stable_job(initial["job"]) == stable_job(item)
        if "core-receipt.json" in entries:
            core = read(directory / "core-receipt.json")
            assert core["source_sha256"] == item["core_sha256"] and core["result"] == RESULT
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        for name, row in entries.items():
            if name.startswith("R860-transport-") and name.endswith(".json"):
                archive.extract_bound(name, row["sha256"], out / name, row["bytes"])
        unused, receipt, sources = prepare_sources(item, out, transport, allow_download=False)
        tag = expected_tag(item, sources)
        restored = []
        for name, row in sorted(entries.items()):
            if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
                continue
            archive.extract_bound(name, row["sha256"], out / name, row["bytes"])
            value = read(out / name)
            assert value["configuration"] == tag and value["result"] == RESULT
            assert value["complete"] is (name != "R860-current.json.gz")
            restored.append(row)
        final_was_complete = False
        if FINAL in entries:
            row = entries[FINAL]
            archive.extract_bound(FINAL, row["sha256"], directory / FINAL, row["bytes"])
            final = read(directory / FINAL)
            assert final["configuration"] == tag and final["result"] == RESULT
            final_was_complete = final["complete"]
            assert isinstance(final_was_complete, bool)
            if final_was_complete:
                shutil.copyfile(directory / FINAL, out / FINAL)
        save(out / "R860-resume-transport-receipt.json", {
            "result": RESULT, "complete": True, "source": resume,
            "restored_mathematical_stages": restored,
            "source_inventory": receipt["source_inventory"],
            "previous_FINAL_complete": final_was_complete,
            "false_FINAL_not_restored_or_used_to_lock_new_current": True,
            "range_transport": archive.receipt(), "old_mathematics_recomputed": False,
        })
    finally:
        archive.close()


def output_manifest(out):
    files = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in (MANIFEST, REFERENCE) or path.name.endswith(".tmp"):
            continue
        files.append({**file_spec(path), "included_in_git": False})
    save(out / MANIFEST, {"result": RESULT, "files": files,
         "temporary_active_checkpoint_retention_days": 1, "reproducible_data_in_git_or_release": False})
    save(out / REFERENCE, {"result": RESULT, **file_spec(out / MANIFEST)})


def compute(item, out, request, transport):
    out.mkdir(parents=True, exist_ok=True)
    code, error, outer_timeout = 1, None, False
    try:
        restore(item, out, transport)
        retained, receipt, sources = prepare_sources(item, out, transport)
        expanded = dict(item)
        expanded["sources"] = {key: dict(value, directory=str((retained / key).resolve()))
                               for key, value in sources.items()}
        expanded["proofs"] = {key: dict(value, path=str(topic_path(value["path"])))
                              for key, value in item["proofs"].items()}
        expanded["method"] = str(topic_path(item["method"]))
        save(out / "public-actions-expanded-job.json", expanded)
        save(out / "public-actions-input.json", {
            "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
            "source_commit": os.environ["GITHUB_SHA"], "job": item,
            "core_sha256": item["core_sha256"], "driver_sha256": sha(__file__),
            "method_sha256": item["method_sha256"], "proofs_sha256": {
                key: value["sha256"] for key, value in item["proofs"].items()},
            "request_sha256": sha(request), "workflow_sha256": sha(REPO / item["workflow"]),
            "root_readme_sha256": sha(REPO / "README.md"),
            "topic_readme_sha256": sha(TOPIC / "README.md"),
            "transport_helper_sha256": item["transport_helper_sha256"],
            "io_helper_sha256": item["io_helper_sha256"],
            "source_inventory": receipt["source_inventory"],
            "actual_configuration": expected_tag(item, sources),
            "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "new_arithmetic_in_wrapper": False,
        })
        command = [sys.executable, str(S / item["core"]), "--config", str(out / "public-actions-expanded-job.json"),
                   "--out", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out / "public-actions-run.log").open("ab") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=60 * (item["budget_minutes"] + 10))
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code, error = 124, "outer_timeout"
        if code == 0:
            assert (out / FINAL).exists() and read(out / FINAL)["complete"] is True
        print((out / "public-actions-run.log").read_text(errors="replace")[-16000:], flush=True)
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
        traceback.print_exc()
    finally:
        save(out / "run-receipt.json", {
            "result": RESULT, "p": 41, "complete": code == 0, "process_exit_code": code,
            "error": error, "outer_timeout": outer_timeout,
            "source_commit": os.environ["GITHUB_SHA"],
            "workflow_run_id": os.environ["GITHUB_RUN_ID"],
            "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"),
            "execution_environment": "public-repository-github-actions",
            "core_receipt_sha256": sha(out / "core-receipt.json") if (out / "core-receipt.json").exists() else None,
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        })
        output_manifest(out)
    return code


def verify(item, out, request, transport):
    manifest = read(out / MANIFEST)
    assert manifest["result"] == RESULT
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for row in entries.values():
        bound(out, row)
    reference = read(out / REFERENCE)
    assert plain(reference) == file_spec(out / MANIFEST)
    run = read(out / "run-receipt.json")
    assert run["result"] == RESULT and run["source_commit"] == os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"]) == str(os.environ["GITHUB_RUN_ID"])
    if "public-actions-input.json" not in entries:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
        print("R860_VERIFY=source_preparation_incomplete", flush=True)
        return 0
    initial = read(out / "public-actions-input.json")
    assert initial["job"] == item and initial["request_sha256"] == sha(request)
    assert initial["core_sha256"] == item["core_sha256"]
    assert initial["driver_sha256"] == sha(__file__)
    retained, receipt, sources = prepare_sources(item, out, transport, allow_download=False)
    tag = expected_tag(item, sources)
    assert initial["actual_configuration"] == tag
    core = None
    if "core-receipt.json" in entries:
        assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        core = read(out / "core-receipt.json")
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    mathematical = {}
    for name in entries:
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        data = read(out / name)
        assert data["result"] == RESULT and data["configuration"] == tag
        assert data["complete"] is (name != "R860-current.json.gz")
        mathematical[name] = data
    if FINAL not in entries:
        assert run["complete"] is False
        print("R860_VERIFY=partial_atomic_stages_preserved", flush=True)
        return 0
    final = read(out / FINAL)
    assert final["result"] == RESULT and final["configuration"] == tag
    if core is not None:
        assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    if not final["complete"]:
        assert run["complete"] is False
        print("R860_VERIFY=honest_partial_expression_scope", flush=True)
        return 0
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert core is not None and core["complete"] is True
    assert core["process_exit_code"] == 0 and core["error"] is None
    for key in ("expanded_bivariate_cofactors_computed", "expanded_power_basis_coordinates_computed",
                "actual_RR_kernel_connection_period_or_height_computed",
                "characteristic_zero_Krylov_matrix_or_inverse_computed",
                "new_full_normal_semilinear_matrix_computed", "old_mathematical_source_arithmetic_recomputed"):
        assert final[key] is False
    assert final["exact_original_semilinear_fraction_DAG_constructed"] is True
    assert final["original_delta_and_nu_fixed_descent_source_bound"] is True
    assert final["actual_original_W_group_count"] == 34
    assert final["original_target_normal_basis_index"] == 72
    audit = read(bound(out, final["source_audit"]))
    assert audit["source_identities"] == tag["sources"]
    assert audit["full_original_selected_member_count"] == 61
    assert audit["old_W_S3_cyclic_and_three_conjugates_recomputed"] is False
    index = read(bound(out, final["coefficient_source_index"]))
    assert index["source_audit"] == final["source_audit"]
    assert index["source_group_checks"] == final["completed_original_W_group_checks"]
    assert index["normal_basis_rank"] == 272 and index["normal_basis_degrees"] == EPS
    assert index["matrix_convention"] == "row_output_column_input"
    assert index["coefficient_rule"]["additional_scale"] == [1, 1]
    assert len(index["source_exact_coordinate_groups"]) == 34
    for k, entry in enumerate(index["source_group_checks"]):
        data = read(bound(out, entry))
        assert data["group"] == k and data["source_original_group"] == index["source_exact_coordinate_groups"][k]
        assert sources["R806"]["files"][data["source_original_group"]["file"]] == data["source_original_group"]
        assert data["all_weighted_forced_zero_positions_checked"] is True
        assert data["original_full820_certificate_consumed_not_recomputed"] is True
        assert data["original_scale_reapplied"] is False
    dag = read(bound(out, final["exact_expression_DAG"]))
    assert dag["coefficient_source_index"] == final["coefficient_source_index"]
    nodes = {}
    for node in dag["nodes"]:
        assert node["id"] not in nodes and all(identifier in nodes for identifier in node["inputs"])
        nodes[node["id"]] = node
    assert all(identifier in nodes for identifier in dag["outputs"].values())
    assert nodes["D_matrix"]["deleted_row"] == nodes["D_matrix"]["deleted_column"] == 0
    assert nodes["N_matrix"]["deleted_row"] == 72 and nodes["N_matrix"]["deleted_column"] == 0
    assert nodes["N_matrix"]["source_adjugate_entry"] == [0, 72]
    assert nodes["N_matrix"]["cofactor_sign"] == 1
    assert nodes["D"]["leading_T_coefficient"] == 1
    assert nodes["D"]["T_degree_bound"] == nodes["D"]["total_degree_bound"] == 271
    assert nodes["N"]["T_degree_bound"] == 270 and nodes["N"]["total_degree_bound"] == 272
    assert nodes["D"]["expanded"] is nodes["N"]["expanded"] is False
    assert nodes["r"]["inputs"] == ["N_at_w", "D_at_w"]
    assert nodes["cY_z"]["inputs"] == ["z", "minus_two_r"]
    assert nodes["minus_two_r"]["scalar"] == -2
    assert dag["nonzero_proofs"][0]["function_field_nonzero_not_every_fiber_unit"] is True
    assert dag["differential_descent"]["FM27_comparison_factor"] == [1, 1]
    assert dag["differential_descent"]["c_Y_nu_equals_nu"] is True
    assert dag["differential_descent"]["c_Y_delta_equals_delta_c_Y"] is True
    assert dag["expanded_power_basis_coordinates_computed"] is False
    assert dag["actual_RR_kernel_connection_period_or_height_computed"] is False
    stages = read(bound(out, final["stage_manifest"]))
    expected = [entries[name] for name in sorted(mathematical)
                if name != "R860-current.json.gz" and not name.startswith("R860-stage-manifest-")]
    assert stages["files"] == expected and stages["actual_complete_stage_count"] == len(expected)
    bound(out, final["resume_state"])
    print("R860_VERIFY=" + json.dumps({"complete": True, "source_members": 61,
          "original_W_groups": 34, "actual_expression_nodes": len(nodes),
          "exact_original_semilinear_fraction_DAG_constructed": True,
          "expanded_bivariate_cofactors_computed": False,
          "actual_RR_kernel_connection_period_or_height_computed": False}, sort_keys=True), flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("compute", "verify"))
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)
    transport = guard(item, args.request)
    code = compute(item, args.output, args.request, transport) if args.mode == "compute" else \
        verify(item, args.output, args.request, transport)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
