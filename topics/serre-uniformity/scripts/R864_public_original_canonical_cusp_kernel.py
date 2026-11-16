#!/usr/bin/env python3
"""R864 standard-library carrier transport and exact cusp-kernel runner.

This module imports only the frozen standard-library R837/Range transport.
The separate core computes the new rational kernel in Actions.
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
REQUEST = TOPIC / "notes/R864-canonical-cusp-kernel-public-request.json"
RESULT = "R864-original-canonical-cusp-kernel"
FINAL = "p41-original-canonical-cusp-kernel-certificate.json"
PREFIX = "R864-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R864-retained-original-inputs.tar.gz"
INVENTORY = "R864-original-source-inventory.json"
INPUT_RECEIPT = "R864-retained-inputs-receipt.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOF_KEYS = ('R805', 'R814', 'R820', 'R860', 'FM')
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
SOURCE_DEFINITIONS = {'R805': {'result': 'R805-original-affine-pencil-free-basis',
          'core_sha256': '730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420',
          'certificate': 'p41-original-affine-pencil-free-basis-certificate.json',
          'count': 7},
 'R820': {'result': 'R820-original-cusp-finite-algebra-and-ideals',
          'core_sha256': '25f5582ed0c6dae2cf29d5eb288469067c09d917bfe1f565fb042978ea9b173c',
          'certificate': 'p41-original-cusp-finite-algebra-ideals-certificate.json',
          'count': 9}}
EPS = [0] + [1] * 144 + [2] * 127
STRATEGY = {'scope': 'complete_original_K_holomorphic_differential_basis',
 'cusp_finite_algebra_degree': 20,
 'domain_dimension': 146,
 'domain_order': '1,z,beta_1,...,beta_144',
 'expected_exact_rank': 19,
 'expected_kernel_dimension': 127,
 'normal_basis_rank': 272,
 'original_sigma_V1_indices': [1, 73],
 'original_sigma_coefficients': [1, 1],
 'original_tau_V1_index': 0,
 'tau_matrix_columns': 'E_0,alpha,E_1,...,E_144',
 'sigma_matrix_columns': 'alpha_inverse,E_0,E_sigma_1,...,E_sigma_144',
 'sigma_regularity_test': 'v*f belongs to original C_sigma',
 'original_nu': '82*tau*dqY/qY',
 'kernel_check_column_block_size': 8,
 'exact_arithmetic': 'Python_Fraction_no_modular_reconstruction',
 'canonical_free_rows_identity': True,
 'original_Q_semilinear_fixed_basis_computed': False,
 'only_transport_resume_budget_directories_excluded_from_mathematical_identity': True}


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
    module_spec = importlib.util.spec_from_file_location("R864_frozen_R837_transport", path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.load_io(item)
    return module


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R864 runs only in the public repository Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == "R864_original_canonical_cusp_kernel.py"
    assert item["wrapper"] == "R864_public_original_canonical_cusp_kernel.py"
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
    assert item["transport_source"]["type"] == "one_unchanged_original_input_carrier"
    assert item["transport_source"]["original_groups"] == ["R805", "R820"]
    assert item["transport_source"]["actual_carrier_member_count"] == 569
    return load_transport(item)


def selected_names(label, directory):
    certificate = read(directory / SOURCE_DEFINITIONS[label]["certificate"])
    names = {MANIFEST, *META, SOURCE_DEFINITIONS[label]["certificate"]}
    if label == "R805":
        names.update(certificate[key]["file"] for key in ("pencil_stage", "graded_free_basis_stage"))
    else:
        assert label == "R820"
        names.update(certificate[key]["file"] for key in ("original_finite_algebra_interface", "stage_manifest"))
        names.update(value["file"] for value in certificate["two_chart_cusp_ideal_indexes"].values())
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
        if name.endswith(".json.gz"):
            value = read(directory / name)
            assert value["complete"] is True and value["configuration"] == tag, (label, name)
    if label == "R805":
        assert certificate["actual_pencil_n"] == 1 and certificate["affine_free_module_rank"] == 272
        assert certificate["graded_free_basis_degrees"] == [1, 144, 127]
    else:
        assert label == "R820"
        assert certificate["normal_basis_rank"] == 272
        assert certificate["normal_basis_degrees"] == EPS
        assert certificate["finite_field_degree"] == 20
        assert certificate["actual_cusp_colengths"] == {"tau": 20, "sigma": 20}
        assert certificate["complete_polynomial_kernels_certified"] is True
        assert certificate["same_original_cusp_field_and_two_chart_transitions_verified"] is True
    return {**identity(source), "certificate": certificate_spec,
            "configuration_sha256": source["configuration_sha256"],
            "selected_files_sha256": fingerprint(files), "files": files}


def cross_source_review(sources, retained):
    c805 = read(retained / "R805" / SOURCE_DEFINITIONS["R805"]["certificate"])
    c820 = read(retained / "R820" / SOURCE_DEFINITIONS["R820"]["certificate"])
    producer = c820["actual_input_producers"]["R805"]
    assert identity(producer) == identity(sources["R805"])
    assert producer["certificate_name"] == sources["R805"]["certificate"]["file"]
    assert producer["certificate_sha256"] == sources["R805"]["certificate"]["sha256"]
    face = read(retained / "R820" / c820["original_finite_algebra_interface"]["file"])
    assert face["all_272_original_two_chart_evaluation_transitions_verified"] is True
    assert face["both_original_nonzero_denominators_inverted_and_fully_multiplied_back"] is True
    assert face["original_common_82_power_cancels_exactly"] == 6


def expected_tag(item, sources):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "arithmetic": "stdlib_exact_rational_cusp_kernel",
        "proofs_sha256": {key: item["proofs"][key]["sha256"] for key in PROOF_KEYS},
        "method_sha256": item["method_sha256"],
        "sources": {key: source_identity(sources[key]) for key in sorted(SOURCE_DEFINITIONS)},
        "normal_basis_degrees": EPS, "strategy": STRATEGY,
    }


def extract_selected_carrier(bundle, members, sources, retained):
    expected = {}
    for group, files in members.items():
        safe_name(group)
        for name, entry in files.items():
            assert safe_name(name) == entry["file"]
            expected[group + "/" + name] = plain(entry)
    for group, source in sources.items():
        (retained / group).mkdir(parents=True, exist_ok=True)
        for name, entry in source["files"].items():
            assert members[group][name] == plain(entry)
    seen, selected = set(), 0
    with tarfile.open(bundle, "r:gz") as archive:
        for entry in archive:
            name = PurePosixPath(entry.name)
            assert entry.isfile() and not name.is_absolute() and len(name.parts) == 2
            assert ".." not in name.parts and entry.name not in seen and entry.name in expected
            seen.add(entry.name)
            reference = expected[entry.name]
            assert entry.size == reference["bytes"]
            group, basename = name.parts
            chosen = group in sources and basename in sources[group]["files"]
            target = retained / group / basename if chosen else None
            temporary = target.with_name(target.name + ".transfer") if chosen else None
            output = temporary.open("wb") if chosen else None
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
            if chosen:
                temporary.replace(target)
                selected += 1
    assert seen == set(expected)
    assert selected == sum(len(source["files"]) for source in sources.values()) == 16
    return len(seen), selected


def download_sources_once(item, retained, out, transport):
    route = item["transport_source"]
    source = route["source"]
    assert route["type"] == "one_unchanged_original_input_carrier"
    assert source["result"] == "R856-original-fixed-branch-ideal-bases"
    metadata = out.parent / "R856-carrier-metadata"
    metadata.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(source, out.parent / "download-R856-carrier", whole=False)
    try:
        archive.extract_bound(MANIFEST, source["manifest_sha256"], metadata / MANIFEST, source["manifest_bytes"])
        manifest = read(metadata / MANIFEST)
        assert manifest["result"] == source["result"]
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name, entry in route["metadata_files"].items():
            assert name == entry["file"] and entries[name] == plain(entry)
        archive.extract_many([(name, entry["sha256"], metadata / name, entry["bytes"])
                              for name, entry in route["metadata_files"].items()])
        initial, run, core = (read(metadata / name) for name in META)
        assert initial["result"] == run["result"] == core["result"] == source["result"]
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert run["error"] is None and core["complete"] is True
        assert run["core_receipt_sha256"] == route["metadata_files"]["core-receipt.json"]["sha256"]
        receipt = read(bound(metadata, route["input_receipt"]))
        inventory = read(bound(metadata, route["source_inventory"]))
        assert inventory["result"] == receipt["result"] == source["result"]
        assert inventory["complete"] is receipt["complete"] is True
        assert plain(receipt["source_inventory"]) == plain(route["source_inventory"])
        members = {group: {name: plain(entry) for name, entry in value["files"].items()}
                   for group, value in inventory["sources"].items()}
        assert set(members) == {"R820", "R805", "R837"}
        for label, original in item["sources"].items():
            assert identity(initial["job"]["sources"][label]) == identity(original)
            assert identity(inventory["sources"][label]) == identity(original)
            assert plain(inventory["sources"][label]["certificate"]) == plain(original["certificate"])
            for name, entry in original["files"].items():
                assert members[label][name] == plain(entry)
        bundle = plain(receipt["source_bundle"])
        assert bundle == plain(route["input_bundle"]) == entries[bundle["file"]]
        assert receipt["minimal_bundle_member_count"] == route["actual_carrier_member_count"] == 569
        archive.extract_bound(bundle["file"], bundle["sha256"], metadata / bundle["file"], bundle["bytes"])
        count, selected = extract_selected_carrier(metadata / bundle["file"], members, item["sources"], retained)
        assert count == 569 and selected == 16
        reviewed = {label: source_review(label, original, retained / label)
                    for label, original in sorted(item["sources"].items())}
        metadata_output = []
        for name in (MANIFEST, *sorted(route["metadata_files"])):
            target = out / ("R864-transport-R856-" + name)
            shutil.copyfile(metadata / name, target)
            metadata_output.append({"original_file": name, "retained_file": file_spec(target)})
        transfer = {"type": route["type"], "carrier_producer": identity(source),
            "input_bundle": bundle, "all_carrier_member_count_and_hashes_verified": count,
            "actual_selected_original_file_count": selected,
            "original_mathematical_producers_preserved": {label: identity(value) for label, value in item["sources"].items()},
            "transport_metadata_original_bytes": metadata_output,
            "range_transport": archive.receipt(), "new_mathematics_executed": False}
        print("R864_SOURCE_CARRIER_COMPLETE=" + json.dumps({"all_members_hashed": count,
              "selected_original_files": selected}, sort_keys=True), flush=True)
        return reviewed, transfer
    finally:
        archive.close()





def prepare_sources(item, out, transport, allow_download=True):
    retained = out.parent / "retained-original-R864"
    retained.mkdir(parents=True, exist_ok=True)
    if all((out / name).exists() for name in (INPUT_RECEIPT, INVENTORY, BUNDLE)):
        receipt, inventory = read(out / INPUT_RECEIPT), read(out / INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is inventory["complete"] is True
        assert receipt["source_mathematical_identities"] == {
            key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)}
        bound(out, receipt["source_inventory"])
        bound(out, receipt["source_bundle"])
        for entry in receipt["range_transport"]["transport_metadata_original_bytes"]:
            assert entry["retained_file"]["file"] == "R864-transport-R856-" + entry["original_file"]
            bound(out, entry["retained_file"])
        count = transport.unpack_sources(out / BUNDLE, retained, inventory)
        reviewed = {key: source_review(key, item["sources"][key], retained / key)
                    for key in sorted(SOURCE_DEFINITIONS)}
        assert reviewed == inventory["sources"]
        assert count == receipt["minimal_bundle_member_count"] == 16
        cross_source_review(reviewed, retained)
        return retained, receipt, reviewed
    assert allow_download, "The exact source carrier is required for verification."
    reviewed, transfer = download_sources_once(item, retained, out, transport)
    cross_source_review(reviewed, retained)
    inventory = {"result": RESULT, "complete": True, "sources": reviewed,
                 "all_original_bytes_preserved": True}
    save(out / INVENTORY, inventory)
    transport.pack_sources(retained, inventory, out / BUNDLE)
    receipt = {"result": RESULT, "complete": True,
        "source_mathematical_identities": {key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)},
        "source_inventory": file_spec(out / INVENTORY), "source_bundle": file_spec(out / BUNDLE),
        "minimal_bundle_member_count": 16, "range_transport": transfer,
        "new_mathematics_executed_in_source_preparation": False}
    save(out / INPUT_RECEIPT, receipt)
    print("R864_INPUT_REVIEW=" + json.dumps(receipt, sort_keys=True), flush=True)
    return retained, receipt, reviewed


def stable_job(item):
    result = {key: value for key, value in item.items()
              if key not in ("resume", "budget_minutes", "rules_last_read_commit", "readme_sha256", "sources", "transport_source")}
    result["sources"] = {key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)}
    return result


def restore(item, out, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    directory = out.parent / "resume-metadata"
    directory.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(resume, out.parent / "download-R864-continuation", whole=False)
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
            if name.startswith("R864-transport-") and name.endswith(".json"):
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
            assert value["complete"] is (name != "R864-current.json.gz")
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
        save(out / "R864-resume-transport-receipt.json", {
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
        print("R864_VERIFY=source_preparation_incomplete", flush=True)
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
        assert data["complete"] is (name != "R864-current.json.gz")
        mathematical[name] = data
    if FINAL not in entries:
        assert run["complete"] is False
        print("R864_VERIFY=partial_atomic_stages_preserved", flush=True)
        return 0
    final = read(out / FINAL)
    assert final["result"] == RESULT and final["configuration"] == tag
    if core is not None:
        assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    if not final["complete"]:
        assert run["complete"] is False
        print("R864_VERIFY=honest_partial_kernel_scope", flush=True)
        return 0
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert core is not None and core["complete"] is True
    assert core["process_exit_code"] == 0 and core["error"] is None
    for key in ("original_Q_semilinear_fixed_basis_computed",
                "original_YP_meromorphic_RR_connections_or_periods_computed",
                "old_W_cusp_ideals_Fourier_or_three_conjugates_recomputed"):
        assert final[key] is False
    assert final["complete_original_K_holomorphic_basis_certified"] is True
    assert final["all20_cusps_and_both_original_charts_verified"] is True
    assert final["actual_cusp_evaluation_rank"] == 19 and final["actual_kernel_dimension"] == 127
    assert core["complete_original_K_holomorphic_basis_certified"] is True
    assert core["actual_cusp_evaluation_rank"] == 19 and core["actual_kernel_dimension"] == 127
    audit = read(bound(out, final["source_audit"]))
    assert audit["source_identities"] == tag["sources"] and audit["selected_original_file_count"] == 16
    assert audit["old_cusp_ideal_or_inverse_or_W_or_Fourier_arithmetic_recomputed"] is False
    matrices = read(bound(out, final["evaluation_matrices"]))
    assert matrices["source_audit"] == final["source_audit"]
    assert matrices["row_count"] == 20 and matrices["column_count"] == 146
    assert set(matrices["matrices"]) == {"tau", "sigma"}
    assert all(len(m) == 20 and all(len(r) == 146 for r in m) for m in matrices["matrices"].values())
    assert matrices["sigma_matrix_evaluates_v_times_tau_function"] is True
    assert matrices["original_82_integer_scales_reinserted"] is False
    rref = read(bound(out, final["rref_certificate"]))
    assert rref["actual_rank"] == 19 and len(rref["pivot_columns"]) == 19
    assert rref["actual_exact_nonzero_minor_determinant"][0] != "0"
    assert len(rref["original_minor_matrix"]) == 19
    assert all(len(r) == 19 for r in rref["original_minor_matrix"])
    assert rref["determinant_equals_original_elimination_pivot_product"] is True
    assert rref["all_remaining_rows_exactly_zero"] is True
    previous = None
    for k in range(19):
        step = mathematical["R864-rref-step-%02d.json.gz" % k]
        assert step["step"] == k and step["previous_step"] == previous
        assert step["source_matrix"] == final["evaluation_matrices"]
        assert len(step["pivot_columns"]) == k + 1
        assert step["all_elimination_operations_exact"] is True
        previous = entries["R864-rref-step-%02d.json.gz" % k]
    assert rref["last_step"] == previous
    kernel = read(bound(out, final["kernel_certificate"]))
    assert kernel["source_rref"] == final["rref_certificate"]
    assert kernel["all_free_rows_identity_verified"] is True
    assert kernel["actual_rank"] == 19 and kernel["kernel_dimension"] == 127
    assert len(kernel["kernel_matrix"]) == 146 and all(len(r) == 127 for r in kernel["kernel_matrix"])
    assert len(kernel["kernel_free_rows"]) == 127
    basis = read(bound(out, final["holomorphic_differential_basis"]))
    assert basis["source_kernel"] == final["kernel_certificate"]
    assert basis["actual_dimension_over_K"] == 127 and len(basis["basis"]) == 127
    for key in ("complete_original_K_holomorphic_basis_certified", "all_original_V1_coordinate_roundtrips_verified",
                "tau_functions_in_complete_original_C_tau", "sigma_v_times_functions_in_complete_original_C_sigma",
                "all_degree_two_normal_rows_zero"):
        assert basis[key] is True
    assert basis["source_rational_coordinates_imply_true_Q_descent"] is False
    assert basis["original_Q_semilinear_fixed_basis_computed"] is False
    assert basis["original_82_power_from_nu_only"] == 1
    assert len(basis["full_two_chart_checks"]) == 16
    expected_checks = []
    for first in range(0, 127, 8):
        stop = min(127, first + 8)
        name = "R864-full-two-chart-check-%03d-%03d.json.gz" % (first, stop)
        value = mathematical[name]
        assert value["source_kernel"] == final["kernel_certificate"]
        assert value["source_matrices"] == final["evaluation_matrices"]
        assert value["first_kernel_column"] == first and value["stop_kernel_column"] == stop
        assert value["full_coordinate_rows_per_chart"] == 20
        assert value["actual_checked_charts"] == ["tau", "sigma"]
        assert value["all_original_entries_exactly_zero"] is True
        expected_checks.append(entries[name])
    assert basis["full_two_chart_checks"] == expected_checks
    for j, row in enumerate(basis["basis"]):
        assert row["basis_index"] == j and len(row["original_V1_coefficients"]) == 146
        for key in ("tau_f_normal_polynomial", "sigma_vf_normal_polynomial"):
            seen = set()
            for term in row[key]:
                i = term["normal_basis_index"]
                assert 0 <= i <= 144 and i not in seen
                seen.add(i)
                assert len(term["polynomial_low_to_high"]) == (2 if i == 0 else 1)
    stages = read(bound(out, final["stage_manifest"]))
    expected = [entries[name] for name in sorted(mathematical)
                if name not in ("R864-current.json.gz", "R864-exact-stages-manifest.json.gz")]
    assert stages["files"] == expected and stages["actual_complete_stage_count"] == len(expected)
    current = read(bound(out, final["resume_state"]))
    assert current["scope_complete"] is True and current["stop_reason"] == "complete"
    assert current["source_mathematical_stage_manifest"] == final["stage_manifest"]
    print("R864_VERIFY=" + json.dumps({"complete": True, "source_members": 16,
        "actual_cusp_evaluation_rank": 19, "actual_K_holomorphic_basis_dimension": 127,
        "original_Q_semilinear_fixed_basis_computed": False}, sort_keys=True), flush=True)
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
