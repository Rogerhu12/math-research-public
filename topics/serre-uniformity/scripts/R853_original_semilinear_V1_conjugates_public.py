#!/usr/bin/env python3
"""Standard-library source transport and result reader for the three R853 RHS."""

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
import traceback


S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R853-three-V1-conjugates-public-request.json"
RESULT = "R853-original-semilinear-V1-generator-conjugates"
FINAL = "p41-original-semilinear-V1-conjugates-certificate.json"
PREFIX = "R853-"
STAGES = "R853-stage-manifest.json.gz"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R853-retained-original-inputs.tar.gz"
INVENTORY = "R853-original-source-inventory.json"
INPUT_RECEIPT = "R853-retained-inputs-receipt.json"
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
PROOFS = ("proof", "descent_proof", "affine_proof", "method")
H64 = re.compile(r"[0-9a-f]{64}")
DECIMAL = re.compile(r"-?(0|[1-9][0-9]*)")
EPS = [0] + [1] * 144 + [2] * 127
TARGETS = ["tau", "sigma", "w0"]
MINOR = "R837-original-V1-reflection-minor.json.gz"
ATTEMPT = "R837-original-V1-reflection-minor-prime-index-0000.json.gz"
ACCEPTED = "R806-accepted-primitive-candidate.json.gz"
DEFINITION = "R806-candidate-0000000000-definition.json.gz"
MULTIPLIER = "R806-exact-polynomial-multiplier-in-original-normal-basis.json.gz"
FREE_BASIS = {"file": "R805-graded-free-basis.json.gz", "bytes": 11649,
              "sha256": "74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9"}
SOURCE_DEFINITIONS = {
    "R786": {"result": "R786-exact-original-power5-short-basis",
        "core_sha256": "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "certificate": "p41-exact-original-power5-short-basis-certificate.json",
        "stage_manifest": "R786-exact-stages-manifest.json.gz"},
    "R837": {"result": "R837-original-fixed-branch-pencil",
        "core_sha256": "5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924",
        "certificate": "p41-original-fixed-branch-pencil-certificate.json",
        "stage_manifest": "R837-stage-manifest.json.gz"},
    "R806": {"result": "R806-original-primitive-multiplication",
        "core_sha256": "b014f9b3cb4923421e6a879eddb4da58dd0baefb28d61a2191f6b0a33e51810d",
        "certificate": "p41-original-primitive-multiplication-certificate.json",
        "stage_manifest": "R806-stage-manifest.json.gz"},
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    tmp.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name and name not in (".", "..")
    assert "\\" not in name
    return name


def plain(value):
    row = {key: value[key] for key in ("file", "bytes", "sha256")}
    safe_name(row["file"])
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert H64.fullmatch(row["sha256"])
    return row


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(directory, value):
    value = plain(value)
    path = Path(directory) / value["file"]
    assert file_spec(path) == value, ("Changed original bytes", value["file"])
    return path


def topic_path(value):
    value = PurePosixPath(value)
    assert not value.is_absolute() and ".." not in value.parts
    result = (TOPIC / str(value)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def source_identity(item):
    return {key: item[key] for key in BASE_KEYS}


def math_names(label):
    if label == "R786":
        return ["R786-exact-power-1-row-" + str(i).zfill(4) + ".json.gz" for i in range(146)]
    if label == "R837":
        return [MINOR, ATTEMPT]
    assert label == "R806"
    return [ACCEPTED, MULTIPLIER, DEFINITION]


def selected_names(label):
    definition = SOURCE_DEFINITIONS[label]
    return sorted(set([MANIFEST, "run-receipt.json", "core-receipt.json", "public-actions-input.json",
                       definition["certificate"], definition["stage_manifest"]] + math_names(label)))


def load_transport(item):
    """Call frozen, standard-library R837 transport functions without rebinding them."""
    path = S / safe_name(item["transport_helper"])
    assert path.name == "R837_original_branch_pencil_public.py"
    assert sha(path) == item["transport_helper_sha256"] == TRANSPORT_SHA
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    spec = importlib.util.spec_from_file_location("R853_frozen_R837_source_transport", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.load_io(item)
    return module


def guard(item, request):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R853 execution belongs to the public repository's Actions.")
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
    assert item["core"] == "R853_original_semilinear_V1_conjugates.py"
    assert item["wrapper"] == "R853_original_semilinear_V1_conjugates_public.py"
    assert sha(S / item["core"]) == item["core_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300
    for key in PROOFS:
        assert sha(topic_path(item[key])) == item[key + "_sha256"]
    assert sha(REPO / "README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC / "README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(SOURCE_DEFINITIONS)
    for label, source in item["sources"].items():
        definition = SOURCE_DEFINITIONS[label]
        assert source["result"] == definition["result"] and source["core_sha256"] == definition["core_sha256"]
        assert source["expected_conclusion"] == "success"
        assert source["selected_file_count"] == len(selected_names(label))
        assert set(source["selected_math_files"]) == set(math_names(label))
        assert H64.fullmatch(source["selected_files_sha256"])
        assert H64.fullmatch(source["configuration_sha256"])
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
        for key in ("certificate", "stage_manifest"):
            assert plain(source[key])["file"] == definition[key]
    return load_transport(item)


def source_review(label, item, directory):
    """Only source bytes, original completion/configuration, and actual schemas."""
    directory = Path(directory)
    source = item["sources"][label]
    definition = SOURCE_DEFINITIONS[label]
    manifest_path = directory / MANIFEST
    assert manifest_path.stat().st_size == source["manifest_bytes"]
    assert sha(manifest_path) == source["manifest_sha256"]
    manifest = read(manifest_path)
    assert manifest["result"] == source["result"]
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    entries[MANIFEST] = file_spec(manifest_path)
    names = selected_names(label)
    selected = {name: entries[name] for name in names}
    for row in selected.values():
        bound(directory, row)
    assert fingerprint([selected[name] for name in sorted(selected)]) == source["selected_files_sha256"]
    certificate = read(bound(directory, source["certificate"]))
    assert certificate["result"] == source["result"] and certificate["complete"] is True
    tag = certificate["configuration"]
    assert tag["result"] == source["result"] and tag["source_sha256"] == source["core_sha256"]
    assert fingerprint(tag) == source["configuration_sha256"]
    initial = read(directory / "public-actions-input.json")
    run = read(directory / "run-receipt.json")
    core = read(directory / "core-receipt.json")
    assert initial["result"] == run["result"] == core["result"] == source["result"]
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and run.get("error") is None
    assert core["complete"] is True and core["certificate_sha256"] == source["certificate"]["sha256"]
    assert run["core_receipt_sha256"] == selected["core-receipt.json"]["sha256"]
    stage_manifest = read(bound(directory, source["stage_manifest"]))
    assert stage_manifest["complete"] is True and stage_manifest["configuration"] == tag
    stages = {row["file"]: plain(row) for row in stage_manifest["files"]}
    assert len(stages) == len(stage_manifest["files"])
    assert all(entries[name] == row for name, row in stages.items())
    data = {}
    for name in math_names(label):
        assert selected[name] == stages[name]
        value = read(directory / name)
        assert value["complete"] is True and value["configuration"] == tag
        assert value.get("result", tag["result"]) == source["result"]
        data[name] = value
    if label == "R786":
        assert certificate["exact_power5_basis_dimension"] == 1234
        assert certificate["exact_K_basis_prefix_bound_qY"] == 128
        assert certificate["all_original_R775_mod739_short_series_compared"] is True
        assert plain(certificate["stages_manifest"]) == plain(source["stage_manifest"])
        for name in math_names(label):
            row = data[name]
            assert row["weight"] == 2 and row["bound_qY"] == 128 and row["integer_scale"] == "6724"
            assert row["original_R775_finite_coefficients_verified"] is True
            assert row["recipe"]["kind"] == "det_semilinear_E1_pair_trace"
            assert row["recipe"]["exact_global_field"] == "K"
            assert len(row["integer_qY_xi_coefficients"]) == 129
            assert all(len(x) == 40 for x in row["integer_qY_xi_coefficients"])
    elif label == "R837":
        minor, attempt = data[MINOR], data[ATTEMPT]
        assert plain(minor["successful_attempt"]) == selected[ATTEMPT]
        assert minor["matrix_shape"] == [560, 146]
        assert minor["actual_modular_rank"] == minor["expected_characteristic_zero_rank"] == 146
        assert minor["selected_columns"] == list(range(146))
        assert len(minor["selected_rows"]) == len(set(minor["selected_rows"])) == 146
        assert all(isinstance(i, int) and 0 <= i < 560 for i in minor["selected_rows"])
        assert minor["minor_determinant_mod_prime"] != 0
        for key in ("matrix_shape", "actual_modular_rank", "selected_rows", "selected_columns",
                    "prime", "prime_index", "minor_determinant_mod_prime"):
            assert minor[key] == attempt[key]
        assert source_identity(tag["sources"]["R786"]) == source_identity(item["sources"]["R786"])
    else:
        accepted, definition_value, multiplier = data[ACCEPTED], data[DEFINITION], data[MULTIPLIER]
        assert certificate["accepted_candidate"] == selected[ACCEPTED]
        assert certificate["polynomial_multiplier"] == selected[MULTIPLIER]
        assert accepted["candidate_definition"] == selected[DEFINITION]
        assert definition_value["recipe"] == {"kind": "original_M2", "index": 2}
        expected = [int(i == 2) for i in range(146)]
        assert [int(x) for x in definition_value["w0_original_M2_integer_coordinates"]] == expected
        assert [int(x) for x in accepted["w0_original_M2_integer_coordinates"]] == expected
        assert [int(x) for x in certificate["actual_w0_original_M2_integer_coordinates"]] == expected
        assert tag["original_tau_index"] == 0 and tag["actual_sigma_integer_n"] == 1
        assert tag["normal_affine_basis_degrees"] == EPS
        assert tag["R805_proof_sha256"] == item["affine_proof_sha256"]
        assert definition_value["original_integer_scale"] == "6724"
        assert accepted["original_function_field_primitive_generator_certified"] is True
        assert certificate["original_function_field_primitive_generator_certified"] is True
        assert plain(multiplier["original_R805_free_basis"]) == FREE_BASIS
        assert multiplier["all272_columns_verified_in_all820_original_rows"] is True
        assert len(multiplier["coordinate_groups"]) == 34
        for row in multiplier["coordinate_groups"] + [accepted["cyclic_witness"]]:
            p = plain(row)
            assert entries[p["file"]] == stages[p["file"]] == p
        assert source_identity(tag["retained_artifacts"]["R786"]) == source_identity(item["sources"]["R786"])
    return {**source_identity(source), "configuration_sha256": source["configuration_sha256"],
            "selected_files_sha256": source["selected_files_sha256"], "files": selected,
            "certificate": plain(source["certificate"]), "stage_manifest": plain(source["stage_manifest"])}


def bound_source_identity(source):
    return {**source_identity(source), "configuration_sha256": source["configuration_sha256"],
            "selected_files_sha256": source["selected_files_sha256"],
            "selected_file_count": len(source["files"]),
            "certificate": plain(source["certificate"]), "stage_manifest": plain(source["stage_manifest"])}


def expected_tag(item, sources):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "python_flint": "0.9.0", "p": 41,
        **{key + "_sha256": item[key + "_sha256"] for key in PROOFS},
        "sources": {label: bound_source_identity(sources[label]) for label in sorted(sources)},
        "original_V1_dimension": 146, "original_qY_prefix_orders": 14,
        "original_xi_coordinates_per_order": 40, "full_original_coordinate_rows": 560,
        "original_V1_integer_scale": "6724", "target_order": TARGETS,
        "original_tau_index": 0, "actual_sigma_integer_n": 1, "actual_w0_index": 2,
        "original_coefficient_field": "K=Q(s),s**2=-3;zeta=(-1+s)/2",
        "coefficient_c0_action": "s->-s,xi41->xi41; original integer xi coefficients fixed",
        "geometric_twist_action": "qY->-qY, even-weight automorphy factor1",
        "matrix_convention": "row40*n+r, original V1 column i; A*C=sign(n)*A*V",
        "original_normal_free_basis": FREE_BASIS, "normal_basis_degrees": EPS,
        "new_exact_right_hand_side_count": 3,
        "old_reflection_minor_recomputed": False, "old_Fourier_or_CM_values_recomputed": False,
        "full_normal_involution_matrix_computed": False,
        "budget_and_absolute_directories_excluded_from_mathematical_identity": True,
    }


def prepare_sources(item, out, transport, allow_download=True):
    out = Path(out)
    retained = out.parent / "retained-original-R853"
    retained.mkdir(parents=True, exist_ok=True)
    receipt_path, inventory_path = out / INPUT_RECEIPT, out / INVENTORY
    if receipt_path.exists() and inventory_path.exists() and (out / BUNDLE).exists():
        receipt, inventory = read(receipt_path), read(inventory_path)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is True and inventory["complete"] is True
        assert receipt["sources"] == item["sources"]
        bound(out, receipt["source_inventory"])
        bound(out, receipt["source_bundle"])
        count = transport.unpack_sources(out / BUNDLE, retained, inventory)
        reviewed = {label: source_review(label, item, retained / label) for label in sorted(SOURCE_DEFINITIONS)}
        assert reviewed == inventory["sources"]
        assert count == receipt["minimal_bundle_member_count"] == 169
        return retained, receipt, reviewed
    assert allow_download, "The completed original source carrier is required for verification"
    reviewed, receipts = {}, {}
    for label in sorted(SOURCE_DEFINITIONS):
        source = item["sources"][label]
        directory = retained / label
        directory.mkdir(parents=True, exist_ok=True)
        print("R853_SOURCE_START=" + label, flush=True)
        archive = transport.IO.Archive(source, out.parent / ("download-R853-" + label), whole=False)
        try:
            archive.extract_bound(MANIFEST, source["manifest_sha256"], directory / MANIFEST, source["manifest_bytes"])
            manifest = read(directory / MANIFEST)
            assert manifest["result"] == source["result"]
            entries = {row["file"]: plain(row) for row in manifest["files"]}
            assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
            assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
            for name, row in entries.items():
                assert len(archive.by_name[name]) == 1 and archive.by_name[name][0].file_size == row["bytes"]
            archive.extract_many([(name, entries[name]["sha256"], directory / name, entries[name]["bytes"])
                                  for name in selected_names(label) if name != MANIFEST])
            reviewed[label] = source_review(label, item, directory)
            receipts[label] = archive.receipt()
            print("R853_SOURCE_COMPLETE=" + json.dumps({"label": label, "selected_files": len(reviewed[label]["files"]),
                  "selected_files_sha256": reviewed[label]["selected_files_sha256"]}, sort_keys=True), flush=True)
        finally:
            archive.close()
    inventory = {"result": RESULT, "complete": True, "sources": reviewed,
                 "all_entries_are_unchanged_completed_original_source_bytes": True}
    save(inventory_path, inventory)
    transport.pack_sources(retained, inventory, out / BUNDLE)
    count = sum(len(value["files"]) for value in reviewed.values())
    assert count == 169
    receipt = {"result": RESULT, "complete": True, "sources": item["sources"],
               "source_inventory": file_spec(inventory_path), "source_bundle": file_spec(out / BUNDLE),
               "minimal_bundle_member_count": count, "range_transport": receipts,
               "old_Fourier_CM_rank_or_multiplier_arithmetic_recomputed": False}
    save(receipt_path, receipt)
    print("R853_INPUT_REVIEW=" + json.dumps({"selected_original_files": count,
          "source_inventory": receipt["source_inventory"], "source_bundle": receipt["source_bundle"],
          "new_mathematics_executed_in_source_preparation": False}, sort_keys=True), flush=True)
    return retained, receipt, reviewed


def stable_job(item):
    return {key: value for key, value in item.items() if key not in (
        "resume", "budget_minutes", "readme_sha256", "rules_last_read_commit", "wrapper_sha256", "workflow")}


def restore(item, out, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    meta = out.parent / "resume-R853-metadata"
    meta.mkdir(parents=True, exist_ok=True)
    archive = transport.IO.Archive(resume, out.parent / "download-R853-continuation", whole=False)
    try:
        archive.extract_bound(MANIFEST, resume["manifest_sha256"], meta / MANIFEST, resume["manifest_bytes"])
        manifest = read(meta / MANIFEST)
        assert manifest["result"] == RESULT
        entries = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == resume["manifest_file_count"]
        assert set(archive.by_name) == set(entries) | {MANIFEST, REFERENCE}
        for name in ("run-receipt.json", "public-actions-input.json", "core-receipt.json", INPUT_RECEIPT, INVENTORY, BUNDLE):
            if name == "core-receipt.json" and name not in entries:
                continue
            row = entries[name]
            destination = out / name if name in (INPUT_RECEIPT, INVENTORY, BUNDLE) else meta / name
            archive.extract_bound(name, row["sha256"], destination, row["bytes"])
        run, initial = read(meta / "run-receipt.json"), read(meta / "public-actions-input.json")
        assert run["result"] == initial["result"] == RESULT
        assert str(run["workflow_run_id"]) == str(resume["run_id"])
        assert run["source_commit"] == initial["source_commit"] == resume["source_commit"]
        assert initial["core_sha256"] == item["core_sha256"]
        assert stable_job(initial["job"]) == stable_job(item)
        assert run["process_exit_code"] in resume["accepted_process_exit_codes"]
        core = None
        if "core-receipt.json" in entries:
            core = read(meta / "core-receipt.json")
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        unused, receipt, sources = prepare_sources(item, out, transport, allow_download=False)
        tag = expected_tag(item, sources)
        names = sorted(name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz"))
        archive.extract_many([(name, entries[name]["sha256"], out / name, entries[name]["bytes"]) for name in names])
        for name in names:
            value = read(out / name)
            assert value["configuration"] == tag and value["complete"] is True
        restored_success = False
        if FINAL in entries:
            row = entries[FINAL]
            archive.extract_bound(FINAL, row["sha256"], meta / FINAL, row["bytes"])
            final = read(meta / FINAL)
            assert final["configuration"] == tag
            # An old incomplete FINAL is a historical receipt, not a current-stage constraint.
            if final["complete"] is True:
                assert run["complete"] is True and run["process_exit_code"] == 0
                assert core is not None and core["complete"] is True
                assert core["certificate_sha256"] == row["sha256"]
                assert final["original_three_V1_conjugates_certified"] is True
                assert final["original_semilinear_function_field_generator_action_certified"] is True
                for key in ("source_audit", "three_conjugate_coordinates", "function_field_action_DAG", "stage_manifest"):
                    assert entries[final[key]["file"]] == plain(final[key])
                    bound(out, final[key])
                shutil.copyfile(meta / FINAL, out / FINAL)
                restored_success = True
        save(out / "resume-inheritance-receipt.json", {"result": RESULT, "complete": True,
             "source_resume": resume, "original_manifest": file_spec(meta / MANIFEST),
             "all_restored_complete_stages": [entries[name] for name in names],
             "restored_successful_final": restored_success, "range_transport": archive.receipt(),
             "completed_exact_conjugates_not_recomputed": True})
    finally:
        archive.close()


def output_manifest(out):
    entries = [dict(file_spec(path), included_in_git=False) for path in sorted(out.iterdir())
               if path.is_file() and path.name not in (MANIFEST, REFERENCE)
               and not path.name.endswith((".tmp", ".download"))]
    save(out / MANIFEST, {"result": RESULT, "files": entries,
         "temporary_active_checkpoint_retention_days": 1, "reproducible_data_in_git_or_release": False})
    save(out / REFERENCE, {"result": RESULT, "manifest_file": MANIFEST,
         "manifest_sha256": sha(out / MANIFEST), "manifest_bytes": (out / MANIFEST).stat().st_size,
         "file_count": len(entries)})


def compute(item, out, request, transport):
    out.mkdir(parents=True, exist_ok=True)
    process, exitcode, error, outer_timeout = None, 1, None, False
    try:
        restore(item, out, transport)
        retained, receipt, sources = prepare_sources(item, out, transport)
        expanded = dict(item)
        expanded["sources"] = {label: {**value, "directory": str((retained / label).resolve())}
                               for label, value in sources.items()}
        for key in PROOFS:
            expanded[key] = str(topic_path(item[key]))
        save(out / "public-actions-expanded-job.json", expanded)
        initial = {"result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
            "source_commit": os.environ["GITHUB_SHA"], "job": item, "request_sha256": sha(request),
            "driver_sha256": sha(__file__), "core_sha256": item["core_sha256"],
            **{key + "_sha256": item[key + "_sha256"] for key in PROOFS},
            "transport_helper_sha256": TRANSPORT_SHA, "io_helper_sha256": RANGE_SHA,
            "workflow_sha256": sha(REPO / item["workflow"]),
            "root_readme_sha256": sha(REPO / "README.md"), "topic_readme_sha256": sha(TOPIC / "README.md"),
            "source_inventory": receipt["source_inventory"],
            "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "all_new_mathematics_runs_only_in_separate_public_Actions_core": True}
        save(out / "public-actions-input.json", initial)
        command = [sys.executable, str(S / item["core"]), "--config", str(out / "public-actions-expanded-job.json"),
                   "--out", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out / "public-actions-run.log").open("w", encoding="utf-8") as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                exitcode = process.wait(timeout=item["budget_minutes"] * 60 + 900)
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                exitcode = 124
    except BaseException as exc:
        error = type(exc).__name__ + ": " + str(exc)
        traceback.print_exc()
        if process is not None and process.poll() is None:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
        exitcode = 1
    finally:
        core_path = out / "core-receipt.json"
        core = read(core_path) if core_path.exists() else None
        final = read(out / FINAL) if (out / FINAL).exists() else None
        complete = exitcode == 0 and core is not None and core.get("complete") is True \
            and final is not None and final.get("complete") is True \
            and final.get("original_three_V1_conjugates_certified") is True \
            and final.get("original_semilinear_function_field_generator_action_certified") is True
        run = {"result": RESULT, "p": 41, "complete": complete, "process_exit_code": exitcode, "error": error,
            "core_receipt_sha256": sha(core_path) if core_path.exists() else None,
            "source_commit": os.environ.get("GITHUB_SHA"), "workflow_run_id": os.environ.get("GITHUB_RUN_ID"),
            "workflow_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "execution_environment": "public-repository-github-actions", "outer_timeout": outer_timeout,
            "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out / "run-receipt.json", run)
        output_manifest(out)
        print("R853_RUN_RECEIPT=" + json.dumps(run, sort_keys=True), flush=True)
    return exitcode


def rational_shape(value):
    assert isinstance(value, list) and len(value) == 2
    assert all(isinstance(x, str) and DECIMAL.fullmatch(x) for x in value)
    assert int(value[1]) > 0


def verify(item, out, request, transport):
    manifest = read(out / MANIFEST)
    assert manifest["result"] == RESULT
    entries = {row["file"]: plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for row in entries.values():
        bound(out, row)
    reference = read(out / REFERENCE)
    assert reference["result"] == RESULT and reference["manifest_sha256"] == sha(out / MANIFEST)
    assert reference["manifest_bytes"] == (out / MANIFEST).stat().st_size and reference["file_count"] == len(entries)
    run = read(out / "run-receipt.json")
    if not run.get("complete"):
        print("R853_INCOMPLETE_IO_REVIEW=" + json.dumps({"complete": False, "run": run,
            "manifest_files": len(entries), "no_partial_stage_is_claimed_as_complete_conjugates": True}, sort_keys=True), flush=True)
        return 2
    retained, receipt, sources = prepare_sources(item, out, transport, allow_download=False)
    initial, core, final = (read(out / name) for name in ("public-actions-input.json", "core-receipt.json", FINAL))
    assert initial["job"] == item and initial["request_sha256"] == sha(request)
    assert initial["source_commit"] == run["source_commit"]
    assert initial["driver_sha256"] == sha(__file__) and initial["core_sha256"] == item["core_sha256"]
    assert core["result"] == final["result"] == RESULT
    assert core["complete"] is True and final["complete"] is True and run["process_exit_code"] == 0
    assert core["source_sha256"] == item["core_sha256"]
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"] == entries[FINAL]["sha256"]
    tag = expected_tag(item, sources)
    assert final["configuration"] == tag
    for flag in ("original_three_V1_conjugates_certified", "original_semilinear_function_field_generator_action_certified"):
        assert final[flag] is True and core[flag] is True
    assert final["full_original_coordinate_rows"] == 560 and final["new_exact_right_hand_side_count"] == 3
    assert final["original_scales_preserved"] is True
    for flag in ("original_Fourier_CM_or_reflection_minor_arithmetic_recomputed",
                 "full146_or272_column_conjugation_matrix_computed", "new_RR_spaces_connections_periods_or_heights_computed"):
        assert final[flag] is False
    stage_spec = plain(final["stage_manifest"])
    assert stage_spec["file"] == STAGES and entries[STAGES] == stage_spec
    inventory = read(bound(out, stage_spec))
    assert inventory["complete"] is True and inventory["configuration"] == tag
    stages = {row["file"]: plain(row) for row in inventory["files"]}
    assert len(stages) == len(inventory["files"]) == 3
    for name, row in stages.items():
        assert entries[name] == row
        value = read(bound(out, row))
        assert value["complete"] is True and value["configuration"] == tag
    actual_math_names = {name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz") and name != STAGES}
    assert actual_math_names == set(stages)
    for key in ("source_audit", "three_conjugate_coordinates", "function_field_action_DAG"):
        assert stages[final[key]["file"]] == plain(final[key])
    audit = read(bound(out, final["source_audit"]))
    coords = read(bound(out, final["three_conjugate_coordinates"]))
    dag = read(bound(out, final["function_field_action_DAG"]))
    assert audit["prefix_matrix_shape"] == [560, 146]
    assert audit["original_reflection_minor"] == sources["R837"]["files"][MINOR]
    assert len(audit["original_R786_prefix_rows"]) == 146
    for i, row in enumerate(audit["original_R786_prefix_rows"]):
        assert row == sources["R786"]["files"]["R786-exact-power-1-row-" + str(i).zfill(4) + ".json.gz"]
    assert coords["source_audit"] == final["source_audit"]
    assert coords["target_order"] == TARGETS and coords["coordinate_matrix_shape"] == [146, 3]
    assert coords["original_integer_scale"] == "6724"
    assert coords["all560_original_coordinates_verified_for_each_conjugate"] is True
    assert coords["full_verified_coordinate_count"] == 1680
    assert coords["all_three_original_conjugates_nonzero"] is True
    assert coords["twice_original_semilinear_action_verified_in_all560_coordinates"] is True
    matrix = coords["coordinates_in_original_integer_scaled_V1_basis"]
    assert len(matrix) == 146 and all(len(row) == 3 for row in matrix)
    for row in matrix:
        for value in row:
            rational_shape(value)
    assert dag["source_audit"] == final["source_audit"] and dag["exact_three_coordinates"] == final["three_conjugate_coordinates"]
    assert dag["original_normal_free_basis"] == FREE_BASIS
    for flag in ("entire_original_function_field_action_defined", "original_arithmetic_twist_not_coefficient_conjugation_alone",
                 "source_K_Y_equals_K_z_w_certified_by_original_R806", "all_three_normal_linear_transports_verified",
                 "three_K_z_w_unit_solve_expressions_source_bound"):
        assert dag[flag] is True
    assert dag["three_Krylov_coordinate_solves_executed"] is False
    assert dag["full272_column_involution_matrix_computed"] is False
    assert dag["Krylov_coordinate_or_multiplier_arithmetic_recomputed"] is False
    assert len(dag["normal_expressions"]) == 3
    for target, value in zip(TARGETS, dag["normal_expressions"]):
        assert value["target"] == target and value["normal_basis_rank"] == 272
        assert value["original_normal_free_basis"] == FREE_BASIS
        assert value["exact_reconstruction_in_original_V1_basis_verified"] is True
        assert value["extra_section_or_integer_scale_inserted"] is False
        assert value["sparse_normal_polynomial_terms"]
        positions = set()
        for term in value["sparse_normal_polynomial_terms"]:
            row, power = term["normal_basis_row"], term["power_of_z"]
            assert isinstance(row, int) and 0 <= row <= 144
            assert power in (0, 1) and (power == 0 or row == 0)
            assert (row, power) not in positions
            positions.add((row, power))
            rational_shape(term["coefficient_Q"])
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert len(nodes) == len(dag["nodes"]) == 16
    assert nodes["original_W"]["producer"] == source_identity(sources["R806"])
    assert nodes["original_W"]["index"] == sources["R806"]["files"][MULTIPLIER]
    old_w = read(retained / "R806" / MULTIPLIER)
    old_accepted = read(retained / "R806" / ACCEPTED)
    assert nodes["original_W"]["exact_coordinate_groups"] == [plain(x) for x in old_w["coordinate_groups"]]
    assert nodes["original_Krylov"]["original_nonzero_cyclic_witness"] == plain(old_accepted["cyclic_witness"])
    for target in TARGETS:
        assert nodes["power_coordinates_" + target]["operation"] == "unit_matrix_solve"
        assert nodes["power_coordinates_" + target]["evaluation_deferred"] is True
    assert dag["constant_field_action"] == {"s": "-s", "zeta": "-1-zeta", "rationals": "fixed"}
    print("R853_COMPLETE_IO_REVIEW=" + json.dumps({"result": RESULT, "certificate": entries[FINAL],
        "stage_manifest": stage_spec, "complete_math_stages": len(stages), "manifest_files": len(entries),
        "original_three_V1_conjugates_certified": True,
        "original_semilinear_function_field_generator_action_certified": True,
        "full_original_coordinate_rows": 560, "new_exact_right_hand_side_count": 3,
        "source_inventory": receipt["source_inventory"], "source_bundle": receipt["source_bundle"],
        "selected_original_files": receipt["minimal_bundle_member_count"], "seconds": final["seconds"],
        "all_output_and_selected_source_bytes_verified": True, "mathematics_reexecuted_by_wrapper": False}, sort_keys=True), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    item = read(REQUEST)
    transport = guard(item, REQUEST)
    return verify(item, args.output, REQUEST, transport) if args.verify else compute(item, args.output, REQUEST, transport)


if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    raise SystemExit(main())
