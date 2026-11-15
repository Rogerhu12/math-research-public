#!/usr/bin/env python3
"""R799: source-bound active inputs and only the new V6 tail/V7/V8 short bases."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import tarfile

from p41_public_actions_recovery import publish, read, save, sha
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R799-public-power7-power8-short-bases-request.json"
RESULT = "R799-original-power7-power8-short-bases"
FINAL = "p41-original-power7-power8-short-bases-certificate.json"
INPUT_BUNDLE = "R799-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R775", "R786", "R795"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
R775_POWER6 = "R775-basis-power-6.json.gz"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def plain_spec(row):
    return {key: row[key] for key in ("file", "bytes", "sha256")}


def bound_path(directory, entries, name):
    assert Path(name).name == name
    row = entries[name]
    path = find_hash(directory, name, row["sha256"])
    assert path.stat().st_size == row["bytes"]
    return path


def producer_metadata(directory, spec):
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == spec["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    paths = {"full-outputs-manifest.json": mp}
    for name in PRODUCER_META[1:]:
        paths[name] = bound_path(directory, entries, name)
    run, core, initial = (read(paths[name]) for name in PRODUCER_META[1:])
    assert run["result"] == spec["result"] and run["complete"] is True and run["process_exit_code"] == 0
    assert str(run["workflow_run_id"]) == str(spec["run_id"]) and run["source_commit"] == spec["source_commit"]
    assert run["core_receipt_sha256"] == sha(paths["core-receipt.json"])
    assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
    assert initial["result"] == spec["result"] and initial["source_commit"] == spec["source_commit"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["core_sha256"] == initial["job"]["core_sha256"] == spec["core_sha256"]
    name = spec["certificate_name"]
    assert entries[name]["sha256"] == spec["files"][name] == core["certificate_sha256"]
    paths[name] = bound_path(directory, entries, name)
    cert = read(paths[name])
    assert cert["complete"] is True and cert["result"] == spec["result"]
    assert cert["configuration"]["source_sha256"] == spec["core_sha256"]
    assert cert["configuration"]["python_flint"] == "0.9.0"
    return entries, paths, cert, initial


def allowed_group_name(label, spec, name):
    if name in set(PRODUCER_META)|set(spec["files"]):
        return True
    if label == "R786":
        match = re.fullmatch(r"R786-exact-power-([15])-row-(\d{4})\.json\.gz", name)
        return bool(match and ((match[1] == "1" and int(match[2]) in (0, 1, 73)) or
                               (match[1] == "5" and 0 <= int(match[2]) < 1234)))
    if label == "R795":
        match = re.fullmatch(r"R795-exact-power-6-row-(\d{4})\.json\.gz", name)
        return bool(match and 0 <= int(match[1]) < 1506)
    return False


def extract_bundle(bundle, target, specs, labels):
    target.mkdir(parents=True, exist_ok=True)
    seen = set()
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in labels
            group, name = relative.parts
            assert allowed_group_name(group, specs[group], name)
            assert str(relative) not in seen
            seen.add(str(relative))
            path = target/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            data = archive.extractfile(member).read()
            if path.exists():
                assert path.read_bytes() == data
            else:
                path.write_bytes(data)


def selected_group_files(directory, label, spec, power6=None, factors786=None):
    entries, paths, cert, initial = producer_metadata(directory, spec)
    selected = dict(spec["files"])
    if label == "R775":
        assert cert["power_basis_dimensions"]["6"] == 1506 and cert["all_recipes_defined_over_original_K"] is True
        stages = {row["file"]: row for row in cert["stages"]}
        assert stages[R775_POWER6]["sha256"] == selected[R775_POWER6]
        assert stages[R775_POWER6]["bytes"] == entries[R775_POWER6]["bytes"]
    elif label == "R786":
        assert power6 is not None and power6["rank"] == len(power6["basis"]) == 1506
        assert cert["basis_in_original_R775_saved_order"] is True
        assert cert["exact_power5_basis_dimension"] == 1234 and cert["exact_K_basis_prefix_bound_qY"] == 128
        for key in ("basis_index", "stages_manifest"):
            row = cert[key]
            assert entries[row["file"]]["bytes"] == row["bytes"] and selected[row["file"]] == row["sha256"]
        inventory = read(bound_path(directory, entries, cert["stages_manifest"]["file"]))
        assert inventory["complete"] is True and inventory["configuration"] == cert["configuration"]
        old_rows = {row["file"]: row for row in inventory["files"]}
        anchors = set()
        for original in power6["basis"]:
            recipe = original["recipe"]
            assert recipe["kind"] == "product" and recipe["left_power"] == 1 and recipe["right_power"] == 5
            anchors.add(recipe["left_index"])
            for side in ("left", "right"):
                power, index = recipe[side+"_power"], recipe[side+"_index"]
                assert (power == 1 and index in (0, 1, 73)) or (power == 5 and 0 <= index < 1234)
                name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
                assert plain_spec(old_rows[name]) == plain_spec(entries[name])
                selected[name] = old_rows[name]["sha256"]
        assert anchors == {0, 1, 73}
    else:
        assert label == "R795" and power6 is not None and factors786 is not None
        assert cert["exact_power6_basis_dimension"] == 1506 and cert["exact_K_basis_prefix_bound_qY"] == 81
        assert cert["basis_integer_scale"] == "92420056270299898187776"
        assert cert["basis_in_original_R775_saved_order"] is True
        assert cert["all_original_R775_mod739_short_series_compared"] is True
        assert cert["all_original_real_cyclotomic_transports_verified"] is True
        for key in ("basis_index", "stage_manifest"):
            row = cert[key]
            assert entries[row["file"]]["bytes"] == row["bytes"] and selected[row["file"]] == row["sha256"]
        index = read(bound_path(directory, entries, cert["basis_index"]["file"]))
        inventory = read(bound_path(directory, entries, cert["stage_manifest"]["file"]))
        for value in (index, inventory):
            assert value["complete"] is True and value["configuration"] == cert["configuration"]
        assert index["dimension"] == len(index["basis_rows"]) == 1506
        assert [row["index"] for row in index["basis_rows"]] == list(range(1506))
        old_rows = {row["file"]: row for row in inventory["files"]}
        for position, row in enumerate(index["basis_rows"]):
            name = "R795-exact-power-6-row-"+str(position).zfill(4)+".json.gz"
            assert row["file"] == name and plain_spec(row) == plain_spec(old_rows[name]) == plain_spec(entries[name])
            selected[name] = row["sha256"]
    for name, digest in selected.items():
        assert entries[name]["sha256"] == digest and allowed_group_name(label, spec, name)
        path = bound_path(directory, entries, name)
        if name != spec["certificate_name"]:
            data = read(path)
            assert data["complete"] is True and data["configuration"] == cert["configuration"]
            if label == "R786" and re.fullmatch(r"R786-exact-power-[15]-row-\d{4}\.json\.gz", name):
                assert data["bound_qY"] == 128 and data["weight"] in (2, 10)
                assert data["integer_scale"] == {2: "6724", 10: "13744803133596058624"}[data["weight"]]
                assert data["original_R775_finite_coefficients_verified"] is True
                assert len(data["integer_qY_xi_coefficients"]) == 129
                assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
            elif label == "R795" and re.fullmatch(r"R795-exact-power-6-row-\d{4}\.json\.gz", name):
                position = int(name[-12:-8])
                assert data["index"] == position and data["recipe"] == power6["basis"][position]["recipe"]
                assert data["weight"] == 12 and data["bound_qY"] == 81
                assert data["integer_scale"] == "92420056270299898187776"
                assert data["all_original_phase_involutions_verified"] is True
                assert data["original_R775_finite_coefficients_verified"] is True
                assert data["averaging_used"] is False and data["old_factor_rows_recomputed"] is False
                assert len(data["integer_qY_xi_coefficients"]) == len(data["integer_v_t_coefficients"]) == 82
                assert all(len(row) == 40 for row in data["integer_qY_xi_coefficients"])
                assert all(len(row) == 20 for row in data["integer_v_t_coefficients"])
                recipe = data["recipe"]
                assert len(data["original_R786_factor_rows"]) == 2
                for row, power, index in zip(data["original_R786_factor_rows"], (1, 5),
                                             (recipe["left_index"], recipe["right_index"])):
                    expected_name = "R786-exact-power-"+str(power)+"-row-"+str(index).zfill(4)+".json.gz"
                    assert row["file"] == expected_name and row["power"] == power and row["index"] == index
                    assert plain_spec(row) == plain_spec(factors786[expected_name])
        paths[name] = path
    return paths, cert, initial


def transfer(paths, target):
    target.mkdir(parents=True, exist_ok=True)
    for name, path in paths.items():
        destination = target/name
        if path.resolve() == destination.resolve():
            continue
        if destination.exists():
            assert sha(destination) == sha(path)
        else:
            shutil.copyfile(path, destination)


def prepare_inputs(item, out):
    specs = item["retained_artifacts"]
    assert set(specs) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified R799 input bundle"
    if not transferred:
        parent = out.parent/"downloaded-R795"
        download(specs["R795"], parent, require_complete=True)
        entries, _, parent_cert, parent_initial = producer_metadata(parent, specs["R795"])
        for label in ("R775", "R786"):
            assert parent_initial["job"]["retained_artifacts"][label] == specs[label]
            assert parent_cert["configuration"]["retained_artifacts"][label] == specs[label]
        bundle_spec = specs["R795"]["input_bundle"]
        assert bundle_spec["file"] == "R795-retained-producer-inputs.tar.gz"
        assert plain_spec(entries[bundle_spec["file"]]) == plain_spec(bundle_spec)
        bundle = bound_path(parent, entries, bundle_spec["file"])
        old_inputs = out.parent/"parent-retained-inputs"
        extract_bundle(bundle, old_inputs, specs, {"R775", "R786"})
        sources = {"R775": old_inputs/"R775", "R786": old_inputs/"R786", "R795": parent}
    else:
        sources = {label: inputs/label for label in LABELS}
    groups, power6, cert775, factors786 = [], None, None, None
    for label in ("R775", "R786", "R795"):
        paths, cert, initial = selected_group_files(sources[label], label, specs[label], power6, factors786)
        target = inputs/label
        transfer(paths, target)
        assert set(path.name for path in target.iterdir() if path.is_file()) == set(paths)
        if label == "R775":
            power6, cert775 = read(target/R775_POWER6), cert
        elif label == "R786":
            stages775 = {row["file"]: row for row in cert775["stages"]}
            old = cert["configuration"]["R775_completed_prefix_producer"]
            for name in ("R775-basis-M2.json.gz", "R775-basis-power-5.json.gz"):
                assert old["files"][name] == stages775[name]["sha256"]
            inventory = read(target/cert["stages_manifest"]["file"])
            factors786 = {row["file"]: row for row in inventory["files"]}
        else:
            for child in ("R775", "R786"):
                assert initial["job"]["retained_artifacts"][child] == specs[child]
                assert cert["configuration"]["retained_artifacts"][child] == specs[child]
        groups.append({"label": label, "producer": specs[label], "file_count": len(paths),
            "all_sizes_sha256_original_schemas_and_parent_identities_verified": True})
    if not (out/INPUT_BUNDLE).exists():
        with tarfile.open(out/INPUT_BUNDLE, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=str(path.relative_to(inputs)), recursive=False)
    save(out/"retained-inputs-receipt.json", {"groups": groups,
        "all_inputs_from_verified_R799_active_bundle": transferred,
        "fresh_download_only_R795_with_its_verified_R775_R786_input_bundle": not transferred,
        "input_bundle_file": INPUT_BUNDLE, "input_bundle_sha256": sha(out/INPUT_BUNDLE),
        "only_three_original_M2_anchors_and_old_power5_power6_inputs_retained": True,
        "old_arithmetic_recomputed": False})
    return inputs


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41 and tag["level"] == 82
    for name in ("R799_proof_sha256", "R799_method_sha256", "retained_artifacts", "power6_new_interval",
                 "new_basis_dimensions", "new_basis_bounds_qY", "anchor_indices", "auxiliary_prime_start",
                 "auxiliary_prime_policy", "selection_batch_size"):
        assert tag[name] == item[name]
    assert tag["power6_new_interval"] == [82, 109]
    assert tag["new_basis_dimensions"] == {"7": 1778, "8": 2050}
    assert tag["new_basis_bounds_qY"] == {"7": 95, "8": 108}
    assert tag["anchor_indices"] == [0, 1, 73]
    assert tag["power6_integer_scale"] == str(82**12)
    assert tag["new_basis_integer_scales"] == {"7": str(82**14), "8": str(82**16)}
    assert tag["real_coordinate_count"] == 20
    assert tag["old_power6_prefix_or_E1_M2_lower_power_arithmetic_recomputed"] is False


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R799-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    initial = read(bound_path(directory, entries, "public-actions-input.json"))
    assert initial["source_commit"] == spec["source_commit"]
    for name in ("result", "p", "core_sha256", "R799_proof_sha256", "R799_method_sha256", "retained_artifacts",
                 "power6_new_interval", "new_basis_dimensions", "new_basis_bounds_qY", "anchor_indices",
                 "auxiliary_prime_start", "auxiliary_prime_policy", "selection_batch_size"):
        assert initial["job"][name] == item[name], "Changed continuation input: "+name
    bundle = bound_path(directory, entries, INPUT_BUNDLE)
    extract_bundle(bundle, out.parent/"retained", item["retained_artifacts"], LABELS)
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    copied = 0
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R799-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound_path(directory, entries, name)
        data = read(source)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
        shutil.copyfile(source, out/name)
        copied += 1
    save(out/"resume-receipt.json", {"producer": spec, "same_exact_core_sha256": item["core_sha256"],
        "complete_checkpoint_files_copied": copied, "verified_minimal_three_group_input_bundle_restored": True,
        "pending_modular_batches_and_exact_candidates_preserved": True,
        "completed_mathematical_stages_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path), "artifact": artifact,
                     "included_in_git": path.name in META and path.stat().st_size < 100_000})
    path = out/"full-outputs-manifest.json"
    save(path, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_exact_basis_rows_or_certificates_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": path.name,
        "manifest_sha256": sha(path), "manifest_bytes": path.stat().st_size, "file_count": len(rows),
        "full_outputs_artifact": artifact, "manifest_in_git": path.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, proof, method = S/item["core"], topic_path(item["proof"]), topic_path(item["method"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "proof_sha256": sha(proof), "method_sha256": sha(method),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "download_helper_sha256": sha(S/"R786_public_exact_power5_short_basis.py"),
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "only V6 q82..108, V7 q0..95 and V8 q0..108 with actual complete-coordinate minors",
        "actual_original_function_polar_divisor_beta_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["producer_inputs_pending"] is False
        assert sha(core) == item["core_sha256"]
        assert sha(proof) == item["R799_proof_sha256"] and sha(method) == item["R799_method_sha256"]
        assert sha(S/"R786_public_exact_power5_short_basis.py") == item["download_helper_sha256"]
        assert sha(S/"p41_public_actions_recovery.py") == item["publication_helper_sha256"]
        assert item["power6_new_interval"] == [82, 109] and item["anchor_indices"] == [0, 1, 73]
        assert item["new_basis_dimensions"] == {"7": 1778, "8": 2050}
        assert item["new_basis_bounds_qY"] == {"7": 95, "8": 108}
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config), "--proof", str(proof),
            "--method", str(method), "--retained", str(inputs), "--output", str(out),
            "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed tails, exact candidates and modular progress retained."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
    except Exception as exception:
        error = type(exception).__name__+": "+str(exception)
    rp = out/"core-receipt.json"
    receipt = read(rp) if rp.exists() else {"complete": False}
    complete = code == 0 and receipt.get("complete") is True
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(rp) if rp.exists() else None,
        "actual_original_V6_tail_V7_V8_bases_completed": complete,
        "old_power6_prefix_or_E1_M2_lower_power_arithmetic_recomputed": False,
        "actual_original_function_polar_divisor_beta_eta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"] is True and run["process_exit_code"] == 0
    rp = out/"core-receipt.json"
    assert sha(rp) == run["core_receipt_sha256"]
    receipt = read(rp)
    assert receipt["result"] == RESULT and receipt["complete"] is True
    assert receipt["source_sha256"] == item["core_sha256"] and sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["p"] == 41
    matching_configuration(cert["configuration"], item)
    assert cert["power6_tail_dimension"] == 1506 and cert["power6_new_interval"] == [82, 109]
    assert cert["new_exact_basis_dimensions"] == {"7": 1778, "8": 2050}
    assert cert["new_exact_basis_bounds_qY"] == {"7": 95, "8": 108}
    assert cert["actual_anchor_indices"] in ([0, 1], [0, 1, 73])
    for name in ("all_original_power6_finite_tails_compared", "all_original_real_cyclotomic_transports_verified",
                 "all_new_basis_rows_match_selecting_modular_columns", "three_original_anchor_basepoint_free_input_verified"):
        assert cert[name] is True
    for name in ("old_power6_prefix_or_E1_M2_lower_power_arithmetic_recomputed",
                 "power7_coefficients_after_qY95_or_power8_after_qY108_generated",
                 "actual_original_function_polar_divisor_beta_eta_or_height_computed"):
        assert cert[name] is False
    inventory_spec = cert["stage_manifest"]
    assert Path(inventory_spec["file"]).name == inventory_spec["file"]
    path = out/inventory_spec["file"]
    assert path.stat().st_size == inventory_spec["bytes"] and sha(path) == inventory_spec["sha256"]
    inventory = read(path)
    assert inventory["complete"] is True
    matching_configuration(inventory["configuration"], item)
    entries = {row["file"]: row for row in inventory["files"]}
    assert len(entries) == len(inventory["files"])
    for name, row in entries.items():
        assert Path(name).name == name and name.startswith("R799-") and name.endswith(".json.gz")
        path = out/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
        data = read(path)
        assert data["complete"] is True
        matching_configuration(data["configuration"], item)
    tail_spec = cert["power6_tail_index"]
    assert entries[tail_spec["file"]] == tail_spec
    tails = read(out/tail_spec["file"])
    assert tails["dimension"] == 1506 and tails["ordinary_power"] == 6
    assert tails["first_exponent"] == 82 and tails["last_exponent_exclusive"] == 109
    assert tails["integer_scale"] == str(82**12) and tails["old_prefix_recomputed"] is False
    assert [row["index"] for row in tails["basis_rows"]] == list(range(1506))
    for position, row in enumerate(tails["basis_rows"]):
        assert row["file"] == "R799-original-power6-tail-row-"+str(position).zfill(4)+".json.gz"
        assert plain_spec(row) == entries[row["file"]]
        data = read(out/row["file"])
        assert data["index"] == position and data["weight"] == 12 and data["integer_scale"] == str(82**12)
        assert data["first_exponent"] == 82 and data["last_exponent_exclusive"] == 109
        assert len(data["integer_qY_xi_coefficients"]) == len(data["integer_v_t_coefficients"]) == 27
        assert all(len(v) == 40 for v in data["integer_qY_xi_coefficients"])
        assert all(len(v) == 20 for v in data["integer_v_t_coefficients"])
        assert data["original_R775_mod739_tail_verified"] is True
        assert data["all_original_phase_involutions_verified"] is True
        assert data["old_prefix_recomputed"] is False and data["old_prefix_bytes_modified"] is False
        assert data["old_factor_rows_recomputed"] is False
    for power, dimension, bound in ((7, 1778, 95), (8, 2050, 108)):
        index_spec = cert["basis_indices"][str(power)]
        assert entries[index_spec["file"]] == index_spec
        index = read(out/index_spec["file"])
        assert index["ordinary_power"] == power and index["dimension"] == dimension and index["bound_qY"] == bound
        assert index["integer_scale"] == str(82**(2*power)) and index["full_original_real_coordinates"] == 20
        assert index["anchor_indices"] == cert["actual_anchor_indices"]
        assert index["all_exact_rows_compared_with_selecting_modular_columns"] is True
        assert index["characteristic_zero_basis_certified"] is True
        assert [row["index"] for row in index["basis_rows"]] == list(range(dimension))
        assert len({row["file"] for row in index["basis_rows"]}) == dimension
        positions = [row["candidate_position"] for row in index["basis_rows"]]
        assert positions == sorted(set(positions))
        minor = index["actual_nonzero_minor"]
        assert minor == cert["actual_new_nonzero_minors"][str(power)]
        assert minor["rows"] == minor["columns"] == dimension
        assert minor["determinant_mod_prime"] % minor["prime"]
        assert len(set(minor["coordinate_row_indices"])) == dimension
        assert all(0 <= i < 20*(bound+1) for i in minor["coordinate_row_indices"])
        assert minor["selected_basis_column_indices"] == list(range(dimension))
        assert minor["all_entries_from_saved_exact_integer_rows"] is True
        for row in index["basis_rows"]:
            assert plain_spec(row) == entries[row["file"]]
            assert row["all_current_prime_coordinates_verified"] is True
            data = read(out/row["file"])
            assert data["ordinary_power"] == power and data["weight"] == 2*power and data["bound_qY"] == bound
            assert data["recipe"] == row["recipe"] and data["integer_scale"] == str(82**(2*power))
            assert len(data["integer_qY_xi_coefficients"]) == len(data["integer_v_t_coefficients"]) == bound+1
            assert all(len(v) == 40 for v in data["integer_qY_xi_coefficients"])
            assert all(len(v) == 20 for v in data["integer_v_t_coefficients"])
            assert data["packing_stride"] == (79 if power == 7 else 121)
            assert data["all_initial_modular_coordinates_verified"] is True
            assert data["all_original_phase_involutions_verified"] is True
            assert data["old_input_arithmetic_recomputed"] is False
            assert data["unrequested_high_coefficients_generated"] is False
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
    mode = parser.parse_args().mode
    out = Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"
    if mode == "compute":
        request = read(REQUEST)
        assert request["session"] == "serre-public-astra-20261115"
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    return publish_small(item, out) if mode == "publish" else verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
