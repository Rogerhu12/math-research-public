#!/usr/bin/env python3
"""Read the actual tail startup failure, then prepare one complete lift transfer.

No old solver is rerun by the inspection. The transfer invokes the existing
same-physical-core transfer entry and produces only a nodal initial guess.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "workdir", "source-run", "outdir"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--modes", type=int, required=True)
    args = parser.parse_args()
    work, repo = args.workdir.resolve(), args.repo.resolve()
    rows = []
    names = ("material-lam002-relative-metric.json",
             "material-lam002-full-residual.json",
             "material-corrector-summary.json", "corrector-actual-00/run.json",
             "material-followup-true_dn_correction.log")
    for name in names:
        path = work / name
        if not path.is_file():
            rows.append(dict(file=name, exists=False))
            continue
        data = path.read_bytes()
        row = dict(file=name, sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
        if path.suffix == ".log":
            lines = data.decode(errors="replace").splitlines()
            chosen = [line for line in lines if re.search(
                r"Error|ERR_|not found|Cannot |Traceback|at file:|Module|Import|Syntax", line)]
            row["error_lines"] = [line[:900] for line in chosen[-24:]]
            row["last_text_lines"] = [line[:700] for line in lines[-20:]
                                      if not line.lstrip().startswith(("{", "["))]
        elif name.endswith("run.json"):
            record = json.loads(data)
            row["error"] = record.get("error")
            row["traceback_lines"] = str(record.get("traceback", "")).splitlines()[-16:]
        rows.append(row)
    tail_files = sorted((work / "corrector-actual-00").glob("tail_*.json.gz"))
    result = dict(status="inspected", diagnostics=dict(
        files=rows, actual_tail_response_count=len(tail_files),
        native_directory_exists=(work / "corrector-native-runs/stage-00").is_dir(),
        scope="Read-only original files; absence of a ready line is not a numerical tail rejection."))
    target = work / "material-tail-startup-inspection.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    script = repo / "topics/visible-flex-held-10pct/scripts/resume_m3/prepare_lifted_mode_restart.py"
    command = [sys.executable, "-u", str(script), "--source-run", str(args.source_run),
               "--modes", str(args.modes), "--tail-config", str(work / "inputs/q060-tail.json"),
               "--outdir", str(args.outdir)]
    return subprocess.run(command, cwd=repo, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
