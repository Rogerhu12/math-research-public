#!/usr/bin/env python3
"""R866 standard-library sources and true holomorphic descent runner.

This module imports only the frozen standard-library R837/Range transport.
The separate core computes the new rational descent matrices in Actions.
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
REQUEST = TOPIC / "notes/R866-holomorphic-semilinear-descent-public-request.json"
RESULT = "R866-original-holomorphic-semilinear-descent"
FINAL = "p41-original-holomorphic-semilinear-descent-certificate.json"
PREFIX = "R866-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R866-retained-original-inputs.tar.gz"
INVENTORY = "R866-original-source-inventory.json"
INPUT_RECEIPT = "R866-retained-inputs-receipt.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOF_KEYS = ('R802', 'R853', 'R853_method', 'R860', 'R864')
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
SOURCE_DEFINITIONS = {'R786': {'result': 'R786-exact-original-power5-short-basis',
          'core_sha256': '4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851',
          'count': 152,
          'certificate': 'p41-exact-original-power5-short-basis-certificate.json'},
 'R837': {'result': 'R837-original-fixed-branch-pencil',
          'core_sha256': '5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924',
          'count': 8,
          'certificate': 'p41-original-fixed-branch-pencil-certificate.json'},
 'R853': {'result': 'R853-original-semilinear-V1-generator-conjugates',
          'core_sha256': '5b65e7ccf7c6663949155fdd30abc4c765823e861259c8f9b90b26d0bc1511df',
          'count': 9,
          'certificate': 'p41-original-semilinear-V1-conjugates-certificate.json'},
 'R864': {'result': 'R864-original-canonical-cusp-kernel',
          'core_sha256': '0dfe5d3fde2adfe90c3384266d5d8083ed46221c1b7b96e04030b0c5c2d26ea9',
          'count': 9,
          'certificate': 'p41-original-canonical-cusp-kernel-certificate.json'}}
EPS = [0] + [1] * 144 + [2] * 127
STRATEGY = {'scope': 'original_holomorphic_semilinear_action_and_complete_Q_fixed_basis',
 'original_V1_dimension': 146,
 'holomorphic_dimension': 127,
 'qY_orders': 14,
 'xi_coordinates_per_order': 40,
 'full_original_coordinate_rows': 560,
 'original_section_integer_scale': '6724',
 'differential_coefficient_multiplier_from_H': '82',
 'H_coefficients_of': 'original_F_j_without_rescaling',
 'source_e_i_already_integer_scaled_relative_to_T': '6724',
 'original_row_convention': '40*n+r',
 'coefficient_c0_action': 's_to_minus_s_xi_fixed',
 'geometric_twist_action': 'qY_to_minus_qY_weight2_automorphy_one',
 'new_row_selection_within_old_R837_146_rows': True,
 'exact_inverse_dimension': 127,
 'semilinear_matrix_convention': 'C_times_conjugate_coefficient_column',
 'Q_fixed_column_rule': 'inverse_column_if_even_order_else_inverse_column_over_original_s',
 'original_s_square': -3,
 'matrix_column_block_size': 8,
 'original_V1_e73_conversion_already_applied_by_R864': True,
 'normal_transport_e73_correction': 'subtract_original_V1_coefficient1_once',
 'full146_or272_conjugation_matrix_computed': False,
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
    module_spec = importlib.util.spec_from_file_location("R866_frozen_R837_transport", path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.load_io(item)
    return module


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R866 runs only in the public repository Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == "R866_original_holomorphic_descent.py"
    assert item["wrapper"] == "R866_public_original_holomorphic_descent.py"
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
    assert item["input_carrier"]["source_label"] == "R853"
    assert item["input_carrier"]["original_member_count"] == 169
    assert item["input_carrier"]["selected_original_groups"] == ["R786", "R837"]
    return load_transport(item)


def selected_names(label, directory):
    certificate = read(directory / SOURCE_DEFINITIONS[label]["certificate"])
    names = {MANIFEST, *META, SOURCE_DEFINITIONS[label]["certificate"]}
    if label == "R786":
        names.add(certificate["stages_manifest"]["file"])
        names.update("R786-exact-power-1-row-%04d.json.gz" % i for i in range(146))
    elif label == "R837":
        names.add(certificate["stage_manifest"]["file"])
        names.add("R837-original-V1-reflection-minor.json.gz")
        minor = read(directory / "R837-original-V1-reflection-minor.json.gz")
        names.add(minor["successful_attempt"]["file"])
    elif label == "R853":
        names.update(certificate[key]["file"] for key in
            ("source_audit", "three_conjugate_coordinates", "function_field_action_DAG", "stage_manifest"))
    else:
        assert label == "R864"
        names.update(certificate[key]["file"] for key in
            ("source_audit", "kernel_certificate", "holomorphic_differential_basis", "stage_manifest"))
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
    stage_spec = certificate["stages_manifest"] if label == "R786" else certificate["stage_manifest"]
    stages = read(bound(directory, stage_spec))
    assert stages["complete"] is True and stages["configuration"] == tag
    indexed = {row["file"]: plain(row) for row in stages["files"]}
    assert len(indexed) == len(stages["files"])
    for name in files:
        if name.endswith(".json.gz") and name != stage_spec["file"]:
            assert indexed[name] == files[name]
    if label == "R786":
        assert certificate["exact_power5_basis_dimension"] == 1234
        assert certificate["exact_K_basis_prefix_bound_qY"] == 128
        assert certificate["all_original_R775_mod739_short_series_compared"] is True
    elif label == "R837":
        minor = read(directory / "R837-original-V1-reflection-minor.json.gz")
        attempt = read(bound(directory, minor["successful_attempt"]))
        for key in ("matrix_shape", "actual_modular_rank", "selected_rows", "selected_columns",
                    "prime", "prime_index", "minor_determinant_mod_prime"):
            assert minor[key] == attempt[key]
        assert minor["matrix_shape"] == [560, 146] and minor["actual_modular_rank"] == 146
        assert minor["selected_columns"] == list(range(146)) and minor["minor_determinant_mod_prime"] != 0
    elif label == "R853":
        assert certificate["original_three_V1_conjugates_certified"] is True
        assert certificate["full_original_coordinate_rows"] == 560
    else:
        assert certificate["complete_original_K_holomorphic_basis_certified"] is True
        assert certificate["all20_cusps_and_both_original_charts_verified"] is True
        assert certificate["actual_cusp_evaluation_rank"] == 19 and certificate["actual_kernel_dimension"] == 127
    return {**identity(source), "certificate": certificate_spec,
            "configuration_sha256": source["configuration_sha256"],
            "selected_files_sha256": fingerprint(files), "files": files}


def cross_source_review(sources, retained):
    c853 = read(retained / "R853" / SOURCE_DEFINITIONS["R853"]["certificate"])
    c864 = read(retained / "R864" / SOURCE_DEFINITIONS["R864"]["certificate"])
    for label in ("R786", "R837"):
        old = c853["configuration"]["sources"][label]
        assert identity(old) == identity(sources[label])
        assert old["certificate"] == sources[label]["certificate"]
        assert old["configuration_sha256"] == sources[label]["configuration_sha256"]
    a853 = read(retained / "R853" / c853["source_audit"]["file"])
    a864 = read(retained / "R864" / c864["source_audit"]["file"])
    assert a853["original_normal_free_basis"] == a864["original_free_basis"]
    for row in a853["original_R786_prefix_rows"]:
        assert sources["R786"]["files"][row["file"]] == plain(row)
    assert sources["R837"]["files"][a853["original_reflection_minor"]["file"]] == plain(a853["original_reflection_minor"])


def expected_tag(item, sources):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "python_flint": "0.9.0",
        "proofs_sha256": {key: item["proofs"][key]["sha256"] for key in PROOF_KEYS},
        "method_sha256": item["method_sha256"],
        "sources": {key: source_identity(sources[key]) for key in sorted(SOURCE_DEFINITIONS)},
        "strategy": STRATEGY,
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
    assert selected == sum(len(source["files"]) for source in sources.values()) == 160
    return len(seen), selected


def download_sources_once(item, retained, out, transport):
    route = item["input_carrier"]
    reviewed, transfers = {}, {}
    for label in ("R853", "R864"):
        source = item["sources"][label]
        directory = retained / label
        directory.mkdir(parents=True, exist_ok=True)
        archive = transport.IO.Archive(source, out.parent / ("download-" + label), whole=False)
        try:
            archive.extract_bound(MANIFEST, source["manifest_sha256"], directory / MANIFEST, source["manifest_bytes"])
            manifest = read(directory / MANIFEST)
            assert manifest["result"] == source["result"]
            entries = {row["file"]: plain(row) for row in manifest["files"]}
            assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
            assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
            selected = []
            for name, row in source["files"].items():
                if name == MANIFEST:
                    continue
                assert entries[name] == plain(row)
                selected.append((name, row["sha256"], directory / name, row["bytes"]))
            archive.extract_many(selected)
            reviewed[label] = source_review(label, source, directory)
            if label == "R853":
                metadata = out.parent / "R853-carrier-metadata"
                metadata.mkdir(parents=True, exist_ok=True)
                for reference in (route["source_inventory"], route["input_receipt"], route["input_bundle"]):
                    reference = plain(reference)
                    assert entries[reference["file"]] == reference
                    archive.extract_bound(reference["file"], reference["sha256"], metadata / reference["file"], reference["bytes"])
                inventory = read(bound(metadata, route["source_inventory"]))
                receipt = read(bound(metadata, route["input_receipt"]))
                assert inventory["result"] == receipt["result"] == source["result"]
                assert inventory["complete"] is receipt["complete"] is True
                assert plain(receipt["source_inventory"]) == plain(route["source_inventory"])
                assert plain(receipt["source_bundle"]) == plain(route["input_bundle"])
                assert receipt["minimal_bundle_member_count"] == route["original_member_count"] == 169
                members = {group: {name: plain(value) for name, value in record["files"].items()}
                           for group, record in inventory["sources"].items()}
                assert set(members) == {"R786", "R806", "R837"}
                chosen_sources = {k: item["sources"][k] for k in route["selected_original_groups"]}
                for group, original in chosen_sources.items():
                    assert identity(inventory["sources"][group]) == identity(original)
                    assert inventory["sources"][group]["certificate"] == original["certificate"]
                    assert members[group] == original["files"]
                count, kept = extract_selected_carrier(metadata / route["input_bundle"]["file"], members, chosen_sources, retained)
                assert count == 169 and kept == 160
                for group, original in chosen_sources.items():
                    reviewed[group] = source_review(group, original, retained / group)
                metadata_output = []
                for reference in (route["source_inventory"], route["input_receipt"]):
                    name = reference["file"]
                    target = out / ("R866-transport-R853-" + name)
                    shutil.copyfile(metadata / name, target)
                    metadata_output.append({"original_file": name, "retained_file": file_spec(target)})
                transfers["original_R853_carrier"] = {"carrier_producer": identity(source),
                    "input_bundle": plain(route["input_bundle"]), "original_member_count_hashed": 169,
                    "selected_original_member_count": 160,
                    "transport_metadata_original_bytes": metadata_output,
                    "unchanged_original_producers": {k: identity(v) for k, v in chosen_sources.items()}}
            transfers[label] = archive.receipt()
        finally:
            archive.close()
    assert sum(len(v["files"]) for v in reviewed.values()) == 178
    cross_source_review(reviewed, retained)
    return reviewed, transfers





def prepare_sources(item, out, transport, allow_download=True):
    retained = out.parent / "retained-original-R866"
    retained.mkdir(parents=True, exist_ok=True)
    if all((out / name).exists() for name in (INPUT_RECEIPT, INVENTORY, BUNDLE)):
        receipt, inventory = read(out / INPUT_RECEIPT), read(out / INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is inventory["complete"] is True
        assert receipt["source_mathematical_identities"] == {
            key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)}
        bound(out, receipt["source_inventory"])
        bound(out, receipt["source_bundle"])
        for entry in receipt["range_transport"]["original_R853_carrier"]["transport_metadata_original_bytes"]:
            assert entry["retained_file"]["file"] == "R866-transport-R853-" + entry["original_file"]
            bound(out, entry["retained_file"])
        count = transport.unpack_sources(out / BUNDLE, retained, inventory)
        reviewed = {key: source_review(key, item["sources"][key], retained / key)
                    for key in sorted(SOURCE_DEFINITIONS)}
        assert reviewed == inventory["sources"]
        assert count == receipt["minimal_bundle_member_count"] == 178
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
        "minimal_bundle_member_count": 178, "range_transport": transfer,
        "new_mathematics_executed_in_source_preparation": False}
    save(out / INPUT_RECEIPT, receipt)
    print("R866_INPUT_REVIEW=" + json.dumps(receipt, sort_keys=True), flush=True)
    return retained, receipt, reviewed


def stable_job(item):
    result = {key: value for key, value in item.items()
              if key not in ("resume", "budget_minutes", "rules_last_read_commit", "readme_sha256", "sources", "input_carrier")}
    result["sources"] = {key: source_identity(item["sources"][key]) for key in sorted(SOURCE_DEFINITIONS)}
    return result


def restore(item, out, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    directory = out.parent / "resume-metadata"
    directory.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(resume, out.parent / "download-R866-continuation", whole=False)
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
            if name.startswith("R866-transport-") and name.endswith(".json"):
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
            assert value["complete"] is (name != "R866-current.json.gz")
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
        save(out / "R866-resume-transport-receipt.json", {
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
        if code == 0:
            code = 1
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
        print("R866_VERIFY=source_preparation_incomplete", flush=True)
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
        assert data["complete"] is (name != "R866-current.json.gz")
        mathematical[name] = data
    if FINAL not in entries:
        assert run["complete"] is False
        print("R866_VERIFY=partial_atomic_stages_preserved", flush=True)
        return 0
    final = read(out / FINAL)
    assert final["result"] == RESULT and final["configuration"] == tag
    if core is not None:
        assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    if not final["complete"]:
        assert run["complete"] is False
        print("R866_VERIFY=honest_partial_kernel_scope", flush=True)
        return 0
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert core is not None and core["complete"] is True
    assert core["process_exit_code"] == 0 and core["error"] is None
    for key in ("connection_period_Hecke_or_height_computed", "full146_or272_conjugation_matrix_computed", "old_source_mathematics_recomputed"):
        assert final[key] is False
    assert final["complete_original_Q_holomorphic_basis_certified"] is True
    assert final["actual_original_c_Y_semilinear_action_certified"] is True
    assert final["actual_holomorphic_dimension"] == 127 and final["full_original_Fourier_coordinate_rows"] == 560
    assert core["complete_original_Q_holomorphic_basis_certified"] is True
    assert core["actual_original_c_Y_semilinear_action_certified"] is True
    audit = read(bound(out, final["source_audit"]))
    assert audit["source_identities"] == tag["sources"]
    assert audit["e73_original_V1_conversion_reapplied"] is False
    assert audit["coefficient_c0_fixes_all_integer_xi_coordinates"] is True
    H = read(bound(out, final["holomorphic_Fourier_matrix"]))
    assert H["source_audit"] == final["source_audit"] and H["matrix_shape"] == [560, 127]
    assert len(H["matrix_rational_num_den"]) == 560 and all(len(r) == 127 for r in H["matrix_rational_num_den"])
    assert H["matrix_integer_scale"] == "6724" and H["differential_coefficients_equal_matrix_times_82"] is True
    assert H["new_scale_relative_to_original_e_i_coefficients"] == [1, 1]
    assert H["all40_constant_coefficients_exactly_zero"] is True
    assert len(H["order_blocks"]) == 14
    for n, reference in enumerate(H["order_blocks"]):
        block = read(bound(out, reference))
        assert block["qY_order"] == n and block["matrix_shape"] == [40, 127]
        assert block["original_section_integer_scale"] == "6724"
        assert block["rational_coefficients_c0_fixed"] is True
    inverse = read(bound(out, final["selected_exact_inverse"]))
    selection = read(bound(out, inverse["source_row_selection"]))
    assert inverse["source_H"] == final["holomorphic_Fourier_matrix"]
    assert inverse["both_exact_inverse_products_verified"] is True
    assert inverse["actual_exact_minor_determinant"][0] != "0"
    assert inverse["matrix_shape"] == [127, 127]
    rows = inverse["selected_rows"]
    assert rows == selection["selected_rows"] and len(rows) == len(set(rows)) == 127
    assert all(40 <= r < 560 and r in audit["old_selected_rows"] for r in rows)
    assert len(inverse["inverse"]) == 127 and all(len(r) == 127 for r in inverse["inverse"])
    assert inverse["section_integer_scale"] == "6724" and inverse["full_original_row_numbers_not_compressed"] is True
    action = read(bound(out, final["semilinear_action"]))
    assert action["source_H"] == final["holomorphic_Fourier_matrix"]
    assert action["source_inverse"] == final["selected_exact_inverse"]
    assert action["matrix_shape"] == [127, 127]
    assert action["actual_involution_square_verified"] is True
    assert action["all560_times127_original_coordinates_verified"] is True
    assert action["coefficient_action"] == "C*bar(x), bar(s)=-s"
    assert action["actual_even_selected_row_count"] + action["actual_odd_selected_row_count"] == 127
    assert action["full146_or272_conjugation_matrix_computed"] is False
    basis = read(bound(out, final["Q_fixed_holomorphic_basis"]))
    assert basis["source_inverse"] == final["selected_exact_inverse"]
    assert basis["source_semilinear_action"] == final["semilinear_action"]
    assert basis["dimension_over_Q"] == 127
    for key in ("complete_original_Q_holomorphic_basis_certified", "all127_vectors_fixed_by_actual_c_Y",
                "independence_and_completeness_from_invertible_Qinv_times_nonzero_diagonal", "original_tau_and_nu_fixed_norms_preserved"):
        assert basis[key] is True
    assert basis["connection_period_Hecke_or_height_computed"] is False
    assert len(action["column_blocks"]) == len(basis["basis_column_blocks"]) == 16
    for block_number, first in enumerate(range(0, 127, 8)):
        stop = min(127, first + 8)
        block = read(bound(out, action["column_blocks"][block_number]))
        assert block["first_column"] == first and block["stop_column"] == stop
        assert block["full560_original_coordinate_rows_verified"] is True
        fixed = read(bound(out, basis["basis_column_blocks"][block_number]))
        assert fixed["first_column"] == first and fixed["stop_column"] == stop
        assert fixed["K_basis"] == ["1", "s"] and fixed["s_square"] == -3
        for key in ("C_times_conjugate_P_equals_P_verified", "all560_original_fixed_expansion_rows_verified",
                    "all_original_V1_normal_roundtrips_verified"):
            assert fixed[key] is True
        assert len(fixed["basis_columns"]) == stop-first
        for j, column in enumerate(fixed["basis_columns"], first):
            assert column["Q_basis_index"] == j and column["selected_original_row"] == rows[j]
            assert column["selected_qY_order"] == rows[j] // 40
            assert len(column["original_V1_coefficients_in_1_s_basis"]) == 146
            expected_scalar = [[1, 1], [0, 1]] if (rows[j] // 40) % 2 == 0 else [[0, 1], [-1, 3]]
            assert column["selected_scalar_in_original_1_s_basis"] == expected_scalar
    stages = read(bound(out, final["stage_manifest"]))
    expected = [entries[name] for name in sorted(mathematical)
                if name not in ("R866-current.json.gz", "R866-exact-stages-manifest.json.gz")]
    assert stages["files"] == expected and stages["actual_complete_stage_count"] == len(expected)
    current = read(bound(out, final["resume_state"]))
    assert current["scope_complete"] is True and current["source_stage_manifest"] == final["stage_manifest"]
    print("R866_VERIFY=" + json.dumps({"complete": True, "source_members": 178,
        "actual_holomorphic_dimension": 127, "full_original_rows": 560,
        "complete_original_Q_holomorphic_basis_certified": True}, sort_keys=True), flush=True)
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
