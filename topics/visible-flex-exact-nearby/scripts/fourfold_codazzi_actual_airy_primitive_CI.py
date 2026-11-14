#!/usr/bin/env python3
"""Run the actual old-curve Airy primitive budget from immutable public Actions inputs."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


PUBLIC = "Rogerhu12/math-research-public"
TOPIC = Path("topics/visible-flex-exact-nearby")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC):
        raise RuntimeError("the actual public repository Actions environment is required")
    if sha(args.manifest) != args.manifest_sha:
        raise ValueError("the full actual Airy primitive manifest changed")
    manifest = json.loads(args.manifest.read_text())
    if manifest["public_repository"] != PUBLIC:
        raise ValueError("wrong public scientific repository")
    repo, output = args.repo.resolve(), args.out_dir.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("preserve every actual Airy-primitive process and result")
    output.mkdir(parents=True, exist_ok=True)
    state = dict(kind="actual_public_actual_old_curve_Airy_primitive_execution",
        complete=False, public_repository=PUBLIC, run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__), manifest_sha256=args.manifest_sha,
        no_full_transport_or_full_response_recomputed=True,
        genuine_PDE_branch_and_full_root_return_not_claimed=True,
        actual_returncode=None)

    def checkpoint():
        (output/"process.json").write_text(json.dumps(state, indent=2, allow_nan=False)+"\n")

    checkpoint()
    for entry in manifest["files"]:
        path = repo/entry["path"]
        if not path.is_file() or sha(path) != entry["sha256"]:
            raise ValueError("an original Airy-primitive input or source differs: "+entry["path"])
    state["verified_input_files"] = len(manifest["files"])
    source = repo/TOPIC/"scripts/fourfold_codazzi_actual_airy_primitive_budget.py"
    native = output/"actual-airy-primitive.json.gz"
    command = [sys.executable, "-u", str(source)]
    for key, value in manifest["input_paths"].items():
        command += ["--"+key.replace("_", "-"), str(repo/value)]
    command += ["--out", str(native)]
    state.update(command=command, mathematical_source_sha256=sha(source))
    checkpoint()
    started = time.monotonic()
    try:
        with (output/"actual-airy-primitive.stdout.log").open("wb") as stream:
            result = subprocess.run(command, cwd=repo/TOPIC, stdout=stream,
                stderr=subprocess.STDOUT, timeout=600, check=False,
                env=dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
                         PYTHONDONTWRITEBYTECODE="1"))
        state["actual_returncode"] = result.returncode
    except subprocess.TimeoutExpired:
        state["actual_returncode"] = 124
        state["timeout_seconds"] = 600
    state["mathematical_wall_seconds"] = time.monotonic()-started
    if native.is_file():
        state["native_sha256"] = sha(native)
        import gzip
        mathematical = json.loads(gzip.decompress(native.read_bytes()))
        state["mathematical_complete"] = mathematical.get("complete") is True
        state["mathematical_gates"] = mathematical.get("gates", [])
        state["amplitude_domains"] = mathematical.get("amplitude_domains", {})
        state["bounds"] = mathematical.get("bounds", {})
        state["finite_amplitude_coefficient_ledger"] = mathematical.get("finite_amplitude_coefficient_ledger", [])
        state["actual_root_finite_reflection_constant_not_identified"] = mathematical.get("actual_root_finite_reflection_constant_not_identified")
    state["complete"] = (state["actual_returncode"] == 0 and native.is_file()
                         and state.get("mathematical_complete") is True)
    checkpoint()
    print(json.dumps(state, ensure_ascii=False), flush=True)
    if state["actual_returncode"]:
        raise SystemExit(state["actual_returncode"])
    if not state["complete"]:
        raise RuntimeError("the actual full old-curve Airy primitive budget did not complete")


if __name__ == "__main__":
    main()
