#!/usr/bin/env python3
"""R797 runner: reuse the actual shared Hodge triples and selected Hom inputs."""
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
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R797-public-five-original-Laurent-prefixes-request.json"
RESULT = "R797-five-original-low-degree-Laurent-prefixes"
FINAL = "p41-five-original-low-degree-Laurent-prefixes-certificate.json"
INPUT_BUNDLE = "R797-retained-producer-inputs.tar.gz"
REFERENCE = "full-outputs-manifest-reference.json"
LABELS = {"R774", "R794"}
PRODUCER_META = ("full-outputs-manifest.json", "run-receipt.json",
                 "core-receipt.json", "public-actions-input.json")
META = {"public-actions-input.json", "retained-inputs-receipt.json",
        "resume-receipt.json", "run-receipt.json", "core-receipt.json"}
MODEL_WITNESS = "R774-original-L-cubic-scalars.json.gz"
SELECTED = "R794-selected-original-low-degree-eta-basis.json.gz"
STATE_KEYS = {"R", "W", "R2", "W2", "U", "U2", "Atilde", "kappa_power"}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def bound_path(directory, entries, name):
    assert Path(name).name == name
    row = entries[name]
    path = find_hash(directory, name, row["sha256"])
    assert path.stat().st_size == row["bytes"]
    return path


def producer_metadata(directory, label, spec):
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == spec["result"]
    entries = {row["file"]: row for row in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    paths = {"full-outputs-manifest.json": mp}
    for name in PRODUCER_META[1:]:
        paths[name] = bound_path(directory, entries, name)
    run, core, initial = (read(paths[name]) for name in PRODUCER_META[1:])
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert str(run["workflow_run_id"]) == str(spec["run_id"])
    assert run["source_commit"] == initial["source_commit"] == spec["source_commit"]
    assert core["complete"] is True and core["source_sha256"] == spec["core_sha256"]
    assert initial["result"] == core["result"] == spec["result"]
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["job"]["core_sha256"] == spec["core_sha256"]
    if label == "R774":
        assert run["result"] == spec["result"]
        assert run["core_receipt_sha256"] == sha(paths["core-receipt.json"])
        assert initial["core_sha256"] == spec["core_sha256"]
    else:
        assert label == "R794"
        assert "core_receipt_sha256" not in run and "core_sha256" not in initial
    name = spec["certificate_name"]
    assert entries[name]["sha256"] == spec["files"][name] == core["certificate_sha256"]
    paths[name] = bound_path(directory, entries, name)
    cert = read(paths[name])
    assert cert["complete"] is True and cert["result"] == spec["result"]
    assert cert["configuration"]["source_sha256"] == spec["core_sha256"]
    assert cert["configuration"]["python_flint"] == "0.9.0"
    return entries, paths, cert


def selected_group_files(directory, label, spec):
    entries, paths, cert = producer_metadata(directory, label, spec)
    selected = dict(spec["files"])
    stages = {row["file"]: row for row in cert["stages"]}
    if label == "R774":
        assert cert["original_six_Fourier_rows_generated_through_Q"] == 2460
        assert cert["no_Neron_Manin_or_KS_scale_changed"] is True
        assert MODEL_WITNESS in selected
        for index in range(56):
            name = "R774-cubic-monomial-"+str(index).zfill(2)+".json.gz"
            selected[name] = stages[name]["sha256"]
    else:
        assert label == "R794" and SELECTED in selected
        assert cert["selected_candidate_indices"] == [0, 3, 1, 21, 15]
        assert cert["selected_map_degrees"] == ["1485", "1521", "1602", "1674", "1728"]
        assert cert["selected_basis_rank"] == 5 and cert["all_original_F0_directions_preserved"] is True
    for name, digest in selected.items():
        assert entries[name]["sha256"] == digest
        path = bound_path(directory, entries, name)
        if name != spec["certificate_name"]:
            data = read(path)
            assert data["complete"] is True and data["configuration"] == cert["configuration"]
            assert stages[name]["sha256"] == digest and stages[name]["bytes"] == entries[name]["bytes"]
            if name.startswith("R774-cubic-monomial-"):
                assert data["G_exponent_range_exclusive"] == [0, 820]
                assert data["xi_basis_degree"] == 40 and data["complete_low_product_computed"] is True
                assert len(data["real_coefficients_flat_qY_xi"]) == len(data["s_coefficients_flat_qY_xi"]) == 32800
            if name == SELECTED:
                assert data["selected_candidate_indices"] == [0, 3, 1, 21, 15]
                assert data["original_kappa_e_R_q_c0_c1_preserved"] is True
                assert len(data["selected_maps"]) == 5
                assert all(len(row["original_omega_differential_coordinates"]) == 6 for row in data["selected_maps"])
        paths[name] = path
    return paths


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
    assert set(item["retained_artifacts"]) == LABELS
    inputs = out.parent/"retained"
    present = [(inputs/label/"full-outputs-manifest.json").exists() for label in LABELS]
    transferred = all(present)
    assert transferred or not any(present), "Partial unverified input bundle"
    groups = []
    for label in ("R774", "R794"):
        spec, target = item["retained_artifacts"][label], inputs/label
        if not transferred:
            directory = out.parent/("downloaded-"+label)
            download(spec, directory, require_complete=True)
            transfer(selected_group_files(directory, label, spec), target)
        paths = selected_group_files(target, label, spec)
        assert set(path.name for path in target.iterdir() if path.is_file()) == set(paths)
        groups.append({"label": label, "producer": spec, "file_count": len(paths),
            "all_sizes_sha256_and_original_schemas_verified": True})
    save(out/"retained-inputs-receipt.json", {"groups": groups,
        "all_inputs_from_verified_R797_active_bundle": transferred,
        "only_shared_triples_original_model_witness_and_new_selected_differentials_retained": True,
        "old_f4_H3_blocks_or_Laurent_coefficients_retained": False,
        "old_arithmetic_recomputed": False})
    if not (out/INPUT_BUNDLE).exists():
        with tarfile.open(out/INPUT_BUNDLE, "w:gz") as archive:
            for path in sorted(inputs.rglob("*")):
                if path.is_file():
                    archive.add(path, arcname=str(path.relative_to(inputs)), recursive=False)
    return inputs


def matching_configuration(tag, item):
    assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
    assert tag["python_flint"] == "0.9.0" and tag["p"] == 41
    for key in ("R797_method_sha256", "R793_proof_sha256", "R781_proof_sha256",
                "R781_core_sha256", "retained_artifacts", "maps"):
        assert tag[key] == item[key]
    assert tag["field"]["dimension_over_Q"] == 280
    assert tag["old_f4_or_shared_Hodge_products_recomputed"] is False
    assert tag["second_c1_phase_or_real_descent_isogeny_applied"] is False


def allowed_group_names(label, spec):
    names = set(PRODUCER_META)|set(spec["files"])
    if label == "R774":
        names |= {"R774-cubic-monomial-"+str(index).zfill(2)+".json.gz" for index in range(56)}
    return names


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R797-continuation"
    download(spec, directory, require_complete=False)
    mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(mp)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    initial = read(bound_path(directory, entries, "public-actions-input.json"))
    assert initial["source_commit"] == spec["source_commit"]
    for name in ("result", "core_sha256", "R797_method_sha256", "R793_proof_sha256", "R781_proof_sha256",
                 "R781_core_sha256", "maps", "retained_artifacts"):
        assert initial["job"][name] == item[name], "Changed continuation input: "+name
    bundle = bound_path(directory, entries, INPUT_BUNDLE)
    target = out.parent/"retained"
    target.mkdir(parents=True, exist_ok=True)
    with tarfile.open(bundle, "r:gz") as archive:
        for member in archive:
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and ".." not in relative.parts
            assert len(relative.parts) == 2 and relative.parts[0] in LABELS
            group, name = relative.parts
            assert name in allowed_group_names(group, item["retained_artifacts"][group])
            path = target/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            data = archive.extractfile(member).read()
            if path.exists():
                assert path.read_bytes() == data
            else:
                path.write_bytes(data)
    shutil.copyfile(bundle, out/INPUT_BUNDLE)
    copied = 0
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R797-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        source = bound_path(directory, entries, name)
        data = read(source)
        matching_configuration(data["configuration"], item)
        assert data["complete"] is True
        shutil.copyfile(source, out/name)
        copied += 1
    save(out/"resume-receipt.json", {"producer": spec,
        "same_exact_core_sha256": item["core_sha256"], "complete_checkpoint_files_copied": copied,
        "verified_minimal_two_group_input_bundle_restored": True,
        "completed_mathematical_maps_or_orders_recomputed": False})


def output_manifest(out):
    artifact = "serre-global-"+RESULT+"-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in ("full-outputs-manifest.json", REFERENCE):
            continue
        rows.append({"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path),
                     "artifact": artifact,
                     "included_in_git": path.name in META and path.stat().st_size < 100_000})
    path = out/"full-outputs-manifest.json"
    save(path, {"result": RESULT, "files": rows, "temporary_active_checkpoint_artifact": artifact,
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_Laurent_coefficients_or_certificates_in_git_or_release": False})
    save(out/REFERENCE, {"result": RESULT, "manifest_file": path.name,
        "manifest_sha256": sha(path), "manifest_bytes": path.stat().st_size,
        "file_count": len(rows), "full_outputs_artifact": artifact,
        "manifest_in_git": path.stat().st_size < 100_000})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, helper = S/item["core"], S/item["laurent_core"]
    method, cusp, recurrence = topic_path(item["method"]), topic_path(item["cusp_proof"]), topic_path(item["recurrence_proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "job": item, "core_sha256": sha(core), "method_sha256": sha(method),
        "cusp_proof_sha256": sha(cusp), "recurrence_proof_sha256": sha(recurrence),
        "R781_core_sha256": sha(helper), "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "download_helper_sha256": sha(S/"R786_public_exact_power5_short_basis.py"),
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "new_arithmetic": "five selected original Hodge scalar contractions and required inverse-free Laurent orders only",
        "actual_rational_map_polar_divisor_eta_or_height_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"] and sha(method) == item["R797_method_sha256"]
        assert sha(helper) == item["R781_core_sha256"]
        assert sha(cusp) == item["R793_proof_sha256"] and sha(recurrence) == item["R781_proof_sha256"]
        restore_resume(item, out)
        inputs = prepare_inputs(item, out)
        config = out.parent/"job-config.json"
        save(config, item)
        command = [sys.executable, "-u", str(core), "--config", str(config), "--method", str(method),
            "--cusp-proof", str(cusp), "--recurrence-proof", str(recurrence), "--laurent-core", str(helper),
            "--retained", str(inputs), "--output", str(out), "--budget-minutes", str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60+120)
            except subprocess.TimeoutExpired:
                error = "Budget reached; completed map/order stages and shared original inputs retained."
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
        "actual_five_original_required_Laurent_prefixes_completed": complete,
        "old_f4_or_shared_Hodge_products_recomputed": False,
        "actual_rational_map_polar_divisor_eta_or_height_computed": False,
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
    assert receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["result"] == RESULT and cert["complete"] is True and cert["p"] == 41
    matching_configuration(cert["configuration"], item)
    assert cert["completed_map_count"] == 5 and cert["coefficient_field_dimension_over_Q"] == 280
    assert cert["selected_candidate_indices"] == [row["candidate_index"] for row in item["maps"]] == [0, 3, 1, 21, 15]
    assert cert["selected_map_degrees"] == [row["map_degree"] for row in item["maps"]]
    for field, parameter in (("complete_Laurent_condition_counts", "complete_Laurent_conditions"),
                             ("normalized_R_bounds", "normalized_R_bound"), ("H3_bounds", "H3_bound")):
        assert cert[field] == [row[parameter] for row in item["maps"]]
    for name in ("all_actual_original_kappas_nonzero", "all_actual_cusp_orders_one",
                 "all_original_real_tangent_phases_verified", "all_recurrence_coefficients_verified_exactly"):
        assert cert[name] is True
    for name in ("old_f4_H3_or_Laurent_recomputed", "old_newform_Fourier_Hodge_products_periods_or_Hom_recomputed",
                 "coefficients_after_individual_required_bounds_generated", "algebraic_kappa_inverse_computed",
                 "second_c1_phase_or_real_descent_isogeny_applied",
                 "actual_relation_matrix_rational_map_polar_divisor_eta_or_height_computed"):
        assert cert[name] is False
    spec = cert["stage_manifest"]
    assert Path(spec["file"]).name == spec["file"]
    path = out/spec["file"]
    assert path.stat().st_size == spec["bytes"] and sha(path) == spec["sha256"]
    manifest = read(path)
    matching_configuration(manifest["configuration"], item)
    assert manifest["complete"] is True
    nested = {row["file"]: row for row in manifest["files"]}
    assert len(nested) == len(manifest["files"]) == sum(row["complete_Laurent_conditions"]+3 for row in item["maps"])
    for name, row in nested.items():
        assert Path(name).name == name
        path = out/name
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
    assert len(cert["map_prefix_certificates"]) == 5
    for parameters, map_spec in zip(item["maps"], cert["map_prefix_certificates"]):
        candidate, count = parameters["candidate_index"], parameters["complete_Laurent_conditions"]
        prefix = "R797-map-"+str(candidate).zfill(3)
        assert map_spec["file"] == prefix+"-complete-prefix.json.gz"
        assert nested[map_spec["file"]] == map_spec
        summary = read(out/map_spec["file"])
        matching_configuration(summary["configuration"], item)
        assert summary["complete"] is True and summary["candidate_index"] == candidate
        assert summary["map_degree"] == parameters["map_degree"] and summary["ordinary_power"] == parameters["ordinary_power"]
        assert summary["complete_Laurent_conditions"] == summary["H3_bound"] == count
        assert summary["normalized_R_bound"] == count-1 and summary["Laurent_exponents"] == [-1, count-2]
        assert summary["actual_cusp_ramification_e"] == 1 and summary["actual_kappa_nonzero"] is True
        assert summary["all_original_real_tangent_phases_verified"] is True
        assert summary["all_recurrence_coefficients_verified_exactly"] is True
        assert summary["actual_relation_matrix_rational_map_polar_divisor_eta_or_height_computed"] is False
        assert len(summary["stages"]) == count+2
        for row in summary["stages"]:
            assert nested[row["file"]] == row
        scalars_name, input_name = prefix+"-new-L-cubic-scalars.json.gz", prefix+"-original-real-H3-input.json.gz"
        scalars, inputs = read(out/scalars_name), read(out/input_name)
        for value in (scalars, inputs):
            matching_configuration(value["configuration"], item)
            assert value["complete"] is True and value["candidate_index"] == candidate
        assert scalars["old_f4_scalar_matrix_consumed"] is False and scalars["old_shared_triples_recomputed"] is False
        assert len(scalars["new_original_L_scalars"]) == 56
        assert len(scalars["primitive_integer_matrix"]) == len(scalars["rational_row_scales"]) == 14
        assert all(len(row) == 112 for row in scalars["primitive_integer_matrix"])
        assert inputs["new_scalar_stage_sha256"] == nested[scalars_name]["sha256"]
        assert inputs["H3_bound"] == count and len(inputs["H3_coefficients_v"]) == count+1
        assert inputs["actual_kappa_nonzero"] is True and inputs["actual_cusp_ramification_e"] == 1
        assert inputs["all_14_coordinate_involutions_verified_at_each_exponent"] is True
        assert inputs["involution_checks"] == 14*count
        assert inputs["qY_shift_applied_exactly_once"] is True
        prior_sha = None
        for n in range(count):
            name = prefix+"-inverse-free-Laurent-"+str(n).zfill(3)+".json.gz"
            state = read(out/name)
            matching_configuration(state["configuration"], item)
            assert state["complete"] is True and state["candidate_index"] == candidate and state["order"] == n
            assert state["exact_differential_identity_at_this_order"] is True
            assert set(state["coefficients"]) == STATE_KEYS
            assert all(len(value["primitive_integer_vector"]) == 280 for value in state["coefficients"].values())
            if n == 0:
                assert state["input_stage_sha256"] == nested[input_name]["sha256"]
                assert state["normalized_constant_R0_one"] is True
            else:
                assert state["previous_stage_sha256"] == prior_sha and state["recurrence_divisor"] == 3*n+1
                assert state["ordinary_nonzero_integer_division_only"] is True
                assert state["kappa_algebraic_inverse_computed"] is False
            prior_sha = nested[name]["sha256"]
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
