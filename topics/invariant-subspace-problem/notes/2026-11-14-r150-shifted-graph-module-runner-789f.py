#!/usr/bin/env python3
"""Single-copy six-shift graph module; bounded prefix or explicit full run."""
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
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--mapping", type=Path, required=True)
    p.add_argument("--nf-receipt", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--seconds", type=int, default=60)
    p.add_argument("--soft-seconds", type=int, default=50)
    p.add_argument("--memory-mib", type=int, default=512)
    a = p.parse_args()
    if a.seconds < 10 or a.soft_seconds < 1 or a.soft_seconds > a.seconds-5 or a.memory_mib <= 0:
        raise ValueError("explicit bounded limits required")
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-shifted-graph-module-789f.cpp"
    nf = json.loads(a.nf_receipt.read_text())
    mapping = json.loads(a.mapping.read_text())
    if (nf["status"] != "completed" or not nf["allSources"] or nf["sourceCount"] != 2195
            or nf["targetCount"] != 9 or nf["outputs"]["normal-forms.bin"]["sha256"] != sha(a.input)
            or mapping["field"] != 31 or len(mapping["sources"]) != 2195
            or len(mapping["components"]) != 1034 or mapping["targets"] != list(range(2, 11))):
        raise ValueError("not the complete original source-faithful NF input")
    binary = a.out / "shifted-graph-module"
    receipt = {"format": "r150-shifted-source-graph-run-v1", "status": "preparing", "field": 31,
               "inputSHA256": sha(a.input), "mappingSHA256": sha(a.mapping), "nfReceiptSHA256": sha(a.nf_receipt),
               "cppSHA256": sha(source), "runnerSHA256": sha(__file__),
               "arithmeticSHA256": sha(root / "2026-11-14-r150-native-normal-form-789f.cpp"),
               "arithmeticHeaderSHA256": sha(root / "2026-11-14-r150-f31-bitplane-789f.hpp"),
               "sourceShiftRule": "degree(R_j)-64", "outputShift": 0, "maximumWeightedRowDegree": 45,
               "secondsLimit": a.seconds, "softSeconds": a.soft_seconds, "memoryMiBLimit": a.memory_mib,
               "storage": "one copy per row; scalar 3/5 use two additions", "outputs": {}}
    receipt_path = a.out / "shifted-graph-receipt.json"
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
    prefix = a.out / "graph"
    command = ["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit", f"--as={a.memory_mib*1024*1024}", "--core=0", "--", str(binary), str(a.input), str(prefix), str(a.soft_seconds)]
    before = time.monotonic()
    child = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "shifted-graph.log").open("w") as log:
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
    complete = code == 0 and last and last.get("status") == "complete-graph-elimination-basis"
    full_non_elimination = code == 0 and last and last.get("status") == "complete-graph-basis-elimination-condition-failed"
    prefix_only = code == 0 and last and last.get("status") == "shifted-graph-prefix-only"
    receipt.update({"status": "completed" if complete else "full-graph-without-elimination" if full_non_elimination else "prefix-only" if prefix_only else "failed-or-incomplete",
                    "exitCode": code, "elapsedSeconds": time.monotonic()-before, "nativeStatistics": last})
    for suffix in ["basis.bin", "metadata.json"]:
        path = Path(str(prefix) + "-" + suffix)
        if path.exists():
            receipt["outputs"][suffix] = {"file": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}
    save()
    print(json.dumps(receipt))
    if not (complete or prefix_only or full_non_elimination):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
