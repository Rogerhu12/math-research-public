#!/usr/bin/env python3
"""R777: public exact short-series stage; publish only small provenance."""
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
REQUEST = TOPIC/"notes/R777-public-exact-short-K-basis-request.json"
RESULT = "R777-exact-short-K-basis-and-Hodge-cube-coordinates"
FINAL = "p41-exact-short-K-basis-and-Hodge-cube-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json",
         "public-actions-run.log", FINAL}


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
    if require_complete:
        assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
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
    for label, spec in item["retained_artifacts"].items():
        assert label in ("R771", "R774", "R775")
        directory = out.parent/("downloaded-"+label)
        target = inputs/label
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
        certificate_name = spec["certificate_name"]
        certificate_sha = spec["files"][certificate_name]
        assert entries[certificate_name]["sha256"] == certificate_sha
        certificate_path = find_hash(directory, certificate_name, certificate_sha)
        certificate = read(certificate_path)
        assert certificate["complete"]
        assert certificate["configuration"]["source_sha256"] == spec["core_sha256"]
        if label == "R771":
            needed = ["R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz" for a in range(82)]
            needed += ["R771-original-level82-Eisenstein-label-group.json.gz",
                       "R771-original-E4-E6-eta12-and-RR-denominators.json.gz"]
        elif label == "R775":
            needed = ["R775-determinant-cosets.json.gz", "R775-basis-M2.json.gz"]
            needed += ["R775-basis-power-"+str(k)+".json.gz" for k in range(2, 7)]
            needed += ["R775-basis-M6-complete.json.gz", "R775-basis-M12-complete.json.gz"]
        else:
            needed = ["R774-original-L-cubic-scalars.json.gz"]
            for block in certificate["H3_blocks"]:
                first = int(block["file"].split("-qY-")[1].split("-")[0])
                if first <= item["H3_coordinate_bound_qY"]:
                    needed.append(block["file"])
        copied = []
        for name in needed:
            row = entries[name]
            source = find_hash(directory, name, row["sha256"])
            assert source.stat().st_size == row["bytes"]
            data = read(source)
            assert data["complete"] and data["configuration"] == certificate["configuration"]
            shutil.copyfile(source, target/name)
            copied.append({"file": name, "sha256": row["sha256"], "bytes": row["bytes"]})
        shutil.copyfile(certificate_path, target/certificate_name)
        shutil.copyfile(manifest_path, target/"full-outputs-manifest.json")
        records.append({"label": label, "producer": spec,
            "producer_run_and_source_verified": True,
            "artifact_metadata_digest_verified": True,
            "certificate_sha256": certificate_sha, "files": copied})
    save(out/"retained-inputs-receipt.json", {"artifact_groups": records,
        "old_producer_mathematics_recomputed": False})
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R777-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    copied = []
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R777-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = find_hash(directory, name, row["sha256"])
        data = read(source)
        tag = data["configuration"]
        assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
        assert tag["R778_proof_sha256"] == item["R778_proof_sha256"]
        assert tag["R772_proof_sha256"] == item["descent_proof_sha256"]
        assert tag["R775_producer"] == item["retained_artifacts"]["R775"]
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
        "full_outputs_artifact": artifact,
        "reproducible_exact_basis_and_coordinate_tables_in_git": False})
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
        "arithmetic": "exact integer cyclotomic short series and one rational694x694 solve with14rhs",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_y_map_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        assert sha(proof) == item["R778_proof_sha256"]
        assert sha(descent) == item["descent_proof_sha256"]
        assert item["basis_bound_qY"] == 142 and item["H3_coordinate_bound_qY"] == 41
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
        "exact_short_K_series_and_H3_coordinates_claimed": complete,
        "actual_y_map_beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete,
                      "exit_code": code, "error": error}), flush=True)
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
    assert tag["R778_proof_sha256"] == item["R778_proof_sha256"]
    assert tag["R772_proof_sha256"] == item["descent_proof_sha256"]
    assert tag["R775_producer"] == item["retained_artifacts"]["R775"]
    assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["actual_cusp_ramification_e"] == 1
    assert cert["exact_K_basis_prefix_bound_qY"] == 142
    assert cert["exact_M6_basis_dimension"] == 694 and cert["exact_M12_basis_dimension"] == 1514
    assert cert["all_series_scaled_by_82_to_their_weight"]
    assert cert["all_original_R775_mod739_series_compared"]
    assert cert["exact_H3_coordinates_in_original_K_basis_computed"]
    assert cert["H3_exact_rational_solve_shape"] == [694, 694, 14]
    assert cert["H3_global_equality_from_known_membership_and_injection"]
    assert not cert["actual_L_kernel_or_y_map_or_beta_or_height_computed"]
    inventory_spec = cert["stages_manifest"]
    inventory_path = out/inventory_spec["file"]
    assert sha(inventory_path) == inventory_spec["sha256"]
    inventory = read(inventory_path)
    assert inventory["complete"] and inventory["configuration"] == tag
    assert len(inventory["files"]) == inventory_spec["stage_count"]
    for row in inventory["files"]:
        assert Path(row["file"]).name == row["file"]
        assert sha(out/row["file"]) == row["sha256"]
        assert (out/row["file"]).stat().st_size == row["bytes"]
    minor = read(out/"R777-short-M6-rational-row-minor.json.gz")
    assert minor["complete"] and minor["configuration"] == tag
    assert minor["rank"] == 694 and minor["determinant_mod_prime"] != 0
    assert len(set(minor["selected_original_coordinate_rows"])) == 694
    assert minor["full_rational_matrix_shape"] == [1680, 694]
    h3 = read(out/"R777-exact-original-H3-coordinates-in-K-basis.json.gz")
    assert h3["complete"] and h3["configuration"] == tag
    assert len(h3["coordinates_in_unscaled_original_K_basis"]) == 694
    assert all(len(row) == 14 for row in h3["coordinates_in_unscaled_original_K_basis"])
    assert h3["exact_rational_matrix_equation_verified"]
    assert h3["original_H3_membership_from_R772"]
    assert h3["global_equality_from_R778_arithmetic_injection"]
    # Arithmetic was checked once by the exact core. This pass checks its
    # complete, source-bound products rather than repeating the solve.
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
        assert request["session"] == "serre-public-resume-20261114"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    assert item["result"] == RESULT
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
