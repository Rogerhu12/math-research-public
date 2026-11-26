#!/usr/bin/env python3
"""Recreate two R211 seed steps, then continue the quartic metric objective.

Recovery text after executor loss on 2026-11-26. New source identity.
Arrays/checkpoints are reproducible local outputs and must not be published.
No Git, network, credentials, or publication is performed by this script.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=60)
    parser.add_argument("--tau", type=float, default=0.05)
    parser.add_argument("--heap-mb", type=int, default=64)
    parser.add_argument("--node", default="node")
    args = parser.parse_args()
    if args.steps < 1 or args.tau <= 0 or args.heap_mb < 64:
        parser.error("positive steps/tau and heap >=64 MB required")
    topic = Path(__file__).resolve().parent.parent
    runner = topic / "scripts/6a65-run-metric-branch-recovered-20261126.cjs"
    candidate = topic / "notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json"
    initial = topic / "notes/2026-11-13-fd2d-R211-full-half-01-initial.json"
    out = args.out_dir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    manifest = {
        "schema": "6a65-cold-r211-quartic-metric-recovered-replay-v1",
        "candidate_sha256": digest(candidate),
        "initial_sha256": digest(initial),
        "runner_sha256": digest(runner),
        "metric_source_sha256": digest(topic / "scripts/6a65-quartic-metric-recovered-20261126.cjs"),
        "bounded_provider_sha256": digest(topic / "scripts/6a65-low-memory-r211-provider-recovered-20261126.cjs"),
        "replay_script_sha256": digest(Path(__file__)),
        "node_version": subprocess.check_output([args.node, "--version"], text=True).strip(),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"),
        "tau": args.tau, "requested_quartic_steps": args.steps,
        "replayed_seed_steps_not_new_research": 2,
        "source_identity": "recovered-20261126; old execution hashes not inherited",
        "stages": [], "states": [],
        "continuous_certificate": False, "strong_target_complete": False,
    }
    manifest_path = out / "run-manifest.json"

    def save() -> None:
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    def stage(label: str, source: Path, tau: str, count: int) -> Path:
        prefix = out / label
        command = [args.node, f"--max-old-space-size={args.heap_mb}",
                   "--max-semi-space-size=4", "--expose-gc", str(runner),
                   str(candidate), str(source), str(prefix), tau, str(count), "run"]
        start = time.monotonic()
        with (out / f"{label}.log").open("w") as log:
            process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, text=True)
            assert process.stdout is not None
            for line in process.stdout:
                print(line, end="", flush=True)
                log.write(line)
                log.flush()
            code = process.wait()
        manifest["stages"].append({"label": label, "command": command,
                                   "exit_code": code,
                                   "wall_seconds": time.monotonic() - start})
        states = sorted(out.glob(f"{label}-[0-9]*.json"),
                        key=lambda p: int(p.stem.rsplit("-", 1)[1]))
        for file in states:
            state = json.loads(file.read_text())
            value = state.get("evaluation") or state["baseline"]
            manifest["states"].append({
                "stage": label, "file": file.name, "sha256": digest(file),
                "accepted": state["accepted"],
                "branch_accepted_steps": state["metricBranchAcceptedSteps"],
                "squared_norm": value["squaredNorm"],
                "sample_max_metric": value["maxRelativeMetric"],
                "sample_max_curvature": value["curvature"]["maxCurvature"],
                "geometry_violations": value["geometry"]["maximumViolations"],
            })
        save()
        if code != 0:
            raise SystemExit(f"{label} exited {code}; completed checkpoints retained locally")
        if len(states) != count or not all(json.loads(p.read_text())["accepted"] for p in states):
            raise SystemExit(f"{label} stopped before all requested accepted steps; state retained")
        return states[-1]

    save()
    seed = stage("r211-seed", initial, "original", 2)
    final = stage("quartic", seed, str(args.tau), args.steps)
    manifest["final_state"] = final.name
    manifest["final_state_sha256"] = digest(final)
    manifest["completed"] = True
    save()
    print(json.dumps({"event": "replay_complete", "manifest": str(manifest_path),
                      "manifest_sha256": digest(manifest_path),
                      "final": manifest["states"][-1]}), flush=True)


if __name__ == "__main__":
    main()

