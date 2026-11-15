#!/usr/bin/env python3
"""R792 runner: minimum certified inputs from active producer bundles."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
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
REQUEST = TOPIC/"notes/R792-public-original-beta-composition-request.json"
RESULT = "R792-original-beta-composition"
FINAL = "p41-original-beta-composition-certificate.json"
INPUT_BUNDLE = "R792-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R735", "R775", "R786", "R787", "R790", "R791"}
DIRECT = ("R787", "R790", "R791")
PARENT_BUNDLES = {"R787": "R787-retained-producer-inputs.tar.gz",
                  "R790": "R790-retained-producer-inputs.tar.gz"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def same_producer(left, right):
    for key in ("result", "run_id", "source_commit", "core_sha256",
                "manifest_sha256", "certificate_name"):
        assert left[key] == right[key], "Changed producer identity: "+key
    name = left["certificate_name"]
    assert left["files"][name] == right["files"][name]


def bound_path(directory, entries, name):
    assert Path(name).name == name
    row = entries[name]
    path = find_hash(directory, name, row["sha256"])
    assert path.stat().st_size == row["bytes"]
    return path


def producer_metadata(directory, label, spec):
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
    assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
    assert initial["result"] == spec["result"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == spec["source_commit"]
    if label == "R791":
        assert "core_receipt_sha256" not in run
        assert initial["job"]["core_sha256"] == spec["core_sha256"]
    else:
        assert run["core_receipt_sha256"] == sha(paths["core-receipt.json"])
        assert initial["core_sha256"] == spec["core_sha256"]
    name = spec["certificate_name"]
    assert entries[name]["sha256"] == spec["files"][name] == core["certificate_sha256"]
    paths[name] = bound_path(directory, entries, name)
    certificate = read(paths[name])
    assert certificate["complete"] is True
    if label == "R735":
        identity = certificate["identity"]
        assert identity["source_sha256"] == spec["core_sha256"]
        assert identity["p"] == 41 and identity["python_flint"] == "0.9.0"
        assert certificate["original_b_not_a_replacement_twist"] is True
    else:
        assert certificate["result"] == spec["result"]
        tag = certificate["configuration"]
        assert tag["source_sha256"] == spec["core_sha256"] and tag["python_flint"] == "0.9.0"
    return entries, paths, certificate, initial


def selected_group_files(directory, label, spec):
    entries, paths, cert, initial = producer_metadata(directory, label, spec)
    selected = dict(spec["files"])
    if label == "R786":
        row = cert["basis_index"]
        assert row["file"] == "R786-exact-power5-basis-index.json.gz"
        assert entries[row["file"]]["bytes"] == row["bytes"]
        selected[row["file"]] = row["sha256"]
    elif label == "R787":
        assert cert["actual_y_map_recovered"] is True
        assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
        assert cert["exact_verified_orders"] == 129
        row = cert["relation_spec"]
        assert row["file"] == "R787-original-function-recipe.json.gz"
        assert entries[row["file"]]["bytes"] == row["bytes"]
        selected[row["file"]] = row["sha256"]
    elif label == "R790":
        assert cert["original_psi_values_and_first_coarse_jets_verified"] is True
        assert cert["M2_dimension"] == 146 and cert["cm_jet_order"] == 5
        assert cert["original_M2_scale"] == "6724"
        assert cert["R786_power5_product_scale"] == "13744803133596058624"
        row = cert["stage_manifest"]
        assert row["file"] == "R790-stage-manifest.json.gz"
        assert entries[row["file"]]["bytes"] == row["bytes"]
        selected[row["file"]] = row["sha256"]
        manifest = read(bound_path(directory, entries, row["file"]))
        assert manifest["complete"] is True and manifest["configuration"] == cert["configuration"]
        assert manifest["M2_output_rows"] == cert["M2_output_rows"]
        nested = {entry["file"]: entry for entry in manifest["files"]}
        assert len(cert["M2_output_rows"]) == 146
        for index, row in enumerate(cert["M2_output_rows"]):
            assert row["file"] == "R790-M2-CM-jet-"+str(index).zfill(4)+".json.gz"
            assert nested[row["file"]] == row
            assert entries[row["file"]]["bytes"] == row["bytes"]
            selected[row["file"]] = row["sha256"]
    stage_rows = {row["file"]: row for row in cert.get("stages", [])}
    for name, digest in selected.items():
        assert entries[name]["sha256"] == digest
        path = bound_path(directory, entries, name)
        if name != spec["certificate_name"]:
            data = read(path)
            assert data["complete"] is True and data["configuration"] == cert["configuration"]
            if label in ("R775", "R791"):
                assert stage_rows[name]["sha256"] == digest
            if label == "R787":
                assert data["candidate_only_until_full_exact_verification"] is False
                assert data["exact_original_A_equals_yB"] is True
                assert data["B_nonzero"] is True and data["full_129_original_relations_verified"] is True
            if label == "R790" and name.startswith("R790-M2-CM-jet-"):
                assert data["integer_scale"] == "6724" and data["R786_power1_scale_preserved"] is True
        paths[name] = path
    return paths, entries, cert, initial


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


def child_from_parent(parent_directory, parent_label, child_label, item, target):
    parent_spec = item["retained_artifacts"][parent_label]
    child_spec = item["retained_artifacts"][child_label]
    entries, paths, cert, initial = producer_metadata(parent_directory, parent_label, parent_spec)
    recorded = initial["job"]["retained_artifacts"][child_label]
    same_producer(recorded, child_spec)
    bundle_name = PARENT_BUNDLES[parent_label]
    bundle = bound_path(parent_directory, entries, bundle_name)
    wanted = set(PRODUCER_META)|set(child_spec["files"])
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert not relative.is_absolute() and ".." not in relative.parts
            if len(relative.parts) != 2 or relative.parts[0] != child_label:
                continue
            name = relative.parts[1]
            if name not in wanted:
                continue
            assert member.isfile()
            data = archive.extractfile(member).read()
            destination = target/name
            if destination.exists():
                assert destination.read_bytes() == data
            else:
                destination.write_bytes(data)
    # The old R787 bundle contains R786 manifest/cert/run/index but not these
    # two small producer receipts.  Reuse only their existing Git metadata.
    mp = target/"full-outputs-manifest.json"
    assert sha(mp) == child_spec["manifest_sha256"]
    child_entries = {row["file"]: row for row in read(mp)["files"]}
    for name, relative in child_spec.get("metadata_repository_paths", {}).items():
        assert child_label == "R786" and name in ("core-receipt.json", "public-actions-input.json")
        assert relative == "computations/R786-exact-original-power5-short-basis/"+\
            child_spec["run_id"]+"-1/"+name
        if not (target/name).exists():
            source = topic_path(relative)
            assert source.stat().st_size == child_entries[name]["bytes"]
            assert sha(source) == child_entries[name]["sha256"]
            shutil.copyfile(source, target/name)
    paths, _, _, _ = selected_group_files(target, child_label, child_spec)
    assert set(paths) == wanted
    return {"parent": parent_label, "child": child_label, "bundle": bundle_name,
            "parent_bundle_sha256": entries[PARENT_BUNDLES[parent_label]]["sha256"],
            "same_parent_recorded_run_source_core_manifest_and_certificate": True,
            "only_required_child_files_extracted": True,
            "small_original_repository_metadata_fallbacks": child_spec.get("metadata_repository_paths", {})}


def prepare_inputs(item, out):
    assert set(item["retained_artifacts"]) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified input bundle"
    source_records = []
    if not transferred:
        downloaded = {}
        for label in DIRECT:
            directory = out.parent/("downloaded-"+label)
            download(item["retained_artifacts"][label], directory, require_complete=True)
            paths, _, _, _ = selected_group_files(directory, label, item["retained_artifacts"][label])
            transfer(paths, inputs/label)
            downloaded[label] = directory
        for parent, child in (("R787", "R786"), ("R790", "R735"), ("R790", "R775")):
            source_records.append(child_from_parent(downloaded[parent], parent, child, item, inputs/child))
    groups = []
    for label in sorted(LABELS):
        paths, _, _, _ = selected_group_files(inputs/label, label, item["retained_artifacts"][label])
        assert set(path.name for path in (inputs/label).iterdir() if path.is_file()) == set(paths)
        groups.append({"label": label, "producer": item["retained_artifacts"][label],
                       "file_count": len(paths), "all_sizes_sha256_and_original_schemas_verified": True})
    # No old R735/R775/R786 artifact is requested.  The current active bundles
    # carry their exact completed inputs, even after those old artifacts expire.
    save(out/"retained-inputs-receipt.json", {"groups": groups,
        "direct_completed_artifact_labels": list(DIRECT), "parent_bundle_transfers": source_records,
        "all_inputs_from_verified_R792_active_bundle": transferred,
        "old_R735_R775_R786_artifacts_downloaded": False,
        "old_arithmetic_recomputed": False})
    if not (out/INPUT_BUNDLE).exists():
        with tarfile.open(out/INPUT_BUNDLE, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=str(path.relative_to(inputs)), recursive=False)
    return inputs


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["R792_proof_sha256"] == item["R792_proof_sha256"]
    assert tag["field_core_sha256"] == item["field_core_sha256"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]
    assert tag["coarse_jet_order"] == item["coarse_jet_order"] == 1
    assert tag["python_flint"] == "0.9.0"
    assert tag["original_map_index"] == 4 and tag["original_map_degree"] == "1206"


def allowed_group_names(label, spec):
    names = set(PRODUCER_META)|set(spec["files"])
    if label == "R786":
        names.add("R786-exact-power5-basis-index.json.gz")
    if label == "R787":
        names.add("R787-original-function-recipe.json.gz")
    if label == "R790":
        names.add("R790-stage-manifest.json.gz")
        names |= {"R790-M2-CM-jet-"+str(index).zfill(4)+".json.gz" for index in range(146)}
    return names


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R792-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    initial = read(bound_path(directory, entries, "public-actions-input.json"))
    assert initial["source_commit"] == spec["source_commit"]
    for name in ("result", "core_sha256", "R792_proof_sha256", "field_core_sha256",
                 "coarse_jet_order", "retained_artifacts"):
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
            assert name in allowed_group_names(group, item["retained_artifacts"][group])
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
        if not (name.startswith("R792-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound_path(directory, entries, name)
        data = read(source)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
        shutil.copyfile(source, out/name)
        copied += 1
    save(out/"resume-receipt.json", {"producer": spec,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": copied,
        "verified_minimal_six_group_input_bundle_restored": True,
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
        "reproducible_point_coordinates_or_certificates_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": path.name,
        "manifest_sha256": sha(path), "manifest_bytes": path.stat().st_size,
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": path.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, field_core = S/item["core"], S/item["field_core"]
    proof = topic_path(item["proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "field_core_sha256": sha(field_core),
        "proof_sha256": sha(proof), "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_beta_C_claimed_before_run": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"]
        assert sha(field_core) == item["field_core_sha256"]
        assert sha(proof) == item["R792_proof_sha256"]
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--proof", str(proof), "--field-core", str(field_core), "--retained", str(inputs),
            "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed source-bound stages and active inputs retained."
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
        "actual_beta_C_computed": complete and receipt.get("actual_beta_C_computed") is True,
        "needs_higher_common_zero_evaluation": receipt.get("needs_higher_common_zero_evaluation", False),
        "original_A_coordinate_lift_computed": False, "actual_heights_or_uniformity_computed": False,
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
    assert cert["result"] == RESULT and cert["complete"] is True
    matching_configuration(cert["configuration"], item)
    assert cert["p"] == 41 and cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["actual_beta_C_computed"] is True and cert["actual_real_descent_image_computed"] is True
    assert cert["original_A_coordinate_lift_computed"] is False
    assert cert["actual_heights_or_uniformity_computed"] is False
    assert cert["point_status"] in ("finite", "infinity") and cert["common_zero_order"] in (0, 1)
    assert cert["original_M2_scale"] == "6724" and cert["original_power5_scale"] == "13744803133596058624"
    assert cert["original_h0_nonzero"] is True and cert["original_Galois_direction_input_verified"] is True
    spec = cert["stage_manifest"]
    assert Path(spec["file"]).name == spec["file"]
    path = out/spec["file"]
    assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
    manifest = read(path)
    matching_configuration(manifest["configuration"], item)
    assert manifest["complete"] is True
    for row in manifest["files"]:
        assert Path(row["file"]).name == row["file"]
        path = out/row["file"]
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        data = read(path)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
    point_spec = cert["point_spec"]
    assert point_spec in manifest["files"]
    point = read(out/point_spec["file"])
    for name in ("point_status", "common_zero_order", "actual_beta_C_computed",
                 "actual_real_descent_image_computed", "original_A_coordinate_lift_computed",
                 "actual_heights_or_uniformity_computed", "quotient_derivative_independently_compared"):
        assert point[name] == cert[name]
    if point["point_status"] == "finite":
        assert point["original_elliptic_equation_verified"] is True
        assert point["original_Galois_direction_verified"] is True
        assert point["real_descent_elliptic_equation_verified"] is True
        assert point["quotient_derivative_independently_compared"] == (point["common_zero_order"] == 0)
    else:
        assert point["beta_C"] == "O" and point["real_descent_image"] == "O"
        assert point["original_y_pole_order"] == 3
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
