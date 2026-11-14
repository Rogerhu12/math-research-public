#!/usr/bin/env python3
"""Public wrapper: the complete original integral-period lattice and map degrees."""
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
REQUEST = TOPIC/"notes/R759-public-integral-period-lattice-request.json"
RESULT = "R759-original-integral-period-lattice-and-map-degrees"
FINAL = "p41-original-integral-period-lattice-and-degree-certificate.json"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json",
         "public-actions-run.log", FINAL}


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual arithmetic runs only in the public repository Actions.")


def root_dir():
    return Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT


def download(group, directory):
    directory.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", group["run_id"],
                    "--repo", "Rogerhu12/math-research-public",
                    "--name", group["artifact_name"], "--dir", str(directory)], check=True)


def find_hash(directory, name, digest):
    matches = [p for p in directory.rglob(name) if p.is_file() and sha(p) == digest]
    if not matches:
        raise ValueError("No retained artifact file has the required SHA: "+name)
    return matches[0]


def prepare_inputs(item, out):
    inputs = out.parent/"inputs"
    inputs.mkdir(parents=True, exist_ok=True)
    records = []
    for label, group in item["retained"].items():
        assert group is not None, "The successful R754 artifact has not yet been supplied"
        directory = out.parent/("downloaded-"+label)
        download(group, directory)
        producer_receipt = None
        if label == "R754":
            manifest_path = find_hash(directory, "full-outputs-manifest.json", group["manifest_sha256"])
            manifest = read(manifest_path)
            assert manifest["result"] == "R754-original-p41-periods-and-Hom-kernel"
            entries = {row["file"]: row for row in manifest["files"]}
            for name, digest in group["files"].items():
                assert entries[name]["sha256"] == digest
            receipt_path = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
            producer_receipt = read(receipt_path)
            assert producer_receipt["complete"]
            assert producer_receipt["source_commit"] == group["source_commit"]
            assert producer_receipt["workflow_run_id"] == group["run_id"]
        copied = []
        for name, digest in group["files"].items():
            assert Path(name).name == name
            source = find_hash(directory, name, digest)
            target = inputs/name
            if target.exists():
                assert sha(target) == digest
            else:
                shutil.copyfile(source, target)
            copied.append({"file": name, "sha256": digest})
        records.append({"label": label, "run_id": group["run_id"],
                        "source_commit": group["source_commit"],
                        "artifact_name": group["artifact_name"], "files": copied,
                        "producer_manifest_sha256": group.get("manifest_sha256"),
                        "producer_completed": None if producer_receipt is None else True})
    save(out/"retained-inputs-receipt.json", {
        "groups": records, "old_model_topology_periods_or_Hom_kernel_recomputed": False})
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R759-continuation"
    download(spec, directory)
    manifest_path = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(manifest_path)
    assert manifest["result"] == RESULT
    copied = []
    for row in manifest["files"]:
        name = row["file"]
        if not (name.startswith("R759-") and name.endswith(".json.gz")) and name != FINAL:
            continue
        assert Path(name).name == name
        source = find_hash(directory, name, row["sha256"])
        obj = read(source)
        assert obj["configuration"]["source_sha256"] == item["core_sha256"]
        assert obj["configuration"]["result"] == RESULT
        target = out/name
        if target.exists():
            assert sha(target) == row["sha256"]
        else:
            shutil.copyfile(source, target)
        copied.append({"file": name, "sha256": row["sha256"],
                       "complete": obj.get("complete", False)})
    assert copied, "A continuation artifact contained no compatible exact checkpoints"
    save(out/"resume-receipt.json", {"run_id": spec["run_id"],
         "artifact_name": spec["artifact_name"], "manifest_sha256": spec["manifest_sha256"],
         "same_exact_source_sha256": item["core_sha256"], "copied": copied})


def output_manifest(out):
    suffix = os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    artifact = "serre-global-"+RESULT+"-"+suffix
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name == "full-outputs-manifest.json":
            continue
        include = path.name in SMALL and path.stat().st_size < 100_000
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path), "included_in_git": include, "artifact": artifact})
    save(out/"full-outputs-manifest.json", {"result": RESULT, "files": rows,
         "full_outputs_artifact": artifact,
         "reproducible_intermediate_coordinates_in_git": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method = S/item["core"], TOPIC/item["method"]
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "p": 41,
        "source_commit": source, "source_repository": "Rogerhu12/math-research-public",
        "core_sha256": sha(core), "method_sha256": sha(method),
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"),
        "topic_readme_sha256": sha(TOPIC/"README.md"),
        "dependencies": [{"file": f, "sha256": sha(TOPIC/f)} for f in item["dependencies"]],
        "retained": item["retained"], "resume": item.get("resume"),
        "budget_minutes": item["budget_minutes"], "arithmetic": "exact integer lattices and rational Gram arithmetic",
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mathematical_completion_claimed": False})
    code, error = 1, None
    try:
        assert item["p"] == 41 and item["result"] == RESULT
        assert not item.get("producer_inputs_pending", True), "Await the actual successful R754 outputs"
        assert sha(core) == item["core_sha256"]
        assert sha(method) == item["method_sha256"]
        inputs = prepare_inputs(item, out)
        restore_resume(item, out)
        command = [sys.executable, "-u", str(core), "--output", str(out), "--inputs", str(inputs),
                   "--r754-core-sha256", item["r754_core_sha256"]]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60)
            except subprocess.TimeoutExpired:
                error = "Budget checkpoint reached; all exact completed and partial stages retained."
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
    save(out/"run-receipt.json", {"result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(receipt_path) if receipt_path.exists() else None,
        "complete_integral_period_lattice_and_degrees_claimed": complete,
        "actual_q_functions_beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"]
    receipt = read(out/"core-receipt.json")
    assert sha(out/"core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["complete"] and receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["complete"] and cert["p"] == 41
    assert cert["configuration"]["source_sha256"] == item["core_sha256"]
    assert cert["configuration"]["R754_core_sha256"] == item["r754_core_sha256"]
    assert cert["source_genus"] == 400 and cert["unchanged_original_closed_chains"] == 800
    assert cert["full_integral_period_lattice_Z_rank"] == 12 and cert["O_K_rank"] == 6
    for field in ("all_1600_rational_period_rows_used", "HNF_unimodular_steps_verified",
                  "zeta_stability_verified", "original_intersection_solve_verified",
                  "positive_definite_degree_form_verified", "exact_LLL_inequalities_verified"):
        assert cert[field]
    assert cert["degree_formula"] == "-a^t Omega^{-1} b, coordinates 1,zeta"
    assert len(cert["degrees_of_LLL_Z_basis"]) == 12
    assert int(cert["selected_degree"]) > 0
    assert not cert["global_minimum_degree_claimed"]
    assert not cert["actual_rational_functions_beta_or_height_computed"]
    for row in cert["stages"]:
        assert sha(out/row["file"]) == row["sha256"]
    final = read(out/"R759-original-integral-maps-and-bounded-recovery-input.json.gz")
    assert final["complete"] and final["Z_basis_rank"] == 12 and final["O_K_rank"] == 6
    assert len(final["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]) == 12
    assert len(final["all_integer_periods_interleaved_1_zeta"]) == 1600
    assert final["degrees"] == cert["degrees_of_LLL_Z_basis"]
    assert final["selected_degree"] == cert["selected_degree"]
    assert final["base_point"] == "original c0, with f(c0)=O" and final["c1_coset"] == 4424
    assert not final["actual_RR_basis_or_rational_functions_computed"]
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
    request = read(REQUEST)
    assert request["session"] == "serre-public-resume-20261114"
    item, out = request["job"], root_dir()/"output"
    if args.mode == "compute":
        return compute(item, out)
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
