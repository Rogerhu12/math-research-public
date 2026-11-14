#!/usr/bin/env python3
"""R774: public runner for the unchanged original Hodge cube."""
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
REQUEST = TOPIC/"notes/R774-public-original-Hodge-cube-request.json"
RESULT = "R774-original-p41-Hodge-cube"
FINAL = "p41-original-Hodge-cube-certificate.json"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json",
         "public-actions-run.log", FINAL}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual arithmetic belongs to the public repository Actions.")


def root_dir():
    return Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def download(spec, directory):
    directory.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", spec["run_id"], "--repo",
                    "Rogerhu12/math-research-public", "--name", spec["artifact_name"],
                    "--dir", str(directory)], check=True)


def find_hash(directory, name, digest):
    matches = [p for p in directory.rglob(name) if p.is_file() and sha(p) == digest]
    if not matches:
        raise ValueError("Retained file/SHA not found: "+name)
    return matches[0]


def prepare_inputs(item, out):
    inputs = out.parent/"inputs"
    inputs.mkdir(parents=True, exist_ok=True)
    records = []
    for label, group in item["retained_artifacts"].items():
        directory = out.parent/("downloaded-"+label)
        download(group, directory)
        if "manifest_repository_path" in group:
            # R745/R748 wrote this small manifest only during publication,
            # after artifact upload.  Read its actual pinned Git copy.
            manifest_path = topic_path(group["manifest_repository_path"])
            assert sha(manifest_path) == group["manifest_sha256"]
            manifest_location = "published-repository-file"
        else:
            manifest_path = find_hash(directory, "full-outputs-manifest.json", group["manifest_sha256"])
            manifest_location = "producer-artifact"
        manifest = read(manifest_path)
        assert manifest["result"] == group["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        run_path = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
        run = read(run_path)
        assert run["complete"] and run["source_commit"] == group["source_commit"]
        assert run["workflow_run_id"] == group["run_id"]
        copied = []
        for name, digest in group["files"].items():
            assert Path(name).name == name and entries[name]["sha256"] == digest
            source = find_hash(directory, name, digest)
            target = inputs/name
            if target.exists():
                assert sha(target) == digest
            else:
                shutil.copyfile(source, target)
            copied.append({"file": name, "sha256": digest})
        records.append({"label": label, "run_id": group["run_id"],
            "source_commit": group["source_commit"], "artifact_name": group["artifact_name"],
            "manifest_sha256": group["manifest_sha256"], "manifest_location": manifest_location, "files": copied,
            "producer_complete": True})
    local_records = []
    for spec in item["retained_repository_files"]:
        source = topic_path(spec["path"])
        assert sha(source) == spec["sha256"]
        target = inputs/spec["file"]
        assert Path(spec["file"]).name == spec["file"]
        if target.exists():
            assert sha(target) == spec["sha256"]
        else:
            shutil.copyfile(source, target)
        local_records.append(spec)
    save(out/"retained-inputs-receipt.json", {
        "artifact_groups": records, "repository_files": local_records,
        "old_newform_finite_fibers_model_periods_lattice_or_RR_bases_recomputed": False})
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R774-continuation"
    download(spec, directory)
    manifest_path = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(manifest_path)
    assert manifest["result"] == RESULT
    copied = []
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R774-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        assert Path(name).name == name
        source = find_hash(directory, name, row["sha256"])
        value = read(source)
        tag = value["configuration"]
        assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
        assert tag["R772_proof_sha256"] == item["proof_sha256"]
        assert tag["R771_basis_certificate_sha256"] == item["basis_certificate_sha256"]
        assert tag["R771_basis_state_sha256"] == item["basis_state_sha256"]
        target = out/name
        if target.exists():
            assert sha(target) == row["sha256"]
        else:
            shutil.copyfile(source, target)
        copied.append({"file": name, "sha256": row["sha256"],
                       "complete": value.get("complete", False)})
    assert copied, "No compatible exact R774 continuation state found"
    save(out/"resume-receipt.json", {"run_id": spec["run_id"],
        "artifact_name": spec["artifact_name"], "manifest_sha256": spec["manifest_sha256"],
        "same_exact_core_sha256": item["core_sha256"], "files": copied})


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
    save(out/"full-outputs-manifest.json", {"result": RESULT, "files": rows,
        "full_outputs_artifact": artifact,
        "reproducible_Fourier_and_exact_cube_tables_in_git": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method, proof = S/item["core"], topic_path(item["method"]), topic_path(item["proof"])
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_repository": "Rogerhu12/math-research-public",
        "source_commit": source, "job": item,
        "core_sha256": sha(core), "method_sha256": sha(method), "proof_sha256": sha(proof),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "publication_helper_sha256": sha(S/"p41_public_actions_recovery.py"),
        "workflow_sha256": sha(REPO/item["workflow"]),
        "retained_artifacts": item["retained_artifacts"], "resume": item.get("resume"),
        "budget_minutes": item["budget_minutes"],
        "arithmetic": "exact integer low products, fixed original L scalars, and actual M6 finite comparison",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mathematical_completion_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        assert not item.get("producer_inputs_pending", True)
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        assert sha(proof) == item["proof_sha256"]
        assert item["Q_bound"] == 2460 and item["qY_bound"] == 820
        inputs = prepare_inputs(item, out)
        restore_resume(item, out)
        command = [sys.executable, "-u", str(core), "--inputs", str(inputs),
                   "--output", str(out), "--proof", str(proof),
                   "--basis-core-sha256", item["basis_core_sha256"],
                   "--basis-certificate-sha256", item["basis_certificate_sha256"],
                   "--basis-state-sha256", item["basis_state_sha256"]]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60)
            except subprocess.TimeoutExpired:
                error = "Budget reached; all completed exact products and partial rows retained."
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
        "exact_original_Hodge_cube_prefix_claimed": complete,
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
    assert tag["R772_proof_sha256"] == item["proof_sha256"]
    assert tag["R771_core_sha256"] == item["basis_core_sha256"]
    assert tag["R771_basis_certificate_sha256"] == item["basis_certificate_sha256"]
    assert tag["R771_basis_state_sha256"] == item["basis_state_sha256"]
    assert cert["selected_original_map_index"] == 4 and cert["selected_original_map_degree"] == "1206"
    assert cert["original_c1_coset"] == 4424
    assert cert["original_newform_prefix_reused_through"] == 4096
    assert not cert["newform_coefficients_recomputed"] and not cert["old_Fourier_rows_through_800_recomputed"]
    assert cert["original_six_Fourier_rows_generated_through_Q"] == 2460
    e = cert["actual_cusp_ramification_e"]
    assert 1 <= e <= 19 and e % 3 == 1
    assert cert["exact_H_cubed_generated_through_qY"] == cert["M6_line_bundle_degree"] == 820
    assert cert["qY_constant_coefficient_zero"] and cert["exact_H_cubed_nonzero"]
    assert cert["exact_rows_stored_with_primitive_integers_and_rational_row_scales"]
    assert cert["full_prefix_uniquely_identifies_original_H3"]
    assert cert["mod739_cleared_H3_coordinates_in_actual_M6_basis_verified"]
    assert cert["all_821_coefficients_verified_for_all_seven_b_coordinates"]
    assert not cert["characteristic_zero_M6_basis_coordinates_computed"]
    assert not cert["actual_y_map_beta_or_height_computed"]
    assert not cert["old_model_topology_periods_or_lattice_recomputed"]
    assert cert["no_Neron_Manin_or_KS_scale_changed"]
    for row in cert["stages"]:
        assert Path(row["file"]).name == row["file"] and sha(out/row["file"]) == row["sha256"]
    scalar_path = out/"R774-original-L-cubic-scalars.json.gz"
    scalar = read(scalar_path)
    assert scalar["complete"] and scalar["configuration"] == tag
    assert len(scalar["rational_row_scales"]) == 14
    assert len(scalar["primitive_integer_matrix"]) == 14
    assert all(len(row) == 112 for row in scalar["primitive_integer_matrix"])
    assert scalar["common_denominator_739_valuation"] == cert["common_denominator_739_valuation"]
    order = read(out/"R774-actual-cusp-order-and-leading-coefficient.json.gz")
    assert order["complete"] and order["configuration"] == tag
    assert order["actual_cusp_ramification_e"] == e
    cursor = 1
    for row in cert["H3_blocks"]:
        assert sha(out/row["file"]) == row["sha256"]
        block = read(out/row["file"])
        assert block["complete"] and block["configuration"] == tag
        assert block["first_exponent"] == cursor
        assert block["rational_row_scale_stage_sha256"] == sha(scalar_path)
        length = block["last_exponent_exclusive"]-cursor
        assert len(block["integer_numerators"]) == 14
        assert all(len(values) == 40*length for values in block["integer_numerators"])
        cursor = block["last_exponent_exclusive"]
    assert cursor == 821
    finite = read(out/"R774-cleared-H3-in-the-actual-M6-basis-mod739.json.gz")
    assert finite["complete"] and finite["configuration"] == tag
    assert finite["all_821_coefficients_verified_for_all_seven_b_coordinates"]
    assert not finite["characteristic_zero_M6_coordinates_inferred_from_reduction"]
    assert finite["common_denominator_739_valuation"] == cert["common_denominator_739_valuation"]
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
        return compute(request["job"], out)
    item = read(out/"public-actions-input.json")["job"]
    assert item["result"] == RESULT
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
