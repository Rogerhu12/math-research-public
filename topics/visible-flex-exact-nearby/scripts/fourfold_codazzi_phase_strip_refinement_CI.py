#!/usr/bin/env python3
"""Consume the completed public R31 once to refine the physical strip.

No original transport, postcomposition, or R31 constant is recomputed here.
All successful and unsuccessful loss trials remain in the fresh native.
"""
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
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--manifest-sha", required=True)
    p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != PUBLIC:
        raise RuntimeError("this mathematical consumer requires this public repository's actual Actions job")
    if sha(args.manifest) != args.manifest_sha:
        raise ValueError("the separately pinned complete consumer manifest changed")
    manifest = json.loads(args.manifest.read_text())
    if manifest["public_repository"] != PUBLIC:
        raise ValueError("wrong public repository")
    repo, out = args.repo.resolve(), args.out_dir.resolve()
    if out.exists() and any(out.iterdir()):
        raise FileExistsError("preserve each actual original process and native")
    out.mkdir(parents=True, exist_ok=True)
    state = dict(kind="actual_public_completed_R31_strip_refinement_execution",
        repository=PUBLIC, run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__), manifest_sha256=args.manifest_sha,
        complete=False, actual_returncode=None,
        original_transport_postcomposition_and_R31_not_recomputed=True,
        true_PDE_branch_full_response_inverse_and_beta_not_claimed=True)

    def checkpoint():
        (out/"process.json").write_text(json.dumps(state, indent=2, allow_nan=False)+"\n")

    checkpoint()
    for item in manifest["files"]:
        path = repo/item["path"]
        if not path.is_file() or sha(path) != item["sha256"]:
            raise ValueError("a complete original source or native is missing or changed: "+item["path"])
    import numpy, scipy, sympy, mpmath, flint
    versions = dict(python=".".join(map(str, sys.version_info[:3])),
        numpy=numpy.__version__, scipy=scipy.__version__, sympy=sympy.__version__,
        mpmath=mpmath.__version__, python_flint=flint.__version__)
    if versions != manifest["runtime"]:
        raise ValueError("the pinned mathematical runtime changed: "+json.dumps(versions))
    state["runtime"] = versions
    state["verified_inputs"] = len(manifest["files"])
    source = repo/TOPIC/"scripts/fourfold_codazzi_phase_R31_strip_refinement.py"
    native = out/"R31-strip-refinement.json.gz"
    inputs = manifest["input_paths"]
    command = [sys.executable, "-u", str(source),
        "--R31", str(repo/inputs["R31"]),
        "--postcomposition", str(repo/inputs["postcomposition"]),
        "--root-contract", str(repo/inputs["root_contract"]),
        "--out", str(native)]
    state["command"] = command
    state["mathematical_source_sha256"] = sha(source)
    checkpoint()
    started = time.monotonic()
    with (out/"refinement.stdout.log").open("wb") as stream:
        child = subprocess.run(command, cwd=repo/TOPIC, stdout=stream,
            stderr=subprocess.STDOUT, timeout=300, check=False)
    state["actual_returncode"] = child.returncode
    state["mathematical_wall_seconds"] = time.monotonic()-started
    if native.is_file():
        state["native_sha256"] = sha(native)
    state["complete"] = child.returncode == 0
    checkpoint()
    print(json.dumps(state, ensure_ascii=False), flush=True)
    if child.returncode:
        raise SystemExit(child.returncode)


if __name__ == "__main__":
    main()
