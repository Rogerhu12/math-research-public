#!/usr/bin/env python3
"""Run and audit the fixed seven-product consumer; retain raw files for one day."""
import os

if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Only the public repository GitHub Actions may run this consumer.")

import hashlib
import json
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[3]
REQUEST = REPO / "topics/serre-uniformity/notes/sigma-reused-p47-critical-product-request.json"
RESULT = "reused-R702-p47-seven-critical-products"
OUT = Path(os.environ["RUNNER_TEMP"]) / "serre-global" / RESULT / "output"
FINAL = "seven-critical-products.json"
MANIFEST = "manifest.json"


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save(path, value):
    Path(path).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def blob(path):
    raw = Path(path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def spec(path):
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def check(job):
    assert job["result"] == RESULT and job["prime"] == 47
    assert job["scope"] == "seven_products_from_existing_A_only"
    assert REPO / job["wrapper"] == Path(__file__).resolve()
    for key in ("core", "wrapper", "workflow", "upstream_data", "upstream_formula"):
        relative = Path(job[key])
        assert not relative.is_absolute() and ".." not in relative.parts
        assert blob(REPO / relative) == job[key + "_git_blob"]
    actual_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
    assert actual_head == os.environ["GITHUB_SHA"]


def parse(job):
    output = read(OUT / FINAL)
    assert output["result"] == RESULT and output["prime"] == 47
    assert output["source_sha256"] == sha(REPO / job["core"])
    for key, env in (("source_commit", "GITHUB_SHA"), ("run_id", "GITHUB_RUN_ID"),
                     ("run_attempt", "GITHUB_RUN_ATTEMPT"), ("repository", "GITHUB_REPOSITORY")):
        assert str(output[key]) == os.environ[env]
    assert output["upstream_git_blob"] == job["upstream_data_git_blob"]
    assert output["upstream_arithmetic_sha256"] == job["upstream_arithmetic_sha256"]
    assert output["new_A_or_f_or_g_series_generated"] is False
    assert output["new_primes"] == []
    assert output["primitive_or_Legendre_weights_computed"] is False
    assert output["all_inert_primes_nonzero_claimed"] is False
    assert len(output["products"]) == 7
    assert all(row["factorial_formula_checked"] is True for row in output["products"])
    digest = hashlib.sha256(canonical(output)).hexdigest()
    marks = [line for line in (OUT / "run.log").read_text(encoding="utf-8").splitlines()
             if line.startswith("RESULT_SHA256=")]
    assert marks == ["RESULT_SHA256=" + digest]
    return output, digest


def compute(job):
    OUT.mkdir(parents=True, exist_ok=True)
    check(job)
    error, code, result_digest = None, 1, None
    try:
        proc = subprocess.run([sys.executable, str(REPO / job["core"]), str(OUT / FINAL)],
            cwd=REPO, capture_output=True, text=True, timeout=60)
        code = proc.returncode
        (OUT / "run.log").write_text(proc.stdout + proc.stderr, encoding="utf-8")
        print(proc.stdout + proc.stderr, end="", flush=True)
        assert code == 0, "The fixed consumer failed"
        _, result_digest = parse(job)
    except Exception as exc:
        error = type(exc).__name__ + ": " + str(exc)
        if code == 0:
            code = 1
    save(OUT / "receipt.json", {"result": RESULT, "complete": code == 0 and error is None,
        "process_exit_code": code, "error": error, "source_commit": os.environ["GITHUB_SHA"],
        "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": os.environ["GITHUB_RUN_ATTEMPT"],
        "request_sha256": sha(REQUEST), "core_sha256": sha(REPO / job["core"]),
        "wrapper_sha256": sha(__file__), "canonical_result_sha256": result_digest,
        "job": job, "raw_output_in_git_or_release": False})
    save(OUT / MANIFEST, {"result": RESULT, "retention_days": 1,
        "files": [spec(path) for path in sorted(OUT.iterdir()) if path.is_file() and path.name != MANIFEST]})
    print("MANIFEST_SHA256=" + sha(OUT / MANIFEST), flush=True)
    return code


def verify(job):
    check(job)
    receipt = read(OUT / "receipt.json")
    assert receipt["complete"] is True and receipt["process_exit_code"] == 0
    assert receipt["job"] == job and receipt["request_sha256"] == sha(REQUEST)
    output, digest = parse(job)
    assert receipt["canonical_result_sha256"] == digest
    manifest = read(OUT / MANIFEST)
    assert manifest["result"] == RESULT and manifest["retention_days"] == 1
    names = set()
    for row in manifest["files"]:
        name = row["file"]
        assert Path(name).name == name and name not in names
        names.add(name)
        assert row == spec(OUT / name)
    assert names == {path.name for path in OUT.iterdir() if path.is_file() and path.name != MANIFEST}
    print(json.dumps({"result": RESULT, "complete": True,
        "critical_products": [row["f_i_g_j"] for row in output["products"]],
        "alternating_critical_convolution": output["alternating_critical_convolution"],
        "alternating_critical_convolution_nonzero": output["alternating_critical_convolution_nonzero"],
        "canonical_result_sha256": digest, "manifest_sha256": sha(OUT / MANIFEST),
        "new_prime_or_all_prime_claim": False}, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    job = read(REQUEST)["job"]
    assert len(sys.argv) == 2 and sys.argv[1] in ("compute", "verify")
    sys.exit(compute(job) if sys.argv[1] == "compute" else verify(job))
