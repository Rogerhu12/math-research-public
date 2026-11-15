#!/usr/bin/env python3
"""R795: retain completed factors and compute only the missing power6 prefix."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tarfile

from p41_public_actions_recovery import publish, read, save, sha
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R795-public-exact-power6-short-basis-request.json"
RESULT = "R795-exact-original-power6-short-basis"
FINAL = "p41-exact-original-power6-short-basis-certificate.json"
INPUT_BUNDLE = "R795-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R775", "R786"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
R775_POWER6 = "R775-basis-power-6.json.gz"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def bound_path(directory, entries, name):
    assert Path(name).name == name
    row = entries[name]
    path = find_hash(directory, name, row["sha256"])
    assert path.stat().st_size == row["bytes"]
    return path


def producer_metadata(directory, spec):
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == spec["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    paths = {"full-outputs-manifest.json": mp}
    for name in PRODUCER_META[1:]:
        paths[name] = bound_path(directory, entries, name)
    run, core, initial = (read(paths[name]) for name in PRODUCER_META[1:])
    assert run["result"] == spec["result"] and run["complete"] is True
    assert run["process_exit_code"] == 0
    assert str(run["workflow_run_id"]) == str(spec["run_id"])
    assert run["source_commit"] == spec["source_commit"]
    assert run["core_receipt_sha256"] == sha(paths["core-receipt.json"])
    assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
    assert initial["result"] == spec["result"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == spec["source_commit"]
    assert initial["core_sha256"] == spec["core_sha256"]
    name = spec["certificate_name"]
    assert entries[name]["sha256"] == spec["files"][name] == core["certificate_sha256"]
    paths[name] = bound_path(directory, entries, name)
    cert = read(paths[name])
    assert cert["complete"] is True and cert["result"] == spec["result"]
    assert cert["configuration"]["source_sha256"] == spec["core_sha256"]
    assert cert["configuration"]["python_flint"] == "0.9.0"
    return entries, paths, cert


def selected_group_files(directory, label, spec, power6=None):
    entries, paths, cert = producer_metadata(directory, spec)
    selected = dict(spec["files"])
    if label == "R775":
        assert cert["power_basis_dimensions"]["6"] == 1506
        assert cert["all_recipes_defined_over_original_K"] is True
        stages = {row["file"]: row for row in cert["stages"]}
        assert stages[R775_POWER6]["sha256"] == selected[R775_POWER6]
        assert stages[R775_POWER6]["bytes"] == entries[R775_POWER6]["bytes"]
    else:
        assert label == "R786" and power6 is not None
        assert cert["basis_in_original_R775_saved_order"] is True
        assert cert["exact_power5_basis_dimension"] == 1234
        assert cert["exact_K_basis_prefix_bound_qY"] == 128
        for key in ("basis_index", "stages_manifest"):
            row = cert[key]
            assert entries[row["file"]]["bytes"] == row["bytes"]
            assert selected[row["file"]] == row["sha256"]
        inventory = read(bound_path(directory, entries, cert["stages_manifest"]["file"]))
        assert inventory["complete"] is True and inventory["configuration"] == cert["configuration"]
        old_rows = {row["file"]: row for row in inventory["files"]}
        assert len(power6["basis"]) == 1506 and power6["rank"] == 1506
        for original in power6["basis"]:
            recipe = original["recipe"]
            assert recipe["kind"] == "product"
            assert recipe["left_power"] == 1 and recipe["right_power"] == 5
            for side in ("left", "right"):
                power, index = recipe[side+"_power"], recipe[side+"_index"]
                assert 0 <= index < (146 if power == 1 else 1234)
                name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
                assert old_rows[name]["bytes"] == entries[name]["bytes"]
                assert old_rows[name]["sha256"] == entries[name]["sha256"]
                selected[name] = old_rows[name]["sha256"]
    for name, digest in selected.items():
        assert entries[name]["sha256"] == digest
        path = bound_path(directory, entries, name)
        if name != spec["certificate_name"]:
            data = read(path)
            assert data["complete"] is True and data["configuration"] == cert["configuration"]
            if label == "R786" and re.fullmatch(r"R786-exact-power-[15]-row-\d{4}\.json\.gz", name):
                assert data["bound_qY"] == 128
                assert data["weight"] in (2, 10)
                assert data["integer_scale"] == {2: "6724", 10: "13744803133596058624"}[data["weight"]]
                assert data["original_R775_finite_coefficients_verified"] is True
        paths[name] = path
    return paths, cert


def transfer(paths, target):
    target.mkdir(parents=True, exist_ok=True)
    for name, path in paths.items():
        destination = target/name
        if path.resolve() == destination.resolve():
            continue
        if destination.exists():
            assert sha(destination) == sha(path)
        else:
            shutil.copyfile(path, destination)


def prepare_inputs(item, out):
    assert set(item["retained_artifacts"]) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified input bundle"
    groups, power6, cert775 = [], None, None
    for label in ("R775", "R786"):
        spec = item["retained_artifacts"][label]
        target = inputs/label
        if not transferred:
            directory = out.parent/("downloaded-"+label)
            download(spec, directory, require_complete=True)
            paths, _ = selected_group_files(directory, label, spec, power6)
            transfer(paths, target)
        paths, cert = selected_group_files(target, label, spec, power6)
        assert set(path.name for path in target.iterdir() if path.is_file()) == set(paths)
        if label == "R775":
            power6 = read(target/R775_POWER6)
            cert775 = cert
        else:
            stages775 = {row["file"]: row for row in cert775["stages"]}
            old = cert["configuration"]["R775_completed_prefix_producer"]
            for name in ("R775-basis-M2.json.gz", "R775-basis-power-5.json.gz"):
                assert old["files"][name] == stages775[name]["sha256"]
        groups.append({"label": label, "producer": spec, "file_count": len(paths),
            "all_sizes_sha256_and_original_schemas_verified": True})
    save(out/"retained-inputs-receipt.json", {"groups": groups,
        "all_inputs_from_verified_R795_active_bundle": transferred,
        "only_power6_recipes_and_their_completed_power1_power5_factors_retained": True,
        "old_arithmetic_recomputed": False})
    if not (out/INPUT_BUNDLE).exists():
        with tarfile.open(out/INPUT_BUNDLE, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=str(path.relative_to(inputs)), recursive=False)
    return inputs


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0"
    assert tag["R793_proof_sha256"] == item["R793_proof_sha256"]
    assert tag["R795_method_sha256"] == item["R795_method_sha256"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]
    assert tag["p"] == 41 and tag["level"] == 82
    assert tag["ordinary_power"] == item["ordinary_power"] == 6
    assert tag["ordinary_power_dimension"] == item["ordinary_power_dimension"] == 1506
    assert tag["basis_bound_qY"] == item["basis_bound_qY"] == 81
    assert tag["basis_integer_scale"] == str(82**12)
    assert tag["new_E1_or_old_power1_to5_arithmetic"] is False


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    return label == "R786" and bool(re.fullmatch(r"R786-exact-power-[15]-row-\d{4}\.json\.gz", name))


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R795-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    initial = read(bound_path(directory, entries, "public-actions-input.json"))
    assert initial["source_commit"] == spec["source_commit"]
    for name in ("result", "core_sha256", "R793_proof_sha256", "R795_method_sha256",
                 "ordinary_power", "ordinary_power_dimension", "basis_bound_qY", "retained_artifacts"):
        assert initial["job"][name] == item[name], "Changed continuation input: "+name
    bundle = bound_path(directory, entries, INPUT_BUNDLE)
    target = out.parent/"retained"
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in LABELS
            group, name = relative.parts
            assert allowed_group_name(group, item["retained_artifacts"][group], name)
            path = target/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            data = archive.extractfile(member).read()
            if path.exists():
                assert path.read_bytes() == data
            else:
                path.write_bytes(data)
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    copied = 0
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R795-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound_path(directory, entries, name)
        data = read(source)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
        shutil.copyfile(source, out/name)
        copied += 1
    save(out/"resume-receipt.json", {"producer": spec,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": copied,
        "verified_minimal_two_group_input_bundle_restored": True,
        "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path),
                     "artifact": artifact,
                     "included_in_git": path.name in META and path.stat().st_size < 100_000})
    path = out/"full-outputs-manifest.json"
    save(path, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_exact_basis_rows_or_certificates_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": path.name,
        "manifest_sha256": sha(path), "manifest_bytes": path.stat().st_size,
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": path.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method, proof = S/item["core"], topic_path(item["method"]), topic_path(item["proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "method_sha256": sha(method),
        "proof_sha256": sha(proof), "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "download_helper_sha256": sha(S/"R786_public_exact_power5_short_basis.py"),
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "only original power6 qY0..81; completed power1/5 factors consumed",
        "multiplication_table_polar_divisor_beta_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"]
        assert sha(method) == item["R795_method_sha256"] and sha(proof) == item["R793_proof_sha256"]
        assert item["ordinary_power"] == 6 and item["ordinary_power_dimension"] == 1506
        assert item["basis_bound_qY"] == 81
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--method", str(method), "--proof", str(proof), "--retained", str(inputs),
            "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed new rows and exact old factors retained for immediate continuation."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    rp = out/"core-receipt.json"
    receipt = read(rp) if rp.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(rp) if rp.exists() else None,
        "actual_original_power6_q0_to81_completed": complete,
        "old_power1_to5_recomputed": False,
        "actual_multiplication_table_polar_divisor_beta_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True and run["process_exit_code"] == 0
    rp = out/"core-receipt.json"
    assert sha(rp) == run["core_receipt_sha256"]
    receipt = read(rp)
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["p"] == 41
    matching_configuration(cert["configuration"], item)
    assert cert["ordinary_power"] == 6 and cert["exact_power6_basis_dimension"] == 1506
    assert cert["exact_K_basis_prefix_bound_qY"] == 81 and cert["basis_integer_scale"] == str(82**12)
    for name in ("basis_in_original_R775_saved_order", "all_original_R775_mod739_short_series_compared",
                 "all_original_real_cyclotomic_transports_verified"):
        assert cert[name] is True
    for name in ("old_E1_M2_power1_to5_or_Laurent_recomputed", "coefficients_after_qY81_generated",
                 "actual_multiplication_table_polar_divisor_beta_eta_or_height_computed"):
        assert cert[name] is False
    spec = cert["stage_manifest"]
    assert Path(spec["file"]).name == spec["file"]
    path = out/spec["file"]
    assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
    manifest = read(path)
    matching_configuration(manifest["configuration"], item)
    assert manifest["complete"] is True
    nested = {row["file"]: row for row in manifest["files"]}
    assert len(nested) == len(manifest["files"]) == 1507
    for name, row in nested.items():
        assert Path(name).name == name
        path = out/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        data = read(path)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
    index_spec = cert["basis_index"]
    assert nested[index_spec["file"]] == index_spec
    index = read(out/index_spec["file"])
    assert index["dimension"] == 1506 and index["ordinary_power"] == 6 and index["bound_qY"] == 81
    assert index["integer_scale"] == str(82**12) and index["basis_selection_recomputed"] is False
    assert [row["index"] for row in index["basis_rows"]] == list(range(1506))
    for position, row in enumerate(index["basis_rows"]):
        name = "R795-exact-power-6-row-"+str(position).zfill(4)+".json.gz"
        assert row["file"] == name
        assert row["sha256"] == nested[name]["sha256"] and row["bytes"] == nested[name]["bytes"]
        data = read(out/name)
        assert data["index"] == position and data["weight"] == 12 and data["bound_qY"] == 81
        assert data["integer_scale"] == str(82**12)
        assert len(data["integer_qY_xi_coefficients"]) == len(data["integer_v_t_coefficients"]) == 82
        assert all(len(values) == 40 for values in data["integer_qY_xi_coefficients"])
        assert all(len(values) == 20 for values in data["integer_v_t_coefficients"])
        assert data["original_R775_finite_coefficients_verified"] is True
        assert data["all_original_phase_involutions_verified"] is True
        assert data["averaging_used"] is False and data["old_factor_rows_recomputed"] is False
        assert data["coefficients_after_qY81_generated"] is False
    return 0


def publish_small(item, out):
    if not (out/"full-outputs-manifest.json").exists():
        output_manifest(out)
    manifest = read(out/"full-outputs-manifest.json")
    pub = out.parent/"publication"
    pub.mkdir(parents=True, exist_ok=True)
    for row in manifest["files"]:
        if row["included_in_git"]:
            assert sha(out/row["file"]) == row["sha256"]
            shutil.copyfile(out/row["file"], pub/row["file"])
    shutil.copyfile(out/REFERENCE, pub/REFERENCE)
    if (out/"full-outputs-manifest.json").stat().st_size < 100_000:
        shutil.copyfile(out/"full-outputs-manifest.json", pub/"full-outputs-manifest.json")
    return publish(item, pub, artifact_prefix="serre-global")


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "publish", "verify"])
    mode = parser.parse_args().mode
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    return publish_small(item, out) if mode == "publish" else verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
