#!/usr/bin/env python3
"""R786: consume completed original power5 stages; publish provenance only."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys

from p41_public_actions_recovery import publish, read, save, sha

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R786-public-exact-power5-short-basis-request.json"
RESULT = "R786-exact-original-power5-short-basis"
FINAL = "p41-exact-original-power5-short-basis-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json",
         }


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual arithmetic belongs to public repository Actions.")


def root_dir():
    return Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def api(path):
    return json.loads(subprocess.check_output(["gh", "api", path], text=True))


def download(spec, directory, require_complete=True):
    metadata = api("repos/Rogerhu12/math-research-public/actions/runs/"+spec["run_id"])
    assert metadata["head_sha"] == spec["source_commit"]
    assert metadata["status"] == "completed"
    if require_complete:
        assert metadata["conclusion"] == "success"
    if spec.get("expected_conclusion"):
        assert metadata["conclusion"] == spec["expected_conclusion"]
    artifact = api("repos/Rogerhu12/math-research-public/actions/artifacts/"+str(spec["artifact_id"]))
    assert artifact["name"] == spec["artifact_name"] and not artifact["expired"]
    assert artifact["workflow_run"]["id"] == int(spec["run_id"])
    assert artifact["digest"] == "sha256:"+spec["archive_sha256"]
    directory.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", spec["run_id"], "--repo",
                    "Rogerhu12/math-research-public", "--name", spec["artifact_name"],
                    "--dir", str(directory)], check=True)


def find_hash(directory, name, digest):
    assert Path(name).name == name
    matches = [path for path in directory.rglob(name) if path.is_file() and sha(path) == digest]
    if not matches:
        raise ValueError("Retained file/SHA not found: "+name)
    return matches[0]


def prepare_inputs(item, out):
    inputs = out.parent/"retained"
    inputs.mkdir(parents=True, exist_ok=True)
    records = []
    assert set(item["retained_artifacts"]) == {"R771", "R775"}
    for label, spec in item["retained_artifacts"].items():
        directory = out.parent/("downloaded-"+label)
        target = inputs/label
        target.mkdir(parents=True, exist_ok=True)
        download(spec, directory, require_complete=(label == "R771"))
        mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        rp = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
        run = read(rp)
        assert run["source_commit"] == spec["source_commit"]
        assert run["workflow_run_id"] == spec["run_id"]
        if label == "R771":
            assert run["complete"] and run["process_exit_code"] == 0
            certificate_name = spec["certificate_name"]
            certificate_sha = spec["files"][certificate_name]
            assert entries[certificate_name]["sha256"] == certificate_sha
            certificate_path = find_hash(directory, certificate_name, certificate_sha)
            certificate = read(certificate_path)
            assert certificate["complete"]
            tag = certificate["configuration"]
            assert tag["source_sha256"] == spec["core_sha256"]
            needed = ["R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz" for a in range(82)]
            needed.append("R771-original-level82-Eisenstein-label-group.json.gz")
            shutil.copyfile(certificate_path, target/certificate_name)
        else:
            # The old producer timed out AFTER completing exactly these stages.
            # No final R775 certificate and no power6 success are assumed.
            assert spec["expected_conclusion"] == "failure"
            assert run["complete"] is False and run["process_exit_code"] == 124
            needed = ["R775-determinant-cosets.json.gz", "R775-basis-M2.json.gz"]
            needed += ["R775-basis-power-"+str(k)+".json.gz" for k in range(2, 6)]
            assert set(spec["files"]) == set(needed)
            anchor = find_hash(directory, "R775-basis-M2.json.gz",
                               spec["files"]["R775-basis-M2.json.gz"])
            data = read(anchor)
            assert data["complete"] is True
            tag = data["configuration"]
            assert tag["source_sha256"] == spec["core_sha256"]
            certificate_sha = None
        copied = []
        for name in needed:
            row = entries[name]
            if label == "R775":
                assert row["sha256"] == spec["files"][name]
            source = find_hash(directory, name, row["sha256"])
            assert source.stat().st_size == row["bytes"]
            data = read(source)
            assert data["complete"] is True and data["configuration"] == tag
            shutil.copyfile(source, target/name)
            copied.append({"file": name, "sha256": row["sha256"], "bytes": row["bytes"]})
        shutil.copyfile(mp, target/"full-outputs-manifest.json")
        records.append({"label": label, "producer": spec,
            "producer_run_and_source_verified": True,
            "artifact_metadata_digest_verified": True,
            "certificate_sha256": certificate_sha, "files": copied,
            "complete_stage_prefix_consumed": label == "R775",
            "R775_final_certificate_assumed": False})
    save(out/"retained-inputs-receipt.json", {
        "artifact_groups": records, "old_producer_mathematics_recomputed": False})
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R786-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    copied = []
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R786-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = find_hash(directory, name, row["sha256"])
        data = read(source)
        tag = data["configuration"]
        assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
        assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
        assert tag["R772_proof_sha256"] == item["descent_proof_sha256"]
        assert tag["R775_completed_prefix_producer"] == item["retained_artifacts"]["R775"]
        if (out/name).exists():
            assert sha(out/name) == row["sha256"]
        else:
            shutil.copyfile(source, out/name)
        copied.append({"file": name, "sha256": row["sha256"],
                       "complete": data.get("complete", False)})
    assert copied, "No compatible completed exact stages in the resume artifact"
    save(out/"resume-receipt.json", {"producer": spec,
        "same_exact_core_sha256": item["core_sha256"], "files": copied,
        "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path),
                     "included_in_git": path.name in SMALL and path.stat().st_size < 100_000,
                     "artifact": artifact})
    manifest_path = out/"full-outputs-manifest.json"
    save(manifest_path, {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_artifact": artifact,
        "reproducible_exact_basis_tables_in_git_or_release": False,
        "reproducible_certificates_in_git_or_release": False,
        "temporary_active_checkpoint_retention_days": 1})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": manifest_path.name,
        "manifest_sha256": sha(manifest_path), "manifest_bytes": manifest_path.stat().st_size,
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": manifest_path.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method = S/item["core"], topic_path(item["method"])
    proof, descent = topic_path(item["proof"]), topic_path(item["descent_proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item,
        "core_sha256": sha(core), "method_sha256": sha(method),
        "proof_sha256": sha(proof), "descent_proof_sha256": sha(descent),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "retained_artifacts": item["retained_artifacts"], "resume": item.get("resume"),
        "budget_minutes": item["budget_minutes"],
        "arithmetic": "exact integer cyclotomic qY0..128 for the original1234 power5 basis; no H3 solve",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_y_map_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        assert sha(proof) == item["R786_proof_sha256"]
        assert sha(descent) == item["descent_proof_sha256"]
        assert item["basis_bound_qY"] == 128 and item["ordinary_power"] == 5
        assert item["ordinary_power_dimension"] == 1234
        inputs = prepare_inputs(item, out)
        restore_resume(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--retained", str(inputs),
                   "--output", str(out), "--config", str(config),
                   "--proof", str(proof), "--descent-proof", str(descent),
                   "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; exact completed stages and their source tags retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    receipt_path = out/"core-receipt.json"
    receipt = read(receipt_path) if receipt_path.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code,
        "error": error, "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(receipt_path) if receipt_path.exists() else None,
        "exact_original_power5_short_basis_claimed": complete,
        "actual_y_map_beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete,
                      "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True
    receipt = read(out/"core-receipt.json")
    assert sha(out/"core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["complete"] is True and receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["complete"] is True and cert["result"] == RESULT and cert["p"] == 41
    tag = cert["configuration"]
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
    assert tag["R772_proof_sha256"] == item["descent_proof_sha256"]
    assert tag["R775_completed_prefix_producer"] == item["retained_artifacts"]["R775"]
    assert tag["qY_bound"] == 128 and tag["ordinary_power"] == 5
    assert tag["ordinary_power_dimension"] == 1234
    assert cert["exact_power5_basis_dimension"] == 1234
    assert cert["exact_K_basis_prefix_bound_qY"] == 128
    assert cert["basis_integer_scale"] == str(82**10)
    assert cert["all_original_R775_mod739_short_series_compared"] is True
    assert cert["actual_L_kernel_or_y_map_or_beta_or_height_computed"] is False
    for key in ("basis_index", "stages_manifest"):
        spec = cert[key]
        assert Path(spec["file"]).name == spec["file"]
        path = out/spec["file"]
        assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
        data = read(path)
        assert data["complete"] is True and data["configuration"] == tag
        if key == "basis_index":
            assert data["dimension"] == 1234 and data["bound_qY"] == 128
            assert len(data["basis_rows"]) == 1234
            assert [row["index"] for row in data["basis_rows"]] == list(range(1234))
        if key == "stages_manifest":
            assert len(data["files"]) == spec["stage_count"]
            for row in data["files"]:
                assert Path(row["file"]).name == row["file"]
                assert sha(out/row["file"]) == row["sha256"]
                assert (out/row["file"]).stat().st_size == row["bytes"]
    # The core verified all new exact arithmetic once; this pass verifies
    # its source-bound products without repeating that arithmetic.
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
    args = parser.parse_args()
    out = root_dir()/"output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    assert item["result"] == RESULT
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
