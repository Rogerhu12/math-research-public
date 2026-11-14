#!/usr/bin/env python3
"""R771: public execution and retained recipe/minor publication."""
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
REQUEST = TOPIC/"notes/R771-public-quotient-RR-bases-request.json"
RESULT = "R771-p41-original-quotient-RR-bases"
FINAL = "p41-original-quotient-RR-basis-certificate.json"
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
    paths, rows = {}, []
    for label in ("R745", "R759"):
        spec = item["retained"][label]
        source = safe_topic_path(spec["path"])
        assert source.is_file() and sha(source) == spec["sha256"]
        data = read(source)
        assert data["complete"]
        assert data["result"] == {
            "R745": "R745-p41-original-Hodge-input",
            "R759": "R759-original-integral-period-lattice-and-map-degrees",
        }[label]
        paths[label] = source
        rows.append({"label": label, "path": spec["path"],
                     "sha256": spec["sha256"], "run_id": spec["run_id"],
                     "source_commit": spec["source_commit"],
                     "existing_small_certificate_read_verbatim": True})
    save(out/"retained-inputs-receipt.json", {
        "inputs": rows, "old_mathematics_recomputed": False,
        "large_old_artifact_downloaded": False})
    return paths


def find_hash(directory, name, digest):
    matches = [p for p in directory.rglob(name) if p.is_file() and sha(p) == digest]
    if not matches:
        raise ValueError("Required retained file/SHA was not found: "+name)
    return matches[0]


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R771-continuation"
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
        if not (name.startswith("R771-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        assert Path(name).name == name
        source = find_hash(directory, name, row["sha256"])
        data = read(source)
        tag = data["configuration"]
        assert tag["result"] == RESULT and tag["source_sha256"] == item["core_sha256"]
        assert tag["R767_proof_sha256"] == item["proof_sha256"]
        assert tag["R745_hodge_certificate_sha256"] == item["retained"]["R745"]["sha256"]
        assert tag["R759_degree_certificate_sha256"] == item["retained"]["R759"]["sha256"]
        target = out/name
        if target.exists():
            assert sha(target) == row["sha256"]
        else:
            shutil.copyfile(source, target)
        copied.append({"file": name, "sha256": row["sha256"],
                       "complete": data.get("complete", False)})
    assert copied, "No compatible retained R771 stages were supplied"
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
        "arithmetic": "exact F_739 coefficients and certified characteristic-zero recipes",
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
                   "--hodge-certificate", str(paths["R745"]),
                   "--degree-certificate", str(paths["R759"]), "--proof", str(proof)]
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
    assert tag["R767_proof_sha256"] == item["proof_sha256"]
    assert tag["R745_hodge_certificate_sha256"] == item["retained"]["R745"]["sha256"]
    assert tag["R759_degree_certificate_sha256"] == item["retained"]["R759"]["sha256"]
    assert tag["prime"] == cert["prime"] == 739 and tag["max_exponent_qY"] == 1640
    assert tag["python_flint"] == "0.9.0"
    assert cert["source_quotient_genus"] == 127 and cert["level"] == 82
    assert cert["H82_order"] == 252 and cert["effective_trace_order"] == 126
    assert cert["M2_dimension"] == 146 and cert["M6_dimension"] == 694 and cert["M12_dimension"] == 1514
    assert cert["power_basis_dimensions"] == {
        "1": 146, "2": 418, "3": 690, "4": 962, "5": 1234, "6": 1506}
    assert len(cert["M2_exact_seeds"]) == 146
    for name, dimension, bound in (("M2", 146, 273), ("M6", 694, 820), ("M12", 1514, 1640)):
        verify_minor(cert[name+"_actual_minor"], dimension, bound)
    assert cert["selected_actual_map_index"] == 4 and cert["selected_actual_map_degree"] == "1206"
    assert cert["cusp_ramification_bound_from_unchanged_R745"] == 19
    assert cert["required_exact_RR_basis_series_through_qY"] == 2846
    assert cert["required_original_h_over_dQ_series_through_Q"] == 8557
    assert cert["actual_characteristic_zero_RR_basis_recipes_certified"]
    assert not cert["characteristic_zero_basis_coefficients_reconstructed_numerically"]
    assert not cert["full_required_characteristic_zero_q_series_computed"]
    assert not cert["actual_y_map_beta_or_height_computed"]
    assert not cert["old_topology_periods_Hom_lattice_or_degrees_recomputed"]
    assert cert["M6_694_minus_degree_not_asserted_without_nonspeciality"]
    for row in cert["stages"]:
        assert Path(row["file"]).name == row["file"]
        assert sha(out/row["file"]) == row["sha256"]
    for name, dimension in (("M2", 146), ("M6-complete", 694), ("M12-complete", 1514)):
        stage = read(out/("R771-basis-"+name+".json.gz"))
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
