#!/usr/bin/env python3
"""Public R796 runner: prepare the original quadratic chart, extend only on demand."""
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
from R786_public_exact_power5_short_basis import api, download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R796-public-original-CM-quadratic-chart-request.json"
RESULT = "R796-original-CM-quadratic-chart"
FINAL = "p41-original-CM-quadratic-chart-certificate.json"
BUNDLE = "R796-retained-producer-inputs.tar.gz"
META = ("full-outputs-manifest.json", "run-receipt.json", "core-receipt.json", "public-actions-input.json")
M2_RECIPE_SHA = "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def configuration(tag, item):
    assert tag["result"] == RESULT and tag["p"] == 41
    assert tag["source_sha256"] == item["core_sha256"] and tag["python_flint"] == "0.9.0"
    for key in ("R796_proof_sha256", "R796_method_sha256", "R793_proof_sha256", "retained_artifacts"):
        assert tag[key] == item[key]
    assert tag["original_M2_recipe_sha256"] == M2_RECIPE_SHA
    assert tag["cusp_highest_exponent"] == 27
    assert tag["cusp_coefficient_convention"] == "original integer xi41^0..39; qY^0..27; packed stride80"
    assert tag["CM_point"] == "original_P1" and tag["coarse_coordinate"] == "a-1"
    assert tag["adapted_basis_policy"] == "first value and tangent anchors; primitive Z[zeta] columns"
    assert tag["monomial_order_policy"] == "lexicographic (a,b),0<=a<=b<=144"
    assert tag["auxiliary_prime_start"] == item["auxiliary_prime_start"]


def producer_metadata(directory, producer):
    mp = find_hash(directory, "full-outputs-manifest.json", producer["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == producer["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    paths = {"full-outputs-manifest.json": mp}
    for name in META[1:]:
        paths[name] = find_hash(directory, name, entries[name]["sha256"])
        assert paths[name].stat().st_size == entries[name]["bytes"]
    run, core, initial = (read(paths[name]) for name in META[1:])
    assert run["result"] == producer["result"] and run["complete"] is True
    assert run["process_exit_code"] == 0 and run["workflow_run_id"] == producer["run_id"]
    assert run["source_commit"] == producer["source_commit"]
    assert run["core_receipt_sha256"] == sha(paths["core-receipt.json"])
    assert core["complete"] is True and core["source_sha256"] == producer["core_sha256"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["source_commit"] == producer["source_commit"]
    assert initial["core_sha256"] == producer["core_sha256"]
    name = producer["certificate_name"]
    assert core["certificate_sha256"] == producer["files"][name] == entries[name]["sha256"]
    cp = find_hash(directory, name, producer["files"][name])
    assert cp.stat().st_size == entries[name]["bytes"]
    certificate = read(cp)
    assert certificate["complete"] is True and certificate["result"] == producer["result"]
    assert certificate["configuration"]["source_sha256"] == producer["core_sha256"]
    assert certificate["configuration"]["python_flint"] == "0.9.0"
    return entries, paths, certificate


def unpack_bundle(path, inputs, item):
    allowed = {label: set(producer["files"]) | set(META)
               for label, producer in item["retained_artifacts"].items()}
    with tarfile.open(path, "r:gz") as archive:
        for member in archive.getmembers():
            relative = Path(member.name)
            assert not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and member.isfile()
            label, filename = relative.parts
            assert label in allowed and filename in allowed[label]
            target = inputs/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as source, target.open("wb") as dest:
                shutil.copyfileobj(source, dest)


def resume(item, out):
    resumed = item.get("resume")
    if not resumed:
        save(out/"resume-receipt.json", {"result": RESULT, "resumed": False})
        return
    directory = out.parent/"resumed-artifact"
    download(resumed, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", resumed["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    ip = find_hash(directory, "public-actions-input.json", entries["public-actions-input.json"]["sha256"])
    rp = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
    initial, receipt = read(ip), read(rp)
    assert initial["source_commit"] == receipt["source_commit"] == resumed["source_commit"]
    assert receipt["workflow_run_id"] == resumed["run_id"]
    old = initial["job"]
    for key in ("result", "p", "core_sha256", "R796_proof_sha256", "R796_method_sha256",
                "R793_proof_sha256", "retained_artifacts", "auxiliary_prime_start"):
        assert old[key] == item[key]
    assert item["requested_jet_length"] >= old["requested_jet_length"]
    bp = find_hash(directory, BUNDLE, entries[BUNDLE]["sha256"])
    assert bp.stat().st_size == entries[BUNDLE]["bytes"]
    unpack_bundle(bp, out.parent/"retained", item)
    copied = []
    for name, entry in entries.items():
        if not (name.startswith("R796-") and name.endswith(".json.gz")):
            continue
        source = find_hash(directory, name, entry["sha256"])
        assert source.stat().st_size == entry["bytes"]
        value = read(source)
        assert value["complete"] is True
        configuration(value["configuration"], item)
        shutil.copyfile(source, out/name)
        copied.append(entry)
    save(out/"resume-receipt.json", {"result": RESULT, "resumed": True, "producer": resumed,
        "previous_request_jet_length": old["requested_jet_length"],
        "new_request_jet_length": item["requested_jet_length"],
        "input_bundle_sha256": sha(bp), "copied_stages": copied,
        "all_completed_mathematical_stages_preserved": True,
        "unchanged_core_proofs_input_and_chart_conventions_verified": True})


def prepare(item, out):
    inputs = out.parent/"retained"
    records = []
    assert set(item["retained_artifacts"]) == {"R786", "R790"}
    for label, producer in item["retained_artifacts"].items():
        target = inputs/label
        target.mkdir(parents=True, exist_ok=True)
        transferred = (target/"full-outputs-manifest.json").exists()
        if transferred:
            directory = target
            metadata = api("repos/Rogerhu12/math-research-public/actions/runs/"+producer["run_id"])
            assert metadata["head_sha"] == producer["source_commit"]
            assert metadata["status"] == "completed" and metadata["conclusion"] == "success"
        else:
            directory = out.parent/("downloaded-"+label)
            download(producer, directory, require_complete=True)
        entries, metadata_paths, certificate = producer_metadata(directory, producer)
        tag = certificate["configuration"]
        stage_key = "stages_manifest" if label == "R786" else "stage_manifest"
        stage_spec = certificate[stage_key]
        name = stage_spec["file"]
        assert producer["files"][name] == stage_spec["sha256"] == entries[name]["sha256"]
        stage_path = find_hash(directory, name, stage_spec["sha256"])
        assert stage_path.stat().st_size == stage_spec["bytes"] == entries[name]["bytes"]
        stage_manifest = read(stage_path)
        assert stage_manifest["complete"] is True and stage_manifest["configuration"] == tag
        stages = {row["file"]: row for row in stage_manifest["files"]}
        if label == "R786":
            assert tag["R775_completed_prefix_producer"]["files"]["R775-basis-M2.json.gz"] == M2_RECIPE_SHA
            expected = {"R786-exact-power-1-row-"+str(i).zfill(4)+".json.gz" for i in range(146)}
        else:
            assert tag["retained_artifacts"]["R775"]["files"]["R775-basis-M2.json.gz"] == M2_RECIPE_SHA
            assert certificate["original_psi_values_and_first_coarse_jets_verified"] is True
            assert certificate["M2_dimension"] == 146 and certificate["cm_jet_order"] == 5
            assert certificate["original_M2_scale"] == "6724"
            expected = {"R790-M2-CM-jet-"+str(i).zfill(4)+".json.gz" for i in range(146)}
        assert set(producer["files"]) == expected | {producer["certificate_name"], name}
        copied = []
        for filename, digest in producer["files"].items():
            assert Path(filename).name == filename and entries[filename]["sha256"] == digest
            source = find_hash(directory, filename, digest)
            assert source.stat().st_size == entries[filename]["bytes"]
            if filename not in (producer["certificate_name"], name):
                assert stages[filename]["sha256"] == digest
                assert stages[filename]["bytes"] == entries[filename]["bytes"]
                value = read(source)
                assert value["complete"] is True and value["configuration"] == tag
            if source.resolve() != (target/filename).resolve():
                shutil.copyfile(source, target/filename)
            copied.append({"file": filename, "bytes": entries[filename]["bytes"], "sha256": digest})
        for filename, source in metadata_paths.items():
            if source.resolve() != (target/filename).resolve():
                shutil.copyfile(source, target/filename)
        records.append({"label": label, "producer": producer, "transferred_active_bundle": transferred,
                        "consumed_files": copied, "complete_configuration_and_original_M2_identity_verified": True})
    with tarfile.open(out/BUNDLE, "w:gz") as archive:
        for path in sorted(inputs.rglob("*")):
            if path.is_file():
                archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
    save(out/"retained-inputs-receipt.json", {"result": RESULT, "groups": records,
        "original_M2_recipe_sha256": M2_RECIPE_SHA,
        "input_bundle": {"file": BUNDLE, "bytes": (out/BUNDLE).stat().st_size, "sha256": sha(out/BUNDLE)},
        "purpose": "one-day active checkpoint transfer; no old mathematical stage is rerun",
        "old_CM_values_M2_q_coefficients_or_Laurent_recomputed": False,
        "reproducible_outputs_saved_in_repository_or_release": False})
    return inputs


def manifest(out):
    rows = [{"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}
            for path in sorted(out.iterdir())
            if path.is_file() and path.name != "full-outputs-manifest.json"]
    save(out/"full-outputs-manifest.json", {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_artifact": "serre-global-"+RESULT+"-"+
            os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"],
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_outputs_saved_in_repository_or_release": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41, "job": item,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "driver_sha256": sha(__file__), "core_sha256": item["core_sha256"],
        "request_sha256": sha(REQUEST), "root_readme_sha256": sha(REPO/"README.md"),
        "topic_readme_sha256": sha(TOPIC/"README.md"), "workflow_sha256": sha(REPO/item["workflow"]),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "requested_jet_length": item["requested_jet_length"],
        "actual_beta_eta_or_heights_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False and item["requested_jet_length"] >= 2
        core, proof = S/item["core"], topic_path(item["proof"])
        method, rr = topic_path(item["method"]), topic_path(item["R793_proof"])
        assert sha(core) == item["core_sha256"]
        assert sha(proof) == item["R796_proof_sha256"]
        assert sha(method) == item["R796_method_sha256"]
        assert sha(rr) == item["R793_proof_sha256"]
        resume(item, out)
        retained = prepare(item, out)
        config = out/"job.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--retained", str(retained), "--output", str(out), "--proof", str(proof),
            "--method", str(method), "--rr-proof", str(rr),
            "--target-length", str(item["requested_jet_length"]),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                     timeout=item["budget_minutes"]*60, check=False)
        code = process.returncode
    except subprocess.TimeoutExpired as exc:
        code, error = 124, type(exc).__name__+": "+str(exc)
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
    complete = code == 0 and (out/FINAL).exists() and read(out/FINAL).get("complete") is True
    if not complete and code == 0:
        code = 1
    core_receipt = out/"core-receipt.json"
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "process_exit_code": code, "complete": complete, "error": error,
        "core_receipt_sha256": sha(core_receipt) if core_receipt.exists() else None,
        "requested_jet_length": item["requested_jet_length"],
        "execution_environment": "public-repository-github-actions",
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_beta_eta_or_heights_computed": False})
    manifest(out)
    if (out/"public-actions-run.log").exists():
        for line in (out/"public-actions-run.log").read_text().splitlines():
            if line.startswith("{") or not complete:
                print(line, flush=True)
    print(json.dumps({"result": RESULT, "complete": complete, "process_exit_code": code, "error": error,
        "manifest_sha256": sha(out/"full-outputs-manifest.json"),
        "requested_jet_length": item["requested_jet_length"]}), flush=True)
    return code


def verify(out):
    run = read(out/"run-receipt.json")
    assert run["complete"] is True and run["process_exit_code"] == 0
    initial = read(out/"public-actions-input.json")
    item = initial["job"]
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["p"] == 41 and cert["complete"] is True
    configuration(cert["configuration"], item)
    assert cert["original_M2_dimension"] == 146 and cert["selected_WP2_monomials"] == 416
    assert cert["global_quadratic_relations"] == 144 and cert["all_144_global_relations_verified"] is True
    assert cert["implicit_x_Jacobian_at_original_CM_point"] == "identity_144"
    assert cert["requested_jet_length"] == cert["completed_jet_length"] == item["requested_jet_length"]
    assert cert["cusp_verification_highest_exponent"] == 27
    assert cert["source_CM_values_or_first_derivatives_recomputed"] is False
    assert cert["old_E1_M2_or_Laurent_prefixes_recomputed"] is False
    assert cert["actual_beta_eta_or_heights_computed"] is False
    stage_spec = cert["stage_manifest"]
    stage_path = out/stage_spec["file"]
    assert sha(stage_path) == stage_spec["sha256"] and stage_path.stat().st_size == stage_spec["bytes"]
    stages = read(stage_path)
    assert stages["complete"] is True
    configuration(stages["configuration"], item)
    for entry in stages["files"]:
        assert Path(entry["file"]).name == entry["file"]
        path = out/entry["file"]
        assert sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]
        value = read(path)
        assert value["complete"] is True
        configuration(value["configuration"], item)
    for key in ("basis_adaptation", "selected_monomials", "global_relations", "ratio_jets"):
        entry = cert[key]
        path = out/entry["file"]
        assert sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]
    kept = read(out/"retained-inputs-receipt.json")["input_bundle"]
    assert kept["file"] == BUNDLE and sha(out/BUNDLE) == kept["sha256"]
    assert (out/BUNDLE).stat().st_size == kept["bytes"]
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

