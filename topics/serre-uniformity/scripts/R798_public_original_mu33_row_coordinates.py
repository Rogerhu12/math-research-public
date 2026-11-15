#!/usr/bin/env python3
"""Public R798 runner: original short-row coordinates and 690 required anchor products."""
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
REQUEST = TOPIC/"notes/R798-public-original-mu33-row-coordinates-request.json"
RESULT = "R798-original-mu33-row-coordinates"
FINAL = "p41-original-mu33-row-coordinate-certificate.json"
BUNDLE = "R798-retained-producer-inputs.tar.gz"
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
    for key in ("R798_proof_sha256", "R798_method_sha256", "R793_proof_sha256", "retained_artifacts"):
        assert tag[key] == item[key]
    assert tag["source_dimension"] == 690 and tag["target_dimension"] == 1506
    assert tag["full_coordinate_count"] == 1640 and tag["prefix_highest_exponent"] == 81
    assert tag["source_integer_scale"] == "304006671424"
    assert tag["target_integer_scale"] == "92420056270299898187776"
    assert tag["v_parameter"] == "v=xi41^-10*qY" and tag["t_parameter"] == "t=xi41+xi41^-1"
    assert tag["full_row_order"] == "20*n+r; 0<=n<=81; 0<=r<=19"
    assert tag["target_basis_order"] == "original R795/R775 ordinary power6 order"
    assert tag["target_coordinate_convention"] == "Psi_I(s)=C(s)_I; old coefficients c give A_I*c"
    assert tag["auxiliary_prime_start"] == item["auxiliary_prime_start"]
    assert tag["auxiliary_prime_policy"] == "increasing primes; actual short-matrix transpose RREF"
    assert tag["anchor_index"] == item["anchor_index"] == 0


def stage_names(label, producer):
    selection = producer["stage_selection"]
    if label == "R786":
        assert selection == {"ordinary_power": 3, "dimension": 690,
            "anchor_witness_powers": [1, 2], "anchor_witness_index": 0}
        names = {"R786-exact-power-3-row-"+str(i).zfill(4)+".json.gz" for i in range(690)}
        names |= {"R786-exact-power-"+str(power)+"-row-0000.json.gz" for power in (1, 2)}
        return names
    assert label == "R795" and selection == {"ordinary_power": 6, "dimension": 1506}
    return {"R795-exact-power-6-row-"+str(i).zfill(4)+".json.gz" for i in range(1506)}


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
    allowed = {label: stage_names(label, producer) | set(producer["files"]) | set(META)
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
    for key in ("result", "p", "core_sha256", "R798_proof_sha256", "R798_method_sha256",
                "R793_proof_sha256", "retained_artifacts", "auxiliary_prime_start", "anchor_index"):
        assert old[key] == item[key]
    bp = find_hash(directory, BUNDLE, entries[BUNDLE]["sha256"])
    assert bp.stat().st_size == entries[BUNDLE]["bytes"]
    unpack_bundle(bp, out.parent/"retained", item)
    copied = []
    for name, entry in entries.items():
        if not (name.startswith("R798-") and name.endswith(".json.gz")):
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
        "unchanged_core_proofs_input_and_coordinate_conventions_verified": True})


def prepare(item, out):
    inputs = out.parent/"retained"
    records = []
    assert set(item["retained_artifacts"]) == {"R786", "R795"}
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
        manifest_key = "stages_manifest" if label == "R786" else "stage_manifest"
        stage_spec = certificate[manifest_key]
        name = stage_spec["file"]
        assert producer["files"][name] == stage_spec["sha256"] == entries[name]["sha256"]
        sp = find_hash(directory, name, stage_spec["sha256"])
        assert sp.stat().st_size == stage_spec["bytes"] == entries[name]["bytes"]
        inventory = read(sp)
        assert inventory["complete"] is True and inventory["configuration"] == tag
        stages = {row["file"]: row for row in inventory["files"]}
        expected = stage_names(label, producer)
        meta_names = {producer["certificate_name"], name}
        if label == "R786":
            assert certificate["exact_K_basis_prefix_bound_qY"] == 128
            assert certificate["basis_in_original_R775_saved_order"] is True
            assert certificate["all_original_R775_mod739_short_series_compared"] is True
        else:
            assert certificate["ordinary_power"] == 6
            assert certificate["exact_power6_basis_dimension"] == 1506
            assert certificate["exact_K_basis_prefix_bound_qY"] == 81
            assert certificate["basis_integer_scale"] == "92420056270299898187776"
            assert certificate["all_original_real_cyclotomic_transports_verified"] is True
            assert certificate["basis_in_original_R775_saved_order"] is True
            ix = certificate["basis_index"]
            assert producer["files"][ix["file"]] == ix["sha256"]
            meta_names.add(ix["file"])
            ip = find_hash(directory, ix["file"], ix["sha256"])
            assert ip.stat().st_size == ix["bytes"]
            index = read(ip)
            assert index["complete"] is True and index["configuration"] == tag
            assert index["dimension"] == 1506
            assert [row["index"] for row in index["basis_rows"]] == list(range(1506))
            for position, row in enumerate(index["basis_rows"]):
                filename = "R795-exact-power-6-row-"+str(position).zfill(4)+".json.gz"
                assert row["file"] == filename and row["sha256"] == stages[filename]["sha256"]
                assert row["bytes"] == stages[filename]["bytes"]
        assert set(producer["files"]) == meta_names
        copied = []
        for filename in sorted(expected | meta_names):
            entry = entries[filename]
            digest = entry["sha256"]
            if filename in producer["files"]:
                assert digest == producer["files"][filename]
            source = find_hash(directory, filename, digest)
            assert source.stat().st_size == entry["bytes"]
            if filename != producer["certificate_name"]:
                value = read(source)
                assert value["complete"] is True and value["configuration"] == tag
                if filename != name:
                    assert stages[filename]["sha256"] == digest
                    assert stages[filename]["bytes"] == entry["bytes"]
                if filename in expected:
                    if label == "R786":
                        power = int(filename.split("-")[3])
                        assert value["weight"] == 2*power and value["bound_qY"] == 128
                        assert value["integer_scale"] == str(82**(2*power))
                        assert value["original_R775_finite_coefficients_verified"] is True
                        rows = value["integer_qY_xi_coefficients"]
                        assert len(rows) == 129 and all(len(row) == 40 for row in rows)
                    else:
                        assert value["weight"] == 12 and value["bound_qY"] == 81
                        assert value["integer_scale"] == "92420056270299898187776"
                        assert value["all_original_phase_involutions_verified"] is True
                        assert value["v_parameter"] == "v=xi41^-10*qY"
                        assert value["t_parameter"] == "t=xi41+xi41^-1"
                        rows = value["integer_v_t_coefficients"]
                        assert len(rows) == 82 and all(len(row) == 20 for row in rows)
            if source.resolve() != (target/filename).resolve():
                shutil.copyfile(source, target/filename)
            copied.append({"file": filename, "bytes": entry["bytes"], "sha256": digest})
        for filename, source in metadata_paths.items():
            if source.resolve() != (target/filename).resolve():
                shutil.copyfile(source, target/filename)
        records.append({"label": label, "producer": producer, "transferred_active_bundle": transferred,
                        "consumed_files": copied, "all_dynamic_stage_hashes_bound_to_original_manifest": True})
    with tarfile.open(out/BUNDLE, "w:gz") as archive:
        for path in sorted(inputs.rglob("*")):
            if path.is_file():
                archive.add(path, arcname=path.relative_to(inputs).as_posix(), recursive=False)
    save(out/"retained-inputs-receipt.json", {"result": RESULT, "groups": records,
        "input_bundle": {"file": BUNDLE, "bytes": (out/BUNDLE).stat().st_size, "sha256": sha(out/BUNDLE)},
        "purpose": "one-day active checkpoint transfer; no old mathematical stage is rerun",
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
        "actual_beta_eta_or_heights_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert item["producer_inputs_pending"] is False
        core, proof = S/item["core"], topic_path(item["proof"])
        method, rr = topic_path(item["method"]), topic_path(item["R793_proof"])
        assert sha(core) == item["core_sha256"]
        assert sha(proof) == item["R798_proof_sha256"]
        assert sha(method) == item["R798_method_sha256"]
        assert sha(rr) == item["R793_proof_sha256"]
        for filename, digest in item["io_helpers_sha256"].items():
            assert Path(filename).name == filename and sha(S/filename) == digest
        resume(item, out)
        retained = prepare(item, out)
        config = out/"job.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config),
            "--retained", str(retained), "--output", str(out), "--proof", str(proof),
            "--method", str(method), "--rr-proof", str(rr),
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
    receipt = out/"core-receipt.json"
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "process_exit_code": code, "complete": complete, "error": error,
        "core_receipt_sha256": sha(receipt) if receipt.exists() else None,
        "execution_environment": "public-repository-github-actions",
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "actual_beta_eta_or_heights_computed": False})
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
    assert cert["source_dimension"] == 690 and cert["target_dimension"] == 1506
    assert cert["full_coordinate_count"] == 1640 and cert["selected_coordinate_count"] == 1506
    assert cert["complement_coordinate_count"] == 134
    assert cert["source_integer_scale"] == "304006671424"
    assert cert["target_integer_scale"] == "92420056270299898187776"
    assert cert["actual_short_matrix_rank_mod_prime"] == 1506
    assert cert["actual_short_minor_determinant_mod_prime"] % cert["actual_short_minor_prime"] != 0
    assert cert["completed_anchor_products"] == 690 and cert["anchor_is_original_tau_cubed"] is True
    assert cert["all_anchor_products_full_1640_verified"] is True
    for key in ("original_basis_inverse_over_Q_computed", "original_V6_basis_coordinates_computed",
                "full_690_squared_table_generated", "old_qY_coefficients_period_Hom_or_Laurent_recomputed",
                "actual_polar_divisors_eta_beta_or_heights_computed"):
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
    for key in ("selected_rows", "anchor_recipe", "source_real_basis_index", "anchor_embedding_index"):
        entry = cert[key]
        assert entry == known[entry["file"]]
    selected = read(out/cert["selected_rows"]["file"])
    assert selected["actual_short_rank_mod_prime"] == 1506
    assert selected["prime"] == cert["actual_short_minor_prime"]
    assert selected["actual_short_minor_determinant_mod_prime"] == cert["actual_short_minor_determinant_mod_prime"]
    assert selected["old_R775_long_minor_reused_as_short_minor"] is False
    I, J = selected["selected_row_indices"], selected["complement_row_indices"]
    assert I == sorted(set(I)) and J == sorted(set(J))
    assert len(I) == 1506 and len(J) == 134 and sorted(I+J) == list(range(1640))
    anchor = read(out/cert["anchor_embedding_index"]["file"])
    assert len(anchor["products"]) == anchor["count"] == 690
    assert anchor["actual_anchor_modular_rank_computed"] is False
    for j, entry in enumerate(anchor["products"]):
        assert entry["source_indices"] == [0, j]
        assert entry["sha256"] == known[entry["file"]]["sha256"]
        product = read(out/entry["file"])
        assert product["source_indices"] == [0, j]
        assert product["selected_rows"] == cert["selected_rows"]
        assert len(product["selected_coordinates"]) == 1506
        assert len(product["complement_coordinates"]) == 134
        assert product["coordinate_denominator"] == "1"
        assert product["integer_scale"] == "92420056270299898187776"
        assert product["all_1640_original_coordinate_products_verified"] is True
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

