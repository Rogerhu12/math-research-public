#!/usr/bin/env python3
"""Bounded whole-torsion state construction from an already COMPLETE F31 GB."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            value.update(chunk)
    return value.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--basis", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--gb-receipt", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--seconds", type=int, default=60)
    parser.add_argument("--memory-mib", type=int, default=512)
    args = parser.parse_args()
    if args.seconds < 1 or args.memory_mib <= 0:
        raise ValueError("explicit positive bounds required")
    source = Path(__file__).with_name("2026-11-14-r150-native-torsion-state-789f.cpp")
    arithmetic = source.with_name("2026-11-14-r150-native-normal-form-789f.cpp")
    gb = json.loads(args.gb_receipt.read_text())
    meta = json.loads(args.metadata.read_text())
    if (gb["status"] != "completed" or gb["nativeStatistics"]["processedSources"] != 2195
            or gb["nativeStatistics"]["basisRows"] != 1021
            or gb["nativeStatistics"]["maximumBasisDegree"] != 8
            or gb["outputs"]["basis.ssi"]["sha256"] != sha(args.basis)
            or gb["outputs"]["basis-metadata.json"]["sha256"] != sha(args.metadata)
            or not meta["complete"] or meta["processedSources"] != 2195
            or meta["moduleOrder"] != "dp,c" or meta["field"] != 31
            or len(meta["basis"]) != 1021 or meta["targets"] != list(range(2, 11))):
        raise ValueError("input is not the complete original F31 basis")
    args.out.mkdir(parents=True, exist_ok=True)
    args.out = args.out.resolve()
    receipt = {"format": "r150-whole-torsion-run-v1", "field": 31, "status": "preparing",
               "basisSHA256": sha(args.basis), "metadataSHA256": sha(args.metadata),
               "gbReceiptSHA256": sha(args.gb_receipt), "cppSHA256": sha(source),
               "arithmeticSHA256": sha(arithmetic), "runnerSHA256": sha(__file__),
               "secondsLimit": args.seconds, "memoryMiBLimit": args.memory_mib, "outputs": {}}
    receipt_file = args.out / "torsion-state-receipt.json"
    save = lambda: receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = args.out / "native-torsion-state"
    command = ["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--",
               "g++", "-O3", "-std=c++17", str(source), "-o", str(binary)]
    compile_result = subprocess.run(command, capture_output=True, text=True)
    if compile_result.returncode:
        receipt.update({"status": "compile-failed", "compileExit": compile_result.returncode,
                        "compileOutput": compile_result.stdout + compile_result.stderr})
        save()
        print(receipt["compileOutput"])
        raise SystemExit(1)
    receipt["binarySHA256"] = sha(binary)
    receipt["status"] = "running"
    save()
    prefix = args.out / "torsion"
    command = ["timeout", "--kill-after=10s", f"{args.seconds}s", "prlimit",
               f"--as={args.memory_mib * 1024 * 1024}", "--core=0", "--",
               str(binary), str(args.basis.resolve()), str(prefix)]
    before = time.monotonic()
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (args.out / "torsion-state.log").open("w") as log:
        for line in child.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
            try:
                event = json.loads(line)
                events.append(event)
                receipt["lastProgress"] = event
                save()
            except ValueError:
                pass
    code = child.wait()
    last = events[-1] if events else None
    completed = code == 0 and last and last.get("status") == "whole-torsion-state-complete"
    receipt.update({"status": "completed" if completed else "failed-or-incomplete", "exitCode": code,
                    "elapsedSeconds": time.monotonic() - before, "nativeStatistics": last})
    for suffix in ["normal-operations.bin", "state.bin", "state.json"]:
        path = Path(str(prefix) + "-" + suffix)
        if path.exists():
            receipt["outputs"][suffix] = {"file": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}
    save()
    print(json.dumps(receipt))
    if not completed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
