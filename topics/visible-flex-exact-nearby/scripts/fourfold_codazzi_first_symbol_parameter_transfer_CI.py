#!/usr/bin/env python3
"""Run only the new finite-part parameter-transfer consumer in public Actions."""
from __future__ import annotations

import argparse
import gzip
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
        raise ValueError("the complete parameter-transfer manifest changed")
    manifest = json.loads(args.manifest.read_text())
    if manifest["public_repository"] != PUBLIC:
        raise ValueError("wrong scientific repository")
    repo, output = args.repo.resolve(), args.out_dir.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("preserve every original mathematical result and failure")
    output.mkdir(parents=True, exist_ok=True)
    state = dict(
        kind="actual_public_first_symbol_parameter_transfer_execution",
        complete=False, public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__), manifest_sha256=args.manifest_sha,
        no_original_phase_or_scalar_germs_recomputed=True,
        no_original_finite_part_integrals_or_root_Newton_steps_recomputed=True,
        true_PDE_background_and_full_return_beta_not_claimed=True,
        verified_input_files=0, actual_returncode=None, failure=None)

    def checkpoint():
        (output/"process.json").write_text(
            json.dumps(state, indent=2, allow_nan=False)+"\n")

    checkpoint()
    try:
        for entry in manifest["files"]:
            path = (repo/entry["path"]).resolve()
            if (not path.is_relative_to(repo) or not path.is_file()
                    or path.stat().st_size != entry["bytes"]
                    or sha(path) != entry["sha256"]):
                raise ValueError("a pinned mathematical input or source changed: "+entry["path"])
            state["verified_input_files"] += 1
        source = repo/TOPIC/"scripts/fourfold_codazzi_first_symbol_parameter_transfer.py"
        native = output/"first-symbol-parameter-transfer.json.gz"
        command = [sys.executable, "-u", str(source), "--topic", str(repo/TOPIC)]
        for key, value in manifest["input_paths"].items():
            command += ["--"+key.replace("_", "-"), str(repo/value)]
        command += ["--out", str(native)]
        state.update(command=command, mathematical_source_sha256=sha(source))
        checkpoint()
        started = time.monotonic()
        try:
            with (output/"first-symbol-parameter-transfer.stdout.log").open("wb") as stream:
                result = subprocess.run(
                    command, cwd=repo/TOPIC, stdout=stream, stderr=subprocess.STDOUT,
                    timeout=1800, check=False,
                    env=dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
                             PYTHONDONTWRITEBYTECODE="1"))
            state["actual_returncode"] = result.returncode
        except subprocess.TimeoutExpired:
            state["actual_returncode"] = 124
            state["timeout_seconds"] = 1800
        state["mathematical_wall_seconds"] = time.monotonic()-started
        if native.is_file():
            state["native_sha256"] = sha(native)
            mathematical = json.loads(gzip.decompress(native.read_bytes()))
            state["mathematical_complete"] = mathematical.get("complete") is True
            state["transfer_enclosure_complete"] = mathematical.get("transfer_enclosure_complete") is True
            state["mathematical_gates"] = mathematical.get("gates", [])
            state["mathematical_failure"] = mathematical.get("failure")
            for key in (
                "complete_strict_parameter_derivative",
                "complete_root_parameter_derivative",
                "complete_total_parameter_derivative",
                "actual_selected_R31_parameter_abs_upper",
                "selected_parameter_complete_transfer_fee",
                "complete_selected_parameter_finite_part",
                "minus_quarter_of_selected_finite_part_with_no_full_return_identification"):
                if key in mathematical:
                    state[key] = mathematical[key]
        state["complete"] = (
            state["actual_returncode"] == 0 and native.is_file()
            and state.get("mathematical_complete") is True)
        checkpoint()
        print(json.dumps(state, ensure_ascii=False), flush=True)
        if state["actual_returncode"]:
            raise SystemExit(state["actual_returncode"])
        if not state["complete"]:
            raise RuntimeError("the complete finite-part parameter transfer did not finish")
    except Exception as exc:
        state["failure"] = dict(type=type(exc).__name__, message=str(exc))
        checkpoint()
        raise


if __name__ == "__main__":
    main()
