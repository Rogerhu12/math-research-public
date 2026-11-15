#!/usr/bin/env python3
"""R790 public runner: source-bound original CM inputs and active continuations."""
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
from R786_public_exact_power5_short_basis import api, download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R790-public-original-CM-fiber-request.json"
RESULT = "R790-original-CM-fiber-jets"
FINAL = "p41-original-CM-fiber-jets-certificate.json"
INPUT_BUNDLE = "R790-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R735", "R754", "R771", "R775"}
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["R790_proof_sha256"] == item["R790_proof_sha256"]
    assert tag["field_core_sha256"] == item["field_core_sha256"]
    assert tag["cm_jet_order"] == item["cm_jet_order"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]
    assert tag["python_flint"] == "0.9.0"


def producer_metadata(directory, spec):
    try:
        mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    except ValueError:
        # The original R735 artifact predates inclusion of this small manifest
        # in its ZIP.  Its already-published Git metadata is an explicitly
        # pinned fallback, never a replacement manifest made from the archive.
        relative = spec.get("manifest_repository_path")
        if relative is None:
            raise
        assert spec["result"] == "R732-p41-original-CM-model"
        assert relative == "computations/R732-p41-original-CM-model/"+\
            spec["run_id"]+"-1/full-outputs-manifest.json"
        mp = topic_path(relative)
        assert mp.is_file() and sha(mp) == spec["manifest_sha256"]
    manifest = read(mp)
    assert manifest["result"] == spec["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    paths = {"full-outputs-manifest.json": mp}
    for name in PRODUCER_META[1:]:
        paths[name] = find_hash(directory, name, entries[name]["sha256"])
        assert paths[name].stat().st_size == entries[name]["bytes"]
    run, core, initial = (read(paths[name]) for name in PRODUCER_META[1:])
    assert run["result"] == spec["result"] and run["complete"] is True
    assert run["workflow_run_id"] == spec["run_id"]
    assert run["source_commit"] == spec["source_commit"] and run["process_exit_code"] == 0
    assert run["core_receipt_sha256"] == sha(paths["core-receipt.json"])
    assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
    assert initial["result"] == spec["result"]
    assert initial["source_commit"] == spec["source_commit"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["core_sha256"] == spec["core_sha256"]
    name = spec["certificate_name"]
    assert core["certificate_sha256"] == spec["files"][name] == entries[name]["sha256"]
    cp = find_hash(directory, name, spec["files"][name])
    assert cp.stat().st_size == entries[name]["bytes"]
    certificate = read(cp)
    assert certificate["complete"] is True
    paths[name] = cp
    return entries, paths, certificate


def prepare_inputs(item, out):
    inputs = out.parent/"retained"
    records = []
    assert set(item["retained_artifacts"]) == LABELS
    for label, spec in item["retained_artifacts"].items():
        target = inputs/label
        target.mkdir(parents=True, exist_ok=True)
        transferred = (target/"full-outputs-manifest.json").exists()
        if transferred:
            directory = target
            metadata = api("repos/Rogerhu12/math-research-public/actions/runs/"+spec["run_id"])
            assert metadata["head_sha"] == spec["source_commit"]
            assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
        else:
            directory = out.parent/("downloaded-"+label)
            download(spec, directory, require_complete=True)
        entries, paths, certificate = producer_metadata(directory, spec)
        if label == "R735":
            # This original producer has identity fields, not configuration/complete
            # fields on its torsion modulus.  Bind the actual chain explicitly.
            identity = certificate["identity"]
            assert identity["source_sha256"] == spec["core_sha256"]
            assert identity["p"] == 41 and identity["torsion_degree"] == 280
            assert identity["python_flint"] == "0.9.0"
            assert certificate["original_b_not_a_replacement_twist"] is True
            assert certificate["torsion_modulus_sha256"] == spec["files"]["p41-original-torsion-modulus.json.gz"]
            stages = None
        else:
            assert certificate["result"] == spec["result"]
            tag = certificate["configuration"]
            assert tag["source_sha256"] == spec["core_sha256"] and tag["python_flint"] == "0.9.0"
            stages = {row["file"]: row for row in certificate["stages"]}
        continuation_files = item.get("continuation_only_retained_files", {}).get(label, {})
        assert not (set(continuation_files)&set(spec["files"]))
        if continuation_files:
            assert label == "R775"
            assert set(continuation_files) == {
                "R775-basis-power-"+str(power)+".json.gz" for power in range(2, 6)}
        copied_files = dict(spec["files"], **continuation_files)
        for name, digest in copied_files.items():
            assert Path(name).name == name and entries[name]["sha256"] == digest
            path = find_hash(directory, name, digest)
            assert path.stat().st_size == entries[name]["bytes"]
            data = read(path)
            if name != spec["certificate_name"]:
                if label == "R735":
                    assert name == "p41-original-torsion-modulus.json.gz"
                    assert data["identity"] == identity
                else:
                    assert stages[name]["sha256"] == digest
                    assert data["complete"] is True and data["configuration"] == tag
            if label == "R754" and name == "R754-original-Weil-pairing.json.gz":
                assert data["p_power_equals_one"] is True and data["not_one"] is True
                assert data["analytic_orientation"] == "exp(2*pi*i/41), by R751 sigma and Legendre proof"
            if label == "R771" and name == "R771-original-level82-Eisenstein-label-group.json.gz":
                assert data["all_group_determinants_one_mod82"] is True
            if label == "R775" and name == "R775-basis-M2.json.gz":
                assert data["rank"] == 146
                assert data["characteristic_zero_independence_certified_by_unit_reduction"] is True
            if label == "R775" and name == "R775-determinant-cosets.json.gz":
                assert data["all_representatives_normalize_original_H82"] is True
            paths[name] = path
        if label == "R775":
            assert certificate["all_recipes_defined_over_original_K"] is True
            assert certificate["M2_dimension"] == 146
        for name, path in paths.items():
            if path.resolve() != (target/name).resolve():
                shutil.copyfile(path, target/name)
        records.append({"label": label, "producer": spec,
            "producer_run_source_core_receipt_and_manifest_verified": True,
            "original_artifact_digest_verified_on_this_download": not transferred,
            "inputs_from_verified_active_resume_bundle": transferred,
            "all_copied_file_sizes_and_sha256_verified": True,
            "continuation_only_files": continuation_files,
            "continuation_only_purpose": "R787/R786 original product recipes for the next beta composition",
            "core_mathematical_input_file_map_unchanged": True,
            "R735_uses_real_identity_schema": label == "R735"})
    save(out/"retained-inputs-receipt.json", {"artifact_groups": records,
        "completed_old_target_periods_Weil_pairing_or_basis_recomputed": False})
    bundle = out/INPUT_BUNDLE
    if not bundle.exists():
        with tarfile.open(bundle, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=str(path.relative_to(inputs)), recursive=False)
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R790-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    old_input = read(find_hash(directory, "public-actions-input.json", entries["public-actions-input.json"]["sha256"]))
    assert old_input["source_commit"] == spec["source_commit"]
    old_job = old_input["job"]
    for name in ("result", "core_sha256", "R790_proof_sha256", "field_core_sha256",
                 "cm_jet_order", "retained_artifacts"):
        assert old_job[name] == item[name], "Changed mathematical continuation input: "+name
    assert old_job.get("continuation_only_retained_files", {}) == \
        item.get("continuation_only_retained_files", {})
    assert INPUT_BUNDLE in entries, "Continuation must carry its verified producer inputs"
    bundle_spec = entries[INPUT_BUNDLE]
    bundle = find_hash(directory, INPUT_BUNDLE, bundle_spec["sha256"])
    assert bundle.stat().st_size == bundle_spec["bytes"]
    target = out.parent/"retained"
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in LABELS
            group, name = relative.parts
            allowed = set(item["retained_artifacts"][group]["files"])|set(PRODUCER_META)|\
                set(item.get("continuation_only_retained_files", {}).get(group, {}))
            assert name in allowed
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
        if not (name.startswith("R790-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        assert Path(name).name == name
        source = find_hash(directory, name, row["sha256"])
        assert source.stat().st_size == row["bytes"]
        data = read(source)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
        if (out/name).exists():
            assert sha(out/name) == row["sha256"]
        else:
            shutil.copyfile(source, out/name)
        copied += 1
    assert copied, "No compatible mathematical checkpoint in continuation"
    save(out/"resume-receipt.json", {"producer": spec,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": copied,
        "complete_source_bound_stages_restored": True,
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
    mp = out/"full-outputs-manifest.json"
    save(mp, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
              "temporary_active_checkpoint_retention_days": 1,
              "reproducible_CM_jets_or_certificates_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": mp.name,
        "manifest_sha256": sha(mp), "manifest_bytes": mp.stat().st_size,
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": mp.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    core, field_core = S/item["core"], S/item["field_core"]
    proof = topic_path(item["proof"])
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "field_core_sha256": sha(field_core),
        "proof_sha256": sha(proof), "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_CM_values_claimed_before_run": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"]
        assert sha(field_core) == item["field_core_sha256"]
        assert sha(proof) == item["R790_proof_sha256"]
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--retained", str(inputs),
                   "--output", str(out), "--config", str(config), "--proof", str(proof),
                   "--field-core", str(field_core),
                   "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; exact completed stages and active checkpoint retained."
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
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_beta_or_height_computed": False})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True and run["process_exit_code"] == 0
    rp = out/"core-receipt.json"
    assert sha(rp) == run["core_receipt_sha256"]
    receipt = read(rp)
    assert receipt["complete"] is True and receipt["result"] == RESULT
    assert receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["complete"] is True and cert["result"] == RESULT and cert["p"] == 41
    matching_configuration(cert["configuration"], item)
    assert cert["M2_dimension"] == 146 and cert["cm_jet_order"] == item["cm_jet_order"]
    assert cert["original_psi_values_and_first_coarse_jets_verified"] is True
    assert cert["actual_y_beta_or_height_computed"] is False
    assert cert["original_M2_scale"] == "6724"
    assert cert["R786_power5_product_scale"] == "13744803133596058624"
    assert cert["distinct_retained_M2_seeds"] == 5
    assert cert["actual_reflected_seed_pairs"] == 10
    spec = cert["stage_manifest"]
    assert Path(spec["file"]).name == spec["file"]
    path = out/spec["file"]
    assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
    stages = read(path)
    matching_configuration(stages["configuration"], item)
    assert stages["complete"] is True
    assert stages["M2_output_rows"] == cert["M2_output_rows"]
    assert len(cert["M2_output_rows"]) == 146
    assert [row["file"] for row in cert["M2_output_rows"]] == [
        "R790-M2-CM-jet-"+str(index).zfill(4)+".json.gz" for index in range(146)]
    expected_rows = {row["file"]: row for row in cert["M2_output_rows"]}
    seen_indices = []
    for row in stages["files"]:
        assert Path(row["file"]).name == row["file"]
        path = out/row["file"]
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        data = read(path)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
        if row["file"].startswith("R790-M2-CM-jet-"):
            assert row == expected_rows[row["file"]]
            assert row["file"] == "R790-M2-CM-jet-"+str(data["index"]).zfill(4)+".json.gz"
            assert data["integer_scale"] == "6724"
            assert data["R786_power1_scale_preserved"] is True
            assert data["M2_recipe_source_sha256"] == \
                item["retained_artifacts"]["R775"]["files"]["R775-basis-M2.json.gz"]
            for key in ("value_K_1_zeta", "derivative_z_K_1_zeta"):
                assert len(data[key]) == 2
                assert all(len(pair) == 2 and all(isinstance(value, str) for value in pair)
                           and int(pair[1]) > 0 for pair in data[key])
            seen_indices.append(data["index"])
    assert sorted(seen_indices) == list(range(146))
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
    assert item["result"] == RESULT
    return publish_small(item, out) if mode == "publish" else verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
