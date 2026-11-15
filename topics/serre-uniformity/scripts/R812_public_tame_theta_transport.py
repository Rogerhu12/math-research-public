#!/usr/bin/env python3
"""R812 public Actions driver for the six fixed exact CM transport cases."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R812-public-tame-theta-transport-request.json"
RESULT = "R812-fixed-tame-theta-transport"
FINAL = "R812-six-case-result.json"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R812 new arithmetic belongs to the public repository Actions.")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, data):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


def spec(path):
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def inside(relative):
    p = Path(relative)
    assert not p.is_absolute() and ".." not in p.parts
    return REPO / p


def check_sources(item):
    assert item["result"] == RESULT and item["scope"] == "six_fixed_algebraic_cases"
    assert item["image"] == "sagemath/sagemath:10.6"
    assert item["sage_version"] == "10.6"
    assert item["budget_minutes"] == 30
    for key in ("core", "wrapper", "proof", "workflow"):
        assert sha(inside(item[key])) == item[key + "_sha256"]
    assert inside(item["wrapper"]).resolve() == Path(__file__).resolve()


def manifest(out):
    artifact = "serre-global-" + RESULT + "-" + os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"]
    rows = [dict(spec(p), included_in_git=False, artifact=artifact)
            for p in sorted(out.iterdir()) if p.is_file() and p.name not in (MANIFEST, REFERENCE)]
    save(out / MANIFEST, {"result": RESULT, "files": rows, "artifact": artifact,
        "retention_days": 1, "automatic_git_or_release_publication": False})
    save(out / REFERENCE, {"result": RESULT, "manifest": spec(out / MANIFEST),
        "artifact": artifact, "file_count": len(rows), "raw_output_in_git_or_release": False})


def parse_log(text, item):
    matches = re.findall(r"^EXECUTION_METADATA=(.*)$", text, re.M)
    assert len(matches) == 1
    meta = json.loads(matches[0])
    for key, env in (("run_id", "GITHUB_RUN_ID"), ("run_attempt", "GITHUB_RUN_ATTEMPT"),
                     ("source_commit", "GITHUB_SHA"), ("repository", "GITHUB_REPOSITORY")):
        assert str(meta[key]) == os.environ[env]
    assert meta["github_actions"] == "true" and meta["source_sha256"] == item["core_sha256"]
    versions = re.findall(r"^SAGE_VERSION=(.*)$", text, re.M)
    assert versions == [item["sage_version"]]
    start = re.search(r"^\{", text, re.M)
    assert start is not None
    result, used = json.JSONDecoder().raw_decode(text[start.start():])
    assert result["result"] == RESULT and result["source_sha256"] == item["core_sha256"]
    digest = hashlib.sha256(canonical(result)).hexdigest()
    assert re.findall(r"^RESULT_SHA256=([0-9a-f]{64})$", text, re.M) == [digest]
    assert result["all_identity_checks_passed"] is True
    assert result["basis"] == ["S", "F", "H", "R", "J", "G"]
    cases = result["cases"]
    assert len(cases) == 6
    assert [(c["gaussian_sign"], c["frobenius_j"]) for c in cases] == [(s, j) for s in (1, -1) for j in range(3)]
    for case in cases:
        assert len(case["FG_power_basis"]) == 12
        cert = case["FG"]
        assert int(cert["power_basis_denominator"]) > 0
        assert isinstance(cert["zero"], bool)
        assert cert["zero"] == (int(cert["integral_norm"]) == 0)
        assert (cert["nonzero_integral_norm_factors"] is None) == cert["zero"]
    assert result["all_six_FG_outputs_nonzero"] is all(not c["FG"]["zero"] for c in cases)
    assert result["det_U"]["zero"] is False
    assert int(result["U_entry_common_denominator"]) > 0
    return meta, result, digest


def compute(item, out):
    guard()
    out.mkdir(parents=True, exist_ok=True)
    check_sources(item)
    source = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    assert source == os.environ["GITHUB_SHA"]
    save(out / "public-actions-input.json", {"result": RESULT, "source_commit": source,
        "source_repository": os.environ["GITHUB_REPOSITORY"], "job": item,
        "request_sha256": sha(REQUEST), "root_readme_sha256": sha(REPO / "README.md"),
        "topic_readme_sha256": sha(TOPIC / "README.md"),
        "prepared_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "finite_case_computation_only": True, "prime_scan_or_high_sigma_jet": False})
    started = time.monotonic()
    log = out / "public-actions-run.log"
    name = "serre-R812-" + os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"]
    error, code, parsed = None, 1, None
    try:
        subprocess.run(["docker", "pull", item["image"]], check=True)
        info = json.loads(subprocess.check_output(["docker", "image", "inspect", item["image"]], text=True))[0]
        digests = [d for d in info["RepoDigests"] if d.startswith("sagemath/sagemath@sha256:")]
        assert len(digests) == 1 and info["Os"] == "linux" and info["Architecture"] == "amd64"
        fixed_image = digests[0]
        save(out / "runtime-image-receipt.json", {"requested_image": item["image"],
            "executed_image": fixed_image, "image_id": info["Id"],
            "architecture": info["Architecture"], "os": info["Os"],
            "image_created": info["Created"], "sage_version_required": item["sage_version"],
            "official_versioned_image": True})
        command = ["docker", "run", "--rm", "--name", name, "--network=none",
            "--mount", "type=bind,src=" + str(REPO) + ",dst=/workspace/serre-source,readonly",
            "--workdir", "/workspace/serre-source", "--env", "PYTHONDONTWRITEBYTECODE=1",
            "--env", "PYTHONUNBUFFERED=1"]
        for key in ("GITHUB_ACTIONS", "GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT",
                    "GITHUB_SHA", "GITHUB_REF", "GITHUB_WORKFLOW", "GITHUB_EVENT_NAME"):
            command.extend(["--env", key + "=" + os.environ[key]])
        command.extend(["--entrypoint", "/usr/bin/sage", fixed_image, "-python",
                        "/workspace/serre-source/" + item["core"]])
        with log.open("w", encoding="utf-8") as stream:
            proc = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT,
                                  timeout=item["budget_minutes"] * 60)
            code = proc.returncode
        text = log.read_text(encoding="utf-8")
        print(text, flush=True)
        assert code == 0, "Mathematical core did not complete"
        meta, result, digest = parse_log(text, item)
        save(out / FINAL, result)
        parsed = result
        save(out / "core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": item["core_sha256"], "proof_sha256": item["proof_sha256"],
            "metadata": meta, "canonical_result_sha256": digest,
            "result_file": spec(out / FINAL), "all_identity_checks_passed": True,
            "all_six_FG_outputs_nonzero": result["all_six_FG_outputs_nonzero"],
            "elapsed_seconds": time.monotonic() - started})
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
        if isinstance(exc, subprocess.TimeoutExpired):
            subprocess.run(["docker", "rm", "-f", name], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            code = 124
        elif code == 0:
            code = 1
        if log.exists():
            print(log.read_text(encoding="utf-8"), flush=True)
    complete = code == 0 and parsed is not None
    save(out / "run-receipt.json", {"result": RESULT, "complete": complete,
        "source_commit": source, "workflow_run_id": os.environ["GITHUB_RUN_ID"],
        "workflow_attempt": os.environ["GITHUB_RUN_ATTEMPT"], "process_exit_code": code,
        "error": error, "execution_environment": "public-repository-github-actions",
        "finished_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "elapsed_seconds": time.monotonic() - started,
        "six_case_values_computed": complete,
        "all_six_nonzero_required_for_success": False,
        "primitive_Legendre_same_h_or_main_uniformity_claimed": False})
    manifest(out)
    print(json.dumps({"result": RESULT, "complete": complete, "exit_code": code, "error": error}), flush=True)
    return code if code else (0 if complete else 1)


def verify(item, out):
    guard()
    check_sources(item)
    initial, run, core = (read(out / n) for n in ("public-actions-input.json", "run-receipt.json", "core-receipt.json"))
    assert initial["job"] == item and initial["source_commit"] == run["source_commit"] == os.environ["GITHUB_SHA"]
    assert run["complete"] is True and run["process_exit_code"] == 0 and core["complete"] is True
    assert core["source_sha256"] == item["core_sha256"] and core["proof_sha256"] == item["proof_sha256"]
    meta, result, digest = parse_log((out / "public-actions-run.log").read_text(encoding="utf-8"), item)
    assert result == read(out / FINAL) and core["metadata"] == meta
    assert core["canonical_result_sha256"] == digest and core["result_file"] == spec(out / FINAL)
    reference = read(out / REFERENCE)
    assert reference["manifest"] == spec(out / MANIFEST)
    inventory = read(out / MANIFEST)
    assert inventory["result"] == RESULT
    names = set()
    for row in inventory["files"]:
        name = row["file"]
        assert Path(name).name == name and name not in names
        names.add(name)
        assert row["bytes"] == (out / name).stat().st_size and row["sha256"] == sha(out / name)
        assert row["included_in_git"] is False
    print(json.dumps({"result": RESULT, "complete": True,
        "all_six_FG_outputs_nonzero": result["all_six_FG_outputs_nonzero"],
        "zero_cases": [[c["gaussian_sign"], c["frobenius_j"]] for c in result["cases"] if c["FG"]["zero"]],
        "canonical_result_sha256": digest,
        "same_h_or_main_uniformity_claimed": False}), flush=True)
    return 0


def main():
    guard()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["compute", "verify"])
    args = parser.parse_args()
    request = read(REQUEST)
    assert request["session"] == "serre-public-astra-20261115"
    out = Path(os.environ["RUNNER_TEMP"]) / "serre-global" / RESULT / "output"
    return compute(request["job"], out) if args.mode == "compute" else verify(request["job"], out)


if __name__ == "__main__":
    sys.exit(main())

