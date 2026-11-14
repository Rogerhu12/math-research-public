#!/usr/bin/env python3
"""Public Actions wrapper for R748; reuse R745 and the original R717 traces."""
import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile

from p41_public_actions_recovery import publish, read, save, sha

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R748-public-signed-CM-root-request.json"
WORKFLOW = REPO/".github/workflows/serre-R748-original-signed-CM-root.yml"
RESULT = "R748-original-signed-CM-root-p41"
FINAL = "R748-original-signed-root-and-Hodge-first-jets.json"
REPOSITORY = "Rogerhu12/math-research-public"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise SystemExit("Actual R748 arithmetic runs only in the public repository Actions.")


def output():
    return Path(os.environ["RUNNER_TEMP"])/"serre-cartier"/RESULT/"output"


def safe_sha(path):
    return sha(path) if Path(path).is_file() else None


def pinned_file(directory, name, expected):
    candidates = [p for p in Path(directory).rglob(name) if p.is_file() and sha(p) == expected]
    if not candidates:
        raise ValueError("No retained file matches the fixed SHA: "+name)
    return candidates[0]


def download(run_id, artifact, directory):
    directory.mkdir(parents=True, exist_ok=True)
    marker = directory/"R748-download-complete.json"
    if marker.exists():
        prior = read(marker)
        assert prior == {"run_id": str(run_id), "artifact": artifact}
        return
    subprocess.run(["gh", "run", "download", str(run_id), "--repo", REPOSITORY,
                    "--name", artifact, "--dir", str(directory)], check=True)
    save(marker, {"run_id": str(run_id), "artifact": artifact})


def retained_hodge(item, out):
    spec = item["retained_hodge"]
    archive = out.parent/"retained-R745-artifact"
    download(spec["run_id"], spec["artifact"], archive)
    dest = out.parent/"retained-R745"
    dest.mkdir(parents=True, exist_ok=True)
    records = []
    for name, expected in spec["files"].items():
        source = pinned_file(archive, name, expected)
        target = dest/name
        shutil.copyfile(source, target)
        records.append({"file": name, "sha256": sha(target), "bytes": target.stat().st_size})
    inputs = next(archive.rglob("public-actions-input.json"))
    original = read(inputs)
    assert original["source_commit"] == spec["source_commit"]
    assert original["source_repository"] == REPOSITORY
    assert original["core_sha256"] == spec["source_sha256"]
    cert = read(dest/"p41-original-Hodge-input-certificate.json")
    assert cert["complete"] and cert["source_sha256"] == spec["source_sha256"]
    assert cert["c1_raw_transport"] == "zeta^2" and cert["original_norm_mod_p"] == [40, 0]
    save(out/"retained-input-receipt.json", {
        "R745": spec, "files": records, "R717": item["retained_norm"],
        "original_finite_fiber_or_trace_repeated": False})
    return dest


def restore_requested_stages(item, out):
    spec = item.get("resume")
    if not spec:
        return
    archive = out.parent/"retained-R748-partial-artifact"
    download(spec["run_id"], spec["artifact"], archive)
    for name, expected in spec["files"].items():
        assert Path(name).name == name
        source = pinned_file(archive, name, expected)
        target = out/name
        if target.exists():
            assert sha(target) == expected
        else:
            shutil.copyfile(source, target)
    save(out/"resume-receipt.json", {"restored": spec, "completed_stages_recomputed": False})


def completed_guard(item, out):
    folder = TOPIC/"computations"/RESULT
    if not folder.exists():
        return False
    for path in sorted(folder.glob("*/"+FINAL), reverse=True):
        prior = read(path)
        if not prior.get("complete") or not prior.get("original_sign_certified"):
            continue
        cfg = prior.get("configuration", {})
        tag = cfg.get("phase_tag", {})
        if tag.get("source_sha256") != item["core_sha256"]:
            continue
        if (cfg.get("precision_bits"), cfg.get("cutoff"), cfg.get("E6_cutoff")) != (
                item["precision_bits"], item["cutoff"], item["E6_cutoff"]):
            continue
        run = read(path.parent/"run-receipt.json")
        assert run["complete"]
        artifact = "serre-cartier-"+RESULT+"-"+run["workflow_run_id"]+"-"+run["workflow_attempt"]
        archive = out.parent/"retained-R748-complete-artifact"
        download(run["workflow_run_id"], artifact, archive)
        original = pinned_file(archive, FINAL, sha(path))
        for stage in prior["stage_files"]:
            source = pinned_file(archive, stage["file"], stage["sha256"])
            shutil.copyfile(source, out/stage["file"])
        shutil.copyfile(original, out/FINAL)
        save(out/"reuse-complete-receipt.json", {
            "previous_workflow_run_id": run["workflow_run_id"], "artifact": artifact,
            "certificate_sha256": sha(path), "same_source_sha256": item["core_sha256"],
            "same_parameters": True, "actual_arithmetic_repeated": False})
        return True
    return False


def source_archive(item, out):
    paths = [REPO/"README.md", TOPIC/"README.md", REQUEST, WORKFLOW,
             Path(__file__), S/item["core"], TOPIC/item["method"],
             S/"p41_public_actions_recovery.py"]
    paths += [TOPIC/rel for rel in item["dependencies"]]
    archive = out/"R748-source-and-request.tar.gz"
    with tarfile.open(archive, "w:gz") as tf:
        for path in paths:
            assert path.is_file(), str(path)
            tf.add(path, arcname=str(path.relative_to(REPO)), recursive=False)
    save(out/"R748-source-manifest.json", {
        "files": [{"file": str(path.relative_to(REPO)), "sha256": sha(path),
                   "bytes": path.stat().st_size} for path in paths],
        "archive": archive.name, "archive_sha256": sha(archive)})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method = S/item["core"], TOPIC/item["method"]
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    # These receipts are written before archives or retained downloads so an
    # early checkout/input failure is itself preserved and publishable.
    save(out/"run-receipt.json", {"result": RESULT, "complete": False,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "error": "Not completed; initial receipt written before source/input checks."})
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_commit": source,
        "source_repository": REPOSITORY, "request_sha256": sha(REQUEST),
        "driver_sha256": sha(__file__), "core_sha256": safe_sha(core),
        "method_sha256": safe_sha(method), "workflow_sha256": safe_sha(WORKFLOW),
        "root_readme_sha256": safe_sha(REPO/"README.md"),
        "topic_readme_sha256": safe_sha(TOPIC/"README.md"),
        "retained_hodge": item["retained_hodge"], "retained_norm": item["retained_norm"],
        "precision_bits": item["precision_bits"], "cutoff": item["cutoff"],
        "E6_cutoff": item["E6_cutoff"],
        "run_url": "https://github.com/"+REPOSITORY+"/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "height_or_uniformity_exclusion_claimed": False})
    error, code, reused = None, 1, False
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        source_archive(item, out)
        hodge = retained_hodge(item, out)
        norm = item["retained_norm"]
        norm_poly, norm_receipt = TOPIC/norm["integer_polynomial"], TOPIC/norm["receipt"]
        assert sha(norm_poly) == norm["integer_polynomial_sha256"]
        assert sha(norm_receipt) == norm["receipt_sha256"]
        old = read(norm_receipt)
        assert old["complete"] and old["all_trace_roundings_unique"]
        assert old["configuration"]["finite_field"]["gamma"] == [7, 30]
        restore_requested_stages(item, out)
        reused = completed_guard(item, out)
        command = [sys.executable, "-u", str(core), "--output", str(out),
                   "--hodge", str(hodge/"original-p41-Hodge-q-expansions.json.gz"),
                   "--hodge-certificate", str(hodge/"p41-original-Hodge-input-certificate.json"),
                   "--integer-polynomial", str(norm_poly), "--norm-receipt", str(norm_receipt),
                   "--precision-bits", str(item["precision_bits"]),
                   "--cutoff", str(item["cutoff"]), "--e6-cutoff", str(item["E6_cutoff"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60)
            except subprocess.TimeoutExpired:
                error = "Runner budget reached; completed exact stages and partial extension retained."
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
    save(out/"run-receipt.json", {"result": RESULT, "p": 41,
        "complete": complete, "process_exit_code": code, "error": error,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(receipt_path) if receipt_path.exists() else None,
        "reused_completed_result": reused, "original_finite_fiber_AFE_DFT_repeated": False,
        "original_sign_certified": receipt.get("original_sign_certified", False),
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code,
                      "error": error, "reused_complete": reused}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["complete"] and run["result"] == RESULT
    receipt_path = out/"core-receipt.json"
    assert sha(receipt_path) == run["core_receipt_sha256"]
    receipt = read(receipt_path)
    assert receipt["complete"] and receipt["source_sha256"] == item["core_sha256"]
    assert receipt["original_sign_certified"] and receipt["all_six_Hodge_first_jets_exact"]
    final = out/FINAL
    assert sha(final) == receipt["certificate_sha256"]
    cert = read(final)
    assert cert["complete"] and cert["p"] == 41
    assert cert["exact_signed_square_identity"] and cert["original_sign_certified"]
    assert cert["original_CM_and_exact_algebraic_balls_overlap"]
    assert cert["opposite_sign_ball_disjoint"] and cert["all_six_Hodge_first_jets_exact"]
    assert cert["positive_embeddings"] == [1, 13, 19, 25, 31, 37]
    assert not cert["old_finite_fiber_AFE_or_DFT_recomputed"]
    assert not cert["quotient_map_beta_height_or_uniformity_exclusion_claimed"]
    assert len(cert["coarse_original_Hodge_primitive_first_coefficients"]) == 6
    for stage in cert["stage_files"]:
        assert sha(out/stage["file"]) == stage["sha256"]
    return 0


def publish_small(item, out):
    run_id = os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    artifact = "serre-cartier-"+RESULT+"-"+run_id
    pub = out.parent/"publication"
    pub.mkdir(parents=True, exist_ok=True)
    wanted = {"public-actions-input.json", "core-receipt.json", "run-receipt.json",
              "retained-input-receipt.json", "resume-receipt.json", "reuse-complete-receipt.json",
              "public-actions-run.log", FINAL, "R748-exact-real-field.json",
              "R748-exact-positive-root.json", "R748-original-CM-sign-balls.json",
              "R748-root-rounding-incomplete.json", "R748-source-and-request.tar.gz",
              "R748-source-manifest.json"}
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file():
            continue
        include = path.name in wanted and path.stat().st_size < 100_000
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path), "included_in_git": include, "artifact": artifact})
        if include:
            shutil.copyfile(path, pub/path.name)
    save(pub/"full-outputs-manifest.json", {"result": RESULT, "files": rows,
         "full_outputs_artifact": artifact,
         "reproducible_new_coefficient_intermediate_in_git": False})
    return publish(item, pub, artifact_prefix="serre-cartier")


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "publish", "verify"])
    args = parser.parse_args()
    request = read(REQUEST)
    assert request["session"] == "serre-public-resume-20261114"
    item, out = request["job"], output()
    if args.mode == "compute":
        return compute(item, out)
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())

