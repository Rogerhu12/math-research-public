#!/usr/bin/env python3
"""Pure IO audit of existing public outputs, with a real partial-clone rule pull."""
import ast
import base64
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/serre-uniformity"
ROOT = Path(__file__).resolve().parents[3]
REQUEST = ROOT/TOPIC/"notes/p41-active-output-audit-request.json"
RULE_PATHS = ("README.md", TOPIC+"/README.md")
OUTPUT = Path(os.environ.get("RUNNER_TEMP", "/tmp"))/"serre-active-output-audit"


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt") if path.suffix == ".gz" else path.open()) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n")


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def api(endpoint):
    return json.loads(subprocess.check_output(["gh", "api", endpoint], text=True))


def git(repo, *args):
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def source_bytes(repo, commit, path):
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    return subprocess.check_output(["git", "show", commit+":"+path], cwd=repo)


def real_rule_pull(request):
    directory = Path(os.environ["RUNNER_TEMP"])/("serre-rules-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"])
    assert not directory.exists()
    subprocess.run(["git", "clone", "--filter=blob:none", "--sparse", "--no-checkout",
                    "--depth=1", "--branch", "main",
                    "https://github.com/"+REPOSITORY+".git", str(directory)], check=True)
    subprocess.run(["git", "sparse-checkout", "set", "--no-cone", *("/"+p for p in RULE_PATHS)],
                   cwd=directory, check=True)
    subprocess.run(["git", "checkout", "main"], cwd=directory, check=True)
    started = utc()
    subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=directory, check=True)
    finished = utc()
    head = git(directory, "rev-parse", "HEAD")
    baseline = request["last_read_rules_commit"]
    subprocess.run(["git", "fetch", "--filter=blob:none", "--depth=1", "origin", baseline],
                   cwd=directory, check=True)
    previous_hashes = {}
    current_hashes = {}
    for path in RULE_PATHS:
        previous_hashes[path] = hashlib.sha256(source_bytes(directory, baseline, path)).hexdigest()
        assert previous_hashes[path] == request["last_read_rule_sha256"][path]
        current_hashes[path] = hashlib.sha256(source_bytes(directory, head, path)).hexdigest()
    difference = subprocess.check_output(["git", "diff", baseline, head, "--", *RULE_PATHS],
                                         cwd=directory, text=True)
    (OUTPUT/"rules.diff").write_text(difference)
    receipt = {"source_repository": REPOSITORY, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
               "actual_command": "git pull --rebase origin main", "partial_clone_filter": "blob:none",
               "started_at_utc": started, "finished_at_utc": finished,
               "last_read_rules_commit": baseline, "pulled_commit": head,
               "previous_readme_sha256": previous_hashes, "current_readme_sha256": current_hashes,
               "rules_changed": bool(difference), "difference": spec(OUTPUT/"rules.diff")}
    save(OUTPUT/"rule-pull-receipt.json", receipt)
    print("SERRE_RULE_PULL_RECEIPT "+json.dumps(receipt, ensure_ascii=False), flush=True)
    if difference:
        print("SERRE_RULE_DIFF_BEGIN\n"+difference+"\nSERRE_RULE_DIFF_END", flush=True)
        raise SystemExit("README changed: root must read the diff before continuing this audit.")
    return directory, receipt


def compact_metadata(value):
    """Only scalar facts, small provenance objects and counts; never coefficient tables."""
    if isinstance(value, dict):
        answer = {}
        for key, entry in value.items():
            if key in {"configuration", "job", "retained_artifacts", "files", "stages",
                       "basis_rows", "tail_rows_in_original_order",
                       "integer_qY_xi_coefficients", "integer_v_t_coefficients"}:
                continue
            if isinstance(entry, list) and len(entry) > 32:
                answer[key+"_count"] = len(entry)
            else:
                answer[key] = compact_metadata(entry)
        return answer
    if isinstance(value, list):
        if len(value) > 32:
            return {"entry_count": len(value)}
        return [compact_metadata(entry) for entry in value]
    if isinstance(value, str) and len(value) > 2000:
        return {"text_bytes": len(value.encode()), "sha256": hashlib.sha256(value.encode()).hexdigest()}
    return value


def verify_target(repository, request, target):
    label, commit = target["label"], target["source_commit"]
    print("SERRE_AUDIT_START "+label+" "+utc(), flush=True)
    run = api("repos/"+REPOSITORY+"/actions/runs/"+target["run_id"])
    assert run["head_sha"] == commit and run["status"] == "completed" and run["conclusion"] == "success"
    artifact = api("repos/"+REPOSITORY+"/actions/artifacts/"+str(target["artifact_id"]))
    assert not artifact["expired"] and artifact["name"] == target["artifact_name"]
    assert artifact["workflow_run"]["id"] == int(target["run_id"])
    assert artifact["workflow_run"]["head_sha"] == commit
    assert artifact["digest"] == "sha256:"+target["archive_sha256"]
    assert artifact["size_in_bytes"] == target["archive_bytes"]
    workspace = Path(os.environ["RUNNER_TEMP"])/("serre-output-audit-"+label)
    workspace.mkdir()
    archive = workspace/"producer.zip"
    with archive.open("wb") as destination:
        subprocess.run(["gh", "api", "repos/"+REPOSITORY+"/actions/artifacts/"+
                        str(target["artifact_id"])+"/zip"], stdout=destination, check=True)
    assert archive.stat().st_size == target["archive_bytes"]
    assert sha(archive) == target["archive_sha256"]
    extracted = workspace/"extracted"
    extracted.mkdir()
    with zipfile.ZipFile(archive) as container:
        for entry in container.infolist():
            path = Path(entry.filename)
            assert not path.is_absolute() and ".." not in path.parts
            assert ((entry.external_attr >> 16) & 0o170000) != 0o120000
        container.extractall(extracted)
    archive.unlink()
    finals = list(extracted.rglob(target["certificate_name"]))
    assert len(finals) == 1
    out = finals[0].parent
    manifest_path = out/"full-outputs-manifest.json"
    manifest = read(manifest_path)
    assert manifest["result"] == target["result"]
    entries = {entry["file"]: entry for entry in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    for name, entry in entries.items():
        assert Path(name).name == name
        path = out/name
        assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
    subprocess.run(["git", "fetch", "--filter=blob:none", "--depth=1", "origin", commit],
                   cwd=repository, check=True)
    original_request = source_bytes(repository, commit, target["request_path"])
    assert hashlib.sha256(original_request).hexdigest() == target["request_sha256"]
    job = json.loads(original_request)["job"]
    assert job["result"] == target["result"] and job["core_sha256"] == target["core_sha256"]
    initial, receipt, core = (read(out/name) for name in
                              ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    assert initial["source_repository"] == REPOSITORY and initial["source_commit"] == commit
    assert receipt["source_commit"] == commit and receipt["workflow_run_id"] == target["run_id"]
    assert initial["job"] == job and initial["request_sha256"] == target["request_sha256"]
    assert initial["driver_sha256"] == target["wrapper_sha256"]
    assert initial["core_sha256"] == target["core_sha256"]
    assert hashlib.sha256(source_bytes(repository, commit, TOPIC+"/scripts/"+job["core"])).hexdigest() == target["core_sha256"]
    assert hashlib.sha256(source_bytes(repository, commit, job["workflow"])).hexdigest() == initial["workflow_sha256"]
    for path, field in ((RULE_PATHS[0], "root_readme_sha256"), (RULE_PATHS[1], "topic_readme_sha256")):
        assert hashlib.sha256(source_bytes(repository, commit, path)).hexdigest() == initial[field]
    sources = workspace/"source"/TOPIC/"scripts"
    sources.mkdir(parents=True)
    for name, digest in request["io_helpers_sha256"].items():
        data = source_bytes(repository, commit, TOPIC+"/scripts/"+name)
        assert hashlib.sha256(data).hexdigest() == digest
        (sources/name).write_bytes(data)
        ast.parse(data, filename=name)
    wrapper = source_bytes(repository, commit, target["wrapper_path"])
    assert hashlib.sha256(wrapper).hexdigest() == target["wrapper_sha256"]
    wrapper_path = sources/Path(target["wrapper_path"]).name
    wrapper_path.write_bytes(wrapper)
    ast.parse(wrapper, filename=wrapper_path.name)
    sys.path.insert(0, str(sources))
    module_spec = importlib.util.spec_from_file_location("audit_"+label, wrapper_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    assert module.RESULT == target["result"] and module.FINAL == target["certificate_name"]
    code = module.verify(out) if label == "R800" else module.verify(job, out)
    assert code == 0
    sys.path.pop(0)
    certificate = read(out/target["certificate_name"])
    stage_spec = certificate["stage_manifest"]
    stages = read(out/stage_spec["file"])
    retained = read(out/"retained-inputs-receipt.json")
    summary = {"label": label, "result": target["result"], "run_id": target["run_id"],
               "source_commit": commit, "artifact_id": target["artifact_id"],
               "artifact_name": target["artifact_name"], "archive_bytes": target["archive_bytes"],
               "archive_sha256": target["archive_sha256"], "artifact_expires_at": artifact["expires_at"],
               "request_sha256": target["request_sha256"], "core_sha256": target["core_sha256"],
               "wrapper_sha256": target["wrapper_sha256"], "certificate": spec(out/target["certificate_name"]),
               "full_manifest": spec(manifest_path), "output_file_count": len(entries),
               "stage_manifest": stage_spec, "stage_file_count": len(stages["files"]),
               "core_receipt": compact_metadata(core), "run_receipt": compact_metadata(receipt),
               "certificate_metadata": compact_metadata(certificate),
               "retained_input_metadata": compact_metadata(retained),
               "full_archive_hash_verified": True, "all_manifest_file_hashes_verified": True,
               "source_bound_wrapper_io_verify_exit_code": code,
               "new_mathematical_arithmetic_executed_by_audit": False,
               "audited_at_utc": utc()}
    if label == "R799":
        summary["basis_index_metadata"] = {
            power: compact_metadata(read(out/entry["file"]))
            for power, entry in certificate["basis_indices"].items()}
        summary["power6_tail_index_metadata"] = compact_metadata(read(out/certificate["power6_tail_index"]["file"]))
    elif label == "R800":
        summary["basis_tail_index_metadata"] = compact_metadata(read(out/certificate["basis_tail_index"]["file"]))
    else:
        summary["map_prefix_metadata"] = [
            compact_metadata(read(out/entry["file"])) for entry in certificate["map_prefix_certificates"]]
    encoded = json.dumps(summary, ensure_ascii=False)
    assert len(encoded.encode()) < 90000
    save(OUTPUT/(label+"-audit-summary.json"), summary)
    print("SERRE_AUDIT_SUMMARY "+encoded, flush=True)
    shutil.rmtree(workspace)
    return summary


def syntax_blobs(request):
    answer = []
    for entry in request.get("syntax_only_blobs", []):
        value = api("repos/"+REPOSITORY+"/git/blobs/"+entry["blob_sha"])
        assert value["encoding"] == "base64"
        content = base64.b64decode(value["content"])
        assert len(content) == entry["bytes"]
        assert hashlib.sha256(content).hexdigest() == entry["sha256"]
        assert hashlib.sha1(b"blob "+str(len(content)).encode()+b"\0"+content).hexdigest() == entry["blob_sha"]
        ast.parse(content, filename=entry["file"])
        answer.append({**entry, "ast_parse_passed": True, "imported_or_executed": False})
    save(OUTPUT/"syntax-only-receipt.json", answer)
    print("SERRE_SYNTAX_ONLY "+json.dumps(answer), flush=True)
    return answer


def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
    OUTPUT.mkdir(parents=True, exist_ok=True)
    request = read(REQUEST)
    assert sha(__file__) == request["audit_script_sha256"]
    repo, pull = real_rule_pull(request)
    syntax = syntax_blobs(request)
    summaries = []
    for target in request["targets"]:
        summaries.append(verify_target(repo, request, target))
    save(OUTPUT/"audit-complete.json", {
        "complete": True, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "source_commit": os.environ["GITHUB_SHA"], "finished_at_utc": utc(),
        "rule_pull": pull, "syntax_only": syntax,
        "audited_summaries": [spec(OUTPUT/(s["label"]+"-audit-summary.json")) for s in summaries],
        "audit_script_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "new_mathematical_arithmetic_executed": False})
    print("SERRE_AUDIT_COMPLETE "+json.dumps(read(OUTPUT/"audit-complete.json")), flush=True)


if __name__ == "__main__":
    main()
