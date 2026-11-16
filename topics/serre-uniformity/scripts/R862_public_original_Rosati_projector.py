#!/usr/bin/env python3
"""Standard-library source transport for the original R862 projector.

Only frozen public IO wrappers are imported.  This wrapper never imports the
mathematical core and never repeats any old mathematical calculation.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import signal
import subprocess
import sys
import tarfile
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R862-original-Rosati-projector-public-request.json"
REPOSITORY = "Rogerhu12/math-research-public"
RESULT = "R862-original-Rosati-projector-and-integral-correspondences"
FINAL = "p41-original-Rosati-projector-and-integral-correspondences-certificate.json"
PREFIX = "R862-original-projector-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
INVENTORY = PREFIX + "original-source-inventory.json"
INPUT_RECEIPT = PREFIX + "retained-inputs-receipt.json"
BUNDLE = PREFIX + "retained-original-inputs.tar.gz"
CORE = "R862_original_Rosati_projector.py"
PUBLIC_IO = "R858_public_original_p41_single_Z.py"
PUBLIC_IO_SHA = "fb77d8fb452a5efbc2cc8e9b7af8a090813ebd9c9e8fb416ee62ea09be88c8ab"
TRANSPORT_PINS = {
    "R852_public_original_one_Z_coefficients.py":
        "873097d8462f1f20d8cb05adb2e5b3261bbea44a1a58de12a05e9286970dee3c",
    "R850_public_original_rigidified_fibres.py":
        "ff318ca06e5bf2a385c866df2abb0ea102d6606eb2af2a818a0493f075b123cf",
    "R824_public_original_global_polar_generators.py":
        "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c",
}
IO = None

# Byte-exact mathematical identity copied from the new core as data only.
STRATEGY = {
    "original_p": 41,
    "original_map_index": 4,
    "original_map_degree": 1206,
    "original_real_map_degree": 3618,
    "coefficient_field": "Q[S]/(S^6-S^5-6*S^4+6*S^3+8*S^2-8*S+1)",
    "field_basis": "1,S,S^2,S^3,S^4,S^5",
    "old_aA_basis": "1,s1,s2,s3,s4,s5; sj=t^j+t^(-j)",
    "norm_polynomial": "Norm_F/Q(X-aA), without a primitiveness assumption",
    "new_characteristic_polynomial_algorithm": "exact integral Faddeev-LeVerrier",
    "D": "q_R^dagger*q_R, sum of seven original real-map pull-push correspondences",
    "projector": "1-P_A(D)/P_A(0)=q^dagger*kappa^(-1)*q",
    "integer_multiple": "-(D^6+c5*D^5+...+c1*D)",
    "integer_denominator": "d_A=P_A(0)>0; no minimality claim",
    "original_T7_phase": "zeta^2",
    "whole_JX_equality_source": "R862 proof, not only the 12-row Hom check",
    "Y_active_Hecke_projector_computed": False,
    "non_p_height_support_computed": False,
    "old_arithmetic_recomputed": False,
    "budget_excluded_from_mathematical_identity": True,
}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def sha(path):
    answer = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            answer.update(block)
    return answer.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
    tmp.replace(path)


def plain(row):
    result = {k: row[k] for k in ("file", "bytes", "sha256")}
    path = PurePosixPath(result["file"])
    assert len(path.parts) == 1 and path.name not in ("", ".", "..")
    assert "\\" not in result["file"] and not path.is_absolute()
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert len(result["sha256"]) == 64
    return result


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(folder, row):
    row = plain(row)
    path = Path(folder) / row["file"]
    assert path.is_file() and path.stat().st_size == row["bytes"]
    assert sha(path) == row["sha256"]
    return path


def load_io(directory=None):
    global IO
    folder = S if directory is None else Path(directory)
    assert sha(folder / PUBLIC_IO) == PUBLIC_IO_SHA
    for name, digest in TRANSPORT_PINS.items():
        assert sha(folder / name) == digest
    entry = importlib.util.spec_from_file_location("R862_frozen_source_IO", folder / PUBLIC_IO)
    IO = importlib.util.module_from_spec(entry)
    entry.loader.exec_module(IO)
    IO.load_transport(folder)


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
            "proof": item["proof"], "strategy": STRATEGY,
            "source_identity": IO.source_identity(item["source"]),
            "carrier_identity": IO.source_identity(item["carrier_source"]),
            "inputs": item["inputs"]}


def review_original_sources(item, retained):
    """Pure IO, callable locally with the already existing source cache."""
    retained = Path(retained)
    carrier, source = item["carrier_source"], item["source"]
    cert = IO.review_source("R852", carrier, retained / "R852")
    public = read(retained / "R852/public-actions-input.json")
    parent = IO.PARENT_IO
    for name in (parent.INVENTORY, parent.BUNDLE, parent.INPUT_RECEIPT):
        bound(retained / "R852", carrier["files"][name])
    nested, groups, original_receipt = parent.sources(public["job"], retained / "R852")
    assert sum(group["selected_file_count"] for group in groups.values()) == 270
    IO.same_origin(source, groups["R791"])
    IO.same_origin(source, cert["configuration"]["source_identities"]["R791"])
    for name, row in source["files"].items():
        assert plain(groups["R791"]["files"][name]) == plain(row)
        IO.copy_bound(Path(nested) / "R791", retained / "R791", row)
    original_cert = IO.review_source("R791", source, retained / "R791")
    for row in item["inputs"].values():
        assert plain(source["files"][row["file"]]) == plain(row)
        IO.stage(retained / "R791", source, row)
    assert item["inputs"]["galois"]["file"] == "R791-original-Hom-Galois-matrices.json.gz"
    assert item["inputs"]["polarization"]["file"] == "R791-original-real-descent-and-eta-basis-inputs.json.gz"
    assert original_cert["selected_real_map_degree"] == "3618"
    return {
        "result": RESULT, "complete": True,
        "carrier_identity": IO.source_identity(carrier),
        "original_source_identity": IO.source_identity(source),
        "original_R852_direct_carrier_members": 9,
        "original_nested_members_verified": 270,
        "selected_R791_members": len(source["files"]),
        "original_source_bundle": plain(original_receipt["source_bundle"]),
        "old_R791_artifact_requested": False,
        "old_R847_artifact_requested": False,
        "all_selected_bytes_source_schemas_and_parent_child_links_verified": True,
        "mathematical_core_imported_or_executed": False,
    }


def pack(retained, groups, target):
    retained, target = Path(retained), Path(target)
    tmp = target.with_name(target.name + ".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0, compresslevel=0) as zipped:
            with tarfile.open(fileobj=zipped, mode="w|") as archive:
                for label, source in sorted(groups.items()):
                    for name, row in sorted(source["files"].items()):
                        path = bound(retained / label, row)
                        info = archive.gettarinfo(str(path), arcname=label + "/" + name)
                        info.uid = info.gid = info.mtime = 0
                        info.uname = info.gname = ""
                        with path.open("rb") as stream:
                            archive.addfile(info, stream)
    tmp.replace(target)


def unpack(bundle, retained, groups):
    expected = {label + "/" + name: plain(row) for label, source in groups.items()
                for name, row in source["files"].items()}
    seen = set()
    retained = Path(retained)
    with tarfile.open(bundle, mode="r|gz") as archive:
        for member in archive:
            assert member.isfile() and member.name in expected and member.name not in seen
            row = expected[member.name]
            assert member.size == row["bytes"]
            target = retained / member.name
            assert target.resolve().is_relative_to(retained.resolve())
            target.parent.mkdir(parents=True, exist_ok=True)
            old = target.exists()
            if old:
                bound(target.parent, row)
            tmp = target.with_name(target.name + ".tmp")
            digest = hashlib.sha256()
            total = 0
            source = archive.extractfile(member)
            assert source is not None
            stream = None if old else tmp.open("wb")
            try:
                for block in iter(lambda: source.read(4*1024*1024), b""):
                    digest.update(block)
                    total += len(block)
                    if stream is not None:
                        stream.write(block)
            finally:
                if stream is not None:
                    stream.close()
            assert total == row["bytes"] and digest.hexdigest() == row["sha256"]
            if not old:
                tmp.replace(target)
            seen.add(member.name)
    assert seen == set(expected)
    return len(seen)


def sources(item, out):
    out = Path(out)
    retained = out.parent / "retained-R862"
    groups = {"R852": item["carrier_source"], "R791": item["source"]}
    present = [(out / name).exists() for name in (BUNDLE, INVENTORY, INPUT_RECEIPT)]
    if all(present):
        receipt, inventory = read(out / INPUT_RECEIPT), read(out / INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is inventory["complete"] is True
        assert inventory["sources"] == groups
        bound(out, receipt["source_inventory"])
        bound(out, receipt["source_bundle"])
        count = unpack(out / BUNDLE, retained, groups)
    else:
        # A hard interruption may leave the IO-only carrier transaction between
        # its atomic files.  Rebuild these transport files from original bytes;
        # no mathematical stage is removed or evaluated.
        if (out / INVENTORY).exists():
            assert read(out / INVENTORY)["sources"] == groups
        retained.mkdir(parents=True, exist_ok=True)
        transport = IO.fetch_source("R852", item["carrier_source"], retained)
        reviewed = review_original_sources(item, retained)
        count = sum(len(source["files"]) for source in groups.values())
        save(out / INVENTORY, {"result": RESULT, "complete": True, "sources": groups,
            "all_members_are_unchanged_original_bytes": True})
        pack(retained, groups, out / BUNDLE)
        save(out / INPUT_RECEIPT, {"result": RESULT, "complete": True,
            "source_inventory": spec(out / INVENTORY), "source_bundle": spec(out / BUNDLE),
            "selected_direct_member_count": count, "source_review": reviewed,
            "range_transport": transport, "old_mathematical_arithmetic_repeated": False})
    reviewed = review_original_sources(item, retained)
    receipt = read(out / INPUT_RECEIPT)
    assert reviewed == receipt["source_review"]
    assert count == receipt["selected_direct_member_count"]
    print("R862_SOURCE_IO_REVIEW=" + json.dumps({
        "direct_members": count, "original_nested_members": 270,
        "source_bundle": receipt["source_bundle"], "old_math_repeated": False}, sort_keys=True), flush=True)
    return retained, receipt


def stable_job(item):
    return {key: value for key, value in item.items()
            if key not in ("budget_minutes", "resume", "session", "readme_sha256",
                           "rules_last_read_commit")}


def topic_path(name):
    path = (TOPIC / name).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def guard(item, request):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == CORE and item["core_sha256"] == sha(S / CORE)
    assert item["wrapper"] == Path(__file__).name and item["wrapper_sha256"] == sha(__file__)
    assert 0 < item["budget_minutes"] <= 300
    assert item["source_IO"] == PUBLIC_IO and item["source_IO_sha256"] == PUBLIC_IO_SHA
    assert item["transport_dependencies"] == TRANSPORT_PINS
    assert sha(topic_path(item["proof"]["path"])) == item["proof"]["sha256"]
    assert sha(REPO / "README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC / "README.md") == item["readme_sha256"]["topic"]
    assert item["source"]["expected_conclusion"] == item["carrier_source"]["expected_conclusion"] == "success"
    assert item["source"]["accepted_process_exit_codes"] == [0]
    assert item["carrier_source"]["accepted_process_exit_codes"] == [0]
    load_io()


def manifest(out):
    rows = [spec(path) for path in sorted(Path(out).iterdir())
            if path.is_file() and path.name not in (MANIFEST, REFERENCE)
            and not path.name.endswith((".tmp", ".partial", ".download"))]
    save(Path(out) / MANIFEST, {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_retention_days": 1,
        "machine_outputs_in_git_or_release": False})
    save(Path(out) / REFERENCE, {"result": RESULT, "manifest_file": MANIFEST,
        "manifest_bytes": (Path(out) / MANIFEST).stat().st_size,
        "manifest_sha256": sha(Path(out) / MANIFEST), "file_count": len(rows)})


def restore(item, out):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    out = Path(out)
    folder = out.parent / "R862-resume-metadata"
    folder.mkdir(parents=True, exist_ok=True)
    archive = IO.IO.Archive(resume, out.parent / "R862-resume-download", whole=False)
    try:
        archive.extract_bound(MANIFEST, resume["manifest_sha256"], folder / MANIFEST, resume["manifest_bytes"])
        data = read(folder / MANIFEST)
        assert data["result"] == RESULT
        entries = {row["file"]: plain(row) for row in data["files"]}
        assert len(entries) == len(data["files"]) == resume["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name in ("run-receipt.json", "public-actions-input.json"):
            row = entries[name]
            archive.extract_bound(name, row["sha256"], folder / name, row["bytes"])
        run, public = read(folder / "run-receipt.json"), read(folder / "public-actions-input.json")
        assert run["source_commit"] == public["source_commit"] == resume["source_commit"]
        assert str(run["workflow_run_id"]) == str(resume["run_id"])
        assert public["source_repository"] == REPOSITORY
        assert public["core_sha256"] == item["core_sha256"]
        assert public["wrapper_sha256"] == item["wrapper_sha256"]
        assert stable_job(public["job"]) == stable_job(item)
        assert run["process_exit_code"] in (0, 1, 124, 137, -15, -9)
        names = [name for name in entries
                 if name.startswith(PREFIX) and name.endswith(".json.gz")]
        if all(name in entries for name in (INVENTORY, INPUT_RECEIPT, BUNDLE)):
            names += [INVENTORY, INPUT_RECEIPT, BUNDLE]
        if run["complete"] is True:
            names.append(FINAL)
        for name in dict.fromkeys(names):
            row = entries[name]
            archive.extract_bound(name, row["sha256"], out / name, row["bytes"])
        for name in names:
            if name.endswith(".json.gz"):
                value = read(out / name)
                assert value["complete"] is True and value["configuration"] == expected_tag(item)
        save(out / "resume-source-receipt.json", {"result": RESULT, "complete": True,
            "source_request": resume, "all_selected_old_bytes_unchanged": True,
            "old_stable_job_identical": True, "range_transport": archive.receipt()})
    finally:
        archive.close()


def stage(out, row, tag):
    value = read(bound(out, row))
    assert value["result"] == RESULT and value["complete"] is True
    assert value["configuration"] == tag
    return value


def review_math(item, out):
    out = Path(out)
    tag = expected_tag(item)
    cert = read(out / FINAL)
    assert cert["complete"] is True and cert["result"] == RESULT
    assert cert["configuration"] == tag
    index = stage(out, cert["stage_manifest"], tag)
    assert index["completed_math_stage_count"] == cert["completed_math_stage_count"] == 4
    files = {row["file"]: plain(row) for row in index["files"]}
    assert len(files) == 4
    for row in files.values():
        stage(out, row, tag)
    keys = ("source_audit", "norm_polynomial", "completed_Hom_matrix_action",
            "integral_correspondence_program")
    for key in keys:
        assert files[cert[key]["file"]] == plain(cert[key])
    norm = stage(out, cert["norm_polynomial"], tag)
    action = stage(out, cert["completed_Hom_matrix_action"], tag)
    program = stage(out, cert["integral_correspondence_program"], tag)
    assert len(norm["field_minimal_polynomial_ascending"]) == 7
    assert len(norm["aA_power_basis"]) == len(norm["multiplication_matrix"]) == 6
    assert all(len(row) == 6 for row in norm["multiplication_matrix"])
    assert len(norm["P_A_ascending"]) == 7 and norm["P_A_ascending"][-1] == "1"
    assert norm["d_A"] == norm["P_A_ascending"][0] == cert["actual_d_A"]
    assert isinstance(norm["d_A"], str) and norm["d_A"].isdigit() and norm["d_A"] != "0"
    assert norm["d_A_positive_integer"] is True
    assert norm["full_Cayley_Hamilton_in_original_field_verified"] is True
    assert norm["full_aA_times_inverse_numerator_equals_dA_verified"] is True
    assert norm["aA_primitiveness_assumed"] is False and norm["d_A_claimed_minimal"] is False
    assert action["matrix_shape"] == [12, 12]
    assert action["norm_polynomial"] == cert["norm_polynomial"]
    for key in ("P_A_of_original_E_exactly_zero",
                "integral_multiple_of_original_E_exactly_dA_identity",
                "full_polynomial_idempotence_mod_X_times_P_A_verified",
                "whole_JX_projection_not_inferred_only_from_12_Hom_rows"):
        assert action[key] is True
    assert program["norm_polynomial"] == cert["norm_polynomial"]
    assert program["completed_Hom_matrix_action"] == cert["completed_Hom_matrix_action"]
    assert program["node_count"] == len(program["nodes"])
    assert len({node["id"] for node in program["nodes"]}) == program["node_count"]
    assert len(program["outputs"]["five_original_symmetric_correspondences"]) == 5
    assert program["this_is_the_Y_active_Hecke_projector"] is False
    assert program["all_fiber_product_equations_materialized"] is False
    for key in ("original_canonical_A_Rosati_projector_as_expression_certified",
                "actual_positive_integer_multiple_and_norm_polynomial_computed",
                "original_full_12_Hom_matrix_action_verified",
                "original_whole_JX_equality_bound_to_proof",
                "original_five_symmetric_correspondence_recipes_preserved"):
        assert cert[key] is True
    for key in ("original_kappa_or_polarization_changed", "Y_active_Hecke_projector_computed",
                "Y_torsion_clearing_N_computed", "non_p_height_support_or_values_computed",
                "actual_height_computed", "height_nonzero_proved",
                "old_Hom_Gram_Galois_or_period_computations_repeated", "all_p_uniformity_proved"):
        assert cert[key] is False
    return cert


def compute(item, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    code, error, cert = 1, None, None
    try:
        restore(item, out)
        retained, receipt = sources(item, out)
        config = {"result": RESULT, "p": 41, "core_sha256": item["core_sha256"],
            "proof": item["proof"], "source": item["source"], "inputs": item["inputs"],
            "carrier_identity": IO.source_identity(item["carrier_source"])}
        config_path = out.parent / "R862-expanded-config.json"
        save(config_path, config)
        save(out / "public-actions-input.json", {"result": RESULT,
            "source_repository": REPOSITORY, "source_commit": os.environ["GITHUB_SHA"],
            "job": item, "core_sha256": item["core_sha256"], "wrapper_sha256": item["wrapper_sha256"],
            "root_readme_sha256": item["readme_sha256"]["root"],
            "topic_readme_sha256": item["readme_sha256"]["topic"],
            "source_inventory": receipt["source_inventory"],
            "expanded_config_sha256": sha(config_path)})
        command = [sys.executable, str(S / CORE), "--config", str(config_path),
            "--proof", str(topic_path(item["proof"]["path"])), "--retained", str(retained),
            "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out / "core.log").open("wb") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"] * 60 + 900)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code, error = 124, "Outer timeout; unchanged complete stages retained."
        if code == 0:
            cert = review_math(item, out)
            core = read(out / "core-receipt.json")
            assert core["complete"] is True and core["process_exit_code"] == 0 and core["error"] is None
            assert core["source_sha256"] == item["core_sha256"]
            assert core["configuration"] == expected_tag(item)
            assert core["certificate_sha256"] == sha(out / FINAL)
    except Exception:
        error, code = traceback.format_exc(), 1
        print(error, flush=True)
    finally:
        save(out / "run-receipt.json", {"result": RESULT, "source_commit": os.environ["GITHUB_SHA"],
            "workflow_run_id": os.environ["GITHUB_RUN_ID"],
            "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "1"),
            "started_at_utc": started, "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "complete": code == 0, "process_exit_code": code, "error": error,
            "core_receipt_sha256": sha(out / "core-receipt.json") if (out / "core-receipt.json").exists() else None,
            "certificate_sha256": sha(out / FINAL) if cert is not None else None})
        manifest(out)
        summary = {"result": RESULT, "complete": code == 0, "process_exit_code": code,
            "error": error, "full_manifest": spec(out / MANIFEST)}
        if cert is not None:
            norm = read(out / cert["norm_polynomial"]["file"])
            summary.update(actual_d_A=cert["actual_d_A"], P_A_ascending=norm["P_A_ascending"],
                stage_manifest=cert["stage_manifest"], certificate=spec(out / FINAL),
                completed_math_stages=4, seconds=cert["seconds"],
                Y_active_Hecke_projector_computed=False, actual_height_computed=False)
        print("R862_PROJECTOR_RUN_RECEIPT=" + json.dumps(summary, sort_keys=True), flush=True)
    return code


def verify(item, out):
    out = Path(out)
    data = read(out / MANIFEST)
    assert data["result"] == RESULT
    rows = {row["file"]: plain(row) for row in data["files"]}
    assert len(rows) == len(data["files"])
    for row in rows.values():
        bound(out, row)
    reference = read(out / REFERENCE)
    assert reference["manifest_sha256"] == sha(out / MANIFEST)
    assert reference["manifest_bytes"] == (out / MANIFEST).stat().st_size
    assert reference["file_count"] == len(rows)
    run, public = read(out / "run-receipt.json"), read(out / "public-actions-input.json")
    assert run["result"] == public["result"] == RESULT
    assert public["job"] == item and public["wrapper_sha256"] == item["wrapper_sha256"]
    assert public["core_sha256"] == item["core_sha256"]
    assert run["source_commit"] == public["source_commit"]
    retained, receipt = sources(item, out)
    assert public["source_inventory"] == receipt["source_inventory"]
    if (out / "core-receipt.json").exists():
        core = read(out / "core-receipt.json")
        assert run["core_receipt_sha256"] == sha(out / "core-receipt.json")
        assert core["source_sha256"] == item["core_sha256"]
        if core["configuration"] is not None:
            assert core["configuration"] == expected_tag(item)
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
        core = None
    for path in out.glob(PREFIX + "*.json.gz"):
        value = read(path)
        assert value["complete"] is True and value["configuration"] == expected_tag(item)
    if run["complete"]:
        cert = review_math(item, out)
        assert core is not None and core["complete"] is True
        assert core["process_exit_code"] == run["process_exit_code"] == 0
        assert run["certificate_sha256"] == core["certificate_sha256"] == sha(out / FINAL)
        print("R862_COMPLETE_IO_REVIEW=" + json.dumps({
            "complete": True, "manifest_members": len(rows),
            "direct_source_members": receipt["selected_direct_member_count"],
            "original_nested_members": 270, "actual_d_A": cert["actual_d_A"],
            "certificate": spec(out / FINAL), "all_original_bytes_and_new_stages_verified": True,
            "mathematical_core_imported_or_executed": False}, sort_keys=True), flush=True)
        return 0
    print("R862_PARTIAL_IO_REVIEW=" + json.dumps({
        "complete": False, "process_exit_code": run["process_exit_code"],
        "manifest_members": len(rows), "all_available_selected_bytes_verified": True,
        "core_receipt_present": core is not None}, sort_keys=True), flush=True)
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("compute", "verify"))
    parser.add_argument("--request", default=str(REQUEST))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    request = Path(args.request)
    item = read(request)
    guard(item, request)
    return compute(item, args.output) if args.mode == "compute" else verify(item, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
