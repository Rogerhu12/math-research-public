#!/usr/bin/env python3
"""Public Actions driver for the original p41 marked compact Manin cycles."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys

from p41_public_actions_recovery import publish, read, save, sha

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R738-public-p41-period-input-request.json"
RESULT = "R738-p41-original-period-input"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("This computation runs only in the public repository Actions.")


def output():
    return Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core = S/item["core"]
    method = TOPIC/item["method"]
    assert item["p"] == 41 and item["result"] == RESULT
    assert sha(core) == item["core_sha256"]
    assert sha(method) == item["method_sha256"]
    source = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                     cwd=REPO, text=True).strip()
    save(out/"public-actions-input.json", {
        "result": RESULT, "p": 41, "source_commit": source,
        "source_repository": "Rogerhu12/math-research-public",
        "request_sha256": sha(REQUEST), "driver_sha256": sha(__file__),
        "core_sha256": sha(core), "method_sha256": sha(method),
        "root_readme_sha256": sha(REPO/"README.md"),
        "topic_readme_sha256": sha(TOPIC/"README.md"),
        "dependencies": [{"file": path, "sha256": sha(TOPIC/path)}
                         for path in item["dependencies"]],
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/" +
                   os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mathematical_completion_claimed": False,
    })
    command = [sys.executable, "-u", str(core), "--output", str(out)]
    error = None
    with (out/"public-actions-run.log").open("w") as log:
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                   start_new_session=True)
        try:
            code = process.wait(timeout=item["budget_minutes"]*60)
        except subprocess.TimeoutExpired:
            error = "Budget reached; preserved actual coset, chain, and matrix outputs."
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            code = 124
    path = out/"core-receipt.json"
    core_receipt = read(path) if path.exists() else {"complete": False}
    complete = code == 0 and core_receipt.get("complete") is True
    save(out/"run-receipt.json", {
        "result": RESULT, "p": 41, "complete": complete,
        "process_exit_code": code, "error": error,
        "source_commit": source,
        "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(path) if path.exists() else None,
        "Hodge_period_or_map_or_beta_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    print(json.dumps({"result": RESULT, "complete": complete,
                      "exit_code": code}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["p"] == 41 and run["complete"] is True
    receipt = read(out/"core-receipt.json")
    assert sha(out/"core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["complete"] is True and receipt["source_sha256"] == item["core_sha256"]
    cert_path = out/"p41-original-period-input-certificate.json"
    assert sha(cert_path) == receipt["certificate_sha256"]
    cert = read(cert_path)
    assert cert["complete"] is True and cert["p"] == 41 and cert["level"] == 246
    assert cert["index"] == 4920 and cert["genus"] == 400
    assert cert["relative_rank"] == 819 and cert["compact_rank"] == 800
    assert cert["cusps"] == 20 and cert["cusp_widths"] == [246]*20
    assert cert["elliptic_order2_fixed"] == 0 and cert["elliptic_order3_fixed"] == 3
    assert cert["intersection_determinant"] == "1"
    assert cert["all_SL2Z_lifts_verified"] is True and cert["all_compact_boundaries_zero"] is True
    assert cert["c0_a"] == "0" and cert["c1_deck_a"] == ["1", "zeta", "zeta^2"]
    assert cert["theta_kernel_order"] == 8 and cert["deck_translation"] == 82
    assert cert["c1_unique_real_R_fixed"] is True and cert["c0_real_orbit"] is True
    assert cert["marked_c1_SL2Z"] == [15130, 123, 123, 1]
    assert cert["complex_conjugation_matrix"] == [-1, -1, 0, 1]
    assert cert["Hodge_period_or_map_or_beta_computed"] is False
    for row in cert["files"]:
        assert sha(out/row["file"]) == row["sha256"]
    return 0


def publish_small(item, out):
    # Reproducible coset, chain, and intersection tables stay in the complete Actions artifact.
    # Only bounded receipts and a small final certificate are committed.
    run_id = os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"]
    artifact = "serre-global-" + RESULT + "-" + run_id
    pub = out.parent/"publication"
    pub.mkdir(parents=True, exist_ok=True)
    wanted = {"public-actions-input.json", "core-receipt.json",
              "run-receipt.json", "public-actions-run.log",
              "p41-original-period-input-certificate.json"}
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file():
            continue
        include = path.name in wanted and path.stat().st_size < 100_000
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path), "included_in_git": include,
                     "artifact": artifact})
        if include:
            shutil.copyfile(path, pub/path.name)
    save(pub/"full-outputs-manifest.json",
         {"result": RESULT, "files": rows, "full_outputs_artifact": artifact,
          "reproducible_intermediate_coordinates_in_git": False})
    return publish(item, pub, artifact_prefix="serre-global")

def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "publish", "verify"])
    args = parser.parse_args()
    request = read(REQUEST)
    assert request["session"] == "serre-public-resume-20261114"
    item = request["job"]
    out = output()
    if args.mode == "compute":
        return compute(item, out)
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
