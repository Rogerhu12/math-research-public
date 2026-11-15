#!/usr/bin/env python3
"""Consume the completed R786/R781 inputs and certify one original L relation."""
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
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R787-public-original-power5-relation-request.json"
RESULT = "R787-original-power5-function-relation"
FINAL = "p41-original-power5-function-relation-certificate.json"
REFERENCE = "full-outputs-manifest-reference.json"
INPUT_BUNDLE = "R787-retained-producer-inputs.tar.gz"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual arithmetic belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC / path


def prepare_inputs(item, out):
    inputs = out.parent / "retained"
    records = []
    assert set(item["retained_artifacts"]) == {"R781", "R786"}
    for label, spec in item["retained_artifacts"].items():
        directory = out.parent / ("downloaded-" + label)
        target = inputs / label
        target.mkdir(parents=True, exist_ok=True)
        reused_transfer = (target / "full-outputs-manifest.json").exists()
        if reused_transfer:
            directory = target
            metadata = api("repos/Rogerhu12/math-research-public/actions/runs/" + spec["run_id"])
            assert metadata["head_sha"] == spec["source_commit"]
            assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
        else:
            download(spec, directory, require_complete=True)
        mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        rp = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
        run = read(rp)
        assert run["source_commit"] == spec["source_commit"]
        assert run["workflow_run_id"] == spec["run_id"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        cn = spec["certificate_name"]
        certificate_sha = spec["files"][cn]
        assert entries[cn]["sha256"] == certificate_sha
        cp = find_hash(directory, cn, certificate_sha)
        certificate = read(cp)
        assert certificate["complete"] is True and certificate["result"] == spec["result"]
        tag = certificate["configuration"]
        assert tag["source_sha256"] == spec["core_sha256"]
        assert tag["python_flint"] == "0.9.0"
        if label == "R786":
            assert certificate["exact_power5_basis_dimension"] == 1234
            assert certificate["exact_K_basis_prefix_bound_qY"] == 128
            assert certificate["basis_integer_scale"] == "13744803133596058624"
            assert certificate["all_original_R775_mod739_short_series_compared"] is True
            assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
            index_spec = certificate["basis_index"]
            assert entries[index_spec["file"]]["sha256"] == index_spec["sha256"]
            ip = find_hash(directory, index_spec["file"], index_spec["sha256"])
            assert ip.stat().st_size == index_spec["bytes"]
            index = read(ip)
            assert index["complete"] is True and index["configuration"] == tag
            assert index["dimension"] == 1234 and index["bound_qY"] == 128
            rows = index["basis_rows"]
            assert len(rows) == 1234 and [r["index"] for r in rows] == list(range(1234))
            for row in rows:
                assert entries[row["file"]]["sha256"] == row["sha256"]
                assert entries[row["file"]]["bytes"] == row["bytes"]
            needed = [index_spec["file"]] + [row["file"] for row in rows]
        else:
            assert certificate["original_map_index"] == 4
            assert certificate["original_map_degree"] == "1206"
            assert certificate["actual_cusp_order"] == 1
            assert certificate["normalized_Laurent_R_bound"] == 142
            assert certificate["all_original_real_tangent_phases_verified"] is True
            assert certificate["all_recurrence_coefficients_verified_exactly"] is True
            needed = ["R781-original-real-field-input.json.gz"]
            needed += ["R781-inverse-free-Laurent-" + str(n).zfill(3) + ".json.gz"
                       for n in range(130)]
        assert len(needed) == len(set(needed))
        for name in needed:
            row = entries[name]
            source = find_hash(directory, name, row["sha256"])
            assert source.stat().st_size == row["bytes"]
            data = read(source)
            assert data["complete"] is True and data["configuration"] == tag
            if source.resolve() != (target / name).resolve():
                shutil.copyfile(source, target / name)
        for source, name in ((mp, "full-outputs-manifest.json"), (cp, cn), (rp, "run-receipt.json")):
            if source.resolve() != (target / name).resolve():
                shutil.copyfile(source, target / name)
        records.append({"label": label, "producer": spec,
                        "producer_run_and_source_verified": True,
                        "original_artifact_digest_verified_on_this_download": not reused_transfer,
                        "inputs_from_verified_active_resume_bundle": reused_transfer,
                        "certificate_sha256": certificate_sha,
                        "complete_source_bound_files_copied": len(needed),
                        "all_copied_file_sizes_and_sha256_verified": True,
                        "source_inventory": "producer full-outputs-manifest.json"})
    save(out / "retained-inputs-receipt.json", {
        "artifact_groups": records, "completed_producer_mathematics_recomputed": False})
    bundle = out / INPUT_BUNDLE
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
    directory = out.parent / "downloaded-R787-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    bundle_rows = [row for row in manifest["files"] if row["file"] == INPUT_BUNDLE]
    assert len(bundle_rows) == 1, "The active continuation must retain its producer inputs."
    bundle_row = bundle_rows[0]
    bundle = find_hash(directory, INPUT_BUNDLE, bundle_row["sha256"])
    assert bundle.stat().st_size == bundle_row["bytes"]
    target = out.parent / "retained"
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in ("R781", "R786")
            path = target / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            data = archive.extractfile(member).read()
            if path.exists():
                assert path.read_bytes() == data
            else:
                path.write_bytes(data)
    shutil.copyfile(bundle, out / INPUT_BUNDLE)
    copied = 0
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R787-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = find_hash(directory, name, row["sha256"])
        assert source.stat().st_size == row["bytes"]
        data = read(source)
        tag = data["configuration"]
        assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
        assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
        assert tag["R787_method_sha256"] == item["R787_method_sha256"]
        assert tag["R781_field_core_sha256"] == item["field_core_sha256"]
        assert tag["retained_artifacts"] == item["retained_artifacts"]
        assert data["complete"] is True
        if (out / name).exists():
            assert sha(out / name) == row["sha256"]
        else:
            shutil.copyfile(source, out / name)
        copied += 1
    assert copied, "No compatible completed stages in the continuation artifact"
    save(out / "resume-receipt.json", {
        "producer": spec, "same_exact_core_sha256": item["core_sha256"],
        "complete_files_copied": copied, "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = ("serre-global-" + RESULT + "-" + os.environ["GITHUB_RUN_ID"] + "-"
                + os.environ["GITHUB_RUN_ATTEMPT"])
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path), "artifact": artifact,
                     "included_in_git": path.name in SMALL and path.stat().st_size < 100_000})
    mp = out / "full-outputs-manifest.json"
    save(mp, {"result": RESULT, "files": rows,
              "temporary_active_checkpoint_artifact": artifact,
              "reproducible_relation_tables_in_git_or_release": False,
              "temporary_active_checkpoint_retention_days": 1})
    save(out / REFERENCE, {"result": RESULT, "manifest_file": mp.name,
                          "manifest_sha256": sha(mp), "manifest_bytes": mp.stat().st_size,
                          "file_count": len(rows), "full_outputs_artifact": artifact,
                          "manifest_in_git": mp.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, field_core = S / item["core"], S / item["field_core"]
    method, proof = topic_path(item["method"]), topic_path(item["proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out / "public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item, "core_sha256": sha(core),
        "field_core_sha256": sha(field_core), "method_sha256": sha(method),
        "proof_sha256": sha(proof), "driver_sha256": sha(__file__),
        "request_sha256": sha(REQUEST), "root_readme_sha256": sha(REPO / "README.md"),
        "topic_readme_sha256": sha(TOPIC / "README.md"),
        "publication_helper_sha256": sha(S / "p41_public_actions_recovery.py"),
        "download_helper_sha256": sha(S / "R786_public_exact_power5_short_basis.py"),
        "workflow_sha256": sha(REPO / item["workflow"]),
        "retained_artifacts": item["retained_artifacts"], "resume": item.get("resume"),
        "budget_minutes": item["budget_minutes"],
        "arithmetic": "original L relation from completed original power5 basis and Laurent stages",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/" + os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_y_map_claimed_before_run": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"]
        assert sha(field_core) == item["field_core_sha256"]
        assert sha(method) == item["R787_method_sha256"]
        assert sha(proof) == item["R786_proof_sha256"]
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent / "job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--retained", str(inputs),
                   "--output", str(out), "--config", str(config), "--proof", str(proof),
                   "--method", str(method), "--field-core", str(field_core),
                   "--budget-minutes", str(item["budget_minutes"])]
        with (out / "public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"] * 60 + 120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; source-bound complete stages retained for continuation."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__ + ": " + str(exception)
    rp = out / "core-receipt.json"
    receipt = read(rp) if rp.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out / "run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete, "process_exit_code": code,
        "error": error, "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(rp) if rp.exists() else None,
        "actual_y_map_recovered": complete, "beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete,
                      "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out / "run-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True
    receipt = read(out / "core-receipt.json")
    assert sha(out / "core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"]
    assert sha(out / FINAL) == receipt["certificate_sha256"]
    cert = read(out / FINAL)
    assert cert["complete"] is True and cert["result"] == RESULT and cert["p"] == 41
    tag = cert["configuration"]
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    assert tag["R786_proof_sha256"] == item["R786_proof_sha256"]
    assert tag["R787_method_sha256"] == item["R787_method_sha256"]
    assert tag["R781_field_core_sha256"] == item["field_core_sha256"]
    assert tag["retained_artifacts"] == item["retained_artifacts"]
    assert cert["original_map_index"] == 4 and cert["original_map_degree"] == "1206"
    assert cert["exact_nonzero_A_B_relation_verified"] is True
    assert cert["original_full_L_retained"] is True
    assert cert["exact_verified_Laurent_exponents"] == [-1, 127]
    assert cert["exact_verified_t_coordinates"] == 20
    assert cert["actual_y_map_recovered"] is True and cert["beta_or_height_computed"] is False
    for key in ("relation_spec", "stage_manifest"):
        spec = cert[key]
        assert Path(spec["file"]).name == spec["file"]
        path = out / spec["file"]
        assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
        data = read(path)
        assert data["complete"] is True and data["configuration"] == tag
        if key == "stage_manifest":
            for row in data["files"]:
                assert Path(row["file"]).name == row["file"]
                path = out / row["file"]
                assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
    # Full characteristic-zero arithmetic is certified by the core once.
    # This pass only verifies the provenance and completed product hashes.
    return 0


def publish_small(item, out):
    if not (out / "full-outputs-manifest.json").exists():
        output_manifest(out)
    manifest = read(out / "full-outputs-manifest.json")
    pub = out.parent / "publication"
    pub.mkdir(parents=True, exist_ok=True)
    for row in manifest["files"]:
        if row["included_in_git"]:
            assert sha(out / row["file"]) == row["sha256"]
            shutil.copyfile(out / row["file"], pub / row["file"])
    shutil.copyfile(out / REFERENCE, pub / REFERENCE)
    if (out / "full-outputs-manifest.json").stat().st_size < 100_000:
        shutil.copyfile(out / "full-outputs-manifest.json", pub / "full-outputs-manifest.json")
    return publish(item, pub, artifact_prefix="serre-global")


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "publish", "verify"])
    args = parser.parse_args()
    out = Path(os.environ["RUNNER_TEMP"]) / "serre-global" / RESULT / "output"
    if args.mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out / "public-actions-input.json")["job"]
    assert item["result"] == RESULT
    return publish_small(item, out) if args.mode == "publish" else verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
