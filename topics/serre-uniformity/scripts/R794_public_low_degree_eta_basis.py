#!/usr/bin/env python3
"""Source-bound public runner for the finite original R794 eta basis selection.

Only completed R791 and R759 files are consumed.  Reproducible outputs and the
active input transfer bundle have one-day artifact retention, never Git/Release.
"""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile

from p41_public_actions_recovery import read, save, sha
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R794-public-low-degree-eta-basis-request.json"
RESULT = "R794-original-low-degree-eta-basis"
FINAL = "p41-original-low-degree-eta-basis-certificate.json"
BUNDLE = "R794-retained-producer-inputs.tar.gz"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def prepare(item, out):
    inputs = out.parent/"inputs"
    inputs.mkdir(parents=True, exist_ok=True)
    records = []
    assert set(item["retained_artifacts"]) == {"R791", "R759"}
    for label, producer in item["retained_artifacts"].items():
        downloaded = out.parent/("downloaded-"+label)
        target = inputs/label
        target.mkdir(parents=True, exist_ok=True)
        download(producer, downloaded, require_complete=True)
        mp = find_hash(downloaded, "full-outputs-manifest.json", producer["manifest_sha256"])
        manifest = read(mp)
        assert manifest["result"] == producer["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        shutil.copyfile(mp, target/mp.name)
        copied = []
        for name in ("run-receipt.json", "core-receipt.json", "public-actions-input.json"):
            source = find_hash(downloaded, name, entries[name]["sha256"])
            assert source.stat().st_size == entries[name]["bytes"]
            shutil.copyfile(source, target/name)
            copied.append({"file": name, "sha256": sha(source), "bytes": source.stat().st_size})
        run = read(target/"run-receipt.json")
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert run["source_commit"] == producer["source_commit"]
        assert run["workflow_run_id"] == producer["run_id"]
        certificate_name = producer["certificate_name"]
        cp = find_hash(downloaded, certificate_name, producer["files"][certificate_name])
        certificate = read(cp)
        assert certificate["complete"] is True and certificate["result"] == producer["result"]
        tag = certificate["configuration"]
        assert tag["source_sha256"] == producer["core_sha256"]
        assert tag["python_flint"] == "0.9.0"
        stages = {row["file"]: row for row in certificate["stages"]}
        for name, digest in producer["files"].items():
            assert Path(name).name == name and entries[name]["sha256"] == digest
            source = find_hash(downloaded, name, digest)
            assert source.stat().st_size == entries[name]["bytes"]
            if name != certificate_name:
                value = read(source)
                assert value["complete"] is True and value["configuration"] == tag
                assert stages[name]["sha256"] == digest
                assert stages[name]["bytes"] == source.stat().st_size
            shutil.copyfile(source, target/name)
            copied.append({"file": name, "sha256": digest, "bytes": source.stat().st_size})
        records.append({"producer": producer, "copied_files": copied,
                        "completed_run_source_and_artifact_digest_verified": True,
                        "all_mathematical_inputs_bound_to_completed_certificate": True})
    with tarfile.open(out/BUNDLE, "w:gz") as archive:
        for source in sorted(inputs.rglob("*")):
            if source.is_file():
                archive.add(source, arcname=source.relative_to(inputs).as_posix(), recursive=False)
    save(out/"retained-inputs-receipt.json", {"result": RESULT, "artifact_groups": records,
        "input_bundle": {"file": BUNDLE, "bytes": (out/BUNDLE).stat().st_size,
                         "sha256": sha(out/BUNDLE)},
        "purpose": "one-day active transfer of the exact consumed inputs for subsequent original function work",
        "old_periods_Hom_SVP_LLL_or_torsion_recomputed": False,
        "reproducible_outputs_saved_in_repository_or_release": False})
    return inputs


def manifest(out):
    files = [{"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}
             for path in sorted(out.iterdir())
             if path.is_file() and path.name != "full-outputs-manifest.json"]
    save(out/"full-outputs-manifest.json", {"result": RESULT, "files": files,
        "temporary_active_checkpoint_artifact": "serre-global-"+RESULT+"-"+
            os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"],
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_outputs_saved_in_repository_or_release": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "job": item,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        core, proof = S/item["core"], topic_path(item["proof"])
        assert sha(core) == item["core_sha256"] and sha(proof) == item["proof_sha256"]
        assert sha(topic_path(item["R793_proof"])) == item["R793_proof_sha256"]
        inputs = prepare(item, out)
        config = out/"job.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--inputs", str(inputs),
                   "--output", str(out), "--proof", str(proof), "--config", str(config)]
        with (out/"public-actions-run.log").open("w") as stream:
            result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                    timeout=item["budget_minutes"]*60, check=False)
        code = result.returncode
    except subprocess.TimeoutExpired as exc:
        code, error = 124, type(exc).__name__+": "+str(exc)
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
    complete = code == 0 and (out/FINAL).exists() and read(out/FINAL).get("complete") is True
    if not complete and code == 0:
        code = 1
    save(out/"run-receipt.json", {"result": RESULT, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "process_exit_code": code, "complete": complete, "error": error,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    manifest(out)
    if (out/"public-actions-run.log").exists():
        for line in (out/"public-actions-run.log").read_text().splitlines():
            if line.startswith("{") or not complete:
                print(line, flush=True)
    print(json.dumps({"result": RESULT, "complete": complete, "process_exit_code": code,
                      "error": error, "manifest_sha256": sha(out/"full-outputs-manifest.json")}), flush=True)
    return code


def verify(out):
    receipt = read(out/"run-receipt.json")
    assert receipt["complete"] is True and receipt["process_exit_code"] == 0
    certificate = read(out/FINAL)
    assert certificate["complete"] is True and certificate["result"] == RESULT
    initial = read(out/"public-actions-input.json")
    job = initial["job"]
    tag = certificate["configuration"]
    assert tag == {"result": RESULT, "p": 41, "source_sha256": job["core_sha256"],
        "python_flint": "0.9.0", "proof_sha256": job["proof_sha256"],
        "retained_artifacts": job["retained_artifacts"], "candidate_set": job["candidate_set"]}
    assert certificate["candidate_count"] == 149 and certificate["selected_basis_rank"] == 5
    assert certificate["actual_basis_and_sums_centered_rank"] == 5
    assert certificate["actual_all_candidates_centered_rank"] == 5
    assert certificate["minimum_total_degree_in_this_149_candidate_set"] is True
    assert certificate["global_Hom_lattice_degree_optimality_claimed"] is False
    assert certificate["all_original_F0_directions_preserved"] is True
    assert certificate["original_R791_basis_change_verified"] is True
    assert certificate["old_Hom_periods_SVP_or_LLL_recomputed"] is False
    assert certificate["actual_polar_divisors_eta_values_or_heights_computed"] is False
    for row in certificate["stages"]:
        path = out/row["file"]
        assert Path(row["file"]).name == row["file"]
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        stage = read(path)
        assert stage["complete"] is True and stage["configuration"] == tag
    kept = read(out/"retained-inputs-receipt.json")["input_bundle"]
    assert kept["file"] == BUNDLE and (out/BUNDLE).stat().st_size == kept["bytes"]
    assert sha(out/BUNDLE) == kept["sha256"]
    return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    mode = parser.parse_args().mode
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if mode == "verify":
        return verify(out)
    request = read(REQUEST)
    assert request["session"] == "serre-public-astra-20261115"
    return compute(request["job"], out)


if __name__ == "__main__":
    sys.exit(main())
