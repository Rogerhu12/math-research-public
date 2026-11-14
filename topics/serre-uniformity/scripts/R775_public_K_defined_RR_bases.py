#!/usr/bin/env python3
"""R775: public execution and retained recipe/minor publication."""
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
REQUEST = TOPIC/"notes/R775-public-K-defined-RR-bases-request.json"
RESULT = "R775-p41-original-K-defined-RR-bases"
FINAL = "p41-original-K-defined-RR-basis-certificate.json"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json",
         "public-actions-run.log", FINAL}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New arithmetic runs only in the public repository Actions.")


def root_dir():
    return Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT


def safe_topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def prepare_inputs(item, out):
    spec = item["retained"]["R771"]
    certificate = safe_topic_path(spec["certificate_path"])
    assert sha(certificate) == spec["certificate_sha256"]
    assert sha(safe_topic_path(spec["core_path"])) == spec["core_sha256"]
    metadata = json.loads(subprocess.check_output([
        "gh", "api", "repos/Rogerhu12/math-research-public/actions/runs/"+spec["run_id"]
    ], text=True))
    assert metadata["head_sha"] == spec["source_commit"]
    assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
    artifact = json.loads(subprocess.check_output([
        "gh", "api", "repos/Rogerhu12/math-research-public/actions/artifacts/"+str(spec["artifact_id"])
    ], text=True))
    assert artifact["name"] == spec["artifact_name"] and not artifact["expired"]
    assert artifact["workflow_run"]["id"] == int(spec["run_id"])
    assert artifact["digest"] == "sha256:"+spec["artifact_zip_sha256"]
    directory = out.parent/"retained-R771"
    downloaded = out.parent/"downloaded-R771"
    directory.mkdir(parents=True, exist_ok=True)
    downloaded.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", spec["run_id"], "--repo",
                    "Rogerhu12/math-research-public", "--name", spec["artifact_name"],
                    "--dir", str(downloaded)], check=True)
    mp = find_hash(downloaded, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == "R771-p41-original-quotient-RR-bases"
    rows = {r["file"]: r for r in manifest["files"]}
    needed = ["R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz" for a in range(82)]
    needed += ["R771-original-level82-Eisenstein-label-group.json.gz",
               "R771-original-E4-E6-eta12-and-RR-denominators.json.gz",
               "R771-basis-M2.json.gz"]
    copied = []
    for name in needed:
        row = rows[name]
        source = find_hash(downloaded, name, row["sha256"])
        data = read(source)
        assert data["complete"]
        assert data["configuration"]["source_sha256"] == spec["core_sha256"]
        assert source.stat().st_size == row["bytes"]
        shutil.copyfile(source, directory/name)
        copied.append({"file": name, "sha256": row["sha256"], "bytes": row["bytes"]})
    cp = find_hash(downloaded, certificate.name, spec["certificate_sha256"])
    shutil.copyfile(cp, directory/certificate.name)
    shutil.copyfile(mp, directory/"full-outputs-manifest.json")
    save(out/"retained-inputs-receipt.json", {
        "producer": spec, "metadata_source_commit_verified": True,
        "artifact_metadata_digest_verified": True,
        "certificate_sha256": sha(cp), "manifest_sha256": sha(mp),
        "completed_stages_copied_verbatim": copied,
        "old_E1_group_level_one_M2_or_other_mathematics_recomputed": False})
    return {"R771": directory}


def find_hash(directory, name, digest):
    matches = [p for p in directory.rglob(name) if p.is_file() and sha(p) == digest]
    if not matches:
        raise ValueError("Required retained file/SHA was not found: "+name)
    return matches[0]


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R775-continuation"
    directory.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", spec["run_id"], "--repo",
                    "Rogerhu12/math-research-public", "--name", spec["artifact_name"],
                    "--dir", str(directory)], check=True)
    manifest_path = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(manifest_path)
    assert manifest["result"] == RESULT
    copied = []
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R775-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        assert Path(name).name == name
        source = find_hash(directory, name, row["sha256"])
        data = read(source)
        tag = data["configuration"]
        assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
        assert tag["R772_proof_sha256"] == item["proof_sha256"]
        assert tag["R771_certificate_sha256"] == item["retained"]["R771"]["certificate_sha256"]
        assert tag["R771_manifest_sha256"] == item["retained"]["R771"]["manifest_sha256"]
        target = out/name
        if target.exists():
            assert sha(target) == row["sha256"]
        else:
            shutil.copyfile(source, target)
        copied.append({"file": name, "sha256": row["sha256"],
                       "complete": data.get("complete", False)})
    assert copied, "No compatible retained R775 stages were supplied"
    save(out/"resume-receipt.json", {"run_id": spec["run_id"],
        "artifact_name": spec["artifact_name"], "manifest_sha256": spec["manifest_sha256"],
        "same_exact_source_sha256": item["core_sha256"], "copied": copied,
        "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name == "full-outputs-manifest.json":
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path),
                     "included_in_git": path.name in SMALL and path.stat().st_size < 100_000,
                     "artifact": artifact})
    save(out/"full-outputs-manifest.json", {
        "result": RESULT, "files": rows, "full_outputs_artifact": artifact,
        "reproducible_Eisenstein_and_product_tables_in_git": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method, proof = S/item["core"], safe_topic_path(item["method"]), safe_topic_path(item["proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(core),
        "method_sha256": sha(method), "proof_sha256": sha(proof),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "retained": item["retained"], "resume": item.get("resume"),
        "budget_minutes": item["budget_minutes"],
        "arithmetic": "exact F_739 determinant-semilinear K recipes, original R771 E1 cache reused",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mathematical_completion_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert sha(core) == item["core_sha256"]
        assert sha(method) == item["method_sha256"]
        assert sha(proof) == item["proof_sha256"]
        assert item["prime"] == 739 and item["max_exponent_qY"] == 1640
        paths = prepare_inputs(item, out)
        restore_resume(item, out)
        command = [sys.executable, "-u", str(core), "--output", str(out),
                   "--retained", str(paths["R771"]), "--proof", str(proof)]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60)
            except subprocess.TimeoutExpired:
                error = "Budget reached; all completed rows and partial basis stages retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    path = out/"core-receipt.json"
    receipt = read(path) if path.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code,
        "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(path) if path.exists() else None,
        "actual_RR_basis_recipes_and_minors_claimed": complete,
        "actual_rational_functions_beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete,
                      "process_exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify_minor(minor, dimension, bound):
    assert minor["rows"] == minor["columns"] == dimension
    assert minor["prime"] == 739 and 0 < minor["determinant_mod_ell"] < 739
    columns = minor["coefficient_exponents"]
    assert len(columns) == dimension and columns == sorted(set(columns))
    assert all(0 <= n <= bound for n in columns)
    assert minor["original_recipe_rows_not_reduced_combinations"]


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
    assert tag["source_sha256"] == item["core_sha256"]
    assert tag["R772_proof_sha256"] == item["proof_sha256"]
    assert tag["R771_certificate_sha256"] == item["retained"]["R771"]["certificate_sha256"]
    assert tag["R771_manifest_sha256"] == item["retained"]["R771"]["manifest_sha256"]
    assert tag["R771_core_sha256"] == item["retained"]["R771"]["core_sha256"]
    assert tag["prime"] == cert["prime"] == 739 and tag["max_exponent_qY"] == 1640
    assert tag["python_flint"] == "0.9.0"
    assert cert["source_quotient_genus"] == 127 and cert["level"] == 82
    assert cert["M2_dimension"] == 146 and cert["M6_dimension"] == 694 and cert["M12_dimension"] == 1514
    assert cert["power_basis_dimensions"] == {
        "1": 146, "2": 418, "3": 690, "4": 962, "5": 1234, "6": 1506}
    assert len(cert["M2_actual_K_recipes"]) == 146
    assert cert["all_recipes_defined_over_original_K"]
    assert all(r["kind"] == "det_semilinear_E1_pair_trace" and 0 <= r["j"] < 40
               and 0 <= r["R771_seed_index"] < 146 for r in cert["M2_actual_K_recipes"])
    for name, dimension, bound in (("M2", 146, 273), ("M6", 694, 820), ("M12", 1514, 1640)):
        verify_minor(cert[name+"_actual_minor"], dimension, bound)
    assert cert["selected_actual_map_index"] == 4 and cert["selected_actual_map_degree"] == "1206"
    assert not cert["actual_original_y_or_beta_or_height_computed"]
    assert not cert["full_characteristic_zero_q_series_computed"]
    assert not cert["old_E1_group_level_one_and_original_M2_recomputed"]
    assert not cert["old_topology_periods_Hom_lattice_or_degrees_recomputed"]
    for row in cert["stages"]:
        assert Path(row["file"]).name == row["file"]
        assert sha(out/row["file"]) == row["sha256"]
    for name, dimension in (("M2", 146), ("M6-complete", 694), ("M12-complete", 1514)):
        stage = read(out/("R775-basis-"+name+".json.gz"))
        assert stage["configuration"] == tag and stage["complete"]
        assert stage["rank"] == len(stage["basis"]) == dimension
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
        item = request["job"]
        return compute(item, out)
    # Publication can move the checkout to a newer main.  Keep the exact
    # original job frozen in the retained input receipt for both later steps.
    item = read(out/"public-actions-input.json")["job"]
    assert item["result"] == RESULT
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
