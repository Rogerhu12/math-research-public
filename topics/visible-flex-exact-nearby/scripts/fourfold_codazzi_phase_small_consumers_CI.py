#!/usr/bin/env python3
"""Run the complete small phase-consumer DAG in this public repository's Actions.

Every original169 transport native is reused byte for byte. This pipeline never
reconstructs a scalar germ or a transported reference polynomial. Local earlier
executions retain their original provenance; this run writes fresh CI natives.
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
    p.add_argument("--repo", type=Path, default=Path.cwd())
    p.add_argument("--manifest", type=Path, required=True)
    p.add_argument("--manifest-sha", required=True)
    p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != PUBLIC:
        raise RuntimeError("mathematical replay is authorized here only in the public repository's real Actions job")
    if sha(args.manifest) != args.manifest_sha:
        raise ValueError("the complete pinned DAG manifest changed")
    manifest = json.loads(args.manifest.read_text())
    repo = args.repo.resolve()
    topic = repo/TOPIC
    if args.out_dir.exists() and any(args.out_dir.iterdir()):
        raise FileExistsError("preserve each actual public Actions consumer run")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out = args.out_dir.resolve()
    state = dict(kind="actual_public_Actions_small_phase_consumer_DAG",
        repository=PUBLIC, run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"), workflow_ref=os.environ.get("GITHUB_WORKFLOW_REF"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        manifest_sha256=args.manifest_sha,
        source_sha256=sha(__file__), complete=False, steps=[], reused_transport_germs=169,
        original127_and_public_remaining42_not_recomputed=True,
        previous_local_records_not_relabelled_as_CI=True)

    def checkpoint():
        (out/"process.json").write_text(json.dumps(state, indent=2, allow_nan=False)+"\n")

    for item in manifest["files"]:
        path = repo/item["path"]
        if not path.is_file() or sha(path) != item["sha256"]:
            raise ValueError("a complete pinned input is absent or changed: "+item["path"])
    import numpy, scipy, sympy, mpmath, flint
    versions = dict(python=".".join(map(str, sys.version_info[:3])),
        numpy=numpy.__version__, scipy=scipy.__version__, sympy=sympy.__version__,
        mpmath=mpmath.__version__, python_flint=flint.__version__)
    if versions != manifest["runtime"]:
        raise ValueError("the pinned original scientific runtime differs: "+json.dumps(versions))
    state["runtime"] = versions
    state["verified_inputs"] = len(manifest["files"])
    checkpoint()
    inputs = {key: str(repo/value) for key, value in manifest["input_paths"].items()}
    outputs = {key: str(out/value) for key, value in manifest["output_names"].items()}
    source = lambda name: str(topic/"scripts"/name)
    dirs = ["--transport-dir", inputs["transport_seed_directory"],
            "--transport-dir", inputs["transport_completed_directory"]]
    commands = [
        ("wiener", [source("fourfold_codazzi_phase_Wiener_transport_lift.py"),
            "--transport-cover", inputs["transport_cover"], *dirs,
            "--root-contract", inputs["root_contract"], "--analytic", inputs["analytic"],
            "--out", outputs["wiener"]]),
        ("actual_twist", [source("fourfold_codazzi_phase_actual169_transversality.py"),
            "--wiener-lift", outputs["wiener"], "--correlated", inputs["correlated"],
            "--out", outputs["actual_twist"]]),
        ("proposal48", [source("fourfold_codazzi_phase_terminal_Arb_head_proposal.py"),
            "--wiener-lift", outputs["wiener"], "--post-modes", "48", "--exp-degree", "24",
            "--out", outputs["proposal48"]]),
        ("post48", [source("fourfold_codazzi_phase_terminal_postcomposition.py"),
            "--wiener-lift", outputs["wiener"], "--root-contract", inputs["root_contract"],
            "--post-modes", "48", "--exp-degree", "24", "--proposal-from", outputs["proposal48"],
            "--out", outputs["post48"]]),
        ("K48_row", [source("fourfold_codazzi_phase_K48_parameter_row.py"),
            "--postcomposition", outputs["post48"], "--actual-twist", outputs["actual_twist"],
            "--root-contract", inputs["root_contract"], "--out", outputs["K48_row"]]),
        ("response_contract", [source("fourfold_codazzi_phase_K48_response_error_contract.py"),
            "--parameter-row", outputs["K48_row"], "--out", outputs["response_contract"]]),
        ("target15", [source("fourfold_codazzi_phase_terminal_bounded15_target.py"),
            "--postcomposition", outputs["post48"], "--out", outputs["target15"]]),
        ("sharp_twist", [source("fourfold_codazzi_phase_complete_label_L2_twist.py"),
            "--wiener-lift", outputs["wiener"], "--analytic", inputs["analytic"],
            "--root-contract", inputs["root_contract"], "--correlated", inputs["correlated"],
            "--actual-twist", outputs["actual_twist"], "--K48-row", outputs["K48_row"],
            *dirs, "--out", outputs["sharp_twist"]]),
        ("R31", [source("fourfold_codazzi_phase_explicit_family_R31.py"),
            "--analytic", inputs["analytic"], "--root-contract", inputs["root_contract"],
            "--root-germ", inputs["root_germ"], "--direction", inputs["direction"],
            "--all-delta", inputs["all_delta"], "--correlated", inputs["correlated"],
            "--postcomposition", outputs["post48"], "--target", outputs["target15"],
            "--sharp-twist", outputs["sharp_twist"], "--K48-row", outputs["K48_row"],
            "--out", outputs["R31"]]),
    ]
    environment = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", PYTHONUNBUFFERED="1")
    for name, argv in commands:
        entry = dict(name=name, command=[sys.executable, "-u", *argv],
            mathematical_source_sha256=sha(argv[0]), output=outputs[name])
        state["steps"].append(entry)
        checkpoint()
        started = time.monotonic()
        print(json.dumps(dict(starting=name, source_sha256=entry["mathematical_source_sha256"])), flush=True)
        with (out/"pipeline.stdout.log").open("ab") as stream:
            completed = subprocess.run(entry["command"], cwd=topic, env=environment,
                stdout=stream, stderr=subprocess.STDOUT, timeout=1200)
        entry.update(exit_code=completed.returncode, seconds=time.monotonic()-started)
        if Path(outputs[name]).exists():
            entry["native_sha256"] = sha(outputs[name])
        checkpoint()
        print(json.dumps(entry), flush=True)
        if completed.returncode:
            raise RuntimeError("the actual public consumer failed; all outputs preserved: "+name)
    state["complete"] = True
    state["exact_family_circle_conjugacy_scope_only"] = True
    state["genuine_PDE_branch_full_body_inverse_and_strong_remainder_not_claimed"] = True
    checkpoint()
    print(json.dumps(dict(complete=True, consumers=len(commands), repository=PUBLIC)), flush=True)


if __name__ == "__main__":
    main()
