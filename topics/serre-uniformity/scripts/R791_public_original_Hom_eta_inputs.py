#!/usr/bin/env python3
"""Public R791 runner: consume old artifacts, retain new outputs only temporarily."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

from p41_public_actions_recovery import read, save, sha
from R786_public_exact_power5_short_basis import download, find_hash

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R791-public-original-Hom-eta-inputs-request.json"
RESULT = "R791-original-Hom-Galois-and-eta-inputs"
FINAL = "p41-original-Hom-Galois-and-eta-input-certificate.json"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New arithmetic belongs to public repository Actions.")


def topic_path(relative):
    path = Path(relative)
    assert not path.is_absolute() and ".." not in path.parts
    return TOPIC/path


def prepare(item, out):
    inputs = out.parent/"inputs"
    inputs.mkdir(parents=True, exist_ok=True)
    records = []
    for label, spec in item["retained_artifacts"].items():
        directory = out.parent/("downloaded-"+label)
        download(spec, directory, require_complete=True)
        mp = find_hash(directory, "full-outputs-manifest.json", spec["manifest_sha256"])
        manifest = read(mp)
        assert manifest["result"] == spec["result"]
        entries = {row["file"]: row for row in manifest["files"]}
        rp = find_hash(directory, "run-receipt.json", entries["run-receipt.json"]["sha256"])
        run = read(rp)
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert run["source_commit"] == spec["source_commit"]
        assert run["workflow_run_id"] == spec["run_id"]
        cp = find_hash(directory, spec["certificate_name"], spec["files"][spec["certificate_name"]])
        certificate = read(cp)
        assert certificate["complete"] is True
        assert certificate["configuration"]["source_sha256"] == spec["core_sha256"]
        stages = {row["file"]: row for row in certificate["stages"]}
        for name, digest in spec["files"].items():
            assert entries[name]["sha256"] == digest
            source = find_hash(directory, name, digest)
            assert source.stat().st_size == entries[name]["bytes"]
            if name != spec["certificate_name"]:
                assert stages[name]["sha256"] == digest
                assert read(source)["configuration"] == certificate["configuration"]
            shutil.copyfile(source, inputs/name)
        records.append({"producer": spec, "run_source_and_artifact_digest_verified": True,
                        "all_copied_files_bound_to_completed_certificate": True})
    for spec in item["retained_repository_files"]:
        source = topic_path(spec["path"])
        assert sha(source) == spec["sha256"]
        assert Path(spec["file"]).name == spec["file"]
        shutil.copyfile(source, inputs/spec["file"])
    save(out/"retained-inputs-receipt.json", {"artifact_groups": records,
        "repository_files": item["retained_repository_files"],
        "old_Miller_period_Hom_HNF_LLL_or_CM_values_recomputed": False})
    return inputs


def manifest(out):
    rows = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
            for p in sorted(out.iterdir()) if p.is_file() and p.name != "full-outputs-manifest.json"]
    save(out/"full-outputs-manifest.json", {"result": RESULT, "files": rows,
        "temporary_active_checkpoint_artifact": "serre-global-"+RESULT+"-"+
            os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"],
        "temporary_active_checkpoint_retention_days": 1,
        "reproducible_outputs_saved_in_repository_or_release": False})


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {"result": RESULT, "job": item,
        "source_repository": "Rogerhu12/math-research-public", "source_commit": source,
        "driver_sha256": sha(__file__), "request_sha256": sha(REQUEST),
        "root_readme_sha256": sha(REPO/"README.md"), "topic_readme_sha256": sha(TOPIC/"README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    code, error = 1, None
    try:
        assert item["result"] == RESULT and item["p"] == 41
        core, method = S/item["core"], topic_path(item["method"])
        assert sha(core) == item["core_sha256"] and sha(method) == item["method_sha256"]
        assert sha(S/"R754_original_periods_and_Hom_kernel.py") == item["field_helper_sha256"]
        inputs = prepare(item, out)
        command = [sys.executable, "-u", str(core), "--inputs", str(inputs), "--output", str(out),
                   "--method", str(method), "--request", str(REQUEST)]
        with (out/"public-actions-run.log").open("w") as stream:
            result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                    timeout=item["budget_minutes"]*60, check=False)
        code = result.returncode
    except BaseException as exc:
        error = type(exc).__name__+": "+str(exc)
    complete = code == 0 and (out/FINAL).exists() and read(out/FINAL).get("complete") is True
    if not complete and code == 0:
        code = 1
    save(out/"run-receipt.json", {"result": RESULT, "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "process_exit_code": code, "complete": complete, "error": error,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    manifest(out)
    if (out/"public-actions-run.log").exists():
        # These are stage SHA summaries and final small result fields, never matrices.
        for line in (out/"public-actions-run.log").read_text().splitlines():
            if line.startswith("{"):
                print(line, flush=True)
            elif not complete:
                print(line, flush=True)
    print(json.dumps({"result": RESULT, "complete": complete, "process_exit_code": code,
                      "error": error, "manifest_sha256": sha(out/"full-outputs-manifest.json")}), flush=True)
    return code


def verify(out):
    receipt = read(out/"run-receipt.json")
    assert receipt["complete"] is True and receipt["process_exit_code"] == 0
    certificate = read(out/FINAL)
    assert certificate["complete"] is True and certificate["result"] == RESULT
    initial = read(out/"public-actions-input.json")
    assert certificate["configuration"]["source_sha256"] == initial["job"]["core_sha256"]
    assert certificate["configuration"]["method_sha256"] == initial["job"]["method_sha256"]
    assert certificate["configuration"]["request_sha256"] == initial["request_sha256"]
    assert certificate["actual_eta_polar_divisors_points_heights_or_uniformity_computed"] is False
    for row in certificate["stages"]:
        path = out/row["file"]
        assert path.stat().st_size == row["bytes"] and sha(path) == row["sha256"]
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
