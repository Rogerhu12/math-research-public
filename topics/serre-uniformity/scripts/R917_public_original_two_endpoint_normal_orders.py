#!/usr/bin/env python3
"""Standard-library source transport and continuation for the two original endpoint orders."""
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

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R917-original-two-endpoint-normal-orders-public-request.json"
RESULT = "R917-original-two-endpoint-normal-orders"
FINAL = "p41-original-two-endpoint-normal-orders-certificate.json"
PREFIX = "R917-endpoint-"
CURRENT = PREFIX + "current.json.gz"
INVENTORY = PREFIX + "stage-manifest.json.gz"
PRIME, ZETA, SROOT = 1000000753, 549966761, 99932770
COUNT, LEAVES, BLOCK = 273, 146, 64
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
SOURCES = ("R873", "R882", "R807", "R883", "R914")
PROOFS = ("R912", "R917", "R873", "R882", "R883", "R914", "R860")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
H64 = re.compile(r"[0-9a-f]{64}")
DEFINITIONS = {
    "R873": ("R873-original-cyclic-seven-correspondence",
        "3c4922ee5b83d82123d234df47e67f82d7c8032f1152c6cf14df34622101918c"),
    "R882": ("R882-original-cyclic-seven-common-place-coefficients",
        "901466ae4d34bf1b558132a3b7c57c1c0bf6f2a8f097bc2283cd562607ba2e0f"),
    "R807": ("R807-original-M6-pole-clearing",
        "d92cf79bb3a30fe8e28709a4e2eaa706a724e195c8d8393e7649466a79cec018"),
    "R883": ("R883-original-t-first-order-frame",
        "2778a81b5639a1eb6285718574af0ce4b48b00e92b648c6ac29ffe70c1da66f7"),
    "R914": ("R914-original-full-V1-involution-and-P1-local-jets",
        "c7dded45af13c7cd37b9c5261d917c2e81d3c179debe963296bbd8caf746e004"),
}
STRATEGY = {
    "scope": "two_original_rank8_normal_orders_and_primitive_t_frames_only",
    "original_curve": "Y with original minus3 descent; no replacement twist",
    "original_auxiliary_prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
    "rank": 8, "geometric_special_fibre_lengths": [1, 1, 3, 3],
    "normal_order_discriminant_order": 4,
    "endpoint_parameters": ["rho0=z-z0", "rho1=iota^*rho0=z-2*beta72-z0"],
    "input_leaf_jet_count": COUNT, "original_V1_dimension": LEAVES,
    "original_ei_scale_already_in_source": "6724", "new_scale_applied": "1",
    "coefficient_order": "P0..P8,K0..K7",
    "common_clear": "Ptilde=theta0^2*P; Ktilde=theta0^2*K; theta0=theta/tau",
    "regular_coefficient_weight": 10,
    "initial_integrality": "Theta=rho^h*U; minimal nonnegative h from actual coefficient valuations",
    "initial_uniform_precision": "input_N-vrho(Ptilde8) after integral numerator deflation",
    "order_enlargement": "End_O(radical(rho O)) via full four-block conditions at orders0,1",
    "each_enlargement_uniform_precision_loss": 2,
    "discriminant_algorithm": "division-free Berkowitz over the complete truncated series ring",
    "basis_convention": "columns in original Theta power basis; exact Laurent polynomial inverse retained",
    "stop_rule": "actual complete integral table and actual discriminant order4",
    "old_P0_theta_A_first3_values_copied": True,
    "monomial_block_size": BLOCK,
    "all_factors_nilpotents_and_original_P_K_preserved": True,
    "source_target_direction": "original Nm_pi_t(pi_s^*I), transported by canonical dual7 on both determinants",
    "exact_nu": "82*tau*dqY/qY; iota fixes nu",
    "t_frame": "t-epsilon=c_epsilon*rho_epsilon+...; c1=-c0; leading multiplies c_epsilon^(-order)",
    "characteristic_zero_order_basis_expanded": False,
    "target272_coordinates_or_target_Norm_frames_computed": False,
    "only_budget_enlargement_limit_and_transport_paths_excluded_from_identity": True,
}

STAGES = INVENTORY
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R917-retained-original-inputs.tar.gz"
INVENTORY = "R917-original-source-inventory.json"
INPUT_RECEIPT = "R917-retained-inputs-receipt.json"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
SOURCE_COUNTS = {"R873": 7, "R882": 8, "R807": 7, "R883": 7, "R914": 11}
FINALS = {
    "R873": "p41-original-cyclic-seven-correspondence-certificate.json",
    "R882": "p41-original-cyclic-seven-common-place-coefficients-certificate.json",
    "R807": "p41-original-M6-pole-clearing-certificate.json",
    "R883": "p41-original-t-first-order-frame-certificate.json",
    "R914": "p41-original-full-V1-involution-and-P1-jets-certificate.json",
}

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)

def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False).encode()).hexdigest()

def plain(value):
    answer = {k: value[k] for k in ("file", "bytes", "sha256")}
    assert isinstance(answer["file"], str) and Path(answer["file"]).name == answer["file"]
    assert "\\" not in answer["file"] and answer["file"] not in (".", "..")
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer

def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}

def bound(folder, value):
    value = plain(value)
    path = Path(folder) / value["file"]
    assert spec(path) == value, str(path)
    return path

def identity(value):
    return {k: str(value[k]) for k in BASE}

def source_identity(value):
    return {**identity(value),
            "configuration_sha256": value["configuration_sha256"],
            "selected_files_sha256": value["selected_files_sha256"],
            "selected_file_count": value["selected_file_count"],
            "certificate": plain(value["certificate"])}

def topic_path(name):
    p = PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path = (TOPIC / str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def load_module(name, path, expected):
    assert sha(path) == expected
    loader = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module

def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"],
        "helper_sha256": item["helper_sha256"], "p": 41, "prime": PRIME,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
        "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "inputs": item["inputs"], "strategy": STRATEGY}

def guard(item):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["future_target_sources"] == {"R903": None, "R907": None}
    assert item["core"] == "R917_original_two_endpoint_normal_orders.py"
    assert item["helper"] == "R917_endpoint_order_arithmetic.py"
    assert item["wrapper"] == Path(__file__).name
    assert sha(HERE / item["core"]) == item["core_sha256"]
    assert sha(HERE / item["helper"]) == item["helper_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300 and item["maximum_enlargement_steps"] >= 1
    assert sha(REPO / "README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC / "README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(SOURCES)
    assert set(item["proofs"]) == set(PROOFS)
    for row in item["proofs"].values():
        assert sha(topic_path(row["file"])) == row["sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    for label, source in item["sources"].items():
        assert (source["result"], source["core_sha256"]) == DEFINITIONS[label]
        assert plain(source["certificate"])["file"] == FINALS[label]
        assert source["selected_file_count"] == SOURCE_COUNTS[label]
        assert H64.fullmatch(source["configuration_sha256"])
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
        files = {name: plain(row) for name, row in source["files"].items()}
        assert len(files) == source["selected_file_count"]
        assert fingerprint(files) == source["selected_files_sha256"]
        assert {MANIFEST, *META, FINALS[label]} <= set(files)
        assert all(name == row["file"] for name, row in files.items())
    for key, row in item["inputs"].items():
        source = item["sources"][row["source_group"]]
        assert source["files"][row["file"]] == plain(row), key
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    assert item["transport_helper"] == "R837_original_branch_pencil_public.py"
    assert item["transport_helper_sha256"] == TRANSPORT_SHA
    io_module = load_module("R917_original_frozen_Range_IO", HERE / item["io_helper"], RANGE_SHA)
    transport = load_module("R917_original_frozen_file_transport", HERE / item["transport_helper"], TRANSPORT_SHA)
    return io_module, transport


def fetch_archive_files(io_module, source, names, folder, work):
    folder.mkdir(parents=True, exist_ok=True)
    archive = io_module.Archive(source, work, whole=False)
    try:
        mp = folder / MANIFEST
        if not mp.exists():
            archive.extract_bound(MANIFEST, source["manifest_sha256"], mp, source["manifest_bytes"])
        assert mp.stat().st_size == source["manifest_bytes"] and sha(mp) == source["manifest_sha256"]
        manifest = read(mp)
        assert manifest["result"] == source["result"]
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name, row in entries.items():
            assert len(archive.by_name[name]) == 1 and archive.by_name[name][0].file_size == row["bytes"]
        assert set(names) - {MANIFEST} <= set(entries)
        todo = []
        for name in names:
            if name == MANIFEST:
                continue
            row = entries[name]
            if (folder / name).exists():
                bound(folder, row)
            else:
                todo.append((name, row["sha256"], folder / name, row["bytes"]))
        archive.extract_many(todo)
        return {name: (spec(mp) if name == MANIFEST else entries[name]) for name in sorted(names)}, archive.receipt()
    finally:
        archive.close()

def verify_transport_metadata(source, folder, selected):
    initial, run, core = [read(folder / n) for n in META]
    assert initial["result"] == run["result"] == core["result"] == source["result"]
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and run.get("error") is None
    assert core["complete"] is True
    assert run["core_receipt_sha256"] == selected["core-receipt.json"]["sha256"]

def review_source(label, source, folder):
    files = {name: plain(row) for name, row in source["files"].items()}
    mp = folder / MANIFEST
    assert mp.stat().st_size == source["manifest_bytes"] and sha(mp) == source["manifest_sha256"]
    manifest = read(mp)
    assert manifest["result"] == source["result"]
    all_files = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(all_files) == len(manifest["files"]) == source["manifest_file_count"]
    assert len(files) == source["selected_file_count"] == SOURCE_COUNTS[label]
    assert fingerprint(files) == source["selected_files_sha256"]
    for name, row in files.items():
        assert row == (spec(mp) if name == MANIFEST else all_files[name])
        bound(folder, row)
    verify_transport_metadata(source, folder, files)
    cert = read(bound(folder, source["certificate"]))
    core = read(folder / "core-receipt.json")
    assert cert["result"] == source["result"] and cert["complete"] is True
    assert core["certificate_sha256"] == source["certificate"]["sha256"]
    tag = cert["configuration"]
    assert tag["result"] == source["result"] and tag["source_sha256"] == source["core_sha256"]
    assert fingerprint(tag) == source["configuration_sha256"]
    for name in files:
        if name.endswith(".json.gz"):
            value = read(folder / name)
            assert value["complete"] is True and value["configuration"] == tag
            assert value.get("result", tag["result"]) == source["result"]
    return {**source_identity(source), "files": files}


def extract_carried_R807(item, folder, retained, selected):
    contract = item["R807_transport"]
    source = item["sources"]["R807"]
    assert contract["source_group"] == "R883"
    for key in ("bundle", "inventory", "receipt"):
        assert selected[contract[key]["file"]] == plain(contract[key])
    inventory = read(bound(folder, contract["inventory"]))
    receipt = read(bound(folder, contract["receipt"]))
    assert inventory["result"] == receipt["result"] == item["sources"]["R883"]["result"]
    assert receipt["complete"] is True
    assert receipt["all_original_members_and_producer_identities_verified"] is True
    assert plain(receipt["source_inventory"]) == plain(contract["inventory"])
    assert plain(receipt["intake"]["bundles"]["R807"]) == plain(contract["bundle"])
    original = inventory["sources"]["R807"]
    assert identity(original["identity"]) == identity(source)
    assert original["configuration_sha256"] == source["configuration_sha256"]
    assert plain(original["certificate"]) == plain(source["certificate"])
    wanted = {"original/" + name: plain(row) for name, row in original["files"].items()}
    assert len(wanted) == contract["actual_original_carrier_member_count"]
    keep = source["files"]
    assert set(keep) <= set(original["files"])
    for name, row in keep.items():
        assert plain(row) == plain(original["files"][name])
    seen = set()
    destdir = retained / "R807"
    destdir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bound(folder, contract["bundle"]), "r:gz") as tar:
        for member in tar:
            path = PurePosixPath(member.name)
            assert member.isfile() and not member.issym() and not member.islnk()
            assert not path.is_absolute() and ".." not in path.parts
            assert len(path.parts) == 2 and path.parts[0] == "original"
            assert member.name in wanted and member.name not in seen
            seen.add(member.name)
            row = wanted[member.name]
            assert member.size == row["bytes"]
            preserve = path.name in keep
            target = destdir / path.name
            temporary = target.with_name(target.name + ".tmp")
            output = temporary.open("wb") if preserve else None
            h, count = hashlib.sha256(), 0
            with tar.extractfile(member) as stream:
                try:
                    for block in iter(lambda: stream.read(1048576), b""):
                        h.update(block); count += len(block)
                        if output is not None:
                            output.write(block)
                finally:
                    if output is not None:
                        output.close()
            assert count == row["bytes"] and h.hexdigest() == row["sha256"], member.name
            if preserve:
                if target.exists():
                    bound(destdir, row); temporary.unlink()
                else:
                    temporary.replace(target)
    assert seen == set(wanted)
    return {"source_group": "R883", "original_producer": identity(source),
        "historical_transport_only": True, "original_bundle": plain(contract["bundle"]),
        "original_inventory": plain(contract["inventory"]), "original_receipt": plain(contract["receipt"]),
        "verified_original_tar_members": len(seen), "preserved_original_files": len(keep),
        "all_live_mathematical_sources_preserved_in_new_selected_bundle": True,
        "original_source_bytes_or_tags_modified": False, "mathematics_executed": False}


def prepare_sources(item, out, io_module, transport, allow_download=True):
    retained = out.parent / "R917-retained-original"
    retained.mkdir(parents=True, exist_ok=True)
    expected_count = sum(SOURCE_COUNTS.values())
    if all((out / n).exists() for n in (BUNDLE, INVENTORY, INPUT_RECEIPT)):
        receipt, inventory = read(out / INPUT_RECEIPT), read(out / INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is True and inventory["complete"] is True
        assert receipt["mathematical_source_bindings"] == {k: source_identity(item["sources"][k]) for k in SOURCES}
        bound(out, receipt["source_bundle"]); bound(out, receipt["source_inventory"])
        count = transport.unpack_sources(out / BUNDLE, retained, inventory)
        reviewed = {k: review_source(k, item["sources"][k], retained / k) for k in SOURCES}
        assert reviewed == inventory["sources"]
        assert count == receipt["actual_selected_original_file_count"] == expected_count
        return retained, reviewed, receipt
    assert allow_download, "A complete selected original source carrier is required for output review."
    routes = {}
    for label in ("R873", "R882", "R883", "R914"):
        print("R917_SOURCE_START=" + label, flush=True)
        source = item["sources"][label]
        names = set(source["files"])
        if label == "R883":
            names.update(item["R807_transport"][key]["file"] for key in ("bundle", "inventory", "receipt"))
        selected, route = fetch_archive_files(io_module, source, sorted(names), retained / label,
                                               out.parent / ("R917-download-" + label))
        for name, row in source["files"].items():
            assert selected[name] == plain(row)
        routes[label] = route
        if label == "R883":
            verify_transport_metadata(source, retained / label, selected)
            routes["R807_via_R883"] = extract_carried_R807(item, retained / label, retained, selected)
    reviewed = {k: review_source(k, item["sources"][k], retained / k) for k in SOURCES}
    inventory = {"result": RESULT, "complete": True, "sources": reviewed,
        "all_entries_are_unchanged_completed_original_source_bytes": True}
    save(out / INVENTORY, inventory)
    transport.pack_sources(retained, inventory, out / BUNDLE)
    count = sum(len(v["files"]) for v in reviewed.values())
    assert count == expected_count
    receipt = {"result": RESULT, "complete": True,
        "mathematical_source_bindings": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "source_bundle": spec(out / BUNDLE), "source_inventory": spec(out / INVENTORY),
        "actual_selected_original_file_count": count, "actual_original_source_groups": list(SOURCES),
        "transport_routes": routes, "all_live_mathematical_inputs_are_in_selected_bundle": True,
        "old_V1_action_P0_P1_jets_P_K_coordinates_or_2058_inverse_recomputed": False,
        "new_mathematics_executed_in_source_preparation": False}
    save(out / INPUT_RECEIPT, receipt)
    print("R917_SOURCE_IO_COMPLETE=" + json.dumps({"source_bundle": receipt["source_bundle"],
        "source_inventory": receipt["source_inventory"], "actual_selected_original_file_count": count,
        "mathematics_executed": False}, sort_keys=True), flush=True)
    return retained, reviewed, receipt


def stable_math(item):
    return expected_tag(item)


def restore(item, out, io_module, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    meta = out.parent / "R917-resume-original-metadata"
    meta.mkdir(parents=True, exist_ok=True)
    archive = io_module.Archive(resume, out.parent / "R917-download-resume", whole=False)
    try:
        archive.extract_bound(MANIFEST, resume["manifest_sha256"], meta / MANIFEST, resume["manifest_bytes"])
        manifest = read(meta / MANIFEST)
        assert manifest["result"] == RESULT
        entries = {x["file"]: plain(x) for x in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == resume["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        needed = [META[0], META[1], BUNDLE, INVENTORY, INPUT_RECEIPT]
        if META[2] in entries:
            needed.append(META[2])
        archive.extract_many([(n, entries[n]["sha256"], (out if n in (BUNDLE, INVENTORY, INPUT_RECEIPT) else meta) / n,
                               entries[n]["bytes"]) for n in needed])
        initial, run = read(meta / META[0]), read(meta / META[1])
        assert initial["result"] == run["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == resume["source_commit"]
        assert str(run["workflow_run_id"]) == str(resume["run_id"])
        assert initial["core_sha256"] == item["core_sha256"]
        assert stable_math(initial["job"]) == stable_math(item)
        assert run["process_exit_code"] in resume["accepted_process_exit_codes"]
        core = None
        if META[2] in entries:
            core = read(meta / META[2])
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries[META[2]]["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        unused, reviewed, receipt = prepare_sources(item, out, io_module, transport, allow_download=False)
        tag = expected_tag(item)
        names = sorted(n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz"))
        archive.extract_many([(n, entries[n]["sha256"], out / n, entries[n]["bytes"]) for n in names])
        for name in names:
            value = read(out / name)
            assert value["result"] == RESULT and value["configuration"] == tag
            assert value["complete"] is (name != CURRENT)
        restored_success = False
        if FINAL in entries:
            row = entries[FINAL]
            archive.extract_bound(FINAL, row["sha256"], meta / FINAL, row["bytes"])
            final = read(meta / FINAL)
            assert final["result"] == RESULT and final["configuration"] == tag
            if final["complete"] is True:
                assert core is not None and core["complete"] is True
                assert run["complete"] is True and run["process_exit_code"] == 0
                assert core["certificate_sha256"] == row["sha256"]
                bound(out, final["stage_manifest"])
                for stage in read(out / final["stage_manifest"]["file"])["files"]:
                    bound(out, stage)
                shutil.copyfile(meta / FINAL, out / FINAL)
                restored_success = True
        save(out / "resume-inheritance-receipt.json", {"result": RESULT, "complete": True,
            "source_resume": resume, "source_manifest": spec(meta / MANIFEST),
            "restored_complete_and_current_files": [entries[n] for n in names],
            "restored_true_final": restored_success,
            "false_final_not_used_as_a_completion_or_stale_current_SHA_constraint": True,
            "range_transport": archive.receipt(), "mathematics_reexecuted_by_wrapper": False})
    finally:
        archive.close()

def write_manifest(out):
    entries = [dict(spec(p), included_in_git=False) for p in sorted(out.iterdir())
               if p.is_file() and p.name not in (MANIFEST, REFERENCE)
               and not p.name.endswith((".tmp", ".download", ".partial"))]
    save(out / MANIFEST, {"result": RESULT, "files": entries,
        "temporary_active_checkpoint_retention_days": 1, "reproducible_data_in_git_or_release": False})
    save(out / REFERENCE, {"result": RESULT, "manifest_file": MANIFEST,
        "manifest_sha256": sha(out / MANIFEST), "manifest_bytes": (out / MANIFEST).stat().st_size,
        "file_count": len(entries)})

def compute(item, out, io_module, transport):
    out.mkdir(parents=True, exist_ok=True)
    code, error, outer_timeout, proc = 1, None, False, None
    try:
        restore(item, out, io_module, transport)
        retained, sources, receipt = prepare_sources(item, out, io_module, transport)
        expanded = dict(item)
        expanded["sources"] = {k: dict(item["sources"][k], files=v["files"],
            directory=str((retained / k).resolve())) for k, v in sources.items()}
        expanded["topic_directory"] = str(TOPIC.resolve())
        save(out / "public-actions-expanded-job.json", expanded)
        initial = {"result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
            "source_commit": os.environ["GITHUB_SHA"], "core_sha256": item["core_sha256"],
            "wrapper_sha256": sha(__file__), "request_sha256": sha(REQUEST), "job": item,
            "method_sha256": item["method_sha256"], "proofs": item["proofs"],
            "actual_configuration": expected_tag(item),
            "source_inventory": receipt["source_inventory"], "source_bundle": receipt["source_bundle"],
            "workflow_sha256": sha(REPO / item["workflow"]),
            "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "all_new_mathematics_only_in_separate_public_Actions_core": True}
        save(out / META[0], initial)
        command = [sys.executable, str(HERE / item["core"]), "--config", str(out / "public-actions-expanded-job.json"),
                   "--out", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out / "public-actions-run.log").open("w", encoding="utf-8") as log:
            proc = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = proc.wait(timeout=60 * item["budget_minutes"] + 600)
            except subprocess.TimeoutExpired:
                outer_timeout, code = True, 124
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    proc.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait()
                error = "Actual outer timeout; complete atomic stages retained."
        if (out / "public-actions-run.log").exists():
            with (out / "public-actions-run.log").open("r", encoding="utf-8", errors="replace") as stream:
                for line in stream:
                    print(line, end="", flush=True)
    except BaseException as exc:
        traceback.print_exc()
        error = type(exc).__name__ + ": " + str(exc)
        code = 1
    finally:
        core = read(out / META[2]) if (out / META[2]).exists() else None
        complete = bool(code == 0 and core and core["complete"] is True and (out / FINAL).exists())
        save(out / META[1], {"result": RESULT, "p": 41, "source_commit": os.environ.get("GITHUB_SHA"),
            "workflow_run_id": os.environ.get("GITHUB_RUN_ID"), "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "complete": complete, "process_exit_code": code, "outer_timeout": outer_timeout,
            "error": error, "core_receipt_sha256": sha(out / META[2]) if core else None,
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "execution_environment": "public_GitHub_Actions"})
        write_manifest(out)
    return code

def own(out, row, tag):
    row = plain(row)
    value = read(bound(out, row))
    assert value["result"] == RESULT and value["configuration"] == tag and value["complete"] is True
    return value

def shape(value, dimensions):
    if not dimensions:
        assert isinstance(value, int) and 0 <= value < PRIME
        return
    assert isinstance(value, list) and len(value) == dimensions[0]
    for x in value:
        shape(x, dimensions[1:])


def laurent_shape(value):
    assert isinstance(value, dict) and isinstance(value["lowest_exponent"], int)
    assert value["exact_finite_Laurent_polynomial_over_residue_field"] is True
    assert isinstance(value["coefficients_ascending"], list)
    assert all(isinstance(x, int) and 0 <= x < PRIME for x in value["coefficients_ascending"])


def order_schema(value):
    assert value["rank"] == 8 and value["prime"] == PRIME
    N = value["absolute_rho_precision"]
    assert isinstance(N, int) and N >= 5
    shape(value["multiplication_structure_coefficients"], [8, 8, 8, N])
    shape(value["one_coordinates"], [8, N])
    for key in ("basis_in_primitive_Theta_powers", "primitive_Theta_powers_in_basis"):
        assert len(value[key]) == 8 and all(len(row) == 8 for row in value[key])
        for row in value[key]:
            for entry in row:
                laurent_shape(entry)
    assert value["all_factors_and_nilpotents_retained"] is True
    assert value["expanded_characteristic_zero_order_basis"] is False
    assert isinstance(value["total_index_length"], int) and value["total_index_length"] >= 0
    assert 0 < value["basis_determinant_unit_mod_prime"] < PRIME
    return N


def verify(item, out, io_module, transport):
    manifest = read(out / MANIFEST)
    assert manifest["result"] == RESULT
    entries = {x["file"]: plain(x) for x in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for row in entries.values():
        bound(out, row)
    run = read(out / META[1])
    assert run["result"] == RESULT and str(run["workflow_run_id"]) == str(os.environ["GITHUB_RUN_ID"])
    if META[0] not in entries:
        assert run["complete"] is False and run["process_exit_code"] != 0 and run["core_receipt_sha256"] is None
        print("R917_SOURCE_PREPARATION_FAILED=" + json.dumps(run, sort_keys=True), flush=True)
        return 0
    initial = read(out / META[0])
    assert initial["result"] == RESULT and initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"] and initial["wrapper_sha256"] == item["wrapper_sha256"]
    assert stable_math(initial["job"]) == stable_math(item)
    unused, sources, receipt = prepare_sources(item, out, io_module, transport, allow_download=False)
    tag = expected_tag(item)
    assert initial["actual_configuration"] == tag
    core = read(out / META[2]) if META[2] in entries else None
    if core is not None:
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == entries[META[2]]["sha256"]
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    all_stages = {}
    for name, row in entries.items():
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            value = read(out / name)
            assert value["result"] == RESULT and value["configuration"] == tag
            assert value["complete"] is (name != CURRENT)
            if name not in (CURRENT, STAGES):
                all_stages[name] = row
    final = read(out / FINAL) if FINAL in entries else None
    if final is not None:
        assert final["result"] == RESULT and final["configuration"] == tag
        if core is not None:
            assert core["certificate_sha256"] == entries[FINAL]["sha256"]
        assert final["source_identities"] == tag["sources"]
        assert final["future_target_sources"] == {"R903": None, "R907": None}
        for key in ("characteristic_zero_order_basis_expanded", "original_target272_endpoint_coordinates_computed",
                    "five_target_endpoint_ideal_lattices_computed", "P0_endpoint_numeric_Norm_calibration_computed",
                    "P1_endpoint_numeric_Norm_calibration_computed", "NmPhi_detU_and_reference_original_frames_evaluated",
                    "Hecke_Picard_active_support_or_height_computed"):
            assert final[key] is False
    if not run["complete"]:
        assert run["process_exit_code"] != 0 and (final is None or final["complete"] is False)
        print("R917_INCOMPLETE_IO_REVIEW=" + json.dumps({"result": RESULT,
            "actual_complete_math_stages": len(all_stages), "core_receipt_present": core is not None,
            "actual_process_exit_code": run["process_exit_code"],
            "actual_stop": core.get("error") if core else run.get("error"),
            "actual_completed_endpoint_count": final["actual_completed_endpoint_count"] if final else 0,
            "original_source_files": receipt["actual_selected_original_file_count"],
            "mathematics_reexecuted": False}, sort_keys=True), flush=True)
        return 0
    assert run["process_exit_code"] == 0 and core is not None and core["complete"] is True
    assert final is not None and final["complete"] is True and final["stop_reason"] is None
    assert final["prime"] == PRIME and final["original_zeta_root"] == ZETA and final["original_s_root"] == SROOT
    assert core["actual_original_two_endpoint_normal_orders_certified"] is True
    assert core["endpoint_target_NormPhi_frames_or_height_computed"] is False
    assert final["actual_completed_endpoint_count"] == core["actual_completed_endpoint_count"] == 2
    for key in ("actual_original_two_endpoint_normal_orders_certified",
                "actual_full_length8_endpoint_algebras_preserved",
                "actual_primitive_and_original_t_order_frames_computed"):
        assert final[key] is True
    inventory = own(out, final["stage_manifest"], tag)
    assert {x["file"]: plain(x) for x in inventory["files"]} == all_stages
    assert plain(final["resume_state"])["file"] == CURRENT
    bound(out, final["resume_state"])
    audit = own(out, final["source_audit"], tag)
    assert audit["source_identities"] == tag["sources"] and audit["inputs"] == item["inputs"]
    assert audit["actual_selected_original_file_count"] == receipt["actual_selected_original_file_count"]
    assert set(final["completed_endpoint_certificates"]) == {"0", "1"}
    endpoints = {}
    for endpoint in (0, 1):
        cert = own(out, final["completed_endpoint_certificates"][str(endpoint)], tag)
        assert cert["endpoint"] == endpoint and cert["prime"] == PRIME
        assert cert["actual_final_discriminant_order"] == 4
        for key in ("common_cleared17_jets_computed", "normal_order_certified",
                    "full_length8_special_fibre_preserved", "primitive_and_original_t_determinant_frames_computed",
                    "all_original_primitive_relation_and_basis_inverse_products_verified",
                    "full_discriminant_order_and_leading_determinant_change_verified"):
            assert cert[key] is True
        assert cert["characteristic_zero_expanded_order_basis_claimed"] is False
        assert cert["target_coordinates_target_ideals_or_endpoint_Norms_computed"] is False
        cleared = own(out, cert["source_common_cleared_jets"], tag)
        assert cleared["endpoint"] == endpoint and cleared["absolute_rho_precision"] == COUNT
        shape(cleared["common_cleared_coefficient_jets_mod_prime"], [17, COUNT])
        assert cleared["source_exact_coordinate_expression"] == item["inputs"]["exact_coordinate_expression"]
        assert cleared["source_original_coordinate_matrix"] == item["inputs"]["seventeen_coordinates"]
        assert cleared["all17_regular_functions_have_original_weight10"] is True
        assert cleared["theta_inverse_computed"] is False and cleared["old_P_K_coordinates_recomputed"] is False
        for row in cleared["source_V8_partial_blocks"]:
            part = own(out, row, tag)
            assert part["endpoint"] == endpoint and part["absolute_rho_precision"] == COUNT
        sections = own(out, cleared["source_theta_A"], tag)
        shape(sections["theta0_jets_mod_prime"], [COUNT]); shape(sections["N692_over_tau4_jets_mod_prime"], [COUNT])
        assert sections["P0_first3_output_coefficients_copied"] is (endpoint == 0)
        for row in sections["source_monomial_blocks"]:
            monomials = own(out, row, tag)
            assert monomials["endpoint"] == endpoint and monomials["absolute_rho_precision"] == COUNT
        primitive = own(out, cert["source_primitive_order"], tag)
        assert primitive["all_eight_complete_unit_quotient_products_verified"] is True
        assert primitive["all_possible_negative_initial_coefficients_verified_zero"] is True
        assert primitive["uniform_precision_is_input_N_minus_leading_order"] is True
        order_schema(primitive["order"])
        order = own(out, cert["complete_normal_order"], tag)
        N = order_schema(order["order"])
        assert N == cert["actual_remaining_rho_precision"]
        discriminant = own(out, cert["complete_trace_discriminant"], tag)
        assert discriminant["discriminant_order"] == 4 and discriminant["division_free_determinant"] is True
        assert discriminant["absolute_rho_precision"] == N
        shape(discriminant["trace_gram_matrix"], [8, 8, N])
        shape(discriminant["discriminant_series"], [N])
        assert discriminant["source_order"] == cert["complete_normal_order"]
        assert len(cert["enlargements"]) == cert["actual_enlargement_step_count"]
        for step, entry in enumerate(cert["enlargements"]):
            assert entry["step"] == step
            kernel = own(out, entry["kernel"], tag)
            grown = own(out, entry["new_order"], tag)
            assert kernel["all_four_block_idealizer_conditions_included"] is True
            assert kernel["index_length_increment"] == entry["index_length_increment"]
            assert grown["original_primitive_relation_in_transported_table_verified"] is True
            verification = grown["verification"]
            for key in ("all_possible_negative_structure_coefficients_vanish",
                        "both_exact_Laurent_basis_inverse_products_verified",
                        "all_eight_left_and_right_unit_products_verified",
                        "complete_512_structure_coefficients_transported"):
                assert verification[key] is True
            assert verification["lowest_possible_shift"] == -2 and verification["uniform_precision_loss"] == 2
        special = own(out, cert["complete_length8_special_fibre"], tag)
        assert special["dimension"] == 8 and special["original_geometric_length_pattern"] == [1, 1, 3, 3]
        assert special["radical_square_dimension"] == 2 and special["all_radical_cube_products_zero"] is True
        assert special["all_factors_and_nilpotents_retained"] is True
        assert special["reduced_quotient_substituted_for_full_fibre"] is False
        shape(special["complete_structure_constants_mod_rho"], [8, 8, 8])
        shape(special["one_mod_rho"], [8])
        frame = own(out, cert["primitive_and_t_frames"], tag)
        assert frame["endpoint"] == endpoint and frame["source_normal_order"] == cert["complete_normal_order"]
        assert frame["local_parameter"] == STRATEGY["endpoint_parameters"][endpoint]
        assert frame["both_determinant_factors_required_under_dual7"] is True
        assert frame["reference_or_target_NormPhi_detU_numeric_calibration_computed"] is False
        assert frame["target_w_Laurent_inverse_or_272_normal_coordinates_computed"] is False
        assert frame["characteristic_zero_basis_or_frame_scalar_expanded"] is False
        assert frame["original_dual7"] == audit["original_dual7"]
        assert frame["original_nu"]["iota_fixes_nu"] is True
        assert frame["original_nu"]["new_nu_over_rho_numeric_value_computed"] is False
        assert len(frame["original_U_coordinates_in_normal_order_basis"]) == 8
        for row in frame["original_U_coordinates_in_normal_order_basis"]:
            laurent_shape(row)
        endpoints[str(endpoint)] = {"certificate": final["completed_endpoint_certificates"][str(endpoint)],
            "normal_order": cert["complete_normal_order"], "special_fibre": cert["complete_length8_special_fibre"],
            "frames": cert["primitive_and_t_frames"], "actual_discriminant_order": 4,
            "actual_enlargement_steps": cert["actual_enlargement_step_count"],
            "actual_remaining_rho_precision": N,
            "actual_primitive_Theta_rho_power": frame["initial_Theta_rho_power"],
            "actual_determinant_rho_order": frame["determinant_rho_order_relative_to_1_U_to_U7"],
            "actual_determinant_rho_leading": frame["determinant_rho_leading_mod_prime"],
            "actual_determinant_t_leading": frame["determinant_t_leading_mod_prime"]}
    print("R917_COMPLETE_IO_REVIEW=" + json.dumps({"result": RESULT,
        "certificate": entries[FINAL], "stage_manifest": final["stage_manifest"],
        "actual_complete_math_stages": len(all_stages),
        "actual_original_source_files": receipt["actual_selected_original_file_count"],
        "endpoints": endpoints, "actual_target_NormPhi_endpoint_frames_computed": False,
        "mathematics_reexecuted_by_wrapper": False, "seconds": final["seconds"]}, sort_keys=True), flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    item = read(REQUEST)
    io_module, transport = guard(item)
    return verify(item, args.output, io_module, transport) if args.verify else compute(item, args.output, io_module, transport)


if __name__ == "__main__":
    raise SystemExit(main())
