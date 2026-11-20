#!/usr/bin/env python3
"""Read the same projected field and attempt its unchanged true-DN correction.

The two read-only diagnostics use one fixed physical field and mean rule. The
independent corrector uses that field only as an initializer and writes other
directories. No failed metric field is accepted, and no homotopy is advanced.
All numerical programs and their original acceptance tests remain unchanged.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "workdir", "prefix-dir", "core-config"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    repo, work = args.repo.resolve(), args.workdir.resolve()
    prefix = args.prefix_dir.resolve()
    scripts = repo / "topics/visible-flex-held-10pct/scripts"
    m3 = scripts / "resume_m3"
    run_path, physical = prefix / "run.json", prefix / "physical.npz"
    record = json.loads(run_path.read_text())
    if not (record.get("solver_success") and not record.get("error")
            and record.get("raw_return", {}).get("success")):
        raise ValueError("An actual guarded projected solve is required")
    actual_hash = hashlib.sha256(physical.read_bytes()).hexdigest()
    if actual_hash != record.get("physical_sha256"):
        raise ValueError("The stored physical field does not match its actual run")

    metric_out = work / "material-lam002-relative-metric.json"
    residual_out = work / "material-lam002-full-residual.json"
    corrector_out = work / "material-corrector-summary.json"
    summary = work / "material-field-followup.json"
    for path in (metric_out, residual_out, corrector_out, summary):
        if path.exists():
            raise ValueError("Keep previous results; use a fresh work directory: " + str(path))
    common = ["--model-adapter", m3 / "actual_m3_metric_model.py",
              "--model-config", run_path, "--physical", physical,
              "--mean-nodes", "512", "--angular", "512", "1024"]
    jobs = [
        ("relative_metric", [sys.executable, "-u", m3 / "audit_full_relative_metric.py",
                             *common, "--out", metric_out], metric_out),
        ("full_residual", [sys.executable, "-u", scripts / "resume_n4/audit_full_frenet_residual.py",
                           *common, "--metric-loader", m3 / "audit_full_relative_metric.py",
                           "--physical-cutoff", "96", "--batch", "8", "--out", residual_out], residual_out),
        ("true_dn_correction", [sys.executable, "-u", m3 / "correct_projected_material_seed.py",
                                "--repo", repo, "--workdir", work,
                                "--prefix-dir", prefix, "--core-config", args.core_config.resolve(),
                                "--workers", "2"], corrector_out),
    ]
    state = dict(scope=__doc__, status="starting", stages=[],
                 initial_run_sha256=hashlib.sha256(run_path.read_bytes()).hexdigest(),
                 physical_sha256=actual_hash,
                 initial_metric_l1=record.get("prefix_audit", {}).get("metric_l1"),
                 mean_nodes=512, complete_surface=False)
    processes, streams = {}, []

    def save():
        summary.write_text(json.dumps(state, indent=2) + "\n")

    try:
        for name, command, output in jobs:
            log = work / ("material-followup-" + name + ".log")
            stream = log.open("x")
            streams.append(stream)
            argv = list(map(str, command))
            state["stages"].append(dict(name=name, argv=argv, output=str(output),
                                        status="running", returncode=None))
            processes[name] = subprocess.Popen(argv, cwd=repo, stdout=stream,
                                                stderr=subprocess.STDOUT)
        state["status"] = "running"
        save()
        while processes:
            changed = False
            for row in state["stages"]:
                proc = processes.get(row["name"])
                if proc is None:
                    continue
                code = proc.poll()
                if code is not None:
                    row.update(status="finished", returncode=code)
                    del processes[row["name"]]
                    changed = True
            if changed:
                save()
            if processes:
                time.sleep(1)
        state["status"] = "finished"
        save()
        return 0 if all(row["returncode"] == 0 for row in state["stages"]) else 2
    except BaseException as exc:
        state.update(status="orchestration_error", error=repr(exc))
        save()
        for proc in processes.values():
            if proc.poll() is None:
                proc.terminate()
        raise
    finally:
        for stream in streams:
            stream.close()


if __name__ == "__main__":
    sys.exit(main())
