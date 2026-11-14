#!/usr/bin/env python3
"""Run the actual root-parametrix interface audit in immutable public Actions."""
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
        raise ValueError("the root-parametrix interface manifest changed")
    manifest = json.loads(args.manifest.read_text())
    if manifest["public_repository"] != PUBLIC:
        raise ValueError("wrong public scientific repository")
    repo, output = args.repo.resolve(), args.out_dir.resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError("preserve every actual root-parametrix interface outcome")
    output.mkdir(parents=True, exist_ok=True)
    state = dict(kind="actual_public_root_parametrix_interface_audit_execution",
        complete=False, failure=None, public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__), manifest_sha256=args.manifest_sha,
        original_completed_computations_recomputed=0,
        complete_transport_amplitudes_and_numerical_strong_budget_not_claimed=True,
        actual_returncode=None)

    def checkpoint():
        (output/"process.json").write_text(json.dumps(state, indent=2, allow_nan=False)+"\n")

    checkpoint()
    try:
        for entry in manifest["files"]:
            path = repo/entry["path"]
            if (not path.is_file() or sha(path) != entry["sha256"]
                    or path.stat().st_size != entry["bytes"]):
                raise ValueError("a root-parametrix input or source differs: "+entry["path"])
        state["verified_input_files"] = len(manifest["files"])
        source = repo/TOPIC/"scripts/fourfold_codazzi_actual_root_parametrix_interface.py"
        native = output/"actual-root-parametrix-interface.json.gz"
        command = [sys.executable, "-u", str(source)]
        for key, value in manifest["input_paths"].items():
            command += ["--"+key.replace("_", "-"), str(repo/value)]
        command += ["--out", str(native)]
        state.update(command=command, mathematical_source_sha256=sha(source))
        checkpoint()
        started = time.monotonic()
        try:
            with (output/"actual-root-parametrix-interface.stdout.log").open("wb") as stream:
                result = subprocess.run(command, cwd=repo/TOPIC, stdout=stream,
                    stderr=subprocess.STDOUT, timeout=600, check=False,
                    env=dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
                             PYTHONDONTWRITEBYTECODE="1"))
            state["actual_returncode"] = result.returncode
        except subprocess.TimeoutExpired:
            state["actual_returncode"] = 124
            state["timeout_seconds"] = 600
        finally:
            state["mathematical_wall_seconds"] = time.monotonic()-started
        if native.is_file():
            state["native_sha256"] = sha(native)
            state["native_bytes"] = native.stat().st_size
            mathematical = json.loads(gzip.decompress(native.read_bytes()))
            state["mathematical_complete"] = mathematical.get("complete") is True
            state["mathematical_failure"] = mathematical.get("failure")
            state["mathematical_gates"] = mathematical.get("gates", [])
            for key in ("bounds", "source_contract", "original_native_sha256",
                        "original_full_seven_positive_response_columns",
                        "exact_density_input_normalization",
                        "unnormalized_residual_order_sufficient",
                        "normalized_correction_order",
                        "complete_Hminus4over3_Hilbert_Schmidt_series_power",
                        "finite_first_coefficient_algebra_audited",
                        "actual_complete_transport_amplitudes_evaluated",
                        "actual_parametrix_CE_and_Cs_evaluated",
                        "numerical_incoming_inverse_cutoff_certified",
                        "numerical_strong_return_budget_certified",
                        "cutoff97_full_return_inverse_proved",
                        "nonzero_delta_positive_graph_or_root_finite_constant_transferred",
                        "nonlinear_PDE_or_true_parameter_Schur_proved"):
                state[key] = mathematical.get(key)
        state["complete"] = (state["actual_returncode"] == 0 and native.is_file()
                             and state.get("mathematical_complete") is True)
        if state["actual_returncode"]:
            raise SystemExit(state["actual_returncode"])
        if not state["complete"]:
            raise RuntimeError("the actual root-parametrix interface audit did not complete")
    except BaseException as error:
        state["failure"] = dict(type=type(error).__name__, message=str(error))
        raise
    finally:
        checkpoint()
        print(json.dumps(state, ensure_ascii=False, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
