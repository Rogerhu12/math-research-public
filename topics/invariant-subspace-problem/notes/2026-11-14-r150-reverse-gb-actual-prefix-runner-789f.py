#!/usr/bin/env python3
"""The single authorized 50-soft/60-hard second exact reverse prefix."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        while block := f.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dag", type=Path, required=True)
    p.add_argument("--gb-receipt", type=Path, required=True)
    p.add_argument("--coefficients", type=Path, required=True)
    p.add_argument("--coefficient-receipt", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-reverse-gb-actual-prefix-789f.cpp"
    gb = json.loads(a.gb_receipt.read_text())
    coefficient_receipt = json.loads(a.coefficient_receipt.read_text())
    if (gb["status"] != "completed" or coefficient_receipt["status"] != "completed"
            or gb["outputs"]["operations.bin"]["sha256"] != sha(a.dag)
            or coefficient_receipt["outputs"]["gb-coefficients.bin"]["sha256"] != sha(a.coefficients)
            or coefficient_receipt["basisSHA256"] != gb["outputs"]["basis.ssi"]["sha256"]):
        raise ValueError("not the linked complete original DAG and exact GQ=hT")
    binary = a.out / "actual-reverse-prefix"
    receipt = {"format": "r150-exact-reverse-prefix-run-v1", "status": "preparing", "field": 31,
               "dagSHA256": sha(a.dag), "coefficientSHA256": sha(a.coefficients),
               "gbReceiptSHA256": sha(a.gb_receipt), "coefficientReceiptSHA256": sha(a.coefficient_receipt),
               "cppSHA256": sha(source), "runnerSHA256": sha(__file__),
               "readerSHA256": sha(root / "2026-11-14-r150-reverse-gb-bound-789f.cpp"),
               "arithmeticSHA256": sha(root / "2026-11-14-r150-native-normal-form-789f.cpp"),
               "secondsLimit": 60, "softSeconds": 50, "memoryMiBLimit": 512, "outputs": {}}
    receipt_path = a.out / "actual-reverse-receipt.json"
    save = lambda: receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    result = subprocess.run(["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--", "g++", "-O3", "-std=c++17", str(source), "-o", str(binary)], capture_output=True, text=True)
    if result.returncode:
        receipt.update({"status": "compile-failed", "compileOutput": result.stdout + result.stderr})
        save()
        print(receipt["compileOutput"])
        raise SystemExit(1)
    receipt["binarySHA256"] = sha(binary)
    receipt["status"] = "running"
    save()
    prefix = a.out / "reverse"
    command = ["timeout", "--kill-after=10s", "60s", "prlimit", "--as=536870912", "--core=0", "--", str(binary), str(a.dag), str(a.coefficients), str(prefix), "50"]
    before = time.monotonic()
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "actual-reverse.log").open("w") as log:
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
    complete = code == 0 and last and last.get("status") == "original-source-coefficients-complete"
    prefix_only = code == 0 and last and last.get("status") == "original-source-reverse-prefix-only"
    receipt.update({"status": "completed" if complete else "prefix-only" if prefix_only else "failed-or-incomplete",
                    "exitCode": code, "elapsedSeconds": time.monotonic()-before, "nativeStatistics": last})
    for suffix in ["original-source-coefficients.bin", "checkpoint.bin", "replay.json"]:
        path = Path(str(prefix) + "-" + suffix)
        if path.exists():
            receipt["outputs"][suffix] = {"file": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}
    save()
    print(json.dumps(receipt))
    if not (complete or prefix_only):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
