#!/usr/bin/env python3
"""Public Actions wrapper for the original p41 Hodge input; reuse R738."""
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
REQUEST = TOPIC/"notes/R745-public-p41-Hodge-input-request.json"
RESULT = "R745-p41-original-Hodge-input"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("This computation runs only in the public repository Actions.")


def output():
    return Path(os.environ["RUNNER_TEMP"])/"serre-global"/RESULT/"output"


def retained_inputs(item, out):
    original = item["retained_topology"]
    archive = out.parent/"downloaded-R738"
    archive.mkdir(parents=True, exist_ok=True)
    subprocess.run(["gh", "run", "download", original["run_id"], "--repo",
                    "Rogerhu12/math-research-public", "--name", original["artifact_name"],
                    "--dir", str(archive)], check=True)
    dest = out.parent/"retained-topology"
    dest.mkdir(parents=True, exist_ok=True)
    records = []
    for name, expected in original["files"].items():
        matches = [path for path in archive.rglob(name) if path.is_file()]
        matching = [path for path in matches if sha(path) == expected]
        if not matching:
            raise ValueError("The retained R738 artifact file has no matching SHA: " + name)
        target = dest/name
        shutil.copyfile(matching[0], target)
        records.append({"file": name, "sha256": sha(target)})
    run = read(dest/"run-receipt.json")
    assert run["complete"] and run["source_commit"] == original["source_commit"]
    assert run["workflow_run_id"] == original["run_id"]
    assert run["workflow_attempt"] == "1"
    cert = read(dest/"p41-original-period-input-certificate.json")
    assert cert["complete"] and cert["c1_coset"] == 4424
    save(out/"retained-topology-receipt.json", {
        "run_id": original["run_id"], "source_commit": original["source_commit"],
        "artifact_name": original["artifact_name"], "files": records,
        "topology_recomputed": False})
    return dest


def compute(item, out):
    out.mkdir(parents=True, exist_ok=True)
    core, method = S/item["core"], TOPIC/item["method"]
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
        "retained_topology": item["retained_topology"],
        "retained_character": item["retained_character"],
        "run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/"+
                   os.environ["GITHUB_RUN_ID"],
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mathematical_completion_claimed": False})
    error = None
    code = 1
    try:
        assert item["p"] == 41 and item["result"] == RESULT
        assert sha(core) == item["core_sha256"]
        assert sha(method) == item["method_sha256"]
        character_path = TOPIC/item["retained_character"]["path"]
        assert sha(character_path) == item["retained_character"]["sha256"]
        character = read(character_path)
        assert character["complete"] and character["configuration"]["prime"] == 41
        fixed = character["configuration"]["finite_field"]
        assert fixed["basis"] == ["1", "zeta"] and fixed["gamma"] == [7, 30]
        assert fixed["order"] == 42 and fixed["gamma_to_n_over_3"] == [0, 1]
        old = retained_inputs(item, out)
        command = [sys.executable, "-u", str(core), "--output", str(out),
                   "--retained-topology", str(old)]
        with (out/"public-actions-run.log").open("w") as stream:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=item["budget_minutes"]*60)
            except subprocess.TimeoutExpired:
                error = "Budget reached; preserved exact new outputs and retained inputs."
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
    save(out/"run-receipt.json", {"result": RESULT, "p": 41,
        "complete": complete, "process_exit_code": code, "error": error,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "execution_environment": "public-repository-github-actions",
        "core_receipt_sha256": sha(path) if path.exists() else None,
        "CM_period_or_map_or_beta_or_height_computed": False,
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    print(json.dumps({"result": RESULT, "complete": complete,
                      "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    run = read(out/"run-receipt.json")
    assert run["result"] == RESULT and run["complete"]
    receipt = read(out/"core-receipt.json")
    assert sha(out/"core-receipt.json") == run["core_receipt_sha256"]
    assert receipt["complete"] and receipt["source_sha256"] == item["core_sha256"]
    path = out/"p41-original-Hodge-input-certificate.json"
    assert sha(path) == receipt["certificate_sha256"]
    cert = read(path)
    assert cert["complete"] and cert["p"] == 41 and cert["level"] == 246
    assert cert["source_genus"] == 400 and cert["Hodge_rank"] == 6
    assert cert["max_exponent_Q"] == 800 and cert["original_norm_mod_p"] == [40, 0]
    assert cert["torus_invariance_verified"] and cert["normalizer_invariance_verified"]
    assert cert["full_tame_descent_verified"] and not cert["topology_recomputed"]
    assert cert["c1_coset"] == 4424 and cert["c1_raw_transport"] == "zeta^2"
    assert cert["c0_cosets"] == [2876, 2822, 2823]
    assert cert["finite_translate_pairs"] == 40 and cert["relative_edges"] == 819
    assert cert["period_prefactor"] == "alpha*sqrt(-3)/7"
    assert cert["differential_q_parameter_factor"] == 246
    assert cert["rank_certificate"]["rank"] == 6
    assert cert["rank_certificate"]["determinant_mod_prime"] != 0
    assert cert["CM_period_or_map_or_beta_or_height_computed"] is False
    for row in cert["files"]:
        assert sha(out/row["file"]) == row["sha256"]
    old = read(out/"retained-topology-receipt.json")
    assert not old["topology_recomputed"]
    assert old["run_id"] == item["retained_topology"]["run_id"]
    return 0


def publish_small(item, out):
    run_id = os.environ["GITHUB_RUN_ID"]+"-"+os.environ["GITHUB_RUN_ATTEMPT"]
    artifact = "serre-global-"+RESULT+"-"+run_id
    pub = out.parent/"publication"
    pub.mkdir(parents=True, exist_ok=True)
    wanted = {"public-actions-input.json", "core-receipt.json", "run-receipt.json",
              "retained-topology-receipt.json", "public-actions-run.log",
              "p41-original-Hodge-input-certificate.json"}
    rows = []
    for path in sorted(out.iterdir()):
        if not path.is_file():
            continue
        include = path.name in wanted and path.stat().st_size < 100_000
        rows.append({"file": path.name, "bytes": path.stat().st_size,
                     "sha256": sha(path), "included_in_git": include, "artifact": artifact})
        if include:
            shutil.copyfile(path, pub/path.name)
    save(pub/"full-outputs-manifest.json", {"result": RESULT, "files": rows,
         "full_outputs_artifact": artifact, "reproducible_intermediate_coordinates_in_git": False})
    return publish(item, pub, artifact_prefix="serre-global")


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "publish", "verify"])
    args = parser.parse_args()
    request = read(REQUEST)
    assert request["session"] == "serre-public-resume-20261114"
    item, out = request["job"], output()
    if args.mode == "compute":
        return compute(item, out)
    if args.mode == "publish":
        return publish_small(item, out)
    return verify(item, out)


if __name__ == "__main__":
    sys.exit(main())
