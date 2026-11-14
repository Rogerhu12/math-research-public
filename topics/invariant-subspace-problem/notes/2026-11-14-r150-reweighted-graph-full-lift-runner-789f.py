#!/usr/bin/env python3
"""Single fixed T64 -> T96 -> nine-target computation.

--seconds is the sum of three native compute caps: half for reconstructing the
T64 graph, the remaining budget less 60 seconds for T96, and 60 for target lift.
Each compilation separately has a 30-second/512-MiB cap. No shift scan/retry.
Large bases remain in --work. Receipts/logs and the gzip target certificate
alone go in --out; failed runs retain their actual last stage.
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
    with Path(path).open("rb") as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()

def read(path):
    return json.loads(path.read_text()) if path.exists() else {}

def main():
    p = argparse.ArgumentParser()
    for name in ("input", "mapping", "nf-receipt", "ann-receipt", "work", "out"):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--seconds", type=int, default=1800)
    p.add_argument("--memory-mib", type=int, default=4096)
    a = p.parse_args()
    if a.seconds < 900 or a.memory_mib < 256:
        raise ValueError("explicit full pipeline budget at least 900 seconds and 256 MiB required")
    a.work.mkdir(parents=True, exist_ok=True)
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    old_runner = root / "2026-11-14-r150-shifted-graph-module-runner-789f.py"
    reweight_runner = root / "2026-11-14-r150-reweighted-graph-module-runner-789f.py"
    target_runner = root / "2026-11-14-r150-reweighted-graph-target-lift-runner-789f.py"
    graph_seconds = a.seconds // 2
    target_seconds = 60
    reweight_seconds = a.seconds - graph_seconds - target_seconds
    before = time.monotonic()
    receipt = {
        "format": "r150-fixed-t96-full-original-target-lift-v1", "field": 31,
        "status": "t64-graph-running", "requestedNativeComputeSeconds": a.seconds,
        "t64HardSeconds": graph_seconds, "t64SoftSeconds": graph_seconds-60,
        "t96HardSeconds": reweight_seconds, "t96SoftSeconds": reweight_seconds-60,
        "targetLiftSeconds": target_seconds, "memoryMiBLimit": a.memory_mib,
        "inputSHA256": sha(a.input), "mappingSHA256": sha(a.mapping),
        "nfReceiptSHA256": sha(a.nf_receipt), "annReceiptSHA256": sha(a.ann_receipt),
        "runnerSHA256": sha(__file__), "t64RunnerSHA256": sha(old_runner),
        "t96RunnerSHA256": sha(reweight_runner), "targetRunnerSHA256": sha(target_runner),
        "outputs": {}
    }
    receipt_path = a.out / "full-lift-receipt.json"
    def save():
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    def copy_small(source, name):
        if source.exists():
            destination = a.out / name
            shutil.copyfile(source, destination)
            receipt["outputs"][name] = {"file": str(destination), "bytes": destination.stat().st_size, "sha256": sha(destination)}
    def stop(status):
        receipt.update(status=status, elapsedSeconds=time.monotonic()-before)
        save()
        print(json.dumps(receipt))
        raise SystemExit(1)
    save()
    old_dir = a.work / "t64"
    code = subprocess.call(["python3", str(old_runner), "--input", str(a.input), "--mapping", str(a.mapping),
        "--nf-receipt", str(a.nf_receipt), "--out", str(old_dir), "--seconds", str(graph_seconds),
        "--soft-seconds", str(graph_seconds-60), "--memory-mib", str(a.memory_mib)])
    old_path = old_dir / "shifted-graph-receipt.json"
    old = read(old_path)
    copy_small(old_path, "t64-graph-receipt.json")
    copy_small(old_dir / "graph-metadata.json", "t64-graph-metadata.json")
    copy_small(old_dir / "shifted-graph.log", "t64-graph.log")
    receipt.update(t64ExitCode=code, t64Status=old.get("status", "missing"))
    if code or old.get("status") not in ("completed", "full-graph-without-elimination"):
        stop("t64-graph-incomplete")
    receipt["status"] = "t96-reweighting-running"
    save()
    new_dir = a.work / "t96"
    code = subprocess.call(["python3", str(reweight_runner), "--graph", str(old_dir / "graph-basis.bin"),
        "--graph-receipt", str(old_path), "--input", str(a.input), "--nf-receipt", str(a.nf_receipt),
        "--out", str(new_dir), "--seconds", str(reweight_seconds), "--soft-seconds", str(reweight_seconds-60),
        "--memory-mib", str(a.memory_mib)])
    new_path = new_dir / "reweighted-graph-receipt.json"
    new = read(new_path)
    copy_small(new_path, "t96-graph-receipt.json")
    copy_small(new_dir / "reweighted-metadata.json", "t96-graph-metadata.json")
    copy_small(new_dir / "reweighted-graph.log", "t96-graph.log")
    receipt.update(t96ExitCode=code, t96Status=new.get("status", "missing"),
                   projectionSpanCertified=new.get("projectionSpanCertified", False))
    if code or not new.get("allOriginalGraphRowsProcessed") or new.get("status") not in (
            "completed", "full-graph-without-projection-certificate"):
        stop("t96-graph-incomplete")
    receipt["status"] = "nine-original-targets-running"
    save()
    target_dir = a.out / "target-lift"
    code = subprocess.call(["python3", str(target_runner), "--graph", str(new_dir / "reweighted-basis.bin"),
        "--graph-receipt", str(new_path), "--input", str(a.input), "--nf-receipt", str(a.nf_receipt),
        "--ann-receipt", str(a.ann_receipt), "--work", str(a.work / "target-lift"), "--out", str(target_dir),
        "--seconds", str(target_seconds), "--memory-mib", str(a.memory_mib)])
    target_path = target_dir / "target-lift-receipt.json"
    target = read(target_path)
    stats = target.get("nativeStatistics") or {}
    complete = (code == 0 and target.get("status") == "completed"
                and stats.get("status") == "original-nine-targets-low-degree-lift-complete"
                and stats.get("fullNormalFormSourceIdentity") is True
                and stats.get("allDegreeBoundsVerified") is True)
    receipt.update(status="completed" if complete else "t96-graph-complete-target-lift-incomplete",
        targetLiftStatus=target.get("status", "missing"), targetLiftExitCode=code,
        fullNormalFormSourceIdentity=complete, allDegreeBoundsVerified=complete,
        elapsedSeconds=time.monotonic()-before,
        sourceIdentity="All original T64 graph vectors are reweighted once at T96. Nonzero outputs of source-leading rows are never discarded during reweighting or called kernel rows. Final completion requires every coefficient of R*C=h31*T for all 2195 original NF sources and all nine original targets, with bounds 146-degree(R_j). Recovery to the original seventeen equations and characteristic-zero membership remain separate.")
    if target_path.exists():
        receipt["outputs"]["target-lift-receipt.json"] = {"file": str(target_path), "sha256": sha(target_path)}
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
