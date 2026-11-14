#!/usr/bin/env python3
"""R769 public runner: reuse R759 and preserve exact bounded-enumeration states."""
import argparse
import datetime as dt
import gzip
import io
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile

from p41_public_actions_recovery import publish, read, save, sha

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R769-public-retained-degree-search-request.json"
WORKFLOW = REPO/".github/workflows/serre-R769-retained-degree-search.yml"
RESULT = "R769-retained-degree-lattice-bounded-search"
FINAL = "p41-retained-degree-lattice-bounded-search-certificate.json"
CHECKPOINT = "R769-exact-enumeration-checkpoint.json.gz"
SMALL = {"public-actions-input.json", "retained-inputs-receipt.json",
         "resume-receipt.json", "run-receipt.json", "core-receipt.json",
         "public-actions-run.log", "R769-retained-Gram-and-exact-LDL.json", FINAL}


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
    assert Path(name).name == name
    matches = [p for p in directory.rglob(name) if p.is_file() and sha(p) == digest]
    if not matches:
        raise ValueError("No retained artifact file has the required SHA: "+name)
    return matches[0]


def sources(item, out):
    paths = [REPO/"README.md", TOPIC/"README.md", S/item["core"], Path(__file__),
             S/"p41_public_actions_recovery.py", TOPIC/item["method"], REQUEST, WORKFLOW]
    paths += [TOPIC/x for x in item["dependencies"]]
    records = []
    archive = io.BytesIO()
    with tarfile.open(fileobj=archive, mode="w") as tf:
        for path in paths:
            relative = path.relative_to(REPO).as_posix()
            data = path.read_bytes()
            entry = tarfile.TarInfo(relative)
            entry.size, entry.mtime, entry.mode = len(data), 0, 0o644
            tf.addfile(entry, io.BytesIO(data))
            records.append({"file": relative, "sha256": sha(path), "bytes": len(data)})
    target = out/"R769-execution-source.tar.gz"
    target.write_bytes(gzip.compress(archive.getvalue(), mtime=0))
    return {"file": target.name, "sha256": sha(target), "sources": records}


def prepare_inputs(item, out):
    group = item["retained"]["R759"]
    directory = out.parent/"downloaded-R759"
    download(group, directory)
    manifest_path = find_hash(directory, "full-outputs-manifest.json", group["manifest_sha256"])
    manifest = read(manifest_path)
    assert manifest["result"] == "R759-original-integral-period-lattice-and-map-degrees"
    entries = {row["file"]: row for row in manifest["files"]}
    receipt = read(find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"]))
    assert receipt["complete"] and receipt["source_commit"] == group["source_commit"]
    assert receipt["workflow_run_id"] == group["run_id"]
    inputs = out.parent/"inputs"
    inputs.mkdir(parents=True, exist_ok=True)
    copied = []
    for name, digest in group["files"].items():
        assert entries[name]["sha256"] == digest
        source = find_hash(directory, name, digest)
        target = inputs/name
        if target.exists():
            assert sha(target) == digest
        else:
            shutil.copyfile(source, target)
        copied.append({"file": name, "sha256": digest})
    save(out/"retained-inputs-receipt.json", {
        "producer_run": group["run_id"], "producer_source_commit": group["source_commit"],
        "producer_complete": True, "producer_manifest_sha256": group["manifest_sha256"],
        "files": copied, "only_retained_Gram_map_vectors_and_certificate_read": True,
        "old_period_HNF_LLL_or_field_computations_repeated": False})
    return inputs


def restore_resume(item, out):
    spec = item.get("resume")
    if spec is None:
        return
    directory = out.parent/"downloaded-R769-continuation"
    download(spec, directory)
    manifest_path = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
    manifest = read(manifest_path)
    assert manifest["result"] == RESULT
    entries = {row["file"]: row for row in manifest["files"]}
    checkpoint_source = find_hash(directory, CHECKPOINT, entries[CHECKPOINT]["sha256"])
    checkpoint = read(checkpoint_source)
    assert checkpoint["configuration"]["source_sha256"] == item["core_sha256"]
    assert checkpoint["configuration"]["result"] == RESULT
    assert checkpoint["configuration"]["degree_bound"] == item["degree_bound"]
    names = {CHECKPOINT, "R769-retained-Gram-and-exact-LDL.json"}
    names.update(row["file"] for row in checkpoint["audit_blocks"])
    for name in ("R769-enumeration-audit-manifest.json.gz", FINAL):
        if name in entries:
            names.add(name)
    if checkpoint.get("winner") is not None:
        names.add(checkpoint["winner"]["file"])
    copied = []
    for name in sorted(names):
        row = entries[name]
        source = find_hash(directory, name, row["sha256"])
        obj = read(source)
        assert obj["configuration"] == checkpoint["configuration"]
        target = out/name
        if target.exists():
            assert sha(target) == row["sha256"]
        else:
            shutil.copyfile(source, target)
        copied.append({"file": name, "sha256": row["sha256"]})
    # Uncommitted blocks beyond the atomic checkpoint are retained in the old
    # artifact, but are not copied over a new deterministic continuation.
    save(out/"resume-receipt.json", {
        "run_id": spec["run_id"], "artifact_name": spec["artifact_name"],
        "manifest_sha256": spec["manifest_sha256"], "same_core_sha256": item["core_sha256"],
        "committed_traversal_prefix_repeated": False,
        "resume_status": checkpoint["status"], "copied": copied})


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
    save(out/"full-outputs-manifest.json", {
        "result": RESULT, "files": rows, "full_outputs_artifact": artifact,
        "full_exact_checkpoints_and_audit_blocks_in_artifact": True})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    core, method = S/item["core"], TOPIC/item["method"]
    initial = {
        "result": RESULT, "p": 41, "source_commit": source,
        "source_repository": "Rogerhu12/math-research-public",
        "request_sha256": sha(REQUEST), "driver_sha256": sha(__file__),
        "degree_bound": item["degree_bound"], "core_seconds": item["core_seconds"],
        "budget_minutes": item["budget_minutes"], "retained": item["retained"],
        "resume": item.get("resume"), "mathematical_completion_claimed": False,
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()}
    # These two files precede source-archive, download, and schema operations.
    save(out/"public-actions-input.json", initial)
    save(out/"run-receipt.json", {
        "result": RESULT, "complete": False, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "stage": "preparation",
        "no_nonzero_map_claimed": False})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41 and item["degree_bound"] == 693
        assert 1 <= item["core_seconds"] <= 840 and item["budget_minutes"] == 15
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        initial.update(core_sha256=sha(core), method_sha256=sha(method),
                       root_readme_sha256=sha(REPO/"README.md"),
                       topic_readme_sha256=sha(TOPIC/"README.md"),
                       workflow_sha256=sha(WORKFLOW), source_archive=sources(item, out))
        save(out/"public-actions-input.json", initial)
        inputs = prepare_inputs(item, out)
        restore_resume(item, out)
        command = [sys.executable, "-u", str(core), "--inputs", str(inputs),
                   "--output", str(out), "--degree-bound", str(item["degree_bound"]),
                   "--max-seconds", str(item["core_seconds"])]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60)
            except subprocess.TimeoutExpired:
                error = "Wrapper budget reached; requested an atomic exact traversal checkpoint."
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=20)
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
        "result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"], "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(receipt_path) if receipt_path.exists() else None,
        "found": complete and receipt.get("found") is True,
        "exhausted": complete and receipt.get("exhausted") is True,
        "no_nonzero_map_claimed": complete and receipt.get("no_nonzero_map_claimed") is True,
        "old_period_HNF_LLL_or_field_computations_repeated": False,
        "actual_rational_functions_beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    output_manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code,
                      "status": receipt.get("status"), "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"]
    assert sha(out/"core-receipt.json") == run["core_receipt_sha256"]
    receipt = read(out/"core-receipt.json")
    assert receipt["complete"] and receipt["source_sha256"] == item["core_sha256"]
    assert sha(out/FINAL) == receipt["certificate_sha256"]
    cert = read(out/FINAL)
    assert cert["complete"] and cert["degree_bound"] == 693
    assert cert["configuration"]["source_sha256"] == item["core_sha256"]
    assert cert["status"] in ("found", "exhausted")
    assert cert["found"] != cert["exhausted"]
    for key in ("LDL", "checkpoint", "audit_manifest"):
        assert sha(out/cert[key+"_file"]) == cert[key+"_sha256"]
    state = read(out/cert["checkpoint_file"])
    assert state["configuration"] == cert["configuration"] and state["complete"]
    assert state["status"] == cert["status"] and state["counts"] == cert["counts"]
    audit = read(out/cert["audit_manifest_file"])
    assert audit["configuration"] == cert["configuration"] and audit["complete"]
    assert audit["blocks"] == state["audit_blocks"]
    assert audit["final_hash"] == cert["audit_chain_final"] == state["audit_chain_final"]
    for row in audit["blocks"]:
        assert sha(out/row["file"]) == row["sha256"]
    if cert["found"]:
        assert not cert["no_nonzero_map_of_degree_at_most_bound"]
        info = cert["witness"]
        assert sha(out/info["file"]) == info["sha256"]
        witness = read(out/info["file"])
        assert witness["configuration"] == cert["configuration"] and witness["complete"]
        assert len(witness["differential_vector_in_original_omega_basis"]) == 6
        v = [int(x) for x in witness["integer_vector_in_retained_LLL_basis"]]
        assert any(v) and len(v) == 12
        G = [[int(x) for x in row] for row in read(out/cert["LDL_file"])["twice_degree_Gram_matrix"]]
        twice = sum(v[i]*G[i][j]*v[j] for i in range(12) for j in range(12))
        assert twice == 2*int(witness["degree"]) and 0 < twice <= 1386
    else:
        assert cert["no_nonzero_map_of_degree_at_most_bound"]
        assert not state["stack"] and state["winner"] is None
        assert cert["counts"]["leaves"] == cert["counts"]["zero_leaves"] == 1
        assert cert["counts"]["frames_entered"] == cert["counts"]["frames_finished"]
    assert cert["no_old_period_HNF_LLL_or_field_computation_repeated"]
    assert not cert["global_minimum_degree_claimed"]
    return 0


def publish_small(item, out):
    if not (out/"public-actions-input.json").exists():
        raise RuntimeError("No initial source receipt exists.")
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
