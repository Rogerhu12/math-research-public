#!/usr/bin/env python3
"""R781 public runner: reuse completed R774 data and preserve each exact order."""
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
REQUEST = TOPIC/"notes/R781-public-Laurent-prefix-request.json"
RESULT = "R781-original-p41-inverse-free-Laurent-prefix"
FINAL = "p41-original-inverse-free-Laurent-prefix-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json", "resume-receipt.json",
         "run-receipt.json", "core-receipt.json"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
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
    if require_complete:
        assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
    artifact = api("repos/Rogerhu12/math-research-public/actions/artifacts/"+str(spec["artifact_id"]))
    assert artifact["name"] == spec["artifact_name"] and not artifact["expired"]
    assert artifact["workflow_run"]["id"] == int(spec["run_id"])
    assert artifact["digest"] == "sha256:"+spec["archive_sha256"]
    directory.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", spec["run_id"], "--repo", "Rogerhu12/math-research-public",
                    "--name", spec["artifact_name"], "--dir", str(directory)], check=True)


def find_hash(directory, name, digest):
    assert Path(name).name == name
    matches = [path for path in directory.rglob(name) if path.is_file() and sha(path) == digest]
    if not matches:
        raise ValueError("Retained file/SHA not found: "+name)
    return matches[0]


def prepare_inputs(item, out):
    inputs = out.parent/"retained"
    spec = item["retained_artifacts"]["R774"]
    directory, target = out.parent/"downloaded-R774", inputs/"R774"
    target.mkdir(parents=True, exist_ok=True)
    download(spec, directory)
    manifest_path = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(manifest_path)
    assert manifest["result"] == spec["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    run_path = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
    run = read(run_path)
    assert run["complete"] and run["source_commit"] == spec["source_commit"]
    assert run["workflow_run_id"] == spec["run_id"]
    cname = spec["certificate_name"]
    csha = spec["files"][cname]
    assert entries[cname]["sha256"] == csha
    cpath = find_hash(directory, cname, csha)
    cert = read(cpath)
    assert cert["complete"] and cert["configuration"]["source_sha256"] == spec["core_sha256"]
    assert cert["actual_cusp_ramification_e"] == 1
    needed = ["R774-original-L-cubic-scalars.json.gz"]
    for block in cert["H3_blocks"]:
        first = int(block["file"].split("-qY-")[1].split("-")[0])
        if first <= item["H3_prefix_bound"]:
            needed.append(block["file"])
    copied = []
    for name in needed:
        entry = entries[name]
        source = find_hash(directory, name, entry["sha256"])
        assert source.stat().st_size == entry["bytes"]
        data = read(source)
        assert data["complete"] and data["configuration"] == cert["configuration"]
        shutil.copyfile(source, target/name)
        copied.append({"file": name, "sha256": entry["sha256"], "bytes": entry["bytes"]})
    shutil.copyfile(cpath, target/cname)
    shutil.copyfile(manifest_path, target/"full-outputs-manifest.json")
    save(out/"retained-inputs-receipt.json", {"producer": spec, "files": copied,
         "producer_run_and_source_verified": True, "artifact_metadata_digest_verified": True,
         "old_producer_mathematics_recomputed": False})
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R781-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    copied = []
    for entry in manifest["files"]:
        name = entry["file"]
        if not (name.startswith("R781-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = find_hash(directory, name, entry["sha256"])
        data = read(source)
        tag = data["configuration"]
        assert data["complete"] and tag["result"] == RESULT
        assert tag["source_sha256"] == item["core_sha256"]
        assert tag["R781_proof_sha256"] == item["R781_proof_sha256"]
        assert tag["R778_proof_sha256"] == item["R778_proof_sha256"]
        assert tag["R774_producer"] == item["retained_artifacts"]["R774"]
        if (out/name).exists():
            assert sha(out/name) == entry["sha256"]
        else:
            shutil.copyfile(source, out/name)
        copied.append({"file": name, "sha256": entry["sha256"]})
    assert copied, "No compatible completed Laurent stages in the continuation artifact"
    save(out/"resume-receipt.json", {"producer": spec, "files": copied,
         "same_exact_core_sha256": item["core_sha256"],
         "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    entries = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        entries.append({"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path),
            "included_in_git": path.name in SMALL and path.stat().st_size < 100_000,
            "temporary_active_checkpoint_artifact": artifact})
    manifest_path = out/"full-outputs-manifest.json"
    save(manifest_path, {"result": RESULT, "files": entries,
                        "temporary_active_checkpoint_artifact": artifact,
                        "checkpoint_retention_days": 1,
                        "reproducible_data_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": manifest_path.name,
         "manifest_sha256": sha(manifest_path), "manifest_bytes": manifest_path.stat().st_size,
         "file_count": len(entries), "temporary_active_checkpoint_artifact": artifact,
         "checkpoint_retention_days": 1, "manifest_in_git": manifest_path.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method = S/item["core"], topic_path(item["method"])
    proof, short = topic_path(item["proof"]), topic_path(item["short_proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
         "source_repository": "Rogerhu12/math-research-public", "source_commit": source, "job": item,
         "core_sha256": sha(core), "method_sha256": sha(method), "proof_sha256": sha(proof),
         "short_proof_sha256": sha(short), "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
         "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
         "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
         "workflow_sha256": sha(REPO/item["workflow"]),
         "retained_artifacts": item["retained_artifacts"], "resume": item.get("resume"),
         "budget_minutes": item["budget_minutes"],
         "arithmetic": "exact primitive280 vectors with rational scale; no kappa inverse",
         "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
         "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
         "actual_y_map_beta_or_height_computed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        assert sha(proof) == item["R781_proof_sha256"] and sha(short) == item["R778_proof_sha256"]
        assert item["prefix_bound"] == 142 and item["H3_prefix_bound"] == 143
        inputs = prepare_inputs(item, out)
        restore_resume(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--retained", str(inputs),
                   "--output", str(out), "--config", str(config), "--proof", str(proof),
                   "--short-proof", str(short), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed source-bound Laurent orders preserved for continuation."
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
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "complete": complete,
         "process_exit_code": code, "error": error, "source_commit": source,
         "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
         "execution_environment": "public-repository-github-actions",
         "core_receipt_sha256": sha(receipt_path) if receipt_path.exists() else None,
         "exact_normalized_Laurent_prefix_claimed": complete,
         "actual_y_map_beta_or_height_computed": False,
         "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"]
    receipt = read(out/"core-receipt.json")
    assert sha(out/"core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["complete"] and receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["complete"] and cert["result"] == RESULT and cert["p"] == 41
    tag = cert["configuration"]
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    assert tag["R781_proof_sha256"] == item["R781_proof_sha256"]
    assert tag["R778_proof_sha256"] == item["R778_proof_sha256"]
    assert tag["R774_producer"] == item["retained_artifacts"]["R774"]
    assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["actual_cusp_order"] == 1 and cert["normalized_Laurent_R_bound"] == 142
    assert cert["retained_H3_bound"] == 143 and cert["coefficient_field_dimension_over_Q"] == 280
    assert cert["all_original_real_tangent_phases_verified"]
    assert cert["all_recurrence_coefficients_verified_exactly"]
    assert not cert["algebraic_kappa_inverse_computed"]
    assert not cert["actual_relation_matrix_or_kernel_computed"]
    assert not cert["actual_y_map_or_beta_or_height_computed"]
    manifest_spec = cert["stages_manifest"]
    manifest_path = out/manifest_spec["file"]
    assert sha(manifest_path) == manifest_spec["sha256"]
    inventory = read(manifest_path)
    assert inventory["complete"] and inventory["configuration"] == tag
    assert len(inventory["files"]) == manifest_spec["stage_count"]
    for entry in inventory["files"]:
        assert Path(entry["file"]).name == entry["file"]
        assert sha(out/entry["file"]) == entry["sha256"]
        assert (out/entry["file"]).stat().st_size == entry["bytes"]
    return 0


def publish_small(item, out):
    output_manifest(out)
    manifest = read(out/"full-outputs-manifest.json")
    pub = out.parent/"publication"
    pub.mkdir(parents=True, exist_ok=True)
    for entry in manifest["files"]:
        if entry["included_in_git"]:
            assert sha(out/entry["file"]) == entry["sha256"]
            shutil.copyfile(out/entry["file"], pub/entry["file"])
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
    return publish_small(item, out) if args.mode == "publish" else verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
