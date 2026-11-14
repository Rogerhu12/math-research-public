#!/usr/bin/env python3
"""One bounded full graph attempt followed immediately by the nine-target lift.

The requested compute budget applies to the graph stage; the target lift has
its own explicit 60-second cap. Large graph data stay in --work.
Only small receipts, dictionaries, logs, and gzip target coefficients go --out.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
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
    p.add_argument("--ann-receipt", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--seconds", type=int, default=1800)
    p.add_argument("--memory-mib", type=int, default=4096)
    a = p.parse_args()
    if a.seconds < 240 or a.memory_mib <= 0:
        raise ValueError("full pipeline needs an explicit budget of at least 240 seconds")
    a.work.mkdir(parents=True, exist_ok=True)
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    graph_runner = root / "2026-11-14-r150-shifted-graph-module-runner-789f.py"
    lift_runner = root / "2026-11-14-r150-shifted-graph-target-lift-runner-789f.py"
    graph_work = a.work / "graph"
    graph_hard = a.seconds
    graph_soft = graph_hard-60
    before = time.monotonic()
    receipt = {"format": "r150-full-shifted-graph-and-original-target-lift-v1", "field": 31,
               "status": "graph-running", "requestedGraphSeconds": a.seconds, "memoryMiBLimit": a.memory_mib,
               "graphHardSeconds": graph_hard, "graphSoftSeconds": graph_soft, "targetLiftSeconds": 60,
               "inputSHA256": sha(a.input), "mappingSHA256": sha(a.mapping),
               "nfReceiptSHA256": sha(a.nf_receipt), "annReceiptSHA256": sha(a.ann_receipt),
               "sourceSHA256": sha(__file__), "graphRunnerSHA256": sha(graph_runner),
               "liftRunnerSHA256": sha(lift_runner), "outputs": {}}
    path = a.out / "full-lift-receipt.json"
    save = lambda: path.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    command = ["python3", str(graph_runner), "--input", str(a.input), "--mapping", str(a.mapping),
               "--nf-receipt", str(a.nf_receipt), "--out", str(graph_work), "--seconds", str(graph_hard),
               "--soft-seconds", str(graph_soft), "--memory-mib", str(a.memory_mib)]
    code = subprocess.call(command)
    graph_receipt_path = graph_work / "shifted-graph-receipt.json"
    graph_receipt = json.loads(graph_receipt_path.read_text()) if graph_receipt_path.exists() else {}
    for source, name in [(graph_receipt_path, "graph-receipt.json"), (graph_work / "graph-metadata.json", "graph-metadata.json"), (graph_work / "shifted-graph.log", "graph.log")]:
        if source.exists():
            target = a.out / name
            shutil.copyfile(source, target)
            receipt["outputs"][name] = {"file": str(target), "bytes": target.stat().st_size, "sha256": sha(target)}
    receipt["graphStatus"] = graph_receipt.get("status", "missing")
    if code or graph_receipt.get("status") != "completed":
        receipt.update({"status": "graph-incomplete-or-not-eliminating", "graphExitCode": code,
                        "elapsedSeconds": time.monotonic()-before})
        save()
        raise SystemExit(1)
    receipt["status"] = "original-target-lift-running"
    save()
    code = subprocess.call(["python3", str(lift_runner), "--graph", str(graph_work / "graph-basis.bin"),
                            "--graph-receipt", str(graph_receipt_path), "--input", str(a.input),
                            "--nf-receipt", str(a.nf_receipt), "--ann-receipt", str(a.ann_receipt),
                            "--work", str(a.work / "target-lift"), "--out", str(a.out / "target-lift"),
                            "--seconds", "60", "--memory-mib", str(a.memory_mib)])
    target_receipt_path = a.out / "target-lift" / "target-lift-receipt.json"
    target_receipt = json.loads(target_receipt_path.read_text()) if target_receipt_path.exists() else {}
    complete = code == 0 and target_receipt.get("status") == "completed"
    receipt.update({"status": "completed" if complete else "graph-complete-target-lift-incomplete",
                    "targetLiftStatus": target_receipt.get("status", "missing"), "targetLiftExitCode": code,
                    "elapsedSeconds": time.monotonic()-before,
                    "sourceIdentity": "Completion requires all 2195 graph columns, the exact 1021/1174 elimination split, zero outputs of all 1174 kernel rows, all nine original targets, and the coefficientwise original R*C=h31*T identity with every source degree bound. Characteristic-zero lifting and constant-prebasis recovery remain separate."})
    if target_receipt_path.exists():
        receipt["outputs"]["target-lift-receipt.json"] = {"file": str(target_receipt_path), "sha256": sha(target_receipt_path)}
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
