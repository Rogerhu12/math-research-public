#!/usr/bin/env python3
"""Bounded exact nine-target lift from the complete fixed T=96 graph."""
import argparse
import gzip
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
    p.add_argument("--graph", type=Path, required=True)
    p.add_argument("--graph-receipt", type=Path, required=True)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--nf-receipt", type=Path, required=True)
    p.add_argument("--ann-receipt", type=Path, required=True)
    p.add_argument("--work", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--seconds", type=int, default=60)
    p.add_argument("--memory-mib", type=int, default=512)
    a = p.parse_args()
    if a.seconds < 1 or a.memory_mib <= 0:
        raise ValueError("positive explicit bounds required")
    a.work.mkdir(parents=True, exist_ok=True)
    a.out.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parent
    source = root / "2026-11-14-r150-reweighted-graph-target-lift-789f.cpp"
    graph = json.loads(a.graph_receipt.read_text())
    nf = json.loads(a.nf_receipt.read_text())
    ann = json.loads(a.ann_receipt.read_text())
    input_hash = sha(a.input)
    if (graph["status"] not in ("completed", "full-graph-without-projection-certificate")
            or not graph.get("allOriginalGraphRowsProcessed")
            or graph.get("sourceShiftRule") != "degree(R_j)-96"
            or graph.get("maximumWeightedRowDegree") != 8
            or graph["nativeStatistics"]["processedSources"] != 2195
            or graph["nativeStatistics"]["outputLeadingRows"] != 1021
            or graph["nativeStatistics"]["sourceLeadingRows"] != 1174
            or input_hash != "eeba714c9a9675a8fdac31bf3cd105f50bc5b26de7940301549d903d964d3840"
            or graph["inputSHA256"] != input_hash
            or graph["outputs"]["basis.bin"]["sha256"] != sha(a.graph)
            or nf["status"] != "completed" or not nf["allSources"]
            or nf["outputs"]["normal-forms.bin"]["sha256"] != input_hash
            or ann["status"] != "completed" or ann["field"] != 31
            or [v["target"] for v in ann["targets"]] != list(range(2, 11))
            or ann["commonMinimum"]["degree"] != 24):
        raise ValueError("complete reweighted original graph and linked original target receipts required")
    coefficients = ann["commonMinimum"]["coefficientsAscending"]
    if len(coefficients) != 25 or coefficients[-1] != 1 or any(not 0 <= a < 31 for a in coefficients):
        raise ValueError("monic common h31")
    hfile = a.work / "common-h31.txt"
    hfile.write_text(" ".join(map(str, coefficients)) + "\n")
    receipt = {"format": "r150-reweighted-graph-target-lift-run-v2", "field": 31, "status": "preparing",
               "graphSHA256": sha(a.graph), "graphReceiptSHA256": sha(a.graph_receipt),
               "sourceShiftRule": "degree(R_j)-96", "maximumProductDegree": 146,
               "graphProjectionSpanCertified": graph.get("projectionSpanCertified", False),
               "graphSourceLeadingRowsWithNonzeroOutput": graph["nativeStatistics"]["sourceLeadingRowsWithNonzeroOutput"],
               "inputSHA256": input_hash, "nfReceiptSHA256": sha(a.nf_receipt),
               "annReceiptSHA256": sha(a.ann_receipt), "cppSHA256": sha(source),
               "arithmeticHeaderSHA256": sha(root / "2026-11-14-r150-f31-bitplane-789f.hpp"),
               "runnerSHA256": sha(__file__), "secondsLimit": a.seconds,
               "memoryMiBLimit": a.memory_mib, "outputs": {}}
    receipt_file = a.out / "target-lift-receipt.json"
    save = lambda: receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    binary = a.work / "graph-target-lift"
    result = subprocess.run(["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--", "g++", "-O3", "-std=c++17", str(source), "-o", str(binary)], capture_output=True, text=True)
    if result.returncode:
        receipt.update({"status": "compile-failed", "compileOutput": result.stdout + result.stderr})
        save()
        print(receipt["compileOutput"])
        raise SystemExit(1)
    receipt["binarySHA256"] = sha(binary)
    receipt["status"] = "running"
    save()
    prefix = a.work / "lift"
    before = time.monotonic()
    child = subprocess.Popen(["timeout", "--kill-after=10s", f"{a.seconds}s", "prlimit", f"--as={a.memory_mib*1024*1024}", "--core=0", "--", str(binary), str(a.graph), str(a.input), str(hfile), str(prefix)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    events = []
    with (a.out / "target-lift.log").open("w") as log:
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
    complete = code == 0 and last and last.get("status") == "original-nine-targets-low-degree-lift-complete" and last.get("fullNormalFormSourceIdentity") and last.get("allDegreeBoundsVerified")
    receipt.update({"status": "completed" if complete else "failed-or-incomplete", "exitCode": code,
                    "elapsedSeconds": time.monotonic()-before, "nativeStatistics": last})
    checkpoint = Path(str(prefix) + "-lift-checkpoint.bin")
    if not complete and checkpoint.exists():
        compressed_checkpoint = a.out / "lift-checkpoint.bin.gz"
        compressed_checkpoint.write_bytes(gzip.compress(checkpoint.read_bytes(), mtime=0))
        receipt["outputs"]["lift-checkpoint.bin"] = {
            "bytes": checkpoint.stat().st_size, "sha256": sha(checkpoint),
            "gzipFile": str(compressed_checkpoint), "gzipBytes": compressed_checkpoint.stat().st_size,
            "gzipSHA256": sha(compressed_checkpoint),
            "status": "all-nine-coefficients-computed-full-polynomial-verification-incomplete"}
    if complete:
        plain = Path(str(prefix) + "-original-coefficients.bin")
        compressed = a.out / "original-coefficients.bin.gz"
        compressed.write_bytes(gzip.compress(plain.read_bytes(), mtime=0))
        if compressed.stat().st_size > 5000000:
            raise ValueError("coefficient artifact exceeded repository limit")
        receipt["outputs"]["original-coefficients.bin"] = {"bytes": plain.stat().st_size, "sha256": sha(plain),
                                                          "gzipFile": str(compressed), "gzipBytes": compressed.stat().st_size,
                                                          "gzipSHA256": sha(compressed)}
        metadata = a.out / "original-coefficients.json"
        shutil.copyfile(Path(str(prefix) + "-original-coefficients.json"), metadata)
        receipt["outputs"]["metadata"] = {"file": str(metadata), "bytes": metadata.stat().st_size, "sha256": sha(metadata)}
    save()
    print(json.dumps(receipt))
    if not complete:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
