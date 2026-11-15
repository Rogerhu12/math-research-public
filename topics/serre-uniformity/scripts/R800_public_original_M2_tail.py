#!/usr/bin/env python3
"""Public R800 runner: only original M2 qY129..195, with exact old-input continuation."""
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
REQUEST = TOPIC/"notes/R800-public-original-M2-tail-request.json"
RESULT = "R800-original-M2-tail-129-195"
FINAL = "p41-original-M2-tail-129-195-certificate.json"
BUNDLE = "R800-retained-producer-inputs.tar.gz"
META = ("full-outputs-manifest.json", "run-receipt.json", "core-receipt.json", "public-actions-input.json")


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
    for key in ("R800_method_sha256", "R772_proof_sha256", "R781_proof_sha256",
                "R793_proof_sha256", "R786_core_helper_sha256", "R795_io_helper_sha256",
                "retained_artifacts"):
        assert tag[key] == item[key]
    assert tag["first_exponent"] == item["first_exponent"] == 129
    assert tag["last_exponent_exclusive"] == item["last_exponent_exclusive"] == 196
    assert tag["original_M2_recipe_sha256"] == "51113988c90b301cb6117fec5c294b77110e1826bf00229b7993ba82144f5d3d"
    assert tag["original_determinant_cosets_sha256"] == "759d6f7643032fa358a0da02417d576f5d6f89a3996f9e6fb4b3bf954c52ecac"
    assert tag["M2_dimension"] == 146 and tag["integer_scale"] == "6724"
    assert tag["E1_integer_scale"] == 82
    assert tag["original_qY"] == "qY=exp(2*pi*i*tau/82); original reference cusp coset0"
    assert tag["original_phase"] == "xi82=-xi41^21; original odd determinant lift"
    assert tag["real_tangent_parameter"] == "v=xi41^-10*qY; t=xi41+xi41^-1"
    assert tag["old_prefix_through_128_recomputed"] is False
    assert tag["ordinary_higher_powers_or_Laurent_recomputed"] is False


def stage_names(label):
    if label == "R771":
        return {"R771-original-level82-Eisenstein-label-group.json.gz"} | {
            "R771-Eisenstein-row-"+str(a).zfill(2)+".json.gz" for a in range(82)}
    if label == "R775":
        return {"R775-basis-M2.json.gz", "R775-determinant-cosets.json.gz"}
    assert label == "R786"
    return {"R786-exact-integral-E1-row-"+str(a).zfill(2)+".json.gz" for a in range(82)} | {
        "R786-exact-power-1-row-"+str(i).zfill(4)+".json.gz" for i in range(146)}


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
    assert run["process_exit_code"] == 0 and str(run["workflow_run_id"]) == str(producer["run_id"])
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
            with archive.extractfile(member) as source, target.open("wb") as destination:
                shutil.copyfileobj(source, destination)


def resume(item, out):
    previous = item.get("resume")
    if previous is None:
        save(out/"resume-receipt.json", {"result": RESULT, "resumed": False})
        return
    directory = out.parent/"resumed-artifact"
    download(previous, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", previous["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    ip = find_hash(directory, "public-actions-input.json", entries["public-actions-input.json"]["sha256"])
    rp = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
    initial, receipt = read(ip), read(rp)
    assert initial["source_commit"] == receipt["source_commit"] == previous["source_commit"]
    assert str(receipt["workflow_run_id"]) == str(previous["run_id"])
    old = initial["job"]
    for key in ("result", "p", "core_sha256", "R800_method_sha256", "R772_proof_sha256",
                "R781_proof_sha256", "R793_proof_sha256", "R786_core_helper_sha256",
                "R795_io_helper_sha256", "retained_artifacts", "first_exponent", "last_exponent_exclusive"):
        assert old[key] == item[key]
    bp = find_hash(directory, BUNDLE, entries[BUNDLE]["sha256"])
    assert bp.stat().st_size == entries[BUNDLE]["bytes"]
    unpack_bundle(bp, out.parent/"retained", item)
    copied = []
    for name, entry in entries.items():
        if not (name.startswith("R800-") and name.endswith(".json.gz")):
            continue
        source = find_hash(directory, name, entry["sha256"])
        assert source.stat().st_size == entry["bytes"]
        value = read(source)
        assert value["complete"] is True
        configuration(value["configuration"], item)
        shutil.copyfile(source, out/name)
        copied.append(entry)
    save(out/"resume-receipt.json", {"result": RESULT, "resumed": True, "producer": previous,
        "input_bundle_sha256": sha(bp), "copied_stages": copied,
        "all_completed_mathematical_stages_preserved": True,
        "unchanged_core_helpers_proofs_input_and_tail_interval_verified": True})


def prepare(item, out):
    inputs = out.parent/"retained"
    records = []
    assert set(item["retained_artifacts"]) == {"R771", "R775", "R786"}
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
        expected = stage_names(label)
        metadata_names = {producer["certificate_name"]}
        if label == "R786":
            inventory_spec = certificate["stages_manifest"]
            name = inventory_spec["file"]
            metadata_names.add(name)
            assert producer["files"][name] == inventory_spec["sha256"] == entries[name]["sha256"]
            path = find_hash(directory, name, inventory_spec["sha256"])
            assert path.stat().st_size == inventory_spec["bytes"] == entries[name]["bytes"]
            inventory = read(path)
            assert inventory["complete"] is True and inventory["configuration"] == tag
            stages = {row["file"]: row for row in inventory["files"]}
            assert certificate["exact_K_basis_prefix_bound_qY"] == 128
            assert certificate["basis_in_original_R775_saved_order"] is True
        else:
            stages = {row["file"]: row for row in certificate["stages"]}
        assert set(producer["files"]) == expected | metadata_names
        copied = []
        for filename, digest in producer["files"].items():
            assert Path(filename).name == filename and entries[filename]["sha256"] == digest
            source = find_hash(directory, filename, digest)
            assert source.stat().st_size == entries[filename]["bytes"]
            if filename != producer["certificate_name"]:
                value = read(source)
                assert value["complete"] is True and value["configuration"] == tag
                if filename in expected:
                    assert stages[filename]["sha256"] == digest
                    assert stages[filename]["bytes"] == entries[filename]["bytes"]
                if label == "R771" and filename.startswith("R771-Eisenstein-row-"):
                    assert value["last_exponent"] >= 195
                    assert len(value["series_by_second_coordinate"]) == 82
                if label == "R786" and filename.startswith("R786-exact-integral-E1-row-"):
                    assert value["bound_qY"] == 128 and value["scale"] == 82
                    assert len(value["sparse_series_by_second_coordinate"]) == 82
                    assert value["original_R771_finite_coefficients_verified"] is True
                if label == "R786" and filename.startswith("R786-exact-power-1-row-"):
                    assert value["weight"] == 2 and value["bound_qY"] == 128
                    assert value["integer_scale"] == "6724"
                    assert len(value["integer_qY_xi_coefficients"]) == 129
                    assert all(len(row) == 40 for row in value["integer_qY_xi_coefficients"])
                    assert value["original_R775_finite_coefficients_verified"] is True
            if source.resolve() != (target/filename).resolve():
                shutil.copyfile(source, target/filename)
            copied.append({"file": filename, "bytes": entries[filename]["bytes"], "sha256": digest})
        for filename, source in metadata_paths.items():
            if source.resolve() != (target/filename).resolve():
                shutil.copyfile(source, target/filename)
        records.append({"label": label, "producer": producer, "transferred_active_bundle": transferred,
                        "consumed_files": copied, "complete_configuration_and_stage_hashes_verified": True})
    # The old partial producer and its successful continuation have different tags;
    # their two shared immutable stage files, rather than entire labels, identify the mathematics.
    r786, r775 = item["retained_artifacts"]["R786"], item["retained_artifacts"]["R775"]
    old_certificate = read(inputs/"R786"/r786["certificate_name"])
    old_prefix = old_certificate["configuration"]["R775_completed_prefix_producer"]
    for name in ("R775-basis-M2.json.gz", "R775-determinant-cosets.json.gz"):
        assert old_prefix["files"][name] == r775["files"][name]
    with tarfile.open(out/BUNDLE, "w:gz") as archive:
        for path in sorted(inputs.rglob("*")):
            if path.is_file():
                archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
    save(out/"retained-inputs-receipt.json", {"result": RESULT, "groups": records,
        "input_bundle": {"file": BUNDLE, "bytes": (out/BUNDLE).stat().st_size, "sha256": sha(out/BUNDLE)},
        "purpose": "one-day active checkpoint transfer; no old mathematical stage is rerun",
        "shared_original_M2_and_coset_file_identities_verified": True,
        "old_q_coefficients_period_Hom_or_Laurent_recomputed": False,
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
        "new_exponents_inclusive": [129, 195], "old_prefix_recomputation_authorized": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        assert item["first_exponent"] == 129 and item["last_exponent_exclusive"] == 196
        core, method = S/item["core"], topic_path(item["method"])
        descent = topic_path(item["R772_proof"])
        tangent = topic_path(item["R781_proof"])
        rr = topic_path(item["R793_proof"])
        for path, key in ((core, "core_sha256"), (method, "R800_method_sha256"),
                          (descent, "R772_proof_sha256"), (tangent, "R781_proof_sha256"),
                          (rr, "R793_proof_sha256")):
            assert sha(path) == item[key]
        assert sha(S/"R786_exact_power5_short_basis.py") == item["R786_core_helper_sha256"]
        assert sha(S/"R795_exact_power6_short_basis.py") == item["R795_io_helper_sha256"]
        for filename, digest in item["io_helpers_sha256"].items():
            assert Path(filename).name == filename and sha(S/filename) == digest
        resume(item, out)
        retained = prepare(item, out)
        config = out/"job.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--retained", str(retained), "--output", str(out), "--method", str(method),
            "--descent-proof", str(descent), "--tangent-proof", str(tangent),
            "--rr-proof", str(rr), "--budget-minutes", str(item["budget_minutes"])]
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
    receipt = out/"core-receipt.json"
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "process_exit_code": code, "complete": complete, "error": error,
        "core_receipt_sha256": sha(receipt) if receipt.exists() else None,
        "execution_environment": "public-repository-github-actions",
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_exponents_inclusive": [129, 195], "actual_beta_eta_or_heights_computed": False})
    manifest(out)
    if (out/"public-actions-run.log").exists():
        for line in (out/"public-actions-run.log").read_text().splitlines():
            if line.startswith("{") or not complete:
                print(line, flush=True)
    print(json.dumps({"result": RESULT, "complete": complete, "process_exit_code": code, "error": error,
                      "manifest_sha256": sha(out/"full-outputs-manifest.json")}), flush=True)
    return code


def verify(out):
    run = read(out/"run-receipt.json")
    assert run["complete"] is True and run["process_exit_code"] == 0
    item = read(out/"public-actions-input.json")["job"]
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["p"] == 41 and cert["complete"] is True
    configuration(cert["configuration"], item)
    assert cert["original_M2_dimension"] == 146
    assert cert["first_exponent"] == 129 and cert["last_exponent_exclusive"] == 196
    assert cert["new_coefficient_count_per_row"] == 67
    assert cert["original_M2_integer_scale"] == "6724"
    assert cert["xi_coordinate_count"] == 40 and cert["real_t_coordinate_count"] == 20
    assert cert["actual_seed_indices"] == [0, 1, 2, 3, 11]
    assert cert["actual_seed_coset_tail_count"] == 200
    assert 1 <= cert["actual_E1_tail_row_count"] <= 82
    for key in ("all_original_recipes_and_old_prefix_identities_preserved",
                "all_new_original_mod739_coefficients_verified", "all_new_real_tangent_involutions_verified"):
        assert cert[key] is True
    for key in ("old_E1_M2_seed_or_other_prefixes_recomputed",
                "ordinary_power2_to8_Laurent_rational_maps_eta_or_heights_computed"):
        assert cert[key] is False
    core = read(out/"core-receipt.json")
    assert run["core_receipt_sha256"] == sha(out/"core-receipt.json")
    assert core["complete"] is True and core["source_sha256"] == item["core_sha256"]
    assert core["certificate_sha256"] == sha(out/FINAL)
    inventory = cert["stage_manifest"]
    path = out/inventory["file"]
    assert sha(path) == inventory["sha256"] and path.stat().st_size == inventory["bytes"]
    stages = read(path)
    assert stages["complete"] is True
    configuration(stages["configuration"], item)
    known = {entry["file"]: entry for entry in stages["files"]}
    for entry in stages["files"]:
        assert Path(entry["file"]).name == entry["file"]
        path = out/entry["file"]
        assert sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]
        value = read(path)
        assert value["complete"] is True
        configuration(value["configuration"], item)
    index_spec = cert["basis_tail_index"]
    assert index_spec == known[index_spec["file"]]
    index = read(out/index_spec["file"])
    assert index["dimension"] == 146 and index["integer_scale"] == "6724"
    assert index["first_exponent"] == 129 and index["last_exponent_exclusive"] == 196
    rows = index["tail_rows_in_original_order"]
    assert len(rows) == 146
    for i, entry in enumerate(rows):
        assert entry["file"] == "R800-original-M2-tail-row-"+str(i).zfill(4)+".json.gz"
        assert entry == known[entry["file"]]
        value = read(out/entry["file"])
        assert value["index"] == i and value["weight"] == 2 and value["integer_scale"] == "6724"
        assert value["first_exponent"] == 129 and value["last_exponent_exclusive"] == 196
        assert len(value["integer_qY_xi_coefficients"]) == 67
        assert all(len(row) == 40 for row in value["integer_qY_xi_coefficients"])
        assert len(value["integer_v_t_coefficients"]) == 67
        assert all(len(row) == 20 for row in value["integer_v_t_coefficients"])
        assert value["all_new_original_mod739_coefficients_verified"] is True
        assert value["all_new_real_tangent_involutions_verified"] is True
        assert value["old_prefix_recomputed"] is False and value["old_prefix_bytes_modified"] is False
        original_name = "R786-exact-power-1-row-"+str(i).zfill(4)+".json.gz"
        assert value["original_R786_prefix"]["file"] == original_name
        assert value["original_R786_prefix"]["sha256"] == item["retained_artifacts"]["R786"]["files"][original_name]
    assert len([name for name in known if name.startswith("R800-original-seed-tail-")]) == 200
    assert len([name for name in known if name.startswith("R800-original-E1-tail-row-")]) == cert["actual_E1_tail_row_count"]
    bundle = read(out/"retained-inputs-receipt.json")["input_bundle"]
    assert bundle["file"] == BUNDLE and sha(out/BUNDLE) == bundle["sha256"]
    assert (out/BUNDLE).stat().st_size == bundle["bytes"]
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

