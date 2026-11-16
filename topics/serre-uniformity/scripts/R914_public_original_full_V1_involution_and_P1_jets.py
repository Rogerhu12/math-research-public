#!/usr/bin/env python3
"""Standard-library source transport, continuation and IO review for R914."""
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
REQUEST = TOPIC / "notes/R914-original-full-V1-involution-and-P1-jets-public-request.json"
RESULT = "R914-original-full-V1-involution-and-P1-local-jets"
FINAL = "p41-original-full-V1-involution-and-P1-jets-certificate.json"
PREFIX = "R914-iota-"
STAGES = PREFIX + "stage-manifest.json.gz"
CURRENT = PREFIX + "current.json.gz"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R914-retained-original-inputs.tar.gz"
INVENTORY = "R914-original-source-inventory.json"
INPUT_RECEIPT = "R914-retained-inputs-receipt.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
H64 = re.compile(r"[0-9a-f]{64}")
PRIME, DIM, XI, ROWS, RANK, LAST, COUNT, GROUP_SIZE = 1000000753, 146, 40, 560, 272, 272, 273, 16
EPS = [0] + [1] * 144 + [2] * 127
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
SOURCES = ("R786", "R805", "R837", "R853", "R872", "R883")
PROOFS = ("R912", "R802", "R805", "R853", "R872", "R883")
SOURCE_COUNTS = {"R786": 152, "R805": 7, "R837": 9, "R853": 9, "R872": 282, "R883": 10}
# BEGIN_FROZEN_DEFINITIONS
DEFINITIONS = {
    "R786": ("R786-exact-original-power5-short-basis",
        "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "p41-exact-original-power5-short-basis-certificate.json"),
    "R805": ("R805-original-affine-pencil-free-basis",
        "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420",
        "p41-original-affine-pencil-free-basis-certificate.json"),
    "R837": ("R837-original-fixed-branch-pencil",
        "5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924",
        "p41-original-fixed-branch-pencil-certificate.json"),
    "R853": ("R853-original-semilinear-V1-generator-conjugates",
        "5b65e7ccf7c6663949155fdd30abc4c765823e861259c8f9b90b26d0bc1511df",
        "p41-original-semilinear-V1-conjugates-certificate.json"),
    "R872": ("R872-original-P0-jets-and-fixed-Picard-RR-spaces",
        "0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874",
        "p41-original-P0-jets-and-fixed-Picard-RR-spaces-certificate.json"),
    "R883": ("R883-original-t-first-order-frame",
        "2778a81b5639a1eb6285718574af0ce4b48b00e92b648c6ac29ffe70c1da66f7",
        "p41-original-t-first-order-frame-certificate.json"),
}
# END_FROZEN_DEFINITIONS
# BEGIN_FROZEN_STRATEGY
STRATEGY = {
    "scope": "complete_original_K_linear_V1_iota_and_P1_local_transport_only",
    "geometric_involution": "iota=T^41, qY->-qY, t->1-t; K fixed",
    "arithmetic_cY_not_substituted_for_geometric_iota": True,
    "original_integer_V1_scale_already_in_source": "6724",
    "additional_scale_applied": False,
    "full_source_rows": ROWS,
    "original_V1_dimension": DIM,
    "old_exact_target_order": ["tau", "sigma", "w0"],
    "new_exact_rhs_indices": [i for i in range(DIM) if i not in (0, 2, 73)],
    "new_exact_rhs_count": 143,
    "reused_columns": "C[:,0]=old_tau; C[:,2]=old_w0; C[:,73]=old_sigma-C[:,1]",
    "selected_rows": "the unchanged R837 original exact-nonzero minor",
    "exact_verification": "S*C=diag((-1)^floor(row/40))*S on all560 rows; C*C=I146",
    "coordinate_field": "Q, extended K-linearly; original s and zeta fixed",
    "auxiliary_prime": PRIME,
    "prime_role": "reduction of exact C and transport of already completed R872 jets",
    "original_normal_degrees": EPS,
    "P0_parameter": "rho0=z-z0",
    "P1_parameter": "rho1=iota^*rho0=z-2*beta72-z0",
    "jet_first_order": 0,
    "jet_last_order": LAST,
    "normal_group_size": GROUP_SIZE,
    "P1_t_frame": "t1=t-1; c1=-c0; all original first3 coefficients transported by minus",
    "old_three_exact_solves_recomputed": False,
    "old_reflection_minor_or_Fourier_rows_recomputed": False,
    "old_P0_Hensel_recurrence_recomputed": False,
    "old_W_Gamma_or_Mg_recomputed": False,
    "endpoint_rank8_order_or_norms_computed": False,
    "only_budget_and_transport_paths_excluded_from_identity": True,
}
# END_FROZEN_STRATEGY


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


def expected_tag(item, sources):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
            "python_flint": "0.9.0", "prime": PRIME,
            "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
            "method_sha256": item["method_sha256"],
            "sources": {k: source_identity(sources[k]) for k in SOURCES},
            "strategy": STRATEGY}


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


def guard(item):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == "R914_original_full_V1_involution_and_P1_jets.py"
    assert item["wrapper"] == Path(__file__).name
    assert sha(HERE / item["core"]) == item["core_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300
    assert sha(REPO / "README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC / "README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(SOURCES)
    assert set(item["transports"]) == {"R853", "R856", "R872", "R883"}
    assert set(item["proofs"]) == set(PROOFS)
    for key in PROOFS:
        assert sha(topic_path(item["proofs"][key]["file"])) == item["proofs"][key]["sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    for label, source in item["sources"].items():
        result, core, final = DEFINITIONS[label]
        assert source["result"] == result and source["core_sha256"] == core
        assert plain(source["certificate"])["file"] == final
        assert source["selected_file_count"] == SOURCE_COUNTS[label]
        assert H64.fullmatch(source["configuration_sha256"])
        assert H64.fullmatch(source["selected_files_sha256"])
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    assert item["transport_helper"] == "R837_original_branch_pencil_public.py"
    assert item["transport_helper_sha256"] == TRANSPORT_SHA
    io_module = load_module("R914_original_frozen_Range_IO", HERE / item["io_helper"], RANGE_SHA)
    transport = load_module("R914_original_frozen_file_transport", HERE / item["transport_helper"], TRANSPORT_SHA)
    return io_module, transport


def selected_names(label):
    names = {MANIFEST, *META, DEFINITIONS[label][2]}
    if label == "R786":
        names.add("R786-exact-stages-manifest.json.gz")
        names.update(f"R786-exact-power-1-row-{i:04d}.json.gz" for i in range(DIM))
    elif label == "R805":
        names.update(("R805-accepted-pencil.json.gz", "R805-graded-free-basis.json.gz"))
    elif label == "R837":
        names.update(("R837-stage-manifest.json.gz", "R837-original-P0-evaluation.json.gz",
                      "R837-original-V1-reflection-minor.json.gz",
                      "R837-original-V1-reflection-minor-prime-index-0000.json.gz"))
    elif label == "R853":
        names.update(("R853-stage-manifest.json.gz", "R853-original-V1-prefix-and-source-audit.json.gz",
                      "R853-three-exact-original-V1-conjugates.json.gz",
                      "R853-original-semilinear-function-field-generator-DAG.json.gz"))
    elif label == "R872":
        names.update(("R872-exact-stages-manifest.json.gz", "R872-point-linearization.json.gz",
                      "R872-point-jets-index.json.gz", "R872-source-audit.json.gz"))
        names.update(f"R872-point-jet-{n:04d}.json.gz" for n in range(COUNT))
    elif label == "R883":
        names.update("R883-" + name + ".json.gz" for name in (
            "original-source-audit", "original-M2-three-jet-leaves", "original-V4-recipe-bridge",
            "original-cleared-section-three-jets", "original-t-first-order-unit-and-frame-DAG"))
    else:
        raise AssertionError(label)
    assert len(names) == SOURCE_COUNTS[label]
    return sorted(names)


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


def carried_groups(item, label, source, folder, retained, io_module, work):
    contract = item["carriers"][label]
    names = {MANIFEST, *META, contract["bundle"]["file"],
             contract["inventory"]["file"], contract["receipt"]["file"]}
    if label == "R853":
        names.update(selected_names("R853"))
    selected, route = fetch_archive_files(io_module, source, sorted(names), folder, work)
    for key in ("bundle", "inventory", "receipt"):
        assert selected[contract[key]["file"]] == plain(contract[key])
    verify_transport_metadata(source, folder, selected)
    inv = read(bound(folder, contract["inventory"]))
    receipt = read(bound(folder, contract["receipt"]))
    assert inv["result"] == receipt["result"] == source["result"]
    assert inv["complete"] is True and receipt["complete"] is True
    assert plain(receipt["source_bundle"]) == plain(contract["bundle"])
    assert plain(receipt["source_inventory"]) == plain(contract["inventory"])
    keep = set(contract["original_groups"])
    assert keep <= set(inv["sources"])
    for group in keep:
        old = inv["sources"][group]
        assert identity(old) == identity(item["sources"][group])
        assert old["configuration_sha256"] == item["sources"][group]["configuration_sha256"]
        assert plain(old["certificate"]) == plain(item["sources"][group]["certificate"])
    wanted = {group + "/" + name: plain(row) for group, desc in inv["sources"].items()
              for name, row in desc["files"].items()}
    seen = set()
    with tarfile.open(bound(folder, contract["bundle"]), "r:gz") as tar:
        for member in tar:
            p = PurePosixPath(member.name)
            assert member.isfile() and not member.issym() and not member.islnk()
            assert not p.is_absolute() and ".." not in p.parts and len(p.parts) == 2
            assert member.name in wanted and member.name not in seen
            seen.add(member.name)
            row = wanted[member.name]
            assert member.size == row["bytes"]
            preserve = p.parts[0] in keep
            target = retained / member.name
            target.parent.mkdir(parents=True, exist_ok=True)
            temp = target.with_name(target.name + ".tmp")
            output = temp.open("wb") if preserve else None
            h, count = hashlib.sha256(), 0
            with tar.extractfile(member) as stream:
                try:
                    for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
                        h.update(block)
                        count += len(block)
                        if output:
                            output.write(block)
                finally:
                    if output:
                        output.close()
            assert count == row["bytes"] and h.hexdigest() == row["sha256"], member.name
            if preserve:
                if target.exists():
                    bound(target.parent, row)
                    temp.unlink()
                else:
                    temp.replace(target)
    assert seen == set(wanted) and len(seen) == contract["actual_original_carrier_member_count"]
    return {"platform_transport": route, "source_bundle": plain(contract["bundle"]),
            "source_inventory": plain(contract["inventory"]),
            "verified_all_original_carrier_members": len(seen),
            "preserved_original_groups": sorted(keep), "new_mathematics_executed": False}


def review_source(label, source, folder):
    files = {}
    mp = folder / MANIFEST
    assert mp.stat().st_size == source["manifest_bytes"] and sha(mp) == source["manifest_sha256"]
    manifest = read(mp)
    assert manifest["result"] == source["result"]
    all_files = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(all_files) == len(manifest["files"]) == source["manifest_file_count"]
    for name in selected_names(label):
        files[name] = spec(mp) if name == MANIFEST else all_files[name]
        bound(folder, files[name])
    assert len(files) == source["selected_file_count"]
    assert fingerprint([files[n] for n in sorted(files)]) == source["selected_files_sha256"]
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


def prepare_sources(item, out, io_module, transport, allow_download=True):
    retained = out.parent / "R914-retained-original"
    retained.mkdir(parents=True, exist_ok=True)
    if all((out / n).exists() for n in (BUNDLE, INVENTORY, INPUT_RECEIPT)):
        receipt, inventory = read(out / INPUT_RECEIPT), read(out / INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is True and inventory["complete"] is True
        assert receipt["mathematical_source_bindings"] == {k: source_identity(item["sources"][k]) for k in SOURCES}
        bound(out, receipt["source_bundle"])
        bound(out, receipt["source_inventory"])
        count = transport.unpack_sources(out / BUNDLE, retained, inventory)
        reviewed = {k: review_source(k, item["sources"][k], retained / k) for k in SOURCES}
        assert reviewed == inventory["sources"] and count == receipt["actual_selected_original_file_count"] == 469
        return retained, reviewed, receipt
    assert allow_download, "A complete original source carrier is required for a completed-run IO review."
    routes = {}
    for label in ("R853", "R856"):
        print("R914_CARRIER_START=" + label, flush=True)
        folder = retained / label if label == "R853" else out.parent / "R914-transport-R856"
        routes[label] = carried_groups(item, label, item["transports"][label], folder,
            retained, io_module, out.parent / ("R914-download-" + label))
    # R853 carries the original R837 reflection records; R856 carries the
    # same producer's P0/P1 value record.  Their common metadata remain byte
    # identical, so the required nine-member R837 closure is already present.
    for label in ("R872", "R883"):
        print("R914_DIRECT_SOURCE_START=" + label, flush=True)
        unused, route = fetch_archive_files(io_module, item["transports"][label],
            selected_names(label), retained / label, out.parent / ("R914-download-" + label))
        routes[label] = route
    reviewed = {k: review_source(k, item["sources"][k], retained / k) for k in SOURCES}
    inventory = {"result": RESULT, "complete": True, "sources": reviewed,
        "all_entries_are_unchanged_completed_original_source_bytes": True}
    save(out / INVENTORY, inventory)
    transport.pack_sources(retained, inventory, out / BUNDLE)
    count = sum(len(v["files"]) for v in reviewed.values())
    assert count == 469
    receipt = {"result": RESULT, "complete": True,
        "mathematical_source_bindings": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "source_bundle": spec(out / BUNDLE), "source_inventory": spec(out / INVENTORY),
        "actual_selected_original_file_count": count, "actual_original_source_groups": list(SOURCES),
        "transport_routes": routes,
        "old_original_three_solves_minor_jets_W_or_CM_values_recomputed": False,
        "new_mathematics_executed_in_source_preparation": False}
    save(out / INPUT_RECEIPT, receipt)
    print("R914_SOURCE_IO_COMPLETE=" + json.dumps({"source_bundle": receipt["source_bundle"],
        "source_inventory": receipt["source_inventory"], "actual_selected_original_file_count": count,
        "mathematics_executed": False}, sort_keys=True), flush=True)
    return retained, reviewed, receipt


def stable_math(item):
    return {"result": item["result"], "p": item["p"], "core_sha256": item["core_sha256"],
            "proofs": item["proofs"], "method_sha256": item["method_sha256"],
            "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
            "strategy": STRATEGY}


def restore(item, out, io_module, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    meta = out.parent / "R914-resume-original-metadata"
    meta.mkdir(parents=True, exist_ok=True)
    archive = io_module.Archive(resume, out.parent / "R914-download-resume", whole=False)
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
        tag = expected_tag(item, reviewed)
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
        expanded["sources"] = {k: dict(v, directory=str((retained / k).resolve())) for k, v in sources.items()}
        expanded["proofs"] = {k: dict(v, file=str(topic_path(v["file"]))) for k, v in item["proofs"].items()}
        expanded["method"] = str(topic_path(item["method"]))
        save(out / "public-actions-expanded-job.json", expanded)
        initial = {"result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
            "source_commit": os.environ["GITHUB_SHA"], "core_sha256": item["core_sha256"],
            "wrapper_sha256": sha(__file__), "request_sha256": sha(REQUEST), "job": item,
            "method_sha256": item["method_sha256"], "proofs": item["proofs"],
            "actual_configuration": expected_tag(item, sources),
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


def rational_pair(value):
    assert isinstance(value, list) and len(value) == 2
    assert all(isinstance(x, str) and re.fullmatch(r"-?(0|[1-9][0-9]*)", x) for x in value)
    assert int(value[1]) > 0


def verify(item, out, io_module, transport):
    manifest = read(out / MANIFEST)
    assert manifest["result"] == RESULT
    entries = {x["file"]: plain(x) for x in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for row in entries.values():
        bound(out, row)
    run = read(out / META[1])
    assert run["result"] == RESULT and str(run["workflow_run_id"]) == str(os.environ["GITHUB_RUN_ID"])
    if not (out / META[0]).exists():
        assert run["complete"] is False and run["process_exit_code"] != 0 and run["core_receipt_sha256"] is None
        print("R914_SOURCE_PREPARATION_FAILED=" + json.dumps(run, sort_keys=True), flush=True)
        return 0
    initial = read(out / META[0])
    assert initial["result"] == RESULT and initial["source_commit"] == run["source_commit"]
    assert initial["core_sha256"] == item["core_sha256"] and initial["wrapper_sha256"] == item["wrapper_sha256"]
    assert stable_math(initial["job"]) == stable_math(item)
    unused, sources, receipt = prepare_sources(item, out, io_module, transport, allow_download=False)
    tag = expected_tag(item, sources)
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
    if not run["complete"]:
        assert run["process_exit_code"] != 0 and (final is None or final["complete"] is False)
        print("R914_INCOMPLETE_IO_REVIEW=" + json.dumps({"result": RESULT,
            "actual_complete_math_stages": len(all_stages), "core_receipt_present": core is not None,
            "actual_process_exit_code": run["process_exit_code"], "actual_error": core.get("error") if core else run.get("error"),
            "original_source_files": receipt["actual_selected_original_file_count"],
            "mathematics_reexecuted": False}, sort_keys=True), flush=True)
        return 0
    assert run["process_exit_code"] == 0 and core is not None and core["complete"] is True
    assert final is not None and final["complete"] is True
    inventory = own(out, final["stage_manifest"], tag)
    assert {x["file"]: plain(x) for x in inventory["files"]} == all_stages
    for key in ("actual_full146_exact_geometric_iota_certified",
                "actual_original_P1_normal_jets_through_order272_computed",
                "actual_original_P1_t_first_order_unit_certified"):
        assert final[key] is True and core[key] is True
    assert final["source_identities"] == tag["sources"]
    assert final["new_exact_right_hand_side_count"] == 143
    matrix = own(out, final["exact_full_V1_coordinate_matrix"], tag)
    assert matrix["coordinate_matrix_shape"] == [146, 146]
    coordinates = matrix["coordinates_in_original_integer_scaled_V1_basis"]
    assert len(coordinates) == 146 and all(len(r) == 146 for r in coordinates)
    for row in coordinates:
        for value in row:
            rational_pair(value)
    assert matrix["new_rhs_original_indices"] == STRATEGY["new_exact_rhs_indices"]
    assert matrix["new_exact_right_hand_side_count"] == 143 and matrix["old_rhs_recomputed"] is False
    checked = own(out, final["exact_full_V1_verification"], tag)
    assert checked["all560_by146_original_exact_Fourier_equations_verified"] is True
    assert checked["exact_matrix_square_is_identity146"] is True
    assert checked["three_old_exact_answers_preserved_including_sigma_e1_plus_e73"] is True
    assert checked["geometric_iota_K_linear_on_original_V1_certified"] is True
    assert checked["coefficient_conjugation_performed"] is False
    for key in ("original_P0_V1_jet_representation", "original_P1_V1_jets"):
        value = own(out, final[key], tag)
        assert value["matrix_shape"] == [273, 146]
        assert len(value["matrix_mod_prime"]) == 273 and all(len(r) == 146 for r in value["matrix_mod_prime"])
    point = own(out, final["original_P1_point_check"], tag)
    assert point["exact_K_point_row_transport_multiplied_back"] is True
    assert point["both_original146_zero_order_rows_match_completed_P0_and_P1_values"] is True
    assert point["rho1_at_original_P1_exactly_zero"] is True
    assert len(point["original_P1_normal_values_K_1_zeta"]) == 272
    index = own(out, final["original_P1_normal_jets"], tag)
    assert index["normal_basis_rank"] == 272 and index["coefficient_count"] == 273
    assert index["first_order"] == 0 and index["last_order"] == 272
    assert index["all272_original_normal_functions_transported_through_order272"] is True
    assert len(index["normal_groups"]) == 17
    for group, entry in enumerate(index["normal_groups"]):
        value = own(out, entry, tag)
        first, stop = group * 16, min(272, (group + 1) * 16)
        assert value["first_normal_row"] == first and value["stop_normal_row"] == stop
        assert value["normal_basis_rows"] == list(range(first, stop))
        assert value["matrix_shape"] == [273, stop - first]
        assert len(value["normal_basis_jet_matrix_mod_prime"]) == 273
        assert all(len(r) == stop - first for r in value["normal_basis_jet_matrix_mod_prime"])
        assert value["all_group_zero_order_coefficients_equal_exact_original_P1_values"] is True
    frame = own(out, final["original_P1_parameter_and_t_frame"], tag)
    assert frame["rho1_is_not_replaced_by_z_minus_zP1"] is True
    assert frame["rho1_on_P1_branch_equals_parameter_to_all273_available_coefficients"] is True
    assert frame["known_t1_coefficient_count"] == 3 and frame["all273_t_coefficients_computed"] is False
    assert frame["exact_c1_expression"]["operation"] == "negate_original_c0"
    for key in ("endpoint_rank8_integral_algebras_computed", "endpoint_NmPhi_detU_and_reference_frames_evaluated",
                "nine_norm_P0_P1_rigidification_computed", "Poincare_period_theta_or_height_computed"):
        assert final[key] is False
    print("R914_COMPLETE_IO_REVIEW=" + json.dumps({"result": RESULT,
        "certificate": entries[FINAL], "stage_manifest": final["stage_manifest"],
        "actual_complete_math_stages": len(all_stages),
        "actual_original_source_files": receipt["actual_selected_original_file_count"],
        "exact_full146_action_certified": True, "all560_exact_rows_verified": True,
        "original_P1_normal_jet_orders": [0, 272], "original_P1_t_frame_coefficients": 3,
        "rank8_endpoint_algebra_or_Norm_frames_evaluated": False,
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
