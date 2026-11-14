#!/usr/bin/env python3
"""Rebuild frozen R259 using only published repository inputs."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script-dir", type=Path, required=True)
    ap.add_argument("--work-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    scripts = args.script_dir.resolve()
    data = scripts / "data"
    work = args.work_dir.resolve()
    recovery, qc = work / "recovery-inputs", work / "qc-inputs"

    def link(source, target):
        source = source.resolve(strict=True)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() or target.is_symlink():
            assert target.resolve(strict=True) == source, target
        else:
            target.symlink_to(source, target_is_directory=source.is_dir())

    for name in ["p41_rational_SS_second_kind_integrals47_complete.json.gz",
                 "p41_SS_second_kind_rhs47.json.gz"]:
        link(data/name, recovery/name)
    link(data/"SS_second_kind_rhs47", recovery/"SS-second-kind-rhs")
    name = "ORD_j05_second_kind_complete47.json.gz"
    link(data/name, qc/"ordinary-second-kind"/name)
    for name in ["ORD_j05_actual_principal_function47.json.gz",
                 "ORD_j05_actual_T2_support47.json.gz",
                 "ORD_j05_actual_F2_first_variable_norm47.json.gz",
                 "p41_canonical_restriction47_candidate1_raw.json.gz"]:
        link(data/name, qc/name)
    args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        sys.executable, str(scripts/"p41_ordinary_F2_connection47.py"),
        "--script-dir", str(scripts), "--recovery-dir", str(recovery),
        "--qc-dir", str(qc), "--work-dir", str(work/"connection"),
        "--output", str(args.output.resolve()),
    ], check=True)


if __name__ == "__main__":
    main()
