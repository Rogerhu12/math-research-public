#!/usr/bin/env python3
"""Bounded exact nine-target coefficient certificate in the completed GB."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--state-dir", type=Path, required=True)
    p.add_argument("--basis-dir", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--seconds", type=int, default=60)
    p.add_argument("--memory-mib", type=int, default=512)
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).with_name("2026-11-14-r150-target-gb-coefficients-789f.cpp")
    state = a.state_dir / "torsion-state.bin"
    operations = a.state_dir / "torsion-normal-operations.bin"
    basis = a.basis_dir / "gb-basis.ssi"
    state_receipt = json.loads((a.state_dir / "torsion-state-receipt.json").read_text())
    gb_receipt = json.loads((a.basis_dir / "native-gb-receipt.json").read_text())
    ann = json.loads((a.state_dir / "target-minimum-annihilators.json").read_text())
    if (state_receipt["status"] != "completed" or gb_receipt["status"] != "completed"
            or ann["status"] != "completed" or ann["commonMinimum"]["degree"] != 24
            or state_receipt["outputs"]["state.bin"]["sha256"] != sha(state)
            or state_receipt["outputs"]["normal-operations.bin"]["sha256"] != sha(operations)
            or gb_receipt["outputs"]["basis.ssi"]["sha256"] != sha(basis)
            or ann["stateSHA256"] != sha(state)):
        raise ValueError("not the complete linked original inputs")
    hfile = a.out / "common-h31.txt"
    hfile.write_text(" ".join(map(str, ann["commonMinimum"]["coefficientsAscending"])) + "\n")
    binary = a.out / "target-gb-coefficients"
    receipt = {"format": "r150-target-gb-coefficients-run-v1", "status": "preparing", "field": 31,
               "stateSHA256": sha(state), "normalOperationsSHA256": sha(operations), "basisSHA256": sha(basis),
               "annReceiptSHA256": sha(a.state_dir / "target-minimum-annihilators.json"),
               "cppSHA256": sha(source), "runnerSHA256": sha(__file__),
               "secondsLimit": a.seconds, "memoryMiBLimit": a.memory_mib, "outputs": {}}
    receipt_file = a.out / "gb-coefficients-receipt.json"
    save = lambda: receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    compile_result = subprocess.run(["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--", "g++", "-O3", "-std=c++17", str(source), "-o", str(binary)], capture_output=True, text=True)
    if compile_result.returncode:
        receipt.update({"status": "compile-failed", "compileOutput": compile_result.stdout + compile_result.stderr})
        save()
        print(receipt["compileOutput"])
        raise SystemExit(1)
    receipt["binarySHA256"] = sha(binary)
    receipt["status"] = "running"
    save()
    before = time.monotonic()
    prefix = a.out / "target"
    result = subprocess.run(["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit", f"--as={a.memory_mib*1024*1024}", "--core=0", "--", str(binary), str(state), str(operations), str(basis), str(hfile), str(prefix)], capture_output=True, text=True)
    (a.out / "gb-coefficients.log").write_text(result.stdout + result.stderr)
    print(result.stdout + result.stderr)
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except ValueError:
            pass
    last = events[-1] if events else None
    complete = result.returncode == 0 and last and last.get("status") == "all-nine-gb-coefficients-complete"
    receipt.update({"status": "completed" if complete else "failed-or-incomplete", "exitCode": result.returncode,
                    "elapsedSeconds": time.monotonic()-before, "nativeStatistics": last})
    for suffix in ["gb-coefficients.bin", "gb-coefficients.json"]:
        file = Path(str(prefix) + "-" + suffix)
        if file.exists():
            receipt["outputs"][suffix] = {"file": str(file), "bytes": file.stat().st_size, "sha256": sha(file)}
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
