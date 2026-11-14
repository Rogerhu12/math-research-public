#!/usr/bin/env python3
"""Public recovery using pinned completed R717 bins and independent chirp phases."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import traceback

from p41_public_actions_recovery import REPO, TOPIC, publish
from R717_public_original_cm_norm import wait_with_readme_checks, stop_process

HERE = Path(__file__).resolve().parent
CORE = HERE / "R717_certified_original_CM_norm.py"
MONITOR = HERE / "R717_public_original_cm_norm.py"
REQUEST = TOPIC / "notes/R717-direct-chirp-recover-request.json"
COMPAT = TOPIC / "notes/R717-p137147-fixed-bin-compatibility.json"
WORKFLOW = REPO / ".github/workflows/serre-R717-direct-chirp-recover.yml"
FINAL = "R717-exact-original-CM-norm.json"
SESSION = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "R717-direct-chirp-session.json"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".next")
    temp.write_text(json.dumps(obj, indent=2) + "\n")
    temp.replace(path)


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def archive(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
            stream.write(data)


def copy_exact(source, target, expected):
    assert sha(source) == expected
    if target.exists():
        assert sha(target) == expected
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    assert sha(target) == expected


def expected_configuration(request, compatibility):
    old = dict(compatibility["old_configuration"])
    old.pop("parameter_sha256")
    old["source_sha256"] = request["arithmetic_sha256"]
    old["parameter_sha256"] = digest(old)
    return old


def validate_request(request):
    assert request["result"] == "R717-original-CM-norm-p137147-direct-chirps"
    assert request["prime"] == 137147 and request["shard_count"] == 4
    assert request["prec_bits"] == 384 and request["tail_bits"] == 256
    assert request["cutoff_multiple"] == 360 and 0 < request["timeout_seconds"] <= 18000
    assert request["python_flint_version"] == "0.9.0"
    assert request["arithmetic_sha256"] == sha(CORE)
    assert request["wrapper_sha256"] == sha(__file__)
    assert request["monitor_sha256"] == sha(MONITOR)
    assert request["compatibility_manifest_sha256"] == sha(COMPAT)
    diagnostic_path = REPO / request["diagnostic_summary_path"]
    assert request["diagnostic_summary_sha256"] and sha(diagnostic_path) == request["diagnostic_summary_sha256"]
    diagnostic = read(diagnostic_path)
    assert diagnostic["complete"] and diagnostic["lattice_enumerations"] == diagnostic["DFTs"] == 0
    compatibility = read(COMPAT)
    assert compatibility["new_core_sha256"] == request["arithmetic_sha256"]
    assert compatibility["source_run_id"] == request["source_run_id"]
    assert compatibility["source_artifact_name"] == request["source_artifact_name"]
    return compatibility, expected_configuration(request, compatibility)


def check_final(path, expected, require_local_artifacts):
    receipt = read(path)
    assert receipt["configuration"] == expected
    assert receipt["complete"] and receipt["all_rows_covered"] and receipt["all_trace_roundings_unique"]
    legacy = receipt["reused_legacy_bin_proof"]
    assert legacy["entire_bin_producer_prefix_byte_equal"]
    assert legacy["all_numeric_configuration_fields_unchanged"]
    assert not legacy["completed_bins_recomputed"]
    if require_local_artifacts:
        for item in receipt["artifacts"]:
            assert sha(path.parent/item["file"]) == item["sha256"]
    return receipt


def existing_complete(request, expected, out):
    local = out / FINAL
    if local.exists():
        receipt = check_final(local, expected, True)
        return {"kind": "same-output-complete", "receipt": str(local),
                "receipt_sha256": sha(local), "padic_result": receipt["padic_result"]}
    base = TOPIC/"computations"/request["result"]
    if not base.exists():
        return None
    for path in sorted(base.glob("*/"+FINAL)):
        receipt = check_final(path, expected, False)
        manifest = read(path.parent/"files-manifest.json")
        row = next(item for item in manifest["files"] if item["file"] == FINAL)
        assert row["sha256"] == sha(path)
        ref = {"kind": "previous-public-complete", "repository_path": str(path.relative_to(REPO)),
               "receipt_sha256": sha(path), "full_outputs_artifact": manifest["full_outputs_artifact"],
               "source_commit": manifest["source_commit"],
               "configuration": receipt["configuration"], "padic_result": receipt["padic_result"],
               "previous_complete_not_reexecuted": True}
        save(out/"R717-reused-complete-reference.json", ref)
        return ref
    return None


def pre_recover_readme_check(out, source):
    fetch = subprocess.run(["git", "fetch", "--depth=1", "--filter=blob:none", "origin", "main"],
                           cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           timeout=120)
    record = {"source_commit": source, "fetch_exit_code": fetch.returncode, "fetch_log": fetch.stdout}
    if fetch.returncode:
        save(out/"R717-pre-recover-readme-check.json", record)
        raise RuntimeError("Could not refresh public README rules")
    diff = subprocess.run(["git", "diff", source, "origin/main", "--", "README.md",
                           "topics/serre-uniformity/README.md"], cwd=REPO, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
    record.update(diff_exit_code=diff.returncode, readmes_changed=bool(diff.stdout.strip()),
                  checked_main_commit=subprocess.check_output(["git", "rev-parse", "origin/main"],
                                                               cwd=REPO, text=True).strip())
    save(out/"R717-pre-recover-readme-check.json", record)
    if diff.returncode or diff.stdout.strip():
        (out/"R717-readme-rules.diff").write_text(diff.stdout)
        raise RuntimeError("README changed; retain inputs and await rule review")


def compute():
    out = Path(os.environ["RUNNER_TEMP"])/"R717-direct-chirp-recover-output"
    out.mkdir(parents=True, exist_ok=True)
    source = os.environ["GITHUB_SHA"]
    result = "R717-original-CM-norm-p137147-direct-chirps"
    request = {}
    save(SESSION, {"out": str(out), "result": result, "request": request})
    summary = {"complete": False, "result": result, "source_commit": source,
               "execution_environment": "public-repository-github-actions",
               "lattice_enumerations": 0, "mathematical_completion_claimed": False}
    save(out/"run-receipt.json", summary)
    source_input = {"result": result, "source_commit": source, "request": request,
                    "sources": [], "source_repository": "Rogerhu12/math-research-public",
                    "execution_environment": "public-repository-github-actions",
                    "mathematical_completion_claimed": False}
    save(out/"public-actions-input.json", source_input)
    process = None
    try:
        request = read(REQUEST)
        save(SESSION, {"out": str(out), "result": result, "request": request})
        source_input.update(request=request, request_sha256=sha(REQUEST))
        save(out/"public-actions-input.json", source_input)
        for path in [Path(__file__), CORE, MONITOR, COMPAT, REQUEST, WORKFLOW,
                     HERE/"p41_public_actions_recovery.py", REPO/"README.md", TOPIC/"README.md"]:
            rel = path.relative_to(REPO)
            dst = out/"sources"/(str(rel)+".gz")
            archive(dst, path.read_bytes())
            source_input["sources"].append({"path": str(rel), "sha256": sha(path),
                            "archive": str(dst.relative_to(out)), "archive_sha256": sha(dst)})
            save(out/"public-actions-input.json", source_input)
        compatibility, expected = validate_request(request)
        diagnostic_path = REPO/request["diagnostic_summary_path"]
        copy_exact(diagnostic_path, out/"R717-prior-diagnostic-summary.json",
                   request["diagnostic_summary_sha256"])
        completed = existing_complete(request, expected, out)
        if completed:
            summary.update(complete=True, status="REUSED_COMPLETE", reference=completed)
            save(out/"run-receipt.json", summary)
            print(json.dumps(summary), flush=True)
            return
        dest = Path(os.environ["RUNNER_TEMP"])/"R717-direct-chirp-original-input"
        dest.mkdir(parents=True, exist_ok=True)
        subprocess.run(["gh", "run", "download", request["source_run_id"], "--repo",
                        "Rogerhu12/math-research-public", "--name",
                        request["source_artifact_name"], "--dir", str(dest)],
                       check=True, timeout=900)
        copied = []
        for name, expected_sha in compatibility["bin_files_sha256"].items():
            matches = list(dest.rglob(name))
            assert len(matches) == 1
            copy_exact(matches[0], out/name, expected_sha)
            copied.append({"file": name, "sha256": expected_sha, "completed_bin_recomputed": False})
        source_matches = list(dest.rglob("R717_certified_original_CM_norm.py.gz"))
        assert len(source_matches) == 1
        copy_exact(source_matches[0], out/compatibility["original_source_archive"],
                   request["original_source_archive_sha256"])
        copy_exact(COMPAT, out/"R717-reused-bin-compatibility.json",
                   request["compatibility_manifest_sha256"])
        save(out/"R717-reused-bin-inputs.json", {
             "source_run_id": request["source_run_id"],
             "source_artifact_name": request["source_artifact_name"],
             "completed_bins": copied, "original_source_archive": compatibility["original_source_archive"],
             "original_source_archive_sha256": request["original_source_archive_sha256"],
             "old_failed_embeddings_copied": False, "old_failed_trace_balls_copied": False})
        pre_recover_readme_check(out, source)
        command = [sys.executable, "-u", str(CORE), "--prime", str(request["prime"]),
                   "--phase", "recover", "--output-dir", str(out),
                   "--shard-count", str(request["shard_count"]),
                   "--prec-bits", str(request["prec_bits"]), "--tail-bits", str(request["tail_bits"]),
                   "--cutoff-multiple", str(request["cutoff_multiple"]),
                   "--bin-compatibility", str(out/"R717-reused-bin-compatibility.json")]
        save(out/"R717-command.json", {"command": command, "arithmetic_sha256": sha(CORE),
             "expected_configuration": expected, "completed_lattice_terms_recomputed": 0})
        with (out/"R717-public-run.log").open("w") as log:
            process = subprocess.Popen(command, cwd=REPO, stdout=log,
                                       stderr=subprocess.STDOUT, start_new_session=True)
            code = wait_with_readme_checks(process, request, out, source)
        if code:
            raise RuntimeError(f"Original norm recovery returned {code}; all partial outputs retained")
        receipt = check_final(out/FINAL, expected, True)
        summary.update(complete=True, status="RECOVERED_WITH_DIRECT_CHIRPS",
                       core_receipt_sha256=sha(out/FINAL), padic_result=receipt["padic_result"],
                       all_rows_covered=True, all_trace_roundings_unique=True,
                       completed_lattice_terms_recomputed=0)
        save(out/"run-receipt.json", summary)
        print(json.dumps(summary), flush=True)
    except BaseException:
        if process is not None and process.poll() is None:
            stop_process(process)
        (out/"R717-public-failure.txt").write_text(traceback.format_exc())
        save(out/"run-receipt.json", summary)
        raise


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("phase", choices=["run", "publish", "verify"])
    args = ap.parse_args()
    if args.phase == "run":
        compute()
        return
    session = read(SESSION)
    out = Path(session["out"])
    if args.phase == "publish":
        raise SystemExit(publish({"result": session["result"]}, out, "serre-cartier"))
    receipt = read(out/"run-receipt.json")
    assert receipt["complete"] and receipt["lattice_enumerations"] == 0
    if receipt["status"] == "REUSED_COMPLETE":
        reference = receipt["reference"]
        assert reference["kind"] in ("same-output-complete", "previous-public-complete")
    else:
        assert sha(out/FINAL) == receipt["core_receipt_sha256"]
        assert receipt["all_trace_roundings_unique"] and receipt["all_rows_covered"]
    print("ORIGINAL_CM_RECOVERY_VERIFIED")


if __name__ == "__main__":
    main()
